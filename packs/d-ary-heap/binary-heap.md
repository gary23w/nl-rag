---
title: "Binary heap"
source: https://en.wikipedia.org/wiki/Binary_heap
domain: d-ary-heap
license: CC-BY-SA-4.0
tags: d-ary heap, implicit heap, priority queue, radix heap
fetched: 2026-07-02
---

# Binary heap

A **binary heap** is a heap data structure that takes the form of a binary tree. Binary heaps are a common way of implementing priority queues. The binary heap was introduced by J. W. J. Williams in 1964 as a data structure for implementing heapsort.

A binary heap is defined as a binary tree with two additional constraints:

- Shape property: a binary heap is a *complete binary tree*; that is, all levels of the tree, except possibly the last one (deepest) are fully filled, and, if the last level of the tree is not complete, the nodes of that level are filled from left to right.
- Heap property: the key stored in each node is either greater than or equal to (≥) (or less than or equal to (≤)) the keys in the node's children, according to some total order.

Heaps where the parent key is greater than or equal to (≥) the child keys are called *max-heaps*; those where it is less than or equal to (≤) are called *min-heaps*. Efficient (that is, logarithmic time) algorithms are known for the two operations needed to implement a priority queue on a binary heap:

- Inserting an element;
- Removing the smallest or largest element from (respectively) a min-heap or max-heap.

Binary heaps are also commonly employed in the heapsort sorting algorithm, which is an in-place algorithm as binary heaps can be implemented as an implicit data structure, storing keys in an array and using their relative positions within that array to represent child–parent relationships.

## Heap operations

Both the insert and remove operations modify the heap to preserve the shape property first, by adding or removing from the end of the heap. Then the heap property is restored by traversing up or down the heap. Both operations take O(log *n*) time.

### Insert

To insert an element to a heap, we perform the following steps:

1. Add the element to the bottom level of the heap at the leftmost open space.
2. Compare the added element with its parent; if they are in the correct order, stop.
3. If not, swap the element with its parent and return to the previous step.

Steps 2 and 3, which restore the heap property by comparing and possibly swapping a node with its parent, are called *the up-heap* operation (also known as *bubble-up*, *percolate-up*, *sift-up*, *trickle-up*, *swim-up*, *heapify-up*, *cascade-up*, or *fix-up*).

The number of operations required depends only on the number of levels the new element must rise to satisfy the heap property. Thus, the insertion operation has a worst-case time complexity of O(log *n*). For a random heap, and for repeated insertions, the insertion operation has an average-case complexity of O(1).

The following animation depicts an example of binary heap insertion. It begins by inserting 15 into the heap at the left-most empty entry on the next available row. However, the heap property is violated since 15 > 8, so we need to swap the 15 and the 8. Even after this swap, the heap property is still violated since 15 > 11, so we need to swap again. The heap property is now satisfied, so the resulting binary tree is a valid max-heap. There is no need to check the left child after this final step: at the start, the max-heap was valid, meaning the root was already greater than its left child, so replacing the root with an even greater value will maintain the property that each node is greater than its children (11 > 5; if 15 > 11, and 11 > 5, then 15 > 5, because of the transitive relation).

### Extract

The procedure for deleting the root from the heap (effectively extracting the maximum element in a max-heap or the minimum element in a min-heap) while retaining the heap property is as follows:

1. Replace the root of the heap with the last element on the last level.
2. Compare the new root with its children; if they are in the correct order, stop.
3. If not, swap the element with one of its children and return to the previous step. (Swap with its smaller child in a min-heap and its larger child in a max-heap.)

Steps 2 and 3, which restore the heap property by comparing and possibly swapping a node with one of its children, are called the *down-heap* (also known as *bubble-down*, *percolate-down*, *sift-down*, *sink-down*, *trickle down*, *heapify-down*, *cascade-down*, *fix-down*, *extract-min* or *extract-max*, or simply *heapify*) operation.

So, if we have the same max-heap as before, we remove the 11 and replace it with the 4. Now the heap property is violated since 8 is greater than 4. In this case, swapping the two elements, 4 and 8, is enough to restore the heap property and we need not swap elements further.

