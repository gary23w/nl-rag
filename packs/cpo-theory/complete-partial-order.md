---
title: "Complete partial order"
source: https://en.wikipedia.org/wiki/Complete_partial_order
domain: cpo-theory
license: CC-BY-SA-4.0
tags: complete partial order, directed-complete partial order, chain-complete poset, least upper bound
fetched: 2026-07-02
---

# Complete partial order

In mathematics, the phrase **complete partial order** is variously used to refer to at least three similar, but distinct, classes of partially ordered sets, characterized by particular completeness properties. Complete partial orders play a central role in theoretical computer science: in denotational semantics and domain theory.

## Definitions

The term **complete partial order**, abbreviated **cpo**, has several possible meanings depending on context.

A partially ordered set is a **directed-complete partial order** (**dcpo**) if each of its directed subsets has a supremum. (A subset of a partial order is directed if it is non-empty and every pair of elements has an upper bound in the subset.) In the literature, dcpos sometimes also appear under the label **up-complete poset**.

A **pointed directed-complete partial order** (**pointed dcpo**, sometimes abbreviated **cppo**), is a dcpo with a least element (usually denoted $\bot$ ). Formulated differently, a pointed dcpo has a supremum for every directed *or empty* subset. The term **chain-complete partial order** is also used, because of the characterization of pointed dcpos as posets in which every chain has a supremum.

A related notion is that of **ω-complete partial order** (**ω-cpo**). These are posets in which every ω-chain ( $x_{1}\leq x_{2}\leq x_{3}\leq ...$ ) has a supremum that belongs to the poset. The same notion can be extended to other cardinalities of chains.

Every dcpo is an ω-cpo, since every ω-chain is a directed set, but the converse is not true. However, every ω-cpo with a basis is also a dcpo (with the same basis). An ω-cpo (dcpo) with a basis is also called a **continuous** ω-cpo (or continuous dcpo).

Note that *complete partial order* is never used to mean a poset in which *all* subsets have suprema; the terminology complete lattice is used for this concept.

Requiring the existence of directed suprema can be motivated by viewing directed sets as generalized approximation sequences and suprema as *limits* of the respective (approximative) computations. This intuition, in the context of denotational semantics, was the motivation behind the development of domain theory.

The dual notion of a directed-complete partial order is called a **filtered-complete partial order**. However, this concept occurs far less frequently in practice, since one usually can work on the dual order explicitly.

By analogy with the Dedekind–MacNeille completion of a partially ordered set, every partially ordered set can be extended uniquely to a minimal dcpo.

## Examples

- Every finite poset is directed complete.
- All complete lattices are also directed complete.
- For any poset, the set of all non-empty filters, ordered by subset inclusion, is a dcpo. Together with the empty filter it is also pointed. If the order has binary meets, then this construction (including the empty filter) actually yields a complete lattice.
- Every set *S* can be turned into a pointed dcpo by adding a least element ⊥ and introducing a flat order with ⊥ ≤ *s* and s ≤ *s* for every *s* in *S* and no other order relations.
- The set of all partial functions on some given set *S* can be ordered by defining *f* ≤ *g* if and only if *g* extends *f*, i.e. if the domain of *f* is a subset of the domain of *g* and the values of *f* and *g* agree on all inputs for which they are both defined. (Equivalently, *f* ≤ *g* if and only if *f* ⊆ *g* where *f* and *g* are identified with their respective graphs.) This order is a pointed dcpo, where the least element is the nowhere-defined partial function (with empty domain). In fact, ≤ is also bounded complete. This example also demonstrates why it is not always natural to have a greatest element.
- The set of all linearly independent subsets of a vector space *V*, ordered by inclusion.
- The set of all partial choice functions on a collection of non-empty sets, ordered by restriction.
- The set of all prime ideals of a ring, ordered by inclusion.
- The specialization order of any sober space is a dcpo.
- Let us use the term "deductive system" as a set of sentences closed under consequence (for defining notion of consequence, let us use e.g. Alfred Tarski's algebraic approach). There are interesting theorems that concern a set of deductive systems being a directed-complete partial ordering. Also, a set of deductive systems can be chosen to have a least element in a natural way (so that it can be also a pointed dcpo), because the set of all consequences of the empty set (i.e. "the set of the logically provable/logically valid sentences") is (1) a deductive system (2) contained by all deductive systems.

## Characterizations

(Markowsky's theorem) An ordered set is a dcpo if and only if it is chain complete; i.e., every non-empty chain has a supremum.

As a corollary, an ordered set is a pointed dcpo if and only if every (possibly empty) chain has a supremum, i.e., if and only if it is chain-complete. Proofs rely on the axiom of choice.

Alternatively, an ordered set P is a pointed dcpo if and only if every order-preserving self-map of P has a least fixpoint.

## Continuous functions and fixed-points

A function *f* between two dcpos *P* and *Q* is called **(Scott) continuous** if it maps directed sets to directed sets while preserving their suprema:

- $f(D)\subseteq Q$ is directed for every directed $D\subseteq P$ .
- $f(\sup D)=\sup f(D)$ for every directed $D\subseteq P$ .

Note that every continuous function between dcpos is a monotone function. This notion of continuity is equivalent to the topological continuity induced by the Scott topology.

The set of all continuous functions between two dcpos *P* and *Q* is denoted [*P* → *Q*]. Equipped with the pointwise order, this is again a dcpo, and pointed whenever *Q* is pointed. Thus the complete partial orders with Scott-continuous maps form a cartesian closed category.

Every order-preserving self-map *f* of a pointed dcpo (*P*, ⊥) has a least fixed-point. If *f* is continuous then this fixed-point is equal to the supremum of the iterates (⊥, *f* (⊥), *f* (*f* (⊥)), ... *f* *n*(⊥), ...) of ⊥ (see also the Kleene fixed-point theorem).

Another fixed point theorem is the Bourbaki–Witt theorem, stating that if f is a function from a dcpo to itself with the property that $f(x)\geq x$ for all x , then f has a fixed point. This theorem, in turn, can be used to prove that Zorn's lemma is a consequence of the axiom of choice.
