# STA257H1 — Probability and Statistics I

UofT · Stats · Half Credit

## About

This skill package provides three teaching modes for mastering STA257H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of probability as measure |
| Deductive | `deductive.json` | Step-by-step derivation of Strong Law of Large Numbers: $\bar{X}_n \xrightarrow{\text{a.s.}} \mu$ |
| Correction | `correction.json` | Fixing the error: confusing convergence in probability with almost sure convergence |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/stats/sta257h1-probability-and-statistics-i ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/stats/sta257h1-probability-and-statistics-i ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/stats/sta257h1-probability-and-statistics-i/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
