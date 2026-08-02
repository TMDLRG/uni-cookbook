# The reader

A read-only reader for this repository, built from this repository.

```
python reader/build.py
python -m http.server -d reader/dist 8080
```

Then open <http://localhost:8080/>. That is the whole thing. Python 3 standard
library only: no pip, no npm, no CDN, no webfont, no analytics, no vendored
dependency, and nothing fetched from the network at build time or at page-view
time. The built pages also open directly from the filesystem — every link is
relative.

Build output goes to `reader/dist/`, which is gitignored. **The repo is the
source of truth; the rendered site is never it.** Delete `reader/dist/` and
rebuild whenever you want; nothing is lost, because nothing lives there.

---

## What it renders

| | |
|---|---|
| Chapters | `encyclopedia/**/*.md` and `cookbook/**/*.md` |
| Ledgers | `encyclopedia/CLAIM-LEDGER.md` (UNI fence), `encyclopedia/NATURE-LEDGER.md` (NATURA classes) |
| Registers | `lexicon/CONCEPTS.json` + `lexicon/terms/*.json` → five register pages |
| Plates | `reader/plates/PL-*.svg` + `PL-*.json` |
| Apparatus | front page, A-Z index, concordance, colophon |

At the last build: **78 chapters, 10 plates, 918 rows** of `## The numbers`
tables, **130** lexicon concepts registered, **43** entries authored, across
**98** files.

Everything in the repo that is **not** rendered is listed on
`/colophon.html` with its sha256 and the reason. Nothing is skipped silently —
a silent omission would break the claim that this is the real, as-is repo.

## The invariants, and how to falsify each

Each is structural — a property of what the code can do, not a promise in a
document.

**1. Read-only.** `build.py` has exactly one write door (`_write_bytes`), and
it resolves the target and refuses any path not inside `reader/dist/`. Reads
go through `read_bytes()`, mode `'rb'`. No database, no server, no form, no
API, no edit affordance. *Falsify it:* run
`reader/test_reader.py::test_readonly_invariant`, or monkeypatch `builtins.open`
and rebuild and assert every write-mode call lands in `dist/`, or simply
`git status` across a build.

**2. ASCII-only output.** Every page is encoded `xmlcharrefreplace`, and
`_write_bytes` re-checks every byte before it lands. Devanagari, IAST, Greek
and em-dashes all leave as numeric character references. This is not cosmetic:
the fleet's MCP `os_file_write` silently corrupts multi-byte UTF-8 — drops
bytes, returns `ok=true` with a wrong sha — and it is the only file transport
this box has. ASCII-only bytes make that bug unable to fire. *Falsify it:* any
emitted byte `>= 0x80`.

**3. Provenance or no page.** Every page carries source path + sha256 + commit
+ built UTC. `build_provenance()` raises rather than half-stamp, and
`templates.render_page()` raises `ProvenanceError` independently. Two locks,
no flag to open either. *Falsify it:* a page missing any of the four.

**4. No external network references.** `fence_scan()` greps every emitted page
for remote asset references and fails the build on a hit. *Falsify it:* load
any page with the network off. Anything that fails to render refutes this.

**5. The repo is the truth.** Every page renders bytes read from its repo file
at build time. Nothing is cached, hand-copied, or carried between builds.
*Falsify it:* the procedure below.

## The test suite

```
python reader/test_reader.py          # 75 tests, stdlib unittest, ~11s
python reader/test_reader.py -v       # each test names what it observes
python reader/test_reader.py TestReadOnlyInvariant
```

It runs ONE real build against the real repo (nothing is mocked, the corpus is
not copied) with every mutation door instrumented — `open()` in a write mode,
`rmtree`, `remove`, `rename`, `mkdir` — and asserts on the record. It also
sha256s the whole repo before and after and requires the bytes not to move.
Last observed run: **75 passed, 0 failed**, against 97 pages.

Two of these tests are easy to write in a way that fails loudly while measuring
the wrong thing, and both mistakes were made and are documented at the test
that fixes them:

- **`test_no_external_refs` must not grep for `http`** — see gap 2 below.
- **`test_no_perfect_claims` must not grep pages for "perfect" or "verified".**
  Measured on the built site: 29 occurrences of "perfect", 1054 of "verified" —
  every one of them *corpus prose*, in the corpus's own voice ("nature did not
  build one perfect component", CN-05). `proven` is likewise the CLAIM-LEDGER's
  own legitimate vocabulary for UNI's build status. A page-wide grep fires on
  all of it, and the only way to make it pass is to censor the repo — breaking
  the one thing the reader exists to keep. So the test reads the **reader's own
  authored strings**, via `ast`, and the reader's own chrome. SIGNUM SIGNUM
  MANET: the corpus's voice and the reader's travel separately.

