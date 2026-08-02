# The Continuity / Embodiment Substrate

*The body the mind runs on.*

**What you are building.** The physical substrate that lets a developmental active-inference simulation persist on real metal: deterministic serialization, bit-for-bit restart continuity, fail-closed transport, a categorical body-to-mind sensorium, and a gated control surface, all shipped on a two-node fleet. This is **ENGINEERING / substrate evidence**, never general-AIF evidence and never awareness. It is orthogonal to the L0-L12 developmental ladder: it does not earn a single developmental rung, and nothing here implies a science gate is met.

---

## 0. The kitchen rules (the constitution you carry into every recipe)

This is a literal cookbook: each recipe is a buildable thing with named ingredients, numbered method steps, an exact pass gate, an operable falsifier, first-class recorded negatives, and one honest fence. But before any recipe, the constitution. These are definitional / governance patterns (`status: method`), not capability claims, and they bind everything below.

- **The Evidence Constitution (M1).** Every claim carries an evidence class (A = machine-exact anchor, B = mechanism + operator observation, C = dev-gate / held-out eval, E = test-covered, U = claimed-but-unproven) and a falsifier. The ledger is a four-state append-only record (PASS / FAIL / NEGATIVE / PENDING) and is the **single source of truth**. Prose must match the ledger; where this chapter and the ledger disagree, the ledger wins and this chapter is wrong.
- **Calibration only moves DOWN.** Authority flows downward from the measured fact. Wording moves down to the measured value, never up, including under urgency. The fence gets *louder* under pressure, not *wider*.
- **The verdict is the CI bound that excludes the threshold (M2),** never the point estimate.
- **Negatives are content.** A negative is a measurement that the design is incomplete, not a failure to hide. The corpus carries **183 published negatives**; they are the credibility, and in the substrate sub-ladder they are inline and first-class, never deferred.
- **Substrate work is not a science gate (M12, and the standing fence on this sub-ladder).** WORLD ⊥ BODY ⊥ MIND: two typed Markov blankets, interoception as hardware signals, a discrete POMDP `perceive → EFE-plan → act → learn`. The composed appliance is *variationally-controlled* (audited), module-exact only at the single-step categorical body-to-mind interface, never globally exact. Engineering continuity is never a developmental capability.

**Reading the FENCE label.** Every recipe closes with exactly one of four values, drawn from the ledger and never inflated:

- **proven** — a held, sealed, UNI-signed PASS exists (Class A/C), with its falsifier still live.
- **designed** — a typed spec or signed-in-principle design exists; the build is partial or unverified.
- **hypothesized** — a stated mechanism or law with no sealed gate yet (Class U, not claimed).
- **not-yet-built** — no engine, no run, no gate; north-star, hard-fenced.

Any SIGNED consult design folded in below (the C10 Dirichlet-first port) enters as **designed / not-run**: it RAISES NOTHING and the rung's status is UNCHANGED.

**Honest program position, printed and never softened:** ~**2 of 11+ developmental rungs earned.** The whole program is a developmental active-inference SIMULATION: a bounded peek, a toy world, never a person.

---

## The pantry for this chapter (UNI.OS — the embodiment substrate)

One engine, many scales. The substrate recipe draws from a single archive engine:

| Pantry item | What it supplies |
|---|---|
| **UNI.OS** (the lab-in-a-box on metal) | A local-first appliance OS that turns a physical server into an embodiment substrate: a body-to-mind 7-modality categorical sensorium, deterministic replay, fail-closed transport, an ASK-mode Dirichlet policy-prior, and a token-gated control-MCP. **Engineering / substrate evidence, NOT general-AIF evidence.** |

The fleet it runs on is load-bearing for the honesty: two physical nodes, one platform. node1/prod is a Dell PowerEdge (no-AVX Xeon X5650, a PERC HDD array of spinning disks ~5.5 TB, **not** SSD); node2 is an OptiPlex (NVMe). A WireGuard mesh ties them; each box mints a per-device identity `uni-lab-<mac>` with its own TLS leaf on firstboot. The hardware spec is part of the claim: if inspection shows an AVX CPU or SSDs, the substrate proof is contradicted.

