# Build the substrate — rocks, water, air, stars

> **Knowledge file `K12-RECIPES-substrate-rocks-water-air-stars.md`** of the UNI Encyclopedia & Cookbook GPT pack.
> This file is a BUILD ARTIFACT: it merges **4** source file(s) from the
> repository `TMDLRG/UNI-Encyclopedia-Cookbook`, byte-for-byte, in the order listed below.
> The repository is the single source of truth; if this file and the repository ever
> disagree, the repository wins and this file is stale.
>
> SOVEREIGNTY RULE (binding, do not merge the two ledgers): this corpus carries TWO sovereign evidence vocabularies. The UNI 4-value fence (proven / designed / hypothesized / not-yet-built) describes ONLY UNI's own build status and is governed by encyclopedia/CLAIM-LEDGER.md. The NATURA 12-value class, in three groups, describes ONLY nature's observed regularities and is governed by encyclopedia/NATURE-LEDGER.md: group A / measured = OBSERVED-REPLICATED, OBSERVED-SINGLE, OBSERVED-CONTESTED; group B / derived = MODELED, MODELED-CONTESTED, HYPOTHESIZED; group C / fenced = INADMISSIBLE, SUPERSEDED, NOT-MEASURED, NOT-SOURCED, NOT-CONFIRMED, NOT-LOCATED. Six of the twelve were registered by NA-00 amendment 2026-07-15-A after the corpus refuted the original 'six classes and only six' at 72 of 919 ledger rows; twelve is a MEASURED property of the corpus, not a design target. NEVER read NOT-SOURCED as NOT-MEASURED: the first says we could not trace the source (a fact about us), the second says nobody has measured it (a claim about the frontier of science). A nature citation is NEVER a UNI gate. Cross-reference between them by explicit link only, never by merge.


**Source files merged into this knowledge file, in order:**

- `cookbook/recipes-natura/CN-01-rocks.md`
- `cookbook/recipes-natura/CN-02-water.md`
- `cookbook/recipes-natura/CN-03-air.md`
- `cookbook/recipes-natura/CN-04-stars.md`

---



<!-- ===== BEGIN cookbook/recipes-natura/CN-01-rocks.md ===== -->

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


<!-- ===== END cookbook/recipes-natura/CN-01-rocks.md ===== -->



<!-- ===== BEGIN cookbook/recipes-natura/CN-02-water.md ===== -->

# CN-02 — Water: the anomalous solvent everything else assumes

> **What you are reading.** The spec sheet of the medium every other NATURA chapter silently assumes. Water is not a neutral background; it is a pile of anomalies, and life is built **on** them, not despite them. Every number below carries a source you can check or is written NOT-MEASURED. Nothing here raises any UNI rung — a citation to chemistry is never a UNI gate. Water also attracts more unearned mysticism than any other substance on Earth while being, measurably, stranger than the mysticism. **That contrast is the chapter.**

---

## The anomaly that runs the temperate world

Liquid water is densest at **3.983 °C**, not at its freezing point. The numbers (Wikipedia, *Properties of water*, compiling standard reference data):

| T | ρ (g/mL) |
|---|---|
| 0 °C | 0.99984283(84) |
| **3.983 °C** | **0.99997495(84)** |
| 25 °C | 0.99704702(83) |

Read the size of it. The 0 → 3.983 °C anomaly is a density swing of **1.32 × 10⁻⁴ — 132 parts per million.** That is the whole effect. It is nearly nothing, and it structures every temperate lake on the planet.

The mechanism is two competing terms. **(a)** Warming increases anharmonic vibration → expansion, as in any liquid. **(b)** Warming bends and breaks the open tetrahedral hydrogen-bond network → molecules pack *closer* → contraction. Ice Ih is an open cage: each oxygen holds four neighbours at arm's length, and the cage encloses empty space. Below 3.983 °C, term (b) wins and water *contracts on heating* (negative thermal expansion). Above it, term (a) wins and water behaves normally.

Now the causal chain, which is worth walking one link at a time:

1. A lake's surface cools in autumn. Cooled water densifies and **sinks**. Convective overturn mixes the whole column.
2. Overturn continues until the entire column reaches ~4 °C.
3. Cool the surface further and it becomes **less** dense. It stops sinking. Overturn **halts**. The heat-loss engine that had access to the whole lake now has access only to a thin surface film.
4. That film freezes. Ice Ih at 0 °C is **0.9167 g/mL** against liquid **0.99984 g/mL** — the solid is **8.32 % less dense** and floats. (Equivalently: water **expands 9.07 %** on freezing. Those are two different quantities from the same pair of numbers; "9 %" is the expansion, not the density deficit. Do not swap them.)
5. The lid, plus snow on it, arrests convection and wind mixing. The bottom sits at ~4 °C. Fish overwinter.

**Get step 5 right, because the popular version is wrong.** Ice does not insulate by being a good insulator: at 0 °C — the temperature that actually matters for a freezing lake — ice conducts heat at ~2.2 W/(m·K) against liquid water's ~0.561, roughly **four times better**. (Quote both at the same temperature or the ratio drifts: liquid water rises to ~0.607 at 25 °C, which would make it ~3.6×.) The insulation comes from *snow* (as low as ~0.074 W/(m·K)) and, above all, from **killing convection**. A conductive lid over still water is a far worse heat exporter than a convecting column. The floating is what buys the still column.

**The counterfactual is MODELED, not observed:** if ice sank, lakes would freeze bottom-up, the ice would be shielded from summer insolation, and shallow water bodies would ratchet toward frozen-solid. No one has run that experiment. It is a physical inference, and it is labelled as one.

**And the teleology is refused here.** Water was not tuned for lakes. The anomaly is a consequence of tetrahedral hydrogen bonding, which is a consequence of two lone pairs and two protons at 104.48°. Life occupied the niche the anomaly created. Per **Gould & Lewontin (1979)**, "it works out well for us" is the exact shape of the error this book exists to catch.

## The thermal ballast — and three corrections

Water's isobaric specific heat is **4.181 J/(g·K) at 25 °C**. The comparison is what makes it worth saying (all from the same compilation, at 25 °C unless noted):

| Liquid | cₚ (J/g·K) | cₚ (J/mol·K), computed here |
|---|---|---|
| **Water** | **4.181** | **75.3** |
| Ammonia (liq)† | **4.700** | 80.0 |
| Ethanol | 2.440 | **112.4** |
| Methanol | 2.140 | 68.6 |
| Mercury | 0.1395 | 28.0 |
| Iron (solid) | 0.449 | — |
| Granite | 0.790 | — |

† **Liquid ammonia at 25 °C is not at 1 atm.** Its normal boiling point is **−33.34 °C**, so a *liquid* at 25 °C exists only under its saturation pressure of **~10 bar** (1003 kPa). The cited compilation prints "4.700" with **no temperature and no pressure**; the condition is supplied here. See correction 1.

Three corrections that popular accounts routinely skip:

