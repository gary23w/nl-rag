---
title: "Dilworth's theorem"
source: https://en.wikipedia.org/wiki/Dilworth's_theorem
domain: extremal-combinatorics
license: CC-BY-SA-4.0
tags: extremal combinatorics, probabilistic method, dilworth's theorem, turan theorem
fetched: 2026-07-02
---

# Dilworth's theorem

In mathematics, in the areas of order theory and combinatorics, **Dilworth's theorem** states that, in any finite partially ordered set, the maximum size of an antichain of incomparable elements equals the minimum number of chains needed to cover all elements. This number is called the **width** of the partial order. The theorem is named for the mathematician Robert P. Dilworth, who published it in 1950.

A version of the theorem for infinite partially ordered sets states that, when there exists a decomposition into finitely many chains, or when there exists a finite upper bound on the size of an antichain, the sizes of the largest antichain and of the smallest chain decomposition are again equal.

## Statement

An antichain in a partially ordered set is a set of elements no two of which are comparable to each other, and a chain is a set of elements every two of which are comparable. A chain decomposition is a partition of the elements of the order into disjoint chains. Dilworth's theorem states that, in any finite partially ordered set, the largest antichain has the same size as the smallest chain decomposition. Here, the size of the antichain is its number of elements, and the size of the chain decomposition is its number of chains. The width of the partial order is defined as the common size of the antichain and chain decomposition.

## Inductive proof

The following proof by induction on the size of the partially ordered set P is based on that of Galvin (1994).

Let P be a finite partially ordered set. The theorem holds trivially if P is empty. So, assume that P has at least one element, and let a be a maximal element of P .

By induction, we assume that for some integer k the partially ordered set $P':=P\setminus \{a\}$ can be covered by k disjoint chains $C_{1},\dots ,C_{k}$ and has at least one antichain $A_{0}$ of size k . Clearly, $A_{0}\cap C_{i}\neq \emptyset$ for $i=1,2,\dots ,k$ . For $i=1,2,\dots ,k$ , let $x_{i}$ be the maximal element in $C_{i}$ that belongs to an antichain of size k in $P'$ , and set $A:=\{x_{1},x_{2},\dots ,x_{k}\}$ . We claim that A is an antichain. Let $A_{i}$ be an antichain of size k that contains $x_{i}$ . Fix arbitrary distinct indices i and j . Then $A_{i}\cap C_{j}\neq \emptyset$ . Let $y\in A_{i}\cap C_{j}$ . Then $y\leq x_{j}$ , by the definition of $x_{j}$ . This implies that $x_{i}\not \geq x_{j}$ , since $x_{i}\not \geq y$ . By interchanging the roles of i and j in this argument we also have $x_{j}\not \geq x_{i}$ . This verifies that A is an antichain.

We now return to P . Suppose first that $a\geq x_{i}$ for some $i\in \{1,2,\dots ,k\}$ . Let K be the chain $\{a\}\cup \{z\in C_{i}:z\leq x_{i}\}$ . Then by the choice of $x_{i}$ , $P\setminus K$ does not have an antichain of size k . Induction then implies that $P\setminus K$ can be covered by $k-1$ disjoint chains since $A\setminus \{x_{i}\}$ is an antichain of size $k-1$ in $P\setminus K$ . Thus, P can be covered by k disjoint chains, as required. Next, if $a\not \geq x_{i}$ for each $i\in \{1,2,\dots ,k\}$ , then $A\cup \{a\}$ is an antichain of size $k+1$ in P (since a is maximal in P ). Now P can be covered by the $k+1$ chains $\{a\},C_{1},C_{2},\dots ,C_{k}$ , completing the proof.

## Proof via Kőnig's theorem

Like a number of other results in combinatorics, Dilworth's theorem is equivalent to Kőnig's theorem on bipartite graph matching and several other related theorems including Hall's marriage theorem.

To prove Dilworth's theorem for a partial order *S* with *n* elements, using Kőnig's theorem, define a bipartite graph *G* = (*U*,*V*,*E*) where *U* = *V* = *S* and where (*u*,*v*) is an edge in *G* when *u* < *v* in *S*. By Kőnig's theorem, there exists a matching *M* in *G*, and a set of vertices *C* in *G*, such that each edge in the graph contains at least one vertex in *C* and such that *M* and *C* have the same cardinality *m*. Let *A* be the set of elements of *S* that do not correspond to any vertex in *C*; then *A* has at least *n* - *m* elements (possibly more if *C* contains vertices corresponding to the same element on both sides of the bipartition) and no two elements of *A* are comparable to each other. Let *P* be a family of chains formed by including *x* and *y* in the same chain whenever there is an edge (*x*,*y*) in *M*; then *P* has *n* - *m* chains. Therefore, we have constructed an antichain and a partition into chains with the same cardinality.

