# S-L0 - Molecular: genome to zygote (float32 tier)

This is the first rung of the UNI developmental ladder (HUMAN-HGM-001: conception toward a speaking three-year-old, eleven levels plus a global affect modulator). It is a no-backprop, nested-Markov-blanket developmental SIMULATION, never a person and never a mind. The honest position is printed on the spine and repeated here without softening: roughly 2 of 11+ developmental rungs are earned, and this chapter accounts for the molecular end of one of them.

The honest position of this specific entry is narrow and exact. UNI models a zygote's first division as an exact discrete Bayesian (conjugate) update, anchored to its closed-form value at the float32 tier (~6e-8, ~1e-6 for a single-step filter), not at the float64 tier. That is the entire claim. It is not a claim that anything was born, awakened, or made alive. It is a toy world, a bounded peek at one well-understood piece of math wired into a developmental scaffold.

## What this rung actually is

The molecular rung implements the conception prior: the inherited "blueprint" that seeds the simulated organism before any development runs. Three primitives carry it. `recombine` combines two parental genomes; `seed_zygote` instantiates the first cell's generative model from that genome; and a no-backprop guard enforces that the only learning rule anywhere in the loop is exact conjugate-Dirichlet count addition (counts plus a learning rate times a sufficient statistic), with autodiff, optax, torch, grad, and backward forbidden in the loop and caught by an AST scan. The first cell division is then expressed as a conjugate Bayesian posterior update: given the prior and the categorical evidence, the engine computes the posterior in closed form and checks it against the analytic value.

This is the ledger's clean, reusable "is the inherited blueprint doing anything?" experiment. The control that travels with it is a marginal-preserving within-family scramble, deliberately not a pooled permutation, so the question "does the genome carry signal beyond chance?" is asked honestly rather than against a strawman.

## The exact claim, with its anchor and its tier (L0.1)

Ledger row **L0.1**, evidence **Class A** (machine-exact anchor), status **proven**, records: the zygote first-division is modeled as exact discrete Bayes (a conjugate update); `recombine` and `seed_zygote` are in place; the no-backprop guard holds; `ontogeny 6/6` passes (`test_embodiment_ontogeny.py`); and Embodiment Rungs 1-2 are GREEN (uncommitted).

The load-bearing calibration is the exactness tier, and it is the heart of this chapter. The JAX core runs **float32**. A float32 host cannot hold a value to the `<1e-10` EXACT tier. So these anchors hold only to **~6e-8** (a ~1e-6 single-step filter), and they are carded at exactly that tier, never higher. The genuine `<1e-10` tier exists only in the NumPy / Rust-f64 path (the cross-language bridge that proves Rust-f64 equals Python); it is not where this rung lives.

This is not a hypothetical caution. A genome docstring once claimed `<1e-10` for this very path; it was caught as an overclaim and corrected to the float32 tier. That correction is the rule made concrete: never card a float32 anchor at the f64 tier. The cell-division identity embedding is held to a separate, looser bound, exceeding 1e-9 would trip its falsifier, and that bound is also stated at its real strength, not inflated toward the f64 oracle.

There is no held-out capability gate here and none is implied. Class A is a machine-exact anchor and a live correctness check, not a dev-gate eval (Class C) and not evidence of any cognitive ability. An anchor proves the arithmetic matches closed form; it does not prove a capability, and the interpretation is fenced accordingly.

### What is NOT claimed in S-L0 - Molecular: genome to zygote (float32 tier)

- **Ceiling.** That UNI "created life" or produced a "conscious baby" or anything alive, aware, or mind-bearing is NOT shown, and neither is exactness at the float64 `<1e-10` tier. The most we claim is exactly L0.1: a float32-tier (~6e-8, ~1e-6 single-step) SIMULATION of a conjugate Bayesian first cell division, with `recombine`/`seed_zygote`, a holding no-backprop guard, `ontogeny 6/6`, and Embodiment Rungs 1-2 GREEN (uncommitted), at Class A, no higher.
- **Fences engaged.** Red line 2 (never consciousness / sentience / aware, no "conscious baby"). Red line 4 (never "created life" / "digital life" as a CLAIM, north-star framing only, posed as an open falsifiable question, never an answer). Red line 7 (never raise a claim above its source class, Class A stays a machine-exact anchor, not a capability or a held-out gate). Red line 10 (no PII, no patent-level math, textbook-level framing only). The standing exactness fence (FM-2, M10): never label a float32 anchor `<1e-10 EXACT`.
- **Negatives that travel with this claim (cite alongside, never strip).** The corrected-overclaim record: the `<1e-10` genome docstring was an overclaim, caught and down-calibrated to the float32 tier; that correction is content, not an embarrassment to hide. The tier ceiling itself is the standing negative: the `<1e-10` EXACT tier is unreachable on this float32 path and lives only in the NumPy / Rust-f64 bridge. The marginal-preserving within-family scramble is the control any "the genome is doing something" reading must clear; it is not a pooled permutation.
- **Parked / owed.** No sign-to-park is owed at L0 (this rung is proven, not parked). Embodiment Rungs 1-2 are GREEN but recorded as uncommitted, the GREEN status is a held check, not a committed milestone, and the chapter carries it that way. The developmental rungs above this (narrative-self, conscience, reasoning, and onward) remain parked or not-yet-built; nothing here advances them.
- **One-line honest summary a skeptic could not dispute.** UNI reproduces the closed-form posterior of a single conjugate Bayesian cell division to the float32 tier (~6e-8) and passes a 6/6 ontogeny test, and that is all this rung claims.

## Falsify this

The lead falsifier, stated operably: run `test_embodiment_ontogeny.py`; if it drops below **6/6**, this rung fails. It also falls if the first-division posterior diverges from the closed-form discrete-Bayes value beyond the float32 tier (~6e-8), if the cell-division identity embedding exceeds **1e-9**, or if the no-backprop guard trips (any autodiff, optax, torch, grad, or backward appears in the loop). Any one of these overturns L0.1. Note the asymmetry the tier enforces: a divergence at the 1e-9 scale would falsify the f64 EXACT tier but is well within the float32 anchor's stated ~6e-8 budget, which is precisely why the claim is carded at float32 and not above it.

## Sources

- Ledger: `CLAIM-LEDGER.md`, row L0.1 and the exactness-tier calibration-down note (Section 1, L0); FM-2 (A-U rubric, exactness-tier honesty) and FM-4 (the not-claimed template) in `MASTER-PLAN.md`; method rows M10 (exactness honesty) and M13 (one engine, no backprop).
- Narrative grounding (PII-redacted): `curated/uni-gpt-digest.md` (Embodiment Rungs 1-2 GREEN; float32 exactness correction) and `curated/uni-mind-digest.md` (the genome / conception-prior primitive: `seed_zygote`, `recombine`, the marginal-preserving within-family scramble control; float32 tier vs the NumPy/Rust-f64 `<1e-10` path).
- Archive pointers (no PII): `...-UNI-GPT` and `...-uni-mind`.
