# The one loop — active inference (VFE to understand, EFE to choose)

> **Knowledge file `K03-METHOD-the-one-loop-active-inference.md`** of the UNI Encyclopedia & Cookbook GPT pack.
> This file is a BUILD ARTIFACT: it merges **1** source file(s) from the
> repository `TMDLRG/UNI-Encyclopedia-Cookbook`, byte-for-byte, in the order listed below.
> The repository is the single source of truth; if this file and the repository ever
> disagree, the repository wins and this file is stale.
>
> SOVEREIGNTY RULE (binding, do not merge the two ledgers): this corpus carries TWO sovereign evidence vocabularies. The UNI 4-value fence (proven / designed / hypothesized / not-yet-built) describes ONLY UNI's own build status and is governed by encyclopedia/CLAIM-LEDGER.md. The NATURA 12-value class, in three groups, describes ONLY nature's observed regularities and is governed by encyclopedia/NATURE-LEDGER.md: group A / measured = OBSERVED-REPLICATED, OBSERVED-SINGLE, OBSERVED-CONTESTED; group B / derived = MODELED, MODELED-CONTESTED, HYPOTHESIZED; group C / fenced = INADMISSIBLE, SUPERSEDED, NOT-MEASURED, NOT-SOURCED, NOT-CONFIRMED, NOT-LOCATED. Six of the twelve were registered by NA-00 amendment 2026-07-15-A after the corpus refuted the original 'six classes and only six' at 72 of 919 ledger rows; twelve is a MEASURED property of the corpus, not a design target. NEVER read NOT-SOURCED as NOT-MEASURED: the first says we could not trace the source (a fact about us), the second says nobody has measured it (a claim about the frontier of science). A nature citation is NEVER a UNI gate. Cross-reference between them by explicit link only, never by merge.


**Source files merged into this knowledge file, in order:**

- `encyclopedia/wing-NATURA/NA-02-the-one-loop.md`

---



<!-- ===== BEGIN encyclopedia/wing-NATURA/NA-02-the-one-loop.md ===== -->

# NA-02 — The one loop: active inference as the method (VFE to understand, EFE to choose)

> **What you are reading.** The operating loop of this wing, stated exactly, with its math in
> readable ASCII and every symbol defined — then, at equal seriousness, the best published
> objections to it. This chapter is a **method**, not a result. Reading it raises no rung and
> settles no question, and it is **not** evidence that anything is intelligent or aware. A method
> earns its keep by making claims falsifiable; it never earns a claim.

---

## The loop, in five steps

1. **PERCEIVE** — minimize **variational free energy** `F`. Build an honest belief `q(s)` about the
   state from what you actually observed. Read before you write.
2. **PREDICT** — state, falsifiably and in advance, what you expect to observe if you act. If you
   cannot state a test, you do not yet understand the state. Return to step 1.
3. **CHOOSE** — minimize **expected free energy** `G(pi)` over candidate policies. One number holds
   both the goal and the uncertainty.
4. **ACT** — take the lowest-`G` policy.
5. **OBSERVE & UPDATE** — capture the receipt. If the observation surprised you, your model was
   wrong. Update it; do not explain the surprise away.

Steps 1 and 3 are two different quantities with two different jobs. Conflating them is the most
common error in applying this framework.

---

## Step 1 — PERCEIVE: minimize variational free energy

You hold a **generative model** `p(o,s)`: a joint over observations `o` and hidden states `s`, saying
how states cause observations and how states evolve. You generally cannot invert it — the true
posterior `p(s|o)` needs a marginal `p(o) = SUM_s p(o,s)` that is usually intractable. So you posit an
**approximate posterior** `q(s)` and improve it against:

```
F[q,o] = E_q(s)[ ln q(s) - ln p(o,s) ]
```

**Decomposition (a) — complexity minus accuracy.** Since `ln p(o,s) = ln p(o|s) + ln p(s)`:

```
F = D_KL[ q(s) || p(s) ]  -  E_q(s)[ ln p(o|s) ]
    \___ complexity ___/     \____ accuracy ____/
```

Explain the data well (**accuracy**), but do not move your beliefs off the prior further than the
data forces (**complexity**). This is why minimizing `F` is not maximizing fit: it selects the
*simplest sufficient* explanation, and a model that fits by contorting its beliefs pays for it in the
complexity term. It is the formal statement of "do not confabulate to raise apparent accuracy."

