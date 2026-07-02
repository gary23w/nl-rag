---
title: "Diameter (computational geometry)"
source: https://en.wikipedia.org/wiki/Diameter_(computational_geometry)
domain: rotating-calipers
license: CC-BY-SA-4.0
tags: rotating calipers, convex polygon width, antipodal pairs, polygon diameter
fetched: 2026-07-02
---

# Diameter (computational geometry)

In computational geometry, the diameter of a finite set of points or of a polygon is its diameter as a set, the largest distance between any two points. The diameter is always attained by two points of the convex hull of the input. A trivial brute-force search can be used to find the diameter of n points in time $O(n^{2})$ (assuming constant-time distance evaluations) but faster algorithms are possible for points in low dimensions.

## Static 2d input

In two dimensions, the diameter can be obtained by computing the convex hull and then applying the method of rotating calipers. This involves finding two parallel support lines for the convex hull (for instance vertical lines through the two vertices with minimum and maximum x -coordinate) and then rotating the two lines through a sequence of discrete steps that keep them as parallel lines of support until they have rotated back to their original orientation. The diameter is the maximum distance between any pair of convex hull vertices found as the two points of contact of the parallel lines in this sweep. The time for this method is dominated by the time for constructing the convex hull: $O(n\log n)$ for a finite set of n points, or time $O(n)$ for a simple polygon with n vertices.

## Dynamic 2d input

For a dynamic two-dimensional point set subject to point insertions and deletions, an approximation to the diameter, with an approximation ratio that can be chosen arbitrarily close to one, can be maintained in time $O(\log ^{2}n)$ per operation. The exact diameter can be maintained dynamically in expected time $O(\log n)$ per operation, in an input model in which the set of points to be inserted and deleted, and the order of insertion and deletion operations, is worst-case but the point chosen to be inserted or deleted in each operation is chosen randomly from the given set.

For a dynamic two-dimensional point set of a different type, n points each moving linearly with fixed velocities, the time at which the points attain their minimum diameter and the diameter at that time can be computed in time $O(n\log ^{2}n)$

## Higher dimensions

In three dimensions, the diameter of a set of points can again be computed in time $O(n\log n)$ . A randomized method for doing this by Clarkson and Shor uses as a subroutine a randomized incremental algorithm for finding the intersection of congruent spheres. The algorithm repeatedly chooses a random input point, finds the farthest distance $\rho$ from it, intersects spheres with radius $\rho$ centered at each point, and eliminates the points contained in the resulting intersection. The eliminated points are within distance $\rho$ of all other points, and therefore cannot be part of any pair with a larger distance than $\rho$ . Each point is eliminated when the farthest distance from it is less than or equal to $\rho$ , the farthest distance from the randomly chosen point, which happens with probability ${\tfrac {1}{2}}$ , so half of the points are eliminated in expectation in each iteration of the algorithm. The total expected time for the algorithm is dominated by the time to find the first intersection of spheres, before the problem is simplified by eliminating any points. This time is $O(n\log n)$ . Ramos provides a non-random algorithm by using ε-nets to derandomize a variation of the Clarkson and Shor algorithm, with the same asymptotic runtime.

In any fixed dimension d , there exists an algorithm for which the exponent of n in the time bound is less than two. It is also possible to approximate the diameter, to within a $(1+\varepsilon )$ approximation ratio, in time $O(n+\varepsilon ^{1/2-d})$ .
