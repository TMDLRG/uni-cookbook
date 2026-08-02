#!/usr/bin/env python3
"""
build_gpt_pack.py — assemble the UNI Encyclopedia + Cookbook into an OpenAI Custom GPT pack.

The repo is the single source of truth. This script is a pure, reproducible BUILD:
it never authors content, it only merges, headers, validates, and zips.

Output:
    gpt/knowledge/K01..K19  (.md)   — merged from the repo corpus
    gpt/knowledge/K20       (.json) — authored by the corpus workflow, validated here
    gpt/MANIFEST.json               — the human's upload checklist + full provenance
    dist/UNI-Encyclopedia-Cookbook-GPT-Pack.zip

Hard limits enforced (OpenAI Custom GPT builder UI, confirmed 2026-07-15 against
help.openai.com "Creating and editing GPTs" / "File uploads FAQ"):
    - 20 knowledge files maximum per GPT      -> len(PACK) must be exactly 20
    - 512 MB per file, 2M tokens per text file -> warn well before
    - 8,000 characters in the Instructions field -> hard gate

Run:  python tools/build_gpt_pack.py
"""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
KNOWLEDGE = REPO / "gpt" / "knowledge"
CONFIG = REPO / "gpt" / "gpt-config"
DIST = REPO / "dist"

MAX_KNOWLEDGE_FILES = 20
INSTRUCTIONS_CHAR_LIMIT = 8000
TOKEN_WARN_CHARS = 6_000_000  # ~1.5M tokens at ~4 chars/token: warn before the 2M cap

SOVEREIGNTY_NOTE = (
    "SOVEREIGNTY RULE (binding, do not merge the two ledgers): this corpus carries TWO "
    "sovereign evidence vocabularies. The UNI 4-value fence (proven / designed / hypothesized "
    "/ not-yet-built) describes ONLY UNI's own build status and is governed by "
    "encyclopedia/CLAIM-LEDGER.md. The NATURA 12-value class, in three groups, describes ONLY "
    "nature's observed regularities and is governed by encyclopedia/NATURE-LEDGER.md: "
    "group A / measured = OBSERVED-REPLICATED, OBSERVED-SINGLE, OBSERVED-CONTESTED; "
    "group B / derived = MODELED, MODELED-CONTESTED, HYPOTHESIZED; "
    "group C / fenced = INADMISSIBLE, SUPERSEDED, NOT-MEASURED, NOT-SOURCED, NOT-CONFIRMED, "
    "NOT-LOCATED. "
    "Six of the twelve were registered by NA-00 amendment 2026-07-15-A after the corpus refuted "
    "the original 'six classes and only six' at 72 of 919 ledger rows; twelve is a MEASURED "
    "property of the corpus, not a design target. "
    "NEVER read NOT-SOURCED as NOT-MEASURED: the first says we could not trace the source (a fact "
    "about us), the second says nobody has measured it (a claim about the frontier of science). "
    "A nature citation is NEVER a UNI gate. Cross-reference between them by explicit link only, "
    "never by merge."
)


def g(pattern: str) -> list[str]:
    """Glob the repo, sorted, repo-relative POSIX paths. Errors if a pattern matches nothing."""
    hits = sorted(p.relative_to(REPO).as_posix() for p in REPO.glob(pattern) if p.is_file())
    if not hits:
        raise SystemExit(f"FATAL: pattern matched no files: {pattern!r}")
    return hits