To prove Kőnig's theorem from Dilworth's theorem, for a bipartite graph *G* = (*U*,*V*,*E*), form a partial order on the vertices of *G* in which *u* < *v* exactly when *u* is in *U*, *v* is in *V*, and there exists an edge in *E* from *u* to *v*. By Dilworth's theorem, there exists an antichain *A* and a partition into chains *P* both of which have the same size. But the only nontrivial chains in the partial order are pairs of elements corresponding to the edges in the graph, so the nontrivial chains in *P* form a matching in the graph. The complement of *A* forms a vertex cover in *G* with the same cardinality as this matching.

This connection to bipartite matching allows the width of any partial order to be computed in polynomial time. More precisely, *n*-element partial orders of width *k* can be recognized in time *O*(*kn*2).

## Extension to infinite partially ordered sets

Dilworth's theorem for infinite partially ordered sets states that a partially ordered set has finite width *w* if and only if it may be partitioned into *w* chains. For, suppose that an infinite partial order *P* has width *w*, meaning that there are at most a finite number *w* of elements in any antichain. For any subset *S* of *P*, a decomposition into *w* chains (if it exists) may be described as a coloring of the incomparability graph of *S* (a graph that has the elements of *S* as vertices, with an edge between every two incomparable elements) using *w* colors; every color class in a proper coloring of the incomparability graph must be a chain. By the assumption that *P* has width *w*, and by the finite version of Dilworth's theorem, every finite subset *S* of *P* has a *w*-colorable incomparability graph. Therefore, by the De Bruijn–Erdős theorem, *P* itself also has a *w*-colorable incomparability graph, and thus has the desired partition into chains.

However, the theorem does not extend so simply to partially ordered sets in which the width, and not just the cardinality of the set, is infinite. In this case the size of the largest antichain and the minimum number of chains needed to cover the partial order may be very different from each other. In particular, for every infinite cardinal number κ there is an infinite partially ordered set of width ℵ0 whose partition into the fewest chains has κ chains.

Perles (1963) discusses analogues of Dilworth's theorem in the infinite setting.

## Dual of Dilworth's theorem (Mirsky's theorem)

A dual of Dilworth's theorem states that the size of the largest chain in a partial order (if finite) equals the smallest number of antichains into which the order may be partitioned. This is called Mirsky's theorem. Its proof is much simpler than the proof of Dilworth's theorem itself: for any element *x*, consider the chains that have *x* as their largest element, and let *N*(*x*) denote the size of the largest of these *x*-maximal chains. Then each set *N*−1(*i*), consisting of elements that have equal values of *N*, is an antichain, and these antichains partition the partial order into a number of antichains equal to the size of the largest chain.

## Perfection of comparability graphs

A comparability graph is an undirected graph formed from a partial order by creating a vertex per element of the order, and an edge connecting any two comparable elements. Thus, a clique in a comparability graph corresponds to a chain, and an independent set in a comparability graph corresponds to an antichain. Any induced subgraph of a comparability graph is itself a comparability graph, formed from the restriction of the partial order to a subset of its elements.

An undirected graph is perfect if, in every induced subgraph, the chromatic number equals the size of the largest clique. Every comparability graph is perfect: this is essentially just Mirsky's theorem, restated in graph-theoretic terms. By the perfect graph theorem of Lovász (1972), the complement of any perfect graph is also perfect. Therefore, the complement of any comparability graph is perfect; this is essentially just Dilworth's theorem itself, restated in graph-theoretic terms (Berge & Chvátal 1984). Thus, the complementation property of perfect graphs can provide an alternative proof of Dilworth's theorem.

## Width of special partial orders

The Boolean lattice *B**n* is the power set of an *n*-element set *X*—essentially {1, 2, …, *n*}—ordered by inclusion or, notationally, (2[*n*], ⊆). Sperner's theorem states that a maximum antichain of *B**n* has size at most

$\operatorname {width} (B_{n})={n \choose \lfloor {n/2}\rfloor }.$

In other words, a largest family of incomparable subsets of *X* is obtained by selecting the subsets of *X* that have median size. The Lubell–Yamamoto–Meshalkin inequality also concerns antichains in a power set and can be used to prove Sperner's theorem.

If we order the integers in the interval [1, 2*n*] by divisibility, the subinterval [*n* + 1, 2*n*] forms an antichain with cardinality *n*. A partition of this partial order into *n* chains is easy to achieve: for each odd integer *m* in [1,2*n*], form a chain of the numbers of the form *m*2*i*. Therefore, by Dilworth's theorem, the width of this partial order is *n*.

The Erdős–Szekeres theorem on monotone subsequences can be interpreted as an application of Dilworth's theorem to partial orders of order dimension two.

The "convex dimension" of an antimatroid is defined as the minimum number of chains needed to define the antimatroid, and Dilworth's theorem can be used to show that it equals the width of an associated partial order; this connection leads to a polynomial time algorithm for convex dimension.
