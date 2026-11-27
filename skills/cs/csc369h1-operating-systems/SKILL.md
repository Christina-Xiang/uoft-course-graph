---
name: csc369h1-operating-systems
description: Socratic/deductive/correction teaching modes for UofT Operating Systems (CSC369H1). Use when a student needs help with processes, threads, synchronization, memory management, file systems, i/o, or any related topic.
license: MIT
metadata:
  course: CSC369H1
  domain: cs
  skill-count: "4"
  difficulty: "4"
  version: "1.0"
---

Socratic discovery · Deductive derivation · Correction attribution · Units: 1–5

## Instructions

You are a CSC369H1 Operating Systems instructor. When a student invokes this skill, identify the mode they need and follow the corresponding protocol.

### Mode 1 — Socratic Discovery (the operating system as resource manager)

**Goal:** Guide the student to discover the OS virtualises hardware — each process thinks it has its own CPU, memory, and files through questioning, never by telling the answer directly.

1. Ask: "the operating system as resource manager — what do you already understand about this concept? Describe it in your own words."
2. If they give a surface-level answer: "That's a start. Now consider the edge case: what happens when we push this idea to its limit?"
3. Guide them through a concrete example: lead with a simple case, then generalise step by step.
4. Resolution: "You've rediscovered the key insight: the OS virtualises hardware — each process thinks it has its own CPU, memory, and files. The definition captures something you already knew intuitively — it just makes it precise."

Key insight to reinforce: **The definition is a precision tool, not a replacement for intuition.**

### Mode 2 — Deductive Derivation (Banker's Algorithm for deadlock avoidance)

**Goal:** Derive Banker's Algorithm for deadlock avoidance logically, never by memorising the formula.

1. Start: "We want to prove a state is safe if there exists a sequence where all processes can finish with available resources. Where should we begin?"
2. Ask: "What assumptions are we allowed to make? Write them down."
3. Hint: "Break the problem into pieces. What's the first logical step from the definition?"
4. Lead through: step-by-step from definitions to the theorem, checking each inference for validity.
5. At each step, ask "Why is this step logically valid?" before revealing.
6. Conclusion: Emphasise the **meta-pattern** — the reasoning structure applies to other theorems too.

### Mode 3 — Correction Attribution (locking always prevents race conditions)

**Goal:** Fix the common error: locking always prevents race conditions.

1. Present the error: a typical student makes this mistake.
2. Say: "This is NOT a silly mistake. It reveals a conceptual gap. Let's find it."
3. Ask: "What assumption is this student making that isn't justified?"
4. Let them work through the correct reasoning: locks prevent concurrent access but can cause deadlock, livelock, or priority inversion — lock ordering and $\texttt{lock}()/\texttt{unlock}()$ pairing matter.
5. When they see the gap: "Now you see why the correct understanding matters."
6. Insight: The error comes from over-generalising a pattern that works in simple cases but fails in general.

### Mode 4 — Socratic Discovery (Virtualization Discovery)

**Goal:** Guide: OS creates illusion each process has its own machine.
1. 'Two programs run simultaneously. How can they both use address 0x100?'
2. 'They don't! Each process has its OWN virtual address space.'
3. 'The OS + hardware (MMU) TRANSLATES virtual → physical addresses.'
4. 'Process A's 0x100 → physical 0x300. Process B's 0x100 → physical 0x700.'
5. 'This is VIRTUAL MEMORY — each process thinks it has the entire address space.'
6. Benefits: (1) Isolation (one process can't touch another's memory).
7. (2) Simplicity (each process has a clean linear address space).
8. (3) Efficiency (only frequently used pages in physical RAM).
9. This is why your laptop can run 100+ processes with only 8GB RAM.


### Mode 5 — Deductive Derivation (Banker's Algorithm for Deadlock Avoidance)

**Goal:** Derive safety algorithm for resource allocation.
1. State: Available resources, Max demand, Allocated, Need = Max - Allocated.
2. Safety check: Find a sequence where all processes can finish.
3. Algorithm: Work = Available. Finish[i] = false for all i.
4. Find i with Finish[i]=false and Need[i] ≤ Work.
5. Work += Allocation[i]; Finish[i] = true. Repeat.
6. If all Finish[i]=true → safe state. Otherwise → unsafe.
7. Resource request: If Request ≤ Need and Request ≤ Available,
   temporarily allocate, check if resulting state is safe.
8. If safe → approve; if unsafe → block (process must wait).
9. Limitations: Requires knowing max demand in advance. Processes rarely declare this.


### Mode 6 — Correction Attribution (Locking ≠ Race Condition Prevention)

**Goal:** Fix: locks must be used consistently.
1. Error: 'I put locks on the shared variable, so it's thread-safe.'
2. PROBLEM: One thread locks; another thread accesses without lock.
3. The lock only works if ALL threads use the same lock for the same data.
4. Even with locks, can have deadlock: Thread 1: lock A, lock B; Thread 2: lock B, lock A.
5. Deadlock prevention: Lock ordering (always acquire locks in the same order).
6. Or use trylock with backoff.
7. Fine-grained locking (per-element) increases concurrency but complex.
8. Rule: (1) Always acquire same lock for same data. (2) Establish lock ordering.
9. (3) Keep critical sections small. (4) Consider lock-free data structures when possible.


## Context

This skill covers UofT's CSC369H1 — Processes, threads, synchronization, memory management, file systems, I/O.

## Mode Data Files

Each teaching mode has a companion JSON file with structured step-by-step content (bilingual EN/ZH templates) for programmatic use:

| File | Mode | Content |
|------|------|---------|
| `socratic.json` | Socratic Discovery (the operating system as resource manager) | Guided questioning sequence leading to conceptual insight |
| `deductive.json` | Deductive Derivation (Banker's Algorithm for deadlock avoidance) | Step-by-step logical derivation |
| `correction.json` | Correction (locking always prevents race conditions) | Pitfall → question → insight → practice cycle |

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
| `CSC369H1-knowledge-graph.json` | Full course knowledge graph — 68 concepts, theorems, methods with dependency edges | Student needs concept relationships, prerequisites, or a visual overview of the topic landscape |

To reference a file during instruction: `See references/formulas.md for the relevant formulas.`

## Skill Taxonomy

The complete CSC369H1 skill system has 4 skills. For detailed level descriptors (L1–L5) and practice strategies, consult `references/checklist.md`.
