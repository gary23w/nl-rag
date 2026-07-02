---
title: "Shortest path problem"
source: https://en.wikipedia.org/wiki/Shortest_path_problem
domain: bellman-ford-algorithm
license: CC-BY-SA-4.0
tags: bellman ford algorithm, shortest path, negative cycle, relaxation step
fetched: 2026-07-02
---

# Shortest path problem

In graph theory, the **shortest path problem** is the problem of finding a path between two vertices (or nodes) in a graph such that the sum of the weights of its constituent edges is minimized.

The problem of finding the shortest path between two intersections on a road map may be modeled as a special case of the shortest path problem in graphs, where the vertices correspond to intersections and the edges correspond to road segments, each weighted by the length or distance of each segment.

## Definition

The shortest path problem can be defined for graphs whether undirected, directed, or mixed. The definition for undirected graphs states that every edge can be traversed in either direction. Directed graphs require that consecutive vertices be connected by an appropriate directed edge.

Two vertices are adjacent when they are both incident to a common edge. A path in an undirected graph is a sequence of vertices $P=(v_{1},v_{2},\ldots ,v_{n})\in V\times V\times \cdots \times V$ such that $v_{i}$ is adjacent to $v_{i+1}$ for $1\leq i<n$ . Such a path P is called a path of length $n-1$ from $v_{1}$ to $v_{n}$ . (The $v_{i}$ are variables; their numbering relates to their position in the sequence and need not relate to a canonical labeling.)

Let $E=\{e_{i,j}\}$ where $e_{i,j}$ is the edge incident to both $v_{i}$ and $v_{j}$ . Given a real-valued weight function $f:E\rightarrow \mathbb {R}$ , and an undirected (simple) graph G , the shortest path from v to $v'$ is the path $P=(v_{1},v_{2},\ldots ,v_{n})$ (where $v_{1}=v$ and $v_{n}=v'$ ) that over all possible n minimizes the sum $\sum _{i=1}^{n-1}f(e_{i,i+1}).$ When each edge in the graph has unit weight or $f:E\rightarrow \{1\}$ , this is equivalent to finding the path with fewest edges.

The problem is also sometimes called the **single-pair shortest path problem**, to distinguish it from the following variations:

- The **single-source shortest path problem**, in which we have to find shortest paths from a source vertex *v* to all other vertices in the graph.
- The **single-destination shortest path problem**, in which we have to find shortest paths from all vertices in the directed graph to a single destination vertex *v*. This can be reduced to the single-source shortest path problem by reversing the arcs in the directed graph.
- The **all-pairs shortest path problem**, in which we have to find shortest paths between every pair of vertices *v*, *v'* in the graph.

These generalizations have significantly more efficient algorithms than the simplistic approach of running a single-pair shortest path algorithm on all relevant pairs of vertices.

## Algorithms

Several well-known algorithms exist for solving this problem and its variants.

- Dijkstra's algorithm solves the single-source shortest path problem with only non-negative edge weights.
- Bellman–Ford algorithm solves the single-source problem if edge weights may be negative.
- A* search algorithm solves for single-pair shortest path using heuristics to try to speed up the search.
- Floyd–Warshall algorithm solves all pairs shortest paths.
- Johnson's algorithm solves all pairs shortest paths, and may be faster than Floyd–Warshall on sparse graphs.
- Viterbi algorithm solves the shortest stochastic path problem with an additional probabilistic weight on each node.

Additional algorithms and associated evaluations may be found in Cherkassky, Goldberg & Radzik (1996).

## Single-source shortest paths

### Undirected graphs

| Weights | Time complexity | Author |
|---|---|---|
| $\mathbb {R}$ + | $O(V^{2})$ | Dijkstra 1959 |
| $\mathbb {R}$ + | $O((E+V)\log {V})$ | Johnson 1977 (binary heap) |
| $\mathbb {R}$ + | $O(E+V\log {V})$ | Fredman & Tarjan 1984 (Fibonacci heap) |
| $\mathbb {N}$ | $O(E)$ | Thorup 1999 (requires constant-time multiplication) |
| $\mathbb {R}$ + | $O(E{\sqrt {\log V\log \log V}})$ | Duan et al. 2023 |

### Unweighted graphs

| Algorithm | Time complexity | Author |
|---|---|---|
| Breadth-first search | $O(E+V)$ |   |

### Directed acyclic graphs

An algorithm using topological sorting can solve the single-source shortest path problem in time Θ(*E* + *V*) in arbitrarily-weighted directed acyclic graphs.

### Directed graphs with nonnegative weights

The following table is taken from Schrijver (2004), with some corrections and additions. A green background indicates an asymptotically best bound in the table; *L* is the maximum length (or weight) among all edges, assuming integer edge weights.

