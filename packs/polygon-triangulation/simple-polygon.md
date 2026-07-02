---
title: "Simple polygon"
source: https://en.wikipedia.org/wiki/Simple_polygon
domain: polygon-triangulation
license: CC-BY-SA-4.0
tags: polygon triangulation, ear clipping, monotone polygon, trapezoid decomposition
fetched: 2026-07-02
---

# Simple polygon

In geometry, a **simple polygon** is a polygon that does not intersect itself and has no holes. That is, it is a piecewise-linear Jordan curve consisting of finitely many line segments. These polygons include as special cases the convex polygons, star-shaped polygons, and monotone polygons.

The sum of external angles of a simple polygon is $2\pi$ . Every simple polygon with n sides can be triangulated by $n-3$ of its diagonals, and by the art gallery theorem its interior is visible from some $\lfloor n/3\rfloor$ of its vertices.

Simple polygons are commonly seen as the input to computational geometry problems, including point in polygon testing, area computation, the convex hull of a simple polygon, triangulation, and Euclidean shortest paths.

Other constructions in geometry related to simple polygons include Schwarz–Christoffel mapping, used to find conformal maps involving simple polygons, polygonalization of point sets, constructive solid geometry formulas for polygons, and visibility graphs of polygons.

## Definitions

A simple polygon is a closed curve in the Euclidean plane consisting of straight line segments, meeting end-to-end to form a polygonal chain. Two line segments meet at every endpoint, and there are no other points of intersection between the line segments. No proper subset of the line segments has the same properties. The qualifier *simple* is sometimes omitted, with the word *polygon* assumed to mean a simple polygon.

The line segments that form a polygon are called its *edges* or *sides*. An endpoint of a segment is called a *vertex* (plural: vertices) or a *corner*. *Edges* and *vertices* are more formal, but may be ambiguous in contexts that also involve the edges and vertices of a graph; the more colloquial terms *sides* and *corners* can be used to avoid this ambiguity. The number of edges always equals the number of vertices. Some sources allow two line segments to form a straight angle (180°), while others disallow this, instead requiring collinear segments of a closed polygonal chain to be merged into a single longer side. Two vertices are *neighbors* if they are the two endpoints of one of the sides of the polygon.

Simple polygons are sometimes called **Jordan polygons**, because they are Jordan curves; the Jordan curve theorem can be used to prove that such a polygon divides the plane into two regions. Indeed, Camille Jordan's original proof of this theorem took the special case of simple polygons (stated without proof) as its starting point. The region inside the polygon (its *interior*) forms a bounded set topologically equivalent to an open disk by the Jordan–Schönflies theorem, with a finite but nonzero area. The polygon itself is topologically equivalent to a circle, and the region outside (the *exterior*) is an unbounded connected open set, with infinite area. Although the formal definition of a simple polygon is typically as a system of line segments, it is also possible (and common in informal usage) to define a simple polygon as a closed set in the plane, the union of these line segments with the interior of the polygon.

A *diagonal* of a simple polygon is any line segment that has two polygon vertices as its endpoints, and that otherwise is entirely interior to the polygon.

## Properties

The *internal angle* of a simple polygon, at one of its vertices, is the angle spanned by the interior of the polygon at that vertex. A vertex is *convex* if its internal angle is less than $\pi$ (a straight angle, 180°) and *concave* if the internal angle is greater than $\pi$ . If the internal angle is $\theta$ , the *external angle* at the same vertex is defined to be its supplement $\pi -\theta$ , the turning angle from one directed side to the next. The external angle is positive at a convex vertex or negative at a concave vertex. For every simple polygon, the sum of the external angles is $2\pi$ (one full turn, 360°). Thus the sum of the internal angles, for a simple polygon with n sides is $(n-2)\pi$ .

Every simple polygon can be partitioned into non-overlapping triangles by a subset of its diagonals. When the polygon has n sides, this produces $n-2$ triangles, separated by $n-3$ diagonals. The resulting partition is called a *polygon triangulation*. The shape of a triangulated simple polygon can be uniquely determined by the internal angles of the polygon and by the cross-ratios of the quadrilaterals formed by pairs of triangles that share a diagonal.

According to the two ears theorem, every simple polygon that is not a triangle has at least two *ears*, vertices whose two neighbors are the endpoints of a diagonal. A related theorem states that every simple polygon that is not a convex polygon has a *mouth*, a vertex whose two neighbors are the endpoints of a line segment that is otherwise entirely exterior to the polygon. The polygons that have exactly two ears and one mouth are called *anthropomorphic polygons*.

