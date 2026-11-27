# MAT334H1 — Complex Variables

UofT · Math · Half Credit

## About

This skill package provides three teaching modes for mastering MAT334H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of complex differentiability |
| Deductive | `deductive.json` | Step-by-step derivation of Cauchy's Integral Formula: $f(a) = \frac{1}{2\pi i}\oint_\gamma \frac{f(z)}{z-a}\,dz$ |
| Correction | `correction.json` | Fixing the error: $\log(z)$ is multi-valued — forgetting branch cuts |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/math/mat334h1-complex-variables ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/math/mat334h1-complex-variables ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/math/mat334h1-complex-variables/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