# --- the pack: exactly 20 slots. (slot, title, [repo-relative source files]) ----------
def build_pack_spec() -> list[tuple[str, str, list[str]]]:
    return [
        ("K01-START-HERE-how-to-use-this-corpus.md",
         "START HERE — the map of this corpus and its two sovereign vocabularies",
         ["encyclopedia/wing-NATURA/00-INDEX.md",
          "encyclopedia/wing-NATURA/NA-00-how-to-read-this-wing.md"]),

        ("K02-NATURE-as-the-authority.md",
         "Nature as the authority — and the discipline that keeps it honest",
         ["encyclopedia/wing-NATURA/NA-01-nature-as-the-authority.md"]),

        ("K03-METHOD-the-one-loop-active-inference.md",
         "The one loop — active inference (VFE to understand, EFE to choose)",
         ["encyclopedia/wing-NATURA/NA-02-the-one-loop.md"]),

        ("K04-METHOD-how-to-make-new-science.md",
         "How to research, observe, and make new science with falsifiable evidence",
         ["encyclopedia/wing-NATURA/NA-03-how-to-make-new-science.md"]),

        ("K05-MIND-BODY-WORLD.md",
         "MIND / BODY / MIND.BODY / WORLD — the Markov blanket, nested across scales",
         ["encyclopedia/wing-NATURA/NA-04-mind-body-world.md"]),

        ("K06-RATIOS-scaling-laws.md",
         "The ratios — allometry and scaling laws across 20+ orders of magnitude",
         ["encyclopedia/wing-NATURA/NA-05-ratios-and-scaling-laws.md"]),

        ("K07-FREQUENCIES-rhythm-and-resonance.md",
         "The frequencies — rhythm, resonance, and the honest fence around them",
         ["encyclopedia/wing-NATURA/NA-06-frequencies-rhythm-and-resonance.md"]),

        ("K08-DIMENSIONLESS-numbers.md",
         "The dimensionless numbers — the cross-scale design toolkit",
         ["encyclopedia/wing-NATURA/NA-07-dimensionless-numbers.md"]),

        ("K09-CELL-level-design.md",
         "Design down to the cell level — the cell as an engineered system",
         ["encyclopedia/wing-NATURA/NA-08-cell-level-design.md"]),

        ("K10-MORPHOGENESIS-and-development.md",
         "Morphogenesis — how a pattern comes from no pattern",
         ["encyclopedia/wing-NATURA/NA-09-morphogenesis-and-development.md"]),

        ("K11-SCALE-LADDER-and-gradients.md",
         "The scale ladder — quark to galaxy, and the gradients between",
         ["encyclopedia/wing-NATURA/NA-10-the-scale-ladder-and-gradients.md"]),

        ("K12-RECIPES-substrate-rocks-water-air-stars.md",
         "Build the substrate — rocks, water, air, stars",
         ["cookbook/recipes-natura/CN-01-rocks.md",
          "cookbook/recipes-natura/CN-02-water.md",
          "cookbook/recipes-natura/CN-03-air.md",
          "cookbook/recipes-natura/CN-04-stars.md"]),

        ("K13-RECIPES-life-dna-and-sperm.md",
         "Build life's information layer — DNA and the delivery vehicle",
         ["cookbook/recipes-natura/CN-05-dna.md",
          "cookbook/recipes-natura/CN-06-sperm.md"]),

        ("K14-RECIPES-ants-the-collective.md",
         "Build the collective — ants, stigmergy, and the colony blanket",
         ["cookbook/recipes-natura/CN-07-ants.md"]),

        ("K15-RECIPES-dinosaurs-whales-bats.md",
         "Build the animals — scaling limits, low-frequency sound, and measurable active inference",
         ["cookbook/recipes-natura/CN-08-dinosaurs.md",
          "cookbook/recipes-natura/CN-09-whales.md",
          "cookbook/recipes-natura/CN-10-bats.md"]),

        ("K16-RECIPES-humans-and-the-open-question.md",
         "Build the human — and the permanent open question beyond it",
         ["cookbook/recipes-natura/CN-11-humans.md",
          "cookbook/recipes-natura/CN-12-beyond-human-open-question.md"]),

        ("K17-UNI-method-and-governance.md",
         "The UNI program — its method constitution, evidence discipline, and honest posture",
         ["cookbook/00-INDEX.md",
          "cookbook/00-front-matter.md",
          "cookbook/01-kitchen-rules.md",
          "cookbook/02-the-pantry.md",
          "cookbook/99-closing.md",
          "cookbook/UNI-GPT-CONSULT-PACKAGE.md",
          "cookbook/UNI-GPT-CONSULT-2026-06-27.md",
          "encyclopedia/00-INDEX.md"]
         + g("encyclopedia/wing-E/*.md")
         + g("encyclopedia/wing-mu/*.md")
         + g("encyclopedia/wing-N/*.md")
         + g("encyclopedia/wing-M/*.md")),

        ("K18-UNI-claim-ledger-and-master-plans.md",
         "The UNI claim ledger (single source of truth) and the authoring master plans",
         ["encyclopedia/CLAIM-LEDGER.md",
          "encyclopedia/MASTER-PLAN.md",
          "cookbook/MASTER-PLAN.md"]),

        ("K19-UNI-science-ladder-and-recipes.md",
         "The UNI L0-L12 developmental ladder, its recipes, the continuity substrate, and Track-A",
         g("encyclopedia/wing-S/*.md")
         + g("cookbook/recipes/*.md")
         + ["cookbook/continuity-substrate.md"]
         + g("encyclopedia/appendix-TA/*.md")),

        # K20 is authored by the corpus workflow (extraction from the chapters), not merged here.
        ("K20-constants-ratios-and-nature-ledger.json",
         "Machine-readable: every constant, ratio, frequency, dimensionless number, and the "
         "nature ledger with its INADMISSIBLE register",
         []),
    ]


