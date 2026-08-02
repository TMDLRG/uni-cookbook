# Build the animals — scaling limits, low-frequency sound, and measurable active inference

> **Knowledge file `K15-RECIPES-dinosaurs-whales-bats.md`** of the UNI Encyclopedia & Cookbook GPT pack.
> This file is a BUILD ARTIFACT: it merges **3** source file(s) from the
> repository `TMDLRG/UNI-Encyclopedia-Cookbook`, byte-for-byte, in the order listed below.
> The repository is the single source of truth; if this file and the repository ever
> disagree, the repository wins and this file is stale.
>
> SOVEREIGNTY RULE (binding, do not merge the two ledgers): this corpus carries TWO sovereign evidence vocabularies. The UNI 4-value fence (proven / designed / hypothesized / not-yet-built) describes ONLY UNI's own build status and is governed by encyclopedia/CLAIM-LEDGER.md. The NATURA 12-value class, in three groups, describes ONLY nature's observed regularities and is governed by encyclopedia/NATURE-LEDGER.md: group A / measured = OBSERVED-REPLICATED, OBSERVED-SINGLE, OBSERVED-CONTESTED; group B / derived = MODELED, MODELED-CONTESTED, HYPOTHESIZED; group C / fenced = INADMISSIBLE, SUPERSEDED, NOT-MEASURED, NOT-SOURCED, NOT-CONFIRMED, NOT-LOCATED. Six of the twelve were registered by NA-00 amendment 2026-07-15-A after the corpus refuted the original 'six classes and only six' at 72 of 919 ledger rows; twelve is a MEASURED property of the corpus, not a design target. NEVER read NOT-SOURCED as NOT-MEASURED: the first says we could not trace the source (a fact about us), the second says nobody has measured it (a claim about the frontier of science). A nature citation is NEVER a UNI gate. Cross-reference between them by explicit link only, never by merge.


**Source files merged into this knowledge file, in order:**

- `cookbook/recipes-natura/CN-08-dinosaurs.md`
- `cookbook/recipes-natura/CN-09-whales.md`
- `cookbook/recipes-natura/CN-10-bats.md`

---



<!-- ===== BEGIN cookbook/recipes-natura/CN-08-dinosaurs.md ===== -->

# CN-08 — Dinosaurs: the scaling limits of a land animal, and how to measure the dead

> **What you are building.** A working method for doing falsifiable science on a system you can never observe, instrumented on the hardest available case: animals that have been dead for 66 million years, that no one has ever seen move, breathe, or bleed. The animals are the worked example. **The epistemics are the payload.** Every number below either carries a source you can check or is written NOT-MEASURED / NOT-SOURCED. Nothing here raises any UNI rung — a citation to palaeontology is never a UNI gate.

---

## The problem this chapter exists to solve

You cannot run the experiment. The animal is gone, the soft tissue is gone, the behaviour is gone. What remains is a mineralised fraction of a skeleton, some footprints pressed into mud that happened to lithify, and — crucially — **physics that has not changed**.

That last clause is the entire method. Gravity was 9.81 m/s². Bone was bone. A column of blood weighed what a column of blood weighs. **The constraints outlived the animal**, and constraints are what make a claim falsifiable. Anything you assert about a dinosaur that does not route through a surviving constraint is decoration.

So the discipline is: find the constraint, state it as an equation, feed the fossil in, **and publish the error bar as loudly as the number.** The chapter runs that loop on bone, mass, speed, breath, heat and necks — and shows it failing twice. The failures are the point.

## The constraint that cannot be negotiated

Galileo got there first, in 1638, in the *Discorsi e dimostrazioni matematiche intorno a due nuove scienze* — the "First Day"/"Second Day" discussion of why a bone scaled up in every dimension must eventually break under its own weight. The argument is three lines and it has never been refuted:

- Mass grows with volume: `M ∝ L³`
- Bone cross-section grows with area: `A ∝ L²`
- Therefore stress: `σ = F/A ∝ L³/L² = L`

**Double the animal geometrically and you double the stress in its bones.** Not the load — the *stress*. Bone strength per unit area is a material property and does not care how big you are. So geometric scaling has a ceiling, and it arrives fast.

Three published escapes exist, and the exponents are the whole argument (cross-ref NA-05, scaling; NA-07, dimensionless numbers). Regressing **log bone length on log bone circumference**, each similarity model predicts a specific exponent:

| Model | Predicted exponent (length vs circumference) |
|---|---|
| Geometric similarity | **1.0** |
| Elastic similarity (McMahon) | **0.67** |
| Static stress similarity | **0.5** |

(Predicted values as tabulated by Kilbourne & Makovicky 2010, *J Anat*, their Table 8, which attributes elastic similarity to McMahon 1975a.) Elastic similarity says a limb bone must get disproportionately fat: `L ∝ D^(2/3)`.

## What the bones actually do (the instructive answer)

Here is where a lesser account would say "dinosaurs followed elastic similarity" and move on. They do not.

Kilbourne & Makovicky (2010), *J Anat*, regressed log length on log circumference (reduced major axis) for femora, tibiae and humeri across **23 dinosaur species**, through **postnatal ontogeny**. The measured exponents:

| Taxon / group | Femoral exponent | Reads as |
|---|---|---|
| *Tyrannosaurus rex* | **0.53** *(95% CI **0.04–0.97**)* | **nothing — the CI spans every model** |
| *Allosaurus fragilis* | **0.82** | between elastic and geometric |
| Sauropodomorphs (most) | **~1.0** | isometric/geometric |
| *Massospondylus carinatus* | **0.81** | between |
| *Maiasaura peeblesorum* | **1.05** | *past* geometric — getting **more gracile** |
| *Hypacrosaurus stebingeri* | **1.09** *(95% CI **1.072–1.113**)* | past geometric — **and the CI is tight** |

