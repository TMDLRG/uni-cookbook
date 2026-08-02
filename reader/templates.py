"""reader/templates.py - page shells for the UNI Encyclopedia-Cookbook reader.

Python 3 STDLIB ONLY. No third-party imports, ever. Exposes exactly one entry point:

    render_page(kind, ctx) -> str        kind in KINDS

and the small set of helpers build.py may reasonably want (esc, to_ascii, badge
renderers). Everything else is private.

--------------------------------------------------------------------------------
WHAT THIS MODULE GUARANTEES (each is structural, not a promise)
--------------------------------------------------------------------------------
1. PURE ASCII OUT. Every string returned by render_page() passes through to_ascii()
   at ONE choke point (the final return). Non-ASCII is emitted as numeric character
   references. Nothing can bypass it, because there is exactly one return path.
   REASON, and it is not cosmetic: the fleet's MCP os_file_write silently corrupts
   multi-byte UTF-8 (drops bytes, returns ok=true with a wrong sha). ASCII-only
   bytes make that bug unable to fire.

2. NO NETWORK. This module emits no http(s) reference of any kind: no CDN, no
   webfont, no analytics, no remote script src. Its only asset reference is the
   relative href to theme.css. System font stack only.
   NOTE FOR test_no_external_refs: an INLINED plate SVG carries
   xmlns="http://www.w3.org/2000/svg". That is an XML namespace IDENTIFIER and is
   never fetched -- reader/plates/PL-01.json:design_fence says so explicitly. A
   test that greps for the bare substring "http" will fire on it. Test for fetching
   constructs instead: src=, href=, url(, @import pointing at http(s).

3. READ-ONLY. This module opens no file, for reading or writing. It has no I/O at
   all. It takes a ctx dict and returns a string. build.py owns all filesystem
   access and is the only writer, into reader/dist/ only.

4. THE TWO VOCABULARIES CANNOT BE MERGED. See "BADGE SOVEREIGNTY" below.

--------------------------------------------------------------------------------
BADGE SOVEREIGNTY (the cardinal rule, made structural)
--------------------------------------------------------------------------------
The corpus carries two sovereign vocabularies that must never be confused:

  * The UNI 4-value fence  - proven / designed / hypothesized / not-yet-built.
    UNI's OWN build status. Governed by encyclopedia/CLAIM-LEDGER.md.
  * The NATURA class       - twelve classes in three groups. NATURE's observed
    regularities. Governed by encyclopedia/wing-NATURA/NA-00-how-to-read-this-wing.md
    (amendment 2026-07-15-A).

A NATURE CITATION IS NEVER A UNI GATE. Reading Kleiber's law raises no UNI rung.

The token `hypothesized` EXISTS IN BOTH VOCABULARIES. NA-00 states the governing
rule for the `NEGATIVE` collision: "one token may not serve both vocabularies".
Therefore badge distinctness may NOT rest on the token text, and may NOT rest on
colour alone (that dies in print and for colourblind readers). It rests on three
independent, redundant signals:

    signal          UNI fence                    NATURA class
    -----------     -------------------------    ---------------------------
    CSS class tree  .fence / .fence--*           .natura / .natura--*
    shape           square, double-ruled box     rounded, single hairline tag
    sigil (text)    "UNI"  + middot              "NATURA" + middot

There is deliberately NO shared base class between them. `.fence` and `.natura`
share no ancestor, no mixin, and no class name -- that is what test_badges_distinct
asserts, and it is why a common `.badge` class is absent from this file and from
theme.css. Do not add one.

HONEST signals are a THIRD thing and get a third treatment (`.honest`). An HONEST
signal is lived experience; it is NEVER calibrated and carries no NATURA class at
all (NA-00 s.v. CN11-59). It is not a NATURA class with a different colour. It is
not on the same axis.

--------------------------------------------------------------------------------
THE ctx CONTRACT (build.py: this is the interface; CONTRACT below is machine-readable)
--------------------------------------------------------------------------------
COMMON to every kind:

  provenance   REQUIRED dict. A page that cannot state its provenance DOES NOT
               RENDER -- render_page raises ProvenanceError. Keys:
                 source_path  str  REQUIRED  repo-relative path this page renders
                 sha256       str  REQUIRED  sha256 of that file's bytes
                                             (may be omitted ONLY when pending=True)
                 commit       str  REQUIRED  git commit SHA of the corpus
                 built_utc    str  REQUIRED  ISO-8601 UTC build stamp
                 sources      list OPTIONAL  [{path, sha256}, ...] extra sources
               For a generated page (index/az/search/colophon) that has no single
               source file, pass source_path='reader/build.py' and its own sha256.
               That is honest: the generator IS that page's source.

  title        str  page title (browser title + running head)
  root         str  relative prefix to reader/dist/ root, e.g. '' or '../'.
                    Default ''. Used for theme.css and all internal links.
  register     str  one of REGISTERS ('en','sa','la','hi','es'). Default 'en'.
  registers    list OPTIONAL register descriptors for the switcher:
                    [{code, label, href, pending: bool, counts: {CITED, COINED,
                      'PENDING-CITATION', 'NOT-ATTEMPTED'}}, ...]
  nav          list OPTIONAL [{href, label}] volume navigation
  site         dict OPTIONAL {title, subtitle}
  folio        str|int OPTIONAL folio (page) mark
  running_head str OPTIONAL verso running head (defaults to site title)

PER KIND (all optional unless marked REQUIRED):

  chapter   id, title REQUIRED, wing, abstract_html, body_html, numbers (list of
            row dicts), marginals (list), see_also (list), plates (list), prev,
            next, dropcap (bool, default True), pending (bool), pending_reason
  index     wings: [{name, title, blurb, chapters: [{id,title,href,abstract}]}]
  az        entries: [{term, href, kind, note}]  (rendered A-Z, client-filterable)
  lexicon   entries: [{concept_id, english_term, store, source_definition,
                       sanskrit{}, latin{}, english{}, hindi{}, spanish{}}],
            counts, file_id, status_vocabulary
  ledger    vocabulary REQUIRED: 'uni' | 'natura'  <- structural sovereignty guard,
            raises VocabularyError if absent/unknown. columns, rows (list of dicts
            or list of lists), intro_html, ledger_title
  plate     plate_id REQUIRED, title, caption, svg_markup (INLINE the SVG; do not
            <img> it -- an <img>-embedded SVG cannot see the page's data-theme and
            desyncs from the page on manual toggle), claims, marginal_note,
            not_claimed, source_chapters, design_fence, number (roman plate no.)
  colophon  body_html, stats (list of {label, value}), fences (list of str)
  search    records: [{title, href, kind, wing, abstract}]  (inline JSON + JS filter)

MISSING CONTENT vs MISSING PROVENANCE -- these are different and must not be conflated:
  * A missing CHAPTER (content absent) renders a PENDING page: pass pending=True and
    pending_reason. sha256 may then be omitted (there are no bytes to hash) and is
    rendered honestly as ABSENT. The build does not crash. (test_partial_corpus)
  * Missing PROVENANCE (no commit / no built_utc / no source_path) RAISES. A page
    that cannot say where it came from must not exist. (test_provenance_present)

Unknown ctx keys are ignored. Missing optional keys degrade to an honest PENDING or
are omitted -- never invented, never crashed on.
"""

import json
import re

__all__ = [
    "render_page", "KINDS", "REGISTERS", "CONTRACT",
    "esc", "to_ascii", "natura_badge", "uni_fence_badge",
    "lex_status_badge", "store_badge",
    "TemplateError", "ProvenanceError", "VocabularyError",
]

# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------


class TemplateError(Exception):
    """Base class for template refusals."""


class ProvenanceError(TemplateError):
    """A page that cannot state its provenance does not render."""


class VocabularyError(TemplateError):
    """A ledger must declare which sovereign vocabulary it speaks."""


# ---------------------------------------------------------------------------
# Vocabularies. Cited to the corpus files that govern them; do not edit here
# without editing there. These lists are the ADMITTED tokens -- an unknown token
# still renders (verbatim, flagged), because silently dropping a class would be
# a worse lie than showing one we do not recognise.
# ---------------------------------------------------------------------------

KINDS = ("chapter", "index", "az", "lexicon", "ledger", "plate", "colophon", "search")

REGISTERS = ("sa", "la", "en", "hi", "es")

REGISTER_LABELS = {
    "sa": "Sanskrit",
    "la": "Latin",
    "en": "English",
    "hi": "Hindi",
    "es": "Spanish",
}

# encyclopedia/CLAIM-LEDGER.md
UNI_FENCE = ("proven", "designed", "hypothesized", "not-yet-built")

# encyclopedia/wing-NATURA/NA-00-how-to-read-this-wing.md, amended 2026-07-15-A:
# "twelve classes in three groups (measured / derived / fenced)".
NATURA_GROUPS = {
    "measured": ("OBSERVED-REPLICATED", "OBSERVED-SINGLE", "OBSERVED-CONTESTED"),
    "derived": ("MODELED", "MODELED-CONTESTED", "HYPOTHESIZED"),
    "fenced": ("INADMISSIBLE", "SUPERSEDED", "NOT-MEASURED",
               "NOT-SOURCED", "NOT-CONFIRMED", "NOT-LOCATED"),
}
NATURA_CLASSES = tuple(c for g in NATURA_GROUPS.values() for c in g)

# lexicon/terms/*.json : status_vocabulary
LEX_STATUS = ("CITED", "PENDING-CITATION", "COINED", "NOT-ATTEMPTED")

# The sovereign stores. HONEST is never calibrated (NA-00 s.v. CN11-59).
STORES = ("TRUE", "HONEST", "META")