**1. Water does not have the highest specific heat of any liquid.** Liquid ammonia beats it (4.70 vs 4.18 J/(g·K)) — a like-for-like comparison of two liquids at 25 °C, but note the pressure is ~10 bar, not 1 atm (see †). *(Whether ammonia exceeds water across its **entire** liquid range — which would make this claim independent of the 25 °C point — is **NOT-VERIFIED in this pass**: sources surfaced here give cₚ ≈ 4.5 at −23 °C and ≈ 4.75 at 27 °C, both above water's 4.18, but no table spanning the full range down to the −77.7 °C melting point was read. Closure: fetch NIST Webbook cₚ along the NH₃ saturation line.)* The claim "water has the highest heat capacity of all liquids" is false at 25 °C and is recorded NEGATIVE below.

**2. Per mole, ethanol beats water.** 112.4 vs 75.3 J/(mol·K), computed from the table. Water's per-gram advantage is *partly just low molar mass* — 18.015 g/mol. A bigger molecule has more vibrational modes to park energy in. Quoting the per-gram figure as though it revealed something about the H-bond network, without saying that molar mass is doing half the work, is overclaiming.

**3. What is actually remarkable is the conjunction.** Per unit **volume** — which is what an ocean or a body has — water stores 4.181 × 0.99705 = **4.17 J/(cm³·K)**. Dry air at 20 °C, 1 atm (ρ = 101325 / (287.05 × 293.15) = **1.204 kg/m³**, cₚ ≈ 1.012 J/(g·K)) stores **1.22 × 10⁻³ J/(cm³·K)**. Ratio: **~3,400×**. Water is high per gram **and** high per cm³ **and** liquid across a 100 K span at 1 atm **and** the most abundant liquid on the planet. No single one of those is unique. The conjunction is why the ocean, not the atmosphere, is Earth's thermal flywheel.

## The evaporative escape

Enthalpy of vaporisation: **40.65 kJ/mol = 2257 kJ/kg at 100 °C**. Ethanol at its boiling point is **38.56 kJ/mol** — *nearly the same per mole*, but **837 J/g** versus water's 2256 J/g. **Water wins 2.7× per gram almost entirely on molar mass.** Same lesson as the specific heat: the anomaly is real, but the per-gram framing inflates it.

This is what makes sweating work. At skin temperatures the **theoretical** value is **λ ≈ 2430 J/g** — which Havenith et al. (2013) measured λ_eff to *approach* when the evaporation happens at the skin itself. Shedding a resting ~100 W purely by evaporation costs 100 / 2430 = **0.041 g/s = 148 g/h**. Shedding ~1000 W of exercise heat costs **1.48 kg/h** — which lands inside the measured human sweat band of ~0.5–2.0 L/h, with elite athletes in heat exceeding 2.5 L/h. The arithmetic and the physiology agree; that agreement is the check. (Cross-ref **CN-11** for the thermoregulation loop.)

**The honest fence on sweating, which is the interesting part:** Havenith et al. measured that the *effective* latent heat at the body is **lower than the theoretical value**, and that how much lower depends on **where the evaporation happens** — the distance from the skin, not vapour resistance as such. λ_eff is close to 2430 J/g for evaporation from the skin, then drops **~11 %** for underwear plus a permeable coverall; **~28 %** when evaporation is from the underwear under a permeable outer; and **in excess of 62 %** when evaporation is from the outermost layer only with no base layer, **rising toward 80 %** as more layers are put between skin and wet outerwear. Evaporation at the outerwear cools the clothing, not you. Sweat that drips does not cool at all. The 2430 J/g is a ceiling, not a delivery — and at the far end of that series, most of the ceiling is gone.

## The skin

Surface tension at 25 °C is **71.97 mN/m** (IAPWS R1-76(2014), recomputed here from its own correlation σ = B τ^μ (1 + bτ), B = 235.8 mN/m, b = −0.625, μ = 1.256, τ = 1 − T/647.096 K → **71.972** — check it yourself; the widely-copied **71.99** is the Wikipedia compilation's figure, not what IAPWS's correlation returns, and the 0.02 mN/m spread moves nothing downstream). That is high for a room-temperature liquid, and it is the H-bond network again: a molecule at the surface has lost half its neighbours.

**The capillary length** — where gravity and surface tension trade places — is κ⁻¹ = √(γ/ρg) = √(0.07197 / 9777.7) = **2.71 mm**. Below that scale, water is ruled by its skin.

**Water striders** live entirely inside that regime. For a leg of radius ~50 µm, the Bond number is Bo = ρgL²/γ = 3.4 × 10⁻⁴ — surface tension beats gravity by ~3,000× (cross-ref **NA-07** for Bo and We). But the *interesting* result is that the naive story was wrong: Hu, Chan & Bush (2003), *Nature* 424:663–666, showed striders transfer momentum to the fluid **not** primarily via capillary waves but via **hemispherical vortices shed by the driving legs** — resolving the standing paradox about how infant striders propel themselves below the wave-speed threshold.

**Capillary ascent, and the correction that matters.** Jurin's law, h = 2γ cos θ / (ρgr), θ = 0:

| Pore radius | Rise | What it is |
|---|---|---|
| 10 µm | **1.47 m** | a xylem vessel lumen |
| 5 nm | **~2.9 km** | a cell-wall meniscus |

The tallest measured redwood is **112.7 m**, with a predicted ceiling of **122–130 m** (Koch et al. 2004, *Nature* 428:851–854). **Capillary rise in the conduit does not explain a tall tree — it is off by ~75×.** The nanometre-scale menisci in cell walls are over-specified by ~25×, and Koch et al. found the real ceiling is set by leaf water potential and its downstream cost to photosynthesis, not by the meniscus failing. This is the NA-08 discipline verbatim: **find the length scale that actually carries the flux before concluding the physics bent.**

## The solvent — and why dissolution is not "water pulls harder"

Water's gas-phase dipole moment is **1.8546 D**. In the liquid, polarisation by neighbours drives it to roughly **2.6–2.9 D** — the network makes each molecule ~50 % more polar than it is alone. (That liquid-phase value is model-dependent and carried as CONTESTED below; you cannot measure a molecular dipole in a liquid without a partitioning convention.)

The consequence is a static dielectric constant of **≈78.4 at 25 °C** — very high. Coulomb's law reads F = q₁q₂/(4πε₀ε_r r²), so **water cuts the force between two ions ~78-fold** relative to vacuum. That is the whole "universal solvent" story in one denominator.

But do not stop there, because the popular version is thermodynamically backwards. Dissolving NaCl in water is **endothermic**: ΔH_soln ≈ **+3.9 kJ/mol** (measured). Salt dissolving makes the water slightly *colder* — you can feel it. Water does not "pull the lattice apart" energetically; it barely breaks even. The lattice enthalpy (~+787 kJ/mol) and the summed ion hydration enthalpies (Na⁺ ≈ −406, Cl⁻ ≈ −363 kJ/mol) are two ~800 kJ/mol terms that **nearly cancel**, leaving a residual of a few kJ/mol that is at the edge of the bookkeeping's own precision — the Born–Haber sum lands near +18, the measurement says +3.9, and the ~14 kJ/mol gap is the error bar on the decomposition, not a discovery. **NaCl dissolves because of entropy**, not because of enthalpy.

Hold that thought for one more section, because it happens again.

## The network: astonishingly fast

The hydrogen-bond network is the cause of everything above. Its energy is **definitionally contested** and that is the honest headline. There is no standard definition of a hydrogen-bond energy in water, because the H-bond is not a separable term in the total cohesive energy. Two anchors:

- **Measured, whole-system:** the sublimation enthalpy of ice Ih at 0 °C is **51.059 kJ/mol**. Each molecule participates in four bonds, each shared by two molecules → two bonds per molecule → **≤ 25.5 kJ/mol per bond** as an upper bound. That bound silently absorbs dispersion and every other cohesive term.
- **Compiled estimate:** ~**23.3 kJ/mol** as an optimal H-bond enthalpy in liquid water.

Anyone quoting a single H-bond energy without naming the convention is overclaiming. The bound is real; the decomposition is not.

**The lifetime, though, is a clean measurement, and it is the most astonishing number here.** Fecko, Eaves, Loparo, Tokmakoff & Geissler (2003), *Science* 301(5640):1698–1702, tracked the OH-stretch frequency of HOD in liquid D₂O with femtosecond infrared spectroscopy:

- **170 femtoseconds** — the period of an underdamped oscillation of the hydrogen bond itself.
- **1.2 picoseconds** — the decay of vibrational correlations, from collective structural reorganisation.

Sit with the second one. The network that floats ice, ballasts oceans, folds every protein in you, and cools you by evaporating, **forgets its own configuration in about a picosecond.** It is not a structure. It is a standing pattern in something that rearranges a trillion times a second. This is the number to reach for when someone offers you "water memory": the measured memory of liquid water's H-bond network is ~10⁻¹² s.

## The hydrophobic effect — the most-botched explanation in popular science

It is **not** "oil hates water." There is no repulsion. Nonpolar solutes and water attract each other by dispersion forces like everything else. The segregation is driven by **what happens to the water**, and Chandler (2005), *Nature* 437(7059):640–647, is explicit that the effect is *multifaceted* — it depends on scale.

Get the two regimes right (Huang & Chandler 2000, *PNAS* 97(15):8324–8327; Lum, Chandler & Weeks 1999, *J Phys Chem B* 103:4570–4577). The crossover is at **~1 nm** — which is, not coincidentally, the characteristic length of protein structure:

**Small solutes (< ~1 nm) — ENTROPY-dominated.** The hydrogen-bond network is *not broken*. In Huang & Chandler's words, "hydrogen bonds simply go around the solute." The cost is entropic: the solute restricts the configuration space available to the surrounding water's hydrogen bonding. Water pays in disorder, not in bond energy. This is Tanford's classical picture (*The Hydrophobic Effect: Formation of Micelles and Biological Membranes*, Wiley-Interscience, 1973; 2nd edn. 1980).

**Large surfaces (> ~1 nm) — ENTHALPY-dominated.** Now the network *cannot* be maintained: "it is impossible to maintain a hydrogen bond network adjacent to an extended surface." Water density is **depleted** near the surface — it partially dries — and the free-energy cost becomes largely energetic, scaling with interfacial area.

So the correct short statement is: **the hydrophobic effect is entropy-driven at the length scale of a single small solute and enthalpy-driven at the length scale of an assembled interface — and the crossover sits right where proteins live.** That is why hydrophobic collapse drives protein folding (a chain assembling *through* the crossover) and why bilayers self-assemble and self-heal (cross-ref **NA-08**: a puncture exposes an extended hydrophobic edge, which is exactly the intolerable case). It also explains why the entropies of protein folding are so variable — the two regimes contribute with different temperature dependences.

Note the pattern: **NaCl dissolves for entropic reasons and oil segregates for entropic reasons.** In both cases the naive energetic story ("water pulls harder", "oil repels water") is wrong, and in both cases the solvent — not the solute — is where the thermodynamics lives.

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `T_ρmax` | **3.983** | °C | liquid H₂O, 1 atm | OBSERVED-REPLICATED | Wikipedia *Properties of water* (compiling standard reference data) | Densimetry finding max outside 3.9–4.1 °C at 1 atm |
| `ρ(3.983 °C)` | 0.99997495(84) | g/mL | as above | OBSERVED-REPLICATED | as above | Value outside stated uncertainty |
| `ρ(0 °C)` | 0.99984283(84) | g/mL | liquid, 1 atm | OBSERVED-REPLICATED | as above | as above |
| `ρ(25 °C)` | 0.99704702(83) | g/mL | liquid, 1 atm | OBSERVED-REPLICATED | as above | as above |
| `Δρ/ρ (0→3.983 °C)` | **1.32 × 10⁻⁴** (132 ppm) | dimensionless | the density anomaly's magnitude | MODELED | Computed here from the two rows above | Arithmetic error |
| `ρ_ice` | 0.9167 | g/mL | ice Ih, 0 °C | OBSERVED-REPLICATED | Wikipedia *Properties of water* | Structural/densimetric measurement outside ±0.001 |
| ice density deficit | **8.32** | % | (1 − 0.9167/0.99984) | MODELED | Computed here | Arithmetic error |
| freezing expansion | **9.07** | % vol | (0.99984/0.9167 − 1) — **not the same as the row above** | MODELED | Computed here | Arithmetic error |
| `k_ice` | ~2.2 (~2.2–2.3; **rises as T falls**) | W/(m·K) | ice Ih, **0 °C, 1 atm** — **higher than liquid water** | OBSERVED-REPLICATED *(secondary compilation)* | Wikipedia *List of thermal conductivities* (CRC-sourced row, ~273 K); **closure: fetch a primary** | Measurement at 0 °C, 1 atm outside ~2.1–2.4 |
| `k_water` | **~0.561** | W/(m·K) | liquid water, **0 °C, 1 atm** — cf. **~0.607 at 25 °C**; the 0 °C value is the one used in the lake argument, and the two must not be mixed | OBSERVED-REPLICATED *(secondary)* | as above (compilations print 0.6065 with **no temperature stated**; the T is supplied here) | Measurement at 0 °C, 1 atm outside ~0.55–0.57 |
| `k_snow` | ~0.074 (range ~0.05–0.25) | W/(m·K) | seasonal snow, density-dependent | OBSERVED-REPLICATED | *J Glaciology*, "The thermal conductivity of seasonal snow" | Measurement outside range at stated density |
| `cₚ` | **4.181** (4.184 at 20 °C) | J/(g·K) | liquid water, 25 °C | OBSERVED-REPLICATED | Wikipedia *Table of specific heat capacities* (secondary compilation; cites Ashby et al., Young & Geller) | Calorimetry outside ±1 % |
| `cₚ` ammonia | **4.700** — **exceeds water** | J/(g·K) | liquid NH₃, **25 °C, saturation pressure ~10 bar** (1003 kPa; liquid at 25 °C only under pressure — normal bp **−33.34 °C**) | OBSERVED-REPLICATED *(secondary; **T and P are not stated in the cited compilation** — condition supplied here from NH₃ vapour-pressure data. Whether ammonia leads water across the **whole** liquid range is **NOT-VERIFIED**; closure: fetch NIST Webbook cₚ(T,P) along the saturation line)* | as above | Calorimetry **at stated T and P** showing ammonia < water |
| `cₚ` ethanol / methanol / mercury | 2.440 / 2.140 / 0.1395 | J/(g·K) | 25 °C | OBSERVED-REPLICATED *(secondary)* | as above | as above |
| molar cₚ: water / ethanol | **75.3 / 112.4 — ethanol wins** | J/(mol·K) | 25 °C | MODELED | Computed here (cₚ × M; M = 18.015 / 46.07) | Arithmetic error |
| volumetric cₚ, water | **4.17** | J/(cm³·K) | 25 °C | MODELED | Computed here (4.181 × 0.99705) | Arithmetic error |
| `ρ_air` | **1.204** | kg/m³ | dry air, 20 °C, 101325 Pa | MODELED | Computed here: P/(R_sp·T), R_sp = 287.05 J/(kg·K) | Ideal-gas assumption refuted at these conditions |
| water : air, cₚ per volume | **~3,400×** | dimensionless | 20–25 °C, 1 atm | MODELED | Computed here | Arithmetic or input error |
| `ΔH_vap` | **2257** (40.65 kJ/mol) | kJ/kg | 100 °C, normal boiling point | OBSERVED-REPLICATED | Wikipedia *Properties of water*; corroborated by steam-table sources in this pass | Calorimetry outside ±1 % |
| `ΔH_vap` ethanol | **38.56 kJ/mol = 837 J/g** — near-equal per **mole** | kJ/mol | ethanol, normal bp | OBSERVED-REPLICATED *(tertiary compilation; primary not fetched)* | surfaced in this pass; **falsifier/closure: fetch CRC or NIST** | Primary value outside ±2 % |
| `λ_sweat` | **~2430** | J/g | the **theoretical** value at skin temperature — **not** a measured physiological constant; Havenith measured λ_eff to *approach* it for evaporation **from the skin** | OBSERVED-REPLICATED (as the value λ_eff approaches at the skin) | Havenith et al. 2013, *J Appl Physiol* 114(6):778–785, doi 10.1152/japplphysiol.01271.2012 | A measured λ_eff for skin evaporation outside 2400–2450 |
| `λ_eff` reduction | up to **~80** — site-dependent: **11 / 28 / >62 / →80** | % below theoretical λ | by **evaporation distance from skin**: underwear + permeable coverall **11**; evaporation from the underwear under a permeable outer **28**; from the outermost layer only, no base layer **>62**, rising toward **80** with more layers between skin and wet outerwear | OBSERVED-REPLICATED | Havenith et al. 2013 (thermal manikin) | A manikin study finding λ_eff reduction outside 11–80 % across these evaporation sites |
| sweat to shed 100 W / 1000 W | **148 g/h / 1.48 kg/h** | — | pure evaporative, λ = 2430 J/g | MODELED | Computed here | Arithmetic error |
| human sweat rate | ~0.5–2.0 (elite in heat >2.5) | L/h | exercising humans | OBSERVED-REPLICATED *(secondary summaries; primary not fetched)* | Sawka et al. 2007, ACSM Position Stand, *Med Sci Sports Exerc*; **closure: fetch the primary** | A measured band outside ~0.5–2.0 L/h |
| `γ` | **71.97** | mN/m | water–vapour, 25 °C | OBSERVED-REPLICATED | IAPWS R1-76(2014), **recomputed here from its own correlation → 71.972**. The widely-copied **71.99** is Wikipedia *Properties of water* — a **different source**, not what IAPWS returns; the 0.02 mN/m spread is inside this row's own falsifier and moves no downstream value | Tensiometry outside IAPWS's ±0.5 % below 100 °C |
| `κ⁻¹` | **2.71** | mm | capillary length, √(γ/ρg), 25 °C | MODELED | Computed here from `γ`, `ρ(25 °C)`, g = 9.80665 | Arithmetic error |
| `Bo` (strider leg) | **3.4 × 10⁻⁴** | dimensionless | ρgL²/γ, L = 50 µm | MODELED | Computed here — **leg radius is an order-of-magnitude assumption, not sourced** | Source a real leg radius; recompute |
| strider propulsion | momentum via **hemispherical vortices**, not primarily capillary waves | — | *Gerridae*, adults and infants | OBSERVED-REPLICATED | Hu, Chan & Bush 2003, *Nature* 424(6949):663–666 | Flow visualisation showing wave-dominated momentum transfer |
| Jurin rise, r = 10 µm / 5 nm | **1.47 m / ~2.9 km** | m | h = 2γcosθ/(ρgr), θ = 0, 25 °C | MODELED | Computed here | Arithmetic error |
| `h_tree,max` | **112.7 measured; 122–130 predicted** | m | *Sequoia sempervirens*; ceiling set by **leaf water potential**, not the meniscus | OBSERVED-REPLICATED (measured) / MODELED (ceiling) | Koch et al. 2004, *Nature* 428:851–854 | A taller undamaged tree; or a mechanism refuting the water-potential limit |
| `μ_gas` | **1.8546** | D | H₂O, gas phase, equilibrium | OBSERVED-REPLICATED *(secondary compilation; primary not fetched)* | Wikipedia *Properties of water* — which states **no uncertainty**; **closure: fetch Clough et al. 1973, *J Chem Phys* 59:2254, or the NIST/CRC dipole-moment table** | Primary measurement outside 1.8546 ± 0.001 D |
| `μ_liquid` | ~2.6–2.9 (ice Ih ~3.09 ± 0.04) | D | **convention-dependent** — no partitioning-free measurement exists | **OBSERVED-CONTESTED / MODELED** | reports surfaced in this pass span 2.6–2.9 ± 0.6 | A partitioning-independent determination |
| `ε_r` | **≈78.4** | dimensionless | static dielectric constant, pure water, 25 °C | OBSERVED-REPLICATED | BNID 115815; formulation: IAPWS R8-97 (Fernández et al., doi 10.1063/1.555997) | Value outside ±0.5 at 25 °C |
| Coulomb attenuation | **~78×** | dimensionless | F ∝ 1/ε_r | MODELED | Computed here from `ε_r` | Continuum-dielectric assumption refuted at ionic contact |
| `ΔH_soln(NaCl)` | **+3.9 — endothermic** | kJ/mol | NaCl in excess water | OBSERVED-REPLICATED *(secondary/tertiary; primary not fetched)* | surfaced in this pass; **closure: fetch CRC/NIST** | Calorimetry showing exothermic dissolution |
| NaCl Born–Haber terms | lattice ~+787; ΔH_hyd Na⁺ ~−406, Cl⁻ ~−363 → sum ≈ **+18 vs +3.9 measured** | kJ/mol | **the ~14 kJ/mol gap is the decomposition's error bar** | MODELED | as above | A decomposition closing to the measured value |
| `ΔH_sub(ice Ih)` | **51.059** | kJ/mol | ice Ih, 0 °C | OBSERVED-REPLICATED *(tertiary compilation)* | LSBU *Water Structure and Science* (Chaplin); primary titled "Sublimation pressure and sublimation enthalpy of H₂O ice Ih between 0 and 273.16 K", *Geochim Cosmochim Acta* — **not fetched in this pass** | Fetch the primary; value outside ±0.1 |
| H-bond energy | **≤25.5 (bound); ~23.3 (estimate)** | kJ/mol | **no standard definition exists** | **OBSERVED-CONTESTED** | bound computed here (51.059/2); estimate: Chaplin, "Water's Hydrogen Bond Strength", arXiv:0706.1355 | An agreed operational definition separating the H-bond from dispersion |
| `τ_HB,osc` | **170** | fs | underdamped H-bond oscillation period; OH of HOD in D₂O | OBSERVED-REPLICATED | Fecko et al. 2003, *Science* 301(5640):1698–1702, doi 10.1126/science.1087251 | Femtosecond IR outside 150–200 fs |
| `τ_HB,decay` | **1.2** | ps | decay of vibrational correlations (collective reorganisation) | OBSERVED-REPLICATED | Fecko et al. 2003 | Femtosecond IR outside ~1–1.5 ps |
| `L_crossover` | **~1** | nm | hydrophobic small→large regime crossover | MODELED (theory + simulation) | Huang & Chandler 2000, *PNAS* 97(15):8324–8327; Lum, Chandler & Weeks 1999, *J Phys Chem B* 103:4570–4577 | A measurement placing the crossover an order of magnitude away |
| hydrophobic driver, < 1 nm | **entropic** — network intact, "hydrogen bonds simply go around the solute" | — | small solutes | MODELED | Huang & Chandler 2000 | Solvation entropy measured near zero for small apolar solutes |
| hydrophobic driver, > 1 nm | **enthalpic** — network depleted, surface partially dries | — | extended apolar surfaces | MODELED | Huang & Chandler 2000; Lum et al. 1999 | Measurement showing no density depletion at an extended apolar surface |
| `θ_HOH` | 104.48 | degrees | H–O–H bond angle | OBSERVED-REPLICATED | Wikipedia *Properties of water* | Structural measurement outside ±0.1° |
| `ε_r`-of-a-drink claims | — | — | any bulk property of ingested "structured water" | **NOT-MEASURED** | not sourced in this pass — no such measurement located | Produce one |

## Falsifier (operable)

This chapter's central structural claim — **that water's biologically load-bearing behaviour is a consequence of the tetrahedral hydrogen-bond network, and that in each case the correct thermodynamic account is about the *water*, not about the solute** — is refuted by exhibiting **one of the following**:

1. A liquid with water's tetrahedral H-bond network **lacking** the density maximum, ice-floats-on-water inversion, and high volumetric cₚ together (i.e. the network is not sufficient); **or**
2. A liquid with **none** of the network exhibiting all three (i.e. the network is not necessary); **or**
3. A demonstration that the hydrophobic effect at < 1 nm is **enthalpy**-dominated under the conditions Huang & Chandler specify — which would move the whole assembly account and, with it, the NA-08 membrane rationale.

Secondary falsifiers are row-local: any number in the table found outside its stated scope under its stated conditions moves **that row and only that row**. A refuted row does not refute the chapter. A refuted crossover, or a refuted network-causality, moves the chapter.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

The receipt is the lesson here, not the verdict. Read what each test *did*.

- **"Water memory" (Benveniste).** — **INADMISSIBLE as stated.** Davenas et al. (1988), *Nature* 333:816–818, reported human basophil degranulation triggered by anti-IgE antiserum diluted past the point where any antibody molecule could remain, concluding the *configuration of water* was biologically active. **The receipt:** *Nature* sent Maddox, Randi & Stewart, who re-ran the assay in the same lab with the same people — and published "'High-dilution' experiments a delusion", *Nature* 334:287–290. The single load-bearing change was **blinding**: sample codes were sealed and taped to the ceiling, to be revealed only after degranulation was scored. Under sealed codes the effect vanished. An independent group later published "Human basophil degranulation is **not** triggered by very dilute antiserum against human IgE" (Hirst, Hayes, Burridge, Pearce & Foreman 1993, *Nature* 366(6455):525–527) — and the honest detail is **theirs**, not the *Nature* team's: their results contained a source of variation they could not account for, but **no aspect of the data was consistent with the previously published claims.** (The *Nature* team's own caveat was different in kind: they called the experiments statistically ill-controlled, with no effort made to exclude systematic error including observer bias.) **The lesson is not "they were frauds." The lesson is that an effect which exists unblinded and dies under sealed codes was located in the observer, and that the people who found this out did so by running the experiment rather than by arguing.** Note also the physical anchor above: liquid water's H-bond network loses its own configuration in **~1.2 ps** (Fecko et al. 2003).

- **Emoto's crystal / intention claims.** — **INADMISSIBLE as a claim about water.** Here the honest handling is subtler than "it failed", because **one controlled test exists and reported a positive result**: Radin, Hayssen, Emoto & Kizu (2006), *Explore (NY)* 2(5):408–411, doi 10.1016/j.explore.2006.06.004, had ~2,000 people in Tokyo direct intention at water in a shielded room in California; crystal images were rated by 100 independent judges, and treated-water crystals scored higher for **aesthetic appeal** (P = .001, one-tailed). **The receipt is what that measured.** The dependent variable was a **subjective aesthetic rating of selected photographs**, not any physical property of water or ice — no density, no spectrum, no diffraction, no nucleation temperature. Emoto's protocol has photographers select the most pleasing crystals; ice crystal habit is exquisitely sensitive to supercooling, nucleation, and trace contaminants, and Tiller's noted objection is that supercooling was **neither controlled nor measured**. Add: the claimant is a co-author, and no replication outside the proponent group has been located in this pass. **So the claim "intention changes water's structure" was never tested. A claim about aesthetic ratings of chosen images was.** That is a specific, checkable defect — not a slur.

- **"Structured / EZ water" as a health claim.** — **Split it, and the split is the whole point.** *(a) EARNED:* the **exclusion zone** — a layer near hydrophilic surfaces (notably Nafion) from which plastic microspheres are excluded — is **real and independently replicated by ~10 laboratories** (Elton, Spencer, Riches & Williams 2020, *Int J Mol Sci* 21(14):5041, doi 10.3390/ijms21145041). It is a genuine phenomenon in search of an explanation. *(b) CONTESTED:* Pollack's "fourth phase / structured water" **explanation** is disputed — the same review reports flaws in the supporting birefringence measurements and argues Schurr's diffusiophoresis account explains things Pollack's cannot (EZ growth time-course, pH gradients from the Nafion surface, the optical-tweezer force field). Several Pollack-lab findings (EZ growth under laser illumination, salt exclusion) await independent replication. *(c) INADMISSIBLE:* the **health claim** — that drinking "structured water" does anything. The EZ is a *bulk interfacial* effect at a synthetic hydrophilic polymer; no measurement of any bulk property of ingested structured water, nor of any clinical endpoint, was located in this pass (**NOT-MEASURED**). The phenomenon is real; the explanation is contested; the health claim is neither. **Collapsing those three into one verdict — in either direction — is the defect.**