The downward-moving node is swapped with the *larger* of its children in a max-heap (in a min-heap it would be swapped with its smaller child), until it satisfies the heap property in its new position. This functionality is achieved by the **Max-Heapify** function as defined below in pseudocode for an array-backed heap *A* of length *length*(*A*). *A* is indexed starting at 1.

```
// Perform a down-heap or heapify-down operation for a max-heap
// A: an array representing the heap, indexed starting at 1
// i: the index to start at when heapifying down
Max-Heapify(A, i):
    left ← 2×i
    right ← 2×i + 1
    largest ← i
    
    if left ≤ length(A) and A[left] > A[largest] then:
        largest ← left

    if right ≤ length(A) and A[right] > A[largest] then:
        largest ← right
    
    if largest ≠ i then:
        swap A[i] and A[largest]
        Max-Heapify(A, largest)
```

For the above algorithm to correctly re-heapify the array, no nodes besides the node at index *i* and its two direct children can violate the heap property. The down-heap operation (without the preceding swap) can also be used to modify the value of the root, even when an element is not being deleted.

In the worst case, the new root has to be swapped with its child on each level until it reaches the bottom level of the heap, meaning that the delete operation has a time complexity relative to the height of the tree, or O(log *n*).

### Insert then extract

Inserting an element then extracting from the heap can be done more efficiently than simply calling the insert and extract functions defined above, which would involve both an `upheap` and `downheap` operation. Instead, we can do just a `downheap` operation, as follows:

1. Compare whether the item we're pushing or the peeked top of the heap is greater (assuming a max heap)
2. If the root of the heap is greater:
  1. Replace the root with the new item
  2. Down-heapify starting from the root
3. Else, return the item we're pushing

Python provides such a function for insertion then extraction called "heappushpop", which is paraphrased below. The heap array is assumed to have its first element at index 1.

```
// Push a new item to a (max) heap and then extract the root of the resulting heap. 
// heap: an array representing the heap, indexed at 1
// item: an element to insert
// Returns the greater of the two between item and the root of heap.
Push-Pop(heap: List<T>, item: T) -> T:
    if heap is not empty and heap[1] > item then:  // < if min heap
        swap heap[1] and item
        _downheap(heap starting from index 1)
    return item
```

A similar function can be defined for popping and then inserting, which in Python is called "heapreplace":

```
// Extract the root of the heap, and push a new item 
// heap: an array representing the heap, indexed at 1
// item: an element to insert
// Returns the current root of heap
Replace(heap: List<T>, item: T) -> T:
    swap heap[1] and item
    _downheap(heap starting from index 1)
    return item
```

Finding an arbitrary element takes O(n) time.

This can be easily proved by considering that the heap is not sorted so we need to look through the whole tree to find the target element.

### Delete

Deleting an arbitrary element can be done as follows:

1. Find the index i of the element we want to delete
2. Swap this element with the last element. Remove the last element after the swap.
3. Down-heapify or up-heapify to restore the heap property. In a max-heap (min-heap), up-heapify is only required when the new key of element i is greater (smaller) than the previous one because only the heap-property of the parent element might be violated. Assuming that the heap-property was valid between element i and its children before the element swap, it can't be violated by a now larger (smaller) key value. When the new key is less (greater) than the previous one then only a down-heapify is required because the heap-property might only be violated in the child elements.

### Decrease or increase key

The decrease key operation replaces the value of a node with a given value with a lower value, and the increase key operation does the same but with a higher value. This involves finding the node with the given value, changing the value, and then down-heapifying or up-heapifying to restore the heap property.

Decrease key can be done as follows:

1. Find the index of the element we want to modify
2. Decrease the value of the node
3. Down-heapify (assuming a max heap) to restore the heap property

Increase key can be done as follows:

1. Find the index of the element we want to modify
2. Increase the value of the node
3. Up-heapify (assuming a max heap) to restore the heap property

## Building a heap

Building a heap from an array of n input elements can be done by starting with an empty heap, then successively inserting each element. This approach, called Williams' method after the inventor of binary heaps, is easily seen to run in *O*(*n* log *n*) time: it performs n insertions at *O*(log *n*) cost each.

