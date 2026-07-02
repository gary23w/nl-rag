---
title: "Segment tree"
source: https://en.wikipedia.org/wiki/Segment_tree
domain: sweep-line-paradigm
license: CC-BY-SA-4.0
tags: sweep line algorithm, event queue, plane sweep, status structure
fetched: 2026-07-02
---

# Segment tree

In computer science, the **segment tree** is a data structure used for storing information about intervals or segments. It allows querying which of the stored segments contain a given point. A similar data structure is the interval tree.

A segment tree for a set I of *n* intervals uses *O*(*n* log *n*) storage and can be built in *O*(*n* log *n*) time. Segment trees support searching for all the intervals that contain a query point in time *O*(log *n* + *k*), *k* being the number of retrieved intervals or segments.

Applications of the segment tree are in the areas of computational geometry, geographic information systems and machine learning.

The segment tree can be generalized to higher dimension spaces.

## Definition

### Description

Let I be a set of intervals, or segments. Let *p*1, *p*2, ..., *pm* be the list of distinct interval endpoints, sorted from left to right. Consider the partitioning of the real line induced by those points. The regions of this partitioning are called *elementary intervals*. Thus, the elementary intervals are, from left to right:

$(-\infty ,p_{1}),[p_{1},p_{1}],(p_{1},p_{2}),[p_{2},p_{2}],\dots ,(p_{m-1},p_{m}),[p_{m},p_{m}],(p_{m},+\infty )$

That is, the list of elementary intervals consists of open intervals between two consecutive endpoints *pi* and *p**i*+1, alternated with closed intervals consisting of a single endpoint. Single points are treated themselves as intervals because the answer to a query is not necessarily the same at the interior of an elementary interval and its endpoints.

Given a set I of intervals, or segments, a segment tree *T* for I is structured as follows:

- *T* is a binary tree.
- Its leaves correspond to the elementary intervals induced by the endpoints in I, in an ordered way: the leftmost leaf corresponds to the leftmost interval, and so on. The elementary interval corresponding to a leaf *v* is denoted Int(*v*).
- The internal nodes of *T* correspond to intervals that are the union of elementary intervals: the interval Int(*N*) corresponding to node *N* is the union of the intervals corresponding to the leaves of the tree rooted at *N*. That implies that Int(*N*) is the union of the intervals of its two children.
- Each node or leaf *v* in *T* stores the interval Int(*v*) and a set of intervals, in some data structure. This canonical subset of node *v* contains the intervals [*x*, *x′*] from I such that [*x*, *x′*] contains Int(*v*) and does not contain Int(parent(*v*)). That is, each node in *T* stores the segments that span through its interval, but do not span through the interval of its parent.

### Construction

A segment tree from the set of segments I, can be built as follows. First, the endpoints of the intervals in I are sorted. The elementary intervals are obtained from that. Then, a balanced binary tree is built on the elementary intervals, and for each node *v* it is determined the interval Int(*v*) it represents. It remains to compute the canonical subsets for the nodes. To achieve this, the intervals in I are inserted one by one into the segment tree. An interval *X* = [*x*, *x′*] can be inserted in a subtree rooted at *T*, using the following procedure:

- If Int(*T*) is contained in *X* then store *X* at *T*, and finish.
- Else:
  - If *X* intersects the interval of the left child of *T*, then insert *X* in that child, recursively.
  - If *X* intersects the interval of the right child of *T*, then insert *X* in that child, recursively.

The complete construction operation takes *O*(*n* log *n*) time, *n* being the number of segments in I.

Proof

Sorting the endpoints takes

O

(

n

log

n

). Building a balanced binary tree from the sorted endpoints, takes linear time on

n

.

The insertion of an interval

X

= [

x

,

x

′

] into the tree, costs O(log

n

).

Proof

Visiting every node takes constant time (assuming that canonical subsets are stored in a simple data structure like a linked list). When we visit node *v*, we either store *X* at *v*, or Int(*v*) contains an endpoint of *X*. As proved above, an interval is stored at most twice at each level of the tree. There is also at most one node at every level whose corresponding interval contains *x*, and one node whose interval contains *x′*. So, at most four nodes per level are visited. Since there are *O*(log *n*) levels, the total cost of the insertion is *O*(log *n*).

### Query

A query for a segment tree receives a point *qx*(should be one of the leaves of tree), and retrieves a list of all the segments stored which contain the point *qx*.

Formally stated; given a node (subtree) *v* and a query point *qx*, the query can be done using the following algorithm:

1. Report all the intervals in *I*(*v*).
2. If *v* is not a leaf:
  - If *qx* is in Int(left child of *v*) then
    - Perform a query in the left child of *v*.
  - If *qx* is in Int(right child of *v*) then
    - Perform a query in the right child of *v*.

In a segment tree that contains *n* intervals, those containing a given query point can be reported in *O*(log *n* + *k*) time, where *k* is the number of reported intervals.

Proof

The query algorithm visits one node per level of the tree, so *O*(log *n*) nodes in total. On the other hand, at a node *v*, the segments in I are reported in *O*(1 + *kv*) time, where *kv* is the number of intervals at node *v*, reported. The sum of all the *kv* for all nodes *v* visited, is *k*, the number of reported segments.

### Storage requirements

A segment tree *T* on a set I of *n* intervals uses *O*(*n* log *n*) storage.

***Lemma***— Any interval [*x*, *x′*] of I is stored in the canonical set for at most two nodes at the same depth.

Proof

Let *v*1, *v*2, *v*3 be the three nodes at the same depth, numbered from left to right; and let p(*v*) be the parent node of any given node *v*. Suppose [*x*, *x′*] is stored at *v*1 and *v*3. This means that [*x*, *x′*] spans the whole interval from the left endpoint of Int(*v*1) to the right endpoint of Int(*v*3). Note that all segments at a particular level are non-overlapping and ordered from left to right: this is true by construction for the level containing the leaves, and the property is not lost when moving from any level to the one above it by combining pairs of adjacent segments. Now either parent(*v*2) = parent(*v*1), or the former is to the right of the latter (edges in the tree do not cross). In the first case, Int(parent(*v*2))'s leftmost point is the same as Int(*v*1)'s leftmost point; in the second case, Int(parent(*v*2))'s leftmost point is to the right of Int(parent(*v*1))'s rightmost point, and therefore also to the right of Int(*v*1)'s rightmost point. In both cases, Int(parent(*v*2)) begins at or to the right of Int(*v*1)'s leftmost point. Similar reasoning shows that Int(parent(*v*2)) ends at or to the left of Int(*v*3)'s rightmost point. Int(parent(*v*2)) must therefore be contained in [*x*, *x′*]; hence, [*x*, *x′*] will not be stored at *v*2.

The set

I

has at most 4

n

+ 1 elementary intervals. Because

T

is a binary balanced tree with at most 4

n

+ 1 leaves, its height is O(log

n

). Since any interval is stored at most twice at a given depth of the tree, that the total amount of storage is

O

(

n

log

n

).

### Generalization for higher dimensions

The segment tree can be generalized to higher dimension spaces, in the form of multi-level segment trees. In higher dimensional versions, the segment tree stores a collection of axis-parallel (hyper-)rectangles, and can retrieve the rectangles that contain a given query point. The structure uses *O*(*n* log*d* *n*) storage, and answers queries in *O*(log*d* *n*) time.

The use of fractional cascading lowers the query time bound by a logarithmic factor. The use of the interval tree on the deepest level of associated structures lowers the storage bound by a logarithmic factor.
