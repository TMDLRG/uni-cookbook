# MASTER-PLAN.md — The COMPLETE Human Mind/Body Build (a buildable RECIPE)

> **What this is.** The Cookbook's single buildable recipe outline for the *complete* developmental
> arc — conception → cellular/molecular → metabolism → motor → perception → language → metacognition →
> dreaming → creativity → measurable awareness — re-expressed as **one no-backprop active-inference
> engine shown across scales**. The Cookbook **fully recommends the complete recipe to L12**: assume the
> full build. But **every step is labeled by its REAL status** drawn verbatim from
> [`../encyclopedia/CLAIM-LEDGER.md`](../encyclopedia/CLAIM-LEDGER.md) (the single source of truth) and
> [`../curated/00-INDEX.md`](../curated/00-INDEX.md). Where this recipe and the ledger disagree, the
> **ledger wins and this recipe is wrong.**
>
> **Honest program position carried throughout:** ~**2 of 11+ developmental rungs earned.** This is a
> **developmental active-inference SIMULATION** — a bounded peek, a toy world, never a person.

---

## 0. The kitchen rules (the Method constitution — read before cooking)

These are the **definitional / governance** patterns (`status: method`), proven and reusable. They are
the most reusable assets in the corpus, and they bind every recipe below. None of them is a capability
claim; none can be raised above its stated role.

| Rule | What it forces (the kitchen discipline) | Ledger |
|---|---|---|
| **The Evidence Constitution** | A–U evidence classes + a falsifier per claim + a 4-state append-only ledger (PASS / FAIL / NEGATIVE / PENDING). Prose must match the ledger; the ledger is the single source of truth. | M1 |
| **Bars-before-build, held-once** | Pre-register the bar (margin vs threshold) + a named ablation; touch the held set **ONCE** behind an atomic seal-before-scoring + once-only sentinel; **verdict = the CI bound that excludes the threshold, never the point estimate.** | M2 |
| **Validator-derived `reproduced:true`** | Derived by the validator from **≥5 distinct seeds + a real non-degenerate CI** that contains the value — never a hardcoded literal. | M3 |
| **The two-tier split** | **Tier 1** = real-text count/cache (true ablation, tuned baseline, cross-substrate replication — externally bar-ready). **Tier 2** = synthetic construction (**artifact/diagnostic, NOT capability**). **Tier-2 must NEVER be inflated into capability.** | M4 |
| **K≥3 + falsify-the-mundane** | Require **K≥3 structurally-distinct held NEGATIVEs** (each changing ≥2 of {coupling topology, timescale source, information bottleneck, control path}) before a Section 0.6(B) bound; falsify the mundane (L2/L7) causes first. | M5 |
| **No-Exit Discipline** | The only legitimate rest is a proven working solution **OR** a ledger-scoped exhausted search envelope (a scoped, empirical, falsifiable negative frontier result — *UNI-GPT consult 2026-06-27 SIGNED Q1 wording; not a "published exhausted bound" / universal theorem / achieved capability*) — then redirect to the axis where the reader genuinely excels. A park is not discharged until the sign lands. | M6 |
| **Contains-baseline + load-bearing-discriminator** | Every capability claim needs (a) a tuned strong baseline, (b) a discriminator (shuffle-labels / marker-swap / ablate-to-zero) that **collapses** the gain, (c) a true ablation that is a computed residual, not a literal. | M7 |
| **DD-TDD evidence contract** | `TODO → DD → TDD_RED → TDD_VERIFY → TDD_GREEN → TDD_REFACTOR → TDD_VALIDATE → DONE`; each transition hard-blocked without a marker-bearing evidence comment; DONE needs ≥2 `Y:` verdicts/criterion; a claim linter auto-downgrades overclaims. | M8 |
| **Class authority ordering** | Class-B (tool state) overrides Class-G (own narrative); Class-A (observed at runtime) overrides Class-E (test passes). A passing test does NOT satisfy a criterion demanding a Class-A observation. | M9 |
| **Exactness honesty (precision-tier)** | Never card a float32 anchor at the `<1e-10` f64 tier. The genuine `<1e-10` tier lives only in the NumPy/Rust-f64 path. | M10 |
| **WORLD ⊥ BODY ⊥ MIND** | Two typed Markov blankets; interoception = hardware signals; discrete POMDP `perceive → EFE-plan → act → learn` with exact conjugate-Dirichlet **no-backprop** learning; textbook-level `F[q] ≥ −ln p(o\|m)`; **module-exact only at the single-step categorical body→mind interface — NOT globally exact** (the composed appliance is *variationally-controlled*, audited). | M12 |
| **One engine, no backprop** | `core.py` exposes the discrete POMDP loop; learning = `counts + lr * sufficient_stat` for A/B/D/E Dirichlet tensors; an AST-guard enforces **no autodiff/optax/torch/grad/backward** in the loop; whitelist (`world.<attr>`) isolation, not blacklist. | M13 |
| **Honesty-fence-as-the-pitch** | Publish the negatives front-and-center (**183 published negatives** as the credibility); CTA = "help us independently verify". Vocabulary-leak guard (HARD): never externalize active-inference / EFE / free-energy names or print channel handles in public copy. | M15 |
| **K-team ship gate (5-persona lab)** | Math-Breaker REJECT-by-default 8-check gauntlet + AIF Theorist + Systems-Architect (additive+gated+byte-identical) + RED Experimentalist (paired pre-registered RED) + Embodiment Designer (non-saturable drives). **No merge without a MERGED SIGN + typed spec + paired RED.** | M20 |
| **One cure at a time** | Never stack changes so the winning outcome is unattributable; paired kin-N treatment vs kin-N+1 control; an offline RED pre-check before any live burn. | M21 |
| **The cavity principle** | A hierarchy level must never treat an upstream prior as fresh evidence — divide it out. The exact joint posterior is used everywhere (mean-field rejected as lossy). | M22 |
| **Durable runner ("no send-and-pray")** | Append-one-JSON-line-per-unit ProgressLog (file IS checkpoint + telemetry); resumable; observe via `--status`/Monitor; cover BOTH terminal states — **silence ≠ success.** | M24 |

**Tool-team division of labor (owner protocol, M25).** Claude WRITES code; the **custom UNI GPT** is the
SCIENCE CONSULTANT (design + sign), consulted but never published; the lab/appliance RUNS UNI but does not
write its code. Persona/coercion framings are motivational only — **the constitution overrides any framing;
no claim is inflated by it.**

