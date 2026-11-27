# MAT224H1 — Linear Algebra II

UofT · Math · Half Credit

## About

This skill package provides three teaching modes for mastering MAT224H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of abstract vector space axioms |
| Deductive | `deductive.json` | Step-by-step derivation of Spectral Theorem for real symmetric matrices: $A = Q\Lambda Q^T$ |
| Correction | `correction.json` | Fixing the error: confusing algebraic multiplicity with geometric multiplicity |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/math/mat224h1-linear-algebra-ii ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/math/mat224h1-linear-algebra-ii ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/math/mat224h1-linear-algebra-ii/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
