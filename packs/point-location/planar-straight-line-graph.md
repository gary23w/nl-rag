---
title: "Planar straight-line graph"
source: https://en.wikipedia.org/wiki/Planar_straight-line_graph
domain: point-location
license: CC-BY-SA-4.0
tags: point location, planar subdivision, trapezoidal decomposition, slab method
fetched: 2026-07-02
---

# Planar straight-line graph

In computational geometry and geometric graph theory, a **planar straight-line graph** (**PSLG**), also called a **straight-line plane graph** or **plane straight-line graph**, is an embedding of a planar graph in the plane such that its edges are mapped into straight-line segments. Fáry's theorem (1948) states that every planar graph has this kind of embedding.

In computational geometry, PSLGs have often been called **planar subdivisions**, with an assumption or assertion that subdivisions are polygonal rather than having curved boundaries.

PSLGs may serve as representations of various maps, e.g., geographical maps in geographical information systems.

Special cases of PSLGs are triangulations (polygon triangulation, point-set triangulation). Point-set triangulations are maximal PSLGs in the sense that it is impossible to add straight edges to them while keeping the graph planar. Triangulations have numerous applications in various areas.

PSLGs may be seen as a special kind of Euclidean graphs. However, in discussions involving Euclidean graphs, the primary interest is their metric properties, i.e., distances between vertices, while for PSLGs the primary interest is the topological properties. For some graphs, such as Delaunay triangulations, both metric and topological properties are of importance.

## Representations

There exist three well-known data structures for representing PSLGs, these are the Winged-edge data structure, Halfedge, and Quadedge. The winged-edge data structure is the oldest of the three, but manipulating it often requires complicated case distinctions. This is because edge references do not store the edge direction, and the directions of edges around a face need not be consistent. The halfedge data structure stores both orientations of an edge and links them properly, simplifying operations and the storage scheme. The Quadedge data structure stores both the planar subdivision and its dual simultaneously. Its records consist explicitly only of edge records, four for each edge, and in a simplified form it is suitable for storing PSLGs.

## Problems in terms of PSLG

- Point location. For a query point, find which face of the PSLG it belongs to.
- Map overlay. Find the overlay of two PSLGs (maps), which is the subdivision of the plane by the two simultaneously embedded PSLGs. In GIS this problem is known as "thematic map overlay".