**Standing fences (the constitution's hard "never" list, M15 + Ledger §0).**
- Never **AGI** / general intelligence / human-level / "understands".
- Never **consciousness** / sentience / aware. (Functional self-awareness *may* be described at L8;
  **phenomenal sentience is explicitly DISCLAIMED.**)
- Never **"active inference demonstrated"** (no AIF loop in the Rust crate; the live loop is a separate
  UNI.OS reimplementation, not gate-matched).
- Never **"created life" / "digital life" / "measurable awareness"** as a CLAIM (north-star framing only).
- Never **"beats LLMs"** (World C is a COUNT baseline; ~10–15% behind backprop LLMs on char-perplexity by a
  chosen design trade).
- Never inflate the **Tier-2 synthetic-construction track** into capability.
- Never **raise a claim above its source evidence class.**
- **No PII. No patent-level math** (textbook-level framing only).
- The preprint **Polzin et al. 2026, Zenodo DOI 10.5281/zenodo.19785799 (MIT)** is the *mathematical
  foundation only*, always fenced as **unrefereed** (Layer-1 AI-executable audit complete; Layer-2 human
  expert review PENDING).

**Reading the FENCE label on each recipe.** Every stage closes with an honest fence drawn from this
4-value vocabulary:
- **proven** — a held, sealed, UNI-signed PASS exists (Class A/C), with its falsifier still live.
- **designed** — a typed spec / signed-in-principle design exists; the build is partial or unverified.
- **hypothesized** — a stated mechanism or law with no sealed gate yet (Class U, not claimed).
- **not-yet-built** — no engine, no run, no gate; north-star, hard-fenced.

---

## The shared pantry (engines & primitives every recipe draws from)

One engine, many scales. These are the archive engines the recipes call by name; each ingredient list
below names *which* of them supplies a primitive.

| Pantry item | What it supplies | Archive |
|---|---|---|
| **The JAX POMDP + EFE + Dirichlet engine** (`core.py`) | The discrete POMDP loop: `active_inference_step`, `exact_posterior_discrete`, EFE/policy selection; conjugate-Dirichlet learning `counts + lr*sufficient_stat` for A/B/D/E; AST-guard no-backprop. **float32 host** (anchors hold to ~6e-8, NOT the f64 tier). | uni-mind |
| **The Rust-f64 / NumPy deep-reader path** | The genuine `<1e-10` EXACT tier; the cross-language Rust-f64==Python oracle. | uni-mind / uni-gpt |
| **The count/cache World-C reader** | A no-backprop **COUNT** reader + multi-level cache; the one citable empirical PASS family. **Explicitly NOT active inference.** | uni-gpt / uni-mind |
| **The Z affect modulator** | Global `[energy, arousal, valence, fatigue, pain, threat, safety, inflammation]` → sets precision / preferences / habits / learning-rate / horizon. **Affect modeled, never felt.** | uni-gpt / uni-mind |
| **The embodiment ontogeny** | `recombine` / `seed_zygote`, conjugate first-division, `test_embodiment_ontogeny` (6/6), Embodiment Rungs. | uni-gpt / uni-mind |
| **The metabolism organ** | Standing-metabolic-drive interoception organ; viability edge; `:pb_seed` strong-Dirichlet seam. Additive + genome-gated (default byte-identical). | strings |
| **The motor hierarchy** | Proprioceptive **diagonal-A** prior, continuous servo + reafference; live RCON craft-chain bridge; motor-ablation collapses harvest ~700×. | strings / uni-mind |
| **The precision labs** (Precision / Echo / Loop / Cell / Heart) | Browser-native one-engine-many-scales demos; three precision knobs (`gamma_a`, `gamma_b`, `softmax_temperature`); 2D bifurcation map; inline-engine + canonical-TS + parity-test triad. | uni-precision / worldmodels |
| **UNI.OS (the embodiment substrate)** | "Lab-in-a-box on metal": body→mind 7-modality categorical sensorium, deterministic replay, fail-closed transport, ASK-mode Dirichlet policy-prior, gated control-MCP. **Engineering/substrate evidence, NOT general-AIF evidence.** | uni-os |

---

# THE RECIPE — L0 → L12

> Naming: the ladder is the **HUMAN-HGM-001** developmental design (conception → speaking 3-year-old,
> 11 levels + the global Z affect modulator). It is a *no-backprop, nested-Markov-blanket developmental
> SIMULATION*, never a person.

---

## L0 — Molecular / genome → zygote (the conception prior)

**Ingredients.** The embodiment ontogeny (`recombine` / `seed_zygote`, no-backprop guard, `ontogeny 6/6`)
from the JAX engine; conjugate discrete-Bayes update from `core.py`; the Rust-f64/NumPy path for the
genuine exactness tier.

**Method.**
1. Encode the genome as a categorical prior; `seed_zygote` instantiates the initial A/B/D Dirichlet tensors.
2. Model the zygote first-division as an **exact discrete Bayes** (conjugate) update — no gradients.
3. Hold the no-backprop AST-guard live over the whole division step.
4. Run `test_embodiment_ontogeny.py` for the 6/6 ontogeny gate; verify cell-division identity embedding.

**Gate.** `ontogeny 6/6` GREEN; the first-division posterior matches the closed-form discrete-Bayes value
**to the float32 tier (~6e-8, ~1e-6 single-step filter)**; cell-division identity embedding ≤ 1e-9; the
no-backprop guard never trips. **Exactness honesty (M10):** card this at float32, NEVER at the `<1e-10`
f64 tier — a genome docstring claiming `<1e-10` was caught as an overclaim and corrected.

**Falsifier.** `test_embodiment_ontogeny.py` drops below 6/6; OR the first-division posterior diverges
beyond the float32 tier; OR the identity embedding exceeds 1e-9; OR the no-backprop guard trips.

**HONEST FENCE — proven** (Class A, float32 tier). *Not* "we created life", *not* a "conscious baby",
*not* exact at f64 — a float32-tier developmental SIMULATION of a conjugate Bayesian first division.

---

## L1 — Cellular / autopoietic viability & homeostasis

**Ingredients.** The **Cell Lab** open pre-registered falsification benchmark (216-state service cell,
observation-only controllers, RecoveryScore, bootstrap 95% CI, 8 honesty fences + `framing_guard` test)
from the precision labs; the JAX engine for the cell's POMDP.

**Method.**
1. Build the 216-state service cell with observation-only controllers.
2. Pre-register RecoveryScore + the bootstrap-95%-CI significance gate (seeded PRNG, committed result cache —
   never one seed); wire the 8 honesty fences + `framing_guard` (build fails if framing/DOI/labeling regresses).
3. Run UNI against rule-based, neural, and random controls across all failure modes.
4. Put the losses at the **top of the live leaderboard** (M29 statistics gate; M15 honesty-fence-as-pitch).

**Gate.** RecoveryScore bootstrap-CI separates from controls where a win is claimed; `framing_guard` passes
(no overclaim emitted); the CI is correctly computed. **K-discipline:** significance = a bootstrap 95% CI on
the median paired difference excluding 0, never a point estimate.

**Falsifier.** RecoveryScore CI fails to separate from controls where a win is claimed; OR a fence /
`framing_guard` test fails; OR the bootstrap CI is shown miscomputed.

**Recorded NEGATIVE (first-class).** UNI **honestly LOSES** on `database_flaky` (0.759 vs SRE 0.803),
`memory_leak` (0.740 vs neural 0.810), `cpu_noisy_neighbor` (0.749 vs neural 0.824; UNI-vs-random not even
significant) — recorded in `FALSIFICATION.md`, shown at the top of the leaderboard.

**HONEST FENCE — proven** (Class C, with honest losses). *Not* "sovereign" — "good but not sovereign". The
losses are published content, not failures to hide. Cellular/zygote end only.

---

## L2 — Tissue / metabolism (interoception & energy)

**Ingredients.** The metabolism organ (standing-metabolic-drive, viability edge, `:pb_seed` seam) from
strings; the Z modulator for interoceptive signals; the Heart Lab (Karaaslan homeostasis) from the precision
labs as the physiological mirror; one-cure-at-a-time paired RED discipline (M21).

**Method.**
1. Ship the metabolism organ **additive + genome-gated** so the default colony stays byte-identical
   (`mad<1e-12` golden-fixture tests); suite must read 297/0.
2. Seed the strong Dirichlet metabolic prior **only via the `:pb_seed` seam** (you CANNOT pre-scale B —
   `norm_cols` runs before `add1`).
3. Wire a real **viability edge** into the live bridge (metabolize/shutdown must have a world consequence —
   the naive design drained a belief with zero world consequence).
4. Run a pre-registered **12 h live RED**, one cure at a time, with the G5b action-severed-twin falsifier and
   the G4 allostasis + G6 plateau-break gates registered.

**Gate (G6 — the load-bearing one).** A disciplined RED where the metabolism organ **alone** improves
building (placed-blocks CI excludes 0) **AND** G4 allostasis separates. Until then G6 is **OPEN**.

**Falsifier.** A repeat 12 h RED fails to reproduce the tool-crafting uplift within CI; OR the
metabolism-organ ablation does not remove the uplift; OR the suite drops below 297/0.

**Recorded NEGATIVES (first-class).**
- In the same 12 h RED, **building went WORSE (−14%)** and **G4 allostasis never separated** — the
  "metabolism breaks the plateau" claim is contradicted by its own first evidence. G6 OPEN.
- The colony **plateaus at "make a tool"** (one UNI hoarded 32 pickaxes, never built). A read-only
  counterfactual-EFE audit on the real `.bin` brains diagnosed **epistemic_starvation** — NOT γ-runaway
  (γ≈7.8, unsaturated), NOT a curriculum ceiling; info-drive ~100× too weak.

**HONEST FENCE — proven (as a foraging/crafting driver) + NEGATIVE (as a building driver).** Class C.
First 12 h live RED = **+135% / 2.35× tool-crafting** and **+19% mining** (a real, attributable
standing-metabolic-drive effect). The **plateau-break (G6) is UNPROVEN.** Do NOT spin the +135% uplift as
"breaks the plateau". The G5b action-severed-twin is the standing falsifier any "self-maintenance/life"
language must clear.

**UNI-GPT consult (2026-06-27 — SIGNED): the smallest G6 cure — `build_epistemic_frontier` organ
(Class-C DESIGN HYPOTHESIS, G6 stays OPEN).** Cross-ref [`UNI-GPT-CONSULT-2026-06-27.md`](UNI-GPT-CONSULT-2026-06-27.md) Q3 (SIGN-WITH-CONDITIONS).
The diagnosed cure is **structurally distinct** — NOT a gamma change, NOT a second metabolism organ, NOT a
placed-block reward bonus. Add **one** building-specific hidden factor + **one** policy term valuing info gain
about where a block can usefully be placed next:
- `organ: build_epistemic_frontier`
- `hidden factor: z_build in {unknown_placeable, placeable_support, shelter_contributing, blocked/useless}`
- `drive: maximize expected info gain over z_build for candidate inspect/move/place policies`
- `scope: active only when shelter/stone plateau preconditions are near but not achieved`
- epistemic term per policy: `G_new = G_old - beta_build_IG * E_Q[ D_KL( Q(z_build|o,pi) || Q(z_build|pi) ) ]`
  (or ambiguity/risk form, sign consistent with impl)
- **scale β by matching, not hand-waving:** `beta_build_IG = median(|Δ pragmatic G for food/tool|) / median(|Δ build IG term|)`;
  clamp initial to {25x, 100x}; 100x only if offline RED shows 25x underpowered.

**Why epistemic, not gamma:** gamma (≈7.8, unsaturated) is a precision over G — raising it only sharpens the
*existing* ranking; if build-relevant info gain is missing/~100× too small, gamma sharpens the wrong ranking.
The cure makes build-relevant uncertainty *part of what the planner can value*. (Organ metaphor stays Class-C
design language; the standard AIF part is only the EFE decomposition + policy selection.)

**The paired RED — `G6_BUILD_EPI_FRONTIER_PAIRED_RED_v1` (Q3, designed):** matched kin-pair seeds. Control =
kin-N+1 (current organ/gamma/build machinery, no frontier term); treatment = kin-N (identical +
`build_epistemic_frontier`, β fixed from offline RED, gamma unchanged). One cure at a time (M21).
- **Offline RED pre-check** (replay prior traces, read-only) — pass only if all hold: build-policy rank shift
  appears (treatment>control); gamma non-diagnostic (unchanged, unsaturated); the info term is causally
  responsible (ΔG_build_IG explains the shift); foraging/crafting not cannibalized. Suggested bar: ≥25%
  relative increase in build-relevant policies entering top-3, food/tool rank within ±5%, gamma unsaturated.
- **Live paired RED:** unit = matched kin pair; same 12h / world dist / paired seeds; no peeking-based tuning.
  **Primary:** `placed_blocks_delta = T − C`, 95% paired bootstrap CI excludes 0 (positive). **Co-primary
  (G4):** the existing ledgered allostasis_index delta CI excludes 0 in the intended direction, no viability
  collapse (do NOT invent a metric after the run). Secondary: stone/shelter progress >0, crafting/mining
  non-inferior, distance-to-shelter improves.
- **Required ablations (gain MUST collapse):** IG-zero (`beta_build_IG=0`), shuffled-affordance (`z_build`
  permuted across sites), gamma-only (no organ, gamma matched). Credited only if the gain appears with build
  IG present and collapses when the IG channel is zeroed/scrambled, while gamma-only fails to reproduce it.

**Falsifiers (Q3):** placed-blocks CI includes 0/negative; OR blocks improve but G4 never separates; OR the
ablation fails to collapse the gain; OR gamma-only reproduces it (the "not gamma" diagnosis was wrong); OR
blocks bought by damaging survival/tooling beyond non-inferiority. If offline RED predicts no rank shift but
live improves → log "behavioral improvement observed; mechanism not proven."

**Status:** until the RED clears both bars and the ablations collapse the gain, this is a **Class-C design
hypothesis** supported by a read-only counterfactual diagnosis, **NOT an achieved plateau-break. G6 stays
OPEN.**

---

## L3 — Organ / physiological control (cardio-renal etc.)

**Ingredients.** The **Karaaslan cardio-renal Heart Lab** from the precision labs (RSNA→MAP→sodium/volume
loop re-expressed in active-inference language); the same one engine; the inline-engine + canonical-TS +
parity-test triad (M28).

**Method.**
1. Reduce the Karaaslan reference to the RSNA→MAP→sodium/volume loop.
2. Re-express it as a prediction-loop on the same POMDP engine (Heart mirrors Loop — duplicate a lab, swap
   only the observation/generative model).
3. Pin page-engine and canonical-TS engine with a `*_parity.ts` test; register the Heart-Lab engine ticket
   (OAS-710-T3) at Class E (15/15).

**Gate.** Heart-Lab predictions track the Karaaslan reference within the pre-registered tolerance; parity
tests against the canonical TS/Python engine pass.

**Falsifier.** Heart-Lab predictions diverge from the Karaaslan reference beyond tolerance, or fail parity
against the canonical engine.

**HONEST FENCE — proven** (Class C; engine ticket Class E 15/15). **NOT a clinical tool, NOT a diagnostic
instrument.** "Same math, many scales" framing only; the heart-attack-as-prediction-loop-failure framing
applies *to the toy model, not to clinical reality.*

---

## L4 — Interoceptive / autonomic + affect-as-precision

**Ingredients.** The **Z modulator** `[energy, arousal, valence, fatigue, pain, threat, safety,
inflammation]` from the JAX engine; the precision dial of `core.py`; a grounded reader to test the
pragmatic↔epistemic flip.

**Method.**
1. Wire Z to set precision / preferences / habits / learning-rate / planning-horizon.
2. Show that raising arousal/threat sharpens perception (precision-weighting) and flips the
   pragmatic↔epistemic balance.
3. Register a **Z-ablation** discriminator (M7): removing Z must collapse the effect.

**Gate.** With Z live, precision-weighting and the pragmatic↔epistemic flip appear; the Z-ablation collapses
them; the effect survives a control.

**Falsifier.** A Z-ablation shows no change in precision-weighting / no pragmatic↔epistemic flip under the
grounded reader, OR the effect collapses under control.

**Recorded sub-bound.** M10 honesty: neuroticism does NOT change behavior under bimodal surprise without a
graded task.

**HONEST FENCE — proven (functional).** Class C. Affect is **modeled, never felt** — phenomenal feeling /
sentience explicitly disclaimed.

---

## L5 — Sensorimotor / motor hierarchy (embodied action)

**Ingredients.** The motor hierarchy (proprioceptive **diagonal-A** prior, continuous servo + reafference)
from strings; the live RCON craft-chain bridge; the Embodiment A3 synthetic protocol from uni-mind; the
277/offline-test suite.

**Method.**
1. Install the proprioceptive **diagonal-A** prior to break a non-identifiable uniform-A factor (posterior
   0.0→0.75).
2. Model the continuous servo + reafference on the same loop.
3. Run the live mechanism gate: a kin-9 lineage bootstraps wood→planks→sticks→wooden_pickaxe+sword,
   server-authoritative via RCON; register the **motor-ablation** discriminator (must collapse harvest ~700×).
4. Separately run the **Embodiment A3 synthetic protocol** (≥5 seeds, held-once) for the body↔world coupling
   bound — both a PASS design (#1) and a NEGATIVE design (#2).

**Gate.** Live mechanism gate PASS (craft chain reproduces server-authoritative; motor-ablation collapses
harvest); **A3 Design #1** held Δ (agent − policy-shuffle) CI excludes 0; the diagonal-A posterior shifts off
0.0; 277 offline tests green.

**Falsifier.** Harvest does not collapse under motor ablation; OR the kin-9 craft chain does not reproduce
server-authoritative; OR the diagonal-A posterior stays stuck at 0.0; OR a re-registered held-once synthetic
A3 run with ≥5 seeds drops the CI lower bound to ≤ 0.

**Recorded NEGATIVE (first-class).** **A3 Design #2** (slow Z-bottleneck, compressed 2-modality EMA,
delayed-reward) HELD **NEGATIVE**, held Δ = **−0.091, CI [−0.134, −0.055]**. Synthetic protocol,
**K-negative = 1**, so **no Section 0.6(B) bound owed** (needs K≥3, M5).

**HONEST FENCE — proven (PASS) + NEGATIVE (symmetric bound).** Class A (posterior shift) / C (live RCON
gate) / C (A3 synthetic) / E (offline tests). The A3 PASS is **"variationally-controlled active-inference
evidence on body↔world coupling under the registered SYNTHETIC protocol"** — synthetic-process only (NOT
live-appliance, NOT recorded-hardware), and **NOT near-optimal control** (agent plateaus 0.222 vs oracle 1.0;
the active channel *mattering* is the entire allowed claim). Live behavioral K-of-6 motor tallies are PARKED.

