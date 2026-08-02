# NA-07 — The dimensionless numbers: the cross-scale design toolkit

> **What you are reading.** The tool that carries a design from a bacterium to a whale without
> lying. A dimensionless group is a *ratio of two competing effects* — the honest currency of scale.
> Two systems sharing the relevant groups are in the same regime, whatever their size. Everything
> here is nature's measured regularity, resting on published literature. **A nature citation is
> never a UNI gate.** This chapter raises no rung of the UNI ledger and never will.

---

## Why a group and not a number

A dimensioned quantity can never be a universal law, because its numerical value changes when you
change the unit. "This wing flaps at 5 Hz" tells you nothing about a wing of a different size. Only
a ratio is scale-free. That sentence is the whole chapter — and it is also the rigorous, earned
version of most claims about "universal frequencies of nature" (see INADMISSIBLE, where it does real
work).

Each group below carries: formula, symbols with units, what it is a ratio *of*, critical values
**with their scope**, a real example with numbers, and its limit.

---

## Reynolds — Re = ρuL/μ = uL/ν

**Ratio of:** inertial to viscous forces. ρ = density [kg m⁻³]; u = speed [m s⁻¹]; L = length [m];
μ = dynamic viscosity [Pa·s]; ν = μ/ρ = kinematic viscosity [m² s⁻¹].

The source is Purcell (1977), *Life at Low Reynolds Number*, Am. J. Phys. **45**:3–11. He writes Re
as `avρ/η` or `av/ν`, with ν ≈ 10⁻² cm² s⁻¹ for water, and gives: a man swimming "might be 10⁴"; a
goldfish or tiny guppy "might get down to 10²"; microorganisms "about 10⁻⁴ or 10⁻⁵."

Check it with his own inputs (a ≈ 1 μm, v ≈ 30 μm s⁻¹, ν = 10⁻² cm² s⁻¹):

    Re = av/ν = (10⁻⁴ × 3×10⁻³) / 10⁻² = 3×10⁻⁵     ✓ inside his stated band

**What that costs.** Stop pushing a bacterium and it coasts "about 0.1 angstrom," taking "about 0.6
microsec to slow down." Inertia is not small — it is *absent*: "what you are doing at the moment is
entirely determined by the forces that are exerted on you at that moment, and by nothing in the past."

**The scallop theorem.** Drop inertia from Navier–Stokes and the equation is time-reversible, so a
one-hinge swimmer exactly retraces its path: "the scallop at low Reynolds number is no good. It can't
swim because it only has one hinge, and if you have only one degree of freedom in configuration space,
you are bound to make a reciprocal motion." You need ≥2 degrees of freedom — a loop in configuration
space. **This is why a sperm cannot swim like a fish**: a fish's reciprocating tail-beat works because
inertia stores the stroke; a sperm has no inertia to store, so it runs a *travelling wave* down its
flagellum (cross-ref CN-06). Purcell's intuition calibration: put a man "in a swimming pool that is
full of molasses" and forbid any body part to move faster than 1 cm min⁻¹.

**Critical value, with scope.** Pipe transition is textbook-quoted at Re ≈ 2300, but this is genuinely
refined. Avila et al. (2011), *The Onset of Turbulence in Pipe Flow*, Science **333**:192–196, locate
the onset of *sustained* turbulence at **Re_c = 2040 ± 10**, where mean puff-decay time equals mean
puff-splitting time. The two numbers answer different questions; citing "2300" without saying which is
sloppy. Scope: smooth circular pipe only — it does not transfer to a wing or an artery.

**Limit:** Re presumes you named the right L and u. **A Re without a stated L is not a number.**

---

## Péclet — Pe = uL/D

**Ratio of:** advection to diffusion. D = diffusion coefficient [m² s⁻¹].

**Why circulation exists.** Purcell derives this group and does not know its name: "I'm sure this
ratio has someone's name but I don't know the literature... Call it S for stirring number, it's just
lv/D." It is the Péclet number. For D ≈ 10⁻⁵ cm² s⁻¹ (small molecule in water) at micron scale he
gets **S ≈ 10⁻²**:

    Pe = lv/D = (10⁻⁴ × 3×10⁻³) / 10⁻⁵ = 3×10⁻²     ✓ reproduces his figure