**Decomposition (b) — the bound on surprise.** Since `ln p(o,s) = ln p(s|o) + ln p(o)`:

```
F = D_KL[ q(s) || p(s|o) ]  -  ln p(o)     and therefore     F >= -ln p(o)
    \___ the bound gap ___/    \_ evidence _/
```

`-ln p(o)` is **surprisal** (self-information): how unexpected the observation was under the model.
KL divergence is non-negative (Gibbs' inequality), so `F` **upper-bounds** surprisal and the slack is
exactly `D_KL[q(s)||p(s|o)]`. Minimizing `F` over `q` does two things at once: it drives `q` toward
the true posterior and tightens the bound toward `-ln p(o)`. The bound is tight **only** when
`q(s) = p(s|o)` exactly. Standard variational Bayes; Buckley et al. (2017), *J. Math. Psych.*
81:55–79, and Da Costa et al. (2020), *J. Math. Psych.* 99:102447, give the derivations.

**Units.** `F` is in **nats** under natural logs, **bits** under base-2
(`1 nat = log2(e) = 1.442695... bits`). An `F` reported without its log base is not a number.

---

## Step 2 — PREDICT: the falsifier goes in before the action

No formula, and not optional. Before acting, write down what you expect to observe and what would
refute you. The reason is structural: **surprise cannot be computed against a prediction that was
never made.** Skip step 2 and step 5 has nothing to update — the loop degenerates into narration, a
model that only ever confirms itself because it only ever wrote down what already happened.

---

## Step 3 — CHOOSE: minimize expected free energy

`F` scores beliefs about what *is*. It cannot score an action, because the observation that action
would produce has not happened. So take the expectation over predicted outcomes: **expected free
energy** `G(pi)`, scored per policy `pi` (a candidate action sequence).

```
G(pi) = D_KL[ q(o|pi) || p(o|C) ]  +  E_q(s|pi)[ H[ p(o|s) ] ]
        \_______ risk _________/      \______ ambiguity ______/
```

**Risk**: how far this policy's predicted outcomes sit from the outcomes you *prefer*, `p(o|C)`.
**Ambiguity**: how uninformative observations will be even if you reach those states — the expected
entropy of the likelihood. High ambiguity means you act and still do not know where you are.

The same quantity rearranges into the reading this wing uses most:

```
G(pi) = -E_q(o|pi)[ D_KL[ q(s|o,pi) || q(s|pi) ] ]  -  E_q(o|pi)[ ln p(o|C) ]
        \________ epistemic value (info gain) ____/     \___ pragmatic value ___/
```

So `G = -(epistemic) - (pragmatic)`, and **minimizing `G` maximizes both**. Epistemic value is how
much the policy is expected to *change your beliefs* — the divergence between the posterior you would
hold after observing and the one you hold now. Pragmatic value is how far it moves you toward `C`.

**Honest note on the equivalence.** The risk/ambiguity form is exact under the standard convention
`q(o,s|pi) = p(o|s) q(s|pi)`. The epistemic/pragmatic form additionally treats `q(s|o,pi)` as standing
in for `p(s|o)` — so where `q` is a poor posterior, the "information gain" reading is itself
approximate. Da Costa et al. (2020) set out both decompositions and the conditions relating them.

**Policy selection.** A softmax over `-G`, sharpened by precision `gamma`:

```
P(pi) = sigma( -gamma * G(pi) )
```

`gamma -> 0` gives a uniform (indifferent) distribution over policies; `gamma -> infinity` gives a
deterministic `argmin G`. Because the softmax argument must be dimensionless and `G` is in nats,
**`gamma` carries units of inverse nats** — a detail routinely dropped. Friston et al. (2017),
*Neural Computation* 29(1):1–49, give the fuller process-theory form, where the policy posterior also
carries a past-evidence term (the free energy of policies) alongside `gamma*G`, and `gamma` is itself
inferred rather than fixed.

### Every symbol

| Symbol | Reads as | What it is |
|---|---|---|
| `o` | observations | what actually arrived at the sensor / the receipt |
| `s` | hidden states | what you cannot see directly and must infer |
| `p(o,s)` | generative model | the joint: how states cause observations, how states evolve |
| `p(o\|s)` | likelihood | the `A` mapping in a discrete POMDP |
| `p(s)` | prior | belief before this observation |
| `p(s\|o)` | true posterior | generally intractable — what `q` approximates |
| `q(s)` | approximate posterior | your honest, improvable belief; the object you optimize |
| `pi` | policy | a candidate action sequence |
| `C` | preferences | prior over *preferred* observations, `p(o\|C)` — the goal, as a distribution |
| `gamma` | precision | inverse-temperature over policies; units nats^-1; `gamma > 0` |
| `F` | variational free energy | scores beliefs; upper-bounds surprisal; nats |
| `G` | expected free energy | scores policies; nats |
| `D_KL` | KL divergence | non-negative; zero iff the two distributions are equal |
| `H` | Shannon entropy | expected surprisal |
| `sigma` | softmax | normalizes `-gamma*G` into a distribution over policies |

---

## Why ONE number must hold both terms

Not elegance — the two failure modes are symmetric, and only a single scalar holding both rules out
both at once:

- **Goal-only** (drop the epistemic term): charges toward `C` through states it cannot identify.
  It optimizes hard against a belief it never tested — the confident wrong actor.
- **Explore-only** (drop the pragmatic term): resolves uncertainty forever and arrives nowhere.
  Information gain is always available somewhere; without `C` there is no reason to stop.

Score them separately and you must hand-tune a trade-off weight — which is exactly the judgment you
were trying to make principled. `G` fixes the exchange rate: both terms in nats, both expectations
under the same predictive distribution, and they add. That is the whole argument for the
construction, and it is an argument about **bookkeeping discipline** — not a claim that any organism
computes `G`.

---

## Nature as the authority — stated precisely, never mystically

> Nature is the authority because it is the only system that has **already run the experiment** — a
> very long parallel search under real physical constraints, in which the failures were deleted.
> **Convergent evolution** — independent lineages arriving at the same solution — is evidence of a
> **constraint-optimum**.

**The mandatory counterweight.** Gould & Lewontin (1979), *The spandrels of San Marco and the
Panglossian paradigm: a critique of the adaptationist programme*, Proc. R. Soc. Lond. B
205(1161):581–598, DOI 10.1098/rspb.1979.0086: **not every trait is an adaptation.** Phylogenetic
inertia, drift, developmental constraint, pleiotropy, and historical contingency all produce features
that are not optimal solutions to anything. Nature is full of frozen accidents — the inverted wiring
of the vertebrate retina; the detour of the recurrent laryngeal nerve.

Therefore **"nature does it this way" is a hypothesis generator, never a proof.** A biomimetic design
must still beat a **tuned conventional baseline** on a **pre-registered** metric, or it is recorded
NEGATIVE. Without that gate the doctrine degenerates into exactly the just-so storytelling Gould &
Lewontin named.

### The worked example: earned versus unearned, in one pair

**EARNED.** Douady & Couder (1992), *Phyllotaxis as a physical self-organized growth process*, Phys.
Rev. Lett. 68(13):2098–2101, DOI 10.1103/PhysRevLett.68.2098, built a **physical experiment**:
ferrofluid droplets deposited at the centre of a silicone-oil dish in a vertical magnetic field with
a weak radial gradient. The droplets polarize into parallel dipoles, repel, and drift outward. As
their dimensionless control parameter (`G_DC = v0*T/r0` — **note the name collision with EFE's `G`;
they are unrelated**) is lowered, the divergence angle converges toward the golden angle and Fibonacci
parastichy pairs appear. Nothing golden was put in; repulsion, advection, and periodic deposition were
put in, and the golden angle came out. That is what an earned ratio looks like: a mechanism, a
physical realization, and a knob you can turn to break it.

**UNEARNED.** "The golden ratio is a universal design law of nature" is **INADMISSIBLE as stated** —
no mechanism, no scope, no refuting observation; it survives by cherry-picking the cases that fit.
Recording it as inadmissible is not a verdict on the person asking. The same question, asked with a
scope and a falsifier, *is* what produced Douady & Couder.

Honor what is measured, fence what is not, never mock the asker.

---

## Honest bounds — the best objections to this method

A method that cannot state the strongest case against itself cannot be used for honest science.
These are as their authors argue them, not strawmen.

**1. A low `F` is not a correctness certificate.** `F` and `G` are **approximate-inference**
objectives. `F` upper-bounds surprisal *under the model you already hold*. A confidently wrong model
can sit at low `F`: the bound gap `D_KL[q(s)||p(s|o)]` is unobservable without the posterior you
could not compute in the first place, and the whole construction is conditional on `p(o,s)` — a
choice, not a measurement. Minimizing `F` never tests whether the generative model was the right one.

**2. Markov blankets: two objects, one name.** Bruineberg, Dołęga, Dewhurst & Baltieri (2022), *The
Emperor's new Markov blankets*, *Behavioral and Brain Sciences* 45:e183, DOI
10.1017/S0140525X21002351, distinguish **"Pearl blankets"** — the original epistemic construct in
Bayesian networks, a tool for inference *within a model* — from **"Friston blankets"**, taken to
demarcate the physical boundary between agent and environment. They argue the literature slides
between the two, and that the metaphysical work needs premises that "cannot be justified by an appeal
to the success of the mathematical framework alone." Correct mathematics does not license the
metaphysical reading.

**3. The derivation's assumptions hold in a narrow region.** Aguilera, Millidge, Tschantz & Buckley
(2022), *How particular is the physics of the free energy principle?*, *Physics of Life Reviews*
40:24–50, examine weakly-coupled non-equilibrium **linear** stochastic systems and find the Markov
blanket condition and the restrictions on solenoidal flows valid only for a **very narrow space of
parameters**, additionally requiring an absence of perception–action asymmetry unusual for living
systems. They also identify an implicit equivalence between the dynamics of average states and the
average of the dynamics, which does not hold for linear systems generally. This is live and
contested — the paper drew commentaries and replies — and is carried here as **OBSERVED-CONTESTED**,
not as a refutation.

**4. Unfalsifiable as a general principle — and the reply.** Colombo & Wright (2021), *First
principles in the life sciences: the free-energy principle, organicism, and mechanism*, *Synthese*
198:3463–3488, DOI 10.1007/s11229-018-01932-w, note the FEP has been called a postulate, an
unfalsifiable principle, a natural law, and an imperative, and identify limits on it as a first
principle. Colombo & Palacios (2021), *Non-equilibrium thermodynamics and the free energy principle in
biology*, *Biology & Philosophy* 36(5), DOI 10.1007/s10539-021-09818-x, press the statistical-physics
foundations. Andrews (2021), *The math is not the territory: navigating the free energy principle*,
*Biology & Philosophy* 36:30, DOI 10.1007/s10539-021-09807-0, argues **both** the enthusiastic and the
dismissive readings err: the FEP should designate a **model structure**, onto which construals are
added — so demanding that the FEP itself be falsifiable is a category error. Take this in both
directions: it defends the FEP from a bad objection *and* concedes the thing that matters here —
**a model structure is not an empirical finding.** Specific process-theory models built on it are
falsifiable; the structure is not; neither may borrow the other's credit.

**5. In the UNI program specifically, `G(pi)` is framing vocabulary, not a computed scheduler.**
Nothing in UNI computes `G` and schedules from it; work is ordered by PENDING-burndown,
inadmissible-event catch, migration gating, and read-agency. Prose implying UNI *runs* EFE is drift
and is a defect. This points at UNI's own ledger, which is the authority on UNI build status; it is
stated here only to stop this chapter being misread as a capability.

**The hard fence.** **A nature citation is never a UNI gate.** Reading Friston, Da Costa, or Douady &
Couder raises no rung. Published biology cannot make any UNI claim "proven" — that word belongs to
UNI's ledger and to nothing in this wing.

---

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `F` | `= D_KL[q(s)‖p(s\|o)] − ln p(o)` | nats | any `q`,`p` with `q` absolutely continuous w.r.t. `p` on the support | MODELED (identity; assumption = the stated support condition) | Buckley et al. (2017) *J Math Psych* 81:55–79; Da Costa et al. (2020) *J Math Psych* 99:102447 | exhibit `q,p,o` with `F < −ln p(o)`; requires `D_KL < 0`, contradicting Gibbs' inequality |
| `F − (−ln p(o))` | `>= 0`; `= 0` iff `q(s) = p(s\|o)` | nats | as above | MODELED (Gibbs' inequality) | Buckley et al. (2017) | exhibit `q ≠ p(s\|o)` with zero gap |
| `1 nat` | `log2(e) = 1.442695...` | bits per nat | any log-base change | MODELED (definitional) | Shannon information convention | arithmetic |
| `G(pi)` | `= risk + ambiguity = −epistemic − pragmatic` | nats | discrete POMDP, convention `q(o,s\|pi) = p(o\|s) q(s\|pi)` | MODELED (assumption = that convention; the epistemic form further assumes `q(s\|o,pi) ≈ p(s\|o)`) | Da Costa et al. (2020); Parr, Pezzulo & Friston (2022) *Active Inference*, MIT Press, DOI 10.7551/mitpress/12441.001.0001 | derive a case where the two decompositions diverge under the stated convention |
| `gamma` | free parameter; **no universal value** | nats^-1 | `gamma > 0` | **NOT-MEASURED** | — (fit per model/subject; not a natural constant) | exhibit a replicated cross-species measurement of a single `gamma` |
| `gamma -> 0` / `gamma -> inf` | uniform over `pi` / deterministic `argmin G` | dimensionless limits | softmax `sigma(−gamma·G)` | MODELED | Friston et al. (2017) *Neural Computation* 29(1):1–49, DOI 10.1162/NECO_a_00912 | evaluate the softmax at the limits |
| golden angle | `360/phi^2 = 137.50776405...` | degrees | exact mathematical constant, `phi = (1+sqrt 5)/2` | MODELED (exact) | definitional | arithmetic |
| divergence angle, Douady–Couder cell | converges **toward** the golden angle as `G_DC` falls; Fibonacci parastichies appear | degrees; `G_DC = v0*T/r0` dimensionless | ferrofluid droplets in silicone oil, vertical B-field with radial gradient; plus the matched numerical model | **OBSERVED-REPLICATED** (physical experiment + simulation; extended in the authors' 1996 *J. Theor. Biol.* series) | Douady & Couder (1992) *Phys. Rev. Lett.* 68(13):2098–2101, DOI 10.1103/PhysRevLett.68.2098 | run the cell at small `G_DC` and observe a stable divergence angle away from the golden angle, or non-Fibonacci parastichy pairs |
| fraction of parameter space where the FEP's blanket + solenoidal conditions hold | reported as "very narrow"; **no scalar fraction extracted here** | dimensionless fraction | weakly-coupled non-equilibrium **linear** stochastic systems | **NOT-MEASURED** as a scalar; the scope restriction itself is **OBSERVED-CONTESTED** | Aguilera et al. (2022) *Phys. Life Rev.* 40:24–50 | publish a measure-theoretic fraction over a stated parameter prior |
| biological systems observed to explicitly compute `G(pi)` | — | count | any taxon | **NOT-MEASURED** | — | exhibit a pre-registered neural recording decoding a per-policy `G` in nats |
| divergence-angle distribution across real plant taxa | — | degrees | seed plants | **NOT-MEASURED in this chapter** (not a claim it is unmeasured in the literature — this chapter did not source it) | — | cite a taxon-level measured distribution with `n` and dispersion |

---

## Falsifier (operable)

This chapter is refuted by any of:

1. **A counterexample to the bound.** Exhibit `q`, `p`, `o` meeting the stated support condition with
   `F < -ln p(o)`. That breaks Gibbs' inequality and takes the construction with it.
2. **A decomposition that does not hold.** Show `risk + ambiguity` and `-(epistemic) - (pragmatic)`
   are not the same quantity under the stated convention — or that the convention is not the one the
   cited sources use.
3. **A symbol with wrong units.** Show `sigma(-gamma*G)` is well-formed with `G` in nats and `gamma`
   dimensionless.
4. **The worked example fails.** Run the Douady–Couder cell at small `G_DC` and get a stable
   divergence angle away from the golden angle, with no Fibonacci parastichies.
5. **A misrepresented critic.** Show that Bruineberg et al., Aguilera et al., Colombo & Wright,
   Colombo & Palacios, or Andrews argue something other than what is attributed above. A critique
   rendered as a strawman is a defect in this chapter, not in the critique.

---

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

| Claim | Disposition | Receipt |
|---|---|---|
| "The golden ratio is a universal design law of nature." | **INADMISSIBLE** — unfalsifiable as stated: no mechanism, no scope, no refuting observation; survives by cherry-picking. | Carried beside its earned neighbour: Douady & Couder (1992) produced the golden angle from repulsion dynamics with no golden-ratio input. The mechanism was earned; the "universal law" is not entailed by it. |
| "A low `F` means the model is correct." | **INADMISSIBLE** — non sequitur. `F` bounds surprisal *under the assumed generative model*; the bound gap is unobservable without the posterior that was intractable to begin with. | `F = D_KL[q‖p(s\|o)] − ln p(o)`: a confidently wrong `q` under a wrong `p(o,s)` can sit at low `F`. Buckley et al. (2017). |
| "The FEP is a falsifiable empirical theory of the brain, confirmed by the evidence." | **INADMISSIBLE as stated** — conflates a model structure with a model. Specific process-theory models are falsifiable; the structure is not, and cannot inherit their results. | Andrews (2021) *Biol. Philos.* 36:30 — demands of falsifiability on the FEP itself "rest on a category error." Colombo & Wright (2021) *Synthese* 198:3463–3488 on its limits as a first principle. |
| "Markov blankets identify the physical boundary of an agent." | **CONTESTED — not asserted here.** Requires premises beyond the formalism's mathematical success. | Bruineberg et al. (2022) *BBS* 45:e183 — the Pearl-blanket / Friston-blanket conflation. |
| "The FEP's assumptions are general." | **OBSERVED-CONTESTED** — both positions carried. Aguilera et al. find the blanket + solenoidal conditions hold only in a narrow parameter region for linear stochastic systems; the paper drew commentaries and replies from FEP proponents. Neither side is adopted here. | Aguilera et al. (2022) *Phys. Life Rev.* 40:24–50, plus the comment/reply series in the same volume. |
| "UNI schedules its work by computing `G(pi)`." | **NEGATIVE / drift** — no `G` is computed as a scheduler anywhere in UNI; `G(pi)` is framing vocabulary. | UNI's ledger is the authority on UNI build status. Scheduling is by PENDING-burndown, inadmissible-event catch, migration gating, read-agency. |
| "This loop is how the brain works." | **Not asserted.** Friston et al. (2017) present a **process theory** — a proposal about neuronal dynamics that reproduces a range of characterized phenomena. Reproducing phenomena is consistency, not identification. | Friston et al. (2017) *Neural Computation* 29(1):1–49. See also Friston (2010) *Nat. Rev. Neurosci.* 11(2):127–138, DOI 10.1038/nrn2787, and the tutorial treatment in Smith, Friston & Whyte (2022) *J. Math. Psych.* 107:102632, DOI 10.1016/j.jmp.2021.102632. |

---

## HONEST FENCE — MODELED

This chapter is **MODELED**: a model structure plus the mathematical identities holding within it.
**The assumptions are the fence**, and they are named — a chosen generative model `p(o,s)`; an
approximate posterior `q(s)` that is generally not the true posterior; the convention
`q(o,s|pi) = p(o|s) q(s|pi)`; and, for the epistemic reading of `G`, treating `q(s|o,pi)` as the
posterior. Every identity above is conditional on those. None is an observation about any organism.

The single OBSERVED-REPLICATED row here — Douady–Couder — is about **ferrofluid droplets and plant
meristems**, not about active inference. It is a worked example of the earned/unearned discipline,
not support for the loop.

---

## Not claimed

- That the loop is **evidence** that anything is intelligent, aware, self-aware, or conscious. It is
  a method. A system that minimizes `F` is a system that minimizes `F`.
- That any biological system **computes** `F` or `G` explicitly — NOT-MEASURED (see the table).
- That the FEP is established, general, or settled. Its status is genuinely contested; the strongest
  published objections are printed above rather than summarized away.
- That `gamma`, or any other parameter here, has a universal natural value.
- That citing this literature raises any UNI rung or makes any UNI claim "proven." **A nature
  citation is never a UNI gate.**
- That "nature does it this way" establishes anything. It generates a hypothesis; a tuned
  conventional baseline on a pre-registered metric decides it.
- Anything about **"the next evolution beyond human"** or "full human." Both remain
  **QUAESTIO-APERTA** — permanent open questions, never a target, never a milestone, never a
  deliverable of this wing.


<!-- ===== END encyclopedia/wing-NATURA/NA-02-the-one-loop.md ===== -->

