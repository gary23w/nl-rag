---
title: "Priority R-tree"
source: https://en.wikipedia.org/wiki/Priority_R-tree
domain: r-tree
license: CC-BY-SA-4.0
tags: r-tree, spatial index tree, bounding box index, hilbert r-tree
fetched: 2026-07-02
---

# Priority R-tree

The **Priority R-tree** is a worst-case asymptotically optimal alternative to the spatial tree R-tree. It was first proposed by Arge, De Berg, Haverkort and Yi, K. in an article from 2004. The prioritized R-tree is essentially a hybrid between a *k*-dimensional tree and a R-tree in that it defines a given object's N-dimensional bounding volume (called Minimum Bounding Rectangles – MBR) as a point in N-dimensions, represented by the ordered pair of the rectangles. The term *prioritized* arrives from the introduction of four priority-leaves that represents the most extreme values of each dimensions, included in every branch of the tree. Before answering a window-query by traversing the sub-branches, the prioritized R-tree first checks for overlap in its priority nodes. The sub-branches are traversed (and constructed) by checking whether the least value of the first dimension of the query is above the value of the sub-branches. This gives access to a quick indexation by the value of the first dimension of the bounding box.

## Performance

Arge *et al.* writes that the priority tree always answers window-queries with $O\left(\left({\frac {N}{B}}\right)^{1-{\frac {1}{d}}}+{\frac {T}{B}}\right)$ I/Os, where N is the number of d-dimensional (hyper-) rectangles stored in the R-tree, B is the disk block size, and T is the output size.

## Dimensions

In the case of $d=2$ the rectangle is represented by $\,((x_{min},y_{min}),(x_{max},y_{max}))$ and the MBR thus four corners $\,(x_{min},y_{min},x_{max},y_{max})$ .
