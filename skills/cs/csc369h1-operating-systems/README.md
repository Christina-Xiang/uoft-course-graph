# CSC369H1 — Operating Systems

UofT · CS · Half Credit

## About

This skill package provides three teaching modes for mastering CSC369H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of the operating system as resource manager |
| Deductive | `deductive.json` | Step-by-step derivation of Banker's Algorithm for deadlock avoidance |
| Correction | `correction.json` | Fixing the error: locking always prevents race conditions |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/cs/csc369h1-operating-systems ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/cs/csc369h1-operating-systems ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/cs/csc369h1-operating-systems/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