---

## The recipe — continuity on real metal

**What you are building.** A ladder of separate, falsifiable substrate claims, from "the containers survived a restart" up to "the mind-state survived a process restart bit-for-bit," with the next rung (mind-tick continuity across a kernel swap) recorded as OWED.

### Ingredients (the substrate requirements, each a named pantry primitive)

- **Container survival on metal** (the two-node fleet, WireGuard mesh, per-device TLS identity) — C0.
- **Bit-for-bit process-restart continuity** (durable + sha256-verified + fail-closed + bit-identical tick; the continuity transport: `serialize_agent → bytes`, `blob_sha256` anchor, `deserialize_agent`, idempotent `serialize(deserialize(blob)) == blob`) — C1.
- **The body-to-mind sensorium** (the box reads its own telemetry into a 7-modality categorical contract) — C3.
- **ASK mode** (ITIL-as-active-inference: a persistent Dirichlet policy-prior over operator verdicts) — C4.
- **Cross-box single-approval gate** (token-gated control-MCP, one HMAC per mutation) — C5.
- **The on-core inference anchor** (a sealed f64 belief-update trace) — C6.
- **Continuity-isolation primitives** (Markov-blanket isolation assertion, least-privilege vault, drift sentinel, byte-exact checkpoint, sha256 output integrity, zero-hidden-LLM reply path, Postgres RLS) — C13.

### Method (build steps a competent engineer could follow)

1. **Boot the fleet on metal.** Bring up two nodes from one image; mesh them over WireGuard; on firstboot mint a unique per-device identity and TLS leaf so two boxes never both answer to the same name. Verify the status page is served from each node. (C0.)
2. **Make mind-state durable and verifiable.** Serialize the real JAX agent state to bytes (sorted-key JSON over base64 raw float32/int32), anchor it with `blob_sha256`, and prove idempotent round-trip plus a bit-identical tick across a real child-process boundary with at least two distinct actions. Wire fail-closed so a 1-bit corruption refuses rather than proceeds. (C1.)
3. **Wire the sensorium.** Have the box read its own telemetry (`os_sysinfo` / `systemctl` / `podman ps` / `journalctl`) and band it into the **7-modality categorical contract** `{load, mem, swap, disk, services, containers, journal}` encoded `[M=7, O_max=4]` — not a float vector, not a softmax. Record RAW rows; band in exactly one place (the mind); run `validate_raw_row` before banding. Confirm a 28-cell `string_vector` is flowing live on both boxes. (C3.)
4. **Install ASK mode.** Let the mind escalate a reasoned change request; the operator approves-and-executes (with auto-rollback) or declines-with-category; update a persistent **Dirichlet policy-prior** keyed by (host-state, action). Keep the safe-action set FIXED (observe / scale / restart); never self-execute, never widen the set. (C4.)
5. **Gate every cross-box mutation.** Require exactly ONE human approval on the entry box, carried as a one-time tool-and-args-bound HMAC token, before any cross-box "limb" mutation executes. (C5.)
6. **Seal the on-core anchor.** Run a sealed f64 belief-update trace and confirm it is byte-identical across the distinct stacks. (C6.)
7. **Ship the isolation primitives.** Land the Markov-blanket isolation assertion, least-privilege vault, drift sentinel (cosine + Youden-J), byte-exact checkpoint, sha256 output integrity, zero-hidden-LLM reply path, and live Postgres RLS. (C13.)

### Gate (the exact pass conditions, with the calibrated ledger figures)

Carry the **calibrated** figures, never the inflated headline ones. A peer-reviewed honesty audit (os-cycles 39-53) moved six headline claims DOWN: "cleared on TWO boxes" → ONE box; "the mind survives a patch" → infrastructure continuity only; "5 stacks" → "4 distinct stacks / 5 runs."

