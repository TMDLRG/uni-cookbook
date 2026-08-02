# mu1 - The Evidence Constitution and ledger discipline

The UNI program is a developmental active-inference SIMULATION: a bounded peek into a toy world, never a person, never a mind. Roughly 2 of 11+ developmental rungs are earned. Before any of that can be said honestly, there has to be a rule for what "earned" means, who decides, and how a claim is allowed to move. This chapter is that rule. It is a constitution, not a result. It asserts no capability. Nothing here proves the science; it only fixes the discipline that keeps every other chapter from overstating the science. If you read "we have a constitution" as "we have proven the program," you have already broken the first rule it sets.

The constitution is recorded in the ledger as a method-class claim (M1), and method is a ceiling as much as A or C is: a governance pattern is proven and reusable, but it can never be raised into a capability claim. That is the entire load this chapter carries, and it carries no more.

## The four-state append-only ledger

There is one single source of truth: the append-only claim ledger. Every claim lives there in exactly one of four states, PASS / FAIL / NEGATIVE / PENDING, and is carded with an evidence class (the A-U rubric) and a falsifier. The rules are simple and unforgiving (M1):

- A claim asserted ahead of its ledger row is forbidden. The prose follows the ledger; the ledger never follows the prose.
- Wording is calibrated DOWN to the measured value, never up, including under urgency. The fence gets louder under pressure, not wider.
- Corrections are forward-only: a row is superseded with lineage, never silently edited. A verdict edited in place rather than superseded is itself a violation of the constitution.
- A capability verdict is the confidence-interval bound that excludes the threshold, never the point estimate.
- The ledger is the single source of truth, and where prose and ledger disagree, the ledger wins and the prose is wrong.

The falsifier requirement is the spine of the whole thing. No claim ships without a stated condition that would prove it false. A claim with no falsifier is not a claim; it is marketing, and marketing is forbidden in this work. The violation falsifier for the constitution itself is concrete: a claim asserted ahead of its ledger, wording calibrated UP, or a verdict edited rather than superseded (M1).

## Negatives are content, and the snapshot is a snapshot

The ledger does not hide its losses; it features them. A partial, a negative, a "most pieces do not help" decomposition is a measurement that the design is incomplete, not an exit and not a failure to bury. The negatives are the credibility. The last recorded ledger snapshot reads 882 rows = 350 PASS / 0 FAIL / 183 NEGATIVE / 349 PENDING. That figure must be cited honestly: it is a provenance-flagged ledger snapshot, not a number a reader can reconstruct from the published rows. The ledger derives from a deduplicated merge of 615 extracted claims, the snapshot enumerates 882 rows, and the carded body surfaces only about 140 distinct rows, so a skeptic counting what is printed cannot independently derive 183. The constitution therefore forbids headlining the bare "183 published negatives" as a credibility number until the count is reconstructable; cite the snapshot as a snapshot, and feature only the negatives the ledger body actually enumerates. Calibrating the credibility-of-the-negatives claim down to what is reconstructable is itself an application of the calibrate-down rule.

## DONE is observed-at-runtime, not test-covered, not grep-confirmed

This is the load-bearing fence of the chapter, and it is where most honest-seeming programs quietly cheat. The constitution holds two distinctions hard.

First, DONE = test-covered (Class E/D), not feature-working (Class A). A passing test does not satisfy a criterion that demands a runtime observation. A Class-E test can never satisfy a Class-A criterion. The provenance taxonomy makes the classes explicit (M30): A = live / observed, C = code / static inspection, E = test-passes, F = doc / prior-claim (inheritable, but must be re-verified before it is leaned on). These are not interchangeable tiers; they are a strict ordering of what was actually witnessed.

Second, class authority is ordered, and the ordering is enforced (M9). Class-B (tool state) overrides Class-G (own narrative); Class-A (observed at runtime) overrides Class-E (tests pass). A test passing does not satisfy a criterion that demanded a Class-A deployment-time check; where sources conflict, the row is marked `[CONFLICT:unresolved]` and resolved with a direct read, narrative never trusted over the tool. The travelling negative that must be cited beside this rule is its concrete failure mode (M9): a criterion marked satisfied by a Class-E test where Class-A was demanded, or narrative trusted over the tool, is exactly the failure the ordering exists to prevent.

