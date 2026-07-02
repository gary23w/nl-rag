---
title: "Priority queue"
source: https://en.wikipedia.org/wiki/Priority_queue
domain: heapsort-algorithm
license: CC-BY-SA-4.0
tags: heapsort algorithm, binary heap, priority queue, in place sorting
fetched: 2026-07-02
---

# Priority queue

In computer science, a **priority queue** is an abstract data type similar to a regular queue where each element has an associated priority determining its order of service. Priority queue serves highest priority items first. Priority values have to be instances of an ordered data type, and higher priority can be given either to the lesser or to the greater values with respect to the given order relation. For example, in the Java standard library, the PriorityQueue class considers the lowest element with respect to their order as having the highest priority.

While priority queues are often implemented using heaps, they are conceptually distinct. A priority queue can be implemented with a heap or with other methods; just as a list can be implemented with a linked list or with an array.

## Operations

A priority queue has the following operations:

### Max-priority queue

- `insert(S, element, priority)`: add an element to set `S` with an associated priority.

- `maximum(S)`: return the element with *highest priority*. This is also known as "`find_max`".

- `extract_max(S)`: remove the element from set `S` with *highest priority*, and return it. This is also known as "`delete`", or "`extract`".

- `increase_key(S, element, k)`: increase the associated priority with an element to the new value `k`.

### Min-priority queue

- `insert(S, element, priority)`: add an element to set `S` with an associated priority.

- `minimum(S)`: return the element with *lowest priority*. This is also known as "`find_min`".

- `extract_min(S)`: remove the element from set `S` with *lowest priority*, and return it. This is also known as "`delete`", or "`extract`".

- `decrease_key(S, element, k)`: decrease the associated priority with an element to the new value `k`.

Stacks and queues can be implemented as particular kinds of priority queues, with the priority determined by the order in which the elements are inserted. In a stack, the priority of each inserted element is monotonically increasing; thus, the last element inserted is always the first retrieved. In a queue, the priority of each inserted element is monotonically decreasing; thus, the first element inserted is always the first retrieved.

In some implementations, if two elements have the same priority, they are served in the same order in which they were enqueued. In other implementations, the order of elements with the same priority is undefined.

## Implementation

### Naive implementations

One can create a simple, but inefficient priority queue in a number of ways. These naive implementations can demonstrate the expected behaviour of a priority queue in a simpler manner.

- *insert* elements into an unsorted array; find and *extract* element with *highest priority* Performance: "`insert`" performs in $O(1)$ constant time, where "`extract_max`" performs in $O(n)$ linear time.

```
insert(element, priority):
 node.element ← element
 node.priority ← priority
 list.append(node)

extract_max():
 highest ← 0
 foreach node in list:
 if highest.priority < node.priority:
  highest ← node
 list.remove(highest)
 return highest.element
```

- *insert* elements into a sorted array; *extract* first element Performance: "`insert`" performs in $O(n)$ linear time, where "`extract_max`" performs in $O(1)$ constant time.

```
insert(element, priority):
 node.element ← element
 node.priority ← priority
 for i in [0...N]:
 element ← list.get_at_index(i)
 if element.priority < node.priority:
  list.insert_at_index(node, i + 1)
  return

extract_max():
 highest ← list.get_at_index(0)
 list.remove(highest)
 return highest.element
```

### Usual implementation

To improve performance, priority queues are typically based on a heap, giving $O(\log n)$ performance for inserts and removals, and $O(n)$ to build the heap initially from a set of n elements. Variants of the basic heap data structure such as pairing heaps or Fibonacci heaps can provide better bounds for some operations.

Alternatively, when a self-balancing binary search tree is used, insertion and removal also take $O(\log n)$ time, although building trees from existing sequences of elements takes $O(n\log n)$ time; this is typical where one might already have access to these data structures, such as with third-party or standard libraries. From a space-complexity standpoint, using self-balancing binary search tree with linked list takes more storage, since it requires storing extra references to other nodes.

From a computational-complexity standpoint, priority queues are congruent to sorting algorithms. The section on the equivalence of priority queues and sorting algorithms, below, describes how efficient sorting algorithms can create efficient priority queues.

### Specialized heaps

There are several specialized heap data structures that either supply additional operations or outperform heap-based implementations for specific types of keys, specifically integer keys. Suppose the set of possible keys is $\{1,2,...,C\}$ .

