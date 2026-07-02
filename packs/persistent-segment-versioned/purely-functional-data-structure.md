---
title: "Purely functional data structure"
source: https://en.wikipedia.org/wiki/Purely_functional_data_structure
domain: persistent-segment-versioned
license: CC-BY-SA-4.0
tags: persistent segment tree, versioned range query, path copying, functional data structure
fetched: 2026-07-02
---

# Purely functional data structure

In computer science, a **purely functional data structure** is a data structure that can be directly implemented in a purely functional language. The main difference between an arbitrary data structure and a purely functional one is that the latter is (strongly) immutable. This restriction ensures the data structure possesses the advantages of immutable objects: (full) persistency, quick copy of objects, and thread safety. Efficient purely functional data structures may require the use of lazy evaluation and memoization.

## Definition

Persistent data structures have the property of keeping previous versions of themselves unmodified. On the other hand, non-persistent structures such as arrays admit a **destructive update**, that is, an update which cannot be reversed. Once a program writes a value in some index of the array, its previous value can not be retrieved anymore.

Formally, a *purely functional data structure* is a data structure which can be implemented in a purely functional language, such as Haskell. In practice, it means that the data structures must be built using only persistent data structures such as tuples, sum types, product types, and basic types such as integers, characters, strings. Such a data structure is necessarily persistent. However, not all persistent data structures are purely functional. For example, a persistent array is a data-structure which is persistent and which is implemented using an array, thus is not purely functional.

In the book *Purely functional data structures*, Okasaki compares destructive updates to master chef's knives. Destructive updates cannot be undone, and thus they should not be used unless it is certain that the previous value is not required anymore. However, destructive updates can also allow efficiency that can not be obtained using other techniques. For example, a data structure using an array and destructive updates may be replaced by a similar data structure where the array is replaced by a map, a random access list, or a balanced tree, which admits a purely functional implementation. But the access cost may increase from constant time to logarithmic time.

## Ensuring that a data structure is purely functional

A data structure is never inherently functional. For example, a stack can be implemented as a singly-linked list. This implementation is purely functional as long as the only operations on the stack return a new stack without altering the old stack. However, if the language is not purely functional, the run-time system may be unable to guarantee immutability. This is illustrated by Okasaki, where he shows the concatenation of two singly-linked lists can still be done using an imperative setting.

In order to ensure that a data structure is used in a purely functional way in an impure functional language, modules or classes can be used to ensure manipulation via authorized functions only.

## Using purely functional data structures

One of the central challenges in adapting existing code to use purely functional data structures lies in the fact that mutable data structures provide "hidden outputs" for functions that use them. Rewriting these functions to use purely functional data structures requires adding these data structures as explicit outputs.

For instance, consider a function that accepts a mutable list, removes the first element from the list, and returns that element. In a purely functional setting, removing an element from the list produces a new and shorter list, but does not update the original one. In order to be useful, therefore, a purely functional version of this function is likely to have to return the new list along with the removed element. In the most general case, a program converted in this way must return the "state" or "store" of the program as an additional result from every function call. Such a program is said to be written in store-passing style.

## Examples

Here is a list of abstract data structures with purely functional implementations:

- Stack (first in, last out) implemented as a singly linked list,
- Queue, implemented as a real-time queue,
- Double-ended queue, implemented as a real-time double-ended queue,
- (Multi)set of ordered elements and map indexed by ordered keys, implemented as a red–black tree, or more generally by a search tree,
- Priority queue, implemented as a Brodal queue
- Random access list, implemented as a skew-binary random access list
- Hash consing
- Zipper (data structure)

## Design and implementation

In his book *Purely Functional Data Structures*, computer scientist Chris Okasaki describes techniques used to design and implement purely functional data structures, a small subset of which are summarized below.

### Laziness and memoization

Lazy evaluation is particularly interesting in a purely functional language because the order of the evaluation never changes the result of a function. Therefore, lazy evaluation naturally becomes an important part of the construction of purely functional data structures. It allows a computation to be done only when its result is actually required. Therefore, the code of a purely functional data structure can, without loss of efficiency, consider similarly data that will effectively be used and data that will be ignored. The only computation required is for the first kind of data; that is what will actually be performed.

One of the key tools in building efficient, purely functional data structures is memoization. When a computation is done, it is saved and does not have to be performed a second time. This is particularly important in lazy implementations; additional evaluations may require the same result, but it is impossible to know which evaluation will require it first.

### Amortized analysis and scheduling

Some data structures, even those that are not purely functional such as dynamic arrays, admit operations that are efficient most of the time (e.g., constant time for dynamic arrays), and rarely inefficient (e.g., linear time for dynamic arrays). *Amortization* can then be used to prove that the average running time of the operations is efficient. That is to say, the few inefficient operations are rare enough, and do not change the asymptotical evolution of time complexity when a sequence of operations is considered.

In general, having inefficient operations is not acceptable for persistent data structures, because this very operation can be called many times. It is not acceptable either for real-time or for imperative systems, where the user may require the time taken by the operation to be predictable. Furthermore, this unpredictability complicates the use of parallelism.

In order to avoid those problems, some data structures allow for the inefficient operation to be postponed—this is called scheduling. The only requirement is that the computation of the inefficient operation should end before its result is actually needed. A constant part of the inefficient operation is performed simultaneously with the following call to an efficient operation, so that the inefficient operation is already totally done when it is needed, and each individual operation remains efficient.

#### Example: queue

Amortized queues are composed of two singly-linked lists: the front and the reversed rear. Elements are added to the rear list and are removed from the front list. Furthermore, whenever the front queue is empty, the rear queue is reversed and becomes the front, while the rear queue becomes empty. The amortized time complexity of each operation is constant. Each cell of the list is added, reversed and removed at most once. In order to avoid an inefficient operation where the rear list is reversed, real-time queues add the restriction that the rear list is only as long as the front list. To ensure that the front list stays longer than the rear list, the rear list is reversed and appended to the front list. Since this operation is inefficient, it is not performed immediately. Instead, it is spread out over the subsequent operations. Thus, each cell is computed before it is needed, and the new front list is totally computed before a new inefficient operation needs to be called.
