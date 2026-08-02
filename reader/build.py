# -*- coding: utf-8 -*-
"""build.py -- the UNI Encyclopedia & Cookbook reader generator.

    python reader/build.py
    python -m http.server -d reader/dist 8080

Python 3 standard library ONLY. No pip, no npm, no vendored third party, and no
network access at build time or at page-view time.

WHAT THIS IS
------------
A static generator that renders THIS repo, as it is on disk right now, into
reader/dist/. It reads; it never writes outside reader/dist/; it has no
database, no server, no API and no edit path. Read-only is not a promise made
in a README -- it is the only thing this code is able to do (see #1).

THE FIVE INVARIANTS, EACH STRUCTURAL RATHER THAN A HABIT
--------------------------------------------------------
1. READ-ONLY.  Every read goes through read_bytes()/read_text(), which open
   mode 'rb' and nothing else. Every write goes through _write_bytes(), which
   resolves the target and REFUSES any path not inside DIST. There is exactly
   one write door in this file and it is guarded by an assertion, not by care.
   WRITE_LOG records every byte written, so a test can audit the whole build.

2. ASCII-ONLY OUTPUT.  Pages are encoded with errors='xmlcharrefreplace', so
   every Devanagari, IAST, Greek and em-dash character leaves as a numeric
   character reference, and _write_bytes() re-checks every byte before it
   lands. Not cosmetic: the fleet's MCP os_file_write silently corrupts
   multi-byte UTF-8 (drops bytes, returns ok=true with a wrong sha), and it is
   the only file transport this box has. ASCII-only bytes make that bug unable
   to fire. This box's own console proved the point during development: cp1252
   stdout raised UnicodeEncodeError on a single arrow, so _say() is ASCII too.

3. PROVENANCE OR NO PAGE.  Every page carries source path + sha256 + commit +
   built UTC. build_provenance() raises rather than return a partial stamp,
   and templates.render_page() raises ProvenanceError independently. Two
   locks, no flag to open either.

4. NO EXTERNAL NETWORK REFERENCES.  fence_scan() greps every emitted page for
   asset-loading references to a remote host and fails the build on a hit. The
   scan runs on output, not on intent.

5. THE REPO IS THE TRUTH.  Every page renders bytes read from the repo file at
   build time. Nothing is cached, hand-copied, or carried between builds.

WHAT THIS FILE DELIBERATELY DOES NOT CLAIM
------------------------------------------
The git commit is CONTEXT, never proof that a page's bytes are in it. At the
time of writing, lexicon/ and reader/plates/ are UNTRACKED: stamping
'commit f1be794' beside a lexicon page would assert its content is in that
commit, which is false. So the commit stamp carries the file's own git state
and says, on the page, when the commit does NOT describe those bytes. The
sha256 -- a fact about the bytes actually rendered -- is the load-bearing
receipt. See GitState and COMMIT_QUALIFIER.

Author-voice fence: this file's generated strings never call anything
verified, proven, perfect, secure or certified. Corpus text is quoted as-is
and is the corpus's own voice, never this generator's.

INTERFACES THIS FILE DOES NOT OWN
---------------------------------
reader/templates.py owns render_page(kind, ctx) -> str and reader/theme.css
owns presentation. This file is the producer and conforms to the ctx contract
documented in templates.py; where the two disagreed, templates.py won and this
file changed. Open contract gaps are listed in reader/README.md.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import markdown as md  # noqa: E402  (local, stdlib-only sibling module)

READER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(READER)
DIST = os.path.join(READER, "dist")
PLATES_DIR = os.path.join(READER, "plates")

GENERATOR = "reader/build.py"
BUILD_UTC = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

# Every byte this process writes, as (abs_path, n_bytes): the read-only audit
# surface. A test asserts every entry is inside DIST.
WRITE_LOG = []

# Every url written this build, so a second write to the same url is a failure
# rather than a silent overwrite. See emit().
EMITTED = set()

# Non-fatal observations about the corpus, surfaced on the colophon rather than
# swallowed. A silent skip would be the dishonest option.
BUILD_NOTES = []


def _say(msg):
    """Console output, ASCII only -- this box's stdout is cp1252 (see #2)."""
    sys.stdout.write(msg.encode("ascii", "replace").decode("ascii") + "\n")
    sys.stdout.flush()


def note(kind, detail):
    BUILD_NOTES.append({"kind": kind, "detail": detail})


# --------------------------------------------------------------------------
# 1. READ-ONLY -- the only two doors
# --------------------------------------------------------------------------

def read_bytes(path):
    """The only read door. Mode 'rb'. Never a write mode, never a '+' mode."""
    with open(path, "rb") as fh:
        return fh.read()


def read_text(path):
    """Decode a repo file as UTF-8. Read-only; the repo is never rewritten."""
    return read_bytes(path).decode("utf-8")


def _assert_inside_dist(abs_path):
    """Refuse any write that is not inside DIST. This is the invariant."""
    target = os.path.realpath(abs_path)
    root = os.path.realpath(DIST)
    if target != root and not target.startswith(root + os.sep):
        raise AssertionError(
            "READ-ONLY VIOLATION: build.py attempted to write outside "
            "reader/dist/: %r (dist=%r). The generator is not permitted to "
            "modify the corpus it renders." % (target, root)
        )
    return target


def _ensure_dir(abs_path):
    _assert_inside_dist(abs_path)
    os.makedirs(abs_path, exist_ok=True)


def to_ascii(text):
    """Encode a page to pure ASCII bytes (invariant #2).

    Non-ASCII becomes a numeric character reference: exact and reversible in
    HTML, so the glyph is preserved and only its transport changes.
    """
    return text.encode("ascii", "xmlcharrefreplace")


def _write_bytes(abs_path, data):
    """The ONLY write door in this file. Guarded, ASCII-checked, audited."""
    target = _assert_inside_dist(abs_path)
    if any(b > 0x7F for b in data):
        raise AssertionError(
            "ASCII VIOLATION: %s carries byte(s) >= 0x80. Emission must go "
            "through to_ascii()." % os.path.relpath(target, DIST)
        )
    _ensure_dir(os.path.dirname(target))
    with open(target, "wb") as fh:
        fh.write(data)
    WRITE_LOG.append((target, len(data)))
    return target


def emit(url, text):
    """Write one page. `url` is dist-root-relative, e.g. 'chapter/na-05.html'.

    Writing the same url twice is REFUSED rather than allowed to overwrite.
    Not a defensive habit: two chapters whose H1s slugged to the same id did
    exactly this, and the build cheerfully reported 98 pages written into 95
    files while three chapters vanished with no error at all. A page that
    overwrites another page is a corpus that lost content silently, which is
    the one thing this reader must never do. See allocate_urls().
    """
    if url in EMITTED:
        raise AssertionError(
            "DUPLICATE PAGE: %r was already written by this build. Refusing to "
            "overwrite -- one of the two pages would vanish silently." % url)
    EMITTED.add(url)
    return _write_bytes(os.path.join(DIST, url.replace("/", os.sep)),
                        to_ascii(text))


def emit_asset(url, data_bytes):
    """Emit one non-HTML asset (JS, CSS, JSON, webmanifest, .md).

    Goes through the same _write_bytes() door as pages, so the ASCII fence and
    the READ-ONLY fence both apply. `url` is dist-root-relative. Refuses to
    overwrite -- same rule as emit(), because the whole point is one write
    per URL. Asset bytes MUST be pure ASCII already (this codebase's rule --
    the fleet's file transport corrupts multi-byte UTF-8).
    """
    if url in EMITTED:
        raise AssertionError(
            "DUPLICATE ASSET: %r was already written by this build." % url)
    EMITTED.add(url)
    return _write_bytes(os.path.join(DIST, url.replace("/", os.sep)),
                        bytes(data_bytes))


def copy_reader_asset(src_rel, dst_url, substitutions=None):
    """Copy reader/<src_rel> to dist/<dst_url> byte-for-byte (ASCII-only).

    `substitutions` is an optional {token: replacement} dict applied to the
    text BEFORE emission -- used only for the SW's __CACHE_VERSION__ token, so
    the SW's cache name changes with each build. Every substitution value is
    itself ASCII (a short SHA or literal). ASCII-ness is re-checked by
    _write_bytes() regardless.
    """
    src_abs = os.path.join(READER, src_rel.replace("/", os.sep))
    data = read_bytes(src_abs)
    if any(b > 0x7F for b in data):
        raise AssertionError(
            "ASSET NOT ASCII: reader/%s carries byte(s) >= 0x80. The fleet's "
            "file transport corrupts multi-byte UTF-8; assets copied verbatim "
            "must be ASCII already." % src_rel)
    if substitutions:
        text = data.decode("ascii")
        for k, v in substitutions.items():
            text = text.replace(k, v)
        data = text.encode("ascii")
    return emit_asset(dst_url, data)


# --------------------------------------------------------------------------
# 2. URLS -- relative, because templates.py emits href verbatim
# --------------------------------------------------------------------------
# Canonical urls are dist-root-relative with NO leading slash ('chapter/x.html').
# templates.py renders href exactly as given and uses ctx['root'] only for
# theme.css, so every href must be made relative to the page that carries it.
# Relative links also mean the built site works from a file:// path or any
# subdirectory, not only from a server root.

def root_for(url):
    """The '../' prefix that gets from `url` back to the dist root."""
    return "../" * url.count("/")


def href(target_url, root):
    return root + target_url


# --------------------------------------------------------------------------
# 3. PROVENANCE
# --------------------------------------------------------------------------

