# CSC165H1 — Mathematical Expression and Reasoning for Computer Science

UofT · CS · Half Credit

## About

This skill package provides three teaching modes for mastering CSC165H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of the halting problem |
| Deductive | `deductive.json` | Step-by-step derivation of Master Theorem for divide-and-conquer recurrences |
| Correction | `correction.json` | Fixing the error: confusing $O$ (upper bound) with $\Theta$ (tight bound) |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/cs/csc165h1-mathematical-expression-and-reasoning-for-computer-science ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/cs/csc165h1-mathematical-expression-and-reasoning-for-computer-science ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/cs/csc165h1-mathematical-expression-and-reasoning-for-computer-science/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
