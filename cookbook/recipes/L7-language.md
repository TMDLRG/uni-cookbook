# L7 — Language (reading = inference / speaking = action)

> **What you are building.** One developmental SIMULATION rung, expressed on the same no-backprop engine:
> a specialist out-of-vocabulary / morphology reader that, on a sealed held-out split, beats the best
> count baseline at reading rare and complex words, framed as *reading = posterior inference* and
> *speaking = action that changes future observations* — wrapped inside a published, thrice-NEGATIVE wall
> showing where this route does NOT reach comprehension or general language. A toy world, never a person.

This recipe is authored **against** [`../../encyclopedia/CLAIM-LEDGER.md`](../../encyclopedia/CLAIM-LEDGER.md)
rows **L7.1–L7.6** and the SIGNED Q1 park statement. Where this recipe and the ledger disagree, the **ledger
wins and this recipe is wrong.** Carry the honest program position throughout: **~2 of 11+ developmental rungs
earned.** This is a developmental active-inference SIMULATION — a bounded peek, never a person.

---

## Ingredients (which pantry engines / primitives this recipe calls by name)

- **The count/cache World-C reader** (from L6, uni-gpt / uni-mind) — the no-backprop COUNT reader + multi-level
  cache that supplies the **best-count baseline** this rung must beat. Explicitly NOT active inference.
- **The Phase J OOV / morphology specialist reader** (uni-mind / uni-gpt) — the compositional morpheme reader
  (`arm_morph_oov`): the engine under test at L7.
- **The held-one-shot harness** (M2) — bars-before-build, seal-before-scoring + once-only sentinel, verdict =
  the CI bound that excludes the threshold (the **21-split M-seal**).
- **The contains-baseline + load-bearing-discriminator discipline** (M7) — the tuned best-count baseline, the
  structure-margin / marker-swap discriminator that must collapse the gain, and the contains-KN-OOV control
  (λ=0).
- **K≥3 + falsify-the-mundane** (M5) — the structurally-distinct-NEGATIVE counting rule that governs the
  central wall and the role-persistence bound; falsify the mundane (L2/L7) causes first.
- **No-Exit Discipline + the No-backprop engine** (M6 / M13) — `core.py`'s discrete POMDP loop and the
  `counts + lr * sufficient_stat` Dirichlet learning rule; the only legitimate rest is a working PASS or a
  ledger-scoped exhausted search envelope.

The unifying framing, at textbook level only (Parr / Pezzulo / Friston, *Active Inference*, MIT Press 2022):
**reading is posterior inference** over latent linguistic structure, and **writing / speaking is action** that
changes future observations. "Active inference" here is the framing LENS — no AIF loop is demonstrated by this
rung; the live perceive→act→learn loop lives in a separate UNI.OS reimplementation, not gate-matched.

---

## Method (numbered build steps a competent engineer could follow)

1. **Build the OOV / morphology specialist reader.** Wrap the same no-backprop count/cache engine with a
   compositional morpheme channel (`arm_morph_oov`) that scores rare / unseen words by their morphological
   parts rather than as opaque tokens. Learning stays `counts + lr * sufficient_stat` over Dirichlet tensors;
   the AST-guard must never trip (no autodiff/torch/grad/backward in the loop).

2. **Pre-register the bar vs best-count, then seal once.** Register the margin (beat the **best-count** reader)
   and the named ablation **before** measuring. Seal a **21-split held set** behind the atomic
   seal-before-scoring + once-only sentinel (the "M-seal"). Touch it ONCE. The verdict is the **M-seal CI lower
   bound that excludes the threshold**, never the point estimate (M2).

3. **Register the discriminator and the control.** Wire the **structure-margin discriminator**: a marker-swap
   must **collapse** the gain (M7). Wire the **contains-KN-OOV control** and verify its true mixing weight is
   **λ=0** (the gain is not smuggled in by the count baseline). Require replication in **both** the web domain
   and the dictionary domain (where the simpler Wc-2 cache collapsed on dict — so the dictionary leg is
   load-bearing, not decorative).