According to the art gallery theorem, in a simple polygon with n vertices, it is always possible to find a subset of at most $\lfloor n/3\rfloor$ of the vertices with the property that every point in the polygon is visible from one of the selected vertices. This means that, for each point p in the polygon, there exists a line segment connecting p to a selected vertex, passing only through interior points of the polygon. One way to prove this is to use graph coloring on a triangulation of the polygon: it is always possible to color the vertices with three colors, so that each side or diagonal in the triangulation has two endpoints of different colors. Each point of the polygon is visible to a vertex of each color, for instance one of the three vertices of the triangle containing that point in the chosen triangulation. One of the colors is used by at most $\lfloor n/3\rfloor$ of the vertices, proving the theorem.

## Special cases

Every convex polygon is a simple polygon. Another important class of simple polygons are the star-shaped polygons, the polygons that have a point (interior or on their boundary) from which every point is visible.

A monotone polygon, with respect to a straight line L , is a polygon for which every line perpendicular to L intersects the interior of the polygon in a connected set. Equivalently, it is a polygon whose boundary can be partitioned into two monotone polygonal chains, subsequences of edges whose vertices, when projected perpendicularly onto L , have the same order along L as they do in the chain.

## Computational problems

In computational geometry, several important computational tasks involve inputs in the form of a simple polygon.

- Point in polygon testing involves determining, for a simple polygon P and a query point q , whether q lies interior to P . It can be solved in linear time; alternatively, it is possible to process a given polygon into a data structure, in linear time, so that subsequent point in polygon tests can be performed in logarithmic time.
- Simple formulae are known for computing the area of the interior of a polygon. These include the shoelace formula for arbitrary polygons, and Pick's theorem for polygons with integer vertex coordinates.
- The convex hull of a simple polygon can also be found in linear time, faster than algorithms for finding convex hulls of points that have not been connected into a polygon.
- Constructing a triangulation of a simple polygon can also be performed in linear time, although the algorithm is complicated. A modification of the same algorithm can also be used to test whether a closed polygonal chain forms a simple polygon (that is, whether it avoids self-intersections) in linear time. This also leads to a linear time algorithm for solving the art gallery problem using at most $\lfloor n/3\rfloor$ points, although not necessarily using the optimal number of points for a given polygon. Although it is possible to transform any two triangulations of the same polygon into each other by flips that replace one diagonal at a time, determining whether one can do so using only a limited number of flips is NP-complete.
- A geodesic path, the shortest path in the plane that connects two points interior to a polygon, without crossing to the exterior, may be found in linear time by an algorithm that uses triangulation as a subroutine. The same is true for the *geodesic center*, a point in the polygon that minimizes the maximum length of its geodesic paths to all other points.
- The visibility polygon of an interior point of a simple polygon, the points that are directly visible from the given point by line segments interior to the polygon, can be constructed in linear time. The same is true for the subset that is visible from at least one point of a given line segment.

Other computational problems studied for simple polygons include constructions of the longest diagonal or the longest line segment interior to a polygon, of the convex skull (the largest convex polygon within the given simple polygon), and of various one-dimensional *skeletons* approximating its shape, including the medial axis and straight skeleton. Researchers have also studied producing other polygons from simple polygons using their offset curves, unions and intersections, and Minkowski sums, but these operations do not always produce a simple polygon as their result. They can be defined in a way that always produces a two-dimensional region, but this requires careful definitions of the intersection and difference operations in order to avoid creating one-dimensional features or isolated points.

According to the Riemann mapping theorem, any simply connected open subset of the plane can be conformally mapped onto a disk. Schwarz–Christoffel mapping provides a method to explicitly construct a map from a disk to any simple polygon using specified vertex angles and pre-images of the polygon vertices on the boundary of the disk. These *pre-vertices* are typically computed numerically.

Every finite set of points in the plane that does not lie on a single line can be connected to form the vertices of a simple polygon (allowing 180° angles); for instance, one such polygon is the solution to the traveling salesperson problem. Connecting points to form a polygon in this way is called polygonalization.

Every simple polygon can be represented by a formula in constructive solid geometry that constructs the polygon (as a closed set including the interior) from unions and intersections of half-planes, with each side of the polygon appearing once as a half-plane in the formula. Converting an n -sided polygon into this representation can be performed in time $O(n\log n)$ .

The visibility graph of a simple polygon connects its vertices by edges representing the sides and diagonals of the polygon. It always contains a Hamiltonian cycle, formed by the polygon sides. The computational complexity of reconstructing a polygon that has a given graph as its visibility graph, with a specified Hamiltonian cycle as its cycle of sides, remains an open problem.
