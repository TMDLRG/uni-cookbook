# NA-09 — Morphogenesis: how a pattern comes from no pattern

> **What you are reading.** The bridge from *cell* to *organism*. A morphogen gradient is
> literally a gradient — this is where "all the gradients between" stops being a figure of
> speech and becomes a measured concentration profile with a length constant in microns. This
> chapter carries nature's observed regularities about how form arises, classed under the
> NATURA vocabulary (OBSERVED-REPLICATED / OBSERVED-CONTESTED / MODELED / HYPOTHESIZED /
> INADMISSIBLE / NOT-MEASURED). **None of it is a UNI gate.** Reading Turing raises no rung.

---

## 1. The problem, stated so it can be answered

An egg is, to a first approximation, a bag of well-mixed cytoplasm. An animal is not. The genome
does not contain a picture of the organism; it contains local rules, identical in every cell.
Morphogenesis is the question of how local rules with no map produce a global form — reliably, at
the right size, in the right orientation, and recovered when you cut it. Two ideas have carried
most of the weight for seventy years. They are usually taught as rivals. They are not.

## 2. Turing's inversion: the destroyer of pattern makes pattern

Turing (1952), *The Chemical Basis of Morphogenesis*, Phil Trans R Soc Lond B 237(641):37–72,
made a claim that is still counter-intuitive on the fifth reading. Diffusion is the canonical
homogenizer: left alone, it erases every gradient it touches. Turing showed that when diffusion
is **coupled to reaction**, and the two species diffuse at *different* rates, the uniform steady
state can become unstable — and the instability has a **preferred length scale**. Diffusion stops
smoothing and starts sculpting.

The mechanism: a short-range **activator** catalysing its own production, plus a long-range
**inhibitor** that the activator also produces and that suppresses it. A local bump of activator
amplifies itself, but its inhibitor outruns it and shuts down the neighbourhood. Local
self-reinforcement, lateral suppression — yielding a stationary periodic pattern whose spacing is
set by chemistry, not by any pre-existing map.

**The math, stated so it is falsifiable.** For the two-species system

```
∂u/∂t = f(u,v) + D_u ∇²u        (u = activator)
∂v/∂t = g(u,v) + D_v ∇²v        (v = inhibitor)
```

perturbations of wavenumber `k` about the homogeneous fixed point grow when

```
h(k²) = D_u D_v k⁴ − (D_v f_u + D_u g_v) k² + det J < 0
```

where `J` is the Jacobian of `(f,g)`. At the onset of instability `h` has a double root, so the
**critical wavenumber and wavelength** are

```
k_c² = √( det J / (D_u D_v) )        λ_c = 2π / k_c = 2π ( D_u D_v / det J )^(1/4)
```

(Turing 1952; standard treatment in Murray (2003), *Mathematical Biology II*, 3rd ed., Springer,
ch. 2.) The instability condition `D_v f_u + D_u g_v > 2√(D_u D_v · det J)` is worth staring at:
set `D_u = D_v` and it collapses to `tr J > 2√(det J)`, which contradicts the stability of the
well-mixed state (`tr J < 0`). **So in a two-species system, equal diffusivities can never give
a Turing pattern.** `D_inhibitor > D_activator` is not a modelling convenience; it is forced.

**The ratio: say exactly what is and is not known.** `d = D_v/D_u > 1` is strict and general. A
*universal* critical ratio `d_c` is **NOT-MEASURED — because it does not exist**: `d_c` is a
function of the reaction kinetics, not a constant of nature, so quoting "you need 10×" as a law
is a category error. What *is* real is the practical difficulty — for common kinetics the
required ratio exceeds what two morphogens of similar molecular size can supply, and the
parameter windows are narrow (the **fine-tuning problem**). And the constraint is narrower than
the two-species theorem suggests: Marcon, Diego, Sharpe & Jaeger (2016), *eLife* 5:e14022, showed
that networks including **cell-autonomous (non-diffusing) nodes** can pattern with *equally*
diffusing signals, for any combination of diffusion coefficients.

## 3. The honest part — and the main lesson of this chapter

