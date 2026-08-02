# L4 — Interoceptive / Autonomic + Affect-as-Precision

> **What you are building.** A global affect modulator `Z` that turns interoceptive / autonomic
> signals into a *precision dial*: raising arousal / threat sharpens perception (precision-weighting)
> and flips the pragmatic↔epistemic balance of planning — affect **MODELED, never felt.** This is one
> rung of a developmental active-inference **SIMULATION**, a bounded peek, never a person.

---

## Ingredients

Drawn from the shared pantry, by name:

- **The Z affect modulator** (uni-gpt / uni-mind) — the global vector
  `[energy, arousal, valence, fatigue, pain, threat, safety, inflammation]` that sets
  precision / preferences / habits / learning-rate / planning-horizon. *Affect modeled, never felt.*
- **The JAX POMDP + EFE + Dirichlet engine** (`core.py`, uni-mind) — the discrete `perceive → EFE-plan →
  act → learn` loop and its **precision dial** (`gamma_a` sensory, `gamma_b` transition, policy
  softmax temperature). **float32 host** — anchors hold to ~6e-8, NOT the f64 tier (M10).
- **A grounded reader** to test the pragmatic↔epistemic flip under live observations.
- **The contains-baseline + load-bearing-discriminator discipline** (M7) — supplies the required
  Z-ablation that must collapse the effect.

This is the WORLD ⊥ BODY ⊥ MIND framing (M12): **interoception = hardware self-signals** entering the
mind through the typed sensory blanket; affect is a *latent modulator over that mind's own precision*,
never a phenomenal state of the substrate.

---

## Method

1. **Wire Z as a precision modulator, not a reward.** Couple the eight-channel `Z` vector to the
   engine's control surface: it sets sensory precision (`gamma_a`), transition precision (`gamma_b`),
   policy temperature, preference weighting (the C tensor), habit strength (E), learning-rate, and
   planning-horizon. Z is a *dial over how sharply the existing generative model is read*, not a new
   objective term — keep the no-backprop AST-guard live (M13); learning stays `counts + lr *
   sufficient_stat`.

2. **Show the precision-weighting effect.** Raise arousal / threat and confirm perception **sharpens**:
   higher `gamma_a` concentrates the observation likelihood, so the posterior tightens around the
   sensed state. This is the textbook claim `F[q] ≥ −ln p(o|m)` read through a precision lens — affect
   tunes *how confidently* the agent reads its world (M12, textbook level only; cite Parr/Pezzulo/
   Friston, *Active Inference*, MIT Press 2022).

3. **Show the pragmatic↔epistemic flip.** Under the grounded reader, demonstrate that shifting Z
   re-weights expected free energy between its **pragmatic** (goal-seeking) and **epistemic**
   (information-seeking) components, so the selected policy flips. Raising threat/arousal moves the
   balance; the planner's chosen action class changes as a function of affect, on the same engine.

4. **Register the Z-ablation discriminator (M7).** Pre-register that **removing Z collapses the
   effect**: with Z ablated, precision-weighting does not change and the pragmatic↔epistemic flip does
   not appear under the grounded reader. The gain is credited ONLY if it appears with Z live and
   disappears under ablation, and survives a control.

---

## Gate

With Z live, precision-weighting and the pragmatic↔epistemic flip both appear; the **Z-ablation
collapses them**; and the effect survives a control.

**Exact ledger figures (L4.1, Class C, status `proven`).** *Affect-as-precision*: emotion modulates
precision so perception sharpens and the pragmatic↔epistemic balance flips; the global Z modulator
`[energy, arousal, valence, fatigue, pain, threat, safety, inflammation]` sets precision / preferences
/ habits / learning-rate / horizon. This is a **dev-gate / held-out** (Class C) result, not a
machine-exact anchor. **The verdict is the gate, never a point estimate** (M2). Do NOT card this above
a Class-C functional result.

---

## Falsifier

An **ablation of the Z modulator shows no change in precision-weighting / no pragmatic↔epistemic flip**
under the grounded reader, OR the effect collapses under control. (Verbatim from ledger row L4.1.) If
removing Z leaves perception equally sharp and planning unchanged, the affect-as-precision claim is
dead.

---

## Recorded NEGATIVE / sub-bound (first-class, inline)

**M10 honest boundary (recorded sub-bound).** **Neuroticism does NOT change behavior under bimodal
surprise without a graded task.** Under the grounded reader's bimodal-surprise probe, varying the
neuroticism-style affect parameter produced no behavioral change — exposing it would need a *graded*
task, not a bimodal one. This is a real boundary on the affect machinery, carried inline beside the
PASS: the Z dial demonstrably modulates precision and the pragmatic↔epistemic balance, but it does
**not** license a claim that every affect-personality parameter drives behavior on every task. The
recorded result delimits the positive rather than inflating it.

---

## HONEST FENCE — **proven** (functional, Class C)

A held, gate-level functional PASS exists, with its Z-ablation falsifier still live. **NOT claimed:**

- **Affect is MODELED, never felt.** Phenomenal feeling / sentience is explicitly **DISCLAIMED** — no
  falsifier is offered for it because it is disclaimed, not tested. Z is a latent modulator over the
  mind's own precision, never a quale, never a felt emotion of the substrate.
- This is **NOT** consciousness, sentience, awareness, a mind, a feeling, AGI, human-level, or
  "active inference demonstrated." (Functional self-awareness may be described only at L8; phenomenal
  sentience stays disclaimed program-wide.) "Active inference" is the framing **lens** here, at
  textbook level only — no AIF loop is claimed in the Rust crate.
- The gate is **Class C** (dev-gate / held-out), NOT a machine-exact (Class A) anchor and NOT the f64
  `<1e-10` exact tier — the JAX host is float32 (M10).
- **No SIGNED consult design is folded into this rung** (the 2026-06-27 consults attach at L2, L5, L9,
  L11, L12); nothing raises L4's status. The rung stands on row L4.1 alone.

**Honest program position:** ~**2 of 11+ developmental rungs earned.** The whole program remains a
developmental active-inference **SIMULATION** — a toy world, a bounded peek, never a person. Where this
recipe and the ledger disagree, the **ledger wins.**
