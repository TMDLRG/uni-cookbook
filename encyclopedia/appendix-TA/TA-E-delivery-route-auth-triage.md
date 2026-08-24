# TA-E - The delivery-route ledger and auth-outage triage

This chapter records, as honest operational method, what a self-hosted publishing engine learned about staying alive when third-party authentication breaks. It claims no science and no capability. The subject is a marketing organism: a multi-container stack that authors content on a Claude subscription (CLI plus scheduler tools, never a server-side LLM loop) and pushes it to social platforms over fragile OAuth that only a human operator can refresh. Everything below is engineering and operational discipline. The honest position for the whole program stays printed and unsoftened: this is a developmental active-inference simulation, a bounded peek, a toy world and never a person, with roughly 2 of 11-plus developmental rungs earned. None of the operational rigor in this chapter moves that number.

The four claims here (ledger rows TA35 through TA38, Section 4.5) are all Class A: direct operational observations made while running the live engine, several of them learned the painful way during a sustained multi-day outage. Class A means observed at runtime; it does not mean "safe," and it does not mean "capability." Each row carries its own falsifier, and the single loudest fence (TA38) is a safety flag, not a feature. Plain ops vocabulary throughout: no framework names, no internal channel handles, no tokens.

## The auth-outage triage protocol (TA35, Class A)

Over a seven-day sustained outage the engine learned a fixed triage protocol for distinguishing a real authentication failure from a transient one, and for refusing the tempting wrong fix. The protocol, recorded exactly:

- Treat `publish_mode=dry` as report-only. In dry mode the engine must create no drafts, because draft creation silently no-ops, and a silent no-op reads as success in any after-the-fact summary. The canonical failure this whole program guards against is precisely that pattern: phases that "complete" while doing nothing.
- `authenticated:true` is a local session heuristic only. It is not the OAuth token. A box can report itself authenticated and still be unable to write to the platform.
- Single-probe, then report. Do one live-API read (for example, reading comments on a recent own-post). If that read 401s, skip the comment-scan, ladder, and analytics phases entirely rather than re-diagnosing a known multi-day outage from scratch on every sweep.
- Distinguish a 401 from a 403. A 401 means the token has expired: it is persistent, and it clears only when the operator re-authenticates. A 403 is a transient blip; writes typically return the same day on their own.
- Do not flip `publish_mode` to live to "fix" the outage. Flipping to live does not address the root cause; it only converts silent no-ops into hard 401s.

The paired negative travels in the same breath as the protocol: in the sampled late-June sweeps the live engine was in exactly such a sustained outage, with LinkedIn 401ing on reads, Reddit OAuth 401ing, nothing published for five-plus days, and roughly 190 posts queued. The engine's largest practical weakness is that it depends on third-party OAuth that only the operator can refresh. The agent never mints tokens and never enters credentials; re-authentication is handed to the owner as a precise click. That boundary is a hard rail, recorded across the archive (for example a Reddit 401 carrying `www-authenticate: Basic realm="reddit"` is a rotated client-secret, a two-minute operator re-issue, never an agent action).

Falsifier (operable): flipping `publish_mode` to live actually fixes an outage, or a 401 clears same-day without operator action. Either would overturn TA35.

## The idempotency / abort-but-succeeded gotcha (TA36, Class A)

A publish call can return `PUBLISHER_UNREACHABLE` or otherwise abort to the client while the sidecar has already succeeded server-side (wrote idempotency and published). The recorded rule: on any abort or timeout, check `idempotency.json` and the platform's Published list before running any fallback. This is not a precaution stated in the abstract. It is a recorded incident: a duplicate newsletter once went out to live subscribers and had to be deleted because a fallback ran without that check. The negative is the content here; the rule exists because the duplicate already happened.

Falsifier (operable): a fallback after an aborted publish never duplicates even without checking `idempotency.json`. That would overturn TA36.

## The anti-no-op real-tool-signature set (TA37, Class A)

Sweep skill files once shipped fictional tool signatures that silently no-op'd for months, so whole phases "completed" while doing nothing. The correction is a documented set of real, confirmed-working tool signatures, recorded so that no documented call quietly fails against the live schema:

- `sweep_manage` actions are only `run | schedule | history | health | mark_complete`.
- `linkedin_set_autonomy_mode(page_id, mode='auto')` is idempotent and is called directly (the list-pages call returns no autonomy field to read back).
- Own-post defense reads the `org_post_id` field (the live URN), then calls `linkedin_get_post_comments(post_urn=org_post_id)`. A `comment_count:0` everywhere is a complete result, not a failure.
- A `memory_store` payload must be valid JSON or it errors.
- When a skill call fails on a parameter or JSON error, fix the skill file and verify against the loaded tool schema, rather than merely flagging it.

The travelling negative is the origin defect itself: the silent-no-op phase that read as success in summaries for months. TA37 is the correction, and it is meaningless if cited without the failure it corrects.

