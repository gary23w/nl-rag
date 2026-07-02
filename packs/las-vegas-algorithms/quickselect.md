---
title: "Quickselect"
source: https://en.wikipedia.org/wiki/Quickselect
domain: las-vegas-algorithms
license: CC-BY-SA-4.0
tags: las vegas algorithm, expected running time, randomized quicksort, monte carlo algorithm
fetched: 2026-07-02
---

# Quickselect

In computer science, **quickselect** is a selection algorithm to find the *k*th smallest element in an unordered list, also known as the *k*th order statistic. Like the related quicksort sorting algorithm, it was developed by Tony Hoare, and thus is also known as **Hoare's selection algorithm**. Like quicksort, it is efficient in practice and has good average-case performance, but has poor worst-case performance. Quickselect and its variants are the selection algorithms most often used in efficient real-world implementations.

Quickselect uses the same overall approach as quicksort, choosing one element as a pivot and partitioning the data in two based on the pivot, accordingly as less than or greater than the pivot. However, instead of recursing into both sides, as in quicksort, quickselect only recurses into one side – the side with the element it is searching for. This reduces the average complexity from $O(n\log n)$ to $O(n)$ , with a worst case of $O(n^{2})$ .

As with quicksort, quickselect is generally implemented as an in-place algorithm, and beyond selecting the kth element, it also partially sorts the data. See selection algorithm for further discussion of the connection with sorting.

## Algorithm

In quicksort, there is a subprocedure called `partition` that can, in linear time, group a list (ranging from indices `left` to `right`) into two parts: those less than a certain element, and those greater than or equal to the element. Here is pseudocode that performs a partition about the element `list[pivotIndex]`:

```
function partition(list, left, right, pivotIndex) is
    pivotValue := list[pivotIndex]
    swap list[pivotIndex] and list[right]  // Move pivot to end
    storeIndex := left
    for i from left to right − 1 do
        if list[i] <= pivotValue then
            swap list[storeIndex] and list[i]
            increment storeIndex
    swap list[right] and list[storeIndex]  // Move pivot to its final place
    return storeIndex
```

This is known as the Lomuto partition scheme, which is simpler but less efficient than Hoare's original partition scheme.

In quicksort, we recursively sort both branches, leading to best-case $O(n\log n)$ time. However, when doing selection, we already know which partition our desired element lies in, since the pivot is in its final sorted position, with all those preceding it in an unsorted order and all those following it in an unsorted order. Therefore, a single recursive call locates the desired element in the correct partition, and we build upon this for quickselect:

```
// Returns the k-th smallest element of list within left..right inclusive
// (i.e. left <= k <= right).
function select(list, left, right, k) is
    if left = right then   // If the list contains only one element,
        return list[left]  // return that element
    pivotIndex  := ...     // select a pivotIndex between left and right,
                           // e.g., left + floor(rand() % (right − left + 1))
    pivotIndex  := partition(list, left, right, pivotIndex)
    // The pivot is in its final sorted position
    if k = pivotIndex then
        return list[k]
    else if k < pivotIndex then
        return select(list, left, pivotIndex − 1, k)
    else
        return select(list, pivotIndex + 1, right, k) 
```

Just as the minimum-based selection algorithm is a partial selection sort, this is a partial quicksort, generating and partitioning only $O(\log n)$ of its $O(n)$ partitions. This simple procedure has expected linear performance, and, like quicksort, has quite good performance in practice. It is also an in-place algorithm, requiring only constant memory overhead if tail call optimization is available, or if eliminating the tail recursion with a loop:

```
function select(list, left, right, k) is
    loop
        if left = right then
            return list[left]
        pivotIndex := ...     // select pivotIndex between left and right
        pivotIndex := partition(list, left, right, pivotIndex)
        if k = pivotIndex then
            return list[k]
        else if k < pivotIndex then
            right := pivotIndex − 1
        else
            left := pivotIndex + 1
```

This `select` function works only with the Lomuto partition scheme. This is because `select` assumes that the return value from partition is the position of the pivot. This is true for the Lomuto partition scheme, but not for the Hoare's partition scheme. In Hoare's scheme, the return value is the last index of the "left" partition, and the pivot is not guaranteed to be "in between" the partitions.

The recursion, as presented, also only works with Lomuto's scheme, as it assumes that the right partition starts with `pivotIndex +1`, while when using Hoare's scheme, the right partition starts at `pivotIndex`.

## Time complexity

Like quicksort, quickselect has good average performance, but is sensitive to the pivot that is chosen. If good pivots are chosen, meaning ones that consistently decrease the search set by a given fraction, then the search set decreases in size exponentially and by induction (or summing the geometric series) one sees that performance is linear, as each step is linear and the overall time is a constant times this (depending on how quickly the search set reduces). However, if bad pivots are consistently chosen, such as decreasing by only a single element each time, then worst-case performance is quadratic: $O(n^{2}).$ This occurs, for example, in searching for the maximum element of a set, using the first element as the pivot, and having sorted data. However, for randomly chosen pivots, this worst case is very unlikely: the probability of using more than $Cn$ comparisons, for any sufficiently large constant C , is superexponentially small as a function of C .

## Variants

The easiest solution is to choose a random pivot, which yields almost certain linear time. Deterministically, one can use the median-of-3 pivot strategy (as in Quicksort), which yields linear performance on partially sorted data, as is common in the real world. However, contrived sequences can still cause worst-case complexity; David Musser describes a "median-of-3 killer" sequence that allows an attack against that strategy, which was one motivation for his introselect algorithm.

One can assure linear performance even in the worst case by using a more sophisticated pivot strategy; this is done in the median of medians algorithm. However, the overhead of computing the pivot is high, and thus, this is generally not used in practice. One can combine basic quickselect with median of medians as a fallback to get both fast average case performance and linear worst-case performance; this is done in introselect.

Finer computations of the average time complexity yield a worst case of $n(2+2\log 2+o(1))\leq 3.4n+o(n)$ for random pivots (in the case of the median; other *k* are faster). The constant can be improved to 3/2 by a more complicated pivot strategy, yielding the Floyd–Rivest algorithm, which has average complexity of $1.5n+O(n^{1/2})$ for median, with other *k* being faster.
