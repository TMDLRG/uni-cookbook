# -*- coding: utf-8 -*-
"""test_reader.py -- the reader's own falsifiers.

    python reader/test_reader.py

Python 3 stdlib unittest ONLY. No pip, no pytest, no fixtures directory.

WHAT THIS SUITE IS FOR
----------------------
Every invariant the reader claims is claimed on a page that a reader can see:
"READ-ONLY", "ASCII-ONLY", "PROVENANCE OR NO PAGE", "NO EXTERNAL NETWORK
REFERENCES". A claim without a falsifier is inadmissible. This file is the
falsifier for each of them, and it is the reason those claims may be made at
all.

THE INSTRUMENT IS SCOPED ON PURPOSE, AND THAT IS THE WHOLE CRAFT OF IT
----------------------------------------------------------------------
Two of these tests are easy to write WRONG in a way that passes loudly and
measures nothing, or fails loudly and measures the wrong thing. Both mistakes
were made during development and both are documented at the test that fixes
them:

  * test_no_external_refs must not grep for the substring "http". Every plate
    SVG carries xmlns="http://www.w3.org/2000/svg" -- a namespace IDENTIFIER
    that is never dereferenced -- and the corpus cites DOIs as <a href> links,
    which are user-initiated navigation, not assets the page loads. A bare
    "http" grep flags all of them and would push a "fix" that strips the
    corpus's own citations. It tests FETCHING CONSTRUCTS instead.

  * test_no_perfect_claims must not grep the whole page for "perfect" or
    "verified". Measured on the built site: 29 occurrences of "perfect" and
    1054 of "verified" -- every one of them CORPUS PROSE, in the corpus's own
    voice ("nature did not build one perfect component", CN-05). The corpus is
    quoted; it is not this reader speaking. "proven" is likewise the CLAIM-
    LEDGER's own legitimate vocabulary for UNI's build status. A page-wide grep
    would fire on all of it and the only way to make it pass would be to censor
    the repo -- which breaks "always the real as-is repo knowledge", the thing
    the reader exists to keep. So that test reads the READER'S OWN AUTHORED
    STRINGS (via ast, from build.py and templates.py) and the reader's own
    chrome. SIGNUM SIGNUM MANET: the signal and the commentary about it travel
    separately, and so do the corpus's voice and the reader's.

A negative result is a HYPOTHESIS until a positive control shows the instrument
can fire. Every fence test below therefore carries a positive control: a
deliberate violation the test must catch. A fence that has never been shown to
fire is not a fence, it is a decoration.

WHAT THIS SUITE DOES NOT CLAIM
------------------------------
It does not claim the reader is secure, correct, or complete. It claims exactly
what each test observes, and no more. Where a path is not exercised by the real
corpus (the PENDING path -- the corpus is complete today, so no chapter is
missing), the test exercises it directly and SAYS that is what it did.
"""

import ast
import builtins
import hashlib
import html as html_mod
import io
import json
import os
import re
import shutil
import sys
import unittest

READER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(READER)
DIST = os.path.join(READER, "dist")

sys.path.insert(0, READER)

import build           # noqa: E402
import markdown as md  # noqa: E402
import templates       # noqa: E402


# ---------------------------------------------------------------------------
# One build for the whole suite, instrumented at the mutation surface.
# ---------------------------------------------------------------------------

PAGES = {}          # dist-relative url -> text (ascii)
FILES = []          # every file in dist
MUTATIONS = []      # (op, abs_path) every mutating call the build made
CORPUS_BEFORE = {}  # repo digest before the build
CORPUS_AFTER = {}   # repo digest after the build
BUILD_STDOUT = ""

_WRITE_MODE = re.compile(r"[wax+]")


def _digest_corpus():
    """sha256 every file in the repo EXCEPT .git and reader/dist.

    reader/dist is the build's output and is expected to change; .git is git's
    own state and `git status` may touch its index while the build reads it.
    Everything else is the corpus, and the corpus must be byte-identical across
    a build. This is the empirical form of the read-only claim: not "the code
    looks like it only reads" but "the bytes did not move".
    """
    out = {}
    dist_real = os.path.realpath(DIST)
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d != ".git"
                 and os.path.realpath(os.path.join(dp, d)) != dist_real
                 and d != "__pycache__"]
        for f in sorted(fn):
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
            try:
                with open(p, "rb") as fh:
                    out[rel] = hashlib.sha256(fh.read()).hexdigest()
            except OSError:
                out[rel] = "UNREADABLE"
    return out


def _inside_dist(path):
    t = os.path.realpath(path)
    d = os.path.realpath(DIST)
    return t == d or t.startswith(d + os.sep)


def setUpModule():
    """Run ONE real build, with every mutation door instrumented.

    The build is not mocked and the corpus is not copied: this is the actual
    generator running against the actual repo, which is the only thing worth
    testing. What is instrumented is the set of calls that could MUTATE
    something -- open() in a write mode, rmtree, remove, rename, mkdir. Every
    one is recorded with its target, and test_readonly_invariant asserts on the
    record.
    """
    global CORPUS_BEFORE, CORPUS_AFTER, BUILD_STDOUT

    CORPUS_BEFORE = _digest_corpus()

    real_open = builtins.open
    real_rmtree = shutil.rmtree
    real_remove = os.remove
    real_unlink = os.unlink
    real_rename = os.rename
    real_makedirs = os.makedirs
    real_mkdir = os.mkdir

    def rec_open(file, mode="r", *a, **k):
        if _WRITE_MODE.search(str(mode)):
            try:
                MUTATIONS.append(("open(%s)" % mode, os.path.realpath(file)))
            except TypeError:
                MUTATIONS.append(("open(%s)" % mode, repr(file)))
        return real_open(file, mode, *a, **k)

    def _wrap(op, fn):
        def inner(path, *a, **k):
            try:
                MUTATIONS.append((op, os.path.realpath(path)))
            except TypeError:
                MUTATIONS.append((op, repr(path)))
            return fn(path, *a, **k)
        return inner

    builtins.open = rec_open
    shutil.rmtree = _wrap("rmtree", real_rmtree)
    os.remove = _wrap("remove", real_remove)
    os.unlink = _wrap("unlink", real_unlink)
    os.rename = _wrap("rename", real_rename)
    os.makedirs = _wrap("makedirs", real_makedirs)
    os.mkdir = _wrap("mkdir", real_mkdir)

    cap = io.StringIO()
    real_stdout = sys.stdout
    try:
        sys.stdout = cap
        rc = build.main(["--quiet"])
    finally:
        sys.stdout = real_stdout
        builtins.open = real_open
        shutil.rmtree = real_rmtree
        os.remove = real_remove
        os.unlink = real_unlink
        os.rename = real_rename
        os.makedirs = real_makedirs
        os.mkdir = real_mkdir

    BUILD_STDOUT = cap.getvalue()
    if rc != 0:
        raise AssertionError("build.main() returned %r; the suite cannot run "
                             "against a build that did not complete." % rc)

    CORPUS_AFTER = _digest_corpus()

    for dp, dn, fn in os.walk(DIST):
        for f in sorted(fn):
            p = os.path.join(dp, f)
            FILES.append(p)
            rel = os.path.relpath(p, DIST).replace(os.sep, "/")
            with open(p, "rb") as fh:
                raw = fh.read()
            if rel.endswith(".html"):
                PAGES[rel] = raw.decode("ascii", "replace")

    if not PAGES:
        raise AssertionError("the build emitted no HTML pages; nothing to test.")


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

_TAG_RE = re.compile(r"<[^>]+>")
_SCRIPT_RE = re.compile(r"<script\b[^>]*>.*?</script>", re.S | re.I)
_STYLE_RE = re.compile(r"<style\b[^>]*>.*?</style>", re.S | re.I)


def page_text(html):
    """Visible text of a page: tags gone, entities resolved, whitespace flat.

    Script and style blocks are removed FIRST: their contents are code, not
    prose, and leaving them in would let a JS string satisfy a fidelity or
    claim test that the visible page does not.
    """
    s = _SCRIPT_RE.sub(" ", html)
    s = _STYLE_RE.sub(" ", s)
    s = _TAG_RE.sub(" ", s)
    s = html_mod.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def reader_authored_strings():
    """Every string literal the reader's own modules author, via ast.

    This is the reader's VOICE: what it says in its own name. It is not the
    corpus's voice, which the reader only carries. Docstrings are excluded --
    they are addressed to a builder reading the source, never rendered to a
    page, and they legitimately QUOTE the banned words in order to ban them.
    """
    out = []
    for mod in ("build.py", "templates.py", "markdown.py"):
        path = os.path.join(READER, mod)
        with open(path, "rb") as fh:
            tree = ast.parse(fh.read().decode("utf-8"), filename=mod)
        docstrings = set()
        for node in ast.walk(tree):
            if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef,
                                 ast.ClassDef)):
                d = ast.get_docstring(node, clean=False)
                if d:
                    docstrings.add(d)
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                if node.value in docstrings:
                    continue
                out.append((mod, getattr(node, "lineno", 0), node.value))
    return out


# ---------------------------------------------------------------------------
# 1. READ-ONLY
# ---------------------------------------------------------------------------


