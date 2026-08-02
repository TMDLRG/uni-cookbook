# PREFLIGHT — must pass before firing

## STATUS: STAGED, NOT DEPLOYED. This checklist has not been run.

**No item below has been checked. Nothing here is a PASS.** Every box is empty because nobody has
worked this list yet. The reader is not serving on any limb.

**How to use this.** Work top to bottom. Each item has a **falsifier** — the specific observation
that closes it. An item is closed by its falsifier or it is PENDING. **There is no third state, and
"it looks fine" is not a falsifier.** If an item cannot be made to pass, **do not fire.**

**A note on negative results, learned the hard way.** A silent probe is not a dead box. ICMP is
policy-dropped on this fleet — a `ping` timeout is *not* evidence of anything. A negative result is
a **hypothesis** until a positive control proves the instrument works. Where an item below is
checked by absence, it names its positive control. Do not skip it.

---

## A. The blocking gate

### A1. `reader/build.py` exists and builds

- [ ] **Falsifier:** `python reader/build.py` exits 0, and `reader/dist/` contains >= 1 `.html`.
- **State as of 2026-07-15: FAILS.** `reader/build.py` does not exist. `git ls-files | grep reader`
  returns nothing. `.gitignore` reserves `reader/dist/` but the reader is `not-yet-built`.
- **Consequence:** `deploy_cookbook.py` refuses at its first gate. **The bundle cannot fire today.**
- **Who closes it:** whoever authors the reader. Not this bundle.

**If A1 fails, stop. Every item below is unreachable.**

---

## B. Local — the corruption guards

### B2. Every file is pure ASCII

- [ ] **Falsifier:** `deploy_cookbook.py --dry-run` prints `ascii guard : PASS` and names the file
  count. It refuses on the first non-ASCII byte, naming the file, byte offset, line, and context.
- **Why:** `os_file_write` corrupts multi-byte UTF-8 — it drops bytes and **still returns `ok=true`
  with a sha-verified read-back lie**. Pure ASCII means the bug **cannot fire**.
- **Positive control:** the guard is proven live, not assumed. Put a literal em-dash into any file in
  `reader/dist/`, run `--dry-run --skip-build`, and confirm it **refuses**. Remove it. A guard nobody
  has seen trip is a guard nobody knows works.

### B3. The working tree is clean

- [ ] **Falsifier:** `git status --porcelain` returns empty; `--dry-run` prints `commit ... (clean)`.
- **Why:** `_provenance.json` content-addresses the deploy by commit sha. A dirty tree means the sha
  does not describe the deployed bytes. The script records `repo_clean:false` honestly and proceeds
  — it does not refuse — so **this one is on you.** A dirty deploy is not reproducible from its
  commit.

### B4. The reader has been read by a human

- [ ] **Falsifier:** a person has opened `reader/dist/index.html` in a browser and can state what it
  discloses — names, private endpoints, internal addresses, tokens.
- **Why:** these bytes are about to be served. If [`PUBLISH-DECISION.md`](PUBLISH-DECISION.md)
  Option C or D is ever chosen, they become **permanently public**. This audit is `not-yet-built`
  and is a **hard prerequisite for any public option**.
- **Not automatable.** No script closes this one.

### B5. No secret is in the bundle or the reader

- [ ] **Falsifier:** `git grep -nEi "(token|secret|bearer|api[_-]?key|password)" -- deploy/ reader/`
  returns only variable names and prose — **never a value**.
- **Why:** the token comes from `UNI_TOKEN` at runtime and is never logged, never written to a file,
  never placed in a URL. If you find a value, that is a **defect: report it and rotate the token.**

---

## C. Transport — node1

### C6. node1 is reachable and the env is set

- [ ] **Falsifier:** `--dry-run` prints `node1 MCP : uni-control-mcp <version>` and a session line.
  The script refuses loudly if `UNI_MCP`/`UNI_TOKEN` are unset or if node1 does not answer.
- **Route:** LAN `10.190.245.121:8080`. **Not the mesh** — this box is a wg client peer pinned to a
  dead literal `10.190.245.122`; node1 moved to `.121`.
- **Positive control:** if it fails, prove the box before blaming it. **A silent `ping` is not
  evidence** — ICMP is policy-dropped here. Use an actual TCP connect to `10.190.245.121:8080`, or
  try `192.168.1.249` (the two LANs are routed). Observed 2026-07-15: 38 tools, uni-control-mcp
  1.27.2.

### C7. The live tool schemas match what the script sends

- [ ] **Falsifier:** `--dry-run` prints the `inputSchema` of `os_file_write` / `os_exec` /
  `os_sysinfo`, and `path` + `content` are both present on `os_file_write`. The script refuses if
  not.
- **Why:** arg names here are **inferred from prior sessions, not read from this server**. That is
  an assumption, so the script reads the live schema and refuses rather than sending a call shaped
  by a stale memory. **Read what it prints** — do not skim past it.

### C8. `os_file_write` exposes a `limb` field

- [ ] **Falsifier:** `limb` appears in `os_file_write`'s live `inputSchema` properties.
- **Why this one matters more than it looks:** without `limb`, a write intended for node2 lands on
  **node1 again** — a silent wrong-box write. That is the **SW-E3-03 class of error** (a build staged
  onto the wrong box, overwriting a file nobody had read). The script refuses node2 rather than risk
  it, and warns on `--dry-run`.

