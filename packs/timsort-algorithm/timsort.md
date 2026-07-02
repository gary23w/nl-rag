---
title: "Timsort"
source: https://en.wikipedia.org/wiki/Timsort
domain: timsort-algorithm
license: CC-BY-SA-4.0
tags: timsort algorithm, adaptive sort, merge sort, stable sort
fetched: 2026-07-02
---

# Timsort

**Timsort** is a hybrid, stable sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data. It was implemented by Tim Peters in 2002 for use in the Python programming language. The algorithm finds subsequences of the data that are already ordered (runs) and uses them to sort the remainder more efficiently. This is done by merging runs until certain criteria are fulfilled. Timsort was Python's standard sorting algorithm from version 2.3 until it was replaced in 3.11 by Powersort, a derived algorithm with a more robust merge policy. Timsort is also used to sort arrays of non-primitive type in Java SE 7, on the Android platform, in GNU Octave, on V8, and in Swift. Rust used a custom version of Timsort until May 2024.

The galloping technique derives from Carlsson, Levcopoulos, and O. Petersson's 1990 paper "Sublinear merging and natural merge sort" and Peter McIlroy's 1993 paper "Optimistic Sorting and Information Theoretic Complexity".

## Operation

Timsort was designed to take advantage of *runs* of consecutive ordered elements that already exist in most real-world data, *natural runs*. It iterates over the data collecting elements into runs and simultaneously putting those runs in a stack. Whenever the runs on the top of the stack match a merge criterion, they are merged. This goes on until all data is traversed; then, all runs are merged two at a time and only one sorted run remains. The advantage of merging ordered runs instead of merging fixed size sub-lists (as done by traditional mergesort) is that it decreases the total number of comparisons needed to sort the entire list.

Each run has a minimum size, which is based on the size of the input and is defined at the start of the algorithm. If a run is smaller than this minimum run size, insertion sort is used to add more elements to the run until the minimum run size is reached.

### Merge criteria

Timsort is a stable sorting algorithm (order of elements with same key is kept) and strives to perform balanced merges (a merge thus merges runs of similar sizes).

In order to achieve sorting stability, only consecutive runs are merged. Between two non-consecutive runs, there can be an element with the same key inside the runs. Merging those two runs would change the order of equal keys. Example of this situation ([] are ordered runs): [1 2 2] 1 4 2 [0 1 2]

In pursuit of balanced merges, Timsort considers three runs on the top of the stack, *X*, *Y*, *Z*, and maintains the invariants:

1. |*Z*| > |*Y*| + |*X*|
2. |*Y*| > |*X*|

If any of these invariants is violated, *Y* is merged with the smaller of *X* or *Z* and the invariants are checked again. Once the invariants hold, the search for a new run in the data can start. These invariants maintain merges as being approximately balanced while maintaining a compromise between delaying merging for balance, exploiting fresh occurrence of runs in cache memory and making merge decisions relatively simple.

### Merge space overhead

The original merge sort implementation is not in-place and it has a space overhead of N (data size). In-place merge sort implementations exist, but have a high time overhead. In order to achieve a middle term, Timsort performs a merge sort with a small time overhead and smaller space overhead than N.

First, Timsort performs a binary search to find the location where the first element of the second run would be inserted in the first ordered run, keeping it ordered. Then, it performs the same algorithm to find the location where the last element of the first run would be inserted in the second ordered run, keeping it ordered. Elements before and after these locations are already in their correct place and do not need to be merged. Then, the smaller of these shrunk runs is copied into temporary memory, and the copied elements are merged with the larger shrunk run into the now free space. If the leftmost shrunk run is smaller, the merge proceeds from left to right. If the rightmost shrunk run is smaller, merging proceeds from right to left (i.e. beginning with elements at the ends of the temporary space and leftmost run, and filling the free space from its end). This optimization reduces the number of required element movements, the running time and the temporary space overhead in the general case.

Example: two runs [1, 2, 3, 6, 10] and [4, 5, 7, 9, 12, 14, 17] must be merged. Note that both runs are already sorted individually. The smallest element of the second run is 4 and it would have to be added at the fourth position of the first run in order to preserve its order (assuming that the first position of a run is 1). The largest element of the first run is 10 and it would have to be added at the fifth position of the second run in order to preserve its order. Therefore, [1, 2, 3] and [12, 14, 17] are already in their final positions and the runs in which elements movements are required are [6, 10] and [4, 5, 7, 9]. With this knowledge, we only need to allocate a temporary buffer of size 2 instead of 4.

### Merge direction

Merging can be done in both directions: left-to-right, as in the traditional mergesort, or right-to-left.

### Galloping mode during merge

An individual merge of runs R1 and R2 keeps the count of consecutive elements selected from a run. When this number reaches the *minimum galloping threshold* (*min_gallop*), Timsort considers that it is likely that many consecutive elements may still be selected from that run and switches into galloping mode. Let us assume that R1 is responsible for triggering it. In this mode, the algorithm performs a two-stage search for the place in the run R1 where the next element *x* of the run R2 would be inserted. In the first stage it performs an exponential search, also known as a galloping search, until finding a *k* such that R1[2*k−1* − 1] < x <= R1[2*k* − 1], i.e. a region of uncertainty comprising 2*k−1* − 1 consecutive elements of R1. The second stage performs a straight binary search of this region to find the exact location in R1 for *x*. Galloping mode is an attempt to adapt the merge algorithm to the pattern of intervals between elements in runs.

