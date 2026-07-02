---
title: "Interpolation search"
source: https://en.wikipedia.org/wiki/Interpolation_search
domain: interpolation-search-algorithm
license: CC-BY-SA-4.0
tags: interpolation search, binary search, uniform distribution, sorted array
fetched: 2026-07-02
---

# Interpolation search

**Interpolation search** is an algorithm for searching for a key in an array that has been ordered by numerical values assigned to the keys (*key values*). It was first described by W. W. Peterson in 1957. Interpolation search resembles the method by which people search a telephone directory for a name (the key value by which the book's entries are ordered): in each step the algorithm calculates where in the remaining search space the sought item might be, based on the key values at the bounds of the search space and the value of the sought key, usually via a linear interpolation. The key value actually found at this estimated position is then compared to the key value being sought. If it is not equal, then depending on the comparison, the remaining search space is reduced to the part before or after the estimated position. This method will only work if calculations on the size of differences between key values are sensible.

By comparison, binary search always chooses the middle of the remaining search space, discarding one half or the other, depending on the comparison between the key found at the estimated position and the key sought — it does not require numerical values for the keys, just a total order on them. The remaining search space is reduced to the part before or after the estimated position. The linear search uses equality only as it compares elements one-by-one from the start, ignoring any sorting.

On average the interpolation search makes about log(log(*n*)) comparisons (if the elements are uniformly distributed), where *n* is the number of elements to be searched. In the worst case (for instance where the numerical values of the keys increase exponentially) it can make up to O(*n*) comparisons.

In interpolation-sequential search, interpolation is used to find an item near the one being searched for, then linear search is used to find the exact item.

## Performance

Using big-O notation, the performance of the interpolation algorithm on a data set of size *n* is *O*(*n*); however under the assumption of a uniform distribution of the data on the linear scale used for interpolation, the performance can be shown to be *O*(log log *n*).

Dynamic interpolation search extends the *o*(log log *n*) bound to other distributions and also supports *O*(log *n*) insertion and deletion.

Practical performance of interpolation search depends on whether the reduced number of probes is outweighed by the more complicated calculations needed for each probe. It can be useful for locating a record in a large sorted file on disk, where each probe involves a disk seek and is much slower than the interpolation arithmetic.

Index structures like B-trees also reduce the number of disk accesses, and are more often used to index on-disk data in part because they can index many types of data and can be updated online. Still, interpolation search may be useful when one is forced to search certain sorted but unindexed on-disk datasets.

## Adaptation to different datasets

When sort keys for a dataset are uniformly distributed numbers, linear interpolation is straightforward to implement and will find an index very near the sought value.

On the other hand, for a phone book sorted by name, the straightforward approach to interpolation search does not apply. The same high-level principles can still apply, though: one can estimate a name's position in the phone book using the relative frequencies of letters in names and use that as a probe location.

Some interpolation search implementations may not work as expected when a run of equal key values exists. The simplest implementation of interpolation search won't necessarily select the first (or last) element of such a run.

## Book-based searching

The conversion of names in a telephone book to some sort of number clearly will not provide numbers having a uniform distribution (except via immense effort such as sorting the names and calling them name #1, name #2, etc.) and further, it is well known that some names are much more common than others (Smith, Jones,) Similarly with dictionaries, where there are many more words starting with some letters than others. Some publishers go to the effort of preparing marginal annotations or even cutting into the side of the pages to show markers for each letter so that at a glance a segmented interpolation can be performed.

## Sample implementation

The following C++ code example is a simple implementation. At each stage it computes a probe position then as with the binary search, moves either the upper or lower bound in to define a smaller interval containing the sought value. Unlike the binary search which guarantees a halving of the interval's size with each stage, a misled interpolation may reduce/i-case efficiency of O(*n*).

```mw
import <cassert>;

import std;

using std::vector;

/*
arr[low, high) is sorted, search the data "key" in this array,
if "key" is found, return the corresponding index (NOT necessarily the highest possible index);
if "key" is not found, just return low - 1

How to verify that the algorithm is correct?
Proof:
(finiteness: after one loop, the width of [low, high] decreases strictly )

Fist, high <--- high - 1
scenario 1. when low = high
scenario 2. when low < high, arr[low] = arr[high]
scenario 3. when low < high, arr[low] < arr[high], key < arr[low] or key > arr[high]
scenario 4. when low < high, arr[low] < arr[high], arr[low] <= key <= arr[high]

Now let's analyze scenario 4:
Once entering the "while" loop,  low <= middle <= high

    let's analyse after one loop(if we don't return), whether "low > high" will occur
    After one loop:
        case a1: "low" branch has been executed in this loop
            arr[middle] < key <= arr[high]
            so we have middle < high
            so after this loop, we have
            low <= high
        case a2: "high" branch has been executed in this loop
            arr[low] <= key < arr[middle]
            so we have low < middle
            so after this loop, we have
            low <= high

    so after one loop(if we don't return), we have "low <= high"

    when we exit the "while" loop:
        case b1: arr[low] >= arr[high]
            In the last loop, if "low" branch is executed, we know
                arr[low - 1] < k <= arr[high]
                arr[low] >= arr[high]
                low <= high
                so we have 
                arr[low - 1] < k <= arr[low] = arr[high]
            In the last loop, if "high" branch is executed, we know
                arr[low] <= key < arr[high + 1]
                arr[low] >= arr[high]
                low <= high
                so we have
                arr[low] = arr[high] <= key < arr[high + 1]

        case b2: (arr[low] < arr[high]) && (arr[low] > key):
            In the last loop, "low" must have been changed
            so we have
            arr[low - 1] < key
            so we have 
            arr[low - 1] < key < arr[low]

        case b3: (arr[low] < arr[high]) && (key > arr[high])
            In the last loop, "high" must have been changed
            so we have
            key < arr[high + 1]
            so we have
            arr[low] < arr[high] < key < arr[high + 1]

*/

// version 1
template <typename T>
static Rank interpolationSearch(vector<T>& arr, const T& key, Rank low, Rank high) {
    high -= 1;
    int middle;
    int initialLow = low;

    while ((arr[low] < arr[high]) && (arr[low] <= key) && (key <= arr[high])) {
        middle = low + ((key - arr[low]) * (high - low)) / (arr[high] - arr[low]);

        assert((low <= middle) && (middle <= high));

        if (arr[middle] < key) {
            low = middle + 1;
        } else if (key < arr[middle]) {
            high = middle - 1;
        } else {
            return middle;
        }
    }

    if (key == arr[low]) {
        return low;
    } else {
        return initialLow - 1;
    }
}

/*
search "key" in the sorted array arr[low, high),
return: the highest index i such that arr[i] <= key

How to verify that the algorithm is correct?
Proof:
finiteness: after one loop, the width of [low, high] decreases strictly 

Fist, high <---- high - 1
scenario 1. when low = high
scenario 2. when low < high, key < arr[low] or arr[high] <= key
scenario 3. when low < high, arr[low] <= key < arr[high]

Now let's analyze scenario 3:
Once entering the "while" loop,  low <= middle < high

when we exit the "while" loop:
    case a1: key < arr[low]
        so "low" is changed in the last loop, we know
        arr[low - 1] <= key < arr[low]
    case a2: arr[high] <= key
        so "high" is changed in the last loop, we know
        key < arr[high], impossible

conclusion: we should return "low - 1"

*/

// version 2
template <typename T> 
static Rank interpolationSearch(vector<T>& arr, const T& key, Rank low, Rank high) {
    high -= 1;
    assert(low <= high);
    Rank middle;

    if(key < arr[low]) {
        return low - 1;
    } 
    if(arr[high] <= key) {
        return high;
    }

    // now low < high ,  arr[low] <= key < arr[high]
    while ((arr[low] <= key) && (key < arr[high])) {
        middle = low + ((high - low) * (key - arr[low])) / (arr[high] - arr[low]);

        assert((low <= middle) && (middle < high));

        if(key < arr[middle]) {
            high = middle;
        } else {
            low = middle + 1;
        } 
    }

    return low - 1;
}
```

Notice that having probed the list at index *mid*, for reasons of loop control administration, this code sets either *high* or *low* to be not *mid* but an adjacent index, which location is then probed during the next iteration. Since an adjacent entry's value will not be much different, the interpolation calculation is not much improved by this one step adjustment, at the cost of an additional reference to distant memory such as disk.

Each iteration of the above code requires between five and six comparisons (the extra is due to the repetitions needed to distinguish the three states of < > and = via binary comparisons in the absence of a three-way comparison) plus some messy arithmetic, while the binary search algorithm can be written with one comparison per iteration and uses only trivial integer arithmetic. It would thereby search an array of a million elements with no more than twenty comparisons (involving accesses to slow memory where the array elements are stored); to beat that, the interpolation search, as written above, would be allowed no more than three iterations.
