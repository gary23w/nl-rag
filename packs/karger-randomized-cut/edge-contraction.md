---
title: "Edge contraction"
source: https://en.wikipedia.org/wiki/Edge_contraction
domain: karger-randomized-cut
license: CC-BY-SA-4.0
tags: karger algorithm, randomized min cut, edge contraction, monte carlo method
fetched: 2026-07-02
---

# Edge contraction

In graph theory, an **edge contraction** is an operation that removes an edge from a graph while simultaneously merging the two vertices that it previously joined. Edge contraction is a fundamental operation in the theory of graph minors. **Vertex identification** is a less restrictive form of this operation.

## Definition

The **edge contraction** operation occurs relative to a particular edge, e . The edge e is removed and its two incident vertices, u and v , are merged into a new vertex w , where the edges incident to w each correspond to an edge incident to either u or v . More generally, the operation may be performed on a set of edges by contracting each edge (in any order).

The resulting graph is sometimes written as $G/e$ . (Contrast this with $G\setminus e$ , which means simply removing the edge e without merging its incident vertices.)

As defined below, an edge contraction operation may result in a graph with multiple edges even if the original graph was a simple graph. However, some authors disallow the creation of multiple edges, so that edge contractions performed on simple graphs always produce simple graphs.

### Formal definition

Let $G=(V,E)$ be a graph (*or directed graph*) containing an edge $e=(u,v)$ with $u\neq v$ . Let f be a function that maps every vertex in $V\setminus \{u,v\}$ to itself, and otherwise, maps it to a new vertex w . The contraction of e results in a new graph $G'=(V',E')$ , where $V'=(V\setminus \{u,v\})\cup \{w\}$ , $E'=E\setminus \{e\}$ , and for every $x\in V$ , $x'=f(x)\in V'$ is incident to an edge $e'\in E'$ if and only if, the corresponding edge, $e\in E$ is incident to x in G .

### Vertex identification

**Vertex identification** (sometimes called **vertex contraction**) removes the restriction that the *contraction* must occur over vertices sharing an incident edge. (Thus, edge contraction is a special case of vertex identification.) The operation may occur on any pair (or subset) of vertices in the graph. Edges between two *contracting* vertices are sometimes removed. If v and $v'$ are vertices of distinct components of G , then we can create a new graph $G'$ by identifying v and $v'$ in G as a new vertex ${\textbf {v}}$ in $G'$ . More generally, given a partition of the vertex set, one can identify vertices in the partition; the resulting graph is known as a quotient graph.

### Vertex cleaving

**Vertex cleaving**, which is the same as vertex splitting, means one vertex is being split into two, where these two new vertices are adjacent to the vertices that the original vertex was adjacent to. This is a reverse operation of vertex identification, although in general for vertex identification, adjacent vertices of the two identified vertices are not the same set.

### Path contraction

**Path contraction** occurs upon the set of edges in a path that *contract* to form a single edge between the endpoints of the path. Edges incident to vertices along the path are either eliminated, or arbitrarily (or systematically) connected to one of the endpoints.

### Twisting

Consider two disjoint graphs $G_{1}$ and $G_{2}$ , where $G_{1}$ contains vertices $u_{1}$ and $v_{1}$ and $G_{2}$ contains vertices $u_{2}$ and $v_{2}$ . Suppose we can obtain the graph G by identifying the vertices $u_{1}$ of $G_{1}$ and $u_{2}$ of $G_{2}$ as the vertex u of G and identifying the vertices $v_{1}$ of $G_{1}$ and $v_{2}$ of $G_{2}$ as the vertex v of G . In a *twisting* $G'$ of G with respect to the vertex set $\{u,v\}$ , we identify, instead, $u_{1}$ with $v_{2}$ and $v_{1}$ with $u_{2}$ .

### Repeated contractions

Given a finite set of edges, the order in which contractions are performed on a graph does not change the result (up to isomorphism). The result reduces to showing that $G/e/(f/e)$ is isomorphic to $G/f/(e/f)$ for two edges $e,f$ of G .

## Applications

Both edge and vertex contraction techniques are valuable in proof by induction on the number of vertices or edges in a graph, where it can be assumed that a property holds for all smaller graphs and this can be used to prove the property for the larger graph.

Edge contraction is used in the recursive formula for the number of spanning trees of an arbitrary connected graph, and in the recurrence formula for the chromatic polynomial of a simple graph.

Contractions are also useful in structures where we wish to simplify a graph by identifying vertices that represent essentially equivalent entities. One of the most common examples is the reduction of a general directed graph to an acyclic directed graph by contracting all of the vertices in each strongly connected component. If the relation described by the graph is transitive, no information is lost as long as we label each vertex with the set of labels of the vertices that were contracted to form it.

Another example is the coalescing performed in global graph coloring register allocation, where vertices are contracted (where it is safe) in order to eliminate move operations between distinct variables.

Edge contraction is used in 3D modelling packages (either manually, or through some feature of the modelling software) to consistently reduce vertex count, aiding in the creation of low-polygon models.
