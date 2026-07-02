---
title: "Quasi-Newton method"
source: https://en.wikipedia.org/wiki/Quasi-Newton_method
domain: quasi-newton-bfgs
license: CC-BY-SA-4.0
tags: quasi newton method, bfgs update, limited memory bfgs, hessian approximation
fetched: 2026-07-02
---

# Quasi-Newton method

In numerical analysis, a **quasi-Newton method** is an iterative numerical method used either to find zeroes or to find local maxima and minima of functions via an iterative recurrence formula much like the one for Newton's method, except using approximations of the derivatives of the functions in place of exact derivatives. Newton's method requires the Jacobian matrix of all partial derivatives of a multivariate function when used to search for zeros or the Hessian matrix when used for finding extrema. Quasi-Newton methods, on the other hand, can be used when the Jacobian matrices or Hessian matrices are unavailable or are impractical to compute at every iteration.

Some iterative methods that reduce to Newton's method, such as sequential quadratic programming, may also be considered quasi-Newton methods.

Newton's method to find zeroes of a function g of multiple variables is given by $x_{n+1}=x_{n}-[J_{g}(x_{n})]^{-1}g(x_{n})$ , where $[J_{g}(x_{n})]^{-1}$ is the right inverse of the Jacobian matrix $J_{g}(x_{n})$ of g evaluated for $x_{n}$ .

Strictly speaking, any method that replaces the exact Jacobian $J_{g}(x_{n})$ with an approximation is a quasi-Newton method. For instance, the chord method (where $J_{g}(x_{n})$ is replaced by $J_{g}(x_{0})$ for all iterations) is a simple example. The methods given below for optimization refer to an important subclass of quasi-Newton methods, secant methods.

Using methods developed to find extrema in order to find zeroes is not always a good idea, as the majority of the methods used to find extrema require that the matrix that is used is symmetrical. While this holds in the context of the search for extrema, it rarely holds when searching for zeroes. Broyden's "good" and "bad" methods are two methods commonly used to find extrema that can also be applied to find zeroes. Other methods that can be used are the column-updating method, the inverse column-updating method, the quasi-Newton least squares method and the quasi-Newton inverse least squares method.

More recently quasi-Newton methods have been applied to find the solution of multiple coupled systems of equations (e.g. fluid–structure interaction problems or interaction problems in physics). They allow the solution to be found by solving each constituent system separately (which is simpler than the global system) in a cyclic, iterative fashion until the solution of the global system is found.

The search for a minimum or maximum of a scalar-valued function is closely related to the search for the zeroes of the gradient of that function. Therefore, quasi-Newton methods can be readily applied to find extrema of a function. In other words, if g is the gradient of f , then searching for the zeroes of the vector-valued function g corresponds to the search for the extrema of the scalar-valued function f ; the Jacobian of g now becomes the Hessian of f . The main difference is that the Hessian matrix is a symmetric matrix, unlike the Jacobian when searching for zeroes. Most quasi-Newton methods used in optimization exploit this symmetry.

In optimization, **quasi-Newton methods** (a special case of **variable-metric methods**) are algorithms for finding local maxima and minima of functions. Quasi-Newton methods for optimization are based on Newton's method to find the stationary points of a function, points where the gradient is 0. Newton's method assumes that the function can be locally approximated as a quadratic in the region around the optimum, and uses the first and second derivatives to find the stationary point. In higher dimensions, Newton's method uses the gradient and the Hessian matrix of second derivatives of the function to be minimized.

In quasi-Newton methods the Hessian matrix does not need to be computed. The Hessian is updated by analyzing successive gradient vectors instead. Quasi-Newton methods are a generalization of the secant method to find the root of the first derivative for multidimensional problems. In multiple dimensions the secant equation is under-determined, and quasi-Newton methods differ in how they constrain the solution, typically by adding a simple low-rank update to the current estimate of the Hessian.

The first quasi-Newton algorithm was proposed by William C. Davidon, a physicist working at Argonne National Laboratory. He developed the first quasi-Newton algorithm in 1959: the DFP updating formula, which was later popularized by Fletcher and Powell in 1963, but is rarely used today. The most common quasi-Newton algorithms are currently the SR1 formula (for "symmetric rank-one"), the BHHH method, the widespread BFGS method (suggested independently by Broyden, Fletcher, Goldfarb, and Shanno, in 1970), and its low-memory extension L-BFGS. The Broyden's class is a linear combination of the DFP and BFGS methods.

The SR1 formula does not guarantee the update matrix to maintain positive-definiteness and can be used for indefinite problems. The Broyden's method does not require the update matrix to be symmetric and is used to find the root of a general system of equations (rather than the gradient) by updating the Jacobian (rather than the Hessian).

One of the chief advantages of quasi-Newton methods over Newton's method is that the Hessian matrix (or, in the case of quasi-Newton methods, its approximation) B does not need to be inverted. Newton's method, and its derivatives such as interior point methods, require the Hessian to be inverted, which is typically implemented by solving a system of linear equations and is often quite costly. In contrast, quasi-Newton methods usually generate an estimate of $B^{-1}$ directly.

