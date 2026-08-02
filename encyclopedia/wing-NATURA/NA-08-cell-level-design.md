# NA-08 — Design down to the cell level: the cell as an engineered system

> **What you are reading.** A working budget for the cell treated as an engineered artifact: what sets its size, what it spends, what its machines actually deliver under measured conditions, and where its sensing precision hits a physical floor. Every number below either carries a source you can check or is written NOT-MEASURED. Nothing here raises any UNI rung — a citation to biology is never a UNI gate.

---

## The one derivation that sets everything else

Start with the only equation a cell-level designer cannot negotiate with. For diffusion in three dimensions, the mean-square displacement is `<r²> = 6Dt`, so the time to traverse a length `L` scales as:

```
t ≈ L² / (6D)
```

The exponent is the whole story. Distance is quadratic in time. Double the cell, quadruple the wait.

Put a real `D` in it. GFP (a 27 kDa protein, a fair stand-in for a mid-sized cytoplasmic protein) diffuses in *E. coli* cytoplasm at **7.7 ± 2.5 µm²/s** (BNID 100193; Elowitz et al. 1999, *J Bacteriol* 181(1):197–203, FRAP + photoactivation). In eukaryotic cytoplasm it is faster: **27 µm²/s** in CHO cells (BNID 101997; Swaminathan et al. 1997, *Biophys J* 72(4):1900–7).

Take the eukaryotic value, `6D = 162 µm²/s`, and read the ladder:

| Distance | Time by diffusion alone | Verdict |
|---|---|---|
| 1 µm | 6.2 ms | free |
| 10 µm | 0.62 s | tolerable |
| 100 µm | 62 s | a minute to deliver a protein — already a problem |
| 1 mm | 6.2 × 10³ s ≈ 1.7 h | broken |
| 1 m (an axon) | 6.2 × 10⁹ s ≈ **195 years** | not a mechanism |

That last row is the load-bearing one. A motor neuron running from spinal cord to toe cannot use diffusion for transport — not "inefficiently", *not at all*. So it does not. Kinesin walks the cargo instead, at roughly **0.5–1 µm/s** in vitro at saturating ATP (Svoboda & Block 1994, *Cell* 77:773–784, force–velocity curves by optical trapping). At ~0.8 µm/s, one metre takes ~1.25 × 10⁶ s ≈ **14 days** — slow, but finite, versus two centuries. A motor beats diffusion by ~4 orders of magnitude over that span. *(The in-vivo fast-axonal-transport rate is a different measurement and is NOT-MEASURED in this pass.)*

The second ceiling is geometric. For a sphere, surface-to-volume is `S/V = 3/R`. An *E. coli* at R ≈ 0.5 µm gets **~6 µm⁻¹** of membrane per unit volume; a mammalian cell at R ≈ 10 µm gets **~0.3 µm⁻¹** — a 20-fold cut in nutrient-flux area per unit of metabolising cytoplasm. Volume grows as `R³`, uptake area as `R²`. Growth is self-strangling.

Two independent constraints, both punishing size, both quadratic-or-worse. *E. coli* sits at ~1 µm diameter × ~2 µm length, ~1 µm³ ≈ 1 fL (BNID 100004; Milo & Phillips 2015, *Cell Biology by the Numbers*). A HeLa cell runs ~20 µm across when confluent, 1,200–4,290 µm³ (mean ≈ 2,425 µm³). Both live in the band where diffusion is still free.

## The exceptions confirm the rule (this is the part to get right)

*Thiomargarita namibiensis* is 100–300 µm wide and reaches **750 µm** (Schulz et al. 1999, *Science* 284:493–495). It appears to break the ceiling. It does not. **80–98% of its volume is a nitrate storage vacuole**, and its living cytoplasm is a shell only **~1–2 µm thick** wrapped around it. The diffusion length that matters is still ~1–2 µm. The organism got big by making most of itself *not cytoplasm*. The constraint was obeyed, not defeated.

This is the discipline: when a case looks like a counterexample, find the length scale that actually carries the flux before concluding the physics bent. It usually did not.

## The energy budget

| | *E. coli* | Mammalian cell (fibroblast, ~3,000 µm³) |
|---|---|---|
| ATP consumed | ~10⁷ /s (BNID 111461, 110656, 110628) | ~10⁹ /s (BNID 111476) |
| Power | ~10⁻¹² W = **1,000 W/kg** (BNID 109687) | ~3 × 10⁻¹⁰ W = **100 W/kg** (BNID 111474/111475) |

