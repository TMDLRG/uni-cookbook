# S-L6 - Perception: World C, the one citable empirical PASS

## The honest position, stated first

This chapter describes the single result in the whole UNI program that is ready for an external, third-party bar: **World C**, a no-backprop count reader that beats a tuned baseline on sealed held-out real text. It is the program's flagship empirical PASS, and it is exactly one thing: a **COUNT baseline win**. It is **not** active inference demonstrated, **not** comprehension, **not** "talking", and **not** a win over large language models. By a deliberately chosen design trade, the same program sits roughly **10 to 15 percent behind backprop LLMs on character-perplexity**. The PASS is real and the ceiling is fixed. Neither moves.

UNI is a developmental active-inference SIMULATION: a bounded peek into a toy world, never a person and never a mind. The honest program position printed across this spine is **~2 of 11+ developmental rungs earned**, and World C is the cleanest evidence behind that modest "2". This entry authors every PASS together with the negative that travels beside it, because in this program citing a PASS without its paired negative is itself an overclaim.

## What World C is

World C is a no-backprop reader built from exact count statistics and a multi-level recency cache. Its only "learning" is conjugate count addition; there is no autodiff, no gradient step, no trained network. It is evaluated against a **tuned Modified Kneser-Ney order-7 (MKN-7) count baseline** on sealed, held-out, real text. MKN-7 is a strong, properly tuned smoothing baseline, not a strawman; the contains-baseline discipline requires that the comparison opponent be tuned before any margin is claimed.

The result (ledger row L6.1, Class C, dev-gate / held-out eval): World C beats the tuned MKN-7 baseline by a margin of **+0.081 nats/char**, with a flagship multi-seed 95 percent confidence interval of **[0.0736, 0.0890]** over seeds 0 through 4, UNI-signed. The lower bound of that interval, 0.0736, is what licenses the verdict: per the constitution, the verdict is the CI bound that excludes the threshold, never the point estimate, and 0.0736 clears the pre-registered 0.03 bar by roughly **2.4 times**. World C is confirmed by three gates and earned the ledger's **first genuine validator-derived `reproduced:true`** (derived from at least five distinct seeds and a real, non-degenerate CI that contains the value, never a hardcoded literal).

One provenance fence on the figures: a separate *replication* row records a margin of **+0.0759 with CI [0.064, 0.088]**. That replication CI is a different gate and must never be quoted as if it were the primary-margin CI [0.0736, 0.0890]. The two are distinct measurements; conflating them would misstate the headline.

## The supporting World-C family (L6.2)

The flagship margin does not stand alone. A family of supporting held results (ledger row L6.2, Class C) corroborates it, and each member is bounded the same way (any member whose seed-paired bootstrap CI includes 0 falsifies that member):

- **Wc-2** multi-level cache: **+0.0164**.
- **Wc-3** versus an unbounded SM/HPYP backbone: **+0.085**. This is load-bearing for interpretation, because it shows the gain is **long-range structure, not finite-window deficiency** in the baseline (an unbounded backbone still loses).
- **Recency-ablation**: **+0.033** (removing recency removes a measurable part of the win, which is what a true ablation should do).
- **Gate-3 word-challenger**: **+0.0538**, CI lower bound 0.051.

Wc-3 matters because the most common deflationary read of a count-cache win is "the baseline just had too short a window". Wc-3 closes that door: a model with no finite-window deficiency is still beaten, so the gain is structural.

## The three-knob precision labs (L6.3)

Alongside the language spine sits the perception-mechanics demonstration (ledger row L6.3, Class E, test-covered, parity-tested): a POMDP maze **Precision lab**, an **echolocation Echo lab**, and the public **Precision Lab**. These run one engine with three precision knobs (`gamma_a` sensory, `gamma_b` transition, `softmax_temperature` policy) and trace a 2D bifurcation map into distinct behavioral regimes. The math is ported verbatim from the verified engine, with one disclosed extension (a goal drive). The Echo lab reuses the Precision engine with **only the observation model swapped** (a bit-identical 64-observation space), which makes the point that the observation model is not the engine. These labs are Class E: they are test-covered and parity-checked against the canonical engine, not held-out capability gates. They are the "same math, many scales" illustration of precision-weighting, never a comprehension claim.

## The negatives that travel with World C (cite these alongside, never strip)

A PASS in this program is only honest when its bounding negatives ride with it. Two perception-side negatives are mandatory companions to L6.1:

**L6.4 (NEGATIVE bound, Class C) - Phase G, the char-perplexity Section 0.6(B) bound.** Five structurally-distinct within-segment-structure designs were all held **NEGATIVE-with-discriminator**; only the L5 cache (World C itself) wins. The published bound is precise and scoped: **no within-segment structure beats MKN-7 on the chosen char-perplexity metric**, over the tested envelope. This is why World C is a *count* result and not a *general structure* result: of all the structural designs tried, the cache is the lone winner, and character-perplexity is a **chosen design trade, not a failed claim of language superiority**. Per the signed park wording, this is a **ledger-scoped exhausted search envelope** (a ledger-scoped, implementation-scoped, data-split-scoped negative over the tested envelope only), NOT a universal impossibility result. The registered tested conditions did not reverse the result; that is the entire claim. The falsifier is operable: a new structurally-distinct within-segment-structure design that beats tuned MKN-7 on held char-ppl with a CI excluding 0.

