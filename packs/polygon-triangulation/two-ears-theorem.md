---
title: "Two ears theorem"
source: https://en.wikipedia.org/wiki/Two_ears_theorem
domain: polygon-triangulation
license: CC-BY-SA-4.0
tags: polygon triangulation, ear clipping, monotone polygon, trapezoid decomposition
fetched: 2026-07-02
---

# Two ears theorem

In geometry, the **two ears theorem** states that every simple polygon with more than three vertices has at least two ears, vertices that can be removed from the polygon without introducing any crossings. The two ears theorem is equivalent to the existence of polygon triangulations. It is frequently attributed to Gary H. Meisters, but was proved earlier by Max Dehn.

## Statement of the theorem

A simple polygon is a simple closed curve in the Euclidean plane consisting of finitely many line segments in a cyclic sequence, with each two consecutive line segments meeting at a common endpoint, and no other intersections. By the Jordan curve theorem, it separates the plane into two regions, one of which (the interior of the polygon) is bounded.

An *ear* of a polygon is defined as a triangle formed by three consecutive vertices $u,v,w$ of the polygon, such that its edge $uw$ lies entirely in the interior of the polygon. The two ears theorem states that every simple polygon that is not itself a triangle has at least two ears.

## Relation to triangulations

An ear and its two neighbors form a triangle within the polygon that is not crossed by any other part of the polygon. Removing a triangle of this type produces a polygon with fewer sides, and repeatedly removing ears allows any simple polygon to be triangulated. Conversely, if a polygon is triangulated, the weak dual of the triangulation (a graph with one vertex per triangle and one edge per pair of adjacent triangles) will be a tree and each leaf of the tree will form an ear. Since every tree with more than one vertex has at least two leaves, every triangulated polygon with more than one triangle has at least two ears. Thus, the two ears theorem is equivalent to the fact that every simple polygon has a triangulation.

Triangulation algorithms based on this principle have been called *ear-clipping algorithms*. Although a naive implementation is slow, ear-clipping can be sped up by the observation that a triple of consecutive vertices of a polygon forms an ear if and only if the central vertex of the triple is convex and the triple forms a triangle that does not contain any reflex vertices. By maintaining a queue of triples with this property, and repeatedly removing an ear from the queue and updating the adjacent triples, it is possible to perform ear-clipping in time $O{\bigl (}n(r+1){\bigr )}$ , where n is the number of input vertices and r is the number of reflex vertices.

If a simple polygon is triangulated, then a triple of consecutive vertices $u,v,w$ forms an ear if v is a convex vertex and none of its other neighbors in the triangulation lie in triangle $uvw$ . By testing all neighbors of all vertices, it is possible to find all the ears of a triangulated simple polygon in linear time. Alternatively, it is also possible to find a single ear of a simple polygon in linear time, without triangulating the polygon.

An ear is called *exposed* when its central vertex belongs to the convex hull of the polygon. However, it is possible for a polygon to have no exposed ears.

Ears are a special case of a *principal vertex*, a vertex such that the line segment connecting the vertex's neighbors does not cross the polygon or touch any other vertex of it. A principal vertex for which this line segment lies outside the polygon is called a *mouth*. Analogously to the two ears theorem, every non-convex simple polygon has at least one mouth. Polygons with the minimum number of principal vertices of both types, two ears and a mouth, are called anthropomorphic polygons. Repeatedly finding and removing a mouth from a non-convex polygon will eventually turn it into the convex hull of the initial polygon. This principle can be applied to the *surrounding polygons* of a set of points; these are polygons that use some of the points as vertices, and contain the rest of them. Removing a mouth from a surrounding polygon produces another surrounding polygon, and the family of all surrounding polygons can be found by reversing this mouth-removal process, starting from the convex hull.

## Proof

Let v be a vertex that is preceded by vertex u and proceeded by vertex w .

We say that v is a **convex corner** if there is a point A on the edge $uv$ and a point B on the edge $vw$ such that the line $AB$ lies within the polygon. If the points $A,B$ were the vertices $u,v$ then we would have an ear - but in general there are corners that are not ears.

Every simple polygon has at least three **convex corners**. If one of these vertices, v, is not an ear, then it can be connected by a diagonal to another vertex x inside the triangle uvw formed by v and its two neighbors; x can be chosen to be the vertex within this triangle that is farthest from line uw. This diagonal decomposes the polygon into two smaller polygons, and repeated decomposition by ears and diagonals eventually produces a triangulation of the whole polygon, from which an ear can be found as a leaf of the dual tree.

## History and proof

The two ears theorem is often attributed to a 1975 paper by Gary H. Meisters, from which the "ear" terminology originated. However, the theorem was proved earlier by Max Dehn (circa 1899) as part of a proof of the Jordan curve theorem. The proof presented in this article follows Dehn's.
