# uni-tab-arm-1 — why the tablet is not covered

## STATUS: STAGED, NOT DEPLOYED — and the tablet is not even a target

**Card this PENDING. It does not close in this bundle.**

The Cookbook Reader is not deployed to any limb. The tablet is additionally **not reachable at all**,
so it is not in `LIMBS` in `deploy_cookbook.py` and no code path in this bundle attempts it.

**This bundle is a 2-of-3-limb deploy. It is not fleet-wide. Do not record it as one.**

---

## The state, as observed

| | |
|---|---|
| **Limb** | `uni-tab-arm-1` (limb3, the Android tablet, via Termux + termuxbridge) |
| **Expected mesh address** | `10.13.13.5` (wg peer) |
| **Reachability** | **UNREACHABLE** |
| **Silent for** | ~3.5 days as of 2026-07-15 |
| **Deploy state** | `not-yet-built` — nothing attempted, nothing written |
| **Route swept by** | the concurrent network session; **all routes negative** |
| **Required to fix** | **hands on the physical device** |

The other two limbs are up. node1 answers on LAN (`10.190.245.121:8080`, 38 tools). node2 answers
through node1 (`limb=uni-lab-79740c`, `ok=True`). **The tablet answers on nothing.**

---

## Why this is a separate outage, and not the mesh one

This matters, because conflating the two would send the operator to fix the wrong thing.

**The mesh outage** (this workstation cannot reach the fleet over wg) is a *client-peer* problem:
this box is pinned to a dead literal `10.190.245.122` while node1 moved to `.121`. It is worked
around by using the LAN, and node1 <-> node2 mesh traffic is unaffected.

**The tablet outage is not that.** node1 and node2 reach each other over the mesh right now. The
tablet does not appear on it. Being a wg peer is not the issue — being *present* is.

The tablet has done this before, and the previous cause is a hypothesis, not a diagnosis, for this
occurrence: on 2026-07-11 it was recovered by fixing a WireGuard `Endpoint` (a dead public IP ->
the LAN IP) and restarting `termuxbridge`. That is a **plausible prior**, not a finding. It has not
been observed this time and must not be reported as the cause.

**The honest state is: the tablet is silent and nobody knows why.** Anything more specific is a
guess.

---

## Why no route can close this remotely

- **Android + Termux is not a systemd box.** There is no unit to restart from node1, no MCP agent
  answering, nothing to poll. The bridge is a userspace process that Android may kill for battery,
  doze, or an OOM decision — with no supervisor to bring it back.
- **The `limb=` route runs *through* node1's MCP.** If the tablet is not on the mesh, node1 has
  nothing to forward to. `limb=uni-tab-arm-1` cannot dial a peer that is not there.
- **The android limb tree is device-local.** It is not in this repository. There is no copy here
  that could be pushed even if a route existed.
- **All routes were swept negative by the network session.** Which brings us to the trap:

### The negative-result trap, stated so it is not walked into again

**Silence is not death.** ICMP is policy-dropped across this fleet — a `ping` timeout means
*nothing*. This session class has already made that error once: ICMP silence was read as a dead
fleet, and the fleet was fine.

**So the falsifier below is deliberately positive.** It requires a box to *speak*, not to fail to
answer. A negative result here is a **hypothesis**, not a finding, until a positive control proves
the instrument works — and the positive control is already in hand: **node1 and node2 answer through
the very same MCP.** The instrument works. The tablet specifically is not answering.

That is a real observation. It is also the *only* one. It says the tablet is not reachable. It does
**not** say the tablet is off, broken, dead, wiped, or anything else. Nobody has looked at it.

---

## The falsifier that closes this PENDING

> **`limb=uni-tab-arm-1` `os_sysinfo` returns `ok=true`.**

That is the whole test. One positive observation, through the same node1 MCP that node2 already
answers on. Until it returns `ok=true`, the tablet is unreachable and the reader is `not-yet-built`
there.