Galloping is not always efficient. In some cases galloping mode requires more comparisons than a simple linear search. According to benchmarks done by the developer, galloping is beneficial only when the initial element of one run is not one of the first seven elements of the other run. This implies an initial threshold of 7. To avoid the drawbacks of galloping mode, two actions are taken: (1) When galloping is found to be less efficient than binary search, galloping mode is exited. (2) The success or failure of galloping is used to adjust *min_gallop*. If the selected element is from the same array that returned an element previously, *min_gallop* is reduced by one, thus encouraging the return to galloping mode. Otherwise, the value is incremented by one, thus discouraging a return to galloping mode. In the case of random data, the value of *min_gallop* becomes so large that galloping mode never recurs.

### Descending runs

In order to also take advantage of data sorted in descending order, Timsort reverses strictly descending runs when it finds them and adds them to the stack of runs. Since descending runs are later blindly reversed, excluding runs with equal elements maintains the algorithm's stability; i.e., equal elements won't be reversed.

### Minimum run size

Because merging is most efficient when the number of runs is equal to, or slightly less than, a power of two, and notably less efficient when the number of runs is slightly more than a power of two, Timsort chooses *minrun* to try to ensure the former condition.

*Minrun* is chosen from the range 32 to 64 inclusive, such that the size of the data, divided by *minrun*, is equal to, or slightly less than, a power of two. The final algorithm takes the six most significant bits of the size of the array, adds one if any of the remaining bits are set, and uses that result as the *minrun*. This algorithm works for all arrays, including those smaller than 64; for arrays of size 63 or less, this sets *minrun* equal to the array size and Timsort reduces to an insertion sort.

## Algorithm

As described above, Timsort consists of several pieces, too long to describe here in pseudocode. Interested readers are strongly advised to read one of the following versions (with the stack size fix of 2015):

- Implementation in Java, from OpenJDK version 11. 940 lines of code, 403 of which are neither blank nor purely comments.
- Implementation in C, from CPython version 3.4.10. Code for Timsort starts at line 965 and ends at line 2084, for a total of 1120 lines, 732 of which are neither blank nor purely comments.
- Implementation in Python, from PyPy commit "7fce1e5", the last update before the "Powersort" policy was incorporated. 636 lines of code, 486 of which are neither blank nor purely comments.

## Analysis

In the worst case, Timsort takes $O(n\log n)$ comparisons to sort an array of n elements. In the best case, which occurs when the input is already sorted, it runs in linear time, meaning that it is an adaptive sorting algorithm.

For an input that has r runs of sorted elements, the running time is $O(n\log r)$ . More strongly, the time is $O(n+n\mathrm {H} )$ , where the run-length entropy $\mathrm {H}$ of an input in which the i th run has size $n_{i}$ is defined to be $\mathrm {H} =-\sum _{i=1}^{r}{\frac {n_{i}}{n}}\log _{2}{\frac {n_{i}}{n}}.$ When all run sizes are equal, the run-length entropy $\log _{2}r$ , its maximum value for any given number r of runs, but it can be smaller when the runs have unevenly distributed sizes. The formula for the running time is given as $n+n\mathrm {H}$ rather than more simply $n\mathrm {H}$ , to account for the possibility that the entropy can be less than one.

The above behavior regarding the run-length entropy $\mathrm {H}$ is purely derived by Timsort's merge criteria, as that is the part responsible for detecting already-sorted parts. The "galloping" routine exploits a new property that can be described as the dual-run entropy $\mathrm {H} ^{*}$ : $\mathrm {H} ^{*}=-\sum _{i=1}^{s}{\frac {n_{i}}{n}}\log _{2}{\frac {n_{i}}{n}}.$ where s the number of times "galloping" is interrupted by and $s\leq r$ . It can be proven that TimSort takes up to $O(n+n\mathrm {H} )$ element moves and $O(n+n\mathrm {H} ^{*})$ value comparisons.

## Adoption and influence

### Influence

Timsort has inspired many similar algorithms, both in when they decide to merge (the nature of merge trees) and how they perform a merge (especially the galloping heuristic). Among them:

- Peeksort, Powersort, adaptive ShiversSort, and α-Mergesort have the same property with regard to $\mathrm {H} ^{*}$ .
- NaturalMergeSort, ShiversSort and α-StackSort do not have the property with regard to $\mathrm {H} ^{*}$ because they can only merge the top two elements of their stack.
- NaturalMergeSort, ShiversSort and PowerSort take up to $n\log _{2}n+O(n)$ comparisons.

Further influences include:

- PersiSort, an algorithm that extends on the merge criterion with persistent homology.

## Formal verification

In 2015, Dutch and German researchers in the EU FP7 ENVISAGE project found a bug in the standard implementation of Timsort. It was fixed in 2015 in Python, Java, and Android.

Specifically, the invariants on stacked run sizes ensure a tight upper bound on the maximum size of the required stack. The implementation preallocated a stack sufficient to sort 264 bytes of input, and avoided further overflow checks.

However, the guarantee requires the invariants to apply to *every* group of three consecutive runs, but the implementation only checked it for the top three. Using the KeY tool for formal verification of Java software, the researchers found that this check is not sufficient, and they were able to find run lengths (and inputs which generated those run lengths) which would result in the invariants being violated deeper in the stack after the top of the stack was merged.

As a consequence, for certain inputs the allocated size is not sufficient to hold all unmerged runs. In Java, this generates for those inputs an array-out-of-bound exception. The smallest input that triggers this exception in Java and Android v7 is of size 67108864 (226). (Older Android versions already triggered this exception for certain inputs of size 65536 (216))

The Java implementation was corrected by increasing the size of the preallocated stack based on an updated worst-case analysis. The article also showed by formal methods how to establish the intended invariant by checking that the *four* topmost runs in the stack satisfy the two rules above. This approach was initially adopted by Python until it switched to Powersort in 2022 with the release of Python 3.11.