CONTRACT = {
    "entry_point": "render_page(kind, ctx) -> str",
    "kinds": list(KINDS),
    "registers": list(REGISTERS),
    "required_common": ["provenance.source_path", "provenance.sha256",
                        "provenance.commit", "provenance.built_utc"],
    "required_by_kind": {
        "chapter": ["title"],
        "ledger": ["vocabulary"],   # 'uni' | 'natura'
        "plate": ["plate_id"],
    },
    "sha256_optional_when": "ctx.get('pending') is True",
    "raises": {
        "ProvenanceError": "provenance missing/incomplete",
        "VocabularyError": "ledger without vocabulary in ('uni','natura')",
        "TemplateError": "unknown kind",
    },
    "guarantees": ["pure-ascii-output", "no-network", "no-file-io",
                   "uni-and-natura-badges-share-no-css-class"],
    "stylesheet": "theme.css (relative to ctx['root'])",
    "theme_contract": (
        "data-theme='dark'|'light' on <html>, prefers-color-scheme as the default "
        "signal. This is NOT a free choice: all 10 plate SVGs in reader/plates/ "
        "already implement exactly this pair. Changing it desyncs every plate."
    ),
}

# ---------------------------------------------------------------------------
# Primitives
# ---------------------------------------------------------------------------


def to_ascii(text):
    """Return `text` as pure ASCII, non-ASCII as numeric character references.

    This is the single choke point that makes ASCII-only output structural.
    Markup is preserved: '<', '>', '&' are ASCII and pass through untouched;
    only characters outside ASCII become &#NNNN; references. That makes it safe
    to apply to a whole assembled document, including inlined SVG markup.
    """
    if text is None:
        return ""
    if not isinstance(text, str):
        text = str(text)
    return text.encode("ascii", "xmlcharrefreplace").decode("ascii")


def esc(text):
    """Escape text for HTML body context. A corpus about honesty ships no XSS hole."""
    if text is None:
        return ""
    if not isinstance(text, str):
        text = str(text)
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#39;"))


def _attr(text):
    """Escape for a double-quoted attribute value."""
    return esc(text)


def _slug(text):
    """Token -> css-safe suffix. 'OBSERVED-REPLICATED' -> 'observed-replicated'."""
    s = re.sub(r"[^a-z0-9]+", "-", str(text).strip().lower())
    return s.strip("-") or "unknown"


def _get(ctx, key, default=""):
    v = ctx.get(key, default)
    return default if v is None else v


def _rows_as_dicts(rows, columns):
    """Accept rows as dicts or as positional lists; normalise to dicts."""
    out = []
    for r in rows or []:
        if isinstance(r, dict):
            out.append(r)
        else:
            out.append({columns[i] if i < len(columns) else "col%d" % i: v
                        for i, v in enumerate(r)})
    return out


# ---------------------------------------------------------------------------
# Badges. THE TWO VOCABULARIES SHARE NO CLASS NAME. See BADGE SOVEREIGNTY above.
# ---------------------------------------------------------------------------


def uni_fence_badge(value):
    """UNI 4-value fence badge. Square, double-ruled, sigil 'UNI'.

    UNI's OWN build status. Never nature's.
    """
    if value in (None, ""):
        return ""
    raw = str(value).strip()
    known = raw.lower() in UNI_FENCE
    cls = "fence fence--" + _slug(raw)
    if not known:
        cls += " fence--unregistered"
        title = ("Not one of the four registered UNI fence values "
                 "(proven / designed / hypothesized / not-yet-built). Rendered verbatim.")
    else:
        title = "UNI 4-value fence (encyclopedia/CLAIM-LEDGER.md): UNI's own build status."
    return ('<span class="%s" title="%s"><span class="fence__sigil">UNI</span>'
            '<span class="fence__value">%s</span></span>'
            % (cls, _attr(title), esc(raw)))


_EMPHASIS = re.compile(r"[*_]{1,2}")
_TOKEN_RUN = re.compile(r"^([A-Z][A-Z-]*[A-Z]|[A-Z]+)\s*(.*)$", re.S)


def _parse_natura_cell(raw):
    """Split a real Class cell into [(token, qualifier), ...].

    THIS IS NOT DEFENSIVE PROGRAMMING -- it is what the corpus actually contains.
    Observed across the real '## The numbers' tables (143 distinct cells):
        '**OBSERVED-CONTESTED**'                     emphasis
        'OBSERVED-REPLICATED *(secondary)*'          token + qualifier
        '**OBSERVED-CONTESTED / MODELED**'           COMPOUND -- a registered
                                                     convention (NA-00 amendment
                                                     2026-07-15-A), not an error
        '**INADMISSIBLE** as stated'                 token + trailing prose
        '**NOT-SOURCED in this pass**'               token + qualifier, both emphasised
        'as above'                                   a back-reference; no class at all

    The qualifier is load-bearing honesty ("not primary-sourced in this pass" is
    the whole point of the row) so it is RENDERED, never dropped -- but it is not
    part of the class token and must not be badged as one.
    """
    s = _EMPHASIS.sub("", str(raw)).strip()
    if not s:
        return []
    out = []
    # Compounds separate on '/' or a middot. A row may legitimately carry two
    # classes (NA-00: "CN05-31 -- MODELED (the ladder rung) . OBSERVED-REPLICATED
    # (the overall band)").
    for part in re.split(r"\s*(?:/|·|&#183;)\s*", s):
        part = part.strip()
        if not part:
            continue
        m = _TOKEN_RUN.match(part)
        if m:
            out.append((m.group(1).strip(), m.group(2).strip()))
        else:
            out.append(("", part))   # e.g. 'as above' -- no token; say so
    return out


def _one_natura_badge(token, qualifier):
    group = ""
    for gname, members in NATURA_GROUPS.items():
        if token in members:
            group = gname
            break
    if not token:
        # The cell names no class token (e.g. the corpus's 'as above'). Do NOT badge
        # it as a class, and do NOT assert WHY it has no token -- 'as above' is a
        # back-reference, but arbitrary text is not, and guessing between them would
        # be inventing a reading the cell does not support.
        return ('<span class="natura-ref" title="This cell names no NATURA class. '
                'Rendered verbatim, as written.">%s</span>' % esc(qualifier))
    cls = "natura natura--" + _slug(token)
    if group:
        cls += " natura--group-" + group
        title = ("NATURA class, group %s (encyclopedia/wing-NATURA/"
                 "NA-00-how-to-read-this-wing.md). Nature's observed regularity. "
                 "A nature citation is never a UNI gate." % group)
    else:
        cls += " natura--unregistered"
        title = ("Not one of the twelve registered NATURA classes. Rendered "
                 "verbatim, unrecognised. Falsifier: if this token is legitimate, "
                 "register it in NA-00; if not, the row is miswritten.")
    badge = ('<span class="%s" title="%s"><span class="natura__sigil">NATURA</span>'
             '<span class="natura__value">%s</span></span>'
             % (cls, _attr(title), esc(token)))
    if qualifier:
        badge += '<span class="natura__qual">%s</span>' % esc(qualifier)
    return badge


def natura_badge(value):
    """NATURA class badge. Rounded, hairline, sigil 'NATURA'.

    Nature's observed regularities. NEVER a UNI gate.

    Handles the real shapes of the corpus's Class cells, including COMPOUND cells
    (two classes on one row -- a registered convention) and trailing qualifiers
    (which are rendered, never swallowed). See _parse_natura_cell.
    """
    if value in (None, ""):
        return ""
    parts = _parse_natura_cell(value)
    if not parts:
        return ""
    if len(parts) == 1:
        return _one_natura_badge(*parts[0])
    # A compound row: both classes shown, joined by a mark that says "and also",
    # never collapsed into one.
    return ('<span class="natura-compound" title="A compound row: this value '
            'carries more than one NATURA class. Both are shown; neither is '
            'dropped.">%s</span>'
            % '<span class="natura-compound__amp">+</span>'.join(
                _one_natura_badge(t, q) for t, q in parts))


def lex_status_badge(value):
    """Lexicon per-register admission status. A third axis again: .lex."""
    if value in (None, ""):
        return ""
    raw = str(value).strip()
    token = raw.upper()
    cls = "lex lex--" + _slug(token)
    if token not in LEX_STATUS:
        cls += " lex--unregistered"
    return '<span class="%s">%s</span>' % (cls, esc(raw))


def store_badge(value):
    """Sovereign store: TRUE / HONEST / META. HONEST is never calibrated."""
    if value in (None, ""):
        return ""
    raw = str(value).strip()
    token = raw.upper()
    cls = "store store--" + _slug(token)
    title = {
        "TRUE": "TRUE signal: falsifiable, reproducible, recalibratable.",
        "HONEST": ("HONEST signal: lived experience. NEVER calibrated. Carries no "
                   "NATURA class and no UNI fence. Sovereign and separate."),
        "META": "META: commentary about a signal. Travels separately from the signal.",
    }.get(token, "Unregistered store token, rendered verbatim.")
    if token not in STORES:
        cls += " store--unregistered"
    return '<span class="%s" title="%s">%s</span>' % (cls, _attr(title), esc(raw))


# ---------------------------------------------------------------------------
# Provenance
# ---------------------------------------------------------------------------


def _check_provenance(ctx, kind):
    p = ctx.get("provenance")
    if not isinstance(p, dict):
        raise ProvenanceError(
            "kind=%r: provenance dict is required. A page that cannot state its "
            "provenance does not render." % kind)
    missing = [k for k in ("source_path", "commit", "built_utc")
               if not str(p.get(k) or "").strip()]
    pending = bool(ctx.get("pending"))
    if not str(p.get("sha256") or "").strip() and not pending:
        missing.append("sha256")
    if missing:
        raise ProvenanceError(
            "kind=%r source_path=%r: provenance incomplete, missing %s. %s"
            % (kind, p.get("source_path"), ", ".join(missing),
               "sha256 may be omitted only when ctx['pending'] is True."))
    return p


