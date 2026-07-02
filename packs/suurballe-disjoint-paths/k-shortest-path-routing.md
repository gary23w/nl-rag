---
title: "k shortest path routing"
source: https://en.wikipedia.org/wiki/K_shortest_path_routing
domain: suurballe-disjoint-paths
license: CC-BY-SA-4.0
tags: suurballe algorithm, disjoint paths, edge disjoint routing, network survivability
fetched: 2026-07-02
---

# *k* shortest path routing

The ***k* shortest path routing** problem is a generalization of the shortest path routing problem in a given network. It asks not only about a shortest path but also about next *k−1* shortest paths (which may be longer than the shortest path). A variation of the problem is the loopless *k* shortest paths.

Finding *k* shortest paths is possible by extending Dijkstra's algorithm or the Bellman-Ford algorithm.

## History

Since 1957, many papers have been published on the *k* shortest path routing problem. Most of the fundamental works were done between 1960s and 2001. Since then, most of the research has been on the problem's applications and its variants. In 2010, Michael Günther et al. published a book on *Symbolic calculation of*k*-shortest paths and related measures with the stochastic process algebra tool CASPA*.

## Algorithm

Dijkstra's algorithm can be generalized to find the *k* shortest paths.

| **Definitions**: **G(V, E)**: weighted directed graph, with set of vertices **V** and set of directed edges **E**, **w(u, v)**: cost of directed edge from node **u** to node **v** (costs are non-negative). Links that do not satisfy constraints on the shortest path are removed from the graph **s**: the source node **t**: the destination node ***K***: the number of shortest paths to find **pu**: a path from **s** to **u** **B** is a heap data structure containing paths **P**: set of shortest paths from **s** to **t** **countu**: number of shortest paths found to node **u** **Algorithm:** **P** =empty, **countu** = 0, for all u in V insert path **ps** = {s} into **B** with cost **0** while **B** is not empty and **countt** < **K**: – let **pu** be the shortest cost path in **B** with cost **C** – **B** = **B** − **{pu }**, **countu** = **countu** + 1 – if **u** = **t** then **P** = **P** U **{pu}** – if **countu** ≤ **K** then for each vertex **v** adjacent to **u**: – let **pv** be a new path with cost **C** + **w(u, v)** formed by concatenating edge **(u, v)** to path **pu** – insert **pv** into **B** return **P** |
|---|
|   |

## Variations

There are two main variations of the *k* shortest path routing problem. In one variation, paths are allowed to visit the same node more than once, thus creating loops. In another variation, paths are required to be simple and loopless. The loopy version is solvable using Eppstein's algorithm and the loopless variation is solvable by Yen's algorithm.

### Loopy variant

In this variant, the problem is simplified by not requiring paths to be loopless. A solution was given by B. L. Fox in 1975 in which the *k*-shortest paths are determined in *O*(*m* + *kn* log *n*) asymptotic time complexity (using big *O* notation). In 1998, David Eppstein reported an approach that maintains an asymptotic complexity of *O*(*m* + *n* log *n* + *k*) by computing an implicit representation of the paths, each of which can be output in *O*(*n*) extra time. In 2015, Akiba *et al.* devised an indexing method as a significantly faster alternative for Eppstein's algorithm, in which a data structure called an index is constructed from a graph and then top-*k* distances between arbitrary pairs of vertices can be rapidly obtained.

### Loopless variant

In the loopless variant, the paths are forbidden to contain loops, which adds an additional level of complexity. It can be solved using Yen's algorithm to find the lengths of all shortest paths from a fixed node to all other nodes in an *n*-node non negative-distance network, a technique requiring only 2*n*2 additions and *n*2 comparison, fewer than other available shortest path algorithms need. The running time complexity is pseudo-polynomial, being *O*(*kn*(*m* + *n* log *n*)) (where *m* and *n* represent the number of edges and vertices, respectively). In 2007, John Hershberger and Subhash Suri proposed a replacement paths algorithm, a more efficient implementation of Lawler's and Yen's algorithm with *O*(*n*) improvement in time for a large number of graphs, but not all of them (therefore not changing the asymptotic bound of Yen's algorithm).

## Some examples and description

### Example 1

The following example makes use of Yen's model to find *k* shortest paths between communicating end nodes. That is, it finds a shortest path, second shortest path, etc. up to the Kth shortest path. More details can be found here. The code provided in this example attempts to solve the *k* shortest path routing problem for a 15-nodes network containing a combination of unidirectional and bidirectional links:

### Example 2

Another example is the use of *k* shortest paths algorithm to track multiple objects. The technique implements a multiple object tracker based on the *k* shortest paths routing algorithm. A set of probabilistic occupancy maps is used as input. An object detector provides the input.

The complete details can be found at "Computer Vision Laboratory – CVLAB".

### Example 3

Another use of *k* shortest paths algorithms is to design a transit network that enhances passengers' experience in public transportation systems. Such an example of a transit network can be constructed by putting traveling time under consideration. In addition to traveling time, other conditions may be taken depending upon economical and geographical limitations. Despite variations in parameters, the *k* shortest path algorithms finds the most optimal solutions that satisfies almost all user needs. Such applications of *k* shortest path algorithms are becoming common, recently Xu, He, Song, and Chaudhry (2012) studied the *k* shortest path problems in transit network systems.

## Applications

The *k* shortest path routing is a good alternative for:

- Geographic path planning
- Network routing, especially in optical mesh network where there are additional constraints that cannot be solved by using ordinary shortest path algorithms.
- Hypothesis generation in computational linguistics
- Sequence alignment and metabolic pathway finding in bioinformatics
- Multiple object tracking as described above
- Road Networks: road junctions are the nodes (vertices) and each edge (link) of the graph is associated with a road segment between two junctions.

- The breadth-first search algorithm is used when the search is only limited to two operations.
- The Floyd–Warshall algorithm solves all pairs shortest paths.
- Johnson's algorithm solves all pairs' shortest paths, and may be faster than Floyd–Warshall on sparse graphs.
- Perturbation theory finds (at worst) the locally shortest path.

Cherkassky et al. provide more algorithms and associated evaluations.
