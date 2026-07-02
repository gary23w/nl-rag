---
title: "Fan triangulation"
source: https://en.wikipedia.org/wiki/Fan_triangulation
domain: polygon-triangulation
license: CC-BY-SA-4.0
tags: polygon triangulation, ear clipping, monotone polygon, trapezoid decomposition
fetched: 2026-07-02
---

# Fan triangulation

In computational geometry, a **fan triangulation** is a simple way to triangulate a polygon by choosing a vertex and drawing edges to all of the other vertices of the polygon. Not every polygon can be triangulated this way, so this method is usually only used for convex polygons.

## Properties

Aside from the properties of all triangulations, fan triangulations have the following properties:

- All convex polygons, but not all polygons, can be fan triangulated.
- Polygons with only one concave vertex can always be fan triangulated, as long as the diagonals are drawn from the concave vertex.
- It can be known if a polygon can be fan triangulated by solving the art gallery problem, in order to determine whether there is at least one vertex that is visible from every point in the polygon.
- The triangulation of a polygon with n vertices uses $n-3$ diagonals, and generates $n-2$ triangles.
- Generating the list of triangles is trivial if an ordered list of vertices is available, and can be computed in linear time. As such, it is unnecessary to explicitly store the list of triangles, and therefore, many graphical libraries implement primitives to represent polygons based on this triangulation.
- Although this triangulation is fit for solving certain problems, such as rasterisation, or collision detection, it may be unfit for other tasks because the origin vertex accumulates a high number of neighbors, and the internal angles of the triangulation are unevenly distributed.