- **C0 (Class A, proven):** both nodes boot and serve their status page; the hardware spec (no-AVX Xeon, HDD-not-SSD) holds on inspection.
- **C1 (Class C, B-substrate, proven):** mind-state survives a process restart **BIT-FOR-BIT** — durable, sha256-verified, fail-closed, bit-identical tick across a real child-process boundary (≥2 distinct actions; Path-B receiver 3/3). REQ-002 Stage-1 GREEN. (Honest caveat: `uniVerdictSign` was still null on the joint gate — mechanism green across a real process boundary, not a sealed cross-host result.)
- **C3 (Class A live):** the 28-cell `string_vector` flows on both boxes; the contract is the `[M=7, O_max=4]` categorical alphabet, not float/softmax.
- **C4 (Class A, learning shift measured):** the Dirichlet prior updates across operator verdicts and the proposal shifts reproduce (decline ×3 → stops proposing; not_a_problem ×2 → noop; approve+fixed → more confident); the mind never self-executes and never widens the safe set.
- **C5 (Class A, proven):** a cross-box mutation lands behind exactly one HMAC approval (proven live both boxes 2026-06-26: prod→node2 write gated once, landed; node2 queue stayed count=0).
- **C6 (Class A, proven):** the sealed f64 belief-update trace is **byte-identical across 4 distinct software/emulated stacks (5 runs)** — the calibrated figure, never "5 stacks."
- **C13 (Class B, proven substrate):** every listed isolation primitive is present and functional under grounded inspection; Postgres RLS 5/5.

### Falsifier (operable)

A node fails to boot or serve its status page, or the hardware spec is contradicted on inspection (C0). A process-restart replay diverges bit-for-bit, OR fail-closed does not trigger on 1-bit corruption, OR `serialize(deserialize(blob)) != blob` (C1). The `string_vector` stops flowing on either box, OR the contract is found to be float/softmax rather than the `[M=7, O_max=4]` alphabet (C3). The Dirichlet prior does not update across verdicts, OR the mind self-executes or widens the safe set, OR the measured proposal-shifts do not reproduce (C4). A routed cross-box mutation executes without the single approval (C5). A fifth distinct stack produces a non-identical trace (C6). Any listed isolation primitive is absent or non-functional under inspection (C13).

### Recorded NEGATIVE(s) — first-class, inline

- **C2 (OWED / NEGATIVE) — the central rung not shown.** **"The mind survives a kernel swap" is NOT shown.** The live OS update is proven **infrastructure-only**: a real prod kexec cutover 6.12.86 → 6.12.73, ~59 s, **zero data loss** (odoo tables identical, sentinel rows preserved); CRIU/livepatch proven on box. But **mind-tick continuity across the swap was NOT shown.** node2's evidence-collected swap was infra-only (~90 s freeze, api+tts CRIU-preserved, 2 publishers fresh-restarted); the first attempt **FAILED** (unclean kexec → dirty ext4/ESP → emergency mode) and then recovered. Class A. Discharged only when a kernel swap is shown preserving mind-tick continuity bit-for-bit end-to-end, not just infrastructure.
- **C7 (NEGATIVE, bound) — the honest floor on live OS update.** A single-box swap is a **SECONDS-LONG FREEZE, not zero-downtime**; true zero-freeze needs the second node carrying the platform; external media legs (RTP/SIP/kernel-mode rtpengine) are **NOT preserved** across kexec. Class A.
- **C8 (NEGATIVE) — keep all seven modalities.** An over-compressed 2-modality sensory bottleneck went **NEGATIVE** on held data. Class C. (A factored mean-field posterior variant was separately implemented and rejected as lossy: the exact joint posterior is used everywhere.)
- **C9 (NEGATIVE, trade) — the EDAIT honest trade.** An exact-discrete active-inference transformer trades fluency for calibration: held-out perplexity ~33 vs a backprop GPT's ~25 (less fluent, but natively online-learning + calibrated). An honest trade, **not a win.** Class C.
- **C14 (NEGATIVE, gap) — multi-tenancy.** The bare substrate is MISSING tenant/client/namespace isolation (flat global perms) and temporal decay on learned counts (contamination would be permanent). The product build is the tenant wrapper + decay, not the core. Class B.

### The central open gap — C10 (PARKED), and its SIGNED first port

