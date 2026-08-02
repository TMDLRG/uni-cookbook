# L11 — Dreaming (offline replay / generative simulation)

**What you are building.** A *recipe-to-build* (nothing built): an offline replay / generative-simulation interval where the same one POMDP engine runs its own generative model forward with the external observation channel detached, so that consolidation can write through the pre-existing no-backprop update rules. This is a **design primitive for a developmental SIMULATION**, never sleep, never mentation, and **never the word "dreamed."**

> **Status up front (the ledger wins).** Ledger row **L11.1 is Class U — not-yet-built.** There is **no engine, no run, no gate** — the status *is* the absence of any artifact. The SIGNED `L11-R1` design below is a **gate to BUILD, not a result**: it raises nothing, and the rung stays **not-yet-built**. Honest program position carried throughout: **~2 of 11+ developmental rungs earned** — a bounded peek, a toy world, never a person.

---

## Ingredients (candidate primitives only — nothing here is wired together yet)

All of these already exist elsewhere in the pantry; **none has been composed into an L11 loop.** The recipe names them so a competent engineer knows what would be assembled, not to imply assembly has happened.

- **The JAX POMDP + EFE + Dirichlet engine** (`core.py`): the discrete `perceive → EFE-plan → act → learn` loop, run here in **offline generative mode** — the generative model sampling trajectories with the observation channel detached. The grounded machinery is ordinary POMDP A, B, C, D, E tensors with a strict **model/process split**; no new optimizer, no backprop, no autodiff (AST-guard live, per M13).
- **The Z affect modulator** `[energy, arousal, valence, fatigue, pain, threat, safety, inflammation]`: used only as the **gate signal** `Z_offline=1` that detaches the observation channel. Affect is modeled, never felt.
- **The durable runner (M24)**, "no send-and-pray": append-one-JSON-line-per-unit ProgressLog that checkpoints `{replay seed, model hash, Z, replay count, update deltas}`; resumable; cover BOTH terminal states (silence is not success).
- **The constitution** (kitchen rules, §0): bars-before-build / held-once (M2), validator-derived `reproduced:true` from ≥5 seeds + a real CI (M3), contains-baseline + load-bearing-discriminator (M7), one engine / no backprop (M13).

There is **no count/cache reader, no embodiment organ, no live appliance** in this recipe — L11 is upstream of all of them. Offline replay is a **UNI design primitive / Class-C experimental mechanism**, not a new established active-inference result.

---

## Method (recipe-to-build — every step is a build instruction for an unbuilt loop)

1. **Define dreaming precisely, with no psychological language.** Dreaming here means *offline replay / generative simulation*: a sealed consolidation interval where the external observation channel is detached (`Z_offline=1`) and the agent's own generative model is run forward to produce **temporally coherent replay trajectories**. The generated `ô` is **model content, not new external data** — the observation-detach is load-bearing.
2. **Constrain what consolidation may write.** Consolidation writes **ONLY** through the pre-existing ledgered update rules (`counts + lr * sufficient_stat` over the A/B/D/E Dirichlet tensors). No new optimizer, no backprop, no hidden supervised labels, no live observations during replay.
3. **Pre-register what a dreaming gate would even measure** before building it — a measurable, falsifiable downstream target ("does offline replay improve a held downstream metric vs a no-replay control"), **never "it dreamed."** Build the smallest such loop; register the discriminator; run held-once.
4. **Make it durable and reproducible.** Wire the M24 runner so a resume reproduces the **same replay trace and the same update deltas** from the checkpoint `{replay seed, model hash, Z, replay count, update deltas}`.

The candidate gate that instantiates this method is the SIGNED `L11-R1` below. **Building it is the work; it has not been done.**

---

## The SIGNED candidate gate — `L11-R1` (DESIGNED / not-yet-built)

> **UNI-GPT consult 2026-06-27 — SIGNED (Q5).** Cross-ref `../UNI-GPT-CONSULT-2026-06-27.md`. This is a **design, not a build and not a result.** Nothing is constructed; L11 remains **not-yet-built, Class-U**. Folding it in **RAISES NOTHING** and the rung's status is **UNCHANGED**.

**`L11-R1`: held sparse-sequence retention after offline replay.**

- **Offline-replay mechanism.** A sealed consolidation interval, observation channel detached (`Z_offline=1`), generative model run forward to produce temporally coherent replay; updates only through existing rules. The durable runner checkpoints `{replay seed, model hash, Z, replay count, update deltas}`; resume must reproduce the same trace and deltas.
- **Smallest gate (predictive before behavioral).** Paired kin seeds; both arms get identical online exposure containing **sparse low-frequency multi-step contingencies**. Offline interval: treatment `Z_offline=1` (coherent replay enabled); control = same checkpoint / same runner path / same "no new data", but **no replay trajectories and no replay-derived updates**. Held eval: no learning; probes are **NOT** replayed traces.
- **Discriminator (the misleading-marginals split).** Online sees a common `A→D` plus a rare task-relevant `A→B→C→reward`; the held probe starts at A where `A→B→C` is correct while recency favors `A→D`. Credit only if the gain concentrates on this split.

