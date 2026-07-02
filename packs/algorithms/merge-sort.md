---
title: "Merge sort"
source: https://en.wikipedia.org/wiki/Merge_sort
domain: algorithms
license: CC-BY-SA-4.0
tags: algorithm, sorting, complexity, big-o, dynamic programming
fetched: 2026-07-02
---

# Merge sort

**Merge sort** (also commonly spelled as **mergesort** or **merge-sort**) is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations of merge sort are stable, which means that the relative order of equal elements is the same between the input and output. Merge sort is a divide-and-conquer algorithm that was invented by John von Neumann in 1945. A detailed description and analysis of bottom-up merge sort appeared in a report by Goldstine and von Neumann as early as 1948.

## Algorithm

Conceptually, a merge sort works as follows:

1. Divide the unsorted list into *n* sub-lists, each containing one element (a list of one element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

Merge sort is efficient because merging and sorting two sublists can be performed in linear time, provided that the sublists are already sorted.

### Top-down implementation

Example C-like code using indices for top-down merge sort algorithm that recursively splits the list into sublists (called *runs* in this example) until sublist size is 1, then merges those sublists to produce a sorted list. The copy back step is avoided with alternating the direction of the merge with each level of recursion (except for an initial one-time copy, that can be avoided too).

As a simple example, consider an array with two elements. The elements are copied to `b`, then merged back to `a`. If there are four elements, when the bottom of the recursion level is reached, single element runs from `a` are merged to `b`, and then at the next higher level of recursion, those two-element runs are merged to `a`. This pattern continues with each level of recursion.

```mw
// Copy a section of the array a into array b (from begin to end - 1)
void copyArray(int[] a, int begin, int end, int[] b) {
    for (int k = begin; k < end; ++k) {
        b[k] = a[k];
    }
}

// Merge two sorted halves (from a) into a single sorted run (into b)
void topDownMerge(int[] a, int begin, int middle, int end, int[] b) {
    int i = begin;
    int j = middle;

    // Merge the two sorted runs into b
    for (int k = begin; k < end; ++k) {
        if (i < middle && (j >= end || a[i] <= a[j])) {
            b[k] = a[i]; // Take element from the left run
            i++;
        } else {
            b[k] = a[j]; // Take element from the right run
            j++;
        }
    }
}

// Split the array a into two halves, sort both halves into b,
// and merge the sorted halves back into a
void topDownSplitMerge(int[] a, int begin, int end, int[] b) {
    if (end - begin <= 1) {
        return; // Base case: Run size is 1, so it's already sorted
    }

    int middle = (begin + end) / 2;  // Find the midpoint to split the array

    // Recursively sort the left and right halves into b
    topDownSplitMerge(b, begin, middle, a);
    topDownSplitMerge(b, middle, end, a);

    // Merge the sorted halves back into a
    topDownMerge(b, begin, middle, end, a);
}

void topDownMergeSort(int[] a, int[] b, int n) {
    // Copy the entire array a into b initially
    copyArray(a, 0, n, b);
    // Recursively split and merge the array b into a
    topDownSplitMerge(a, 0, n, b);
}
```

Sorting the entire array is accomplished by topDownMergeSort(a, b, a.length).

### Bottom-up implementation

Example C-like code using indices for bottom-up merge sort algorithm which treats the list as an array of *n* sublists (called *runs* in this example) of size 1, and iteratively merges sub-lists back and forth between two buffers:

```mw
// Copy array b into array a
void copyArray(int[] b, int[] a, int n) {
    for (int i = 0; i < n; i++) {
        a[i] = b[i];
    }
}

// Left run is a[left : right-1].
// Right run is a[right : end-1].
void bottomUpMerge(int[] a, int left, int right, int end, int[] b) {
    int i = left;
    int j = right;

    // While there are elements in the left or right runs...
    for (int k = left; k < end; ++k) {
        // If left run head exists and is <= existing right run head.
        if (i < right && (j >= end || a[i] <= a[j])) {
            b[k] = a[i];
            i = i + 1;
        } else {
            b[k] = a[j];
            j = j + 1;    
        }
    }
}

void bottomUpMergeSort(int[] a, int[] b, int n) {
    // Each 1-element run in a is already "sorted".
    // Make successively longer sorted runs of length 2, 4, 8, 16... until the whole array is sorted.
    for (int width = 1; width < n; width *= 2) {
        // Array a is full of runs of length width.
        for (int i = 0; i < n; i = i + 2 * width) {
            // Merge two runs: a[i:i+width-1] and a[i+width:i+2*width-1] to b[]
            // or copy a[i:n-1] to b[] (if (i+width >= n))
            bottomUpMerge(a, i, Math.min(i + width, n), Math.min(i + 2 * width, n), b);
        }
        // Now work array b is full of runs of length 2 * width.
        // Copy array b to array a for the next iteration.
        // A more efficient implementation would swap the roles of a and b.
        copyArray(b, a, n);
    }
}
```

### Top-down implementation using lists

Pseudocode for top-down merge sort algorithm which recursively divides the input list into smaller sublists until the sublists are trivially sorted, and then merges the sublists while returning up the call chain.

```
function merge_sort(list m) is
    // Base case. A list of zero or one elements is sorted, by definition.
    if length of m ≤ 1 then
        return m

    // Recursive case. First, divide the list into equal-sized sublists
    // consisting of the first half and second half of the list.
    // This assumes lists start at index 0.
    var left := empty list
    var right := empty list
    for each x with index i in m do
        if i < (length of m)/2 then
            add x to left
        else
            add x to right

    // Recursively sort both sublists.
    left := merge_sort(left)
    right := merge_sort(right)

    // Then merge the now-sorted sublists.
    return merge(left, right)
```

In this example, the merge function merges the left and right sublists.

```
function merge(left, right) is
    var result := empty list

    while left is not empty and right is not empty do
        if first(left) ≤ first(right) then
            append first(left) to result
            left := rest(left)
        else
            append first(right) to result
            right := rest(right)

    // Either left or right may have elements left; consume them.
    // (Only one of the following loops will actually be entered.)
    while left is not empty do
        append first(left) to result
        left := rest(left)
    while right is not empty do
        append first(right) to result
        right := rest(right)
    return result
```

### Bottom-up implementation using lists

Pseudocode for bottom-up merge sort algorithm which uses a small fixed size array of references to nodes, where `array[i]` is either a reference to a list of size 2*i* or *nil*. *node* is a reference or pointer to a node. The `merge()` function would be similar to the one shown in the top-down merge lists example, it merges two already sorted lists, and handles empty lists. In this case, `merge()` would use *node* for its input parameters and return value.

```
function merge_sort(node head) is
    // return if empty list
    if head = nil then
        return nil
    var node array[32]; initially all nil
    var node result
    var node next
    var int  i
    result := head
    // merge nodes into array
    while result ≠ nil do
        next := result.next;
        result.next := nil
        for (i = 0; (i < 32) && (array[i] ≠ nil); i += 1) do
            result := merge(array[i], result)
            array[i] := nil
        // do not go past end of array
        if i = 32 then
            i -= 1
        array[i] := result
        result := next
    // merge array into single list
    result := nil
    for (i = 0; i < 32; i += 1) do
        result := merge(array[i], result)
    return result
```

### Top-down implementation in a declarative style

Haskell-like pseudocode, showing how merge sort can be implemented in such a language using constructs and ideas from functional programming.

```mw
mergeSort :: Ord a => [a] -> [a]
mergeSort []  = []
mergeSort [x] = [x]
mergeSort xs  = merge (mergeSort l, mergeSort r)
  where (l, r) = splitAt (length xs `div` 2) xs

merge :: Ord a => ([a], [a]) -> [a]
merge ([], xs) = xs
merge (xs, []) = xs
merge (x:xs, y:ys) | x <= y    = x : merge(xs, y:ys)
                   | otherwise = y : merge(x:xs, ys)
```

## Analysis

In sorting *n* objects, merge sort has an average and worst-case performance of O(*n* log *n*) comparisons. If the running time (number of comparisons) of merge sort for a list of length *n* is *T*(*n*), then the recurrence relation *T*(*n*) = 2*T*(*n*/2) + *n* follows from the definition of the algorithm (apply the algorithm to two lists of half the size of the original list, and add the *n* steps taken to merge the resulting two lists). The closed form follows from the master theorem for divide-and-conquer recurrences.

The number of comparisons made by merge sort in the worst case is given by the sorting numbers. These numbers are equal to or slightly smaller than (*n* ⌈lg *n*⌉ − 2⌈lg *n*⌉ + 1), which is between (*n* lg *n* − *n* + 1) and (*n* lg *n* + *n* + O(lg *n*)). Merge sort's best case takes about half as many iterations as its worst case.

For large *n* and a randomly ordered input list, merge sort's expected (average) number of comparisons approaches *α*·*n* fewer than the worst case, where $\alpha =-1+\sum _{k=0}^{\infty }{\frac {1}{2^{k}+1}}\approx 0.2645.$

In the *worst* case, merge sort uses approximately 39% fewer comparisons than quicksort does in its *average* case, and in terms of moves, merge sort's worst case complexity is O(*n* log *n*) - the same complexity as quicksort's best case.

Merge sort is more efficient than quicksort for some types of lists if the data to be sorted can only be efficiently accessed sequentially, and is thus popular in languages such as Lisp, where sequentially accessed data structures are very common. Unlike some (efficient) implementations of quicksort, merge sort is a stable sort.

Merge sort's most common implementation does not sort in place; therefore, the memory size of the input must be allocated for the sorted output to be stored in (see below for variations that need only *n*/2 extra spaces).

## Natural merge sort

A natural merge sort is similar to a bottom-up merge sort except that any naturally occurring runs (sorted sequences) in the input are exploited. Both monotonic and bitonic (alternating up/down) runs may be exploited, with lists (or equivalently tapes or files) being convenient data structures (used as FIFO queues or LIFO stacks). In the bottom-up merge sort, the starting point assumes each run is one item long. In practice, random input data will have many short runs that just happen to be sorted. In the typical case, the natural merge sort may not need as many passes because there are fewer runs to merge. In the best case, the input is already sorted (i.e., is one run), so the natural merge sort need only make one pass through the data. In many practical cases, long natural runs are present, and for that reason natural merge sort is exploited as the key component of Timsort. Example:

```
Start       :  3  4  2  1  7  5  8  9  0  6
Select runs : (3  4)(2)(1  7)(5  8  9)(0  6)
Merge       : (2  3  4)(1  5  7  8  9)(0  6)
Merge       : (1  2  3  4  5  7  8  9)(0  6)
Merge       : (0  1  2  3  4  5  6  7  8  9)
```

Formally, the natural merge sort is said to be Runs-optimal, where ${\mathtt {Runs}}(L)$ is the number of runs in L , minus one.

Tournament replacement selection sorts are used to gather the initial runs for external sorting algorithms.

## Ping-pong merge sort

Instead of merging two blocks at a time, a ping-pong merge merges four blocks at a time. The four sorted blocks are merged simultaneously to auxiliary space into two sorted blocks, then the two sorted blocks are merged back to main memory. Doing so omits the copy operation and reduces the total number of moves by half. An early public domain implementation of a four-at-once merge was by WikiSort in 2014, the method was later that year described as an optimization for patience sorting and named a ping-pong merge. Quadsort implemented the method in 2020 and named it a quad merge.

## In-place merge sort

One drawback of merge sort, when implemented on arrays, is its *O*(*n*) working memory requirement. Several methods to reduce memory or make merge sort fully in-place have been suggested:

- Kronrod (1969) suggested an alternative version of merge sort that uses constant additional space.
- Katajainen *et al.* present an algorithm that requires a constant amount of working memory: enough storage space to hold one element of the input array, and additional space to hold *O*(1) pointers into the input array. They achieve an *O*(*n* log *n*) time bound with small constants, but their algorithm is not stable.
- Several attempts have been made at producing an *in-place merge* algorithm that can be combined with a standard (top-down or bottom-up) merge sort to produce an in-place merge sort. In this case, the notion of "in-place" can be relaxed to mean "taking logarithmic stack space", because standard merge sort requires that amount of space for its own stack usage. It was shown by Geffert *et al.* that in-place, stable merging is possible in *O*(*n* log *n*) time using a constant amount of scratch space, but their algorithm is complicated and has high constant factors: merging arrays of length n and m can take 5*n* + 12*m* + *o*(*m*) moves. This high constant factor and complicated in-place algorithm was made simpler and easier to understand. Bing-Chao Huang and Michael A. Langston presented a straightforward linear time algorithm *practical in-place merge* to merge a sorted list using fixed amount of additional space. They both have used the work of Kronrod and others. It merges in linear time and constant extra space. The algorithm takes little more average time than standard merge sort algorithms, free to exploit *O*(*n*) temporary extra memory cells, by less than a factor of two. Though the algorithm is much faster in a practical way, it is unstable for some lists. But using similar concepts, they have been able to solve this problem. Other in-place algorithms include SymMerge, which takes *O*((*n* + *m*) log (*n* + *m*)) time in total and is stable. Plugging such an algorithm into merge sort increases its complexity to the non-linearithmic, but still quasilinear, *O*(*n* (log *n*)2).
- Many applications of external sorting use a form of merge sorting where the input gets split up to a higher number of sublists, ideally to a number for which merging them still makes the currently processed set of pages fit into main memory.
- A modern stable, linear, and in-place merge variant is block merge sort, which creates a section of unique values to use as swap space.
- The space overhead can be reduced to *O*(√*n*) by using binary searches and rotations. This method is employed by the C++ STL library and quadsort.
- An alternative to reduce the copying into multiple lists is to associate a new field of information with each key (the elements in *m* are called keys). This field will be used to link the keys and any associated information together in a sorted list (a key and its related information is called a record). Then the merging of the sorted lists proceeds by changing the link values; no records need to be moved at all. A field which contains only a link will generally be smaller than an entire record so less space will also be used. This is a standard sorting technique, not restricted to merge sort.
- A simple way to reduce the space overhead to *n*/2 is to maintain *left* and *right* as a combined structure, copy only the *left* part of *m* into temporary space, and to direct the *merge* routine to place the merged output into *m*. With this version it is better to allocate the temporary space outside the *merge* routine, so that only one allocation is needed. The excessive copying mentioned previously is also mitigated, since the last pair of lines before the *return result* statement (function *merge*in the pseudo code above) become superfluous.

## Use with tape drives

An external merge sort is practical to run using disk or tape drives when the data to be sorted is too large to fit into memory. External sorting explains how merge sort is implemented with disk drives. A typical tape drive sort uses four tape drives. All I/O is sequential (except for rewinds at the end of each pass). A minimal implementation can get by with just two record buffers and a few program variables.

Naming the four tape drives as A, B, C, D, with the original data on A, and using only two record buffers, the algorithm is similar to the bottom-up implementation, using pairs of tape drives instead of arrays in memory. The basic algorithm can be described as follows:

1. Merge pairs of records from A; writing two-record sublists alternately to C and D.
2. Merge two-record sublists from C and D into four-record sublists; writing these alternately to A and B.
3. Merge four-record sublists from A and B into eight-record sublists; writing these alternately to C and D
4. Repeat until you have one list containing all the data, sorted—in log2(*n*) passes.

Instead of starting with very short runs, usually a hybrid algorithm is used, where the initial pass will read many records into memory, do an internal sort to create a long run, and then distribute those long runs onto the output set. The step avoids many early passes. For example, an internal sort of 1024 records will save nine passes. The internal sort is often large because it has such a benefit. In fact, there are techniques that can make the initial runs longer than the available internal memory. One of them, the Knuth's 'snowplow' (based on a binary min-heap), generates runs twice as long (on average) as a size of memory used.

With some overhead, the above algorithm can be modified to use three tapes. *O*(*n* log *n*) running time can also be achieved using two queues, or a stack and a queue, or three stacks. In the other direction, using *k* > two tapes (and *O*(*k*) items in memory), we can reduce the number of tape operations in *O*(log *k*) times by using a k/2-way merge.

A more sophisticated merge sort that optimizes tape (and disk) drive usage is the polyphase merge sort.

## Optimizing merge sort

On modern computers, locality of reference can be of paramount importance in software optimization, because multilevel memory hierarchies are used. Cache-aware versions of the merge sort algorithm, whose operations have been specifically chosen to minimize the movement of pages in and out of a machine's memory cache, have been proposed. For example, the **tiled merge sort** algorithm stops partitioning subarrays when subarrays of size S are reached, where S is the number of data items fitting into a CPU's cache. Each of these subarrays is sorted with an in-place sorting algorithm such as insertion sort, to discourage memory swaps, and normal merge sort is then completed in the standard recursive fashion. This algorithm has demonstrated better performance on machines that benefit from cache optimization. (LaMarca & Ladner 1997)

## Parallel merge sort

Merge sort parallelizes well due to the use of the divide-and-conquer method. Several different parallel variants of the algorithm have been developed over the years. Some parallel merge sort algorithms are strongly related to the sequential top-down merge algorithm while others have a different general structure and use the K-way merge method.

### Merge sort with parallel recursion

The sequential merge sort procedure can be described in two phases, the divide phase and the merge phase. The first consists of many recursive calls that repeatedly perform the same division process until the subsequences are trivially sorted (containing one or no element). An intuitive approach is the parallelization of those recursive calls. Following pseudocode describes the merge sort with parallel recursion using the fork and join keywords:

```
// Sort elements lo through hi (exclusive) of array A.
algorithm mergesort(A, lo, hi) is
    if lo+1 < hi then  // Two or more elements.
        mid := ⌊(lo + hi) / 2⌋
        fork mergesort(A, lo, mid)
        mergesort(A, mid, hi)
        join
        merge(A, lo, mid, hi)
```

This algorithm is the trivial modification of the sequential version and does not parallelize well. Therefore, its speedup is not very impressive. It has a span of $\Theta (n)$ , which is only an improvement of $\Theta (\log n)$ compared to the sequential version (see Introduction to Algorithms). This is mainly due to the sequential merge method, as it is the bottleneck of the parallel executions.

### Merge sort with parallel merging

Better parallelism can be achieved by using a parallel merge algorithm. Cormen et al. present a binary variant that merges two sorted sub-sequences into one sorted output sequence.

In one of the sequences (the longer one if unequal length), the element of the middle index is selected. Its position in the other sequence is determined in such a way that this sequence would remain sorted if this element were inserted at this position. Thus, one knows how many other elements from both sequences are smaller and the position of the selected element in the output sequence can be calculated. For the partial sequences of the smaller and larger elements created in this way, the merge algorithm is again executed in parallel until the base case of the recursion is reached.

The following pseudocode shows the modified parallel merge sort method using the parallel merge algorithm (adopted from Cormen et al.).

```
/**
 * A: Input array
 * B: Output array
 * lo: lower bound
 * hi: upper bound
 * off: offset
 */
algorithm parallelMergesort(A, lo, hi, B, off) is
    len := hi - lo + 1
    if len == 1 then
        B[off] := A[lo]
    else let T[1..len] be a new array
        mid := ⌊(lo + hi) / 2⌋ 
        mid' := mid - lo + 1
        fork parallelMergesort(A, lo, mid, T, 1)
        parallelMergesort(A, mid + 1, hi, T, mid' + 1) 
        join 
        parallelMerge(T, 1, mid', mid' + 1, len, B, off)
```

In order to analyze a recurrence relation for the worst case span, the recursive calls of parallelMergesort have to be incorporated only once due to their parallel execution, obtaining

$T_{\infty }^{\text{sort}}(n)=T_{\infty }^{\text{sort}}\left({\frac {n}{2}}\right)+T_{\infty }^{\text{merge}}(n)=T_{\infty }^{\text{sort}}\left({\frac {n}{2}}\right)+\Theta \left(\log(n)^{2}\right).$

For detailed information about the complexity of the parallel merge procedure, see Merge algorithm.

The solution of this recurrence is given by

$T_{\infty }^{\text{sort}}=\Theta \left(\log(n)^{3}\right).$

This parallel merge algorithm reaches a parallelism of ${\textstyle \Theta \left({\frac {n}{(\log n)^{2}}}\right)}$ , which is much higher than the parallelism of the previous algorithm. Such a sort can perform well in practice when combined with a fast stable sequential sort, such as insertion sort, and a fast sequential merge as a base case for merging small arrays.

### Parallel multiway merge sort

It seems arbitrary to restrict the merge sort algorithms to a binary merge method, since there are usually p > 2 processors available. A better approach may be to use a K-way merge method, a generalization of binary merge, in which k sorted sequences are merged. This merge variant is well suited to describe a sorting algorithm on a PRAM.

#### Basic idea

Given an unsorted sequence of n elements, the goal is to sort the sequence with p available processors. These elements are distributed equally among all processors and sorted locally using a sequential Sorting algorithm. Hence, the sequence consists of sorted sequences $S_{1},...,S_{p}$ of length ${\textstyle \lceil {\frac {n}{p}}\rceil }$ . For simplification let n be a multiple of p , so that ${\textstyle \left\vert S_{i}\right\vert ={\frac {n}{p}}}$ for $i=1,...,p$ .

These sequences will be used to perform a multisequence selection/splitter selection. For $j=1,...,p$ , the algorithm determines splitter elements $v_{j}$ with global rank ${\textstyle k=j{\frac {n}{p}}}$ . Then the corresponding positions of $v_{1},...,v_{p}$ in each sequence $S_{i}$ are determined with binary search and thus the $S_{i}$ are further partitioned into p subsequences $S_{i,1},...,S_{i,p}$ with ${\textstyle S_{i,j}:=\{x\in S_{i}|rank(v_{j-1})<rank(x)\leq rank(v_{j})\}}$ .

Furthermore, the elements of $S_{1,i},...,S_{p,i}$ are assigned to processor i , means all elements between rank ${\textstyle (i-1){\frac {n}{p}}}$ and rank ${\textstyle i{\frac {n}{p}}}$ , which are distributed over all $S_{i}$ . Thus, each processor receives a sequence of sorted sequences. The fact that the rank k of the splitter elements $v_{i}$ was chosen globally, provides two important properties: On the one hand, k was chosen so that each processor can still operate on ${\textstyle n/p}$ elements after assignment. The algorithm is perfectly load-balanced. On the other hand, all elements on processor i are less than or equal to all elements on processor $i+1$ . Hence, each processor performs the *p*-way merge locally and thus obtains a sorted sequence from its sub-sequences. Because of the second property, no further *p*-way-merge has to be performed, the results only have to be put together in the order of the processor number.

#### Multi-sequence selection

In its simplest form, given p sorted sequences $S_{1},...,S_{p}$ distributed evenly on p processors and a rank k , the task is to find an element x with a global rank k in the union of the sequences. Hence, this can be used to divide each $S_{i}$ in two parts at a splitter index $l_{i}$ , where the lower part contains only elements which are smaller than x , while the elements bigger than x are located in the upper part.

The presented sequential algorithm returns the indices of the splits in each sequence, e.g. the indices $l_{i}$ in sequences $S_{i}$ such that $S_{i}[l_{i}]$ has a global rank less than k and $\mathrm {rank} \left(S_{i}[l_{i}+1]\right)\geq k$ .

```
algorithm msSelect(S : Array of sorted Sequences [S_1,..,S_p], k : int) is
    for i = 1 to p do 
	(l_i, r_i) = (0, |S_i|-1)
	
    while there exists i: l_i < r_i do
	// pick Pivot Element in S_j[l_j], .., S_j[r_j], chose random j uniformly
	v := pickPivot(S, l, r)
	for i = 1 to p do 
	    m_i = binarySearch(v, S_i[l_i, r_i]) // sequentially
	if m_1 + ... + m_p >= k then // m_1+ ... + m_p is the global rank of v
	    r := m  // vector assignment
	else
	    l := m 
	
    return l
```

For the complexity analysis the PRAM model is chosen. If the data is evenly distributed over all p , the p-fold execution of the *binarySearch* method has a running time of ${\mathcal {O}}\left(p\log \left(n/p\right)\right)$ . The expected recursion depth is ${\mathcal {O}}\left(\log \left(\textstyle \sum _{i}|S_{i}|\right)\right)={\mathcal {O}}(\log(n))$ as in the ordinary Quickselect. Thus the overall expected running time is ${\mathcal {O}}\left(p\log(n/p)\log(n)\right)$ .

Applied on the parallel multiway merge sort, this algorithm has to be invoked in parallel such that all splitter elements of rank ${\textstyle i{\frac {n}{p}}}$ for $i=1,..,p$ are found simultaneously. These splitter elements can then be used to partition each sequence in p parts, with the same total running time of ${\mathcal {O}}\left(p\,\log(n/p)\log(n)\right)$ .

#### Pseudocode

Below, the complete pseudocode of the parallel multiway merge sort algorithm is given. We assume that there is a barrier synchronization before and after the multisequence selection such that every processor can determine the splitting elements and the sequence partition properly.

```
/**
 * d: Unsorted Array of Elements
 * n: Number of Elements
 * p: Number of Processors
 * return Sorted Array
 */
algorithm parallelMultiwayMergesort(d : Array, n : int, p : int) is
    o := new Array[0, n]                         // the output array
    for i = 1 to p do in parallel                // each processor in parallel
        S_i := d[(i-1) * n/p, i * n/p] 	         // Sequence of length n/p
	sort(S_i)                                // sort locally
        synch
	v_i := msSelect([S_1,...,S_p], i * n/p)          // element with global rank i * n/p
        synch
	(S_i,1, ..., S_i,p) := sequence_partitioning(si, v_1, ..., v_p) // split s_i into subsequences
	    
	o[(i-1) * n/p, i * n/p] := kWayMerge(s_1,i, ..., s_p,i)  // merge and assign to output array
	
    return o
```

#### Analysis

Firstly, each processor sorts the assigned $n/p$ elements locally using a sorting algorithm with complexity ${\mathcal {O}}\left(n/p\;\log(n/p)\right)$ . After that, the splitter elements have to be calculated in time ${\mathcal {O}}\left(p\,\log(n/p)\log(n)\right)$ . Finally, each group of p splits have to be merged in parallel by each processor with a running time of ${\mathcal {O}}(\log(p)\;n/p)$ using a sequential p-way merge algorithm. Thus, the overall running time is given by

${\mathcal {O}}\left({\frac {n}{p}}\log \left({\frac {n}{p}}\right)+p\log \left({\frac {n}{p}}\right)\log(n)+{\frac {n}{p}}\log(p)\right)$ .

#### Practical adaption and application

The multiway merge sort algorithm is very scalable through its high parallelization capability, which allows the use of many processors. This makes the algorithm a viable candidate for sorting large amounts of data, such as those processed in computer clusters. Also, since in such systems memory is usually not a limiting resource, the disadvantage of space complexity of merge sort is negligible. However, other factors become important in such systems, which are not taken into account when modelling on a PRAM. Here, the following aspects need to be considered: Memory hierarchy, when the data does not fit into the processors cache, or the communication overhead of exchanging data between processors, which could become a bottleneck when the data can no longer be accessed via the shared memory.

Sanders et al. have presented in their paper a bulk synchronous parallel algorithm for multilevel multiway mergesort, which divides p processors into r groups of size $p'$ . All processors sort locally first. Unlike single level multiway mergesort, these sequences are then partitioned into r parts and assigned to the appropriate processor groups. These steps are repeated recursively in those groups. This reduces communication and especially avoids problems with many small messages. The hierarchical structure of the underlying real network can be used to define the processor groups (e.g. racks, clusters,...).

### Further variants

Merge sort was one of the first sorting algorithms where optimal speed up was achieved, with Richard Cole using a clever subsampling algorithm to ensure *O*(1) merge. Other sophisticated parallel sorting algorithms can achieve the same or better time bounds with a lower constant. For example, in 1991 David Powers described a parallelized quicksort (and a related radix sort) that can operate in *O*(log *n*) time on a CRCW parallel random-access machine (PRAM) with *n* processors by performing partitioning implicitly. Powers further shows that a pipelined version of Batcher's Bitonic Mergesort at *O*((log *n*)2) time on a butterfly sorting network is in practice actually faster than his *O*(log *n*) sorts on a PRAM, and he provides detailed discussion of the hidden overheads in comparison, radix and parallel sorting.

## Comparison with other sort algorithms

Although heapsort has the same time bounds as merge sort, it requires only Θ(1) auxiliary space instead of merge sort's Θ(*n*). On typical modern architectures, efficient quicksort implementations generally outperform merge sort for sorting RAM-based arrays. Quicksorts are preferred when the data size to be sorted is lesser, since the space complexity for quicksort is O(log *n*), it helps in utilizing cache locality better than merge sort (with space complexity O(n)). On the other hand, merge sort is a stable sort and is more efficient at handling slow-to-access sequential media. Merge sort is often the best choice for sorting a linked list: in this situation it is relatively easy to implement a merge sort in such a way that it requires only Θ(1) extra space, and the slow random-access performance of a linked list makes some other algorithms (such as quicksort) perform poorly, and others (such as heapsort) completely impossible.

As of Perl 5.8, merge sort is its default sorting algorithm (it was quicksort in previous versions of Perl). In Java, the Arrays.sort() methods use merge sort or a tuned quicksort depending on the datatypes and for implementation efficiency switch to insertion sort when fewer than seven array elements are being sorted. The Linux kernel uses merge sort for its linked lists.

Timsort, a tuned hybrid of merge sort and insertion sort is used in variety of software platforms and languages including the Java and Android platforms and is used by Python since version 2.3; since version 3.11, Timsort's merge policy was updated to Powersort.
