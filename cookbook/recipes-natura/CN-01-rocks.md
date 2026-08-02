# CN-01 — Rocks: the mineral substrate

> **What you are building.** A working model of the mineral substrate — what every other chapter's system is made of and standing on — and this cookbook's **reference case for a boundary with no internal model**: the zero of the ladder, against which every claim about inference gets calibrated. Every number below carries a source you can check or is written NOT-MEASURED. Nothing here raises any UNI rung — a citation to geology is never a UNI gate.

---

## What a mineral is — and where the definition actually frays

The textbook line — a naturally occurring solid with a definite chemical composition and an ordered atomic arrangement — is useful and slightly false. The definition that governs the discipline is the IMA Commission on New Minerals and Mineral Names' (Nickel 1995, *Can Mineral* 33:689–690), and its operative wording is looser and more honest: in general terms a mineral is an element or chemical compound that is **normally crystalline** and that has been formed as a result of **geological processes**.

Read the hedges, because they are the content. **"Normally crystalline"**, not crystalline: amorphous phases have been admitted (georgeite, calciouranoite), and metamict substances — once crystalline, lattice destroyed by ionizing radiation — are admitted if the pre-metamict phase can be established. **"Geological processes"** does the real work: ice is a mineral, liquid water is not; mercury is a mineral though never crystalline on Earth; anthropogenic substances are **not** minerals however identical, only "synthetic equivalents".

So the category is not a natural kind read off nature. It is a **committee's operational definition with a curation policy**, explicitly non-retroactive. As of the January 2026 IMA-CNMNC list, 6,200 species are valid — a state of a ledger, not a fact about the Earth.

## The master building block, and one genuine hierarchical build rule

Take one silicon, put four oxygens around it: the **SiO₄⁴⁻ tetrahedron**. Si–O in tetrahedral coordination runs ~1.62 Å on average (individual bonds 1.55–1.72 Å); a regular tetrahedron puts O–Si–O at 109.47°, and the Hückel energy of an isolated silicate ion minimises at exactly that angle when the four bonds are equal.

Now the rule. Tetrahedra link by **sharing corner oxygens** — never edges or faces in ordinary silicates, because that would push the Si⁴⁺ cations too close. Count the shared ("bridging") oxygens per tetrahedron and you generate, with no free parameters, the entire silicate kingdom:

| Class | Bridging O per tetrahedron | Unit | Si:O | Dimensionality | Example |
|---|---|---|---|---|---|
| **Neso**silicate | 0 | SiO₄ | 0.25 | isolated points | olivine |
| **Soro**silicate | 1 | Si₂O₇ | 0.286 | pairs | epidote group |
| **Cyclo**silicate | 2 | SiₙO₃ₙ | 0.333 | rings | beryl, tourmaline |
| **Ino**silicate, single chain | 2 | SiO₃ | 0.333 | 1-D | pyroxene |
| **Ino**silicate, double chain | 2.5 | Si₄O₁₁ | 0.364 | 1-D, ladder | amphibole |
| **Phyllo**silicate | 3 | Si₂O₅ | 0.40 | 2-D | mica, clay |
| **Tecto**silicate | 4 | SiO₂ | 0.50 | 3-D | quartz, feldspar |

This is Bragg's classification (Bragg 1930; Náray-Szabó 1930, on Machatschki's 1928 suggestion that the *kind and degree of linkage* of tetrahedra should be the classifying principle) — a real hierarchical build rule and the spine of this chapter: **one monomer, one polymerisation parameter, the whole series**. The Si:O and bridging-oxygen columns are computed here from stoichiometry; check them, they are arithmetic.

## The closed enumeration — and the place nature walked out of it

How many essentially different ways can matter be periodically ordered in three-dimensional space? The answer is **230**, and it is a theorem, not a survey. Combine 14 Bravais lattices with 32 crystallographic point groups (sorting into **7 crystal systems**: triclinic, monoclinic, orthorhombic, tetragonal, trigonal, hexagonal, cubic), add screw axes and glide planes, and the enumeration closes. Fedorov (1891) and Schoenflies (1891) did it independently; the corrected list of 230 emerged from their correspondence by 1892.

Say plainly why this is remarkable. **Mineralogy is one of the very few natural sciences whose hypothesis space over structure is closed and written down.** There is no complete enumeration of possible proteins, organisms, ecosystems or programs; here there is — 6,200 known species across an alphabet of 230 letters, and the alphabet is complete. For an inference engine that is a gift: the prior over structure is a proper, finite, enumerable distribution.

**Now the counterweight, which is the better lesson.** The 230 enumerate **periodic** order. In 1984 Shechtman, Blech, Gratias & Cahn (*Phys Rev Lett* 53:1951–1953) reported a phase with long-range orientational order, no translational symmetry, and five-fold diffraction symmetry — forbidden in every one of the 230. The reaction was not curiosity. Linus Pauling: *"There is no such thing as quasicrystals. Just quasiscientists."* Shechtman took the 2011 Nobel Prize in Chemistry, and in 2009 Bindi, Steinhardt, Yao & Lu (*Science* 324:1306–1309) reported a natural quasicrystal in a khatyrkite-bearing sample from the Koryak Mountains. The phase was named **icosahedrite**, Al₆₃Cu₂₄Fe₁₃, with six five-fold axes, only in 2011 (Bindi et al., *Am Mineral* 96:928–931, doi:10.2138/am.2011.3758), and its host was shown to be the **Khatyrka meteorite** in 2012 (Bindi et al., *PNAS* 109:1396–1401). Carry the three scopes separately: the 2009 paper neither named the mineral nor claimed a meteorite.

The theorem was never wrong; its **scope** was misread, then forgotten, then defended. "Periodic" was an axiom nobody restated out loud, so a replicated observation was rejected for years for contradicting a proof whose premises had gone silent — in the best-enumerated science we have.

## Bowen's series: the recipe, and the spine closing on itself

Bowen (1922), *J Geol* 30(3):177–198, established from experiment and observation the order in which silicate minerals crystallise out of cooling basaltic magma — a genuine temperature-ordered recipe. A **discontinuous branch** (olivine → pyroxene → amphibole → biotite, each reacting with the melt to become the next) and a **continuous branch** (Ca-rich → Na-rich plagioclase, one solid solution re-equilibrating continuously) converge at low temperature on K-feldspar → muscovite → **quartz**.

Look at the discontinuous branch with the previous section's table in hand:

> olivine (neso, 0 bridging O) → pyroxene (single chain, 2) → amphibole (double chain, 2.5) → biotite (sheet, 3) → quartz (framework, 4)

