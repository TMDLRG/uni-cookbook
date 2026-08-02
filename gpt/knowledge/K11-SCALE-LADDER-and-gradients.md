# The scale ladder — quark to galaxy, and the gradients between

> **Knowledge file `K11-SCALE-LADDER-and-gradients.md`** of the UNI Encyclopedia & Cookbook GPT pack.
> This file is a BUILD ARTIFACT: it merges **1** source file(s) from the
> repository `TMDLRG/UNI-Encyclopedia-Cookbook`, byte-for-byte, in the order listed below.
> The repository is the single source of truth; if this file and the repository ever
> disagree, the repository wins and this file is stale.
>
> SOVEREIGNTY RULE (binding, do not merge the two ledgers): this corpus carries TWO sovereign evidence vocabularies. The UNI 4-value fence (proven / designed / hypothesized / not-yet-built) describes ONLY UNI's own build status and is governed by encyclopedia/CLAIM-LEDGER.md. The NATURA 12-value class, in three groups, describes ONLY nature's observed regularities and is governed by encyclopedia/NATURE-LEDGER.md: group A / measured = OBSERVED-REPLICATED, OBSERVED-SINGLE, OBSERVED-CONTESTED; group B / derived = MODELED, MODELED-CONTESTED, HYPOTHESIZED; group C / fenced = INADMISSIBLE, SUPERSEDED, NOT-MEASURED, NOT-SOURCED, NOT-CONFIRMED, NOT-LOCATED. Six of the twelve were registered by NA-00 amendment 2026-07-15-A after the corpus refuted the original 'six classes and only six' at 72 of 919 ledger rows; twelve is a MEASURED property of the corpus, not a design target. NEVER read NOT-SOURCED as NOT-MEASURED: the first says we could not trace the source (a fact about us), the second says nobody has measured it (a claim about the frontier of science). A nature citation is NEVER a UNI gate. Cross-reference between them by explicit link only, never by merge.


**Source files merged into this knowledge file, in order:**

- `encyclopedia/wing-NATURA/NA-10-the-scale-ladder-and-gradients.md`

---



<!-- ===== BEGIN encyclopedia/wing-NATURA/NA-10-the-scale-ladder-and-gradients.md ===== -->

# NA-10 — The scale ladder: quark to galaxy, and the gradients between

> **What you are reading.** The wing's spine. A rung-by-rung placement table across ~36 orders of magnitude in length, and — the actual payload — the rule for knowing when a number you fitted on one rung stops meaning anything on the next. Every value below carries a source, or is written **NOT-MEASURED** (no measurand exists) or **NOT-SOURCED in this pass** (a measurand exists; this pass did not fetch the primary). There is no fourth state — a plausible number with silent provenance is exactly the defect this chapter exists to catch — and where a re-read found one standing in the ladder table, it is named in the NOT-SOURCED rows below rather than left silent. Nothing here raises any UNI rung; a nature citation is never a UNI gate.

---

## The span, and what it is not

From the proton's rms charge radius, **8.4075(64) × 10⁻¹⁶ m** (CODATA 2022, NIST), to the Milky Way's D25 isophotal diameter, **26.8 ± 1.1 kpc ≈ 8.3 × 10²⁰ m** (attributed to Goodwin et al. 1997/98, *The Observatory* 118:201–208, via secondary summary — see the open row), is a factor of ~**10³⁶**.

The ladder is *not* a continuum with things sprinkled along it. It is a set of **regimes separated by boundaries**, and the whole engineering value of the chapter is in the boundaries. Inside a regime, one force dominates, one or two dimensionless groups govern, and fitted power laws behave. Across a boundary, the dominant force changes identity and every fitted exponent you carried across is a category error wearing a decimal point.

## The ladder

`L` = characteristic length. `t` = a characteristic time *of that rung's own dynamics* (see the honesty note on the time gradient below — these are **not one measurand**). Blanket = is a Markov blanket identifiable (cross-ref **NA-04**, mind/body/world)?

