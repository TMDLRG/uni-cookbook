# NA-03 — How to research, observe, and make new science with falsifiable evidence

> **What you are reading.** The operable procedure for turning an observation into a claim that can be killed. Not a philosophy of science: a checklist a builder can run tomorrow morning. Every rule below is stated as an action with a receipt and a way to fail. The chapter ends by showing how to make something genuinely NEW — which, in practice, means learning to recognise a residual and refusing to explain it away.
>
> **Hard fence, stated first because everything after it depends on it:** a nature citation is NEVER a UNI gate. Reading Platt raises no rung. Citing Popper makes nothing in this program `proven` — that word belongs exclusively to the UNI ledger's own 4-value fence and is never used in this wing for nature's science. This chapter describes how science is made. It asserts no UNI capability whatsoever.

---

## 1. The asymmetry: why "it fits" is nearly worthless

Confirmation and refutation are not symmetric, and the whole method rests on that. Any number of agreeing observations leaves a universal claim standing but unearned; one clean disagreeing observation kills it. Popper's demarcation: a system is empirical only if it forbids something — "it must be possible for an empirical scientific system to be refuted by experience" (Popper, *The Logic of Scientific Discovery*, 1959; quoted in Platt 1964, p. 350).

The operational consequence is blunt. If your hypothesis is compatible with every outcome you can imagine, you have no hypothesis, you have a vocabulary. Before you run anything, write down the observation that would make you abandon the idea. If you cannot write that sentence, stop — no amount of data collection will convert you.

The corollary builders skip: **fit is cheap.** A model that fits is a model that was flexible enough to fit. The question is never "does it fit," it is "was this fit at risk?"

## 2. The procedure: Platt's strong inference (this is the core of the chapter)

Platt's claim: fields advance at wildly different rates, and the fast ones share a method applied "formally and explicitly and regularly" rather than occasionally. His steps, verbatim (Platt 1964, *Science* 146:347–353, p. 347):

> 1) Devising alternative hypotheses;
> 2) Devising a crucial experiment (or several of them), with alternative possible outcomes, each of which will, as nearly as possible, exclude one or more of the hypotheses;
> 3) Carrying out the experiment so as to get a clean result;
> 1′) Recycling the procedure, making subhypotheses or sequential hypotheses to refine the possibilities that remain; and so on.

Read step 2 again. The experiment is not designed to *support* your favourite; it is designed so that **each possible outcome deletes something**. An experiment whose every outcome leaves all hypotheses alive is not an experiment, it is an expense.

Platt's image for the recursion is a tree: "at the first fork, we choose — or, in this case, 'nature' or the experimental outcome chooses — to go to the right branch or the left." He calls it a "conditional inductive tree" or "logical tree," and notes it is already written down in first-year chemistry — the qualitative-analysis table, where you add reagent A and the red precipitate itself selects your next move (p. 347). His verdict on anything else: **"Any conclusion that is not an exclusion is insecure and must be rechecked"** (p. 348). His touchstone, which costs nothing and can be carried anywhere — he calls it The Question (p. 352):

> "But sir, what experiment could disprove your hypothesis?" or on hearing a scientific experiment described, "But sir, what hypothesis does your experiment disprove?"

Ask it of your own work, before you write code, not after. Platt's diagnosis of why we don't: "We become 'method-oriented' rather than 'problem-oriented'" (p. 348).

**How to execute it.** Write the tree down as a file, before the build. Each node: the K hypotheses live here; the measurement; the outcome→exclusion mapping stated in advance (*if I see X, hypothesis 2 dies; if Y, 1 and 3 die*). Run it, record which branch nature took, recycle. The file is the artifact. If the outcome→exclusion mapping was not written before the run, you did not do strong inference — you did storytelling with a dataset.

## 3. Chamberlin: multiple working hypotheses, or the ruling theory eats you

Platt's step 1 is load-bearing and has its own literature. Chamberlin (1890, *Science* ns-15(366):92–96; reprinted 1965, *Science* 148:754–759) diagnosed the failure mode exactly:

> "The moment one has offered an original explanation for a phenomenon which seems satisfactory, that moment affection for his intellectual child springs into existence and as the explanation grows into a definite theory his parental affections cluster about his offspring and it grows more and more dear to him…" (quoted in Platt 1964, p. 350)

