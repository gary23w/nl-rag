---
title: "Monotone polygon"
source: https://en.wikipedia.org/wiki/Monotone_polygon
domain: polygon-triangulation
license: CC-BY-SA-4.0
tags: polygon triangulation, ear clipping, monotone polygon, trapezoid decomposition
fetched: 2026-07-02
---

# Monotone polygon

In geometry, a polygon P in the plane is called **monotone** with respect to a straight line L, if every line orthogonal to L intersects the boundary of P at most twice.

Similarly, a polygonal chain C is called **monotone** with respect to a straight line L, if every line orthogonal to L intersects C at most once.

For many practical purposes this definition may be extended to allow cases when some edges of P are orthogonal to L, and a simple polygon may be called monotone if a line segment that connects two points in P and is orthogonal to L lies completely in P.

Following the terminology for monotone functions, the former definition describes **polygons strictly monotone** with respect to L.

## Properties

Assume that *L* coincides with the *x*-axis. Then the leftmost and rightmost vertices of a monotone polygon decompose its boundary into two monotone polygonal chains such that when the vertices of any chain are being traversed in their natural order, their X-coordinates are monotonically increasing or decreasing. In fact, this property may be taken for the definition of monotone polygon and it gives the polygon its name.

A convex polygon is monotone with respect to any straight line and a polygon which is monotone with respect to every straight line is convex.

A linear time algorithm is known to report all directions in which a given simple polygon is monotone. It was generalized to report all ways to decompose a simple polygon into two monotone chains (possibly monotone in different directions.)

Point in polygon queries with respect to a monotone polygon may be answered in logarithmic time after linear time preprocessing (to find the leftmost and rightmost vertices).

A monotone polygon may be easily triangulated in linear time.

For a given set of points in the plane, a bitonic tour is a monotone polygon that connects the points. The minimum perimeter bitonic tour for a given point set with respect to a fixed direction may be found in polynomial time using dynamic programming. It is easily shown that such a minimal bitonic tour is a simple polygon: a pair of crossing edges may be replaced with a shorter non-crossing pair while preserving the bitonicity of the new tour.

A simple polygon may be easily cut into monotone polygons in *O*(*n* log *n*) time. However, since a triangle is a monotone polygon, polygon triangulation is in fact cutting a polygon into monotone ones, and it may be performed for simple polygons in *O*(*n*) time with a complex algorithm. A simpler randomized algorithm with linear expected time is also known.

Cutting a simple polygon into the minimal number of uniformly monotone polygons (i.e., monotone with respect to the same line) can be performed in polynomial time.

In the context of motion planning, two nonintersecting monotone polygons are separable by a single translation (i.e., there exists a translation of one polygon such that the two become separated by a straight line into different halfplanes) and this separation may be found in linear time.

## Generalizations

### Sweepable polygons

A polygon is called **sweepable**, if a straight line may be continuously moved over the whole polygon in such a way that at any moment its intersection with the polygonal area is a convex set. A monotone polygon is sweepable by a line which does not change its orientation during the sweep. A polygon is **strictly sweepable** if no portion of its area is swept more than once. Both types of sweepability are recognized in quadratic time.

### 3D

There is no single straightforward generalization of polygon monotonicity to higher dimensions.

In one approach the preserved monotonicity trait is the line *L*. A three-dimensional polyhedron is called **weakly monotonic** in direction *L* if all cross-sections orthogonal to *L* are simple polygons. If the cross-sections are convex, then the polyhedron is called **weakly monotonic in convex sense**. Both types may be recognized in polynomial time.

In another approach the preserved one-dimensional trait is the orthogonal direction. This gives rise for the notion of polyhedral terrain in three dimensions: a polyhedral surface with the property that each vertical (i.e., parallel to Z axis) line intersects the surface at most by one point or segment.
