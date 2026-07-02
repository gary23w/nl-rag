---
title: "Binary search (part 2/2)"
source: https://en.wikipedia.org/wiki/Binary_search
domain: algorithms
license: CC-BY-SA-4.0
tags: algorithm, sorting, complexity, big-o, dynamic programming
fetched: 2026-07-02
part: 2/2
---

## Library support

Many languages' standard libraries include binary search routines:

- C provides the function `bsearch()` in its standard library, which is typically implemented via binary search, although the official standard does not require it to do so.
- C++'s standard library provides the functions `binary_search()`, `lower_bound()`, `upper_bound()` and `equal_range()`. Using the C++20 `std::ranges` library, it can be applied over a range as `std::ranges::binary_search()`.
- D's standard library Phobos, in `std.range` module provides a type `SortedRange` (returned by `sort()` and `assumeSorted()` functions) with methods `contains()`, `equalRange()`, `lowerBound()` and `trisect()`, that use binary search techniques by default for ranges that offer random access.
- COBOL provides the `SEARCH ALL` verb for performing binary searches on COBOL ordered tables.
- Go's `sort` standard library package contains the functions `Search`, `SearchInts`, `SearchFloat64s`, and `SearchStrings`, which implement general binary search, as well as specific implementations for searching slices of integers, floating-point numbers, and strings, respectively.
- Java offers a set of overloaded `binarySearch()` static methods in the classes `Arrays` and `Collections` in the standard `java.util` package for performing binary searches on Java arrays and on `List`s, respectively.
- Microsoft's .NET Framework 2.0 offers static generic versions of the binary search algorithm in its collection base classes. An example would be `System.Array`'s method `BinarySearch<T>(T[] array, T value)`.
- For Objective-C, the Cocoa framework provides the `NSArray -indexOfObject:inSortedRange:options:usingComparator:` method in Mac OS X 10.6+. Apple's Core Foundation C framework also contains a `CFArrayBSearchValues()` function.
- Python provides the `bisect` module that keeps a list in sorted order without having to sort the list after each insertion.
- Ruby's Array class includes a `bsearch` method with built-in approximate matching.
- Rust's slice primitive provides `binary_search()`, `binary_search_by()`, `binary_search_by_key()`, and `partition_point()`.