- **NEGATIVE / false claim:** "water has the highest specific heat capacity of any liquid." **Liquid ammonia is 4.700 vs water's 4.181 J/(g·K)** — both liquids at 25 °C, ammonia under its ~10 bar saturation pressure (bp −33.34 °C), a condition the compilations omit and this chapter supplies. Recorded because the claim is near-universal in teaching material.

- **NEGATIVE / conflation trap:** quoting water's per-gram cₚ or ΔH_vap as evidence about the hydrogen-bond network without stating that **molar mass does much of the work**. Per mole, ethanol beats water on cₚ (112.4 vs 75.3 J/(mol·K)) and nearly ties it on ΔH_vap (38.56 vs 40.65 kJ/mol).

- **NEGATIVE / conflation trap:** "ice insulates the lake because ice is a good insulator." **Ice conducts ~4× better than liquid water** (~2.2 vs ~0.561 W/(m·K), **both at 0 °C** — quote the two at different temperatures and the ratio drifts). The insulation is snow plus the **arrest of convection**.

- **NEGATIVE / conflation trap:** "capillary action lifts water up a tree." Jurin's law in a 10 µm xylem lumen gives **1.47 m** against a measured 112.7 m tree — off by ~75×. The menisci that carry the tension are nanometre-scale cell-wall pores, and per Koch et al. 2004 the ceiling is set by leaf water potential, not by the meniscus.

- **NEGATIVE / the botched classic:** "oil and water repel." There is no repulsion. See the Chandler section.

- **NOT-MEASURED in this pass:** any bulk physical property, or any clinical endpoint, of ingested "structured water"; a primary (rather than compiled) source for the thermal conductivities of ice and liquid water; the water strider's leg radius and mass.

- **NOT-FETCHED in this pass (named, with closure):** CRC/NIST primaries for ethanol ΔH_vap and ΔH_soln(NaCl); the *Geochim Cosmochim Acta* ice-Ih sublimation paper; Sawka et al. 2007 ACSM Position Stand; the primary for the **gas-phase dipole moment** (Clough et al. 1973, *J Chem Phys* 59:2254, or the NIST/CRC dipole table — the value is carried on a secondary compilation that states no uncertainty); **NIST Webbook cₚ(T,P) along the NH₃ saturation line**, which would both confirm the ammonia point's stated conditions and settle whether ammonia leads water across the entire liquid range. Each is carried above with its class marked down accordingly.

## HONEST FENCE — MODELED

This chapter is fenced **MODELED**. Its individual rows carry their own classes (most OBSERVED-REPLICATED, several OBSERVED-CONTESTED, several NOT-MEASURED), but the *chapter as an artifact* composes measured constants through stated assumptions — ideal-gas air density, Jurin's law with θ = 0 and a perfectly wetting rigid cylinder, continuum dielectric response at ionic contact, a spherical/cylindrical leg for Bo, two-H-bonds-per-molecule bookkeeping for the sublimation bound — to reach design conclusions. **The assumptions are the fence.** The continuum-dielectric one is the weakest: ε_r = 78.4 is a *bulk* property, and the first hydration shell around an ion is not bulk water. The ~78× attenuation is a scaling argument, not a contact-distance calculation.

Per **Gould & Lewontin (1979), "The Spandrels of San Marco and the Panglossian Paradigm"**: none of the above establishes that water is *for* anything. Water is not fine-tuned for life; its anomalies fall out of tetrahedral hydrogen bonding, which falls out of two lone pairs and two protons, and biology is what colonised the resulting niche. **Nature's authority here is precisely and only this: it has already run a very long search under real physical constraints in which the failures were deleted.** That makes each number a *hypothesis generator*, never a proof. Per repo rule **M7**, any design taken from this chapter must still beat a **tuned conventional baseline** on a **pre-registered metric** with a load-bearing discriminator, or it is recorded **NEGATIVE**.

## Not claimed

- **Not claimed:** that water is fine-tuned, designed, purposive, special-because-it-suits-us, or evidence of anything beyond chemistry. The anthropic inversion is refused explicitly above.
- **Not claimed:** that water's anomalies are *unique*. Ammonia beats it on cₚ; ethanol beats it on molar cₚ and nearly ties it on molar ΔH_vap; and **silicon, gallium, germanium, antimony and bismuth also expand on freezing** — any substance with an open tetrahedral or otherwise low-coordination solid does (silicon expands ~10 %, more than water's 9.07 %). *(Class: OBSERVED-REPLICATED via secondary compilations surfaced in this pass — see Wikipedia, "Category:Materials that expand upon freezing"; primaries not fetched. Falsifier/closure: fetch density-vs-phase primaries for Si and Ga.)* Water is the only **common, ambient-temperature** substance that does it. What is remarkable is the **conjunction plus the abundance**, not any single record.
- **Not claimed:** that the H-bond energy has a single value. It does not have an agreed operational definition, and the chapter prints the bound rather than a number.
- **Not claimed:** that the liquid-phase dipole moment is measured. It is convention-dependent and carried CONTESTED.
- **Not claimed:** that the sunken-ice counterfactual is observed. It is a physical inference, labelled MODELED.
- **Not claimed:** that Radin et al. 2006 is fraudulent, incompetent, or unpublished. It is a real published study that measured **aesthetic ratings of selected photographs**. The finding is not disputed here; the **inference from it to a claim about water** is what fails, and the reason is printed.
- **Not claimed:** that the exclusion zone is fake. It is replicated by ~10 labs and is real. Only the *health* claim is inadmissible, and the contested *explanation* is carried as contested.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** Reading Fecko et al. 2003 does not make any UNI claim proven, designed, or built. The NATURA vocabulary (OBSERVED-REPLICATED / OBSERVED-CONTESTED / MODELED / HYPOTHESIZED / INADMISSIBLE / NOT-MEASURED) and the UNI ledger vocabulary (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. This chapter contains **zero** UNI claims.
- **QUAESTIO-APERTA:** "full human" and "beyond human" appear nowhere in this chapter as a target, milestone, or deliverable. They are permanent open questions, and the chemistry of the solvent has no bearing on them.


<!-- ===== END cookbook/recipes-natura/CN-02-water.md ===== -->



<!-- ===== BEGIN cookbook/recipes-natura/CN-03-air.md ===== -->

# CN-03 — Air: the atmosphere as a working fluid

> **What you are building.** A working specification for the gas your design sits in: what it is made of, how thick it is, how it carries momentum, sound and light, what it does as a heat engine, and where it refuses to hold you up. Air is not "background" — it is a fluid with a density, a viscosity, a sound speed and a scattering cross-section, and every one of those decides something. Every value below carries a source you can check or is written NOT-MEASURED. Nothing here raises any UNI rung — a citation to geophysics is never a UNI gate.

---

## The mixture, and the row that moves

Dry air by volume (NASA NSSDC Earth Fact Sheet, Colorado mirror): **N₂ 78.084%, O₂ 20.946%, Ar 9,340 ppm (0.934%)** — three gases are 99.96% of it — then Ne 18.18, He 5.24, CH₄ 1.7, Kr 1.14, H₂ 0.55 ppm.

Two facts about that table are load-bearing and usually skipped.

**It is a *dry-air* table.** Water vapour is variable — the same sheet says "typically makes up about 1%" — and it is a *diluent*: humid air is dry air pushed aside. "20.95% O₂" is a mole fraction of the dry component. At 1013.25 hPa that is an O₂ partial pressure of **212 hPa**, and *that*, not the percentage, is what a respiring organism sees. Hold it for the oxygen section.

**One row is not a constant, and the fact sheet is the receipt.** The copy fetched here lists **CO₂ at 350 ppm** — roughly 80 ppm stale. The measured Mauna Loa monthly mean for **June 2026 was 431.44 ppm** (NOAA Global Monitoring Laboratory, page updated 05 Jul 2026) against **429.61 ppm in June 2025**: a difference of **1.83 ppm**. The Met Office forecast the 2026 seasonal peak at **432.2 ± 0.6 ppm** in May — a forecast, therefore MODELED.

The discipline in miniature: a NASA composition table is a good source for the rows that do not move and a *wrong* source for the row that does. **An undated CO₂ figure is not a number.** The Mauna Loa record is why we can say so — one instrument class, one site, run continuously for decades. Its value is not that any single reading is precise, but that the *same* measurement repeated long enough made a 1.83 ppm/yr signal unmistakable against the seasonal sawtooth. That is what a long baseline buys, and it is the only reason the stale row is detectable as stale.

## The one derivation: how thick is the air?

Hydrostatic balance, `dP/dz = −ρg`, plus the ideal gas law `ρ = PM/(RT)`:

```
dP/P = −(Mg/RT) dz   →   P(z) = P₀·exp(−z/H),   H = RT/(Mg)
```

One length falls out of it. With `R` = 8.314 J/(mol·K), `T` = 288 K, `M` = 0.028964 kg/mol, `g` = 9.807 m/s²:

```
H = (8.314 × 288)/(0.028964 × 9.807) = 8,430 m ≈ 8.4 km
```

The NASA sheet lists **8.5 km**. The 1% gap is the isothermal assumption — the real troposphere cools with height — and that gap *is* the fence:

| Altitude | `exp(−z/H)` | Meaning |
|---|---|---|
| 5.84 km (= H·ln2) | 0.500 | **half the atmosphere's mass lies below this** |
| 8.849 km (Everest) | 0.350 | ~35% of sea-level pressure at the summit |
| 100 km (Kármán line) | 7 × 10⁻⁶ | the model has failed |

Everest is roughly right. Kármán is roughly *wrong* — real pressure near 100 km is orders below 7 ppm of sea level, because `T` and `M` both move enormously over 12 scale heights and the model assumed neither does. **The isothermal exponential is good for one or two scale heights, then it lies.**

Total atmospheric mass is just the weight the surface holds up:

```
M_atm = P₀A/g = (101,325 × 5.10×10¹⁴)/9.807 = 5.27 × 10¹⁸ kg
```

The accepted figure is ≈5.15 × 10¹⁸ kg. The 2% gap is not an error — it is **mountains**. Invert it: 5.15 × 10¹⁸ kg implies a mean *surface* pressure of ~990 hPa, not 1013, because the mean solid surface is not at sea level. A discrepancy you can explain is worth more than an agreement you cannot.

## The comparison that decides everything: air against water

At 20 °C, 1 atm:

| | air | water | ratio |
|---|---|---|---|
| density `ρ` | 1.204 kg/m³ *(computed `PM/RT`)* | 998.2 kg/m³ | water **829×** denser |
| dynamic viscosity `μ` | 1.81 × 10⁻⁵ Pa·s | 1.002 × 10⁻³ Pa·s | water **55×** more viscous |
| **kinematic viscosity `ν = μ/ρ`** | **1.50 × 10⁻⁵ m²/s** | **1.00 × 10⁻⁶ m²/s** | **air 15× more viscous** |

Read the third row twice, because it inverts the second. Water is 55× more viscous in the sense you probably mean by the word — resistance to shear. But it is 829× denser, and momentum diffusion is `μ` *per unit inertia*, which is `ν`. Divide 829 by 55: **15**. **Kinematically, air is the stickier fluid.**

`ν` is the only fluid property in `Re = vL/ν` (cross-ref **NA-07**), so **the same body at the same speed sits at a Reynolds number 15× lower in air than in water.** Air pushes you toward the viscous end of the ladder; water pushes you toward the inertial end.

| System | `v` | `L` | fluid | `Re` |
|---|---|---|---|---|
| insect wing | 3 m/s | 3 mm | air | ~6 × 10² |
| bat wing | 10 m/s | 0.1 m | air | ~7 × 10⁴ |
| whale fluke | 5 m/s | 3 m | water | ~1.5 × 10⁷ |

Four orders separate the insect from the bat; another two and a half separate the bat from the whale. **Flying and swimming are not one problem at two scales — they are different regimes.** An insect at `Re` ~10² lives where viscosity is a live term and steady aerofoil theory is a bad model; a whale at `Re` ~10⁷ lives in fully inertial, turbulent-boundary-layer flow. Designing one from the other's intuitions is the error this table exists to prevent.

## Sound

```
c = √(γRT/M) = √(1.400 × 8.314 × 293.15 / 0.028964) = 343.2 m/s at 20 °C
```

The same formula at 0 °C gives **331.3 m/s**. Note what is *absent*: pressure. `c` depends on `T` and `M` only — `ρ` and stiffness both scale with `P` and cancel. Sound is not slower on a mountain because the air is thin; it is slower because the air is cold. **`c ∝ √T`**. (In water, ~1,482 m/s at 20 °C — 4.3× faster, which is why an acoustic design ported from air to water breaks on wavelength first.)

**Attenuation is the real payoff.** Classical Stokes–Kirchhoff absorption (viscosity + thermal conduction) scales as **`α ∝ f²`**. If that were the whole story air would be simple. It is not: below ~10 kHz, absorption is dominated by **vibrational relaxation of N₂ and O₂**, catalysed by water molecules — so `α` depends on humidity, *non-monotonically*. Measured at 20 °C, 101.325 kPa (NPL *Kaye & Laby* tables, as reproduced by Frontier Labs — a tertiary reproduction, flagged):

| | 10% RH | 30% RH | 50% RH | 70% RH | 90% RH |
|---|---|---|---|---|---|
| 1 kHz | 14 | 5 | 4.7 | 5 | 5.3 |
| 2 kHz | 45 | 14 | 9.9 | 9 | 9.1 |
| 8 kHz | 180 | 170 | 110 | 78 | 63 |
| 10 kHz | 190 | **240** | 160 | 120 | 95 |

*(dB/km. The source prints all nine RH columns at 10% steps; only alternating columns are shown here — which means the 10 kHz **maximum is not displayed**: it falls in the omitted 20% RH column at **280 dB/km**, and the full published row runs 190 / 280 / 240 / 190 / 160 / 130 / 120 / 100 / 95. The published 5 kHz / 90% cell reads "8", anomalous against its row; not used here.)*

Two things. **Humidity dependence is non-monotonic** — at 10 kHz `α` *rises* 190 → 240 dB/km between 10% and 30% RH, peaking at **280** near **20% RH**, then falls monotonically to 95 at 90%. **And frequency dependence is not clean `f²` here**: 1 → 10 kHz is 10× in `f` but only **34×** in `α` at 50% RH, where `f²` demands 100×. Relaxation, not the classical term, runs this band.

Budget 100 dB of absorption at 20 °C / 50% RH: **1 kHz → 21 km; 10 kHz → 0.63 km.** A factor of 10 in pitch costs ~34× in range. That is why low frequencies travel far, and it sets up **CN-09/CN-10**. One caveat usually dropped: absorption sits *on top of* geometric spreading (−6 dB per distance doubling), which is **frequency-independent** — at low `f` and short range spreading dominates and absorption is a rounding error; at high `f` and long range absorption is the whole story. Quoting either alone is the error. *(Sub-1 kHz coefficients are **NOT-MEASURED** here — the infrasound case is extrapolation, not a fetched number.)*

## Light: why the sky is blue, and why it is not violet

Rayleigh's result: for scatterers much smaller than the wavelength, scattered intensity goes as **`1/λ⁴`** (Strutt [Rayleigh] 1871, *Phil. Mag.* 41:107–120, 274–279). Run it: blue (450 nm) against red (650 nm) → (650/450)⁴ = **4.4×**. Violet (400 nm) against red → **7.0×**.

So why is the sky not violet? Because `1/λ⁴` is one factor in a product. The solar spectrum has less power in the violet, and the human cone response is weakest there. **Sky colour is the scattering cross-section × the source spectrum × the observer** — and only the first is Rayleigh's. A design that reads `1/λ⁴` off the page and predicts violet has used a correct law to reach a wrong answer by dropping two terms. Note the law's own fence: it holds for scatterers ≪ λ. Cloud droplets are not — which is why clouds are white, and it is the same physics declining to apply.

## The heat engine, and a dimensionless payoff

Balance absorbed sunlight against blackbody emission, with `S` = 1361 W/m², albedo 0.30, `σ` = 5.670 × 10⁻⁸ W/(m²·K⁴):

```
T_e = [S(1−α)/(4σ)]^(1/4) = 254.6 K
```

The measured mean surface temperature is **288 K**. The **33 K** gap is the greenhouse effect — two constants and an albedo, in one line.

**And the same mirror is stale in two rows, not one.** The NASA fact sheet cited eight times in this chapter does not agree with the line above. It prints **Bond albedo 0.385**, **`S` = 1367.6 W/m²**, and — directly, for the exact quantity just derived — **"Black-body temperature (K): 247.3"**. On its own inputs `T_e` ≈ **246.8 K** (recomputed here; the sheet prints 247.3) and the greenhouse gap is **~41 K**, not 33. The values used here (α = 0.30, `S` = 1361) are the modern CERES/TSI-era figures and are, in this pass, **NOT primary-sourced**; the sheet's are believed superseded. Say the uncomfortable half out loud: this chapter made a virtue of catching that sheet's stale CO₂ row — the stale row that *supported* the argument — so the stale albedo row, which does *not*, gets the identical receipt or the method was never a method. **Catching only the stale row that flatters you is not discipline; it is preference wearing discipline's clothes.**

Treat the circulation as a heat engine: heat in near the tropical surface (~300 K), rejected to space at the radiating temperature (~255 K):

```
η ≤ 1 − 255/300 = 0.15  (15%)
```

That is a **ceiling, not a performance figure**. The actual fraction of absorbed solar power appearing as kinetic energy of the general circulation is far below it and is **NOT-MEASURED in this pass** — I will not print a number I did not fetch.

The engine's geometry: air rises at the equator, moves poleward aloft, and descends near **~30°** — the **Hadley cell**, which is why the world's deserts are banded there. Why 30° and not the pole? Rotation.

```
f = 2Ω sin φ,   Ω = 7.2921 × 10⁻⁵ rad/s   →   f(45°) = 1.031 × 10⁻⁴ s⁻¹
```

and the **Rossby number `Ro = U/(fL)`** says whether rotation matters at all:

| Flow | `U` | `L` | `Ro` | Verdict |
|---|---|---|---|---|
| midlatitude weather system | 10 m/s | 1,000 km | **0.097** | rotation **dominates** → geostrophic balance |
| tornado | 50 m/s | 100 m | **~4.8 × 10³** | rotation **irrelevant** to its dynamics |
| draining sink | 0.01 m/s | 0.3 m | **~3 × 10²** | rotation **irrelevant** |

`Ro` ≈ 0.1 is the whole reason weather maps work: at that value the pressure-gradient and Coriolis forces nearly balance, so wind blows *along* isobars rather than across them. Inside the Hadley cells the vorticity-based *local* Rossby number is order **1** — a different definition and a different regime, where rotation and advection are comparable rather than one dominating. The sink row is the famous one, and it earns a receipt rather than a sneer — see the INADMISSIBLE section.

## Oxygen has a history

The 20.946% row is a recent condition, not a property of the planet. For roughly the first half of Earth's existence there was effectively no free O₂; the **Great Oxidation Event** ended that. The dating rests on the disappearance of mass-independent fractionation of sulphur isotopes (S-MIF), which requires an ozone-free, O₂-poor atmosphere to be produced and preserved.

The date is **contested, and the contest is the interesting part.** Luo et al. (2016), *Sci. Adv.* 2:e1600134, place it at **2.33 Ga** from the last S-MIF occurrence in South Africa — later than the ~2.4–2.45 Ga often quoted. Then "Globally asynchronous sulphur isotope signals require re-definition of the Great Oxidation Event", *Nat. Commun.* (2018), argues the signal is not globally synchronous at all, which makes "*the* date" the wrong question; *Nat. Commun.* (2023), "Reconciling discrepant minor sulfur isotope records…", attempts to close it. **Carry the dispute; do not average it.**

Berner's **GEOCARBSULF** gives a broad late-Palaeozoic O₂ peak of **about 30%** in the Permian (Berner 2006, *Geochim. Cosmochim. Acta* 70(23):5653–5664; revised in Berner 2009, *Am. J. Sci.* 309(7):603–606, reporting higher Mesozoic/Cenozoic values and no drop below 15%). **This is a model output, not a measurement** — a mass balance over isotopic and weathering parameters. Label it MODELED every time.

### The giant-insect hypothesis — and why it is now CONTESTED

The story is famous: ~30% O₂ in the Carboniferous and Permian; insects breathe by *diffusion* down blind-ended tracheae rather than a pumped circulation; diffusion worsens with distance (the `L²` argument of **NA-08**); so hyperoxia relaxed the ceiling and insects got huge. And they did — ***Meganeuropsis permiana***, an Early Permian griffinfly, reached a wingspan of about **71 cm**.

Clean diffusion argument. It may be wrong.

**For:** Harrison, Kaiser & VandenBrooks (2010), *Proc. R. Soc. B* 277(1690):1937–1946, doi:10.1098/rspb.2010.0001, review the case that tracheal O₂ limitation constrains maximum insect size and late-Palaeozoic hyperoxia permitted gigantism — supported by beetles' disproportionate rise in tracheal investment with size, exactly the compensation the hypothesis predicts.

**Against:** Snelling et al. (2026), *Nature*, doi:10.1038/s41586-026-10291-3 (online 25 March 2026), argue at the delivery endpoint rather than the trunk. Tracheoles occupy **~1% or less** of flight-muscle volume in most species — capillaries take ~**10×** that in bird and mammal cardiac muscle — and relative tracheolar space scales up only **~1.8-fold across a 10,000-fold body-mass range**, holding when extended to *M. permiana*. Snelling, quoted in *phys.org*, 25 March 2026 — **press coverage, not the paper text**: *"There is some compensation occurring in larger insects, but it is trivial in the grand scheme of things."* (The chapter previously printed this quote cut at "trivial." with no ellipsis; a quotation mark must bound what was actually said.) If O₂ delivery were binding, the giants should compensate at the tracheoles. They do not. Alternatives proposed: vertebrate predation; exoskeletal biomechanics.

**Class it OBSERVED-CONTESTED.** The 2026 result attacks *one mechanism* with a morphometric scaling measurement; it does not show O₂ was irrelevant to Palaeozoic insect size, nor refute the GEOCARBSULF curve. Honest position, July 2026: **the correlation is real, the classical mechanism is under serious and recent attack, the replacement is not settled.** The mirror-image overrun is fenced below.

## Flight: why air holds a bat but not a whale

Lift is `L = ½ρv²S·C_L`; in level flight `L = W = mg`, so **wing loading** `W/S = ½ρv²C_L` and `v ∝ √(W/S)`. Scale isometrically — mass `∝ ℓ³`, wing area `∝ ℓ²`:

```
W/S ∝ ℓ ∝ m^(1/3)   →   v ∝ m^(1/6)
```

Bigger flyers must fly faster. That is geometry. The kill is power. Induced power goes as `P ∝ W²/(ρvb²)`; substituting `v ∝ m^(1/6)` and `b² ∝ m^(2/3)`:

```
P_req ∝ m² / (m^(1/6) · m^(2/3)) = m^(7/6)
```

This is **Pennycuick's 7/6 law**. Power *required* climbs as `m^(7/6)`; power *available* from muscle climbs more slowly — muscle mass scales as `m`, but maximum wingbeat frequency falls with size, so the product lags, going as **`m^(2/3)`**. Two curves with different exponents — **7/6 against 2/3** — cross exactly once, and the crossing is a **maximum flying mass**: **~12 kg** for aerobically powered *continuous* flapping flight (Pennycuick — **NOT-SOURCED** here, via secondary reports rather than the primary, which is why it is quoted and not derived).

**The census does not simply agree, and the honest version is more useful than the tidy one.** The heaviest large male great and kori bustards *average* ~16 kg — that is a **mean, not a maximum** — and verified individuals run **over 20 kg**, with great bustard accounts to ~21 kg. Those birds sit **above** the stated ceiling. So the claim is not "theory and census agree": the ceiling and the census are the **same order**, and the exceedance is concentrated in taxa whose flight is **burst, not continuous** — bustards are famously reluctant flyers. That scope condition, *continuous aerobic flapping*, is the term doing the real work. Whether a 21 kg bustard sustains it is a live question this chapter does not close — and it is this chapter's own ledger falsifier ("an extant bird sustaining aerobic flapping flight well above 16 kg") pointed back at its own row. Printing "theory and census agree" required stretching the ceiling up to 16 and pulling the census down to 16 until they touched. Neither move was sourced.

Run the whale. `m` = 1.5 × 10⁵ kg (order-of-magnitude), `W` = 1.47 × 10⁶ N; be *generous*: `C_L` = 1.0, `v` = 30 m/s.

```
S = 2W/(ρv²C_L) = 2(1.47×10⁶)/(1.204 × 900 × 1.0) ≈ 2,715 m²
```

At aspect ratio 8 that is a **147 m** wingspan, and the power to flap it exists in no tissue. The whale is **~10⁴×** past the ceiling. Try the static route — buoyancy:

```
V_air   = 1.5×10⁵/1.204 ≈ 1.2 × 10⁵ m³   (a sphere ~62 m across)
V_water = 1.5×10⁵/1026  ≈ 146 m³         (≈ its own body)
```

**There is the answer, and it is just `ρ`.** To hold the whale up statically, air demands 1.2 × 10⁵ m³ of displacement; seawater demands ~146 m³ — the whale's own volume, for free. The ratio is **852** — the *seawater*/air density ratio, the same quantity as the 829 in the table above and differing only because seawater is denser than the fresh water there. (1026/1.204 = 852; the table's 829 is 998.2/1.204. Mixing the two would be a free 3%.) Water holds a whale by *existing*. Air has to be *worked*, and the work scales as `m^(7/6)` while the muscle does not. A bat at ~10⁻² kg is four orders under the ceiling and flies without argument.

