# STA238H1 — Probability, Statistics and Data Analysis II

UofT · Stats · Half Credit

## About

This skill package provides three teaching modes for mastering STA238H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of maximum likelihood estimation |
| Deductive | `deductive.json` | Step-by-step derivation of Neyman-Pearson Lemma |
| Correction | `correction.json` | Fixing the error: confidence interval $(L,U)$ means $P(\mu \in (L,U))$ — but $\mu$ is fixed, not random |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/stats/sta238h1-probability-statistics-and-data-analysis-ii ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/stats/sta238h1-probability-statistics-and-data-analysis-ii ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/stats/sta238h1-probability-statistics-and-data-analysis-ii/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
