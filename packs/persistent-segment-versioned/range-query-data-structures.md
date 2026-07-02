---
title: "Range query (computer science)"
source: https://en.wikipedia.org/wiki/Range_query_(data_structures)
domain: persistent-segment-versioned
license: CC-BY-SA-4.0
tags: persistent segment tree, versioned range query, path copying, functional data structure
fetched: 2026-07-02
---

# Range query (computer science)

(Redirected from

Range query (data structures)

)

In computer science, the **range query** problem consists of efficiently answering several queries regarding a given interval of elements within an array. For example, a common task, known as range minimum query, is finding the smallest value inside a given range within a list of numbers.

## Definition

Given a function f that accepts an array, a range query $f_{q}(l,r)$ on an array $a=[a_{1},..,a_{n}]$ takes two indices l and r and returns the result of f when applied to the subarray $[a_{l},\ldots ,a_{r}]$ . For example, for a function $\operatorname {sum}$ that returns the sum of all values in an array, the range query $\operatorname {sum} _{q}(l,r)$ returns the sum of all values in the range $[l,r]$ .

## Solutions

### Prefix sum array

Range sum queries may be answered in constant time and linear space by pre-computing an array p of same length as the input such that for every index i, the element pi is the sum of the first i elements of a. Any query may then be computed as follows: $\operatorname {sum} _{q}(l,r)=p_{r}-p_{l-1}.$

This strategy may be extended to any other binary operation f whose inverse function $f^{-1}$ is well-defined and easily computable. It can also be extended to higher dimensions with a similar pre-processing. For example, if pi,j contains the sum of the first *i* × *j* elements of a, then $\operatorname {sum} _{q}(l,r,t,b)=p_{r,b}-p_{l-1,b}-p_{r,t-1}+p_{l-1,t-1}.$

### Dynamic range queries

A more difficult subset of the problem consists of executing range queries on dynamic data; that is, data that may mutate between each query. In order to efficiently update array values, more sophisticated data structures like the segment tree or Fenwick tree are necessary.

## Examples

### Semigroup operators

When the function of interest in a range query is a semigroup operator, the notion of $f^{-1}$ is not always defined, so the strategy in the previous section does not work. Andrew Yao showed that there exists an efficient solution for range queries that involve semigroup operators. He proved that for any constant c, a pre-processing of time and space $\Theta (c\cdot n)$ allows to answer range queries on lists where f is a semigroup operator in $\theta (\alpha _{c}(n))$ time, where $\alpha _{c}$ is a certain functional inverse of the Ackermann function.

There are some semigroup operators that admit slightly better solutions. For instance when $f\in \{\max ,\min \}$ . Assume $f=\min$ then $\min(A[1..n])$ returns the index of the minimum element of $A[1..n]$ . Then ${\textstyle \min _{i,j}(A)}$ denotes the corresponding minimum range query. There are several data structures that allow to answer a range minimum query in $O(1)$ time using a pre-processing of time and space $O(n)$ . One such solution is based on the equivalence between this problem and the lowest common ancestor problem.

The Cartesian tree $T_{A}$ of an array $A[1,n]$ has as root $a_{i}=\min\{a_{1},a_{2},\ldots ,a_{n}\}$ and as left and right subtrees the Cartesian tree of $A[1,i-1]$ and the Cartesian tree of $A[i+1,n]$ respectively. A range minimum query ${\textstyle \min _{i,j}(A)}$ is the lowest common ancestor in $T_{A}$ of $a_{i}$ and $a_{j}$ . Because the lowest common ancestor can be solved in constant time using a pre-processing of time and space $O(n)$ , range minimum query can as well. The solution when $f=\max$ is analogous. Cartesian trees can be constructed in linear time.

### Mode

The mode of an array is the element that appears the most in it. For instance the mode of $a=[4,5,6,7,4]$ is 4. In case of a tie, any of the most frequent elements might be picked as the mode. A range mode query consists in pre-processing $A[1,n]$ such that we can find the mode in any range of $A[1,n]$ . Several data structures have been devised to solve this problem, we summarize some of the results in the following table.

