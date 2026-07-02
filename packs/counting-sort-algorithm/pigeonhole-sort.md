---
title: "Pigeonhole sort"
source: https://en.wikipedia.org/wiki/Pigeonhole_sort
domain: counting-sort-algorithm
license: CC-BY-SA-4.0
tags: counting sort, integer sorting, stable sort, pigeonhole principle
fetched: 2026-07-02
---

# Pigeonhole sort

**Pigeonhole sorting** is a sorting algorithm that is suitable for sorting lists of elements where the number *n* of elements and the length *N* of the range of possible key values are approximately the same. It requires O(*n* + *N*) time. It is similar to counting sort, but differs in that it "moves items twice: once to the bucket array and again to the final destination [whereas] counting sort builds an auxiliary array then uses the array to compute each item's final destination and move the item there."

The pigeonhole algorithm works as follows:

1. Given an array of values to be sorted, set up an auxiliary array of initially empty "pigeonholes" (analogous to a pigeon-hole messagebox in an office or desk), one pigeonhole for each key in the range of the keys in the original array.
2. Going over the original array, put each value into the pigeonhole corresponding to its key, such that each pigeonhole eventually contains a list of all values with that key.
3. Iterate over the pigeonhole array in increasing order of keys, and for each pigeonhole, put its elements into the original array in increasing order.

## Implementation

Below is an implementation of Pigeonhole sort in pseudocode. This function sorts the array in-place and modifies the supplied array.

```
function pigeonhole(array arr) is 
    min ← min(arr)
    max ← max(arr) 
    index ← 0
    range ← max - min + 1
    array tmp ← new array of length range

    for i = 0 to range STEP 1
        tmp[i] = 0

    for i = 0 to length(arr) STEP 1
        tmp[arr[i] - min] = tmp[arr[i] - min] + 1 

    for i = 0 to range STEP 1
        while tmp[i] > 0 do
            tmp[i] = tmp[i] - 1
            arr[index] = i + min
            index = index + 1
```

## Example

Suppose one were sorting these value pairs by their first element:

- (5, "hello")
- (3, "pie")
- (8, "apple")
- (5, "king")

For each value between 3 and 8 we set up a pigeonhole, then move each element to its pigeonhole:

- 3: (3, "pie")
- 4:
- 5: (5, "hello"), (5, "king")
- 6:
- 7:
- 8: (8, "apple")

The pigeonhole array is then iterated over in order, and the elements are moved back to the original list.

The difference between pigeonhole sort and counting sort is that in counting sort, the auxiliary array does not contain lists of input elements, only counts:

- 3: 1
- 4: 0
- 5: 2
- 6: 0
- 7: 0
- 8: 1

For arrays where *N* is much larger than *n*, bucket sort is a generalization that is more efficient in space and time.
