---
title: "Pitteway triangulation"
source: https://en.wikipedia.org/wiki/Pitteway_triangulation
domain: delaunay-triangulation-algo
license: CC-BY-SA-4.0
tags: delaunay triangulation, bowyer watson algorithm, empty circle, constrained delaunay
fetched: 2026-07-02
---

# Pitteway triangulation

In computational geometry, a **Pitteway triangulation** is a point set triangulation in which the nearest neighbor of any point *p* within the triangulation is one of the vertices of the triangle containing *p*. Alternatively, it is a Delaunay triangulation in which each internal edge crosses its dual Voronoi diagram edge. Pitteway triangulations are named after Michael Pitteway, who studied them in 1973. Not every point set supports a Pitteway triangulation. When such a triangulation exists it is a special case of the Delaunay triangulation, and consists of the union of the Gabriel graph and convex hull.

## History

The concept of a Pitteway triangulation was introduced by Pitteway (1973). See also McLain (1976), who writes "An optimal partition is one in which, for any point within any triangle, that point lies at least as close to one of the vertices of that triangle as to any other data point." The name "Pitteway triangulation" was given by Okabe et al. (2000).

## Counterexamples

Gold (1978) points out that not every point set supports a Pitteway triangulation. For instance, any triangulation of a regular pentagon includes a central isosceles triangle such that a point *p* near the midpoint of one of the triangle sides has its nearest neighbor outside the triangle.

## Relation to other geometric graphs

When a Pitteway triangulation exists, the midpoint of each edge interior to the triangulation must have the two edge endpoints as its nearest neighbors, for any other neighbor would violate the Pitteway property for nearby points in one of the two adjacent triangles. Thus, a circle having that edge as diameter must be empty of vertices, so the Pitteway triangulation consists of the Gabriel graph together with the convex hull of the point set. Conversely, when the Gabriel graph and convex hull together form a triangulation, it is a Pitteway triangulation.

Since all Gabriel graph and convex hull edges are part of the Delaunay triangulation, a Pitteway triangulation, when it exists, is unique for points in general position and coincides with the Delaunay triangulation. However, point sets with no Pitteway triangulation will still have a Delaunay triangulation.

In the Pitteway triangulation, each edge *pq* either belongs to the convex hull or crosses the edge of the Voronoi diagram that separates the cells containing *p* and *q*. In some references this property is used to define a Pitteway triangulation, as a Delaunay triangulation in which all internal Delaunay edges cross their dual Voronoi edges. However, a Pitteway triangulation may include convex hull edges that do not cross their duals.
