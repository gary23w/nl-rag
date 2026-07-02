---
title: "Quicksort (part 2/2)"
source: https://en.wikipedia.org/wiki/Quicksort
domain: quicksort-algorithm
license: CC-BY-SA-4.0
tags: quicksort algorithm, divide and conquer, partition scheme, quickselect algorithm
fetched: 2026-07-02
part: 2/2
---

## Relation to other algorithms

Quicksort is a space-optimized version of the binary tree sort. Instead of inserting items sequentially into an explicit tree, quicksort organizes them concurrently into a tree that is implied by the recursive calls. The algorithms make exactly the same comparisons, but in a different order. An often desirable property of a sorting algorithm is stability – that is, the order of elements that compare equal is not changed, allowing controlling order of multikey tables (e.g., directory or folder listings) in a natural way. This property is hard to maintain for in-place quicksort (that uses only constant additional space for pointers and buffers, and *O*(log *n*) additional space for the management of explicit or implicit recursion). For variant quicksorts involving extra memory due to representations using pointers (e.g., lists or trees) or files (effectively lists), it is trivial to maintain stability. The more complex, or disk-bound, data structures tend to increase time cost, in general, making increasing use of virtual memory or disk.

The most direct competitor of quicksort is heapsort. Heapsort has the advantages of simplicity and a worst-case run time of *O*(*n* log *n*), but heapsort's *average* running time is usually considered slower than in-place quicksort, primarily due to its worse locality of reference. This result is debatable; some publications indicate the opposite. The main disadvantage of quicksort is the implementation complexity required to avoid bad pivot choices and the resultant *O*(*n*2) performance. Introsort is a variant of quicksort that solves this problem by switching to heapsort when a bad case is detected. Major programming languages, such as C++ (in the GNU and LLVM implementations), use introsort.

Quicksort also competes with merge sort, another *O*(*n* log *n*) sorting algorithm. Merge sort's main advantages are that it is a stable sort and has excellent worst-case performance. The main disadvantage of merge sort is that it is an out-of-place algorithm, so when operating on arrays, efficient implementations require *O*(*n*) auxiliary space (vs. *O*(log *n*) for quicksort with in-place partitioning and tail recursion, or *O*(1) for heapsort).

Merge sort works very well on linked lists, requiring only a small, constant amount of auxiliary storage. Although quicksort *can* be implemented as a stable sort using linked lists, there is no reason to; it will often suffer from poor pivot choices without random access, and is essentially always inferior to merge sort. Merge sort is also the algorithm of choice for external sorting of very large data sets stored on slow-to-access media such as disk storage or network-attached storage.

Bucket sort with two buckets is very similar to quicksort; the pivot in this case is effectively the value in the middle of the value range, which does well on average for uniformly distributed inputs.

### Selection-based pivoting

A selection algorithm chooses the kth smallest of a list of numbers; this is an easier problem in general than sorting. One simple but effective selection algorithm works nearly in the same manner as quicksort, and is accordingly known as quickselect. The difference is that instead of making recursive calls on both sublists, it only makes a single tail-recursive call on the sublist that contains the desired element. This change lowers the average complexity to linear or *O*(*n*) time, which is optimal for selection, but the selection algorithm is still *O*(*n*2) in the worst case.

A variant of quickselect, the median of medians algorithm, chooses pivots more carefully, ensuring that the pivots are near the middle of the data (between the 30th and 70th percentiles), and thus has guaranteed linear time – *O*(*n*). This same pivot strategy can be used to construct a variant of quicksort (median of medians quicksort) with *O*(*n* log *n*) time. However, the overhead of choosing the pivot is significant, so this is generally not used in practice.

More abstractly, given an *O*(*n*) selection algorithm, one can use it to find the ideal pivot (the median) at every step of quicksort and thus produce a sorting algorithm with *O*(*n* log *n*) running time. Practical implementations of this variant are considerably slower on average, but they are of theoretical interest because they show an optimal selection algorithm can yield an optimal sorting algorithm.

### Variants

#### Multi-pivot quicksort

Instead of partitioning into two subarrays using a single pivot, multi-pivot quicksort (also multiquicksort) partitions its input into some s number of subarrays using *s* − 1 pivots. While the dual-pivot case (*s* = 3) was considered by Sedgewick and others already in the mid-1970s, the resulting algorithms were not faster in practice than the "classical" quicksort. A 1999 assessment of a multiquicksort with a variable number of pivots, tuned to make efficient use of processor caches, found it to increase the instruction count by some 20%, but simulation results suggested that it would be more efficient on very large inputs. A version of dual-pivot quicksort developed by Yaroslavskiy in 2009 turned out to be fast enough to warrant implementation in Java 7, as the standard algorithm to sort arrays of primitives (sorting arrays of objects is done using Timsort). The performance benefit of this algorithm was subsequently found to be mostly related to cache performance, and experimental results indicate that the three-pivot variant may perform even better on modern machines.

#### External quicksort