def merge_slot(slot: str, title: str, sources: list[str]) -> str:
    """Concatenate sources under one honest header that names every file merged."""
    out: list[str] = []
    out.append(f"# {title}\n")
    out.append(
        f"> **Knowledge file `{slot}`** of the UNI Encyclopedia & Cookbook GPT pack.\n"
        f"> This file is a BUILD ARTIFACT: it merges **{len(sources)}** source file(s) from the\n"
        f"> repository `TMDLRG/UNI-Encyclopedia-Cookbook`, byte-for-byte, in the order listed below.\n"
        f"> The repository is the single source of truth; if this file and the repository ever\n"
        f"> disagree, the repository wins and this file is stale.\n>\n"
        f"> {SOVEREIGNTY_NOTE}\n"
    )
    out.append("\n**Source files merged into this knowledge file, in order:**\n")
    for s in sources:
        out.append(f"- `{s}`")
    out.append("\n---\n")
    for s in sources:
        p = REPO / s
        if not p.is_file():
            raise SystemExit(f"FATAL: source file missing (corpus incomplete?): {s}")
        body = p.read_text(encoding="utf-8")
        out.append(f"\n\n<!-- ===== BEGIN {s} ===== -->\n")
        out.append(body.rstrip("\n"))
        out.append(f"\n\n<!-- ===== END {s} ===== -->\n")
    return "\n".join(out) + "\n"