def _git(args):
    try:
        p = subprocess.run(
            ["git", "-C", ROOT] + args,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20,
        )
        if p.returncode != 0:
            return None
        return p.stdout.decode("utf-8", "replace").strip()
    except (OSError, subprocess.SubprocessError):
        return None


class GitState(object):
    """Per-file git state, so the commit stamp is never an overclaim.

    A repo-level commit does NOT mean a given file's bytes are in it: at the
    time of writing, lexicon/ and reader/plates/ are untracked. Each page
    states its own file state next to the commit; the sha256 is the receipt
    that always holds.
    """

    def __init__(self):
        self.commit = _git(["rev-parse", "HEAD"])
        self.available = self.commit is not None
        self.tracked, self.modified, self.untracked = set(), set(), set()
        if self.available:
            ls = _git(["ls-files"])
            if ls:
                self.tracked = {p.strip() for p in ls.split("\n") if p.strip()}
            porc = _git(["status", "--porcelain", "--untracked-files=all"])
            if porc:
                for line in porc.split("\n"):
                    if len(line) < 4:
                        continue
                    code, path = line[:2], line[3:].strip().strip('"')
                    (self.untracked if code == "??" else self.modified).add(path)
        self.dirty = bool(self.modified or self.untracked)

    @property
    def short(self):
        return self.commit[:7] if self.commit else "NOT-AVAILABLE"

    def file_state(self, rel_posix):
        """clean | modified | untracked | unknown."""
        if not self.available:
            return "unknown"
        if rel_posix in self.modified:
            return "modified"
        if rel_posix in self.untracked:
            return "untracked"
        if rel_posix in self.tracked:
            return "clean"
        return "untracked"


GIT = None  # set in main()

# The correction that keeps the commit stamp honest. templates.py's provenance
# footer says a page "renders the repository file named above, as it stood at
# that commit" -- which is true only for a tracked, unmodified file. For the
# other three states the qualifier travels WITH the commit, on the page, rather
# than being left to a reader's assumption.
COMMIT_QUALIFIER = {
    "clean": "",
    "modified": (" -- NOTE: this file is MODIFIED in the working tree, so it is "
                 "NOT as it stood at that commit. The sha256 above is the "
                 "receipt for the bytes actually rendered."),
    "untracked": (" -- NOTE: this file is UNTRACKED and is in NO commit. The "
                  "commit is the repo's position, not this file's provenance. "
                  "The sha256 above is this page's only receipt."),
    "unknown": (" -- NOTE: git was not available at build time, so no commit "
                "could be read. The sha256 above is this page's only receipt."),
}


def build_provenance(abs_path, extra_sources=None):
    """Provenance or no page (invariant #3). Raises rather than half-stamp."""
    rel = os.path.relpath(abs_path, ROOT).replace(os.sep, "/")
    data = read_bytes(abs_path)
    state = GIT.file_state(rel)
    prov = {
        "source_path": rel,
        "sha256": hashlib.sha256(data).hexdigest(),
        "commit": (GIT.commit or "NOT-AVAILABLE") + COMMIT_QUALIFIER[state],
        "built_utc": BUILD_UTC,
        # Extra keys templates.py ignores, kept because tests and the colophon
        # read them and because they are the honest detail.
        "bytes": len(data),
        "commit_short": GIT.short,
        "git_state": state,
        "generator": GENERATOR,
        "falsifier": (
            "sha256 the file at %s; a digest other than the one above refutes "
            "this page." % rel),
    }
    if extra_sources:
        prov["sources"] = extra_sources
    for k in ("source_path", "sha256", "commit", "built_utc"):
        if not str(prov.get(k) or "").strip():
            raise AssertionError(
                "PROVENANCE INCOMPLETE for %s (missing %r). A page that cannot "
                "state its provenance does not render." % (rel, k))
    return prov


