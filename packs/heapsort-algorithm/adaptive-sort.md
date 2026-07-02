---
title: "Adaptive sort"
source: https://en.wikipedia.org/wiki/Adaptive_sort
domain: heapsort-algorithm
license: CC-BY-SA-4.0
tags: heapsort algorithm, binary heap, priority queue, in place sorting
fetched: 2026-07-02
---

# Adaptive sort

A sorting algorithm falls into the **adaptive sort** family if it takes advantage of existing order in its input. It benefits from the presortedness in the input sequence – or a limited amount of disorder for various definitions of measures of disorder – and sorts faster. Adaptive sorting is usually performed by modifying existing sorting algorithms.

## Motivation

Comparison-based sorting algorithms have traditionally dealt with achieving an optimal bound of *O*(*n* log *n*) when dealing with time complexity. Adaptive sort takes advantage of the existing order of the input to try to achieve better times, so that the time taken by the algorithm to sort is a smoothly growing function of the size of the sequence *and* the disorder in the sequence. In other words, the more presorted the input is, the faster it should be sorted.

This is an attractive feature for a sorting algorithm because sequences that nearly sorted are common in practice. Thus, the performance of existing sorting algorithms can be improved by taking into account the existing order in the input.

Most worst-case sorting algorithms that do optimally well in the worst-case, notably heap sort and merge sort, do not take existing order within their input into account, although this deficiency is easily rectified in the case of merge sort by checking if the last element of the left-hand group is less than (or equal) to the first element of the righthand group, in which case a merge operation may be replaced by simple concatenation – a modification that is well within the scope of making an algorithm adaptive.

## Examples

A classic example of an adaptive sorting algorithm is insertion sort. In this sorting algorithm, the input is scanned from left to right, repeatedly finding the position of the current item, and inserting it into an array of previously sorted items.

Pseudo-code for the insertion sort algorithm follows (array X is zero-based):

```
procedure Insertion Sort (X):
    for j = 1 to length(X) - 1 do
        t ← X[j]
        i ← j
        while i > 0 and X[i - 1] > t do
            X[i] ← X[i - 1]
            i ← i - 1
        end
        X[i] ← t
    end
```

The performance of this algorithm can be described in terms of the number of inversions in the input, and then ⁠ $T(n)$ ⁠ will be roughly equal to ⁠ $I(A)+(n-1)$ ⁠, where ⁠ $I(A)$ ⁠ is the number of inversions. Using this measure of presortedness – being relative to the number of inversions – insertion sort takes less time to sort the closer the array of data is to being sorted.

Other examples of adaptive sorting algorithms are adaptive heap sort, adaptive merge sort, patience sort, Shellsort, smoothsort, splaysort, Timsort, and Cartesian tree sorting.
