# Cookbook Reader — architecture

## STATUS: STAGED, NOT DEPLOYED

**This document describes a design, not a running system.** The reader is not serving on any limb.
Every "each limb serves" sentence below is the design's intent in the present tense of the design —
it is not an observation. Nothing here has been observed on a live box, because nothing has been
fired. See [`README.md`](README.md).

---

## The one decision everything follows from: the reader is STATIC

The reader is a directory of immutable files — HTML, CSS, JSON — copied into an nginx serve root
that node1 already serves. No process. No database. No API. No write path at runtime.

This is not a limitation the design tolerates. **It is the design.** Every hard problem below is
absent rather than solved, and each one is absent *because* the reader is static:

| The problem active-active normally forces you to solve | Why it does not exist here |
|---|---|
| Split-brain (two limbs accept conflicting writes) | **There is no write path.** Nothing on a limb can author a change to the corpus. Two limbs cannot diverge from each other because neither can diverge from the commit it was given. |
| Replication / consensus / quorum | Nothing to replicate. Each limb gets its own complete, immutable copy pushed from the workstation. No limb reads another limb. |
| Leader election, failover of a leader | There is no leader. Every limb is a peer serving bytes. |
| Session affinity, sticky routing | Every request is idempotent and stateless. Any limb answers any request identically. |
| Cache invalidation across limbs | The content is content-addressed. A different corpus is a different commit, so a different deploy. |
| Data loss on a limb dying | A limb holds no unique state. It is a cache of a git commit. Its loss costs nothing; its rebuild is a re-run of the deploy. |

**Keep it static.** The moment the reader gains a write path — a comment box, a bookmark, a
search-index the box mutates, a hit counter — every row in that right-hand column becomes a real
distributed-systems problem, and this design's entire honesty argument collapses. If a future
feature needs server-side state, it does not belong in this reader; it belongs in a separate organ
with its own architecture and its own ledger.

---

## Content addressing: a limb advertises what it serves

Each limb serves a static `/glass/cookbook/_provenance.json` describing the exact bytes it holds:

```json
{
  "state": "COMPLETE",
  "commit": "f1be79446b845d5b642b74d3e963cd1f5ce05632",
  "commit_short": "f1be794",
  "repo_clean": true,
  "limb": "node1",
  "deployed_at_utc": "...",
  "file_count": 0,
  "files": { "index.html": "<sha256>", "...": "<sha256>" }
}
```

The point is one property: **a stale limb is visibly stale, not silently wrong.**

Anyone — operator, script, or reader — can `GET` each limb's `_provenance.json`, compare `commit`
against `git rev-parse HEAD`, and know exactly which limb is behind. There is no inference, no
heartbeat to interpret, no "it looks up". Staleness is a fact you read, not a state you guess.

Two properties make this hold:

- **`_provenance.json` is written LAST.** A half-copied tree has no `_provenance.json` (first
  deploy) or still carries the previous commit's file (re-deploy). It never advertises a completeness
  it does not have. During a re-run the script first overwrites it with `"state":
  "DEPLOY-IN-PROGRESS"`, so an interrupted re-deploy is visibly mid-flight rather than falsely
  complete.
- **Every file's sha256 is listed.** The advertisement is falsifiable file-by-file, not just at the
  commit level. If a limb claims commit X, you can check that its bytes actually are commit X's
  bytes.

**What `_provenance.json` does NOT do:** it does not make a limb serve the right thing. It makes a
limb *tell the truth about what it serves*. Nothing enforces freshness. A limb can serve a
6-month-old commit forever and its provenance will honestly say so, and no alarm will fire. **There
is no automatic staleness detection in this design.** Closing that would need a checker organ that
polls each limb and compares against HEAD — `not-yet-built`, out of scope, and named here so it is
not mistaken for present.

---

## The five serve paths, each with its real status

The reader is one directory of files. Everything below is about how a request reaches it. **A path
being LIVE means nginx is serving that path today — it does not mean the reader is there.** The
reader is on none of them.

### 1. LAN — node1 `10.190.245.121:443`, also `192.168.1.249:443`

**Status: LIVE.** nginx on node1 binds `0.0.0.0:443` and serves both LANs (they are routed).
This is where the deploy lands first and where the operator will observe it.

**Failure modes.** Single box: node1 down = this path dead, no failover, nothing reroutes. Requires
being on the LAN (or routed to it) — nothing off-LAN reaches it. Both addresses are the *same
nginx on the same box*: two addresses are not two limbs, and treating `.121` and `192.168.1.249` as
redundancy is a category error. **The workstation's own reachability is by LAN only** — it is a wg
client peer pinned to a dead literal `10.190.245.122` while node1 moved to `.121`, so the mesh path
from *this* box is down even though the mesh itself is up between the limbs.

### 2. wg mesh — `10.13.13.1` (node1), `10.13.13.3` (node2)

**Status: LIVE between node1 and node2.** This is the path that makes active-active real: both
limbs serve their own copy on the mesh, so a client on the mesh can ask either one.

**Failure modes.** **No health-aware failover.** There is no load balancer and this design does not
add one. A client picks an address; if that limb is down, the client gets a connection failure and
must pick the other **by hand**. Nothing detects, nothing reroutes, nothing retries. Active-active
here means "both are serving", not "something fails over for you" — those are different claims and
only the first is true. A mesh outage severs `limb=` routing fleet-wide; a cold start (all boxes at
once) is the known deadlock. **Not reachable from the workstation today** (see path 1).

### 3. Tailnet — `uni-lab-hub` `100.100.188.48`

