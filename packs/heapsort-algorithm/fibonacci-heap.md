---
title: "Fibonacci heap"
source: https://en.wikipedia.org/wiki/Fibonacci_heap
domain: heapsort-algorithm
license: CC-BY-SA-4.0
tags: heapsort algorithm, binary heap, priority queue, in place sorting
fetched: 2026-07-02
---

# Fibonacci heap

In computer science, a **Fibonacci heap** is a data structure for priority queue operations, consisting of a collection of heap-ordered trees. It has a better amortized running time than many other priority queue data structures including the binary heap and binomial heap. Michael L. Fredman and Robert E. Tarjan developed Fibonacci heaps in 1984 and published them in a scientific journal in 1987. Fibonacci heaps are named after the Fibonacci numbers, which are used in their running time analysis.

The amortized times of all operations on Fibonacci heaps is constant, except *delete-min*. Deleting an element (most often used in the special case of deleting the minimum element) works in $O(\log n)$ amortized time, where n is the size of the heap. This means that starting from an empty data structure, any sequence of *a* insert and *decrease-key* operations and *b* *delete-min* operations would take $O(a+b\log n)$ worst case time, where n is the maximum heap size. In a binary or binomial heap, such a sequence of operations would take $O((a+b)\log n)$ time. A Fibonacci heap is thus better than a binary or binomial heap when b is smaller than a by a non-constant factor. It is also possible to merge two Fibonacci heaps in constant amortized time, improving on the logarithmic merge time of a binomial heap, and improving on binary heaps which cannot handle merges efficiently.

Using Fibonacci heaps improves the asymptotic running time of algorithms which utilize priority queues. For example, Dijkstra's algorithm and Prim's algorithm can be made to run in $O(|E|+|V|\log |V|)$ time.

## Structure

A Fibonacci heap is a collection of trees satisfying the minimum-heap property, that is, the key of a child is always greater than or equal to the key of the parent. This implies that the minimum key is always at the root of one of the trees. Compared with binomial heaps, the structure of a Fibonacci heap is more flexible. The trees do not have a prescribed shape and in the extreme case the heap can have every element in a separate tree. This flexibility allows some operations to be executed in a lazy manner, postponing the work for later operations. For example, merging heaps is done simply by concatenating the two lists of trees, and operation *decrease key* sometimes cuts a node from its parent and forms a new tree.

However, at some point order needs to be introduced to the heap to achieve the desired running time. In particular, degrees of nodes (here degree means the number of direct children) are kept quite low: every node has degree at most $\log n$ and the size of a subtree rooted in a node of degree k is at least $F_{k+2}$ , where $F_{i}$ is the i th Fibonacci number. This is achieved by the rule: at most one child can be cut off each non-root node. When a second child is cut, the node itself needs to be cut from its parent and becomes the root of a new tree (see Proof of degree bounds, below). The number of trees is decreased in the operation *delete-min*, where trees are linked together.

As a result of a relaxed structure, some operations can take a long time while others are done very quickly. For the amortized running time analysis, we use the potential method, in that we pretend that very fast operations take a little bit longer than they actually do. This additional time is then later combined and subtracted from the actual running time of slow operations. The amount of time saved for later use is measured at any given moment by a potential function. The potential $\phi$ of a Fibonacci heap is given by $\phi =t+2m,$ where t is the number of trees in the Fibonacci heap, and m is the number of marked nodes. A node is marked if at least one of its children was cut, since this node was made a child of another node (all roots are unmarked). The amortized time for an operation is given by the sum of the actual time and c times the difference in potential, where *c* is a constant (chosen to match the constant factors in the big O notation for the actual time).

Thus, the root of each tree in a heap has one unit of time stored. This unit of time can be used later to link this tree with another tree at amortized time 0. Also, each marked node has two units of time stored. One can be used to cut the node from its parent. If this happens, the node becomes a root and the second unit of time will remain stored in it as in any other root.

## Operations

To allow fast deletion and concatenation, the roots of all trees are linked using a circular doubly linked list. The children of each node are also linked using such a list. For each node, we maintain its number of children and whether the node is marked.

### Find-min

We maintain a pointer to the root containing the minimum key, allowing $O(1)$ access to the minimum. This pointer must be updated during the other operations, which adds only a constant time overhead.

### Merge

The merge operation simply concatenates the root lists of two heaps together and sets the minimum to be the smaller of the two heaps. This can be done in constant time, and the potential does not change, leading again to constant amortized time.

### Insert

The insertion operation can be considered a special case of the merge operation, with a single node. The node is simply appended to the root list, increasing the potential by one. The amortized cost is thus still constant.

### Delete-min

The delete-min operation does most of the work in restoring the structure of the heap. It has three phases:

