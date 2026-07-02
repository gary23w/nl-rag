---
title: "Treemapping"
source: https://en.wikipedia.org/wiki/Treemapping
domain: treemap-viz
license: CC-BY-SA-4.0
tags: treemapping, nested rectangles, voronoi treemap, space filling
fetched: 2026-07-02
---

# Treemapping

In information visualization and computing, **treemapping** is a method for displaying hierarchical data using nested figures, usually rectangles.

Treemaps display hierarchical (tree-structured) data as a set of nested rectangles. Each branch of the tree is given a rectangle, which is then tiled with smaller rectangles representing sub-branches. A leaf node's rectangle has an area proportional to a specified dimension of the data. Often the leaf nodes are colored to show a separate dimension of the data.

When the color and size dimensions are correlated in some way with the tree structure, one can often easily see patterns that would be difficult to spot in other ways, such as whether a certain color is particularly prevalent. A second advantage of treemaps is that, by construction, they make efficient use of space. As a result, they can legibly display thousands of items on the screen simultaneously.

## Tiling algorithms

To create a treemap, one must define a tiling algorithm, that is, a way to divide a region into sub-regions of specified areas. Ideally, a treemap algorithm would create regions that satisfy the following criteria:

1. A small aspect ratio—ideally close to one. Regions with a small aspect ratio (i.e., fat objects) are easier to perceive.
2. Preserve some sense of the ordering in the input data (ordered).
3. Change to reflect changes in the underlying data (high stability).

These properties have an inverse relationship. As the aspect ratio is optimized, the order of placement becomes less predictable. As the order becomes more stable, the aspect ratio is degraded.

### Rectangular treemaps

To date, fifteen primary rectangular treemap algorithms have been developed:

| Algorithm | Order | Aspect ratios | Stability |
|---|---|---|---|
| **BinaryTree** | partially ordered | high | stable |
| **Slice And Dice** | ordered | very high | stable |
| **Strip** | ordered | medium | medium stability |
| **Pivot by middle** | ordered | medium | medium stability |
| **Pivot by split** | ordered | medium | low stability |
| **Pivot by size** | ordered | medium | medium stability |
| **Split** | ordered | medium | medium stability |
| **Spiral** | ordered | medium | medium stability |
| **Hilbert** | ordered | medium | medium stability |
| **Moore** | ordered | medium | medium stability |
| **Squarified** | unordered | low | low stability |
| **Mixed Treemaps** | unordered | low | medium stability |
| **Approximation** | unordered | low | medium stability |
| **Git** | unordered | medium | stable |
| **Local moves** | unordered | medium | stable |

### Convex treemaps

Rectangular treemaps have the disadvantage that their aspect ratio might be arbitrarily high in the worst case. As a simple example, if the tree root has only two children, one with weight $1/n$ and one with weight $1-1/n$ , then the aspect ratio of the smaller child will be n , which can be arbitrarily high. To cope with this problem, several algorithms have been proposed that use regions that are general convex polygons, not necessarily rectangular.

**Convex treemaps** were developed in several steps, each step improved the upper bound on the aspect ratio. The bounds are given as a function of n - the total number of nodes in the tree, and d - the total depth of the tree.

1. Onak and Sidiropoulos proved an upper bound of $O((d\log {n})^{17})$ .
2. De-Berg and Onak and Sidiropoulos improve the upper bound to $O(d+\log {n})$ , and prove a lower bound of $O(d)$ .
3. De-Berg and Speckmann and van-der-Weele improve the upper bound to $O(d)$ , matching the theoretical lower bound. (For the special case where the depth is 1, they present an algorithm that uses only four classes of 45-degree-polygons (rectangles, right-angled triangles, right-angled trapezoids and 45-degree pentagons), and guarantees an aspect ratio of at most 34/7.)

The latter two algorithms operate in two steps (greatly simplified for clarity):

1. The original tree is converted to a binary tree: each node with more than two children is replaced by a sub-tree in which each node has exactly two children.
2. Each region representing a node (starting from the root) is divided to two, using a line that keeps the angles between edges as large as possible. It is possible to prove that, if all edges of a convex polygon are separated by an angle of at least $\phi$ , then its aspect ratio is $O(1/\phi )$ . It is possible to ensure that, in a tree of depth d , the angle is divided by a factor of at most d , hence the aspect ratio guarantee.

#### Orthoconvex treemaps

In convex treemaps, the aspect ratio cannot be constant - it grows with the depth of the tree. To attain a constant aspect-ratio, **Orthoconvex treemaps** can be used. There, all regions are orthoconvex rectilinear polygons with aspect ratio at most 64; and the leaves are either rectangles with aspect ratio at most 8, or L-shapes or S-shapes with aspect ratio at most 32.

For the special case where the depth is 1, they present an algorithm that uses only rectangles and L-shapes, and the aspect ratio is at most $2+2/{\sqrt {3}}\approx 3.15$ ; the internal nodes use only rectangles with aspect ratio at most $1+{\sqrt {3}}\approx 2.73$ .

### Other treemaps

**Voronoi Treemaps**

based on

Voronoi diagram

calculations. The algorithm is iterative and does not give any upper bound on the aspect ratio.

**Jigsaw Treemaps**

based on the geometry of space-filling curves. They assume that the weights are integers and that their sum is a square number. The regions of the map are

rectilinear polygons

and highly non-ortho-convex. Their aspect ratio is guaranteed to be at most 4.

**GosperMaps**

based on the geometry of

Gosper curves

. It is ordered and stable, but has a very high aspect ratio.

## History

Area-based visualizations have existed for decades. For example, mosaic plots (also known as Marimekko diagrams) use rectangular tilings to show joint distributions (i.e., most commonly they are essentially stacked column plots where the columns are of different widths). The main distinguishing feature of a treemap, however, is the recursive construction that allows it to be extended to hierarchical data with any number of levels. This idea was invented by professor Ben Shneiderman at the University of Maryland Human – Computer Interaction Lab in the early 1990s. Shneiderman and his collaborators then deepened the idea by introducing a variety of interactive techniques for filtering and adjusting treemaps.

These early treemaps all used the simple "slice-and-dice" tiling algorithm. Despite many desirable properties (it is stable, preserves ordering, and is easy to implement), the slice-and-dice method often produces tilings with many long, skinny rectangles. In 1994 Mountaz Hascoet and Michel Beaudouin-Lafon invented a "squarifying" algorithm, later popularized by Jarke van Wijk, that created tilings whose rectangles were closer to square. In 1999 Martin Wattenberg used a variation of the "squarifying" algorithm that he called "pivot and slice" to create the first Web-based treemap, the SmartMoney Map of the Market, which displayed data on hundreds of companies in the U.S. stock market. Following its launch, treemaps enjoyed a surge of interest, particularly in financial contexts.

A third wave of treemap innovation came around 2004, after Marcos Weskamp created the Newsmap, a treemap that displayed news headlines. This example of a non-analytical treemap inspired many imitators, and introduced treemaps to a new, broad audience. In recent years, treemaps have made their way into the mainstream media, including usage by the New York Times. The Treemap Art Project produced 12 framed images for the National Academies (United States), shown at the Every AlgoRiThm has ART in It exhibit in Washington, DC and another set for the collection of Museum of Modern Art in New York.
