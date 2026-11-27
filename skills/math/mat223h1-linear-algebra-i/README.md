# MAT223H1 — Linear Algebra I

UofT · Mathematics Major · Year 1 · 0.5 credit

## About

This skill package provides three teaching modes for mastering MAT223H1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of the geometric meaning behind algebraic operations |
| Deductive | `deductive.json` | Step-by-step derivation of the Rank-Nullity Theorem |
| Correction | `correction.json` | Fixing the misconception that λ = 0 is "not a real eigenvalue" |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/math/mat223h1-linear-algebra-i ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/math/mat223h1-linear-algebra-i ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/math/mat223h1-linear-algebra-i/SKILL.md
```

## References

All supporting documents are in `references/`:

- `formulas.md` — key definitions, theorems, matrix/determinant recipes
- `proof-techniques.md` — basis extension, dimension arguments, diagonalization criteria
- `counterexamples.md` — 22 classic non-examples organized by concept
- `concept-map.md` — unit-to-unit dependency graph + geometric↔algebraic mapping
- `checklist.md` — per-unit progress tracker with skill self-assessment
- `applications.md` — PageRank, PCA, computer graphics, regression, Markov chains

## Skill Taxonomy

| Tier | Skills |
|------|--------|
| A. Foundational | LA1 Geo-Algebra Translation, LA3 Axiomatic Reasoning |
| B. Core | LA2 Algorithmic Thinking, LA4 Abstraction Lifting, LA5 Determinant Strategy, LA6 Eigen-Patterns, LA7 Projection Geometry |
| C. Synthesis | LA8 Diagonalization Power |

## License

See `LICENSE` file.