def _provenance_block(ctx):
    """The footer every page carries: source path + sha256 + commit + build UTC."""
    p = ctx["provenance"]
    pending = bool(ctx.get("pending"))
    sha = str(p.get("sha256") or "").strip()
    if not sha:
        sha_html = ('<span class="prov__absent" title="The source file was not '
                    'present at build time; there are no bytes to hash.">ABSENT '
                    '(file not present at build)</span>')
    else:
        sha_html = '<code class="prov__sha">%s</code>' % esc(sha)

    rows = [
        ("Source", '<code class="prov__path">%s</code>' % esc(p.get("source_path"))),
        ("sha256", sha_html),
        ("Corpus commit", '<code class="prov__commit">%s</code>' % esc(p.get("commit"))),
        ("Built (UTC)", '<time class="prov__utc">%s</time>' % esc(p.get("built_utc"))),
    ]
    extra = ""
    sources = p.get("sources") or []
    if sources:
        items = []
        for s in sources:
            if isinstance(s, dict):
                items.append('<li><code>%s</code> <span class="prov__sha2">%s</span></li>'
                             % (esc(s.get("path")), esc(s.get("sha256") or "")))
            else:
                items.append("<li><code>%s</code></li>" % esc(s))
        extra = ('<details class="prov__more"><summary>Additional sources '
                 '(%d)</summary><ul class="prov__list">%s</ul></details>'
                 % (len(items), "".join(items)))

    body = "".join('<div class="prov__row"><span class="prov__k">%s</span>'
                   '<span class="prov__v">%s</span></div>' % (esc(k), v)
                   for k, v in rows)
    note = ('<p class="prov__note">This page renders the repository file named above, '
            'as it stood at that commit. To check it, open that path in the repo and '
            'compare. The reader never edits the corpus and holds no copy of it.</p>')
    return ('<footer class="prov" id="provenance">'
            '<h2 class="prov__h">Provenance</h2>%s%s%s%s</footer>'
            % (body, extra, note, _pending_footnote(ctx, pending)))


def _pending_footnote(ctx, pending):
    if not pending:
        return ""
    reason = ctx.get("pending_reason") or "Not stated."
    return ('<p class="prov__pending">This page is <strong>PENDING</strong>: %s</p>'
            % esc(reason))


# ---------------------------------------------------------------------------
# Chrome: head, running head, nav, register switcher, footer
# ---------------------------------------------------------------------------

# No-FOUC theme bootstrap. data-theme on <html> is the contract the plate SVGs
# already implement ([data-theme="dark"] .plNN {...}); prefers-color-scheme is the
# default signal when no explicit choice is stored. No network, no dependencies.
_THEME_BOOT = (
    "(function(){try{var t=localStorage.getItem('uni-reader-theme');"
    "if(t==='dark'||t==='light'||t==='sepia'){document.documentElement.setAttribute('data-theme',t);}"
    "var f=localStorage.getItem('uni-reader-font');"
    "if(f==='S'||f==='M'||f==='L'){document.documentElement.setAttribute('data-font-size',f);}"
    "var s=localStorage.getItem('uni-reader-sidebar');"
    "if(s==='collapsed'||s==='hidden'){document.documentElement.setAttribute('data-sidebar',s);}}"
    "catch(e){}})();"
)

_THEME_TOGGLE_JS = (
    "(function(){var b=document.getElementById('themetoggle');if(!b)return;"
    "function cur(){var e=document.documentElement.getAttribute('data-theme');"
    "if(e)return e;return window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)')"
    ".matches?'dark':'light';}"
    "function set(t){document.documentElement.setAttribute('data-theme',t);"
    "try{localStorage.setItem('uni-reader-theme',t);}catch(e){}"
    "b.setAttribute('aria-pressed',String(t==='dark'));}"
    "b.hidden=false;b.setAttribute('aria-pressed',String(cur()==='dark'));"
    "b.addEventListener('click',function(){set(cur()==='dark'?'light':'dark');});})();"
)

_FILTER_JS = (
    "(function(){var i=document.getElementById('filter');if(!i)return;"
    "var box=document.getElementById('filterable');if(!box)return;"
    "var items=box.querySelectorAll('[data-key]');"
    "var count=document.getElementById('filtercount');"
    "var groups=box.querySelectorAll('[data-group]');"
    "i.closest('.filterbar').hidden=false;"
    "function run(){var q=i.value.trim().toLowerCase();var n=0;"
    "for(var k=0;k<items.length;k++){var el=items[k];"
    "var hit=!q||el.getAttribute('data-key').indexOf(q)>-1;"
    "el.hidden=!hit;if(hit)n++;}"
    "for(var g=0;g<groups.length;g++){var grp=groups[g];"
    "var vis=grp.querySelectorAll('[data-key]:not([hidden])').length;grp.hidden=vis===0;}"
    "if(count){count.textContent=q?(n+' of '+items.length+' shown'):(items.length+' entries');}}"
    "i.addEventListener('input',run);run();})();"
)

_SEARCH_JS = (
    "(function(){var d=document.getElementById('searchdata');if(!d)return;"
    "var recs=[];try{recs=JSON.parse(d.textContent);}catch(e){return;}"
    "var i=document.getElementById('q'),out=document.getElementById('results'),"
    "st=document.getElementById('searchstatus');if(!i||!out)return;"
    "var form=document.getElementById('searchform');if(form){form.hidden=false;"
    # Replaces the inline onsubmit="return false;" the form used to carry (removed
    # 2026-07-15-D: the HTML fence exists to forbid on* handlers and was not checking
    # for them). This listener is NOT decoration -- the form has no action, and a form
    # with no action submits to the CURRENT url, so without it pressing Enter in the
    # search field reloads search.html and throws the query away. Behaviour is identical
    # to the attribute's: the submit is cancelled and filtering stays live-on-input.
    "form.addEventListener('submit',function(e){e.preventDefault();});}"
    "function esc(s){var p=document.createElement('p');p.textContent=s==null?'':String(s);"
    "return p.innerHTML;}"
    "function run(){var q=i.value.trim().toLowerCase();out.innerHTML='';"
    "if(!q){if(st){st.textContent=recs.length+' pages in this volume. Type to filter.';}return;}"
    "var hits=[];for(var k=0;k<recs.length;k++){var r=recs[k];"
    "var hay=((r.title||'')+' '+(r.wing||'')+' '+(r.kind||'')+' '+(r.abstract||'')).toLowerCase();"
    "var at=hay.indexOf(q);if(at>-1){hits.push([at,r]);}}"
    "hits.sort(function(a,b){return a[0]-b[0];});"
    "if(st){st.textContent=hits.length+' of '+recs.length+' pages match.';}"
    "var h='';for(var k=0;k<hits.length;k++){var r=hits[k][1];"
    "h+='<li class=\\'result\\'><a href=\\''+esc(r.href)+'\\'>'+esc(r.title)+'</a>'+"
    "(r.wing?' <span class=\\'result__wing\\'>'+esc(r.wing)+'</span>':'')+"
    "(r.abstract?'<p class=\\'result__abstract\\'>'+esc(r.abstract)+'</p>':'')+'</li>';}"
    "out.innerHTML=h;}"
    "i.addEventListener('input',run);run();})();"
)


_SW_REGISTER_JS = (
    # PWA service-worker registration. Capability-guarded, wrapped in try/catch
    # and fail-closed: a browser without serviceWorker (or one whose scope
    # forbids it) simply gets a plain read-only site. `serviceWorker.register`
    # is the unforgeable marker used by test_no_unescaped_html_from_corpus_
    # reached_a_page to allowlist this inline script.
    "(function(){try{if('serviceWorker' in navigator){"
    "var m=document.querySelector('meta[name=\"uni-reader-root\"]');"
    "var r=(m&&m.getAttribute('content'))||'./';"
    "navigator.serviceWorker.register(r+'sw.js',{scope:'./'});}"
    "}catch(e){}})();"
)


def _head(ctx, kind):
    root = _get(ctx, "root", "")
    site = ctx.get("site") or {}
    site_title = site.get("title") or "The UNI Encyclopedia & Cookbook"
    title = _get(ctx, "title") or site_title
    full = title if title == site_title else "%s -- %s" % (title, site_title)
    lang = _get(ctx, "register", "en") or "en"
    if lang not in REGISTERS:
        lang = "en"
    # `uni-reader-root` is the meta tag app.js and sw.js read to compute
    # same-origin asset URLs (search-index.json, precache-manifest.json,
    # _provenance.json, sw.js). Emitting it makes every relative fetch resolve
    # against the DIST root regardless of where the site is served: from
    # /glass/cookbook/ on a fleet limb, or from / on a local `python -m
    # http.server -d reader/dist`. Hardcoding /glass/cookbook/ would break the
    # local case; hardcoding / would break the deployed case. This fixes both.
    return (
        "<!doctype html>\n"
        '<html lang="%s">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="uni-reader-root" content="%s">\n'
        "<title>%s</title>\n"
        '<link rel="stylesheet" href="%stheme.css">\n'
        '<link rel="manifest" href="%smanifest.webmanifest">\n'
        "<script>%s</script>\n"
        "<script>%s</script>\n"
        "</head>\n" % (esc(lang), _attr(root), esc(full), _attr(root),
                       _attr(root), _THEME_BOOT, _SW_REGISTER_JS)
    )


def _running_head(ctx, kind):
    site = ctx.get("site") or {}
    verso = _get(ctx, "running_head") or site.get("title") or "The UNI Encyclopedia & Cookbook"
    recto = _get(ctx, "wing") or _get(ctx, "id") or REGISTER_LABELS.get(
        _get(ctx, "register", "en"), "")
    return ('<header class="rh" role="banner">'
            '<span class="rh__verso">%s</span>'
            '<span class="rh__recto">%s</span>'
            "</header>" % (esc(verso), esc(recto)))


def _nav(ctx):
    items = ctx.get("nav") or []
    if not items:
        return ""
    links = "".join(
        '<li><a href="%s"%s>%s</a></li>'
        % (_attr(i.get("href", "#")),
           ' aria-current="page"' if i.get("current") else "",
           esc(i.get("label", "")))
        for i in items)
    return ('<nav class="vnav" aria-label="Volume">'
            '<ul class="vnav__list">%s</ul>'
            '<button id="themetoggle" class="vnav__theme" type="button" hidden '
            'aria-pressed="false" title="Switch between the light and dark volume">'
            '<span class="vnav__themelabel">Light / Dark</span></button>'
            "</nav>" % links)


