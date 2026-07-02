---
title: "Convex polygon"
source: https://en.wikipedia.org/wiki/Convex_polygon
domain: rotating-calipers
license: CC-BY-SA-4.0
tags: rotating calipers, convex polygon width, antipodal pairs, polygon diameter
fetched: 2026-07-02
---

# Convex polygon

In geometry, a **convex polygon** is a polygon that is the boundary of a convex set. This means that the line segment between two points of the polygon is contained in the union of the interior and the boundary of the polygon. In particular, it is a simple polygon (not self-intersecting). Equivalently, a polygon is convex if every line that does not contain any edge intersects the polygon in at most two points.

## Strictly convex polygon

A convex polygon is *strictly* convex if no line contains more than two vertices of the polygon. In a convex polygon, all interior angles are less than *or equal* to 180 degrees, while in a strictly convex polygon all interior angles are strictly less than 180 degrees.

## Properties

The following properties of a simple polygon are all equivalent to convexity:

- Every internal angle is less than or equal to 180 degrees.
- Every point on every line segment between two points inside or on the boundary of the polygon remains inside or on the boundary.
- The polygon is entirely contained in a closed half-plane defined by each of its edges.
- For each edge, the interior points are all on the same side of the line that the edge defines.
- The angle at each vertex contains all other vertices in its edges and interior.
- The polygon is the convex hull of its edges.

Additional properties of convex polygons include:

- The intersection of two convex polygons is a convex polygon.
- A convex polygon may be triangulated in linear time through a fan triangulation, consisting in adding diagonals from one vertex to all other vertices.
- Helly's theorem: For every collection of at least three convex polygons: if all intersections of all but one polygon are nonempty, then the intersection of all the polygons is nonempty.
- Krein–Milman theorem: A convex polygon is the convex hull of its vertices. Thus it is fully defined by the set of its vertices, and one only needs the corners of the polygon to recover the entire polygon shape.
- Hyperplane separation theorem: Any two convex polygons with no points in common have a separator line. If the polygons are closed and at least one of them is compact, then there are even two parallel separator lines (with a gap between them).
- **Inscribed triangle** property: Of all triangles contained in a convex polygon, there exists a triangle with a maximal area whose vertices are all polygon vertices.
- **Inscribing triangle** property: every convex polygon with area A can be inscribed in a triangle of area at most equal to $2A$ . Equality holds (exclusively) for a parallelogram.
- **Inscribed/inscribing rectangles** property: For every convex body C in the plane, we can inscribe a rectangle r in C such that a homothetic copy R of r is circumscribed about C and the positive homothety ratio is at most 2 and $0.5{\text{ × Area}}(R)\leq {\text{Area}}(C)\leq 2{\text{ × Area}}(r)$ .
- The mean width of a convex polygon is equal to its perimeter divided by $\pi$ , thus the diameter of a circle with the same perimeter as the polygon.

Every polygon inscribed in a circle (such that all vertices of the polygon touch the circle), if not self-intersecting, is convex. However, not every convex polygon can be inscribed in a circle.

## Strict convexity

The following properties of a simple polygon are all equivalent to strict convexity:

- Every internal angle is strictly less than 180 degrees.
- Every line segment between two points in the interior, or between two points on the boundary but not on the same edge, is strictly interior to the polygon (except at its endpoints if they are on the edges).
- For each edge, the interior points and the boundary points not contained in the edge are on the same side of the line that the edge defines.
- The angle at each vertex contains all other vertices in its interior (except the given vertex and the two adjacent vertices).

Every non-degenerate triangle is strictly convex.
