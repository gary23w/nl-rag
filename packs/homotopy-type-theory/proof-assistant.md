---
title: "Proof assistant"
source: https://en.wikipedia.org/wiki/Proof_assistant
domain: homotopy-type-theory
license: CC-BY-SA-4.0
tags: homotopy type theory, intuitionistic type theory, univalent foundations, identity type
fetched: 2026-07-02
---

# Proof assistant

In computer science and mathematical logic, a **proof assistant** or **interactive theorem prover** is a software tool to assist with the development of formal proofs by human–machine collaboration. This involves some sort of interactive proof editor, or other interface, with which a human can guide the search for proofs, the details of which are stored in, and some steps provided by, a computer.

A recent effort within this field is making these tools use artificial intelligence to automate the formalization of ordinary mathematics.

## Automated proof checking

**Automated proof checking** is the process of using software for checking proofs for correctness. It is one of the most developed fields in automated reasoning. Automated proof checking differs from automated theorem proving in that automated proof checking simply mechanically checks the formal workings of an existing proof, instead of trying to develop new proofs or theorems itself. Because of this, the task of automated proof verification is much simpler than that of automated theorem proving, allowing automated proof checking software to be much simpler than automated theorem proving software.

Because of this small size, some automated proof checking systems can have less than a thousand lines of core code, and are thus themselves amenable to both hand-checking and automated software verification. The Mizar system, HOL Light, and Metamath are examples of automated proof checking systems. Automated proof checking can be done either as a batch operation, or interactively, as part of an interactive theorem proving system.

## History

Automath, which was developed by Nicolaas Govert de Bruijn starting in 1967, is often considered the first proof checker and the first system to utilize the Curry–Howard correspondence between programs and proofs. Automath was used by L.S. van Benthem Jutting in 1977 to formalize Landau's *Foundations of Analysis*, which was the first formalization of the real numbers.

In 1973, Robert Boyer and J Moore published *Proving Theorems about LISP Functions* which aimed to verify programs, not mathematics. Their theorem prover is now known as ACL2.

In the 1970s, Edinburgh LCF introduced the idea of using a functional programming language as the metalanguage for a theorem prover, and led to the HOL family of proof assistants.

The 1990s saw the rise of Rocq, (then known as Coq), which has been used for many large-scale formalization projects. Since the late 2010s, Lean, a proof assistant strongly influenced by Rocq, has become another popular choice, especially for formalizing mathematics.

## System comparison

Name

Latest version

Developer(s)

Implementation language

Features

Higher-order logic

Dependent types

Small

kernel

Proof automation

Proof by

reflection

Code generation

ACL2

8.3

Matt Kaufmann

,

J Strother Moore

Common Lisp

No

Untyped

No

Yes

Yes

Already executable

Agda

2.8.0

Ulf Norell, Nils Anders Danielsson, and Andreas Abel (

Chalmers

and

Gothenburg

)

Haskell

Yes

Yes

Yes

No

Partial

Already executable

Albatross

0.4

Helmut Brandl

OCaml

Yes

No

Yes

Yes

Unknown

Not yet implemented

F*

repository

Microsoft Research

and

INRIA

F*

Yes

Yes

No

Yes

Yes

Yes

HOL Light

repository

John Harrison

OCaml

Yes

No

Yes

Yes

No

No

HOL4

Kananaskis-13 (or repo)

Michael Norrish, Konrad Slind, and others

Standard ML

Yes

No

Yes

Yes

No

Yes

Idris

2 0.6.0

Edwin Brady

Idris

Yes

Yes

Yes

Unknown

Partial

Yes

Isabelle

Isabelle2025 (March 2025)

Larry Paulson

(

Cambridge

),

Tobias Nipkow

(

München

) and Makarius Wenzel

Standard ML

,

Scala

Yes

No

Yes

Yes

Yes

Yes

Lean

v4.28.0-rc1

Leonardo de Moura

(

AWS

)

C++

, Lean

Yes

Yes

Yes

Yes

Yes

Yes

LEGO

1.3.1

Randy Pollack (

Edinburgh

)

Standard ML

Yes

Yes

Yes

No

No

No

