# STA237H1 — Probability, Statistics and Data Analysis I

UofT · Stats · Half Credit

## About

This skill package provides three teaching modes for mastering STA237H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of probability spaces and axioms |
| Deductive | `deductive.json` | Step-by-step derivation of Law of Large Numbers: $\bar{X}_n \xrightarrow{p} \mu$ |
| Correction | `correction.json` | Fixing the error: confusing $P(A \cap B)$ with $P(A)P(B)$ — assuming independence without justification |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/stats/sta237h1-probability-statistics-and-data-analysis-i ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/stats/sta237h1-probability-statistics-and-data-analysis-i ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/stats/sta237h1-probability-statistics-and-data-analysis-i/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
