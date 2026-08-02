# L2 — Tissue / metabolism (interoception and energy)

> **Recipe CB-L2.** A chapter of the literal UNI Cookbook. The Cookbook fully recommends the complete
> build to L12, but every step is labeled by its REAL status drawn verbatim from
> [`../../encyclopedia/CLAIM-LEDGER.md`](../../encyclopedia/CLAIM-LEDGER.md). Where this recipe and the
> ledger disagree, the **ledger wins and this recipe is wrong.**
>
> **Honest program position (printed, never softened):** ~**2 of 11+ developmental rungs earned.** This
> whole program is a developmental active-inference **SIMULATION** — a bounded peek, a toy world, never a
> person.

---

## What you are building

A standing **metabolic drive** for the embodied colony: an interoceptive organ that gives a body a real
energy/satiety budget and a viability edge (it can die), so that maintaining itself becomes
*metabolically necessary*. The pantry framing is `WORLD ⊥ BODY ⊥ MIND` (M12): interoception is a body
signal, never a felt state. Affect is **modeled, never felt**.

You are building this as a **proven foraging/crafting driver** and, in the same breath, recording its
first-class **NEGATIVE as a building driver**. The headline temptation — "metabolism breaks the plateau
to stone and shelter" — is the gate **G6**, and G6 is **OPEN**. Do not let the +135 percent uplift
spin into a plateau-break.

---

## Ingredients

Drawn from the shared pantry by name:

- **The metabolism organ** (strings): standing-metabolic-drive interoception organ; energy/satiety
  factors; a draining/refilling emptying-B; setpoint-peaked preferences `C`; the `:pb_seed` strong-Dirichlet
  seam; a live viability edge in the bridge. Additive + genome-gated (default byte-identical).
- **The Z affect modulator** (uni-gpt / uni-mind): the global `[energy, arousal, valence, fatigue, pain,
  threat, safety, inflammation]` vector that carries the interoceptive signals into precision / preferences /
  habits / learning-rate / horizon.
- **The Heart Lab** (uni-precision / worldmodels) as the *physiological mirror* of the same one engine
  (the reduced Karaaslan cardio-renal homeostasis loop) — "same math, many scales," used here only as the
  cross-scale teaching companion, not as a metabolism gate.
- **One-cure-at-a-time paired RED discipline** (M21): paired kin-N treatment vs kin-N+1 control; never
  stack changes so the winning outcome is unattributable; an offline RED pre-check before any live burn.
- **The JAX POMDP + EFE + Dirichlet engine** (`core.py`) for the no-backprop loop; the read-only
  **counterfactual-EFE (shadow-EFE) audit** path for diagnosing the plateau on the real brains.

---

## Method

1. **Ship the organ additive + genome-gated.** Install the metabolism organ as a new opt-in genome organ
   absent from `default/0`, so the default streamed colony stays **byte-identical** — verify with the
   `mad < 1e-12` golden-fixture tests over the depth-5 planner. The full suite must read **297/0** before
   you proceed (L2.1).

2. **Seed the strong Dirichlet metabolic prior only via the `:pb_seed` seam.** You CANNOT seed a strong
   prior by pre-scaling `B`: `norm_cols` runs before `add1`, which wipes any magnitude you tried to bake in
   (L2.4). The `:pb_seed` concentration field is applied *after* `norm_cols`. This seam is the only place a
   "10-100x lifetime strong prior" can be expressed.

3. **Wire a real viability edge into the live bridge.** The naive design is a trap: in the live bridge,
   `metabolize` / `Viability` / `shutdown` were Sim/Eval-only, so a naive emptying-`B` drained a *belief*
   with **zero world consequence** — an all-`:noop` twin stays exactly as "viable" as an actor (L2.4). Wire
   drain-per-tick, refill-only-when-the-body-has-food, and **die-at-empty** into `bridge.ex` so foraging
   becomes metabolically necessary and a body can actually die. Add satiety→`C` appetite attenuation so a
   sated body's preferences relax.

4. **Run an offline RED pre-check before any live burn (M21).** Run the real engine in a synthetic world
   first. This is load-bearing: the offline pre-check previously caught an "eat-every-tick attractor" (the
   seeded drain model was ~6x too pessimistic vs the real store) *before* a live RED was wasted. Fix the
   generative model (gentle drain; "eating is need-driven, not a habit," mirroring the `:noop`-is-non-habitual
   rule) until offline `G0/G1/G2/G3/G5b` are green.

5. **Run the pre-registered 12 h live paired RED, one cure at a time.** Unit = a matched kin pair:
   treatment = organ-on (kin-N), control = kin-N+1 with the organ off, identical code / world / body, only
   the gated metabolic coupling differing. Register up front: the **G4 allostasis** separation gate, the
   **G6 plateau-break** gate, and the **G5b action-severed-twin** falsifier. Collect server-authoritative
   behavior via RCON (<=10-min cadence) plus brain probes at start/mid/end so the record survives context
   compaction. Reset the RED clock to a clean T0 if the treatment arm's brains crash during setup (pre-T0
   data is exploratory only).