def generated_provenance(what, digest_over):
    """Provenance for a page with no single source file.

    templates.py's contract: pass source_path='reader/build.py' and its own
    sha256 -- "the generator IS that page's source", which is honest and is
    adopted here. The digest of the derived content travels too, so the page
    still carries a falsifiable receipt of what it was built from.
    """
    self_path = os.path.join(READER, "build.py")
    prov = build_provenance(self_path)
    prov["derived_from"] = what
    prov["content_digest"] = hashlib.sha256(
        json.dumps(digest_over, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()
    prov["falsifier"] = (
        "This page is generated from %s. Rebuild on the same tree: a differing "
        "content digest (%s) means the corpus changed."
        % (what, prov["content_digest"][:12]))
    return prov


# --------------------------------------------------------------------------
# 4. THE TWO SOVEREIGN VOCABULARIES
# --------------------------------------------------------------------------
# NATURA: nature's observed regularities. Twelve classes, per
# encyclopedia/wing-NATURA/NA-00-how-to-read-this-wing.md as amended
# 2026-07-15-A, mirrored by tools/verify_class_vocabulary.py (the repo's own
# falsifier for this list) and independently by templates.NATURA_CLASSES.
NATURA_CLASSES = (
    "OBSERVED-REPLICATED", "OBSERVED-SINGLE", "OBSERVED-CONTESTED",
    "MODELED-CONTESTED", "MODELED", "HYPOTHESIZED", "INADMISSIBLE",
    "NOT-MEASURED", "SUPERSEDED", "NOT-SOURCED", "NOT-CONFIRMED",
    "NOT-LOCATED",
)

# UNI's own build status, governed by encyclopedia/CLAIM-LEDGER.md.
UNI_FENCE = ("proven", "designed", "hypothesized", "not-yet-built")

# Sorted longest-first so MODELED-CONTESTED is never mis-read as MODELED.
_CLASS_RE = re.compile(
    "|".join(re.escape(c) for c in sorted(NATURA_CLASSES, key=len, reverse=True)))


def extract_natura_classes(cell_text):
    """The registered NATURA classes named in a cell, in order.

    Never invents a class. A cell naming none yields [] and is reported as a
    build note -- that is NA-00's own falsifier #2 ("the classes are not
    exhaustive"), kept from firing silently. Rendering is templates.py's
    natura_badge(), which parses the raw cell; this is for the index and notes.
    """
    plain = re.sub(r"[*_`]", "", cell_text)
    seen, out = set(), []
    for m in _CLASS_RE.finditer(plain):
        if m.group(0) not in seen:
            seen.add(m.group(0))
            out.append(m.group(0))
    return out


def assert_vocabularies_sovereign():
    """'hypothesized' is in BOTH vocabularies and means different things.

    templates.py keeps them apart with disjoint CSS trees (.fence / .natura).
    This asserts the two token sets are the only overlap and that this file
    never routes a NATURA class into the UNI fence or back.
    """
    overlap = {v.lower() for v in NATURA_CLASSES} & {v.lower() for v in UNI_FENCE}
    if overlap != {"hypothesized"}:
        note("vocabulary-drift",
             "The overlap between the NATURA classes and the UNI 4-value fence "
             "is %r; it was 'hypothesized' alone when this reader was written. "
             "The badge sovereignty rule may need restating." % sorted(overlap))
    return sorted(overlap)


# --------------------------------------------------------------------------
# 5. THE REPO WALK
# --------------------------------------------------------------------------

CHAPTER_DIRS = (
    ("encyclopedia", "The Encyclopedia"),
    ("cookbook", "The Cookbook"),
)

# The two sovereign ledgers render as kind='ledger', which forces each to
# declare the vocabulary it speaks before it may badge a row.
LEDGER_FILES = {
    "encyclopedia/CLAIM-LEDGER.md": ("uni", "UNI's own build status"),
    "encyclopedia/NATURE-LEDGER.md": ("natura", "Nature's observed regularities"),
}

# Everything in the repo that is NOT rendered is listed on the colophon with
# its sha256 and this reason. A silent omission would break "always the real
# as-is repo knowledge" -- so nothing is omitted silently.
NOT_RENDERED_REASON = {
    "prompts": "Operator prompt drafts and orchestration instructions: working "
               "material addressed to a builder, not encyclopedia content.",
    "deploy": "Deployment runbooks carrying host and endpoint placeholders. "
              "Not corpus, and not published by the reader.",
    "tools": "Build and verification scripts. Listed with their sha256; run "
             "them from the repo, not from a web page.",
    "gpt": "The GPT consultant pack (K20 is 377 KB of machine-readable JSON). "
           "Listed with its sha256; a data artifact, not a chapter.",
    "reader": "The reader's own source, including this generator.",
    "dist": "Build output.",
    ".gitignore": "Repo configuration.",
}

REGISTERS = (
    # The operator's stated order: Sanskrit, Latin, English, Hindi, Spanish.
    ("sa", "Sanskrit", "sanskrit"),
    ("la", "Latin", "latin"),
    ("en", "English", "english"),
    ("hi", "Hindi", "hindi"),
    ("es", "Spanish", "spanish"),
)


def _chapter_id(rel_posix, title):
    """The chapter's own id, taken from its H1 -- never invented.

    The corpus convention is 'ID<space><separator><space>Title':
        'NA-05 -- The ratios...'   'CN-11 -- Humans...'
        'S-L0 - Molecular...'      'mu1 - The Evidence Constitution...'
        'L0 -- Molecular / genome' 'TA-A - The no-API content model'

    THE SEPARATOR MUST BE SPACE-DELIMITED, and that is the whole subtlety. An
    earlier version allowed a bare '[-:]' and read '# UNI-GPT Consult --
    2026-06-27' as id 'UNI' -- matching the hyphen INSIDE 'UNI-GPT' -- which
    collided with UNI-GPT-CONSULT-PACKAGE.md and silently overwrote a chapter.
    Requiring spaces around the separator makes 'UNI-GPT Consult' fail the
    id test (it contains a space) and fall back to its filename, which is
    unique by construction.
    """
    m = re.match(r"^\s*(\S{1,12})\s+(?:[-–—:]|--)\s+\S", title)
    if m and re.match(r"^[A-Za-z][A-Za-z0-9.\-]*$", m.group(1)):
        return m.group(1)
    return os.path.splitext(os.path.basename(rel_posix))[0]


def allocate_urls(found):
    """Assign one unique url per chapter. Collisions are resolved, never lost.

    Two chapters may legitimately share an id-slug: encyclopedia/00-INDEX.md
    and cookbook/00-INDEX.md both title out to '00-index', as do the two
    MASTER-PLAN.md files. Left alone, the second silently overwrites the first
    and a chapter vanishes from the reader with no error -- which is exactly
    the failure this corpus exists to refuse.

    When a base slug is claimed by more than one file, EVERY member of that
    group is disambiguated by its section (never just the later one), so the
    urls do not depend on walk order and stay stable across builds.
    """
    base = {}
    for e in found:
        if os.path.exists(e["abs"]):
            head = read_text(e["abs"]).split("\n", 1)[0].lstrip("#").strip()
            cid = _chapter_id(e["rel"], head)
        else:
            cid = os.path.splitext(os.path.basename(e["rel"]))[0]
        e["_id"] = cid
        base.setdefault(md.slugify(cid), []).append(e)

    urls = {}
    for slug, group in sorted(base.items()):
        for e in group:
            folder = "ledger" if e["rel"] in LEDGER_FILES else "chapter"
            if len(group) == 1:
                use = slug
            else:
                use = md.slugify("%s-%s" % (e["wing"].replace("/", "-"),
                                            e["_id"]))
            urls[e["rel"]] = "%s/%s.html" % (folder, use)
        if len(group) > 1:
            note("url-collision",
                 "The id-slug %r is claimed by %d files (%s). Each is given a "
                 "section-qualified url instead, so no chapter is overwritten."
                 % (slug, len(group), ", ".join(x["rel"] for x in group)))

    if len(set(urls.values())) != len(urls):
        dupes = [u for u in urls.values() if list(urls.values()).count(u) > 1]
        raise AssertionError(
            "URL ALLOCATION FAILED: %r is still claimed twice after "
            "disambiguation. A chapter would be silently overwritten."
            % sorted(set(dupes)))
    return urls


def build_corpus_tree(chapters, root):
    """The corpus tree passed as ctx['corpus_tree'] to every page.

    Shape (matches templates._sidebar's reader):
        [{"name": wing, "title": wing,
          "chapters": [{"id", "title", "href", "path"}]}]

    Order preserves discover_chapters() order (repo walk order), so the same
    tree renders in the same sequence every build.  `root` is the page's
    '../'-prefix (see root_for()), so the href is page-relative -- the same
    convention templates.py uses everywhere else.
    """
    by_wing = []
    seen = {}
    for c in chapters:
        if c.missing:
            continue
        if c.wing not in seen:
            seen[c.wing] = {"name": c.wing, "title": c.wing, "chapters": []}
            by_wing.append(seen[c.wing])
        seen[c.wing]["chapters"].append({
            "id": c.id, "title": c.title,
            "href": root + c.url, "path": c.rel,
        })
    return by_wing


def build_search_index(chapters, plates):
    """The concordance data the offline search overlay in app.js reads.

    One row per live chapter, plus one row per plate. `body` is the plain-text
    body trimmed to ~300 chars -- the corpus's own words, HTML-stripped so the
    grep matches what the reader will actually see.
    """
    rows = []
    for c in chapters:
        if c.missing or c.doc is None:
            continue
        text = re.sub(r"<[^>]+>", " ", c.doc.html)
        text = re.sub(r"\s+", " ", text).strip()
        rows.append({
            "path": c.url,
            "title": c.title,
            "body": text[:300],
        })
    for p in plates:
        cap = re.sub(r"\s+", " ", (p.get("caption") or "")).strip()
        rows.append({
            "path": p["url"],
            "title": "%s -- %s" % (p["id"], p["title"]),
            "body": cap[:300],
        })
    return rows


def _abstract_of(source):
    """The leading blockquote, where a chapter has one (38 of 90 do).

    There is NO YAML front matter anywhere in this corpus -- measured: 0 of 90
    files open with '---'. So chapter metadata is derived from the document's
    own structure: the H1 is the title, and a blockquote before the first rule
    or heading is the abstract. A chapter without one gets None, never a
    fabricated summary.
    """
    lines = source.split("\n")[1:]
    buf = []
    for ln in lines[:12]:
        if ln.startswith(">"):
            buf.append(ln)
            continue
        if buf:
            break
    return "\n".join(buf) if buf else None


_NUMBERS_COLS = ("symbol", "value", "units", "scope", "class", "source",
                 "falsifier")


def parse_numbers_tables(doc, rel_posix):
    """Extract the '## The numbers' tables -- the corpus's own claim tables.

    Header shape is NORMALISED, not exact-matched: of the 23 tables, 21 use
    'Symbol|Value|Units|Scope|Class|Source|Falsifier', NA-01 uses
    'Scope (where it holds)', and NA-03 uses lowercase headers. Exact matching
    would silently drop two chapters' numbers.

    Cells are handed on as the corpus wrote them. The Class cell goes to
    templates.natura_badge(), which parses emphasis, compounds and qualifiers.
    """
    rows_out = []
    for t in doc.tables:
        h = t.get("heading") or ""
        if not h.lower().startswith("the numbers"):
            continue
        norm = [re.split(r"[ (]", c.strip().lower())[0] for c in t["headers"]]
        if tuple(norm) != _NUMBERS_COLS:
            note("numbers-table-shape",
                 "%s: a '## The numbers' table has headers %r, which do not "
                 "match the corpus convention %r. It still renders in the "
                 "chapter body; its rows are not carried into the claim index."
                 % (rel_posix, t["headers"], list(_NUMBERS_COLS)))
            continue
        idx = {k: norm.index(k) for k in _NUMBERS_COLS}
        for r in t["rows"]:
            if len(r) < len(_NUMBERS_COLS):
                note("numbers-row-short",
                     "%s: a numbers row has %d cells, expected %d. Skipped from "
                     "the claim index; the chapter body still shows it."
                     % (rel_posix, len(r), len(_NUMBERS_COLS)))
                continue
            cls_cell = r[idx["class"]]
            classes = extract_natura_classes(cls_cell)
            if not classes:
                note("unregistered-class",
                     "%s: class cell %r names none of NA-00's twelve registered "
                     "classes. Carried verbatim and rendered as-is; not badged."
                     % (rel_posix, cls_cell[:90]))
            rows_out.append({
                # templates._numbers_table reads these exact keys.
                "symbol": re.sub(r"`", "", r[idx["symbol"]]).strip(),
                "value_html": md.render_inline(r[idx["value"]]),
                # units/scope render their inline markdown like every other
                # cell. They were passed as raw source text, so a real cell
                # ('**ideal** regular tetrahedron') showed its asterisks on the
                # page. The corpus wrote emphasis; the reader now shows it.
                "units_html": md.render_inline(r[idx["units"]]),
                "scope_html": md.render_inline(r[idx["scope"]]),
                "units": r[idx["units"]],
                "scope": r[idx["scope"]],
                "class": cls_cell,
                "source_html": md.render_inline(r[idx["source"]]),
                "falsifier_html": md.render_inline(r[idx["falsifier"]]),
                # build.py's own use (A-Z, counts); templates ignores these.
                "_classes": classes,
            })
    return rows_out


class Chapter(object):
    __slots__ = ("id", "title", "url", "rel", "abs", "section", "wing", "doc",
                 "provenance", "abstract_md", "numbers", "kind", "missing")

    def __init__(self, **kw):
        for k in self.__slots__:
            setattr(self, k, kw.get(k))


def discover_chapters():
    """Walk the corpus in the repo's own sort order -- stated, not guessed."""
    found = []
    for top, label in CHAPTER_DIRS:
        base = os.path.join(ROOT, top)
        if not os.path.isdir(base):
            note("missing-section", "%s/ is not present in this repo." % top)
            continue
        for dp, dn, fn in os.walk(base):
            dn[:] = sorted(d for d in dn if not d.startswith("."))
            for f in sorted(fn):
                if not f.endswith(".md"):
                    continue
                abs_p = os.path.join(dp, f)
                wing = os.path.relpath(dp, base).replace(os.sep, "/")
                found.append({
                    "abs": abs_p,
                    "rel": os.path.relpath(abs_p, ROOT).replace(os.sep, "/"),
                    "section": label,
                    "wing": top if wing == "." else "%s/%s" % (top, wing),
                })
    return found


def load_chapter(entry, resolver, url):
    """Render one chapter. `url` comes from allocate_urls() and is authoritative.

    The resolver's root is set from `url` BEFORE the parse, because the body's
    links are rewritten during the parse. Setting it afterwards left every
    cross-chapter link in a chapter/ page pointing at 'ledger/x.html' instead
    of '../ledger/x.html' -- every one of them a 404.
    """
    abs_p, rel = entry["abs"], entry["rel"]
    kind = "ledger" if rel in LEDGER_FILES else "chapter"
    if not os.path.exists(abs_p):
        # test_partial_corpus: a missing chapter is a PENDING page, not a crash.
        cid = entry.get("_id") or os.path.splitext(os.path.basename(rel))[0]
        return Chapter(id=cid, title=cid, url=url, rel=rel, abs=abs_p,
                       section=entry["section"], wing=entry["wing"], doc=None,
                       provenance=None, abstract_md=None, numbers=[],
                       kind=kind, missing=True)
    source = read_text(abs_p)
    resolver.root = root_for(url)
    resolver.current_dir = os.path.dirname(rel) or "."
    doc = md.parse(source, link_resolver=resolver)
    title = doc.title or os.path.splitext(os.path.basename(rel))[0]
    return Chapter(
        id=entry.get("_id") or _chapter_id(rel, title), title=title, url=url,
        rel=rel, abs=abs_p, section=entry["section"], wing=entry["wing"],
        doc=doc, provenance=build_provenance(abs_p),
        abstract_md=_abstract_of(source),
        numbers=parse_numbers_tables(doc, rel), kind=kind, missing=False)


# --------------------------------------------------------------------------
# 6. CROSS-REFERENCES
# --------------------------------------------------------------------------

class LinkResolver(object):
    """Rewrite in-repo links to reader URLs; never present a dead link as live.

    Hrefs are resolved to dist-root-relative urls and then made page-relative
    with `root`, because templates.py emits href verbatim.

    An off-site href (a DOI, a journal) stays an <a>: it is user-initiated
    navigation, not an asset the page loads. Nothing is fetched at page view,
    which is what the offline-first fence is actually about.
    """

    def __init__(self):
        self.by_rel = {}
        self.current_dir = "."
        self.root = ""
        self.xrefs = []

    def register(self, rel_posix, url):
        self.by_rel[rel_posix] = url

    def __call__(self, target):
        if not target or target.startswith("#"):
            return None
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:", target):
            return (target, "xref-external")
        path, _, frag = target.partition("#")
        if not path:
            return None
        rel = os.path.normpath(
            os.path.join(self.current_dir, path)).replace(os.sep, "/")
        if rel in self.by_rel:
            url = self.root + self.by_rel[rel]
            if frag:
                url += "#" + md.slugify(frag)
            self.xrefs.append((self.current_dir, rel))
            return (url, "xref")
        # A repo file the reader does not render: shown as text carrying its
        # path, never as a link that 404s.
        return (None, "xref-unrendered")


# --------------------------------------------------------------------------
# 7. LEXICON -- the five registers
# --------------------------------------------------------------------------

def load_lexicon():
    """Read lexicon/CONCEPTS.json + lexicon/terms/*.json exactly as they are.

    Every count on a register page is computed from these bytes at build time.
    Nothing about the lexicon's completeness is hardcoded, because the honest
    state is that most of it is not done, and that state must be free to change
    under the reader without the reader lying about it.
    """
    lex = {"concepts": [], "entries": [], "files": [], "meta": {},
           "status_vocabulary": {}}
    cpath = os.path.join(ROOT, "lexicon", "CONCEPTS.json")
    if os.path.exists(cpath):
        data = json.loads(read_text(cpath))
        lex["concepts"] = data.get("concepts", [])
        lex["meta"] = {
            "what_this_is": data.get("what_this_is", ""),
            "schema_version": data.get("schema_version"),
            "counts_at_authorship": data.get("counts_at_authorship", {}),
            "domains_registered": data.get("domains_registered", []),
            "falsifiers": data.get("falsifiers", []),
        }
        lex["files"].append(build_provenance(cpath))
    else:
        note("lexicon-missing",
             "lexicon/CONCEPTS.json is not present; the register pages render "
             "as PENDING rather than inventing a lexicon.")

    tdir = os.path.join(ROOT, "lexicon", "terms")
    if os.path.isdir(tdir):
        for f in sorted(os.listdir(tdir)):
            if not f.endswith(".json"):
                continue
            p = os.path.join(tdir, f)
            data = json.loads(read_text(p))
            lex["files"].append(build_provenance(p))
            lex["status_vocabulary"].update(data.get("status_vocabulary", {}))
            for e in data.get("entries", []):
                e["_file"] = os.path.relpath(p, ROOT).replace(os.sep, "/")
                e.setdefault("reviewer", data.get("reviewer"))
                lex["entries"].append(e)
    lex["entries"].sort(key=lambda e: str(e.get("concept_id") or ""))
    return lex


def register_counts(lex, field):
    """CITED / COINED / PENDING-CITATION / NOT-ATTEMPTED -- counted, not claimed."""
    counts = {}
    for e in lex["entries"]:
        v = e.get(field)
        st = v.get("status", "NOT-ATTEMPTED") if isinstance(v, dict) \
            else "NOT-ATTEMPTED"
        counts[st] = counts.get(st, 0) + 1
    return counts


# --------------------------------------------------------------------------
# 8. PLATES
# --------------------------------------------------------------------------

_SVG_FENCE_PATTERNS = (
    (re.compile(r"<\s*script", re.I), "a <script> element"),
    (re.compile(r"\son[a-z]+\s*=", re.I), "an on* event handler"),
    (re.compile(r"@import", re.I), "an @import"),
    (re.compile(r"url\(\s*['\"]?\s*https?:", re.I), "a remote url()"),
    (re.compile(r"(?:xlink:)?href\s*=\s*['\"]\s*https?:", re.I), "a remote href"),
    (re.compile(r"<\s*(?:image|use)[^>]+https?:", re.I), "a remote image/use"),
    (re.compile(r"<\s*foreignObject", re.I), "a <foreignObject>"),
)

# The SVG namespace is an identifier, never dereferenced. It is the one http
# string a plate may carry, and it is allowed by name rather than by pattern.
_SVG_NS = 'xmlns="http://www.w3.org/2000/svg"'


def check_svg_fence(svg_text):
    """Verify the design-only fence on the SVG bytes; never trust the claim.

    Each plate's JSON asserts 'script_elements: 0'. That is the plate's own
    narrative about itself (Class-G). This function is the observation
    (Class-B). M9 ranks tool state above own narrative, so where they disagree
    the observation wins and the plate is not inlined.
    """
    probe = svg_text.replace(_SVG_NS, "")
    return [what for rx, what in _SVG_FENCE_PATTERNS if rx.search(probe)]


def load_plates():
    """Load every plate, in the corpus's own sort order.

    The ordinal assigned here (1..n) is THE plate number for the whole build --
    the plate page and every chapter that references the plate must print the
    same one, or the same artwork is two different plates to a reader. It is
    assigned once, here, rather than by each caller's enumerate().
    """
    plates = []
    if not os.path.isdir(PLATES_DIR):
        note("plates-missing", "reader/plates/ is not present; no plates render.")
        return plates
    for f in sorted(os.listdir(PLATES_DIR)):
        if not f.endswith(".json"):
            continue
        pid = os.path.splitext(f)[0]
        jpath = os.path.join(PLATES_DIR, f)
        spath = os.path.join(PLATES_DIR, pid + ".svg")
        meta = json.loads(read_text(jpath))
        svg_inline, fence_hits, svg_prov = None, [], None
        if os.path.exists(spath):
            svg = read_text(spath)
            svg_prov = build_provenance(spath)
            fence_hits = check_svg_fence(svg)
            if fence_hits:
                note("plate-fence",
                     "%s.svg trips the design-only fence (%s) and is NOT "
                     "inlined. The plate page renders its caption and claims."
                     % (pid, "; ".join(fence_hits)))
            else:
                svg_inline = svg
        else:
            note("plate-missing-svg",
                 "%s.json has no %s.svg beside it; that plate renders PENDING."
                 % (pid, pid))
        extra = [{"path": svg_prov["source_path"], "sha256": svg_prov["sha256"]}] \
            if svg_prov else None
        plates.append({
            "id": meta.get("id", pid),
            "title": meta.get("title", pid),
            "subtitle": meta.get("subtitle"),
            "caption": meta.get("caption", ""),
            "url": "plate/%s.html" % md.slugify(pid),
            "source_chapters": meta.get("source_chapters", []),
            "source_paths": plate_source_paths(meta.get("id", pid),
                                               meta.get("source_chapters", [])),
            "claims": meta.get("claims", []),
            "marginal_note": meta.get("marginal_note"),
            "not_claimed": meta.get("not_claimed", []),
            "design_fence": meta.get("design_fence") or meta.get("design_only"),
            "svg_markup": svg_inline,
            "fence_hits": fence_hits,
            "provenance": build_provenance(jpath, extra_sources=extra),
        })
    for n, p in enumerate(plates, 1):
        p["number"] = n
    return plates


def plate_source_paths(plate_id, source_chapters):
    """Normalise a plate's source_chapters to repo-relative paths.

    The ten plates carry TWO shapes, both authored by hand and both real:
      - a list of strings, each a path plus a free-text annotation, e.g.
        'encyclopedia/NATURE-LEDGER.md (rows NA04-01 ...)' -- and in PL-09, a
        path followed by TWO spaces before the annotation;
      - a list of dicts with a 'path' key (PL-02, PL-04, PL-08, PL-10).
    Assuming either shape alone drops four plates' cross-references, so both
    are handled and any third shape is reported rather than guessed at.
    """
    out = []
    for s in source_chapters or []:
        if isinstance(s, dict):
            p = s.get("path")
        elif isinstance(s, str):
            p = s.strip().split()[0] if s.strip() else None
        else:
            note("plate-source-shape",
                 "%s: a source_chapters entry is a %s -- neither a string nor a "
                 "dict with a 'path'. Not linked."
                 % (plate_id, type(s).__name__))
            continue
        if p:
            out.append(p.strip())
    return out


# --------------------------------------------------------------------------
# 9. OUTPUT FENCE -- scan what was emitted, not what was intended
# --------------------------------------------------------------------------

# Patterns that can only be MARKUP. Escaped prose cannot produce them: a
# chapter that discusses "<script>" is emitted as "&lt;script&gt;" and cannot
# match "<\s*script".
_MARKUP_REF_PATTERNS = (
    # REMOTE <script src> only. Same-origin, relative sources are permitted:
    # the reader emits `app.js`, `sw.js`, and `search-index.json` as its own
    # assets and loads them from disk-adjacent paths, which is exactly the
    # offline-first shape this fence exists to protect. The docstring below
    # in fence_scan() names "a remote <script src>" as what this catches; the
    # earlier unconditional pattern was stricter than the stated intent, and
    # forced the scrivener shell to inline its own script as a workaround. The
    # relaxed pattern still fires on `https://cdn/x.js` and on `//host/x.js`,
    # which is what the fence was written to keep out.
    # POSITIVE CONTROL: test_no_external_refs_positive_control asserts the
    # relaxed pattern still catches both remote shapes.
    (re.compile(r"""<\s*script[^>]*\ssrc\s*=\s*['"]?\s*(?:https?:)?//""", re.I),
     "a remote <script src>"),
    # An on* handler in a TAG. Added 2026-07-15-D, and the reason is the finding:
    # _SVG_FENCE_PATTERNS has carried an on* pattern since it was written, this list
    # never did, and search.html shipped `<form ... onsubmit="return false;">` straight
    # through the fence that exists to forbid exactly that. One fence caught it; the
    # other was not looking. Removing only the attribute would have left the hole.
    #
    # NOT the SVG fence's pattern, and the difference is load-bearing. There it is a
    # bare r"\son[a-z]+\s*=", which is safe on a plate (pure markup, no prose). Here the
    # markup patterns run on the WHOLE DOCUMENT, and that is only sound because escaped
    # text cannot forge a tag (see fence_scan). A bare \son[a-z]+= is NOT a tag pattern:
    # entity-escaping does not touch `onclick=`, so a chapter that merely DISCUSSES an
    # on* handler in prose would trip it -- the same false positive the '@import' note
    # below records, which fired on a plate for describing a fence it honours. Anchoring
    # to `<tag ...` restores the invariant: [^>]* cannot cross a '>', so prose inside an
    # element can never reach the handler position.
    (re.compile(r"<\s*[a-z][^>]*\son[a-z]+\s*=", re.I), "an on* event handler"),
    (re.compile(r"""<\s*link[^>]*href\s*=\s*['"]?\s*(?:https?:)?//""", re.I),
     "a remote <link href> (stylesheet/font/icon)"),
    (re.compile(r"""<\s*img[^>]*src\s*=\s*['"]?\s*(?:https?:)?//""", re.I),
     "a remote <img src>"),
    (re.compile(r"<\s*iframe", re.I), "an <iframe>"),
    (re.compile(r"\ssrcset\s*=", re.I), "a srcset"),
    (re.compile(r"<\s*(?:audio|video|embed|object)\b", re.I),
     "an embedded media element"),
)

# Patterns that are only live INSIDE a style context (a <style> block or a .css
# file). In body text '@import' is six inert characters.
_STYLE_REF_PATTERNS = (
    (re.compile(r"@import", re.I), "an @import"),
    (re.compile(r"""url\(\s*['"]?\s*(?:https?:)?//""", re.I), "a remote url()"),
)

_STYLE_BLOCK_RE = re.compile(r"<style[^>]*>(.*?)</style>", re.S | re.I)
_CSS_COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)


def fence_scan(text, where, css=False):
    """Invariant #4, checked on emitted bytes rather than on intent.

    THE INSTRUMENT IS SCOPED, AND THAT IS THE POINT. An earlier version grepped
    the whole page for '@import' and fired on plate/pl-01.html -- where the
    string appears inside PL-01's own design_fence note, as escaped prose
    reading "no @import". That was a false positive: the reader was flagged for
    *describing* a fence it honours. A negative is only a finding once the
    instrument is known to measure the right thing, so:
      * markup patterns run on the whole document -- escaped text cannot forge
        a tag;
      * style patterns run ONLY inside <style> blocks, or over the whole input
        when css=True, and COMMENTS are stripped first. theme.css opens with
        the comment "NO WEBFONT. NO CDN. NO @import. NO url() TO A NETWORK."
        and tripped this scan on its own promise. A comment fetches nothing.

    Deliberately NOT flagged, each exclusion reasoned:
      * <a href="https://doi.org/..."> is a hyperlink, not an asset reference.
        Nothing is fetched at page load, and stripping the corpus's citations
        would damage the scholarship this fence exists to protect.
      * xmlns="http://www.w3.org/2000/svg" is a namespace identifier, never
        dereferenced (reader/plates/PL-01.json:design_fence says so, and
        check_svg_fence() verifies it independently rather than believing it).
      * An inline <script> with no src: templates.py ships a theme toggle and
        an offline search filter. Both are local and fetch nothing; a remote
        <script src> is what this catches.
    """
    hits = []
    if css:
        style_text = [_CSS_COMMENT_RE.sub(" ", text)]
        markup = ""
    else:
        markup = _HTML_COMMENT_RE.sub(" ", text.replace(_SVG_NS, ""))
        style_text = [_CSS_COMMENT_RE.sub(" ", b)
                      for b in _STYLE_BLOCK_RE.findall(text)]

    def hit(rx, what, hay):
        m = rx.search(hay)
        if m:
            hits.append("%s near %r"
                        % (what, hay[max(0, m.start() - 50):m.end() + 30]))

    for rx, what in _MARKUP_REF_PATTERNS:
        hit(rx, what, markup)
    for block in style_text:
        for rx, what in _STYLE_REF_PATTERNS:
            hit(rx, what, block)
    if hits:
        raise AssertionError(
            "EXTERNAL-REFERENCE FENCE TRIPPED in %s: %s" % (where, "; ".join(hits)))


# --------------------------------------------------------------------------
# 10. THE BUILD
# --------------------------------------------------------------------------

def _import_templates():
    try:
        import templates
    except ImportError as e:
        raise SystemExit(
            "reader/templates.py is required and could not be imported (%s).\n"
            "Contract: templates.render_page(kind, ctx) -> str, for kind in\n"
            "  chapter | ledger | index | az | lexicon | plate | colophon | "
            "search\nSee reader/README.md." % e)
    if not hasattr(templates, "render_page"):
        raise SystemExit(
            "reader/templates.py defines no render_page(kind, ctx) -> str.")
    return templates


def main(argv=None):
    global GIT
    ap = argparse.ArgumentParser(description="Build the UNI reader (read-only).")
    ap.add_argument("--out", default=DIST,
                    help="output dir; must be reader/dist")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    if os.path.realpath(args.out) != os.path.realpath(DIST):
        raise SystemExit("--out must be reader/dist. This generator writes "
                         "nowhere else.")

    t0 = time.time()
    del WRITE_LOG[:]
    del BUILD_NOTES[:]
    EMITTED.clear()
    GIT = GitState()
    templates = _import_templates()
    assert_vocabularies_sovereign()

    # -- clear dist: the only destructive act, and it is fenced twice --------
    _assert_inside_dist(DIST)
    if os.path.basename(os.path.realpath(DIST)) != "dist":
        raise SystemExit("refusing to clear %r: it is not named 'dist'" % DIST)
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    _ensure_dir(DIST)

    # -- walk ---------------------------------------------------------------
    resolver = LinkResolver()
    found = discover_chapters()

    # Allocate every url up front, so a cross-reference resolves on the first
    # pass and no two chapters can claim the same page.
    urls = allocate_urls(found)
    for rel, url in urls.items():
        resolver.register(rel, url)

    chapters = [load_chapter(e, resolver, urls[e["rel"]]) for e in found]
    live = [c for c in chapters if not c.missing]
    plates = load_plates()
    lex = load_lexicon()

    # -- shared chrome, rebuilt per page because href must be page-relative --
    def nav_for(root):
        return [
            {"href": href("index.html", root), "label": "Front"},
            {"href": href("az.html", root), "label": "A-Z index"},
            {"href": href("search.html", root), "label": "Concordance"},
            {"href": href("colophon.html", root), "label": "Colophon"},
        ]

    def registers_for(root):
        return [{"code": code, "label": name,
                 "href": href("lexicon/%s.html" % code, root),
                 "pending": field != "english",
                 "counts": register_counts(lex, field)}
                for code, name, field in REGISTERS]

    site = {"title": "The UNI Encyclopedia & Cookbook",
            "subtitle": "A reader for the repo, rendered from the repo."}

    n_pages = 0

    def render(kind, ctx, url):
        nonlocal n_pages
        root = root_for(url)
        ctx.setdefault("root", root)
        ctx.setdefault("site", site)
        ctx.setdefault("nav", nav_for(root))
        ctx.setdefault("registers", registers_for(root))
        ctx.setdefault("register", "en")
        # The corpus tree the sidebar and TOC overlay read. Rebuilt with the
        # page's root so every href is page-relative, matching templates.py's
        # convention for hrefs across the whole reader.
        ctx.setdefault("corpus_tree", build_corpus_tree(chapters, root))
        html = templates.render_page(kind, ctx)
        if not isinstance(html, str):
            raise AssertionError(
                "templates.render_page(%r) returned %s, expected str."
                % (kind, type(html).__name__))
        fence_scan(html, url)
        emit(url, html)
        n_pages += 1

    # -- chapters + ledgers -------------------------------------------------
    for i, c in enumerate(chapters):
        root = root_for(c.url)
        resolver.root = root
        resolver.current_dir = os.path.dirname(c.rel) or "."
        prev_c = chapters[i - 1] if i > 0 else None
        next_c = chapters[i + 1] if i + 1 < len(chapters) else None

        if c.missing:
            render("chapter", {
                "id": c.id, "title": c.title, "wing": c.wing,
                "pending": True,
                "pending_reason": (
                    "The build registry lists %s, but the file is not in the "
                    "repo at build time. Falsifier: add that file and rebuild; "
                    "this page then renders its content." % c.rel),
                "provenance": {
                    "source_path": c.rel, "sha256": "",
                    "commit": (GIT.commit or "NOT-AVAILABLE"),
                    "built_utc": BUILD_UTC,
                },
                "body_html": "",
            }, c.url)
            continue

        # The abstract is re-rendered with this page's root so its links work.
        abstract_html = md.render(c.abstract_md, resolver) if c.abstract_md else None
        # 'number' is the plate's ORDINAL, which templates._plate_figures turns
        # into a roman numeral. Passing p['id'] ('PL-01') here made _roman()
        # int() it, fail, and return '' -- so every chapter plate captioned
        # itself 'Plate .' with no number at all, silently. plate_id travels
        # too, as the fallback templates.py reaches for.
        chapter_plates = [
            {"href": href(p["url"], root), "title": p["title"],
             "label": "%s -- %s" % (p["id"], p["title"]),
             "caption": p["caption"], "number": p["number"],
             "plate_id": p["id"]}
            for p in plates if c.rel in p["source_paths"]]

        if c.kind == "ledger":
            vocab, describes = LEDGER_FILES[c.rel]
            render("ledger", {
                "title": c.title, "ledger_title": c.title,
                "vocabulary": vocab,
                # The whole document, rendered as-is: prose, every table, every
                # fence. The ledger is the authority, so it is carried whole
                # rather than reduced to a row set.
                "intro_html": c.doc.html,
                "columns": [], "rows": [],
                "describes": describes,
                "provenance": c.provenance,
            }, c.url)
            continue

        render("chapter", {
            "id": c.id, "title": c.title, "wing": c.wing,
            "abstract_html": abstract_html,
            "body_html": c.doc.html,
            "numbers": c.numbers,
            "plates": chapter_plates,
            "see_also": [
                {"href": href(resolver.by_rel[r], root),
                 "label": next((x.title for x in chapters if x.rel == r), r)}
                for r in sorted({rel for cd, rel in resolver.xrefs
                                 if cd == (os.path.dirname(c.rel) or ".")})
                if r != c.rel and r in resolver.by_rel],
            "prev": {"href": href(prev_c.url, root), "label": prev_c.title}
                    if prev_c else None,
            "next": {"href": href(next_c.url, root), "label": next_c.title}
                    if next_c else None,
            "provenance": c.provenance,
        }, c.url)

    # -- plates -------------------------------------------------------------
    for p in plates:
        root = root_for(p["url"])
        render("plate", {
            "plate_id": p["id"], "title": p["title"], "subtitle": p["subtitle"],
            # The ordinal load_plates() assigned -- the same one every chapter
            # cites, so a plate has ONE number across the whole volume.
            "number": p["number"],
            "caption": p["caption"],
            "svg_markup": p["svg_markup"],
            "claims": p["claims"],
            "marginal_note": p["marginal_note"],
            "not_claimed": p["not_claimed"],
            "design_fence": p["design_fence"],
            "source_chapters": [
                {"href": href(resolver.by_rel[sp], root),
                 "label": next((c.title for c in chapters if c.rel == sp), sp)}
                if sp in resolver.by_rel else {"label": sp}
                for sp in p["source_paths"]],
            "pending": p["svg_markup"] is None,
            "pending_reason": (
                "The plate's SVG is absent, or it trips the design-only fence "
                "(%s) and is therefore not inlined. Falsifier: supply a "
                "script-free, reference-free %s.svg and rebuild."
                % ("; ".join(p["fence_hits"]) or "no artwork found", p["id"]))
                if p["svg_markup"] is None else None,
            "provenance": p["provenance"],
        }, p["url"])

    # -- the five registers -------------------------------------------------
    for code, name, field in REGISTERS:
        url = "lexicon/%s.html" % code
        root = root_for(url)
        counts = register_counts(lex, field)
        pending = field != "english"
        render("lexicon", {
            "title": "%s register" % name,
            "register": code,
            "entries": lex["entries"],
            # templates._render_lexicon reads counts['status_census'] -- a
            # five-register census of what each register actually carries,
            # counted from lexicon/ at build time. Passing the flat per-register
            # dict left that section dark on every page: the one table that
            # states the honest shape of the whole lexicon never rendered. The
            # census is keyed by the field name templates.py maps each register
            # code to.
            "counts": {
                "status_census": {f: register_counts(lex, f)
                                  for _c, _n, f in REGISTERS},
                "register": counts,
            },
            "file_id": ", ".join(sorted({e.get("_file", "") for e in lex["entries"]}))
                       or "lexicon/",
            "status_vocabulary": lex["status_vocabulary"],
            "lexicon_meta": lex["meta"],
            "pending": pending,
            "pending_reason": (
                "English is the only register with full chapter prose. The %d "
                "chapters of this corpus are NOT translated into %s and are not "
                "shown here as if they were; this page carries the canonical "
                "terminology from lexicon/, each term with its own status and "
                "citation. Machine-translating the chapters and presenting the "
                "output as a register would be fabrication, so it is not done. "
                "No back-translation test in lexicon/ has been run, and no "
                "Sanskritist, Latinist, Hindi or Spanish lexicographer has "
                "reviewed any entry: every rendering is PENDING / SUB EXAMINE. "
                "Of the %d concepts registered in lexicon/CONCEPTS.json, %d "
                "carry an entry in any register. Falsifier: run each entry's "
                "back_translation_test and record the result."
                % (len(live), name, len(lex["concepts"]), len(lex["entries"]))
            ) if pending else None,
            "provenance": lex["files"][0] if lex["files"] else generated_provenance(
                "lexicon/ (absent from this repo)", []),
        }, url)

    # -- A-Z index ----------------------------------------------------------
    az = []

    def az_add(term, url, kind, note_text=None):
        term = re.sub(r"[`*_]", "", (term or "")).strip()
        if term:
            az.append({"term": term, "href": href(url, ""), "kind": kind,
                       "note": note_text})

    for c in live:
        az_add(c.title, c.url, c.section, c.wing)
        for r in c.numbers:
            az_add(r["symbol"], c.url, "number",
                   "%s -- the numbers%s" % (c.id,
                                            "; " + ", ".join(r["_classes"])
                                            if r["_classes"] else ""))
    for p in plates:
        az_add(p["title"], p["url"], "plate", "Plate %s" % p["id"])
    for e in lex["entries"]:
        az_add(e.get("english_term"), "lexicon/en.html", "lexicon",
               e.get("concept_id"))
    az.sort(key=lambda x: (x["term"].lower(), x["kind"]))

    render("az", {
        "title": "A-Z index", "entries": az,
        "provenance": generated_provenance(
            "every rendered page: chapter titles, the symbol of every "
            "'## The numbers' row, every plate title, and every lexicon term",
            [(e["term"], e["href"]) for e in az]),
    }, "az.html")

    # -- concordance --------------------------------------------------------
    records = []
    for c in live:
        records.append({
            "title": c.title, "href": href(c.url, ""), "kind": c.kind,
            "wing": c.wing,
            "abstract": re.sub(r"<[^>]+>", "", md.render(c.abstract_md))[:400]
                        if c.abstract_md else "",
        })
    for p in plates:
        records.append({"title": "%s -- %s" % (p["id"], p["title"]),
                        "href": href(p["url"], ""), "kind": "plate",
                        "wing": "reader/plates", "abstract": p["caption"][:400]})
    render("search", {
        "title": "Concordance", "records": records,
        "provenance": generated_provenance(
            "every rendered chapter, ledger and plate",
            [(r["title"], r["href"]) for r in records]),
    }, "search.html")

    # -- colophon: the manifest, including what is NOT rendered --------------
    # Everything that reached a page counts as rendered -- not only chapters.
    # The plates and the lexicon ARE pages; marking their files 'no' would tell
    # the reader they were skipped when they were not.
    rendered_rels = {c.rel for c in live}
    rendered_rels |= {p["provenance"]["source_path"] for p in plates}
    rendered_rels |= {s["path"] for p in plates
                      for s in p["provenance"].get("sources", [])}
    rendered_rels |= {f["source_path"] for f in lex["files"]}
    manifest = []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = sorted(d for d in dn if d != ".git"
                       and os.path.realpath(os.path.join(dp, d))
                       != os.path.realpath(DIST))
        for f in sorted(fn):
            abs_p = os.path.join(dp, f)
            rel = os.path.relpath(abs_p, ROOT).replace(os.sep, "/")
            top = rel.split("/")[0]
            data = read_bytes(abs_p)
            manifest.append({
                "path": rel,
                "sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
                "git_state": GIT.file_state(rel),
                "rendered": rel in rendered_rels,
                "reason": None if rel in rendered_rels
                          else NOT_RENDERED_REASON.get(top, "Not corpus content."),
            })

    n_numbers = sum(len(c.numbers) for c in live)
    colophon_body = _colophon_body(manifest, lex, plates, live, n_numbers)
    render("colophon", {
        "title": "Colophon",
        "body_html": colophon_body,
        "stats": [
            {"label": "Chapters rendered", "value": len(live)},
            {"label": "Plates", "value": len(plates)},
            {"label": "'The numbers' rows carried", "value": n_numbers},
            {"label": "Lexicon concepts registered", "value": len(lex["concepts"])},
            {"label": "Lexicon entries authored", "value": len(lex["entries"])},
            {"label": "Files in the repo", "value": len(manifest)},
            {"label": "Files rendered", "value": sum(1 for m in manifest
                                                     if m["rendered"])},
            {"label": "Corpus commit", "value": GIT.short},
            {"label": "Working tree", "value": "dirty" if GIT.dirty else "clean"},
            {"label": "Built (UTC)", "value": BUILD_UTC},
            {"label": "Build notes", "value": len(BUILD_NOTES)},
        ],
        "fences": [
            "READ-ONLY: this generator has one write door, and it refuses any "
            "path outside reader/dist/. It opens repo files 'rb' only. There is "
            "no database, no server, no form, no API and no edit path. "
            "Falsifier: run reader/test_reader.py::test_readonly_invariant, or "
            "diff the repo across a build.",
            "ASCII-ONLY: every page is encoded with xmlcharrefreplace and every "
            "byte is checked before it is written. Falsifier: any emitted byte "
            ">= 0x80.",
            "PROVENANCE OR NO PAGE: every page carries source path + sha256 + "
            "commit + built UTC, and the generator raises rather than "
            "half-stamp. Falsifier: a page missing any of the four.",
            "NO EXTERNAL NETWORK REFERENCES: emitted pages are scanned for "
            "remote asset references and the build fails on a hit. Falsifier: "
            "load any page with the network off; anything that fails to render "
            "refutes this.",
            "THE COMMIT IS CONTEXT, THE SHA256 IS THE RECEIPT: a repo commit "
            "does not mean a file's bytes are in it. Untracked and modified "
            "files say so on their own page.",
            "A NATURA CITATION IS NEVER A UNI GATE. The NATURA classes describe "
            "nature; the UNI 4-value fence describes UNI's own build status. "
            "'hypothesized' is a member of both vocabularies and means "
            "different things in each; they share no CSS class.",
        ],
        "provenance": generated_provenance(
            "a walk of every file in the repository",
            [(m["path"], m["sha256"]) for m in manifest]),
    }, "colophon.html")

    # -- front page ---------------------------------------------------------
    wings = []
    for top, label in CHAPTER_DIRS:
        by_wing = {}
        for c in chapters:
            if c.section != label:
                continue
            by_wing.setdefault(c.wing, []).append(c)
        for wing_name in sorted(by_wing):
            wings.append({
                "name": wing_name, "title": wing_name,
                "blurb": label,
                "chapters": [
                    {"id": c.id, "title": c.title, "href": href(c.url, ""),
                     "abstract": re.sub(r"<[^>]+>", "",
                                        md.render(c.abstract_md))[:280]
                                 if c.abstract_md else ""}
                    for c in by_wing[wing_name]],
            })
    render("index", {
        "title": "The UNI Encyclopedia & Cookbook",
        "wings": wings,
        "intro_html": _index_intro(live, plates, lex, n_numbers),
        "provenance": generated_provenance(
            "every chapter, ledger and plate in the repository",
            sorted(c.rel for c in live)),
    }, "index.html")

    # -- theme.css (owned by another agent; copied byte-for-byte) ------------
    css_src = os.path.join(READER, "theme.css")
    if os.path.exists(css_src):
        css = read_text(css_src)
        fence_scan(css, "theme.css", css=True)
        _write_bytes(os.path.join(DIST, "theme.css"), to_ascii(css))
    else:
        note("theme-missing",
             "reader/theme.css is not present, so pages render unstyled. The "
             "text is readable without it; the stylesheet is not load-bearing "
             "for the words.")
        _say("  WARNING: reader/theme.css is missing; pages will be unstyled.")

    # -- client runtime + PWA + scrivener + search index + precache ----------
    # Every one of these goes through _write_bytes() (the ONE write door). No
    # emission steps outside DIST or without the ASCII check.

    # Client runtime for the e-reader shell.
    if os.path.exists(os.path.join(READER, "app.js")):
        copy_reader_asset("app.js", "app.js")
    else:
        note("app-js-missing", "reader/app.js is not present; the reader shell "
                               "carries no client runtime.")

    # PWA manifest.
    if os.path.exists(os.path.join(READER, "manifest.webmanifest")):
        copy_reader_asset("manifest.webmanifest", "manifest.webmanifest")
    else:
        note("manifest-missing", "reader/manifest.webmanifest is not present.")

    # Service worker. The literal token __CACHE_VERSION__ is replaced with
    # this build's short commit sha so the cache name changes on every build.
    if os.path.exists(os.path.join(READER, "sw.js")):
        copy_reader_asset(
            "sw.js", "sw.js",
            substitutions={"__CACHE_VERSION__": GIT.short})
    else:
        note("sw-js-missing", "reader/sw.js is not present.")

    # Scrivener: the HONEST-store note-taker. Client-only (IndexedDB); no
    # server endpoint. Its README travels with the code because scrivener/
    # is a distributable subtree in its own right.
    scriv_dir = os.path.join(READER, "scrivener")
    if os.path.isdir(scriv_dir):
        if os.path.exists(os.path.join(scriv_dir, "app.js")):
            copy_reader_asset("scrivener/app.js", "scrivener/app.js")
        if os.path.exists(os.path.join(scriv_dir, "style.css")):
            copy_reader_asset("scrivener/style.css", "scrivener/style.css")
        if os.path.exists(os.path.join(scriv_dir, "README.md")):
            copy_reader_asset("scrivener/README.md", "scrivener/README.md")
        # Small shell page that inlines style.css and scrivener/app.js and
        # mounts the list view. Inlined rather than referenced because the
        # existing fence forbids any <script src=> (see fence_scan()); the
        # Scrivener's whole surface is same-origin so this changes nothing
        # about what the browser loads, only where the bytes live.
        scriv_srcs = []
        for f in ("app.js", "style.css", "README.md"):
            fp = os.path.join(scriv_dir, f)
            if os.path.exists(fp):
                scriv_srcs.append({
                    "path": "reader/scrivener/" + f,
                    "sha256": hashlib.sha256(read_bytes(fp)).hexdigest(),
                })
        scriv_prov = generated_provenance(
            "reader/scrivener/{app.js,style.css,README.md} inlined into a "
            "shell page that mounts the list view",
            scriv_srcs)
        scriv_prov["sources"] = scriv_srcs
        # The shell is HTML like any other page and must clear the same
        # external-refs fence. It used to be emitted around the fence -- if a
        # future edit introduces a remote <script src> or an on* handler, that
        # is a real defect and must be surfaced here, not silently shipped.
        scriv_html = _scrivener_shell_html(scriv_prov)
        fence_scan(scriv_html, "scrivener/index.html")
        emit("scrivener/index.html", scriv_html)
    else:
        note("scrivener-missing",
             "reader/scrivener/ is not present; no note-taker is emitted.")

    # Search index: what the offline search overlay in app.js loads.
    search_rows = build_search_index(chapters, plates)
    emit_asset("search-index.json",
               json.dumps(search_rows, sort_keys=True).encode("ascii"))

    # Build-time provenance stub. app.js reads /_provenance.json to render the
    # current-limb line ("limb: X - commit Y") in the bottom chrome, and
    # sw.js network-firsts this URL so a stale entry never wins over a fresh
    # per-limb one. On the fleet the operator's deploy script REWRITES this
    # file with the real per-limb values (limb hostname, deploy UTC, etc.).
    # Emitting a build-time fallback here means:
    #   - a local `python -m http.server -d reader/dist` shows something
    #     sensible ("limb: build-time - commit XXX") instead of blank;
    #   - the precache-manifest lists a real file (sw.js's isProvenance
    #     branch was pointing at a URL the build never emitted, which meant
    #     the SW install would 404 on it and abort);
    #   - the deploy-script overwrite still wins on the fleet, because it
    #     writes AFTER build.py has run.
    emit_asset("_provenance.json",
               json.dumps({
                   "limb": "build-time",
                   "commit": GIT.commit or "NOT-AVAILABLE",
                   "commit_short": GIT.short,
                   "build_utc": BUILD_UTC,
                   "generator": GENERATOR,
                   "note": ("Build-time fallback provenance. On deployed limbs "
                            "the operator's deploy script OVERWRITES this "
                            "with per-limb provenance (hostname, deploy UTC). "
                            "This file makes the offline reader show sensible "
                            "provenance when served locally."),
               }, sort_keys=True).encode("ascii"))

    # Precache manifest: LAST, so it can list every other emission but not
    # itself. sw.js expects {"version", "files":[{path,size,sha256}]} at
    # install time; the task also specifies {url,size,sha256}. The entries
    # carry BOTH `path` and `url` -- the same string -- so both readers work
    # against one file.
    files = []
    for dp, dn, fn in os.walk(DIST):
        dn[:] = sorted(dn)
        for f in sorted(fn):
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, DIST).replace(os.sep, "/")
            if rel == "precache-manifest.json":
                continue
            data = read_bytes(p)
            files.append({
                "path": rel, "url": rel,
                "size": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            })
    emit_asset("precache-manifest.json",
               json.dumps({"version": GIT.short, "files": files},
                          sort_keys=True).encode("ascii"))

    if not args.quiet:
        _say("")
        _say("  UNI reader built.")
        _say("    pages      : %d" % n_pages)
        _say("    chapters   : %d   plates: %d   numbers rows: %d"
             % (len(live), len(plates), n_numbers))
        _say("    lexicon    : %d concepts registered, %d entries authored"
             % (len(lex["concepts"]), len(lex["entries"])))
        _say("    commit     : %s (%s working tree)"
             % (GIT.short, "dirty" if GIT.dirty else "clean"))
        _say("    built UTC  : %s" % BUILD_UTC)
        _say("    bytes out  : %d across %d files"
             % (sum(n for _p, n in WRITE_LOG), len(WRITE_LOG)))
        _say("    notes      : %d (all on colophon.html)" % len(BUILD_NOTES))
        for nt in BUILD_NOTES[:6]:
            _say("      - [%s] %s" % (nt["kind"], nt["detail"][:100]))
        if len(BUILD_NOTES) > 6:
            _say("      ... %d more on the colophon" % (len(BUILD_NOTES) - 6))
        _say("    elapsed    : %.2fs" % (time.time() - t0))
        _say("")
        _say("  Serve it:  python -m http.server -d reader/dist 8080")
        _say("")
    return 0