| Space | Query Time | Restrictions |
|---|---|---|
| $O(n^{2-2\epsilon })$ | $O(n^{\epsilon }\log n)$ | $0\leq \epsilon \leq {\frac {1}{2}}$ |
| $O\left({\frac {n^{2}\log \log n}{\log n}}\right)$ | $O(1)$ |   |

Recently Jørgensen et al. proved a lower bound on the cell-probe model of $\Omega \left({\tfrac {\log n}{\log(Sw/n)}}\right)$ for any data structure that uses S cells.

### Median

This particular case is of special interest since finding the median has several applications. On the other hand, the median problem, a special case of the selection problem, is solvable in *O*(*n*), using the median of medians algorithm. However its generalization through range median queries is recent. A range median query $\operatorname {median} (A,i,j)$ where *A,i* and *j* have the usual meanings returns the median element of $A[i,j]$ . Equivalently, $\operatorname {median} (A,i,j)$ should return the element of $A[i,j]$ of rank ${\frac {j-i}{2}}$ . Range median queries cannot be solved by following any of the previous methods discussed above including Yao's approach for semigroup operators.

There have been studied two variants of this problem, the offline version, where all the *k* queries of interest are given in a batch, and a version where all the pre-processing is done up front. The offline version can be solved with $O(n\log k+k\log n)$ time and $O(n\log k)$ space.

The following pseudocode of the quickselect algorithm shows how to find the element of rank r in $A[i,j]$ an unsorted array of distinct elements, to find the range medians we set $r={\frac {j-i}{2}}$ .

```
rangeMedian(A, i, j, r) {
    if A.length() == 1
        return A[1]

    if A.low is undefined then
        m = median(A)
        A.low  = [e in A | e <= m]
        A.high = [e in A | e > m ]

    calculate t the number of elements of A[i, j] that belong to A.low

    if r <= t then
        return rangeMedian(A.low, i, j, r)
    else
        return rangeMedian(A.high, i, j, r-t)
}
```

Procedure `rangeMedian` partitions `A`, using `A`'s median, into two arrays `A.low` and `A.high`, where the former contains the elements of `A` that are less than or equal to the median `m` and the latter the rest of the elements of `A`. If we know that the number of elements of $A[i,j]$ that end up in `A.low` is `t` and this number is bigger than `r` then we should keep looking for the element of rank `r` in `A.low`; otherwise we should look for the element of rank $(r-t)$ in `A.high`. To find t, it is enough to find the maximum index $m\leq i-1$ such that $a_{m}$ is in `A.low` and the maximum index $l\leq j$ such that $a_{l}$ is in `A.high`. Then $t=l-m$ . The total cost for any query, without considering the partitioning part, is $\log n$ since at most $\log n$ recursion calls are done and only a constant number of operations are performed in each of them (to get the value of t fractional cascading should be used). If a linear algorithm to find the medians is used, the total cost of pre-processing for k range median queries is $n\log k$ . The algorithm can also be modified to solve the online version of the problem.

### Majority

