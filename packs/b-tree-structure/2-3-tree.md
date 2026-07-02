---
title: "2–3 tree"
source: https://en.wikipedia.org/wiki/2–3_tree
domain: b-tree-structure
license: CC-BY-SA-4.0
tags: b-tree, multiway search tree, disk-based index, database index tree
fetched: 2026-07-02
---

# 2–3 tree

In computer science, a **2–3 tree** is a tree data structure, where every node with children (internal node) has either two children (2-node) and one data element or three children (3-node) and two data elements. A 2–3 tree is a B-tree of order 3. Nodes on the outside of the tree (leaf nodes) have no children and one or two data elements. 2–3 trees were invented by John Hopcroft in 1970.

2–3 trees are required to be balanced, meaning that each leaf is at the same level. It follows that each right, center, and left subtree of a node contains the same or close to the same amount of data.

## Definitions

We say that an internal node is a **2-node** if it has *one* data element and *two* children.

We say that an internal node is a **3-node** if it has *two* data elements and *three* children.

A **4-node**, with three data elements, may be temporarily created during manipulation of the tree but is never persistently stored in the tree.

- (2 node)2 node
- (3 node)3 node

We say that T is a **2–3 tree** if and only if one of the following statements hold:

- T is empty. In other words, T does not have any nodes.
- T is a 2-node with data element a. If T has left child p and right child q, then
  - p and q are 2–3 trees of the same height;
  - a is greater than each element in p; and
  - a is less than each data element in q.
- T is a 3-node with data elements a and b, where a < b. If T has left child p, middle child q, and right child r, then
  - p, q, and r are 2–3 trees of equal height;
  - a is greater than each data element in p and less than each data element in q; and
  - b is greater than each data element in q and less than each data element in r.

## Properties

- Every internal node is a 2-node or a 3-node.
- All leaves are at the same level.
- All data is kept in sorted order.

## Operations

### Searching

Searching for an item in a 2–3 tree is similar to searching for an item in a binary search tree. Since the data elements in each node are ordered, a search function will be directed to the correct subtree and eventually to the correct node which contains the item.

1. Let T be a 2–3 tree and d be the data element we want to find. If T is empty, then d is not in T and we're done.
2. Let t be the root of T.
3. Suppose t is a leaf.
  - If d is not in t, then d is not in T. Otherwise, d is in T. We need no further steps and we're done.
4. Suppose t is a 2-node with left child p and right child q. Let a be the data element in t. There are three cases:
  - If d is equal to a, then we've found d in T and we're done.
  - If $d<a$ , then set T to p, which by definition is a 2–3 tree, and go back to step 2.
  - If $d>a$ , then set T to q and go back to step 2.
5. Suppose t is a 3-node with left child p, middle child q, and right child r. Let a and b be the two data elements of t, where $a<b$ . There are four cases:
  - If d is equal to a or b, then d is in T and we're done.
  - If $d<a$ , then set T to p and go back to step 2.
  - If $a<d<b$ , then set T to q and go back to step 2.
  - If $d>b$ , then set T to r and go back to step 2.

### Insertion

Insertion maintains the balanced property of the tree.

To insert into a 2-node, the new key is added to the 2-node in the appropriate order.

To insert into a 3-node, more work may be required depending on the location of the 3-node. If the tree consists only of a 3-node, the node is split into three 2-nodes with the appropriate keys and children.

If the target node is a 3-node whose parent is a 2-node, the key is inserted into the 3-node to create a temporary 4-node. In the illustration, the key 10 is inserted into the 2-node with 6 and 9. The middle key is 9, and is promoted to the parent 2-node. This leaves a 3-node of 6 and 10, which is split to be two 2-nodes held as children of the parent 3-node.

If the target node is a 3-node and the parent is a 3-node, a temporary 4-node is created then split as above. This process continues up the tree to the root. If the root must be split, then the process of a single 3-node is followed: a temporary 4-node root is split into three 2-nodes, one of which is considered to be the root. This operation grows the height of the tree by one.

### Deletion

Deleting a key from a non-leaf node can be done by replacing it by its immediate predecessor or successor, and then deleting the predecessor or successor from a leaf node. Deleting a key from a leaf node is easy if the leaf is a 3-node. Otherwise, it may require creating a temporary 1-node which may be absorbed by reorganizing the tree, or it may repeatedly travel upwards before it can be absorbed, as a temporary 4-node may in the case of insertion. Alternatively, it's possible to use an algorithm which is both top-down and bottom-up, creating temporary 4-nodes on the way down that are then destroyed as you travel back up. Deletion methods are explained in more detail in the references.

### Parallel operations

Since 2–3 trees are similar in structure to red–black trees, parallel algorithms for red–black trees can be applied to 2–3 trees as well.
