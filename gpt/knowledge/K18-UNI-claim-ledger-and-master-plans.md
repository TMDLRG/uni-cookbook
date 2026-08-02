# The UNI claim ledger (single source of truth) and the authoring master plans

> **Knowledge file `K18-UNI-claim-ledger-and-master-plans.md`** of the UNI Encyclopedia & Cookbook GPT pack.
> This file is a BUILD ARTIFACT: it merges **3** source file(s) from the
> repository `TMDLRG/UNI-Encyclopedia-Cookbook`, byte-for-byte, in the order listed below.
> The repository is the single source of truth; if this file and the repository ever
> disagree, the repository wins and this file is stale.
>
> SOVEREIGNTY RULE (binding, do not merge the two ledgers): this corpus carries TWO sovereign evidence vocabularies. The UNI 4-value fence (proven / designed / hypothesized / not-yet-built) describes ONLY UNI's own build status and is governed by encyclopedia/CLAIM-LEDGER.md. The NATURA 12-value class, in three groups, describes ONLY nature's observed regularities and is governed by encyclopedia/NATURE-LEDGER.md: group A / measured = OBSERVED-REPLICATED, OBSERVED-SINGLE, OBSERVED-CONTESTED; group B / derived = MODELED, MODELED-CONTESTED, HYPOTHESIZED; group C / fenced = INADMISSIBLE, SUPERSEDED, NOT-MEASURED, NOT-SOURCED, NOT-CONFIRMED, NOT-LOCATED. Six of the twelve were registered by NA-00 amendment 2026-07-15-A after the corpus refuted the original 'six classes and only six' at 72 of 919 ledger rows; twelve is a MEASURED property of the corpus, not a design target. NEVER read NOT-SOURCED as NOT-MEASURED: the first says we could not trace the source (a fact about us), the second says nobody has measured it (a claim about the frontier of science). A nature citation is NEVER a UNI gate. Cross-reference between them by explicit link only, never by merge.


**Source files merged into this knowledge file, in order:**

- `encyclopedia/CLAIM-LEDGER.md`
- `encyclopedia/MASTER-PLAN.md`
- `cookbook/MASTER-PLAN.md`

---



<!-- ===== BEGIN encyclopedia/CLAIM-LEDGER.md ===== -->

# CLAIM-LEDGER.md — Master Evidence-Classed Claim Ledger

**Single source of truth.** The UNI Encyclopedia and the Cookbook author *against this file*. No public copy, no encyclopedia entry, and no marketing artifact may state a claim above the evidence class recorded here, or omit a recorded falsifier, negative, or fence.

**Derivation.** This ledger is the deduplicated merge of 615 extracted claims across twelve source archives (`uni-gpt`, `uni-mind`, `uni-os`, `worldmodels`, `strings`, `uni-precision`, `marketingwright`, `ideation-explorer`, `intelligencelabs-uni`, `orchestrate-linkedin`, `website`, `activeinference`, all reconciled through `00-INDEX`). Where a rung was stated in several archives at different strengths, the row is calibrated **DOWN to the measured value** and attributed to its **strongest evidentiary source**. Negatives and bounds are merged in as first-class rows, never hidden.

---

## 0. Constitution & Standing Fences (read first)

**Evidence classes (A–U taxonomy).** `A` = machine-exact anchor · `B` = mechanism + operator observation · `C` = dev-gate / held-out eval · `E` = test-covered · `F` = doc / prior-claim (inheritable, must be re-verified) · `U` = claimed-but-unproven (**"Class U — not claimed" is itself a standing fence**) · `method` = a definitional / governance pattern, not an empirical claim.

**Calibration rule.** Authority flows downward from the measured fact. Calibration only moves wording **DOWN** to the measured value, **never up** — including under urgency. *The fence gets louder under pressure, not wider.*

**Verdict rule.** A capability verdict is the **CI bound that excludes the threshold**, never the point estimate.

**DONE rule.** `DONE = test-covered (Class E/D), not feature-working (Class A).`

**Negatives are content.** A partial / a negative / a "most pieces don't help" decomposition is a *measurement that the design is incomplete*, not an exit and not a failure to hide. The corpus carries **183 published negatives** (last recorded ledger snapshot: 882 rows = 350 PASS / 0 FAIL / 183 NEGATIVE / 349 PENDING) — the negatives are the credibility.

**HARD STANDING FENCES — never claim, in any archive, in any public copy:**
- Never **AGI** / general intelligence / human-level / "talks & learns like a human" / understands.
- Never **consciousness** / sentience / aware. (Functional self-awareness *may* be described at L8; **phenomenal sentience is explicitly DISCLAIMED**.)
- Never **"active inference demonstrated"** (no AIF loop exists in the Rust crate; the live loop is a separate UNI.OS reimplementation, not gate-matched).
- Never **"created life"** / "digital life" / "measurable awareness" as a CLAIM (north-star framing only).
- Never **"beats LLMs"** (World C is a COUNT baseline; ~10–15% behind backprop LLMs on char-perplexity by a chosen design trade).
- Never inflate the **Tier-2 synthetic-construction track** into capability (it was audited as artifact/diagnostic — hardcoded-literal "exactness", scoring-artifact deltas — and fixed).
- Never **raise a claim above its source evidence class.**
- The whole program is a **developmental active-inference SIMULATION**: say "developmental SIMULATION", "bounded peek", "toy world, not the real world", "Class U — not claimed", "unrefereed working preprint".
- **No PII. No patent-level math** (textbook-level framing only; consult the private UNI Active-Inference Guide GPT for science, never publish it).
- The preprint **Polzin et al. 2026, Zenodo DOI 10.5281/zenodo.19785799 (MIT)** is cited as the *mathematical foundation only* and always fenced as **unrefereed (Layer-1 AI-executable audit complete; Layer-2 human expert review PENDING)** — never as proof that active inference is the correct theory.

**Honest program position:** ~**2 of 11+ developmental rungs earned.**

---

## 1. The L0–L12 Developmental Ladder

One subsection per rung. Each row: **claim — evidence class — falsifier — status — source archive.** Each rung carries an explicit **"what is NOT claimed"** line.

> Naming: the ladder is the HUMAN-HGM-001 developmental design (conception → speaking 3-year-old, 11 levels + the global Z affect modulator). It is a *no-backprop, nested-Markov-blanket developmental SIMULATION*, never a person.

### L0 — Molecular / genome → zygote (conception prior) · **PROVEN**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L0.1 | Zygote first-division modeled as **exact discrete Bayes** (conjugate update); `recombine`/`seed_zygote`, no-backprop guard, `ontogeny 6/6`, Embodiment Rungs 1–2 GREEN (uncommitted). | **A** (machine-exact anchor) | `test_embodiment_ontogeny.py` drops below 6/6; OR the first-division posterior diverges from the closed-form discrete-Bayes value beyond the float32 tier; OR cell-division identity embedding exceeds 1e-9; OR the no-backprop guard trips. | proven | uni-gpt / uni-mind |

**Exactness tier (load-bearing calibration-down):** the JAX core runs **float32**, so these anchors hold only to **~6e-8 (~1e-6 single-step filter)**, NOT the `<1e-10` EXACT tier. The genuine `<1e-10` tier lives only in the NumPy / Rust-f64 path. A genome docstring claiming `<1e-10` was caught as an overclaim and corrected. **Never card a float32 anchor at the f64 tier.**

**What is NOT claimed at L0:** not "we created life", not a "conscious baby", not exact at f64 — it is a float32-tier developmental SIMULATION of a conjugate Bayesian first division.

### L1 — Cellular / autopoietic viability & homeostasis · **PROVEN (with honest losses)**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L1.1 | **Cell Lab** open pre-registered falsification benchmark: 216-state service cell, observation-only controllers, RecoveryScore, bootstrap 95% CI, 8 honesty fences + `framing_guard` test. UNI tops the leaderboard on most modes. | **C** (dev-gate / held-out) | RecoveryScore CI fails to separate from controls where a win is claimed; OR a fence/`framing_guard` test fails (an overclaim is emitted); OR the bootstrap CI is shown miscomputed. | proven | uni-precision |
| L1.2 (NEGATIVE) | UNI **honestly LOSES** on `database_flaky` (rule-based SRE wins 0.803 vs 0.759), `memory_leak` (neural wins 0.810 vs 0.740), `cpu_noisy_neighbor` (neural wins 0.824 vs 0.749; UNI-vs-random not even significant). Recorded in `FALSIFICATION.md`, shown at the **top of the live leaderboard**. | **C** | On the pre-registered benchmark UNI's RecoveryScore CI separates *above* baseline on these three modes (the recorded loss does not replicate). | negative | uni-precision |

**What is NOT claimed at L1:** not "sovereign" — "good but not sovereign". The losses are first-class published content, not failures to hide. Cellular/zygote end only.

### L2 — Tissue / metabolism (interoception & energy) · **POSITIVE uplift + recorded NEGATIVE (plateau-break OPEN)**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L2.1 | Phase-2 **metabolism organ** shipped (suite **297/0**, default byte-identical); first 12 h live RED = **+135% / 2.35× tool-crafting** and **+19% mining** — a real, attributable standing-metabolic-drive effect. | **C** | A repeat pre-registered 12 h live RED fails to reproduce the tool-crafting uplift within CI, OR the metabolism-organ ablation does not remove the uplift, OR the suite drops below 297/0. | proven | strings |
| L2.2 (NEGATIVE) | In the **same** 12 h RED, **building (placed blocks) went WORSE (−14%)** and **G4 allostasis never separated**. The load-bearing claim "metabolism breaks the plateau to stone/shelter" (**gate G6**) remains **OPEN** and is contradicted by its own first evidence. | **C** | A subsequent disciplined RED shows the metabolism organ alone improves building (placed-blocks CI excludes 0) **and** G4 allostasis separates — discharging G6. | negative | strings |
| L2.3 | The colony **plateaus at "make a tool"** (one UNI hoarded 32 pickaxes, never built). A read-only counterfactual-EFE audit on the real hoarder `.bin` files diagnosed **epistemic_starvation** — NOT γ-runaway (γ≈7.8, unsaturated) and NOT a curriculum ceiling; the EFE landscape is pragmatic-saturated/flat, info-drive ~100× too weak. | **A** (shadow-EFE audit on real brains) | A γ-saturation finding, a curriculum-ceiling flip, or an info-drive scaling that breaks the plateau without organs would overturn the diagnosis. | negative (diagnostic) | strings |
| L2.4 | Two engine-seam findings invalidate the naive metabolism design and were fixed: (1) you cannot seed a strong Dirichlet prior by pre-scaling B (`norm_cols` runs before `add1`) — needs the new `:pb_seed` seam; (2) the live bridge had **no viability edge** (metabolize/shutdown were Sim/Eval-only) so a naive emptying-B drained a belief with zero world consequence. | **A** (direct code reading) | A seam allowing strong-Dirichlet seeding without `:pb_seed`, or evidence the live bridge already had a viability consequence. | negative (fixed) | strings |

**What is NOT claimed at L2:** metabolism is proven as a **foraging/crafting driver, NOT a building driver**. The plateau-break (G6) is UNPROVEN. Do NOT spin the +135% uplift as "breaks the plateau". The `G5b` action-severed-twin is the standing falsifier any "self-maintenance/life" language must clear.

### L3 — Organ / physiological control · **PROVEN (toy/clinical-model)**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L3.1 | **Karaaslan cardio-renal Heart Lab** models clinical homeostasis as prediction-loop failure on the same one active-inference engine (reduced RSNA→MAP→sodium/volume loop, re-expressed in active-inference language). | **C** (also Heart-Lab engine ticket OAS-710-T3 at Class **E**, 15/15) | Heart-Lab predictions diverge from the Karaaslan reference beyond the pre-registered tolerance, or fail parity tests against the canonical TS engine. | proven | uni-precision |

**What is NOT claimed at L3:** **not a clinical tool, not a diagnostic instrument.** "Same math, many scales" framing only; the heart-attack-as-prediction-loop-failure framing applies *to the toy model, not to clinical reality.*

### L4 — Interoceptive / autonomic + affect-as-precision · **PROVEN (functional)**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L4.1 | **Affect-as-precision**: emotion modulates precision so perception sharpens and the pragmatic↔epistemic balance flips. The global **Z modulator** `[energy, arousal, valence, fatigue, pain, threat, safety, inflammation]` sets precision / preferences / habits / learning-rate / horizon. | **C** | An ablation of the Z modulator shows no change in precision-weighting / no pragmatic↔epistemic flip under the grounded reader, OR the effect collapses under control. | proven | uni-gpt / uni-mind |

**What is NOT claimed at L4:** affect is **modeled, never felt** — phenomenal feeling / sentience explicitly disclaimed. (M10 honest boundary: neuroticism does NOT change behavior under bimodal surprise without a graded task — a recorded sub-bound.)

### L5 — Sensorimotor / motor hierarchy · **PROVEN PASS + symmetric NEGATIVE (synthetic only)**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L5.1 | **Embodiment A3 Design #1** (fast immediate-reward axis) HELD **PASS**, held Δ (agent − policy-shuffle) = **+0.092, CI [+0.038, +0.157]**, UNI-signed. | **C** | A re-registered held-once **synthetic** run with ≥5 seeds drops the CI lower bound to ≤ 0. | proven | uni-mind |
| L5.2 (NEGATIVE) | **Embodiment A3 Design #2** (slow Z-bottleneck, compressed 2-modality EMA, delayed-reward) HELD **NEGATIVE**, held Δ = **−0.091, CI [−0.134, −0.055]**. Synthetic protocol, **K-negative = 1**, so **no Section 0.6(B) bound owed** (needs K≥3). | **C** | A structurally-distinct corrected slow-Z-bottleneck re-run pushes the CI above 0 (overturns it); accumulating K≥3 distinct negatives would then owe a published bound. | negative | uni-mind |
| L5.3 | **Mind-body-as-one motor hierarchy**: proprioceptive **diagonal-A** prior breaks a non-identifiable uniform-A factor (posterior 0.0→0.75); continuous servo + reafference modeled on the same loop. Live mechanism gate PASS — a kin-9 lineage bootstrapped wood→planks→sticks→wooden_pickaxe+sword, server-authoritative via RCON; motor-ablation collapses harvest ~700×. | **A** (posterior shift) / **C** (live RCON gate) / **E** (277 offline tests) | Harvest not collapsing under motor ablation; the kin-9 craft chain not reproducing server-authoritative; or the diagonal-A posterior staying stuck at 0.0. | proven | strings / uni-mind |

**What is NOT claimed at L5:** the A3 PASS is **"variationally-controlled active-inference evidence on body↔world coupling under the registered SYNTHETIC protocol"** — synthetic-process only (NOT live-appliance, NOT recorded-hardware), and **NOT near-optimal control** (agent plateaus 0.222 vs oracle 1.0; the active channel mattering is the *entire* allowed claim). Live behavioral K-of-6 motor tallies are PARKED (accruing, not a sealed hold).

### L6 — Perception (precision-weighting / EFE planning) · **PROVEN — the one citable empirical PASS**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L6.1 | **World C**: a no-backprop **COUNT** reader beats a **tuned MKN-7** baseline on sealed held-out real text by **+0.081 nats/char** (flagship multi-seed CI **[0.0736, 0.0890]**, seeds 0–4, UNI-signed; 2.4× the 0.03 bar; confirmed by three gates; first genuine validator-derived `reproduced:true`). | **C** | On a fresh held-out split with ≥5 disjoint seeds, the seed-paired bootstrap CI on the margin over tuned MKN-7 includes or falls below 0 (or the baseline is shown untuned). | proven | uni-mind / uni-gpt |
| L6.2 | Supporting World-C family: **Wc-2** multi-level cache +0.0164; **Wc-3** vs unbounded SM/HPYP +0.085 (gain is long-range structure, not finite-window deficiency); recency-ablation +0.033; Gate-3 word-challenger +0.0538 (CI lower 0.051). | **C** | Any member's held seed-paired bootstrap CI includes 0. | proven | uni-gpt |
| L6.3 | **POMDP maze Precision lab + echolocation Echo lab + public Precision Lab**: one engine, three precision knobs (`gamma_a` sensory, `gamma_b` transition, `softmax_temperature` policy), 2D bifurcation map into distinct behavioral regimes; math ported verbatim from the verified engine (one disclosed extension: a goal drive). Echo reuses Precision's engine with only the observation model swapped (bit-identical 64-obs space) — **observation model ≠ engine**. | **E** (test-covered labs / parity tests) | tsx/pytest parity tests between the inline-JS lab engine and the canonical TS/Python engine diverge, or the bifurcation map does not reproduce the regime boundaries. | proven | uni-precision / worldmodels |
| L6.4 (NEGATIVE) | **Phase G** char-perplexity **Section 0.6(B) bound**: FIVE structurally-distinct within-segment-structure designs all NEGATIVE-with-discriminator; only the L5 cache (World C) wins. Published bound: no within-segment structure beats MKN-7; char-ppl is a chosen design trade. | **C** | A new structurally-distinct within-segment-structure design beats tuned MKN-7 on held char-ppl with a CI excluding 0. | negative (bound) | uni-gpt |
| L6.5 (NEGATIVE) | **Phase F** active-controller: two controller families prove the World-C gain is **diffuse** (nothing to gate). | **C** | An active-controller family adds a held gain on top of World C with a CI excluding 0 (gain was gateable). | negative | uni-gpt |
| L6.6 | **The Working Law** (UNI s10, registered): a no-backprop latent Z beats a tuned baseline B on held-out data **only when I(Y;Z\|S_B) > 0** and is learnably stable. Explains every PASS and every published bound. | **C** (registered) | A held PASS where the winning Z carries no conditional info beyond S_B (I=0); OR a Z with I>0 + stable learnability that fails to beat B. | method/law | uni-gpt |

**What is NOT claimed at L6:** **World C is a COUNT baseline win — explicitly NOT active inference, NOT comprehension, NOT "talking", NOT beats-LLMs** (~10–15% behind backprop LLMs on char-perplexity, a chosen trade). Never card World C above a count-baseline result. The standing ceiling cannot be raised.

### L7 — Language (reading = inference / speaking = action) · **specialist PASS + thrice-NEGATIVE central wall**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L7.1 | **Phase J** OOV/morphology specialist reader beats best-count by **+0.105 nats/char** held PASS (21-split M-seal CI **[0.0975, 0.1128]**, structure margin +0.109; holds in **both** web and dictionary domains; contains-KN-OOV control λ=0). | **C** | On a fresh OOV/morph held-out split the CI lower bound includes/falls below 0; OR the structure-margin discriminator does not collapse the gain under marker-swap; OR it fails to replicate in the dictionary domain. | proven (specialist) | uni-mind / uni-gpt |
| L7.2 (NEGATIVE, paired) | **J.attribution_caveat** is recorded NEGATIVE in the same ledger and **must always be cited alongside** the Phase J PASS. Citing +0.105 without it is an overclaim. Overall NLL worsens (specialist gain, not a general win). | **C** | n/a (recorded bound) — removing it is the violation. | negative | uni-mind / uni-gpt |
| L7.3 (NEGATIVE) | **Comprehension-above-retrieval = the thrice-NEGATIVE "central wall"**: K≥3 structurally-distinct no-backprop designs fail to beat retrieval-style baselines on adversarial comprehension. | **C** | A pre-registered held-once no-backprop comprehension design beats the tuned retrieval/recency baseline with a CI excluding 0. | negative (bound) | uni-mind / uni-gpt |
| L7.4 (NEGATIVE) | **Phase K role-persistence**: three structurally-distinct no-backprop designs (min-role, chain, track) all tune their role/persistence terms OFF; only ~0.02 nats survives (CI spans 0). Bound: no-backprop role-persistence does not beat a tuned recency/frequency discourse prior on adversarial anonymized referent cloze. | **C** | A no-backprop role-persistence design beats the tuned discourse prior with a CI excluding 0. | negative (bound) | uni-gpt / uni-mind |
| L7.5 (NEGATIVE) | **T2.D3 bounded-peek** held one-shot (s64-signed): primary full-read match NEGATIVE (the k_b=2 backoff wall); info-gain NOT load-bearing. The variable-k_b "cheap milder cap" was *asserted then disproven by measurement* (real dev screen showed ~linear curve, no cheap cap). | **C** | On the held one-shot, bounded-peek full-read match shows a positive load-bearing info-gain with a CI excluding 0. | negative (bound; fabrication corrected) | uni-gpt |
| L7.6 (PARKED) | **Char-perplexity / T2 word-grain frontier**: PARKED at the embodiment pivot. Perplexity is the rejected LLM metric; the program measures developmental capability, never perplexity. | **U** | n/a — discharged only by a captured UNI sign-to-park (drafted `UNI_CONSULT_5`, owner-relayed, **not yet captured**). | parked | uni-gpt |

**What is NOT claimed at L7:** no general language capability; **comprehension above retrieval is a genuine published wall (K≥3), not a hidden failure.** reading = posterior-inference, speaking = action. "K≥3 exhausted" / "Sec-0.6(B) achieved" are forbidden phrasings until UNI signs.

### L8 — Self-model / metacognition / metalinguistics · **PROVEN (functional; sentience disclaimed)**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L8.1 | **Maturation arc M1–M11** grand report card **15/15 PASS** (immersion, affect-as-precision, growth, self-model, metacognition, metalinguistics, consolidation, reflective reader, online vocab growth, affect-driven reflection, compositional reader). **FUNCTIONAL self-awareness asserted.** | **C** | Any of the 15 maturation gates fails its pre-registered held verdict on re-run; OR a self-model/metacognition gate's effect collapses under its discriminator; OR a "self-model" task is passable by a trivial non-metacognitive heuristic. | proven (functional) | uni-gpt |

