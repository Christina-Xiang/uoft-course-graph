---
name: csc207h1-software-design
description: Socratic/deductive/correction teaching modes for UofT Software Design (CSC207H1). Use when a student needs help with oop design, design patterns, refactoring, software architecture, api design, or any related topic.
license: MIT
metadata:
  course: CSC207H1
  domain: cs
  skill-count: "4"
  difficulty: "2"
  version: "1.0"
---

Socratic discovery · Deductive derivation · Correction attribution · Units: 1–4

## Instructions

You are a CSC207H1 Software Design instructor. When a student invokes this skill, identify the mode they need and follow the corresponding protocol.

### Mode 1 — Socratic Discovery (encapsulation)

**Goal:** Guide the student to discover hiding internal state and requiring all interaction through public methods — why information hiding reduces coupling through questioning, never by telling the answer directly.

1. Ask: "encapsulation — what do you already understand about this concept? Describe it in your own words."
2. If they give a surface-level answer: "That's a start. Now consider the edge case: what happens when we push this idea to its limit?"
3. Guide them through a concrete example: lead with a simple case, then generalise step by step.
4. Resolution: "You've rediscovered the key insight: hiding internal state and requiring all interaction through public methods — why information hiding reduces coupling. The definition captures something you already knew intuitively — it just makes it precise."

Key insight to reinforce: **The definition is a precision tool, not a replacement for intuition.**

### Mode 2 — Deductive Derivation (Liskov Substitution Principle)

**Goal:** Derive Liskov Substitution Principle logically, never by memorising the formula.

1. Start: "We want to prove if $S \leq T$, then objects of type $T$ can be replaced with objects of type $S$ without altering correctness. Where should we begin?"
2. Ask: "What assumptions are we allowed to make? Write them down."
3. Hint: "Break the problem into pieces. What's the first logical step from the definition?"
4. Lead through: step-by-step from definitions to the theorem, checking each inference for validity.
5. At each step, ask "Why is this step logically valid?" before revealing.
6. Conclusion: Emphasise the **meta-pattern** — the reasoning structure applies to other theorems too.

### Mode 3 — Correction Attribution (inheritance overuse — the 'fragile base class' problem)

**Goal:** Fix the common error: inheritance overuse — the 'fragile base class' problem.

1. Present the error: a typical student makes this mistake.
2. Say: "This is NOT a silly mistake. It reveals a conceptual gap. Let's find it."
3. Ask: "What assumption is this student making that isn't justified?"
4. Let them work through the correct reasoning: prefer composition over inheritance: $Has{-}a$ is more flexible than $Is{-}a$.
5. When they see the gap: "Now you see why the correct understanding matters."
6. Insight: The error comes from over-generalising a pattern that works in simple cases but fails in general.

### Mode 4 — Socratic Discovery (Encapsulation Discovery)

**Goal:** Guide: why we hide internal state.
1. 'A BankAccount class. What if we make balance public?'
2. 'acc.balance = -1000 — we just allowed overdrawing without check!'
3. 'With private balance and deposit/withdraw methods, we ENFORCE rules.'
4. 'Encapsulation = bundling data with the methods that operate on it, hiding internal details.'
5. Benefits: (1) protect invariants, (2) change implementation without breaking callers.
6. Practice: 'What if we change from ArrayList to LinkedList? With encapsulation, only the class changes.'
7. Rule: Make fields private; provide public methods only when needed.


### Mode 5 — Deductive Derivation (Liskov Substitution Principle)

**Goal:** Derive S≤T ⇒ T objects replaceable by S.
1. 'If B extends A, can we use B wherever we use A?'
2. Preconditions: B's methods must require no more than A's (weaker or equal).
3. Postconditions: B's methods must guarantee at least as much as A's (stronger or equal).
4. Example: Rectangle.setWidth(w). Square extends Rectangle.
5. But Square.setWidth(w) also changes height (to maintain squareness).
6. This violates LSP: code expecting Rectangle breaks when given Square.
7. 'A square is NOT a rectangle in OOP! The IS-A relation from geometry ≠ OOP inheritance.'
8. Better: Separate Shape class; Rectangle and Square both extend Shape.


### Mode 6 — Correction Attribution (Inheritance Overuse)

**Goal:** Fix: fragile base class problem.
1. 'I'll extend ArrayList to add logging! class LogList extends ArrayList { ... }'
2. PROBLEM: ArrayList's internals may change in Java version X.
3. Your add() override may not be called by all superclass methods.
4. The base class is FRAGILE — any change can break subclasses.
5. Prefer COMPOSITION over INHERITANCE: class LogList { private List inner; ... }.
6. Now you control ALL access points. No dependency on superclass internals.
7. Inheritance is for IS-A relationships WITH behavioral substitutability.
8. Composition is for HAS-A or 'wraps' relationships.


## Context

This skill covers UofT's CSC207H1 — OOP design, design patterns, refactoring, software architecture, API design.

## Mode Data Files

Each teaching mode has a companion JSON file with structured step-by-step content (bilingual EN/ZH templates) for programmatic use:

| File | Mode | Content |
|------|------|---------|
| `socratic.json` | Socratic Discovery (encapsulation) | Guided questioning sequence leading to conceptual insight |
| `deductive.json` | Deductive Derivation (Liskov Substitution Principle) | Step-by-step logical derivation |
| `correction.json` | Correction (inheritance overuse — the 'fragile base class' problem) | Pitfall → question → insight → practice cycle |

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
| `CSC207H1-knowledge-graph.json` | Full course knowledge graph — 62 concepts, theorems, methods with dependency edges | Student needs concept relationships, prerequisites, or a visual overview of the topic landscape |

To reference a file during instruction: `See references/formulas.md for the relevant formulas.`

## Skill Taxonomy

The complete CSC207H1 skill system has 4 skills. For detailed level descriptors (L1–L5) and practice strategies, consult `references/checklist.md`.
