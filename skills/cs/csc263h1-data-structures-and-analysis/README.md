# CSC263H1 — Data Structures and Analysis

UofT · CS · Half Credit

## About

This skill package provides three teaching modes for mastering CSC263H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of amortised analysis |
| Deductive | `deductive.json` | Step-by-step derivation of union-find has amortised $O(\alpha(n))$ per operation |
| Correction | `correction.json` | Fixing the error: hash tables are $O(1)$ worst-case |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/cs/csc263h1-data-structures-and-analysis ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/cs/csc263h1-data-structures-and-analysis ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/cs/csc263h1-data-structures-and-analysis/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
