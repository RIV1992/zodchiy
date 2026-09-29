#!/usr/bin/env python3
"""Check this repository's structure, relative Markdown links, and core budget.

Uses only the Python standard library. Does not evaluate design quality or
replace human review of public content.
"""

import json
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
    "skills/zodchiy/references/catalog.md",
    "skills/zodchiy/references/air-constructivism.md",
    "skills/zodchiy/references/presence-gouache.md",
    "skills/zodchiy/references/material-presence.md",
    "skills/zodchiy/data/profiles.json",
)


def contrast(first, second):
    def luminance(color):
        channels = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
                  for c in channels]
        return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))

    bright, dark = sorted((luminance(first), luminance(second)), reverse=True)
    return (bright + 0.05) / (dark + 0.05)


def validate_profiles(path):
    """Validate the authored light-profile contract, not a rendered interface."""
    errors = []
    checks = 0
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if data["schema_version"] != 1:
            raise ValueError("Unsupported profile schema")
        required_roles = {"canvas", "surface", "surfaceMuted", "ink", "inkMuted",
                          "border", "subtleBorder", "accent", "accentInk", "accentSoft", "focus"}

        def color(value):
            if not isinstance(value, str) or not re.fullmatch(r"#[0-9A-Fa-f]{6}", value):
                raise ValueError(f"Invalid sRGB HEX: {value!r}")

        def pair(label, foreground, background, minimum):
            nonlocal checks
            checks += 1
            ratio = contrast(foreground, background)
            if ratio < minimum:
                errors.append(f"{label}: {ratio:.3f}:1 below {minimum}:1")

        if set(data["themes"]) != {"open", "clear", "warm", "balanced", "focused"}:
            raise ValueError("Unexpected theme IDs")
        for name, theme in data["themes"].items():
            tokens = theme["tokens"]
            if theme["mode"] != "light" or set(tokens) != required_roles:
                raise ValueError(f"Incomplete light profile: {name}")
            for value in tokens.values():
                color(value)
            for foreground in ("ink", "inkMuted"):
                for background in ("canvas", "surface", "surfaceMuted"):
                    pair(f"{name}.{foreground}/{background}", tokens[foreground], tokens[background], 4.5)
            for foreground, background in (("accentInk", "accent"), ("ink", "accentSoft")):
                pair(f"{name}.{foreground}/{background}", tokens[foreground], tokens[background], 4.5)
            for background in ("canvas", "surface", "surfaceMuted"):
                pair(f"{name}.border/{background}", tokens["border"], tokens[background], 3)
            pair(f"{name}.focus/surface", tokens["focus"], tokens["surface"], 3)
            for action, value in data["actions"].items():
                if action == "linkDecoration":
                    if value != "underline":
                        raise ValueError("Text links must preserve their underline")
                elif not (isinstance(value, str) and value.startswith("{") and
                          value.endswith("}") and value[1:-1] in tokens):
                    raise ValueError(f"Unknown role alias: {action}={value!r}")
        if set(data["semantics"]) != {"error", "success", "warning", "info"}:
            raise ValueError("Incomplete semantic roles")
        for name, state in data["semantics"].items():
            color(state["foreground"])
            color(state["background"])
            pair(name, state["foreground"], state["background"], 4.5)
        type_profiles = data["typography"]
        if set(type_profiles) != {"mp-noto", "editorial-golos-literata"}:
            raise ValueError("Unexpected typography profiles")
        for profile in type_profiles.values():
            for role in ("sans", "serif"):
                families = profile["families"][role]
                if not isinstance(families, list) or not families or not all(isinstance(f, str) and f for f in families):
                    raise ValueError(f"Invalid font families: {role}")
        if set(type_profiles["mp-noto"]["roles"]) != {"title", "section", "block", "body", "ui", "metadata", "quote"}:
            raise ValueError("Incomplete typography role scale")
        if not type_profiles["editorial-golos-literata"]["scale_policy"]:
            raise ValueError("Editorial typography needs a project scale policy")
        image = data["image_palettes"]["air-print"]
        if image["kind"] != "image-only" or set(image["colors"]) != {"blue", "terracotta", "paper"}:
            raise ValueError("Invalid print image palette")
        for value in image["colors"].values():
            color(value)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        errors.append(f"Profiles: {error}")
    return errors, checks


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

    profile_errors, checks = validate_profiles(ROOT / "skills/zodchiy/data/profiles.json")
    errors.extend(profile_errors)
    print(f"Profiles: {checks} specified opaque color pairs checked")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("Package checks passed. This is not a design-quality evaluation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
