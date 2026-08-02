# NA-05 — The ratios: allometry and scaling laws across 20+ orders of magnitude

> **What you are reading.** How a quantity changes when size changes, and how to carry that across scales without lying. The exponent is the science; the prefactor is the engineering. The flagship case — Kleiber's law — is real, useful, and genuinely disputed, and this chapter carries the dispute at full strength rather than resolving it by preference. Every number below either carries a source you can check or is written NOT-MEASURED. **A nature citation is never a UNI gate.** This chapter contains zero UNI claims and raises no rung.

---

## The method, and why the exponent is the only part that travels

Take a quantity `Y` and a body mass `M`. The allometric form is `Y = aM^b`, which on logarithms is a straight line:

```
log Y = log a + b · log M
```

`b = 1` means `Y` tracks mass exactly — **isometry**. Any other `b` is **allometry**: shape or function must change with size, because it cannot stay the same.

Here is why `b` matters and `a` does not, in one line. Switch mass from grams to kilograms, `M' = M/1000`. Then `Y = aM^b = a·1000^b·(M')^b`. The prefactor moved by a factor of `1000^b`. **The exponent did not move at all.** `b` is dimensionless and unit-invariant; `a` carries units and is an artifact of your bookkeeping. So the exponent is a candidate statement about nature, and the prefactor is a statement about your build. Both are needed to compute a magnitude; only one of them is the science.

This has a sharp corollary that most of this chapter's disputes turn on: **`log M` is not defined for a dimensional quantity.** What you actually fit is `log(M/M₀)` for some implicit scale `M₀` (usually 1 g). For a straight line this is harmless — the choice of `M₀` moves the intercept and nothing else, because a line has no preferred origin. The moment your model is *not* a line, `M₀` stops being harmless. Hold that thought.

## The flagship: Kleiber's law, and why it is OBSERVED-CONTESTED

Max Kleiber found that basal metabolic rate scales as roughly `M^(3/4)` (Kleiber 1932, *Hilgardia* 6:315–353). **Based on 13 data points** (as reported by Kolokotrones et al. 2010, *Nature* 464:753–756). The competing claim is older: Rubner (1883) argued from surface area — heat is lost through a surface `∝ L²`, mass grows `∝ L³`, so metabolism should track `M^(2/3)`. Rubner's argument is not naive. It is dimensional analysis, and dimensional analysis is usually right.

Nearly a century later, here is the actual state of the evidence. These are careful studies by competent people on overlapping data:

| Study | Exponent | 95% CI | n | Verdict |
|---|---|---|---|---|
| Savage et al. 2004, **binned** | 0.737 | 0.711–0.762 | 52 bins | includes 3/4, excludes 2/3 |
| Savage et al. 2004, **unbinned** | 0.712 | 0.699–0.724 | 626 spp. | **excludes 2/3 AND 3/4** |
| White & Seymour 2003 (interspecific) | 0.68 | *not read in this pass* | 619→469 spp. | excludes 3/4, includes 2/3 |
| White & Seymour 2003 (interordinal) | 0.65 | *not read in this pass* | **15 orders** (17 before exclusions) | excludes 3/4 |
| White & Seymour 2005, true BMR | 0.686 | ±0.014 | n=469 — **the same fit as row 3** | excludes 3/4, ~excludes 2/3 |
| White & Seymour 2005, thermoneutral RMR | 0.712 | ±0.013 | — | **excludes both** |

*(The Savage rows are quoted from search-indexed full text; the PDF returned 403 and was not opened here — see the retrieval-route disclosure below. They are load-bearing, so they are flagged, not laundered.)*

*(**Count the papers, not the rows — this table invites the error it exists to expose.** These six rows are **three papers**. Rows 1–2 are one Savage et al. fit, binned and unbinned. Rows 3 and 5 are **the same n=469 regression at two roundings**: the 2005 figure is White & Seymour restating their own 2003 result in their own review, which is not replication. Row 6 changes the *rate definition*, not the dataset. So: three papers over two overlapping compilations of the same literature. Six rows of rounding-level agreement are not six independent corroborations, and reading them as such is exactly the move the paragraph immediately below catches for Savage — and then failed to apply to rows 3–6.)*

Read the first two rows again. **They are the same paper.** Savage et al. (2004), *Functional Ecology* 18:257–282, is titled *The predominance of quarter-power scaling in biology*. Its own fit to all 626 unbinned species yields a confidence interval, `[0.699, 0.724]`, that **rejects 3/4**. The 3/4 conclusion arrives only after binning by 0.1 log-unit mass intervals — a defensible correction for a dataset over-weighted toward small mammals, but a *choice*, and the choice is what produces the headline.

This is the repo's **M2** in the wild: the verdict is the CI bound excluding the threshold, never the point estimate. Point estimates of 0.712 and 0.737 look like agreement. Their confidence intervals reach opposite verdicts.

Meanwhile the "3/4 is typical" evidence dissolves on contact with its own spread. Glazier (2005), *Biological Reviews* 80:611–662, re-examines Peters's (1983) compilation of 146 allometric relations: mean `b = 0.738 ± 0.018`, satisfyingly close to 0.75 — but the distribution runs from **<0.5 to >1.0**, and while 49% of exponents fall in 0.7–0.8, **51% fall outside it**. The compilation is also 72% vertebrate (117/162) and 44% birds and mammals (72/162), in a world where most animals are invertebrates. Intraspecific scaling is worse: Withers's (1992) sample of 220 species spans `b = 0.3 to 1.8`, mean 0.724, **mode 0.667**. Dodds, Rothman & Weitz (2001), *J Theor Biol* 209:9–27, treated 2/3 as the null and found little reason to reject it — while noting a systematic *increase* in the exponent at larger masses. That observation was the tell.

## The resolution, and the objection to the resolution

Kolokotrones et al. (2010) fitted McNab's 637-species mammalian dataset (6 orders of magnitude in mass; 447 species with body temperature, 5 orders) to a quadratic in log-space:

```
log₁₀B = b₀ + b₁log₁₀M + b₂(log₁₀M)²
```

The quadratic term is not marginal: `b₂ = 0.0322 ± 0.0053`, `P = 9.0 × 10⁻¹⁰` (n = 636, mass in grams, B in watts). The relationship has **convex curvature on a log-log plot. It is not a power law at all.**

The consequence is computable. The local slope is the derivative, `b₁ + 2b₂log₁₀M`. Using their temperature-corrected fit (`b₁ = 0.5371`, `b₂ = 0.0294`), the local slope is `0.5371 + 0.0588·log₁₀M(g)`:

| Local slope | Mass at which it holds |
|---|---|
| 0.57 | ~3.6 g (a shrew) |
| **2/3** | **~160 g** |
| **3/4** | **~4.2 kg** |
| 0.87 | ~460 kg |
| 1.0 | ~7.4 × 10⁷ g ≈ 74 t — **EXTRAPOLATED, ~2.2 decades past the data** |

*(Computed here; reproduces the 0.57→0.87 range Kolokotrones et al. report over their fitted data, and their ~10⁸ g estimate for where the slope reaches 1.)*