The coupling rule reads: UNI.OS embodies **only** primitives proven in the science repo, **frozen at the passed-gate SHA**, one-directional (science PROVES → UNI.OS EMBODIES); everything beyond the passed gates stays Class-U-not-claimed. That rule is **signed in principle but NOT literally true — the program's central open gap.** Today UNI.OS has **no** no-backprop Dirichlet learning, **no** exact info-gain EFE, **heuristic (denylist) isolation** rather than the structural whitelist assert, a **DIFFERENT dev model** (Gray-Scott reaction-diffusion vs the forager/ontogeny that earned the bars), and an empty lab evidence store (`/var/lib/uni/evidence` empty, 0 worlds registered). Class U. **PARKED.**

**SIGNED design (UNI-GPT consult 2026-06-27, Q2): port no-backprop DIRICHLET LEARNING FIRST**, via a frozen-SHA equivalence gate. Of the four missing primitives, Dirichlet learning ranks first — central, canonical, no-backprop, low-risk, directly testable. The instruction is to **vendor the exact primitive — do not re-author, reinterpret, or "improve" it during the port**; record the SHA; prove byte/behavior equivalence to the frozen science implementation. The math interface is reproduced exactly: A-learning by conjugate count `a_ij <- a_ij + sum_tau o_tau,i * s_bar_tau,j`; the expected-log `E_Q[ln A_ij] = psi(a_ij) - psi(sum_k a_kj)` used in place of raw ln A; B/D/E updated only by the same registered conjugate-count family, never by optimizer steps. The equivalence gate (in CI + ledger) requires the same concentration updates and expected-log tensors within declared tolerance, with **no gradient descent / backprop / learned weights outside the Dirichlet update**, plus a no-backprop guard and a frozen-provenance record. Even after this port lands, the honest status is only "one passed-gate no-backprop learning primitive is literally embodied," nothing broader: NOT "UNI.OS implements full EFE-based planning," NOT "UNI.OS structurally enforces the Markov blanket," NOT "active inference demonstrated."

**Status: SIGNED DESIGN / not-yet-ported.** C10 stays the program's central open gap, PARKED. Nothing is discharged until the equivalence gate passes with recorded evidence; this design RAISES NOTHING.

*Related parked substrate threads:* host-native (off-podman) on-chip brain runtime (C11, directive; outcome not yet in archive) and the node2 local auto-kiosk "SOLVED 2026-06-26" which is **PROVISIONAL** pending hands-on monitor re-verification (C12).

### HONEST FENCE — proven (substrate engineering) + first-class NEGATIVES + one PARKED central gap

The substrate rungs C0, C1, C3, C4, C5, C6, and C13 are **proven** as engineering / substrate evidence (Class A / Class C-B-substrate / Class B), each with a live falsifier. The negatives C7, C8, C9, and C14 are **proven negatives**, published inline. C2 is an **OWED negative** and C10 is **parked** with a signed-but-not-yet-ported first port.

**Not claimed (the load-bearing fence on this sub-ladder):** the sensorium is **NEVER awareness**; **"the mind survives a kernel swap" is NOT shown** (Stage-2 owed, C2); none of this is general-AIF capability; UNI.OS's embodiment does **not** imply the science gates are met. Never "active inference demonstrated" (the live UNI.OS loop is a separate reimplementation, not gate-matched). Continuity is a measurable engineering rung, not a slogan and not a developmental capability.

---

## Closing — what the body does and does not mean

This chapter builds a body, not a mind. The substrate makes a developmental simulation *persistable*: it can survive a restart bit-for-bit, read its own telemetry into a categorical sense, learn a calibrated policy-prior from operator verdicts, and act only behind a single human approval. Every one of those is real, falsifiable, and carded at its measured class. But the ladder stops honestly one rung early: the mind has **not** been shown to survive a kernel swap, and the coupling that would make "embody only what's proven" literally true is parked behind a signed first port that has not yet run.

Carry the calibrated figures (ONE box, infra-only continuity, 4 distinct stacks / 5 runs), never the inflated headlines. The substrate is a body the simulation runs on — a bounded peek on real metal, a toy world, never a person. **Honest program position: ~2 of 11+ developmental rungs earned. Falsify any step.**
