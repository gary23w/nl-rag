---
title: "BK-tree"
source: https://en.wikipedia.org/wiki/BK-tree
domain: metric-space-tree
license: CC-BY-SA-4.0
tags: ball tree, vantage-point tree, metric tree, cover tree, nearest neighbor search
fetched: 2026-07-02
---

# BK-tree

A **BK-tree** (short for **Burkhard-Keller tree**) is a metric tree suggested by Walter Austin Burkhard and Robert M. Keller specifically adapted to discrete metric spaces. For simplicity, given a way to measure the **distance** between any two elements of a set, a BK-tree is built with a single root node and several subtrees, each connected to the root as a child. All nodes in a subtree have an equal distance to the root node, and the edge weight of the edge connecting the subtree to the root is equal to the distance. As shown in the picture. Also, each subtree of a BK-tree is a BK-tree.

BK-trees can be used for approximate string matching in a dictionary . The problem is formulated as follows: Given a pattern string $P=p_{1}p_{2}...p_{m}$ and a text string $T=t_{1}t_{2}\dots t_{n}$ , we need to find a substring $T_{j',j}=t_{j'}\dots t_{j}$ in T , which, of all substrings of T , has the smallest edit distance to the pattern P .

An ordinary way using BK-tree is to insert all $\Theta (n^{2})$ substrings of T and the pattern string P into the BK-tree, and find the subtree containing nodes with the smallest distance from the root. This will lead to a time complexity of $\Theta (n^{2}\log n)$ . However, this algorithm is very accurate and can find every substrings with the smallest edit distance to P .

## Example

This picture depicts the BK-tree for the set W of words {"book", "books", "cake", "boo", "boon", "cook", "cape", "cart"} obtained by using the Levenshtein distance

- each node u is labeled by a string of $w_{u}\in W$ ;
- each arc $(u,v)$ is labeled by $d_{uv}=d(w_{u},w_{v})$ where $w_{u}$ denotes the word assigned to u .

The BK-tree is built so that:

- for all node u of the BK-tree, the weight assigned to its egress arcs are distinct;
- for all arc $e=(u,v)$ labeled by k , each descendant $v'$ of v satisfies the following equation: $d(w_{u},w_{v'})=k$ :
  - *Example 1:* Consider the arc from "book" to "books". The distance between "book" and any word in {"books", "boo", "boon", "cook"} is equal to 1;
  - *Example 2:* Consider the arc from "books" to "boo". The distance between "books" and any word in {"boo", "boon", "cook"} is equal to 2.

## Insertion

The insertion primitive is used to populate a BK-tree t according to a discrete metric d .

**Input:**

- t : the BK-tree;
  - $d_{uv}$ denotes the weight assigned to an arc $(u,v)$ ;
  - $w_{u}$ denotes word assigned to a node u ;
- d : the discrete metric used by t (e.g. the Levenshtein distance);
- w : the element to be inserted into t ;

**Output:**

- The node of t corresponding to w

**Algorithm:**

- **If** the t is empty:
  - Create a root node r in t
  - $w_{r}\leftarrow w$
  - **Return** r
- Set u to the root of t
- **While** u exists:
  - $k\leftarrow d(w_{u},w)$
  - **If** $k=0$ :
    - **Return** u
  - Find v the child of u such that $d_{uv}=k$
  - **If** v is not found:
    - Create the node v
    - $w_{v}\leftarrow w$
    - Create the arc $(u,v)$
    - $d_{uv}\leftarrow k$
    - **Return** v
  - $u\leftarrow v$

## Lookup

Given a searched element w , the lookup primitive traverses the BK-tree to find the closest element of w . The key idea is to restrict the exploration of t to nodes that can only improve the best candidate found so far by taking advantage of the BK-tree organization and of the triangle inequality (cut-off criterion).

**Input:**

- t : the BK-tree;
- d : the corresponding discrete metric (e.g. the Levenshtein distance);
- w : the searched element;
- $d_{max}$ : the maximum distance allowed between the best match and w , defaults to $+\infty$ ;

**Output:**

- $w_{best}$ : the closest element to w stored in t and according to d or $\perp$ if not found;

**Algorithm:**

- **If** t is empty:
  - **Return** $\perp$
- Create S a set of nodes to process, and insert the root of t into S .
- $(w_{best},d_{best})\leftarrow (\perp ,d_{max})$
- **While** $S\neq \emptyset$ :
  - Pop an arbitrary node u from S
  - $d_{u}\leftarrow d(w,w_{u})$
  - **If** $d_{u}<d_{best}$ :
    - $(w_{best},d_{best})\leftarrow (w_{u},d_{u})$
  - **For each** egress-arc $(u,v)$ :
    - **If** $|d_{uv}-d_{u}|<d_{best}$ : (cut-off criterion)
      - Insert v into S .
- **Return** $w_{best}$

## Example of the lookup algorithm

Consider the example 8-node B-K Tree shown above and set $w=$ "cool". S is initialized to contain the root of the tree, which is subsequently popped as the first value of u with $w_{u}$ ="book". Further $d_{u}=2$ since the distance from "book" to "cool" is 2, and $d_{best}=2$ as this is the best (i.e. smallest) distance found thus far. Next each outgoing arc from the root is considered in turn: the arc from "book" to "books" has weight 1, and since $|1-2|=1$ is less than $d_{best}=2$ , the node containing "books" is inserted into S for further processing. The next arc, from "book" to "cake," has weight 4, and since $|4-2|=2$ is not less than $d_{best}=2$ , the node containing "cake" is not inserted into S . Therefore, the subtree rooted at "cake" will be pruned from the search, as the word closest to "cool" cannot appear in that subtree. To see why this pruning is correct, notice that a candidate word c appearing in "cake"s subtree having distance less than 2 to "cool" would violate the triangle inequality: the triangle inequality requires that for this set of three numbers (as sides of a triangle), no two can sum to less than the third, but here the distance from "cool" to "book" (which is 2) plus the distance from "cool" to c (which is less than 2) cannot reach or exceed the distance from "book" to "cake" (which is 4). Therefore, it is safe to disregard the entire subtree rooted at "cake".

Next the node containing "books" is popped from S and now $d_{u}=3$ , the distance from "cool" to "books." As $d_{u}>d_{best}$ , $d_{best}$ remains set at 2 and the single outgoing arc from the node containing "books" is considered. Next, the node containing "boo" is popped from S and $d_{u}=2$ , the distance from "cool" to "boo." This again does not improve upon $d_{best}=2$ . Each outgoing arc from "boo" is now considered; the arc from "boo" to "boon" has weight 1, and since $|2-1|=1<d_{best}=2$ , "boon" is added to S . Similarly, since $|2-2|=0<d_{best}$ , "cook" is also added to S .

Finally each of the two last elements in S are considered in arbitrary order: suppose the node containing "cook" is popped first, improving $d_{best}$ to distance 1, then the node containing "boon" is popped last, which has distance 2 from "cool" and therefore does not improve the best result. Finally, "cook" is returned as the answer $w_{best}$ with $d_{best}=1$ .

## Time Complexity

The efficiency of BK-trees depends strongly on the structure of the tree and the distribution of distances between stored elements.

In the **average case**, both insertion and lookup operations take $\Theta (\log n)$ time, assuming the tree remains relatively balanced and the distance metric distributes elements evenly.

In the **worst case**, when the data or distance function causes the tree to become highly unbalanced (for example, when many elements are at similar distances), both insertion and lookup can degrade to $\Theta (n)$ .

In practical applications, the actual performance depends on the choice of distance metric (e.g., the Levenshtein distance) and on the allowed search radius during approximate matching.