Falsifier (operable): a documented signature here no-ops or errors against the live loaded tool schema. That would overturn TA37.

## The HARD go-live safety flag (TA38, Class A, negative/safety)

This is the loudest fence in the chapter and it is recorded as a negative, not a feature. `PUBLISH_MODE=dry` does NOT gate the publishers' Playwright path. A publish action taken with a live browser session CAN post live even while the environment is nominally in dry mode. The required action, before any live publishing, is to add `auto_publish=false` in `proxyPublisher`, and to stay in dry until that override is in place. Dry mode is not a safety net for the browser route; treating it as one is how a "test" run reaches real subscribers.

This row is a negative precisely because the intuitive safety assumption (dry means nothing posts) is false on the Playwright leg. It must never be softened into "dry mode keeps you safe," and the outage must never be "fixed" by flipping `publish_mode` to live (TA35) to force a post through.

Falsifier (operable): `PUBLISH_MODE=dry` is shown to actually block the Playwright publish path with a live session. That would overturn TA38.

### What is NOT claimed in TA-E

- Ceiling: a careless reader might infer that the publishing engine is safely autonomous, that "dry mode" is a guaranteed safety net, or that any of this operational rigor is evidence of intelligence or capability. None of that is shown. The most we claim is exactly four Class-A operational observations: a triage protocol that distinguishes a persistent 401 from a transient 403 and refuses the flip-to-live "fix" (TA35); a check-before-fallback rule that prevents duplicate publishes after an abort-but-succeeded (TA36); a documented real-tool-signature set that replaces a silent-no-op defect (TA37); and a hard safety flag that `PUBLISH_MODE=dry` does not gate the Playwright path so `auto_publish=false` must be set before live publishing (TA38).
- Fences engaged: the no-credentials / no-token rail (the agent never mints tokens, never enters credentials, never logs in or authorizes; re-auth is an operator click). The plain-ops-vocabulary guard (red line 12, vocabulary-leak): this is a Track-A chapter, so it uses ordinary operations language and never externalizes active-inference, EFE, or free-energy framing, and never prints internal channel handles. The no-PII / no-secrets rail (red line 10): no tokens, no channel handles, no client identities. The substrate-is-not-a-science-gate fence (red line 8): operational reliability is engineering, never a developmental rung.
- Negatives that travel with this claim (cite alongside, never strip): TA35 must be cited with the recorded live outage (five-plus days down, LinkedIn and Reddit both 401ing, roughly 190 posts queued, operator-only fix). TA36 must be cited with the actual duplicate-newsletter incident that forced the rule. TA37 must be cited with the months-long silent-no-op defect it corrects. TA38 is itself a recorded negative/safety row and must never be presented as a feature or as a reassurance that dry mode is safe.
- Parked / owed: no sign-to-park and no Class-A observation is owed for this chapter; all four rows are already Class A. The standing operational gap that surrounds them remains open and is named, not discharged: the engine depends on fragile third-party OAuth that only the operator can refresh, and the `social-publisher` browser-route cure still awaits its per-platform operator login. That dependency is a recorded weakness, not a solved problem.
- One-line honest summary a skeptic could not dispute: these are four hard-won operational rules for keeping a publishing engine from lying to itself or to its subscribers when auth breaks; they are reliability engineering, they prove no capability, and the loudest of them is a warning that "dry mode" does not make the browser path safe.

## Falsify this

The lead falsifier, stated operably: flip `publish_mode` to live during a real outage and show that it fixes the outage, or show a 401 clearing the same day with no operator action. Either result overturns the core of the triage protocol (TA35). The standing safety falsifier sits alongside it: demonstrate that `PUBLISH_MODE=dry` actually blocks the Playwright publish path with a live session, and TA38 falls. Until then, stay in dry, set `auto_publish=false` before any live publishing, and let the operator hold the only credentials.

## Sources

- Ledger: `CLAIM-LEDGER.md` Section 4.5, rows TA35-TA38 (Class A operational; TA38 negative/safety), with the surrounding Track-A negatives in Section 4.6 (TA-N1 through TA-N6 on the OAuth-fragility and dead-route bounds).
- Digest: `curated/orchestrate-linkedin-digest.md` (the auth-outage triage protocol, the anti-no-op real-tool-signature set, the idempotency/abort-but-succeeded gotcha, the publishing self-heal route ledger, and the operator-only credential boundary).
- Digest: `curated/uni-os-digest.md` (the go-live safety flag: `PUBLISH_MODE=dry` does not gate the Playwright path; add `auto_publish=false` in `proxyPublisher`; the operator-elevation wall).
- Archive provenance (PII-redacted, local-only, never quoted with identities): the ORCHESTRATE LinkedIn campaign archive (Track-A core) and the UNI.OS archive (substrate / go-live safety). No PII, no secrets, no tokens, no internal channel handles.