For roughly four decades, Turing patterning was a beautiful theory with thin biological
evidence. Appearance was doing the work: an animal had stripes, a reaction-diffusion simulation
made stripes, therefore reaction-diffusion. **That inference is invalid**, and the field says so
in print. Kondo (2022), *The present and future of Turing models in developmental biology*,
Development 149(24):dev200974, states it plainly: *"even if a spatial patterning is successfully
reproduced by a reaction-diffusion model, it may not be clear whether or not a diffusion factor
is responsible."* Many "Turing patterns" in the popular literature are **pattern-matching on
appearance, not identified mechanism.** Fitting a pattern is not identifying a cause.

What raises the class is a **diagnostic perturbation** — an experiment whose outcome the Turing
mechanism predicts and the alternatives do not:

| System | The load-bearing discriminator | Source |
|---|---|---|
| Zebrafish pigment stripes | Laser-ablate a square of melanophores in a stripe; the pattern **regenerates** and the ablation response maps short-range activation + long-range inhibition between cell types. The interaction network — not a fitted image — carries the property. | Nakamasu, Takahashi, Kanbe & Kondo (2009), *PNAS* 106:8429–8434 |
| Mouse palatal rugae | Excise a ruga. New Shh stripes appear **not at the cut edge** but as *bifurcating* stripes branching off the neighbouring stripe — the signature of reaction-diffusion, and not of a pre-patterned map. FGF/Shh identified as the activator–inhibitor pair. | Economou, Ohazama, Tucker & Sharpe (2012), *Nat Genet* 44:348–351 |
| Mouse digits | A Bmp-Sox9-Wnt network, modulated by morphogen gradients, recapitulates wild-type Sox9 stripes **and the perturbation experiments**. | Raspopovic, Marcon, Russo & Sharpe (2014), *Science* 345(6196):566–570 |

Note the fence on the third row honestly: Raspopovic et al. established the network by **modelling
plus perturbation**, not by measuring the diffusivities of the species in the limb bud. It is the
strongest available case for a molecular Turing system in a tetrapod limb, and the diffusible
identities remain model-inferred. That is **OBSERVED-CONTESTED**, and saying so costs nothing.

## 4. Wolpert's French flag: position first, fate second

Wolpert (1969), *Positional information and the spatial pattern of cellular differentiation*,
J Theor Biol 25(1):1–47 (DOI 10.1016/S0022-5193(69)80016-0), proposed the complementary idea. A
line of cells reads a monotonic gradient; each cell compares the local concentration against
**thresholds** and adopts a fate — blue, white, red. Gradient → threshold → fate. Position is
measured *before* it is interpreted, and the interpretation is a gene regulatory network acting
as a comparator bank.

The difference from Turing is precise and worth memorising: **positional information is not a
self-organising mechanism.** It presupposes an earlier asymmetry — a source, a pole, a polarity —
and explains only the readout. Turing manufactures asymmetry from nothing but needs no map.
Green & Sharpe (2015), *Development* 142(7):1203–1211, is the field's reconciliation: the two
work *together*, in identifiable combinations — a gradient can bias, orient, or locally tune a
reaction-diffusion system (exactly what the digit network does), and a reaction-diffusion output
can in turn serve as the positional cue another tissue reads. Rivalry was never the right frame.

## 5. Bicoid, and a gradient measured to the physical limit

The Drosophila Bicoid gradient is the most heavily quantified positional system in biology, and
it closes the loop with NA-08's physical-limits framing.

The gradient is roughly exponential with a **length constant λ ≈ 100 μm** in an embryo of
**L ≈ 490 μm** (Gregor, Wieschaus, McGregor, Bialek & Tank (2007a), *Stability and nuclear
dynamics of the Bicoid morphogen gradient*, Cell 130(1):141–152). In the companion paper —
Gregor, Tank, Wieschaus & Bialek (2007b), *Probing the limits to positional information*,
Cell 130(1):153–164 — four independent measures of precision all land near **10%**: the Bicoid
difference between **adjacent nuclei** (~8 μm apart) at the hunchback boundary is only ~10%, yet
those nuclei express *significantly different* Hunchback; and the *hb* domain is positioned along
the AP axis to **2–3% of egg length**.

