---
title: "Optimization and root finding (scipy.optimize)"
source: https://docs.scipy.org/doc/scipy/reference/optimize.html
domain: scipy-library
license: BSD-3-Clause
tags: scipy library, scientific python, numerical routines, signal processing scipy
fetched: 2026-07-02
---

# Optimization and root finding (`scipy.optimize`)

SciPy `optimize` provides functions for minimizing (or maximizing) objective functions, possibly subject to constraints. It includes solvers for nonlinear problems (with support for both local and global optimization algorithms), linear programming, constrained and nonlinear least-squares, root finding, and curve fitting.

Common functions and objects, shared across different solvers, are:

| `show_options`([solver, method, disp]) | Show documentation for additional options of optimization solvers. |
|---|---|
| `OptimizeResult` | Represents the optimization result. |
| `OptimizeWarning` | General warning for `scipy.optimize`. |

## Optimization

### Scalar functions optimization

| `minimize_scalar`(fun[, bracket, bounds, ...]) | Local minimization of scalar function of one variable. |
|---|---|

The `minimize_scalar` function supports the following methods:

- minimize_scalar(method=’brent’)
- minimize_scalar(method=’bounded’)
- minimize_scalar(method=’golden’)

### Local (multivariate) optimization

| `minimize`(fun, x0[, args, method, jac, hess, ...]) | Minimization of scalar function of one or more variables. |
|---|---|

The `minimize` function supports the following methods:

- minimize(method=’Nelder-Mead’)
- minimize(method=’Powell’)
- minimize(method=’CG’)
- minimize(method=’BFGS’)
- minimize(method=’Newton-CG’)
- minimize(method=’L-BFGS-B’)
- minimize(method=’TNC’)
- minimize(method=’COBYLA’)
- minimize(method=’COBYQA’)
- minimize(method=’SLSQP’)
- minimize(method=’trust-constr’)
- minimize(method=’dogleg’)
- minimize(method=’trust-ncg’)
- minimize(method=’trust-krylov’)
- minimize(method=’trust-exact’)

Constraints are passed to `minimize` function as a single object or as a list of objects from the following classes:

| `NonlinearConstraint`(fun, lb, ub[, jac, ...]) | Nonlinear constraint on the variables. |
|---|---|
| `LinearConstraint`(A[, lb, ub, keep_feasible]) | Linear constraint on the variables. |

Simple bound constraints are handled separately and there is a special class for them:

| `Bounds`([lb, ub, keep_feasible]) | Bounds constraint on the variables. |
|---|---|

Quasi-Newton strategies implementing `HessianUpdateStrategy` interface can be used to approximate the Hessian in `minimize` function (available only for the ‘trust-constr’ method). Available quasi-Newton methods implementing this interface are:

| `BFGS`([exception_strategy, min_curvature, ...]) | Broyden-Fletcher-Goldfarb-Shanno (BFGS) Hessian update strategy. |
|---|---|
| `SR1`([min_denominator, init_scale]) | Symmetric-rank-1 Hessian update strategy. |

### Global optimization

| `basinhopping`(func, x0[, niter, T, stepsize, ...]) | Find the global minimum of a function using the basin-hopping algorithm. |
|---|---|
| `brute`(func, ranges[, args, Ns, full_output, ...]) | Minimize a function over a given range by brute force. |
| `differential_evolution`(func, bounds[, args, ...]) | Finds the global minimum of a multivariate function. |
| `shgo`(func, bounds[, args, constraints, n, ...]) | Finds the global minimum of a function using SHG optimization. |
| `dual_annealing`(func, bounds[, args, ...]) | Find the global minimum of a function using Dual Annealing. |
| `direct`(func, bounds, *[, args, eps, maxfun, ...]) | Finds the global minimum of a function using the DIRECT algorithm. |

## Least-squares and curve fitting

### Nonlinear least-squares

| `least_squares`(fun, x0[, jac, bounds, ...]) | Solve a nonlinear least-squares problem with bounds on the variables. |
|---|---|

### Linear least-squares

| `nnls`(A, b, *[, maxiter]) | Solve `argmin_x \|\| Ax - b \|\|_2^2` for `x>=0`. |
|---|---|
| `lsq_linear`(A, b[, bounds, method, tol, ...]) | Solve a linear least-squares problem with bounds on the variables. |
| `isotonic_regression`(y, *[, weights, increasing]) | Nonparametric isotonic regression. |

### Curve fitting

| `curve_fit`(f, xdata, ydata[, p0, sigma, ...]) | Use non-linear least squares to fit a function, f, to data. |
|---|---|

## Root finding

### Scalar functions