def _esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def _scrivener_shell_html(provenance):
    """The scrivener/index.html shell.

    Inlines reader/scrivener/style.css and reader/scrivener/app.js because the
    existing external-refs fence forbids any <script src=> (see fence_scan()).
    Inlining is byte-identical: nothing more is loaded from the network; the
    only difference is that the bytes live inside the HTML instead of beside
    it. The Scrivener writes only to the browser's IndexedDB -- there is no
    server endpoint in v1 and this shell has no form that targets one.

    The </script> escape in the inline JS matters: a literal '</script' inside
    a <script> block ends the block early. app.js does not contain that
    literal today, but the substitution below is preserved defensively so a
    future edit cannot introduce that failure mode silently.

    Carries the same provenance footer every page carries -- source path +
    sha256 + commit + built UTC -- because "provenance or no page" is the
    invariant and it does not care that this page is a code shell rather
    than a corpus render.
    """
    style_path = os.path.join(READER, "scrivener", "style.css")
    js_path = os.path.join(READER, "scrivener", "app.js")
    css = read_text(style_path) if os.path.exists(style_path) else ""
    js = read_text(js_path) if os.path.exists(js_path) else ""
    js_safe = js.replace("</script", "<\\/script")

    sha = str(provenance.get("sha256") or "").strip()
    sha_html = ('<code class="prov__sha">%s</code>' % _esc(sha)) if sha else (
        '<span class="prov__absent" title="No single source file for a '
        'generated shell.">ABSENT (generated shell)</span>')
    sources_html = ""
    src_list = provenance.get("sources") or []
    if src_list:
        items = []
        for s in src_list:
            items.append('<li><code>%s</code> <span class="prov__sha2">%s</span></li>'
                         % (_esc(s.get("path")), _esc(s.get("sha256") or "")))
        sources_html = (
            '<details class="prov__more"><summary>Additional sources</summary>'
            '<ul>%s</ul></details>' % "".join(items))

    prov_html = (
        '<footer class="prov" role="contentinfo">'
        '<h2 class="prov__h">Provenance</h2>'
        '<dl class="prov__dl">'
        '<dt>Source</dt><dd><code class="prov__path">%s</code></dd>'
        '<dt>sha256</dt><dd>%s</dd>'
        '<dt>Corpus commit</dt><dd><code class="prov__commit">%s</code></dd>'
        '<dt>Built (UTC)</dt><dd><time class="prov__utc">%s</time></dd>'
        '</dl>%s</footer>'
        % (_esc(provenance.get("source_path")),
           sha_html,
           _esc(provenance.get("commit")),
           _esc(provenance.get("built_utc")),
           sources_html))

    return (
        "<!doctype html>\n"
        '<html lang="en"><head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>Scrivener -- UNI Encyclopedia and Cookbook</title>\n"
        '<link rel="stylesheet" href="../theme.css">\n'
        '<link rel="manifest" href="../manifest.webmanifest">\n'
        "<style>%s</style>\n"
        "</head>\n"
        '<body class="scrivener-page">\n'
        '<main id="main">\n'
        '<h1>Scrivener -- HONEST-store notes</h1>\n'
        '<p>Notes are held in this browser\'s IndexedDB (database '
        '<code>cookbook.scrivener</code>). Sovereign from the TRUE-store '
        'cookbook. Append-only; corrections happen by superseding, and the '
        'old note stays on record. No server endpoint; nothing is uploaded.</p>\n'
        '<div data-role="scrivener-list"></div>\n'
        "</main>\n"
        "%s\n"
        "<script>%s</script>\n"
        "</body></html>\n"
        % (css, prov_html, js_safe))


