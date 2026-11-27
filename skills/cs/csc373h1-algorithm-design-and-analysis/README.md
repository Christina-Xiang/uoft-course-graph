# CSC373H1 — Algorithm Design and Analysis

UofT · CS · Half Credit

## About

This skill package provides three teaching modes for mastering CSC373H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of optimal substructure |
| Deductive | `deductive.json` | Step-by-step derivation of Max-Flow Min-Cut Theorem |
| Correction | `correction.json` | Fixing the error: greedy works whenever the problem has optimal substructure |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/cs/csc373h1-algorithm-design-and-analysis ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/cs/csc373h1-algorithm-design-and-analysis ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/cs/csc373h1-algorithm-design-and-analysis/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