A bacterium runs at ~1,000 W/kg — roughly three orders of magnitude above a human's whole-body specific power. It also turns over its *entire ATP pool in about one second*. There is no reservoir. The cell is a just-in-time system with no buffer, which is why its power supply cannot be interrupted.

What does it spend on? Overwhelmingly, **protein synthesis**. A peptide bond costs **4 ATP** — 2 from pyrophosphate release at aminoacyl-tRNA charging (which makes the reaction irreversible) plus 1 GTP for each of two elongation factors. In *E. coli* on rich medium, peptide-bond synthesis is **19.1 of 31.4 mmol ATP per gram of cells ≈ 61%** of total ATP expenditure (Milo & Phillips 2015). Building the polymer *is* the budget; DNA, lipid, and wall synthesis are rounding errors beside it.

Neurons invert this. In grey matter the dominant cost is **ion pumping** — the Na⁺/K⁺-ATPase, which spends 1 ATP per 3 Na⁺ extruded, and takes ~50% of the budget. Attwell & Laughlin (2001), *J Cereb Blood Flow Metab* 21(10):1133–1145, apportion signalling energy as **action potentials 47%, postsynaptic glutamate effects 34%, resting potential 13%, glutamate recycling 3%**. *Fence: these are modelled apportionments for rodent grey matter, not direct per-process measurements, and Howarth, Gleeson & Attwell (2012), JCBFM, published revised budgets. Cite the 2001 split only with that revision named.*

## The machines, with their conditions

Performance numbers without conditions are not numbers.

**ATP synthase (F₁) — a real rotary motor.** Noji et al. (1997), *Nature* 386:299–302, attached a fluorescent actin filament to the γ subunit and watched it turn: one revolution = **three discrete 120° steps**, each driven by one ATP. Yasuda et al. (1998), *Cell* 93:1117–1124: torque is **~40 pN·nm, constant** across loads and speeds; work per 120° step ≈ **80 pN·nm**, against an in-cell ATP free energy of ~90 pN·nm — i.e. operating near the thermodynamic ceiling. Yasuda et al. (2001), *Nature* 410:898–904: **~130 rev/s** at saturating ATP, with the 120° step resolving into ~90° + ~30° substeps. No human rotary engine touches that efficiency.

**Kinesin.** Step **8 nm** (Svoboda et al. 1993, *Nature* 365:721–727, optical trapping interferometry); **1 ATP per 8-nm step** (Schnitzer & Block 1997, *Nature* 388:386–390). Stall force is **assay-dependent and genuinely spread**: 5–6 pN (Svoboda & Block 1994) vs **7–8 pN** under a molecular force clamp (Visscher, Schnitzer & Block 1999, *Nature* 400:184–189). Do not average them — carry both and name the assay.

**Myosin-V** steps **~36 nm**, stall ~2–3 pN, step size ~constant from 5 pN forward to 1.5 pN backward load. **Cytoplasmic dynein** is the messy one: 8 nm steps are reported, but so is a load-dependent step growing 8 → 16 → 24 → 32 nm as load falls. That is unresolved, not a number to quote flat.

**Ribosome.** *E. coli* ~**20 aa/s** (BNID 100059, 105067, 108490), varying 4–22 aa/s with growth rate; budding yeast **3–10 aa/s** at 30 °C (BNID 107871); mouse ES cells ~6 aa/s (BNID 107952). Error: **10⁻⁴–10⁻³ per codon** (Kramer & Farabaugh 2007, *RNA* 13:87–96). The ribosome is ~10⁵–10⁶ times sloppier than DNA replication — and that is a design choice, not a defect. Proteins are disposable; the genome is not.

**RNA polymerase.** *E. coli* **40–80 nt/s** (BNID 104900, 104902, 108488). Mammalian *elongation* is comparable at 50–100 nt/s (BNID 105566, 105113, 100662), but the *average rate across a gene* including pausing is ~6 nt/s (BNID 100661) — an order of magnitude apart. Conflating elongation rate with average rate is a common error.

**DNA polymerase — the layered number people flatten.** Fidelity is three stages multiplied, and quoting the final figure as if the polymerase achieved it alone is wrong:

| Layer | Error rate |
|---|---|
| Base selectivity (polymerase alone) | ~10⁻⁴–10⁻⁵ |
| + exonucleolytic proofreading (×10²–10³) | ~10⁻⁶–10⁻⁷ |
| + mismatch repair | → **10⁻⁸–10⁻¹⁰ per nt** |

(Kunkel 2004, *J Biol Chem*; Kunkel & Bebenek 2000, *Annu Rev Biochem*; Fijalkowska et al. 2012.) The lesson for a designer: **10⁻¹⁰ is a systems property, not a component property.** It was bought with three cheap layers, not one expensive one.