1. The root containing the minimum element is removed, and each of its d children becomes a new root. It takes time $O(d)$ to process these new roots, and the potential increases by $d-1$ . Therefore, the amortized running time of this phase is $O(d)=O(\log n)$ .
2. There may be up to n roots. We therefore decrease the number of roots by successively linking together roots of the same degree. When two roots have the same degree, we make the one with the larger key a child of the other, so that the minimum heap property is conserved. The degree of the smaller root increases by one. This is repeated until every root has a different degree. To find trees of the same degree efficiently, we use an array of length $O(\log n)$ in which we keep a pointer to one root of each degree. When a second root is found of the same degree, the two are linked and the array is updated. The actual running time is $O(\log n+m)$ , where m is the number of roots at the beginning of the second phase. In the end, we will have at most $O(\log n)$ roots (because each has a different degree). Therefore, the difference in the potential from before to after this phase is $O(\log n)-m$ . Thus, the amortized running time is $O(\log n+m)+c(O(\log n)-m)$ . By choosing a sufficiently large c such that the terms in m cancel out, this simplifies to $O(\log n)$ .
3. Search the final list of roots to find the minimum, and update the minimum pointer accordingly. This takes $O(\log n)$ time, because the number of roots has been reduced.

Overall, the amortized time of this operation is $O(\log n)$ , provided that $d=O(\log n)$ . The proof of this is given in the following section.

### Decrease-key

If decreasing the key of a node x causes it to become smaller than its parent, then it is cut from its parent, becoming a new unmarked root. If it is also less than the minimum key, then the minimum pointer is updated.

We then initiate a series of *cascading cuts*, starting with the parent of x . As long as the current node is marked, it is cut from its parent and made an unmarked root. Its original parent is then considered. This process stops when we reach an unmarked node y . If y is not a root, it is marked. In this process we introduce some number, say k , of new trees. Except possibly x , each of these new trees loses its original mark. The terminating node y may become marked. Therefore, the change in the number of marked nodes is between of $-k$ and $-k+2$ . The resulting change in potential is $k+2(-k+2)=-k+4$ . The actual time required to perform the cutting was $O(k)$ . Hence, the amortized time is $O(k)+c(-k+4)$ , which is constant, provided c is sufficiently large.

## Proof of degree bounds

The amortized performance of a Fibonacci heap depends on the degree (number of children) of any tree root being $O(\log n)$ , where n is the size of the heap. Here we show that the size of the (sub)tree rooted at any node x of degree d in the heap must have size at least $F_{d+2}$ , where $F_{i}$ is the i th Fibonacci number. The degree bound follows from this and the fact (easily proved by induction) that $F_{d+2}\geq \varphi ^{d}$ for all integers $d\geq 0$ , where $\varphi =(1+{\sqrt {5}})/2\approx 1.618$ is the golden ratio. We then have $n\geq F_{d+2}\geq \varphi ^{d}$ , and taking the log to base $\varphi$ of both sides gives $d\leq \log _{\varphi }n$ as required.

Let x be an arbitrary node in a Fibonacci heap, not necessarily a root. Define $\mathrm {size} (x)$ to be the size of the tree rooted at x (the number of descendants of x , including x itself). We prove by induction on the height of x (the length of the longest path from x to a descendant leaf) that $\mathrm {size} (x)\geq F_{d+2}$ , where d is the degree of x .

**Base case:** If x has height 0 , then $d=0$ , and $\mathrm {size} (x)=1\geq F_{2}$ .

**Inductive case:** Suppose x has positive height and degree $d>0$ . Let $y_{1},y_{2}\dots y_{d}$ be the children of x , indexed in order of the times they were most recently made children of x ( $y_{1}$ being the earliest and $y_{d}$ the latest), and let $c_{1},c_{2}\dots c_{d}$ be their respective degrees.

We claim that $c_{i}\geq i-2$ for each i . Just before $y_{i}$ was made a child of x , $y_{1}\dots y_{i-1}$ were already children of x , and so x must have had degree at least $i-1$ at that time. Since trees are combined only when the degrees of their roots are equal, it must have been the case that $y_{i}$ also had degree at least $i-1$ at the time when it became a child of x . From that time to the present, $y_{i}$ could have only lost at most one child (as guaranteed by the marking process), and so its current degree $c_{i}$ is at least $i-2$ . This proves the claim.

Since the heights of all the $y_{i}$ are strictly less than that of x , we can apply the inductive hypothesis to them to get $\mathrm {size} (y_{i})\geq F_{c_{i}+2}\geq F_{(i-2)+2}=F_{i}.$ The nodes x and $y_{1}$ each contribute at least 1 to $\mathrm {size} (x)$ , and so we have ${\begin{aligned}\mathrm {size} (x)&\geq 2+\sum _{i=2}^{d}\mathrm {size} (y_{i})\\&\geq 2+\sum _{i=2}^{d}F_{i}\\&=1+\sum _{i=0}^{d}F_{i}\\&=F_{d+2}\end{aligned}}$ where the last step is an identity for Fibonacci numbers. This gives the desired lower bound on $\mathrm {size} (x)$ .

