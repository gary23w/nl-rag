---
title: "Scott domain"
source: https://en.wikipedia.org/wiki/Scott_domain
domain: denotational-semantics
license: CC-BY-SA-4.0
tags: denotational semantics, domain theory, scott domain, semantic domain
fetched: 2026-07-02
---

# Scott domain

In the mathematical fields of order and domain theory, a **Scott domain** is an algebraic, bounded-complete and directed-complete partial order (dcpo). They are named in honour of Dana S. Scott, who was the first to study these structures at the advent of domain theory. Scott domains are very closely related to algebraic lattices, being different only in possibly lacking a greatest element. They are also closely related to Scott information systems, which constitute a "syntactic" representation of Scott domains.

While the term "Scott domain" is widely used with the above definition, the term "domain" does not have such a generally accepted meaning and different authors will use different definitions; Scott himself used "domain" for the structures now called "Scott domains". Additionally, Scott domains appear with other names like "algebraic semilattice" in some publications.

Originally, Dana Scott demanded a complete lattice, and the Russian mathematician Yuri Yershov constructed the isomorphic structure of a directed-complete partial order (dcpo). But this was not recognized until after scientific communications improved after the fall of the Iron Curtain. In honour of their work, a number of mathematical papers now dub this fundamental construction a "Scott–Ershov" domain.

## Definition

Formally, a non-empty partially ordered set $(D,\leq )$ is called a *Scott domain* if the following hold:

- D is directed-complete, i.e. all directed subsets of D have a supremum.
- D is bounded-complete, i.e. all subsets of D that have some upper bound have a supremum.
- D is algebraic, i.e. every element of D can be obtained as the supremum of a directed set of compact elements of D.

## Properties

Since the empty set certainly has some upper bound, we can conclude the existence of a least element $\bot$ (the supremum of the empty set) from bounded completeness.

The property of being bounded-complete is equivalent to the existence of infima of all *non-empty* subsets of D. It is well known that the existence of *all* infima implies the existence of all suprema and thus makes a partially ordered set into a complete lattice. Thus, when a top element (the infimum of the empty set) is adjoined to a Scott domain, one can conclude that:

1. the new top element is compact (since the order was directed complete before) and
2. the resulting poset will be an algebraic lattice (i.e. a complete lattice that is algebraic).

Consequently, Scott domains are in a sense "almost" algebraic lattices. However, removing the top element from a complete lattice does not always produce a Scott domain. (Consider the complete lattice ${\mathcal {P}}(\mathbb {N} )$ . The finite subsets of $\mathbb {N}$ form a directed set, but have no upper bound in ${\mathcal {P}}(\mathbb {N} )\setminus \{\mathbb {N} \}$ .)

Scott domains become topological spaces by introducing the Scott topology.

## Explanation

Scott domains are intended to represent *partial algebraic data*, ordered by information content. An element $x\in D$ is a piece of data that might not be fully defined. The statement $x\leq y$ means " y contains all the information that x does". The bottom element is the element containing no information at all. Compact elements are the elements representing a finite amount of information.

With this interpretation we can see that the supremum $\bigvee X$ of a subset $X\subseteq D$ is the element that contains all the information that *any* element of X contains, but *no more*. Obviously such a supremum only exists (i.e., makes sense) provided X does not contain inconsistent information; hence the domain is directed and bounded complete, but not *all* suprema necessarily exist. The algebraicity axiom essentially ensures that all elements get all their information from (non-strictly) lower down in the ordering; in particular, the jump from compact or "finite" to non-compact or "infinite" elements does not covertly introduce any extra information that cannot be reached at some finite stage.

On the other hand, the infimum $\bigwedge X$ is the element that contains all the information that is shared by *all* elements of X , and *no less*. If X contains no consistent information, then its elements have no information in common and so its infimum is $\bot$ . In this way all non-empty infima exist, but not all infima are necessarily interesting.

This definition in terms of partial data allows an algebra to be defined as the limit of a sequence of increasingly more defined partial algebras—in other words a fixed point of an operator that adds progressively more information to the algebra. For more information, see Domain theory.

## Examples

- Every finite poset is directed-complete and algebraic (though not necessarily bounded-complete). Thus any bounded-complete finite poset is a Scott domain.
- The natural numbers with an additional top element ω constitute an algebraic lattice, hence a Scott domain. For more examples in this direction, see the article on algebraic lattices.
- Consider the set of all finite and infinite words over the alphabet {0,1}, ordered by the prefix order on words. Thus, a word w is smaller than some word v if w is a prefix of v, i.e. if there is some (finite or infinite) word v' such that $wv'=v$ . For example, $101\leq 10110$ . The empty word is the bottom element of this ordering, and every directed set (which is always a chain) is easily seen to have a supremum. Likewise, one immediately verifies bounded completeness. However, the resulting poset is certainly missing a top having many maximal elements instead (namely all the infinite words). It is also algebraic, since every finite word happens to be compact and we certainly can approximate infinite words by chains of finite ones. Thus this is a Scott domain that is not an algebraic lattice.
- For a negative example, consider the real numbers in the unit interval [0,1], ordered by their natural order. This bounded-complete dcpo is not algebraic. In fact its only compact element is 0.