## The membrane

The lipid bilayer is **~4–5 nm** thick. A neuron holds **~−70 mV** across it. Divide:

```
E = V/d = 0.07 V / (4–5 × 10⁻⁹ m) ≈ 1.4–1.8 × 10⁷ V/m
```

For comparison, the dielectric strength of dry air at 1 atm is ≈ 3 × 10⁶ V/m *(standard reference value; not primary-sourced in this pass)*. **Every cell in your body sustains a field roughly five times what makes air explode into a spark** — continuously, for decades, across a structure two molecules thick. That is not a metaphor; it is `V/d`.

Specific membrane capacitance is ~**1 µF/cm² (0.01 F/m²)** and is nearly invariant across cell types — one of the most replicated numbers in biophysics — because it is set by bilayer thickness and lipid dielectric constant, which barely move.

Why a bilayer and nothing else: it is the only structure that is simultaneously (a) self-assembling from a single amphiphile species with no machinery, (b) self-healing (a puncture closes because the hydrophobic edge is energetically intolerable), (c) fluid enough for embedded proteins to diffuse and assemble, and (d) an insulator good enough to hold 10⁷ V/m. Nothing engineered does all four at once.

## Sensing is bounded inference — and the bound is calculable

This is the deepest link between the cell and the inference method. Berg & Purcell (1977), *Biophys J* 20:193–219, asked how precisely a cell can measure a concentration when the molecules arrive by diffusion. The answer is a floor set by counting noise. The **robust, uncontested scaling** is:

```
δc/c  ~  (D · a · c · T)^(−1/2)
```

`D` = ligand diffusion coefficient, `a` = receptor/cell size, `c` = concentration, `T` = integration time. Read it as an engineer: precision buys nothing cheaply. To halve your error you must **quadruple** integration time — pay in latency. This is a *speed–accuracy tradeoff derived from physics*, and it is exactly the tradeoff a variational scheme negotiates. A cell is doing bounded inference about its chemical world; the bound is not a metaphor, it is a number.

Bialek & Setayeshgar (2005), *PNAS* 102(29):10040–10045, argued the Berg–Purcell estimate is **"a 'noise floor' that is independent of kinetic details; real systems can be noisier but not more precise than this"** — i.e. no receptor chemistry, however clever, buys precision below the diffusive floor. That structural claim is the durable one.

**The prefactor, however, is genuinely contested — carry the dispute.** Kaizu et al. (2014), *Biophys J* 106(4):976–985 ("The Berg-Purcell limit revisited"), report that the Bialek–Setayeshgar diffusive term is missing a factor of `1/(2(1−n̄))` present in both Berg–Purcell's and their own expressions, and attribute the discrepancy to B–S linearising the reaction–diffusion equations and thereby neglecting correlations between receptor state and local ligand concentration. Kaizu et al. agree with Berg–Purcell up to a geometric factor. **The scaling is settled; the constant is not.** Anyone quoting a single closed-form Berg–Purcell prefactor without naming which convention they are in is overclaiming. *(The exact expressions are deliberately not transcribed here — see NOT-MEASURED below.)*

Berg & Purcell also derived a receptor-array result: a modest number of small receptors covering a tiny fraction of the cell surface achieves near-maximal diffusive capture. The specific formula and count are **NOT-SOURCED in this pass** — see the open row.

## Bioelectricity: the cleanest available lesson in signal vs annotation

Levin's programme is the sharpest live test of SIGNUM SIGNUM MANET, because the measurements and the interpretation are routinely welded together in the popular account and must be pulled apart.

**The signal (measured, replicated):** transmembrane potential (Vmem) distributions are measurable across tissue and are *instructive*, not merely correlated, for anatomical outcome. Pai et al. (2012), *Development* 139(2):313–323: a striking hyperpolarisation demarcates a specific cell cluster in the Xenopus anterior neural field during normal embryogenesis, and manipulating Vmem in *non-eye* cells induces well-formed ectopic eyes — morphologically and histologically similar to endogenous eyes — **far outside the anterior neural field**. In planaria, gap-junction blockade (octanol) during regeneration yields two-headed worms, and the phenotype is **stable across subsequent regenerations with no further drug and no genomic change** (reviewed in Levin 2021, *Cell* 184(8):1971–1989; see also Emmons-Bell et al. 2015; Durant et al. 2021, *Phil Trans R Soc B* 376:20190765 on bistability of the pattern state).

