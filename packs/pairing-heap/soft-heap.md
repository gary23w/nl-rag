---
title: "Soft heap"
source: https://en.wikipedia.org/wiki/Soft_heap
domain: pairing-heap
license: CC-BY-SA-4.0
tags: pairing heap, self-adjusting heap, priority queue, mergeable heap
fetched: 2026-07-02
---

# Soft heap

In computer science, a **soft heap** is a variant on the simple heap data structure that has constant amortized time complexity for 5 types of operations. This is achieved by carefully "corrupting" (increasing) the keys of at most a constant number of values in the heap.

## Definition and performance

The constant time operations are:

- **create**(*S*): Create a new soft heap
- **insert**(*S*, *x*): Insert an element into a soft heap
- **meld**(*S*, *S'*): Combine the contents of two soft heaps into one, destroying both
- **delete**(*S*, *x*): Delete an element from a soft heap
- **findmin**(*S*): Get the element with minimum key in the soft heap

Other heaps such as Fibonacci heaps achieve most of these bounds without any corruption, but cannot provide a constant-time bound on the critical *delete* operation. The amount of corruption can be controlled by the choice of a parameter $\varepsilon$ , but the lower this is set, the more time insertions require: expressed using Big-O notation, the amortized time will be $O(\log 1/\varepsilon )$ for an error rate of $\varepsilon$ . Some versions of soft heaps allow the *create*, *insert*, and *meld* operations to take constant time in the worst case, producing amortized rather than worst-case performance only for findmin and delete. As with comparison sort, these algorithms access the keys only by comparisons; if arithmetic operations on integer keys are allowed, the time dependence on $\varepsilon$ can be reduced to $O(\log \log 1/\varepsilon )$ or (with randomization) ${\textstyle O({\sqrt {\log \log 1/\varepsilon }})}$ .

More precisely, the error guarantee offered by the soft heap is the following: each soft heap is initialized with a parameter $\varepsilon$ , chosen between 0 and 1/2. Then at any point in time it will contain at most $\varepsilon \cdot n$ corrupted keys, where n is the number of elements inserted so far. Note that this does not guarantee that only a fixed percentage of the keys *currently* in the heap are corrupted: in an unlucky sequence of insertions and deletions, it can happen that all elements in the heap will have corrupted keys. Similarly, there is no guarantee that in a sequence of elements extracted from the heap with *findmin* and *delete*, only a fixed percentage will have corrupted keys: in an unlucky scenario only corrupted elements are extracted from the heap. When a key is corrupted, the value stored for it in the soft key is higher than its initially-given value; corruption can never decrease the value of any key. The *findmin* operation finds the minimum value among the currently stored keys, including the corrupted ones.

The soft heap was designed by Bernard Chazelle in 2000. The term "corruption" in the structure is the result of what Chazelle called "carpooling" in a soft heap. Each node in the soft heap contains a linked list of keys and one common key. The common key is an upper bound on the values of the keys in the linked list. Once a key is added to the linked list, it is considered corrupted because its value is never again relevant in any of the soft heap operations: only the common keys are compared. This is what makes soft heaps "soft"; one cannot be sure whether any particular value put into it will be corrupted. The purpose of these corruptions is effectively to lower the information entropy of the data, enabling the data structure to break through information-theoretic barriers regarding heaps.

## Applications

Despite their limitations and unpredictable nature, soft heaps are useful in the design of deterministic algorithms. For instance, they have been used to achieve the best complexity to date for finding a minimum spanning tree. Other problems whose efficient solution has been simplified using soft heaps include finding the k th smallest element in several classes of structured sets of values, including heap-ordered trees, sorted matrices, and sumsets.

Another simple example is a selection algorithm, to find the k th smallest of a group of n numbers:

- Initialize a soft heap with error rate $1/3$ , allowing at most 33% of its inserted keys to be corrupted.
- Insert all n elements into the heap.
- Repeat $n/3$ times: perform a findmin operation and delete the key that it returns.
- Let L be the deleted element whose correct key is largest.
- Compare L to all of the given elements, partition them into the subset less than L and the subset greater than L , placing elements that are equal to L into the first subset when they were deleted and into the second subset otherwise.
- Recursively call the same selection algorithm in the subset that contains the k th smallest.

After the comparison step of the algorithm, the first of the two subsets contains all of the deleted keys, so it includes at least $n/3$ elements. Among the $2n/3$ elements that were not deleted, at most $n/3$ are corrupted, so at least $n/3$ are uncorrupted. These uncorrupted and undeleted elements must all belong to the second subset, because they are greater than or equal to the soft heap's (possibly corrupted) value of L , which is in turn greater than the true value of L . Thus, both subsets have between 33% and 66% of the elements. Because each level of recursion reduces the problem size by a constant factor, the total time of the algorithm can be bounded by a geometric series, showing that it is $O(n)$ .