def _register_switcher(ctx):
    regs = ctx.get("registers") or []
    if not regs:
        return ""
    cur = _get(ctx, "register", "en")
    out = []
    for r in regs:
        code = r.get("code", "")
        label = r.get("label") or REGISTER_LABELS.get(code, code)
        href = r.get("href", "#")
        is_cur = code == cur
        cls = "reg__item" + (" reg__item--current" if is_cur else "")
        badge = ""
        if r.get("pending"):
            badge = '<span class="reg__pending">PENDING</span>'
        inner = '<span class="reg__label">%s</span>%s' % (esc(label), badge)
        if is_cur:
            out.append('<li class="%s"><span aria-current="true">%s</span></li>'
                       % (cls, inner))
        else:
            out.append('<li class="%s"><a href="%s">%s</a></li>'
                       % (cls, _attr(href), inner))
    return ('<nav class="reg" aria-label="Register">'
            '<span class="reg__legend">Register</span>'
            '<ul class="reg__list">%s</ul></nav>' % "".join(out))


def _counts_line(counts):
    """CITED / COINED / PENDING-CITATION census for a register."""
    if not counts:
        return ""
    parts = []
    for token in LEX_STATUS:
        n = counts.get(token)
        if n:
            parts.append('<span class="census__pair">%s <strong>%d</strong></span>'
                         % (lex_status_badge(token), int(n)))
    if not parts:
        return ""
    return '<p class="census">%s</p>' % "".join(parts)


def _register_fence(ctx):
    """The honest state of a non-English register, stated on the page itself.

    English is the ONLY register with full chapter prose. Saying so, on every
    non-English page, is the deliverable -- not an apology for one.
    """
    reg = _get(ctx, "register", "en")
    if reg == "en" or reg not in REGISTERS:
        return ""
    label = REGISTER_LABELS.get(reg, reg)
    counts = {}
    for r in (ctx.get("registers") or []):
        if r.get("code") == reg:
            counts = r.get("counts") or {}
            break
    return (
        '<aside class="fencebox" role="note">'
        '<h2 class="fencebox__h">This %s register is PENDING</h2>'
        '<p>English is the only register carrying full chapter prose. That is the '
        'honest state of this work, and this page will not pretend otherwise.</p>'
        '<p>What this register carries: the canonical terminology from '
        '<code>lexicon/</code>, the doctrine and the fences, and chapter titles and '
        'abstracts where they have been authored. <strong>What it does not carry: '
        'translated chapter prose.</strong> No chapter has been machine-translated '
        'into %s. Presenting machine output as a register would be fabrication, so '
        'the prose is absent rather than invented.</p>'
        '<p class="fencebox__terms">Terminology admitted in this register:</p>%s'
        '<p class="fencebox__auth">Every term carries its own status and its own '
        'authority. <span class="lex lex--cited">CITED</span> means the named '
        'authority was consulted in that pass and carries the headword in the '
        'claimed sense. <span class="lex lex--coined">COINED</span> means no '
        'attested term carries the concept and a compound is proposed, with its '
        'morphology. <span class="lex lex--pending-citation">PENDING-CITATION</span> '
        'means a rendering is proposed but was not looked up, and is not admitted. '
        'No entry in this work has been reviewed by a lexicographer of this '
        'language.</p>'
        '</aside>' % (esc(label), esc(label), _counts_line(counts))
    )


def _foot(ctx, kind, extra_js=""):
    root = _get(ctx, "root", "")
    js = _THEME_TOGGLE_JS + (extra_js or "")
    # `<script src="{root}app.js" defer>` is same-origin relative -- the
    # relaxed fence in build.py (a REMOTE <script src>, matching the pattern
    # already in place for <link href> and <img src>) permits this. app.js is
    # emitted as its own asset in DIST and precached by the service worker; it
    # is not inlined into every page (which would multiply ~22 KB of runtime
    # by ~150 pages for no cache benefit).
    return ("%s\n<script>%s</script>\n"
            '<script src="%sapp.js" defer></script>\n'
            "</body>\n</html>\n"
            % (_provenance_block(ctx), js, _attr(root)))


def _open_body(ctx, kind):
    return ('<body class="page page--%s" data-kind="%s">\n'
            '<a class="skip" href="#main">Skip to the text</a>\n%s%s%s\n'
            % (_slug(kind), _slug(kind), _running_head(ctx, kind),
               _nav(ctx), _register_switcher(ctx)))


def _folio(ctx):
    f = ctx.get("folio")
    if f in (None, ""):
        return ""
    return '<div class="folio" aria-hidden="true">%s</div>' % esc(f)


# ---------------------------------------------------------------------------
# Shared fragments
# ---------------------------------------------------------------------------


def _marginals(items):
    """Receipts, falsifiers and notes, set in the margin as in a printed volume."""
    if not items:
        return ""
    out = []
    for m in items:
        if isinstance(m, str):
            out.append('<aside class="mn"><p class="mn__body">%s</p></aside>' % esc(m))
            continue
        label = m.get("label") or m.get("kind") or ""
        body = m.get("html") or esc(m.get("text") or "")
        cls = "mn"
        k = _slug(m.get("kind") or "")
        if k:
            cls += " mn--" + k
        head = '<span class="mn__label">%s</span>' % esc(label) if label else ""
        out.append('<aside class="%s">%s<div class="mn__body">%s</div></aside>'
                   % (cls, head, body))
    return '<div class="margin">%s</div>' % "".join(out)


def _numbers_table(rows):
    """The '## The numbers' table: Symbol|Value|Units|Scope|Class|Source|Falsifier.

    The Class column is badged with the NATURA vocabulary. Every number carries
    value + units + scope + class + source + falsifier -- that is the house rule,
    and the table renders all six or says why not.
    """
    if not rows:
        return ""
    body = []
    for r in rows:
        cls_val = r.get("class", r.get("cls", ""))
        body.append(
            "<tr>"
            '<td class="num__sym"><code>%s</code></td>'
            '<td class="num__val">%s</td>'
            '<td class="num__units">%s</td>'
            '<td class="num__scope">%s</td>'
            '<td class="num__class">%s</td>'
            '<td class="num__source">%s</td>'
            '<td class="num__fals">%s</td>'
            "</tr>"
            # units/scope accept a rendered *_html exactly as value/source/
            # falsifier do. They used to be esc()'d as plain text, so a real
            # cell like '**ideal** regular tetrahedron' printed its asterisks
            # at the reader. Lossless but wrong: the corpus wrote emphasis and
            # the page showed punctuation. The plain-text keys still work and
            # are still escaped, so a caller passing raw text is safe.
            % (esc(r.get("symbol", "")),
               r.get("value_html") or esc(r.get("value", "")),
               r.get("units_html") or esc(r.get("units", "")),
               r.get("scope_html") or esc(r.get("scope", "")),
               natura_badge(cls_val),
               r.get("source_html") or esc(r.get("source", "")),
               r.get("falsifier_html") or esc(r.get("falsifier", ""))))
    return (
        '<section class="numbers" aria-labelledby="numbers-h">'
        '<h2 id="numbers-h" class="numbers__h">The numbers</h2>'
        '<p class="numbers__note">Every row carries value, units, scope, class, '
        'source and falsifier. The classes in this table are <strong>NATURA</strong> '
        'classes -- rounded tags, describing nature. They are not the UNI fence, and '
        '<strong>no row here moves a UNI rung</strong>.</p>'
        '<div class="tablewrap"><table class="num">'
        "<thead><tr><th>Symbol</th><th>Value</th><th>Units</th><th>Scope</th>"
        "<th>Class</th><th>Source</th><th>Falsifier</th></tr></thead>"
        "<tbody>%s</tbody></table></div></section>" % "".join(body))


def _see_also(items):
    if not items:
        return ""
    links = "".join(
        '<li><a href="%s">%s</a>%s</li>'
        % (_attr(i.get("href", "#")), esc(i.get("label", "")),
           '<span class="seealso__note">%s</span>' % esc(i["note"]) if i.get("note") else "")
        for i in items if isinstance(i, dict))
    if not links:
        return ""
    return ('<nav class="seealso" aria-labelledby="seealso-h">'
            '<h2 id="seealso-h" class="seealso__h">See also</h2>'
            '<ul class="seealso__list">%s</ul></nav>' % links)


_ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
          "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"]


def _roman(n):
    try:
        n = int(n)
    except (TypeError, ValueError):
        return ""
    return _ROMAN[n] if 0 < n < len(_ROMAN) else str(n)


def _plate_figures(plates):
    """Numbered plate references inside a chapter."""
    if not plates:
        return ""
    out = []
    for p in plates:
        num = _roman(p.get("number")) or esc(p.get("plate_id", ""))
        fig = ""
        if p.get("svg_markup"):
            fig = '<div class="plate__art">%s</div>' % p["svg_markup"]
        elif p.get("href"):
            fig = ('<p class="plate__ref"><a href="%s">View the plate</a></p>'
                   % _attr(p["href"]))
        out.append(
            '<figure class="plate" id="plate-%s">%s'
            '<figcaption class="plate__cap">'
            '<span class="plate__no">Plate %s.</span> '
            '<span class="plate__title">%s</span>'
            '<span class="plate__text">%s</span>'
            "</figcaption></figure>"
            % (_attr(_slug(p.get("plate_id", num))), fig, esc(num),
               esc(p.get("title", "")), esc(p.get("caption", ""))))
    return "".join(out)


def _pending_panel(ctx):
    reason = ctx.get("pending_reason") or "The source file was not present at build time."
    return ('<div class="pendingbox" role="note">'
            '<p class="pendingbox__h">PENDING</p>'
            '<p>This chapter is named in the corpus but its text did not render.</p>'
            '<p class="pendingbox__why">%s</p>'
            '<p class="pendingbox__fals">Falsifier: add the file at the source path '
            'named below and rebuild; this panel is replaced by the chapter. Until '
            'then the reader shows the gap rather than filling it.</p>'
            "</div>" % esc(reason))


