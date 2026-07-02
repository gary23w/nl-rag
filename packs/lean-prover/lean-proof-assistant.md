---
title: "Lean (proof assistant)"
source: https://en.wikipedia.org/wiki/Lean_(proof_assistant)
domain: lean-prover
license: CC-BY-SA-4.0
tags: lean prover, lean theorem prover, lean4, mathlib lean
fetched: 2026-07-02
---

# Lean (proof assistant)

**Lean** is a proof assistant and a functional programming language. It is based on the calculus of constructions with inductive types. It is a free and open-source software project hosted on GitHub. Development is currently supported by the nonprofit Lean Focused Research Organization (FRO).

## History

Lean was developed primarily by Brazilian computer scientist Leonardo de Moura while employed by Microsoft Research and now Amazon Web Services and has had significant contributions from other coauthors and collaborators during its history.

Launched in 2013, initial versions of the language, later known as Lean 1 and 2, were experimental and contained features such as support for homotopy type theory-based foundations that were later dropped.

Lean 3 (first released Jan 20, 2017) was the first moderately stable version of Lean. It was implemented primarily in C++ with some features written in Lean itself. After version 3.4.2, Lean 3 was officially end-of-lifed while development of Lean 4 began. In this interim period members of the Lean community developed and released unofficial versions up to 3.51.1.

In 2021, Lean 4 was released, which was a reimplementation of the Lean theorem prover capable of producing C code which is then compiled, enabling the development of efficient domain-specific automation. Lean 4 also contains a hygienic macro system and improved type class synthesis and memory management procedures over the previous version. Another benefit compared to Lean 3 is the ability to avoid touching C++ code in order to modify the frontend and other key parts of the core system, as they are now all implemented in Lean and available to the end user to be overridden as needed.

Lean 4 is not backwards-compatible with Lean 3. It uses the C++17 version of C++.

In 2023, the Lean FRO was formed, with the goals of improving the language's scalability and usability, and implementing proof automation.

In 2025, ACM SIGPLAN Programming Languages Software Award was awarded to Gabriel Ebner, Soonho Kong, Leo de Moura and Sebastian Ullrich for Lean, cited for its "significant impact on mathematics, hardware and software verification, and AI".

In 2026, the *mathlib* library was awarded the Demailly prize for open science.

## Overview

Lean includes many features useful for functional programming and theorem proving, such as dependent types, type classes, multi-threading, an expressive tactic language, and a module system.

### Libraries

The official Lean standard library is called *Std* and contains common data structures and functions useful for programming, such as tree maps, hash maps, datetime functions, and concurrency primitives. The standard library is complemented by the community-maintained *batteries*, which implements additional data structures that may be used for both mathematical research and more conventional software development.

In 2017, a community-maintained project to develop a Lean library *mathlib* began, with the goal to digitize as much of pure mathematics as possible in one large cohesive library, up to research level mathematics. As of May 2025, mathlib had formalized over 210,000 theorems and 100,000 definitions in Lean.

Other libraries include *CSLib* which is a theoretical computer science library, *SciLean* which is a library for scientific computing in Lean, and *PhysLib*, whose goal is to digitize physics using Lean.

### Editor integration

Lean integrates with Visual Studio Code, Neovim and Emacs. Interfacing is done via a client-extension and Language Server Protocol server. In these editors, Unicode symbols can be typed using LaTeX-like sequences, such as `\times` for "×".

## Examples (Lean 4)

The natural numbers can be defined as an inductive type. This definition is based on the Peano axioms and states that every natural number is either zero or the successor of some other natural number.

```mw
inductive Nat : Type
  | zero : Nat
  | succ : Nat → Nat
```

Addition of natural numbers can be defined recursively, using pattern matching.

```mw
def Nat.add : Nat → Nat → Nat
  | n, Nat.zero   => n                      -- n + 0 = n  
  | n, Nat.succ m => Nat.succ (Nat.add n m) -- n + succ(m) = succ(n + m)
```

This is a simple proof of $(P\wedge Q)\implies (Q\wedge P)$ for two propositions P and Q (where $\wedge$ is the conjunction and $\implies$ the implication) in Lean using tactic mode:

```mw
theorem and_swap (p q : Prop) : p ∧ q → q ∧ p := by
  intro h            -- assume p ∧ q with proof h, the goal is q ∧ p
  apply And.intro    -- the goal is split into two subgoals, one is q and the other is p
  · exact h.right    -- the first subgoal is exactly the right part of h : p ∧ q
  · exact h.left     -- the second subgoal is exactly the left part of h : p ∧ q
```

This same proof in term mode:

```mw
theorem and_swap (p q : Prop) : p ∧ q → q ∧ p :=
  fun ⟨hp, hq⟩ => ⟨hq, hp⟩
```

The theorem can also be proved using the grind tactic, which uses techniques from SMT solvers to automatically construct proofs:

```mw
theorem and_swap (p q : Prop) : p ∧ q → q ∧ p := by
  grind
```

## Usage

### Mathematics

Lean has received attention from mathematicians such as Thomas Hales, Kevin Buzzard, Terence Tao, and Heather Macbeth. Hales is using it for his project, Formal Abstracts. Buzzard uses it for the Xena project. One of the Xena Project's goals is to rewrite every theorem and proof in the undergraduate math curriculum of Imperial College London in Lean. Tao released a Lean companion to his real analysis textbook *Analysis I*, consisting of a formalization of selected sections of the mathematical text. Macbeth is using Lean to teach students the fundamentals of mathematical proof with instant feedback.

#### Noteworthy formalizations

In 2021, a team of researchers used Lean to verify the correctness of a proof by Peter Scholze in the area of condensed mathematics. The project garnered attention for formalizing a result at the cutting edge of mathematical research. In 2023, Terence Tao used Lean to formalize a proof of the Polynomial Freiman-Ruzsa (PFR) conjecture, a result published by Tao and collaborators in the same year. In 2026, Erdős Problems 728, 347, and 369 were solved using AI assistance and formally verified with Lean.

### Physics

Physlib aspires to be the definitive library for physics in Lean, akin to Mathlib for mathematics. It aims to be a comprehensive repository containing fundamental definitions, theorems, and calculations from physics. Kevin Buzzard at Imperial College London says that formalisation is having a big impact on mathematics, and that there is no reason that theoretical physics can’t be treated in the same way.

> “Ideally, we need a million lines of physics, and that might be hard work to get. If the machines aren’t pretty good at doing physics initially, then there’ll be manual work at the beginning, and then eventually the machines will hopefully take over”

#### Noteworthy formalizations

In 2025, Joseph Tooby-Smith used Lean to discover an error in a paper published in 2006 on the stability of the Two-Higgs-doublet model (2HDM) potential.

### Artificial intelligence

In 2022, OpenAI and Meta AI independently created AI models to generate proofs of various high-school-level olympiad problems in Lean. Meta AI's model is available for public use with the Lean environment.

In 2023, Vlad Tenev and Tudor Achim co-founded startup Harmonic, which aims to reduce AI hallucinations by generating and checking Lean code.

In 2024, Google DeepMind created AlphaProof which proves mathematical statements in Lean at the level of a silver medalist at the International Mathematical Olympiad. This was the first AI system that achieved a medal-worthy performance on a math olympiad's problems.

In April 2025, DeepSeek introduced DeepSeek-Prover-V2, an AI model designed for theorem proving in Lean 4, built on top of DeepSeek-V3.
