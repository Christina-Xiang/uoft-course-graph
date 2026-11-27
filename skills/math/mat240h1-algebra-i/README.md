# MAT240H1 — Algebra I

UofT · Math · Half Credit

## About

This skill package provides three teaching modes for mastering MAT240H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of vector spaces over arbitrary fields |
| Deductive | `deductive.json` | Step-by-step derivation of Cayley-Hamilton Theorem: $p_A(A)=0$ |
| Correction | `correction.json` | Fixing the error: assuming every linear operator has an eigenvalue |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/math/mat240h1-algebra-i ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/math/mat240h1-algebra-i ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/math/mat240h1-algebra-i/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
