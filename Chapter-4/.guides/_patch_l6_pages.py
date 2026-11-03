import pathlib
import re

base = pathlib.Path(__file__).resolve().parent / "content" / "Level-6---Sub-Agents-c7d8"
for p in base.rglob("*.json"):
    if p.name == "index.json":
        continue
    text = p.read_text(encoding="utf-8")
    new = text.replace(
        '"layout":"1-panel","path":[]',
        '"layout":"2-panels-tree-guides-left","path":["level6"]',
    )
    new = re.sub(r'"path": \[\]', '"path": ["level6"]', new)
    if new != text:
        p.write_text(new, encoding="utf-8")
        print("updated", p.relative_to(base))
