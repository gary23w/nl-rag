---
title: "Judy array"
source: https://en.wikipedia.org/wiki/Judy_array
domain: radix-patricia-tree
license: CC-BY-SA-4.0
tags: radix tree, patricia trie, compressed trie, bitwise trie
fetched: 2026-07-02
---

# Judy array

In computer science, a **Judy array** is an early-2000s Hewlett-Packard hand-optimized implementation of a 256-ary radix tree that uses many situational node types to reduce latency from CPU cache-line fills. As a compressed radix tree, a Judy array can store potentially sparse integer- or string-indexed data with comparatively low memory usage and low read latency, without relying on hashing or tree balancing, and without sacrificing in-order traversal. Per-operation latency scales as $O(\log n)$ —as expected of a tree—and the leading constant factor is small enough that Judy arrays are suitable even to the peta-element range. When applicable, they can be faster than implementations of AVL trees, B-trees, hash tables, or skip lists from the same time period.

## History

The Judy array was invented by Douglas Baskins over the years leading up to 2002 and named after his sister.

## Node types

Broadly, tree nodes in Judy arrays fall into one of three categories, though the implementation uses situational variations within each category:

- A **linear** node is a short, fixed-capacity, array-based association list meant to fit in one cache line. That is, such a node has an array of key bytes and a parallel array of values or pointers. Lookup is by linear search over the key array and then random access to the corresponding index in the value/pointer array.
- A **bitmap** node is a size-256 bitvector tracking which values/children are present and then a sorted list of corresponding values or pointers. Lookup is by population count of the bits up to the target index and then random access to the corresponding entry in the value/pointer array. The bitmap fits within a typical CPU cache line, and random access only loads one cache line from the sorted list, so for reading these nodes require at most two cache-line fills.
- An **uncompressed** node is a conventional trie node as an array of values/pointers. Lookup is by random access using the key byte as an index, which at the CPU level requires visiting one cache line.

Linear nodes are used for low branching, bitmap nodes for intermediate branching, and uncompressed nodes for high branching.

## Advantages and disadvantages

Due to cache optimizations, Judy arrays are fast, especially for very large datasets. On certain tasks involving data that are sequential or nearly sequential, Judy arrays can even outperform hash tables, since, unlike hash tables, the internal tree structure of Judy arrays maintains the ordering of the keys.

On the other hand, Judy arrays are not suitable for all key types, rely heavily on compile-time case-splitting (which increases both the compiled code size and the work involved in retuning for a new architecture), make some concessions to older architectures that may not be relevant to modern machines, and do not exploit SIMD. They are optimized for read performance over write performance.
