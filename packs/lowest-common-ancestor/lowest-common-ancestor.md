---
title: "Lowest common ancestor"
source: https://en.wikipedia.org/wiki/Lowest_common_ancestor
domain: lowest-common-ancestor
license: CC-BY-SA-4.0
tags: lowest common ancestor, range minimum query, euler tour, tarjan offline lca
fetched: 2026-07-02
---

# Lowest common ancestor

In graph theory and computer science, the **lowest common ancestor** (**LCA**) (also called **least common ancestor**) of two nodes v and w in a tree or directed acyclic graph (DAG) T is the lowest (i.e. deepest) node that has both v and w as descendants, where we define each node to be a descendant of itself (so if v has a direct connection from w, w is the lowest common ancestor).

The LCA of v and w in T is the shared ancestor of v and w that is located farthest from the root. Computation of lowest common ancestors may be useful, for instance, as part of a procedure for determining the distance between pairs of nodes in a tree: the distance from v to w can be computed as the distance from the root to v, plus the distance from the root to w, minus twice the distance from the root to their lowest common ancestor (Djidjev, Pantziou & Zaroliagis 1991).

In a tree data structure where each node points to its parent, the lowest common ancestor can be easily determined by finding the first intersection of the paths from v and w to the root. In general, the computational time required for this algorithm is O(h) where h is the height of the tree (length of longest path from a leaf to the root). However, there exist several algorithms for processing trees so that lowest common ancestors may be found more quickly. Tarjan's off-line lowest common ancestors algorithm, for example, preprocesses a tree in linear time to provide constant-time LCA queries. In general DAGs, similar algorithms exist, but with super-linear complexity.

## History

The lowest common ancestor problem was defined by Alfred Aho, John Hopcroft, and Jeffrey Ullman (1973), but Dov Harel and Robert Tarjan (1984) were the first to develop an optimally efficient lowest common ancestor data structure. Their algorithm processes any tree in linear time, using a heavy path decomposition, so that subsequent lowest common ancestor queries may be answered in constant time per query. However, their data structure is complex and difficult to implement. Tarjan also found a simpler but less efficient algorithm, based on the union-find data structure, for computing lowest common ancestors of an offline batch of pairs of nodes.

Baruch Schieber and Uzi Vishkin (1988) simplified the data structure of Harel and Tarjan, leading to an implementable structure with the same asymptotic preprocessing and query time bounds. Their simplification is based on the principle that, in two special kinds of trees, lowest common ancestors are easy to determine: if the tree is a path, then the lowest common ancestor can be computed simply from the minimum of the levels of the two queried nodes, while if the tree is a complete binary tree, the nodes may be indexed in such a way that lowest common ancestors reduce to simple binary operations on the indices. The structure of Schieber and Vishkin decomposes any tree into a collection of paths, such that the connections between the paths have the structure of a binary tree, and combines both of these two simpler indexing techniques.

Omer Berkman and Uzi Vishkin (1993) discovered a completely new way to answer lowest common ancestor queries, again achieving linear preprocessing time with constant query time. Their method involves forming an Euler tour of a graph formed from the input tree by doubling every edge, and using this tour to write a sequence of level numbers of the nodes in the order the tour visits them; a lowest common ancestor query can then be transformed into a query that seeks the minimum value occurring within some subinterval of this sequence of numbers. They then handle this range minimum query problem (RMQ) by combining two techniques, one technique based on precomputing the answers to large intervals that have sizes that are powers of two, and the other based on table lookup for small-interval queries. This method was later presented in a simplified form by Michael Bender and Martin Farach-Colton (2000). As had been previously observed by Gabow, Bentley & Tarjan (1984), the range minimum problem can in turn be transformed back into a lowest common ancestor problem using the technique of Cartesian trees.

Further simplifications were made by Alstrup et al. (2004) and Fischer & Heun (2006).

Sleator and Tarjan (1983) proposed the dynamic LCA variant of the problem in which the data structure should be prepared to handle LCA queries intermixed with operations that change the tree (that is, rearrange the tree by adding and removing edges). This variant can be solved in $O(\log N)$ time in the total size of the tree for all modifications and queries. This is done by maintaining the forest using the dynamic trees data structure with partitioning by size; this then maintains a heavy-light decomposition of each tree, and allows LCA queries to be carried out in logarithmic time in the size of the tree.

As mentioned above, LCA can be reduced to RMQ. An efficient solution to the resulting RMQ problem starts by partitioning the number sequence into blocks. Two different techniques are used for queries across blocks and within blocks.

### Reduction from LCA to RMQ

Reduction of LCA to RMQ starts by walking the tree. For each node visited, record in sequence its label and depth. Suppose nodes *x* and *y* occur in positions *i* and *j* in this sequence, respectively. Then the LCA of *x* and *y* will be found in position RMQ(*i*, *j*), where the RMQ is taken over the depth values.

Despite that there exists a constant time and linear space solution for general RMQ, but a simplified solution can be applied that make uses of LCA’s properties. This simplified solution can only be used for RMQ reduced from LCA.

Similar to the solution mentioned above, we divide the sequence into each block $B_{i}$ , where each block $B_{i}$ has size of $b={1 \over 2}\log n$ .

By splitting the sequence into blocks, the $RMQ(i,j)$  query can be solved by solving two different cases:

#### Case 1: if i and j are in different blocks

To answer the $RMQ(i,j)$ query in case one, there are 3 groups of variables precomputed to help reduce query time.

