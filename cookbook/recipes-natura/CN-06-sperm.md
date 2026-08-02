# CN-06 — Sperm: the minimal motile delivery vehicle

> **What you are building.** A delivery vehicle stripped to the bone, designed against a spec that admits no negotiation. Read it as a design exercise, not as biology appreciation: the physics writes most of the requirements document, and a designer who does not read the physics first builds something that does not move at all. Every number below carries a source you can check, its **condition**, or the word NOT-MEASURED. Nothing here raises any UNI rung — a citation to biology is never a UNI gate.

---

## The spec

Deliver one haploid genome to one target. The environment is viscous, hostile, and unmapped. You get one shot: the vehicle is terminally differentiated at spermiation — no transcription, no repair, no rebuild. You may draw fuel from the medium (fructose in semen, glucose in tract fluid), so the *energy* budget is not fixed, but the *machinery* budget is: whatever you shipped with is all you will ever have. You are one of hundreds of millions launched simultaneously, and the medium's Reynolds number is about **5 × 10⁻³**.

That last line is the whole requirements document. Read it first or build the wrong thing.

## The regime: do the arithmetic before you draw anything

`Re = ρuL/µ`. Put real numbers in:

- `ρ ≈ 1.0 × 10³ kg/m³` — water. (At 37 °C it is ≈ 993 kg/m³; a 0.7 % correction cannot move an order of magnitude.)
- `u = 62 µm/s = 6.2 × 10⁻⁵ m/s` — mean progressive velocity of **migrating** human sperm, low-viscosity medium, **37 °C**, n = 16 (Smith et al. 2009, *Cell Motil Cytoskeleton* 66(4):220–236).
- `L = 55 µm = 5.5 × 10⁻⁵ m` — whole cell. WHO morphometry: head 4–5 µm, midpiece ~7–8 µm, tail ≥ 45 µm (WHO 2021, 6th ed.).
- `µ = 7.0 × 10⁻⁴ Pa·s` — aqueous buffer at 37 °C, measured at ~0.7 mPa·s (Saggiorato et al. 2017, *Nat Commun* 8:1415).

```
Re = (1.0×10³ · 6.2×10⁻⁵ · 5.5×10⁻⁵) / 7.0×10⁻⁴
   = 3.41×10⁻⁶ / 7.0×10⁻⁴
   = 4.9 × 10⁻³
```

Bracket the inputs (u = 30–65 µm/s, L = 50–60 µm) and you get **2 × 10⁻³ to 6 × 10⁻³**. In cervical mucus the denominator explodes: at `µ ≈ 0.14 Pa·s` (the 1 % methylcellulose analogue characterised in Smith et al. 2009; midcycle mucus is estimated at ~0.2 Pa·s from Wolf et al. 1977's moduli), and taking the velocity **actually observed at that viscosity** (`u = 65 µm/s`, Smith et al. 2009 — not the 62 µm/s used above), `Re ≈ 2.6 × 10⁻⁵`. Hold `u` at 62 µm/s instead and it is 2.4 × 10⁻⁵; the exponent does not care, but the input swap is named rather than hidden.

Now the consequence, computed rather than asserted. If the flagellum stopped, how far would the cell coast? Stokes drag gives `τ = m/(6πµa)`. Take the cell volume as a head ellipsoid (4.5 × 3 × 1 µm ≈ 7.1 µm³) plus a flagellar cylinder (50 µm × 0.5 µm diameter ≈ 9.8 µm³) ≈ 17 µm³ = 1.7 × 10⁻¹⁷ m³; at `ρ_cell ≈ 1.1 × 10³ kg/m³`, `m ≈ 1.9 × 10⁻¹⁴ kg`. With `a ≈ 2 µm`:

```
6πµa = 6π · 7.0×10⁻⁴ · 2×10⁻⁶ = 2.6 × 10⁻⁸ kg/s
τ    = 1.9×10⁻¹⁴ / 2.6×10⁻⁸  ≈ 7.3 × 10⁻⁷ s  (0.7 µs)
d    = u·τ = 6.2×10⁻⁵ · 7.3×10⁻⁷ ≈ 4.5 × 10⁻¹¹ m ≈ 0.45 Å
```

**The vehicle coasts less than a third of a carbon–carbon bond length (1.54 Å).** Inertia is not "small" here. It is absent. Every micron of progress must be paid for at the instant it is made.

## Purcell's scallop theorem: physics dictating form

Purcell (1977), *Am J Phys* 45:3–11, states the constraint that a naive designer will violate: **a body at low Reynolds number cannot propel itself by a purely reciprocal deformation.** The Stokes equations contain no time derivative. The flow is set entirely by the *instantaneous* boundary configuration, so the net displacement depends only on the **sequence of shapes**, never on the rate at which they are traversed. Open the scallop slowly, close it quickly — it does not matter. Run the shape sequence forward and then backward and you return exactly to where you started. Speed buys nothing; only asymmetry in the *shape path* buys anything.

**Say the design failure out loud.** A designer ignorant of this theorem builds a paddle — one hinge, one degree of freedom, stroke and recovery. It is the obvious solution, it is what works at human scale, and it produces **exactly zero** net displacement. Not inefficient. Zero. This is the cleanest case in biology of physics writing the form: the flagellum *must* beat non-reciprocally, and it does — a travelling wave, propagating head-to-tip, tracing a loop in configuration space that never retraces itself.

Purcell's own minimal escape was the three-link swimmer: two hinges, a cycle in a 2-D configuration space that encloses area. Lauga (2011), *Soft Matter* 7:3060–3065, enumerates the escapes: non-reciprocal kinematics, inertia, extra degrees of freedom, **non-Newtonian fluids**, hydrodynamic interactions, boundaries.

That fourth escape is a fence on this chapter, not a footnote. Cervical mucus is **viscoelastic**, not Newtonian: Maxwell fits to the moduli measured by **Wolf et al. 1977** give relaxation times of ~0.027–0.033 s and effective viscosities of ~0.2 Pa·s (Day 0) to ~0.68 Pa·s (Day 5) — **MODELED**, per Smith et al. 2009's fit. (**Smith et al. did not measure mucus.** Their own cone-and-plate rheometry at 37 °C characterises their 1 % methylcellulose *analogue*, which is less elastic: relaxation time 0.006 s at µ = 0.14 Pa·s. Do not splice the analogue's number onto the mucus end of the range.) So the theorem's premise is *violated in vivo*. It still explains why the flagellum is a travelling wave — the design is old and the constraint held wherever it applied — but anyone who says "the scallop theorem forbids X in the female tract" has skipped a step.