Here is why this is a physics result and not a biology anecdote. Applying the **Berg–Purcell**
scheme — concentration estimated by counting ligand-binding events — the authors estimate that a
single Bcd binding site at the *hb* promoter would need **of order 2 hours** to read the
concentration to 10% accuracy. The embryo does it in minutes. The readout is therefore *at or
near* the physical limit, and must be recruiting spatial and temporal averaging (across binding
sites, across nuclei, across time) to get there. Development is not merely using a gradient; it
is **estimating a latent variable about as well as the physics of molecular counting permits.**
Dubuis, Tkačik, Wieschaus, Gregor & Bialek (2013), *Positional information, in bits*,
PNAS 110(41):16301–16308, closes it: four gap genes jointly specify a cell's location with an
error bar of **~1% egg length** — near the point where every cell row could have a unique
identity, and nearly constant along the axis.

**And now the contested part, printed rather than buried.** The synthesis-diffusion-degradation
(SDD) picture requires `λ ≈ √(D τ)`. Gregor et al. (2007a) measured Bicoid-eGFP diffusion at
**D = 0.30 ± 0.09 μm²/s** (FRAP; 0.37 ± 0.05 by an indirect nuclear-exchange estimate). The
arithmetic is unforgiving: τ ≈ λ²/D ≈ (100 μm)²/(0.3 μm²/s) ≈ 3.3×10⁴ s ≈ **9 hours** — but the
gradient is established roughly **1 hour** after fertilization. Grimm, Coppey & Wieschaus (2010),
*Modelling the Bicoid gradient*, Development 137(14):2253–2264, print the conclusion: with this
diffusivity *"models 1–3 cannot explain the experimentally observed length scale of the
gradient"* — the measured D is *"an order of magnitude too small"*. The single best-measured
gradient in developmental biology **does not close against its own simplest model.** That is
OBSERVED-CONTESTED, it is the most instructive row in this chapter, and any account that omits it
is selling a story.

## 6. Scaling: the same proportions at a different size

An embryo half the size still builds correct proportions. A pure SDD gradient does not scale —
its λ is set by D and τ, which know nothing about egg length. Yet Bicoid's length constant does
track egg length across dipteran species (Gregor, Bialek, de Ruyter van Steveninck, Tank &
Wieschaus (2005), *Diffusion and scaling during early embryonic pattern formation*,
PNAS 102:18403–18407), and the Dpp gradient of the Drosophila wing disc scales with disc size —
with the striking downstream regularity that mitosis onset tracks a **50% increase in Dpp
signalling since the start of the cell cycle** (Wartlick et al. (2011), *Dynamics of Dpp
signaling and proliferation control*, Science 331:1154–1159).

The leading mechanism is **expansion–repression** (Ben-Zvi & Barkai (2010), PNAS
107(15):6924–6929): a diffusible *expander* widens the gradient, and morphogen signalling
represses the expander's production. Sharp gradient → expander expressed widely → expander
accumulates → gradient widens → expander domain shrinks → steady state at the size-matched width.
It is an **integral feedback controller** in the exact control-theoretic sense: the system
integrates its own error until the error vanishes. Class **MODELED** — the topology is general,
but the expander's molecular identity is system-specific and not a settled universal.

## 7. The control logic, and the landscape metaphor

Gene regulatory networks are the comparator bank: cooperative binding gives sigmoidal
input–output, mutual repression between neighbouring fates sharpens a shallow gradient into a
crisp boundary, and feedback buys robustness to input noise. Waddington's **canalization** and
his *epigenetic landscape* (Waddington (1957), *The Strategy of the Genes*, Allen & Unwin) — the
ball rolling down branching valleys — is the field's most famous picture.

**Be honest about what it is: a metaphor, not a measurement.** Nobody measured a landscape. There
is a real modern formalization — Ferrell (2012), *Bistability, bifurcations, and Waddington's
epigenetic landscape*, Current Biology (PMID 22677291), maps valleys to stable steady states,
ridges to unstable ones, valley-splitting to pitchfork bifurcations. Ferrell's own finding is the
interesting one: worked through for cell-fate induction, the computed landscape **does not**
qualitatively resemble Waddington's picture. The metaphor survives as intuition and fails as
geometry. The bistability formalism is MODELED; the landscape-as-drawn is HYPOTHESIZED at best.

## 8. Mechanics is a morphogen — and this is the wing's strongest case