For disk files, an external sort based on partitioning similar to quicksort is possible. It is slower than external merge sort, but doesn't require extra disk space. 4 buffers are used, 2 for input, 2 for output. Let $N=$ the number of records in the file, $B=$ the number of records per buffer, and $M=N/B=$ the number of buffer segments in the file. Data is read (and written) from both ends of the file inwards. Let X represent the segments that start at the beginning of the file, and Y represent segments that start at the end of the file. Data is read into the X and Y read buffers. A pivot record is chosen and the records in the X and Y buffers other than the pivot record are copied to the X write buffer in ascending order and Y write buffer in descending order based comparison with the pivot record. Once either X or Y buffer is filled, it is written to the file, and the next X or Y buffer is read from the file. The process continues until all segments are read and one write buffer remains. If that buffer is an X write buffer, the pivot record is appended to it and the X buffer is written. If that buffer is a Y write buffer, the pivot record is prepended to the Y buffer and the Y buffer written. This constitutes one partition step of the file, and the file is now composed of two subfiles. The start and end positions of each subfile are pushed/popped to a stand-alone stack or the main stack via recursion. To limit stack space to $O(\log _{2}(n))$ , the smaller subfile is processed first. For a stand-alone stack, push the larger subfile parameters onto the stack, iterate on the smaller subfile. For recursion, recurse on the smaller subfile first, then iterate to handle the larger subfile. Once a sub-file is less than or equal to 4 B records, the subfile is sorted in-place via quicksort and written. That subfile is now sorted and in place in the file. The process is continued until all sub-files are sorted and in place. The average number of passes on the file is approximately ${\frac {1+\ln(N+1)}{(4B)}}$ , but worst case pattern is N passes (equivalent to $O(n^{2})$ for worst case internal sort).

#### Three-way radix quicksort

This algorithm is a combination of radix sort and quicksort. Pick an element from the array (the pivot) and consider the first character (key) of the string (multikey). Partition the remaining elements into three sets: those whose corresponding character is less than, equal to, and greater than the pivot's character. Recursively sort the "less than" and "greater than" partitions on the same character. Recursively sort the "equal to" partition by the next character (key). Given we sort using bytes or words of length W bits, the best case is *O*(*KN*) and the worst case *O*(2*K**N*) or at least *O*(*N*2) as for standard quicksort, given for unique keys *N*<2*K*, and K is a hidden constant in all standard comparison sort algorithms including quicksort. This is a kind of three-way quicksort in which the middle partition represents a (trivially) sorted subarray of elements that are *exactly* equal to the pivot.

#### Quick radix sort

Also developed by Powers as an *O*(*K*) parallel PRAM algorithm. This is again a combination of radix sort and quicksort, but the quicksort left/right partition decision is made on successive bits of the key, and is thus *O*(*KN*) for N K-bit keys. All comparison sort algorithms implicitly assume the transdichotomous model with K in *Θ*(log *N*), as if K is smaller we can sort in *O*(*N*) time using a hash table or integer sorting. If *K* ≫ log *N* but elements are unique within *O*(log *N*) bits, the remaining bits will not be looked at by either quicksort or quick radix sort. Failing that, all comparison sorting algorithms will also have the same overhead of looking through *O*(*K*) relatively useless bits but quick radix sort will avoid the worst case *O*(*N*2) behaviours of standard quicksort and radix quicksort, and will be faster even in the best case of those comparison algorithms under these conditions of uniqueprefix(*K*) ≫ log *N*. See Powers for further discussion of the hidden overheads in comparison, radix, and parallel sorting.

#### BlockQuicksort

In any comparison-based sorting algorithm, minimizing the number of comparisons requires maximizing the amount of information gained from each comparison, meaning that the comparison results are unpredictable. This causes frequent branch mispredictions, limiting performance. BlockQuicksort rearranges the computations of quicksort to convert unpredictable branches to data dependencies. When partitioning, the input is divided into moderate-sized blocks (which fit easily into the data cache), and two arrays are filled with the positions of elements to swap. (To avoid conditional branches, the position is unconditionally stored at the end of the array, and the index of the end is incremented if a swap is needed.) A second pass exchanges the elements at the positions indicated in the arrays. Both loops have only one conditional branch, a test for termination, which is usually taken.

The BlockQuicksort technique is incorporated into LLVM's C++ STL implementation, libcxx, providing a 50% improvement on random integer sequences. Pattern-defeating quicksort (pdqsort), a version of introsort, also incorporates this technique.

#### Partial and incremental quicksort

Several variants of quicksort exist that separate the k smallest or largest elements from the rest of the input.

### Generalization

Richard Cole and David C. Kandathil, in 2004, discovered a one-parameter family of sorting algorithms, called partition sorts, which on average (with all input orderings equally likely) perform at most $n\log n+{O}(n)$ comparisons (close to the information theoretic lower bound) and ${\Theta }(n\log n)$ operations; at worst they perform ${\Theta }(n\log ^{2}n)$ comparisons (and also operations); these are in-place, requiring only additional ${O}(\log n)$ space. Practical efficiency and smaller variance in performance were demonstrated against optimized quicksorts (of Sedgewick and Bentley-McIlroy).
