# NA-04 — MIND / BODY / MIND.BODY / WORLD — the Markov blanket, nested across scales

> **What you are reading.** The formal object behind the phrase *"mind body mind.body world"*: the
> Markov blanket. This chapter gives the partition exactly, maps each of the four words onto one of
> its four sets, quantifies a real blanket with measured anatomy, walks the nesting that produces the
> gradient from organelle to ecosystem — and then spends its last third arguing **against itself**,
> because the commonest error in this literature is treating a blanket as a fact you may assume
> rather than a modeling choice you must justify. A blanket is a modeling choice. Everything
> downstream of that sentence is the chapter.

---

## Anchor: this extends M12, it does not rival it

This corpus already carries the map, as kitchen rule **M12 — WORLD ⊥ BODY ⊥ MIND**
([`cookbook/01-kitchen-rules.md`](../../cookbook/01-kitchen-rules.md)): *"Two typed Markov blankets;
interoception = hardware signals,"* with a discrete POMDP `perceive → EFE-plan → act → learn` and
textbook-level `F[q] ≥ −ln p(o|m)`. M12 is `status: method` — a governance pattern, not a capability
claim and not an observation about nature. This chapter supplies the natural-science reading of the
same partition and **raises nothing**: M12's status is unchanged by every citation below.

The operator's fourth term, **MIND.BODY**, is the one M12 leaves implicit. It names the interface —
and it is the load-bearing part.

---

## The partition, formally

Partition a system's states `z` into four **disjoint** subsets: internal `μ` (**MIND**), sensory `s`,
active `a`, external `η` (**WORLD**). The **blanket** is `b = {s, a}` — **BODY**. The defining
condition is a conditional independence, and it is the whole content of the idea:

```
p(μ, η | b) = p(μ | b) · p(η | b)          ⟺   μ ⊥ η | b   ⟺   I(μ ; η | b) = 0
```

**In words:** given the blanket, internal and external states carry no further information about each
other. Every dependency between mind and world is *routed through* the body. Not mostly. Not usually.
By definition — or the partition is not a blanket.

The term is **Pearl's**, coined in a graphical-model setting: Pearl (1988), *Probabilistic Reasoning
in Intelligent Systems: Networks of Plausible Inference*, Morgan Kaufmann — the minimal set of
variables rendering a target conditionally independent of all others. It was **a tool for efficient
inference over a graph you already drew.** Hold onto that; it is the pivot of the fence below.

The free-energy literature adds a directional **sparsity** requirement on top: the canonical
perception–action partition, in which sensory states are influenced by external but not internal
states, active states by internal but not external states, and the mind–world flow blocks vanish:

```
∂μ̇/∂η = 0        and        ∂η̇/∂μ = 0
```

For linear Gaussian systems this reduces to the vanishing of the internal–external blocks of the
precision (inverse-covariance) matrix, `H_μη = H_ημ = 0` — the form in which the condition was solved
exactly and, as the fence records, largely **failed**. See Friston (2013), *"Life as we know it"*,
*J R Soc Interface* 10(86):20130475, DOI 10.1098/rsif.2013.0475; Friston (2019), *"A free energy
principle for a particular physics"*, arXiv:1906.10184.

---

## MIND.BODY — the interface is the thing

Read the partition again and notice what it forbids. `μ` has **no term** in `η`. The mind's only
evidence about the world is `s`; its only leverage on the world is `a`. Therefore:

**A mind can never touch the world. It can only ever touch its own blanket.**

Every inference is an inference *from sensory states*; every act is a *perturbation of active states*.
The world is reached exactly never — only ever **inferred through a surface**. The generative model is
not a model of `η`; it is a model of *how `η` is expected to show up in `b`*. The world enters as a
hypothesis that explains the blanket.