**The annotation (separate, contested, not claimed here):** that these bioelectric states constitute *cognition*, *memory*, or *decision-making* by cell collectives, or license a "Mind Everywhere" framing. The word "memory" in "pattern memory" is doing interpretive work — the *measurement* is a bistable state variable that persists and is heritable across regeneration. Bistable persistent state is a well-defined dynamical property. Whether it is *memory in the sense that word usually carries* is an interpretive claim resting on argument, not on the voltage recording.

**Both are legitimate. They have different evidentiary weight and must travel separately.** A design that cites the ectopic-eye result to license a claim about cognition has crossed the lane. The signal is strong enough that it needs no help from the annotation.

## The earned and the unearned: ratios and frequencies

The operator's mandate names ratios and frequencies. Separate them by receipt, with respect, and without sneering.

**EARNED — the golden angle in phyllotaxis.** ~137.5° is real and it has a real physical mechanism. Douady & Couder (1992), *Phys Rev Lett* 68:2098–2101, reproduced Fibonacci phyllotaxis in a **physical laboratory experiment** — magnetically repelling droplets deposited periodically into a rotating dish — plus numerical simulation. The pattern falls out of simple repulsion dynamics and an iterative deposition process; the system converges toward the golden mean because it *avoids rational (periodic) organisation*. No mysticism is required, and none is needed. This is what an earned ratio looks like: a mechanism, a physical replication, and a falsifier.

**INADMISSIBLE — "the golden ratio is a universal design law of nature."** Unfalsifiable as stated and sustained by cherry-picking. Recorded, not mocked. The distance between this and Douady & Couder is the entire method.

**EARNED, with its attachment fenced — the Schumann resonance.** ~**7.83 Hz** is a genuine measured Earth–ionosphere cavity resonance, predicted by Schumann (1952) from Maxwell's equations and the known cavity geometry, confirmed experimentally in 1954 (Schumann & König), with harmonics resolved by Balser & Wagner (1960) at ~14.3, 20.8, 27.3, 33.8 Hz. The **cavity physics is not in doubt.** Whether that field couples to anything at cell scale is a *completely separate claim* requiring a measured field amplitude at the membrane and a comparison against `k_BT` and membrane noise. **That amplitude is NOT-MEASURED in this pass.** The measured existence of a resonance is not evidence for any biological effect of it.

## The design checklist (operable)

To design at the cell level, state these six or you have not designed anything:

1. **Length scale `L`.** Everything follows. Above ~10–20 µm you have bought a transport problem.
2. **Re and Pe regime.** For *E. coli* (v ≈ 3 × 10⁻⁵ m/s, L = 2 × 10⁻⁶ m, ρ = 10³ kg/m³, µ = 10⁻³ Pa·s): `Re = ρvL/µ ≈ 6 × 10⁻⁵`. Inertia does not exist; stop coasting. And `Pe = vL/D ≈ 0.06–0.1` for a small molecule (D ~ 10⁻⁹ m²/s): **stirring is useless at this scale** — you cannot mix your way out, you can only wait or pump. (Purcell 1977, *Am J Phys* 45:3–11. Arithmetic shown so you can check it; inputs are order-of-magnitude.)
3. **Diffusion time budget.** `t ≈ L²/(6D)`. If it exceeds your control loop's period, you need a motor, not a gradient.
4. **ATP budget.** In ATP/s, against ~10⁷/s (bacterial) or ~10⁹/s (mammalian). Remember the pool turns over in ~1 s — no buffer.
5. **Information budget.** Bits/s *and the error rate you can afford*. 10⁻³ for a protein, 10⁻¹⁰ for the genome — and note the second was bought with three cheap layers, not one perfect component.
6. **The blanket.** State what is inside, what *is* the membrane, and what is outside. If you cannot draw the boundary, you do not have a system; you have a region.

