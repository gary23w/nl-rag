---
title: "Shellsort"
source: https://en.wikipedia.org/wiki/Shellsort
domain: shellsort-algorithm
license: CC-BY-SA-4.0
tags: shellsort algorithm, gap sequence, insertion sort, in place algorithm
fetched: 2026-07-02
---

# Shellsort

**Shellsort**, also known as **Shell sort** or **Shell's method**, is an in-place comparison sort. It can be understood as either a generalization of sorting by exchange (bubble sort) or sorting by insertion (insertion sort). The method starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between elements to be compared. By starting with far-apart elements, it can move some out-of-place elements into the position faster than a simple nearest-neighbor exchange. The running time of Shellsort is heavily dependent on the gap sequence it uses. For many practical variants, determining their time complexity remains an open problem.

The algorithm was first published by Donald Shell in 1959, and has nothing to do with shells.

## Description

Shellsort is an optimization of insertion sort that allows the exchange of items that are far apart. The idea is to arrange the list of elements so that, starting anywhere, taking every *h*th element produces a sorted list. Such a list is said to be *h*-sorted. It can also be thought of as *h* interleaved lists, each individually sorted. Beginning with large values of *h* allows elements to move long distances in the original list, reducing large amounts of disorder quickly, and leaving less work for smaller *h*-sort steps to do. If the list is then *k-sorted* for some smaller integer *k*, then the list remains *h*-sorted. A final sort with *h* = 1 ensures the list is fully sorted at the end, but a judiciously chosen decreasing sequence of *h* values leaves very little work for this final pass to do.

In simplistic terms, this means if we have an array of 1024 numbers, our first gap (*h*) could be 512. We then run through the list comparing each element in the first half to the element in the second half. Our second gap (*k*) is 256, which breaks the array into four sections (starting at 0, 256, 512, 768), and we make sure the first items in each section are sorted relative to each other, then the second item in each section, and so on. In practice the gap sequence could be anything, but the last gap is always 1 to finish the sort (effectively finishing with an ordinary insertion sort).

An example run of Shellsort with gaps 5, 3 and 1 is shown below.

a

1

a

2

a

3

a

4

a

5

a

6

a

7

a

8

a

9

a

10

a

11

a

12

Input data

62

83

18

53

07

17

95

86

47

69

25

28

After 5-sorting

17

28

18

47

07

25

83

86

53

69

62

95

After 3-sorting

17

07

18

47

28

25

69

62

53

83

86

95

After 1-sorting

07

17

18

25

28

47

53

62

69

83

86

95

The first pass, 5-sorting, performs insertion sort on five separate subarrays (*a*1, *a*6, *a*11), (*a*2, *a*7, *a*12), (*a*3, *a*8), (*a*4, *a*9), (*a*5, *a*10). For instance, it changes the subarray (*a*1, *a*6, *a*11) from (62, 17, 25) to (17, 25, 62). The next pass, 3-sorting, performs insertion sort on the three subarrays (*a*1, *a*4, *a*7, *a*10), (*a*2, *a*5, *a*8, *a*11), (*a*3, *a*6, *a*9, *a*12). The last pass, 1-sorting, is an ordinary insertion sort of the entire array (*a*1,..., *a*12).

As the example illustrates, the subarrays that Shellsort operates on are initially short; later they are longer but almost ordered. In both cases insertion sort works efficiently.

Unlike insertion sort, Shellsort is not a stable sort since gapped insertions transport equal elements past one another and thus lose their original order. It is an adaptive sorting algorithm in that it executes faster when the input is partially sorted.

## Example

This is a C# example using Marcin Ciura's gap sequence, with an inner insertion sort.

```mw
using System.Collections.Generic;

// Sort an array a[0...n-1].
List<int> gaps = [701, 301, 132, 57, 23, 10, 4, 1]; // Ciura gap sequence

// Start with the largest gap and work down to a gap of 1
// similar to insertion sort but instead of 1, gap is being used in each step
foreach (int gap in gaps)
{
    // Do a gapped insertion sort for every element in gaps
    // Each loop leaves a[0..gap-1] in gapped order
    for (int i = gap; i < n; ++i)
    {
        // save a[i] in temp and make a hole at position i
        int temp = a[i];
        // shift earlier gap-sorted elements up until the correct location for a[i] is found
        for (int j = i; (j >= gap) && (a[j - gap] > temp); j -= gap)
        {
            a[j] = a[j - gap];
        }
        // put temp (the original a[i]) in its correct location
        a[j] = temp;
    }
}
```

## Gap sequences

The question of deciding which gap sequence to use is difficult. Every gap sequence that contains 1 yields a correct sort (as this makes the final pass an ordinary insertion sort); however, the properties of thus obtained versions of Shellsort may be very different. Too few gaps slows down the passes, and too many gaps produces an overhead.

