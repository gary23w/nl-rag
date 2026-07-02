---
title: "Coordinate descent"
source: https://en.wikipedia.org/wiki/Coordinate_descent
domain: gradient-descent-variants
license: CC-BY-SA-4.0
tags: gradient descent variants, momentum method, nesterov acceleration, adagrad rmsprop
fetched: 2026-07-02
---

# Coordinate descent

**Coordinate descent** is an optimization algorithm that successively minimizes along coordinate directions to find the minimum of a function. At each iteration, the algorithm determines a coordinate or coordinate block via a coordinate selection rule, then exactly or inexactly minimizes over the corresponding coordinate hyperplane while fixing all other coordinates or coordinate blocks. A line search along the coordinate direction can be performed at the current iterate to determine the appropriate step size. Coordinate descent is applicable in both differentiable and derivative-free contexts.

## Description

Coordinate descent is based on the idea that the minimization of a multivariable function $F(\mathbf {x} )$ can be achieved by minimizing it along one direction at a time, i.e., solving univariate (or at least much simpler) optimization problems in a loop. In the simplest case of *cyclic coordinate descent*, one cyclically iterates through the directions, one at a time, minimizing the objective function with respect to each coordinate direction at a time. That is, starting with initial variable values

$\mathbf {x} ^{0}=(x_{1}^{0},\ldots ,x_{n}^{0})$

,

round $k+1$ defines $\mathbf {x} ^{k+1}$ from $\mathbf {x} ^{k}$ by iteratively solving the single variable optimization problems

$x_{i}^{k+1}={\underset {y\in \mathbb {R} }{\operatorname {arg\,min} }}\;f(x_{1}^{k+1},\dots ,x_{i-1}^{k+1},y,x_{i+1}^{k},\dots ,x_{n}^{k})$

for each variable $x_{i}$ of $\mathbf {x}$ , for i from 1 to n .

Thus, one begins with an initial guess $\mathbf {x} ^{0}$ for a local minimum of F , and gets a sequence $\mathbf {x} ^{0},\mathbf {x} ^{1},\mathbf {x} ^{2},\dots$ iteratively.

By doing line search in each iteration, one automatically has

$F(\mathbf {x} ^{0})\geq F(\mathbf {x} ^{1})\geq F(\mathbf {x} ^{2})\geq \dots .$

It can be shown that this sequence has similar convergence properties as steepest descent. No improvement after one cycle of line search along coordinate directions implies a stationary point is reached.

This process is illustrated below.

### Differentiable case

In the case of a continuously differentiable function F, a coordinate descent algorithm can be sketched as:

- Choose an initial parameter vector **x**.
- Until convergence is reached, or for some fixed number of iterations:
  - Choose an index i from 1 to n.
  - Choose a step size α.
  - Update xi to *xi* − α⁠∂*F*/∂*xi*⁠(**x**).

The step size can be chosen in various ways, e.g., by solving for the exact minimizer of *f*(*xi*) = *F*(**x**) (i.e., F with all variables but xi fixed), or by traditional line search criteria.

## Limitations

Coordinate descent has two problems. One of them is the case of a non-smooth objective function. The following picture shows that coordinate descent iteration may get stuck at a non-stationary point if the level curves of the function are not smooth. Suppose that the algorithm is at the point (−2, −2); then there are two axis-aligned directions it can consider for taking a step, indicated by the red arrows. However, every step along these two directions will increase the objective function's value (assuming a minimization problem), so the algorithm will not take any step, even though both steps together would bring the algorithm closer to the optimum. While this example shows that coordinate descent does not necessarily converge to the optimum, it is possible to show formal convergence under reasonable conditions.

The other problem is difficulty in parallelism. Since the nature of coordinate descent is to cycle through the directions and minimize the objective function with respect to each coordinate direction, coordinate descent is not an obvious candidate for massive parallelism. Recent research works have shown that massive parallelism is applicable to coordinate descent by relaxing the change of the objective function with respect to each coordinate direction.

## Applications

Coordinate descent algorithms are popular with practitioners owing to their simplicity, but the same property has led optimization researchers to largely ignore them in favor of more interesting (complicated) methods. An early application of coordinate descent optimization was in the area of computed tomography where it has been found to have rapid convergence and was subsequently used for clinical multi-slice helical scan CT reconstruction. A cyclic coordinate descent algorithm (CCD) has been applied in protein structure prediction. Moreover, there has been increased interest in the use of coordinate descent with the advent of large-scale problems in machine learning, where coordinate descent has been shown competitive to other methods when applied to such problems as training linear support vector machines (see LIBLINEAR) and non-negative matrix factorization. They are attractive for problems where computing gradients is infeasible, perhaps because the data required to do so are distributed across computer networks.
