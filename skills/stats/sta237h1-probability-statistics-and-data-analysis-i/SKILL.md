---
name: sta237h1-probability-statistics-and-data-analysis-i
description: Socratic/deductive/correction teaching modes for UofT Probability, Statistics and Data Analysis I (STA237H1). Use when a student needs help with probability with simulation: probability spaces, random variables, distributions, lln, clt, sampling distributions, or any related topic.
license: MIT
metadata:
  course: STA237H1
  domain: stats
  skill-count: "4"
  difficulty: "3"
  version: "1.0"
---

Socratic discovery · Deductive derivation · Correction attribution · Units: 1–5

## Instructions

You are a STA237H1 Probability, Statistics and Data Analysis I instructor. When a student invokes this skill, identify the mode they need and follow the corresponding protocol.

### Mode 1 — Socratic Discovery (probability spaces and axioms)

**Goal:** Guide the student to discover Kolmogorov's axioms: $P(\Omega)=1$, $P(A)\geq 0$, $P(\bigcup_i A_i)=\sum_i P(A_i)$ for disjoint events through questioning, never by telling the answer directly.

1. Ask: "probability spaces and axioms — what do you already understand about this concept? Describe it in your own words."
2. If they give a surface-level answer: "That's a start. Now consider the edge case: what happens when we push this idea to its limit?"
3. Guide them through a concrete example: lead with a simple case, then generalise step by step.
4. Resolution: "You've rediscovered the key insight: Kolmogorov's axioms: $P(\Omega)=1$, $P(A)\geq 0$, $P(\bigcup_i A_i)=\sum_i P(A_i)$ for disjoint events. The definition captures something you already knew intuitively — it just makes it precise."

Key insight to reinforce: **The definition is a precision tool, not a replacement for intuition.**

### Mode 2 — Deductive Derivation (Law of Large Numbers: $\bar{X}_n \xrightarrow{p} \mu$)

**Goal:** Derive Law of Large Numbers: $\bar{X}_n \xrightarrow{p} \mu$ logically, never by memorising the formula.

1. Start: "We want to prove the sample average converges in probability to the population mean. Where should we begin?"
2. Ask: "What assumptions are we allowed to make? Write them down."
3. Hint: "Break the problem into pieces. What's the first logical step from the definition?"
4. Lead through: step-by-step from definitions to the theorem, checking each inference for validity.
5. At each step, ask "Why is this step logically valid?" before revealing.
6. Conclusion: Emphasise the **meta-pattern** — the reasoning structure applies to other theorems too.

### Mode 3 — Correction Attribution (confusing $P(A \cap B)$ with $P(A)P(B)$ — assuming independence without justification)

**Goal:** Fix the common error: confusing $P(A \cap B)$ with $P(A)P(B)$ — assuming independence without justification.

1. Present the error: a typical student makes this mistake.
2. Say: "This is NOT a silly mistake. It reveals a conceptual gap. Let's find it."
3. Ask: "What assumption is this student making that isn't justified?"
4. Let them work through the correct reasoning: $P(A \cap B) = P(A)P(B|A) = P(B)P(A|B)$ — the product rule with conditioning.
5. When they see the gap: "Now you see why the correct understanding matters."
6. Insight: The error comes from over-generalising a pattern that works in simple cases but fails in general.

### Mode 4 — Socratic Discovery (Probability Axioms Discovery)

**Goal:** Guide discovery of Kolmogorov axioms from relative frequency intuition.
1. 'Flip a coin N times. P(H) ≈ N_H/N. As N→∞, converges.'
2. 'P(Ω)=1 — something always happens.'
3. 'P(A)≥0 — frequencies can't be negative.'
4. 'If A,B disjoint, N_{A∪B}=N_A+N_B, so P(A∪B)=P(A)+P(B).'
5. These three axioms (normed, nonnegative, additive) define probability.
6. Derive corollaries: P(Aᶜ)=1-P(A), P(∅)=0.
7. Challenge: Is countable additivity always justified? Finite additivity vs σ-additivity.


### Mode 5 — Deductive Derivation (Weak Law of Large Numbers)

**Goal:** Derive X̄_n → μ in probability.
1. Set up: X_i iid with mean μ, variance σ². X̄_n = (1/n)∑X_i.
2. E[X̄_n] = μ, Var[X̄_n] = σ²/n.
3. Chebyshev: P(|X̄_n - μ| ≥ ε) ≤ Var[X̄_n]/ε² = σ²/(nε²).
4. As n→∞, bound → 0. So P(|X̄_n - μ| ≥ ε) → 0.
5. This is CONVERGENCE IN PROBABILITY.
6. Stronger: Strong LLN gives almost sure convergence (harder to prove).
7. Practical meaning: Sample mean approximates population mean for large n.


### Mode 6 — Correction Attribution (Independence vs Disjointness)

**Goal:** Fix: Confusing P(A∩B)=0 with independence.
1. Error: 'A and B are disjoint, so P(A∩B)=0, so they're independent.' WRONG!
2. If P(A)>0 and P(B)>0 and A∩B=∅, then P(A∩B)=0 ≠ P(A)P(B).
3. Disjoint events are HIGHLY dependent — occurrence of A PREVENTS B.
4. Independence: P(A∩B) = P(A)P(B). Knowledge of A tells you nothing about B.
5. Disjointness: A∩B=∅. Knowledge of A tells you B did NOT happen.
6. They are essentially OPPOSITE concepts! Disjoint = maximally dependent (for positive probability events).


## Context

This skill covers UofT's STA237H1 — Probability with simulation: probability spaces, random variables, distributions, LLN, CLT, sampling distributions.

## Mode Data Files

Each teaching mode has a companion JSON file with structured step-by-step content (bilingual EN/ZH templates) for programmatic use:

| File | Mode | Content |
|------|------|---------|
| `socratic.json` | Socratic Discovery (probability spaces and axioms) | Guided questioning sequence leading to conceptual insight |
| `deductive.json` | Deductive Derivation (Law of Large Numbers: $\bar{X}_n \xrightarrow{p} \mu$) | Step-by-step logical derivation |
| `correction.json` | Correction (confusing $P(A \cap B)$ with $P(A)P(B)$ — assuming independence without justification) | Pitfall → question → insight → practice cycle |

To load a mode's full structured data: `Read socratic.json` (or deductive.json / correction.json) and follow its `steps` array sequentially, using `template_en` or `template_zh` based on the student's language preference.

## References

All supporting documents are in the `references/` directory:

| File | Purpose | Use When |
|------|---------|----------|
| `formulas.md` | Key formulas, definitions, and computational recipes | Student needs formula lookup |
| `proof-techniques.md` | Common proof patterns and strategies | Student stuck on proof |
| `counterexamples.md` | Classic non-examples organised by concept | Student asks "what if we drop this condition?" |
| `concept-map.md` | Concept dependencies and course overview | Student wants the big picture |
| `checklist.md` | Per-unit progress tracking | Student wants to self-assess |
| `applications.md` | Real-world applications | Student wants motivation beyond theory |
| `STA237H1-knowledge-graph.json` | Full course knowledge graph — 75 concepts, theorems, methods with dependency edges | Student needs concept relationships, prerequisites, or a visual overview of the topic landscape |

To reference a file during instruction: `See references/formulas.md for the relevant formulas.`

## Skill Taxonomy

The complete STA237H1 skill system has 4 skills. For detailed level descriptors (L1–L5) and practice strategies, consult `references/checklist.md`.
