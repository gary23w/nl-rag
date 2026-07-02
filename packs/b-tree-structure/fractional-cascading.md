---
title: "Fractional cascading"
source: https://en.wikipedia.org/wiki/Fractional_cascading
domain: b-tree-structure
license: CC-BY-SA-4.0
tags: b-tree, multiway search tree, disk-based index, database index tree
fetched: 2026-07-02
---

# Fractional cascading

In computer science, **fractional cascading** is a technique to speed up a sequence of binary searches for the same value in a sequence of related data structures. The first binary search in the sequence takes a logarithmic amount of time, as is standard for binary searches, but successive searches in the sequence are faster. The original version of fractional cascading, introduced in two papers by Chazelle and Guibas in 1986 (Chazelle & Guibas 1986a; Chazelle & Guibas 1986b), combined the idea of cascading, originating in range searching data structures of Lueker (1978) and Willard (1978), with the idea of fractional sampling, which originated in Chazelle (1983). Later authors introduced more complex forms of fractional cascading that allow the data structure to be maintained as the data changes by a sequence of discrete insertion and deletion events.

## Example

As a simple example of fractional cascading, consider the following problem. We are given as input a collection of k ordered lists $L_{i}$ of numbers, such that the total length $\sum _{i}|L_{i}|$ of all lists is n , and must process them so that we can perform binary searches for a query value q in each of the k lists. For instance, with $k=4$ and $n=17$ ,

$L_{1}$

= 24, 64, 65, 80, 93

$L_{2}$

= 23, 25, 26

$L_{3}$

= 13, 44, 62, 66

$L_{4}$

= 11, 35, 46, 79, 81

The simplest solution to this searching problem is just to store each list separately. If we do so, the space requirement is $O(n)$ , but the time to perform a query is $O{\bigl (}k\log(n/k){\bigr )}$ , as we must perform a separate binary search in each of k lists. The worst case for querying this structure occurs when each of the k lists has equal size $n/k$ , so each of the k binary searches involved in a query takes time $O{\bigl (}\log(n/k){\bigr )}$ .

A second solution allows faster queries at the expense of more space: we may merge all the k lists into a single big list L , and associate with each item x of L a list of the results of searching for x in each of the smaller lists $L_{i}$ . If we describe an element of this merged list as $x[a,b,c,d]$ where x is the numerical value and a , b , c , and d are the positions (the first number has position 0) of the next element at least as large as x in each of the original input lists (or the position after the end of the list if no such element exists), then we would have

L

=

11

[0,0,0,0],

13

[0,0,0,1],

23

[0,0,1,1],

24

[0,1,1,1],

25

[1,1,1,1],

26

[1,2,1,1],

35

[1,3,1,1],

44

[1,3,1,2],

46

[1,3,2,2],

62

[1,3,2,3],

64

[1,3,3,3],

65

[2,3,3,3],

66

[3,3,3,3],

79

[3,3,4,3],

80

[3,3,4,4],

81

[4,3,4,4],

93

[4,3,4,5]

This merged solution allows a query in time $O(k+\log n)$ : simply search for q in L and then report the results stored at the item x found by this search. For instance, if $q=50$ , searching for q in L finds the item 62[1,3,2,3], from which we return the results $L_{1}[1]=64$ , $L_{2}[3]$ (a flag value indicating that q is past the end of $L_{2}$ ), $L_{3}[2]=62$ , and $L_{4}[3]=79$ . However, this solution pays a high penalty in space complexity: it uses space $O(kn)$ as each of the n items in L must store a list of k search results.

Fractional cascading allows this same searching problem to be solved with time and space bounds meeting the best of both worlds: query time $O(k+\log n)$ , and space $O(n)$ . The fractional cascading solution is to store a new sequence of lists $M_{i}$ . The final list in this sequence, $M_{k}$ , is equal to $L_{k}$ ; each earlier list $M_{i}$ is formed by merging $L_{i}$ with every second item from $M_{i+1}$ . With each item x in this merged list, we store two numbers: the position resulting from searching for x in $L_{i}$ and the position resulting from searching for x in $M_{i+1}$ . For the data above, this would give us the following lists:

$M_{1}$

=

24

[0, 1],

25

[1, 1],

35

[1, 3],

64

[1, 5],

65

[2, 5],

79

[3, 5],

80

[3, 6],

93

[4, 6]

$M_{2}$

=

23

[0, 1],

25

[1, 1],

26

[2, 1],

35

[3, 1],

62

[3, 3],

79

[3, 5]

$M_{3}$

=

13

[0, 1],

35

[1, 1],

44

[1, 2],

62

[2, 3],

66

[3, 3],

79

[4, 3]

$M_{4}$

=

11

[0, 0],

35

[1, 0],

46

[2, 0],

79

[3, 0],

81

[4, 0]

