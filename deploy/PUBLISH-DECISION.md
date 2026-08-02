# The exposure decision — for the operator, not decided here

## STATUS: STAGED, NOT DEPLOYED. NOTHING IS EXPOSED.

**No path in this document has been configured. The reader is not serving on any limb, and is not
reachable from the public internet by any route.** `tailscale serve status` returns "No serve
config". There is no `cloudflared.service`. This document exists so the exposure question is
answered **before** the deploy, deliberately, by the operator.

**This bundle does not make this decision and the deploy script does not implement any option
below.** `deploy_cookbook.py` copies files into an nginx root and nothing else. Every command here
is a separate, manual, operator-run act.

---

## The asymmetry that organizes the whole decision

The cookbook is **private research in a private repository**
(`github.com/TMDLRG/UNI-Encyclopedia-Cookbook`, stated private by the operator; not verified from
this box).

- **Private -> public** is one command, and takes effect in seconds.
- **Public -> private** is also one command — **and it does not undo the first one.**

Withdrawing a URL removes future access. It does not remove what was already taken. Between the
moment a path is public and the moment you withdraw it, anything that fetched the page keeps it:

- **Search engine indexes and their caches.** A crawler that fetched the page holds a copy. De-listing
  is a request to a third party, on their schedule, not a delete.
- **The Internet Archive and similar crawlers.** Explicitly designed to be permanent. Removal is a
  request, honored at their discretion.
- **Anyone who read, saved, screenshotted, scraped, or forked it.** No mechanism reaches these.
- **LLM training scrapes.** A corpus about UNI's method, published openly, may be ingested into a
  training set. There is no removal path from a trained model.

`robots.txt` and `noindex` are **requests to well-behaved crawlers**. They are not access control.
They do not bind a scraper that ignores them, and a scraper that ignores them is not exotic.

**So the honest framing is not "should this be public?" but "am I willing for this to be permanently
public, starting now?"** — because that is the only question the public options actually ask. The
reversal you get is reversal of *future* access, never of *past* access. A trial run is not
available at the public tier: there is no such thing as briefly public.

This asymmetry is the entire risk. Everything below is detail.

---

## The options

### Option A — Tailnet only (RECOMMENDED DEFAULT)

**Do nothing beyond the deploy.** node1 is already on the tailnet (`uni-lab-hub`,
`100.100.188.48`). Files in the nginx root are reachable at
`http://100.100.188.48/glass/cookbook/` the moment they land.

```
(no command — this is what the deploy already gives you)
```

| | |
|---|---|
| **Exposes** | the reader, over plain HTTP inside the tailnet |
| **To whom** | devices on your tailnet, authenticated by your identity provider |
| **How to reverse** | `python deploy/deploy_cookbook.py --rollback` (removes the directory); or remove node1 from the tailnet |
| **Cannot un-ring** | **nothing** — the audience is a closed set you control and can enumerate |
| **Depends on** | the Tailscale coordination service; the tailnet client on each device |

**Why this is the default:** it is the only option whose reversal is complete. The audience is
people you have already authorized. If the decision turns out wrong, undoing it actually undoes it.
It also costs zero configuration and adds zero moving parts to a box another session is working on.

**What it does not give you:** anyone outside the tailnet cannot read it. If the actual requirement
is "a person without a tailnet account must read this", Option A does not meet it — and that
requirement should be stated out loud, because it is the only thing that justifies the tiers below.

---

### Option B — Tailscale serve (private HTTPS inside the tailnet)

`serve` is **not** funnel. It stays inside the tailnet. It adds HTTPS with a real certificate and a
stable MagicDNS name.

```bash
# on node1 — proxy the existing nginx to a tailnet-only HTTPS endpoint
tailscale serve --bg https / http://127.0.0.1:80

# check what is configured
tailscale serve status

# reverse
tailscale serve --https=443 off
```

| | |
|---|---|
| **Exposes** | the reader over HTTPS, at a MagicDNS name |
| **To whom** | devices on your tailnet — **same audience as Option A** |
| **How to reverse** | `tailscale serve --https=443 off` — immediate, complete |
| **Cannot un-ring** | **nothing** — audience unchanged from A; the hostname enters Tailscale's cert log (public CT logs record the hostname, not the content) |
| **Depends on** | the same coordination service, plus one more moving part |

**Honest note:** Option B's *only* gain over A is HTTPS and a nicer name for the **same audience**.
It does not widen access. If you do not need HTTPS inside the tailnet, this is a moving part bought
for nothing. Note the certificate transparency log entry — that publishes the *hostname*, never the
content, but a hostname can itself be a disclosure if it is descriptive.

---

### Option C — Tailscale Funnel (PUBLIC INTERNET)

> **This publishes to the entire public internet. Anyone with the URL, and anyone who finds the URL,
> can read the cookbook. No account, no login, no allowlist. Crawlers will find it.**