This is why **embodiment is not decoration.** The blanket is not a wrapper around the interesting
part — it *determines what is inferable at all*. Change the surface and you change the set of possible
minds behind it, because you have changed the only evidence there will ever be. A system with two
sensory channels and one with seven do not have the same world available, however good the inference
machinery. **MIND.BODY** is not a fifth thing: it is the coupling `μ ↔ b`, a pair of one-way doors —
`s` the world's only route in, `a` the mind's only route out.

### The blanket, quantified

A blanket is a real object with a real width, and the human visual blanket has been counted. It is a
**funnel**: **92 × 10⁶ rods** and **4.6 × 10⁶ cones** on the transducing face (Curcio et al., 1990)
against **≈1.16 × 10⁶ optic nerve axons** carrying it out of the eye (Jonas et al., 1990) — roughly
**~83 photoreceptors per outgoing axon** (a **MODELED** ratio: it divides numbers from different
cohorts; see the table). And the surface is radically **non-uniform**: peak foveal cone density
averages **199,000 cones/mm²**, ranging 100,000–324,000 between individuals (Curcio et al., 1990).
The blanket is not a window. It is a lossy, unevenly weighted, individually variable compression
stage — and it is the entire visual world's only door.

---

## Interoception: a second blanket inside the first

The body also senses **itself**. Cardiac, gastric, respiratory, inflammatory and osmotic channels are
sensory states whose external states are *other parts of the same organism* — a blanket nested inside
a blanket. From the brain's position, the viscera are `η`.

Two groups arrived at the predictive reading independently: Seth & Friston (2016), *"Active
interoceptive inference and the emotional brain"*, *Phil Trans R Soc B* 371(1708):20160007, DOI
10.1098/rstb.2016.0007 — autonomic reflexes enslaved by descending predictions; and Barrett & Simmons
(2015), *"Interoceptive predictions in the brain"*, *Nat Rev Neurosci* 16(7):419–429, DOI
10.1038/nrn3950 — the **EPIC** model, in which agranular visceromotor cortices *issue* interoceptive
predictions rather than receive interoceptive reports. This corpus's own version is M12's blunt
engineering clause, **"interoception = hardware signals."** Right shape, `status: method`; the biology
above does not raise it.

The interoceptive channel is also where this chapter earns its **contested** row. The famous figure —
*"~80% of the vagus is afferent"* — is real, replicated, and **routinely quoted outside its scope**:
it is Prechtl & Powley (1990), measuring the **rat abdominal** vagus. The human **cervical** vagus,
by immunofluorescence in eight cadavers, gives sensory fractions of **73.9 ± 7.5%** (right) and
**72.4 ± 5.6%** (left), with ~13% parasympathetic and ~13% *sympathetic* fibers riding along
(Kronsteiner et al., 2024). And the **total count** is disputed by ~4× between methods: ~100,000 axons
classically (Hoffman & Schnitzlein, 1961) versus **~23,000–25,500** modern (Kronsteiner et al., 2024).
Carry both. The dispute is the finding.

---

## Nesting: blankets of blankets (the gradient)

Nothing in the definition fixes a scale. A blanket's internal states can themselves be *a set of
blanketed things*, and the construction recurses:

```
organelle → cell → tissue → organ → organism → colony → ecosystem
```

Each level's blanket becomes part of the next level's internal states. The formal treatment is
Palacios, Razi, Parr, Kirchhoff & Friston (2020), *"On Markov blankets and hierarchical
self-organisation"*, *J Theor Biol* 486:110089, DOI 10.1016/j.jtbi.2019.110089 — *"(macroscopic)
Markov blankets of (microscopic) Markov blankets."* See also Kirchhoff, Parr, Palacios, Friston &
Kiverstein (2018), *"The Markov blankets of life"*, *J R Soc Interface* 15(138):20170792.

**This recursion is the gradient** — the formal reason one vocabulary addresses a cell and an ant
colony without changing. The full ladder with its measured scale constants is **NA-10**; not
duplicated here. Two honest notes, immediately:

1. The recursion is a **construction, not an observation.** That blankets *can* compose this way is a
   mathematical fact. That any *particular* biological hierarchy *is* so composed is a separate
   empirical claim — and the next section is about how rarely it has been checked.