## The numbers (the ratio/frequency table)

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `D_GFP,ec` | 7.7 ± 2.5 | µm²/s | GFP (27 kDa), *E. coli* cytoplasm, FRAP/photoactivation | OBSERVED-REPLICATED | BNID 100193; Elowitz et al. 1999, *J Bacteriol* 181(1):197–203 | Repeat FRAP; a value outside 3–14 µm²/s under stated conditions refutes |
| `D_GFP,euk` | 27 | µm²/s | GFP-S65T, CHO cytoplasm | OBSERVED-REPLICATED | BNID 101997; Swaminathan et al. 1997, *Biophys J* 72(4):1900–7 | Independent FRAP in eukaryotic cytoplasm disagreeing >2× |
| `t(1 m)` | ~6.2 × 10⁹ (≈195 yr) | s | 3D diffusion, D = 27 µm²/s, `t = L²/6D` | MODELED | Computed here from BNID 101997 + `<r²>=6Dt` | Arithmetic error, or a demonstration of 1 m protein transport by diffusion alone |
| `S/V` | 6 vs 0.3 | µm⁻¹ | sphere `3/R`; R = 0.5 µm vs 10 µm | MODELED | Computed here (geometry) | Geometric error |
| `L_Thio` | 100–300 (max 750) | µm | *Thiomargarita namibiensis*, cell width | OBSERVED-REPLICATED | Schulz et al. 1999, *Science* 284:493–495 | Larger true-cytoplasm cell found |
| `f_vac` | 80–98 | % of cell volume | *Thiomargarita* nitrate vacuole; cytoplasm shell ~1–2 µm | OBSERVED-REPLICATED | Schulz et al. 1999 | Show cytoplasm fills the cell |
| `ATP_ec` | ~10⁷ | ATP/s/cell | *E. coli*, growing | OBSERVED-REPLICATED | BNID 111461, 110656, 110628 | Independent measurement >10× off |
| `ATP_mam` | ~10⁹ | ATP/s/cell | human fibroblast, ~3,000 µm³ | OBSERVED-REPLICATED | BNID 111476 | As above |
| `P_ec` | ~10⁻¹² (1,000 W/kg) | W/cell | *E. coli*, glucose minimal media | OBSERVED-REPLICATED | BNID 109687 | As above |
| `c_pep` | 4 | ATP per peptide bond | 2 (PPi, aa-tRNA charging) + 1 GTP × 2 elongation factors | OBSERVED-REPLICATED | Milo & Phillips 2015, *Cell Biology by the Numbers* | Show a bond formed for <4 |
| `f_prot` | 61 | % of total cell ATP | *E. coli*, rich medium; 19.1 of 31.4 mmol ATP/g cells | MODELED | Milo & Phillips 2015 (budget model) | Recompute the budget; a different dominant sink |
| `ΔG_ATP` | −47 to −50 (≈20 k_BT ≈ 80–90 pN·nm) | kJ/mol | in vivo; *E. coli* on glucose −47 | OBSERVED-REPLICATED | BioNumbers ("How much energy is released in ATP hydrolysis?") | Measured phosphorylation potential outside −40 to −65 |
| `ΔG°'_ATP` | −28 to −34 (≈12 k_BT) | kJ/mol | **standard** conditions (1 M) — NOT the cell | OBSERVED-REPLICATED | as above | — |
| `τ_F1` | ~40 | pN·nm | F₁-ATPase torque, constant across load/speed | OBSERVED-REPLICATED | Yasuda et al. 1998, *Cell* 93:1117–1124 | Load-dependent torque under same assay |
| `W_F1` | ~80 (vs ~90 available) | pN·nm per 120° step | F₁, single-molecule, in vitro | OBSERVED-REPLICATED | Yasuda et al. 1998; Noji et al. 1997, *Nature* 386:299–302 | Work/step measured well below 80 |
| `ω_F1` | ~130 | rev/s | F₁, saturating ATP; 120° = 90° + 30° substeps | OBSERVED-REPLICATED | Yasuda et al. 2001, *Nature* 410:898–904 | Substep structure fails to replicate |
| `d_kin` | 8 | nm/step | kinesin-1 on microtubule, optical trap | OBSERVED-REPLICATED | Svoboda et al. 1993, *Nature* 365:721–727 | A different step periodicity |
| `n_ATP,kin` | 1 | ATP per 8-nm step | kinesin-1 | OBSERVED-REPLICATED | Schnitzer & Block 1997, *Nature* 388:386–390 | Measured coupling ≠ 1:1 |
| `F_stall,kin` | **5–6** *or* **7–8** | pN | 5–6: Svoboda & Block 1994. 7–8: force clamp, Visscher 1999 | **OBSERVED-CONTESTED** | Svoboda & Block 1994, *Cell* 77:773–784; Visscher et al. 1999, *Nature* 400:184–189 | Resolve by assay; do not average. A study reconciling both under one method |
| `v_kin` | ~0.5–1 (commonly ~0.8) | µm/s | saturating ATP, near-zero load, in vitro | OBSERVED-REPLICATED | Svoboda & Block 1994 (force–velocity) | Outside range under stated conditions |
| `d_myoV` | ~36 | nm/step | myosin-V on actin; stall ~2–3 pN | OBSERVED-REPLICATED | single-molecule optical trap literature | Different step periodicity |
| `d_dyn` | 8 (or 8→32, load-dependent) | nm/step | cytoplasmic dynein — **unresolved** | **OBSERVED-CONTESTED** | Optical-tweezer reports disagree | A method resolving load-dependence |
| `r_rib,ec` | ~20 (range 4–22) | aa/s | *E. coli*, growth-rate dependent | OBSERVED-REPLICATED | BNID 100059, 105067, 108490 | Outside 4–22 at stated growth rate |
| `r_rib,euk` | 3–10 (yeast, 30 °C); ~6 (mouse ES) | aa/s | eukaryote | OBSERVED-REPLICATED | BNID 107871, 107952 | As above |
| `ε_rib` | 10⁻⁴–10⁻³ | per codon | missense/misreading | OBSERVED-REPLICATED | Kramer & Farabaugh 2007, *RNA* 13:87–96 | Measured rate outside range |
| `r_RNAP,ec` | 40–80 | nt/s | *E. coli* | OBSERVED-REPLICATED | BNID 104900, 104902, 108488 | Outside range |
| `r_RNAP,mam` | 50–100 elongation **vs** ~6 average-across-gene | nt/s | mammalian — **do not conflate** | OBSERVED-REPLICATED | BNID 105566/105113/100662; BNID 100661 | Show the two measure the same thing |
| `ε_pol` | ~10⁻⁴–10⁻⁵ | per nt | polymerase base selectivity **alone** | OBSERVED-REPLICATED | Kunkel & Bebenek 2000, *Annu Rev Biochem*; Kunkel 2004, *JBC* | Exonuclease-deficient rate outside range |
| `ε_proof` | ~10⁻⁶–10⁻⁷ (×10²–10³ gain) | per nt | + exonucleolytic proofreading | OBSERVED-REPLICATED | as above | MMR-deficient rate outside range |
| `ε_final` | 10⁻⁸–10⁻¹⁰ | per nt | + mismatch repair; pro- and eukaryotes | OBSERVED-REPLICATED | as above | Whole-genome mutation accumulation outside range |
| `d_bilayer` | 4–5 | nm | lipid bilayer thickness | OBSERVED-REPLICATED | standard membrane biophysics; Milo & Phillips 2015 | Structural measurement outside range |
| `V_m` | ~−70 | mV | resting neuron | OBSERVED-REPLICATED | standard electrophysiology | — |
| `E_m` | **1.4–1.8 × 10⁷** | V/m | `V/d`, 70 mV over 4–5 nm | MODELED | Computed here from `V_m` and `d_bilayer` | Arithmetic error, or `d`/`V` refuted |
| `E_air` | ≈3 × 10⁶ | V/m | dry air, 1 atm — dielectric strength | OBSERVED-REPLICATED *(not primary-sourced in this pass)* | standard physical reference | Fetch a primary reference |
| `C_m` | ~1 (0.01) | µF/cm² (F/m²) | specific membrane capacitance, near-invariant across cell types | OBSERVED-REPLICATED | standard membrane biophysics (Cole; Hodgkin & Huxley 1952) | A cell type deviating >2× with intact bilayer |
| `κ_MT` | 2.2 × 10⁻²³ (±6.4%); 2.1 × 10⁻²³ (±4.7%, rhodamine) | N·m² | taxol-stabilised microtubule, flexural rigidity | OBSERVED-REPLICATED | Gittes et al. 1993, *J Cell Biol* 120(4):923–934 | Independent measurement >2× off |
| `ℓ_p,MT` | ~5,200 (5.2 mm) | µm | microtubule persistence length, `ℓ_p = κ/k_BT` | OBSERVED-REPLICATED | Gittes et al. 1993 | see contested row below |
| `ℓ_p,MT` **length-dependence** | persistence length varies with filament length | — | grafted MTs | **OBSERVED-CONTESTED** | Pampaloni et al. 2006, *PNAS* — length-dependent `ℓ_p`; contradicts a single MT constant | Resolve; a method showing length-independence |
| `ℓ_p,actin` | ~17.7 | µm | actin filament, rhodamine-phalloidin | OBSERVED-REPLICATED | Gittes et al. 1993 | Independent measurement >2× off |
| `ℓ_p,MT/ℓ_p,actin` | ~294 (~300×) | dimensionless | Gittes values | MODELED | Computed here | Ratio recomputation |
| `δc/c` **scaling** | ∝ `(D·a·c·T)^(−1/2)` | dimensionless | diffusion-limited chemoreception | OBSERVED-REPLICATED (as a scaling) | Berg & Purcell 1977, *Biophys J* 20:193–219 | A sensor beating the −1/2 exponent |
| `δc/c` **prefactor** | **disputed** | — | B–P vs Bialek–Setayeshgar vs Kaizu: B–S term missing `1/(2(1−n̄))` | **OBSERVED-CONTESTED / MODELED** | Bialek & Setayeshgar 2005, *PNAS* 102(29):10040–5; Kaizu et al. 2014, *Biophys J* 106(4):976–85 | A treatment retaining receptor–ligand correlations that settles the constant |
| `Re` | ~6 × 10⁻⁵ | dimensionless | *E. coli*: v ≈ 3 × 10⁻⁵ m/s, L = 2 µm, ρ = 10³ kg/m³, µ = 10⁻³ Pa·s | MODELED | Computed here; regime per Purcell 1977, *Am J Phys* 45:3–11 | Inputs refuted (swim speed is order-of-magnitude) |
| `Pe` | ~0.06–0.1 | dimensionless | same, D ~ 10⁻⁹ m²/s (small molecule) | MODELED | Computed here | Demonstrate advective mixing gain at this scale |
| `f_Schumann` | **7.83** (harmonics ~14.3, 20.8, 27.3, 33.8) | Hz | Earth–ionosphere cavity fundamental | OBSERVED-REPLICATED | Schumann 1952 (prediction); Schumann & König 1954 (confirmation); Balser & Wagner 1960 | ELF measurement failing to find the cavity mode |
| `E_Schumann@membrane` | — | V/m | field amplitude at a cell membrane | **NOT-MEASURED** | not sourced in this pass | Measure amplitude; compare to `k_BT` and membrane noise |
| `θ_golden` | ~137.5 | degrees | phyllotaxis divergence angle; physically reproduced | OBSERVED-REPLICATED | Douady & Couder 1992, *Phys Rev Lett* 68:2098–2101 | Repulsion-dynamics experiment failing to converge to the golden mean |
| `E_neuron` split | AP 47 / postsyn-glutamate 34 / rest 13 / recycling 3 | % of signalling ATP | rodent grey matter — **modelled apportionment**, revised 2012 | MODELED | Attwell & Laughlin 2001, *JCBFM* 21(10):1133–45; rev. Howarth et al. 2012 | Recompute the budget; the 2012 revision supersedes on any point of conflict |
| `n_Na/ATP` | 3 Na⁺ per 1 ATP | ions/ATP | Na⁺/K⁺-ATPase stoichiometry | OBSERVED-REPLICATED | Attwell & Laughlin 2001 and standard references | Measured stoichiometry ≠ 3:2:1 |