His remedy is not neutrality, it is **plurality**: the method "differs from the simple working hypothesis in that it distributes the effort and divides the affections." Each hypothesis brings its own criteria and means of testing; a family of them "encompass[es] the subject on all sides."

The operable rule: **K ≥ 2 always, K ≥ 3 for anything you intend to claim.** One hypothesis plus a null is not multiple working hypotheses — the null is usually a strawman you already know how to beat. Make the K *structurally distinct*: differing in mechanism, not in parameter. Platt saw the deeper payoff: with a single Ruling Theory each, disputes become conflicts between men; with multiple hypotheses on the table, "it becomes purely a conflict between ideas" (p. 350). That is a social benefit with an epistemic mechanism, and it is why the rule survives contact with a real lab.

## 4. Severity: when a passing test actually counts

A test your claim passed tells you something only if it *could have failed*. Mayo's severity requirement makes this operational (Mayo, *Statistical Inference as Severe Testing*, CUP 2018; Mayo & Spanos 2006, *BJPS* 57:323–357). Weak form: you do **not** have evidence for claim C if the method that produced agreeing data x had little capability of finding flaws in C even if C were false. Strong form: if C passed a test that had high capability of contradicting C, the passing outcome is evidence for C.

Put it on the pre-run checklist as one line: **"If C were false, what is the probability this exact procedure would still have passed it?"** If the answer is "high" or "I don't know," the test is not severe and its pass is worth nothing, whatever p-value is attached. A weak pass and a severe pass are different species of result and must never share a column.

## 5. Pre-register; touch the held set once; read the bound, not the point

Three rules, and they are one rule.

**Pre-register the bar before the build.** The margin, the threshold, the named ablation expected to collapse the gain, the stopping rule. Simmons, Nelson & Simonsohn (2011) make the stopping rule requirement #1 for authors: decide the rule for terminating data collection *before* collection begins and report it. "The rule itself is secondary, but it must be determined ex ante and be reported."

**Touch the held-out set exactly ONCE**, behind a seal-before-scoring step and a once-only sentinel. A held set scored twice is a training set with a good reputation.

**The verdict is the confidence-interval bound that excludes the threshold, never the point estimate.** This is the UNI repo's own rule M2 (`../wing-mu/mu2-bars-before-build.md`; `CLAIM-LEDGER.md` §3), cited here as method, raising nothing. The 1919 eclipse shows why it matters. Two model predictions for starlight deflection at the solar limb: general relativity 1.75″, the Newtonian half-deflection 0.87″ (Dyson, Eddington & Davidson 1920, *Phil. Trans. R. Soc. A* 220:291–333). Measured: Sobral 4-inch 1.98 ± 0.12″; Príncipe 1.61 ± 0.31″. Computing from those published values (my arithmetic, not theirs): Sobral sits ~9.3 sigma above the Newtonian value and ~1.9 sigma above the GR value; Príncipe ~2.4 sigma above Newtonian and ~0.5 sigma from GR. The honest reading: 1919 **severely excluded the Newtonian value** and was **consistent with, but did not pin, the GR value**. That is a real result, and it is not the result "Einstein confirmed." The excluding bound is the verdict; the point estimate is decoration.

Note what travels with it: the Sobral 16-inch plate set was excluded as "diffused and apparently out of focus." That exclusion may well be correct on instrument grounds — and it is exactly the researcher degree of freedom that Simmons requirement #5 exists to force into daylight (*if observations are eliminated, report the results with them included*). An exclusion is not a sin. An **undisclosed** exclusion is.

## 6. The tuned baseline and the load-bearing discriminator

A gain over a strawman is not a gain. Three things are required together (UNI rule M7, `CLAIM-LEDGER.md` §3, cited as method):

1. **A tuned strong baseline.** Tune the baseline with the same effort you spent on your method. An untuned baseline measures your enthusiasm, not your mechanism.
2. **A load-bearing discriminator that COLLAPSES the gain.** Shuffle the labels; swap the markers; ablate the mechanism to zero. If the gain survives its own mechanism being destroyed, the gain was never the mechanism's — it was leakage, and you have just measured your pipeline.
3. **A true ablation that is a computed residual, not a literal.** An ablation number typed in by hand is a claim about a run that did not happen.