### C9. The parent-dir route is known

- [ ] **Falsifier:** `--dry-run` names the route (native mkdir tool, or podman+busybox), and on the
  real run `ls -d /opt/uni/services/glass/ui/cookbook` **proves** the directory exists before any
  file is written.
- **Why:** `os_file_write` silently no-ops when the parent is missing — **and still returns
  `ok=true` with a sha-verified read-back lie.** Every "successful" write into an unproven directory
  may be a lie. The script refuses and prints the manual `mkdir -p` rather than write blind.
- **Note:** the node1 argv[0] allowlist has **no `mkdir`**. The podman route needs the busybox image
  present. If neither works, create the dir by hand — that is a fine outcome, not a failure.

---

## D. Blast radius

### D10. Nothing outside the cookbook dir is touched

- [ ] **Falsifier:** `--dry-run`'s write plan lists **only** paths under
  `/opt/uni/services/glass/ui/cookbook/`. No unit, no quadlet, no nginx config, no reload appears
  anywhere.
- **Enforced in code:** every `os_exec` must match `ALLOWED_EXEC_INTENTS`
  (`verify-dir-exists` / `create-dir` / `remove-cookbook-dir`) and is refused if its argv contains
  `nft`, `wg `, `uni-dns`, `systemctl`, `iptables`, `nginx`, `quadlet`, or `daemon-reload`.

### D11. The other live session's lane is clear

- [ ] **Falsifier:** the operator confirms the concurrent node1+node2 session (registry, wg
  ListenPort, name map, PHARUS beacon) **is not mid-cutover right now**.
- **Why:** this is the reason the design is static. **Not automatable — ask the human.** Two sessions
  writing the same box is how you get a state nobody predicted.

### D12. nginx already serves the parent root

- [ ] **Falsifier:** `https://10.190.245.121/glass/horologium.html` returns 200 **before** you fire.
- **Why:** this is the **positive control for the whole serve path.** It proves nginx serves
  `/opt/uni/services/glass/ui/` right now. If it is 200 before the deploy and `/glass/cookbook/` is
  404 after, the problem is the deploy — not nginx. Without this control, a 404 afterward is
  ambiguous and you will debug the wrong box.

---

## E. Decisions made before, not after

### E13. The exposure decision is made

- [ ] **Falsifier:** the operator has read [`PUBLISH-DECISION.md`](PUBLISH-DECISION.md) and named an
  option. Default: **A (tailnet)** — private, reversible, zero config.
- **Why before:** public exposure **cannot be un-rung**. Indexes, archives, scrapes and training
  corpora keep what they took. There is no such thing as briefly public. Deciding after the fact
  means deciding under pressure about something already irreversible.

### E14. The tablet's absence is understood and carded

- [ ] **Falsifier:** the operator has read [`TABLET.md`](TABLET.md) and accepts that this is a
  **2-of-3-limb deploy**.
- **This is not fleet-wide.** Do not record it as one.

---

## F. After firing — the receipt

**Nothing above proves the deploy. These do.**

### F15. Both limbs serve the reader at HEAD

- [ ] **Falsifier:** both return **200** and report the **same `commit` as `git rev-parse HEAD`**:
  - `https://10.190.245.121/glass/cookbook/_provenance.json` (node1, LAN)
  - `https://10.13.13.3/glass/cookbook/_provenance.json` (node2, mesh)
- **Anything less is a partial deploy.** A limb whose `commit` differs is **stale**. A limb reporting
  `"state": "DEPLOY-IN-PROGRESS"` was interrupted — re-run.

### F16. The reader actually renders

- [ ] **Falsifier:** `https://10.190.245.121/glass/cookbook/` returns 200 and a **human reads a
  chapter in a browser.** A 200 on a JSON file is not a reader; bytes on disk are not a page that
  renders.

### F17. The receipt is recorded, and the bundle is committed

- [ ] **Falsifier:** the `audit_id` + UTC of the deploy is captured, **and `deploy/` is committed to
  git.**
- **Why both:** *a deploy receipt is not a substitute for a commit.* A bundle that fired but exists
  only as an untracked local tree is not durable — the next session cannot roll back what it cannot
  read.

---

## The refusals this script will issue (all of them deliberate)

It **fails loudly rather than succeeding vaguely.** There is no "probably worked" branch.

| It refuses when | Because |
|---|---|
| `reader/build.py` is missing | it will not deploy an empty tree and call it a reader |
| any file has a non-ASCII byte | `os_file_write` corrupts multi-byte UTF-8 and lies `ok=true` |
| `reader/dist/` has no `.html` | a reader with no HTML is not a reader |
| `UNI_MCP`/`UNI_TOKEN` unset | it will never hardcode an endpoint or a token |
| node1 does not answer | half a deploy is worse than none |
| a tool or field is missing from the live schema | it will not send a call shaped by a stale memory |
| `os_file_write` has no `limb` and node2 is the target | a silent wrong-box write is the SW-E3-03 error |
| the target dir cannot be **proven** to exist | writes into a missing parent silently no-op and lie |
| a returned sha != the local sha256 | the bytes on the limb are not the bytes we sent |
| no sha can be found in the response | `ok=true` alone is not a receipt |
| an `os_exec` argv touches nft/wg/uni-dns/units | another session is live on those boxes |
| rollback cannot prove the dir is gone | it will not pretend a rollback happened |
