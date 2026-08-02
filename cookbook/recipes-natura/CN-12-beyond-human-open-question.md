# CN-12 — Beyond human: the permanent open question (QUAESTIO APERTA)

> **What you are reading.** Not a recipe. This chapter is a **QUAESTIO-APERTA register entry**, and it deliberately does not carry the recipe wing's *"What you are building"* header, because it builds nothing and must never be read as though it did. It designs no successor to the human, names no target, schedules no milestone, and predicts no outcome. It does one job: it maps the **constraint space** any candidate would have to satisfy, and states what would falsify each claim people make about it. Nothing here is claimed. Nothing here is a plan. There is no roadmap in this chapter and there must never be one.

The operator's question — *"the next evolution beyond human"* — is a permanent open question, exactly as **"full human"** is. Standing doctrine is absolute on this and this chapter does not soften it: never a target, never a milestone, never a deliverable. What follows is therefore not an answer. It is a map of the fence and the physics.

---

## 1. Why the question is ill-posed as usually asked

This is the chapter's most useful correction, and it is good science rather than evasion.

**"Beyond human" presumes a scalar ladder with humans on a rung.** Evolution has no such ladder. It has a fitness landscape defined *relative to an environment*, and the landscape moves. There is no axis along which "more evolved" is a measurable quantity, because there is no environment-independent quantity to measure. A tapeworm that lost its gut is not less evolved than its free-living ancestor; it is *differently* adapted, and it has had exactly as long to get there. The intuition that there is a ladder is the **great chain of being** — a pre-Darwinian idea that keeps returning because it is intuitive, not because it survived contact with data.

Gould's argument in *Full House* (1996, Harmony Books) is the sharpest available correction, and it is a statistical one rather than a rhetorical one. Complexity has a **left wall**: life cannot be arbitrarily simpler than the simplest viable self-replicator. Start a random walk hard against a wall and the walk's *maximum* will drift away from the wall over time — not because the walk is directional, but because the wall is the only barrier. The right tail extends; the **mode does not move**. Gould's point is that the mode of life on Earth is, and has always been, bacteria. Reading "progress" off the growth of the right tail is reading a boundary condition as a driving force.

This matters here operationally: **if you cannot state the environment, you cannot state the fitness, and "beyond" has no referent.** Every claim about a successor that does not name the selective environment it is a successor *in* is not a weak claim. It is a claim with no truth conditions.

What *does* exist is a constraint space. That part is measurable, and it is the payload.

## 2. The real measured constraints

### Thermodynamic

**Landauer's principle.** Erasing one bit of information dissipates at least `k_B T ln2` (Landauer 1961, *IBM J Res Dev* 5(3):183–191). Compute it, with `k_B = 1.380649 × 10⁻²³ J/K` (exact, SI 2019):

```
T = 300 K:  k_B T ln2 = 1.380649e-23 × 300 × 0.693147 = 2.87 × 10⁻²¹ J
T = 310 K:  k_B T ln2 = 1.380649e-23 × 310 × 0.693147 = 2.97 × 10⁻²¹ J   (body temperature)
```

This is not a modelling convenience. Bérut et al. (2012), *Nature* 483:187–190, measured it — a single colloidal particle in a modulated double-well potential, with mean dissipated heat **saturating at the Landauer bound in the limit of long erasure cycles**. It is an experimentally-grounded floor.

**How far above the floor does a measured neural circuit run?** *(Asked that way on purpose: the only per-bit costs measured below are from a fly, and nothing here establishes that a fly photoreceptor and a human cortical synapse are interchangeable per bit.)* The honest answer is that *the question has no single number*, and the reason is worth more than a number would be.

Accounting A — the whole-budget ceiling. The brain draws **~20 W**. At body temperature:

```
20 W / 2.97e-21 J = 6.7 × 10²¹ irreversible bit-erasures per second
```

That is the *ceiling* 20 W could buy if the brain were a perfect Landauer-limited erasure machine. It is not one.

Accounting B — measured cost per bit. Laughlin, de Ruyter van Steveninck & Anderson (1998), *Nat Neurosci* 1(1):36–41, measured the ATP cost of transmitting known amounts of information in **blowfly retina**: **~10⁴ ATP per bit at a chemical synapse**, and **10⁶–10⁷ ATP per bit** for graded signals in a photoreceptor or interneuron, or for spike coding.

Turning ATP into joules needs a free energy, and that number carries conditions this chapter must declare rather than borrow silently. NA-08's `ΔG_ATP` row gives **−47 to −50 kJ/mol in vivo**, anchored on *E. coli* on glucose (−47), and states no `[ATP]/[ADP][Pi]`, pH, or free-Mg²⁺ conditions — in-vivo ΔG depends on all of them, so it is a **range under unstated conditions, not a constant**. Three declarations, all **assumptions rather than measurements**, and all made explicit here because an undeclared condition is the exact defect this section prosecutes:

1. The ~50 kJ/mol below is the **endpoint** of NA-08's range. At −47 the ratios move by 0.03 orders.
2. The per-bit cost is a **fly retina** value; the ΔG anchor is a **bacterium**. They are multiplied together below as though both generalised to mammalian neural signalling. *(Falsifier: a mammalian ATP/bit measurement >10× off the fly value.)*
3. The ratios divide by the **300 K** bound, where Accounting A used the 310 K one. At 310 K they move by a further 0.01 orders.