Finding frequent elements in a given set of items is one of the most important tasks in data mining. Finding frequent elements might be a difficult task to achieve when most items have similar frequencies. Therefore, it might be more beneficial if some threshold of significance was used for detecting such items. One of the most famous algorithms for finding the majority of an array was proposed by Boyer and Moore which is also known as the Boyer–Moore majority vote algorithm. Boyer and Moore proposed an algorithm to find the majority element of a string (if it has one) in $O(n)$ time and using $O(1)$ space. In the context of Boyer and Moore's work and generally speaking, a majority element in a set of items (for example string or an array) is one whose number of instances is more than half of the size of that set. Few years later, Misra and Gries proposed a more general version of Boyer and Moore's algorithm using $O\left(n\log \left({\frac {1}{\tau }}\right)\right)$ comparisons to find all items in an array whose relative frequencies are greater than some threshold $0<\tau <1$ . A range $\tau$ -majority query is one that, given a subrange of a data structure (for example an array) of size $|R|$ , returns the set of all distinct items that appear more than (or in some publications equal to) $\tau |R|$ times in that given range. In different structures that support range $\tau$ -majority queries, $\tau$ can be either static (specified during pre-processing) or dynamic (specified at query time). Many of such approaches are based on the fact that, regardless of the size of the range, for a given $\tau$ there could be at most $O(1/\tau )$ distinct *candidates* with relative frequencies at least $\tau$ . By verifying each of these candidates in constant time, $O(1/\tau )$ query time is achieved. A range $\tau$ -majority query is decomposable in the sense that a $\tau$ -majority in a range R with partitions $R_{1}$ and $R_{2}$ must be a $\tau$ -majority in either $R_{1}$ or $R_{2}$ . Due to this decomposability, some data structures answer $\tau$ -majority queries on one-dimensional arrays by finding the Lowest common ancestor (LCA) of the endpoints of the query range in a Range tree and validating two sets of candidates (of size $O(1/\tau )$ ) from each endpoint to the lowest common ancestor in constant time resulting in $O(1/\tau )$ query time.

#### Two-dimensional arrays

