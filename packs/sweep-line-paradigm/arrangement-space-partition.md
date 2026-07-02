---
title: "Arrangement (space partition)"
source: https://en.wikipedia.org/wiki/Arrangement_(space_partition)
domain: sweep-line-paradigm
license: CC-BY-SA-4.0
tags: sweep line algorithm, event queue, plane sweep, status structure
fetched: 2026-07-02
---

# Arrangement (space partition)

In discrete geometry, an **arrangement** is the decomposition of the d-dimensional linear, affine, or projective space into connected cells of different dimensions, induced by a finite collection of geometric objects, which are usually of dimension one less than the dimension of the space, and often of the same type as each other, such as hyperplanes or spheres.

## Definition

For a set A of objects in $\mathbb {R} ^{d}$ , the cells in the arrangement are the connected components of sets of the form $(\cap X)\setminus \cup (A\setminus X)$ for subsets X of A . That is, for each X the cells are the connected components of the points that belong to every object in X and do not belong to any other object. For instance the cells of an arrangement of lines in the Euclidean plane are of three types:

- Isolated points, for which X is the subset of all lines that pass through the point.
- Line segments or rays, for which X is a singleton set of one line. The segment or ray is a connected component of the points that belong only to that line and not to any other line of A
- Convex polygons (possibly unbounded), for which X is the empty set, and its intersection (the empty intersection) is the whole space. These polygons are the connected components of the subset of the plane formed by removing all the lines in A .

## Types of arrangement

Of particular interest are the arrangements of lines and arrangements of hyperplanes.

More generally, geometers have studied arrangements of other types of curves in the plane, and of other more complicated types of surface. Arrangements in complex vector spaces have also been studied; since complex lines do not partition the complex plane into multiple connected components, the combinatorics of vertices, edges, and cells does not apply to these types of space, but it is still of interest to study their symmetries and topological properties.

## Applications

An interest in the study of arrangements was driven by advances in computational geometry, where the arrangements were unifying structures for many problems. Advances in study of more complicated objects, such as algebraic surfaces, contributed to "real-world" applications, such as motion planning and computer vision.
