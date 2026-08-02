# CB-02 — The shared pantry (engines and primitives)

**What you are building:** the stocked shelf every later recipe reaches into. Not a new dish: the
single set of engines and primitives, named, fenced, and labeled by real status, so that when L0
calls for "the embodiment ontogeny" or L6 calls for "the count/cache World-C reader," you know
exactly which jar it means, what it actually proves, and what it must never be read to prove.

One engine, many scales. That is the load-bearing fact of this whole book. The recipes do not each
ship their own model; they reuse one discrete-categorical active-inference engine and swap only the
observation/generative model and the world it couples to. The pantry below names the engines the
recipes call by name. Each recipe's **Ingredients** list points back here.

---

## The kitchen rules carried in (the constitution travels with the food)

Two governance patterns from the master plan's kitchen rules (`status: method`, never a capability
claim) define what every pantry engine is and is not:

- **WORLD ⊥ BODY ⊥ MIND (M12).** Two typed Markov blankets. Interoception is hardware signals. The
  mind runs a discrete POMDP loop `perceive → EFE-plan → act → learn` with exact conjugate-Dirichlet
  no-backprop learning, surprisal/VFE carried only at the textbook level `F[q] ≥ −ln p(o|m)`. The
  composed appliance is **variationally-controlled (audited), module-exact only at the single-step
  categorical body→mind interface — NOT globally exact.**
- **One engine, no backprop (M13).** `core.py` exposes the discrete POMDP loop
  (`active_inference_step`, `exact_posterior_discrete`, EFE/policy selection); learning is
  `counts + lr * sufficient_stat` for the A/B/D/E Dirichlet tensors; an AST-guard enforces
  **no autodiff / optax / torch / grad / backward** in the loop, and isolation is a whitelist
  (`world.<attr>`), not a blacklist.

These are `status: method` (Class `method`/E). They are not evidence that active inference is
demonstrated. "Active inference" and "free energy principle" appear here only as the framing **lens**,
at textbook level (Parr, Pezzulo, Friston, *Active Inference*, MIT Press 2022; plus the unrefereed
preprint, Polzin et al. 2026, Zenodo DOI 10.5281/zenodo.19785799, MIT, foundation only). **No AIF loop
exists in the Rust crate**; the live UNI.OS loop is a separate reimplementation, not gate-matched.

**Reading the FENCE label.** Every recipe closes with one of four words, drawn from the ledger and
never inflated:

- **proven** — a held, sealed, UNI-signed PASS exists (Class A/C), falsifier still live.
- **designed** — a typed spec / signed-in-principle design exists; the build is partial or unverified.
- **hypothesized** — a stated mechanism or law with no sealed gate yet (Class U, not claimed).
- **not-yet-built** — no engine, no run, no gate; north-star, hard-fenced.

---

## The shared pantry

| Pantry item | What it supplies | Real status (this pantry) |
|---|---|---|
| **The JAX POMDP + EFE + Dirichlet engine** (`core.py`) | The discrete POMDP loop: `active_inference_step`, `exact_posterior_discrete`, EFE/policy selection; conjugate-Dirichlet learning `counts + lr*sufficient_stat` for A/B/D/E; AST-guard no-backprop. | proven as a method (M13, Class E); **float32 host** — anchors hold to **~6e-8 (~1e-6 single-step filter)**, NOT the `<1e-10` f64 tier. |
| **The Rust-f64 / NumPy deep-reader path** | The genuine `<1e-10` EXACT tier; the cross-language Rust-f64 == Python oracle (M10/M11). | proven (the only path carded at the f64 tier). |
| **The count/cache World-C reader** | A no-backprop **COUNT** reader + multi-level cache; the one citable empirical PASS family (L6.1: +0.081 nats/char, CI [0.0736, 0.0890]). | proven (Class C). **Explicitly NOT active inference.** |
| **The Z affect modulator** | Global `[energy, arousal, valence, fatigue, pain, threat, safety, inflammation]` → sets precision / preferences / habits / learning-rate / horizon (L4.1). | proven functional (Class C). **Affect modeled, never felt.** |
| **The embodiment ontogeny** | `recombine` / `seed_zygote`, conjugate first-division, `test_embodiment_ontogeny` (6/6), Embodiment Rungs (L0.1). | proven (Class A, float32 tier). |
| **The metabolism organ** | Standing-metabolic-drive interoception organ; viability edge; `:pb_seed` strong-Dirichlet seam (L2.1). Additive + genome-gated (default byte-identical). | proven as a foraging/crafting driver (Class C); recorded NEGATIVE as a building driver, G6 OPEN. |
| **The motor hierarchy** | Proprioceptive **diagonal-A** prior (posterior 0.0→0.75), continuous servo + reafference; live RCON craft-chain bridge; motor-ablation collapses harvest ~700× (L5.3). | proven (Class A posterior shift / C live RCON gate / E 277 tests). |
| **The precision labs** (Precision / Echo / Loop / Cell / Heart) | Browser-native one-engine-many-scales demos; three precision knobs (`gamma_a`, `gamma_b`, `softmax_temperature`); 2D bifurcation map; inline-engine + canonical-TS + parity-test triad (L1.1, L3.1, L6.3). | proven (Class C / E with parity tests). |
| **UNI.OS (the embodiment substrate)** | "Lab-in-a-box on metal": body→mind 7-modality categorical sensorium (`[M=7, O_max=4]`), deterministic replay, fail-closed transport, ASK-mode Dirichlet policy-prior, gated control-MCP (C1, C3, C4, C5). | proven as **engineering/substrate evidence, NOT general-AIF evidence.** |

