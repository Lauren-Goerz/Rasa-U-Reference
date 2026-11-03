#!/usr/bin/env python3
"""
Verify Codio guide TOC coherence under .guides/content/.

Checks:
- Root index.json chapter order: each entry is an existing chapter folder with chapter index.json.
- Each chapter index unit order: each unit folder exists and has unit index.json.
- Each unit index page order: every id has matching .md and .json; no stray *.md page stems missing from order.

Exit 0 if all pass; exit 1 with messages on failure.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    content = repo / ".guides" / "content"
    root_idx_path = content / "index.json"
    if not root_idx_path.is_file():
        print("ERROR: missing", root_idx_path, file=sys.stderr)
        return 1

    root_idx = json.loads(root_idx_path.read_text(encoding="utf-8"))
    errors: list[str] = []

    chapter_order = root_idx.get("order", [])
    for ch_name in chapter_order:
        ch_dir = content / ch_name
        if not ch_dir.is_dir():
            errors.append(f"Root order: chapter folder missing: {ch_name}")
            continue
        ch_json = ch_dir / "index.json"
        if not ch_json.is_file():
            errors.append(f"Chapter {ch_name}: missing index.json")
            continue
        ch = json.loads(ch_json.read_text(encoding="utf-8"))
        for unit_name in ch.get("order", []):
            u_dir = ch_dir / unit_name
            if not u_dir.is_dir():
                errors.append(f"{ch_name}: unit folder missing: {unit_name}")
                continue
            u_json = u_dir / "index.json"
            if not u_json.is_file():
                errors.append(f"{ch_name}/{unit_name}: missing index.json")
                continue
            u = json.loads(u_json.read_text(encoding="utf-8"))
            ordered_pages = u.get("order", [])
            md_stems = {p.stem for p in u_dir.glob("*.md")}
            for stem in ordered_pages:
                if not (u_dir / f"{stem}.md").is_file():
                    errors.append(f"{ch_name}/{unit_name}: order lists {stem} but .md missing")
                if not (u_dir / f"{stem}.json").is_file():
                    errors.append(f"{ch_name}/{unit_name}: order lists {stem} but .json missing")
            for stem in md_stems:
                if stem not in ordered_pages:
                    errors.append(
                        f"{ch_name}/{unit_name}: {stem}.md on disk but not in unit index order"
                    )

    # Chapter dirs on disk that look like guides but are not in root order
    for p in content.iterdir():
        if not p.is_dir():
            continue
        if not p.name.startswith("Chapter-"):
            continue
        if p.name not in chapter_order:
            errors.append(f"Chapter folder on disk not in root index order: {p.name}")

    # Unit folders under each chapter vs chapter TOC
    for ch_name in chapter_order:
        ch_dir = content / ch_name
        if not ch_dir.is_dir():
            continue
        ch_json = ch_dir / "index.json"
        if not ch_json.is_file():
            continue
        ch = json.loads(ch_json.read_text(encoding="utf-8"))
        toc_units = set(ch.get("order", []))
        disk_units = {p.name for p in ch_dir.iterdir() if p.is_dir() and p.name.startswith("Unit-")}
        for u in sorted(disk_units - toc_units):
            errors.append(f"{ch_name}: Unit folder on disk not in chapter order: {u}")
        for u in sorted(toc_units - disk_units):
            errors.append(f"{ch_name}: chapter order lists unit but folder missing: {u}")

    if errors:
        print("Guides TOC verification FAILED:", len(errors), "issue(s)", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        return 1

    print("Guides TOC OK:", len(chapter_order), "chapters,", "all unit/page pairs match index order.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