**The consequence is severe.** At Pe ≪ 1 stirring is useless: "this bug can't do anything by stirring
its local surroundings... You can thrash around a lot, but the fellow who just sits there quietly
waiting for stuff to diffuse will collect just as much." Solving diffusion in a Stokes flow field, he
finds that to raise intake **10%** the cell must swim **700 μm s⁻¹ — ~20× faster than it can** —
because intake rises only as √v.

**The crossover is the design number.** Advection beats diffusion beyond **L\* = D/u**: "you go that
magic distance, D/v... for typical D and v, you have to go about 30 μm and that's just about what the
swimming bacteria were doing."

    L* = D/v = 10⁻⁵ / 3×10⁻³ = 33 μm     ✓ matches his ~30 μm

The bacterium swims not to *stir* but to **outrun diffusion** — to sample a different neighbourhood.
Every organism above ~1 mm needs a pump because diffusion cannot serve a body once L ≫ D/u.

**Limit:** D is species-specific. Pe for oxygen ≠ Pe for a protein in the same flow.

---

## Damköhler — Da

**Ratio of:** reaction rate to transport rate. **Da_I = k·τ** (τ = residence time [s]);
Da_II = kL²/D compares reaction to diffusion.

Da ≪ 1 → **reaction-limited** (chemistry is the bottleneck; stirring does nothing). Da ≫ 1 →
**transport-limited** (reagent consumed at the surface; the problem is delivery, not catalysis).
Da ≈ 1 → both matter; model, don't estimate.

**It pairs with Pe:** a cell with a fast enzyme (Da ≫ 1) and no circulation (Pe ≪ 1) starves *no
matter how good the enzyme is*. Optimising the catalyst when the system is transport-limited is the
most common design error at any scale.

**Limit:** presumes one dominant reaction and one dominant transport path.

---

## Froude — Fr = v²/(gL)

**Ratio of:** inertial to gravitational forces. g = 9.81 m s⁻²; L = hip height (gait) or waterline
length (hulls). **Some authors use Fr = v/√(gL) — one is the square of the other. A Froude number
without its convention stated is defective.**

Alexander (1976), *Estimates of speeds of dinosaurs*, Nature **261**:129–130, used dynamic similarity
— animals of different size move similarly at equal Fr — to read speed off a trackway:

    v = 0.25 · g^0.5 · SL^1.67 · h^(−1.17)

with SL = stride length [m], h = hip height [m] ≈ **4 × footprint length**. Estimated dinosaur speeds:
**1.0–3.6 m s⁻¹** — notably slow.

**This is OBSERVED-CONTESTED and must be carried as such.** The formula's validity on *compliant*
substrates — mud, which is exactly what preserves a trackway — is disputed; recent work reports
trackway speeds are not validated by extant birds on compliant substrates, implying the classic method
**overestimates** speed (2025, PMC12187409). Carry both positions (cross-ref NA-06, CN-08).

**Limit:** Fr similarity assumes gravity-dominated dynamics and geometric similarity. It says nothing
about elastic storage — Fr cannot see a kangaroo's tendon spring.

---

## Strouhal — St = fA/U

**Ratio of:** oscillatory to forward speed. f = beat frequency [Hz]; A = peak-to-peak amplitude [m];
U = cruise speed [m s⁻¹].

Taylor, Nudds & Thomas (2003), *Flying and swimming animals cruise at a Strouhal number tuned for high
power efficiency*, Nature **425**:707–711: efficiency peaks over a narrow band and cruising animals sit
in it — **0.2 < St < 0.4** for dolphins, sharks and bony fish; birds, bats and insects at cruise are
constrained similarly.

**This is the strongest cross-taxon convergence in this chapter — which is exactly where Gould &
Lewontin bites.** Convergence across independent lineages is evidence of a constraint-optimum; it is
*not* proof that any given animal's St is an adaptation rather than a by-product of wing inertia. The
claim's scope is "at cruise" — not takeoff, not manoeuvre.

**Scope matters.** Bush & Hu (2006), *Walking on Water*, Annu. Rev. Fluid Mech. **38**:339–369, report
a *different* band for water-walkers: **0.1 < St < 1** (large), **0.01 < St < 0.1** (arthropods). Same
symbol, different regime. Do not transfer 0.2–0.4 outside cruise.

