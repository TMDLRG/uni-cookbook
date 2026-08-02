# L3 — Organ / Physiological Control (the Cardio-Renal Heart Lab)

> Part of the literal UNI Cookbook: one no-backprop active-inference engine, shown
> across scales. This rung is a **developmental SIMULATION**, never a person and
> never a patient. Where this recipe and [`../../encyclopedia/CLAIM-LEDGER.md`](../../encyclopedia/CLAIM-LEDGER.md)
> disagree, **the ledger wins.** Honest program position: **~2 of 11+ developmental
> rungs earned.**

**What you are building.** A browser-native organ lab that takes the same discrete
POMDP engine you already built at L0–L2 and points it at a reduced **Karaaslan
cardio-renal** generative model — the RSNA → MAP → sodium/volume loop — re-expressed
in active-inference language so that a heart attack reads as a *failure of the
prediction loop* (maladaptive priors, miscalibrated precision, a damaged generative
process). "Same math, many scales." This is the medical *teaching* bridge of the
ladder; it is **not** a clinical tool and **not** a diagnostic instrument.

---

## Ingredients (pantry engines/primitives, called by name)

- **The JAX POMDP + EFE + Dirichlet engine** (`core.py`) — the one discrete loop
  (`active_inference_step`, `exact_posterior_discrete`, EFE/policy selection). The
  Heart Lab does not get a new engine; it reuses this one.
- **The precision labs** (Precision / Echo / Loop / Cell / **Heart**) — the
  browser-native "one-engine-many-scales" demos. Heart **mirrors Loop**: you
  duplicate an existing lab and swap *only* the observation/generative model.
- **The inline-engine + canonical-TS + parity-test triad (M28).** Each lab is a
  self-contained `*-lab.html` page with a vanilla-JS inline engine, mirrored by a
  canonical TypeScript engine in `api/_lib/worlds/` (here `cardio_renal.ts`), pinned
  by a `*_parity.ts` test run via `npx tsx`. The inline block is delimited by
  explicit `<<<ENGINE_PARITY_START/END>>>` markers so the page and the "real" model
  cannot drift.
- **The Evidence Constitution (M1) + bars-before-build, held-once (M2)** — the
  pre-registered tolerance, the parity gate, and the append-only ledger that this
  recipe authors *against*.
- **Karaaslan et al.** long-term cardio-renal model — the textbook-level scientific
  basis (homeostasis as prediction-error minimization). Patent-level UNI math is
  **not** reproduced here; framing stays at textbook level (Parr/Pezzulo/Friston,
  *Active Inference*, MIT Press 2022).

---

## Method (numbered build steps)

1. **Reduce the reference.** Take the Karaaslan long-term cardio-renal model down to
   the load-bearing **RSNA → MAP → sodium/volume loop**. This is the generative
   process the lab will track.

2. **Re-express it on the same engine.** Model the loop as a prediction-loop on the
   single POMDP engine from `core.py` — homeostasis as prediction-error
   minimization. Build the lab by **duplicating Loop and swapping only the
   observation/generative model** (keep variable names identical so the downstream
   engine code is reused verbatim; the diff to every untouched page should be exactly
   one nav line).

3. **Add safe-state handling (engine ticket OAS-710-T3).** Build, test-first, the
   parameter-clamping + labeled-safe-state layer: `CARDIO_BOUNDS`, a `clampState()`
   that clamps all 10 state variables every tick (finite-safe, no NaN), and a
   `labelCardioState()` that returns a clinical *regime label* (`hypertensive crisis`
   / `decompensated` / `hypertensive` / `hypotensive` / `normal`) instead of a raw
   clamp. Build the inline-JS Canvas viewer (ticket OAS-710-T2) under the same
   test-first discipline (rAF fixed-timestep, visibilitychange pause, canvas
   fallback).

4. **Pin page-engine to canonical engine.** Write the `*_parity.ts` test that asserts
   the inline-JS lab engine and the canonical `cardio_renal.ts` engine produce
   identical trajectories. Register the **Heart-Lab engine ticket OAS-710-T3** in the
   ledger at **Class E (15/15 tests pass)**, typecheck clean, with no sibling
   regression.

