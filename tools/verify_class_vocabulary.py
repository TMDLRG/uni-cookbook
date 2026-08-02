# -*- coding: utf-8 -*-
"""verify_class_vocabulary.py — the falsifier for the NA-00 class-vocabulary amendment
of 2026-07-15.

Pre-registered BEFORE the amendment was written. It answers exactly one question:

    does any row of encyclopedia/NATURE-LEDGER.md, any classed entry of
    gpt/knowledge/K20-constants-ratios-and-nature-ledger.json, or any row of the
    "## The numbers" tables in the CHAPTERS THEMSELVES, carry a class string
    outside the vocabulary NA-00 registers?

It is the operable form of NA-00's own falsifier #2 ("the classes are not exhaustive or
not disjoint"). That falsifier FIRED once already, on 72 rows; this script is what keeps
it from firing silently again.

SCOPE DEFECT, RECORDED AND CLOSED 2026-07-15-C — read this before trusting a PASS.
    This script formerly checked the ledger and K20 and NOTHING ELSE. It never opened the
    23 chapters it was certifying. On 2026-07-15 it therefore reported
    "PASS - zero rows outside the registered vocabulary" while **52 chapter rows across
    10 files still carried PRE-amendment class strings** (42 bare/qualified `OBSERVED`,
    3 `NEGATIVE`, 5 `as above`, 2 CN-05 cells not leading with a token). The amendment had
    closed the ledger and K20; the chapters were never in scope, so the gap could not be
    seen from the tool's own output. A verifier whose scope is invisible cannot be audited,
    and a green result from a narrow scope is worse than no result: it is a false negative
    wearing a PASS.
    Two things close it: (1) CHAPTERS are now a scope, counted on their own line;
    (2) EVERY scope prints itself below, so the next reader can see what was NOT checked.

TOKENIZER, CHANGED 2026-07-15-C, and why — this changed a real number, so it is declared.
    lead_token() previously used strip_bold(), which only strips `**` when the WHOLE cell
    is bold. Chapter cells routinely bold only the token and leave the qualifier plain
    (`**MODELED** (as above; unreplicated)`), so strip_bold() returned the cell unchanged,
    `^(TOKEN)\\b` hit the leading asterisks, and the cell was reported OUT-OF-VOCABULARY
    although its class is plainly MODELED. On the chapters that produced 40 FALSE
    POSITIVES on top of the 52 real rows (90 reported, 52 real). Emphasis markers are now
    stripped before the leading-token match. This is safe by construction: every registered
    class token is drawn from [A-Z-] only, so removing `*`, `` ` `` and `_` cannot damage,
    truncate or lengthen a token. It changes NO ledger or K20 count (both were already
    whole-cell-bold or plain); it only stops the chapter scan from crying wolf. The count
    it changes is 90 -> 52, and 52 is the number the chapters were actually fixed against.

Exit 0 = zero out-of-vocabulary rows IN EVERY SCOPE. Exit 1 = at least one scope is
incomplete; the count and the offending rows are printed per scope. A non-zero exit is a
real finding, not a test bug.

Run:  python tools/verify_class_vocabulary.py
"""
import collections
import glob
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "encyclopedia", "NATURE-LEDGER.md")
K20 = os.path.join(ROOT, "gpt", "knowledge",
                   "K20-constants-ratios-and-nature-ledger.json")

# The chapters this script certifies. Globbed, never listed by hand: a hard-coded list
# would silently drop a chapter added later, which is the same class of scope defect this
# script was extended to close.
CHAPTER_DIRS = [
    os.path.join("encyclopedia", "wing-NATURA"),
    os.path.join("cookbook", "recipes-natura"),
]

# ---------------------------------------------------------------- vocabulary
# The six canonical classes (NA-00, original design).
SIX = [
    "OBSERVED-REPLICATED",
    "OBSERVED-CONTESTED",
    "MODELED",
    "HYPOTHESIZED",
    "INADMISSIBLE",
    "NOT-MEASURED",
]

# Registered by AMENDMENT 2026-07-15-A (NA-00 §"Amendment record").
AMENDED = [
    "OBSERVED-SINGLE",      # measured, no independent replication on record
    "MODELED-CONTESTED",    # model-derived AND genuinely disputed
    "SUPERSEDED",           # once carried, since retracted/withdrawn/contradicted
    "NOT-SOURCED",          # value stated, source not traced in this pass
    "NOT-CONFIRMED",        # primary named at one remove, not read in this pass
    "NOT-LOCATED",          # the named source was searched for and not found
]

REGISTERED = SIX + AMENDED

