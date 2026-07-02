---
title: "Ideal (order theory)"
source: https://en.wikipedia.org/wiki/Ideal_(order_theory)
domain: denotational-domains
license: CC-BY-SA-4.0
tags: domain theory, directed-complete partial order, continuous function, algebraic lattice
fetched: 2026-07-02
---

# Ideal (order theory)

In mathematical order theory, an **ideal** is a special subset of a partially ordered set (poset). Although this term historically was derived from the notion of a ring ideal of abstract algebra, it has subsequently been generalized to a different notion. Ideals are of great importance for many constructions in order and lattice theory.

## Definitions

A subset I of a partially ordered set $(P,\leq )$ is an **ideal**, if the following conditions hold:

1. I is non-empty,
2. for every *x* in I and *y* in *P*, *y* ≤ *x* implies that *y* is in I  (I is a lower set),
3. for every *x*, *y* in I, there is some element *z* in I, such that *x* ≤ *z* and *y* ≤ *z*  (I is a directed set).

While this is the most general way to define an ideal for arbitrary posets, it was originally defined for lattices only. In this case, the following equivalent definition can be given: a subset I of a lattice $(P,\leq )$ is an ideal if and only if it is a lower set that is closed under finite joins (suprema); that is, it is nonempty and for all *x*, *y* in I, the element $x\vee y$ of *P* is also in I.

A weaker notion of **order ideal** is defined to be a subset of a poset P that satisfies the above conditions 1 and 2. In other words, an order ideal is simply a lower set. Similarly, an ideal can also be defined as a "directed lower set".

The dual notion of an ideal, i.e., the concept obtained by reversing all ≤ and exchanging $\vee$ with $\wedge ,$ is a filter.

Frink ideals, pseudoideals and Doyle pseudoideals are different generalizations of the notion of a lattice ideal.

An ideal or filter is said to be **proper** if it is not equal to the whole set *P*.

The smallest ideal that contains a given element *p* is a *principal ideal* and *p* is said to be a *principal element* of the ideal in this situation. The principal ideal $\downarrow p$ for a principal *p* is thus given by ↓ *p* = {*x* ∈ *P* | *x* ≤ *p*}.

## Terminology confusion

The above definitions of "ideal" and "order ideal" are the standard ones, but there is some confusion in terminology. Sometimes the words and definitions such as "ideal", "order ideal", "Frink ideal", or "partial order ideal" mean one another.

## Prime ideals

An important special case of an ideal is constituted by those ideals whose set-theoretic complements are filters, i.e. ideals in the inverse order. Such ideals are called **prime ideals**. Also note that, since we require ideals and filters to be non-empty, every prime ideal is necessarily proper. For lattices, prime ideals can be characterized as follows:

A subset I of a lattice $(P,\leq )$ is a prime ideal, if and only if

1. I is a proper ideal of *P*, and
2. for all elements *x* and *y* of *P*, $x\wedge y$ in I implies that *x* ∈ *I* or *y* ∈ *I*.

It is easily checked that this is indeed equivalent to stating that $P\setminus I$ is a filter (which is then also prime, in the dual sense).

For a complete lattice the further notion of a **completely prime ideal** is meaningful. It is defined to be a proper ideal I with the additional property that, whenever the meet (infimum) of some arbitrary set *A* is in *I*, some element of *A* is also in I. So this is just a specific prime ideal that extends the above conditions to infinite meets.

The existence of prime ideals is in general not obvious, and often a satisfactory amount of prime ideals cannot be derived within ZF (Zermelo–Fraenkel set theory without the axiom of choice). This issue is discussed in various prime ideal theorems, which are necessary for many applications that require prime ideals.

## Maximal ideals

An ideal I is a *maximal ideal* if it is proper and there is no *proper* ideal *J* that is a strict superset of I. Likewise, a filter *F* is maximal if it is proper and there is no proper filter that is a strict superset.

When a poset is a distributive lattice, maximal ideals and filters are necessarily prime, while the converse of this statement is false in general.

Maximal filters are sometimes called ultrafilters, but this terminology is often reserved for Boolean algebras, where a maximal filter (ideal) is a filter (ideal) that contains exactly one of the elements {*a*, ¬*a*}, for each element *a* of the Boolean algebra. In Boolean algebras, the terms *prime ideal* and *maximal ideal* coincide, as do the terms *prime filter* and *maximal filter*.

There is another interesting notion of maximality of ideals: Consider an ideal I and a filter *F* such that I is disjoint from *F*. We are interested in an ideal *M* that is maximal among all ideals that contain I and are disjoint from *F*. In the case of distributive lattices such an *M* is always a prime ideal. A proof of this statement follows.

Proof

Assume the ideal *M* is maximal with respect to disjointness from the filter *F*. Suppose for a contradiction that *M* is not prime, i.e. there exists a pair of elements *a* and *b* such that *a* ∧ *b* in *M* but neither *a* nor *b* are in *M*. Consider the case that for all *m* in *M*, *m* ∨ *a* is not in *F*. One can construct an ideal *N* by taking the downward closure of the set of all binary joins of this form, i.e. *N* = { *x* | *x* ≤ *m* ∨ *a* for some *m* ∈ *M*}. It is readily checked that *N* is indeed an ideal disjoint from *F* which is strictly greater than *M*. But this contradicts the maximality of *M* and thus the assumption that *M* is not prime.

For the other case, assume that there is some *m* in *M* with *m* ∨ *a* in *F*. Now if any element *n* in *M* is such that *n* ∨ *b* is in *F*, one finds that (*m* ∨ *n*) ∨ *b* and (*m* ∨ *n*) ∨ *a* are both in *F*. But then their meet is in *F* and, by distributivity, (*m* ∨ *n*) ∨ (*a* ∧ *b*) is in *F* too. On the other hand, this finite join of elements of *M* is clearly in *M*, such that the assumed existence of *n* contradicts the disjointness of the two sets. Hence all elements *n* of *M* have a join with *b* that is not in *F*. Consequently one can apply the above construction with *b* in place of *a* to obtain an ideal that is strictly greater than *M* while being disjoint from *F*. This finishes the proof.

However, in general it is not clear whether there exists any ideal *M* that is maximal in this sense. Yet, if we assume the axiom of choice in our set theory, then the existence of *M* for every disjoint filter–ideal-pair can be shown. In the special case that the considered order is a Boolean algebra, this theorem is called the Boolean prime ideal theorem. It is strictly weaker than the axiom of choice and it turns out that nothing more is needed for many order-theoretic applications of ideals.

## Applications

The construction of ideals and filters is an important tool in many applications of order theory.

- In Stone's representation theorem for Boolean algebras, the maximal ideals (or, equivalently via the negation map, ultrafilters) are used to obtain the set of points of a topological space, whose clopen sets are isomorphic to the original Boolean algebra.
- Order theory knows many completion procedures to turn posets into posets with additional completeness properties. For example, the ideal completion of a given partial order *P* is the set of all ideals of *P* ordered by subset inclusion. This construction yields the free dcpo generated by *P*. An ideal is principal if and only if it is compact in the ideal completion, so the original poset can be recovered as the sub-poset consisting of compact elements. Furthermore, every algebraic dcpo can be reconstructed as the ideal completion of its set of compact elements.

## History

Ideals were introduced by Marshall H. Stone first for Boolean algebras, where the name was derived from the ring ideals of abstract algebra. He adopted this terminology because, using the isomorphism of the categories of Boolean algebras and of Boolean rings, the two notions do indeed coincide.

Generalization to any posets was done by Frink.