**The largest flyers, honestly.** *Pelagornis sandersi* (Ksepka 2014, *PNAS*, doi:10.1073/pnas.1320297111): wingspan **6.06–7.38 m** depending on feather-reconstruction method, mass ~**22–40 kg**, modelled as an efficient long-range marine soarer. It exceeds the ~12 kg *flapping* ceiling because soaring is a different power budget — energy from the air, not the muscle — so the ceiling does not bind it. Not a refutation of Pennycuick: a ceiling applying only where its assumptions hold. *Quetzalcoatlus northropi* is harder, and **the spread is the finding**: **~70 kg** (Chatterjee & Templin 2004), **~200–250 kg** (the consensus cluster — Paul 2002; Witton 2008; Witton & Habib 2010; Martin & Palmer 2014), **~544 kg** (Henderson 2010) at a 10–11 m wingspan — a **~8× disagreement** from the same fossils, with the high-end analysis concluding it could not sustain powered flight at all. Quoting one figure as *the* mass of the largest flying animal reports a preference, not a measurement.

## The blanket: air as an external state with slow dynamics

Per **M12**, the atmosphere sits in WORLD, outside the body's Markov blanket, and its defining property for a designer is **timescale separation**. It is a slowly-varying external state, sensed through a thin interface (a lung, a spiracle, a stoma) and perturbed negligibly by any individual. `H` = 8.4 km, `M_atm` = 5.3 × 10¹⁸ kg, a CO₂ signal moving 1.83 ppm in a *year*: on the timescale of any control loop an organism runs, air is a boundary condition. It becomes an internal variable only when you aggregate over the whole biosphere and geological time — which is where the next claim lives, and where it gets into trouble.

### Gaia — HYPOTHESIZED, and the objection is not a quibble

Lovelock & Margulis (1974), *Tellus* 26(1–2):2–10, observed something real: Earth's atmosphere is wildly out of thermodynamic equilibrium (O₂ and CH₄ coexisting is the standard exhibit), it has stayed habitable across a large rise in solar luminosity, and life is not a passenger — it is a principal flux. **The observation is sound.** The inference — that the biosphere *regulates* the planet, homeostatically, "by and for" itself — is the contested part.

**The serious objection is about the unit of selection, and it is structural.** Doolittle (1981), "Is Nature Really Motherly?", *CoEvolution Quarterly*, and Dawkins (1982), *The Extended Phenotype*, put it the same way from different directions: natural selection acts on differentially reproducing entities. There is **one** Earth — no population of competing siblings, no reproduction, no inheritance with variation. So planetary homeostasis could not have been *selected for*: any organism whose local trait improved regulation at a cost to its own fitness loses to the neighbour that skipped it. **Gaia as usually stated requires a selective process for which no unit exists.** That is not hostility to the idea; it is naming the missing mechanism.

**Daisyworld answers a narrower question, and must be read as exactly that.** Watson & Lovelock (1983), *Tellus B* 35(4):284–289, doi:10.1111/j.1600-0889.1983.tb00031.x, built a world of black and white daisies, each growing only for its own local fitness with no regulatory intent, and showed planetary temperature nonetheless stabilises across a range of solar luminosity. **It is an existence proof that a mechanism is possible** — global homeostasis emerging from purely local selfish fitness, without teleology — which defuses the "Gaia requires foresight" objection. **It is not evidence that Earth uses that mechanism**, and it does not answer Doolittle and Dawkins in general: it builds a world where the coupling happens to be tight and sign-correct, which is an assumption about Daisyworld, not a finding about Earth.