# Rows that deliberately carry NO evidence class, and are registered AS SUCH by the
# amendment rather than given one. Keyed by ledger_row_id, because the whole point is
# that each is an individually-named exception, not an open category.
NOT_A_CLASS = {
    "NA03-16": "definitional convention (SI defining constants) - not an observation of nature",
    "CN04-22": "historical prediction, not a measurement - the measurement is CN04-23",
    "CN11-59": "HONEST signal (first-person testimony) - belongs to the HONEST store, never calibrated",
    "CN12-41": "NONDUM FALSIFICABILIS - a register status, extra Arborem, not an evidence class",
}

PIPE_SPLIT = re.compile(r"(?<!\\)\|")
ROW_RE = re.compile(r"^\|\s*`([A-Z]{2}\d{2}-\d+)`\s*\|")

# A class cell must LEAD with a registered token. Qualifiers after it are free text
# (provenance notes, part-names for compound rows) and are carried verbatim.
TOKEN_RE = re.compile(r"^(%s)\b" % "|".join(
    sorted(REGISTERED, key=len, reverse=True)))


def strip_bold(s):
    s = s.strip()
    while s.startswith("**") and s.endswith("**") and len(s) > 4:
        s = s[2:-2].strip()
    return s


# Emphasis markers are never part of a class token: every registered token is [A-Z-] only.
# Removing them before the leading-token match therefore cannot damage a token, and it is
# what lets `**MODELED** (qualifier)` parse as MODELED. See the TOKENIZER note in the
# module docstring - this replaced strip_bold() in lead_token() on 2026-07-15-C.
EMPHASIS_RE = re.compile(r"[*`_]+")


def strip_emphasis(s):
    return EMPHASIS_RE.sub("", s.strip()).strip()


def lead_token(cls):
    """Return the registered leading token of a class cell, or None.

    The cell must LEAD with the token once emphasis is removed. A cell that merely
    CONTAINS a token somewhere ('rung MODELED; overall band OBSERVED-REPLICATED',
    'value printed in source; provenance NOT-SOURCED') is deliberately NOT accepted:
    which class such a row carries is ambiguous, and the amendment re-ordered exactly
    those two cells rather than teaching the parser to guess.
    """
    m = TOKEN_RE.match(strip_emphasis(cls))
    return m.group(1) if m else None


SEC4_RE = re.compile(r"^##\s*4\.\s")
SEC5_RE = re.compile(r"^##\s*5\.\s")


def load_ledger():
    """Parse the ledger rows of section 4 ONLY.

    Scoped deliberately. Other sections (the §1 vocabulary tables, the §5 counts) legitimately
    cite row ids inside two-column documentation tables, and those are NOT ledger rows. An
    earlier revision of this script matched any table row starting with a backticked id and
    reported 923 rows against a true 919 - a false positive it raised against its own author.
    The ledger is what §4 contains; nothing else is a row.
    """
    rows = []
    in_sec4 = False
    for i, ln in enumerate(io.open(LEDGER, encoding="utf-8").read().split("\n")):
        if SEC4_RE.match(ln):
            in_sec4 = True
            continue
        if SEC5_RE.match(ln):
            in_sec4 = False
            continue
        if not in_sec4:
            continue
        m = ROW_RE.match(ln)
        if not m:
            continue
        body = ln.strip().strip("|")
        cells = [c.strip() for c in PIPE_SPLIT.split(body)]
        rows.append({"lineno": i + 1, "id": m.group(1), "cells": cells})
    return rows


def check_ledger():
    rows = load_ledger()
    bad, byclass = [], collections.Counter()
    # duplicate ids would mean §4 scoping has broken, or a row was pasted twice
    dupes = [k for k, v in collections.Counter(r["id"] for r in rows).items() if v > 1]
    for k in dupes:
        bad.append((k, "-", "DUPLICATE row_id in section 4"))
    for r in rows:
        if len(r["cells"]) != 10:
            bad.append((r["id"], r["lineno"], "MALFORMED: %d cells" % len(r["cells"])))
            continue
        cls = r["cells"][7]
        if r["id"] in NOT_A_CLASS:
            byclass["(carried, not classed)"] += 1
            continue
        tok = lead_token(cls)
        if tok is None:
            bad.append((r["id"], r["lineno"], strip_bold(cls)[:90]))
        else:
            byclass[tok] += 1
    return rows, bad, byclass


