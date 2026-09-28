#!/usr/bin/env python3
"""Check this repository's structure, relative Markdown links, and core budget.

Uses only the Python standard library. Does not evaluate design quality or
replace human review of public content.
"""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "skills/zodchiy/SKILL.md"
CORE_WORD_LIMIT = 702
REQUIRED = (
    "README.md", "README.ru.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
    "docs/installation.md", "docs/development.md", "docs/evaluation.md",
    "skills/zodchiy/SKILL.md", "skills/zodchiy/agents/openai.yaml",
    "skills/zodchiy/references/workspaces.md",
    "skills/zodchiy/references/explanation.md",
    "skills/zodchiy/references/reading.md",
    "skills/zodchiy/references/visual-direction.md",
    "skills/zodchiy/references/learning.md",
)


def main():
    errors = []
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"Missing or empty file: {relative}")

    if CORE.is_file():
        core = CORE.read_text(encoding="utf-8")
        words = len(core.split())
        print(f"Core: {words}/{CORE_WORD_LIMIT} whitespace-separated words")
        if words > CORE_WORD_LIMIT:
            errors.append("Core exceeds the agreed word budget")
        if not core.startswith("---\nname: zodchiy\ndescription: "):
            errors.append("Unexpected core frontmatter")
        if not re.match(r'\A---\nname: zodchiy\ndescription: "[^\n]+"\n---\n', core):
            errors.append("Expected a quoted, single-line description and closing frontmatter")

    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", content):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f"Broken local link in {path.relative_to(ROOT)}: {target}")
        if re.search(r"libfile_[A-Za-z0-9]|sediment://|sandbox:/|/workspace/|/root/\.codex/", content):
            errors.append(f"Internal file reference in {path.relative_to(ROOT)}")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("Package checks passed. This is not a design-quality evaluation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