**Class: HYPOTHESIZED** — and the three parts (OBSERVED-REPLICATED disequilibrium, HYPOTHESIZED regulation, MODELED Daisyworld) travel separately or the fence has failed.

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `f_N2` | 78.084 | % by volume | dry air, sea level | OBSERVED-REPLICATED | NASA NSSDC Earth Fact Sheet (Colorado mirror) | Independent composition measurement outside ±0.01% |
| `f_O2` | 20.946 | % by volume | **dry** air, sea level | OBSERVED-REPLICATED | as above | As above |
| `f_Ar` | 9,340 (0.934%) | ppm by volume | dry air | OBSERVED-REPLICATED | as above | As above |
| `P_O2` | 212 | hPa | O₂ partial pressure at 1013.25 hPa | MODELED | Computed here: 0.20946 × 1013.25 | Arithmetic |
| `f_H2O` | ~1 (highly variable) | % by volume | near-surface, typical | OBSERVED-REPLICATED | as above ("Water is highly variable") | — |
| `[CO₂]` | **431.44** | ppm | **Mauna Loa monthly mean, June 2026** | OBSERVED-REPLICATED | NOAA GML *Trends in CO₂*, updated 05 Jul 2026 | Re-read the record; a different published monthly mean for June 2026 |
| `[CO₂]` prior yr | 429.61 | ppm | Mauna Loa monthly mean, June 2025 | OBSERVED-REPLICATED | NOAA GML, as above | As above |
| `Δ[CO₂]/yr` | 1.83 | ppm/yr | June 2025 → June 2026, single-site | OBSERVED-REPLICATED | NOAA GML, as above | As above |
| `[CO₂]` 2026 peak | 432.2 ± 0.6 | ppm | **forecast** monthly mean, May 2026 | **MODELED** | Met Office annual CO₂ forecast | Compare against the realised May 2026 observation |
| `[CO₂]` NASA row | 350 | ppm | **STALE** — as printed on the fact sheet | **INADMISSIBLE as current** | NASA NSSDC Earth Fact Sheet (mirror) | Already refuted by the NOAA row above |
| `H` | **8.43** | km | `RT/(Mg)`; T=288 K, M=0.028964 kg/mol, g=9.807 | MODELED | Computed here | Arithmetic; or refute an input |
| `H` (published) | 8.5 | km | Earth scale height as listed | OBSERVED-REPLICATED | NASA NSSDC Earth Fact Sheet (mirror) | Independent value outside 8–9 km |
| `z(½ mass)` | 5.84 | km | `H·ln2`, isothermal | MODELED | Computed here | Arithmetic; isothermal assumption |
| `P/P₀` (Everest) | 0.350 | — | z = 8.849 km, isothermal `H` = 8.43 km | MODELED | Computed here | Compare to measured summit barometry |
| `P/P₀` (100 km) | 7 × 10⁻⁶ | — | **model out of range** — see fence | **MODELED (failing)** | Computed here | Any real 100 km pressure measurement — it refutes this row, by design |
| `M_atm` | 5.27 × 10¹⁸ *(vs ≈5.15 × 10¹⁸ accepted)* | kg | `P₀A/g`; gap = mean surface elevation | MODELED | Computed here; accepted value not primary-sourced in this pass | Fetch a primary `M_atm`; check the 990 hPa reconciliation |
| `ρ_air` | 1.204 | kg/m³ | 20 °C, 101.325 kPa; `PM/RT` | MODELED | Computed here | Arithmetic |
| `ρ_air` (surface) | 1.217 | kg/m³ | 288 K, 1014 mb | OBSERVED-REPLICATED | NASA NSSDC Earth Fact Sheet (mirror) | Independent measurement >2% off |
| `μ_air` | 1.81 × 10⁻⁵ | Pa·s | 20 °C, 1 atm | OBSERVED-REPLICATED *(not primary-sourced in this pass)* | standard reference; cross-checks against Sutherland's formula → 1.813 × 10⁻⁵ | Fetch NIST/CRC; a value outside 1.79–1.84 × 10⁻⁵ refutes |
| `μ_water` | 1.002 × 10⁻³ | Pa·s | 20 °C, 1 atm | OBSERVED-REPLICATED *(not primary-sourced in this pass)* | standard reference (IAPWS-class value) | Fetch IAPWS; outside 0.99–1.01 × 10⁻³ refutes |
| `ρ_water` | 998.2 | kg/m³ | 20 °C | OBSERVED-REPLICATED *(not primary-sourced in this pass)* | standard reference | Fetch a primary table |
| **`ν_air`** | **1.50 × 10⁻⁵** | m²/s | 20 °C, 1 atm; `μ/ρ` | MODELED | Computed here from the two rows above: 1.81 × 10⁻⁵ / 1.204 = 1.503 × 10⁻⁵. *(The often-quoted 1.51 × 10⁻⁵ corresponds to the Sutherland `μ` = 1.813 × 10⁻⁵, not to the `μ` row used here; this chapter divides the row it prints.)* | Either input refuted |
| **`ν_water`** | **1.00 × 10⁻⁶** | m²/s | 20 °C; `μ/ρ` | MODELED | Computed here; cross-checks vs. published 1.0038 mm²/s at 20.2 °C | Either input refuted |
| **`ν_air/ν_water`** | **15.0** | dimensionless | 20 °C | MODELED | Computed here | Arithmetic |
| `ρ_water/ρ_air` | 829 | dimensionless | 20 °C | MODELED | Computed here | Arithmetic |
| `μ_water/μ_air` | 55 | dimensionless | 20 °C — **note the inversion vs `ν`** | MODELED | Computed here (829/55 = 15 ✓) | Arithmetic |
| `Re` insect | ~6 × 10² | dimensionless | 3 mm, 3 m/s, air | MODELED | Computed here; inputs order-of-magnitude | Inputs refuted |
| `Re` bat | ~7 × 10⁴ | dimensionless | 0.1 m chord, 10 m/s, air | MODELED | Computed here; inputs order-of-magnitude | Inputs refuted |
| `Re` whale | ~1.5 × 10⁷ | dimensionless | 3 m chord, 5 m/s, water | MODELED | Computed here; inputs order-of-magnitude | Inputs refuted |
| `c_air` | **343.2** | m/s | 20 °C; `√(γRT/M)`, γ=1.400 | MODELED | Computed here | Measured `c` outside 342–344 m/s at 20 °C |
| `c_air` (0 °C) | 331.3 | m/s | 0 °C, same formula | MODELED | Computed here | As above |
| `c ∝ √T` | exponent ½ | — | ideal gas; **independent of pressure** | MODELED | Computed here from `√(γRT/M)` | Demonstrate a pressure dependence of `c` at fixed T |
| `c_water` | ~1,482 | m/s | 20 °C | OBSERVED-REPLICATED *(not primary-sourced in this pass)* | standard reference | Fetch a primary value |
| `α ∝ f²` | exponent 2 | — | **classical (Stokes–Kirchhoff) term only** | MODELED | classical acoustics | Not the observed exponent below 10 kHz — see next rows |
| `α` (measured) | 1 kHz: 4.7 / 10 kHz: 160 | dB/km | 20 °C, 101.325 kPa, 50% RH | OBSERVED-REPLICATED *(tertiary reproduction)* | NPL *Kaye & Laby* tables, as reproduced by Frontier Labs | Fetch NPL/ISO 9613-1 directly; a value >20% off refutes |
| `α(10k)/α(1k)` | **34** *(pure `f²` predicts 100)* | dimensionless | 20 °C, 50% RH | MODELED | Computed here from the row above | Arithmetic; or the source table refuted |
| `α` humidity shape | **non-monotonic**: peak **280** at **20% RH**; 190 → 240 → 95 dB/km at 10 → 30 → 90% RH | dB/km | 10 kHz, 20 °C | OBSERVED-REPLICATED *(tertiary reproduction)* | as above | A primary table showing monotonic humidity dependence at 10 kHz |
| `α` below 1 kHz | — | dB/km | infrasound / low audio band | **NOT-MEASURED** | not fetched in this pass | Fetch ISO 9613-1 tables for 50–1000 Hz |
| range @ 100 dB | 21 km (1 kHz) vs 0.63 km (10 kHz) | km | 20 °C, 50% RH, absorption only | MODELED | Computed here | Either input refuted |
| Rayleigh | `∝ 1/λ⁴` | — | scatterers ≪ λ | OBSERVED-REPLICATED | Strutt [Rayleigh] 1871, *Phil. Mag.* 41:107–120, 274–279 | A small-particle scattering exponent ≠ 4 |
| blue/red | 4.4 | dimensionless | (650/450)⁴ | MODELED | Computed here | Arithmetic |
| violet/red | 7.0 | dimensionless | (650/400)⁴ — **yet the sky is blue** | MODELED | Computed here | Arithmetic |
| `T_e` | **254.6** | K | `[S(1−α)/4σ]^¼`; S=1361 W/m², α=0.30 | MODELED | Computed here; S and albedo **not primary-sourced in this pass — and the NASA sheet cited elsewhere in this chapter disagrees** (next row) | Fetch CERES/TSI primaries; the cited fact sheet's own 0.385 / 1367.6 / 247.3 K disagree with this row and are believed superseded |
| Bond albedo + `T_e` (NASA sheet) | **0.385** → `T_e` **247.3** (printed); **246.8** recomputed here from its own S and α | — / K | **as printed on the fact sheet**, with its `S` = 1367.6 W/m² | **INADMISSIBLE as current** | NASA NSSDC Earth Fact Sheet (Colorado mirror) — same sheet, same defect as its 350 ppm CO₂ row | Superseded by modern CERES-era planetary albedo ≈0.29–0.31 and TSI ≈1361 W/m²; refute *those* and this row returns and the greenhouse gap becomes ~41 K |
| `T_s` | 288 | K | mean surface temperature | OBSERVED-REPLICATED | NASA NSSDC Earth Fact Sheet (mirror) | Independent value >2 K off |
| greenhouse ΔT | **33.4** | K | `T_s − T_e` | MODELED | Computed here | Either input refuted |
| `η_Carnot` | ≤ 0.15 (15%) | dimensionless | `1 − 255/300`; a **ceiling**, not a performance | MODELED | Computed here | Arithmetic; or refute the reservoir temperatures |
| KE generation | — | W/m² | fraction of solar input → circulation KE | **NOT-MEASURED** | not fetched in this pass | Fetch a primary energetics budget |
| `Ω` | 7.2921 × 10⁻⁵ | rad/s | Earth sidereal rotation | OBSERVED-REPLICATED *(not primary-sourced in this pass)* | standard geodetic constant | Fetch IERS conventions |
| `f(45°)` | 1.031 × 10⁻⁴ | s⁻¹ | `2Ω sin φ` | MODELED | Computed here | Arithmetic |
| `Ro` synoptic | **0.097** | dimensionless | U=10 m/s, L=1,000 km, φ=45° | MODELED | Computed here | Inputs refuted |
| `Ro` tornado | ~4.8 × 10³ | dimensionless | U=50 m/s, L=100 m | MODELED | Computed here | Inputs refuted |
| `Ro` sink | ~3 × 10² | dimensionless | U=0.01 m/s, L=0.3 m | MODELED | Computed here; U is a plausible residual, order-of-magnitude | Measure the residual circulation in a real sink |
| Hadley extent | ~30 | ° latitude | equator → subtropics, approximately axisymmetric | OBSERVED-REPLICATED | standard atmospheric dynamics | An observed circulation terminating far from 30° |
| Hadley local `Ro` | ~1 (0.3–0.6 at extremities) | dimensionless | vorticity-based `Ro_L = −ζ̄/f` — **different definition** | MODELED *(secondary; see NOT-SOURCED)* | axisymmetric Hadley literature (Hill & Bordoni; Schneider 1977), via a fetched summary | Fetch the primary; a value far from unity |
| GOE | **2.33** *(vs ~2.4–2.45 commonly quoted)* | Ga | last occurrence of S-MIF, South Africa | **OBSERVED-CONTESTED** | Luo et al. 2016, *Sci. Adv.* 2:e1600134 | See next row — asynchrony would void "a" date |
| GOE synchrony | **disputed** | — | S-isotope signals may be globally asynchronous | **OBSERVED-CONTESTED** | *Nat. Commun.* (2018) "Globally asynchronous sulphur isotope signals…"; *Nat. Commun.* (2023) "Reconciling discrepant minor sulfur isotope records…" | A globally synchronous S-MIF disappearance |
| `O₂` Permian peak | ~30 | % | Phanerozoic maximum, late Palaeozoic | **MODELED** | Berner 2006, *GCA* 70(23):5653–5664; rev. Berner 2009, *Am. J. Sci.* 309(7):603–606 | Recompute the mass balance; a proxy measurement contradicting |
| `O₂` at 300 Ma | ~45% above present | relative | as reported alongside Snelling et al. | MODELED | via phys.org report of Snelling et al. 2026 | Consistent with the ~30% row (30/20.95 = 1.43) |
| Wingspan *M. permiana* | ~71 | cm | Early Permian griffinfly; largest known insect | OBSERVED-REPLICATED | Guinness World Records (wing impressions, Elmo, Kansas, 1937); widely reported | A larger insect wing fossil |
| Tracheole vol. fraction | **≤1** | % of flight-muscle volume | most insect species | OBSERVED-REPLICATED | Snelling et al. 2026, *Nature*, doi:10.1038/s41586-026-10291-3 | Independent morphometry >2× off |
| Tracheole scaling | **1.8-fold** over a **10⁴-fold** mass range | — | incl. extension to *M. permiana* | OBSERVED-REPLICATED | Snelling et al. 2026 | Show strong compensation in giant taxa |
| Capillary comparison | ~10× the tracheole fraction | — | bird/mammal cardiac muscle | OBSERVED-REPLICATED | Snelling et al. 2026 | Independent morphometry |
| O₂-limitation hypothesis | **CONTESTED** | — | tracheal O₂ limits max insect size | **OBSERVED-CONTESTED** | **For:** Harrison, Kaiser & VandenBrooks 2010, *Proc. R. Soc. B* 277(1690):1937–1946, doi:10.1098/rspb.2010.0001. **Against:** Snelling et al. 2026, *Nature* | Rearing experiments across `aPO₂` resolving max size; do **not** average the two positions |
| `W/S ∝ m^(1/3)`; `v ∝ m^(1/6)` | exponents ⅓, ⅙ | — | isometric scaling of a flyer | MODELED | Computed here | Show non-isometric wing-area scaling that breaks it |
| `P_req ∝ m^(7/6)` | exponent 7/6 | — | induced power, isometric | MODELED | Computed here; = Pennycuick's 7/6 law | Arithmetic; or measured power scaling ≠ 7/6 |
| `P_avail ∝ m^(2/3)` | exponent 2/3 | — | muscle mass `∝ m`, wingbeat frequency falls with size | MODELED | Computed here; the second curve in the crossing | Measured power-available scaling ≠ 2/3 |
| max flapping mass **(theory)** | **~12** | kg | aerobically powered **continuous** flapping flight; `m^(7/6)` vs `m^(2/3)` crossing | MODELED *(**NOT-SOURCED** — via secondary reports, not the primary)* | Pennycuick's aerodynamic theory; secondary reports also give "largest extant flying species ≈12–14 kg" (Pennycuick 1989) | Fetch the primary; or a measured power-available exponent ≠ 2/3 |
| heaviest extant flyers **(census)** | large males **average ~16**; verified individuals **>20**, accounts to **~21** | kg | great bustard *(Otis tarda)* / kori bustard *(Ardeotis kori)* | OBSERVED-REPLICATED *(not primary-sourced in this pass)* | widely reported census figures — **the ~16 kg figure is a mean, not a maximum** | Fetch a primary mass series; a verified maximum outside 19–21 kg |
| ceiling vs census | **exceedance, not agreement** | — | heaviest bustards sit **above** the ~12 kg theoretical ceiling | **OBSERVED-CONTESTED** | this chapter; the two rows above, each in its own scope | Show a >16 kg bird **sustaining continuous aerobic flapping** → refutes the ceiling. Show bustard flight is burst-only → the ceiling's scope condition holds and the exceedance is not one |
| whale wing area | ~2,715 (span ~147 m at AR 8) | m² | m=1.5×10⁵ kg, v=30 m/s, C_L=1.0, ρ=1.204 | MODELED | Computed here; mass is order-of-magnitude | Arithmetic; inputs |
| whale `V_air` vs `V_water` | 1.2 × 10⁵ vs ~146 | m³ | buoyant displacement needed; ratio = **852** = `ρ_seawater/ρ_air` *(cf. 829 for fresh water at 20 °C — different fluid, different row)* | MODELED | Computed here: 1026/1.204 = 852 | Arithmetic |
| *Pelagornis* wingspan | **6.06–7.38** | m | depends on feather-reconstruction method | OBSERVED-REPLICATED | Ksepka 2014, *PNAS*, doi:10.1073/pnas.1320297111 | Re-measure; a span outside the range |
| *Pelagornis* mass | ~22–40 | kg | regression-dependent; **exceeds the flapping ceiling — it soared** | OBSERVED-REPLICATED | Ksepka 2014 | As above |
| *Quetzalcoatlus* mass | **70 / 200–250 / 544** — a **~8× spread** | kg | 10–11 m wingspan; same fossils, three answers | **OBSERVED-CONTESTED** | Chatterjee & Templin 2004 (~70); Paul 2002 / Witton 2008 / Witton & Habib 2010 / Martin & Palmer 2014 (~200–250, the consensus cluster); Henderson 2010 (~544) — via secondary reports, see NOT-SOURCED | A method reconciling the three; **do not quote one as "the" mass — and do not round the ends inward, which shrinks the finding** |
| Gaia (regulation) | — | — | biosphere homeostatically regulates the planet | **HYPOTHESIZED** | Lovelock & Margulis 1974, *Tellus* 26(1–2):2–10 | Specify a unit of selection, or a mechanism needing none, that survives Doolittle/Dawkins |
| Atmospheric disequilibrium | observed | — | e.g. O₂/CH₄ coexistence; belongs to no theory | OBSERVED-REPLICATED | Lovelock & Margulis 1974 and standard atmospheric chemistry | Show the atmosphere is at thermodynamic equilibrium |
| Daisyworld | **existence proof of a mechanism** — not evidence Earth uses it | — | model world; local selfish fitness → global T stability | **MODELED** | Watson & Lovelock 1983, *Tellus B* 35(4):284–289, doi:10.1111/j.1600-0889.1983.tb00031.x | Model reproduction failing to stabilise; **cannot** be falsified by anything about Earth — that is the point |
| Bathtub Coriolis (as told) | **INADMISSIBLE** | — | "your sink swirls by hemisphere" | **INADMISSIBLE** | refuted by `Ro` ~3 × 10² above | Measure sink vorticity sign vs. hemisphere without controlling residual circulation |
| Bathtub Coriolis (as done) | detected | — | 6-ft tank, 6 in deep, covered, **24 h settling** | OBSERVED-REPLICATED | Shapiro 1962, "Bath-Tub Vortex", *Nature* 196(4859):1080–1081; Southern-Hemisphere counterpart, *Nature* 207:1084 | Repeat with settling and fail to see the rotation |

## Falsifier (operable)

This chapter's central structural claim — **that the single number deciding whether a body flies or swims is the *kinematic* viscosity `ν`, not the density or the dynamic viscosity, and that air's `ν` being ~15× water's is why the two are different regimes rather than one problem at two scales** — is refuted by exhibiting **one pair of geometrically similar bodies operating at the same Reynolds number in air and in water whose flow regimes, force coefficients and control strategies differ systematically beyond measurement error.** If `Re` is matched and the physics still differs, `ν` was not the deciding variable and the chapter's spine is wrong. *(Compressibility is the known escape hatch — matched-`Re` comparison is valid only at Mach ≪ 1. A refutation must stay in that band or it refutes nothing.)*

Secondary falsifiers are row-local: any table entry found outside its stated scope under its stated conditions moves **that row and only that row**. A refuted `α` at 10 kHz does not touch the `ν` argument. A refuted `ν` moves the chapter.

