---
title: "Handshaking lemma"
source: https://en.wikipedia.org/wiki/Handshaking_lemma
domain: eulerian-path-traversal
license: CC-BY-SA-4.0
tags: eulerian path, eulerian circuit, degree condition, bridge finding
fetched: 2026-07-02
---

# Handshaking lemma

In graph theory, the **handshaking lemma** is the statement that, in every finite undirected graph, the number of vertices that touch an odd number of edges is even. For example, if there is a party of people who shake hands, the number of people who shake an odd number of other people's hands is even. The handshaking lemma is a consequence of the **degree sum formula**, also sometimes called the handshaking lemma, according to which the sum of the degrees (the numbers of times each vertex is touched) equals twice the number of edges in the graph. Both results were proven by Leonhard Euler (1736) in his famous paper on the Seven Bridges of Königsberg that began the study of graph theory.

Beyond the Seven Bridges of Königsberg Problem, which subsequently formalized Eulerian Tours, other applications of the degree sum formula include proofs of certain combinatorial structures. For example, in the proofs of Sperner's lemma and the mountain climbing problem the geometric properties of the formula commonly arise. The complexity class PPA encapsulates the difficulty of finding a second odd vertex, given one such vertex in a large implicitly-defined graph.

## Definitions and statement

An undirected graph consists of a system of vertices, and edges connecting unordered pairs of vertices. In any graph, the degree $\deg(v)$ of a vertex v is defined as the number of edges that have v as an endpoint. For graphs that are allowed to contain loops connecting a vertex to itself, a loop should be counted as contributing two units to the degree of its endpoint for the purposes of the handshaking lemma. Then, the handshaking lemma states that, in every finite graph, there must be an even number of vertices for which $\deg(v)$ is an odd number. The vertices of odd degree in a graph are sometimes called **odd nodes** (or **odd vertices**); in this terminology, the handshaking lemma can be rephrased as the statement that every graph has an even number of odd nodes.

The degree sum formula states that $\sum _{v\in V}\deg v=2|E|,$ where V is the set of nodes (or vertices) in the graph and E is the set of edges in the graph. That is, the sum of the vertex degrees equals twice the number of edges. In directed graphs, another form of the degree-sum formula states that the sum of in-degrees of all vertices, and the sum of out-degrees, both equal the number of edges. Here, the in-degree is the number of incoming edges, and the out-degree is the number of outgoing edges. A version of the degree sum formula also applies to finite families of sets or, equivalently, multigraphs: the sum of the degrees of the elements (where the degree equals the number of sets containing it) always equals the sum of the cardinalities of the sets.

Both results also apply to any subgraph of the given graph and in particular to its connected components. A consequence is that, for any odd vertex, there must exist a path connecting it to another odd vertex.

## Applications

### Euler paths and tours

Schematic view of Königsberg's seven bridges

Graph with vertices for each land mass and an edge for each bridge

Leonhard Euler first proved the handshaking lemma in his work on the Seven Bridges of Königsberg, asking for a walking tour of the city of Königsberg (now Kaliningrad) crossing each of its seven bridges once. This can be translated into graph-theoretic terms as asking for an Euler path or Euler tour of a connected graph representing the city and its bridges: a walk through the graph that traverses each edge once, either ending at a different vertex than it starts in the case of an Euler path or returning to its starting point in the case of an Euler tour. Euler stated the fundamental results for this problem in terms of the number of odd vertices in the graph, which the handshaking lemma restricts to be an even number. If this number is zero, an Euler tour exists, and if it is two, an Euler path exists. Otherwise, the problem cannot be solved. In the case of the Seven Bridges of Königsberg, the graph representing the problem has four odd vertices, and has neither an Euler path nor an Euler tour. It was therefore impossible to tour all seven bridges in Königsberg without repeating a bridge.

In the Christofides–Serdyukov algorithm for approximating the traveling salesperson problem, the geometric implications of the degree sum formula plays a vital role, allowing the algorithm to connect vertices in pairs in order to construct a graph on which an Euler tour forms an approximate TSP tour.

### Combinatorial enumeration

Several combinatorial structures may be shown to be even in number by relating them to the odd vertices in an appropriate "exchange graph".