However, Williams' method is suboptimal. A faster method (due to Floyd) starts by arbitrarily putting the elements on a binary tree, respecting the shape property (the tree could be represented by an array, see below). Then starting from the lowest level and moving upwards, sift the root of each subtree downward as in the deletion algorithm until the heap property is restored. More specifically if all the subtrees starting at some height h have already been "heapified" (the bottommost level corresponding to $h=0$ ), the trees at height $h+1$ can be heapified by sending their root down along the path of maximum valued children when building a max-heap, or minimum valued children when building a min-heap. This process takes $O(h)$ operations (swaps) per node. In this method most of the heapification takes place in the lower levels. Since the height of the heap is $\lfloor \log n\rfloor$ , the number of nodes at height h is $\leq {\frac {2^{\lfloor \log n\rfloor }}{2^{h}}}\leq {\frac {n}{2^{h}}}$ . Therefore, the cost of heapifying all subtrees is:

${\begin{aligned}\sum _{h=0}^{\lfloor \log n\rfloor }{\frac {n}{2^{h}}}O(h)&=O\left(n\sum _{h=0}^{\lfloor \log n\rfloor }{\frac {h}{2^{h}}}\right)\\&=O\left(n\sum _{h=0}^{\infty }{\frac {h}{2^{h}}}\right)\\&=O(n)\end{aligned}}$

This uses the fact that the given infinite series ${\textstyle \sum _{i=0}^{\infty }i/2^{i}}$ converges.

The exact value of the above (the worst-case number of comparisons during the heap construction) is known to be equal to:

$2n-2s_{2}(n)-e_{2}(n)$

,

where *s*2(*n*) is the sum of all digits of the binary representation of n and *e*2(*n*) is the exponent of 2 in the prime factorization of n.

The average case is more complex to analyze, but it can be shown to asymptotically approach 1.8814 *n* − 2 log2*n* + *O*(1) comparisons.

The **Build-Max-Heap** function that follows, converts an array *A* which stores a complete binary tree with *n* nodes to a max-heap by repeatedly using **Max-Heapify** (down-heapify for a max-heap) in a bottom-up manner. The array elements indexed by *floor*(*n*/2) + 1, *floor*(*n*/2) + 2, ..., *n* are all leaves for the tree (assuming that indices start at 1)—thus each is a one-element heap, and does not need to be down-heapified. **Build-Max-Heap** runs **Max-Heapify** on each of the remaining tree nodes.

```
Build-Max-Heap (A):
    for each index i from floor(length(A)/2) downto 1 do:
        Max-Heapify(A, i)
```

## Heap implementation

Heaps are commonly implemented with an array. Any binary tree can be stored in an array, but because a binary heap is always a complete binary tree, it can be stored compactly. No space is required for pointers; instead, the parent and children of each node can be found by arithmetic on array indices. These properties make this heap implementation a simple example of an implicit data structure or Ahnentafel list. Details depend on the root position, which in turn may depend on constraints of a programming language used for implementation, or programmer preference. Specifically, sometimes the root is placed at index 1, in order to simplify arithmetic.

Let *n* be the number of elements in the heap and *i* be an arbitrary valid index of the array storing the heap. If the tree root is at index 0, with valid indices 0 through *n −*1, then each element *a* at index *i* has

- children at indices 2*i*+ 1 and 2*i*+ 2
- its parent at index *floor*((*i* − 1) / 2).

Alternatively, if the tree root is at index 1, with valid indices 1 through *n*, then each element *a* at index *i* has

- children at indices 2*i* and 2*i*+1
- its parent at index *floor*(*i* / 2).

This implementation is used in the heapsort algorithm which reuses the space allocated to the input array to store the heap (i.e. the algorithm is done in-place). This implementation is also useful as a Priority queue. When a dynamic array is used, insertion of an unbounded number of items is possible.

The `upheap` or `downheap` operations can then be stated in terms of an array as follows: suppose that the heap property holds for the indices *b*, *b*+1, ..., *e*. The sift-down function extends the heap property to *b*−1, *b*, *b*+1, ..., *e*. Only index *i* = *b*−1 can violate the heap property. Let *j* be the index of the largest child of *a*[*i*] (for a max-heap, or the smallest child for a min-heap) within the range *b*, ..., *e*. (If no such index exists because 2*i* > *e* then the heap property holds for the newly extended range and nothing needs to be done.) By swapping the values *a*[*i*] and *a*[*j*] the heap property for position *i* is established. At this point, the only problem is that the heap property might not hold for index *j*. The sift-down function is applied tail-recursively to index *j* until the heap property is established for all elements.