**The exactness fence (M10, load-bearing here).** The JAX core that `core.py` lives in is **float32**.
Its machine-exact anchors hold to ~6e-8, not the `<1e-10` tier. A genome docstring claiming `<1e-10`
was caught as an overclaim and corrected. Only the NumPy / Rust-f64 deep-reader path earns the f64
tier. Any recipe that calls the JAX engine inherits the float32 ceiling; never card a JAX anchor at f64.

**The count-baseline fence (L6.1, L6.6).** World C is the program's one citable empirical PASS, and it
is a **COUNT baseline win — NOT active inference, NOT comprehension, NOT "talking," NOT beats-LLMs.** It
sits ~10–15% behind backprop LLMs on char-perplexity by a chosen design trade. The standing ceiling on
this ingredient cannot be raised; "World C" in any Ingredients list means a count/cache reader and
nothing more. **Engine-attached published bounds (cross-ref):** Phase G (L6.4) — five structurally-distinct
within-segment-structure designs all NEGATIVE-with-discriminator, only the L5 cache (World C) wins; Phase F
(L6.5) — the World-C gain is **diffuse** (nothing to gate). These are first-class ledger negatives on the
reader-as-engine; full treatment lives in the L6 recipe.

**The substrate fence (continuity sub-ladder, §2).** UNI.OS supplies a real body→mind sensorium, a
bit-for-bit process-restart continuity (Stage-1 / C1, Class C engineering), a measured ASK-mode
Dirichlet learning shift, and a single-approval control gate — all live on metal. This is **engineering
/ substrate evidence, orthogonal to L0–L12, NOT general-AIF evidence.** It does not imply any science
gate is met. Stage-2 (the mind surviving a real kernel swap) is **owed, not shown** (C2 NEGATIVE/owed).
And the "embody only what's proven" coupling is the program's central open gap (C10, PARKED, Class U):
UNI.OS has no no-backprop Dirichlet learning, no exact info-gain EFE, heuristic isolation, and a
different dev model than the one that earned the bars. When a recipe lists UNI.OS, it is borrowing a
substrate, never a science result.

**Honest floor (C7, first-class NEGATIVE).** A single-box swap is a **SECONDS-LONG FREEZE, not
zero-downtime** — true zero-freeze needs the second node carrying the platform — and external media legs
(RTP/SIP/kernel-mode rtpengine) are **NOT preserved** across kexec. Two more UNI.OS-attached negatives are
carried here by cross-reference and treated in full in CB-continuity: the **EDAIT trade** (C9) — an
exact-discrete active-inference transformer trades fluency for calibration, held-out perplexity ~33 vs a
backprop GPT's ~25 (an honest trade, not a win); and the **multi-tenancy gap** (C14) — the bare substrate
is missing tenant/namespace isolation and temporal count-decay (the product build is the wrapper, not the
core).

**The affect fence (L4.1).** The Z modulator is `proven functional` — it sets precision and flips the
pragmatic↔epistemic balance, and a Z-ablation collapses the effect. Affect is **modeled, never felt**;
phenomenal feeling and sentience are explicitly disclaimed wherever Z appears.