**And the travelling wave alone is still not enough.** A wave on a slender filament produces thrust only because of **drag anisotropy**: the resistance coefficient normal to the filament exceeds the tangential one. Gray & Hancock (1955), *J Exp Biol* 32:802–814, give resistive-force coefficients for sea-urchin sperm far from a boundary. Their ratio is **not a measurement and not exactly 2**: it is a slender-body Stokes coefficient, `ζ⊥/ζ∥ = 2(ln(2λ/a) − 0.5)/(ln(2λ/a) + 0.5)`, which is **strictly less than 2 for any real filament** — ≈1.5–1.8 at realistic `ln(2λ/a) ≈ 3–5` — and reaches 2 only asymptotically as the aspect ratio → ∞. Cite it **MODELED**, with the slenderness assumption as its fence. Set that ratio to 1 and the thrust integrates to zero — travelling wave or not. **The entire propulsion of every flagellate on Earth is bought from an order-1.5-to-2 asymmetry in the drag on a thin rod.**

## The motor: sliding is not bending

The axoneme is the 9+2 array — nine doublet microtubules around a central pair — with thousands of dyneins attached to the doublets. Cryo-electron tomography puts **~67,500 dyneins in a sea-urchin sperm flagellum**; on the two-groups-of-doublets hypothesis, ~15,000 are active per beat, each taking ~8 nm power strokes (Chen et al. 2015, *Biophys J* 109:2562–2573, and refs therein).

Dynein *slides* adjacent doublets past each other. Sliding is shear. Shear is not bending. **The conversion is done by constraint, and the receipt is an ablation.** Summers & Gibbons (1971), *PNAS* 68(12):3092–3096, briefly digested sea-urchin axonemes with trypsin, then added ATP. The axonemes did not bend. They **disintegrated actively**, sliding apart into individual tubules and groups, the partially disintegrated axoneme tending to coil into a helix. *How far* they extended is **NOT-SOURCED in this pass** — secondary accounts conflict (several-fold / ~7× / the common textbook nine-fold), and the 50th-anniversary review (Lindemann & Mitchell, *Mol Biol Cell* 2018) recounts the experiment without giving an extension figure. Falsifier: read S&G 1971 pp. 3092–3096 and print it.

**One attribution correction, since this paragraph is the receipt.** That trypsin's targets are the radial-spoke heads and nexin links, with the dynein arms left intact, is **later work** (Witman et al.) — S&G 1971 did not identify which structures the digestion removed. The ablation still licenses the conclusion; it does not license the mechanism being read back into the 1971 paper.

Read that as a designer. The links are not scaffolding; **the links are the transmission.** Remove the thing that resists sliding and the motor still runs, still burns ATP, still generates force — and the machine disintegrates instead of swimming. Curvature is what shear becomes when you refuse to let it go anywhere.

## A rate without its condition is not a number

Same cells, same 37 °C, same population of migrating human sperm; only the fluid changes (Smith et al. 2009):

| | low viscosity | high viscosity (~0.14 Pa·s) |
|---|---|---|
| beat frequency | **23 Hz** | **11 Hz** |
| wavelength | 39 µm | 18 µm |
| wavespeed | 890 µm/s | 200 µm/s |
| progression per beat | 2.7 µm | 5.8 µm |
| **progressive velocity** | **62 µm/s** | **65 µm/s** |

The frequency halves. The wavespeed drops 4.4-fold. **The swimming speed does not change.** The cell trades frequency for wavelength along an approximately constant wavespeed constraint (`wavespeed = frequency × wavelength`) and holds its output flat against a ~200-fold rise in viscosity. Yazdan Parast et al. (2024), *Small Methods* 8(7):e2300928, report the same invariance across 75–1,000 mPa·s for human sperm, with sperm dissipating **over sixfold more energy into the fluid without elevating metabolic activity**.

Quote "human sperm beat at 20 Hz" without the viscosity and the temperature and you have published a number that is wrong by 2× for half the conditions it will be read under.

## Efficiency: honestly terrible, and instructive

Chen et al. (2015) measured single demembranated sea-urchin sperm axonemes, reactivated at [ATP] = 20 µM, in buffer versus 0.5 % methylcellulose:

| | low viscosity | high viscosity |
|---|---|---|
| chemomechanical `ε_chemo` | 0.34 | 0.6 |
| hydrodynamic `ε_hydro` | **0.004** | **0.013** |
| overall `ε_swim` | **0.001** | **0.008** |

ATP per beat is **not** the one viscosity-independent quantity here, and the condition belongs on it: **(2.3 ± 0.2) × 10⁵ ATP/beat** in low viscosity → **(3.2 ± 0.5) × 10⁵** in 0.5 % methylcellulose. That ~39 % rise is the paper's own headline result — raising the viscosity raises the energy consumed per beat cycle. Rate: **(2.4 ± 0.3) × 10⁶ ATP/s** for an actively beating axoneme (vs (9.2 ± 0.2) × 10⁵ ATP/s inactive — dyneins burn ATP even when the thing is not swimming).

Read that against the table above: energy **per beat** goes *up* under load at the same time as `ε_hydro` goes *up*. Both move the same way, and neither moves the way a naive efficiency argument predicts — it is the same counterintuitive direction the HONEST FENCE flags at the end of this chapter.

The dynein-to-mechanical-work conversion is respectable (34–60 %). The **hydrodynamic** efficiency is 0.4–1.3 %. The authors name the reason: the **predominant contribution of elastic deformation over hydrodynamic dissipation**. Almost all the mechanical work goes into bending the flagellum against its own stiffness; almost none goes into pushing water. The axoneme is not a well-designed propeller. It is a well-designed *bending machine* that happens to propel.

**Fence, load-bearing:** these are demembranated sea-urchin axonemes at 20 µM ATP, **not** intact human sperm at physiological ATP. `ε_hydro` for an intact human spermatozoon is **NOT-MEASURED here**.

## Energy: where the ATP comes from was genuinely contested

The midpiece carries **~50–75 mitochondria**, ~1 mtDNA copy each (Hirata et al. 2002, *Reprod Med Biol* 1(2):41–47). Obvious inference: the midpiece is the power plant. The obvious inference is at best half right. Miki et al. (2004), *PNAS* 101(47):16501–16506, knocked out **GAPDHS**, the sperm-specific glycolytic isozyme bound to the fibrous sheath along the **principal piece**. Gapds⁻/⁻ males were infertile with sluggish, non-progressive sperm — **while mitochondrial function was unchanged**. Glycolysis, distributed *along the flagellum*, was doing the work.

