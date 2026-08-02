# -*- coding: utf-8 -*-
"""markdown.py -- a dependency-free Markdown subset renderer for the UNI reader.

Python 3 standard library ONLY. No pip, no npm, no vendored third party.

WHY A SUBSET AND NOT A LIBRARY
------------------------------
The reader's brief forbids runtime dependencies, so this renders the Markdown
*this corpus actually uses* -- not CommonMark in general. The subset was chosen
by measuring the corpus (90 .md files, 2026-07-15, repo tip f1be794), not by
guessing. Every inclusion and every omission below is a measurement:

  SUPPORTED (observed in the corpus, counts from the survey)
    ATX headings  # .. ######      97 h1 / 857 h2 / 396 h3
    fenced code blocks   ```       278 fences
    GFM tables (with \\| escapes)   3800 rows, 244 delimiter rows, 86 rows
                                    carrying an escaped pipe, 0 column mismatches
    unordered lists   - * +        1942 (15 nested)
    ordered lists     1. 1)        668 (10 nested)
    blockquotes       >            1356
    thematic breaks   --- *** ___  440
    inline: code spans, strong, emphasis, links, backslash escapes
    paragraphs

  DELIBERATELY NOT SUPPORTED -- each omission is a defect avoided, not a gap
    4-space indented code blocks
        All 172 candidate lines in this corpus are ordered-list continuation
        lines (e.g. cookbook/recipes/L12-creativity-awareness.md:104-108).
        Implementing indented code would render that prose as code. Fenced
        code is the corpus's only code block.
    setext headings (=== / ---)
        Zero in the corpus; all 90 files open with an ATX '# '. Supporting it
        would make the 440 '---' thematic breaks ambiguous.
    $...$ / $$...$$ TeX math
        There is ZERO TeX math in this corpus. All 20 lines containing '$' are
        either shell variables ($env:UNI_MCP, deploy/README.md:93) or money
        ($200 in CLAIM-LEDGER.md:311; $3,450 at :380). A '$' math rule would
        eat the ledger's own numbers. Display math in this corpus is written
        as fenced code with Unicode, and renders as such -- correctly, and
        with no renderer to fetch. See MATH_POLICY below.
    images, reference links, autolinks, strikethrough, HTML passthrough
        Zero in the corpus (see RAW HTML below).

RAW HTML IS ESCAPED, ALWAYS -- THIS IS FIDELITY, NOT ONLY SECURITY
------------------------------------------------------------------
The corpus contains angle-bracket text that is prose, not markup: '<sha>'
(cookbook/MASTER-PLAN.md:821) and '<r̄>' (encyclopedia/NATURE-LEDGER.md:464).
Passing HTML through would *delete these words from the page* -- the browser
would eat them as unknown tags. So escaping is what makes the page faithful to
the repo, and it also means this renderer cannot emit an injected script. There
is no raw-HTML mode and no flag to enable one.

MATH_POLICY
-----------
Math degrades honestly or not at all. This renderer never fetches a math
engine and never guesses at TeX. A fenced block whose info string is 'math',
'tex' or 'latex' is emitted as labelled TeX SOURCE in a <pre class="math-src">
so a reader can see exactly what it says. As measured above, the corpus
currently contains no such block; the path exists so that adding one degrades
to honest source rather than to a silent CDN fetch.

CONTRACT
--------
    render(md, link_resolver=None) -> str          # HTML fragment
    parse(md, link_resolver=None) -> Document      # .html .headings .tables
    render_inline(text, link_resolver=None) -> str # inline HTML fragment
    escape(text) -> str
    slugify(text) -> str
    split_table_row(line) -> list[str]

The returned str is unicode. ASCII-safe emission is the caller's step
(build.py encodes with 'xmlcharrefreplace'), so this module stays a renderer.

link_resolver(href) -> (new_href_or_None, css_class_or_None)
    Return (None, cls) to render the link as inert text (used for repo targets
    the reader does not render, so a dead link is never presented as live).
    Return None to leave the href untouched.
"""

import re

__all__ = [
    "render",
    "parse",
    "render_inline",
    "escape",
    "slugify",
    "split_table_row",
    "Document",
    "SUPPORTED",
    "NOT_SUPPORTED",
]

