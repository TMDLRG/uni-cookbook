# UNI Encyclopedia & Cookbook

Two books and a build, in one repository.

- **`encyclopedia/`** — a science-honest reference work about the UNI program: what it has actually
  built, at what evidence class, with every negative published and every falsifier live.
- **`cookbook/`** — the buildable recipes: the L0–L12 developmental ladder, and now the NATURA
  recipes (build DNA, a sperm, an ant colony, a dinosaur, a whale, a bat, a rock, water, air, a
  star, a human — and the open question beyond).
- **`gpt/`** — a 20-file pack that loads this corpus into the **UNI Active Inference Guide** custom
  GPT, built reproducibly from the two books by `tools/build_gpt_pack.py`.

**The honest position, printed here and never softened: ~2 of 11+ developmental rungs earned.** The
UNI program is a developmental active-inference *simulation* — a bounded peek, a toy world, never a
person. "Full human" and "beyond human" are permanent open questions, never targets.

---

## The two sovereign ledgers (the rule that organizes everything)

This repository carries **two** evidence vocabularies. They are sovereign, and merging them is the
cardinal error.

| | **The UNI fence** | **The NATURA class** |
|---|---|---|
| **Describes** | UNI's own build status | Nature's observed regularities |
| **Governed by** | [`encyclopedia/CLAIM-LEDGER.md`](encyclopedia/CLAIM-LEDGER.md) | [`encyclopedia/NATURE-LEDGER.md`](encyclopedia/NATURE-LEDGER.md) |
| **Values** | `proven` · `designed` · `hypothesized` · `not-yet-built` | `OBSERVED-REPLICATED` · `OBSERVED-CONTESTED` · `MODELED` · `HYPOTHESIZED` · `INADMISSIBLE` · `NOT-MEASURED` |
| **Rests on** | held, sealed, UNI-signed gates | published, replicated literature |

**A nature citation is never a UNI gate.** Reading Kleiber's law raises no UNI rung. Citing published
biology makes no UNI claim `proven`. This is the same discipline the repo already applies to
UNI.OS ("substrate evidence is never general-AIF evidence"). Cross-reference the two ledgers by
explicit link only — never by merge.

Where any prose disagrees with its ledger, **the ledger wins and the prose is wrong.**

---

## Map

| Where | What |
|---|---|
| [`encyclopedia/00-INDEX.md`](encyclopedia/00-INDEX.md) | the reference work — wings E (evidence), S (the L0–L12 science ladder), N (meaning), M (movement), μ (method) |
| [`encyclopedia/wing-NATURA/`](encyclopedia/wing-NATURA/) | **the nature wing** — nature as the authority, the one loop, how to make new science, mind/body/world, the ratios, the frequencies, the dimensionless numbers, cell-level design, morphogenesis, the scale ladder |
| [`cookbook/00-INDEX.md`](cookbook/00-INDEX.md) | the recipes — the kitchen rules, the pantry, and L0–L12 |
| [`cookbook/recipes-natura/`](cookbook/recipes-natura/) | **the build catalog** — rocks, water, air, stars, DNA, sperm, ants, dinosaurs, whales, bats, humans, and the open question beyond |
| [`encyclopedia/CLAIM-LEDGER.md`](encyclopedia/CLAIM-LEDGER.md) | the single source of truth for UNI's claims |
| [`encyclopedia/NATURE-LEDGER.md`](encyclopedia/NATURE-LEDGER.md) | the sovereign ledger for nature's measured regularities |
| [`gpt/`](gpt/) | the custom-GPT pack + [`gpt/README-START-HERE.md`](gpt/README-START-HERE.md) |
| [`tools/build_gpt_pack.py`](tools/build_gpt_pack.py) | the reproducible build |

---

## Nature as the authority — stated precisely

The doctrine is defensible in exactly one form, and the corpus holds it there:

> Nature is the authority because it is the only system that has **already run the experiment** — a
> very long parallel search under real physical constraints, in which the failures were deleted.
> Convergent evolution is **evidence of a constraint-optimum**.

And it is only honest with its counterweight, which travels with it everywhere:

> Not every trait is an adaptation (Gould & Lewontin 1979). Drift, phylogenetic inertia,
> developmental constraint and frozen accidents are real — the vertebrate retina is wired backwards.
> **"Nature does it this way" is a hypothesis generator, never a proof.** The bio-inspired design
> still has to beat a tuned conventional baseline on a pre-registered metric, or it is recorded
> NEGATIVE.

That second paragraph is what separates this from cargo-cult biomimicry.

---

## Rebuilding the GPT pack

```bash
python tools/build_gpt_pack.py
```

The build merges the corpus into exactly 20 knowledge files (the OpenAI hard cap), validates the
JSON, gates the Instructions file against the 8,000-character limit, writes `gpt/MANIFEST.json`, and
zips to `dist/`. It fails loudly rather than truncating silently.

Never hand-edit a `gpt/knowledge/K*` file: it is a build artifact, and your edit is overwritten on
the next build with no record of why. Edit the chapter in `encyclopedia/` or `cookbook/` and rebuild.

---

## The honesty rail (binding on every file here)

- **RES IPSAE, NON SIMULACRA.** No fabricated numbers. Every value carries a real citation, or it is
  written `NOT-MEASURED`. There is no third state.
- Every number carries **units + the scope it holds over + its evidence class + its source + its
  falsifier**. A number without units or scope is a defect.
- Banned in author voice (quote-with-attribution only): *verified, secure, guaranteed, certified,
  self-aware, conscious, AGI, intelligent*. `proven` is reserved for UNI-ledger status and never
  describes nature's science.
- **TRUE** signals (falsifiable, reproducible, recalibratable) and **HONEST** signals (lived
  experience, never calibrated) stay sovereign and are never merged.
- Contested values are carried **with the dispute**, both positions named — never silently resolved.
- The failures are published, at the top, not buried. **Falsify any step.**