| # | Rung | `L` (m) | Characteristic `t` (s) | Characteristic energy | Dominant force / constraint | Governing group(s) | Blanket? |
|---|---|---|---|---|---|---|---|
| 1 | Quark / nucleon | ~8.4 × 10⁻¹⁶ | ~3 × 10⁻²⁴ (`r_p/c`, computed) | ~8.8 MeV per nucleon (binding, peak at Fe/Ni) | **Strong (colour + residual)** | `α_s(m_Z) = 0.1180 ± 0.0009` (PDG) — runs to O(1) at ~1 GeV | **No** |
| 2 | Atom | `a₀` = 5.29177210544(82) × 10⁻¹¹ (CODATA 2022) | ~1.5 × 10⁻¹⁶ (Bohr orbital period, computed) | 13.6 eV (H ionization) | **Electromagnetic** | `α⁻¹` = 137.035999177(21) (CODATA 2022) | **No** |
| 3 | Molecule | ~1.5 × 10⁻¹⁰ (C–C bond) | ~1.1 × 10⁻¹⁴ (C–H stretch ~3000 cm⁻¹, computed) | ~348 kJ/mol (C–C) | EM / covalent | `E_bond/RT ≈ 140` at 300 K (computed) | **No** |
| 4 | Macromolecule | ~5 × 10⁻⁹ (protein) | 10⁻⁶–10⁰ (folding) | ΔG_fold ~20–63 kJ/mol net | EM + hydrophobic effect + conformational entropy | `ΔG_fold/k_BT` ~8–25 | **No** |
| 5 | Assembly (ribosome, capsid, nucleosome) | 2 × 10⁻⁸ – 10⁻⁷ | ~5 × 10⁻² per residue (~20 aa/s, NA-08) | 4 ATP / peptide bond (NA-08) | EM / self-assembly | `ΔG_bind/k_BT` | Marginal |
| 6 | Organelle | 5 × 10⁻⁷ – 10⁻⁶ (mitochondrion) | NOT-MEASURED as a single quantity | ΔΨm; ATP flux | EM + **membrane** | `S/V`, `Pe` | **Yes** — double membrane, own genome, own fission |
| 7 | **Cell** | 10⁻⁶ – 10⁻⁴ | ~1.2 × 10³ (*E. coli* division, rich medium) | ~10⁷ ATP/s; ~10⁻¹² W (NA-08) | **Viscosity + diffusion** | `Re ≈ 6 × 10⁻⁵`, `Pe ≈ 0.06–0.1`, `S/V = 3/R` (NA-08) | **Yes** — plasma membrane. The canonical case |
| 8 | Tissue | 10⁻⁴ – 10⁻² | 10⁰ – 10⁵ | O₂ flux-limited | Diffusion + convection + mechanics | `Pe`, `Da`, Thiele modulus; O₂ penetration ~100–200 µm | Marginal / contested |
| 9 | Organ | 10⁻² – 10⁻¹ | ~1 (heartbeat) | Regional metabolic rate | **Bulk transport + mechanics** | `Re` (aorta ~10³–4×10³); Womersley `α` ~20 (human aorta, rest) | Marginal |
| 10 | **Organism** | 10⁻³ – 3 × 10¹ | 10⁻¹ – 10⁹ (beat → lifespan) | BMR ∝ `M^b` | Inertia; **gravity enters** | `Re` 10⁻⁵ → 3 × 10⁸; `Fr`; `St` 0.2–0.4 cruise; Kleiber `b` | **Yes** |
| 11 | Colony / society | 10⁻¹ – 10⁴ | 10⁶ – 10⁹ | Colony energy budget | **No new physical force** — informational/behavioural coupling | NOT-MEASURED (no agreed group) | **Contested** (superorganism debate) |
| 12 | Ecosystem | 10³ – 10⁷ | 10⁸ – 10¹¹ (succession) | NPP (W/m²) | Energy flux + trophic structure | Trophic transfer efficiency (~10% nominal; measured spread wide) | **No** |
| 13 | Planet | 6.3781 × 10⁶ (IAU nominal terrestrial equatorial radius) | 8.6164 × 10⁴ (sidereal day); 3.156 × 10⁷ (orbit) | 1361 W/m² (IAU nominal TSI) | **Gravity + radiative EM** | `Ra`, `Ro`, `Ek` | **No** |
| 14 | Star | 6.957 × 10⁸ (IAU nominal solar radius) | ~10¹⁰ yr (nuclear, Sun) | 3.828 × 10²⁶ W (IAU nominal luminosity) | **Gravity vs radiation/gas pressure** | Eddington ratio | **No** |
| 15 | Stellar system | 1 AU = 1.495978707 × 10¹¹ (IAU, exact); heliopause ~120 AU | 3.156 × 10⁷ (1 yr) | GM⊙ = 1.3271244 × 10²⁰ m³/s² (IAU nominal) | **Gravity (Keplerian)** | Kepler's third law; eccentricity | **No** |
| 16 | Galaxy | ~8.3 × 10²⁰ (D25 26.8 kpc) | ~7 × 10¹⁵ (galactic year, ~225–250 Myr) | NOT-MEASURED here | **Gravity + dark-matter halo** | Flat rotation curve; `M/L`; Toomre `Q` | **No** |

Read the "Blanket?" column downward. It is not monotone. **Blankets appear at rungs 6, 7, 10 and vanish above and below.** A galaxy is enormous and has no blanket. A mitochondrion is a micron across and has one. Size is not what makes a boundary.

## What a rung actually is — emergence, stated operably

A new rung exists when **all three** hold. State them or you have not identified a level, you have merely named a size.

**(a) A boundary with real conditional independence forms.** Internal states are screened from external states by the boundary — this is the Markov-blanket condition (cross-ref NA-04). It is a *factorization* claim about the dynamics, and it is checkable. Not "there is a surface"; "the inside is conditionally independent of the outside given the boundary".

**(b) A new characteristic timescale separates from the level below.** This is the actual mechanism of hierarchy, and it is **Simon (1962)**, "The Architecture of Complexity", *Proc. Am. Philos. Soc.* 106(6):467–482: near-decomposability means intra-component linkages are stronger than inter-component linkages, which has the effect of separating the **high-frequency dynamics** of the hierarchy — the internal structure of the components — from the **low-frequency dynamics** — the interaction among components. Timescale separation is not a description of hierarchy; it is what *makes* one. Simon's watchmaker parable supplies the evolutionary half: the watchmaker who builds stable ten-part subassemblies loses only the last subassembly when interrupted, and so his expected work loss is smaller by orders of magnitude. **Hierarchies are what evolution can reach, because stable intermediates are what interruption spares.**

**(c) The level has its own dynamics that do not require tracking the level below.** This is **Anderson (1972)**, "More Is Different", *Science* 177(4047):393–396, DOI 10.1126/science.177.4047.393, rejecting the "constructionist hypothesis": the ability to reduce everything to simple fundamental laws does not imply the ability to start from those laws and reconstruct the universe. Anderson's claim is not mystical and does not need to be. It is that broken symmetry at each level generates concepts (rigidity, a phase, a species) that are not present in the level below.

Note the honest ordering: (b) *causes* (c). If the timescales did not separate, you would have to track the fast level and there would be no autonomous slow dynamics to write down. Emergence here is a statement about **spectral gaps in a dynamical system**, not about magic.

## The best regime-change example there is: Reynolds number and the death of the scallop theorem

`Re = ρvL/µ = vL/ν` — the ratio of inertial to viscous forces. `ν_water ≈ 1.0 × 10⁻⁶ m²/s` at 20 °C.

Vogel's table of self-propelled organisms (*Life in Moving Fluids: The Physical Biology of Flow*, Princeton UP) runs from a **bacterium at Re ≈ 10⁻⁵** (0.01 mm/s) to a **large whale at Re ≈ 3 × 10⁸** (10 m/s), with a sea-urchin sperm at ~0.03 and a tuna at ~3 × 10⁷ in between. Check the endpoints independently: whale, `v = 10 m/s`, `L = 30 m` → `Re = 3 × 10⁸` ✓. *E. coli*, `v ≈ 3 × 10⁻⁵ m/s`, `L = 2 × 10⁻⁶ m` → `Re ≈ 6 × 10⁻⁵` ✓ (NA-08).

**That is a span of ~10¹³, not ~10¹⁰.** The ~10¹⁰ figure in circulation is short by about three orders of magnitude; the sourced span is ~13 orders. Corrected here rather than carried.

And the physics of swimming **changes identity** across it, not degree.

