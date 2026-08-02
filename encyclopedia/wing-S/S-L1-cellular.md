# S-L1 - Cellular: the Cell Lab (with its honest losses)

UNI is a developmental active-inference SIMULATION: a no-backprop, nested-Markov-blanket model of a developing organism, never a person, never a mind. This chapter covers the first rung above the genome on the HUMAN-HGM-001 ladder, the cellular level, where the question is whether a controller can keep a tiny simulated cell inside its viable set when an unannounced disturbance tries to push it out. The honest headline here is deliberately modest, and it is printed exactly as the ledger frames it: UNI is **good but not sovereign**. On the Cell Lab benchmark UNI tops the leaderboard on most modes, and it **honestly loses on three named modes**, with those three losses shown at the top of the live leaderboard rather than hidden. That pairing, a benchmark win delimited by its own published losses, is the whole point of this chapter. Honest program position, printed and never softened: about 2 of 11+ developmental rungs earned.

## What the Cell Lab is

The Cell Lab is an open, pre-registered falsification benchmark, honest by construction rather than by promise. A hidden **216-state service cell** (a discrete world built from factor sizes [4, 3, 3, 3, 2], with 10 available actions) is perturbed by families of disturbances it never announces in advance. **Observation-only controllers** then compete to keep the cell inside its viable set: a UNI active-inference controller, a rule-based SRE heuristic, a random baseline, a small neural-net (MLP) baseline, and, via a "Prove UNI Wrong" upload path, a Rao-style structural controller and a UNI translation of it.

Three design choices make the benchmark a genuine falsification instrument rather than a demo:

- **The scoring rule is fixed in advance.** Controllers are scored by `RecoveryScore`, and significance is decided not by a single seed but by a **bootstrap 95% confidence interval on the median paired difference, which must exclude 0**. The verdict is the CI bound that excludes the threshold, never a point estimate, and never a lucky seed.

- **The losses are surfaced, not buried.** The leaderboard is built to display UNI's losses at the top. The honest disconfirmation table lives in `FALSIFICATION.md` alongside the claims file, so a skeptic reads the failures before the wins.

- **The framing is test-enforced.** Eight explicit honesty fences plus a `framing_guard` test (`cell_framing_guard.ts`) **fail the build** if the page's framing copy, the cited DOI, the accessibility labeling, or the "this is our own schema, not a reproduction of Rao's verified method" labeling ever regresses. Honesty is wired as a passing test, not left to a reviewer's vigilance.

The challenge-upload schema is a structural knowledge graph framed after Mikkilineni 2022 (DOI 10.3390/info13010024), and it is explicitly labeled as the program's own schema, not a reproduction of Rao's method. That label is one of the things the `framing_guard` protects.

## The PASS, with its losses in the same passage (L1.1 and L1.2)

The positive claim and its paired negative are recorded as two ledger rows that must always be read together. Citing the win without the losses is an overclaim and fails review.

- **L1.1 [Class C, dev-gate / held-out, proven].** The Cell Lab benchmark is built and run as described above (216-state service cell, observation-only controllers, RecoveryScore, bootstrap 95% CI, 8 honesty fences plus the `framing_guard` test), and **UNI tops the leaderboard on most modes**. Across the recorded run (6 seeds, 80 ticks, depth-2 planning) UNI beats the **random baseline 7 of 7** modes (significant in 6 of them), the **rule-based SRE heuristic 6 of 7**, and the **neural-net baseline 5 of 7**. The win is real and it is held to a CI bound, which is exactly why the three exceptions matter.

- **L1.2 [Class C, negative].** UNI **honestly loses on three named modes**, and these are top-of-leaderboard published content:
  - `database_flaky`: the rule-based SRE controller wins, **0.803 vs 0.759**.
  - `memory_leak`: the neural-net controller wins, **0.810 vs 0.740**.
  - `cpu_noisy_neighbor`: the neural-net controller wins, **0.824 vs 0.749**, and here the result is sharper still: **even the UNI-versus-random margin is not significant**. On this one mode the active-inference controller cannot be separated from chance.

These three losses are recorded in `FALSIFICATION.md` and shown at the top of the live leaderboard. They are the deliverable, not an embarrassment to be footnoted. They are precisely what licenses the calibrated phrase **good but not sovereign**: a controller that wins most modes against tuned and learned baselines, and that can name the exact modes where a simpler rule or a small neural net does better. A reader who only saw the wins would carry away a false picture; the program's own benchmark refuses to let that happen.