Every fence test carries a **positive control** (a deliberate violation it must
catch) and, where it could fire on the innocent, a **negative control** (the
real legitimate case it must pass — the SVG namespace, a DOI citation, a CSS
comment stating the fence, the corpus's own honest prose). A fence never shown
to fire is a decoration, not a fence; and a test that has never been shown to
pass the innocent is a censorship engine waiting for a maintainer.

## How to verify a page against the repo file it came from

Every page's footer names its source and the sha256 of the bytes that were
rendered. That digest is the receipt:

```
python -c "import hashlib;print(hashlib.sha256(open('encyclopedia/wing-NATURA/NA-05-ratios-and-scaling-laws.md','rb').read()).hexdigest())"
```

Compare it to the `sha256` in the footer of `/chapter/na-05.html`. If they
differ, the page is stale or wrong, and the page is the thing that is wrong.

### The commit is context; the sha256 is the receipt

A repo commit does **not** mean a file's bytes are in it. At the time of
writing, `lexicon/` and `reader/plates/` are **untracked** — stamping
`commit f1be794` beside a lexicon page would assert its content is in that
commit, which is false. So every page states its own git file-state next to
the commit, and says so on the page when the commit does not describe those
bytes:

| file state | what the page says |
|---|---|
| `clean` | the commit describes these bytes |
| `modified` | tracked, but modified in the working tree — the commit does **not** describe these bytes |
| `untracked` | in **no** commit; the sha256 is this page's only receipt |
| `unknown` | git was unavailable at build time; the sha256 is the only receipt |

## The five registers are not five translations

**English is the only register with full chapter prose.** That is the honest
state and every non-English register page says so, carries a PENDING badge, and
prints its own counts, computed at build time from `lexicon/`:

| register | status census (at last build) |
|---|---|
| Sanskrit | CITED 1 · COINED 42 |
| Latin | CITED 1 · COINED 39 · PENDING-CITATION 3 |
| Hindi | COINED 8 · PENDING-CITATION 35 |
| Spanish | PENDING-CITATION 43 |

No chapter is machine-translated. Presenting machine output as a register would
be fabrication, so the prose is absent rather than invented. No back-translation
test in `lexicon/` has been run and no lexicographer has reviewed any entry, so
every rendering is PENDING / SUB EXAMINE. Of 130 registered concepts, 43 carry
an entry in any register. Nothing in the reader is hardcoded about this: change
`lexicon/` and the counts move.

## Two vocabularies, never merged

The reader renders the **NATURA classes** (nature's observed regularities,
twelve classes, governed by `wing-NATURA/NA-00`) and the **UNI 4-value fence**
(UNI's own build status, governed by `CLAIM-LEDGER.md`) as visually distinct
badges that share no CSS class.

This is not decoration. **`hypothesized` is a member of both vocabularies and
means different things in each.** So badge identity can never rest on the token
text. A NATURA citation is never a UNI gate: reading Kleiber's law raises no
UNI rung. `build.py` asserts the two badge vocabularies stay disjoint, and a
ledger page will not render unless it declares which vocabulary it speaks.

---

## The Markdown subset (`markdown.py`)

`markdown.py` renders the Markdown **this corpus actually uses**, measured
across all 90 `.md` files — not CommonMark in general. Every omission below is
a defect avoided, not a gap.

**Supported:** ATX headings (97 h1 / 857 h2 / 396 h3), fenced code (278), GFM
tables (3800 rows, 244 delimiter rows, 86 with escaped pipes, 0 column
mismatches), unordered lists (1942), ordered lists (668), blockquotes (1356),
thematic breaks (440), code spans, strong, emphasis, links, backslash escapes.

**Deliberately not supported, and why:**

- **4-space indented code blocks.** All 172 candidate lines in this corpus are
  ordered-list *continuation* lines (e.g.
  `cookbook/recipes/L12-creativity-awareness.md:104-108`). Implementing
  indented code would render that prose as code.
- **`$...$` / `$$...$$` TeX math.** There is **zero** TeX math in this corpus.
  All 20 lines containing `$` are shell variables (`$env:UNI_MCP`,
  `deploy/README.md:93`) or money (`$200` in `CLAIM-LEDGER.md:311`, `$3,450` at
  `:380`). A `$` math rule would eat the ledger's own numbers. Display math
  here is written as fenced code with Unicode and renders as such — correctly,
  and with nothing to fetch.
- **Setext headings.** Zero in the corpus; all 90 files open with an ATX `#`.
  Supporting them would make the 440 `---` thematic breaks ambiguous.
- **Raw HTML passthrough.** There is no flag for this. See below.
- **Images, reference links, autolinks, strikethrough.** Zero in the corpus.

### Raw HTML is escaped, always — that is fidelity, not only security

The corpus contains angle-bracket text that is prose, not markup: `<sha>`
(`cookbook/MASTER-PLAN.md:821`) and `<r̄>` (`encyclopedia/NATURE-LEDGER.md:464`).
Passing HTML through would **delete those words from the page** — the browser
would eat them as unknown tags. Escaping is what makes the page faithful to the
repo; it also means this renderer cannot emit an injected script.

### Math degrades honestly or not at all

No math engine is vendored, so none is faked. A fenced block marked `math`,
`tex` or `latex` renders as **labelled TeX source** in a `<pre class="math-src">`
with a caption saying it is not typeset. The corpus currently contains no such
block; the path exists so that adding one degrades to honest source rather than
to a silent CDN fetch.

---

## The ctx contract

`build.py` is the producer; `reader/templates.py` owns
`render_page(kind, ctx) -> str` and documents the contract, including a
machine-readable `templates.CONTRACT`. **Where the two disagreed, templates.py
won and build.py changed.** Read `templates.py`'s module docstring for the
authoritative field list. The parts most easily got wrong:

- `provenance.built_utc` — *not* `build_utc`.
- `href` is emitted **verbatim**; `root` is used only for `theme.css`. So every
  href must already be page-relative (`../ledger/x.html` from inside
  `chapter/`). `build.py` computes this with `root_for(url)`.
- `kind='ledger'` **requires** `vocabulary` in `('uni','natura')` or it raises
  `VocabularyError` — the sovereignty guard.
- `kind='plate'` requires `plate_id`; pass `svg_markup` (inline), never an
  `<img>` — an `<img>`-embedded SVG cannot see the page's `data-theme`.
- A missing **chapter** is `pending=True` + `pending_reason`, and `sha256` may
  then be omitted. Missing **provenance** raises. These are different things.

### Contract gaps — CLOSED 2026-07-16, each with the test that holds it shut

These were found by building the site and reading the emitted bytes, not by
reading the source. Each is now fixed and each fix carries a named falsifier in
`test_reader.py`, so it cannot silently come back.

1. ~~**`numbers` rows:** `units`/`scope` escaped as plain text.~~ **CLOSED.**
   templates now accepts `units_html`/`scope_html` (the plain keys still work
   and are still escaped); `build.py` renders both through
   `md.render_inline`. A real cell — `**ideal** regular tetrahedron` — showed
   its asterisks while `value` beside it rendered.
   *Falsifier:* `test_numbers_cells_render_their_markdown`.
2. ~~**`kind='ledger'` with `rows=[]`:** an empty table reading "PENDING: no
   rows were passed to this ledger".~~ **CLOSED.** The table is suppressed when
   `intro_html` carries the document; an honest PENDING remains for the case
   where there is genuinely nothing. It printed PENDING directly beneath the
   fully-rendered ledger — lying in the modest direction, which is still lying,
   and it teaches a reader to discount every other PENDING on the site.
   *Falsifier:* `test_ledger_does_not_claim_a_false_pending`.
3. ~~**Plate numbers:** `build.py` passed `number='PL-01'`; `_roman()` int()s
   it, failed, returned `''`.~~ **CLOSED.** Every chapter plate captioned
   itself `Plate .` with no number. `load_plates()` now assigns the ordinal
   once, and the plate page and every citing chapter print the same one.
   *Falsifier:* `test_plate_numbers_render`.
4. ~~**Plate `source_chapters`:** `esc()`'d a dict.~~ **CLOSED.** 47 Python dict
   reprs — `{'href': '../chapter/na-04.html', 'label': ...}` — were the visible
   text of the "Drawn from" marginal on every plate page. templates now renders
   `{href,label}` as a link and `{label}` as a path.
   *Falsifier:* `test_plate_source_chapters_are_links`, `test_no_python_repr_reached_a_page`.
5. ~~**Table wrappers:** `markdown.py` emitted `class="table-wrap"`; `theme.css`
   styles only `.tablewrap`.~~ **CLOSED.** No rule matched, so all ~3800 corpus
   table rows rendered with no `overflow-x` container and a wide table pushed
   the whole page body into a horizontal scroll.
   *Falsifier:* `test_table_wrap_class_matches_the_stylesheet`.
6. ~~**Lexicon status census:** `build.py` passed flat counts; templates reads
   `counts['status_census'].`~~ **CLOSED.** The one table stating the honest
   shape of the whole lexicon never rendered on any page.
   *Falsifier:* `test_register_counts_are_counted_not_claimed`.
7. **`markdown.py` had no link-scheme fence.** **CLOSED (latent, never fired).**
   The corpus contains zero `javascript:`/`data:` links — measured — so nothing
   was wrong on the page. But the fence was "no author has typed one yet",
   which is luck, not a fence. A refused scheme now renders as inert text
   carrying its own words; refusing to execute a thing is not a licence to
   delete it. *Falsifier:* `test_link_scheme_fence`, `test_safe_schemes_still_work`.

### Known contract gaps (open, and honest about it)

1. **The provenance footer** says a page "renders the repository file named
   above, as it stood at that commit." That is true only for a tracked,
   unmodified file. `build.py` compensates by appending the file-state
   qualifier to the `commit` string itself, so the correction travels on the
   page. *Fix:* let templates render `provenance.git_state` directly.
   Held meanwhile by `test_provenance_commit_does_not_overclaim`, which fails
   if an untracked or modified file is ever stamped without its qualifier.
2. **`test_no_external_refs` must not grep for the bare substring `http`.**
   Two legitimate cases exist: `xmlns="http://www.w3.org/2000/svg"` on every
   inlined plate (an XML namespace *identifier*, never dereferenced) and
   `<a href="https://doi.org/...">` citations (user-initiated navigation, not
   an asset fetch). Test for **fetching constructs**: `src=`, `<link href=`,
   `url(`, `@import` pointing at `http(s)`. `build.py`'s own `fence_scan()`
   does exactly this, and scopes `@import`/`url()` to style contexts with
   comments stripped — because both `PL-01.json` and `theme.css` *describe*
   the fence in prose ("no `@import`"), and an unscoped grep fires on the
   promise instead of the violation.

## Build notes are content, not noise

`build.py` reports what it observed about the corpus rather than swallowing it.
All of it lands on `/colophon.html`. At the last build, 52 notes, including:

- **`url-collision`** — `encyclopedia/00-INDEX.md` and `cookbook/00-INDEX.md`
  both slug to `00-index`, as do the two `MASTER-PLAN.md` files. Every member
  of a colliding group gets a section-qualified url, so no chapter is
  overwritten and urls do not depend on walk order. `emit()` refuses a
  duplicate write outright: an earlier build reported 98 pages written into 95
  files while three chapters vanished with no error.
- **`unregistered-class`** — a `## The numbers` Class cell naming none of
  NA-00's twelve registered classes: `as above` (a back-reference), and
  `**NEGATIVE (framing superseded)**` — `NEGATIVE` is deliberately *not* a
  NATURA class (NA-00 says registering it as one would put a UNI ledger state
  into nature's vocabulary). The cell is carried verbatim and rendered as-is,
  never dropped and never invented into a class. This is NA-00's own falsifier
  #2 kept from firing silently.
- **`numbers-table-shape`** — a `## The numbers` table whose headers do not
  match the corpus convention. Headers are *normalised*, not exact-matched: of
  the 23 tables, 21 use `Symbol|Value|Units|Scope|Class|Source|Falsifier`,
  `NA-01` uses `Scope (where it holds)`, and `NA-03` uses lowercase. Exact
  matching would silently drop two chapters' numbers.

## Structure

| file | owner | what it is |
|---|---|---|
| `build.py` | this reader | the generator: repo walk, provenance, ASCII emission, `dist/` |
| `markdown.py` | this reader | the dependency-free Markdown subset renderer |
| `templates.py` | separate | `render_page(kind, ctx) -> str`, the page shells |
| `theme.css` | separate | the print-encyclopedia stylesheet (light + dark + print) |
| `test_reader.py` | separate | the invariant tests |
| `plates/` | separate | 10 engraved reference plates (SVG + JSON) |

## Honest state

- The chapters have **no front matter**. Measured: 0 of 90 files open with
  `---`. Chapter metadata is derived from the document's own structure — the H1
  is the title, and a leading blockquote is the abstract. Only **38 of 90**
  chapters have one; the rest render without an abstract rather than with a
  fabricated summary.
- The reader ships **no search box**. `/search.html` is a static concordance —
  every heading of every page, printed, so the browser's own find works
  offline.
- `templates.py` ships a small inline theme-toggle script and an offline filter.
  Both are local and fetch nothing. The **plates** are held to the stricter
  design-only fence: `build.py` verifies each SVG for `<script>`, `on*`
  handlers, `@import`, remote `url()`/`href`, and `<foreignObject>` **on the
  bytes**, and refuses to inline any plate that trips it — rather than trusting
  the `design_fence` block in the plate's own JSON, which is the plate's
  narrative about itself.
- The reader renders the corpus. It states no claim of its own about nature or
  about UNI, and it raises no rung.
