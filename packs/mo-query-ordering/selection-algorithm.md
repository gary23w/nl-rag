---
title: "Selection algorithm"
source: https://en.wikipedia.org/wiki/Selection_algorithm
domain: mo-query-ordering
license: CC-BY-SA-4.0
tags: mo algorithm, offline query ordering, query square root blocking, range query batching
fetched: 2026-07-02
---

# Selection algorithm

In computer science, a **selection algorithm** is an algorithm for finding the k th smallest value in a collection of orderable values, such as numbers. The value that it finds is called the k th order statistic. Selection includes as special cases the problems of finding the minimum, median, and maximum element in the collection. Selection algorithms include quickselect, and the median of medians algorithm. When applied to a collection of n values, these algorithms take linear time, $O(n)$ as expressed using big O notation. For data that is already structured, faster algorithms may be possible; as an extreme case, selection in an already-sorted array takes time $O(1)$ .

## Problem statement

An algorithm for the selection problem takes as input a collection of values, and a number k . It outputs the k th smallest of these values, or, in some versions of the problem, a collection of the k smallest values. For this to be well-defined, it should be possible to sort the values into an order from smallest to largest; for instance, they may be integers, floating-point numbers, or some other kind of object with a numeric key. However, they are not assumed to have been already sorted. Often, selection algorithms are restricted to a comparison-based model of computation, as in comparison sort algorithms, where the algorithm has access to a comparison operation that can determine the relative ordering of any two values, but may not perform any other kind of arithmetic operations on these values.

To simplify the problem, some works on this problem assume that the values are all distinct from each other, or that some consistent tie-breaking method has been used to assign an ordering to pairs of items with the same value as each other. Another variation in the problem definition concerns the numbering of the ordered values: is the smallest value obtained by setting $k=0$ , as in zero-based numbering of arrays, or is it obtained by setting $k=1$ , following the usual English-language conventions for the smallest, second-smallest, etc.? This article follows the conventions used by Cormen et al., according to which all values are distinct and the minimum value is obtained from $k=1$ .

With these conventions, the maximum value, among a collection of n values, is obtained by setting $k=n$ . When n is an odd number, the median of the collection is obtained by setting $k=(n+1)/2$ . When n is even, there are two choices for the median, obtained by rounding this choice of k down or up, respectively: the *lower median* with $k=n/2$ and the *upper median* with $k=n/2+1$ .

## Algorithms

### Sorting and heapselect

As a baseline algorithm, selection of the k th smallest value in a collection of values can be performed by the following two steps:

- Sort the collection
- If the output of the sorting algorithm is an array, retrieve its k th element; otherwise, scan the sorted sequence to find the k th element.

The time for this method is dominated by the sorting step, which requires $\Theta (n\log n)$ time using a comparison sort. Even when integer sorting algorithms may be used, these are generally slower than the linear time that may be achieved using specialized selection algorithms. Nevertheless, the simplicity of this approach makes it attractive, especially when a highly-optimized sorting routine is provided as part of a runtime library, but a selection algorithm is not. For inputs of moderate size, sorting can be faster than non-random selection algorithms, because of the smaller constant factors in its running time. This method also produces a sorted version of the collection, which may be useful for other later computations, and in particular for selection with other choices of k .

For a sorting algorithm that generates one item at a time, such as selection sort, the scan can be done in tandem with the sort, and the sort can be terminated once the k th element has been found. One possible design of a consolation bracket in a single-elimination tournament, in which the teams who lost to the eventual winner play another mini-tournament to determine second place, can be seen as an instance of this method. Applying this optimization to heapsort produces the heapselect algorithm, which can select the k th smallest value in time $O(n+k\log n)$ . This is fast when k is small relative to n , but degenerates to $O(n\log n)$ for larger values of k , such as the choice $k=n/2$ used for median finding.

### Pivoting

Many methods for selection are based on choosing a special "pivot" element from the input, and using comparisons with this element to divide the remaining $n-1$ input values into two subsets: the set L of elements less than the pivot, and the set R of elements greater than the pivot. The algorithm can then determine where the k th smallest value is to be found, based on a comparison of k with the sizes of these sets. In particular, if $k\leq |L|$ , the k th smallest value is in L , and can be found recursively by applying the same selection algorithm to L . If $k=|L|+1$ , then the k th smallest value is the pivot, and it can be returned immediately. In the remaining case, the k th smallest value is in R , and more specifically it is the element in position $k-|L|-1$ of R . It can be found by applying a selection algorithm recursively, seeking the value in this position in R .