---

## Gate (what "the pantry is stocked" means)

The pantry has no single empirical gate — it is the shelf, not a dish. Its pass condition is
**fidelity**: every ingredient above is carded at exactly its ledger class and no higher, and every
recipe that lists an ingredient inherits that ingredient's fence. Concretely:

- the JAX engine ships float32 anchors at **~6e-8**, never `<1e-10` (M10/M13);
- World C is cited only as a **+0.081 nats/char count-baseline PASS**, flagship CI **[0.0736, 0.0890]**,
  seeds 0–4 (L6.1), never as active inference or a beats-LLMs result;
- UNI.OS is cited only as **substrate/engineering** evidence (§2), never as a science gate;
- the AST no-backprop guard (M13) holds across every engine that claims it.

**Falsifier.** The pantry fails if any ingredient is carded above its ledger class anywhere in the
book: a float32 JAX anchor printed at the f64 tier; World C described as comprehension, talking, active
inference, or beating LLMs; UNI.OS substrate work read as a met science gate; or the no-backprop guard
shown tripping where an engine claims it holds. Where this pantry and the ledger disagree, the **ledger
wins and this pantry page is wrong.**

**Recorded NEGATIVES (first-class, inline).** Scope contract: **engine-attached** negatives are carried
here (metabolism −14% / G6 OPEN, the 2-modality bottleneck C8, A3 #2, mean-field-rejected, plus the
fenced C7 / C9 / C14 and L6.4 / L6.5 cross-refs above); **per-rung** negatives (L1 honest losses, the L7
central wall + J.attribution_caveat) live in their own recipe chapters by design, not here.

- **The metabolism organ is a foraging/crafting driver, not a building driver.** In the same first 12 h
  live RED that gave +135% / 2.35× tool-crafting and +19% mining (L2.1), **building went WORSE (−14%)**
  and **G4 allostasis never separated** (L2.2). The plateau-break gate **G6 stays OPEN.** A read-only
  counterfactual-EFE audit on real hoarder `.bin` brains diagnosed **epistemic_starvation** — NOT
  γ-runaway (γ≈7.8, unsaturated), NOT a curriculum ceiling (L2.3). Stock the organ for foraging; never
  spin the +135% as "breaks the plateau."
- **The over-compressed sensory bottleneck went NEGATIVE.** A 2-modality `deep_state` bottleneck lost on
  held data versus the full 7-modality contract (C8) — keep all 7 modalities. The same negative recurs
  on the science side as A3 Design #2 (slow Z-bottleneck), held Δ **−0.091, CI [−0.134, −0.055]**, a
  single sealed motor negative (**K-negative = 1**, no Section 0.6(B) bound owed; L5.2).
- **The exact joint posterior is mandatory.** A factored mean-field posterior variant was implemented
  and **rejected as lossy** (the cavity principle, M22). The exact joint is used everywhere; mean-field
  is not a shortcut a recipe may take.

---

## HONEST FENCE — proven (as a method-and-engine shelf), with named designed/parked items.

The pantry as a set of method patterns (M12, M13, M10) and held engines (L0.1 Class A; L1.1, L2.1,
L3.1, L4.1, L5.3, L6.1, L6.3 Class C/E; C1, C3, C4, C5 substrate) is **proven** at its stated classes,
falsifiers live. Folded in as **DESIGNED / not-run** (raising nothing, leaving every rung's status
unchanged): the SIGNED consult designs the later recipes reach for — L2's `build_epistemic_frontier`
organ (G6 stays OPEN), L5's Design #3 Proprioceptive Servo Bridge, L9-G1, L11-R1, the L12 bound, and the
C10 Dirichlet-first port. Each is a typed spec or signed-in-principle design, not a result.

**Not claimed:** this pantry does not demonstrate active inference, does not create life or a synthetic
organism, does not make UNI conscious / aware / self-aware, and does not show UNI is human-level or AGI.
The JAX core is float32 (anchors ~6e-8, not f64); World C is a count baseline (~10–15% behind backprop
LLMs, not active inference, not beats-LLMs); UNI.OS is engineering/substrate evidence, not general-AIF
evidence. The whole program remains a **developmental active-inference SIMULATION** — a bounded peek, a
toy world, never a person. Honest position: **~2 of 11+ developmental rungs earned.**