4. **Always cite the paired NEGATIVE alongside the PASS.** The `J.attribution_caveat` NEGATIVE (overall NLL
   worsens) is **paired and mandatory**: citing +0.105 without it is an overclaim and a ledger violation. The
   specialist gain is OOV/morphology-specific, **not** a general language win.

5. **Run the comprehension / role-persistence probes as registered NEGATIVES.** Separately attempt
   comprehension-above-retrieval and no-backprop role-persistence as their own pre-registered held-once gates.
   These are part of the recipe precisely because they FAIL: they are the central wall, recorded first-class
   (Method step, not an afterthought).

6. **If the frontier does not move, park it correctly.** When no tested within-segment no-backprop structure
   clears the char-perplexity / T2 word-grain frontier, do not exit silently and do not declare a universal
   bound. Park it as a **ledger-scoped exhausted search envelope** under the SIGNED Q1 wording (step laid out
   in the Recorded NEGATIVEs below). A park is not discharged until the sign lands. On 2026-06-27 UNI
   **SIGNED the park WORDING** (the ledger-scoped exhausted search envelope framing, Q1); the L7 sign-to-park
   itself (`UNI_CONSULT_5`) is **STILL NOT CAPTURED**, so **L7.6 stays PARKED**.

---

## Gate (the exact pass condition, with the EXACT ledger figures)

**PASS condition (ledger row L7.1):** Phase J beats best-count by **+0.105 nats/char** on the sealed held-out
OOV/morphology split, with:

- **21-split M-seal CI [0.0975, 0.1128]** (the CI lower bound 0.0975 excludes 0 — verdict is this bound, not the
  point estimate);
- **structure margin +0.109**;
- the result **holds in BOTH the web and dictionary domains**;
- the **contains-KN-OOV control λ=0** (no leakage through the count baseline).

**Mandatory paired citation (ledger row L7.2):** the PASS is only validly stated together with
`J.attribution_caveat` (overall NLL worsens — specialist gain, not a general win). The +0.105 figure may
**never** be cited alone.

This is the **only PASS at L7**, and it is a *specialist* PASS. It does not raise the rung above its class.

---

## Falsifier (operable)

The Phase J PASS is falsified if **any** of the following hold (ledger row L7.1):

- On a fresh OOV/morphology held-out split, the **CI lower bound includes or falls below 0**; OR
- the **structure-margin discriminator does NOT collapse the gain under marker-swap** (the gain was not the
  morphological structure it was claimed to be); OR
- the result **fails to replicate in the dictionary domain**.

(The paired `J.attribution_caveat`, row L7.2, has no separate falsifier — removing it from any citation of
Phase J **is** the violation.)

---

## Recorded NEGATIVE(s) — first-class, inline, the central wall

These are *results*, not failures to hide. They are the credibility (the corpus carries 183 published
negatives). At L7 the negatives are the central content of the rung.

- **`J.attribution_caveat` — paired, mandatory (ledger L7.2, Class C).** Overall NLL **worsens** under Phase J:
  the +0.105 nats/char is an **OOV/morphology specialist gain, not a general language improvement.** Always
  cite it alongside the PASS. Citing +0.105 without it is an overclaim.

- **Comprehension-above-retrieval = the thrice-NEGATIVE "central wall" (ledger L7.3, Class C).** **K≥3
  structurally-distinct** no-backprop designs all FAIL to beat retrieval-style baselines on adversarial
  comprehension. This is a **genuine published wall (K≥3), not a hidden failure.** Falsifier: a pre-registered
  held-once no-backprop comprehension design beats the tuned retrieval/recency baseline with a CI excluding 0.

- **Phase K role-persistence (ledger L7.4, Class C — bound).** Three structurally-distinct no-backprop designs
  (min-role, chain, track) all **tune their role/persistence terms OFF**; only **~0.02 nats survives, and its CI
  spans 0.** Bound: no-backprop role-persistence does not beat a tuned recency/frequency discourse prior on
  adversarial anonymized referent cloze. Falsifier: a no-backprop role-persistence design beats the tuned
  discourse prior with a CI excluding 0.

