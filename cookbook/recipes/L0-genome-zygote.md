# L0 — Molecular / genome → zygote (the conception prior)

> One recipe, one engine, shown at the smallest scale: the very first cell division, modeled as an exact
> conjugate Bayesian update with no gradients. A developmental active-inference SIMULATION of conception,
> never a person, never a baby, never life.

**What you are building.** A float32-tier, no-backprop instantiation of the conception prior: encode a
genome as a categorical prior, `seed_zygote` the initial Dirichlet tensors, and model the zygote's first
division as an **exact discrete Bayes (conjugate) update** that matches the closed-form value to the
float32 tier, gated by `test_embodiment_ontogeny.py` at 6/6 with a live no-backprop guard.

---

## Ingredients (pantry engines / primitives, called by name)

- **The embodiment ontogeny** (`recombine` / `seed_zygote`, the no-backprop AST-guard, `ontogeny 6/6`,
  conjugate first-division, the cell-division identity embedding) — from the JAX engine (`uni-mind` /
  `uni-gpt`).
- **The JAX POMDP + EFE + Dirichlet engine** (`core.py`): the conjugate discrete-Bayes update
  (`exact_posterior_discrete`); learning is `counts + lr * sufficient_stat` for the A/B/D Dirichlet
  tensors. **float32 host** — anchors hold to ~6e-8 (~1e-6 single-step filter), NOT the f64 tier.
- **The Rust-f64 / NumPy deep-reader path**: the genuine `<1e-10` EXACT tier and the cross-language
  Rust-f64 == Python oracle. Named here only to mark the boundary you must NOT cross when carding L0.
- **Method constitution called by name:** M13 (one engine, no backprop — AST-guard, `world.<attr>`
  whitelist isolation), M10 (exactness honesty — never card a float32 anchor at the f64 tier), M12
  (WORLD ⊥ BODY ⊥ MIND — module-exact only at the single-step categorical interface).

---

## Method (numbered build steps)

1. **Encode the genome as a categorical prior.** Represent the inherited blueprint as categorical
   parameters; `seed_zygote` instantiates the initial A/B/D Dirichlet tensors from it. Keep the
   model/process split sacred: the agent owns only the MODEL and couples through a typed Markov blanket;
   it never reads world hidden state.
2. **Model the zygote first-division as an exact discrete Bayes (conjugate) update.** Use
   `exact_posterior_discrete` from `core.py`. No gradients: the only update is conjugate count addition.
3. **Hold the no-backprop AST-guard live over the whole division step (M13).** An AST scan must find no
   autodiff / optax / torch / grad / backward in the loop; isolation is a `world.<attr>` whitelist, not a
   blacklist.
4. **Run `test_embodiment_ontogeny.py` for the 6/6 ontogeny gate.** Verify the cell-division identity
   embedding holds. (Embodiment Rungs 1–2 are GREEN but **uncommitted** — the figures below are the held
   gate values, carded at their real class.)
5. **Optional control (reusable "is the blueprint doing anything?" experiment).** Compare `recombine`
   against a **marginal-preserving within-family scramble** (NOT a pooled permutation): the scramble
   preserves marginal statistics so any surviving effect is attributable to inherited structure, not to
   the marginals. Treat any positive dev signal from this as DEV-only, never as a held PASS.

---

## Gate (the exact pass condition — EXACT ledger figures, ledger row L0.1)

`ontogeny 6/6` GREEN; the first-division posterior matches the **closed-form discrete-Bayes value to the
float32 tier (~6e-8, ~1e-6 single-step filter)**; the **cell-division identity embedding ≤ 1e-9**; and the
no-backprop guard never trips.

**Exactness honesty (M10, load-bearing).** Card this at **float32**, NEVER at the `<1e-10` f64 tier. The
JAX `core.py` host runs float32, so these anchors hold only to ~6e-8 (~1e-6 single-step filter). The
genuine `<1e-10` EXACT tier lives ONLY in the NumPy / Rust-f64 path. **Recorded negative (inline):** a
genome docstring claiming `<1e-10` was caught as an overclaim and corrected to `<1e-6 (float32 tier)` —
the precision-tier line is the one carded here.

Ledger class for L0.1: **A** (machine-exact anchor), at the float32 tier. Status: **proven**.

---

## Falsifier (operable)

Any one of these falsifies L0.1:
- `test_embodiment_ontogeny.py` drops below 6/6; OR
- the first-division posterior diverges from the closed-form discrete-Bayes value **beyond the float32
  tier**; OR
- the cell-division identity embedding **exceeds 1e-9**; OR
- the no-backprop AST-guard **trips** (any autodiff in the loop).

---

## Recorded NEGATIVE(s) (first-class, inline)

- **The `<1e-10` docstring overclaim (caught and corrected).** A genome docstring asserted the f64 EXACT
  tier (`<1e-10`) for a float32-host result. This was caught as an overclaim and corrected to
  `<1e-6 (float32 tier)`. It is recorded here not as a hidden failure but as the load-bearing reason this
  rung is carded at float32: never card a float32 anchor at the f64 tier (M10). The negative is the
  precision discipline working as designed.

---

## HONEST FENCE — proven (Class A, float32 tier)

A held, sealed value exists: `ontogeny 6/6` GREEN, first-division posterior matching the closed-form
discrete-Bayes value to the float32 tier (~6e-8, ~1e-6 single-step filter), identity embedding ≤ 1e-9, the
no-backprop guard live. Its falsifier (above) is still live.

**Not claimed at L0 (the exact not-claimed line):** *not* "we created life", *not* a "conscious baby",
*not* exact at f64 — it is a **float32-tier developmental SIMULATION of a conjugate Bayesian first
division**. No awareness, no sentience, no person; functional self-awareness is not even in scope at this
rung (that vocabulary is reserved for L8, and phenomenal sentience is disclaimed program-wide). "Active
inference" here is the framing LENS at textbook level (Parr/Pezzulo/Friston, *Active Inference*, MIT Press
2022), not a demonstrated AIF loop; the genuine exactness tier is the Rust-f64 path, not this one.

**Honest program position (printed, never softened):** ~2 of 11+ developmental rungs earned. The whole
program is a developmental active-inference SIMULATION — a bounded peek, a toy world, never a person.
Where this recipe and the ledger disagree, the ledger wins.