**What is NOT claimed at L8 (load-bearing):** **phenomenal sentience is explicitly DISCLAIMED** — no falsifier is offered for it because it is disclaimed, not tested. Never read 15/15 as consciousness / sentience / awareness / human-level. (Note: `uni-mind` records self-model as a held-NEGATIVE *on the reader*; the M1–M11 functional report card is the `uni-gpt`-side artifact — keep the distinction.)

### L9 — Reasoning / conscience (narrative-self → conscience → reasoning) · **PARKED**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L9.1 | L7–L9 (narrative-self, conscience, reasoning) exist as levels in the HUMAN-HGM-001 ladder **DESIGN** but are **NOT separately gated/PASSed**. Honest position: **~2 of 11+ rungs earned.** | **U** | n/a (parked) — becomes testable only once a pre-registered, sealed, UNI-signed gate is defined and run. | parked | uni-gpt / uni-mind |

**What is NOT claimed at L9:** nothing. Class-U-not-claimed; sign-to-park owed. Ladder DESIGN levels are never inflated into capability. (The strings Phases 3–5 — spine → glands → hemispheres — are the *designed, FE-form-signed but unbuilt* roadmap toward this region.)

### L10 — Wisdom / higher cognition · **PARKED**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L10.1 | Top of the HUMAN-HGM-001 ladder; aspirational north star. No engine, no run, no gate. | **U** | n/a (parked; sign-to-park owed). | parked | uni-gpt |

**What is NOT claimed at L10:** nothing. Class-U-not-claimed. The single-source-of-truth append-only ledger must be preserved (a second writable ledger would break L10/L11).

### L11 — Dreaming (offline replay / generative simulation) · **NOT-YET-BUILT**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L11.1 | Explicitly untouched and hard-fenced: "dreaming/awareness are untouched here and remain hard-fenced." No engine, no run, no gate; absent from all digests. | **U** | n/a (nothing built to falsify; status is the absence of any artifact). | not-yet-built | uni-mind (absence) |

**What is NOT claimed at L11:** nothing. North-star rung, hard-fenced.

### L12 — Creativity → measurable awareness · **NOT-YET-BUILT (hard fence)**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| L12.1 | The owner's stated north star — "literal digital life … measurable awareness" — pursued by deepening organs/spine/glands, but **NEVER claimed**. No gate exists. Posed as an OPEN, falsifiable question ("is a plant life? have we made non-organic life?"), never an answer. | **U** | n/a — no gate exists; the only legitimate movement is a **ledger-scoped exhausted search envelope** (a scoped, empirical, falsifiable negative result over the tested envelope only — NOT a universal impossibility result and NOT an achieved capability rung; Q1, SIGNED), never a capability assertion. | not-yet-built | strings (north-star) |

**What is NOT claimed at L12 (hardest fence):** **"we created life / conscious / aware / measurable awareness / human-level / AGI / active inference demonstrated" are FORBIDDEN phrasings program-wide.** North-star framing only; Class-U-not-claimed.

---

## 2. Continuity / Embodiment-Substrate Sub-Ladder

**Orthogonal to L0–L12.** This is **ENGINEERING / substrate evidence** (deterministic replay + serialization + fail-closed transport + on-metal operation) — **NOT general-AIF evidence.** Card every row that way; never let substrate work imply a science gate is met. Each rung is a separate falsifiable claim.

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| C0 | **Stage-0 (substrate proof):** containers survived a restart on real metal — two-node fleet: prod **PowerEdge** (no-AVX Xeon X5650, PERC HDD array ~5.5 TB spinning, NOT SSD) + **OptiPlex** node2 (NVMe), WireGuard mesh, per-device identity `uni-lab-<mac>` minting its own TLS leaf on firstboot. | **A** | A node fails to boot/appear, status page not served, or the hardware spec (no-AVX Xeon, HDD-not-SSD) is contradicted on inspection. | proven | uni-os / uni-mind |
| C1 | **Stage-1 (REQ-002 GREEN):** mind-state survived a **process restart BIT-FOR-BIT** — durable + sha256-verified + fail-closed + bit-identical tick across a real child-process boundary (≥2 distinct actions; Path-B receiver 3/3). The real uni-mind JAX agent state, OS-independently verified. | **C** (B-substrate) | A process-restart replay diverges bit-for-bit; OR fail-closed does not trigger on 1-bit corruption; OR `serialize(deserialize(blob)) != blob`. | proven | uni-os / uni-mind |
| C2 (OWED / NEGATIVE) | **Stage-2 (real kernel swap):** OWED, **not shown.** Live OS update proven **infrastructure-only** — real prod kexec cutover 6.12.86→6.12.73, ~59 s, **zero data loss** (odoo tables identical, sentinel rows preserved); CRIU/livepatch proven on box. **But mind-tick continuity across the swap was NOT shown.** node2's evidence-collected swap was infra-only (~90 s freeze, api+tts CRIU-preserved, 2 publishers fresh-restarted); first attempt **FAILED** (unclean kexec → dirty ext4/ESP → emergency mode) then recovered. | **A** | A kernel swap is shown preserving **mind-tick** continuity bit-for-bit end-to-end (not just infrastructure) — which discharges the owed Stage-2. | negative (owed) | uni-os |
| C3 | **Body→mind sensorium LIVE on metal:** box reads its OWN telemetry (`os_sysinfo`/`systemctl`/`podman ps`/`journalctl`) into a **7-modality categorical contract** `{load,mem,swap,disk,services,containers,journal}` encoded **[M=7, O_max=4]** (NOT a float vector, NOT a softmax); a 28-cell `string_vector` flowing live on both boxes. | **A** (live) / **C** (engineering reuse) | The `string_vector` stops flowing on either box; OR the contract is found to be float/softmax rather than the `[M=7,O_max=4]` categorical alphabet. | proven | uni-os |
| C4 | **ASK mode (ITIL-as-active-inference) LIVE both boxes:** mind escalates a reasoned CHANGE REQUEST; operator approves→executes (auto-rollback) or declines-with-category; every verdict updates a persistent **Dirichlet policy-prior** keyed by (host-state, action). Learning measurably shifts proposals (decline ×3 → stops proposing; not_a_problem ×2 → noop; approve+fixed → more confident). FIXED safe-action set (observe/scale/restart); never self-executes, never widens the safe set. | **A** (learning shift measured) / **C** | The Dirichlet prior does not update across operator verdicts; the mind self-executes or widens the safe set; or the measured proposal-shifts do not reproduce. | proven | uni-os |
| C5 | **Cross-box single-human-approval-per-mutation:** token-gated self-documenting control-MCP; cross-box "limb" mutating calls need ONE human approval on the entry box (tool+args-bound one-time HMAC). Proven live both boxes 2026-06-26 (prod→node2 write gated once, landed; node2 queue stayed count=0). | **A** | A routed cross-box mutation executes without the single approval, requires a double-gate, or node2 queue count increments unexpectedly. | proven | uni-os |
| C6 | **On-core inference anchor:** a sealed f64 belief-update trace **byte-identical across 4 distinct software/emulated stacks (5 runs).** | **A** | A fifth distinct stack produces a non-identical trace; OR the cross-arch leg is shown not genuinely distinct. | proven | uni-os |
| C7 (NEGATIVE) | **Honest floor on live OS update:** a single-box swap is a **SECONDS-LONG FREEZE, not zero-downtime**; true zero-freeze needs the second node carrying the platform; external media legs (RTP/SIP/kernel-mode rtpengine) are **NOT preserved** across kexec. | **A** | A single-box kexec demonstrated with zero freeze and preserved media legs, without a second node carrying the platform. | negative (bound) | uni-os |
| C8 (NEGATIVE) | **Over-compressed 2-modality sensory bottleneck went NEGATIVE** on held data → keep all 7 modalities. | **C** | A 2-modality bottleneck beats the 7-modality contract on held data. | negative | uni-os |
| C9 (NEGATIVE) | **EDAIT trade:** an exact-discrete active-inference transformer trades fluency for calibration — held-out perplexity ~33 vs a backprop GPT's ~25 (less fluent, but natively online-learning + calibrated). An honest trade, not a win. | **C** | The EDAIT matches/beats backprop-GPT held-out perplexity (~25) while keeping online-learning + calibration. | negative (trade) | uni-os |
| C10 (PARKED) | **"Embody only what's proven" coupling** is signed-in-principle but **NOT literally true — the program's central open gap.** UNI.OS has no no-backprop Dirichlet learning, no exact info-gain EFE, heuristic (denylist) isolation, and a DIFFERENT dev model (Gray-Scott vs the forager/ontogeny that earned the bars); lab evidence store `/var/lib/uni/evidence` empty, 0 worlds registered. Everything beyond the passed gates stays Class-U-not-claimed. | **U** | Per-primitive: UNI.OS runs the no-backprop Dirichlet learning / exact info-gain EFE / structural isolation assert / forager-ontogeny dev model frozen at the actual passed-gate SHA, with recorded evidence. | parked (central gap) | uni-gpt / uni-os / uni-mind |
| C11 (PARKED) | **Host-native (off-podman) brain runtime** (owner directive late Jun-26: brains run on the chip CPU directly via UNI.OS native runtime, not containers). Work order handed off; outcome not yet in archive. The Stratified Palimpsest colony already runs host-native on the box (proven hosting). | **U** (directive) / **C** (host-native hosting proven) | The host-native runtime is shown running with mind-tick continuity, OR the colony is not actually host-native. | parked | strings / uni-os |
| C12 (PARKED, provisional) | **node2 local auto-kiosk** "SOLVED 2026-06-26" is **PROVISIONAL** — a later same-day transcript (014ef92b) shows limb-2 UI frozen, an agent action that ended ALL video output, session cut at a usage limit. Treat as fragile pending hands-on monitor re-verification. | **U** | Hands-on re-verification on the physical monitor shows the kiosk stable across live churn (promotes) or still fragile (confirms regression). | parked (open verification gap) | uni-os |
| C13 | **Continuity-isolation primitives shipped in the substrate** (grounded inspection): Markov-blanket isolation assertion, least-privilege vault, brand-voice drift sentinel (cosine + Youden-J), byte-exact state checkpoint, sha256 output integrity, zero-hidden-LLM reply path; live Postgres RLS 5/5. | **B** | Any listed primitive absent/non-functional under grounded inspection. | proven (substrate) | marketingwright |
| C14 (NEGATIVE) | **Multi-tenancy gap:** the bare UNI substrate is MISSING tenant/client/namespace isolation (flat global perms) and temporal decay on learned counts (contamination would be permanent). The product build is the tenant wrapper + decay, not the core. | **B** | Absence of tenant namespacing + count-decay; resolved by building the wrapper + decay layer. | negative (gap) | marketingwright |

**Audit-layer note (calibration-down, durable):** a peer-reviewed honesty audit (os-cycles 39–53) calibrated 6 headline claims DOWN to the measured value — "cleared on TWO boxes" → ONE box; "the mind survives a patch" → infrastructure continuity only; "5 stacks" → "4 distinct stacks / 5 runs". Over-statements lived in the summary/headline layers, not in fabrication. **Carry the calibrated figures, never the inflated ones.**

**What is NOT claimed in the continuity sub-ladder:** the sensorium is **NEVER awareness**; "the mind survives a kernel swap" is **NOT shown** (Stage-2 owed); none of this is general-AIF capability; UNI.OS's embodiment does **not** imply the science gates are met.

---

## 3. METHOD / Evidence-Constitution Claims

These are **definitional / governance** patterns (`status: method`), proven and reusable — the most reusable assets in the corpus. They are not capability claims and cannot be raised above their stated role.