def check_k20():
    d = json.load(io.open(K20, encoding="utf-8"))
    lists = ["constants", "dimensionless_numbers", "scaling_laws",
             "frequencies", "inadmissible", "open_questions"]
    bad, n = [], 0
    mirror_bad = []
    for L in lists:
        for e in d[L]:
            if not e.get("class"):
                continue
            n += 1
            rid = e.get("ledger_row_id")
            if rid in NOT_A_CLASS:
                continue
            if lead_token(e["class"]) is None:
                bad.append((e["id"], rid, e["class"][:80]))
            # the mirror invariant: contested_note, when it restates the class, must agree
            cn = e.get("contested_note")
            if isinstance(cn, str) and cn.startswith("class as written: "):
                if cn[len("class as written: "):] != e["class"]:
                    mirror_bad.append((e["id"], e["class"][:50], cn[:60]))
    return d, n, bad, mirror_bad


# ------------------------------------------------------------------ chapter scope
# The chapters are the artifacts the ledger EXTRACTS. Until 2026-07-15-C they were never
# checked, which is how 52 rows kept pre-amendment strings under a PASS. The class column
# is located from each table's OWN header row rather than hard-coded: the wing's tables are
# 7-column (Symbol|Value|Units|Scope|Class|Source|Falsifier), but reading the position from
# the header means a chapter that reorders its columns is still checked correctly instead
# of being silently mis-parsed.
NUMBERS_H_RE = re.compile(r"^##\s+The numbers\b")
SEP_RE = re.compile(r"^\|[\s:\-\|]+\|$")


def chapter_files():
    out = []
    for d in CHAPTER_DIRS:
        out.extend(sorted(glob.glob(os.path.join(ROOT, d, "*.md"))))
    return out


def chapter_number_rows(path):
    """[(lineno, class_cell)] for every row of this file's '## The numbers' table(s).

    Scoped to that section on purpose. These chapters carry other tables (crosswalks,
    vocabulary restatements, worked examples) whose cells are prose about classes, not
    class cells - counting those would be the mirror of the ledger's own 923-vs-919
    false positive.
    """
    rows = []
    in_sec, class_idx = False, None
    for i, ln in enumerate(io.open(path, encoding="utf-8").read().split("\n")):
        if ln.startswith("#"):
            in_sec = bool(NUMBERS_H_RE.match(ln))
            class_idx = None
            continue
        if not in_sec:
            continue
        s = ln.strip()
        if not s.startswith("|") or SEP_RE.match(s):
            continue
        cells = [c.strip() for c in PIPE_SPLIT.split(s.strip("|"))]
        low = [c.lower() for c in cells]
        if "class" in low and ("symbol" in low or "value" in low):
            class_idx = low.index("class")      # header row - learn the column
            continue
        if class_idx is None or class_idx >= len(cells):
            continue
        rows.append((i + 1, cells[class_idx]))
    return rows


def prefix_of(path):
    """'NA-10-the-scale-ladder-and-gradients.md' -> 'NA10'; 'CN-01-rocks.md' -> 'CN01'."""
    m = re.match(r"^([A-Z]{2})-(\d{2})-", os.path.basename(path))
    return (m.group(1) + m.group(2)) if m else None


# NA03-16 (the SI defining constants) lives in NA-03's PROSE, immediately below its table,
# not in it. That is the whole of the ledger's disclosed 918-table-rows + 1 = 919. It is the
# only ledger row with no chapter table row, and excluding it here is what makes the
# positional alignment below exact rather than off-by-one.
PROSE_ONLY = {"NA03-16"}


def check_chapters(ledger_rows_):
    """Out-of-vocabulary class cells in the chapters' own '## The numbers' tables.

    Chapter tables carry no row_id column, so rows are aligned to the ledger POSITIONALLY,
    which is exactly what the ledger promises ("sorted by chapter, then by the order the
    row appears in that chapter's table"). Two things fall out of that, both wanted:
      * offenders are named by their ledger_row_id, not just a line number; and
      * the four deliberately-unclassed rows are exempted from the SAME NOT_A_CLASS list
        the ledger uses, instead of a second hand-maintained copy that could drift from it.
    A count mismatch is reported as a finding in its own right: it means the ledger and the
    chapter it extracts have diverged, and no per-row class result from that file is
    trustworthy until it is resolved.
    """
    byprefix = collections.OrderedDict()
    for r in ledger_rows_:
        byprefix.setdefault(r["id"].split("-")[0], []).append(r)

    bad, misaligned, byclass, n = [], [], collections.Counter(), 0
    scanned = []
    for path in chapter_files():
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        pre = prefix_of(path)
        rows = chapter_number_rows(path)
        lrows = [r for r in byprefix.get(pre, []) if r["id"] not in PROSE_ONLY]
        scanned.append((rel, len(rows)))
        if pre is None or pre not in byprefix:
            if rows:
                misaligned.append((rel, "%d table rows but no ledger section" % len(rows)))
            continue
        if len(rows) != len(lrows):
            misaligned.append((rel, "ledger has %d rows, chapter table has %d"
                               % (len(lrows), len(rows))))
            continue
        for (lineno, cls), lr in zip(rows, lrows):
            n += 1
            if lr["id"] in NOT_A_CLASS:
                byclass["(carried, not classed)"] += 1
                continue
            tok = lead_token(cls)
            if tok is None:
                bad.append((lr["id"], rel, lineno, strip_emphasis(cls)[:80]))
            else:
                byclass[tok] += 1
    return scanned, n, bad, misaligned, byclass


