---
title: "Iterative compression"
source: https://en.wikipedia.org/wiki/Iterative_compression
domain: fixed-parameter-tractable
license: CC-BY-SA-4.0
tags: fixed parameter tractable, bounded search tree, iterative compression, color coding technique
fetched: 2026-07-02
---

# Iterative compression

In computer science, **iterative compression** is an algorithmic technique for the design of fixed-parameter tractable algorithms, in which one element (such as a vertex of a graph) is added to the problem in each step, and a small solution for the problem prior to the addition is used to help find a small solution to the problem after the step.

The technique was invented by Reed, Smith and Vetta to show that the odd cycle transversal problem was solvable in time *O*(3*k* *kmn*), for a graph with n vertices, m edges, and odd cycle transversal number k. Odd cycle transversal is the problem of finding the smallest set of vertices of a graph that includes at least one vertex from every odd cycle; its parameterized complexity was a longstanding open question. This technique later proved very useful in showing fixed-parameter tractability results. It is now considered to be one of the fundamental techniques in the area of parameterized algorithmics.

Iterative compression has been used successfully in many problems, for instance odd cycle transversal (see below) and edge bipartization, feedback vertex set, and cluster vertex deletion. It has also been used successfully for exact exponential time algorithms for independent set.

## Technique

Iterative compression applies, for instance, to parameterized graph problems whose inputs are a graph *G* = (*V*,*E*) and a natural number k, and where the problem is to test the existence of a solution (a set of vertices) of size ≤ *k*. Suppose that the problem has the following properties:

- It is closed under induced subgraphs: If a solution of size ≤ *k* exists in a given graph, then a solution of this size or smaller also exists in every induced subgraph).
- If X is a solution, and X' is a set of vertices containing X, then X' is also a solution.
- There exists an efficient subroutine which, given a solution Y of size *k* + 1 determines whether it can be *compressed* to a solution of size k. That is, it finds a solution of size k or determines that no such solution exists.

If these assumptions are met, then the problem can be solved by adding vertices one at a time to an induced subgraph, and finding the solution to the induced subgraph, as follows:

1. Start with a subgraph induced by a vertex set S of size k, and a solution X that equals S itself. (If X is not a solution to S then no solution exists.)
2. While *S* ≠ *V*, perform the following steps:
  - Let v be any vertex of *V* \ *S*, and add v to S
  - Test whether the (*k* + 1)-vertex solution *Y* = *X* ∪ {v} to S can be compressed to a k-vertex solution.
  - If it cannot be compressed, abort the algorithm: the input graph has no k-vertex solution.
  - Otherwise, set X to the new compressed solution and continue the loop.

This algorithm calls the compression subroutine a linear number of times. Therefore, if the compression variant is solvable in fixed-parameter tractable time, i.e., *f*(*k*) · *n**c* for some constant *c*, then the iterative compression procedure solving the entire problem runs in *f*(*k*) · *n**c*+1 time. The same technique can be applied to finding sets of edges for graph properties closed under subgraphs (rather than induced subgraph), or for other properties beyond graph theory. When the value of the parameter k is unknown, it can be found by using an outer level of exponential search or sequential search for the optimal choice of k, with each step of the search based on the same iterative compression algorithm.

## Applications

An odd cycle transversal of a graph is a set of vertices which can be deleted to make the graph bipartite. In their original paper, Reed et al. gave an iterative compression algorithm to determine if a graph has an odd cycle transversal of size at most *k*, in time *O*(3*k* *kmn*). Later, a simpler algorithm was given, also using iterative compression, by Lokshstanov, Saurabh and Sikdar. In order to compress a deletion set Y of size *k* + 1 to a deletion set X of size k, their algorithm tests all of the 3*k*+1 partitions of Y into three subsets: the subset of Y that belongs to the new deletion set, and the two subsets of Y that belong to the two sides of the bipartite graph that remains after deleting X. Once these three sets have been selected, the remaining vertices of a deletion set X (if it exists) can be found from them by applying a max-flow min-cut algorithm.

Vertex cover is another example for which iterative compression can be employed. In the vertex cover problem, a graph *G* = (*V*,*E*) and a natural number k are taken as inputs and the algorithm must decide whether there exists a set X of k vertices such that every edge is incident to a vertex in X. In the compression variant of the problem, the input is a set Y of *k* + 1 vertices that are incident to all edges of the graph, and the algorithm must find a set X of size k with the same property, if it exists. One way to do this is to test all 2*k* + 1 choices of which subset of Y is to be removed from the cover and reintroduced back into the graph. Such a choice can only work if no two removed vertices are adjacent, and for each such choice, the subroutine must include in the cover all the vertices outside Y that are incident to an edge that becomes uncovered by this removal. Using this subroutine in an iterative compression algorithm gives a simple *O*(2*k* *n*2) algorithm for vertex cover.
