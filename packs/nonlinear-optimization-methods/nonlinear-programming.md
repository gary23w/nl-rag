---
title: "Nonlinear programming"
source: https://en.wikipedia.org/wiki/Nonlinear_programming
domain: nonlinear-optimization-methods
license: CC-BY-SA-4.0
tags: nonlinear programming, sequential quadratic programming, trust region, gauss-newton algorithm
fetched: 2026-07-02
---

# Nonlinear programming

In mathematics, **nonlinear programming** (**NLP**), also known as **nonlinear optimization**, is the process of solving an optimization problem where some of the constraints are not linear equalities or the objective function is not a linear function. An optimization problem is one of calculation of the extrema (maxima, minima or stationary points) of an objective function over a set of unknown real variables and conditional to the satisfaction of a system of equalities and inequalities, collectively termed constraints. It is the sub-field of mathematical optimization that deals with problems that are not linear.

## Definition and discussion

Let *n*, *m*, and *p* be positive integers. Let *X* be a subset of *Rn* (usually a box-constrained one), let *f*, *gi*, and *hj* be real-valued functions on *X* for each *i* in {*1*, ..., *m*} and each *j* in {*1*, ..., *p*}, with at least one of *f*, *gi*, and *hj* being nonlinear.

A nonlinear programming problem is an optimization problem of the form

${\begin{aligned}{\text{minimize }}&f(x)\\{\text{subject to }}&g_{i}(x)\leq 0{\text{ for each }}i\in \{1,\dotsc ,m\}\\&h_{j}(x)=0{\text{ for each }}j\in \{1,\dotsc ,p\}\\&x\in X.\end{aligned}}$

Depending on the constraint set, there are several possibilities:

- *feasible* problem is one for which there exists at least one set of values for the choice variables satisfying all the constraints.
- an *infeasible* problem is one for which no set of values for the choice variables satisfies all the constraints. That is, the constraints are mutually contradictory, and no solution exists; the feasible set is the empty set.
- *unbounded* problem is a feasible problem for which the objective function can be made to be better than any given finite value. Thus there is no optimal solution, because there is always a feasible solution that gives a better objective function value than does any given proposed solution.

Most realistic applications feature feasible problems, with infeasible or unbounded problems seen as a failure of an underlying model. In some cases, infeasible problems are handled by minimizing a sum of feasibility violations.

Some special cases of nonlinear programming have specialized solution methods:

- If the objective function is concave (maximization problem), or convex (minimization problem) and the constraint set is convex, then the program is called convex and general methods from convex optimization can be used in most cases.
- If the objective function is quadratic and the constraints are linear, quadratic programming techniques are used.
- If the objective function is a ratio of a concave and a convex function (in the maximization case) and the constraints are convex, then the problem can be transformed to a convex optimization problem using fractional programming techniques.

## Applicability

A typical non-convex problem is that of optimizing transportation costs by selection from a set of transportation methods, one or more of which exhibit economies of scale, with various connectivities and capacity constraints. An example would be petroleum product transport given a selection or combination of pipeline, rail tanker, road tanker, river barge, or coastal tankship. Owing to economic batch size the cost functions may have discontinuities in addition to smooth changes.

In experimental science, some simple data analysis (such as fitting a spectrum with a sum of peaks of known location and shape but unknown magnitude) can be done with linear methods, but in general these problems are also nonlinear. Typically, one has a theoretical model of the system under study with variable parameters in it and a model the experiment or experiments, which may also have unknown parameters. One tries to find a best fit numerically. In this case one often wants a measure of the precision of the result, as well as the best fit itself.

## Methods for solving a general nonlinear program

### Analytic methods

Under differentiability and constraint qualifications, the Karush–Kuhn–Tucker (KKT) conditions provide necessary conditions for a solution to be optimal. If some of the functions are non-differentiable, subdifferential versions of Karush–Kuhn–Tucker (KKT) conditions are available.

Under convexity, the KKT conditions are sufficient for a global optimum. Without convexity, these conditions are sufficient only for a local optimum. In some cases, the number of local optima is small, and one can find all of them analytically and find the one for which the objective value is smallest.

### Numeric methods

In most realistic cases, it is very hard to solve the KKT conditions analytically, and so the problems are solved using numerical methods. These methods are iterative: they start with an initial point, and then proceed to points that are supposed to be closer to the optimal point, using some update rule. There are three kinds of update rules:

- Zero-order routines - use only the values of the objective function and constraint functions at the current point;
- First-order routines - use also the values of the *gradients* of these functions;
- Second-order routines - use also the values of the *Hessians* of these functions.

Third-order routines (and higher) are theoretically possible, but not used in practice, due to the higher computational load and little theoretical benefit.

### Branch and bound

Another method involves the use of branch and bound techniques, where the program is divided into subclasses to be solved with convex (minimization problem) or linear approximations that form a lower bound on the overall cost within the subdivision. With subsequent divisions, at some point an actual solution will be obtained whose cost is equal to the best lower bound obtained for any of the approximate solutions. This solution is optimal, although possibly not unique. The algorithm may also be stopped early, with the assurance that the best possible solution is within a tolerance from the best point found; such points are called ε-optimal. Terminating to ε-optimal points is typically necessary to ensure finite termination. This is especially useful for large, difficult problems and problems with uncertain costs or values where the uncertainty can be estimated with an appropriate reliability estimation.

## Implementations

There exist numerous nonlinear programming solvers, including open source:

- ALGLIB (C++, C#, Java, Python API) implements several first-order and derivative-free nonlinear programming solvers
- NLopt (C/C++ implementation, with numerous interfaces including Julia, Python, R, MATLAB/Octave), includes various nonlinear programming solvers
- SciPy (de facto standard for scientific Python) has scipy.optimize solver, which includes several nonlinear programming algorithms (zero-order, first order and second order ones).
- IPOPT (C++ implementation, with numerous interfaces including C, Fortran, Java, AMPL, R, Python, etc.) is an interior point method solver (zero-order, and optionally first order and second order derivatives).

Proprietary solvers include SNOPT (written in Fortran, with interfaces to C, C++, Python and MATLAB).

## Numerical Examples

### 2-dimensional example

A simple problem (shown in the diagram) can be defined by the constraints ${\begin{aligned}x_{1}&\geq 0\\x_{2}&\geq 0\\x_{1}^{2}+x_{2}^{2}&\geq 1\\x_{1}^{2}+x_{2}^{2}&\leq 2\end{aligned}}$ with an objective function to be maximized $f(\mathbf {x} )=x_{1}+x_{2}$ where **x** = (*x*1, *x*2).

### 3-dimensional example

Another simple problem (see diagram) can be defined by the constraints ${\begin{aligned}x_{1}^{2}-x_{2}^{2}+x_{3}^{2}&\leq 2\\x_{1}^{2}+x_{2}^{2}+x_{3}^{2}&\leq 10\end{aligned}}$ with an objective function to be maximized $f(\mathbf {x} )=x_{1}x_{2}+x_{2}x_{3}$ where **x** = (*x*1, *x*2, *x*3).