def _prevnext(ctx):
    prev, nxt = ctx.get("prev"), ctx.get("next")
    if not prev and not nxt:
        return ""
    p = ('<a class="pn__prev" href="%s"><span class="pn__dir">Previous</span>'
         '<span class="pn__t">%s</span></a>'
         % (_attr(prev.get("href", "#")), esc(prev.get("label", ""))) if prev else "")
    n = ('<a class="pn__next" href="%s"><span class="pn__dir">Next</span>'
         '<span class="pn__t">%s</span></a>'
         % (_attr(nxt.get("href", "#")), esc(nxt.get("label", ""))) if nxt else "")
    return '<nav class="pn" aria-label="Chapter">%s%s</nav>' % (p, n)


# ---------------------------------------------------------------------------
# E-reader shell (chrome + sidebar + right rail + TOC overlay + note capture)
# ---------------------------------------------------------------------------
#
# CONTRACT for Reader-JS (the JS agent):
#   The template emits stable IDs and data-role hooks with the payload
#   already serialised into data-* attributes. The JS reads them, wires up
#   behaviour with addEventListener (no on* handlers in HTML, per the fence),
#   and mounts into the empty containers we provide. The template invents
#   NO behaviour: if the JS never loads, the reader still shows every word.
#
# The Scrivener capture path is READ-INTO-BROWSER-INDEXEDDB only. No POST
# route exists in v1. The template surfaces a button skeleton and an empty
# modal container; the JS owns the storage. See the build's honesty rail:
# a corpus about honesty writes nothing on the server for a captured note.
#
# ctx keys consumed here (all optional; degrade honestly if absent):
#   corpus_tree      list of {name, title, chapters:[{id,title,href}]}
#   position         dict {index, total, label}   e.g. {label:"CN-10 of 23"}
#   limbs            dict {node1, node2, tablet}  sibling URLs
#   provenance_url   str  URL of /_provenance.json  (default: root+"_provenance.json")
#   scriv_anchor     str  anchor id to attach a new note to (default: "top")


def _json_attr(v):
    """Serialise `v` as JSON safe to sit inside a double-quoted HTML attribute.

    The reader's ASCII choke point escapes any residual non-ASCII, and the
    HTML escape here converts the double-quotes and '<' the browser would
    otherwise mis-parse. Reading the attribute back with element.dataset
    (or getAttribute) returns the original JSON, verbatim.
    """
    return _attr(json.dumps(v, ensure_ascii=True))


def _sidebar(ctx, kind):
    """Left rail: the corpus tree. Rendered semantically (an <ol> with links)
    so it works with no JS, and carrying data-corpus-tree so the JS agent has
    the same information as one JSON payload if it wants to redraw."""
    tree = ctx.get("corpus_tree") or []
    current = _get(ctx, "id")
    wings_html = []
    for w in tree:
        wname = w.get("name") or ""
        wtitle = w.get("title") or ""
        chs = []
        for c in w.get("chapters") or []:
            cid = c.get("id") or ""
            is_cur = (cid and cid == current)
            aria = ' aria-current="page"' if is_cur else ""
            cls = "sb__ch" + (" sb__ch--current" if is_cur else "")
            chs.append(
                '<li class="%s"><a href="%s"%s>'
                '<span class="sb__id">%s</span>'
                '<span class="sb__t">%s</span></a></li>'
                % (cls, _attr(c.get("href", "#")), aria,
                   esc(cid), esc(c.get("title", ""))))
        wings_html.append(
            '<li class="sb__wing"><details%s>'
            '<summary class="sb__wingname">'
            '<span class="sb__wingcode">%s</span>'
            '<span class="sb__wingtitle">%s</span></summary>'
            '<ol class="sb__chapters">%s</ol></details></li>'
            % (' open' if any(
                (c.get("id") == current) for c in (w.get("chapters") or [])
               ) else "",
               esc(wname), esc(wtitle), "".join(chs) or ""))
    tree_html = ('<ol class="sb__tree">%s</ol>' % "".join(wings_html)) if wings_html \
                else ('<p class="sb__empty">The corpus tree was not passed to '
                      'this page. The reader still renders every word.</p>')
    return (
        '<aside class="sidebar" id="sidebar" data-role="sidebar" '
        'data-corpus-tree="%s" aria-label="Contents">'
        '<div class="sb__head">'
        '<span class="sb__label">Contents</span>'
        '<button class="sb__collapse" type="button" '
        'data-role="sidebar-collapse" aria-controls="sidebar" '
        'aria-expanded="true" title="Collapse contents">'
        '<span aria-hidden="true">&#8676;</span>'
        '<span class="sr">Collapse contents</span></button></div>'
        '%s</aside>' % (_json_attr(tree), tree_html))


def _topchrome(ctx, kind):
    """Top bar: title, position, prev/next, TOC, font size, theme, search,
    capture-note. The controls carry data-role attributes; the JS wires them."""
    title = esc(_get(ctx, "title") or "")
    pos = ctx.get("position") or {}
    pos_label = pos.get("label")
    if not pos_label and pos.get("total"):
        idx = pos.get("index")
        pos_label = ("%s of %s" % (idx, pos["total"])) if idx else ("of %s" % pos["total"])
    pos_html = ('<span class="tc__pos" data-role="chapter-position">%s</span>'
                % esc(pos_label)) if pos_label else ""
    prev, nxt = ctx.get("prev"), ctx.get("next")
    prev_href = _attr(prev.get("href", "#")) if prev else ""
    next_href = _attr(nxt.get("href", "#")) if nxt else ""
    nav_html = (
        '<nav class="tc__nav" data-role="chapter-nav" '
        'data-prev="%s" data-next="%s" aria-label="Chapter navigation">'
        '%s%s</nav>'
        % (prev_href, next_href,
           ('<a class="tc__prev" href="%s" rel="prev" title="Previous chapter">'
            '<span aria-hidden="true">&#8592;</span>'
            '<span class="sr">Previous chapter</span></a>' % prev_href) if prev else "",
           ('<a class="tc__next" href="%s" rel="next" title="Next chapter">'
            '<span aria-hidden="true">&#8594;</span>'
            '<span class="sr">Next chapter</span></a>' % next_href) if nxt else ""))
    anchor = _attr(ctx.get("scriv_anchor") or (_get(ctx, "id") or "top"))
    fs_val = _attr(ctx.get("font_size") or "M")
    th_val = _attr(ctx.get("theme") or "light")
    return (
        '<header class="topchrome" role="toolbar" aria-label="Reader controls">'
        '<div class="tc__lead">'
        '<button class="tc__toc" type="button" data-role="toc-open" '
        'aria-controls="tocoverlay" title="Contents (t)">'
        '<span aria-hidden="true">&#9776;</span>'
        '<span class="sr">Open contents</span></button>'
        '<h1 class="tc__title" title="%s">%s</h1>%s</div>'
        '<div class="tc__mid">%s</div>'
        '<div class="tc__tail">'
        '<div class="tc__group" data-role="font-size" data-value="%s" '
        'role="group" aria-label="Text size">'
        '<button type="button" data-size="S" aria-label="Small text">S</button>'
        '<button type="button" data-size="M" aria-label="Medium text">M</button>'
        '<button type="button" data-size="L" aria-label="Large text">L</button>'
        '</div>'
        '<div class="tc__group" data-role="theme" data-value="%s" '
        'role="group" aria-label="Volume theme">'
        '<button type="button" data-theme-choice="light" title="Light volume" '
        'aria-label="Light volume">Lt</button>'
        '<button type="button" data-theme-choice="sepia" title="Sepia volume" '
        'aria-label="Sepia volume">Sp</button>'
        '<button type="button" data-theme-choice="dark" title="Dark volume" '
        'aria-label="Dark volume">Dk</button>'
        '</div>'
        '<label class="tc__search"><span class="sr">Search this volume</span>'
        '<input type="search" data-role="search" placeholder="Search..." '
        'autocomplete="off"></label>'
        '<button class="tc__note" type="button" data-role="scrivener-open" '
        'data-anchor="%s" title="Capture a note (n)">'
        '<span aria-hidden="true">+</span> Note</button>'
        '</div></header>'
        % (title, title, pos_html, nav_html, fs_val, th_val, anchor)
    )


def _bottomchrome(ctx, kind):
    """Bottom bar: reading progress, current-limb text, sibling-limb flyout."""
    root = _get(ctx, "root", "")
    prov_url = ctx.get("provenance_url") or (root + "_provenance.json")
    limbs = ctx.get("limbs") or {}
    limb_items = []
    for name, url in (limbs.items() if isinstance(limbs, dict) else []):
        limb_items.append(
            '<li><a href="%s" rel="alternate">%s</a></li>'
            % (_attr(url), esc(name)))
    limb_list = ('<ul class="bc__limbs">%s</ul>' % "".join(limb_items)) if limb_items \
                else ('<p class="bc__limbs bc__limbs--empty">No sibling '
                      'limbs were declared for this build.</p>')
    return (
        '<footer class="bottomchrome" role="contentinfo" '
        'aria-label="Reader status">'
        '<div class="bc__progress" data-role="reading-progress" '
        'role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">'
        '<div class="bc__progressbar"></div></div>'
        '<div class="bc__row">'
        '<div class="bc__prov" data-role="provenance" '
        'data-provenance-url="%s">'
        '<span class="bc__provlabel">Limb:</span> '
        '<span class="bc__provvalue" data-role="provenance-value">'
        'PENDING (loads from _provenance.json)</span></div>'
        '<details class="bc__switch" data-role="limb-switcher" '
        'data-limbs="%s">'
        '<summary>Try another limb</summary>%s</details>'
        '</div></footer>'
        % (_attr(prov_url), _json_attr(limbs), limb_list))