For instance, as C. A. B. Smith proved, in any cubic graph G there must be an even number of Hamiltonian cycles through any fixed edge $uv$ ; these are cycles that pass through each vertex exactly once. Thomason (1978) used a proof based on the handshaking lemma to extend this result to graphs in which all vertices have odd degree. Thomason defines an exchange graph H , the vertices of which are in one-to-one correspondence with the Hamiltonian paths in G beginning at u and continuing through edge $uv$ . Two such paths $p_{1}$ and $p_{2}$ are defined as being connected by an edge in H if one may obtain $p_{2}$ by adding a new edge to the end of $p_{1}$ and removing another edge from the middle of $p_{1}$ . This operation is reversible, forming a symmetric relation, so H is an undirected graph. If path p ends at vertex w , then the vertex corresponding to p in H has degree equal to the number of ways that p may be extended by an edge that does not connect back to u ; that is, the degree of this vertex in H is either $\deg(w)-1$ (an even number) if p does not form part of a Hamiltonian cycle through $uv$ , or $\deg(w)-2$ (an odd number) if p is part of a Hamiltonian cycle through $uv$ . Since H has an even number of odd vertices, G must have an even number of Hamiltonian cycles through $uv$ .

### Other applications

The handshaking lemma (or degree sum formula) are also used in proofs of several other results in mathematics. These include the following:

- Sperner's lemma states that, if a big triangle is subdivided into smaller triangles meeting edge-to-edge, and the vertices are labeled with three colors so that only two of the colors are used along each edge of the big triangle, then at least one of the smaller triangles has vertices of all three colors; it has applications in fixed-point theorems, root-finding algorithms, and fair division. One proof of this lemma forms an exchange graph whose vertices are the triangles (both small and large) and whose edges connect pairs of triangles that share two vertices of some particular two colors. The big triangle necessarily has odd degree in this exchange graph, as does a small triangle with all three colors, but not the other small triangles. By the handshaking lemma, there must be an odd number of small triangles with all three colors, and therefore at least one such triangle must exist.

- The mountain climbing problem states that, for sufficiently well-behaved functions on a unit interval, with equal values at the ends of the interval, it is possible to coordinate the motion of two points, starting from opposite ends of the interval, so that they meet somewhere in the middle while remaining at points of equal value throughout the motion. One proof of this involves approximating the function by a piecewise linear function with the same extreme points, parameterizing the position of the two moving points by the coordinates of a single point in the unit square, and showing that the available positions for the two points form a finite graph, embedded in this square, with only the starting position and its reversal as odd vertices. By the handshaking lemma, these two positions belong to the same connected component of the graph, and a path from one to the other necessarily passes through the desired meeting point.
- The reconstruction conjecture concerns the problem of uniquely determining the structure of a graph from the multiset of subgraphs formed by removing a single vertex from it. Given this information, the degree-sum formula can be used to recover the number of edges in the given graph and the degrees of each vertex. From this, it is possible to determine whether the given graph is a regular graph, and if so to determine it uniquely from any vertex-deleted subgraph by adding a new neighbor for all the subgraph vertices of too-low degree. Therefore, all regular graphs can be reconstructed.
- The game of Hex is played by two players, who place pieces of their color on a tiling of a parallelogram-shaped board by hexagons until one player has a connected path of adjacent pieces from one side of the board to the other. It can never end in a draw: by the time the board has been completely filled with pieces, one of the players will have formed a winning path. One proof of this forms a graph from a filled game board, with vertices at the corners of the hexagons, and with edges on sides of hexagons that separate the two players' colors. This graph has four odd vertices at the corners of the board, and even vertices elsewhere, so it must contain a path connecting two corners, which necessarily has a winning path for one player on one of its sides.

## Proof

Euler's proof of the degree sum formula uses the technique of double counting: he counts the number of incident pairs $(v,e)$ where e is an edge and vertex v is one of its endpoints, in two different ways. Vertex v belongs to $\deg(v)$ pairs, where $\deg(v)$ (the degree of v ) is the number of edges incident to it. Therefore, the number of incident pairs is the sum of the degrees. However, each edge in the graph belongs to exactly two incident pairs, one for each of its endpoints; therefore, the number of incident pairs is $2|E|$ . Since these two formulas count the same set of objects, they must have equal values. The same proof can be interpreted as summing the entries of the incidence matrix of the graph in two ways, by rows to get the sum of degrees and by columns to get twice the number of edges.

