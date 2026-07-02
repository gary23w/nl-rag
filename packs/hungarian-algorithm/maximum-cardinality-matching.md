---
title: "Maximum-cardinality matching"
source: https://en.wikipedia.org/wiki/Maximum_cardinality_matching
domain: hungarian-algorithm
license: CC-BY-SA-4.0
tags: hungarian algorithm, assignment problem, bipartite matching, combinatorial optimization
fetched: 2026-07-02
---

# Maximum-cardinality matching

(Redirected from

Maximum cardinality matching

)

In graph theory, a **maximum-cardinality matching** is a special kind of subgraph useful in many computational contexts. Given a graph G, a matching is a subgraph where no two edges share a vertex. The cardinality of the matching is the number of edges in the subgraph, and the maximum cardinality is the largest number of edges a matching can contain. A matching for a given graph is a **maximum-cardinality matching** if its cardinality is this maximum cardinality. If we think of each edge as "covering" the vertices it connects exactly once, then a maximal matching is also the largest non-overlapping cover of the graph. If all the vertices are covered, we call it a perfect matching. For finite graphs, a maximum-cardinality matching always exists, but is not usually unique. The cardinality of the matching is never more than half the number of vertices and also never more than the number of edges.

An important special case of the maximum-cardinality matching problem is when G is a bipartite graph representing a binary relation, whose vertices V are partitioned between left vertices in X and right vertices in Y, and edges in E always connect a left vertex to a right vertex. In this case, the problem can be efficiently solved with simpler algorithms than in the general case.

The calculation of a **maximum matching** for a given graph is a fundamental task in computational graph theory. There are nonconstructive characterization theorems for the size of a maximum matching. This article is about computation of maximum matchings.

## Algorithms for bipartite graphs

### Flow-based algorithm

The simplest way to compute a maximum-cardinality matching is to follow the Ford–Fulkerson algorithm. This algorithm solves the more general problem of computing the maximum flow. A bipartite graph (*X* + *Y*, *E*) can be converted to a flow network as follows.

- Add a source vertex s; add an edge from s to each vertex in X.
- Add a sink vertex t; add an edge from each vertex in Y to t.
- Assign a capacity of 1 to each edge.

Since each edge in the network has integral capacity, there exists a maximum flow where all flows are integers; these integers must be either 0 or 1 since the all capacities are 1. Each integral flow defines a matching in which an edge is in the matching if and only if its flow is 1. It is a matching because:

- The incoming flow into each vertex in X is at most 1, so the outgoing flow is at most 1 too, so at most one edge adjacent to each vertex in X is present.
- The outgoing flow from each vertex in Y is at most 1, so the incoming flow is at most 1 too, so at most one edge adjacent to each vertex in Y is present.

The Ford–Fulkerson algorithm proceeds by repeatedly finding an augmenting path from some *x* ∈ *X* to some *y* ∈ Y and updating the matching M by taking the symmetric difference of that path with M (assuming such a path exists). As each path can be found in *O*(*E*) time, the running time is *O*(*VE*), and the maximum matching consists of the edges of E that carry flow from X to Y.

### Advanced algorithms

An improvement to this algorithm is given by the more elaborate Hopcroft–Karp algorithm, which searches for multiple augmenting paths simultaneously. This algorithm runs in $O({\sqrt {V}}E)$ time.

The algorithm of Chandran and Hochbaum for bipartite graphs runs in time that depends on the size of the maximum matching k, which for |*X*| < |*Y*| is

$O\left(\min\{|X|k,E\}+{\sqrt {k}}\min\{k^{2},E\}\right).$

Using Boolean operations on words of size $\lambda$ the complexity is further improved to

$O\left(\min \left\{|X|k,{\frac {|X||Y|}{\lambda }},E\right\}+k^{2}+{\frac {k^{2.5}}{\lambda }}\right).$

More efficient algorithms exist for special kinds of bipartite graphs:

- For sparse bipartite graphs, the maximum matching problem can be solved in ${\tilde {O}}(E^{10/7})$ with Madry's algorithm based on electric flows.
- For planar bipartite graphs, the problem can be solved in time *O*(*n* log3 *n*) where n is the number of vertices, by reducing the problem to maximum flow with multiple sources and sinks.

## Algorithms for arbitrary graphs

The blossom algorithm finds a maximum-cardinality matching in general (not necessarily bipartite) graphs. It runs in time $O(|V|^{2}\cdot |E|)$ . A better performance of *O*(√*V**E*) for general graphs, matching the performance of the Hopcroft–Karp algorithm on bipartite graphs, can be achieved with the much more complicated algorithm of Micali and Vazirani. The same bound was achieved by an algorithm by Blum and an algorithm by Gabow and Tarjan.

An alternative approach uses randomization and is based on the fast matrix multiplication algorithm. This gives a randomized algorithm for general graphs with complexity $O(V^{2.372})$ . This is better in theory for sufficiently dense graphs, but in practice the algorithm is slower.

Other algorithms for the task are reviewed by Duan and Pettie (see Table I). In terms of approximation algorithms, they also point out that the blossom algorithm and the algorithms by Micali and Vazirani can be seen as approximation algorithms running in linear time for any fixed error bound.

## Applications and generalizations

- By finding a maximum-cardinality matching, it is possible to decide whether there exists a perfect matching.
- The problem of finding a matching with maximum weight in a **weighted graph** is called the maximum-weight matching problem, and its restriction to bipartite graphs is called the assignment problem. If each vertex can be matched to several vertices at once, then this is a generalized assignment problem.
- A priority matching is a particular maximum-cardinality matching in which prioritized vertices are matched first.
- The problem of finding a maximum-cardinality matching in hypergraphs is NP-complete even for 3-uniform hypergraphs.
