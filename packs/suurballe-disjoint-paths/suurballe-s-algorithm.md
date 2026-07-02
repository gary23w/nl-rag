---
title: "Suurballe's algorithm"
source: https://en.wikipedia.org/wiki/Suurballe's_algorithm
domain: suurballe-disjoint-paths
license: CC-BY-SA-4.0
tags: suurballe algorithm, disjoint paths, edge disjoint routing, network survivability
fetched: 2026-07-02
---

# Suurballe's algorithm

In theoretical computer science and network routing, **Suurballe's algorithm** is an algorithm for finding two disjoint paths in a nonnegatively-weighted directed graph, so that both paths connect the same pair of vertices and have minimum total length. The algorithm was conceived by John W. Suurballe and published in 1974. The main idea of Suurballe's algorithm is to use Dijkstra's algorithm to find one path, to modify the weights of the graph edges, and then to run Dijkstra's algorithm a second time. The output of the algorithm is formed by combining these two paths, discarding edges that are traversed in opposite directions by the paths, and using the remaining edges to form the two paths to return as the output. The modification to the weights is similar to the weight modification in Johnson's algorithm, and preserves the non-negativity of the weights while allowing the second instance of Dijkstra's algorithm to find the correct second path.

The problem of finding two disjoint paths of minimum weight can be seen as a special case of a minimum cost flow problem, where in this case there are two units of "flow" and nodes have unit "capacity". Suurballe's algorithm, also, can be seen as a special case of a minimum cost flow algorithm that repeatedly pushes the maximum possible amount of flow along a shortest augmenting path. The first path found by Suurballe's algorithm is the shortest augmenting path for the initial (zero) flow, and the second path found by Suurballe's algorithm is the shortest augmenting path for the residual graph left after pushing one unit of flow along the first path.

## Definitions

Let *G* be a weighted directed graph with vertex set *V* and edge set *E* (figure A); let *s* be a designated source vertex in *G*, and let *t* be a designated destination vertex. Let each edge (*u*,*v*) in *E*, from vertex *u* to vertex *v*, have a non-negative cost *w*(*u*,*v*).

Define d(*s*,*u*) to be the cost of the shortest path to vertex *u* from vertex *s* in the shortest path tree rooted at *s* (figure C).

Note: Node and Vertex are often used interchangeably.

## Algorithm

Suurballe's algorithm performs the following steps:

1. Find the shortest path tree *T* rooted at node *s* by running Dijkstra's algorithm (figure C). This tree contains for every vertex *u*, a shortest path from *s* to *u*. Let *P*1 be the shortest cost path from *s* to *t* (figure B). The edges in *T* are called *tree edges* and the remaining edges (the edges missing from figure C) are called *non-tree edges*.
2. Modify the cost of each edge in the graph by replacing the cost *w*(*u*,*v*) of every edge (*u*,*v*) by *w′*(*u*,*v*) = *w*(*u*,*v*) − d(*s*,*v*) + d(*s*,*u*). According to the resulting modified cost function, all tree edges have a cost of 0, and non-tree edges have a non-negative cost. For example: If *u*=B, *v*=E, then *w′*(*u*,*v*) = *w*(B,E) − d(A,E) + d(A,B) = 2 − 3 + 1 = 0 If *u*=E, *v*=B, then *w′*(*u*,*v*) = *w*(E,B) − d(A,B) + d(A,E) = 2 − 1 + 3 = 4
3. Create a residual graph *Gt* formed from *G* by removing the edges of *G* on path *P*1 that are directed into *s* and then reverse the direction of the zero length edges along path *P*1 (figure D).
4. Find the shortest path *P*2 in the residual graph *Gt* by running Dijkstra's algorithm (figure E).
5. Discard the reversed edges of *P*2 from both paths. The remaining edges of *P*1 and *P*2 form a subgraph with two outgoing edges at *s*, two incoming edges at *t*, and one incoming and one outgoing edge at each remaining vertex. Therefore, this subgraph consists of two edge-disjoint paths from *s* to *t* and possibly some additional (zero-length) cycles. Return the two disjoint paths from the subgraph.

## Example

The following example shows how Suurballe's algorithm finds the shortest pair of disjoint paths from *A* to *F*.

Figure **A** illustrates a weighted graph *G*.

Figure **B** calculates the shortest path *P*1 from *A* to *F* (*A*–*B*–*D*–*F*).

Figure **C** illustrates the shortest path tree *T* rooted at *A*, and the computed distances from *A* to every vertex (*u*).

Figure **D** shows the residual graph *Gt* with the updated cost of each edge and the edges of path *P*1 reversed.

Figure **E** calculates path *P*2 in the residual graph *Gt* (*A*–*C*–*D*–*B*–*E*–*F*).

Figure **F** illustrates both path *P*1 and path *P*2.

Figure **G** finds the shortest pair of disjoint paths by combining the edges of paths *P*1 and *P*2 and then discarding the common reversed edges between both paths (*B*–*D*). As a result, we get the two shortest pair of disjoint paths (*A*–*B*–*E*–*F*) and (*A*–*C*–*D*–*F*).

## Correctness

The weight of any path from s to t in the modified system of weights equals the weight in the original graph, minus d(*s*,*t*). Therefore, the shortest two disjoint paths under the modified weights are the same paths as the shortest two paths in the original graph, although they have different weights.

Suurballe's algorithm may be seen as a special case of the successive shortest paths method for finding a minimum cost flow with total flow amount two from s to t. The modification to the weights does not affect the sequence of paths found by this method, only their weights. Therefore, the correctness of the algorithm follows from the correctness of the successive shortest paths method.

## Analysis and running time

This algorithm requires two iterations of Dijkstra's algorithm. Using Fibonacci heaps, both iterations can be performed in time $O(|E|+|V|\log |V|)$ where $|V|$ and $|E|$ are the number of vertices and edges respectively. Therefore, the same time bound applies to Suurballe's algorithm.

## Variations

The version of Suurballe's algorithm as described above finds paths that have disjoint edges, but that may share vertices. It is possible to use the same algorithm to find vertex-disjoint paths, by replacing each vertex by a pair of adjacent vertices, one with all of the incoming adjacencies *u-in* of the original vertex, and one with all of the outgoing adjacencies *u-out*. Two edge-disjoint paths in this modified graph necessarily correspond to two vertex-disjoint paths in the original graph, and vice versa, so applying Suurballe's algorithm to the modified graph results in the construction of two vertex-disjoint paths in the original graph. Suurballe's original 1974 algorithm was for the vertex-disjoint version of the problem, and was extended in 1984 by Suurballe and Tarjan to the edge-disjoint version.

By using a modified version of Dijkstra's algorithm that simultaneously computes the distances to each vertex *t* in the graphs *Gt*, it is also possible to find the total lengths of the shortest pairs of paths from a given source vertex *s* to every other vertex in the graph, in an amount of time that is proportional to a single instance of Dijkstra's algorithm.

Note: The pair of adjacent vertices resulting from the split are connected by a zero cost uni-directional edge from the incoming to outgoing vertex. The source vertex becomes *s-out* and the destination vertex becomes *t-in*.