None of these moves the result against a spread of 3 orders — which is the point of stating them rather than the reason to omit them. Taking the ~50 kJ/mol endpoint, one ATP ≈ `50,000 / 6.022e23 = 8.3 × 10⁻²⁰ J`:

```
10⁴ ATP/bit  →  8.3e-16 J/bit  /  2.87e-21  =  2.9 × 10⁵   ≈ 5.5 orders of magnitude above Landauer
10⁶ ATP/bit  →  8.3e-14 J/bit                =  2.9 × 10⁷   ≈ 7.5 orders
10⁷ ATP/bit  →  8.3e-13 J/bit                =  2.9 × 10⁸   ≈ 8.5 orders
```

Laughlin et al. state the conclusion in their own terms: energy consumption is several orders of magnitude greater than the thermodynamic minimum. The arithmetic above is consistent with that.

**The spread is the finding — and it has to be attributed to what actually causes it.** Accounting A is the Landauer bound *itself*: a perfect Landauer-limited machine sits **0 orders above it by construction**, so A is a ceiling, not a measurement of any brain. Accounting B alone ranges over **~3 orders (5.5–8.5)**, and that spread is *internal to one 1998 paper* — driven by which signalling mode you count as the bit operation: a chemical synapse (~10⁴ ATP/bit) or graded/spike coding (10⁶–10⁷). The full A-to-B spread is therefore **~5.5–8.5 orders**, not 3. Either way the load-bearing decision — *what counts as one bit operation in a brain* — is **NOT-MEASURED**. Anyone quoting a single "the brain is N orders above Landauer" figure without declaring their bit-accounting is quoting a choice as if it were a measurement.

**Bremermann's limit.** `c²/h` bounds information processing per unit mass (Bremermann 1962, in *Self-Organizing Systems*):

```
c²/h = 8.98755179e16 / 6.62607015e-34 = 1.36 × 10⁵⁰ bits·s⁻¹·kg⁻¹
```

For a **~1.4 kg** brain *(standard reference figure, not primary-sourced in this pass)* that is ~1.9 × 10⁵⁰ bits/s. How far away that is **is not a single number either, and for exactly the reason just given** — it depends on the bit-accounting, so the accounting gets declared here rather than a bare figure quoted:

```
vs Accounting A  (6.7e21 bit-erasures/s)  →  1.9e50 / 6.7e21 = 2.8e28   ≈ 28 orders
vs Accounting B  (10⁴ ATP/bit: 2.4e16 b/s) →  1.9e50 / 2.4e16 = 7.9e33   ≈ 34 orders
vs Accounting B  (10⁷ ATP/bit: 2.4e13 b/s) →  1.9e50 / 2.4e13 = 7.9e36   ≈ 37 orders
```

So: **~28 to ~37 orders of magnitude**, depending on the accounting. **It is a real limit and it binds nothing.** Naming it here is the point: a limit ~28–37 orders distant is not a constraint on design, and citing it as though it were is a rhetorical move, not an engineering one.

**The ceiling that actually binds is heat.** Erasure costs energy; energy becomes heat; heat leaves through a **surface** growing as `R²` while the computing **volume** grows as `R³`. This is NA-08's surface-to-volume argument (`S/V = 3/R`) at a different scale, and it is why density — not the Landauer floor and certainly not Bremermann's — is the operative ceiling.

### Physical: signal speed versus size

This is the most concrete constraint in the chapter, and it is the one that answers *"why not just make it bigger?"* with arithmetic.

Conduction delay is `τ = L/v`. Brain path length `L` scales with radius `R`. So **doubling brain radius doubles every conduction delay at fixed velocity.** Unconditional; no constant required.

The only escape is raising `v`. Conduction velocity in myelinated axons rises **linearly with axon diameter** — replicated since Hursh (1939), *Am J Physiol* 127(1):131–139, and Gasser & Grundfest (1939). Now watch the geometry close:

- Hold delay `τ` fixed while `R` grows ⇒ need `v ∝ R` ⇒ need diameter `d ∝ R`.
- One long-range axon's volume ∝ length × `d²` ∝ `R × R² = R³`.
- Neuron count to be connected ∝ brain volume ∝ `R³`.
- Total long-range wiring volume ∝ `R³ × R³ = R⁶` — inside a skull that only grows as `R³`.

**At double the radius you need eight times more wiring volume than you have brain.** Holding cross-brain delay constant while scaling up is not expensive; it is geometrically impossible.

So biology did not do it. Two independent measurements show what it did instead:

1. **It pays partially.** Zhang & Sejnowski (2000), *PNAS* 97:5621–5626, measured white matter growing disproportionately faster than grey across several orders of magnitude of mammalian brain size — a power law with exponent **4/3** (minus a small cortical-thickness correction). White matter *does* outgrow grey. Just nowhere near `R⁶`.
2. **It buys a thin fast subset and lets the bulk go slow.** Phillips et al. (2015), *Proc R Soc B* 282:20151535 (correction: 282:20152620), used electron microscopy on the corpus callosum of **14 anthropoid primate species spanning a 97-fold range of brain mass** — and found the fastest cross-brain conduction times, carried by 95th-percentile axons, varied only between **3 and 9 ms**. The **majority of callosal axons are under 1 µm** in every species — and the same paper measures what that costs the bulk: for **median** axon diameters, cross-brain conduction times varied substantially more, between **11 and 38 ms**. That measured 11–38 ms — not the order-of-magnitude 0.1 m path estimate below — is the load-bearing delay figure in this chapter. Most interhemispheric traffic is slow *and stays slow* regardless of brain size, and Phillips et al. report that for *both* size classes, increased diameter does not entirely compensate for the delay that comes with a larger brain.