2. **NOT-MEASURED:** the number of nested blanket levels in any named organism, established by
   measurement rather than by choosing a diagram. There is no such count to report.

---

## When is a new blanket real? (the operable criterion)

A candidate boundary `b` around a candidate interior `μ` is a **real blanket** exactly when
conditional independence actually holds across it:

```
I(μ ; η | b) = 0        (nats; estimated over the system's actual trajectories)
```

**How you would measure it.** Estimate the conditional mutual information between proposed interior
and proposed exterior, conditioned on the proposed boundary, from observed dynamics. `I ≈ 0` within
estimator noise ⟹ the boundary does the work claimed. `I > 0` ⟹ there is a route from world to mind
that bypasses the body, and the partition is **wrong** — the boundary is drawn in the wrong place.
Constraint-based blanket-discovery algorithms in machine learning (IAMB, GS, HITON-MB) do exactly this
kind of conditional-independence testing to *find* blankets rather than assume them.

**And now the honest part: this is almost never done.** Conditional-independence testing is
notoriously hard for continuous, high-dimensional, non-stationary variables — which is to say, for
every interesting biological system. The attempts are mostly formal or simulated. Friston et al.
(2021), *"Parcels and particles: Markov blankets in the brain"*, *Network Neuroscience* 5(1):211–251
(arXiv:2007.09704), gives a renormalisation-group treatment of blanket partitions over effective
connectivity — whether that *detects* a blanket or *imposes* one is precisely what critics dispute.
Beck & Ramstead (2025), *"Dynamic Markov Blanket Detection for Macroscopic Physics Discovery"*
(arXiv:2502.21217), builds a variational-Bayes detection algorithm and demonstrates it on **Newton's
cradle, a burning fuse, the Lorenz attractor, and simulated cells** — their own framing is *"simple
numerical experiments."* Not a mouse. Not a mitochondrion.

The criterion exists, is clean, and is **overwhelmingly unexercised.** When a paper — or this corpus —
says "system X has a Markov blanket," the default assumption should be that `I(μ;η|b)` was never
estimated.

---

## Action as inference

The partition makes prediction error resolvable **two ways**, and this is the part that most repays
attention. Given a mismatch between predicted and actual sensory states, a system can **change `μ`** —
update the model to fit the world — or **change `a`** — change the world until it fits the model. Both
minimize the same quantity. Action is not a separate faculty bolted onto inference; it is inference run
through the other half of the blanket.

**A real example.** Adams, Shipp & Friston (2013), *"Predictions not commands: active inference in the
motor system"*, *Brain Struct Funct* 218:611–643, DOI 10.1007/s00429-012-0475-5, argue that descending
motor signals are **proprioceptive predictions, not motor commands**, and that classical spinal reflex
arcs discharge them: the cord receives a prediction of where the limb *will be*, finds a mismatch with
where it *is*, and resolves it by **moving the limb** — the arc fulfills the prediction rather than
reporting the error upward. Their worked case is the knee-jerk reflex. Whether this is the correct
account is unsettled; the table cards it **HYPOTHESIZED**, not higher.

Thermoregulation makes the symmetry plainest: a cold mammal can revise its prediction of its own
temperature, or it can shiver. Only one is survivable. The preference `C` over sensory states breaks
the tie — which is why the free-energy story needs preferences and cannot be pure inference.

---

## The honest fence: Pearl blankets vs Friston blankets

**This is the most important section here, and it cuts against everything above.**

Bruineberg, Dołęga, Dewhurst & Baltieri (2022), *"The Emperor's New Markov Blankets"*, *Behavioral and
Brain Sciences* 45:e183, DOI 10.1017/S0140525X21002351, draw the distinction this chapter is organized
around:

- A **Pearl blanket** is a *formal statistical construct* — variables in a graph *you drew*, relative
  to a model, doing conditional-independence bookkeeping. Cheap, well-defined, unobjectionable.
