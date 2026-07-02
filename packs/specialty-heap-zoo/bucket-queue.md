---
title: "Bucket queue"
source: https://en.wikipedia.org/wiki/Bucket_queue
domain: specialty-heap-zoo
license: CC-BY-SA-4.0
tags: soft heap, kinetic heap, weak heap, mergeable heap, calendar queue
fetched: 2026-07-02
---

# Bucket queue

A **bucket queue** is a data structure that implements the priority queue abstract data type: it maintains a dynamic collection of elements with numerical priorities and allows quick access to the element with minimum (or maximum) priority. In the bucket queue, the priorities must be integers, and it is particularly suited to applications in which the priorities have a small range. A bucket queue has the form of an array of buckets: an array data structure, indexed by the priorities, whose cells contain collections of items with the same priority as each other. With this data structure, insertion of elements and changes of their priority take constant time. Searching for and removing the minimum-priority element takes time proportional to the number of buckets or, by maintaining a pointer to the most recently found bucket, in time proportional to the difference in priorities between successive operations.

The bucket queue is the priority-queue analogue of pigeonhole sort (also called bucket sort), a sorting algorithm that places elements into buckets indexed by their priorities and then concatenates the buckets. Using a bucket queue as the priority queue in a selection sort gives a form of the pigeonhole sort algorithm. Bucket queues are also called **bucket priority queues** or **bounded-height priority queues**. When used for quantized approximations to real number priorities, they are also called **untidy priority queues** or **pseudo priority queues**. They are closely related to the calendar queue, a structure that uses a similar array of buckets for exact prioritization by real numbers.

Applications of the bucket queue include computation of the degeneracy of a graph, fast algorithms for shortest paths and widest paths for graphs with weights that are small integers or are already sorted, and greedy approximation algorithms for the set cover problem. The quantized version of the structure has also been applied to scheduling and to marching cubes in computer graphics. The first use of the bucket queue was in a shortest path algorithm by Dial (1969).

## Operation

### Basic data structure

A bucket queue can handle elements with integer priorities in the range from 0 or 1 up to some known bound C, and operations that insert elements, change the priority of elements, or extract (find and remove) the element that has the minimum (or maximum) priority. It consists of an array A of container data structures; in most sources these containers are doubly linked lists but they could alternatively be dynamic arrays or dynamic sets. The container in the pth array cell *A*[*p*] stores the collection of elements whose priority is p.

A bucket queue can handle the following operations:

- To insert an element x with priority p, add x to the container at *A*[*p*].
- To change the priority of an element, remove it from the container for its old priority and re-insert it into the container for its new priority.
- To extract an element with the minimum or maximum priority, perform a sequential search in the array to find the first or last non-empty container, respectively, choose an arbitrary element from this container, and remove it from the container.

In this way, insertions and priority changes take constant time, and extracting the minimum or maximum priority element takes time *O*(*C*).

### Optimizations

As an optimization, the data structure can start each sequential search for a non-empty bucket at the most recently-found non-empty bucket instead of at the start of the array. This can be done in either of two different ways, lazy (delaying these sequential searches until they are necessary) or eager (doing the searches ahead of time). The choice of when to do the search affects which of the data structure operations is slowed by these searches. Dial's original version of the structure used a lazy search. This can be done by maintaining an index L that is a lower bound on the minimum priority of any element currently in the queue. When inserting a new element, L should be updated to the minimum of its old value and the new element's priority. When searching for the minimum priority element, the search can start at L instead of at zero, and after the search L should be left equal to the priority that was found in the search. Alternatively, the eager version of this optimization keeps L updated so that it always points to the first non-empty bucket. When inserting a new element with a priority smaller than L, the data structure sets L to the new priority, and when removing the last element from a bucket with priority L, it performs a sequential search through larger indexes until finding a non-empty bucket and setting L to the priority of the resulting bucket.

