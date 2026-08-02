# E1 - The calibration ledger and "Falsify this"

The UNI program keeps a single append-only evidence ledger, and that ledger, not any
headline, is the law. The encyclopedia authors *against* it: no chapter may state a
claim above the evidence class recorded there, omit a recorded falsifier, or hide a
recorded negative. This chapter is about the public artifact that makes that discipline
visible: a calibration ledger that records, per claim, an evidence class, a falsifier,
and a four-state verdict (PASS / FAIL / NEGATIVE / PENDING), and a "Falsify this" close
that hands a skeptic the exact condition that would prove the claim wrong. The honest
position the ledger enforces, printed and never softened, is that roughly **2 of 11+
developmental rungs are earned**, and the whole thing remains a developmental
active-inference SIMULATION, a bounded peek, a toy world, never a person and never a mind.

The load-bearing idea here is plain: **negatives are content.** A partial, a recorded
NEGATIVE, a "most pieces don't help" decomposition is a measurement that the design is
incomplete, not an exit and not a failure to hide. The negatives are the credibility. The
ledger is built so that a positive result can never travel without the negative that
delimits it.

## The four-state, append-only ledger (method, M1)

The Evidence Constitution (ledger row **M1**, class `method`) defines the public layer as
a chaptered Evidence Explorer carrying A-U evidence classes, a falsifier per claim, and a
four-state append-only ledger: PASS / FAIL / NEGATIVE / PENDING. Three rules give it
teeth. First, **calibration only moves DOWN** to the measured value, never up, including
under urgency: the fence gets louder under pressure, not wider. Second, a capability
**verdict is the confidence-interval bound that excludes the threshold, never the point
estimate.** Third, **DONE means test-covered (Class E/D), not feature-working (Class A)**:
a passing test does not satisfy a criterion that demands a runtime observation. The
falsifier for M1 itself is operable: a claim asserted ahead of its ledger, wording
calibrated up, or a verdict edited rather than superseded with lineage.

This discipline is enforced mechanically, not by good intentions. Ledger row **M8**
(class `method`) records a server-side evidence contract: every ticket walks
`TODO -> DD -> TDD_RED -> TDD_VERIFY -> TDD_GREEN -> TDD_REFACTOR -> TDD_VALIDATE -> DONE`,
each transition hard-blocked unless a marker-bearing evidence comment is logged first, DONE
requires at least two explicit `Y:` verdicts per criterion, and a **claim linter
auto-downgrades overclaims** (it caught a "PROVEN" and demoted it to Class E). M8's
falsifier: a phase transition that succeeds without its required marker, a DONE with fewer
than two `Y:` verdicts, or the linter failing to downgrade "PROVEN".

Significance is a gate, not a vibe. Ledger row **M29** (class `method`) records
**honesty-as-a-test**: a `framing_guard` build test fails the build if framing copy, the
DOI, accessibility, or "does not reproduce Rao's method" labeling regresses; and a
statistical PASS means a bootstrap 95% confidence interval on the median paired difference
excluding 0, under a seeded PRNG (Mulberry32) with a committed result cache, never a single
seed and never a point estimate. Its falsifier: framing or DOI or labeling regressing
without `framing_guard` failing, or a significance verdict decided on one seed.

## The provenance-flagged snapshot (read it as a snapshot)

The last recorded ledger snapshot is **882 rows = 350 PASS / 0 FAIL / 183 NEGATIVE /
349 PENDING.** This figure must be carried as a **provenance-flagged snapshot, not as a
re-countable headline.** The ledger derives from a deduplicated merge of 615 extracted
claims; the snapshot enumerates 882 rows; the carded body shows only about 140 distinct
rows. A skeptic counting the published rows **cannot** independently derive 183. So the
honest form is: the corpus records 183 published negatives as a snapshot, and the
credibility comes from the negatives the ledger body actually enumerates and cites
alongside their paired positives, not from the bare number "183" used as a trophy. Per the
calibration-down rule, the snapshot is cited as a snapshot, and the enumerated negatives
carry the weight.

## The audit layer: six headlines calibrated DOWN (Section 2)

The clearest worked example of calibration-down in action is the peer-reviewed honesty
audit recorded in the continuity sub-ladder (Section 2, audit-layer note, durable). Over
os-cycles 39-53, an audit **calibrated six headline claims DOWN to their measured value.**
Three are load-bearing and must be carried in their calibrated, not inflated, form:

- "cleared on **TWO boxes**" was calibrated to **ONE box.**
- "**the mind survives a patch**" was calibrated to **infrastructure continuity only.**
- "**5 stacks**" was calibrated to "**4 distinct stacks / 5 runs**."