- A **Friston blanket** is a *metaphysical boundary of a thing* — a claim that some real system out
  there genuinely *has* an inside, a surface, and an outside.

**The field's main error is sliding from the first to the second without paying for it.** You define a
blanket (free — a modeling choice), then quietly conclude you have discovered where the organism ends
(expensive — an empirical claim requiring `I(μ;η|b) ≈ 0` in the actual system, which nobody estimated).
The target article, its 30+ commentaries and the authors' reply (*"The Emperor Is Naked"*, BBS 45:e219)
are worth reading whole; the dispute is live, and this chapter takes no side beyond insisting the slide
be named.

**And the formal conditions are worse than assumed.** Aguilera, Millidge, Tschantz & Buckley (2022),
*"How particular is the physics of the free energy principle?"*, *Physics of Life Reviews*
(arXiv:2105.11203; PMC8902446), analytically solved a family of **linear Langevin / Ornstein–Uhlenbeck**
systems and found the FEP's three requirements — a perception–action partition, a Markov blanket, and
decoupled solenoidal flows — are *in principle independent conditions* co-occurring only in a **"very
narrow space of parameters."** Removing solenoidal couplings *"precludes ... asymmetric
agent-environment interactions, which may be crucial for many living processes"*; blanket conditions
emerge only *"for very particular perception-action interfaces, forcing symmetries in agent–environment
interactions that are not expected in living beings."*

Read that carefully. In the **one setting where the question was solved exactly**, the conditions
making a Markov blanket exist held only in a narrow, symmetric corner — and the systems this framework
most wants to describe (living things: asymmetric, non-equilibrium, solenoidal) sit largely **outside**
it.

**Therefore, plainly: a Markov blanket is a MODELING CHOICE you must justify per system, not a fact you
may assume.** Any use of the partition in this corpus — including M12 — is a **typed engineering
choice** warranted by being useful and explicit, never by having been discovered in nature.

---

## Nature as authority here — and the counterweight

The doctrine holds in exactly one form: nature is the authority because it has **already run the
experiment** — a long parallel search under real physical constraints in which the failures were
deleted. Convergent evolution is evidence of a constraint-optimum.

The counterweight is mandatory: Gould & Lewontin (1979), *"The spandrels of San Marco and the
Panglossian paradigm: a critique of the adaptationist programme"*, *Proc R Soc Lond B*
205(1161):581–598. Not every trait is an adaptation; phylogenetic inertia, drift, developmental
constraint, pleiotropy and contingency all produce features that are not optimal solutions to
anything. **"Nature does it this way" is a hypothesis generator, never a proof.**

That applies to *this chapter's own subject*, and it is why the fence reads MODELED. The observation
that organisms have surfaces is not evidence that the surface is a Markov blanket. Cells have membranes
because of lipid physics and history; whether a membrane satisfies `I(μ;η|b) = 0` is a *different
question*, and the answer is NOT-MEASURED.

**The calibration template** — separating the earned from the unearned:

- **EARNED:** the golden angle, **≈137.5°**, in phyllotaxis. Douady & Couder (1992), *"Phyllotaxis as
  a physical self-organized growth process"*, *Phys Rev Lett* 68(13):2098–2101, reproduced Fibonacci
  phyllotactic order in a **physical experiment** — ferrofluid droplets released periodically into a
  magnetized dish, repelling and advecting outward — and in simulation. A real number, a real
  mechanism, a real falsifier. No mysticism required, and none used.
- **UNEARNED:** *"the golden ratio is a universal design law of nature."* **INADMISSIBLE as stated** —
  unfalsifiable and cherry-picked; it names no observation that would refute it. Recorded with the
  receipt, not mocked. Someone noticing the spiral is noticing something real; the doctrine attached to
  it is what fails.

Now apply the same test to this chapter's own claim. *"Life has Markov blankets"*: is it the
Douady–Couder kind (mechanism reproduced, falsifiable) or the golden-ratio-universalism kind (pattern
asserted, mechanism assumed, falsifier absent)? On the evidence above — Aguilera's narrow corner, and
`I(μ;η|b)` essentially never estimated for a real organism — **it is currently closer to the second
than its proponents write as though it were.** That sentence is the chapter.