**Limit:** presumes steady cruise; silent about unsteady manoeuvre.

---

## Womersley — α = R√(ωρ/μ)

**Ratio of:** transient (oscillatory) inertia to viscous shear. R = vessel radius [m]; ω = 2πf
[rad s⁻¹].

Human values: ascending aorta **α ≈ 13.2** (≈20.3 taken as characteristic in some studies); carotid
**≈4.4**; capillaries **≈0.005** (arterioles, capillaries, venules all α < 1). Source: Womersley-number
literature survey, *Cardiovasc. Eng. Technol.* (2024), doi 10.1007/s13239-024-00723-4.

**Read the physics off the number.** At α ≫ 1 (aorta) flow is inertia-dominated with a *blunt,
plug-like* profile lagging the pressure gradient — a pulsatile, wave-carrying elastic reservoir. At
α ≪ 1 (capillary) flow is quasi-steady and Poiseuille-like, parabolic and in phase — **the capillary
does not know the heart is beating.** Same fluid, same pump, two regimes, one number.

**Limit:** assumes a Newtonian fluid in a rigid tube. Blood is shear-thinning, vessels are compliant,
and in capillaries the red cell is comparable to the vessel diameter — continuum blood is arguably the
wrong model there entirely.

---

## Weber and Bond/Eötvös — We = ρU²w/σ ; Bo = ρghw/σ

**Ratio of:** We = inertia to surface tension; Bo = gravity to surface tension. σ = surface tension
[N m⁻¹] (air–water ≈ 0.07); w = leg width [m]. (Conventions per Bush & Hu 2006.)

**The capillary length is the crossover:** ℓ_c = (σ/ρg)^(1/2) **≈ 2.6 mm** (Bush & Hu 2006). Below it
surface tension dominates gravity; above it, gravity wins. **This is why an insect's world and a
human's world are different worlds.**

**Why water striders work.** Hu, Chan & Bush (2003), *The hydrodynamics of water strider locomotion*,
Nature **424**:663–666: striders are "insects of characteristic length 1 cm and weight 10 dynes"
(10⁻⁴ N), supported by surface tension from curvature of the free surface. From the paper's own numbers
the required leg contact length is

    L_contact = W/σ = 10⁻⁴ N / 0.07 N m⁻¹ ≈ 1.4 mm

— trivially available on a 1 cm insect. Criteria (Bush & Hu 2006): **Bo < 1** → supported by surface
tension; **We < 1** → the driving leg's meniscus survives, satisfied by all water-walking insects
**apart from the galloping fisher spider** (carry the exception — it is real). They report the fit
**Bo ∼ We** across water walkers.

Hu, Chan & Bush resolve **Denny's paradox** (infant striders should be unable to propel themselves):
striders transfer momentum "not primarily through capillary waves, but rather through hemispherical
vortices shed by their driving legs." The paradox arose from the minimum capillary wave speed
**c_m = 23 cm s⁻¹** (Lighthill 1979, via Bush & Hu 2006), below which steady motion radiates no waves.

**Why an insect drowns in a droplet — the real forces.** Bush & Hu (2006): water-walking insects "weigh
no more than 1–10 dynes and have total body perimeter of order 1 cm," so crossing the air–water
interface "would require that they generate forces of order **10–100 times their weight**." The surface
is not a nuisance to an insect — it is a wall. Hydrophobic leg microstructure is the adaptation that
keeps it from ever having to cross.

**Limit:** σ collapses with surfactant. A drop of detergent sinks a strider — also the cleanest
falsification test of the whole account.

---

## Knudsen — Kn = λ/L

**Ratio of:** molecular mean free path to system size. **Where "fluid" stops being a fluid.** λ ≈ 68 nm
for air at 1 atm, 25 °C (standard kinetic theory).

**Regimes (gas flows):** continuum Kn < 0.01 (Navier–Stokes, no-slip); slip 0.01–0.1 (Navier–Stokes
usable *if* slip boundary conditions are added); transition 0.1–10 (kinetic theory required);
free-molecular > 10 (molecules collide only with walls).