Metamath

v0.198

Norman Megill

ANSI C

Mizar

8.1.11

Białystok University

Free Pascal

Partial

Yes

No

No

No

No

Nqthm

NuPRL

5

Cornell University

Common Lisp

Yes

Yes

Yes

Yes

Unknown

Yes

PVS

6.0

SRI International

Common Lisp

Yes

Yes

No

Yes

No

Unknown

Rocq

9.0

INRIA

OCaml

Yes

Yes

Yes

Yes

Yes

Yes

Twelf

1.7.1

Frank Pfenning

, Carsten Schürmann

Standard ML

Yes

Yes

Unknown

No

No

Unknown

- ACL2 – a programming language, a first-order logical theory, and a theorem prover (with both interactive and automatic modes) in the Boyer–Moore tradition.
- HOL theorem provers – A family of tools ultimately derived from the LCF theorem prover. In these systems, the logical core is a library of their programming language. Theorems represent new elements of the language and can only be introduced via "strategies" which guarantee logical correctness. Strategy composition gives users the ability to produce significant proofs with relatively few interactions with the system. Members of the family include:
  - HOL4 – The "primary descendant", still under active development. Support for both Moscow ML and Poly/ML. Has a BSD-style license.
  - HOL Light – A thriving "minimalist fork". OCaml based.
  - ProofPower – Went proprietary, then returned to open source. Based on Standard ML.
- IMPS, An Interactive Mathematical Proof System.
- Isabelle is an interactive theorem prover where other systems can be encoded. Isabelle/HOL is its most popular instance, whose foundation is close to that of the HOL prover. Other instances include Isabelle/ZF and Isabelle/FOL. The main code-base is BSD-licensed, but the Isabelle distribution bundles many add-on tools with different licenses.
- Jape – Java based.
- Lean is both an interactive theorem prover and a functional, dependently-typed programming language. It is based on the calculus of inductive constructions with non-cumulative universes. Since version 4 (released in 2023), it is self-hosting. It can be used to formalise mathematics (and has a large, coherent library for formal mathematics), but also for software and hardware verification.
- LEGO
- Matita – A light system based on the calculus of inductive constructions.
- MINLOG – A proof assistant based on first-order minimal logic.
- Mizar – A proof assistant based on first-order logic, in a natural deduction style, and Tarski–Grothendieck set theory.
- PhoX – A proof assistant based on higher-order logic which is eXtensible.
- Prototype Verification System (PVS) – a proof language and system based on higher-order logic.
- Rocq (formerly named *Coq*) – A popular interactive theorem prover based on the calculus of inductive constructions.
- Theorem Proving System (TPS) and ETPS – Interactive theorem provers also based on simply typed lambda calculus, but based on an independent formulation of the logical theory and independent implementation.

## User interfaces

A commonly used front-end for proof assistants was the Emacs-based Proof General, developed at the University of Edinburgh. Nowadays, many provers include their own editor. Rocq includes RocqIDE, which is based on OCaml/Gtk. Isabelle includes Isabelle/jEdit, which is based on jEdit and the Isabelle/Scala infrastructure for document-oriented proof processing. More recently, Visual Studio Code extensions have been developed for Rocq, Isabelle by Makarius Wenzel, and for Lean 4 by the leanprover developers.

## Formalization extent

Freek Wiedijk has been keeping a ranking of proof assistants by the amount of formalized theorems out of a list of 100 well-known theorems. As of September 2025, only six systems have formalized proofs of more than 70% of the theorems, namely Isabelle, HOL Light, Lean, Rocq, Metamath and Mizar.

## Notable formalized proofs

The following is a list of notable proofs that have been formalized within proof assistants.

| Theorem | Proof assistant | Year |
|---|---|---|
| Four color theorem | Rocq | 2005 |
| Feit–Thompson theorem | Rocq | 2012 |
| Fundamental group of the circle | Rocq | 2013 |
| Erdős–Graham problem | Lean | 2022 |
| Polynomial Freiman-Ruzsa conjecture over $\mathbb {F} _{2}$ | Lean | 2023 |
| BB(5) = 47,176,870 | Rocq | 2024 |
