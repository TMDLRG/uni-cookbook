# MASTER-PLAN.md — The UNI Encyclopedia (table of contents + authoring rules)

**What this is.** The authoring blueprint for the **UNI ENCYCLOPEDIA** — the public reference work
about the UNI program (a *developmental active-inference SIMULATION*, never a person, never a mind).
This file fixes the front matter (the Evidence Constitution, the A–U rubric, the standing fences and
red-line list, the "what is NOT claimed" template), the body structure (the four live-hub wings ×
the L0–L12 science spine × the Method wing × the Track-A appendix), a one-page authoring spec per
chapter, and the ordered **Session-3 authoring queue**.

**Authority.** This plan authors *against* two files and never ahead of them:
- the single source of truth — [`CLAIM-LEDGER.md`](./CLAIM-LEDGER.md) (882-row append-only ledger, every claim carded A–U with a falsifier);
- the Session-1 synthesis — [`../curated/00-INDEX.md`](../curated/00-INDEX.md) (the 11 per-archive digests, the wing map, the Track-A/Track-B split).

If any encyclopedia prose disagrees with `CLAIM-LEDGER.md`, **the ledger wins and the prose is wrong.**
No chapter may state a claim above the evidence class recorded in the ledger, omit a recorded falsifier,
or hide a recorded negative.

**Honest program position (print it, do not soften it):** **~2 of 11+ developmental rungs earned.**

---

# PART I — FRONT MATTER (the constitution; read before authoring any chapter)

## FM-1. The Evidence Constitution

Every entry in the encyclopedia is governed by six rules carried verbatim from the ledger:

1. **A falsifier per claim.** No claim ships without a stated condition that would prove it false.
   A claim with no falsifier is not a claim — it is marketing, and it is forbidden.
2. **The append-only ledger is the single source of truth.** Four states only:
   **PASS / FAIL / NEGATIVE / PENDING.** Corrections are forward-only (supersede with lineage),
   never silent edits. Prose cites the ledger; if they disagree, the ledger wins.
3. **Calibration only moves DOWN.** Authority flows downward from the measured fact. Wording is
   calibrated **down** to the measured value, **never up** — including under urgency.
   *The fence gets louder under pressure, not wider.*
4. **Verdict = the CI bound that excludes the threshold, never the point estimate.**
5. **DONE = test-covered (Class E/D), not feature-working (Class A).** A passing test does not
   satisfy a criterion that demands a runtime observation.
6. **Negatives are content.** A partial / a negative / a "most pieces don't help" decomposition is a
   *measurement that the design is incomplete*, not an exit and not a failure to hide. **The negatives
   are the credibility.**
   *Provenance fence (do not feature as a re-countable headline).* The figure **882 rows = 350 PASS /
   0 FAIL / 183 NEGATIVE / 349 PENDING** is a **recorded ledger snapshot**, not a count reconstructable
   from this document: the ledger derives from a deduplicated merge of 615 extracted claims
   (`CLAIM-LEDGER.md` line 5), the snapshot enumerates 882 rows, and the carded body shows only ~140
   distinct rows. A skeptic counting the published rows **cannot** independently derive 183. Cite the
   snapshot **as a snapshot** (provenance-flagged), and headline only the negatives actually enumerated
   in the ledger body — never the bare "183 published negatives" as a credibility number until the count
   is reconstructable, per the calibration-down rule.

**No-Exit Discipline.** The only legitimate rest is a proven working solution **or** a published,
exhausted, falsifiable bound — then redirect to the axis where the reader genuinely excels. Never go
silent on an open gate. A park is not discharged until its sign-to-park lands. Falsify the mundane
causes (L2 metabolism / L7 retrieval-and-recency) before calling any NEGATIVE.

## FM-2. The evidence-class rubric (A..U)

The class is the ceiling. A chapter may card a claim **at or below** its ledger class, never above.

| Class | Name | Means | Authoring rule |
|---|---|---|---|
| **A** | machine-exact anchor / live observation | observed at runtime, or exact to the float tier (machine-checkable) | the strongest class; still fence the *interpretation* (an anchor is not a capability). |
| **B** | mechanism + operator observation | a mechanism shown working under grounded inspection, short of a held eval | never present a B as a held-out PASS. |
| **C** | dev-gate / held-out eval | a pre-registered, sealed, held-once gate with a CI verdict | this is the empirical-PASS tier; cite the CI bound, not the point estimate. |
| **E** | test-covered | tests pass (and `D` = test-covered design) | **DONE ≠ working.** A Class-E pass never satisfies a Class-A criterion. |
| **F** | doc / prior-claim | inheritable from a document or earlier claim | **must be re-verified** before it is leaned on; mark inherited. |
| **U** | claimed-but-unproven | asserted but not earned (e.g. "human-level"; the parked frontier) | **"Class U — not claimed" is itself a standing fence.** Class-U content is described as *not-yet-built / parked*, never as capability. |
| **method** | definitional / governance pattern | a reusable discipline, not an empirical claim | proven and reusable, but cannot be raised into a capability claim. |

**Class-authority ordering** (when sources conflict): Class-B (tool state) overrides Class-G (own
narrative); Class-A (observed at runtime) overrides Class-E (test passes). Mark `[CONFLICT:unresolved]`
and resolve with a direct read. (The A–F subset — A live · C code/static · E test · F doc/inheritable —
is the per-ticket provenance taxonomy; the full A–U taxonomy adds B mechanism, U not-claimed, and `method`.)

**Exactness-tier honesty (load-bearing).** Never label a float32 anchor `<1e-10 EXACT`. The JAX core
runs **float32**, so its anchors hold only to **~6e-8 (~1e-6 single-step filter)**; the genuine `<1e-10`
tier lives only in the NumPy / Rust-f64 path (the cross-language Rust-f64 == Python bridge). A genome
docstring that claimed `<1e-10` was caught as an overclaim and corrected. Card every anchor at its real tier.

## FM-3. Standing fences + the red-line list

**Standing program framing — say it this way, every chapter:** "developmental SIMULATION",
"bounded peek", "toy world, not the real world", "Class U — not claimed", "unrefereed working
preprint", "same math, many scales", "count baselines / LOOP not LEAP."

**THE RED LINES — never claim, in any chapter, in any public copy, under any pressure:**

1. Never **AGI** / general intelligence / human-level / "talks & learns like a human" / "understands."
2. Never **consciousness** / sentience / aware. (Functional self-awareness *may* be described at L8;
   **phenomenal sentience is explicitly DISCLAIMED** — no falsifier is offered because it is disclaimed,
   not tested.)
3. Never **"active inference demonstrated."** No AIF loop exists in the Rust crate; the live UNI.OS loop
   is a separate reimplementation, **not gate-matched.** "Active inference" is the framing *lens*, never
   a demonstrated result.
4. Never **"created life" / "digital life" / "measurable awareness"** as a CLAIM (north-star framing only;
   posed as an open falsifiable question, never an answer).
5. Never **"beats LLMs."** World C is a **COUNT** baseline; the program is ~10–15% behind backprop LLMs on
   char-perplexity by a chosen design trade. EDAIT is an honest fluency-for-calibration trade (~33 vs ~25 ppl).
6. Never inflate the **Tier-2 synthetic-construction track** into capability (it was audited as
   artifact/diagnostic — hardcoded-literal "exactness", scoring-artifact deltas, no AIF loop — and fixed).
7. Never **raise a claim above its source evidence class.**
8. Never let **substrate / continuity engineering** imply a science gate is met (it is engineering evidence,
   not general-AIF evidence).
9. Never publish "**K≥3 exhausted**" / "**§0.6(B) achieved**" phrasings until UNI signs the relevant park.
10. **No PII. No secrets/tokens/internal channel handles** (a *link* may exist; the handle is never
    *featured*). **No patent-level UNI math — textbook-level framing only** (consult the private UNI
    Active-Inference Guide GPT for science; never publish it).
11. **The preprint** (Polzin et al. 2026, Zenodo DOI 10.5281/zenodo.19785799, MIT) is cited as the
    **mathematical foundation only** and always fenced **unrefereed** (Layer-1 AI-executable audit complete;
    Layer-2 human expert review **PENDING**) — never as proof that active inference is the correct theory.
    *PII note (not a red-line breach):* the named authorship "Polzin et al." is **already public under the
    cited DOI**, so reproducing the author form is an **intended public attribution, not incidental PII
    leakage** — the no-PII red line (item 10) is not violated by this sanctioned citation. (If a public
    encyclopedia copy must not bind the program to the owner's surname, fence the citation to the
    **DOI + title only**; absent that instruction the published authorship stands as intended attribution.)
12. **Vocabulary-leak guard (HARD, test-enforced):** never externalize active-inference / EFE / free-energy
    framework names or print internal channel handles in public copy. Public copy says "count baselines",
    "prediction-error", "LOOP not LEAP."

