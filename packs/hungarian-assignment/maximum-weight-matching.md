---
title: "Maximum-weight matching"
source: https://en.wikipedia.org/wiki/Maximum-weight_matching
domain: hungarian-assignment
license: CC-BY-SA-4.0
tags: hungarian algorithm, assignment problem, kuhn munkres method, cost matrix
fetched: 2026-07-02
---

# Maximum-weight matching

**Maximum-weight matching** is an optimization problem in graph theory in which the goal is to find a matching of maximum possible total weight in an edge-weighted graph. A matching is an independent edge set (that is, a set of edges in which none of the members share a common endpoint). The **weight** of a matching is the sum of the weights on its edges.

The problem is a generalization of the maximum cardinality matching problem because it allows edges to carry arbitrary numerical weights. When all edge weights are equal, a maximum-weight matching is equivalent to a maximum cardinality matching.

The maximum-weight matching problem is solvable in polynomial time using, for example, the $O(EV^{2})$ blossom algorithm, or Gabow's $O(V^{3})$ algorithm. This contrasts with the problem of computing the (weighted) maximum independent set of vertices in a graph, which is NP-hard.

By adjusting the given edge weights, algorithms for the maximum-weight matching problem can also be used to solve the **maximum cardinality** maximum-weight matching problem, where the objective is to find, among all matchings with maximum cardinality, one whose total weight is maximised. Similar ideas can also be used to solve the maximum cardinality **minimum** weight matching problem. In cases where the edge-weighted graph is bipartite, such problems are also known as the assignment problem.

## Definition

Given an undirected graph $G=(V,E,w)$ with vertex set V , edge set E , and weight function $w:E\to \mathbb {R}$ , a maximum-weight matching is an independent set of edges $M\subseteq E$ that maximises the total weight

$w(M)=\sum _{e\in M}w(e).$

The edge weights may be positive, negative, or mixed.

## Maximum cardinality weighted matchings

A commonly occurring variant of the problem involves computing a matching that contains as many edges as possible. The total weight of the matching is then used as a secondary measure.

To solve the **maximum-cardinality maximum-weight** matching problem on $G=(V,E,w)$ , a new graph $G'=(V,E,w')$ is formed in which, for each edge $e\in E$ ,

$w'(e)=C+w(e),$

where C is an appropriate positive constant. A maximum-weight matching in $G'$ then corresponds to a maximum cardinality maximum-weight matching in G .

To solve the maximum cardinality **minimum** weight matching problem, set

$w'(e)=C-w(e).$

Again, a maximum-weight matching on $G'$ yields a maximum cardinality minimum weight matching in G .

In both cases, a constant C is needed to force the algorithm to favor matchings with greater cardinality regardless of the edge weights in G . Any value of

$C>2\sum _{e\in E}|w(e)|$

is sufficient for this purpose.

## Algorithms and implementations

The maximum-weight matching problem is solvable in polynomial time. Well-known algorithms include:

- The $O(EV^{2})$ blossom algorithm, introduced by Jack Edmonds in 1965 and later extended for weighted matchings. Its complexity was also later improved to $O(EV+V^{2}\log V)$ .
- The $O(V^{3})$ algorithm of Harold Gabow, which makes use of priority queues and tree structures.
- The $O(V^{3})$ Hungarian algorithm, which solves the maximum cardinality maximum-weight matching problem in bipartite graphs only.

Other algorithms are reviewed by Duan and Pettie. Their work also proposes an approximation algorithm for general graphs that runs in linear time for any fixed error bound.

Efficient implementations are available in several software libraries, including NetworkX, LEDA, and the LEMON graph library.

## Applications

Maximum-weight matchings (and their maximum cardinality variants) arise in a wide range of optimization settings.

- Maximum cardinality minimum cost matchings are used in the approximation algorithm of Christofides for the traveling salesman problem. In problem instances where the edge weights form a metric space, this algorithm guarantees solution costs that are no more than 50% worse than the optimal cost.
- Problems that involve assigning resources to entities can be modelled as maximum-weight matching problems on bipartite graphs, with edge weights reflecting the desirability of particular assignments. Examples include assigning workers to tasks, blood samples to patients, taxis to waiting customers, and sellers to buyers.
- Maximum cardinality minimum cost matchings are used for solving several types of packing problem; particularly those that require optimal sequences of items to be identified.
- In bioinformatics, the maximum-weight matching problem is used in analysing protein–protein interaction. Here, protein interactions within an organism are modelled as an edge-weighted graph, with vertices representing individual proteins and edge weights representing the confidence of their interactions being biologically relevant. The goal is to identify densely connected subgraphs within the graph, as these are likely to correspond to stable protein complexes that function as a unit within cells.
- Maximum cardinality minimum cost matchings are used when solving the Chinese postman problem, which involves finding a minimum weight walk that visits every edge of an edge-weighted graph at least once.
