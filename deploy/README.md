# Cookbook Reader — UNI deploy bundle

## STATUS: STAGED, NOT DEPLOYED

**Nothing in this bundle has been fired. The Cookbook Reader is not serving on any limb.**
No file has been written to node1 or node2. No MCP call was made in authoring this bundle. The
operator drives the deployment; the bundle only makes it a single, reviewable, reversible command.

| | |
|---|---|
| **Deploy state** | `not-yet-built` — nothing written to any limb |
| **Bundle state** | authored, unreviewed, unfired |
| **Blocking PENDING** | `reader/build.py` does not exist in this repo (see below) |
| **Staged at commit** | `f1be794` (`git rev-parse HEAD`, 2026-07-15) |
| **Target** | `/opt/uni/services/glass/ui/cookbook/` on node1, then node2 |

---

## The blocking PENDING, stated first

**`reader/build.py` DOES NOT EXIST.** This bundle deploys a reader that has not been built.

This is not a guess. `.gitignore` already reserves the path:

```
# Build artifacts — regenerate with `python reader/build.py`.
reader/dist/
```

...but `git ls-files | grep reader` returns nothing and `ls reader` returns
`No such file or directory`. The reader is `not-yet-built`.

`deploy_cookbook.py` **refuses to run** until it exists. That refusal is deliberate: the script will
not deploy an empty tree and then advertise it as a reader.

- **Falsifier that closes this PENDING:** `python reader/build.py` exits 0 and `reader/dist/`
  contains at least one `.html` file. At that moment `deploy_cookbook.py --dry-run` proceeds past
  its first gate.
- **Who closes it:** whoever authors the reader. Not this bundle. This bundle is the transport, not
  the reader.

Everything below is written for the state *after* that PENDING closes. Until then, the exact
commands in this file are staged and unfireable.

---

## What this is

A static, read-only HTML reader for the UNI Encyclopedia & Cookbook corpus, copied as plain files
into the nginx serve root that node1 **already** serves (`/opt/uni/services/glass/ui/`, alongside
`horologium.html`, `arbor.html`, `index.html`).

**What it adds to a limb:** files in one new directory.

**What it does NOT touch — by design, and asserted in the script:**

- no new systemd unit, no quadlet
- no nginx config edit, no nginx reload
- no `wg`, no `nftables`, no `uni-dns`
- no existing unit on any box

That list is not politeness. **Another session is live on node1 and node2 right now** (registry, wg
ListenPort, name map, PHARUS beacon). This bundle must not enter its lane. A static reader needs
nothing more than files in a directory that is already served, so it takes nothing more.

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for why static is also what makes active-active trivial.

---

## Before you fire

Work [`PREFLIGHT.md`](PREFLIGHT.md) top to bottom. Every item has a falsifier. If an item cannot be
made to pass, do not fire.

Decide the exposure question **before** you fire, not after:
[`PUBLISH-DECISION.md`](PUBLISH-DECISION.md). The default is the tailnet — private and reversible.
Public exposure (Funnel / cloudflared) is an explicit operator decision this bundle does not make
and cannot un-ring.

---

## The exact commands to fire

Run from the **operator's workstation**, from the repo root. The workstation reaches node1 over LAN
(`10.190.245.121:8080`); it does **not** reach the fleet over the wg mesh (this box is a wg client
peer pinned to a dead literal `10.190.245.122`; node1 moved to `.121`). There is **no SSH** from the
workstation (`root@.121` -> `Permission denied (publickey)`; the `uni_deploy` key is not here).
**MCP `os_file_write` is the transport.**

### 1. Set the environment (never commit these; never paste a token into a file)

```powershell
$env:UNI_MCP   = "http://<node1-host>:<port>/<mcp-path>"   # the node1 MCP endpoint
$env:UNI_TOKEN = "<the bearer token>"                      # from the operator's store, not from git
```

```bash
export UNI_MCP="http://<node1-host>:<port>/<mcp-path>"
export UNI_TOKEN="<the bearer token>"
```

No endpoint credential and no token appears anywhere in this bundle. `deploy_cookbook.py` reads both
from the environment and refuses to start if either is unset. If you find a token in any file here,
that is a defect — report it and rotate the token.

### 2. Dry run first — it makes no mutation

```bash
python deploy/deploy_cookbook.py --dry-run
```