Read the delay ladder against Purves et al. (2001), *Neuroscience*, 2nd ed., Sinauer — myelinated axons conduct **up to 150 m/s**, unmyelinated **0.5–10 m/s**. For an order-of-magnitude cross-brain path `L ≈ 0.1 m` *(estimate, NOT-SOURCED as a measurement)*:

| `v` (m/s) | `τ = L/v` | note |
|---|---|---|
| 150 (fastest myelinated) | 0.67 ms | the expensive minority |
| 10 (fast unmyelinated) | 10 ms | Phillips' measured 3–9 ms (95th-percentile axons) sits just **below** this; their **median**-axon 11–38 ms straddles and exceeds it |
| 0.5 (slow unmyelinated) | 200 ms | longer than the perceptual events it must bind |

The `R⁶` model predicts its own escape hatch: shrink the fraction of neurons that must reach across, i.e. **modularise**. That is precisely the conjecture of Ringo, Doty, Demeter & Simard (1994), *Cereb Cortex* 4(4):331–343 — that hemispheric specialisation *arises from* interhemispheric conduction delay, brains clustering time-critical work locally because the wires cannot be made fast enough. **The model is falsifiable exactly here:** a large-brained lineage with low functional lateralisation and no compensating architecture would move it.

### Informational

Shannon (1948), *Bell Syst Tech J* 27:379–423, 623–656, bounds what any channel can carry. Applying it to a person is where the care is needed.

The widely-repeated **"~40–60 bits/s"** conscious-throughput figure is **estimate-laden and must be fenced, not repeated as fact.** Its lineage runs through Zimmermann's sensory-physiology estimate and Nørretranders' *The User Illusion* (1991), and the quoted value drifts across sources — 16, 20, 40, 60 bits/s appear in different retellings of the same underlying estimate. A number whose value depends on who is retelling it is not a measurement.

The current serious treatment is Zheng & Meister (2025), *Neuron* 113(2):(Perspective) — sensory systems gather **~10⁹ bits/s**; human behavioural throughput is **~10 bits/s**. And it is **already formally contested**: Sauerbrei & Pruszynski (2025), *Nat Neurosci*, "The brain works at more than 10 bits per second," accept a ceiling on high-level cognition but argue that unconscious real-time motor control — occupying most of the CNS — substantially exceeds it. **Carry the dispute, do not average it.** The contest is not noise; it is the observation that "throughput" is not a single well-defined quantity for a brain.

### Developmental / evolutionary

You cannot get there from here by fiat. **Phylogenetic constraint** means the reachable set is a neighbourhood of what already exists — development is a dependency graph, and most edits to an early node are lethal, which is why early development is the most conserved part of the process (NA-09). **Mutation–selection balance** bounds how fast a lineage can move against drift. And in small populations **drift dominates selection**, so the very populations easiest to engineer are the ones whose trajectories are least controllable. None of this makes change impossible. It makes *directed* change slow and its direction weakly held.

### Metabolic — and an honest disconfirmation

The **expensive-tissue hypothesis** (Aiello & Wheeler 1995, *Current Anthropology* 36(2):199–221) proposed that the metabolic cost of a large brain is offset by a reduced gut — humans' smaller relative gut size almost exactly compensating the larger brain's cost at an unremarkable basal metabolic rate. It is elegant, it is widely repeated, and **the comparative test largely did not support it.**

Navarrete, van Schaik & Isler (2011), *Nature* 480:91–93, tested it across **100 mammalian species including 23 primates**: controlling for fat-free body mass, brain size was **not** negatively correlated with digestive-tract mass — or with the mass of any other expensive organ. They report instead a negative correlation between brain size and **adipose depots**, reading encephalisation and fat storage as compensatory strategies against starvation.

The honest status is **OBSERVED-CONTESTED**, not "refuted": Liao et al. (2016), *Am Nat* 188(6):693–700, found the predicted negative brain-mass/gut-length correlation **within 30 anuran species**. So the hypothesis fails across mammals and holds within frogs.

**This is exactly the wing's method working, and it is worth saying plainly.** A beautiful, intuitive, famous hypothesis met a comparative test and lost its generality. Recording that is not a footnote — it is the reason anything else here is worth reading.

## 3. The gradients that are real

These vary continuously and are measurable. **None of them measures "advancement."** That is not a hedge; it is the finding.

**Neuron count.** Azevedo et al. (2009), *J Comp Neurol* 513(5):532–541, by isotropic fractionator: the human brain averages **86 billion neurons** and ~85 billion non-neuronal cells, with **~16 billion in the cerebral cortex**.

Then the gradient breaks, twice, in the same year:

- **The African elephant** (Herculano-Houzel et al. 2014, *Front Neuroanat* 8:46) has **257 billion neurons** — three times the human total — but **97.5% of them (251 billion) sit in the cerebellum**. Its cerebral cortex has twice the mass of ours and holds only **5.6 billion** neurons, about a third of the human count. So *total* neuron count is decisively not the variable.
- **The long-finned pilot whale** (Mortensen et al. 2014, *Front Neuroanat* 8:132) has **~37.2 × 10⁹ neocortical neurons** — roughly **twice** the human figure. The authors' stated conclusion is the opposite of Herculano-Houzel's: that absolute neocortical neuron number is *not* what correlates with human cognitive abilities, at least against cetaceans.

