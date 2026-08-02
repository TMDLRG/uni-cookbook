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