At `Re ≈ 10⁻⁵`, inertia does not exist. Compute the coasting distance for a 1 µm sphere when propulsion stops: Stokes drag gives a decay time `τ = 2ρa²/(9µ)` = `2(10³)(10⁻¹²)/(9 × 10⁻³)` = **2.2 × 10⁻⁷ s**, so the coast is `d = vτ` = `3 × 10⁻⁵ × 2.2 × 10⁻⁷` = **6.7 × 10⁻¹² m = 0.067 Å** — about **1/16 of a hydrogen atom's diameter** (`2a₀` = 1.06 Å). Order-of-magnitude consistent with Purcell's own back-of-envelope in **Purcell (1977)**, *Am. J. Phys.* 45(1):3–11, DOI 10.1119/1.10903. A bacterium cannot coast. There is no "let go and glide". Stop pushing and you have already stopped.

Hence Purcell's **scallop theorem**: a low-Re swimmer executing a *reciprocal* stroke — a shape sequence identical when reversed — nets **zero** displacement in an incompressible Newtonian fluid, because Stokes flow is time-reversible. Purcell's phrasing: it "exactly retraces its trajectory, and it's back where it started" (Purcell 1977). A real scallop, at `Re ~10⁴–10⁵`, swims perfectly well by clapping. Shrink it to a micron and the identical stroke transports it **nowhere, forever**. Nothing about the animal changed. The dominant term in the Navier–Stokes equation did.

**And the theorem is premise-bound, which is the second half of the lesson.** Qiu et al. (2014), "Swimming by reciprocal motion at low Reynolds number", *Nature Communications* 5:5119, DOI 10.1038/ncomms6119, built a single-hinge "micro-scallop" that **does** propel by reciprocal motion at `Re = 1.4 × 10⁻⁴ – 3 × 10⁻³` — in shear-thickening and shear-thinning **non-Newtonian** fluids, with a Newtonian glycerol control. The theorem was not refuted; its premise ("Newtonian") was withdrawn. **A law fitted inside a regime is a law about that regime's premises.** Change a premise and you are on a different rung of a different ladder.

## The other regime change: quarter-power holds inside a regime, and breaks at the boundary

Kleiber's `B ∝ M^(3/4)` is the wing's most-quoted ratio, and it is the wing's best worked example of a regime-bounded law.

**Boundary evidence.** DeLong, Okie, Moses, Sibly & Brown (2010), "Shifts in metabolic scaling, production, and efficiency across major evolutionary transitions of life", *PNAS* 107(29):12941–12945, DOI 10.1073/pnas.1007783107, fitted metabolic rate against body mass across ~16 orders of magnitude in size, split at the taxonomic boundaries:

| Group | Active-state exponent | Inactive-state exponent | n (active / inactive) |
|---|---|---|---|
| Prokaryotes | **1.7** (superlinear) | 2.0 | 44 / 121 |
| Protists | **1.0** (linear) | 1.1 | 51 / 52 |
| Metazoans | **0.76** (sublinear) | 0.79 | 71 / 15 |

Their conclusion, in their own framing: Kleiber's 3/4-power law **does not apply universally across organisms**. The exponent does not drift — it *changes sign of curvature relative to linear*, from superlinear to linear to sublinear, and it does so **exactly at the major evolutionary transitions**. That is not noise. That is a rung boundary showing up in the residuals.

**Curvature evidence, inside the metazoan regime.** Kolokotrones, Van Savage, Deeds & Fontana (2010), "Curvature in metabolic scaling", *Nature* 464:753–756, DOI 10.1038/nature08920: the mass–metabolic-rate relation has **convex curvature on a logarithmic scale and is therefore not a pure power law at all**, even after accounting for body temperature; it needs a quadratic term in log-mass, which breaks the scale invariance a power law asserts. The payoff is diagnostic: attempts to fit a straight line to what is really a curve produce "scaling exponents" that depend on which data you used — **data sets dominated by small mammals tend to yield ~2/3, data sets dominated by large mammals tend to yield ~3/4**. The decades-long 2/3-vs-3/4 argument was, on this account, two groups fitting straight lines to different arcs of one curve and each reporting their arc's slope as a universal constant.

*Fence: Kolokotrones et al. is contested, and the exchange has **two published turns** — carry both. MacKay (2011), "Mass scale and curvature in metabolic scaling", *J. Theor. Biol.* 280(1):194–196, is a published comment against it; **Deeds, Savage & Fontana (2011)**, "Curvature in metabolic scaling: a reply to MacKay", *J. Theor. Biol.* 280(1):197–198, DOI 10.1016/j.jtbi.2011.03.036, is a published reply by three of the four original authors, in the same issue immediately following the comment. The curvature claim is carried as **OBSERVED-CONTESTED** — live on both sides, settled by neither. Citing the comment without the reply would be a one-sided rendering of a dispute this chapter's own method requires it to carry whole.*

## The regime-change rule (the operable output)

> **A power law fitted within a regime does not extrapolate through a regime boundary.** Not "less accurately". It does not carry, and its exponent stops being a fact about the world.

Detection procedure. Run all five before extrapolating a fitted exponent across any decade you did not measure:

1. **Did the dominant dimensionless group move by orders of magnitude across the span?** (`Re`: ~13 orders, bacterium → whale.) If yes, suspect a boundary.
2. **Did the dominant force change identity?** (Viscosity → inertia. Diffusion → convection. EM → gravity.) A change of *dominant term*, not of coefficient, is a boundary.
3. **Does the log-log plot have curvature?** Fit a quadratic in log-mass and test the quadratic coefficient against zero (Kolokotrones et al. 2010). Curvature is a power law's own confession.
4. **Does the fitted exponent depend on which subset of the data you fit?** If small-dominated and large-dominated subsets give different slopes, you have a curve, not a law (Kolokotrones et al. 2010: 2/3 vs 3/4).
5. **Is there an independent structural boundary at the suspected break?** (DeLong et al. 2010: prokaryote → protist → metazoan.) An independently-motivated break is worth far more than a break found by searching for one — a break located *only* by scanning residuals is a **fitted artefact until pre-registered**. Per **M2**, the verdict is the CI bound excluding the threshold, never the point estimate.

## The gradients: which are measured, which are rhetorical

This section is the chapter's honesty fence. The ladder invites gradient talk, and most gradient talk is unearned.

**MEASURED, real, comparable across rungs:**