**The lung.** An alveolus is ~200 μm: Kn = 68×10⁻⁹/200×10⁻⁶ ≈ 3.4×10⁻⁴ → **continuum**; deep-lung air
is an ordinary fluid. But a 100 nm aerosol particle in that same alveolus sees Kn ≈ 0.7 →
**transition regime**: Stokes drag is wrong without the Cunningham slip correction. **Same air, same
lung, two regimes — because Kn depends on the L you are asking about, not on the fluid.** (Arithmetic
mine; MODELED.)

**Limit:** a gas concept. Liquids have no comparable mean free path.

---

## Deborah — De = t_relax / t_observe

**Ratio of:** the material's relaxation time to your observation time. Reiner (1964), *The Deborah
Number*, Physics Today **17**(1):62, doi 10.1063/1.3051374.

**De ≫ 1 → behaves as a solid. De ≪ 1 → behaves as a liquid.** Not "appears to" — *behaves as*. Pitch,
silly putty, glacial ice, the Earth's mantle: each is solid or liquid depending entirely on how long
you watch.

**This is the earned, rigorous version of "everything depends on the timescale."** In this form it is a
defensible statement of continuum mechanics with a falsifier. Without the ratio it is a slogan. That
difference is the entire discipline of this wing.

The correct reading is not "solidity is subjective." It is sharper: *solid* and *liquid* are not
properties of a material at all — they are properties of the **pairing** of a material with an
observation timescale. The material supplies one honest number (t_relax); you supply the other.
Purcell's mantle figure makes it concrete — viscosity "of 10²¹ P" is why the mantle is a solid to a
seismic wave and a fluid to a continent. Note what this does *not* license: De is a statement about
material response, not a warrant for treating any timescale claim as earned merely because timescales
are involved.

**Limit:** presumes a *single* dominant relaxation time. Real polymers and tissues have a broad
relaxation *spectrum*; one De is then a summary, not a description.

---

## The rest of the kit

| Group | Formula | Ratio of | One example |
|---|---|---|---|
| **Prandtl** Pr | ν/α | momentum to thermal diffusivity | 7 (water), 0.71 (air), 0.025 (mercury). Pr ≪ 1 → heat outruns momentum; thermal boundary layer *thicker* than velocity layer. |
| **Schmidt** Sc | ν/D | momentum to mass diffusivity | Pr's mass-transfer twin. Sc ≫ 1 in liquids: momentum spreads far faster than solute. |
| **Nusselt** Nu | hL/k_fluid | total to conductive heat transfer | Nu = 1 → pure conduction, no convective benefit. Nu is the *answer* you measure, not an input. |
| **Sherwood** Sh | k_c L/D | total to diffusive mass transfer | Nu's twin. Sphere in stagnant fluid: Sh = 2 — the diffusion-limited floor Purcell's 4πaND expresses. |
| **Grashof** Gr | gβΔT L³/ν² | buoyancy to viscous forces | Free convection's Re. Gr/Re² ≫ 1 → buoyancy dominates forced flow. |
| **Rayleigh** Ra | Gr·Pr = gβΔT L³/(να) | buoyancy to diffusive damping | **Ra_c = 1707.762** (rigid–rigid), critical wavenumber ≈ 3.117, *independent of Pr at onset*. Below it, no convection; above it, Bénard cells. |
| **Biot** Bi | hL/k_solid | internal conductive to surface resistance | **Bi < 0.1** → lumped-capacitance admissible. Bi and Nu look identical: **k is the solid's in Bi, the fluid's in Nu.** Confusing them is a classic error. |
| **Mach** Ma | u/c | flow to sound speed | Ma < 0.3 → density change <~5%, incompressible admissible. Ma = 1 → shocks. |

---

## Buckingham Pi — generating your OWN groups

Buckingham (1914), *On Physically Similar Systems; Illustrations of the Use of Dimensional Equations*,
Physical Review **4**(4):345–376, doi 10.1103/PhysRev.4.345. (He introduced the symbol π — hence the
name. He was not first: Vaschy (1892); Federman and Riabouchinsky (1911) have priority.)

**The recipe, runnable:**

1. **List all n relevant variables.** This is the whole game and it is *not* mathematics — it is physics
   judgment. Omit a relevant variable and every group downstream is wrong.