| Weights | Algorithm | Time complexity | Author |
|---|---|---|---|
| $\mathbb {R}$ |   | $O(V^{2}EL)$ | Ford 1956 |
| $\mathbb {R}$ | Bellman–Ford algorithm | $O(VE)$ | Shimbel 1955, Bellman 1958, Moore 1959 |
| $\mathbb {R}$ |   | $O(V^{2}\log {V})$ | Dantzig 1960 |
| $\mathbb {R}$ | Dijkstra's algorithm with list | $O(V^{2})$ | Leyzorek et al. 1957, Dijkstra 1959, Minty (see Pollack & Wiebenson 1960), Whiting & Hillier 1960 |
| $\mathbb {R}$ | Dijkstra's algorithm with binary heap | $O((E+V)\log {V})$ | Johnson 1977 |
| $\mathbb {R}$ | Dijkstra's algorithm with Fibonacci heap | $O(E+V\log {V})$ | Fredman & Tarjan 1984, Fredman & Tarjan 1987 |
| $\mathbb {R}$ | Quantum Dijkstra algorithm with adjacency list | $O({\sqrt {VE}}\log ^{2}{V})$ | Dürr et al. 2006 |
| $\mathbb {R}$ | Dijkstra's-Bellman–Ford hybrid with a divide-and-conquer frontier reduction | $O(E\log ^{2/3}{V})$ | Duan et al. 2025 |
| $\mathbb {N}$ | Dial's algorithm (Dijkstra's algorithm using a bucket queue with *L* buckets) | $O(E+LV)$ | Dial 1969 |
|   |   | $O(E\log {\log {L}})$ | Johnson 1981, Karlsson & Poblete 1983 |
|   | Gabow's algorithm | $O(E\log _{E/V}L)$ | Gabow 1983, Gabow 1985 |
|   |   | $O(E+V{\sqrt {\log {L}}})$ | Ahuja et al. 1990 |
| $\mathbb {N}$ | Thorup | $O(E+V\log {\log {V}})$ | Thorup 2004 |

### Directed graphs with arbitrary weights without negative cycles

| Weights | Algorithm | Time complexity | Author |
|---|---|---|---|
| $\mathbb {R}$ |   | $O(V^{2}EL)$ | Ford 1956 |
| $\mathbb {R}$ | Bellman–Ford algorithm | $O(VE)$ | Shimbel 1955, Bellman 1958, Moore 1959 |
| $\mathbb {R}$ | Johnson-Dijkstra with binary heap | $O(VE+V\log V)$ | Johnson 1977 |
| $\mathbb {R}$ | Johnson-Dijkstra with Fibonacci heap | $O(VE+V\log V)$ | Fredman & Tarjan 1984, Fredman & Tarjan 1987, adapted after Johnson 1977 |
| $\mathbb {Z}$ | Johnson's technique applied to Dial's algorithm | $O(V(E+L))$ | Dial 1969, adapted after Johnson 1977 |
| $\mathbb {Z}$ | Interior-point method with Laplacian solver | $O(E^{10/7}\log ^{O(1)}V\log ^{O(1)}L)$ | Cohen et al. 2017 |
| $\mathbb {Z}$ | Interior-point method with $\ell _{p}$ flow solver | $E^{4/3+o(1)}\log ^{O(1)}L$ | Axiotis, Mądry & Vladu 2020 |
| $\mathbb {Z}$ | Robust interior-point method with sketching | $O((E+V^{3/2})\log ^{O(1)}V\log ^{O(1)}L)$ | van den Brand et al. 2020 |
| $\mathbb {Z}$ | $\ell _{1}$ interior-point method with dynamic min-ratio cycle data structure | $O(E^{1+o(1)}\log L)$ | Chen et al. 2022 |
| $\mathbb {Z}$ | Based on low-diameter decomposition | $O(E\log ^{8}V\log L)$ | Bernstein, Nanongkai & Wulff-Nilsen 2022 |
| $\mathbb {R}$ | Hop-limited shortest paths | $O(EV^{8/9}\log ^{O(1)}V)$ | Fineman 2024 |
| $\mathbb {R}$ | Steiner-Tree Gadgets | $O(V^{2+o(1)})$ | Khanna & Song 2026 harvnb error: no target: CITEREFKhannaSong2026 (help) |

### Directed graphs with arbitrary weights with negative cycles

Finds a negative cycle or calculates distances to all vertices.

| Weights | Algorithm | Time complexity | Author |
|---|---|---|---|
| $\mathbb {Z}$ |   | $O(E{\sqrt {V}}\log {N})$ | Andrew V. Goldberg |

### Planar graphs with nonnegative weights

| Weights | Algorithm | Time complexity | Author |
|---|---|---|---|
| $\mathbb {R} _{\geq 0}$ |   | $O(V)$ | Henzinger et al. 1997 |

## Applications

