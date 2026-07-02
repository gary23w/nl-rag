---
title: "Scapegoat tree"
source: https://en.wikipedia.org/wiki/Scapegoat_tree
domain: scapegoat-tree
license: CC-BY-SA-4.0
tags: scapegoat tree, self-balancing tree, amortized analysis, weight-balanced tree
fetched: 2026-07-02
---

# Scapegoat tree

In computer science, a **scapegoat tree** is a self-balancing binary search tree, invented by Arne Andersson in 1989 and again by Igal Galperin and Ronald L. Rivest in 1993. It provides worst-case ${\color {Blue}O(\log n)}$ lookup time (with n as the number of entries) and $O(\log n)$ amortized insertion and deletion time.

Unlike most other self-balancing binary search trees which also provide worst case $O(\log n)$ lookup time, scapegoat trees have no additional per-node memory overhead compared to a regular binary search tree: besides key and value, a node stores only two pointers to the child nodes. This makes scapegoat trees easier to implement and, due to data structure alignment, can reduce node overhead by up to one-third.

Instead of the small incremental rebalancing operations used by most balanced tree algorithms, scapegoat trees rarely but expensively choose a "scapegoat" and completely rebuilds the subtree rooted at the scapegoat into a complete binary tree. Thus, scapegoat trees have $O(n)$ worst-case update performance.

## Theory

A binary search tree is said to be weight-balanced if half the nodes are on the left of the root, and half on the right. An α-weight-balanced node is defined as meeting a relaxed weight balance criterion:

```
size(left) ≤ α*size(node)
size(right) ≤ α*size(node)
```

Where size can be defined recursively as:

```
function size(node) is
    if node = nil then
        return 0
    else
        return size(node->left) + size(node->right) + 1
    end if
end function
```

Even a degenerate tree (linked list) satisfies this condition if α=1, whereas an α=0.5 would only match almost complete binary trees.

A binary search tree that is α-weight-balanced must also be **α-height-balanced**, that is

```
height(tree) ≤ floor(log1/α(size(tree)))
```

By contraposition, a tree that is not α-height-balanced is not α-weight-balanced.

Scapegoat trees are not guaranteed to keep α-weight-balance at all times, but are always loosely α-height-balanced in that

```
height(scapegoat tree) ≤ floor(log1/α(size(tree))) + 1.
```

Violations of this height balance condition can be detected at insertion time, and imply that a violation of the weight balance condition must exist.

This makes scapegoat trees similar to red–black trees in that they both have restrictions on their height. They differ greatly though in their implementations of determining where the rotations (or in the case of scapegoat trees, rebalances) take place. Whereas red–black trees store additional 'color' information in each node to determine the location, scapegoat trees find a **scapegoat** which isn't α-weight-balanced to perform the rebalance operation on. This is loosely similar to AVL trees, in that the actual rotations depend on 'balances' of nodes, but the means of determining the balance differs greatly. Since AVL trees check the balance value on every insertion/deletion, it is typically stored in each node; scapegoat trees are able to calculate it only as needed, which is only when a scapegoat needs to be found.

Unlike most other self-balancing search trees, scapegoat trees are entirely flexible as to their balancing. They support any α such that 0.5 < α < 1. A high α value results in fewer balances, making insertion quicker but lookups and deletions slower, and vice versa for a low α. Therefore in practical applications, an α can be chosen depending on how frequently these actions should be performed.

## Operations

### Lookup

Lookup is not modified from a standard binary search tree, and has a worst-case time of $O(\log n)$ . This is in contrast to splay trees which have a worst-case time of $O(n)$ . The reduced node memory overhead compared to other self-balancing binary search trees can further improve locality of reference and caching.

### Insertion

Insertion is implemented with the same basic ideas as an unbalanced binary search tree, however with a few significant changes.

When finding the insertion point, the depth of the new node must also be recorded. This is implemented via a simple counter that gets incremented during each iteration of the lookup, effectively counting the number of edges between the root and the inserted node. If this node violates the α-height-balance property (defined above), a rebalance is required.

To rebalance, an entire subtree rooted at a **scapegoat** undergoes a balancing operation. The scapegoat is defined as being an ancestor of the inserted node which isn't α-weight-balanced. There will always be at least one such ancestor. Rebalancing any of them will restore the α-height-balanced property.

One way of finding a scapegoat, is to climb from the new node back up to the root and select the first node that isn't α-weight-balanced.

Climbing back up to the root requires $O(\log n)$ storage space, usually allocated on the stack, or parent pointers. This can actually be avoided by pointing each child at its parent as you go down, and repairing on the walk back up.

To determine whether a potential node is a viable scapegoat, we need to check its α-weight-balanced property. To do this we can go back to the definition:

```
size(left) ≤ α*size(node)
size(right) ≤ α*size(node)
```

However a large optimization can be made by realizing that we already know two of the three sizes, leaving only the third to be calculated.

Consider the following example to demonstrate this. Assuming that we're climbing back up to the root:

```
size(parent) = size(node) + size(sibling) + 1
```

But as:

```
size(inserted node) = 1.
```

