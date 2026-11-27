# STA314H1 — Statistical Methods for Machine Learning I

UofT · Stats · Half Credit

## About

This skill package provides three teaching modes for mastering STA314H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of the bias-variance tradeoff |
| Deductive | `deductive.json` | Step-by-step derivation of representer theorem for kernel methods |
| Correction | `correction.json` | Fixing the error: cross-validation leaks information when feature selection is done before the split |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/stats/sta314h1-statistical-methods-for-machine-learning-i ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/stats/sta314h1-statistical-methods-for-machine-learning-i ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/stats/sta314h1-statistical-methods-for-machine-learning-i/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
