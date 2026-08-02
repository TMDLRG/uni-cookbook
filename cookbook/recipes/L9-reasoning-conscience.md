# L9 — Reasoning / conscience (narrative-self → conscience → reasoning)

**What you are building.** A *design*, not a dish: the first pre-registered, sealed, UNI-signed gate that would let the developmental simulation begin to test whether a slow cross-level latent ("a spine") can carry a commitment forward and improve prediction when the local segment points the wrong way. Nothing here is cooked yet. This whole chapter is **PARKED, Class-U — not claimed**, and the signed `L9-G1` design below is a gate to BUILD, not a result. Honest program position: **~2 of 11+ developmental rungs earned.**

---

## Read this first (the fence on the whole chapter)

L9 names three ladder levels — narrative-self, conscience, reasoning — that exist as *design* in the HUMAN-HGM-001 arc and as a *designed, FE-form-signed but unbuilt* roadmap (the strings Phases 3–5: spine → glands → hemispheres). They are **NOT separately gated or PASSed**. Ledger row **L9.1 is Class U (parked)**: "L7–L9 (narrative-self, conscience, reasoning) exist as levels in the HUMAN-HGM-001 ladder DESIGN but are NOT separately gated/PASSed." Its falsifier field reads **n/a (parked)** — a falsifier exists only once a gate is defined and run. Ladder DESIGN levels are never inflated into capability. Nothing in this chapter raises the rung.

The UNI-GPT consult of 2026-06-27 (SIGNED) added a *designed* first gate, `L9-G1`. Per the consult, adding it **raises nothing**: L9 remains parked, Class-U. The consult's own caveat is load-bearing and is repeated verbatim below: "Phase-3 spine"/"cavity principle" are our design labels grounded in the standard hierarchical / deep active-inference pattern (slow high levels set empirical priors for fast low levels) — **a modeling / inference claim, NOT a claim about reasoning or conscience in the world.**

---

## Ingredients

These are **designed, not yet supplied as a gated engine.** Each is named so a competent engineer knows what to reach for when the build is actually authorized.

- **The HUMAN-HGM-001 ladder DESIGN for L7–L9** (narrative-self, conscience, reasoning) — design levels only, never carded as capability.
- **The strings Phases 3–5 roadmap** (spine → glands → hemispheres) — designed, every FE form already UNI-GPT-signed, **but unbuilt**. The strings digest records these explicitly as "designed roadmap, gated, every FE form already UNI-GPT-signed, not built."
- **The cavity principle (M22)** — a hierarchy level must never treat an upstream prior as fresh evidence; divide it out. The exact joint posterior is used everywhere (mean-field rejected as lossy). This is the durable correctness rule for the whole inference hierarchy.
- **Parameter-information-gain curiosity** (the pymdp pA/pB parameter-information-gain form) as a candidate primitive.
- **The JAX POMDP + EFE + Dirichlet engine** (`core.py`) supplies the discrete loop and conjugate-Dirichlet no-backprop learning that any future spine would have to run inside; the AST-guard keeps backprop out of the loop.

No engine, no run, no gate is supplied today. That absence is the status.

---

## Method (recipe-to-define)

The published recipe is a recipe *to define*, because the gate does not yet exist.

1. **Define a pre-registered, sealed, UNI-signed gate** for narrative-self / conscience / reasoning. **None exists today.** The signed `L9-G1` design (below) is the smallest such target proposed so far — and it deliberately does **not** test reasoning, conscience, or narrative-self; it tests only persistent cross-level state plus constraint-sensitive prediction.
2. **Build the spine (strings Phase 3)** to carry cross-level priors *without double-counting* — the cavity principle (M22). The spine carries ONE slow latent across several lower-level segments; the receiving segment's own evidence path must be divided out of the downward prior.
3. **Run the gate held-once;** verdict = the CI bound that excludes the threshold, never the point estimate (M2). Touch the held set ONCE behind an atomic seal-before-scoring + once-only sentinel.

Until step 1 is actually done and step 3 is actually run, the rung stays parked.

