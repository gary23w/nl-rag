---
title: "Rotating calipers"
source: https://en.wikipedia.org/wiki/Rotating_calipers
domain: rotating-calipers
license: CC-BY-SA-4.0
tags: rotating calipers, convex polygon width, antipodal pairs, polygon diameter
fetched: 2026-07-02
---

# Rotating calipers

In computational geometry, the method of **rotating calipers** is an algorithm design technique that can be used to solve optimization problems including finding the width or diameter of a set of points.

The method is so named because the idea is analogous to rotating a spring-loaded vernier caliper around the outside of a convex polygon. Every time one blade of the caliper lies flat against an edge of the polygon, it forms an antipodal pair with the point or edge touching the opposite blade. The complete "rotation" of the caliper around the polygon detects all antipodal pairs; the set of all pairs, viewed as a graph, forms a thrackle. The method of rotating calipers can be interpreted as the projective dual of a sweep line algorithm in which the sweep is across slopes of lines rather than across x- or y-coordinates of points.

## History

The rotating calipers method was first used in the dissertation of Michael Shamos in 1978. Shamos used this method to generate all antipodal pairs of points on a convex polygon and to compute the diameter of a convex polygon in $O(n)$ time. Godfried Toussaint coined the phrase "rotating calipers" and demonstrated that the method was applicable in solving many other computational geometry problems.

## Shamos's algorithm

Shamos gave the following algorithm in his dissertation (pp. 77–82) for the rotating calipers method, which generated all antipodal pairs of vertices on a convex polygon:

```mw
/* p[] is in standard form, ie, counter clockwise order, 
     distinct vertices, no collinear vertices.
   ANGLE(m, n) is a procedure that returns the clockwise angle 
     swept out by a ray as it rotates from a position parallel 
     to the directed segment Pm,Pm+1 to a position parallel to Pn, Pn+1
   We assume all indices are reduced to mod N (so that N+1 = 1).
*/
GetAllAntiPodalPairs(p[1..n])
    // Find first anti-podal pair by locating vertex opposite P1
    i = 1
    j = 2
    while angle(i, j) < pi
        j++
    yield i, j

    /* Now proceed around the polygon taking account of
         possibly parallel edges. Line L passes through
         Pi, Pi+1 and M passes through Pj, Pj+1
    */

    // Loop on j until all of P has been scanned
    current = i    
    while j != n
        if angle(current, i + 1) <= angle(current, j + 1)
            j++
            current = j
        else
            i++
            current = i
        yield i, j

        // Now take care of parallel edges
        if angle(current, i + 1) = angle(current, j + 1)
            yield i + 1, j
            yield i, j + 1
            yield i + 1, j + 1
            if current = i
                j++
            else
                i++
```

Another version of this algorithm appeared in the text by Preparata and Shamos in 1985 that avoided calculation of angles:

```mw
GetAllAntiPodalPairs(p[1..n])
    i = n
    j = i + 1
    while (Area(i, i + 1, j + 1) > Area(i, i + 1, j))
        j = j + 1
    j0 = j
    while (i != j0)
        i = i + 1
        yield i, j
        while (Area(i, i + 1, j + 1) > Area(i, i + 1, j))
            j = j + 1
            if ((i, j) != (j0, 1))
                yield i, j
        if (Area(i, i + 1, j + 1) = Area(i, i + 1, j))
            if ((i, j) != (j0, n))
                yield i, j + 1
```

## Applications

Pirzadeh describes various applications of rotating calipers method.

### Distances

- Diameter (maximum width) of a convex polygon
- Width (minimum width) of a convex polygon
- Maximum distance between two convex polygons
- Minimum distance between two convex polygons
- Widest empty (or separating) strip between two convex polygons (a simplified low-dimensional variant of a problem arising in support vector machine based machine learning)
- Grenander distance between two convex polygons
- Optimal strip separation (used in medical imaging and solid modeling)

### Bounding boxes

- Minimum area oriented bounding box
- Minimum perimeter oriented bounding box

### Triangulations

- Onion triangulations
- Spiral triangulations
- Quadrangulation
- Nice triangulation
- Art gallery problem
- Wedge placement optimization problem

### Multi-polygon operations

- Union of two convex polygons
- Common tangents to two convex polygons
- Intersection of two convex polygons
- Critical support lines of two convex polygons
- Vector sums (or Minkowski sum) of two convex polygons
- Convex hull of two convex polygons

### Traversals

- Shortest transversals
- Thinnest-strip transversals

### Others

- Non parametric decision rules for machine learned classification
- Aperture angle optimizations for visibility problems in computer vision
- Finding longest cells in millions of biological cells
- Comparing precision of two people at firing range
- Classify sections of brain from scan images
