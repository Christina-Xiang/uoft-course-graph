# STA410H1 — Statistical Computation

UofT · Stats · Half Credit

## About

This skill package provides three teaching modes for mastering STA410H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of generating random variables from a uniform source |
| Deductive | `deductive.json` | Step-by-step derivation of Metropolis-Hastings Algorithm |
| Correction | `correction.json` | Fixing the error: burn-in removes the need for MCMC convergence diagnostics |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/stats/sta410h1-statistical-computation ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/stats/sta410h1-statistical-computation ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/stats/sta410h1-statistical-computation/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
