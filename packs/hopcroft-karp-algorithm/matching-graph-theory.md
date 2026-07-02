---
title: "Matching (graph theory)"
source: https://en.wikipedia.org/wiki/Matching_(graph_theory)
domain: hopcroft-karp-algorithm
license: CC-BY-SA-4.0
tags: hopcroft karp algorithm, bipartite matching, augmenting path, maximum cardinality matching
fetched: 2026-07-02
---

# Matching (graph theory)

In the mathematical discipline of graph theory, a **matching** or **independent edge set** in an undirected graph is a set of edges without common vertices. In other words, a subset of the edges is a matching if each vertex appears in at most one edge of that matching.

Finding a largest matching in a bipartite graph can be treated as a network flow problem. Finding a largest matching in a general graph is much more difficult; it can be done using Edmonds' blossom algorithm.

## Definitions

Given a graph *G* = (*V*, *E*), a **matching** *M* in *G* is a set of pairwise non-adjacent edges, none of which are loops; that is, no two edges share common vertices.

M is a matching *of* $U\subseteq V$ if every vertex in U is incident with an edge in M .

A vertex is **matched** (or **saturated**) if it is an endpoint of one of the edges in the matching. Otherwise the vertex is **unmatched** (or **unsaturated**).

A **maximal matching** is a matching *M* of a graph *G* that is not a subset of any other matching. A matching *M* of a graph *G* is maximal if every edge in *G* has a non-empty intersection with at least one edge in *M*. The following figure shows examples of maximal matchings (red) in three graphs.

A **maximum matching** (also known as maximum-cardinality matching) is a matching that contains the largest possible number of edges. There may be many maximum matchings. The **matching number** $\nu (G)$ of a graph G is the size of a maximum matching. Every maximum matching is maximal, but not every maximal matching is a maximum matching. The following figure shows examples of maximum matchings in the same three graphs.

A **perfect matching** is a matching that matches all vertices of the graph. That is, a matching is perfect if every vertex of the graph is incident to an edge of the matching. A matching is perfect if $|M|=|V|/2$ . Every perfect matching is maximum and hence maximal. In some literature, the term **complete matching** is used. In the above figure, only part (b) shows a perfect matching. A perfect matching is also a minimum-size edge cover. Thus, the size of a maximum matching is no larger than the size of a minimum edge cover: ⁠ $\nu (G)\leq \rho (G)$ ⁠. A graph can only contain a perfect matching when the graph has an even number of vertices.

A **near-perfect matching** is one in which exactly one vertex is unmatched. Clearly, a graph can only contain a near-perfect matching when the graph has an odd number of vertices, and near-perfect matchings are maximum matchings. In the above figure, part (c) shows a near-perfect matching. If every vertex is unmatched by some near-perfect matching, then the graph is called factor-critical.

An **induced matching** is a matching that is the edge set of an induced subgraph.

## Alternating and augmenting paths

Given a matching *M*, an **alternating path** is a path that begins with an unmatched vertex and whose edges belong alternately to the matching and not to the matching. An **augmenting path** is an alternating path that starts from and ends on free (unmatched) vertices. Berge's lemma states that a matching *M* is maximum if and only if there is no augmenting path with respect to M *.* Using Berge's lemma, we can start from any matching M and repeatedly apply augmenting paths until no more augmenting paths are found. This reduces the problem of finding a large matching to finding augmented paths.

## Properties

In any graph without isolated vertices, the sum of the matching number and the edge covering number equals the number of vertices. If there is a perfect matching, then both the matching number and the edge cover number are |*V* | / 2.

### Characterizations

Kőnig's theorem states that, in bipartite graphs, the maximum matching is equal in size to the minimum vertex cover. Via this result, the minimum vertex cover, maximum independent set, and maximum vertex biclique problems may be solved in polynomial time for bipartite graphs.

Hall's marriage theorem provides a characterization of bipartite graphs which have a perfect matching and Tutte's theorem on perfect matchings provides a characterization for arbitrary graphs.

A spectral characterization of the matching number of a graph is given by Hassani Monfared and Mallik as follows: Let G be a graph on n vertices, and $\lambda _{1}>\lambda _{2}>\ldots >\lambda _{k}>0$ be k distinct nonzero purely imaginary numbers where $2k\leq n$ . Then the matching number of G is k if and only if (a) there is a real skew-symmetric matrix A with graph G and eigenvalues $\pm \lambda _{1},\pm \lambda _{2},\ldots ,\pm \lambda _{k}$ and $n-2k$ zeros, and (b) all real skew-symmetric matrices with graph G have at most $2k$ nonzero eigenvalues. Note that the (simple) graph of a real symmetric or skew-symmetric matrix A of order n has n vertices and edges given by the nonozero off-diagonal entries of A .

### Maximum vs. maximal matchings

If *A* and *B* are two maximal matchings, then |*A*| ≤ 2|*B*| and |*B*| ≤ 2|*A*|. To see this, observe that each edge in *B* \ *A* can be adjacent to at most two edges in *A* \ *B* because *A* is a matching; moreover each edge in *A* \ *B* is adjacent to an edge in *B* \ *A* by maximality of *B*, hence

$|A\setminus B|\leq 2|B\setminus A|.$

Further we deduce that

$|A|=|A\cap B|+|A\setminus B|\leq 2|B\cap A|+2|B\setminus A|=2|B|.$

In particular, this shows that any maximal matching is a 2-approximation of a maximum matching and also a 2-approximation of a minimum maximal matching. This inequality is tight: for example, if *G* is a path with 3 edges and 4 vertices, the size of a minimum maximal matching is 1 and the size of a maximum matching is 2.

## Matching polynomials

