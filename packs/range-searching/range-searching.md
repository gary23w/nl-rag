---
title: "Range searching"
source: https://en.wikipedia.org/wiki/Range_searching
domain: range-searching
license: CC-BY-SA-4.0
tags: range searching, orthogonal range query, kd tree query, fractional cascading
fetched: 2026-07-02
---

# Range searching

In computer science, the **range searching** problem consists of processing a set *S* of objects, in order to determine which objects from *S* intersect with a query object, called the *range*. For example, if *S* is a set of points corresponding to the coordinates of several cities, find the subset of cities within a given range of latitudes and longitudes.

The range searching problem and the data structures that solve it are a fundamental topic of computational geometry. Applications of the problem arise in areas such as geographical information systems (GIS), computer-aided design (CAD) and databases.

## Variations

There are several variations of the problem, and different data structures may be necessary for different variations. In order to obtain an efficient solution, several aspects of the problem need to be specified:

- Object types: Algorithms depend on whether *S* consists of points, lines, line segments, boxes, polygons.... The simplest and most studied objects to search are points.
- Range types: The query ranges also need to be drawn from a predetermined set. Some well-studied sets of ranges, and the names of the respective problems are axis-aligned rectangles (orthogonal range searching), simplices, halfspaces, and spheres/circles.
- Query types: If the list of all objects that intersect the query range must be reported, the problem is called range reporting, and the query is called a *reporting query*. Sometimes, only the number of objects that intersect the range is required. In this case, the problem is called *range counting*, and the query is called a *counting query*. The *emptiness query* reports whether there is at least one object that intersects the range. In the *semigroup version*, a commutative semigroup (**S**,+) is specified, each point is assigned a weight from **S**, and it is required to report the semigroup sum of the weights of the points that intersect the range.
- Dynamic range searching vs. static range searching: In the static setting the set *S* is known in advance. In dynamic setting objects may be inserted or deleted between queries.
- Offline range searching: Both the set of objects and the whole set of queries are known in advance.

## Data structures

### Orthogonal range searching

In orthogonal range searching, the set *S* consists of n points in d dimensions, and the query consists of intervals in each of those dimensions. Thus, the query consists of a multi-dimensional axis-aligned rectangle. With an output size of k , Jon Bentley used a k-d tree to achieve (in Big O notation) $O(n)$ space and $O{\big (}n^{1-{\frac {1}{d}}}+k{\big )}$ query time. Bentley also proposed using range trees, which improved query time to $O(\log ^{d}n+k)$ but increased space to $O(n\log ^{d-1}n)$ . Dan Willard used downpointers, a special case of fractional cascading to reduce the query time further to $O(\log ^{d-1}n+k)$ .

While the above results were achieved in the pointer machine model, further improvements have been made in the word RAM model of computation in low dimensions (2D, 3D, 4D). Bernard Chazelle used compress range trees to achieve $O(\log n)$ query time and $O(n)$ space for range counting. Joseph JaJa and others later improved this query time to $O\left({\dfrac {\log n}{\log \log n}}\right)$ for range counting, which matches a lower bound and is thus asymptotically optimal.

As of 2015, the best results (in low dimensions (2D, 3D, 4D)) for range reporting found by Timothy M. Chan, Kasper Larsen, and Mihai Pătrașcu, also using compressed range trees in the word RAM model of computation, are one of the following:

- $O(n)$ space, $O(\log ^{\epsilon }n+k\log ^{\epsilon }n)$ query time
- $O(n\log \log n)$ space, $O(\log \log n+k\log \log n)$ query time
- $O(n\log ^{\epsilon }n)$ space, $O(\log \log n+k)$ query time

In the orthogonal case, if one of the bounds is infinity, the query is called three-sided. If two of the bounds are infinity, the query is two-sided, and if none of the bounds are infinity, then the query is four-sided.

### Dynamic range searching

While in static range searching the set *S* is known in advance, dynamic range searching, insertions and deletions of points are allowed. In the incremental version of the problem, only insertions are allowed, whereas the decremental version only allows deletions. For the orthogonal case, Kurt Mehlhorn and Stefan Näher created a data structure for dynamic range searching which uses dynamic fractional cascading to achieve $O(n\log n)$ space and $O(\log n\log \log n+k)$ query time. Both incremental and decremental versions of the problem can be solved with $O(\log n+k)$ query time, but it is unknown whether general dynamic range searching can be done with that query time.

### Colored range searching

The problem of colored range counting considers the case where points have categorical attributes. If the categories are considered as colors of points in geometric space, then a query is for how many colors appear in a particular range. Prosenjit Gupta and others described a data structure in 1995 which solved 2D orthogonal colored range counting in $O(n^{2}\log ^{2}n)$ space and $O(\log ^{2}n)$ query time. This was later on generalized to higher dimensions.

## Applications

In addition to being considered in computational geometry, range searching, and orthogonal range searching in particular, has applications for range queries in databases. Colored range searching is also used for and motivated by searching through categorical data. For example, determining the rows in a database of bank accounts which represent people whose age is between 25 and 40 and who have between $10000 and $20000 might be an orthogonal range reporting problem where age and money are two dimensions.