**Status: LIVE, zero work.** node1 is already on the tailnet. The moment files land in the nginx
root, they are reachable at `http://100.100.188.48/glass/cookbook/` from any device on the tailnet.
No configuration, no new port, no new exposure.

**This is the recommended access path** (see [`PUBLISH-DECISION.md`](PUBLISH-DECISION.md)): private
to the tailnet, authenticated by the tailnet, reversible by removing the device.

**Failure modes.** node1-only — node2 is not on the tailnet, so this path has **no redundancy at
all**; node1 down = dead. Requires the tailnet client and an authorized account. Depends on a
third-party coordination service being up. MagicDNS names cache; a device that moves may be reached
at a stale name until TTL expiry.

### 4. Tailscale serve / funnel

**Status: AVAILABLE, UNCONFIGURED.** `tailscale serve status` returns "No serve config" (rc=0). The
binary is there; nothing is configured.

- `tailscale serve` = HTTPS **inside the tailnet** (private, a real cert, a nicer name).
- `tailscale funnel` = **PUBLISHES TO THE PUBLIC INTERNET.**

**These two are one command apart and their consequences are not comparable.** Do not treat them as
variants of one feature.

**Failure modes.** `serve`: another node1-only path; adds a moving part for a hostname. `funnel`:
world-readable, including to crawlers and caches — see `PUBLISH-DECISION.md`. This bundle configures
neither.

### 5. cloudflared tunnel

**Status: CREDENTIALS EXIST, CONNECTOR IS NOT A UNIT, INGRESS NOT CONFIGURED FOR THE READER.**

`config.yml` holds tunnel `9b98a1bc-5dd9-4feb-8297-b579ef2727b4` and its credentials, with ingress
for **`dialwright.solwright.com` -> `https://localhost:8443` only**. There is **no
`cloudflared.service`** (`systemctl status cloudflared` -> rc=4). Nothing is running this tunnel as
a managed service.

Reaching the reader this way needs an ingress rule **and** a connector process — i.e. a new unit on
node1. **That is exactly what this bundle refuses to do**, both because it is out of the static
design's blast radius and because another session is live on node1. Public exposure via this path
is a separate, operator-driven decision.

**Failure modes.** Public by nature (same one-way exposure as Funnel). Depends on Cloudflare and on
a connector staying up — with no unit, nothing restarts it. Adding the unit collides with the live
session's lane. DNS TTL caching means a hostname change is not instant and **de-publishing is not
instant either**.

---

## Failure modes shared by every path

Stated once, applying to all five:

- **DNS TTL caching.** Any name-based path (MagicDNS, `serve`, cloudflared hostname) is cached by
  resolvers. A change is not immediate and neither is a withdrawal. Removing a name does not remove
  it from caches that already hold it.
- **No health-aware failover anywhere.** No load balancer, no VIP, no anycast, no client retry
  logic. Redundancy in this design means "another limb also has the bytes", not "traffic moves". A
  client that picked a dead limb stays broken until a human points it elsewhere.
- **No staleness enforcement.** `_provenance.json` reports; nothing reconciles.
- **node2 is on the mesh only.** Of the five paths, node2 answers on exactly one (path 2). The
  "active-active" property is real only for mesh clients. **A LAN or tailnet client has no
  redundancy** — those paths are node1-only. This is the honest scope of the redundancy claim.
- **The tablet answers on none of them.** See [`TABLET.md`](TABLET.md).

---

## Deploy flow

```
workstation (this box)
  |
  |  1. python reader/build.py          -> reader/dist/   (local, pure ASCII asserted)
  |  2. git rev-parse HEAD              -> the content address
  |
  |  MCP over HTTP (JSON-RPC + SSE), LAN 10.190.245.121:8080
  |  NO SSH from here; os_file_write is the transport
  v
node1 "uni-lab"                          node2 "uni-lab-79740c"
  /opt/uni/services/glass/ui/cookbook/     /opt/uni/services/glass/ui/cookbook/
  served by the EXISTING nginx             served by the EXISTING nginx
  (no unit, no config edit, no reload)     (reached via node1, limb=uni-lab-79740c)
```

**Order is load-bearing:** node1 fully (files, then `_provenance.json` last), then node2 the same
way. Never `_provenance.json` before the files it describes.

**Why the reader emits pure ASCII:** `os_file_write` silently corrupts multi-byte UTF-8 — it drops
bytes and still returns `ok=true` with a sha-verified read-back lie. The reader emits pure ASCII so
**the bug cannot fire**, and the deploy script asserts it and refuses on the first non-ASCII byte.
This is a guard against a known-live defect, not a style preference. It is why the reader cannot
render the corpus's em-dashes and accented citations as literal bytes — that is a real cost of
this transport, accepted knowingly.

**Why parent dirs are created and verified first:** `os_file_write` silently no-ops when the parent
directory is missing — and still returns `ok=true` with a sha-verified read-back lie. A write whose
success cannot be distinguished from a no-op is not a receipt. The script creates the dirs, proves
them with `ls -d`, and refuses if it cannot.

---

## What this design deliberately does not have

Named so nobody mistakes absence for oversight:

- no load balancer, no VIP, no anycast, no health checks
- no automatic failover, no automatic staleness detection, no reconciliation
- no server-side search, no comments, no bookmarks, no analytics, no hit counters
- no runtime write path of any kind
- no new unit, quadlet, nginx config, or reload on any box
- no tablet coverage

Each is absent because a static reader does not need it. Each would have to be argued for on its own
merits, against the blast radius it costs.