This is NA-08's `t ≈ L²/6D` argument in a new costume: the midpiece sits ~50 µm from the tip. Rather than diffuse ATP down the whole flagellum, bolt the factory to the fibrous sheath and make it everywhere at once. **But do not over-read one knockout in one species.** Ford (2006), *Hum Reprod Update* 12(3):269–274, frames the mouse result against the human case, where the balance is not settled. Record it **OBSERVED-CONTESTED / species-dependent**, not solved.

## Payload: protamines and the acrosome

**Protamines.** Small, arginine-rich, they displace histones during spermiogenesis and coil DNA into toroids of ~50 kb. That *toroid mechanism* has a genuine single-molecule receipt: Brewer, Corzett & Balhorn (1999), *Science* 286(5437):120–123, drew single **λ-phage** DNA molecules into protamine toroids in an optical trap and read the kinetics against the number of arginine anchoring domains. **Mind the receipt boundary:** Brewer 1999 measured λ-phage DNA in a trap — not sperm chromatin, and not against a somatic comparator. It is a receipt for the mechanism, never for a fold-compaction ratio.

Compaction itself, from the review literature (Balhorn 2007, *Genome Biol* 8(9):227): sperm chromatin ends up **~10× more compacted than the somatic interphase nucleus**, and **≥6× more condensed than mitotic chromosomes**. Those are two different comparators; **carry them separately** — collapsing them is how the familiar "10–20×" range gets made, and this pass could not source its 20× upper bound at all.

Three payoffs at once: a smaller head (less drag on a vehicle whose entire propulsion comes from a 2:1 drag ratio); mechanical and chemical protection for a genome that cannot be repaired en route; and transcriptional silence — the payload is **inert cargo, not a running process**. That last one is why the vehicle can be gutted of everything else. Histone retention is itself contested and species-split: **~5–15 % retained in human sperm, ~1 % in mouse** (Balhorn 2007). Carry the spread; do not average it.

**The acrosome** is a Golgi-derived secretory vesicle capping the head, loaded with hydrolases including acrosin — and here the knockout literature delivers a lesson worth more than the fact. Acrosin-null **mice are fertile** (Baba et al. 1994, cited in Hirose et al. 2020); for years this was read as "acrosin is dispensable." Then Hirose et al. (2020), *PNAS* 117(5):2513–2518, made acrosin-null **hamsters**: completely infertile, sperm reaching and attaching to the zona pellucida but unable to penetrate it — and **strip the zona artificially and every oocyte was fertilised**, localising the defect exactly. One negative knockout in one species had refuted nothing.

## Navigation as inference — and the epistemic action

**Sea urchin: OBSERVED-REPLICATED.** Ward et al. (1985), *J Cell Biol* 101:2324–2329, identified resact from *Arbacia punctulata* egg jelly. Kaupp et al. (2003), *Nat Cell Biol* 5:109–117: **a single bound resact molecule elicits a Ca²⁺ response**; 50–100 saturate it. Kashikar et al. (2012), *J Cell Biol* 198(6):1075–1091: minimal detectable gradient **0.8 fM/µm**; sampling window **0.2–0.6 s**. Ramírez-Gómez et al. (2020), *eLife* 9:e50532: chemotaxis is driven by the **slope**, and they **predict** — from a theoretical detection-limit derivation sweeping 10⁻¹¹–10⁻⁶ M, not from a measurement — a threshold relative steepness of ~2.6–3 × 10⁻³ µm⁻¹.

**Human: OBSERVED-CONTESTED, and stay honest about it.** Progesterone activates CatSper and drives Ca²⁺ influx in human sperm — that much is replicated (Strünker et al. 2011, *Nature* 471:382–386; Lishko et al. 2011, *Nature* 471:387–391). Whether progesterone is *the* chemoattractant is disputed: charcoal-stripping follicular fluid abolished hyperactivation-like motility **but not chemotaxis**, while stripping cumulus-conditioned medium abolished chemotactic activity. Rheotaxis is reported for mouse and human sperm (Miki & Clapham 2013, *Curr Biol* 23:443–452). Thermotaxis was proposed from a ~2 °C difference between the **isthmus** (the sperm reservoir) and the **isthmic–ampullary junction** (the fertilisation site) in the rabbit (Bahat et al. 2003, *Nat Med* 9:149–150). Note what that is: an **anatomical** temperature difference between two sites, with **no distance attached to it**. The gradient length over which Bahat et al. assayed thermotaxis in vitro is **NOT-SOURCED in this pass** — falsifier: read Bahat et al. 2003's methods and print the chamber gradient in °C/mm. The claim was then **questioned by Miki & Clapham (2013)**, on the grounds that convective currents would swamp it. Human guidance is not settled. Do not write it as if it were.

**Now the part worth stealing.** Jikeli et al. (2015), *Nat Commun* 6:7985, tracked *A. punctulata* sperm holographically in 3-D. Swimming freely far from boundaries **with no chemoattractant gradient present**, sperm followed helical paths of radius **8.4 ± 3.1 µm**, period **0.38 ± 0.07 s**, pitch **47.6 ± 9.1 µm**, speed **200 ± 57 µm/s** (n = 20 cells, 1 s tracks). Those are the **unstimulated baseline** — the control the chemotactic responses were later measured against, *not* measurements taken under a gradient. In 3-D chemoattractant landscapes, that helix becomes the sampling instrument: *a spatial gradient is translated into a temporal stimulus pattern.* The helical motion sweeps the flagellum through the field, so a static gradient arrives at the receptors as a **periodic modulation**, which entrains Ca²⁺ oscillations, which steer.

