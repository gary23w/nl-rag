---
title: "Sweep line algorithm"
source: https://en.wikipedia.org/wiki/Sweep_line_algorithm
domain: sweep-line-paradigm
license: CC-BY-SA-4.0
tags: sweep line algorithm, event queue, plane sweep, status structure
fetched: 2026-07-02
---

# Sweep line algorithm

In computational geometry, a **sweep line algorithm** or **plane sweep algorithm** is an algorithmic paradigm that uses a conceptual *sweep line* or *sweep surface* to solve various problems in Euclidean space. It is one of the critical techniques in computational geometry.

The idea behind algorithms of this type is to imagine that a line (often a vertical line) is swept or moved across the plane, stopping at some points. Geometric operations are restricted to geometric objects that either intersect or are in the immediate vicinity of the sweep line whenever it stops, and the complete solution is available once the line has passed over all objects.

## Applications

An application of the approach had led to a breakthrough in the computational complexity of geometric algorithms when Shamos and Hoey presented algorithms for line segment intersection in the plane in 1976. In particular, they described how a combination of the scanline approach with efficient data structures (self-balancing binary search trees) makes it possible to detect whether there are intersections among N segments in the plane in time complexity of O(*N* log *N*). The closely related Bentley–Ottmann algorithm uses a sweep line technique to report all K intersections among any N segments in the plane in time complexity of O((*N* + *K*) log *N*) and space complexity of O(*N*).

Since then, this approach has been used to design efficient algorithms for a number of problems in computational geometry, such as the construction of the Voronoi diagram (Fortune's algorithm) and the Delaunay triangulation or boolean operations on polygons.

## Generalizations and extensions

Topological sweeping is a form of plane sweep with a simple ordering of processing points, which avoids the necessity of completely sorting the points; it allows some sweep line algorithms to be performed more efficiently.

The rotating calipers technique for designing geometric algorithms may also be interpreted as a form of the plane sweep, in the projective dual of the input plane: a form of projective duality transforms the slope of a line in one plane into the *x*-coordinate of a point in the dual plane, so the progression through lines in sorted order by their slope as performed by a rotating calipers algorithm is dual to the progression through points sorted by their *x*-coordinates in a plane sweep algorithm.

The sweeping approach may be generalised to higher dimensions.