class TestReadOnlyInvariant(unittest.TestCase):
    """The hard invariant: the generator reads the corpus and cannot change it."""

    def test_readonly_invariant(self):
        # (a) Observed: every mutating call the build made targeted dist.
        self.assertTrue(MUTATIONS, "no mutating calls were recorded at all -- "
                                   "the instrument did not run; this is a "
                                   "broken test, not a passing invariant.")
        outside = [(op, p) for op, p in MUTATIONS if not _inside_dist(p)]
        self.assertEqual(
            [], outside,
            "READ-ONLY VIOLATION: the build mutated %d path(s) outside "
            "reader/dist/:\n%s" % (len(outside), "\n".join(
                "  %s -> %s" % (op, p) for op, p in outside[:20])))

        # (b) Observed: the corpus bytes did not move. The empirical claim.
        self.assertEqual(
            set(CORPUS_BEFORE), set(CORPUS_AFTER),
            "the build added or removed corpus files: added=%r removed=%r"
            % (sorted(set(CORPUS_AFTER) - set(CORPUS_BEFORE))[:10],
               sorted(set(CORPUS_BEFORE) - set(CORPUS_AFTER))[:10]))
        changed = [k for k in CORPUS_BEFORE if CORPUS_BEFORE[k] != CORPUS_AFTER[k]]
        self.assertEqual([], changed,
                         "READ-ONLY VIOLATION: %d corpus file(s) changed across "
                         "the build: %r" % (len(changed), changed[:10]))

    def test_readonly_write_door_is_guarded(self):
        """Positive control: the guard must actually refuse. A fence that has
        never been shown to fire is a decoration, not a fence."""
        with self.assertRaises(AssertionError):
            build._assert_inside_dist(os.path.join(ROOT, "README.md"))
        with self.assertRaises(AssertionError):
            build._assert_inside_dist(os.path.join(DIST, "..", "..", "escape.txt"))
        # And it must ALLOW a legitimate target, or it is refusing everything
        # and proves nothing.
        self.assertTrue(build._assert_inside_dist(os.path.join(DIST, "ok.html")))

    def test_readonly_no_write_modes_in_source(self):
        """Static: no module opens anything in a write mode except the one door.

        build.py's _write_bytes is the single permitted writer. This reads the
        source rather than trusting the docstring that says so.
        """
        offenders = []
        for mod in ("build.py", "templates.py", "markdown.py", "test_reader.py"):
            path = os.path.join(READER, mod)
            with open(path, "rb") as fh:
                tree = ast.parse(fh.read().decode("utf-8"), filename=mod)
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                fn = node.func
                name = getattr(fn, "id", None) or getattr(fn, "attr", None)
                if name != "open":
                    continue
                mode = None
                if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                    mode = node.args[1].value
                for kw in node.keywords:
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = kw.value.value
                if mode and _WRITE_MODE.search(str(mode)):
                    offenders.append("%s:%d open(mode=%r)"
                                     % (mod, node.lineno, mode))
        # build.py:_write_bytes and this test file's own tmp writes are the
        # only permitted ones; they are named explicitly so a NEW one is a
        # failure rather than a silent addition.
        allowed = {"build.py", "test_reader.py"}
        unexpected = [o for o in offenders if o.split(":")[0] not in allowed]
        self.assertEqual([], unexpected,
                         "a module that must never write opened a write mode: %r"
                         % unexpected)

    def test_readonly_templates_and_markdown_do_no_io(self):
        """templates.py and markdown.py must have no file I/O at all."""
        for mod in ("templates.py", "markdown.py"):
            path = os.path.join(READER, mod)
            with open(path, "rb") as fh:
                src = fh.read().decode("utf-8")
            tree = ast.parse(src, filename=mod)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    name = (getattr(node.func, "id", None)
                            or getattr(node.func, "attr", None))
                    self.assertNotIn(
                        name, ("open", "remove", "rmtree", "rename", "mkdir",
                               "makedirs", "system", "popen"),
                        "%s:%d calls %s(); this module must have no I/O."
                        % (mod, node.lineno, name))
            for node in ast.walk(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    names = [a.name.split(".")[0] for a in node.names]
                    for n in names:
                        self.assertNotIn(
                            n, ("subprocess", "socket", "urllib", "requests",
                                "http", "shutil"),
                            "%s imports %r; this module must not reach the "
                            "filesystem or the network." % (mod, n))


# ---------------------------------------------------------------------------
# 2. ASCII-ONLY
# ---------------------------------------------------------------------------


class TestAsciiOnlyOutput(unittest.TestCase):
    """Deployment depends on this: MCP os_file_write corrupts multi-byte UTF-8."""

    def test_ascii_only_output(self):
        bad = []
        for p in FILES:
            with open(p, "rb") as fh:
                raw = fh.read()
            for i, b in enumerate(raw):
                if b > 0x7F:
                    bad.append("%s: byte 0x%02X at offset %d"
                               % (os.path.relpath(p, DIST), b, i))
                    break
        self.assertEqual([], bad,
                         "ASCII VIOLATION in %d file(s). The fleet's only file "
                         "transport silently corrupts multi-byte UTF-8, so a "
                         "non-ASCII byte here is a deployment defect:\n%s"
                         % (len(bad), "\n".join(bad[:10])))
        self.assertGreater(len(FILES), 1, "no files were checked")

    def test_ascii_preserves_the_glyph(self):
        """ASCII-safety must not DELETE the character -- it must reference it.

        A build that dropped every Devanagari glyph would pass a naive
        byte check while destroying the lexicon. So: the reference must be
        present and must decode back to the original character.
        """
        s = templates.to_ascii(u"अ — θ")
        self.assertNotIn("?", s, "to_ascii() replaced a glyph instead of "
                                 "referencing it -- the character is lost.")
        self.assertEqual(u"अ — θ", html_mod.unescape(s),
                         "to_ascii() is not reversible; the glyph did not "
                         "survive the transport.")
        # And the real pages must carry real references, not stripped text.
        joined = "".join(PAGES.values())
        self.assertRegex(joined, r"&#\d+;",
                         "no numeric character reference appears anywhere in "
                         "the built site; either the corpus lost its non-ASCII "
                         "content or the encoder is dropping it.")


# ---------------------------------------------------------------------------
# 3. NO EXTERNAL REFERENCES
# ---------------------------------------------------------------------------

# Fetching constructs ONLY. See the module docstring for why this is not a
# grep for "http": the plate SVGs' xmlns and the corpus's DOI citations are
# both legitimate and neither is fetched.
_FETCH_PATTERNS = (
    # REMOTE <script src> only. Same-origin relative sources (e.g. app.js
    # loaded from the DIST root) are the OFFLINE-FIRST shape the fence is
    # written to protect, not to forbid. Mirrors build.py's
    # _MARKUP_REF_PATTERNS. Positive control below asserts that both
    # `https://...` and protocol-relative `//host/...` still trip this.
    (re.compile(r"""<\s*script[^>]*\ssrc\s*=\s*['"]?\s*(?:https?:)?//""", re.I),
     "remote <script src>"),
    (re.compile(r"""<\s*link[^>]*href\s*=\s*['"]?\s*(?:https?:)?//""", re.I),
     "remote <link href>"),
    (re.compile(r"""<\s*img[^>]*src\s*=\s*['"]?\s*(?:https?:)?//""", re.I),
     "remote <img src>"),
    (re.compile(r"<\s*iframe", re.I), "<iframe>"),
    (re.compile(r"\ssrcset\s*=", re.I), "srcset"),
    (re.compile(r"<\s*(?:audio|video|embed|object)\b", re.I), "embedded media"),
    (re.compile(r"@import", re.I), "@import"),
    (re.compile(r"""url\(\s*['"]?\s*(?:https?:)?//""", re.I), "remote url()"),
    (re.compile(r"""<\s*use[^>]+(?:xlink:)?href\s*=\s*['"]\s*https?:""", re.I),
     "remote <use>"),
)

_SVG_NS = 'xmlns="http://www.w3.org/2000/svg"'
_CSS_COMMENT = re.compile(r"/\*.*?\*/", re.S)
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)


class TestNoExternalRefs(unittest.TestCase):
    """Offline-first: the built site must fetch nothing, ever."""

    def _scan(self, text, css=False):
        """Independent of build.fence_scan -- a test that called the code under
        test would only prove the scanner agrees with itself."""
        hits = []
        if css:
            hay = _CSS_COMMENT.sub(" ", text)
            styles = [hay]
            markup = ""
        else:
            markup = _HTML_COMMENT.sub(" ", text.replace(_SVG_NS, ""))
            styles = [_CSS_COMMENT.sub(" ", b) for b in
                      re.findall(r"<style[^>]*>(.*?)</style>", text, re.S | re.I)]
        for rx, what in _FETCH_PATTERNS:
            # @import and url() are live only inside a style context; in body
            # prose '@import' is six inert characters (PL-01's design_fence note
            # literally contains the words "no @import").
            if what in ("@import", "remote url()"):
                for block in styles:
                    if rx.search(block):
                        hits.append(what)
                continue
            if markup and rx.search(markup):
                hits.append(what)
        return hits

    def test_no_external_refs(self):
        bad = {}
        for url, text in PAGES.items():
            hits = self._scan(text)
            if hits:
                bad[url] = hits
        self.assertEqual({}, bad,
                         "EXTERNAL REFERENCE(S) in the built site: %r" % bad)

        css = os.path.join(DIST, "theme.css")
        if os.path.exists(css):
            with open(css, "rb") as fh:
                hits = self._scan(fh.read().decode("ascii", "replace"), css=True)
            self.assertEqual([], hits, "theme.css reaches the network: %r" % hits)

    def test_no_external_refs_positive_control(self):
        """The instrument must fire on a real violation, or it measures nothing.

        The relaxed `<script src>` pattern (permitting same-origin relative
        sources) still fires on the two remote shapes the fence was written
        to reject: an explicit `https://` URL and a protocol-relative `//host`
        URL. Both are the fence's actual failure modes; both are tested.
        """
        self.assertIn("remote <script src>",
                      self._scan('<script src="https://cdn.example/x.js"></script>'))
        self.assertIn("remote <script src>",
                      self._scan('<script src="//evil.example/x.js"></script>'))
        self.assertIn("remote <link href>",
                      self._scan('<link rel="stylesheet" href="https://f/x.css">'))
        self.assertIn("@import", self._scan("<style>@import url(x);</style>"))
        self.assertIn("remote url()",
                      self._scan("<style>a{background:url(//evil/x.png)}</style>"))

    def test_no_external_refs_does_not_fire_on_the_legitimate(self):
        """The other half of the control: it must NOT fire on the innocent.

        These four are the exact false positives that were observed during
        development. Each would push a 'fix' that damages the corpus.
        """
        self.assertEqual([], self._scan('<svg %s><path d="M0 0"/></svg>' % _SVG_NS),
                         "fired on the SVG namespace identifier (never fetched)")
        self.assertEqual([], self._scan('<a href="https://doi.org/10.1234/x">cite</a>'),
                         "fired on a DOI citation link (user-initiated navigation, "
                         "not an asset the page loads)")
        self.assertEqual([], self._scan("<p>the fence forbids @import and url(//x)</p>"),
                         "fired on escaped prose that DESCRIBES the fence")
        self.assertEqual([], self._scan("/* NO CDN. NO @import. */\nbody{color:red}",
                                        css=True),
                         "fired on a CSS comment stating the fence it keeps")
        # Same-origin, relative <script src> is what the runtime ships:
        # <script src="app.js">, <script src="../app.js">. These are the
        # offline-first shape the fence protects, not what it forbids.
        self.assertEqual([], self._scan('<script src="app.js" defer></script>'),
                         "fired on a same-origin relative <script src>; that "
                         "is the shape the reader emits for its own runtime")
        self.assertEqual([], self._scan('<script src="../app.js" defer></script>'),
                         "fired on a ../-prefixed relative <script src>; that "
                         "is the shape a deeper page emits for its runtime")

    def test_no_network_capable_code_in_pages(self):
        """The inline scripts are a theme toggle and a filter. No fetching."""
        for url, text in PAGES.items():
            for block in re.findall(r"<script[^>]*>(.*?)</script>", text,
                                    re.S | re.I):
                if "application/json" in text[:0]:  # data blocks handled below
                    continue
                for bad in ("fetch(", "XMLHttpRequest", "WebSocket",
                            "importScripts", "navigator.sendBeacon", "eval("):
                    self.assertNotIn(bad, block,
                                     "%s: inline script uses %s" % (url, bad))


