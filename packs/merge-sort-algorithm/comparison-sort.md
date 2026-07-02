---
title: "Comparison sort"
source: https://en.wikipedia.org/wiki/Comparison_sort
domain: merge-sort-algorithm
license: CC-BY-SA-4.0
tags: merge sort, stable sort, external sorting, merge algorithm
fetched: 2026-07-02
---

# Comparison sort

A **comparison sort** is a type of sorting algorithm that only reads the list elements through a single abstract comparison operation (often a "less than or equal to" operator or a three-way comparison) that determines which of two elements should occur first in the final sorted list. The only requirement is that the operator forms a total preorder over the data; that is:

1. if *a* ≤ *b* and *b* ≤ *c* then *a* ≤ *c* (transitivity)
2. for all *a* and *b*, *a* ≤ *b* or *b* ≤ *a* (connexity).

It is possible that both *a* ≤ *b* and *b* ≤ *a* with *a* ≠ *b*; in this case either may come first in the sorted list. In a stable sort, the input order determines the sorted order in this case.

Comparison sorts studied in the literature are "comparison-based". Elements *a* and *b* can be swapped or otherwise re-arranged by the algorithm only when the order between these elements has been established based on the outcomes of prior comparisons. This is the case when the order between *a* and *b* can be derived via the transitive closure of these prior comparison outcomes.

For comparison-based sorts, the decision to execute basic operations other than comparisons is based on the outcome of comparisons. Hence in a time analysis, the number of executed comparisons is used to determine upper bound estimates for the number of executed basic operations such as swaps or assignments.

A metaphor for thinking about comparison sorts is that someone has a set of unlabelled weights and a balance scale. Their goal is to line up the weights in order by their weight without any information except that obtained by placing two weights on the scale and seeing which one is heavier (or if they weigh the same).

## Examples

Some of the most well-known comparison sorts include:

- Quicksort
- Heapsort
- Shellsort
- Merge sort
- Introsort
- Insertion sort
- Selection sort
- Bubble sort
- Odd–even sort
- Cocktail shaker sort
- Cycle sort
- Merge-insertion sort
- Smoothsort
- Timsort
- Block sort

## Performance limits and advantages of different sorting techniques

There are fundamental limits on the performance of comparison sorts. A comparison sort must have an average-case lower bound of Ω(*n* log *n*) comparison operations, which is known as linearithmic time. This is a consequence of the limited information available through comparisons alone — or, to put it differently, of the vague algebraic structure of totally ordered sets. In this sense, mergesort, heapsort, and introsort are asymptotically optimal in terms of the number of comparisons they must perform, although this metric neglects other operations. Non-comparison sorts (such as the examples discussed below) can achieve O(*n*) performance by using operations other than comparisons, allowing them to sidestep this lower bound (assuming elements are constant-sized).

Comparison sorts may run faster on some lists; many adaptive sorts such as insertion sort run in O(*n*) time on an already-sorted or nearly-sorted list. The Ω(*n* log *n*) lower bound applies only to the case in which the input list can be in any possible order.

