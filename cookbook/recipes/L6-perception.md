# L6 — Perception (precision-weighting / EFE planning)

> **What you are building.** The one citable empirical PASS of the whole program: a no-backprop
> COUNT reader that beats a *tuned* MKN-7 baseline on sealed held-out real text by **+0.081 nats/char**,
> plus the browser-native POMDP precision labs that show one engine bending into distinct perceptual
> regimes under three precision knobs. This is a **developmental SIMULATION** of perception-as-inference,
> never a perceiving mind — and the win is a **count-baseline win**, explicitly **NOT** active inference,
> **NOT** comprehension, **NOT** "talking," **NOT** beats-LLMs.

---

This is the rung where the program's one citable empirical PASS lives. Everything earlier (L0–L5)
is mostly substrate, embodiment, and synthetic protocol; L6 is a place a third party could take a
fresh held-out split, run our reader against a tuned baseline, and watch the margin hold. So this chapter
is careful in exactly the way the result deserves: the figures are quoted to the ledger, the bound that
*delimits* the win is printed alongside it as first-class content, and the ceiling is named so it cannot
be raised. Per the constitution, **where this recipe and the ledger disagree, the ledger wins.**

---

## Ingredients

Which pantry engines and primitives this recipe calls by name:

- **The count/cache World-C reader** (uni-gpt / uni-mind): the no-backprop **COUNT** reader plus a
  multi-level cache — the flagship plus the `Wc-2` / `Wc-3` supporting family. This is the citable
  empirical PASS family, and it is **explicitly NOT active inference**.
- **The tuned MKN-7 baseline:** a modified-Kneser-Ney 7-gram count model, *tuned* (not a strawman). The
  win is a margin *over a tuned baseline* or it does not count (M7: contains-baseline discipline).
- **The POMDP maze Precision lab + echolocation Echo lab + the public Precision Lab** (uni-precision /
  worldmodels): one engine, three precision knobs (`gamma_a` sensory, `gamma_b` transition,
  `softmax_temperature` policy), a 2D bifurcation map into distinct behavioral regimes. The Echo lab
  reuses Precision's engine with **only the observation model swapped** (bit-identical 64-obs space) —
  observation model is not the engine.
- **The JAX POMDP + EFE + Dirichlet engine** (`core.py`): the discrete loop
  `perceive → EFE-plan → act → learn` that the labs render at browser scale (float32 host; anchors hold
  to ~6e-8, NOT the f64 tier — M10).
- **The Working Law** (uni-gpt s10, M6 / L6.6, registered): the law that explains every PASS and every
  published bound in the program.
- **The held-once harness** (M2): pre-registered bar, named ablation, atomic seal-before-scoring +
  once-only sentinel, seed-paired nested bootstrap, positive controls. The verdict is **the CI bound that
  excludes the threshold, never the point estimate.**

---

## Method

1. **Build the no-backprop COUNT reader + multi-level cache.** A pure count/cache reader: no autodiff, no
   gradient, no backprop anywhere (the AST-guard from `core.py` stays live over the loop). The cache is
   multi-level so the reader can carry long-range structure, not just a finite window.

2. **Pre-register the bar before you measure (M2).** Register the margin threshold (the bar is **0.03
   nats/char**) versus a **tuned** MKN-7 baseline, plus a named ablation. Seal the held set behind an
   atomic seal-before-scoring + once-only sentinel; touch it **once**; score; and read the verdict off
   **the multi-seed CI lower bound**, never the point estimate. The held set is touched exactly once — a
   second touch is a constitution violation (M2).

