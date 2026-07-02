---
title: "Sorted array"
source: https://en.wikipedia.org/wiki/Sorted_array
domain: interpolation-search-algorithm
license: CC-BY-SA-4.0
tags: interpolation search, binary search, uniform distribution, sorted array
fetched: 2026-07-02
---

# Sorted array

A **sorted array** is an array data structure in which each element is sorted in numerical, alphabetical, or some other order, and placed at equally spaced addresses in computer memory. It is typically used in computer science to implement static lookup tables to hold multiple values which have the same data type. Sorting an array is useful in organising data in ordered form and recovering them rapidly.

## Overview

Sorted arrays are the most space-efficient data structure with the best locality of reference for sequentially stored data.

Elements within a sorted array are found using a binary search, in O(log *n*); thus sorted arrays are suited for cases when one needs to be able to look up elements quickly, e.g. as a set or multiset data structure. This complexity for lookups is the same as for self-balancing binary search trees.

In some data structures, an array of structures is used. In such cases, the same sorting methods can be used to sort the structures according to some key as a structure element; for example, sorting records of students according to roll numbers or names or grades.

If one is using a sorted dynamic array, then it is possible to insert and delete elements. The insertion and deletion of elements in a sorted array executes at O(*n*), due to the need to shift all the elements following the element to be inserted or deleted; in comparison a self-balancing binary search tree inserts and deletes at O(log *n*). In the case where elements are deleted or inserted at the end, a sorted dynamic array can do this in amortized O(1) time while a self-balancing binary search tree always operates at O(log *n*).

Elements in a sorted array can be looked up by their index (random access) at O(1) time, an operation taking O(log *n*) or O(*n*) time for more complex data structures.

## History

John von Neumann wrote the first array sorting program (merge sort) in 1945, when the first stored-program computer was still being built.