*(CIs quoted where retrieved from Kilbourne & Makovicky's Table 3 in this pass — the* T. rex *and* Hypacrosaurus *rows. The bare point estimates carry CIs too; they are not printed here because they were not read off the table, and this chapter does not invent error bars to decorate a number.)*

And Carrano's **interspecific** result, reported by the same authors, verbatim: "femoral exponent, 0.83; tibial exponent, 0.78; metatarsal III exponent, 0.80".

Read that table honestly and it says four things at once:

1. **Dinosaurs do not follow elastic similarity.** 0.83 is not 0.67.
2. **They do not follow geometric similarity either.** 0.83 is not 1.0.
3. **They do not follow one rule at all — but read the error bar before you say who differs from whom.** It is tempting to set *T. rex* at 0.53 against *Hypacrosaurus* at 1.09 and call it a contrast. **The data will not carry that.** The *T. rex* CI is **0.04–0.97**: it contains static-stress similarity (0.5), contains elastic similarity (0.67), and reaches to the doorstep of geometric (1.0). It **discriminates among none of them**, and a point estimate with a CI that wide cannot anchor a comparison with anything. The real signal is on the hadrosaurid side, where the intervals are tight — *Hypacrosaurus* at **1.094 (95% CI 1.072–1.113)** excludes every standard model from below, and Kilbourne & Makovicky note the hadrosaurid values "are higher than any" the standard models predict. So the honest statement is: **hadrosaurids demonstrably exceed the models; *T. rex* is uninformative.** The one-rule claim dies on the hadrosaurids alone. It does not need the theropod, and it does not get it.
4. **Intraspecific ≠ interspecific.** Growing a *Maiasaura* (1.05) and comparing adult dinosaurs to each other (femur 0.83) are different questions with different answers. Conflating them is a category error, and it is common.

This is what a real scaling result looks like: a **spread with structure in it**, not a law. The tidy models are the null hypotheses that got **partially rejected**, and the residual — the fact that hadrosaurids sit high, with intervals tight enough to exclude every standard model — is the actual finding. A model that had fit perfectly would have taught you less. *(The symmetrical claim that "big theropods sit low" is **not supported**: the* T. rex *interval spans the model space. This chapter had that contrast in an earlier draft and withdrew it — printing a point estimate bare and reading a conclusion off it is precisely the defect this chapter exists to name, and it is easier to commit than to catch.)*

## Mass: where the spread *is* the result

You cannot weigh a dinosaur. Two method families try:

- **Volumetric.** Reconstruct the body as a 3D solid, assign densities, integrate. Every step injects a judgement.
- **Extant-scaling.** Measure a load-bearing bone's circumference, push it through a regression calibrated on animals you *can* weigh. Circumference proxies cross-sectional area, which carries weight. Campione & Evans (2012), *BMC Biology* 10:60, built the canonical version on combined humeral + femoral circumference across extant quadrupedal tetrapods.

Now take one animal — *Tyrannosaurus rex* specimen **FMNH PR2081** ("Sue"), one of the best-preserved large dinosaurs in existence — and collect what **one study, on one specimen**, says at its own two extremes:

| Method / source | Estimate for FMNH PR2081 |
|---|---|
| Hutchinson et al. (2011) volumetric — **minimal** model | **9,502 kg** |
| Hutchinson et al. (2011) volumetric — **maximal** model | **18,489 kg** |

**Low to high: a factor of ~1.95.** On the *same bones*, by the *same team*, in the *same paper* — which is what makes it damning rather than merely untidy. That is not sloppiness; it is the honest width of the inference, and Hutchinson et al. (2011), *PLoS ONE* 6(10):e26037, print it themselves: their results are "complicated by specimen variation, incomplete preservation, mounting errors and investigator biases." They also do the thing that makes it science rather than a range — they **rank** the models, judging the maximal models "less plausible" and expecting true mass "much closer to our minimal models."

**And they commit to a number.** Their abstract concludes, verbatim, that "adult *T. rex* had body masses around 6000–8000 kg, with the largest known specimen ('Sue') perhaps ∼9500 kg." Print that, prominently, because a chapter that quoted this paper's *spread* while suppressing this paper's *central estimate* would be selecting the flattering half — the exact move it spends the rest of its length prosecuting.

*(**Scope note**, and it is the reason this section was rebuilt: a figure of **3,800–4,500 kg** circulates for* Tyrannosaurus*, and an earlier draft of this chapter printed it as the low end of Sue's envelope, yielding a headline spread of ~4.9×. **That was a scope error.** The figure appears in Hutchinson et al. 2011 exactly once, as a description of somebody else's input assumption — "Persons and Currie used smaller body mass estimates (3800–4500 kg) for* Tyrannosaurus*" — scoped to the **genus**, not to PR2081, and it is not the output of a scaling equation applied to this or any specimen. It is not an estimate of Sue. Putting it at the bottom of Sue's range and calling the result "the same bones" was false of that row, and it inflated the headline by a factor of two and a half. A chapter whose thesis is that scope-free numbers are unevaluable does not get to run a scope-free number as its headline.)*

Convergence has since improved. Campione & Evans (2020), *Biological Reviews* 95:1759–1797, reviewed accuracy and precision across both families and report that the two largely agree. *(Fence: retrieved at abstract/summary level in this pass; full text not fetched. The widely-repeated "~7 tonnes for an adult* T. rex*" is **squarely inside the cited literature** — Hutchinson et al. 2011's own conclusion is 6,000–8,000 kg — so the **value** is sourced. What is **NOT-SOURCED here** is its specific **attribution to this review**, because I could not open the primary. Fence the attribution, not the number.)*

**The operable rule:** a dinosaur mass quoted as a bare number is not a measurement. `M(FMNH PR2081) = 9,500 kg` is a *claim*; `M(FMNH PR2081) = 9,502 kg (minimal volumetric model; authors' preferred region; plausible envelope to 18,489 kg maximal, which the authors judge "less plausible"; Hutchinson et al. 2011)` is a *result*. A GPT — or a documentary, or a museum placard — quoting one figure with no method and no error bar has failed this chapter.

## Speed from trackways: the showpiece

This is the best thing in palaeontology: **a footprint becomes a falsifiable speed** by way of a dimensionless number (cross-ref NA-07).

Alexander (1976), *Nature* 261:129–130, published:

```
u = 0.25 · g^0.5 · λ^1.67 · h^(−1.17)
```

| Symbol | Meaning | Units |
|---|---|---|
| `u` | speed | m·s⁻¹ |
| `g` | gravitational acceleration = 9.81 | m·s⁻² |
| `λ` | **stride length** (same foot to same foot) — measured directly off the trackway | m |
| `h` | **hip height** — *not* measured; estimated as `h ≈ 4 × footprint length` | m |

*(Equation and symbol definitions as stated verbatim by Prescott et al. 2025, Biology Letters, DOI 10.1098/rsbl.2025.0191, which reproduces Alexander's 1976 formulation.)*

### Where those constants come from

The exponents look arbitrary. They are not. The equation is **algebraically identical** to the dynamic-similarity relation `λ/h = 2.3 · Fr^0.3`, where `Fr = u²/(gh)` is the Froude number. Invert it:

```
Fr = [(λ/h)/2.3]^(10/3)
u² = g·h·(λ/h)^(10/3)·2.3^(−10/3)
u  = g^(1/2) · λ^(5/3) · h^(−7/6) · 2.3^(−5/3)
```

Check the three constants against Alexander's:
- `5/3 = 1.667` → **1.67** ✓
- `1/2 − 5/3 = −7/6 = −1.167` → **−1.17** ✓
- `2.3^(−5/3) = 1/4.008 = 0.2495` → **0.25** ✓

All three fall out. *(This algebra is computed here — MODELED — and you can check it in a minute. The **historical** claim that Alexander derived his constants from that specific dynamic-similarity fit — conventionally credited to Alexander & Jayes 1983, J Zool, DOI 10.1111/j.1469-7998.1983.tb04266.x — is **NOT-SOURCED in this pass**; I did not retrieve either primary text. The equivalence is arithmetic; the attribution is not.)*

The physical content: **animals of different sizes move in dynamically similar ways at equal Froude number.** That is what lets you use living animals to calibrate a dead one.

### Work one

Take a large theropod trackway. *Inputs stated as illustrative:*
- footprint length `FL = 0.60 m` → `h = 4 × 0.60 =` **2.40 m**
- stride length `λ =` **3.50 m**

```
g^0.5     = 3.132
λ^1.67    = 3.50^1.67  = 8.103
h^−1.17   = 2.40^−1.17 = 0.3590

u = 0.25 × 3.132 × 8.103 × 0.3590 = 2.28 m/s
```

**`u ≈ 2.28 m·s⁻¹ ≈ 8.2 km/h`** — a brisk walk. Not a chase. Now cross-check with two independent diagnostics:

- **Relative stride length:** `λ/h = 3.50/2.40 = 1.46`. Below the conventional walking threshold of ~2.0.
- **Froude number:** `Fr = u²/(gh) = 5.19/23.54 = 0.22`. Below the ~0.5 walk/run region.

Both say *walking*. They agree because they are the same equation wearing different clothes — which is a consistency check, not independent confirmation. Say so.

### Now break it

Here is why this chapter respects Alexander's equation: **it is falsifiable, and it has been partly falsified.**

Prescott et al. (2025), *Biology Letters*, DOI 10.1098/rsbl.2025.0191, used "high-speed video recordings of two helmeted guineafowl (*Numida meleagris*) traversing mud of varying consistency across 20 trials," measured their real speeds, then applied Alexander's equation to the tracks they left. **That is n=2 individuals of one species on one substrate class** — carry that number through everything below, because it bounds the whole result:

| | Measured (video) | Calculated (Alexander) |
|---|---|---|
| Range | **0.04–0.97 m·s⁻¹** | **0.17–1.84 m·s⁻¹** |
| Mean | **0.29 m·s⁻¹** | **0.61 m·s⁻¹** |

**"Calculated speed ranged from 1.17 to 4.74× measured speed."** The equation **overestimated, systematically**, worst at slow speeds. Their conclusion: trackway speed estimates are "inaccurate, if not outright misleading" for animals moving freely over compliant substrate.

**Now carry their caveats, or you overstate the negative into a fabrication of the opposite sign.** The authors ask for exactly what they do not have: "far more extensive studies need to be carried out across a range of body sizes, grain sizes and foot morphologies to enable more confident reconstructions." And they name the boundary of their own result: "it is possible that trackways formed in coarser sediments, such as sand, fit Alexander's formula more closely as the 'pull effect' would be less pronounced." So this is a **real hit on the method, on mud, for two small birds** — not a general refutation, and this chapter does not get to spend it as one. Inflating a negative is the same defect as inflating a positive; it just flatters a different prior.

And the weak link is exactly where you would predict — `h`. Alexander's `4 × track length` rule gave **26 cm**; the skeletal hip height was **25.8 cm** (a near-perfect hit); but the **functional mid-stance hip height was 18–20 cm**. The rule predicts the *anatomy* well and the *mechanically relevant quantity* badly, because a bird walks with a crouched limb. Feed `h` too large into `h^(−1.17)` and the error propagates with an exponent on it. Mud also inflates `λ`.

**This is the good outcome.** A method that could not be tested against living animals would be a story. This one was tested, and it moved. Alexander's own estimates — reported as roughly **1.0–3.6 m·s⁻¹** *(fence: via abstract summary; the 1976 primary was not retrieved in this pass)* — should now be read as **upper bounds on soft ground**, not speeds.

## Respiration: a hypothesis that predicted where the holes would be

Birds do not breathe like us. Air moves **unidirectionally** through a rigid flow-through lung, driven by a system of **air sacs** acting as bellows. The air sacs send out diverticula that **invade bone** and hollow it — postcranial skeletal pneumaticity.

That gives a hypothesis a **hard, checkable, spatially specific prediction**: *if* non-avian dinosaurs had this system, their bones should be hollow **in the particular places** the diverticula reach, with the foramina and internal chambers to show it — not hollow generally, not hollow wherever convenient.

The bones are hollow in the predicted places.

- **O'Connor & Claessens (2005)**, *Nature* 436(7048):253–256, DOI 10.1038/nature03716, reconstructed the respiratory system of an exceptional *Majungatholus atopus* specimen and found air sacs plus a thoracic skeleton consistent with flow-through ventilation.
- **Wedel (2003)**, *Paleobiology* 29(2):243–255, read sauropod vertebral laminae, fossae and internal chambers as osteological correlates of bird-style diverticula — and noted the **sequence** matches: in birds, cervical air sacs pneumatise cervical and anterior thoracic vertebrae, abdominal air sacs pneumatise posterior thoracic vertebrae and synsacrum later in ontogeny; sauropod *evolution* parallels that bird *ontogeny*.

**Why this is strong:** the prediction was risky. The bones could have been solid. They could have been hollow in the wrong places. They were not. That is a hypothesis paying rent.

## Thermal: carry the disagreement, don't resolve it

**Gigantothermy** is the null hypothesis you must beat before invoking endothermy. Surface-to-volume falls as `3/R` (cross-ref NA-05): a big animal exchanges heat with the world slowly, so bulk alone buys thermal stability. Paladino, O'Connor & Spotila (1990), *Nature* 344:858–860, coined it from leatherback turtles — >900 kg animals holding ~25–30 °C cores in ~7 °C water on reptile-grade metabolism. *(Fence: leatherback figures via secondary summary in this pass.)*

Then the measurements arrived, and they did not settle it.

- **Eagle et al. (2011)**, *Science* 333(6041):443–445, DOI 10.1126/science.1206196, used clumped-isotope (¹³C–¹⁸O ordering) thermometry on large Jurassic sauropod teeth: **36–38 °C**, mammal-like. But note what else they report — that is **4–7 °C *lower*** than a body-temperature-scales-with-mass model predicted. **A model made a prediction and the measurement came in under it.** That is a falsification event, and it implies sauropods had some means of *shedding* heat.
- **LAGs.** Lines of arrested growth — dark rings in bone section — were long read as an ectotherm signature. **Köhler et al. (2012)**, *Nature* 487:358–361, DOI 10.1038/nature11264, found cyclical growth to be a universal trait of homoeothermic endotherms in a global survey of wild ruminants. **LAGs are therefore no longer evidence of ectothermy.** An argument died; the underlying observation survived.
- **Wiemann et al. (2022)**, *Nature* 606:522–526, DOI 10.1038/s41586-022-04770-6, used Raman/FTIR to quantify metabolic lipoxidation signals in bone and inferred high metabolic rates across ornithischians, sauropods, theropods and pterosaurs — endothermy ancestral to Ornithodira.
- **And it was immediately contested.** **Motani, Gold, Carlson & Vermeij (2023)**, "Amniote metabolism and the evolution of endothermy," *Nature* 621(7977):E1–E3 — a **Matters Arising** comment, not a research paper — DOI 10.1038/s41586-023-06411-y, argue the uncertainty is too large to support the ancestral inference (**a single relative-intensity value may correspond to metabolic rates differing fivefold**) and note the near-absence of calibration for gigantothermic mesotherms. **Wiemann et al. replied**: *Nature* 621:E4–E6 (2023), DOI 10.1038/s41586-023-06412-x. *(An earlier draft rendered this as "*Nature* (2023) argues" — a journal cannot argue. Four named people did, and this chapter names authors for every other citation in it. Rendering a signed comment as an institutional verdict inflates the weight of the contest and makes it harder to check — and it would be inflating a contest this chapter is otherwise right to carry.)* *(**Fence:** the fivefold-uncertainty figure and the mesotherm-calibration claim are **NOT-VERIFIED against the primary in this pass** — paywalled on two attempts. Carried as the commenters' stated position, not as a checked number.)*

**State of play: OBSERVED-CONTESTED.** Not "dinosaurs were warm-blooded." The honest sentence is: *multiple independent lines indicate metabolic rates and body temperatures well above modern ectotherms in at least some dinosaur lineages, the ancestral reconstruction is disputed on measurement-uncertainty grounds, and the dispute is live.* Anyone who gives you a clean answer here is selling something.

## Necks: do the arithmetic and look at what it costs

Sauropod necks are the most extreme cantilever any land animal has built, and they create a problem that is pure hydrostatics.

**The measurements.** Moore et al. (2023), *J Syst Palaeontol* 21(1), DOI 10.1080/14772019.2023.2171818, infer a neck of **~15.1 m** for *Mamenchisaurus sinocanadorum* — the longest confidently inferable for any sauropod, **>6× a giraffe's**. Taylor & Wedel (2013), *PeerJ* 1:e36, DOI 10.7717/peerj.36, give *Supersaurus* ~15 m and a world-record bull giraffe at **2.4 m**. *(Note the honest drift: Taylor & Wedel 2013 put* M. sinocanadorum *at ~12 m; the 2023 reanalysis moved it to ~15.1 m. Estimates move. Print the date.)*

**How it was affordable.** Not muscle — **subtraction**. Sauropods used bird-style pneumaticity to hollow the neck out. Air space proportion (ASP) runs around **50–60%** in adult neosauropod cervicals, **up to 79%** in the largest (*Sauroposeidon*) — **Wedel 2005, as reported by Schwarz-Wings et al. (2009)**, *Proc R Soc B* 277(1678):11–17, DOI 10.1098/rspb.2009.1275. *(Attribute the measurement to whoever made it. Schwarz-Wings et al. cite these figures to Wedel — verbatim: "in an adult neosauropod is around 50–60%, but could range up to 79 per cent in the largest neosauropods like* Sauroposeidon *(… Wedel 2005)". They are a finite-element study of two vertebrae; they measured no* Sauroposeidon *and generated no ASP data. An earlier draft named them as the source — the same laundering this chapter avoids one screen up with "Carrano, as reported by Kilbourne & Makovicky".)* What Schwarz-Wings et al. **did** contribute is an FEA of **exactly two vertebrae** — an undetermined diplodocid mid-cervical and *Brachiosaurus* C3 — finding "the interior of both vertebrae is nearly stress free," i.e. **bone was removed exactly where it was doing no work.** Taylor & Wedel (2013) give ASP 0.50–0.70 and specific gravities as low as **0.2**, against compact bone at **1.8–2.0**. Sauropods also had **13–17 cervicals** (19 in *M. hochuanensis*) and no chewing apparatus to carry at the far end — where mammals are stuck at **exactly seven** cervicals (sloths and sirenians excepted).

**Now the arithmetic — the part that creates the problem.** Blood is a fluid; a raised head sits on top of a column of it. Take `ρ_blood ≈ 1050 kg·m⁻³`, `g = 9.81 m·s⁻²`:

```
ρg = 1050 × 9.81 = 10,300 Pa per metre
   ÷ 133.322 Pa/mmHg
   = 77.3 mmHg per metre of height
```

**And here is where you do not congratulate yourself.** The tempting move is to "check" this against the ~**77 mmHg per metre** that circulates in the giraffe literature, watch it match, and declare the tool validated. **That check is empty.** `dP/dz = ρg` is a **definition** — hydrostatics, not a finding — and the ~77 mmHg/m in the literature *is* ρg for blood, the same constant wearing a mammal. Reproducing it tests nothing except whether ρ_blood was transcribed correctly. There is no independent measurement here to agree with, and an earlier draft of this section claimed one ("the arithmetic reproduces the measurement. Good — the tool works") on the strength of a figure it never sourced to an author. **The hydrostatics is sound because hydrostatics is sound, not because an animal confirmed it.**

**Now point it at a sauropod.** For a head **9 m** above the heart:

```
9 m × 77.3 mmHg/m = 695 mmHg   (just to hold the column up)
+ ~50 mmHg                      (Seymour's perfusion term — HIS constant, not an independent one)
≈ 745 mmHg
```

Seymour (2009), *Biology Letters* 5(3):317–319, gives **750 mmHg** MAP for that geometry — and gives it by **exactly the construction above**: "the static blood column alone would produce 700 mm Hg at heart level," then "to induce flow, it is reasonable to add perhaps 50 mm Hg, giving a mean systemic arterial blood pressure of 750 mm Hg."

**So say what that agreement is, and is not.** It is not a check on Seymour. It is Seymour's own decomposition, re-run with Seymour's own +50 mmHg perfusion constant, and it therefore carries **zero independent evidential weight**. What it confirms is that this chapter transcribed ρ, `h`, and his term correctly — an arithmetic consistency check on itself. An earlier draft called this "my arithmetic independently lands on his published figure"; the word *independently* was doing work the arithmetic cannot do. **Same fence as the Froude/λ-h agreement above:** the same equation wearing different clothes is a consistency check, not confirmation. The chapter stated that rule sixty lines earlier and then broke it — which is how these get in.

For scale: baseline mammalian MAP is ~100 mmHg; measured giraffe MAP at heart is **185 ± 41.6 mmHg** (Mitchell et al. 2006, *J Exp Biol* 209(13):2515), at head **100.3 ± 20.9 mmHg** (Mitchell & Skinner 1993, via Mitchell et al. 2006).

**And here is the bill.** Seymour reports that producing the **700 mmHg** static column — his figure is stated against 700, not the 750 total; the perfusion term rides on top, and this chapter just spent three lines on that decomposition, so it had better honour it here — needs "a heart weighing 5 per cent of the body weight," with walls **5× thicker and 15× heavier** than expected for a similarly sized animal producing only 100 mmHg. And the circulation would then consume **~49% of the animal's total energy budget**, against ~10% at 100 mmHg. **Half the animal's metabolism, to hold its head up.** His conclusion: it "would probably make more energetic sense for the animal to feed with its neck close to horizontal."

**Carry the competing hypotheses; do not pick a winner:**
1. **High browsing** — the classic; Seymour's cost argument is aimed squarely at it.
2. **Horizontal feeding envelope** (Seymour 2009) — sweep a huge volume at low cardiac cost without walking.
3. **Some sauropods did raise them anyway** — Christian (2010), *Biology Letters* 6(6):823, argues from *Euhelopus zdanskyi* for high browsing. *(Fence: title/venue located; primary not fetched in this pass.)*
4. **Sexual selection / mate attraction** — named among candidate pressures by Taylor & Wedel (2013).

**An honest loose end — and the source closes most of it.** Take the two giraffe means at face value: 185 − 100.3 = 84.7 mmHg ÷ 77.3 mmHg/m implies only **~1.1 m** of column — shorter than a standing giraffe's head-above-heart height. Mitchell et al. (2006) — *the same paper both pressures came off* — hit this discrepancy themselves and answer it on the page. Their model predicted ~255 mmHg at the heart against 185 ± 41.6 measured, and they write: "this lower than predicted average pressure may be because some of the animals were anaesthetized at the time of measurement, or were holding their heads at an average angle less than vertical, or did not have two meter long necks, but it is also possible that mechanisms exist that reduce the work of the heart."

**Three of those four are exactly the posture/individual/anaesthesia confounds; the fourth is a live physiological hypothesis.** So the gap is **explained but not closed**: the residual — whether a real work-reducing mechanism exists — stays open, and it is *the authors' own* open question, not a hole in this chapter's sourcing. An earlier draft fenced this whole item **NOT-MEASURED** for want of "the primary texts," which was false: the text was in hand, quoted twice, two paragraphs up. **NOT-MEASURED is for what cannot be sourced, not for what was not read** — using it as a substitute for turning the page is the same defect as a sourceless claim, wearing a modest hat. I am printing the discrepancy rather than quietly averaging it away, because the arithmetic that produced 745 mmHg is the same arithmetic that throws this up, and you do not get to keep only the flattering half.

## Birds are dinosaurs: the recipe never stopped running

Stated plainly, as phylogeny and not as a flourish: **birds are maniraptoran theropod dinosaurs.** Not descendants-of. Not like. *Are* — the same way a bat is a mammal. Non-avian dinosaurs ended at the K–Pg boundary; **Dinosauria did not.** There are dinosaurs outside your window.

The receipts, and note that they include **a refuted objection**, which is worth more than a confirmation:

- **The furcula — the objection that died.** Heilmann's influential 1926 book treated the apparent absence of clavicles/furculae in dinosaurs as powerful evidence *barring* them from bird ancestry. **Norell, Makovicky & Clark (1997)**, *Nature* 389:447, DOI 10.1038/38918, reported a furcula in Dromaeosauridae — the group closest to birds. The prediction implied by the bird-dinosaur hypothesis was that the wishbone would turn up. It turned up. *(Honest residue: furculae are absent in some other theropods, and whether that absence is real or a preservation artefact remains unresolved — so the element's evolutionary history is still partly open.)*
- **Feathers on a non-avialan dinosaur.** *Sinosauropteryx*, described 1996, Yixian Formation, Liaoning — **Chen, Dong & Zhen (1998)**, *Nature* 391:147–152 — the first dinosaur taxon outside Avialae found with feather evidence. **Swisher et al. (1999)**, *Nature* 400:58, dated the beds.
- **Feathers older than the "first bird."** *Anchiornis huxleyi*, Late Jurassic, **>160 Ma** — fully feathered wings, at least ~10 Myr **before** *Archaeopteryx*. Feathers predate birds; they are not a flight invention.
- **Feather-like structures in an ornithischian.** *Kulindadromeus zabaikalicus* — on the *other* major branch of Dinosauria, which pushes the trait's origin deeper still.
- **The transitional fossil.** *Archaeopteryx* carries wishbone, flight feathers, wings and a partially reversed first toe alongside plainly dinosaurian characters — Huxley saw it in 1868; Ostrom made the modern case in the 1970s.

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `σ ∝ L` | stress grows linearly with length | — | geometric scaling of any solid | MODELED | Galileo 1638, *Discorsi* (Two New Sciences); arithmetic shown above | A geometrically scaled structure whose bone stress does not rise with `L` |
| `b_geom` | 1.0 | dimensionless | predicted length-vs-circumference exponent, geometric similarity | MODELED | Kilbourne & Makovicky 2010, *J Anat*, Table 8 | Derivation error |
| `b_elastic` | 0.67 | dimensionless | elastic similarity (`L ∝ D^(2/3)`); attributed to McMahon 1975a | MODELED | Kilbourne & Makovicky 2010, Table 8 | Derivation error |
| `b_stress` | 0.5 | dimensionless | static stress similarity | MODELED | Kilbourne & Makovicky 2010, Table 8 | Derivation error |
| `b_fem,Trex` | **0.5341** — **95% CI 0.04159–0.9718** | dimensionless | *T. rex*, femur, **ontogenetic**, RMA log L vs log C — **CI contains static-stress (0.5), elastic (0.67) and nears geometric (1.0): discriminates among NONE; carries no contrast with any other taxon** | OBSERVED-SINGLE *(one growth series, one study; CI spans the model space — **downgraded from OBSERVED-REPLICATED**)* | Kilbourne & Makovicky 2010, *J Anat*, Table 3 | Re-measure the growth series; RMA slope or CI outside the **published** 0.04159–0.9718 *(the earlier falsifier "~0.5 ± 0.1" was invented — ~4.6× tighter than the real CI, i.e. unfalsifiable-as-written against the actual data)* |
| `b_fem,Allo` | **0.82** | dimensionless | *Allosaurus fragilis*, femur, ontogenetic | OBSERVED-REPLICATED | Kilbourne & Makovicky 2010 | As above |
| `b_fem,sauropodomorph` | **~1.0** (*Massospondylus* 0.81) | dimensionless | sauropodomorphs, femur, ontogenetic | OBSERVED-REPLICATED | Kilbourne & Makovicky 2010 | As above |
| `b_fem,hadrosaur` | **1.05** (*Maiasaura*); **1.094** (*Hypacrosaurus*, **95% CI 1.072–1.113**) | dimensionless | hadrosaurids, femur, ontogenetic — **tight CI excludes every standard model from below; this is the section's real signal, and it stands alone without the *T. rex* row** | OBSERVED-REPLICATED | Kilbourne & Makovicky 2010, Table 3 | Re-measure; slope or CI overlapping 1.0 |
| `b_fem,interspecific` | **0.83** (tibia **0.78**; MT III **0.80**) | dimensionless | **interspecific**, non-avian dinosaurs — **do not conflate with ontogenetic** | OBSERVED-REPLICATED | Carrano, as reported by Kilbourne & Makovicky 2010 — verbatim: "femoral exponent, 0.83; tibial exponent, 0.78; metatarsal III exponent, 0.80" | Fetch Carrano primary; femoral exponent outside ~0.83 ± 0.05 |
| `M_adult,Trex,published` | **6,000–8,000**; "Sue" perhaps **~9,500** | kg | adult *T. rex* — **the authors' own stated conclusion**, verbatim: "adult *T. rex* had body masses around 6000–8000 kg, with the largest known specimen ('Sue') perhaps ∼9500 kg" | OBSERVED-CONTESTED | Hutchinson et al. 2011, *PLoS ONE* 6(10):e26037, abstract | An independent volumetric study concluding outside this band |
| `M_Trex,PersonsCurrie` | **3,800–4,500** | kg | mass range **assumed as an INPUT for the genus *Tyrannosaurus*** by Persons & Currie — **not an estimate of PR2081**, not a scaling-equation output for any specimen, and **not admissible as the low end of Sue's envelope** | OBSERVED-CONTESTED | reported (and treated as too small) by Hutchinson et al. 2011, *PLoS ONE* 6(10):e26037 — verbatim: "Persons and Currie used smaller body mass estimates (3800–4500 kg) for *Tyrannosaurus*" | Fetch Persons & Currie; establish what the range was derived from and at what scope |
| `M(PR2081)_min` | **9,502** | kg | *T. rex* "Sue", volumetric **minimal** model — authors' preferred region | OBSERVED-CONTESTED | Hutchinson et al. 2011, *PLoS ONE* 6(10):e26037, Table 6 | Independent volumetric reconstruction outside ~8,000–11,000 kg |
| `M(PR2081)_max` | **18,489** | kg | *T. rex* "Sue", volumetric **maximal** model — authors judge "less plausible" | OBSERVED-CONTESTED | Hutchinson et al. 2011, Table 6 | As above |
| `M(PR2081)_spread` | **~1.95×** (9,502 → 18,489) | dimensionless | **minimal-to-maximal envelope; same specimen, same study, same bones** — **this is the headline** *(corrected: an earlier draft printed ~4.9× by taking Persons & Currie's genus-level input assumption as Sue's low end — a scope error, see the row above)* | MODELED | Computed here from the two rows above | Arithmetic error |
| `M_adults_Trex` | **minimal models 5,777–9,502**; **maximal models 10,768–18,489** | kg | four adult *T. rex*, **min/max per specimen**: CM 9380 = 7,394/14,564; FMNH PR2081 = 9,502/18,489; BHI 3033 = 5,934/10,837; MOR 555 = 5,777/10,768 *(the envelope belongs to the specimen — read Table 6 down its columns, not across its rows)* | OBSERVED-CONTESTED | Hutchinson et al. 2011, Table 6 | Independent volumetric reconstruction of any listed specimen outside its stated pair |
| C&E-2012 coefficients | — | — | Campione & Evans 2012 regression constants + PPE | **NOT-SOURCED** | *BMC Biology* 10:60, DOI 10.1186/1741-7007-10-60 — **primary text not retrievable in this pass** | Open the primary; print the coefficients |
| `u` (Alexander) | `0.25·g^0.5·λ^1.67·h^−1.17` | m·s⁻¹ | bipedal trackway speed | MODELED | Alexander 1976, *Nature* 261:129–130; equation as reproduced verbatim by Prescott et al. 2025 | See the Prescott row |
| `h` from track | `h ≈ 4 × footprint length` | m | Alexander's hip-height rule — **the weak link** | MODELED | Alexander 1976 | See the Prescott row |
| `u_example` | **2.28** (≈8.2 km/h) | m·s⁻¹ | `FL=0.60 m → h=2.40 m`, `λ=3.50 m` — **illustrative inputs, not a real trackway** | MODELED | Computed here | Arithmetic error |
| `λ/h_example` | **1.46** | dimensionless | same; <2.0 conventional walking threshold | MODELED | Computed here; thresholds via secondary summary | Threshold convention refuted |
| `Fr_example` | **0.22** | dimensionless | `Fr = u²/(gh)`, **convention stated** | MODELED | Computed here | Arithmetic error |
| Alexander↔Froude identity | `0.25·g^0.5·λ^1.67·h^−1.17` ⟺ `λ/h = 2.3·Fr^0.3` | — | `5/3=1.67`; `1/2−5/3=−1.17`; `2.3^(−5/3)=0.2495≈0.25` | MODELED | **Algebra computed here** — checkable in a minute | Redo the algebra |
| — *its attribution* | — | — | that Alexander's constants came from Alexander & Jayes' fit | **NOT-SOURCED** | Alexander & Jayes 1983, *J Zool*, DOI 10.1111/j.1469-7998.1983.tb04266.x — not retrieved | Open either primary |
| `u_measured,guineafowl` | **0.04–0.97** (mean 0.29) | m·s⁻¹ | **two helmeted guineafowl (*Numida meleagris*), n=2 individuals, 20 trials**, mud of varying consistency, high-speed video + photogrammetry | OBSERVED-SINGLE *(single study, n=2, one species — **downgraded from OBSERVED-REPLICATED**; n=2 is not "replicated" and "extant birds" was class inflation)* | Prescott et al. 2025, *Biol Lett*, DOI 10.1098/rsbl.2025.0191 | Repeat across other taxa, body sizes, grain sizes and foot morphologies — **the authors' own request** |
| `u_calc,guineafowl` | **0.17–1.84** (mean 0.61) | m·s⁻¹ | Alexander's equation on the **same two birds'** tracks | OBSERVED-SINGLE *(single study, n=2, one species)* | Prescott et al. 2025 | As above |
| **`u_calc/u_meas`** | **1.17–4.74×** | dimensionless | **systematic overestimate; worst at slow speed** — **on mud, n=2 guineafowl only**; authors allow coarser sediment (sand) "fit Alexander's formula more closely as the 'pull effect' would be less pronounced" | OBSERVED-SINGLE *(single study, n=2, one species)* | Prescott et al. 2025 | A trial recovering ratio ≈1.0 on compliant substrate; **or a sand trial fitting Alexander**, which the authors flag as possible |
| `h` error source | 4×track = **26 cm**; skeletal = **25.8 cm**; **functional mid-stance = 18–20 cm** | cm | **same two guineafowl**; the rule predicts anatomy well, mechanics badly | OBSERVED-SINGLE *(single study, n=2, one species)* | Prescott et al. 2025 | Show functional ≈ skeletal hip height in a walking biped |
| `u_Alexander,1976` | **~1.0–3.6** | m·s⁻¹ | Alexander's original dinosaur estimates | OBSERVED-CONTESTED *(via abstract summary; primary not retrieved)* | Alexander 1976 | Open the primary; re-read as upper bounds per Prescott et al. 2025 |
| Flow-through lung | air sacs + thoracic skeleton consistent with unidirectional flow | — | *Majungatholus atopus*, exceptional specimen | OBSERVED-REPLICATED | O'Connor & Claessens 2005, *Nature* 436(7048):253–256, DOI 10.1038/nature03716 | A theropod with the diagnostic foramina but no air-sac-consistent thorax |
| Pneumatic correlates | vertebral laminae/fossae/chambers = diverticula of cervical & abdominal air sacs | — | sauropods; bird ontogeny ↔ sauropod evolution parallel | OBSERVED-REPLICATED | Wedel 2003, *Paleobiology* 29(2):243–255 | Bones hollow in **non**-predicted places, or solid in predicted ones |
| `ASP` | **~50–60%**, up to **79%** (*Sauroposeidon*) | % vertebral volume as air | adult neosauropod cervicals | OBSERVED-REPLICATED | **Wedel 2005, as reported by** Schwarz-Wings et al. 2009, *Proc R Soc B* 277(1678):11–17, DOI 10.1098/rspb.2009.1275 *(they cite it to Wedel; they measured no *Sauroposeidon* and generated no ASP data — **do not name the quoter as the source**)* | Re-measure **Wedel's CT dataset**; ASP outside range |
| `ASP` (2nd) | **0.50–0.70**; specific gravity to **0.2** (vs compact bone **1.8–2.0**) | dimensionless | sauropod cervicals | OBSERVED-REPLICATED | Taylor & Wedel 2013, *PeerJ* 1:e36, DOI 10.7717/peerj.36 | As above |
| Stress field | vertebral interior "nearly stress free"; bone resorbed where unloaded | — | FEA of **exactly two vertebrae**: undetermined diplodocid mid-cervical; *Brachiosaurus* C3 — **this, and only this, is Schwarz-Wings et al.'s own contribution** | MODELED | Schwarz-Wings et al. 2009 | FEA showing high interior stress |
| `T_body,sauropod` | **36–38** | °C | large Jurassic sauropod teeth, clumped-isotope (¹³C–¹⁸O) | OBSERVED-REPLICATED | Eagle et al. 2011, *Science* 333(6041):443–445, DOI 10.1126/science.1206196 | Independent thermometry outside range |
| `ΔT_model` | **4–7 °C lower than predicted** | °C | measured vs mass-scaling body-temperature model — **model partly falsified** | OBSERVED-REPLICATED | Eagle et al. 2011 | Re-run the scaling model |
| LAGs | **cyclical growth is universal in homoeothermic endotherms** | — | global survey, wild ruminants | OBSERVED-REPLICATED | Köhler et al. 2012, *Nature* 487:358–361, DOI 10.1038/nature11264 | An endotherm survey finding no LAGs |
| Dinosaur metabolic rates | high; endothermy inferred ancestral to Ornithodira | — | Raman/FTIR lipoxidation signals in bone | **OBSERVED-CONTESTED** | Wiemann et al. 2022, *Nature* 606:522–526, DOI 10.1038/s41586-022-04770-6 | See the contest row |
| — *the contest* | **one intensity value ↔ metabolic rates differing ~5×**; ancestral inference unsupported | — | **Matters Arising** comment; calibration gap for gigantothermic mesotherms — **both numbers NOT-VERIFIED against the primary (paywalled, 2 attempts); carried as the commenters' stated position** | **OBSERVED-CONTESTED** | **Motani, Gold, Carlson & Vermeij 2023**, *Nature* 621(7977):E1–E3 (Matters Arising), DOI 10.1038/s41586-023-06411-y; reply **Wiemann et al. 2023**, *Nature* 621:E4–E6, DOI 10.1038/s41586-023-06412-x | A calibration collapsing the 5× band — **and, first: open the primary and check the 5× figure itself** |
| Gigantothermy | leatherback >900 kg holds ~25–30 °C core in ~7 °C water | kg, °C | *Dermochelys coriacea* | OBSERVED-REPLICATED *(figures via secondary summary in this pass)* | Paladino, O'Connor & Spotila 1990, *Nature* 344:858–860 | Open the primary; re-measure core temp |
| `L_neck,max` | **~15.1** | m | *Mamenchisaurus sinocanadorum*; >6× giraffe | OBSERVED-CONTESTED | Moore et al. 2023, *J Syst Palaeontol* 21(1), DOI 10.1080/14772019.2023.2171818 | New cervical material; **note 2013 estimate was ~12 m** |
| `L_neck,Supersaurus` | **~15** | m | *Supersaurus* | OBSERVED-CONTESTED | Taylor & Wedel 2013, *PeerJ* 1:e36 | As above |
| `L_neck,giraffe` | **2.4** | m | world-record bull giraffe | OBSERVED-REPLICATED | Taylor & Wedel 2013 | A longer measured giraffe neck |
| `n_cervical` | sauropods **13–17** (19 in *M. hochuanensis*); mammals **exactly 7** (sloths/sirenians excepted) | count | — | OBSERVED-REPLICATED | Taylor & Wedel 2013 | A mammal outside the exceptions with ≠7 |
| **`dP/dz`** | **77.3** (78.0 at ρ=1060) | mmHg per metre | `ρg`, ρ_blood ≈ 1050 kg·m⁻³, g = 9.81 — **a definition (hydrostatics), not a measurement** | MODELED | **Computed here.** The ~77 mmHg/m quoted in the giraffe literature **is this same `ρg`**, not an independent measurement of it — **no cross-check is claimed** *(an earlier draft claimed one, against an unattributed figure)* | Arithmetic error, or ρ_blood refuted |
| `P_column(9 m)` | **~695** (+~50 perfusion ≈ **745**) | mmHg | 9 m head-above-heart; **the +50 is Seymour's perfusion term, not an independent constant** | MODELED | Computed here | Arithmetic error |
| `MAP_sauropod` | **750** (= **700** static column **+ ~50** perfusion) | mmHg | ~9 m raised head | MODELED | Seymour 2009, *Biol Lett* 5(3):317–319 — **the arithmetic above REPRODUCES his construction using his own +50 term: a consistency check on this chapter's transcription, NOT an independent landing** | Re-derive; a different ρ or geometry |
| `m_heart/M` | **~5%** of body weight; walls **5× thicker, 15× heavier** than an animal producing 100 mmHg | % | **to produce 700 mmHg** — the static column below an upright *Barosaurus* neck — **not the 750 total** | MODELED | Seymour 2009, verbatim: "a heart weighing 5 per cent of the body weight was necessary to produce 700 mm Hg" | Re-run the cardiac model |
| **`f_circ`** | **~49%** of total energy budget (vs **~10%** at 100 mmHg) | % | sauropod circulation at 750 mmHg | MODELED | Seymour 2009 | Re-run the model; a cheaper route to 750 mmHg |
| `MAP_giraffe,heart` | **185 ± 41.6** | mmHg | giraffe, at heart level | OBSERVED-REPLICATED | Mitchell et al. 2006, *J Exp Biol* 209(13):2515 | Independent catheterisation outside range |
| `MAP_giraffe,head` | **100.3 ± 20.9** | mmHg | giraffe, at head | OBSERVED-REPLICATED | Mitchell & Skinner 1993, via Mitchell et al. 2006 | As above |
| giraffe column reconciliation | 84.7 mmHg ÷ 77.3 ⇒ **~1.1 m** — shorter than standing head-above-heart | m | **explained by the source itself**: anaesthesia, head held at "an average angle less than vertical", or necks not 2 m long; **residual open question is the authors' own** — "it is also possible that mechanisms exist that reduce the work of the heart" | OBSERVED-CONTESTED *(explanation stated by the authors; the residual mechanism is untested — **was wrongly fenced NOT-MEASURED against a source already quoted twice in this chapter**)* | Mitchell et al. 2006, *J Exp Biol* 209(13):2515 (verbatim) | Catheterise conscious giraffes of known neck length at known head angle; a residual gap surviving those controls indicts the work-reducing-mechanism hypothesis |
| Birds ∈ Dinosauria | birds are maniraptoran theropods | — | phylogeny | OBSERVED-REPLICATED | Huxley 1868; Ostrom 1970s; Norell et al. 1997; Chen et al. 1998 | A phylogeny placing Aves outside Dinosauria on comparable data |
| Furcula in Dromaeosauridae | present — **refutes Heilmann's 1926 objection** | — | *Velociraptor* | OBSERVED-REPLICATED | Norell, Makovicky & Clark 1997, *Nature* 389:447, DOI 10.1038/38918 | Re-identify the element as non-furcular |
| Feathers pre-Avialae | *Sinosauropteryx* (desc. 1996), Yixian Fm., Liaoning | — | first non-avialan dinosaur with feather evidence | OBSERVED-REPLICATED | Chen, Dong & Zhen 1998, *Nature* 391:147–152; dating Swisher et al. 1999, *Nature* 400:58 | Re-interpret the integument as collagen and have it hold |
| Feathers pre-*Archaeopteryx* | *Anchiornis huxleyi*, **>160 Ma**, ≥10 Myr older | Ma | Late Jurassic | OBSERVED-REPLICATED *(dating via secondary summary in this pass)* | Xu et al.; Moore et al. 2023 context | Redate the Tiaojishan/Haifanggou beds |
| Feathers in Ornithischia | *Kulindadromeus zabaikalicus* — feather-like structures on the other branch | — | — | OBSERVED-CONTESTED | described 2014; primary not fetched in this pass | Re-interpret the structures |

## Falsifier (operable)

This chapter's central structural claim — **that a fossil constrains a falsifiable quantity only through a physical relation that outlived the animal, and that every such estimate must be published as an envelope whose width is itself the result** — is refuted by exhibiting **one dinosaur quantity (mass, speed, temperature, pressure) that is (a) determined to a stated precision, (b) by a method that does not route through a surviving physical constraint or a living calibration animal, and (c) that survives an independent test against an extant organism.** Prescott et al. 2025 is the standing demonstration that the *opposite* keeps happening: the best-known such method, tested against **two live helmeted guineafowl on mud**, overestimated by **1.17–4.74×**. *(And note that demonstration's own scope — n=2, one species, one substrate class, with the authors themselves allowing that sand may fit Alexander better. It is a real hit, not a general refutation. A chapter arguing that scope is everything does not get to quietly widen its own best exhibit into "extant birds", which an earlier draft did.)*

Secondary, row-local: any table row found outside its stated scope moves **that row only**. A refuted `ASP` does not touch the speed section. What *would* move the chapter is a demonstration that a bare, method-free dinosaur number can be made to hold.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **Any dinosaur figure quoted as precise with no method and no error bar.** — **INADMISSIBLE.** "*T. rex* weighed 7 tonnes." "*T. rex* ran at 20 mph." Not wrong — *unevaluable*. **And be precise about where the defect is**, because an earlier draft of this entry was not: the defect in "7 tonnes" is **not the number**. ~7 t sits inside Hutchinson et al. 2011's own published conclusion — "adult *T. rex* had body masses around 6000–8000 kg" — i.e. inside the very paper this chapter leans on. The defect is that **no method and no envelope is named**, so no falsifier exists, so it is not a measurement. *(The earlier draft declared the ~7 t figure NOT-SOURCED because a **different** paper, Campione & Evans 2020, could not be opened — while its own primary source stated the value outright. Declaring a figure unsourceable when your cited primary asserts it is a **sourceless refusal**: the RES IPSAE rule run backwards. It reads as manufactured, and it was.)* **Receipt:** the same specimen (FMNH PR2081) carries a published minimal-to-maximal envelope of **9,502–18,489 kg** from a single study — a **1.95× spread** — so any single unqualified figure is selecting from that range without saying so. This is the chapter's headline inadmissibility.
- **NEGATIVE / the confirmation that wasn't:** Alexander's trackway equation, tested against **two helmeted guineafowl (*Numida meleagris*, n=2, one species) on mud**, **overestimated speed by 1.17–4.74×** (Prescott et al. 2025). Recorded as a **published negative**, first-class — and **scoped**, because the authors themselves call for studies "across a range of body sizes, grain sizes and foot morphologies" and allow that coarser sediment may fit the formula more closely. The method remains the best available and remains worth teaching — *because* it was testable enough to fail. An untestable method could not have earned a negative.
- **NEGATIVE / conflation trap — ontogenetic vs interspecific allometry.** *Maiasaura*'s femoral exponent of **1.05** is how one animal grows. **0.83** is how adult species compare. Quoting one as the other is a category error (Kilbourne & Makovicky 2010 flag exactly this).
- **NEGATIVE / this chapter's own defects, recorded rather than silently patched.** A prior draft committed, and this pass corrected: a **headline scope error** (Persons & Currie's genus-level input assumption of 3,800–4,500 kg read as Sue's low end, inflating the spread 1.95× → 4.9×); a **table misparse** (Hutchinson Table 6 read across rows and diagonally, producing "minimal 5,800–10,800 / maximal 7,400–18,500", neither of which is a minimal or a maximal range); a **suppressed central conclusion** (the source's own 6,000–8,000 kg, whose absence made the spread look wider than the literature is); a **fabricated error bar** (a "~0.5 ± 0.1" falsifier invented for *T. rex* where the published CI is 0.04–0.97, ~4.6× wider); an **altered exponent** (Carrano's femoral 0.83 printed as ~0.80 five times); **class inflation** (n=2 guineafowl as "extant birds", OBSERVED-REPLICATED); **two circular validations** presented as corroboration (ρg "checked" against ρg; Seymour's construction re-run with Seymour's constant and called independent); a **false NOT-MEASURED** (fenced against a source quoted twice in the same section); and **citation laundering** (Wedel's ASP data attributed to the paper that quotes it). **Recorded because the failure mode is the point:** every one of these is the exact defect the chapter names elsewhere in its own voice, and a chapter that prosecutes scope-free numbers while running one as its headline is not a stricter chapter than the ones it criticises — it is the same chapter with better vocabulary. The rules do not exempt the author who wrote them.
- **NEGATIVE / conflation trap — the Froude convention.** `Fr = u²/(gh)` and `Fr = u/√(gh)` differ **by a square**. "Fr = 0.5" in one is "Fr ≈ 0.71" in the other. Every Froude number in this chapter is `u²/(gh)`, stated. A gait threshold quoted without its convention is not a threshold.
- **NEGATIVE / dead argument — LAGs as evidence of ectothermy.** Retired by Köhler et al. 2012: cyclical growth is universal in homoeothermic endotherms. The bone rings are still there; **the inference from them is gone.** Recorded because the argument still circulates.
- **INADMISSIBLE as stated — "dinosaurs were warm-blooded" / "dinosaurs were cold-blooded."** Both are underdetermined by current evidence and neither names what would refute it. The admissible form carries the taxon, the proxy, the number, and the contest (Wiemann et al. 2022 vs **Motani, Gold, Carlson & Vermeij 2023**, DOI 10.1038/s41586-023-06411-y).
- **NOT-SOURCED in this pass — Campione & Evans (2012) regression coefficients and percent prediction error.** The paper is real and cited (*BMC Biology* 10:60, DOI 10.1186/1741-7007-10-60); its **numbers are not printed here because I could not open the primary text.** Search engines offered me candidate coefficients; I declined them — a plausible sourceless number is the worst defect available, and this chapter would be self-refuting if it committed it while arguing against it. **Closure:** fetch the primary and print the equation.
- **NOT-SOURCED in this pass:** the attribution of Alexander's 0.25/1.67/−1.17 to Alexander & Jayes' dynamic-similarity fit (the *algebraic identity* is computed here and stands); Alexander 1976's own speed range (via abstract summary); **the *attribution* of a headline *T. rex* mass figure to Campione & Evans 2020 — note the narrowing: the **value** (~7 t) **is** sourced, to Hutchinson et al. 2011's own 6,000–8,000 kg conclusion; only the attribution to *this review* is unchecked, and an earlier draft wrongly fenced the value itself**; the walking/trotting/running `λ/h` thresholds (2.0 / 2.9); Christian 2010 on *Euhelopus*; *Kulindadromeus* primary; *Anchiornis* dating primary; leatherback figures in Paladino et al. 1990.
- **NOT-VERIFIED in this pass:** Motani et al. 2023's fivefold-uncertainty figure and their gigantothermic-mesotherm calibration claim (primary paywalled on two attempts). Carried as the commenters' stated position, **not refuted, not checked**.
- **RESOLVED in this pass — was wrongly fenced NOT-MEASURED:** the reconciliation of giraffe MAP-at-heart with MAP-at-head (implies ~1.1 m of column). **Mitchell et al. 2006 state the explanation themselves** — anaesthesia, sub-vertical head angle, or necks shorter than 2 m — with a residual hypothesis that heart-work-reducing mechanisms may exist. The earlier fence claimed the primary texts were not retrieved; **both giraffe pressures had already been quoted out of that same paper.** Recorded because **mis-fencing a sourced answer as unsourceable is the same defect as a sourceless claim** — it just looks like modesty instead of overreach, which is why it survived review.

## HONEST FENCE — MODELED

This chapter is fenced **MODELED**. Individual rows carry their own classes — several OBSERVED-REPLICATED (Kilbourne & Makovicky's **hadrosaurid** exponents and Carrano's interspecific ones, Eagle's isotopes, Köhler's ruminants, the pneumaticity correlates), several OBSERVED-CONTESTED (every mass estimate, every metabolic inference, the neck lengths, the giraffe reconciliation), several plain OBSERVED that a prior draft over-classed (**Prescott's trials — n=2 guineafowl, not "extant birds"**; the *T. rex* femoral exponent, whose CI spans the model space), several NOT-SOURCED / NOT-VERIFIED — but the **chapter as an artifact is a chain of models**: it composes measured constants through stated assumptions (`ρ_blood ≈ 1050 kg·m⁻³`; `h ≈ 4×FL`; `Fr = u²/(gh)`; spherical S/V for gigantothermy) to reach conclusions about animals nobody has observed. **The assumptions are the fence.** Change `ρ_blood` to 1060 and `dP/dz` moves 77.3 → 78.0 mmHg/m — immaterial, because the argument turns on *~700 mmHg vs ~100 mmHg*, an order-of-magnitude gap, not on the third digit. But a reader who needs the third digit must state ρ.

Per **Gould & Lewontin (1979), "The Spandrels of San Marco and the Panglossian Paradigm"**: none of the above establishes that any dinosaur feature is an optimum. Pneumatic bone may be a phylogenetic inheritance that happened to enable long necks rather than an adaptation *for* them — the Wedel (2003) parallel between bird ontogeny and sauropod evolution is as readable as developmental constraint as it is as design. Drift, inertia, and frozen accidents produce features that solve nothing. **Nature's authority here is precisely and only this: it already ran the experiment, under real constraints, for ~165 million years, with the failures deleted.** That makes convergence evidence of a constraint-optimum and makes every number above a **hypothesis generator** — never a proof. Per repo rule **M7**, any bio-inspired design taken from this chapter must still beat a **tuned conventional baseline** on a **pre-registered metric**, with a discriminator that collapses the gain, or it is recorded **NEGATIVE**.

## Not claimed

- **Not claimed:** that any dinosaur mass, speed, or body temperature in this chapter is known. Every one is an **envelope produced by a stated method**. The `1.95×` minimal-to-maximal spread on FMNH PR2081 is the honest state of the best-preserved specimen we have — **and a factor of two on the best specimen in existence is a strong enough result that it never needed the inflated 4.9× a prior draft gave it.**
- **Not claimed:** that Alexander's equation is wrong, or that it should be discarded. It is the best available method, it is falsifiable, and it took a hit against live birds. Both halves are the point.
- **Not claimed:** that dinosaurs were endothermic, ectothermic, or mesothermic; or that sauropods did or did not raise their necks. Both evidence bases are **contested**, and both contests are printed rather than resolved — Wiemann et al. vs the 2023 reanalysis; Seymour's cost argument vs Christian's *Euhelopus* argument.
- **Not claimed:** that pneumaticity evolved *in order to* lighten necks. Correlation of pattern with function is not evidence of purpose — see the Gould & Lewontin fence.
- **Not claimed:** that the extinct animals resembled the popular image of them. Anything believed about dinosaur colour, sound, or behaviour that is not tied to a preserved correlate is **unconstrained**, and this chapter asserts none of it.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** Reading Hutchinson et al. 2011 does not make any UNI claim proven, designed, or built. The NATURA vocabulary (OBSERVED-REPLICATED / OBSERVED-CONTESTED / MODELED / HYPOTHESIZED / INADMISSIBLE / NOT-MEASURED) and the UNI ledger vocabulary (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. This chapter contains **zero** UNI claims.
- **QUAESTIO-APERTA:** "full human" and "the next evolution beyond human" appear nowhere in this chapter as a target, milestone, or deliverable. They are permanent open questions. That birds are dinosaurs is a statement about phylogeny; it implies nothing whatsoever about UNI, and nothing here is a construction plan.


<!-- ===== END cookbook/recipes-natura/CN-08-dinosaurs.md ===== -->



<!-- ===== BEGIN cookbook/recipes-natura/CN-09-whales.md ===== -->

# CN-09 — Whales: the upper bound of animal life, and low-frequency information

> **What you are building.** Two instruments from one animal. First, a method for asking *what sets a maximum* when the obvious constraint has been removed — buoyancy deletes the bone-stress ceiling that CN-08 spent a chapter deriving, so the blue whale is a controlled experiment in what limit shows up *next*. Second, a working model of low-frequency sound as a long-baseline information channel, including the units trap that makes most published comparisons of "loudness" wrong. Every number below either carries a source you can check or is written NOT-MEASURED / NOT-CONFIRMED. Nothing here raises any UNI rung — a citation to marine biology is never a UNI gate.

---

## The headline number has never been measured

Start with the fact that disciplines the whole chapter. Motani & Pyenson (2024), *PeerJ* 12:e16978, state it flatly: **"The body mass of the largest blue whale has never been measured."** Not "poorly measured" — never. Every mass you have ever read for a blue whale is one of three things:

1. **A piecemeal weighing, biased low.** Winston (1950) weighed a 27.1 m female in parts at **≥136.4 tons** — "at least", because blood and fluid are lost in butchering.
2. **A length→mass regression.** Motani & Pyenson compute a 33 m blue whale at **234 t (95% CI 187–294)**, and correcting for fluid loss give **two conditional estimates, each with its own interval**: **252 t (95% CI 201–306)** correcting for **7% blood loss**, and **272 t (95% CI 217–342)** correcting for **14%**. Note the CI width: the upper bound is nearly double the lower. *(The two are not merged here. "252–272 t (CI 201–342)" is a **hull of two intervals** — a CI no analysis in the paper produced — and it drops the blood-loss assumption that generates each. Collapsing two conditional estimates into one unconditioned interval is the exact error this section exists to teach against.)*
3. **A volumetric model.** Their 3D reconstruction gives **266–279 t**, overlapping the regression CI.

The longest reliably measured blue whale was a **33.26 m** female (Risting 1928). The famous "190 tonne" figure is a whaling record and is *not* the largest possible; it is one animal, weighed under industrial conditions, and it is not what the regressions predict for the longest animals.

**This is the lesson before any biology:** the most-cited number about the largest animal that has ever lived is an *extrapolation*, and its honest form is an interval, not a point. CN-08's rule holds here exactly — the spread is the result.

**The title claim was contested and the challenge failed.** Bianucci et al. (2023) described *Perucetus colossus*, an extinct basilosaurid, at **85–340 t**, raising the possibility it outweighed a blue whale. Motani & Pyenson (2024) re-derived it: most likely **60–70 t** (at 17 m), maximum **98–114 t** (at 20 m), concluding that *Perucetus* "did not exceed the body mass of today's blue whales." Record this as a live example of the method working in public: an extraordinary claim, a stated method, a re-analysis, a retraction of the extreme. The blue whale keeps the record — for now, and by argument, not by decree.

*(Cavity fence, per **M22**: the 85–340 t figure reached this chapter **through Motani & Pyenson's account of it**, not from reading Bianucci et al. 2023. It is therefore reported as one side of a dispute *as characterised by the other side* — which is exactly the position from which a number should not be trusted. Closure: fetch Bianucci et al. 2023 and read the mass estimation directly.)*

## Buoyancy removes one ceiling. It does not remove *the* ceiling.

CN-08's constraint is square–cube: bone cross-sectional area grows as `L²`, weight as `L³`, so stress on the skeleton climbs as `L`. Immersion cancels the load — a neutrally buoyant animal's skeleton is not carrying it. So the land ceiling is gone. **What appears in its place?**

Three candidate limits. Only one currently has a direct measurement behind it.

**Candidate 1 — foraging energetics (the strongest result).** Goldbogen et al. (2019), *Science* 366(6471):1367–1372, tagged whales across the size spectrum from harbour porpoise to blue whale and computed **energetic efficiency (EE) = energy from captured prey ÷ energy expended** (including diving costs and post-dive recovery). The result is a *divergence*, and the divergence is the finding:

- In **toothed whales** (single-prey feeders), **EE falls as body size rises.** Bigger odontocetes do eat bigger prey — but "not disproportionally larger". The energy gained per dive fails to cover the rising cost of being large and diving deep.
- In **rorquals** (lunge filter feeders on krill), **EE rises with body size.** Each lunge by the largest rorquals engulfs a krill patch whose integrated energy content exceeds the largest toothed-whale prey **by at least an order of magnitude**, engulfing a volume calculated at **100–160% of the whale's own body volume**.
- **Balaenids** (bowhead, right whales — continuous-ram filter feeders on copepods) show **lower EE than rorquals of similar size.** Filter feeding alone is not the trick; filter feeding *on dense patches* is.

The scaling held across simulated metabolic rates from `MR ∝ M⁰·⁴⁵` to `M⁰·⁷⁵` — i.e. the conclusion does not depend on picking a favourable metabolic exponent, which is the ablation that matters. Their conclusion: **"Maximum size in filter feeders is likely constrained by prey availability across space and time."** Not by bone. Not by heat. By whether the krill is there.

**Candidate 2 — cardiac limits.** Goldbogen et al. (2019), *PNAS* 116(50):25329–25332, put an ECG tag on **one** blue whale (8.5-hour record). Dive heart rates were **4–8 bpm, minimum 2 bpm** — *below* the allometrically predicted resting rate of **15 bpm** for a 70,000 kg animal. Surface rates hit **25–37 bpm**, which they place near the maximum possible, and they suggest this "may have limited the evolution of maximum body size."

**Carry the tension, do not resolve it.** These two papers share a first author and a year. The *Science* paper says size "does not seem to be limited by physiology... but rather is limited by prey availability." The *PNAS* paper says cardiac physiology may be the limit. Both are in the table below, tagged OBSERVED-CONTESTED, because that is what they are. n=1 for the heart.

**Candidate 3 — thermal.** NOT-MEASURED in this pass. A large endotherm in cold water is the *easy* thermal case (surface-to-volume falls as `3/R`; cf. CN-08's gigantothermy). No sourced figure identifies heat as the binding constraint on cetacean size, and none is invented here.

## The honest kicker: the biggest animal eats some of the smallest

Here is the part that inverts the intuition. Baleen filter feeding is a **low-trophic-level** strategy. The blue whale is not the apex of a food chain; it *short-circuits* one.

The arithmetic is energy flow. Pauly & Christensen (1995), *Nature* 374:255–257, computed the primary production required to sustain global fisheries using **a mean trophic transfer efficiency of 10% — and their phrasing is load-bearing: "a value that was re-estimated rather than assumed"**, derived from **48 published trophic models** spanning six aquatic ecosystem types, with fractional trophic levels from 1.0 (edible algae) to 4.2 (tunas).

Ten percent per rung. Every trophic level up costs you an order of magnitude. A predator at level 4.2 lives on roughly `10⁻³·²` of the primary production that a grazer at level 2 can reach. **Krill sit near the bottom.** Eating them directly, in bulk, is the difference between a landscape that can support a 200-tonne animal and one that cannot.

This is why the ocean can afford a blue whale and the land cannot — and the reason is *not* buoyancy. It is that no terrestrial habitat presents a **dense, mobile, low-trophic-level patch that a large animal can engulf whole**. Grass is low-trophic and abundant but it does not aggregate into a bolus you can swallow in one gulp at 100–160% of your body volume; it must be cropped, chewed, and fermented, which is a rate-limited process. The ocean's krill swarms are a *pre-concentrated* low-trophic resource. Goldbogen et al. call filter feeding "an evolutionary pathway to extremes in body size that are not available to lineages that must feed on one prey at a time."

*(Fence: the land-versus-sea contrast in the preceding paragraph is this chapter's synthesis from the Goldbogen and Pauly & Christensen results. It is MODELED reasoning, not a sourced comparative measurement, and it is in the table as such.)*

## Dive physiology: the solution to a gas problem was to remove the gas

**Myoglobin.** Noren & Williams (2000), *Comp Biochem Physiol A* 126(2):181–191, measured skeletal-muscle myoglobin across cetaceans spanning **70 to 80,000 kg**: **1.81–5.78 g Mb per 100 g wet muscle**. Arregui et al. (2021), *Animals* 11(2):451, measured up to **~6.3 g·100 g⁻¹** in striped dolphin epaxial muscle, and found locomotor muscles carry **92.8%** of total muscle O₂ stores. Against this, non-diving mammals run **below ~0.5 g·100 g⁻¹**; the comparative literature attributes a **10–30×** diver-to-non-diver ratio to Kooyman (1989) — *fence: the Kooyman primary was not read in this pass, and an exact human skeletal-muscle value is NOT-MEASURED here.* Myoglobin content and body mass together explain **50%** of variance in cetacean dive performance, and **83%** in odontocetes alone.

Mirceta et al. (2013), *Science* 340(6138):1234192, supply the mechanism, and it is a beautiful one: you cannot simply make more myoglobin, because concentrated protein precipitates. Ancestral sequence reconstruction across a **130-species** phylogeny reveals **elevated myoglobin net surface charge** in divers — like charges repel, so the molecules stay in solution at concentrations that would otherwise aggregate. The constraint on oxygen storage was never "how much Mb can I express"; it was colloid chemistry, and evolution solved it electrostatically.

**Bradycardia.** 2–8 bpm on a dive (Goldbogen et al. 2019 *PNAS*, above). Slowing the pump rations the store.

**Lung collapse — and the number people flatten.** Ridgway & Howard (1979), *Science* 206(4423):1182–1183, inferred from intramuscular nitrogen washout in *Tursiops truncatus* a **lung collapse depth of about 70 m**, after which gas exchange stops and nitrogen loading ceases. That is the canonical figure. But Moore et al. (2011), *J Exp Biol* 214:2390–2397, **imaged** compression directly by hyperbaric CT and **extrapolated** collapse depth to zero gas volume, getting different, larger numbers: the reported range runs from **58 m** (grey seal, lungs at **50% TLC**) to **133 m** (harbour porpoise, **100% TLC**). Every one of those numbers carries a TLC condition, because a lung starting at half its gas volume reaches collapse volume **shallower**, not deeper — the condition is not decoration, it is the direction of the effect.

*(Two fences. **(a)** "Measured" would be doing work the paper does not support: their vessel is rated only to **170 m depth-equivalent**, so the collapse depths are **extrapolations to zero gas volume, not readings**. **(b)** Per-specimen values for the common dolphin are **NOT-CONFIRMED** in this pass — the paper is paywalled, and two independent extraction attempts returned **mutually contradictory tables**, i.e. no trustworthy witness. An earlier pass of this chapter printed a common-dolphin pair (115 m @ 100% TLC / 127 m @ 50% TLC) that is **physically inverted** against Boyle's law and against the abstract's own range endpoints, so it was label-swapped or simply wrong; it is removed rather than repaired, because guessing which way to swap it would be inventing a number. Falsifier/closure: fetch Moore et al. 2011 **Table 2** and print each value with its species **and** its TLC condition.)*

**The specimens were dead.** Two methods, two answers, both legitimate, neither refuting the other — one infers from live physiology, one extrapolates from post-mortem mechanics. Do not average them; name the assay. (This is NA-08's kinesin-stall-force lesson in a different animal.)

The design payload stands regardless of which number wins: **the whale's answer to decompression sickness is not to manage nitrogen, but to eliminate the compartment that dissolves it.** Collapse the alveoli, force air into rigid non-exchanging airways, and the gas cannot enter the blood. You do not regulate the failure mode. You delete its substrate.

**The records, told honestly.** Schorr et al. (2014), *PLOS ONE* 9(3):e92633, tagged eight Cuvier's beaked whales (*Ziphius cavirostris*), logging 3,732 hours and 6,827 dives — **1,142 deep and 5,685 shallow** *(the 6,827 total is this chapter's sum from the paper's Table; the paper prints the two classes separately, and the figure 6,827 is not itself printed there)*. The records: **2,992 m** and **137.5 min**. The mean **deep** dive is 1,401 m (s.d. 137.8) and 67.4 min (s.d. 6.9) — computed over the **1,142 deep dives only**, **n = 1,142, not 6,827**. Carrying the total into the deep-dive mean overstates its sample by ~6× and silently mixes two dive classes with wildly different durations. Quick et al. (2020), *J Exp Biol* 223(18):jeb222109, analysed 3,680 dives from 23 tags: **median 59.0 min**, max **132 min**, with 5% exceeding **77.7 min** — their behavioural aerobic dive limit estimate.

And then the famous one. The **222-minute** dive that made headlines is real — but Quick et al. **censored it from their primary dataset**, along with a 173-min dive from the same individual (ZcTag066), because they were "recorded 17 and 24 days after a known 1-h exposure to a Navy mid-frequency active sonar signal." **The record-breaking dive is a post-sonar-exposure dive.** Almost every popular retelling drops that clause, and a number reported without its condition is worth less than the same number with it.

**But read what the censoring means, and read it from the authors — not into them.** The exclusion is a **statistical-hygiene decision for the bADL estimation**, not a disturbance verdict. Quick et al. say of these very dives that they are "perhaps more indicative of the true limits of the diving behaviour of this species." **The primary authors lean toward capacity.** So the honest position is that whether the 222-min dive measures a *disturbed* animal or a *capable* one is **UNRESOLVED**, and both readings are carried here rather than the chapter adopting the one it finds more interesting. The falsifier is the right one either way: an unexposed animal reaching >137.5 min.

## Sound: why low frequency is the long-baseline channel

Absorption rises steeply with frequency. Thorp's expression (via the TU Delft OCW propagation reader, ch. 3; primary: Thorp 1967, *JASA* 42:270) gives α in dB/km for f in kHz:

```
α = 0.11 f²/(1 + f²)  +  44 f²/(4100 + f²)  +  0.0003 f²
```

The three terms are boric acid relaxation, magnesium sulfate relaxation, and viscosity. Published values, and the distance to lose 10 dB:

| f | α (dB/km) | r₁₀dB |
|---|---|---|
| 100 Hz | 0.0012 | **8,333 km** |
| 1 kHz | 0.07 | 143 km |
| 10 kHz | 1.2 | 8.3 km |

Four orders of magnitude in range across two orders in frequency. Extrapolating the same formula down to a fin whale's band (**this chapter's own arithmetic, fenced MODELED, and below Thorp's fitting range**): at **20 Hz, α ≈ 4.8 × 10⁻⁵ dB/km**, giving r₁₀dB ≈ **2.1 × 10⁵ km** — about five Earth circumferences. *Absorption is simply not the limit down here.* For comparison, air at 2 kHz — **at 20 °C, 50% RH, 101.325 kPa**, per **ISO 9613-1** — absorbs at **≈ 9.9 dB/km ≈ 1.14 × 10⁻³ m⁻¹**, **≈ 80× more than seawater** at the same frequency (Thorp: 1.4 × 10⁻⁵ m⁻¹). The temperature, humidity and pressure are **part of the number**: an air absorption quoted with no stated condition is a number with no condition, which this chapter's own rail forbids. (Cross-ref NA-06 on frequency; CN-03 on air.)

*(Fence, and it cost this chapter its headline: earlier passes printed "air at 2 kHz absorbs at 0.02 m⁻¹, **over 1,000× more than seawater**" on the authority of the TU Delft OCW reader ch.3, which does say exactly that. **The reader's air value is wrong by ~17× and its ratio by ~13×** — recorded as a NEGATIVE below. A course reader is not a primary, and this chapter classed it OBSERVED-REPLICATED anyway.)*

**The SOFAR channel.** Sound speed in the sea has a minimum at depth — pressure raises it going down, temperature raises it going up, so there is a turning point (Møhl et al. measured 1477 m/s at the surface falling to 1468 m/s at 500 m in Norwegian coastal water). Rays leaving that axis are **refracted back toward it** from both sides: the layer is a waveguide, and energy trapped in it never touches the lossy surface or seafloor. Ewing & Worzel (1948), *Geological Society of America Memoir* 27, demonstrated it — charges detected at up to **900 nmi (~1,700 km)**. *(Fence: axis depth ~750–1,200 m at midlatitudes, shoaling to near-surface in polar regions, is from a secondary source in this pass.)*

### The units trap — this is where most comparisons die

**Underwater dB and airborne dB are different quantities.** Underwater sound is referenced to **1 µPa**; air to **20 µPa**. Two corrections separate them: the reference-pressure ratio (20² = 400) and the acoustic impedance ratio (ρc water / ρc air ≈ 3600). Together:

```
10 · log₁₀(400 × 3600) = 61.58 dB
```

So a number quoted "re 1 µPa" is **~62 dB larger** than the same physical intensity quoted in air. Møhl et al. (2003) do this conversion themselves: their 235 dB re 1 µPa rms corresponds to **173 dB SPL re 20 µPa** in air. This chapter's independent arithmetic gives 235 − 61.58 = **173.4** — agreement with the primary source, which is the only reason it is printed.

**Any text comparing a whale to a jet engine without this correction is wrong by ~62 dB.** That is not a quibble; it is a factor of ~1.4 million in intensity.

**Source levels, with their conventions attached.** Širović, Hildebrand & Wiggins (2007), *JASA* 122(2):1208–1215, using calibrated bottom-moored hydrophones off the Western Antarctic Peninsula: **blue whale 189 ± 3 dB re 1 µPa @ 1 m over 25–29 Hz**; **fin whale 189 ± 4 dB re 1 µPa @ 1 m over 15–28 Hz**. They localized blue whales to **200 km** (hyperbolic localization, range error 3.8 km) and fin whales to **56 km** (multipath, error 3.4 km). Those are **measured detection ranges** — the distance at which a hydrophone heard a whale, not the distance at which a whale hears a whale.

### HONEST FENCE — "whales hear each other across an ocean"

**The claim originates with Payne & Webb (1971)**, *Ann. N.Y. Acad. Sci.* 188:110–141, "Orientation by means of long range acoustic signaling in baleen whales." What it did: propagate fin-whale-like 20 Hz signals through a deep-sound-channel model and compute the range at which they fall to ambient noise, proposing that baleen whales live in acoustic contact across an ocean basin — the "acoustic herd."

**What it did not do: observe two whales communicating at range.** It is a **calculation**. Secondary sources render its headline number as ~700 km, 3,500 miles, 4,000 miles, and 13,000 miles (the last for a pre-propeller ocean) — a spread of more than an order of magnitude, because the answer depends entirely on the assumed noise floor. **The primary was not read in this pass, so no specific Payne–Webb range is asserted here.** Falsifier/closure: fetch *Ann. N.Y. Acad. Sci.* 188:110–141 and read the propagation section.

**What is measured:** whales *emit* at 189 dB re 1 µPa @ 1 m, and hydrophones detect them at ~10² km (Širović et al. 2007). **What is not measured:** that a whale receives, recognises, and acts on a conspecific's call at basin scale. Fifty years of anecdote is not a measurement.

**The best evidence to date is correlational and recent.** Podolskiy, Teilmann & Heide-Jørgensen (2024), *Phys. Rev. Research* 6:033174, analysed 144 days of dive records from 12 tagged bowhead whales in Disko Bay, West Greenland, and found **dive synchronisation at separations up to ~100 km, persisting for up to a week**. That is consistent with the acoustic herd hypothesis. It is **not** a demonstration of it: their tags recorded *dives*, not *sounds*, so the acoustic mechanism is inferred from timing correlation, and a shared environmental driver is not excluded.

**And the channel is being closed.** Andrew et al. (2002), *ARLO* 3(2):65–70, compared the *same receiver* off Point Sur, California, across four decades: 1994–2001 levels exceed 1963–1965 by **~10 dB between 20 and 80 Hz *and* between 200 and 300 Hz**, and by **~3 dB at 100 Hz**. McDonald, Hildebrand & Wiggins (2006), *JASA* 120(2):711–718, west of San Nicolas Island: **10–12 dB higher at 30–50 Hz** in 2003–2004 than 1964–1966 (95% CI = 2.6 dB), ≈ **2.5–3 dB/decade**, tracking a commercial fleet that roughly doubled in number and quadrupled in gross tonnage between 1965 and 2003. Two independent sites, two teams, same direction.

**The rise is *not* band-selective on the published evidence — and an earlier pass of this chapter claimed it was.** Both measured rises — Andrew's 20–80 Hz, McDonald's 30–50 Hz — sit **at or just above** the 15–29 Hz band the blue and fin whales use, and **neither team reports a measurement inside that band**. Worse for the tidy story: Andrew's *second* ~10 dB rise at **200–300 Hz** sits 7–20× above the whale bands, and it is the one datum the earlier pass omitted — from the prose and from the `ΔN_ambient` row alike. The honest statement is that the noise rise **overlaps the low-frequency channel without being confined to it**. Falsifier/closure: a calibrated long-baseline measurement resolving 15–29 Hz specifically.

*(A satisfying detail that shows the data are honest rather than tidy: McDonald et al. found the 1960s were **louder above 300 Hz**, owing to a diel component absent in modern records. A clean "everything got noisier" story would have been more suspicious.)*

## Toothed whales: convergence down to the amino acid

This is the wing's strongest single receipt for NA-01's doctrine — and its strongest lesson in how far a convergence claim may be pushed.

**The earned core.** Two independent groups published in the *same issue* of *Current Biology* in 2010: Liu et al., 20(2):R53–R54, and Li, Liu, Shi & Zhang, 20(2):R55–R56, "The hearing gene *Prestin* unites echolocating bats and whales." *Prestin* is the motor protein of outer hair cells — it is what makes the cochlear amplifier work at high frequency. Build a gene tree from Prestin protein sequences and **the bottlenose dolphin lands inside the microbats** — contradicting the species phylogeny — with evidence of selection driving the substitutions. Bats and toothed whales, which are not each other's closest relatives by any other evidence, converged on the *same molecular solution* to the *same physical problem*. That is not a metaphor about nature's ingenuity; it is a tree topology that contradicts the species tree. *(Fence: the bat–cetacean divergence date is NOT-SOURCED in this pass and no figure is asserted here; the argument rests on the topological conflict, which needs no date.)*

**The overreach, and its correction.** Parker et al. (2013), *Nature* 502(7470):228–231, scaled this up: 22 mammal genomes, 805,053 amino acids across 2,326 orthologous genes, reporting convergence signatures at **~200 loci** — a genome-wide phenomenon. Zou & Zhang (2015), *MBE* 32(5):1237–1241, titled their reply **"No Genome-Wide Protein Sequence Convergence for Echolocation"** and found the reported signature "largely reflect[s] the background level of sequence convergence unrelated to the origins of echolocation." Their finding: **12 of 14** genuinely convergent sites fell within **six of seven already-known hearing proteins** — "at most a few proteins were subject to convergent evolution." (Thomas & Hahn 2015, *MBE* 32(5):1232–1236, attacked the null model on the same page range.)

**Read the outcome correctly.** The rebuttal did **not** touch *Prestin*: Zou & Zhang explicitly preserve it as having passed "proper statistical tests and functional assays." **The specific, mechanistically motivated convergence survived; the genome-wide generalisation did not.** For NA-01 this is *better* than an uncontested claim would have been — the doctrine is that convergence under a shared physical constraint is evidence of a constraint-optimum, and what survived is precisely the locus where the constraint bites. What died is the claim that convergence was smeared across the genome, where no constraint argument predicted it.

**The loudest sound measured from an animal.** Møhl, Wahlberg, Madsen, Heerfordt & Lund (2003), *JASA* 114(2):1143–1154, using a GPS-synchronised large-aperture array (5–10 units, 14 h) in the Bleik Canyon off Vesterålen: on-axis sperm whale clicks reach **236 dB re 1 µPa rms** (eight further events at 226–234 dB; they adopt **235 dB** as representative), duration **~100 µs**, centroid **15 kHz**, directionality index **27 dB**, and a half-power **half-angle of ~4°** — that is, a **full −3 dB beamwidth of ~8°**. Møhl et al. print the *half-angle* ("The half power, half-angle of this function is 4°"); beamwidths are conventionally quoted as **full width**, so "beam width ~4°" is off by 2× against any paper a reader would compare it to. Their own characterisation: these are "by far the loudest of sounds recorded from any biological source."

**Why the number was wrong for forty years, and it is a methods story.** Early single-hydrophone work reported **170–180 dB** and concluded the clicks were weak, long, and non-directional — therefore not sonar. They were recording a **27 dB-directional** source *off-axis*. Large-aperture arrays later found 202–223 dB. Møhl et al. resolved it: **only about one click in a thousand** recorded is the on-axis monopulse. The "gentle" sperm whale of the classical literature was an artefact of standing in the wrong place. **A directional source measured off-axis does not give you a smaller number; it gives you a wrong one.**

Two calibration handles from the same paper, both theirs: 235 dB re 1 µPa rms is **10–14 dB above what is measurable 1 m in front of the muzzle of a powerful rifle**; and radiating it *omnidirectionally* would need **2 MW** at 100% efficiency — the 27 dB of directionality is what reduces the requirement to a merely astonishing **4 kW**.

**And Møhl et al. flag the trap themselves:** they report **true rms**, noting it is "significantly different (yielding lower values) from the peak-to-peak measures, used in most of the literature on odontocete clicks." So a sperm whale click and a dolphin click quoted from two papers are frequently **not in the same unit**. Always read the convention before comparing.

**The frequency argument closes the loop.** Their detection calculation for a squid (*Loligo*, target strength −40 dB) gives a detection threshold ~20 dB at **1 km** — and they note the absorption term "has a minimal impact due to the relatively low frequencies of the pulse spectrum." Substitute a dolphin-like **100 kHz** pulse, all else equal, and detectability falls by **~60 dB** at that range. The sperm whale is a long-range sonar *because* it is a 15 kHz sonar. It pays for the low frequency with a two-metre nose, and buys back the beam width with sheer aperture. **The sonar equation itself is developed in CN-10 — it is not duplicated here.**

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `M_blue,measured` | — | t | mass of the largest blue whale | **NOT-MEASURED** | Motani & Pyenson 2024, *PeerJ* 12:e16978 | Weigh one intact |
| `M_blue,piece` | ≥136.4 | t | 27.1 m female, weighed in parts (fluid lost) | OBSERVED-SINGLE | Winston 1950, via Motani & Pyenson 2024 | Re-weigh under controlled loss accounting |
| `M_blue,regr` | 234 (95% CI 187–294); fluid-corrected **252 (CI 201–306)** @ 7% blood loss, **272 (CI 217–342)** @ 14% | t | 33 m blue whale, length→mass regression. **The two fluid-corrected values are separate estimates under separate blood-loss assumptions — never merge them into one interval; "CI 201–342" is a hull of two intervals, not an interval** | MODELED | Motani & Pyenson 2024 | New regression on a larger measured sample; an independent fluid-loss accounting outside 7–14% |
| `M_blue,vol` | 266–279 | t | 3D volumetric model | MODELED | Motani & Pyenson 2024 | Independent volumetric model outside range |
| `L_blue,max` | 33.26 | m | longest reliably measured blue whale | OBSERVED-SINGLE | Risting 1928, via Motani & Pyenson 2024 | A longer verifiable measurement |
| `M_Perucetus` | **85–340 vs 60–70 (max 98–114)** | t | *P. colossus*: original vs re-analysis. **85–340 is reported via the rebuttal, not the primary (M22 cavity)** | **OBSERVED-CONTESTED** | Bianucci et al. 2023 **as characterised in** Motani & Pyenson 2024, *PeerJ* 12:e16978 | Fetch Bianucci et al. 2023 directly; third independent estimate; new postcrania |
| `EE_odontocete` | decreases with body mass | ratio | energy captured ÷ energy expended | OBSERVED-REPLICATED | Goldbogen et al. 2019, *Science* 366:1367–1372 | Tag data showing EE rising with size in odontocetes |
| `EE_rorqual` | increases with body mass | ratio | lunge filter feeders on krill | OBSERVED-REPLICATED | Goldbogen et al. 2019, *Science* | As above, inverted |
| `EE_robustness` | holds for MR ∝ M^0.45 … M^0.75 | — | metabolic-exponent ablation | MODELED | Goldbogen et al. 2019, *Science* | An exponent in range that flips the sign |
| `V_engulf` | 100–160 | % of whale's own body volume | largest rorquals, per lunge | OBSERVED-REPLICATED | Goldbogen et al. 2019, *Science* | Direct volumetric measurement outside range |
| `E_lunge/E_prey,odont` | ≥1 | orders of magnitude | largest rorqual lunge vs largest toothed-whale prey | OBSERVED-REPLICATED | Goldbogen et al. 2019, *Science* | Prey-energy census closing the gap |
| **Size limit** | **prey availability, not physiology** *vs* **cardiac limit** | — | *Science* 2019 vs *PNAS* 2019, shared first author | **OBSERVED-CONTESTED** | Goldbogen et al. 2019 *Science* 366:1367–1372; *PNAS* 116:25329–25332 | ECG on n≫1 blue whales; a prey-abundance manipulation |
| `f_HR,dive` | 4–8 (min **2**) | bpm | blue whale, foraging dives ≤184 m, ≤16.5 min | OBSERVED-SINGLE (**n=1**) | Goldbogen et al. 2019, *PNAS* 116(50):25329–25332 | Second instrumented blue whale outside range |
| `f_HR,surface` | 25–37 | bpm | post-deep-dive tachycardia, near inferred max | OBSERVED-SINGLE (**n=1**) | Goldbogen et al. 2019, *PNAS* | As above |
| `f_HR,pred` | 15 | bpm | allometrically predicted resting, 70,000 kg | MODELED | Goldbogen et al. 2019, *PNAS* | Re-derive the allometry |
| `TE_trophic` | **10** | % per trophic level | 48 trophic models, 6 aquatic ecosystem types; **re-estimated, not assumed** | OBSERVED-REPLICATED | Pauly & Christensen 1995, *Nature* 374:255–257 | Re-estimate from independent models outside ~5–15% |
| `TL_range` | 1.0 (edible algae) – 4.2 (tunas) | fractional trophic level | 39 commodity groups, global catch 94.3 Mt/yr 1988–91 | OBSERVED-REPLICATED | Pauly & Christensen 1995 | Re-assign trophic levels |
| Land-vs-sea size asymmetry | no terrestrial pre-concentrated low-trophic patch | — | **this chapter's synthesis** | **MODELED** | Composed here from Goldbogen 2019 + Pauly & Christensen 1995 | Exhibit a terrestrial bulk-engulfable low-trophic resource |
| `[Mb]_cetacean` | 1.81–5.78 | g Mb / 100 g wet muscle | cetaceans, body mass 70–80,000 kg | OBSERVED-REPLICATED | Noren & Williams 2000, *Comp Biochem Physiol A* 126(2):181–191 | Measurement outside range under stated method |
| `[Mb]_dolphin,max` | ~6.3 | g Mb / 100 g | striped dolphin, epaxial middle | OBSERVED-SINGLE | Arregui et al. 2021, *Animals* 11(2):451 | Independent assay >2× off |
| `f_Mb,locomotor` | 92.8 | % of total muscle O₂ store | three delphinid species | OBSERVED-SINGLE | Arregui et al. 2021 | Re-partition by muscle group |
| `[Mb]_terrestrial` | <~0.5 (ratio 10–30× divers:non-divers) | g Mb / 100 g | non-diving mammals — **Kooyman 1989 primary not read here** | OBSERVED-REPLICATED *(secondary attribution)* | Kooyman 1989, cited in the comparative literature | Fetch Kooyman 1989; measure human muscle Mb |
| `[Mb]_human` | — | g Mb / 100 g | human skeletal muscle | **NOT-MEASURED** | not sourced in this pass | Fetch a primary value |
| `Z_Mb` | elevated net surface charge in divers | — | ancestral reconstruction, 130-species phylogeny | OBSERVED-REPLICATED | Mirceta et al. 2013, *Science* 340(6138):1234192 | A high-[Mb] diver without the charge signature |
| `r²_dive` | 50 (all cetaceans); 83 (odontocetes) | % variance in max dive duration explained by [Mb] + body mass | — | MODELED | Noren & Williams 2000 | Re-run the regression |
| `d_collapse,N₂` | ~70 | m | *Tursiops truncatus*, **live**, inferred from N₂ washout | OBSERVED-SINGLE | Ridgway & Howard 1979, *Science* 206(4423):1182–1183 | Repeat washout; a different inferred depth |
| `d_collapse,CT` | range **58** (grey seal, 50% TLC) – **133** (harbour porpoise, 100% TLC); per-specimen common-dolphin values **NOT-CONFIRMED** | m | **post-mortem** hyperbaric CT, **extrapolated to zero gas volume** — vessel rated only to 170 m depth-equivalent, so these are extrapolations, **not readings**. Every value carries a TLC condition. *Do not average with the row above* | **OBSERVED-CONTESTED** | Moore et al. 2011, *J Exp Biol* 214:2390–2397 (**abstract only — Table 2 not read in this pass**) | In-vivo imaging under pressure reconciling both; fetch Table 2 for per-specimen values |
| `d_dive,max` | **2,992** | m | *Ziphius cavirostris*, mammalian depth record | OBSERVED-SINGLE | Schorr et al. 2014, *PLOS ONE* 9(3):e92633 | A deeper tagged mammalian dive |
| `t_dive,mean` | 67.4 (s.d. 6.9) @ 1,401 m (s.d. 137.8) | min | *Ziphius*, mean **deep** dive, 8 whales / **n = 1,142 deep dives** (of 6,827 total = 1,142 deep + 5,685 shallow; **the 6,827 sum is this chapter's, from the paper's Table — the paper does not print it**). **n is the deep-dive count, not the total** | OBSERVED-REPLICATED | Schorr et al. 2014 | Independent tagging outside range |
| `t_dive,median` | 59.0 (max 132; 95th pct 77.7 = bADL) | min | *Ziphius*, 3,680 dives / 23 tags, **primary dataset** | OBSERVED-REPLICATED | Quick et al. 2020, *J Exp Biol* 223(18):jeb222109 | Independent dataset outside range |
| `t_dive,222` | **222** (and 173) | min | **one** individual (ZcTag066); **censored from the bADL estimation for statistical hygiene** — 17 and 24 d after a known 1-h Navy mid-frequency sonar exposure. **Capacity vs disturbance is UNRESOLVED, and the primary authors lean *capacity*:** "perhaps more indicative of the true limits of the diving behaviour of this species" | **OBSERVED-CONTESTED** *(the dispute is capacity-vs-disturbance; the censoring is **not** a disturbance verdict)* | Quick et al. 2020 | An unexposed animal reaching >137.5 min |
| `α(f)` | 0.11f²/(1+f²) + 44f²/(4100+f²) + 0.0003f² | dB/km (f in kHz) | Thorp; **N. Atlantic, <50 kHz** | OBSERVED-REPLICATED | Thorp 1967, *JASA* 42:270, via TU Delft OCW reader ch.3 | Measured α outside fit under stated conditions |
| `α(100 Hz)` | 0.0012 → r₁₀dB **8,333** | dB/km → km | Thorp, published table | OBSERVED-REPLICATED | TU Delft OCW reader ch.3 | Recompute; field measurement |
| `α(1 kHz)` | 0.07 → r₁₀dB 143 | dB/km → km | Thorp, published table | OBSERVED-REPLICATED | as above | as above |
| `α(10 kHz)` | 1.2 → r₁₀dB 8.3 | dB/km → km | Thorp, published table | OBSERVED-REPLICATED | as above | as above |
| `α(20 Hz)` | ~4.8 × 10⁻⁵ → r₁₀dB ~2.1 × 10⁵ | dB/km → km | **computed here**, Thorp extrapolated **below its fitting range** | **MODELED** | Computed here; formula per Thorp 1967 | Field measurement at 20 Hz; a low-f formula disagreeing |
| `α(15 kHz)` | **2.47 (Thorp, evaluated here) vs 1.5 (adopted by Møhl et al. for their sonar-equation example)** | dB/km | **two model inputs, not two observations.** Møhl et al. state no site measurement — 1.5 dB/km is a parameter they plug into a worked example. The gap is an **unexplained parameter difference, not a contested observation**, and no source cited attributes it to a site effect. Do not reconcile by averaging | **MODELED** | Computed here (Thorp 1967); Møhl et al. 2003 (**parameter choice, not a measurement**) | Measure α at 15 kHz at both sites |
| `α_air,2kHz` | **≈ 9.9 dB/km ≈ 1.14 × 10⁻³ m⁻¹** | dB/km; m⁻¹ | air at **2 kHz, 20 °C, 50% RH, 101.325 kPa** — **the condition is part of the number** | **MODELED** (ISO 9613-1 evaluated here) | **ISO 9613-1** (the standard, *not* the course reader); implementation checked against ISO 9613-2 Table 2 (20 °C/70% RH: 1k ≈ 5, 2k ≈ 9, 4k ≈ 23 dB/km) | An ISO 9613-1 table lookup or calibrated air-absorption measurement at 2 kHz disagreeing with ~10 dB/km |
| `α_air/α_water` | **≈ 80×** | ratio | at 2 kHz (air 1.14 × 10⁻³ m⁻¹ @ 20 °C/50% RH vs Thorp 1.4 × 10⁻⁵ m⁻¹). **Not ">1,000×" — that figure came from the TU Delft reader's air value, which is wrong by ~17×; see the NEGATIVE below** | **MODELED** (arithmetic on the two source rows) | Computed here from ISO 9613-1 + Thorp 1967 | Independent measurement of either term |
| **`ΔdB_air/water`** | **61.58** | dB | `10·log₁₀(20² × 3600)`: reference-pressure ratio × impedance ratio | MODELED (**arithmetic**) | Computed here; cross-checked against Møhl et al. 2003's own 235→173 conversion | Arithmetic error; a different impedance ratio |
| `SL_blue` | **189 ± 3** | dB re 1 µPa @ 1 m, 25–29 Hz | calibrated bottom-moored hydrophones, W. Antarctic Peninsula | OBSERVED-REPLICATED | Širović, Hildebrand & Wiggins 2007, *JASA* 122(2):1208–1215 | Calibrated measurement outside 186–192 |
| `SL_fin` | **189 ± 4** | dB re 1 µPa @ 1 m, 15–28 Hz | as above | OBSERVED-REPLICATED | Širović et al. 2007 | As above |
| `r_detect,blue` | 200 (error 3.8) | km | **measured** localization range (hyperbolic) — *hydrophone hears whale* | OBSERVED-SINGLE | Širović et al. 2007 | Longer localization with stated error |
| `r_detect,fin` | 56 (error 3.4) | km | **measured** localization range (multipath) | OBSERVED-SINGLE | Širović et al. 2007 | As above |
| `SL_sperm` | **236 max; 235 representative** (8 events 226–234) | dB re 1 µPa **rms** (on-axis) | *Physeter*, large-aperture array, 14 h, Bleik Canyon | OBSERVED-SINGLE | Møhl et al. 2003, *JASA* 114(2):1143–1154 | Calibrated on-axis measurement outside range |
| `SL_sperm,offaxis` | **170–180 (classical) vs 202–223 (large-aperture) vs 236 (on-axis)** | dB re 1 µPa | **the same animal** — the spread is aspect angle, not disagreement | OBSERVED-REPLICATED | Møhl et al. 2003 (reviewing Backus & Schevill 1966 etc.) | Show the classical figures were on-axis |
| `SL_sperm,air-equiv` | 173 | dB SPL re 20 µPa | 235 dB re 1 µPa rms converted **by the source authors** | MODELED | Møhl et al. 2003 | Recompute the impedance conversion |
| `DI_sperm` | 27 (half-power **half-angle** ~4° ⇒ **full −3 dB beamwidth ~8°**) | dB | composite directionality index. **Møhl et al. print the half-angle; beamwidth is conventionally quoted full-width — name the convention or be wrong by 2×** | OBSERVED-SINGLE | Møhl et al. 2003 | Reconstruct the radiation pattern |
| `p_on-axis` | ~1 in 1,000 | clicks | probability a recorded click is the on-axis monopulse | OBSERVED-SINGLE | Møhl et al. 2003 | A recording geometry with a different hit rate |
| `P_sperm` | 2 MW omni @ 100% eff. → **4 kW** at DI = 27 dB | W | peak acoustic power to make 235 dB re 1 µPa rms | MODELED | Møhl et al. 2003 | Recompute; refute DI |
| `t_click` / `f_c` | ~100 µs / 15 kHz (cBW_rms 4.1 kHz) | s / Hz | on-axis p1 pulse | OBSERVED-SINGLE | Møhl et al. 2003 | Independent on-axis recording |
| **rms vs p-p** | true rms is **significantly lower** than peak-to-peak, "used in most of the literature on odontocete clicks" | — | **the units trap** | OBSERVED-REPLICATED | Møhl et al. 2003 (their own caveat) | — |
| `Δ_100kHz` | ~60 | dB detectability lost to absorption at 1 km | substituting a dolphin-like 100 kHz pulse, ceteris paribus | MODELED | Møhl et al. 2003 | Recompute the sonar equation |
| `c_sound` | 1477 (surface) → 1468 (500 m) | m/s | Norwegian coastal water, measured profile | OBSERVED-SINGLE | Møhl et al. 2003 | Independent CTD profile |
| `z_SOFAR` | ~750–1,200 (midlat); near-surface polar | m | deep sound channel axis | OBSERVED-REPLICATED *(secondary source in this pass)* | Ewing & Worzel 1948, *GSA Memoir* 27; depth via secondary | Fetch a primary sound-speed climatology |
| `r_SOFAR,demo` | up to 900 nmi (~1,700 km) | km | 1944 R/V *Saluda* explosive-charge demonstration | OBSERVED-SINGLE | Ewing & Worzel 1948 | Read the primary; a different demonstrated range |
| `r_PayneWebb` | **NOT-CONFIRMED** (secondaries render ~700 km / 3,500 mi / 4,000 mi / 13,000 mi) | km | calculated basin-scale range for 20 Hz calls | **MODELED / NOT-CONFIRMED** | Payne & Webb 1971, *Ann NY Acad Sci* 188:110–141 — **primary not read in this pass** | Fetch the primary and read the propagation section |
| Whales hear each other across a basin | — | — | reception + response at basin scale | **NOT-MEASURED** | — | Show a whale detectably responds to an identified conspecific call at ≥10³ km |
| `r_sync,bowhead` | up to ~100 (persisting up to ~1 week) | km | 12 tagged bowheads, 144 d, Disko Bay; **dives recorded, sounds not** | OBSERVED-SINGLE (mechanism **inferred**) | Podolskiy, Teilmann & Heide-Jørgensen 2024, *Phys Rev Research* 6:033174 | Simultaneous acoustic + dive tags; exclude a shared environmental driver |
| `ΔN_ambient` | ~10 (**20–80 Hz**) **and** ~10 (**200–300 Hz**); ~3 (100 Hz) | dB, 1963–65 → 1994–2001 | **same receiver**, Point Sur, California. **The 200–300 Hz rise sits 7–20× above the whale bands — it is part of Andrew's result and it refutes any "concentrated in the whale band" reading** | OBSERVED-REPLICATED | Andrew et al. 2002, *ARLO* 3(2):65–70 | Recalibrate; a site showing no rise |
| `ΔN_ambient,SN` | **10–12** (95% CI 2.6) at 30–50 Hz ⇒ **2.5–3 dB/decade** | dB, 1964–66 → 2003–04 | west of San Nicolas Is.; 138 d continuous | OBSERVED-REPLICATED | McDonald, Hildebrand & Wiggins 2006, *JASA* 120(2):711–718 | Independent long-baseline site disagreeing |
| `ΔN_>300Hz` | 1960s **higher** (diel component absent today) | dB | the counter-trend — the data are not tidy | OBSERVED-SINGLE | McDonald et al. 2006 | Re-analyse the 1960s diel signal |
| `N_ships` | ~2× count, ~4× gross tonnage, 1965→2003 | — | world commercial fleet | OBSERVED-SINGLE | McDonald et al. 2006 | Independent fleet statistics |
| Noise rise vs the whale band | measured rises (Andrew **20–80 Hz**; McDonald **30–50 Hz**) **overlap but are not confined to** the 15–29 Hz blue/fin band; **neither team reports a measurement inside that band**, and Andrew finds a comparable rise at 200–300 Hz | — | **this chapter's synthesis** — *not* "concentrated in the whale band", which no cited paper supports | **MODELED** | Composed here from Andrew et al. 2002 + McDonald et al. 2006 + Širović et al. 2007 | A calibrated long-baseline measurement resolving 15–29 Hz specifically |
| **Prestin convergence** | dolphin groups **inside** microbats in the Prestin protein tree | — | echolocating bats + toothed whales | OBSERVED-REPLICATED | Li, Liu, Shi & Zhang 2010, *Curr Biol* 20(2):R55–R56; Liu et al. 2010, 20(2):R53–R54 (**independent, same issue**) | A Prestin tree recovering the species topology |
| **Genome-wide convergence** | **~200 loci (Parker) vs "background level" (Zou & Zhang)** | loci | 22 genomes, 805,053 aa, 2,326 genes | **OBSERVED-CONTESTED** *(the genome-wide claim did not survive)* | Parker et al. 2013, *Nature* 502(7470):228–231; **Zou & Zhang 2015, *MBE* 32(5):1237–1241**; Thomas & Hahn 2015, *MBE* 32(5):1232–1236 | A method settling the null model |
| Hearing-gene convergence | **12 of 14** convergent sites in **6 of 7** known hearing proteins; Prestin explicitly upheld | sites | Zou & Zhang's own re-analysis | OBSERVED-REPLICATED | Zou & Zhang 2015 | Re-analysis dispersing the sites genome-wide |

## Falsifier (operable)

This chapter's central structural claim — **that the ceiling on animal size, once buoyancy removes the skeletal-stress constraint, is set by the energetics of acquiring a low-trophic-level resource in bulk, not by the mechanics of being large** — is refuted by exhibiting **either**:

1. **A large aquatic animal whose foraging energetic efficiency rises with body size and which nevertheless does not approach the size ceiling**, with prey demonstrably abundant across its range and season — which would show prey availability is not binding; **or**
2. **A direct measurement identifying a mechanical, cardiac, thermal, or respiratory ceiling that binds at a mass below ~250 t** — e.g. ECG on a statistically adequate sample of blue whales showing surface heart rate saturating at a mass well under the observed maximum. (Goldbogen et al. 2019 *PNAS* is n=1 and is a *candidate* for this falsifier, not a satisfaction of it.)

The **low-frequency channel claim** — that the useful long-baseline information channel in the sea is low-frequency *because absorption scales steeply with frequency* — is refuted by a calibrated field measurement of α at 20–100 Hz exceeding the Thorp/Francois–Garrison predictions by more than an order of magnitude, or by demonstrating a >10³ km biological signalling channel above 10 kHz.

Row-local falsifiers are in the table. A refuted row moves that row. A refuted `EE`-versus-size divergence, or a refuted `α ∝ f²`, moves the chapter.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **"Whale calls can be heard across an ocean" / "whales talk to each other across the globe."** — **NOT-MEASURED as stated, and routinely presented as if measured.** Payne & Webb (1971) *calculated* a basin-scale range; they did not observe reception. Fifty years on, the best evidence remains correlational (Podolskiy et al. 2024: dive synchrony to ~100 km, with sounds *not* recorded). The measured quantities are a 189 dB re 1 µPa @ 1 m source level and ~200 km hydrophone localization. **Emission is not communication, and detection by an instrument is not reception by an animal.** Recorded as an open question with a stated falsifier, not as folklore and not with contempt — Payne & Webb's model was good science that has simply never been closed.
- **NEGATIVE / units trap — comparing underwater dB to airborne dB directly.** Wrong by **61.58 dB** (~1.4 × 10⁶ in intensity). "The sperm whale is louder than a jet engine" is not a finding; it is a missing impedance correction. Møhl et al. (2003) do the conversion themselves: 235 dB re 1 µPa rms = **173 dB SPL re 20 µPa**. Recorded because the error is near-universal in popular accounts.
- **NEGATIVE / units trap — rms versus peak-to-peak.** Møhl et al. report **true rms** and warn it is "significantly different (yielding lower values) from the peak-to-peak measures, used in most of the literature on odontocete clicks." Quoting a sperm whale click against a dolphin click across two papers is frequently a comparison **between different units**. Named by the primary source itself.
- **NEGATIVE / units trap — half-angle versus full beamwidth.** Møhl et al. print "a half-angle, half-power beam width of about 4°". Beamwidths are **conventionally quoted as full width**, so the sperm whale's −3 dB beam is **~8°** — and an earlier pass of this chapter printed "half-power beam width ~4°", **wrong by 2× against any paper a reader would compare it to**. Same class of error as *re* 1 µPa-vs-*re* 20 µPa and rms-vs-p-p, and committed **while quoting the very source that supplies the warning**, in the section devoted to warning about it. Recorded as the third instance because the pattern is the point: a convention is not a detail, and the trap catches the people who know about the trap.
- **NEGATIVE / a teaching source's order-of-magnitude error, laundered here as OBSERVED-REPLICATED.** The TU Delft OCW propagation reader (ch.3) states verbatim: "For 2 kHz this is 0.02 m-1, which is over a factor 1000 larger than in seawater at the same frequency (Thorpe: 1.4x10-5 m-1)." **The reader's air value is wrong by ~17×.** Its own conversion on the same page — α(dB/km) = 8686·α(m⁻¹) — turns 0.02 m⁻¹ into **174 dB/km** at 2 kHz, which is physically absurd. **ISO 9613-1** evaluated here (2 kHz, 20 °C, 50% RH, 101.325 kPa) gives **9.87 dB/km = 1.14 × 10⁻³ m⁻¹**; and 0.02 m⁻¹ is in fact the ISO air value at **~10 kHz** (1.83 × 10⁻² m⁻¹), so the reader appears to have **mislabelled a 10 kHz value as 2 kHz**. The true ratio is **≈ 81×**, not >1,000×. Recorded **twice over**: against the reader, whose error is carried into the wider literature; and against this chapter, which transcribed it faithfully, **classed it OBSERVED-REPLICATED — the strongest NATURA class — with no primary read and no secondary-source fence** (while fencing `z_SOFAR` and `[Mb]_terrestrial` correctly on the same page), and staked its entire low-frequency thesis on an air/water contrast it had wrong by ~13×. **A faithful transcription of a wrong number is still a wrong number, and fidelity to a secondary is not evidence.**
- **NEGATIVE / the censored record — and this chapter's own misreading of what the censoring meant.** The widely reported **222-minute** Cuvier's beaked whale dive was **excluded from Quick et al.'s own analysis** — it and a 173-min dive came from one individual 17 and 24 days after a known Navy mid-frequency sonar exposure. Reporting the number without that condition is reporting a number without its scope, and popular retellings do exactly that. **But an earlier pass of this chapter glossed the censoring as meaning the dive "may be evidence of *disturbance*, not capacity", called the ordinary reading an *inversion* of the source's meaning, and attributed all of that to Quick et al. The authors hold the opposite view.** They write that these extreme durations are "perhaps more indicative of the true limits of the diving behaviour of this species", and they censored them for **statistical hygiene in the bADL estimation** — not on suspicion of disturbance. Capacity vs disturbance is **UNRESOLVED, and the primary authors lean capacity**. Recorded as a NEGATIVE **against this chapter**: presenting one's own inference as the cited authors' position — and then accusing everyone else of inverting them — is precisely what **M22** exists to stop, and it was committed in a chapter whose stated doctrine is *read the primary*, as its flagship NEGATIVE. The uncensored figures are median 59.0 min, max 132 min, bADL ≈ 77.7 min.
- **NEGATIVE / genome-wide echolocation convergence.** Parker et al. (2013)'s ~200-locus genome-wide signature **did not survive**: Zou & Zhang (2015) found it "largely reflect[s] the background level of sequence convergence unrelated to the origins of echolocation." Recorded as a published negative, and recorded as a *success* of the method under **M15** — the specific, mechanistically motivated *Prestin* result stands precisely because someone tried to break the general one and could not break the specific one.
- **NEGATIVE / off-axis measurement of a directional source.** Forty years of literature described sperm whale clicks as weak (170–180 dB), long, and non-directional, and inferred *from those properties* that the clicks were not sonar. The source has DI = 27 dB and only ~1 click in 1,000 is recorded on-axis. **The error was not in the instruments; it was in the geometry**, and it propagated into a wrong functional conclusion for four decades.
- **INADMISSIBLE — "the blue whale is nature's most efficient/perfect design."** Unfalsifiable as stated: no observation is specified that could refute it. The falsifiable neighbours are in the table (EE rises with size in rorquals; falls in odontocetes) and are what should be cited instead. Recorded, not mocked.
- **NEGATIVE / cavity (M22).** *Perucetus*'s 85–340 t is reported here **only through the paper that rebuts it**. That is a cavity: the rebuttal is not a neutral witness to the claim's strength. The dispute is recorded; the original number is *not* endorsed at any confidence, in either direction. Named because the tidy version of this story ("Perucetus was 340 t, then it wasn't") would be built entirely out of one side's characterisation of the other.
- **NOT-CONFIRMED in this pass:** Payne & Webb's specific calculated range (secondaries disagree by >10×); Kooyman (1989)'s primary myoglobin comparison; the SOFAR axis depth (secondary source); the "190 t / 27.6 m, 1947" whaling record (secondary source); Bianucci et al. 2023's primary mass estimate (read only via its rebuttal); the bat–cetacean divergence date (no figure asserted); **Moore et al. 2011's per-specimen lung-collapse depths for the common dolphin** (paper paywalled, Table 2 not read; two independent extraction attempts returned **mutually contradictory tables**, so there is no trustworthy witness — only the abstract's range endpoints, **58 m** grey seal @ 50% TLC and **133 m** harbour porpoise @ 100% TLC, are confirmed, and the previously printed dolphin pair was **physically inverted** against Boyle's law and has been removed rather than guessed at). Each is printed with that status rather than laundered into a clean number.
- **NOT-MEASURED:** the mass of the largest blue whale; human skeletal-muscle myoglobin; any thermal ceiling on cetacean body size; whether any whale receives and acts on a conspecific call at basin scale.

## HONEST FENCE — MODELED

This chapter is fenced **MODELED**. Individual rows carry their own classes — many OBSERVED-REPLICATED, several **OBSERVED-CONTESTED** (Perucetus mass; the size-limit mechanism; lung-collapse depth; genome-wide convergence; the censored 222-min dive), several **NOT-MEASURED** — but the chapter *as an artifact* composes measured constants through stated assumptions to reach design conclusions. **The assumptions are the fence:** the `α(20 Hz)` row extrapolates Thorp's formula below its fitting range; `α_air,2kHz` is ISO 9613-1 **evaluated here at one stated condition** (20 °C, 50% RH, 101.325 kPa) and moves with temperature and humidity; `α(15 kHz)` compares **two model inputs, not two observations**; the air/water dB offset assumes plane waves and a nominal impedance ratio of 3600; the land-versus-sea size asymmetry and the noise-rise-versus-whale-band overlap are this chapter's own syntheses, not sourced comparative measurements. Two of the headline results rest on **n=1** (the blue whale ECG) or on **inference rather than observation of the mechanism** (bowhead synchrony).

Per **Gould & Lewontin (1979), "The Spandrels of San Marco and the Panglossian Paradigm"**: nothing above establishes that any cetacean feature is an optimum. Drift, phylogenetic inertia, developmental constraint, and frozen accidents produce traits that solve nothing — and cetaceans carry conspicuous ones, having re-entered the water with an air-breathing tetrapod body plan that a designer starting fresh would never choose. **Nature's authority here is precise and narrow: it has already run a very long parallel search under real physical constraints in which the failures were deleted.** That makes the bat–whale *Prestin* convergence evidence of a constraint-optimum *at that locus* — and makes every number above a **hypothesis generator**, not a proof. Per repo rule **M7**, any design taken from this chapter must still beat a **tuned conventional baseline** on a **pre-registered metric**, with a discriminator that would collapse the gain, or it is recorded **NEGATIVE**.

## Not claimed

- **Not claimed:** that whales communicate across ocean basins. That is the chapter's flagship NOT-MEASURED and it has an operable falsifier. The measured facts (189 dB source levels, ~200 km localization, ~100 km dive synchrony) do not add up to it, and stacking them until they seem to is the exact error this chapter exists to prevent.
- **Not claimed:** that prey availability *is* the blue whale's size limit. Goldbogen et al. (2019, *Science*) argue it; Goldbogen et al. (2019, *PNAS*) point at cardiac limits. **Both are carried; neither is adopted.** A chapter that picked one would be more satisfying and less honest.
- **Not claimed:** that lunge feeding is "optimal", or that filter feeding is a general route to gigantism. Balaenids filter-feed and show *lower* efficiency than similarly sized rorquals — the mechanism is bulk engulfment of *dense patches*, and the counterexample is inside the same clade.
- **Not claimed:** that the sperm whale's 236 dB is comparable to any airborne figure without the 61.58 dB correction, or to any peak-to-peak odontocete figure without a convention check.
- **Not claimed:** that echolocation convergence extends genome-wide. It does not; that claim was published and rebutted, and both are cited.
- **Not claimed:** that any whale is self-aware, cognitive, linguistic, or that whale song constitutes language. Nothing in this chapter measures any such thing. Source levels, call bands, dive timing, and gene trees are what were measured; they license no claim about experience, and the honest position on cetacean minds is that this chapter does not address it.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** Reading Møhl et al. 2003 does not make any UNI claim proven, designed, or built. The NATURA twelve-value class (OBSERVED-REPLICATED / OBSERVED-SINGLE / OBSERVED-CONTESTED / MODELED / MODELED-CONTESTED / HYPOTHESIZED / INADMISSIBLE / SUPERSEDED / NOT-MEASURED / NOT-SOURCED / NOT-CONFIRMED / NOT-LOCATED — six of them registered by NA-00 amendment 2026-07-15-A) and the UNI four-value fence (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. This chapter contains **zero** UNI claims.
- **QUAESTIO-APERTA:** "the next evolution beyond human" and "full human" appear nowhere in this chapter as a target, milestone, or deliverable. They are permanent open questions, and the upper bound of animal size has no bearing on them.


<!-- ===== END cookbook/recipes-natura/CN-09-whales.md ===== -->



<!-- ===== BEGIN cookbook/recipes-natura/CN-10-bats.md ===== -->

# CN-10 — Bats: active inference you can measure

> **What you are building.** The wing's **keystone chapter for the method**. Everywhere else in this wing, active inference is an abstraction laid over a system that was not built to expose it. A bat exposes it. A bat **emits energy at a metered cost in order to receive an informative return**, **changes the emission to resolve a specific uncertainty**, and does all of it in **Hz, dB, ms and metres** — quantities you can put a microphone on. This is the one animal where NA-02's expected-free-energy **epistemic term stops being a metaphor and becomes an instrument reading**. Every number below either carries a source you can check or is written NOT-MEASURED / NOT-SOURCED. Nothing here raises any UNI rung — a citation to sensory biology is never a UNI gate.

---

## Why this chapter is the keystone, stated as a claim that can fail

NA-02 decomposes expected free energy as `G(pi) = risk + ambiguity = −(epistemic) − (pragmatic)`. The **epistemic term** says: *an agent will pay to reduce uncertainty, before that reduction pays out in goal terms.* It is the whole reason active inference is not control theory with a prior. It is also the hardest term to see in a real animal, because information-seeking normally hides inside behaviour doing three other things at once.

A bat's call does not hide it. The call **costs** (measurable in joules and dB). The call **returns information and nothing else** — the echo does not feed the bat, warm it, or move it. And the call is **adjusted in flight, on a millisecond timescale, in the direction that reduces uncertainty about the hypothesis currently in question**. Emission cost paid for information return, both sides on a meter, is the epistemic term with wires attached.

The active-inference *reading* is a lens, fenced HYPOTHESIZED throughout. The measurements are not the lens; they stand whether or not the lens is any good.

## The one calculation: `lambda = c/f`, and why a bat cannot be a baritone

Take the speed of sound in air, `c ≈ 343 m/s` at 20 °C, 1 atm (standard acoustics; `c ≈ 331.3·sqrt(1 + T/273.15)` m/s — not primary-sourced in this pass). Wavelength is `lambda = c/f`. Read the ladder:

| `f` | `lambda = c/f` | What that size is |
|---|---|---|
| 10 kHz | **34 mm** | bigger than most moths |
| 20 kHz | 17 mm | a large moth's wing |
| 50 kHz | **6.9 mm** | a midge |
| 100 kHz | 3.4 mm | a small fly |
| 212 kHz | **1.6 mm** | a gnat |

At 50 kHz, `lambda = 343 / 50000 = 6.86 mm ≈ 7 mm`. **That single line is why bats are ultrasonic.** A target much smaller than the wavelength does not reflect a sound wave so much as get walked around by it — the returned energy collapses (the Rayleigh regime). An echolocator wanting an echo off a chironomid with a 9–12 mm wingspan cannot work at 10 kHz, where `lambda` is three times the animal. It has to shorten the ruler, and shortening the ruler *is* raising the frequency. There is no third option.

The measured range across species is consistent with exactly this pressure. Bat calls span roughly **9–11 kHz to 212 kHz** in **dominant (peak) frequency**, with aerial-feeding assemblages on four continents dominated by **20–60 kHz** (Fenton, Portfors, Rautenbach & Waterman 1998, *Can J Zool* 76(6):1174–1182, DOI 10.1139/z98-043 — **that 20–60 kHz assemblage result is what Fenton 1998 measures; the full span is NOT-CONFIRMED to that paper in this pass**). At the top, *Cloeotis percivali* is reported at a **212 kHz** carrier — `lambda = 1.6 mm`. At the bottom, *Euderma maculatum* calls at **~9–12 kHz** (Fullard & Dawson 1997, *J Exp Biol* 200:129–137) and eats **eared moths** — that low frequency is not about target size at all, but about being inaudible to the prey. One end of the range is set by physics, the other by an arms race.

**Two scope notes the range needs, or it is not a number.** First, **the endpoints are not the same measurand**: the 212 kHz figure is a CF *carrier*, the 9–12 kHz figure a *dominant/peak* frequency. For a CF bat the carrier is the dominant component, so the span is readable — but only if the metric is named, and it is named here rather than left to the reader. Second, **the floor is the same animal as the low endpoint**. The literature's canonical phrasing puts the floor at **11 kHz** *and names *E. maculatum* as the species setting it* — while this chapter's own `f_Euderma` row reports **9–12 kHz** across sources. An 11 kHz floor and a 9 kHz call by the species that sets that floor are one measurement reported at two precisions, not two findings. **The floor is therefore printed ~9–11 kHz, species-dependent**, instead of being contradicted two rows later by its own source species.

**Carry the citation chain honestly.** The 212 kHz figure is stated by Thiagavel, Santana & Ratcliffe (2017), *Sci Rep* 7:828, DOI 10.1038/s41598-017-00959-2, citing **Bell & Fenton (1984)**, *Behav Ecol Sociobiol* 15:109–114 — a paper about *Hipposideros ruber*. The primary *Cloeotis* measurement was **not confirmed in this pass**. Per **M22**, an upstream statement is not fresh evidence. The number is printed with its chain visible, not laundered.

**And now the part it would be dishonest to omit.** The wavelength argument is a *derivation*, it has been tested against real insects, and it did not fully survive. **Waters, Rydell & Jones (1995)**, *Behav Ecol Sociobiol* 37(5):321–328, DOI 10.1007/BF00174136, measured echo target strength of actual prey and found it **virtually independent of emitted frequency across 20–100 kHz** — contrary to models built on spheres and disks. Real insects are not spheres. So the wavelength argument explains why bats are not at 5 kHz; it does **not** cleanly explain the choice *within* the band bats actually use. OBSERVED-CONTESTED, not smoothed over: the chapter's best derivation and its most instructive partial defeat.

## What the frequency costs: the compromise the title of Fenton 1998 names

Frequency is not free. **Atmospheric absorption rises steeply with it.** Jakobsen, Brinkløv & Surlykke (2013), *Front Physiol* 4:89, DOI 10.3389/fphys.2013.00089, tabulate (from Lawrence & Simmons 1982 and ANSI 1995):

- 25 → 50 kHz: **0.7 → 1.7 dB/m** (20 °C, 50% RH)
- 45 → 90 kHz: **1.4 → 4 dB/m** (25 °C, 80% RH)

Put a target at 5 m — a 10 m round trip. At 45 kHz that is `10 × 1.4 = 14 dB` of absorption; at 90 kHz, `10 × 4 = 40 dB`. **Doubling the frequency costs 26 dB of round-trip absorption alone**, before spreading loss, before target strength. A bat buying resolution with frequency pays for it in range at a brutal exchange rate. Every echolocator sits somewhere on that curve; 20–60 kHz is where most of them sit. *Cloeotis* at 212 kHz has bought a 1.6 mm ruler and, by the trend, a very short reach — **its absorption coefficient at 212 kHz is NOT-MEASURED here**, and I will not extrapolate a curve past its sourced points to manufacture the number.

## Range is time: `2R = ct`

The echo carries range as **delay**. Sound goes out and comes back, so `2R = ct`, i.e. `t = 2R/c`:

| Target range `R` | Echo delay `t = 2R/c` |
|---|---|
| 0.1 m | 0.58 ms |
| 0.5 m | 2.9 ms |
| **1 m** | **5.8 ms** |
| 2 m | 11.7 ms |
| **5 m** | **29 ms** |
| 10 m | 58 ms |

The conversion constant is **5.83 ms per metre of range**. Everything downstream is bookkeeping against that number.

**CF vs FM falls straight out of it** — the two call architectures are two ends of the time–bandwidth trade:

- **FM (frequency-modulated sweep) is for ranging and resolution.** Matched-filter range resolution is `Δr = c/(2B)` for bandwidth `B` (standard sonar/radar theory; not primary-sourced in this pass). For a *single-frequency* pulse of duration `tau`, `B ≈ 1/tau`, so `Δr ≈ c·tau/2` — resolution is chained to duration, and a 0.5 ms tone gives `Δr = 343 × 0.0005 / 2 = 8.6 cm`. Sweep the same 0.5 ms across `B = 60 kHz` (an **illustrative input, not a sourced species value**) and `Δr = 343/(2 × 60000) = 2.9 mm` — a ~30× gain at identical duration. **FM buys resolution without paying duration.** That is what a sweep is *for*.
- **CF (constant-frequency tone) is for Doppler and flutter.** Frequency resolution runs the other way: `Δf ≈ 1/tau`. *Hipposideros armiger* — **a hipposiderid, not a rhinolophid horseshoe bat; the splice this chapter fences below starts here if the families are merged** — holds echo frequency to a standard deviation of **110 Hz** (Schoeppler, Schnitzler & Denzinger 2018, *Sci Rep* 8:4598, DOI 10.1038/s41598-018-22880-y). **Now the premise, stated out loud, because the arithmetic below is worthless without it:** 110 Hz is a measure of how tightly the bat *stabilises its own emission* — a motor-control statistic. It is **not** a measurement of the frequency structure the bat's *receiver* must resolve, and Schoeppler et al. do not claim it is. *If* the bat stabilises the echo to 110 Hz *because* 110 Hz is the scale it must resolve — **an inference, not a measurement** — then resolving structure at that scale needs `tau ≥ 1/110 s ≈ 9 ms`, and the CF component cannot be short. **The arithmetic bounds it, conditional on that premise; it forbids nothing until the premise is argued.** (Fourier resolution is a soft bound besides: coherent frequency *estimation* can beat `1/tau` at high SNR. Measured CF durations are NOT-SOURCED here; the bound is derived, not quoted — and deriving it from real CF durations, rather than from a control statistic standing in for a resolution requirement, is the better move once they are sourced.)

FM is a ruler. CF is a tachometer. A bat needing both carries a CF-FM call and pays for both.

## The pulse–echo overlap problem, derived rather than asserted

A call of duration `tau` is not a point in time; it is `c·tau` metres of air. The echo from range `R` starts arriving at `2R/c` after the call *starts*. The call is still going until `tau`. **Overlap-free ranging therefore requires `2R/c ≥ tau`, i.e. `R ≥ c·tau/2`.** Now put in the measured call durations from Moss & Surlykke (2010), *Front Behav Neurosci* 4:33, DOI 10.3389/fnbeh.2010.00033:

| Phase | Duration `tau` | Pulse length `c·tau` | Overlap-free only beyond `c·tau/2` |
|---|---|---|---|
| Search | 15–20 ms | 5.1–6.9 m | **2.6–3.4 m** |
| Approach | 2–5 ms | 0.69–1.7 m | **0.34–0.86 m** |
| Terminal buzz | 0.5–1 ms | 0.17–0.34 m | **8.6–17 cm** |

Read the right-hand column against the left. **The bat's call duration collapses by a factor of ~30 across the attack, and the overlap-free floor collapses with it, staying just under the closing target.** A search call that could not cleanly range anything nearer than 2.6 m would be blind at the moment of capture. The bat does not solve this with better processing; it **changes its own emission** so the question stays answerable. That is action taken to keep an inference well-posed, and it is measured in milliseconds.

## The terminal buzz — and the refutation of its obvious explanation

Closing on prey, a bat drives its call rate up to **beyond 160 calls/s** (Elemans, Mead, Jakobsen & Ratcliffe 2011, *Science* 333(6051):1885–1888, DOI 10.1126/science.1207309), with Moss & Surlykke reporting **up to ~170/s**. This is the **terminal buzz**: the measurable signature of an agent throwing its information rate to the ceiling at exactly the moment uncertainty is most expensive. In NA-02's terms, the epistemic term is being maximised precisely where the pragmatic term is about to be settled.

Now the part worth the whole section. The *obvious* explanation of the buzz ceiling is **pulse–echo overlap**: at pulse interval `PI` the unambiguous range is `c·PI/2`, so 160 calls/s (`PI = 6.25 ms`) implies `343 × 0.00625 / 2 = 1.07 m` — a tidy story in which the bat stops speeding up because it would start confusing echoes.

**That story is refuted.** Elemans et al. showed **laryngeal motor performance, not echo overlap, sets the ceiling**: bats have a previously unknown class of **superfast muscle** (the anterior cricothyroid, in *Myotis daubentonii*) producing positive work in cyclic contraction **up to 160 Hz, and in one case 200 Hz**. The constraint is the meat, not the mathematics. A clean, plausible, arithmetically correct hypothesis lost to a direct measurement of the actuator. **Record which one won.**

## Doppler-shift compensation: the sharpest measured instance of action-to-optimize-inference

This is the strongest thing in the chapter.

A horseshoe bat's cochlea has an **auditory fovea**: a grossly expanded frequency representation centred on a narrow **reference frequency**, with sharply tuned neurons overrepresented at that frequency throughout the auditory pathway (Schnitzler & Denzinger 2011, *J Comp Physiol A* 197(5):541–559, DOI 10.1007/s00359-010-0569-6). In *Rhinolophus ferrumequinum* the inferior colliculus overrepresents best frequencies of **83.0–84.5 kHz** (Schuller & Pollak 1979, *J Comp Physiol* 132:47–54, DOI 10.1007/BF00617731). The bat's model of the world is sharp in a **~1.5 kHz-wide slot** and blunt outside it.

Flying at the target ruins this. For a bat closing at speed `v` on a stationary reflector, the echo returns at `f_r = f_e·(c+v)/(c−v)`. At `v = 5 m/s` that factor is `348/338 = 1.0296` — an echo from an 83 kHz emission comes back at **85.4 kHz: ~2.4 kHz above the 83 kHz reference frequency, and roughly 1 kHz clear of the fovea's 84.5 kHz upper edge**. (Both numbers are correct and they are not the same number; "2.4 kHz above the fovea" would collapse a 1.5 kHz-wide band to its lower edge. The ~1 kHz is the one that carries the argument.) The bat has flown its own signal out of the only band where its model is precise.

**So the bat lowers its voice.** To land the echo back on 83.0 kHz it must emit `83000 / 1.0296 = 80.6 kHz` — dropping emitted frequency by **~2.4 kHz** (computed here). The *Rhinolophus* control literature established that the animal does exactly this. **Two quantities are involved and they are kept separate, because collapsing them manufactures a third that nobody measured:** rhinolophids and *P. parnellii* hold `F_echo` to a precision of **0.1–0.2% around `F_ref`** — the **band**, ≈83–166 Hz at `F_ref` = 83 kHz — and hold `F_ref` at approximately **150–200 Hz above `F_rest`** — the **offset**. Both are stated in Schoeppler et al. (2018), who also measured in-flight echo frequency held to **SD 110 Hz — 0.17% of the reference** in *H. armiger*.

**Sit with what that is.** The bat cannot move its fovea. So it moves the world's input into the fovea, by changing its own motor output, continuously, in closed loop, at 0.17% precision. **It is not adapting its model to its sensations. It is adapting its sensations to its model.** Nothing else in this wing is this literal.

**Type the connection to NA-02 correctly, because the obvious phrasing is a category error.** It is tempting to call this "precision, `gamma`". It is not `gamma`. NA-02's `gamma` is *policy* precision — the softmax inverse-temperature over policies, `sigma(−gamma·G)`, units nats⁻¹. The fovea is *sensory* precision: sharpness of the likelihood `p(o|s)`. The correct statement is narrower and better: NA-02's `G = risk + ambiguity`, where **ambiguity is the expected entropy of the likelihood**, `E_q(s|pi)[H[p(o|s)]]`. An action moving the echo into the band where `p(o|s)` is sharpest **lowers the ambiguity term of `G` directly**. DSC is an ambiguity-minimising action. That is the exact hook, and it is worth more than the loose one.

**Fence the splice.** The fovea width (83.0–84.5 kHz) is *R. ferrumequinum*; the 110 Hz DSC precision is *H. armiger*, a hipposiderid whose auditory fovea is reported as **less developed**. The comparison "the action is ~14× finer than the fovea is wide" is **illustrative across two species, not a within-animal measurement**. The within-species pairing is **NOT-MEASURED** here, and its falsifier is in the table.

## Reafference: predicting your own action's sensory consequence (cross-ref NA-04)

A bat emitting 140 dB SPL at 10 cm and then listening for an echo dozens of dB quieter has an obvious problem: **it is about to deafen itself with its own voice.**

It solves this in the shape NA-04's forward-model account describes — but **by efference copy, not by temporal precedence**, and the distinction is the whole of what Suga & Jen actually measured. Middle-ear muscle activity — chiefly the **stapedius** — is **synchronous with vocalisation**, not before it and not a reflex after it. In Suga & Jen's words (1975, *J Exp Biol* 62(2):277–311, in *Myotis lucifugus*), the muscles "received a message from the vocalization system when the bat vocalized, and contracted synchronously with vocalization," and "the duration of the contraction-relaxation was so short that the self-stimulation was attenuated, but the echoes were not." **The muscles are driven by a copy of the motor command, not by the sound that command produces.** That is the forward-model point, and it stands without any pre-vocal lead: the bat's ear is being told what the bat is about to do by the system doing it.

**The timings that paper reports are the timings of the mechanism it was ruling *out*.** Suga & Jen's latencies — **3–4 ms** (electromyogram) and **4–8 ms** (attenuation of the cochlear microphonic) — are *acoustic middle-ear-muscle **reflex*** latencies, and they are reported precisely in order to reject the reflex: "these muscles failed to attenuate orientation signals by the reflex." Reading those figures as a pre-vocal lead inverts the paper — it converts a refutation into its opposite. **Any lead time of muscle onset before call onset is NOT-SOURCED here**; see the table, where the claim is carried as an open row with its falsifier rather than as a number. Reported attenuation is **17–25 dB** (the spread is real and printed). Destroying the stapedius reportedly abolishes the effect (Henson 1965 — **cited by** the above, **not read in this pass**).

Then there is a second, separately sourced measurement. Jakobsen et al. (2013) report that during approach the bat's **receiver sensitivity falls by ~6 dB for each halving of target distance**, attributed to the same muscles — an **automatic gain control that tracks range**, measured in dB. That much is observed.

**What is *not* observed is the anticipation.** Reading this schedule as open-loop against an echo amplitude the bat *predicts* from its own closing geometry — rather than as a loop driven by echo amplitudes already arriving — is **HYPOTHESIZED**: this pass sources the 6 dB/halving relationship but no experiment discriminating a predicted-geometry drive from an echo-driven one. The gain schedule is the measurement; the forward model is the reading laid over it. The efference-copy result above is the chapter's actual evidence for prediction-not-reflex, and it is enough — this row does not need to be conscripted into carrying more than it weighs.

## Intensity: what the epistemic term actually costs, and the contest over it

The correct convention matters, and getting it wrong is a common defect. Source level is **dB SPL re 20 µPa at 0.1 m** (10 cm from the mouth) — Jakobsen et al. (2013).

- Open-space aerial hawkers: **~130 dB SPL**, up to and beyond **140 dB** (Surlykke & Kalko 2008, *PLoS ONE* 3:e2036, DOI 10.1371/journal.pone.0002036) — reported as the highest airborne levels for any animal.
- "Whispering" bats, long assumed to be ~70 dB, actually reach **110 dB SPL** (Jakobsen et al. 2013).

At 140 dB SPL the acoustic pressure amplitude at 10 cm is `20e-6 × 10^(140/20) = 200 Pa` (computed here) — about **0.2% of one atmosphere**, from a mammal weighing a few grams.

**Does that cost anything?** This is the chapter's live scientific dispute, and it resolves along an axis, which is the best kind:

- **Speakman & Racey (1991)**, *Nature* 350:421–423, DOI 10.1038/350421a0: mass-adjusted flight energy expenditure in echolocating bats was **not significantly different** from non-echolocating bats and birds. Title: *No cost of echolocation for bats in flight*. The mechanism offered is **coupling call emission to the wingbeat** — the call rides an exhalation the flight muscles are producing anyway. Holderied & von Helversen (2003), *Proc R Soc B* 270(1530):2293–2299, DOI 10.1098/rspb.2003.2487, found small and medium bats **match their maximum detection range to their wingbeat period** — the same clock serving both.
- **Voigt & Lewanzik (2012)**, *J Comp Physiol B* 182:831–840, DOI 10.1007/s00360-012-0663-x, re-tested it in the 5 g *Rhogeessa io*: cost of transport was **not related to pulse emission rate**, and flight power was **lower** than predicted if call cost were additive. Consistent with Speakman & Racey.
- **Currie, Boonman, Troxell, Yovel & Voigt (2020)**, *Nat Ecol Evol* 4(9):1174–1177, DOI 10.1038/s41559-020-1249-8, bounded it: costs are negligible **only for low call intensities**; **above 130 dB SPL (re 10 cm)** sound production becomes, in their word, exorbitant for small bats.

**So "echolocation is free during flight" is not wrong — it is scope-limited, and 2020 printed the scope.** Below ~130 dB the epistemic term is nearly free because it rides an action the animal is taking anyway; above it, the bat buys information with metabolism at a rate that caps how loud it can be. **The price of information is not zero and not constant. It is a function with a knee, and the knee has been measured.** For a method claiming agents trade energy for uncertainty reduction, that is about as good as nature gets.

## Flight: the membrane wing

Bat wings are not bird wings, and the difference is not decorative. A bat wing is a **thin skin membrane stretched over elongated arm and hand bones**, with the **digits themselves forming the leading and trailing edges** — compliant, anisotropically stiff (stiffest along the bones), carrying membrane-tensioning muscles found in no bird, and offering a far wider range of in-stroke morphological adjustment (Hedenström & Johansson 2015, *J Exp Biol* 218(5):653–663, DOI 10.1242/jeb.031203). A bird changes wing shape by moving feathers over each other. **A bat changes wing shape by changing the shape of the wing.**

**Strouhal (cross-ref NA-06).** `St = fA/U`. Taylor, Nudds & Thomas (2003), *Nature* 425:707–711, DOI 10.1038/nature02000, found flying and swimming animals — bats included — cruise in **0.2 < St < 0.4**, the band of high propulsive efficiency. The bat-specific measurement sharpens it: **Lindhe Norberg & Winter (2006)**, *J Exp Biol* 209(19):3887–3897, DOI 10.1242/jeb.02446, filmed *Glossophaga soricina* across 1.23–7.52 m/s and found `St = 0.17–0.22` near minimum-power speed (4–6 m/s), `St = 0.25–0.40` at 3.4–4 m/s, and `St = 0.5–0.68` below 3 m/s, where unsteady effects take over and lift/thrust production degrades. **The honest wrinkle: the efficient cruise sits slightly *below* the canonical 0.2 bound.** The band describes where animals cruise; it is not a law they obey.

**Wing loading and aspect ratio.** Norberg & Rayner (1987), *Phil Trans R Soc B* 316:335–427, DOI 10.1098/rstb.1987.0030, ran a PCA over 200+ species: **high aspect ratio → open air; low aspect ratio → clutter; low wing loading → slower flight.** The pattern lines up with the sonar — open-space bats are the loud, long-range ones. **The numerical ranges for wing loading in N/m² and aspect ratio are NOT-SOURCED in this pass and are therefore not printed here**, and bat aspect ratio is reported under both full-span and half-span conventions, so quoting one against the other is an error waiting to happen.

## Jamming, and the arms race

*Bertholdia trigona* is a palatable tiger moth that answers an attacking *Eptesicus fuscus* with ultrasonic clicks. **Corcoran, Barber & Conner (2009)**, *Science* 325(5938):325–327, DOI 10.1126/science.1174096, used ultrasonic recording plus high-speed infrared videography of live bat–moth interactions to show the clicks **jam** the bat's sonar — a controlled demonstration, not an inference from correlation. Corcoran, Barber, Hristov & Conner (2011), *J Exp Biol* 214:2416–2425, DOI 10.1242/jeb.054783, then discriminated among three candidate mechanisms — phantom echo, ranging interference, masking — and found bats **missed by ~15–20 cm, the distance predicted by ranging interference**. In the field, **Corcoran & Conner (2012)**, *J Exp Biol* 215(24):4278–4287, DOI 10.1242/jeb.076943: clicking moths captured **6.8%** of the time vs **71%** for silenced conspecifics — a **defence ratio of 10.4**. Fernández, Dowdy & Conner (2022), *J Exp Biol* 225(18):jeb244187, DOI 10.1242/jeb.244187, added a dose–response: **77% capture at 0% duty cycle**, odds of capture falling **~4% per 1% increase in moth duty cycle**, and a jamming window of about **2 ms before echo arrival**.

The other direction is on the same meter. An average noctuoid moth first hears *Eptesicus fuscus* at **20–25 m**, but *Euderma maculatum* at **less than 1 m** (Fullard & Dawson 1997). The spotted bat pays the wavelength penalty — a 34 mm ruler, hopeless for small targets — to buy 20+ metres of acoustic invisibility against eared prey. **That is why the bottom of the frequency range exists.** (Reviewed in ter Hofstede & Ratcliffe 2016, *J Exp Biol* 219(11):1589–1602, DOI 10.1242/jeb.086686.)

**The two-agent reading — an arms race as two agents each minimising their own surprise at the other's expense — is HYPOTHESIZED.** It is a story about the measurements, not a measurement. No coupled-agent free-energy model has been fitted to these data in this pass, and none is claimed.

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `c` | ≈343 | m/s | air, 20 °C, 1 atm; `c ≈ 331.3·sqrt(1+T/273.15)` | OBSERVED-REPLICATED *(standard reference; not primary-sourced in this pass)* | standard acoustics | Fetch a primary reference; a measured `c` outside 330–350 at stated conditions |
| `f_range` | **~9–11 to 212** | kHz | **dominant (peak) frequency of the strongest call component**, across species. Floor is **species-dependent, set by *E. maculatum*** (see `f_Euderma`) — printed ~9–11, not 11, so it does not contradict its own source species. The 212 kHz endpoint is a CF **carrier** (the dominant component *for a CF bat*, but not the same measurement as a peak-frequency estimate) | OBSERVED-REPLICATED (as a range) **/ span attribution NOT-CONFIRMED** | Thiagavel et al. 2017, *Sci Rep* 7:828. **Fenton et al. 1998's confirmed subject is the 20–60 kHz assemblage result, not the full span — the span is NOT-CONFIRMED to that paper in this pass and is no longer attributed to it** | A species outside the range **on the stated metric** under stated recording conditions; **and, separately: locate the 11–212 span in a primary or review source (Fenton 1998? ter Hofstede & Ratcliffe 2016?) and re-attribute this row to whichever carries it, or strike the span** |
| `f_mode` | **20–60** | kHz | aerial-feeding assemblages: Canada, Mexico, Brazil, Zimbabwe | OBSERVED-REPLICATED | Fenton et al. 1998 | A comparable assemblage not dominated by 20–60 kHz |
| `f_Cloeotis` | 212 | kHz | *Cloeotis percivali* carrier — **chain-flagged (M22)** | **OBSERVED-CONTESTED / NOT-CONFIRMED** | Thiagavel et al. 2017 **citing** Bell & Fenton 1984, *Behav Ecol Sociobiol* 15:109–114 (primary **not read in this pass**) | Read Bell & Fenton 1984; if the measurement is not there, the chain breaks |
| `f_Euderma` | **9–12** (also reported ~10.5, ~12.7) | kHz | *Euderma maculatum* dominant/peak frequency — **real spread across sources**. **This species is what sets the `f_range` floor**, which is why that floor is printed ~9–11 rather than 11: an 11 kHz floor and a 9 kHz call by the floor's own source species are one measurement at two precisions, not a contradiction to leave standing | **OBSERVED-CONTESTED** | Fullard & Dawson 1997, *J Exp Biol* 200:129–137; ~10.5 in Thiagavel et al. 2017 | Recording outside 9–13 kHz; or a study reconciling the reported values |
| `lambda@50kHz` | **6.9** | mm | `lambda = c/f`, c = 343 m/s | MODELED | Computed here | Arithmetic error, or `c` refuted |
| `lambda@212kHz` | 1.6 | mm | as above | MODELED | Computed here | as above |
| `lambda@10kHz` | 34 | mm | as above | MODELED | Computed here | as above |
| `TS(f)` **insects** | **~independent of f** across 20–100 kHz | dB | real prey items — **contradicts sphere/disk Rayleigh models** | **OBSERVED-CONTESTED** | Waters, Rydell & Jones 1995, *Behav Ecol Sociobiol* 37(5):321–8, DOI 10.1007/BF00174136 | Measure TS of real insects across 20–100 kHz and recover a strong `f` dependence |
| `alpha_atm` | **0.7 → 1.7** | dB/m | 25 → 50 kHz, 20 °C, 50% RH | OBSERVED-REPLICATED | Jakobsen, Brinkløv & Surlykke 2013, *Front Physiol* 4:89, DOI 10.3389/fphys.2013.00089, from Lawrence & Simmons 1982; ANSI 1995 | Re-measure at stated T/RH; values >2× off |
| `alpha_atm` | **1.4 → 4** | dB/m | 45 → 90 kHz, 25 °C, 80% RH | OBSERVED-REPLICATED | as above | as above |
| `ΔL_2f` | **26** | dB | round-trip absorption penalty, 45→90 kHz, R = 5 m (10 m path) | MODELED | Computed here from `alpha_atm` | Arithmetic error, or `alpha_atm` refuted |
| `alpha_atm@212kHz` | — | dB/m | absorption at *Cloeotis*'s carrier | **NOT-MEASURED** | not sourced in this pass | Fetch ANSI 1995 / Lawrence & Simmons 1982 and evaluate at 212 kHz |
| `t(R)` | **5.83** | ms per metre of range | `t = 2R/c`, two-way | MODELED | Computed here | Arithmetic error, or `c` refuted |
| `tau_search` | **15–20** | ms | search-phase call duration | OBSERVED-REPLICATED | Moss & Surlykke 2010, *Front Behav Neurosci* 4:33, DOI 10.3389/fnbeh.2010.00033 | Measured durations outside range for a search-phase FM bat |
| `tau_approach` | **2–5** | ms | approach phase | OBSERVED-REPLICATED | Moss & Surlykke 2010 | as above |
| `tau_buzz` | **0.5–1** | ms | terminal buzz | OBSERVED-REPLICATED | Moss & Surlykke 2010 | as above |
| `R_min` | **2.6–3.4 / 0.34–0.86 / 0.086–0.17** | m (search / approach / buzz) | overlap-free floor `R ≥ c·tau/2` | MODELED | Computed here from `tau` + `c` | Arithmetic error; or a bat ranging cleanly inside `c·tau/2` |
| `rate_buzz` | **>160** (up to ~170) | calls/s | terminal buzz repetition rate | OBSERVED-REPLICATED | Elemans et al. 2011, *Science* 333(6051):1885–8, DOI 10.1126/science.1207309; Moss & Surlykke 2010 | Recording of a terminal buzz capped well below 160/s |
| `f_muscle` | **up to 160; 200 in one case** | Hz | anterior cricothyroid, *Myotis daubentonii*, positive work in cyclic contraction | OBSERVED-REPLICATED | Elemans et al. 2011 | Repeat the work-loop assay; a ceiling well below 160 Hz |
| **buzz ceiling cause** | **laryngeal motor performance**, NOT pulse–echo overlap | — | *M. daubentonii* | OBSERVED-REPLICATED | Elemans et al. 2011 | A bat exceeding its measured muscle cycling limit; or overlap shown to bind first |
| `R_unamb@160/s` | **1.07** | m | `c·PI/2`, PI = 6.25 ms | MODELED | Computed here | Arithmetic error |
| `f_fovea` | **83.0–84.5** | kHz | *R. ferrumequinum* inferior colliculus, overrepresented best frequencies | OBSERVED-REPLICATED | Schuller & Pollak 1979, *J Comp Physiol* 132:47–54, DOI 10.1007/BF00617731 | Map IC best frequencies and find no overrepresentation |
| `SD_echo` | **110** (= 0.17% of `F_ref`) | Hz | *Hipposideros armiger* (**a hipposiderid — NOT a rhinolophid/horseshoe bat**), in-flight DSC precision. **An emission-control statistic: how tightly the bat stabilises `F_echo`. It is NOT a measured resolution requirement of the bat's receiver, and the source does not claim it is** — see `tau_CF,min`, which depends on reading it as one | OBSERVED-REPLICATED | Schoeppler, Schnitzler & Denzinger 2018, *Sci Rep* 8:4598, DOI 10.1038/s41598-018-22880-y | Onboard-mic replication with SD >5× larger |
| `drift_Frest/Fref` | up to **230 / 250** | Hz | *H. armiger*, within a session | OBSERVED-REPLICATED | Schoeppler et al. 2018 | as above |
| `band_DSC` | **0.1–0.2% of `F_ref`** (≈83–166 Hz at `F_ref` = 83 kHz) | % of `F_ref` | rhinolophids and *P. parnellii* — the **band**: precision within which `F_echo` is held around `F_ref`. **A different quantity from `offset_DSC` below; an earlier version of this row printed "~200 Hz band centred ~150 Hz above resting", which split the single 150–200 Hz *offset* figure into a width and a centre and invented a band nobody measured** | OBSERVED-REPLICATED | Schoeppler et al. 2018, *Sci Rep* 8:4598, DOI 10.1038/s41598-018-22880-y: "Rhinolophids and P. parnellii maintained Fecho with a high precision of only 0.1–0.2% around Fref" | Re-measure; a band >2× wider under the same paradigm |
| `offset_DSC` | **~150–200** | Hz (`F_ref` above `F_rest`) | *R. ferrumequinum*, *R. euryale*, *P. parnellii*, in flight — the **offset**, not the band | OBSERVED-REPLICATED | Schoeppler et al. 2018: "In flight, Rhinolophus ferrumequinum, Rhinolophus euryale, and P. parnellii accurately maintain Fref at approximately 150–200 Hz above Frest" | Re-measure; an offset outside 100–250 Hz under the same paradigm |
| `Δf_emit` | **~2.4** | kHz (lowering) | bat at v = 5 m/s, `f_r = f_e(c+v)/(c−v)`, `F_ref` = 83 kHz | MODELED | Computed here | Arithmetic error; or a DSC bat that does not lower emission when closing |
| `tau_CF,min` | **≳9** | ms | derived bound: `Δf ≈ 1/tau ≤ 110 Hz` — **soft** (coherent estimation can beat 1/tau) **and conditional on an unmeasured premise: that the 110 Hz emission-control SD equals the flutter-resolution scale the receiver must resolve. The premise is an inference, not a measurement, and the bound is worth exactly what the premise is worth** | MODELED *(premise HYPOTHESIZED)* | Computed here from `SD_echo` | Show CF-FM flutter discrimination at that precision with `tau` ≪ 9 ms; **or show that the required flutter-resolution scale differs from the DSC control SD — which collapses the premise and with it this row**; best closure is to source real CF durations and compare rather than derive |
| **fovea width vs DSC precision, same animal** | — | — | within-species pairing | **NOT-MEASURED** | two species spliced here (*R. ferrumequinum* fovea, *H. armiger* DSC) | Measure fovea width and DSC precision in one species |
| `Δr = c/(2B)` | 2.9 (at B = 60 kHz) / 8.6 (at B ≈ 1/tau, tau = 0.5 ms) | mm / cm | matched-filter range resolution — **B = 60 kHz is an illustrative input, not a species value** | MODELED *(standard sonar theory; not primary-sourced)* | Computed here | Cite a primary text; or a species FM bandwidth that moves the number |
| **bat range-discrimination threshold** | — | — | measured psychophysics (the "jitter" literature) | **NOT-SOURCED in this pass** | — | Read the jitter experiments and their replication attempts before quoting any threshold |
| `SL_open` | **~130, up to and beyond 140** | dB SPL **re 20 µPa @ 0.1 m** | open-space aerial-hawking bats | OBSERVED-REPLICATED | Surlykke & Kalko 2008, *PLoS ONE* 3:e2036, DOI 10.1371/journal.pone.0002036; Jakobsen et al. 2013 | Calibrated on-axis recording well below 130 dB for an open-space hawker |
| `SL_whisper` | **up to 110** (not ~70) | dB SPL re 20 µPa @ 0.1 m | "whispering" bats | OBSERVED-REPLICATED | Jakobsen et al. 2013 | Calibrated recording capping at ~70 dB |
| `p@140dB` | **200** | Pa (≈0.2% of 1 atm) | `p = 20e-6 × 10^(SL/20)` at 0.1 m | MODELED | Computed here | Arithmetic error |
| `t_reflex` | **3–4** (EMG) / **4–8** (cochlear microphonic) | ms | acoustic middle-ear-muscle ***reflex*** latency, *M. lucifugus* — **reported by the authors in order to REJECT the reflex as the mechanism: too slow to attenuate the outgoing call.** "its shortest latency in terms of electromyograms and of the attenuation of the cochlear microphonic was 3-4 and 4-8 msec, respectively, so that these muscles failed to attenuate orientation signals by the reflex" | OBSERVED-REPLICATED | Suga & Jen 1975, *J Exp Biol* 62(2):277–311 | Re-measure reflex latency; a latency short enough for the reflex to attenuate the emission after all |
| **MEM timing vs vocalisation** | **synchronous** — driven by an **efference copy**, not by the sound and not by a pre-vocal lead | — | stapedius/tensor tympani, *M. lucifugus* | OBSERVED-REPLICATED | Suga & Jen 1975: the muscles "received a message from the vocalization system when the bat vocalized, and contracted synchronously with vocalization" | EMG showing muscle onset leading or lagging call onset, with a stated sign |
| **MEM pre-vocal lead time** | — | ms | onset of middle-ear-muscle contraction **relative to call onset**, with a sign | **NOT-SOURCED in this pass** | — **Struck: an earlier version of this row printed "4–6 ms before vocalisation" and "8.8 ± 2.2 ms" as an unresolved discrepancy. Neither figure is in Suga & Jen 1975 (the row's only citation), the 8.8 ± 2.2 could not be sourced anywhere in this pass, and Suga & Jen report the opposite sign — "synchronously". Two unsourced numbers dressed as a live controversy is not a contested row; it is a fabrication with a hedge on it** | Find an EMG study reporting MEM onset relative to call onset **with a stated sign** |
| `A_MEM` | **17–25** | dB attenuation of self-generated signal | middle-ear muscle contraction during emission | OBSERVED-REPLICATED *(spread real; some sources report ~20–30)* | Suga & Jen 1975; Henson 1965 (**cited by**, not read here) | Measure with stapedius intact vs ablated |
| `AGC` | **~6** | dB sensitivity drop per halving of target distance | approach phase, attributed to middle-ear muscles | OBSERVED-REPLICATED | Jakobsen et al. 2013, citing Suga & Jen 1975 | Measure receiver gain vs range and find no schedule |
| **cost of echolocation in flight** | **negligible at low intensity; exorbitant above ~130 dB SPL @ 0.1 m for small bats** | — | *Rhogeessa io* (5 g); *Pipistrellus nathusii* | **OBSERVED-CONTESTED → resolved along intensity** | Speakman & Racey 1991, *Nature* 350:421–3, DOI 10.1038/350421a0; Voigt & Lewanzik 2012, *J Comp Physiol B* 182:831–40, DOI 10.1007/s00360-012-0663-x; **Currie et al. 2020, *Nat Ecol Evol* 4(9):1174–7, DOI 10.1038/s41559-020-1249-8** | Measure flight metabolic rate vs call intensity in a third species; a knee absent, or at a very different SPL |
| `rate_pulse,flight` | **19.7 ± 2.7** (range 15.3–25.8) | pulses/s | *Rhogeessa io*, in flight (non-buzz) | OBSERVED-REPLICATED | Voigt & Lewanzik 2012 | Replication outside range |
| `St_cruise` | **0.2–0.4** | dimensionless | flying + swimming animals at cruise, bats included | OBSERVED-REPLICATED | Taylor, Nudds & Thomas 2003, *Nature* 425:707–11, DOI 10.1038/nature02000 | A cruising animal well outside the band under the same `St = fA/U` convention |
| `St_Glossophaga` | **0.17–0.22** (4–6 m/s); **0.25–0.40** (3.4–4 m/s); **0.5–0.68** (<3 m/s) | dimensionless | *Glossophaga soricina*, wind tunnel, 1.23–7.52 m/s | OBSERVED-REPLICATED | Lindhe Norberg & Winter 2006, *J Exp Biol* 209(19):3887–97, DOI 10.1242/jeb.02446 | High-speed replication moving the bands |
| **wing loading / aspect ratio numeric ranges** | — | N/m² / dimensionless | bats | **NOT-SOURCED in this pass** | Norberg & Rayner 1987 pattern is sourced; the numbers are not | Read Norberg & Rayner 1987, *Phil Trans R Soc B* 316:335–427, DOI 10.1098/rstb.1987.0030; state full- vs half-span convention |
| **AR/wing-loading pattern** | high AR → open air; low AR → clutter; low wing loading → slower flight | — | PCA over 200+ species | OBSERVED-REPLICATED | Norberg & Rayner 1987 | Re-run on a modern phylogeny with phylogenetic correction; pattern vanishes |
| `capture_clicking` | **6.8** vs **71** (silenced) | % capture success | *Bertholdia trigona* vs *Eptesicus fuscus*, **field** | OBSERVED-REPLICATED | Corcoran & Conner 2012, *J Exp Biol* 215(24):4278–87, DOI 10.1242/jeb.076943 | Field replication with a defence ratio near 1 |
| `defence_ratio` | **10.4** (= 71/6.8) | dimensionless | as above | MODELED | Computed by Corcoran & Conner 2012 from their own rates | as above |
| `miss_distance` | **~15–20** | cm | jammed bats; matches **ranging-interference** prediction | OBSERVED-REPLICATED | Corcoran, Barber, Hristov & Conner 2011, *J Exp Biol* 214:2416–25, DOI 10.1242/jeb.054783 | A method discriminating the three hypotheses and favouring phantom echo or masking |
| `dose_response` | **77%** capture at 0% duty cycle; odds **−4% per +1%** duty cycle | % | *E. fuscus*, playback | OBSERVED-REPLICATED | Fernández, Dowdy & Conner 2022, *J Exp Biol* 225(18):jeb244187, DOI 10.1242/jeb.244187 | Replicate the dose–response and find no slope |
| `t_jam` | **~2** | ms window before echo arrival | click must land inside it to jam | OBSERVED-REPLICATED | Fernández et al. 2022 | Vary click timing; jamming persists far outside 2 ms |
| `d_detect,moth` | **20–25** (*E. fuscus*) vs **<1** (*E. maculatum*) | m | average noctuoid moth's detection distance | OBSERVED-REPLICATED | Fullard & Dawson 1997 | Neurophysiology giving a different threshold; a moth detecting *E. maculatum* at >5 m |
| `f_click,B.trigona` | up to **4,500** | clicks/s | *Bertholdia trigona* — **chain-flagged** | **NOT-CONFIRMED** | tertiary source citing Corcoran et al. 2009; **primary not read in this pass** | Read Corcoran et al. 2009 (*Science* 325:325–7) and confirm or strike |

## Falsifier (operable)

**The chapter's structural claim:** *a bat's call parameters are not fixed traits but state-dependent actions, and each one moves in the direction that keeps a specific inference well-posed — with the emission cost, the parameter change, and the uncertainty being resolved all separately measurable.*

**It is refuted by exhibiting an echolocating bat that hunts successfully with a call whose duration, rate, intensity and frequency do not covary with target range and closing speed** — specifically: one that keeps `tau` at search-phase values (15–20 ms) through the terminal approach while ranging targets inside `c·tau/2`, or a CF-FM bat that lets its echo drift out of its measured fovea while continuing to discriminate flutter at the same precision. Every measured phase transition (search → approach → buzz), every DSC trace, and the 6 dB/halving gain schedule are the claim's exposed surface. **They are all recordable with a calibrated microphone and a high-speed camera. Go and record one.**

Secondary falsifiers are row-local: any number found outside its stated scope under its stated conditions moves **that row only**. A refuted row does not refute the chapter. A bat that does not adapt its emission does.

**A cheaper falsifier, for the impatient:** the buzz-ceiling result already shows the method works. The overlap hypothesis was elegant, arithmetically correct, and wrong. It lost to a work-loop assay on a muscle. If the structural claim above is doing real work, more of it should lose the same way.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **NEGATIVE — "pulse–echo overlap sets the terminal-buzz call-rate ceiling."** Arithmetically tidy (`c·PI/2 = 1.07 m` at 160 calls/s), widely repeatable, **refuted**: Elemans et al. 2011 measured the actuator and found laryngeal motor performance binds first. Recorded because it is exactly the failure mode this wing exists to catch — a derivation that predicts the right number for the wrong reason.
- **NEGATIVE / OBSERVED-CONTESTED — the naive wavelength argument, applied *within* the bat band.** `lambda = c/f` explains why echolocators are ultrasonic rather than sonic. It does **not** survive contact with real prey: Waters, Rydell & Jones (1995) measured insect target strength as **frequency-independent over 20–100 kHz**, against sphere/disk model predictions. The chapter's best derivation is scope-limited and the scope is printed.
- **NEGATIVE / sign reversal — "middle-ear muscle contraction begins *before* vocalisation."** Carried in an earlier version of this chapter as the load-bearing premise of the whole reafference section, cited to Suga & Jen 1975. **The cited paper says the opposite**: the muscles "contracted synchronously with vocalization." Jen & Suga 1976 (*Science*, DOI 10.1126/science.1251206) report middle-ear muscle action potentials **~3 ms *after*** those of the laryngeal muscles; the Frontiers 2021 review (DOI 10.3389/fevo.2021.661216) has stapedius contraction "coincident with the onset of the out-going signal." **Nothing found says "before."** The error's anatomy is worth recording: Suga & Jen's *reflex* latencies (3–4 / 4–8 ms), which the paper reports **in order to reject the reflex**, were re-signed into a pre-vocal lead — a refutation flipped into its opposite and then used as evidence. The forward-model reading survives on the paper's actual finding (**efference copy, not reflex**), which never needed the lead. Recorded because the failure was invisible: the sentence read as more precise, not less.
- **NEGATIVE / fabricated precision — "8.8 ± 2.2 ms."** Printed alongside "~4–6 ms" as an unresolved discrepancy "also reported in this lineage," under a row citing only Suga & Jen 1975. **Neither number is in that paper, and the 8.8 ± 2.2 could not be sourced anywhere in this pass.** The `±` term did the damage: it reads as an instrument talking. **A hedge is not a citation** — "the discrepancy is NOT-RESOLVED and both are carried" dressed two unsourced values as a live controversy, which is strictly worse than printing one, because it borrows the chapter's own honesty vocabulary to launder them. Both struck; the row is now open with a falsifier.
- **NEGATIVE / convention trap — mixing dB conventions.** Source levels appear as **rms SPL** and as **peak-equivalent (pe) SPL** (e.g. Holderied & von Helversen 2003 report up to 133 dB **pe** SPL). These are **not interchangeable** and averaging across them is an error. Any dB figure without `re 20 µPa` **and** a reference distance **and** rms-vs-pe is not a number.
- **NEGATIVE / convention trap — aspect ratio.** Bat aspect ratio is reported under both **full-span** and **half-span** conventions. A "half-span AR of 2.75–3.75" and a "full-span AR of 5.5–7.5" can describe the same animal. Quoting one against the other manufactures a difference that is not there.
- **NEGATIVE / scope trap — "echolocation is free for flying bats."** True as measured (Speakman & Racey 1991; Voigt & Lewanzik 2012) and **false above ~130 dB SPL @ 0.1 m for small bats** (Currie et al. 2020). Quoting the 1991 title without the 2020 bound is a scope error, not a citation.
- **INADMISSIBLE — "bats prove that consciousness/intention is required for intelligent behaviour."** Nagel's question (what it is like to be a bat) is a real philosophical question and is **not** answered, addressed, or bounded by any measurement in this chapter. As a claim about the measurements, it names no observation that could refute it. Recorded, not mocked: it is a good question in the wrong ledger.
- **INADMISSIBLE — "bat sonar demonstrates a natural implementation of the free-energy principle."** As stated, unfalsifiable: no observation is specified that would show a bat *not* implementing it. The admissible version is narrow and is what this chapter claims: **specific measured behaviours (DSC, call-duration collapse, the buzz, the gain schedule) are consistent with ambiguity-minimising action, and the fit has not been quantitatively tested here.** The difference between those two sentences is the whole method.
- **NOT-CONFIRMED (M22 chain flags):** the *Cloeotis percivali* 212 kHz primary measurement (chain: Thiagavel 2017 → Bell & Fenton 1984, unread here); the *B. trigona* 4,500 clicks/s figure (tertiary → Corcoran et al. 2009, unread here); **the 11–212 kHz span's attribution — Fenton et al. 1998's confirmed subject is the 20–60 kHz assemblage result, and the span was not confirmed to that paper in this pass** (closure: locate the span in Fenton 1998 or in a review that carries it, and re-attribute). All printed **with the chain visible**. Closure: read the primaries.
- **NOT-SOURCED in this pass:** numeric wing-loading and aspect-ratio ranges; species FM sweep bandwidths; CF component durations; a primary reference for `c` in air; bat range-discrimination ("jitter") thresholds; the Corcoran et al. 2009 in-paper capture statistics (the 2012 field figures are used instead, and are sourced); **any pre-vocal lead time of middle-ear-muscle onset relative to call onset** (the previously printed "~4–6 ms" and "8.8 ± 2.2 ms" are struck — see the NEGATIVE ledger above); **whether the anticipatory reading of the 6 dB/halving gain schedule can be discriminated from an echo-amplitude-driven one** (the schedule itself is sourced to Jakobsen et al. 2013; only the anticipation is unsourced).
- **NOT-MEASURED:** atmospheric absorption at 212 kHz; within-species pairing of fovea width and DSC precision; any fitted coupled-agent free-energy model of the bat–moth arms race.

## HONEST FENCE — MODELED

This chapter is fenced **MODELED**. Most individual rows are OBSERVED-REPLICATED; several are OBSERVED-CONTESTED, NOT-SOURCED, or NOT-MEASURED, and carry their own class. But the **chapter as an artifact** composes measured constants through stated assumptions — `c = 343 m/s` at 20 °C (echolocation happens at other temperatures and humidities, and every derived metre moves with `c`); a stationary reflector in the Doppler algebra; free-field spherical spreading; matched-filter resolution bounds that assume a receiver the bat may or may not implement. **The assumptions are the fence.** Change `c` by 5% and every range in the chapter moves by 5%; the conclusions survive because they turn on the *structure* — that resolution trades against range, that duration trades against overlap — not on the prefactors.

The **active-inference reading is HYPOTHESIZED throughout and is a lens, not a finding.** No `G(pi)` has been computed for any bat here. No policy space has been enumerated, no preference distribution `C` specified, no `gamma` fitted. The claim is the weaker and honest one: **these measured behaviours have the shape the epistemic and ambiguity terms describe, and the shape is close enough to be worth testing.** The measurements are the asset and they stand alone. If the lens were withdrawn tomorrow, DSC would still hold the echo to 110 Hz.

Per **Gould & Lewontin (1979), "The Spandrels of San Marco and the Panglossian Paradigm"**: none of this establishes that any bat trait is an optimum. Phylogenetic inertia, drift, developmental constraint and frozen accidents produce traits that solve nothing, and the bat literature has its own candidates — a larynx that had to be repurposed, a cochlea that cannot move its fovea and forces the animal to compensate with motor output instead. **Nature's authority here is precise and limited: it already ran the search under real physical constraints and deleted the failures.** Convergence — bats and dolphins arriving independently at broadband clicks and range-from-delay — is evidence of a constraint-optimum. It is a **hypothesis generator**, never a proof. Per repo rule **M7**, any sonar or active-sensing design taken from this chapter must beat a **tuned conventional baseline** on a **pre-registered metric**, with a discriminator that collapses the claimed gain, or it is recorded **NEGATIVE**. "Bats do it this way" is not an argument. It is a place to start looking.

## Not claimed

- **Not claimed:** that a bat is conscious, aware, or has experience. This chapter takes no position on Nagel's question and produces no evidence bearing on it. It is a permanent OPEN QUESTION, in a different ledger.
- **Not claimed:** **that a bat computes expected free energy.** Nothing here shows a bat evaluating `G(pi)` over a policy space, or anything isomorphic to it. The bat emits, listens, and adjusts. "Minimising the ambiguity term" is *our description of its behaviour*, in our vocabulary, for our purposes. **The bat is not doing our arithmetic.** Anyone who reads this chapter as evidence that active inference is *implemented* in a bat brain has crossed the exact lane the chapter was written to hold.
- **Not claimed:** that the active-inference reading is required to explain any measurement here. Classical sensorimotor control, signal-detection theory and plain optimal-foraging accounts predict much of it. **No discriminating experiment separating those accounts from the active-inference account is offered, and none is known to me in this pass.** Until one exists, the lens earns nothing it has not paid for.
- **Not claimed:** that DSC is `gamma` (policy precision, NA-02). It is an action that lowers the **ambiguity** term by moving sensory input into a high-precision likelihood band. The two precisions are different objects with different units. **Conflating them is a category error and this chapter refuses it.**
- **Not claimed:** any bat range-discrimination threshold. The psychophysics is contested and NOT-SOURCED here.
- **Not claimed:** any numeric bat wing loading or aspect ratio. NOT-SOURCED here; the *pattern* is sourced, the *numbers* are not, and the convention trap is live.
- **Not claimed:** that the bat–moth arms race has been modelled as coupled surprise minimisation. That reading is HYPOTHESIZED and unfitted.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** Reading Elemans et al. 2011 does not make any UNI claim proven, designed, or built. The NATURA vocabulary (OBSERVED-REPLICATED / OBSERVED-CONTESTED / MODELED / HYPOTHESIZED / INADMISSIBLE / NOT-MEASURED) and the UNI ledger vocabulary (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. **This chapter contains zero UNI claims.**
- **QUAESTIO-APERTA:** "full human" and "beyond human" appear nowhere here as a target, milestone, or deliverable. They are permanent open questions. A bat has been running measurable active sensing for tens of millions of years and it has no bearing on them whatsoever.


<!-- ===== END cookbook/recipes-natura/CN-10-bats.md ===== -->

