---
title: "Exponential search"
source: https://en.wikipedia.org/wiki/Exponential_search
domain: binary-search-algorithm
license: CC-BY-SA-4.0
tags: binary search, sorted array, logarithmic search, search algorithm
fetched: 2026-07-02
---

# Exponential search

In computer science, an **exponential search** (also called **doubling search** or **galloping search** or **Struzik search**) is an algorithm, created by Jon Bentley and Andrew Chi-Chih Yao in 1976, for searching sorted, unbounded/infinite lists. There are numerous ways to implement this, with the most common being to determine a range that the search key resides in and performing a binary search within that range. This takes $O(\log i)$ time, where i is the position of the search key in the list, if the search key is in the list, or the position where the search key should be, if the search key is not in the list.

Exponential search can also be used to search in bounded lists. Exponential search can even out-perform more traditional searches for bounded lists, such as binary search, when the element being searched for is near the beginning of the array. This is because exponential search will run in *$O(\log i)$* time, where i is the index of the element being searched for in the list, whereas binary search would run in $O(\log n)$ time, where n is the number of elements in the list.

## Algorithm

Exponential search allows for searching through a sorted, unbounded list for a specified input value (the search "key"). The algorithm consists of two stages. The first stage determines a range in which the search key would reside if it were in the list. In the second stage, a binary search is performed on this range. In the first stage, assuming that the list is sorted in ascending order, the algorithm looks for the first exponent, *j*, where the value 2j is greater than the search key. This value, 2j becomes the upper bound for the binary search with the previous power of 2, 2j - 1, being the lower bound for the binary search.

```mw
// Returns the position of key in the array arr of length size.
template <typename T>
int exponential_search(T arr[], int size, T key)
{
    if (size == 0) {
        return NOT_FOUND;
    }

    int bound = 1;
    while (bound < size && arr[bound] < key) {
        bound *= 2;
    }

    return binary_search(arr, key, bound/2, min(bound, size));
}
```

In each step, the algorithm compares the search key value with the key value at the current search index. If the element at the current index is smaller than the search key, the algorithm repeats, skipping to the next search index by doubling it, calculating the next power of 2. If the element at the current index is larger than the search key, the algorithm now knows that the search key, if it is contained in the list at all, is located in the interval formed by the previous search index, 2j - 1, and the current search index, 2j. The binary search is then performed with the result of either a failure, if the search key is not in the list, or the position of the search key in the list.

## Performance

The first stage of the algorithm takes $O(\log i)$ time, where i is the index where the search key would be in the list. This is because, in determining the upper bound for the binary search, the while loop is executed exactly $\lceil \log(i)\rceil$ times. Since the list is sorted, after doubling the search index $\lceil \log(i)\rceil$ times, the algorithm will be at a search index that is greater than or equal to *i* as $2^{\lceil \log(i)\rceil }\geq i$ . As such, the first stage of the algorithm takes $O(\log i)$ time.

The second part of the algorithm also takes $O(\log i)$ time. As the second stage is simply a binary search, it takes $O(\log n)$ where *n* is the size of the interval being searched. The size of this interval would be 2*j* - 2*j* - 1 where, as seen above, *j* = $\log i$ . This means that the size of the interval being searched is 2log *i* - 2log *i* - 1 = 2log *i* - 1. This gives us a runtime of log (2log *i* - 1) = log (*i*) - 1 = $O(\log i)$ .

This gives the algorithm a total runtime, calculated by summing the runtimes of the two stages, of $O(\log i)$ + $O(\log i)$ = 2 $O(\log i)$ = $O(\log i)$ .

## Alternatives

Bentley and Yao suggested several variations for exponential search. These variations consist of performing a binary search, as opposed to a unary search, when determining the upper bound for the binary search in the second stage of the algorithm. This splits the first stage of the algorithm into two parts, making the algorithm a three-stage algorithm overall. The new first stage determines a value *$j'$*, much like before, such that $2^{j'}$ is larger than the search key and $2^{j'/2}$ is lower than the search key. Previously, *$j'$* was determined in a unary fashion by calculating the next power of 2 (i.e., adding 1 to *j*). In the variation, it is proposed that $j'$ is doubled instead (e.g., jumping from 22 to 24 as opposed to 23). The first *$j'$* such that $2^{j'}$ is greater than the search key forms a much rougher upper bound than before. Once this *$j'$* is found, the algorithm moves to its second stage and a binary search is performed on the interval formed by $j'/2$ and $j'$ , giving the more accurate upper bound exponent *j*. From here, the third stage of the algorithm performs the binary search on the interval 2*j* - 1 and 2*j*, as before. The performance of this variation is $\lfloor \log i\rfloor +2\lfloor \log(\lfloor \log i\rfloor +1)\rfloor +1=O(\log i)$ .

Bentley and Yao generalize this variation into one where any number, *k*, of binary searches are performed during the first stage of the algorithm, giving the *k*-nested binary search variation. The asymptotic runtime does not change for the variations, running in $O(\log i)$ time, as with the original exponential search algorithm.

Also, a data structure with a tight version of the dynamic finger property can be given when the above result of the *k*-nested binary search is used on a sorted array. Using this, the number of comparisons done during a search is log (*d*) + log log (*d*) + ... + *O*(log **d*), where *d* is the difference in rank between the last element that was accessed and the current element being accessed.

## Applications

An algorithm based on exponentially increasing the search band solves global pairwise alignment for *$O(ns)$*, where *n* is the length of the sequences and *s* is the edit distance between them.