2. **Write each variable's dimensions** (M, L, T, Θ, …).
3. **Compute j = the RANK of the dimensional matrix** — *not* the number of base dimensions. (Textbooks
   routinely say "number of dimensions"; that is the common failure mode, and it is wrong whenever the
   dimensions are not independently represented.)
4. **Number of groups = n − j.**
5. **Choose j repeating variables** that (a) span all j dimensions, (b) cannot themselves form a
   dimensionless group, (c) exclude the variable you are solving for.
6. **Form each Π** as the repeating set to unknown exponents times one non-repeating variable; solve so
   the product is dimensionless.
7. **Check each Π is dimensionless.** Every time.
8. **Write Π₁ = f(Π₂, …, Π_{n−j}).**

**Worked example — drag on a sphere.** Variables: F [M L T⁻²], ρ [M L⁻³], U [L T⁻¹], D [L],
μ [M L⁻¹ T⁻¹]. n = 5; rank j = 3. **Groups = 2.** Repeating set: ρ, U, D.

    Π₁ = F/(ρU²D²)   → drag coefficient C_d (up to the π/8 frontal-area convention)
    Π₂ = μ/(ρUD)     → 1/Re

**Result: C_d = f(Re).** Five variables collapse to one curve.

**And now the fence, printed where it hurts.** That took ten minutes. It did **not** hand you f. Nothing
in Buckingham's theorem predicts C_d ≈ 0.5 in the subcritical range, or that near **Re ≈ 3×10⁵** the
smooth-sphere drag *falls* ~5× as the boundary layer trips turbulent and the wake narrows — the **drag
crisis**. That is why golf balls have dimples, and dimensional analysis could never have told you.
**Only the experiment found it.**

---

## Dynamic similarity — and the conflict you cannot escape

**The rule:** geometrically similar systems sharing every relevant group have identical dimensionless
results. Test the model, trust the full scale.

**The fence: you can rarely match all groups at once.** The ship model is the classic. Wave-making needs
**Fr**; skin friction needs **Re**. Same fluid (ν fixed), model at scale λ:

- Fr matching requires **v_m = v_s·√λ** (model goes *slower*)
- Re matching requires **v_m = v_s/λ** (model goes *faster*)

At λ = 1/25: v_m = 0.2·v_s versus v_m = 25·v_s. **Incompatible by a factor of 125.** No cleverness
removes this.

**What you do about it — Froude's hypothesis, stated as the assumption it is.** Split resistance into a
wave-making (residuary) part governed by Fr and a frictional part governed by Re. Run at **matched Fr**;
measure total resistance; estimate the model's friction from a flat-plate correlation at the *model's*
Re (e.g. the ITTC-1957 line) and subtract; scale the residuary remainder by Fr; add back *full-scale*
friction at *full-scale* Re.

**This is MODELED, and its assumptions are the fence:** that the two components are independent and
additive (they are not, strictly — the boundary layer alters the wave field), and that a flat plate is
an acceptable friction proxy for a hull. It works well enough to build ships. It is not a law. Every
group conflict is resolved by exactly this kind of named, assumption-carrying decomposition — or it is
not resolved at all.

---