As with the related pivoting-based quicksort algorithm, the partition of the input into L and R may be done by making new collections for these sets, or by a method that partitions a given list or array data type in-place. Details vary depending on how the input collection is represented. The time to compare the pivot against all the other values is $O(n)$ . However, pivoting methods differ in how they choose the pivot, which affects how big the subproblems in each recursive call will be. The efficiency of these methods depends greatly on the choice of the pivot. If the pivot is chosen badly, the running time of this method can be as slow as $O(n^{2})$ .

- If the pivot were exactly at the median of the input, then each recursive call would have at most half as many values as the previous call, and the total times would add in a geometric series to $O(n)$ . However, finding the median is itself a selection problem, on the entire original input. Trying to find it by a recursive call to a selection algorithm would lead to an infinite recursion, because the problem size would not decrease in each call.
- Quickselect chooses the pivot uniformly at random from the input values. It can be described as a prune and search algorithm, a variant of quicksort, with the same pivoting strategy, but where quicksort makes two recursive calls to sort the two subcollections L and R , quickselect only makes one of these two calls. Its expected time is $O(n)$ . For any constant C , the probability that its number of comparisons exceeds $Cn$ is superexponentially small in C .
- The Floyd–Rivest algorithm, a variation of quickselect, chooses a pivot by randomly sampling a subset of r data values, for some sample size r , and then recursively selecting two elements somewhat above and below position $rk/n$ of the sample to use as pivots. With this choice, it is likely that k is sandwiched between the two pivots, so that after pivoting only a small number of data values between the pivots are left for a recursive call. This method can achieve an expected number of comparisons that is $n+\min(k,n-k)+o(n)$ . In their original work, Floyd and Rivest claimed that the $o(n)$ term could be made as small as $O({\sqrt {n}})$ by a recursive sampling scheme, but the correctness of their analysis has been questioned. Instead, more rigorous analysis has shown that a version of their algorithm achieves $O({\sqrt {n\log n}})$ for this term. Although the usual analysis of both quickselect and the Floyd–Rivest algorithm assumes the use of a true random number generator, a version of the Floyd–Rivest algorithm using a pseudorandom number generator seeded with only logarithmically many true random bits has been proven to run in linear time with high probability.

- The median of medians method partitions the input into sets of five elements, and uses some other non-recursive method to find the median of each of these sets in constant time per set. It then recursively calls itself to find the median of these $n/5$ medians. Using the resulting median of medians as the pivot produces a partition with $\max(|L|,|R|)\leq 7n/10$ . Thus, a problem on n elements is reduced to two recursive problems on $n/5$ elements (to find the pivot) and at most $7n/10$ elements (after the pivot is used). The total size of these two recursive subproblems is at most $9n/10$ , allowing the total time to be analyzed as a geometric series adding to $O(n)$ . Unlike quickselect, this algorithm is deterministic, not randomized. It was the first linear-time deterministic selection algorithm known, and is commonly taught in undergraduate algorithms classes as an example of a divide and conquer that does not divide into two equal subproblems. However, the high constant factors in its $O(n)$ time bound make it slower than quickselect in practice, and slower even than sorting for inputs of moderate size.
- Hybrid algorithms such as introselect can be used to achieve the practical performance of quickselect with a fallback to medians of medians guaranteeing worst-case $O(n)$ time.

### Factories

The deterministic selection algorithms with the smallest known numbers of comparisons, for values of k that are far from 1 or n , are based on the concept of *factories*, introduced in 1976 by Arnold Schönhage, Mike Paterson, and Nick Pippenger. These are methods that build partial orders of certain specified types, on small subsets of input values, by using comparisons to combine smaller partial orders. As a very simple example, one type of factory can take as input a sequence of single-element partial orders, compare pairs of elements from these orders, and produce as output a sequence of two-element totally ordered sets. The elements used as the inputs to this factory could either be input values that have not been compared with anything yet, or "waste" values produced by other factories. The goal of a factory-based algorithm is to combine together different factories, with the outputs of some factories going to the inputs of others, in order to eventually obtain a partial order in which one element (the k th smallest) is larger than some $k-1$ other elements and smaller than another $n-k$ others. A careful design of these factories leads to an algorithm that, when applied to median-finding, uses at most $2.942n$ comparisons. For other values of k , the number of comparisons is smaller.

### Parallel algorithms

