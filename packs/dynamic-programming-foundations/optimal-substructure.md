---
title: "Optimal substructure"
source: https://en.wikipedia.org/wiki/Optimal_substructure
domain: dynamic-programming-foundations
license: CC-BY-SA-4.0
tags: dynamic programming, memoization technique, optimal substructure, bellman equation
fetched: 2026-07-02
---

# Optimal substructure

In computer science, a problem is said to have **optimal substructure** if an optimal solution can be constructed from optimal solutions of its subproblems. This property is used to determine the usefulness of greedy algorithms for a problem.

Typically, a greedy algorithm is used to solve a problem with optimal substructure if it can be proven by induction that this is optimal at each step. Otherwise, provided the problem exhibits overlapping subproblems as well, divide-and-conquer methods or dynamic programming may be used. If there are no appropriate greedy algorithms and the problem fails to exhibit overlapping subproblems, often a lengthy but straightforward search of the solution space is the best alternative.

In the application of dynamic programming to mathematical optimization, Richard Bellman's Principle of Optimality is based on the idea that in order to solve a dynamic optimization problem from some starting period *t* to some ending period *T*, one implicitly has to solve subproblems starting from later dates *s*, where *t<s<T*. This is an example of optimal substructure. The Principle of Optimality is used to derive the Bellman equation, which shows how the value of the problem starting from *t* is related to the value of the problem starting from *s*.

## Example

Consider finding a shortest path for traveling between two cities by car, as illustrated in Figure 1. Such an example is likely to exhibit optimal substructure. That is, if the shortest route from Seattle to Los Angeles passes through Portland and then Sacramento, then the shortest route from Portland to Los Angeles must pass through Sacramento too. That is, the problem of how to get from Portland to Los Angeles is nested inside the problem of how to get from Seattle to Los Angeles. (The wavy lines in the graph represent solutions to the subproblems.)

As an example of a problem that is unlikely to exhibit optimal substructure, consider the problem of finding the cheapest airline ticket from Buenos Aires to Moscow. Even if that ticket involves stops in Miami and then London, we can't conclude that the cheapest ticket from Miami to Moscow stops in London, because the price at which an airline sells a multi-flight trip is usually not the sum of the prices at which it would sell the individual flights in the trip.

## Definition

A slightly more formal definition of optimal substructure can be given. Let a "problem" be a collection of "alternatives", and let each alternative have an associated cost, *c*(*a*). The task is to find a set of alternatives that minimizes *c*(*a*). Suppose that the alternatives can be partitioned into subsets, i.e. each alternative belongs to only one subset. Suppose each subset has its own cost function. The minima of each of these cost functions can be found, as can the minima of the global cost function, *restricted to the same subsets*. If these minima match for each subset, then it's almost obvious that a global minimum can be picked not out of the full set of alternatives, but out of only the set that consists of the minima of the smaller, local cost functions we have defined. If minimizing the local functions is a problem of "lower order", and (specifically) if, after a finite number of these reductions, the problem becomes trivial, then the problem has an optimal substructure.

## Problems with optimal substructure

- Longest common subsequence problem
- Longest increasing subsequence
- Longest palindromic substring
- All-Pairs Shortest Path
- Any problem that can be solved by dynamic programming.

## Problems *without* optimal substructure

- Longest path problem
- Addition-chain exponentiation
- *Least-cost airline fare.* Using online flight search, we will frequently find that the cheapest flight from airport A to airport B involves a single connection through airport C, but the cheapest flight from airport A to airport C involves a connection through some other airport D. However, if the problem takes the maximum number of layovers as a parameter, then the problem has optimal substructure. The cheapest flight from A to B that involves at most *k* layovers is either the direct flight; or the cheapest flight from A to some airport C that involves at most *t* layovers for some integer *t* with *0≤t<k*, plus the cheapest flight from C to B that involves at most *k−1−t* layovers.
