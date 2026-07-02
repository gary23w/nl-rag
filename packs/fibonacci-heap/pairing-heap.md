---
title: "Pairing heap"
source: https://en.wikipedia.org/wiki/Pairing_heap
domain: fibonacci-heap
license: CC-BY-SA-4.0
tags: fibonacci heap, amortized heap, priority queue, mergeable heap
fetched: 2026-07-02
---

# Pairing heap

A **pairing heap** is a type of heap data structure with relatively simple implementation and excellent practical amortized performance, introduced by Michael Fredman, Robert Sedgewick, Daniel Sleator, and Robert Tarjan in 1986. Pairing heaps are heap-ordered multiway tree structures, and can be considered simplified Fibonacci heaps. They are considered a "robust choice" for implementing such algorithms as Prim's MST algorithm, and support the following operations (assuming a min-heap):

- *find-min*: simply return the top element of the heap.
- *meld*: compare the two root elements, the smaller remains the root of the result, the larger element and its subtree is appended as a child of this root.
- *insert*: create a new heap for the inserted element and *meld* into the original heap.
- *decrease-key* (optional): remove the subtree rooted at the key to be decreased, replace the key with a smaller key, then *meld* the result back into the heap.
- *delete-min*: remove the root and do repeated *melds* of its subtrees until one tree remains. Various merging strategies are employed.

The analysis of pairing heaps' time complexity was initially inspired by that of splay trees. The amortized time per *delete-min* is *O*(log *n*), and the operations *find-min*, *meld*, and *insert* run in *O*(1) time.

When a *decrease-key* operation is added as well, determining the precise asymptotic running time of pairing heaps has turned out to be difficult. Initially, the time complexity of this operation was conjectured on empirical grounds to be *O*(1), but Fredman proved that the amortized time per *decrease-key* is at least $\Omega (\log \log n)$ for some sequences of operations. Using a different amortization argument, Pettie then proved that *insert*, *meld*, and *decrease-key* all run in $O(2^{2{\sqrt {\log \log n}}})$ amortized time, which is $o(\log n)$ . Elmasry later introduced elaborations of pairing heaps (lazy, consolidate) for which *decrease-key* runs in $O(\log \log n)$ amortized time and other operations have optimal amortized bounds, but no tight $\Theta (\log \log n)$ bound is known for the original data structure.

Although the asymptotic performance of pairing heaps is worse than other priority queue algorithms such as Fibonacci heaps, which perform *decrease-key* in $O(1)$ amortized time, the performance in practice is excellent. Jones and Larkin, Sen, and Tarjan conducted experiments on pairing heaps and other heap data structures. They concluded that d-ary heaps such as binary heaps are faster than all other heap implementations when the *decrease-key* operation is not needed (and hence there is no need to externally track the location of nodes in the heap), but that when *decrease-key* is needed pairing heaps are often faster than d-ary heaps and almost always faster than other pointer-based heaps, including data structures like Fibonacci heaps that are theoretically more efficient. Chen et al. examined priority queues specifically for use with Dijkstra's algorithm and concluded that in normal cases using a d-ary heap without *decrease-key* (instead duplicating nodes on the heap and ignoring redundant instances) resulted in better performance, despite the inferior theoretical performance guarantees.

## Structure

A pairing heap is either an empty heap, or a pairing tree consisting of a root element and a possibly empty list of pairing trees. The heap ordering property requires that parent of any node is no greater than the node itself. The following description assumes a purely functional heap that does not support the *decrease-key* operation.

```
type PairingTree[Elem] = Heap(elem: Elem, subheaps: List[PairingTree[Elem]])
type PairingHeap[Elem] = Empty | PairingTree[Elem]
```

A pointer-based implementation for RAM machines, supporting *decrease-key*, can be achieved using three pointers per node, by representing the children of a node by a doubly-linked list: a pointer to the node's first child, one to its next sibling, and one to its previous sibling (or, for the leftmost sibling, to its parent). It can also be viewed as a variant of a Left-child right-sibling binary tree with an additional pointer to a node's parent (which represents its previous sibling or actual parent for the leftmost sibling). Alternatively, the previous-pointer can be omitted by letting the last child point back to the parent, if a single Boolean flag is added to indicate "end of list". This achieves a more compact structure at the expense of a constant overhead factor per operation.

