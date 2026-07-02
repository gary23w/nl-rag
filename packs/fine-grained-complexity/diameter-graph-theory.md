---
title: "Diameter (graph theory)"
source: https://en.wikipedia.org/wiki/Diameter_(graph_theory)
domain: fine-grained-complexity
license: CC-BY-SA-4.0
tags: fine grained complexity, fine grained reduction, strong exponential time hypothesis, 3sum conjecture
fetched: 2026-07-02
---

# Diameter (graph theory)

In graph theory, the **diameter** of a connected undirected graph is the farthest distance between any two of its vertices. That is, it is the diameter of a set for the set of vertices of the graph, and for the shortest-path distance in the graph. Diameter may be considered either for weighted or for unweighted graphs. Researchers have studied the problem of computing the diameter, both in arbitrary graphs and in special classes of graphs.

The diameter of a disconnected graph may be defined to be infinite, or undefined.

## Graphs of low diameter

The degree diameter problem seeks tight relations between the diameter, number of vertices, and degree of a graph. One way of formulating it is to ask for the largest graph with given bounds on its degree and diameter. For any fixed degree, this maximum size is exponential in diameter, with the base of the exponent depending on the degree.

The girth of a graph, the length of its shortest cycle, can be at most $2k+1$ for a graph of diameter k . The regular graphs for which the girth is exactly $2k+1$ are the Moore graphs. Only finitely many Moore graphs exist, but their exact number is unknown. They provide the solutions to the degree diameter problem for their degree and diameter.

Small-world networks are a class of graphs with low diameter, modeling the real-world phenomenon of six degrees of separation in social networks.

## Algorithms

### In arbitrary graphs

The diameter of a graph can be computed by using a shortest path algorithm to compute shortest paths between all pairs of vertices, and then taking the maximum of the distances that it computes. For instance, in a graph with positive edge weights, this can be done by repeatedly using Dijkstra's algorithm, once for each possible starting vertex. In a graph with n vertices and m edges, this takes time $O(mn+n^{2}\log n)$ . Computing all-pairs shortest paths is the fastest known method for computing the diameter of a weighted graph exactly.

In an unweighted graph, Dijkstra's algorithm may be replaced by a breadth-first search, giving time $O(mn)$ . Alternatively, the diameter may be computed using an algorithm based on fast matrix multiplication, in time proportional to the time for multiplying $n\times n$ matrices, approximately $O(n^{2.37})$ using known matrix multiplication algorithms. For sparse graphs, with few edges, repeated breadth-first search is faster than matrix multiplication. Assuming the strong exponential time hypothesis, repeated breadth-first search is near-optimal: this hypothesis implies that no algorithm can achieve time $O(m^{2-\varepsilon })$ for any $\varepsilon >0$ .

It is possible to approximate the diameter of a weighted graph to within an approximation ratio of 3/2, in time ${\tilde {O}}(\min(m^{3/2},mn^{2/3})$ , where the ${\tilde {O}}$ notation hides logarithmic factors in the time bound. Under the strong exponential time hypothesis, no substantially more accurate approximation, substantially faster than all pairs shortest paths, is possible.

### In special classes of graphs

The diameter can be computed in linear time for interval graphs, and in near-linear time for graphs of bounded treewidth. In median graphs, the diameter can be found in the subquadratic time bound ${\tilde {O}}(n^{1.6456})$ . In any class of graphs closed under graph minors, such as the planar graphs, it is possible to compute the diameter in subquadratic time, with an exponent depending on the graph family.