- **Length.** ~10³⁶ — and it is the one column whose endpoints are commensurable to within a factor of ~2, which is nothing across 36 orders. It is still **not literally one measurand**, and this chapter does not get to make the claim it refuses `t`: rungs 1/2/13/14 are **radii**, rung 16 is a **photometric isophotal diameter** (D25 — the isophote where B-band surface brightness falls to 25 mag/arcsec², a brightness convention rather than a geometric extent), and rungs 4–12 are **ranges**. The ladder's top rung is therefore measured by a different *kind* of instrument than its bottom rung. **The span is real; the uniformity is approximate.** Unlike `t`, the heterogeneity does not change the physical question being asked — a factor of ~2 and a radius-vs-diameter convention do not move a 10³⁶ conclusion — which is why `L` stays MEASURED and `t` does not.
- **Specific power (W/kg).** The same measurand at every rung, and it is worth stating because it runs the *opposite* way to intuition. **Both endpoints are conversions, and both are labelled so.** An *E. coli* runs at **~10³ W/kg** — computed, not measured: BNID 109687 is an **O₂ uptake rate** (30 mmol O₂/gDW/h, *E. coli* strain C-3000, glucose minimal medium), turned into W/kg through the enthalpy of O₂ consumption and a cell mass. It is not a W/kg observation. The Sun runs at `L⊙/M⊙` = `3.828 × 10²⁶ W / 1.988 × 10³⁰ kg` = **1.9 × 10⁻⁴ W/kg** (computed from IAU 2015 nominal values). **A bacterium outputs roughly 5 million times more power per kilogram than the Sun does.** The ratio is **MODELED ÷ MODELED** — the same arithmetic on both sides, so the same class on both sides, which is the point: dividing a sourced luminosity by a sourced mass and dividing a sourced O₂ rate by a sourced mass cannot be two different classes in one comparison. The conclusion survives the one open scope question in the chain (dry- vs wet-mass basis, worth ~4× — see the row), because the result is a factor of ~10⁶ and the ambiguity is a factor of ~4. It demolishes any "energy density rises with scale" narrative with room to spare.
- **Reynolds number** — but *only within the self-propelled-body domain*, rungs 7–10. It is not defined for an atom or a galaxy.

**PART-MEASURED, PART-RHETORICAL:**

- **Time.** Each rung's `t` is measured. But `r_p/c`, a C–H stretch period, a cell division time, and the Sun's nuclear lifetime are **not one measurand** — they are a light-crossing time, a vibrational period, a doubling time, and a fuel-exhaustion time. The endpoints are real; the *gradient* is an artefact of putting four different physical questions in one column. Column `t` above is a placement aid, **not a scaling relation**, and must never be regressed.

**RHETORICAL — NOT-MEASURED, and the fence is here:**

- **"Information density."** No agreed measurand exists spanning quark to galaxy. Genome information content is measurable *at one rung*; there is no bits-per-m³ figure comparable between a nucleon and a galaxy. **NOT-MEASURED.** Falsifier: state the measurand, state the units, measure two rungs with it.
- **"Degree of internal model."** No measurand. No units. No instrument. This is the gradient the ladder most *invites* and it is the one with the least behind it. Recorded **NOT-MEASURED**, not softened. Whatever a variational scheme is doing at rung 7, no one has published a scalar that orders rungs 1–16 by "modelledness". Writing the ladder as an ascent toward mind is a **rhetorical move dressed as a measurement**, and it is exactly the kind of move this wing exists to catch.
- **"Complexity."** Same verdict. Simon (1962) gives a *structural* criterion (near-decomposability) that is checkable per system; it does not yield a scalar that monotonically increases with size.

## Major transitions as rung-crossings

Maynard Smith & Szathmáry (1995), *The Major Transitions in Evolution*, Oxford University Press, ISBN 978-0-19-850294-4 (and Szathmáry & Maynard Smith 1995, *Nature* 374(6519):227–232, DOI 10.1038/374227a0) list eight:

1. Replicating molecules → populations of molecules in compartments
2. Independent replicators (RNA) → chromosomes
3. RNA as gene *and* enzyme → DNA genes; protein enzymes
4. Prokaryotes → eukaryotes
5. Asexual clones → sexual populations
6. Protists → multicellular organisms
7. Solitary individuals → colonies with non-reproductive castes
8. Primate societies → human societies with language

Several of these are **rung-crossings in exactly the sense above**: entities that previously replicated independently became bounded inside a new blanket with its own slower dynamics. Transition 1 builds the rung-7 blanket. Transition 4 builds rung 6 (the mitochondrion's blanket is a *former* rung-7 blanket demoted to an organelle's). Transition 6 builds rungs 8–10. And DeLong et al. (2010) is the receipt that these are *physically* real boundaries and not just a taxonomist's convenience: the metabolic exponent changes at them.

**The framework is influential and it is debated — carry both.** West, Fisher, Gardner & Kiers (2015), "Major evolutionary transitions in individuality", *PNAS* 112(33):10112–10119, DOI 10.1073/pnas.1421402112, break transitions into two steps (group formation; transformation into an integrated entity) and argue explicitly toward "a simpler and more unified description" — the framing itself implying the original list offered a mixture of explanations rather than one. A recurring criticism holds that the list lacks theoretical unity, and that transition 8 (language) does not meet the criterion of previously free-living entities becoming integrated into a higher-level individual. **This criticism is recorded here from secondary summary; the primary sources for the theoretical-unity objection were NOT located in this pass** — see the open row. Do not cite the objection to a specific author on this chapter's authority.

## Place any object on the ladder — the 5-step procedure

