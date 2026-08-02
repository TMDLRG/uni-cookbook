# ORCHESTRATE — UNI BUILDER (GAIA): a visual active-inference construction kit

**Paste target:** Codex 5.6, cold. You have no other context. Everything you need to start is in this
document; everything you need to finish is in the repository named in §4. Read §4 before §1 executes.

**The one-line brief:** ship a **CAD/LEGO builder for active-inference agents** that a three-year-old
can enter and a PhD can verify — with a teaching layer, a test pyramid, and full hyperlink provenance
into an existing 23-chapter science corpus. **Software is the deliverable. Documents serve it.**

---

## 0. READ THIS BEFORE §1 — the five things that make this prompt different

Four of these correct real defects in the previous revision of this prompt (v1). One is the hard
practical guard. They override anything below that contradicts them.

1. **ONE evidence vocabulary system, on three orthogonal axes (§16).** v1 invented two of its own. The
   corpus already runs the real ones. Yours are deleted. §16 is the reconciliation, and it is the
   section a reviewer will check first.
2. **The corpus is upstream truth (§4).** Every claim you emit hyperlinks to a chapter anchor or a
   ledger row id, or it is `NOT-SOURCED` and says so. You do not restate the corpus in your own words
   and call it a source.
3. **Product before paperwork (§7, §8, §10).** v1's fatal risk was 36 documents and 15 live reports
   before a single pixel. Inverted here: **M0 is a running builder in week one.** Documents are
   generated *from* the running system, never hand-authored ahead of it.
4. **`G(pi)` is framing vocabulary on this program, not a computed scheduler (§11).** Do not build a
   scheduler that claims to compute `Delta-G`. The corpus records that exact claim as a **drift
   defect**. You may *teach*, *display*, and *simulate* `G` inside a toy agent; you may not *schedule
   your own work* by it and say the program does.
5. **Three of the things you were told exist, do not (§4.3).** `lexicon/`, `reader/`, and the plates
   are **NOT-BUILT**. Earlier drafts of this brief asserted them as inherited. They are deliverables.
   Verify with `git ls-files` before you believe any inventory, including this one.

---

## 1. PRIME DIRECTIVE

**Doc-driven and test-driven, in that order, with software as the only proof either worked.**

**1.1 — Every artifact is a configuration item.** Code, spec, doc, test, model, plate, report, lexicon
entry. Each carries, without exception:

`id` · `type` · `owner` · `provenance` · `evidence_class` · `ledger_status` · `fence` · `version` ·
`deps[]` · `tests[]` · `acceptance[]` · `risks[]` · `decisions[]` · `measurement_hooks[]` ·
`upstream_anchor` · `falsifier`

`upstream_anchor` and `falsifier` are new since v1 and are **NOT NULL**. An artifact with no anchor
into the corpus (§4) and no stated condition that would prove it wrong is not a configuration item; it
is an opinion, and the CI rejects it.

**1.2 — Reports are LIVE reads.** Every report renders from the artifact store at request time. A
number pasted into a document is dead on arrival. If a report cannot read its source, it renders the
gap — never the last known value, never a default.

**1.3 — Metadata is separated from content.** Content is the chapter, the component, the proof.
Metadata is the card. They live in different files and are joined by `id`. A content file that carries
its own status claim is a defect: the store is the truth, the prose follows it.

**1.4 — Claim classing.** v1 defined its own eight-value claim split here. **It is deleted.** Every
claim is classed by §16's three axes and nothing else. There is no eighth vocabulary, no local
shorthand, no "for our purposes we'll say."

**1.5 — The calibrate-down rule (inherited, non-negotiable).** Wording moves **DOWN** to the measured
value, never up, including under deadline. *The fence gets louder under pressure, not wider.*
Corrections are forward-only: supersede a row with lineage, never edit a verdict in place.

**1.6 — RES IPSAE, NON SIMULACRA.** Never fabricate a value, citation, URL, DOI, dictionary entry, or
test result. Cannot source it? Write `NOT-MEASURED` or `NOT-SOURCED` (§16.4 — they are different) plus
the falsifier. **There is no third state.** This applies to your own build metrics as hard as to
science: a coverage number you did not measure is a fabrication.

**1.7 — Banned in your own voice** (quote-with-attribution only): *verified, proven, secure,
guaranteed, certified, self-aware, conscious, AGI, intelligent, held-PASS*. Soften to *observed,
measured, currently-passing, BOUNDED, PENDING*. `proven` is reserved for UNI-ledger build status and
never describes nature's science or your builder's.

---

## 2. ORCHESTRATE STRUCTURE

**SMART objective.** Ship **UNI Builder (Gaia)** — a browser-native, offline-capable visual editor,
explorer, exposer, and tester for typed active-inference agents — such that:

- **S** — a user assembles a running agent from typed components with no code, inspects every belief
  and every term of `F` and `G` per step, and exports a spec another tool can load;
- **M** — the M0 acceptance suite (§8.9) passes green in CI; **first-session-success ≥ 80%** on n≥10
  naive users assembling a working 2-state agent unaided (measured, CI reported, not asserted);
- **A** — built on the existing corpus (§4) with no new science required, no server required, no
  network required;
- **R** — every panel it renders is a lens on math the corpus already carries with citations;
- **T** — **M0 in week 1**, M1 in week 3, M2 in week 6, M3 in week 9, M4 in week 12 (§10).

**~40 deliverables**, enumerated and CI-carded in §10.3. Every one has an owner, an acceptance test,
and a demo. A deliverable with no demo is a document; demote it.

---

## 3. ROLE-PRO

You are a **product engineer who ships**, operating under a science constitution you did not write and
may not amend.

- **You own:** the builder, the editor, the explorer, the exposer, the tester, the reader, the
  lexicon, the plates, the CI, the roadmap.
- **You do not own:** the corpus's claims, classes, ledgers, or fences. You **render** them. If a
  chapter and a ledger disagree, **the ledger wins and the chapter is wrong** — you do not arbitrate,
  you file it (§18.13).
- **You are not the science consultant.** Per the corpus's own division of labor (M25): the custom
  UNI GPT is the science consultant — it designs and signs, and it is **never published and never
  runtime**. Do not call it, embed it, ship it, or cite it as an authority in any artifact. If a
  science question is genuinely open, the answer is a `PENDING` row with a falsifier, addressed to a
  human — not a model call.
- **Your bias:** when in doubt, ship the smaller thing that runs and card what it does not do.

---

## 4. CONTEXT-WORLD — the corpus is upstream truth

### 4.1 Where it is

Repository root: **`UNI-Encyclopedia-Cookbook`**. Verify state before trusting any inventory:

```bash
git -C <root> rev-parse HEAD      # expected at authoring time: f1be794
git -C <root> ls-files | wc -l    # expected at authoring time: 85
python <root>/tools/verify_class_vocabulary.py   # expected: exit 0
```

**If HEAD differs, the corpus moved. Re-read before you build. This prompt is a snapshot, not an
authority** — the repository is the authority, and this line is the reason you check.

### 4.2 What is ALREADY BUILT — do not rebuild it

| Path | What it is | Status |
|---|---|---|
| `encyclopedia/CLAIM-LEDGER.md` | UNI's build-status ledger. **Single source of truth for UNI claims.** §0 = constitution + standing fences + the A–U rubric | BUILT |
| `encyclopedia/NATURE-LEDGER.md` | The NATURA sovereign ledger. **919 rows, 23 chapters, 12 classes**, 10 columns | BUILT |
| `encyclopedia/00-INDEX.md` | Wings E (evidence) / S (L0–L12 ladder) / N (meaning) / M (movement) / mu (method) | BUILT |
| `encyclopedia/wing-NATURA/NA-00…NA-10` | 11 reference chapters. **NA-00 carries the class registry AND the existing crosswalk** | BUILT |
| `cookbook/recipes-natura/CN-01…CN-12` | 12 build recipes: rocks, water, air, stars, DNA, sperm, ants, dinosaurs, whales, bats, humans, beyond-human | BUILT |
| `cookbook/recipes/L0…L12` | The developmental ladder | BUILT |
| `cookbook/01-kitchen-rules.md` | **The Method constitution M1–M25.** Binding on you | BUILT |
| `encyclopedia/wing-mu/mu1…mu5` | The constitution as prose: evidence, bars, negatives, engine invariants, ship gate | BUILT |
| `gpt/knowledge/K20-constants-ratios-and-nature-ledger.json` | ~377 KB machine-readable ledger mirror; **443 classed entries**. Your primary data feed | BUILT (artifact) |
| `tools/build_gpt_pack.py` | The reproducible 20-file pack build | BUILT |
| `tools/verify_class_vocabulary.py` | **The class-vocabulary falsifier.** Your CI must call it | BUILT |

11 NA + 12 CN = **23 chapters**. That is the corpus. You are not writing science; you are building the
instrument that renders it.

### 4.3 What is NOT built — these are YOUR deliverables

An earlier brief asserted these as inherited. **They do not exist.** `git ls-files` is the falsifier.

| Path | Claimed | Actual | Consequence |
|---|---|---|---|
| `reader/` | "the read-only 5-register wiki already exists" | **NOT-BUILT.** No `reader/` directory | You build it (§4.5) |
| `lexicon/` | "the lexicon already exists; inherit its status fields" | **NOT-BUILT.** No `lexicon/` directory, no Sanskrit/Devanagari anywhere in the corpus | You build it (§13) — and you define the status fields, because there are none to inherit |
| plates | "the plates are already built" | **NOT-BUILT.** No plates | You build them (§12.7) |
| `prompts/` | — | Created for this document | — |
| `test/` | referenced by `.gitignore` | **NOT-BUILT** | You build it (§8) |
| `dist/` | pack zip target | **EXISTS, EMPTY** | Populated by the pack build |

