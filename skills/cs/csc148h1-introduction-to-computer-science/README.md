# CSC148H1 — Introduction to Computer Science

UofT · CS · Half Credit

## About

This skill package provides three teaching modes for mastering CSC148H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of recursion |
| Deductive | `deductive.json` | Step-by-step derivation of induction for recursion correctness |
| Correction | `correction.json` | Fixing the error: infinite recursion — no base case or base case never reached |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/cs/csc148h1-introduction-to-computer-science ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/cs/csc148h1-introduction-to-computer-science ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/cs/csc148h1-introduction-to-computer-science/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
