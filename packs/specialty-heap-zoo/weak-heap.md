---
title: "Weak heap"
source: https://en.wikipedia.org/wiki/Weak_heap
domain: specialty-heap-zoo
license: CC-BY-SA-4.0
tags: soft heap, kinetic heap, weak heap, mergeable heap, calendar queue
fetched: 2026-07-02
---

# Weak heap

In computer science, a **weak heap** is a data structure for priority queues, combining features of the binary heap and binomial heap. It can be stored in an array as an implicit binary tree like a binary heap, and has the efficiency guarantees of binomial heaps.

A sorting algorithm using weak heaps, weak-heapsort, uses a number of comparisons that is close to the theoretical lower bound on the number of comparisons required to sort a list, so is particularly useful when comparison is expensive, such as when comparing strings using the full Unicode collation algorithm.

## Description

A weak heap is most easily understood as a heap-ordered multi-way tree stored as a binary tree using the "right-child left-sibling" convention. (This is equivalent to, but reversed from, the usual left-child right-sibling binary tree.)

In the multi-way tree, and assuming a max-heap, each parent's key is greater than or equal to (≥) all the child keys (and thus, by induction, all members of the subtree).

Expressed as a binary tree, this translates to the following invariants:

- The root node has no left child
- For every node, the value associated with that node is greater than or equal to the values associated with all nodes in its right subtree.
- The leaves of the tree have heights that are all within one of each other.

The last condition is a consequence of the fact that an implicit binary tree is a complete binary tree.

The structure of this tree maps very neatly onto the traditional 1-based (Ahnentafel) implicit binary tree arrangement, where node k has a next sibling (left child) numbered 2*k* and a first child (right child) numbered 2*k* + 1, by adding an additional root numbered 0. This root has no siblings, only a first child, which is node 1 (2×0 + 1).

This structure is very similar to that of a binomial heap, with a tree of height h being composed of a root plus trees of heights *h* − 1, *h* − 2, ..., 1. A perfect (no missing leaves) weak heap with 2*n* elements is exactly isomorphic to a binomial heap of the same size, but the two algorithms handle sizes which are not a power of 2 differently: a binomial heap uses multiple perfect trees, while a weak heap uses a single imperfect tree.

Weak heaps require the ability to exchange the left and right children (and associated subtrees) of a node. In an explicit (pointer-based) representation of the tree, this is straightforward. In an implicit (array) representation, this requires one "reverse bit" per internal node to indicate which child is considered the left child. A weak heap is thus not a strictly implicit data structure since it requires *O*(*n*) additional space (⁠1/2⁠ bit per node). However, it is often possible to find space for this extra bit within the node structure, such as by tagging a pointer which is already present.

In the implicit binary tree, node k with reverse bit *rk* has parent ⌊⁠*k*/2⁠⌋, left child 2*k* + *rk*, and right child 2*k* + 1 − *rk*.

Viewed as a multi-way tree, each node in a weak heap is linked to two others: a "next sibling" and a "first child". In the implicit tree, the links are fixed, so *which* of the two links is the sibling and which the first child is indicated by the reverse bit.

## Operations on weak heaps

Note that *every* node in a weak heap can be considered the root of a smaller weak heap by ignoring its next sibling. Nodes with no first child are automatically valid weak heaps.

A node of height h has *h* − 1 children: a first child of height *h* − 1, a second child of height *h* − 2, and so on to the last child of height 1. These may be found by following the first child link and then successive next sibling links.

It also has next siblings of height *h* − 1, *h* − 2, etc.

A node's parent in the multi-way tree is called its "distinguished ancestor". To find this in the binary tree, find the node's binary parent. If the node is the right child (first child), the parent is the distinguished ancestor. If the node is the left child (next sibling), its distinguished ancestor is the same as its binary parent's. In the implicit tree, finding the binary parent is easy, but its reverse bit must be consulted to determine which type of child the node is. (Early papers used the term "grandparent" for the distinguished ancestor, a meaning confusingly different from the usual "parent of parent".)

