---
title: "Matroid intersection"
source: https://en.wikipedia.org/wiki/Matroid_intersection
domain: matroid-theory
license: CC-BY-SA-4.0
tags: matroid theory, oriented matroid, tutte polynomial, matroid intersection
fetched: 2026-07-02
---

# Matroid intersection

In combinatorial optimization, the **matroid intersection** problem is to find a largest common independent set in two matroids over the same ground set. If the elements of the matroid are assigned real weights, the **weighted matroid intersection** problem is to find a common independent set with the maximum possible weight. These problems generalize many problems in graph theory and combinatorial optimization including finding maximum matchings and maximum weight matchings in bipartite graphs and finding arborescences in directed graphs.

The **matroid intersection theorem**, due to Jack Edmonds, says that for any two matroids $M_{1}=(E,{\mathcal {I}}_{1})$ and $M_{2}=(E,{\mathcal {I}}_{2})$ we have

$\max _{I\in {\mathcal {I}}_{1}\cap {\mathcal {I}}_{2}}|I|=\min _{A\subseteq E}(r_{1}(A)+r_{2}(E\setminus A))$

where $r_{1}$ and $r_{2}$ are the respective rank functions of $M_{1}$ and $M_{2}$ . In other words, there is always a simple upper bound proof, consisting of a partitioning of the ground set amongst the two matroids, whose value (the sum of the respective ranks) equals the size of a maximum common independent set.

Based on this theorem, the matroid intersection problem for two matroids can be solved in polynomial time using matroid partitioning algorithms.

## Examples

Let *G* = (*U*,*V*;*E*) be a bipartite graph. One may define a partition matroid *MU* on the ground set *E*, in which a set of edges is independent if no two of the edges have the same endpoint in *U*. Similarly one may define a matroid *MV* in which a set of edges is independent if no two of the edges have the same endpoint in *V*. Any set of edges that is independent in both *MU* and *MV* has the property that no two of its edges share an endpoint; that is, it is a matching. Thus, the largest common independent set of *MU* and *MV* is a maximum matching in *G*.

Similarly, if each edge has a weight, then the maximum-weight independent set of *MU* and *MV* is a Maximum weight matching in *G*.

## Algorithms

There are several polynomial-time algorithms for weighted matroid intersection, with different run-times. The run-times are given in terms of n - the number of elements in the common base-set, r - the maximum between the ranks of the two matroids, T - the number of operations required for a circuit-finding oracle, and k - the number of elements in the intersection (in case we want to find an intersection of a specific size k ).

- Edmonds' algorithm uses linear programming and polyhedra.
- Lawler's algorithm.
- Iri and Tomizawa's algorithm
- Andras Frank's algorithm uses $O(n^{3}T)$ arithmetic operations.
- Orlin and Vande-Vate's algorithm.
- Cunningham's algorithm requires $O(r^{1.5}nT)$ operations on general matroids, and $O(nr^{2}\log {r})$ operations on linear matroid, for two *r*-by-*n* matrices.
- Brezovec, Cornuejos and Glover present two algorithms for weighted matroid intersection.
  - The first algorithm requires that all weights be integers, and finds an intersection of cardinality k in time $O((n^{3}k^{2}+nkT)\cdot (1+\log {W}))$ .
  - The second algorithm runs in time $O(nr\cdot (\log {n}+r+T))$ .
- Huang, Kakimura and Kamiyama show that the weighted matroid intersection problem can be solved by solving *W* instances of the unweighted matroid intersection problem, where *W* is the largest given weight, assuming that all given weights are integral. This algorithm is faster than previous algorithms when *W* is small. They also present an approximation algorithm that finds an *e*-approximate solution by solving $O(\epsilon ^{-1}\log {r})$ instances of the unweighted matroid intersection problem, where *r* is the smaller rank of the two input matroids.
- Ghosh, Gurjar and Raj study the run-time complexity of matroid intersection in the parallel computing model.
- Bérczi, Király, Yamaguchi and Yokoi present strongly polynomial-time algorithms for weighted matroid intersection using more restricted oracles.

## Extensions

### Maximizing weight subject to cardinality

In a variant of weighted matroid intersection, called "(Pk)", the goal is to find a common independent set with the maximum possible weight among all such sets with cardinality *k*, if such a set exists. This variant, too, can be solved in polynomial time.

### Three matroids

The matroid intersection problem becomes NP-hard when three matroids are involved, instead of only two.

One proof of this hardness result uses a reduction from the Hamiltonian path problem in directed graphs. Given a directed graph *G* with *n* vertices, and specified nodes *s* and *t*, the Hamiltonian path problem is the problem of determining whether there exists a simple path of length *n* − 1 that starts at *s* and ends at *t*. It may be assumed without loss of generality that *s* has no incoming edges and *t* has no outgoing edges. Then, a Hamiltonian path exists if and only if there is a set of *n* − 1 elements in the intersection of three matroids on the edge set of the graph: two partition matroids ensuring that the in-degree and out-degree of the selected edge set are both at most one, and the graphic matroid of the undirected graph formed by forgetting the edge orientations in *G*, ensuring that the selected edge set has no cycles.

### Matroid parity

Another computational problem on matroids, the matroid parity problem, was formulated by Lawler as a common generalization of matroid intersection and non-bipartite graph matching. However, although it can be solved in polynomial time for linear matroids, it is NP-hard for other matroids, and requires exponential time in the matroid oracle model.

### Valuated matroids

A **valuated matroid** is a matroid equipped with a value function *v* on the set of its bases, with the following *exchange property*: for any two distinct bases A and B , if $a\in A\setminus B$ , then there exists an element $b\in B\setminus A$ such that both $(A\setminus \{a\})\cup \{b\}$ and $(B\setminus \{b\})\cup \{a\}$ are bases, and : $v(A)+v(B)\leq v(B\setminus \{b\}\cup \{a\})+v(A\setminus \{a\}\cup \{b\})$ .

Given a weighted bipartite graph *G* = (*X*+*Y*, *E*) and two valuated matroids, one on *X* with bases set *BX* and valuation *vX*, and one on *Y* with bases *BY* and valuation *vY*, the **valuated independent assignment problem** is the problem of finding a matching *M* in *G*, such that *MX* (the subset of *X* matched by *M*) is a base in *BX*, *MY* is a base in *BY*, and subject to this, the sum $w(M)+v_{X}(M_{X})+v_{Y}(M_{Y})$ is maximized. The weighted matroid intersection problem is a special case in which the matroid valuations are constant, so we only seek to maximize $w(M)$ subject to *MX* is a base in *BX* and *MY* is a base in *BY* *.* Murota presents a polynomial-time algorithm for this problem.
