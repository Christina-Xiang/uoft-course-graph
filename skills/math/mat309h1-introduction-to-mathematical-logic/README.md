# MAT309H1 — Introduction to Mathematical Logic

UofT · Math · Half Credit

## About

This skill package provides three teaching modes for mastering MAT309H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of formal languages and truth |
| Deductive | `deductive.json` | Step-by-step derivation of Gödel's Completeness Theorem: $\Gamma \vdash \varphi \iff \Gamma \models \varphi$ |
| Correction | `correction.json` | Fixing the error: confusing completeness of a logic with completeness of a theory |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/math/mat309h1-introduction-to-mathematical-logic ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/math/mat309h1-introduction-to-mathematical-logic ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/math/mat309h1-introduction-to-mathematical-logic/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
