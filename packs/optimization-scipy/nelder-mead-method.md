---
title: "Nelder–Mead method"
source: https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method
domain: optimization-scipy
license: CC-BY-SA-4.0
tags: mathematical optimization, nelder-mead method, sequential quadratic programming, interior-point method
fetched: 2026-07-02
---

# Nelder–Mead method

The **Nelder–Mead method** (also **downhill simplex method**, **amoeba method**, or **polytope method**) is a numerical method used to find a local minimum or maximum of an objective function in a multidimensional space. It is a direct search method (based on function comparison) and is often applied to nonlinear optimization problems for which derivatives may not be known. However, the Nelder–Mead technique is a heuristic search method that can converge to non-stationary points on problems that can be solved by alternative methods.

The Nelder–Mead technique was proposed by John Nelder and Roger Mead in 1965, as a development of the method of Spendley et al.

## Overview

The method uses the concept of a simplex, which is a special polytope of *n* + 1 vertices in *n* dimensions. Examples of simplices include a line segment in one-dimensional space, a triangle in two-dimensional space, a tetrahedron in three-dimensional space, and so forth.

The method approximates a local optimum of a problem with *n* variables when the objective function varies smoothly and is unimodal. Typical implementations minimize functions, and we maximize $f(\mathbf {x} )$ by minimizing $-f(\mathbf {x} )$ .

For example, a suspension bridge engineer has to choose how thick each strut, cable, and pier must be. These elements are interdependent, but it is not easy to visualize the impact of changing any specific element. Simulation of such complicated structures is often extremely computationally expensive to run, possibly taking upwards of hours per execution. The Nelder–Mead method requires, in the original variant, no more than two evaluations per iteration, except for the *shrink* operation described later, which is attractive compared to some other direct-search optimization methods. However, the overall number of iterations to proposed optimum may be high.

Nelder–Mead in *n* dimensions maintains a set of *n* + 1 test points arranged as a simplex. It then extrapolates the behavior of the objective function measured at each test point in order to find a new test point and to replace one of the old test points with the new one, and so the technique progresses. The simplest approach is to replace the worst point with a point reflected through the centroid of the remaining *n* points. If this point is better than the best current point, then we can try stretching exponentially out along this line. On the other hand, if this new point isn't much better than the previous value, then we are stepping across a valley, so we shrink the simplex towards a better point. An intuitive explanation of the algorithm from "Numerical Recipes":

> The downhill simplex method now takes a series of steps, most steps just moving the point of the simplex where the function is largest (“highest point”) through the opposite face of the simplex to a lower point. These steps are called reflections, and they are constructed to conserve the volume of the simplex (and hence maintain its nondegeneracy). When it can do so, the method expands the simplex in one or another direction to take larger steps. When it reaches a “valley floor”, the method contracts itself in the transverse direction and tries to ooze down the valley. If there is a situation where the simplex is trying to “pass through the eye of a needle”, it contracts itself in all directions, pulling itself in around its lowest (best) point.

Unlike modern optimization methods, the Nelder–Mead heuristic can converge to a non-stationary point, unless the problem satisfies stronger conditions than are necessary for modern methods. Modern improvements over the Nelder–Mead heuristic have been known since 1979.

Many variations exist depending on the actual nature of the problem being solved. A common variant uses a constant-size, small simplex that roughly follows the gradient direction (which gives steepest descent). Visualize a small triangle on an elevation map flip-flopping its way down a valley to a local bottom. This method is also known as the **flexible polyhedron method**. This, however, tends to perform poorly against the method described in this article because it makes small, unnecessary steps in areas of little interest.

## One possible variation of the NM algorithm

(This approximates the procedure in the original Nelder–Mead article.)

We are trying to minimize the function $f(\mathbf {x} )$ , where $\mathbf {x} \in \mathbb {R} ^{n}$ . Our current test points are $\mathbf {x} _{1},\ldots ,\mathbf {x} _{n+1}$ .