The case is trivialized down to:

```
size[x+1] = size[x] + size(sibling) + 1
```

Where x = this node, x + 1 = parent and size(sibling) is the only function call actually required.

Once the scapegoat is found, the subtree rooted at the scapegoat is completely rebuilt to be perfectly balanced. This can be done in $O(n)$ time by traversing the nodes of the subtree to find their values in sorted order and recursively choosing the median as the root of the subtree.

As rebalance operations take $O(n)$ time (dependent on the number of nodes of the subtree), insertion has a worst-case performance of $O(n)$ time. However, because these worst-case scenarios are spread out, insertion takes $O(\log n)$ amortized time.

#### Sketch of proof for cost of insertion

Scapegoat trees are loosely height balanced, having a height of at most $\lfloor \log _{1/\alpha }n\rfloor$ , which is $O(\log n)$ by 0.5 < α < 1. The cost of finding the insertion point and placing the node is bounded by the height, which is $O(\log n)$ . Following the insertion, there may be a rebalancing that can cost up to $O(n)$ . We will now show that the cost of rebalancing is amortized $O(\log n)$ per insertion.

Define the Imbalance of a node *v* to be the absolute value of the difference in size between its left node and right node minus 1, or 0, whichever is greater. In other words:

$I(v)=\operatorname {max} (|\operatorname {left} (v)-\operatorname {right} (v)|-1,0)$

Additionally, we define the imbalance of a subtree to be the sum of the imbalance of the nodes in the subtree.

**Lemma 1:** Immediately before rebuilding the subtree rooted at v , $I(v)\in \Omega (|v|)$ ( $\Omega$ is Big Omega notation.)

Proof:

By definition, the scapegoat node is not α-weight-balanced, thus a child subtree has size at least $\alpha |v|$ , and the sibling subtree has size at most $(1-\alpha )|v|$ . The imbalance of the node v is then $I(v)\geq |\alpha |v|-(1-\alpha )|v||-1=|2\alpha -1||v|-1$ , and as $\alpha >0.5$ is a fixed constant, $I(V)=\Omega (|V|)$ . Thus, the imbalance of the subtree rooted at v is also $\Omega (|V|)$ .

**Lemma 2:** Immediately after rebuilding a subtree rooted at v , $I(v)=0$ .

Proof:

The rebuilt tree is perfectly balanced, such that the size of subtrees rooted at the same level differ by at most 1. By the above definition of imbalance, the imbalance of all nodes in the subtree is then 0.

**Theorem 3:** The amortized cost of insertion is $O(\log n)$ .

Proof:

As any $O(|v|)$ rebuild reduces $I(v)$ by $\Omega (|v|)-0=\Omega (|v|)$ by Lemmas 1 and 2, the cost of repairing each unit of imbalance is

${O(|v|) \over \Omega (|v|)}=O(1)$ .

Every insertion can introduce at most 1 unit of imbalance into all subtrees containing it. The inserted node can only be in at most 1 subtree per level of the tree, meaning the number of subtrees including it is bounded by the height of the tree, which is $O(\log n)$ . As every unit of imbalance costs $O(1)$ to fix, resulting in an amortized cost of rebalancing per insertion insertion of

$O(\log n)O(1)=O(\log n)$ .

By adding the costs of the initial search phase and rebalancing, the amortized cost of insertion is thus

$O(\log n)+O(\log n)=O(\log n)$ .

This bound holds for all 0.5 < α < 1.

### Deletion

Scapegoat trees are unusual in that deletion is easier than insertion. To enable deletion, scapegoat trees need to store an additional value with the tree data structure. This property, which we will call MaxNodeCount simply represents the highest achieved NodeCount. It is set to NodeCount whenever the entire tree is rebalanced, and after insertion is set to max(MaxNodeCount, NodeCount).

To perform a deletion, we simply remove the node as you would in a simple binary search tree, but if

```
NodeCount ≤ α*MaxNodeCount
```

then we rebalance the entire tree about the root, remembering to set MaxNodeCount to NodeCount.

This gives deletion a worst-case performance of $O(n)$ time, whereas the amortized time is $O(\log n)$ .

#### Sketch of proof for cost of deletion

Suppose the scapegoat tree has n elements and has just been rebuilt (in other words, it is a complete binary tree). At most $n/2-1$ deletions can be performed before the tree must be rebuilt. Each of these deletions take $O(\log n)$ time (the amount of time to search for the element and flag it as deleted). The $n/2$ deletion causes the tree to be rebuilt and takes $O(\log n)+O(n)$ (or just $O(n)$ ) time. Using aggregate analysis it becomes clear that the amortized cost of a deletion is $O(\log n)$ :

${\sum _{1}^{n/2}O(\log n)+O(n) \over n/2}={{n \over 2}O(\log n)+O(n) \over n/2}=O(\log n)\$

## Etymology

The name **Scapegoat tree** *"[...] is based on the common wisdom that, when something goes wrong, the first thing people tend to do is find someone to blame (the scapegoat)."* In the Bible, a scapegoat is an animal that is ritually burdened with the sins of others, and then driven away.