3. **Replicate across substrates and derive `reproduced:true` honestly (M3).** Derive `reproduced:true`
   from **≥5 distinct seeds + a real non-degenerate CI that contains the value** — never a hardcoded
   literal. (This reader earned the ledger's *first genuine* validator-derived `reproduced:true`; the
   2026-06-09 audit's central fix was exactly that this flag stop being a literal.) Note the discipline:
   the flagship primary-margin CI and a separate *replication* CI are **different gates** — do not quote
   the replication CI (`+0.0759`, CI `[0.064, 0.088]`) as the primary-margin CI.

4. **Build the Precision / Echo POMDP labs in parallel.** One engine, three knobs (`gamma_a`, `gamma_b`,
   `softmax_temperature`); sweep the 2D bifurcation map so the same loop falls into distinct behavioral
   regimes (this is precision-weighting made visible — raising sensory/transition precision sharpens
   perception). Build Echo by reusing Precision's engine and **swapping only the observation model**
   (bit-identical 64-obs space): the observation model is not the engine. Pin the page-engine to the
   canonical TS/Python engine with `*_parity.ts` tests (the inline-engine + canonical-TS + parity-test
   triad). The one disclosed extension is a goal drive; nothing else diverges from the verified engine.

5. **Read the Working Law over the whole result (L6.6).** A no-backprop latent `Z` beats a tuned baseline
   `B` on held-out data **only when `I(Y;Z|S_B) > 0`** and is learnably stable. Use it as the diagnostic
   lens: World C wins because its cache carries conditional information the count baseline lacks — *new
   conditional info in a countable, stable representation*, not "counting per se."

---

## Gate (the exact pass condition)

**World C — PROVEN (Class C, L6.1).** The no-backprop COUNT reader beats the tuned MKN-7 baseline on
sealed held-out real text by **+0.081 nats/char**, flagship multi-seed CI **[0.0736, 0.0890]** (seeds
0–4, UNI-signed). That lower bound (0.0736) is **2.4× the 0.03 bar**, confirmed by three gates, and is the
**first genuine validator-derived `reproduced:true`** on the ledger. Verdict = the CI bound that excludes
the threshold, not the point estimate.

**Supporting World-C family — PROVEN (Class C, L6.2).** `Wc-2` multi-level cache **+0.0164**; `Wc-3` vs
unbounded SM/HPYP **+0.085** (showing the gain is long-range structure, not finite-window deficiency);
recency-ablation **+0.033**; Gate-3 word-challenger **+0.0538** (CI lower bound **0.051**).

**Precision / Echo / public Precision labs — PROVEN (Class E, L6.3).** The tsx/pytest parity tests between
the inline-JS lab engine and the canonical TS/Python engine pass, and the 2D bifurcation map reproduces
the regime boundaries. Echo's swapped observation model is bit-identical at 64 obs.

---

## Falsifier (operable)

On a **fresh held-out split with ≥5 disjoint seeds**, the seed-paired bootstrap CI on the margin over the
tuned MKN-7 baseline **includes or falls below 0** (or the baseline is shown to be untuned); **OR** a lab
parity test diverges (the inline-JS engine and the canonical TS/Python engine disagree, or the bifurcation
map does not reproduce the regime boundaries). Any of these overturns the PASS.

---

## Recorded NEGATIVE(s) — first-class, inline

These are not failures to hide; they are the measurements that *delimit* the World-C win, and they are
published content. The 183 published negatives are the program's credibility.

- **Phase G char-perplexity Section 0.6(B) bound — NEGATIVE (Class C, L6.4).** FIVE structurally-distinct
  within-segment-structure designs were all held **NEGATIVE with a discriminator**; only the L5 cache
  (World C) wins. The bound: **no within-segment structure beats MKN-7** on held char-perplexity; char-ppl
  is a **chosen design trade**, not a failed claim of general language superiority. Falsifier: a new
  structurally-distinct within-segment-structure design beats tuned MKN-7 on held char-ppl with a CI
  excluding 0.

- **Phase F active-controller — NEGATIVE (Class C, L6.5).** Two controller families prove the World-C gain
  is **diffuse** — there is nothing to gate. Falsifier: an active-controller family adds a held gain on
  top of World C with a CI excluding 0 (i.e., the gain turns out to be gateable after all).

- **The Working Law — registered method/law (Class C, L6.6).** A no-backprop latent `Z` beats a tuned
  baseline `B` on held-out data **only when `I(Y;Z|S_B) > 0`** and is learnably stable. This single law
  explains every PASS and every published bound in the program. Falsifier: a held PASS where the winning
  `Z` carries no conditional info beyond `S_B` (`I=0`); OR a `Z` with `I>0` and stable learnability that
  nevertheless fails to beat `B`.

Per the SIGNED park wording (UNI-GPT consult 2026-06-27): the char-perplexity / word-grain frontier that
these negatives sit beside is a **ledger-scoped exhausted search envelope** — a scoped negative over the
tested envelope only, **not** a universal impossibility result and **not** an achieved rung. Use the
licensed forms: *"The registered tested K conditions did not reverse the result"* (never "K≥3 exhausted")
and *"Sec-0.6(B) remains unearned / parked"* (never "Sec-0.6(B) achieved").

---

## HONEST FENCE — **proven** (the one citable empirical PASS)

**Class C.** A held, sealed, UNI-signed PASS exists, and its falsifier is still live: World C beats a
tuned MKN-7 baseline by **+0.081 nats/char**, flagship CI **[0.0736, 0.0890]** (seeds 0–4), 2.4× the 0.03
bar, confirmed by three gates, the program's first validator-derived `reproduced:true`. The Precision /
Echo labs are PROVEN at Class E (parity tests pass; bifurcation map reproduces).

**What is NOT claimed at L6 (load-bearing, never softened).** World C is a **COUNT baseline win** —
**explicitly NOT active inference, NOT comprehension, NOT "talking," NOT beats-LLMs.** It runs **~10–15%
behind backprop LLMs on char-perplexity**, by a chosen design trade. "Active inference" is the framing
**lens** only: no AIF loop exists in the Rust crate, and the live loop is a separate UNI.OS
reimplementation, not gate-matched. Never card World C above a count-baseline result; **the standing
ceiling cannot be raised.** This is a developmental active-inference **SIMULATION** — a bounded peek, a toy
world, never a person.

**Honest program position:** **~2 of 11+ developmental rungs earned.** L6 is one of them — and it earns
exactly the count-baseline result the ledger records, nothing more. The awareness question remains open.