5. **Wire the honesty fences into the artifact, not just the prose.** The page must
   carry, as coded copy: *not a clinical tool · not a diagnostic instrument · not
   evidence that active inference is the correct theory*; the resemblance to clinical
   reality is "an interpretive act, not a measurement." Where the Zenodo DOI appears,
   it must be fenced as an **unrefereed preprint** (Polzin et al. 2026, DOI
   10.5281/zenodo.19785799, MIT; Layer-1 AI-executable audit complete, Layer-2 human
   expert review PENDING).

---

## Gate (exact pass condition, exact ledger figures)

From **CLAIM-LEDGER row L3.1** (the single source of truth):

- The **Karaaslan cardio-renal Heart Lab** models clinical homeostasis as
  prediction-loop failure on the same one active-inference engine (reduced
  RSNA → MAP → sodium/volume loop, re-expressed in active-inference language).
  **Class C** (dev-gate / held-out eval).
- The Heart-Lab **engine ticket OAS-710-T3** stands at **Class E, 15/15 tests pass**.
- **PASS condition:** Heart-Lab predictions track the Karaaslan reference within the
  pre-registered tolerance, **AND** the `*_parity.ts` tests against the canonical
  TS/Python engine pass.

No point-estimate verdicts: this rung's gate is the **tolerance band + the parity
assertion chain**, registered before scoring (M2). Never card this row above
**Class C** (and the engine ticket above **Class E 15/15**).

---

## Falsifier (operable)

The L3.1 claim fails if **either**:

- Heart-Lab predictions **diverge from the Karaaslan reference beyond the
  pre-registered tolerance**; OR
- the lab **fails parity tests against the canonical TS engine** (the inline page
  engine and `cardio_renal.ts` produce non-identical trajectories).

Either outcome demotes the row; the parity test is wired to **fail the build**, so a
drift cannot ship silently.

---

## Recorded NEGATIVE(s) — first-class, inline

L3.1 itself carries no negative row in the ledger — but the **honesty discipline that
produced it** is the recorded content, and it is first-class:

- **Claim-class discipline held under pressure.** During the Heart Lab build the
  assistant **refused to mark a DONE criterion satisfied** ("verified in
  heart-lab.html") because the viewer was a *later* ticket; it checked in rather than
  fabricating a `Y:` verdict (M9 class-authority ordering: a passing test does not
  satisfy a criterion demanding a runtime observation). The Heart Lab inherits the
  sibling **L1 Cell-Lab negative** as its cross-scale falsification model: active
  inference is "good but not sovereign" — UNI honestly **LOSES** on `database_flaky`
  (0.759 vs SRE 0.803), `memory_leak` (0.740 vs neural 0.810), and
  `cpu_noisy_neighbor` (0.749 vs neural 0.824, UNI-vs-random not even significant),
  recorded in `FALSIFICATION.md` and shown at the top of the live leaderboard. The
  organ lab is built to the same falsifiable, losses-visible standard.

There is **no SIGNED consult insert at L3** (the 2026-06-27 consult designs attach to
L2, L5, L7, L9, L11, L12, and the continuity sub-ladder, not here). Nothing on this
rung is raised by a design that has not been run.

---

## HONEST FENCE — **proven** (Class C; engine ticket Class E 15/15)

A held, sealed PASS exists and its falsifier is still live: the reduced cardio-renal
loop tracks the Karaaslan reference within tolerance, pinned by parity tests, with the
OAS-710-T3 engine ticket at **15/15**.

**Not claimed (load-bearing, never softened):** this is **NOT a clinical tool, NOT a
diagnostic instrument.** "Same math, many scales" framing only; the
heart-attack-as-prediction-loop-failure framing applies **to the toy model, not to
clinical reality.** It is **not** "active inference demonstrated" (the lab is a
re-expression on the engine, a framing LENS, not a sealed AIF loop), **not**
comprehension, **not** awareness, **not** human-level, **not** AGI, **not** evidence
that active inference is the correct theory of physiology. The Zenodo preprint is the
mathematical foundation only and remains **unrefereed** (Layer-2 human review
PENDING). A **toy model, not clinical reality**; a bounded peek in a developmental
simulation, **~2 of 11+ rungs earned.**