# ---------------------------------------------------------------------------
# 4. PROVENANCE
# ---------------------------------------------------------------------------


class TestProvenancePresent(unittest.TestCase):
    """A page that cannot state its provenance does not render."""

    def test_provenance_present(self):
        missing = []
        for url, text in PAGES.items():
            t = page_text(text)
            if 'class="prov__path"' not in text:
                missing.append("%s: no source path" % url)
            if 'class="prov__commit"' not in text:
                missing.append("%s: no commit" % url)
            if 'class="prov__utc"' not in text:
                missing.append("%s: no built UTC" % url)
            if 'class="prov__sha"' not in text and 'class="prov__absent"' not in text:
                missing.append("%s: no sha256 and no honest ABSENT marker" % url)
            if "Provenance" not in t:
                missing.append("%s: no provenance block" % url)
        self.assertEqual([], missing,
                         "%d page(s) cannot state their provenance:\n%s"
                         % (len(missing), "\n".join(missing[:15])))

    def test_provenance_refuses_to_half_stamp(self):
        """Positive control at BOTH locks (build.py and templates.py)."""
        good = {"source_path": "x.md", "sha256": "a" * 64,
                "commit": "deadbeef", "built_utc": "2026-07-16T00:00:00Z"}
        for drop in ("source_path", "commit", "built_utc", "sha256"):
            p = dict(good)
            p.pop(drop)
            with self.assertRaises(templates.ProvenanceError,
                                   msg="templates rendered a page missing %r" % drop):
                templates.render_page("colophon", {"title": "x", "provenance": p})
        with self.assertRaises(templates.ProvenanceError):
            templates.render_page("colophon", {"title": "x"})
        # sha256 may be dropped ONLY for a pending page -- there are no bytes.
        p = dict(good)
        p.pop("sha256")
        out = templates.render_page("chapter", {"title": "x", "provenance": p,
                                                "pending": True,
                                                "pending_reason": "absent"})
        self.assertIn("ABSENT", out)

    def test_provenance_sha256_is_the_real_digest(self):
        """THE load-bearing test of 'always the real as-is repo knowledge'.

        Every page names a source file and a sha256. Hash the named file and
        compare. If a page ever rendered from a cached or hand-copied
        duplicate, this is what catches it.
        """
        checked, bad = 0, []
        for url, text in PAGES.items():
            m_path = re.search(r'<code class="prov__path">([^<]+)</code>', text)
            m_sha = re.search(r'<code class="prov__sha">([0-9a-f]{64})</code>', text)
            if not m_path or not m_sha:
                continue
            rel = html_mod.unescape(m_path.group(1))
            src = os.path.join(ROOT, rel.replace("/", os.sep))
            if not os.path.exists(src):
                bad.append("%s: names source %r which does not exist" % (url, rel))
                continue
            with open(src, "rb") as fh:
                real = hashlib.sha256(fh.read()).hexdigest()
            if real != m_sha.group(1):
                bad.append("%s: claims sha256 %s for %s, actual %s"
                           % (url, m_sha.group(1)[:12], rel, real[:12]))
            checked += 1
        self.assertEqual([], bad, "provenance is not the truth:\n%s"
                         % "\n".join(bad[:10]))
        self.assertGreater(checked, 50,
                           "only %d pages carried a checkable sha256; the test "
                           "is not measuring the site." % checked)

    def test_provenance_commit_does_not_overclaim(self):
        """An untracked file must NOT be stamped as if it were in the commit.

        lexicon/ and reader/plates/ are untracked at the time of writing.
        Stamping 'commit f1be794' beside them without qualification would
        assert their bytes are in that commit, which is false.
        """
        offenders = []
        for url, text in PAGES.items():
            m_path = re.search(r'<code class="prov__path">([^<]+)</code>', text)
            m_commit = re.search(r'<code class="prov__commit">([^<]*)</code>', text)
            if not m_path or not m_commit:
                continue
            rel = html_mod.unescape(m_path.group(1))
            state = build.GIT.file_state(rel)
            commit_txt = html_mod.unescape(m_commit.group(1))
            if state in ("untracked", "modified", "unknown"):
                if "NOTE:" not in commit_txt:
                    offenders.append("%s: source %s is %s but the commit stamp "
                                     "carries no qualifier" % (url, rel, state))
        self.assertEqual([], offenders, "\n".join(offenders[:10]))


# ---------------------------------------------------------------------------
# 5. CORPUS FIDELITY
# ---------------------------------------------------------------------------


class TestCorpusFidelity(unittest.TestCase):
    """The page must carry the file's ACTUAL sentences, not a summary of them."""

    def _plain_sentences(self, source, limit=6):
        """Lines that are plain prose: no markdown, no table, no code.

        Only these can be compared literally, because the renderer legitimately
        transforms everything else. Comparing a line containing '**' against
        rendered HTML would test the test, not the reader.
        """
        out = []
        for line in source.split("\n"):
            s = line.strip()
            if len(s) < 60 or len(s) > 400:
                continue
            if re.search(r"[|`*_#>\[\]<>]|^\s*[-+]\s|^\s*\d+[.)]\s", s):
                continue
            if s.startswith("---") or "  " in s:
                continue
            out.append(re.sub(r"\s+", " ", s))
            if len(out) >= limit:
                break
        return out

    def test_corpus_fidelity(self):
        checked, bad = 0, []
        for url, text in PAGES.items():
            if not url.startswith(("chapter/", "ledger/")):
                continue
            m = re.search(r'<code class="prov__path">([^<]+)</code>', text)
            if not m:
                continue
            rel = html_mod.unescape(m.group(1))
            src = os.path.join(ROOT, rel.replace("/", os.sep))
            if not os.path.exists(src):
                continue
            with open(src, "rb") as fh:
                source = fh.read().decode("utf-8")
            sentences = self._plain_sentences(source)
            if not sentences:
                continue
            rendered = page_text(text)
            for s in sentences:
                if s not in rendered:
                    bad.append("%s (from %s): the source sentence is not on the "
                               "page:\n    %r" % (url, rel, s[:150]))
                    break
            checked += 1
        self.assertEqual([], bad, "the reader is not carrying the corpus:\n%s"
                         % "\n".join(bad[:6]))
        self.assertGreater(checked, 40,
                           "only %d chapters were fidelity-checked; the test is "
                           "not measuring the corpus." % checked)

    def test_corpus_fidelity_positive_control(self):
        """The comparison must be able to fail. A sentence NOT in the corpus
        must not be found on a page built from the corpus."""
        joined = " ".join(page_text(t) for t in PAGES.values())
        self.assertNotIn(
            "This sentence was fabricated by the reader's own test suite and "
            "appears in no file of this repository.", joined)

    def test_every_chapter_reaches_a_page(self):
        """No chapter may vanish silently -- the failure this corpus refuses.

        Two chapters whose ids slugged the same silently overwrote each other
        during development: the build reported 98 pages into 95 files. Count
        the corpus's .md files and account for every one.
        """
        found = build.discover_chapters()
        self.assertTrue(found, "discover_chapters() found no chapters")
        urls = build.allocate_urls(found)
        self.assertEqual(len(set(urls.values())), len(urls),
                         "two chapters share a url; one would overwrite the other")
        for e in found:
            url = urls[e["rel"]]
            self.assertIn(url, PAGES,
                          "%s allocated url %r but no such page was emitted"
                          % (e["rel"], url))

    def test_numbers_rows_carry_all_six(self):
        """Every number carries value + units + scope + class + source +
        falsifier. That is the house rule; this counts it on the built page."""
        rows = 0
        for url, text in PAGES.items():
            rows += len(re.findall(r'<td class="num__fals">', text))
        self.assertGreater(rows, 100,
                           "only %d numbers rows reached the site; the corpus "
                           "has ~918." % rows)
        # Scoped to CHAPTER numbers tables. A plate page reuses class="num" for
        # its own claims table, whose cells are pc__ref / pc__sym / ... -- a
        # different table with a Ref column, not a defective numbers table. An
        # earlier version keyed on class="num" and failed on every plate page,
        # which would have pushed a 'fix' to the wrong table entirely.
        for url, text in PAGES.items():
            if 'class="numbers"' not in text:
                continue
            for cell in ("num__sym", "num__val", "num__units", "num__scope",
                         "num__class", "num__source", "num__fals"):
                self.assertIn(cell, text,
                              "%s renders a numbers table without a %s column"
                              % (url, cell))

    def test_numbers_cells_render_their_markdown(self):
        """Every numbers cell renders the corpus's inline markdown.

        units and scope were passed as RAW SOURCE and escaped as plain text, so
        a real cell -- '**ideal** regular tetrahedron' -- printed its asterisks
        at the reader while value, source and falsifier beside it rendered
        properly. Lossless, but the corpus wrote emphasis and the page showed
        punctuation.
        """
        # The probe is '**' and a backtick ONLY -- never a lone underscore.
        # An earlier version also flagged '(?<!\w)_\w' and fired on two cells
        # that were rendering perfectly well: 'λ_eff' and 'ε_r'. ASCII-safe
        # emission turns the Greek letter into '&#955;', so the subscript's
        # underscore ends up preceded by ';' and LOOKS like an opening
        # emphasis delimiter. Those underscores are correct and load-bearing --
        # markdown.py refuses intra-word '_' precisely so the corpus's
        # identifiers survive -- and 'fixing' them would delete the subscripts
        # from the science.
        stars = []
        for url, text in PAGES.items():
            if 'class="numbers"' not in text:
                continue
            for cellcls in ("num__units", "num__scope", "num__val"):
                for m in re.finditer(r'<td class="%s">(.*?)</td>' % cellcls,
                                     text, re.S):
                    if re.search(r"\*\*|`", m.group(1)):
                        stars.append("%s %s: %r" % (url, cellcls, m.group(1)[:70]))
        self.assertEqual([], stars,
                         "%d numbers cell(s) show raw markdown punctuation "
                         "instead of rendering it:\n%s"
                         % (len(stars), "\n".join(stars[:6])))

    def test_plate_claims_carry_all_six(self):
        """The plate claims table is the OTHER table that must carry the six."""
        for url, text in PAGES.items():
            if 'class="pclaims"' not in text:
                continue
            for cell in ("pc__sym", "pc__val", "pc__units", "pc__scope",
                         "pc__class", "pc__source", "pc__fals"):
                self.assertIn(cell, text,
                              "%s renders a claims table without a %s column"
                              % (url, cell))


# ---------------------------------------------------------------------------
# 6. ESCAPING
# ---------------------------------------------------------------------------