---

## The SIGNED L9-G1 gate design (DESIGNED / not-yet-run — folded in, raises nothing)

UNI-GPT consult 2026-06-27 (SIGN), cross-ref `cookbook/UNI-GPT-CONSULT-2026-06-27.md` Q4. This is a *designed* gate, **not a result**. Adding it raises nothing; L9 remains parked, Class-U.

**Smallest L9 target — `L9-G1: Cavity-correct delayed commitment-state prediction`** (explicitly NOT reasoning / conscience / narrative-self): build the strings Phase-3 spine to carry ONE slow latent `z_spine = {role_id, active_commitment, norm/constraint_tag}` across several lower-level segments, then test whether it improves prediction when the local segment points the wrong way. Sealed episode: seg-1 establishes a commitment; segs 2..N are distractors; the final segment requires predicting the next action / conflict cue. It is the *smallest* such target because it needs only persistent cross-level state + constraint-sensitive prediction — **no open-ended reasoning, morality, selfhood, language, or metacognition.**

**Primary bar.** `ΔNLL = NLL_baseline − NLL_spine > 0`, 95% paired bootstrap CI excludes 0; effect-size guard ≥3% relative NLL reduction on the load-bearing delayed-commitment subset.

**Secondary bar.** Conflict / violation tag AUC or F1 +≥0.05 absolute, paired CI excludes 0.

**Calibration guard.** ECE worsens by ≤ a pre-registered margin (e.g. +0.02).

**Tuned baseline it must beat.** A **tuned recency-frequency discourse prior** — segment-local predictor + exp-decayed role/action frequencies + low-order transition counts over role/action/conflict tags + tuned window k, decay τ, smoothing α. It may use recent tags / context but may NOT carry a slow latent spine with cavity-correct cross-level residuals; it is tuned on train/val only and frozen before test. Beating only an *untuned* recency model leaves the gate OPEN. This is **deliberately the same baseline as the parked L9/L10 NEGATIVE** (see below), so a pass here would have to beat the exact prior that has so far won.

**Discriminator + computed-residual (cavity) ablation.** Load-bearing discriminator = `local-distractor commitment reversal` — credit only if the improvement concentrates on this split, not on easy same-topic continuity. The cavity ablation uses the computed residual `r_t(x) = log p(x_t | q_high(z_t)) − log p(x_t | q_cavity(z_t))`, where `q_cavity` excludes the receiving segment's own evidence path; treatment uses `q_local + r_t`, ablation sets `r_t := 0` (or episode-shuffles `r_t`) and **MUST collapse the gain.** Double-counting sentinel = a `naive-spine` ablation (full high-level posterior as downward prior WITHOUT cavity subtraction; expected to sharpen confidence but worsen calibration).

**Fenced pass-claim (signed; applies only IF/WHEN run and passed).** *"L9-G1 passed, fenced. In a sealed delayed-commitment prediction task, the Phase-3 spine improved commitment-conditioned next-action and conflict-tag prediction over a tuned recency-frequency discourse prior; the improvement concentrated on the pre-registered local-distractor split and collapsed when the computed cavity residual was zeroed or shuffled."* **Non-license:** does NOT claim reasoning, conscience, narrative-self, metacognition, awareness, consciousness, AGI, human-level language, created life, or "active inference demonstrated"; does NOT unpark L9 globally. Evidence class if/when earned: hierarchical AIF substrate Class B/Sec; Phase-3 spine design Class C.

**Status: DESIGNED / not-yet-run. L9 STAYS PARKED, Class-U — not claimed.**

---

## Gate

**None defined.** L9 becomes testable only once a pre-registered, sealed, UNI-signed gate is defined and run. Until then: **Class-U — not claimed** (ledger row L9.1, status: parked).

The `L9-G1` bars above are a **gate to BUILD**, not a met condition. There are no figures to cite as achieved, because nothing has been run. The only honest numbers on this rung are the *bars a future run would have to clear* (ΔNLL CI excludes 0 with ≥3% relative reduction on the delayed-commitment subset; conflict-tag AUC/F1 +≥0.05; ECE worsens ≤ +0.02) — none of which is a result.