The dated rows carry a standing falsifier by construction: **`[CO₂]` = 431.44 ppm is true of June 2026 and of nothing else.** Re-fetch NOAA GML before quoting it. The NASA fact sheet's 350 ppm row is what this row looks like when nobody does.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **"Water spirals down the drain one way in the north and the other in the south."** — **INADMISSIBLE as stated**, and the receipt is a dimensionless number, not a sneer. `Ro = U/(fL)` ≈ **3 × 10²** for a sink: rotation is ~300× too weak to compete with the residual circulation already in the basin from filling it, its geometry, or the plug being pulled. **But the underlying physics is real and was measured.** Shapiro (1962, *Nature* 196:1080–1081) built a covered 6-ft tank, filled it with a deliberate *clockwise* swirl, let it settle **24 hours** to kill `U`, and drained it: the float sat motionless for 12–15 minutes, then turned **counter**clockwise at ~1 rev per 3–4 s. A Southern-Hemisphere counterpart followed (*Nature* 207:1084). Read the method: **the 24-hour settle is not fussiness, it is the experiment.** Driving `U → 0` drives `Ro → 0`, the only regime where the effect can win. This is the exact shape of an earned/unearned split — the folk claim is false, the physics is true, and the difference is a controlled variable. Neither half may be quoted without the other.
- **"The sky is blue because of `1/λ⁴`, therefore it should be violet."** — **NEGATIVE / conflation trap.** The law is right and the conclusion is wrong, because observed colour is scattering cross-section **×** solar spectrum **×** cone response, and only the first is Rayleigh's. Recorded because it is the cleanest example here of a correct law producing a wrong answer through a dropped term.
- **"Absorption in air goes as `f²`."** — **NEGATIVE as a general statement.** True of the classical Stokes–Kirchhoff term; false of real air below ~10 kHz, where N₂/O₂ vibrational relaxation dominates. **Receipt:** 1 → 10 kHz at 20 °C/50% RH gives **34×**, not the 100× `f²` demands; and humidity dependence at 10 kHz is **non-monotonic** (190 → 240 → 95 dB/km at 10 → 30 → 90% RH, peaking at **280** near 20% RH), which no `f²` law can produce.
- **"CO₂ is 350 ppm" (or any undated CO₂ figure).** — **INADMISSIBLE.** Receipt printed above: a live NASA-derived fact sheet carries 350 ppm while the measured June 2026 value is 431.44 ppm. The defect is not the number; it is the missing date on a row that moves ~2 ppm/yr.
- **"Giant Carboniferous insects prove high O₂ allowed gigantism."** — **NOT admissible as settled**, in either direction. The correlation is real and the classical mechanism (Harrison et al. 2010) is a serious diffusion argument. It is now under direct attack at the delivery endpoint: Snelling et al. (2026, *Nature*) find tracheolar investment rises only **1.8-fold across a 10⁴-fold mass range** — trivial compensation where the hypothesis demands a great deal. **Equally INADMISSIBLE is the mirror-image overrun:** "the 2026 paper shows oxygen was irrelevant." It shows *one mechanism* fails *one morphometric scaling test*. Class: **OBSERVED-CONTESTED** — print both citations or neither.
- **"Quetzalcoatlus weighed X kg."** — **INADMISSIBLE as a point estimate.** Published values span **70 → 544 kg** (~8×) from the same fossils. Quoting one reports a preference. Quote the spread or say nothing — and quote it *whole*: rounding 544 down to "~500" quietly reports a smaller disagreement than the literature contains, which is the same defect one rounding-step milder.
- **"Gaia is science" / "Gaia is nonsense."** — **Both INADMISSIBLE as stated.** The disequilibrium observation is OBSERVED-REPLICATED and independent of the theory; the regulation claim is HYPOTHESIZED with a live, unanswered mechanism objection (Doolittle 1981; Dawkins 1982: no unit of selection, one non-reproducing Earth). Contempt is a defect exactly as much as credulity is; the fence goes on the claim, not the claimant.
- **"Daisyworld shows Earth self-regulates."** — **NEGATIVE / category error, and the most common one here.** Watson & Lovelock (1983) is an **existence proof that a mechanism is possible** without teleology — which genuinely defuses the "Gaia needs foresight" objection. It is **not** evidence that Earth runs that mechanism. A model showing X *can* occur and an observation that X *does* occur are different claims. Daisyworld supplies only the first, and cannot in principle supply the second.
- **NOT-SOURCED in this pass:** the *Quetzalcoatlus* mass primaries (Chatterjee & Templin 2004; Paul 2002; Witton 2008; Witton & Habib 2010; Martin & Palmer 2014; Henderson 2010) are attributed via fetched secondary reports, not read; the Hadley local-`Ro` value of 0.3–0.6 at cell extremities is from a fetched summary of the axisymmetric literature; Pennycuick's **~12 kg** ceiling is via secondary reports rather than the primary — **as is the bustard census (~16 kg mean, >20 kg verified) it is measured against**, so *both sides* of the ceiling-vs-census comparison are secondary and neither may be hardened until read; the atmospheric-absorption table is a **tertiary** reproduction of NPL *Kaye & Laby* (the NPL host failed TLS verification; ISO 9613-1 was paywalled and scanned). Closure for all: fetch the primaries.
- **NOT-MEASURED:** absorption coefficients below 1 kHz — **the infrasound long-range claim here is an extrapolation, not a fetched number**, and CN-09/CN-10 must source it independently; the fraction of solar input appearing as circulation kinetic energy; primary references for `μ_air`, `μ_water`, `ρ_water`, `c_water`, `Ω`, `S`, and Earth's albedo — **and note that `S` and albedo are not merely unsourced here: the NASA sheet this chapter cites eight times contradicts both** (0.385 / 1367.6 W/m² / 247.3 K), and the judgement that it is stale rather than right is itself owed a CERES/TSI primary.

## HONEST FENCE — MODELED

This chapter is fenced **MODELED**. Individual rows carry their own classes — many OBSERVED-REPLICATED, several OBSERVED-CONTESTED (the GOE date, the O₂/gigantism mechanism, *Quetzalcoatlus*), one HYPOTHESIZED (Gaia), several NOT-MEASURED — but the *chapter as an artifact* is a composition: it runs measured constants through stated idealisations (isothermal atmosphere; ideal gas; dry air; isometric scaling of flyers; `C_L` = 1.0 and AR = 8 assumed for a whale that has neither) to reach design conclusions. **The idealisations are the fence, and the chapter prints the places they break on purpose** — the 100 km pressure row is retained *because* it is wrong; the `M_atm` gap is retained *because* it resolves to mountains.

Per **Gould & Lewontin (1979), "The Spandrels of San Marco and the Panglossian Paradigm"**: nothing above establishes that any organism's relationship to air is an optimum. That flying birds run out at ~16–21 kg is consistent with the 7/6 law *and* with phylogenetic inertia, drift, developmental constraint, and contingency. Convergence is evidence of a constraint-optimum, not proof of one. **Nature's authority here is precise and limited: it has already run a very long parallel search in this exact fluid, at this exact `ν`, under real physical constraints, with the failures deleted.** That makes every number above a **hypothesis generator**. Per repo rule **M7**, any air-inspired design taken from this chapter must still beat a **tuned conventional baseline** on a **pre-registered metric**, with a discriminator that collapses the claimed gain and a true computed-residual ablation, or it is recorded **NEGATIVE**.

## Not claimed

- **Not claimed:** that the atmosphere is regulated, homeostatic, purposive, alive, or an agent. The disequilibrium is measured; the regulation is HYPOTHESIZED and carries an unanswered unit-of-selection objection. Daisyworld is a mechanism's existence proof, not evidence about Earth. These three travel separately.
- **Not claimed:** that high Palaeozoic O₂ caused insect gigantism, **or that it did not.** The class is OBSERVED-CONTESTED as of July 2026 and the chapter refuses to collapse it in either direction.
- **Not claimed:** any single mass for *Quetzalcoatlus northropi*. The ~8× spread (70 → 544 kg) is the finding.
- **Not claimed:** that the isothermal scale height describes the real atmosphere above ~2`H`. It is a derivation with a stated failure altitude, printed with its failure.
- **Not claimed:** that `α ∝ f²` describes real air in the audible band; that Rayleigh's `1/λ⁴` alone predicts sky colour; or that any dated value here survives its date.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** Reading Berner 2006 does not make any UNI claim proven, designed, or built. The NATURA class vocabulary (OBSERVED-REPLICATED / OBSERVED-CONTESTED / MODELED / HYPOTHESIZED / INADMISSIBLE / NOT-MEASURED) and the UNI ledger vocabulary (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. This chapter contains **zero** UNI claims.
- **Not claimed:** that "nature does it this way" is an argument. See the Gould & Lewontin fence.
- **QUAESTIO-APERTA:** "full human" and "beyond human" appear nowhere in this chapter as a target, milestone, or deliverable. They are permanent open questions, and atmospheric physics has no bearing on them.


<!-- ===== END cookbook/recipes-natura/CN-03-air.md ===== -->



<!-- ===== BEGIN cookbook/recipes-natura/CN-04-stars.md ===== -->

# CN-04 — Stars: the factory that made every atom in the cell

> **What you are building.** The provenance chain for the matter in NA-08's cell — an audit trail from a proton to a carbon atom to a gold atom, with a source on every link and NOT-MEASURED where the chain is open. Along the way you are building two transferable things: a reading of a star as a **negative-feedback control system** (which is load-bearing, not decorative), and a third instance of the **hidden-state inference** method that CN-01 and NA-02 already use. Nothing here raises any UNI rung — a citation to astrophysics is never a UNI gate.

---

## The one equation that holds a star up

A star is not held up by anything exotic. It is held up by its own pressure gradient against its own weight:

```
dP/dr = −G · M(r) · ρ(r) / r²
```

That is hydrostatic equilibrium. Every stable star satisfies it on timescales longer than its sound-crossing time. The interesting content is not the equation — it is what happens when you perturb it.

**Read it as a control loop.** The core contracts slightly; compression raises `T`. Nuclear rates are ferociously steep in temperature — the logarithmic sensitivity `ν = ∂ln ε/∂ln T` is **~4** for the p-p chain near 15 MK, **~18–20** for CNO, **~40** for triple-alpha near 10⁸ K *(standard reference values; not primary-sourced in this pass)*. So a 1% contraction buys a large jump in energy generation. Pressure rises, the core expands, `T` falls, the rate falls back. The loop closes. This is a proportional controller whose gain is the temperature exponent and whose **feedback path is the ideal-gas equation of state**, `P ∝ ρT` — the `T` there is what couples pressure back to the thermostat.

**The reading earns its keep because the loop can break.** In a *degenerate* core, electron degeneracy pressure is nearly independent of temperature: `P ≈ P(ρ)`, and `T` drops out of the feedback path. A temperature rise now raises the reaction rate but *not* the pressure, so nothing damps it. The result is thermonuclear runaway — the helium flash, and, in the accreting-white-dwarf channel, the Type Ia supernova that is modelled as the source of roughly half to two-thirds of the iron in your blood (MODELED/CONTESTED — see the `f_Fe,Ia` row). A star is a reactor with a mechanical governor; remove the governor and it detonates.

**One caveat.** Dimensional analysis gives `P_c ~ GM²/R⁴`; the exact uniform-density result `P_c = 3GM²/(8πR⁴)` evaluates for the Sun to **~1.3 × 10¹⁴ Pa**. The true value is **~170× higher** (`P_c,☉` ≈ 2.3 × 10¹⁶ Pa, SSM; arXiv:2501.09971 Table 1), because the Sun is nothing like uniform: central density **~149 g/cm³** against a mean of **1.41 g/cm³**, a factor of **~106**. The scaling is right; the prefactor is worthless without structure.

## Before the star: the Jeans criterion

Stars need a prior step — a cloud that collapses. The **Jeans criterion** (Jeans 1902, *Phil Trans R Soc A* 199:1–53) sets when self-gravity beats thermal support: a perturbation grows if its wavelength exceeds

```
λ_J = c_s · √(π / (G ρ))
```

Below `λ_J`, pressure crosses the region faster than gravity can collapse it and the perturbation merely oscillates. Above it, gravity wins. The competition in one line: **can a signal cross the region before gravity closes it?**

**Recorded honestly — the Jeans swindle.** The derivation linearises about a *uniform, static, infinite* background. But a uniform static self-gravitating medium is **not a solution of the equations** — it would itself be collapsing. The background field is silently set to zero to make the algebra work; the defect is known and named (Binney & Tremaine, *Galactic Dynamics*). The criterion survives because it approximates well where other methods can check it, not because the derivation is sound.

## The organizing observation: the HR diagram

Plot luminosity against effective temperature for many stars and they do **not** fill the plane. About 90% collapse onto a narrow diagonal band — the main sequence — with sparse clumps for giants, supergiants, and white dwarfs (Hertzsprung 1911; Russell 1914, *Nature* 93:252). Its content is *negative*: the plane is mostly empty. A 2-D observable space collapsing to a 1-D locus means one parameter nearly determines the star. That parameter is **mass**.

**Fenced:** the tidy statement — the **Vogt–Russell "theorem"**, that mass and composition uniquely fix structure and evolution — **is not a theorem**. Never proved, with known counterexamples. A heuristic that is usually approximately right.

## The scaling law — and what the textbook gets wrong

The main sequence's collapse is quantified by the mass–luminosity relation, `L ∝ M^α`. Every textbook prints **α ≈ 3.5**. The best modern calibration says that number **does not exist**.

Eker et al. (2018), *MNRAS* 479(4):5491–5511 (doi:10.1093/mnras/sty1834), fitted 509 main-sequence stars from detached eclipsing binaries over `0.179 ≤ M/M☉ ≤ 31` and found a **six-piece** relation, with break points where the energy-transport mechanism shifts:

| Domain | Mass range (M☉) | α |
|---|---|---|
| Ultra low-mass | 0.179 – 0.45 | **2.028** |
| Very low-mass | 0.45 – 0.72 | **4.572** |
| Low mass | 0.72 – 1.05 | **5.743** |
| Intermediate | 1.05 – 2.40 | **4.329** |
| High mass | 2.40 – 7 | **3.967** |
| Very high mass | 7 – 31 | **2.865** |

**No piece is 3.5.** The exponent runs from 2.0 to 5.7 and is *non-monotonic*. The canonical 3.5 is a rough average over a range that should never have been averaged, and the break points are the physics — they mark transitions in how energy gets out. `M^3.5` is defensible as an order-of-magnitude device and indefensible as a measurement.

### The rhyme with allometry — and why it is only a rhyme

Kleiber's law says metabolic rate scales as `B ∝ M^(3/4)` across organisms (cross-ref **NA-05**); here power output scales as `L ∝ M^α` across stars. Both are power laws relating a mass to a power, and the temptation to call this a deep unity is strong. **Refuse it.** Four reasons, each sufficient alone:

1. **The exponents are not close.** 3/4 versus 2.0–5.7.
2. **The sign of `α − 1` is opposite.** Kleiber is *sublinear* — a bigger animal burns *less* power per kilogram. The stellar relation is wildly *superlinear*. Not one phenomenon with different constants; they point in opposite directions.
3. **The mechanisms share nothing.** The stellar exponent falls out of radiative-diffusion opacity plus the mass–radius–T_eff relation. Kleiber's candidate mechanisms are distribution-network geometry or surface-limited heat loss — themselves contested (Dodds, Rothman & Weitz 2001, *J Theor Biol* 209(1):9–27; White & Seymour 2003, *PNAS* 100(7):4046–4049, doi:10.1073/pnas.0436428100, report ~2/3 for mammals).
4. **A power law is the generic output of a scale-free constraint.** Many unrelated mechanisms produce one; a shared functional *form* is the weakest available evidence of shared mechanism.

So: **a rhyme, recorded as a rhyme.** "Everything follows power laws" is not a unification — it is what happens when a few constraints dominate. Cataloguing that is useful; calling it a law of nature is the defect this wing exists to prevent.

## Lifetime: why heavy elements exist at all

Fuel goes as `M`, burn rate as `L`, so `t ∝ M/L ∝ M^(1−α)`.

With the textbook α = 3.5, `t ∝ M^(−2.5)`; anchoring on the Sun at ~10¹⁰ yr, a 30 M☉ star gets `10¹⁰ × 30^(−2.5) ≈ 2 × 10⁶ yr`. With Eker's *measured* α = 2.865 for that range the exponent is −1.865 and the same arithmetic gives `≈ 1.8 × 10⁷ yr` — **nine times longer**. Both are crude: the naive scaling assumes a fixed burned-fuel fraction, but massive stars have large convective cores and burn more of it, pushing the other way. Detailed tracks land in between. **The honest version:** this argument does not settle the exponent, but the *order* is robust — **10⁶–10⁷ yr**, three to four orders below the Sun. That is all it needs, and it is this chapter's load-bearing point:

**Big stars die fast, and that is the only reason heavy elements are in circulation.** The Solar System formed 4.567 Gyr ago (Pb–Pb dating of CAIs; Connelly et al. 2012, *Science* 338:651–655) in a Galaxy roughly 13 Gyr old. A star that lives 10⁶–10⁷ yr and explodes has run **thousands of generations** in that window, each returning processed material to the interstellar medium. If massive stars lived as long as the Sun, the enrichment timescale would be comparable to the age of the Galaxy and the pre-solar nebula would have been nearly pristine — no rock, no iron, no cell. The steep negative exponent decouples the enrichment clock from the cosmic clock.

## The burning

**p-p chain.** Four protons to one ⁴He via deuterium and ³He. The standard solar model attributes **~99%** of solar energy to it, **~1%** to CNO (Salmon et al. 2021, *A&A* 651, A106, arXiv:2105.00911; the solar-neutrino review arXiv:2501.09971 Table 1 gives central `T = 1.54 × 10⁷ K`, `ρ = 149 g/cm³`).

**CNO cycle.** Same net reaction, but C/N/O act as *catalysts* — consumed and regenerated. Far steeper in `T` (ν ~ 18–20), so it takes over above ~17–18 MK and dominates above a solar mass. Note the dependency: CNO **needs carbon a previous generation made**. The first stars could not run it.

**And it is measured, not assumed.** The Borexino Collaboration (2020), *Nature* 587:577–582 (doi:10.1038/s41586-020-2934-0), detected solar CNO neutrinos directly from 1,072 days of Phase-III live time: **Φ(CNO) = 7.0 (+3.0 / −2.0) × 10⁸ cm⁻² s⁻¹**. The collaboration's *final* result — Correlated Integrated Directionality over the complete 2007–2021 dataset, combined with an improved Phase-III spectral fit (Borexino Collaboration 2023, *Phys Rev D* 108:102005, arXiv:2307.14636) — tightens that to **6.7 (+1.2 / −0.8) × 10⁸**. A catalytic cycle in the core of a star 1.5 × 10⁸ km away, confirmed by counting neutrinos in a tank under a mountain.

**Triple-alpha — the bottleneck.** Two ⁴He make ⁸Be, which is **unbound** and falls apart in ~10⁻¹⁶ s *(standard nuclear data; not primary-sourced in this pass)*. With no stable mass-5 or mass-8 nucleus, the road from helium to carbon is washed out. Salpeter (1952) noted that at stellar core densities a tiny *equilibrium* population of ⁸Be persists, so ⁸Be + ⁴He → ¹²C can proceed — but the rate came out far too low to make the carbon that is observably there.

## Hoyle's prediction: this wing's thesis in one anecdote

Fred Hoyle's move in 1953 is the cleanest demonstration in the history of science of the method NA-01 argues for. He did not measure a nucleus. He reasoned:

> Carbon exists, in the observed cosmic abundance. The known triple-alpha rate cannot make it. Therefore the rate is wrong. Therefore there must be an unknown **resonance** in ¹²C, just above the ⁸Be + α threshold, that enormously enhances the cross-section. It should sit near **7.68 MeV** and have spin-parity **0⁺**.