Chemistry is not the only patterning field. Force is one too, and here the evidence is
quantitative, predictive, and — decisively — **physically instantiated outside the organism.**

**Differential adhesion.** Steinberg's hypothesis (Steinberg (1963), *Reconstruction of tissues
by dissociated cells*, Science 141) held that tissues behave as immiscible liquids whose
"surface tensions" arise from differential intercellular adhesion, so sorting and envelopment
follow from thermodynamics. Foty, Pfleger, Forgacs & Steinberg (1996), Development
122(5):1611–1620, measured it on chick embryonic tissues by parallel-plate compression and got a
strict hierarchy that **predicts which tissue envelops which**: limb bud mesoderm σ = 20.1
dyn/cm, pigmented epithelium 12.6, heart 8.5, liver 4.6, neural retina 1.6. Foty & Steinberg
(2005), *Dev Biol* 278:255–263, then tuned cadherin levels in L cells and recovered a **linear**
relation between aggregate surface tension and surface cadherin density. Measured, ordered,
predictive.

**Buckling.** Savin, Kurpios, Shyer, Florescu, Liang, Mahadevan & Tabin (2011), *On the growth
and form of the gut*, Nature 476:57–62, showed that the gut's reproducible looping comes from
**differential growth** between the gut tube and the anchoring dorsal mesentery — homogeneous,
isotropic forces, no map. They then built the discriminator: a **physical mimic** out of a
pliable rubber tube stitched to a stretched latex sheet, which produces the same loops; and a
theory whose predictions for loop number, size and shape — from measured geometry, elasticity and
relative growth alone — are quantitatively consistent with chick embryos across stages. Shyer et
al. (2013), *Villification: how the gut gets its villi*, Science 342(6155):212, extended it: the
sequential differentiation of smooth muscle layers restricts growth, and the compressive stress
buckles the epithelium through ridges → zigzags → individual villi.

**Cortical folding.** Tallinen, Chung, Biggins & Mahadevan (2014), *Gyrification from constrained
cortical expansion*, PNAS 111:12667–12672, showed that gyri and sulci arise as a nonlinear
mechanical instability from tangential expansion of grey matter constrained by white matter: when
transversely isotropic tangential expansion exceeds **g ≈ 1.29**, sulcification becomes
energetically favourable, and brain-like deep sulci appear when the **grey/white shear modulus
ratio is near unity**. Then Tallinen, Chung, Rousseau, Girard, Lefèvre & Mahadevan (2016), *On
the growth and form of cortical convolutions*, Nat Phys 12:588–593, did the thing that makes this
the strongest nature-as-authority case in the wing: they **3D-printed a fetal brain from MRI,
coated it in a swelling gel, and put it in solvent** — and the gel folded into sulci and gyri
resembling the real brain. A physical object, outside biology, reproducing the form. This is what
"nature has already run the experiment" cashes out to when it is earned: not an analogy, a
*replication of the mechanism in a different substrate*.

## 9. Regeneration and bioelectric prepatterns

Pattern is not only built; it is *maintained and restored*. Beyond gradients and forces sits a
bioelectric layer — standing voltage and gap-junctional coupling carrying spatial information.
Emmons-Bell, Durant, … Lobo & Levin (2015), *Int J Mol Sci* 16(11):27865–27896, blocked gap
junctions in **genetically wild-type** *Girardia dorotocephala* planaria and got regenerated heads
with the shapes and brain morphologies of *other species* — stochastically, reverting weeks later.
Genome unchanged; form changed. **NA-08**'s standing fence on the bioelectric literature applies
here unchanged: the observations are real, the "pattern memory" reading is an interpretation, and
the two travel separately.

## 10. The active-inference reading — a lens, not a result

Friston, Levin, Sengupta & Pezzulo (2015), *Knowing one's place: a free-energy approach to
pattern regulation*, J R Soc Interface 12(105):20141383, recast development as inference: cells
sharing a generative model of organismal form act to minimize surprise about their own expected
place in it, and the target morphology becomes the prior. Under this reading a morphogen gradient
is a *sensory channel about position*, threshold readout is *inference over a latent variable*,
and regeneration is *active inference* — acting to make the sensed state match the expected one.

