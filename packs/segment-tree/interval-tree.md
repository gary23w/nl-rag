---
title: "Interval tree"
source: https://en.wikipedia.org/wiki/Interval_tree
domain: segment-tree
license: CC-BY-SA-4.0
tags: segment tree, range query structure, interval tree, range minimum query
fetched: 2026-07-02
---

# Interval tree

In computer science, an **interval tree** is a tree data structure to hold intervals. Specifically, it allows one to efficiently find all intervals that overlap with any given interval or point. It is often used for windowing queries, for instance, to find all roads on a computerized map inside a rectangular viewport, or to find all visible elements inside a three-dimensional scene. A similar data structure is the segment tree.

The trivial solution is to visit each interval and test whether it intersects the given point or interval, which requires $O(n)$ time, where n is the number of intervals in the collection. Since a query may return all intervals, for example if the query is a large interval intersecting all intervals in the collection, this is asymptotically optimal; however, output-sensitive algorithms, where the runtime is expressed in terms of m (the number of intervals produced by the query) may also be considered. Interval trees have a query time of $O(\log n+m)$ and an initial creation time of $O(n\log n)$ , while limiting memory consumption to $O(n)$ . After creation, interval trees may be dynamic, allowing efficient insertion and deletion of an interval in $O(\log n)$ time. If the endpoints of intervals are within a small integer range (*e.g.*, in the range $[1,\ldots ,O(n)]$ ), faster and in fact optimal data structures exist with preprocessing time $O(n)$ and query time $O(1+m)$ for reporting m intervals containing a given query point (see for a very simple one).

## Naïve approach

In a simple case, the intervals do not overlap and they can be inserted into a simple binary search tree and queried in $O(\log n)$ time. However, with arbitrarily overlapping intervals, there is no way to compare two intervals for insertion into the tree since orderings sorted by the beginning points or the ending points may be different. A naïve approach might be to build two parallel trees, one ordered by the beginning point, and one ordered by the ending point of each interval. This allows discarding half of each tree in $O(\log n)$ time, but the results must be merged, requiring $O(n)$ time. This returns queries in $O(n+\log n)=O(n)$ , which is no better than brute-force.

Interval trees solve this problem. This article describes two alternative designs for an interval tree, dubbed the *centered interval tree* and the *augmented tree*.

## Centered interval tree

Queries require $O(\log n+m)$ time, with n being the total number of intervals and m being the number of reported results. Construction requires $O(n\log n)$ time, and storage requires $O(n)$ space.

### Construction

Given a set of n intervals on the number line, a data structure needs to be constructed so that all intervals overlapping another interval or point can be efficiently retrieved.

First, the entire range of all the intervals is taken and divided in half at $x_{\textrm {center}}$ (in practice, $x_{\textrm {center}}$ should be picked to keep the tree relatively balanced). This gives three sets of intervals, those completely to the left of $x_{\textrm {center}}$ , called $S_{\textrm {left}}$ , those completely to the right of $x_{\textrm {center}}$ , called $S_{\textrm {right}}$ , and those overlapping $x_{\textrm {center}}$ , called $S_{\textrm {center}}$ .

The intervals in $S_{\textrm {left}}$ and $S_{\textrm {right}}$ are recursively divided in the same manner until there are no intervals left.

The intervals in $S_{\textrm {center}}$ that overlap the center point are stored in a separate data structure linked to the node in the interval tree. This data structure consists of two lists, one containing all the intervals sorted by their beginning points, and another containing all the intervals sorted by their ending points.

The result is a binary tree with each node storing:

- A center point
- A pointer to another node containing all intervals completely to the left of the center point
- A pointer to another node containing all intervals completely to the right of the center point
- All intervals overlapping the center point sorted by their beginning point
- All intervals overlapping the center point sorted by their ending point

### Intersecting

Interval trees allow for quickly computing all the ranges overlapping any input.

#### With a point

The task is to find all intervals in the tree that overlap a given point x . The tree is walked with a similar recursive algorithm as would be used to traverse a traditional binary tree, but with extra logic to support searching the intervals overlapping the "center" point at each node.

For each tree node, x is compared to $x_{\textrm {center}}$ , the midpoint used in node construction above. If x is less than $x_{\textrm {center}}$ , the leftmost set of intervals, $S_{\textrm {left}}$ , is considered. If x is greater than $x_{\textrm {center}}$ , the rightmost set of intervals, $S_{\textrm {right}}$ , is considered.

As each node is processed as the tree is traversed from the root to a leaf, the ranges in its $S_{\textrm {center}}$ are processed. If x is less than $x_{\textrm {center}}$ , all intervals in $S_{\textrm {center}}$ must end after x , or they could not also overlap $x_{\textrm {center}}$ . Therefore, it is only necessary find those intervals in $S_{\textrm {center}}$ that begin before x . The lists of $S_{\textrm {center}}$ , which have already been constructed, can be consulted. Since only the interval beginnings are relevant in this scenario, the list can be sorted by beginnings. If the closest number no greater than x is found in this list, all ranges from the beginning of the list to that found point overlap x because they begin before x and end after x (because they overlap $x_{\textrm {center}}$ which is larger than x ). Thus, the intervals in the list can be enumerated until the startpoint value exceeds x .