1. **Order** according to the values at the vertices: $f(\mathbf {x} _{1})\leq f(\mathbf {x} _{2})\leq \cdots \leq f(\mathbf {x} _{n+1}).$ Check whether method should stop. See **Termination** (sometimes called "convergence").
2. Calculate $\mathbf {x} _{o}$ , the centroid of all points except $\mathbf {x} _{n+1}$ .
3. **Reflection** Compute reflected point $\mathbf {x} _{r}=\mathbf {x} _{o}+\alpha (\mathbf {x} _{o}-\mathbf {x} _{n+1})$ with $\alpha >0$ . If the reflected point is better than the second worst, but not better than the best, i.e. $f(\mathbf {x} _{1})\leq f(\mathbf {x} _{r})<f(\mathbf {x} _{n})$ , then obtain a new simplex by replacing the worst point $\mathbf {x} _{n+1}$ with the reflected point $\mathbf {x} _{r}$ , and go to step 1.
4. **Expansion** If the reflected point is the best point so far, $f(\mathbf {x} _{r})<f(\mathbf {x} _{1})$ , then compute the expanded point $\mathbf {x} _{e}=\mathbf {x} _{o}+\gamma (\mathbf {x} _{r}-\mathbf {x} _{o})$ with $\gamma >1$ . If the expanded point is better than the reflected point, $f(\mathbf {x} _{e})<f(\mathbf {x} _{r})$ , then obtain a new simplex by replacing the worst point $\mathbf {x} _{n+1}$ with the expanded point $\mathbf {x} _{e}$ and go to step 1; else obtain a new simplex by replacing the worst point $\mathbf {x} _{n+1}$ with the reflected point $\mathbf {x} _{r}$ and go to step 1.
5. **Contraction** Here it is certain that $f(\mathbf {x} _{r})\geq f(\mathbf {x} _{n})$ . (Note that $\mathbf {x} _{n}$ is second or "next" to the worst point.) If $f(\mathbf {x} _{r})<f(\mathbf {x} _{n+1})$ , then compute the contracted point on the outside $\mathbf {x} _{c}=\mathbf {x} _{o}+\rho (\mathbf {x} _{r}-\mathbf {x} _{o})$ with $0<\rho \leq 0.5$ . If the contracted point is better than the reflected point, i.e. $f(\mathbf {x} _{c})<f(\mathbf {x} _{r})$ , then obtain a new simplex by replacing the worst point $\mathbf {x} _{n+1}$ with the contracted point $\mathbf {x} _{c}$ and go to step 1; Else go to step 6; If $f(\mathbf {x} _{r})\geq f(\mathbf {x} _{n+1})$ , then compute the contracted point on the inside $\mathbf {x} _{c}=\mathbf {x} _{o}+\rho (\mathbf {x} _{n+1}-\mathbf {x} _{o})$ with $0<\rho \leq 0.5$ . If the contracted point is better than the worst point, i.e. $f(\mathbf {x} _{c})<f(\mathbf {x} _{n+1})$ , then obtain a new simplex by replacing the worst point $\mathbf {x} _{n+1}$ with the contracted point $\mathbf {x} _{c}$ and go to step 1; Else go to step 6;
6. **Shrink** Replace all points except the best ( $\mathbf {x} _{1}$ ) with $\mathbf {x} _{i}=\mathbf {x} _{1}+\sigma (\mathbf {x} _{i}-\mathbf {x} _{1})$ and go to step 1.

**Note**: $\alpha$ , $\gamma$ , $\rho$ and $\sigma$ are respectively the reflection, expansion, contraction and shrink coefficients. Standard values are $\alpha =1$ , $\gamma =2$ , $\rho =1/2$ and $\sigma =1/2$ .

For the **reflection**, since $\mathbf {x} _{n+1}$ is the vertex with the higher associated value among the vertices, we can expect to find a lower value at the reflection of $\mathbf {x} _{n+1}$ in the opposite face formed by all vertices $\mathbf {x} _{i}$ except $\mathbf {x} _{n+1}$ .

For the **expansion**, if the reflection point $\mathbf {x} _{r}$ is the new minimum along the vertices, we can expect to find interesting values along the direction from $\mathbf {x} _{o}$ to $\mathbf {x} _{r}$ .

Concerning the **contraction**, if $f(\mathbf {x} _{r})>f(\mathbf {x} _{n})$ , we can expect that a better value will be inside the simplex formed by all the vertices $\mathbf {x} _{i}$ .

Finally, the **shrink** handles the rare case that contracting away from the largest point increases f , something that cannot happen sufficiently close to a non-singular minimum. In that case we contract towards the lowest point in the expectation of finding a simpler landscape. However, Nash notes that finite-precision arithmetic can sometimes fail to actually shrink the simplex, and implemented a check that the size is actually reduced.

## Initial simplex

The initial simplex is important. Indeed, a too small initial simplex can lead to a local search, consequently the NM can get more easily stuck. So this simplex should depend on the nature of the problem. However, the original article suggested a simplex where an initial point is given as $\mathbf {x} _{1}$ , with the others generated with a fixed step along each dimension in turn. Thus the method is sensitive to scaling of the variables that make up $\mathbf {x}$ .

## Termination

Criteria are needed to break the iterative cycle. Nelder and Mead used the sample standard deviation of the function values of the current simplex. If these fall below some tolerance, then the cycle is stopped and the lowest point in the simplex returned as a proposed optimum. Note that a very "flat" function may have almost equal function values over a large domain, so that the solution will be sensitive to the tolerance. Nash adds the test for shrinkage as another termination criterion. Note that programs terminate, while iterations may converge.