| `root_scalar`(f[, args, method, bracket, ...]) | Find a root of a scalar function. |
|---|---|
| `brentq`(f, a, b[, args, xtol, rtol, maxiter, ...]) | Find a root of a function in a bracketing interval using Brent's method. |
| `brenth`(f, a, b[, args, xtol, rtol, maxiter, ...]) | Find a root of a function in a bracketing interval using Brent's method with hyperbolic extrapolation. |
| `ridder`(f, a, b[, args, xtol, rtol, maxiter, ...]) | Find a root of a function in an interval using Ridder's method. |
| `bisect`(f, a, b[, args, xtol, rtol, maxiter, ...]) | Find root of a function within an interval using bisection. |
| `newton`(func, x0[, fprime, args, tol, ...]) | Find a root of a real or complex function using the Newton-Raphson (or secant or Halley's) method. |
| `toms748`(f, a, b[, args, k, xtol, rtol, ...]) | Find a root using TOMS Algorithm 748 method. |
| `RootResults`(root, iterations, ...) | Represents the root finding result. |

The `root_scalar` function supports the following methods:

- root_scalar(method=’brentq’)
- root_scalar(method=’brenth’)
- root_scalar(method=’bisect’)
- root_scalar(method=’ridder’)
- root_scalar(method=’newton’)
- root_scalar(method=’toms748’)
- root_scalar(method=’secant’)
- root_scalar(method=’halley’)

The table below lists situations and appropriate methods, along with *asymptotic* convergence rates per iteration (and per function evaluation) for successful convergence to a simple root(*). Bisection is the slowest of them all, adding one bit of accuracy for each function evaluation, but is guaranteed to converge. The other bracketing methods all (eventually) increase the number of accurate bits by about 50% for every function evaluation. The derivative-based methods, all built on `newton`, can converge quite quickly if the initial value is close to the root. They can also be applied to functions defined on (a subset of) the complex plane.

| Domain of f | Bracket? | Derivatives? | Solvers | Convergence |   |   |
|---|---|---|---|---|---|---|
| *fprime* | *fprime2* | Guaranteed? | Rate(s)(*) |   |   |   |
| *R* | Yes | N/A | N/A | bisection brentq brenth ridder toms748 | Yes Yes Yes Yes Yes | 1 “Linear” >=1, <= 1.62 >=1, <= 1.62 2.0 (1.41) 2.7 (1.65) |
| *R* or *C* | No | No | No | secant | No | 1.62 (1.62) |
| *R* or *C* | No | Yes | No | newton | No | 2.00 (1.41) |
| *R* or *C* | No | Yes | Yes | halley | No | 3.00 (1.44) |

See also

`scipy.optimize.cython_optimize` – Typed Cython versions of root finding functions

Fixed point finding:

| `fixed_point`(func, x0[, args, xtol, maxiter, ...]) | Find a fixed point of the function. |
|---|---|

### Multidimensional

| `root`(fun, x0[, args, method, jac, tol, ...]) | Find a root of a vector function. |
|---|---|

The `root` function supports the following methods:

- root(method=’hybr’)
- root(method=’lm’)
- root(method=’broyden1’)
- root(method=’broyden2’)
- root(method=’anderson’)
- root(method=’linearmixing’)
- root(method=’diagbroyden’)
- root(method=’excitingmixing’)
- root(method=’krylov’)
- root(method=’df-sane’)

## Elementwise Minimization and Root Finding

- Elementwise Scalar Optimization (`scipy.optimize.elementwise`)
  - Root finding
    - find_root
    - bracket_root
  - Minimization
    - find_minimum
    - bracket_minimum

## Linear programming / MILP

| `milp`(c, *[, integrality, bounds, ...]) | Mixed-integer linear programming. |
|---|---|
| `linprog`(c[, A_ub, b_ub, A_eq, b_eq, bounds, ...]) | Linear programming: minimize a linear objective function subject to linear equality and inequality constraints. |

The `linprog` function supports the following methods:

- linprog(method=’simplex’)
- linprog(method=’interior-point’)
- linprog(method=’revised simplex’)
- linprog(method=’highs-ipm’)
- linprog(method=’highs-ds’)
- linprog(method=’highs’)

The simplex, interior-point, and revised simplex methods support callback functions, such as:

| `linprog_verbose_callback`(res) | A sample callback function demonstrating the linprog callback interface. |
|---|---|

## Assignment problems

| `linear_sum_assignment`(cost_matrix[, maximize]) | Solve the linear sum assignment problem. |
|---|---|
| `quadratic_assignment`(A, B[, method, options]) | Approximates solution to the quadratic assignment problem and the graph matching problem. |

The `quadratic_assignment` function supports the following methods:

- quadratic_assignment(method=’faq’)
- quadratic_assignment(method=’2opt’)

## Utilities

### Finite-difference approximation

| `approx_fprime`(xk, f[, epsilon]) | Finite difference approximation of the derivatives of a scalar or vector-valued function. |
|---|---|
| `check_grad`(func, grad, x0, *args[, epsilon, ...]) | Check the correctness of a gradient function by comparing it against a (forward) finite-difference approximation of the gradient. |

### Hessian approximation

| `LbfgsInvHessProduct`(*args, **kwargs) | Linear operator for the L-BFGS approximate inverse Hessian. |
|---|---|
| `HessianUpdateStrategy`() | Interface for implementing Hessian update strategies. |

### Benchmark problems

| `rosen`(x) | The Rosenbrock function. |
|---|---|
| `rosen_der`(x) | The derivative (i.e. gradient) of the Rosenbrock function. |
| `rosen_hess`(x) | The Hessian matrix of the Rosenbrock function. |
| `rosen_hess_prod`(x, p) | Product of the Hessian matrix of the Rosenbrock function with a vector. |

## Legacy functions

The functions below are not recommended for use in new scripts; all of these methods are accessible via a newer, more consistent interfaces, provided by the interfaces above.

### Optimization

General-purpose multivariate methods:

| `fmin`(func, x0[, args, xtol, ftol, maxiter, ...]) | Minimize a function using the downhill simplex algorithm. |
|---|---|
| `fmin_powell`(func, x0[, args, xtol, ftol, ...]) | Minimize a function using modified Powell's method. |
| `fmin_cg`(f, x0[, fprime, args, gtol, norm, ...]) | Minimize a function using a nonlinear conjugate gradient algorithm. |
| `fmin_bfgs`(f, x0[, fprime, args, gtol, norm, ...]) | Minimize a function using the BFGS algorithm. |
| `fmin_ncg`(f, x0, fprime[, fhess_p, fhess, ...]) | Unconstrained minimization of a function using the Newton-CG method. |

Constrained multivariate methods:

| `fmin_l_bfgs_b`(func, x0[, fprime, args, ...]) | Minimize a function func using the L-BFGS-B algorithm. |
|---|---|
| `fmin_tnc`(func, x0[, fprime, args, ...]) | Minimize a function with variables subject to bounds, using gradient information in a truncated Newton algorithm. |
| `fmin_cobyla`(func, x0, cons[, args, ...]) | Minimize a function using the Constrained Optimization By Linear Approximation (COBYLA) method. |
| `fmin_slsqp`(func, x0[, eqcons, f_eqcons, ...]) | Minimize a function using Sequential Least Squares Programming. |

Univariate (scalar) minimization methods:

| `fminbound`(func, x1, x2[, args, xtol, ...]) | Bounded minimization for scalar functions. |
|---|---|
| `brent`(func[, args, brack, tol, full_output, ...]) | Given a function of one variable and a possible bracket, return a local minimizer of the function isolated to a fractional precision of tol. |
| `golden`(func[, args, brack, tol, ...]) | Return the minimizer of a function of one variable using the golden section method. |

### Least-squares

| `leastsq`(func, x0[, args, Dfun, full_output, ...]) | Minimize the sum of squares of a set of equations. |
|---|---|

### Root finding

General nonlinear solvers:

| `fsolve`(func, x0[, args, fprime, ...]) | Find the roots of a function. |
|---|---|
| `broyden1`(F, xin[, iter, alpha, ...]) | Find a root of a function, using Broyden's first Jacobian approximation. |
| `broyden2`(F, xin[, iter, alpha, ...]) | Find a root of a function, using Broyden's second Jacobian approximation. |
| `NoConvergence` | Exception raised when nonlinear solver fails to converge within the specified *maxiter*. |

Large-scale nonlinear solvers:

| `newton_krylov`(F, xin[, iter, rdiff, method, ...]) | Find a root of a function, using Krylov approximation for inverse Jacobian. |
|---|---|
| `anderson`(F, xin[, iter, alpha, w0, M, ...]) | Find a root of a function, using (extended) Anderson mixing. |
| `BroydenFirst`([alpha, reduction_method, max_rank]) | Find a root of a function, using Broyden's first Jacobian approximation. |
| `InverseJacobian`(jacobian) | A simple wrapper that inverts the Jacobian using the *solve* method. |
| `KrylovJacobian`([rdiff, method, ...]) | Find a root of a function, using Krylov approximation for inverse Jacobian. |

Simple iteration solvers:

| `excitingmixing`(F, xin[, iter, alpha, ...]) | Find a root of a function, using a tuned diagonal Jacobian approximation. |
|---|---|
| `linearmixing`(F, xin[, iter, alpha, verbose, ...]) | Find a root of a function, using a scalar Jacobian approximation. |
| `diagbroyden`(F, xin[, iter, alpha, verbose, ...]) | Find a root of a function, using diagonal Broyden Jacobian approximation. |
