---
title: "Minimum cut"
source: https://en.wikipedia.org/wiki/Minimum_cut
domain: gomory-hu-tree
license: CC-BY-SA-4.0
tags: gomory hu tree, all pairs min cut, cut tree, flow equivalent tree
fetched: 2026-07-02
---

# Minimum cut

In graph theory, a **minimum cut** or **min-cut** of a graph is a cut (a partition of the vertices of a graph into two disjoint subsets) that is minimal in some metric. In the simplest *unweighted min-cut problem*, the goal is to minimize the number of edges connecting the two parts.

Variations of the minimum cut problem consider *weighted graphs*, *directed graphs*, *terminals*, and partitioning the vertices into *more than two sets*.

The weighted min-cut problem allowing both positive and negative weights can be trivially transformed into a weighted maximum cut problem by flipping the sign in all weights.

## Without terminal nodes

The input is a graph G = (V, E). The required output is a partition V = S + T (a partition of the vertices into two disjoint subsets S and T). Any such partition has a *cost,* and the goal is to find a partition with a smallest cost.

- In the unweighted version, the cost of a cut (S,T) is the number of edges with one end at S and one end at T. In this case, the minimum cut equals the edge connectivity of the graph. Karger's algorithm provides an efficient randomized method for finding the cut.
- In the weighted version, each edge in E has a weight, and the cost of a cut (S,T) is the total weight of edges with one end at S and one end at T. When the weights are non-negative, the problem can be solved in polynomial time by the Stoer-Wagner algorithm.

### k-cut

A generalization of the minimum cut problem without terminals is the minimum k-cut, in which the goal is to partition the graph into at least k connected components by removing as few edges as possible. For a fixed value of k, this problem can be solved in polynomial time, though the algorithm is not practical for large k.

## With terminal nodes

In the variant called *min s-t cut*, the input contains, in addition to the graph, two nodes called *s* (source) and *t* (target / sink). The required output is a partition V = S + T such that s is in S and t is in T.

In a flow network, the minimum cut separates the source and sink vertices and minimizes the total sum of the capacities of the edges that are directed from the source side of the cut to the sink side of the cut. As shown in the max-flow min-cut theorem, the weight of this cut equals the maximum amount of flow that can be sent from the source to the sink in the given network.

In a weighted, undirected network, it is possible to calculate the cut that separates a particular pair of vertices from each other and has minimum possible total cost. A system of cuts that solves this problem for every possible vertex pair can be collected into a structure known as the Gomory–Hu tree of the graph.

### k-cut

A generalization of the minimum cut problem with terminals is the k-terminal cut, or multi-terminal cut. In a planar graph, this problem can be solved in polynomial time. However, in general this problem is NP-hard, even for $k=3$ .

## Applications

Graph partition problems are a family of combinatorial optimization problems in which a graph is to be partitioned into two or more parts with additional constraints such as balancing the sizes of the two sides of the cut. Segmentation-based object categorization can be viewed as a specific case of normalized min-cut spectral clustering applied to image segmentation. It can also be used as a generic clustering method, where the nodes are data samples assumed to be taken from a metric space and edge weights are their distances. This is however often impractical due do the high computational complexity for $k>2$ .

Due to max-flow min-cut theorem, 2 nodes' Minimum cut value is equal to their maxflow value. In this case, some algorithms used in maxflow problem could also be used to solve this question.

## Number of minimum cuts

A graph with n vertices can at the most have ${\binom {n}{2}}={\frac {n(n-1)}{2}}$ distinct minimum cuts. This bound is tight in the sense that a (simple) cycle on n vertices has exactly ${\frac {n(n-1)}{2}}$ minimum cuts.
