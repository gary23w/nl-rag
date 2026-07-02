---
title: "Hyperbolic tree"
source: https://en.wikipedia.org/wiki/Hyperbolic_tree
domain: focus-plus-context
license: CC-BY-SA-4.0
tags: focus plus context, fisheye distortion, hyperbolic tree, detail overview
fetched: 2026-07-02
---

# Hyperbolic tree

A **hyperbolic tree** (often shortened as **hypertree**) is an information visualization and graph drawing method inspired by hyperbolic geometry.

Displaying hierarchical data as a tree suffers from visual clutter as the number of nodes per level can grow exponentially. For a simple binary tree, the maximum number of nodes at a level *n* is 2*n*, while the number of nodes for trees with more branching grows much more quickly. Drawing the tree as a node-link diagram thus requires exponential amounts of space to be displayed.

One approach is to use a *hyperbolic tree*, first introduced by Lamping et al. Hyperbolic trees employ hyperbolic space, which intrinsically has "more room" than Euclidean space. For instance, linearly increasing the radius of a circle in Euclidean space increases its circumference linearly, while the same circle in hyperbolic space would have its circumference increase exponentially. Exploiting this property allows laying out the tree in hyperbolic space in an uncluttered manner: placing a node far enough from its parent gives the node almost the same amount of space as its parent for laying out its own children.

Displaying a hyperbolic tree commonly utilizes the Poincaré disk model of hyperbolic geometry, though the Klein-Beltrami model can also be used. Both display the entire hyperbolic plane within a unit disk, making the entire tree visible at once. The unit disk gives a fish-eye lens view of the plane, giving more emphasis to nodes which are in focus and displaying nodes further out of focus closer to the boundary of the disk. Traversing the hyperbolic tree requires Möbius transformations of the space, bringing new nodes into focus and moving higher levels of the hierarchy out of view.

Hyperbolic trees were patented in the U.S. by Xerox in 1996, but the patent has since expired.
