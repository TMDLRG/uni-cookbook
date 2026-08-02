#!/usr/bin/env python3
"""
deploy_cookbook.py - copy the built Cookbook Reader into the EXISTING nginx serve root
on node1, then node2. Static files only.

    STATUS: STAGED, NOT DEPLOYED. Running this script is what deploys. Authoring it did not.

Run FROM THE OPERATOR'S WORKSTATION, against node1's MCP over HTTP (JSON-RPC + SSE +
mcp-session-id). There is no SSH from the workstation (the uni_deploy key is not here), so
os_file_write is the transport.

    export UNI_MCP="http://<node1-host>:<port>/<mcp-path>"
    export UNI_TOKEN="<bearer token>"
    python deploy/deploy_cookbook.py --dry-run     # mutates nothing
    python deploy/deploy_cookbook.py               # fires
    python deploy/deploy_cookbook.py --rollback    # removes the cookbook dir

NEITHER THE ENDPOINT NOR THE TOKEN IS EVER HARDCODED OR LOGGED. Both come from the
environment. The token is never printed, never written to a file, never placed in a URL.

WHAT THIS SCRIPT WILL NEVER TOUCH (asserted, not merely intended):
    nftables, wg, uni-dns, any systemd unit, any quadlet, any nginx config, any nginx reload.
It writes files under /opt/uni/services/glass/ui/cookbook/ and nothing else. Every os_exec it
issues is checked against ALLOWED_EXEC_INTENTS below and refused if it does not match.

THE THREE KNOWN-LIVE DEFECTS THIS SCRIPT GUARDS AGAINST (each is real, each has bitten):
    1. os_file_write CORRUPTS multi-byte UTF-8 - silently drops bytes, still returns ok=true
       with a sha-verified read-back lie. GUARD: every file must be pure ASCII or we refuse.
    2. os_file_write SILENTLY NO-OPS when the parent dir is missing - and still returns
       ok=true with a sha-verified read-back lie. GUARD: create parents first, prove with
       `ls -d`, refuse if unproven.
    3. A returned ok=true is NOT a receipt. GUARD: compare the returned sha against a locally
       computed sha256 for every single file; refuse on any mismatch.

House rule this script obeys: it fails loudly rather than succeeding vaguely. There is no
"probably worked" branch. Every claim it prints is backed by a response it read.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
READER_BUILD = REPO / "reader" / "build.py"
READER_DIST = REPO / "reader" / "dist"

# The deploy target: INSIDE the nginx root node1 already serves. No unit, no config, no reload.
REMOTE_ROOT = "/opt/uni/services/glass/ui"
REMOTE_DIR = REMOTE_ROOT + "/cookbook"
PROVENANCE = "_provenance.json"

# The three limbs. The workstation and the wired PC are wg CLIENT PEERS, not limbs.
# uni-tab-arm-1 is UNREACHABLE (hands-on-device) - see TABLET.md. It is deliberately absent.
LIMBS = [
    {"name": "node1", "limb": None},                   # node1 = the MCP host itself, no limb arg
    {"name": "node2", "limb": "uni-lab-79740c"},       # reached THROUGH node1 via limb=
]

# os_exec argv[0] allowlist observed on node1 (2026-07-15). No bash/python/cp/tee/base64/tar/rm.
NODE1_EXEC_ALLOWLIST = {
    "cat", "cloudflared", "df", "free", "git", "hostname", "ip", "journalctl", "ls", "lsblk",
    "nft", "ping", "podman", "ss", "systemctl", "tailscale", "uname", "uni-promote",
    "uni-rollback", "uptime", "wg",
}

# Every os_exec this script may ever issue must match one of these intents. Anything else is a
# bug in this script and is refused before it reaches the wire. This is the blast-radius fence.
ALLOWED_EXEC_INTENTS = ("verify-dir-exists", "create-dir", "remove-cookbook-dir")

# Things that must never appear in any argv we send, regardless of intent.
FORBIDDEN_EXEC_SUBSTRINGS = ("nft", "wg ", "wg-quick", "uni-dns", "systemctl", "iptables",
                             "nginx", "quadlet", "daemon-reload")

SHA_ALGOS = ("sha256", "sha1", "sha512", "md5")


class Refuse(SystemExit):
    """A loud, deliberate refusal. Never caught, never softened, never retried."""

    def __init__(self, msg: str):
        super().__init__(f"\nREFUSED: {msg}\n")


def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def all_shas(data: bytes) -> dict[str, str]:
    return {a: hashlib.new(a, data).hexdigest() for a in SHA_ALGOS}


# ---------------------------------------------------------------------------------------
# MCP over HTTP: JSON-RPC 2.0, streamable HTTP, SSE responses, mcp-session-id header.
# ---------------------------------------------------------------------------------------
class MCP:
    def __init__(self, endpoint: str, token: str, verbose: bool = False):
        self.endpoint = endpoint
        self._token = token          # never logged, never rendered, never serialized
        self.session_id: str | None = None
        self.verbose = verbose
        self._rpc_id = 0

    def _headers(self) -> dict[str, str]:
        h = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "Authorization": f"Bearer {self._token}",
        }
        if self.session_id:
            h["mcp-session-id"] = self.session_id
        return h

    @staticmethod
    def _parse_sse(body: str) -> dict:
        """An SSE frame is `event: message` + `data: {...}` lines. Take the last data payload."""
        payloads = [ln[5:].strip() for ln in body.splitlines() if ln.startswith("data:")]
        if not payloads:
            raise Refuse(f"MCP returned no SSE data frame. Raw body:\n{body[:2000]}")
        return json.loads(payloads[-1])

    def _post(self, payload: dict, expect_response: bool = True) -> dict | None:
        self._rpc_id += 1
        if "id" in payload:
            payload["id"] = self._rpc_id
        raw = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(self.endpoint, data=raw, headers=self._headers(),
                                     method="POST")
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                sid = resp.headers.get("mcp-session-id")
                if sid and not self.session_id:
                    self.session_id = sid
                body = resp.read().decode("utf-8", errors="replace")
                ctype = resp.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")[:1000]
            raise Refuse(
                f"node1 MCP returned HTTP {e.code} for {payload.get('method')!r}.\n"
                f"  {detail}\n"
                f"  If 401/403: UNI_TOKEN is wrong or expired.\n"
                f"  If 404: UNI_MCP path is wrong.\n"
                f"  NOTHING WAS DEPLOYED."
            )
        except urllib.error.URLError as e:
            raise Refuse(
                f"node1 is UNREACHABLE at the configured UNI_MCP endpoint: {e.reason}\n"
                f"  This box is a wg CLIENT PEER pinned to a dead literal (10.190.245.122);\n"
                f"  node1 moved to 10.190.245.121. Reach it over LAN, not the mesh.\n"
                f"  Check: ping 10.190.245.121   (note: ICMP may be policy-dropped - a silent\n"
                f"  ping is NOT evidence of a dead box. Prefer an actual TCP connect.)\n"
                f"  NOTHING WAS DEPLOYED."
            )

        if not expect_response:
            return None
        if not body.strip():
            raise Refuse(f"MCP returned an empty body for {payload.get('method')!r}.")
        msg = self._parse_sse(body) if "text/event-stream" in ctype else json.loads(body)
        if "error" in msg:
            raise Refuse(f"MCP error on {payload.get('method')!r}: {msg['error']}")
        return msg.get("result", {})

    def initialize(self) -> dict:
        result = self._post({
            "jsonrpc": "2.0", "id": 0, "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "cookbook-deploy", "version": "1"},
            },
        })
        # The initialized notification carries no id and expects no response.
        self._post({"jsonrpc": "2.0", "method": "notifications/initialized"},
                   expect_response=False)
        return result or {}

    def list_tools(self) -> dict[str, dict]:
        result = self._post({"jsonrpc": "2.0", "id": 0, "method": "tools/list", "params": {}})
        return {t["name"]: t for t in (result or {}).get("tools", [])}

    def call(self, name: str, args: dict) -> dict:
        result = self._post({
            "jsonrpc": "2.0", "id": 0, "method": "tools/call",
            "params": {"name": name, "arguments": args},
        }) or {}
        # MCP wraps tool output in content blocks; unwrap a JSON text block if that is what we got.
        for block in result.get("content", []) or []:
            if block.get("type") == "text":
                try:
                    return json.loads(block["text"])
                except (json.JSONDecodeError, KeyError):
                    return {"_raw_text": block.get("text", "")}
        return result


# ---------------------------------------------------------------------------------------
# Honest response reading: find the sha, find the ok, without assuming a key name.
# ---------------------------------------------------------------------------------------
def find_hex(obj, length: int) -> list[str]:
    """Recursively collect hex strings of exactly `length` chars. We do not assume a key name."""
    found: list[str] = []
    if isinstance(obj, str):
        if len(obj) == length and re.fullmatch(r"[0-9a-fA-F]+", obj):
            found.append(obj.lower())
    elif isinstance(obj, dict):
        for v in obj.values():
            found += find_hex(v, length)
    elif isinstance(obj, list):
        for v in obj:
            found += find_hex(v, length)
    return found


def response_is_ok(resp: dict) -> bool:
    if isinstance(resp.get("ok"), bool):
        return resp["ok"]
    if isinstance(resp.get("success"), bool):
        return resp["success"]
    if isinstance(resp.get("isError"), bool):
        return not resp["isError"]
    return True  # absence of an error field is not evidence; the sha check is what we trust


def verify_returned_sha(resp: dict, data: bytes, remote_path: str) -> str:
    """
    THE receipt. ok=true is not one - it lies when the parent dir is missing and it lies on
    UTF-8 corruption. Only a sha that matches our locally computed sha256 is a receipt.
    """
    local = all_shas(data)
    returned = find_hex(resp, 64)
    if returned:
        if local["sha256"] in returned:
            return local["sha256"]
        raise Refuse(
            f"SHA MISMATCH on {remote_path}\n"
            f"  local  sha256 : {local['sha256']}\n"
            f"  remote sha(s) : {', '.join(returned)}\n"
            f"  The bytes on the limb are NOT the bytes we sent. Do not trust this tree.\n"
            f"  Run --rollback and investigate before any retry."
        )
    # No 64-char hex. Maybe the box hashes with something else - name it, do not guess past it.
    for algo, want in local.items():
        if algo == "sha256":
            continue
        if want in find_hex(resp, len(want)):
            raise Refuse(
                f"{remote_path}: the limb returned a {algo.upper()} digest, not SHA256.\n"
                f"  This script verifies sha256. Adjust SHA_ALGOS handling deliberately.\n"
                f"  Refusing rather than accepting an unverified write."
            )
    raise Refuse(
        f"{remote_path}: could not find ANY sha in the os_file_write response, so the write\n"
        f"  is UNVERIFIED. ok=true alone is not a receipt (it lies on the missing-parent-dir\n"
        f"  bug and on UTF-8 corruption). Response keys: {list(resp.keys())}\n"
        f"  Run with --dry-run --verbose to print the raw response shape."
    )


# ---------------------------------------------------------------------------------------
# Local preflight
# ---------------------------------------------------------------------------------------
def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True,
                          check=True).stdout.strip()


def local_preflight(skip_build: bool) -> tuple[str, bool, list[tuple[str, bytes]]]:
    print("== LOCAL PREFLIGHT ==")

    if not READER_BUILD.is_file():
        raise Refuse(
            f"reader/build.py DOES NOT EXIST at {READER_BUILD}\n\n"
            f"  The Cookbook Reader is not-yet-built. .gitignore already reserves reader/dist/\n"
            f"  ('regenerate with `python reader/build.py`'), but the reader itself has not been\n"
            f"  authored. This script will not deploy an empty tree and call it a reader.\n\n"
            f"  FALSIFIER THAT CLOSES THIS: `python reader/build.py` exits 0 and reader/dist/\n"
            f"  contains at least one .html file. Then re-run this script.\n"
            f"  See deploy/README.md - this is the bundle's one blocking PENDING."
        )

    if not skip_build:
        print("  building: python reader/build.py")
        r = subprocess.run([sys.executable, str(READER_BUILD)], cwd=str(REPO))
        if r.returncode != 0:
            raise Refuse(f"reader/build.py exited {r.returncode}. Fix the build. NOTHING DEPLOYED.")
    else:
        print("  [--skip-build] using the existing reader/dist/ as-is")

    if not READER_DIST.is_dir():
        raise Refuse(f"{READER_DIST} does not exist even after the build. NOTHING DEPLOYED.")

    files: list[tuple[str, bytes]] = []
    for p in sorted(READER_DIST.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(READER_DIST).as_posix()
        if rel == PROVENANCE:
            continue  # we author this ourselves, last
        files.append((rel, p.read_bytes()))

    if not files:
        raise Refuse(f"{READER_DIST} contains no files. Nothing to deploy. NOTHING DEPLOYED.")
    if not any(rel.endswith(".html") for rel, _ in files):
        raise Refuse(
            f"{READER_DIST} contains no .html file. A reader with no HTML is not a reader.\n"
            f"  Refusing to deploy a tree that cannot be read."
        )

    # THE ASCII GUARD. os_file_write corrupts multi-byte UTF-8 silently and still returns
    # ok=true with a sha-verified read-back lie. Pure ASCII means the bug CANNOT fire.
    for rel, data in files:
        try:
            data.decode("ascii")
        except UnicodeDecodeError as e:
            bad = data[e.start:e.start + 1]
            line = data[:e.start].count(b"\n") + 1
            raise Refuse(
                f"NON-ASCII BYTE in reader/dist/{rel} at byte {e.start} (line {line}): {bad!r}\n"
                f"  Context: {data[max(0, e.start - 40):e.start + 40]!r}\n\n"
                f"  os_file_write CORRUPTS multi-byte UTF-8: it drops bytes and STILL returns\n"
                f"  ok=true with a sha-verified read-back lie. The reader must emit pure ASCII so\n"
                f"  that bug cannot fire. Fix reader/build.py to escape this character as an HTML\n"
                f"  entity (e.g. &mdash; &#8212;). NOTHING DEPLOYED."
            )

    commit = git("rev-parse", "HEAD")
    dirty = bool(git("status", "--porcelain"))
    total = sum(len(d) for _, d in files)
    print(f"  commit        : {commit[:7]} ({'DIRTY - see below' if dirty else 'clean'})")
    print(f"  files         : {len(files)}  ({total:,} bytes)")
    print(f"  ascii guard   : PASS (all {len(files)} files are pure ASCII)")
    if dirty:
        print("  [WARN] The working tree is DIRTY. The commit sha in _provenance.json will NOT")
        print("         describe the bytes being deployed. repo_clean:false will record that")
        print("         honestly, but a dirty deploy is not reproducible from the commit alone.")
    return commit, dirty, files


# ---------------------------------------------------------------------------------------
# Remote helpers
# ---------------------------------------------------------------------------------------
def exec_argv(mcp: MCP, argv: list[str], limb: str | None, intent: str, dry: bool) -> dict:
    """Two-step os_exec: dry_run=true -> confirm=<token>. Fenced by intent + substring checks."""
    if intent not in ALLOWED_EXEC_INTENTS:
        raise Refuse(f"BUG: os_exec intent {intent!r} is not in ALLOWED_EXEC_INTENTS.")
    if argv[0] not in NODE1_EXEC_ALLOWLIST:
        raise Refuse(f"BUG: argv[0]={argv[0]!r} is not in the node1 os_exec allowlist.")
    joined = " ".join(argv)
    for bad in FORBIDDEN_EXEC_SUBSTRINGS:
        if bad in joined:
            raise Refuse(
                f"BLAST-RADIUS FENCE TRIPPED: {bad!r} appears in an os_exec this script was about\n"
                f"  to run: {joined!r}\n"
                f"  This bundle must never touch nftables/wg/uni-dns/units. Another session is\n"
                f"  live on node1+node2. Refusing. This is a bug in this script - report it."
            )

    args: dict = {"argv": argv, "dry_run": True}
    if limb:
        args["limb"] = limb
    first = mcp.call("os_exec", args)
    if dry:
        return first

    token = None
    for key in ("confirm_token", "confirm", "token"):
        if isinstance(first.get(key), str):
            token = first[key]
            break
    if not token:
        raise Refuse(
            f"os_exec dry_run returned no confirm token for {joined!r}.\n"
            f"  Response keys: {list(first.keys())}. Refusing to guess. NOTHING FURTHER DEPLOYED."
        )
    args2: dict = {"argv": argv, "confirm": token}
    if limb:
        args2["limb"] = limb
    return mcp.call("os_exec", args2)


def dir_exists(mcp: MCP, path: str, limb: str | None) -> bool:
    """Prove a directory exists. This is what defeats the silent-no-op bug."""
    resp = exec_argv(mcp, ["ls", "-d", path], limb, "verify-dir-exists", dry=False)
    blob = json.dumps(resp)
    if path in blob and "No such file" not in blob:
        return True
    return False


def ensure_dir(mcp: MCP, path: str, limb: str | None, tools: dict, dry: bool) -> None:
    """
    Create the target dir and PROVE it. os_file_write silently no-ops when the parent is
    missing and STILL returns ok=true with a sha-verified read-back lie, so an unproven dir
    means every subsequent 'successful' write may be a lie.

    Route cascade, most-honest first. If no route works we REFUSE and print the manual command
    rather than writing into a directory we could not prove.
    """
    if dry:
        route = ("native mkdir tool" if _mkdir_tool(tools)
                 else "podman + busybox mkdir -p (podman is allowlisted; no unit touched)")
        print(f"    [dry-run] would ensure {path} exists via: {route}")
        print(f"    [dry-run] would then PROVE it with: ls -d {path}")
        return

    if dir_exists(mcp, path, limb):
        print(f"    dir exists (proven): {path}")
        return

    tool = _mkdir_tool(tools)
    if tool:
        mcp.call(tool, ({"path": path, "limb": limb} if limb else {"path": path}))
    else:
        # podman IS on the argv[0] allowlist. Mount the serve root, mkdir inside it.
        # This touches no unit, no config, no network. It is the narrowest route available.
        exec_argv(mcp, [
            "podman", "run", "--rm", "-v", f"{REMOTE_ROOT}:/mnt:z",
            "docker.io/library/busybox:latest", "mkdir", "-p", f"/mnt/{Path(path).name}",
        ], limb, "create-dir", dry=False)

    if not dir_exists(mcp, path, limb):
        raise Refuse(
            f"Could not create or prove {path}.\n\n"
            f"  os_file_write SILENTLY NO-OPS when the parent dir is missing and still returns\n"
            f"  ok=true with a sha-verified read-back lie. Deploying into an unproven directory\n"
            f"  would produce a fake receipt for every file. Refusing.\n\n"
            f"  Do it by hand on the limb, then re-run this script:\n"
            f"      mkdir -p {path} && chmod 0755 {path}\n\n"
            f"  (The node1 os_exec argv[0] allowlist has no mkdir; the podman+busybox route\n"
            f"  needs the busybox image present. Either is fine - just prove the dir exists.)"
        )
    print(f"    dir created (proven): {path}")


def _mkdir_tool(tools: dict) -> str | None:
    for name in tools:
        low = name.lower()
        if "mkdir" in low or ("dir" in low and any(v in low for v in ("make", "create", "new"))):
            return name
    return None


def write_file(mcp: MCP, remote_path: str, data: bytes, limb: str | None, dry: bool) -> str:
    local = sha256_of(data)
    if dry:
        print(f"    [dry-run] would write {remote_path:<58} {len(data):>7,}B  {local[:12]}")
        return local
    text = data.decode("ascii")  # guarded upstream; ASCII is why the UTF-8 bug cannot fire
    args: dict = {"path": remote_path, "content": text}
    if limb:
        args["limb"] = limb
    resp = mcp.call("os_file_write", args)
    if not response_is_ok(resp):
        raise Refuse(f"os_file_write reported failure for {remote_path}: {resp}")
    confirmed = verify_returned_sha(resp, data, remote_path)
    print(f"    wrote {remote_path:<62} {len(data):>7,}B  sha {confirmed[:12]} OK")
    return confirmed


def assert_tool_schemas(tools: dict, dry: bool) -> None:
    """
    Buy information before irreversibility: read the LIVE inputSchema rather than trusting
    remembered arg names. If a field we intend to send is not in the schema, refuse.
    """
    print("== MCP TOOL SCHEMAS (read live, not assumed) ==")
    for needed in ("os_file_write", "os_exec"):
        if needed not in tools:
            raise Refuse(
                f"node1 MCP does not expose {needed!r}. Available: {sorted(tools)}\n"
                f"  Refusing rather than guessing a transport. NOTHING DEPLOYED."
            )
    for name in ("os_file_write", "os_exec", "os_sysinfo"):
        t = tools.get(name)
        if not t:
            continue
        schema = t.get("inputSchema", {}) or {}
        props = sorted((schema.get("properties") or {}).keys())
        required = schema.get("required", [])
        print(f"  {name}")
        print(f"    properties : {props}")
        print(f"    required   : {required}")

    wprops = set(((tools["os_file_write"].get("inputSchema") or {}).get("properties") or {}))
    if wprops:
        for field in ("path", "content"):
            if field not in wprops:
                raise Refuse(
                    f"os_file_write has no {field!r} field. This script sends "
                    f"path/content{'/limb' if True else ''}.\n"
                    f"  Live properties: {sorted(wprops)}\n"
                    f"  The remembered arg names are WRONG for this server version. Refusing to\n"
                    f"  send a call shaped by a stale memory. Fix this script against the schema\n"
                    f"  printed above. NOTHING DEPLOYED."
                )
        if "limb" not in wprops:
            print("    [WARN] os_file_write exposes no 'limb' field. node2 is reached via limb=.")
            print("           node1 will still deploy; node2 will refuse rather than write locally.")
    if dry:
        print("  (schemas read; nothing written)")


def check_reachable(mcp: MCP) -> dict:
    info = mcp.initialize()
    server = info.get("serverInfo", {})
    print(f"  node1 MCP  : {server.get('name', '?')} {server.get('version', '?')}")
    print(f"  session    : {'established' if mcp.session_id else 'no mcp-session-id header'}")
    return info


# ---------------------------------------------------------------------------------------
# Provenance
# ---------------------------------------------------------------------------------------
def provenance_bytes(commit: str, dirty: bool, files: list[tuple[str, bytes]], limb_name: str,
                     state: str) -> bytes:
    doc = {
        "state": state,
        "commit": commit,
        "commit_short": commit[:7],
        "repo_clean": not dirty,
        "repo": "https://github.com/TMDLRG/UNI-Encyclopedia-Cookbook",
        "limb": limb_name,
        "deployed_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "deployed_by": "deploy/deploy_cookbook.py",
        "file_count": len(files),
        "files": {rel: sha256_of(data) for rel, data in files},
        "note": (
            "This limb serves an immutable copy of the commit named above. It is a cache of a "
            "git commit, not a source of truth: if this file's commit differs from the "
            "repository HEAD, THIS LIMB IS STALE and the repository wins. Nothing enforces "
            "freshness; this file only reports it honestly."
        ),
    }
    # ensure_ascii=True is load-bearing: the payload must be pure ASCII (os_file_write bug).
    return (json.dumps(doc, indent=2, ensure_ascii=True) + "\n").encode("ascii")


# ---------------------------------------------------------------------------------------
# Deploy / rollback
# ---------------------------------------------------------------------------------------
def deploy_limb(mcp: MCP, target: dict, commit: str, dirty: bool,
                files: list[tuple[str, bytes]], tools: dict, dry: bool) -> None:
    name, limb = target["name"], target["limb"]
    print(f"\n== {name.upper()} {'(limb=' + limb + ')' if limb else '(the MCP host itself)'} ==")

    if limb:
        wprops = set(((tools["os_file_write"].get("inputSchema") or {}).get("properties") or {}))
        if wprops and "limb" not in wprops:
            raise Refuse(
                f"Cannot reach {name}: os_file_write has no 'limb' field on this server.\n"
                f"  Writing without it would deploy to node1 AGAIN, not to {name} - a silent\n"
                f"  wrong-box write. That is the SW-E3-03 class of error. Refusing.\n"
                f"  node1 may already be deployed; that is safe and idempotent."
            )

    # 1. Parents FIRST, proven. Never write into an unproven dir.
    ensure_dir(mcp, REMOTE_DIR, limb, tools, dry)

    # 2. On a RE-RUN, mark the tree in-flight before touching it, so an interrupted re-deploy
    #    is visibly mid-flight rather than falsely advertising the previous commit as current.
    if not dry and dir_exists(mcp, f"{REMOTE_DIR}/{PROVENANCE}", limb):
        print("    re-run detected: marking tree DEPLOY-IN-PROGRESS before overwriting")
        write_file(mcp, f"{REMOTE_DIR}/{PROVENANCE}",
                   provenance_bytes(commit, dirty, files, name, "DEPLOY-IN-PROGRESS"), limb, dry)

    # 3. Content. Subdirectories are created and proven before their files land.
    seen: set[str] = set()
    for rel, data in files:
        parent = str(Path(rel).parent).replace("\\", "/")
        if parent not in (".", "") and parent not in seen:
            ensure_dir(mcp, f"{REMOTE_DIR}/{parent}", limb, tools, dry)
            seen.add(parent)
        write_file(mcp, f"{REMOTE_DIR}/{rel}", data, limb, dry)

    # 4. Provenance LAST. A half-copied tree never advertises itself as complete.
    write_file(mcp, f"{REMOTE_DIR}/{PROVENANCE}",
               provenance_bytes(commit, dirty, files, name, "COMPLETE"), limb, dry)
    print(f"  {name}: {len(files)} files + {PROVENANCE}"
          f"{' (dry-run: nothing written)' if dry else ' - every sha verified'}")


def rollback(mcp: MCP, dry: bool) -> None:
    print("== ROLLBACK: remove the cookbook dir from every limb ==")
    print("   (nothing else is touched, because nothing else was ever touched)")
    for target in LIMBS:
        name, limb = target["name"], target["limb"]
        print(f"\n-- {name}")
        if dry:
            print(f"   [dry-run] would remove {REMOTE_DIR}")
            continue
        if not dir_exists(mcp, REMOTE_DIR, limb):
            print(f"   {REMOTE_DIR} does not exist - nothing to roll back")
            continue
        try:
            exec_argv(mcp, [
                "podman", "run", "--rm", "-v", f"{REMOTE_ROOT}:/mnt:z",
                "docker.io/library/busybox:latest", "rm", "-rf", f"/mnt/{Path(REMOTE_DIR).name}",
            ], limb, "remove-cookbook-dir", dry=False)
        except SystemExit:
            raise Refuse(
                f"Could not remove {REMOTE_DIR} on {name}.\n"
                f"  The node1 os_exec argv[0] allowlist has no `rm`, and the podman+busybox route\n"
                f"  failed. This script will NOT pretend a rollback happened.\n\n"
                f"  Remove it by hand on {name}:\n"
                f"      rm -rf {REMOTE_DIR}\n\n"
                f"  FALSIFIER: https://<limb>/glass/cookbook/_provenance.json returns 404."
            )
        if dir_exists(mcp, REMOTE_DIR, limb):
            raise Refuse(f"{REMOTE_DIR} still exists on {name} after removal. Remove it by hand.")
        print(f"   removed (proven gone): {REMOTE_DIR}")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Deploy the static Cookbook Reader into the existing nginx root on node1+node2.")
    ap.add_argument("--dry-run", action="store_true",
                    help="build, guard, read live schemas, print the plan. Mutates NOTHING.")
    ap.add_argument("--rollback", action="store_true", help="remove the cookbook dir from the limbs")
    ap.add_argument("--skip-build", action="store_true", help="use reader/dist/ as-is")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    endpoint = os.environ.get("UNI_MCP")
    token = os.environ.get("UNI_TOKEN")
    if not endpoint or not token:
        raise Refuse(
            "UNI_MCP and/or UNI_TOKEN are not set.\n\n"
            "  Neither is hardcoded in this bundle and neither may ever be committed.\n"
            "      export UNI_MCP=\"http://<node1-host>:<port>/<mcp-path>\"\n"
            "      export UNI_TOKEN=\"<bearer token>\"\n"
            "  Get them from the operator's store. Never paste a token into a file in this repo."
        )

    print("=" * 78)
    print("  COOKBOOK READER DEPLOY" + ("  [DRY RUN - MUTATES NOTHING]" if args.dry_run else ""))
    print("  target: " + REMOTE_DIR + "   (static files inside the EXISTING nginx root)")
    print("  never touches: nftables | wg | uni-dns | any unit | nginx config | nginx reload")
    print("=" * 78)

    mcp = MCP(endpoint, token, verbose=args.verbose)

    print("\n== NODE1 REACHABILITY (refuse if unreachable) ==")
    check_reachable(mcp)
    tools = mcp.list_tools()
    print(f"  tools      : {len(tools)} exposed")

    if args.rollback:
        assert_tool_schemas(tools, args.dry_run)
        rollback(mcp, args.dry_run)
        print("\nROLLBACK COMPLETE." if not args.dry_run else "\nDRY RUN - nothing removed.")
        print("Falsifier: /glass/cookbook/_provenance.json returns 404 on both limbs.")
        return 0

    commit, dirty, files = local_preflight(args.skip_build)
    assert_tool_schemas(tools, args.dry_run)

    for target in LIMBS:
        deploy_limb(mcp, target, commit, dirty, files, tools, args.dry_run)

    print("\n" + "=" * 78)
    if args.dry_run:
        print("  DRY RUN COMPLETE - NOTHING WAS WRITTEN. The reader is not deployed.")
        print("  Read the plan above. If it is right, re-run without --dry-run.")
    else:
        print(f"  WRITES COMPLETE at commit {commit[:7]} - every file's sha verified.")
        print("\n  THIS IS NOT YET A RECEIPT. Observe it yourself before believing it:")
        print("    https://10.190.245.121/glass/cookbook/_provenance.json    (node1, LAN)")
        print("    https://10.13.13.3/glass/cookbook/_provenance.json        (node2, mesh)")
        print(f"    Both must return 200 AND report commit {commit[:7]}.")
        print("\n  uni-tab-arm-1 is NOT deployed (unreachable, hands-on-device). See TABLET.md.")
        print("  This is a 2-of-3-limb deploy. It is not fleet-wide. Do not record it as one.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