def _index_intro(live, plates, lex, n_numbers):
    """The front page's own statement of what this is. Facts, counted here."""
    return (
        "<p>This is a reader for the repository it is built from. It renders "
        "%d chapters, %d plates and %d rows of '<em>The numbers</em>' tables, "
        "each carrying value, units, scope, evidence class, source and "
        "falsifier. Every page states the file it came from, that file's "
        "sha256, the corpus commit, and the UTC it was built.</p>"
        "<p>The reader only reads. It has no database, no server, no form and "
        "no edit path, and it fetches nothing from the network.</p>"
        "<p><strong>Two vocabularies live here and are never merged.</strong> "
        "The <em>NATURA</em> classes describe nature's observed regularities, "
        "measured by other people, in published work. The <em>UNI 4-value "
        "fence</em> describes UNI's own build status. A nature citation is "
        "never a UNI gate: reading Kleiber's law raises no UNI rung.</p>"
        "<p><strong>The five registers are not five translations.</strong> "
        "English is the only register with full chapter prose. The other four "
        "carry the canonical terminology from <code>lexicon/</code> and say so "
        "on their own pages; %d concepts are registered and %d carry an entry "
        "in any register. No back-translation test has been run, and no "
        "lexicographer has reviewed an entry, so every rendering is PENDING.</p>"
        % (len(live), len(plates), n_numbers, len(lex["concepts"]),
           len(lex["entries"])))