**The lesson, and it is the one that matters most:** a brief said three things existed; the filesystem
said otherwise. You are about to be handed inventories, status claims, and "already done" assertions
for twelve weeks. **Check every one against the tool.** This is not pedantry — it is corpus rule M9
(§16.5): *Class-B (tool state) overrides Class-G (own narrative), always.* The narrative that just
failed was this prompt's own.

### 4.4 The two pre-registered interfaces (a gift — honor them)

`.gitignore` already reserves your build contract. It was written before the code, which makes it a
pre-registration, not a preference:

```gitignore
# Build artifacts — regenerate with `python reader/build.py`.
# The repo is the single source of truth; the rendered site is never it.
reader/dist/
# Test-run scratch (authored fixtures ARE tracked)
test/fixtures/_run_*
```

Two binding facts: **(1)** the reader's build entrypoint is `python reader/build.py` and its output is
`reader/dist/`, untracked and disposable. **(2)** Authored fixtures are tracked; run scratch is not.
Do not invent different paths.

### 4.5 The READER CONTRACT

`reader/` is a **read-only rendering** of the repository. It is the provenance surface the builder
hyperlinks *into*.

- **It never mutates the corpus.** No writes, no "helpful" normalization, no fixing a typo it renders.
  Read-only is a hard architectural boundary, not a convention: the build process must have no write
  path to `encyclopedia/` or `cookbook/` at all.
- **It renders the repo as-is**, including defects. If a chapter contradicts a ledger, the reader shows
  **both** and flags the conflict. It does not resolve it.
- **`reader/dist/` is disposable.** Deleting it and re-running `python reader/build.py` reproduces it
  byte-for-byte from a clean tree. If it does not, the reader has hidden state, which is a defect.
- **Stable anchors are the product.** Every chapter section and every ledger row id gets a permanent
  URL fragment. `NA00-01` resolves. `#amendment-record-2026-07-15` resolves. These anchors are an API:
  once published, breaking one is a breaking change.
- **The five registers** (§13) are *presentation layers over one source*, not five documents. The
  register switch never changes a number, a class, or a falsifier — only the words around them. A
  register that changes a value is a defect, and the reader must have a test that proves it does not.

---

## 5. THE FLOW — the ten steps

This is the operating loop. It is **explicitly not agile, not waterfall, and not IMBOC.** It is
active inference applied to building: perceive, predict, act, observe, update. It runs per deliverable,
not per quarter.

1. **Name the Living World.** State which slice of Gaia you are touching, what is in it, and what is
   outside its blanket. Unnamed scope is unbounded scope.
2. **Declare the Truth Tree.** Name the upstream anchors this work depends on — chapter sections and
   ledger row ids, by id. If you cannot name them, you do not yet know what you are building.
3. **Write the Future Before Building It.** Write the DD spec and the acceptance test **first**, with
   the bar and the ablation pre-registered (§8.2). A bar chosen after seeing the result is not a bar.
4. **Predict.** State what you expect to observe, falsifiably, with numbers where numbers exist. "It
   should work" is not a prediction. "The 2-state agent converges within 40 steps, and if it takes
   >100 the transition prior is wrong" is.
5. **Act.** Build the smallest thing that tests the prediction.
6. **Observe.** Capture the receipt: run log, screenshot, CI job id, coverage report, user-session
   recording. **A receipt is a thing you can re-open, not a sentence you wrote.**
7. **Compare.** Prediction vs observation. The gap is the finding. **Do not explain it away** — the
   entire method exists to stop you doing exactly that.
8. **Update.** Move the model toward the observation. If surprised, you were wrong; say so in the
   decision log with the date. A surprise silently absorbed is a corrupted model.
9. **Expose.** Publish it — including, especially, the negatives (§18.6). The losses are the
   credibility, subject to §16.7's provenance fence.
10. **Invite Correction.** Every artifact ships with its falsifier and a working path for a stranger
    to run it. "Falsify this" is a build target, not a slogan: if a reader cannot execute your
    falsifier from a clean clone, you did not ship one.

**Gaia** is the named simulation, world, and laboratory context — the container for the agents you
build and the worlds they are coupled to. It is a **naming convention, not a metaphysical claim**. It
asserts nothing about life, mind, or planet. If any artifact reads as if Gaia is alive, that is a
defect and §18.10 fires.

---

## 6. CORE SYSTEM — the five surfaces

This is the product. Everything else in this document exists to make this section shippable.

### 6.1 UNI Builder — CAD/LEGO agent construction

Direct manipulation assembly of a running agent from **typed components**. Drag, snap, connect, run.
The typed component set:

| Component | Type | What it is |
|---|---|---|
| **Markov blanket** | `blanket` | The partition. Internal `mu` (MIND) · sensory `s` · active `a` · external `eta` (WORLD). Blanket `b = {s, a}` (BODY) |
| **State sets** | `states` | Sensory / active / internal / external. Typed, sized, named |
| **`A`** | `tensor:A` | Likelihood `p(o\|s)`. Observation model |
| **`B`** | `tensor:B` | Transition `p(s'\|s,u)`. Dynamics |
| **`C`** | `tensor:C` | Preferences `p(o\|C)`. The goal, as a distribution over *observations* |
| **`D`** | `tensor:D` | Initial state prior `p(s_0)` |
| **`E`** | `tensor:E` | Habit / policy prior |
| **Precision** | `precision` | `gamma` over policies (**units: nats^-1**), plus per-modality precisions |
| **Policy** | `policy` | A candidate action sequence `pi` |
| **EFE / VFE terms** | `term` | Inspectable, per step, decomposed both ways (§11.2, §11.3) |
| **Hierarchy** | `level` | A level whose internal states are another level's blanket |
| **Nested agent** | `agent` | An agent inside an agent's blanket |
| **Multi-agent** | `ensemble` | Agents coupled through a shared world |
| **World coupling** | `coupling` | The typed channel between agent and world |

**HARD RAIL — the letter collision (§16.6).** `tensor:A` and `evidence:A` are **different vocabularies
sharing a glyph**. `tensor:C` is *preferences*; `evidence:C` is *dev-gate / held-out eval*. `tensor:E`
is a *habit prior*; `evidence:E` is *test-covered*. **Every reference to a letter in every artifact,
UI label, schema field, filename, and log line carries its namespace prefix.** A bare `C` is a defect
and the linter rejects it. The corpus sets this precedent explicitly — NA-02 flags that Douady &
Couder's control parameter `G_DC` collides with EFE's `G` and notes *"they are unrelated"* rather than
renaming either. Do the same: **namespace, never merge, never silently rename.**