The table below compares most proposed gap sequences published so far. Some of them have decreasing elements that depend on the size of the sorted array (*N*). Others are increasing infinite sequences, whose elements less than *N* should be used in reverse order.

| OEIS | General term (*k* ≥ 1) | Concrete gaps | Worst-case time complexity | Author and year of publication |
|---|---|---|---|---|
|   | $\left\lfloor {\frac {N}{2^{k}}}\right\rfloor$ | $1,2,\ldots ,\left\lfloor {\frac {N}{4}}\right\rfloor ,\left\lfloor {\frac {N}{2}}\right\rfloor$ | $\Theta \left(N^{2}\right)$ [e.g. when *N* = 2*p*] | Shell, 1959 |
|   | $2\left\lfloor {\frac {N}{2^{k+1}}}\right\rfloor +1$ | $1,3,\ldots ,\;2\left\lfloor {\frac {N}{8}}\right\rfloor +1,\;\;2\left\lfloor {\frac {N}{4}}\right\rfloor +1$ | $\Theta \left(N^{\frac {3}{2}}\right)$ | Frank & Lazarus, 1960 |
| A000225 | $2^{k}-1$ | $1,3,7,15,31,63,\ldots$ | $\Theta \left(N^{\frac {3}{2}}\right)$ | Hibbard, 1963 |
| A083318 | $2^{k}+1$ , prefixed with 1 | $1,3,5,9,17,33,65,\ldots$ | $\Theta \left(N^{\frac {3}{2}}\right)$ | Papernov & Stasevich, 1965 |
| A003586 | Successive numbers of the form $2^{p}3^{q}$ (3-smooth numbers) | $1,2,3,4,6,8,9,12,\ldots$ | $\Theta \left(N\log ^{2}N\right)$ | Pratt, 1971 |
| A003462 | ${\frac {3^{k}-1}{2}}$ , not greater than $\left\lceil {\frac {N}{3}}\right\rceil$ | $1,4,13,40,121,\ldots$ | $\Theta \left(N^{\frac {3}{2}}\right)$ | Knuth, 1973, based on Pratt, 1971 |
| A036569 | ${\begin{aligned}&\prod \limits _{I}a_{q},{\hbox{where}}\\a_{0}={}&3\\a_{q}={}&\min \left\{n\in \mathbb {N} \colon n\geq \left({\frac {5}{2}}\right)^{q+1},\forall p\colon 0\leq p<q\Rightarrow \gcd(a_{p},n)=1\right\}\\I={}&\left\{0\leq q<r\mid q\neq {\frac {1}{2}}\left(r^{2}+r\right)-k\right\}\\r={}&\left\lfloor {\sqrt {2k+{\sqrt {2k}}}}\right\rfloor \end{aligned}}$ | $1,3,7,21,48,112,\ldots$ | $O\left(N^{1+{\sqrt {\frac {8\ln \left(5/2\right)}{\ln(N)}}}}\right)$ | Incerpi & Sedgewick, 1985, Knuth |
| A036562 | $4^{k}+3\cdot 2^{k-1}+1$ , prefixed with 1 | $1,8,23,77,281,\ldots$ | $O\left(N^{\frac {4}{3}}\right)$ | Sedgewick, 1982 |
| A033622 | ${\begin{cases}9\left(2^{k}-2^{\frac {k}{2}}\right)+1&k{\text{ even}},\\8\cdot 2^{k}-6\cdot 2^{(k+1)/2}+1&k{\text{ odd}}\end{cases}}$ | $1,5,19,41,109,\ldots$ | $O\left(N^{\frac {4}{3}}\right)$ | Sedgewick, 1986 |
|   | $h_{k}=\max \left\{\left\lfloor {\frac {5h_{k-1}-1}{11}}\right\rfloor ,1\right\},h_{0}=N$ | $1,\ldots ,\left\lfloor {\frac {5}{11}}\left\lfloor {\frac {5N-1}{11}}\right\rfloor -{\frac {1}{11}}\right\rfloor ,\left\lfloor {\frac {5N-1}{11}}\right\rfloor$ | $\Theta \left(N^{2}\right)$ [for certain values of *N*] | Gonnet & Baeza-Yates, 1991 |
| A108870 | $\left\lceil {\frac {1}{5}}\left(9\cdot \left({\frac {9}{4}}\right)^{k-1}-4\right)\right\rceil$ (or equivalently, $\left\lceil {\frac {\left(9/4\right)^{k}-1}{\left(9/4\right)-1}}\right\rceil$ ) | $1,4,9,20,46,103,\ldots$ | Unknown | Tokuda, 1992 (misquote per OEIS) |
| A102549 | Unknown (experimentally derived) | $1,4,10,23,57,132,301,701$ | Unknown | Ciura, 2001 |
| A366726 | $\left\lceil {\frac {\gamma ^{k}-1}{\gamma -1}}\right\rceil ,\gamma =2.243609061420001\ldots$ | $1,4,9,20,45,102,230,516,\ldots$ | Unknown | Lee, 2021 |
|   | $\left\lfloor 4.0816\cdot 8.5714^{\frac {k}{2.2449}}\right\rfloor$ | $1,4,10,27,72,187,488,\ldots$ | Unknown | Skean, Ehrenborg, Jaromczyk, 2023 |