SUPPORTED = (
    "atx-headings", "fenced-code", "gfm-tables", "unordered-lists",
    "ordered-lists", "blockquotes", "thematic-breaks", "paragraphs",
    "inline-code", "strong", "emphasis", "links", "backslash-escapes",
)

NOT_SUPPORTED = (
    "indented-code-blocks", "setext-headings", "tex-math-dollar",
    "images", "reference-links", "autolinks", "strikethrough",
    "raw-html-passthrough",
)

MATH_INFO_STRINGS = ("math", "tex", "latex")

# Characters CommonMark lets a backslash escape.
_ESCAPABLE = set("\\`*_{}[]()#+-.!|<>~\"'&$:/")

# Link schemes that EXECUTE rather than navigate. A 'javascript:' href is a
# script element wearing an <a>: escaping the body does not stop it, because it
# never passes through escape() as markup at all -- it arrives as a URL.
#
# Measured 2026-07-15 across the 90 .md files: the corpus contains ZERO links
# with any of these schemes. That is exactly why the fence goes in NOW. Without
# it the fence is not "this renderer refuses an execution vector", it is "no
# author has typed one yet" -- which is luck, not a fence, and the reader's own
# brief is that a corpus about honesty must not ship an XSS hole.
#
# A refused scheme renders as INERT TEXT carrying its own words (see _try_link):
# the link's label and target are shown, never silently deleted. Refusing to
# execute a thing is not a licence to disappear it -- that would be the reader
# editing the corpus, which is the one thing it may not do.
_DANGEROUS_SCHEME_RE = re.compile(
    r"^[\s\x00-\x20]*(?:javascript|data|vbscript|file)\s*:", re.I)