As in Newton's method, one uses a second-order approximation to find the minimum of a function $f(x)$ . The Taylor series of $f(x)$ around an iterate is

$f(x_{k}+\Delta x)\approx f(x_{k})+\nabla f(x_{k})^{\mathrm {T} }\,\Delta x+{\frac {1}{2}}\Delta x^{\mathrm {T} }B\,\Delta x,$

where ( $\nabla f$ ) is the gradient, and B an approximation to the Hessian matrix. The gradient of this approximation (with respect to $\Delta x$ ) is

$\nabla f(x_{k}+\Delta x)\approx \nabla f(x_{k})+B\,\Delta x,$

and setting this gradient to zero (which is the goal of optimization) provides the Newton step:

$\Delta x=-B^{-1}\nabla f(x_{k}).$

The Hessian approximation B is chosen to satisfy

$\nabla f(x_{k}+\Delta x)=\nabla f(x_{k})+B\,\Delta x,$

which is called the *secant equation* (the Taylor series of the gradient itself). In more than one dimension B is underdetermined. Using n different secants would be enough to determine B , but is equivalent to computing a finite difference Hessian. In one dimension, solving for B and applying the Newton's step with the updated value is equivalent to the secant method. The various quasi-Newton methods differ in their choice of the solution to the secant equation (in one dimension, all the variants are equivalent). Most methods (but with exceptions, such as Broyden's method) seek a symmetric solution ( $B^{T}=B$ ); furthermore, the variants listed below can be motivated by finding an update $B_{k+1}$ that is as close as possible to $B_{k}$ in some norm; that is, $B_{k+1}=\operatorname {argmin} _{B}\|B-B_{k}\|_{V}$ , where V is some positive-definite matrix that defines the norm. An approximate initial value $B_{0}=\beta I$ is often sufficient to achieve rapid convergence, although there is no general strategy to choose $\beta$ . Note that $B_{0}$ should be positive-definite. The unknown $x_{k}$ is updated applying the Newton's step calculated using the current approximate Hessian matrix $B_{k}$ :

- $\Delta x_{k}=-\alpha _{k}B_{k}^{-1}\nabla f(x_{k})$ , with $\alpha$ chosen to satisfy the Wolfe conditions;
- $x_{k+1}=x_{k}+\Delta x_{k}$ ;
- The gradient computed at the new point $\nabla f(x_{k+1})$ , and

$y_{k}=\nabla f(x_{k+1})-\nabla f(x_{k})$

is used to update the approximate Hessian $B_{k+1}$ , or directly its inverse $H_{k+1}=B_{k+1}^{-1}$ using the Sherman–Morrison formula.

- A key property of the BFGS and DFP updates is that if $B_{k}$ is positive-definite, and $\alpha _{k}$ is chosen to satisfy the Wolfe conditions, then $B_{k+1}$ is also positive-definite.

The most popular update formulas are:

| Method | $\displaystyle B_{k+1}=$ | $H_{k+1}=B_{k+1}^{-1}=$ |
|---|---|---|
| BFGS | $B_{k}+{\frac {y_{k}y_{k}^{\mathrm {T} }}{y_{k}^{\mathrm {T} }\Delta x_{k}}}-{\frac {B_{k}\Delta x_{k}(B_{k}\Delta x_{k})^{\mathrm {T} }}{\Delta x_{k}^{\mathrm {T} }B_{k}\,\Delta x_{k}}}$ | $\left(I-{\frac {\Delta x_{k}y_{k}^{\mathrm {T} }}{y_{k}^{\mathrm {T} }\Delta x_{k}}}\right)H_{k}\left(I-{\frac {y_{k}\Delta x_{k}^{\mathrm {T} }}{y_{k}^{\mathrm {T} }\Delta x_{k}}}\right)+{\frac {\Delta x_{k}\Delta x_{k}^{\mathrm {T} }}{y_{k}^{\mathrm {T} }\,\Delta x_{k}}}$ |
| Broyden | $B_{k}+{\frac {y_{k}-B_{k}\Delta x_{k}}{\Delta x_{k}^{\mathrm {T} }\,\Delta x_{k}}}\,\Delta x_{k}^{\mathrm {T} }$ | $H_{k}+{\frac {(\Delta x_{k}-H_{k}y_{k})\Delta x_{k}^{\mathrm {T} }H_{k}}{\Delta x_{k}^{\mathrm {T} }H_{k}\,y_{k}}}$ |
| Broyden family | $(1-\varphi _{k})B_{k+1}^{\text{BFGS}}+\varphi _{k}B_{k+1}^{\text{DFP}},\quad \varphi \in [0,1]$ |   |
| DFP | $\left(I-{\frac {y_{k}\,\Delta x_{k}^{\mathrm {T} }}{y_{k}^{\mathrm {T} }\,\Delta x_{k}}}\right)B_{k}\left(I-{\frac {\Delta x_{k}y_{k}^{\mathrm {T} }}{y_{k}^{\mathrm {T} }\,\Delta x_{k}}}\right)+{\frac {y_{k}y_{k}^{\mathrm {T} }}{y_{k}^{\mathrm {T} }\,\Delta x_{k}}}$ | $H_{k}+{\frac {\Delta x_{k}\Delta x_{k}^{\mathrm {T} }}{\Delta x_{k}^{\mathrm {T} }\,y_{k}}}-{\frac {H_{k}y_{k}y_{k}^{\mathrm {T} }H_{k}}{y_{k}^{\mathrm {T} }H_{k}y_{k}}}$ |
| SR1 | $B_{k}+{\frac {(y_{k}-B_{k}\,\Delta x_{k})(y_{k}-B_{k}\,\Delta x_{k})^{\mathrm {T} }}{(y_{k}-B_{k}\,\Delta x_{k})^{\mathrm {T} }\,\Delta x_{k}}}$ | $H_{k}+{\frac {(\Delta x_{k}-H_{k}y_{k})(\Delta x_{k}-H_{k}y_{k})^{\mathrm {T} }}{(\Delta x_{k}-H_{k}y_{k})^{\mathrm {T} }y_{k}}}$ |