## Operations

### Meld

Melding with an empty heap returns the other heap, otherwise a new heap is returned that has the minimum of the two root elements as its root element and just adds the heap with the larger root to the list of subheaps:

```
function meld(heap1, heap2: PairingHeap[Elem]) -> PairingHeap[Elem]
    if heap1 is Empty
        return heap2
    elsif heap2 is Empty
        return heap1
    elsif heap1.elem < heap2.elem
        return Heap(heap1.elem, heap2 :: heap1.subheaps)
    else
        return Heap(heap2.elem, heap1 :: heap2.subheaps)
```

### Insert

The easiest way to insert an element into a heap is to meld the heap with a new heap containing just this element and an empty list of subheaps:

```
function insert(elem: Elem, heap: PairingHeap[Elem]) -> PairingHeap[Elem]
    return meld(Heap(elem, []), heap)
```

### Find-min

The function *find-min* simply returns the root element of the heap:

```
function find-min(heap: PairingHeap[Elem]) -> Elem
    if heap is Empty
        error
    else
        return heap.elem
```

### Delete-min

The only non-trivial fundamental operation is the deletion of the minimum element from the heap. This requires performing repeated melds of its children until only one tree remains. The standard strategy first melds the subheaps in pairs (this is the step that gave this data structure its name) from left to right and then melds the resulting list of heaps from right to left:

```
function delete-min(heap: PairingHeap[Elem]) -> PairingHeap[Elem]
    if heap is Empty
        error
    else
        return merge-pairs(heap.subheaps)
```

This uses the auxiliary function *merge-pairs*:

```
function merge-pairs(list: List[PairingTree[Elem]]) -> PairingHeap[Elem]
    if length(list) == 0
        return Empty
    elsif length(list) == 1
        return list[0]
    else
        return meld(meld(list[0], list[1]), merge-pairs(list[2..]))
```

That this does indeed implement the described two-pass left-to-right then right-to-left merging strategy can be seen from this reduction:

```
   merge-pairs([H1, H2, H3, H4, H5, H6, H7])
=> meld(meld(H1, H2), merge-pairs([H3, H4, H5, H6, H7]))
     # meld H1 and H2 to H12, then the rest of the list
=> meld(H12, meld(meld(H3, H4), merge-pairs([H5, H6, H7])))
     # meld H3 and H4 to H34, then the rest of the list
=> meld(H12, meld(H34, meld(meld(H5, H6), merge-pairs([H7]))))
     # meld H5 and H6 to H56, then the rest of the list
=> meld(H12, meld(H34, meld(H56, H7)))
     # switch direction, meld the last two resulting heaps, giving H567
=> meld(H12, meld(H34, H567))
     # meld the last two resulting heaps, giving H34567
=> meld(H12, H34567) 
     # finally, meld the first pair with the result of merging the rest
=> H1234567
```

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

1. *make-heap* is the operation of building a heap from a sequence of *n* unsorted elements. It can be done in *Θ*(*n*) time whenever *meld* runs in *O*(log *n*) time (where both complexities can be amortized). Another algorithm achieves *Θ*(*n*) for binary heaps.
2. For persistent heaps (not supporting *decrease-key*), a generic transformation reduces the cost of *meld* to that of *insert*, while the new cost of *delete-min* is the sum of the old costs of *delete-min* and *meld*. Here, it makes *meld* run in *Θ*(1) time (amortized, if the cost of *insert* is) while *delete-min* still runs in *O*(log *n*). Applied to skew binomial heaps, it yields Brodal-Okasaki queues, persistent heaps with optimal worst-case complexities.
3. Lower bound of $\Omega (\log \log n),$ upper bound of $O(2^{2{\sqrt {\log \log n}}}).$
4. Brodal queues and strict Fibonacci heaps achieve optimal worst-case complexities for heaps. They were first described as imperative data structures. The Brodal-Okasaki queue is a persistent data structure achieving the same optimum, except that *decrease-key* is not supported.