Two 2014 papers, same journal, directly opposed conclusions from compatible counts. **OBSERVED-CONTESTED, and printed as such.** The gradient is real and measured; what it *means* is not settled, and this chapter does not settle it.

**Encephalization quotient (EQ).** Brain mass divided by the mass predicted for that body mass from a fitted allometry (Jerison 1973). Its limits are structural: the fitted exponent and coefficient are **choices**, so EQ is not well-defined until you declare them. *(Specific constants NOT-SOURCED in this pass.)* And the metric loses its own contest: Deaner, Isler, Burkart & van Schaik (2007), *Brain Behav Evol* 70(2):115–124, meta-analysed cognitive performance across primates and found **absolute brain size the best predictor**, while EQ and other body-size-corrected residuals were **not strongly correlated** with it. They also found no advantage for neocortex-based measures over whole-brain ones.

**Other real gradients:** cortical neuron density (higher in primate than rodent cortices of comparable size, a consequence of divergent scaling rules — Herculano-Houzel 2011); lifespan; generation time; and *the degree to which a system carries a generative model of its environment* — which is the gradient this repo's method actually cares about and which is **NOT-MEASURED** as a scalar for any organism, including the human one.

## 4. What would have to be true

For each popular claim: one observation that would support, one that would refute. Where a claim admits neither, it is marked INADMISSIBLE-as-stated with the reason. **Several of these are serious positions held by serious people. The point is not to rule. It is to demand a falsifier.**