def main() -> int:
    pack = build_pack_spec()

    # ---- gate 1: exactly 20 knowledge files (the OpenAI hard cap)
    if len(pack) != MAX_KNOWLEDGE_FILES:
        raise SystemExit(
            f"FATAL: pack has {len(pack)} slots; the Custom GPT UI accepts exactly "
            f"{MAX_KNOWLEDGE_FILES} knowledge files maximum."
        )

    KNOWLEDGE.mkdir(parents=True, exist_ok=True)
    DIST.mkdir(parents=True, exist_ok=True)

    manifest_files = []
    total_chars = 0

    for slot, title, sources in pack:
        target = KNOWLEDGE / slot

        if slot.endswith(".json"):
            # Authored by the workflow (extraction). We validate, we do not write.
            if not target.is_file():
                raise SystemExit(f"FATAL: {slot} was not authored by the corpus workflow.")
            raw = target.read_text(encoding="utf-8")
            try:
                data = json.loads(raw)
            except json.JSONDecodeError as e:
                raise SystemExit(f"FATAL: {slot} is not valid JSON: {e}")
            n = len(raw)
            counts = {k: len(v) for k, v in data.items() if isinstance(v, list)}
            print(f"  [ok] {slot:<52} {n:>9,} chars  (validated JSON: {counts})")
        else:
            text = merge_slot(slot, title, sources)
            target.write_text(text, encoding="utf-8")
            n = len(text)
            if n > TOKEN_WARN_CHARS:
                print(f"  [WARN] {slot} is {n:,} chars — approaching the 2M-token per-file cap.")
            print(f"  [ok] {slot:<52} {n:>9,} chars  ({len(sources)} source file(s))")

        total_chars += n
        manifest_files.append(
            {
                "slot": slot,
                "title": title,
                "chars": n,
                "upload_to": "Knowledge",
                "merged_from": sources if sources else ["(authored by the corpus workflow)"],
            }
        )

    # ---- gate 2: the Instructions field must fit the 8,000-character box
    instr_path = CONFIG / "INSTRUCTIONS.md"
    if not instr_path.is_file():
        raise SystemExit(f"FATAL: {instr_path} missing — the Instructions field has no content.")
    instr = instr_path.read_text(encoding="utf-8")
    instr_chars = len(instr)
    if instr_chars > INSTRUCTIONS_CHAR_LIMIT:
        raise SystemExit(
            f"FATAL: INSTRUCTIONS.md is {instr_chars:,} chars — over the "
            f"{INSTRUCTIONS_CHAR_LIMIT:,}-char Custom GPT Instructions limit. Cut it."
        )
    print(f"\n  [ok] INSTRUCTIONS.md {instr_chars:,} / {INSTRUCTIONS_CHAR_LIMIT:,} chars "
          f"({INSTRUCTIONS_CHAR_LIMIT - instr_chars:,} to spare)")

    config_path = CONFIG / "CONFIG.json"
    if not config_path.is_file():
        raise SystemExit(f"FATAL: {config_path} missing.")
    json.loads(config_path.read_text(encoding="utf-8"))  # validate

    # ---- the manifest: the human's checklist + honest provenance
    manifest = {
        "pack": "UNI Encyclopedia & Cookbook — OpenAI Custom GPT pack",
        "repo": "https://github.com/TMDLRG/UNI-Encyclopedia-Cookbook",
        "built_by": "tools/build_gpt_pack.py (reproducible build; the repo is the source of truth)",
        "target": "OpenAI Custom GPT builder — chat UI (chatgpt.com), NOT the Assistants API",
        "limits_observed": {
            "max_knowledge_files": MAX_KNOWLEDGE_FILES,
            "knowledge_files_in_pack": len(pack),
            "instructions_char_limit": INSTRUCTIONS_CHAR_LIMIT,
            "instructions_chars_used": instr_chars,
            "max_file_size": "512 MB per file",
            "per_file_token_cap": "2M tokens per text/document file",
            "source": "help.openai.com — 'Creating and editing GPTs' / 'File uploads FAQ', "
                      "confirmed 2026-07-15",
        },
        "upload_steps": [
            "1. chatgpt.com -> Explore GPTs -> your GPT -> Edit -> Configure tab.",
            "2. Name: paste gpt-config/CONFIG.json .name",
            "3. Description: paste gpt-config/CONFIG.json .description",
            "4. Instructions: paste the ENTIRE contents of gpt-config/INSTRUCTIONS.md",
            "5. Conversation starters: paste each string from CONFIG.json .conversation_starters",
            "6. Knowledge: upload ALL 20 files from knowledge/ (drag the folder contents in).",
            "7. Capabilities: set per CONFIG.json .capabilities",
            "8. Save / Update.",
        ],
        "sovereignty_rule": SOVEREIGNTY_NOTE,
        "total_knowledge_chars": total_chars,
        "files": manifest_files,
    }
    (REPO / "gpt" / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # ---- the zip
    zip_path = DIST / "UNI-Encyclopedia-Cookbook-GPT-Pack.zip"
    root = "UNI-Encyclopedia-Cookbook-GPT-Pack"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.write(REPO / "gpt" / "README-START-HERE.md", f"{root}/README-START-HERE.md")
        z.write(REPO / "gpt" / "MANIFEST.json", f"{root}/MANIFEST.json")
        z.write(instr_path, f"{root}/gpt-config/INSTRUCTIONS.md")
        z.write(config_path, f"{root}/gpt-config/CONFIG.json")
        for slot, _, _ in pack:
            z.write(KNOWLEDGE / slot, f"{root}/knowledge/{slot}")

    size = zip_path.stat().st_size
    print(f"\n  [ok] {zip_path}")
    print(f"       {size:,} bytes  |  {len(pack)} knowledge files  |  "
          f"{total_chars:,} chars of corpus")
    print("\nBUILD CLEAN — all gates passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
