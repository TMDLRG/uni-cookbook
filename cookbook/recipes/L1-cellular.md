# L1 — Cellular / autopoietic viability & homeostasis

> **What you are building.** A 216-state "service cell" that the same no-backprop
> active-inference engine must keep alive inside a viable set against disturbances it
> never announces — an *open, pre-registered falsification benchmark* whose published
> losses are the credibility, not a hidden failure. A developmental SIMULATION of
> autopoietic homeostasis, never a living cell and never a person.

This is the second-earned rung (~2 of 11+). It re-reads autopoiesis as homeostatic
prediction-error control: a cell stays a cell by predicting the consequences of its own
acts and correcting drift before the viability edge is crossed. Same engine as L0, one
scale up.

---

## Ingredients

Pantry engines this recipe calls by name:

- **The Cell Lab** (precision labs): the open pre-registered falsification benchmark — a
  hidden 216-state service cell (factor sizes `[4,3,3,3,2]`, 10 actions), **observation-only
  controllers**, `RecoveryScore`, a bootstrap 95% CI gate, **8 honesty fences** + a
  `framing_guard` build test, plus `CLAIMS.md` and `FALSIFICATION.md`.
- **The JAX POMDP + EFE + Dirichlet engine** (`core.py`, uni-mind): supplies the cell's
  discrete POMDP loop (`active_inference_step`, exact posterior, EFE/policy selection;
  conjugate-Dirichlet `counts + lr*sufficient_stat`, AST no-backprop guard).
- **Method constitution:** M2 (bars-before-build, held-once), M7 (contains-baseline +
  load-bearing discriminator), M15 (honesty-fence-as-the-pitch), M9 (class authority).
- **The inline-engine + canonical-TS + parity-test triad:** the vanilla-JS engine inside
  `cell-lab.html`, mirrored by `service_cell.ts` in `api/_lib/worlds/`, pinned by a
  `*_parity.ts` test so the page cannot lie about its math. Determinism via a Mulberry32
  seeded PRNG + a committed `cell-bench-cache.json`.

---

## Method

1. **Build the hidden world.** Stand up the 216-state service cell and the disturbance
   *families* (e.g. `database_flaky`, `memory_leak`, `cpu_noisy_neighbor`) — the cell never
   announces which family is acting. Define the viable set; falling outside it is the thing
   recovery must prevent.
2. **Make every controller observation-only.** UNI active inference, a rule-based SRE
   heuristic, a random control, and a small neural-net (MLP) baseline all see *only*
   observations — no privileged read of the hidden 216-state truth. This is the M7 tuned-
   baseline requirement: UNI must beat *strong* controls, not strawmen.
3. **Pre-register the gate (M2).** Register `RecoveryScore` and the significance rule:
   a **bootstrap 95% CI on the median paired difference that must exclude 0** — seeded PRNG,
   committed result cache, **never one seed**. Seal before scoring. The verdict is the CI
   bound, never the point estimate.
4. **Wire honesty as a test.** Install the 8 honesty fences + the `cell_framing_guard.ts`
   test that **fails the build** if the page's framing copy, the Zenodo DOI caveat,
   accessibility, or the "this is our own schema, NOT a reproduction of Rao's verified
   method" labeling regresses. A claim linter over status comments auto-downgrades any
   overclaim (the general M8 discipline: a status linter is meant to catch an inflated
   "PROVEN" and force it to the held class — a method note, not a recorded Cell-Lab event).
5. **Run the tournament.** UNI vs rule-based, neural, and random across all failure modes.
   Pin the page engine to `service_cell.ts` with the parity test.
6. **Put the losses at the top of the live leaderboard** (M15). The board surfaces UNI's
   defeats first; disconfirmations are the deliverable, not theatre.

---

## Gate (exact ledger figures — L1.1)

UNI tops the leaderboard on **most** modes, with the win measured the only honest way:
`RecoveryScore`'s bootstrap 95% CI on the median paired difference **separates from the
control where a win is claimed** (CI excludes 0), the `framing_guard` passes (no overclaim
is emitted), and the bootstrap CI is correctly computed. Significance = a bootstrap 95% CI
excluding 0, never a point estimate. (The ledger records the outcome at this grain only —
"UNI tops the leaderboard on most modes"; no per-control win-counts are claimed here.)

Evidence class: **C** (dev-gate / held-out eval).

---

## Falsifier (operable)

The L1 PASS falls if, on the pre-registered benchmark, **any one** of these holds:

- `RecoveryScore`'s CI fails to separate from the controls on a mode where a win is claimed; OR
- a fence / the `framing_guard` test fails (an overclaim is emitted); OR
- the bootstrap CI is shown to be miscomputed.

Companion falsifier for the recorded negative (L1.2): if UNI's `RecoveryScore` CI later
separates *above* baseline on the three lost modes, the recorded loss did not replicate.

---

## Recorded NEGATIVE (first-class, inline — L1.2)

UNI **honestly LOSES** on three modes, recorded in `FALSIFICATION.md` and shown at the
**top of the live leaderboard**:

| Failure mode | Winner | UNI score |
|---|---|---|
| `database_flaky` | rule-based SRE (0.803) | 0.759 |
| `memory_leak` | neural (0.810) | 0.740 |
| `cpu_noisy_neighbor` | neural (0.824) | 0.749 — *UNI-vs-random not even significant here* |

Class **C**. These are not bugs to fix before publication; they are the published content.
On `cpu_noisy_neighbor` UNI does not even clear the random control significantly — and that
fact is printed first, not buried.

---

## HONEST FENCE — **proven** (Class C, with honest losses)

A held, pre-registered, bootstrap-CI-gated benchmark exists and is signed PASS on most
modes, with its falsifier still live and its three defeats published at the top of the
leaderboard. **Not "sovereign" — "good but not sovereign."** Active inference is one
capable controller among several, beaten cleanly on three named modes by a tuned heuristic
and a neural baseline; those losses are top-of-leaderboard content.

**Not claimed at L1:** not a living cell, not "created life", not awareness, not
comprehension, not a general-purpose controller, not AGI. This is the cellular / zygote end
of the developmental ladder only. The Cell Lab models *autopoiesis as homeostatic
prediction-error control in a toy world*, never the real world; the Zenodo preprint
(Polzin et al. 2026, DOI 10.5281/zenodo.19785799, MIT) behind the math stays fenced as an
**unrefereed** mathematical foundation (Layer-1 AI-executable audit complete; Layer-2 human
expert review PENDING). Honest program position: **~2 of 11+ developmental rungs earned.**
Where this recipe and the ledger disagree, the ledger wins.
