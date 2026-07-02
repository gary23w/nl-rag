---
title: "Initial algebra"
source: https://en.wikipedia.org/wiki/Initial_algebra
domain: structural-induction-pl
license: CC-BY-SA-4.0
tags: structural induction, well-founded induction, recursive datatype, inductive proof
fetched: 2026-07-02
---

# Initial algebra

In mathematics, an **initial algebra** is an initial object in the category of F-algebras for a given endofunctor F. This initiality provides a general framework for induction and recursion.

## Examples

### Functor 1 + (−)

Consider the endofunctor 1 + (−), i.e. *F* : **Set** → **Set** sending X to 1 + *X*, where 1 is a one-point (singleton) set, a terminal object in the category. An algebra for this endofunctor is a set X (called the *carrier* of the algebra) together with a function *f* : (1 + *X*) → *X*. Defining such a function amounts to defining a point *x* ∈ *X* and a function *X* → *X*. Define

${\begin{aligned}\operatorname {zero} \colon 1&\longrightarrow \mathbf {N} \\*&\longmapsto 0\end{aligned}}$

and

${\begin{aligned}\operatorname {succ} \colon \mathbf {N} &\longrightarrow \mathbf {N} \\n&\longmapsto n+1.\end{aligned}}$

Then the set **N** of natural numbers together with the function [zero,succ]: 1 + **N** → **N** is an initial F-algebra. The initiality (the universal property for this case) is not hard to establish; the unique homomorphism to an arbitrary F-algebra (*A*, [*e*, *f*]), for *e*: 1 → *A* an element of A and *f*: *A* → *A* a function on A, is the function sending the natural number n to *fn*(*e*), that is, *f*(*f*(…(*f*(*e*))…)), the n-fold application of f to e.

The set of natural numbers is the carrier of an initial algebra for this functor: the point is zero and the function is the successor function.

### Functor 1 + N × (−)

For a second example, consider the endofunctor 1 + **N** × (−) on the category of sets, where **N** is the set of natural numbers. An algebra for this endofunctor is a set X together with a function 1 + **N** × *X* → *X*. To define such a function, we need a point *x* ∈ *X* and a function **N** × *X* → *X*. The set of finite lists of natural numbers is an initial algebra for this functor. The point is the empty list, and the function is cons, taking a number and a finite list, and returning a new finite list with the number at the head.

In categories with binary coproducts, the definitions just given are equivalent to the usual definitions of a natural number object and a list object, respectively.

## Final coalgebra

Dually, a **final coalgebra** is a terminal object in the category of F-coalgebras. The finality provides a general framework for coinduction and corecursion.

For example, using the same functor 1 + (−) as before, a coalgebra is defined as a set X together with a function *f* : *X* → (1 + *X*). Defining such a function amounts to defining a partial function *f'*: *X* ⇸ *X* whose domain is formed by those $x\in X$ for which *f*(*x*) does not belong to 1. Having such a structure, we can define a chain of sets: *X*0 being a subset of *X* on which *f*′ is not defined, *X*1 which elements map into *X*0 by *f*′, *X*2 which elements map into *X*1 by *f*′, etc., and *X**ω* containing the remaining elements of X. With this in view, the set $\mathbf {N} \cup \{\omega \}$ , consisting of the set of natural numbers extended with a new element ω, is the carrier of the final coalgebra, where $f'$ is the predecessor function (the inverse of the successor function) on the positive naturals, but acts like the identity on the new element ω: *f*(*n* + 1) = *n*, *f*(*ω*) = *ω*. This set $\mathbf {N} \cup \{\omega \}$ that is the carrier of the final coalgebra of 1 + (−) is known as the set of conatural numbers.

For a second example, consider the same functor 1 + **N** × (−) as before. In this case the carrier of the final coalgebra consists of all lists of natural numbers, finite as well as infinite. The operations are a test function testing whether a list is empty, and a deconstruction function defined on non-empty lists returning a pair consisting of the head and the tail of the input list.

## Theorems

- Initial algebras are minimal (i.e., have no proper subalgebra).
- Final coalgebras are simple (i.e., have no proper quotients).

## Use in computer science

Various finite data structures used in programming, such as lists and trees, can be obtained as initial algebras of specific endofunctors. While there may be several initial algebras for a given endofunctor, they are unique up to isomorphism, which informally means that the "observable" properties of a data structure can be adequately captured by defining it as an initial algebra.

To obtain the type List(*A*) of lists whose elements are members of set A, consider that the list-forming operations are:

- $\mathrm {nil} \colon 1\to \mathrm {List} (A)$
- $\mathrm {cons} \colon A\times \mathrm {List} (A)\to \mathrm {List} (A)$

Combined into one function, they give:

- $[\mathrm {nil} ,\mathrm {cons} ]\colon (1+A\times \mathrm {List} (A))\to \mathrm {List} (A),$

which makes this an F-algebra for the endofunctor F sending X to 1 + (*A* × *X*). It is, in fact, *the* initial F-algebra. Initiality is established by the function known as *foldr* in functional programming languages such as Haskell and ML.

Likewise, binary trees with elements at the leaves can be obtained as the initial algebra

- $[\mathrm {tip} ,\mathrm {join} ]\colon A+(\mathrm {Tree} (A)\times \mathrm {Tree} (A))\to \mathrm {Tree} (A).$

Types obtained this way are known as algebraic data types.

Types defined by using least fixed point construct with functor F can be regarded as an initial F-algebra, provided that parametricity holds for the type.

In a dual way, similar relationship exists between notions of greatest fixed point and terminal F-coalgebra, with applications to coinductive types. These can be used for allowing potentially infinite objects while maintaining strong normalization property. In the strongly normalizing (each program terminates) Charity programming language, coinductive data types can be used for achieving surprising results, e.g. defining lookup constructs to implement such “strong” functions like the Ackermann function.
