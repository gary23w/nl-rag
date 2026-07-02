---
title: "Relaxation (iterative method)"
source: https://en.wikipedia.org/wiki/Relaxation_(iterative_method)
domain: multigrid-methods
license: CC-BY-SA-4.0
tags: multigrid method, gauss-seidel method, successive over-relaxation, domain decomposition
fetched: 2026-07-02
---

# Relaxation (iterative method)

In numerical mathematics, **relaxation methods** are iterative methods for solving systems of equations, including nonlinear systems.

Relaxation methods were developed for solving large sparse linear systems, which arose as finite-difference discretizations of differential equations. They are also used for the solution of linear equations for linear least-squares problems and also for systems of linear inequalities, such as those arising in linear programming. They have also been developed for solving nonlinear systems of equations.

Relaxation methods are important especially in the solution of linear systems used to model elliptic partial differential equations, such as Laplace's equation and its generalization, Poisson's equation. These equations describe boundary-value problems, in which the solution-function's values are specified on boundary of a domain; the problem is to compute a solution also on its interior. Relaxation methods are used to solve the linear equations resulting from a discretization of the differential equation, for example by finite differences.

Iterative relaxation of solutions is commonly dubbed smoothing because with certain equations, such as Laplace's equation, it resembles repeated application of a local smoothing filter to the solution vector. These are not to be confused with relaxation methods in mathematical optimization, which approximate a difficult problem by a simpler problem whose "relaxed" solution provides information about the solution of the original problem.

## Model problem of potential theory

When φ is a smooth real-valued function on the real numbers, its second derivative can be approximated by:

${\frac {d^{2}\varphi (x)}{{dx}^{2}}}={\frac {\varphi (x{-}h)-2\varphi (x)+\varphi (x{+}h)}{h^{2}}}\,+\,{\mathcal {O}}(h^{2})\,.$

Using this in both dimensions for a function φ of two arguments at the point (*x*, *y*), and solving for φ(*x*, *y*), results in:

$\varphi (x,y)={\tfrac {1}{4}}\left(\varphi (x{+}h,y)+\varphi (x,y{+}h)+\varphi (x{-}h,y)+\varphi (x,y{-}h)\,-\,h^{2}{\nabla }^{2}\varphi (x,y)\right)\,+\,{\mathcal {O}}(h^{4})\,.$

To approximate the solution of the Poisson equation:

${\nabla }^{2}\varphi =f\,$

numerically on a two-dimensional grid with grid spacing *h*, the relaxation method assigns the given values of function φ to the grid points near the boundary and arbitrary values to the interior grid points, and then repeatedly performs the assignment φ := φ* on the interior points, where φ* is defined by:

$\varphi ^{*}(x,y)={\tfrac {1}{4}}\left(\varphi (x{+}h,y)+\varphi (x,y{+}h)+\varphi (x{-}h,y)+\varphi (x,y{-}h)\,-\,h^{2}f(x,y)\right)\,,$

until convergence.

The method is easily generalized to other numbers of dimensions.

## Convergence and acceleration

While the method converges under general conditions, it typically makes slower progress than competing methods. Nonetheless, the study of relaxation methods remains a core part of linear algebra, because the transformations of relaxation theory provide excellent preconditioners for new methods. Indeed, the choice of preconditioner is often more important than the choice of iterative method.

Multigrid methods may be used to accelerate the methods. One can first compute an approximation on a coarser grid – usually the double spacing 2*h* – and use that solution with interpolated values for the other grid points as the initial assignment. This can then also be done recursively for the coarser computation.