Parallel algorithms for selection have been studied since 1975, when Leslie Valiant introduced the parallel comparison tree model for analyzing these algorithms, and proved that in this model selection using a linear number of comparisons requires $\Omega (\log \log n)$ parallel steps, even for selecting the minimum or maximum. Researchers later found parallel algorithms for selection in $O(\log \log n)$ steps, matching this bound. In a randomized parallel comparison tree model it is possible to perform selection in a bounded number of steps and a linear number of comparisons. On the more realistic parallel RAM model of computing, with exclusive read exclusive write memory access, selection can be performed in time $O(\log n)$ with $O(n/\log n)$ processors, which is optimal both in time and in the number of processors. With concurrent memory access, slightly faster parallel time is possible in general, and the $\log n$ term in the time bound can be replaced by $\log k$ .

### Sublinear data structures

When data is already organized into a data structure, it may be possible to perform selection in an amount of time that is sublinear in the number of values. As a simple case of this, for data already sorted into an array, selecting the k th element may be performed by a single array lookup, in constant time. For values organized into a two-dimensional array of size $m\times n$ , with sorted rows and columns, selection may be performed in time $O{\bigl (}m\log(2n/m){\bigr )}$ , or faster when k is small relative to the array dimensions. For a collection of m one-dimensional sorted arrays, with $k_{i}$ items less than the selected item in the i th array, the time is ${\textstyle O{\bigl (}m+\sum _{i=1}^{m}\log(k_{i}+1){\bigr )}}$ .

Selection from data in a binary heap takes time $O(k)$ . This is independent of the size n of the heap, and faster than the $O(k\log n)$ time bound that would be obtained from best-first search. This same method can be applied more generally to data organized as any kind of heap-ordered tree (a tree in which each node stores one value in which the parent of each non-root node has a smaller value than its child). This method of performing selection in a heap has been applied to problems of listing multiple solutions to combinatorial optimization problems, such as finding the k shortest paths in a weighted graph, by defining a state space of solutions in the form of an implicitly defined heap-ordered tree, and then applying this selection algorithm to this tree. In the other direction, linear time selection algorithms have been used as a subroutine in a priority queue data structure related to the heap, improving the time for extracting its k th item from $O(\log n)$ to $O(\log ^{*}n+\log k)$ ; here $\log ^{*}n$ is the iterated logarithm.

For a collection of data values undergoing dynamic insertions and deletions, the order statistic tree augments a self-balancing binary search tree structure with a constant amount of additional information per tree node, allowing insertions, deletions, and selection queries that ask for the k th element in the current set to all be performed in $O(\log n)$ time per operation. Going beyond the comparison model of computation, faster times per operation are possible for values that are small integers, on which binary arithmetic operations are allowed. It is not possible for a streaming algorithm with memory sublinear in both n and k to solve selection queries exactly for dynamic data, but the count–min sketch can be used to solve selection queries approximately, by finding a value whose position in the ordering of the elements (if it were added to them) would be within $\varepsilon n$ steps of k , for a sketch whose size is within logarithmic factors of $1/\varepsilon$ .

## Lower bounds

The $O(n)$ running time of the selection algorithms described above is necessary, because a selection algorithm that can handle inputs in an arbitrary order must take that much time to look at all of its inputs. If any one of its input values is not compared, that one value could be the one that should have been selected, and the algorithm can be made to produce an incorrect answer. Beyond this simple argument, there has been a significant amount of research on the exact number of comparisons needed for selection, both in the randomized and deterministic cases.

Selecting the minimum of n values requires $n-1$ comparisons, because the $n-1$ values that are not selected must each have been determined to be non-minimal, by being the largest in some comparison, and no two of these values can be largest in the same comparison. The same argument applies symmetrically to selecting the maximum.

The next simplest case is selecting the second-smallest. After several incorrect attempts, the first tight lower bound on this case was published in 1964 by Soviet mathematician Sergey Kislitsyn. It can be shown by observing that selecting the second-smallest also requires distinguishing the smallest value from the rest, and by considering the number p of comparisons involving the smallest value that an algorithm for this problem makes. Each of the p items that were compared to the smallest value is a candidate for second-smallest, and $p-1$ of these values must be found larger than another value in a second comparison in order to rule them out as second-smallest. With $n-1$ values being the larger in at least one comparison, and $p-1$ values being the larger in at least two comparisons, there are a total of at least $n+p-2$ comparisons. An adversary argument, in which the outcome of each comparison is chosen in order to maximize p (subject to consistency with at least one possible ordering) rather than by the numerical values of the given items, shows that it is possible to force p to be at least $\log _{2}n$ . Therefore, the worst-case number of comparisons needed to select the second smallest is $n+\lceil \log _{2}n\rceil -2$ , the same number that would be obtained by holding a single-elimination tournament with a run-off tournament among the values that lost to the smallest value. However, the expected number of comparisons of a randomized selection algorithm can be better than this bound; for instance, selecting the second-smallest of six elements requires seven comparisons in the worst case, but may be done by a randomized algorithm with an expected number of 6.5 comparisons.

