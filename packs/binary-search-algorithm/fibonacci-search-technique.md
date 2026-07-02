---
title: "Fibonacci search technique"
source: https://en.wikipedia.org/wiki/Fibonacci_search_technique
domain: binary-search-algorithm
license: CC-BY-SA-4.0
tags: binary search, sorted array, logarithmic search, search algorithm
fetched: 2026-07-02
---

# Fibonacci search technique

In computer science, the **Fibonacci search technique** is a method of searching a sorted array using a divide and conquer algorithm that narrows down possible locations with the aid of Fibonacci numbers. The technique is conceptually similar to a binary search, which repeatedly splits the search interval into two equal halves. Fibonacci search, however, splits the array into two unequal parts, with sizes that are consecutive Fibonacci numbers.

This method has a key advantage on older computer hardware where arithmetic division or bit-shifting operations were computationally expensive compared to addition and subtraction. Since the Fibonacci sequence is based on addition, this search method could be implemented more efficiently. While on modern CPUs the performance difference is often negligible, the algorithm remains of theoretical and historical interest. On average, Fibonacci search performs about 4% more comparisons than binary search, and it has an average-case complexity and worst-case complexity of $O(\log n)$ (see Big O notation).

Fibonacci search can also have an advantage in searching data stored in certain structures, such as on a magnetic tape, where seek times are heavily dependent on the distance from the current head position. It is derived from Golden section search, an algorithm by Jack Kiefer (1953) to search for the maximum or minimum of a unimodal function in an interval.

## Algorithm

The Fibonacci search technique works by first finding the smallest Fibonacci number that is greater than or equal to the length of the array. Let this Fibonacci number be $F_{m}$ . The algorithm then uses the preceding Fibonacci numbers, $F_{m-1}$ and $F_{m-2}$ , to probe the array at an index, narrowing the search space in each step. The size of the step decreases at each iteration according to the Fibonacci sequence.

Let *k* be defined as an element in *F*, the array of Fibonacci numbers. *n* = *Fm* is the array size. If *n* is not a Fibonacci number, let *Fm* be the smallest number in *F* that is greater than *n*.

The array of Fibonacci numbers is defined where *F**k*+2 = *F**k*+1 + *Fk*, when *k* ≥ 0, *F*1 = 1, and *F0* = 1.

To test whether an item is in the list of ordered numbers, follow these steps:

1. Set *k* = *m*.
2. If *k* = 0, stop. There is no match; the item is not in the array.
3. Compare the item against element in *F**k*−1.
4. If the item matches, stop.
5. If the item is less than entry *F**k*−1, discard the elements from positions *F**k*−1 + 1 to *n*. Set *k* = *k* − 1 and return to step 2.
6. If the item is greater than entry *F**k*−1, discard the elements from positions 1 to *F**k*−1. Renumber the remaining elements from 1 to *F**k*−2, set *k* = *k* − 2, and return to step 2.

Alternative implementation (from "Sorting and Searching" by Knuth):

- Given a table of records *R1*, *R2*, ..., *RN* whose keys are in increasing order *K*1 < *K*2 < ... < *KN*, the algorithm searches for a given argument *K*. Assume *N*+1= *F**k*+1

1. [Initialize] *i* ← *F**k*, *p* ← *F**k*−1, *q* ← *F**k*−2 (throughout the algorithm, *p* and *q* will be consecutive Fibonacci numbers)
2. [Compare] If *K* < *Ki*, go to *Step 3*; if *K* > *Ki* go to *Step 4*; and if *K* = *Ki*, the algorithm terminates successfully.
3. [Decrease *i*] If *q*=0, the algorithm terminates unsuccessfully. Otherwise set (*i*, *p*, *q*) ← (*i* − *q*, *q*, *p* − *q*) (which moves *p* and *q* one position back in the Fibonacci sequence); then return to *Step 2*
4. [Increase *i*] If *p*=1, the algorithm terminates unsuccessfully. Otherwise set (*i*, *p*, *q*) ← (*i* + *q*, *p* − *q*, 2*q* − *p*) (which moves *p* and *q* two positions back in the Fibonacci sequence); and return to *Step 2*

The two variants of the algorithm presented above always divide the current interval into a larger and a smaller subinterval. The original algorithm, however, would divide the new interval into a smaller and a larger subinterval in Step 4. This has the advantage that the new *i* is closer to the old *i* and is more suitable for accelerating searching on magnetic tape.

### Example

Suppose we want to search for the number `x = 85` in the following sorted array of `n = 11` elements:

`[10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]`

1. **Find the Fibonacci numbers:**
  - The smallest Fibonacci number greater than or equal to `n = 11` is $F_{7}=13$ . So, `m = 7`.
  - The two preceding Fibonacci numbers are $F_{5}=5$ and $F_{6}=8$ .
  - We will maintain an offset for the subarray we are searching. Initially, `offset = -1`.
2. **First comparison:**
  - The first comparison index is `i = min(offset + F_6, n-1) = min(-1 + 8, 10) = 7`.
  - We compare `x` with the element at index 7: `array[7]` is 82.
  - Since `x = 85` is greater than `82`, we eliminate the elements from the start of the array up to index 7. The new search space is the subarray from index 8 onwards.
  - We update the Fibonacci numbers by moving two steps down: `m = m - 2 = 6` (so the new Fibonacci numbers for the step size will be $F_{5}=5$ and $F_{4}=3$ ).
  - We update the offset: `offset = i = 7`.
3. **Second comparison:**
  - The next comparison index is `i = min(offset + F_4, n-1) = min(7 + 3, 10) = 10`.
  - We compare `x` with the element at index 10: `array[10]` is 100.
  - Since `x = 85` is less than `100`, we eliminate the elements from index 10 to the end.
  - We update the Fibonacci numbers by moving one step down: `m = m - 1 = 5` (new step sizes will be $F_{4}=3$ and $F_{3}=2$ ).
  - The offset remains `offset = 7`.
4. **Third comparison:**
  - The next comparison index is `i = min(offset + F_3, n-1) = min(7 + 2, 10) = 9`.
  - We compare `x` with the element at index 9: `array[9]` is 90.
  - Since `x = 85` is less than `90`, we eliminate the elements from index 9 to the end.
  - We update the Fibonacci numbers by moving one step down: `m = m - 1 = 4` (new step sizes will be $F_{3}=2$ and $F_{2}=1$ ).
  - The offset remains `offset = 7`.
5. **Fourth comparison:**
  - The next comparison index is `i = min(offset + F_2, n-1) = min(7 + 1, 10) = 8`.
  - We compare `x` with the element at index 8: `array[8]` is 85.
  - The item is found at index 8. The algorithm terminates successfully.
