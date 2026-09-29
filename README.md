# Zodchiy — Зодчий

**UX/UI design and visual direction, grounded in the user's task.**

[Русская версия](README.ru.md)

Zodchiy is a skill for designing interfaces, exploring visual concepts, and reviewing the result. It connects user tasks, interface structure, and visual choices, then guides checks against the project's requirements and references.

The name is the Russian word for a master builder or architect. A companion to [Chtets](https://github.com/RIV1992/chtets): **Chtets shapes the thought; Zodchiy shapes the space where people act.**

## Status

**0.3.0 — an authored catalog loaded on demand.** Three directions, a separate two-color image variant, five light Material Presence palettes, two typography profiles, and two editorial patterns. Task and existing project decisions come first; a local fix does not trigger style selection. The core stays within 702 words. See [evaluation](docs/evaluation.md) for checks and limits.

The skill instructions are in Russian. The package is Markdown, YAML, and JSON; it has no runtime dependencies and does not train the model.

## What it covers

- Find whether the problem lies in the product model, user flow, information hierarchy, visual composition, or implementation.
- Explore alternatives when a choice is open; implement the agreed direction when it is settled.
- Connect a visual reference to an observable property, an implementation choice, and the actual rendered result.
- Check meaning and behavior, visual composition, and implementation separately.
- Record the scope and evidence behind a lesson without turning it into a universal design rule.

## Install and use

Copy the complete [`skills/zodchiy`](skills/zodchiy) directory to the skill location supported by your agent. Keep its `references/` and `data/` directories alongside `SKILL.md`. See [installation](docs/installation.md).

For clients that support explicit skill invocation:

```text
Используй $zodchiy: проверь UX/UI этого интерфейса по задаче пользователя,
требованиям проекта и приложенным референсам.
```

Supply the actual brief and relevant artifacts. A build passing is not evidence that the visual result has been accepted by a person.

## Use the catalog

```text
Zodchiy, choose a direction from the catalog for this brief.
Zodchiy, use Material Presence with the Warm palette; keep project fonts.
Zodchiy, draft a photo-treatment brief for Presence / Style 04.
Zodchiy, use First Page for the catalog and Chorus for supported conclusions.
```

The [catalog](skills/zodchiy/references/catalog.md) separates composition, image treatment, systems, and patterns. Gouache derives color from the source photo; the two-color print variant has its own palette. The original Style 04 visual anchor is not bundled, so exact reproduction is not promised. Numeric profiles remain working foundations that need verification in the target interface. Russian pattern names are «Первая полоса» and «Хор».

## Repository map

| Path | Purpose |
|---|---|
| [skills/zodchiy/SKILL.md](skills/zodchiy/SKILL.md) | Compact core workflow and reference routing |
| [skills/zodchiy/references](skills/zodchiy/references) | Workspaces, explanation, reading, visual direction, and learning |
| [skills/zodchiy/data/profiles.json](skills/zodchiy/data/profiles.json) | Canonical palette, typography, and color-role profiles |
| [skills/zodchiy/agents/openai.yaml](skills/zodchiy/agents/openai.yaml) | Optional client display metadata |
| [docs/installation.md](docs/installation.md) | Installation and portable use |
| [docs/development.md](docs/development.md) | Package boundaries and maintenance |
| [docs/evaluation.md](docs/evaluation.md) | Checks, supporting artifacts, and limits of the evidence |
| [scripts/validate.py](scripts/validate.py) | Local structure, link, and core-size checks |

The core has a 702-word ceiling, measured as whitespace-separated words including frontmatter. Load supporting notes only when they fit the task. Public contributions must exclude personal cases and private artifacts, including disguised copies of them.

## Checks

```bash
python3 scripts/validate.py
```

These are package checks, not an evaluation of design quality. See [contributing](CONTRIBUTING.md) and the [changelog](CHANGELOG.md).

## License

[MIT](LICENSE), copyright 2026 RIV1992.