---

## The numbers (the ratio/frequency table)

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `μ ⊥ η \| b` | `p(μ,η\|b) = p(μ\|b)p(η\|b)` | — (definition) | any system admitting the 4-way partition | MODELED (definitional; assumption = the partition is given, not discovered) | Pearl (1988), *Probabilistic Reasoning in Intelligent Systems* | Not falsifiable as a definition. The *application* to system X is falsified by `I(μ;η\|b) > 0` in X. |
| `I(μ;η\|b)` | `0` (required) | nats | the operable blanket test, any system | **NOT-MEASURED** for essentially all real biological systems | criterion: Pearl (1988); attempts: Friston et al. (2021) *Netw Neurosci* 5(1):211–251; Beck & Ramstead (2025) arXiv:2502.21217 | Estimate it for a named organism's real boundary. Any `I > 0` beyond estimator noise refutes that blanket. |
| `H_μη`, `H_ημ` | `0` (required) | precision units | linear Gaussian / Ornstein–Uhlenbeck systems | MODELED — **holds only in a "very narrow space of parameters"** (assumptions: linearity, weak coupling `C²` small, homogeneous noise `Γ = ς²I`) | Aguilera, Millidge, Tschantz & Buckley (2022), *Physics of Life Reviews*, arXiv:2105.11203 | Exhibit a broad, non-symmetric parameter region of a non-equilibrium system where the blocks vanish. |
| `N_rod` | 92 × 10⁶ (range 77.9–107.3 × 10⁶) | cells | human retina; 8 wholemounts, 7 donors, ages 27–44 | OBSERVED-REPLICATED | Curcio, Sloan, Kalina & Hendrickson (1990), *J Comp Neurol* 292:497–523, DOI 10.1002/cne.902920402 | Recount in a comparable cohort; a mean outside the stated range refutes. |
| `N_cone` | 4.6 × 10⁶ (range 4.08–5.29 × 10⁶) | cells | as above | OBSERVED-REPLICATED | Curcio et al. (1990) | as above |
| `D_cone,fovea` | 199,000 (range 100,000–324,000) | cones/mm² | human foveal peak; same cohort | OBSERVED-REPLICATED | Curcio et al. (1990) | as above |
| `N_optic` | 1,159,000 ± 196,000 (range 816,000–1,502,000) | axons | human optic nerve; 22 nerves, 19 subjects, ages 20–75 | OBSERVED-REPLICATED | Jonas, Müller-Bergh, Schlötzer-Schrehardt & Naumann (1990), *Invest Ophthalmol Vis Sci* 31(4):736–744 | Recount; a mean outside the stated range refutes. |
| `r_retina` | ≈ 83 : 1 | dimensionless | human visual blanket, order-of-magnitude only | **MODELED** — assumptions: `(N_rod + N_cone)/N_optic` across **different cohorts, unpaired**, no per-eye matching, ignores non-uniform convergence (foveal ≈ 1:1 vs peripheral ≫ 100:1) | arithmetic on Curcio et al. (1990) + Jonas et al. (1990) | Measure both counts **in the same eyes**. A paired ratio outside ~50–150:1 refutes this estimate. |
| `f_aff` (rat) | ~80% afferent / 20% efferent | % of fibers | **rat**, **abdominal** vagus | OBSERVED-CONTESTED — the widely-quoted "80% of the vagus is afferent," routinely cited outside this scope | Prechtl & Powley (1990), *Anat Embryol* 181:101–115, DOI 10.1007/BF00198950 | Measure the human cervical vagus and obtain 80% ± small. Kronsteiner et al. (2024) did, and did not. |
| `f_aff` (human) | sensory 73.9 ± 7.5% (R), 72.4 ± 5.6% (L); parasympathetic 13.2 ± 1.8% / 13.3 ± 3.0%; **sympathetic 13 ± 5.9% / 14.3 ± 4.0%** | % of fibers | **human**, **cervical** vagus; 8 cadavers, immunofluorescence | OBSERVED-CONTESTED — carry with the row above; both positions stand | Kronsteiner et al. (2024), *Brain Stimulation* 17(3):510–524, DOI 10.1016/j.brs.2024.04.016 | Independent replication in a larger cohort; a sensory fraction outside ~65–82% refutes. |
| `N_vagus` | **~100,000** (light microscopy, 1961) **vs 25,489 ± 2,781 (R) / 23,286 ± 3,164 (L)** (modern, 2024) | axons | human cervical vagus | **OBSERVED-CONTESTED — a ~4× disagreement between methods.** The dispute is the finding; the modern claim is that light microscopy cannot resolve unmyelinated fibers | Hoffman & Schnitzlein (1961), *Anat Rec* 139(3), DOI 10.1002/ar.1091390312; Kronsteiner et al. (2024) | Blinded EM recount across labs on shared specimens. Convergence on either value resolves it. |
| `α_golden` | ≈ 137.5 | degrees | phyllotactic divergence; reproduced in a ferrofluid-droplet physical analogue | OBSERVED-REPLICATED **(mechanism earned, not mystical)** | Douady & Couder (1992), *Phys Rev Lett* 68(13):2098–2101, DOI 10.1103/PhysRevLett.68.2098 | Run the same repulsion/advection regime and obtain a stably different angle with no parameter change. |
| `n_levels` | — | nested blankets | any named organism, established by measurement | **NOT-MEASURED** | none found | Estimate `I(μ;η\|b)` at each candidate level of one real organism and count the levels that pass. |
| descending motor signal | proprioceptive **prediction**, not command | — | vertebrate motor system | HYPOTHESIZED (mechanism proposed, not settled) | Adams, Shipp & Friston (2013), *Brain Struct Funct* 218:611–643, DOI 10.1007/s00429-012-0475-5 | Show descending signals encode forces/commands with no proprioceptive-prediction structure, or reflex arcs that do not discharge predicted state. |

