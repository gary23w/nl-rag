---
title: "Convex hull of a simple polygon"
source: https://en.wikipedia.org/wiki/Convex_hull_of_a_simple_polygon
domain: gift-wrapping
license: CC-BY-SA-4.0
tags: gift wrapping algorithm, jarvis march, convex hull output, beneath beyond
fetched: 2026-07-02
---

# Convex hull of a simple polygon

In discrete geometry and computational geometry, the **convex hull of a simple polygon** is the polygon of minimum perimeter that contains a given simple polygon. It is a special case of the more general concept of a convex hull. It can be computed in linear time, faster than algorithms for convex hulls of point sets.

The convex hull of a simple polygon can be subdivided into the given polygon itself and into polygonal *pockets* bounded by a polygonal chain of the polygon together with a single convex hull edge. Repeatedly reflecting an arbitrarily chosen pocket across this convex hull edge produces a sequence of larger simple polygons; according to the Erdős–Nagy theorem, this process eventually terminates with a convex polygon.

## Structure

The convex hull of a simple polygon is itself a convex polygon. Overlaying the original simple polygon onto its convex hull partitions this convex polygon into regions, one of which is the original polygon. The remaining regions are called *pockets*. Each pocket is itself a simple polygon, bounded by a polygonal chain on the boundary of the given simple polygon and by a single edge of the convex hull. A polygon that is already convex has no pockets.

One can form a hierarchical description of any given polygon by constructing its hull and its pockets in this way and then recursively forming a hierarchy of the same type for each pocket. This structure, called a *convex differences tree*, can be constructed efficiently.

## Algorithms

Finding the convex hull of a simple polygon can be performed in linear time. Several early publications on this problem were discovered to be incorrect, often because they led to intermediate states with crossings that caused them to break. The first correct linear-time algorithm for this problem was given by McCallum & Avis (1979). Even after its publication, other incorrect algorithms continued to be published. Brönnimann & Chan (2006) write that a majority of the published algorithms for the problem are incorrect, although a later history collected by Greg Aloupis lists only seven out of fifteen algorithms as being incorrect.

A particularly simple algorithm for this problem was published by Graham & Yao (1983) and Lee (1983). Like the Graham scan algorithm for convex hulls of point sets, it is based on a stack data structure. The algorithm traverses the polygon in clockwise order, starting from a vertex known to be on the convex hull (for instance, its leftmost point). As it does, it stores a convex sequence of vertices on the stack, the ones that have not yet been identified as being within pockets. The points in this sequence are the vertices of a convex polygon (not necessarily the hull of all vertices seen so far) that may have pockets attached to some of its edges. At each step, the algorithm follows a path along the polygon from the stack top to the next vertex that is not in one of the two pockets adjacent to the stack top. Then, while the top two vertices on the stack together with this new vertex are not in convex position, it pops the stack, before finally pushing the new vertex onto the stack. When the clockwise traversal reaches the starting point, the algorithm is completed and the stack contains the convex hull vertices in clockwise order. Each step of the algorithm either pushes a vertex onto the stack or pops it from the stack, and each vertex is pushed and popped at most once, so the total time for the algorithm is linear. If the input vertices are given in clockwise order in an array, then the output can be returned in the same array, using only a constant number of additional variables as intermediate storage.

A similar method can also be used to construct convex hulls of piecewise smooth closed curves in the plane. By using a deque in place of a stack, a similar algorithm can be generalized to the convex hull of any polygonal chain, and the algorithm for simple polygons can be started at any vertex of the polygon rather than requiring an extreme vertex as the starting vertex.

## Flipping pockets

A *flip* of a pocket constructs a new polygon from the given one by reflecting the polygonal chain that bounds a pocket across the convex hull edge of the pocket. Each flip produces another simple polygon with equal perimeter and greater area, although multiple simultaneous flips may introduce crossings. Flipping an arbitrarily chosen pocket, and then repeating this process with the pockets of each successively formed polygon, produces a sequence of simple polygons. According to the Erdős–Nagy theorem, this flipping process eventually terminates, by reaching a convex polygon. As with the problem of convex hull construction, this problem has a long history of incorrect proofs.