Suppose we wish to perform a query in this structure, for $q=50$ . We first do a standard binary search for q in $M_{1}$ , finding the value **64**[1,5]. The "1" in 64[1,5], tells us that the search for q in $L_{1}$ should return $L_{1}[1]=64$ . The "5" in **64**[1,5] tells us that the approximate location of q in $M_{2}$ is position 5. More precisely, binary searching for q in $M_{2}$ would return either the value 79[3,5] at position 5, or the value 62[3,3] one place earlier. By comparing q to 62, and observing that it is smaller, we determine that the correct search result in $M_{2}$ is 62[3,3]. The first "3" in 62[3,3] tells us that the search for q in $L_{2}$ should return $L_{2}[3]$ , a flag value meaning that q is past the end of list $L_{2}$ . The second "3" in 62[3,3] tells us that the approximate location of q in $M_{3}$ is position 3. More precisely, binary searching for q in $M_{3}$ would return either the value 62[2,3] at position 3, or the value 44[1,2] one place earlier. A comparison of q with the smaller value 44 shows us that the correct search result in $M_{3}$ is 62[2,3]. The "2" in 62[2,3] tells us that the search for q in $L_{3}$ should return $L_{3}[2]=62$ , and the "3" in 62[2,3] tells us that the result of searching for q in $M_{4}$ is either 79[3,0] at position 3 or 46[2,0] at position 2; comparing q with 46 shows that the correct result is 79[3,0] and that the result of searching for q in $L_{4}$ is $L_{4}[3]=79$ . Thus, we have found q in each of our four lists, by doing a binary search in the single list $M_{1}$ followed by a single comparison in each of the successive lists.

More generally, for any data structure of this type, we perform a query by doing a binary search for q in $M_{1}$ , and determining from the resulting value the position of q in $L_{1}$ . Then, for each $i>1$ , we use the known position of q in $M_{i}$ to find its position in $M_{i+1}$ . The value associated with the position of q in $M_{i}$ points to a position in $M_{i+1}$ that is either the correct result of the binary search for q in $M_{i+1}$ or is a single step away from that correct result, so stepping from i to $i+1$ requires only a single comparison. Thus, the total time for a query is $O(k+\log n)$

In our example, the fractionally cascaded lists have a total of 25 elements, less than twice that of the original input. In general, the size of $M_{i}$ in this data structure is at most $|L_{i}|+{\frac {1}{2}}|L_{i+1}|+{\frac {1}{4}}|L_{i+2}|+\cdots +{\frac {1}{2^{j}}}|L_{i+j}|+\cdots ,$ as may easily be proven by induction. Therefore, the total size of the data structure is at most $\sum |M_{i}|=\sum |L_{i}|\left(1+{\frac {1}{2}}+{\frac {1}{4}}+\cdots \right)\leq 2n=O(n),$ as may be seen by regrouping the contributions to the total size coming from the same input list $L_{i}$ together with each other.

## The general problem

In general, fractional cascading begins with a *catalog graph*, a directed graph in which each vertex is labeled with an ordered list. A query in this data structure consists of a path in the graph and a query value *q*; the data structure must determine the position of *q* in each of the ordered lists associated with the vertices of the path. For the simple example above, the catalog graph is itself a path, with just four nodes. It is possible for later vertices in the path to be determined dynamically as part of a query, in response to the results found by the searches in earlier parts of the path.

