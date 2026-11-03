#!/usr/bin/env python3
"""Replace Codio guide folder ids Chapter-1-N---* with Level-N---* across the repo."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SELF = Path("tools/replace_guide_folder_paths.py")

SKIP_DIRS = {".git", ".cursor", "__pycache__", ".venv", "venv", "node_modules"}

# Full folder names only (longest numeric segment first avoids accidents).
REPLACEMENTS: list[tuple[str, str]] = [
    ("Chapter-1-6---Sub-Agents-c7d8", "Level-6---Sub-Agents-c7d8"),
    ("Chapter-1-5---Tool-Calling-f9e0", "Level-5---Tool-Calling-f9e0"),
    ("Chapter-1-4---Multiple-Slots-e5f6", "Level-4---Multiple-Slots-e5f6"),
    ("Chapter-1-3---Slot-Collection-a4b5", "Level-3---Slot-Collection-a4b5"),
    ("Chapter-1-2---Custom-Actions-30d6", "Level-2---Custom-Actions-30d6"),
    ("Chapter-1-1---Just-Responses-d3b4", "Level-1---Just-Responses-d3b4"),
]

TEXT_SUFFIXES = {
    ".md",
    ".json",
    ".yml",
    ".yaml",
    ".py",
    ".txt",
    ".ps1",
    ".sh",
    ".workspace",
    ".toml",
    ".rst",
    ".html",
    ".css",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".svg",
    ".code-workspace",
}


def process_file(path: Path) -> bool:
    try:
        raw = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return False
    orig = raw
    for old, new in REPLACEMENTS:
        raw = raw.replace(old, new)
    if raw != orig:
        path.write_text(raw, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed: list[Path] = []
    for path in REPO.rglob("*"):
        if not path.is_file():
            continue
        try:
            rel = path.relative_to(REPO)
        except ValueError:
            continue
        if rel.as_posix() == SELF.as_posix():
            continue
        if any(p in SKIP_DIRS for p in rel.parts):
            continue
        suf = path.suffix.lower()
        if suf not in TEXT_SUFFIXES and not path.name.endswith(".code-workspace"):
            continue
        if process_file(path):
            changed.append(rel)
    print(f"Updated {len(changed)} files")
    for r in sorted(changed)[:100]:
        print(" ", r)
    if len(changed) > 100:
        print(f" ... and {len(changed) - 100} more")


if __name__ == "__main__":
    main()