Likewise, if x is greater than $x_{\textrm {center}}$ , all intervals in $S_{\textrm {center}}$ must begin before x , so the intervals that end after x can be found using the list sorted by interval endings.

If x exactly matches $x_{\textrm {center}}$ , all intervals in $S_{\textrm {center}}$ can be added to the results without further processing and tree traversal can be stopped.

#### With an interval

For a result interval r to intersect the query interval q one of the following must hold:

- either the start or end point of r is in q ; or
- r completely encloses q .

We first find all intervals with start and/or end points inside q using a separately-constructed tree. In the one-dimensional case, we can use a search tree containing all the start and end points in the interval set, each with a pointer to its corresponding interval. A binary search in $O(\log n)$ time for the start and end of q reveals the minimum and maximum points to consider. Each point within this range references an interval that overlaps q and is added to the result list. Care must be taken to avoid duplicates, since an interval might both begin and end within q . This can be done using a binary flag on each interval to mark whether or not it has been added to the result set.

Finally, we must find intervals that enclose q . To find these, we pick any point inside q and use the algorithm above to find all intervals intersecting that point (again, being careful to remove duplicates).

### Higher dimensions

The interval tree data structure can be generalized to a higher dimension N with identical query and construction time and $O(n\log n)$ space.

First, a range tree in N dimensions is constructed that allows efficient retrieval of all intervals with beginning and end points inside the query region R . Once the corresponding ranges are found, the only thing that is left are those ranges that enclose the region in some dimension. To find these overlaps, N interval trees are created, and one axis intersecting R is queried for each. For example, in two dimensions, the bottom of the square R (or any other horizontal line intersecting R ) would be queried against the interval tree constructed for the horizontal axis. Likewise, the left (or any other vertical line intersecting R ) would be queried against the interval tree constructed on the vertical axis.

Each interval tree also needs an addition for higher dimensions. At each node we traverse in the tree, x is compared with $S_{\textrm {center}}$ to find overlaps. Instead of two sorted lists of points as was used in the one-dimensional case, a range tree is constructed. This allows efficient retrieval of all points in $S_{\textrm {center}}$ that overlap region R .

### Deletion

If after deleting an interval from the tree, the node containing that interval contains no more intervals, that node may be deleted from the tree. This is more complex than a normal binary tree deletion operation.

An interval may overlap the center point of several nodes in the tree. Since each node stores the intervals that overlap it, with all intervals completely to the left of its center point in the left subtree, similarly for the right subtree, it follows that each interval is stored in the node closest to the root from the set of nodes whose center point it overlaps.

Normal deletion operations in a binary tree (for the case where the node being deleted has two children) involve promoting a node further from the leaf to the position of the node being deleted (usually the leftmost child of the right subtree, or the rightmost child of the left subtree).

As a result of this promotion, some nodes that were above the promoted node will become its descendants; it is necessary to search these nodes for intervals that also overlap the promoted node, and move those intervals into the promoted node. As a consequence, this may result in new empty nodes, which must be deleted, following the same algorithm again.

### Balancing

The same issues that affect deletion also affect rotation operations; rotation must preserve the invariant that nodes are stored as close to the root as possible.

## Augmented tree

Another way to represent intervals is described in Cormen et al. (2009, Section 14.3: Interval trees, pp. 348–354).

Both insertion and deletion require $O(\log n)$ time, with n being the total number of intervals in the tree prior to the insertion or deletion operation.

An augmented tree can be built from a simple ordered tree, for example a binary search tree or self-balancing binary search tree, ordered by the 'low' values of the intervals. An extra annotation is then added to every node, recording the maximum upper value among all the intervals from this node down. Maintaining this attribute involves updating all ancestors of the node from the bottom up whenever a node is added or deleted. This takes only O(*h*) steps per node addition or removal, where *h* is the height of the node added or removed in the tree. If there are any tree rotations during insertion and deletion, the affected nodes may need updating as well.

Now, it is known that two intervals A and B overlap only when both $A_{\textrm {low}}\leq B_{\textrm {high}}$ and $A_{\textrm {high}}\geq B_{\textrm {low}}$ . When searching the trees for nodes overlapping with a given interval, you can immediately skip:

- all nodes to the right of nodes whose low value is past the end of the given interval.
- all nodes that have their maximum high value below the start of the given interval.

### Membership queries

Some performance may be gained if the tree avoids unnecessary traversals. These can occur when adding intervals that already exist or removing intervals that don't exist.

A total order can be defined on the intervals by ordering them first by their lower bounds and then by their upper bounds. Then, a membership check can be performed in $O(\log n)$ time, versus the $O(k+\log n)$ time required to find duplicates if k intervals overlap the interval to be inserted or removed. This solution has the advantage of not requiring any additional structures. The change is strictly algorithmic. The disadvantage is that membership queries take $O(\log n)$ time.

Alternately, at the rate of $O(n)$ memory, membership queries in expected constant time can be implemented with a hash table, updated in lockstep with the interval tree. This may not necessarily double the total memory requirement, if the intervals are stored by reference rather than by value.