The discriminator is the biomimetic design's specific gate, too. "Nature does it this way" earns nothing until the nature-derived design beats the tuned conventional baseline on the pre-registered metric. If it does not, record NEGATIVE and keep the receipt.

## 7. Statistical honesty: the numbers that should scare you into method

**Flexibility manufactures significance.** Simmons et al. (2011) simulated 15,000 samples per scenario on a two-condition design with 20 observations per cell, and measured the false-positive rate at p<.05 under four ordinary researcher degrees of freedom: two dependent variables, 9.5%; adding 10 more observations per cell and re-testing, 7.7%; controlling for gender or its interaction, 11.7%; dropping one of three conditions, 12.6%. Combined, all four: **60.7%**. Their words: "A researcher is more likely than not to falsely detect a significant effect by just using these four common researcher degrees of freedom." Note the class of that number — it is MODELED, from a simulation whose assumptions are its fence, and it is quoted here as MODELED, not as a measured field rate.

**The garden of forking paths.** You do not need to p-hack deliberately. Gelman & Loken (2014, *American Scientist* 102(6):460) point out that a researcher making reasonable, data-contingent analytic choices produces the same inflation without ever running a test twice — the multiple comparisons happened in the counterfactual analyses you *would* have run had the data looked otherwise. This is why pre-registration, not virtue, is the fix.

**HARKing.** Kerr (1998, *Personality and Social Psychology Review* 2(3):196–217) named it: Hypothesizing After the Results are Known — presenting a post hoc hypothesis as if it were a priori. HARKing converts an exploratory finding into a fraudulent confirmation while feeling like good writing.

**Power.** Button et al. (2013, *Nature Reviews Neuroscience* 14:365–376, doi:10.1038/nrn3475) estimated a median statistical power of **21%** across 49 meta-analyses covering 730 studies in the 2011 neuroscience literature. At 21% power, a "significant" result is more likely to be noise dressed up than signal, and any effect that does clear the bar is necessarily overestimated. This figure is CONTESTED: Nord et al. (2017, *J. Neurosci.* 37(34):8051–8061) reanalysed the same data with mixture modelling and found substantial heterogeneity across subfields rather than a single field-wide median. Both positions are carried here; neither is suppressed.

**Replication.** The Open Science Collaboration (2015, *Science* 349:aac4716) replicated 100 studies from three psychology journals: 97% of the originals reported statistically significant results; **36%** of the replications did. Replication effect sizes were about half the originals; 47% of original effect sizes fell inside the replication's 95% CI. This is CONTESTED: Gilbert, King, Pettigrew & Wilson (2016, *Science* 351:1037) argued the estimate was biased low by low power and protocol infidelities, and the OSC replied in the same issue. Carry both. Note also Scheel, Schijen & Lakens (2021, *AMPPS*, doi:10.1177/25152459211007467): **96%** positive results in a sample of the standard psychology literature versus **44%** in Registered Reports, where review and the publication decision happen before results are known. The descriptive gap is not in dispute; the causal attribution to preregistration is, because Registered Reports differ from the comparison sample in more than their timing.

**Why it compounds.** Ioannidis (2005, *PLoS Med* 2(8):e124, doi:10.1371/journal.pmed.0020124) models the positive predictive value of a research finding as a function of pre-study odds, power, bias, and the number of teams chasing the same effect, and concludes that for most designs and settings it is more likely for a claim to be false than true. This is a MODEL. Its assumptions are its fence, and it is quoted as MODELED.

**The practical rule:** report the effect size and its interval; the p-value is at best a screening statistic and at worst a decoy (Wasserstein & Lazar 2016, *The American Statistician* 70(2):129–133). An effect with no size is not a finding.

## 8. Measurement first: units, calibration, and the provenance that travels

No hypothesis survives a bad instrument, and instruments lie quietly.

**Precision is not accuracy.** Precision is the spread of repeated measurements; accuracy is closeness to the true value. A tight cluster in the wrong place is a precise, inaccurate, and extremely convincing instrument. You cannot detect the offset by measuring more — only by calibrating against a standard. (Vocabulary per JCGM 200:2012, the *International Vocabulary of Metrology*; uncertainty per JCGM 100:2008, the GUM.)