def check_registry_declared():
    """The registered vocabulary must actually be declared in both artifacts."""
    led = io.open(LEDGER, encoding="utf-8").read()
    d = json.load(io.open(K20, encoding="utf-8"))
    missing = []
    for c in REGISTERED:
        if c not in led:
            missing.append("NATURE-LEDGER.md does not name %s" % c)
        if c not in d.get("evidence_classes", {}):
            missing.append("K20 evidence_classes lacks %s" % c)
    return missing


def main():
    print("=" * 78)
    print("NA-00 class-vocabulary verifier  (falsifier #2, operable form)")
    print("=" * 78)

    rows, bad, byclass = check_ledger()
    crows, cn, cbad, cmis, cbyclass = check_chapters(load_ledger())

    # ---- SCOPE, PRINTED. A verifier that does not say what it looked at cannot be
    # audited, and this script has already shipped one silent scope gap (see docstring).
    # Print it FIRST, before any result, so a green line is never read without it.
    print("\nSCOPE OF THIS RUN (what a PASS below does and does not cover)")
    print("  1. %-24s %s" % ("NATURE-LEDGER.md",
                             os.path.relpath(LEDGER, ROOT).replace("\\", "/")))
    print("     %-24s section 4 rows only; %d rows" % ("", len(rows)))
    print("  2. %-24s %s" % ("K20 machine twin",
                             os.path.relpath(K20, ROOT).replace("\\", "/")))
    print("  3. %-24s %d files, '## The numbers' tables only; %d rows" % (
        "CHAPTERS", len(crows), cn))
    for d in CHAPTER_DIRS:
        print("     %-24s %s/*.md" % ("", d.replace("\\", "/")))
    print("  NOT in scope: prose outside those tables; the UNI CLAIM-LEDGER (a separate")
    print("     sovereign vocabulary); any file not listed above.")

    print("\n[NATURE-LEDGER.md]  rows parsed: %d" % len(rows))
    for k, v in byclass.most_common():
        mark = "six     " if k in SIX else (
            "amended " if k in AMENDED else "not-class")
        print("   %s %4d  %s" % (mark, v, k))
    print("   %s %4d  %s" % ("-" * 8, sum(byclass.values()), "TOTAL"))

    d, n, kbad, mirror_bad = check_k20()
    print("\n[K20 json]  parses OK; classed entries: %d" % n)

    print("\n[CHAPTERS]  files scanned: %d; table rows parsed: %d" % (len(crows), cn))
    for k, v in cbyclass.most_common():
        mark = "six     " if k in SIX else (
            "amended " if k in AMENDED else "not-class")
        print("   %s %4d  %s" % (mark, v, k))
    print("   %s %4d  %s" % ("-" * 8, sum(cbyclass.values()), "TOTAL"))

    missing = check_registry_declared()

    print("\n" + "-" * 78)
    ok = True
    print("OUT-OF-VOCABULARY ROWS (ledger)   : %d" % len(bad))
    for rid, ln, c in bad:
        ok = False
        print("    %s (line %s): %s" % (rid, ln, c))
    print("OUT-OF-VOCABULARY ENTRIES (K20)   : %d" % len(kbad))
    for eid, rid, c in kbad:
        ok = False
        print("    %s [%s]: %s" % (eid, rid, c))
    print("OUT-OF-VOCABULARY ROWS (chapters) : %d" % len(cbad))
    for rid, rel, ln, c in cbad:
        ok = False
        print("    %s  %s:%d: %s" % (rid, rel, ln, c))
    print("LEDGER/CHAPTER MISALIGNMENTS      : %d" % len(cmis))
    for rel, why in cmis:
        ok = False
        print("    %s: %s" % (rel, why))
    print("CLASS-MIRROR DISAGREEMENTS (K20)  : %d" % len(mirror_bad))
    for eid, a, b in mirror_bad:
        ok = False
        print("    %s: class=%r note=%r" % (eid, a, b))
    print("UNDECLARED REGISTERED CLASSES     : %d" % len(missing))
    for m in missing:
        ok = False
        print("    %s" % m)

    print("-" * 78)
    print("RESULT: %s" % ("PASS - zero rows outside the registered vocabulary, "
                          "in every scope above"
                          if ok else "FAIL - at least one scope is incomplete"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