Other methods are Pearson's method, McCormick's method, the Powell symmetric Broyden (PSB) method and Greenstadt's method. These recursive low-rank matrix updates can also represented as an initial matrix plus a low-rank correction. This is the Compact quasi-Newton representation, which is particularly effective for constrained and/or large problems.

## Relationship to matrix inversion

When f is a convex quadratic function with positive-definite Hessian B , one would expect the matrices $H_{k}$ generated by a quasi-Newton method to converge to the inverse Hessian $H=B^{-1}$ . This is indeed the case for the class of quasi-Newton methods based on least-change updates.

## Regular Quasi-Newton Methods

An attempt to provide an overview of the various approaches to quasi-Newton methods was made in 1985 in the article “Regular Quasi-Newton Methods.” Here, a comprehensive class of these methods was developed, a representation of all rank 1 formulas of the so-called symmetric, novelized Huang class, which includes well-known methods such as the Davidon-Fletcher-Powell (DFP), Broyden-Fletcher-Goldfarb-Shanno (BFGS), and Self-Scaling-Variable-Metric (SSVM) methods. Suggestions for further optimization of the solution behavior of quasi-Newton methods are also given. The following class of “regular” (i.e., preferred for use due to special properties) Quasi-Newton update formulas was constructed:

$H_{i+1}:=B(H_{i},p_{i},q_{i},\theta _{i},r_{i},\rho _{i})$

with

$B(H,p,q,\theta ,r,\rho )=rH+{{\rho \sigma +r\tau \theta } \over \sigma ^{2}}pp^{T}+r{{(\theta -1)} \over \tau }Hqq^{T}H-{{r\theta } \over \sigma }(pq^{T}H+Hqp^{T});$

$H\in \mathbb {R} ^{nxn}$

positive definite;

$p,q\in \mathbb {R} ^{n};\epsilon =p^{T}H^{-1}p;$

$\sigma =p^{T}q;\tau =q^{T}Hq;\theta ,r,\rho \in \mathbb {R} ;r>0;\rho \sigma >0;$

$\theta [\epsilon \tau -\sigma ^{2}]>-\sigma ^{2};r\tau [\rho \sigma +\theta (r\tau -\rho \sigma )]\geq 0$

.

For approximate, sufficiently accurate beam minimization, positive definite $H_{0}\in \mathbb {R} ^{nxn}$ and arbitrary $x_{0}\in \mathbb {R} ^{n}$ , the following applies to these regular methods, which are derived from the above formula:

1) The methods are quasi-Newton methods.

2) The matrices $H_{i}$ are positive definite for all iterations. Thus,

$f(x_{i+1})<f(x_{i})$

applies for all iterations.

3) For all iterations $i\geq 0$ , we obtain solutions to the minimization problem.

For exact beam minimization and quadratic objective functions, each of these methods also terminates at the minimum point after at most n iteration steps. In particular, the regular quasi-Newton methods have the good properties of both the extended Greenstadt class and the symmetric, extended Huang class with regard to convergence and stability.

It can be assumed that all particularly powerful quasi-Newton methods are regular.

## Notable implementations

Implementations of quasi-Newton methods are available in many programming languages.

Notable open source implementations include:

- GNU Octave uses a form of BFGS in its `fsolve` function, with trust region extensions.
- GNU Scientific Library implements the Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm.
- ALGLIB implements (L)BFGS in C++ and C#
- R's `optim` general-purpose optimizer routine uses the BFGS method by using `method="BFGS"`.
- Scipy.optimize has fmin_bfgs. In the SciPy extension to Python, the `scipy.optimize.minimize` function includes, among other methods, a BFGS implementation.

Notable proprietary implementations include:

- Mathematica includes quasi-Newton solvers.
- The NAG Library contains several routines for minimizing or maximizing a function which use quasi-Newton algorithms.
- In MATLAB's Optimization Toolbox, the `fminunc` function uses (among other methods) the BFGS quasi-Newton method. Many of the constrained methods of the Optimization toolbox use BFGS and the variant L-BFGS.
