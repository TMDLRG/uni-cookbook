# CN-05 — DNA: the information substrate

> **What you are reading.** The molecule treated as what it is: a physical polymer with measured dimensions and mechanics, carrying a measurable quantity of information at a measured error rate, packed by a measured hierarchy, copied at measured speed. Geometry first, information second, and the deflation immediately after — because the single most expensive mistake available here is to read DNA as source code. Every number below carries a source you can find or is written NOT-MEASURED. Nothing here raises any UNI rung.

---

## Geometry first

The B-form double helix, at the resolution a designer actually needs:

- **Rise: ~3.4 Å per base pair** (0.34 nm). This is the number that converts sequence length into physical length, and it is the most load-bearing constant in the chapter.
- **Diameter: ~20 Å** (2 nm).
- **Base pairs per turn: this is where the textbook is wrong, instructively.**

Watson & Crick (1953), *Nature* 171:737–738, proposed the structure with **10 bp/turn** — a value read off X-ray fibre diffraction of oriented, semi-crystalline DNA (Wilkins, Stokes & Wilson, *Nature* 171:738, and Franklin & Gosling's Photo 51 appear in the same 25 April 1953 issue; *exact Franklin & Gosling pagination NOT-CONFIRMED in this pass*). Fibres are not solution.

Wang (1979), *PNAS* 76(1):200–203, doi:10.1073/pnas.76.1.200, measured it properly in solution: run pairs of covalently closed circular DNAs differing by 1–58 bp out of ~4,350 bp on a gel and read the topoisomer ladder. Result: **10.4 ± 0.1 bp/turn**, which Wang states is "significantly different from the value 10.0 base pairs per turn for the B form fiber structure."

Rhodes & Klug (1980), *Nature* 286(5773):573–578, PMID 7402337, "Helical periodicity of DNA determined by enzyme digestion," bound short stiff DNA to flat surfaces, digested with DNase I and read the cutting periodicity: **10.6 ± 0.1 bases**.

**These two do not resolve into a tidy story, and the tidy story is the trap.** Rhodes & Klug do *not* report 10.6 as a surface-bound value. Their abstract's final sentence, verbatim: "We identify this value with the number of base pairs per turn of the DNA double helix **in solution**." So Wang's 10.4 and Rhodes & Klug's 10.6 are two claims about the **same quantity under the same nominal condition**, reached by two different assays — a topoisomer ladder against a DNase I cutting periodicity. That is a **method-dependent discrepancy, and this pass does not reconcile it.** Both are primary. They disagree.

The ubiquitously quoted "**~10.5**" sits between them. It is not nowhere: Potaman & Sinden's Table 1 — this chapter's source for the rest of the geometry — *prints* 10.5 as B-DNA's residues per helical turn. But **why** the field settled on 10.5 (an independent determination? a rounding? a midpoint?) is **NOT-SOURCED in this pass**. Quote 10.5 if you like; know that it is neither Wang's number nor Rhodes & Klug's, and that the two primaries it sits between have not been reconciled here.

**Grooves — and a convention trap this chapter fell into.** Two pairs circulate for B-DNA's major/minor groove widths: **~12 Å / ~6 Å**, and the widely repeated textbook pair **22 Å / 12 Å**. **Both are NOT-SOURCED in this pass.**

An earlier draft of this chapter attributed the 12/6 pair to Potaman & Sinden, "DNA: Alternative Conformations and Biology," *Madame Curie Bioscience Database* (Landes Bioscience, NCBI Bookshelf NBK6545). **That citation was fabricated.** NBK6545's Table 1 carries no groove-width row at all — its rows are direction of helix rotation, residues per helical turn, axial rise, pitch, base-pair tilt, rotation per residue, diameter, glycosidic bond, and sugar pucker — and its prose describes the grooves only qualitatively, as a cylinder of 20 Å diameter bearing a major and a minor groove. The 12/6 values are standard in the literature and may well be right; **the receipt was not.** *Recorded below, not quietly deleted.*

The conventions are the reason two pairs exist at all: groove width is reported either as a **phosphate–phosphate distance** or with the **van der Waals radii of the phosphates subtracted**. But watch what that does *not* buy. The offset usually quoted is ~5.8 Å, and it accounts for the minor pair (12 − 5.8 = 6.2 ≈ 6) while **failing on the major pair**: 22 − 5.8 = **16.2, not 12**. The two printed pairs differ by **10 Å** in the major groove. So "different convention" is **not** a sufficient explanation, the ~5.8 Å offset is itself **NOT-SOURCED here**, and the provenance of the textbook 22 Å remains **genuinely unexplained**. **A groove width quoted without its convention is underspecified** — and this chapter did not have a sourced one. Do not average them; name the convention or do not print the number. *The chapter now obeys its own rule here rather than lecturing it.*

**The three families** (same source unless noted):

| | A-DNA | B-DNA | Z-DNA |
|---|---|---|---|
| Sense | right | right | **left** |
| bp/turn | 11 | **10.5** *(this source)*; cf. 10.4 soln (Wang) / 10.6 soln (Rhodes & Klug) / 10 fibre | 12 |
| Rise | 2.55 Å | 3.4 Å | 3.7 Å |
| Diameter | 23 Å (9 Å axial hole) | 20 Å | 18 Å |
| Sugar pucker | C3′-endo | C2′-endo | alternating |

Z-DNA is not a curiosity invented to fill a table — it was solved crystallographically at atomic resolution: Wang et al. (1979), *Nature* 282:680, "Molecular structure of a left-handed double helical DNA fragment at atomic resolution." The molecule has **more than one stable conformation**, and which one it occupies depends on sequence and environment. A design that treats DNA as one fixed geometry has already lost information.

## It is a polymer, so it has mechanics

The number that turns DNA from a diagram into an object: **persistence length ℓ_p ≈ 50 nm ≈ 150 bp** in ~0.1 M aqueous NaCl **at ~20–25 °C**, a consensus value reproduced by magnetic tweezers, optical tweezers, and AFM (see the review by Peters & Maher, "DNA curvature and flexibility in vitro and in vivo," *Q Rev Biophys* 43(1):23–63, PMID 20478077).

**The temperature belongs in that scope, and this chapter previously omitted it.** Geggier, Kotlyar & Vologodskii (2011), *NAR* 39(4):1419–1426, doi:10.1093/nar/gkq932, PMID 20952402, "Temperature dependence of DNA persistence length," measured ℓ_p *falling* as it warms: **53.2 nm at 5 °C → 42.5 nm at 42 °C**. Their conclusion, verbatim: DNA persistence length "strongly depends on temperature and accounting for this dependence is important in quantitative comparison between experimental results obtained at different temperatures." Two consequences, and both cut against citing this paper as support for the 50 nm figure. First, they worked in **TBE with 10 mM MgCl₂ — not ~0.1 M NaCl** — so it is a *different ionic condition*, a **condition on** the consensus rather than a replication of it. Second, their values at and above body temperature sit **at or below the 45–55 nm band this chapter prints as its own falsifier**. By the chapter's own rule that a rate without a temperature is underspecified, a persistence length without one is too.

Read it as an engineer. Below ~150 bp, DNA is effectively a **stiff rod** — you cannot bend it appreciably with thermal energy. Above it, DNA is a **flexible coil** and behaves like a worm-like chain. This single constant explains why a nucleosome is a *problem*: wrapping 147 bp around a histone octamer means bending DNA through ~1.65 superhelical turns *at* its persistence length, which is not free. Something has to pay, and the histones pay it with binding energy.

Fence the constant honestly: sub-100 bp DNA is **more bendable than the worm-like chain predicts** — Vafabakhsh & Ha, *Science* (PMC3565842), report extreme bendability by single-molecule cyclisation. The 50 nm value is a large-scale property, not a licence to extrapolate to short loops.

## The information content, then the deflation

Four bases, equiprobable: `log₂(4) = 2 bits/bp`. That is the ceiling, and it assumes no correlations — real genomes have plenty, so 2 bits/bp is an **upper bound**, not a content measurement.

Use the honest genome size. Not GRCh38 ("~3.1 Gbp" with gaps), but **T2T-CHM13**: Nurk et al. (2022), *Science* 376:44–53, doi:10.1126/science.abj6987 — **3,054,815,472 bp** of gapless nuclear DNA (chromosomes 1–22 and X) plus a 16,569 bp mitochondrial genome. Now compute:

```
Haploid : 3.055e9 bp x 2 bits = 6.11e9 bits = 764 MB  (728 MiB)
Diploid : ~6.11e9 bp x 2 bits = 1.22e10 bits = 1.53 GB (1.42 GiB)
```

**A human genome fits on a DVD.** Hold that number, then deflate it immediately, because it is not a design specification.

Coding DNA is **1–2% of the genome** (Piovesan et al. 2019, *BMC Res Notes*, "Human protein-coding genes and gene feature statistics in 2019," doi:10.1186/s13104-019-4343-8; the exome is ~1.5%). ~20,000 protein-coding genes. Whatever the other 98% is doing, it is not spelling out a body plan.

And then the **C-value paradox** finishes the job. Genome size does not track organismal complexity — not weakly, not noisily, *not at all* (conversion throughout: 1 pg = 0.978 Gbp, Doležel et al. 2003, *Cytometry A*, doi:10.1002/cyto.a.10013):

| Organism | Genome (1C) | vs human |
|---|---|---|
| Human (T2T-CHM13) | 3.055 Gbp | 1× |
| Onion, *Allium cepa* | 16.75 pg ≈ **16.4 Gbp**; ≥95% repetitive | **5.4×** |
| South American lungfish, *Lepidosiren paradoxa* | **91 Gbp**, ~90% repeat content — largest animal genome **sequenced** | **~30×** |
| *Paris japonica* | 152.23 pg ≈ **149 Gbp** | ~49× |
| Fork fern, *Tmesipteris oblanceolata* | **160.45 Gbp** — current eukaryotic record | **52×** |

Sources: Fernández et al. (2024), *iScience*, "A 160 Gbp fork fern genome shatters size record for eukaryotes," doi:10.1016/j.isci.2024.109889; Schartl et al. (2024), *Nature* 634:96–103, doi:10.1038/s41586-024-07830-1 (lungfish); Pellicer, Fay & Leitch (2010), *Bot J Linn Soc* 164(1):10, doi:10.1111/j.1095-8339.2010.01072.x (*Paris japonica*).

**A fern carries 52× your information budget.** If genome size measured design content, that fact would be a catastrophe. It is not a catastrophe; it is a refutation of the premise.

## The error budget, in layers — the chapter's best engineering lesson

Routinely conflated, so do it carefully. The famous ~10⁻¹⁰ is **not the polymerase's error rate.** It is what comes out of a stack.

Schaaper (1993), *J Biol Chem* 268(32):23762–23765, "Base selection, proofreading, and mismatch repair during DNA replication in *Escherichia coli*" (PMID 8226906), measured the three layers in *E. coli* by sequencing 866 *lacI* mutations across strains with the error-correction pathways disabled. **What he reports are fold-discriminations, not power-of-ten error rates** — verbatim, base selection discriminates against errors by **200,000–2,000,000-fold**, proofreading by **40–200-fold**, and mismatch repair by **20–400-fold**, "each depending on the type of error."

**The familiar decade decomposition is a different paper, and this chapter previously misattributed it to Schaaper.** It is Fijalkowska, Schaaper & Jonczyk (2012), *FEMS Microbiol Rev* 36(6):1105–1121, doi:10.1111/j.1574-6976.2012.00338.x, PMID 22404288 — a review, citing Schaaper — which reads, verbatim: "Roughly, the contribution of each of these components to the error rate can be estimated at 10⁻⁵ (insertion), 10⁻² (proofreading), and 10⁻³ (mismatch repair), accounting for the 10⁻¹⁰ overall rate, although each contribution is highly dependent on the precise type of error under question." Its abstract puts the overall rate at **10⁻⁹ to 10⁻¹¹ errors per base pair**.

**Keep the two apart, because the decades do not reproduce the measurement.** Proofreading at 40–200-fold is 10⁻¹·⁶–10⁻²·³; MMR at 20–400-fold is 10⁻¹·³–10⁻²·⁶. The round decades are the review's convenience — reasonable, explicitly hedged by its own "roughly," and *not* Schaaper's numbers. Kunkel's reviews (Kunkel 2004, *J Biol Chem* 279(17):16895–16898; Kunkel & Bebenek 2000, *Annu Rev Biochem* 69:497–529) give **in vitro** polymerase insertion fidelity at ~10⁻⁴–10⁻⁵, with 3′→5′ exonucleolytic proofreading and then MMR stacked on top.

Put the diploid genome through it (6.11 × 10⁹ bp, one replication):

| Layer | Error rate/bp | Errors per replication |
|---|---|---|
| Polymerase base selection alone | **~10⁻⁵** (in vivo estimate) — *cf.* ~10⁻⁴ in vitro | **~61,000** — *cf.* ~610,000 at the in-vitro rung |
| + 3′→5′ exonucleolytic proofreading (× ~10⁻²) | ~10⁻⁷ | **~610** |
| + mismatch repair (× ~10⁻³) | ~10⁻¹⁰ | **~0.6** |

**Read the ladder's own arithmetic before you trust it.** This table uses Fijalkowska et al.'s decomposition, which has the merit of actually *composing*: 10⁻⁵ × 10⁻² × 10⁻³ = 10⁻¹⁰ exactly. An earlier draft of this table started at the *in vitro* 10⁻⁴ rung and still printed **10⁻⁷** after proofreading — which silently requires a **10³** gain, contradicting the same row's own stated gain of 10¹–10², contradicting the text above it, and contradicting Schaaper's measured 40–200-fold. **That rung was arithmetically broken and is corrected here.** Nor does the corrected ladder escape the deeper problem: composing Schaaper's *measured* factors onto a 10⁻⁵ rung spans **~10⁻⁷·⁹ to ~10⁻⁹·⁹**, reaching 10⁻¹⁰ only at its most generous edge. **The decades are round because they were chosen to land on 10⁻¹⁰ — not because three measurements happened to multiply out that way.** The ladder is **MODELED** at every rung, and its rungs are the review's estimate, not any single paper's measurement.

**The principle survives that, and it generalises far beyond biology: nature did not build one perfect component. It stacked three cheap imperfect ones, each individually unimpressive, and multiplied their independent failure probabilities.** A ~10⁻⁵ part, a ~10⁻² filter, and a ~10⁻³ filter compose to 10⁻¹⁰. No single element in the chain is remarkable. The chain is. If you set out to build a 10⁻¹⁰ component you will fail; if you set out to build three cheap layers whose failures are uncorrelated, you will succeed. *The independence is the whole trick* — correlated failures collapse the product back toward the worst layer. **Note what that argument does and does not need:** it needs the layers to be cheap, stacked, and independent. It does not need any particular rung, which is fortunate, because the rungs are the softest numbers in this chapter.

**Now fence the first rung, because it is contested.** St Charles et al. (2015), *DNA Repair (Amst)* 31:41–51, doi:10.1016/j.dnarep.2015.04.006, dissected the layers *in vivo* in yeast and report, verbatim: in the absence of proofreading and MMR, Pol ε and Pol δ synthesise DNA in vivo "with apparent base selectivity that is **more than 100 times higher than measured *in vitro***." They further find proofreading is **strand-asymmetric** (Pol ε on the leading strand vs Pol δ on the lagging strand contribute differently), and that "on average, proofreading contributes more to replication fidelity than does MMR" — while the per-mismatch split "vary[s] from nearly all proofreading of some mismatches to mostly MMR of other mismatches."

So the tidy 10⁻⁵ → 10⁻⁷ → 10⁻¹⁰ ladder is a **teaching model assembled from measurements taken in different systems against different denominators**. **Three positions now sit on the first rung alone:** ~10⁻⁴ in vitro (Kunkel); ~10⁻⁵ as a review's in vivo estimate (Fijalkowska et al. 2012); and, measured in vivo in yeast, base selectivity **>100× better than in vitro** (St Charles et al. 2015) — which would push the rung below 10⁻⁶. **This pass did not reconcile them and does not print a reconciliation.** The *stacking principle* survives the discrepancy intact; the *specific rungs* do not travel without their assay.

One more denominator trap: the human germline rate of **1.20 × 10⁻⁸ per nucleotide per generation** (Kong et al. 2012, *Nature* 488(7412):471–475, doi:10.1038/nature11396, at mean paternal age 29.7, with paternal mutations doubling every ~16.5 years) is **per generation, not per replication**. A generation contains many germline divisions. Multiplying it by 6.11 Gbp gives ~73 de novo sites per generation as a MODELED figure — but do not set it beside 10⁻¹⁰ as if they measured the same thing.

## Packing: 2 metres into 6 micrometres

Do not cite the 2 m; derive it, from the rise:

```
3.055e9 bp x 0.34 nm/bp = 1.04 m  (haploid)
                        ~ 2.08 m  (diploid)
Nucleus, d = 6 um:  V = (4/3)pi(3 um)^3 = 113 um^3
Linear packing ratio: 2.08 m / 6e-6 m ~ 3.5e5
```

But run the *volume*, which almost nobody does. DNA as a cylinder of radius 1 nm:

```
V_DNA = pi (1e-3 um)^2 x 2.08e6 um = 6.5 um^3  ->  6.5 / 113 = ~5.8% of nuclear volume
```

**The nucleus is 94% not-DNA.** Packing is *not* a space problem. It is a **topology and access problem**: keep 2 m of a 50-nm-persistence-length polymer untangled, unbroken, and selectively readable. Volume was never the constraint. That reframing is the point.

The hierarchy, with its honesty applied where it is owed:

- **Nucleosome — solid.** Luger et al. (1997), *Nature* 389(6648):251–260, doi:10.1038/38444, solved the core particle at 2.8 Å with **146 bp** of α-satellite DNA wrapped **1.65 left-handed superhelical turns** around a histone octamer. The canonical **147 bp** comes from the higher-resolution follow-up: Richmond & Davey (2003), *Nature* 423:145, doi:10.1038/nature01595, at 1.9 Å. Both numbers are real; they are different crystals. (Richmond & Davey also found nucleosomal DNA carries "twice the curvature necessary" for the superhelical path — the bending is not gentle.)
- **The 30 nm fibre — CONTESTED in vivo, and this matters.** It is in every textbook. Maeshima, Hihara & Eltsov (2010), *Curr Opin Cell Biol*, doi:10.1016/j.ceb.2010.03.001 (PMID 20346642), asked directly — "Chromatin structure: does the 30-nm fibre exist in vivo?" — and report that cryo-EM of vitrified human mitotic cells, imaged close to native state, found **no 30-nm fibres**. Ou et al. (2017), *Science* 357(6349):eaag0025, doi:10.1126/science.aag0025, using ChromEMT electron tomography, found chromatin to be "a **disordered 5- to 24-nanometer-diameter curvilinear chain**" packed at varying 3D concentration — again no 30-nm fibre. (ChromEMT requires fixation, dehydration, heavy-metal staining and plastic embedding; cryo-ET does not. The two methods have different artifacts and agree anyway, which is why this is strong.) The 30 nm fibre is well established **in vitro**. Its existence as an in vivo structural level is **OBSERVED-CONTESTED** and should not be drawn in a diagram without the fence.
- **Loops / TADs / chromosome** — the levels above. **NOT-SOURCED in this pass.**

## Replication: the arithmetic that makes a huge genome copyable

Rates first (Milo & Phillips, *Cell Biology by the Numbers*, "How long does it take cells to copy their genomes?"):

- *E. coli* fork: **~600 bp/s** in vivo average (BNID 109251); classic figure ~1,000 nt/s.
- Eukaryotic fork: **4–40 bp/s** ≈ 1 kb/min (BNID 104930, 104935, 104936, 104937). **~25–150× slower.**

*E. coli*, 4.6 Mbp, one origin, bidirectional: `4.6e6 / (2 x 600) = 3,833 s = 64 min` (at 1,000 bp/s: 38 min). But *E. coli* divides in **~20 min** (BNID 103514) — faster than it can copy itself. The trick is **overlapping replication cycles**: fire new origins before the last round finishes, running >6 origins and >10 forks at once (BNID 102356). The cell is replicating a genome it has not finished replicating.

Humans cannot use that trick, and the fork is far slower. Do the arithmetic. Diploid 6.11 Gbp, one origin, two forks, v = 20 bp/s:

```
6.11e9 / (2 x 20) = 1.53e8 s = 4.8 YEARS
```

Measured S phase is **~10 hours** (BNID 103742, 103741, 102204). Solve for the origins required:

```
N = 6.11e9 / (2 x 20 bp/s x 3.6e4 s) ~ 4,200 origins
   (v = 4 bp/s -> ~21,000;  v = 40 bp/s -> ~2,100)
```

Measured human origin count: **~1,000 to 100,000** (BNID 107654, 109283). **The prediction lands inside the measurement.** 4.8 years → 10 hours, a factor of ~4,200, bought entirely by **parallelism at bidirectional origins** — not by a faster polymerase. (Pushed to the limit: *D. melanogaster* embryos copy ~120 Mbp every **8 minutes**, BNID 101971.) Nature's answer to "this component is too slow" was never "build a faster component."

## The code: 64 → 20, and why the redundancy is not noise

4³ = **64 codons**; **61 sense codons** for **20 amino acids** plus 3 stops. Average **3.05 codons per amino acid**. Information-theoretically the code throws away `log₂(64) − log₂(21) = 6 − 4.39 = 1.61 bits per codon`.

That discarded 1.61 bits is not waste — it is **error tolerance, and it is measurably non-random**. Freeland & Hurst (1998), *J Mol Evol* 47(3):238–248, doi:10.1007/PL00006381, PMID 9732450, scored the canonical code against randomly generated alternatives for how well it minimises the damage of point mutation and mistranslation (errors land on synonymous codons or on chemically similar amino acids, measured by polar requirement). Verbatim from the abstract: "if we employ weightings to allow for biases in translation, then **only 1 in every million random alternative codes generated is more efficient than the natural code**."

**The unweighted figure is a different paper, seven years earlier — and it is not quite the number everyone quotes.** Haig & Hurst (1991), *J Mol Evol* 33(5):412–417, doi:10.1007/BF02103132, PMID 1960738, "A quantitative measure of error minimization in the genetic code," report — verbatim — that "single-base changes in the natural code had a smaller average effect on polar requirement than **all but 0.02% of random codes**." **0.02% is ≈1 in 5,000, not 1 in 10,000.** The familiar 10⁻⁴ headline is a *secondary restatement*: Koonin & Novozhilov (2009), *IUBMB Life* 61(2):99–111, PMID 19117371, write that "the probability of a random code to be fitter than the standard one is *P*₁ ≈ 10⁻⁴" — a ~2× loosening of the primary it compresses. Freeland & Hurst 1998's abstract contains **no** 1-in-10,000 figure at all; an earlier draft of this chapter sourced both endpoints to that one paper, which misattributed Haig & Hurst's result.

So the famous pair is **two papers, two conditions, and one rounding** — not one paper's two settings. The "one in a million" arrives only once transition/transversion bias and mistranslation bias are weighted in. **Carry the conditions or the headline is not the result** — and carry the citation, or the headline is not even the right author's.

**The honest later critique, which is essential.** Novozhilov, Wolf & Koonin (2007), *Biol Direct*, "Evolution of the genetic code: partial optimization of a random code for robustness to translation error in a rugged fitness landscape" (PMID 17956616), find the standard code is "the result of **partial optimization** of a random code" — highly robust, "but there is a **huge number of more robust codes**," and it could evolve from a random code via a short series of codon reassignments. So: the code is **a local optimum on a rugged landscape, not the global optimum, and not a miracle**. "One in a million" and "not the best available" are both true. That pair is the whole discipline of this chapter in one line.

## The central dogma, and its real exceptions

DNA → RNA → protein, with information not flowing back out of protein. The exceptions are real, sourced, and not merely decorative:

- **Reverse transcription.** Temin & Mizutani (1970), *Nature* 226:1211–1213, doi:10.1038/2261211a0, and Baltimore (1970), *Nature* 226:1209–1211 — back-to-back in the same 27 June 1970 issue. RNA → DNA. The arrow reverses.
- **Prions.** Prusiner (1982), *Science* 216:136–144, doi:10.1126/science.6801762, PMID 6801762: "a small proteinaceous infectious particle which is resistant to inactivation by most procedures that modify nucleic acids." Heritable conformational information carried with **no nucleic acid**. The substrate itself is optional.

DNA is *a* hereditary substrate. It is not *the* hereditary substrate.

## The active-inference reading — HYPOTHESIZED, a lens only

Fenced explicitly. **This is a framing, not a measurement, and no observation below is offered as evidence for it.**

One may *read* the genome as a **prior over phenotypes**, fitted by ancestral surprise: lineages whose priors mispredicted their niche were deleted, so the surviving distribution encodes something about the statistics of the environments that did the deleting. The layered error budget then reads as **precision control** — the accuracy of transmission set to a value, not maximised, since a 10⁻¹⁰ genome and a 10⁻³–10⁻⁴ ribosome coexist in one cell by different budgets.

**This is a lens.** It generates questions (what would a measured prior look like? what units?). It measures nothing, predicts no number in the table above, and could be deleted from this chapter without changing a single value. Treat it accordingly. A UNI design must not cite it as support for anything.

## The numbers

| Symbol | Value | Units | Scope | Class | Source | Falsifier |
|---|---|---|---|---|---|---|
| `rise` | ~3.4 (0.34) | Å (nm) /bp | B-DNA | OBSERVED-REPLICATED | Potaman & Sinden, NCBI Bookshelf NBK6545; Watson & Crick 1953, *Nature* 171:737–738 | Structural measurement outside 3.3–3.5 Å under B-form conditions |
| `bp/turn` (fibre) | 10.0 | bp | B-form **fibre** diffraction | OBSERVED-REPLICATED | Watson & Crick 1953; as compared in Wang 1979 | Re-analysis of fibre data giving ≠10 |
| `bp/turn` (solution) | **10.4 ± 0.1** | bp | B-DNA free in solution, physiological; topoisomer gel | OBSERVED-REPLICATED | Wang 1979, *PNAS* 76(1):200–203, doi:10.1073/pnas.76.1.200 | Repeat topoisomer ladder; value outside 10.3–10.5 |
| `bp/turn` (Rhodes & Klug) | **10.6 ± 0.1** | bases | DNase I cutting periodicity on DNA immobilised on three surfaces; **the authors identify the value with the repeat *in solution*** | OBSERVED-REPLICATED | Rhodes & Klug 1980, *Nature* 286(5773):573–578, PMID 7402337 | Repeat digestion periodicity outside 10.5–10.7 |
| `bp/turn` 10.4 vs 10.6 | **unreconciled** — two primaries, same nominal condition (solution), two assays | bp | topoisomer ladder (Wang) vs DNase I periodicity (Rhodes & Klug) | **OBSERVED-CONTESTED** | Wang 1979; Rhodes & Klug 1980 | An assay reconciling the two, or a re-measurement collapsing the gap |
| `bp/turn` "10.5" | 10.5 | bp | quoted everywhere; **printed by Potaman & Sinden Table 1** as B-DNA residues/turn; sits between two unreconciled primaries | **NOT-SOURCED in this pass (value printed in source; provenance not traced)** | Potaman & Sinden, NBK6545 Table 1 | Establish whether 10.5 is an independent determination, a rounding, or a midpoint of 10.4 and 10.6 |
| `diameter` | 23 (A) / ~20 (B) / 18 (Z) | Å | A-, B-, Z-DNA | OBSERVED-REPLICATED | Potaman & Sinden, NBK6545 Table 1 | Structural measurement outside range |
| `groove widths` (12/6) | major ~12, minor ~6 | Å | B-DNA, convention **not sourced here** | **NOT-SOURCED in this pass** | not confirmed here — NBK6545 Table 1 has **no groove-width row**; the prior attribution to it was **fabricated** (recorded below) | Fetch a primary printing these values **and** naming the measurement convention |
| `groove widths` (22/12) | 22 / 12 | Å | widely repeated textbook pair — **different convention** | **NOT-SOURCED in this pass** | not confirmed here | Fetch a primary source and name the measurement convention |
| `groove` convention offset | ~5.8 | Å | claimed offset between P–P and vdW-corrected conventions | **NOT-SOURCED in this pass** | not confirmed here | Fetch a primary defining groove width as smallest P–P separation minus the phosphate diameter. Note it accounts for 12 → 6.2 ≈ 6 but **fails** on 22 → 16.2 ≠ 12 (a 10 Å gap), so it does **not** reconcile the two pairs |
| A-DNA | 11 bp/turn; rise 2.55 Å; C3′-endo; 9 Å axial hole; tilt ~20° | — | A-form | OBSERVED-REPLICATED | Potaman & Sinden, NBK6545 | Structural measurement outside range |
| Z-DNA | left-handed; 12 bp/turn; rise 3.7 Å; 18 Å; 30°/bp | — | Z-form, atomic-resolution crystal | OBSERVED-REPLICATED | Wang et al. 1979, *Nature* 282:680; Potaman & Sinden | Re-refinement contradicting handedness or repeat |
| `ℓ_p` | **~50 (~150)** | nm (bp) | dsDNA, ~0.1 M NaCl, **~20–25 °C**; tweezers + AFM consensus | OBSERVED-REPLICATED | Peters & Maher 2010, "DNA curvature and flexibility in vitro and in vivo," *Q Rev Biophys* 43(1):23–63, PMID 20478077 | Independent single-molecule measurement outside 45–55 nm **at the stated temperature and ionic strength** |
| `ℓ_p` vs temperature | **53.2 nm (5 °C) → 42.5 nm (42 °C)** | nm | **TBE + 10 mM MgCl₂ — a different ionic condition from the row above**; j-factor + linking-number methods. A **condition on** the 50 nm consensus, not support for it: at ≥37 °C it sits at or below that row's own falsifier band | OBSERVED-REPLICATED | Geggier, Kotlyar & Vologodskii 2011, *NAR* 39(4):1419–1426, doi:10.1093/nar/gkq932, PMID 20952402 | A measurement showing ℓ_p temperature-independent across 5–42 °C |
| `ℓ_p` sub-100 bp | short DNA **more bendable** than WLC predicts | — | <100 bp cyclisation | **OBSERVED-CONTESTED** | Vafabakhsh & Ha, *Science*, PMC3565842 | A cyclisation method restoring WLC agreement below 100 bp |
| `I/bp` | **2** | bits/bp | `log₂(4)`; **upper bound**, assumes no correlation | MODELED | Computed here | Arithmetic error (the bound itself is definitional) |
| `G_human` | **3,054,815,472** (+16,569 mtDNA) | bp | T2T-CHM13, gapless, chr1–22 + X | OBSERVED-REPLICATED | Nurk et al. 2022, *Science* 376:44–53, doi:10.1126/science.abj6987 | Independent T2T assembly differing >0.1% |
| `I_genome` | 6.11e9 bits ≈ **764 MB** (haploid); ~1.53 GB (diploid) | bits/bytes | at 2 bits/bp, T2T-CHM13 | MODELED | Computed here | Arithmetic error |
| `f_coding` | **1–2** (exome ~1.5) | % of genome | human | OBSERVED-REPLICATED | Piovesan et al. 2019, *BMC Res Notes*, doi:10.1186/s13104-019-4343-8 | Annotation revision moving coding fraction outside 1–2% |
| `pg→bp` | 1 pg = **0.978e9** | bp | flow-cytometry conversion | OBSERVED-REPLICATED | Doležel et al. 2003, *Cytometry A*, doi:10.1002/cyto.a.10013 | Re-derivation of nucleotide-pair molecular weight |
| `G_onion` | 16.75 pg ≈ **16.4** (≥95% repetitive) | Gbp | *Allium cepa* 1C | OBSERVED-REPLICATED | onion assembly literature (PMC8496297; PMC11865573) + Doležel conversion | Flow-cytometry re-measurement outside 15–18 Gbp |
| `G_lungfish` | **91** (~90% repeat) | Gbp | *Lepidosiren paradoxa* — largest **sequenced** animal genome | OBSERVED-REPLICATED | Schartl et al. 2024, *Nature* 634:96–103, doi:10.1038/s41586-024-07830-1 | Independent assembly differing >10% |
| `G_P.aethiopicus` | ~130 | Gbp | marbled lungfish — **estimate, NOT sequenced** | **OBSERVED-CONTESTED / NOT-SEQUENCED** | flagged as unsequenced in Schartl et al. 2024 coverage | Sequence it |
| `G_fern` | **160.45** | Gbp/1C | *Tmesipteris oblanceolata* — current eukaryotic record | OBSERVED-REPLICATED | Fernández et al. 2024, *iScience*, doi:10.1016/j.isci.2024.109889 | Independent flow cytometry differing >10% |
| `G_Paris` | 152.23 pg ≈ 149 | Gbp | *Paris japonica* 1C | OBSERVED-REPLICATED | Pellicer et al. 2010, *Bot J Linn Soc* 164(1):10, doi:10.1111/j.1095-8339.2010.01072.x | Re-measurement outside range |
| `G_Polychaos` | 670 pg (~655 Gbp) | — | *Polychaos dubium* — **DO NOT USE** | **INADMISSIBLE** | BNID 104470, flagged "dubious report / outdated value" | Re-measure single nuclei with modern methods |
| `ε_selection` | ~10⁻⁴–10⁻⁵ (in vitro); **~10⁻⁵** (in vivo *E. coli*, **a review's round estimate**) | per bp | polymerase base selection **alone** | **OBSERVED-CONTESTED** (assay-dependent) | Kunkel 2004, *JBC* 279(17):16895–8 (in vitro); Fijalkowska, Schaaper & Jonczyk 2012, *FEMS Microbiol Rev* 36(6):1105–1121, PMID 22404288 (the 10⁻⁵ estimate). **Schaaper 1993 measures a 200,000–2,000,000-fold discrimination, not a rate** | See in-vivo row below; an assay reconciling both |
| Schaaper's measured factors | base selection **200,000–2,000,000×**; proofreading **40–200×**; MMR **20–400×** | fold discrimination | *E. coli*, 866 sequenced *lacI* mutations in correction-deficient strains | OBSERVED-REPLICATED | Schaaper 1993, *JBC* 268(32):23762–23765, PMID 8226906 | A re-dissection outside these fold ranges |
| `ε_selection` in vivo vs in vitro | in vivo base selectivity **>100× higher** than in vitro | — | yeast Pol ε / Pol δ, proofreading- and MMR-deficient background | **OBSERVED-CONTESTED** | St Charles et al. 2015, *DNA Repair* 31:41–51, doi:10.1016/j.dnarep.2015.04.006 | An in-vitro assay reproducing the in-vivo selectivity |
| `ε_proof` | ~10⁻⁷ **as a ladder rung** (= 10⁻⁵ × the review's ~10⁻² factor) | per bp | + 3′→5′ exonucleolytic proofreading | **MODELED** — a review's round decade; **not** reproduced by the measured factor | rung from Fijalkowska et al. 2012; measured factor = **40–200×** (10⁻¹·⁶–10⁻²·³), Schaaper 1993, *JBC* 268(32):23762–23765 | An in vivo proofreading gain measured outside 40–200×. *Prior draft printed ~10⁻⁷ off a 10⁻⁴ rung with a stated gain of 10¹–10² — arithmetically impossible (needs 10³); corrected* |
| `ε_MMR` | **~10⁻¹⁰** overall as the ladder rung (× the review's ~10⁻³ factor); measured overall band **10⁻⁹–10⁻¹¹** | per bp | + mismatch repair; overall | **MODELED (the ladder rung); OBSERVED-REPLICATED (the overall band)** | Fijalkowska et al. 2012 (abstract: "as low as 10⁻⁹ to 10⁻¹¹ errors per base pair"); measured MMR factor = **20–400×** (10⁻¹·³–10⁻²·⁶), Schaaper 1993 | Mutation-accumulation whole-genome rate outside 10⁻⁹–10⁻¹¹ |
| ladder vs measured factors | Schaaper's measured factors on a 10⁻⁵ rung span **~10⁻⁷·⁹ to ~10⁻⁹·⁹** — reaching 10⁻¹⁰ only at the most generous edge | per bp | the decades do **not** reproduce from the measurement | **MODELED** | Computed here from Schaaper 1993 + Fijalkowska et al. 2012 | Arithmetic error; or a dissection whose measured factors compose to 10⁻¹⁰ |
| proofreading asymmetry | strand-asymmetric (Pol ε leading vs Pol δ lagging); proofreading > MMR **on average**, but varies per mismatch | — | yeast, in vivo | OBSERVED-REPLICATED | St Charles et al. 2015 | A dissection showing strand symmetry |
| errors/replication | ~6.1e4 → ~610 → **~0.6** | errors per diploid genome copy | 6.11 Gbp at 10⁻⁵ / 10⁻⁷ / 10⁻¹⁰ (in-vivo ladder); ~6.1e5 at the in-vitro 10⁻⁴ rung | MODELED | Computed here | Arithmetic error, or a refuted ε row |
| `μ_germline` | **1.20e-8** | per nt per **generation** (mean paternal age 29.7; +~2 mutations/yr; paternal doubling ~16.5 yr) | human trios — **different denominator from ε** | OBSERVED-REPLICATED | Kong et al. 2012, *Nature* 488(7412):471–475, doi:10.1038/nature11396 | Independent trio study outside range at matched paternal age |
| `n_denovo` | ~73 | sites/generation | `1.2e-8 x 6.11e9` | MODELED | Computed here | Arithmetic error; direct counts use a callable-fraction denominator |
| `L_DNA` | **1.04 (2.08)** | m, haploid (diploid) | `3.055e9 bp x 0.34 nm` | MODELED | Computed here from `rise` + `G_human` | Arithmetic error, or `rise` refuted |
| `V_nucleus` | ~113 | µm³ | sphere, d = 6 µm | MODELED | Computed here (geometry) | Geometric error; nuclei are not spheres |
| `f_DNA,vol` | **~5.8** | % of nuclear volume | DNA as r = 1 nm cylinder, 2.08 m, in 113 µm³ | MODELED | Computed here | Arithmetic error, or a refuted radius |
| packing ratio | ~3.5e5 | dimensionless (linear) | 2.08 m / 6 µm | MODELED | Computed here | Arithmetic error |
| `nucleosome` | **146** bp @ 2.8 Å; **147** bp @ 1.9 Å; 1.65 superhelical turns; histone octamer | bp | crystal structures — **different crystals, both real** | OBSERVED-REPLICATED | Luger et al. 1997, *Nature* 389:251–260, doi:10.1038/38444; Richmond & Davey 2003, *Nature* 423:145, doi:10.1038/nature01595 | A re-refinement changing the wrap length |
| 30 nm fibre **in vivo** | **contested — not observed** in cryo-EM of vitrified cells nor in ChromEMT | nm | in vivo interphase/mitotic chromatin | **OBSERVED-CONTESTED** | Maeshima et al. 2010, *Curr Opin Cell Biol*, PMID 20346642; Ou et al. 2017, *Science* 357:eaag0025, doi:10.1126/science.aag0025 | A near-native in-vivo imaging method resolving regular 30-nm fibres |
| chromatin chain in vivo | "disordered **5- to 24-nanometer-diameter curvilinear chain**" | nm | ChromEMT, interphase + mitosis | OBSERVED-REPLICATED | Ou et al. 2017 | Independent tomography contradicting the diameter distribution |
| loops / TADs / chromosome | — | — | levels above the chain | **NOT-SOURCED in this pass** | — | Fetch Hi-C / loop-extrusion primaries |
| `v_fork,ec` | **~600** (classic ~1,000) | bp/s | *E. coli*, in vivo average | OBSERVED-REPLICATED | BNID 109251; Milo & Phillips | In vivo measurement outside 400–1,000 bp/s |
| `v_fork,euk` | **4–40** (~1 kb/min) | bp/s | eukaryotic replisome | OBSERVED-REPLICATED | BNID 104930, 104935, 104936, 104937 | Outside range |
| `t_ec` | 64 min (at 600 bp/s); 38 min (at 1,000) | min | 4.6 Mbp, 1 origin, 2 forks | MODELED | Computed here | Arithmetic error |
| *E. coli* multi-fork | >6 origins, >10 forks; doubling ~20 min < copy time | — | fast growth — overlapping cycles | OBSERVED-REPLICATED | BNID 102356; BNID 103514 | A fast-growing strain with a single round per division |
| `t_human,1origin` | **4.8** | years | 6.11 Gbp, 1 origin, 2 forks, 20 bp/s | MODELED | Computed here | Arithmetic error |
| `T_S` | **~10** | hours | human S phase | OBSERVED-REPLICATED | BNID 103742, 103741, 102204 | Cell type outside range |
| `N_origins` (required) | **~4,200** (2,100–21,000 over v = 40–4 bp/s) | origins | solved from `G/(2vT)` | MODELED | Computed here | Arithmetic error |
| `N_origins` (measured) | **1,000–100,000** (Drosophila ~10,000) | origins | human | OBSERVED-REPLICATED | BNID 107654, 109283 | A measurement excluding the predicted band |
| `t_Dmel` | ~8 | min per ~120 Mbp genome | *D. melanogaster* embryo | OBSERVED-REPLICATED | BNID 101971 | Outside range |
| codons | **64** → 61 sense + 3 stop → **20** aa; 3.05 codons/aa | — | canonical code | OBSERVED-REPLICATED | standard; Freeland & Hurst 1998 | A canonical-code recount |
| bits discarded | **1.61** | bits/codon | `log₂(64) − log₂(21)` | MODELED | Computed here | Arithmetic error |
| code optimality (unweighted) | natural code beats **all but 0.02%** of random codes on polar requirement (**≈1 in 5,000**) | — | polar-requirement metric; all single-base errors equiprobable | OBSERVED-REPLICATED | Haig & Hurst 1991, *J Mol Evol* 33(5):412–417, doi:10.1007/BF02103132, PMID 1960738 | Re-run the unweighted simulation; a figure outside 0.02% |
| code optimality — the "1 in 10⁴" headline | **P₁ ≈ 10⁻⁴** | — | a **secondary restatement** of Haig & Hurst, ~2× looser than their 0.02%; **not** a figure in Freeland & Hurst 1998, to which this chapter previously misattributed it | OBSERVED-REPLICATED *(as a restatement, not a primary)* | Koonin & Novozhilov 2009, *IUBMB Life* 61(2):99–111, PMID 19117371 | Locate a primary reporting 10⁻⁴ directly, or retire the headline in favour of 0.02% |
| code optimality (weighted) | **1 in 10⁶** random codes beat it | — | + transition/transversion bias + mistranslation bias weighted in | OBSERVED-REPLICATED | Freeland & Hurst 1998, *J Mol Evol* 47(3):238–248, doi:10.1007/PL00006381, PMID 9732450 | Re-run the simulation with the stated weightings |
| code = **partial** optimum | "huge number of more robust codes" exist; standard code = partial optimisation of a random code on a rugged landscape | — | — | OBSERVED-REPLICATED | Novozhilov, Wolf & Koonin 2007, *Biol Direct*, PMID 17956616 | A search failing to find more robust codes |
| reverse transcription | RNA → DNA | — | Rous sarcoma virus / RNA tumour viruses | OBSERVED-REPLICATED | Temin & Mizutani 1970, *Nature* 226:1211–1213, doi:10.1038/2261211a0; Baltimore 1970, *Nature* 226:1209–1211 | — |
| prion | heritable conformational information, **no nucleic acid required** | — | scrapie agent | OBSERVED-REPLICATED | Prusiner 1982, *Science* 216:136–144, doi:10.1126/science.6801762 | A nucleic acid found necessary for infectivity |
| genome-as-prior | — | — | active-inference reading | **HYPOTHESIZED** | this chapter, as a lens | Specify a measurable prior with units, then measure it |

## Falsifier (operable)

The chapter's central structural claim — **that DNA's extraordinary system-level properties are bought by composing cheap, individually unimpressive layers whose failures are uncorrelated, not by building excellent components** — is refuted by exhibiting **either**:

1. **a single replication component that achieves ≤10⁻⁹ errors/bp on its own**, with proofreading and mismatch repair genetically ablated, at physiological rate; **or**
2. **a eukaryotic cell copying a ≥1 Gbp genome within one measured S phase from ≤10 origins**, i.e. buying the throughput with fork speed rather than parallelism.

Either result moves the chapter. Neither *Thiomargarita*-style redescription nor a faster polymerase variant qualifies: the claim is about **where the performance comes from**, and it dies only if performance is shown to come from one place.

Secondary falsifiers are row-local: any number in the table found outside its stated scope **under its stated assay** moves that row and only that row. A refuted row does not refute the chapter; a refuted layering principle does.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **`G_Polychaos` = 670 pg (~655 Gbp) as "the largest genome"** — **INADMISSIBLE.** Still the top hit in popular sources; still wrong to cite. **Receipt of failure:** BNID 104470 carries it flagged "dubious report" and "outdated value"; the measurement used 1960s methods assaying **whole cells rather than isolated nuclei**, and has never been repeated with modern methods. Excluding it, the records are *Tmesipteris oblanceolata* (160.45 Gbp) and *Lepidosiren paradoxa* (91 Gbp, sequenced). Recorded, not mocked — it was an honest 1960s measurement, and the defect is in **re-citing it in 2026**, not in having made it.
- **"DNA is a program / source code / blueprint"** — **INADMISSIBLE as stated.** No falsifier accompanies it; it is a metaphor doing argumentative work. The receipt is in this chapter's own numbers: 1–2% coding; a 52× genome in a fork fern; ≥95% repeat content in an onion. Keller, *The Century of the Gene* (Harvard UP, 2000), argues the cell may as well be read as the program and DNA as (part of) the data; Peluffo (2015), *Genetics* 200(3):685–696, doi:10.1534/genetics.115.178418, traces the metaphor's genesis and its failures — it omits temporality, mechanical forces in development, symbiosis, and environment. **A GPT that thinks DNA is source code will design wrong**: it will look for a specification where there is a *prior*, expect compile-time determinism where there is *context-dependent chemistry*, and treat 98% of the substrate as dead weight to be optimised away.
- **`10⁻¹⁰` quoted as DNA polymerase's error rate** — **NEGATIVE / conflation trap.** It is the rate *after three layers*. The polymerase alone is ~10⁻⁴–10⁻⁵ in vitro. Recorded because it is the single most common error in this material.
- **`1.2 × 10⁻⁸` (per generation) set beside `10⁻¹⁰` (per replication)** — **NEGATIVE / conflation trap.** Different denominators. A generation contains many germline divisions; the numbers are not comparable and their ratio means nothing.
- **The layered stack presented as one coherent in vivo measurement** — **NOT-RECONCILED, recorded as such.** The ladder now printed (10⁻⁵ → 10⁻⁷ → 10⁻¹⁰) is Fijalkowska et al. 2012's round-decade estimate: self-consistent, but it does **not** reproduce from Schaaper's measured fold-discriminations. St Charles et al. 2015 measure in vivo base selectivity **>100× higher than in vitro**. This pass did **not** reconcile them and prints no reconciliation. The stacking *principle* survives; the *rungs* do not travel without their assay.
- **The power-of-ten decomposition (10⁻⁵ / 10⁻² / 10⁻³ → 10⁻¹⁰) attributed to Schaaper 1993** — **NEGATIVE / this chapter's own misattribution, now corrected.** Schaaper 1993 reports **fold-discriminations** (200,000–2,000,000× / 40–200× / 20–400×), not decades, and its abstract contains no "about 10⁻¹⁰" clause — a clause this chapter previously printed **in quotation marks** against his name. The decomposition and that clause belong to Fijalkowska, Schaaper & Jonczyk 2012, *FEMS Microbiol Rev* 36(6):1105–1121 — a review, citing Schaaper. **A quotation mark is a claim about a source, and it was false here.**
- **The ladder rung 10⁻⁴ → 10⁻⁷ under a stated gain of 10¹–10²** — **NEGATIVE / arithmetically impossible, now corrected.** 10⁻⁴ × 10⁻¹ = 10⁻⁵ and 10⁻⁴ × 10⁻² = 10⁻⁶; reaching 10⁻⁷ needs **10³**, which contradicted the row's own gain, the chapter's own text, and Schaaper's measured 40–200×. The row was graded OBSERVED-REPLICATED while contradicting itself. It generated the printed ~610 figure, which survives only because the first rung moved to 10⁻⁵.
- **The 30 nm chromatin fibre drawn as an established in vivo level** — **NEGATIVE.** Two independent near-native methods (cryo-EM of vitrified cells; ChromEMT) fail to find it. It is real **in vitro**. Textbook diagrams showing it inside a living nucleus are ahead of the evidence.
- **"~10.5 bp/turn" explained as a midpoint of a solution value and a surface value** — **NEGATIVE / this chapter's own error, now corrected.** Rhodes & Klug explicitly identify their 10.6 with "the number of base pairs per turn of the DNA double helix **in solution**." So 10.4 and 10.6 are two assays of the **same quantity under the same nominal condition**, and their disagreement is **method-dependent and unreconciled here** — *not* dissolved by "two conditions, both right," which was a resolution this chapter invented and its own cited source refutes. 10.5 is printed as B-DNA's residues/turn by Potaman & Sinden Table 1; whether it is an independent determination or a rounding is **NOT-SOURCED in this pass**. Use it as shorthand, never as a receipt.
- **Attributing the 12/6 Å groove widths to Potaman & Sinden (NBK6545)** — **NEGATIVE / a fabricated citation by this chapter, now corrected.** NBK6545's Table 1 has **no groove-width row** (its rows: handedness, residues/turn, axial rise, pitch, tilt, rotation/residue, diameter, glycosidic bond, sugar pucker), and its prose treats the grooves qualitatively. The values are standard and may well be right; **the receipt was invented.** Recorded because of *where* it happened: in the very passage that lectures "name the convention or do not print the number," graded OBSERVED-REPLICATED. **The chapter committed its own cardinal defect (RES IPSAE NON SIMULACRA) in the sentence warning against it.** That is the most instructive failure in this file.
- **Groove widths quoted without a convention** — **NEGATIVE, and the convention story does not close.** Both pairs are now **NOT-SOURCED here.** The ~5.8 Å offset accounts for the minor pair (12 → 6.2 ≈ 6) but **fails on the major pair** (22 → 16.2, not 12 — a **10 Å** gap). "Different convention" is therefore **not** a sufficient explanation, and this chapter no longer asserts it as one. The ~5.8 Å figure is itself unsourced here.
- **NOT-MEASURED / NOT-SOURCED in this pass:** loops, TADs, and chromosome-level organisation; the exact Franklin & Gosling 1953 pagination; **both groove-width pairs (12/6 and 22/12) and the ~5.8 Å convention offset**; **the provenance of "10.5 bp/turn"**; **any reconciliation of Wang's 10.4 with Rhodes & Klug's 10.6**; any reconciliation of the in vivo and in vitro fidelity stacks; a primary reporting the code-optimality figure as 10⁻⁴ directly (the primary says 0.02%).

## HONEST FENCE — MODELED

Fenced **MODELED**. Individual rows carry their own classes (most OBSERVED-REPLICATED; several OBSERVED-CONTESTED; one INADMISSIBLE; several NOT-SOURCED). But the *chapter as an artifact* is a budget model: it composes measured constants through stated assumptions — a spherical nucleus, DNA as a 1 nm-radius cylinder, a mid-range 20 bp/s fork, 2 bits/bp with no sequence correlation, and a fidelity ladder assembled from **different assays in different organisms**. **The assumptions are the fence.** The origin-count prediction (~4,200) lands inside the measured band (1,000–100,000), but that band spans two orders of magnitude and is therefore a **weak** test — do not oversell the agreement.

Per **Gould & Lewontin (1979), "The Spandrels of San Marco and the Panglossian Paradigm"**: nothing above establishes that any feature of DNA is an optimum. The C-value paradox is itself the loudest evidence *against* pan-adaptationism in this chapter — genome size is substantially drift, transposon load, and frozen accident, not design. Novozhilov et al. 2007 say the same of the code: a **local** optimum on a rugged landscape. **Nature's authority here is precisely and only this: it already ran a very long parallel search under real physical constraints, with the failures deleted.** That makes the layering principle a **hypothesis generator**. It does not make it a proof. Per repo rule **M7**, any UNI design taking the stacked-cheap-layers principle from this chapter must still beat a **tuned** conventional baseline (e.g. one high-quality component) on a **pre-registered** metric, with a discriminator that collapses the gain and a true computed-residual ablation — or it is recorded **NEGATIVE**.

## Not claimed

- **Not claimed:** that DNA is a program, code, blueprint, or specification. It is a chemically stable, high-fidelity, mechanically characterised information substrate whose readout is context-dependent and whose bulk is not specification. The metaphor's critique is cited above and is load-bearing, not decorative.
- **Not claimed:** that 2 bits/bp is the genome's information content. It is an **upper bound** that assumes independence across positions. Real genomes are correlated; the true figure is lower and is **NOT-MEASURED here**.
- **Not claimed:** that the non-coding 98% is junk. The C-value paradox refutes *"genome size measures design content"* — it does **not** establish what any particular sequence does. The ENCODE claim that >80% of the genome is functional is **contested**: Graur et al. (2013), *Genome Biol Evol* 5(3):578–590, doi:10.1093/gbe/evt028, argue it conflicts with the <10% estimated to be under purifying selection. **This chapter takes no position** and asserts neither 80% nor 10%.
- **Not claimed:** that the fidelity ladder's rungs are settled. They are assay-dependent and the in vivo/in vitro discrepancy is printed, unreconciled.
- **Not claimed:** that the 30 nm fibre does not exist. It exists in vitro. Its status as an **in vivo** structural level is contested and carried as contested.
- **Not claimed:** that the genome-as-prior reading measures anything, predicts anything, or supports any UNI design. It is fenced **HYPOTHESIZED** and is deletable without changing one number in this chapter.
- **Not claimed:** that any citation above raises any UNI rung. **A nature citation is NEVER a UNI gate.** The NATURA classes (OBSERVED-REPLICATED / OBSERVED-CONTESTED / MODELED / HYPOTHESIZED / INADMISSIBLE / NOT-MEASURED) and the UNI ledger's four values (proven / designed / hypothesized / not-yet-built) describe different kinds of claim and never merge. This chapter contains **zero** UNI claims.
- **QUAESTIO-APERTA:** "full human" and "beyond human" appear nowhere here as a target, milestone, or deliverable. They are permanent open questions. Sequencing a genome has no bearing on them, and the ability to write one has no bearing on them either.
