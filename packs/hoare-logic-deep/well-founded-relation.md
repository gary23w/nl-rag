---
title: "Well-founded relation"
source: https://en.wikipedia.org/wiki/Well-founded_relation
domain: hoare-logic-deep
license: CC-BY-SA-4.0
tags: Hoare logic, Hoare triple, partial correctness, total correctness
fetched: 2026-07-02
---

# Well-founded relation

| Transitive binary relations |
|---|
| Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Total, Semiconnex Anti- reflexive Equivalence relation (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Preorder (Quasiorder) ✗ ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total preorder ✗ ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Prewellordering ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-quasi-ordering ✗ ✗ ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-ordering ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Lattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ Join-semilattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ (Green tick)Y ✗ ✗ Meet-semilattice ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ Strict partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict weak order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Definitions, for all $a,b$ and $S\neq \varnothing :$ ${\begin{aligned}&aRb\\\Rightarrow {}&bRa\end{aligned}}$ ${\begin{aligned}aRb{\text{ and }}&bRa\\\Rightarrow a={}&b\end{aligned}}$ ${\begin{aligned}a\neq {}&b\Rightarrow \\aRb{\text{ or }}&bRa\end{aligned}}$ ${\begin{aligned}\min S\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\vee b\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\wedge b\\{\text{exists}}\end{aligned}}$ $aRa$ ${\text{not }}aRa$ ${\begin{aligned}aRb\Rightarrow \\{\text{not }}bRa\end{aligned}}$ |
| (Green tick)Y indicates that the column's property is always true for the row's term (at the very left), while ✗ indicates that the property is not guaranteed in general (it might, or might not, hold). For example, that every equivalence relation is symmetric, but not necessarily antisymmetric, is indicated by (Green tick)Y in the "Symmetric" column and ✗ in the "Antisymmetric" column, respectively. All definitions tacitly require the homogeneous relation R be transitive: for all $a,b,c,$ if $aRb$ and $bRc$ then $aRc.$ A term's definition may require additional properties that are not listed in this table. |

In mathematics, a binary relation R is called **well-founded** (or **wellfounded** or **foundational**) on a set or, more generally, a class X if every non-empty subset (or subclass) *S* ⊆ *X* has a minimal element with respect to R; that is, there exists an *m* ∈ *S* such that for every *s* ∈ *S*, one does not have *s* *R* *m*. More formally, a relation is well-founded if: $(\forall S\subseteq X)\;[S\neq \varnothing \implies (\exists m\in S)(\forall s\in S)\lnot (s\mathrel {R} m)].$ Some authors include an extra condition that R is set-like, i.e., that the elements less than any given element form a set.

Equivalently, assuming the axiom of dependent choice, a relation is well-founded when it contains no infinite descending chains, meaning there is no infinite sequence *x*0, *x*1, *x*2, ... of elements of X such that *x**n*+1 *R* *x**n* for every natural number n.

In order theory, a partial order is called well-founded if the corresponding strict order is a well-founded relation. If the order is a total order, then it is called a well-order.

In set theory, a set x is called a **well-founded set** if the set membership relation is well-founded on the transitive closure of x. The axiom of regularity, which is one of the axioms of Zermelo–Fraenkel set theory, asserts that all sets are well-founded.

A relation R is **converse well-founded**, **upwards well-founded**, or **Noetherian** on X, if the converse relation *R*−1 is well-founded on X. In this case R is also said to satisfy the ascending chain condition. In the context of rewriting systems, a Noetherian relation is also called **terminating**.

## Induction and recursion

An important reason that well-founded relations are interesting is because a version of transfinite induction can be used on them: if (*X*, *R*) is a well-founded relation, *P*(*x*) is some property of elements of X, and we want to show that

P

(

x

)

holds for all elements

x

of

X

,

it suffices to show that:

If

x

is an element of

X

and

P

(

y

)

is true for all

y

such that

y

R

x

, then

P

(

x

)

must also be true.

That is, $(\forall x\in X)\;[(\forall y\in X)\;[y\mathrel {R} x\implies P(y)]\implies P(x)]\quad {\text{implies}}\quad (\forall x\in X)\,P(x).$

Well-founded induction is sometimes called Noetherian induction, after Emmy Noether.

On par with induction, well-founded relations also support construction of objects by transfinite recursion. Let (*X*, *R*) be a set-like well-founded relation and F a function that assigns an object *F*(*x*, *g*) to each pair of an element *x* ∈ *X* and a function g on the set {*y*: *y* *R* *x*} of predecessors of x. Then there is a unique function G such that for every *x* ∈ *X*, $G(x)=F\left(x,G\vert _{\left\{y:\,y\mathrel {R} x\right\}}\right).$

That is, if we want to construct a function G on X, we may define *G*(*x*) using the values of *G*(*y*) for *y* *R* *x*.

As an example, consider the well-founded relation (**N**, *S*), where **N** is the set of all natural numbers, and S is the graph of the successor function *x* ↦ *x*+1. Then induction on S is the usual mathematical induction, and recursion on S gives primitive recursion. If we consider the order relation (**N**, <), we obtain complete induction, and course-of-values recursion. The statement that (**N**, <) is well-founded is also known as the well-ordering principle.

There are other interesting special cases of well-founded induction. When the well-founded relation is the usual ordering on the class of all ordinal numbers, the technique is called transfinite induction. When the well-founded set is a set of recursively defined data structures, the technique is called structural induction. When the well-founded relation is set membership on the universal class, the technique is known as ∈-induction. See those articles for more details.

## Examples

Well-founded relations that are not totally ordered include:

- The positive integers {1, 2, 3, ...}, with the order defined by *a* < *b* if and only if a divides b and *a* ≠ *b*.
- The set of all finite strings over a fixed alphabet, with the order defined by *s* < *t* if and only if s is a proper substring of t.
- The set **N** × **N** of pairs of natural numbers, ordered by (*n*1, *n*2) < (*m*1, *m*2) if and only if *n*1 < *m*1 and *n*2 < *m*2.
- Every class whose elements are sets, with the relation ∈ ("is an element of"). This is the axiom of regularity.
- The nodes of any finite directed acyclic graph, with the relation R defined such that *a* *R* *b* if and only if there is an edge from a to b.

Examples of relations that are not well-founded include:

- The negative integers {−1, −2, −3, ...}, with the usual order, since any unbounded subset has no least element.
- The set of strings over a finite alphabet with more than one element, under the usual (lexicographic) order, since the sequence "B" > "AB" > "AAB" > "AAAB" > ... is an infinite descending chain. This relation fails to be well-founded even though the entire set has a minimum element, namely the empty string.
- The set of non-negative rational numbers (or reals) under the standard ordering, since, for example, the subset of positive rationals (or reals) lacks a minimum.

## Other properties

If (*X*, <) is a well-founded relation and x is an element of X, then the descending chains starting at x are all finite, but this does not mean that their lengths are necessarily bounded. Consider the following example: Let X be the union of the positive integers with a new element ω that is bigger than any integer. Then X is a well-founded set, but there are descending chains starting at ω of arbitrary great (finite) length; the chain ω, *n* − 1, *n* − 2, ..., 2, 1 has length n for any n.

The Mostowski collapse lemma implies that set membership is a universal among the extensional well-founded relations: for any set-like well-founded relation R on a class X that is extensional, there exists a class C such that (*X*, *R*) is isomorphic to (*C*, ∈).

## Reflexivity

A relation R is said to be reflexive if *a* *R* *a* holds for every a in the domain of the relation. Every reflexive relation on a nonempty domain has infinite descending chains, because any constant sequence is a descending chain. For example, in the natural numbers with their usual order ≤, we have 1 ≥ 1 ≥ 1 ≥ .... To avoid these trivial descending sequences, when working with a partial order ≤, it is common to apply the definition of well foundedness (perhaps implicitly) to the alternate relation < defined such that *a* < *b* if and only if *a* ≤ *b* and *a* ≠ *b*. More generally, when working with a preorder ≤, it is common to use the relation < defined such that *a* < *b* if and only if *a* ≤ *b* and *b* ≰ *a*. In the context of the natural numbers, this means that the relation <, which is well-founded, is used instead of the relation ≤, which is not. In some texts, the definition of a well-founded relation is changed from the definition above to include these conventions.