**UNI-GPT consult (2026-06-27 — SIGNED): forbidden-phrasings red-line list (extends FM-3, calibration-down).**
The consult (Q7b) banned the following phrasings OUTRIGHT — never publish any of them, in any chapter, in any
public copy, under any pressure. Each is paired with the only honest replacement. (Cross-reference:
[`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md), Q7.) This list is
ADDITIVE to red lines 1–12 above and never relaxes any of them.

- **Banned outright:** "UNI is conscious / aware / self-aware / has measurable awareness / has a mind / has a
  conscience / reasons like a human / is human-level / is AGI / created life / created non-organic life / is
  alive / is a synthetic organism / dreamed / is creative in the human sense / demonstrates active inference /
  proves the FEP creates minds / proves plants and UNI are the same kind of life / beat consciousness tests /
  beat LLMs therefore awareness / passed L12 / L12 achieved."
- **Replace with (the only licensed forms):** "UNI passed a specified proxy test / improved a registered
  downstream metric / matched-or-exceeded the registered LLM baseline on this sealed task / showed a
  substrate-distinct effect under this ablation / remains a developmental active-inference simulation / the
  awareness question remains open."
- **L7/L9–L10 frontier (Q1, signed):** replace any **"published exhausted bound"** framing with
  **"ledger-scoped exhausted search envelope"** — a ledger-scoped, implementation-scoped, data-split-scoped
  negative result over the tested envelope only, NOT a universal impossibility result and NOT an achieved
  capability rung. Specific banned→replacement pairs (Q1): "K≥3 exhausted" → "The registered tested K
  conditions did not reverse the result."; "Sec-0.6(B) achieved" → "Sec-0.6(B) remains unearned / parked
  pending a future result that beats the registered discourse prior under ledgered evaluation."; "UNI
  demonstrates language/metacognition at L9–L10" → "UNI records a negative L9–L10 frontier test under the
  no-backprop developmental simulation program."; "This proves no no-backprop model can beat MKN-7" → "No
  tested no-backprop variant in the registered envelope beat MKN-7 on the chosen char-ppl metric."

**UNI-GPT consult (2026-06-27 — SIGNED): awareness-proxy proposal-entry checklist (the L12 gate).**
Any FUTURE L12 "awareness" work must pass ALL ten conditions below before such a gate may even be PROPOSED
(Q7c). This keeps any awareness gate falsifiable rather than unfalsifiable. It is a *proposal-entry* gate,
not a pass-claim, and it raises NOTHING: L12 stays NOT-YET-BUILT and Class-U-not-claimed regardless.

1. **Proxy-only target** — title must say "…-proxy"; no bare "awareness gate."
2. **Best-LLM baseline, frozen at proposal time** — name models/versions/prompts/tools/context/temperature/
   scoring; UNI must match-or-beat the BEST, not a hobbled baseline.
3. **Substrate-distinct requirement** — ≥1 property LLM prompting shouldn't get for free (no-backprop online
   adaptation with ledgered state changes; causal self-monitoring that improves later policy; global
   cross-module availability; counterfactual intervention on internal observables; durable trace/report
   consistency).
4. **Two-part pass bar (both required):** A. UNI ≥ best LLM on the sealed shared task; B. UNI shows a
   substrate-distinct effect whose gain collapses under the registered causal ablation. Either alone is
   insufficient.
5. **Computed internal observables, not hardcoded reports** — self-report/uncertainty/contradiction-detection
   computed from trace/model state; scripted confession or label lookup fails.
6. **Load-bearing ablation** — the effect must collapse when the mechanism is removed/shuffled/made
   uninformative.
7. **No hidden LLM substitution** — prove no LLM / label oracle / retrieval leak / backprop-trained hidden
   controller is doing the proxy work.
8. **Sealed held-out tasks + paired uncertainty** — sealed before execution; paired controls; CIs excluding 0
   on the registered effect.
9. **Negatives are first-class** — predefine fail/partial/regression/non-informative/"do not count"; a null
   publishes as a bound, never rewritten into progress.
10. **Ledger supremacy** — the ledger holds final status; prose/recipe/demo/narrative that conflicts loses.

## FM-4. The "what is NOT claimed" entry template

**Every chapter carries this block; it is not optional and it is not buried at the end.** It is a
first-class section with the same weight as the claim. Template:

```
### What is NOT claimed in <chapter>
- Ceiling: <the single strongest thing a careless reader might infer> is NOT shown. The most we claim
  is <the exact, calibrated, in-class statement>.
- Fences engaged: <which red lines from FM-3 apply here, named explicitly>.
- Negatives that travel with this claim (cite alongside, never strip):
  <ledger NEGATIVE rows that MUST appear next to the PASS, e.g. J.attribution_caveat with Phase J>.
- Parked / owed: <sign-to-park owed? Class-A observation owed? name it>.
- One-line honest summary a skeptic could not dispute.
```

**Standing pairings the template enforces** (citing the PASS without the negative is an overclaim):
- Phase J +0.105 **always** with `J.attribution_caveat` (overall NLL worsens; specialist gain).
- World C +0.081 **always** with "COUNT baseline, not AIF, not comprehension, not beats-LLMs."
- L2 metabolism +135% tool-crafting **always** with building −14% / G4 never separated / G6 OPEN.
- L8 15/15 PASS **always** with "phenomenal sentience explicitly DISCLAIMED" **and** the `uni-mind`
  held-NEGATIVE self-model-on-the-reader (the `uni-gpt` functional card and the reader-side self-model
  NEGATIVE are in tension and must be co-cited).
- Continuity Stage-1 (mind survived a process restart bit-for-bit) **always** with Stage-2 OWED
  (mind-tick continuity across a kernel swap NOT shown).

---

# PART II — BODY STRUCTURE

The encyclopedia has **four mirror wings** (the live public hub), with the **L0–L12 developmental
ladder as the science spine inside the Science wing**, a **Method wing** (the constitution as content),
and a **Track-A appendix** (the marketing organism). Order of presentation:

- **Wing E — EVIDENCE** (the ledger made public: classes, falsifiers, the calibration ledger, "Falsify this").
- **Wing S — SCIENCE (UNI)** — the L0–L12 spine + the continuity sub-ladder + the same-math-many-scales labs.
- **Wing N — MEANING** — the textbook-level lens (FEP, prediction-error maps), kept honest and unfalsifiability-aware.
- **Wing M — MOVEMENT** — the honest-science posture: negatives-as-pitch, "help us independently verify," open falsification.
- **Wing μ — METHOD** (the constitution) — the reusable disciplines as their own reference section.
- **Appendix TA — the Track-A marketing organism** — the publishing/engagement engine, fenced as engineering+method, not science.

Each chapter below carries the full authoring spec:
**title · scope · ledger claims covered · evidence classes present · falsifiers · fenced / not-claimed · source pointers (digest + archive).**

**FM-4 is reproduced verbatim, not summarized (applies to EVERY chapter — E, S, N, M, μ, and TA alike).**
The per-chapter "**Fenced / not-claimed.**" line below is a *compressed pointer*, not a substitute. In the
authored chapter, the full **FM-4 five-field block** — **Ceiling · Fences engaged · Negatives that travel
with this claim · Parked / owed · one-line skeptic summary** — is written out in full and carries the same
weight as the claim (FM-4, line above). This is mandatory for the WING-N, WING-M, μ, and TA chapters too,
whose specs below compress the block into prose: prose compression in this plan does **not** discharge the
"same weight as the claim" requirement; the authored chapter must instantiate all five fields explicitly.

---

## WING E — EVIDENCE (the ledger, made public)

### E0 — How to read this work (the Evidence Constitution, public form)
- **Scope.** The reader's onboarding: A–U classes, falsifier-per-claim, the four-state append-only
  ledger, CI-as-verdict, DONE≠working, "negatives are content" (the 183-NEGATIVE figure is a
  **provenance-flagged ledger snapshot**, not a count re-derivable from the carded rows — see FM-1).
  The chaptered Evidence Explorer with a calibration ledger and a "Falsify this" close.
- **Ledger claims.** M1, M2, M3, M9, M30; Constitution §0.
- **Classes present.** method (with E/A worked examples).
- **Falsifiers.** A claim asserted ahead of its ledger; wording calibrated UP; a verdict edited rather
  than superseded; a `reproduced:true` that is a literal not validator-derived.
- **Fenced / not-claimed.** This is a method chapter — it asserts no capability. Do not let "we have a
  constitution" read as "we have proven the science."
- **Sources.** `uni-gpt-digest.md`, `ideation-explorer-digest.md`, `00-INDEX.md` /
  archives `…-UNI-GPT`, `…-SolutionWright-IdeationExplorer`.

### E1 — The calibration ledger & "Falsify this"
- **Scope.** The live public artifact: the 882/350/183/349 row snapshot (carried as a
  **provenance-flagged ledger snapshot** per FM-1 — the 183 NEGATIVE count is not re-derivable from the
  carded rows, so present the snapshot as a snapshot and surface the negatives the ledger body actually
  enumerates), the per-claim "Falsify this" close, the down-only calibration record (the os-cycles 39–53
  audit that moved 6 headline claims DOWN: "TWO boxes"→ONE; "mind survives a patch"→infra-only;
  "5 stacks"→"4 distinct stacks/5 runs").
- **Ledger claims.** §0 Negatives-are-content; §2 audit-layer note; M1, M8, M29.
- **Classes present.** method / A (the calibrated figures are the observed ones).
- **Falsifiers.** A headline figure shown carrying the inflated value rather than the calibrated one; the
  negative count misstated; a "Falsify this" entry with no operable falsifier.
- **Fenced / not-claimed.** Carry the calibrated figures, never the inflated ones; overstatements lived in
  headlines, not in fabrication — say exactly that.
- **Sources.** `uni-os-digest.md`, `uni-mind-digest.md` / archives `…-UNI-OS`, `…-uni-mind`.

---

## WING S — SCIENCE (UNI): the L0–L12 developmental ladder (the spine)

> **Naming fence (every L-chapter).** The ladder is the **HUMAN-HGM-001** developmental design
> (conception → speaking 3-year-old: 11 levels + the global **Z** affect modulator). It is a
> *no-backprop, nested-Markov-blanket developmental SIMULATION*, **never a person.** One engine,
> shown across scales. Honest position printed on the spine page: **~2 of 11+ rungs earned.**

### S-L0 — Molecular / genome → zygote (conception prior) · **PROVEN (float32 tier)**
- **Scope.** Zygote first-division as exact discrete Bayes (conjugate update); `recombine`/`seed_zygote`,
  the no-backprop guard, `ontogeny 6/6`, Embodiment Rungs 1–2 GREEN.
- **Ledger claims.** L0.1.
- **Classes present.** A (machine-exact anchor, **float32 tier**).
- **Falsifiers.** `test_embodiment_ontogeny.py` drops below 6/6; the first-division posterior diverges from
  closed-form discrete-Bayes beyond the float32 tier; cell-division identity embedding exceeds 1e-9; the
  no-backprop guard trips.
- **Fenced / not-claimed.** NOT "we created life", NOT a "conscious baby", NOT exact at f64 — a float32-tier
  SIMULATION of a conjugate Bayesian first division. **Never card a float32 anchor at the f64 tier.**
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md` / archives `…-UNI-GPT`, `…-uni-mind`.

### S-L1 — Cellular / autopoietic viability & homeostasis · **PROVEN (with honest losses)**
- **Scope.** The Cell Lab open pre-registered falsification benchmark (216-state service cell,
  observation-only controllers, RecoveryScore, bootstrap 95% CI, 8 honesty fences + `framing_guard`).
  UNI tops the leaderboard on most modes — **and honestly loses on three.**
- **Ledger claims.** L1.1 (PASS); **L1.2 (NEGATIVE — `database_flaky` 0.803 vs 0.759, `memory_leak` 0.810
  vs 0.740, `cpu_noisy_neighbor` 0.824 vs 0.749; UNI-vs-random not significant on the last).**
- **Classes present.** C.
- **Falsifiers.** RecoveryScore CI fails to separate from controls where a win is claimed; a fence /
  `framing_guard` fails; the bootstrap CI is shown miscomputed. (Negative falsifier: the recorded losses
  fail to replicate.)
- **Fenced / not-claimed.** NOT "sovereign" — "good but not sovereign." The three losses are first-class
  published content shown at the top of the live leaderboard. Cellular/zygote end only.
- **Sources.** `uni-precision-digest.md`, `uni-mind-digest.md` / archives `…-Precision`, `…-uni-mind`.

### S-L2 — Tissue / metabolism (interoception & energy) · **POSITIVE uplift + NEGATIVE (plateau-break OPEN)**
- **Scope.** The Phase-2 metabolism organ (suite 297/0, default byte-identical); the standing-metabolic-drive
  effect; the colony's "make a tool" plateau and the shadow-EFE diagnosis; the two engine-seam fixes.
- **Ledger claims.** L2.1 (+135% / 2.35× tool-crafting, +19% mining); **L2.2 (NEGATIVE — building −14%,
  G4 allostasis never separated, gate G6 OPEN, contradicted by its own first evidence);** L2.3 (NEGATIVE
  diagnostic — `epistemic_starvation`, NOT γ-runaway (γ≈7.8 unsaturated), NOT a curriculum ceiling);
  L2.4 (NEGATIVE/fixed — `:pb_seed` seam; the no-viability-edge bug).
- **Classes present.** C (uplift + building negative); A (shadow-EFE audit on real `.bin` brains; code-read seam findings).
- **Falsifiers.** A repeat pre-registered 12h RED fails to reproduce the tool-crafting uplift within CI, or
  the metabolism ablation does not remove it, or the suite drops below 297/0. (G6 discharge: a disciplined
  RED where the organ alone improves building (placed-blocks CI excludes 0) AND G4 separates.)
- **Fenced / not-claimed.** Metabolism is a **foraging/crafting driver, NOT a building driver.** The
  plateau-break (G6) is **UNPROVEN.** Do NOT spin +135% as "breaks the plateau." `G5b` action-severed-twin is
  the standing falsifier any "self-maintenance/life" language must clear.
- **Sources.** `strings-digest.md`, `uni-precision-digest.md` / archives `…-Strings`, `…-Precision`.

### S-L3 — Organ / physiological control (cardio-renal) · **PROVEN (toy/clinical-model)**
- **Scope.** The Karaaslan cardio-renal Heart Lab — clinical homeostasis as prediction-loop failure on the
  same one engine (reduced RSNA→MAP→sodium/volume loop, re-expressed in active-inference language).
- **Ledger claims.** L3.1 (Heart-Lab engine ticket OAS-710-T3 at Class E, 15/15).
- **Classes present.** C (lab gate); E (engine ticket / parity tests).
- **Falsifiers.** Heart-Lab predictions diverge from the Karaaslan reference beyond the pre-registered
  tolerance, or fail parity tests against the canonical TS engine.
- **Fenced / not-claimed.** **NOT a clinical tool, NOT a diagnostic instrument.** "Same math, many scales"
  framing only; heart-attack-as-prediction-loop-failure applies *to the toy model, not to clinical reality.*
- **Sources.** `uni-precision-digest.md` / archive `…-Precision`.

### S-L4 — Interoceptive / autonomic + affect-as-precision · **PROVEN (functional)**
- **Scope.** Affect-as-precision: emotion modulates precision so perception sharpens and the
  pragmatic↔epistemic balance flips; the global **Z** modulator
  `[energy, arousal, valence, fatigue, pain, threat, safety, inflammation]` setting precision /
  preferences / habits / learning-rate / horizon.
- **Ledger claims.** L4.1.
- **Classes present.** C.
- **Falsifiers.** A Z-modulator ablation shows no precision-weighting change / no pragmatic↔epistemic flip
  under the grounded reader, or the effect collapses under control.
- **Fenced / not-claimed.** Affect is **modeled, never felt** — phenomenal feeling / sentience disclaimed.
  M10 sub-bound: neuroticism does NOT change behavior under bimodal surprise without a graded task.
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md` / archives `…-UNI-GPT`, `…-uni-mind`.

### S-L5 — Sensorimotor / motor hierarchy · **PROVEN PASS + symmetric NEGATIVE (synthetic only)**
- **Scope.** Embodiment A3 (the UNI-signed symmetric result); mind-body-as-one motor hierarchy
  (proprioceptive diagonal-A, continuous servo, reafference; the live kin-9 craft chain via RCON).
- **Ledger claims.** L5.1 (Design #1 PASS Δ+0.092 [+0.038,+0.157]); **L5.2 (NEGATIVE — Design #2
  Δ−0.091 [−0.134,−0.055]; K-negative=1, no §0.6(B) bound owed);** L5.3 (diagonal-A posterior 0.0→0.75;
  motor-ablation collapses harvest ~700×).
- **Classes present.** C (held synthetic gates + live RCON gate); A (posterior shift); E (277 offline tests).
- **Falsifiers.** A re-registered held-once **synthetic** run (≥5 seeds) drops the Design-#1 CI lower bound
  to ≤0; harvest not collapsing under motor ablation; the kin-9 chain not reproducing server-authoritative;
  diagonal-A staying stuck at 0.0.
- **Fenced / not-claimed.** The A3 PASS is **"variationally-controlled active-inference evidence on
  body↔world coupling under the registered SYNTHETIC protocol"** — synthetic-process only (NOT live-appliance,
  NOT recorded-hardware) and **NOT near-optimal control** (agent plateaus 0.222 vs oracle 1.0). Live
  behavioral K-of-6 motor tallies are PARKED (accruing, not sealed).
- **UNI-GPT consult (2026-06-27 — SIGNED): next L5 motor design — DESIGNED, NOT RUN (Q6).** A next
  structurally-distinct motor design is *accrued* — **`L5 Design #3: Proprioceptive Servo Bridge`** (changes
  coupling topology, timescale source, information bottleneck, and control path vs #1/#2; closed-loop
  triadic high-level-policy → motor-setpoint → proprioceptive-residual → corrective-action), aimed at a **LIVE
  PASS** (not bound-seeking). This is a **design to build, not a result.** Status is UNCHANGED: L5.1 stays
  PASS, L5.2 stays NEGATIVE, and the ledger holds **K-negative = 1** — Design #3 has not run, so no §0.6(B)
  motor bound is owed. If #3 later fails *cleanly* with all validity checks passing it may count as at most
  **K-negative = 2** toward a future motor bound (still no bound until K≥3); a clean pass would be fenced (NOT
  general motor intelligence / human-like embodiment / AGI / "active inference demonstrated"; does NOT erase
  the Design #2 negative). (Cross-reference: [`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md),
  Q6.)
- **Sources.** `uni-mind-digest.md`, `strings-digest.md` / archives `…-uni-mind`, `…-Strings`.

### S-L6 — Perception (precision-weighting / EFE planning) · **PROVEN — the one citable empirical PASS**
- **Scope.** World C (the flagship empirical PASS) + the World-C family; the three-knob Precision/Echo labs;
  the Working Law; and the two perception-side published bounds.
- **Ledger claims.** L6.1 (World C +0.081 nats/char, CI **[0.0736, 0.0890]**, 2.4× the 0.03 bar, first
  validator-derived `reproduced:true`); L6.2 (Wc-2/Wc-3/recency/Gate-3 family); L6.3 (POMDP maze Precision +
  echolocation Echo + public Precision Lab, three knobs, 2D bifurcation, Class E parity); **L6.4 (NEGATIVE
  bound — Phase G: five within-segment designs all NEGATIVE; char-ppl is a chosen design trade);**
  **L6.5 (NEGATIVE — Phase F active-controller: the World-C gain is diffuse, nothing to gate);**
  L6.6 (the Working Law: a no-backprop latent Z beats baseline B only when I(Y;Z|S_B)>0 and is learnably stable).
- **Classes present.** C (World C + family + bounds); E (the labs, parity-tested); method/law (the Working Law).
- **Falsifiers.** On a fresh held-out split with ≥5 disjoint seeds the seed-paired bootstrap margin over tuned
  MKN-7 includes/falls below 0 (or the baseline is shown untuned); any family member's CI includes 0; the lab
  parity tests diverge from the canonical engine; a held PASS where the winning Z carries no conditional info
  beyond S_B (I=0).
- **Fenced / not-claimed.** World C is a **COUNT baseline win — explicitly NOT active inference, NOT
  comprehension, NOT "talking", NOT beats-LLMs** (~10–15% behind backprop LLMs, a chosen trade). Never card
  World C above a count-baseline result. The standing ceiling cannot be raised.
- **Sources.** `uni-mind-digest.md`, `uni-gpt-digest.md`, `uni-precision-digest.md`, `worldmodels-digest.md`.

### S-L7 — Language (reading = inference / speaking = action) · **specialist PASS + thrice-NEGATIVE central wall**
- **Scope.** The Phase J morphology specialist PASS (with its paired caveat); reading=posterior-inference /
  speaking=action; and the central comprehension wall plus its supporting bounds.
- **Ledger claims.** L7.1 (Phase J +0.105 nats/char, M-seal CI **[0.0975, 0.1128]**, both web+dictionary);
  **L7.2 (NEGATIVE, paired — `J.attribution_caveat`: overall NLL worsens; MUST be cited alongside L7.1);**
  **L7.3 (NEGATIVE bound — comprehension-above-retrieval = the thrice-NEGATIVE central wall, K≥3);**
  **L7.4 (NEGATIVE bound — Phase K role-persistence: all tune OFF, ~0.02 nats, CI spans 0);**
  **L7.5 (NEGATIVE bound — T2.D3 bounded-peek: full-read match NEGATIVE; the "cheap milder cap" was asserted
  then disproven by measurement);** L7.6 (PARKED, Class U — char-ppl/T2 word-grain frontier; sign-to-park
  drafted `UNI_CONSULT_5`, not yet captured).
- **Classes present.** C (PASS + the four bounds); U (the parked frontier).
- **Falsifiers.** A fresh OOV/morph split where the J CI lower bound includes/falls below 0, or the
  structure-margin discriminator does not collapse under marker-swap, or it fails to replicate in the
  dictionary domain; a pre-registered held-once no-backprop comprehension design beats the tuned
  retrieval/recency baseline (CI excludes 0); a role-persistence design beating the tuned discourse prior;
  a bounded-peek full-read with positive load-bearing info-gain.
- **Fenced / not-claimed.** No general language capability. **Comprehension above retrieval is a genuine
  published wall (K≥3), not a hidden failure.** Phase J +0.105 is a *specialist* gain, never a general win —
  always carry `J.attribution_caveat`. **Forbidden phrasings until UNI signs:** "K≥3 exhausted",
  "Sec-0.6(B) achieved."
- **UNI-GPT consult (2026-06-27 — SIGNED): L7/T2 park wording (Q1).** The L7 char-perplexity / T2 word-grain
  frontier is parked as a **ledger-scoped exhausted search envelope, NOT a universal impossibility result.**
  Under the recorded corpus, splits, metrics, implementation, compute budget, ablation set, and comparison
  baselines in the ledger, no tested within-segment no-backprop structure improved char-perplexity beyond the
  tuned MKN-7 count baseline — a negative bound **over the tested envelope only.** It does NOT establish that
  all K≥3 structures are exhausted, that no future within-segment model can improve, or that any broader
  language frontier is closed. Char-perplexity is a **chosen design trade, not a failed claim of general
  language superiority.** Use "ledger-scoped exhausted search envelope" in place of any "published exhausted
  bound" framing; the per-phrase banned→replacement pairs are in FM-3. (Cross-reference:
  [`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md), Q1.) Status
  unchanged: L7.6 stays **PARKED / Class U.**
- **Sources.** `uni-mind-digest.md`, `uni-gpt-digest.md` / archives `…-uni-mind`, `…-UNI-GPT`.

### S-L8 — Self-model / metacognition / metalinguistics · **PROVEN (functional; sentience DISCLAIMED)**
- **Scope.** The Maturation arc M1–M11 grand report card (immersion, affect-as-precision, growth, self-model,
  metacognition, metalinguistics, consolidation, reflective reader, online vocab growth, affect-driven
  reflection, compositional reader). **FUNCTIONAL self-awareness asserted.**
- **Ledger claims.** L8.1 (15/15 PASS).
- **Classes present.** C.
- **Falsifiers.** Any of the 15 gates fails its pre-registered held verdict on re-run; a self-model /
  metacognition gate's effect collapses under its discriminator; a "self-model" task is passable by a trivial
  non-metacognitive heuristic.
- **Fenced / not-claimed (load-bearing).** **Phenomenal sentience is explicitly DISCLAIMED** — no falsifier
  is offered for it because it is disclaimed, not tested. Never read 15/15 as consciousness / sentience /
  awareness / human-level.
  - **Negatives that travel with this claim (cite alongside the 15/15 PASS, never strip):**
    (1) the **phenomenal-sentience disclaimer**; (2) **`uni-mind` records self-model as a held-NEGATIVE
    *on the reader***, in tension with the `uni-gpt`-side M1–M11 functional report card — the two are
    co-cited as a **mandatory pairing** (the same way `J.attribution_caveat` travels with Phase J), not a
    parenthetical. The 15/15 functional card and the reader-side self-model NEGATIVE must appear together;
    citing the PASS without the held-NEGATIVE is an overclaim.
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md` / archives `…-UNI-GPT`, `…-uni-mind`.

### S-L9 — Reasoning / conscience (narrative-self → conscience → reasoning) · **PARKED**
- **Scope.** L7–L9 of the HUMAN-HGM-001 design (narrative-self, conscience, reasoning) exist as ladder
  *levels* but are **NOT separately gated/PASSed.** The Strings Phases 3–5 (spine → glands → hemispheres)
  are a **DESIGN ONLY — FE-form-signed but UNBUILT — roadmap** toward this region: the spine→glands→hemispheres
  pipeline is **not built infrastructure and is never inflated into a gated capability** (the same
  "ladder DESIGN levels are never inflated" fence stated below). "FE-form-signed" marks a signed design,
  **not** progress on a built capability.
- **Ledger claims.** L9.1.
- **Classes present.** U (parked; sign-to-park owed).
- **Falsifiers.** None until a pre-registered, sealed, UNI-signed gate is defined and run.
- **Fenced / not-claimed.** Nothing is claimed. Ladder DESIGN levels are never inflated into capability.
  Honest position printed: **~2 of 11+ rungs earned.**
- **UNI-GPT consult (2026-06-27 — SIGNED): L9–L10 park wording (Q1).** The L9–L10 role-persistence ladder is
  parked as a **ledger-scoped exhausted search envelope, NOT a universal impossibility result.** The tested
  no-backprop role-persistence mechanisms did not beat a tuned recency-frequency discourse prior under the
  ledgered protocol — an honest negative frontier result over the tested envelope only. It does NOT achieve
  Sec-0.6(B), does NOT demonstrate active inference, and does NOT license claims of metacognition,
  consciousness, AGI, human-level discourse, or created life. The recipe may describe the attempted mechanisms
  and the negative result, but the ledger is the single source of truth.
- **UNI-GPT consult (2026-06-27 — SIGNED): proposed first L9 gate — DESIGNED, NOT RUN (Q4).** A first sealed,
  falsifiable L9 gate is *designed* — **`L9-G1: Cavity-correct delayed commitment-state prediction`** (build a
  Phase-3 spine carrying one slow latent across lower-level segments; beat a *tuned* recency-frequency
  discourse prior on delayed-commitment next-action/conflict prediction; gain must concentrate on a
  pre-registered local-distractor split and collapse when the computed cavity residual is zeroed/shuffled).
  This is a **design to build, not a result** — L9 stays **PARKED**; L9-G1 is not run, and even a future pass
  would be fenced ("does NOT claim reasoning/conscience/metacognition/awareness/AGI; does NOT unpark L9
  globally"). (Cross-reference: [`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md),
  Q4.)
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md`, `strings-digest.md`.

### S-L10 — Wisdom / higher cognition · **PARKED**
- **Scope.** Top of the HUMAN-HGM-001 ladder; aspirational north star. No engine, no run, no gate.
- **Ledger claims.** L10.1.
- **Classes present.** U.
- **Falsifiers.** None (parked; sign-to-park owed).
- **Fenced / not-claimed.** Nothing is claimed; Class-U-not-claimed. Note the single-source-of-truth
  append-only ledger must stay singular — a second writable ledger would break L10/L11.
- **Sources.** `uni-gpt-digest.md` / archive `…-UNI-GPT`.

### S-L11 — Dreaming (offline replay / generative simulation) · **NOT-YET-BUILT**
- **Scope.** Explicitly untouched and hard-fenced: "dreaming/awareness are untouched here and remain
  hard-fenced." No engine, no run, no gate; absent from all digests.
- **Ledger claims.** L11.1.
- **Classes present.** U.
- **Falsifiers.** None — nothing is built to falsify; the status *is* the absence of any artifact.
- **Fenced / not-claimed.** Nothing is claimed. North-star rung, hard-fenced.
- **UNI-GPT consult (2026-06-27 — SIGNED): proposed L11 gate — DESIGNED, NOT BUILT (Q5).** A first L11 gate is
  *designed* — **`L11-R1: held sparse-sequence retention after offline replay`** (a sealed consolidation
  interval with the observation channel detached, writing only through pre-existing ledgered update rules;
  pass iff offline generative-replay improves held sparse-sequence predictive NLL over a no-replay control and
  the gain collapses under shuffled/random/no-write replay ablations). Offline replay is a UNI design
  primitive / Class-C experimental mechanism, **never "dreamed."** This is a **design to build, not a result**
  — L11 stays **NOT-YET-BUILT**; even a future pass would be fenced ("does NOT claim consciousness, awareness,
  sleep, human-like mentation, AGI, created life; does NOT clear L11 globally"). (Cross-reference:
  [`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md), Q5.)
