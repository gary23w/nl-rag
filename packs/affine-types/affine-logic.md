---
title: "Affine logic"
source: https://en.wikipedia.org/wiki/Affine_logic
domain: affine-types
license: CC-BY-SA-4.0
tags: affine type system, affine logic, move semantics, borrow checker
fetched: 2026-07-02
---

# Affine logic

**Affine logic** is a substructural logic whose proof theory rejects the structural rule of contraction. It can also be characterized as linear logic with weakening.

The name "affine logic" is associated with linear logic, to which it differs by allowing the weakening rule. Jean-Yves Girard introduced the name as part of the geometry of interaction semantics of linear logic, which characterizes linear logic in terms of linear algebra; here he alludes to affine transformations on vector spaces.

Affine logic predated linear logic. V. N. Grishin used this logic in 1974, after observing that Russell's paradox cannot be derived in a set theory without contraction, even with an unbounded comprehension axiom. Likewise, the logic formed the basis of a decidable sub-theory of predicate logic, called 'Direct logic' (Ketonen & Wehrauch, 1984; Ketonen & Bellin, 1989).

Affine logic can be embedded into linear logic by rewriting the affine arrow $A\rightarrow B$ as the linear arrow $A\multimap B\otimes \top$ .

Whereas full linear logic (i.e. propositional linear logic with multiplicatives, additives, and exponentials) is undecidable, full affine logic is decidable.

Affine logic forms the foundation of ludics.