def _toc_overlay(ctx, kind):
    """A full-page contents overlay with reading progress per chapter and
    keyboard-shortcut hints. Hidden by default; the JS toggles the [hidden]
    attribute and the [data-open] state. Renders the same tree the sidebar
    carries, so with no JS the overlay markup is still readable in the DOM."""
    tree = ctx.get("corpus_tree") or []
    current = _get(ctx, "id")
    wings_html = []
    for w in tree:
        chs = []
        for c in w.get("chapters") or []:
            cid = c.get("id") or ""
            is_cur = (cid and cid == current)
            cls = "toc__ch" + (" toc__ch--current" if is_cur else "")
            chs.append(
                '<li class="%s"><a href="%s">'
                '<span class="toc__id">%s</span>'
                '<span class="toc__t">%s</span>'
                '<span class="toc__prog" data-chapter-id="%s" '
                'aria-hidden="true"></span></a></li>'
                % (cls, _attr(c.get("href", "#")), esc(cid),
                   esc(c.get("title", "")), _attr(cid)))
        wings_html.append(
            '<section class="toc__wing"><h3 class="toc__wingh">'
            '<span class="toc__wingcode">%s</span>'
            '<span class="toc__wingtitle">%s</span></h3>'
            '<ol class="toc__list">%s</ol></section>'
            % (esc(w.get("name", "")), esc(w.get("title", "")),
               "".join(chs) or '<li class="toc__empty">PENDING</li>'))
    tree_html = ("".join(wings_html) if wings_html
                 else '<p class="toc__empty">The corpus tree was not passed '
                      'to this page.</p>')
    return (
        '<div class="tocoverlay" id="tocoverlay" role="dialog" '
        'aria-modal="true" aria-labelledby="tocoverlay-h" hidden>'
        '<div class="toc__panel">'
        '<header class="toc__head">'
        '<h2 id="tocoverlay-h" class="toc__h">Contents</h2>'
        '<button class="toc__close" type="button" '
        'data-role="toc-close" aria-label="Close contents">'
        '<span aria-hidden="true">&#215;</span></button>'
        '</header>'
        '<div class="toc__body">%s</div>'
        '<footer class="toc__foot"><h3 class="toc__kh">Keyboard</h3>'
        '<dl class="toc__keys">'
        '<dt><kbd>t</kbd></dt><dd>Open / close contents</dd>'
        '<dt><kbd>&#8592;</kbd> <kbd>&#8594;</kbd></dt><dd>Previous / next chapter</dd>'
        '<dt><kbd>/</kbd></dt><dd>Focus search</dd>'
        '<dt><kbd>n</kbd></dt><dd>Capture a note</dd>'
        '<dt><kbd>[</kbd> <kbd>]</kbd></dt><dd>Text smaller / larger</dd>'
        '<dt><kbd>Esc</kbd></dt><dd>Close overlay</dd>'
        '</dl></footer></div></div>'
        % tree_html)


def _scriv_skeleton(ctx, kind):
    """The Scrivener modal skeleton -- an empty container the JS mounts into,
    and a floating capture button. Hidden by default; no server endpoint."""
    anchor = _attr(ctx.get("scriv_anchor") or (_get(ctx, "id") or "top"))
    return (
        '<div class="scriv-modal" id="scriv-modal" data-role="scriv-modal-container" '
        'role="dialog" aria-modal="true" aria-labelledby="scriv-modal-h" hidden>'
        '<div class="scriv__panel">'
        '<header class="scriv__head">'
        '<h2 id="scriv-modal-h" class="scriv__h">Capture a note</h2>'
        '<button class="scriv__close" type="button" data-role="scriv-close" '
        'aria-label="Close">'
        '<span aria-hidden="true">&#215;</span></button></header>'
        '<div class="scriv__body" data-role="scriv-mount">'
        '<p class="scriv__pending">The Scrivener has not loaded. Notes are '
        'held in this browser\'s IndexedDB; nothing is sent to a server.</p>'
        '</div></div></div>'
        '<button class="floating-add" type="button" '
        'data-role="scrivener-open" data-anchor="%s" '
        'aria-controls="scriv-modal" title="Capture a note (n)">'
        '<span aria-hidden="true">+</span>'
        '<span class="floating-add__l">Note</span></button>' % anchor)


def _ereader_wrap(ctx, kind, main_html):
    """Wrap a page's main content in the e-reader shell: sidebar + reader-col
    (top chrome + main + bottom chrome) + TOC overlay + Scrivener skeleton.

    Applied to chapter / index / az / lexicon. The other kinds (plate, ledger,
    colophon, search) render without the shell -- they are either wide artefact
    pages (plate/ledger) or single-purpose destinations (colophon/search)
    where the shell adds furniture without adding reading."""
    return (
        '<div class="ereader" data-kind="%s">'
        '%s'
        '<div class="reader-col">'
        '%s'
        '%s'
        '%s'
        '</div>'
        '%s'
        '%s'
        '</div>'
        % (_slug(kind),
           _sidebar(ctx, kind),
           _topchrome(ctx, kind),
           main_html,
           _bottomchrome(ctx, kind),
           _toc_overlay(ctx, kind),
           _scriv_skeleton(ctx, kind)))


# ---------------------------------------------------------------------------
# Page kinds
# ---------------------------------------------------------------------------


def _render_chapter(ctx):
    pending = bool(ctx.get("pending"))
    cid = _get(ctx, "id")
    title = _get(ctx, "title")
    wing = _get(ctx, "wing")
    dropcap = ctx.get("dropcap", True) and not pending

    head = ""
    if cid:
        head += '<p class="ch__id">%s</p>' % esc(cid)
    head += '<h1 class="ch__title">%s</h1>' % esc(title)
    if wing:
        head += '<p class="ch__wing">%s</p>' % esc(wing)

    abstract = ""
    if ctx.get("abstract_html"):
        abstract = '<div class="abstract">%s</div>' % ctx["abstract_html"]
    elif ctx.get("abstract"):
        abstract = '<div class="abstract"><p>%s</p></div>' % esc(ctx["abstract"])

    if pending:
        body = _pending_panel(ctx)
    else:
        body = ctx.get("body_html") or ""
        if not body.strip():
            body = ('<p class="empty">NOT-MEASURED: the source file rendered no body '
                    'text. This is stated rather than hidden.</p>')

    prose_cls = "prose" + (" prose--dropcap" if dropcap else "")
    article = (
        '<article class="ch">'
        '<div class="ch__head">%s</div>'
        '<div class="rule rule--double" aria-hidden="true"></div>'
        "%s"
        '<div class="%s">%s</div>'
        "%s"
        "</article>"
        % (head, abstract, prose_cls, body, _see_also(ctx.get("see_also")))
    )
    # The numbers table and the plates are siblings of the article, not children of
    # it, so the grid can give them the FULL measure (text column + margin column).
    # Measured, not guessed: the real 7-column numbers table of CN-02 lays out at
    # ~1249px, against a 66ch text column of ~594px. Nested inside the prose it can
    # only scroll sideways -- and the numbers table is the most important artifact
    # in the whole work, since it is where every claim meets its source and its
    # falsifier. A printed encyclopedia sets a wide table across the measure; so
    # does this. .tablewrap still scrolls as the honest fallback on a narrow screen.
    main = ('<main id="main" class="volume">%s%s%s%s%s%s</main>'
            % (_register_fence(ctx), article, _marginals(ctx.get("marginals")),
               _numbers_table(ctx.get("numbers")),
               _plate_figures(ctx.get("plates")),
               _prevnext(ctx)))
    return _ereader_wrap(ctx, "chapter", main)


def _render_index(ctx):
    site = ctx.get("site") or {}
    parts = ['<div class="titlepage">']
    parts.append('<h1 class="tp__title">%s</h1>'
                 % esc(site.get("title") or _get(ctx, "title")))
    if site.get("subtitle"):
        parts.append('<p class="tp__sub">%s</p>' % esc(site["subtitle"]))
    parts.append('<div class="rule rule--double" aria-hidden="true"></div>')
    if ctx.get("intro_html"):
        parts.append('<div class="tp__intro prose">%s</div>' % ctx["intro_html"])
    parts.append("</div>")

    for w in ctx.get("wings") or []:
        chs = []
        for c in w.get("chapters") or []:
            chs.append(
                '<li class="toc__item">'
                '<a class="toc__link" href="%s">'
                '<span class="toc__id">%s</span>'
                '<span class="toc__t">%s</span>'
                '<span class="toc__leader" aria-hidden="true"></span>'
                "</a>%s</li>"
                % (_attr(c.get("href", "#")), esc(c.get("id", "")),
                   esc(c.get("title", "")),
                   '<p class="toc__abstract">%s</p>' % esc(c["abstract"])
                   if c.get("abstract") else ""))
        if not chs:
            chs = ['<li class="toc__item toc__item--empty">PENDING: no chapters '
                   "rendered in this wing.</li>"]
        parts.append(
            '<section class="wing" id="wing-%s">'
            '<h2 class="wing__h"><span class="wing__name">%s</span>'
            '<span class="wing__title">%s</span></h2>'
            "%s"
            '<ol class="toc">%s</ol></section>'
            % (_attr(_slug(w.get("name", ""))), esc(w.get("name", "")),
               esc(w.get("title", "")),
               '<p class="wing__blurb">%s</p>' % esc(w["blurb"]) if w.get("blurb") else "",
               "".join(chs)))
    main = ('<main id="main" class="volume volume--wide">%s%s</main>'
            % (_register_fence(ctx), "".join(parts)))
    return _ereader_wrap(ctx, "index", main)


def _render_az(ctx):
    entries = ctx.get("entries") or []
    buckets = {}
    for e in entries:
        term = str(e.get("term", "")).strip()
        letter = term[:1].upper()
        if not letter.isalpha():
            letter = "#"
        buckets.setdefault(letter, []).append(e)

    letters = sorted(buckets, key=lambda c: (c == "#", c))
    jump = "".join('<li><a href="#az-%s">%s</a></li>' % (_attr(_slug(l) or "sym"), esc(l))
                   for l in letters)
    secs = []
    for l in letters:
        items = sorted(buckets[l], key=lambda e: str(e.get("term", "")).lower())
        lis = []
        for e in items:
            key = " ".join(str(e.get(k, "")) for k in ("term", "kind", "note")).lower()
            lis.append(
                '<li class="az__item" data-key="%s">'
                '<a class="az__link" href="%s"><span class="az__term">%s</span>'
                '<span class="az__leader" aria-hidden="true"></span>'
                '<span class="az__kind">%s</span></a>%s</li>'
                % (_attr(key), _attr(e.get("href", "#")), esc(e.get("term", "")),
                   esc(e.get("kind", "")),
                   '<span class="az__note">%s</span>' % esc(e["note"])
                   if e.get("note") else ""))
        secs.append('<section class="az__group" id="az-%s" data-group="%s">'
                    '<h2 class="az__letter">%s</h2><ul class="az__list">%s</ul></section>'
                    % (_attr(_slug(l) or "sym"), _attr(l), esc(l), "".join(lis)))

    main = (
        '<main id="main" class="volume volume--wide">'
        '<h1 class="pg__title">%s</h1>'
        '<div class="rule rule--double" aria-hidden="true"></div>'
        '<nav class="azjump" aria-label="Letters"><ul class="azjump__list">%s</ul></nav>'
        '<div class="filterbar" hidden>'
        '<label class="filterbar__l" for="filter">Filter the index</label>'
        '<input id="filter" class="filterbar__i" type="search" autocomplete="off" '
        'placeholder="Type to narrow">'
        '<span id="filtercount" class="filterbar__c">%d entries</span></div>'
        '<div id="filterable" class="azcols">%s</div>'
        "</main>"
        % (esc(_get(ctx, "title", "Index")), jump, len(entries), "".join(secs)))
    return _ereader_wrap(ctx, "az", main)