*(**Say the word — rule 1, applied to this chapter.** The fitted data end at local slope **0.87, ~460 kg**: Kolokotrones et al. report the slope rising "from 0.57 to 0.87 over the range of the fitted data". The last row therefore sits **~2.2 decades beyond the fitted range** and is an **extrapolation**, which is rule 5's "#1 way scaling arguments fail" committed in this chapter's own table. Kolokotrones et al. hedge it twice themselves, and both hedges belong here: the slope rising "without bound" "**may be due to the paucity of data for large animals**", and the size-limit reading is prefaced "**If this is correct**". The row is kept because it is interesting, and flagged because it is unearned.)*

**There is no exponent.** There is a curve. Fit a line to a mouse-heavy dataset and you get 2/3; fit one to a dog-and-up dataset and you get 3/4. Both fits are locally correct and globally meaningless. Kolokotrones et al. state the mechanism directly: datasets with fewer large mammals exhibit smaller exponents. That is *exactly* the difference between White & Seymour's data and Savage et al.'s binned data. Neither team was incompetent. Both were fitting a line to a curve.

**Now the honest counterweight, because this resolution is itself contested.** MacKay (2011), *J Theor Biol* 280(1):194–196, raises the `M₀` problem flagged above. A parabola *does* have a preferred origin. Under a change of mass scale, `b₂` is invariant but `b₁` shifts — so, in MacKay's assessment, no meaning attaches to the values or *P*-values of `b₁` in Kolokotrones's Table 1; they are artifacts of choosing `M₀ = 1 g`. (Only the *local slope* and `b₂` survive a unit change — which is why the table above is stated in local slopes at named masses, not in `b₁`.) MacKay adds three more receipts: the quadratic buys `R²` from 0.958 to **0.961** — roughly one-tenth of the residual variance, a very small purchase; Hayssen & Lacy (1985) fitted the same log-quadratic model 25 years earlier and rejected it in favour of separate linear models per Order; and if you instead test the residuals of the best linear model **Order by Order**, only the Rodentia show a significant quadratic (`p = 0.02`, 0.02 of variance). **That last receipt has to be quoted with the concession sitting one sentence earlier in MacKay's own paragraph:** *"If one does this for all the eutheria, the quadratic term remains significant."* MacKay's own preferred test, run on the pooled eutherian data, **leaves the curvature standing**; only decomposing by Order weakens it. So the objection is that curvature may be a **between-Order artifact** — not that MacKay's test kills it. Most pointedly: strip two metabolically peculiar species from McNab's marsupials and the remaining **70 species fit `k = 0.75 ± 0.01` with `R² = 0.990`**. Kleiber's law is nearly exact — for marsupials.

**And the comment drew a published reply on the facing pages.** A chapter that carries Kozlowski → Brown → Kozlowski below has to carry this exchange to its end too, or it is selecting the side that supports its own fence. Deeds, Savage & Fontana (2011), *J Theor Biol* 280:197–198 — **three of Kolokotrones et al.'s own four authors, so a rebuttal by the accused, not an independent corroboration** — answer MacKay's three points. On `b₁`: the artifact is **conceded, and argued irrelevant**, because *"the only parameter necessary for the assessment of curvature in the data is `b₂`, which MacKay himself agrees is scale-invariant"*, so *"any scale dependence of `b₀` or `b₁` is irrelevant with regard to the conclusions we draw."* Read carefully, that **abandons `b₁` rather than rescuing it** — and it is the same move this chapter already made by stating local slopes at named masses instead of `b₁`. On the residual test: a constrained two-step fit *"will produce an inherently worse fit and, consequently, reduce the significance of curvature. We question the value of a statistical model that is sub-optimal by construction."* On the missing physical rationale: the quadratic is a **statistical** model for detecting curvature, not a mechanism, and the objection *"confuses statistical models aimed at characterizing properties of data with physical models aimed at explaining them."* They add that curvature *"remained significant even when accounting for other variables such as body temperature, phylogenetic relationships, food sources and habitat."* **What the reply never addresses is MacKay's other two receipts:** the uncited Hayssen & Lacy (1985) rejection, and the 70-marsupial fit. Those stand unrebutted.

So: the curvature may be a between-Order artifact rather than a law of size — and the case that it is not is made by the people who proposed it. **This dispute is live.** Class it OBSERVED-CONTESTED and carry it that way.

## WBE: where 3/4 comes from, and what the derivation costs

West, Brown & Enquist (1997), *Science* 276:122–126, derive 3/4 from three assumptions: a space-filling fractal-like branching network that supplies the whole body volume; a **size-invariant terminal unit** (the capillary); and minimisation of the energy required to distribute resources. Class: **MODELED**. The assumptions are the fence.

Kozlowski & Konarzewski (2004), *Functional Ecology* 18:283–289, argue the model is mathematically inconsistent unless either metabolic rate is directly proportional to mass — which would defeat its own purpose — or the size-invariance assumption is violated; that animals built to the model cannot span a broad size range, because for large animals vessel volume would exceed body volume; and that 3/4 is not universal, so the model explains a pattern that does not exist. Brown, West & Enquist (2005), *Functional Ecology* 19:735–738, reply that this misreads assumption (2): only the *capillary's own* parameters are invariant, while the **service volume** each capillary supplies scales as `M^(1/4)` — which is the engine of the 3/4 result, not a contradiction of it. Kozlowski & Konarzewski (2005) rejoin that the questions remain. Banavar et al. (2002), *PNAS* 99:10506–10509, make the related structural point about size-invariant terminal demand.

That exchange is a stalemate of interpretations. **The decisive receipt is empirical and it is a sign error.** Kolokotrones et al. show that WBE's 3/4 holds only asymptotically, in the infinite-mass limit; for finite animals the model yields `M = c₀B + c₁B^(4/3)`, and with both coefficients positive this predicts **concave** curvature. The data are **convex**. Not "a poor fit" — the wrong sign. Modified variants (moving the pulsatile/smooth flow transition a constant *fraction* of levels from the heart) do produce convex curvature and fit nearly as well as the quadratic. **What is refuted is the specific 1997 geometry, not network explanations in general.** That distinction is the whole discipline.

## The quarter-power family: how much survives measurement

This is where a builder gets burned, because the family is quoted as if every member were measured.

- **Heart rate `∝ M^(−1/4)`** — Lindstedt & Hoppeler (2023), *J Exp Biol* 226(24):jeb245766, state the exponent directly: resting heart rate *"scales as M–1/4 resulting in resting cardiac output scaling in parallel with metabolism."* The **prefactor** usually quoted alongside it — `f = 241·M^(−0.25)` bpm, `M` in kg, attributed to Calder's cardiac allometry — is **NOT-MEASURED in this pass and is not printed here as sourced**: the number `241` does not appear in Lindstedt & Hoppeler, and the Calder/Stahl primary was not read. Sourcing a value to neither the citation nor the primary is the third state this chapter's own rail forbids. **Falsifier: read Calder 1984, *Size, Function and Life History*, or Stahl 1967, and print the coefficient actually given.** Only the exponent is used below — which is the chapter's own thesis about prefactors, applied to itself.
- **Lifespan `∝ M^(1/4)`** — **this one does not survive.** de Magalhães, Costa & Church (2007), *J Gerontol A* 62(2), fit 856 mammals (excluding cetaceans): `t_max = 4.88·M^0.153` years, `M` in grams, `R² = 0.66`. For 518 birds: `t_max = 5.22·M^0.218`, `R² = 0.70`. **Neither exponent is 1/4.** The mammalian value, 0.153, is not close.
- **VO₂max `∝ M^0.872`** across 34 eutherian species spanning **7 g – 500 kg** (Lindstedt & Hoppeler 2023) — against basal ~0.70. **The exponent depends on which metabolic state you measure.** There is no "the" metabolic exponent even for one animal.