When the binary representation of *N* contains many consecutive zeroes, Shellsort using Shell's original gap sequence makes Θ(*N*2) comparisons in the worst case. For instance, this case occurs for *N* equal to a power of two when elements greater and smaller than the median occupy odd and even positions respectively, since they are compared only in the last pass.

The Gonnet and Baeza-Yates implementation of Shellsort (GBY91) also uses gaps that start with *N* and performs better than many of the other sequences on average, but is also prone to a Θ(*N*2) worst case: Let X be a gap in the sequence. The GBY91 gaps' common ratio of 2.2 permits at least two consecutive integers Y and Y+1 to equal X from floor division by 2.2. Choose Y or Y+1, whichever one is even, to repeat the process, and one obtains an infinitely long chain of even gaps > X by induction. With X = 1, one generates infinite options for *N* where all GBY91 gaps > 1 are even and thus are Θ(*N*2) on the same aforementioned worst case input for Shell's original gaps.

Although it has higher complexity than the *O*(*N* log *N*) that is optimal for comparison sorts, Pratt's version lends itself to sorting networks and has the same asymptotic gate complexity as Batcher's bitonic sorter.

Gonnet and Baeza-Yates observed that Shellsort makes the fewest comparisons on average when the ratios of successive gaps are roughly equal to 2.2. This is why their sequence with ratio 2.2 and Tokuda's sequence with ratio 2.25 prove efficient. However, it is not known why this is so. Sedgewick recommends using gaps which have low greatest common divisors or are pairwise coprime. Using gaps which are odd numbers appears to help - speedups of about 25% have been seen in practice versus Shell's original code. Using gaps which are not multiples of 2, 3 or 5 appear to reduce run times further - speedups of about 35% versus Shell's original seem possible. Using gaps which are prime numbers only (ending with 1), appear to produce speedups of about 40% over the original code.

With respect to the average number of comparisons, Ciura's sequence has the best known performance; gaps greater than 701 were not determined but the sequence can be further extended according to the recursive formula $h_{k}=\lfloor 2.25h_{k-1}\rfloor$ .

Tokuda's sequence, defined by the simple formula $h_{k}=\lceil h'_{k}\rceil$ , where $h'_{k}=2.25h'_{k-1}+1$ , $h'_{1}=1$ , can be recommended for practical applications.

If the maximum input size is small, as may occur if Shellsort is used on small subarrays by another recursive sorting algorithm such as quicksort or merge sort, then it is possible to tabulate an optimal sequence for each input size. For N = 128 and N = 1000, Ciura empirically found that (1, 4, 9, 24, 85) and (1, 4, 10, 23, 57, 156, 409, 995) made the fewest number of comparisons on average respectively.

## Computational complexity

The following property holds: after *h*2-sorting of any *h*1-sorted array, the array remains *h*1-sorted. Every *h*1-sorted and *h*2-sorted array is also (*a*1*h*1+*a*2*h*2)-sorted, for any nonnegative integers *a*1 and *a*2. The worst-case complexity of Shellsort is therefore connected with the Frobenius problem: for given integers *h*1,..., *hn* with gcd = 1, the Frobenius number *g*(*h*1,..., *hn*) is the greatest integer that cannot be represented as *a*1*h*1+ ... +*anhn* with nonnegative integer *a*1,..., *an*. Using known formulae for Frobenius numbers, we can determine the worst-case complexity of Shellsort for several classes of gap sequences. Proven results are shown in the above table.

Mark Allen Weiss proved that Shellsort runs in *O*(*N* log *N*) time when the input array is in reverse order.

