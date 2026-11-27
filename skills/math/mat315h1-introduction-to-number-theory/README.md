# MAT315H1 — Introduction to Number Theory

UofT · Math · Half Credit

## About

This skill package provides three teaching modes for mastering MAT315H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of prime numbers |
| Deductive | `deductive.json` | Step-by-step derivation of Law of Quadratic Reciprocity |
| Correction | `correction.json` | Fixing the error: $\mathbb{Z}/n\mathbb{Z}$ is a field $\iff$ $n$ is prime — ignoring non-prime modulus structures |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/math/mat315h1-introduction-to-number-theory ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/math/mat315h1-introduction-to-number-theory ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/math/mat315h1-introduction-to-number-theory/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