def _lex_register_cell(entry, code):
    """One register's rendering of one term, with its status and its authority."""
    d = entry.get({"sa": "sanskrit", "la": "latin", "en": "english",
                   "hi": "hindi", "es": "spanish"}[code]) or {}
    if not d:
        return '<div class="lx__cell lx__cell--none">%s</div>' % lex_status_badge("NOT-ATTEMPTED")

    parts = ['<div class="lx__cell">']
    parts.append('<p class="lx__reg">%s</p>' % esc(REGISTER_LABELS[code]))

    if code == "en":
        parts.append('<p class="lx__form">%s</p>' % esc(d.get("term", "")))
        if d.get("definition"):
            parts.append('<p class="lx__def">%s</p>' % esc(d["definition"]))
        parts.append("</div>")
        return "".join(parts)

    form = d.get("devanagari") or d.get("form") or d.get("term") or ""
    if form:
        parts.append('<p class="lx__form" lang="%s">%s</p>' % (esc(code), esc(form)))
    if d.get("iast"):
        parts.append('<p class="lx__iast">%s</p>' % esc(d["iast"]))
    if d.get("status"):
        parts.append('<p class="lx__status">%s</p>' % lex_status_badge(d["status"]))
    if d.get("grammar"):
        parts.append('<p class="lx__gram">%s</p>' % esc(d["grammar"]))
    if d.get("literal_gloss"):
        parts.append('<p class="lx__gloss">Literally: %s</p>' % esc(d["literal_gloss"]))
    if d.get("classical_or_post_classical"):
        parts.append('<p class="lx__pc">%s</p>' % esc(d["classical_or_post_classical"]))
    if d.get("headword_as_in_lexicon"):
        parts.append('<p class="lx__hw"><span class="lx__k">Headword</span> %s</p>'
                     % esc(d["headword_as_in_lexicon"]))
    if d.get("morphological_derivation"):
        parts.append('<details class="lx__more"><summary>Morphology</summary>'
                     "<p>%s</p></details>" % esc(d["morphological_derivation"]))
    if d.get("citation"):
        parts.append('<details class="lx__more lx__more--cit"><summary>Authority</summary>'
                     '<p class="lx__cit">%s</p></details>' % esc(d["citation"]))
    parts.append("</div>")
    return "".join(parts)


def _render_lexicon(ctx):
    entries = ctx.get("entries") or []
    cur = _get(ctx, "register", "en")
    order = [cur] + [c for c in REGISTERS if c != cur]

    cards = []
    for e in entries:
        key = " ".join(str(e.get(k, "")) for k in ("concept_id", "english_term")).lower()
        cells = "".join(_lex_register_cell(e, c) for c in order)
        cards.append(
            '<article class="lx" data-key="%s" id="term-%s">'
            '<header class="lx__head">'
            '<h2 class="lx__term">%s</h2>'
            '<p class="lx__id"><code>%s</code> %s</p>'
            "</header>"
            "%s"
            '<div class="lx__grid">%s</div>'
            "</article>"
            % (_attr(key), _attr(_slug(e.get("concept_id", ""))),
               esc(e.get("english_term", "")),
               esc(e.get("concept_id", "")),
               store_badge(e.get("store", "")),
               '<p class="lx__srcdef">%s</p>' % esc(e["source_definition"])
               if e.get("source_definition") else "",
               cells))

    if not cards:
        cards = ['<p class="empty">PENDING: no lexicon entries were passed to this '
                 "page. The lexicon renders what <code>lexicon/</code> holds; it "
                 "invents nothing.</p>"]

    census = ""
    counts = ctx.get("counts") or {}
    cen = counts.get("status_census") or {}
    if cen:
        rows = []
        for code in REGISTERS:
            name = {"sa": "sanskrit", "la": "latin", "en": "english",
                    "hi": "hindi", "es": "spanish"}[code]
            c = cen.get(name)
            if not c:
                continue
            cells = "".join('<td class="cen__n">%s <strong>%d</strong></td>'
                            % (lex_status_badge(t), int(c.get(t, 0)))
                            for t in LEX_STATUS if c.get(t))
            rows.append("<tr><th>%s</th>%s</tr>" % (esc(REGISTER_LABELS[code]), cells))
        if rows:
            census = ('<section class="cen"><h2 class="cen__h">Status census</h2>'
                      '<p class="cen__note">What each register actually carries, '
                      'counted. This is the honest shape of the work.</p>'
                      '<div class="tablewrap"><table class="cen__t"><tbody>%s</tbody>'
                      "</table></div></section>" % "".join(rows))

    main = (
        '<main id="main" class="volume volume--wide">'
        "%s"
        '<h1 class="pg__title">%s</h1>'
        '<div class="rule rule--double" aria-hidden="true"></div>'
        "%s%s"
        '<div class="filterbar" hidden>'
        '<label class="filterbar__l" for="filter">Filter the terms</label>'
        '<input id="filter" class="filterbar__i" type="search" autocomplete="off" '
        'placeholder="Type to narrow">'
        '<span id="filtercount" class="filterbar__c">%d entries</span></div>'
        '<div id="filterable" class="lxlist" data-group="terms">%s</div>'
        "</main>"
        % (_register_fence(ctx), esc(_get(ctx, "title", "Lexicon")),
           '<div class="prose">%s</div>' % ctx["intro_html"] if ctx.get("intro_html") else "",
           census, len(entries), "".join(cards)))
    return _ereader_wrap(ctx, "lexicon", main)


def _render_ledger(ctx):
    """A ledger renders in exactly ONE sovereign vocabulary. It must say which."""
    vocab = str(ctx.get("vocabulary") or "").strip().lower()
    if vocab not in ("uni", "natura"):
        raise VocabularyError(
            "kind='ledger': ctx['vocabulary'] must be 'uni' or 'natura', got %r. "
            "The UNI 4-value fence and the NATURA classes are sovereign and are "
            "never merged; a ledger page that does not declare which vocabulary it "
            "speaks cannot badge its rows without risking the cardinal sin, so it "
            "does not render." % ctx.get("vocabulary"))

    badge = uni_fence_badge if vocab == "uni" else natura_badge
    columns = ctx.get("columns") or []
    rows = _rows_as_dicts(ctx.get("rows"), columns)
    class_cols = {"class", "status", "fence", "verdict"}

    head = "".join("<th>%s</th>" % esc(c) for c in columns)
    body = []
    for r in rows:
        tds = []
        for c in columns:
            v = r.get(c, "")
            if str(c).strip().lower() in class_cols and v:
                tds.append('<td class="lg__class">%s</td>' % badge(v))
            else:
                tds.append('<td class="lg__cell">%s</td>' % esc(v))
        body.append("<tr>%s</tr>" % "".join(tds))

    if vocab == "uni":
        fence_note = (
            '<aside class="vocabbox vocabbox--uni" role="note">'
            '<h2 class="vocabbox__h">This ledger speaks the UNI 4-value fence</h2>'
            '<p>Every badge on this page is <strong>UNI\'s own build status</strong> '
            '-- proven / designed / hypothesized / not-yet-built -- governed by '
            '<code>encyclopedia/CLAIM-LEDGER.md</code>. These rows say nothing about '
            'nature. They are not observations, and they carry no NATURA class.</p>'
            '<p>Observed program position, unsoftened: roughly 2 of 11+ rungs earned. '
            'This is a developmental active-inference simulation -- a toy world, '
            'never a person.</p></aside>')
    else:
        fence_note = (
            '<aside class="vocabbox vocabbox--natura" role="note">'
            '<h2 class="vocabbox__h">This ledger speaks the NATURA classes</h2>'
            '<p>Every badge on this page describes <strong>nature\'s observed '
            'regularities</strong> -- twelve classes in three groups (measured, '
            'derived, fenced), governed by '
            '<code>encyclopedia/wing-NATURA/NA-00-how-to-read-this-wing.md</code>. '
            '<strong>A nature citation is never a UNI gate.</strong> No row on this '
            'page raises a UNI rung, and none of them is a claim about UNI.</p>'
            '<p>The fenced classes carry no usable value; the class says why. They '
            'are first-class rows here, never hidden.</p></aside>')

    # THE TABLE IS OPTIONAL, AND SAYING SO IS THE HONEST PART.
    # build.py carries each ledger WHOLE, as its own document, through
    # intro_html -- prose, every table, every fence -- because the ledger is the
    # authority and reducing it to a row set would drop the fences that govern
    # how its rows may be read. It therefore passes columns=[] and rows=[].
    # This function used to render an empty <table> plus the line "PENDING: no
    # rows were passed to this ledger" DIRECTLY BENEATH the fully-rendered
    # ledger. A page that cries PENDING while showing the content is lying in
    # the modest direction, which is still lying, and it teaches a reader to
    # discount every other PENDING on the site. So:
    #   rows        -> render the row table
    #   no rows, but the document is here -> the document IS the ledger; no table
    #   neither     -> an honest PENDING, because now there is really nothing
    if body:
        table = ('<div class="tablewrap"><table class="lg lg--%s">'
                 "<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>"
                 % (esc(vocab), head, "".join(body)))
    elif ctx.get("intro_html"):
        table = ""
    else:
        table = ('<p class="empty">PENDING: this ledger page received neither '
                 "rows nor a document to render. Falsifier: pass either, and "
                 "this line is replaced by the ledger.</p>")

    return (
        '<main id="main" class="volume volume--wide">'
        "%s"
        '<h1 class="pg__title">%s</h1>'
        '<div class="rule rule--double" aria-hidden="true"></div>'
        "%s%s%s"
        "</main>"
        % (_register_fence(ctx),
           esc(_get(ctx, "ledger_title") or _get(ctx, "title", "Ledger")),
           fence_note,
           '<div class="prose">%s</div>' % ctx["intro_html"] if ctx.get("intro_html") else "",
           table))