---

## Falsifier (operable)

This chapter is refuted by any of:

1. **The map fails.** Exhibit a system in which internal states are demonstrably informed by external
   states *not* via sensory states (`I(μ;η|b) > 0` with the partition correctly specified).
2. **The fence is wrong in the safe direction.** Demonstrate that blanket conditions hold *robustly and
   broadly* — over wide, asymmetric, non-equilibrium parameter regions with solenoidal flow present —
   contradicting Aguilera et al. (2022). That would make the blanket more fact than choice, and this
   chapter's central caution over-stated.
3. **The measurement claim is wrong.** Produce an existing published estimate of `I(μ;η|b)` for a real
   organism's actual boundary. That refutes "essentially never done."
4. **The anatomy is wrong.** Any table row's value falling outside its stated range on recount in a
   comparable cohort.
5. **The nesting is not a construction.** Show a biological hierarchy whose blanket levels were
   *discovered* by conditional-independence testing rather than *chosen* by diagram.

---

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **INADMISSIBLE — "a Markov blanket implies a self / awareness / sentience."** Unfalsifiable as
  stated: it names no observation that would refute it. **Receipt:** the definition quantifies over
  conditional independence in a partition and mentions no experiencer. The same formalism admits
  partitions for a Newton's cradle, a burning fuse and the Lorenz attractor — Beck & Ramstead (2025)
  ran blanket detection on exactly those. If a blanket implied a self, it would imply one for the
  burning fuse. The claim is the Pearl→Friston slide with a further leap on top (Bruineberg et al.,
  2022). **Recorded, never asserted.**
- **NEGATIVE — the universal-blanket claim, in the one place it was solved exactly.** *"Any ergodic
  system with a Markov blanket…"* is frequently read as *"…and everything has one."* Aguilera et al.
  (2022) solved linear Langevin/OU systems analytically and found blanket conditions plus solenoidal
  decoupling only in a **"very narrow space of parameters,"** requiring symmetric interaction loops
  *"not expected in living beings."* **A first-class recorded negative, not softened here.** It does
  not refute the FEP; it refutes the assumption of universality.