class TestEscaping(unittest.TestCase):
    """A corpus about honesty must not ship an XSS hole.

    Escaping here is also FIDELITY: the corpus contains angle-bracket text that
    is prose, not markup ('<sha>', '<r-bar>'). Passing HTML through would let
    the browser eat those words -- deleting them from the page.
    """

    def test_escaping(self):
        evil = '<script>alert("xss")</script> & <img src=x onerror=alert(1)>'
        out = md.render(evil)
        # The test is that no LIVE tag exists -- not that the letters are gone.
        # An earlier version of this test asserted `'onerror=' not in out` and
        # failed on the CORRECT output, because the whole string is escaped to
        # text and the word 'onerror=' legitimately appears as prose inside
        # '&lt;img src=x onerror=alert(1)&gt;'. Demanding its absence would have
        # demanded the renderer DELETE the corpus's characters -- the opposite
        # of what escaping is for. So: assert there is no unescaped '<'.
        self.assertNotIn("<script", out.lower())
        self.assertNotIn("<img", out.lower())
        self.assertIn("&lt;script&gt;", out)
        self.assertIn("&lt;img", out)
        self.assertIn("&amp;", out)
        # No raw '<' survives except the <p> the renderer itself opened.
        self.assertEqual(["<p>", "</p>"], re.findall(r"</?p>", out))
        self.assertEqual(2, out.count("<"), "an unescaped '<' reached the "
                                            "output: %r" % out)

    def test_escaping_is_fidelity(self):
        """The words must SURVIVE, not merely be neutralised."""
        out = md.render("The receipt is <sha> for the run.")
        self.assertIn("&lt;sha&gt;", out)
        self.assertIn("sha", page_text(out))

    def test_escaping_in_tables_and_code(self):
        out = md.render("| A |\n|---|\n| <b>x</b> |")
        self.assertNotIn("<b>", out)
        self.assertIn("&lt;b&gt;", out)
        out = md.render("```\n<script>bad()</script>\n```")
        self.assertNotIn("<script>", out)

    def test_escaping_via_templates(self):
        """templates.esc() is the other escaping door."""
        self.assertEqual("&lt;script&gt;", templates.esc("<script>"))
        self.assertEqual("&amp;", templates.esc("&"))
        self.assertEqual("&quot;", templates.esc('"'))
        self.assertEqual("&#39;", templates.esc("'"))

    def test_no_unescaped_html_from_corpus_reached_a_page(self):
        """Whole-site check: no page carries a script element other than the
        reader's own known, inline, network-free ones.

        A <script type="application/json"> is a DATA block, not code: the
        browser does not execute it. search.html ships the concordance that way.
        It is checked as data (it must parse as JSON, and must not be able to
        break out of its own element), not against the code allowlist -- an
        earlier version looked for the marker in the script BODY, found the raw
        JSON payload there, and reported the site's own search index as an
        unrecognised script.
        """
        known = ("uni-reader-theme", "themetoggle", "getElementById('filter')",
                 "getElementById('searchdata')", "getElementById('q')",
                 # scrivener/index.html inlines reader/scrivener/app.js -- an
                 # IndexedDB-only note-taker with no fetch/XHR/WebSocket
                 # (test_scrivener_is_client_only asserts this on the emitted
                 # file). The DB name is the unforgeable marker.
                 "cookbook.scrivener",
                 # templates._SW_REGISTER_JS -- the PWA service-worker
                 # registration inlined into every page's <head>. Same-origin,
                 # capability-guarded, no fetch.
                 "serviceWorker.register")
        # Same-origin, relative <script src> is permitted (this is how app.js
        # is wired into every page). A REMOTE src is not; the fence in
        # build.fence_scan() and test_no_external_refs already catch it.
        # Here we check the per-tag attribute directly to keep a second
        # observer on the invariant.
        _remote_src_re = re.compile(
            r"""src\s*=\s*['"]?\s*(?:https?:)?//""", re.I)
        for url, text in PAGES.items():
            for m in re.finditer(r"<script([^>]*)>(.*?)</script>", text, re.S | re.I):
                attrs, body = m.group(1), m.group(2)
                self.assertIsNone(_remote_src_re.search(attrs),
                                  "%s: a REMOTE <script src> reached a page: %r"
                                  % (url, attrs[:120]))
                if "src=" in attrs.lower():
                    # A src'd script has no body of its own; the code path
                    # below (which classifies inline JS as data-block or
                    # known-inline) does not apply. The script's own bytes
                    # live in a separate emitted asset (app.js) and are
                    # tested by TestClientRuntimeAssets.
                    continue
                if "application/json" in attrs.lower():
                    try:
                        json.loads(body)
                    except ValueError as e:
                        self.fail("%s: the JSON data block does not parse: %s"
                                  % (url, e))
                    self.assertNotIn(
                        "</script", body.lower(),
                        "%s: a record broke out of the JSON data block" % url)
                    self.assertNotIn(
                        "<script", body.lower(),
                        "%s: a record injected a script into the data block" % url)
                    continue
                if not any(k in body for k in known):
                    self.fail("%s: an unrecognised inline script reached a page: %r"
                              % (url, body[:120]))

    def test_link_scheme_fence(self):
        """A javascript:/data:/vbscript: href is an execution vector.

        The corpus contains none today (measured). The renderer must still
        refuse one, or the fence depends on the corpus never changing -- which
        is not a fence, it is luck.
        """
        for scheme in ("javascript:alert(1)", "JavaScript:alert(1)",
                       "data:text/html;base64,PHNjcmlwdD4=",
                       "vbscript:msgbox(1)", "  javascript:alert(1)"):
            out = md.render("[click](%s)" % scheme)
            low = out.lower()
            self.assertNotIn('href="javascript:', low,
                             "a javascript: href survived: %r" % out)
            self.assertNotIn('href="data:', low,
                             "a data: href survived: %r" % out)
            self.assertNotIn('href="vbscript:', low,
                             "a vbscript: href survived: %r" % out)
            self.assertIn("click", page_text(out),
                          "the link TEXT was dropped; refusing the scheme must "
                          "not delete the corpus's words: %r" % out)

    def test_safe_schemes_still_work(self):
        """The other half: refusing the dangerous must not break the ordinary."""
        out = md.render("[doi](https://doi.org/10.1234/x)")
        self.assertIn('href="https://doi.org/10.1234/x"', out)
        out = md.render("[m](mailto:a@b.c)")
        self.assertIn('href="mailto:a@b.c"', out)
        out = md.render("[rel](../chapter/x.html)")
        self.assertIn('href="../chapter/x.html"', out)


# ---------------------------------------------------------------------------
# 7. BADGE SOVEREIGNTY
# ---------------------------------------------------------------------------


class TestBadgesDistinct(unittest.TestCase):
    """The cardinal rule, made structural: the two vocabularies never merge.

    'hypothesized' is a member of BOTH vocabularies and means different things
    in each. So distinctness may not rest on the token text, and may not rest
    on colour alone (that dies in print and for colourblind readers).
    """

    def _classes(self, html):
        out = set()
        for m in re.finditer(r'class="([^"]+)"', html):
            out.update(m.group(1).split())
        return out

    def test_badges_distinct(self):
        # The collision token itself: the hardest case, tested first.
        uni = templates.uni_fence_badge("hypothesized")
        nat = templates.natura_badge("HYPOTHESIZED")
        cu, cn = self._classes(uni), self._classes(nat)
        self.assertTrue(cu and cn, "a badge rendered no class at all")
        self.assertEqual(set(), cu & cn,
                         "THE CARDINAL SIN: the UNI fence badge and the NATURA "
                         "badge share CSS class(es) %r for the SAME token "
                         "'hypothesized'. The two vocabularies would be "
                         "indistinguishable at a glance." % (cu & cn))
        # No shared ancestor class name anywhere in either tree.
        for c in cu:
            self.assertTrue(c.startswith("fence"),
                            "UNI badge carries non-fence class %r" % c)
        for c in cn:
            self.assertTrue(c.startswith("natura"),
                            "NATURA badge carries non-natura class %r" % c)

    def test_badges_distinct_across_every_value(self):
        for v in templates.UNI_FENCE:
            for n in templates.NATURA_CLASSES:
                cu = self._classes(templates.uni_fence_badge(v))
                cn = self._classes(templates.natura_badge(n))
                self.assertEqual(set(), cu & cn,
                                 "UNI %r and NATURA %r share class(es) %r"
                                 % (v, n, cu & cn))

    def test_badges_carry_a_non_colour_signal(self):
        """Colour dies in print and for colourblind readers, so the badge must
        say which vocabulary it speaks IN TEXT."""
        self.assertIn("UNI", page_text(templates.uni_fence_badge("proven")))
        self.assertIn("NATURA", page_text(templates.natura_badge("OBSERVED-SINGLE")))

    def test_no_shared_base_class_in_theme_css(self):
        """theme.css must give them no shared CLASS and no shared IDENTITY.

        WHAT THIS DOES NOT FORBID, and why the distinction is the test:
        theme.css carries '@media (prefers-contrast: more) { .fence, .natura,
        .lex, .store { border-width: 2px } }'. An earlier version of this test
        failed on that grouped selector. It was WRONG. A grouped selector is not
        a shared class -- the two still share no class name, no ancestor and no
        mixin -- and thickening every badge's border for a high-contrast reader
        does not make a UNI fence look like a NATURA class. Making that test
        pass would have meant DELETING AN ACCESSIBILITY RULE to satisfy a
        misreading of the sovereignty rule.

        What actually matters is that the IDENTITY-BEARING properties differ.
        So this asserts the real thing: no shared '.badge' class name, and the
        shape signal (border-radius: square vs rounded) is never granted to
        both by one selector -- because shape is what survives monochrome print
        and colourblindness, where colour does not.
        """
        css_path = os.path.join(READER, "theme.css")
        with open(css_path, "rb") as fh:
            css = fh.read().decode("utf-8")
        css = re.sub(r"/\*.*?\*/", " ", css, flags=re.S)

        self.assertNotRegex(css, r"(?<![\w-])\.badge(?![\w-])",
                            "a shared '.badge' class exists in theme.css; the "
                            "two vocabularies must share no class name.")

        identity = ("border-radius", "content")
        for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
            sel, body = m.group(1), m.group(2)
            if ".fence" in sel and ".natura" in sel:
                for prop in identity:
                    self.assertNotRegex(
                        body, r"(?<![\w-])%s\s*:" % re.escape(prop),
                        "theme.css gives .fence and .natura the same %r through "
                        "one selector (%r). Shape is the signal that survives "
                        "print and colourblindness; it may not be shared."
                        % (prop, sel.strip()[:80]))

        # The shape signal must actually EXIST and actually DIFFER, or there is
        # nothing for the rule above to protect.
        radii = {}
        for name in ("fence", "natura"):
            for m in re.finditer(r"\.%s\s*\{([^}]*)\}" % name, css):
                r = re.search(r"border-radius\s*:\s*([^;]+)", m.group(1))
                if r:
                    radii[name] = r.group(1).strip()
        self.assertEqual(2, len(radii),
                         "could not find a border-radius for both .fence and "
                         ".natura; the non-colour shape signal is missing: %r"
                         % radii)
        self.assertNotEqual(radii["fence"], radii["natura"],
                            "the UNI fence and the NATURA badge have the SAME "
                            "border-radius (%r); the shape signal that must "
                            "survive monochrome print does not distinguish "
                            "them." % radii)

    def test_stores_are_a_third_axis(self):
        """HONEST is never calibrated; it is not a NATURA class in a hat."""
        h = templates.store_badge("HONEST")
        ch = self._classes(h)
        self.assertEqual(set(), ch & self._classes(templates.natura_badge("MODELED")))
        self.assertEqual(set(), ch & self._classes(templates.uni_fence_badge("proven")))
        self.assertIn("NEVER calibrated", h)

    def test_badges_on_the_built_site_stay_sovereign(self):
        """Not just in unit isolation -- on the real pages.

        THE COMPARISON IS BY CLASS TOKEN, NOT BY SUBSTRING, and that distinction
        is the whole test. An earlier version asserted `'fence' not in cls` for
        every natura badge and failed across 25 pages on the class
        'natura--group-fenced'. That class is the NATURA group named FENCED
        (NA-00's three groups: measured / derived / fenced) -- it is not the UNI
        fence, it merely contains those six letters. A test written to catch a
        conflation of two vocabularies had itself conflated two meanings of one
        word, and 'fixing' the reader to please it would have renamed a
        legitimate NA-00 group. Tokens, then, and exact prefixes.
        """
        pages_with_natura = [u for u, t in PAGES.items() if "natura--" in t]
        self.assertTrue(pages_with_natura, "no NATURA badge reached the site")
        for url, text in PAGES.items():
            for m in re.finditer(r'class="([^"]*)"', text):
                toks = set(m.group(1).split())
                uni = {t for t in toks if t == "fence" or t.startswith("fence--")}
                nat = {t for t in toks if t == "natura" or t.startswith("natura--")}
                self.assertFalse(
                    uni and nat,
                    "%s: one element carries BOTH vocabularies: UNI %r and "
                    "NATURA %r. This is the cardinal sin made visible."
                    % (url, sorted(uni), sorted(nat)))

    def test_badge_token_check_does_not_fire_on_the_fenced_group(self):
        """Control for the test above: NA-00's 'fenced' GROUP is not the UNI
        fence, and must not be read as one."""
        out = templates.natura_badge("NOT-MEASURED")
        self.assertIn("natura--group-fenced", out,
                      "the fenced group class is gone; this control is stale")
        toks = set(re.search(r'class="(natura[^"]*)"', out).group(1).split())
        self.assertFalse({t for t in toks if t == "fence" or t.startswith("fence--")},
                         "a NATURA badge carries a UNI fence class token")

    def test_ledger_must_declare_its_vocabulary(self):
        """A ledger that does not say which vocabulary it speaks does not render."""
        prov = {"source_path": "x.md", "sha256": "a" * 64, "commit": "c",
                "built_utc": "t"}
        with self.assertRaises(templates.VocabularyError):
            templates.render_page("ledger", {"title": "x", "provenance": prov})
        with self.assertRaises(templates.VocabularyError):
            templates.render_page("ledger", {"title": "x", "provenance": prov,
                                             "vocabulary": "both"})
        for v in ("uni", "natura"):
            out = templates.render_page("ledger", {"title": "x", "provenance": prov,
                                                   "vocabulary": v})
            self.assertIn("vocabbox--" + v, out)


