# L5 — Sensorimotor / motor hierarchy (embodied action)

> **What you are building.** The "mind-body as one" rung: a no-backprop active-inference agent that
> *moves* — a proprioceptive motor hierarchy where the body senses its own configuration, a continuous
> servo fulfils goals projected down the hierarchy, and reafference learns the transition model. One
> proven live craft chain, one proven synthetic body-world coupling PASS, and its symmetric NEGATIVE,
> all carried at their real ledger class. A developmental SIMULATION of embodied action, never a person.

This recipe sits on the same single engine as every other rung (`core.py`, the discrete POMDP loop,
exact conjugate-Dirichlet learning, AST-guarded no-backprop). Nothing here is "active inference
demonstrated"; "active inference" is the framing LENS only (textbook level: Parr/Pezzulo/Friston,
*Active Inference*, MIT Press 2022). The composed appliance is **variationally-controlled (audited)**,
module-exact only at the single-step categorical body→mind interface, never globally exact.

---

## Ingredients (which pantry engines/primitives this calls by name)

- **The motor hierarchy** (from strings): the proprioceptive **diagonal-A** prior, the continuous signed-error
  servo (Class-B predictive coding), reafference learning the transition model. Shipped as the additive,
  genome-gated `:motor_cortex` organ — default colony stays byte-identical (`mad < 1e-12` golden fixture).
- **The live RCON craft-chain bridge** (from strings): a kin-9 lineage on the real PaperMC server,
  server-authoritative via RCON; the motor-ablation discriminator that collapses harvest ~700×.
