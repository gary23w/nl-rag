---
title: "Bounding sphere"
source: https://en.wikipedia.org/wiki/Bounding_sphere
domain: minimum-enclosing-circle
license: CC-BY-SA-4.0
tags: smallest enclosing circle, welzl algorithm, bounding sphere, minimum enclosing ball
fetched: 2026-07-02
---

# Bounding sphere

In mathematics, given a non-empty set of objects of finite extension in d -dimensional space, for example a set of points, a **bounding sphere**, **enclosing sphere** or **enclosing ball** for that set is a d -dimensional solid sphere containing all of these objects.

Used in computer graphics and computational geometry, a bounding sphere is a special type of bounding volume. There are several fast and simple bounding sphere construction algorithms with a high practical value in real-time computer graphics applications.

In statistics and operations research, the objects are typically points, and generally the sphere of interest is the **minimal bounding sphere**, that is, the sphere with minimal radius among all bounding spheres. It may be proven that such a sphere is unique: If there are two of them, then the objects in question lie within their intersection. But an intersection of two non-coinciding spheres of equal radius is contained in a sphere of smaller radius.

The problem of computing the center of a minimal bounding sphere is also known as the "unweighted Euclidean 1-center problem".

## Applications

### Clustering

Such spheres are useful in clustering, where groups of similar data points are classified together.

In statistical analysis the scattering of data points within a sphere may be attributed to measurement error or natural (usually thermal) processes, in which case the cluster represents a perturbation of an ideal point. In some circumstances this ideal point may be used as a substitute for the points in the cluster, advantageous in reducing calculation time.

In operations research the clustering of values to an ideal point may also be used to reduce the number of inputs in order to obtain approximate values for NP-hard problems in a reasonable time. The point chosen is not usually the center of the sphere, as this can be biased by outliers, but instead some form of average location such as a least squares point is computed to represent the cluster.

## Algorithms

There are exact and approximate algorithms for solving the bounding sphere problem.

### Linear programming

Nimrod Megiddo studied the 1-center problem extensively and published on it at least five times in the 1980s. In 1983, he proposed a "prune and search" algorithm which finds the optimum bounding sphere and runs in linear time if the dimension is fixed as a constant. When the dimension d is taken into account, the execution time complexity is $O(2^{O(d^{2})}n)$ , which is impractical for high-dimensional applications.

In 1991, Emo Welzl proposed a much simpler randomized algorithm, generalizing a randomized linear programming algorithm by Raimund Seidel. The expected running time of Welzl's algorithm is $O((d+1)(d+1)!\ n)$ , which again reduces to $O(n)$ for any fixed dimension d . The paper provides experimental results demonstrating its practicality in higher dimensions. A more recent deterministic algorithm of Timothy Chan runs in $O(d^{\left({\frac {1}{2}}+o(1)\right)d}n)$ , again reducing to $O(n)$ time with fixed dimension, with a smaller, but still exponential, dependence on the dimension.

The open-source Computational Geometry Algorithms Library (CGAL) contains an implementation of Welzl's algorithm.

### Second order cone programming

The smallest enclosing sphere of a finite point set can also be computed using convex optimization, specifically second-order cone programming (SOCP). This approach formulates the problem as minimizing the radius of a sphere subject to second-order (quadratic) constraints that require each point to lie within or on the sphere. Explicitly, the optimization problem is:

minimize:

r

subject to: ||

x

i

−

c

||₂ ≤

r

, for all

i

where the center *c* and radius *r* are the optimization variables, and *x*i are the input points.

This formulation defines a convex optimization problem that can be solved efficiently using modern interior-point methods and SOCP solvers. While this approach provides an exact mathematical formulation, the solution is typically computed to high numerical accuracy rather than exact machine precision. As such, it offers a practical alternative to geometric algorithms, especially in higher dimensions or when integrating with other optimization-based methods.

This convex formulation is discussed in sources such as Boyd & Vandenberghe's convex optimization book, and is widely supported in convex optimization software such as CVX, CVXPY, and MOSEK.

### Ritter's bounding sphere

In 1990, Jack Ritter proposed a simple algorithm to find a non-minimal bounding sphere. It is widely used in various applications for its simplicity. The algorithm works in this way:

1. Pick a point x from P , search a point y in P , which has the largest distance from x ;
2. Search a point z in P , which has the largest distance from y . Set up an initial ball B , with its centre as the midpoint of y and z , the radius as half of the distance between y and z ;
3. If all points in P are within ball B , then we get a bounding sphere. Otherwise, let p be a point outside the ball, constructs a new ball covering both point p and previous ball. Repeat this step until all points are covered.

Ritter's algorithm runs in time $O(nd)$ on inputs consisting of n points in d -dimensional space, which makes it very efficient. However, it gives only a coarse result which is usually 5% to 20% larger than the optimum.

### Core-set based approximation

Bădoiu et al. presented a $1+\varepsilon$ approximation to the bounding sphere problem, where a $1+\varepsilon$ approximation means that the constructed sphere has radius at most $(1+\varepsilon )r$ , where r is the smallest possible radius of a bounding sphere.

A coreset is a small subset, that a $1+\varepsilon$ expansion of the solution on the subset is a bounding sphere of the whole set. The coreset is constructed incrementally by adding the farthest point into the set in each iteration.

Kumar et al. improved this approximation algorithm so that it runs in time $O({\frac {nd}{\epsilon }}+{\frac {1}{\epsilon ^{4.5}}}\log {\frac {1}{\epsilon }})$ .

### Fischer's exact solver

Fischer et al. (2003) proposed an exact solver, though the algorithm does not have a polynomial running time in the worst case. The algorithm is purely combinatorial and implements a pivoting scheme similar to the simplex method for linear programming, used earlier in some heuristics. It starts with a large sphere that covers all points and gradually shrinks it until it cannot be shrunk further. The algorithm features correct termination rules in cases of degeneracies, overlooked by prior authors; and efficient handling of partial solutions, which produces a major speed-up. The authors verified that the algorithm is efficient in practice in low and moderately low (up to 10,000) dimensions and claim it does not exhibit numerical stability problems in its floating-point operations. A C++ implementation of the algorithm is available as an open-source project.

### Extremal points optimal sphere

Larsson (2008) proposed the "extremal points optimal sphere" method with controllable speed to accuracy approximation to solve the bounding sphere problem. This method works by taking a set of s direction vectors and projecting all points onto each vector in s ; s serves as a speed-accuracy trade-off variable. An exact solver is applied to the $2s$ extremal points of these projections. The algorithm then iterates over the remaining points, if any, growing the sphere if necessary. For large n this method is orders of magnitude faster than exact methods, while giving comparable results. It has a worst case time of $O(sn)$ .
