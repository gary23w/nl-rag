---
title: "Order statistic tree"
source: https://en.wikipedia.org/wiki/Order_statistic_tree
domain: weight-balanced-tree
license: CC-BY-SA-4.0
tags: weight-balanced tree, self-balancing tree, augmented search tree, order statistic tree
fetched: 2026-07-02
---

# Order statistic tree

In computer science, an **order statistic tree** is a variant of the binary search tree (or more generally, a B-tree) that supports two additional operations beyond insertion, lookup and deletion:

- Select(*i*) – find the *i*-th smallest element stored in the tree
- Rank(*x*) – find the rank of element *x* in the tree, i.e. its index in the sorted list of elements of the tree

Both operations can be performed in *O*(log *n*) worst case time when a self-balancing tree is used as the base data structure.

To turn a regular search tree into an order statistic tree, the nodes of the tree need to store one additional value, which is the size of the subtree rooted at that node (i.e., the number of nodes below it). All operations that modify the tree must adjust this information to preserve the invariant that

```
size[x] = size[left[x]] + size[right[x]] + 1
```

where `size[nil] = 0` by definition. Select can then be implemented as

```
function Select(t, i)
    // Returns the i'th element (one-indexed) of the elements in t
    p ← size[left[t]]+1
    if i = p
        return t
    else if i < p
        return Select(left[t], i)
    else
        return Select(right[t], i - p)
```

Rank can be implemented, using the parent-function p[x], as

```
function Rank(T, x)
    // Returns the position of x (one-indexed) in the linear sorted list of elements of the tree T
    r ← size[left[x]] + 1
    y ← x
    while y ≠ T.root
        if y = right[p[y]]
            r ← r + size[left[p[y]]] + 1
        y ← p[y]
    return r
```

Order-statistic trees can be further amended with bookkeeping information to maintain balance (e.g., tree height can be added to get an order statistic AVL tree, or a color bit to get a red–black order statistic tree). Alternatively, the size field can be used in conjunction with a weight-balancing scheme at no additional storage cost.