# ---------------------------------------------------------------------------
# 8. NO "PERFECT" CLAIMS -- scoped to the READER'S voice, not the corpus's
# ---------------------------------------------------------------------------

# Phrases that would only appear if the READER asserted them. Deliberately
# narrow: see the module docstring for why a page-wide grep for "perfect" or
# "verified" is the wrong instrument and cannot be made right.
_CLAIM_PHRASES = (
    r"perfect(?:ly)?\s+(?:sanskrit|latin|hindi|spanish|english|translat\w+)",
    r"translat\w+\s+(?:is|are|was|were|has been|have been)\s+"
    r"(?:perfect|verified|proven|certified|guaranteed)",
    r"(?:perfectly|accurately|faithfully)\s+translated",
    r"translation\s+(?:is\s+)?(?:complete|perfect|verified)",
    r"(?:verified|proven|certified|guaranteed)\s+translation",
    r"all\s+(?:terms|entries)\s+(?:are\s+)?(?:cited|verified|attested)",
)
_CLAIM_RE = [re.compile(p, re.I) for p in _CLAIM_PHRASES]

# Banned in the READER'S OWN author voice (the honesty rail). Quoting them in
# order to fence them is fine; asserting them is not.
_BANNED_AUTHOR_VOICE = ("self-aware", "conscious", "agi", "held-pass")


class TestNoPerfectClaims(unittest.TestCase):

    def test_no_perfect_claims(self):
        """No emitted page claims a translation is perfect or verified."""
        bad = []
        for url, text in PAGES.items():
            t = page_text(text)
            for rx in _CLAIM_RE:
                for m in rx.finditer(t):
                    bad.append("%s: %r" % (url, t[max(0, m.start() - 70):
                                                  m.end() + 40]))
        self.assertEqual([], bad,
                         "%d translation-perfection claim(s) on the built site. "
                         "Rule 18.14 of the operator's own charter: 'Do not "
                         "claim perfect translation.'\n%s"
                         % (len(bad), "\n".join(bad[:8])))

    def test_no_perfect_claims_positive_control(self):
        """The instrument must fire on the claim it exists to catch."""
        for probe in ("This is perfect Sanskrit.",
                      "The translation is verified.",
                      "Every term was faithfully translated.",
                      "a proven translation of the corpus",
                      "All terms are cited."):
            self.assertTrue(any(rx.search(probe) for rx in _CLAIM_RE),
                            "the instrument does not fire on %r" % probe)

    def test_no_perfect_claims_does_not_fire_on_the_corpus(self):
        """The control that keeps this test from censoring the repo.

        These are REAL sentences from the built site (CN-05, CN-09). They are
        the corpus's own voice, they are honest, and they must pass. A test
        that failed them would demand the corpus be edited to please the test.
        """
        for innocent in (
            "nature did not build one perfect component",
            "It stacked three cheap imperfect ones",
            'INADMISSIBLE -- "the blue whale is nature\'s most perfect design."',
            "a near-perfect hit",
            "A model that had fit perfectly would have taught you less.",
        ):
            hits = [rx.pattern for rx in _CLAIM_RE if rx.search(innocent)]
            self.assertEqual([], hits,
                             "the instrument fires on the corpus's own honest "
                             "prose %r via %r -- it would force a censorship "
                             "'fix'." % (innocent, hits))

    def test_reader_author_voice_is_fenced(self):
        """The reader's OWN strings -- read via ast, so the corpus cannot
        contaminate the measurement."""
        bad = []
        for mod, lineno, s in reader_authored_strings():
            low = s.lower()
            for rx in _CLAIM_RE:
                if rx.search(low):
                    bad.append("%s:%d claims %r" % (mod, lineno, s[:90]))
            for w in _BANNED_AUTHOR_VOICE:
                if re.search(r"(?<![\w-])%s(?![\w-])" % re.escape(w), low):
                    bad.append("%s:%d uses banned author-voice %r in %r"
                               % (mod, lineno, w, s[:90]))
        self.assertEqual([], bad, "\n".join(bad[:10]))

    def test_non_english_registers_state_their_pending_status(self):
        """The deliverable: every non-English register SAYS it is not translated.

        This is the positive obligation matching the negative one above -- the
        reader must not claim perfection, AND must state the honest state.
        """
        for code in ("sa", "la", "hi", "es"):
            url = "lexicon/%s.html" % code
            self.assertIn(url, PAGES, "no %s register page was emitted" % code)
            t = page_text(PAGES[url])
            self.assertIn("PENDING", t, "%s does not say it is PENDING" % url)
            self.assertIn("not carry", t.lower().replace("does not carry",
                                                         "not carry"),
                          "%s does not state what it lacks" % url)
            self.assertRegex(
                t, r"(?i)no chapter has been machine-translated",
                "%s does not state that the prose is untranslated" % url)
        t_en = page_text(PAGES["lexicon/en.html"])
        self.assertNotIn("This English register is PENDING", t_en,
                         "English is the register with full prose; it must not "
                         "be marked PENDING")

    def test_register_counts_are_counted_not_claimed(self):
        """The spec's requirement: the count of CITED vs COINED vs
        PENDING-CITATION in that register, on the page."""
        lex = build.load_lexicon()
        for code, name, field in build.REGISTERS:
            if field == "english":
                continue
            counts = build.register_counts(lex, field)
            t = page_text(PAGES["lexicon/%s.html" % code])
            for token in ("CITED", "COINED", "PENDING-CITATION"):
                n = counts.get(token)
                if n:
                    self.assertRegex(
                        t, r"%s\s*%d" % (re.escape(token), n),
                        "lexicon/%s.html does not carry the counted %s total "
                        "(%d)" % (code, token, n))


# ---------------------------------------------------------------------------
# 9. PARTIAL CORPUS
# ---------------------------------------------------------------------------