- **T2.D3 bounded-peek, held one-shot, s64-signed (ledger L7.5, Class C — bound; fabrication corrected).**
  Primary full-read match is **NEGATIVE** (the `k_b=2` backoff wall); info-gain is **NOT load-bearing.** The
  variable-`k_b` "cheap milder cap" was **asserted then disproven by measurement** (the real dev screen showed a
  ~linear curve — there is no cheap cap). The honest correction is part of the record. Falsifier: on the held
  one-shot, bounded-peek full-read match shows a positive load-bearing info-gain with a CI excluding 0.

- **Char-perplexity / T2 word-grain frontier — PARKED (ledger L7.6, Class U).** PARKED at the embodiment pivot.
  Perplexity is the rejected LLM metric; the program measures developmental capability, never perplexity. The
  park WORDING was **SIGNED 2026-06-27** (Q1, below); the sign-to-park remains **OWED / not yet captured**, so
  the frontier stays **PARKED**. The park stays PARKED; **no rung is raised.**

### The park WORDING, stated exactly (SIGNED Q1, 2026-06-27 — the LOAD-BEARING frontier wording; the sign-to-park itself remains OWED)

UNI signs the park as a **ledger-scoped exhausted search envelope — NOT a universal impossibility result and
NOT an achieved rung.** UNI will NOT sign the phrase "published exhausted bound"; what exists is a published
*negative frontier result* over the tested envelope only. Canonical signed wording:

> We park the L7 char-perplexity / T2 word-grain frontier and the L9–L10 role-persistence ladder as a
> **ledger-scoped exhausted search envelope, not a universal impossibility result.** Under the recorded corpus,
> splits, metrics, implementation, compute budget, ablation set, and comparison baselines in the ledger, no
> tested within-segment no-backprop structure improved char-perplexity beyond the tuned MKN-7 count baseline.
> This establishes a negative bound **over the tested envelope only.** It does not establish that all K≥3
> structures are exhausted, that no future within-segment model can improve, or that any broader
> language-modeling frontier has been closed.
>
> Char-perplexity is recorded as a **chosen design trade, not a failed claim of general language superiority**:
> World C remains a count-model baseline — not an active-inference demonstration, not a beats-LLMs claim, not
> evidence of human-level language capacity.

**Banned phrasings → signed replacements (Q1):**

- "K≥3 exhausted" → **"The registered tested K conditions did not reverse the result."**
- "Sec-0.6(B) achieved" → **"Sec-0.6(B) remains unearned / parked pending a future result that beats the
  registered discourse prior under ledgered evaluation."**
- "UNI demonstrates language/metacognition at L9–L10" → "UNI records a negative L9–L10 frontier test under the
  no-backprop developmental simulation program."
- "This proves no no-backprop model can beat MKN-7" → "No tested no-backprop variant in the registered envelope
  beat MKN-7 on the chosen char-ppl metric."

---

## HONEST FENCE — **proven (specialist) + NEGATIVE (central wall)**

**Status: proven** (Class C, held / sealed / UNI-signed, falsifier still live) **for the Phase J specialist
PASS only**, *always* carried with its paired `J.attribution_caveat` NEGATIVE; **plus a first-class NEGATIVE
central wall** (the thrice-NEGATIVE comprehension bound, the role-persistence bound, the T2.D3 bound) and a
**parked frontier** held as a ledger-scoped exhausted search envelope. The rung's overall status is
**UNCHANGED** by any of the SIGNED Q1 park language: the park RAISES NOTHING.

**Not claimed (load-bearing, never softened):** **no general language capability.** This is **not** comprehension,
**not** "talking," **not** "understands," **not** human-level language, **not** AGI, **not** "active inference
demonstrated," **not** "beats LLMs." Reading = posterior inference, speaking = action — at textbook level only.
**Comprehension above retrieval is a genuine published wall (K≥3), not a hidden failure.** The +0.105 figure is
a specialist OOV/morphology gain whose overall NLL worsens, never a general win. "K≥3 exhausted" and
"Sec-0.6(B) achieved" are **forbidden phrasings**; per the SIGNED Q1 above the parked frontier is a
**ledger-scoped exhausted search envelope, never a "published exhausted bound."** Honest program position:
**~2 of 11+ rungs earned** — a developmental SIMULATION, a bounded peek, a toy world, not a person.