1. **Measure `L`.** Take the characteristic length — the shortest dimension that carries the relevant flux, not the longest dimension you can find. (NA-08: *Thiomargarita* is 750 µm wide and its `L` is 1–2 µm, because the cytoplasm is a shell. Getting `L` wrong puts the object on the wrong rung and every later step inherits the error.)
2. **Name the dominant force.** Strong / EM / viscous / inertial / gravitational. If two contend, you are **at a boundary** — say so and stop extrapolating, do not average.
3. **Compute the governing dimensionless group(s)** from the table's column for that rung. `Re` and `Pe` at rungs 7–10; `α` at rung 2; `α_s` at rung 1; `Ra`/`Ro` at rung 13. The group, not the size, tells you which physics is running.
4. **Test for a blanket.** Can you state what is inside, what *is* the boundary, and what is outside — with conditional independence, not just a visible surface? Yes → it is an entity at that rung. No → it is a **region**, not a system (NA-08's rule; NA-04's typing). Rungs 12–16 fail this test and that is fine; galaxies do not need blankets.
5. **Check the regime before importing any ratio.** Run the five-test procedure above against every fitted exponent you were about to carry in. If any of the five fires, the ratio does not cross — record it NOT-APPLICABLE at the new rung rather than extrapolating. Then, per **M7**: any design taken from this placement must still beat a **tuned** baseline on a **pre-registered** metric with a discriminator that collapses the gain, or it is recorded **NEGATIVE**.

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `r_p` | 8.4075(64) × 10⁻¹⁶ | m | proton rms charge radius | OBSERVED-REPLICATED | CODATA 2022 (NIST, `physics.nist.gov/cgi-bin/cuu/Value?rp`) | Next CODATA adjustment moves it beyond stated `u` |
| `t_strong` | ~2.8 × 10⁻²⁴ | s | `r_p/c` — light-crossing time of a nucleon | MODELED | Computed here from `r_p` (CODATA 2022) and `c` | Arithmetic error; or a claim this is a *measured* interaction time (it is not) |
| `α_s(m_Z)` | 0.1180 ± 0.0009 | dimensionless | strong coupling at the Z mass; runs to O(1) at ~1 GeV | OBSERVED-REPLICATED | PDG world average (recent editions give 0.1179–0.1180 ± 0.0009) | A PDG edition outside 0.117–0.119 |
| `a₀` | 5.291 772 105 44(82) × 10⁻¹¹ | m | Bohr radius | OBSERVED-REPLICATED | CODATA 2022 (NIST, `Value?bohrrada0`) | Next CODATA adjustment beyond stated `u` |
| `α⁻¹` | 137.035 999 177(21) | dimensionless | fine-structure constant; `α` = 7.297 352 5643(11) × 10⁻³ | OBSERVED-REPLICATED | CODATA 2022 (NIST, `Value?alph`) | As above |
| `T_Bohr` | ~1.5 × 10⁻¹⁶ | s | `2πa₀/(αc)`, H ground state | MODELED | Computed here from CODATA 2022 `a₀`, `α`, `c` | Arithmetic error |
| `E_ion,H` | 13.6 | eV | hydrogen ionization | OBSERVED-REPLICATED *(standard reference; primary not read in this pass)* | standard atomic physics (NIST ASD) | Fetch NIST ASD; a value outside 13.59–13.60 |
| `E_C–C` | ~348 | kJ/mol | C–C bond dissociation enthalpy | OBSERVED-REPLICATED *(standard reference; primary not read in this pass)* | standard thermochemical tables | Fetch a primary table; value outside ~330–360 |
| `E_bond/RT` | ~140 | dimensionless | 348 kJ/mol ÷ `RT` (2.494 kJ/mol at 300 K) | MODELED | Computed here | Arithmetic error |
| `t_vib` | ~1.1 × 10⁻¹⁴ | s | C–H stretch, ~3000 cm⁻¹ | MODELED | Computed here from a standard IR wavenumber | Wavenumber refuted |
| `ΔG_fold` | ~20–63 (5–15 kcal/mol) | kJ/mol | net protein folding stability, typical globular | OBSERVED-REPLICATED *(standard range; primary not sourced in this pass)* | standard protein biophysics | Locate a primary survey; range refuted |
| `ν_water` | ~1.0 × 10⁻⁶ | m²/s | kinematic viscosity, 20 °C | OBSERVED-REPLICATED *(standard reference)* | standard fluid-property tables | Measurement outside ~0.9–1.1 × 10⁻⁶ at 20 °C |
| `Re_bact` | ~10⁻⁵ (Vogel); ~6 × 10⁻⁵ (computed, *E. coli*) | dimensionless | bacterium, 0.01 mm/s (Vogel) vs *E. coli* 30 µm/s | MODELED | Vogel, *Life in Moving Fluids*, Princeton UP *(table via secondary summary — primary not read in this pass)*; NA-08 | Read Vogel's table directly; inputs refuted |
| `Re_whale` | ~3 × 10⁸ | dimensionless | large whale, 10 m/s; check: `vL/ν` = 10 × 30 / 10⁻⁶ = 3 × 10⁸ ✓ | MODELED | Vogel (as above); independently recomputed here | As above |
| `Re` **span** | ~10¹³ (≈13 orders), **not ~10¹⁰** | dimensionless | bacterium → whale | MODELED | Computed here from the two rows above | Show a sourced span of ~10¹⁰; the ~10¹⁰ figure is **corrected here** |
| `τ_coast` | 2.2 × 10⁻⁷ | s | `2ρa²/(9µ)`; a = 1 µm, ρ = 10³ kg/m³, µ = 10⁻³ Pa·s | MODELED | Computed here (Stokes drag) | Arithmetic error; inputs refuted |
| `d_coast` | 6.7 × 10⁻¹² (0.067 Å ≈ 1/16 of `2a₀`) | m | 1 µm sphere at 30 µm/s, propulsion off | MODELED | Computed here; order-of-magnitude consistent with Purcell 1977 | Read Purcell 1977 p.4 and compare; a bacterium observed to coast a measurable distance |
| Scallop theorem | reciprocal stroke → **zero** net displacement | — | low `Re`, **incompressible AND Newtonian** | OBSERVED-REPLICATED (as a theorem + its premises) | Purcell 1977, *Am J Phys* 45(1):3–11, DOI 10.1119/1.10903 | A Newtonian, incompressible, low-`Re` reciprocal swimmer that translates |
| Scallop theorem **premise break** | reciprocal swimming **achieved** at `Re` = 1.4 × 10⁻⁴ – 3 × 10⁻³ | dimensionless | micro-scallop in shear-thickening / shear-thinning **non-Newtonian** fluids; Newtonian glycerol control | OBSERVED-REPLICATED | Qiu et al. 2014, *Nat Commun* 5:5119, DOI 10.1038/ncomms6119 | Failure to replicate in a non-Newtonian fluid |
| `St` | 0.2–0.4 | dimensionless | cruising flight/swimming | OBSERVED-REPLICATED | Taylor, Nudds & Thomas 2003, *Nature* 425:707–711 | Cruise `St` outside range across taxa |
| `b_prokaryote` | **1.7** active / 2.0 inactive | dimensionless | metabolic rate vs body mass; n = 44 / 121 | OBSERVED-REPLICATED | DeLong et al. 2010, *PNAS* 107(29):12941–5, DOI 10.1073/pnas.1007783107 | Refit with independent data; CI covering 0.75 |
| `b_protist` | **1.0** active / 1.1 inactive | dimensionless | n = 51 / 52 | OBSERVED-REPLICATED | DeLong et al. 2010 | As above |
| `b_metazoan` | **0.76** active / 0.79 inactive | dimensionless | n = 71 / 15 | OBSERVED-REPLICATED | DeLong et al. 2010 | As above |
| Kleiber universality | **refuted as universal** | — | 3/4 does not apply across prokaryote/protist/metazoan | OBSERVED-REPLICATED | DeLong et al. 2010 (their explicit conclusion) | A dataset in which one exponent fits all three groups |
| Metabolic **curvature** | convex on log-log; quadratic in log-mass required; not a pure power law | — | mammals, temperature-corrected | **OBSERVED-CONTESTED** | Kolokotrones et al. 2010, *Nature* 464:753–6, DOI 10.1038/nature08920; **contested by** MacKay 2011, *J Theor Biol* 280(1):194–196; **replied to by** Deeds, Savage & Fontana 2011, *J Theor Biol* 280(1):197–198, DOI 10.1016/j.jtbi.2011.03.036 — the exchange is live on both sides | Quadratic coefficient CI covering zero on independent data |
| Exponent-by-subset | small-dominated → **~2/3**; large-dominated → **~3/4** | dimensionless | mammals; artefact of fitting a line to a curve | **OBSERVED-CONTESTED** (with the row above) | Kolokotrones et al. 2010 | Both subsets return the same slope |
| `P/m` *E. coli* | ~10³ (order-of-magnitude; **wet-mass basis** — see falsifier) | W/kg | *E. coli* **strain C-3000**, glucose minimal medium; **a conversion, not a W/kg measurement** | **MODELED** | Computed from BNID 109687 — which is an **O₂ uptake rate**, 30 mmol O₂ / g dry cell weight / h, strain C-3000, minimal medium — via the enthalpy of O₂ consumption (~478 kJ/mol O₂) ÷ a cell mass; chain via NA-08 | Recomputed here: 30 mmol/gDW/h × 478 kJ/mol ÷ 3600 s = **~4 × 10³ W/kg *dry*** ≈ **~1.2 × 10³ W/kg *wet*** at dry/wet ≈ 0.3 — so the stated ~10³ closes on a **wet** basis only. **NA-08's mass basis is NOT-CONFIRMED in this pass**; if dry, this row is ~4 × 10³ and the ratio row rises to ~2 × 10⁷. The ~10⁶ conclusion stands either way. Also: an independent measurement >10× off |
| `L⊙/M⊙` | 1.9 × 10⁻⁴ | W/kg | Sun; `3.828 × 10²⁶ W` ÷ `1.988 × 10³⁰ kg` | MODELED | Computed here from IAU 2015 nominal `L⊙` and `(GM)⊙`/`G` (CODATA 2022) | Arithmetic error |
| `P/m` ratio | ~5 × 10⁶ (bacterium : Sun) | dimensionless | specific power; **MODELED ÷ MODELED** — both endpoints are conversions, neither is a W/kg observation | MODELED | Computed here from the two rows above | Recomputation; ~2 × 10⁷ if the *E. coli* row is dry-basis — the ~10⁶ order survives either way |
| `R⊙` | 6.957 × 10⁸ | m | IAU **nominal** solar radius (exact by adoption, not a CBE) | OBSERVED-REPLICATED (adopted constant) | IAU 2015 Res. B3; Prša et al. 2016, *AJ* 152:41, DOI 10.3847/0004-6256/152/2/41 | IAU re-adoption |
| `L⊙` | 3.828 × 10²⁶ | W | IAU nominal solar luminosity | OBSERVED-REPLICATED (adopted constant) | as above | as above |
| `S⊙` | 1361 | W/m² | IAU nominal total solar irradiance | OBSERVED-REPLICATED (adopted constant) | as above | as above |
| `T_eff,⊙` | 5772 | K | IAU nominal solar effective temperature | OBSERVED-REPLICATED (adopted constant) | as above | as above |
| `(GM)⊙` | 1.3271244 × 10²⁰ | m³/s² | IAU nominal solar mass parameter | OBSERVED-REPLICATED (adopted constant) | as above | as above |
| `R_eE` | 6.3781 × 10⁶ | m | IAU nominal terrestrial equatorial radius (polar: 6.3568 × 10⁶) | OBSERVED-REPLICATED (adopted constant) | as above | as above |
| AU | 1.495 978 707 × 10¹¹ | m | astronomical unit, exact by IAU definition | OBSERVED-REPLICATED (defined) | IAU 2012 Res. B2 *(definition; primary not read in this pass)* | Fetch IAU 2012 Res. B2 |
| `D25_MW` | 26.8 ± 1.1 (≈8.3 × 10²⁰ m) | kpc | Milky Way isophotal diameter | OBSERVED-CONTESTED *(secondary summary; primary not read in this pass)* | attributed to Goodwin et al. 1997/98, *The Observatory* 118:201–208 | Read the primary; an independent estimate outside 25.7–27.9 kpc |
| `R₀` | **8178 ± 13(stat) ± 22(sys)** (≈ 8.178 kpc; 0.16% stat, 0.27% total) | pc | Sun → Galactic Centre; **direct geometric** measurement — S2's orbit via VLTI/GRAVITY interferometry + 27 yr astrometry/spectroscopy | OBSERVED-REPLICATED *(current standard reference)* | GRAVITY Collab. (Abuter et al.) 2019, *A&A* 625:L10, DOI 10.1051/0004-6361/201935656, arXiv:1904.05721 *(primary read in this pass)* | An independent geometric measurement outside ~8.13–8.23 kpc |
| `R₀` — the 2016 standoff *(historical; resolved)* | **8.32 ± 0.07(stat) ± 0.14(sys)** *vs* **7.86 ± 0.14(stat) ± 0.04(sys)** — **~2.2σ** apart on errors combined in quadrature (computed here); intervals do not overlap | kpc | Sgr A* stellar orbits: Gillessen = multistar fit; Boehle = **combined S2+S38** fit. Boehle's **S2-only** fit gives 8.02 ± 0.36 ± 0.04, "completely consistent" with GRAVITY — the offset is the combined fit, not the data | **OBSERVED-CONTESTED → resolved by method** | Gillessen et al. **2017**, *ApJ* 837:30 (arXiv:1611.09144, posted 2016 — hence the common "2016") vs Boehle et al. 2016, *ApJ* 830:17; both values and the S2-only diagnosis quoted in GRAVITY Collab. 2019 *(read in this pass)* | Superseded as a live value by the row above; retained as the worked averaging-trap case. Refuted if the S2-only/combined-fit diagnosis is overturned |
| Ladder span | ~10³⁶ | dimensionless | `r_p` → `D25_MW` | MODELED | Computed here | Arithmetic error |
| "Information density" gradient | — | — | across rungs 1–16 | **NOT-MEASURED** | no measurand located | State the measurand + units; measure two non-adjacent rungs |
| "Degree of internal model" gradient | — | — | across rungs 1–16 | **NOT-MEASURED** | no measurand located | As above. Until then it is rhetoric |
| Trophic transfer efficiency | ~10% nominal; measured spread wide | % | ecosystem energy flux | **NOT-SOURCED in this pass** | not confirmed here | Fetch a primary survey (e.g. Lindeman and successors) |
| O₂ tissue penetration | ~100–200 | µm | why capillary spacing is what it is | **NOT-SOURCED in this pass** | standard physiology, primary not located | Fetch a primary; Krogh-cylinder measurement |
| Womersley `α` (aorta) | ~20 | dimensionless | human aorta, rest | **NOT-SOURCED in this pass** | standard cardiovascular reference | Fetch a primary |
| MTE list | 8 transitions | — | Maynard Smith & Szathmáry | OBSERVED-REPLICATED (as a published framework) | Maynard Smith & Szathmáry 1995, OUP, ISBN 978-0-19-850294-4; Szathmáry & Maynard Smith 1995, *Nature* 374(6519):227–232, DOI 10.1038/374227a0 | — |
| MTE "lacks theoretical unity" objection | — | — | criticism of the list, esp. transition 8 | **NOT-SOURCED in this pass** — recorded from secondary summary only | West et al. 2015, *PNAS* 112(33):10112–9, DOI 10.1073/pnas.1421402112 argues toward "a more unified description" but its abstract does **not** propose excluding transitions | Locate the primary making the theoretical-unity objection; do not attribute it on this chapter's authority |

