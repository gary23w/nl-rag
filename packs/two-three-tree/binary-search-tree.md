---
title: "Binary search tree"
source: https://en.wikipedia.org/wiki/Binary_search_tree
domain: two-three-tree
license: CC-BY-SA-4.0
tags: 2-3 tree, balanced search tree, multiway search tree, b-tree family
fetched: 2026-07-02
---

# Binary search tree

In computer science, a **binary search tree** (**BST**), also called an **ordered** or **sorted binary tree**, is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree. The time complexity of operations on the binary search tree is linear with respect to the height of the tree.

Binary search trees allow binary search for fast lookup, addition, and removal of data items. Since the nodes in a BST are laid out so that each comparison skips about half of the remaining tree, the lookup performance is proportional to that of binary logarithm. BSTs were devised in the 1960s for the problem of efficient storage of labeled data and are attributed to Conway Berners-Lee and David Wheeler.

The performance of a binary search tree is dependent on the order of insertion of the nodes into the tree since arbitrary insertions may lead to degeneracy; several variations of the binary search tree can be built with guaranteed worst-case performance. The basic operations include: search, traversal, insert and delete. BSTs with guaranteed worst-case complexities perform better than an unsorted array, which would require linear search time.

The complexity analysis of BST shows that, on average, the insert, delete and search takes $\Theta (\log n)$ for n nodes. In the worst case, they degrade to that of a singly linked list: $O(n)$ . To address the boundless increase of the tree height with arbitrary insertions and deletions, self-balancing variants of BSTs are introduced to bound the worst lookup complexity to that of the binary logarithm. AVL trees were the first self-balancing binary search trees, invented in 1962 by Georgy Adelson-Velsky and Evgenii Landis.

Binary search trees can be used to implement abstract data types such as dynamic sets, lookup tables and priority queues, and used in sorting algorithms such as tree sort.

## History

The binary search tree algorithm was discovered independently by several researchers, including P.F. Windley, Andrew Donald Booth, Andrew Colin, Thomas N. Hibbard. The algorithm is attributed to Conway Berners-Lee and David Wheeler, who used it for storing labeled data in magnetic tapes in 1960. One of the earliest and popular binary search tree algorithm is that of Hibbard.

The time complexity of a binary search tree increases boundlessly with the tree height if the nodes are inserted in an arbitrary order, therefore self-balancing binary search trees were introduced to bound the height of the tree to $O(\log n)$ . Various **height-balanced** binary search trees were introduced to confine the tree height, such as AVL trees, Treaps, and red–black trees.

## Overview

A binary search tree is a rooted binary tree in which nodes are arranged in strict total order in which the nodes with keys greater than any particular node *A* is stored on the right sub-trees to that node *A* and the nodes with keys equal to or less than *A* are stored on the left sub-trees to *A,* satisfying the binary search property.

Binary search trees are also efficacious in sortings and search algorithms. However, the search complexity of a BST depends upon the order in which the nodes are inserted and deleted; since in worst case, successive operations in the binary search tree may lead to degeneracy and form a singly linked list (or "unbalanced tree") like structure, thus has the same worst-case complexity as a linked list.

Binary search trees are also a fundamental data structure used in construction of abstract data structures such as sets, multisets, and associative arrays.

## Operations

### Searching

Searching in a binary search tree for a specific key can be programmed recursively or iteratively.

Searching begins by examining the root node. If the tree is nil, the key being searched for does not exist in the tree. Otherwise, if the key equals that of the root, the search is successful and the node is returned. If the key is less than that of the root, the search proceeds by examining the left subtree. Similarly, if the key is greater than that of the root, the search proceeds by examining the right subtree. This process is repeated until the key is found or the remaining subtree is ${\text{nil}}$ . If the searched key is not found after a ${\text{nil}}$ subtree is reached, then the key is not present in the tree.

The following pseudocode implements the BST search procedure through recursion.

| Recursive-Tree-Search(x, key) **if** x = NIL **or** key = x.key **then** **return** x **if** key < x.key **then** **return** Recursive-Tree-Search(x.left, key) **else** **return** Recursive-Tree-Search(x.right, key) **end if** |
|---|

The recursive procedure continues until a ${\text{nil}}$ or the ${\text{key}}$ being searched for are encountered.

The recursive version of the search can be "unrolled" into a while loop. On most machines, the iterative version is found to be more efficient.

