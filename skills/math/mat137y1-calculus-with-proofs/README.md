# MAT137Y1 — Calculus with Proofs

UofT · Mathematics Major · Year 1 · 0.5 credit (full-year course)

## About

This skill package provides three teaching modes for mastering MAT137Y1:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of ε-δ limit definition |
| Deductive | `deductive.json` | Step-by-step derivation of the product rule |
| Correction | `correction.json` | Fixing the chain-rule inner-derivative pitfall |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/math/mat137y1-calculus-with-proofs ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/math/mat137y1-calculus-with-proofs ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/math/mat137y1-calculus-with-proofs/SKILL.md
```

## References

All supporting documents are in `references/`:

- `formulas.md` — derivative/integral/limit quick reference
- `proof-techniques.md` — ε-δ templates, MVT patterns, induction
- `counterexamples.md` — 28 classic counterexamples
- `concept-map.md` — unit-to-unit concept dependency map
- `checklist.md` — per-unit progress tracker
- `planetary-orbits-lagrange.md` — applied derivation (Kepler + Lagrange)

## Skill Taxonomy

| Tier | Skills |
|------|--------|
| A. Foundational | A1 Formal Definition, A2 Inequality, A3 Symbolic, A4 Counterexample |
| B. Core | B1 Limits, B2 Continuity, B3 Differentiation, B4 Integration, B5 Series, B6 Expansion |
| C. Synthesis | C1 Proof, C2 Modeling, C3 Error Control, C4 Strategy |

## License

See `LICENSE` file.
