---
title: "Cycle sort"
source: https://en.wikipedia.org/wiki/Cycle_sort
domain: elementary-sorts
license: CC-BY-SA-4.0
tags: insertion sort, selection sort, bubble sort, cocktail shaker sort
fetched: 2026-07-02
---

# Cycle sort

**Cycle sort** is an in-place, unstable sorting algorithm, a comparison sort that is theoretically optimal in terms of the total number of writes to the original array, unlike any other in-place sorting algorithm. It is based on the idea that the permutation to be sorted can be factored into cycles, which can individually be rotated to give a sorted result.

Unlike nearly every other sort, items are *never* written elsewhere in the array simply to push them out of the way of the action. Each value is either written zero times, if it is already in its correct position, or written one time to its correct position. This matches the minimal number of overwrites required for a completed in-place sort.

Minimizing the number of writes is useful when making writes to some huge data set is very expensive, such as with EEPROMs like Flash memory where each write reduces the lifespan of the memory.

## Algorithm

To illustrate the idea of cycle sort, consider a list with distinct elements. Given an element x , we can find the index at which it will occur in the *sorted list* by simply counting the number of elements in the entire list that are smaller than x . Now

1. If the element is already at the correct position, do nothing.
2. If it is not, we will write it to its intended position. That position is inhabited by a different element y , which we then have to move to *its* correct position. This process of displacing elements to their correct positions continues until an element is moved to the original position of x . This completes a cycle.

Repeating this process for every element sorts the list, with a single writing operation if and only if an element is not already at its correct position. While computing the correct positions takes $O(n)$ time for every single element, thus resulting in a quadratic time algorithm, the number of writing operations is minimized.

### Implementation

To create a working implementation from the above outline, two issues need to be addressed:

1. When computing the correct positions, we have to make sure not to double-count the first element of the cycle.
2. If there are duplicate elements present, when we try to move an element x to its correct position, that position might already be inhabited by an x . Simply swapping these would cause the algorithm to cycle indefinitely. Instead, we have to insert the element *after any of its duplicates*.

The following Python implementation performs cycle sort on an array, counting the number of writes to that array that were needed to sort it.

Python

```mw
def cycle_sort(array) -> int:
    """Sort an array in place and return the number of writes."""
    writes = 0

    # Loop through the array to find cycles to rotate.
    # Note that the last item will already be sorted after the first n-1 cycles.
    for cycle_start in range(0, len(array) - 1):
        item = array[cycle_start]

        # Find where to put the item.
        pos = cycle_start
        for i in range(cycle_start + 1, len(array)):
            if array[i] < item:
                pos += 1

        # If the item is already there, this is not a cycle.
        if pos == cycle_start:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while item == array[pos]:
            pos += 1

        array[pos], item = item, array[pos]
        writes += 1

        # Rotate the rest of the cycle.
        while pos != cycle_start:
            # Find where to put the item.
            pos = cycle_start
            for i in range(cycle_start + 1, len(array)):
                if array[i] < item:
                    pos += 1

            # Put the item there or right after any duplicates.
            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
            writes += 1

    return writes
```

The next implementation written in C++ simply performs cyclic array sorting.

```mw
template <typename type_array>
void cycle_sort(type_array *Array, int array_size)
{
	for (int cycle_start = 0; cycle_start < array_size - 1; cycle_start++)
	{
		type_array item = Array[cycle_start];

		int pos = cycle_start;
		for (int i = cycle_start + 1; i < array_size; i++)
			if (Array[i] < item)
				pos += 1;
		if (pos == cycle_start)
			continue;
		while (item == Array[pos])
			pos += 1;

		std::swap(Array[pos], item);

		while (pos != cycle_start)
		{
			pos = cycle_start;
			for (int i = cycle_start + 1; i < array_size; i++)
				if (Array[i] < item)
					pos += 1;
			while (item == Array[pos])
				pos += 1;

			std::swap(Array[pos], item);
		}
	}
}
```

## Situation-specific optimizations

When the array contains only duplicates of a relatively small number of items, a constant-time perfect hash function can greatly speed up finding where to put an item1, turning the sort from Θ(*n*2) time to Θ(*n* + *k*) time, where *k* is the total number of hashes. The array ends up sorted in the order of the hashes, so choosing a hash function that gives you the right ordering is important.

Before the sort, create a histogram, sorted by hash, counting the number of occurrences of each hash in the array. Then create a table with the cumulative sum of each entry in the histogram. The cumulative sum table will then contain the position in the array of each element. The proper place of elements can then be found by a constant-time hashing and cumulative sum table lookup rather than a linear search.