| Claim | Would support | Would refute | Status |
|---|---|---|---|
| **Mind uploading / whole-brain emulation** (Sandberg & Bostrom 2008, FHI Tech. Rep. 2008-3) | A simulation built from a fixed structural scan alone that reproduces an animal's behavioural repertoire without further tuning. The substrate now exists to try: FlyWire's complete adult *Drosophila* connectome — **139,255 proofread neurons, >50 million synapses** (Dorkenwald et al. 2024, *Nature*) | Exhibit one functionally load-bearing variable not recoverable from any fixed structural scan — a graded state that changes behaviour and is not inferable from connectivity plus molecular identity | **HYPOTHESIZED** — falsifiable in principle, unsettled. The roadmap's scale-separation assumption is the load-bearing one |
| **Substrate independence** — *as functional organisation* | A brain function realised on a materially different substrate at matched input/output | Exhibit a brain function provably unrealisable on any other substrate at any speed | **HYPOTHESIZED** — falsifiable |
| **Substrate independence** — *as experience* ("the upload is conscious") | — | — | **INADMISSIBLE-as-stated.** No observation is specified that distinguishes a system that has experience from one behaving identically without it. This is a fence on the claim's *form*, not a verdict on its truth, and not a slight to those who hold it. Give it a falsifier and it moves |
| **Intelligence explosion** (Good 1965) | A sustained superlinear return: rate of improvement on a pre-registered held-out metric rising as a function of the system's own prior improvements, over multiple cycles, no exogenous input | Measured diminishing returns per cycle — each self-improvement yielding less than the last on the pre-registered metric | **HYPOTHESIZED / NOT-MEASURED.** Falsifiable if and only if the metric is pre-registered and held out. Without that it is unfalsifiable in practice |
| **Engineered speciation** | Already partly observed — in **two experiments of different lengths, which must not be merged into one figure**: Rice & Salt selected *D. melanogaster* on habitat preference in a complex maze with mating local to the selected habitat, reporting pre-zygotic isolation after **25 generations** (Rice & Salt 1988, *Am Nat* 131:911–917 — *count secondary-sourced in this pass; primary paywalled*); and a **35-generation** maze experiment in which complete reproductive isolation evolved as a *correlated character* under sympatric conditions (Rice & Salt 1990, *Evolution* 44:1140–1152 — *count stated in the paper's own abstract*; reviewed Rice & Hostert 1993, *Evolution* 47:1637–1653) | Replicated failure of reproductive isolation to evolve under equivalent disruptive selection | **OBSERVED** — and the only entry here that is not speculative, which is exactly why its generation counts are scoped per-experiment rather than summed or averaged. Note precisely: **speciation is population divergence, not life from non-life.** Nothing in this row touches "created life," and the two must not be conflated |

## 5. The register: quaestiones apertae carried whole

Two open questions are carried in UNI's **QUAESTIONES APERTAE** register — a store deliberately outside the Tree. They are recorded here **verbatim, with the attribution each source gives them, and are not answered, not endorsed, and not derided.**

As they stand in the register (`uni-onchip/design/11-VALIDATIO-RECEIPT.md:21`), in the Latin canon:

> `anima in silicio? - attributum (Harish)`
> `silicium ut aqua? - quaestio aperta`
> status: `NONDUM FALSIFICABILIS` — pinned `extra Arborem - fossa seiunctionis` — `leguntur, non aguntur - nullam rotam movent`

As the operator's own phrasing is recorded in the session memory of the 2026-07-04 doctrine drop:

> *"if a soul is energy, could silicon hold one; is silicon water-like in abundance with no known barrier to life moving between organic types"* — attributed to **Michael**; the record notes his phrasing is **explicitly hypothetical**, and that **no falsifier has been offered, so it cannot enter the Tree.**

**Two honest notes on provenance, and no more.** First, the attributions differ between the two records and are **not merged here**: the register tags the `anima in silicio?` line `attributum (Harish)`, while the English phrasing above is attributed to Michael. SIGNUM SIGNUM MANET — each string keeps the attribution its own source gives it. Second, the brief that commissioned this chapter cited a doctrine row **"D3-08"**; no such row was located. The rows actually governing this register and located on disk are `10-DOCTRINA-V2.md:461` (**SAEPES ASSERTIONIS** — "register entries are never asserted and never mocked … quote-with-attribution only, exact words preserved"), `10-DOCTRINA-V2.md:267` (attributed teachings held sovereign), `12-FALSIFIERS-V2.md:15` (**VOLUMEN-MOVENS** — any register line found wired to any gear, pointer, or computation is a register breach), and `D6-R7`. **"D3-08" is recorded NOT-LOCATED** rather than assumed; falsifier below.

**No falsifier has yet been offered for either question. That is precisely why they sit in a register and not in a ledger** — and it is why this chapter leaves them exactly where they are. They are read, not acted on. They move no wheel.

---

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `E_L(300)` | 2.87 × 10⁻²¹ | J per bit erased | `k_B T ln2`, T = 300 K | MODELED (computed) | Landauer 1961, *IBM J Res Dev* 5(3):183–191; `k_B` exact per SI 2019 | Arithmetic error |
| `E_L(310)` | 2.97 × 10⁻²¹ | J per bit erased | `k_B T ln2`, T = 310 K (body) | MODELED (computed) | as above | Arithmetic error |
| `E_L` **measured** | saturates at `k_B T ln2` | J | single colloidal particle, modulated double-well, long erasure cycles | OBSERVED-REPLICATED | Bérut et al. 2012, *Nature* 483:187–190 | An erasure cycle dissipating reproducibly below the bound |
| `P_brain` | ~20 | W | human brain, ~2% body mass, ~20% of resting metabolism | OBSERVED-REPLICATED *(not primary-sourced in this pass)* | standard cerebral-metabolism references (Clarke & Sokoloff, *Basic Neurochemistry*) | Fetch a primary calorimetric/CMR source; a value outside ~15–25 W |
| `N_L,brain` | 6.7 × 10²¹ | bit-erasures/s | ceiling: 20 W ÷ `k_B T ln2` at 310 K | MODELED | Computed here | Arithmetic error, or `P_brain` refuted |
| `E_bit,syn` | ~10⁴ | ATP per bit | chemical synapse, blowfly retina | OBSERVED-REPLICATED | Laughlin, de Ruyter van Steveninck & Anderson 1998, *Nat Neurosci* 1(1):36–41 | Independent measurement >10× off under stated conditions |
| `E_bit,graded` | 10⁶–10⁷ | ATP per bit | graded signals in photoreceptor/interneuron, or spike coding | OBSERVED-REPLICATED | as above | As above |
| `r_Landauer` | ~10⁵·⁵ – 10⁸·⁵ | dimensionless | **blowfly retina** signalling (Laughlin et al. 1998) ÷ Landauer floor at 300 K; ATP at ~50 kJ/mol — the endpoint of NA-08's −47 to −50 range, which is *E. coli*-anchored and states no `[ATP]/[ADP][Pi]`, pH or Mg²⁺ conditions. **Assumes fly per-bit cost and bacterial ΔG generalise to mammalian neural signalling: an assumption, not a measurement** | MODELED | Computed here from Laughlin et al. 1998 + NA-08 `ΔG_ATP` | Arithmetic error; a different ATP free energy; **or a mammalian ATP/bit measurement >10× off the fly value** |
| **"orders above Landauer"** as a single figure | — | — | depends entirely on what counts as one bit operation in a brain | **NOT-MEASURED** | — | Define and measure a brain's irreversible-operation count |
| `c²/h` | 1.36 × 10⁵⁰ | bits·s⁻¹·kg⁻¹ | Bremermann's limit | MODELED (computed) | Bremermann 1962, *Self-Organizing Systems*; `c`, `h` exact per SI 2019 | Arithmetic error |
| `m_brain` | ~1.4 | kg | adult human brain mass, as used for the Bremermann figure | OBSERVED-REPLICATED *(standard reference; **not primary-sourced in this pass**)* | standard anatomical references | Fetch a primary source; a value outside ~1.2–1.5 kg |
| `d_Bremermann` | **~28 to ~37** | orders of magnitude | distance from `c²/h × 1.4 kg` down to a brain — **~28** vs Accounting A's ceiling, **~34–37** vs Accounting B's measured per-bit costs | MODELED (computed) | Computed here | Arithmetic error; or a **declared** accounting landing outside ~28–37 |
| **"orders below Bremermann"** as a single figure | — | — | like `r_Landauer`, it is fixed only once a bit-accounting is chosen | **NOT-MEASURED** | — | Declare an accounting. Any bare figure (a "~39" follows from an undeclared ~10¹¹ bits/s) is a choice, not a measurement |
| `v_myel` | up to 150 | m/s | myelinated axons | OBSERVED-REPLICATED | Purves et al. 2001, *Neuroscience* 2nd ed., Sinauer | Measurement outside stated range |
| `v_unmyel` | 0.5–10 | m/s | unmyelinated axons | OBSERVED-REPLICATED | as above | As above |
| `v ∝ d` | linear | — | conduction velocity vs outer diameter, myelinated | OBSERVED-REPLICATED | Hursh 1939, *Am J Physiol* 127(1):131–139; Gasser & Grundfest 1939 | A myelinated preparation with non-linear `v(d)` |
| `v ∝ d` **constant** | — | m·s⁻¹·µm⁻¹ | the proportionality constant | **NOT-SOURCED in this pass** | not confirmed here | Fetch Hursh 1939 and read the fitted slope |
| `τ_callosal` | **3–9** | ms | fastest cross-brain time, 95th-percentile axons, 14 anthropoid primates over a **97-fold** brain-mass range | OBSERVED-REPLICATED | Phillips et al. 2015, *Proc R Soc B* 282:20151535 (corr. 282:20152620) | An anthropoid with 95th-percentile cross-brain time outside 3–9 ms |
| `τ_callosal,median` | **11–38** | ms | cross-brain conduction time for **median** axon diameters, same 14 anthropoid primates — *the bulk of interhemispheric traffic* | OBSERVED-REPLICATED | Phillips et al. 2015, *Proc R Soc B* 282:20151535 (corr. 282:20152620) | An anthropoid with median cross-brain time outside 11–38 ms |
| `d_callosal` | majority < 1 | µm | callosal myelinated axons, all 14 species | OBSERVED-REPLICATED | Phillips et al. 2015 | A species with majority > 1 µm |
| `W ∝ G^(4/3)` | 4/3 (less a small cortical-thickness correction) | dimensionless exponent | white vs grey matter, mammals, several orders of magnitude | OBSERVED-REPLICATED | Zhang & Sejnowski 2000, *PNAS* 97:5621–5626 | A mammalian dataset fitting a materially different exponent |
| `V_wire ∝ R⁶` | 6 | dimensionless exponent | **crude model**: wiring volume to hold `τ` fixed as `R` grows; assumes fixed fraction of long-range neurons, linear `v(d)`, spherical brain | **MODELED** | Computed here; cf. Zhang & Sejnowski's more careful 4/3 derivation | The assumptions — chiefly *fixed fraction of long-range neurons*, which modular brains violate by design |
| `L_crossbrain` | ~0.1 | m | human cross-brain path, order-of-magnitude | **NOT-SOURCED** | estimate only | Measure a callosal path length |
| `N_neur,human` | 86 × 10⁹ (cortex ~16 × 10⁹) | neurons | human brain, isotropic fractionator | OBSERVED-REPLICATED | Azevedo et al. 2009, *J Comp Neurol* 513(5):532–541 | Independent count >2× off |
| `N_neur,elephant` | 257 × 10⁹ total; **251 × 10⁹ (97.5%) in cerebellum**; cortex **5.6 × 10⁹** | neurons | African elephant | OBSERVED-REPLICATED | Herculano-Houzel et al. 2014, *Front Neuroanat* 8:46 | Independent count >2× off |
| `N_neocort,pilot whale` | ~37.2 × 10⁹ | neocortical neurons | long-finned pilot whale — **~2× the human figure** | OBSERVED-REPLICATED | Mortensen et al. 2014, *Front Neuroanat* 8:132 | Independent count >2× off |
| **neuron count ⇒ cognition** | — | — | Herculano-Houzel 2014 and Mortensen 2014 draw **opposite** conclusions from compatible counts | **OBSERVED-CONTESTED** | Herculano-Houzel et al. 2014; Mortensen et al. 2014 | A measure resolving both under one framework. Do not average |
| **EQ as predictor** | not strongly correlated with cognitive performance; **absolute brain size** predicts best; no neocortex advantage | — | meta-analysis across non-human primates | OBSERVED-REPLICATED | Deaner, Isler, Burkart & van Schaik 2007, *Brain Behav Evol* 70(2):115–124 | An independent primate meta-analysis where EQ outperforms absolute size |
| EQ constants | — | — | fitted exponent + coefficient are **choices**; EQ undefined until declared | **NOT-SOURCED in this pass** | Jerison 1973 not fetched | Fetch Jerison 1973 and read the fitted allometry |
| `B_sensory` | ~10⁹ | bits/s | human sensory data-gathering | MODELED | Zheng & Meister 2025, *Neuron* 113(2) | Recompute from receptor counts and rates |
| `B_behaviour` | ~10 | bits/s | human behavioural throughput — a **literature synthesis, not a new experiment**: same paper and same method as `B_sensory`, and classed the same way | **MODELED-CONTESTED** | Zheng & Meister 2025, *Neuron* 113(2) **(Perspective)**; **contested** by Sauerbrei & Pruszynski 2025, *Nat Neurosci* ("The brain works at more than 10 bits per second") — unconscious motor control substantially exceeds it | Carry both. A measure reconciling cognitive throughput and motor control under one accounting |
| "40–60 bits/s" conscious bandwidth | **do not quote as fact** | bits/s | value drifts 16/20/40/60 across retellings of one estimate | **INADMISSIBLE as a measurement** (admissible as an *estimate*, attributed) | Zimmermann via Nørretranders 1991, *The User Illusion* | Locate the primary experiment and its stated CI |
| **expensive-tissue hypothesis** | brain size **not** negatively correlated with gut (or any expensive organ) across **100 mammals / 23 primates**, controlling fat-free body mass; brain **is** negatively correlated with adipose depots | — | mammals | **OBSERVED-CONTESTED** | Aiello & Wheeler 1995, *Curr Anthropol* 36(2):199–221 (proposed); **Navarrete, van Schaik & Isler 2011, *Nature* 480:91–93 (disconfirmed in mammals)**; Liao et al. 2016, *Am Nat* 188(6):693–700 (**supported within 30 anurans**) | Resolve the taxon split. Do not cite Aiello & Wheeler without Navarrete et al. |
| `n_gen,Rice&Salt 1988` | **25** | generations | *D. melanogaster*, disruptive selection on habitat preference → pre-zygotic isolation | OBSERVED-SINGLE *(count **secondary-sourced in this pass** — primary paywalled)* | Rice & Salt 1988, *Am Nat* 131:911–917 (DOI 10.1086/284831); count per TalkOrigins speciation FAQ and Wikipedia "Laboratory experiments of speciation", which agree | Fetch Rice & Salt 1988 and read the stated count; a primary count ≠ 25 |
| `n_gen,Rice&Salt 1990` | **35** | generations | *D. melanogaster*, complex habitat maze, sympatric; complete reproductive isolation as a **correlated character** | OBSERVED-REPLICATED | Rice & Salt 1990, *Evolution* 44:1140–1152 — **the paper's own abstract** states a 35-generation experiment (PMID 28563894) | Replicated failure under equivalent selection; a primary count ≠ 35 |
| `n_gen,Rice&Salt` **as one merged figure** | — | — | the 1988 and 1990 experiments ran different lengths under different designs | **INADMISSIBLE — do not merge** | — | Any single generation count offered for "the Rice & Salt experiment" without naming which of 1988 / 1990 it belongs to |
| `N_FlyWire` | 139,255 neurons; >50 × 10⁶ synapses | — | complete adult *Drosophila* connectome, proofread | OBSERVED-REPLICATED | Dorkenwald et al. 2024, *Nature* | Independent reconstruction differing materially |
| **"more evolved"** | — | — | no environment-independent scalar exists | **INADMISSIBLE** | Gould 1996, *Full House* | Specify an environment-independent measurable. None is known |
| **degree of internal generative model** | — | — | as a scalar, for any organism | **NOT-MEASURED** | — | Define it operationally and measure it on two species |
| doctrine row **"D3-08"** | — | — | cited in this chapter's commissioning brief | **NOT-LOCATED** | grep of `uni-onchip/design/` found no such row | Produce the row, or correct the citation to the located rows (`10-DOCTRINA-V2.md:461`, `:267`; `12-FALSIFIERS-V2.md:15`; `D6-R7`) |
| `anima in silicio?` / `silicium ut aqua?` | — | — | QUAESTIONES APERTAE register, `extra Arborem` | **NONDUM FALSIFICABILIS** (register status; carried, not classed) | `uni-onchip/design/11-VALIDATIO-RECEIPT.md:21` | **None offered.** That is why they are in a register and not a ledger |

## Falsifier (operable)

This chapter's central structural claim is: **there is no measurable scalar along which "beyond human" is defined, and the constraints that actually bind any candidate are thermodynamic (heat, not the Landauer floor), geometric (wiring volume against delay), and developmental — not a shortage of will or ambition.**

It is refuted by **exhibiting an environment-independent, measurable quantity `Q` such that (a) `Q` is computable from observation of an organism alone without reference to a selective environment, (b) `Q` orders known organisms in a way that survives the elephant/pilot-whale counterexamples in the table above, and (c) `Q` is not a redescription of "similarity to humans."** Clause (c) is the load-bearing one: every candidate scalar proposed so far fails it, which is the chapter's actual finding.

The `R⁶` wiring model is separately falsifiable and **weaker than the rest**: it assumes a fixed fraction of long-range neurons. A brain that modularises violates that assumption *on purpose* — which is why the model predicts modularity rather than predicting impossibility. Refute it by exhibiting a large-brained lineage with low functional lateralisation, delays that did not grow with size, and no compensating architecture.

Row-local falsifiers are in the table. A refuted row moves that row only. A refuted "no scalar exists" moves the chapter.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **"More evolved" / "higher on the evolutionary ladder" / "beyond human" as a scalar.** — **INADMISSIBLE.** No environment-independent measurable is specified. Evolution is a fitness landscape relative to an environment, not a ladder. Recorded with the receipt (Gould 1996, *Full House*: the mode does not move; the right tail extends because there is a left wall). This is the chapter's reason for existing.
- **NEGATIVE — the expensive-tissue hypothesis in mammals.** Aiello & Wheeler (1995) is elegant, famous, and **did not survive the comparative test**: Navarrete et al. (2011), *Nature* 480:91–93, across 100 mammals, found no negative correlation between brain size and gut (or any expensive organ) once fat-free body mass was controlled. Recorded as a first-class negative, not a footnote. It survives *within anurans* (Liao et al. 2016), so the honest status is CONTESTED-by-taxon, not "wrong". **This entry is the wing's method working, published against a hypothesis the wing would have liked to be true.**
- **NEGATIVE — total neuron count as a proxy for anything.** The African elephant has 3× the human neuron total and puts 97.5% of it in the cerebellum (Herculano-Houzel et al. 2014). The long-finned pilot whale has ~2× the human *neocortical* count (Mortensen et al. 2014). Two 2014 papers in the same journal reach opposite conclusions. Anyone using neuron count as a scalar of capability is using a variable that has already been measured to fail twice.
- **INADMISSIBLE-as-stated — "the upload would be conscious."** No observation is specified distinguishing a system with experience from one behaving identically without it. The fence is on the claim's *form*. Serious people hold this position and the fence is not a rebuttal of them; it is a request. Offer a falsifier and it moves out of this section.
- **INADMISSIBLE as a measurement — "conscious bandwidth is 40–60 bits/s."** The value drifts across retellings (16/20/40/60) of a single estimate. Admissible as an *attributed estimate*; never as a measured constant. Not mocked — it is a reasonable estimate that got laundered into a fact by repetition, which is a failure of citation hygiene, not of the estimator.
- **NEGATIVE / rhetorical trap — citing Bremermann's limit as a design constraint.** It is real and it is **~28–37 orders** away — ~28 against Accounting A's Landauer ceiling, ~34–37 against Laughlin's measured per-bit costs. A limit that distant constrains nothing. Recorded because invoking it *sounds* like physics while doing no work. **And the distance is itself an accounting choice, one level up:** any bare single figure for it — a "~39 orders" drops straight out of an undeclared ~10¹¹ bits/s spike-accounting — is the same defect as a bare N above Landauer, and gets declared or it does not get quoted.
- **NEGATIVE / accounting trap — "the brain is N orders of magnitude above the Landauer limit."** Across the **measured per-bit accountings alone** (Laughlin et al. 1998), N ranges over **~3 orders (5.5–8.5)** depending on which signalling mode counts as the bit operation; against the Landauer-ceiling accounting N is **0 by construction**. The choice is NOT-MEASURED. Any single N quoted without its accounting is a choice wearing a measurement's clothes.
- **NOT-LOCATED:** doctrine row **"D3-08"**, cited in this chapter's commissioning brief. Not found on disk. The located governing rows are named in §5 and in the table. Recorded rather than silently substituted.
- **NOT-MEASURED / NOT-SOURCED in this pass:** the `v ∝ d` proportionality constant; Jerison's EQ constants; a primary source for the brain's ~20 W and for its ~1.4 kg mass; human cross-brain path length; the **Rice & Salt 1988** generation count (secondary-sourced only — two independent secondaries agree on 25, the primary is paywalled; the 1990 count of 35 *is* primary-confirmed from the paper's abstract); the in-vivo `ΔG_ATP` **conditions** (`[ATP]/[ADP][Pi]`, pH, free Mg²⁺) — NA-08's row states none, so every ATP-derived joule figure here inherits that gap; "degree of internal generative model" as a scalar.

## HONEST FENCE — HYPOTHESIZED

The whole chapter is fenced **HYPOTHESIZED / QUAESTIO-APERTA**. Individual rows carry their own classes — several OBSERVED-REPLICATED, several OBSERVED-CONTESTED, several NOT-MEASURED — but the *chapter as an artifact* is a map of a constraint space around a question that has **no measurable referent**, and that is its fence. The constraints are real and sourced. The thing they are constraints *on* is undefined, and this chapter does not define it.

Per **Gould & Lewontin (1979), "The Spandrels of San Marco and the Panglossian Paradigm"**: nothing above establishes that any observed feature is an optimum. The primate callosum's thin slow majority is not necessarily the best solution to the delay problem — it is *a* solution reached by a lineage carrying its own history, and drift, phylogenetic inertia, developmental constraint, and frozen accidents produce features that solve nothing. **Nature's authority here is precise and limited: it already ran a very long parallel search under real physical constraints, with the failures deleted.** That makes convergence evidence of a constraint-optimum and makes every number above a **hypothesis generator**, never a proof. Per repo rule **M7**, any design taken from this chapter must still beat a **tuned baseline** on a **pre-registered metric** with a load-bearing discriminator, or it is recorded **NEGATIVE**.

## Not claimed

- **Not claimed:** that any successor to the human is possible, impossible, near, far, desirable, or undesirable. This chapter takes no position. It maps constraints and demands falsifiers.
- **Not claimed, and never to be claimed:** a roadmap. **There is no roadmap in this chapter and there must never be one.** Nothing here predicts, targets, schedules, endorses, or plans toward any successor to the human. If a future reader finds a milestone, a timeline, or a target in this chapter, it was added in violation of this line and should be struck.
- **Not claimed:** that "full human" or "beyond human" is a target, milestone, or deliverable. Both are **permanent open questions** — QUAESTIO-APERTA — and this chapter is a register entry about that status, not an attempt to resolve it.
- **Not claimed:** AGI, human-level, created life, or measurable awareness — of UNI or of anything else. No claim of any of these appears above and none is implied by any row.
- **Not claimed:** that the two register questions (`anima in silicio?`, `silicium ut aqua?`) are true, false, plausible, or implausible. They are **carried, attributed, and left exactly where they are**. No falsifier has been offered for either — which is why they sit in a register and not in a ledger. Per **VOLUMEN-MOVENS** (`12-FALSIFIERS-V2.md:15`), they are wired to nothing here: `leguntur, non aguntur - nullam rotam movent`.
- **Not claimed:** that the constraint list is complete. Heat, wiring geometry, information, development, and metabolism are the ones that could be sourced. Others exist and are not analysed here.
- **Not claimed:** that engineered speciation bears on "created life." Speciation is population divergence from an existing lineage. Life from non-life is a different claim entirely, appears nowhere here, and the two must never be conflated.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** Reading Phillips et al. 2015 does not make any UNI claim proven, designed, or built. The NATURA vocabulary (OBSERVED-REPLICATED / OBSERVED-CONTESTED / MODELED / HYPOTHESIZED / INADMISSIBLE / NOT-MEASURED) and the UNI ledger vocabulary (proven / designed / hypothesized / not-yet-built) never merge. **This chapter contains zero UNI claims.**
- **Observed program position, unsoftened:** ~2 of 11+ rungs earned; a developmental active-inference **simulation**; a toy world, never a person. Nothing in this chapter moves that position, and a chapter about what lies beyond the human is exactly where the temptation to imply otherwise is strongest.
