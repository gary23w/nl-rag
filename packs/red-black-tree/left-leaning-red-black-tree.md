---
title: "Left-leaning red–black tree"
source: https://en.wikipedia.org/wiki/Left-leaning_red–black_tree
domain: red-black-tree
license: CC-BY-SA-4.0
tags: red-black tree, balanced binary tree, self-balancing tree, left-leaning red-black tree
fetched: 2026-07-02
---

# Left-leaning red–black tree

A **left-leaning red–black** (**LLRB**) tree is a type of self-balancing binary search tree, introduced by Robert Sedgewick. It is a variant of the red–black tree and guarantees the same asymptotic complexity for operations, but is designed to be easier to implement.

## Properties

A left-leaning red-black tree satisfies all the properties of a red-black tree:

1. Every node is either red or black.
2. A NIL node is considered black.
3. A red node does not have a red child.
4. Every path from a given node to any of its descendant NIL nodes goes through the same number of black nodes.
5. The root is black (by convention).

Additionally, the left-leaning property states that:

2. If a node has only one red child, it must be the left child.

The left-leaning property reduces the number of cases that must be considered when implementing search tree operations.

## Relation to 2–3 and 2–3–4 trees

LLRB trees are isomorphic 2–3–4 trees. Unlike conventional red-black trees, the 3-nodes always lean left, making this relationship a 1 to 1 correspondence. This means that for every LLRB tree, there is a unique corresponding 2–3–4 tree, and vice versa.

If we impose the additional requirement that a node may not have two red children, LLRB trees become isomorphic to 2–3 trees, since 4-nodes are now prohibited. Sedgewick remarks that the implementations of LLRB 2–3 trees and LLRB 2–3–4 trees differ only in the position of a single line of code.

## Analysis

All of the red-black tree algorithms that have been proposed are characterized by a worst-case search time bounded by a small constant multiple of log *N* in a tree of N keys, and the behavior observed in practice is typically that same multiple faster than the worst-case bound, close to the optimal log *N* nodes examined that would be observed in a perfectly balanced tree.

Specifically, in a left-leaning red-black 2–3 tree built from N random keys, Sedgewick's experiments suggest that:

- A random successful search examines log2 *N* − 0.5 nodes.
- The average tree height is about 2 ln *N*.
- The average size of left subtree exhibits log-oscillating behavior.