The on-core inference anchor (ledger row **C6**, class A) is therefore carded exactly as: a
sealed f64 belief-update trace **byte-identical across 4 distinct software/emulated stacks
(5 runs)**, with the falsifier that a fifth distinct stack produces a non-identical trace,
or the cross-arch leg is shown not genuinely distinct. The continuity claim is carded at
its true reach by **C2** (class A, status NEGATIVE/OWED): Stage-1 showed mind-state surviving
a process restart bit-for-bit, but Stage-2, **mind-tick continuity across a real kernel
swap, is NOT shown and remains OWED** (the live OS update was proven infrastructure-only, a
real kexec cutover with zero data loss but no demonstrated mind-tick continuity; node2's
first attempt FAILED then recovered, infra-only). The discharging falsifier for C2 is
exact: a kernel swap shown preserving mind-tick continuity bit-for-bit end-to-end, not just
infrastructure.

The decisive and honest meta-finding: the **over-statements lived in the summary and
headline layers, not in fabrication.** The underlying measurements were sound; the words
that described them had drifted upward, and the audit pulled them back to the float. That
is the entire point of a calibration ledger. Say it exactly that way: nothing was faked;
the headlines were too loud, and the fence got louder, not wider, in response.

### What is NOT claimed in E1

- **Ceiling.** That UNI "has a verified system of 183 proven results" or that the continuity
  engineering proves a science gate is met is NOT shown. The most we claim is: the program
  maintains a four-state append-only ledger (M1) with server-enforced evidence transitions
  (M8) and statistics-not-vibes significance gates (M29); the last recorded snapshot is a
  **provenance-flagged 882 / 350 PASS / 0 FAIL / 183 NEGATIVE / 349 PENDING**, not a
  re-countable headline; and a recorded audit calibrated six headlines DOWN to the measured
  value (ONE box, infrastructure-only continuity, 4 distinct stacks / 5 runs).
- **Fences engaged.** Red line 7 (never raise a claim above its source class). Red line 8
  (substrate/continuity engineering must never imply a science gate is met). Red line 3
  ("active inference" is the framing lens, never a demonstrated loop). Red line 10 (no PII,
  no secrets, no featured channel handles). The calibration-down rule and the
  snapshot-provenance fence (FM-1).
- **Negatives that travel with this claim (cite alongside, never strip).** The six
  down-calibrations (Section 2 audit note: TWO boxes -> ONE; mind-survives-a-patch ->
  infra-only; 5 stacks -> 4 distinct stacks/5 runs). The **C2 NEGATIVE/OWED** row: Stage-2
  mind-tick continuity across a kernel swap is NOT shown. The provenance fence on the 183
  figure: it is a snapshot, not independently re-derivable from the carded rows.
- **Parked / owed.** Stage-2 continuity (C2) is OWED, not parked. The ledger's own
  `evidenceClass` field is partly self-asserted (a known unguarded surface, later partly
  code-gated), so the constitution is a discipline under continual hardening, not a finished
  proof.
- **One-line honest summary a skeptic could not dispute.** UNI publishes a four-state
  append-only ledger that records its negatives as first-class content and, on audit, pulls
  its own headlines down to the measured value rather than up.

## Falsify this

The lead falsifier for the calibration discipline is the one M1 itself names, stated
operably: find a public UNI claim asserted **ahead of its ledger row**, or a headline
figure carried at its **inflated** value rather than its **calibrated** one (for example,
"two boxes" where the ledger says one box, "the mind survives a kernel swap" where the
ledger says infrastructure-only and Stage-2 is OWED, or "5 stacks" where the ledger says
"4 distinct stacks / 5 runs"), or a "Falsify this" entry that ships with **no operable
falsifier at all.** Any one of those, found in shipped copy, falsifies the claim that this
program calibrates down rather than up. The standing rule holds: if the prose and the
ledger ever disagree, the ledger wins and the prose is wrong.

## Sources

- Curated digest: `curated/uni-os-digest.md` (the os-cycles 39-53 honesty audit, the
  calibration ledger, the infra-only kexec floor, the 4-distinct-stacks/5-runs anchor),
  PII-redacted. Underlying archive pointer: `...-UNI-OS`.
- Curated digest: `curated/uni-mind-digest.md` (the 882-row ledger snapshot
  350 PASS / 183 NEGATIVE / 349 PENDING, "the 183 negatives are the credibility,"
  authority-flows-downward calibration), PII-redacted. Underlying archive pointer:
  `...-uni-mind`.
- Ledger rows (single source of truth, `encyclopedia/CLAIM-LEDGER.md`): Section 0
  (negatives-are-content, the four-state constitution, the snapshot provenance fence);
  Section 2 audit-layer note and rows **C2** (NEGATIVE/OWED) and **C6** (4 distinct stacks /
  5 runs); method rows **M1**, **M8**, **M29**.