## Falsifier (operable)

The chapter's central structural claim is the **regime-change rule**: *a power law fitted within a regime does not extrapolate through a regime boundary, where a boundary is marked by a change in the dominant force and an orders-of-magnitude change in the dominant dimensionless group.*

It is refuted by exhibiting **one power law, fitted on data entirely within one regime, that predicts — within its stated CI, on data never used in the fit — observations on the far side of a boundary at which the dominant force demonstrably changed identity.** Concretely: fit `B ∝ M^b` on metazoans alone and predict prokaryote metabolic rates within CI. DeLong et al. (2010) is the standing evidence that this fails (0.76 vs 1.7). A single clean success moves the chapter.

Secondary, row-local falsifiers are in each table row. A refuted row moves that row. A refuted regime-change rule moves the chapter.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **"Re changes by ~10¹⁰ from bacterium to whale."** — **NEGATIVE, corrected here.** The sourced span (Vogel's table, endpoints independently recomputed) is **~10¹³**, ~13 orders, not ~10. Recorded because the wrong figure was carried into this chapter's own brief and would have propagated. The correction does not weaken the point; it strengthens it.
- **"The scale ladder is a ladder of increasing consciousness / awareness / mind."** — **INADMISSIBLE.** No measurand, no units, no instrument, no falsifier. The blanket column above is not monotone in size (rungs 6, 7, 10 have blankets; 12–16 do not), so even the one structurally checkable property does not ascend with scale. Recorded, not mocked: the intuition that the ladder points somewhere is honest and common. It is simply not a measurement, and dressing it as one is the defect.
- **"The Earth/biosphere is an organism" (Gaia, as a literal claim).** — **INADMISSIBLE as stated at rung 13.** It fails criterion (a): no boundary with demonstrated conditional independence is exhibited. Gaia as a *heuristic* about coupled biotic–abiotic feedback names real, measurable couplings and is admissible in that form. The organism claim, as stated, names no falsifier. The two must not travel together.
- **"Emergence means the whole is more than the sum of its parts."** — **INADMISSIBLE as stated.** Unfalsifiable: no observation is specified that could refute it. The **admissible** neighbour is in the body of this chapter and has three checkable conditions (conditional independence; timescale separation; autonomous slow dynamics), each with a test. Anderson (1972) is the earned version; the slogan is the unearned one. The distance between them is the method.
- **NEGATIVE / extrapolation trap:** quoting Kleiber's 3/4 as a law of life. It is a metazoan-regime fit. Prokaryotes are **superlinear at ~1.7** (DeLong et al. 2010). Recorded because the 3/4 exponent is the single most over-extrapolated number in this wing.
- **NEGATIVE / conflation trap:** treating the `t` column of the ladder table as a scaling relation. It is a placement aid built from **four different physical measurands**. Regressing it produces a number about nothing.
- **NEGATIVE / averaging trap — and the method arrived.** In 2016 `R₀` (Sun → Galactic Centre) stood at **8.32 ± 0.07(stat) ± 0.14(sys) kpc** (Gillessen et al. **2017**, *ApJ* 837:30) *or* **7.86 ± 0.14(stat) ± 0.04(sys) kpc** (Boehle et al. 2016, *ApJ* 830:17) — **~2.2σ** apart on errors combined in quadrature (computed here), intervals not overlapping. Averaging them would have manufactured a value no one measured. The row's instruction was *resolve by method*, and the method then resolved it: **GRAVITY Collab. 2019** (*A&A* 625:L10) measured `R₀` **geometrically** — a different instrument, not a re-weighting of the old two — at **8178 ± 13 ± 22 pc** (0.3%), landing near Gillessen, and located where the disagreement came from: Boehle's **S2-only** fit gives 8.02 ± 0.36 ± 0.04 kpc, "completely consistent" with GRAVITY, so the offset lived in the **combined S2+S38** fit rather than in the data. **Kept as this chapter's worked example precisely because it resolved**, and it resolved in the shape the rule predicted: carrying both values intact is what left the discrepancy legible as a *methodological* signal. An average would have erased the very thing that got fixed. The rule made a prediction about how the standoff would end, and the prediction held — which is why a resolved case is a stronger teacher here than a live one.
- **NOT-SOURCED in this pass:** Vogel's Re table read from the primary; the IAU 2012 AU definition primary; the Goodwin et al. Milky Way D25 primary; trophic transfer efficiency; O₂ tissue penetration depth; aortic Womersley number; the primary source for the MTE theoretical-unity objection. Each is flagged in its row with a closure action. **None of them is load-bearing for the regime-change rule.**
- **NOT-SOURCED in this pass — ladder-table values carrying no row in "The numbers".** Caught by this chapter's own gate on re-read, and named here rather than left standing, because the header's promise was **not true of the chapter's own table**: **C–C bond length ~1.5 × 10⁻¹⁰ m** (rung 3 — the bond *energy* has a row, the *length* did not); **aortic `Re` ~10³–4×10³** (rung 9 — the Womersley `α` in the same cell was flagged NOT-SOURCED, the `Re` sitting beside it was not); **galactic year ~7 × 10¹⁵ s / ~225–250 Myr** (rung 16); **heliopause ~120 AU** (rung 15); **mitochondrion `L` 5 × 10⁻⁷–10⁻⁶ m** (rung 6); ***E. coli* division time ~1.2 × 10³ s** (rung 7). None is fabricated — all are standard textbook values, and none is load-bearing for the regime-change rule — but **standard-and-probably-true is not the same as sourced**, and a plausible number with silent provenance is the precise defect this chapter exists to catch. Recorded because the gate caught its own author, which is the only evidence that a gate works. Closure action for each: fetch a primary (a cross-ref to NA-08 is an acceptable source; silence is not) and give it a row with a falsifier.
- **NOT-MEASURED:** any scalar ordering rungs 1–16 by "information density", "degree of internal model", or "complexity".

## HONEST FENCE — MODELED

Fenced **MODELED**. Individual rows carry their own classes (many OBSERVED-REPLICATED, several OBSERVED-CONTESTED, several NOT-MEASURED/NOT-SOURCED), but the *chapter as an artifact* is a **placement model**: it composes measured constants and published fits through stated assumptions — that "characteristic length" is well-defined per rung; that one force dominates per regime; that adopted IAU nominal constants stand in for measured stellar/planetary values (they are exact **by adoption**, explicitly *not* current best estimates, and must never be quoted as measurements with uncertainties). **The assumptions are the fence.** The rung count and the rung boundaries are a **choice**, not a discovery: a different carving (adding virus, biofilm, galaxy cluster) is equally defensible. What is *not* a choice is that the dominant force changes identity across the span, and that fitted exponents do not survive those changes.

Per **Gould & Lewontin (1979)**, "The Spandrels of San Marco and the Panglossian Paradigm": nothing above establishes that any rung's arrangement is an optimum. Drift, phylogenetic inertia, developmental constraint, and frozen accidents produce structure that solves nothing. **Nature's authority here is precisely and only this: it already ran the experiment under real constraints, with the failures deleted** — so convergence at a rung is evidence of a constraint-optimum, and every number above is a **hypothesis generator**, never a proof. Per **M7**, a design taken from this ladder must beat a **tuned** baseline on a **pre-registered** metric with a discriminator that collapses the gain and a true computed-residual ablation, or it is recorded **NEGATIVE**. Per **M22**, this chapter's own placements are an upstream prior and must never be re-served as fresh evidence downstream.

## Not claimed

- **Not claimed:** that the ladder is a progression, a hierarchy of value, an arrow, or a direction. It is an ordering **by length**. The blanket column does not ascend with it, and specific power runs against it by ~5 × 10⁶ from bacterium to Sun.
- **Not claimed:** that "degree of internal model" or "information density" increases along the ladder. **NOT-MEASURED.** No measurand exists. This is the gradient the ladder most invites and the one with the least behind it, and that asymmetry is stated on purpose.
- **Not claimed:** that emergence is mysterious, or that it is trivial. The operable version has three testable conditions and is a claim about spectral gaps in a dynamical system. Both the mystical reading and the dismissive reading are defects.
- **Not claimed:** that the Maynard Smith & Szathmáry framework is settled. It is influential **and** debated; the debate is carried in the body and the objection's primary source is **NOT-SOURCED in this pass**.
- **Not claimed:** that Kolokotrones et al. (2010) settles metabolic scaling — **nor that MacKay settles it against them.** It is **OBSERVED-CONTESTED** and the exchange is live on both sides: MacKay (2011), *J Theor Biol* 280(1):194–196, is a published comment against it; **Deeds, Savage & Fontana (2011)**, *J Theor Biol* 280(1):197–198, is the original authors' published reply in the same issue. Both turns are carried; neither is the verdict. The regime-change rule does **not** rest on it — DeLong et al. (2010) carries the boundary claim independently, and the rule would stand if the curvature claim fell.
- **Not claimed:** that the sixteen rungs are the right sixteen. The carving is a choice; the boundaries' physics is not.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** The NATURA twelve-value class (OBSERVED-REPLICATED / OBSERVED-SINGLE / OBSERVED-CONTESTED / MODELED / MODELED-CONTESTED / HYPOTHESIZED / INADMISSIBLE / SUPERSEDED / NOT-MEASURED / NOT-SOURCED / NOT-CONFIRMED / NOT-LOCATED — six of them registered by NA-00 amendment 2026-07-15-A) and the UNI four-value fence (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. This chapter contains **zero** UNI claims.
- **QUAESTIO-APERTA:** "full human" and "beyond human" appear nowhere here as a target, milestone, or deliverable. They are permanent open questions. The scale ladder has no top, no destination, and no rung labelled with either of them — and the temptation to read one in at rung 10 or 11 is exactly what the NOT-MEASURED fence on "degree of internal model" exists to refuse.


<!-- ===== END encyclopedia/wing-NATURA/NA-10-the-scale-ladder-and-gradients.md ===== -->