With respect to the average number of operations, none of the proven results concerns a practical gap sequence. For gaps that are powers of two, Espelid computed this average as $0.5349N{\sqrt {N}}-0.4387N-0.097{\sqrt {N}}+O(1)$ . Knuth determined the average complexity of sorting an *N*-element array with two gaps (*h*, 1) to be ${\frac {2N^{2}}{h}}+{\sqrt {\pi N^{3}h}}$ . It follows that a two-pass Shellsort with *h* = Θ(*N*1/3) makes on average *O*(*N*5/3) comparisons/inversions/running time. Yao found the average complexity of a three-pass Shellsort. His result was refined by Janson and Knuth: the average number of comparisons/inversions/running time made during a Shellsort with three gaps (*ch*, *cg*, 1), where *h* and *g* are coprime, is ${\frac {N^{2}}{4ch}}+O(N)$ in the first pass, ${\frac {1}{8g}}{\sqrt {\frac {\pi }{ch}}}(h-1)N^{3/2}+O(hN)$ in the second pass and $\psi (h,g)N+{\frac {1}{8}}{\sqrt {\frac {\pi }{c}}}(c-1)N^{3/2}+O\left((c-1)gh^{1/2}N\right)+O\left(c^{2}g^{3}h^{2}\right)$ in the third pass. *ψ*(*h*, *g*) in the last formula is a complicated function asymptotically equal to ${\sqrt {\frac {\pi h}{128}}}g+O\left(g^{-1/2}h^{1/2}\right)+O\left(gh^{-1/2}\right)$ . In particular, when *h* = Θ(*N*7/15) and *g* = Θ(*N*1/5), the average time of sorting is *O*(*N*23/15).

Based on experiments, it is conjectured that Shellsort with Hibbard's gap sequence runs in *O*(*N*5/4) average time, and that Gonnet and Baeza-Yates's sequence requires on average 0.41*N* ln *N* (ln ln *N* + 1/6) element moves. Approximations of the average number of operations formerly put forward for other sequences fail when sorted arrays contain millions of elements.

The graph below shows the average number of element comparisons use by various gap sequences, divided by the theoretical lower bound, i.e. log2*N*!. Ciuria's sequence 1, 4, 10, 23, 57, 132, 301, 701 (labelled Ci01) has been extended according to the formula $h_{k}=\lfloor 2.25h_{k-1}\rfloor$ .

Applying the theory of Kolmogorov complexity, Jiang, Li, and Vitányi proved the following lower bound for the order of the average number of operations/running time in a *p*-pass Shellsort: Ω(*pN*1+1/*p*) when *p* ≤ log2*N* and Ω(*pN*) when *p* > log2*N*. Therefore, Shellsort has prospects of running in an average time that asymptotically grows like *N* log*N* only when using gap sequences whose number of gaps grows in proportion to the logarithm of the array size. It is, however, unknown whether Shellsort can reach this asymptotic order of average-case complexity, which is optimal for comparison sorts. The lower bound was improved by Vitányi for every number of passes p to $\Omega (N\sum _{k=1}^{p}h_{k-1}/h_{k})$ where $h_{0}=N$ . This result implies for example the Jiang-Li-Vitányi lower bound for all p -pass increment sequences and improves that lower bound for particular increment sequences. In fact all bounds (lower and upper) currently known for the average case are precisely matched by this lower bound. For example, this gives the new result that the Janson-Knuth upper bound is matched by the resulting lower bound for the used increment sequence, showing that three pass Shellsort for this increment sequence uses $\Theta (N^{23/15})$ comparisons/inversions/running time. The formula allows us to search for increment sequences that yield lower bounds which are unknown; for example an increment sequence for four passes which has a lower bound greater than $\Omega (pn^{1+1/p})=\Omega (n^{5/4})$ for the increment sequence $h_{1}=n^{11/16},$ $h_{2}=n^{7/16},$ $h_{3}=n^{3/16},$ $h_{4}=1$ . The lower bound becomes $T=\Omega (n\cdot (n^{1-11/16}+n^{11/16-7/16}+n^{7/16-3/16}+n^{3/16})=\Omega (n^{1+5/16})=\Omega (n^{21/16}).$

The worst-case complexity of any version of Shellsort is of higher order: Plaxton, Poonen, and Suel showed that it grows at least as rapidly as $\Omega \left(N\left({\log N \over \log \log N}\right)^{2}\right)$ . Robert Cypher proved a stronger lower bound: $\Omega \left(N{{(\log N)^{2}} \over {\log \log N}}\right)$ when $h_{s+1}>h_{s}$ for all s .

## Applications

Shellsort performs more operations and has higher cache miss ratio than quicksort. However, since it can be implemented using little code and does not use the call stack, some implementations of the qsort function in the C standard library targeted at embedded systems use it instead of quicksort. Shellsort is, for example, used in the uClibc library. For similar reasons, in the past, Shellsort was used in the Linux kernel.

Shellsort can also serve as a sub-algorithm of introspective sort, to sort short subarrays and to prevent a slowdown when the recursion depth exceeds a given limit. This principle is employed, for instance, in the bzip2 compressor.
