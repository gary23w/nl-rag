---
title: "Cover tree"
source: https://en.wikipedia.org/wiki/Cover_tree
domain: metric-space-tree
license: CC-BY-SA-4.0
tags: ball tree, vantage-point tree, metric tree, cover tree, nearest neighbor search
fetched: 2026-07-02
---

# Cover tree

The **cover tree** is a type of data structure in computer science that is specifically designed to facilitate the speed-up of a nearest neighbor search. It is a refinement of the Navigating Net data structure, and related to a variety of other data structures developed for indexing intrinsically low-dimensional data.

The tree can be thought of as a hierarchy of levels with the top level containing the root point and the bottom level containing every point in the metric space. Each level *C* is associated with an integer value *i* that decrements by one as the tree is descended. Each level *C* in the cover tree has three important properties:

- **Nesting:** $C_{i}\subseteq C_{i-1}$
- **Covering:** For every point $p\in C_{i-1}$ , there exists a point $q\in C_{i}$ such that the distance from p to q is less than or equal to $2^{i}$ and exactly one such q is a parent of p .
- **Separation:** For all points $p,q\in C_{i}$ , the distance from p to q is greater than $2^{i}$ .

## Complexity

### Find

Like other metric trees the cover tree allows for nearest neighbor searches in $O(\eta *\log {n})$ where $\eta$ is a constant associated with the dimensionality of the dataset and n is the cardinality. To compare, a basic linear search requires $O(n)$ , which is a much worse dependence on n . However, in high-dimensional metric spaces the $\eta$ constant is non-trivial, which means it cannot be ignored in complexity analysis. Unlike other metric trees, the cover tree has a theoretical bound on its constant that is based on the dataset's expansion constant or doubling constant (in the case of approximate NN retrieval). The bound on search time is $O(c^{12}\log {n})$ where c is the expansion constant of the dataset.

### Insert

Although cover trees provide faster searches than the naive approach, this advantage must be weighed with the additional cost of maintaining the data structure. In a naive approach adding a new point to the dataset is trivial because order does not need to be preserved, but in a cover tree it can take $O(c^{6}\log {n})$ time. However, this is an upper-bound, and some techniques have been implemented that seem to improve the performance in practice.

### Space

The cover tree uses implicit representation to keep track of repeated points. Thus, it only requires O(n) space.
