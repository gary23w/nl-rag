---
title: "Perfect matching"
source: https://en.wikipedia.org/wiki/Perfect_matching
domain: blossom-edmonds-contraction
license: CC-BY-SA-4.0
tags: blossom algorithm, edmonds matching, general graph matching, odd cycle contraction
fetched: 2026-07-02
---

# Perfect matching

In graph theory, a **perfect matching** in a graph is a matching that covers every vertex of the graph. More formally, given a graph G with edges E and vertices V, a perfect matching in G is a subset M of E, such that every vertex in V is adjacent to exactly one edge in M. The adjacency matrix of a perfect matching is a symmetric permutation matrix.

A perfect matching is also called a **1-factor**; see Graph factorization for an explanation of this term. In some literature, the term **complete matching** is used.

Every perfect matching is a maximum-cardinality matching, but the opposite is not true. For example, consider the following graphs:

In graph (b) there is a perfect matching (of size 3) since all 6 vertices are matched; in graphs (a) and (c) there is a maximum-cardinality matching (of size 2) which is not perfect, since some vertices are unmatched.

A perfect matching is also a minimum-size edge cover. If there is a perfect matching, then both the matching number and the edge cover number equal |*V*| / 2.

A perfect matching can only occur when the graph has an even number of vertices. A **near-perfect matching** is one in which exactly one vertex is unmatched. This can only occur when the graph has an odd number of vertices, and such a matching must be maximum. In the above figure, part (c) shows a near-perfect matching. If, for every vertex in a graph, there is a near-perfect matching that omits only that vertex, the graph is also called factor-critical.

## Characterizations

Hall's marriage theorem provides a characterization of bipartite graphs which have a perfect matching.

Tutte's theorem on perfect matchings provides a characterization for arbitrary graphs.

A perfect matching is a spanning 1-regular subgraph, a.k.a. a 1-factor. In general, a spanning *k*-regular subgraph is a *k*-factor.

A spectral characterization for a graph to have a perfect matching is given by Hassani Monfared and Mallik as follows: Let G be a graph on even n vertices and $\lambda _{1}>\lambda _{2}>\ldots >\lambda _{\frac {n}{2}}>0$ be ${\frac {n}{2}}$ distinct nonzero purely imaginary numbers. Then G has a perfect matching if and only if there is a real skew-symmetric matrix A with graph G and eigenvalues $\pm \lambda _{1},\pm \lambda _{2},\ldots ,\pm \lambda _{\frac {n}{2}}$ . Note that the (simple) graph of a real symmetric or skew-symmetric matrix A of order n has n vertices and edges given by the nonzero off-diagonal entries of A .

## Computation

Deciding whether a graph admits a perfect matching can be done in polynomial time, using any algorithm for finding a maximum cardinality matching.

However, counting the number of perfect matchings, even in bipartite graphs, is #P-complete. This is because computing the permanent of an arbitrary 0–1 matrix (another #P-complete problem) is the same as computing the number of perfect matchings in the bipartite graph having the given matrix as its biadjacency matrix.

A theorem of Pieter Kasteleyn states that the number of perfect matchings in a planar graph can be computed exactly in polynomial time via the FKT algorithm.

The number of perfect matchings in a complete graph *Kn* (with *n* even) is given by the double factorial: $(n-1)!!$

## Connection to Graph Coloring

An edge-colored graph can induce a number of (not necessarily proper) vertex colorings equal to the number of perfect matchings, as every vertex is covered exactly once in each matching. This property has been investigated in quantum physics and computational complexity theory.

## Perfect matching polytope

The **perfect matching polytope** of a graph is a polytope in **R**|E| in which each corner is an incidence vector of a perfect matching.
