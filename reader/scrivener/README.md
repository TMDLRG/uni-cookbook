# Scrivener -- HONEST-store note-taker

The Scrivener is a sibling app to the read-only Encyclopedia-Cookbook reader.
It captures HONEST signals -- notes, questions, predictions, theories,
hypotheses, and observations of nature -- from wherever you are in the reader
(or on the standalone list page) and stores them locally in the browser.

It is not part of the reader's TRUE store. It is sovereign. Read on.

## What it stores, and where

Everything the Scrivener writes lives in **your browser's IndexedDB**, in a
database called `cookbook.scrivener`, in a store called `notes`.

There is **no server component** in v1. The Scrivener never talks to any
network endpoint. It does not `fetch()`. It does not open a WebSocket. It has
no back door to the generator's filesystem: the reader's read-only invariant
is untouched by adding this app.

If you clear your browser's site data, or open the reader in a private-mode
window, or move to a different browser, the notes on the machine you left
behind stay there and the new browser starts empty. Use **Export JSON** to
carry a copy off the device; use **Import JSON** on the new one.

## HONEST vs TRUE -- the sovereign split

The reader's cookbook carries the TRUE store: falsifiable, reproducible,
recalibratable material with citations. The Scrivener carries the HONEST
store: your lived experience, exactly as lived.

The two never merge. In practice this means the Scrivener:

- **Does not calibrate anything you write.** Your words go in as your words.
- **Never edits a note in place.** If a note is later wrong, you write a NEW
  note that supersedes it -- and the old note stays on record. This is the
  append-only rail; corrections are always additions, never overwrites.
- **Never uses the words "verified" or "proven"** in the UI's own voice.
- **Requires a falsifier** for `prediction` and `hypothesis` notes. Without
  a falsifier, a prediction or a hypothesis is inadmissible -- the Save
  button stays disabled until you supply one. This mirrors the operator's
  doctrine directly in the UI rather than trusting the human to remember it.

If you write a `theory` and later find it was wrong, the correct move is to
capture a new note (with `supersedes = <old id>`) that says so. The old
theory is honest history; it stayed true to what you thought at the time.

## How to use it

- Any page that loads `app.js` shows a small floating **S** button in the
  bottom-right corner. Click it to open the capture modal.
- A page can also dispatch a `scrivener:open` window event with an optional
  `detail` object (see below) to pre-fill the modal.
- The standalone list page (any page carrying `[data-role="scrivener-list"]`)
  mounts a full list-and-manage view with search, filter, export, and import.

### Note fields

| field         | notes                                                |
| ------------- | ---------------------------------------------------- |
| type          | one of note, question, prediction, theory, hypothesis, observation |
| title         | short; optional                                      |
| body          | markdown-ish plain text; stored as-is, not rendered  |
| tags          | comma-separated                                      |
| anchor        | chapter / heading / url, auto-filled from the page   |
| falsifier     | required for prediction / hypothesis                 |
| location      | optional; only captured if you tick the checkbox     |
| supersedes    | set automatically when you use the "Supersede" action |

Each saved note also carries:

- `id` -- a time-prefixed random hex string (sorts by time)
- `created_utc` -- ISO-8601 UTC
- `device_hint` -- a short device / user-agent tail
- `store` -- always `HONEST`

### Programmatic capture

```js
window.dispatchEvent(new CustomEvent("scrivener:open", {
  detail: {
    type: "observation",
    title: "grass wet at dawn",
    body: "no rain overnight; dew.",
    tags: ["field", "weather"],
    anchor: { chapter_id: "ch-03", heading_id: "sec-dew" }
  }
}));
```

The public JS surface is also on `window.Scrivener`:

```js
Scrivener.open(opts)          // open the modal
Scrivener.list_all()          // Promise<[note, ...]>
Scrivener.get(id)             // Promise<note|null>
Scrivener.add(note)           // Promise<note>  (add only; append-only)
Scrivener.import_batch(notes) // Promise<{new, duplicate, malformed}>
Scrivener.note_to_markdown(n) // string
```

There is intentionally no public `delete` in the UI or the public API. The
doctrine forbids removing an HONEST note. A hidden `_dev_delete` exists on
`window.Scrivener` for exceptional developer use only; do not wire it into
any UI.

## Export / import

- **Export JSON** downloads `scrivener-YYYY-MM-DDTHHMMSSZ.json`, wrapping
  every note in `{ schema_version, exported_utc, store: "HONEST", notes: [...] }`.
  Use this to back up a browser or move notes across devices.
- **Export Markdown** downloads a `.md` with one section per note, front-matter
  first, then body. Suitable for reading, archiving, or feeding into a
  downstream TRUE-store admission pipeline (which does its own calibration --
  do not conflate the two).
- **Import JSON** reads a previously exported file and adds notes it does not
  already have. An id that already exists is **ignored**, not overwritten --
  this preserves the append-only rail. A summary counts new / duplicate /
  malformed rows.

## Rails and constraints for anyone editing this app

- Vanilla JS, stdlib-only. No frameworks, no build step, no npm.
- Pure ASCII in every emitted byte. All non-ASCII characters go as numeric
  character references or `\uXXXX` escapes. This is load-bearing because the
  fleet's only file transport silently corrupts multi-byte UTF-8.
- No external network references. No CDN. No webfont. No `fetch()`, no
  `XMLHttpRequest`, no `WebSocket`.
- No inline `on*` handlers in emitted HTML. Wire events via
  `addEventListener` from `app.js`.
- Never add a delete-a-note UI. Corrections happen by superseding.
- Never write "verified" or "proven" in the UI's own voice. If a downstream
  process calibrates a note, that is a TRUE-store operation and belongs
  somewhere else, not here.

## Fallback: no IndexedDB

If a browser has IndexedDB disabled (private-mode Safari on some builds,
ancient runtimes), the modal still saves -- it downloads a one-note JSON
file so nothing is lost. The list view will say clearly that no local store
is available.