More generally, selecting the k th element out of n requires at least $n+\min(k,n-k)-O(1)$ comparisons, in the average case, matching the number of comparisons of the Floyd–Rivest algorithm up to its $o(n)$ term. The argument is made directly for deterministic algorithms, with a number of comparisons that is averaged over all possible permutations of the input values. By Yao's principle, it also applies to the expected number of comparisons for a randomized algorithm on its worst-case input.

For deterministic algorithms, it has been shown that selecting the k th element requires ${\bigl (}1+H(k/n){\bigr )}n+\Omega ({\sqrt {n}})$ comparisons, where $H(x)=x\log _{2}{\frac {1}{x}}+(1-x)\log _{2}{\frac {1}{1-x}}$ is the binary entropy function. The special case of median-finding has a slightly larger lower bound on the number of comparisons, at least $(2+\varepsilon )n$ , for $\varepsilon \approx 2^{-80}$ .

## Exact numbers of comparisons

Knuth supplies the following triangle of numbers summarizing pairs of n and k for which the exact number of comparisons needed by an optimal selection algorithm is known. The n th row of the triangle (starting with $n=1$ in the top row) gives the numbers of comparisons for inputs of n values, and the k th number within each row gives the number of comparisons needed to select the k th smallest value from an input of that size. The rows are symmetric because selecting the k th smallest requires exactly the same number of comparisons, in the worst case, as selecting the k th largest.

0

1

1

2

3

2

3

4

4

3

4

6

6

6

4

5

7

8

8

7

5

6

8

10

10

10

8

6

7

9

11

12

12

11

9

7

8

11

12

14

14

14

12

11

8

9

12

14

15

16

16

15

14

12

9

Most, but not all, of the entries on the left half of each row can be found using the formula $n-k+(k-1){\bigl \lceil }\log _{2}(n+2-k){\bigr \rceil }.$ This describes the number of comparisons made by a method of Abdollah Hadian and Milton Sobel, related to heapselect, that finds the smallest value using a single-elimination tournament and then repeatedly uses a smaller tournament among the values eliminated by the eventual tournament winners to find the next successive values until reaching the k th smallest. Some of the larger entries were proven to be optimal using a computer search.

## Language support

Very few languages have built-in support for general selection, although many provide facilities for finding the smallest or largest element of a list. Notable exceptions are the standard libraries of C++ and Rust. The Standard Template Library of C++ provides a templated `nth_element` method with a guarantee of expected linear time. Rust's standard library provides multiple variants of the `select_nth_unstable` member function for the `slice` data type. These variants all have guaranteed linear running time for all inputs.

Python's standard library includes `heapq.nsmallest` and `heapq.nlargest` functions for returning the smallest or largest elements from a collection, in sorted order. The implementation maintains a binary heap, limited to holding k elements, and initialized to the first k elements in the collection. Then, each subsequent item of the collection may replace the largest or smallest element in the heap if it is smaller or larger than this element. The algorithm's memory usage is superior to heapselect (the former only holds k elements in memory at a time while the latter requires manipulating the entire dataset into memory). Running time depends on data ordering. The best case is $O((n-k)+k\log k)$ for already sorted data. The worst-case is $O(n\log k)$ for reverse sorted data. In average cases, there are likely to be few heap updates and most input elements are processed with only a single comparison. For example, extracting the 100 largest or smallest values out of 10,000,000 random inputs makes 10,009,401 comparisons on average.

Since 2017, Matlab has included `maxk()` and `mink()` functions, which return the maximal (minimal) k values in a vector as well as their indices. The Matlab documentation does not specify which algorithm these functions use or what their running time is.

## History

Quickselect was presented without analysis by Tony Hoare in 1965, and first analyzed in a 1971 technical report by Donald Knuth. The first known linear time deterministic selection algorithm is the median of medians method, published in 1973 by Manuel Blum, Robert W. Floyd, Vaughan Pratt, Ron Rivest, and Robert Tarjan. They trace the formulation of the selection problem to work of Charles L. Dodgson (better known as Lewis Carroll) who in 1883 pointed out that the usual design of single-elimination sports tournaments does not guarantee that the second-best player wins second place, and to work of Hugo Steinhaus circa 1930, who followed up this same line of thought by asking for a tournament design that can make this guarantee, with a minimum number of games played (that is, comparisons).
