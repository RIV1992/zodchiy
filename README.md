# Zodchiy — Зодчий

**UX/UI design and visual direction, grounded in the user's task.**

[Русская версия](README.ru.md)

Zodchiy is a skill for designing interfaces, exploring visual concepts, and reviewing the result. It connects user tasks, interface structure, and visual choices, then guides checks against the project's requirements and references.

The name is the Russian word for a master builder or architect. A companion to [Chtets](https://github.com/RIV1992/chtets): **Chtets shapes the thought; Zodchiy shapes the space where people act.**

## Status

**0.2.0 — focused workflow update.** This version adds three refinements: follow the user's route from the ordinary entry point through completion and return; inherit project decisions with scoped exceptions; check affected screens when shared components or styles change. The core remains within its 702-word limit. See [evaluation](docs/evaluation.md) for the checks and their limits.

The skill instructions are in Russian. The package is Markdown and YAML; it has no runtime dependencies and does not train the model.

## What it covers

- Find whether the problem lies in the product model, user flow, information hierarchy, visual composition, or implementation.
- Explore alternatives when a choice is open; implement the agreed direction when it is settled.
- Connect a visual reference to an observable property, an implementation choice, and the actual rendered result.
- Check meaning and behavior, visual composition, and implementation separately.
- Record the scope and evidence behind a lesson without turning it into a universal design rule.

## Install and use

Copy the complete [`skills/zodchiy`](skills/zodchiy) directory to the skill location supported by your agent. Keep its `references/` directory alongside `SKILL.md`. See [installation](docs/installation.md).

For clients that support explicit skill invocation:

```text
Используй $zodchiy: проверь UX/UI этого интерфейса по задаче пользователя,
требованиям проекта и приложенным референсам.
```

Supply the actual brief and relevant artifacts. A build passing is not evidence that the visual result has been accepted by a person.

## Repository map

| Path | Purpose |
|---|---|
| [skills/zodchiy/SKILL.md](skills/zodchiy/SKILL.md) | Compact core workflow and reference routing |
| [skills/zodchiy/references](skills/zodchiy/references) | Workspaces, explanation, reading, visual direction, and learning |
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