```bash
# on node1 — THIS IS THE PUBLIC STEP
tailscale funnel --bg https / http://127.0.0.1:80

tailscale funnel status

# reverse — stops FUTURE access only
tailscale funnel --https=443 off
```

| | |
|---|---|
| **Exposes** | the entire reader directory, world-readable |
| **To whom** | **everyone.** Search crawlers, archivers, scrapers, LLM training pipelines, any person |
| **How to reverse** | `tailscale funnel --https=443 off` — stops new requests within seconds |
| **Cannot un-ring** | **search indexes and caches; the Internet Archive; anyone who already fetched, saved, or scraped it; any training corpus that ingested it.** The hostname is permanently in public CT logs even after withdrawal — a former Funnel hostname is a durable public record that the endpoint existed |
| **Depends on** | Tailscale's public relay infrastructure |

**Before choosing C, answer these out loud:**

1. Is every claim in the corpus one you are willing to defend publicly, permanently, under your
   name? The corpus carries negatives and open questions **on purpose** — is publishing them at this
   maturity what you want?
2. Does the corpus name people, machines, private endpoints, or internal addresses? A reader built
   from these chapters could carry them into a public page. **Nobody has audited the rendered
   output for this** — that audit is `not-yet-built` and is a hard prerequisite for C.
3. Is there an actual reader outside the tailnet, or is C being chosen because it is easy?
4. Is a specific, known person the audience? Then C is the wrong shape — it serves *everyone* to
   reach *one*.

**Falsifier for "the audit passed":** a human has read every file in `reader/dist/` and can name
what it discloses. Until then, C is not ready regardless of the decision.

---

### Option D — cloudflared tunnel (PUBLIC INTERNET, plus a new unit)

Credentials exist: tunnel `9b98a1bc-5dd9-4feb-8297-b579ef2727b4` in `config.yml`, ingress for
`dialwright.solwright.com` -> `https://localhost:8443` **only**. There is **no
`cloudflared.service`** (rc=4) — nothing runs this tunnel as a managed service.

Reaching the reader this way needs **both** a new ingress rule **and** a connector process, i.e. a
**new unit on node1**.

```yaml
# config.yml — a new ingress rule would be needed (NOT APPLIED, shown for the decision only)
ingress:
  - hostname: <a-hostname-you-choose>
    service: http://localhost:80
  - hostname: dialwright.solwright.com
    service: https://localhost:8443
  - service: http_status:404
```

| | |
|---|---|
| **Exposes** | the reader, world-readable, at a hostname you choose |
| **To whom** | **everyone** — same public audience as C |
| **How to reverse** | remove the ingress rule + stop the connector; DNS record removal is **subject to TTL caching** — not instant |
| **Cannot un-ring** | everything in C, plus the DNS name in public records and CT logs |
| **Depends on** | Cloudflare; a connector process that **has no unit, so nothing restarts it** |

**Two reasons this bundle will not do it, independent of the exposure question:**

1. **It requires a new unit on node1.** That is outside the static design's blast radius and is the
   one thing this bundle promises not to do.
2. **Another session is live on node1 and node2 right now** (registry, wg ListenPort, name map,
   PHARUS beacon). Adding a unit and editing `config.yml` enters its lane. **Do not do this while
   that session is live**, whatever the exposure decision is.

Option D also touches `dialwright.solwright.com`'s config file. A mistake there breaks a *different*
live service. That risk is not the reader's to take.

---

## Side by side

| | **A: tailnet** | **B: serve** | **C: Funnel** | **D: cloudflared** |
|---|---|---|---|---|
| Audience | your devices | your devices | **the world** | **the world** |
| Public internet | no | no | **YES** | **YES** |
| Work to configure | none | one command | one command | ingress + **a new unit** |
| Reversal | complete | complete | **future access only** | **future access only**, + DNS TTL |
| Permanent residue | none | hostname in CT log | **indexes, archives, scrapes, CT log** | **all of C + DNS records** |
| Touches the live session's lane | no | no | no | **YES** |
| New moving parts on node1 | 0 | 1 | 1 | 2 |

---

## The recommendation, and its limit

**Recommended default: Option A — tailnet.** It is private, its reversal is complete, it costs no
configuration, it adds nothing to a box another session is working on, and it already works the
moment the deploy lands.

**Public exposure (C or D) requires an explicit operator decision.** This bundle will not make it,
will not prepare it, and will not leave it one flag away. Two things must be true first, and
neither is true today:

1. **A human has read the rendered output** and can name what it discloses. `not-yet-built`.
2. **A named reader exists outside the tailnet** who cannot be served by A or B.

If both become true, C is the cheaper and cleaner of the two public options — it needs no unit and
does not touch the live session's lane. D's only advantage is a custom hostname, bought with a new
unit on a box that is currently busy.

**The decision is the operator's. It is not made here, and nothing here presumes it.**