**That is epistemic action, at the scale of one cell.** The helix is not a side-effect of asymmetric beating that navigation tolerates — it is the sampling instrument. The cell **acts in order to generate the observation it cannot otherwise obtain**. This is NA-02's Expected Free Energy with the epistemic term doing visible work: a policy chosen not because it moves toward the goal — a helix is a *detour*, paid for in pitch per revolution — but because it **resolves uncertainty about the state**. Goal-only would swim straight and stay blind. And it is bounded as NA-08's Berg & Purcell (1977) scaling says: `δc/c ~ (D·a·c·T)^(−1/2)`. Precision costs integration time. **But be exact about what was measured.** Kashikar's 0.2–0.6 s window is a measured **Ca²⁺-response latency**, which the authors then *read* as a sampling time. Identifying that latency with Berg & Purcell's integration time `T` is **MODELED**, not measured: it assumes the latency is set by counting statistics rather than by transduction-cascade kinetics — which is not established, and which Kashikar's own electrotonic-blurring mechanism (next paragraph) arguably cuts against. Falsifier: show the latency scales with chemoattractant concentration as a counting-limited `T` predicts, rather than being fixed by transduction kinetics. The epistemic-action reading survives either way.

**Do not repeat the folk explanation.** The common framing — "a sperm is too small to sense a gradient across its own body, so it samples temporally" — is a **hypothesis**, and the measurements point elsewhere. Kashikar et al.'s stated mechanism is *electrotonic blurring*: the CNGK channel is distributed along the whole flagellum and hyperpolarisation spreads within milliseconds, so spatial information is smeared out. And Tan & Chiam (2018), *PLoS Comput Biol* 14(3):e1005966, model the choice and conclude it turns on **speed-to-size, not size** — noting explicitly that sperm are *relatively big* and use temporal sensing anyway because they are fast. Three claims, three evidence classes, never merged. The epistemic-action reading survives all three intact.

## Numbers: the redundancy, and what it is for

Median total sperm number in the WHO reference population is ~**255 × 10⁶ per ejaculate**; the 5th-centile lower reference limit is **39 × 10⁶** (Cooper et al. 2010, *Hum Reprod Update* 16(3):231–245; WHO 2021, 6th ed.). Williams et al. (1993), *Hum Reprod* 8(12):2019–2026, ligated and flushed both Fallopian tubes ~18 h after insemination in 10 women undergoing hysterectomy and recovered a **median of 251 spermatozoa (range 79–1,386)**.

**~10⁸ launched. ~10² arrive. Six orders of magnitude of attrition, measured.**

What is the redundancy *for*? **Carry the competing hypotheses; do not assert one.**