This builds the reader locally, asserts every file is pure ASCII, contacts node1 read-only, prints
the live `inputSchema` of every tool it intends to call, and prints the exact write plan (path, byte
count, local sha256) for both limbs. **It writes nothing.**

Read the plan. If the plan is wrong, stop.

### 3. Fire

```bash
python deploy/deploy_cookbook.py
```

node1 first, then node2 via `limb=uni-lab-79740c`. Per limb: parent dirs created and verified,
then every file written and its returned sha checked against a locally computed sha256, then
`_provenance.json` written **last**.

### 4. Observe (the receipt)

```
https://10.190.245.121/glass/cookbook/                    # node1, LAN
https://192.168.1.249/glass/cookbook/                     # node1, the other LAN (routed)
https://10.13.13.1/glass/cookbook/_provenance.json        # node1, wg mesh
https://10.13.13.3/glass/cookbook/_provenance.json        # node2, wg mesh
http://100.100.188.48/glass/cookbook/                     # node1, tailnet (uni-lab-hub)
```

**The deploy is done when, and only when,** both `_provenance.json` files return 200 and both report
the same `commit` as `git rev-parse HEAD`. Anything less is a partial deploy — see the rollback.

Until you have observed that with your own eyes, the reader is `not-yet-built`, not deployed. This
file will not be updated to say otherwise by the script; a deploy receipt is not a commit and a
commit is not a receipt.

---

## Rollback

```bash
python deploy/deploy_cookbook.py --rollback
```

Removes `/opt/uni/services/glass/ui/cookbook/` from node1 and node2. Nothing else is touched, because
nothing else was ever touched — there is no unit to stop, no config to revert, no reload to undo.
**That is the entire benefit of the static design.** The blast radius of the rollback is exactly the
blast radius of the deploy: one directory.

If the script cannot perform the removal (the node1 `os_exec` argv[0] allowlist has no `rm`), it
**refuses and prints the exact manual command** rather than pretending. Removing a directory is not
something this bundle will fake a success on.

**Falsifier that closes the rollback:** `https://10.190.245.121/glass/cookbook/_provenance.json`
returns 404 on both limbs.

---

## Every PENDING in this bundle, with the falsifier that closes it

| PENDING | Falsifier that closes it |
|---|---|
| `reader/build.py` does not exist | `python reader/build.py` exits 0 and `reader/dist/` holds >=1 `.html` |
| Reader not deployed to node1 | `https://10.190.245.121/glass/cookbook/_provenance.json` returns 200 with `commit` == HEAD |
| Reader not deployed to node2 | `https://10.13.13.3/glass/cookbook/_provenance.json` returns 200 with `commit` == HEAD |
| Reader not deployed to the tablet | `limb=uni-tab-arm-1` `os_sysinfo` returns `ok=true` — see [`TABLET.md`](TABLET.md) |
| MCP tool arg names are inferred, not read | `--dry-run` prints each tool's live `inputSchema`; the script refuses if a needed field is absent |
| `os_file_write` sha algorithm assumed sha256 | The returned sha equals the locally computed sha256; the script refuses on any mismatch and names the algorithm if it matches another |
| Parent-dir creation route unconfirmed | `--dry-run` names the route it will take; `ls -d` verifies the dir exists before any write |
| Tailscale serve/funnel unconfigured | `tailscale serve status` returns a config instead of "No serve config" |
| cloudflared connector is not a unit | `systemctl status cloudflared` returns something other than rc=4 |

**There is no third state.** An item is closed by its falsifier or it is PENDING.

---

## The three limbs

| Limb | Route | State |
|---|---|---|
| node1 `uni-lab` | LAN `10.190.245.121:8080` MCP; also `192.168.1.249` | reachable — deploy target |
| node2 `uni-lab-79740c` | via node1, `limb=uni-lab-79740c` | reachable — deploy target |
| tablet `uni-tab-arm-1` | none | **UNREACHABLE**, hands-on-device — [`TABLET.md`](TABLET.md) |

There are **only three limbs**. The workstation and the wired PC are wg **client peers**, not limbs,
and are not deploy targets.

**This bundle does not deploy fleet-wide.** It deploys to two of three limbs. Saying otherwise would
be a false claim about a box nobody has heard from in 3.5 days.