**That is a specific, falsifiable number, extracted from an abundance.** Hoyle took it to the Kellogg Radiation Laboratory at Caltech and asked them to look. They looked. Dunbar, Pixley, Wenzel & Whaling (1953), "The 7.68-Mev State in C¹²", *Phys Rev* 92:649–650 (doi:10.1103/PhysRev.92.649), **found it**; the prediction is recorded in Hoyle, Dunbar, Wenzel & Whaling (1953), *Phys Rev* 92:1095, and developed in Hoyle (1954), *ApJS* 1:121. The modern value is **7,654.07 ± 0.19 keV**, 0⁺, the second excited state of ¹²C (NNDC, via Freer & Fynbo 2014, *Prog Part Nucl Phys* 78:1–23, doi:10.1016/j.ppnp.2014.06.001); rates were revised again by Fynbo et al. (2005), *Nature* 433:136–139 (doi:10.1038/nature03219).

An observation about nature — *how much carbon there is* — predicted the excitation energy of a nuclear state, and the prediction held. Nature had already run the experiment; Hoyle read the answer off the output and inverted it to a constant.

**Now the correction, because the story is usually told wrong.** The popular version is that Hoyle predicted the resonance *because carbon-based life exists* — the founding anthropic prediction. **This is historically refuted.** Kragh (2010), "An anthropic myth: Fred Hoyle's carbon-12 resonance level", *Archive for History of Exact Sciences* 64:721–751 (doi:10.1007/s00407-010-0068-8), shows Hoyle and his contemporaries did not connect the level to life at all; the anthropic gloss was retrofitted in the 1980s. **And the true version is better.** "We exist" is not a quantitative constraint and predicts no number. **The cosmic carbon abundance is a measurement**, and it did the work. Stripping the mysticism off does not diminish the story — it is the difference between an anecdote and a method.

## The iron peak: why fusion stops

Binding energy per nucleon rises steeply from hydrogen, peaks, and falls. Fusion releases energy only while climbing; past the peak it **costs** energy. At the top the fuel is not exhausted, it is *thermodynamically unavailable*.

**The peak is not where you were told.** Highest binding energy per nucleon is **⁶²Ni at 8.7945 MeV/nucleon**, then **⁵⁸Fe at 8.7922**, then **⁵⁶Fe at 8.7903** — first to third spans **4.2 keV/nucleon, 0.048%**. ⁵⁶Fe is nevertheless routinely called "the most stable nucleus", and a real fact sits under the sloppy phrasing: ⁵⁶Fe has the **lowest mass per nucleon**, a different quantity, because ⁶²Ni carries a larger neutron fraction (34/62 vs 30/56) and neutrons are heavier than protons. Both are true of different quantities; quoting either as "the" answer without naming the quantity is the error.

**And stars do not make ⁵⁶Fe directly.** Silicon burning under nuclear statistical equilibrium favours the alpha-conjugate **⁵⁶Ni** (Z = N = 28); iron arrives by decay, ⁵⁶Ni → ⁵⁶Co (t½ ≈ 6 d) → ⁵⁶Fe (t½ ≈ 77 d) *(standard nuclear data; not primary-sourced in this pass)*. Not a footnote — **that chain powers the Type Ia light curve**. The cosmological standard candle is radioactive nickel turning into the iron in your haemoglobin, in public, on a 77-day clock. Once the core is iron-peak the governor has nothing left to burn; photodisintegration and electron capture remove pressure support and the core collapses in of order a second.

## Beyond iron: s-process, r-process, and what GW170817 actually showed

Above iron the Coulomb barrier is too high and fusion is endothermic. Everything heavier is built by **neutron capture**, which has no barrier. Burbidge, Burbidge, Fowler & Hoyle (1957), "Synthesis of the Elements in Stars", *Rev Mod Phys* 29:547–650 — B²FH — laid out the classification that still stands, independently with Cameron (1957).

- **s-process (slow).** Capture slower than β⁻ decay, so the path hugs the valley of stability. Site: thermally pulsing AGB stars. Roughly half the nuclei above iron, up to Bi/Pb.
- **r-process (rapid).** Capture much faster than β⁻ decay, driving far to the neutron-rich side before decaying back. The other half — **and all the actinides**. Requires extreme neutron densities.

**The r-process site was open for sixty years.** GW170817 (Abbott et al. 2017, *Phys Rev Lett* 119:161101) — a neutron-star merger seen in gravitational waves with an electromagnetic counterpart, the kilonova AT2017gfo — closed a large part of it. Watson et al. (2019), *Nature* 574:497–500 (doi:10.1038/s41586-019-1676-3), identified a **Sr II** P Cygni feature at ~8000 Å at 1.4, 2.4 and 3.4 days post-merger: a freshly synthesised neutron-capture element in the spectrum of a merger.

**Now the correction, and it matters.** It is widely written — including in the brief that commissioned this chapter — that GW170817 **measured the origin of gold**. It did not. Gillanders et al. (2021), *MNRAS* 506(3):3560–3577 (doi:10.1093/mnras/stab1861), searched AT2017gfo specifically for platinum and gold and found **no prominent Pt or Au signatures**, setting tentative upper limits **Pt ≲ a few × 10⁻³ M☉**, **Au ≲ 10⁻² M☉**.

The honest chain: **strontium (Z = 38) was identified** → an r-process runs in neutron-star mergers → gold (Z = 79) is an r-process product **by abundance pattern and nuclear theory** → mergers are inferred to be *a* site of gold production. Every link is defensible, but **"measured" attaches to strontium and nothing heavier.** "We know where gold comes from because we saw it" is false; "an r-process runs in neutron-star mergers because we saw strontium, and gold is an r-process element" is true — three links, one of them theory. **Also contested:** whether mergers are the *dominant* r-process site. Mergers take time to inspiral, yet r-process europium sits in very old metal-poor stars, which some models cannot reach without a prompt channel (rare magnetorotational supernovae, collapsars). Site identified; budget open.

## The Eddington limit

There is a ceiling on how bright a thing can be and still hold together. Radiation carries momentum; at high enough luminosity, radiation pressure on free electrons (Thomson scattering), coupled to protons electrostatically, exceeds gravity and the outer layers leave:

```
L_Edd = 4π G M m_p c / σ_T
```

Evaluating (G = 6.674 × 10⁻¹¹, m_p = 1.673 × 10⁻²⁷ kg, c = 2.998 × 10⁸ m/s, σ_T = 6.652 × 10⁻²⁹ m², M☉ = 1.989 × 10³⁰ kg): **L_Edd ≈ 1.26 × 10³¹ (M/M☉) W ≈ 3.3 × 10⁴ (M/M☉) L☉** (Eddington 1926, *The Internal Constitution of the Stars*). The Sun's 3.828 × 10²⁶ W is **3.0 × 10⁻⁵ of its Eddington limit** — nowhere near radiation-limited. Very massive stars run within a factor of a few of it, which is why they shed mass in violent winds and why the stellar mass function has an upper end.

**Fenced:** the derivation assumes spherical symmetry, steady state, fully ionised hydrogen, and electron-scattering opacity *only*. Real atmospheres are clumped and line-driven; genuinely super-Eddington sources are observed (ultraluminous X-ray sources). A scaling and an idealisation, not a hard wall.

## Frequencies: the Sun rings, and we listen

**This is the same method as CN-01 and NA-02, in a third domain.** The photosphere is opaque, so you infer the hidden interior from the frequencies of its surface oscillations.

Leighton, Noyes & Simon (1962), *ApJ* 135:474, discovered a ubiquitous **~5-minute oscillation** in photospheric velocity. Ulrich (1970), *ApJ* 162:993, and Leibacher & Stein (1971) interpreted it as *standing acoustic waves* — global modes trapped in a cavity, refracted back up by the rising sound speed at depth and reflected down at the surface — and Deubner (1975), *A&A* 44:371, confirmed it by resolving the predicted ridges in the k–ω diagram. Power peaks near **3,300 μHz ≈ 3.3 mHz**.

The inference works because **each mode samples a different depth**: a mode's frequency is an integral of the sound speed over its cavity. Measure many, invert, and you recover `c_s(r)` through 700,000 km of plasma you will never see. Bahcall, Pinsonneault & Basu (2001), *ApJ* 555:990, report the rms fractional difference between standard-solar-model and helioseismic sound speeds as **0.10% across 0.05–0.95 R☉** — a model of a star's interior, checked against its ringing, agreeing to one part in a thousand.

**The residual is where the science is — and it is live.** Asplund et al. (2009), *ARA&A* 47:481 (AGSS09), revised solar C/N/O abundances *downward* using 3D hydrodynamic model atmospheres — better atmospheric physics. Models built on those low-metallicity abundances **break** the helioseismic agreement; the older high-metallicity GS98 abundances (Grevesse & Sauval 1998) preserve it. This is the **solar abundance problem**, unresolved. Borexino's CNO flux is a third, independent probe, and it lands **consistent with high-metallicity models**, disfavouring low-Z (Borexino Collaboration 2023, *Phys Rev D* 108:102005, arXiv:2307.14636; arXiv:2501.09971).

So: two independent hidden-state inference channels — acoustic modes and neutrinos — agree with each other and disagree with the best spectroscopic atmosphere modelling. Nobody knows why. **That is what an honest inference problem looks like.** The method is not "the model matched, therefore we understand the Sun." It is *the model matched to 0.10%, and the residual is now the most informative thing in the room*.

**Pulsar timing** is the same trick with a different clock. Hulse & Taylor (1975), *ApJ* 195:L51, found PSR B1913+16, a pulsar bound to another neutron star. Pulse arrival times are the signal; general relativity is the generative model; the **residual** carries the hidden state. Weisberg & Huang (2016), *ApJ* 829:55 (doi:10.3847/0004-637X/829/1/55), analysed **9,257 times-of-arrival over 35 years** and report the ratio of observed orbital decay (kinematically corrected) to the GR prediction as **0.9983 ± 0.0016**, with masses **1.438 ± 0.001** and **1.390 ± 0.001 M☉**. Gravitational-wave emission, inferred to ~0.2% from the timing of a rotating star **~4 kpc (~13,000 light years)** away, decades before a wave was directly detected.

**Three domains — Earth's interior, the Sun's interior, a binary's orbit — one method.** Observe a frequency at an accessible surface; hold a generative model of the inaccessible interior; invert; then *read the residual*. Not an analogy: the same inference, and the one NA-02 describes.

## We are made of star stuff — the provenance table

Sagan's phrase is not poetry. It is a sourced supply chain — with honest gaps. General reference: Johnson (2019), "Populating the periodic table: Nucleosynthesis of the elements", *Science* 363(6426):474–478 (doi:10.1126/science.aau9540).

| Element (in the cell) | Dominant origin | Class | Note |
|---|---|---|---|
| **H** (water, every organic molecule) | Big Bang nucleosynthesis, first ~3 min | OBSERVED-REPLICATED | Never made since, only consumed |
| **He** | BBN (`Y_p ≈ 0.245` primordial mass fraction) + stellar H burning | OBSERVED-REPLICATED | Biologically inert; the intermediate for everything else |
| **Li, Be, B** | BBN (⁷Li) + cosmic-ray spallation | **OBSERVED-CONTESTED** | The **primordial lithium problem** is open: BBN+CMB over-predicts ⁷Li vs old stars by ~3× |
| **C** | Triple-alpha, via the Hoyle state | OBSERVED-REPLICATED (process) / **CONTESTED** (site split) | AGB stars vs massive stars — the budget split is model-dependent |
| **N** | CNO cycle; AGB hot-bottom burning | OBSERVED-REPLICATED (process) | Site split model-dependent |
| **O** | He/C burning in massive stars → core-collapse SNe | OBSERVED-REPLICATED | The most abundant element in your body by mass |
| **Fe** | **~50–70% Type Ia**, remainder core-collapse | **MODELED / CONTESTED** | Via ⁵⁶Ni → ⁵⁶Co → ⁵⁶Fe. Solar-neighbourhood chemical-evolution estimates genuinely spread |
| **Au** | r-process; neutron-star mergers identified as *a* site | **MODELED** (Au itself), OBSERVED (Sr) | **Gold was NOT detected in AT2017gfo** (Gillanders et al. 2021). Sr was (Watson et al. 2019) |

