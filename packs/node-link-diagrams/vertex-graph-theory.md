---
title: "Vertex (graph theory)"
source: https://en.wikipedia.org/wiki/Vertex_(graph_theory)
domain: node-link-diagrams
license: CC-BY-SA-4.0
tags: node link, tree structure, influence diagram, vertex edge
fetched: 2026-07-02
---

# Vertex (graph theory)

In discrete mathematics, and more specifically in graph theory, a **vertex** (plural **vertices**) or **node** is the fundamental unit of which graphs are formed: an undirected graph consists of a set of vertices and a set of edges (unordered pairs of vertices), while a directed graph consists of a set of vertices and a set of arcs (ordered pairs of vertices). In a diagram of a graph, a vertex is usually represented by a circle with a label, and an edge is represented by a line or arrow extending from one vertex to another.

From the point of view of graph theory, vertices are treated as featureless and indivisible objects, although they may have additional structure depending on the application from which the graph arises; for instance, a semantic network is a graph in which the vertices represent concepts or classes of objects.

The two vertices forming an edge are said to be the endpoints of this edge, and the edge is said to be incident to the vertices. A vertex *w* is said to be adjacent to another vertex *v* if the graph contains an edge (*v*,*w*). The neighborhood of a vertex *v* is an induced subgraph of the graph, formed by all vertices adjacent to *v*.

## Types of vertices

The degree of a vertex, denoted 𝛿(v) in a graph is the number of edges incident to it. An **isolated vertex** is a vertex with degree zero; that is, a vertex that is not an endpoint of any edge (the example image illustrates one isolated vertex). A **leaf vertex** (also **pendant vertex**) is a vertex with degree one. In a directed graph, one can distinguish the outdegree (number of outgoing edges), denoted 𝛿 +(v), from the indegree (number of incoming edges), denoted 𝛿−(v); a **source vertex** is a vertex with indegree zero, while a **sink vertex** is a vertex with outdegree zero. A simplicial vertex is one whose closed neighborhood forms a clique: every two neighbors are adjacent. A universal vertex is a vertex that is adjacent to every other vertex in the graph.

A cut vertex is a vertex the removal of which would disconnect the remaining graph; a vertex separator is a collection of vertices the removal of which would disconnect the remaining graph into small pieces. A k-vertex-connected graph is a graph in which removing fewer than *k* vertices always leaves the remaining graph connected. An independent set is a set of vertices no two of which are adjacent, and a vertex cover is a set of vertices that includes at least one endpoint of each edge in the graph. The vertex space of a graph is a vector space having a set of basis vectors corresponding with the graph's vertices.

A graph is vertex-transitive if it has symmetries that map any vertex to any other vertex. In the context of graph enumeration and graph isomorphism it is important to distinguish between **labeled vertices** and **unlabeled vertices**. A labeled vertex is a vertex that is associated with extra information that enables it to be distinguished from other labeled vertices; two graphs can be considered isomorphic only if the correspondence between their vertices pairs up vertices with equal labels. An unlabeled vertex is one that can be substituted for any other vertex based only on its adjacencies in the graph and not based on any additional information.

Vertices in graphs are analogous to, but not the same as, vertices of polyhedra: the skeleton of a polyhedron forms a graph, the vertices of which are the vertices of the polyhedron, but polyhedron vertices have additional structure (their geometric location) that is not assumed to be present in graph theory. The vertex figure of a vertex in a polyhedron is analogous to the neighborhood of a vertex in a graph.