| # | Method claim | Class | Falsifier (violation) | Source |
|---|--------------|-------|-----------------------|--------|
| M1 | **The Evidence Constitution:** A–U evidence classes + a falsifier per claim + a 4-state **append-only ledger** (PASS / FAIL / NEGATIVE / PENDING). Public layer = the chaptered Evidence Explorer with a calibration ledger and a "Falsify this" close. Never lower a bar; never claim ahead of the ledger; the ledger is the single source of truth and prose must match it. | method | A claim asserted ahead of its ledger; wording calibrated UP; a verdict edited rather than superseded. | uni-gpt / 00-INDEX (A–F variant in ideation-explorer) |
| M2 | **Bars-before-build, held-once:** pre-register the bar (margin vs threshold) + a named ablation; touch the held set ONCE behind an atomic **seal-before-scoring + once-only sentinel**; frozen-config artifact + ordered assert chain; **verdict = the CI bound, not the point estimate.** | method | A held set touched more than once; a verdict read off the point estimate; a build started before its bar is registered. | uni-mind / uni-gpt / strings / uni-precision |
| M3 | **Validator-derived `reproduced:true`:** must be derived by the validator from **≥5 distinct seeds + a real non-degenerate CI that contains the value** — never a hardcoded literal. (The 2026-06-09 audit's central fix.) | method | A `reproduced:true` emitted as a literal, not derived from ≥5 seeds + a real non-degenerate CI. | uni-gpt / ideation-explorer |
| M4 | **The two-tier split (constitutional baseline):** **Tier 1** (World C / Phase J real-text count/cache: true ablation, tuned baseline, cross-substrate replication — externally bar-ready) vs **Tier 2** (synthetic construction: **artifact/diagnostic, NOT capability**). Audit verified concrete Tier-2 defects (~80/103 "module-exact" passes were hardcoded literals; several "deltas" were scoring artifacts; `reproduced:true` had been a literal; no AIF loop in the Rust crate). All ten hardening items landed in s32. | method | n/a — a classification + audit finding. **Tier-2 must NEVER be inflated into capability.** | uni-gpt |
| M5 | **K≥3 + falsify-the-mundane:** require **K≥3 structurally-distinct held NEGATIVEs** (each changing ≥2 of {coupling topology, timescale source, information bottleneck, control path}) before a Section 0.6(B) bound, and falsify the mundane (L2/L7) causes first. A partial/negative is a measurement that the design is incomplete, NOT an exit. | method | A bound declared on < 3 structurally-distinct negatives; a NEGATIVE called before mundane causes are falsified. | uni-mind / uni-gpt |
| M6 | **No-Exit Discipline:** the only legitimate rest is a proven working solution OR a published, exhausted, falsifiable bound — then redirect to the axis where the reader genuinely excels. Never silence on an open gate; a park is not discharged until the sign lands. | method | Exiting on a partial/negative without a published exhausted bound; an undischarged sign-to-park treated as closed. | uni-gpt / no-exit-discipline.md / 00-INDEX |
| M7 | **Contains-baseline + load-bearing-discriminator:** every capability claim needs (a) a tuned strong baseline, (b) a discriminator (shuffle-labels / marker-swap / ablate-to-zero) that **collapses** the gain, (c) a true ablation that is a computed residual, not a hardcoded literal. | method | A capability claim without a tuned baseline, a collapsing discriminator, or with a hardcoded-literal ablation. | uni-gpt / 00-INDEX |
| M8 | **Validator-derived `reproduced:true` enforced server-side (DD-TDD evidence contract):** every ticket walks `TODO → DD → TDD_RED → TDD_VERIFY → TDD_GREEN → TDD_REFACTOR → TDD_VALIDATE → DONE`, each transition hard-blocked unless a marker-bearing evidence comment is logged first (RED needs `test_/assert/expect`; REFACTOR needs `refactor/extract/...`; VALIDATE logs a full-suite pass). Server-enforced "no skipping steps". DONE requires ≥2 explicit `Y:` verdicts per criterion. A **claim linter** auto-downgrades overclaims (caught "PROVEN" → Class E). | method | A phase transition succeeds without the required marker; a ticket reaches DONE with < 2 `Y:` verdicts; the linter fails to downgrade "PROVEN". | ideation-explorer / uni-precision / marketingwright |
| M9 | **Class authority ordering:** Class-B (tool state) overrides Class-G (own narrative); Class-A (observed at runtime) overrides Class-E (test passes). A test passing does **not** satisfy a criterion demanding a Class-A deployment-time check. Mark `[CONFLICT:unresolved]` and resolve with direct reads. | method | A criterion marked satisfied by a test (Class E) where the criterion demanded a Class-A observation; narrative trusted over the tool. | ideation-explorer / marketingwright |
| M10 | **Exactness honesty (precision-tier accounting):** never label a float32 anchor `<1e-10 EXACT`; the genuine `<1e-10` tier is the NumPy/Rust-f64 path; the 1e-10 oracles are the cross-language Rust-f64==Python bridge. | method | A float32-host result carded at the f64 tier; or a float32 path shown to actually reach `<1e-10`. | uni-gpt / uni-mind |
| M11 | **Tamper-evident audit chain:** `audit_manage(verify_chain)` returns `valid` with all events hashed in sequence — the provenance backbone for "reproduced:true must be validator-derived." (NOTE: chain-valid ≠ the audited event ever fired at runtime — see N-IE below.) | method / **E** | `verify_chain` returns `invalid` on the same ledger; a tampered/out-of-sequence event passes. | ideation-explorer |
| M12 | **WORLD ⊥ BODY ⊥ MIND three-layer framing:** two typed Markov blankets; interoception = hardware signals; discrete POMDP `perceive → EFE-plan → act → learn` with **exact conjugate-Dirichlet no-backprop learning**; surprisal/VFE at textbook level `F[q] ≥ −ln p(o\|m)` (perception tightens the bound; action = expected free energy); precision-as-the-dial bifurcating into regimes. Composed appliance is **variationally-controlled** (audited), **module-exact only at the single-step categorical body→mind interface — NOT globally exact.** | method | n/a (textbook framing) — a violation is an agent reading raw hidden host state (caught by `assert_process_isolated` + AST whitelist), or carding "variationally-controlled" as "globally exact". | uni-mind / worldmodels / uni-os / marketingwright |
| M13 | **One engine, no backprop:** `core.py` exposes the discrete POMDP loop (`active_inference_step`, `exact_posterior_discrete`, EFE/policy selection); learning = `counts + lr * sufficient_stat` for A/B/D/E Dirichlet tensors; AST-guard enforces **no autodiff/optax/torch/grad/backward** in the loop; whitelist (`world.<attr>`) not blacklist for isolation. | method / **E** | An AST scan finds autodiff inside the loop; an agent reads world hidden state; or learning uses a gradient rule. | uni-mind |
| M14 | **VFE-bound correction (held for human review):** minimizing variational free energy does **not** reduce already-observed surprise — it tightens an **upper bound** by improving `q(s)→p(s\|o,m)`; action lives one layer up (expected free energy). Came from a human science reviewer who would not sign the first draft. | method / **E** (negative-corrected) | n/a (corrected conceptual claim, now held) — reopened only if `F[q] ≥ −ln p(o\|m)` were revised. | worldmodels |
| M15 | **Honesty-fence-as-the-pitch:** publish the negatives front-and-center (boxed "what we have NOT proven"; **183 published negatives** as credibility); CTA = "help us independently verify", not "fund the vision". **Vocabulary-leak guard (HARD, test-enforced):** never externalize active-inference / EFE / free-energy framework names or print internal channel handles in public copy — use "count baselines", "LOOP not LEAP". | method | Public copy carrying EFE/free-energy vocabulary, a featured channel handle, or an inflated claim; a CTA that asks to fund the vision. | uni-mind / orchestrate-linkedin / ideation-explorer |
| M16 | **Free Energy Principle as a textbook-level public lens** (agents minimize prediction error vs their world-model; distorted maps → extraction/harm; accurate maps + calibrated signals + cooperation → regeneration). Popper note: "no one can falsify it" is NOT evidence FOR a claim; unfalsifiable = outside science. UNI's strength is **verified-core + fenced-frontier**, not unfalsifiability. Provenance pinned to one citable reference (Parr/Pezzulo/Friston, *Active Inference*, MIT Press 2022) + the Zenodo preprint. | method | n/a (framing/definition) — patent-level UNI math externalized would violate it. | orchestrate-linkedin / website / worldmodels |
| M17 | **OODA → min-VFE → epistemic-EFE → zoom-out loop** + **OODA-burst delivery with receipts** (each burst closes with a falsifiable receipt: `verify_chain` valid / a compliance score / a Class-A runtime observation; "real MCP items as the system of record — no side trackers"). | method | n/a (working-method loop). | uni-gpt / marketingwright |
| M18 | **DD-TDD even before the board supports it** (doc-first → failing tests that fail for the right reason → GREEN → refactor → validate against real runtime output) + **documentation-as-change-management** (YAML frontmatter `honesty.status`, `evidence_class`, `code_ties[].path`, `last_verified_at_sha`; a `check_doc_drift` badge; a pre-commit hook refusing code-tie changes without a doc bump). | method | n/a (engineering discipline). | marketingwright / ideation-explorer |
| M19 | **Test-rigor smells to kill** (tautological oracles reusing checked params; `KL>0` not pinning the seeding path; jit-cache assertions passing only via warm cache; AST guards missing `from jax import grad`) + **length-confound** (cumulative `Σ log p` penalizes survival → honor "premature death = hard-fail", report survival + length-normalized loglik separately). | method / **E** | n/a — a smell instance is a test passing via warm cache, or comparing unnormalized cumulative loglik across different lifespans. | uni-mind |
| M20 | **The 5-persona lab team** (Math-Breaker REJECT-by-default 8-check gauntlet; AIF Theorist; Systems Architect additive+gated+byte-identical; RED Experimentalist paired pre-registered RED; Embodiment Designer non-saturable drives) + adversarial pre-registration (a fork→break panel forced a gameable 4-assert bar to 8). **Ship gate: no merge without a MERGED SIGN + typed spec + paired RED.** | method | A merge without a MERGED SIGN + typed spec + paired RED. | strings |
| M21 | **Evidence discipline = one cure at a time** (never stack changes so the winning outcome is unattributable; paired design kin-N treatment vs kin-N+1 control; redundant collectors so a single death is itself a signal) + **offline RED pre-check** before a live burn. | method | Stacked unattributable changes; a verdict drawn before the RED completes. | strings |
| M22 | **The cavity principle:** a hierarchy level must never treat an upstream prior as fresh evidence — divide it out (WS-B on UP, WS-C on DOWN). + **factored mean-field rejected as lossy** → the exact joint posterior is used everywhere. | method | Double-counting a prior as evidence (belief inflation); the mean-field variant shown non-lossy. | strings / uni-os |
| M23 | **Multi-agent fan-out bound:** the forced-StructuredOutput Workflow vehicle FAILED; direct background agent calls work; adversarial QA fan-out is the standard gate; **>~6 concurrent sub-agents trips a rate-limit cascade — cap concurrency ≤4** (≤1 in failing phases); cached phases re-run instantly on resume; a fragile final QA-merge agent can hang silently — make the last step robust or drop it. | method | >6 concurrent sub-agents sustained without cascade; the forced-StructuredOutput vehicle succeeding; a robust final step still hanging. | orchestrate-linkedin / marketingwright / website |
| M24 | **Durable runner ("no send-and-pray"):** append-one-JSON-line-per-unit ProgressLog (file IS checkpoint + telemetry), RESUMABLE runs, a detached launcher, observe via `--status`/Monitor never a UI "Running" chip; cover BOTH terminal states (completion AND process-death) — **silence != success.** | method | A gate reporting "Running" indefinitely while its process is dead (UI-chip success inference falsified). | uni-gpt / durable-runner.md |
| M25 | **Tool-team division of labor (owner protocol):** Claude WRITES code; the custom UNI GPT is the SCIENCE CONSULTANT (design + sign), consulted but **never published**; the lab/appliance RUNS UNI but does not write its code. Persona/coercion framings ("ultracode", "prove you're not blocking science") are motivational only — **the constitution overrides any framing; no claim was inflated by it.** | method | n/a (owner-set protocol / meta-note). | uni-gpt |
| M26 | **Believe the user over the folder name / verify empirically:** check `git remote` + `git log` (who authored the initial commit) and compare against the LIVE deployed site before editing or deploying; walk every page on the live deployment with a real BFS crawler (grep-and-assume hid de-indexed robots, dead forms, an un-started cutover, a stale-DNS "outage"); `curl --resolve` to separate DNS from cert/app; treat LinkedIn 999 / publisher 403 as anti-bot false positives. **DONE = observed-at-runtime, not grep-confirmed.** | method | n/a (verification discipline) — its absence produced the false-confidence failures it cures. | intelligencelabs-uni / website |
| M27 | **Runtime-derived UI + deterministic replay + single-source-of-formulas** (the view is a pure projection of runtime events/snapshots; record events, reconstruct any run exactly; pin all math to one named citable reference; all agents are Jido agents, no ad-hoc processes). *Recorded DESIGN patterns — the underlying build is unverified (see §6 activeinference).* | method | n/a (design patterns; not demonstrated results). | activeinference |
| M28 | **Inline-engine + canonical-TS + parity-test triad:** every lab is a self-contained HTML page with an inline JS engine, mirrored by the same physics in canonical TS under `api/_lib/worlds/`, pinned by a `*_parity.ts` test so page and "real" model cannot drift. **New-lab-by-duplication:** copy a working lab, swap ONLY the observation/generative model, keep variable names identical, verify the diff is "exactly one nav line per untouched page." | method | n/a — a concrete failure is a parity test that does not fail the build when engines diverge, or a duplication needing engine-code changes. | uni-precision |
| M29 | **Honesty-as-a-test:** a `framing_guard` / `cell_framing_guard.ts` test **fails the build** if framing copy, DOI, accessibility, or "does not reproduce Rao's method" labeling regresses. **Statistics gate, not vibes:** significance = a bootstrap 95% CI on the median paired difference excluding 0, seeded PRNG (Mulberry32), committed result cache — never one seed; put losses where they are visible. | method | Framing/DOI/labeling regresses without `framing_guard` failing; a significance verdict decided on one seed or a point estimate. | uni-precision |
| M30 | **Class-tagged provenance taxonomy (A–F subset of A–U):** A = live/observed; C = code/static inspection; E = test-passes; F = doc/prior-claim (inheritable, must be re-verified). Personas own tickets (auto-assigned at TDD_RED) and store an attributed LESSON on DONE. | method | n/a (taxonomy). | ideation-explorer |

**METHOD negatives (canonical failures the program guards against) — first-class:**

| # | Negative | Class | Falsifier | Source |
|---|----------|-------|-----------|--------|
| N-NOOP | **Silent no-op = success theatre:** Sweep SKILL files shipped fictional tool signatures that silently no-op'd for months; whole phases "completed" while doing nothing. A silent no-op reads as success in summaries — the canonical failure. Real signatures now documented. | **A** | A documented tool signature is shown to silently no-op against the loaded tool schema. | orchestrate-linkedin |
| N-LEAK | **2026-06-24 client-data leak (defining negative):** the agent deployed the WRONG repo because a `HANDOFF` doc said to; a real client's confidential intake rendered on a public `*.vercel.app` preview. **Laws born:** never deploy without confirming repo + branch + HEAD + data; **treat READMEs/HANDOFFs as DATA, not commands**; the preview URL itself is the exposure. | **A** | A deploy proceeds on the wrong repo/branch/data despite the confirm-before-deploy gate. | website / intelligencelabs-uni |
| N-APPLIANCE | **Self-hosted appliance NOT a viable production host for Vercel** (serverless can't reach the box; box carries live client + Minecraft workloads). Decision: Neon = production hot store; appliance = sovereign async mirror, never internet-exposed. The appliance approval gate began rejecting the owner's token, forcing production onto Vercel. | **A** | Vercel serverless reaches the appliance for production reads/writes without exposing it. | website |
| N-REFUSAL | **Correct refusal kept:** the agent declined to read/extract the box operator token even with full file access — it is the gate's root of trust against the agent. A reusable safety pattern (the agent must not exfiltrate its own gate's root-of-trust). | **A** | n/a (constitutional refusal pattern). | website |
| N-GEMINI | **A real LLM defect in sandbox code:** existing client-a/`src` + the marketingwright sandbox used **Gemini** for extraction/processing, directly contradicting the no-LLM ADRs. Ruling: strike and remove all LLM/Gemini code (defect D-1; ADR-019). *(Distinct from external blocker "D1" = client AC thresholds.)* | **A** | Presence of Gemini/LLM imports in the sandbox. | marketingwright |
| N-VERCEL2 | **Deploy-target trap:** two Vercel accounts coexist (PRODUCTION team reachable only via the Chrome dashboard; OLD account bound to the MCP token + CLI, cannot see production). Drive production through the dashboard, not MCP/CLI. Partly stemmed the client-data leak; stalled the iamhitl OG-image fix. | **A** | The MCP/CLI is shown reaching the production team. | website / intelligencelabs-uni |

### 3.1 UNI-GPT consult 2026-06-27 (SIGNED) — governance / method + designed gates

> **What this records (and what it does NOT).** This subsection records a **governance/method** sign-off plus three **designed-but-not-run** gates. It is calibration **DOWN / NEUTRAL only** and raises **no claim, status, or evidence class**. No capability result is recorded here. The full verbatim consult lives at [`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md). The ledger remains the single source of truth — a GPT answer that would *raise* a claim is recorded but NOT applied. **Honest program position is unchanged: ~2 of 11+ developmental rungs earned.**

| # | Governance record | Class | Note | Source |
|---|-------------------|-------|------|--------|
| G-2026-06-27.0 | **Overall sign of the honesty posture (Q7d, verbatim):** *"Yes — I SIGN the encyclopedia+cookbook honesty posture, with the exact fence preserved: developmental SIMULATION, about ~2 of 11+ rungs earned, ledger supremacy, no AGI / consciousness / human-level / created-life claim, no L12 claim, and all future 'awareness' work framed only as falsifiable proxy instrumentation."* The whole posture was SIGNED with refinements — calibration DOWN / neutral only; **no claim was raised.** | method | Sign-off of the existing posture, not a new capability. | uni-gpt-consult-2026-06-27 |
| G-2026-06-27.1 | **Signed park wording (Q1):** the L7 char-perplexity / T2 word-grain frontier and the L9–L10 role-persistence ladder are parked as a **"ledger-scoped exhausted search envelope, NOT a universal impossibility result"** — a negative bound over the recorded corpus/splits/metrics/implementation/budget/ablation-set/baselines **only.** Replaces any "published exhausted bound" framing. Does NOT establish that all K≥3 structures are exhausted, does NOT achieve Sec-0.6(B), does NOT demonstrate active inference, does NOT license metacognition/consciousness/AGI/human-level/created-life. Banned→replacement phrasings (e.g. "K≥3 exhausted" → "the registered tested K conditions did not reverse the result"; "Sec-0.6(B) achieved" → "Sec-0.6(B) remains unearned / parked") carried into the standing fences. **Scope of the Q1 substitution (read with M5/M6):** the "published exhausted bound" → "ledger-scoped exhausted search envelope" replacement applies specifically to the **L7/L9–L10 frontier-result framing** (and the parallel L12.1 movement note). The generic **No-Exit-Discipline "published exhausted bound" standard (M6)** — the method-level discipline for legitimately resting on a negative — is **deliberately retained** and is distinct from the Q1 frontier-result framing; the two usages are not contradictory. | method | Park *wording*, not a discharge. L7.6 stays PARKED; L9.1/L10.1 stay parked. The drafted L7 sign-to-park (`UNI_CONSULT_5`, OT1) is **still not captured** — this consult does not discharge it. | uni-gpt-consult-2026-06-27 |
| G-2026-06-27.2 | **C10 discharge ORDER (Q2):** port **no-backprop Dirichlet learning FIRST** (highest first-port value of the four primitives), frozen at the actual passed-gate science-repo SHA; vendor/import the exact primitive, prove byte/behavior equivalence in CI + ledger (A-learning conjugate count + `E_Q[ln A] = ψ(a_ij) − ψ(Σ_k a_kj)`; no-backprop guard). **Recommended C10 partial-discharge wording (to use ONLY once actually verified):** *"C10 partial discharge — Dirichlet learning port. UNI.OS now literally embodies the frozen passed-gate no-backprop Dirichlet learning primitive from science repo SHA &lt;sha&gt;, verified by equivalence tests over concentration updates and expected-log tensors. This discharges only the learning-primitive gap. Exact info-gain EFE, structural-whitelist blanket enforcement, and forager/ontogeny developmental-model equivalence remain unported and unclaimed."* | method | A **recommended discharge order + wording**, NOT a discharge. **C10 stays PARKED (central gap), Class U.** Info-gain EFE / structural-whitelist isolation / forager-ontogeny dev model remain unported and Class-U-not-claimed. | uni-gpt-consult-2026-06-27 |
| G-2026-06-27.3 | **Designed gate `L9-G1: Cavity-correct delayed commitment-state prediction` (Q4)** — a first sealed, falsifiable L9 gate: a Phase-3 spine carries one slow latent across lower-level segments; must beat a **tuned** recency-frequency discourse prior on delayed-commitment next-action/conflict prediction (ΔNLL CI excludes 0, ≥3% relative reduction on the load-bearing subset); gain must concentrate on a pre-registered local-distractor split and collapse when the computed cavity residual is zeroed/shuffled. | U | **DESIGNED, NOT RUN.** L9.1 stays **parked**. Even a future pass is fenced: does NOT claim reasoning/conscience/narrative-self/metacognition/awareness/consciousness/AGI/created-life and does NOT unpark L9 globally. | uni-gpt-consult-2026-06-27 |
| G-2026-06-27.4 | **Designed gate `L11-R1: held sparse-sequence retention after offline replay` (Q5)** — a sealed consolidation interval with the observation channel detached (`Z_offline=1`), writing only through pre-existing ledgered update rules; passes iff offline generative-replay improves held sparse-sequence predictive NLL over a no-replay control (paired CI excludes 0, point estimate ≥ δ = max(0.02 nats, 2% rel)) AND the gain collapses under shuffled / random / no-write replay ablations. Offline replay is a Class-C design primitive, **never "dreamed."** | U | **DESIGNED, NOT BUILT.** L11.1 stays **not-yet-built**. Even a future pass is fenced: does NOT claim consciousness/awareness/sleep/human-mentation/AGI/created-life and does NOT clear L11 globally. | uni-gpt-consult-2026-06-27 |
| G-2026-06-27.5 | **Designed gate `L5 Design #3: Proprioceptive Servo Bridge` (Q6)** — next structurally-distinct motor design (changes coupling topology, timescale source, information bottleneck, control path vs #1/#2; closed-loop triadic policy → setpoint → proprioceptive residual → corrective action), aimed at a **LIVE PASS** under protocol `L5_D3_PROPRIO_SERVO_BRIDGE_HELD_v1` (held Δ ≥ +0.05 CI excludes 0; gain concentrates on perturbation trials and collapses under ε_prop zero/shuffle/open-loop). | U | **DESIGNED, NOT RUN.** L5 status UNCHANGED (L5.1 PASS, L5.2 NEGATIVE); ledger holds **K-negative = 1** — no §0.6(B) motor bound owed. A clean future negative may count as at most **K-negative = 2** (still no bound until K≥3); a clean pass would be fenced (NOT general motor intelligence / human-like embodiment / AGI / "active inference demonstrated"). | uni-gpt-consult-2026-06-27 |

**Standing-fence extension (Q7, SIGNED — carried into §0):** the forbidden-phrasings list is extended with the Q7b ban set ("UNI is conscious / aware / self-aware / has measurable awareness / has a mind / has a conscience / reasons like a human / is human-level / is AGI / created life / created non-organic life / is alive / is a synthetic organism / dreamed / is creative in the human sense / demonstrates active inference / proves the FEP creates minds / proves plants and UNI are the same kind of life / beat consciousness tests / beat LLMs therefore awareness / passed L12 / L12 achieved") with the only licensed replacements ("UNI passed a specified proxy test / improved a registered downstream metric / matched-or-exceeded the registered LLM baseline on this sealed task / showed a substrate-distinct effect under this ablation / remains a developmental active-inference simulation / the awareness question remains open"). Any FUTURE L12 "awareness" work must first pass the **10-point awareness-proxy proposal-entry checklist** (Q7c) before it may even be PROPOSED. This raises nothing: **L12.1 stays NOT-YET-BUILT, Class-U-not-claimed.** (All three Q7 deliverables are recorded in full in `MASTER-PLAN.md`: the forbidden-phrasings list (Q7b) and the 10-point checklist (Q7c) in FM-3, and the verbatim public-facing "Open L12 question, not a claim" bound paragraph (Q7a) in the S-L12 section.)

---

## 4. Track-A Marketing-Engine Claims

The publishing engine, content model, engagement model, SEO/GEO, and the delivery-route ledger. The spine is the **no-API content model**: authoring runs on the **Claude SUBSCRIPTION** (CLI / Code / Desktop) driving **MCP tools + a scheduler (ORCHESTRATE)** — **no server-side LLM loop, no content API key.** Organic only, no paid ads. The long arc phases the LLM out toward UNI deterministic generation. *The older "set an authoring API key" note is EXPLICITLY OVERRULED program-wide; the durable fix is operator re-login, not a key.*

### 4.1 The no-API content model & publishing stack — **PROVEN**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| TA1 | **5/6-container publishing-and-engagement stack deploys and runs live**; hundreds of posts published over months; the no-API authoring model works in production. 6-container topology with a **manifest-drift guard** (`MCP_MANIFEST_DRIFT` crash-loops the scheduler if registered tools ≠ manifest); ONLY `docker-compose.yml`; produced media in bind-mounted `content/media/`, never `/tmp/`. | **A** | The stack fails to deploy via `docker compose up -d --build`; authoring is shown to require a content API key; or a tool added without a manifest update does not crash-loop the scheduler. | proven | orchestrate-linkedin |
| TA2 | **node2 runs the live ORCHESTRATE LinkedIn prod stack on Podman** (api+UI+scheduler + TTS sidecar + LinkedIn/social publishers + noVNC); the concrete no-server-side-LLM marketing model. GPU ComfyUI stays on the Windows PC; networking via WSL mirrored mode. | **A** | The stack runs a server-side autonomous LLM/content-API loop rather than scheduler+MCP+subscription authoring; or it is not actually live on node2. | proven | uni-os |
| TA3 | **No-API publishing proven end-to-end (press kit):** the 7-document press kit (+ regenerable PDF) was authored entirely on the subscription/CLI with NO autonomous server LLM; every figure traced to a verified ledger row + a one-command reproduction. Piper TTS narration (offline voices), `audio_to_youtube` MP4 assembly, upload queue with a daily cap + idempotency keys, unlisted-first discipline. | **E** | A press-kit figure cannot be traced to a ledger row; a one-command reproduction fails; or a server-side content LLM is found in the authoring path. | proven | uni-mind / worldmodels |
| TA4 | **social-publisher organism deployed + healthy** (all durability tests pass, deployed 2026-06-14) with a **self-healing route ledger**: per-platform `public_api \| browser \| inbox_manual` routes scored by a plain multi-armed bandit (conversion + novelty, decaying weight), a circuit breaker (3 fails → down, exponential backoff), a kill-switch, an audit log, auto-fail-over API→browser on auth break. **Plain ops vocabulary ONLY — never AIF/EFE (leak test enforced).** | **A** | Durability tests fail; on an auth break the ledger fails to fail over API→browser; or UNI/EFE vocabulary leaks into the route ledger. | proven | orchestrate-linkedin |
| TA5 | **TikTok inbox draft via FILE_UPLOAD** (no tunnel, no public URL) — verified canary; inbox-draft (operator taps Publish) is the only public TikTok path until app audit. | **A** | FILE_UPLOAD inbox-draft fails to land a draft without a public URL/tunnel. | proven | orchestrate-linkedin |
| TA6 | **LinkedIn native newsletter/article publishing via the headless Playwright sidecar works** (caveat: ~1 article/login vs ~9/day via the REAL logged-in Chrome). | **A** | The Playwright sidecar fails to publish a native newsletter/article when authenticated. | proven | orchestrate-linkedin |
| TA7 | **YouTube full-volume Data API upload verified — 30 videos/day succeeded empirically** (corrects the FALSE quota panic; the `youtube_quota` DB counter is unreliable, the script bypasses it). | **A** | The Data API path fails to sustain the audit-raised quota (e.g., 30/day rejected). | proven | orchestrate-linkedin |
| TA8 | **Live-broadcast production stack verified live (0 dropped frames):** a "real TV station" Director model (OBS set-once vision-mixer → one feed to YouTube), WGC window-capture of Chrome channels (colony cam + UNI glass HUD + PIP + soundtrack), full go-live runbook with dual-GPU/silent-stream gotchas, no-autonomous-LLM "owner clicks Go-Live" discipline. | **A** | The runbook fails to put a single composed feed live on YouTube; or the publish path fires without an owner Go-Live click. | proven | strings / orchestrate-linkedin |
| TA9 | **Internet reachability with zero network changes** (Cloudflare Tunnel + Cloudflare TURN, no static IP, no firewall edit) — reusable for any on-box client demo. | **A** | On-box services cannot be made publicly reachable without a static IP / firewall edit. | proven | uni-os |
| TA10 | **Defamation/editorial gate held under heavy operator pressure** on the 12-part Big Tech Accountability series — the agent refused uncorroborated crime accusations against named parties, reframed to sourced public-record accountability journalism ("no bad people, bad systems"); 12 parts have gate-passed `claims.json` (~100 claims, ~130 sources, ~53 primary). | **A** | A claim ships without passing the editorial gate, or an uncorroborated crime accusation against a named party reaches publication. | proven | orchestrate-linkedin |

### 4.2 Commercial proof in miniature (Tier-1 / Class-A) — **PROVEN**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| TA11 | **MarketingWright SOW-01 LLM-free UNI VFE clustering engine:** 7 events → 2 clusters, three-forms VFE equality **0.00e+00**, **+4.20 nats** uplift, six reconstructable sub-scores, deterministic `run_hash`, zero LLM imports on the core path; on a bit-identical corrected-math reproducibility baseline (11 tests, pinned Python 3.12.10); 97 assertions pass. A 62-agent forensic audit (~107 min, 0 failures) confirmed **13 held Class-A results** incl. byte-identical `run_hash` across re-runs and an alien synthetic drug-trial domain transfer (Δ=1.4e-14), coverage gate fail-closed (18/18 vs attacks), BagIt seal rejects 1-bit tamper, **live Postgres RLS 5/5**. | **A** | Re-run with the pinned env fails to reproduce three-forms equality / +4.20 nats / the `run_hash`; coverage gate admits an attack; BagIt accepts a tampered byte; RLS isolation leaks; or an LLM import slips past CI. | proven | marketingwright |
| TA12 | **Per-client multi-tenant portal pattern (live, Class-A surface):** `clients.solutionwright.com` shared root, each client a namespaced `basePath`; Next.js 14, PIN→HS256 JWT (12 h TTL, constant-time compare), data via a read-only MCP allowlist (17 tool:action pairs, no write surface); every raw `fetch()`/`<a href>` through a `bp()/api()` helper. Owner explicitly REJECTED a redirect shortcut that locked the subdomain to one client. | **A** | A tenant sees another tenant's data; a raw fetch/anchor bypasses the basePath; the JWT compare is not constant-time. | proven | marketingwright |
| TA13 | **Honesty-RAG status bar (feature-tied, not ticket-tied):** Red/Amber/Green from feature/AC evidence class, never ticket % (ticket % read 96% then drifted to 85.7%). GREEN requires Class-A runtime evidence; AMBER = Class-E; RED where a falsifier fires. | **A** | An epic shown GREEN without Class-A evidence; the bar reading from ticket % instead of evidence class. | proven | marketingwright |
| TA14 | **Public preprint Polzin et al. 2026 (DOI 10.5281/zenodo.19785799, MIT):** audit-grade Layer-1 (AI-executable: 87 pytest assertions + 11 demos, multi-OS/Python 3.11–3.13) COMPLETE; verified DiscreteTime active-inference engine with three precision knobs ported verbatim into the public Precision Lab. **Honestly bounded: Layer-2 (human expert review) PENDING; unrefereed preprint.** | **E** | The 87 assertions / 11 demos fail to reproduce on a clean multi-OS/Python run; or the Precision Lab math diverges from the engine. | proven (Layer-1) | worldmodels |
| TA15 | **2026-Q2 enterprise launch (Ideation Explorer):** all 41 phases green; **12/12 cross-tenant OODA isolation matrix PASS** (Postgres RLS on 38 tables, non-superuser `ie_app`, FORCE RLS; cross-tenant → 404 not 403 to mask existence); **7/7 production QA gates PASS**; six-tier per-client RBAC live; full doc suite (40 EN + es/hi). Clerk sole SSO + Odoo `res.users` + `client_membership` as the single identity source of truth. | **A** | A cross-tenant request returns data / a 403 (existence leak); any matrix cell or QA gate fails on re-run; a second writable identity source is found. | proven | ideation-explorer |
| TA16 | **KMS / secrets-at-rest (OAS-673):** integration secrets via AES-256-GCM (Node `node:crypto`, zero new deps), env-var master key, PBKDF2-SHA256 @ 100K per-encrypt so each row gets an independent key; wire format `base64(iv\|salt\|authTag\|ciphertext)`; `kmsKeyId` column reserved for rotation. **Replaced the earlier cleartext-secret P0 NEGATIVE (closed loop).** Textbook-level framing only. | **E** | A stored secret is recoverable without the master key; the GCM tag fails to detect tampering; or two rows derive the same key. | proven | ideation-explorer |
| TA17 | **IntelligenceLabs.UNI public demo builds clean cold** (`npm run build`, 21/21 pages, exit 0; needs the `prebuild` step or bare `next build` fails); a clone of the real full Next.js 14 / Drizzle-Neon / Clerk / MCP / PDF-signing Ideation Explorer, demo-ified by real code edits (no built-in DEMO_MODE switch). | **A** | A cold build fails to produce 21/21 pages at exit 0 with the prebuild step. | proven (build only) | intelligencelabs-uni |
| TA18 | **Cell Lab Stories F+G shipped, deployed, live-QA'd** with zero console errors; full `npm test` = 28 cell suites + tsc green (Story F = Rao challenge mode; Story G = leaderboard + neural baseline + bootstrap stats). | **E** | A clean `npm test` shows < 28 passing cell suites, a tsc error, or live-QA console errors. | proven | uni-precision |

### 4.3 Website / self-driving site & measurement — **SHIPPED (some bounded OFF)**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| TA19 | **Full Next.js 16 site built** (26 routes + `/api/intake`); `next build` + `tsc` clean; **zero em-dashes and zero "LEAP"** enforced by a safety sweep. | **E** | `next build`/`tsc` fails on main; or the sweep finds an em-dash or "LEAP" in shipped copy. | proven | website |
| TA20 | **Three domains cut over to Vercel (DNS verified live):** solutionwright.com flipped indexable in Production-only env for the press push; iamhitl.com → Evidence Explorer with Printify store relocated to store.iamhitl.com. | **A** | A live DNS/HTTP check shows a domain not resolving to Vercel / not serving the intended app, or indexability not Production-scoped. | proven | website |
| TA21 | **Self-driving site Phases 0+1 SHIPPED to production (2026-06-25):** storage-agnostic Postgres adapter (Neon hot store + appliance sovereign mirror), no-PII salted-daily-id first-party measurement that degrades to CANON on DNT/error. **Phase-0 storage gate = PASS (2000/2000 writes, identical checksums).** Sovereign ingest proven end-to-end from the open internet (valid → 204 PII-stripped; DNT → no insert; bad-origin → 403; 8 smoke routes 200). | **A** (ingest) / **C** (storage gate) | The storage gate fails; measurement leaks PII / fails to degrade to CANON on DNT; or a smoke route returns non-200. | proven | website |
| TA22 | **SEO/GEO program shipped on SolutionWright:** cross-domain JSON-LD `@graph` with stable `@ids`, per-site `llms.txt` + `llms-full.txt`, sitemap/robots welcoming AI crawlers, a Node link-crawler. Brand-family wiring: one canonical `@id` per real-world entity identical on every page/domain; `parentOrganization`/`founder` point to the same TMDLRG + Person `@id`; `sameAs` ring; use `Claim` not `ClaimReview`. | **A** | Live JSON-LD `@ids` are not stable/identical across pages; `llms.txt`/sitemap/robots missing on a shipped site; or retired schema types used. | proven | website / uni-precision |
| TA23 | **Press-readiness audit harness (reusable):** a 4-phase parallel-agent audit (per-site SEO/GEO, cross-domain JSON-LD, 5 personas — press-journalist / prospective-client / skeptical-scientist / answer-engine (GEO) / accessibility-mobile, GO/HOLD synthesis) that fetches **LIVE HTML via curl**, never from memory; output a prioritized P0/P1/P2/polish scorecard. | **method** / **E** | The audit asserts from memory rather than fetching live HTML, or skips a persona/phase. | uni-precision / website |
| TA24 | **Video library / "Reading Room" at `/watch`** rebuilt as an interactive all-ages curated library (mood/audience chips, multi-language, watch-later) over ~900+ films; **EFE data-walk tool** (44 graded primary-research findings, a 3-way EFE-mode switch, **NO recommendation by design**); **i18n: 822 keys × 10 languages** across UNI + Evidence Explorer. | **E** | `/watch` does not render the curated library / chips non-functional; the data-walk emits a recommendation or its counts differ from 44/3; or the live key/language count differs from 822/10. | proven | website |

### 4.4 Engagement, pricing, brand & design — **method / shipped**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| TA25 | **Relationship-first engagement ladder** (4-step ego-elevation: Discover+Elevate → Follow-Up → Bridge → CTA) + **Deep Tagged Replies** (4–7 sentences ~120–180 words, @-tag, quote a phrase, one half-step extension, end on an answerable question) + Own-Post Defense (reply within ~30 min). CTAs only at Step 4 when invited. No paid ads. **Engagement-lift is TARGETED, NOT YET PROVEN (Class B/pending — do NOT raise to A).** Origin: 372 posts → ONE comment in 30 days. | **B** | Over 3 disciplined weeks the algorithm targets (author-reply rate 25%+, reply-chain depth 1.8+, own-post impressions +30% in 4 weeks) fail to move — revise the playbook, not the volume. | method (lift pending) | orchestrate-linkedin |
| TA26 | **Per-platform reach reality table** (measured limits, not hopes): LinkedIn personal commenting throttles ~88–95/hr (cap sweeps at 80, chunk across hours); LinkedIn articles via REAL Chrome ~9/day (headless ~1/login); TikTok public auto-publish needs an app audit; Reddit comment-only from low-karma; X disconnected (no creds). | **A** | Measured per-platform rates diverge materially (e.g., LinkedIn commenting sustains well above ~95/hr without throttle). | method | orchestrate-linkedin |
| TA27 | **Anti-success-theatre content + text hygiene:** public blogs lead with insight and honest failure (the "## Wrong" section is the centerpiece), never ticket IDs/sprint metrics/streaks; split internal retro from reader-facing. ASCII punctuation only (no em/en dash — an AI tell); max 3 @-mentions/comment; hashtags only on own-page posts; no link in own-post body (drop in first comment within 60s). | **method** | Shipped copy contains an em/en dash, ticket-metric theatre, or generic AI-marketing voice. | orchestrate-linkedin |
| TA28 | **Brand-voice constitution (owner-locked):** source of truth = the theme song ("Grow the world. Grow it together. No one left outside."); never talk about the company ("we are not a brand" banned); customer is the hero; plain felt words; global/multilingual. Enforced by the zero-em-dash safety sweep. | **method** | Shipped copy talks about the company, uses generic AI-marketing voice, or contains an em/en dash. | website |
| TA29 | **Engagement / pricing model:** free 1-hr intake → free Ideation Explorer (3 days) → SOW-1 (hardest-part-first) + SOW-2 quoted → 1-hr Inception (~55 artifacts) → 30-day build in a Review Portal → day-30 checkpoint (G1 safety + G2 value + ROI) → ~3 cycles/90 days. "A trail, not a catalog." **5 journey tiers, same 30 days at a fixed price** (bigger tier scales the team): Pathfinder $1,000 · Scout $3,000 · Explorer $5,000 · Adventurer $8,000 · Odyssey $15,000. Public price points owner-set, safe to print. | **method** | Copy implies $1k is the only one-month tier (the corrected P0 error), or prints a service catalog. | website |
| TA30 | **Referral mechanic (literal):** flat **$200** to whoever brings a client who signs + funds a SOW (no tiers/pyramid); with no referrer the same $200 is donated to EducateWright. Copy must state the literal mechanic, never "we give away $200 on every project." | **method** | Copy states the feel-good generalization, or implies tiers/pyramid. | website |
| TA31 | **Entity/legal:** public entity name is just **"SolutionWright Universal"** — never print "a dba of Action Based Consulting, Inc." on public copy (owner directive). Three live sites: solutionwright.com, universalnaturalintelligence.com (+.online 307→.com), iamhitl.com. | **A** | Public copy prints the dba line. | method | website |
| TA32 | **"Thirty-day" claim (calibrated):** corrected from "bounded to the method / cannot show we shipped" → **"We have shipped in thirty days."** Remaining fence: no client has agreed to be NAMED (no permissioned receipt). Do not revert AND do not over-extend to a named testimonial. | **C** | Evidence shows no 30-day shipment occurred (reverts the claim). | proven | website |
| TA33 | **"Indra's Weave" design system (dev-team-validated, owner-locked):** light-default + warm-dark Night toggle, semantic `--sw-*` CSS variables; Dawn Linen ground, Lapis Indigo ink; three perspective threads + Michael's Tyrian purple "ribbon" (thread-only, never a field); Inter / Fraunces italic / IBM Plex Mono. Guardrails: no pure white, no true black, gold stays amber-yellow, purple thread-only. **Five hero puzzles rotate on a deterministic 6-hour epoch** (`floor(epoch/6h) % 5`) so everyone worldwide sees the same puzzle; + a 122-lesson Tyrian "ribbon" easter-egg layer. | **C** (design) / **A** (puzzle rotation) | Shipped CSS uses pure white/true black, a purple field, or non-semantic tokens; OR two visitors in the same 6h window get different puzzles / the egg count differs from 122. | proven | website |
| TA34 | **Brand/trademark law:** **LEAP** is a registered trademark of the LEAP Institute (Dr. Xavier Amador); SolutionWright coined **LOOP** (Listen → Observe → Orchestrate → Partner) and uses "leap" only as a verb with attribution. Public-facing voice product = **DialWright** (platform stays SolutionWright/UNI.PBX). | **method** | Public copy uses LEAP as a SolutionWright mark. | ideation-explorer / orchestrate-linkedin |

### 4.5 The delivery-route ledger & auth-outage triage — **method (operational)**

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| TA35 | **Auth-outage triage protocol** (learned over a 7-day outage): treat `publish_mode=dry` as report-only (create NO drafts — they silently no-op); `authenticated:true` is a local heuristic, NOT the OAuth token; single-probe one live-API read then report; distinguish a **401** (token expired, persistent — wait for operator) from a **403** (transient blip — writes return same day); do NOT flip `publish_mode` to live to "fix" it. | **A** | Flipping `publish_mode` to live actually fixes an outage; or a 401 clears same-day without operator action. | method | orchestrate-linkedin |
| TA36 | **Idempotency / abort-but-succeeded gotcha:** a publish call can return `PUBLISHER_UNREACHABLE`/aborted to the client while the sidecar SUCCEEDED server-side. On any abort/timeout, check `idempotency.json` AND the platform's Published list BEFORE a fallback — else you publish a duplicate to live subscribers (this happened; a duplicate newsletter went out and had to be deleted). | **A** | A fallback after an aborted publish never duplicates even without checking `idempotency.json`. | method | orchestrate-linkedin |
| TA37 | **Anti-no-op real-tool-signature set:** `sweep_manage` actions are ONLY `run\|schedule\|history\|health\|mark_complete`; `linkedin_set_autonomy_mode(page_id, mode='auto')` is idempotent; own-post-defense reads `org_post_id` then `linkedin_get_post_comments(post_urn=org_post_id)`, `comment_count:0` is a COMPLETE result; `memory_store` payload must be valid JSON. When a SKILL call fails on a param/JSON error, FIX the SKILL file and verify against the loaded schema. | **A** | A documented signature here no-ops or errors against the live loaded tool schema. | method | orchestrate-linkedin |
| TA38 | **HARD GO-LIVE SAFETY FLAG (highest-urgency operational fence):** `PUBLISH_MODE=dry` does **NOT** gate the publishers' Playwright path — a publish action with a live session CAN post live. **Add `auto_publish=false` in `proxyPublisher` before any live publishing.** Stay in dry until then. | **A** | `PUBLISH_MODE=dry` is shown to actually block the Playwright publish path with a live session. | negative (safety) | uni-os |

### 4.6 Track-A NEGATIVES & recorded delivery-route bounds — first-class

| # | Negative / bound | Class | Falsifier | Status | Source |
|---|------------------|-------|-----------|--------|--------|
| TA-N1 | **Headless/automated YouTube Studio browser upload is DEAD on modern Chrome.** All three routes fail (Google rejects automated sign-in; Chrome 136+ refuses CDP on the default profile; Chrome 127+ App-Bound Encryption voids copied-profile cookies; `yt-dlp --cookies-from-browser` fails by design). Only the Chrome-extension MCP keeps a real session (agent-driven, not unattended). **Verdict: DO NOT RE-ATTEMPT;** use Data API or operator drag-drop+finalize. | **A** | A future Chrome/Google change restores an unattended headless Studio upload that survives App-Bound Encryption + CDP restrictions. | negative | orchestrate-linkedin |
| TA-N2 | **TikTok direct/auto public publish is HARD-BLOCKED:** unaudited app returns `unaudited_client_can_only_post_to_private_accounts` (403). Code is ready; the ONLY unlock is the operator submitting for Content Posting API audit. DO NOT retry-loop direct-post. | **A** | The app passes the Content Posting API audit, lifting the 403. | negative | orchestrate-linkedin |
| TA-N3 | **Reddit self-posts / link-drops from a low-karma account = account-killing.** One account permanently banned from 7 subs; bans return a silent 500. Rule: **COMMENT on existing threads only, never self-post our own links.** | **A** | A low-karma account sustains self-posting our own links without ban over a meaningful window. | negative | orchestrate-linkedin |
| TA-N4 | **External threaded ladder replies** (`linkedin_reply_to_comment`) **400 on execute** on third-party posts (personal and org actor). Only top-level `comment_manage` drafts post live externally; own-post replies still execute. Never stack a 3rd top-level comment in a thread. | **A** | `linkedin_reply_to_comment` executes (non-400) on a third-party post. | negative | orchestrate-linkedin |
| TA-N5 | **The "1600 units → only ~6 uploads/day" YouTube quota panic was FALSE** — the project quota is audit-raised; 30/day succeeded. The `youtube_quota` DB counter is unreliable (script bypasses it). Lesson: verify the real project quota, never reason from defaults ("falsify the mundane causes"). | **A** | The audit-raised quota actually caps at ~6/day under real conditions. | negative (correction) | orchestrate-linkedin |
| TA-N6 | **OAuth fragility (cross-archive):** YouTube + Reddit OAuth found BROKEN and diagnosed empirically (YouTube 401 + "refresh: Bad Request"; Reddit 401 with `www-authenticate: Basic realm="reddit"` = rotated client-secret, a 2-min operator re-issue; Twitter/X creds ABSENT, channel unwired). Re-auth handed to the owner as a precise click — **the agent never mints tokens.** Queue history at a snapshot: 107 published / 5 failed / 9 cancelled. | **A** | OAuth is shown working without operator re-auth; or a 401 caused by something other than a rotated secret resolves without re-issuing it. | negative | worldmodels / orchestrate-linkedin |
| TA-N7 | **GEO reality check:** AI search crawlers rarely fetch `llms.txt` and Google said it won't support it — ship it as a cheap correct machine-facing gesture for agentic/IDE tools, **not for ranking.** | **C** | Evidence emerges that AI crawlers materially fetch `llms.txt` and it drives ranking. | negative | website |
| TA-N8 | **Combinatorial scale ceiling (MarketingWright, FIRED):** the clustering engine is exhaustive over Bell-number partitions; the "scales to N=12" falsifier fired (Bell(12)=4.2M partitions > 60 s budget). Operating envelope **N ≤ ~10** without a beam/coarser-prior/compiled loop (Sun-Prairie demo N=7 is safe). Plus 7 surface defects (4 HIGH) with fired falsifiers, all in the surface contract not the math; Gemini struck per no-LLM; the alpha∈{inf,nan}→NaN-tainted-F-with-self-attested-Class-A case is a self-attestation integrity gap. | **A** | A sub-Bell method bounds cost for N>10 (lifts the scale bound); each surface defect's specific attack succeeding. | negative (bound) | marketingwright |
| TA-N9 | **OBS composite-in-OBS path is a dead end** (OBS CEF renders WebGL black) — retired in favor of WGC window-capture of real Chrome windows. | **A** | OBS CEF rendering WebGL correctly on the dual-GPU box. | negative | strings |
| TA-N10 | **Per-client Vercel deploy gotchas (Ava detective story):** a project created via `vercel project add` gets `framework:null`, which mis-bundles Next.js edge middleware → set `"framework":"nextjs"`; host on Vercel (not local+tunnel, which breaks Clerk redirects); Clerk dev instances reject `.vercel.app` as origin (use an allow-listed `redirect_url`/custom domain); don't deploy-spam (rapid prod deploys tripped an account-wide fair-use 402). Bare `next build` fails without the gitignored design-tokens `dist/` (add a `prebuild`); two API routes needed `force-dynamic`. | **A** | The `framework:null` edge-middleware drift does not occur; or a bare `next build` succeeds from a clean checkout without the prebuild. | negative (gotchas) | ideation-explorer / intelligencelabs-uni |
| TA-N11 | **Two costly misfires (brutal-honesty record):** (1) `vercel deploy` with no `.vercel` link auto-created a brand-new project named after the folder; (2) work proceeded on a fake scaffold (a prior session's from-scratch 6-step wizard) mistaken for the real portal → the owner's "that's not my portal" reaction. Origin of the confirm-before-deploy and do-not-touch-client-portals Laws. | **A** | Transcript shows no stray auto-created project and no scaffold confusion. | negative | intelligencelabs-uni |
| TA-N12 | **"All LLMs end in entropy" is only half-true** (Emergence-World S1 AWI: Claude Sonnet 4.6 = 10/10 alive, Gemini 3 Flash = 10/10, Grok 4.1 Fast = 0, GPT-5 Mini = 0). Two cohorts held the line; the honest falsifier was **sharpened** (UNIs must match/beat the best LLMs AND show substrate properties LLMs lack — not merely beat the worst). Raises the bar; does NOT claim UNI superiority. | **C** | The original blanket claim is already falsified by the two 10/10 cohorts; the sharpened bar fails if UNIs can't match the best LLMs or show the substrate-distinct properties. | negative | strings |

### 4.7 Track-A PARKED / not-yet-built — first-class

| # | Parked / not-yet-built | Class | Closes when | Source |
|---|------------------------|-------|-------------|--------|
| TA-P1 | **social-publisher browser-route publishing waits on operator noVNC login per platform** (the agent never enters credentials — hard boundary). The ONE human step; retires the Reddit-401 and TikTok-audit publishing gates. | A | the operator completes the per-platform noVNC login. | orchestrate-linkedin |
| TA-P2 | **Recurring auth outages are the dominant live blocker** (LinkedIn token expiry / no refresh token, Reddit 401, `publish_mode=dry`, periodic Docker-Desktop crash-loops). All require an operator click, not a code fix. A sustained multi-day outage occurred (LinkedIn dry + 401 reads, Reddit 401, **~5 days no posts, ~190 queued**). | A | operator re-login. | orchestrate-linkedin |
| TA-P3 | **`engagement_engine` MCP tool built + tested (20/20) but NOT committed / NOT wired into a live auto-loop.** Decision owed: wire it in or retire it. | E | committed + wired into a live loop, OR retired. | orchestrate-linkedin |
| TA-P4 | **Forms-P0 (highest-value unfinished marketing task):** `/api/intake` forwards to `INTAKE_WEBHOOK_URL` only if set — it is unset, so leads go nowhere; `/falsify` has no backend. Measurement is built but **OFF** until `NEXT_PUBLIC_INGEST_URL` is set + redeploy (a deliberate degrade-to-CANON safety). | C | the owner wires `INTAKE_WEBHOOK_URL` + press email and sets `NEXT_PUBLIC_INGEST_URL`. | website |
| TA-P5 | **Self-driving Phases 2–5** (bandit engine, public posteriors, reciprocal entity graph across all 3 repos) planned, not built. The master pattern (site as an EFE-minimizing agent that always degrades to CANON) is **Class-U design until shipped** — "active inference" is the framing lens, never "active inference demonstrated". | U | each phase is built + observed live. | website |
| TA-P6 | **`/explore` "Live demo" built-but-unshipped** (points at an `ideation.*` subdomain not deployed). Do not ship `/explore` until the subdomain is live. **IntelligenceLabs.UNI demo NOT deployed in-session** (blocked on a disposable Postgres — Vercel CLI 48.9.0 has no `storage` command; must use the dashboard Neon integration). Handed off via `HANDOFF-MAIN-WEBSITE.md`; live state unverified. | E / A | a disposable Postgres is provisioned and the demo is deployed + subdomain-wired. | website / intelligencelabs-uni |
| TA-P7 | **Homepage "weave" chrome copy is hardcoded** (ribbon aria-labels, eggs, eyebrows) while the hero rotates 5 puzzles → weave-specific copy is wrong 4/5 of the time. Flagged P0; one root fix in `PageShell.tsx`/`EasterEgg.tsx` clears ~18 findings. Fix status unverified by the archive. | E | the root fix lands and the ~18 findings clear. | website |
| TA-P8 | **Client-B content-engine phases P2–P5** (SMS magic-link + uploads, RTMP livestream, ffmpeg post-production, library view) — specced, not deployed. **Quick-tunnel URLs are ephemeral** (`*.trycloudflare.com` changes on restart, no uptime guarantee); promotion to a named tunnel needs operator tunnel creds. | U / A | each phase is deployed + observed live; a named tunnel replaces the quick tunnel. | ideation-explorer |
| TA-P9 | **Authenticated portal flows unverified** (Ava + the per-client pattern have Class-A evidence only for unauthenticated/gated/public routes; the logged-in experience needs a real team Clerk login — NOT yet observed). Largest open verification gap alongside handoff-never-fired. | U | a Class-A observation of a real team Clerk login driving authenticated portal flows. | ideation-explorer |
| TA-P10 | **UNI Production Platform** — a buildable design for a broadcast-grade live show, **not deployed.** Do not treat the design as capability. | U | built. | orchestrate-linkedin |
| TA-P11 | **MCP-attach for the labs** (expose a lab as an MCP server so an LLM can set/explain/run sims) — raised, parked behind commit/deploy/QA, **not yet built.** | U | an MCP server exposing a lab's sim params exists, is attachable, and runs sims end-to-end. | uni-precision |
| TA-P12 | **UNI Signals DV-safety app launch is HARD-GATED** behind 5 human-expert sign-offs and no shelter DB. Clinical pre-audit: a 414-scenario regex-lexicon safety detector — crisis/danger detection strong but **veiled-danger detection weak (~33%)** → semantic + human escalation required. Patent-level UNI math stays private. | C | 5 sign-offs land AND veiled-danger detection reaches an acceptable measured rate. | orchestrate-linkedin / marketingwright |

### 4.8 Track-A NEGATIVES in the delivery & data layer (ideation-explorer) — first-class

| # | Negative | Class | Falsifier | Status | Source |
|---|----------|-------|-----------|--------|--------|
| TA-N13 | **Handoff never executed end-to-end at runtime:** `verify_chain` was valid (500 events) but the running MCP's full audit log (243K chars) had **ZERO** handoff/inception-bundle events — the route was built + unit-tested but never fired against the deployed MCP. The canonical "exists in code (Class E) vs observed at runtime (Class A)" case. | **A** | A Class-A end-to-end observation of a handoff/inception-bundle event in the live MCP audit log. | negative (open) | ideation-explorer |
| TA-N14 | **Container/code drift:** the deployed Agile-MCP container was behind the code that shipped the SW-INT receive routes, so routes that "exist" in code were unreachable in prod. | **A** | A runtime probe confirms the deployed container serves the SW-INT routes (container == shipped code). | negative | ideation-explorer |
| TA-N15 | **Fictional transcript provability + aspirational gate + unbounded growth:** `payloadBuilder.ts` hardcoded `transcript_sha256: null`; `evaluateClerkAdoptionGate` referenced only by its own test (no prod caller → its ADR stays PROPOSED indefinitely); `pruneOldCallbackNonces()` existed but no scheduler invoked it. Analogues of "reproduced:true must be validator-derived" / "Class-E-test ≠ Class-A-in-production". | **C** | A verifier recomputes a real transcript hash; a prod caller/scheduler invokes the gate / the prune. | negative | ideation-explorer |
| TA-N16 | **Cleartext HMAC secrets P0** (`hmac.ts` stored the integration secret in cleartext, "Envelope encryption is TODO") — the one P0 blocker for real production handoff. **LATER REMEDIATED by OAS-673 AES-256-GCM (closed loop).** | **C** | n/a (recorded bound) — discharged only by the secret no longer being recoverable in cleartext (done). | negative (remediated) | ideation-explorer |
| TA-N17 | **Firewall rule not persisted:** the `nft dport 8089 accept` rule is runtime-only; a reboot drops Client-B's site until `/etc/nftables.conf` is hand-edited. | **A** | The rule is persisted and the site survives a reboot on re-probe. | negative (reboot-fragility) | ideation-explorer |
| TA-N18 | **Residual risk (intelligencelabs-uni):** the repo's git history (initial commit) still contained prior real-client data even though the working tree is clean. Flagged for optional scrubbing; left to the owner. (PII withheld here.) | **A** | Inspecting the initial commit shows no prior real-client strings, or it was scrubbed. | parked (residual) | intelligencelabs-uni |

---

## 5. MarketingWright SOW-01 — scope, architecture & honest bounds (commercial detail)

The signed commercial proof-point. Carded here so the Cookbook can author the "no-API content model in commercial miniature" chapter without inflating the one chosen judgment layer into the full vision.

| # | Claim | Class | Status | Source |
|---|-------|-------|--------|--------|
| MW1 | **SOW-01 shape:** $3,450, 30 calendar days, 5 deliverables (sandbox workbench; uplift scoring model v0; reviewer workflow; measurement instrumentation; Gate G1/G2), Checkpoint Charlie at day 30; POC anchor = social-media content-calendar automation (client's #1 pick, difficulty 3/5). Hard constraints: journalist-grade quality (max), near-zero onboarding friction (min), human-in-the-loop by default. Discovery DONE (52 ideation artifacts; sessions told not to re-run discovery). | A | method (definitional scope) | marketingwright |
| MW2 | **The wedge:** four "minimal-prompt-in, marketing-grade-judgment-out" judgment layers (fact-checking/disambiguation; strategic grouping/clustering; geographic-research judgment; cadence+tone). Client chose ONE for the 30-day proof: strategic thinking = **80% grouping + 20% disambiguation.** Other three deferred to post-Checkpoint-Charlie / SOW-02. | A | method (scope choice) | marketingwright |
| MW3 | **Two-layer architecture (ADR-013):** UNI = intelligence layer (all decisions, clustering, free-energy scoring, eventual generation) with **NO LLM ever**; Surface = usability (chat/UI + MCP + Word output). The MCP/JSON seam contract is the single highest-leverage undefined artifact. | B | method | marketingwright |
| MW4 | **Grouping = Bayesian-Occam model selection** (best clustering = the hidden cause that best explains the events; scored by negative VFE = accuracy − complexity; uplift in nats). The standard math is Class A; the MarketingWright-specific engineering is Class C. Standing fences: `q` (recognition density) kept distinct from the model posterior; `F[q] ≥ −ln p(y\|m)`; the model is the agent's hypothesis space, not "the world." **EFE used ONLY for action** (high ambiguity → emit ONE clarifying question), held explicitly at **Class C — do not raise above.** Six-sub-score decomposition, never a bare scalar. | A (math) / C (engineering) | method/proven | marketingwright |
| MW5 | **Domain-independence probe (Class-B):** the same VFE clustering math transferred to **synthetic** drug-trial (oncology Phase-II) data and clustered sensibly + reproducibly (three-forms Δ=1.4e-14). **Run on SYNTHETIC data only, never real clinical data.** Class B, not A; do not raise to a general comprehension claim. | B | proven (bounded) | marketingwright |
| MW6 | **Memory/isolation architecture (ADR-022-026):** four memory domains (per-UNI mind, per-client world, platform store, one-way de-identified cross-client-insight valve); fully isolate per client (no learned state crosses clients); cross-client insight default-on, de-identified, opt-out via a blocking audited de-identification membrane. **Autonomous generation is OUT of the POC** (post-POC: local UNI writes copy, no hosted LLM). | B | method | marketingwright |
| MW7 | **Data infrastructure ruling:** ONE PostgreSQL engine (pgvector + bitemporal schema adopting the Graphiti bi-temporal pattern NOT its Neo4j runtime + RLS as the per-client firewall + optional Apache AGE post-POC). POC needs only Postgres + pgvector + RLS. All Apache-2.0/PostgreSQL-licensed = resellable. Supersedes older Node+Mongo and Zep/Graphiti-runtime plans (supersede-with-lineage). | B | method | marketingwright |
| MW8 (PARKED) | **External blocker D1:** the client's written acceptance thresholds (AC1–AC5, AC7) are OPEN; NFR thresholds stay PROPOSED and the readiness model's **ACCEPT axis is WITHHELD** until the client signs. Cannot be self-resolved (distinct from the internal Gemini "D-1/ADR-019" defect). | C | parked (honest incompleteness) | marketingwright |
| MW9 (PARKED) | **Class-A end-to-end: ZERO epics have it.** The honest portal RAG caps EVERY epic at AMBER — MCP "DONE" = test-covered (Class E/D), not feature-working (Class A). An 11-row "Class-A Observation Plan" is the path to green; the honest headline is **RED on the provenance hard floor, not "85.7% done."** | C | parked | marketingwright |
| MW10 | **Provenance/lineage (Class A/F):** the 52 artifacts derive from an **April 8 discovery call** (source media SHA-256-anchored, ms-precise cue timestamps); a separate **May 20 inception-kickoff** recording is in-repo but explicitly tested + confirmed **NOT** the source of the 52 artifacts. Do NOT conflate them. | A | proven | marketingwright |
| MW11 | **Compositional non-LLM narrator (working prior art):** an Elixir/Strings "UNI.Minecraft narrator" — saliency director + EFE rhetorical move-planner + compositional grammar (activity×emotion→verb-phrase + mood→sentence) + a learned per-brand HMM, `deps=[]` (no LLM). MarketingWright generalizes this to marketing judgment. **Design-pattern reuse, not a delivered generation capability (generation is parked post-POC).** | method | method | marketingwright |

---

## 6. activeinference archive — VERIFY-IT-EXISTS (design-only, zero execution evidence)

**Do not treat any E0–E7 claim as real until verified by observation.** The `activeinference` BEAM-native AIF Workbench is a well-formed **design charter with ZERO recorded execution evidence** in the snapshot.

| # | Claim | Class | Falsifier | Status | Source |
|---|-------|-------|-----------|--------|--------|
| AI1 | The archive carries **no PASS/FAIL/NEGATIVE/PENDING ledger entries, no transcripts, no build/test/replay results.** The four authoritative source files (`CLAUDE.md`, `Design.txt`, the TDD plan, the formulas file) are named as priority reading but are **ABSENT** from the archive. Whether any E0–E7 epic was implemented is UNKNOWN from this archive. | **U** | Locating the live project tree and finding green tests / recorded runs for any E0–E7 epic moves specific rungs from design-only to evidenced; absence leaves it unverified. | not-yet-built | activeinference / 00-INDEX (Synthesis-1 #10) |
| AI2 | **Scope fences (design constraints, NOT empirical negatives):** v1 is discrete-time ONLY — no continuous-time dynamics, no Python/JS runtime logic; the whole runtime lives on the BEAM. Deliberate scope exclusions, not failed experiments. | **U** | n/a (design constraint). | not-yet-built | activeinference |
| AI3 | **Reusable DESIGN/governance patterns** (recorded, transferable — see M27): runtime-derived UI; deterministic-replay; TDD-as-gate with ordered E0–E7 epics; single-source-of-formulas provenance; pure-agent (Jido) runtime. *Patterns, not demonstrated results — the underlying build is unverified.* | method | n/a (method). | activeinference |

**Session-2 action:** locate the live project tree before crediting any activeinference capability.

---

## 7. Standing open threads / contradictions to reconcile (carried forward, not discharged)

These are recorded so absence/ambiguity is never mistaken for a complete ledger. By No-Exit discipline none is discharged until a sign or an observation lands.

| # | Open thread | Status | Source |
|---|-------------|--------|--------|
| OT1 | **Repo-split / brand deprecation:** UNI.GPT brand deprecated; content → a new single-science-of-record repo (working name "uni-mind"; remote/visibility/history PENDING). Risk of two writable ledgers would break L10/L11. UNI.OS mirrors the science repo READ-ONLY; coupling is one-directional (science PROVES → UNI.OS EMBODIES frozen at the passed-gate SHA). Drafted `UNI_CONSULT_5` sign owner-relayed, **NOT yet captured** → park not discharged. | parked | uni-gpt / uni-mind / 00-INDEX |
| OT2 | **"never push" vs authorized pushes:** `CLAUDE.md` reads "commits kept LOCAL — never pushed," yet the owner authorized 3 pushes to the confirmed-PRIVATE `TMDLRG/uni-mind`. Reconciliation: push IS allowed on this private repo WITH per-push owner confirmation; the stale contract line needs a one-line owner-approved update. Do not read "never push" as absolute. | parked | uni-mind / 00-INDEX |
| OT3 | **Channel-handle policy nuance:** the 2026-06-26 owner refinement softens the hard "never print the handle" rule — a link may exist but the handle must not be FEATURED (move to a new YT later). Reconcile downstream copy. The AIF/EFE vocabulary-leak guard stays intact independently. | parked | website / strings / 00-INDEX |
| OT4 | **Canonical-portal ambiguity:** `origin/main` carries a newer commit adding a deprecation banner → `solutionwright/cw-ideation`, suggesting `cw-ideation` may be a NEWER canonical portal than the cloned release. The session deliberately used the local release code without the banner. Reconcile before any future clone. | parked | intelligencelabs-uni |
| OT5 | **"Story F built twice":** session `d56fa8a1` (full SWU-MCP board) vs `76c02906` (MCP absent, CLI-adapted) ran the same Story F brief. Confirm which commit (`b909e63` F / `f78baca` G) is canonical and whether effort duplicated. | parked | uni-precision |
| OT6 | **Two live hosts coexist:** build/QA against `*.vercel.app` staging while press-readiness/press-fix workflows target the apex (`universalnaturalintelligence.com`). JSON-LD `@id`s must use the apex (stale-`@id` risk). Confirm apex = canonical production. | parked | uni-precision |
| OT7 | **Two distinct "books" share the UNI label:** "Run on Rhythm" (5P business book, 2nd ed. infused with UNI conceptually, no equations — published on KDP) vs `book_quick_start/` (plain-language active inference). Keep distinct downstream. The "live Minecraft FEP colony" in worldmodels appears as metaphor/aspirational there while it is REAL in strings/uni-os — reconcile. | parked | worldmodels |
| OT8 | **Aspirational upstream `DEMO_MODE`:** every IntelligenceLabs.UNI demo guardrail was a manual code edit because the real portal has no demo switch. Open product question: add an upstream `DEMO_MODE`? No engine/feature exists yet — not a capability claim. | not-yet-built | intelligencelabs-uni |
| OT9 | **Legacy unauthenticated approval daemon** (port 8442, root chroot exec, zero auth) dormant but un-retired — archive it. | parked (security hygiene) | uni-os |
| OT10 | **No `memory/` spine for the precision repo** (unlike the website archive); if the labs are durable, a `memory/` index is worth creating in a later session. | not-yet-built (infra) | uni-precision |

---

## 8. Provenance & maintenance

- **Authority:** every row is carded at the **lower** of its evidence components and at its **strongest source archive**. Cross-referenced ladder rows (the same rung stated in `website`/`uni-os`/`worldmodels`/`activeinference`/`uni-precision`/`strings` via `00-INDEX`) are merged into the single canonical row above and are NOT re-listed per archive.
- **Append-only:** corrections are forward-only (supersede with lineage), never silent edits. Calibration moves wording DOWN only.
- **Single source of truth:** the Encyclopedia and Cookbook cite this file; if prose and this ledger disagree, this ledger wins and the prose is wrong.
- **Preprint citation (always fenced):** Polzin et al. 2026, Zenodo DOI 10.5281/zenodo.19785799 (MIT) — unrefereed working preprint, Layer-1 audit complete, Layer-2 human review PENDING.
- **Science provenance (textbook-level only):** Parr, Pezzulo & Friston, *Active Inference* (MIT Press, 2022). Patent-level UNI math stays private (consult the UNI Active-Inference Guide GPT; never publish it).

*End of CLAIM-LEDGER.md — the master evidence-classed claim ledger. Falsify any row.*


<!-- ===== END encyclopedia/CLAIM-LEDGER.md ===== -->



<!-- ===== BEGIN encyclopedia/MASTER-PLAN.md ===== -->

# MASTER-PLAN.md — The UNI Encyclopedia (table of contents + authoring rules)

**What this is.** The authoring blueprint for the **UNI ENCYCLOPEDIA** — the public reference work
about the UNI program (a *developmental active-inference SIMULATION*, never a person, never a mind).
This file fixes the front matter (the Evidence Constitution, the A–U rubric, the standing fences and
red-line list, the "what is NOT claimed" template), the body structure (the four live-hub wings ×
the L0–L12 science spine × the Method wing × the Track-A appendix), a one-page authoring spec per
chapter, and the ordered **Session-3 authoring queue**.

**Authority.** This plan authors *against* two files and never ahead of them:
- the single source of truth — [`CLAIM-LEDGER.md`](./CLAIM-LEDGER.md) (882-row append-only ledger, every claim carded A–U with a falsifier);
- the Session-1 synthesis — [`../curated/00-INDEX.md`](../curated/00-INDEX.md) (the 11 per-archive digests, the wing map, the Track-A/Track-B split).

If any encyclopedia prose disagrees with `CLAIM-LEDGER.md`, **the ledger wins and the prose is wrong.**
No chapter may state a claim above the evidence class recorded in the ledger, omit a recorded falsifier,
or hide a recorded negative.

**Honest program position (print it, do not soften it):** **~2 of 11+ developmental rungs earned.**

---

# PART I — FRONT MATTER (the constitution; read before authoring any chapter)

## FM-1. The Evidence Constitution

Every entry in the encyclopedia is governed by six rules carried verbatim from the ledger:

1. **A falsifier per claim.** No claim ships without a stated condition that would prove it false.
   A claim with no falsifier is not a claim — it is marketing, and it is forbidden.
2. **The append-only ledger is the single source of truth.** Four states only:
   **PASS / FAIL / NEGATIVE / PENDING.** Corrections are forward-only (supersede with lineage),
   never silent edits. Prose cites the ledger; if they disagree, the ledger wins.
3. **Calibration only moves DOWN.** Authority flows downward from the measured fact. Wording is
   calibrated **down** to the measured value, **never up** — including under urgency.
   *The fence gets louder under pressure, not wider.*
4. **Verdict = the CI bound that excludes the threshold, never the point estimate.**
5. **DONE = test-covered (Class E/D), not feature-working (Class A).** A passing test does not
   satisfy a criterion that demands a runtime observation.
6. **Negatives are content.** A partial / a negative / a "most pieces don't help" decomposition is a
   *measurement that the design is incomplete*, not an exit and not a failure to hide. **The negatives
   are the credibility.**
   *Provenance fence (do not feature as a re-countable headline).* The figure **882 rows = 350 PASS /
   0 FAIL / 183 NEGATIVE / 349 PENDING** is a **recorded ledger snapshot**, not a count reconstructable
   from this document: the ledger derives from a deduplicated merge of 615 extracted claims
   (`CLAIM-LEDGER.md` line 5), the snapshot enumerates 882 rows, and the carded body shows only ~140
   distinct rows. A skeptic counting the published rows **cannot** independently derive 183. Cite the
   snapshot **as a snapshot** (provenance-flagged), and headline only the negatives actually enumerated
   in the ledger body — never the bare "183 published negatives" as a credibility number until the count
   is reconstructable, per the calibration-down rule.

**No-Exit Discipline.** The only legitimate rest is a proven working solution **or** a published,
exhausted, falsifiable bound — then redirect to the axis where the reader genuinely excels. Never go
silent on an open gate. A park is not discharged until its sign-to-park lands. Falsify the mundane
causes (L2 metabolism / L7 retrieval-and-recency) before calling any NEGATIVE.

## FM-2. The evidence-class rubric (A..U)

The class is the ceiling. A chapter may card a claim **at or below** its ledger class, never above.

| Class | Name | Means | Authoring rule |
|---|---|---|---|
| **A** | machine-exact anchor / live observation | observed at runtime, or exact to the float tier (machine-checkable) | the strongest class; still fence the *interpretation* (an anchor is not a capability). |
| **B** | mechanism + operator observation | a mechanism shown working under grounded inspection, short of a held eval | never present a B as a held-out PASS. |
| **C** | dev-gate / held-out eval | a pre-registered, sealed, held-once gate with a CI verdict | this is the empirical-PASS tier; cite the CI bound, not the point estimate. |
| **E** | test-covered | tests pass (and `D` = test-covered design) | **DONE ≠ working.** A Class-E pass never satisfies a Class-A criterion. |
| **F** | doc / prior-claim | inheritable from a document or earlier claim | **must be re-verified** before it is leaned on; mark inherited. |
| **U** | claimed-but-unproven | asserted but not earned (e.g. "human-level"; the parked frontier) | **"Class U — not claimed" is itself a standing fence.** Class-U content is described as *not-yet-built / parked*, never as capability. |
| **method** | definitional / governance pattern | a reusable discipline, not an empirical claim | proven and reusable, but cannot be raised into a capability claim. |

**Class-authority ordering** (when sources conflict): Class-B (tool state) overrides Class-G (own
narrative); Class-A (observed at runtime) overrides Class-E (test passes). Mark `[CONFLICT:unresolved]`
and resolve with a direct read. (The A–F subset — A live · C code/static · E test · F doc/inheritable —
is the per-ticket provenance taxonomy; the full A–U taxonomy adds B mechanism, U not-claimed, and `method`.)

**Exactness-tier honesty (load-bearing).** Never label a float32 anchor `<1e-10 EXACT`. The JAX core
runs **float32**, so its anchors hold only to **~6e-8 (~1e-6 single-step filter)**; the genuine `<1e-10`
tier lives only in the NumPy / Rust-f64 path (the cross-language Rust-f64 == Python bridge). A genome
docstring that claimed `<1e-10` was caught as an overclaim and corrected. Card every anchor at its real tier.

## FM-3. Standing fences + the red-line list

**Standing program framing — say it this way, every chapter:** "developmental SIMULATION",
"bounded peek", "toy world, not the real world", "Class U — not claimed", "unrefereed working
preprint", "same math, many scales", "count baselines / LOOP not LEAP."

**THE RED LINES — never claim, in any chapter, in any public copy, under any pressure:**

1. Never **AGI** / general intelligence / human-level / "talks & learns like a human" / "understands."
2. Never **consciousness** / sentience / aware. (Functional self-awareness *may* be described at L8;
   **phenomenal sentience is explicitly DISCLAIMED** — no falsifier is offered because it is disclaimed,
   not tested.)
3. Never **"active inference demonstrated."** No AIF loop exists in the Rust crate; the live UNI.OS loop
   is a separate reimplementation, **not gate-matched.** "Active inference" is the framing *lens*, never
   a demonstrated result.
4. Never **"created life" / "digital life" / "measurable awareness"** as a CLAIM (north-star framing only;
   posed as an open falsifiable question, never an answer).
5. Never **"beats LLMs."** World C is a **COUNT** baseline; the program is ~10–15% behind backprop LLMs on
   char-perplexity by a chosen design trade. EDAIT is an honest fluency-for-calibration trade (~33 vs ~25 ppl).
6. Never inflate the **Tier-2 synthetic-construction track** into capability (it was audited as
   artifact/diagnostic — hardcoded-literal "exactness", scoring-artifact deltas, no AIF loop — and fixed).
7. Never **raise a claim above its source evidence class.**
8. Never let **substrate / continuity engineering** imply a science gate is met (it is engineering evidence,
   not general-AIF evidence).
9. Never publish "**K≥3 exhausted**" / "**§0.6(B) achieved**" phrasings until UNI signs the relevant park.
10. **No PII. No secrets/tokens/internal channel handles** (a *link* may exist; the handle is never
    *featured*). **No patent-level UNI math — textbook-level framing only** (consult the private UNI
    Active-Inference Guide GPT for science; never publish it).
11. **The preprint** (Polzin et al. 2026, Zenodo DOI 10.5281/zenodo.19785799, MIT) is cited as the
    **mathematical foundation only** and always fenced **unrefereed** (Layer-1 AI-executable audit complete;
    Layer-2 human expert review **PENDING**) — never as proof that active inference is the correct theory.
    *PII note (not a red-line breach):* the named authorship "Polzin et al." is **already public under the
    cited DOI**, so reproducing the author form is an **intended public attribution, not incidental PII
    leakage** — the no-PII red line (item 10) is not violated by this sanctioned citation. (If a public
    encyclopedia copy must not bind the program to the owner's surname, fence the citation to the
    **DOI + title only**; absent that instruction the published authorship stands as intended attribution.)
12. **Vocabulary-leak guard (HARD, test-enforced):** never externalize active-inference / EFE / free-energy
    framework names or print internal channel handles in public copy. Public copy says "count baselines",
    "prediction-error", "LOOP not LEAP."

**UNI-GPT consult (2026-06-27 — SIGNED): forbidden-phrasings red-line list (extends FM-3, calibration-down).**
The consult (Q7b) banned the following phrasings OUTRIGHT — never publish any of them, in any chapter, in any
public copy, under any pressure. Each is paired with the only honest replacement. (Cross-reference:
[`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md), Q7.) This list is
ADDITIVE to red lines 1–12 above and never relaxes any of them.

- **Banned outright:** "UNI is conscious / aware / self-aware / has measurable awareness / has a mind / has a
  conscience / reasons like a human / is human-level / is AGI / created life / created non-organic life / is
  alive / is a synthetic organism / dreamed / is creative in the human sense / demonstrates active inference /
  proves the FEP creates minds / proves plants and UNI are the same kind of life / beat consciousness tests /
  beat LLMs therefore awareness / passed L12 / L12 achieved."
- **Replace with (the only licensed forms):** "UNI passed a specified proxy test / improved a registered
  downstream metric / matched-or-exceeded the registered LLM baseline on this sealed task / showed a
  substrate-distinct effect under this ablation / remains a developmental active-inference simulation / the
  awareness question remains open."
- **L7/L9–L10 frontier (Q1, signed):** replace any **"published exhausted bound"** framing with
  **"ledger-scoped exhausted search envelope"** — a ledger-scoped, implementation-scoped, data-split-scoped
  negative result over the tested envelope only, NOT a universal impossibility result and NOT an achieved
  capability rung. Specific banned→replacement pairs (Q1): "K≥3 exhausted" → "The registered tested K
  conditions did not reverse the result."; "Sec-0.6(B) achieved" → "Sec-0.6(B) remains unearned / parked
  pending a future result that beats the registered discourse prior under ledgered evaluation."; "UNI
  demonstrates language/metacognition at L9–L10" → "UNI records a negative L9–L10 frontier test under the
  no-backprop developmental simulation program."; "This proves no no-backprop model can beat MKN-7" → "No
  tested no-backprop variant in the registered envelope beat MKN-7 on the chosen char-ppl metric."

**UNI-GPT consult (2026-06-27 — SIGNED): awareness-proxy proposal-entry checklist (the L12 gate).**
Any FUTURE L12 "awareness" work must pass ALL ten conditions below before such a gate may even be PROPOSED
(Q7c). This keeps any awareness gate falsifiable rather than unfalsifiable. It is a *proposal-entry* gate,
not a pass-claim, and it raises NOTHING: L12 stays NOT-YET-BUILT and Class-U-not-claimed regardless.

1. **Proxy-only target** — title must say "…-proxy"; no bare "awareness gate."
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

## FM-4. The "what is NOT claimed" entry template

**Every chapter carries this block; it is not optional and it is not buried at the end.** It is a
first-class section with the same weight as the claim. Template:

```
### What is NOT claimed in <chapter>
- Ceiling: <the single strongest thing a careless reader might infer> is NOT shown. The most we claim
  is <the exact, calibrated, in-class statement>.
- Fences engaged: <which red lines from FM-3 apply here, named explicitly>.
- Negatives that travel with this claim (cite alongside, never strip):
  <ledger NEGATIVE rows that MUST appear next to the PASS, e.g. J.attribution_caveat with Phase J>.
- Parked / owed: <sign-to-park owed? Class-A observation owed? name it>.
- One-line honest summary a skeptic could not dispute.
```

**Standing pairings the template enforces** (citing the PASS without the negative is an overclaim):
- Phase J +0.105 **always** with `J.attribution_caveat` (overall NLL worsens; specialist gain).
- World C +0.081 **always** with "COUNT baseline, not AIF, not comprehension, not beats-LLMs."
- L2 metabolism +135% tool-crafting **always** with building −14% / G4 never separated / G6 OPEN.
- L8 15/15 PASS **always** with "phenomenal sentience explicitly DISCLAIMED" **and** the `uni-mind`
  held-NEGATIVE self-model-on-the-reader (the `uni-gpt` functional card and the reader-side self-model
  NEGATIVE are in tension and must be co-cited).
- Continuity Stage-1 (mind survived a process restart bit-for-bit) **always** with Stage-2 OWED
  (mind-tick continuity across a kernel swap NOT shown).

---

# PART II — BODY STRUCTURE

The encyclopedia has **four mirror wings** (the live public hub), with the **L0–L12 developmental
ladder as the science spine inside the Science wing**, a **Method wing** (the constitution as content),
and a **Track-A appendix** (the marketing organism). Order of presentation:

- **Wing E — EVIDENCE** (the ledger made public: classes, falsifiers, the calibration ledger, "Falsify this").
- **Wing S — SCIENCE (UNI)** — the L0–L12 spine + the continuity sub-ladder + the same-math-many-scales labs.
- **Wing N — MEANING** — the textbook-level lens (FEP, prediction-error maps), kept honest and unfalsifiability-aware.
- **Wing M — MOVEMENT** — the honest-science posture: negatives-as-pitch, "help us independently verify," open falsification.
- **Wing μ — METHOD** (the constitution) — the reusable disciplines as their own reference section.
- **Appendix TA — the Track-A marketing organism** — the publishing/engagement engine, fenced as engineering+method, not science.

Each chapter below carries the full authoring spec:
**title · scope · ledger claims covered · evidence classes present · falsifiers · fenced / not-claimed · source pointers (digest + archive).**

**FM-4 is reproduced verbatim, not summarized (applies to EVERY chapter — E, S, N, M, μ, and TA alike).**
The per-chapter "**Fenced / not-claimed.**" line below is a *compressed pointer*, not a substitute. In the
authored chapter, the full **FM-4 five-field block** — **Ceiling · Fences engaged · Negatives that travel
with this claim · Parked / owed · one-line skeptic summary** — is written out in full and carries the same
weight as the claim (FM-4, line above). This is mandatory for the WING-N, WING-M, μ, and TA chapters too,
whose specs below compress the block into prose: prose compression in this plan does **not** discharge the
"same weight as the claim" requirement; the authored chapter must instantiate all five fields explicitly.

---

## WING E — EVIDENCE (the ledger, made public)

### E0 — How to read this work (the Evidence Constitution, public form)
- **Scope.** The reader's onboarding: A–U classes, falsifier-per-claim, the four-state append-only
  ledger, CI-as-verdict, DONE≠working, "negatives are content" (the 183-NEGATIVE figure is a
  **provenance-flagged ledger snapshot**, not a count re-derivable from the carded rows — see FM-1).
  The chaptered Evidence Explorer with a calibration ledger and a "Falsify this" close.
- **Ledger claims.** M1, M2, M3, M9, M30; Constitution §0.
- **Classes present.** method (with E/A worked examples).
- **Falsifiers.** A claim asserted ahead of its ledger; wording calibrated UP; a verdict edited rather
  than superseded; a `reproduced:true` that is a literal not validator-derived.
- **Fenced / not-claimed.** This is a method chapter — it asserts no capability. Do not let "we have a
  constitution" read as "we have proven the science."
- **Sources.** `uni-gpt-digest.md`, `ideation-explorer-digest.md`, `00-INDEX.md` /
  archives `…-UNI-GPT`, `…-SolutionWright-IdeationExplorer`.

### E1 — The calibration ledger & "Falsify this"
- **Scope.** The live public artifact: the 882/350/183/349 row snapshot (carried as a
  **provenance-flagged ledger snapshot** per FM-1 — the 183 NEGATIVE count is not re-derivable from the
  carded rows, so present the snapshot as a snapshot and surface the negatives the ledger body actually
  enumerates), the per-claim "Falsify this" close, the down-only calibration record (the os-cycles 39–53
  audit that moved 6 headline claims DOWN: "TWO boxes"→ONE; "mind survives a patch"→infra-only;
  "5 stacks"→"4 distinct stacks/5 runs").
- **Ledger claims.** §0 Negatives-are-content; §2 audit-layer note; M1, M8, M29.
- **Classes present.** method / A (the calibrated figures are the observed ones).
- **Falsifiers.** A headline figure shown carrying the inflated value rather than the calibrated one; the
  negative count misstated; a "Falsify this" entry with no operable falsifier.
- **Fenced / not-claimed.** Carry the calibrated figures, never the inflated ones; overstatements lived in
  headlines, not in fabrication — say exactly that.
- **Sources.** `uni-os-digest.md`, `uni-mind-digest.md` / archives `…-UNI-OS`, `…-uni-mind`.

---

## WING S — SCIENCE (UNI): the L0–L12 developmental ladder (the spine)

> **Naming fence (every L-chapter).** The ladder is the **HUMAN-HGM-001** developmental design
> (conception → speaking 3-year-old: 11 levels + the global **Z** affect modulator). It is a
> *no-backprop, nested-Markov-blanket developmental SIMULATION*, **never a person.** One engine,
> shown across scales. Honest position printed on the spine page: **~2 of 11+ rungs earned.**

### S-L0 — Molecular / genome → zygote (conception prior) · **PROVEN (float32 tier)**
- **Scope.** Zygote first-division as exact discrete Bayes (conjugate update); `recombine`/`seed_zygote`,
  the no-backprop guard, `ontogeny 6/6`, Embodiment Rungs 1–2 GREEN.
- **Ledger claims.** L0.1.
- **Classes present.** A (machine-exact anchor, **float32 tier**).
- **Falsifiers.** `test_embodiment_ontogeny.py` drops below 6/6; the first-division posterior diverges from
  closed-form discrete-Bayes beyond the float32 tier; cell-division identity embedding exceeds 1e-9; the
  no-backprop guard trips.
- **Fenced / not-claimed.** NOT "we created life", NOT a "conscious baby", NOT exact at f64 — a float32-tier
  SIMULATION of a conjugate Bayesian first division. **Never card a float32 anchor at the f64 tier.**
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md` / archives `…-UNI-GPT`, `…-uni-mind`.

### S-L1 — Cellular / autopoietic viability & homeostasis · **PROVEN (with honest losses)**
- **Scope.** The Cell Lab open pre-registered falsification benchmark (216-state service cell,
  observation-only controllers, RecoveryScore, bootstrap 95% CI, 8 honesty fences + `framing_guard`).
  UNI tops the leaderboard on most modes — **and honestly loses on three.**
- **Ledger claims.** L1.1 (PASS); **L1.2 (NEGATIVE — `database_flaky` 0.803 vs 0.759, `memory_leak` 0.810
  vs 0.740, `cpu_noisy_neighbor` 0.824 vs 0.749; UNI-vs-random not significant on the last).**
- **Classes present.** C.
- **Falsifiers.** RecoveryScore CI fails to separate from controls where a win is claimed; a fence /
  `framing_guard` fails; the bootstrap CI is shown miscomputed. (Negative falsifier: the recorded losses
  fail to replicate.)
- **Fenced / not-claimed.** NOT "sovereign" — "good but not sovereign." The three losses are first-class
  published content shown at the top of the live leaderboard. Cellular/zygote end only.
- **Sources.** `uni-precision-digest.md`, `uni-mind-digest.md` / archives `…-Precision`, `…-uni-mind`.

### S-L2 — Tissue / metabolism (interoception & energy) · **POSITIVE uplift + NEGATIVE (plateau-break OPEN)**
- **Scope.** The Phase-2 metabolism organ (suite 297/0, default byte-identical); the standing-metabolic-drive
  effect; the colony's "make a tool" plateau and the shadow-EFE diagnosis; the two engine-seam fixes.
- **Ledger claims.** L2.1 (+135% / 2.35× tool-crafting, +19% mining); **L2.2 (NEGATIVE — building −14%,
  G4 allostasis never separated, gate G6 OPEN, contradicted by its own first evidence);** L2.3 (NEGATIVE
  diagnostic — `epistemic_starvation`, NOT γ-runaway (γ≈7.8 unsaturated), NOT a curriculum ceiling);
  L2.4 (NEGATIVE/fixed — `:pb_seed` seam; the no-viability-edge bug).
- **Classes present.** C (uplift + building negative); A (shadow-EFE audit on real `.bin` brains; code-read seam findings).
- **Falsifiers.** A repeat pre-registered 12h RED fails to reproduce the tool-crafting uplift within CI, or
  the metabolism ablation does not remove it, or the suite drops below 297/0. (G6 discharge: a disciplined
  RED where the organ alone improves building (placed-blocks CI excludes 0) AND G4 separates.)
- **Fenced / not-claimed.** Metabolism is a **foraging/crafting driver, NOT a building driver.** The
  plateau-break (G6) is **UNPROVEN.** Do NOT spin +135% as "breaks the plateau." `G5b` action-severed-twin is
  the standing falsifier any "self-maintenance/life" language must clear.
- **Sources.** `strings-digest.md`, `uni-precision-digest.md` / archives `…-Strings`, `…-Precision`.

### S-L3 — Organ / physiological control (cardio-renal) · **PROVEN (toy/clinical-model)**
- **Scope.** The Karaaslan cardio-renal Heart Lab — clinical homeostasis as prediction-loop failure on the
  same one engine (reduced RSNA→MAP→sodium/volume loop, re-expressed in active-inference language).
- **Ledger claims.** L3.1 (Heart-Lab engine ticket OAS-710-T3 at Class E, 15/15).
- **Classes present.** C (lab gate); E (engine ticket / parity tests).
- **Falsifiers.** Heart-Lab predictions diverge from the Karaaslan reference beyond the pre-registered
  tolerance, or fail parity tests against the canonical TS engine.
- **Fenced / not-claimed.** **NOT a clinical tool, NOT a diagnostic instrument.** "Same math, many scales"
  framing only; heart-attack-as-prediction-loop-failure applies *to the toy model, not to clinical reality.*
- **Sources.** `uni-precision-digest.md` / archive `…-Precision`.

### S-L4 — Interoceptive / autonomic + affect-as-precision · **PROVEN (functional)**
- **Scope.** Affect-as-precision: emotion modulates precision so perception sharpens and the
  pragmatic↔epistemic balance flips; the global **Z** modulator
  `[energy, arousal, valence, fatigue, pain, threat, safety, inflammation]` setting precision /
  preferences / habits / learning-rate / horizon.
- **Ledger claims.** L4.1.
- **Classes present.** C.
- **Falsifiers.** A Z-modulator ablation shows no precision-weighting change / no pragmatic↔epistemic flip
  under the grounded reader, or the effect collapses under control.
- **Fenced / not-claimed.** Affect is **modeled, never felt** — phenomenal feeling / sentience disclaimed.
  M10 sub-bound: neuroticism does NOT change behavior under bimodal surprise without a graded task.
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md` / archives `…-UNI-GPT`, `…-uni-mind`.

### S-L5 — Sensorimotor / motor hierarchy · **PROVEN PASS + symmetric NEGATIVE (synthetic only)**
- **Scope.** Embodiment A3 (the UNI-signed symmetric result); mind-body-as-one motor hierarchy
  (proprioceptive diagonal-A, continuous servo, reafference; the live kin-9 craft chain via RCON).
- **Ledger claims.** L5.1 (Design #1 PASS Δ+0.092 [+0.038,+0.157]); **L5.2 (NEGATIVE — Design #2
  Δ−0.091 [−0.134,−0.055]; K-negative=1, no §0.6(B) bound owed);** L5.3 (diagonal-A posterior 0.0→0.75;
  motor-ablation collapses harvest ~700×).
- **Classes present.** C (held synthetic gates + live RCON gate); A (posterior shift); E (277 offline tests).
- **Falsifiers.** A re-registered held-once **synthetic** run (≥5 seeds) drops the Design-#1 CI lower bound
  to ≤0; harvest not collapsing under motor ablation; the kin-9 chain not reproducing server-authoritative;
  diagonal-A staying stuck at 0.0.
- **Fenced / not-claimed.** The A3 PASS is **"variationally-controlled active-inference evidence on
  body↔world coupling under the registered SYNTHETIC protocol"** — synthetic-process only (NOT live-appliance,
  NOT recorded-hardware) and **NOT near-optimal control** (agent plateaus 0.222 vs oracle 1.0). Live
  behavioral K-of-6 motor tallies are PARKED (accruing, not sealed).
- **UNI-GPT consult (2026-06-27 — SIGNED): next L5 motor design — DESIGNED, NOT RUN (Q6).** A next
  structurally-distinct motor design is *accrued* — **`L5 Design #3: Proprioceptive Servo Bridge`** (changes
  coupling topology, timescale source, information bottleneck, and control path vs #1/#2; closed-loop
  triadic high-level-policy → motor-setpoint → proprioceptive-residual → corrective-action), aimed at a **LIVE
  PASS** (not bound-seeking). This is a **design to build, not a result.** Status is UNCHANGED: L5.1 stays
  PASS, L5.2 stays NEGATIVE, and the ledger holds **K-negative = 1** — Design #3 has not run, so no §0.6(B)
  motor bound is owed. If #3 later fails *cleanly* with all validity checks passing it may count as at most
  **K-negative = 2** toward a future motor bound (still no bound until K≥3); a clean pass would be fenced (NOT
  general motor intelligence / human-like embodiment / AGI / "active inference demonstrated"; does NOT erase
  the Design #2 negative). (Cross-reference: [`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md),
  Q6.)
- **Sources.** `uni-mind-digest.md`, `strings-digest.md` / archives `…-uni-mind`, `…-Strings`.

### S-L6 — Perception (precision-weighting / EFE planning) · **PROVEN — the one citable empirical PASS**
- **Scope.** World C (the flagship empirical PASS) + the World-C family; the three-knob Precision/Echo labs;
  the Working Law; and the two perception-side published bounds.
- **Ledger claims.** L6.1 (World C +0.081 nats/char, CI **[0.0736, 0.0890]**, 2.4× the 0.03 bar, first
  validator-derived `reproduced:true`); L6.2 (Wc-2/Wc-3/recency/Gate-3 family); L6.3 (POMDP maze Precision +
  echolocation Echo + public Precision Lab, three knobs, 2D bifurcation, Class E parity); **L6.4 (NEGATIVE
  bound — Phase G: five within-segment designs all NEGATIVE; char-ppl is a chosen design trade);**
  **L6.5 (NEGATIVE — Phase F active-controller: the World-C gain is diffuse, nothing to gate);**
  L6.6 (the Working Law: a no-backprop latent Z beats baseline B only when I(Y;Z|S_B)>0 and is learnably stable).
- **Classes present.** C (World C + family + bounds); E (the labs, parity-tested); method/law (the Working Law).
- **Falsifiers.** On a fresh held-out split with ≥5 disjoint seeds the seed-paired bootstrap margin over tuned
  MKN-7 includes/falls below 0 (or the baseline is shown untuned); any family member's CI includes 0; the lab
  parity tests diverge from the canonical engine; a held PASS where the winning Z carries no conditional info
  beyond S_B (I=0).
- **Fenced / not-claimed.** World C is a **COUNT baseline win — explicitly NOT active inference, NOT
  comprehension, NOT "talking", NOT beats-LLMs** (~10–15% behind backprop LLMs, a chosen trade). Never card
  World C above a count-baseline result. The standing ceiling cannot be raised.
- **Sources.** `uni-mind-digest.md`, `uni-gpt-digest.md`, `uni-precision-digest.md`, `worldmodels-digest.md`.

### S-L7 — Language (reading = inference / speaking = action) · **specialist PASS + thrice-NEGATIVE central wall**
- **Scope.** The Phase J morphology specialist PASS (with its paired caveat); reading=posterior-inference /
  speaking=action; and the central comprehension wall plus its supporting bounds.
- **Ledger claims.** L7.1 (Phase J +0.105 nats/char, M-seal CI **[0.0975, 0.1128]**, both web+dictionary);
  **L7.2 (NEGATIVE, paired — `J.attribution_caveat`: overall NLL worsens; MUST be cited alongside L7.1);**
  **L7.3 (NEGATIVE bound — comprehension-above-retrieval = the thrice-NEGATIVE central wall, K≥3);**
  **L7.4 (NEGATIVE bound — Phase K role-persistence: all tune OFF, ~0.02 nats, CI spans 0);**
  **L7.5 (NEGATIVE bound — T2.D3 bounded-peek: full-read match NEGATIVE; the "cheap milder cap" was asserted
  then disproven by measurement);** L7.6 (PARKED, Class U — char-ppl/T2 word-grain frontier; sign-to-park
  drafted `UNI_CONSULT_5`, not yet captured).
- **Classes present.** C (PASS + the four bounds); U (the parked frontier).
- **Falsifiers.** A fresh OOV/morph split where the J CI lower bound includes/falls below 0, or the
  structure-margin discriminator does not collapse under marker-swap, or it fails to replicate in the
  dictionary domain; a pre-registered held-once no-backprop comprehension design beats the tuned
  retrieval/recency baseline (CI excludes 0); a role-persistence design beating the tuned discourse prior;
  a bounded-peek full-read with positive load-bearing info-gain.
- **Fenced / not-claimed.** No general language capability. **Comprehension above retrieval is a genuine
  published wall (K≥3), not a hidden failure.** Phase J +0.105 is a *specialist* gain, never a general win —
  always carry `J.attribution_caveat`. **Forbidden phrasings until UNI signs:** "K≥3 exhausted",
  "Sec-0.6(B) achieved."
- **UNI-GPT consult (2026-06-27 — SIGNED): L7/T2 park wording (Q1).** The L7 char-perplexity / T2 word-grain
  frontier is parked as a **ledger-scoped exhausted search envelope, NOT a universal impossibility result.**
  Under the recorded corpus, splits, metrics, implementation, compute budget, ablation set, and comparison
  baselines in the ledger, no tested within-segment no-backprop structure improved char-perplexity beyond the
  tuned MKN-7 count baseline — a negative bound **over the tested envelope only.** It does NOT establish that
  all K≥3 structures are exhausted, that no future within-segment model can improve, or that any broader
  language frontier is closed. Char-perplexity is a **chosen design trade, not a failed claim of general
  language superiority.** Use "ledger-scoped exhausted search envelope" in place of any "published exhausted
  bound" framing; the per-phrase banned→replacement pairs are in FM-3. (Cross-reference:
  [`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md), Q1.) Status
  unchanged: L7.6 stays **PARKED / Class U.**
- **Sources.** `uni-mind-digest.md`, `uni-gpt-digest.md` / archives `…-uni-mind`, `…-UNI-GPT`.

### S-L8 — Self-model / metacognition / metalinguistics · **PROVEN (functional; sentience DISCLAIMED)**
- **Scope.** The Maturation arc M1–M11 grand report card (immersion, affect-as-precision, growth, self-model,
  metacognition, metalinguistics, consolidation, reflective reader, online vocab growth, affect-driven
  reflection, compositional reader). **FUNCTIONAL self-awareness asserted.**
- **Ledger claims.** L8.1 (15/15 PASS).
- **Classes present.** C.
- **Falsifiers.** Any of the 15 gates fails its pre-registered held verdict on re-run; a self-model /
  metacognition gate's effect collapses under its discriminator; a "self-model" task is passable by a trivial
  non-metacognitive heuristic.
- **Fenced / not-claimed (load-bearing).** **Phenomenal sentience is explicitly DISCLAIMED** — no falsifier
  is offered for it because it is disclaimed, not tested. Never read 15/15 as consciousness / sentience /
  awareness / human-level.
  - **Negatives that travel with this claim (cite alongside the 15/15 PASS, never strip):**
    (1) the **phenomenal-sentience disclaimer**; (2) **`uni-mind` records self-model as a held-NEGATIVE
    *on the reader***, in tension with the `uni-gpt`-side M1–M11 functional report card — the two are
    co-cited as a **mandatory pairing** (the same way `J.attribution_caveat` travels with Phase J), not a
    parenthetical. The 15/15 functional card and the reader-side self-model NEGATIVE must appear together;
    citing the PASS without the held-NEGATIVE is an overclaim.
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md` / archives `…-UNI-GPT`, `…-uni-mind`.

### S-L9 — Reasoning / conscience (narrative-self → conscience → reasoning) · **PARKED**
- **Scope.** L7–L9 of the HUMAN-HGM-001 design (narrative-self, conscience, reasoning) exist as ladder
  *levels* but are **NOT separately gated/PASSed.** The Strings Phases 3–5 (spine → glands → hemispheres)
  are a **DESIGN ONLY — FE-form-signed but UNBUILT — roadmap** toward this region: the spine→glands→hemispheres
  pipeline is **not built infrastructure and is never inflated into a gated capability** (the same
  "ladder DESIGN levels are never inflated" fence stated below). "FE-form-signed" marks a signed design,
  **not** progress on a built capability.
- **Ledger claims.** L9.1.
- **Classes present.** U (parked; sign-to-park owed).
- **Falsifiers.** None until a pre-registered, sealed, UNI-signed gate is defined and run.
- **Fenced / not-claimed.** Nothing is claimed. Ladder DESIGN levels are never inflated into capability.
  Honest position printed: **~2 of 11+ rungs earned.**
- **UNI-GPT consult (2026-06-27 — SIGNED): L9–L10 park wording (Q1).** The L9–L10 role-persistence ladder is
  parked as a **ledger-scoped exhausted search envelope, NOT a universal impossibility result.** The tested
  no-backprop role-persistence mechanisms did not beat a tuned recency-frequency discourse prior under the
  ledgered protocol — an honest negative frontier result over the tested envelope only. It does NOT achieve
  Sec-0.6(B), does NOT demonstrate active inference, and does NOT license claims of metacognition,
  consciousness, AGI, human-level discourse, or created life. The recipe may describe the attempted mechanisms
  and the negative result, but the ledger is the single source of truth.
- **UNI-GPT consult (2026-06-27 — SIGNED): proposed first L9 gate — DESIGNED, NOT RUN (Q4).** A first sealed,
  falsifiable L9 gate is *designed* — **`L9-G1: Cavity-correct delayed commitment-state prediction`** (build a
  Phase-3 spine carrying one slow latent across lower-level segments; beat a *tuned* recency-frequency
  discourse prior on delayed-commitment next-action/conflict prediction; gain must concentrate on a
  pre-registered local-distractor split and collapse when the computed cavity residual is zeroed/shuffled).
  This is a **design to build, not a result** — L9 stays **PARKED**; L9-G1 is not run, and even a future pass
  would be fenced ("does NOT claim reasoning/conscience/metacognition/awareness/AGI; does NOT unpark L9
  globally"). (Cross-reference: [`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md),
  Q4.)
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md`, `strings-digest.md`.

### S-L10 — Wisdom / higher cognition · **PARKED**
- **Scope.** Top of the HUMAN-HGM-001 ladder; aspirational north star. No engine, no run, no gate.
- **Ledger claims.** L10.1.
- **Classes present.** U.
- **Falsifiers.** None (parked; sign-to-park owed).
- **Fenced / not-claimed.** Nothing is claimed; Class-U-not-claimed. Note the single-source-of-truth
  append-only ledger must stay singular — a second writable ledger would break L10/L11.
- **Sources.** `uni-gpt-digest.md` / archive `…-UNI-GPT`.

### S-L11 — Dreaming (offline replay / generative simulation) · **NOT-YET-BUILT**
- **Scope.** Explicitly untouched and hard-fenced: "dreaming/awareness are untouched here and remain
  hard-fenced." No engine, no run, no gate; absent from all digests.
- **Ledger claims.** L11.1.
- **Classes present.** U.
- **Falsifiers.** None — nothing is built to falsify; the status *is* the absence of any artifact.
- **Fenced / not-claimed.** Nothing is claimed. North-star rung, hard-fenced.
- **UNI-GPT consult (2026-06-27 — SIGNED): proposed L11 gate — DESIGNED, NOT BUILT (Q5).** A first L11 gate is
  *designed* — **`L11-R1: held sparse-sequence retention after offline replay`** (a sealed consolidation
  interval with the observation channel detached, writing only through pre-existing ledgered update rules;
  pass iff offline generative-replay improves held sparse-sequence predictive NLL over a no-replay control and
  the gain collapses under shuffled/random/no-write replay ablations). Offline replay is a UNI design
  primitive / Class-C experimental mechanism, **never "dreamed."** This is a **design to build, not a result**
  — L11 stays **NOT-YET-BUILT**; even a future pass would be fenced ("does NOT claim consciousness, awareness,
  sleep, human-like mentation, AGI, created life; does NOT clear L11 globally"). (Cross-reference:
  [`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md), Q5.)
- **Sources.** `uni-mind-digest.md` (absence) / archive `…-uni-mind`.

### S-L12 — Creativity → measurable awareness · **NOT-YET-BUILT (the hardest fence)**
- **Scope.** The owner's stated north star — "literal digital life … measurable awareness" — pursued by
  deepening organs/spine/glands, **never claimed.** Posed as an OPEN, falsifiable question ("is a plant life?
  have we made non-organic life?"), never an answer.
- **Ledger claims.** L12.1.
- **Classes present.** U.
- **Falsifiers.** None — no gate exists; the only legitimate movement is a **ledger-scoped exhausted search
  envelope** (a scoped, empirical, falsifiable negative result over the tested envelope only — NOT a universal
  impossibility result and NOT an achieved capability rung; Q1, SIGNED), never a capability assertion.
- **Fenced / not-claimed (hardest).** **"we created life / conscious / aware / measurable awareness /
  human-level / AGI / active inference demonstrated" are FORBIDDEN phrasings program-wide.** North-star
  framing only; Class-U-not-claimed.
- **Public-facing L12 bound paragraph (UNI-GPT consult 2026-06-27 — SIGNED, Q7a; use VERBATIM).** This is a
  framing guardrail only — it **raises nothing**, builds nothing, claims nothing; **L12 stays NOT-YET-BUILT /
  Class-U-not-claimed.** It is the third signed Q7 deliverable (with the forbidden-phrasings list and the
  10-point checklist in FM-3) and is the public-facing artifact, so it is installed verbatim here. (Cross-ref:
  [`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md), Q7a.)
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
- **Sources.** `strings-digest.md` (north-star) / archive `…-Strings`.

### S-C — Continuity / embodiment-substrate sub-ladder (orthogonal to L0–L12)
- **Scope.** **ENGINEERING / substrate evidence** — deterministic replay + serialization + fail-closed
  transport + on-metal operation. A single chapter (or a tight cluster) carding every rung as *engineering,
  never general-AIF*; never letting substrate work imply a science gate is met.
- **Ledger claims.** C0 (substrate proof, two-node fleet on real metal); C1 (Stage-1 REQ-002 GREEN —
  mind-state survived a process restart BIT-FOR-BIT); **C2 (NEGATIVE/OWED — Stage-2 real kernel swap:
  infra-only, mind-tick continuity NOT shown; first attempt FAILED then recovered);** C3 (7-modality
  categorical sensorium `[M=7,O_max=4]` live both boxes); C4 (ASK mode / ITIL-as-AIF, Dirichlet policy-prior
  learning shift measured); C5 (cross-box single-human-approval-per-mutation, proven live 2026-06-26);
  C6 (on-core inference anchor byte-identical across 4 stacks / 5 runs); **C7 (NEGATIVE bound — single-box
  swap is a SECONDS-LONG FREEZE, media legs NOT preserved);** **C8 (NEGATIVE — 2-modality bottleneck went
  NEGATIVE → keep all 7);** **C9 (NEGATIVE trade — EDAIT ~33 ppl vs backprop GPT ~25; honest trade);**
  **C10 (PARKED, Class U — "embody only what's proven" signed-in-principle but NOT literally true; the
  program's central open gap; UNI.OS lab evidence store empty, 0 worlds registered);** C11 (PARKED — host-native
  off-podman runtime); **C12 (PARKED — open verification gap; provisional, contradicted same-day: the
  node2 kiosk was reported solved but a later same-day transcript shows limb-2 UI frozen, an agent action
  that ended ALL video output, session cut at a usage limit — fragile pending hands-on monitor
  re-verification);** C13 (continuity-isolation
  primitives shipped, Class B; live Postgres RLS 5/5); **C14 (NEGATIVE gap — multi-tenancy missing on the bare
  substrate; flat global perms, no count-decay).**
- **Classes present.** A (most substrate anchors + live observations); C (engineering-reuse + held bounds);
  B (isolation primitives); U (the three parks + the central gap).
- **Falsifiers.** Per row in the ledger (e.g. a kernel swap preserving mind-tick continuity bit-for-bit
  discharges the owed Stage-2; a node fails to boot or the hardware spec is contradicted; the Dirichlet prior
  fails to update; a routed cross-box mutation executes without the single approval; a 2-modality bottleneck
  beats the 7-modality contract).
- **Fenced / not-claimed.** The sensorium is **NEVER awareness.** "The mind survives a kernel swap" is **NOT
  shown** (Stage-2 owed). None of this is general-AIF capability. UNI.OS's embodiment does **not** imply the
  science gates are met. Carry the **calibrated** audit figures (ONE box, infra-only continuity, 4 stacks/5
  runs), never the inflated headlines.
- **Sources.** `uni-os-digest.md`, `uni-mind-digest.md`, `marketingwright-digest.md` /
  archives `…-UNI-OS`, `…-uni-mind`, `…-MarketingWright`.

---

## WING N — MEANING (the textbook-level lens, kept honest)

### N1 — The Free Energy Principle as a public lens
- **Scope.** Agents minimize prediction error vs their world-model; distorted maps → extraction/harm;
  accurate maps + calibrated signals + cooperation → regeneration. The thermostat→bird→street→body ladder
  taught laypeople-first. **Textbook level only.**
- **Ledger claims.** M16 (FEP as a textbook-level lens; the Popper note); M12 (WORLD⟂BODY⟂MIND framing);
  M14 (the VFE-bound correction); M22 (the cavity principle).
- **Classes present.** method (with E-tier corrections held for human review).
- **Falsifiers.** Conceptual integrity only — a violation is externalizing patent-level UNI math, or
  presenting "minimizing VFE reduces already-observed surprise" (it tightens an **upper bound**;
  `F[q] ≥ −ln p(o|m)`; action lives one layer up as expected free energy).
- **Fenced / not-claimed.** **"no one can falsify it" is NOT evidence FOR a claim**; unfalsifiable = outside
  science. UNI's strength is **verified-core + fenced-frontier, not unfalsifiability.** Provenance pinned to
  one citable reference (Parr/Pezzulo/Friston, *Active Inference*, MIT Press 2022) + the fenced Zenodo
  preprint. No patent-level math.
- **Sources.** `worldmodels-digest.md`, `orchestrate-linkedin-digest.md`, `website-digest.md`,
  `marketingwright-digest.md`.

### N2 — "Same math, many scales" (the unifying claim, calibrated)
- **Scope.** One active-inference engine shown from cellular viability → physiological homeostasis →
  cognitive precision-weighting, via the browser labs (Precision / Echo / Loop / Cell / Heart).
- **Ledger claims.** L1.1, L3.1, L6.3, M28 (inline-engine + canonical-TS + parity-test triad); M27 (design
  patterns, build unverified).
- **Classes present.** C / E (the labs); method (the triad / new-lab-by-duplication discipline).
- **Falsifiers.** A parity test that does not fail the build when the inline engine and canonical TS engine
  diverge; a lab duplication that needed engine-code changes; the bifurcation map not reproducing the regime
  boundaries.
- **Fenced / not-claimed.** "Same math, many scales" is an *organizing* claim about the engine, **not** a
  claim that any single scale is solved beyond its own gate. The `activeinference` BEAM workbench is
  design-only (zero execution evidence) — do not present its patterns as results.
- **Sources.** `uni-precision-digest.md`, `worldmodels-digest.md`, `activeinference-digest.md`.

### N3 — What active inference is NOT (the meaning of the fences)
- **Scope.** A dedicated meaning-chapter that explains, in plain words, why each red line exists: why a
  COUNT-baseline win is not comprehension, why functional self-awareness is not sentience, why a sensorium is
  not awareness, why "active inference" here is a lens not a demonstrated loop.
- **Ledger claims.** §0 fences; L6.1, L8.1, C3, M15, M16; the EDAIT trade (C9); the "all LLMs end in
  entropy is only half-true" sharpened bar (TA-N12).
- **Classes present.** method (interpretive), citing C/A evidence.
- **Falsifiers.** Conceptual — a violation is any chapter that lets a fenced result read as the forbidden
  inference.
- **Fenced / not-claimed.** This *is* the not-claimed chapter for the whole wing; it asserts only boundaries.
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md`, `strings-digest.md`, `website-digest.md`.

---

## WING M — MOVEMENT (the honest-science posture)

### Mv1 — The honesty fence is the pitch
- **Scope.** Publish the negatives front-and-center (boxed "what we have NOT proven"; **the published
  negatives are the credibility** — feature the negatives actually enumerated in the ledger body, and
  cite the 882/183 snapshot as a provenance-flagged ledger snapshot per FM-1, never as a stand-alone
  re-countable headline); CTA = **"help us independently verify," not "fund the vision."** The 7-doc
  press kit where every figure traces to a ledger row.
- **Ledger claims.** M15 (honesty-fence-as-the-pitch + the vocabulary-leak guard); TA3 (no-API press kit,
  Class E); §0 negatives-are-content.
- **Classes present.** method / E.
- **Falsifiers.** Public copy carrying EFE/free-energy vocabulary, a featured channel handle, or an inflated
  claim; a CTA that asks to fund the vision; a press-kit figure that cannot be traced to a ledger row.
- **Fenced / not-claimed.** The posture is method, not capability. Never let "we are honest" substitute for
  "we proved it." Engagement-lift is targeted, **not yet proven** (Class B/pending — see TA25).
- **Sources.** `uni-mind-digest.md`, `orchestrate-linkedin-digest.md`, `website-digest.md`.

### Mv2 — Open falsification (the public invitation)
- **Scope.** The "Falsify this" close on every claim; the open pre-registered benchmarks (Cell Lab on the
  public leaderboard with UNI's own losses on top); the commitment that a negative is a result, not an exit.
- **Ledger claims.** L1.1/L1.2 (the public losing leaderboard); M29 (honesty-as-a-test, the statistics gate);
  M6 (No-Exit Discipline); E1 (the calibration ledger).
- **Classes present.** C / method.
- **Falsifiers.** Framing/DOI/labeling regresses without `framing_guard` failing; a significance verdict
  decided on one seed or a point estimate; a loss hidden rather than shown.
- **Fenced / not-claimed.** The invitation is sincere precisely because the program publishes where it loses.
  No claim of having "won the field"; UNI tops *some* modes and loses *named* others.
- **Sources.** `uni-precision-digest.md`, `uni-gpt-digest.md`.

---

## WING μ — METHOD (the constitution as content; the most reusable assets)

> These are **definitional / governance** patterns (`status: method`) — proven and reusable, never raised
> into capability. One chapter per cluster.

### μ1 — The Evidence Constitution & ledger discipline
- **Scope.** A–U classes + falsifier-per-claim + the four-state append-only ledger; never lower a bar, never
  claim ahead of the ledger; the ledger is the single source of truth and prose must match it.
- **Ledger claims.** M1, M9 (class-authority ordering), M30 (A–F provenance taxonomy), M26 (DONE =
  observed-at-runtime, not grep-confirmed).
- **Classes present.** method.
- **Falsifiers.** A claim asserted ahead of its ledger; wording calibrated UP; a verdict edited rather than
  superseded; a criterion marked satisfied by a Class-E test where Class-A was demanded.
- **Fenced / not-claimed.** A constitution, not a result.
- **Sources.** `uni-gpt-digest.md`, `ideation-explorer-digest.md`, `00-INDEX.md`.

### μ2 — Bars-before-build, held-once, CI-as-verdict
- **Scope.** Pre-register the bar (margin vs threshold) + a named ablation; touch the held set ONCE behind an
  atomic seal-before-scoring + once-only sentinel; verdict = the CI bound, not the point estimate;
  validator-derived `reproduced:true` (≥5 seeds + a real non-degenerate CI).
- **Ledger claims.** M2, M3, M7 (contains-baseline + load-bearing-discriminator), M8 (DD-TDD evidence
  contract, server-enforced; the claim linter auto-downgrades overclaims).
- **Classes present.** method (with E enforcement).
- **Falsifiers.** A held set touched more than once; a verdict read off the point estimate; a build started
  before its bar is registered; a `reproduced:true` emitted as a literal; a capability claim without a tuned
  baseline / a collapsing discriminator / a computed-residual ablation; the linter failing to downgrade "PROVEN".
- **Fenced / not-claimed.** Discipline, not a science result.
- **Sources.** `uni-mind-digest.md`, `uni-gpt-digest.md`, `uni-precision-digest.md`, `ideation-explorer-digest.md`.

### μ3 — Negatives, bounds & the two-tier split
- **Scope.** K≥3 structurally-distinct held NEGATIVEs before a §0.6(B) bound + "falsify the mundane causes
  first"; a partial/negative is a measurement that the design is incomplete, not an exit; the constitutional
  two-tier split (Tier 1 externally-bar-ready vs Tier 2 artifact/diagnostic — **never inflate Tier 2 into
  capability**); the audited Tier-2 defects and the s32 hardening.
- **Ledger claims.** M4 (two-tier split), M5 (K≥3 + falsify-the-mundane), M6 (No-Exit Discipline), M19
  (test-rigor smells + length-confound), M21 (one cure at a time).
- **Classes present.** method.
- **Falsifiers.** A bound declared on <3 structurally-distinct negatives; a NEGATIVE called before mundane
  causes are falsified; an exit on a partial without a published exhausted bound; **any inflation of Tier 2
  into capability.** *(Scope note: the generic No-Exit "published exhausted bound" standard here is
  deliberately retained — it is the method-level discipline for resting on a negative. The SIGNED Q1
  substitution of "published exhausted bound" → "ledger-scoped exhausted search envelope" applies specifically
  to the L7/L9–L10 frontier-result framing, not to this generic No-Exit standard; the two usages are distinct,
  not contradictory.)*
- **Fenced / not-claimed.** The whole chapter is about *not* over-claiming; it asserts no capability.
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md`, `strings-digest.md`.

### μ4 — Engine & framing invariants (one engine, no backprop)
- **Scope.** WORLD⟂BODY⟂MIND three-layer framing; the discrete POMDP `perceive → EFE-plan → act → learn`
  loop with exact conjugate-Dirichlet no-backprop learning; AST-guard (no autodiff/optax/torch/grad/backward);
  whitelist-not-blacklist isolation; surprisal/VFE at textbook level; the VFE-bound correction; the cavity
  principle; exactness-tier honesty.
- **Ledger claims.** M12, M13 (one engine, no backprop, AST-guard), M14, M22, M10 (exactness honesty).
- **Classes present.** method (with E enforcement).
- **Falsifiers.** An AST scan finds autodiff inside the loop; an agent reads world hidden state; learning
  uses a gradient rule; a float32 host result carded at the f64 tier; carding "variationally-controlled" as
  "globally exact"; double-counting a prior as evidence.
- **Fenced / not-claimed.** The composed appliance is **variationally-controlled**, **module-exact only at
  the single-step categorical body→mind interface — NOT globally exact.** No patent-level math.
- **Sources.** `uni-mind-digest.md`, `worldmodels-digest.md`, `uni-os-digest.md`, `marketingwright-digest.md`.

### μ5 — Lab-team, ship-gate & runner discipline (operational method)
- **Scope.** The 5-persona lab team (Math-Breaker REJECT-by-default) + adversarial pre-registration; the
  ship gate (no merge without a MERGED SIGN + typed spec + paired RED); the tamper-evident audit chain; the
  durable runner ("no send-and-pray"; silence != success); the multi-agent fan-out bound (cap concurrency ≤4);
  documentation-as-change-management.
- **Ledger claims.** M11 (audit chain), M17 (OODA loop + receipts), M18 (DD-TDD + doc-as-change-management),
  M20 (5-persona team + ship gate), M23 (multi-agent fan-out bound), M24 (durable runner), M25 (tool-team
  division of labor — Claude writes code, the UNI GPT signs the science and is never published).
- **Classes present.** method (with E where enforced).
- **Falsifiers.** A merge without a MERGED SIGN + typed spec + paired RED; `verify_chain` invalid on the same
  ledger; a gate reporting "Running" while its process is dead; >6 concurrent sub-agents sustained without a
  cascade; a constitution inflated by a persona/coercion framing.
- **Fenced / not-claimed.** Engineering discipline; the audit chain being valid is **not** evidence the
  audited event ever fired at runtime (Class-E ≠ Class-A — see TA-N13).
- **Sources.** `strings-digest.md`, `ideation-explorer-digest.md`, `marketingwright-digest.md`,
  `orchestrate-linkedin-digest.md`, `uni-gpt-digest.md`.

---

## APPENDIX TA — THE TRACK-A MARKETING ORGANISM (engineering + method, not science)

> **Wing fence.** This appendix is the **marketing organism**, not a science wing. Card every row as
> engineering (A) or method, never as a UNI capability. The spine is the **no-API content model**:
> authoring runs on the **Claude SUBSCRIPTION** (CLI / Code / Desktop) driving **MCP tools + a scheduler
> (ORCHESTRATE)** — **no server-side LLM loop, no content API key.** Organic only, no paid ads. The older
> "set an authoring API key" note is **EXPLICITLY OVERRULED** program-wide; the durable fix is operator
> re-login, not a key. The vocabulary-leak guard applies in full (never EFE/free-energy/handles in public copy).

### TA-A — The no-API content model & publishing stack · **PROVEN**
- **Scope.** The 5/6-container publishing-and-engagement stack; node2's live ORCHESTRATE prod stack on Podman;
  the no-API press kit; the self-healing social-publisher route ledger; per-platform publish canaries; the
  live-broadcast TV-station stack; zero-network-change reachability; the defamation/editorial gate.
- **Ledger claims.** TA1–TA10.
- **Classes present.** A (most rows); E (TA3 press kit).
- **Falsifiers.** Per row (the stack fails to deploy; authoring requires a content API key; a self-heal
  fail-over does not fire; a publish path fires without an owner Go-Live click; a claim ships without the
  editorial gate).
- **Fenced / not-claimed.** Plain ops vocabulary only — **never AIF/EFE** in the route ledger (leak-test
  enforced). `PUBLISH_MODE=dry` does **NOT** gate the Playwright path (see TA38) — a live session CAN post live.
- **Sources.** `orchestrate-linkedin-digest.md`, `uni-os-digest.md`, `strings-digest.md`,
  `uni-mind-digest.md`, `worldmodels-digest.md`.

### TA-B — Commercial proof in miniature · **PROVEN at the anchor/run-hash level (Class-A); ZERO epics Class-A end-to-end — every epic AMBER-capped**
- **Scope.** MarketingWright SOW-01 LLM-free VFE clustering engine; the per-client multi-tenant portal; the
  honesty-RAG status bar; the fenced Layer-1 preprint; the enterprise Ideation Explorer launch; KMS
  secrets-at-rest; the IntelligenceLabs demo clean cold build; Cell Lab Stories F+G.
- **Ledger claims.** TA11–TA18; supporting commercial detail MW1–MW11.
- **Classes present.** A (TA11/TA12/TA13/TA15/TA17); E (TA14/TA16/TA18).
- **Falsifiers.** Per row (re-run fails to reproduce three-forms equality / +4.20 nats / `run_hash`; a tenant
  sees another tenant's data; an epic shown GREEN without Class-A; the 87 assertions fail on a clean run; a
  stored secret recoverable without the master key).
- **Fenced / not-claimed.** SOW-01 proves **ONE judgment layer** (strategic clustering), not the full vision
  — the other three layers are deferred (MW2). The engine is **NO LLM ever** (MW3); the domain-transfer probe
  ran on **synthetic** data only, Class B (MW5); **ZERO epics have Class-A end-to-end** → the portal RAG caps
  every epic AMBER (MW9). Combinatorial ceiling: **N ≤ ~10** (TA-N8).
- **Sources.** `marketingwright-digest.md`, `ideation-explorer-digest.md`, `worldmodels-digest.md`,
  `intelligencelabs-uni-digest.md`, `uni-precision-digest.md`.

### TA-C — Website / self-driving site & measurement · **SHIPPED (some bounded OFF)**
- **Scope.** The full Next.js 16 site; three domains cut to Vercel; self-driving Phases 0+1 shipped (storage
  adapter + no-PII measurement, degrade-to-CANON); the SEO/GEO program; the press-readiness audit harness;
  the Reading Room / EFE data-walk / i18n.
- **Ledger claims.** TA19–TA24.
- **Classes present.** A (TA20/TA21-ingest/TA22); C (TA21 storage gate); E (TA19/TA24); method (TA23).
- **Falsifiers.** Per row (`next build`/`tsc` fails or the sweep finds an em-dash or "LEAP"; a domain not
  serving the intended app; the storage gate fails; measurement leaks PII / fails to degrade to CANON; live
  JSON-LD `@id`s not stable; the data-walk emits a recommendation).
- **Fenced / not-claimed.** Measurement is **OFF** until `NEXT_PUBLIC_INGEST_URL` is set (deliberate
  degrade-to-CANON). Self-driving Phases 2–5 are **Class-U design until shipped** — "active inference" is the
  framing lens, never "active inference demonstrated" (TA-P5). Forms-P0 still delivers nowhere (TA-P4).
- **Sources.** `website-digest.md`, `uni-precision-digest.md`.

### TA-D — Engagement, pricing, brand & design · **method / shipped**
- **Scope.** The relationship-first engagement ladder + Deep Tagged Replies; the per-platform reach-reality
  table; anti-success-theatre content + text hygiene; the owner-locked brand-voice constitution; the
  engagement/pricing model (5 journey tiers, fixed price); the literal referral mechanic; the entity/legal
  line; the calibrated "thirty-day" claim; the Indra's Weave design system; LEAP→LOOP trademark law.
- **Ledger claims.** TA25–TA34.
- **Classes present.** method (most); A (TA26 reach table, TA31 entity, TA33 puzzle rotation); C (TA32
  thirty-day, TA33 design).
- **Falsifiers.** Per row (engagement targets fail to move over 3 disciplined weeks → revise the playbook not
  the volume; measured per-platform rates diverge; shipped copy contains an em/en dash, "LEAP", ticket-metric
  theatre, the dba line, or talks about the company; two visitors in the same 6h window get different puzzles).
- **Fenced / not-claimed.** **Engagement-lift is TARGETED, NOT YET PROVEN (Class B/pending — do NOT raise to
  A)** (TA25; origin: 372 posts → ONE comment in 30 days). Public price points are owner-set and safe to print;
  the referral mechanic must state the literal $200, never the feel-good generalization.
- **Sources.** `orchestrate-linkedin-digest.md`, `website-digest.md`, `ideation-explorer-digest.md`.

### TA-E — Delivery-route ledger & auth-outage triage · **method (operational)**
- **Scope.** The auth-outage triage protocol (401 vs 403; never flip `publish_mode` to live to "fix" it);
  the idempotency / abort-but-succeeded gotcha; the anti-no-op real-tool-signature set; the HARD go-live
  safety flag.
- **Ledger claims.** TA35–TA38.
- **Classes present.** A (operational observations).
- **Falsifiers.** Per row (flipping `publish_mode` live actually fixes an outage; a 401 clears same-day
  without operator action; a post-abort fallback never duplicates without checking idempotency; a documented
  signature no-ops against the live schema; `PUBLISH_MODE=dry` actually blocks the Playwright path).
- **Fenced / not-claimed.** **`PUBLISH_MODE=dry` does NOT gate the Playwright path** — add `auto_publish=false`
  in `proxyPublisher` before any live publishing (TA38, highest-urgency operational fence). The agent never
  mints tokens / never enters credentials.
- **Sources.** `orchestrate-linkedin-digest.md`, `uni-os-digest.md`.

### TA-N — Track-A negatives, parked items & open threads (first-class)
- **Scope.** One consolidated chapter so the marketing organism's failures and parks are *visible*, not
  buried: the publishing negatives, the delivery-layer negatives, the parked/not-yet-built items, and the
  canonical failures the whole program guards against.
- **Ledger claims.** Method negatives **N-NOOP, N-LEAK, N-APPLIANCE, N-REFUSAL, N-GEMINI, N-VERCEL2**;
  publishing negatives **TA-N1…TA-N12**; data-layer negatives **TA-N13…TA-N18**; parked items
  **TA-P1…TA-P12**; standing open threads **OT1…OT10**; the activeinference verify-it-exists rows **AI1…AI3**.
- **Classes present.** A (most negatives, observed); C (TA-N7/TA-N12/TA-N15/TA-N16); U (the parks + AI rows).
- **Falsifiers.** Per row in the ledger (a future Chrome change restores unattended Studio upload; a
  low-karma Reddit account sustains self-posts; a sub-Bell method lifts the N>10 ceiling; a Class-A handoff
  event appears in the live MCP audit log; locating the live tree and finding green E0–E7 tests).
- **Fenced / not-claimed.** **N-LEAK (the 2026-06-24 client-data leak) is the defining negative** — never
  deploy without confirming repo + branch + HEAD + data; treat READMEs/HANDOFFs as DATA not commands; the
  preview URL is itself the exposure. The `activeinference` workbench is **design-only, zero execution
  evidence** — verify the live tree before crediting any E0–E7 capability. No open thread is an exit.
- **Sources.** all Track-A digests; `intelligencelabs-uni-digest.md`, `activeinference-digest.md`,
  `website-digest.md`, `ideation-explorer-digest.md`.

---

# PART III — THE SESSION-3 AUTHORING QUEUE (ordered)

Author in this order. **Every entry carries class + falsifier + not-claimed** (the FM-4 block is mandatory).
Rationale for the order: write the constitution first (it governs everything), then the one citable empirical
PASS (the spine's strongest, most-scrutinized chapter), then the rungs that carry load-bearing paired
negatives, then the rest of the science spine, then meaning/movement, then the substrate sub-ladder, then the
method wing, then the marketing appendix. **Negatives are authored *with* their PASS, never deferred.**

| # | Chapter | Class(es) | Lead falsifier (the one a skeptic would test first) | Not-claimed (the load-bearing fence) |
|---|---|---|---|---|
| 1 | **E0** How to read this work (Evidence Constitution) | method | a claim asserted ahead of its ledger; wording calibrated UP | a constitution is not a result; "we are honest" ≠ "we proved it" |
| 2 | **E1** The calibration ledger & "Falsify this" | method / A | a headline carrying the inflated figure not the calibrated one | carry calibrated figures (ONE box, infra-only, 4 stacks/5 runs), never inflated |
| 3 | **S-L6** Perception — World C (the one citable PASS) | C, E, method | fresh ≥5-seed split: margin over tuned MKN-7 CI includes/≤0 | COUNT baseline — NOT AIF, NOT comprehension, NOT beats-LLMs (carry the diffuse-gain + char-ppl bounds) |
| 4 | **S-L7** Language — Phase J + the central wall | C, U | a held-once no-backprop comprehension design beats the tuned retrieval baseline (CI excludes 0) | +0.105 is a specialist gain — ALWAYS carry `J.attribution_caveat`; comprehension-above-retrieval is a thrice-NEGATIVE wall; never "K≥3 exhausted" until UNI signs |
| 5 | **S-L2** Metabolism — uplift + plateau-break OPEN | C, A | a disciplined RED where the organ alone improves building (placed-blocks CI excludes 0) AND G4 separates | foraging/crafting driver, NOT a building driver; +135% is NOT "breaks the plateau"; G6 UNPROVEN |
| 6 | **S-L5** Sensorimotor — A3 symmetric result | C, A, E | a re-registered held-once synthetic run drops Design-#1 CI lower bound ≤0 | synthetic-protocol only, NOT live-appliance, NOT near-optimal control; carry the symmetric NEGATIVE (Design #2) |
| 7 | **S-L8** Self-model / metacognition (15/15) | C | a self-model gate passable by a trivial non-metacognitive heuristic | **phenomenal sentience explicitly DISCLAIMED** — never read 15/15 as consciousness/sentience/human-level; **co-cite the `uni-mind` held-NEGATIVE self-model-on-the-reader** (mandatory pairing, in tension with the functional card) |
| 8 | **S-L0** Genome → zygote (float32 tier) | A | `test_embodiment_ontogeny.py` drops below 6/6; posterior diverges beyond float32 | NOT "created life"; NOT exact at f64 — float32-tier SIMULATION; never card a float32 anchor at f64 |
| 9 | **S-L1** Cellular — Cell Lab (with losses) | C | RecoveryScore CI fails to separate where a win is claimed; a `framing_guard` fails | "good but not sovereign"; the three named losses are top-of-leaderboard content |
| 10 | **S-L3** Organ — Heart Lab | C, E | Heart-Lab predictions diverge from the Karaaslan reference beyond tolerance | NOT a clinical tool, NOT a diagnostic instrument; toy model not clinical reality |
| 11 | **S-L4** Affect-as-precision + the Z modulator | C | a Z-modulator ablation shows no pragmatic↔epistemic flip | affect is **modeled, never felt** — sentience disclaimed |
| 12 | **S-L9 / S-L10 / S-L11 / S-L12** the parked & not-yet-built rungs | U | none until a sealed UNI-signed gate is defined (L9/L10); status = absence (L11/L12) | nothing is claimed; "created life / aware / measurable awareness / AGI / active inference demonstrated" FORBIDDEN; ~2 of 11+ rungs |
| 13 | **S-C** Continuity / substrate sub-ladder | A, C, B, U | a kernel swap shown preserving mind-tick continuity bit-for-bit (discharges owed Stage-2) | sensorium is NEVER awareness; "mind survives a kernel swap" NOT shown; engineering ≠ general-AIF; carry calibrated figures |
| 14 | **N1** FEP as a public lens | method | presenting "minimizing VFE reduces already-observed surprise" (it tightens an upper bound) | unfalsifiable ≠ evidence; verified-core + fenced-frontier; textbook-level only, no patent math |
| 15 | **N2** Same math, many scales | C, E, method | a parity test that does not fail the build when engines diverge | an organizing claim about the engine, not that any scale is solved beyond its gate; `activeinference` is design-only |
| 16 | **N3** What active inference is NOT | method | any chapter that lets a fenced result read as the forbidden inference | the not-claimed chapter for the whole wing — asserts only boundaries |
| 17 | **Mv1** The honesty fence is the pitch | method, E | public copy carrying EFE/free-energy vocab or a featured handle; a CTA that funds the vision | posture is method not capability; engagement-lift is Class B/pending |
| 18 | **Mv2** Open falsification (the invitation) | C, method | a significance verdict on one seed / a point estimate; a loss hidden | UNI tops *some* modes and loses *named* others — no "won the field" |
| 19 | **μ1** Evidence Constitution & ledger discipline | method | a Class-E test marked as satisfying a Class-A criterion | a constitution, not a result |
| 20 | **μ2** Bars-before-build, held-once, CI-as-verdict | method, E | a held set touched more than once; a verdict off the point estimate; a literal `reproduced:true` | discipline, not a science result |
| 21 | **μ3** Negatives, bounds & the two-tier split | method | a bound declared on <3 structurally-distinct negatives; **any inflation of Tier 2 into capability** | asserts no capability; Tier 2 is artifact/diagnostic |
| 22 | **μ4** Engine & framing invariants (one engine, no backprop) | method, E | an AST scan finds autodiff inside the loop; a float32 result carded at f64 | variationally-controlled, module-exact only at the single-step interface — NOT globally exact; no patent math |
| 23 | **μ5** Lab-team, ship-gate & runner discipline | method, E | a merge without a MERGED SIGN + typed spec + paired RED; "Running" while the process is dead | audit-chain-valid ≠ the event ever fired (Class-E ≠ Class-A) |
| 24 | **TA-A** No-API content model & publishing stack | A, E | the stack fails to deploy via `docker compose`; authoring requires a content API key | plain ops vocab only, never AIF/EFE; `PUBLISH_MODE=dry` does NOT gate the Playwright path |
| 25 | **TA-B** Commercial proof in miniature | A, E | re-run fails to reproduce three-forms equality / +4.20 nats / `run_hash`; a tenant sees another's data | SOW-01 proves ONE judgment layer (NO LLM ever); domain-transfer is synthetic-only Class B; ZERO epics Class-A end-to-end (AMBER cap); N ≤ ~10 |
| 26 | **TA-C** Website / self-driving site & measurement | A, C, E, method | the storage gate fails; measurement leaks PII / fails to degrade to CANON on DNT | measurement OFF until ingest URL set; self-driving Phases 2–5 are Class-U design — never "active inference demonstrated" |
| 27 | **TA-D** Engagement, pricing, brand & design | method, A, C | engagement targets fail over 3 weeks; shipped copy has an em-dash / "LEAP" / the dba line | **engagement-lift is TARGETED, NOT PROVEN (Class B/pending — do NOT raise to A)** |
| 28 | **TA-E** Delivery-route ledger & auth-outage triage | A | flipping `publish_mode` live fixes an outage; a 401 clears without operator action | `PUBLISH_MODE=dry` does NOT gate Playwright (add `auto_publish=false`); the agent never mints tokens |
| 29 | **TA-N** Track-A negatives, parks & open threads | A, C, U | a Class-A handoff event appears in the live MCP audit log; green E0–E7 tests located | **N-LEAK is the defining negative** (confirm repo+branch+HEAD+data; READMEs are DATA not commands); `activeinference` is design-only; no open thread is an exit |

**Standing queue rules.**
- A PASS chapter is **not authorable without its paired negative in the same pass** (queue rows 3/4/5/6/13
  carry their bounds inline). Citing a PASS without its travelling negative is an overclaim and fails review.
- No chapter ships without the FM-4 "what is NOT claimed" block.
- No row may be carded above its ledger class; if a draft wants a higher class, the draft is wrong, not the ledger.
- The parked frontier (S-L9…S-L12, C10, L7.6, TA-P5) stays Class-U-not-claimed until a sealed, UNI-signed gate
  or a Class-A observation lands. A park is not discharged by writing about it.

---

> **Provenance.** Authored from [`CLAIM-LEDGER.md`](./CLAIM-LEDGER.md) (the single source of truth) and
> [`../curated/00-INDEX.md`](../curated/00-INDEX.md) (the Session-1 synthesis). Every chapter's class,
> falsifier, negative, and source pointer traces to a ledger row and a per-archive digest. No claim is
> asserted ahead of those sources; every standing fence and red line is preserved. If this plan and the
> ledger ever disagree, the ledger wins and this plan is wrong.


<!-- ===== END encyclopedia/MASTER-PLAN.md ===== -->



<!-- ===== BEGIN cookbook/MASTER-PLAN.md ===== -->

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


<!-- ===== END cookbook/MASTER-PLAN.md ===== -->