- When only `insert`, `find-min` and `extract-min` are needed and in case of integer priorities, a bucket queue can be constructed as an array of C linked lists plus a pointer ${\text{top}}$ , initially C . Inserting an item with key k appends the item to the k 'th list, and updates ${\text{top}}\gets {\text{min}}({\text{top}},k)$ , both in constant time. `extract-min` deletes and returns one item from the list with index ${\text{top}}$ , then increments ${\text{top}}$ if needed until it again points to a non-empty list; this takes $O(C)$ time in the worst case. These queues are useful for sorting the vertices of a graph by their degree.
- A van Emde Boas tree supports the `minimum`, `maximum`, `insert`, `delete`, `search`, `extract-min`, `extract-max`, `predecessor` and `successor]` operations in $O(\log \log C)$ time, but has a space cost for small queues of about $O(2^{m/2})$ , where m is the number of bits in the priority value. The space can be reduced significantly with hashing.
- The Fusion tree by Fredman and Willard implements the `minimum` operation in $O(1)$ time and `insert` and `extract-min` operations in $O(\log n/\log \log C)$ time. However it is stated by the author that, "Our algorithms have theoretical interest only; The constant factors involved in the execution times preclude practicality."

For applications that do many "peek" operations for every "`extract-min`" operation, the time complexity for peek actions can be reduced to $O(1)$ in all tree and heap implementations by caching the highest priority element after every insertion and removal. For insertion, this adds at most a constant cost, since the newly inserted element is compared only to the previously cached minimum element. For deletion, this at most adds an additional "peek" cost, which is typically cheaper than the deletion cost, so overall time complexity is not significantly impacted.

Monotone priority queues are specialized queues that are optimized for the case where no item is ever inserted that has a lower priority (in the case of min-heap) than any item previously extracted. This restriction is met by several practical applications of priority queues.

### Summary of running times

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

## Equivalence of priority queues and sorting algorithms

### Using a priority queue to sort

The semantics of priority queues naturally suggest a sorting method: insert all the elements to be sorted into a priority queue, and sequentially remove them; they will come out in sorted order. This is actually the procedure used by several sorting algorithms, once the layer of abstraction provided by the priority queue is removed. This sorting method is equivalent to the following sorting algorithms:

| Name | Priority queue implementation | Best | Average | Worst |
|---|---|---|---|---|
| Heapsort | Heap | $n\log n$ | $n\log n$ | $n\log n$ |
| Smoothsort | Leonardo heap | n | $n\log n$ | $n\log n$ |
| Selection sort | Unordered array | $n^{2}$ | $n^{2}$ | $n^{2}$ |
| Insertion sort | Ordered array | n | $n^{2}$ | $n^{2}$ |
| Tree sort | Self-balancing binary search tree | $n\log n$ | $n\log n$ | $n\log n$ |

### Using a sorting algorithm to make a priority queue

A sorting algorithm can also be used to implement a priority queue. Specifically, Thorup says:

> We present a general deterministic linear space reduction from priority queues to sorting implying that if we can sort up to n keys in $S(n)$ time per key, then there is a priority queue supporting `delete` and `insert` in $O(S(n))$ time and `find-min` in constant time.

That is, if there is a sorting algorithm which can sort in $O(S)$ time per key, where S is some function of n and word size, then one can use the given procedure to create a priority queue where pulling the highest-priority element is $O(1)$ time, and inserting new elements (and deleting elements) is $O(S)$ time. For example, if one has an $O(n\log n)$ sort algorithm, one can create a priority queue with $O(1)$ pulling and $O(\log n)$ insertion.

## Libraries

A priority queue is often considered to be a "container data structure".

The Standard Template Library (STL), and the C++ 1998 standard, specifies std::priority_queue as one of the STL container adaptor class templates. However, it does not specify how two elements with same priority should be served, and indeed, common implementations will not return them according to their order in the queue. It implements a max-priority-queue, and has three parameters: a comparison object for sorting such as a function object (defaults to `less<T>` if unspecified), the underlying container for storing the data structures (defaults to `std::vector<T>`), and two iterators to the beginning and end of a sequence. Unlike actual STL containers, it does not allow iteration of its elements (it strictly adheres to its abstract data type definition). STL also has utility functions for manipulating another random-access container as a binary max-heap. The Boost libraries also have an implementation in the library heap.

Python's heapq module implements a binary min-heap on top of a list.

Java's library contains a `PriorityQueue` (`java.util.PriorityQueue`) class, which implements a min-priority-queue as a binary heap.

.NET's library contains a System.Collections.Generic.PriorityQueue class, which implements an array-backed, quaternary min-heap.

Scala's library contains a scala.collection.mutable.PriorityQueue class, which implements a max-priority-queue.

Go's library contains a container/heap module, which implements a min-heap on top of any compatible data structure.

Rust's standard library contains a std::collections::BinaryHeap struct, which implements a priority queue with a binary heap.

The Standard PHP Library extension contains the class SplPriorityQueue.