---

## Gate

Two distinct gates live at L2. Carry both at their exact ledger figures and never collapse one into the
other.

**The proven uplift gate (L2.1, Class C).** The first 12 h live RED is a PASS for metabolism as a
foraging/crafting driver: **+135% / 2.35x tool-crafting** and **+19% mining** — a real, attributable
standing-metabolic-drive effect, with the default colony byte-identical and the suite at **297/0**.

**G6 — the load-bearing plateau-break gate (OPEN).** A disciplined RED in which the metabolism organ
**alone** improves building, with the **placed-blocks CI excluding 0**, **AND** the G4 allostasis index
separates in the intended direction. Until both hold, **G6 is OPEN** and no plateau-break may be claimed.
Per the ledger, G6 is presently **contradicted by its own first evidence** (see the recorded NEGATIVE).

---

## Falsifier (operable)

The proven uplift is falsified if any of:

- a repeat pre-registered 12 h live RED **fails to reproduce the tool-crafting uplift within CI**; OR
- the **metabolism-organ ablation does not remove the uplift** (the gain was not attributable to the organ);
  OR
- the **suite drops below 297/0** (byte-identity / regression broken).

G6 is **discharged** (not falsified — earned) only by a subsequent disciplined RED where the organ alone
improves building (placed-blocks CI excludes 0) **and** G4 allostasis separates.

The standing **G5b action-severed-twin** is the falsifier that any "self-maintenance / life" language must
clear: an `:noop`-twin with action severed must NOT stay as viable as an actor. Any such language that has
not cleared G5b is an overclaim.

---

## Recorded NEGATIVE(s) (first-class, inline)

These are content, not failures to hide — they are the credibility of the rung.

- **L2.2 (NEGATIVE, Class C) — metabolism is NOT yet a building driver.** In the **same** 12 h RED that
  produced the +135% crafting uplift, **building (placed blocks) went WORSE: −14%**, and **G4 allostasis
  never separated**. The load-bearing claim "metabolism breaks the plateau to stone/shelter" (gate **G6**)
  is therefore **OPEN and contradicted by its own first evidence**. Do NOT spin the +135% as a plateau-break.
  *Falsifier-to-discharge:* a subsequent disciplined RED shows placed-blocks CI excludes 0 AND G4 separates.

- **L2.3 (NEGATIVE, diagnostic; Class A shadow-EFE audit on real brains) — the plateau is epistemic
  starvation, not gamma-runaway.** The colony **plateaus at "make a tool"** (one UNI hoarded **32 pickaxes**,
  never built). A read-only counterfactual-EFE (shadow-EFE) audit on the real hoarder `.bin` brains
  diagnosed **epistemic_starvation** — **NOT** gamma-runaway (gamma ≈ **7.8**, **unsaturated**) and **NOT** a
  curriculum ceiling; the EFE landscape is pragmatic-saturated and flat, and the information drive is
  **~100x too weak**. *Falsifier:* a gamma-saturation finding, a curriculum-ceiling flip, or an info-drive
  scaling that breaks the plateau without organs would overturn the diagnosis.

- **L2.4 (NEGATIVE, fixed; Class A direct code reading) — two engine seams that invalidated the naive
  design.** (1) You cannot seed a strong Dirichlet prior by pre-scaling `B` (`norm_cols` runs before `add1`),
  so the new `:pb_seed` seam is required. (2) The live bridge had **no viability edge** — `metabolize` /
  `shutdown` were Sim/Eval-only, so a naive emptying-`B` drained a belief with zero world consequence. Both
  fixed in the shipped organ. *Falsifier:* a seam allowing strong-Dirichlet seeding without `:pb_seed`, or
  evidence the live bridge already had a viability consequence.

---

## UNI-GPT consult (2026-06-27 — SIGNED): the smallest G6 cure is a Class-C DESIGN HYPOTHESIS; **G6 stays OPEN**

The diagnosed cure for the plateau is a **structurally distinct** organ — NOT a gamma change, NOT a second
metabolism organ, NOT a placed-block reward bonus. Cross-ref
[`../UNI-GPT-CONSULT-2026-06-27.md`](../UNI-GPT-CONSULT-2026-06-27.md) Q3 (SIGN-WITH-CONDITIONS). This is
**DESIGNED / not-run. It RAISES NOTHING. The rung's status is UNCHANGED and G6 stays OPEN.**

**The organ — `build_epistemic_frontier`.** Add **one** building-specific hidden factor + **one** policy
term valuing info gain about where a block can usefully be placed next:
- `hidden factor: z_build in {unknown_placeable, placeable_support, shelter_contributing, blocked/useless}`
- `drive: maximize expected info gain over z_build for candidate inspect/move/place policies`
- `scope: active only when shelter/stone plateau preconditions are near but not achieved`
- epistemic term per policy:
  `G_new = G_old - beta_build_IG * E_Q[ D_KL( Q(z_build|o,pi) || Q(z_build|pi) ) ]`