## Falsifier (operable)

This chapter's central structural claim — **that diffusion time scaling as `L²` is what sets the cell's size ceiling, and that every apparent exception either shrinks the effective diffusion length or replaces diffusion with a motor** — is refuted by exhibiting **one organism with a contiguous metabolically active cytoplasm whose shortest transport dimension exceeds ~50 µm, that relies on diffusion (not motors, not cytoplasmic streaming, not a vacuole shell, not multinucleation) for its bulk internal transport, and that sustains a normal growth rate.** *Thiomargarita* is not that organism (vacuole shell, cytoplasm 1–2 µm), nor is a 1 m neuron (kinesin/dynein), nor is a coenocyte (multiple nuclei distributed to shorten the delivery length — the same fix applied combinatorially).

Secondary falsifiers, each row-local: any number in the table found outside its stated scope under its stated conditions moves that row and only that row. A refuted row does not refute the chapter; a refuted `L²` moves the chapter.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **"The golden ratio is a universal design law of nature."** — INADMISSIBLE. Unfalsifiable as stated: no observation is specified that could refute it, and the supporting instances are selected post hoc. **Receipt of failure:** the claim survives every counterexample by redescription, which is the signature of an unfalsifiable claim. Recorded, not mocked. The *earned* neighbour (θ ≈ 137.5° in phyllotaxis, with the Douady & Couder 1992 physical mechanism) is in the table above — the contrast is the lesson, not the rebuke.
- **432 Hz tuning as physics or biology.** — INADMISSIBLE as a physical or biological claim. No mechanism is specified at which any measured biological quantity would differ from 440 Hz tuning; as stated it names no falsifier. It may be recorded as an HONEST/cultural signal (a real aesthetic preference, honestly held) — never as a TRUE/measured one. These are separate stores and never merge.
- **Chakra-frequency tables.** — INADMISSIBLE as physics. The tabulated Hz values do not correspond to a measured field, oscillation, or coupling in any published measurement located here. Admissible as an HONEST/cultural signal, never as a TRUE/measured one. Recorded with respect for the person asking; the fence is on the claim class, not the questioner.
- **Schumann-resonance human-health claims.** — Distinct from the cavity resonance itself, which is EARNED and in the table. The health claim requires a measured field amplitude at the target tissue and a comparison against `k_BT` and membrane noise. That amplitude is **NOT-MEASURED here**, so the claim is not evaluated — neither asserted nor refuted. The existence of a resonance is not evidence of a biological effect of it; that inference is the defect.
- **NEGATIVE / conflation trap:** quoting mammalian RNA polymerase at "~6 nt/s" as its *elongation* rate is wrong (elongation is 50–100 nt/s; ~6 nt/s is the across-gene average including pausing). Recorded because the error is common and the two BNIDs are adjacent.
- **NEGATIVE / conflation trap:** quoting `10⁻¹⁰` as *DNA polymerase's* error rate is wrong. It is the rate *after* three layers. The polymerase alone is ~10⁻⁴–10⁻⁵.
- **NOT-SOURCED in this pass:** the Berg & Purcell receptor-array result (the capture-rate formula and the receptor count achieving near-maximal capture over a small surface fraction). The qualitative result is attributed to Berg & Purcell 1977; the numbers are **not printed here because they were not confirmed.** Falsifier/closure: fetch *Biophys J* 20:193–219 and read the array section.
- **NOT-MEASURED:** in-vivo fast axonal transport rate; Schumann field amplitude at a cell membrane; a primary source for the dielectric strength of air.

