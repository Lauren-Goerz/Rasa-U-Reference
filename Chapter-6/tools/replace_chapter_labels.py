#!/usr/bin/env python3
"""Replace Chapter 1.x display labels with Level x across text files (repo root)."""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SELF_REL = Path("tools/replace_chapter_labels.py")

SKIP_DIRS = {
    ".git",
    ".cursor",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    ".mypy_cache",
    ".pytest_cache",
    ".rasa",
}

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
}

# Longest chapter numbers first (1.6 before 1.1).
UPPER = [
    ("Chapter 1.6", "Level 6"),
    ("Chapter 1.5", "Level 5"),
    ("Chapter 1.4", "Level 4"),
    ("Chapter 1.3", "Level 3"),
    ("Chapter 1.2", "Level 2"),
    ("Chapter 1.1", "Level 1"),
]

LOWER = [
    ("chapter 1.6", "level 6"),
    ("chapter 1.5", "level 5"),
    ("chapter 1.4", "level 4"),
    ("chapter 1.3", "level 3"),
    ("chapter 1.2", "level 2"),
    ("chapter 1.1", "level 1"),
]

# Ranges and shorthand — longest matches first (avoid partial chops).
EXTRA = [
    ("Chapters 1.4–1.5", "Levels 4–5"),
    ("Chapters 1.4-1.5", "Levels 4-5"),
    ("Chapters 1.1–1.6", "Levels 1–6"),
    ("Chapters 1.1-1.6", "Levels 1-6"),
    ("Chapters 1.1–1.5", "Levels 1–5"),
    ("Chapters 1.1-1.5", "Levels 1-5"),
    ("Chapters 1.1–1.3", "Levels 1–3"),
    ("Chapters 1.1-1.3", "Levels 1-3"),
    ("chapters 1.2–1.4", "levels 2–4"),
    ("chapters 1.2-1.4", "levels 2-4"),
    ("Chapters 1.2, 1.3, and 1.4", "Levels 2, 3, and 4"),
    ("chapters 1.2, 1.3, and 1.4", "levels 2, 3, and 4"),
    ("Chapters 1.3 and 1.4", "Levels 3 and 4"),
    ("chapters 1.3 and 1.4", "levels 3 and 4"),
    ("Ch 1.3 end → Ch 1.4 end", "Level 3 end → Level 4 end"),
    ("Ch 1.3 end -> Ch 1.4 end", "Level 3 end -> Level 4 end"),
    ("Ch 1.3 → Ch 1.4", "Level 3 → Level 4"),
    ("Ch 1.3 -> Ch 1.4", "Level 3 -> Level 4"),
    ("authoritative Ch 1.3 end", "authoritative Level 3 end"),
    ("Ch 1.3 end", "Level 3 end"),
    ("Ch 1.4 end", "Level 4 end"),
    ("Ch 1.2", "Level 2"),
    ("Ch 1.3", "Level 3"),
    ("Ch 1.4", "Level 4"),
    ("Ch 1.5", "Level 5"),
    ("Ch 1.6", "Level 6"),
    ("Ch 1.1", "Level 1"),
]


def process_file(path: Path) -> bool:
    try:
        raw = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return False

    original = raw
    for old, new in UPPER:
        raw = raw.replace(old, new)
    for old, new in LOWER:
        raw = raw.replace(old, new)
    for old, new in EXTRA:
        raw = raw.replace(old, new)

    raw = re.sub(r"Level (\d) \(Level \1 ([^)]+)\)", r"Level \1 \2", raw)
    for n in range(1, 7):
        raw = re.sub(rf"Level {n} \(Level {n}\)", f"Level {n}", raw)

    raw = re.sub(
        r"Levels 1[–-]6 \(Levels 1[–-]6\)",
        "Levels 1–6",
        raw,
    )

    if raw != original:
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
        if rel.as_posix() == SELF_REL.as_posix():
            continue
        if any(p in SKIP_DIRS for p in rel.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if process_file(path):
            changed.append(path)

    print(f"Updated {len(changed)} files")
    for p in sorted(changed)[:80]:
        print(" ", p.relative_to(REPO))
    if len(changed) > 80:
        print(f" ... and {len(changed) - 80} more")


if __name__ == "__main__":
    main()