### Java example: Adding a new interval to the tree

The key of each node is the interval itself, hence nodes are ordered first by low value and finally by high value, and the value of each node is the end point of the interval:

```mw
public void add(Interval i) {
    put(i, i.getEnd());
}
```

### Java example: Searching a point or an interval in the tree

To search for an interval, one walks the tree, using the key (`n.getKey()`) and high value (`n.getValue()`) to omit any branches that cannot overlap the query. The simplest case is a point query:

```mw
// Search for all intervals containing "p", starting with the
// node "n" and adding matching intervals to the list "result"
public void search(IntervalNode n, Point p, List<Interval> result) {
    // Don't search nodes that don't exist
    if (n == null)
        return;

    // If p is to the right of the rightmost point of any interval
    // in this node and all children, there won't be any matches.
    if (p.compareTo(n.getValue()) > 0)
        return;

    // Search left children
    search(n.getLeft(), p, result);

    // Check this node
    if (n.getKey().contains(p))
        result.add(n.getKey());

    // If p is to the left of the start of this interval,
    // then it can't be in any child to the right.
    if (p.compareTo(n.getKey().getStart()) < 0)
        return;

    // Otherwise, search right children
    search(n.getRight(), p, result);
}
```

where

a

.compareTo(

b

)

returns a negative value if a < b

a

.compareTo(

b

)

returns zero if a = b

a

.compareTo(

b

)

returns a positive value if a > b

The code to search for an interval is similar, except for the check in the middle:

```mw
// Check this node
if (n.getKey().overlapsWith(i))
    result.add (n.getKey());
```

`overlapsWith()` is defined as:

```mw
public boolean overlapsWith(Interval other) {
    return start.compareTo(other.getEnd()) <= 0 &&
           end.compareTo(other.getStart()) >= 0;
}
```

### Higher dimensions

Augmented trees can be extended to higher dimensions by cycling through the dimensions at each level of the tree. For example, for two dimensions, the odd levels of the tree might contain ranges for the *x*-coordinate, while the even levels contain ranges for the *y*-coordinate. This approach effectively converts the data structure from an augmented binary tree to an augmented kd-tree, thus significantly complicating the balancing algorithms for insertions and deletions.

A simpler solution is to use nested interval trees. First, create a tree using the ranges for the *y*-coordinate. Now, for each node in the tree, add another interval tree on the *x*-ranges, for all elements whose *y*-range is the same as that node's *y*-range.

The advantage of this solution is that it can be extended to an arbitrary number of dimensions using the same code base.

At first, the additional cost of the nested trees might seem prohibitive, but this is usually not so. As with the non-nested solution earlier, one node is needed per *x*-coordinate, yielding the same number of nodes for both solutions. The only additional overhead is that of the nested tree structures, one per vertical interval. This structure is usually of negligible size, consisting only of a pointer to the root node, and possibly the number of nodes and the depth of the tree.

## Medial- or length-oriented tree

A medial- or length-oriented tree is similar to an augmented tree, but symmetrical, with the binary search tree ordered by the medial points of the intervals. There is a maximum-oriented binary heap in every node, ordered by the length of the interval (or half of the length). Also we store the minimum and maximum possible value of the subtree in each node (thus the symmetry).

### Overlap test

Using only start and end values of two intervals $\left(a_{i},b_{i}\right)$ , for $i=0,1$ , the overlap test can be performed as follows:

$a_{0}<b_{1}$ and $a_{1}<b_{0}$

This can be simplified using the sum and difference:

$s_{i}=a_{i}+b_{i}$

$d_{i}=b_{i}-a_{i}$

Which reduces the overlap test to:

$\left|s_{1}-s_{0}\right|<d_{0}+d_{1}$

### Adding interval

Adding new intervals to the tree is the same as for a binary search tree using the medial value as the key. We push $d_{i}$ onto the binary heap associated with the node, and update the minimum and maximum possible values associated with all higher nodes.

### Searching for all overlapping intervals

Let's use $a_{q},b_{q},m_{q},d_{q}$ for the query interval, and $M_{n}$ for the key of a node (compared to $m_{i}$ of intervals)

Starting with root node, in each node, first we check if it is possible that our query interval overlaps with the node subtree using minimum and maximum values of node (if it is not, we don't continue for this node).

Then we calculate $\min \left\{d_{i}\right\}$ for intervals inside this node (not its children) to overlap with query interval (knowing $m_{i}=M_{n}$ ):

$\min \left\{d_{i}\right\}=\left|m_{q}-M_{n}\right|-d_{q}$

and perform a query on its binary heap for the $d_{i}$ 's bigger than $\min \left\{d_{i}\right\}$

Then we pass through both left and right children of the node, doing the same thing.

In the worst-case, we have to scan all nodes of the binary search tree, but since binary heap query is optimum, this is acceptable (a 2- dimensional problem can not be optimum in both dimensions)

This algorithm is expected to be faster than a traditional interval tree (augmented tree) for search operations. Adding elements is a little slower in practice, though the order of growth is the same.