Real-world measures of sorting speed may need to take into account the ability of some algorithms to optimally use relatively fast cached computer memory, or the application may benefit from sorting methods where sorted data begins to appear to the user quickly (and then user's speed of reading will be the limiting factor) as opposed to sorting methods where no output is available until the whole list is sorted.

Despite these limitations, comparison sorts offer the notable practical advantage that control over the comparison function allows sorting of many different datatypes and fine control over how the list is sorted. For example, reversing the result of the comparison function allows the list to be sorted in reverse; and one can sort a list of tuples in lexicographic order by just creating a comparison function that compares each part in sequence:

```
function tupleCompare((lefta, leftb, leftc), (righta, rightb, rightc))
    if lefta ≠ righta
        return compare(lefta, righta)
    else if leftb ≠ rightb
        return compare(leftb, rightb)
    else
        return compare(leftc, rightc)
```

Comparison sorts generally adapt more easily to complex orders such as the order of floating-point numbers. Additionally, once a comparison function is written, any comparison sort can be used without modification; non-comparison sorts typically require specialized versions for each datatype.

This flexibility, together with the efficiency of the above comparison sorting algorithms on modern computers, has led to widespread preference for comparison sorts in most practical work.

## Alternatives

Some sorting problems admit a strictly faster solution than the Ω(*n* log *n*) bound for comparison sorting by using non-comparison sorts; an example is integer sorting, where all keys are integers. When the keys form a small (compared to n) range, counting sort is an example algorithm that runs in linear time. Other integer sorting algorithms, such as radix sort, are not asymptotically faster than comparison sorting, but can be faster in practice.

The problem of sorting pairs of numbers by their sum is not subject to the Ω(*n*² log *n*) bound either (the square resulting from the pairing up); the best known algorithm still takes O(*n*² log *n*) time, but only O(*n*²) comparisons.

## Number of comparisons required to sort a list

| *n* | $\left\lceil \log _{2}(n!)\right\rceil$ | Minimum |
|---|---|---|
| 1 | 0 | 0 |
| 2 | 1 | 1 |
| 3 | 3 | 3 |
| 4 | 5 | 5 |
| 5 | 7 | 7 |
| 6 | 10 | 10 |
| 7 | 13 | 13 |
| 8 | 16 | 16 |
| 9 | 19 | 19 |
| 10 | 22 | 22 |
| 11 | 26 | 26 |
| 12 | 29 | 30 |
| 13 | 33 | 34 |
| 14 | 37 | 38 |
| 15 | 41 | 42 |
| 16 | 45 | 46 |
| 17 | 49 | 50 |
| 18 | 53 | 54 |
| 19 | 57 | 58 |
| 20 | 62 | 62 |
| 21 | 66 | 66 |
| 22 | 70 | 71 |
|   |   |   |
| *n* | $\left\lceil \log _{2}(n!)\right\rceil$ | $n\log _{2}n-{\frac {n}{\ln 2}}$ |
| 10 | 22 | 19 |
| 100 | 525 | 521 |
| 1 000 | 8 530 | 8 524 |
| 10 000 | 118 459 | 118 451 |
| 100 000 | 1 516 705 | 1 516 695 |
| 1 000 000 | 18 488 885 | 18 488 874 |

Above: A comparison of the lower bound

$\left\lceil \log _{2}(n!)\right\rceil$

to the actual minimum number of comparisons (from

OEIS

:

A036604

) required to sort a list of

n

items (for the worst case). Below: Using

Stirling's approximation

, this lower bound is well-approximated by

$n\log _{2}n-{\frac {n}{\ln 2}}$

.

The number of comparisons that a comparison sort algorithm requires increases in proportion to $n\log(n)$ , where n is the number of elements to sort. This bound is asymptotically tight.

Given a list of distinct numbers (we can assume this because this is a worst-case analysis), there are n factorial permutations exactly one of which is the list in sorted order. The sort algorithm must gain enough information from the comparisons to identify the correct permutation. If the algorithm always completes after at most $f(n)$ steps, it cannot distinguish more than $2^{f(n)}$ cases because the keys are distinct and each comparison has only two possible outcomes. Therefore,

$2^{f(n)}\geq n!$

, or equivalently

$f(n)\geq \log _{2}(n!).$

By looking at the first $n/2$ factors of $n!=n(n-1)\cdots 1$ , we obtain

$\log _{2}(n!)\geq \log _{2}\left(\left({\frac {n}{2}}\right)^{\frac {n}{2}}\right)={\frac {n}{2}}{\frac {\log n}{\log 2}}-{\frac {n}{2}}=\Theta (n\log n).$

$\log _{2}(n!)=\Omega (n\log n).$

This provides the lower-bound part of the claim. A more precise bound can be given via Stirling's approximation. An upper bound of the same form, with the same leading term as the bound obtained from Stirling's approximation, follows from the existence of the algorithms that attain this bound in the worst case, like merge sort.

The above argument provides an *absolute*, rather than only asymptotic lower bound on the number of comparisons, namely $\left\lceil \log _{2}(n!)\right\rceil$ comparisons. This lower bound is fairly good (it can be approached within a linear tolerance by a simple merge sort), but it is known to be inexact. For example, $\left\lceil \log _{2}(13!)\right\rceil =33$ , but the minimal number of comparisons to sort 13 elements has been proved to be 34.

Determining the *exact* number of comparisons needed to sort a given number of entries is a computationally hard problem even for small *n*, and no simple formula for the solution is known. For some of the few concrete values that have been computed, see OEIS: A036604.

### Lower bound for the average number of comparisons

A similar bound applies to the average number of comparisons. Assuming that

- all keys are distinct, i.e. every comparison will give either *a*>*b* or *a*<*b*, and
- the input is a random permutation, chosen uniformly from the set of all possible permutations of *n* elements,

it is impossible to determine which order the input is in with fewer than log2(*n*!) comparisons on average.

This can be most easily seen using concepts from information theory. The Shannon entropy of such a random permutation is log2(*n*!) bits. Since a comparison can give only two results, the maximum amount of information it provides is 1 bit. Therefore, after *k* comparisons the remaining entropy of the permutation, given the results of those comparisons, is at least log2(*n*!) − *k* bits on average. To perform the sort, complete information is needed, so the remaining entropy must be 0. It follows that *k* must be at least log2(*n*!) on average.

The lower bound derived via information theory is phrased as 'information-theoretic lower bound'. The information-theoretic lower bound is correct, but may be far from the strongest possible lower bound. For example, the information-theoretic lower bound of selection is $\left\lceil \log _{2}(n)\right\rceil$ whereas $n-1$ comparisons are needed by an adversarial argument. The interplay between information-theoretic lower bound and the true lower bound are much like a real-valued function lower-bounding an integer function. However, this is not exactly correct when the average case is considered.

To unearth what happens while analyzing the average case, the key is that what does 'average' refer to? Averaging over what? With some knowledge of information theory, the information-theoretic lower bound averages over the set of all permutations as a whole. But any computer algorithms (under what are believed currently) must treat each permutation as an individual instance of the problem. Hence, the average lower bound we're searching for is averaged over all individual cases.

To search for the lower bound relating to the non-achievability of computers, we adopt the Decision tree model. Let's rephrase a bit of what our objective is. In the Decision tree model, the lower bound to be shown is the lower bound of the average length of root-to-leaf paths of an $n!$ -leaf binary tree (in which each leaf corresponds to a permutation). The minimum average length of a binary tree with a given number of leaves is achieved by a balanced full binary tree, because any other binary tree can have its path length reduced by moving a pair of leaves to a higher position. With some careful calculations, for a balanced full binary tree with $n!$ leaves, the average length of root-to-leaf paths is given by

${\frac {(2n!-2^{\lfloor \log _{2}n!\rfloor +1})\cdot \lceil \log _{2}n!\rceil +(2^{\lfloor \log _{2}n!\rfloor +1}-n!)\cdot \lfloor \log _{2}n!\rfloor }{n!}}=\lceil \log _{2}n!\rceil +1-{\frac {2^{\lceil \log _{2}n!\rceil }}{n!}}$

For example, for *n* = 3, the information-theoretic lower bound for the average case is approximately 2.58, while the average lower bound derived via Decision tree model is 8/3, approximately 2.67.

In the case that multiple items may have the same key, there is no obvious statistical interpretation for the term "average case", so an argument like the above cannot be applied without making specific assumptions about the distribution of keys.

### n log n maximum number of comparisons for array-size in format 2^k

Can easy compute for real algorithm sorted-list-merging (array are sorted n-blocks with size 1, merge to 1–1 to 2, merge 2–2 to 4...).

```
(1) = = = = = = = =

(2) =   =   =   =     // max 1 compares (size1+size2-1), 4x repeats to concat 8 arrays with size 1 and 1
   === === === ===

(3)   =       =       // max 7 compares, 2x repeats to concat 4 arrays with size 2 and 2
     ===     ===  
    =====   ===== 
   ======= =======

(4)                   // max 15 compares, 1x repeats to concat 2 arrays with size 4 and 4

Formula extraction:
n = 256 = 2^8 (array size in format 2^k, for simplify)
On = (n-1) + 2(n/2-1) + 4(n/4-1) + 8(n/8-1) + 16(n/16-1) + 32(n/32-1) + 64(n/64-1) + 128(n/128-1)
On = (n-1) + (n-2) + (n-4) + (n-8) + (n-16) + (n-32) + (n-64) + (n-128)
On = n+n+n+n+n+n+n+n - (1+2+4+8+16+32+64+128)   | 1+2+4... = formula for geometric sequence Sn = a1 * (q^i - 1) / (n - 1), n is number of items, a1 is first item
On = 8*n - 1 * (2^8 - 1) / (2 - 1)
On = 8*n - (2^8 - 1)   | 2^8 = n
On = 8*n - (n - 1)
On = (8-1)*n + 1   | 8 = ln(n)/ln(2) = ln(256)/ln(2)
On = (ln(n)/ln(2) - 1) * n + 1

Example:
n = 2^4 = 16, On ~= 3*n
n = 2^8 = 256, On ~= 7*n
n = 2^10 = 1.024, On ~= 9*n
n = 2^20 = 1.048.576, On ~= 19*n
```

### Sorting a pre-sorted list

If a list is already close to sorted, according to some measure of sortedness, the number of comparisons required to sort it can be smaller. An adaptive sort takes advantage of this "presortedness" and runs more quickly on nearly-sorted inputs, often while still maintaining an $O(n\log n)$ worst case time bound. An example is adaptive heap sort, a sorting algorithm based on Cartesian trees. It takes time $O(n\log k)$ , where k is the average, over all values x in the sequence, of the number of times the sequence jumps from below x to above x or vice versa.