class TestPartialCorpus(unittest.TestCase):
    """A missing chapter renders as PENDING and does not crash the build.

    HONEST SCOPE: the corpus is COMPLETE at the time of writing -- every .md
    the registry finds is on disk, so the real build does not exercise this
    path. These tests drive it directly and say so, rather than reporting a
    green tick for a path nothing ran.
    """

    def test_partial_corpus(self):
        phantom = os.path.join(ROOT, "encyclopedia",
                               "NA-99-this-chapter-does-not-exist.md")
        self.assertFalse(os.path.exists(phantom),
                         "the phantom fixture exists on disk; this test would "
                         "measure nothing")
        entry = {
            "abs": phantom,
            "rel": "encyclopedia/NA-99-this-chapter-does-not-exist.md",
            "section": "The Encyclopedia",
            "wing": "encyclopedia",
            "_id": "NA-99",
        }
        ch = build.load_chapter(entry, build.LinkResolver(), "chapter/na-99.html")
        self.assertTrue(ch.missing, "a missing chapter was not marked missing")
        self.assertIsNone(ch.doc)
        self.assertEqual([], ch.numbers)

        out = templates.render_page("chapter", {
            "id": ch.id, "title": ch.title, "wing": ch.wing,
            "pending": True,
            "pending_reason": "The build registry lists %s, but the file is not "
                              "in the repo at build time." % ch.rel,
            "provenance": {"source_path": ch.rel, "sha256": "",
                           "commit": "deadbeef",
                           "built_utc": "2026-07-16T00:00:00Z"},
            "body_html": "",
        })
        t = page_text(out)
        self.assertIn("PENDING", t)
        self.assertIn("ABSENT", t, "a pending page must say its sha256 is "
                                   "ABSENT, not invent one")
        self.assertIn("Falsifier", t, "a PENDING page must carry its falsifier")
        self.assertIn(ch.rel, t, "a PENDING page must name the file it wants")

    def test_partial_corpus_does_not_fabricate(self):
        """The PENDING page must not invent a sha256 or a body."""
        out = templates.render_page("chapter", {
            "id": "X", "title": "X", "pending": True,
            "pending_reason": "absent",
            "provenance": {"source_path": "a/b.md", "sha256": "",
                           "commit": "c", "built_utc": "t"},
        })
        self.assertNotRegex(out, r'class="prov__sha">[0-9a-f]{64}',
                            "a pending page invented a sha256")

    def test_missing_optional_sections_degrade(self):
        """A chapter with no abstract, no numbers, no plates still renders."""
        prov = {"source_path": "x.md", "sha256": "a" * 64, "commit": "c",
                "built_utc": "t"}
        out = templates.render_page("chapter", {
            "title": "Bare", "provenance": prov, "body_html": "<p>Body.</p>"})
        self.assertIn("Body.", out)
        # An empty body says so rather than rendering a blank page.
        out = templates.render_page("chapter", {
            "title": "Empty", "provenance": prov, "body_html": ""})
        self.assertIn("NOT-MEASURED", out)

    def test_absent_lexicon_and_plates_do_not_crash(self):
        """The reader must build against a repo without lexicon/ or plates/."""
        real_plates = build.PLATES_DIR
        try:
            build.PLATES_DIR = os.path.join(READER, "no-such-plates-dir")
            del build.BUILD_NOTES[:]
            plates = build.load_plates()
            self.assertEqual([], plates)
            self.assertTrue(any(n["kind"] == "plates-missing"
                                for n in build.BUILD_NOTES),
                            "an absent plates/ dir was skipped silently")
        finally:
            build.PLATES_DIR = real_plates
            del build.BUILD_NOTES[:]


# ---------------------------------------------------------------------------
# 10. CONTRACT CONFORMANCE between build.py and templates.py
# ---------------------------------------------------------------------------


class TestContractConformance(unittest.TestCase):
    """Where build.py and templates.py disagree, a page renders something the
    reader cannot use. Each of these was an OBSERVED defect on the built site.
    """

    def test_no_python_repr_reached_a_page(self):
        """A dict or list repr on the page means a ctx contract mismatch.

        OBSERVED before the fix: 47 dict reprs on the plate pages, e.g.
        "{'href': '../chapter/na-04.html', 'label': 'NA-04 ...'}" rendered as
        the visible text of the 'Drawn from' marginal.
        """
        bad = []
        for url, text in PAGES.items():
            t = page_text(text)
            for rx in (r"\{'[a-z_]+':\s", r'\{"[a-z_]+":\s',
                       r"<\w+ object at 0x", r"\[\{'"):
                for m in re.finditer(rx, t):
                    bad.append("%s: %r" % (url, t[max(0, m.start() - 40):
                                                 m.end() + 80]))
        self.assertEqual([], bad,
                         "%d Python repr(s) leaked onto the built site -- a "
                         "ctx contract mismatch between build.py and "
                         "templates.py:\n%s" % (len(bad), "\n".join(bad[:5])))

    def test_plate_numbers_render(self):
        """OBSERVED before the fix: every chapter plate rendered 'Plate .'

        build.py passed number='PL-01'; templates._roman() int()s it, failed,
        and returned '' -- so the caption lost its number silently.
        """
        for url, text in PAGES.items():
            for m in re.finditer(r'<span class="plate__no">Plate ([^<]*)</span>',
                                 text):
                self.assertTrue(
                    m.group(1).strip().rstrip("."),
                    "%s: a plate caption renders 'Plate .' with no number" % url)

    def test_plate_source_chapters_are_links(self):
        """A plate's 'Drawn from' must link the chapter, not print a dict."""
        t = PAGES["plate/pl-01.html"]
        m = re.search(r'Drawn from</span><div class="mn__body">(.*?)</div>',
                      t, re.S)
        self.assertIsNotNone(m, "plate/pl-01.html has no 'Drawn from' marginal")
        self.assertIn("<a href=", m.group(1),
                      "the plate's sources are not links: %r" % m.group(1)[:200])

    def test_ledger_does_not_claim_a_false_pending(self):
        """OBSERVED before the fix: both ledger pages rendered an empty table
        and the line 'PENDING: no rows were passed to this ledger' -- directly
        under the FULL ledger, which had rendered fine. A page that says
        PENDING while showing the content is lying in the honest direction,
        which is still lying.
        """
        for url in ("ledger/claim-ledger.html", "ledger/nature-ledger.html"):
            self.assertIn(url, PAGES)
            t = page_text(PAGES[url])
            self.assertNotIn("no rows were passed to this ledger", t,
                             "%s claims PENDING while rendering its rows" % url)

    def test_ledgers_carry_their_content(self):
        for url, vocab in (("ledger/claim-ledger.html", "uni"),
                           ("ledger/nature-ledger.html", "natura")):
            text = PAGES[url]
            self.assertIn("vocabbox--" + vocab, text,
                          "%s does not declare its sovereign vocabulary" % url)
            self.assertGreater(len(page_text(text)), 4000,
                               "%s rendered almost no content" % url)

    def test_table_wrap_class_matches_the_stylesheet(self):
        """A scroll container the stylesheet does not know is not a container.

        OBSERVED before the fix: markdown.py emitted class="table-wrap" while
        theme.css styles only '.tablewrap { overflow-x: auto }'. Every one of
        the corpus's ~3800 table rows rendered with no scroll container, so a
        wide table pushed the page body into a horizontal scroll instead of
        scrolling inside its own box.
        """
        with open(os.path.join(READER, "theme.css"), "rb") as fh:
            css = fh.read().decode("utf-8")
        wrappers = set(re.findall(r'<div class="(table-?wrap)"', md.render(
            "| A | B |\n|---|---|\n| 1 | 2 |")))
        self.assertTrue(wrappers, "markdown.py emitted no table wrapper at all")
        for w in wrappers:
            self.assertRegex(
                css, r"\.%s\s*\{[^}]*overflow-x:\s*auto" % re.escape(w),
                "markdown.py wraps tables in .%s but theme.css defines no "
                "'.%s { overflow-x: auto }' rule, so corpus tables have no "
                "scroll container." % (w, w))

    def test_every_page_kind_rendered(self):
        kinds = {"index.html": "index", "az.html": "az",
                 "search.html": "search", "colophon.html": "colophon"}
        for url in kinds:
            self.assertIn(url, PAGES, "the build emitted no %s" % url)
        self.assertTrue(any(u.startswith("chapter/") for u in PAGES))
        self.assertTrue(any(u.startswith("ledger/") for u in PAGES))
        self.assertTrue(any(u.startswith("plate/") for u in PAGES))
        self.assertTrue(any(u.startswith("lexicon/") for u in PAGES))

    def test_internal_links_resolve(self):
        """A dead internal link is a page presented as live that 404s."""
        dead = []
        for url, text in PAGES.items():
            base = os.path.dirname(url)
            for m in re.finditer(r'<a[^>]+href="([^"#][^"]*)"', text):
                href = html_mod.unescape(m.group(1))
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:", href):
                    continue
                target = href.split("#")[0]
                if not target:
                    continue
                rel = os.path.normpath(os.path.join(base, target)).replace(
                    os.sep, "/")
                if not os.path.exists(os.path.join(DIST, rel.replace("/", os.sep))):
                    dead.append("%s -> %s" % (url, href))
        self.assertEqual([], dead, "%d dead internal link(s):\n%s"
                         % (len(dead), "\n".join(sorted(set(dead))[:15])))

    def test_no_duplicate_page_urls(self):
        self.assertEqual(len(build.EMITTED), len(set(build.EMITTED)))
        # PAGES holds only .html; EMITTED also carries the client runtime
        # assets (app.js, sw.js, manifest, precache-manifest.json,
        # search-index.json, scrivener/*). Compare the html subset directly.
        html_urls = {u for u in build.EMITTED if u.endswith(".html")}
        self.assertEqual(len(PAGES), len(html_urls),
                         "the build recorded %d html urls but %d html files "
                         "are on disk" % (len(html_urls), len(PAGES)))


# ---------------------------------------------------------------------------
# 11. THE RENDERER ITSELF
# ---------------------------------------------------------------------------


class TestMarkdownSubset(unittest.TestCase):
    """The subset was chosen by measuring the corpus. These are the measurements."""

    def test_headings_and_slugs(self):
        d = md.parse("# Title\n\n## Section one\n")
        self.assertEqual("Title", d.title)
        self.assertIn('<h1 id="title">', d.html)
        self.assertIn('<h2 id="section-one">', d.html)

    def test_duplicate_heading_ids_are_unique(self):
        d = md.parse("# A\n\n## The numbers\n\n## The numbers\n")
        ids = [h["id"] for h in d.headings]
        self.assertEqual(len(ids), len(set(ids)), "duplicate anchor ids: %r" % ids)

    def test_table_escaped_pipe(self):
        """86 corpus rows carry an escaped pipe; splitting naively shreds them."""
        cells = md.split_table_row(r"| `p(mu \| s)` | x |")
        self.assertEqual(2, len(cells), "escaped pipe split the row: %r" % cells)
        out = md.render("| A | B |\n|---|---|\n| `p(a \\| b)` | y |")
        self.assertIn("p(a | b)", html_mod.unescape(page_text(out)))

    def test_intraword_underscore_is_not_emphasis(self):
        """The corpus is full of b_Kleiber, N_sg, T_b. Emphasis would delete
        the underscores from the science."""
        out = md.render("The exponent b_Kleiber and N_sg and f_aff hold.")
        self.assertNotIn("<em>", out)
        self.assertIn("b_Kleiber", page_text(out))

    def test_no_indented_code_blocks(self):
        """All 172 candidates in the corpus are ordered-list continuations;
        rendering them as code would turn prose into code."""
        out = md.render("1. item\n\n    continuation prose here\n")
        self.assertNotIn("<pre>", out)

    def test_no_dollar_math(self):
        """All 20 '$' lines in the corpus are shell vars or money. A '$' math
        rule would eat the ledger's own numbers."""
        out = md.render("The cost was $200 and $3,450 for $env:UNI_MCP.")
        self.assertIn("$200", page_text(out))
        self.assertNotIn("<math", out)

    def test_math_fence_degrades_honestly(self):
        """No renderer is vendored, so math must show as labelled source --
        never fetch, never silently render wrong."""
        out = md.render("```math\nF = E_q[ln q - ln p]\n```")
        self.assertIn("math-src", out)
        self.assertIn("F = E_q[ln q - ln p]", html_mod.unescape(page_text(out)))
        self.assertIn("not typeset", page_text(out))

    def test_parse_always_progresses(self):
        """A hang leaves no receipt. Every pathological input must terminate."""
        for src in ("|\n", "| a |\n", "***\n", "__\n", "____\n",
                    "> \n", "- \n", "```\n", "[](", "1.\n", "|||\n",
                    "a__b__c\n", "**\n", "# \n"):
            d = md.parse(src)
            self.assertIsInstance(d.html, str)

    def test_blockquote_and_lists(self):
        self.assertIn("<blockquote>", md.render("> quoted\n"))
        self.assertIn("<ul>", md.render("- a\n- b\n"))
        self.assertIn("<ol>", md.render("1. a\n2. b\n"))
        self.assertIn("<ol start=\"3\">", md.render("3. a\n4. b\n"))

    def test_nested_lists(self):
        out = md.render("- a\n  - b\n")
        self.assertIn("<ul><li>a<ul><li>b</li></ul></li></ul>", out)