The sift-down function is fast. In each step it only needs two comparisons and one swap. The index value where it is working doubles in each iteration, so that at most log2 *e* steps are required.

For big heaps and using virtual memory, storing elements in an array according to the above scheme is inefficient: (almost) every level is in a different page. B-heaps are binary heaps that keep subtrees in a single page, reducing the number of pages accessed by up to a factor of ten.

The operation of merging two binary heaps takes Θ(*n*) for equal-sized heaps. The best you can do is (in case of array implementation) simply concatenating the two heap arrays and build a heap of the result. A heap on *n* elements can be merged with a heap on *k* elements using O(log *n* log *k*) key comparisons, or, in case of a pointer-based implementation, in O(log *n* log *k*) time. An algorithm for splitting a heap on *n* elements into two heaps on *k* and *n-k* elements, respectively, based on a new view of heaps as an ordered collections of subheaps was presented in. The algorithm requires O(log *n* * log *n*) comparisons. The view also presents a new and conceptually simple algorithm for merging heaps. When merging is a common task, a different heap implementation is recommended, such as binomial heaps, which can be merged in O(log *n*).

Additionally, a binary heap can be implemented with a traditional binary tree data structure, but there is an issue with finding the adjacent element on the last level on the binary heap when adding an element. This element can be determined algorithmically or by adding extra data to the nodes, called "threading" the tree—instead of merely storing references to the children, we store the inorder successor of the node as well.

It is possible to modify the heap structure to make the extraction of both the smallest and largest element possible in O $(\log n)$ time. To do this, the rows alternate between min heap and max-heap. The algorithms are roughly the same, but, in each step, one must consider the alternating rows with alternating comparisons. The performance is roughly the same as a normal single direction heap. This idea can be generalized to a min-max-median heap.

## Derivation of index equations

In an array-based heap, the children and parent of a node can be located via simple arithmetic on the node's index. This section derives the relevant equations for heaps with their root at index 0, with additional notes on heaps with their root at index 1.

To avoid confusion, we define the **level** of a node as its distance from the root, such that the root itself occupies level 0.

### Child nodes

For a general node located at index i (beginning from 0), we will first derive the index of its right child, ${\text{right}}=2i+2$ .

Let node i be located in level L, and note that any level l contains exactly $2^{l}$ nodes. Furthermore, there are exactly $2^{l+1}-1$ nodes contained in the layers up to and including layer l (think of binary arithmetic; 0111...111 = 1000...000 - 1). Because the root is stored at 0, the kth node will be stored at index $(k-1)$ . Putting these observations together yields the following expression for the **index of the last node in layer l**.

${\text{last}}(l)=(2^{l+1}-1)-1=2^{l+1}-2$

Let there be j nodes after node i in layer L, such that

${\begin{alignedat}{2}i=&\quad {\text{last}}(L)-j\\=&\quad (2^{L+1}-2)-j\\\end{alignedat}}$

Each of these j nodes must have exactly 2 children, so there must be $2j$ nodes separating i's right child from the end of its layer ( $L+1$ ).

${\begin{alignedat}{2}{\text{right}}=&\quad {\text{last(L + 1)}}-2j\\=&\quad (2^{L+2}-2)-2j\\=&\quad 2(2^{L+1}-2-j)+2\\=&\quad 2i+2\end{alignedat}}$

Noting that the left child of any node is always 1 place before its right child, we get ${\text{left}}=2i+1$ .

If the root is located at index 1 instead of 0, the last node in each level is instead at index $2^{l+1}-1$ . Using this throughout yields ${\text{left}}=2i$ and ${\text{right}}=2i+1$ for heaps with their root at 1.

### Parent node

Every non-root node is either the left or right child of its parent, so one of the following must hold:

- $i=2\times ({\text{parent}})+1$
- $i=2\times ({\text{parent}})+2$

Hence,

${\text{parent}}={\frac {i-1}{2}}\;{\textrm {or}}\;{\frac {i-2}{2}}$

Now consider the expression $\left\lfloor {\dfrac {i-1}{2}}\right\rfloor$ .