- **scale beta by matching, not hand-waving:**
  `beta_build_IG = median(|delta pragmatic G for food/tool|) / median(|delta build IG term|)`; clamp initial
  to {25x, 100x}; 100x only if the offline RED shows 25x underpowered.

**Why epistemic, not gamma.** Gamma (≈7.8, unsaturated) is a precision over `G` — raising it only sharpens
the *existing* ranking. If build-relevant info gain is missing or ~100x too small, gamma sharpens the wrong
ranking. The cure makes build-relevant uncertainty *part of what the planner can value*. (The organ metaphor
stays Class-C design language; the standard active-inference part is only the EFE decomposition + policy
selection, at textbook level.)

**The paired RED — `G6_BUILD_EPI_FRONTIER_PAIRED_RED_v1` (designed).** Matched kin-pair seeds; control =
kin-N+1 (current organ/gamma/build machinery, no frontier term); treatment = kin-N (identical +
`build_epistemic_frontier`, beta fixed from the offline RED, gamma unchanged). One cure at a time (M21).
- **Offline RED pre-check** (replay prior traces, read-only) — pass only if all hold: a build-policy rank
  shift appears (treatment > control); gamma non-diagnostic (unchanged, unsaturated); the info term is
  causally responsible (delta-G_build_IG explains the shift); foraging/crafting not cannibalized. Suggested
  bar: >=25% relative increase in build-relevant policies entering top-3, food/tool rank within +/-5%, gamma
  unsaturated.
- **Live paired RED:** unit = matched kin pair; same 12 h / world dist / paired seeds; no peeking-based
  tuning. **Primary:** `placed_blocks_delta = T - C`, 95% paired bootstrap CI excludes 0 (positive).
  **Co-primary (G4):** the existing ledgered allostasis_index delta CI excludes 0 in the intended direction,
  no viability collapse (do NOT invent a metric after the run). Secondary: stone/shelter progress > 0,
  crafting/mining non-inferior, distance-to-shelter improves.
- **Required ablations (gain MUST collapse):** IG-zero (`beta_build_IG = 0`), shuffled-affordance
  (`z_build` permuted across sites), gamma-only (no organ, gamma matched). Credited only if the gain appears
  with build IG present and collapses when the IG channel is zeroed/scrambled, while gamma-only fails to
  reproduce it.

**Falsifiers (Q3).** Placed-blocks CI includes 0 / is negative; OR blocks improve but G4 never separates; OR
the ablation fails to collapse the gain; OR gamma-only reproduces it (the "not gamma" diagnosis was wrong);
OR blocks bought by damaging survival/tooling beyond non-inferiority. If the offline RED predicts no rank
shift but live improves, log "behavioral improvement observed; mechanism not proven."

**Status.** Until the RED clears both bars and the ablations collapse the gain, `build_epistemic_frontier`
is a **Class-C design hypothesis** supported by a read-only counterfactual diagnosis, **NOT an achieved
plateau-break. G6 stays OPEN.**

---

## HONEST FENCE

**proven (as a foraging/crafting driver) + NEGATIVE (as a building driver).** Class C.

- **proven:** a held, signed result exists (Class C, L2.1) — the first 12 h live RED is a real, attributable
  standing-metabolic-drive effect: **+135% / 2.35x tool-crafting** and **+19% mining**, default colony
  byte-identical, suite **297/0**. Its falsifier is still live (a repeat RED must reproduce within CI; the
  organ ablation must remove the uplift).
- **NEGATIVE:** in the same RED, **building went WORSE (−14%)** and **G4 allostasis never separated**
  (L2.2). The plateau diagnosis is **epistemic_starvation**, not gamma-runaway (gamma ≈ 7.8 unsaturated,
  info-drive ~100x too weak; L2.3).
- **designed (RAISES NOTHING):** the SIGNED `build_epistemic_frontier` organ and its paired RED are a
  Class-C **design hypothesis**, folded in as DESIGNED / not-run. The rung's status is UNCHANGED. **G6 stays
  OPEN.**

**The not-claimed line.** Metabolism is proven as a **foraging/crafting driver, NOT a building driver**.
The **plateau-break (G6) is UNPROVEN** and is contradicted by its own first evidence. Do NOT spin the +135%
uplift as "breaks the plateau." This is **not** life, **not** a synthetic organism, **not** self-aware,
**not** consciousness, **not** "active inference demonstrated"; energy and satiety are **modeled, never
felt**. The **G5b action-severed-twin** is the standing falsifier any "self-maintenance / life" language
must clear. This rung **remains a developmental active-inference simulation** — a bounded peek, a toy world,
never a person. ~2 of 11+ rungs earned.