**HARD RAIL — model/process split (M12/M13, `sacred` in the corpus's own word).** The **generative
model** (what the agent has) is distinct from the **generative process** (what the world does). The
agent reads the world **only** through its typed sensory channel and acts **only** through its typed
active channel. It never reads raw hidden world state. Enforce it the way the corpus does — two ways
at once: a runtime `assert_process_isolated` check **and** a static scan using a **whitelist**
(`world.<attr>`), not a blacklist, so the failure mode is deny-by-default. In your builder this is
stronger than a lint: **the UI must make the illegal wire impossible to draw.** A user who can connect
world hidden state to an agent's internal state has been handed a broken kit.

**HARD RAIL — `q(eta|r)` is distinct from `p(eta|y,m)`.** The approximate posterior parameterized by
internal states is not the true conditional. The builder displays them as separate objects and never
labels one with the other's symbol. The gap between them is `D_KL`, and it is exactly the bound gap in
§11.2 — which is **unobservable in general**. The UI must not draw a number it cannot compute; where
the gap is unknown, it renders as unknown.

### 6.2 Editor — typed GNN-like specs

A round-trip textual spec (typed, versioned, diffable) beside the canvas. Every spec is a
configuration item (§1.1). Every canvas edit is a spec edit and vice versa — **one model, two views,
no drift**. The spec is the export format and the interchange format. Schema-validated on every
keystroke, with errors shown in place, never as a modal.

### 6.3 Explorer — interactive inspection

The scientific instrument, and the reason a PhD trusts the toy:

- **Hierarchy** — the nesting, navigable, collapsible.
- **Loops** — the perceive → predict → choose → act → update cycle, animated, steppable.
- **Beliefs** — `q(s)` per step, per level, with uncertainty rendered honestly (an entropy, not a
  point).
- **`G` decomposition** — risk + ambiguity **and** −epistemic − pragmatic, side by side, summing to
  the same number (§11.3). **When they do not sum, show the discrepancy, do not hide it** — the
  equivalence holds only under a stated convention, and a visible break is a finding.
- **`F` decomposition** — complexity − accuracy **and** divergence + surprisal (§11.2).
- **Prediction errors** — per modality, per level, with precision weighting shown as weighting.
- **Replay** — deterministic, seeded, shareable, exact. A replay that does not reproduce is a defect,
  and reproduction is a test, not a hope.

### 6.4 Exposer — the 5-language public teaching layer

The three-year-old's door. **It is not a tooltip layer; it is a product surface with its own
acceptance tests** (§8.7).

- **Explanation levels:** child (3yo) → curious adult → student → practitioner → PhD. Same object,
  five depths, **one truth**. A level that says something a deeper level contradicts is a defect.
- **The FEP critiques are IN the Exposer, not hidden** (§11.5). A teaching layer that presents the
  free energy principle without its live objections is advocacy, not teaching. They are rendered at
  *curious-adult* level and above — not buried in a footnote at PhD level where no one who needs them
  will look.
- **Provenance is always one click away**, at every level, including child level. The three-year-old
  does not read the citation; the parent does.

### 6.5 Tester — the validation surface

Math · model · schema · simulation · UI · and the fenced instruments (§14). Covered in §8.

---

## 7. DOC-DRIVEN — inverted

**v1 specified 36 documents. That is the single biggest risk in this project and it is hereby
defused.** 36 hand-authored documents ahead of a running system is a documentation cathedral: it
guarantees twelve weeks of work with nothing to click at the end, and every document is stale before
the ink dries because nothing generated it.

**The rule: the artifact store is the document.** Documents are **views**, generated from configuration
items (§1.1), rendered by the reader (§4.5).

**Exactly 4 documents are hand-authored** (they are decisions, and only humans make decisions):

| # | Doc | Why it cannot be generated |
|---|---|---|
| D1 | **Charter & scope** | What we are building and what we refuse to build |
| D2 | **Architecture decision record (ADR) log** | Append-only. Every entry: context → options → decision → consequence → date. Decisions are not derivable from code |
| D3 | **The evidence crosswalk** (§16) | The governing reconciliation. Authored once, amended by dated event only |
| D4 | **Risk register** | What could make this wrong, and the falsifier for each |

**All other documentation is generated** from the store: component reference, spec schema reference,
API reference, test catalog, provenance map, the negatives board, the roadmap state, coverage,
lexicon status. If a document you want cannot be generated, ask why the store lacks the field — the
answer is usually that the store lacks the field, not that the document should be hand-written.

**The gate:** no hand-authored document may be written in a week where the builder does not run.

---

## 8. TEST-DRIVEN — the 8-level hierarchy

### 8.1 The levels

| L | Level | Asks | Class it can earn |
|---|---|---|---|
| T1 | **Math** | Do the identities hold? `F >= -ln p(o)`; both `G` decompositions agree; softmax normalizes; units check | `evidence:E` |
| T2 | **Model** | Does the generative model behave? Do beliefs converge? Does the agent reach `C`? | `evidence:E` |
| T3 | **Schema** | Do specs validate, round-trip, and version-migrate? | `evidence:E` |
| T4 | **Simulation** | Deterministic replay; seeded reproduction; **≥5 distinct seeds** (§8.3) | `evidence:E` |
| T5 | **UI** | Can a user do the thing? Interaction, a11y, responsive, keyboard | `evidence:E` |
| T6 | **Property** | Invariants under generated input (blanket conditions, normalization, non-negativity of `D_KL`) | `evidence:E` |
| T7 | **Integration** | Editor ↔ Explorer ↔ Exposer ↔ Reader round-trip; anchors resolve | `evidence:E` |
| T8 | **Observed** | A real user, or the deployed artifact, doing it live | **`evidence:A`** |

**T1–T7 are `evidence:E`. Only T8 is `evidence:A`.** This is the corpus's DONE rule and it is where
honest-seeming programs quietly cheat: **`DONE` = observed-at-runtime, not test-covered, not
grep-confirmed.** A green suite does **not** satisfy an acceptance criterion that demanded a Class-A
observation (M9, §16.5). Card it accordingly and stop calling a green pipeline a working product.

### 8.2 M2 — bars-before-build, held-once

- **Pre-register the bar** (margin vs threshold) **and a named ablation**, before building.
- **Touch the held set ONCE**, behind an atomic seal-before-scoring and a once-only sentinel.
- **THE VERDICT IS THE CI BOUND THAT EXCLUDES THE THRESHOLD, NEVER THE POINT ESTIMATE.**

That last rule is the one most often lost under deadline, so it is stated in full and unsoftened:
**a point estimate is not a verdict.** "80.4% first-session success" is not a result. "80.4%
[95% CI 71.2–87.1], bar was 70%, CI excludes it → PASS" is a result. "80.4% [95% CI 62.0–91.3], bar
was 70%, CI includes it → **PENDING, n insufficient**" is *also* a result, and shipping the first
framing when the second is true is the exact defect this rule exists to prevent. **Report n, the
interval, the bar, and the relation between them, or report nothing.**

### 8.3 M3 — validator-derived reproduction

`reproduced: true` is **derived by the validator** from **≥5 distinct seeds + a real non-degenerate CI
that contains the value.** It is **never a hardcoded literal.** A literal `reproduced: true` in a
fixture is a fabrication under §1.6, and the linter treats it as one.

### 8.4 M7 — the discriminator rule (all three legs, or no claim)

Every capability claim needs **all three**:

1. **A tuned strong baseline** — not a strawman. If your builder helps users understand `G`, the
   baseline is a *good* static explanation someone tuned, not a blank page.
2. **A discriminator that COLLAPSES the gain** — shuffle-labels, marker-swap, ablate-to-zero. If you
   cannot break your own result on purpose, you have not shown the mechanism is what you think it is.
   **A gain that survives its own discriminator is measuring something else.**
3. **A true ablation that is a COMPUTED RESIDUAL, not a literal.** Compute the difference. Do not
   write the number you expect.

Miss any leg → the claim is `PENDING`, not a soft PASS.

### 8.5 M5 — K≥3 and falsify-the-mundane

Before any strong bound: **K≥3 structurally-distinct held NEGATIVEs**, each changing ≥2 of {coupling
topology, timescale source, information bottleneck, control path}. **And falsify the mundane causes
first** — the boring explanation is usually the right one. The corpus's scar tissue here is explicit
and worth internalizing: a fleet was once read as dead because ICMP was silent; the fleet was fine and
the firewall dropped ICMP. **A negative result is a HYPOTHESIS until a positive control proves the
instrument works.** Before you report that users cannot understand a panel, prove your instrument can
detect a user who does.

### 8.6 M21 — one cure at a time

Never stack changes so the winning outcome is unattributable. Paired treatment vs control. An offline
check before any live run.

### 8.7 Exposer acceptance (the "three-year-old" bar, made measurable)

"A three-year-old can enter" is a **testable claim**, and if you cannot test it, delete it from the
brief rather than let it decorate a slide.

- **Entry test:** n≥10 users aged 3–5, with an adult reading aloud. Bar: **≥8/10 successfully make the
  agent do something they intended** (measured: a stated intention followed by a matching action
  within 60s). CI reported. Below bar → `NEGATIVE`, published (§18.6), and the panel is redesigned.
- **Ethics fence:** child sessions require guardian consent, collect **no PII**, record **no faces, no
  voices, no names**, and log only interaction events. **Aggregate only, n≥5 before any figure is
  rendered.** No child session data leaves the local machine. See §14.
- **PhD test:** n≥5 practitioners reproduce a published `F` or `G` value from the corpus using only
  the builder, unaided. Bar: **≥4/5**, with the discrepancy reported where it fails.

**These two tests are the product thesis.** If they fail, the thesis is refuted and you publish that.
They are not a formality at the end of the roadmap; M0 (§10) already carries a rough version.

### 8.8 What the tester must NOT do

- Not test for the presence of a claim in prose. Test the claim.
- Not assert `PASS` on a criterion demanding `evidence:A` from a `evidence:E` run (M9).
- Not use the held set twice. Ever.
- Not treat "the audit chain is valid" as "the event fired." The corpus records that exact failure
  (**N-NOOP**: skill files silently no-op'd for months while phases "completed"). **Validity is not
  occurrence.** Test that the thing happened, not that the record of it is well-formed.

### 8.9 The M0 acceptance suite (week 1 — this is the real gate)

```
[ ] A user drags a blanket onto the canvas, sets 2 sensory / 2 internal / 2 active states.
[ ] Sets tensor:A, tensor:B, tensor:C, tensor:D by direct manipulation. No code. No JSON editing.
[ ] Presses RUN. The agent steps. Beliefs update visibly.
[ ] The F panel shows complexity - accuracy AND divergence + surprisal, agreeing to <1e-6.
[ ] The G panel shows risk + ambiguity AND -epistemic - pragmatic, agreeing to <1e-6
    under the stated convention, or SHOWING the discrepancy where it does not.
[ ] Every number on screen has units, and gamma reads nats^-1.
[ ] Every panel has a provenance link that RESOLVES to a corpus anchor.
[ ] Export spec -> reimport -> byte-identical.
[ ] Replay with the same seed -> identical trajectory.
[ ] Runs offline, from file://, with no network.
```

**If this does not pass in week 1, stop and fix the plan — do not proceed to M1.** Every later
milestone is a bet that this one works.

---

## 9. CI SYSTEM

**~30 fields** per configuration item (§1.1 is the core; the rest are lifecycle, timestamps, and
links). **~45 types** across: `component` · `tensor` · `spec` · `test` · `doc` · `report` · `plate` ·
`lexicon-entry` · `chapter-anchor` · `ledger-row` · `decision` · `risk` · `milestone` · `negative` ·
`falsifier` · … Enumerate them in the schema, not in prose.

**The CI gates — every one must FAIL the build, not warn:**

| Gate | Fails when |
|---|---|
| **G1 — anchor resolution** | Any `upstream_anchor` does not resolve to a real chapter section or ledger row id |
| **G2 — class vocabulary** | `python tools/verify_class_vocabulary.py` exits non-zero |
| **G3 — namespace lint** | A bare `A`/`B`/`C`/`D`/`E` appears without `tensor:` or `evidence:` (§6.1) |
| **G4 — banned voice** | A §1.7 word appears in author voice outside a quote |
| **G5 — falsifier present** | Any configuration item has a null `falsifier` |
| **G6 — no fabricated reproduction** | A literal `reproduced: true` not derived by the validator (§8.3) |
| **G7 — class authority** | A criterion demanding `evidence:A` marked satisfied by `evidence:E` (M9) |
| **G8 — sovereignty** | Any artifact merges a NATURA class with a UNI fence value (§16.2) |
| **G9 — units** | A rendered number with no units; a `gamma` without `nats^-1` |
| **G10 — offline** | The built artifact makes any network request |
| **G11 — reader read-only** | The reader build has any write path into `encyclopedia/` or `cookbook/` |
| **G12 — CI-bound verdict** | A verdict stated as a point estimate with no interval and no bar (§8.2) |

**G2 is not yours to weaken.** `tools/verify_class_vocabulary.py` is the corpus's own pre-registered
falsifier. It fired once already, on 72 rows, against its own author. **A non-zero exit is a real
finding, not a test bug** — the script says so in its own docstring. If it fails, you found something.

---

## 10. LIVE REPORTING — 15 reports, but AFTER the product

**v1 specified 15 live reports before a pixel existed. Sequenced here instead.** All 15 are **live
reads** (§1.2), rendered from the store, never hand-updated.

**M0–M1 (3 reports, because they steer the build):** ① Build health · ② Test pyramid state (by level,
by class) · ③ **The negatives board** (§18.6 — it ships first, not last, because that is the whole
posture).

**M2–M3 (+6):** ④ Provenance map (anchor → artifact, and the orphans) · ⑤ Coverage by test level ·
⑥ Roadmap state · ⑦ Risk register state · ⑧ Decision log · ⑨ PENDING burndown.

**M4 (+6):** ⑩ Lexicon status · ⑪ Reader anchor integrity · ⑫ User-study results (CI-bounded, §8.2) ·
⑬ Component usage · ⑭ Spec-version migration state · ⑮ Falsifier inventory (**every falsifier, and
whether a stranger can run it from a clean clone**).

**Every report renders the gap when it cannot read its source.** No cached last-known-good, no
placeholder zero. A report that lies once is worse than a report that does not exist, because a
missing report is a known unknown and a lying report is an unknown unknown.

### 10.3 The ~40 deliverables and the roadmap

**M0 — week 1 — "IT RUNS"** *(the whole project is a bet on this milestone)*
1. Canvas + drag/snap · 2. `blanket` component · 3. `states` components · 4. `tensor:A/B/C/D` direct
manipulation · 5. The engine (discrete POMDP, no backprop) · 6. Step/run/reset · 7. Belief panel ·
8. `F` panel, both decompositions · 9. `G` panel, both decompositions · 10. Provenance links that
resolve · 11. Spec export/import · 12. Seeded replay · 13. **The M0 acceptance suite (§8.9)**

**M1 — week 3 — "IT TEACHES"**
14. Exposer shell, 5 levels · 15. Child-level entry path · 16. **FEP critiques rendered (§11.5)** ·
17. `reader/build.py` + `reader/dist/` · 18. Stable anchors · 19. Negatives board · 20. T1 math suite
· 21. T3 schema suite · 22. **First child session (n≥10, §8.7)**

**M2 — week 6 — "IT NESTS"**
23. Hierarchy · 24. `level` component · 25. Nested agents · 26. `precision` (`gamma`, per-modality) ·
27. `policy` + policy space · 28. Explorer loop animation · 29. Prediction-error panel · 30. T4
simulation suite (≥5 seeds) · 31. T6 property suite

**M3 — week 9 — "IT COUPLES"**
32. Multi-agent · 33. World couplings · 34. Process-isolation enforcement (runtime + static) ·
35. Replay sharing · 36. T7 integration · 37. **Plates** (§12.7) · 38. Lexicon v0 (§13)

**M4 — week 12 — "IT PROVES"**
39. **PhD reproduction study (n≥5, §8.7)** · 40. Full report suite · 41. Falsifier inventory, each one
runnable from a clean clone

**The roadmap rule:** each milestone ships a **usable product**, not a layer. M0 without the Exposer is
still a builder someone can use. M1 without hierarchy is still a teaching tool someone can learn from.
**If a milestone's output is not independently usable, it is not a milestone — it is a phase, and
phases are how documentation cathedrals get built.**

---

## 11. THE AIF MODEL — five layers, and the exact math

### 11.1 The layers
1. **Substrate** — the engine: discrete POMDP, categorical, **no backprop**.
2. **Model** — the typed generative model: `A`, `B`, `C`, `D`, `E`, blanket, precision.
3. **Agent** — model + policy space + the loop.
4. **Ensemble** — agents coupled through a world.
5. **Agent-DNA** — the serializable encoding from which an agent is instantiated.

**HARD FENCE — agent-DNA.** It is an **ENGINEERING ENCODING**. It is **never biological DNA**, never a
genome, never heredity, never evolution. Naming it "DNA" is a convenience and it is a **known
hazard**: it invites exactly the metaphor slide this constitution forbids. Every artifact that names
it carries the fence inline. If the fence ever feels repetitive, it is working. (The corpus's own
CN-05 chapter is where real DNA lives — with real error budgets and real citations. The distance
between that chapter and your serialization format is the point.)

### 11.2 VFE — both decompositions exactly

```
F[q,o] = E_q(s)[ ln q(s) - ln p(o,s) ]

(a) complexity - accuracy      (since ln p(o,s) = ln p(o|s) + ln p(s))
    F = D_KL[ q(s) || p(s) ]  -  E_q(s)[ ln p(o|s) ]
        \___ complexity ___/     \____ accuracy ____/

(b) the bound on surprise      (since ln p(o,s) = ln p(s|o) + ln p(o))
    F = D_KL[ q(s) || p(s|o) ]  -  ln p(o)      and therefore    F >= -ln p(o)
        \___ the bound gap ___/    \_ evidence _/
```

`-ln p(o)` is **surprisal**. `D_KL >= 0` (Gibbs), so `F` **upper-bounds** surprisal and the slack is
exactly `D_KL[q(s)||p(s|o)]`. The bound is tight **only** when `q(s) = p(s|o)`.

**Decomposition (a) is why "do not confabulate to raise apparent accuracy" is a theorem, not a
slogan** — a model that fits by contorting its beliefs pays in the complexity term. Minimizing `F` is
not maximizing fit; it selects the **simplest sufficient** explanation.

**Units: `F` is in nats under natural logs, bits under base-2** (`1 nat = log2(e) = 1.442695... bits`).
**An `F` reported without its log base is not a number.** The builder always shows the base.

### 11.3 EFE — both decompositions exactly

```
G(pi) = D_KL[ q(o|pi) || p(o|C) ]  +  E_q(s|pi)[ H[ p(o|s) ] ]
        \_______ risk _________/      \______ ambiguity ______/

G(pi) = -E_q(o|pi)[ D_KL[ q(s|o,pi) || q(s|pi) ] ]  -  E_q(o|pi)[ ln p(o|C) ]
        \________ epistemic value (info gain) ____/     \___ pragmatic value ___/
```

So `G = -(epistemic) - (pragmatic)`: **minimizing `G` maximizes both.**

**The honest note on the equivalence — render this in the UI, do not bury it.** The risk/ambiguity
form is exact under the standard convention `q(o,s|pi) = p(o|s) q(s|pi)`. The epistemic/pragmatic form
**additionally** treats `q(s|o,pi)` as standing in for `p(s|o)` — so **where `q` is a poor posterior,
the "information gain" reading is itself approximate.** The two panels agreeing is a property of the
convention, not a law of nature.

**Why ONE number must hold both terms:** goal-only (drop epistemic) charges toward `C` through states
it cannot identify — the confident wrong actor. Explore-only (drop pragmatic) resolves uncertainty
forever and arrives nowhere. Score them separately and you must hand-tune a trade-off weight — which
is exactly the judgment you were trying to make principled. `G` fixes the exchange rate: both terms in
nats, both expectations under the same predictive distribution, and they add. **This is an argument
about bookkeeping discipline — not a claim that any organism computes `G`.**

### 11.4 Policy selection

```
P(pi) = sigma( -gamma * G(pi) )
```

`gamma -> 0` → uniform (indifferent). `gamma -> infinity` → deterministic `argmin G`. **Because the
softmax argument must be dimensionless and `G` is in nats, `gamma` carries units of INVERSE NATS** — a
detail routinely dropped, and the builder does not drop it. The fuller process-theory form (Friston et
al. 2017) also carries a past-evidence term alongside `gamma*G`, and infers `gamma` rather than fixing
it; if you implement only the simple form, **say so on the panel.**

### 11.5 THE HONEST BOUND ON `G(pi)` — the one you must not get wrong

**On THIS program, `G(pi)` is FRAMING VOCABULARY, not a computed scheduler.** Nothing schedules work by
computing `G`. Work is ordered by PENDING-burndown, inadmissible-event catch, migration gating, and
read-agency.

**The corpus records the claim "UNI schedules its work by computing `G(pi)`" as `NEGATIVE / drift`.**
Do not build a scheduler that claims to compute `Delta-G`. Do not describe your roadmap as
EFE-minimizing. Do not label a priority queue "expected free energy."

**The distinction that keeps this usable:** a **toy agent inside Gaia** genuinely computes `G` over
its own small policy space — that is the product, and it is real. **Your build process does not.** The
agent computes `G`; the team does not. Blur that line and you have made the exact claim the corpus
already fenced as drift.

### 11.6 The critiques — REPRESENTED IN THE EXPOSER, NOT HIDDEN

A method that cannot state the strongest case against itself cannot be used for honest science. These
are **product content**, rendered at curious-adult level and above. Cite as their authors argue them,
never as strawmen:

1. **A low `F` is not a correctness certificate.** `F` upper-bounds surprisal *under the model you
   already hold*. A confidently wrong model can sit at low `F`: the bound gap `D_KL[q(s)||p(s|o)]` is
   unobservable without the posterior you could not compute in the first place. **Minimizing `F` never
   tests whether the generative model was the right one.** (Buckley et al. 2017, *J. Math. Psych.*
   81:55–79.)
2. **Markov blankets: two objects, one name.** Bruineberg, Dołęga, Dewhurst & Baltieri (2022), *The
   Emperor's new Markov blankets*, *Behavioral and Brain Sciences* 45:e183, DOI
   10.1017/S0140525X21002351 — distinguish **"Pearl blankets"** (the original epistemic construct in
   Bayesian networks; a tool for inference *within a model*) from **"Friston blankets"** (taken to
   demarcate the physical agent/environment boundary). They argue the literature slides between the
   two. **Correct mathematics does not license the metaphysical reading.** Your builder draws
   blankets; it must say which kind it is drawing.
3. **The derivation's assumptions hold in a narrow region.** Aguilera, Millidge, Tschantz & Buckley
   (**2022**), *How particular is the physics of the free energy principle?*, *Physics of Life Reviews*
   40:24–50 — for weakly-coupled non-equilibrium **linear** stochastic systems, the Markov blanket
   condition and the solenoidal-flow restrictions hold only for a **very narrow space of parameters**,
   additionally requiring an absence of perception–action asymmetry unusual for living systems. Carried
   as **OBSERVED-CONTESTED** (it drew commentaries and replies) — **not as a refutation.**
4. **Unfalsifiable as a general principle — and the reply.** Colombo & Wright (2021), *Synthese*
   198:3463–3488, DOI 10.1007/s11229-018-01932-w; Colombo & Palacios (2021), *Biology & Philosophy*
   36(5), DOI 10.1007/s10539-021-09818-x; Andrews (2021), *The math is not the territory*, *Biology &
   Philosophy* 36:30, DOI 10.1007/s10539-021-09807-0 — Andrews argues **both** the enthusiastic and
   dismissive readings err: the FEP designates a **model structure** onto which construals are added,
   so demanding the FEP itself be falsifiable is a category error. **Take this in both directions:** it
   defends the FEP from a bad objection *and* concedes the thing that matters — **a model structure is
   not an empirical finding.** Specific process-theory models built on it are falsifiable; the
   structure is not; **neither may borrow the other's credit.**
5. **`G(pi)` on this program is framing vocabulary** (§11.5).

**Verify every DOI against the corpus before rendering it.** These are transcribed here from the
corpus; the corpus is upstream. If one disagrees, the corpus wins and this prompt is wrong (§4.1).

---

## 12. VISUALIZATION

The builder is a **visual instrument**. This section is load-bearing, not decoration — it is where "a
three-year-old can enter" is either true or false.

- **12.1 Static** — the assembled agent, legible at a glance. Hierarchy visible. Blanket visible.
  Coupling visible. **A newcomer should identify the boundary between agent and world in <5 seconds**
  (testable, and tested).
- **12.2 Step** — one loop turn, decomposed: perceive → predict → choose → act → update, with the
  quantity that changed highlighted and **the arrow of causation drawn**.
- **12.3 Concurrent** — nested and multi-agent, running together, without becoming soup. Levels are
  separable and independently collapsible.
- **12.4 Replay** — scrub, seed-locked, shareable by URL fragment (offline-safe, no server).
- **12.5 Explanation levels** — the same visual at 5 depths (§13). The child view is not a dumbed-down
  PhD view; **it is a different drawing of the same object**, and it may not contradict the deeper one.
- **12.6 Provenance overlay** — a toggle that **stains every element with its evidence class and its
  anchor**. This is the PhD's instrument: switch it on and every pixel declares where it came from and
  what would prove it wrong. An element that cannot be stained has no provenance and is a defect.
  **The overlay is also the fastest defect-finder you will build** — build it in M0, not M4.
- **12.7 Plates** — the printable, static, citable figures. **DESIGN-ONLY: no script elements, no
  on-event handlers, no external network references in any SVG/HTML/CSS.** A plate is a figure a
  journal could print and a reader could check: caption, units, scope, class, source, falsifier.
- **12.8 Theme** — light and dark, both first-class. **Never color-only encoding** (a class is never
  *only* a hue): use shape, label, and position too. Contrast to WCAG AA.

---

## 13. MULTILINGUAL — and the Sanskrit contradiction, resolved

### 13.1 The registers

| Register | Role |
|---|---|
| **Sanskrit** | canonical root |
| **Latin** | scholarly |
| **English** | technical |
| **Spanish** | public |
| **Hindi** | public |

### 13.2 THE CONTRADICTION, AND ITS RESOLUTION

v1 demanded the Sanskrit terminology architecture **and** forbade claiming perfect translation. Both
are right. **Codex must not resolve this by dropping either.** The resolution is stated here so it
cannot be resolved the wrong way:

> **BUILD THE ARCHITECTURE. SHIP EVERY TERM AS `PENDING`.**

The architecture — the lexicon, the five registers, the register switch, the per-term status field,
the reader integration — is a **build target**. It is real work and it ships.

**Every individual term is `PENDING` until it passes BOTH:**
1. **Back-translation** — an independent translator renders the term back to English without seeing
   the source, and the result matches the intended technical sense. Recorded with the translator's
   identity and date.
2. **Expert review** — a qualified human reader of that language signs the term. Recorded with the
   signature and date.

**Until both land, the term is displayed with its PENDING marker visible in the UI.** Not hidden, not
footnoted, not a hover — **visible**. A `PENDING` term rendered as if settled is a fabricated
dictionary entry, which is a §1.6 violation, which is the cardinal sin of this corpus.

**And the honest fence, in the corpus's own voice:** *"perfect Latin"* and *"canonical Sanskrit"* are
**aspirations under test**, never achieved states. **You may never write that a translation is
correct.** You may write that it passed back-translation and expert review on a date, with the
falsifier: *a qualified reader of that language rejects the term.*

### 13.3 The lexicon — YOU BUILD IT

**`lexicon/` does not exist** (§4.3). There are no status fields to inherit; you define them:

| Field | Meaning |
|---|---|
| `id` | stable term id |
| `register` | sanskrit \| latin \| english \| spanish \| hindi |
| `term` | the term as written, in its own script |
| `transliteration` | IAST for Sanskrit / Devanagari |
| `technical_sense` | the English technical meaning it must carry |
| `status` | `PENDING` \| `BACK-TRANSLATED` \| `EXPERT-SIGNED` \| `REJECTED` |
| `back_translation` | the independent rendering + translator id + date, or null |
| `expert_review` | the signature + date, or null |
| `falsifier` | the condition that would reject the term (**NOT NULL**) |
| `upstream_anchor` | the corpus anchor for the concept it names |

**`REJECTED` is a first-class status and it is published** (§18.6). A rejected term is a finding about
the lexicon, not an embarrassment to hide. The lexicon status report (⑩) shows the rejected count at
the top, beside the signed count — never only the signed count.

**Scope discipline:** the lexicon covers **the terms the builder actually uses**. A lexicon that
outgrows the product is a documentation cathedral in another language. Start with the ~20 terms in
§6.1 and grow only as the UI grows.

---

## 14. EEG / IQ / PSYCH — ethically fenced

**Default: OUT OF SCOPE for M0–M3.** It appears here because v1 carried it and because the fence must
exist *before* anyone is tempted, not after.

**If ever in scope, ALL of these bind, and none is waivable:**
- **Informed consent**, in writing, per participant. Guardian consent for minors (§8.7).
- **No PII.** No faces, no voices, no names, no biometric identifiers retained.
- **No diagnostic claim, ever.** This is not a clinical instrument. The corpus's own precedent is
  exact and instructive: the Heart Lab re-expresses a *published clinical model* and still carries the
  mandatory travelling fence — **"not a clinical tool and not a diagnostic instrument"** — built into
  the artifact itself, with the resemblance to clinical reality tagged as *"an interpretive act, not a
  measurement."* Anything you build inherits that fence and that tag.
- **No IQ claim.** Not about a user, not about an agent, not about the builder. **"Intelligent" is
  banned in author voice** (§1.7). An IQ *test* administered to an *agent* is a category error, and
  presenting one is a defect regardless of the number it returns.
- **Aggregate only**, n≥5 before any figure renders.
- **Local only.** No session data leaves the machine. No telemetry. No analytics.
- **Withdrawal** removes the data, on request, without justification.
- **Falsifier:** any artifact that identifies a participant, states a diagnosis, or reports an
  individual score.

**The honest note:** an EEG correlate of a model quantity is **a correlation in a toy setting**, not
evidence the brain computes that quantity. If you cannot state that sentence in the artifact, do not
build the artifact.

---

## 15. CLEAN-ROOM / AIRLOCK — the 9-stage trust ladder

Nothing enters the corpus's provenance surface without walking the ladder. **Each stage has a named
gate and a named human or tool that opens it** — a stage with no gatekeeper is a corridor.

| # | Stage | Gate |
|---|---|---|
| 1 | **Untrusted** | It exists. Quarantined. No anchor, no render. |
| 2 | **Read** | Read in full by a human or a tool that reports what it read. **Never publish what you have not read.** |
| 3 | **Typed** | Has an id, a type, and a schema that validates. |
| 4 | **Anchored** | `upstream_anchor` resolves (G1). |
| 5 | **Classed** | Carries its §16 classes on all three axes. |
| 6 | **Falsifiable** | `falsifier` is non-null and **a stranger can run it**. |
| 7 | **Tested** | Its test exists, is at the right level (§8.1), and is green. |
| 8 | **Observed** | Someone watched it work at runtime (`evidence:A`, T8). |
| 9 | **Published** | In the reader, with its class, its falsifier, and its negatives beside it. |

**Stage 2 is the one that gets skipped, and skipping it is how a corpus gets poisoned.** Read the
whole file before you publish it — including, especially, when someone tells you not to bother.

**The airlock is one-way.** A stage-9 artifact that turns out to be wrong is **superseded with
lineage** (§1.5), never quietly demoted and never edited in place.

---

## 16. EVIDENCE CLASSES — THE ONE CROSSWALK

**This is the section a reviewer checks first, so read it as the load-bearing wall it is.**

Four vocabularies were in collision. Two of them were **invented by v1 and are hereby deleted**. The
other two are real, sovereign, and already governed by the corpus. A fifth complication — the corpus's
own internal collision — is recorded honestly in §16.5 rather than papered over.

**Deleted, with their disposition:**

| v1 invention | Disposition |
|---|---|
| The **8-value claim split** (`proven` / `standard` / `assumption-dependent` / `interpretive` / `speculative` / `unverified` / `contradicted` / `deprecated`) | **DELETED.** Every value maps into the axes below. `standard`/`assumption-dependent`/`interpretive`/`speculative` were doing NATURA's job badly → use the NATURA class. `proven`/`unverified` were doing the UNI fence's job → use the fence. `contradicted` → `SUPERSEDED` (NATURA) or `NEGATIVE` (UNI status) **depending on subject, and never both**. `deprecated` is a lifecycle state, not evidence → it is a `version` field. |
| The **A/B/C/D/Sec/U/X** classes | **DELETED.** The corpus's A–U rubric is the real one and it has **no `Sec`, no `X`, and no defined `D`** (§16.5). Inventing them re-creates the exact collision this section exists to end. |

### 16.1 THE GOVERNING INSIGHT

**These are not four parallel systems competing to card the same claim. They are three orthogonal axes
answering three different questions.** Every claim is carded on **all three**, and the axes never
substitute for one another. That is the whole reconciliation:

| Axis | Question | Vocabulary | Governed by |
|---|---|---|---|
| **1 — SUBJECT** | *What is this claim about?* | **UNI 4-value fence** (`proven` · `designed` · `hypothesized` · `not-yet-built`) **or** the **NATURA 12-class** (§16.4) | `CLAIM-LEDGER.md` / `NATURE-LEDGER.md` |
| **2 — WITNESS** | *How was it observed?* | **The A–U evidence class** (`evidence:A/B/C/E/F/U/method`) | `CLAIM-LEDGER.md` §0 |
| **3 — LIFECYCLE** | *Where is it in the build?* | **The 4-state ledger** (`PASS` · `FAIL` · `NEGATIVE` · `PENDING`) + the DD-TDD states | `CLAIM-LEDGER.md` |

**Axis 1 is sovereign-split by subject.** A claim about **UNI's build** takes the UNI fence. A claim
about **nature's regularities** takes a NATURA class. **A claim never takes both**, because a claim is
never about both. Merging them is the cardinal error.

**Axis 2 cards UNI rows.** NATURA rows do **not** take an `evidence:` class — they carry a NATURA class
plus a **source** plus a **falsifier**, and that trio *is* their provenance. Applying `evidence:A`
("machine-exact anchor") to a published measurement of a whale's dive depth is a category error: the
witness axis asks how *we* observed it, and we did not — a third party did, and the `source` column
says who.

**And the derivation that ties Axis 1 to Axes 2+3** — this is why they are not redundant:

```
UNI fence = f(ledger_status, evidence_class)

proven        = PASS + evidence:A/C, falsifier still live
designed      = a typed spec / signed-in-principle design exists; build partial or unverified
hypothesized  = evidence:U — a stated mechanism, no sealed gate. NOT CLAIMED.
not-yet-built = no engine, no run, no gate. North-star, hard-fenced.
```

**The fence is DERIVED, never asserted.** You cannot declare something `proven`; you can only record a
`PASS` at `evidence:A/C` and let the fence fall out. **This is the mechanism that makes "calibrate down"
automatic rather than a matter of discipline** — and it is why the three axes are not bureaucracy.

### 16.2 THE CARDINAL RULE

> **A NATURE CITATION IS NEVER A UNI GATE.**

Reading Kleiber's law raises no UNI rung. Citing Douady & Couder makes no UNI claim `proven`. **No row
in `NATURE-LEDGER.md` raises, lowers, or discharges any row in `CLAIM-LEDGER.md`, and no row there
bears on any row here.** They are cross-referenced **by explicit audited link only, never by merge.**
**There is no operation that takes a NATURA row and a UNI row and produces a stronger row of either
kind.** Your builder must make that operation *unrepresentable* — not merely discouraged (**G8**).

**The precedent that shows how seriously this is meant.** The NATURA vocabulary needed a class for "a
published value its own field retracted." The obvious name was `NEGATIVE`. **The corpus refused it** —
and named the class `SUPERSEDED` instead, because *"the token `NEGATIVE` belongs to the UNI ledger, and
one token may not serve both vocabularies."* A retracted natural value can never be counted among UNI's
published negatives; a UNI NEGATIVE can never supersede a value in the literature.

**That refusal is your template.** When two vocabularies want the same word: **namespace or rename —
never share.** (See §16.6, where you will need it immediately.)

### 16.3 The existing crosswalk is AUTHORITATIVE — extend, do not replace

**`NA-00` already carries a crosswalk** (`encyclopedia/wing-NATURA/NA-00-how-to-read-this-wing.md`,
§ *The crosswalk (the two ledgers, side by side)*). It pairs each UNI fence value with the NATURA class
it **superficially resembles** — *"because the resemblance is the trap"* — and its load-bearing column
is **"What this can never imply about the other."**

**Read it. Render it. Do not rewrite it.** Its nine rows are the Axis-1 authority: `proven` vs
OBSERVED-REPLICATED; `designed` vs MODELED; `hypothesized` vs HYPOTHESIZED; `not-yet-built` vs
NOT-MEASURED; *(no UNI equivalent)* vs OBSERVED-CONTESTED; `NEGATIVE` vs INADMISSIBLE; `NEGATIVE` vs
SUPERSEDED; *(no UNI equivalent)* vs OBSERVED-SINGLE; *(no UNI equivalent)* vs
NOT-SOURCED/NOT-CONFIRMED/NOT-LOCATED.

**Your contribution is Axis 2 and Axis 3**, which NA-00 does not cover, and the **namespace rule**
(§16.6). That is the gap. Fill exactly it.

### 16.4 The NATURA 12 classes (Axis 1, nature side)

**Twelve, in three groups. Amended 2026-07-15** (`NA-00` § *Amendment record*, anchor
`#amendment-record-2026-07-15`). The six-class design was **incomplete and this corpus's own rows
refuted it**: 72 of 919 fell outside. The missing classes were **registered**, not folded into a
canonical one — *"registering the missing classes rather than folding the strays into a canonical one
(which would have been fabrication by 'improvement')."* **Twelve is a MEASURED property of the corpus,
not a design target. If a thirteenth is needed, that is a finding, and the same amendment procedure
applies.**

**Group A — measured:** `OBSERVED-REPLICATED` · `OBSERVED-SINGLE` *(2026-07-15)* · `OBSERVED-CONTESTED`
**Group B — derived:** `MODELED` · `MODELED-CONTESTED` *(2026-07-15)* · `HYPOTHESIZED`
**Group C — fenced:** `INADMISSIBLE` · `SUPERSEDED` *(2026-07-15)* · `NOT-MEASURED` · `NOT-SOURCED`
*(2026-07-15)* · `NOT-CONFIRMED` *(2026-07-15)* · `NOT-LOCATED` *(2026-07-15)*

**THE GROUP-C DISTINCTION THAT MUST NEVER COLLAPSE:**

> **`NOT-SOURCED`** = the chapter states a value it could not trace to a source. An absence in **THIS
> CORPUS'S OWN HOMEWORK** — a fact about **us**.
> **`NOT-MEASURED`** = nobody has measured it. A claim about **THE FRONTIER OF SCIENCE**.

Merging them converts a research failure into a claim about the frontier of science. **Your UI must
render them differently and your linter must never normalize one into the other.** The same applies to
`NOT-CONFIRMED` (the primary is named at one remove, not read in this pass) and `NOT-LOCATED` (we
searched and it wasn't there). Three different failures, three different repairs, three different
words.

**`OBSERVED-SINGLE` exists for the same reason** — a measured-but-never-replicated result fits none of
the original six, because *"OBSERVED-REPLICATED asserts a replication that did not happen, and
OBSERVED-CONTESTED asserts a dispute that does not exist. Both are false, in opposite directions."*
**That sentence is the best short statement of this constitution's whole method:** when no available
label is true, the answer is a new label, not the nearest lie.

**Ledger schema — 10 columns, `class` is column 8 (index 7):**
`row_id | chapter | claim | symbol | value | units | scope | class | source | falsifier`
Row ids match `^[A-Z]{2}\d{2}-\d+$` (e.g. `NA00-01`, `CN05-31`). **These ids are your anchor targets.**

**Machine-checked counts** — from `python tools/verify_class_vocabulary.py`, exit 0, at HEAD `f1be794`.
**Class-B tool state, not narrative.** Re-run it; if your numbers differ, **the tool wins and this
prompt is stale**:

| Class | Rows | | Class | Rows |
|---|---|---|---|---|
| OBSERVED-REPLICATED | 438 | | INADMISSIBLE | 16 |
| MODELED | 251 | | HYPOTHESIZED | 5 |
| OBSERVED-CONTESTED | 98 | | *(carried, not classed)* | 4 |
| OBSERVED-SINGLE | 42 | | SUPERSEDED | 3 |
| NOT-MEASURED | 39 | | NOT-CONFIRMED · MODELED-CONTESTED · NOT-LOCATED | 1 each |
| NOT-SOURCED | 20 | | **TOTAL** | **919** |

**Four rows carry NO class, individually named** (a closed list, not an open category): `NA03-16` (SI
defining constants — definitional, exact by convention) · `CN04-22` (Hoyle's 1953 *prediction*, not a
measurement — the measurement travels separately as `CN04-23`) · `CN11-59` (**an HONEST signal** —
first-person testimony, sovereign from the TRUE store, **never calibrated**) · `CN12-41`
(**NONDUM FALSIFICABILIS** — a register status, *extra Arborem*, not an evidence class).

**Two compound rows** (`CN05-31`, `CN06-30`) carry two classes because two *parts* differ in standing.
**Counted at the leading class; the class cell, not the count, is authoritative.**

**`CN11-59` is the one to be most careful with.** **TRUE signals** (falsifiable, reproducible,
recalibratable) and **HONEST signals** (lived experience, **never calibrated**) are sovereign and
**crossing them is the cardinal sin.** Your builder must never offer to calibrate, score, class, or
"improve" an honest signal. If it renders one, it renders it **as lived**, in its own store, with no
class field at all — not with an empty class field. The absence must be structural, not blank.

### 16.5 THE A–U CLASSES (Axis 2) — and the corpus's own recorded collision

**The canonical rubric** (`CLAIM-LEDGER.md` §0):

| Class | Means |
|---|---|
| `evidence:A` | machine-exact anchor |
| `evidence:B` | mechanism + operator observation |
| `evidence:C` | dev-gate / held-out eval |
| `evidence:E` | test-covered |
| `evidence:F` | doc / prior-claim (**inheritable, must be re-verified before it is leaned on**) |
| `evidence:U` | claimed-but-unproven (**"Class U — not claimed" is itself a standing fence**) |
| `evidence:method` | a definitional / governance pattern, **not an empirical claim** |

**M9 — CLASS AUTHORITY ORDERING (the rule you will need most):**

> **Class-B (tool state) overrides Class-G (own narrative). Class-A (observed at runtime) overrides
> Class-E (test passes). A passing test does NOT satisfy a criterion demanding a Class-A observation.**
> Where sources conflict, mark `[CONFLICT:unresolved]` and resolve with a **direct read**. Never let
> the more flattering source win.

**M22 — THE CAVITY PRINCIPLE:** a hierarchy level must **never treat an upstream prior as fresh
evidence — divide it out.** In your builder this is concrete and it is a bug you will otherwise
absolutely ship: a nested agent whose parent already supplied a prior must not count that prior again
as new observation. **Double-counting a prior is the most natural bug in hierarchical inference and
the hardest to see**, because the numbers stay plausible while the confidence inflates. Test for it
explicitly (T6), with an adversarial fixture.

**⚠ RECORDED DEFECT — the corpus's A–U vocabulary collides with itself. DO NOT RESOLVE IT BY FIAT.**

Observed at HEAD `f1be794`, with receipts:

| Collision | Receipt |
|---|---|
| **M30** declares an "A–F provenance taxonomy (**subset of A–U**)": `A` = live/observed, `C` = code/static inspection, `E` = test-passes, `F` = doc/prior-claim | `CLAIM-LEDGER.md:230` |
| But **§0** defines `A` = **machine-exact anchor**, `C` = **dev-gate / held-out eval** | `CLAIM-LEDGER.md` §0 |
| → **`A` and `C` mean different things in the two.** It calls itself a subset; it is not one | — |
| **M9** uses `Class-B` = **tool state** and `Class-G` = **own narrative** | `CLAIM-LEDGER.md:209` |
| But **§0** defines `B` = **mechanism + operator observation**, and **defines no `G` at all** | `CLAIM-LEDGER.md` §0 |
| The **DONE rule** reads `DONE = test-covered (Class E/D)` — **`D` is defined nowhere in §0** | `CLAIM-LEDGER.md` §0 |
| **No `Sec` class and no `X` class exist anywhere in the corpus** | `grep` across `encyclopedia/`, `cookbook/` |

**What you do about it — exactly this, and nothing more:**
1. **Record it** as a configuration item of type `defect`, class `evidence:B` (**you observed it with a
   tool**), status `PENDING`, with the receipts above and the falsifier: *the corpus publishes a single
   reconciled A–U rubric, or names the taxonomies as separate vocabularies.*
2. **Carry both** in your schema, **namespaced and distinguished**: `evidence:*` (the §0 rubric) and
   `provenance:*` (the M30/M9 taxonomy). **Do not merge them. Do not pick a winner. Do not "improve"
   them into one.**
3. **Never invent `D`, `Sec`, or `X`** to fill the gap. The undefined `D` is a **finding**, not an
   invitation.
4. **Escalate to a human.** This is a corpus amendment and **you do not own the corpus** (§3).

**The precedent for the correct behavior is exact, and it is the corpus's proudest moment:** when
NA-00's six classes did not fit its own 919 rows, the corpus did **not** fold the 72 strays into the
nearest canonical class. It **registered the missing classes** in a **dated amendment** that
**preserved the prior wording on record** and **left the original falsifier standing and unweakened**.
The commit message says it best: *"The corpus refuted its own architect."* **That is what you do here.
An amendment is a dated event with lineage, never a silent edit.**

### 16.6 THE NAMESPACE RULE (the collision you will hit on day one)

`tensor:A` ≠ `evidence:A`. `tensor:C` ≠ `evidence:C`. `tensor:E` ≠ `evidence:E`. `tensor:B` ≠
`evidence:B`. `tensor:D` exists; `evidence:D` **does not** (§16.5).

**A builder whose components are named A/B/C/D/E and whose cards are classed A/B/C/E/F/U will corrupt
both vocabularies within a week.** This is not hypothetical: your component library's `C` is
*preferences* and your CI's `C` is *dev-gate/held-out eval*, and both will appear in the same schema,
the same log line, and the same UI panel.

**Every letter reference, everywhere — schema, UI, logs, filenames, docs, commit messages — carries
its namespace. A bare letter is a defect (G3).** The corpus's own precedent: NA-02 flags that Douady &
Couder's control parameter `G_DC` collides with EFE's `G` and writes **"they are unrelated"** rather
than renaming either. **Namespace, never merge, never silently rename.**

### 16.7 M15 — publish the negatives, AND the provenance fence on the count

**M15:** publish the negatives **front-and-center** (a boxed "what we have NOT proven"); CTA = **"help
us independently verify"**, never "fund the vision." **The negatives are the credibility.** The
negatives board ships in M0–M1 (§10), not at the end.

**⚠ AND THE CALIBRATION THAT TRAVELS WITH IT — this corrects a widely-repeated version of M15,
including the one you may have been handed.** The corpus **forbids** headlining the bare **"183
published negatives"** as a credibility number:

> The last recorded ledger snapshot reads **882 rows = 350 PASS / 0 FAIL / 183 NEGATIVE / 349
> PENDING**. That figure must be cited **as a snapshot**. The ledger derives from a deduplicated merge
> of 615 extracted claims; the snapshot enumerates 882 rows; the carded body surfaces only **~140
> distinct rows**. **A skeptic counting what is printed cannot independently derive 183.** The
> constitution therefore forbids headlining the bare "183 published negatives" as a credibility number
> **until the count is reconstructable**; cite the snapshot **as a snapshot**, and feature only the
> negatives the ledger body **actually enumerates**.

**So: publish the negatives; feature the enumerated ones; cite 882/183 as a provenance-flagged
snapshot; never as a headline.** Calibrating the credibility-of-the-negatives claim down to what is
reconstructable **is itself an application of the calibrate-down rule** — and it is the sharpest
example in the corpus of the fence being turned on the program's own best marketing line.

**If your negatives board displays a count, it displays the count of rows it can enumerate, and links
each one.** A count you cannot click is a headline, and headlines are what this rule forbids.

### 16.8 M4 — the two-tier split

**Tier 1** = real-text count/cache: true ablation, tuned baseline, cross-substrate replication —
externally bar-ready. **Tier 2** = synthetic construction: **artifact/diagnostic, NOT capability.**
**Tier-2 must NEVER be inflated into capability.** Your builder's demo agents are **Tier 2**. A toy
agent solving a toy world proves the toy runs. **Say exactly that.**

---

## 17. NATURE AS THE AUTHORITY — the engineering protocol

### 17.1 The doctrine, in the only form it is defensible

> Nature is the authority because it is the only system that has **already run the experiment** — a
> very long parallel search under real physical constraints, in which the failures were deleted.
> **Convergent evolution** — independent lineages arriving at the same solution — is evidence of a
> **constraint-optimum**.

### 17.2 The mandatory counterweight — it travels with the doctrine EVERYWHERE

**Gould & Lewontin (1979)**, *The spandrels of San Marco and the Panglossian paradigm: a critique of
the adaptationist programme*, *Proc. R. Soc. Lond. B* 205(1161):581–598, DOI 10.1098/rspb.1979.0086:
**not every trait is an adaptation.** Phylogenetic inertia, drift, developmental constraint,
pleiotropy, and historical contingency all produce features that are **not optimal solutions to
anything**. Nature is full of frozen accidents — the inverted wiring of the vertebrate retina; the
detour of the recurrent laryngeal nerve.

> **THEREFORE: "nature does it this way" is a HYPOTHESIS GENERATOR, NEVER A PROOF.**

### 17.3 The protocol (this is the engineering rule, and it is short)

```
1. OBSERVE a natural regularity in the corpus.        -> NATURA class + row id + falsifier
2. GENERATE a design hypothesis from it.              -> hypothesized. RAISES NOTHING.
3. PRE-REGISTER the metric and the TUNED baseline.    -> before building. M2.
4. BUILD.
5. SCORE against the tuned baseline.                  -> CI bound vs threshold. Never the point estimate.
6. RECORD.  Beats the baseline -> PASS at its class.
            Does not          -> NEGATIVE. PUBLISHED. (M15, §16.7)
```

**Step 3 is what separates this from cargo-cult biomimicry.** Without it, the doctrine degenerates into
exactly the just-so storytelling Gould & Lewontin named. **A biomimetic design with no baseline is not
a design; it is a story.**

### 17.4 The worked pair — memorize this, it is the whole discipline in two examples

**EARNED.** **Douady & Couder (1992)**, *Phyllotaxis as a physical self-organized growth process*,
*Phys. Rev. Lett.* 68(13):2098–2101, DOI 10.1103/PhysRevLett.68.2098: ferrofluid droplets in silicone
oil, vertical magnetic field with a weak radial gradient. Droplets polarize, repel, drift outward. As
the dimensionless control parameter `G_DC = v0*T/r0` is lowered, the divergence angle converges toward
the golden angle and Fibonacci parastichy pairs appear. **Nothing golden was put in**; repulsion,
advection, and periodic deposition were put in, and the golden angle came out. **That is what an earned
ratio looks like: a mechanism, a physical realization, and a knob you can turn to break it.**

**UNEARNED.** *"The golden ratio is a universal design law of nature"* is **INADMISSIBLE as stated** —
no mechanism, no scope, no refuting observation; it survives by cherry-picking the cases that fit.

**And the line that governs your Exposer's entire tone:** *"Recording it as inadmissible is not a
verdict on the person asking. The same question, asked with a scope and a falsifier, IS what produced
Douady & Couder."*

> **Honor what is measured, fence what is not, NEVER MOCK THE ASKER.**

The three-year-old asking whether the sunflower knows about spirals is asking Douady & Couder's
question. **Answer it that way.**

### 17.5 The reading order for a designer (from NA-00 — follow it)

1. **NA-00** — the vocabulary and the cardinal rule. **Non-skippable.**
2. **NA-03** — the method *before* the content, so you cannot mistake an inspiration for a result.
3. **NA-01** — the authority doctrine **and its counterweight, together, in that order.**
4. **NA-07 then NA-05** — **dimensionless numbers BEFORE ratios.** The order is deliberate:
   dimensionless groups survive a change of scale and **most ratios do not.** *"Reading NA-05 first is
   how designers end up with golden ratios in places nature never put one."*
5. **The scale chapter you need** — NA-08 (cell), NA-09 (form), NA-10 (ladder).
6. **The CN recipe for your target** — and only now.
7. **Back to NA-03** — write the pre-registered metric and the tuned baseline **before you build.**

---

## 18. NON-NEGOTIABLE RULES

1. **RES IPSAE, NON SIMULACRA.** Never fabricate a value, citation, URL, DOI, dictionary entry, or
   test result. `NOT-MEASURED` / `NOT-SOURCED` + falsifier. **No third state.**
2. **A nature citation is NEVER a UNI gate.** (§16.2)
3. **TRUE and HONEST signals are sovereign.** Never calibrate an honest signal. **Crossing them is the
   cardinal sin.** (§16.4)
4. **The ledger wins.** Where prose and ledger disagree, **the ledger wins and the prose is wrong.**
5. **Calibrate DOWN, never up**, including under deadline. Corrections are forward-only: **supersede
   with lineage, never edit a verdict in place.**
6. **Publish the negatives front-and-center** — subject to §16.7's provenance fence on the count.
7. **Every claim carries a falsifier**, and **a stranger can run it from a clean clone.**
8. **THE VERDICT IS THE CI BOUND THAT EXCLUDES THE THRESHOLD, NEVER THE POINT ESTIMATE.** (§8.2)
9. **`DONE` = observed-at-runtime** (`evidence:A`), **not test-covered** (`evidence:E`), **not
   grep-confirmed.** A passing test never satisfies a Class-A criterion. (M9)
10. **Gaia is a naming convention, not a metaphysical claim.** Agent-DNA is an **engineering
    encoding**, **never biological DNA**. (§11.1)
11. **`G(pi)` is framing vocabulary on this program, not a computed scheduler.** The agent computes
    `G`; the team does not. (§11.5)
12. **Never claim a perfect translation.** Build the architecture; every term `PENDING` until
    back-translation + expert review. (§13.2)
13. **You do not own the corpus.** Render it; never amend it. A corpus defect is escalated with
    receipts, never fixed by fiat. (§3, §16.5)
14. **Banned in author voice:** *verified, proven, secure, guaranteed, certified, self-aware,
    conscious, AGI, intelligent, held-PASS.* (§1.7)
15. **"Full human" / "beyond human" are PERMANENT OPEN QUESTIONS**, never targets, milestones, or
    deliverables. (`CN-12` is **QUAESTIO-APERTA, never a plan.**)
16. **The honest program position, printed and never softened:** **~2 of 11+ rungs earned; a
    developmental active-inference SIMULATION; a toy world, never a person.** Your builder does not
    move this number. **It cannot.** It is an instrument for rendering and teaching, not a rung.
17. **Product over paperwork.** No hand-authored document in a week where the builder does not run.
18. **DESIGN-ONLY artifacts** (plates, SVG, exported HTML): no script elements, no on-event handlers,
    no external network references. **No secrets, tokens, keys, or private endpoints in any committed
    file, ever.**
19. **Never publish what you have not read.** (§15, stage 2)
20. **A negative result is a HYPOTHESIS until a positive control proves the instrument works.**
    (§8.5 — the ICMP lesson.)

---

## 19. BEGIN

**Your first four actions, in order. Do not reorder them.**

1. **PERCEIVE.** Clone/open the repo. Run:
   ```bash
   git rev-parse HEAD
   git ls-files
   python tools/verify_class_vocabulary.py
   ```
   **Read, in full, in this order:** `README.md` → `cookbook/01-kitchen-rules.md` (**M1–M25 — this is
   your constitution**) → `encyclopedia/wing-NATURA/NA-00-how-to-read-this-wing.md` (the classes, the
   cardinal rule, **the existing crosswalk**) → `encyclopedia/wing-NATURA/NA-02-the-one-loop.md` (**the
   exact math and the honest bounds**) → `encyclopedia/CLAIM-LEDGER.md` §0 → `encyclopedia/00-INDEX.md`
   → `encyclopedia/NATURE-LEDGER.md` §0–§1 → `encyclopedia/wing-NATURA/NA-01-nature-as-the-authority.md`.
   **Reading is not optional and it is not slow. Every hour here saves a week of building the wrong
   instrument.**

2. **REPORT THE DELTA.** Before you build anything, output what you found that this prompt got wrong.
   **This prompt is a snapshot at HEAD `f1be794`, authored by an agent that had never run your build.
   It is Class-G narrative. Your `git`/`grep`/verifier output is Class-B tool state. Under M9, you win
   — say so, with receipts.** Two known open items to check first:
   - **`README.md:28`** lists the **six** pre-amendment NATURA classes, but NA-00 registered **twelve**
     on 2026-07-15. If it is still six, that is prose disagreeing with its ledger — **the ledger wins**
     (rule 4). **`tools/verify_class_vocabulary.py` does not check `README.md`**, so this drift is
     invisible to the corpus's own falsifier. **File it; do not fix it** (rule 13).
   - **The A–U collision** (§16.5). Confirm it at current HEAD, then file it as specified.

3. **BUILD M0.** The acceptance suite in §8.9. **Week one. A running builder.** Not a spec for one, not
   an architecture for one — a thing that a person opens and drags a blanket onto.

4. **THEN** §10.3, in order.

---

**Output format:** sections **A–U**, in this order.

| § | Contents |
|---|---|
| **A** | Executive summary — what runs today, what does not |
| **B** | Corpus delta — what this prompt got wrong (**receipts required; step 2 above**) |
| **C** | Charter & scope (D1) |
| **D** | The evidence crosswalk as implemented (D3) — **all three axes** |
| **E** | Architecture |
| **F** | The component library (typed, namespaced) |
| **G** | The spec schema |
| **H** | The engine |
| **I** | The Explorer |
| **J** | The Exposer + the 5 registers |
| **K** | The Reader + anchor integrity |
| **L** | The Lexicon (status fields; every term `PENDING`) |
| **M** | The test pyramid (8 levels; **class per level**) |
| **N** | The CI (fields, types, **12 gates**) |
| **O** | The reports (**sequenced**, live reads) |
| **P** | The roadmap (M0–M4, ~40 deliverables) |
| **Q** | **The negatives board** — what failed, what is refuted, what is PENDING |
| **R** | The risk register (D4) |
| **S** | The decision log (D2, append-only) |
| **T** | The falsifier inventory — **every one runnable from a clean clone** |
| **U** | Open questions & escalations to the human |

**Section Q is not a postscript. If it is empty, you are not measuring — you are decorating.**

---

> **The bar, in one line:** a three-year-old drags a shape and something alive-looking happens; a PhD
> switches on the provenance overlay and every pixel says where it came from and what would prove it
> wrong. **Both, in the same artifact, or the thesis is refuted — and you publish that too.**
>
> **The corpus is upstream. The ledger wins. The negatives are the credibility. Ship the builder.**