**Network flows** are a fundamental concept in graph theory and operations research, often used to model problems involving the transportation of goods, liquids, or information through a network. A network flow problem typically involves a directed graph where each edge represents a pipe, wire, or road, and each edge has a capacity, which is the maximum amount that can flow through it. The goal is to find a feasible flow that maximizes the flow from a source node to a sink node.

**Shortest Path Problems** can be used to solve certain network flow problems, particularly when dealing with single-source, single-sink networks. In these scenarios, we can transform the network flow problem into a series of shortest path problems.

### Transformation Steps

1. **Create a Residual Graph:**
  - For each edge (u, v) in the original graph, create two edges in the residual graph:
    - (u, v) with capacity c(u, v)
    - (v, u) with capacity 0
  - The residual graph represents the remaining capacity available in the network.
2. **Find the Shortest Path:**
  - Use a shortest path algorithm (e.g., Dijkstra's algorithm, Bellman-Ford algorithm) to find the shortest path from the source node to the sink node in the residual graph.
3. **Augment the Flow:**
  - Find the minimum capacity along the shortest path.
  - Increase the flow on the edges of the shortest path by this minimum capacity.
  - Decrease the capacity of the edges in the forward direction and increase the capacity of the edges in the backward direction.
4. **Update the Residual Graph:**
  - Update the residual graph based on the augmented flow.
5. **Repeat:**
  - Repeat steps 2-4 until no more paths can be found from the source to the sink.

## All-pairs shortest paths

The all-pairs shortest path problem finds the shortest paths between every pair of vertices v, v' in the graph. The all-pairs shortest paths problem for unweighted directed graphs was introduced by Shimbel (1953), who observed that it could be solved by a linear number of matrix multiplications that takes a total time of *O*(*V*4).

### Undirected graph

| Weights | Time complexity | Algorithm |
|---|---|---|
| $\mathbb {R}$ + | $O(V^{3})$ | Floyd–Warshall algorithm |
| $\{1,\infty \}$ | $O(V^{\omega }\log V)$ | Seidel's algorithm (expected running time using fast matrix multiplication algorithms) |
| $\mathbb {N}$ | $O(V^{3}/2^{\Omega (\log V)^{1/2}})$ | Williams 2014 |
| $\mathbb {R}$ + | $O(EV\log \alpha (E,V))$ | Pettie & Ramachandran 2002 |
| $\mathbb {N}$ | $O(EV)$ | Thorup 1999 applied to every vertex (requires constant-time multiplication). |

### Directed graph

| Weights | Time complexity | Algorithm |
|---|---|---|
| $\mathbb {R}$ (no negative cycles) | $O(V^{3})$ | Floyd–Warshall algorithm |
| $\mathbb {N}$ | $O(V^{3}/2^{\Omega (\log V)^{1/2}})$ | Williams 2014 |
| $\mathbb {R}$ (no negative cycles) | $O(V^{2.5}\log ^{2}{V})$ | Quantum search |
| $\mathbb {R}$ (no negative cycles) | $O(EV+V^{2}\log V)$ | Johnson–Dijkstra |
| $\mathbb {R}$ (no negative cycles) | $O(EV+V^{2}\log \log V)$ | Pettie 2004 |
| $\mathbb {N}$ | $O(EV+V^{2}\log \log V)$ | Hagerup 2000 |

## Applications

Shortest path algorithms are applied to automatically find directions between physical locations, such as driving directions on web mapping websites like MapQuest or Google Maps. For this application fast specialized algorithms are available.

If one represents a nondeterministic abstract machine as a graph where vertices describe states and edges describe possible transitions, shortest path algorithms can be used to find an optimal sequence of choices to reach a certain goal state, or to establish lower bounds on the time needed to reach a given state. For example, if vertices represent the states of a puzzle like a Rubik's Cube and each directed edge corresponds to a single move or turn, shortest path algorithms can be used to find a solution that uses the minimum possible number of moves.

In a networking or telecommunications mindset, this shortest path problem is sometimes called the min-delay path problem and usually tied with a widest path problem. For example, the algorithm may seek the shortest (min-delay) widest path, or widest shortest (min-delay) path.

A more lighthearted application is the games of "six degrees of separation" that try to find the shortest path in graphs like movie stars appearing in the same film.

Other applications, often studied in operations research, include plant and facility layout, robotics, transportation, and VLSI design.

### Road networks

A road network can be considered as a graph with positive weights. The nodes represent road junctions and each edge of the graph is associated with a road segment between two junctions. The weight of an edge may correspond to the length of the associated road segment, the time needed to traverse the segment, or the cost of traversing the segment. Using directed edges it is also possible to model one-way streets. Such graphs are special in the sense that some edges are more important than others for long-distance travel (e.g. highways). This property has been formalized using the notion of highway dimension. There are a great number of algorithms that exploit this property and are therefore able to compute the shortest path a lot quicker than would be possible on general graphs.

All of these algorithms work in two phases. In the first phase, the graph is preprocessed without knowing the source or target node. The second phase is the query phase. In this phase, source and target node are known. The idea is that the road network is static, so the preprocessing phase can be done once and used for a large number of queries on the same road network.

The algorithm with the fastest known query time is called hub labeling and is able to compute shortest path on the road networks of Europe or the US in a fraction of a microsecond. Other techniques that have been used are:

- ALT (A* search, landmarks, and triangle inequality)
- Arc flags
- Contraction hierarchies
- Transit node routing
- Reach-based pruning
- Labeling
- Hub labels

For shortest path problems in computational geometry, see Euclidean shortest path.

The shortest multiple disconnected path is a representation of the primitive path network within the framework of Reptation theory. The widest path problem seeks a path so that the minimum label of any edge is as large as possible.

Other related problems may be classified into the following categories.

### Paths with constraints

Unlike the shortest path problem, which can be solved in polynomial time in graphs without negative cycles, shortest path problems which include additional constraints on the desired solution path are called Constrained Shortest Path First, and are harder to solve. One example is the constrained shortest path problem, which attempts to minimize the total cost of the path while at the same time maintaining another metric below a given threshold. This makes the problem NP-complete (such problems are not believed to be efficiently solvable for large sets of data, see P = NP problem). Another NP-complete example requires a specific set of vertices to be included in the path, which makes the problem similar to the Traveling Salesman Problem (TSP). The TSP is the problem of finding the shortest path that goes through every vertex exactly once, and returns to the start. The problem of finding the longest path in a graph is also NP-complete.

### Partial observability

The Canadian traveller problem and the stochastic shortest path problem are generalizations where either the graph is not completely known to the mover, changes over time, or where actions (traversals) are probabilistic.

### Strategic shortest paths

Sometimes, the edges in a graph have personalities: each edge has its own selfish interest. An example is a communication network, in which each edge is a computer that possibly belongs to a different person. Different computers have different transmission speeds, so every edge in the network has a numeric weight equal to the number of milliseconds it takes to transmit a message. Our goal is to send a message between two points in the network in the shortest time possible. If we know the transmission-time of each computer (the weight of each edge), then we can use a standard shortest-paths algorithm. If we do not know the transmission times, then we have to ask each computer to tell us its transmission-time. But, the computers may be selfish: a computer might tell us that its transmission time is very long, so that we will not bother it with our messages. A possible solution to this problem is to use a variant of the VCG mechanism, which gives the computers an incentive to reveal their true weights.

### Negative cycle detection

In some cases, the main goal is not to find the shortest path, but only to detect if the graph contains a negative cycle. Some shortest-paths algorithms can be used for this purpose:

- The Bellman–Ford algorithm can be used to detect a negative cycle in time $O(|V||E|)$ .
- Cherkassky and Goldberg survey several other algorithms for negative cycle detection.

## General algebraic framework on semirings: the algebraic path problem

Many problems can be framed as a form of the shortest path for some suitably substituted notions of addition along a path and taking the minimum. The general approach to these is to consider the two operations to be those of a semiring. Semiring multiplication is done along the path, and the addition is between paths. This general framework is known as the algebraic path problem.

Most of the classic shortest-path algorithms (and new ones) can be formulated as solving linear systems over such algebraic structures.

More recently, an even more general framework for solving these (and much less obviously related problems) has been developed under the banner of valuation algebras.

## Shortest path in stochastic time-dependent networks

In real-life, a transportation network is usually stochastic and time-dependent. The travel duration on a road segment depends on many factors such as the amount of traffic (origin-destination matrix), road work, weather, accidents and vehicle breakdowns. A more realistic model of such a road network is a stochastic time-dependent (STD) network.

There is no accepted definition of optimal path under uncertainty (that is, in stochastic road networks). It is a controversial subject, despite considerable progress during the past decade. One common definition is a path with the minimum expected travel time. The main advantage of this approach is that it can make use of efficient shortest path algorithms for deterministic networks. However, the resulting optimal path may not be reliable, because this approach fails to address travel time variability.

To tackle this issue, some researchers use travel duration distribution instead of its expected value. So, they find the probability distribution of total travel duration using different optimization methods such as dynamic programming and Dijkstra's algorithm . These methods use stochastic optimization, specifically stochastic dynamic programming to find the shortest path in networks with probabilistic arc length. The terms *travel time reliability* and *travel time variability* are used as opposites in the transportation research literature: the higher the variability, the lower the reliability of predictions.

To account for variability, researchers have suggested two alternative definitions for an optimal path under uncertainty. The *most reliable path* is one that maximizes the probability of arriving on time given a travel time budget. An *α-reliable path* is one that minimizes the travel time budget required to arrive on time with a given probability.
