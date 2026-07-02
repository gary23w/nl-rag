---
title: "Gilbert–Johnson–Keerthi distance algorithm"
source: https://en.wikipedia.org/wiki/Gilbert%E2%80%93Johnson%E2%80%93Keerthi_distance_algorithm
domain: bullet-physics
license: CC-BY-SA-4.0
tags: bullet physics, bullet physics library, 3d physics engine, bullet collision
fetched: 2026-07-02
---

# Gilbert–Johnson–Keerthi distance algorithm

The **Gilbert–Johnson–Keerthi distance algorithm** is a method of determining the minimum distance between two convex sets, first published by Elmer G. Gilbert, Daniel W. Johnson, and S. Sathiya Keerthi in 1988. Unlike many other distance algorithms, it does not require that the geometry data be stored in any specific format, but instead relies solely on a support function to iteratively generate closer simplices to the correct answer using the *configuration space obstacle* (CSO) of two convex shapes, more commonly known as the Minkowski difference.

"Enhanced GJK" algorithms use edge information to speed up the algorithm by following edges when looking for the next simplex. This improves performance substantially for polytopes with large numbers of vertices.

GJK makes use of Johnson's distance sub algorithm, which computes in the general case the point of a tetrahedron closest to the origin, but is known to suffer from numerical robustness problems. In 2017 Montanari, Petrinic, and Barbieri proposed a new sub-algorithm based on signed volumes which avoids the multiplication of potentially small quantities and reduces the total CPU time of the GJK algorithm by an average of 10%, with improvements ranging from 5% to 25% in scenarios where the objects are in contact.

GJK algorithms are often used incrementally in simulation systems and video games. In this mode, the final simplex from a previous solution is used as the initial guess in the next iteration, or "frame". If the positions in the new frame are close to those in the old frame, the algorithm will converge in one or two iterations. This yields collision detection systems which operate in near-constant time.

The algorithm's stability, speed, and small storage footprint make it popular for realtime collision detection, especially in physics engines for video games.

## Overview

GJK relies on two functions:

- $\mathrm {Support} (\mathrm {shape} ,{\vec {d}})$ , which returns the point on shape which has the highest dot product with ${\vec {d}}$ .
- $\mathrm {NearestSimplex} (s)$ , which takes a simplex s and returns the simplex on s closest to the origin, and a direction toward the origin normal to the new simplex. If s itself contains the origin, NearestSimplex accepts s and the two shapes are determined to intersect.

The simplices handled by NearestSimplex may each be any simplex sub-space of **R***n*. For example in 3D, they may be a point, a line segment, a triangle, or a tetrahedron; each defined by 1, 2, 3, or 4 points respectively.

### Pseudocode

```
function GJK_intersection(shape p, shape q, vector initial_axis):
    vector  A = Support(p, initial_axis) − Support(q, −initial_axis)
    simplex s = {A}
    vector  D = −A

    loop:
        A = Support(p, D) − Support(q, −D)
        if dot(A, D) < 0:
            reject
        s = s ∪ {A}
        s, D, contains_origin := NearestSimplex(s)
        if contains_origin:
            accept
```

## Illustration