**Class: HYPOTHESIZED / MODELED. This is a reframing, not a measurement.** The paper offers a
proof of principle by simulation. It is admissible here for exactly one reason: it is
*consilient* with a measured fact — Gregor 2007b's finding that positional readout runs near the
Berg-Purcell limit is what one would expect of a system doing near-optimal estimation. Consilience
is not confirmation. The lens has not yet paid for itself with a prediction that a
non-inferential model of the same system would get wrong, and until it does, it is vocabulary.

## 11. Nature as authority here — and the counterweight, in the same breath

Nature is the authority here because it already ran the search: buckling, adhesion hierarchies and
reaction-diffusion are what survived under real physical constraint, and their independent
re-appearance across lineages is **evidence of a constraint-optimum**. That is the whole claim,
and it is a **hypothesis generator**.

Gould & Lewontin (1979), *The spandrels of San Marco and the Panglossian paradigm*, Proc R Soc
Lond B 205(1161):581–598 (DOI 10.1098/rspb.1979.0086), is the counterweight, and it bites hardest
exactly here. Gut loops and cortical folds are *mechanical consequences of differential growth*.
Whether the resulting shape is an adaptation **for** anything is a question the mechanics does not
answer — a fold can be a spandrel, a by-product of how the thing was built. So: a biomimetic
design must still beat a **tuned conventional baseline** on a **pre-registered metric** (repo rule
M7), or it is recorded NEGATIVE. "Nature folds it this way" is where the work starts.

## The numbers (the ratio/frequency table)

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| λ_Bcd | ≈ 100 | μm | *D. melanogaster* early embryo, L ≈ 490 μm | OBSERVED-REPLICATED | Gregor et al. (2007a), Cell 130(1):141–152 | Independent Bcd-GFP profiling giving a decay constant far outside ~80–120 μm at standard temperature |
| L | ≈ 490 | μm | same embryo, AP axis | OBSERVED-REPLICATED | Gregor et al. (2007a) | Direct imaging outside ~450–550 μm |
| D_Bcd | 0.30 ± 0.09 (FRAP); 0.37 ± 0.05 (indirect) | μm²/s | cortical cytoplasm, cycles 10–14 | **OBSERVED-CONTESTED** — incompatible with λ ≈ 100 μm under SDD | Gregor et al. (2007a); dispute printed in Grimm et al. (2010), Development 137(14):2253–2264 | A method giving D large enough that √(Dτ) reproduces λ within the ~1 h formation window would dissolve the tension |
| τ_required | ≈ 9 (≈3.3×10⁴ s) | hours | SDD arithmetic λ²/D from the two rows above | MODELED (derivation from cited inputs) | Grimm et al. (2010): D is *"an order of magnitude too small"* | A non-SDD transport mechanism (e.g. mRNA-distribution or active transport) reconciling λ, D and the ~1 h window |
| Δc/c | ≈ 10 | % | adjacent nuclei (~8 μm apart) at the *hb* boundary, cycle 14 | OBSERVED-REPLICATED | Gregor et al. (2007b), Cell 130(1):153–164 | Measured inter-nuclear Bcd difference at the boundary ≫ or ≪ 10% |
| σ_x (*hb* domain) | 2–3 | % egg length | *hb* transcription domain position, embryo-to-embryo | OBSERVED-REPLICATED | Gregor et al. (2007b) | Reproducibility measured far worse (≫3% EL) in a clean prep |
| σ_x (4 gap genes) | ≈ 1 | % egg length | joint gap-gene readout, AP axis, near-constant along axis | OBSERVED-REPLICATED | Dubuis et al. (2013), PNAS 110(41):16301–16308 | Decoding a fresh dataset yielding error ≫1% EL |
| τ_Berg-Purcell | order of 2 | hours | time for ONE *hb* Bcd binding site to read c to 10% accuracy | MODELED (assumes: diffusion-limited binding, single independent site, Berg-Purcell counting) | Gregor et al. (2007b) | A binding-kinetics measurement showing single-site 10% accuracy achievable in minutes |
| k_c² | √( det J / (D_u D_v) ) | μm⁻² | 2-species reaction-diffusion at instability onset | MODELED (assumes: two species, linear stability about a homogeneous fixed point) | Turing (1952), Phil Trans R Soc B 237(641):37–72; Murray (2003) ch. 2 | A measured 2-species Turing wavelength not tracking (D_u D_v/det J)^(1/4) |
| d = D_v/D_u | > 1, strictly | dimensionless | 2-species activator–inhibitor only | MODELED | Turing (1952); Murray (2003) | An observed 2-species Turing pattern with measured D_u = D_v and no cell-autonomous node |
| d_c (universal) | **NOT-MEASURED — no such constant** | — | `d_c` is kinetics-dependent, not a constant of nature | NOT-MEASURED | — | Exhibit a kinetics-independent threshold; none is known |
| d requirement (≥3 nodes) | can be **any** ratio, incl. 1:1 | dimensionless | networks containing cell-autonomous (non-diffusing) nodes | MODELED | Marcon et al. (2016), *eLife* 5:e14022 | A proof that cell-autonomous nodes cannot relax the constraint |
| g_c | ≈ 1.29 | dimensionless (tangential expansion ratio) | grey matter on white, μ_grey/μ_white ≈ 1, soft-solid model | MODELED | Tallinen et al. (2014), PNAS 111:12667–12672 | Physical/gel model sulcifying at a markedly different expansion |
| σ (limb bud mesoderm) | 20.1 | dyn/cm | chick embryonic tissue aggregate, parallel-plate compression | OBSERVED-REPLICATED | Foty et al. (1996), Development 122(5):1611–1620 | Remeasurement inverting the envelopment hierarchy |
| σ (pigmented epithelium / heart / liver / neural retina) | 12.6 / 8.5 / 4.6 / 1.6 | dyn/cm | as above | OBSERVED-REPLICATED | Foty et al. (1996) | A tissue enveloping one of higher measured σ |
| σ vs cadherin density | linear | — | transfected L-cell aggregates (E-, N-, P-cadherin) | OBSERVED-REPLICATED | Foty & Steinberg (2005), Dev Biol 278:255–263 | Titration showing no monotone σ–cadherin relation |
| Dpp mitosis trigger | ≈ 50 | % increase in signalling since cell-cycle start | *Drosophila* wing imaginal disc | OBSERVED-REPLICATED | Wartlick et al. (2011), Science 331:1154–1159 | Division timing uncorrelated with relative Dpp increase |
| Golden angle | ≈ 137.5 | degrees | phyllotactic divergence angle; reproduced physically | OBSERVED-REPLICATED **with mechanism** | Douady & Couder (1992), *Phys Rev Lett* 68:2098–2101 | A repulsion-dynamics system in the same parameter regime not converging to ~137.5° |

