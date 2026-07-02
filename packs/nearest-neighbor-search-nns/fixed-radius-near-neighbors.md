---
title: "Fixed-radius near neighbors"
source: https://en.wikipedia.org/wiki/Fixed-radius_near_neighbors
domain: nearest-neighbor-search-nns
license: CC-BY-SA-4.0
tags: nearest neighbor search, best bin first, space partitioning, vantage point tree
fetched: 2026-07-02
---

# Fixed-radius near neighbors

In computational geometry, the **fixed-radius near neighbor problem** is a variant of the nearest neighbor search problem. In the fixed-radius near neighbor problem, one is given as input a set of points in *d*-dimensional Euclidean space and a fixed distance Δ. One must design a data structure that, given a query point *q*, efficiently reports the points of the data structure that are within distance Δ of *q*. The problem has long been studied; Bentley (1975) cites a 1966 paper by Levinthal that uses this technique as part of a system for visualizing molecular structures, and it has many other applications.

## Solution by rounding and hashing

One method for solving the problem is to round the points to an integer lattice, scaled so that the distance between grid points is the desired distance Δ. A hash table can be used to find, for each input point, the other inputs that are mapped to nearby grid points, which can then be tested for whether their unrounded positions are actually within distance Δ. The number of pairs of points tested by this procedure, and the time for the procedure, is linear in the combined input and output size when the dimension is a fixed constant. However, the constant of proportionality in the linear time bound grows exponentially as a function of the dimension. Using this method, it is possible to construct indifference graphs and unit disk graphs from geometric data in linear time.

## Other solutions

Modern parallel methods for GPU are able to efficiently compute all pairs fixed-radius NNS. For finite domains, the method of Green shows the problem can be solved by sorting on a uniform grid, finding all neighbors of all particles in O(kn) time, where k is proportional to the average number of neighbors. Hoetzlein improves this further on modern hardware with counting sorting and atomic operations.

## Applications

The fixed-radius near neighbors problem arises in continuous Lagrangian simulations (such as smoothed particle hydrodynamics), computational geometry, and point cloud problems (surface reconstructions).