**Bowen's temperature order is the polymerisation order.** Two series established independently — one by melting experiments, one by X-ray structure — turn out to be the same list. Cooling is polymerising. The spine closes on itself, checkable against the table above rather than taken on faith. Fence it: the *ordering correspondence* is observed; the *causal story* (as melt evolves, silica activity rises and tetrahedra progressively link) is **MODELED**, and Bowen's series is a scheme for one starting composition under fractionation, not a law of igneous rocks.

## Three process routes, one control surface

**Igneous** (crystallise from melt), **sedimentary** (weather, transport, deposit, cement), **metamorphic** (recrystallise in the solid state under changed P–T) are process routes, not compositional classes — the same atoms take different routes and land in different structures.

The control surface is the **P–T phase diagram**, and Al₂SiO₅ is the cleanest instrument on it: one composition, three minerals. **Kyanite** (high P), **andalusite** (low P, low T) and **sillimanite** (high T) meet at an invariant point. Two determinations, carried separately and never averaged: Holdaway (1971), *Am J Sci* 271:97–131, put it near ~501 °C, ~3.8 kbar; Holdaway & Mukhopadhyay (1993), *Am Mineral* 78:298–315, reevaluated it to **504 ± 20 °C, 3.75 ± 0.25 kbar**. Print both or the instruction to carry the dispute is unexecutable — a reader shown one number cannot avoid averaging two. The 1971 point falls inside the 1993 brackets: narrow agreement, not licence to merge. This row is scoped to the **Holdaway line of work**; the wider aluminosilicate triple-point literature is not carried here. Find kyanite in a rock and you have read a coordinate off that surface: the rock is a **thermobarometer that was left running**.

## Hardness: the ordinal trap, with receipts

Mohs (1822, *Grundriß der Mineralogie*) ranked ten minerals 1–10 by which scratches which. It is an **ordinal scale and nothing more**: the scale is not linear, the integers do not license interpolation, and the scratching procedure was never well defined. Mohs 4 is not twice Mohs 2; you cannot take a ratio, an average or a difference; there is no meaningful "mean hardness" of a rock.

The receipts are better than the argument. Whitney, Broz & Cook (2007), *Am Mineral* 92:281–288, Table 1, measured indentation hardness (H), toughness (K_IC) and indentation modulus (E*):

| Mohs | Mineral | Microhardness (GPa) | DSI hardness (GPa) | K_IC (MPa·m^½) | E* (GPa) |
|---|---|---|---|---|---|
| 5–5.5 | kyanite (001) | — | 14.8 ± 1.4 | — | 186 ± 8 |
| 6 | orthoclase (101) | 6.9 ± 0.7 | 9.1 ± 0.6 | 1.1 ± 0.4 | 89 ± 7 |
| 6–6.5 | periclase MgO \* | **5.3 ± 1.0** | 9.4 ± 1.4 | 3.9 ± 0.8 | 233 ± 12 |
| 6.5–7 | sillimanite (010) | 11.0 ± 2.7 | 15.9 ± 1.5 | 1.6 ± 1.5 | 207 ± 6 |
| 6.5–7 | andalusite (001) | 9.8 ± 1.5 | 11.6 ± 0.3 | 1.8 ± 0.5 | 232 ± 6 |
| 7 | quartz (0001) | 12.1 ± 1.1 | 14.5 ± 0.4 | 1.5 ± 0.3 | 117 ± 3 |
| 7 | kyanite (010) | 11.9 ± 1.7 | 16.3 ± 1.6 | — | 253 ± 19 |

*\* **Polycrystalline** — Whitney et al.'s own Table 1 footnote. Periclase is a **synthetic** reference material, not a single crystal ("With the exception of the cubic zirconia and periclase samples, which were synthetic"), and the authors caution that "comparison with single-crystal values for MgO are more appropriate." Mohs is a scratch test on single crystals. Carrying that footnote is not pedantry here — it is the whole thesis of this chapter applied to its own table.*

Two rows break the scale as a physical quantity — and they are the **clean** ones, not the tempting one:

1. **Kyanite (001), the lowest Mohs entry in the table at 5–5.5, is *harder* by DSI indentation (14.8 GPa) than orthoclase at Mohs 6 (9.1) and periclase at Mohs 6–6.5 (9.4).** A rank inversion on a single crystal, no reference-sample caveat attached: the ordinal ordering is not the hardness ordering.
2. **Kyanite appears twice, at Mohs 5–5.5 and Mohs 7 — same crystal, same composition, different faces.** Hardness is not a scalar property of a substance; it is directional, and the modulus swings 186 → 253 GPa with the indented plane.

**The receipt this chapter declines to use**, recorded so nobody re-imports it: periclase (Mohs 6–6.5) is softer than orthoclase (Mohs 6) **by microhardness** — 5.3 vs 6.9 GPa — which looks like the cleanest inversion on the table and is not. Periclase is the polycrystalline synthetic; and the **DSI column of the same table preserves the Mohs order for that pair** (9.4 ± 1.4 vs 9.1 ± 0.6, error bars overlapping). Both columns are indentation, so "softer by indentation" would be true only of the column that suits the argument. It points the right way and carries no weight. Note also that Whitney et al. conclude something narrower than "the scale is destroyed": that minerals, "particularly those in the range of 6–8, may vary considerably in indentation hardness."

The general result, from the companion study on the Mohs standards themselves (Broz, Cook & Whitney 2006, *Am Mineral* 91:135–142, doi:10.2138/am.2006.1844): none of the measured properties increases consistently or linearly with Mohs number across the whole scale. The reason is mechanistic — **scratch resistance is a composite** of hardness, fracture toughness *and* elastic modulus. Three properties collapsed into one integer; the map is not invertible, so no care recovers a physical quantity from a Mohs number. Keep the scale — a superb 200-year-old field test costing one fingernail. Just never do arithmetic on it.

## Deep time is measured, not narrated

The claim that the Earth is billions of years old is not a story. It is a decay-constant measurement with an error bar, and the constants are the falsifiable part.

| Isotope | Half-life | Source |
|---|---|---|
| ²³⁸U | (4.4683 ± 0.0024) × 10⁹ yr | Jaffey et al. (1971), *Phys Rev C* 4:1889–1906 |
| ²³⁵U | (7.0381 ± 0.0048) × 10⁸ yr | Jaffey et al. (1971) |
| ⁴⁰K | (1.2522 ± 0.0027) × 10⁹ yr | DDEP 2025 eval.; Mougeot et al., *Metrologia* 63(1) (2026), doi:10.1088/1681-7575/ae3733 |
| ⁸⁷Rb | 49.61 ± 0.16 Ga | Villa, De Bièvre, Holden & Renne (2015), *GCA* 164:382–385 |
| ¹⁴⁷Sm | 106.25 ± 0.38 Ga | Villa et al. (2020), *GCA* (IUPAC-IUGS) |

