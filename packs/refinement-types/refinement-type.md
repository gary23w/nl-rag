---
title: "Refinement type"
source: https://en.wikipedia.org/wiki/Refinement_type
domain: refinement-types
license: CC-BY-SA-4.0
tags: refinement type, liquid types, predicate subtyping, dependent refinement
fetched: 2026-07-02
---

# Refinement type

In type theory, a **refinement type** is a type endowed with a predicate which is assumed to hold for any element of the refined type. Refinement types can express preconditions when used as function arguments or postconditions when used as return types: for instance, the type of a function which accepts natural numbers and returns natural numbers greater than 5 may be written as $f:\mathbb {N} \rightarrow \{n\in \mathbb {N} \,|\,n>5\}$ . Refinement types are thus related to behavioral subtyping.

## History

The concept of refinement types was first introduced in Freeman and Pfenning's 1991 *Refinement types for ML*, which presents a type system for a subset of Standard ML. The type system "preserves the decidability of ML's type inference" whilst still "allowing more errors to be detected at compile-time". In more recent times, refinement type systems have been developed (primary in academia) for languages such as Haskell, TypeScript, Rust, and as libraries for real world usage in Scala.
