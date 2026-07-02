---
title: "1-center problem"
source: https://en.wikipedia.org/wiki/1-center_problem
domain: minimum-enclosing-circle
license: CC-BY-SA-4.0
tags: smallest enclosing circle, welzl algorithm, bounding sphere, minimum enclosing ball
fetched: 2026-07-02
---

# 1-center problem

The **1-center problem**, also known as **minimax problem** or **minmax location problem**, is a classical combinatorial optimization problem in operations research of facilities location type. In its most general case the problem is stated as follows: given a set of *n* demand points, a space of feasible locations of a facility and a function to calculate the transportation cost between a facility and any demand point, find a location of the facility which minimizes the maximum facility-demand point transportation cost.

There are numerous particular cases of the problem, depending on the choice of the locations both of demand points and facilities, as well as the distance function.

A simple special case is when the feasible locations and demand points are in the plane with Euclidean distance as transportation cost (**planar minmax Euclidean facility location problem, Euclidean 1-center problem in the plane,** etc.). It is also known as the smallest circle problem. Its generalization to *n*-dimensional Euclidean spaces is known as the smallest enclosing ball problem. A further generalization (**weighted Euclidean facility location**) is when the set of weights is assigned to demand points and the transportation cost is the sum of the products of distances by the corresponding weights. Another special case, the closest string problem, arises when the inputs are strings and their distance is measured using Hamming distance.

The 1-center problem can be restated as finding a star in a weighted complete graph that minimizes the maximum weight of the selected edges. The corresponding problem of minimizing the maximum weight of a path between two selected vertices, in place of a star, is called the minimax path problem.