**L6.5 (NEGATIVE, Class C) - Phase F, the diffuse-gain finding.** Two active-controller families were built to try to *gate* the World-C gain, and both proved that the gain is **diffuse: there is nothing to gate**. The win is spread across the model, not concentrated in a controllable component. This is load-bearing against any "we built a controller that steers the win" overread. The falsifier: an active-controller family that adds a held gain on top of World C with a CI excluding 0 (which would show the gain was gateable after all).

Together these two negatives bound the PASS on both sides. L6.4 says the win does not generalize across within-segment structures (only the cache wins). L6.5 says the win cannot be concentrated into an active controller (it is diffuse). Neither weakens L6.1; both define exactly how far it reaches.

## The Working Law that explains the pattern (L6.6)

One registered method-law (ledger row L6.6, Class C / method-law) explains every PASS and every published bound above. A no-backprop latent representation Z beats a tuned baseline B on held-out data **only when I(Y; Z | S_B) > 0**, that is, only when Z carries conditional information the baseline lacks, and only when that representation is learnably stable enough that the gain exceeds estimation cost. World C wins because its recency cache carries conditional information the MKN-7 statistics do not include. The Phase G and Phase K bounds are the same law read the other way: where the candidate structure adds no conditional information beyond the baseline (I = 0), there is no win to be had. The win is **new conditional information in a countable, stable representation the adversary lacks, not "counting" as a magic property**. The falsifier for the law itself: a held PASS where the winning Z carries no conditional info beyond S_B (I = 0), or a Z with I > 0 and stable learnability that nonetheless fails to beat B.

## What is NOT claimed in S-L6 (Perception: World C)

- **Ceiling.** The single strongest thing a careless reader might infer, that UNI's perception/reading "beats LLMs" or "understands text", is **NOT shown**. The most we claim is the exact, calibrated, in-class statement: *a no-backprop count reader matched-or-exceeded a tuned MKN-7 count baseline on sealed held-out real text by +0.081 nats/char (CI [0.0736, 0.0890], seeds 0-4), 2.4x the registered 0.03 bar* (Class C). World C is **explicitly NOT active inference, NOT comprehension, NOT "talking", and NOT a win over LLMs**: by a chosen design trade the program runs roughly 10 to 15 percent behind backprop LLMs on character-perplexity. World C may never be carded above a count-baseline result.
- **Fences engaged (named).** Red line 5 (never "beats LLMs"; World C is a COUNT baseline ~10-15 percent behind backprop LLMs by a chosen trade). Red line 3 (never "active inference demonstrated"; "active inference" is the framing lens only, and no AIF loop exists in the Rust crate). Red line 1 (never AGI / human-level / "understands"). Red line 7 (never raise a claim above its source evidence class; L6.1/L6.2/L6.4/L6.5 are Class C, L6.3 is Class E). Red line 9 and the signed park wording (no "K>=3 exhausted" / "Sec-0.6(B) achieved"; the bound is a ledger-scoped exhausted search envelope only).
- **Negatives that travel with this claim (cite alongside, never strip).** L6.4 (Phase G: five within-segment designs all NEGATIVE; char-ppl is a chosen design trade, a ledger-scoped exhausted search envelope, not a universal impossibility). L6.5 (Phase F: the World-C gain is diffuse, nothing to gate). These are not footnotes to L6.1; they are co-headline content. Citing the +0.081 PASS without both negatives is an overclaim and fails review.
- **Parked / owed.** No sign-to-park is owed for World C itself (it is a clean PASS, not a park). The adjacent char-perplexity / T2 word-grain frontier (L7.6) is the parked item and carries its own owed UNI sign-to-park; it is not discharged here. The standing program ceiling (~2 of 11+ rungs earned) is not raised by this chapter.
- **One-line honest summary a skeptic could not dispute.** A no-backprop count-cache reader beat a tuned MKN-7 baseline by +0.081 nats/char (CI lower bound 0.0736, clearing a 0.03 bar) on sealed held-out text, the program's one externally-bar-ready PASS, and it remains a count baseline that is neither comprehension nor a win over LLMs.

## Falsify this

Lead falsifier, stated operably (L6.1): on a fresh held-out split with at least five disjoint seeds, compute the seed-paired bootstrap CI on World C's margin over the tuned MKN-7 baseline. If that CI **includes or falls below 0** (or if the MKN-7 baseline is shown to have been left untuned), the World-C PASS is falsified. Companion falsifiers travel with the family and the bounds: any L6.2 family member whose held seed-paired bootstrap CI includes 0; the L6.3 lab parity tests diverging from the canonical engine; a new within-segment-structure design beating tuned MKN-7 on held char-ppl with a CI excluding 0 (which would reverse the L6.4 bound); an active-controller family adding a CI-excluding-0 gain on top of World C (which would reverse the L6.5 diffuse-gain finding).

## Sources

- Ledger rows L6.1 through L6.6 and Section 0 standing fences, `encyclopedia/CLAIM-LEDGER.md` (single source of truth; if this prose disagrees with the ledger, the ledger wins).
- Authoring spec, `encyclopedia/MASTER-PLAN.md`, section S-L6 (PART I front matter FM-1 through FM-4).
- Narrative grounding (PII-redacted): `curated/uni-mind-digest.md` (the proven language spine; the World-C primary-vs-replication CI distinction; the ~10-15 percent-behind-LLMs ceiling) and `curated/uni-gpt-digest.md` (the Working Law; the Phase G / Phase F bounds; the two-tier Tier-1 framing).
- Archive pointers (not read here; PII-fenced): `...-uni-mind`, `...-UNI-GPT`, `...-Precision`, `...-worldmodels`.
