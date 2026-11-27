# STA261H1 — Probability and Statistics II

UofT · Stats · Half Credit

## About

This skill package provides three teaching modes for mastering STA261H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of sufficiency and the Rao-Blackwell Theorem |
| Deductive | `deductive.json` | Step-by-step derivation of Rao-Blackwell Theorem: $E[\delta(X) \mid T(X)]$ has variance no larger than $\delta(X)$ |
| Correction | `correction.json` | Fixing the error: UMVUE always exists and is unique |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/stats/sta261h1-probability-and-statistics-ii ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/stats/sta261h1-probability-and-statistics-ii ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/stats/sta261h1-probability-and-statistics-ii/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