1. **Selection filter.** The tract screens: cervical mucus rejects poor morphology and motility, the oviductal reservoir binds preferentially (Sakkas et al. 2015, *Hum Reprod Update* 21(6):711–726). Redundancy is the input to a sieve.
2. **Raffle / numbers game.** Under sperm competition, fertilisation probability scales with your share of sperm at the ovum; more tickets, more chances (Parker's sperm-competition games). Redundancy is the bet.
3. **Transport loss.** Most sperm are simply lost mechanically. Redundancy compensates for a lossy channel and selects nothing.

These are not equivalent, and the human case does not obviously favour the raffle: relative testis mass is the classic discriminator (Harcourt et al. 1981, *Nature* 293:55–57 — chimpanzees, with multi-male mating, carry far more spermatogenic tissue than gorillas or orangutans), and humans sit intermediate-to-low. Sakkas et al. themselves hedge on whether the survivors are *better* or merely *there*. **Unresolved. Say so.**

## Transferable design rules

1. **Compute the regime before you sketch.** `Re`, then `Pe`, then everything else. A 0.45 Å coasting distance is a design constraint, not trivia.
2. **Find the theorem that forbids the obvious solution.** The paddle is the obvious solution and it scores exactly zero. Ask what the physics *forbids* before asking what it permits.
3. **Constraint is transmission.** Sliding became bending because something refused to let it slide. Where your design converts one quantity into another, check whether the converter is a *restraint* rather than a *mechanism*.
4. **Buy asymmetry cheaply.** All flagellar propulsion rides on a drag anisotropy of order **1.5–2**. Find the smallest asymmetry that breaks your symmetry and build on it.
5. **Distribute the supply, don't ship it.** Bolt the ATP factory to the fibrous sheath rather than diffuse ATP 50 µm. `L²/6D` decides this, not preference.
6. **Make the payload inert.** A cargo that is also a running process is two systems, both of which can fail.
7. **Act to see.** The helix costs pitch and buys the gradient. If your controller cannot observe the state, the correct policy may be one that *sacrifices progress to generate an observation*. That is the EFE epistemic term, and a single cell pays it.
8. **Never quote a rate without its condition.** 23 Hz and 11 Hz are the same cell.

## The numbers

**On two class labels used below.** Several rows are marked bare **`OBSERVED`** rather than `OBSERVED-REPLICATED`: they are *measured but not independently replicated*, and NA-00's class set has no value for that state — the bare-`OBSERVED` + parenthetical convention is the one already used in CN-08 and CN-10. **`NOT-SOURCED`** marks a number this pass could not trace to the primary it is attached to: neither confirmed nor refuted, and never to be read as measured. **Wing-level PENDING, surfaced not patched:** NA-00 declares "six classes and only six," while `encyclopedia/NATURE-LEDGER.md` — linked from the README as the governing document — **does not exist**, and at least three chapters already use classes outside the six. A chapter is the wrong place to mint a class, so the gap is named here. Falsifier: add an explicit unreplicated-observation value (and `NOT-SOURCED`) to the wing ledger, then re-class these rows to it.

> **CLOSED 2026-07-15 — the PENDING is discharged; this chapter's falsifier fired as written.** The
> paragraph above is the record as written and is **left unedited**; this note is appended. Two of
> its statements are now out of date: `encyclopedia/NATURE-LEDGER.md` **now exists**, and NA-00 **no
> longer declares "six classes and only six"** — the corpus refuted that at 72 of 919 rows.
>
> **This chapter's falsifier named both fixes, and both were made.** NA-00
> [Amendment 2026-07-15-A](../../encyclopedia/wing-NATURA/NA-00-how-to-read-this-wing.md#amendment-record-2026-07-15)
> registered **`OBSERVED-SINGLE`** (the explicit unreplicated-observation value) **and**
> **`NOT-SOURCED`** — exactly the pair this paragraph asked for. This chapter's 10 bare-`OBSERVED`
> rows are re-classed to `OBSERVED-SINGLE`; its `NOT-SOURCED` row keeps its string, now registered
> rather than out-of-vocabulary. **No value, source, or falsifier in this chapter changed.**
>
> **On `NOT-SOURCED`, which this chapter defined correctly before the vocabulary had a slot for it:**
> its gloss — *"a number this pass could not trace to the primary it is attached to: neither
> confirmed nor refuted, and never to be read as measured"* — is now the registered definition's
> core. NA-00 carries the distinction this chapter implied and made explicit: **NOT-SOURCED is an
> absence in *our homework*; NOT-MEASURED is an absence in *the literature*.** They may never be
> merged. **The chapter was right, and it was right first.**

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `u` | 62 (low visc) / 65 (high visc) | µm/s | migrating human sperm, 37 °C, n = 16 / 19 | OBSERVED-REPLICATED | Smith et al. 2009, *Cell Motil Cytoskeleton* 66(4):220–236, DOI 10.1002/cm.20345 | Repeat high-frame-rate imaging of the *migrating* cohort; a mean outside 40–90 µm/s refutes |
| `f_beat` | **23** (low visc) / **11** (high visc) | Hz | same cells, 37 °C; low-visc buffer vs ~0.14 Pa·s analogue | OBSERVED-REPLICATED | Smith et al. 2009 | A frequency independent of viscosity under the same conditions |
| `f_beat` | ~20 | Hz | human sperm, 37 °C, buffer ~0.7 mPa·s, tethered, n = 35 | OBSERVED-REPLICATED | Saggiorato et al. 2017, *Nat Commun* 8:1415, DOI 10.1038/s41467-017-01462-y | As above |
| `λ` | 39 (low visc) / 18 (high visc) | µm | human sperm flagellar wavelength, 37 °C | OBSERVED-REPLICATED | Smith et al. 2009 | Outside range at stated viscosity |
| `c_wave` | 890 (low visc) / 200 (high visc) | µm/s | wavespeed = f × λ | OBSERVED-REPLICATED | Smith et al. 2009 | Recompute; `c ≠ fλ` under stated conditions |
| `L_cell` | ~50–60 (head 4–5, midpiece ~7–8, tail ≥45) | µm | derived from WHO 2021 **normative morphometry criteria** — what counts as a *normal-form* spermatozoon — **not** a measured distribution over a population; used as an input to `Re` regardless | **NOT-MEASURED** *(in this pass; the criteria are normative, not a morphometric result)* | WHO 2021, *WHO laboratory manual…human semen*, 6th ed. | Fetch a primary morphometry study (e.g. a CASA/morphometric cohort) and print mean ± s.d. total length |
| `L_flag` | ~41 | µm | human flagellum, tethered-cell imaging | OBSERVED-REPLICATED | Saggiorato et al. 2017 | Independent measurement >1.5× off |
| `µ_buffer` | 0.7 (0.73 ± 0.01 for HTF) | mPa·s | aqueous buffer, **37 °C** | OBSERVED-REPLICATED | Saggiorato et al. 2017 | Rheometry outside range at 37 °C |
| `µ_mucus` | ~0.14 (analogue) / ~0.2 (midcycle, Day 0) / ~0.68 (Day 5) | Pa·s | Maxwell fit to measured G′/G″ at ~5 Hz, 37 °C | **MODELED** | Smith et al. 2009 (rheometry + fit); mucus moduli from Wolf et al. 1977, *Fertil Steril* 28:47–52 | A direct steady-shear viscosity of periovulatory mucus outside 0.1–1 Pa·s |
| `Re` | **4.9 × 10⁻³** (bracket 2–6 × 10⁻³) | dimensionless | human sperm, `ρuL/µ`; ρ=10³, u=6.2e−5, L=5.5e−5, µ=7.0e−4 (SI) | **MODELED** | Computed here from Smith 2009 + Saggiorato 2017 + WHO 6th ed; regime per Purcell 1977, *Am J Phys* 45:3–11 | Arithmetic error, or any input refuted under its stated condition |
| `Re_mucus` | ~2.6 × 10⁻⁵ | dimensionless | `ρuL/µ`; ρ=10³, **u = 6.5e−5 (65 µm/s — the high-viscosity migrant velocity, Smith 2009; NOT the 6.2e−5 used for `Re`)**, L=5.5e−5, µ = 0.14 Pa·s (SI) | **MODELED** | Computed here | Recompute. At u = 6.2e−5 the value is **2.4 × 10⁻⁵** — the input swap is named because the scope must not read "same" next to a number that needs a different input; the exponent is unmoved either way |
| `d_coast` | **~0.45 Å (4.5 × 10⁻¹¹ m)**, τ ≈ 0.7 µs | m | Stokes coasting, `τ=m/(6πµa)`; V≈17 µm³, ρ_cell≈1.1×10³, a≈2 µm | **MODELED** | Computed here (inputs order-of-magnitude) | Recompute; a measured coasting distance >1 nm refutes |
| `ζ⊥/ζ∥` | **≈2 asymptotic only**; **~1.5–1.8** at realistic aspect ratios. `ζ⊥/ζ∥ = 2(ln(2λ/a) − 0.5)/(ln(2λ/a) + 0.5)` — strictly **< 2** for any real filament, → 2 as aspect ratio → ∞ | dimensionless | **resistive-force-theory coefficient**, slender filament, far from a boundary — a derived coefficient, not a measurement | **MODELED** *(slenderness is the fence)* | Gray & Hancock 1955, *J Exp Biol* 32:802–814 | A slender-body or numerical computation giving a ratio outside 1.4–2.0 at flagellar aspect ratios |
| `n_dynein` | ~67,500 total; ~15,000 active/beat | motors | sea-urchin sperm flagellum; active count is a **hypothesis** (67,500 × 2/9) | OBSERVED-REPLICATED (total, cryo-ET) / **HYPOTHESIZED** (active fraction) | Chen et al. 2015, *Biophys J* 109:2562–2573, DOI 10.1016/j.bpj.2015.11.003, and refs therein | Count in situ; an active fraction ≠ ~2/9 |
| `d_dynein` | ~8 | nm/power stroke | axonemal dynein, single-molecule | OBSERVED-REPLICATED | Chen et al. 2015 and refs therein | Different step periodicity |
| axoneme extension on trypsin + ATP | — (the "five or more times original length" previously printed here is **withdrawn as unsourced**; secondary accounts conflict: several-fold / ~7× / nine-fold) | fold of original length | demembranated sea-urchin axoneme, brief trypsin digestion, + ATP | **NOT-SOURCED** | Summers & Gibbons 1971, *PNAS* 68(12):3092–3096 — extension figure not read in this pass; Lindemann & Mitchell, *Mol Biol Cell* 2018 (50-yr review) recounts the experiment and gives no figure | Read S&G 1971 pp. 3092–3096 and print the extension factor |
| `n_ATP/beat` | **(2.3 ± 0.2) × 10⁵** (low visc) → **(3.2 ± 0.5) × 10⁵** (0.5 % MC) | ATP/beat | **demembranated** sea-urchin sperm axoneme, single-cell, [ATP] = 20 µM, **viscosity as stated — this quantity is *not* viscosity-independent** | **OBSERVED-SINGLE** *(single study)* | Chen et al. 2015 | Bulk *S. purpuratus* gives ~1 × 10⁵/beat — **already a 2.3× discrepancy; carry it** |
| `r_ATP` | (2.4 ± 0.3) × 10⁶ active; (9.2 ± 0.2) × 10⁵ inactive | ATP/s | demembranated *Lytechinus* sperm axoneme | **OBSERVED-SINGLE** *(single study)* | Chen et al. 2015 | Independent single-cell measurement >2× off |
| `ε_hydro` | **0.004** (low visc) → **0.013** (high visc) | dimensionless | demembranated sea-urchin axoneme, 20 µM ATP, buffer vs 0.5 % MC | **OBSERVED-SINGLE** *(single study — not replicated)* | Chen et al. 2015, Table S1 | Independent replication >3× off; **not** transferable to intact human sperm |
| `ε_chemo` | 0.34 → 0.6 | dimensionless | as above | **OBSERVED-SINGLE** *(single study — not replicated)* | Chen et al. 2015 | As above |
| `ε_swim` | **0.001** → **0.008** | dimensionless | as above; `ε_swim = ε_chemo · ε_hydro` | **OBSERVED-SINGLE** *(single study — not replicated)* | Chen et al. 2015 | As above |
| `ε_hydro,human` | — | dimensionless | intact human spermatozoon | **NOT-MEASURED** | not sourced in this pass | Measure ATP turnover + kinematics on one intact human cell |
| `n_mito` | ~50–75 (~1 mtDNA each) | per cell | human sperm midpiece | **OBSERVED-SINGLE** *(via review; primary count not retrieved in this pass)* | Hirata et al. 2002, *Reprod Med Biol* 1(2):41–47, DOI 10.1046/j.1445-5781.2002.00007.x | Direct EM/qPCR count outside range |
| glycolysis vs OXPHOS | mouse: glycolysis (GAPDHS) required despite intact mitochondria; human: **unsettled** | — | Gapds⁻/⁻ mice infertile, sluggish, no forward progression | **OBSERVED-CONTESTED / species-dependent** | Miki et al. 2004, *PNAS* 101(47):16501–16506; framed vs human in Ford 2006, *Hum Reprod Update* 12(3):269–274 | A human-sperm study settling the dominant pathway under physiological substrate |
| histone retention | **~5–15 %** (human) vs **~1 %** (mouse) | % of nucleoproteins | sperm chromatin | **OBSERVED-CONTESTED** (the human range is itself disputed) | Balhorn 2007, *Genome Biol* 8(9):227 | A method reconciling the spread; do not average |
| chromatin compaction | **~10× vs the somatic interphase nucleus**; **≥6× vs mitotic chromosomes**. The **"up to 20×"** upper bound previously printed here is **NOT-SOURCED** — not confirmed, not refuted | fold | protamine-packaged sperm chromatin; **two distinct comparators — carry both, do not average them into one range** | **OBSERVED-SINGLE** *(via review; primary comparator study not retrieved)* | Balhorn 2007, *Genome Biol* 8(9):227 | Fetch the primary study that measured the ratio, name its comparator, and print it; a measured packing ratio outside range refutes |
| toroid | ~50 (up to ~60) | kb DNA per toroid | protamine–DNA toroid | OBSERVED-REPLICATED | Hud et al. 1995, as reviewed in Balhorn 2007; **single-molecule receipt for the toroid *mechanism*** (λ-phage DNA in an optical trap — not sperm chromatin, not a compaction ratio): Brewer, Corzett & Balhorn 1999, *Science* 286(5437):120–123 | Structural measurement outside range |
| resact sensitivity | **1** bound molecule evokes a Ca²⁺ response; 50–100 saturate | molecules | *Arbacia punctulata* sperm | OBSERVED-REPLICATED | Kaupp et al. 2003, *Nat Cell Biol* 5:109–117 | Single-molecule response fails to replicate |
| min. gradient | **0.8** | fM/µm | *A. punctulata*, resact | **OBSERVED-SINGLE** *(single group — not independently replicated)* | Kashikar et al. 2012, *J Cell Biol* 198(6):1075–1091, DOI 10.1083/jcb.201204024 | Independent measurement >10× off |
| `T_sample` | **0.2–0.6** | s | *A. punctulata*, **measured Ca²⁺-response latency**, which the authors read as a sampling window. Equating it with Berg & Purcell's integration time `T` is a **MODELED** identification, not an observation | **OBSERVED-SINGLE** *(single group)* — the latency; **MODELED** — its identification with `T` | Kashikar et al. 2012 | Independent measurement >10× off. For the `T` identification: show the latency scales with chemoattractant concentration as a counting-limited `T` predicts, rather than being fixed by transduction kinetics |
| slope threshold | ~2.6–3 × 10⁻³ | µm⁻¹ (relative steepness) | *S. purpuratus*, speract, ~10⁻⁹ M regime; a **predicted detection limit**, not a measured threshold (`γmin = ξmax* ~ 2.6×10⁻³ µm⁻¹`, derived; sweep 10⁻¹¹–10⁻⁶ M) | **MODELED** | Ramírez-Gómez et al. 2020, *eLife* 9:e50532 (theoretical detection-limit derivation) | A measured chemotactic response below the predicted slope threshold, or a measured threshold >3× off the prediction |
| helix | r = **8.4 ± 3.1** µm; period **0.38 ± 0.07** s; pitch **47.6 ± 9.1** µm; u = **200 ± 57** µm/s | — | *A. punctulata*, free 3-D swimming **far from boundaries with NO gradient present** (the unstimulated baseline, not a chemoattractant condition), holographic tracking, **n = 20**, 1 s tracks | OBSERVED-REPLICATED | Jikeli et al. 2015, *Nat Commun* 6:7985, DOI 10.1038/ncomms8985 | Independent 3-D tracking outside stated s.d. |
| human chemotaxis | progesterone → CatSper → Ca²⁺ influx **replicated**; progesterone as *the* chemoattractant **disputed** | — | human sperm | **OBSERVED-CONTESTED** | Strünker et al. 2011, *Nature* 471:382–386; Lishko et al. 2011, *Nature* 471:387–391; contested per charcoal-stripping studies | A pre-registered in-vivo-relevant assay settling it |
| thermotaxis | ~2 °C between the **isthmus** (reservoir) and the **isthmic–ampullary junction** (fertilisation site) — rabbit, **anatomical, no distance attached**. The **"over 20 mm"** and **">50 % accumulate warm-side"** previously printed here are **withdrawn: NOT-SOURCED** to Bahat 2003 | — | capacitated mammalian sperm — **questioned** (convection confound) | **OBSERVED-CONTESTED** (the ~2 °C anatomical difference) / **NOT-SOURCED** (the assay gradient length and the accumulation fraction, in this pass) | Bahat et al. 2003, *Nat Med* 9:149–150 (brief communication; no abstract indexed on PubMed); questioned in Miki & Clapham 2013, *Curr Biol* 23:443–452 | Read Bahat et al. 2003's methods and print the chamber gradient in °C/mm and the accumulation fraction; separately, a convection-controlled replication |
| `N_ejac` | median ~**255 × 10⁶**; 5th-centile **39 × 10⁶** | sperm/ejaculate | WHO reference population (TTP ≤ 12 months) | OBSERVED-REPLICATED | Cooper et al. 2010, *Hum Reprod Update* 16(3):231–245; WHO 2021, 6th ed. | Re-derive from the reference cohort |
| `N_tube` | median **251** (range **79–1,386**) | sperm in both Fallopian tubes | 10 parous women, ~18 h post-insemination, tubes ligated + flushed | **OBSERVED-SINGLE** *(single study, n = 10 — not replicated)* | Williams et al. 1993, *Hum Reprod* 8(12):2019–2026 | An independent flush study giving a median outside ~50–2,000 |
| attrition | ~10⁶-fold (10⁸ → 10²) | fold | ejaculate → tube | **MODELED** | Computed here from the two rows above | Either input row refuted |
| acrosin | KO **mice fertile**; KO **hamsters completely infertile** (zona-penetration defect; zona-free oocytes all fertilised) | — | targeted mutants | OBSERVED-REPLICATED | Hirose et al. 2020, *PNAS* 117(5):2513–2518, DOI 10.1073/pnas.1917595117 (citing Baba et al. 1994 for the mouse) | A third species contradicting both |
| `δc/c` scaling | ∝ `(D·a·c·T)^(−1/2)` | dimensionless | diffusion-limited chemoreception — see NA-08 for the **contested prefactor** | OBSERVED-REPLICATED (as a scaling) | Berg & Purcell 1977, *Biophys J* 20:193–219 | A sensor beating the −1/2 exponent |

## Falsifier (operable)

This chapter's central structural claim — **that the flagellum's travelling wave is forced by the low-Reynolds-number regime rather than chosen among alternatives, and that any reciprocal (time-reversible) stroke would deliver exactly zero net displacement in a Newtonian fluid** — is refuted by exhibiting **one microswimmer that achieves sustained net progression in a Newtonian fluid at Re < 10⁻² using a strictly reciprocal shape sequence (one degree of freedom, forward path = time-reverse of return path), with the medium's Newtonian rheology measured and reported, and inertial, boundary, and hydrodynamic-interaction effects excluded.** Non-Newtonian media do not count — Lauga (2011) already lists viscoelasticity as a legitimate escape, and cervical mucus is viscoelastic; that escape is inside the theory, not a refutation of it.

Row-local falsifiers are printed in the table. A refuted row moves that row. A refuted scallop theorem moves the chapter.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **"Kamikaze sperm": that a large fraction of the ejaculate is a specialised non-fertilising caste that blocks or kills rival sperm.** — **NEGATIVE, with a receipt.** Moore, Martin & Birkhead (1999), *Proc R Soc B* 266(1436):2343–2350, mixed ejaculates from different males in combination and looked for exactly the predicted effects (differential mortality, agglutination, morphological damage). They found **very few significant changes** in sperm aggregation or performance between different-male and same-male mixtures, and **none consistent with the previously reported findings**; they concluded that incapacitation of rival sperm "seems an unlikely mechanism of sperm competition in humans". The hypothesis made a testable prediction, the test was run, the prediction did not reproduce. **Match the wording to the source:** "very few significant changes … none *consistent with*" is not "none" — some signal was seen, and the authors' claim is that none of it reproduced the predicted pattern, which is why their own summary hedges to *unlikely* rather than *refuted*. (The donor count — often given as 15 men — is **NOT-SOURCED in this pass**; falsifier: read the methods and print *n*.) Recorded because it is the *good* outcome of the method, and because the idea still circulates in popular accounts as though it had survived. This bullet exists to celebrate honesty about a negative result, so it is the one place the wording must match the source exactly.
- **"Sperm race to the egg and the fastest wins."** — **INADMISSIBLE as stated.** It names no falsifier: "fastest" is unmeasured in vivo, the tract is not a racecourse, and Smith et al. 2009 observed a 34 µm/s spread in progressive velocity among high-viscosity migrants that their kinematic parameters **did not explain**. The competing accounts (filter / raffle / transport loss) are printed above and remain unresolved. The race narrative is a story fitted to the outcome.
- **NEGATIVE / conflation trap:** quoting sperm beat frequency without viscosity and temperature. 23 Hz and 11 Hz are the *same cells at the same temperature* (Smith et al. 2009). Any single-number citation is wrong under half its readings.
- **NEGATIVE / conflation trap:** quoting `ε_hydro ≈ 0.4–1.3 %` or `2.3 × 10⁵ ATP/beat` as properties of *human sperm*. They are properties of **demembranated sea-urchin axonemes reactivated at 20 µM ATP** — and `2.3 × 10⁵` carries one further condition that is easy to drop precisely because it sits next to a low/high-viscosity table: **viscosity**. It is the *low-viscosity* value, rising to **(3.2 ± 0.5) × 10⁵ in 0.5 % methylcellulose**. Quoting it bare drops the species, the membrane, the [ATP] **and the load**. Chen et al.'s own paper prints a 2.3× disagreement with the earlier bulk *S. purpuratus* figure (~1 × 10⁵ ATP/beat) — the constant is not settled even within the species.
- **NEGATIVE / inference trap:** "the midpiece mitochondria power the flagellum." Miki et al. 2004 knocked out glycolysis and got infertile, non-progressive sperm **with mitochondrial function intact**. The obvious anatomical inference was wrong in the mouse — and the human case is still **unsettled**, so neither pathway may be asserted for humans.
- **HYPOTHESIZED, commonly stated as fact:** "sperm sample temporally *because* the cell is too small to read a gradient across its body." The mechanism Kashikar et al. (2012) actually report is **electrotonic blurring** (CNGK distributed along the flagellum; hyperpolarisation spreads in milliseconds). Tan & Chiam (2018) model the choice and conclude sperm are **relatively big** and use temporal sensing because they are **fast**. Three claims, three classes. The folk version is recorded here as unearned in the form usually given.
- **NOT-MEASURED in this pass:** hydrodynamic efficiency of an intact human spermatozoon; total ATP expended by one human sperm over the whole journey; a primary morphometric source for human sperm total length (the WHO criteria are **normative classification criteria, not a measured distribution**, and are named as such — the `L_cell` row is classed NOT-MEASURED for exactly this reason, and it is an input to the headline `Re`); the unsteady/oscillatory Reynolds number under a stated length convention (it is **convention-dependent** — flagellar radius vs flagellum length give answers orders of magnitude apart — and is therefore not printed rather than printed wrongly).
- **NOT-SOURCED in this pass** (a number was previously printed here and could not be traced to the primary it was attached to; **withdrawn, not replaced with a guess** — each is neither confirmed nor refuted): the **20 mm** gradient length and the **>50 % warm-side accumulation** attributed to Bahat et al. 2003; the **five-or-more-fold** axoneme extension attributed to Summers & Gibbons 1971; the **20×** upper bound on sperm-vs-somatic chromatin compaction; the **15 men** donor count attributed to Moore, Martin & Birkhead 1999. Each carries its own falsifier in the row or bullet above, and every one of them is discharged the same way: **open the primary and read the figure.** Recorded as a class because the pattern matters more than any single row — a plausible number welded to a real citation is the defect this chapter's own rail names worst, and four of them survived to this pass.

## HONEST FENCE — MODELED

This chapter is fenced **MODELED**. Individual rows are OBSERVED-REPLICATED, bare OBSERVED (measured, unreplicated), OBSERVED-CONTESTED, MODELED, NOT-SOURCED and NOT-MEASURED — read each row's own class, not this fence. But the *chapter as an artifact* is a design budget: it composes measured constants through stated assumptions — Newtonian `ρ` and `µ` for a viscoelastic in-vivo medium; a cell length from morphometric *criteria* rather than a primary morphometry paper; an effective sphere radius `a ≈ 2 µm` for a shape that is not a sphere; order-of-magnitude cell volume and density for the coasting estimate. **The assumptions are the fence.** They move `Re` and `d_coast` by factors of a few. They cannot move the exponent, which is the load-bearing part: `Re ~ 10⁻³` and `d_coast ~ 10⁻¹¹ m` survive any plausible revision of the inputs.

**A standing disagreement inside this chapter — carried, not averaged.** Three flagellar lengths appear above and they do not reconcile: `L_flag` = **41 µm** (Saggiorato et al. 2017 — **measured**, tethered human cells) vs **tail ≥ 45 µm** (WHO 2021 — **normative criteria**, not a measurement), which is what feeds `L = 55 µm` into the headline `Re`, vs a **50 µm** flagellar cylinder used in the coasting-volume estimate. The only *measured* length of the three sits **below** the criteria floor and implies a total cell length of ~46 µm, not 55 µm — a ~10 % disagreement. If Saggiorato's length is right, the printed `Re` is **~20 % high** and the coast estimate's volume is ~10 % high. This chapter carries Chen's 2.3× ATP disagreement and Balhorn's histone-retention spread rather than averaging them; the same rule applies here, and it was silently missing until this pass. As with `ρ` and `µ`: **the exponent survives either way**, and the exponent is the load-bearing part.

Per **Gould & Lewontin (1979), "The Spandrels of San Marco and the Panglossian Paradigm"**: none of this establishes that the spermatozoon is an optimum. Drift, phylogenetic inertia, developmental constraint, pleiotropy and frozen accidents produce features that solve nothing — and this chapter contains a live candidate: `ε_hydro ≈ 0.4–1.3 %` is *terrible*, and Chen et al. found it goes **up** in high-viscosity media that sea-urchin sperm never encounter, which they themselves call counterintuitive. **Nature's authority here is precise and limited: it already ran a very long parallel search under real physical constraints in which the failures were deleted.** That makes convergence evidence of a constraint-optimum and makes every number above a **hypothesis generator**. It does not make any of them a proof. Per repo rule **M7**, a biomimetic design taken from this chapter must beat a **tuned conventional baseline** on a **pre-registered metric**, with a discriminator that collapses the gain, or it is recorded **NEGATIVE**.

## Not claimed

- **Not claimed:** that a sperm decides, wants, seeks, knows, or navigates in any sense involving experience. "Epistemic action" here is a *statistical* description — a policy whose selection weight includes an uncertainty-resolving term. The helix is a sampling geometry. Nothing above bears on whether anything is like anything.
- **Not claimed:** that any citation raises any UNI rung. **A nature citation is NEVER a UNI gate.** Reading Purcell 1977 does not make any UNI claim proven, designed, or built. The NATURA classes (OBSERVED-REPLICATED / OBSERVED-CONTESTED / MODELED / HYPOTHESIZED / INADMISSIBLE / NOT-MEASURED) and the UNI ledger's four values (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. **This chapter contains zero UNI claims.**
- **Not claimed:** that human sperm perform chemotaxis. The Ca²⁺ physiology is replicated; the guidance claim is contested and is carried as contested.
- **Not claimed:** that the scallop theorem governs the female reproductive tract. Its Newtonian premise is violated there, and the violation is a *named escape route* in Lauga (2011), not an oversight.
- **Not claimed:** that the sea-urchin efficiency and ATP numbers transfer to humans. They are printed with their species, their demembranation state, and their [ATP].
- **Not claimed:** that the attrition figure resolves *why* the redundancy exists. Three hypotheses are printed and none is selected.
- **Not claimed:** that this design is optimal, or that "nature does it this way" is an argument. See the Gould & Lewontin fence — and note the 1 % hydrodynamic efficiency sitting in the table as a standing counterexample to reading this cell as an optimised propeller.
- **QUAESTIO-APERTA:** "full human" and "beyond human" appear nowhere in this chapter as a target, milestone, or deliverable. They are permanent open questions, and the design of a delivery vehicle has no bearing on them.