**Units are part of the claim.** A number without units is not a value, and a value without a scope is not a claim. Since 20 May 2019 the SI is defined by fixing exact numerical values for defining constants — Δν_Cs = 9 192 631 770 Hz, c = 299 792 458 m/s, h = 6.626 070 15 × 10⁻³⁴ J·s, e = 1.602 176 634 × 10⁻¹⁹ C, k = 1.380 649 × 10⁻²³ J/K, N_A = 6.022 140 76 × 10²³ mol⁻¹ (BIPM, *SI Brochure*, 9th ed., 2019). **These are conventions, not measurements** — they carry no evidence class in this wing's vocabulary, and that is the lesson: h is no longer measured, the kilogram is measured against it. Know which of your numbers are definitions and which are observations. Confusing them is a category error that no statistic will catch.

**The instrument has its own error, and it is not the last term you should add — it is the first one you should hunt.** OPERA (2011, arXiv:1109.4897) measured muon neutrinos arriving 60.7 ± 6.9 (stat) ± 7.4 (sys) ns earlier than light over the 730 km CERN→Gran Sasso baseline, i.e. (v−c)/c ≈ 2.48 × 10⁻⁵. The collaboration did the right thing — published the anomaly with full error budget and explicitly declined to interpret it. Then a loose fibre-optic connector between the GPS antenna and the master clock was found, worth ~73.2 ns, plus a master-clock oscillator off by 0.124 ppm in the opposite direction. The 2012 re-measurement gave 6.5 ± 15 ns: consistent with zero. The claim died. **The method worked exactly as designed** — and it worked because the provenance set (what was measured, on what instrument, by whom, when, through which cable) had been kept well enough to find the cable.

That is the rule: **the provenance set travels with the datum, permanently.** A number separated from its instrument, its operator, its timestamp, and its calibration state is an orphan, and an orphan cannot be debugged — only believed or disbelieved.

## 9. Controls, blinding, randomization — and the positive control nobody runs

Blinding is not hygiene theatre; the bias is measured. Schulz, Chalmers, Hayes & Altman (1995, *JAMA* 273(5):408–412, doi:10.1001/jama.273.5.408) assessed 250 controlled trials from 33 meta-analyses: odds ratios were exaggerated by **41%** in trials with inadequately concealed allocation, **30%** with unclearly concealed allocation, and **17%** in trials that were not double-blind. This has been replicated and refined: Wood et al. (2008, *BMJ*; 1,346 trials across 146 meta-analyses) and Savović et al. (2012, *Ann. Intern. Med.* 157(6):429–438; 7 datasets, 1,973 trials) found the exaggeration concentrated in **subjectively** assessed outcomes — ratio of odds ratios 0.69 (95% CI 0.59–0.82) for inadequate/unclear concealment and 0.75 (0.61–0.93) for lack of blinding — with little evidence of bias for objective outcomes (0.91, 95% CI 0.80–1.03; and 1.01, 0.92–1.10). The refinement is the interesting part: the effect is real, and it is *scoped*. That is what replication buys you — not a louder yes, but a sharper boundary.

**Randomize** to break the correlation between assignment and everything you didn't think of. That is the whole point: randomization protects against the confounders you cannot name, which are the ones that will get you.

**Run the positive control.** A negative control tells you your pipeline doesn't invent signal. A **positive control** — a manipulation with a known, expected effect — tells you your pipeline can *detect* signal at all. Without it, a null result is uninterpretable: you cannot distinguish "no effect" from "broken assay," and those two conclusions have nothing in common. Most nulls that get quietly binned are missing exactly this. Run both, always, in the same batch.

## 10. The negative result is a result

A negative is content, not an exit. Michelson & Morley (1887, *Am. J. Sci.* (3rd ser.) 34:333–345) predicted a 0.40-fringe displacement from Earth's motion through the ether; the observed maximum was 0.02 fringes and the average "much less than 0.01," bounding any relative ether velocity below roughly one-sixth of Earth's ~30 km/s orbital velocity — under ~5 km/s. It found nothing. It is one of the most consequential experiments ever run, and it is consequential **because** the bound was tight enough to hurt. A null with a wide bound is a shrug; a null with a tight bound is a wall that theory now has to route around.