## Falsifier (operable)

This chapter is refuted if any of the following is observed:

1. **A two-species Turing pattern in a real tissue with `D_activator = D_inhibitor`** and no
   cell-autonomous node in the network. That would break the linear-stability theorem in §2, not
   just an example.
2. **A measured Turing wavelength that does not track `2π(D_u D_v/det J)^(1/4)`** when all four
   inputs are measured independently in the same system.
3. **The Bicoid tension resolves in the wrong direction**: a direct measurement of D that is both
   ~0.3 μm²/s *and* consistent with λ ≈ 100 μm forming within ~1 hour under SDD. The arithmetic
   forbids this; if it were observed, the arithmetic or a measurement is wrong.
4. **Positional readout beating the Berg-Purcell bound** without spatial/temporal averaging —
   i.e. a single binding site achieving 10% accuracy in minutes. That would refute the physical-
   limit framing this chapter shares with NA-08.
5. **Gut looping or cortical folding failing the physical model quantitatively** — a chick gut
   whose loop number/size departs from the measured-geometry prediction, or a swelling-gel brain
   that does not fold at g ≈ 1.29 with modulus ratio ≈ 1.
6. **The envelopment hierarchy inverting**: a tissue of measured lower σ failing to envelop one
   of higher σ.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **"It looks like a Turing pattern, therefore it is one."** INADMISSIBLE. Fitting an image is
  not identifying a mechanism, and the field says so: *"even if a spatial patterning is
  successfully reproduced by a reaction-diffusion model, it may not be clear whether or not a
  diffusion factor is responsible"* — Kondo (2022), Development 149(24):dev200974. Receipt of
  failure: for ~40 years the theory ran ahead of any identified molecular system. The admissible
  form requires a **diagnostic perturbation** (§3), not a resemblance.