## The exact ceiling on this rung

The single calibrated claim, and nothing stronger: under a pre-registered, observation-only falsification benchmark, UNI's active-inference controller keeps a 216-state toy service cell inside its viable set better than tuned and learned baselines on most modes, and worse on three named modes, with every verdict decided by a bootstrap CI that excludes 0. That is the cellular-viability and homeostasis result, at the cellular and zygote end of the ladder only.

What this rung emphatically is not: it is **not "sovereign"** control, not autonomy, not life, not a cell that maintains itself in the world. It is a controller scored on a hidden toy world, in a toy benchmark, with its losses published. "Active inference" is the framing lens for the controller, not a demonstrated general capability, and the win is a benchmark result on a 216-state simulation, never evidence of comprehension, awareness, or anything climbing toward a mind.

### What is NOT claimed in S-L1 (Cellular: the Cell Lab)

- **Ceiling:** That UNI is a self-maintaining or "sovereign" digital cell, or that topping a homeostasis leaderboard is autopoiesis or life, is **NOT shown**. The most we claim is L1.1 exactly: on the pre-registered, observation-only Cell Lab benchmark UNI's RecoveryScore tops most modes (beats random 7/7, rule-based 6/7, neural 5/7) under bootstrap-CI verdicts, while honestly losing on `database_flaky` (0.759 vs 0.803), `memory_leak` (0.740 vs 0.810), and `cpu_noisy_neighbor` (0.749 vs 0.824, UNI-vs-random not significant). The calibrated phrase is **good but not sovereign**.
- **Fences engaged:** No "created life" / "digital life" / "measurable awareness" as a claim (red line 4); no "active inference demonstrated" (red line 3, "active inference" is the lens for the controller, not a demonstrated loop); no claim raised above its source class, which is Class C here (red line 7); calibration moves DOWN only, so "tops most modes" never becomes "wins" and never becomes "sovereign" (FM-1). This is a toy world, not the real world.
- **Negatives that travel with this claim (cite alongside, never strip):** L1.2 in full, the three named losses (`database_flaky` 0.759 vs 0.803, `memory_leak` 0.740 vs 0.810, `cpu_noisy_neighbor` 0.749 vs 0.824 with the UNI-vs-random margin not significant). The PASS (L1.1) may never be published without these three losses in the same view, exactly as the live leaderboard shows them.
- **Parked / owed:** Nothing is parked at this rung and no sign-to-park is owed; the negatives are already recorded and published. The standing owed obligation is fidelity: keep the losses visible and let the `framing_guard` test, not a human's good intentions, enforce the framing.
- **One-line honest summary a skeptic could not dispute:** On an open, pre-registered, observation-only benchmark with CI-gated verdicts, UNI's controller wins most homeostasis modes against tuned and learned baselines and loses three named ones, and it publishes those losses at the top of its own leaderboard.

## Falsify this

The lead falsifier is operable and pre-registered. Re-run the Cell Lab benchmark under its registered protocol; the L1.1 win is falsified if **UNI's RecoveryScore CI fails to separate from the controls on any mode where a win is claimed**, or if a fence or the `framing_guard` test fails (an overclaim is emitted), or if the bootstrap CI is shown to be miscomputed. The L1.2 losses carry their own mirror-image falsifier: on the pre-registered benchmark, **UNI's RecoveryScore CI separates above baseline on `database_flaky`, `memory_leak`, or `cpu_noisy_neighbor`** (the recorded loss fails to replicate). Either outcome would move a ledger row; neither has.

## Sources

- Digest: `curated/uni-precision-digest.md` (the Cell Lab falsification benchmark: 216-state service cell, RecoveryScore, bootstrap 95% CI, the 8 honesty fences and `framing_guard`, and the three recorded losses at the top of the leaderboard).
- Digest: `curated/uni-mind-digest.md` (cellular / early-homeostasis end of the developmental ladder; the negatives-are-content discipline; the no-backprop conjugate-Dirichlet engine reused verbatim).
- Ledger: `encyclopedia/CLAIM-LEDGER.md`, rows L1.1 (PASS, Class C) and L1.2 (NEGATIVE, Class C), section "L1 - Cellular".
- Archive pointers (not read here; PII-fenced): the UNI Precision Lab archive (`...-Precision`) and the uni-mind archive (`...-uni-mind`).