Read the table honestly and the sentence lands harder than the poetry version. The hydrogen in the water in your cells has not been touched since the first three minutes of the universe. The carbon in every protein exists because a nuclear resonance sits 7,654 keV above the ¹²C ground state — and because Hoyle inferred that number from an abundance before anyone measured it. The oxygen came from stars that lived a few million years and exploded. Roughly half to two-thirds of the iron in your blood is modelled to have been assembled as nickel in a detonating white dwarf and decayed into iron over the following months. And the gold is the honest one: we have identified an r-process running in colliding neutron stars, and we infer the gold from the pattern. **We have not seen it.**

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `dP/dr` | `−GM(r)ρ(r)/r²` | Pa/m | hydrostatic equilibrium; any star on timescales ≫ sound-crossing | MODELED | standard stellar structure | A stable star with a measured pressure gradient inconsistent with its mass distribution |
| `ν_pp` | ~4 | dimensionless (`∂ln ε/∂ln T`) | p-p chain near 15 MK | OBSERVED-REPLICATED *(standard reference; not primary-sourced in this pass)* | standard nuclear astrophysics | Measured cross-section temperature dependence outside range |
| `ν_CNO` | ~18–20 | dimensionless | CNO cycle near 15–20 MK | OBSERVED-REPLICATED *(standard reference; not primary-sourced in this pass)* | as above | As above |
| `ν_3α` | ~40 | dimensionless | triple-alpha near 10⁸ K | OBSERVED-REPLICATED *(standard reference; not primary-sourced in this pass)* | as above | As above |
| `T_c,☉` | 1.54 × 10⁷ | K | standard solar model, current epoch | MODELED | arXiv:2501.09971 Table 1; cf. Salmon et al. 2021, *A&A* 651, A106, arXiv:2105.00911 | An SSM variant outside 1.4–1.7 × 10⁷ K reproducing helioseismology + neutrinos |
| `ρ_c,☉` | 149 | g/cm³ | standard solar model, current epoch | MODELED | arXiv:2501.09971 Table 1 | As above |
| `ρ_mean,☉` | 1.41 | g/cm³ | `M☉/((4/3)πR☉³)`, M☉=1.989×10³⁰ kg, R☉=6.957×10⁸ m | MODELED | Computed here | Arithmetic error |
| `ρ_c/ρ_mean` | ~106 | dimensionless | Sun | MODELED | Computed here from the two rows above | Arithmetic error |
| `P_c` (uniform-ρ) | ~1.3 × 10¹⁴ | Pa | `3GM²/(8πR⁴)`, Sun — **a lower bound, not a value**; the SSM value is **~170× higher** (next row) | MODELED | Computed here | Arithmetic error |
| `P_c,☉` (SSM) | 2.3 × 10¹⁶ | Pa | standard solar model, current epoch | MODELED | arXiv:2501.09971 Table 1 | An SSM variant outside this range reproducing helioseismology + neutrinos |
| `λ_J` | `c_s√(π/(Gρ))` | m | Jeans length, isothermal, uniform static background | MODELED | Jeans 1902, *Phil Trans R Soc A* 199:1–53 | See the Jeans-swindle row |
| Jeans swindle | derivation linearises about a background that is not a solution | — | the `λ_J` derivation | **INADMISSIBLE as rigorous** | Binney & Tremaine, *Galactic Dynamics* | A derivation retaining the background field that recovers `λ_J` |
| `α` (MLR) | **2.028 / 4.572 / 5.743 / 4.329 / 3.967 / 2.865** | dimensionless | six pieces over 0.179–31 M☉; 509 stars, detached eclipsing binaries | OBSERVED-REPLICATED | Eker et al. 2018, *MNRAS* 479(4):5491–5511, doi:10.1093/mnras/sty1834 (Table 4) | An independent DEB sample with a single exponent, or different break points |
| `α` = 3.5 | **not found in any piece** | dimensionless | the textbook value | **SUPERSEDED** | contradicted by Eker et al. 2018 | Show a mass range where 3.5 is the calibrated fit |
| `t_MS,☉` | ~10¹⁰ | yr | Sun, main sequence | MODELED *(standard reference; not primary-sourced in this pass)* | standard stellar evolution | Evolutionary track outside 8–12 Gyr |
| `t_MS(30 M☉)` | **2 × 10⁶ (α=3.5) vs 1.8 × 10⁷ (α=2.865)**; robust range **10⁶–10⁷** | yr | `t ∝ M^(1−α)`, anchored on the Sun | MODELED | Computed here from Eker et al. 2018 + `t ∝ M/L` | A detailed evolutionary track for 30 M☉ outside 10⁶–10⁷ yr |
| `t_☉,formation` | 4.567 × 10⁹ | yr | Pb–Pb dating of CAIs | OBSERVED-REPLICATED | Connelly et al. 2012, *Science* 338:651–655 | Independent radiometric dating >1% off |
| `f_pp` / `f_CNO` | ~99 / ~1 | % of solar energy | standard solar model | MODELED, **confirmed for CNO** | Salmon et al. 2021, *A&A* 651, A106, arXiv:2105.00911; arXiv:2501.09971 | An SSM with a materially different split fitting the neutrino data |
| `Φ(CNO)` **final** | **6.7 (+1.2 / −0.8) × 10⁸** | cm⁻² s⁻¹ | solar CNO neutrinos; CID over the complete 2007–2021 dataset + an improved Phase-III spectral fit | OBSERVED-REPLICATED | Borexino Collaboration 2023, *Phys Rev D* 108:102005, arXiv:2307.14636 | An independent detector outside the interval |
| `Φ(CNO)` **first detection** | **7.0 (+3.0 / −2.0) × 10⁸** | cm⁻² s⁻¹ | solar CNO neutrinos; Borexino Phase-III spectral fit, 1,072 d live time | OBSERVED-REPLICATED | Borexino Collaboration 2020, *Nature* 587:577–582, doi:10.1038/s41586-020-2934-0 | Superseded in precision, not in fact |
| `t½(⁸Be)` | ~10⁻¹⁶ | s | ⁸Be ground state, unbound | OBSERVED-REPLICATED *(standard nuclear data; not primary-sourced in this pass)* | standard nuclear data tables | Measured lifetime >10× off |
| `E_x(Hoyle)` **predicted** | **~7.68** | MeV | Hoyle's prediction from the observed carbon abundance, 1953 | — (a prediction, not a measurement) | Hoyle, Dunbar, Wenzel & Whaling 1953, *Phys Rev* 92:1095 | Historical record |
| `E_x(Hoyle)` **first measured** | **7.68** | MeV | Kellogg Radiation Laboratory, 1953 | OBSERVED-REPLICATED | Dunbar, Pixley, Wenzel & Whaling 1953, *Phys Rev* 92:649–650, doi:10.1103/PhysRev.92.649 | Superseded in precision, not in fact |
| `E_x(Hoyle)` **modern** | **7,654.07 ± 0.19** | keV | ¹²C second excited state, 0⁺ | OBSERVED-REPLICATED | NNDC, via Freer & Fynbo 2014, *Prog Part Nucl Phys* 78:1–23, doi:10.1016/j.ppnp.2014.06.001 | A measurement outside ±0.19 keV |
| `BE/A(⁶²Ni)` | **8.7945** | MeV/nucleon | **highest known** binding energy per nucleon | OBSERVED-REPLICATED | standard nuclear mass tables | A nuclide measured higher |
| `BE/A(⁵⁸Fe)` | 8.7922 | MeV/nucleon | second | OBSERVED-REPLICATED | as above | As above |
| `BE/A(⁵⁶Fe)` | 8.7903 | MeV/nucleon | third — but **lowest mass per nucleon** (a different quantity) | OBSERVED-REPLICATED | as above | Show ⁵⁶Fe has the highest BE/A, or that mass/nucleon and BE/A are the same quantity |
| `ΔBE/A` (⁶²Ni − ⁵⁶Fe) | 4.2 (0.048%) | keV/nucleon | the whole "iron peak" spread | MODELED | Computed here from the rows above | Arithmetic error |
| `t½(⁵⁶Ni → ⁵⁶Co)` | ~6 | d | powers the early Type Ia light curve | OBSERVED-REPLICATED *(standard nuclear data; not primary-sourced in this pass)* | standard nuclear data tables | Measured half-life >10% off |
| `t½(⁵⁶Co → ⁵⁶Fe)` | ~77 | d | powers the Type Ia light-curve tail | OBSERVED-REPLICATED *(standard nuclear data; not primary-sourced in this pass)* | standard nuclear data tables | As above |
| `f_Fe,Ia` | **~50–70** | % of solar-neighbourhood ⁵⁶Fe | chemical-evolution estimates genuinely spread | **MODELED / CONTESTED** | galactic chemical evolution literature; Johnson 2019, *Science* 363:474–478 | A model-independent measurement of the split |
| Sr II in AT2017gfo | P Cygni ~8000 Å at 1.4, 2.4, 3.4 d post-merger | — | kilonova AT2017gfo / GW170817 | OBSERVED-REPLICATED | Watson et al. 2019, *Nature* 574:497–500, doi:10.1038/s41586-019-1676-3 | Reanalysis attributing the feature to a non-r-process species |
| **Au in AT2017gfo** | **NOT DETECTED**; `M_Au ≲ 10⁻²`, `M_Pt ≲ few × 10⁻³` | M☉ (upper limits) | "no platinum or gold signatures are prominent in the ejecta" | **NOT-MEASURED** (upper limits only) | Gillanders et al. 2021, *MNRAS* 506(3):3560–3577, doi:10.1093/mnras/stab1861 | A spectroscopic identification of Au or Pt in a kilonova |
| `M_ejecta`(AT2017gfo) | — | M☉ | total r-process ejecta mass | **NOT-SOURCED in this pass** | not confirmed here | Fetch the kilonova modelling papers and read the mass |
| r-process **dominant** site | mergers identified as *a* site; dominance open (delay-time vs Eu in metal-poor stars) | — | galactic r-process budget | **OBSERVED-CONTESTED** | Watson et al. 2019 (site); chemical-evolution tension | A chemical-evolution model reproducing early Eu with mergers alone |
| `f_5min` | ~3,300 (≈3.3 mHz, ~5 min period) | μHz | solar p-mode power peak | OBSERVED-REPLICATED | Leighton, Noyes & Simon 1962, *ApJ* 135:474; Deubner 1975, *A&A* 44:371 | Independent Doppler imaging failing to find the peak |
| `Δc_s/c_s` | **0.10** | % (rms fractional) | SSM vs helioseismic inversion, 0.05–0.95 R☉ | OBSERVED-REPLICATED (inversion) / MODELED (the model side) | Bahcall, Pinsonneault & Basu 2001, *ApJ* 555:990 | An independent inversion disagreeing at >0.5% |
| Solar abundance problem | low-Z (AGSS09) breaks helioseismic agreement; high-Z (GS98) preserves it; Borexino CNO favours **high-Z** | — | **unresolved** | **OBSERVED-CONTESTED** | Asplund et al. 2009, *ARA&A* 47:481; Grevesse & Sauval 1998, *Space Sci Rev* 85:161; Borexino Collaboration 2023, *Phys Rev D* 108:102005 (high-Z agreement); arXiv:2501.09971 | An SSM reconciling AGSS09 abundances with 0.1% sound speed *and* the neutrino fluxes |
| `Ṗ_b,obs/Ṗ_b,GR` | **0.9983 ± 0.0016** | dimensionless | PSR B1913+16; 9,257 TOAs over 35 yr | OBSERVED-REPLICATED | Weisberg & Huang 2016, *ApJ* 829:55, doi:10.3847/0004-637X/829/1/55 | A ratio outside the interval on longer baselines |
| `M_psr` / `M_comp` | 1.438 ± 0.001 / 1.390 ± 0.001 | M☉ | PSR B1913+16 | OBSERVED-REPLICATED | Weisberg & Huang 2016 | As above |
| `d`(B1913+16) | **4.1 (+2.0 / −0.7)** | kpc | VLBI annual geometric parallax, `π = 0.24 (+0.06 / −0.08)` mas. Weisberg & Huang 2016 instead assumed `9.8 ± 3.1` kpc (dispersion-measure based) for the galactic-acceleration correction; the distance is the **dominant systematic** on the 0.9983 ratio | OBSERVED-SINGLE | Deller et al. 2018, *ApJ* 862:139, doi:10.3847/1538-4357/aacf95 | An independent parallax outside the interval |
| `L_Edd` | **1.26 × 10³¹ (M/M☉)** ≈ 3.3 × 10⁴ (M/M☉) L☉ | W | `4πGMm_p c/σ_T`; spherical, steady, ionised H, Thomson opacity only | MODELED | Eddington 1926, *The Internal Constitution of the Stars*; arithmetic computed here | Arithmetic error; or a *steady spherical* source persistently above it |
| `L☉/L_Edd,☉` | **3.0 × 10⁻⁵** | dimensionless | `3.828 × 10²⁶ / 1.26 × 10³¹` | MODELED | Computed here | Arithmetic error |
| `Y_p` | ~0.245 | mass fraction | primordial helium, BBN/CMB concordance | OBSERVED-REPLICATED *(standard reference; not primary-sourced in this pass)* | BBN/CMB literature | An independent determination outside ~0.24–0.25 |
| Lithium problem | BBN+CMB over-predicts ⁷Li vs metal-poor stars by ~3× | — | primordial ⁷Li — **open** | **OBSERVED-CONTESTED** | BBN literature; Johnson 2019, *Science* 363:474–478 | A resolution (stellar depletion, or new physics) that closes it |

## Falsifier (operable)

This chapter's central structural claim — **that the steep negative main-sequence lifetime exponent (`t ∝ M^(1−α)` with α > 1) is what makes heavy elements available on a timescale short compared to the age of the Galaxy, and is therefore a necessary condition for the cell's atoms to exist** — is refuted by exhibiting **one self-consistent galactic chemical-evolution model in which massive stars have main-sequence lifetimes comparable to the Sun's (~10¹⁰ yr), and which nonetheless reproduces the observed solar Fe/H, C/H and O/H at a formation time of 4.567 Gyr ago in a ~13 Gyr-old Galaxy.** If the enrichment does not require fast-dying massive stars, the causal claim fails and this chapter's spine breaks.

Secondary falsifiers are row-local. Each row in the table carries its own; a refuted row moves that row only. A refuted **α > 1** across the massive-star range, or a refuted **10⁶–10⁷ yr** lifetime for a 30 M☉ star, moves the chapter.

Two falsifiers for the method sections, printed separately because they are the transferable content. **The control-loop reading** is refuted by exhibiting a star with a *non-degenerate, ideal-gas* core in which a temperature perturbation produces **no** restoring pressure response — the feedback path absent where the equation of state says it should be present. **The hidden-state-inference reading** is refuted by showing that helioseismic inversion, seismic tomography, and pulsar timing are *not* the same inference — that at least one recovers interior structure without holding a generative model and inverting a surface observable.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **"Hoyle predicted the carbon-12 resonance because carbon-based life exists" (the anthropic origin story).** — **INADMISSIBLE as history.** **Receipt:** Kragh (2010), *Archive for History of Exact Sciences* 64:721–751, doi:10.1007/s00407-010-0068-8, documents that Hoyle and his contemporaries did not associate the level with life; the anthropic reading was applied retrospectively in the 1980s. The correct account — prediction from the **observed cosmic carbon abundance** — is *stronger*, because an abundance is a measurement and "we exist" predicts no number. Recorded because this is the most-repeated version of the best story in this chapter, and it is wrong.
- **"GW170817 measured where gold comes from."** — **NEGATIVE.** **Receipt:** Gillanders et al. (2021), *MNRAS* 506(3):3560–3577, searched AT2017gfo for exactly this and found **no prominent Pt or Au signatures**, reporting only upper limits (Au ≲ 10⁻² M☉). What was identified is **strontium** (Watson et al. 2019, *Nature* 574:497–500). Gold's merger origin is an **inference from the r-process abundance pattern**, not a detection. Recorded against this chapter's own commissioning brief, which contained the error.
- **"L ∝ M^3.5 is the mass–luminosity relation."** — **NEGATIVE.** **Receipt:** Eker et al. (2018), *MNRAS* 479:5491–5511, Table 4: six calibrated pieces over 0.179–31 M☉ with exponents 2.028, 4.572, 5.743, 4.329, 3.967, 2.865. **None is 3.5**, and the sequence is non-monotonic. Usable as an order-of-magnitude device; inadmissible as a measurement.
- **"⁵⁶Fe is the most tightly bound nucleus."** — **NEGATIVE** as stated. **Receipt:** ⁶²Ni has the highest binding energy per nucleon (8.7945 vs 8.7903 MeV/nucleon). ⁵⁶Fe has the lowest *mass per nucleon* — a different quantity. True of one quantity, false of the other; stating it without naming the quantity is the defect.
- **The Jeans swindle.** — **INADMISSIBLE as a rigorous derivation**, while remaining in use as a working criterion. The linearisation is about a uniform static self-gravitating background that is not a solution of the governing equations. Named and used, not hidden.
- **"Stellar `L ∝ M^α` and Kleiber's `B ∝ M^(3/4)` reveal a shared scaling principle."** — **INADMISSIBLE as stated.** Unfalsifiable in that form (no observation would refute a "shared principle"), and the two are *opposite in sign of `α − 1`* — sublinear versus superlinear — with no shared mechanism. Power laws are the generic output of scale-free constraints. Recorded as a **rhyme**; the temptation is real and the refusal is the method.
- **NOT-MEASURED / NOT-SOURCED in this pass:** the total r-process ejecta mass of AT2017gfo; primary sources for the reaction-rate temperature exponents (ν_pp, ν_CNO, ν_3α), the ⁸Be and ⁵⁶Ni/⁵⁶Co half-lives, `Y_p`, and the solar main-sequence lifetime — all standard reference values, flagged in the table, **printed only with that flag attached**. Closure: fetch the primary nuclear-data and stellar-evolution references and replace the flag with a citation.
- **OPEN, not resolved:** the primordial lithium problem; the r-process dominance budget; the solar abundance problem — printed as contested rather than adjudicated, because this chapter cannot adjudicate them.

## HONEST FENCE — MODELED

This chapter is fenced **MODELED**. Individual rows carry their own classes — many OBSERVED-REPLICATED (the Hoyle state energy, the Borexino CNO flux, the Eker exponents, the Weisberg–Huang ratio, the Sr II identification), several OBSERVED-CONTESTED (the iron budget, the r-process dominance, the solar abundance problem, the lithium problem), several NOT-MEASURED. But the *chapter as an artifact* is a **provenance model**: it composes measured constants through stated assumptions — spherical symmetry, the ideal-gas equation of state, `t ∝ M/L` at fixed burned-fuel fraction, solar-neighbourhood chemical evolution as a proxy for "where your atoms came from" — to reach a supply chain. **The assumptions are the fence.** The `t ∝ M/L` step is crude in a way the text prints rather than hides: two defensible exponents give answers differing by a factor of nine, and only the *order* survives.

Per **Gould & Lewontin (1979), "The Spandrels of San Marco and the Panglossian Paradigm"**: nothing above establishes that any stellar or nuclear parameter is an optimum, or that the universe is arranged for carbon. The Hoyle state is where it is; the observed carbon abundance is the evidence that it is there; **the inference runs abundance → resonance, and it does not run backwards into purpose.** Reading fine-tuning out of the Hoyle state is the astrophysical form of the adaptationist error — inferring that because a structure is functional, it was *for* something. Nature's authority here is precise and narrow: **it already ran the experiment, at scales and durations no laboratory can reach, and the failures are simply absent from the sky.** That makes the surviving population evidence of a constraint-optimum and every number above a **hypothesis generator** — not a proof. Per repo rule **M7**, any design taken from this chapter must still beat a **tuned conventional baseline** on a **pre-registered metric** with a load-bearing discriminator, or it is recorded **NEGATIVE**.

## Not claimed

- **Not claimed:** that the universe is fine-tuned, designed, or arranged for life, or that the Hoyle state is evidence of any of these. The prediction ran from a measured abundance to a nuclear energy level. The anthropic gloss is recorded INADMISSIBLE as history (Kragh 2010); the fine-tuning inference is a separate metaphysical claim carried nowhere in this chapter.
- **Not claimed:** that gold's origin has been measured. An r-process was identified in a neutron-star merger *via strontium*; gold is inferred from the abundance pattern. **Au was searched for in AT2017gfo and not found** (Gillanders et al. 2021). Three links, one of them theory — stated wherever gold appears.
- **Not claimed:** that neutron-star mergers are the dominant r-process site. Identified as *a* site; the galactic budget is printed as contested.
- **Not claimed:** that the stellar mass–luminosity relation and biological allometry share a mechanism, a principle, or anything but a functional form. **A rhyme, flagged as a rhyme**, with four printed reasons the unification fails — including that the exponents run in opposite directions about 1.
- **Not claimed:** that a star is alive, self-organising beyond negative feedback, or a model for mind. The control-loop reading is a statement about `P ∝ ρT` closing a loop — engineering vocabulary applied to a physical referent, not a claim about agency, cognition, or experience. NA-04's blanket structure does not apply to a star, and this chapter draws no such blanket.
- **Not claimed:** that the standard solar model is correct. It agrees with helioseismic sound speed to 0.10% rms and **currently fails** to reconcile the best spectroscopic abundances with that agreement. The residual is printed as the live problem it is.
- **Not claimed:** that the provenance table is complete or its site splits settled. The C and N splits are model-dependent; the Fe split spans 50–70%; the lithium row is an open problem.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** Reading Eker et al. 2018 does not make any UNI claim proven, designed, or built. The NATURA twelve-value class (OBSERVED-REPLICATED / OBSERVED-SINGLE / OBSERVED-CONTESTED / MODELED / MODELED-CONTESTED / HYPOTHESIZED / INADMISSIBLE / SUPERSEDED / NOT-MEASURED / NOT-SOURCED / NOT-CONFIRMED / NOT-LOCATED — six of them registered by NA-00 amendment 2026-07-15-A) and the UNI four-value fence (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. This chapter contains **zero** UNI claims.
- **QUAESTIO-APERTA:** "full human" and "beyond human" appear nowhere in this chapter as a target, milestone, or deliverable. They are permanent open questions. Stellar nucleosynthesis has no bearing on them.


<!-- ===== END cookbook/recipes-natura/CN-04-stars.md ===== -->