class TestGeneratorUnits(unittest.TestCase):

    def test_chapter_id_requires_spaced_separator(self):
        """'# UNI-GPT Consult -- 2026-06-27' must NOT yield id 'UNI'.

        It did once: the hyphen INSIDE 'UNI-GPT' matched, the id collided with
        another file, and a chapter was silently overwritten.
        """
        self.assertEqual("NA-05", build._chapter_id("x/na-05.md",
                                                    "NA-05 -- The ratios"))
        self.assertEqual("mu1", build._chapter_id("x/mu1.md",
                                                  "mu1 - The Evidence Constitution"))
        self.assertEqual(
            "uni-gpt-consult-package",
            build._chapter_id("x/uni-gpt-consult-package.md",
                              "UNI-GPT Consult -- 2026-06-27"),
            "an id was taken from a hyphen inside a word; this silently "
            "overwrote a chapter once")

    def test_url_allocation_disambiguates_every_member(self):
        """Both 00-INDEX.md files must get distinct urls -- and not by walk
        order, or the urls move between builds."""
        found = build.discover_chapters()
        urls = build.allocate_urls(found)
        idx = [u for r, u in urls.items() if r.endswith("00-INDEX.md")]
        self.assertGreater(len(idx), 1, "expected two 00-INDEX.md files")
        self.assertEqual(len(idx), len(set(idx)),
                         "the two 00-INDEX.md files share a url")

    def test_emit_refuses_a_duplicate_url(self):
        """Positive control: writing the same url twice must be refused, not
        allowed to silently overwrite a chapter."""
        before = set(build.EMITTED)
        try:
            build.EMITTED.add("probe/dup.html")
            with self.assertRaises(AssertionError):
                build.emit("probe/dup.html", "<html></html>")
        finally:
            build.EMITTED.clear()
            build.EMITTED.update(before)

    def test_natura_class_extraction_is_longest_first(self):
        """MODELED-CONTESTED must never be read as MODELED."""
        self.assertEqual(["MODELED-CONTESTED"],
                         build.extract_natura_classes("**MODELED-CONTESTED**"))
        self.assertEqual(["OBSERVED-REPLICATED"],
                         build.extract_natura_classes(
                             "OBSERVED-REPLICATED *(secondary)*"))
        self.assertEqual([], build.extract_natura_classes("as above"))

    def test_natura_compound_cells_keep_both_classes(self):
        """A compound row is a registered convention; dropping one is data loss."""
        out = templates.natura_badge("**OBSERVED-CONTESTED / MODELED**")
        self.assertIn("OBSERVED-CONTESTED", out)
        self.assertIn("MODELED", out)
        self.assertIn("natura-compound", out)

    def test_natura_qualifier_is_rendered_not_swallowed(self):
        """'not primary-sourced in this pass' IS the point of the row."""
        out = templates.natura_badge("OBSERVED-REPLICATED *(secondary)*")
        self.assertIn("(secondary)", page_text(out))

    def test_svg_fence_is_observed_not_believed(self):
        """A plate's JSON asserts 'script_elements: 0'. That is the plate's own
        narrative (Class-G). M9 ranks tool state (Class-B) above it."""
        self.assertEqual([], build.check_svg_fence(
            '<svg %s><path d="M0 0"/></svg>' % 'xmlns="http://www.w3.org/2000/svg"'))
        self.assertTrue(build.check_svg_fence("<svg><script>x()</script></svg>"))
        self.assertTrue(build.check_svg_fence('<svg><rect onclick="x()"/></svg>'))
        self.assertTrue(build.check_svg_fence('<svg><image href="https://e/x.png"/></svg>'))

    def test_every_plate_svg_passes_its_own_fence(self):
        """The design-only fence, checked on the real plates."""
        for p in build.load_plates():
            self.assertEqual([], p["fence_hits"],
                             "plate %s trips the design-only fence: %r"
                             % (p["id"], p["fence_hits"]))
            self.assertTrue(p["svg_markup"], "plate %s did not inline" % p["id"])

    def test_vocabularies_overlap_is_only_hypothesized(self):
        self.assertEqual(["hypothesized"], build.assert_vocabularies_sovereign())

    def test_build_notes_are_surfaced_not_swallowed(self):
        """52 observations were made about the corpus; the colophon must carry
        them, or a silent skip is exactly what happened."""
        self.assertIn("colophon.html", PAGES)
        t = page_text(PAGES["colophon.html"])
        self.assertIn("What this build observed", t)
        for kind in ("url-collision", "unregistered-class"):
            self.assertIn(kind, t, "the colophon does not surface %r notes" % kind)

    def test_colophon_accounts_for_every_repo_file(self):
        """'Always the real as-is repo knowledge' means nothing is omitted
        silently -- what is not rendered must be listed and reasoned."""
        t = PAGES["colophon.html"]
        for probe in ("gpt/knowledge", "tools/build_gpt_pack.py",
                      "reader/build.py"):
            self.assertIn(probe, html_mod.unescape(page_text(t)),
                          "the colophon does not account for %r" % probe)


# ---------------------------------------------------------------------------
# 12. CLIENT RUNTIME + PWA + SCRIVENER + SEARCH INDEX + PRECACHE MANIFEST
# ---------------------------------------------------------------------------


def _read(path):
    with open(path, "rb") as fh:
        return fh.read()


class TestClientRuntimeAssets(unittest.TestCase):
    """Every new asset the build now emits: dist/app.js, dist/sw.js,
    dist/manifest.webmanifest, dist/scrivener/{app.js, style.css, README.md,
    index.html}, dist/search-index.json, dist/precache-manifest.json.

    ASCII-ONLY still holds for every one of them (test_ascii_only_output
    already iterates FILES, which now includes these), and each carries the
    invariant tests specific to its purpose below.
    """

    _JS_ASSETS = (
        "app.js", "sw.js",
        "scrivener/app.js",
    )
    _CSS_ASSETS = ("scrivener/style.css",)
    _JSON_ASSETS = ("manifest.webmanifest", "search-index.json",
                    "precache-manifest.json",
                    # Build-time provenance fallback. On the fleet the
                    # operator's deploy script overwrites this with per-limb
                    # values; locally it makes the reader show sensible
                    # provenance instead of blank.
                    "_provenance.json")

    def test_all_expected_assets_emitted(self):
        for rel in (self._JS_ASSETS + self._CSS_ASSETS + self._JSON_ASSETS
                    + ("scrivener/index.html", "scrivener/README.md")):
            p = os.path.join(DIST, rel.replace("/", os.sep))
            self.assertTrue(os.path.exists(p),
                            "the build did not emit %s" % rel)
            self.assertGreater(os.path.getsize(p), 0, "%s is empty" % rel)

    def test_ascii_only_still_holds(self):
        """Extend the ASCII fence to explicitly cover every new asset.

        test_ascii_only_output already scans FILES, but naming these here
        makes the CI report a specific asset by name rather than pointing at
        a byte offset in a random file, and it exercises the intent that this
        set is fenced.
        """
        for rel in (self._JS_ASSETS + self._CSS_ASSETS + self._JSON_ASSETS
                    + ("scrivener/index.html", "scrivener/README.md")):
            p = os.path.join(DIST, rel.replace("/", os.sep))
            raw = _read(p)
            for i, b in enumerate(raw):
                if b > 0x7F:
                    self.fail("%s carries non-ASCII byte 0x%02X at %d"
                              % (rel, b, i))


class TestScrivenerIsClientOnly(unittest.TestCase):
    """The Scrivener writes ONLY to the browser's IndexedDB. No fetch, no
    XHR, no cross-origin URL, no server endpoint. Read-only invariant of the
    corpus reader stands because the Scrivener never touches the generator's
    filesystem.
    """

    def _text(self, rel):
        return _read(os.path.join(DIST, rel.replace("/", os.sep))).decode(
            "ascii", "replace")

    def test_scrivener_app_is_indexeddb_backed(self):
        js = self._text("scrivener/app.js")
        self.assertTrue(
            re.search(r"\bindexedDB\b|\bIndexedDB\b", js),
            "scrivener/app.js does not use IndexedDB -- the doctrine says the "
            "HONEST store is the browser's IndexedDB")

    def test_scrivener_does_no_fetch_or_xhr(self):
        # fetch, XHR, and WebSocket must all be absent from the Scrivener's
        # JS AND its inlined shell page.
        banned = ("fetch(", "XMLHttpRequest", "WebSocket", "sendBeacon",
                  "importScripts")
        for rel in ("scrivener/app.js", "scrivener/index.html"):
            body = self._text(rel)
            for b in banned:
                self.assertNotIn(b, body,
                                 "%s uses %r -- the Scrivener must be client-"
                                 "only, no network I/O." % (rel, b))

    def test_scrivener_makes_no_cross_origin_or_mutating_request(self):
        # No absolute http/https URL, no protocol-relative //host, and no
        # verb-shaped API call ("POST", "PUT", "DELETE" as bare tokens in a
        # network context). The only http string tolerated is the SVG
        # namespace identifier -- which no Scrivener file carries.
        for rel in ("scrivener/app.js", "scrivener/index.html"):
            body = self._text(rel)
            self.assertNotRegex(body, r"https?://",
                                "%s carries an http(s) URL" % rel)
            self.assertNotRegex(body, r"[\"']//[a-zA-Z0-9.]",
                                "%s carries a protocol-relative URL" % rel)
            for method in ('"POST"', "'POST'", '"PUT"', "'PUT'",
                           '"DELETE"', "'DELETE'", '"PATCH"', "'PATCH'"):
                self.assertNotIn(method, body,
                                 "%s carries the write-verb %s" % (rel, method))

    def test_scrivener_shell_page_has_no_edit_of_corpus(self):
        """The Scrivener's shell page must not expose ANY static form,
        input, textarea, or fetch target that points at a corpus path.

        The only editable surface is the modal the JS mints at runtime in
        the browser DOM, and its writes are all IndexedDB. What THIS test
        forbids is a STATIC <form action="../chapter/..."> or similar in
        the emitted HTML markup. The inline <script> block's own string
        contents build the modal at runtime and are checked separately by
        test_scrivener_does_no_fetch_or_xhr; grepping the whole file for
        '<input' would fire on those JS strings, which is not a defect.
        """
        html = self._text("scrivener/index.html")
        # Isolate the markup OUTSIDE inline scripts/styles.
        markup = re.sub(r"<script\b[^>]*>.*?</script>", "", html,
                        flags=re.S | re.I)
        markup = re.sub(r"<style\b[^>]*>.*?</style>", "", markup,
                        flags=re.S | re.I)
        for tag in ("<input", "<textarea", "<form"):
            self.assertNotIn(tag, markup.lower(),
                             "scrivener/index.html carries a static %s in "
                             "its markup (outside inline script/style)" % tag)
        # And no href/src back into corpus paths anywhere -- even in a JS
        # string literal, a corpus URL is a smell worth flagging.
        for rx in (r'action\s*=\s*["\'][^"\']*(?:chapter|ledger|plate|lexicon)/',
                   r'\bhref\s*=\s*["\'][^"\']*(?:chapter|ledger|plate|lexicon)/'):
            self.assertNotRegex(html, rx,
                                "scrivener/index.html targets a corpus path")


