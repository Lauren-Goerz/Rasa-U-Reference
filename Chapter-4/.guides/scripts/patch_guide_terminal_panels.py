#!/usr/bin/env python3
"""
Set guide page JSON so pages that expect terminal use open with #terminal on panel 1 (right),
with layout 2-panels-tree-guides-left (guide left, tree/terminal right).

Run from repo root: python .guides/scripts/patch_guide_terminal_panels.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CONTENT_ROOT = Path(__file__).resolve().parents[1] / "content"

# Markdown content suggests students need a terminal (case-insensitive search).
TERMINAL_MD_PATTERNS = [
    re.compile(r"\brasa\s+(train|inspect|run|shell|data)\b", re.I),
    re.compile(r"python\s+-m\s+rasa\b", re.I),
    re.compile(r"source\s+[^\n]*\.venv|\.venv/bin/activate", re.I),
    re.compile(r"Scripts\\\\activate|Scripts/activate", re.I),
    re.compile(r"\*\*Terminal\*\*", re.I),
    re.compile(r"(^|\n)\s*1\.\s+\*\*Terminal\.\*\*", re.I),
    re.compile(r"Open (your |the )?terminal", re.I),
    re.compile(r"in the terminal", re.I),
    re.compile(r"From the terminal", re.I),
    re.compile(r"code-output-compare-", re.I),  # Code Test assessments
    re.compile(r"`cd\s+level\d`", re.I),
    re.compile(r"mkdir\s+-p\s+logs", re.I),
    re.compile(r"rasa\s+pro\s+install", re.I),
    re.compile(r"pip\s+install", re.I),
    re.compile(r"python\s+-m\s+venv\b", re.I),
]


def md_expects_terminal(text: str) -> bool:
    if not text:
        return False
    return any(p.search(text) for p in TERMINAL_MD_PATTERNS)


def build_terminal_files(old_files: list | None) -> list[dict]:
    """Preserve auto-run command if present; otherwise standard #terminal open."""
    if not old_files:
        return [{"path": "#terminal", "panel": 1, "action": "open"}]
    for f in old_files:
        if not isinstance(f, dict):
            continue
        path = f.get("path", "")
        if path == "#terminal":
            out = {"path": "#terminal", "panel": 1, "action": f.get("action") or "open"}
            if "command" in f:
                out["command"] = f["command"]
            return [out]
        # Rare: command without #terminal path (minified broken JSON)
        if f.get("command") and path != "#terminal":
            out = {"path": "#terminal", "panel": 1, "action": "open", "command": f["command"]}
            return [out]
    return [{"path": "#terminal", "panel": 1, "action": "open"}]


def patch_page_json(path: Path, dry_run: bool) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("type") != "page":
        return False

    md_path = path.with_suffix(".md")
    if not md_path.is_file():
        return False

    md_text = md_path.read_text(encoding="utf-8")
    if not md_expects_terminal(md_text):
        return False

    old_files = data.get("files")
    new_files = build_terminal_files(old_files if isinstance(old_files, list) else None)

    changed = False
    if data.get("files") != new_files:
        data["files"] = new_files
        changed = True
    if data.get("layout") != "2-panels-tree-guides-left":
        data["layout"] = "2-panels-tree-guides-left"
        changed = True

    if changed and not dry_run:
        path.write_text(json.dumps(data, indent="\t", ensure_ascii=False) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    updated: list[str] = []
    for json_path in sorted(CONTENT_ROOT.rglob("*.json")):
        if json_path.name == "index.json":
            continue
        try:
            if patch_page_json(json_path, dry_run=args.dry_run):
                updated.append(str(json_path.relative_to(CONTENT_ROOT.parent)))
        except (json.JSONDecodeError, OSError) as e:
            print("SKIP", json_path, e)

    print(f"{'Would update' if args.dry_run else 'Updated'} {len(updated)} page JSON(s)")
    for u in updated:
        print(" ", u)


if __name__ == "__main__":
    main()
