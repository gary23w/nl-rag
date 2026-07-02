---
title: "Boolean operations on polygons"
source: https://en.wikipedia.org/wiki/Boolean_operations_on_polygons
domain: sweep-line-paradigm
license: CC-BY-SA-4.0
tags: sweep line algorithm, event queue, plane sweep, status structure
fetched: 2026-07-02
---

# Boolean operations on polygons

**Boolean operations on polygons** are a set of Boolean operations (AND, OR, NOT, XOR, ...) operating on one or more sets of polygons in computer graphics. These sets of operations are widely used in computer graphics, CAD, and in EDA (in integrated circuit physical design and verification software). These are also used for activities like rapid prototyping in product design, medical device development, or even the creation of elaborate artworks.

## Algorithms

- Greiner–Hormann clipping algorithm
- Vatti clipping algorithm
- Sutherland–Hodgman algorithm (special case algorithm)
- Weiler–Atherton clipping algorithm (special case algorithm)

## Uses in software

Early algorithms for Boolean operations on polygons were based on the use of bitmaps. Using bitmaps in modeling polygon shapes has many drawbacks. One of the drawbacks is that the memory usage can be very large, since the resolution of polygons is proportional to the number of bits used to represent polygons. The higher the resolution is desired, the more the number of bits is required.

Modern implementations for Boolean operations on polygons tend to use plane sweep algorithms (or Sweep line algorithms). A list of papers using plane sweep algorithms for Boolean operations on polygons can be found in References below.

Boolean operations on convex polygons and monotone polygons of the same direction may be performed in linear time.