Three details that matter more than the ages:

- **²³⁸U/²³⁵U is a paired clock.** Two isotopes of one element, in one mineral, half-lives differing 6.3×, decaying to two lead isotopes. The concordia is **internally checkable**: if the two disagree, the grain leaked, and it says so. A self-falsifying measurement is rare and worth copying.
- **⁴⁰K needs an extra measured parameter, and the branches must close.** ⁴⁰K has two real destinations: **β⁻ to ⁴⁰Ca at 89.56(7)%**, and **electron capture to ⁴⁰Ar at ≈10.44%** — which sum to 100.00%, as two channels must. The EC branch is itself split, and the split is the whole point: **10.34(7)%** lands on an *excited* ⁴⁰Ar state (the 1460.8 keV γ), while **0.098%** goes straight to the ⁴⁰Ar **ground state**, emitting no γ at all. K–Ar dating measures all radiogenic ⁴⁰Ar, so it uses **EC₀ + EC\***. Quote 10.34% as "the EC branch" and you have silently dropped a channel and lost 0.10% of the decay — and the branches no longer close, which is the arithmetic tell. That ground-state branch was only *observed* in 2023 (KDK collaboration, *Phys Rev Lett* 131:052503), at roughly half the long-used theoretical prediction; it is the reason the 2025 DDEP re-evaluation exists, and that re-evaluation also moved the half-life from 1.248 ± 0.003 to 1.2522 ± 0.0027 × 10⁹ yr. The constants are still moving.
- **¹⁴⁶Sm *was* openly contested — then someone ran the experiment.** Two half-lives were in community use, ~68 Ma and ~103 Ma; the IUPAC-IUGS Task Group (Villa et al. 2020) **declined to recommend either**, instructing authors to compute both — but conditioned that on the words *"pending dedicated re-investigations."* Those words are a falsifier, and it has fired. Chiera, Sprung, Amelin, Dressler, Schumann & Talip (2024), *Sci Rep*, doi:10.1038/s41598-024-64104-6, re-determined ¹⁴⁶Sm by combined mass spectrometry and α-counting at **92.0 ± 2.6 Ma (k = 1)** — agreeing with **neither** legacy value — and record that the shorter one was **retracted** by its authors after sample-processing inconsistencies. So the dispute is not the two-value standoff it is famous as, and "compute both" is superseded. Carry the dispute *as it now stands*, not as it was framed: the discipline is to re-check a falsifier that reads "someone does the experiment" before repeating the framing — which is precisely the failure the two-thirds figure below is convicted of.

What it buys: **CAIs at 4567.30 ± 0.16 Ma** (Connelly et al. 2012, *Science* 338:651–655), and a Jack Hills detrital zircon at **4404 ± 8 Ma** (Wilde, Valley, Peck & Graham 2001, *Nature* 409:175–178) whose zoned δ¹⁸O (7.4 to 5.0‰) implies liquid water on Earth within ~160 Myr of t=0. A grain of sand carries that, and the number has an error bar.

## The interior is a posterior — Vp/Vs and the signal that isn't there

The chapter's tightest link to the method. Nobody has sampled below the crust; the deepest borehole — Kola SG-3 — reaches **12,262 m** (Popov, Pevzner, Pimenov & Romushkevich 1999, *Tectonophysics* 306:345–366, doi:10.1016/S0040-1951(99)00065-7), about 0.19% of the way to the centre. Everything below is a **hidden state**, and the Preliminary Reference Earth Model (Dziewonski & Anderson 1981, *Phys Earth Planet Inter* 25:297–356) is not a measurement of it — it is a **posterior over a parameterised generative model**, conditioned on ~1,000 normal-mode periods, ~500 summary travel times, ~100 mode Q values, the Earth's mass and moment of inertia, and ~1.75 × 10⁶ ISC travel-time observations. **Seismic tomography is the inversion; the model is the belief.**

| Depth (km) | ρ (g/cm³) | Vp (km/s) | Vs (km/s) | Vp/Vs | ν |
|---|---|---|---|---|---|
| 0–3 (ocean) | 1.02 | 1.45 | **0.00** | ∞ | 0.5 |
| 3–15 (upper crust) | 2.60 | 5.80 | 3.20 | 1.813 | 0.281 |
| 24.4, below Moho | 3.38 | 8.02 | 4.40 | 1.825 | 0.285 |
| 400 (above → below) | 3.54 → 3.72 | 8.91 → 9.13 | 4.77 → 4.93 | 1.867 → 1.852 | 0.299 → 0.294 |
| 670 (above → below) | 3.99 → 4.38 | 10.27 → 10.75 | 5.57 → 5.95 | 1.843 → 1.808 | 0.291 → 0.280 |
| 2891, mantle side | 5.57 | 13.72 | 7.26 | 1.888 | 0.305 |
| 2891, core side | 9.90 | 8.06 | **0.00** | ∞ | 0.5 |
| 5149.5, outer core | 12.17 | 10.36 | **0.00** | ∞ | 0.5 |
| 5149.5, inner core | 12.76 | 11.03 | **3.50** | 3.147 | 0.444 |
| 6371 (centre) | 13.09 | 11.26 | 3.67 | 3.071 | 0.441 |

