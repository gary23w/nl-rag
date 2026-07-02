---
title: "Level ancestor problem"
source: https://en.wikipedia.org/wiki/Level_ancestor_problem
domain: lowest-common-ancestor
license: CC-BY-SA-4.0
tags: lowest common ancestor, range minimum query, euler tour, tarjan offline lca
fetched: 2026-07-02
---

# Level ancestor problem

In graph theory and theoretical computer science, the **level ancestor problem** is the problem of preprocessing a given rooted tree *T* into a data structure that can determine the ancestor of a given node at a given distance from the root of the tree.

More precisely, let *T* be a rooted tree with *n* nodes, and let *v* be an arbitrary node of *T*. The level ancestor query LA(*v*,*d*) requests the ancestor of node *v* at depth *d*, where the depth of a node *v* in a tree is the number of edges on the shortest path from the root of the tree to node *v*. It is possible to solve this problem in constant time per query, after a preprocessing algorithm that takes O(*n*) and that builds a data structure that uses O(*n*) storage space.

## Jump pointer algorithm

The jump pointer algorithm pre-processes a tree in O(*n* log *n*) time and answers level ancestor queries in O(log *n*) time. The jump pointer algorithm associates up to log *n* pointers to each vertex of the tree. These pointers are called jump pointers because they jump up the tree towards the root of the tree. For a given node *v* of a tree, the algorithm stores an array of length l jumpers where $\ell =\lfloor \log _{2}(\operatorname {depth} (v))\rfloor$ . The *i*th element of this array points to the 2*i*th ancestor of *v*. Using such data structure helps us jump halfway up the tree from any given node. When the algorithm is asked to process a query, we repeatedly jump up the tree using these pointers. The number of jumps will be at most log *n* and therefore queries can be answered in log *n* time.

## Ladder algorithm

The ladder algorithm is based on the idea of simplifying a tree into a collection of paths. The reason for this is the fact that paths are easier to be queried when it comes to level ancestor queries. Consider a path P consisting of n nodes rooted at a node r. We can store the path into an array of size n called Ladder and we can quickly answer a level ancestor query of LA(v, d) by returning Ladder[d] if depth(v)≤d. This will take O(*1*). However, this will only work if the given tree is a path. Otherwise, we need to decompose it into paths. This is done in two stages: long-path decomposition and extending the long paths into ladders.

### Stage 1: long-path decomposition

This is a recursive method that decomposes a given tree into paths. This stages starts off by finding the longest root-to-leaf path in the tree. It then removes this path by breaking its ties from the tree which will break the remaining of the tree into sub-trees and then it recursively processes each sub-tree. Every time a path is decomposed, an array is created in association with the path that contains the elements on the path from the root to the leaf. The base case of this recursion is when the tree is a path in which case its removal leaves an empty graph. Each vertex v has a unique ladder which is the ladder containing it and we call it the "v's ladder". However, after this pre-processing stage, the queries cannot be answered quickly. In fact in order to answer a level ancestor query, the algorithm needs to jump from a path to another until it reaches the root and there could be Θ(√*n*) of such paths on a leaf-to-root path. This leads us to an algorithm that can pre-process the tree in O(*n*) time and answers queries in O(√*n*). In order to reach the optimal query time, we need to process the results in a second stage described below.

### Stage 2: extending the long paths into ladders

The first stage of the algorithm decomposes the tree into a number of disjoint paths. In the second stage of the algorithm, each path is extended and therefore the resulting paths will not be mutually exclusive. In the first stage of the algorithm, each path is associated with an array of size *h'*. We extend this path by adding the *h'* immediate ancestors at the top of the path in the same array. This will extend each array twice its original size at most which will result in *2n* total number of nodes in all the ladders. Notice that the number of ladders is not changed and each node's ladder remains the same. Although a node v can be listed in multiple paths now but its ladder is the one that was associated to v in the first stage of the algorithm. These two stages can be processed in O(*n*) time but the query time is not constant yet. Consider a level ancestor query on a node u of height h. By travelling to the top of u's ladder, a vertex of height at least *2h* will be reached. Observe that all the nodes have a height of at least 1 and therefore after doing this i times, we reach a node of height at least 2i and therefore we need to do this at most log *n* times. This gives us a query time of O(log *n*).

### Stage 3: combining the two approaches

It turns out that the ladder algorithm does not do the trick on its own. In fact the jump pointer algorithm and the ladder algorithm complement one another. The two algorithms work in opposite directions: the jump pointer algorithm makes exponentially decreasing hops and the ladder algorithm makes exponentially increasing hops. A combination of the two algorithms can answer queries in O(*1*) time. A single jump pointer takes any query at least halfway up the tree after which climbing up only one ladder will answer the query. This results in O(*n* log *n*) pre-processing time and O(*1*) query time. The pre-processing can be further reduced to O(*n*) time by an application of the Method of Four Russians, in which the tree is reduced to a smaller tree with linear preprocessing, and a collection of very small trees, which are small enough that an exhaustive enumeration of all trees and the preprocessing of those trees is still O(*n*) time. Trees of size (log *n*)/4 suffice.

## Berkman and Vishkin's solution

A different solution is due to Berkman and Vishkin. This solution is based on the Euler tour technique for processing trees. The main observation is that LA(*v*,*d*) is the first node of depth *d* that appears in the Euler tour after the last appearance of *v*. Thus, by constructing the Euler tour and associated information on depth, the problem is reduced to a query on arrays, named *find smaller* (FS). For an array *A*, and a valid index *i*, FS(*i*,*x*) returns the first index *j*>*i* such that *A*[*i*]<*x* (here, we use *x*=*d*+1). An efficient solution to the FS problem is hard in general, but easier for the special case that arises from Euler tours; in this case, adjacent elements differ by ±1. This idea yields O(1) query time, with a preprocessing algorithm of complexity O(*n* log *n*). The preprocessing time is improved to O(*n*) by an application of the Method of Four Russians.