Now compose the two measured exponents and watch the most famous invariant in comparative physiology come apart:

```
beats/lifetime  ∝  M^(−0.25) · M^(+0.153)  =  M^(−0.097)
```

**It is not invariant.** It declines with mass — across 7 decades of mammalian mass, by `10^(7 × 0.097) ≈ 4.8×`. The "constant ~10⁹ heartbeats" is a *consequence of assuming the lifespan exponent is exactly +1/4*, which cancels the −1/4 of heart rate. Insert the measured 0.153 and the cancellation fails. *(Fence: this composes exponents from two different datasets and eras — a legitimate defect in its own right, per M22. It is offered as an arithmetic check, not a new measurement.)*

And the data agree that it is not constant. Levine (1997), *J Am Coll Cardiol* 30:1104–1106, reports **7.3 ± 5.6 × 10⁸ beats/lifetime** for mammals — *"within an order of magnitude, remarkably constant"*, in his words. **Levine does not state what the `±` is.** SD, SEM and range are all live readings, and the source defines none of them; it is read here as a **standard deviation**, which is the ordinary convention for a cross-species mean and the reading *least* favourable to the argument being made with it. On that stated assumption the spread is **77% of the mean**, and a "constant" with a 77% coefficient of variation is a tendency. **Falsifier: if the `±` is a SEM, the across-species spread is far wider and this argument strengthens rather than collapses — so the reading is fenced, not load-bearing.** An undefined `±` promoted to a named statistic is this chapter's own priority-3 defect, and it is fenced here rather than committed. Levine's own scope statements are the useful part: a Galapagos tortoise (177 y at 6 bpm) lands at 5.6 × 10⁸, close to the mammal mean; but haddock (3.5 × 10⁷) and brown trout (6.7 × 10⁷) come in **an order of magnitude lower**, and *Daphnia* burns 1.3 × 10⁷ in 30 days at 25 °C.

**And humans are the conspicuous exception — Levine says so explicitly.** The inverse heart-rate/lifespan relation holds across mammals *with the exception of the human species*. At ~70 bpm for ~80 years: `70 × 60 × 24 × 365.25 × 80 ≈ 2.9 × 10⁹` — about **4× the mammalian mean**, and Levine quotes ~3 billion. **An outlier is data.** Humans do not sit on the line, and no amount of admiring the line changes that.

## Surface/volume `∝ L^(−1)`, and an ecogeographic rule that is 70% true

For a sphere, `S/V = 3/R`. Under isometry, surface `∝ M^(2/3)`. This is the oldest ratio in biology and it is the entire content of Rubner's surface law.

**Bergmann's rule** — bodies larger in colder places — is its most cited ecological consequence. Meiri & Dayan (2003), *J Biogeogr* 30:331–351, reviewed 149 mammal and 94 bird species using only studies that tested significance. Conformity: **65–71% of mammals, 72–76% of birds** *(percentages as reported via Teplitsky & Millien 2014; the primary paper was not read in this pass — see the open row)*. So roughly **three in ten mammals do the opposite or nothing.** That is a tendency with a large exception class, not a law. Meiri & Dayan also name the confound that will not go away: latitude bundles altitude, aridity, vegetation structure and food availability, all of which move body size independently of heat. The S/V mechanism is a *hypothesis about why*, and it is not what was measured.

## Elastic similarity, and the model that mostly failed

Galileo (1638, *Two New Sciences*) got there first and is still right. Hold shape constant and scale up: weight `∝ L³`, supporting cross-section `∝ L²`, so bone stress `σ = F/A ∝ L³/L² = L`. **Stress grows linearly with size at constant shape.** Scale an animal up enough and it breaks under itself. Shape *must* change. This is the first quantitative result in biology and it needs no revision.

McMahon (1973), *Science* 179:1201–1204, proposed the fix: **elastic similarity**, `L ∝ D^(2/3)`. The algebra cascades cleanly — with `M ∝ D²L` and `L ∝ D^(2/3)`, we get `M ∝ D^(8/3)`, hence `D ∝ M^(3/8)`, `L ∝ M^(1/4)`, and surface `∝ D·L ∝ M^(5/8)` (all computed here; reproduces the `M^(5/8)` surface exponent and the `M^(−1/4)` biological-frequency result McMahon states). McMahon derived Kleiber's 3/4 from it.

**Two things must be said about that, and the second is usually omitted.**

First: **elastic similarity and WBE are incompatible mechanisms that predict the same exponent.** An exponent that multiple unrelated mechanisms produce is weak evidence for any of them. Per **M7**, if a discriminator does not collapse the alternatives, the agreement is not a result. 3/4 does not discriminate McMahon from West.

Second: **elastic similarity mostly failed its own empirical test.** Alexander et al. (1979), *J Zool* 189:305–314, measured femora, tibiae, humeri and radii across 32 mammal species from 0.020 to 3500 kg and found length `∝ M^0.31` and diameter `∝ M^0.35` — against elastic similarity's predicted `M^0.25` and `M^0.375`, and isometry's `M^0.333` for both. *(**Primary not read in this pass** — the paper is paywalled and returned 403; the exponents and the species count come via secondary sources, and secondary sources give the count as **37, not 32**. The row is fenced in the NOT-READ list below rather than left looking checked. The **direction** of the result — geometric, not elastic — is independently corroborated, which is what the negative verdict rests on.)* **Mammalian long bones scale close to geometric similarity.** Elastic similarity applied mainly to bovids. Later work suggests bone dimensions support *neither* model cleanly. The famous derivation of Kleiber from elasticity rests on a premise the bones do not obey.

## `t ∝ L²/D`: the ratio that forces circulatory systems to exist

The most under-appreciated ratio in biology, and the one with the least wiggle room. For 3D diffusion, `t ≈ L²/(6D)`. With oxygen in water, `D = 2.0 × 10⁻⁹ m²/s = 2000 µm²/s` **at room temperature** (BNID 114984; St-Denis & Fell 1971, *Can J Chem Eng* 49:885) — hold onto that condition, it is collected below:

| Distance | Time for O₂ to diffuse it |
|---|---|
| 10 µm | 8.3 ms |
| 100 µm | 0.83 s |
| 1 mm | 83 s |
| 1 cm | 8.3 × 10³ s ≈ 2.3 h |
| 10 cm | 8.3 × 10⁵ s ≈ **9.6 days** |

Now compute the crossover that actually forces the design. For a sphere of radius `R` consuming O₂ uniformly at `a` mol m⁻³ s⁻¹, supplied by diffusion from a surface at concentration `C₀`, the steady state is `C(r) = C₀ − (a/6D)(R² − r²)`. Oxygen reaches the centre only if:

```
R_max = √(6·D·C₀ / a)
```

