---
title: "Klee–Minty cube"
source: https://en.wikipedia.org/wiki/Klee–Minty_cube
domain: simplex-method-pivoting
license: CC-BY-SA-4.0
tags: simplex method, pivot rule, bland rule, revised simplex
fetched: 2026-07-02
---

# Klee–Minty cube

The **Klee–Minty cube** or **Klee–Minty polytope** (named after Victor Klee and George J. Minty) is a unit hypercube of variable dimension whose corners have been perturbed. Klee and Minty demonstrated that George Dantzig's simplex algorithm has poor worst-case performance when initialized at one corner of their "squashed cube". On the three-dimensional version, the simplex algorithm and the criss-cross algorithm visit all 8 corners in the worst case.

In particular, many optimization algorithms for linear optimization exhibit poor performance when applied to the Klee–Minty cube. In 1973 Klee and Minty showed that Dantzig's simplex algorithm was not a polynomial-time algorithm when applied to their cube. Later, modifications of the Klee–Minty cube have shown poor behavior both for other basis-exchange pivoting algorithms and also for interior-point algorithms.

## Description

The Klee–Minty cube was originally specified with a parameterized system of linear inequalities, with the dimension as the parameter. The cube in two-dimensional space is a *squashed square*, and the "cube" in three-dimensional space is a *squashed cube*. Illustrations of the "cube" have appeared besides algebraic descriptions. The Klee–Minty polytope is given by: ${\begin{aligned}x_{1}&\leq 5\\4x_{1}+x_{2}&\leq 25\\8x_{1}+4x_{2}+x_{3}&\leq 125\\&\vdots \\2^{D}x_{1}+2^{D-1}x_{2}+\dots +4x_{D-1}+x_{D}&\leq 5^{D}\\x_{1}\geq 0,\,\,\dots ,\,\,x_{D}&\geq 0.\end{aligned}}$

This has D variables, D constraints other than the D non-negativity constraints, and $2^{D}$ vertices, just as a D -dimensional hypercube does. If the objective function to be maximized is $2^{D-1}x_{1}+2^{D-2}x_{2}+\dots +2x_{D-1}+x_{D},$ and if the initial vertex for the simplex algorithm is the origin, then the algorithm as formulated by Dantzig visits all $2^{D}$ vertices, finally reaching the optimal vertex $(0,0,\dots ,5^{D})$ .

## Computational complexity

The Klee–Minty cube has been used to analyze the performance of many algorithms, both in the worst case and on average. The time complexity of an algorithm counts the number of arithmetic operations sufficient for the algorithm to solve the problem. For example, Gaussian elimination requires the order of $D^{3}$ operations, and so it is said to have polynomial time-complexity because its complexity is bounded by a cubic polynomial. There are examples of algorithms that do not have polynomial-time complexity. For example, a generalization of Gaussian elimination called Buchberger's algorithm has for its complexity an exponential function of the problem data (the degree of the polynomials and the number of variables of the multivariate polynomials). Because exponential functions eventually grow much faster than polynomial functions, an exponential complexity implies that an algorithm has slow performance on large problems.

### Worst case

In mathematical optimization, the Klee–Minty cube is an example that shows the worst-case computational complexity of many algorithms of linear optimization. It is a deformed cube with exactly  2*D* corners in dimension D . Klee and Minty showed that Dantzig's simplex algorithm visits all corners of a (perturbed) cube in dimension D in the worst case.

Modifications of the Klee–Minty construction showed similar exponential time complexity for other pivoting rules of simplex type, which maintain primal feasibility, such as Bland's rule. Another modification showed that the criss-cross algorithm, which does not maintain primal feasibility, also visits all the corners of a modified Klee–Minty cube. Like the simplex algorithm, the criss-cross algorithm visits all 8 corners of the three-dimensional cube in the worst case.

#### Path-following algorithms

Further modifications of the Klee–Minty cube have shown the poor performance of central-path–following algorithms for linear optimization, in that the central path comes arbitrarily close to each of the corners of a cube. This "vertex-stalking" performance is surprising because such path-following algorithms have polynomial-time complexity for linear optimization.

### Average case

The Klee–Minty cube has also inspired research on average-case complexity. When eligible pivots are made randomly (and not by the rule of steepest descent), Dantzig's simplex algorithm needs on average quadratically many steps (on the order of $O(D^{2})$ . Standard variants of the simplex algorithm take on average D steps for a cube. However according to Fukuda & Namiki (1994), when it is initialized at a random corner of the cube, the criss-cross algorithm visits only D additional corners. Both the simplex algorithm and the criss-cross algorithm visit exactly 3 additional corners of the three-dimensional cube on average.