## The numbers (the ratio/frequency table)

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| Re (bacterium) | ~10⁻⁴–10⁻⁵ (recomputed 3×10⁻⁵) | — | ~1 μm organism, 30 μm s⁻¹, water | OBSERVED-REPLICATED | Purcell (1977) Am J Phys 45:3–11 | Micron swimmer coasting ≫ 0.1 Å after thrust stops |
| Re (man swimming) | ~10⁴ | — | human in water | OBSERVED-REPLICATED | Purcell (1977) | Measured u, L, ν disagreeing by >1 order |
| Re (blue whale) | ~1×10⁸ | — | L ≈ 25 m, u ≈ 5 m s⁻¹, ν_sw ≈ 10⁻⁶ m² s⁻¹ | MODELED (arithmetic mine, sourced inputs) | computed; published statements agree at order 10⁸ | Sourced cetacean cruise Re outside 10⁷–10⁹ |
| ν (water) | ~10⁻² | cm² s⁻¹ | liquid water, room temp | OBSERVED-REPLICATED | Purcell (1977) | Standard viscometry |
| Coast distance (bacterium) | ~0.1 | Å | 1 μm organism, 30 μm s⁻¹, water | OBSERVED-REPLICATED | Purcell (1977) | Observe measurable glide |
| Stopping time (bacterium) | ~0.6 | μs | as above | OBSERVED-REPLICATED | Purcell (1977) | Observe momentum persistence |
| Pe / "S" (bacterium) | ~10⁻² (recomputed 3×10⁻²) | — | micron scale, D ≈ 10⁻⁵ cm² s⁻¹ | OBSERVED-REPLICATED | Purcell (1977) | Stirring raising local uptake at Pe ≪ 1 |
| L\* = D/u | ~30 (recomputed 33) | μm | small molecule, bacterial speed, water | OBSERVED-REPLICATED | Purcell (1977) | Bacterial run lengths systematically ≠ D/v |
| Speed for +10% intake | 700 (≈20× achievable) | μm s⁻¹ | Stokes flow around a sphere | MODELED (Purcell's relaxation solution) | Purcell (1977) | Intake rising faster than √v |
| Re_c (pipe, sustained) | 2040 ± 10 | — | smooth circular pipe | OBSERVED-CONTESTED | Avila et al. (2011) Science 333:192–196 | Sustained turbulence reproducibly below 2030 |
| Re_c (pipe, textbook) | ~2300 (range ~2000–4000) | — | smooth pipe, disturbance-dependent | OBSERVED-CONTESTED | standard texts; Reynolds (1883) | — (answers a different question than 2040) |
| St (cruise) | 0.2–0.4 | — | dolphins, sharks, bony fish; birds/bats/insects **at cruise only** | OBSERVED-REPLICATED | Taylor, Nudds & Thomas (2003) Nature 425:707–711 | Cruising taxon reproducibly outside 0.2–0.4 |
| St (water walkers) | 0.01–0.1 (arthropods); 0.1–1 (large) | — | air–water interface locomotion | OBSERVED-REPLICATED | Bush & Hu (2006) ARFM 38:339–369 | Measured water-walker St outside band |
| Wo α (ascending aorta) | ≈13.2 (≈20.3 some studies) | — | human ascending aorta | OBSERVED-CONTESTED (varies by study/subject) | Cardiovasc Eng Technol (2024) doi 10.1007/s13239-024-00723-4 | Measured α outside ~10–21 in healthy adults |
| Wo α (capillary) | ≈0.005 (micro-circulation all <1) | — | human microcirculation | OBSERVED-REPLICATED | as above | Pulsatile inertial profile in a capillary |
| Dinosaur trackway speeds | 1.0–3.6 | m s⁻¹ | Alexander's Fr method, h ≈ 4× foot length | OBSERVED-CONTESTED | Alexander (1976) Nature 261:129–130; contra PMC12187409 (2025) | Extant-bird validation on compliant substrate contradicting formula |
| Capillary length ℓ_c | ≈2.6 | mm | air–water, σ ≈ 0.07 N m⁻¹ | OBSERVED-REPLICATED | Bush & Hu (2006) | Direct meniscus measurement |
| Strider length / weight | 1 cm / 10 dynes (10⁻⁴ N) | cm / dyn | water striders | OBSERVED-REPLICATED | Hu, Chan & Bush (2003) Nature 424:663–666 | Direct mass measurement |
| Insect interface-crossing force | 10–100× body weight | — | insects 1–10 dyn, perimeter ~1 cm | OBSERVED-REPLICATED | Bush & Hu (2006) | Measured crossing force ≈ body weight |
| Min. capillary wave speed c_m | 23 | cm s⁻¹ | air–water interface | OBSERVED-REPLICATED | Lighthill (1979), via Bush & Hu (2006) | Waves radiated by steady motion below 23 cm s⁻¹ |
| Kn regime bounds | <0.01 / 0.01–0.1 / 0.1–10 / >10 | — | **gas** flows | OBSERVED-REPLICATED | standard rarefied-gas references | No-slip Navier–Stokes matching data at Kn > 0.1 |
| λ (air) | ≈68 | nm | 1 atm, 25 °C | OBSERVED-REPLICATED | standard kinetic theory | Direct mean-free-path measurement |
| Ra_c | 1707.762 (wavenumber ≈3.117) | — | rigid–rigid boundaries, **Pr-independent at onset** | OBSERVED-REPLICATED | Rayleigh–Bénard linear stability | Onset reproducibly below Ra ≈ 1700, rigid–rigid |
| Pr | 7 (water) / 0.71 (air) / 0.025 (mercury) | — | near room temperature | OBSERVED-REPLICATED | standard property tables | Property measurement |
| Bi threshold | 0.1 | — | lumped-capacitance admissibility | MODELED (engineering convention, not a law) | standard heat-transfer texts | Material internal gradients at Bi < 0.1 |
| Ma threshold | 0.3 | — | incompressibility admissible (Δρ <~5%) | MODELED (convention) | standard gas dynamics | Density change >5% below Ma 0.3 |
| Sphere drag crisis | Re ≈ 3×10⁵; C_d ≈ 0.5 → ~0.1 | — | smooth sphere | OBSERVED-REPLICATED | standard sphere drag curve | Smooth-sphere C_d not dropping near 3×10⁵ |
| Golden angle | ≈137.5 | degrees (dimensionless) | phyllotactic divergence; reproduced physically | OBSERVED-REPLICATED | Douady & Couder (1992) PRL 68:2098–2101 | Repulsion dynamics failing to select ≈137.5° |
| Earth mantle viscosity | 10²¹ | poise | mantle flow | MODELED (geophysical inference) | quoted in Purcell (1977) | Independent rheological determination |
| Prefactor f in Π₁ = f(Π₂,…) | — | — | any Buckingham result | **NOT-MEASURED** | — | *(this is the point — see fence)* |

---

## Falsifier (operable)

This chapter is refuted, in whole or in relevant part, by:

1. **A reproducible micron-scale swimmer achieving net displacement by strictly reciprocal
   (one-degree-of-freedom) motion in a Newtonian fluid at Re ≪ 1** — breaks the scallop theorem and the
   Re section. (Live scope caveat: net motion by reciprocal stroke *is* reported at **intermediate** Re
   and in **non-Newtonian** fluids — those mark Purcell's boundary, they do not refute him.)
2. **A Pe ≪ 1 system in which stirring measurably raises local uptake** — refutes the Péclet section and
   Purcell's √v result.
3. **A cruising flyer or swimmer reproducibly outside 0.2 < St < 0.4** at steady cruise across
   independent labs.
4. **Sustained pipe turbulence reproducibly below Re ≈ 2030**, or a demonstration that puff-decay and
   puff-splitting times do not cross.
5. **A dimensionless group that predicts its own prefactor** without experiment — refutes this chapter's
   central fence, and most of dimensional analysis with it.
6. **Any number in the table disagreeing with its cited source.** Check them. That is what they are
   printed for.

---

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **INADMISSIBLE — "432 Hz is nature's frequency"** (and every claim of that shape). The defect is
  structural, and it is the cleanest teaching case here: **432 Hz has units.** A dimensioned quantity
  cannot be a scale-free law, because its numerical value changes with the unit — 432 Hz is also
  25,920 min⁻¹, and nothing about nature changed. A universal claim must be dimensionless or it is not
  a universal claim. INADMISSIBLE **as physics/biology**, with that receipt. It may be recorded as an
  HONEST/cultural signal — a tuning preference is a real thing that real people really have — and never
  as a TRUE/measured one. The two stores never merge.
- **INADMISSIBLE — "the Schumann resonance is nature's universal frequency."** Split the claim. The
  **~7.83 Hz fundamental is real and measured**: predicted by Schumann (1952), confirmed by direct
  measurement in 1960 (Balser & Wagner, *Nature*), harmonics near 14.3, 20.8, 27.3, 33.8 Hz, excited by
  global lightning. That is EARNED — and it is a cavity resonance of *one particular* Earth–ionosphere
  waveguide, a *dimensioned* property set by the planet's own geometry. It therefore **cannot** be a
  universal constant: change the planet's radius, change the frequency. The attached human-health claims
  are a **separate, unearned** claim requiring their own evidence and are not supported here. (The
  literature surfaced by naive search on this topic is dominated by non-primary sources; prefer the
  primary citations.)
- **INADMISSIBLE — "the golden ratio is a universal design law of nature."** Unfalsifiable as stated (no
  observation is specified that could refute it) and cherry-picked in practice. Recorded with its
  receipt.
- **EARNED — the golden angle, and the template for all of the above.** The ~137.5° phyllotactic
  divergence angle **is** real, **is** dimensionless, and **has a physical mechanism**: Douady & Couder
  (1992), *Phyllotaxis as a physical self-organized growth process*, Phys. Rev. Lett. **68**:2098–2101,
  reproduced Fibonacci phyllotaxis in a **physical** experiment — ferrofluid droplets in a magnetic
  field repelling as d⁻⁴ — and in simulation. The pattern self-organises under repulsion, converging to
  the golden mean because the system avoids rational (periodic) organisation. **No mysticism is required
  and none is admitted.** Honour what is measured; fence what is not; never mock the person asking.
  That is the whole method.
- **NEGATIVE — the mandatory counterweight: "nature does it this way, therefore it is optimal."** Gould &
  Lewontin (1979), *The Spandrels of San Marco and the Panglossian Paradigm*, Proc. R. Soc. Lond. B
  **205**:581–598: not every trait is an adaptation. Phylogenetic inertia, drift, developmental
  constraint, pleiotropy and historical contingency produce features that are *not* optimal solutions to
  anything (the vertebrate retina's inverted wiring; the recurrent laryngeal nerve's detour).
  **Therefore convergent evolution is evidence of a constraint-optimum and a HYPOTHESIS GENERATOR —
  never a proof.** Any biomimetic design taken from this chapter must still beat a **tuned conventional
  baseline** on a **pre-registered** metric or be recorded NEGATIVE (rule M7). The St = 0.2–0.4
  convergence is the strongest candidate here and is still subject to this rule.
- **NEGATIVE — Alexander's trackway formula on compliant substrates.** Carried above as
  OBSERVED-CONTESTED: neither silently trusted nor silently dropped.
- **NOT-MEASURED — every prefactor.** See the fence.

---

## HONEST FENCE — MODELED

**Dimensional analysis gives you the FORM and the GROUPS. It never gives you the prefactor.**

Every constant in this chapter — 1707.762, 2040, 0.2–0.4, 23 cm s⁻¹, 137.5° — came from a
**measurement**, not from the algebra. The algebra told us only *which axis to plot them against*. That
is an enormous gift. It is not a result.

**Operably: a design argued purely from dimensionless groups with no measured coefficient is
NOT-MEASURED, not a result.** When a proposal says "we matched the Strouhal number, so it will be
efficient," it has matched the *axis* and measured *nothing*. Ask for the coefficient. Ask which
experiment produced it. Ask over what scope it holds.

The chapter is classed **MODELED** as a whole: the groups are exact algebra; every threshold in them is
a fit or a measurement carrying its own assumptions and scope. Individual rows carry their own classes,
and those govern.

---

## Not claimed

- **No UNI claim is made or raised here.** This chapter cites published fluid mechanics and biology.
  **A nature citation is never a UNI gate.** Nothing in the UNI ledger moves because Purcell wrote a
  paper in 1977. Any reading that lets a literature citation imply a UNI capability is a lane-crossing
  and is defective.
- **Not claimed: that these groups are complete.** They are the ones with the best receipts. New problems
  need new groups — which is why the Buckingham recipe is here rather than a longer list.
- **Not claimed: that matching a group makes a design good.** It makes it *comparable*.
- **Not claimed: that any biological value here is an optimum.** Gould & Lewontin (1979) forbids that
  inference without a baseline and a pre-registered metric.
- **Not claimed: any prefactor, coefficient, or efficiency this chapter did not source.**
- **Not claimed: that dynamic similarity can be fully achieved.** It usually cannot (Re vs Fr). The named
  decomposition is an assumption, carried as one.
- **QUAESTIO-APERTA.** Whether these groups extend to substrates and regimes nature has not run — and
  what, if anything, "the next evolution beyond human" would even be — is a **permanent open question**.
  Not a target, not a milestone, not a deliverable. It appears here only to be fenced.