So: publish either way, and publish the bound, not the shrug. If you cannot state how small the effect must be given your null, you have not finished the analysis. The UNI ledger applies the same rule to itself — negatives are sealed and signed by the identical machinery that signs passes, and a method that can only produce passes is not a method.

## 11. How to make something NEW: the anomaly loop

New science is not made by having a better idea. It is made by finding a **residual the current model cannot absorb** and then refusing to make it go away. The procedure:

1. **Find the residual.** Subtract the best current model from the observation. What's left is your raw material. Most of the time it is your instrument (see §8) — which is why step 2 exists.
2. **Falsify the mundane first.** Exhaust the boring explanations: calibration drift, leakage, a loose cable, contamination, a bug, a confound. Penzias & Wilson (1965, *ApJ* 142:419–421) had ~3.5 K of excess antenna temperature at 4080 Mc/s that they could not remove. They hunted it for months. They evicted the pigeons and scrubbed the droppings out of the horn. **The excess stayed.** That is when a residual becomes physics. The mundane causes are not an obstacle to the discovery — clearing them *is* the discovery's evidence.
3. **Characterize it.** Is it stable? Isotropic? Does it scale? Does it depend on anything you can turn? An anomaly you cannot describe quantitatively is a rumour. Mercury's perihelion residual survived this step for over half a century: ~43″ per century of precession that Newtonian mechanics could not account for (Le Verrier 1859, refined by Newcomb 1882), stable, measured, and stubbornly unexplained.
4. **Propose K ≥ 2 competing mechanisms.** For Mercury, the live hypotheses included an undiscovered planet, a solar oblateness term, a modified force law, and — eventually — a new theory of gravity. Note that "Vulcan" was a perfectly respectable hypothesis. It just lost.
5. **Design the experiment that kills at least one.** Not the one that supports your favourite. The 1.75″ vs 0.87″ split of §5 is what this looks like when it is done right: two theories, two numbers, one measurement, and the measurement had to land somewhere.
6. **Run it and publish either way.** OPERA published an anomaly it did not believe, then published its own refutation. Both were correct scientific acts. The anomaly's death was not a failure of the method; it *was* the method.

The residual that survives step 2 is the most valuable object in science, and it is almost always found by someone who was annoyed rather than someone who was inspired. Penzias and Wilson were not looking for the origin of the universe; they were trying to fix a hiss. The CMB is now measured at 2.72548 ± 0.00057 K (Fixsen 2009, *ApJ* 707:916) — the anomaly became one of the most precise numbers in cosmology. That trajectory, nuisance → residual → characterized anomaly → discriminating test → precision measurement, is the shape of new science. Learn to recognise it at stage one.

## 12. Nature as authority — stated precisely, and its mandatory counterweight

Nature is the authority for exactly one reason, and it is not a mystical one: **nature has already run the experiment.** A very long parallel search under real physical constraints, in which the failures were deleted. Convergent evolution — independent lineages arriving at the same solution — is evidence of a constraint-optimum, because the same answer was found repeatedly by searches that did not communicate.

The counterweight is not optional; without it the doctrine collapses into just-so storytelling. Gould & Lewontin (1979, *Proc. R. Soc. Lond. B* 205(1161):581–598) named the failure: not every trait is an adaptation. Phylogenetic inertia, drift, developmental constraint, pleiotropy, and historical contingency all produce features that are not optimal solutions to anything. Nature is full of frozen accidents — the vertebrate retina's inverted wiring, the recurrent laryngeal nerve's detour around the aorta. **Therefore "nature does it this way" is a hypothesis generator, never a proof**, and the biomimetic design must still beat the tuned baseline of §6 or be recorded NEGATIVE.