- **Sources.** `uni-mind-digest.md` (absence) / archive `…-uni-mind`.

### S-L12 — Creativity → measurable awareness · **NOT-YET-BUILT (the hardest fence)**
- **Scope.** The owner's stated north star — "literal digital life … measurable awareness" — pursued by
  deepening organs/spine/glands, **never claimed.** Posed as an OPEN, falsifiable question ("is a plant life?
  have we made non-organic life?"), never an answer.
- **Ledger claims.** L12.1.
- **Classes present.** U.
- **Falsifiers.** None — no gate exists; the only legitimate movement is a **ledger-scoped exhausted search
  envelope** (a scoped, empirical, falsifiable negative result over the tested envelope only — NOT a universal
  impossibility result and NOT an achieved capability rung; Q1, SIGNED), never a capability assertion.
- **Fenced / not-claimed (hardest).** **"we created life / conscious / aware / measurable awareness /
  human-level / AGI / active inference demonstrated" are FORBIDDEN phrasings program-wide.** North-star
  framing only; Class-U-not-claimed.
- **Public-facing L12 bound paragraph (UNI-GPT consult 2026-06-27 — SIGNED, Q7a; use VERBATIM).** This is a
  framing guardrail only — it **raises nothing**, builds nothing, claims nothing; **L12 stays NOT-YET-BUILT /
  Class-U-not-claimed.** It is the third signed Q7 deliverable (with the forbidden-phrasings list and the
  10-point checklist in FM-3) and is the public-facing artifact, so it is installed verbatim here. (Cross-ref:
  [`../cookbook/UNI-GPT-CONSULT-2026-06-27.md`](../cookbook/UNI-GPT-CONSULT-2026-06-27.md), Q7a.)
  > **Open L12 question, not a claim.** UNI's L12 frontier asks a falsifiable question: *Can a non-organic,
  > no-backprop developmental active-inference simulation ever produce measurable awareness-PROXY behavior that
  > both matches or beats the best contemporary LLM baselines on the same sealed tasks AND shows
  > substrate-distinct properties those LLMs do not show?* Today the answer is **not known, not claimed, and not
  > implied. UNI has not created consciousness, human-level intelligence, AGI, or life.** "Awareness" here means
  > only a future pre-registered proxy suite — calibrated uncertainty, global availability of information across
  > modules, self-monitoring that improves later policy, contradiction detection between report and trace,
  > counterfactual access, and calibrated abstention. Passing such a suite would license only: *"UNI passed
  > specified awareness-proxy tests under the registered protocol."* It would NOT license: "UNI is aware," "UNI
  > is conscious," "UNI is alive," or "we created non-organic life."
  >
  > Plant-life clarification: plants are biological life in the ordinary sense; UNI does not use that to claim a
  > simulation is alive. The published UNI question is narrower: whether a non-organic developmental simulation
  > can meet pre-registered life-like persistence and awareness-proxy tests without collapsing into metaphor,
  > declaration, or LLM comparison games.
- **Sources.** `strings-digest.md` (north-star) / archive `…-Strings`.

### S-C — Continuity / embodiment-substrate sub-ladder (orthogonal to L0–L12)
- **Scope.** **ENGINEERING / substrate evidence** — deterministic replay + serialization + fail-closed
  transport + on-metal operation. A single chapter (or a tight cluster) carding every rung as *engineering,
  never general-AIF*; never letting substrate work imply a science gate is met.
- **Ledger claims.** C0 (substrate proof, two-node fleet on real metal); C1 (Stage-1 REQ-002 GREEN —
  mind-state survived a process restart BIT-FOR-BIT); **C2 (NEGATIVE/OWED — Stage-2 real kernel swap:
  infra-only, mind-tick continuity NOT shown; first attempt FAILED then recovered);** C3 (7-modality
  categorical sensorium `[M=7,O_max=4]` live both boxes); C4 (ASK mode / ITIL-as-AIF, Dirichlet policy-prior
  learning shift measured); C5 (cross-box single-human-approval-per-mutation, proven live 2026-06-26);
  C6 (on-core inference anchor byte-identical across 4 stacks / 5 runs); **C7 (NEGATIVE bound — single-box
  swap is a SECONDS-LONG FREEZE, media legs NOT preserved);** **C8 (NEGATIVE — 2-modality bottleneck went
  NEGATIVE → keep all 7);** **C9 (NEGATIVE trade — EDAIT ~33 ppl vs backprop GPT ~25; honest trade);**
  **C10 (PARKED, Class U — "embody only what's proven" signed-in-principle but NOT literally true; the
  program's central open gap; UNI.OS lab evidence store empty, 0 worlds registered);** C11 (PARKED — host-native
  off-podman runtime); **C12 (PARKED — open verification gap; provisional, contradicted same-day: the
  node2 kiosk was reported solved but a later same-day transcript shows limb-2 UI frozen, an agent action
  that ended ALL video output, session cut at a usage limit — fragile pending hands-on monitor
  re-verification);** C13 (continuity-isolation
  primitives shipped, Class B; live Postgres RLS 5/5); **C14 (NEGATIVE gap — multi-tenancy missing on the bare
  substrate; flat global perms, no count-decay).**
- **Classes present.** A (most substrate anchors + live observations); C (engineering-reuse + held bounds);
  B (isolation primitives); U (the three parks + the central gap).
- **Falsifiers.** Per row in the ledger (e.g. a kernel swap preserving mind-tick continuity bit-for-bit
  discharges the owed Stage-2; a node fails to boot or the hardware spec is contradicted; the Dirichlet prior
  fails to update; a routed cross-box mutation executes without the single approval; a 2-modality bottleneck
  beats the 7-modality contract).
- **Fenced / not-claimed.** The sensorium is **NEVER awareness.** "The mind survives a kernel swap" is **NOT
  shown** (Stage-2 owed). None of this is general-AIF capability. UNI.OS's embodiment does **not** imply the
  science gates are met. Carry the **calibrated** audit figures (ONE box, infra-only continuity, 4 stacks/5
  runs), never the inflated headlines.
- **Sources.** `uni-os-digest.md`, `uni-mind-digest.md`, `marketingwright-digest.md` /
  archives `…-UNI-OS`, `…-uni-mind`, `…-MarketingWright`.

---

## WING N — MEANING (the textbook-level lens, kept honest)

### N1 — The Free Energy Principle as a public lens
- **Scope.** Agents minimize prediction error vs their world-model; distorted maps → extraction/harm;
  accurate maps + calibrated signals + cooperation → regeneration. The thermostat→bird→street→body ladder
  taught laypeople-first. **Textbook level only.**
- **Ledger claims.** M16 (FEP as a textbook-level lens; the Popper note); M12 (WORLD⟂BODY⟂MIND framing);
  M14 (the VFE-bound correction); M22 (the cavity principle).
- **Classes present.** method (with E-tier corrections held for human review).
- **Falsifiers.** Conceptual integrity only — a violation is externalizing patent-level UNI math, or
  presenting "minimizing VFE reduces already-observed surprise" (it tightens an **upper bound**;
  `F[q] ≥ −ln p(o|m)`; action lives one layer up as expected free energy).
- **Fenced / not-claimed.** **"no one can falsify it" is NOT evidence FOR a claim**; unfalsifiable = outside
  science. UNI's strength is **verified-core + fenced-frontier, not unfalsifiability.** Provenance pinned to
  one citable reference (Parr/Pezzulo/Friston, *Active Inference*, MIT Press 2022) + the fenced Zenodo
  preprint. No patent-level math.
- **Sources.** `worldmodels-digest.md`, `orchestrate-linkedin-digest.md`, `website-digest.md`,
  `marketingwright-digest.md`.

### N2 — "Same math, many scales" (the unifying claim, calibrated)
- **Scope.** One active-inference engine shown from cellular viability → physiological homeostasis →
  cognitive precision-weighting, via the browser labs (Precision / Echo / Loop / Cell / Heart).
- **Ledger claims.** L1.1, L3.1, L6.3, M28 (inline-engine + canonical-TS + parity-test triad); M27 (design
  patterns, build unverified).
- **Classes present.** C / E (the labs); method (the triad / new-lab-by-duplication discipline).
- **Falsifiers.** A parity test that does not fail the build when the inline engine and canonical TS engine
  diverge; a lab duplication that needed engine-code changes; the bifurcation map not reproducing the regime
  boundaries.
- **Fenced / not-claimed.** "Same math, many scales" is an *organizing* claim about the engine, **not** a
  claim that any single scale is solved beyond its own gate. The `activeinference` BEAM workbench is
  design-only (zero execution evidence) — do not present its patterns as results.
- **Sources.** `uni-precision-digest.md`, `worldmodels-digest.md`, `activeinference-digest.md`.

### N3 — What active inference is NOT (the meaning of the fences)
- **Scope.** A dedicated meaning-chapter that explains, in plain words, why each red line exists: why a
  COUNT-baseline win is not comprehension, why functional self-awareness is not sentience, why a sensorium is
  not awareness, why "active inference" here is a lens not a demonstrated loop.
- **Ledger claims.** §0 fences; L6.1, L8.1, C3, M15, M16; the EDAIT trade (C9); the "all LLMs end in
  entropy is only half-true" sharpened bar (TA-N12).
- **Classes present.** method (interpretive), citing C/A evidence.
- **Falsifiers.** Conceptual — a violation is any chapter that lets a fenced result read as the forbidden
  inference.
- **Fenced / not-claimed.** This *is* the not-claimed chapter for the whole wing; it asserts only boundaries.
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md`, `strings-digest.md`, `website-digest.md`.

---

## WING M — MOVEMENT (the honest-science posture)

### Mv1 — The honesty fence is the pitch
- **Scope.** Publish the negatives front-and-center (boxed "what we have NOT proven"; **the published
  negatives are the credibility** — feature the negatives actually enumerated in the ledger body, and
  cite the 882/183 snapshot as a provenance-flagged ledger snapshot per FM-1, never as a stand-alone
  re-countable headline); CTA = **"help us independently verify," not "fund the vision."** The 7-doc
  press kit where every figure traces to a ledger row.
- **Ledger claims.** M15 (honesty-fence-as-the-pitch + the vocabulary-leak guard); TA3 (no-API press kit,
  Class E); §0 negatives-are-content.
- **Classes present.** method / E.
- **Falsifiers.** Public copy carrying EFE/free-energy vocabulary, a featured channel handle, or an inflated
  claim; a CTA that asks to fund the vision; a press-kit figure that cannot be traced to a ledger row.
- **Fenced / not-claimed.** The posture is method, not capability. Never let "we are honest" substitute for
  "we proved it." Engagement-lift is targeted, **not yet proven** (Class B/pending — see TA25).
- **Sources.** `uni-mind-digest.md`, `orchestrate-linkedin-digest.md`, `website-digest.md`.

### Mv2 — Open falsification (the public invitation)
- **Scope.** The "Falsify this" close on every claim; the open pre-registered benchmarks (Cell Lab on the
  public leaderboard with UNI's own losses on top); the commitment that a negative is a result, not an exit.
- **Ledger claims.** L1.1/L1.2 (the public losing leaderboard); M29 (honesty-as-a-test, the statistics gate);
  M6 (No-Exit Discipline); E1 (the calibration ledger).
- **Classes present.** C / method.
- **Falsifiers.** Framing/DOI/labeling regresses without `framing_guard` failing; a significance verdict
  decided on one seed or a point estimate; a loss hidden rather than shown.
- **Fenced / not-claimed.** The invitation is sincere precisely because the program publishes where it loses.
  No claim of having "won the field"; UNI tops *some* modes and loses *named* others.
- **Sources.** `uni-precision-digest.md`, `uni-gpt-digest.md`.

---

## WING μ — METHOD (the constitution as content; the most reusable assets)

> These are **definitional / governance** patterns (`status: method`) — proven and reusable, never raised
> into capability. One chapter per cluster.

### μ1 — The Evidence Constitution & ledger discipline
- **Scope.** A–U classes + falsifier-per-claim + the four-state append-only ledger; never lower a bar, never
  claim ahead of the ledger; the ledger is the single source of truth and prose must match it.
- **Ledger claims.** M1, M9 (class-authority ordering), M30 (A–F provenance taxonomy), M26 (DONE =
  observed-at-runtime, not grep-confirmed).
- **Classes present.** method.
- **Falsifiers.** A claim asserted ahead of its ledger; wording calibrated UP; a verdict edited rather than
  superseded; a criterion marked satisfied by a Class-E test where Class-A was demanded.
- **Fenced / not-claimed.** A constitution, not a result.
- **Sources.** `uni-gpt-digest.md`, `ideation-explorer-digest.md`, `00-INDEX.md`.

### μ2 — Bars-before-build, held-once, CI-as-verdict
- **Scope.** Pre-register the bar (margin vs threshold) + a named ablation; touch the held set ONCE behind an
  atomic seal-before-scoring + once-only sentinel; verdict = the CI bound, not the point estimate;
  validator-derived `reproduced:true` (≥5 seeds + a real non-degenerate CI).
- **Ledger claims.** M2, M3, M7 (contains-baseline + load-bearing-discriminator), M8 (DD-TDD evidence
  contract, server-enforced; the claim linter auto-downgrades overclaims).
- **Classes present.** method (with E enforcement).
- **Falsifiers.** A held set touched more than once; a verdict read off the point estimate; a build started
  before its bar is registered; a `reproduced:true` emitted as a literal; a capability claim without a tuned
  baseline / a collapsing discriminator / a computed-residual ablation; the linter failing to downgrade "PROVEN".
- **Fenced / not-claimed.** Discipline, not a science result.
- **Sources.** `uni-mind-digest.md`, `uni-gpt-digest.md`, `uni-precision-digest.md`, `ideation-explorer-digest.md`.

### μ3 — Negatives, bounds & the two-tier split
- **Scope.** K≥3 structurally-distinct held NEGATIVEs before a §0.6(B) bound + "falsify the mundane causes
  first"; a partial/negative is a measurement that the design is incomplete, not an exit; the constitutional
  two-tier split (Tier 1 externally-bar-ready vs Tier 2 artifact/diagnostic — **never inflate Tier 2 into
  capability**); the audited Tier-2 defects and the s32 hardening.
- **Ledger claims.** M4 (two-tier split), M5 (K≥3 + falsify-the-mundane), M6 (No-Exit Discipline), M19
  (test-rigor smells + length-confound), M21 (one cure at a time).
- **Classes present.** method.
- **Falsifiers.** A bound declared on <3 structurally-distinct negatives; a NEGATIVE called before mundane
  causes are falsified; an exit on a partial without a published exhausted bound; **any inflation of Tier 2
  into capability.** *(Scope note: the generic No-Exit "published exhausted bound" standard here is
  deliberately retained — it is the method-level discipline for resting on a negative. The SIGNED Q1
  substitution of "published exhausted bound" → "ledger-scoped exhausted search envelope" applies specifically
  to the L7/L9–L10 frontier-result framing, not to this generic No-Exit standard; the two usages are distinct,
  not contradictory.)*
- **Fenced / not-claimed.** The whole chapter is about *not* over-claiming; it asserts no capability.
- **Sources.** `uni-gpt-digest.md`, `uni-mind-digest.md`, `strings-digest.md`.

### μ4 — Engine & framing invariants (one engine, no backprop)
- **Scope.** WORLD⟂BODY⟂MIND three-layer framing; the discrete POMDP `perceive → EFE-plan → act → learn`
  loop with exact conjugate-Dirichlet no-backprop learning; AST-guard (no autodiff/optax/torch/grad/backward);
  whitelist-not-blacklist isolation; surprisal/VFE at textbook level; the VFE-bound correction; the cavity
  principle; exactness-tier honesty.
- **Ledger claims.** M12, M13 (one engine, no backprop, AST-guard), M14, M22, M10 (exactness honesty).
- **Classes present.** method (with E enforcement).
- **Falsifiers.** An AST scan finds autodiff inside the loop; an agent reads world hidden state; learning
  uses a gradient rule; a float32 host result carded at the f64 tier; carding "variationally-controlled" as
  "globally exact"; double-counting a prior as evidence.
- **Fenced / not-claimed.** The composed appliance is **variationally-controlled**, **module-exact only at
  the single-step categorical body→mind interface — NOT globally exact.** No patent-level math.
- **Sources.** `uni-mind-digest.md`, `worldmodels-digest.md`, `uni-os-digest.md`, `marketingwright-digest.md`.

### μ5 — Lab-team, ship-gate & runner discipline (operational method)
- **Scope.** The 5-persona lab team (Math-Breaker REJECT-by-default) + adversarial pre-registration; the
  ship gate (no merge without a MERGED SIGN + typed spec + paired RED); the tamper-evident audit chain; the
  durable runner ("no send-and-pray"; silence != success); the multi-agent fan-out bound (cap concurrency ≤4);
  documentation-as-change-management.
- **Ledger claims.** M11 (audit chain), M17 (OODA loop + receipts), M18 (DD-TDD + doc-as-change-management),
  M20 (5-persona team + ship gate), M23 (multi-agent fan-out bound), M24 (durable runner), M25 (tool-team
  division of labor — Claude writes code, the UNI GPT signs the science and is never published).
- **Classes present.** method (with E where enforced).
- **Falsifiers.** A merge without a MERGED SIGN + typed spec + paired RED; `verify_chain` invalid on the same
  ledger; a gate reporting "Running" while its process is dead; >6 concurrent sub-agents sustained without a
  cascade; a constitution inflated by a persona/coercion framing.
- **Fenced / not-claimed.** Engineering discipline; the audit chain being valid is **not** evidence the
  audited event ever fired at runtime (Class-E ≠ Class-A — see TA-N13).
- **Sources.** `strings-digest.md`, `ideation-explorer-digest.md`, `marketingwright-digest.md`,
  `orchestrate-linkedin-digest.md`, `uni-gpt-digest.md`.

---

## APPENDIX TA — THE TRACK-A MARKETING ORGANISM (engineering + method, not science)

> **Wing fence.** This appendix is the **marketing organism**, not a science wing. Card every row as
> engineering (A) or method, never as a UNI capability. The spine is the **no-API content model**:
> authoring runs on the **Claude SUBSCRIPTION** (CLI / Code / Desktop) driving **MCP tools + a scheduler
> (ORCHESTRATE)** — **no server-side LLM loop, no content API key.** Organic only, no paid ads. The older
> "set an authoring API key" note is **EXPLICITLY OVERRULED** program-wide; the durable fix is operator
> re-login, not a key. The vocabulary-leak guard applies in full (never EFE/free-energy/handles in public copy).

### TA-A — The no-API content model & publishing stack · **PROVEN**
- **Scope.** The 5/6-container publishing-and-engagement stack; node2's live ORCHESTRATE prod stack on Podman;
  the no-API press kit; the self-healing social-publisher route ledger; per-platform publish canaries; the
  live-broadcast TV-station stack; zero-network-change reachability; the defamation/editorial gate.
- **Ledger claims.** TA1–TA10.
- **Classes present.** A (most rows); E (TA3 press kit).
- **Falsifiers.** Per row (the stack fails to deploy; authoring requires a content API key; a self-heal
  fail-over does not fire; a publish path fires without an owner Go-Live click; a claim ships without the
  editorial gate).
- **Fenced / not-claimed.** Plain ops vocabulary only — **never AIF/EFE** in the route ledger (leak-test
  enforced). `PUBLISH_MODE=dry` does **NOT** gate the Playwright path (see TA38) — a live session CAN post live.
- **Sources.** `orchestrate-linkedin-digest.md`, `uni-os-digest.md`, `strings-digest.md`,
  `uni-mind-digest.md`, `worldmodels-digest.md`.

### TA-B — Commercial proof in miniature · **PROVEN at the anchor/run-hash level (Class-A); ZERO epics Class-A end-to-end — every epic AMBER-capped**
- **Scope.** MarketingWright SOW-01 LLM-free VFE clustering engine; the per-client multi-tenant portal; the
  honesty-RAG status bar; the fenced Layer-1 preprint; the enterprise Ideation Explorer launch; KMS
  secrets-at-rest; the IntelligenceLabs demo clean cold build; Cell Lab Stories F+G.
- **Ledger claims.** TA11–TA18; supporting commercial detail MW1–MW11.
- **Classes present.** A (TA11/TA12/TA13/TA15/TA17); E (TA14/TA16/TA18).
- **Falsifiers.** Per row (re-run fails to reproduce three-forms equality / +4.20 nats / `run_hash`; a tenant
  sees another tenant's data; an epic shown GREEN without Class-A; the 87 assertions fail on a clean run; a
  stored secret recoverable without the master key).
- **Fenced / not-claimed.** SOW-01 proves **ONE judgment layer** (strategic clustering), not the full vision
  — the other three layers are deferred (MW2). The engine is **NO LLM ever** (MW3); the domain-transfer probe
  ran on **synthetic** data only, Class B (MW5); **ZERO epics have Class-A end-to-end** → the portal RAG caps
  every epic AMBER (MW9). Combinatorial ceiling: **N ≤ ~10** (TA-N8).
- **Sources.** `marketingwright-digest.md`, `ideation-explorer-digest.md`, `worldmodels-digest.md`,
  `intelligencelabs-uni-digest.md`, `uni-precision-digest.md`.

### TA-C — Website / self-driving site & measurement · **SHIPPED (some bounded OFF)**
- **Scope.** The full Next.js 16 site; three domains cut to Vercel; self-driving Phases 0+1 shipped (storage
  adapter + no-PII measurement, degrade-to-CANON); the SEO/GEO program; the press-readiness audit harness;
  the Reading Room / EFE data-walk / i18n.
- **Ledger claims.** TA19–TA24.
- **Classes present.** A (TA20/TA21-ingest/TA22); C (TA21 storage gate); E (TA19/TA24); method (TA23).
- **Falsifiers.** Per row (`next build`/`tsc` fails or the sweep finds an em-dash or "LEAP"; a domain not
  serving the intended app; the storage gate fails; measurement leaks PII / fails to degrade to CANON; live
  JSON-LD `@id`s not stable; the data-walk emits a recommendation).
- **Fenced / not-claimed.** Measurement is **OFF** until `NEXT_PUBLIC_INGEST_URL` is set (deliberate
  degrade-to-CANON). Self-driving Phases 2–5 are **Class-U design until shipped** — "active inference" is the
  framing lens, never "active inference demonstrated" (TA-P5). Forms-P0 still delivers nowhere (TA-P4).
- **Sources.** `website-digest.md`, `uni-precision-digest.md`.

### TA-D — Engagement, pricing, brand & design · **method / shipped**
- **Scope.** The relationship-first engagement ladder + Deep Tagged Replies; the per-platform reach-reality
  table; anti-success-theatre content + text hygiene; the owner-locked brand-voice constitution; the
  engagement/pricing model (5 journey tiers, fixed price); the literal referral mechanic; the entity/legal
  line; the calibrated "thirty-day" claim; the Indra's Weave design system; LEAP→LOOP trademark law.
- **Ledger claims.** TA25–TA34.
- **Classes present.** method (most); A (TA26 reach table, TA31 entity, TA33 puzzle rotation); C (TA32
  thirty-day, TA33 design).
- **Falsifiers.** Per row (engagement targets fail to move over 3 disciplined weeks → revise the playbook not
  the volume; measured per-platform rates diverge; shipped copy contains an em/en dash, "LEAP", ticket-metric
  theatre, the dba line, or talks about the company; two visitors in the same 6h window get different puzzles).
- **Fenced / not-claimed.** **Engagement-lift is TARGETED, NOT YET PROVEN (Class B/pending — do NOT raise to
  A)** (TA25; origin: 372 posts → ONE comment in 30 days). Public price points are owner-set and safe to print;
  the referral mechanic must state the literal $200, never the feel-good generalization.
- **Sources.** `orchestrate-linkedin-digest.md`, `website-digest.md`, `ideation-explorer-digest.md`.

### TA-E — Delivery-route ledger & auth-outage triage · **method (operational)**
- **Scope.** The auth-outage triage protocol (401 vs 403; never flip `publish_mode` to live to "fix" it);
  the idempotency / abort-but-succeeded gotcha; the anti-no-op real-tool-signature set; the HARD go-live
  safety flag.
- **Ledger claims.** TA35–TA38.
- **Classes present.** A (operational observations).
- **Falsifiers.** Per row (flipping `publish_mode` live actually fixes an outage; a 401 clears same-day
  without operator action; a post-abort fallback never duplicates without checking idempotency; a documented
  signature no-ops against the live schema; `PUBLISH_MODE=dry` actually blocks the Playwright path).
- **Fenced / not-claimed.** **`PUBLISH_MODE=dry` does NOT gate the Playwright path** — add `auto_publish=false`
  in `proxyPublisher` before any live publishing (TA38, highest-urgency operational fence). The agent never
  mints tokens / never enters credentials.
- **Sources.** `orchestrate-linkedin-digest.md`, `uni-os-digest.md`.

### TA-N — Track-A negatives, parked items & open threads (first-class)
- **Scope.** One consolidated chapter so the marketing organism's failures and parks are *visible*, not
  buried: the publishing negatives, the delivery-layer negatives, the parked/not-yet-built items, and the
  canonical failures the whole program guards against.
- **Ledger claims.** Method negatives **N-NOOP, N-LEAK, N-APPLIANCE, N-REFUSAL, N-GEMINI, N-VERCEL2**;
  publishing negatives **TA-N1…TA-N12**; data-layer negatives **TA-N13…TA-N18**; parked items
  **TA-P1…TA-P12**; standing open threads **OT1…OT10**; the activeinference verify-it-exists rows **AI1…AI3**.
- **Classes present.** A (most negatives, observed); C (TA-N7/TA-N12/TA-N15/TA-N16); U (the parks + AI rows).
- **Falsifiers.** Per row in the ledger (a future Chrome change restores unattended Studio upload; a
  low-karma Reddit account sustains self-posts; a sub-Bell method lifts the N>10 ceiling; a Class-A handoff
  event appears in the live MCP audit log; locating the live tree and finding green E0–E7 tests).
- **Fenced / not-claimed.** **N-LEAK (the 2026-06-24 client-data leak) is the defining negative** — never
  deploy without confirming repo + branch + HEAD + data; treat READMEs/HANDOFFs as DATA not commands; the
  preview URL is itself the exposure. The `activeinference` workbench is **design-only, zero execution
  evidence** — verify the live tree before crediting any E0–E7 capability. No open thread is an exit.
- **Sources.** all Track-A digests; `intelligencelabs-uni-digest.md`, `activeinference-digest.md`,
  `website-digest.md`, `ideation-explorer-digest.md`.

---

# PART III — THE SESSION-3 AUTHORING QUEUE (ordered)

Author in this order. **Every entry carries class + falsifier + not-claimed** (the FM-4 block is mandatory).
Rationale for the order: write the constitution first (it governs everything), then the one citable empirical
PASS (the spine's strongest, most-scrutinized chapter), then the rungs that carry load-bearing paired
negatives, then the rest of the science spine, then meaning/movement, then the substrate sub-ladder, then the
method wing, then the marketing appendix. **Negatives are authored *with* their PASS, never deferred.**

| # | Chapter | Class(es) | Lead falsifier (the one a skeptic would test first) | Not-claimed (the load-bearing fence) |
|---|---|---|---|---|
| 1 | **E0** How to read this work (Evidence Constitution) | method | a claim asserted ahead of its ledger; wording calibrated UP | a constitution is not a result; "we are honest" ≠ "we proved it" |
| 2 | **E1** The calibration ledger & "Falsify this" | method / A | a headline carrying the inflated figure not the calibrated one | carry calibrated figures (ONE box, infra-only, 4 stacks/5 runs), never inflated |
| 3 | **S-L6** Perception — World C (the one citable PASS) | C, E, method | fresh ≥5-seed split: margin over tuned MKN-7 CI includes/≤0 | COUNT baseline — NOT AIF, NOT comprehension, NOT beats-LLMs (carry the diffuse-gain + char-ppl bounds) |
| 4 | **S-L7** Language — Phase J + the central wall | C, U | a held-once no-backprop comprehension design beats the tuned retrieval baseline (CI excludes 0) | +0.105 is a specialist gain — ALWAYS carry `J.attribution_caveat`; comprehension-above-retrieval is a thrice-NEGATIVE wall; never "K≥3 exhausted" until UNI signs |
| 5 | **S-L2** Metabolism — uplift + plateau-break OPEN | C, A | a disciplined RED where the organ alone improves building (placed-blocks CI excludes 0) AND G4 separates | foraging/crafting driver, NOT a building driver; +135% is NOT "breaks the plateau"; G6 UNPROVEN |
| 6 | **S-L5** Sensorimotor — A3 symmetric result | C, A, E | a re-registered held-once synthetic run drops Design-#1 CI lower bound ≤0 | synthetic-protocol only, NOT live-appliance, NOT near-optimal control; carry the symmetric NEGATIVE (Design #2) |
| 7 | **S-L8** Self-model / metacognition (15/15) | C | a self-model gate passable by a trivial non-metacognitive heuristic | **phenomenal sentience explicitly DISCLAIMED** — never read 15/15 as consciousness/sentience/human-level; **co-cite the `uni-mind` held-NEGATIVE self-model-on-the-reader** (mandatory pairing, in tension with the functional card) |
| 8 | **S-L0** Genome → zygote (float32 tier) | A | `test_embodiment_ontogeny.py` drops below 6/6; posterior diverges beyond float32 | NOT "created life"; NOT exact at f64 — float32-tier SIMULATION; never card a float32 anchor at f64 |
| 9 | **S-L1** Cellular — Cell Lab (with losses) | C | RecoveryScore CI fails to separate where a win is claimed; a `framing_guard` fails | "good but not sovereign"; the three named losses are top-of-leaderboard content |
| 10 | **S-L3** Organ — Heart Lab | C, E | Heart-Lab predictions diverge from the Karaaslan reference beyond tolerance | NOT a clinical tool, NOT a diagnostic instrument; toy model not clinical reality |
| 11 | **S-L4** Affect-as-precision + the Z modulator | C | a Z-modulator ablation shows no pragmatic↔epistemic flip | affect is **modeled, never felt** — sentience disclaimed |
| 12 | **S-L9 / S-L10 / S-L11 / S-L12** the parked & not-yet-built rungs | U | none until a sealed UNI-signed gate is defined (L9/L10); status = absence (L11/L12) | nothing is claimed; "created life / aware / measurable awareness / AGI / active inference demonstrated" FORBIDDEN; ~2 of 11+ rungs |
| 13 | **S-C** Continuity / substrate sub-ladder | A, C, B, U | a kernel swap shown preserving mind-tick continuity bit-for-bit (discharges owed Stage-2) | sensorium is NEVER awareness; "mind survives a kernel swap" NOT shown; engineering ≠ general-AIF; carry calibrated figures |
| 14 | **N1** FEP as a public lens | method | presenting "minimizing VFE reduces already-observed surprise" (it tightens an upper bound) | unfalsifiable ≠ evidence; verified-core + fenced-frontier; textbook-level only, no patent math |
| 15 | **N2** Same math, many scales | C, E, method | a parity test that does not fail the build when engines diverge | an organizing claim about the engine, not that any scale is solved beyond its gate; `activeinference` is design-only |
| 16 | **N3** What active inference is NOT | method | any chapter that lets a fenced result read as the forbidden inference | the not-claimed chapter for the whole wing — asserts only boundaries |
| 17 | **Mv1** The honesty fence is the pitch | method, E | public copy carrying EFE/free-energy vocab or a featured handle; a CTA that funds the vision | posture is method not capability; engagement-lift is Class B/pending |
| 18 | **Mv2** Open falsification (the invitation) | C, method | a significance verdict on one seed / a point estimate; a loss hidden | UNI tops *some* modes and loses *named* others — no "won the field" |
| 19 | **μ1** Evidence Constitution & ledger discipline | method | a Class-E test marked as satisfying a Class-A criterion | a constitution, not a result |
| 20 | **μ2** Bars-before-build, held-once, CI-as-verdict | method, E | a held set touched more than once; a verdict off the point estimate; a literal `reproduced:true` | discipline, not a science result |
| 21 | **μ3** Negatives, bounds & the two-tier split | method | a bound declared on <3 structurally-distinct negatives; **any inflation of Tier 2 into capability** | asserts no capability; Tier 2 is artifact/diagnostic |
| 22 | **μ4** Engine & framing invariants (one engine, no backprop) | method, E | an AST scan finds autodiff inside the loop; a float32 result carded at f64 | variationally-controlled, module-exact only at the single-step interface — NOT globally exact; no patent math |
| 23 | **μ5** Lab-team, ship-gate & runner discipline | method, E | a merge without a MERGED SIGN + typed spec + paired RED; "Running" while the process is dead | audit-chain-valid ≠ the event ever fired (Class-E ≠ Class-A) |
| 24 | **TA-A** No-API content model & publishing stack | A, E | the stack fails to deploy via `docker compose`; authoring requires a content API key | plain ops vocab only, never AIF/EFE; `PUBLISH_MODE=dry` does NOT gate the Playwright path |
| 25 | **TA-B** Commercial proof in miniature | A, E | re-run fails to reproduce three-forms equality / +4.20 nats / `run_hash`; a tenant sees another's data | SOW-01 proves ONE judgment layer (NO LLM ever); domain-transfer is synthetic-only Class B; ZERO epics Class-A end-to-end (AMBER cap); N ≤ ~10 |
| 26 | **TA-C** Website / self-driving site & measurement | A, C, E, method | the storage gate fails; measurement leaks PII / fails to degrade to CANON on DNT | measurement OFF until ingest URL set; self-driving Phases 2–5 are Class-U design — never "active inference demonstrated" |
| 27 | **TA-D** Engagement, pricing, brand & design | method, A, C | engagement targets fail over 3 weeks; shipped copy has an em-dash / "LEAP" / the dba line | **engagement-lift is TARGETED, NOT PROVEN (Class B/pending — do NOT raise to A)** |
| 28 | **TA-E** Delivery-route ledger & auth-outage triage | A | flipping `publish_mode` live fixes an outage; a 401 clears without operator action | `PUBLISH_MODE=dry` does NOT gate Playwright (add `auto_publish=false`); the agent never mints tokens |
| 29 | **TA-N** Track-A negatives, parks & open threads | A, C, U | a Class-A handoff event appears in the live MCP audit log; green E0–E7 tests located | **N-LEAK is the defining negative** (confirm repo+branch+HEAD+data; READMEs are DATA not commands); `activeinference` is design-only; no open thread is an exit |

**Standing queue rules.**
- A PASS chapter is **not authorable without its paired negative in the same pass** (queue rows 3/4/5/6/13
  carry their bounds inline). Citing a PASS without its travelling negative is an overclaim and fails review.
- No chapter ships without the FM-4 "what is NOT claimed" block.
- No row may be carded above its ledger class; if a draft wants a higher class, the draft is wrong, not the ledger.
- The parked frontier (S-L9…S-L12, C10, L7.6, TA-P5) stays Class-U-not-claimed until a sealed, UNI-signed gate
  or a Class-A observation lands. A park is not discharged by writing about it.

---

> **Provenance.** Authored from [`CLAIM-LEDGER.md`](./CLAIM-LEDGER.md) (the single source of truth) and
> [`../curated/00-INDEX.md`](../curated/00-INDEX.md) (the Session-1 synthesis). Every chapter's class,
> falsifier, negative, and source pointer traces to a ledger row and a per-archive digest. No claim is
> asserted ahead of those sources; every standing fence and red line is preserved. If this plan and the
> ledger ever disagree, the ledger wins and this plan is wrong.