In either of these two variations, each sequential search takes time proportional to the difference between the old and new values of L. This could be significantly faster than the *O*(*C*) time bound for the searches in the un-optimized version of the data structure. In many applications of priority queues such as Dijkstra's algorithm, the minimum priorities form a monotonic sequence, allowing a monotone priority queue to be used. In these applications, for both the lazy and eager variations of the optimized structure, the sequential searches for non-empty buckets cover disjoint ranges of buckets. Because each bucket is in at most one of these ranges, their numbers of steps add to at most C. Therefore, in these applications, the total time for a sequence of n operations is *O*(*n* + *C*), rather than the slower *O*(*nC*) time bound that would result without this optimization. A corresponding optimization can be applied in applications where a bucket queue is used to find elements of maximum priority, but in this case it should maintain an index that upper-bounds the maximum priority, and the sequential search for a non-empty bucket should proceed downwards from this upper bound.

Another optimization (already given by Dial 1969) can be used to save space when the priorities are monotonic and, throughout the course of an algorithm, always fall within a range of r values rather than extending over the whole range from 0 to C. In this case, one can index the array by the priorities modulo r rather than by their actual values. The search for the minimum priority element should always begin at the previous minimum, to avoid priorities that are higher than the minimum but have lower moduli. In particular, this idea can be applied in Dijkstra's algorithm on graphs whose edge lengths are integers in the range from 1 to r.

Because creating a new bucket queue involves initializing an array of empty buckets, this initialization step takes time proportional to the number of priorities. A variation of the bucket queue described by Donald B. Johnson in 1981 instead stores only the non-empty buckets in a linked list, sorted by their priorities, and uses an auxiliary search tree to quickly find the position in this linked list for any new buckets. It takes time *O*(log log *C*) to initialize this variant structure, constant time to find an element with minimum or maximum priority, and time *O*(log log *D*) to insert or delete an element, where D is the difference between the nearest smaller and larger priorities to the priority of the inserted or deleted element.

### Example

For example, consider a bucket queue with four priorities, the numbers 0, 1, 2, and 3. It consists of an array A whose four cells each contain a collection of elements, initially empty. For the purposes of this example, A can be written as a bracketed sequence of four sets: $A=[\emptyset ,\emptyset ,\emptyset ,\emptyset ]$ . Consider a sequence of operations in which we insert two elements x and y with the same priority 1, insert a third element z with priority 3, change the priority of x to 3, and then perform two extractions of the minimum-priority element.

- After inserting x with priority 1, $A=[\emptyset ,\{x\},\emptyset ,\emptyset ]$ .
- After inserting y with priority 1, $A=[\emptyset ,\{x,y\},\emptyset ,\emptyset ]$ .
- After inserting z with priority 3, $A=[\emptyset ,\{x,y\},\emptyset ,\{z\}]$ .
- Changing the priority of x from 1 to three involves removing it from $A[1]$ and adding it to $A[3]$ , after which $A=[\emptyset ,\{y\},\emptyset ,\{x,z\}]$ .
- Extracting the minimum-priority element, in the basic version of the bucket queue, searches from the start of A to find its first non-empty element: $A[0]$ is empty but $A[1]=\{y\}$ , a non-empty set. It chooses an arbitrary element of this set (the only element, y ) as the minimum-priority element. Removing y from the structure leaves $A=[\emptyset ,\emptyset ,\emptyset ,\{x,z\}]$ .
- The second extract operation, in the basic version of the bucket queue, searches again from the start of the array: $A[0]=\emptyset$ , $A[1]=\emptyset$ , $A[2]=\emptyset$ , $A[3]={}$ non-empty. In the improved variants of the bucket queue, this search starts instead at the last position that was found to be non-empty, $A[1]$ . In either case, $A[3]=\{x,z\}$ is found to be the first non-empty set. One of its elements is chosen arbitrarily as the minimum-priority element; for example, z might be chosen. This element is removed, leaving $A=[\emptyset ,\emptyset ,\emptyset ,\{x\}]$ .

## Applications

### Graph degeneracy

A bucket queue can be used to maintain the vertices of an undirected graph, prioritized by their degrees, and repeatedly find and remove the vertex of minimum degree. This greedy algorithm can be used to calculate the degeneracy of a given graph, equal to the largest degree of any vertex at the time of its removal. The algorithm takes linear time, with or without the optimization that maintains a lower bound on the minimum priority, because each vertex is found in time proportional to its degree and the sum of all vertex degrees is linear in the number of edges of the graph.