Gagie et al. proposed a data structure that supports range $\tau$ -majority queries on an $m\times n$ array A . For each query $\operatorname {Q} =(\operatorname {R} ,\tau )$ in this data structure a threshold $0<\tau <1$ and a rectangular range $\operatorname {R}$ are specified, and the set of all elements that have relative frequencies (inside that rectangular range) greater than or equal to $\tau$ are returned as the output. This data structure supports dynamic thresholds (specified at query time) and a pre-processing threshold $\alpha$ based on which it is constructed. During the pre-processing, a set of *vertical* and *horizontal* intervals are built on the $m\times n$ array. Together, a vertical and a horizontal interval form a *block.* Each block is part of a *superblock* nine times bigger than itself (three times the size of the block's horizontal interval and three times the size of its vertical one). For each block a set of candidates (with ${\frac {9}{\alpha }}$ elements at most) is stored which consists of elements that have relative frequencies at least ${\frac {\alpha }{9}}$ (the pre-processing threshold as mentioned above) in its respective superblock. These elements are stored in non-increasing order according to their frequencies and it is easy to see that, any element that has a relative frequency at least $\alpha$ in a block must appear its set of candidates. Each $\tau$ -majority query is first answered by finding the *query block,* or the biggest block that is contained in the provided query rectangle in $O(1)$ time. For the obtained query block, the first ${\frac {9}{\tau }}$ candidates are returned (without being verified) in $O(1/\tau )$ time, so this process might return some false positives. Many other data structures (as discussed below) have proposed methods for verifying each candidate in constant time and thus maintaining the $O(1/\tau )$ query time while returning no false positives. The cases in which the query block is smaller than $1/\alpha$ are handled by storing $\log \left({\frac {1}{\alpha }}\right)$ different instances of this data structure of the following form:

$\beta =2^{-i},\;\;i\in \left\{1,\dots ,\log \left({\frac {1}{\alpha }}\right)\right\}$

where $\beta$ is the pre-processing threshold of the i -th instance. Thus, for query blocks smaller than $1/\alpha$ the $\lceil \log(1/\tau )\rceil$ -th instance is queried. As mentioned above, this data structure has query time $O(1/\tau )$ and requires $O\left(mn(H+1)\log ^{2}\left({\frac {1}{\alpha }}\right)\right)$ bits of space by storing a Huffman-encoded copy of it (note the $\log({\frac {1}{\alpha }})$ factor and also see Huffman coding).

#### One-dimensional arrays

Chan et al. proposed a data structure that given a one-dimensional array A , a subrange R of A (specified at query time) and a threshold $\tau$ (specified at query time), is able to return the list of all $\tau$ -majorities in $O(1/\tau )$ time requiring $O(n\log n)$ words of space. To answer such queries, Chan et al. begin by noting that there exists a data structure capable of returning the *top-k* most frequent items in a range in $O(k)$ time requiring $O(n)$ words of space. For a one-dimensional array $A[0,..,n-1]$ , let a one-sided top-k range query to be of form $A[0..i]{\text{ for }}0\leq i\leq n-1$ . For a maximal range of ranges $A[0..i]{\text{ through }}A[0..j]$ in which the frequency of a distinct element e in A remains unchanged (and equal to f ), a horizontal line segment is constructed. The x -interval of this line segment corresponds to $[i,j]$ and it has a y -value equal to f . Since adding each element to A changes the frequency of exactly one distinct element, the aforementioned process creates $O(n)$ line segments. Moreover, for a vertical line $x=i$ all horizontal line segments intersecting it are sorted according to their frequencies. Note that, each horizontal line segment with x -interval $[\ell ,r]$ corresponds to exactly one distinct element e in A , such that $A[\ell ]=e$ . A top-k query can then be answered by shooting a vertical ray $x=i$ and reporting the first k horizontal line segments that intersect it (remember from above that these line segments are already sorted according to their frequencies) in $O(k)$ time.

Chan et al. first construct a range tree in which each branching node stores one copy of the data structure described above for one-sided range top-k queries and each leaf represents an element from A . The top-k data structure at each node is constructed based on the values existing in the subtrees of that node and is meant to answer one-sided range top-k queries. Please note that for a one-dimensional array A , a range tree can be constructed by dividing A into two halves and recursing on both halves; therefore, each node of the resulting range tree represents a range. It can also be seen that this range tree requires $O(n\log n)$ words of space, because there are $O(\log n)$ levels and each level $\ell$ has $2^{\ell }$ nodes. Moreover, since at each level $\ell$ of a range tree all nodes have a total of n elements of A at their subtrees and since there are $O(\log n)$ levels, the space complexity of this range tree is $O(n\log n)$ .

Using this structure, a range $\tau$ -majority query $A[i..j]$ on $A[0..n-1]$ with $0\leq i\leq j\leq n$ is answered as follows. First, the lowest common ancestor (LCA) of leaf nodes i and j is found in constant time. Note that there exists a data structure requiring $O(n)$ bits of space that is capable of answering the LCA queries in $O(1)$ time. Let z denote the LCA of i and j , using z and according to the decomposability of range $\tau$ -majority queries (as described above and in ), the two-sided range query $A[i..j]$ can be converted into two one-sided range top-k queries (from z to i and j ). These two one-sided range top-k queries return the top-( $1/\tau$ ) most frequent elements in each of their respective ranges in $O(1/\tau )$ time. These frequent elements make up the set of *candidates* for $\tau$ -majorities in $A[i..j]$ in which there are $O(1/\tau )$ candidates some of which might be false positives. Each candidate is then assessed in constant time using a linear-space data structure (as described in Lemma 3 in ) that is able to determine in $O(1)$ time whether or not a given subrange of an array A contains at least q instances of a particular element e .

#### Tree paths

Gagie et al. proposed a data structure which supports queries such that, given two nodes u and v in a tree, are able to report the list of elements that have a greater relative frequency than $\tau$ on the path from u to v . More formally, let T be a labelled tree in which each node has a label from an alphabet of size $\sigma$ . Let $label(u)\in [1,\dots ,\sigma ]$ denote the label of node u in T . Let $P_{uv}$ denote the unique path from u to v in T in which middle nodes are listed in the order they are visited. Given T , and a fixed (specified during pre-processing) threshold $0<\tau <1$ , a query $Q(u,v)$ must return the set of all labels that appear more than $\tau |P_{uv}|$ times in $P_{uv}$ .

To construct this data structure, first ${O}(\tau n)$ nodes are *marked*. This can be done by marking any node that has distance at least $\lceil 1/\tau \rceil$ from the bottom of the three (height) and whose depth is divisible by $\lceil 1/\tau \rceil$ . After doing this, it can be observed that the distance between each node and its nearest marked ancestor is less than $2\lceil 1/\tau \rceil$ . For a marked node x , $\log(depth(x))$ different sequences (paths towards the root) $P_{i}(x)$ are stored,

$P_{i}(x)=\left\langle \operatorname {label} (x),\operatorname {par} (x),\operatorname {par} ^{2}(x),\ldots ,\operatorname {par} ^{2^{i}}(x)\right\rangle$

for $0\leq i\leq \log(depth(x))$ where $\operatorname {par} (x)$ returns the label of the direct parent of node x . Put another way, for each marked node, the set of all paths with a power of two length (plus one for the node itself) towards the root is stored. Moreover, for each $P_{i}(x)$ , the set of all majority *candidates* $C_{i}(x)$ are stored. More specifically, $C_{i}(x)$ contains the set of all $(\tau /2)$ -majorities in $P_{i}(x)$ or labels that appear more than $(\tau /2).(2^{i}+1)$ times in $P_{i}(x)$ . It is easy to see that the set of candidates $C_{i}(x)$ can have at most $2/\tau$ distinct labels for each i . Gagie et al. then note that the set of all $\tau$ -majorities in the path from any marked node x to one of its ancestors z is included in some $C_{i}(x)$ (Lemma 2 in ) since the length of $P_{i}(x)$ is equal to $(2^{i}+1)$ thus there exists a $P_{i}(x)$ for $0\leq i\leq \log(depth(x))$ whose length is between $d_{xz}{\text{ and }}2d_{xz}$ where $d_{xz}$ is the distance between x and z. The existence of such $P_{i}(x)$ implies that a $\tau$ -majority in the path from x to z must be a $(\tau /2)$ -majority in $P_{i}(x)$ , and thus must appear in $C_{i}(x)$ . It is easy to see that this data structure require $O(n\log n)$ words of space, because as mentioned above in the construction phase $O(\tau n)$ nodes are marked and for each marked node some candidate sets are stored. By definition, for each marked node $O(\log n)$ of such sets are stores, each of which contains $O(1/\tau )$ candidates. Therefore, this data structure requires $O(\log n\times (1/\tau )\times \tau n)=O(n\log n)$ words of space. Please note that each node x also stores $count(x)$ which is equal to the number of instances of $label(x)$ on the path from x to the root of T , this does not increase the space complexity since it only adds a constant number of words per node.

Each query between two nodes u and v can be answered by using the decomposability property (as explained above) of range $\tau$ -majority queries and by breaking the query path between u and v into four subpaths. Let z be the lowest common ancestor of u and v , with x and y being the nearest marked ancestors of u and v respectively. The path from u to v is decomposed into the paths from u and v to x and y respectively (the size of these paths are smaller than $2\lceil 1/\tau \rceil$ by definition, all of which are considered as candidates), and the paths from x and y to z (by finding the suitable $C_{i}(x)$ as explained above and considering all of its labels as candidates). Please note that, boundary nodes have to be handled accordingly so that all of these subpaths are disjoint and from all of them a set of $O(1/\tau )$ candidates is derived. Each of these candidates is then verified using a combination of the $labelanc(x,\ell )$ query which returns the lowest ancestor of node x that has label $\ell$ and the $count(x)$ fields of each node. On a w -bit RAM and an alphabet of size $\sigma$ , the $labelanc(x,\ell )$ query can be answered in $O\left(\log \log _{w}\sigma \right)$ time whilst having linear space requirements. Therefore, verifying each of the $O(1/\tau )$ candidates in $O\left(\log \log _{w}\sigma \right)$ time results in $O\left((1/\tau )\log \log _{w}\sigma \right)$ total query time for returning the set of all $\tau$ -majorities on the path from u to v .

All the problems described above have been studied for higher dimensions as well as their dynamic versions. On the other hand, range queries might be extended to other data structures like trees, such as the level ancestor problem. A similar family of problems are orthogonal range queries, also known as counting queries.
