---
title: "Kirkpatrick–Seidel algorithm"
source: https://en.wikipedia.org/wiki/Kirkpatrick–Seidel_algorithm
domain: gift-wrapping
license: CC-BY-SA-4.0
tags: gift wrapping algorithm, jarvis march, convex hull output, beneath beyond
fetched: 2026-07-02
---

# Kirkpatrick–Seidel algorithm

The **Kirkpatrick–Seidel algorithm** is an algorithm designed for computing the convex hull of a set of points in the plane, offering a time complexity of ${\mathcal {O}}(n\log h)$ , where n is the number of input points and h is the number of points on the convex hull. This output-sensitive time complexity implies that the algorithm’s running time depends on both the input size and the size of the output.

Earlier output-sensitive algorithms, such as the gift wrapping algorithm, exhibited asymptotic running times of ${\mathcal {O}}(nh)$ , while non-output-sensitive algorithms typically ran in ${\mathcal {O}}(n\log n)$ time. The Kirkpatrick–Seidel algorithm offers a significant improvement by achieving a more efficient asymptotic bound, making it faster for certain types of input.

Despite its theoretical optimality, the algorithm is not widely used in practice for moderate-sized data sets due to the implementation complexity and constants hidden in the asymptotic notation.

## Algorithm

The Kirkpatrick–Seidel algorithm is a refinement of the classical divide-and-conquer approach for computing convex hulls, often described as "marriage-before-conquest". In the traditional divide-and-conquer approach, the set of points is split into two halves (typically by a vertical line), the convex hull of each half is computed recursively, and the two hulls are merged by finding the "bridge" edges (bitangents) that connect them.

In contrast, the Kirkpatrick–Seidel algorithm first finds the median of the points’ x -coordinates and identifies the convex hull edges that intersect the vertical line at this median. Points that cannot contribute to the convex hull on either side of the median line are discarded. The algorithm then proceeds recursively on the remaining points to compute the upper and lower parts of the convex hull.

At each recursion level i , the algorithm solves at most $2^{i}$ subproblems, each containing at most $n/2^{i}$ points. Since each subproblem identifies a single edge of the convex hull, the total number of subproblems is bounded by h , the number of points on the hull. In the worst case, when no points can be discarded early, the recursion depth is ${\mathcal {O}}(\log h)$ , and each level processes ${\mathcal {O}}(n)$ points. This results in an overall time complexity of ${\mathcal {O}}(n\log h)$ .

## Recent Developments

Since its introduction, the Kirkpatrick–Seidel algorithm has inspired several developments in both theoretical and practical aspects of convex hull algorithms. Notably, recent advancements have focused on instance-optimality and universal optimality.

Instance-optimality: This concept relates to finding algorithms that are optimal for a specific set of instances, based on the distribution and geometry of the input points. Recent research has explored algorithms that adapt to specific input distributions and dynamically improve performance on typical data sets.

Universal optimality: This development seeks algorithms that are optimal for all types of inputs, providing a guaranteed worst-case performance across a broad range of input configurations. The Kirkpatrick–Seidel algorithm is a strong contender for universal optimality in two-dimensional convex hulls.

Quantum approaches: With the rise of quantum computing, there has been research into quantum algorithms for convex hulls, exploring whether quantum algorithms could outperform classical methods, including the Kirkpatrick–Seidel algorithm, in specific cases. The quantum speedup, however, is still an open area of research.

## Practical Evaluation

While the Kirkpatrick–Seidel algorithm is theoretically optimal in terms of its time complexity, its practical applicability is limited for moderate-sized datasets due to several factors. McQueen and Toussaint's experimental study revealed that, while the algorithm performed well on large datasets, the constant factors hidden in the asymptotic notation of ${\mathcal {O}}(n\log h)$ make it less efficient for smaller instances compared to other algorithms such as Chan's. Chan’s algorithm, while asymptotically less efficient in theory, is often preferred in practice due to its simpler implementation and better performance on smaller instances.

## Comparative Analysis

When compared to other output-sensitive convex hull algorithms, such as Chan's algorithm, the Kirkpatrick–Seidel algorithm offers a better asymptotic bound ( ${\mathcal {O}}(n\log h)$ versus ${\mathcal {O}}(nh)$ for the gift wrapping algorithm and Chan's method). However, Chan's algorithm is more practical due to its simpler implementation, lower constant factors, and better performance on a wide range of practical data sets. For moderate-sized problems, Chan's algorithm remains a popular choice, especially for its easier implementation and better constants.

## Constraints and Open Problems

Although the Kirkpatrick–Seidel algorithm is theoretically optimal, several issues remain open in both its practical application and theoretical expansion:

Implementation complexity: The algorithm’s complex recursive structure and reliance on finding the median of points make it harder to implement efficiently, especially compared to other algorithms with simpler designs.

Constant factors: The hidden constants in the time complexity ${\mathcal {O}}(n\log h)$ may make the algorithm slower in practice for moderate-sized datasets, limiting its practical applicability.

High-dimensional generalization: While the algorithm is efficient in two dimensions, its generalization to higher dimensions faces significant challenges due to the increasing complexity of the convex hull problem in higher-dimensional spaces.

Quantum algorithms: The potential for quantum algorithms to offer speedups for convex hull computations is an area of active research. However, no quantum algorithm has yet been proven to outperform classical algorithms like Kirkpatrick–Seidel in practical scenarios.