---

## Gate (the exact pass condition — applies ONLY if/when `L11-R1` is built and run)

Today there is **no gate to pass** — *"The status is the absence of any artifact."* The figures below are the **registered design bar**, not a measured result.

- **Primary.** `held_sequence_NLL = -log Q_agent(correct held next outcome/action | probe)`. **Pass iff** the paired bootstrap 95% CI for `ΔNLL = NLL_control − NLL_treatment` **excludes 0 (positive)** AND the point estimate is at least **δ = max(0.02 nats/decision, 2% relative)**. (Verdict = the CI bound that excludes the threshold, never the point estimate — M2.)
- **Secondary (if an action exists).** `first_action_success_delta > 0`, CI excludes 0.
- **Collapse ablations (the gain MUST disappear under each).** (1) **shuffled temporal replay** (same counts, order broken); (2) **random replay** (same compute, trajectories drawn from marginals not coherent B-rollouts); (3) **no-write replay** (coherent trajectories generated, consolidation writes disabled). **Safety ablation:** an *observation-attached* offline interval — if THAT wins, the "result" is extra online data, not replay.

**Fenced pass-claim (signed, applies only IF/WHEN built and passed):** *"L11-R1 passed, fenced. In a sealed paired evaluation, an offline generative-replay consolidation interval improved held sparse-sequence predictive NLL over a no-replay control; used no live observations during replay; and collapsed under shuffled/random/no-write replay ablations. Narrow claim: the simulation has a measurable offline-replay consolidation effect under the registered protocol."* Evidence class would be POMDP substrate **B**, offline-replay design **C**. **Non-license:** does NOT claim consciousness, awareness, sleep, human-like mentation, AGI, human-level cognition, created life, reasoning, creativity, or "active inference demonstrated"; does NOT clear L11 globally.

---

## Falsifier

**n/a — nothing is built to falsify; the status is the absence of any artifact.** The `L11-R1` falsifiers below apply **only once that gate is built and run** — the gate **fails if any** holds:

- `ΔNLL` CI includes 0 / is negative; OR the CI excludes 0 but the point estimate is below `δ`.
- shuffled / random replay does **NOT** collapse the gain.
- **no-write replay still improves** (the benefit is not consolidation).
- the offline channel is **not actually detached** (any live observation, environment query, supervised label, or probe leakage).
- **unfair control** (more data, different wall-clock, extra tuning, or a different checkpoint).
- the gain is **probe leakage**; OR a lower rung regresses beyond non-inferiority; OR the durable runner is **non-reproducible on resume**.
- **claim inflation** implying consciousness / sleep / human-mentation / AGI / created-life / global L11.

---

## Recorded NEGATIVE(s) (first-class, inline)

L11 carries **no own measured negative** because **nothing has been run** — and that absence is itself the honest record (ledger row **L11.1**, Class U, *"absent from all digests"*). The first-class negatives that **bind this chapter** come from the surrounding rungs and the structure of the method:

- **The structural negative — there is no artifact.** Per the narrative grounding, *"dreaming/awareness are untouched here and remain hard-fenced."* This is recorded as a NEGATIVE-for-completeness, not deferred: L11 is the *absence* of an engine, a run, and a gate.
- **The pre-baked collapse ablations are negative-discriminators (M7).** The `L11-R1` design **bakes its own falsifiers in**: if shuffled/random replay does not collapse the gain, or no-write replay still wins, the candidate result is recorded NEGATIVE on the spot — coherence-of-replay and write-through-consolidation are the load-bearing causes, and the safety ablation (observation-attached) exists precisely to catch "this was just extra online data."
- **K-discipline inherited (M5).** Even a *clean* `L11-R1` outcome — pass or negative — is a single design. No Section 0.6(B) bound is owed or claimable here: a dreaming bound would need **K≥3 structurally-distinct held NEGATIVEs**, and zero exist because zero have been run.

---

## HONEST FENCE — **not-yet-built** (hard fence, Class U)

**Not claimed:** not consciousness, not awareness, not sleep, not "dreamed," not human-like mentation, not reasoning, not creativity, not AGI, not human-level cognition, not created life, not "active inference demonstrated." Explicitly untouched: **"dreaming/awareness are untouched here and remain hard-fenced."** This is a **north-star rung**, never claimed as achieved.

Offline replay is a **design primitive** of a developmental active-inference SIMULATION, **never the word "dreamed."** The SIGNED `L11-R1` design above is a **gate to BUILD, not a result** — it is folded in as **DESIGNED / not-run**, it **raises nothing**, and the rung's status is **UNCHANGED: not-yet-built, Class-U — not claimed.** Where this recipe and the ledger disagree, the **ledger wins.** Honest program position: **~2 of 11+ developmental rungs earned.**
