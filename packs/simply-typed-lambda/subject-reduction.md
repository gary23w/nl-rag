---
title: "Subject reduction"
source: https://en.wikipedia.org/wiki/Subject_reduction
domain: simply-typed-lambda
license: CC-BY-SA-4.0
tags: simply typed lambda calculus, typing rule, type judgment, strong normalization
fetched: 2026-07-02
---

# Subject reduction

In type theory, a type system has the property of **subject reduction** (also **subject evaluation**, **type preservation** or simply **preservation**) if evaluation of expressions does not cause their type to change. Formally, if ⊢ *e*1 : *τ* and *e*1 → *e*2 then ⊢ *e*2 : *τ*. Intuitively, this means one would not like to write an expression, in say Haskell, of type Int, and have it evaluate to a value *v*, only to find out that *v* is a string.

Together with progress, it is an important meta-theoretical property for establishing type soundness of a type system.

The opposite property, if Γ ⊢ *e*2 : *τ* and *e*1 → *e*2 then Γ ⊢ *e*1 : *τ*, is called **subject expansion**. It often does not hold as evaluation can erase ill-typed sub-terms of an expression, resulting in a well-typed one.