def _colophon_body(manifest, lex, plates, live, n_numbers):
    """The colophon: how the reader was made, and what it did NOT render."""
    parts = [
        "<h2>How this reader is made</h2>",
        "<p>One command: <code>python reader/build.py</code>. It walks this "
        "repository, renders each file's own bytes, and writes static HTML into "
        "<code>reader/dist/</code>. Python 3 standard library only: no pip, no "
        "npm, no CDN, no webfont, no analytics, no vendored dependency. Serve "
        "it with <code>python -m http.server -d reader/dist 8080</code>, or "
        "open the files directly.</p>",
        "<h2>What is not rendered, and why</h2>",
        "<p>The reader renders the encyclopedia, the cookbook, the two "
        "sovereign ledgers, the lexicon and the plates. Everything else in the "
        "repository is listed below with its sha256 and the reason it is not a "
        "page. Nothing is omitted silently: a silent omission would break the "
        "claim that this is the real, as-is repository.</p>",
    ]

    unrendered = [m for m in manifest if not m["rendered"]]
    parts.append('<div class="tablewrap"><table><thead><tr><th>Path</th>'
                 "<th>Bytes</th><th>git state</th><th>sha256</th>"
                 "<th>Why it is not a page</th></tr></thead><tbody>")
    for m in unrendered:
        parts.append(
            "<tr><td><code>%s</code></td><td>%d</td><td>%s</td>"
            "<td><code>%s</code></td><td>%s</td></tr>"
            % (_esc(m["path"]), m["bytes"], _esc(m["git_state"]),
               _esc(m["sha256"][:12]), _esc(m["reason"] or "")))
    parts.append("</tbody></table></div>")

    parts.append("<h2>Every file this build read</h2>")
    parts.append("<p>%d files, each with the sha256 of the bytes read at build "
                 "time. This is the falsifier for the whole reader: hash any "
                 "file in the repo and compare.</p>" % len(manifest))
    parts.append('<div class="tablewrap"><table><thead><tr><th>Path</th>'
                 "<th>Bytes</th><th>git state</th><th>sha256</th>"
                 "<th>Rendered</th></tr></thead><tbody>")
    for m in manifest:
        parts.append(
            "<tr><td><code>%s</code></td><td>%d</td><td>%s</td>"
            "<td><code>%s</code></td><td>%s</td></tr>"
            % (_esc(m["path"]), m["bytes"], _esc(m["git_state"]),
               _esc(m["sha256"][:12]), "yes" if m["rendered"] else "no"))
    parts.append("</tbody></table></div>")

    if BUILD_NOTES:
        parts.append("<h2>What this build observed</h2>")
        parts.append("<p>%d observation(s) the generator made about the corpus "
                     "while reading it. These are reported rather than "
                     "swallowed; each is a fact about the repo, not a failure "
                     "of the build.</p>" % len(BUILD_NOTES))
        parts.append("<ul>")
        for n in BUILD_NOTES:
            parts.append("<li><strong>%s</strong> &#183; %s</li>"
                         % (_esc(n["kind"]), _esc(n["detail"])))
        parts.append("</ul>")
    else:
        parts.append("<h2>What this build observed</h2><p>No observations were "
                     "recorded: every file the generator read matched the "
                     "shapes it expects.</p>")
    return "".join(parts)


if __name__ == "__main__":
    sys.exit(main())
