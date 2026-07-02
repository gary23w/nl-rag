---
title: "Cocktail shaker sort"
source: https://en.wikipedia.org/wiki/Cocktail_shaker_sort
domain: elementary-sorts
license: CC-BY-SA-4.0
tags: insertion sort, selection sort, bubble sort, cocktail shaker sort
fetched: 2026-07-02
---

# Cocktail shaker sort

**Cocktail shaker sort**, also known as **bidirectional bubble sort**, **cocktail sort**, **shaker sort** (which can also refer to a variant of selection sort), **ripple sort**, **shuffle sort**, or **shuttle sort**, is an extension of bubble sort. The algorithm extends bubble sort by operating in two directions. While it improves on bubble sort by more quickly moving items to the beginning of the list, it provides only marginal performance improvements.

Like most variants of bubble sort, cocktail shaker sort is used primarily as an educational tool. More efficient algorithms such as quicksort, merge sort, or timsort are used by the sorting libraries built into popular programming languages such as Python and Java.

## Pseudocode

The simplest form goes through the whole list each time:

```
procedure cocktailShakerSort(A : list of sortable items) is
    do
        swapped := false
        for each i in 0 to length(A) − 2 do:
            if A[i] > A[i + 1] then // test whether the two elements are in the wrong order
                swap(A[i], A[i + 1]) // let the two elements change places
                swapped := true
            end if
        end for
        if not swapped then
            // we can exit the outer loop here if no swaps occurred.
            break do-while loop
        end if
        swapped := false
        for each i in length(A) − 2 to 0 do:
            if A[i] > A[i + 1] then
                swap(A[i], A[i + 1])
                swapped := true
            end if
        end for
    while swapped // if no elements have been swapped, then the list is sorted
end procedure
```

The first rightward pass will shift the largest element to its correct place at the end, and the following leftward pass will shift the smallest element to its correct place at the beginning. The second complete pass will shift the second largest and second smallest elements to their correct places, and so on. After *i* passes, the first *i* and the last *i* elements in the list are in their correct positions, and do not need to be checked. By shortening the part of the list that is sorted each time, the number of operations can be halved (see bubble sort).

This is an example of the algorithm in MATLAB/OCTAVE with the optimization of remembering the last swap index and updating the bounds.

```mw
function A = cocktailShakerSort(A)
% `beginIdx` and `endIdx` marks the first and last index to check
beginIdx = 1;
endIdx = length(A) - 1;
while beginIdx <= endIdx
    newBeginIdx = endIdx;
    newEndIdx = beginIdx;
    for ii = beginIdx:endIdx
        if A(ii) > A(ii + 1)
            [A(ii+1), A(ii)] = deal(A(ii), A(ii+1));
            newEndIdx = ii;
        end
    end

    % decreases `endIdx` because the elements after `newEndIdx` are in correct order
    endIdx = newEndIdx - 1;

    for ii = endIdx:-1:beginIdx
        if A(ii) > A(ii + 1)
            [A(ii+1), A(ii)] = deal(A(ii), A(ii+1));
            newBeginIdx = ii;
        end
    end
    % increases `beginIdx` because the elements before `newBeginIdx` are in correct order
    beginIdx = newBeginIdx + 1;
end
end
```

## Differences from bubble sort

Cocktail shaker sort is a slight variation of bubble sort. It differs in that instead of repeatedly passing through the list from bottom to top, it passes alternately from bottom to top and then from top to bottom. It can achieve slightly better performance than a standard bubble sort. The reason for this is that bubble sort only passes through the list in one direction and therefore can only move items backward one step each iteration.

An example of a list that proves this point is the list (2,3,4,5,1), which would only need to go through one pass of cocktail sort to become sorted, but if using an ascending bubble sort would take four passes. However one cocktail sort pass should be counted as two bubble sort passes. Typically cocktail sort is less than two times faster than bubble sort.

Another optimization can be that the algorithm remembers where the last actual swap has been done. In the next iteration, there will be no swaps beyond this limit and the algorithm has shorter passes. As the cocktail shaker sort goes bidirectionally, the range of possible swaps, which is the range to be tested, will reduce per pass, thus reducing the overall running time slightly.

## Complexity

The complexity of the cocktail shaker sort in big O notation is $O(n^{2})$ for both the worst case and the average case, but it becomes closer to $O(n)$ if the list is mostly ordered before applying the sorting algorithm. For example, if every element is at a position that differs by at most k (k ≥ 1) from the position it is going to end up in, the complexity of cocktail shaker sort becomes $O(kn).$

The cocktail shaker sort is also briefly discussed in the book *The Art of Computer Programming*, along with similar refinements of bubble sort. In conclusion, Knuth states about bubble sort and its improvements:

> But none of these refinements leads to an algorithm better than straight insertion [that is, insertion sort]; and we already know that straight insertion isn't suitable for large *N*. [...] In short, the bubble sort seems to have nothing to recommend it, except a catchy name and the fact that it leads to some interesting theoretical problems.

— D. E. Knuth

## Variations

- Dual Cocktail Shaker sort is a variant of Cocktail Shaker Sort that performs a forward and backward pass per iteration simultaneously, improving performance compared to the original.