The discipline of separating the earned from the unearned, with respect and with the receipt, is worked in full in NA-01/NA-02 and summarized here by its canonical pair. The golden angle in phyllotaxis, ≈137.5°, is **earned**: Douady & Couder (1992, *Phys. Rev. Lett.* 68:2098–2101) reproduced Fibonacci phyllotactic order in a physical ferrofluid-droplet experiment and in numerical simulation, from simple repulsion dynamics plus a growth rate — the convergence to the golden mean falls out of the system's avoidance of rational (periodic) organization. No mysticism required, and a real mechanism supplied. "The golden ratio is a universal design law of nature" is **not** earned: unfalsifiable as stated, cherry-picked in practice, and recorded INADMISSIBLE below. Honour the first; fence the second; never mock the person who asked.

---

## The numbers (the ratio/frequency table)

| symbol | value | units | scope | class | source | falsifier |
|---|---|---|---|---|---|---|
| FPR₄ | 60.7 | % (at p<.05) | 15,000 simulated samples; 2-condition design, 20 obs/cell, 4 combined researcher DFs. Individually: 9.5 / 7.7 / 11.7 / 12.6 % | MODELED | Simmons, Nelson & Simonsohn (2011), *Psych. Sci.* 22(11):1359–1366, Table 1 | Re-run the published simulation under the stated assumptions and obtain a materially different rate |
| r_rep | 36 (vs 97 originals) | % significant at p<.05 | 100 studies, 3 psychology journals, 2008 volumes; does NOT generalize to other fields un-remeasured | OBSERVED-CONTESTED | Open Science Collaboration (2015), *Science* 349:aac4716 | Contested by Gilbert et al. (2016), *Science* 351:1037 (low power + protocol infidelity bias the estimate low); OSC replied same issue. Both carried |
| RR⁺ | 96 vs 44 | % positive results (standard lit. vs Registered Reports) | Sample of standard psychology literature vs published RRs | OBSERVED-CONTESTED | Scheel, Schijen & Lakens (2021), *AMPPS*, doi:10.1177/25152459211007467 | Descriptive gap undisputed; causal attribution to preregistration disputed — RRs differ in topic/design too |
| power_med | 21 | % (median statistical power) | 49 meta-analyses, 730 studies, 2011 neuroscience literature | OBSERVED-CONTESTED | Button et al. (2013), *Nat. Rev. Neurosci.* 14:365–376, doi:10.1038/nrn3475 | Nord et al. (2017), *J. Neurosci.* 37(34):8051–8061 refit with mixture modelling: substantial subfield heterogeneity, not one field-wide median |
| bias_conceal | 41 / 30 / 17 | % OR exaggeration (inadequate / unclear concealment / not double-blind) | 250 trials, 33 meta-analyses, Cochrane Pregnancy & Childbirth Database | OBSERVED-REPLICATED | Schulz et al. (1995), *JAMA* 273(5):408–412, doi:10.1001/jama.273.5.408 | Replicated + scoped by Wood et al. (2008) *BMJ* (1,346 trials) and Savović et al. (2012) *Ann. Intern. Med.* 157(6):429–438 (1,973 trials): ROR 0.69 [0.59–0.82] concealment / 0.75 [0.61–0.93] blinding for SUBJECTIVE outcomes; 0.91 [0.80–1.03] / 1.01 [0.92–1.10] for objective |
| Δ_MM | expected 0.40; observed max 0.02, mean <0.01 | fringes | Michelson interferometer, Cleveland 1887; bounds ether drift < ~1/6 × 30 km/s ≈ <5 km/s | OBSERVED-REPLICATED | Michelson & Morley (1887), *Am. J. Sci.* (3rd ser.) 34:333–345 | Any reproducible fringe displacement at the predicted 0.40 magnitude |
| δ_GR / δ_N | 1.75 / 0.87 | arcsec (deflection at solar limb) | Predictions, not measurements: GR vs Newtonian half-deflection | MODELED | Dyson, Eddington & Davidson (1920), *Phil. Trans. R. Soc. A* 220:291–333, doi:10.1098/rsta.1920.0009 | A measurement excluding both values |
| δ_1919 | Sobral 1.98 ± 0.12; Príncipe 1.61 ± 0.31 | arcsec | 1919 eclipse, 2 sites. Excludes Newtonian (~9.3σ / ~2.4σ — my arithmetic on the published values); does NOT pin GR (Sobral ~1.9σ above 1.75) | OBSERVED-CONTESTED | ibid.; commentary PMC4360090 | The Sobral 16-inch plate set was EXCLUDED as "diffused and apparently out of focus" — a disclosed exclusion travels with this result permanently |
| Δt_OPERA | 60.7 ± 6.9 (stat) ± 7.4 (sys) → 6.5 ± 15 | ns (neutrino early-arrival, 730 km baseline) | (v−c)/c ≈ 2.48 × 10⁻⁵ initially; refuted 2012 | INADMISSIBLE | OPERA Collab. (2011), arXiv:1109.4897; 2012 re-measurement | FAILED: loose GPS fibre connector (~73.2 ns) + master-clock oscillator off 0.124 ppm. Re-measured 6.5 ± 15 ns = consistent with zero. Receipt carried, claim withdrawn |
| Δϖ_Mercury | ~43 | arcsec/century (unexplained perihelion precession) | Residual after Newtonian planetary perturbations; Le Verrier 1859 (38″), Newcomb 1882 (43″) | OBSERVED-REPLICATED | Le Verrier (1859); Newcomb (1882); Einstein (1915/1916) | A Newtonian account (undiscovered mass, oblateness) reproducing the residual without new gravity |
| T_ant | ≈3.5 | K (excess antenna temperature at 4080 Mc/s) | Holmdel horn antenna, 1964–65; survived removal of every known instrumental/atmospheric term, incl. the pigeons | OBSERVED-REPLICATED | Penzias & Wilson (1965), *ApJ* 142:419–421 | An instrumental or local source reproducing the excess |
| T_CMB | 2.72548 ± 0.00057 | K | Present-day CMB monopole temperature | OBSERVED-REPLICATED | Fixsen (2009), *ApJ* 707:916 | A measurement outside the stated interval by a calibrated instrument |
| α_golden | ≈137.5 | degrees (divergence angle) | Phyllotactic order; reproduced in a ferrofluid-droplet physical experiment AND numerical simulation from repulsion + growth rate | OBSERVED-REPLICATED | Douady & Couder (1992), *Phys. Rev. Lett.* 68:2098–2101 | A repulsion-dynamics system at the stated growth parameter failing to converge on the golden mean |
| — | NOT-MEASURED | — | The rate at which strong inference (§2) actually accelerates a field vs conventional practice. Platt asserts it ("perhaps by an order of magnitude"); no controlled measurement is cited here | NOT-MEASURED | — | An empirical study measuring discovery rate against method adherence would fill this row |
| — | NOT-MEASURED | — | The false-positive rate of the ACTUAL published literature (as opposed to Simmons' simulation or Ioannidis' model) | NOT-MEASURED | — | A field-wide audit with a ground-truth set would fill this row |