### Dial's algorithm for shortest paths

In Dijkstra's algorithm for shortest paths in directed graphs with edge weights that are positive integers, the priorities are monotone, and a monotone bucket queue can be used to obtain a time bound of *O*(*m* + *dc*), where m is the number of edges, d is the diameter of the network, and c is the maximum (integer) link cost. This variant of Dijkstra's algorithm is also known as Dial's algorithm, after Robert B. Dial, who published it in 1969. The same idea also works, using a quantized bucket queue, for graphs with positive real edge weights when the ratio of the maximum to minimum weight is at most c. In this quantized version of the algorithm, the vertices are processed out of order, compared to the result with a non-quantized priority queue, but the correct shortest paths are still found. In these algorithms, the priorities will only span a range of width *c* + 1, so the modular optimization can be used to reduce the space to *O*(*n* + *c*).

A variant of the same algorithm can be used for the widest path problem. In combination with methods for quickly partitioning non-integer edge weights into subsets that can be assigned integer priorities, it leads to near-linear-time solutions to the single-source single-destination version of the widest path problem.

### Greedy set cover

The set cover problem has as its input a family of sets. The output should be a subfamily of these sets, with the same union as the original family, including as few sets as possible. It is NP-hard, but has a greedy approximation algorithm that achieves a logarithmic approximation ratio, essentially the best possible unless P = NP. This approximation algorithm selects its subfamily by repeatedly choosing a set that covers the maximum possible number of remaining uncovered elements. A standard exercise in algorithm design asks for an implementation of this algorithm that takes linear time in the input size, which is the sum of sizes of all the input sets.

This may be solved using a bucket queue of sets in the input family, prioritized by the number of remaining elements that they cover. Each time that the greedy algorithm chooses a set as part of its output, the newly covered set elements should be subtracted from the priorities of the other sets that cover them; over the course of the algorithm the number of these changes of priorities is just the sum of sizes of the input sets. The priorities are monotonically decreasing integers, upper-bounded by the number of elements to be covered. Each choice of the greedy algorithm involves finding the set with the maximum priority, which can be done by scanning downwards through the buckets of the bucket queue, starting from the most recent previous maximum value. The total time is linear in the input size.

### Scheduling

Bucket queues can be used to schedule tasks with deadlines, for instance in packet forwarding for internet data with quality of service guarantees. For this application, the deadlines should be quantized into discrete intervals, and tasks whose deadlines fall into the same interval are considered to be of equivalent priority.

A variation of the quantized bucket queue data structure, the calendar queue, has been applied to scheduling of discrete-event simulations, where the elements in the queue are future events prioritized by the time within the simulation that the events should happen. In this application, the ordering of events is critical, so the priorities cannot be approximated. Therefore, the calendar queue performs searches for the minimum-priority element in a different way than a bucket queue: in the bucket queue, any element of the first non-empty bucket may be returned, but instead the calendar queue searches all the elements in that bucket to determine which of them has the smallest non-quantized priority. To keep these searches fast, this variation attempts to keep the number of buckets proportional to the number of elements, by adjusting the scale of quantization and rebuilding the data structure when it gets out of balance. Calendar queues may be slower than bucket queues in the worst case (when many elements all land in the same smallest bucket) but are fast when elements are uniformly distributed among buckets causing the average bucket size to be constant.

### Fast marching

In applied mathematics and numerical methods for the solution of differential equations, untidy priority queues have been used to prioritize the steps of the fast marching method for solving boundary value problems of the Eikonal equation, used to model wave propagation. This method finds the times at which a moving boundary crosses a set of discrete points (such as the points of an integer grid) using a prioritization method resembling a continuous version of Dijkstra's algorithm, and its running time is dominated by its priority queue of these points. It can be sped up to linear time by rounding the priorities used in this algorithm to integers, and using a bucket queue for these integers. As in Dijkstra's and Dial's algorithms, the priorities are monotone, so fast marching can use the monotone optimization of the bucket queue and its analysis. However, the discretization introduces some error into the resulting calculations.