## Performance

Although Fibonacci heaps look very efficient, they have the following two drawbacks:

1. They are complicated to implement.
2. They are not as efficient in practice when compared with theoretically less efficient forms of heaps. In their simplest version, they require manipulation of four pointers per node, whereas only two or three pointers per node are needed in other structures, such as the binomial heap, or pairing heap. This results in large memory consumption per node and high constant factors on all operations.

Although the total running time of a sequence of operations starting with an empty structure is bounded by the bounds given above, some (very few) operations in the sequence can take very long to complete (in particular, delete-min has linear running time in the worst case). For this reason, Fibonacci heaps and other amortized data structures may not be appropriate for real-time systems.

It is possible to create a data structure which has the same worst-case performance as the Fibonacci heap has amortized performance. One such structure, the Brodal queue, is, in the words of the creator, "quite complicated" and "[not] applicable in practice." Invented in 2012, the strict Fibonacci heap is a simpler (compared to Brodal's) structure with the same worst-case bounds. Despite being simpler, experiments show that in practice the strict Fibonacci heap performs slower than more complicated Brodal queue and also slower than basic Fibonacci heap. The run-relaxed heaps of Driscoll et al. give good worst-case performance for all Fibonacci heap operations except merge. Recent experimental results suggest that the Fibonacci heap is more efficient in practice than most of its later derivatives, including quake heaps, violation heaps, strict Fibonacci heaps, and rank pairing heaps, but less efficient than pairing heaps or array-based heaps.

## Summary of running times

Here are time complexities of various heap data structures. The abbreviation am. indicates that the given complexity is amortized, otherwise it is a worst-case complexity. For the meaning of "*O*(*f*)" and "*Θ*(*f*)" see Big O notation. Names of operations assume a min-heap.

| Operation | find-min | delete-min | decrease-key | insert | meld | make-heap |
|---|---|---|---|---|---|---|
| Binary | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(*n*) | *Θ*(*n*) |
| Skew | *Θ*(1) | *O*(log *n*) am. | *O*(log *n*) am. | *O*(log *n*) am. | *O*(log *n*) am. | *Θ*(*n*) am. |
| Leftist | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(*n*) |
| Binomial | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(1) am. | *Θ*(log *n*) | *Θ*(*n*) |
| Skew binomial | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(1) | *Θ*(log *n*) | *Θ*(*n*) |
| 2–3 heap | *Θ*(1) | *O*(log *n*) am. | *Θ*(1) | *Θ*(1) am. | *O*(log *n*) | *Θ*(*n*) |
| Bottom-up skew | *Θ*(1) | *O*(log *n*) am. | *O*(log *n*) am. | *Θ*(1) am. | *Θ*(1) am. | *Θ*(*n*) am. |
| Pairing | *Θ*(1) | *O*(log *n*) am. | *o*(log *n*) am. | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Rank-pairing | *Θ*(1) | *O*(log *n*) am. | *Θ*(1) am. | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Fibonacci | *Θ*(1) | *O*(log *n*) am. | *Θ*(1) am. | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Strict Fibonacci | *Θ*(1) | *Θ*(log *n*) | *Θ*(1) | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Brodal | *Θ*(1) | *Θ*(log *n*) | *Θ*(1) | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |

1. *make-heap* is the operation of building a heap from a sequence of *n* unsorted elements. It can be done in *Θ*(*n*) time whenever *meld* runs in *O*(log *n*) time (where both complexities can be amortized). Another algorithm achieves *Θ*(*n*) for binary heaps.
2. For persistent heaps (not supporting *decrease-key*), a generic transformation reduces the cost of *meld* to that of *insert*, while the new cost of *delete-min* is the sum of the old costs of *delete-min* and *meld*. Here, it makes *meld* run in *Θ*(1) time (amortized, if the cost of *insert* is) while *delete-min* still runs in *O*(log *n*). Applied to skew binomial heaps, it yields Brodal-Okasaki queues, persistent heaps with optimal worst-case complexities.
3. Lower bound of $\Omega (\log \log n),$ upper bound of $O(2^{2{\sqrt {\log \log n}}}).$
4. Brodal queues and strict Fibonacci heaps achieve optimal worst-case complexities for heaps. They were first described as imperative data structures. The Brodal-Okasaki queue is a persistent data structure achieving the same optimum, except that *decrease-key* is not supported.