For graphs, the handshaking lemma follows as a corollary of the degree sum formula. In a sum of integers, the parity of the sum is not affected by the even terms in the sum; the overall sum is even when there is an even number of odd terms, and odd when there is an odd number of odd terms. Since one side of the degree sum formula is the even number $2|E|$ , the sum on the other side must have an even number of odd terms; that is, there must be an even number of odd-degree vertices.

Alternatively, it is possible to use mathematical induction to prove the degree sum formula, or to prove directly that the number of odd-degree vertices is even, by removing one edge at a time from a given graph and using a case analysis on the degrees of its endpoints to determine the effect of this removal on the parity of the number of odd-degree vertices.

## In special classes of graphs

The

Clebsch graph

, regular of degree five, has an even number of vertices (16) and a number of edges (40) that is a multiple of five.

The

rhombic dodecahedron

is

biregular

with six vertices of degree four and eight vertices of degree three;

6 × 4 = 8 × 3 = 24

, its number of edges.

### Regular graphs

The degree sum formula implies that every r -regular graph with n vertices has $nr/2$ edges. Because the number of edges must be an integer, it follows that when r is odd the number of vertices must be even. Additionally, for odd values of r , the number of edges must be divisible by r .

### Bipartite and biregular graphs

A bipartite graph has its vertices split into two subsets, with each edge having one endpoint in each subset. It follows from the same double counting argument that, in each subset, the sum of degrees equals the number of edges in the graph. In particular, both subsets have equal degree sums. For biregular graphs, with a partition of the vertices into subsets $V_{1}$ and $V_{2}$ with every vertex in a subset $V_{i}$ having degree $r_{i}$ , it must be the case that $|V_{1}|r_{1}=|V_{2}|r_{2}$ ; both equal the number of edges.

### Infinite graphs

The handshaking lemma does not apply in its usual form to infinite graphs, even when they have only a finite number of odd-degree vertices. For instance, an infinite path graph with one endpoint has only a single odd-degree vertex rather than having an even number of such vertices. However, it is possible to formulate a version of the handshaking lemma using the concept of an end, an equivalence class of semi-infinite paths ("rays") considering two rays as equivalent when there exists a third ray that uses infinitely many vertices from each of them. The degree of an end is the maximum number of edge-disjoint rays that it contains, and an end is odd if its degree is finite and odd. More generally, it is possible to define an end as being odd or even, regardless of whether it has infinite degree, in graphs for which all vertices have finite degree. Then, in such graphs, the number of odd vertices and odd ends, added together, is either even or infinite.

### Subgraphs

By a theorem of Gallai the vertices of any graph can be partitioned as $V=V_{e}\cup V_{o}$ where in the two resulting induced subgraphs, $G[V_{e}]$ has all degrees even and $G[V_{o}]$ has all degrees odd. Here, $|V_{o}|$ must be even by the handshaking lemma. It is also possible to find even-degree and odd-degree induced subgraphs with many vertices. An induced subgraph of even degree can be found with at least half of the vertices, and an induced subgraph of odd degree (in a graph with no isolated vertices) can be found with $|V_{o}|/|V|>1/10000$ .

## Computational complexity

In connection with the exchange graph method for proving the existence of combinatorial structures, it is of interest to ask how efficiently these structures may be found. For instance, suppose one is given as input a Hamiltonian cycle in a cubic graph; it follows from Smith's theorem that there exists a second cycle. How quickly can this second cycle be found? Papadimitriou (1994) investigated the computational complexity of questions such as this, or more generally of finding a second odd-degree vertex when one is given a single odd vertex in a large implicitly-defined graph. He defined the complexity class PPA to encapsulate problems such as this one; a closely related class defined on directed graphs, PPAD, has attracted significant attention in algorithmic game theory because computing a Nash equilibrium is computationally equivalent to the hardest problems in this class.

Computational problems proven to be complete for the complexity class PPA include computational tasks related to Sperner's lemma and to fair subdivision of resources according to the Hobby–Rice theorem.
