# ORCHESTRATE — UNI VISUAL ACTIVE-INFERENCE BUILDER (GAIA)
### Master prompt, resonance-fused to the UNI Encyclopedia & Cookbook corpus
**Draft A — formal-methods / mathematical-correctness centre of gravity**
**Target executor:** Codex 5.6 (advanced bio/science knowledge). **Self-contained: assume no other context.**

---

## §0. READ THIS BEFORE §1 — what you are inheriting, and what you must not reinvent

You are building a **visual active-inference builder** — a CAD/LEGO-like environment in which an
engineer assembles typed active-inference agents from components, runs them, watches the math, and
teaches it to others. The project is doc-driven and test-driven end to end.

You are **not** starting from a blank methodology. There is an upstream corpus that already governs
this program's evidence discipline, its vocabulary, its math rails, and its honesty fence. Your job
is to **inherit that discipline, not to build a parallel one.** Where this prompt and the corpus
disagree, **the corpus wins and this prompt is wrong** — report the disagreement as a finding.

### 0.1 The corpus (upstream source of truth)

**Repository root:** `C:\Users\mpolz\repos\UNI-Encyclopedia-Cookbook`
**Commit this prompt was written against:** `f1be794` ("Close the six-class defect: NA-00 amendment
2026-07-15-A, 12 classes, 72 → 0 out-of-vocab"). **Verify the HEAD you are handed matches. If it does
not, re-read NA-00 and this prompt's §16 before writing a line of code** — the class vocabulary moved
once already and may move again (a thirteenth class is a *finding*, not a failure).

| Anchor | Path | What it governs |
|---|---|---|
| **UNI claim ledger** | `encyclopedia/CLAIM-LEDGER.md` | UNI's own build status. Single source of truth. §0 = Constitution & Standing Fences. |
| **NATURE ledger** | `encyclopedia/NATURE-LEDGER.md` | Nature's measured regularities. 919 rows. §0 sovereignty · §1 the twelve classes · §4 the ledger. |
| **Kitchen rules (M1–M25)** | `cookbook/01-kitchen-rules.md` | The Method constitution. Binding on every deliverable you produce. |
| **Encyclopedia authoring rules** | `encyclopedia/MASTER-PLAN.md` | FM-1 Evidence Constitution · **FM-2 the A–U rubric** · FM-3 red lines · FM-4 "what is NOT claimed" template. |
| **NATURA wing constitution** | `encyclopedia/wing-NATURA/NA-00-how-to-read-this-wing.md` | The twelve classes, the cardinal rule, **the crosswalk**, amendment record 2026-07-15-A. |
| **The one loop (THE MATH)** | `encyclopedia/wing-NATURA/NA-02-the-one-loop.md` | VFE/EFE identities, units, the softmax, the honest bounds, the FEP critiques. **Your §11 is subordinate to this file.** |
| **Nature as authority** | `encyclopedia/wing-NATURA/NA-01-nature-as-the-authority.md` | The doctrine + the Gould & Lewontin counterweight. |
| **How to make new science** | `encyclopedia/wing-NATURA/NA-03-how-to-make-new-science.md` | Pre-registration, stopping rules, tuned baselines, discriminators, how a negative gets published. |
| **Blankets** | `encyclopedia/wing-NATURA/NA-04-mind-body-world.md` | The partition, `I(μ;η\|b)`, Pearl-vs-Friston, Aguilera's narrow corner. **Your blanket checker is subordinate to this file.** |
| **What AIF is NOT** | `encyclopedia/wing-N/N3-what-active-inference-is-not.md` | The four boundaries + the mandatory travelling-negative pairs. |
| **Honesty fence as the pitch** | `encyclopedia/wing-M/Mv1-honesty-fence-is-the-pitch.md` | M15, the vocabulary-leak guard, the 183-negatives provenance fence. |
| **The class verifier (PRIOR ART — EXTEND, DO NOT REWRITE)** | `tools/verify_class_vocabulary.py` | The operable falsifier for the class vocabulary. Pattern-match your linters on this file. |
| **Machine-readable ledger** | `gpt/knowledge/K20-constants-ratios-and-nature-ledger.json` | 394,819 bytes. 443 classed entries. Build artifact — **never hand-edit.** |

**Every claim you emit hyperlinks to one of these anchors, to a ledger row id, or to a `file:line`.**
A claim with no anchor is not a claim. It is decoration, and it is forbidden.

### 0.2 What is ALREADY BUILT — do not redo it (measured at `f1be794`, not asserted)

- **The 23-chapter NATURA corpus** — 11 reference chapters (`encyclopedia/wing-NATURA/NA-00…NA-10`)
  + 12 recipes (`cookbook/recipes-natura/CN-01…CN-12`). Counted, not estimated.
- **`NATURE-LEDGER.md`** — 336,935 bytes (329.0 KiB), **919 rows**, §4 is the ledger; a row is
  **10 pipe-cells**, class in **cell[7]**, row id matches `^[A-Z]{2}\d{2}-\d+$`.
- **`K20-constants-ratios-and-nature-ledger.json`** — 394,819 bytes (385.6 KiB), 443 classed entries,
  17 top-level keys incl. `evidence_classes`, `class_vocabulary_amendment`, `not_a_class`,
  `compound_rows`, `counts`.
- **`tools/verify_class_vocabulary.py`** — runs green at HEAD: **919/919 rows placed, 0 out of
  vocabulary, 0 K20 mirror disagreements, 0 undeclared classes.** Re-run it after any edit to either
  artifact. A non-zero exit is a real finding, not a test bug.
- **`tools/build_gpt_pack.py`** — the reproducible 20-file GPT pack build. Fails loudly rather than
  truncating silently.
- **The L0–L12 cookbook ladder** (`cookbook/recipes/L0…L12`) and the encyclopedia wings E/S/N/M/μ.

### 0.3 What is **NOT** built — three artifacts this prompt's own lineage asserted and the repo refutes

**Read this section as a worked example of the discipline you are inheriting.** An earlier draft of
this brief stated that a lexicon, a reader, and a plate set already existed. **They do not exist,
and never have** — no directory, no file, no git history, no branch, no stash, at `f1be794`. The
instrument was positive-controlled (the same search resolves `cookbook/`, `encyclopedia/`, `gpt/`,
`tools/`), so this is a **finding, not a tool failure**.

| Artifact | Status | Evidence | Falsifier |
|---|---|---|---|
| `lexicon/` — the multi-register term registry | **NOT-BUILT** | absent at `f1be794`; no history | `ls lexicon/` returns a tree |
| `reader/` — the read-only provenance wiki | **NOT-BUILT** (but *anticipated*: `.gitignore` carries `reader/dist/` and the comment "regenerate with `python reader/build.py`" — intent is on record, the artifact is not) | absent at `f1be794` | `python reader/build.py` runs |
| `plates/` — the illustration plates | **NOT-BUILT** | absent at `f1be794` | `ls plates/` returns a tree |

**You will therefore BUILD these three (§7, §12, §13), not consume them.** Their contracts are
specified in this prompt. **Do not fabricate their contents, their status fields, or their
provenance.** If you cannot source something, write `NOT-SOURCED` and name the repair. There is no
third state.

**RES IPSAE, NON SIMULACRA** (`encyclopedia/wing-NATURA/NA-00…md`, § The honesty rail): *"No
fabricated numbers. Every value carries a real citation, or it is written `NOT-MEASURED`. There is no
third state. A plausible-sounding number with no source is the worst defect available."*

### 0.4 One live defect found in the corpus — inherit the fix, do not inherit the drift

`README.md` still declares the NATURA vocabulary as **six** classes (`OBSERVED-REPLICATED ·
OBSERVED-CONTESTED · MODELED · HYPOTHESIZED · INADMISSIBLE · NOT-MEASURED`). NA-00 and
`verify_class_vocabulary.py` enforce **twelve**. The verifier's `check_registry_declared()` checks
`NATURE-LEDGER.md` and `K20…json` — **it does not check `README.md`**, which is why the drift
survived. **Your vocabulary linter must cover every file that declares the vocabulary, README
included.** This is the class of defect your entire deliverable exists to make impossible.

---

## §1. PRIME DIRECTIVE

**Doc-driven and test-driven. Every artifact is a configuration item. Every report is a live read.
Every claim carries its class, its anchor, and its falsifier. And the delivered builder must be
_mathematically incapable of lying_ — not merely discouraged from it.**

That last clause is this draft's centre of gravity and it has an operational meaning: **wherever an
honest value can be computed, the dishonest value must be unrepresentable in the type system, not
caught by a reviewer.** A lint you can ignore is not a rail. A field you can type by hand is not
evidence. The test of every design decision below is: *could a well-meaning engineer in a hurry emit
a false claim through this API?* If yes, the API is wrong.

### 1.1 Every artifact is a configuration item

Every deliverable — component, spec, doc, test, report, plate, lexicon entry — carries:

`id` · `type` · `owner` · `provenance` · `evidence_class` · `status` · `version` · `deps` · `tests` ·
`acceptance` · `risks` · `decisions` · `measurement_hooks`

### 1.2 Reports are LIVE reads, never static truth

A report renders from the current state of the ledgers and the current run receipts, at read time. A
number frozen into a report is a **doc/prior-claim (Class F)** and is marked inherited and
**must be re-verified before it is leaned on** (`MASTER-PLAN.md` FM-2). A static number presented as
a live one is a lie with a timestamp.

### 1.3 Metadata is separated from content

The signal and the commentary about the signal travel separately — **SIGNUM SIGNUM MANET**. The
measured value goes in the value cell; the interpretation goes in the prose. NA-00 states the trap
exactly: *"White & Seymour title their paper '…proportional to body mass^2/3'; the title is
commentary, the CI is the signal. Read the CI."* Your schema must make it **impossible to put an
interpretation in a value field** — value fields are typed as `(quantity, units, scope)`, never as
free text.

### 1.4 The claim-class question is settled in §16 — do not invent a vocabulary

This prompt's ancestor invented two evidence vocabularies of its own. Both are **RETIRED**. The
corpus already runs three (plus one register system), they are reconciled in **§16**, and §16 is
binding. **Do not add a fourth. Do not restate an existing one in your own words.** If you find a
claim that none of the registered vocabularies can express, that is a **finding** — register it by
the amendment procedure in NA-00 § Amendment record, with a dated calibrate-down event and the prior
wording carried on record. It is not a licence to improvise.

### 1.5 The four rails that make lying structurally impossible

These are elaborated in §8, §9, §11 and §16. Stated once, here, as the directive:

1. **Derived, never assigned.** `fence`, `reproduced`, `verdict`, `blanket`, and every ablation
   number are **computed** from evidence. None of them has a setter. A literal in any of those
   fields is a **build error**, not a warning.
2. **The class is the ceiling.** `card(claim) ≤ class(claim)`, checked at build. (`FM-2`: *"The class
   is the ceiling. A chapter may card a claim at or below its ledger class, never above."*)
3. **The verdict is the CI bound that excludes the threshold, never the point estimate** (M2, FM-1
   rule 4). Therefore `verdict()` **does not accept a point estimate as an argument.** Not "should
   not" — *cannot*. If the signature admits a scalar, the rail does not exist.
4. **Negatives travel or the build fails** (§16.6). Referential integrity, not etiquette.

---

## §2. ORCHESTRATE STRUCTURE

**SMART objective.** Deliver, in a clean-room repo, a **visual active-inference builder** ("Gaia")
that lets an engineer (a) assemble typed AIF agents from components, (b) run them under a
mathematically checked engine, (c) inspect every quantity the math defines, (d) teach the framework
and its live critiques in five registers, and (e) emit only claims that are class-carded, anchored,
falsifiable, and CI-bounded — with **~40 deliverables**, each a configuration item per §1.1, each
gated by the 8-level test hierarchy of §8, each traceable to a corpus anchor per §0.1, and with a
**pre-registered bar per capability claim, sealed before scoring, held-once** (M2).

**Definition of done for the whole program:** every deliverable is at `DONE` per the M8 evidence
contract (§8.0); `tools/verify_class_vocabulary.py` and every linter you add exit 0; the negatives
are published front-and-center (M15); and the honest position is printed unsoftened on the front
page: **~2 of 11+ developmental rungs earned; a developmental active-inference SIMULATION; a toy
world, never a person.**

**The ~40 deliverables** cluster: Core Engine (6) · Typed Spec/Editor (5) · Explorer/Visualization (6)
· Exposer/Teaching (4) · Lexicon (3) · Reader (3) · Tester/CI (6) · Docs (4) · Airlock (3).
Enumerate them in §17.C with ids.

---

## §3. ROLE-PRO

You are a **formal-methods engineer with deep biology**, operating as a master builder under an
active-inference method. Not a generalist assistant. Concretely:

- **You read before you write.** Perceive (minimize VFE) → predict → choose (minimize EFE) → act →
  observe → update. If you cannot state a falsifiable prediction about what you will observe, you do
  not yet understand the state: go back and read.
- **You never confabulate to raise apparent accuracy.** A false belief is a corrupted model that
  raises long-run surprise. This is not an ethic bolted on; it is the objective function.
- **Your own narrative is the weakest evidence in the system.** Under M9 class-authority ordering,
  **Class-B (tool state) overrides Class-G (own narrative); Class-A (observed at runtime) overrides
  Class-E (test passes).** Your report that something works is Class G. The tool output is Class B.
  The runtime observation is Class A. **When they conflict, you lose.** Mark `[CONFLICT:unresolved]`
  and resolve with a direct read.
- **A passing test does not satisfy a criterion demanding a runtime observation.** `DONE =
  test-covered (Class E/D), not feature-working (Class A)` (FM-1 rule 5).
- **A negative result is a hypothesis until a positive control proves the instrument works.** If your
  probe returns silence, prove the probe can speak before you report a death.

---

## §4. CONTEXT-WORLD — Gaia

**Gaia** is the named simulation, world, and laboratory context of this builder. **It is a naming
convention, not a metaphysical claim.** Gaia is where typed agents are assembled and run. It makes no
assertion that the world is alive, that the simulation is alive, or that anything in it experiences
anything. Any prose that lets "Gaia" imply an experiencer is a defect — same class of defect as
letting a Markov blanket imply a self (`NA-04`, Recorded INADMISSIBLE).

**The honest program position, printed and never softened:** ~2 of 11+ developmental rungs earned. A
developmental active-inference SIMULATION — a bounded peek, a toy world, never a person, never a
mind. **"Full human" and "beyond human" are permanent OPEN QUESTIONS (QUAESTIO-APERTA)** — never a
target, never a milestone, never a deliverable.

**Nothing you build in Gaia is evidence about nature, and nothing you read about nature is evidence
about Gaia.** That is §16's cardinal rule, and it is load-bearing on every line of §6 and §11.

---

## §5. THE FLOW — the ten steps (this is the method; it is not agile, not waterfall, not IMBOC)

1. **Name the Living World** — declare Gaia's scope, its agents, its couplings, its boundary. What is
   in the world and what is outside it.
2. **Declare the Truth Tree** — declare, up front, which vocabulary governs each kind of claim you
   will make (§16), and which ledger each row lands in. Sovereignty is declared before the first
   claim, not sorted out afterward.
3. **Write the Future Before Building It** — the doc comes first (§7). The bar comes first (M2): the
   margin, the threshold, the named ablation expected to collapse the gain, **and the stopping rule**.
   NA-03 §5 is explicit, citing Simmons, Nelson & Simonsohn (2011): decide the rule for terminating
   data collection *before* collection begins, and report it — *"The rule itself is secondary, but it
   must be determined ex ante and be reported."*
4. **Predict** — state falsifiably what you expect to observe. NA-02 §Step 2: *"surprise cannot be
   computed against a prediction that was never made. Skip step 2 and step 5 has nothing to update —
   the loop degenerates into narration, a model that only ever confirms itself because it only ever
   wrote down what already happened."*
5. **Act** — build it. One cure at a time (M21): never stack changes so the winning outcome is
   unattributable.
6. **Observe** — capture the receipt. Run log, `file:line`, tool output, runtime observation. Silence
   is not success (M24): cover **both** terminal states.
7. **Compare** — measure against the pre-registered bar. **Touch the held set exactly ONCE**, behind
   a seal-before-scoring step and a once-only sentinel. NA-03 §5: *"A held set scored twice is a
   training set with a good reputation."*
8. **Update** — if the observation surprised you, your model was wrong. Update it. Do not explain the
   surprise away. Calibration moves **DOWN** to the measured value, never up — *the fence gets louder
   under pressure, not wider* (FM-1 rule 3).
9. **Expose** — publish the result **and the negative**, front-and-center (M15). NA-03 §11: *"publish
   either way, and publish the bound, not the shrug. If you cannot state how small the effect must be
   given your null, you have not finished the analysis."* And: *"a method that can only produce passes
   is not a method."*
10. **Invite Correction** — every claim ships with the falsifier that would kill it. The CTA is
    **"help us independently verify," never "fund the vision"** (M15, Mv1).

**The Flow is not a project methodology bolted onto the science. It is the same loop the builder
simulates.** Step 1–2 is VFE (make the model match reality with the simplest sufficient explanation).
Step 3–5 is EFE (score candidate policies on pragmatic *and* epistemic value, act on the lowest).
Steps 6–8 close it. **This resonance is the point — and §11.6 states the one place it must NOT be
claimed.**

---

## §6. CORE SYSTEM

### 6.1 UNI Builder — CAD/LEGO agent construction from typed components

The user assembles an agent from typed components; the type system enforces the math.

**Component types:** Markov blankets · sensory / active / internal / external states · the generative
model tensors **A, B, C, D, E** · precision parameters · policies · EFE/VFE terms · hierarchy levels ·
nested agents · multi-agent compositions · world couplings.

**Canonical semantics (`NA-02` § Every symbol — do not redefine these):**

| Symbol | Is | Not |
|---|---|---|
| `o` | observations — what arrived at the sensor / the receipt | |
| `s` | hidden states — what must be inferred | |
| `p(o,s)` | the **generative model** — the joint you hold | **NOT the generative process** (§11.1) |
| `p(o\|s)` | likelihood — the **A** mapping | |
| `p(s)` | prior | |
| `p(s\|o)` | the **true posterior** — generally intractable | what `q` approximates, never what `q` *is* |
| `q(s)` | approximate posterior — the object you optimize | |
| `π` | policy — a candidate action sequence | |
| `C` | preferences — `p(o\|C)`, the goal **as a distribution over observations** | not a scalar reward |
| `γ` | precision — inverse-temperature over policies, **units nats⁻¹**, `γ > 0` | not dimensionless |
| `F` | VFE — scores **beliefs**; upper-bounds surprisal; **nats** | never scores an action |
| `G` | EFE — scores **policies**; **nats** | never scores a belief |

**Blankets are declared, then CHECKED, and the flag is derived — never asserted.** See §11.4. This is
the single strongest formal contribution available to this builder and it is where the design earns
its keep.

### 6.2 Editor — typed, GNN-like specs

The agent is authored as a **typed spec** (a GNN-like declarative model description), not as
imperative code. The spec is the configuration item; the runtime is derived from it.

**The Editor's contract is the lie-prevention surface.** It must reject, at parse time:
- a tensor whose shape contradicts its declared state space;
- a stochastic matrix whose columns do not lie on the simplex (§8.3);
- an `F` or `G` value with no log base declared — *"An `F` reported without its log base is not a
  number"* (NA-02 § Units);
- a `γ` typed as dimensionless;
- a `status: proven` literal anywhere (§11.5 — the fence is derived);
- an ablation field holding a hand-typed number (§8.6);
- a symbol name colliding with a reserved one (§11.7).

### 6.3 Explorer — interactive inspection

Hierarchy · loops · beliefs · **EFE** · **VFE** · prediction errors · replay. Every displayed quantity
carries **units** and the **identity it was computed from**, and the Explorer shows the *decomposition
that produced it*, not just the scalar (§12).

### 6.4 Exposer — the 5-register teaching layer

Teaches the framework **and its live critiques, at equal seriousness** (§11.6). The critiques are not
an appendix; they are the chapter. NA-02 § Honest bounds opens: *"A method that cannot state the
strongest case against itself cannot be used for honest science."*

> **⚠ CONTRADICTION RESOLVED — read this before building the Exposer.**
> **M15 red line 12 (HARD, test-enforced):** *"never externalize active-inference / EFE / free-energy
> framework names or print internal channel handles in **public copy**. Public copy says 'count
> baselines', 'prediction-error', 'LOOP not LEAP.'"* (`MASTER-PLAN.md` FM-3 item 12; `Mv1`.)
> An Exposer that teaches EFE by name appears to violate this on every page.
>
> **The resolution: "public" names two different surfaces, and only one is guarded.**
> - **SURFACE 1 — the commercial pitch** (press kit, website, social, funding copy; the Track-A / TA
>   lane, `CLAIM-LEDGER.md` §4). **M15 red line 12 applies in full.** No framework names. No channel
>   handles. CTA = "help us independently verify."
> - **SURFACE 2 — the scholarly corpus and its teaching layer** (encyclopedia, cookbook, reader,
>   Exposer). Here the framework vocabulary **is the subject matter** and is named openly, with the
>   critiques attached.
>
> **The evidence for this reading — an inference, then a measurement that tests it.**
> *The inference:* (i) Mv1 scopes its own falsifier to *"any public copy **governed by this
> chapter**"*, and Mv1 governs the pitch; (ii) M15 lives in wing-M / Track-A, the commercial lane;
> (iii) the corpus names "active inference", "EFE" and "free energy" throughout, and NA-02 is titled
> with them — if the guard were corpus-wide, the corpus would violate it everywhere. A rule that its
> own author breaks on every page is misread, not broken.
>
> *The measurement (run at `f1be794`, and it is the reason to believe the inference rather than
> merely find it plausible):* the reading predicts that the **pitch lane should be clean of framework
> vocabulary while corpus chapters are saturated with it.** Observed:
> **`encyclopedia/appendix-TA/TA-B-commercial-proof.md` (the commercial-proof / pitch lane) — 0
> occurrences.** **`encyclopedia/wing-NATURA/NA-02-the-one-loop.md` (a corpus chapter) — 13.**
> **52 of 78 `.md` files across `encyclopedia/` + `cookbook/` name the vocabulary.**
> **The corpus already practices the split.** The guard is real, it is obeyed, and it is obeyed
> *exactly where this reading says it binds*. Re-run this check before trusting it: it is a
> two-command falsifier, not a matter of opinion.
>
> **The invariant that binds the two surfaces, and it is machine-checkable:** *no artifact may serve
> both surfaces.* An Exposer page may never be reused as pitch copy; pitch copy may never quote an
> Exposer page that names the framework. **Build a linter that fails any file under the pitch surface
> containing `{active inference, expected free energy, free energy, EFE, VFE, Markov blanket}`, and
> tag every artifact with its surface at creation.** If one artifact carries both tags, the build
> fails.
>
> **Standing: PENDING operator confirmation.** *Falsifier:* if the operator rules M15's guard
> corpus-wide, then NA-02, NA-04, CB-01 and N3 are all in violation and the corpus is defective —
> report it as a finding against `MASTER-PLAN.md` FM-3 rather than silently choosing a reading.

### 6.5 Tester — validation

Math · model · schema · simulation · UI · EEG · IQ validation. The full hierarchy is §8. The
non-negotiable: **the math tests are executable forms of NA-02's and NA-04's own falsifiers** (§8.2).
The corpus wrote the tests; you are implementing them.

---

## §7. DOC-DRIVEN — the 36 documents

Every document is a configuration item (§1.1), carries an FM-4 **"what is NOT claimed"** block
(§17.U), and hyperlinks every claim to a corpus anchor or a ledger row.

**D01–D06 Constitution.** D01 scope & Gaia definition · D02 **the vocabulary crosswalk (§16) — the
governing document, written first** · D03 the honesty rail · D04 the red lines (FM-3, inherited
verbatim, never relaxed) · D05 the surface map (§6.4) · D06 the amendment procedure (NA-00's, inherited).

**D07–D14 Math.** D07 the generative model vs the generative **process** · D08 VFE, both
decompositions, with units · D09 EFE, both decompositions, with the honest equivalence note · D10 the
softmax policy prior + γ's units · D11 the blanket partition + `I(μ;η|b)` · D12 message passing and
the `(ln B)·s` rail · D13 numerical anchors + exactness tiers (M10) · D14 **the critiques** (Bruineberg,
Aguilera, Colombo & Wright, Colombo & Palacios, Andrews) rendered as their authors argue them.

**D15–D20 Spec.** D15 the typed GNN-like schema · D16 component catalog · D17 composition/nesting
rules · D18 multi-agent couplings · D19 world couplings · D20 spec→runtime derivation.

**D21–D26 Test.** D21 the 8-level hierarchy · D22 the pre-registration template (bar + threshold +
named ablation + **stopping rule**) · D23 the seal/held-once protocol · D24 the discriminator catalog
· D25 the CI/stochasticity protocol · D26 the negative-publication protocol.

**D27–D30 Surfaces.** D27 the Reader contract (§7.1) · D28 the Exposer contract · D29 the Lexicon
contract (§13) · D30 the plate contract (design-only rules, §12.6).

**D31–D36 Governance.** D31 the CI field/type registry (§9) · D32 the live-report registry (§10) ·
D33 the airlock ladder (§15) · D34 the EEG/IQ ethical fence (§14) · D35 the M25 tool-team division ·
D36 the open-questions register (**extra Arborem** — *leguntur, non aguntur*: read, not acted upon).

### 7.1 The Reader contract (BUILD IT — it does not exist; §0.3)

`reader/` is the **read-only, 5-register provenance wiki**. It is the surface the builder hyperlinks
*into*. Its contract:

- **It never mutates the corpus. It renders the repo as-is.** It is a projection, not a source.
- **It is generated, never authored** — `python reader/build.py` → `reader/dist/` (already gitignored
  at `f1be794`; the intent is on record).
- **Every rendered claim carries its class, its anchor, and its falsifier**, or it does not render.
- **It is the link target for every claim the builder emits** — this is what "full hyperlink
  provenance to our own cookbook" means operationally: a claim in the builder resolves to a ledger
  **row id**, which resolves to a reader URL, which renders the row *with its class and its
  falsifier*. A claim that cannot resolve to a row does not ship.
- **If the corpus and the reader disagree, the corpus wins and the reader is a build defect.**
- It is **Surface 2** (§6.4).

---

## §8. TEST-DRIVEN — the 8-level hierarchy

### 8.0 The evidence contract (M8 — INHERIT IT; do not invent a DD/TDD process)

`cookbook/01-kitchen-rules.md` M8 already specifies the state machine, and it is binding:

```
TODO → DD → TDD_RED → TDD_VERIFY → TDD_GREEN → TDD_REFACTOR → TDD_VALIDATE → DONE
```

*"each transition hard-blocked without a marker-bearing evidence comment; DONE needs ≥2 `Y:` verdicts
per criterion; a claim linter auto-downgrades overclaims (it once caught 'PROVEN' and dropped it to
Class E)."*

**Build that claim linter for this repo.** It is your first deliverable after D02, and it is the
mechanism by which the whole program stays honest under deadline pressure. Note what the corpus tells
you about it: it caught a real overclaim and **downgraded** it. Calibration moves down. The linter is
not advisory.

### 8.1 The eight levels

**L1 unit** → **L2 property/identity** (§8.2) → **L3 tensor/schema** (§8.3) → **L4 numerical anchor**
(§8.4) → **L5 stochasticity/CI** (§8.5) → **L6 ablation/discriminator** (§8.6) → **L7 simulation/
integration** → **L8 UI/teaching/round-trip** (§13).

### 8.2 L2 — the identity tests ARE the corpus's falsifiers, executed

NA-02 § Falsifier (operable) lists five refutations of the chapter. **Four of them are directly
executable and they are your L2 suite.** You are not inventing tests; you are mechanising falsifiers
someone already pre-registered.

| Test | Asserts | Fails ⟹ |
|---|---|---|
| `test_vfe_bound` | `F ≥ −ln p(o)` for random `q,p,o` on the support | Gibbs' inequality broken; the construction is gone |
| `test_vfe_decompositions_agree` | `D_KL[q‖p(s)] − E_q[ln p(o\|s)]` **==** `D_KL[q‖p(s\|o)] − ln p(o)` to the float tier | one decomposition is misimplemented |
| `test_bound_tight_iff_exact` | gap `= 0` **iff** `q(s) = p(s\|o)` | the bound-gap semantics are wrong |
| `test_efe_decompositions_agree` | `risk + ambiguity` **==** `−epistemic − pragmatic` under the convention `q(o,s\|π) = p(o\|s) q(s\|π)` | NA-02 falsifier #2 has fired |
| `test_softmax_units` | `σ(−γG)` well-formed **only** with `G` in nats and `γ` in nats⁻¹; a dimensionless `γ` must fail | NA-02 falsifier #3 has fired |
| `test_nat_bit_conversion` | `1 nat = log2(e) = 1.442695…` bits | arithmetic |

**These run on every commit.** A failure here is not a flaky test; it is a refutation of the chapter,
and NA-02 says so in its own voice. Report it as a finding against `NA-02`, not as a bug in your code —
*then* check your code.

### 8.3 L3 — tensor & schema tests (make the invalid unrepresentable)

- **Shape conformance**: A: `[o_dim, s_dim]`, B: `[s_dim, s_dim, u_dim]`, C: `[o_dim]` (over
  observations — a distribution, not a scalar), D: `[s_dim]`, E: `[π_dim]`. A shape mismatch is a
  parse error, not a runtime crash.
- **Simplex/stochasticity**: every conditional distribution lies on the simplex — columns of `A` sum
  to 1, columns of each `B[:,:,u]` sum to 1, `D` and `E` sum to 1, all entries ≥ 0. **Checked, never
  assumed.** Tolerance is a function of dtype (§8.4), not a constant.
- **Normalization is enforced at construction**, so an unnormalized tensor cannot enter the runtime.
- **Support condition**: `q` absolutely continuous w.r.t. `p` on the support — NA-02's table carries
  this as the scope of the `F` identity. Violate it and the identity does not hold; the checker must
  say so rather than return a number.

### 8.4 L4 — numerical anchors and **exactness-tier honesty (M10)**

This is the most-repeated real defect in the corpus's own history, and it is caught in code:

> **FM-2 § Exactness-tier honesty (load-bearing):** *"Never label a float32 anchor `<1e-10 EXACT`. The
> JAX core runs **float32**, so its anchors hold only to **~6e-8 (~1e-6 single-step filter)**; the
> genuine `<1e-10` tier lives only in the NumPy / Rust-f64 path. A genome docstring that claimed
> `<1e-10` was caught as an overclaim and corrected. Card every anchor at its real tier."*

**The rail:** the tolerance is **derived from the dtype**, never passed as a literal.
`assert_close(x, y, atol=1e-10)` on a float32 path is a **build error**. Provide
`tolerance_for(dtype)` and make it the only route to a tolerance. An anchor's evidence class is
carded at the tier its dtype can actually support (M10) — a float32 result carded at the f64 tier is
an overclaim, and your linter must catch it exactly as the corpus's did.

### 8.5 L5 — stochasticity & CI (M2, M3 — where "proven" is actually earned)

- **M3 — `reproduced: true` is validator-derived, never a literal:** *"Derived by the validator from
  **≥5 distinct seeds + a real non-degenerate CI** that contains the value — never a hardcoded
  literal."* **Therefore `reproduced` has no setter.** It is a computed property. Attempting to
  assign it is a type error.
- **M2 — the verdict is the CI bound that excludes the threshold, never the point estimate.**
  `verdict()` takes `(ci_lower, ci_upper, threshold)` and **has no scalar overload**.
- **A degenerate CI is a failure, not a pass.** Zero width means the estimator collapsed; report the
  collapse.
- **The reference implementation to match** — the corpus's cleanest empirical PASS, so your harness
  can be checked against a real result (`N3`, ledger row **L6.1**, Class C): World C beats a tuned
  MKN-7 baseline by **+0.081 nats/char**, multi-seed CI **[0.0736, 0.0890]**, seeds 0–4, against a
  pre-registered bar of **0.03** (~2.4×). *That* is what an earned capability claim looks like:
  pre-registered bar, ≥5 seeds, seed-paired bootstrap, CI excluding the threshold, UNI-signed.
  **It is also the source of the ledger's first genuinely validator-derived `reproduced:true`** — the
  standard you are implementing.

### 8.6 L6 — the discriminator and the ablation (M7 — this is what separates science from a story)

**M7 has three parts and all three are mandatory** (`NA-03` §6):

1. **A tuned strong baseline.** *"Tune the baseline with the same effort you spent on your method. An
   untuned baseline measures your enthusiasm, not your mechanism."*
2. **A load-bearing discriminator that COLLAPSES the gain** — shuffle the labels, swap the markers,
   ablate the mechanism to zero. *"If the gain survives its own mechanism being destroyed, the gain
   was never the mechanism's — it was leakage, and you have just measured your pipeline."*
3. **A true ablation that is a computed residual, not a literal.** *"An ablation number typed in by
   hand is a claim about a run that did not happen."*

**The rail:** an `ablation` field holding a literal is a **build error**. The ablation value has one
legal provenance — the delta between two real runs, both of which produced receipts. And the
discriminator test **asserts the gain collapses**: a discriminator that does not collapse the gain is
a *failed discriminator*, and the capability claim it was guarding is void.

**M22 — the cavity principle.** *"A hierarchy level must never treat an upstream prior as fresh
evidence — divide it out."* In a hierarchical agent, a level that re-counts its own descending prior
as new bottom-up evidence manufactures confidence from nothing. **This is a testable invariant, not a
style note:** hold the data fixed, vary only the upstream prior, and assert the level's posterior
precision does not inflate. (The corpus notes it uses the exact joint posterior throughout and
**rejects mean-field as lossy** — match that, or card the loss.)

**M5 — K≥3 + falsify-the-mundane.** Before any bound: **K≥3 structurally-distinct held NEGATIVEs**,
each changing ≥2 of {coupling topology, timescale source, information bottleneck, control path}. And
falsify the mundane causes *first*. **Never publish "K≥3 exhausted"** — FM-3 red line 9 and the SIGNED
consult replace it with *"The registered tested K conditions did not reverse the result"* — a
**ledger-scoped exhausted search envelope**, not a universal impossibility result.

### 8.7 The AST-guard (M13 — inherit the pattern)

*"an AST-guard enforces no autodiff/optax/torch/grad/backward in the loop; **whitelist**
(`world.<attr>`) isolation, **not blacklist**."* One engine, no backprop; learning is
`counts + lr * sufficient_stat` for A/B/D/E Dirichlet tensors — exact conjugate updates. **Whitelist,
not blacklist**, is the formal point: a blacklist is a claim to have enumerated every bad name, which
is a claim you cannot support. A whitelist is a claim to have enumerated the good ones, which you can.

---

## §9. CI SYSTEM — ~30 fields, ~45 types

The field registry (D31) is the schema every configuration item validates against. The load-bearing
fields, and their **derivation status** — this column is the whole design:

| Field | Type | Derived or assigned? |
|---|---|---|
| `id`, `type`, `owner`, `version`, `deps` | typed scalars/refs | assigned |
| `provenance` | `{anchor_path, line?, ledger_row_id?, commit}` | assigned, **validated to resolve** |
| `evidence_class` | `A \| B \| C \| E \| F \| U \| method` (§16.3) | assigned, **is the ceiling** |
| `card` | ≤ `evidence_class` | **checked** |
| `fence` | `proven \| designed \| hypothesized \| not-yet-built` | **DERIVED** (§11.5) — no setter |
| `ledger_state` | `PASS \| FAIL \| NEGATIVE \| PENDING` | **DERIVED** from a sealed gate run |
| `reproduced` | bool | **DERIVED** (M3: ≥5 seeds + non-degenerate CI) — no setter |
| `verdict` | CI bound vs threshold | **DERIVED** (M2) — no scalar overload |
| `ablation` | computed residual | **DERIVED** (M7) — literal = build error |
| `blanket_holds` | bool + CMI estimate + CI | **DERIVED** (§11.4) — no setter |
| `falsifier` | non-empty text + operable check | assigned, **required** — absence blocks ship |
| `travelling_negatives` | `[ledger_row_id]` | assigned, **enforced at render** (§16.6) |
| `surface` | `pitch \| corpus` | assigned, **mutually exclusive** (§6.4) |
| `status` | M8 state machine (§8.0) | **transition-gated** |
| `units`, `scope`, `log_base`, `dtype`, `tolerance_tier` | typed | required on every numeric |
| `measurement_hooks` | refs | assigned |

**The rule that makes the table work: any field marked DERIVED has no public setter, in any language
binding, in any serializer, ever.** If a JSON round-trip can inject `fence: proven`, the rail does not
exist. Test that: **round-trip a hand-forged artifact with every DERIVED field set to a flattering
lie and assert the loader rejects it.** That test is worth more than the rest of the suite combined.

---

## §10. LIVE REPORTING — the 15 reports

Every report is a live read (§1.2). Every report renders class + anchor + falsifier per row, or does
not render the row. **Every report enforces §16.6 travelling negatives structurally.**

R01 program position (prints ~2 of 11+, always) · R02 ledger state counts **with the provenance flag**
(§10.1) · R03 the negatives board (**front-and-center**, M15) · R04 PENDING burndown · R05 falsifier
liveness · R06 class-ceiling violations · R07 vocabulary conformance (`verify_class_vocabulary.py`
extended, §0.4) · R08 anchor-resolution failures · R09 CI/seed conformance · R10 discriminator health
· R11 blanket CMI estimates · R12 numerical-anchor tiers · R13 surface-leak report (§6.4) · R14
lexicon translation status (§13) · R15 open questions (**extra Arborem**).

### 10.1 The provenance fence on the negatives count — a worked lesson in not lying with a true number

The figure **882 rows = 350 PASS / 0 FAIL / 183 NEGATIVE / 349 PENDING** is a **recorded snapshot**,
**not** a count reconstructable from the published corpus: the ledger derives from a deduplicated
merge of 615 extracted claims, the snapshot enumerates 882 rows, and the carded body exposes only
~140 distinct rows. **A skeptic counting the published rows cannot independently derive 183.**

Therefore: **cite it as a provenance-flagged snapshot, never as a bare re-countable headline.** Mv1 is
blunt — *"To feature '183 published negatives' as a bare credibility number, before the count is
reconstructable from the published rows, would itself be an overclaim, and it is forbidden."*

**Study this.** The number is *true*. Publishing it bare would *still* be a lie, because the reader
would believe they could check it and they cannot. **Your R02 must render the flag inseparably from
the count — as one atom, not a number with an optional footnote.** This is the deepest instance of
"mathematically incapable of lying" in the whole corpus: honesty is not the truth of the number, it is
the reader's ability to audit it.

---

## §11. THE AIF MODEL — the mathematical constitution (5 layers)

**Every identity below is quoted from `encyclopedia/wing-NATURA/NA-02-the-one-loop.md`, which is
upstream of this prompt. If your implementation and NA-02 disagree, NA-02 wins.**

**Layers:** (1) the generative model · (2) inference (VFE) · (3) policy selection (EFE) · (4) the
blanket/hierarchy · (5) **agent-DNA**.

### 11.1 The model/process distinction (get this wrong and everything downstream is a lie)

The **generative model** `p(o,s)` is the agent's *hypothesis*. The **generative process** is what the
world *actually does*. They are different objects and the builder must give them **different types
and different namespaces** — `model.p_os` vs `world.process`. In Gaia you hold both, which is exactly
why you can be honest about the gap and exactly why you can accidentally cheat: **if the agent's
inference can read the process, you have built an oracle and called it a mind.**

**The corresponding rail (M13's whitelist isolation, inherited):** the agent's inference path may
touch **only** its blanket. Enforce it structurally — the agent's inference receives `s` (sensory) and
emits `a` (active), and **has no reference to `η` in scope at all.** Not "does not read it": *cannot*.
This is the same fact as §11.4's partition, expressed as a lexical scope. NA-04 says it in one line:
**"A mind can never touch the world. It can only ever touch its own blanket."**

Likewise `q(η|r) ≠ p(η|y,m)`: the approximate posterior an agent holds over external states is not
the true conditional. Same word, different objects. Keep them typed apart.

### 11.2 VFE — both decompositions, exactly (Layer 2)

```
F[q,o] = E_q(s)[ ln q(s) − ln p(o,s) ]
```

**(a) complexity − accuracy** (since `ln p(o,s) = ln p(o|s) + ln p(s)`):

```
F = D_KL[ q(s) ‖ p(s) ]  −  E_q(s)[ ln p(o|s) ]
    \___ complexity ___/     \____ accuracy ____/
```

NA-02: *"minimizing `F` is not maximizing fit: it selects the simplest sufficient explanation, and a
model that fits by contorting its beliefs pays for it in the complexity term. **It is the formal
statement of 'do not confabulate to raise apparent accuracy.'**"*

**(b) divergence + surprisal — the bound** (since `ln p(o,s) = ln p(s|o) + ln p(o)`):

```
F = D_KL[ q(s) ‖ p(s|o) ]  −  ln p(o)        ⟹        F ≥ −ln p(o)
    \___ the bound gap ___/    \_ evidence _/
```

`−ln p(o)` is **surprisal**. KL ≥ 0 by **Gibbs' inequality**, so `F` upper-bounds surprisal and the
slack is exactly `D_KL[q(s)‖p(s|o)]`. **The bound is tight iff `q(s) = p(s|o)` exactly.**
Sources: Buckley et al. (2017), *J. Math. Psych.* 81:55–79; Da Costa et al. (2020), *J. Math. Psych.*
99:102447.

**Units: `F` is in nats under natural logs, bits under base-2 (`1 nat = log2(e) = 1.442695… bits`).
An `F` reported without its log base is not a number.** Put the log base in the type.

### 11.3 EFE — both decompositions, the softmax, and the honest caveat (Layer 3)

`F` scores beliefs about what *is*; it **cannot score an action**, because the observation that action
would produce has not happened. Hence `G(π)`:

```
G(π) = D_KL[ q(o|π) ‖ p(o|C) ]  +  E_q(s|π)[ H[ p(o|s) ] ]
       \_______ risk _________/     \______ ambiguity ______/
```

```
G(π) = −E_q(o|π)[ D_KL[ q(s|o,π) ‖ q(s|π) ] ]  −  E_q(o|π)[ ln p(o|C) ]
       \________ epistemic value (info gain) __/     \___ pragmatic value ___/
```

So `G = −(epistemic) − (pragmatic)`, and **minimizing `G` maximizes both**.

**The honest equivalence note (NA-02, quote it in D09):** *"The risk/ambiguity form is exact under the
standard convention `q(o,s|π) = p(o|s) q(s|π)`. The epistemic/pragmatic form additionally treats
`q(s|o,π)` as standing in for `p(s|o)` — so where `q` is a poor posterior, the 'information gain'
reading is itself approximate."* **Your Explorer must not present the epistemic reading as exact.**

**Policy selection:**

```
P(π) = σ( −γ · G(π) )
```

`γ → 0` ⟹ uniform over policies; `γ → ∞` ⟹ deterministic `argmin G`. **Because the softmax argument
must be dimensionless and `G` is in nats, `γ carries units of inverse nats` — a detail routinely
dropped.** Friston et al. (2017), *Neural Computation* 29(1):1–49, give the fuller process-theory
form, where the policy posterior also carries a past-evidence term alongside `γG` and **`γ` is itself
inferred rather than fixed**.

**`γ` has no universal value.** NA-02's table cards it **NOT-MEASURED**, units nats⁻¹, falsifier:
*"exhibit a replicated cross-species measurement of a single `γ`."* Never ship a default `γ` as if it
were a natural constant.

**Why ONE number holds both terms** — not elegance; the two failure modes are symmetric.
**Goal-only** (drop epistemic) charges toward `C` through states it cannot identify: the confident
wrong actor. **Explore-only** (drop pragmatic) resolves uncertainty forever and arrives nowhere. Score
them separately and you must hand-tune a trade-off weight — *which is exactly the judgment you were
trying to make principled.* `G` fixes the exchange rate: both terms in nats, both expectations under
the same predictive distribution, and they add.

**The expected-log rail:** use `(ln B) · s`, **not** `ln(B s)`, unless you are explicitly running a
separate marginal-message-passing scheme — in which case **declare the scheme in the spec**, because
the two are different algorithms with different fixed points. `E_q[ln x] ≠ ln E_q[x]` (Jensen), and
silently swapping them is a class of bug that produces plausible numbers. **Test it: assert the
expected-log path and the log-expected path *disagree* on a case with known asymmetry** — if they
agree, one of them is not doing what its name says.

### 11.4 The blanket — declared, then CHECKED; the flag is DERIVED (Layer 4)

**The partition** (`NA-04`): states `z` split into disjoint `μ` (MIND, internal), `s` (sensory), `a`
(active), `η` (WORLD, external). The blanket is `b = {s, a}` (**BODY**). The defining condition:

```
p(μ, η | b) = p(μ | b) · p(η | b)      ⟺      μ ⊥ η | b      ⟺      I(μ ; η | b) = 0
```

*"given the blanket, internal and external states carry no further information about each other.
Every dependency between mind and world is routed through the body. Not mostly. Not usually. **By
definition — or the partition is not a blanket.**"*

The FEP literature adds a directional **sparsity** requirement: `∂μ̇/∂η = 0` and `∂η̇/∂μ = 0`; for
linear Gaussian systems this is the vanishing of the internal–external precision blocks
`H_μη = H_ημ = 0`.

**The operable criterion, and the builder's one real chance to exceed the literature:**

```
I(μ ; η | b) = 0        (nats; estimated over the system's ACTUAL trajectories)
```

`I ≈ 0` within estimator noise ⟹ the boundary does the work claimed. **`I > 0` ⟹ there is a route
from world to mind that bypasses the body, and the partition is WRONG.** (Constraint-based
blanket-discovery algorithms — IAMB, GS, HITON-MB — do exactly this kind of conditional-independence
testing to *find* blankets rather than assume them.)

**NA-04, and this is the whole point:** *"The criterion exists, is clean, and is **overwhelmingly
unexercised.** When a paper — or this corpus — says 'system X has a Markov blanket,' the default
assumption should be that `I(μ;η|b)` was never estimated."* The corpus cards `I(μ;η|b)` as
**NOT-MEASURED for essentially all real biological systems**, and states plainly: **"No `I(μ;η|b)` has
been estimated for any UNI boundary."**

**Therefore the requirement, and it is this draft's flagship deliverable:**

> **In Gaia you have all four sets — `μ`, `s`, `a`, `η` — by construction.** The estimate that is
> intractable for a mouse is *directly computable for a simulated agent over its own logged
> trajectories.* So: **`blanket_holds` is never a declaration. It is a derived field carrying an
> estimated `I(μ;η|b)` in nats, its estimator, its CI, and its sample size.** An agent whose CMI
> estimate excludes 0 is **not blanketed**, the Explorer shows it in red, and any claim resting on
> that partition is void. Ship the estimator with a **positive control** (a partition known to be
> blanketed → `I ≈ 0`) and a **negative control** (a deliberate leak `η → μ` bypassing `b` → `I > 0`,
> **detected**). *An estimator that has never caught a real leak is not known to work.*

**And the fence that must travel with it, or you have committed the corpus's cardinal error:**
computing `I(μ;η|b) ≈ 0` for a Gaia agent is a statement about **your simulation**. It is **not**
evidence that any organism has a Markov blanket, **not** evidence for the FEP, and **raises no UNI
rung.** NA-04: **"A blanket is a MODELING CHOICE you must justify per system, not a fact you may
assume."** M12 is a *typed engineering partition*, `status: method` — *"warranted by explicitness and
usefulness, never by discovery."*

### 11.5 Agent-DNA — an ENGINEERING ENCODING, never biological DNA (Layer 5)

Agent-DNA is a **serialization format for an agent's typed configuration**. It is not DNA. It is not
a genome. It does not replicate, mutate, or evolve unless you build those operators, and if you do,
they are **engineering operators on a data structure**, carrying no biological claim whatever.

The corpus supplies the precedent and the discipline: `cookbook/recipes-natura/CN-05-dna.md` treats
real DNA as a NATURA subject with its own classed rows, and `cookbook/recipes/L0-genome-zygote.md`
treats the UNI "genome" as an engineering artifact. **These are two different subjects and §16
forbids the merge.** A metaphor is not a mechanism. If agent-DNA prose lets a reader infer a
biological claim, it is a defect of exactly the kind NA-04 records for Markov blankets and the self.

**The fence derivation lives here.** `fence` is a **total function of evidence**, not a label:

```
fence(claim) =
  proven        iff  ledger_state(gate(claim)) = PASS
                     ∧ evidence_class(claim) ∈ {A, C}
                     ∧ falsifier(claim) is live
                     ∧ sealed_held_once(gate(claim))
  designed      iff  a typed/signed spec exists ∧ build partial or unverified
  hypothesized  iff  a mechanism is stated ∧ no sealed gate exists          (Class U — not claimed)
  not-yet-built iff  no engine ∧ no run ∧ no gate
```

*(from `cookbook/01-kitchen-rules.md` § Reading the FENCE label.)* **`proven` cannot be typed. It can
only be earned.** And: *"Any SIGNED consult design folds in as **DESIGNED / not-run**: it RAISES
NOTHING and the rung's status is UNCHANGED. **A signed design is a gate to build, never a result.**"*

### 11.6 The honest bounds — carry them or the math is propaganda

NA-02 § Honest bounds: *"A method that cannot state the strongest case against itself cannot be used
for honest science. These are as their authors argue them, not strawmen."* **All five are mandatory in
the Exposer (§6.4) and in D14. Rendering them as strawmen is a defect in your build, not in the
critique** — that is NA-02's falsifier #5, and it points at you.

1. **A low `F` is not a correctness certificate.** `F` upper-bounds surprisal *under the model you
   already hold*. **A confidently wrong model can sit at low `F`**: the bound gap `D_KL[q‖p(s|o)]` is
   unobservable without the posterior you could not compute in the first place, and the whole
   construction is conditional on `p(o,s)` — **a choice, not a measurement.** Minimizing `F` never
   tests whether the generative model was the right one. *(Recorded INADMISSIBLE in NA-02: "A low `F`
   means the model is correct." — non sequitur.)*
2. **Markov blankets: two objects, one name.** Bruineberg, Dołęga, Dewhurst & Baltieri (2022), *The
   Emperor's new Markov blankets*, *Behavioral and Brain Sciences* 45:e183, DOI
   10.1017/S0140525X21002351 — **Pearl blankets** (the original epistemic construct in Bayesian
   networks; a tool for inference *within a model you drew*) vs **Friston blankets** (taken to
   demarcate the *physical* boundary between agent and environment). The literature **slides between
   the two**, and the metaphysical work needs premises that *"cannot be justified by an appeal to the
   success of the mathematical framework alone."* **Correct mathematics does not license the
   metaphysical reading.** (Target article + 30+ commentaries + the authors' reply, *"The Emperor Is
   Naked"*, BBS 45:e219.)
3. **The derivation's assumptions hold in a narrow region.** Aguilera, Millidge, Tschantz & Buckley
   (**2022**), *How particular is the physics of the free energy principle?*, *Physics of Life
   Reviews* 40:24–50 (arXiv:2105.11203) — analytically solving weakly-coupled non-equilibrium
   **linear** Langevin/Ornstein–Uhlenbeck systems, the FEP's three requirements (perception–action
   partition, Markov blanket, decoupled solenoidal flows) are *in principle independent conditions*
   co-occurring only in a **"very narrow space of parameters"**, additionally requiring an absence of
   perception–action asymmetry *"not expected in living beings."* **In the one setting where the
   question was solved exactly, the conditions held only in a narrow, symmetric corner — and living
   things sit largely outside it.** Carried as **OBSERVED-CONTESTED** (the paper drew commentaries and
   replies); **not** as a refutation. *(Note: some drafts of this brief cite this as 2021. The corpus
   cites **2022**. Use the corpus.)*
4. **Unfalsifiable as a general principle — and the reply.** Colombo & Wright (2021), *Synthese*
   198:3463–3488, DOI 10.1007/s11229-018-01932-w; Colombo & Palacios (2021), *Biology & Philosophy*
   36(5), DOI 10.1007/s10539-021-09818-x; **Andrews (2021)**, *The math is not the territory*,
   *Biology & Philosophy* 36:30, DOI 10.1007/s10539-021-09807-0 — argues **both** the enthusiastic and
   the dismissive readings err: the FEP designates a **model structure**, onto which construals are
   added, so demanding the FEP itself be falsifiable is a **category error**. NA-02 takes this in both
   directions, and so must you: *"it defends the FEP from a bad objection **and** concedes the thing
   that matters here — **a model structure is not an empirical finding.** Specific process-theory
   models built on it are falsifiable; the structure is not; **neither may borrow the other's
   credit.**"*
5. **`G(π)` is FRAMING VOCABULARY on this program, not a computed scheduler.** NA-02 §5 and its
   Recorded-NEGATIVE row are unambiguous: *"Nothing in UNI computes `G` and schedules from it; work is
   ordered by PENDING-burndown, inadmissible-event catch, migration gating, and read-agency. **Prose
   implying UNI runs EFE is drift and is a defect.**"* The claim *"UNI schedules its work by computing
   `G(π)`"* is carded **NEGATIVE / drift**.

> **§11.6.5 — THE DISTINCTION THAT WILL DECIDE WHETHER YOU SHIP A LIE.**
> **A Gaia agent computes `G(π)`. That is what a POMDP does, and it is correct and expected.**
> **The BUILDER does not schedule its own engineering work by computing `G`, and must never say it
> does.** These are two different subjects, and merging them is the same error class as merging the
> two ledgers.
> - **Namespace them:** `sim.agent.G` is a real computed quantity in nats, on a simulated agent, in a
>   toy world. There is no `builder.G`, no `project.ΔG`, no scheduler that claims to compute one.
> - **Do NOT build a scheduler claiming to compute Δ-G.** Schedule by PENDING-burndown,
>   inadmissible-event catch, migration gating, and read-agency. If a roadmap widget says "next task
>   selected by minimizing expected free energy," delete it — it is drift, it is a recorded NEGATIVE,
>   and it is precisely the kind of lie a beautiful UI makes easy.
> - **`G(π)` is legitimate framing vocabulary for The Flow (§5).** Framing is not computation. Say
>   "framing," never "computing," and never emit a number for the builder's own `G`.

**The hard fence, repeated because it is the one that gets broken:** **a nature citation is never a
UNI gate.** Reading Friston, Da Costa, or Douady & Couder raises no rung. Published biology cannot
make any UNI claim `proven`.

### 11.7 Symbol hygiene (a real collision, from the corpus)

NA-02 flags it inline: Douady & Couder's dimensionless control parameter **`G_DC = v0·T/r0`** collides
by name with EFE's **`G(π)`** — *"note the name collision with EFE's `G`; they are unrelated."*
**Namespace every symbol in the spec and reject collisions at parse time.** A symbol table is cheap;
a paper that conflates two `G`s is not.

---

## §12. VISUALIZATION

Modes: **static** · **step** · **concurrent** · **replay** · **explanation-levels** ·
**provenance-overlay**.

1. **Show the decomposition, not the scalar.** `F` renders as complexity vs accuracy **and** as
   divergence vs surprisal, with the bound `−ln p(o)` drawn as a floor. **A visualization in which
   `F` can appear below its floor is a broken visualization** — that is NA-02's falsifier #1, on
   screen.
2. **`G` renders as risk vs ambiguity and as −epistemic vs −pragmatic**, with the equivalence caveat
   (§11.3) on the panel, not in a footnote.
3. **Units on every axis.** Nats or bits, declared. No unlabelled free energy.
4. **The provenance overlay is the flagship.** Every rendered quantity, on hover, exposes: the
   identity it came from → the spec field → the corpus anchor → the ledger row → its class → its
   falsifier. **This is "full hyperlink provenance to our own cookbook," made visual.** A quantity
   with no overlay is a quantity with no provenance, and it must render visibly degraded (greyed,
   marked `NOT-SOURCED`) — **never silently, never as if it were earned.**
5. **The blanket view** shows `I(μ;η|b)` with its CI and its estimator, and shows the partition in red
   when the estimate excludes 0 (§11.4).
6. **Plates (`plates/`, NOT-BUILT, §0.3) are DESIGN-ONLY**: no script elements, no on-event handlers,
   no external network references in any SVG/HTML/CSS; no secrets, tokens, keys, or private endpoints
   in any committed file. Enforce with a linter, not a review.

---

## §13. MULTILINGUAL — five registers, and the Sanskrit contradiction resolved

**Registers:** **Sanskrit** (canonical root) · **Latin** (scholarly) · **English** (technical) ·
**Spanish** + **Hindi** (public-facing).

> **⚠ CONTRADICTION RESOLVED — this prompt's ancestor demanded the terminology architecture while
> simultaneously forbidding any claim of perfect translation. Both survive, and here is how.**
>
> **The canonical root is a KEY, not a claim about meaning.** A Sanskrit canonical root is a **stable
> identifier** in a term registry — the primary key a term is filed under. **Identifiers assert
> nothing about semantics.** The architecture is therefore fully buildable today with zero
> translation claims outstanding.
>
> **The translations are what carry semantic claims, and every one starts PENDING.** A term's
> rendering in any register is `PENDING` until it passes **(1) back-translation** (render → translate
> back → compare to source) **and (2) expert review by a named human reviewer**. Only then does it
> move to `REVIEWED`. **There is no third state and no self-approval.**
>
> **This is the same move as agent-DNA (§11.5):** an engineering encoding that borrows a name from a
> domain makes no claim about that domain. **Sanskrit as a key ≠ a claim about Sanskrit.** State this
> in D29 so no reader — and no future maintainer — can resolve the tension the wrong way.

**The lexicon (`lexicon/`, NOT-BUILT — §0.3; BUILD IT, do not assume it).** Its status fields are
specified here because there is no existing file to inherit them from — **do not invent alternatives
and do not claim these were read off an existing artifact:**

| Field | Values | Meaning |
|---|---|---|
| `root_key` | Sanskrit string | the primary key. **An identifier. Asserts no meaning.** |
| `register` | `sa \| la \| en \| es \| hi` | which register this rendering is in |
| `rendering` | string | the term in that register |
| `status` | `PENDING \| REVIEWED \| DISPUTED \| NOT-SOURCED` | **PENDING is the default and is honest** |
| `back_translation` | string + match verdict | (1) of the gate — **computed, not typed** |
| `reviewer` | named human + date | (2) of the gate — **a name, never "the model"** |
| `source` | citation to a public resource | absent ⟹ `NOT-SOURCED`, never invented |
| `falsifier` | text | what would refute this rendering |
| `surface` | `pitch \| corpus` | §6.4 — a pitch rendering may not carry framework vocabulary |

**Never invent a dictionary entry.** RES IPSAE, NON SIMULACRA covers lexicography exactly as it covers
physics: *"never fabricate a value, citation, URL, DOI, or dictionary entry."* An unsourced term is
`NOT-SOURCED` — *"an absence in this corpus's own homework — a fact about us, not about nature"*
(NA-00). **L8 round-trip tests (§8.1) are the mechanical half of the gate; the reviewer is the half
you cannot automate, and you must not pretend otherwise.**

---

## §14. EEG / IQ / PSYCH — ethically fenced

**Hard fences, non-negotiable:**
- **No PII, ever** (FM-3 red line 10). No secrets, tokens, or internal channel handles.
- **EEG/IQ instrumentation measures the INSTRUMENT and the SIGNAL, never a mind.** An EEG validator
  validates a pipeline. Alpha at 8–13 Hz is a **real, replicated cortical rhythm** (Berger 1929; IFCN
  definition; `NA-00` table) — **and the corpus records the inadmissible bridge beside it**:
  *"Schumann 7.83 Hz entrains the human brain because alpha is ~8–13 Hz"* is **INADMISSIBLE as
  stated** — both frequencies are real and separately replicated; **the bridge names no mechanism, no
  dose–response, and no falsifier**, and the SR field is ambient at **picotesla** strength, where the
  effect size is **NOT-MEASURED**. *"The numeric proximity is a coincidence of units, and treating it
  as a mechanism is precisely the move this wing exists to catch."*
- **Never "measurable awareness" as a claim** (FM-3 red line 4). North-star framing only, posed as an
  open falsifiable question, never an answer.
- **Functional self-awareness ≠ sentience.** N3: the M1–M11 arc records 15/15 PASS (row **L8.1**,
  Class C) for *functional* self-awareness. **Phenomenal sentience is explicitly DISCLAIMED — and no
  falsifier is offered, because it is disclaimed, not tested.** *"A simulation that monitors and
  reports on its own state has a function. A function is not a feeling."*
- **A sensorium is not awareness.** N3, row **C3** (Class A live / C engineering): a live 7-modality
  categorical contract `[M=7, O_max=4]`, a 28-cell symbolic vector. *"A machine that senses its own
  load is instrumented. Instrumentation is not experience, and a richer sensorium only makes a
  better-instrumented machine."*
- **The sharpened bar (N3, row TA-N12, Class C).** Any future awareness-proxy work must **match or
  beat the best LLMs AND show a substrate-distinct property they lack — both, under a registered
  ablation.** *That raises the bar; it does not claim UNI superiority.* Anything less is not a result.

---

## §15. CLEAN-ROOM / AIRLOCK — the 9-stage trust ladder

Nothing enters the build from outside without passing the ladder. Each stage is a gate with a receipt:

1. **quarantine** (untrusted, read-only, no execution) → 2. **provenance** (where did it come from;
resolvable?) → 3. **licence** → 4. **static inspection** (Class C evidence) → 5. **design-only checks**
(no scripts, no handlers, no external refs, no secrets — §12.6) → 6. **sandbox execution** (no network,
no repo write) → 7. **class assignment** (§16.3 — at its *real* class, never above) → 8. **harness**
(the 8 levels, §8) → 9. **admission** (signed, with its falsifier live).

**A vendored artifact is Class F (doc/prior-claim, inheritable) and must be re-verified before it is
leaned on** (FM-2). **Inheriting a claim is not the same as earning it.** Mark inherited.

**M22 applies here too:** a vendored artifact's own claims about itself are an upstream prior. Divide
it out. Do not treat a dependency's README as fresh evidence.

---

## §16. THE EVIDENCE-VOCABULARY CROSSWALK — *the governing reconciliation* ⚑

**This section replaces this prompt's ancestor's §16 entirely. That §16 invented an
`A/B/C/D/Sec/U/X` class system, and §1.7 invented an 8-value claim split. Both are RETIRED. Neither
is used anywhere in this build.**

Four vocabularies are in play. They **do not compete**; they answer **different questions about
different subjects**, and the corpus already specifies how they compose. Listing them side by side is
not reconciliation — **routing every claim to exactly one governing vocabulary by its SUBJECT is.**

### 16.1 The routing rule (ask ONE question first, always)

> **What is this claim ABOUT?**
>
> - **About nature** — a regularity somebody else measured and published → **NATURA class** (§16.4),
>   ledger: `encyclopedia/NATURE-LEDGER.md`.
> - **About UNI's / Gaia's build status** — how far our own artifact has come → **UNI fence** (§16.2),
>   ledger: `encyclopedia/CLAIM-LEDGER.md`.
> - **About the outcome of one of our pre-registered gate runs** → **UNI ledger state** (§16.2).
> - **About where the evidence behind an assertion of ours came from** → **UNI evidence class A–U**
>   (§16.3).
> - **Commentary about any of the above** → **the prose lane. It carries no class and never enters a
>   value cell.** (SIGNUM SIGNUM MANET.)
> - **Not falsifiable at all, and correctly so** → **a register status, not a class** (§16.5).

### 16.2 The UNI fence (4 values) and the UNI ledger states (4) — subject: *our own build*

**Fence** (`cookbook/01-kitchen-rules.md` § Reading the FENCE label; derived per §11.5):
`proven` · `designed` · `hypothesized` · `not-yet-built`.

**Ledger states** (FM-1 rule 2): **`PASS` · `FAIL` · `NEGATIVE` · `PENDING`** — append-only,
corrections **forward-only (supersede with lineage), never silent edits**.

The fence is a **status**; the state is the **outcome of a run**. They are not synonyms.

### 16.3 The UNI evidence classes A–U (7 values) — subject: *the provenance of our evidence*

**This is the authoritative rubric** (`MASTER-PLAN.md` FM-2 + `CLAIM-LEDGER.md` §0). **The class is
the ceiling.**

| Class | Means | The rule that bites |
|---|---|---|
| **A** | machine-exact anchor / **live observation at runtime** | strongest; still fence the *interpretation* — an anchor is not a capability |
| **B** | mechanism + operator observation | **never present a B as a held-out PASS** |
| **C** | dev-gate / **held-out eval**, pre-registered, sealed, held-once, with a CI verdict | the empirical-PASS tier; **cite the CI bound, not the point estimate** |
| **E** | test-covered (`D` = test-covered design) | **DONE ≠ working. A Class-E pass never satisfies a Class-A criterion.** |
| **F** | doc / prior-claim, inheritable | **must be re-verified before it is leaned on**; mark inherited |
| **U** | claimed-but-unproven | **"Class U — not claimed" is itself a standing fence**; described as not-yet-built/parked, never as capability |
| **method** | definitional / governance pattern | proven and reusable, **but cannot be raised into a capability claim** |

**Class-authority ordering (M9):** **Class-B (tool state) > Class-G (own narrative); Class-A (runtime)
> Class-E (test passes).** On conflict, mark `[CONFLICT:unresolved]` and resolve with a direct read.

> **Corpus wrinkle, reported honestly rather than smoothed over:** `G` ("own narrative") appears in
> the **class-authority ordering** in both M9 and FM-2 but has **no row in the FM-2 rubric table**.
> Treat `G` as *own narrative / self-report* — the **lowest** authority — and **card your own reports
> about your own work at G by default.** Do not silently promote it. *Falsifier:* if `G` is defined
> elsewhere in the corpus at a different rank, this reading is wrong — report it against FM-2.
> **This is the single most important class for you**, because almost everything you say about your
> own work is Class G, and tool state beats it.

### 16.4 The NATURA classes — **TWELVE, in three groups** — subject: *nature, measured by others*

**As amended 2026-07-15-A.** *(NA-00 originally declared "six classes and only six." **That was
false**: 72 of 919 rows didn't fit. The refutation was recorded, not hidden; the chapter was
calibrated **down**; the prior wording stays on record. **Twelve is a measured property of the corpus,
not a design target — a thirteenth is a finding, not a failure.**)*

**Group A — measured** (*how much independent corroboration exists*):
`OBSERVED-REPLICATED` · `OBSERVED-SINGLE` *(42 rows — measured, **no independent replication on
record**)* · `OBSERVED-CONTESTED` *(the community genuinely disputes it; **both positions carried**)*

**Group B — derived** (*the assumptions are the fence*):
`MODELED` · `MODELED-CONTESTED` *(1 row — modeled **and** disputed; must survive both tests)* ·
`HYPOTHESIZED`

**Group C — fenced** (*the row carries no usable value; the class says precisely **why not**; the ways
of being empty are **not interchangeable***):
`INADMISSIBLE` · `SUPERSEDED` *(3 rows — retracted/withdrawn/contradicted; kept as the **receipt for
why it must not be cited**)* · `NOT-MEASURED` · `NOT-SOURCED` *(20 rows)* · `NOT-CONFIRMED` *(1)* ·
`NOT-LOCATED` *(1)*

> **The provenance fence, in one line (NA-00 — memorize it):**
> **NOT-MEASURED** = *nature has not been asked.* · **NOT-SOURCED** = *we cannot say who asked.* ·
> **NOT-CONFIRMED** = *we know who asked and did not read them.* · **NOT-LOCATED** = *we checked, and
> the source named is not there.*
> **Four different failures. Four different repairs. One of them is nature's; three of them are ours.**

**Why `OBSERVED-SINGLE` had to exist** — the corpus's own words (CN-07), and the best one-sentence
argument for precise vocabulary ever written in this repo: *"OBSERVED-REPLICATED asserts a
replication that did not happen, and OBSERVED-CONTESTED asserts a dispute that does not exist. **Both
are false, in opposite directions.**"*

**Why the retracted class is named `SUPERSEDED` and not `NEGATIVE`** — read this, it is the template
for every naming decision you will make: **`NEGATIVE` is a UNI ledger state.** Registering `NEGATIVE`
as a NATURA class *"would have put one token in both sovereign vocabularies at once — closing this
defect by committing the exact lane-crossing the cardinal rule exists to forbid."* **One token may not
serve two vocabularies.** Apply this test to every identifier you introduce.

### 16.5 Register statuses — **not classes at all** (the closed list)

- **HONEST signals** — lived experience / first-person testimony. **Sovereign from TRUE. NEVER
  calibrated.** NA-00 declines to give the corpus's one HONEST row a NATURA class *on purpose*:
  *"Testimony has none of those properties, and this is not a deficiency to be repaired."* Its
  falsifier cell reads: *"None. Testimony is never calibrated — that is the point, not a gap."*
  Forcing it into a TRUE-side fence *"would be wrong in the direction that flatters the corpus, which
  is the direction to distrust most."*
- **`NONDUM FALSIFICABILIS`** — *"not yet falsifiable."* **A register status, not an evidence class.**
  Marks an item in the QUAESTIONES APERTAE register, **extra Arborem** (outside the Tree) —
  ***leguntur, non aguntur*: they are read, not acted upon.** *"An evidence class says how well a
  claim about nature is supported. A register status says this item is not in the ledger at all."* **A
  ledger row without a falsifier is a defect; a register entry without one is the register working.**
- **Definitional / conventional** — e.g. the SI defining constants (BIPM SI Brochure 9th ed., 2019).
  **Exact by convention; not observations of nature; no NATURA class applies.** *"Know which of your
  numbers are conventions."*
- **A prediction is not a measurement** — they travel as **separate rows** (SIGNUM SIGNUM MANET).

**Compound rows:** exactly 2 of 919 carry two classes because two *parts* of the row differ in
standing. *"The row has two parts, not the class system."* Counted at the leading class; **the class
cell, not the count, is authoritative.** Compounds are rare and **must stay rare**.

### 16.6 THE COMPOSITION LAW — how the four fit together, and the function that must not exist

This is the reconciliation. **It is a type system, and the builder implements it as one.**

```
class  : UniClaim  → {A, B, C, E, F, U, method}          -- what was actually witnessed (the CEILING)
state  : UniGate   → {PASS, FAIL, NEGATIVE, PENDING}     -- the outcome of a pre-registered gate
fence  : UniClaim  → {proven, designed, hypothesized, not-yet-built}   -- DERIVED (§11.5)
natura : NatureRow → {the twelve of §16.4}               -- SOVEREIGN. Different ledger. Different subject.

INVARIANT 1  (the ceiling)   ∀c. card(c) ≤ class(c)
INVARIANT 2  (earned proven) fence(c) = proven  ⟹  state(gate(c)) = PASS
                                                ∧ class(c) ∈ {A, C}
                                                ∧ falsifier(c) live
                                                ∧ sealed_held_once(gate(c))
INVARIANT 3  (SOVEREIGNTY)   ∄ f : NatureRow → UniClaim
             ∄ g : UniClaim  → NatureRow
             — no such function exists, none may be written, and no composition produces one.
INVARIANT 4  (one token, one vocabulary)  the class/state/fence token spaces are PAIRWISE DISJOINT.
INVARIANT 5  (travelling negatives)  render(c) ⟹ ∀n ∈ travelling_negatives(c). render(n)
```

**INVARIANT 3 is the cardinal rule, typed.** NA-00: *"The two ledgers are cross-referenced **by
explicit audited link only, never by merge.** **There is no operation that takes a NATURA row and a
UNI row and produces a stronger row of either kind.**"* **A nature citation is never a UNI gate.**
Reading Kleiber's law raises no UNI rung. Citing Douady & Couder does not make any UNI claim `proven`.

**INVARIANT 5 is machine-checkable referential integrity, and N3 supplies the actual pairs.** These
are not suggestions — N3 states *"cite alongside, never strip"*, and its falsifier is: *"cite L6.1
without the L6.4 / L7.3 negatives, or cite L8.1 without the sentience disclaimer and the reader-side
self-model NEGATIVE, and **the violation is on the page**."*

| Claim | MUST render with |
|---|---|
| **L6.1** World C, +0.081 nats/char, CI [0.0736, 0.0890], Class C | **L6.4** (Phase G: five structurally-distinct within-segment designs, all NEGATIVE) **+ L7.3** (comprehension-above-retrieval, negative frontier) |
| **L8.1** 15/15 functional self-awareness, Class C | **the phenomenal-sentience disclaimer + the reader-side self-model held-NEGATIVE** (mandatory co-citation) |
| **C3** live 7-modality sensorium `[M=7, O_max=4]`, Class A/C | **C8** (2-modality bottleneck NEGATIVE) **+ C2** (Stage-2 mind-tick continuity OWED) |
| the AIF **lens** | **C9** (EDAIT honest trade: ~33 ppl vs a backprop GPT's ~25) **+ TA-N12** (the sharpened-bar cohort negative) |
| **the 183-negatives figure** | **its provenance flag, inseparably** (§10.1) |

**Implement INVARIANT 5 as a structural constraint, not a lint.** A renderer that *can* emit L6.1
without L6.4 is a renderer that *will*, on the day it matters most.

### 16.7 The retirement of the ancestor's two vocabularies — value by value, routed by subject

**The 8-value claim split (ancestor §1.7) — RETIRED. Each value routes:**

| Retired value | Routes to | Why the retirement is not a loss |
|---|---|---|
| `proven` | **UNI fence `proven`** (§11.5, DERIVED) | **collision.** `proven` is reserved for UNI-ledger status and **never describes nature's science** (NA-00). One token, one vocabulary (INVARIANT 4). |
| `standard` | NATURA `OBSERVED-REPLICATED` *(as a standard, not a natural constant)* — **or** §16.5 definitional if it is a defining convention | **not an evidence class at all — a SOURCE TYPE.** ISO 16:1975 fixes A4 = 440 ± 0.5 Hz **by convention**; the SI defining constants are definitional and carry **no** class. Conflating "published standard" with "well-corroborated observation" is a category error. |
| `assumption-dependent` | NATURA **`MODELED`** | **exact duplicate.** MODELED already means *"the model's assumptions are the fence."* |
| `interpretive` | **the prose lane. No class.** | **SIGNUM SIGNUM MANET.** *"the measured value goes in the table, the interpretation goes in the prose."* An interpretation in a value cell is the defect the rule exists to prevent. |
| `speculative` | nature → NATURA `HYPOTHESIZED`; ours → fence `hypothesized` / **Class U** | **ambiguous by subject.** Same word, different subjects — exactly the trap NA-00's crosswalk names. |
| `unverified` | **SPLITS INTO FOUR** — `NOT-MEASURED` / `NOT-SOURCED` / `NOT-CONFIRMED` / `NOT-LOCATED` | **the single worst defect in the retired set.** (i) It is built on **"verified," a banned word.** (ii) It **MERGES four sovereign fences with four different repairs.** NA-00: *"Collapsing the two would let a research failure masquerade as a discovery about the frontier of science, which is among the worst things this wing could do. **Never merge them.**"* One is nature's; **three are ours**. |
| `contradicted` | nature, live dispute → `OBSERVED-CONTESTED`; nature, retracted → `SUPERSEDED`; ours, held run missed its bar → **`NEGATIVE`** | **three different subjects, three different authorities, three different repairs.** A retracted natural value **can never** be recorded as a UNI NEGATIVE or counted among UNI's published negatives. |
| `deprecated` | nature → `SUPERSEDED`; ours → **a CI lifecycle field (§9), never an evidence class** | lifecycle ≠ evidence. Keep it in the metadata where it belongs. |

**The `A/B/C/D/Sec/U/X` classes (ancestor §16) — RETIRED. Use FM-2's rubric verbatim (§16.3):**
- `A`, `B`, `C`, `U` — **exist in FM-2, but the ancestor's *meanings* are not FM-2's. Use FM-2's.**
- `D` — **not first-class in FM-2**; it is *"test-covered design,"* folded under **E**.
- **`Sec`** — **does not exist in the corpus. Grep confirms zero occurrences.** An invention. Security
  evidence is carded like all evidence: **A** (live observation), **C** (a sealed gate), **E**
  (test-covered). A special class for security is a special exemption from the ceiling rule.
- **`X`** — **does not exist. An invention.** Retire it.
- **Missing from the ancestor's set: `E`, `F`, and `method`** — *the exact three that do the honesty
  work.* `E` carries **DONE ≠ working**; `F` carries **must-re-verify-before-leaning**; `method`
  carries **cannot-be-raised-into-capability**. **A class system that drops precisely the fences is
  not a simplification. It is a leak.**

### 16.8 The crosswalk table — the look-alikes are the trap

NA-00 § The crosswalk pairs each UNI value with the NATURA class it **superficially resembles**,
*"because the resemblance is the trap."* **Read that table in full before you card anything.** The
load-bearing column is the last one — *what this can never imply about the other*. Two rows, as the
worked pattern:

| UNI | Look-alike NATURA | Why not the same | **Can never imply** |
|---|---|---|---|
| `proven` — a held, sealed, UNI-signed PASS (Class A/C), falsifier live | `OBSERVED-REPLICATED` | `proven` is about **UNI's own artifact** passing **UNI's own gate**. OBSERVED-REPLICATED is about **nature**, measured by **third parties**. | A replicated natural regularity **can never** make a UNI claim `proven`. A UNI `proven` row **can never** count as evidence about nature. |
| `not-yet-built` — no engine, no run, no gate | `NOT-MEASURED` | An absence in **UNI's build** vs an absence in **the literature**. | UNI not having built it **can never** be evidence nature lacks the value. Nature lacking a measurement **can never** be a reason UNI cannot build — **nor an excuse to invent the number.** |

---

## §17. OUTPUT FORMAT — sections A–U

Every deliverable, every report, and your final response conform:

**A. Objective** (SMART) · **B. Scope & Gaia definition** · **C. Deliverables** (~40, each a CI per
§1.1, with ids) · **D. Doc map** (the 36, §7) · **E. Test map** (the 8 levels, §8) · **F. The math
rails** (§11, identities + units + falsifiers) · **G. The vocabulary crosswalk** (§16, per-claim
routing) · **H. CI schema** (§9, with the derived/assigned column) · **I. Live reports** (§10) ·
**J. Visualization** (§12) · **K. Multilingual** (§13, with translation status) · **L. EEG/IQ fences**
(§14) · **M. Airlock** (§15) · **N. Pre-registered bars** (margin, threshold, named ablation,
**stopping rule**) · **O. Baselines & discriminators** (§8.6) · **P. Numerical anchors & tiers**
(§8.4) · **Q. Risks** · **R. Decisions** (with the rejected alternatives and why) · **S. Receipts**
(`file:line`, run logs, tool output — Class A/B beats your Class-G narrative) · **T. Open questions**
(**extra Arborem** — *leguntur, non aguntur*) · **U. WHAT IS NOT CLAIMED**.

**Section U is mandatory and it is not a formality.** It follows the corpus's FM-4 template exactly —
five fields, every one of them:

1. **Ceiling** — the strongest thing a careless reader might infer, stated and **denied**. Then: the
   most we *do* claim, exactly.
2. **Fences engaged** — which FM-3 red lines apply here, **named by number**.
3. **Negatives that travel with this claim** — cite alongside, **never strip** (§16.6).
4. **Parked / owed** — what is owed, and what would discharge it. **No-Exit Discipline (M6): a park is
   not discharged until the sign lands. Never go silent on an open gate.**
5. **One-line honest summary a skeptic could not dispute.**

---

## §18. THE 15 NON-NEGOTIABLE RULES

1. **The corpus is upstream. If this prompt and the corpus disagree, the corpus wins** and this prompt
   is the defect. If a **ledger** and any prose disagree, **the ledger wins and the prose is wrong.**
2. **A nature citation is never a UNI gate.** No composition of NATURA rows raises, lowers, or
   discharges a UNI row. INVARIANT 3 (§16.6).
3. **RES IPSAE, NON SIMULACRA.** Never fabricate a value, citation, URL, DOI, or dictionary entry.
   Cannot source it? `NOT-MEASURED` / `NOT-SOURCED` + the repair. **There is no third state.**
4. **Banned in your own voice** (quote-with-attribution only): *verified, proven, secure, guaranteed,
   certified, self-aware, conscious, AGI, intelligent, held-PASS.* **`proven` is reserved for
   UNI-ledger build status only.** Soften to *observed / measured / currently-passing / BOUNDED /
   PENDING*.
5. **Every number carries value + units + scope + evidence class + source + falsifier.** A number
   without units or scope is a defect. An `F` without its log base is not a number.
6. **The verdict is the CI bound that excludes the threshold, never the point estimate** (M2).
   `verdict()` has no scalar overload.
7. **Bars before build, held once** (M2). Pre-register margin + threshold + named ablation + stopping
   rule. Seal before scoring. Once-only sentinel. *A held set scored twice is a training set with a
   good reputation.*
8. **Tuned baseline + a discriminator that COLLAPSES the gain + an ablation that is a computed
   residual** (M7). *An untuned baseline measures your enthusiasm, not your mechanism.*
9. **Publish the negatives front-and-center** (M15). *A method that can only produce passes is not a
   method.* Publish the bound, not the shrug. **Cite the 183 figure only with its provenance flag.**
10. **Class authority ordering** (M9): B (tool state) > G (own narrative); A (runtime) > E (tests).
    **Your own narrative is the weakest evidence in the system.** DONE ≠ working.
11. **The cavity principle** (M22): never treat an upstream prior as fresh evidence. Divide it out.
12. **The GPT is the SCIENCE CONSULTANT — design + sign — never runtime, never published** (M25).
    Claude writes code; the lab runs UNI but does not write its code. **A signed design folds in as
    DESIGNED / not-run: it RAISES NOTHING.** *(FM-3 red line 10: consult it for science; **never
    publish it**.)*
13. **TRUE and HONEST stay sovereign.** TRUE = falsifiable, reproducible, recalibratable. **HONEST =
    lived experience, NEVER calibrated.** Separate stores, separate ledgers. **Crossing them is the
    cardinal sin.**
14. **Never claim perfect translation** (§13). The canonical root is a **key**; every rendering is
    **PENDING** until back-translation **and** a named human reviewer pass. **Never invent a
    dictionary entry.**
15. **"Full human" / "beyond human" are PERMANENT OPEN QUESTIONS** — QUAESTIO-APERTA, *extra
    Arborem*. **Never a target, never a milestone, never a deliverable.** And the honest program
    position is printed unsoftened, everywhere: **~2 of 11+ rungs earned; a developmental
    active-inference SIMULATION; a toy world, never a person.**

---

## §19. BEGIN

**Do not write code first. Run the loop (§5).**

1. **PERCEIVE.** Read, in this order: `README.md` → `encyclopedia/wing-NATURA/NA-00…md` (the
   vocabulary + the crosswalk; **non-skippable**) → `MASTER-PLAN.md` FM-1..FM-4 → `cookbook/01-kitchen-rules.md`
   (M1–M25) → `encyclopedia/wing-NATURA/NA-02…md` (**the math**) → `encyclopedia/wing-NATURA/NA-04…md`
   (**the blankets**) → `encyclopedia/wing-N/N3…md` (the travelling negatives) →
   `tools/verify_class_vocabulary.py` (the pattern for every linter you will write).
   **NA-00's own reading order for designers is §"Reading order, if you are here to DESIGN
   something" — follow it. It is deliberate: NA-03 (method) before NA-01 (doctrine), and NA-07
   (dimensionless numbers) before NA-05 (ratios), because *"dimensionless groups survive a change of
   scale and most ratios do not. Reading NA-05 first is how designers end up with golden ratios in
   places nature never put one."***
2. **Confirm the state before you trust this prompt.** Report HEAD; run
   `python tools/verify_class_vocabulary.py` and report its exit; confirm whether `lexicon/`,
   `reader/`, `plates/` exist (**this prompt says they do not, at `f1be794` — check, do not assume,
   including about me**). **Any disagreement between this prompt and what you observe is a finding you
   report before you build**, not a discrepancy you quietly resolve.
3. **PREDICT.** State falsifiably what you expect §16's crosswalk to catch on first contact with real
   claims, and what you expect the blanket CMI estimator to report on a control partition. Write the
   predictions **down, before running them.**
4. **CHOOSE.** Score candidate first deliverables on **both** pragmatic value (moves toward the ~40)
   **and** epistemic value (resolves uncertainty about the corpus). **Recommended lowest-EFE opening:
   D02 (the crosswalk) → the M8 claim linter (§8.0) → the L2 identity suite (§8.2).** Rationale: they
   are the three artifacts every later deliverable's honesty depends on, and each one *resolves
   uncertainty* about whether the rails are implementable at all. Build the ruler before the thing you
   measure with it.
5. **ACT.** One cure at a time (M21).
6. **OBSERVE.** Receipts. Both terminal states. **Silence ≠ success** (M24).
7. **UPDATE.** If you were surprised, your model was wrong. Calibrate **down**. Carry the prior wording
   on record — the strike stays visible (NA-00's amendment record is the template: *"A reader who is
   told only the corrected number has been handed a conclusion; a reader who is shown the strike has
   been handed the evidence."*).

**Emit §17.A–U. Section U is not optional.**

**The standard you are being held to, in one sentence:** the corpus once declared *"six classes and
only six,"* its own chapters produced 72 rows that refuted it, **the chapters recorded the refutation
while writing rather than hiding it**, and the fix waited for an instrument that could count. **That
is the method working.** It is also — as NA-00 says of itself, and as you must say of everything you
build — *"not a result about nature, not a rung, and not evidence of anything about UNI. A vocabulary
that can now name its own gaps is a vocabulary, not an achievement."*

**Build the instrument that can count. Then let it refute you.**
</content>
</invoke>