---

## Falsifier

**n/a (parked).** A falsifier exists only once a gate is defined; the ledger row L9.1 falsifier field is literally "n/a (parked)." The `L9-G1` falsifiers below apply **only once that gate is built and run** — they are part of the design, not active tests:

The gate (when built and run) fails if any of: ΔNLL CI includes 0 or the reduction is <3%; the improvement appears only on easy continuity, not the local-distractor split; zero/shuffle of `r_t` does NOT collapse the gain; a naive non-cavity spine matches/beats the cavity spine without a calibration penalty; a stronger tuned baseline closes the gap; leakage is found; the gain trades off against an already-earned lower rung; OR any write-up implies reasoning / conscience / metacognition / AIF-demonstrated / AGI / consciousness / human-level / created-life.

---

## Recorded NEGATIVE(s)

These are first-class and inline. They are the reason this region is parked rather than open, and they define exactly what a future L9-G1 pass would have to overturn.

- **L7.4 — Phase K role-persistence (NEGATIVE, bound).** Three structurally-distinct no-backprop designs (min-role, chain, track) all tune their role/persistence terms **OFF**; only ~0.02 nats survives (CI spans 0). Bound: **no-backprop role-persistence does not beat a tuned recency/frequency discourse prior** on adversarial anonymized referent cloze. This is the *same* tuned discourse prior the L9-G1 design picks as its baseline — by design — which is why beating it would be the load-bearing event.

- **The signed L7 / T2 / L9–L10 Park Statement (UNI-GPT consult 2026-06-27, Q1, SIGNED).** Per the canonical signed wording: "For L9–L10: the tested no-backprop role-persistence mechanisms did not beat a tuned recency-frequency discourse prior under the ledgered protocol. This parks the rung as an honest negative frontier result. It does not achieve Sec-0.6(B), does not demonstrate active inference, and does not license claims of metacognition, consciousness, AGI, human-level discourse, or created life." This is a **ledger-scoped exhausted search envelope, not a universal impossibility result and not an achieved rung.** Use the signed replacements: instead of "K≥3 exhausted" write **"The registered tested K conditions did not reverse the result."**; instead of "Sec-0.6(B) achieved" write **"Sec-0.6(B) remains unearned / parked."**

- **The owed sign-to-park (open).** By No-Exit Discipline (M6) a park is not discharged until the sign lands. The L9–L10 ladder park is folded into the 2026-06-27 signed Q1 statement; the earlier char-perplexity / T2 park sign (`UNI_CONSULT_5`) was drafted and owner-relayed but recorded as not-yet-captured. Carry the park as PARKED, never as closed.

---

## HONEST FENCE — designed (PARKED, sign-to-park owed)

**Class U. Nothing is claimed.** This rung is a *design*, not a dish. Ladder DESIGN levels are never inflated into capability. The strings Phases 3–5 (spine → glands → hemispheres) are the designed-but-unbuilt roadmap toward this region; the signed `L9-G1` design above is a **gate to BUILD, not a result** — folding it in **raises nothing** and the rung's status is **UNCHANGED**.

**Not claimed (load-bearing, never softened):** UNI does **not** reason, does **not** have a conscience, does **not** have a narrative self, is **not** self-aware here, does **not** demonstrate active inference, is **not** human-level, is **not** AGI, has **not** created life. "Phase-3 spine" and "cavity principle" are design labels for the standard hierarchical / deep active-inference pattern (slow high levels setting empirical priors for fast low levels) — a modeling / inference claim, **NOT** a claim about reasoning or conscience in the world. The whole program remains a **developmental active-inference SIMULATION**: a bounded peek, a toy world, never a person. **~2 of 11+ developmental rungs earned.** The cookbook fully recommends building toward L12 — and this step, honestly, is **designed / parked, Class-U, not-claimed**, with the gate still owed.
