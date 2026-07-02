---
title: "Dutch national flag problem"
source: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
domain: quicksort-algorithm
license: CC-BY-SA-4.0
tags: quicksort algorithm, divide and conquer, partition scheme, quickselect algorithm
fetched: 2026-07-02
---

# Dutch national flag problem

The **Dutch national flag problem** is a computational problem proposed by Edsger Dijkstra. The flag of the Netherlands consists of three colors: red, white, and blue. Given balls of these three colors arranged randomly in a line (it does not matter how many balls there are), the task is to arrange them such that all balls of the same color are together and their collective color groups are in the correct order.

The solution to this problem is of interest for designing sorting algorithms; in particular, variants of the quicksort algorithm that must be robust to repeated elements may use a three-way partitioning function that groups items less than a given key (red), equal to the key (white) and greater than the key (blue). Several solutions exist that have varying performance characteristics, tailored to sorting arrays with either small or large numbers of repeated elements.

## The array case

This problem can also be viewed in terms of rearranging elements of an array. Suppose each of the possible elements could be classified into exactly one of three categories (bottom, middle, and top). For example, if all the elements are in 0 ... 1, the bottom could be defined as elements in 0 ... 0.25 (not including 0.25), the middle as 0.25 ... 0.5 (not including 0.5) and the top as 0.5 and greater. (The choice of these values illustrates that the categories need not be equal ranges). The problem is then to produce an array such that all "bottom" elements come before (have an index less than the index of) all "middle" elements, which come before all "top" elements.

One algorithm is to have the top group grow down from the top of the array, the bottom group grow up from the bottom, and keep the middle group just above the bottom. The algorithm indexes three locations, the bottom of the top group, the top of the bottom group, and the top of the middle group. Elements that are yet to be sorted fall between the middle and the top group. At each step, examine the element just above the middle. If it belongs to the top group, swap it with the element just below the top. If it belongs in the bottom, swap it with the element just above the bottom. If it is in the middle, leave it. Update the appropriate index. Complexity is Θ(n) moves and examinations.

### Pseudocode

The following pseudocode for three-way partitioning which assumes zero-based array indexing was proposed by Dijkstra himself. It uses three indices i, j and k, maintaining the invariant that *i* ≤ *j* ≤ *k*.

- Entries from 0 up to (but not including) i are values less than mid,
- entries from i up to (but not including) j are values equal to mid,
- entries from j up to (and including) k are values not yet sorted, and
- entries from k + 1 to the end of the array are values greater than mid.

```
procedure three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    k ← size of A - 1

    while j <= k:
        if A[j] < mid:
            swap A[i] and A[j]
            i ← i + 1
            j ← j + 1
        else if A[j] > mid:
            swap A[j] and A[k]
            k ← k - 1
        else:
            j ← j + 1
```