Apple's Core Foundation framework contains a CFBinaryHeap structure, which implements a min-heap.

## Applications

### Bandwidth management

Priority queuing can be used to manage limited resources such as bandwidth on a transmission line from a network router. In the event of outgoing traffic queuing due to insufficient bandwidth, all other queues can be halted to send the traffic from the highest priority queue upon arrival. This ensures that the prioritized traffic (such as real-time traffic, e.g. an RTP stream of a VoIP connection) is forwarded with the least delay and the least likelihood of being rejected due to a queue reaching its maximum capacity. All other traffic can be handled when the highest priority queue is empty. Another approach used is to send disproportionately more traffic from higher priority queues.

Many modern protocols for local area networks also include the concept of priority queues at the media access control (MAC) sub-layer to ensure that high-priority applications (such as VoIP or IPTV) experience lower latency than other applications which can be served with best-effort service. Examples include IEEE 802.11e (an amendment to IEEE 802.11 which provides quality of service) and ITU-T G.hn (a standard for high-speed local area network using existing home wiring (power lines, phone lines and coaxial cables).

Usually a limitation (policer) is set to limit the bandwidth that traffic from the highest priority queue can take, in order to prevent high priority packets from choking off all other traffic. This limit is usually never reached due to high level control instances such as the Cisco Callmanager, which can be programmed to inhibit calls which would exceed the programmed bandwidth limit.

### Discrete event simulation

Another use of a priority queue is to manage the events in a discrete event simulation. The events are added to the queue with their simulation time used as the priority. The execution of the simulation proceeds by repeatedly pulling the top of the queue and executing the event thereon.

*See also*: Scheduling (computing), queueing theory

### Dijkstra's algorithm

When the graph is stored in the form of adjacency list or matrix, priority queue can be used to extract minimum efficiently when implementing Dijkstra's algorithm, although one also needs the ability to alter the priority of a particular vertex in the priority queue efficiently.

If instead, a graph is stored as node objects, and priority-node pairs are inserted into a heap, altering the priority of a particular vertex is not necessary if one tracks visited nodes. Once a node is visited, if it comes up in the heap again (having had a lower priority number associated with it earlier), it is popped-off and ignored.

### Huffman coding

Huffman coding requires one to repeatedly obtain the two lowest-frequency trees. A priority queue is one method of doing this.

Best-first search algorithms, like the A* search algorithm, find the shortest path between two vertices or nodes of a weighted graph, trying out the most promising routes first. A priority queue (also known as the *fringe*) is used to keep track of unexplored routes; the one for which the estimate (a lower bound in the case of A*) of the total path length is smallest is given highest priority. If memory limitations make best-first search impractical, variants like the SMA* algorithm can be used instead, with a double-ended priority queue to allow removal of low-priority items.

### ROAM triangulation algorithm

The Real-time Optimally Adapting Meshes (ROAM) algorithm computes a dynamically changing triangulation of a terrain. It works by splitting triangles where more detail is needed and merging them where less detail is needed. The algorithm assigns each triangle in the terrain a priority, usually related to the error decrease if that triangle would be split. The algorithm uses two priority queues, one for triangles that can be split and another for triangles that can be merged. In each step the triangle from the split queue with the highest priority is split, or the triangle from the merge queue with the lowest priority is merged with its neighbours.

### Prim's algorithm for minimum spanning tree

Using min heap priority queue in Prim's algorithm to find the minimum spanning tree of a connected and undirected graph, one can achieve a good running time. This min heap priority queue uses the min heap data structure which supports operations such as `insert`, `minimum`, `extract-min`, `decrease-key`. In this implementation, the weight of the edges is used to decide the priority of the vertices. Lower the weight, higher the priority and higher the weight, lower the priority.

## Parallel priority queue

Parallelization can be used to speed up priority queues, but requires some changes to the priority queue interface. The reason for such changes is that a sequential update usually only has ${\textstyle O(1)}$ or ${\textstyle O(\log n)}$ cost, and there is no practical gain to parallelize such an operation. One possible change is to allow the concurrent access of multiple processors to the same priority queue. The second possible change is to allow batch operations that work on ${\textstyle k}$ elements, instead of just one element. For example, `extractMin` will remove the first ${\textstyle k}$ elements with the highest priority.

### Concurrent parallel access

If the priority queue allows concurrent access, multiple processes can perform operations concurrently on that priority queue. However, this raises two issues. First of all, the definition of the semantics of the individual operations is no longer obvious. For example, if two processes want to extract the element with the highest priority, should they get the same element or different ones? This restricts parallelism on the level of the program using the priority queue. In addition, because multiple processes have access to the same element, this leads to contention.

The concurrent access to a priority queue can be implemented on a Concurrent Read, Concurrent Write (CRCW) PRAM model. In the following the priority queue is implemented as a skip list. In addition, an atomic synchronization primitive, CAS, is used to make the skip list lock-free. The nodes of the skip list consists of a unique key, a priority, an array of pointers, for each level, to the next nodes and a `delete` mark. The `delete` mark marks if the node is about to be deleted by a process. This ensures that other processes can react to the deletion appropriately.

- `insert(e)`: First, a new node with a key and a priority is created. In addition, the node is assigned a number of levels, which dictates the size of the array of pointers. Then a search is performed to find the correct position where to insert the new node. The search starts from the first node and from the highest level. Then the skip list is traversed down to the lowest level until the correct position is found. During the search, for every level the last traversed node will be saved as parent node for the new node at that level. In addition, the node to which the pointer, at that level, of the parent node points towards, will be saved as the successor node of the new node at that level. Afterwards, for every level of the new node, the pointers of the parent node will be set to the new node. Finally, the pointers, for every level, of the new node will be set to the corresponding successor nodes.
- `extract-min`: First, the skip list is traversed until a node is reached whose `delete` mark is not set. This `delete` mark is than set to true for that node. Finally the pointers of the parent nodes of the deleted node are updated.

If the concurrent access to a priority queue is allowed, conflicts may arise between two processes. For example, a conflict arises if one process is trying to insert a new node, but at the same time another process is about to delete the predecessor of that node. There is a risk that the new node is added to the skip list, yet it is not longer reachable. (See image)

### *K*-element operations

In this setting, operations on a priority queue is generalized to a batch of ${\textstyle k}$ elements. For instance, `k_extract-min` deletes the ${\textstyle k}$ smallest elements of the priority queue and returns those.

In a shared-memory setting, the parallel priority queue can be easily implemented using parallel binary search trees and join-based tree algorithms. In particular, `k_extract-min` corresponds to a *split* on the binary search tree that has ${\textstyle O(\log n)}$ cost and yields a tree that contains the ${\textstyle k}$ smallest elements. `k_insert` can be applied by a *union* of the original priority queue and the batch of insertions. If the batch is already sorted by the key, `k_insert` has ${\textstyle O(k\log(1+{\frac {n}{k}}))}$ cost. Otherwise, we need to first sort the batch, so the cost will be ${\textstyle O(k\log(1+{\frac {n}{k}})+k\log k)=O(k\log n)}$ . Other operations for priority queue can be applied similarly. For instance, `k_decrease-key` can be done by first applying `difference` and then `union`, which first deletes the elements and then inserts them back with the updated keys. All these operations are highly parallel, and the theoretical and practical efficiency can be found in related research papers.

The rest of this section discusses a queue-based algorithm on distributed memory. We assume each processor has its own local memory and a local (sequential) priority queue. The elements of the global (parallel) priority queue are distributed across all processors.

A `k_insert` operation assigns the elements uniformly random to the processors which insert the elements into their local queues. Note that single elements can still be inserted into the queue. Using this strategy the global smallest elements are in the union of the local smallest elements of every processor with high probability. Thus each processor holds a representative part of the global priority queue.

This property is used when `k_extract-min` is executed, as the smallest ${\textstyle m}$ elements of each local queue are removed and collected in a result set. The elements in the result set are still associated with their original processor. The number of elements ${\textstyle m}$ that is removed from each local queue depends on ${\textstyle k}$ and the number of processors ${\textstyle p}$ . By parallel selection the ${\textstyle k}$ smallest elements of the result set are determined. With high probability these are the global ${\textstyle k}$ smallest elements. If not, ${\textstyle m}$ elements are again removed from each local queue and put into the result set. This is done until the global ${\textstyle k}$ smallest elements are in the result set. Now these ${\textstyle k}$ elements can be returned. All other elements of the result set are inserted back into their local queues. The running time of `k_extract-min` is expected ${\textstyle O({\frac {k}{p}}\log(n))}$ , where ${\textstyle k=\Omega (p\cdot \log(p))}$ and ${\textstyle n}$ is the size of the priority queue.

The priority queue can be further improved by not moving the remaining elements of the result set directly back into the local queues after a `k_extract-min` operation. This saves moving elements back and forth all the time between the result set and the local queues.

By removing several elements at once a considerable speedup can be reached. But not all algorithms can use this kind of priority queue. Dijkstra's algorithm for example can not work on several nodes at once. The algorithm takes the node with the smallest distance from the priority queue and calculates new distances for all its neighbor nodes. If you would take out ${\textstyle k}$ nodes, working at one node could change the distance of another one of the ${\textstyle k}$ nodes. So using k-element operations destroys the label setting property of Dijkstra's algorithm.