## HONEST FENCE — MODELED

This chapter is fenced **MODELED**. Its individual rows carry their own classes (most OBSERVED-REPLICATED, several OBSERVED-CONTESTED, several NOT-MEASURED), but the *chapter as an artifact* is a budget model: it composes measured constants through stated assumptions (3D diffusion convention `<r²>=6Dt`; spherical S/V; order-of-magnitude inputs for Re and Pe) to reach design conclusions. **The assumptions are the fence.** Change the diffusion convention (1D `L²/2D` vs 3D `L²/6D`) and every derived time moves by 3×; the conclusions are robust to that factor because they turn on the *exponent*, not the prefactor — but a reader who needs the prefactor must state the convention.

Per **Gould & Lewontin (1979), "The Spandrels of San Marco and the Panglossian Paradigm"**: none of the above establishes that any cellular feature is an optimum. Phylogenetic inertia, drift, developmental constraint, pleiotropy, and historical contingency produce features that solve nothing. The inverted vertebrate retina and the recurrent laryngeal nerve's detour are frozen accidents, not designs. **Nature's authority here is precisely and only this: it has already run a very long parallel search under real physical constraints in which the failures were deleted.** That makes convergence evidence of a constraint-optimum and makes every number above a *hypothesis generator*. It does not make any of them a proof. Per repo rule **M7**, a biomimetic design taken from this chapter must still beat a **tuned conventional baseline** on a **pre-registered metric** with a load-bearing discriminator, or it is recorded **NEGATIVE**.

