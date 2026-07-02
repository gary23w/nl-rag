---
title: "Bitonic tour"
source: https://en.wikipedia.org/wiki/Bitonic_tour
domain: held-karp-exact
license: CC-BY-SA-4.0
tags: held karp algorithm, traveling salesman exact, bitmask dynamic programming, subset states
fetched: 2026-07-02
---

# Bitonic tour

In computational geometry, a **bitonic tour** of a set of point sites in the Euclidean plane is a closed polygonal chain that has each site as one of its vertices, such that any vertical line crosses the chain at most twice.

## Optimal bitonic tours

The **optimal bitonic tour** is a bitonic tour of minimum total length. It is a standard exercise in dynamic programming to devise a polynomial time algorithm that constructs the optimal bitonic tour. Although the usual method for solving it in this way takes time $O(n^{2})$ , a faster algorithm with time $O(n\log ^{2}n)$ is known.

The problem of constructing optimal bitonic tours is often credited to Jon L. Bentley, who published in 1990 an experimental comparison of many heuristics for the traveling salesman problem; however, Bentley's experiments do not include bitonic tours. The first publication that describes the bitonic tour problem appears to be a different 1990 publication, the first edition of the textbook *Introduction to Algorithms* by Thomas H. Cormen, Charles E. Leiserson, and Ron Rivest, which lists Bentley as the originator of the problem.

## Properties

The optimal bitonic tour has no self-crossings, because any two edges that cross can be replaced by an uncrossed pair of edges with shorter total length due to the triangle inequality. Therefore, it forms a polygonalization of the input.

When compared to other tours that might not be bitonic, the optimal bitonic tour is the one that minimizes the total amount of horizontal motion, with ties broken by Euclidean distance.

For points in the plane with distinct integer x -coordinates and with real-number y -coordinates that lie within an interval of length $2{\sqrt {2}}$ or less, the optimal bitonic tour is an optimal traveling salesperson tour.

## Other optimization criteria

The same dynamic programming algorithm that finds the optimal bitonic tour may be used to solve other variants of the traveling salesman problem that minimize lexicographic combinations of motion in a fixed number of coordinate directions.

At the 5th International Olympiad in Informatics, in Mendoza, Argentina in 1993, one of the contest problems involved bitonic tours: the contestants were to devise an algorithm that took as input a set of sites and a collection of allowed edges between sites and construct a bitonic tour using those edges that included as many sites as possible. As with the optimal bitonic tour, this problem may be solved by dynamic programming.