The third leg is verification discipline (M26): believe the user over the folder name and verify empirically. Check `git remote` and `git log` against the live deployment before editing or deploying; walk every page of the live site with a real crawler rather than grepping the repo and assuming, because grep-and-assume has hidden de-indexed robots files, dead forms, an un-started cutover, and a stale-DNS "outage." The one-line rule that travels with M26 is the whole point: DONE = observed-at-runtime, not grep-confirmed. Its falsifier is plain: M26's own absence produced the false-confidence failures it cures. This chapter is authored under that rule. The ledger figures below were read out of the ledger; they were not grep-confirmed from a summary, and they are not observed-at-runtime claims about the system, only recorded method facts.

## What is NOT claimed in mu1 - The Evidence Constitution and ledger discipline

- Ceiling: that "the program has a rigorous evidence constitution" implies "the program's scientific claims are therefore proven" is NOT shown. The most we claim is that M1, M9, M30, and M26 are proven, reusable, method-class governance patterns. They establish how a claim must be earned and how it may move; they earn no capability themselves and certify no rung. Method is a ceiling, not a springboard.
- Fences engaged: red line 7 (never raise a claim above its source evidence class) is the chapter's whole subject. Red line 9 / the SIGNED park wording (a frontier negative is a ledger-scoped exhausted search envelope, never "K>=3 exhausted" or "Sec-0.6(B) achieved") is the calibrate-down rule applied to parks. The DONE = observed-at-runtime fence (Class E never satisfies Class A) is engaged directly. The provenance fence on the 183-negative snapshot (cite as a snapshot, not a re-countable headline) is engaged. No-PII and no-secrets (red line 10) apply: the digests carry redacted client handles and a Clerk test key that are never reproduced.
- Negatives that travel with this claim (cite alongside, never strip): the M9 failure mode (a Class-E test marked as satisfying a Class-A criterion; narrative trusted over the tool) travels beside the class-authority rule. The provenance flag on the 882-row snapshot (the 183 NEGATIVE count is not re-derivable from the carded rows) travels beside any mention of "negatives are content." The N-LEAK and N-NOOP method negatives (a wrong-repo deploy driven by a HANDOFF doc treated as a command; SKILL files that silently no-op'd for months while phases "completed") are the canonical runtime failures M26 and the DONE-not-grep rule exist to prevent, and are cited as the constitution's own scar tissue, not hidden.
- Parked / owed: nothing in this chapter is parked, because nothing here is a frontier result; the constitution is method-class and fully earned. What it owes the rest of the encyclopedia is enforcement: every chapter that cites a PASS owes its travelling NEGATIVE in the same passage, and a Class-A observation owed by another chapter (for example continuity Stage-2 mind-tick, or a live behavioral motor tally) stays owed until observed, never discharged by a test.
- One-line honest summary a skeptic could not dispute: this chapter proves only that the program has a strict, falsifier-bearing, append-only, calibrate-down, observe-at-runtime evidence discipline, and that discipline by itself proves no scientific capability whatsoever.

## Falsify this

The lead falsifier, stated operably: exhibit one published claim in this corpus asserted ahead of its ledger row, or one verdict calibrated UP rather than DOWN to its measured value, or one verdict edited in place rather than superseded with lineage, or one criterion marked satisfied by a Class-E test where the criterion demanded a Class-A runtime observation. Any single one of those falsifies the claim that this program runs under the Evidence Constitution. The constitution is only as real as its weakest enforced row.

## Sources

- `curated/uni-gpt-digest.md` (the constitution as the program's reusable asset: A-U classes, the four-state append-only ledger, the calibrate-down and exactness-honesty rules, the 882-row snapshot provenance).
- `curated/ideation-explorer-digest.md` (the DD-TDD evidence contract and the A-F provenance taxonomy with per-DONE-criterion `Y:`/`N:` verdicts; the brutal-honesty audit separating "exists in code" from "observed at runtime").
- `encyclopedia/CLAIM-LEDGER.md` rows M1 (the Evidence Constitution), M9 (class-authority ordering), M30 (A-F provenance taxonomy), M26 (DONE = observed-at-runtime, not grep-confirmed); the METHOD negatives N-LEAK and N-NOOP; Constitution Section 0 and front matter FM-1 through FM-4.
- Archive pointers (local, PII-bearing, never reproduced): the UNI-GPT research-ledger archive and the SolutionWright Ideation-Explorer engagement-portal archive, reconciled through `curated/00-INDEX.md`.
