---
title: "Beap"
source: https://en.wikipedia.org/wiki/Beap
domain: specialty-heap-zoo
license: CC-BY-SA-4.0
tags: soft heap, kinetic heap, weak heap, mergeable heap, calendar queue
fetched: 2026-07-02
---

# Beap

A **beap**, or **bi-parental heap**, is a data structure for a set (or map, or multiset or multimap) that enables elements (or mappings) to be located, inserted, or deleted in sublinear time. In a beap, each element is stored in a node with up to two parents and up to two children, with the property that the value of a parent node is never greater than the value of either of its children.

Beaps are implemented using an array containing only the values to be stored, with the parent-child relationships being determined implicitly by the array indices. (That is: beaps are an implicit data structure.) In that respect they are similar to binary heaps, which are usually implemented that way as well. However, their performance characteristics are different from heaps; in particular, a beap enables sublinear retrieval of arbitrary elements.

The beap was introduced by Ian Munro and Hendra Suwanda. A related data structure is the Young tableau.

## Performance

The height of the structure is approximately ${\sqrt {n}}$ . Also, assuming the last level is full, the number of elements on that level is also ${\sqrt {n}}$ . In fact, because of these properties all basic operations (insert, remove, find) run in $O({\sqrt {n}})$ time on average. Find operations in the heap can be $O(n)$ in the worst case. Removal and insertion of new elements involves propagation of elements up or down (much like in a heap) in order to restore the beap invariant. An additional perk is that beap provides constant time access to the smallest element and $O({\sqrt {n}})$ time for the maximum element.

Actually, a $O({\sqrt {n}})$ find operation can be implemented if parent pointers at each node are maintained. You would start at the absolute bottom-most element of the top node (similar to the left-most child in a heap) and move either up or right to find the element of interest.

## Applications
