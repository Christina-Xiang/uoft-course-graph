# MAT244H1 — Introduction to Ordinary Differential Equations

UofT · Math · Half Credit

## About

This skill package provides three teaching modes for mastering MAT244H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of direction fields and geometric intuition for ODEs |
| Deductive | `deductive.json` | Step-by-step derivation of variation of parameters for $y''+p(t)y'+q(t)y = g(t)$ |
| Correction | `correction.json` | Fixing the error: assuming $e^{\int p}$ is always the correct integrating factor |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/math/mat244h1-introduction-to-ordinary-differential-equations ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/math/mat244h1-introduction-to-ordinary-differential-equations ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/math/mat244h1-introduction-to-ordinary-differential-equations/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