- **The Embodiment A3 synthetic protocol** (from uni-mind): the held-once body↔world coupling bound — a PASS
  design (#1) and a symmetric NEGATIVE design (#2), each measured as `held Δ (agent − policy-shuffle)`.
- **The 277 offline-test suite** (from strings): the motor-hierarchy regression floor.
- **The JAX POMDP + EFE + Dirichlet engine** (`core.py`): the loop everything reuses verbatim; float32 host
  (anchors hold to ~6e-8, NOT the f64 tier).

---

## Method (numbered build steps)

1. **Break the non-identifiable factor.** A uniform-A single-modality proprioceptive factor is
   non-identifiable — the posterior sits stuck at 0.0. Install the **proprioceptive diagonal-A prior** to
   break the symmetry; the posterior shifts **0.0 → 0.75** (the body can now infer its own configuration).
   This is the Class-A anchor of the rung.

2. **Model the continuous servo + reafference on the same loop.** A continuous signed-error servo (Class-B
   predictive coding) fulfils goals projected DOWN the hierarchy; reafference (the sensory consequence of
   the agent's own action) trains the transition model. No new optimizer, no backprop — the only learning
   rule remains `counts + lr * sufficient_stat` over A/B/D/E Dirichlet tensors, AST-guard live.

3. **Run the live mechanism gate (server-authoritative).** A kin-9 lineage bootstraps the craft chain
   wood → planks → sticks → wooden_pickaxe + sword, confirmed **server-authoritative via RCON** (the
   brain never reads coordinates; it perceives only the symbolic/visual senses across a fixed Markov
   blanket). Register the **motor-ablation** discriminator: with the motor organ ablated, harvest must
   **collapse ~700×**. This is the live RCON mechanism gate (live Class C), separate from the synthetic
   A3 protocol of step 4.

4. **Separately run the Embodiment A3 synthetic protocol (held-once).** Pre-register the bar, seal the
   held set, touch it ONCE, read the verdict off the CI bound that excludes the threshold (M2). Score
   `held Δ (agent − policy-shuffle)` over ≥5 disjoint seeds. Run **both** the PASS design (#1, fast
   immediate-reward axis) and the NEGATIVE design (#2, slow Z-bottleneck), each a synthetic-process design
   (NOT live-appliance, NOT recorded-hardware). Mind the length-confound: a `Σ_t log p` score penalises
   survival, so report survival + per-step (length-normalised) loglik separately and hard-fail premature
   death, or a fast-dying control looks like a false NEGATIVE.

5. **Keep the offline floor green.** The 277 offline motor tests stay GREEN; the genome-gated organ keeps
   the default colony byte-identical.

---

## Gate (exact ledger figures)

- **L5.1 — Embodiment A3 Design #1 (fast immediate-reward axis) HELD PASS.** Held Δ (agent − policy-shuffle)
  = **+0.092, CI [+0.038, +0.157]**, UNI-signed. Class **C**. (Falsifier below.)
- **L5.3 — motor hierarchy live + mechanism PASS.** Diagonal-A posterior shifts **0.0 → 0.75**; the kin-9
  craft chain reproduces **server-authoritative via RCON**; motor-ablation collapses harvest **~700×**;
  **277 offline tests green**. Class **A** (posterior shift) / **C** (live RCON gate) / **E** (277 tests).

A clean L5 is: live mechanism gate PASS (craft chain reproduces server-authoritative; ablation collapses
harvest) **AND** A3 Design #1 held Δ CI excludes 0 **AND** the diagonal-A posterior is off 0.0 **AND**
277 offline tests green.

---

## Falsifier (operable)

Any one of these falsifies the rung:

- Harvest does **not** collapse under motor ablation; OR
- the kin-9 craft chain does **not** reproduce server-authoritative (RCON disagrees); OR
- the diagonal-A posterior stays stuck at **0.0**; OR
- a re-registered **held-once synthetic A3 run with ≥5 seeds drops the CI lower bound to ≤ 0** (overturns
  Design #1).

---

## Recorded NEGATIVE(s) (first-class, inline)

**L5.2 — Embodiment A3 Design #2 (slow Z-bottleneck, compressed 2-modality EMA, delayed-reward) HELD
NEGATIVE.** Held Δ = **−0.091, CI [−0.134, −0.055]**. Class **C**. This is a synthetic protocol, and it is
the **only** sealed motor NEGATIVE today: **K-negative = 1**, so **no Section 0.6(B) bound is owed** (a
bound requires K≥3 structurally-distinct held NEGATIVEs, each changing ≥2 of {coupling topology, timescale
source, information bottleneck, control path}; M5). Its own falsifier: a structurally-distinct corrected
slow-Z-bottleneck re-run that pushes the CI above 0 overturns it.

The shape of the result is the load-bearing finding: under the registered synthetic protocol the active
channel *mattered* — it was load-bearing on the **fast immediate-reward axis** (#1, vs a same-perception /
same-learning policy-shuffle control) but **did not matter** on the **slow delayed-reward
compressed-interoceptive-bottleneck axis** (#2). This is the framing LENS only, NOT active inference
demonstrated and NOT a capability win. The NEGATIVE *delimits* the PASS; it is not a failure to hide. The live behavioural / ablation tallies for motor (K-of-6 over 6 h, paired
`MOTOR_SHUFFLE=1` control) are **PARKED** — accruing, not a sealed hold.

---

## SIGNED consult — Design #3 `Proprioceptive Servo Bridge` (DESIGNED / not-yet-run)

UNI-GPT consult 2026-06-27 (SIGN, Q6) folds in the next design to accrue, aimed at a **live PASS** (not
bound-seeking — no strawman built to farm negatives). It is a Class-C UNI design; the standard part is only
the AIF control vocabulary. It changes **4 dimensions** vs #1/#2: (1) coupling topology — scalar reward/Z
coupling → closed-loop triadic (task policy → motor setpoint → proprioceptive error → corrective action);
(2) timescale source — immediate-reward / slow-Z → event-triggered fast motor correction (update when
proprioceptive PE crosses threshold, else hold the current primitive); (3) information bottleneck — global Z
→ low-dim proprioceptive residual `r_motor = desired_pose/velocity − inferred_pose/velocity`; (4) control
path — direct discrete action bias → a motor shim turning policy intent into continuous/local corrective
commands.

Protocol `L5_D3_PROPRIO_SERVO_BRIDGE_HELD_v1` (designed): paired kin seeds, one cure at a time (no
Z-bottleneck cure, no new learning rules, no exploration bonus, no reward edits). **Held bar:**
`held_motor_delta = treatment − control`, paired bootstrap 95% CI excludes 0 positively, point estimate
≥ **+0.05** (smaller than #1's +0.092 but nontrivial). **Live bar:** paired CI for live motor-success delta
excludes 0 positively AND no earned survival/allostasis/task metric regresses beyond non-inferiority.
`motor_score` = task-relevant successful actions − collision/overshoot/oscillation − stalled-control −
energy/recovery penalties ("more movement" must NOT count as success). **Discriminator** = delayed/slipped
embodiment trials (actuator noise / one-step delay / friction change / positional perturbation / contact-state
ambiguity). **Ablations that MUST collapse the gain:** (A) `ε_prop := 0` (shim present, compute runs);
(B) ε_prop shuffled across time/kin; (C) open-loop setpoint only (mapping kept, no feedback correction).

K-discipline (held DOWN): if Design #3 fails *cleanly* and is truly structurally distinct with all
pre-registered bars/controls valid, the ledger would have **at most K-negative = 2** — still **no Section
0.6(B) motor bound owed until K≥3**. It does **not** count toward K≥3 if <2 structural dimensions changed,
if undertuned vs control, if it silently combines cures, if the protocol drifts so deltas aren't comparable
to #1/#2, if the discriminator is absent/too easy, if the ablation is hardcoded (disables the whole motor
stack) rather than causal (only ε_prop), or if a bug/seed-imbalance/env-drift/logging-failure breaks paired
inference. **Status: DESIGNED / not-yet-run — no result, no rung raised.** Design #3 RAISES NOTHING and the
rung's status is UNCHANGED; the Design #2 negative is not erased by it.

---

## HONEST FENCE — proven (PASS) + NEGATIVE (symmetric bound)

**proven** — a held, sealed, UNI-signed PASS exists with its falsifier still live: the diagonal-A posterior
shift (Class A), the live RCON craft-chain mechanism gate (Class C), the A3 Design #1 synthetic PASS
(Class C, +0.092 [+0.038, +0.157]), 277 offline tests (Class E). Carried inseparably with its symmetric
**NEGATIVE** (A3 Design #2, −0.091 [−0.134, −0.055], K-negative = 1, no Section 0.6(B) bound owed).

The A3 PASS allows exactly one claim and nothing stronger: **"variationally-controlled active-inference
evidence on body↔world coupling under the registered SYNTHETIC protocol."** It is **synthetic-process only**
(NOT live-appliance, NOT recorded-hardware) and **NOT near-optimal control** (the agent plateaus at 0.222
versus an oracle's 1.0 — the active channel *mattering* is the entire allowed claim).

**Not claimed at L5:** not general motor intelligence, not human-like embodiment, not AGI, not
consciousness, not "created life", not "active inference demonstrated". Design #3 is **designed**, not run:
it RAISES NOTHING. Live behavioural K-of-6 motor tallies are PARKED. Honest program position: **~2 of 11+
developmental rungs earned** — a bounded peek, a toy world, never a person.