- **"Turing requires D_inhibitor/D_activator ≥ 10, universally."** INADMISSIBLE as stated. `d_c`
  is set by the kinetics; there is no kinetics-independent threshold. The defensible statements
  are `d > 1` strictly (2-species) and "the required ratios are often implausibly large for
  similarly-sized morphogens" (the fine-tuning problem) — and even the strict requirement is
  relaxed by cell-autonomous nodes (Marcon et al. 2016).
- **The Bicoid SDD closure.** Recorded **NEGATIVE, carried with the PASS.** The best-measured
  gradient in biology has a measured D an order of magnitude too small to explain its own length
  constant under the simplest model (Grimm et al. 2010). The precision results (§5) stand; the
  transport model does not close. Both are printed.
- **Waddington's landscape as a measured object.** INADMISSIBLE as physics. It is a metaphor.
  The honest modern statement: bistability/bifurcation formalism is MODELED, and Ferrell (2012)
  found that a worked cell-fate-induction landscape does **not** qualitatively resemble
  Waddington's drawing. Recorded as a NEGATIVE *for the picture*, not for the intuition.
- **"The golden ratio is a universal design law of nature."** INADMISSIBLE — unfalsifiable as
  stated and sustained by cherry-picking. The **earned** neighbouring claim, recorded with
  respect: the golden angle ≈137.5° in phyllotaxis is real *and mechanistically explained* —
  Douady & Couder (1992) reproduced it in a **physical ferrofluid-droplet experiment** from
  simple repulsion between successively-placed elements, no mysticism required. Same subject
  matter; opposite evidence class. Honour the first, fence the second, mock neither.
- **"Development is active inference."** Not asserted. HYPOTHESIZED (§10). A lens.

## HONEST FENCE — OBSERVED-CONTESTED

The chapter's spine is OBSERVED-REPLICATED (the Bicoid precision numbers, the tissue surface
tensions, the ablation/excision diagnostics, the golden angle). But the chapter as a whole is
fenced **OBSERVED-CONTESTED**, and deliberately so: the single best-quantified morphogen gradient
in developmental biology **does not close against its own simplest transport model** (Grimm et al.
2010), and the general question of how many real patterns are mechanistically Turing rather than
Turing-shaped is live (Kondo 2022). Both positions are carried above. A chapter on morphogenesis
that reads as settled has been edited for comfort.

## Not claimed

- **Not claimed:** that reaction-diffusion is the general mechanism of biological patterning. It
  is *an* identified mechanism in a small number of systems (§3) and a hypothesis elsewhere.
- **Not claimed:** that the Bicoid gradient is understood. Its precision is measured; its
  transport is contested (§5).
- **Not claimed:** that gut loops, villi or cortical folds are adaptations *for* anything. Their
  **mechanics** is measured and predictive; their **adaptive value** is a separate question this
  chapter does not answer (§11, Gould & Lewontin).
- **Not claimed:** that development *is* inference, or that minimizing free energy explains
  morphogenesis. Friston et al. (2015) is a reframing consilient with one measured fact; it has
  not yet made a discriminating prediction (§10).
- **Not claimed:** that any of the above raises any UNI rung. **A nature citation is never a UNI
  gate.** Nothing in this chapter is evidence about UNI's build status; consult
  [`../CLAIM-LEDGER.md`](../CLAIM-LEDGER.md) for that, and never cross the two vocabularies.
- **Not claimed:** that "the next evolution beyond human" is a target, milestone or deliverable
  of anything here. It remains **QUAESTIO-APERTA** — a permanent open question. Morphogenesis
  describes how the forms that exist come to be; it licenses no roadmap for forms that do not.
- **Not claimed:** that Waddington's landscape is a real surface, or that any chakra/frequency
  scheme has a morphogenetic mechanism. The former is a metaphor; the latter is INADMISSIBLE as
  physics and may be recorded only as an HONEST/cultural signal, never as a TRUE/measured one.

---

> **Cross-references.** NA-08 (physical limits of sensing; the Berg-Purcell bound; the standing
> bioelectric fence). Wing N (the free-energy lens, kept honest). Rule M7 (contains-baseline +
> load-bearing discriminator) governs every biomimetic design derived from this chapter.