To handle queries of this type, for a graph in which each vertex has at most *d* incoming and at most *d* outgoing edges for some constant *d*, the lists associated with each vertex are augmented by a fraction of the items from each outgoing neighbor of the vertex; the fraction must be chosen to be smaller than 1/*d*, so that the total amount by which all lists are augmented remains linear in the input size. Each item in each augmented list stores with it the position of that item in the unaugmented list stored at the same vertex, and in each of the outgoing neighboring lists. In the simple example above, *d* = 1, and we augmented each list with a 1/2 fraction of the neighboring items.

A query in this data structure consists of a standard binary search in the augmented list associated with the first vertex of the query path, together with simpler searches at each successive vertex of the path. If a 1/*r* fraction of items are used to augment the lists from each neighboring item, then each successive query result may be found within at most *r* steps of the position stored at the query result from the previous path vertex, and therefore may be found in constant time without having to perform a full binary search.

## Dynamic fractional cascading

In *dynamic fractional cascading*, the list stored at each node of the catalog graph may change dynamically, by a sequence of updates in which list items are inserted and deleted. This causes several difficulties for the data structure.

First, when an item is inserted or deleted at a node of the catalog graph, it must be placed within the augmented list associated with that node, and may cause changes to propagate to other nodes of the catalog graph. Instead of storing the augmented lists in arrays, they should be stored as binary search trees, so that these changes can be handled efficiently while still allowing binary searches of the augmented lists.

Second, an insertion or deletion may cause a change to the subset of the list associated with a node that is passed on to neighboring nodes of the catalog graph. It is no longer feasible, in the dynamic setting, for this subset to be chosen as the items at every *d*th position of the list, for some *d*, as this subset would change too drastically after every update. Rather, a technique closely related to B-trees allows the selection of a fraction of data that is guaranteed to be smaller than 1/*d*, with the selected items guaranteed to be spaced a constant number of positions apart in the full list, and such that an insertion or deletion into the augmented list associated with a node causes changes to propagate to other nodes for a fraction of the operations that is less than 1/*d*. In this way, the distribution of the data among the nodes satisfies the properties needed for the query algorithm to be fast, while guaranteeing that the average number of binary search tree operations per data insertion or deletion is constant.

Third, and most critically, the static fractional cascading data structure maintains, for each element *x* of the augmented list at each node of the catalog graph, the index of the result that would be obtained when searching for *x* among the input items from that node and among the augmented lists stored at neighboring nodes. However, this information would be too expensive to maintain in the dynamic setting. Inserting or deleting a single value *x* could cause the indexes stored at an unbounded number of other values to change. Instead, dynamic versions of fractional cascading maintain several data structures for each node:

- A mapping of the items in the augmented list of the node to small integers, such that the ordering of the positions in the augmented list is equivalent to the comparison ordering of the integers, and a reverse map from these integers back to the list items. The order-maintenance technique of Dietz (1982) allows this numbering to be maintained efficiently.
- An integer searching data structure such as a van Emde Boas tree for the numbers associated with the input list of the node. With this structure, and the mapping from items to integers, one can efficiently find for each element *x* of the augmented list, the item that would be found on searching for *x* in the input list.
- For each neighboring node in the catalog graph, a similar integer searching data structure for the numbers associated with the subset of the data propagated from the neighboring node. With this structure, and the mapping from items to integers, one can efficiently find for each element *x* of the augmented list, a position within a constant number of steps of the location of *x* in the augmented list associated with the neighboring node.

These data structures allow dynamic fractional cascading to be performed at a time of O(log *n*) per insertion or deletion, and a sequence of *k* binary searches following a path of length *k* in the catalog graph to be performed in time O(log *n* + *k* log log *n*).

## Applications

Typical applications of fractional cascading involve range search data structures in computational geometry. For example, consider the problem of *half-plane range reporting*: that is, intersecting a fixed set of *n* points with a query half-plane and listing all the points in the intersection. The problem is to structure the points in such a way that a query of this type may be answered efficiently in terms of the intersection size *h*. One structure that can be used for this purpose is the convex layers of the input point set, a family of nested convex polygons consisting of the convex hull of the point set and the recursively-constructed convex layers of the remaining points. Within a single layer, the points inside the query half-plane may be found by performing a binary search for the half-plane boundary line's slope among the sorted sequence of convex polygon edge slopes, leading to the polygon vertex that is inside the query half-plane and farthest from its boundary, and then sequentially searching along the polygon edges to find all other vertices inside the query half-plane. The whole half-plane range reporting problem may be solved by repeating this search procedure starting from the outermost layer and continuing inwards until reaching a layer that is disjoint from the query halfspace. Fractional cascading speeds up the successive binary searches among the sequences of polygon edge slopes in each layer, leading to a data structure for this problem with space O(*n*) and query time O(log *n* + *h*). The data structure may be constructed in time O(*n* log *n*) by an algorithm of Chazelle (1985). As in our example, this application involves binary searches in a linear sequence of lists (the nested sequence of the convex layers), so the catalog graph is just a path.

Another application of fractional cascading in geometric data structures concerns point location in a monotone subdivision, that is, a partition of the plane into polygons such that any vertical line intersects any polygon in at most two points. As Edelsbrunner, Guibas & Stolfi (1986) showed, this problem can be solved by finding a sequence of polygonal paths that stretch from left to right across the subdivision, and binary searching for the lowest of these paths that is above the query point. Testing whether the query point is above or below one of the paths can itself be solved as a binary search problem, searching for the x coordinate of the points among the x coordinates of the path vertices to determine which path edge might be above or below the query point. Thus, each point location query can be solved as an outer layer of binary search among the paths, each step of which itself performs a binary search among x coordinates of vertices. Fractional cascading can be used to speed up the time for the inner binary searches, reducing the total time per query to O(log *n*) using a data structure with space O(*n*). In this application the catalog graph is a tree representing the possible search sequences of the outer binary search.

Beyond computational geometry, Lakshman & Stiliadis (1998) and Buddhikot, Suri & Waldvogel (1999) apply fractional cascading in the design of data structures for fast packet filtering in internet routers. Gao et al. (2004) use fractional cascading as a model for data distribution and retrieval in sensor networks.
