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
