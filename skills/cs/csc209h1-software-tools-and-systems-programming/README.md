# CSC209H1 — Software Tools and Systems Programming

UofT · CS · Half Credit

## About

This skill package provides three teaching modes for mastering CSC209H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of pointers and memory |
| Deductive | `deductive.json` | Step-by-step derivation of producer-consumer with bounded buffer |
| Correction | `correction.json` | Fixing the error: buffer overflow: assuming input will fit without checking size |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/cs/csc209h1-software-tools-and-systems-programming ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/cs/csc209h1-software-tools-and-systems-programming ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/cs/csc209h1-software-tools-and-systems-programming/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