class TestNoInlineEventHandlers(unittest.TestCase):
    """No <tag ... on*=...> handler in ANY emitted HTML.

    The existing HTML fence in build.fence_scan() already catches this on
    every page. This test also runs it here on the on-disk output, so a
    regression is caught even if the build's own scan were weakened.
    """

    _RE = re.compile(r"<\s*[a-z][^>]*\son[a-z]+\s*=", re.I)

    def test_no_inline_event_handlers(self):
        bad = []
        for dp, dn, fn in os.walk(DIST):
            for f in sorted(fn):
                if not f.endswith(".html"):
                    continue
                p = os.path.join(dp, f)
                text = _read(p).decode("ascii", "replace")
                m = self._RE.search(text)
                if m:
                    rel = os.path.relpath(p, DIST).replace(os.sep, "/")
                    bad.append("%s near %r" % (rel,
                                               text[max(0, m.start() - 40):
                                                    m.end() + 30]))
        self.assertEqual([], bad,
                         "%d emitted HTML file(s) carry an on* handler:\n%s"
                         % (len(bad), "\n".join(bad[:5])))


class TestServiceWorker(unittest.TestCase):
    """The SW file must reference CACHE_VERSION (substituted) and a scope
    that matches manifest.webmanifest.scope."""

    def test_sw_manifest_has_scope_and_version(self):
        sw = _read(os.path.join(DIST, "sw.js")).decode("ascii")
        manifest = json.loads(_read(os.path.join(
            DIST, "manifest.webmanifest")).decode("ascii"))
        # CACHE_VERSION is present and is NOT the literal token (build.py
        # substituted GIT.short into it).
        self.assertRegex(sw, r"\bCACHE_VERSION\b",
                         "sw.js does not reference CACHE_VERSION")
        m = re.search(r'var\s+CACHE_VERSION\s*=\s*"([^"]+)"', sw)
        self.assertIsNotNone(m, "sw.js does not define CACHE_VERSION")
        self.assertNotEqual("__CACHE_VERSION__", m.group(1),
                            "build.py did not substitute the CACHE_VERSION "
                            "token in sw.js")
        # SCOPE agreement between sw.js and manifest.webmanifest.
        #
        # Both are now DEPLOYMENT-AGNOSTIC: the manifest declares scope='./'
        # (relative to the manifest URL, so resolved to its own directory in
        # the browser); sw.js derives SCOPE_PATH at parse time from its own
        # URL (`new URL('./', self.location).pathname`). That means the same
        # file works at /glass/cookbook/ on a fleet limb AND at / from a
        # local `python -m http.server -d reader/dist`. A string-literal
        # SCOPE_PATH would have to be one or the other.
        scope = manifest.get("scope")
        self.assertEqual(
            "./", scope,
            "manifest.webmanifest scope must be './' (relative to the "
            "manifest URL); a hardcoded absolute path breaks whichever "
            "deployment is not that one. Got %r." % scope)
        # sw.js must derive SCOPE_PATH from its own location, not hardcode it.
        self.assertRegex(
            sw, r"SCOPE_PATH\s*=\s*new\s+URL\s*\(\s*['\"]\.\/['\"]\s*,\s*self\.location",
            "sw.js does not derive SCOPE_PATH from self.location; a hardcoded "
            "value ties the SW to one deployment.")
        # And the derived expression must be the only assignment: no lingering
        # hardcoded string form.
        self.assertNotRegex(
            sw, r'var\s+SCOPE_PATH\s*=\s*"/[^"]+/"',
            "sw.js still carries a hardcoded absolute SCOPE_PATH string; the "
            "dynamic derivation was added but the literal was not removed.")


class TestPrecacheManifest(unittest.TestCase):
    """The precache manifest lists every file the SW needs and each entry's
    sha256 matches the on-disk bytes -- or the SW would fail to install."""

    def _load(self):
        raw = _read(os.path.join(DIST, "precache-manifest.json")).decode(
            "ascii")
        return json.loads(raw)

    def test_precache_manifest_has_entries(self):
        data = self._load()
        files = data.get("files") if isinstance(data, dict) else data
        self.assertIsInstance(files, list, "precache-manifest.json is not a "
                                            "list-shaped file catalogue")
        self.assertGreater(len(files), 10,
                           "precache-manifest.json lists only %d file(s); the "
                           "build emits ~100" % len(files))

    def test_precache_manifest_shas_match_disk(self):
        data = self._load()
        files = data.get("files") if isinstance(data, dict) else data
        # Sample five: index, colophon, search, one chapter, one plate. The
        # sample is picked from what's in the manifest, not made up.
        picks = []
        wanted_prefixes = ("index.html", "colophon.html", "search.html",
                           "chapter/", "plate/")
        for prefix in wanted_prefixes:
            for e in files:
                path = e.get("path") or e.get("url")
                if path and path.startswith(prefix):
                    picks.append(e)
                    break
        self.assertGreaterEqual(len(picks), 3,
                                "the manifest carries fewer than three of the "
                                "expected sampled files: %r"
                                % [e.get("path") or e.get("url") for e in picks])
        bad = []
        for e in picks:
            path = e.get("path") or e.get("url")
            claimed = e.get("sha256")
            p = os.path.join(DIST, path.replace("/", os.sep))
            if not os.path.exists(p):
                bad.append("%s: manifest lists file that is not on disk"
                           % path)
                continue
            real = hashlib.sha256(_read(p)).hexdigest()
            if real != claimed:
                bad.append("%s: manifest sha256 %s, disk sha256 %s"
                           % (path, claimed[:12], real[:12]))
        self.assertEqual([], bad,
                         "precache-manifest.json sha256(s) do not match disk:"
                         "\n%s" % "\n".join(bad))

    def test_precache_manifest_does_not_list_itself(self):
        """A precache entry for the manifest itself is a circular dependency
        the SW would try to install and re-fetch on every activate."""
        data = self._load()
        files = data.get("files") if isinstance(data, dict) else data
        for e in files:
            path = e.get("path") or e.get("url")
            self.assertNotEqual("precache-manifest.json", path,
                                "the precache manifest lists ITSELF")


class TestReadOnlyInvariantStillHolds(unittest.TestCase):
    """Explicit re-affirmation: the corpus bytes did not move AND every
    mutating call still targeted dist. TestReadOnlyInvariant above already
    asserts this; this class states it under a name the extension tests can
    reference so a regression report says which invariant broke.
    """

    def test_read_only_invariant_still_holds(self):
        # Repeat the two central assertions of TestReadOnlyInvariant so this
        # is a first-class check on the extended build, not a hope.
        outside = [(op, p) for op, p in MUTATIONS if not _inside_dist(p)]
        self.assertEqual([], outside,
                         "READ-ONLY VIOLATION after extension: %d path(s) "
                         "outside reader/dist/" % len(outside))
        changed = [k for k in CORPUS_BEFORE if CORPUS_BEFORE.get(k)
                   != CORPUS_AFTER.get(k)]
        self.assertEqual([], changed,
                         "READ-ONLY VIOLATION after extension: %d corpus "
                         "file(s) changed: %r" % (len(changed), changed[:10]))


class TestSearchIndex(unittest.TestCase):
    """search-index.json feeds the offline search overlay in app.js."""

    def test_search_index_is_array_of_rows(self):
        rows = json.loads(_read(os.path.join(
            DIST, "search-index.json")).decode("ascii"))
        self.assertIsInstance(rows, list)
        self.assertGreater(len(rows), 30,
                           "search-index.json carries only %d row(s); the "
                           "corpus has ~80 chapters" % len(rows))
        for r in rows[:20]:
            self.assertIn("path", r)
            self.assertIn("title", r)
            self.assertIn("body", r)
            self.assertLessEqual(len(r["body"]), 320,
                                 "search row body exceeds ~300 chars: %d"
                                 % len(r["body"]))


class TestCorpusTreeInSidebar(unittest.TestCase):
    """The sidebar carries data-corpus-tree as JSON on every chapter page."""

    def test_data_corpus_tree_present_and_parses(self):
        # At least one chapter page must carry the attribute with parseable
        # JSON. The attribute is HTML-attribute-escaped, so &quot; is what
        # the browser (and this test, via html_mod.unescape) reads back.
        page = None
        for url, text in PAGES.items():
            if url.startswith("chapter/") and 'data-corpus-tree=' in text:
                page = (url, text)
                break
        self.assertIsNotNone(page,
                             "no chapter page carries data-corpus-tree")
        url, text = page
        m = re.search(r'data-corpus-tree="([^"]*)"', text)
        self.assertIsNotNone(m, "%s: data-corpus-tree found but attribute "
                                "value did not parse" % url)
        raw = html_mod.unescape(m.group(1))
        tree = json.loads(raw)
        self.assertIsInstance(tree, list)
        self.assertGreater(len(tree), 0)
        for w in tree:
            self.assertIn("name", w)
            self.assertIn("chapters", w)


if __name__ == "__main__":
    unittest.main(verbosity=2)