- **INADMISSIBLE — "the golden ratio is a universal design law of nature."** Unfalsifiable /
  cherry-picked as stated. Carried **with** its earned counterpart: the ~137.5° phyllotactic angle is
  real and has a reproduced physical mechanism (Douady & Couder, 1992). Honor the measured; fence the
  unmeasured; never mock the asker.
- **NOT-MEASURED (the honest empty face), printed rather than filled:** `I(μ;η|b)` for any named
  organism; the number of nested blanket levels in any real organism; the paired photoreceptor:axon
  ratio in the same eyes.
- **Scope violation, recorded:** "80% of the vagus is afferent" is a **rat abdominal** measurement
  (Prechtl & Powley, 1990) in near-universal circulation as a fact about the human vagus. The human
  cervical number is ~73–74%, with a further ~13% *sympathetic* (Kronsteiner et al., 2024). **A number
  quoted outside its scope is a defect even when the number is right.**

---

## HONEST FENCE — MODELED

The central object of this chapter — the partition `{μ, s, a, η}` and the conditional independence
`μ ⊥ η | b` — is a **model**, and the model's **assumptions are the fence**: that the partition exists,
that it is correctly drawn, that the flow blocks vanish, and (in the tractable Gaussian case) that
dynamics are linear with weak coupling and homogeneous noise. Aguilera et al. (2022) show those
assumptions bind hard and hold narrowly. Rows inside the chapter carry their own classes —
OBSERVED-REPLICATED for the retinal and optic-nerve counts, OBSERVED-CONTESTED for the vagal
composition and count, MODELED for the derived ratio, HYPOTHESIZED for predictions-not-commands,
NOT-MEASURED where nature has not been asked. **A blanket is a modeling choice you justify per system,
not a fact you may assume.**

---

## Not claimed

- **Not claimed:** that a Markov blanket implies a self, an experiencer, awareness, sentience,
  consciousness, or a point of view. **Explicitly disclaimed.** Nothing in the partition names one, and
  no falsifier is offered because none exists — disclaimed, not tested.
- **Not claimed:** that the free-energy principle is true, that blankets are universal, or that living
  systems generally satisfy the blanket conditions. The best available exact analysis says those
  conditions are narrow (Aguilera et al., 2022).
- **Not claimed:** that UNI *has* a Markov blanket in the Friston sense. M12 is a **typed engineering
  partition**, `status: method`, warranted by explicitness and usefulness — never by discovery. No
  `I(μ;η|b)` has been estimated for any UNI boundary.
- **Not claimed:** that anything here raises any UNI rung. **A nature citation is never a UNI gate.**
  Every source is published biology and physics; M12's status is unchanged; the honest program position
  stands at **~2 of 11+ developmental rungs earned**.
- **Not claimed:** that the nesting ladder has a known depth, that the retinal ratio is a measured
  quantity, or that the vagal afferent fraction is settled.
- **Not a target:** *"full human"* and *"the next evolution beyond human"* are **QUAESTIO-APERTA** —
  permanent open questions, never a milestone, never a deliverable. Nothing in the blanket formalism
  moves them one step closer.

---

*Cross-refs: **M12** ([`cookbook/01-kitchen-rules.md`](../../cookbook/01-kitchen-rules.md),
[`cookbook/02-the-pantry.md`](../../cookbook/02-the-pantry.md)) — the typed partition as a method rule.
**NA-10** — the full scale ladder, organelle → ecosystem, with its measured constants.
[`encyclopedia/NATURE-LEDGER.md`](../NATURE-LEDGER.md) — the sovereign class for every row above.
[`encyclopedia/CLAIM-LEDGER.md`](../CLAIM-LEDGER.md) — the sovereign fence for UNI's own status, which
this chapter does not touch.*