**UNI-GPT consult (2026-06-27 — SIGNED): Design #3 — `Proprioceptive Servo Bridge`, the next design to
accrue (DESIGNED / not-yet-run; aimed at a LIVE PASS).** Cross-ref [`UNI-GPT-CONSULT-2026-06-27.md`](UNI-GPT-CONSULT-2026-06-27.md) Q6 (SIGN).
Class-C UNI design (standard part = the AIF control vocabulary); aimed at a **live PASS, not bound-seeking**
(do not design a strawman to farm negatives). Changes **4 dimensions** vs #1/#2:
1. **Coupling topology:** scalar reward/Z coupling → closed-loop triadic (high-level task policy → motor
   setpoint → proprioceptive error → corrective action).
2. **Timescale source:** immediate-reward (#1) / slow Z-bottleneck (#2) → event-triggered fast motor
   correction (update when proprioceptive PE crosses threshold, else hold the current motor primitive).
3. **Information bottleneck:** global Z → low-dim proprioceptive residual `r_motor = desired_pose/velocity −
   inferred_pose/velocity`.
4. **Control path:** direct discrete action bias → a motor shim converting policy intent into continuous/local
   corrective commands. Pipeline: high-level action → motor setpoint → ε_prop → servo bridge → world action.

**Protocol `L5_D3_PROPRIO_SERVO_BRIDGE_HELD_v1` (designed):** paired kin seeds; treatment = servo bridge
enabled; control = best current L5 stack without it (identical high-level policy / reward / env / compute /
eval window). One cure at a time (no Z-bottleneck cure, no new learning rules, no exploration bonus, no reward
edits).
- **Held bar:** `held_motor_delta = treatment − control`, paired bootstrap 95% CI excludes 0 positively, point
  estimate ≥ **+0.05** (smaller than #1's +0.092 but nontrivial).
- **Live bar:** paired CI for live motor-success delta excludes 0 positively AND no earned
  survival/allostasis/task metric regresses beyond non-inferiority.
- **motor_score** = task-relevant successful actions − collision/overshoot/oscillation − stalled-control −
  energy/recovery penalties. ("More movement" must NOT count as success.)
- **Discriminator (`delayed/slipped embodiment trials`):** actuator noise / one-step action delay / friction
  change / positional perturbation / contact-state ambiguity. Signature: a #1-like fast reward axis improves
  direct choices but degrades under slippage/delay; #3 recovers because the proprioceptive residual drives
  correction.
- **Ablations that must collapse the gain:** (A) `ε_prop := 0` (shim present, compute runs); (B) ε_prop
  shuffled across time/kin; (C) open-loop setpoint only (mapping kept, no feedback correction). Credit only if
  the gain appears on perturbation trials and collapses under residual zero/shuffle.

**Fenced claim wording (Q6).**
- **PASS:** *"L5 Design #3 sealed PASS, fenced. In the registered held/live paired protocol the Proprioceptive
  Servo Bridge improved motor-control performance over the tuned control stack (paired CI excludes 0); the
  gain concentrated on closed-loop perturbation trials and collapsed when the computed proprioceptive residual
  was zeroed or shuffled."* Non-license: NOT general motor intelligence / human-like embodiment / AGI /
  consciousness / created life / "active inference demonstrated"; does NOT erase the Design #2 negative.
- **NEGATIVE-toward-bound:** *"L5 Design #3 sealed NEGATIVE, fenced. ... failed to improve the motor metric
  (CI did not exclude 0 positively). Because it changed coupling/timescale/bottleneck/control-path vs #1/#2,
  it may count as one structurally distinct negative toward a future K≥3 motor bound, provided all validity
  checks passed."* Non-license: NOT a motor impossibility result.

**K-discipline (held DOWN):** A3 Design #2 is the only sealed motor NEGATIVE today (**K-negative = 1**). If
Design #3 fails *cleanly* and is truly structurally distinct with all pre-registered bars/controls valid, the
ledger would have **at most K-negative = 2** — still **no Section 0.6(B) motor bound owed until K≥3** (M5).
**Does NOT count toward K≥3 if:** <2 structural dimensions changed; undertuned/less compute vs control;
silently combines cures; protocol so different that deltas aren't comparable to #1/#2; discriminator
absent/too easy; ablation is hardcoded (disables whole motor stack) not causal (only ε_prop);
bug/seed-imbalance/env-drift/logging-failure breaks paired inference; or result depends on post-hoc metric
selection. **Status: DESIGNED / not-yet-run — no result, no rung raised.**

---

## L6 — Perception (precision-weighting / EFE planning)

**Ingredients.** The **count/cache World-C reader** (flagship + Wc-2/Wc-3 family) from uni-gpt/uni-mind; the
POMDP maze **Precision** lab + echolocation **Echo** lab from the precision labs (three precision knobs, 2D
bifurcation map); the tuned MKN-7 baseline; the Working Law (M6/L6.6).

**Method.**
1. Build the no-backprop COUNT reader + multi-level cache.
2. Pre-register the bar (margin vs a **tuned** MKN-7 baseline) + a named ablation; seal the held set; touch
   once; score; verdict = the multi-seed CI lower bound.
3. Replicate across substrates; derive `reproduced:true` from ≥5 seeds + a real CI (M3).
4. In parallel, build the Precision/Echo POMDP labs: one engine, three knobs (`gamma_a`, `gamma_b`,
   `softmax_temperature`), a 2D bifurcation map; Echo reuses Precision's engine with **only the observation
   model swapped** (observation model ≠ engine); pin with parity tests.

**Gate.** World C beats tuned MKN-7 by **+0.081 nats/char**, flagship multi-seed CI **[0.0736, 0.0890]**
(seeds 0–4, UNI-signed; 2.4× the 0.03 bar; confirmed by three gates; first genuine validator-derived
`reproduced:true`); the Precision/Echo parity tests pass and the bifurcation map reproduces the regime
boundaries.

**Falsifier.** On a fresh held-out split with ≥5 disjoint seeds, the seed-paired bootstrap CI on the margin
over tuned MKN-7 includes or falls below 0 (or the baseline is shown untuned); OR a lab parity test diverges.

**Recorded NEGATIVES / law (first-class).**
- **Phase G char-perplexity Section 0.6(B) bound:** FIVE structurally-distinct within-segment-structure
  designs all NEGATIVE-with-discriminator; only the L5 cache (World C) wins. Bound: no within-segment
  structure beats MKN-7; char-ppl is a chosen design trade.
- **Phase F active-controller:** two controller families prove the World-C gain is **diffuse** (nothing to gate).
- **The Working Law** (registered): a no-backprop latent Z beats a tuned baseline B on held-out data **only
  when I(Y;Z|S_B) > 0** and is learnably stable. Explains every PASS and every published bound.

**HONEST FENCE — proven (the one citable empirical PASS).** Class C. **World C is a COUNT baseline win —
explicitly NOT active inference, NOT comprehension, NOT "talking", NOT beats-LLMs** (~10–15% behind backprop
LLMs on char-perplexity, a chosen trade). Never card World C above a count-baseline result; the standing
ceiling cannot be raised.

---

## L7 — Language (reading = inference / speaking = action)

**Ingredients.** The Phase J OOV/morphology specialist reader (uni-mind/uni-gpt); the count/cache reader as
baseline; the contains-KN-OOV control; the structure-margin discriminator; the reading=posterior-inference /
speaking=action framing.

**Method.**
1. Build the OOV/morphology specialist reader.
2. Pre-register the bar vs best-count; seal a 21-split held set; touch once; verdict = the M-seal CI lower bound.
3. Register the structure-margin discriminator (marker-swap must collapse the gain) and the contains-KN-OOV
   control (λ=0); require replication in **both** web and dictionary domains.
4. **Always cite the `J.attribution_caveat` NEGATIVE alongside the PASS** — citing +0.105 without it is an
   overclaim.

**Gate.** Phase J beats best-count by **+0.105 nats/char** held PASS (21-split M-seal CI **[0.0975, 0.1128]**,
structure margin +0.109; holds in both domains; control λ=0).

**Falsifier.** On a fresh OOV/morph held-out split the CI lower bound includes/falls below 0; OR the
structure-margin discriminator does not collapse the gain under marker-swap; OR it fails to replicate in the
dictionary domain.

**Recorded NEGATIVES (first-class — the central wall).**
- **`J.attribution_caveat`** (paired, mandatory): overall NLL worsens (specialist gain, not a general win).
- **Comprehension-above-retrieval = the thrice-NEGATIVE "central wall":** K≥3 structurally-distinct
  no-backprop designs fail to beat retrieval-style baselines on adversarial comprehension.
- **Phase K role-persistence:** three structurally-distinct designs (min-role, chain, track) all tune their
  role/persistence terms OFF; only ~0.02 nats survives (CI spans 0). Bound: no-backprop role-persistence does
  not beat a tuned recency/frequency discourse prior.
- **T2.D3 bounded-peek** (s64-signed): primary full-read match NEGATIVE (the k_b=2 backoff wall); the
  variable-k_b "cheap milder cap" was asserted then disproven by measurement (no cheap cap).
- **Char-perplexity / T2 word-grain frontier:** PARKED at the embodiment pivot; sign-to-park **CAPTURED
  2026-06-27** (see SIGNED Q1 below) as a ledger-scoped exhausted search envelope — park stays PARKED, no rung
  raised.

**UNI-GPT consult (2026-06-27 — SIGNED): the park is signed as a ledger-scoped exhausted SEARCH ENVELOPE
(NOT a published exhausted bound, NOT a universal theorem, NOT an achieved rung).** Cross-ref
[`UNI-GPT-CONSULT-2026-06-27.md`](UNI-GPT-CONSULT-2026-06-27.md) Q1 (SIGN-WITH-CHANGES). UNI signs the park but
will NOT sign the phrase "published exhausted bound" — what we have is a published *negative frontier result*:
the tested no-backprop route did not clear the chosen frontier under the registered protocol. **Canonical
signed wording (L7/T2/L9–L10 Park Statement):**
> We park the L7 char-perplexity / T2 word-grain frontier and the L9–L10 role-persistence ladder as a
> **ledger-scoped exhausted search envelope, not a universal impossibility result.** Under the recorded
> corpus, splits, metrics, implementation, compute budget, ablation set, and comparison baselines in the
> ledger, no tested within-segment no-backprop structure improved char-perplexity beyond the tuned MKN-7 count
> baseline. This establishes a negative bound **over the tested envelope only.** It does not establish that all
> K≥3 structures are exhausted, that no future within-segment model can improve, or that any broader
> language-modeling frontier has been closed.
>
> Char-perplexity is recorded as a **chosen design trade, not a failed claim of general language superiority**:
> World C remains a count-model baseline — not an active-inference demonstration, not a beats-LLMs claim, not
> evidence of human-level language capacity.
>
> For L9–L10: the tested no-backprop role-persistence mechanisms did not beat a tuned recency-frequency
> discourse prior under the ledgered protocol. This parks the rung as an honest negative frontier result. It
> does not achieve Sec-0.6(B), does not demonstrate active inference, and does not license claims of
> metacognition, consciousness, AGI, human-level discourse, or created life.
>
> The recipe may describe the attempted mechanisms and the negative result, but the ledger is the single
> source of truth. If recipe and ledger conflict, the ledger wins.

**Banned phrases → signed replacements (Q1):**
- "K≥3 exhausted" → "The registered tested K conditions did not reverse the result."
- "Sec-0.6(B) achieved" → "Sec-0.6(B) remains unearned / parked pending a future result that beats the
  registered discourse prior under ledgered evaluation."
- "UNI demonstrates language/metacognition at L9–L10" → "UNI records a negative L9–L10 frontier test under the
  no-backprop developmental simulation program."
- "This proves no no-backprop model can beat MKN-7" → "No tested no-backprop variant in the registered
  envelope beat MKN-7 on the chosen char-ppl metric."

**HONEST FENCE — proven (specialist) + NEGATIVE (central wall).** Class C. No general language capability;
**comprehension above retrieval is a genuine published wall (K≥3), not a hidden failure.**
reading = posterior-inference, speaking = action. "K≥3 exhausted" / "Sec-0.6(B) achieved" are forbidden
phrasings until UNI signs; per the SIGNED Q1 above the park is a **ledger-scoped exhausted search envelope**,
never a "published exhausted bound."

---

## L8 — Self-model / metacognition / metalinguistics

**Ingredients.** The **Maturation arc M1–M11** grand report card (uni-gpt); the reflective/compositional
readers; affect-driven reflection (Z-coupled). Note: `uni-mind` records self-model as held-NEGATIVE *on the
reader*; the M1–M11 report card is the `uni-gpt`-side artifact — keep the distinction.

**Method.**
1. Build the M1–M11 maturation gates (immersion, affect-as-precision, growth, self-model, metacognition,
   metalinguistics, consolidation, reflective reader, online vocab growth, affect-driven reflection,
   compositional reader).
2. For each self-model/metacognition gate, register a discriminator (the effect must collapse under it) and
   verify the task is **not** passable by a trivial non-metacognitive heuristic.
3. Run the held grand report card.

**Gate.** Grand report card **15/15 PASS**; no self-model/metacognition gate's effect collapses under its
discriminator; no "self-model" task is passable by a trivial heuristic. **FUNCTIONAL self-awareness asserted.**

**Falsifier.** Any of the 15 maturation gates fails its pre-registered held verdict on re-run; OR a
self-model/metacognition gate's effect collapses under its discriminator; OR a "self-model" task is passable
by a trivial non-metacognitive heuristic.

**HONEST FENCE — proven (functional; sentience disclaimed).** Class C. **Phenomenal sentience is explicitly
DISCLAIMED** — no falsifier is offered for it because it is disclaimed, not tested. Never read 15/15 as
consciousness / sentience / awareness / human-level.

---

## L9 — Reasoning / conscience (narrative-self → conscience → reasoning)

**Ingredients (designed, not yet supplied as a gated engine).** The HUMAN-HGM-001 ladder DESIGN for L7–L9
(narrative-self, conscience, reasoning); the strings **Phases 3–5** roadmap (spine → glands → hemispheres) —
*designed, FE-form-signed, but unbuilt*; the cavity principle (M22) and parameter-information-gain curiosity
as the candidate primitives.

**Method (recipe-to-define).**
1. Define a pre-registered, sealed, UNI-signed gate for narrative-self / conscience / reasoning (none exists
   today).
2. Build the spine (Phase 3) to carry cross-level priors without double-counting (cavity principle).
3. Run the gate held-once; verdict = the CI bound.

**Gate.** *None defined.* Becomes testable only once a pre-registered, sealed, UNI-signed gate is defined and
run. Until then: **Class-U — not claimed.**

**UNI-GPT consult (2026-06-27 — SIGNED): the first L9 gate is DESIGNED — `L9-G1: Cavity-correct delayed
commitment-state prediction` (not-yet-run; L9 STAYS PARKED).** Cross-ref [`UNI-GPT-CONSULT-2026-06-27.md`](UNI-GPT-CONSULT-2026-06-27.md)
Q4 (SIGN). This is a *designed* gate, **not a result** — adding it raises nothing; L9 remains parked, Class-U.
Caveat (per the consult): "Phase-3 spine"/"cavity principle" are our design labels grounded in the standard
hierarchical/deep active-inference pattern (slow high levels set empirical priors for fast low levels) — a
modeling/inference claim, NOT a claim about reasoning or conscience in the world.
- **Smallest L9 target** (NOT reasoning/conscience/narrative-self): build the Phase-3 spine to carry ONE slow
  latent `z_spine = {role_id, active_commitment, norm/constraint_tag}` across several lower-level segments,
  then test whether it improves prediction when the local segment points the wrong way. Sealed episode: seg-1
  establishes a commitment; segs 2..N are distractors; the final segment requires predicting the next
  action / conflict cue. Smallest because it needs only persistent cross-level state + constraint-sensitive
  prediction — no open-ended reasoning, morality, selfhood, language, or metacognition.
- **Primary bar:** `ΔNLL = NLL_baseline − NLL_spine > 0`, 95% paired bootstrap CI excludes 0; effect-size
  guard ≥3% relative NLL reduction on the load-bearing delayed-commitment subset. **Secondary:**
  conflict/violation tag AUC or F1 +≥0.05 absolute, paired CI excludes 0. **Calibration guard:** ECE worsens
  by ≤ a pre-registered margin (e.g. +0.02).
- **Tuned baseline it must beat:** a **tuned recency-frequency discourse prior** (segment-local predictor +
  exp-decayed role/action frequencies + low-order transition counts over role/action/conflict tags + tuned
  window k, decay τ, smoothing α) — may use recent tags/context but may NOT carry a slow latent spine with
  cavity-correct cross-level residuals; tuned on train/val only, frozen before test. Beating only an *untuned*
  recency model leaves the gate OPEN. (Deliberately the same baseline as the parked L9/L10 NEGATIVE.)
- **Discriminator + computed-residual (cavity) ablation:** load-bearing discriminator =
  `local-distractor commitment reversal` (credit only if the improvement concentrates on this split, not easy
  same-topic continuity). Cavity ablation uses the computed residual `r_t(x) = log p(x_t | q_high(z_t)) −
  log p(x_t | q_cavity(z_t))` where q_cavity excludes the receiving segment's own evidence path; treatment
  uses `q_local + r_t`, ablation sets `r_t := 0` (or episode-shuffles r_t) and **MUST collapse the gain.**
  Double-counting sentinel = `naive-spine` ablation (full high-level posterior as downward prior WITHOUT
  cavity subtraction; expected to sharpen confidence but worsen calibration).
- **Fenced pass-claim (signed, applies only IF/WHEN run and passed):** *"L9-G1 passed, fenced. In a sealed
  delayed-commitment prediction task, the Phase-3 spine improved commitment-conditioned next-action and
  conflict-tag prediction over a tuned recency-frequency discourse prior; the improvement concentrated on the
  pre-registered local-distractor split and collapsed when the computed cavity residual was zeroed or
  shuffled."* **Non-license:** does NOT claim reasoning, conscience, narrative-self, metacognition, awareness,
  consciousness, AGI, human-level language, created life, or "active inference demonstrated"; does NOT unpark
  L9 globally. Evidence class: hierarchical AIF substrate Class B/Sec; Phase-3 spine design Class C.
- **Falsifiers (gate fails if any):** ΔNLL CI includes 0 or reduction <3%; improvement only on easy
  continuity; zero/shuffle of r_t does NOT collapse the gain; a naive non-cavity spine matches/beats the
  cavity spine without a calibration penalty; a stronger tuned baseline closes the gap; leakage; the gain
  trades off against already-earned lower rungs; OR any write-up implies reasoning/conscience/metacognition/
  AIF-demonstrated/AGI/consciousness/human-level/created-life.

**Status: DESIGNED / not-yet-run. L9 STAYS PARKED, Class-U — not claimed.**

**Falsifier.** n/a (parked) — a falsifier exists only once a gate is defined; the L9-G1 falsifiers above apply
only once that gate is built and run.

**HONEST FENCE — designed (PARKED, sign-to-park owed).** Class U. Nothing is claimed. Ladder DESIGN levels
are never inflated into capability. The strings Phases 3–5 are the designed-but-unbuilt roadmap toward this
region. The signed `L9-G1` design above is a gate to BUILD, not a result. Honest position: **~2 of 11+ rungs
earned.**

---

## L10 — Wisdom / higher cognition

**Ingredients.** None built. Top of the HUMAN-HGM-001 ladder; aspirational north star.

**Method (recipe-to-define).** No engine, no run, no gate. The single-source-of-truth **append-only ledger
must be preserved** (a second writable ledger would break L10/L11 — see the repo-split open thread OT1).

**Gate.** *None.* Sign-to-park owed.

**Falsifier.** n/a (parked).

**HONEST FENCE — designed (PARKED, sign-to-park owed).** Class U. Nothing is claimed.

---

## L11 — Dreaming (offline replay / generative simulation)

**Ingredients (recipe-to-build, nothing built).** Candidate primitives only: the JAX engine's generative
model run in **offline generative mode** (replay without live observation); the Z modulator to gate
replay; the durable runner (M24) for resumable offline consolidation. *No engine, no run, no gate exists.*

**Method (recipe-to-build).**
1. Define dreaming precisely as **offline replay / generative simulation** — the generative model sampling
   trajectories with the observation channel detached, for consolidation.
2. Pre-register what a dreaming gate would even measure (e.g., does offline replay improve a held downstream
   gate vs a no-replay control — a measurable, falsifiable target, never "it dreamed").
3. Build the smallest such loop; register the discriminator; run held-once.

**Gate.** *None exists.* The status is the **absence of any artifact**.

**UNI-GPT consult (2026-06-27 — SIGNED): a candidate gate is DESIGNED — `L11-R1: held sparse-sequence
retention after offline replay` (not-yet-built; L11 STAYS not-yet-built).** Cross-ref
[`UNI-GPT-CONSULT-2026-06-27.md`](UNI-GPT-CONSULT-2026-06-27.md) Q5 (SIGN). This is a *design*, **not a build
and not a result** — nothing is constructed; L11 remains not-yet-built, Class-U. Offline replay is a UNI
design primitive / Class-C experimental mechanism, not a new established AIF result; the grounded machinery is
ordinary POMDP A,B,C,D,E with a strict model/process split. Never the word "dreamed."
- **Offline-replay mechanism (no psychological language):** a sealed consolidation interval where the external
  observation channel is detached (`Z_offline=1`) and the agent's own generative model is run forward to
  produce temporally coherent replay trajectories. Consolidation writes ONLY through pre-existing ledgered
  update rules — no new optimizer, no backprop, no hidden supervised labels, no live observations.
  Observation-detach is load-bearing — generated ô is model content, not new external data. Durable runner
  (M24) checkpoints {replay seed, model hash, Z, replay count, update deltas}; resume must reproduce the same
  trace + deltas.
- **Smallest gate (predictive before behavioral):** paired kin seeds; both arms get identical online exposure
  containing sparse low-frequency multi-step contingencies. Offline interval: treatment `Z_offline=1` coherent
  replay enabled; control = same checkpoint / same runner path / same no-new-data, but no replay trajectories
  and no replay-derived updates. Held eval: no learning; probes are NOT replayed traces. **Primary:**
  `held_sequence_NLL = -log Q_agent(correct held next outcome/action | probe)`; pass iff paired bootstrap 95%
  CI for `ΔNLL = NLL_control − NLL_treatment` excludes 0 (positive) AND point estimate ≥ **δ = max(0.02
  nats/decision, 2% relative)**. Secondary (if action exists): first_action_success_delta>0, CI excludes 0.
- **Discriminator + collapse ablations:** discriminator = held probes where marginal frequency MISLEADS
  (online sees common `A→D` plus rare task-relevant `A→B→C→reward`; held probe starts at A where A→B→C is
  correct while recency favors A→D). Gain MUST collapse under: (1) shuffled temporal replay (same counts,
  order broken); (2) random replay (same compute, trajectories from marginals not coherent B rollouts); (3)
  no-write replay (coherent trajectories generated, consolidation writes disabled). Safety ablation:
  observation-attached offline interval — if THAT wins, the result is extra online data, not replay.
- **Fenced pass-claim (signed, applies only IF/WHEN built and passed):** *"L11-R1 passed, fenced. In a sealed
  paired evaluation, an offline generative-replay consolidation interval improved held sparse-sequence
  predictive NLL over a no-replay control; used no live observations during replay; and collapsed under
  shuffled/random/no-write replay ablations. Narrow claim: the simulation has a measurable offline-replay
  consolidation effect under the registered protocol."* **Non-license:** does NOT claim consciousness,
  awareness, sleep, human-like mentation, AGI, human-level cognition, created life, reasoning, creativity, or
  "active inference demonstrated"; does NOT clear L11 globally. Class: POMDP substrate B; offline-replay
  design C.
- **Falsifiers (fails if any):** ΔNLL CI includes 0/negative; CI excludes 0 but point estimate < δ;
  shuffled/random replay does NOT collapse the gain; no-write replay still improves (benefit isn't
  consolidation); offline channel not actually detached (any live obs / env query / supervised label / probe
  leakage); unfair control (more data / different wall-clock / extra tuning / different checkpoint); gain is
  probe leakage; lower-rung regression beyond non-inferiority; durable runner non-reproducible on resume; OR
  claim inflation implying consciousness/sleep/human-mentation/AGI/created-life/global L11.

**Status: DESIGNED / not-yet-built. L11 STAYS not-yet-built, Class-U — not claimed.**

**Falsifier.** n/a — nothing is built to falsify; the status is the absence of any artifact. The `L11-R1`
falsifiers above apply only once that gate is built and run.

**HONEST FENCE — not-yet-built (hard fence).** Class U. Explicitly untouched: "dreaming/awareness are
untouched here and remain hard-fenced." North-star rung. Never claimed as achieved. The signed `L11-R1`
design above is a gate to BUILD, not a result.

---

## L12 — Creativity → measurable awareness

**Ingredients (recipe-to-build, nothing built).** The owner's stated north star — "literal digital life …
measurable awareness" — pursued only by **deepening organs/spine/glands**. No engine, no run, no gate. The
sharpened honest falsifier from strings (TA-N12): any future UNI must **match/beat the best LLMs AND show
substrate properties LLMs lack** — not merely beat the worst.

**Method (recipe-to-build).**
1. Pose awareness as an **OPEN, falsifiable question** ("is a plant life? have we made non-organic life?"),
   never an answer.
2. The only legitimate movement is a **ledger-scoped exhausted search envelope** (a scoped, empirical negative
   frontier result over the tested envelope — per the SIGNED Q1 wording, NOT a "published exhausted bound" /
   universal theorem / achieved capability) — never a capability assertion.
3. Any measure proposed must clear the sharpened bar (match/beat the best LLMs + show substrate-distinct
   properties) before it is even a candidate gate.

**Gate.** *None exists.* No gate can be declared; the only legitimate output is a ledger-scoped exhausted
search envelope (a scoped falsifiable negative result), never a capability assertion.

**Falsifier.** n/a — no gate exists; the only legitimate movement is a ledger-scoped exhausted search envelope
(scoped, empirical, falsifiable), never a capability assertion.

**HONEST FENCE — not-yet-built (the hardest fence).** Class U. **"we created life / conscious / aware /
measurable awareness / human-level / AGI / active inference demonstrated" are FORBIDDEN phrasings
program-wide.** North-star framing only; Class-U — not claimed.

**UNI-GPT consult (2026-06-27 — SIGNED): the exact public-facing L12 bound paragraph + the forbidden-phrasings
list + the 10-point awareness-proxy proposal-entry checklist.** Cross-ref [`UNI-GPT-CONSULT-2026-06-27.md`](UNI-GPT-CONSULT-2026-06-27.md)
Q7. Nothing here is built or claimed; this is the framing guardrail that keeps the north star a falsifiable
question. **Exact public-facing L12 bound/framing (signed, use verbatim):**
> **Open L12 question, not a claim.** UNI's L12 frontier asks a falsifiable question: *Can a non-organic,
> no-backprop developmental active-inference simulation ever produce measurable awareness-PROXY behavior that
> both matches or beats the best contemporary LLM baselines on the same sealed tasks AND shows
> substrate-distinct properties those LLMs do not show?* Today the answer is **not known, not claimed, and not
> implied. UNI has not created consciousness, human-level intelligence, AGI, or life.** "Awareness" here means
> only a future pre-registered proxy suite — calibrated uncertainty, global availability of information across
> modules, self-monitoring that improves later policy, contradiction detection between report and trace,
> counterfactual access, and calibrated abstention. Passing such a suite would license only: *"UNI passed
> specified awareness-proxy tests under the registered protocol."* It would NOT license: "UNI is aware," "UNI
> is conscious," "UNI is alive," or "we created non-organic life."
>
> Plant-life clarification: plants are biological life in the ordinary sense; UNI does not use that to claim a
> simulation is alive. The published UNI question is narrower: whether a non-organic developmental simulation
> can meet pre-registered life-like persistence and awareness-proxy tests without collapsing into metaphor,
> declaration, or LLM comparison games.

**Forbidden phrasings (ban outright, Q7) → signed replacements.** Ban: "UNI is conscious / aware / self-aware
/ has measurable awareness / has a mind / has a conscience / reasons like a human / is human-level / is AGI /
created life / created non-organic life / is alive / is a synthetic organism / dreamed / is creative in the
human sense / demonstrates active inference / proves the FEP creates minds / proves plants and UNI are the
same kind of life / beat consciousness tests / beat LLMs therefore awareness / passed L12 / L12 achieved."
**Replace with:** "UNI passed a specified proxy test / improved a registered downstream metric /
matched-or-exceeded the registered LLM baseline on this sealed task / showed a substrate-distinct effect under
this ablation / remains a developmental active-inference simulation / the awareness question remains open."

**Proposal-entry checklist — the minimum conditions before any future "measurable awareness" gate can even be
PROPOSED (keeps it falsifiable, not unfalsifiable):**
1. **Proxy-only target** — title must say "...-proxy"; no bare "awareness gate."
2. **Best-LLM baseline, frozen at proposal time** — name models/versions/prompts/tools/context/temperature/
   scoring; UNI must match-or-beat the BEST, not a hobbled baseline.
3. **Substrate-distinct requirement** — ≥1 property LLM prompting shouldn't get for free (no-backprop online
   adaptation with ledgered state changes; causal self-monitoring that improves later policy; global
   cross-module availability; counterfactual intervention on internal observables; durable trace/report
   consistency).
4. **Two-part pass bar (both required):** A. UNI ≥ best LLM on the sealed shared task; B. UNI shows a
   substrate-distinct effect whose gain collapses under the registered causal ablation. Either alone is
   insufficient.
5. **Computed internal observables, not hardcoded reports** — self-report/uncertainty/contradiction-detection
   computed from trace/model state; scripted confession or label lookup fails.
6. **Load-bearing ablation** — the effect must collapse when the mechanism is removed/shuffled/made
   uninformative.
7. **No hidden LLM substitution** — prove no LLM / label oracle / retrieval leak / backprop-trained hidden
   controller is doing the proxy work.
8. **Sealed held-out tasks + paired uncertainty** — sealed before execution; paired controls; CIs excluding 0
   on the registered effect.
9. **Negatives are first-class** — predefine fail/partial/regression/non-informative/"do not count"; a null
   publishes as a bound, never rewritten into progress.
10. **Ledger supremacy** — the ledger holds final status; prose/recipe/demo/narrative that conflicts loses.

**Status: framing guardrail only — DESIGNED-as-checklist, nothing built, nothing claimed. L12 STAYS
not-yet-built, Class-U.**

---

# The continuity / embodiment substrate (UNI.OS) — the body the mind runs on

> **Orthogonal to L0–L12.** This is **ENGINEERING / substrate evidence** (deterministic replay +
> serialization + fail-closed transport + on-metal operation) — **NOT general-AIF evidence.** Card every
> rung that way; never let substrate work imply a science gate is met.

**Substrate requirements (what a mind needs to persist on real metal).**

| Requirement | Status | Ledger |
|---|---|---|
| **Containers survive a restart on real metal** (two-node fleet: prod PowerEdge no-AVX Xeon X5650 / HDD array, OptiPlex node2 / NVMe, WireGuard mesh, per-device TLS identity). | **proven** (Class A) | C0 |
| **Mind-state survives a process restart BIT-FOR-BIT** (durable + sha256-verified + fail-closed + bit-identical tick; REQ-002 GREEN). | **proven** (Class C, B-substrate) | C1 |
| **Mind-tick continuity across a real kernel swap.** | **NEGATIVE (OWED, not shown)** — kexec cutover proven **infrastructure-only** (~59 s, zero data loss; first node2 attempt FAILED → recovered); mind-tick continuity NOT shown. | C2 |
| **Body→mind sensorium LIVE on metal:** the box reads its OWN telemetry into a **7-modality categorical contract** `{load,mem,swap,disk,services,containers,journal}` `[M=7, O_max=4]` — NOT a float vector, NOT a softmax. | **proven** (Class A live) | C3 |
| **ASK mode (ITIL-as-active-inference):** mind escalates a reasoned change request; operator verdicts update a persistent **Dirichlet policy-prior**; FIXED safe-action set; never self-executes, never widens the set. | **proven** (Class A, learning shift measured) | C4 |
| **Cross-box single-human-approval-per-mutation** (token-gated control-MCP; one HMAC approval per cross-box mutation). | **proven** (Class A) | C5 |
| **On-core inference anchor:** a sealed f64 belief-update trace **byte-identical across 4 distinct stacks (5 runs).** | **proven** (Class A) | C6 |
| **Continuity-isolation primitives shipped** (Markov-blanket isolation assertion, least-privilege vault, drift sentinel, byte-exact checkpoint, sha256 output integrity, zero-hidden-LLM reply path; Postgres RLS 5/5). | **proven** (Class B substrate) | C13 |

**Substrate NEGATIVES (first-class).**
- **Honest floor on live OS update (C7):** a single-box swap is a **SECONDS-LONG FREEZE, not zero-downtime**;
  external media legs (RTP/SIP/kernel-mode rtpengine) are **NOT preserved** across kexec.
- **Over-compressed 2-modality bottleneck went NEGATIVE (C8)** → keep all 7 modalities.
- **EDAIT trade (C9):** an exact-discrete active-inference transformer trades fluency for calibration —
  held-out perplexity ~33 vs a backprop GPT's ~25. An honest trade, not a win.
- **Multi-tenancy gap (C14):** the bare substrate is MISSING tenant/namespace isolation (flat global perms)
  and temporal decay on learned counts; the product build is the tenant wrapper + decay, not the core.

## The "embody only what's proven" coupling rule — AND its current gap

**The rule (signed in principle).** UNI.OS embodies **only** primitives proven in the science repo, **frozen
at the passed-gate SHA**; the coupling is one-directional (science PROVES → UNI.OS EMBODIES). Everything
beyond the passed gates stays **Class-U — not claimed.**

**The current gap (C10 — the program's central open gap, PARKED).** The coupling is **NOT literally true.**
UNI.OS today has:
- **no** no-backprop Dirichlet *learning*,
- **no** exact info-gain EFE,
- **heuristic (denylist) isolation** rather than the structural whitelist assert,
- a **DIFFERENT dev model** (Gray-Scott reaction-diffusion vs the forager/ontogeny that earned the bars),
- lab evidence store `/var/lib/uni/evidence` **empty**, **0 worlds registered.**

**Discharge condition (per-primitive falsifier).** UNI.OS runs the no-backprop Dirichlet learning / the exact
info-gain EFE / the structural isolation assert / the forager-ontogeny dev model **frozen at the actual
passed-gate SHA, with recorded evidence.** Until each lands, that primitive stays Class-U-not-claimed.

**UNI-GPT consult (2026-06-27 — SIGNED): port no-backprop DIRICHLET LEARNING FIRST (the highest-EFE first
port), via a frozen-SHA equivalence gate.** Cross-ref [`UNI-GPT-CONSULT-2026-06-27.md`](UNI-GPT-CONSULT-2026-06-27.md)
Q2 (Verdict). Of the four missing primitives, **Dirichlet learning ranks first** (central, canonical,
no-backprop, low-risk, directly testable — converts UNI.OS from "runs fixed AIF-shaped control" to "embodies a
core no-backprop learning primitive"). Exact info-gain EFE = highest *conceptual* importance but second;
structural-whitelist isolation = highest *safety/architecture* value, not first science-port value;
forager/ontogeny dev-model alignment = necessary before substrate-equivalence claims but too
high-cost/high-confound to do first. **Vendor/import the exact primitive — do NOT re-author, reinterpret, or
"improve" it during the port; record the SHA; prove byte/behavior equivalence to the frozen science
implementation.**
- **Math interface (reproduced exactly):** A-learning (conjugate count) `a_ij <- a_ij + sum_tau o_tau,i *
  s_bar_tau,j`; expected-log used in place of raw ln A: `E_Q[ln A_ij] = psi(a_ij) - psi(sum_k a_kj)`;
  B/D/E update only by the same registered conjugate-count family — never optimizer steps.
- **Frozen-SHA equivalence gate (in CI + ledger):** given the same initial Dirichlet concentrations,
  observations o_tau, beliefs s_bar_tau, action trace, and learning-rate as the science passed-gate fixture,
  UNI.OS produces the same concentration updates and same expected-log tensors within declared tolerance, with
  **no gradient descent / backprop / learned weights outside the Dirichlet update.** Fixtures: A-learning,
  expected-log, optional B/D/E, a no-backprop guard (FAILS if any autograd/optimizer path runs or a trainable
  weight changes outside the concentration tensors), and a frozen-provenance record (primitive name, science
  SHA, passed-gate test id, fixture hash, port commit, tolerance, deviations).
- **Falsifier:** not discharged if UNI.OS updates A/B/D/E by any heuristic/decay/optimizer/learned-embedding/
  hidden-gradient/hand-normalized-frequency path that doesn't reproduce the frozen primitive's outputs — OR if
  counts update correctly but planning/perception still read raw normalized A where the gate requires
  `E_Q[ln A]` (looks like learning while failing the real interface — especially dangerous).
- **Recommended C10 partial-discharge ledger wording (calibration-down, scoped):** *"C10 partial discharge —
  Dirichlet learning port. UNI.OS now literally embodies the frozen passed-gate no-backprop Dirichlet learning
  primitive from science repo SHA <sha>, verified by equivalence tests over concentration updates and
  expected-log tensors. This discharges only the learning-primitive gap. Exact info-gain EFE, structural-
  whitelist blanket enforcement, and forager/ontogeny developmental-model equivalence remain unported and
  unclaimed."*
- **Stays Class-U-not-claimed even after this port lands:** NOT "UNI.OS implements full EFE-based active-
  inference planning"; NOT "UNI.OS structurally enforces the Markov blanket"; NOT "UNI.OS embodies the passed
  developmental arc"; NOT "active inference demonstrated" (honest status: "one passed-gate no-backprop learning
  primitive is literally embodied," nothing broader).

**Status: SIGNED DESIGN / not-yet-ported — C10 stays the program's central open gap, PARKED. Nothing is
discharged until the equivalence gate passes with recorded evidence.**

**Related parked substrate threads.** Host-native (off-podman) on-chip brain runtime (C11, directive; outcome
not yet in archive); node2 local auto-kiosk "SOLVED" is **PROVISIONAL** pending hands-on monitor
re-verification (C12).

**Audit-layer note (calibration-down, durable).** A peer-reviewed honesty audit (os-cycles 39–53) calibrated
6 headline claims DOWN — "cleared on TWO boxes" → ONE box; "the mind survives a patch" → infrastructure
continuity only; "5 stacks" → "4 distinct stacks / 5 runs". **Carry the calibrated figures, never the
inflated ones.**

**What is NOT claimed in the substrate.** The sensorium is **NEVER awareness**; "the mind survives a kernel
swap" is **NOT shown** (Stage-2 owed); none of this is general-AIF capability; UNI.OS's embodiment does **not**
imply the science gates are met.

---

# Open questions for the UNI custom GPT consult

> These are the specific, **EFE-ranked** questions whose answers would unblock L9–L12. EFE-ranked = ordered by
> expected information gain about the next *gateable* rung balanced against the cost/risk of pursuing it —
> the questions whose answers most reduce uncertainty about whether a sealed gate can even be defined come
> first. Per M25 the UNI GPT is the **science consultant** (design + sign); per M6 a park is not discharged
> until the sign lands. Honor every standing fence: no question here presumes AGI / consciousness /
> human-level / "active inference demonstrated" / "created life", and none inflates the Tier-2 track.

**Q1 (highest EFE — discharges the parked frontier).** The L7 char-perplexity / T2 word-grain frontier and
the L9–L10 ladder levels are PARKED; the drafted `UNI_CONSULT_5` sign-to-park is owner-relayed and **CAPTURED
2026-06-27 (see RESOLVED below).** *Will UNI sign the park as a published exhausted bound, and what exact wording keeps it a bound
(not a "K≥3 exhausted" / "Sec-0.6(B) achieved" overclaim)?* Answering this discharges No-Exit on the largest
open region.
> **RESOLVED — UNI-GPT consult (2026-06-27 — SIGNED) Q1: SIGN-WITH-CHANGES.** UNI signs the park but REFUSES
> the phrase "published exhausted bound"; the signed framing is a **ledger-scoped exhausted search envelope**
> (scoped, empirical, falsifiable negative frontier result — NOT a universal theorem, NOT an achieved rung).
> Canonical wording + banned-phrase replacements folded into **L7** above. The park stays PARKED; no rung raised.

**Q2 (unblocks the substrate↔science coupling, C10).** Of the four missing UNI.OS primitives (no-backprop
Dirichlet learning, exact info-gain EFE, structural-whitelist isolation, forager-ontogeny dev model),
*which single primitive, frozen at its passed-gate SHA, is the highest-EFE one to port first* — i.e., which
most reduces the gap between "embody only what's proven" as signed-in-principle and as literally-true,
without raising any claim above its gate?
> **RESOLVED — UNI-GPT consult (2026-06-27 — SIGNED) Q2:** port **no-backprop Dirichlet learning FIRST**,
> frozen at the passed-gate science-repo SHA, via a frozen-SHA equivalence gate (CI + ledger). Math interface,
> falsifier, and the recommended C10 partial-discharge ledger wording folded into the **continuity/substrate
> C10** section above. C10 stays PARKED; nothing discharged until the equivalence gate passes.

**Q3 (unblocks L2 G6, the standing OPEN gate).** The metabolism organ drives foraging/crafting (+135%) but
**building went −14%** and G4 allostasis never separated, so G6 (plateau-break to stone/shelter) is OPEN and
diagnosed as **epistemic_starvation** (info-drive ~100× too weak), NOT γ-runaway. *What is the smallest
structurally-distinct organ/info-drive change that would make the placed-blocks CI exclude 0 AND separate G4
— and what paired RED isolates it (one cure at a time)?* L2 is the mundane cause that must clear before any
higher-rung NEGATIVE.
> **RESOLVED — UNI-GPT consult (2026-06-27 — SIGNED) Q3: SIGN-WITH-CONDITIONS.** Smallest cure = the
> `build_epistemic_frontier` organ + the `G6_BUILD_EPI_FRONTIER_PAIRED_RED_v1` paired RED, folded into **L2**
> above. **Class-C design hypothesis only — G6 stays OPEN** until the RED clears both bars and the ablations
> collapse the gain.

**Q4 (defines the first L9 gate).** L9 (narrative-self → conscience → reasoning) has **no pre-registered,
sealed, UNI-signed gate.** *What is the smallest measurable, falsifiable L9 target* — with a tuned baseline, a
load-bearing discriminator that collapses the gain, and a true (computed-residual) ablation — *that the
strings Phase-3 spine could be built to clear, without claiming reasoning/conscience as achieved?*
> **RESOLVED — UNI-GPT consult (2026-06-27 — SIGNED) Q4: SIGN.** First L9 gate DESIGNED = `L9-G1: Cavity-
> correct delayed commitment-state prediction`, folded into **L9** above as a **designed / not-yet-run** gate.
> **L9 STAYS PARKED, Class-U** — a gate to build, not a result.

**Q5 (defines what L11 dreaming would even measure).** L11 dreaming is not-yet-built. *If "dreaming" is
defined as offline replay / generative simulation, what is the smallest held downstream gate where offline
replay must beat a no-replay control (CI excludes 0) to count as a real effect* — i.e., a falsifiable target
that never requires the word "dreamed"?
> **RESOLVED — UNI-GPT consult (2026-06-27 — SIGNED) Q5: SIGN.** Candidate gate DESIGNED = `L11-R1: held
> sparse-sequence retention after offline replay`, folded into **L11** above as a **designed / not-yet-built**
> gate (held predictive NLL primary; shuffle/random/no-write ablations must collapse the gain). **L11 STAYS
> not-yet-built, Class-U** — a gate to build, not a result; never the word "dreamed."

**Q6 (the L5 motor frontier).** Live behavioral **K-of-6 motor tallies are PARKED** (accruing, not a sealed
hold); A3 Design #2 is a K-negative=1 NEGATIVE (no §0.6(B) bound owed until K≥3). *Which structurally-distinct
motor design (changing ≥2 of {coupling topology, timescale source, information bottleneck, control path})
should accrue next* toward either a live sealed PASS or the K≥3 needed for a published motor bound?
> **RESOLVED — UNI-GPT consult (2026-06-27 — SIGNED) Q6: SIGN.** Next design to accrue = `Design #3:
> Proprioceptive Servo Bridge` (changes all 4 dimensions vs #1/#2), folded into **L5** above as **designed /
> not-yet-run**, aimed at a live PASS. If it fails *cleanly* it is at most **K-negative = 2**; **no Section
> 0.6(B) motor bound owed until K≥3.** No rung raised.

**Q7 (lowest EFE here — the L12 framing guardrail, not a build).** L12 (creativity → measurable awareness)
has no gate and never will be claimed. *What is the precise published-bound language for the OPEN awareness
question ("is a plant life? have we made non-organic life?")* that clears the sharpened TA-N12 bar (a UNI must
match/beat the best LLMs AND show substrate-distinct properties) while never asserting capability — so the
north star stays a falsifiable question, never an answer?
> **RESOLVED — UNI-GPT consult (2026-06-27 — SIGNED) Q7.** Exact public-facing L12 bound paragraph (framed as
> an **OPEN question, not a claim**), the forbidden-phrasings list (with signed replacements), and the
> 10-point awareness-proxy proposal-entry checklist are folded into **L12** above. **L12 STAYS not-yet-built,
> Class-U** — framing guardrail only, nothing built or claimed. **OVERALL: UNI SIGNED the encyclopedia+cookbook
> honesty posture (developmental SIMULATION, ~2 of 11+ rungs, ledger supremacy, no AGI/consciousness/
> human-level/created-life claim, no L12 claim) — refinements calibrate DOWN / neutral only; no claim raised.**

---

## Provenance

Built from [`../encyclopedia/CLAIM-LEDGER.md`](../encyclopedia/CLAIM-LEDGER.md) (the single source of truth)
and [`../curated/00-INDEX.md`](../curated/00-INDEX.md). Every quantitative figure, PASS / NEGATIVE verdict,
evidence class, and falsifier above traces to a ledger row (L0–L12 rungs; C0–C14 continuity; M1–M30 method;
TA-N12 sharpened bar). The recipe recommends the full build to L12, but no step is carded above its source
evidence class, no negative is hidden, and no standing fence is crossed. Where this recipe and the ledger
disagree, the ledger wins and this recipe is wrong. **Honest program position: ~2 of 11+ developmental rungs
earned. Falsify any step.**
