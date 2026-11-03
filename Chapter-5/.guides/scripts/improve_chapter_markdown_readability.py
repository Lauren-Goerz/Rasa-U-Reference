#!/usr/bin/env python3
"""
Readability pass for .guides/content/Chapter-*/*.md (prose only; skips ``` fences):
- Spaced em dash ( — ) -> comma + space (common plain-English alternative)
- §2 -> section 2 (avoid § in UI)
Skips CODIO_*SYNC.md and *GAPS*.md
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "content"


def split_fences(text: str) -> list[tuple[bool, str]]:
    # Match fenced blocks even when indented (list items, etc.)
    fence = re.compile(r"^\s*```[\w]*\s*$", re.MULTILINE)
    parts: list[tuple[bool, str]] = []
    pos = 0
    in_code = False
    for m in fence.finditer(text):
        if m.start() > pos:
            parts.append((in_code, text[pos : m.start()]))
        in_code = not in_code
        pos = m.end()
    parts.append((in_code, text[pos:]))
    return parts


def prose_pass(segment: str) -> str:
    t = segment.replace(" — ", ", ")
    # Remaining em dashes (often unspaced): prefer comma for readability
    t = t.replace("\u2014", ", ")
    t = re.sub(r"\b§\s*(\d+(?:\.\d+)?)\b", r"section \1", t)
    t = re.sub(r"\*\*§(\d+)\*\*", r"**section \1**", t)
    # **Label**, Rest at start of sentence -> **Label.** Rest (numbered steps)
    t = re.sub(
        r"^(\s*\d+\.\s+\*\*[^*]+\*\*),\s+([A-Z])",
        r"\1. \2",
        t,
        flags=re.MULTILINE,
    )
    t = re.sub(r",(\s*,)+", r",", t)
    return t


def process_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    out: list[str] = []
    changed = False
    for is_code, seg in split_fences(raw):
        if is_code:
            out.append(seg)
        else:
            new = prose_pass(seg)
            if new != seg:
                changed = True
            out.append(new)
    new_text = "".join(out)
    if new_text != raw:
        path.write_text(new_text, encoding="utf-8")
    return changed


def main() -> None:
    base = ROOT
    n = 0
    for ch in sorted(base.glob("Chapter-*")):
        if not ch.is_dir():
            continue
        for md in sorted(ch.rglob("*.md")):
            name = md.name
            if name.startswith("CODIO_") and "SYNC" in name:
                continue
            if "GAPS" in name.upper():
                continue
            if process_file(md):
                n += 1
                print(md.relative_to(base.parent))
    print(f"Updated {n} files.")


if __name__ == "__main__":
    main()