def _render_plate(ctx):
    pid = _get(ctx, "plate_id")
    num = _roman(ctx.get("number"))
    art = ""
    if ctx.get("svg_markup"):
        art = '<div class="plate__art">%s</div>' % ctx["svg_markup"]
    else:
        art = ('<p class="empty">PENDING: the plate artwork was not passed to this '
               "page. The caption and the claims below still render.</p>")

    claims = ""
    rows = ctx.get("claims") or []
    if rows:
        body = "".join(
            "<tr>"
            '<td class="pc__ref"><code>%s</code></td>'
            '<td class="pc__sym"><code>%s</code></td>'
            '<td class="pc__val">%s</td>'
            '<td class="pc__units">%s</td>'
            '<td class="pc__scope">%s</td>'
            '<td class="pc__class">%s</td>'
            '<td class="pc__source">%s</td>'
            '<td class="pc__fals">%s</td>'
            "</tr>"
            % (esc(c.get("ref", "")), esc(c.get("symbol", "")), esc(c.get("value", "")),
               esc(c.get("units", "")), esc(c.get("scope", "")),
               natura_badge(c.get("class", "")),
               esc(c.get("source", "")), esc(c.get("falsifier", "")))
            for c in rows if isinstance(c, dict))
        claims = ('<section class="pclaims"><h2 class="pclaims__h">The claims on this '
                  'plate</h2><p class="numbers__note">NATURA classes. Nature, not UNI. '
                  'No row here moves a UNI rung.</p>'
                  '<div class="tablewrap"><table class="num">'
                  "<thead><tr><th>Ref</th><th>Symbol</th><th>Value</th><th>Units</th>"
                  "<th>Scope</th><th>Class</th><th>Source</th><th>Falsifier</th></tr>"
                  "</thead><tbody>%s</tbody></table></div></section>" % body)

    marg = []
    mn = ctx.get("marginal_note")
    if isinstance(mn, dict):
        inner = "".join('<p class="mn__p"><span class="mn__k">%s</span> %s</p>'
                        % (esc(k.replace("_", " ")), esc(v))
                        for k, v in mn.items() if isinstance(v, str) and k != "subject")
        marg.append({"label": mn.get("subject") or "Marginal note", "html": inner,
                     "kind": "note"})
    elif isinstance(mn, str) and mn:
        marg.append({"label": "Marginal note", "text": mn, "kind": "note"})

    nc = ctx.get("not_claimed")
    if nc:
        if isinstance(nc, (list, tuple)):
            inner = "<ul>%s</ul>" % "".join("<li>%s</li>" % esc(x) for x in nc)
        else:
            inner = "<p>%s</p>" % esc(nc)
        marg.append({"label": "Not claimed", "html": inner, "kind": "notclaimed"})

    src = ctx.get("source_chapters")
    if src:
        # build.py passes {href, label} for a chapter the reader renders and
        # {label} for one it does not (per THE ctx CONTRACT). esc()ing the dict
        # itself printed the Python repr -- "{'href': '../chapter/na-04.html',
        # 'label': 'NA-04 ...'}" -- as the visible text of this marginal, on
        # every plate page. A plate's sources are the whole reason to trust the
        # plate, so they render as links where there is one and as a plain path
        # where there is not; a bare string stays supported.
        items = []
        for x in src:
            if isinstance(x, dict):
                label = x.get("label") or x.get("path") or ""
                if x.get("href"):
                    items.append('<li><a href="%s">%s</a></li>'
                                 % (_attr(x["href"]), esc(label)))
                else:
                    items.append("<li><code>%s</code></li>" % esc(label))
            else:
                items.append("<li><code>%s</code></li>" % esc(x))
        marg.append({"label": "Drawn from", "html": "<ul>%s</ul>" % "".join(items),
                     "kind": "source"})

    fence = ctx.get("design_fence")
    if isinstance(fence, dict):
        inner = ('<p>Design-only artwork: %s script elements, %s event handlers, '
                 "%s external references.</p>"
                 % (esc(fence.get("script_elements", "?")),
                    esc(fence.get("event_handlers", "?")),
                    esc(fence.get("external_references", "?"))))
        if fence.get("notes"):
            inner += "<p>%s</p>" % esc(fence["notes"])
        marg.append({"label": "Design fence", "html": inner, "kind": "fence"})

    figure = (
        '<figure class="plate plate--full">%s'
        '<figcaption class="plate__cap">'
        '<span class="plate__no">Plate %s.</span> '
        '<span class="plate__title">%s</span>'
        '<span class="plate__text">%s</span>'
        "</figcaption></figure>"
        % (art, esc(num or pid), esc(_get(ctx, "title")), esc(_get(ctx, "caption"))))

    return ('<main id="main" class="volume volume--wide">'
            "%s"
            '<p class="ch__id">%s</p>'
            '<h1 class="pg__title">%s</h1>'
            '<div class="rule rule--double" aria-hidden="true"></div>'
            "%s%s%s</main>"
            % (_register_fence(ctx), esc(pid), esc(_get(ctx, "title")),
               figure, claims, _marginals(marg)))


def _render_colophon(ctx):
    stats = ctx.get("stats") or []
    stat_html = ""
    if stats:
        stat_html = ('<dl class="colo__stats">%s</dl>'
                     % "".join("<dt>%s</dt><dd>%s</dd>"
                               % (esc(s.get("label", "")), esc(s.get("value", "")))
                               for s in stats if isinstance(s, dict)))
    fences = ctx.get("fences") or []
    fence_html = ""
    if fences:
        fence_html = ('<section class="colo__fences"><h2>The fences this volume '
                      'keeps</h2><ul>%s</ul></section>'
                      % "".join("<li>%s</li>" % esc(f) for f in fences))

    return (
        '<main id="main" class="volume">'
        '<div class="colo">'
        '<h1 class="colo__h">Colophon</h1>'
        '<div class="rule rule--double" aria-hidden="true"></div>'
        "%s"
        '<div class="colo__body prose">%s</div>'
        "%s%s"
        '<p class="colo__mark" aria-hidden="true">&#8258;</p>'
        '<p class="colo__set">Set from the repository itself, in the reader\'s system '
        'serif. No webfont, no network, no third-party code. The reader is a static '
        'generator: it reads the corpus and writes only into its own output '
        'directory. It cannot change what it shows you.</p>'
        "</div></main>"
        % (_register_fence(ctx), ctx.get("body_html") or "", stat_html, fence_html))


def _render_search(ctx):
    records = ctx.get("records") or []
    # ensure_ascii=True keeps the payload ASCII; escaping '<' keeps a record
    # containing '</script>' from breaking out of the data block.
    payload = json.dumps(records, ensure_ascii=True).replace("<", "\\u003c")
    return (
        '<main id="main" class="volume volume--wide">'
        '<h1 class="pg__title">%s</h1>'
        '<div class="rule rule--double" aria-hidden="true"></div>'
        '<form id="searchform" class="srch" hidden>'
        '<label class="srch__l" for="q">Search this volume</label>'
        '<input id="q" class="srch__i" type="search" autocomplete="off" '
        'placeholder="Title, wing, or abstract">'
        "</form>"
        '<noscript><p class="srch__no">Search filters the page with a few lines of '
        'inline script and no network. With scripting off, use the '
        '<a href="%saz.html">A-Z index</a>, which is plain HTML.</p></noscript>'
        '<p id="searchstatus" class="srch__status">%d pages in this volume.</p>'
        '<ul id="results" class="results"></ul>'
        '<script id="searchdata" type="application/json">%s</script>'
        "</main>"
        % (esc(_get(ctx, "title", "Search")), _attr(_get(ctx, "root", "")),
           len(records), payload))


_RENDERERS = {
    "chapter": _render_chapter,
    "index": _render_index,
    "az": _render_az,
    "lexicon": _render_lexicon,
    "ledger": _render_ledger,
    "plate": _render_plate,
    "colophon": _render_colophon,
    "search": _render_search,
}

_EXTRA_JS = {
    "az": _FILTER_JS,
    "lexicon": _FILTER_JS,
    "search": _SEARCH_JS,
}


# ---------------------------------------------------------------------------
# The entry point
# ---------------------------------------------------------------------------


def render_page(kind, ctx):
    """Render one page. Returns pure-ASCII HTML.

    kind : one of KINDS
    ctx  : dict, see THE ctx CONTRACT in the module docstring.

    Raises TemplateError (unknown kind), ProvenanceError (a page that cannot state
    its provenance does not render), or VocabularyError (a ledger that does not
    declare its sovereign vocabulary does not render).
    """
    if kind not in _RENDERERS:
        raise TemplateError("unknown page kind %r; expected one of %s"
                            % (kind, ", ".join(KINDS)))
    if not isinstance(ctx, dict):
        raise TemplateError("ctx must be a dict, got %r" % type(ctx).__name__)

    _check_provenance(ctx, kind)
    main = _RENDERERS[kind](ctx)

    doc = "%s%s%s%s%s" % (
        _head(ctx, kind),
        _open_body(ctx, kind),
        main,
        _folio(ctx),
        _foot(ctx, kind, _EXTRA_JS.get(kind, "")),
    )
    # THE single ASCII choke point. Nothing returns from this module except here.
    return to_ascii(doc)
