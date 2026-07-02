---
title: "Doubly connected edge list"
source: https://en.wikipedia.org/wiki/Doubly_connected_edge_list
domain: mesh-connectivity-structure
license: CC-BY-SA-4.0
tags: half-edge mesh, winged edge, quad-edge, doubly connected edge list
fetched: 2026-07-02
---

# Doubly connected edge list

The **doubly connected edge list** (**DCEL**), also known as **half-edge data structure**, is a data structure to represent an embedding of a planar graph in the plane, and polytopes in 3D. This data structure provides efficient manipulation of the topological information associated with the objects in question (vertices, edges, faces). It is used in many algorithms of computational geometry to handle polygonal subdivisions of the plane, commonly called planar straight-line graphs (PSLG). For example, a Voronoi diagram is commonly represented by a DCEL inside a bounding box.

This data structure was originally suggested by Muller and Preparata for representations of 3D convex polyhedra. Simplified versions of the data structure, as described here, only consider connected graphs, but the DCEL structure may be extended to handle disconnected graphs as well by introducing dummy edges between disconnected components.

## Data structure

DCEL is more than just a doubly linked list of edges. In the general case, a DCEL contains a record for each edge, vertex and face of the subdivision. Each record may contain additional information, for example, a face may contain the name of the area. Each edge usually bounds two faces and it is, therefore, convenient to regard each edge as two "half-edges" (which are represented by the two edges with opposite directions, between two vertices, in the picture on the right). Each half-edge is "associated" with a single face and thus has a pointer to that face. *All* half-edges associated with a face are clockwise or counter-clockwise. For example, in the picture on the right, all half-edges associated with the middle face (i.e. the "internal" half-edges) are counter-clockwise. A half-edge has a pointer to the next half-edge and previous half-edge of the same face. To reach the other face, we can go to the twin of the half-edge and then traverse the other face. Each half-edge also has a pointer to its origin vertex (the destination vertex can be obtained by querying the origin of its twin, or of the next half-edge).

Each vertex contains the coordinates of the vertex and also stores a pointer to an arbitrary edge that has the vertex as its origin. Each face stores a pointer to some half-edge of its outer boundary (if the face is unbounded then pointer is null). It also has a list of half-edges, one for each hole that may be incident within the face. If the vertices or faces do not hold any interesting information, there is no need to store them, thus saving space and reducing the data structure's complexity.