*(ρ, Vp, Vs from the tabulated PREM_1s model, IRIS/SAGE EMC; Vp/Vs and ν = (Vp² − 2Vs²)/(2(Vp² − Vs²)) computed here. **The Vs = 0 entries — ocean and outer core — are imposed by PREM's parameterisation, not fitted.** They are model inputs, and the ∞ and 0.5 beside them follow arithmetically from an assumption rather than from data.)*

**The decisive observation is an absence** — and it is an **observation**, which is exactly why it must not be cited to PREM. Oldham (1906), *Q J Geol Soc* 62:456–475, established a core from seismic travel times; Gutenberg (1913), *Phys Z* 14:1217–1218, placed the boundary near 2900 km; Jeffreys (1926), *MNRAS Geophys Suppl* 1:371, doi:10.1111/j.1365-246X.1926.tb05385.x, established that the core is **liquid**. S-waves do not traverse it, because a liquid has no shear modulus: μ = 0. *The Earth's outer core is liquid, and we know it because of a signal that is not there.*

**Now the honest part, in the section that preaches this exact distinction.** PREM's Vs = 0 through the outer core is **not** that observation and is not a result. PREM *parameterises* the outer core as fluid and **imposes** μ = 0 a priori: the zero is a model **input**. Quoting it to five decimals as "0.00000" would dress a hard-coded constant as a five-significant-figure posterior, and citing PREM for outer-core liquidity cites a belief in place of the datum that constrains it. The observation constrains the model; the model then reproduces the constraint it was handed, which is not evidence. That ordering — observation first, model downstream — is the section's whole claim, and it only works if the zero is labelled an axiom. *(One caveat worth carrying honestly: Jeffreys' most persuasive argument was not the shadow zone but a rigidity budget from Earth tides. The textbook story is tidier than the history.)*

At 5149.5 km shear returns — Vs = 3.50 km/s — and *that* number is fitted, not imposed: the inner core transmits shear and is solid, at ν ≈ 0.44, close to the liquid limit of 0.5. *(PREM model output; the interpretation is unsettled and not claimed here.)* Note the check built into the table's top row: PREM's first 3 km is seawater, ρ = 1.02, Vp = 1.45, Vs = 0 — the model reproduces a thing you can dip a hand in.

**This is the epistemic term in EFE doing real work**: the S-wave shadow resolves ambiguity about a state no pragmatic action could ever reach.

## Blanket analysis: the reference case for no internal model

Per **NA-04** and rule **M12** (WORLD ⊥ BODY ⊥ MIND, two typed Markov blankets), state exactly what a rock is. A rock has a **boundary** — a real partition of inside from outside — plus **internal states**, and **sensory states** in the trivial sense that the outside impinges on it. What it lacks:

1. **No internal states that model external states.** Nothing inside the rock stands in for anything outside it *for the rock's own use*.
2. **No active states.** It does nothing that changes its own sensory states. No policies π, therefore no policy selection, therefore no EFE.
3. **No preferences C.** No outcome is preferred, so "surprise" is undefined for it — and no `C` means no pragmatic term.
4. **No temporal depth.** No prediction, no counterfactual, no next state it is *for*.

**And here is the trap the shared vocabulary sets.** A crystal at equilibrium genuinely does minimise a **free energy** — Gibbs free energy, `G = H − TS`. That minimisation is real, measured, and is why the P–T diagram works at all. It is **not** variational free energy: no generative model, no `q(s)`, no posterior, no accuracy−complexity trade. **Two different quantities wearing one name.** Sliding from "rocks minimise free energy" to "rocks perform inference" is a pun, not an argument, and it is the most seductive error available in this cookbook. The rock is the reference case precisely because it makes the pun visible.

**The rock is a write-once medium with no reader.** A zircon *records* its crystallisation age; its δ¹⁸O zoning *records* the water it grew from; kyanite *records* a P–T coordinate — genuine storage, at high fidelity, over 4.4 Gyr. But the rock never reads it, and never uses it to predict, act or persist. **The posterior lives in the geochronologist, never in the zircon.** Storage is not inference; a trace is not a belief.

**Why it matters for the ladder:** the rock is L0 — the floor, the calibration point. Any system whose only claim is "it has a boundary and settles into a low-energy state" has claimed exactly as much as a pebble. Stating that floor is what makes the higher rungs cost something.

## The rocks are downstream of the cells — and the number is not what you were told

Hazen et al. (2008), *Am Mineral* 93:1693–1720, proposed that Earth's mineralogy **evolved** in ten stages, driven by progressive separation of elements from a near-uniform pre-solar nebula, widening ranges of P, T and the activities of H₂O/CO₂/O₂, and **far-from-equilibrium conditions generated by living systems**: ~12 "ur-minerals" → ~250 species in unweathered meteorite and lunar samples → ~1,500 by purely physical and chemical processes → thousands more only after life. *(Stage counts from the authors' institutional summary; the primary PDF returned HTTP 404 this pass — see the open row.)* The 2008 abstract concluded that biochemical processes may be responsible, directly or indirectly, for most of Earth's 4,300 then-known species — the widely repeated **"two-thirds"** figure.

**Check the number, because the brief for this chapter asserted it and it does not survive.** Hazen & Morrison (2022), *Am Mineral* 107:1262–1287, doi:10.2138/am-2022-8099, surveyed 57 paragenetic modes across 5,659 species and reported, explicitly contrary to previous estimates, that only **~34%** of mineral species form *exclusively* as a consequence of biological processes — naming the contrast with the two-thirds estimate of Hazen et al. (2008). **The same author superseded his own headline number.** Anyone citing "two-thirds of minerals require life" today is citing a figure its originators withdrew.

What actually stands, from the 2022 audit:

- **At least 2,707 of 5,659 species (47.8%)** form under biological influence, and **more than 1,900 exclusively** through biology — which the authors characterise as a significant, pervasive **planetary biomarker**.
- **1,998 species** arise by near-surface oxidative weathering/alteration — the second-largest factor in Earth's mineral diversity, and it exists because photosynthesis oxygenated the atmosphere.
- **The largest factor is not life. It is water: at least** 4,583 minerals — **81.0%** — arise through water–rock interactions. Much of the diversity was established within the **first 250 Myr**.

Read those "at least"s as the authors wrote them. 2,707 and 4,583 are explicit **lower bounds**, not point estimates, so the water-over-life ranking compares two floors — it is not a measured margin, and the gap between them is not a quantity. **And note what class this evidence can bear.** It is one survey, by one author team, resting on expert assignment of species to *"our proposed 57 paragenetic modes"* — their words, alongside *"we welcome additions and corrections."* No independent group has replicated it. That is a classification scheme applied to a database: closer to **MODELED** than to observed-and-replicated, and the rows below are classed accordingly. The chapter's own narrative is the argument for that caution — this same team's 2008 headline stood wrong for fourteen years until they themselves overturned it. **The 2022 audit has not been independently checked either.** Saying so does not weaken the self-correction lesson; it *is* the lesson, applied one turn further.

The load-bearing fact survives, restated correctly: **the mineral kingdom is not a passive stage that life stands on — it is roughly half a product of life, and the biggest rewrite came from an atmosphere that cells built.** Turquoise and malachite are downstream of photosynthesis. For "nature as authority" this is the strongest available statement of why substrate and system do not separate into clean layers: read a rock carefully enough and you are reading a biosignature.

And the correction teaches better than the fact. The two-thirds figure was famous, repeated for fourteen years, and wrong — caught by the author re-auditing his own claim against a bigger dataset, not by a critic. **That is what a working honesty fence looks like from the inside.**

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `n_IMA` | 6,200 | valid species | IMA-CNMNC list, **January 2026** — a dated snapshot, not a constant | OBSERVED-REPLICATED | IMA-CNMNC, *The New IMA List of Minerals* (2026-01): "the list includes selected information on the 6200 currently valid species" | Consult current CNMNC master list; a different count. **This row is built to go stale — see `r_IMA`** |
| `r_IMA` | ~78–105 (mean ~91 over 2024-09 → 2026-01) | valid species added per year | IMA-CNMNC list-to-list deltas; **the rate is not steady** — the most recent interval is the slowest | OBSERVED-REPLICATED | Computed here from successive IMA Master Lists: 6079 (2024-09) → 6126 (2025-03) → 6161 (2025-07) → 6200 (2026-01) | Recount from successive CNMNC master lists; a rate outside the band |
| `d_Si–O` | ~1.62 (range 1.55–1.72) | Å | Si–O, tetrahedral coordination, silicate structures | OBSERVED-REPLICATED *(primary not read this pass)* | Si–O bond-length literature (Brown & Gibbs, *Am Mineral*; Cruickshank's rule ~1.63 Å) | Refine a silicate structure; mean Si–O outside 1.55–1.72 |
| `θ_O–Si–O` | 109.47 | degrees | **ideal** regular tetrahedron; real angles distort | MODELED | Geometry; Hückel-energy minimum at ideal angle (*Am Mineral* 57:1614) | A regular-tetrahedron silicate at a different angle |
| Si:O series | 0.25 → 0.286 → 0.333 → 0.364 → 0.40 → 0.50 | dimensionless | neso→soro→cyclo/ino₁→ino₂→phyllo→tecto | MODELED | Computed here from stoichiometry | Arithmetic error |
| bridging O | 0 → 1 → 2 → 2.5 → 3 → 4 | per tetrahedron | same series | MODELED | Computed here | Arithmetic error |
| `N_sg` | **230** (32 point groups, 14 Bravais lattices, 7 systems) | space groups | **periodic** order in 3-D Euclidean space — a closed **formal** result about the space, not a survey of rocks | **MODELED** (closed formal result; deliberately **not** an empirical class — no mineral could refute it, and no field replication bears on it) | Fedorov (1891); Schoenflies (1891); list corrected to 230 by 1892 | **Formal, not empirical:** re-derive the enumeration — exhibit a 231st periodic group, or a duplicate among the 230 |
| quasicrystal | 5-fold symmetry, no translational periodicity | — | **outside all 230**; synthetic 1984, natural 2009, **named 2011**, **meteoritic 2012** — three papers, three scopes | OBSERVED-REPLICATED | Shechtman, Blech, Gratias & Cahn (1984), *Phys Rev Lett* 53:1951–1953 (synthetic); Bindi, Steinhardt, Yao & Lu (2009), *Science* 324:1306–1309 (natural quasicrystal observed — named nothing, claimed no meteorite); Bindi et al. (2011), *Am Mineral* 96:928–931, doi:10.2138/am.2011.3758 (**the name** icosahedrite + the Al₆₃Cu₂₄Fe₁₃ formula); Bindi et al. (2012), *PNAS* 109:1396–1401 (**Khatyrka meteorite** origin) | Show icosahedrite is periodic or a twinning artefact |
| Al₂SiO₅ triple pt | **both carried:** ~501 °C, ~3.8 kbar (1971) **and** 504 ± 20 °C, 3.75 ± 0.25 kbar (1993) | °C, kbar | kyanite–andalusite–sillimanite invariant point; **scoped to the Holdaway line of work** — the wider aluminosilicate triple-point literature is not carried in this row | **OBSERVED-CONTESTED** | Holdaway (1971), *Am J Sci* 271:97–131; reevaluated Holdaway & Mukhopadhyay (1993), *Am Mineral* 78:298–315 | Re-run the brackets; coordinates outside **504 ± 20 °C, 3.75 ± 0.25 kbar**. Do not average the two — the 1971 point falls *inside* the 1993 brackets, which is agreement, not licence to merge |
| `H_qtz` | 12.1 ± 1.1 (micro) / 14.5 ± 0.4 (DSI) | GPa | quartz (0001) | OBSERVED-REPLICATED | Whitney, Broz & Cook (2007), *Am Mineral* 92:281–288, Table 1 | Independent indentation on (0001) outside range |
| `E*_qtz` | 117 ± 3 | GPa | quartz (0001), indentation modulus | OBSERVED-REPLICATED | Whitney et al. (2007), Table 1 | As above |
| `K_IC,qtz` | 1.5 ± 0.3 | MPa·m^½ | quartz (0001) | OBSERVED-REPLICATED | Whitney et al. (2007) | As above |
| `H_orth` | 6.9 ± 0.7 (micro) / 9.1 ± 0.6 (DSI) | GPa | orthoclase (101), **Mohs 6** | OBSERVED-REPLICATED | Whitney et al. (2007), Table 1 | As above |
| `H_per` | **5.3 ± 1.0** (micro) / 9.4 ± 1.4 (DSI) | GPa | periclase MgO, **Mohs 6–6.5** — **polycrystalline synthetic reference material, not a single crystal** (Whitney et al. Table 1 footnote; the authors: "comparison with single-crystal values for MgO are more appropriate"). Softer than orthoclase **by microhardness only**; the **DSI column preserves Mohs order** for the pair (9.4 ± 1.4 vs 9.1 ± 0.6, overlapping) | OBSERVED-REPLICATED *(the values)* / **scope-mismatched for any rank-inversion claim** — Mohs is a single-crystal scratch test | Whitney et al. (2007), Table 1 | Re-indent **single-crystal** MgO; the microhardness inversion disappears |
| `K_IC,per` | 3.9 ± 0.8 | MPa·m^½ | periclase — toughest of that set, and among the softest; **polycrystalline synthetic** (as above) | OBSERVED-REPLICATED | Whitney et al. (2007) | As above |
| `H_ky` | Mohs 5–5.5 on (001) **vs** Mohs 7 on (100)/(010); **DSI 14.8 ± 1.4 on (001)**; E* 186 ± 8 → 253 ± 19 | GPa | kyanite — **one crystal, two Mohs numbers, face-dependent**; and (001), the table's **lowest** Mohs entry, is **harder by DSI** than orthoclase (9.1) and periclase (9.4) — **the clean rank inversion: single-crystal, no reference-sample caveat** | OBSERVED-REPLICATED | Whitney et al. (2007), Table 1 | Indent both faces and find isotropy; or find (001) softer than orthoclase by DSI |
| Mohs linearity | **none** | — | Mohs vs indentation H, K_IC, E* across the scale | OBSERVED-REPLICATED | Broz, Cook & Whitney (2006), *Am Mineral* 91:135–142, doi:10.2138/am.2006.1844 | Exhibit a monotone linear map from Mohs to any measured property |
| `ρ` (PREM) | 1.02 / 2.60 / 3.38 / 5.57 / 9.90 / 13.09 | g/cm³ | ocean / upper crust / sub-Moho mantle / base of mantle / outer-core top / centre | MODELED (posterior) | Dziewonski & Anderson (1981), *Phys Earth Planet Inter* 25:297–356; tabulated PREM_1s (IRIS/SAGE EMC) | Refit with new data; densities move |
| S-wave shadow | **no S arrival through the outer core** | — | **the observation** — the outer core has no shear strength. This is the datum the model is conditioned on, and it is not PREM | **OBSERVED-REPLICATED** | Oldham (1906), *Q J Geol Soc* 62:456–475 (a core exists); Gutenberg (1913), *Phys Z* 14:1217–1218 (boundary ~2900 km); Jeffreys (1926), *MNRAS Geophys Suppl* 1:371, doi:10.1111/j.1365-246X.1926.tb05385.x (the core is **liquid** — his decisive argument was a tidal rigidity budget, not the shadow itself) | **Observe an S-wave traversing the outer core** |
| `Vs` outer core | **0 (imposed)** | km/s | PREM, 2891–5149.5 km — **a parameterisation constraint, not a fit result**: PREM defines the outer core as fluid and sets μ = 0 a priori | MODELED (**model input** — the one interior number that is *not* output; do not quote it as "0.00000") | PREM tabulated | Not falsifiable *as model output* — it is an assumption. Falsify the **assumption** via the row above |
| `Vs` inner core | 3.50431 (ICB) → 3.66780 (centre) | km/s | PREM inner core — transmits shear; **fitted**, unlike the outer-core zero | MODELED (posterior) | PREM tabulated | Show the inner core does not transmit shear |
| `Vp/Vs` | 1.813 (upper crust) / 1.825 (sub-Moho) / 1.888 (base mantle) / ∞ (outer core) / 3.147 (ICB) | dimensionless | PREM | MODELED | Computed here from PREM tabulated Vpv/Vsv | Arithmetic error |
| `ν` | 0.281 / 0.285 / 0.305 / 0.5 / **0.444** | dimensionless | Poisson's ratio, same horizons; ν = (Vp²−2Vs²)/(2(Vp²−Vs²)) | MODELED | Computed here from PREM | Arithmetic error; interpretation of ν≈0.44 not claimed |
| `t½ ²³⁸U` | (4.4683 ± 0.0024) × 10⁹ | yr | | OBSERVED-REPLICATED | Jaffey et al. (1971), *Phys Rev C* 4:1889–1906 | Re-measure specific activity; outside stated uncertainty |
| `t½ ²³⁵U` | (7.0381 ± 0.0048) × 10⁸ | yr | ratio to ²³⁸U = 6.35× — the concordia's leverage | OBSERVED-REPLICATED | Jaffey et al. (1971) | As above |
| `t½ ⁴⁰K` | (1.2522 ± 0.0027) × 10⁹ | yr | ⁴⁰K half-life *(coverage factor **not read this pass** — fetch the primary)* | OBSERVED-REPLICATED | DDEP 2025 evaluation; Mougeot et al., *Metrologia* 63(1) (2026), doi:10.1088/1681-7575/ae3733 | **Supersedes 1.248 ± 0.003 × 10⁹** — re-evaluate |
| ⁴⁰K branches | β⁻→⁴⁰Ca **89.56(7)%**; EC→⁴⁰Ar **total ≈10.44%** = EC\* **10.34(7)%** (excited state, 1460.8 keV γ) **+** EC₀ **0.098%** (ground state, no γ). **89.56 + 10.44 = 100.00** — two channels, they must close | % | **K–Ar uses EC₀ + EC\***, i.e. *all* radiogenic ⁴⁰Ar — **not** EC\* alone. Quoting 10.34% as "the EC branch" drops a channel and loses 0.10% of the decay | OBSERVED-REPLICATED | DDEP 2025 evaluation (Mougeot et al. 2026, doi:10.1088/1681-7575/ae3733); EC₀ **first observed** by the KDK collaboration, *Phys Rev Lett* 131:052503 (2023): I(EC₀) = 0.098% ± 0.023 (stat) ± 0.010 (sys) — roughly half the long-used prediction, and the reason the 2025 re-evaluation exists | Branches that fail to sum to 100%; or an EC₀ re-measurement outside the KDK uncertainty |
| `t½ ⁸⁷Rb` | 49.61 ± 0.16 | Ga | λ₈₇ = (1.3972 ± 0.0045) × 10⁻¹¹ a⁻¹ | OBSERVED-REPLICATED | Villa, De Bièvre, Holden & Renne (2015), *GCA* 164:382–385 | Independent determination outside stated uncertainty |
| `t½ ¹⁴⁷Sm` | 106.25 ± 0.38 | Ga | λ₁₄₇ = (6.524 ± 0.024) × 10⁻¹² a⁻¹, k = 2 | OBSERVED-REPLICATED | Villa et al. (2020), *GCA* (IUPAC-IUGS recommendation) | As above |
| `t½ ¹⁴⁶Sm` | **92.0 ± 2.6 (k = 1)** — the current determination | Ma | direct re-determination by mass spectrometry + α-counting; agrees with **neither** legacy value | OBSERVED-REPLICATED *(one dedicated determination; **not yet independently repeated**)* | Chiera, Sprung, Amelin, Dressler, Schumann & Talip (2024), *Sci Rep*, doi:10.1038/s41598-024-64104-6 | Independent re-determination outside 92.0 ± 2.6 |
| `t½ ¹⁴⁶Sm` (legacy) | ~68 **(retracted)** *or* ~103 | Ma | **SUPERSEDED FRAMING — do not "compute both."** Villa et al. (2020) declined to recommend either *"pending dedicated re-investigations"*; that re-investigation was published in 2024. The ~68 Ma value was **retracted by its authors** (Kinoshita et al.) after inconsistencies in sample processing | **SUPERSEDED (framing superseded)** | Villa et al. (2020), *GCA* (IUPAC-IUGS); retraction + history recorded in Chiera et al. (2024) | **This row's falsifier already fired.** Kept as the receipt for why "carry both" no longer applies — and as a reminder to re-check any falsifier that reads "someone does the experiment" |
| `t_CAI` | 4567.30 ± 0.16 | Ma | oldest solar-system solids; U-corrected Pb-Pb | OBSERVED-REPLICATED | Connelly et al. (2012), *Science* 338:651–655 | Independent Pb-Pb outside uncertainty |
| `t_zircon` | 4404 ± 8 | Ma | Jack Hills detrital zircon; δ¹⁸O 7.4→5.0‰ | OBSERVED-REPLICATED | Wilde, Valley, Peck & Graham (2001), *Nature* 409:175–178 | An older confirmed terrestrial grain; or refute the δ¹⁸O inference |
| `f_bio,2008` | ~2/3 of 4,300 | species | **SUPERSEDED — DO NOT CITE** | **SUPERSEDED (withdrawn)** | Hazen et al. (2008), *Am Mineral* 93:1693–1720 | Superseded by the authors themselves — see next row |
| `f_bio,excl` | **~34** | % of 5,659 | form **exclusively** via biological processes | **MODELED** — single-team assignment of species to the authors' own 57 *proposed* paragenetic modes; **no independent replication** | Hazen & Morrison (2022), *Am Mineral* 107:1262–1287, doi:10.2138/am-2022-8099 | **Standing falsifier: nobody has independently re-audited the paragenetic-mode assignments.** Do so |
| `n_bio,infl` | **at least** 2,707 of 5,659 (**47.8%**) | species | form under biological **influence** (not exclusively) — the authors' explicit **"at least"**: a **lower bound**, not a point estimate | **MODELED** (as above; unreplicated) | Hazen & Morrison (2022) | As above |
| `n_bio,excl` | **>1,900** | species | exclusively biological — a planetary biomarker; already stated as a bound | **MODELED** (as above; unreplicated) | Hazen & Morrison (2022) | As above |
| `n_water` | **at least** 4,583 (**81.0%**) | species | water–rock interaction — the authors' explicit **"at least"**. **Largest single factor, ahead of life — but this ranks two lower bounds; it is not a measured margin** | **MODELED** (as above; unreplicated) | Hazen & Morrison (2022) | As above |
| `n_weather` | 1,998 | species | near-surface weathering/oxidation — commonest paragenetic mode | **MODELED** (as above; unreplicated) | Hazen & Morrison (2022) | As above |
| `n_modes` | 57 (3,349 species = 59.2% from **one** mode only) | paragenetic modes | across 5,659 species; **"our proposed"** scheme, the authors adding "we welcome additions and corrections" | **MODELED** — the classification scheme itself; unreplicated | Hazen & Morrison (2022) | As above |
| stage counts | ~12 → ~250 → ~1,500 | species | ur-minerals → meteorite/lunar → pre-biological | **MODELED** *(author's institutional summary; **primary not read** — the 2008 PDF returned HTTP 404 this pass. A number whose primary has not been read cannot be classed observed-and-replicated; and these are stage estimates from the same team whose 2008 headline was later withdrawn)* | Hazen et al. (2008) as summarised at hazen.carnegiescience.edu | Read *Am Mineral* 93:1693–1720 directly and confirm |
| `K_qtz`, `G_qtz`, `ρ_qtz` | — | GPa, g/cm³ | single-crystal adiabatic bulk/shear moduli, quartz & olivine | **NOT-MEASURED** (not sourced this pass) | — | Fetch Bass (1995), *AGU Ref. Shelf* 2:45–63 |
| `d_borehole` | **12,262** | m | Kola SG-3 — deepest direct sample of the Earth by **true vertical depth** (longer directional wells exist by *measured length*); ~0.19% of the way to the centre | OBSERVED-REPLICATED | Popov, Pevzner, Pimenov & Romushkevich (1999), *Tectonophysics* 306(3–4):345–366, doi:10.1016/S0040-1951(99)00065-7: "The Kola superdeep well SG-3 reaches a depth of 12,262 m" | A deeper true-vertical borehole; or a re-survey of SG-3 outside 12,262 m |

## Falsifier (operable)

This chapter's central structural claim — **that silicate mineralogy is generated by one hierarchical build rule (corner-sharing polymerisation of SiO₄ tetrahedra), and that Bowen's independently-established temperature order of crystallisation is that same polymerisation order** — is refuted by exhibiting **either**:

1. a common rock-forming silicate whose structure cannot be assigned a bridging-oxygen count in {0, 1, 2, 2.5, 3, 4} and whose Si:O ratio therefore falls outside the series; **or**
2. a fractionating basaltic melt in which the discontinuous branch crystallises out of polymerisation order — e.g. a sheet silicate appearing before a single-chain pyroxene under Bowen's stated conditions.

Neither the cyclosilicates (2 bridging O, ring topology rather than chain — a *dimensionality* variant at fixed linkage, already in the table) nor the quasicrystals (not silicates, not periodic — they refute the *230's scope*, not the polymerisation rule) is that counterexample.

Secondary falsifiers are row-local: any number in the table found outside its stated scope under its stated conditions moves **that row and only that row**. A refuted row does not refute the chapter; a refuted polymerisation rule moves the chapter.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **NEGATIVE / WITHDRAWN — "two-thirds of Earth's minerals require life / an oxygenated biosphere."** The originating authors superseded it. Hazen & Morrison (2022) report ~34% forming *exclusively* through biology, explicitly against the two-thirds estimate of Hazen et al. (2008). **Receipt of failure:** a 5,659-species paragenetic audit versus a 2008 stage-model estimate; the claim's own authors reversed it. This chapter's brief asserted the two-thirds figure and instructed that it be checked. It was checked. It is wrong. Recorded here rather than repeated.
- **NEGATIVE / conflation trap — "biology is the main driver of Earth's mineral diversity."** It is the **second**. Water is first: **at least** 4,583 species (81.0%) via water–rock interaction versus **at least** 2,707 (47.8%) under biological influence (Hazen & Morrison 2022). Both are the authors' explicit **lower bounds**, so this ranks two floors — the margin between them is not a measured quantity — and it rests on one unreplicated single-team survey. Recorded because the corrected fact is still routinely overstated in the direction of the retracted one, and because **the correction itself has not been independently checked either.**
- **NEGATIVE / scale-abuse — arithmetic on Mohs numbers.** Averaging, differencing, or taking ratios of Mohs hardness is invalid: the scale is ordinal, and scratch resistance composes hardness, toughness and modulus into one integer (Broz et al. 2006). **Receipt (single-crystal, uncontaminated):** kyanite (001), at Mohs 5–5.5, is **harder** by DSI indentation (14.8 GPa) than orthoclase at Mohs 6 (9.1) and periclase at Mohs 6–6.5 (9.4) — a rank inversion; and kyanite carries Mohs 5–5.5 and 7 on different faces of the same crystal (Whitney et al. 2007). **Receipt explicitly NOT used:** the periclase-vs-orthoclase *microhardness* inversion (5.3 vs 6.9 GPa). Periclase is a polycrystalline synthetic reference material, and the DSI column of the same table shows no inversion for that pair. Recorded as a **rejected receipt** so that nobody re-imports it.
- **INADMISSIBLE as stated — "crystals hold/emit healing or scalar energy," "crystal grids," quartz as a consciousness amplifier.** No mechanism is specified and no observation is named that could refute the claim; as stated it is unfalsifiable. Recorded, not mocked. The *earned* neighbours are close by and are worth more than the claim: quartz **piezoelectricity** is real, measured, and runs the clock in the device you are reading this on; the P–T surface really does let a mineral report the conditions of its own growth. The distance between those and a "crystal grid" is the entire method. These may be recorded as HONEST/cultural signals — real aesthetic and personal meaning, honestly held — never as TRUE/measured ones. Separate stores, never merged.
- **INADMISSIBLE as physics — "the golden ratio governs crystal form."** Unfalsifiable as stated. The genuinely interesting five-fold story is the opposite of mystical and is in the table: five-fold symmetry is *forbidden* in all 230 periodic space groups, quasicrystals achieve it *by not being periodic*, and one occurs naturally (icosahedrite). Real, strange, sourced, and it needs no help.
- **RECORDED FAILURE OF THE FIELD — the quasicrystal rejection.** A replicated observation (Shechtman et al. 1984) was dismissed for years because it violated a completeness theorem whose *scope condition* ("periodic") had stopped being restated. Pauling's line — *"There is no such thing as quasicrystals. Just quasiscientists."* — is preserved here not to sneer at Pauling but because **the failure mode is the lesson**: a proof is complete only within its axioms, and an axiom nobody says out loud becomes a prejudice. Recorded as the reference case for scope-forgetting.
- **NOT-SOURCED in this pass:** single-crystal bulk/shear moduli and densities for quartz and olivine (falsifier/closure: fetch Bass 1995, *AGU Ref. Shelf* 2:45–63); the primary text of Hazen et al. (2008) — the author's hosted PDF returned HTTP 404, so the ten-stage counts (~12 / ~250 / ~1,500) rest on the author's institutional summary and are flagged in the table; the Si–O bond-length primary; the coverage factor on the ⁴⁰K half-life. **Closed since:** the Kola borehole depth — now sourced to Popov et al. (1999) at 12,262 m, and no longer a plausible sourceless numeral.

## HONEST FENCE — MODELED

This chapter is fenced **MODELED**. Its rows carry their own classes (many OBSERVED-REPLICATED, one OBSERVED-CONTESTED, a block of MODELED — including every Hazen & Morrison row, the 230-space-group theorem, and PREM — two NEGATIVE/superseded, one NOT-MEASURED), but the *chapter as an artifact* composes measured constants through stated assumptions to reach structural conclusions. **The assumptions are the fence**, and three deserve naming:

1. **The Si:O and bridging-oxygen columns are stoichiometric idealisations.** Real silicates substitute Al for Si tetrahedrally, which is precisely why the feldspars are tectosilicates without being SiO₂. The series is a build rule, not a formula generator.
2. **PREM is a posterior, not the Earth** — *except where it is an assumption.* Every interior number above is model output conditioned on a specific dataset and a specific parameterisation, at a 1 s reference period, transversely isotropic in the outer 220 km. It is a *belief about* the interior. **Vs = 0 in the outer core is the exception, and must not be listed as output:** PREM imposes μ = 0 there by parameterisation, so that zero is an input the model was handed, not a result it earned. The shadow-zone observation (Oldham 1906; Jeffreys 1926) is robust; the third decimal place is not; and the outer-core zero is neither — it is an axiom.
3. **Bowen's series is one starting composition under fractionation**, not a law of igneous rocks.

Per **Gould & Lewontin (1979), "The Spandrels of San Marco and the Panglossian Paradigm"**: none of the above establishes that any mineral structure is an optimum. Minerals are not adapted to anything — this is the one chapter where that is trivially so, and it is worth saying because it makes the counterweight concrete rather than ritual. **Nature's authority here is precisely and only this: the Earth has already run a 4.5-Gyr parallel search over a closed structural alphabet under real physical constraints, and the phases that could not persist are gone.** That makes an observed structure evidence of a constraint-optimum *given* its P–T–X conditions, and makes every number above a **hypothesis generator**. It does not make any of them a warrant. Per repo rule **M7**, any design taken from this chapter must still beat a **tuned conventional baseline** on a **pre-registered metric** with a load-bearing discriminator, or it is recorded **NEGATIVE**.

## Not claimed

- **Not claimed:** that a rock senses, models, remembers, or infers anything. A zircon *stores* information with extraordinary fidelity and *never reads it*. Storage is not inference; a trace is not a belief; the posterior is in the geochronologist.
- **Not claimed:** that minimising Gibbs free energy is minimising variational free energy. They share a name and nothing else that matters. Crystallisation is thermodynamic relaxation with no generative model, no `q(s)`, no preferences `C`, and no policies. **This is the chapter's central fence and the reason the rock is the reference case.**
- **Not claimed:** that the 230 space groups exhaust ordered matter. They exhaust **periodic** order in 3-D. Quasicrystals are ordered and aperiodic, and nature made one. The scope condition is part of the result.
- **Not claimed:** that Bowen's series is universal, or that the polymerisation correspondence is causal. The *ordering* is an observed fact about two independently established series; the mechanism is MODELED.
- **Not claimed:** any interpretation of the inner core's computed ν ≈ 0.44. The number falls out of PREM; what it means about inner-core rheology is a live question this chapter does not enter.
- **Not claimed:** that the IMA species count is a fact about the Earth. It is the state of a committee's ledger under an explicitly non-retroactive, curated definition, and it moves — see row `r_IMA`: **~78–105 species per year** across the four most recent master lists (mean ~91/yr over 2024-09 → 2026-01), and the rate is **not** steady.
- **Not claimed:** the two-thirds mineral-evolution figure, in any form. It is recorded above as withdrawn. What *is* claimed, with receipts, is the weaker and still-startling statement: **at least** ~47.8% of mineral species form under biological influence, >1,900 exclusively so, and water — not life — is the largest single factor at **at least** 81.0%. All three are the authors' **lower bounds**, from one unreplicated single-team survey, and are fenced **MODELED** — not OBSERVED-REPLICATED.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** Reading Dziewonski & Anderson (1981) does not make any UNI claim proven, designed, or built. The NATURA vocabulary (OBSERVED-REPLICATED / OBSERVED-CONTESTED / MODELED / HYPOTHESIZED / INADMISSIBLE / NOT-MEASURED) and the UNI ledger vocabulary (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. This chapter contains **zero** UNI claims.
- **QUAESTIO-APERTA:** "full human" and "beyond human" appear nowhere here as target, milestone, or deliverable. They are permanent open questions. The mineral substrate has no bearing on them, and the rock's place at L0 is a floor for the ladder, not a step toward its top.
