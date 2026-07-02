---
title: "UB-tree"
source: https://en.wikipedia.org/wiki/UB-tree
domain: b-tree-structure
license: CC-BY-SA-4.0
tags: b-tree, multiway search tree, disk-based index, database index tree
fetched: 2026-07-02
---

# UB-tree

The **UB-tree**, also known as the **Universal B-Tree**, as proposed by Rudolf Bayer and Volker Markl is a balanced tree for storing and efficiently retrieving multidimensional data. Like a B+ tree, information is stored only in the leaves. Records are stored according to Z-order, also called Morton order. Z-order is calculated by bitwise interlacing of the keys.

Insertion, deletion, and point query are done as with ordinary B+ trees. To perform range searches in multidimensional point data, however, an algorithm must be provided for calculating, from a point encountered in the data base, the next Z-value which is in the multidimensional search range.

The original algorithm to solve this key problem was exponential with the dimensionality and thus not feasible ("GetNextZ-address"). A solution to this "crucial part of the UB-tree range query" has been described later. This method has already been described in an older paper where using Z-order with search trees has first been proposed.