If node i is a left child, this gives the result immediately, however, it also gives the correct result if node i is a right child. In this case, $(i-2)$ must be even, and hence $(i-1)$ must be odd.

${\begin{alignedat}{2}\left\lfloor {\dfrac {i-1}{2}}\right\rfloor =&\quad \left\lfloor {\dfrac {i-2}{2}}+{\dfrac {1}{2}}\right\rfloor \\=&\quad {\frac {i-2}{2}}\\=&\quad {\text{parent}}\end{alignedat}}$

Therefore, irrespective of whether a node is a left or right child, its parent can be found by the expression:

${\text{parent}}=\left\lfloor {\dfrac {i-1}{2}}\right\rfloor$

Since the ordering of siblings in a heap is not specified by the heap property, a single node's two children can be freely interchanged unless doing so violates the shape property (compare with treap). Note, however, that in the common array-based heap, simply swapping the children might also necessitate moving the children's sub-tree nodes to retain the heap property.

The binary heap is a special case of the d-ary heap in which d = 2.

## Summary of running times

Here are time complexities of various heap data structures. The abbreviation am. indicates that the given complexity is amortized, otherwise it is a worst-case complexity. For the meaning of "*O*(*f*)" and "*Θ*(*f*)" see Big O notation. Names of operations assume a min-heap.

| Operation | find-min | delete-min | decrease-key | insert | meld | make-heap |
|---|---|---|---|---|---|---|
| Binary | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(*n*) | *Θ*(*n*) |
| Skew | *Θ*(1) | *O*(log *n*) am. | *O*(log *n*) am. | *O*(log *n*) am. | *O*(log *n*) am. | *Θ*(*n*) am. |
| Leftist | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(*n*) |
| Binomial | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(1) am. | *Θ*(log *n*) | *Θ*(*n*) |
| Skew binomial | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(1) | *Θ*(log *n*) | *Θ*(*n*) |
| 2–3 heap | *Θ*(1) | *O*(log *n*) am. | *Θ*(1) | *Θ*(1) am. | *O*(log *n*) | *Θ*(*n*) |
| Bottom-up skew | *Θ*(1) | *O*(log *n*) am. | *O*(log *n*) am. | *Θ*(1) am. | *Θ*(1) am. | *Θ*(*n*) am. |
| Pairing | *Θ*(1) | *O*(log *n*) am. | *o*(log *n*) am. | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Rank-pairing | *Θ*(1) | *O*(log *n*) am. | *Θ*(1) am. | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Fibonacci | *Θ*(1) | *O*(log *n*) am. | *Θ*(1) am. | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Strict Fibonacci | *Θ*(1) | *Θ*(log *n*) | *Θ*(1) | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Brodal | *Θ*(1) | *Θ*(log *n*) | *Θ*(1) | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |

1. In fact, this procedure can be shown to take Θ(*n* log *n*) time in the worst case, meaning that *n* log *n* is also an asymptotic lower bound on the complexity. In the *average case* (averaging over all permutations of n inputs), though, the method takes linear time.
2. This does not mean that *sorting* can be done in linear time since building a heap is only the first step of the heapsort algorithm.
3. *make-heap* is the operation of building a heap from a sequence of *n* unsorted elements. It can be done in *Θ*(*n*) time whenever *meld* runs in *O*(log *n*) time (where both complexities can be amortized). Another algorithm achieves *Θ*(*n*) for binary heaps.
4. For persistent heaps (not supporting *decrease-key*), a generic transformation reduces the cost of *meld* to that of *insert*, while the new cost of *delete-min* is the sum of the old costs of *delete-min* and *meld*. Here, it makes *meld* run in *Θ*(1) time (amortized, if the cost of *insert* is) while *delete-min* still runs in *O*(log *n*). Applied to skew binomial heaps, it yields Brodal-Okasaki queues, persistent heaps with optimal worst-case complexities.
5. Lower bound of $\Omega (\log \log n),$ upper bound of $O(2^{2{\sqrt {\log \log n}}}).$
6. Brodal queues and strict Fibonacci heaps achieve optimal worst-case complexities for heaps. They were first described as imperative data structures. The Brodal-Okasaki queue is a persistent data structure achieving the same optimum, except that *decrease-key* is not supported.