**Definitional values, deliberately carrying NO evidence class** (this is the point, not an omission): the SI defining constants — Δν_Cs = 9 192 631 770 Hz, c = 299 792 458 m/s, h = 6.626 070 15 × 10⁻³⁴ J·s, e = 1.602 176 634 × 10⁻¹⁹ C, k = 1.380 649 × 10⁻²³ J/K, N_A = 6.022 140 76 × 10²³ mol⁻¹ (BIPM *SI Brochure* 9th ed., 2019; effective 20 May 2019). These are exact by convention. They are not observations of nature and this wing's evidence classes do not apply to them. Know which of your numbers are conventions.

## Falsifier (operable)

This chapter claims that the listed procedure is what distinguishes claims that survive from claims that do not. It is refuted by any of the following:

- A body of claims produced **without** pre-registration, held-once scoring, tuned baselines, and collapsing discriminators that replicates at a rate indistinguishable from a matched body produced **with** them. (Scheel et al. 2021's 96%/44% gap is the current evidence against this; a well-powered study showing no gap under matched topics/designs would falsify the section.)
- A demonstration that severity (§4) is not discriminating — i.e. that tests with low capability of detecting a false claim pass true and false claims at materially different rates.
- Any number in the table above traced to a source that does not contain it, or to no source at all.
- Any sentence in this chapter that lets a citation in this wing imply a UNI ledger rung.

## Recorded INADMISSIBLE / NEGATIVE (first-class, inline)

- **OPERA superluminal neutrinos (2011).** INADMISSIBLE — FAILED observation. 60.7 ns early arrival traced to a loose GPS fibre connector (~73.2 ns) and a 0.124 ppm master-clock oscillator offset; re-measured at 6.5 ± 15 ns, consistent with zero. Recorded with the receipt, not mocked: the collaboration published the anomaly *with* its error budget, declined to interpret it, and published its own refutation. This is the method working, not failing.
- **"The golden ratio is a universal design law of nature."** INADMISSIBLE as stated — unfalsifiable (no observation is specified that would refute it) and cherry-picked in practice. The measured golden angle in phyllotaxis (≈137.5°) is a separate, EARNED claim with a physical mechanism (Douady & Couder 1992). Honour the first; do not let it launder the second.
- **432 Hz tuning as physics or biology.** INADMISSIBLE — no mechanism, no falsifier as stated. May be recorded as an HONEST/cultural signal; never as a TRUE/measured one, and the two stores never merge.
- **Chakra-frequency tables.** INADMISSIBLE as physics. Recordable as HONEST/cultural signal only. The Schumann resonance (~7.83 Hz) IS a real measured Earth–ionosphere cavity resonance and belongs in a different column entirely from the human-health claims attached to it, which are a separate and unearned claim.
- **Vulcan (the intra-Mercurial planet).** NEGATIVE, and a good hypothesis. It made a risky prediction, the prediction failed, and it died on schedule. Recorded to show that a losing hypothesis in a K≥2 set is a *contribution*, not an embarrassment.
- **NEGATIVE carried against §12:** the adaptationist reading of nature is bounded by Gould & Lewontin (1979). Convergence is evidence of a constraint-optimum; a single trait's existence is evidence of nothing. Any nature-derived design in this corpus that has not beaten a tuned baseline is recorded NEGATIVE regardless of how elegant its biological precedent is.

## HONEST FENCE — OBSERVED-REPLICATED

The chapter's *methodological* content (blinding/concealment bias magnitudes, the replication shortfall, the flexibility-inflates-false-positives result, the negative-result exemplars) rests on measured, independently replicated literature, cited above with ranges and falsifiers. Two rows are explicitly OBSERVED-CONTESTED and carry both positions (OSC 2015 vs Gilbert et al. 2016; Button et al. 2013 vs Nord et al. 2017). Two rows are MODELED and fenced by their assumptions (Simmons' simulation; Ioannidis' PPV model). Two rows are NOT-MEASURED and left empty rather than filled. One row is INADMISSIBLE and carried with its receipt.

## Not claimed

- **Not claimed:** that following this checklist produces truth. It produces claims that can be killed, and a record of which survived. That is all it produces, and it is enough.
- **Not claimed:** any UNI capability, rung, or gate. No citation in this chapter raises anything in `CLAIM-LEDGER.md`. M2 and M7 are cited as method — they are the repo's own governance rules, class `method`, and referencing them here asserts no result. **A nature citation is never a UNI gate.**
- **Not claimed:** that nature's solutions are optimal, or that "nature does it this way" is an argument. §12's counterweight is binding: it is a hypothesis generator, and the tuned-baseline gate of §6 is where it earns or dies.
- **Not claimed:** that the replication-crisis figures generalize beyond their measured scopes. 36% is 100 studies in three psychology journals; 21% is 49 neuroscience meta-analyses; 41/30/17% is one obstetric trial database, subsequently scoped to subjective outcomes. Field-wide extrapolation from any of them is exactly the error this chapter is about.
- **Not claimed:** that Platt's asserted order-of-magnitude speedup from strong inference has been measured. It has not — recorded NOT-MEASURED above. The procedure is recommended on its logic and on the survival record of the fields that use it, not on a controlled trial of methodology, which does not exist.
- **Permanent open question (QUAESTIO-APERTA):** "the next evolution beyond human" is not a target, milestone, or deliverable of this or any chapter. It is an open question and is never planned toward.
- **Fences engaged:** the word `proven` is reserved for the UNI ledger's own 4-value fence and appears in this chapter only inside a quotation (Platt quoting Popper: "there is no such thing as proof in science"). SIGNUM SIGNUM MANET is enforced structurally: measured values live in the table, interpretations live in the prose, and the 1919 sigma computations are labelled as my arithmetic on published values rather than as published results.