Put a resting human in it. Dissolved arterial O₂ at PaO₂ = 100 mmHg is 0.3 mL O₂ per 100 mL (Henry's law, 0.003 mL·O₂/100 mL/mmHg), i.e. `C₀ ≈ 0.134 mol/m³`. Resting O₂ consumption ~250 mL/min over 70 kg ≈ 0.07 m³ gives `a = 2.66 × 10⁻³ mol m⁻³ s⁻¹`. Then:

```
R_max = √(6 × 2.0×10⁻⁹ × 0.134 / 2.66×10⁻³) = √(6.0×10⁻⁷) ≈ 7.8 × 10⁻⁴ m ≈ 0.78 mm
```

**Condition mismatch, stated — this chapter's own priority-3 defect, inside its own showpiece calculation.** The `D` above is BNID 114984's **room-temperature** value, while every other input here — `PaO₂`, resting VO₂, the body it describes — is at **37 °C**. `D` for O₂ in water is roughly 50% higher at 37 °C than at ~22 °C, and since `R_max ∝ √D`, the 37 °C figure would be **~0.95 mm rather than 0.78 mm**. The cross-check below moves with it: `(950/75)² ≈ 160×` rather than ~100×, which makes the agreement with the ~40–75× physiological estimate **worse — a factor of ~2–4, not ~2**. The >1.5 mm conclusion survives either way, because the error widens the diffusion bound rather than rescuing anything. But a rate quoted without its temperature is exactly the defect this chapter fences elsewhere, and the chapter even carries a `C_sat,water,37 °C` row — it knew the body temperature and never reconciled `D` to it. **A 37 °C `D` for O₂ in water is NOT-SOURCED in this pass. Falsifier: source one and recompute both figures.**

**Nothing thicker than about 1.5 mm can run on dissolved-oxygen diffusion at human resting metabolism.** A circulatory system is not an optimisation or an elegance. It is the unavoidable price of exceeding a millimetre.

**Cross-check it against anatomy, which is how you know a model is doing work.** Observed intercapillary distance in human skeletal muscle is 100–200 µm — a Krogh radius of 50–100 µm, about 8–15× smaller than the resting figure. The model therefore *predicts* that working muscle runs at `(778/75)² ≈ 100×` the resting whole-body specific rate. The physiological estimate is ~40–75×. **Agreement to within a factor of ~2** — which is what a sphere model applied to cylindrical geometry with a non-zero edge PO₂ should cost, and no better. *(That ~2× holds at the room-temperature `D`. At a 37 °C `D` the prediction rises to ~160× and the agreement degrades to ~2–4× — see the condition note above. The residual is stated at both, because picking the flattering one is the defect.)* Stating the residual is the point.

## Sublinear and superlinear: colonies and cities

**Ant colonies.** Hou et al. (2010), *PNAS* 107(8):3634–3638, report whole-colony metabolic rate scaling as `M^0.81` — and this is the cleanest available lesson in reading a CI. **95% CI: 0.55–1.08** (r² = 0.82, n = **12 colonies** + 391 unitary insects). That interval **excludes nothing**: it contains 2/3, 3/4, and isometry. The study cannot discriminate the hypotheses it is cited for. Their intraspecific exponents (0.44–0.94, n = 5) bracket everything too, and their unitary-insect lifespan CI runs `0.01–0.47`. The colony *production* exponent is genuinely tight (combined 0.74, CI 0.71–0.76) — cite that one, not the metabolic one.

**Cities.** Bettencourt et al. (2007), *PNAS* 104(17):7301–7306, Table 1. Three classes, and the honest reading is that "~1.15" is not a value but a **cluster**:

- **Superlinear:** private R&D employment 1.34 [1.29–1.39]; new patents 1.27 [1.25–1.29], n=331 USA 2001; GDP 1.15 [1.06–1.23], China 2002; total wages 1.12 [1.09–1.13]; **new AIDS cases 1.23 [1.18–1.29]**.
- **Linear:** total housing 1.00 [0.99–1.01]; total employment 1.01 [0.99–1.02]; household water 1.01 [0.89–1.11].
- **Sublinear:** gasoline stations 0.77 [0.74–0.81]; road surface 0.83 [0.74–0.92] (**n = 29**); electrical cables 0.87 [0.82–0.92].

Note the AIDS row. **Superlinear scaling is value-neutral**: cities superlinearly produce patents *and* disease, by the same exponent class. Anyone quoting 1.15 as a case for cities has selected the rows.

And the class itself is contested. Leitão et al. (2016), *R Soc Open Sci* 3:150649, tested 5 models against 15 datasets in a framework where fluctuations are modelled explicitly, and conclude that whether `β ≠ 1` — and the confidence interval around it — depends crucially on the fluctuations in the data, on how they are modelled, and on the heavy-tailed distribution of city sizes. Bettencourt's `[1.25, 1.29]` is tight *conditional on a fluctuation model*, and that condition is exactly what is in dispute.

## The earned and the unearned: the golden angle

**EARNED.** ~137.5° in phyllotaxis. Douady & Couder (1992), *Phys Rev Lett* 68:2098–2101, reproduced Fibonacci phyllotaxis in a **physical laboratory experiment** — ferrofluid droplets dropped periodically at the centre of a **stationary** horizontal Teflon dish of silicone oil, sitting in a **vertical magnetic field with a weak radial gradient** (minimal at the centre, maximal at the rim); the field polarises each drop into a dipole, so the drops repel one another and self-advect outward down the gradient — plus numerical simulation. As advection speed decreased, the divergence angle converged to the golden angle. The mechanism is the system avoiding rational (periodic) organisation. **The dish does not rotate, and that is the entire result:** the angle is the experiment's *output*, not an imposed boundary condition. An externally imposed rotation would hand the system the very angular scale it is celebrated for generating spontaneously. Mechanism, physical replication, falsifier. That is what an earned ratio looks like, and it needs no mysticism to be beautiful.

**INADMISSIBLE.** "The golden ratio is a universal design law of nature." The distance between this sentence and Douady & Couder is the entire method — see the record below.

## How to use a ratio to design (the operable payload)

1. **State the target scale and the fitted range.** If the target is outside the range, you are extrapolating. Say the word.
2. **Carry the exponent, not the prefactor — and read its CI, not its point estimate.** If the CI contains the alternatives you meant to discriminate (Hou's `[0.55, 1.08]`), the ratio decides nothing. **Stop.** This is M2.
3. **Compute the magnitude with the prefactor, in stated units, showing the arithmetic** so a reader can refute it.
4. **State the falsifier before you look.**
5. **Check whether the regime changed.** ← the #1 way scaling arguments fail. A power law fitted in one range does not extrapolate through a regime change, and the fit will not warn you.
6. **Record NEGATIVE if it fails.** Per M7, a bio-inspired design must beat a **tuned** baseline on a **pre-registered** metric with a discriminator that collapses the gain, or it is a negative result.

Step 5 has a price tag, computed from this chapter's own numbers. Take the local 3/4 slope, valid at ~4.2 kg, and extrapolate it down to a 3 g shrew — 3.1 decades. Against Kolokotrones's quadratic:

```
line (b=0.75):  Δlog₁₀B = 0.75 × (0.477 − 3.623) = −2.360
quadratic:      Δlog₁₀B = 0.263 − 2.332          = −2.069
discrepancy = 0.291 in log₁₀  →  10^0.291 ≈ 1.95×
```

**The 3/4 line underpredicts the shrew's metabolic rate by about a factor of 2.** Not catastrophic — and that is precisely why it is dangerous. A 2× error looks like measurement noise, passes review, and is wrong for a structural reason no amount of better data will fix.

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `b_Kleiber` | 3/4 (measured slope reported 0.74) | dimensionless | BMR vs mass, 13 data points | **OBSERVED-CONTESTED** | Kleiber 1932, *Hilgardia* 6:315–353; n=13 per Kolokotrones et al. 2010, *Nature* 464:753–756 | See every row below; the dispute *is* the falsification record |
| `b_Rubner` | 2/3 | dimensionless | surface-law argument; respiration trials on dogs | **OBSERVED-CONTESTED** | Rubner 1883 | Data rejecting 2/3 at a stated mass range |
| `b_Savage,binned` | 0.737 | dimensionless | mammal BMR, 0.1 log-unit bins | **OBSERVED-CONTESTED** | Savage et al. 2004, *Funct Ecol* 18:257–282 (95% CI 0.711–0.762, n=52) | Re-fit with different binning |
| `b_Savage,unbinned` | **0.712** | dimensionless | mammal BMR, all species — **CI excludes 2/3 and 3/4** | **OBSERVED-CONTESTED** | Savage et al. 2004 (95% CI 0.699–0.724, n=626) | Re-fit; show binning is not what moves the verdict |
| `b_White&Seymour` | 0.68 (interspecific); 0.65 (interordinal) — both **≠ 3/4**, both **= 2/3** within error | dimensionless | 619 spp. → 469 after excluding Artiodactyla, Lagomorpha, Soricidae, Macropodidae; T_b-corrected to 36.2 °C, Q₁₀=3.0 | **OBSERVED-CONTESTED** | White & Seymour 2003, *PNAS* 100(7):4046–9 *(CIs not read in this pass)* | A dataset with equivalent basal-condition rigour giving 3/4 |
| `b_WS,BMR / SMR / RMRt` | 0.686±0.014 / 0.675±0.013 / 0.712±0.013 | dimensionless | **exponent depends on which rate is measured**; the BMR/SMR figures are White & Seymour's **own 2003 fits restated in their 2005 review — same authors, same dataset, same regression, so not a replication** | **OBSERVED-CONTESTED** *(re-classed: the identical underlying result is OBSERVED-CONTESTED two rows up; one result cannot hold two classes)* | White & Seymour 2003, as tabulated in White & Seymour 2005, *J Exp Biol* 208:1611 | Show the three definitions give one exponent |
| `b₂` (curvature) | **0.0322 ± 0.0053** (P = 9.0×10⁻¹⁰); 0.0294 ± 0.0057 with T | dimensionless | McNab dataset, n=636 (447 with T); **unit-scale invariant** | **OBSERVED-CONTESTED** | Kolokotrones et al. 2010, *Nature* 464:753–756, Table 1 | MacKay 2011 — see contested row; reply: Deeds, Savage & Fontana 2011 |
| `b₁` | 0.5400 ± 0.0295 (0.5371 ± 0.0305 with T) | dimensionless | **artifact of M₀ = 1 g; not interpretable alone** | **INADMISSIBLE as "the exponent"** | Kolokotrones et al. 2010; objection: MacKay 2011, *J Theor Biol* 280(1):194–6; reply: Deeds, Savage & Fontana 2011, 280:197–8 — **concedes the artifact, calls it irrelevant to curvature; the class stands either way** | Derive: under `M'=kM`, `b₁' = b₁ − 2b₂log k` |
| local slope | **0.57 → 0.87** (rises with mass) | dimensionless | ~3.6 g to ~460 kg; = `b₁ + 2b₂log₁₀M` | MODELED | Computed here from Kolokotrones Table 1; matches their stated range | Arithmetic error |
| `M(slope=2/3)` | ~160 g (temp fit); ~93 g (no-temp fit) | g | mass where local slope = 2/3 | MODELED | Computed here | Arithmetic error |
| `M(slope=3/4)` | ~4.2 kg (temp fit); ~1.8 kg (no-temp fit) | kg | mass where local slope = 3/4 | MODELED | Computed here | Arithmetic error |
| `M(slope=1)` | ~7.4 × 10⁷ g ≈ 74 t | g | proposed upper bound on animal size — **EXTRAPOLATION: ~2.2 decades beyond the fitted data, which end at ~460 kg (local slope 0.87)**. Kolokotrones et al.'s own two hedges: the unbounded slope rise "may be due to the **paucity of data for large animals**", and the size-limit reading holds only "**If this is correct**" | MODELED (**extrapolated — rule 1 applies to this row**) | Computed here; Kolokotrones et al. state ~10⁸ g (100 t) | A larger animal; or the slope not reaching 1 |
| ΔR² from curvature | 0.958 → 0.961; **7%** of unexplained variance per Kolokotrones, **~one-tenth** per MacKay | — | **small purchase — always carry this next to the P value** | OBSERVED-REPLICATED | Kolokotrones et al. 2010 (95.8→96.1%, 7%); MacKay 2011 (~1/10) | Recompute; the two sources state the same ΔR² and differ on the fraction |
| `k_marsupial` | **0.75 ± 0.01**, R² = 0.990 | dimensionless | 70 marsupials (McNab 2008), excluding *Tarsipes rostratus* + *Lasiorhinus latifrons* | **OBSERVED-CONTESTED** | MacKay 2011 | Re-fit with the 2 species retained |
| curvature within Orders | significant only in Rodentia (p=0.02, 0.02 of variance) — **but pooled across all eutheria the quadratic term "remains significant" under the same test, MacKay's own words** | — | residual-based test; the near-vanishing is a **within-Order result only** | **OBSERVED-CONTESTED** | MacKay 2011 | Independent within-Order test |
| reply to MacKay | `b₁` artifact **conceded, argued irrelevant** (only `b₂` assesses curvature); MacKay's two-step residual test called **"sub-optimal by construction"**; curvature reported to survive T_b, phylogeny, food source and habitat | — | rebuttal by **3 of Kolokotrones et al.'s 4 authors — not independent**; silent on Hayssen & Lacy (1985) and on the 70-marsupial fit | **OBSERVED-CONTESTED** | Deeds, Savage & Fontana 2011, *J Theor Biol* 280:197–198, doi:10.1016/j.jtbi.2011.03.036 | Answer the two receipts it leaves standing; or an independent party adjudicating the residual-test dispute |
| WBE assumptions | space-filling fractal network; size-invariant terminal unit; energy minimisation | — | derivation of 3/4 | **MODELED** | West, Brown & Enquist 1997, *Science* 276:122–126 | The assumptions are the fence — see rows below |
| WBE finite-size form | `M = c₀B + c₁B^(4/3)`, both c > 0 → **concave**; data are **convex** | — | **wrong sign of curvature** | MODELED (refuted on this point) | Kolokotrones et al. 2010 | Show `c₁ < 0` follows from WBE's own minimisation |
| `b_heart` | −1/4 | dimensionless | resting mammals; **L&H state no n and no mass range for the resting-HR claim** — their 34-species / 7 g–500 kg series is *maximal* heart rate (−0.15) and VO₂max, not this row | OBSERVED-REPLICATED | Lindstedt & Hoppeler 2023, *J Exp Biol* 226(24):jeb245766 — *"resting heart rate scales as M–1/4"* | Modern re-fit with CI outside −0.30 to −0.20 |
| `f` prefactor (heart rate) | **NOT-MEASURED in this pass.** `241` (bpm, `M` in kg) is widely quoted but **appears nowhere in Lindstedt & Hoppeler 2023**, and the Calder/Stahl primary was not read | bpm | — | **NOT-MEASURED** | none read; attributed to Calder's cardiac allometry — **the citation does not carry the value** | Read Calder 1984, *Size, Function and Life History*, or Stahl 1967; print the coefficient it gives |
| `b_lifespan,mammal` | **0.153** (`t_max = 4.88·M^0.153` yr, M in g), R²=0.66 | dimensionless | 856 mammals, cetaceans excluded — **not 1/4** | OBSERVED-REPLICATED | de Magalhães, Costa & Church 2007, *J Gerontol A* 62(2) | Re-fit giving CI containing 0.25 |
| `b_lifespan,bird` | 0.218 (`t_max = 5.22·M^0.218` yr), R²=0.70 | dimensionless | 518 birds | OBSERVED-REPLICATED | de Magalhães et al. 2007 ("body mass explained 70% of the variation in tmax") | As above |
| `b_VO₂max` | **0.872** | dimensionless | 34 eutherian species, **7 g – 500 kg** — vs basal ~0.70 | OBSERVED-REPLICATED | Lindstedt & Hoppeler 2023 | Show basal and max share an exponent |
| beats/lifetime | **7.3 ± 5.6 × 10⁸** — **`±` convention not stated in the source; read here as SD** → 77% of mean | beats | mammals | **OBSERVED-CONTESTED** | Levine 1997, *J Am Coll Cardiol* 30:1104–6 | An "invariant" needs a CV that does not span an order of magnitude. **If the `±` is a SEM the species spread is wider still and this row strengthens** |
| beats/lifetime, human | ~2.9 × 10⁹ (70 bpm × 80 yr); Levine quotes ~3 × 10⁹ | beats | **the conspicuous exception, ~4× the mammal mean** | MODELED (computed here) + OBSERVED | Computed here; Levine 1997 states humans are the exception | Arithmetic; or a mammal line that humans fall on |
| beats/lifetime, other | tortoise 5.6×10⁸; haddock 3.5×10⁷; brown trout 6.7×10⁷; *Daphnia* 1.3×10⁷ | beats | **fish are an order of magnitude below mammals** | OBSERVED-REPLICATED *(as reported by Levine 1997)* | Levine 1997 | Independent measurement |
| beats/lifetime **scaling** | `∝ M^(−0.097)` → **~4.8× decline over 7 decades of mass** | dimensionless | composition of −0.25 and +0.153 | MODELED (computed here) | Computed from Lindstedt & Hoppeler 2023 + de Magalhães et al. 2007 | Measure beats/lifetime vs mass directly in one dataset — **this composition mixes sources (M22)** |
| `D_O₂,water` | 2.0 × 10⁻⁹ (= 2000 µm²/s) | m²/s | **room temperature — but fed into a 37 °C calculation in `R_max` below; the mismatch is stated there, not hidden** | OBSERVED-REPLICATED | BNID 114984; St-Denis & Fell 1971, *Can J Chem Eng* 49:885 | Independent measurement >2× off |
| `C₀` (dissolved arterial O₂) | 0.134 (0.3 mL O₂/100 mL at PaO₂ 100 mmHg) | mol/m³ | Henry's law, 0.003 mL·O₂/100 mL/mmHg | OBSERVED-REPLICATED *(standard physiology; primary not read in this pass)* | standard respiratory physiology | Measurement outside 0.10–0.16 |
| `C_sat,water,37 °C` | 207.3 (0.207 mol/m³) | µM | air-saturated pure water, 100 kPa | OBSERVED-REPLICATED *(secondary: Bioblast)* | Bioblast, *Oxygen solubility* | Primary thermodynamic table disagreeing >10% |
| `a` (resting O₂ use) | 2.66 × 10⁻³ | mol m⁻³ s⁻¹ | 250 mL O₂/min, 70 kg, ρ = 1000 kg/m³ | MODELED (computed here) | Computed; VO₂ rest is a **standard reference value, not primary-sourced in this pass** | Refute the 250 mL/min input |
| `R_max` | **~0.78** at room-temperature `D`; **~0.95 at 37 °C** | mm | sphere, `√(6DC₀/a)`, human resting metabolism — **`D` is room-temperature, the calculation is 37 °C; a 37 °C `D` is NOT-SOURCED in this pass** | MODELED (computed here) | Computed from the three rows above | Exhibit tissue >1.5 mm thick living on dissolved-O₂ diffusion at this `a`. **The condition error widens the bound — it does not rescue the conclusion** |
| Krogh radius (observed) | 50–100 (intercapillary 100–200) | µm | human skeletal muscle | OBSERVED-REPLICATED *(secondary sources in this pass)* | Krogh-model literature | Direct measurement outside range |
| muscle:rest specific rate | **predicted ~100×** at room-temperature `D` (**~160×** at 37 °C); physiological estimate ~40–75× | dimensionless | reconciles `R_max` with the Krogh radius — **agreement only to ~2×, degrading to ~2–4× once `D` is put at body temperature** | MODELED (computed here) | Computed; sphere-vs-cylinder geometry mismatch is the residual | Measure working-muscle specific VO₂ directly |
| `σ ∝ L` | stress grows **linearly** with size at constant shape | — | `F/A ∝ L³/L²` | OBSERVED-REPLICATED (geometry) | Galileo 1638, *Two New Sciences* | Geometric error |
| elastic similarity | `L ∝ D^(2/3)`; → `D ∝ M^(3/8)`, `L ∝ M^(1/4)`, `S ∝ M^(5/8)` | dimensionless | McMahon's model | **MODELED** | McMahon 1973, *Science* 179:1201–4; cascade computed here (reproduces his `M^(5/8)`) | See next row — **largely refuted empirically** |
| bone scaling (measured) | length `∝ M^0.31`; diameter `∝ M^0.35` | dimensionless | 32 mammal spp. (**secondary sources say 37 — unresolved here**), 0.020–3500 kg — **close to geometric similarity, not elastic (0.25 / 0.375)** | OBSERVED-REPLICATED *(**primary not read in this pass; exponents and n via secondary sources**)* | Alexander et al. 1979, *J Zool* 189:305–314 | Read the primary; a species count or exponent outside the stated values moves this row. **The NEGATIVE verdict rests on the direction (geometric, not elastic), which is corroborated independently, and survives either count** |
| `b_colony,metabolic` | **0.81, 95% CI 0.55–1.08** | dimensionless | 12 colonies + 391 unitary insects; **CI excludes nothing** | **OBSERVED-CONTESTED** | Hou et al. 2010, *PNAS* 107(8):3634–8 | More colonies; a CI that excludes an alternative |
| `b_colony,production` | 0.74, 95% CI 0.71–0.76 (r²=0.99, combined) | dimensionless | colonies + unitary organisms — **the tight row** | OBSERVED-REPLICATED | Hou et al. 2010 | Independent re-fit |
| `b_city,superlinear` | **cluster 1.07–1.34**, not a single value | dimensionless | patents 1.27 [1.25–1.29]; R&D empl. 1.34 [1.29–1.39]; GDP 1.15 [1.06–1.23]; wages 1.12 [1.09–1.13]; **AIDS 1.23 [1.18–1.29]** | **OBSERVED-CONTESTED** | Bettencourt et al. 2007, *PNAS* 104(17):7301–6, Table 1 | Leitão et al. 2016 — see next row |
| `b_city,sublinear` | gasoline stations 0.77 [0.74–0.81]; road surface 0.83 [0.74–0.92] (**n=29**); cables 0.87 [0.82–0.92] | dimensionless | Germany/USA 2001–02 | **OBSERVED-CONTESTED** | Bettencourt et al. 2007 | As above |
| urban `β ≠ 1` | **model-dependent** | — | 5 models × 15 datasets; depends on fluctuations, their model, and heavy-tailed city sizes | **OBSERVED-CONTESTED** | Leitão et al. 2016, *R Soc Open Sci* 3:150649 (arXiv:1604.02872) | A fluctuation model class under which the verdict is stable |
| `θ_golden` | ~137.5 | degrees | phyllotaxis divergence angle; **physically reproduced** | OBSERVED-REPLICATED | Douady & Couder 1992, *Phys Rev Lett* 68:2098–2101 | Repulsion-dynamics experiment failing to converge to the golden mean |
| Bergmann conformity | 65–71% (mammals); 72–76% (birds) | % of species | 149 mammals, 94 birds | **OBSERVED-CONTESTED** | Meiri & Dayan 2003, *J Biogeogr* 30:331–351 — **percentages via Teplitsky & Millien 2014; primary not read (M22)** | Read the primary; a value outside these ranges |
| exponent spread | mean 0.738±0.018 but **51% of exponents outside 0.7–0.8**; range <0.5 to >1.0 | dimensionless | 146 relations (Peters 1983), 72% vertebrate | OBSERVED-REPLICATED | Glazier 2005, *Biol Rev* 80:611–662 | Recount the distribution |
| intraspecific spread | **0.3 to 1.8**; mean 0.724, **mode 0.667** | dimensionless | 220 species (Withers 1992) | OBSERVED-REPLICATED | Glazier 2005 | Recount |
| MLBH bounds | 2/3 (surface-area limits) to 1 (mass/volume power limits) | dimensionless | metabolic-level boundaries hypothesis | **HYPOTHESIZED** | Glazier 2005, 2010, *Biol Rev* 85:111–138 | An exponent stably outside [2/3, 1] with a demonstrated mechanism |

## Falsifier (operable)

This chapter's central structural claim — **that an allometric exponent is a property of a *mass range*, not of a taxon or a mechanism, so that a power law fitted in one range does not extrapolate through a regime change** — is refuted by exhibiting **one mammalian BMR dataset spanning ≥5 orders of magnitude in mass, measured under basal conditions, in which a single power law is not rejected against a quadratic alternative, AND whose fitted exponent is reproduced within its 95% CI by an independent dataset with a materially different mass distribution.** The Kolokotrones/MacKay exchange is the live test of exactly this: MacKay's 70-marsupial fit (`k = 0.75 ± 0.01`, R² = 0.990) is a partial counter-instance already on the record, and is why the chapter is fenced OBSERVED-CONTESTED rather than settled. Extend that fit across 5 orders of magnitude and the chapter's claim weakens materially.

Secondary falsifiers are row-local: any number in the table found outside its stated scope under its stated conditions moves that row and only that row. A refuted row does not refute the chapter. A single reproducible global exponent moves the chapter.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **"The golden ratio is a universal design law of nature."** — **INADMISSIBLE.** Unfalsifiable as stated: no observation is specified that could refute it, and supporting instances are selected post hoc. **Receipt of failure:** the claim survives every counterexample by redescription — the signature of an unfalsifiable claim. Recorded, not mocked. Its earned neighbour (θ ≈ 137.5° with the Douady & Couder 1992 ferrofluid mechanism) is in the table above; **the contrast is the lesson, not the rebuke.**
- **"Kleiber's law is a law."** — **NEGATIVE.** Recorded as a naming defect with a receipt: 51% of compiled exponents fall outside 0.7–0.8 (Glazier 2005); the same paper's binned and unbinned fits disagree on whether 3/4 survives (Savage et al. 2004); the log-log relation carries significant convex curvature (Kolokotrones et al. 2010). It is a robust *regularity over a range*, which is a real and useful thing, and is not a law.
- **`b₁ = 0.54` quoted as "the metabolic exponent."** — **INADMISSIBLE.** It is the local slope at `M₀ = 1 g` and changes value if you measure mass in kilograms (`b₁' = b₁ − 2b₂log k`). Only `b₂` and the local slope at a *named* mass are unit-invariant. Receipt: MacKay 2011.
- **NEGATIVE / the exponent does not discriminate:** McMahon's elastic similarity (1973) and WBE's fractal network (1997) are incompatible mechanisms that both predict 3/4. Per **M7**, agreement with an exponent that multiple unrelated mechanisms produce is not evidence for any one of them. Recorded because "the model predicts 3/4 and we observe 3/4" is the most common malformed argument in this literature.
- **NEGATIVE / elastic similarity, empirically:** Alexander et al. (1979) measured mammal limb bones scaling close to **geometric** similarity (`L ∝ M^0.31`, `D ∝ M^0.35`) rather than elastic (`M^0.25`, `M^0.375`). The famous derivation of Kleiber from elasticity rests on a premise the bones largely do not obey. Recorded as a first-class negative, not a footnote.
- **NEGATIVE / reading a point estimate:** Hou et al. (2010)'s colony metabolic exponent 0.81 is routinely cited as support for 3/4 colony scaling. Its 95% CI is `[0.55, 1.08]`, which excludes 2/3, 3/4, *and* isometry from refutation alike. With n = 12 the study has no discriminating power on this question. **The verdict is the CI bound (M2).** Their production exponent (0.74, CI 0.71–0.76) is the citable row.
- **NEGATIVE / selecting rows:** citing urban superlinearity as a case *for* cities requires ignoring `new AIDS cases: β = 1.23 [1.18–1.29]` in the same table (Bettencourt et al. 2007). The exponent class is value-neutral.
- **NOT-SOURCED in this pass:** the widely repeated anecdote that Kleiber chose 3/4 over his measured 0.74 because it was easier on a slide rule. It was **not confirmed** against Kleiber 1932 or any primary source here and is therefore **not printed as fact**. Closure: read *Hilgardia* 6:315–353.
- **RETRIEVAL ROUTE, disclosed:** the Savage et al. (2004) statistics — binned `0.737 [0.711, 0.762]`, n=52; unbinned `0.712 [0.699, 0.724]`, n=626 — are **quoted from search-indexed full text of the paper, corroborated by two independent queries returning identical figures, P values and journal house-style formatting. The PDF itself returned HTTP 403 and was not opened here.** They are load-bearing for this chapter's central argument and are therefore flagged rather than laundered. Closure: open *Functional Ecology* 18:257–282 and read the mammalian BMR section. **Falsifier: if the unbinned CI does not exclude 3/4, the sharpest claim in this chapter's Kleiber section falls and must be struck.** *(**Retrieval upgraded this pass, and the route differs by source:** Kolokotrones et al. 2010, MacKay 2011 and the Deeds, Savage & Fontana 2011 reply were read as **directly extracted PDF text**; White & Seymour 2003, de Magalhães et al. 2007 and Lindstedt & Hoppeler 2023 were **quoted from publisher/PMC full text**. Quotations attributed to those six are verbatim from the source. The Savage 403 stands unchanged.)*
- **NOT-MEASURED / NOT-READ in this pass:** the primary Calder/Stahl heart-rate allometry (Stahl 1967, *J Appl Physiol* 22:453–460 was retrieved but is a *respiratory*-variable paper and its scan OCRs too poorly to extract a heart-rate row) — **and therefore the `f = 241·M^(−0.25)` prefactor is NOT-MEASURED and is no longer printed as sourced: `241` appears nowhere in Lindstedt & Hoppeler 2023, which states the exponent and no coefficient, so the value was sourced to neither its citation nor its primary**; **Alexander et al. (1979), *J Zool* 189:305–314** (paywalled; publisher and ResearchGate both returned 403 — the `M^0.31`/`M^0.35` exponents, mass range and species count are via secondary sources, and those give the count as **37** against the **32** printed above; the *direction* of the result is corroborated, so the elastic-similarity NEGATIVE stands regardless); **a 37 °C diffusion coefficient for O₂ in water** (the `R_max` calculation runs on BNID's room-temperature `D`; the mismatch and its ~0.95 mm consequence are stated at the calculation rather than buried); Meiri & Dayan (2003) primary text (percentages taken from Teplitsky & Millien 2014 — an upstream prior, per **M22**); a primary source for resting human VO₂ = 250 mL/min; White & Seymour (2003) confidence intervals (the paper itself **is** now readable at PMC153045 and its exponents, exclusions and interordinal `n`=15 were read this pass — the CIs were not); Kleiber 1932 and Rubner 1883 primary texts (both cited via Kolokotrones et al. 2010 and standard secondary sources); Hayssen & Lacy (1985) and Heusner (1982)/Feldman & McMahon (1983) on the intraspecific ≈2/3 vs interspecific ≈3/4 split — **all cited here via MacKay 2011, not read.**

## HONEST FENCE — OBSERVED-CONTESTED

This chapter is fenced **OBSERVED-CONTESTED**, and the fence is on the flagship, not the periphery. *That metabolic rate rises sublinearly with mass* is OBSERVED-REPLICATED and not in doubt. *What the exponent is* is disputed by competent people using overlapping data and reaching non-overlapping confidence intervals — and the leading resolution (curvature) is itself under a serious live objection (MacKay 2011) that its `b₁` is a unit artifact, that it buys ~10% of residual variance, that a rejected 1985 model was not cited, and that the curvature may be a **between-Order artifact** — Order by Order only the Rodentia retain a significant quadratic, though MacKay concedes in the same paragraph that pooled across all eutheria it *"remains significant"* under his own test. **And that objection drew a reply** (Deeds, Savage & Fontana 2011) which concedes the `b₁` artifact but argues it is irrelevant, since only `b₂` carries the curvature claim — while leaving MacKay's Hayssen & Lacy and marsupial receipts unanswered. **The claim, the resolution, and the objection to the resolution are all contested. Print all three, at full strength, including the half that does not suit the fence.**

Individual rows carry their own classes: the geometry (`σ ∝ L`, `S/V = 3/R`, `t ∝ L²/D`) is as close to settled as this wing gets, because it is arithmetic under stated assumptions; the mechanisms (WBE, elastic similarity, MLBH) are MODELED or HYPOTHESIZED and their assumptions are their fence; several rows are NOT-MEASURED.

Per **Gould & Lewontin (1979)**, *"The Spandrels of San Marco and the Panglossian Paradigm"*: none of the above establishes that any scaling relation is an optimum. Drift, phylogenetic inertia, developmental constraint, pleiotropy, and frozen accidents produce exponents that optimise nothing — and an exponent is an unusually easy thing to find a story for after the fact. **Nature's authority here is precise and limited: it has already run a very long parallel search under real physical constraints in which the failures were deleted.** Convergence is therefore evidence of a constraint-optimum, and every exponent above is a **hypothesis generator**. It is not a proof. Per repo rule **M7**, a design taken from this chapter must still beat a **tuned** baseline on a **pre-registered** metric with a discriminator that collapses the gain, or it is recorded **NEGATIVE**.

## Not claimed

- **Not claimed:** that metabolic rate scales as `M^(3/4)`. Nor as `M^(2/3)`. The chapter's position is that the question is malformed as usually asked, because the log-log relation carries curvature — and that *this* position is contested too, and the contest is printed.
- **Not claimed:** that Kolokotrones et al. (2010) settled the Kleiber dispute. It supplied a mechanism for the *variance in reported exponents* and a sign-error refutation of WBE's finite-size prediction. MacKay (2011) disputes the model that did so.
- **Not claimed:** that the WBE model is refuted as a class. Its specific 1997 vascular geometry predicts curvature of the wrong sign; modified variants recover convexity. Network-based explanation is alive; one geometry is not.
- **Not claimed:** that ~10⁹ heartbeats per lifetime is an invariant. Measured: 7.3 ± 5.6 × 10⁸ with a 77% CV (*on the stated reading of Levine's undefined `±` as a SD*), an order of magnitude lower in fish, and **humans ~4× above the mammalian mean**. Composing the measured exponents gives `M^(−0.097)`, not `M^0`.
- **Not claimed:** that humans' longevity outlier status is explained here. It is recorded as data, not narrated. Levine's own speculation about extending life by cardiac slowing is **his hypothesis, not a result**, and inferring an intervention from a cross-species correlation is the defect this chapter exists to prevent.
- **Not claimed:** that cities and organisms are the same kind of thing, or that superlinear urban scaling is established. Leitão et al. (2016) show the verdict is model-dependent.
- **Not claimed:** that Bergmann's rule follows from surface-to-volume. The conformity rate (~65–76%) is an observation; the S/V mechanism is a hypothesis about why, and latitude confounds altitude, aridity, vegetation and food.
- **Not claimed:** that the `R_max ≈ 0.78 mm` calculation is a measurement. It is a sphere model with a uniform sink, stated inputs, and a factor-of-~2 residual against the observed Krogh radius. The residual is printed because a model that hides its residual is not doing work.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** The NATURA classes (OBSERVED-REPLICATED / OBSERVED-CONTESTED / MODELED / HYPOTHESIZED / INADMISSIBLE / NOT-MEASURED) and the UNI ledger's four values (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. This chapter contains **zero** UNI claims.
- **QUAESTIO-APERTA:** "full human" and "the next evolution beyond human" appear nowhere here as target, milestone, or deliverable. They are permanent open questions. Nothing about the human heartbeat or lifespan outlier bears on them, and reading one into the other would be the exact lane-crossing this wing exists to prevent.
