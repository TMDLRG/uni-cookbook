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