| Iterative-Tree-Search(x, key) **while** x ≠ NIL **and** key ≠ x.key **do** **if** key < x.key **then** x := x.left **else** x := x.right **end if** **repeat** **return** x |
|---|

Since the search may proceed till some leaf node, the running time complexity of BST search is $O(h)$ where h is the height of the tree. However, the worst case for BST search is $O(n)$ where n is the total number of nodes in the BST, because an unbalanced BST may degenerate to a linked list. However, if the BST is height-balanced the height is $O(\log n)$ .

#### Successor and predecessor

For certain operations, given a node ${\text{x}}$ , finding the successor or predecessor of ${\text{x}}$ is crucial. Assuming all the keys of a BST are distinct, the successor of a node ${\text{x}}$ in a BST is the node with the smallest key greater than ${\text{x}}$ 's key. On the other hand, the predecessor of a node ${\text{x}}$ in a BST is the node with the largest key smaller than ${\text{x}}$ 's key. The following pseudocode finds the successor and predecessor of a node ${\text{x}}$ in a BST.

| BST-Successor(x) **if** x.right ≠ NIL **then** **return** BST-Minimum(x.right) **end if** y := x.parent **while** y ≠ NIL **and** x = y.right **do** x := y y := y.parent **repeat** **return** y | BST-Predecessor(x) **if** x.left ≠ NIL **then** **return** BST-Maximum(x.left) **end if** y := x.parent **while** y ≠ NIL **and** x = y.left **do** x := y y := y.parent **repeat** **return** y |
|---|---|

Operations such as finding a node in a BST whose key is the maximum or minimum are critical in certain operations, such as determining the successor and predecessor of nodes. Following is the pseudocode for the operations.

| BST-Maximum(x) **while** x.right ≠ NIL **do** x := x.right **repeat** **return** x | BST-Minimum(x) **while** x.left ≠ NIL **do** x := x.left **repeat** **return** x |
|---|---|

### Insertion

Operations such as insertion and deletion cause the BST representation to change dynamically. The data structure must be modified in such a way that the properties of BST continue to hold. New nodes are inserted as leaf nodes in the BST. Following is an iterative implementation of the insertion operation.

| 1 BST-Insert(T, z) 2 y := NIL 3 x := T.root 4 **while** x ≠ NIL **do** 5 y := x 6 **if** z.key < x.key **then** 7 x := x.left 8 **else** 9 x := x.right 10 **end if** 11 **repeat** 12 z.parent := y 13 **if** y = NIL **then** 14 T.root := z 15 **else if** z.key < y.key **then** 16 y.left := z 17 **else** 18 y.right := z 19 **end if** |
|---|

The procedure maintains a "trailing pointer" ${\text{y}}$ as a parent of ${\text{x}}$ . After initialization on line 2, the **while** loop along lines 4-11 causes the pointers to be updated. If ${\text{y}}$ is ${\text{nil}}$ , the BST is empty, thus ${\text{z}}$ is inserted as the root node of the binary search tree ${\text{T}}$ , if it is not ${\text{nil}}$ , insertion proceeds by comparing the keys to that of ${\text{y}}$ on the lines 15-19 and the node is inserted accordingly.

### Deletion

The deletion of a node, say ${\text{Z}}$ , from the binary search tree ${\text{BST}}$ has three cases:

1. If ${\text{Z}}$ is a leaf node, it is replaced by ${\text{NIL}}$ as shown in (a).
2. If ${\text{Z}}$ has only one child, the child node of ${\text{Z}}$ gets elevated by modifying the parent node of ${\text{Z}}$ to point to the child node, consequently taking ${\text{Z}}$ 's position in the tree, as shown in (b) and (c).
3. If ${\text{Z}}$ has both left and right children, the in-order successor of ${\text{Z}}$ , say ${\text{Y}}$ , displaces ${\text{Z}}$ by following the two cases:
  1. If ${\text{Y}}$ is ${\text{Z}}$ 's right child, as shown in (d), ${\text{Y}}$ displaces ${\text{Z}}$ and ${\text{Y}}$ 's right child remain unchanged.
  2. If ${\text{Y}}$ lies within ${\text{Z}}$ 's right subtree but is not ${\text{Z}}$ 's right child, as shown in (e), ${\text{Y}}$ first gets replaced by its own right child, and then it displaces ${\text{Z}}$ 's position in the tree.
4. Alternatively, the in-order predecessor can also be used.

The following pseudocode implements the deletion operation in a binary search tree.

