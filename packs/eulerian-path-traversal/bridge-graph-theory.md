---
title: "Bridge (graph theory)"
source: https://en.wikipedia.org/wiki/Bridge_(graph_theory)
domain: eulerian-path-traversal
license: CC-BY-SA-4.0
tags: eulerian path, eulerian circuit, degree condition, bridge finding
fetched: 2026-07-02
---

# Bridge (graph theory)

In graph theory, a **bridge**, **isthmus**, **cut-edge**, or **cut arc** is an edge of a graph whose deletion increases the graph's number of connected components. Equivalently, an edge is a bridge if and only if it is not contained in any cycle. For a connected graph, a bridge can uniquely determine a cut. A graph is said to be **bridgeless** or **isthmus-free** if it contains no bridges.

This type of bridge should be distinguished from an unrelated meaning of "bridge" in graph theory, a subgraph separated from the rest of the graph by a specified subset of vertices; see bridge in the Glossary of graph theory.

## Trees and forests

A graph with n nodes can contain at most $n-1$ bridges, since adding additional edges must create a cycle. The graphs with exactly $n-1$ bridges are exactly the trees, and the graphs in which every edge is a bridge are exactly the forests.

In every undirected graph, there is an equivalence relation on the vertices according to which two vertices are related to each other whenever there are two edge-disjoint paths connecting them. (Every vertex is related to itself via two length-zero paths, which are identical but nevertheless edge-disjoint.) The equivalence classes of this relation are called **2-edge-connected components**, and the bridges of the graph are exactly the edges whose endpoints belong to different components. The **bridge-block tree** of the graph has a vertex for every nontrivial component and an edge for every bridge.

## Relation to vertex connectivity

Bridges are closely related to the concept of articulation vertices, vertices that belong to every path between some pair of other vertices. The two endpoints of a bridge are articulation vertices unless they have a degree of 1, although it may also be possible for a non-bridge edge to have two articulation vertices as endpoints. Analogously to bridgeless graphs being 2-edge-connected, graphs without articulation vertices are 2-vertex-connected.

In a cubic graph, every cut vertex is an endpoint of at least one bridge.

## Bridgeless graphs

A **bridgeless graph** is a graph that does not have any bridges. Equivalent conditions are that each connected component of the graph has an open ear decomposition, that each connected component is 2-edge-connected, or (by Robbins' theorem) that every connected component has a strong orientation.

An important open problem involving bridges is the cycle double cover conjecture, due to Seymour and Szekeres (1978 and 1979, independently), which states that every bridgeless graph admits a multi-set of simple cycles which contains each edge exactly twice.

## Tarjan's bridge-finding algorithm

The first linear time algorithm (linear in the number of edges) for finding the bridges in a graph was described by Robert Tarjan in 1974. It performs the following steps:

- Find a spanning forest of G
- Create a Rooted forest F from the spanning forest
- Traverse the forest F in preorder and number the nodes. Parent nodes in the forest now have lower numbers than child nodes.
- For each node v in preorder (denoting each node using its preorder number), do:
  - Compute the number of forest descendants $ND(v)$ for this node, by adding one to the sum of its children's descendants.
  - Compute $L(v)$ , the lowest preorder label reachable from v by a path for which all but the last edge stays within the subtree rooted at v . This is the minimum of the set consisting of the preorder label of v , of the values of $L(w)$ at child nodes of v and of the preorder labels of nodes reachable from v by edges that do not belong to F .
  - Similarly, compute $H(v)$ , the highest preorder label reachable by a path for which all but the last edge stays within the subtree rooted at v . This is the maximum of the set consisting of the preorder label of v , of the values of $H(w)$ at child nodes of v and of the preorder labels of nodes reachable from v by edges that do not belong to F .
  - For each node w with parent node v , if $L(w)=w$ and $H(w)<w+ND(w)$ then the edge from v to w is a bridge.

## Bridge-finding with chain decompositions

A very simple bridge-finding algorithm uses chain decompositions. Chain decompositions do not only allow to compute all bridges of a graph, they also allow to *read off* every cut vertex of *G* (and the block-cut tree of *G*), giving a general framework for testing 2-edge- and 2-vertex-connectivity (which extends to linear-time 3-edge- and 3-vertex-connectivity tests).

Chain decompositions are special ear decompositions depending on a DFS-tree *T* of *G* and can be computed very simply: Let every vertex be marked as unvisited. For each vertex *v* in ascending DFS-numbers 1...*n*, traverse every backedge (i.e. every edge not in the DFS tree) that is incident to *v* and follow the path of tree-edges back to the root of *T*, stopping at the first vertex that is marked as visited. During such a traversal, every traversed vertex is marked as visited. Thus, a traversal stops at the latest at *v* and forms either a directed path or cycle, beginning with v; we call this path or cycle a *chain*. The *i*th chain found by this procedure is referred to as *Ci*. *C=C1,C2,...* is then a *chain decomposition* of *G*.

The following characterizations then allow to *read off* several properties of *G* from *C* efficiently, including all bridges of *G*. Let *C* be a chain decomposition of a simple connected graph *G=(V,E)*.

1. *G* is 2-edge-connected if and only if the chains in *C* partition *E*.
2. An edge *e* in *G* is a bridge if and only if *e* is not contained in any chain in *C*.
3. If *G* is 2-edge-connected, *C* is an ear decomposition.
4. *G* is 2-vertex-connected if and only if *G* has minimum degree 2 and *C1* is the only cycle in *C*.
5. A vertex *v* in a 2-edge-connected graph *G* is a cut vertex if and only if *v* is the first vertex of a cycle in *C - C1*.
6. If *G* is 2-vertex-connected, *C* is an open ear decomposition.

## Bridges and Eulerian cycles

Define an **Eulerian graph** as a graph with an Eulerian cycle. Every Eulerian graph is bridgeless. This is because in an Eulerian graph every edge is a part of an Eulerian cycle. Hence, if the edge is deleted, then its endpoints remain connected through the rest of the cycle. But the opposite is not true.

Define an **almost Eulerian graph** as a graph that can be made Eulerian by adding a single edge (equivalently, a graph that contains an Eulerian trail). Every almost-Eulerian graph is almost-bridgeless, but the opposite is not true.

The classes of bridgeless graphs and almost-Eulerian graphs have a non-empty intersection (the Eulerian graphs are both bridgeless and almost-Eulerian), but they do not contain each other.