Although the distinguished ancestor may be log2*n* levels high in the tree, the *average* distance is 2. (It's at least 1, and half of the time we recurse, so *D* = 1 + *D*/2, meaning that *D* = 2.) Thus, even a simple iterative algorithm for finding the distinguished ancestor is sufficient.

Like binomial heaps, the fundamental operation on weak heaps is merging two heaps of equal height h, to make a weak heap of height *h*+1. This requires exactly one comparison, between the roots. Whichever root is greater (assuming a max-heap) is the final root. Its first child is the losing root, which retains its children (right subtree). The winning root's children are installed as siblings of the losing root.

This operation can be performed on the implicit tree structure because the heaps being merged are never arbitrary. Rather, the two heaps are formed as part of sifting a node up the multi-way tree:

- The first is a normal weak heap (whose next sibling link exists, but is ignored).
- The second is the imaginary heap formed by linking the first root's distinguished ancestor (multi-way parent) to the first root's following siblings.

At the beginning, the heap invariants apply everywhere *except* possibly between the first root and its distinguished ancestor. All *other* nodes are less than or equal to their distinguished ancestors.

After comparing the two roots, the merge proceeds in one of two ways:

1. (The distinguished ancestor is greater or equal.) Nothing needs to be moved, and the result of the merge is the distinguished ancestor.
2. (The first root is greater.) The first root's binary children (first child and next sibling) are exchanged (using the reverse bit), and then the first root and its distinguished ancestor are exchanged (by copying).

The second case works because, in the multi-way tree, each node keeps its children with it. The first root is promoted up the tree because it is greater than its distinguished ancestor. Thus, it is safely greater than all of the ancestor's previous children.

The previous ancestor, however, is not a safe parent for the first root's old children, because it is less than the first root and so it's not guaranteed to be greater than or equal to all of its children.

By swapping the binary children, the appropriate subset of the demoted ancestor's old children (which are safely less than or equal to it) are demoted with it. The demoted ancestor's new siblings are the first root's old children, promoted, which are safely less than or equal to the promoted first root.

After this operation, it is uncertain whether the invariant is maintained between the new distinguished ancestor and *its* distinguished ancestor, so the operation is repeated until the root is reached.

## Weak-heap sort

Weak heaps may be used to sort an array, in essentially the same way as a conventional heapsort. First, a weak heap is built out of all of the elements of the array, and then the root is repeatedly exchanged with the last element, which is sifted down to its proper place.

A weak heap of n elements can be formed in *n* − 1 merges. It can be done on various orders, but a simple bottom-up implementation works from the end of the array to the beginning, merging each node with its distinguished ancestor. Note that *finding* the distinguished ancestor is simplified because the reverse bits in all parents of the heaps being merged are unmodified from their initial state ("not reversed"), and so do not need to be consulted.

As with heapsort, if the array to be sorted is larger than the CPU cache, performance is improved if subtrees are merged as soon as two of the same size become available, rather than merging all subtrees on one level before proceeding to the next.

Sifting down in a weak heap can be done in *h* = ⌈log2*n*⌉ comparisons, as opposed to 2 log2*n* for a binary heap, or 1.5 log2*n* for the "bottom-up heapsort" variant. This is done by "merging up": after swapping the root with the last element of the heap, find the last (height 1) child of the root. Merge this with the root (its distinguished ancestor), resulting in a valid height-2 heap at the global root. Then go to the previous sibling (binary parent) of the last merged node, and merge again. Repeat until the root is reached, when it will be correct for the complete tree.

## Priority queue operations

In a weak max-heap, the maximum value can be found (in constant time) as the value associated with the root node; similarly, in a weak min-heap, the minimum value can be found at the root.

As with binary heaps, weak heaps can support the typical operations of a priority queue data structure: insert, delete-min, delete, or decrease-key, in logarithmic time per operation.

Sifting up is done using the same process as in binary heaps. The new node is added at the leaf level, then compared with its distinguished ancestor and swapped if necessary (the merge operation). This is repeated until no more swaps are necessary or the root is reached.

Variants of the weak heap structure allow constant amortized time insertions and decrease-keys, matching the time for Fibonacci heaps.

## History and applications

Weak heaps were introduced by Dutton (1993), as part of a variant heap sort algorithm that (unlike the standard heap sort using binary heaps) could be used to sort n items using only *n* log2*n* + *O*(*n*) comparisons. They were later investigated as a more generally applicable priority queue data structure.
