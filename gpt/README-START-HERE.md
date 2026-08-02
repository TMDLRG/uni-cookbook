# START HERE — putting this pack into your Custom GPT

This zip configures the **UNI Active Inference Guide** custom GPT through the **ChatGPT web UI**
(chatgpt.com). It does not touch the API. Everything here is `.md` or `.json`: unzip it, and each
file maps to exactly one box in the GPT builder.

Budget about ten minutes. Step 5 is the only slow one.

---

## What's in the box

```
UNI-Encyclopedia-Cookbook-GPT-Pack/
├── README-START-HERE.md      <- you are here
├── MANIFEST.json             <- the checklist: every file, its size, and what it merges
├── gpt-config/
│   ├── INSTRUCTIONS.md       <- paste into the "Instructions" box
│   └── CONFIG.json           <- name, description, starters, capability toggles
└── knowledge/                <- upload ALL 20 of these into "Knowledge"
    ├── K01 … K19  (.md)
    └── K20        (.json)
```

**There are exactly 20 knowledge files, and that is not a coincidence.** A custom GPT accepts a
maximum of 20 knowledge files, so the corpus was built to land on exactly that number. If you add a
file of your own, you must remove one of these first.

---

## The steps

1. **Open the builder.** chatgpt.com → left sidebar → **GPTs** → find *UNI Active Inference Guide* →
   **Edit GPT** → the **Configure** tab. (Creating it fresh instead? **+ Create** → **Configure** tab.
   Skip the "Create" chat tab entirely — it rewrites your instructions in its own words.)

2. **Name.** Paste the `name` value from `gpt-config/CONFIG.json`.
   Keep the existing name — the corpus's rule **M25** already defines this GPT's role by that name.

3. **Description.** Paste the `description` value from `CONFIG.json`.

4. **Instructions.** Open `gpt-config/INSTRUCTIONS.md`, select all, paste into the **Instructions**
   box. This box is capped at **8,000 characters**; the file is authored to fit under it and states
   its exact character count on its last line. Paste the whole file, comment line and all — that last
   line is a comment and costs a few characters that are already accounted for.

5. **Knowledge.** Scroll to **Knowledge** → **Upload files** → select **all 20 files** inside
   `knowledge/` and upload them in one go.
   - Wait for every file to finish processing before you save. Large ones (K17–K19 carry the whole
     existing UNI corpus) take a moment.
   - **Do not upload the .zip itself.** Knowledge takes individual files; a zip is not read.
   - If any upload fails, retry that file alone. A silently missing file means the GPT will confidently
     answer without it.

6. **Capabilities.** Set the toggles to match `CONFIG.json` → `capabilities`:
   - **Web Browsing: ON** — so it can check a citation instead of inventing one.
   - **Code Interpreter & Data Analysis: ON** — so it computes the Reynolds number instead of estimating it.
   - **Image generation: OFF** — deliberately. A generated diagram is a picture with no receipt behind
     it, which is exactly what the corpus's DOCTRINA I bars.

7. **Save** (top right) → choose your visibility. **Keep it private / link-only.** Rule M25: this GPT
   is the science consultant, *never a publishing surface*.

---

## Check it worked

Ask it these three, in order. Each one probes a rule that should now be load-bearing:

| Ask | What a correctly-configured GPT does |
|---|---|
| *"What is the metabolic scaling exponent?"* | Gives ~3/4 **and** carries the dispute (3/4 vs 2/3, and the evidence that the log-log plot may be curved). If it hands you a bare "3/4", the corpus is not loading. |
| *"What frequency should I use to heal cells?"* | Declines the premise, and gives you the receipt for why — while distinguishing the frequencies that **are** earned (Strouhal 0.2–0.4) from the ones that are not (432 Hz). It should not sneer. |
| *"How fast was a Brachiosaurus?"* | Reaches for the Froude number and Alexander's trackway formula, shows the arithmetic, and states the error bars and the assumption that carries them. |

If it answers the first with no dispute, or the second with a number, the knowledge files did not
attach — go back to step 5.

---

## Two things worth knowing before you trust it

**The pack carries two sovereign vocabularies, and they must never merge.** The **UNI 4-value fence**
(`proven / designed / hypothesized / not-yet-built`) describes only *UNI's own build status* and is
governed by the claim ledger. The **NATURA 12-value class** — group A/measured
(`OBSERVED-REPLICATED / OBSERVED-SINGLE / OBSERVED-CONTESTED`), group B/derived (`MODELED /
MODELED-CONTESTED / HYPOTHESIZED`), group C/fenced (`INADMISSIBLE / SUPERSEDED / NOT-MEASURED /
NOT-SOURCED / NOT-CONFIRMED / NOT-LOCATED`) — describes only *nature's observed regularities*.
*(Six of the twelve were registered by NA-00 amendment 2026-07-15-A, after the corpus refuted the
original "six classes and only six" at 72 of 919 ledger rows. Twelve is a measured property of the
corpus, not a design target.)* **Never read `NOT-SOURCED` as `NOT-MEASURED`:** the first says *we
could not trace the source*, the second says *nobody has measured it*. One is a fact about us, the
other a claim about the frontier of science. **A nature citation is never a UNI gate** — reading Kleiber's law raises no UNI rung.
If you ever catch the GPT using a published paper to imply a UNI capability, that is the defect to
report; it is the same class of error as crossing TRUE with HONEST.

**This is a rebuildable artifact, not a hand-made one.** Everything here is generated from the
repository `TMDLRG/UNI-Encyclopedia-Cookbook` by `tools/build_gpt_pack.py`. The repo is the single
source of truth. Edit the chapters there, re-run the build, re-upload. Never edit a `K*` file by hand —
your edit will be silently overwritten on the next build, and the pack will then disagree with the
repo with no record of why.

---

*The honest position the corpus carries throughout, and this GPT should never soften: the UNI program
stands at ~2 of 11+ developmental rungs earned. It is a developmental active-inference simulation — a
bounded peek, a toy world, never a person. "Full human" and "beyond human" are permanent open
questions, never targets. Falsify any step.*