_HR_RE = re.compile(r"^ {0,3}(?:(?:\*\s*){3,}|(?:-\s*){3,}|(?:_\s*){3,})$")
_ATX_RE = re.compile(r"^ {0,3}(#{1,6})(?:\s+(.*?))?\s*$")
_FENCE_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})\s*([^`]*)$")
_UL_RE = re.compile(r"^(\s*)([-*+])(\s+)(.*)$")
_OL_RE = re.compile(r"^(\s*)(\d{1,9})([.)])(\s+)(.*)$")
_BQ_RE = re.compile(r"^ {0,3}>\s?(.*)$")
_TABLE_DELIM_RE = re.compile(r"^\s*\|?\s*:?-{1,}:?\s*(\|\s*:?-{1,}:?\s*)*\|?\s*$")


# --------------------------------------------------------------------------
# primitives
# --------------------------------------------------------------------------

def escape(text, quote=True):
    """Escape text for HTML. Applied to every character of every text run.

    There is no path through this module that emits un-escaped source text.
    """
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    if quote:
        text = text.replace('"', "&quot;").replace("'", "&#39;")
    return text


def slugify(text):
    """A stable, ASCII-only anchor id.

    Non-ASCII is dropped rather than transliterated: a transliteration would be
    an unsourced claim about a script, and this file does not make those.
    Falls back to a hash-free 'sec' so an id is never empty.
    """
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"[*_]+", "", text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "sec"


def split_table_row(line):
    """Split a GFM table row into raw cell strings.

    Splits on UNESCAPED pipes only. '\\|' stays in the cell text and is
    unescaped later by the inline pass -- the GFM order. This matters here:
    86 corpus rows carry an escaped pipe, and 77 carry a pipe inside a code
    span, e.g. cookbook/recipes-natura/CN-07-ants.md:173
        `p(mu,eta \\| s,a) = p(mu\\|s,a)*p(eta\\|s,a)`
    Splitting naively on '|' would shred that cell into six.
    """
    line = line.strip()
    cells = []
    buf = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line):
            buf.append(c)
            buf.append(line[i + 1])
            i += 2
            continue
        if c == "|":
            cells.append("".join(buf))
            buf = []
            i += 1
            continue
        buf.append(c)
        i += 1
    cells.append("".join(buf))
    # A leading/trailing pipe produces an empty first/last cell; drop those.
    if cells and not cells[0].strip():
        cells.pop(0)
    if cells and not cells[-1].strip():
        cells.pop()
    return [c.strip() for c in cells]


# --------------------------------------------------------------------------
# inline
# --------------------------------------------------------------------------

def _find_closer(text, start, delim):
    """Find an unescaped closing delimiter run at or after `start`."""
    i = start
    n = len(delim)
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "`":
            j = _skip_code(text, i)
            if j > i:
                i = j
                continue
        if text.startswith(delim, i):
            return i
        i += 1
    return -1


def _skip_code(text, i):
    """Return index just past a code span starting at i, or i if unterminated."""
    m = re.match(r"`+", text[i:])
    if not m:
        return i
    ticks = m.group(0)
    close = text.find(ticks, i + len(ticks))
    while close != -1:
        after = close + len(ticks)
        if after < len(text) and text[after] == "`":
            close = text.find(ticks, after)
            continue
        return after
    return i


def _is_word_char(c):
    return c.isalnum()


def render_inline(text, link_resolver=None):
    """Render inline markdown. Every literal run is escaped."""
    out = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]

        # backslash escape
        if c == "\\" and i + 1 < n and text[i + 1] in _ESCAPABLE:
            out.append(escape(text[i + 1]))
            i += 2
            continue

        # code span -- highest precedence, so * and _ inside code stay literal
        if c == "`":
            m = re.match(r"`+", text[i:])
            ticks = m.group(0)
            end = _skip_code(text, i)
            if end > i:
                inner = text[i + len(ticks):end - len(ticks)]
                # GFM: one leading+trailing space is stripped if both present
                if len(inner) > 1 and inner[0] == " " and inner[-1] == " " \
                        and inner.strip():
                    inner = inner[1:-1]
                # An escaped pipe survives cell-splitting to here; make it a pipe.
                inner = inner.replace("\\|", "|")
                out.append("<code>%s</code>" % escape(inner))
                i = end
                continue
            out.append(escape(c))
            i += 1
            continue

        # link [text](href)
        if c == "[":
            res = _try_link(text, i, link_resolver)
            if res is not None:
                html, i = res
                out.append(html)
                continue
            out.append(escape(c))
            i += 1
            continue

        # strong (** or __), then emphasis (* or _)
        #
        # Every failure path below falls through to the literal-character exit
        # at the bottom, which always advances `i`. An earlier version used a
        # for/else here and could 'break' without advancing on an intra-word
        # '__' -- an infinite loop. Straight-line control flow instead: there
        # is exactly one exit that does not consume a delimiter, and it
        # consumes a character.
        if c in "*_":
            delim = c * 2 if text.startswith(c * 2, i) else c
            strong = len(delim) == 2

            # An intra-word '_' is never emphasis (CommonMark). This is
            # load-bearing here, not pedantry: the corpus is full of
            # identifiers like b_Kleiber, N_sg, f_aff, T_b and b_Savage,unbinned.
            # Treating those as emphasis would silently delete underscores from
            # the science and italicise half a chapter.
            intraword_open = (
                c == "_" and i > 0 and _is_word_char(text[i - 1])
            )
            nxt = text[i + len(delim)] if i + len(delim) < n else ""
            if not intraword_open and nxt not in ("", " "):
                close = _find_closer(text, i + len(delim), delim)
                if close > i + len(delim):
                    closes_intraword = (
                        c == "_" and close + len(delim) < n
                        and _is_word_char(text[close + len(delim)])
                    )
                    inner = text[i + len(delim):close]
                    if not closes_intraword and inner.strip() \
                            and not inner[0].isspace():
                        tag = "strong" if strong else "em"
                        out.append("<%s>%s</%s>"
                                   % (tag, render_inline(inner, link_resolver), tag))
                        i = close + len(delim)
                        continue

        # literal character -- the only non-consuming exit, and it consumes one
        out.append(escape(c))
        i += 1
    return "".join(out)


def _is_dangerous_scheme(href):
    """True if `href` executes rather than navigates.

    Control characters and whitespace are stripped BEFORE the scheme is read,
    because browsers ignore them inside a scheme: 'java\\tscript:alert(1)' and
    'java\\nscript:alert(1)' both execute. Testing the raw string would let a
    tab walk straight through the fence.
    """
    probe = re.sub(r"[\x00-\x20\s]", "", href or "")
    return bool(_DANGEROUS_SCHEME_RE.match(probe))


def _try_link(text, i, link_resolver):
    """Parse [label](href) at i. Returns (html, next_index) or None."""
    depth = 0
    j = i
    while j < len(text):
        if text[j] == "\\":
            j += 2
            continue
        if text[j] == "`":
            k = _skip_code(text, j)
            if k > j:
                j = k
                continue
        if text[j] == "[":
            depth += 1
        elif text[j] == "]":
            depth -= 1
            if depth == 0:
                break
        j += 1
    if j >= len(text) or depth != 0:
        return None
    label = text[i + 1:j]
    if j + 1 >= len(text) or text[j + 1] != "(":
        return None
    k = j + 2
    depth = 1
    while k < len(text):
        if text[k] == "\\":
            k += 2
            continue
        if text[k] == "(":
            depth += 1
        elif text[k] == ")":
            depth -= 1
            if depth == 0:
                break
        k += 1
    if k >= len(text) or depth != 0:
        return None
    href = text[j + 2:k].strip()
    # A title in quotes, if present, is dropped rather than half-rendered.
    m = re.match(r'^(\S+)\s+"[^"]*"$', href)
    if m:
        href = m.group(1)
    inner = render_inline(label, link_resolver)

    cls = None
    if link_resolver is not None:
        resolved = link_resolver(href)
        if resolved is not None:
            href, cls = resolved
    if href is None:
        # A target the reader does not render: shown, never presented as live.
        attrs = ' class="%s"' % escape(cls) if cls else ""
        return ('<span%s>%s</span>' % (attrs, inner), k + 1)

    if _is_dangerous_scheme(href):
        # An execution vector, refused. Rendered as inert text that still
        # carries the label AND the refused target, so the page shows what the
        # source said and why it is not a link. The renderer refuses to execute
        # it; it does not get to delete it.
        return ('<span class="xref-refused" title="This link was not rendered '
                'as a link: its URL scheme executes code rather than '
                'navigating. The target is shown as text.">%s <code '
                'class="xref-refused__target">%s</code></span>'
                % (inner, escape(href)), k + 1)

    attrs = ' class="%s"' % escape(cls) if cls else ""
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:", href) and not href.startswith("#"):
        # Off-site: user-initiated navigation only. It is not an asset ref --
        # nothing here is fetched at page load. rel hardens the hop.
        attrs += ' rel="noopener noreferrer external"'
    return ('<a href="%s"%s>%s</a>' % (escape(href), attrs, inner), k + 1)


# --------------------------------------------------------------------------
# blocks
# --------------------------------------------------------------------------

class Document(object):
    """The rendered result plus what the page furniture needs.

    headings: [{'level': int, 'text': str, 'id': str}]
    tables:   [{'headers': [str], 'rows': [[str]], 'align': [str|None],
                'line': int, 'heading': str|None}]  -- raw cell source, so a
              caller (build.py) can parse '## The numbers' without re-lexing.
    """

    __slots__ = ("html", "headings", "tables", "title")

    def __init__(self, html, headings, tables, title=None):
        self.html = html
        self.headings = headings
        self.tables = tables
        self.title = title


def render(md, link_resolver=None):
    """Render a Markdown document to an HTML fragment."""
    return parse(md, link_resolver).html


def parse(md, link_resolver=None):
    md = md.replace("\r\n", "\n").replace("\r", "\n").replace("\t", "    ")
    lines = md.split("\n")
    out = []
    headings = []
    tables = []
    seen_ids = {}
    title = None
    cur_heading = [None]

    def add_heading(level, raw):
        nonlocal title
        base = slugify(raw)
        if base in seen_ids:
            seen_ids[base] += 1
            hid = "%s-%d" % (base, seen_ids[base])
        else:
            seen_ids[base] = 0
            hid = base
        headings.append({"level": level, "text": raw, "id": hid})
        if level == 1 and title is None:
            title = raw
        cur_heading[0] = raw
        return hid

    i = 0
    n = len(lines)
    # Guaranteed progress. Every branch below MUST advance `i`, or the build
    # hangs instead of failing. This is checked on every iteration because the
    # bug already bit once: a '|' line with no delimiter row after it was
    # claimed by _is_block_start(), then refused by the paragraph fallback,
    # and spun forever emitting nothing. A hang is worse than a crash -- it
    # leaves no receipt. The invariant is now structural, not a habit.
    last_i = -1
    while i < n:
        if i == last_i:  # pragma: no cover -- invariant, not a branch
            raise AssertionError(
                "markdown.parse made no progress at line %d: %r. This is a "
                "renderer defect, not a corpus defect." % (i + 1, lines[i])
            )
        last_i = i
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        # fenced code
        m = _FENCE_RE.match(line)
        if m:
            indent, fence, info = m.group(1), m.group(2), (m.group(3) or "").strip()
            char = fence[0]
            need = len(fence)
            i += 1
            buf = []
            while i < n:
                cl = lines[i]
                cm = re.match(r"^ {0,3}(%s{%d,})\s*$" % (re.escape(char), need), cl)
                if cm:
                    i += 1
                    break
                if indent and cl.startswith(indent):
                    cl = cl[len(indent):]
                buf.append(cl)
                i += 1
            code = "\n".join(buf)
            info_l = info.lower().split()[0] if info else ""
            if info_l in MATH_INFO_STRINGS:
                # Honest degradation: labelled TeX source. Never fetched, never
                # guessed at. See MATH_POLICY in the module docstring.
                out.append(
                    '<figure class="math-block">'
                    '<pre class="math-src"><code>%s</code></pre>'
                    '<figcaption>TeX source, shown as source. '
                    'No math renderer is vendored; this is not typeset.'
                    '</figcaption></figure>' % escape(code)
                )
            else:
                cls = ' class="lang-%s"' % escape(info_l) if info_l else ""
                out.append("<pre><code%s>%s</code></pre>" % (cls, escape(code)))
            continue

        # ATX heading
        m = _ATX_RE.match(line)
        if m:
            level = len(m.group(1))
            raw = (m.group(2) or "").strip()
            raw = re.sub(r"\s+#+\s*$", "", raw)
            hid = add_heading(level, raw)
            out.append('<h%d id="%s">%s</h%d>'
                       % (level, hid, render_inline(raw, link_resolver), level))
            i += 1
            continue

        # thematic break (checked after ATX; before lists, since '- - -' is an hr)
        if _HR_RE.match(line):
            out.append("<hr />")
            i += 1
            continue

        # table: a pipe row followed by a delimiter row
        if line.lstrip().startswith("|") and i + 1 < n \
                and _TABLE_DELIM_RE.match(lines[i + 1]) and "|" in lines[i + 1]:
            html, tbl, i = _parse_table(lines, i, link_resolver)
            tbl["heading"] = cur_heading[0]
            tables.append(tbl)
            out.append(html)
            continue

        # blockquote
        if _BQ_RE.match(line):
            buf = []
            while i < n and (_BQ_RE.match(lines[i])
                             or (lines[i].strip() and not _is_block_start(lines[i])
                                 and buf)):
                bm = _BQ_RE.match(lines[i])
                buf.append(bm.group(1) if bm else lines[i])
                i += 1
            inner = parse("\n".join(buf), link_resolver)
            out.append("<blockquote>%s</blockquote>" % inner.html)
            continue

        # lists
        if _UL_RE.match(line) or _OL_RE.match(line):
            html, i = _parse_list(lines, i, link_resolver)
            out.append(html)
            continue

        # paragraph -- the fallback, and therefore the thing that must always
        # consume. The first line is taken unconditionally: if it reached here
        # it is a line no other handler claimed (e.g. a stray '|' row, a table
        # continuation with no delimiter), and the honest rendering of an
        # unclaimed line is its own text, not a hang and not silence.
        buf = [lines[i].strip()]
        i += 1
        while i < n and lines[i].strip() and not _is_block_start(lines[i]):
            buf.append(lines[i].strip())
            i += 1
        out.append("<p>%s</p>" % render_inline(" ".join(buf), link_resolver))

    return Document("\n".join(out), headings, tables, title)


def _is_block_start(line):
    if _ATX_RE.match(line) or _HR_RE.match(line) or _BQ_RE.match(line):
        return True
    if _FENCE_RE.match(line):
        return True
    if _UL_RE.match(line) or _OL_RE.match(line):
        return True
    if line.lstrip().startswith("|"):
        return True
    return False


def _parse_table(lines, i, link_resolver):
    header = split_table_row(lines[i])
    delim = split_table_row(lines[i + 1])
    align = []
    for d in delim:
        d = d.strip()
        if d.startswith(":") and d.endswith(":"):
            align.append("center")
        elif d.endswith(":"):
            align.append("right")
        elif d.startswith(":"):
            align.append("left")
        else:
            align.append(None)
    start_line = i + 1
    i += 2
    rows = []
    while i < len(lines) and lines[i].lstrip().startswith("|"):
        rows.append(split_table_row(lines[i]))
        i += 1

    def cell(tag, txt, k):
        a = align[k] if k < len(align) else None
        st = ' style="text-align:%s"' % a if a else ""
        return "<%s%s>%s</%s>" % (tag, st, render_inline(txt, link_resolver), tag)

    # class="tablewrap": the name theme.css actually styles ('.tablewrap {
    # overflow-x: auto }'). This wrapper WAS emitted as "table-wrap", which no
    # rule matched, so every one of the corpus's ~3800 table rows rendered with
    # no scroll container and a wide table pushed the whole page body into a
    # horizontal scroll. templates.py emits "tablewrap"; this is the same box
    # and carries the same name.
    html = ['<div class="tablewrap"><table>', "<thead><tr>"]
    for k, h in enumerate(header):
        html.append(cell("th", h, k))
    html.append("</tr></thead><tbody>")
    for r in rows:
        html.append("<tr>")
        for k in range(len(header)):
            html.append(cell("td", r[k] if k < len(r) else "", k))
        html.append("</tr>")
    html.append("</tbody></table></div>")
    return ("".join(html),
            {"headers": header, "rows": rows, "align": align, "line": start_line},
            i)


def _parse_list(lines, i, link_resolver):
    """Parse a list, nesting by indent. Returns (html, next_index)."""
    def item_at(idx):
        if idx >= len(lines):
            return None
        m = _OL_RE.match(lines[idx])
        if m:
            return ("ol", len(m.group(1)), m.group(4), m.group(5), m.group(2))
        m = _UL_RE.match(lines[idx])
        if m:
            return ("ul", len(m.group(1)), m.group(3), m.group(4), None)
        return None

    first = item_at(i)
    base_indent = first[1]
    kind = first[0]
    start = first[4]

    out = []
    if kind == "ol" and start not in (None, "1"):
        out.append('<ol start="%s">' % escape(start))
    else:
        out.append("<%s>" % kind)

    while i < len(lines):
        it = item_at(i)
        if it is None:
            if not lines[i].strip():
                # A blank line ends the list unless another item follows at or
                # deeper than base indent (loose list).
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                nxt = item_at(j)
                if nxt and nxt[1] >= base_indent:
                    i = j
                    continue
            break
        k, indent, _sp, text, _st = it
        if indent > base_indent:
            # Deeper item: recurse and attach inside the open <li>. Depth is
            # checked BEFORE kind, so a nested '1.' under a '- ' nests rather
            # than flattening into a sibling list.
            sub, i = _parse_list(lines, i, link_resolver)
            if out and out[-1].endswith("</li>"):
                out[-1] = out[-1][: -len("</li>")] + sub + "</li>"
            else:
                out.append(sub)
            continue
        if indent < base_indent or k != kind:
            break

        i += 1
        content = [text]
        # Continuation lines: indented further, not themselves items.
        while i < len(lines):
            if not lines[i].strip():
                break
            nxt = item_at(i)
            if nxt is not None:
                break
            stripped = lines[i]
            if len(stripped) - len(stripped.lstrip()) > base_indent:
                content.append(stripped.strip())
                i += 1
                continue
            break
        out.append("<li>%s</li>"
                   % render_inline(" ".join(content), link_resolver))

    out.append("</%s>" % kind)
    return ("".join(out), i)
