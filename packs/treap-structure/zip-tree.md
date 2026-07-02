---
title: "Zip tree"
source: https://en.wikipedia.org/wiki/Zip_tree
domain: treap-structure
license: CC-BY-SA-4.0
tags: treap, randomized binary search tree, cartesian tree, zip tree
fetched: 2026-07-02
---

# Zip tree

The **zip tree** was introduced as a variant of random binary search tree by Robert Tarjan, Caleb Levy, and Stephen Timmel. Zip trees are similar to max treaps except ranks are generated through a geometric distribution and maintain their max-heap property during insertions and deletions through unzipping and zipping rather than tree rotations. Nodes of the tree contain a distinct, comparable key and a numeric rank. The tree is max heap ordered with respect to the ranks with ties broken in favor of smaller keys. Nodes of the tree must contain distinct keys but allow for duplicate ranks. The rank tie-breaker favoring smaller keys creates a bias in the tree favoring smaller nodes. A slightly modified zip tree variant, zip-zip trees address this bias by introducing a different tie-breaker with a second rank.

## Operations

Zip trees support the operations of a binary search tree. The main implementation differences come through the zip tree's implementation of insert and delete through unzipping and zipping paths to maintain the heap ordering of the tree.

The time it takes to insert or delete a node *u* is equal to the time to search for *u* plus the time for unzipping or zipping. The time it takes to unzip or zip is proportional to one plus the number of nodes on the path(s) being unzipped/zipped. The expected depth of any node in a zip tree is at most 1.5 log *n*, making the expected running time of the insert, delete, and search operations all *O(*log *n)*.

### Insertion

When inserting a node *x* into a zip tree, first generate a new rank from a geometric distribution with a probability of success of 1/2. Let *x.key* be the key of the node *x*, and let *x.rank* be the rank of the node *x*.

Then, follow the search path for *x* in the tree until finding a node *u* such that *u.rank* *<= x.rank* and *u.key < x.key*. Continue along the search path for *x*, "unzipping" every node *v* passed by placing them either in path *P* if *v.key < x.key*, or path *Q* if *v.key > x.key*. Keys must be unique so if at any point *v.key = x.key*, the search stops and no new node is inserted.

Once the search for *x* is complete, *x* is inserted in place of the node *u.* The top node of the path *P* becomes the left child of *x* and the top node of *Q* becomes the right child. The parent and child pointers between *u* and *u.parent* will be updated accordingly with *x*, and if *u* was previously the root node, *x* becomes the new root.

### Deletion

When deleting a node *x*, first search the tree to find it. If no node is found with the same key as *x.key*, no deletion occurs.

Once *x* is found, continue two searches down the left and right subtrees of *x*, "zipping" together the right spine of the left subtree and left spine of the right subtree into one path *R* in decreasing order by rank. While creating this path top-down, nodes are added as left and right children of their parent accordingly based on their keys.

Once the path *R* is complete, the root of the path will replace *x*. The parent and child pointers between *x* and *x*.*parent* are updated accordingly, and if *x* was previously the root node, the top node of *R* is the new root.