A generating function of the number of *k*-edge matchings in a graph is called a matching polynomial. Let *G* be a graph and *mk* be the number of *k*-edge matchings. One matching polynomial of *G* is

$\sum _{k\geq 0}m_{k}x^{k}.$

Another definition gives the matching polynomial as

$\sum _{k\geq 0}(-1)^{k}m_{k}x^{n-2k},$

where *n* is the number of vertices in the graph. Each type has its uses; for more information see the article on matching polynomials.

## Algorithms and computational complexity

### Maximum-cardinality matching

A fundamental problem in combinatorial optimization is finding a *maximum matching*. This problem has various algorithms for different classes of graphs.

In an *unweighted bipartite graph*, the optimization problem is to find a maximum cardinality matching. The problem is solved by the Hopcroft-Karp algorithm in time *O*(√*V**E*) time, and there are more efficient randomized algorithms, approximation algorithms, and algorithms for special classes of graphs such as bipartite planar graphs, as described in the main article.

### Maximum-weight matching

In a *weighted* *bipartite graph,* the optimization problem is to find a maximum-weight matching; a dual problem is to find a minimum-weight matching. This problem is often called **maximum weighted bipartite matching**, or the **assignment problem**. The Hungarian algorithm solves the assignment problem and it was one of the beginnings of combinatorial optimization algorithms. It uses a modified shortest path search in the augmenting path algorithm. If the Bellman–Ford algorithm is used for this step, the running time of the Hungarian algorithm becomes $O(V^{2}E)$ , or the edge cost can be shifted with a potential to achieve $O(V^{2}\log {V}+VE)$ running time with the Dijkstra algorithm and Fibonacci heap.

In a *non-bipartite weighted graph*, the problem of **maximum weight matching** can be solved in time $O(V^{2}E)$ using Edmonds' blossom algorithm.

### Maximal matchings

A maximal matching can be found with a simple greedy algorithm. A maximum matching is also a maximal matching, and hence it is possible to find a *largest* maximal matching in polynomial time. It is also possible to find a maximum matching with the use of fast matrix multiplication algorithms in the time $O({n^{\omega }})$ for $~2.37\leq \omega <3$ . However, no polynomial-time algorithm is known for finding a **minimum maximal matching**, that is, a maximal matching that contains the *smallest* possible number of edges.

A maximal matching with *k* edges is an edge dominating set with *k* edges. Conversely, if we are given a minimum edge dominating set with *k* edges, we can construct a maximal matching with *k* edges in polynomial time. Therefore, the problem of finding a minimum maximal matching is essentially equal to the problem of finding a minimum edge dominating set. Both of these two optimization problems are known to be NP-hard; the decision versions of these problems are classical examples of NP-complete problems. Both problems can be approximated within factor 2 in polynomial time: simply find an arbitrary maximal matching *M*.

### Counting problems

The number of matchings in a graph is known as the Hosoya index of the graph. It is #P-complete to compute this quantity, even for bipartite graphs. It is also #P-complete to count perfect matchings, even in bipartite graphs, because computing the permanent of an arbitrary 0–1 matrix (another #P-complete problem) is the same as computing the number of perfect matchings in the bipartite graph having the given matrix as its biadjacency matrix. However, there exists a fully polynomial time randomized approximation scheme for counting the number of bipartite matchings. A remarkable theorem of Kasteleyn states that the number of perfect matchings in a planar graph can be computed exactly in polynomial time via the FKT algorithm.

The number of perfect matchings in a complete graph *K**n* (with *n* even) is given by the double factorial (*n* − 1)!!. The numbers of matchings in complete graphs, without constraining the matchings to be perfect, are given by the telephone numbers.

The number of perfect matchings in a graph is also known as the hafnian of its adjacency matrix.

### Finding all maximally matchable edges

One of the basic problems in matching theory is to find in a given graph all edges that may be extended to a maximum matching in the graph (such edges are called maximally matchable edges, or **allowed** edges). Algorithms for this problem include:

- For general graphs, a deterministic algorithm in time $O(VE)$ and a randomized algorithm in time ${\tilde {O}}(V^{2.376})$ .
- For bipartite graphs, if a single maximum matching is found, a deterministic algorithm runs in time $O(V+E)$ .

### Online bipartite matching

The problem of developing an online algorithm for matching was first considered by Richard M. Karp, Umesh Vazirani, and Vijay Vazirani in 1990.

In the online setting, nodes on one side of the bipartite graph ("clients") arrive one at a time and must either be immediately matched to the other side of the graph ("servers") or discarded. This is a natural generalization of the secretary problem and has applications to online ad auctions. A simple greedy algorithm is 1/2-competitive. For the unweighted maximization case with a random arrival model, Karp, Vazirani and Vazirani gave a randomized algorithm that attains a competitive ratio of 0.632. The bound was later improved to 0.696. The problem was also studied in a model where clients may switch servers in order to improve the matching, and the goal is to economize on the number of switches while achieving a maximum matching.

## Applications

### Matching in general graphs

- A **Kekulé structure** of an aromatic compound consists of a perfect matching of its carbon skeleton, showing the locations of double bonds in the chemical structure. These structures are named after Friedrich August Kekulé von Stradonitz, who showed that benzene (in graph theoretical terms, a 6-vertex cycle) can be given such a structure.
- The Hosoya index is the number of non-empty matchings plus one; it is used in computational chemistry and mathematical chemistry investigations for organic compounds.
- The Chinese postman problem involves finding a minimum-weight perfect matching as a subproblem.

### Matching in bipartite graphs

- The graduation problem is about choosing minimum set of classes from given requirements for graduation.
- The Hitchcock transport problem involves bipartite matching as a sub-problem.
- The subtree isomorphism problem involves bipartite matching as a sub-problem.
