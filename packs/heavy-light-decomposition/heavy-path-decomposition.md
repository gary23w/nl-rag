---
title: "Heavy-light decomposition"
source: https://en.wikipedia.org/wiki/Heavy_path_decomposition
domain: heavy-light-decomposition
license: CC-BY-SA-4.0
tags: heavy light decomposition, tree path query, chain partition, segment tree on tree
fetched: 2026-07-02
---

# Heavy-light decomposition

(Redirected from

Heavy path decomposition

)

In combinatorial mathematics and theoretical computer science, **heavy-light decomposition** (also called **heavy path decomposition**) is a technique for decomposing a rooted tree into a set of paths. In a heavy path decomposition, each non-leaf node selects one "heavy edge", the edge to the child that has the greatest number of descendants (breaking ties arbitrarily). The selected edges form the paths of the decomposition.

## Decomposition into paths

If the edges of a tree *T* are partitioned into a set of heavy edges and light edges, with one heavy edge from each non-leaf node to one of its children, then the subgraph formed by the heavy edges consists of a set of paths, with each non-leaf vertex belonging to exactly one path, the one containing its heavy edge. Leaf nodes of the tree that are not the endpoint of a heavy edge may be considered as forming paths of length zero. In this way, each vertex belongs to exactly one of the paths. Each path has a head vertex, its topmost vertex.

Alternatively, the paths of heavy edges may be extended by including one light edge, the one from the head of the path to its parent. In this variation of the decomposition, some vertices belong to multiple paths, but every edge of *T* belongs to exactly one path.

## The path tree

The paths of the decomposition may themselves be organized into a tree called the "path tree", "heavy path tree", or "compressed tree". Each node of the path tree corresponds to a path of the heavy path decomposition. If *p* is a path of the heavy path decomposition, then the parent of *p* in the path tree is the path containing the parent of the head of *p*. The root of the path tree is the path containing the root of the original tree. Alternatively, the path tree may be formed from the original tree by edge contraction of all the heavy edges.

A "light" edge of a given tree is an edge that was not selected as part of the heavy path decomposition. If a light edge connects two tree nodes *x* and *y*, with *x* the parent of *y*, then *x* must have at least twice as many descendants as *y*. Therefore, on any root-to-leaf path of a tree with *n* nodes, there can be at most log2 *n* light edges. Equivalently, the path tree has height at most log2 *n*.

## Applications

Heavy path decomposition was introduced by Sleator & Tarjan (1983) as part of the amortized analysis of their link/cut tree structure, and by Harel & Tarjan (1984) as part of their data structure for lowest common ancestors, The link/cut tree data structure uses a partition of a dynamic tree into paths that is not necessarily the heavy path decomposition; its analysis uses a potential function measuring its distance from the heavy path decomposition, and the small height of the path tree implies that each data structure operation performs only a small number of steps that cannot be charged against improvements to this function. In the lowest common ancestor data structure, the decomposition is used to embed the input tree into a complete binary tree of logarithmic depth, allowing each query to be solved by constant-time bitwise operations.

Subsequent applications of heavy path decomposition have included solving the level ancestor problem, computing the edit distance between trees, graph drawing and greedy embedding, finding a path near all nodes of a given graph, fault diagnosis in fiber-optic communication networks, and decoding grammar-based codes, among others.