When it passes, the tablet becomes a deploy target — and the work is small: add it to `LIMBS` in
`deploy_cookbook.py`:

```python
{"name": "node3", "limb": "uni-tab-arm-1"},
```

...and re-run. The script is idempotent, so re-running against node1 and node2 is safe and simply
re-verifies their shas. **But do not add that line before the falsifier passes** — a limb that
cannot be reached will make the script refuse, which is correct behaviour but not a useful way to
learn what you already know.

**Whether the tablet's Termux/nginx even serves `/opt/uni/services/glass/ui/` on the same path is
itself unconfirmed** — the android limb is a different shape of box (its `:8443` is legitimately
different). Assume nothing about the path until someone reads the device. That is a second PENDING
hiding behind the first.

---

## What the operator must do, on the device

**This needs hands. There is no remote path.** Roughly, in order:

1. **Pick up the tablet. Wake it.** Confirm it is powered and on the network at all.
2. **Open Termux.** Confirm the app is alive and was not killed or updated out from under itself.
3. **Check the bridge:** is the `termuxbridge` process running? Android may have killed it for
   battery/doze/OOM — that is the highest-prior cause on this class of device.
4. **Check WireGuard:** `wg show` on the device. Is the interface up? Is the `Endpoint` for node1
   still pointing at a **live** address? **node1 moved to `10.190.245.121`.** A peer pinned to an
   old literal is exactly the failure this fleet already had twice — once on this very tablet
   (2026-07-11), once on this workstation (still live today).
5. **Re-establish the mesh**, then run the falsifier **from node1**: `limb=uni-tab-arm-1`
   `os_sysinfo`.

Item 4 is the highest-value probe: it is cheap, it is the known prior for **both** boxes that have
gone silent on this fleet, and node1's address change is a known, dated event. **Look there first.**

If none of that explains it, the state is still honestly "unknown" — and the next step is
observation, not a theory.

---

## What this bundle does about it

**Nothing, deliberately.** It deploys to the two limbs that answer, records that it did so, and
leaves this card open. It does not:

- attempt the tablet and swallow the failure
- claim a fleet-wide deploy
- assume the 2026-07-11 `Endpoint` fix is the cause again
- report "the tablet is down" as a finding — the finding is **"the tablet is not reachable"**, and
  the difference between those two sentences is the whole discipline

When the falsifier passes, the tablet is one line and one re-run away.

---

## CORRECTION 2026-07-16 - this file's original falsifier was UNSATISFIABLE

The text above is the record as written and is **left unedited**. This note is appended, not
substituted. Calibration is down-only; the prior wording stays on record.

The original PENDING carried the falsifier *"os_file_write limb=uni-tab-arm-1 returns ok=true with
a verifiable sha."* That test **can never pass**. `uni-tab-arm-1` does not run `uni-control-mcp`;
it runs `uni-android-limb-agent`, which implements exactly five tools, and `os_file_write` is not
among them. The agent says so itself when asked directly (`POST 10.13.13.5:8091/mcp`):

```
HTTP 400  {"error": "unknown tool os_file_read",
           "available": ["os_sysinfo","glass_telemetry","podman_ps","podman_images","podman_run"]}
```

A falsifier that cannot fire is a **fence wearing a falsifier's clothes** - the exact defect this
corpus exists to bar, shipped by this corpus. It is struck.

**Three further claims are struck**, all one error class - a blind instrument read as a finding:

| Struck claim | What is actually true | Receipt |
|---|---|---|
| "the tablet is unreachable" | It is reachable. | `os_sysinfo` -> SAMSUNG-SM-T377A, android 7.1.1, abi armeabi-v7a, uptime 19475.62s, `server: uni-android-limb-agent`, `routedTo: remote` |
| "the mesh error is false - a capability gap wearing a reachability message" | **The error was accurate for the moment it fired.** `_forward_android_stdlib` (sha 4aac2a46) has two distinct exits: `resp is None` -> *"could not be reached over the mesh"*; `status >= 400` -> *"returned HTTP N"*. The probe hit the first because the agent process was genuinely down (adb/USB work on the device at that time). Two honest snapshots of a lifecycle, not one inconsistent code path. | live router read + direct-to-agent HTTP 400 |
| "the tablet's calls cannot be proven, only believed" (`audit_id: None`) | `_route_remote()` writes to node1's ledger **unconditionally for every routed call**. The missing `audit_id` is a missing **echo**, not a missing **entry**. Completeness gap, not security gap. | `{"audit_id":"349a30cc80b94b88","event":"limb_route","tool":"os_sysinfo","limb":"uni-tab-arm-1","ok":true}` |

## OBSERVED 2026-07-16 - the tablet IS deployable, and here is the path

Probed from the workstation (10.190.245.117 -> 10.190.245.151, same LAN segment; 8443, 8091, 8022
all OPEN). The `:8443` glass is its **own static-file python3 process** (pid 8857,
`Server: BaseHTTP/0.6 Python/3.13.13`) reading plain files from `/sdcard/UNI.DDNA.OS/limb/glass-ui/`.
**It serves generic nested static files**, and the serve prefix is `/glass/`, not the root - which
is why a naive probe of `/index.html` 404s and looks like a dead server:

```
/glass/                      200   110,135 B
/glass/config.json           200     5,171 B   application/json; charset=utf-8
/glass/configure.html        200    34,848 B   text/html; charset=utf-8
/glass/configure.js          200    25,768 B   application/javascript; charset=utf-8
/glass/nope-27942/x.html     404              <- POSITIVE CONTROL: can see a miss
/glass/cookbook/index.html   404              <- the target, currently free
```

MIME derives per-extension and nested paths resolve - a real static handler over `glass-ui/`, not
an allowlist of four filenames. **The third limb is a file copy and nothing else**: no unit, no
port, no config, no restart.

- **source** `reader/dist/` - 99 files + `_provenance.json`, ~6.85 MB, pure ASCII by construction
- **target** `/sdcard/UNI.DDNA.OS/limb/glass-ui/cookbook/` (subdirs chapter, ledger, lexicon, plate)
- **`_provenance.json` is written LAST** - it is the completeness marker; a half-copied tree that
  advertises itself as complete is the failure mode the deploy script exists to prevent
- **transport**: Termux `ssh -p 8022` (proven from node1) or the termuxbridge RUN_COMMAND
  broadcast. **Not** the MCP: `os_file_write` does not exist on this limb.

**Blocked on**: no ssh credential for the tablet from the workstation (`ssh -p 8022
root@10.190.245.151` -> Permission denied (publickey,password,keyboard-interactive); the
`uni_deploy` key is not on this box - `root@node1` refuses it too). Needs a key placed for this
box, or the network session / operator to perform the copy.

## THE REPLACEMENT FALSIFIER (satisfiable, observable, guarded)

> `GET https://10.13.13.5:8443/glass/cookbook/_provenance.json` returns **200** AND reports
> **commit 3b8e061** AND **file_count 99**.

**Its positive controls - both must pass or the result is VOID:**

1. `GET /glass/config.json` -> **200** (the prober can see a hit)
2. `GET /glass/nope-<random>/x.html` -> **404** (the prober can see a miss)

If either control fails, report **nothing**. A negative result is a hypothesis, not a finding,
until a positive control proves the instrument works. Borrowed from the network session's
`route_proof.py`, which exits **VOID (rc=2)** rather than let its own blindness look like a
finding.

**Until that falsifier returns 200, this deploy is carded 2-of-3 and is NOT fleet-wide.**

---

## CLOSED 2026-07-16 - third limb DEPLOYED and INDEPENDENTLY VERIFIED. 3 of 3.

