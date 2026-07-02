---
title: "C++ Standard Library"
source: https://en.wikipedia.org/wiki/C%2B%2B_Standard_Library
domain: abseil-cpp-lib
license: CC-BY-SA-4.0
tags: abseil library, cpp common libraries, abseil augmented standard library, abseil flat hash map
fetched: 2026-07-02
---

# C++ Standard Library

In the C++ programming language, the **C++ Standard Library** is a collection of classes and functions, which are written in the core language and part of the C++ ISO Standard itself.

## Overview

The C++ Standard Library provides several generic containers, functions to use and manipulate these containers, function objects, generic strings and streams (including interactive and file I/O), support for some language features, and functions for common tasks such as finding the square root of a number. The C++ Standard Library also incorporates most headers of the ISO C standard library ending with ".h", but their use was deprecated (reverted the deprecation since C++23). C++23 instead considers these headers as useful for interoperability with C, and recommends against their usage outside of programs that are intended to be both valid C and C++ programs. No other headers in the C++ Standard Library end in ".h". Features of the C++ Standard Library are declared within the `std` namespace.

The C++ Standard Library is based upon conventions introduced by the Standard Template Library (STL), and has been influenced by research in generic programming and developers of the STL such as Alexander Stepanov and Meng Lee. Although the C++ Standard Library and the STL share many features, neither is a strict superset of the other. The design of the C++ standard library, much like the C standard library, is minimalistic, and contains only core features for programming, lacking most of the more specialised features offered by the Java standard library or C# standard library. For more features, some third-party libraries such as Boost libraries and POCO C++ Libraries, which offer additional features, may be used to supplement the standard library. An implementation for a C++ standard library header is described as "freestanding" if the execution of the program does not rely on an operating system.

A noteworthy feature of the C++ Standard Library is that it not only specifies the syntax and semantics of generic algorithms, but also places requirements on their performance. These performance requirements often correspond to a well-known algorithm, which is expected but not required to be used. In most cases this requires linear time O(*n*) or linearithmic time O(*n* log *n*), but in some cases higher bounds are allowed, such as quasilinear time O(*n* log2 *n*) for stable sort (to allow in-place merge sort). Previously, sorting was only required to take O(*n* log *n*) on average, allowing the use of quicksort, which is fast in practice but has poor worst-case performance, but introsort was introduced to allow both fast average performance and optimal worst-case complexity, and as of C++11, sorting is guaranteed to be at worst linearithmic. In other cases requirements remain laxer, such as selection, which is only required to be linear on average (as in quickselect), not requiring worst-case linear as in introselect.

The C++ Standard Library underwent ISO standardization as part of the C++ ISO Standardization effort in the 1990s. Since 2011, it has been expanded and updated every three years with each revision of the C++ standard.

C++20 specifies the introduction of standard library header units, and C++23 adds full module support for the standard library.

## Implementations

| Name | Organization | Homepage | Acronym | Licence | Latest release |
|---|---|---|---|---|---|
| GNU C++ Standard Library | GNU Project and Free Software Foundation |   | libstdc++ | GPLv3 with GCC Runtime Library Exception | New major release once per year |
| LLVM C++ Standard Library | LLVM Developer Group |   | libc++ | Apache License 2.0 with LLVM Exceptions | Every 2 weeks |
| NVIDIA C++ Standard Library | Nvidia |   | libcudacxx | Apache License 2.0 with LLVM Exceptions | September 4, 2024 (2024-09-04) |
| Microsoft C++ Standard Library | Microsoft |   | MSVC STL | Apache License 2.0 with LLVM Exceptions | Daily |
| HPX C++ Standard Library for Parallelism and Concurrency | STELLAR Group |   | HPX | Boost Software License 1.0 | June 29, 2025 (2025-06-29) |
| Electronic Arts Standard Template Library | Electronic Arts |   | EASTL | BSD 3-Clause License | October 2, 2025 (2025-10-02) |
| Dinkum C++ Library | Dinkumware | Archived 11 February 2021 at the Wayback Machine | Unknown | Commercial | Unknown |
| Cray C++ Standard Library | Cray User Group |   | Unknown | Commercial | Unknown |

### Discontinued

#### Apache C++ Standard Library

The Apache C++ Standard Library is another open-source implementation. It was originally developed commercially by Rogue Wave Software and later donated to the Apache Software Foundation. However, after more than five years without a release, the board of the Apache Software Foundation decided to end this project and move it to Apache Attic.
