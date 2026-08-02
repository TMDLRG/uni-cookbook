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