The network session held the working ssh:8022 credential this workstation lacked and drove the
file-copy itself (tar+gzip -> base64 -> chunk-write to node1 -> reassemble/verify in a throwaway
busybox container -> ssh:8022 into the tablet's `/sdcard/UNI.DDNA.OS/limb/glass-ui/cookbook/`,
`_provenance.json` written LAST). Two real transport gotchas it hit and worked around, recorded for
the next person: Linux `MAX_ARG_STRLEN` caps a single exec argv element at 128 KB (chunk size
600 KB -> 100 KB, 22 round-trips); GNU tar throws `Cannot utime`/`Cannot change mode` on Android's
FUSE `/sdcard` (cosmetic - content lands intact).

**The replacement falsifier was run for real, and I re-ran it independently from the workstation
rather than trust the receipt** - the same courtesy the network session extended by reproducing my
findings instead of accepting them:

```
[control +] GET /glass/config.json           200   (prober can see a hit)
[control -] GET /glass/nope-<random>/x.html  404   (prober can see a miss)   -> not blind
GET /glass/cookbook/_provenance.json         200   state COMPLETE, commit 3b8e061,
                                                    file_count 99, limb uni-tab-arm-1
```

And beyond the marker, an independent **sha256 content cross-check** (tablet-served bytes vs this
repo's local `reader/dist/`), because `_provenance.json` proves a marker landed, not that 99 files
did:

```
lexicon/hi.html     MATCH   238,669 B    <- Hindi: the multi-byte transport-corruption risk case
lexicon/sa.html     MATCH   238,665 B    <- Sanskrit: same
chapter/cn-10.html  MATCH   125,689 B
theme.css           MATCH    42,470 B
index.html          MATCH    39,807 B
```

5/5 byte-identical. The two multilingual files - the exact case the pure-ASCII emit design was
built to protect - landed byte-perfect through a base64+tar transport, which is what ASCII-only
bytes (numeric character references for all Devanagari/IAST) buy you.

The tablet's `_provenance.json` `deployed_by` field states plainly it was a manual ssh copy on the
build session's behalf, **not** `deploy_cookbook.py` - SIGNUM SIGNUM MANET applied to the
provenance record itself. Nothing on the tablet was touched outside the new `cookbook/`
subdirectory: no unit, no port, no config, no restart.

**All three limbs now serve commit 3b8e061:**

| limb | serve | verified |
|---|---|---|
| `uni-lab` (node1) | `https://10.190.245.121/glass/cookbook/` | 200 + control, commit 3b8e061, 99 files |
| `uni-lab-79740c` (node2) | via nginx, checked over the MCP | commit 3b8e061, 99 files, COMPLETE |
| `uni-tab-arm-1` (tablet) | `https://10.13.13.5:8443/glass/cookbook/` (LAN `10.190.245.151:8443`) | 200 + both controls + 5/5 sha256 content MATCH |

This deploy is now fleet-wide. It is recorded as one because it was observed as one.

---

## NOTE 2026-07-16 - INTENTIONAL divergence on the tablet copy (do not overwrite blindly)

The tablet's `/sdcard/UNI.DDNA.OS/limb/glass-ui/cookbook/index.html` has been intentionally
customised by the network session (`UNI-OS Fleet network self-healing mesh`, their commit
`9f1c68f`, applied via `lab-os/beacon/tools/add_icon_bar_to_tablet_uis.py` on branch
`selfnet/pharus-beacon`). The customisation adds an icon-bar; the file diverges byte-for-byte
from this repo's `reader/dist/index.html`.

**When re-deploying the tablet to a new commit**, two paths, operator's choice:
1. **Overwrite** — let `deploy_cookbook.py` (or the equivalent ssh:8022 copy) write the fresh
   `index.html` and `_provenance.json`. The icon-bar is lost until re-applied.
2. **Preserve** — deploy every file EXCEPT `index.html`, then have the network session re-run
   `add_icon_bar_to_tablet_uis.py` against the freshly-deployed base.

There is no correct default. Ask before the next tablet deploy.