## Not claimed

- **Not claimed:** that a cell is aware, sentient, cognitive, or that it "knows" anything. The Berg–Purcell result says a cell's chemical estimate is bounded by counting noise. "Bounded inference" is a *statistical* description of a physical process, not a claim about experience.
- **Not claimed:** that building a cell is close, tractable, or on any roadmap. Nothing here is a construction plan.
- **Not claimed:** that Levin's bioelectric phenomena establish cognition, memory, or mind in cell collectives. The measurements (instructive Vmem, ectopic eyes, stable heteromorphic regeneration) are strong and replicated. The cognitive framing is a **separate, contested interpretive claim** and is carried separately. Citing the first to license the second is the lane-crossing this chapter exists to prevent.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** Reading Gittes et al. 1993 does not make any UNI claim proven, designed, or built. The NATURA vocabulary (OBSERVED-REPLICATED / OBSERVED-CONTESTED / MODELED / HYPOTHESIZED / INADMISSIBLE / NOT-MEASURED) and the UNI ledger vocabulary (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. This chapter contains **zero** UNI claims.
- **Not claimed:** that the cell's design is optimal, or that "nature does it this way" is an argument. See the Gould & Lewontin fence.
- **Not claimed:** any single closed-form Berg–Purcell prefactor. The scaling is settled; the constant is disputed and the dispute is printed.
- **Not claimed:** that the exceptions section is exhaustive. Cytoplasmic streaming, syncytia, and multinucleation are named as size-ceiling workarounds but are not analysed here.
- **QUAESTIO-APERTA:** "the next evolution beyond human" and "full human" appear nowhere in this chapter as a target, milestone, or deliverable. They are permanent open questions, not plans, and cell-level design has no bearing on them.