| 1 BST-Delete(BST, z) 2 **if** z.left = NIL **then** 3 Shift-Nodes(BST, z, z.right) 4 **else if** z.right = NIL **then** 5 Shift-Nodes(BST, z, z.left) 6 **else** 7 y := BST-Successor(z) 8 **if** y.parent ≠ z **then** 9 Shift-Nodes(BST, y, y.right) 10 y.right := z.right 11 y.right.parent := y 12 **end if** 13 Shift-Nodes(BST, z, y) 14 y.left := z.left 15 y.left.parent := y 16 **end if** |
|---|
| 1 Shift-Nodes(BST, u, v) 2 **if** u.parent = NIL **then** 3 BST.root := v 4 **else if** u = u.parent.left **then** 5 u.parent.left := v 5 **else** 6 u.parent.right := v 7 **end if** 8 **if** v ≠ NIL **then** 9 v.parent := u.parent 10 **end if** |

The ${\text{BST-Delete}}$ procedure deals with the 3 special cases mentioned above. Lines 2-3 deal with case 1; lines 4-5 deal with case 2 and lines 6-16 for case 3. The helper function ${\text{Shift-Nodes}}$ is used within the deletion algorithm for the purpose of replacing the node ${\text{u}}$ with ${\text{v}}$ in the binary search tree ${\text{BST}}$ . This procedure handles the deletion (and substitution) of ${\text{u}}$ from ${\text{BST}}$ .

## Traversal

A BST can be traversed through three basic algorithms: inorder, preorder, and postorder tree walks.

- **Inorder tree walk**: Nodes from the left subtree get visited first, followed by the root node and right subtree. Such a traversal visits all the nodes in the order of non-decreasing key sequence.
- **Preorder tree walk**: The root node gets visited first, followed by left and right subtrees.
- **Postorder tree walk**: Nodes from the left subtree get visited first, followed by the right subtree, and finally, the root.

Following is a recursive implementation of the tree walks.

| Inorder-Tree-Walk(x) **if** x ≠ NIL **then** Inorder-Tree-Walk(x.left) *visit node* Inorder-Tree-Walk(x.right) **end if** | Preorder-Tree-Walk(x) **if** x ≠ NIL **then** *visit node* Preorder-Tree-Walk(x.left) Preorder-Tree-Walk(x.right) **end if** | Postorder-Tree-Walk(x) **if** x ≠ NIL **then** Postorder-Tree-Walk(x.left) Postorder-Tree-Walk(x.right) *visit node* **end if** |
|---|---|---|

Without rebalancing, insertions or deletions in a binary search tree may lead to degeneration, resulting in a height n of the tree (where n is number of items in a tree), so that the lookup performance is deteriorated to that of a linear search. Keeping the search tree balanced and height bounded by $O(\log n)$ is a key to the usefulness of the binary search tree. This can be achieved by "self-balancing" mechanisms during the updation operations to the tree designed to maintain the tree height to the binary logarithmic complexity.

### Height-balanced trees

A tree is height-balanced if the heights of the left sub-tree and right sub-tree are guaranteed to be related by a constant factor. This property was introduced by the AVL tree and continued by the red–black tree. The heights of all the nodes on the path from the root to the modified leaf node have to be observed and possibly corrected on every insert and delete operation to the tree.

### Weight-balanced trees

In a weight-balanced tree, the criterion of a balanced tree is the number of leaves of the subtrees. The weights of the left and right subtrees differ at most by 1 . However, the difference is bound by a ratio $\alpha$ of the weights, since a strong balance condition of 1 cannot be maintained with $O(\log n)$ rebalancing work during insert and delete operations. The $\alpha$ -weight-balanced trees gives an entire family of balance conditions, where each left and right subtrees have each at least a fraction of $\alpha$ of the total weight of the subtree.

### Types

There are several self-balanced binary search trees, including T-tree, treap, red-black tree, B-tree, 2–3 tree, and Splay tree.

## Examples of applications

### Sort

Binary search trees are used in sorting algorithms such as tree sort, where all the elements are inserted at once and the tree is traversed at an in-order fashion. BSTs are also used in quicksort.

### Priority queue operations

Binary search trees are used in implementing priority queues, using the node's key as priorities. Adding new elements to the queue follows the regular BST insertion operation but the removal operation depends on the type of priority queue:

- If it is an ascending order priority queue, removal of an element with the lowest priority is done through leftward traversal of the BST.
- If it is a descending order priority queue, removal of an element with the highest priority is done through rightward traversal of the BST.