First, the minimum element with the smallest index in each block $B_{i}$ is precomputed and denoted as $y_{i}$ . A set of $y_{i}$ takes $O(n/b)$ space.

Second, given the set of $y_{i}$ , the RMQ query for this set is precomputed using the solution with constant time and linearithmic space. There are $n/b$ blocks, so the lookup table in that solution takes $O({n \over b}\log {n \over b})$ space. Because $b={1 \over 2}\log n$ , $O({n \over b}\log {n \over b})$ = $O(n)$ space. Hence, the precomputed RMQ query using the solution with constant time and linearithmic space on these blocks only take $O(n)$ space.

Third, in each block $B_{i}$ , let $k_{i}$ be an index in $B_{i}$ such that $0\leq k_{i}<b$ . For all $k_{i}$ from 0 until b , block $B_{i}$ is divided into two intervals $[0,k_{i})$ and $[k_{i},b)$ . Then the minimum element with the smallest index for intervals in $[0,k_{i})$ and $[k_{i},b)$ in each block $B_{i}$ is precomputed. Such minimum elements are called as prefix min for the interval in $[0,k_{i})$ and suffix min for the interval in $[k_{i},b)$ . Each iteration of $k_{i}$ computes a pair of prefix min and suffix min. Hence, the total number of prefix mins and suffix mins in a block $B_{i}$ is $2b$ . Since there are $n/b$ blocks, in total, all prefix min and suffix min arrays take $O(2b\cdot {n \over b})$ which is $O(n)$ spaces.

In total, it takes $O(n)$ space to store all 3 groups of precomputed variables mentioned above.

Therefore, answering the $RMQ(i,j)$ query in case 1 is simply taking the minimum of the following three questions:

Let $B_{i}$ be the block that contains the element at index i , and $B_{j}$ for index j .

1. The suffix min in $[i\mod b,b)$ in the block $B_{i}$
2. Answering the RMQ query on a subset of y s from blocks $\{B_{i+1}...B_{j-1}\}$ using the solution with constant time and linearithmic space
3. The prefix min in $[0,j\mod b)$ in the block $B_{j}$

All 3 questions can be answered in constant time. Hence, case 1 can be answered in linear space and constant time.

#### Case 2: if i and j are in the same block

The sequence of RMQ that reduced from LCA has one property that a normal RMQ doesn’t have. The next element is always +1 or -1 from the current element. For example:

Therefore, each block $B_{i}$ can be encoded as a bitstring with 0 represents the current depth -1, and 1 represent the current depth +1. This transformation turns a block $B_{i}$ into a bitstring of size $b-1$ . A bitstring of size $b-1$ has $2^{b-1}$ possible bitstrings. Since $b={1 \over 2}\log n$ , so $2^{b-1}\leq 2^{b}=2^{{1 \over 2}\log n}=n^{1 \over 2}={\sqrt {n}}$ .

Hence, $B_{i}$ is always one of the ${\sqrt {n}}$ possible bitstring with size of $b-1$ .

Then, for each possible bitstring, we apply the naïve quadratic space constant time solution. This will take up ${\sqrt {n}}\cdot b^{2}$ spaces, which is $O({\sqrt {n}}\cdot (\log n)^{2})\leq O({\sqrt {n}}\cdot {\sqrt {n}})=O(n)$ .

Therefore, answering the $RMQ(i,j)$ query in case 2 is simply finding the corresponding block (in which is a bitstring) and perform a table lookup for that bitstring. Hence, case 2 can be solved using linear space with constant searching time.

## Extension to directed acyclic graphs

While originally studied in the context of trees, the notion of lowest common ancestors can be defined for directed acyclic graphs (DAGs), using either of two possible definitions. In both, the edges of the DAG are assumed to point from parents to children.

- Given *G* = (*V*, *E*), Aït-Kaci et al. (1989) define a poset (*V*, ≤) such that *x* ≤ *y* iff x is reachable from y. The lowest common ancestors of x and y are then the minimum elements under ≤ of the common ancestor set {*z* ∈ *V* | *x* ≤ *z* and *y* ≤ *z*}.
- Bender et al. (2005) gave an equivalent definition, where the lowest common ancestors of x and y are the nodes of out-degree zero in the subgraph of G induced by the set of common ancestors of x and y.

In a tree, the lowest common ancestor is unique; in a DAG of n nodes, each pair of nodes may have as much as *n*-2 LCAs (Bender et al. 2005), while the existence of an LCA for a pair of nodes is not even guaranteed in arbitrary connected DAGs.

A brute-force algorithm for finding lowest common ancestors is given by Aït-Kaci et al. (1989): find all ancestors of x and y, then return the maximum element of the intersection of the two sets. Better algorithms exist that, analogous to the LCA algorithms on trees, preprocess a graph to enable constant-time LCA queries. The problem of *LCA existence* can be solved optimally for sparse DAGs by means of an O(|*V*||*E*|) algorithm due to Kowaluk & Lingas (2005).

Dash et al. (2013) present a unified framework for preprocessing directed acyclic graphs to compute *a representative* lowest common ancestor in *a rooted DAG* in constant time. Their framework can achieve near-linear preprocessing times for sparse graphs and is available for public use.

## Applications

The problem of computing lowest common ancestors of classes in an inheritance hierarchy arises in the implementation of object-oriented programming systems (Aït-Kaci et al. 1989). The LCA problem also finds applications in models of complex systems found in distributed computing (Bender et al. 2005).
