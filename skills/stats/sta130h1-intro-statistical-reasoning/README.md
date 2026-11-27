# STA130H1 — An Introduction to Statistical Reasoning and Data Science

UofT · Stats · Half Credit

## About

This skill package provides three teaching modes for mastering STA130H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of what is a p-value |
| Deductive | `deductive.json` | Step-by-step derivation of Central Limit Theorem: $\bar{X}_n \xrightarrow{d} N(\mu, \sigma^2/n)$ |
| Correction | `correction.json` | Fixing the error: p-value is the probability that $H_0$ is true |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/stats/sta130h1-an-introduction-to-statistical-reasoning-and-data-science ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/stats/sta130h1-an-introduction-to-statistical-reasoning-and-data-science ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/stats/sta130h1-an-introduction-to-statistical-reasoning-and-data-science/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
