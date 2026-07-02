---
title: "Iterative method"
source: https://en.wikipedia.org/wiki/Iterative_method
domain: multigrid-methods
license: CC-BY-SA-4.0
tags: multigrid method, gauss-seidel method, successive over-relaxation, domain decomposition
fetched: 2026-07-02
---

# Iterative method

In computational mathematics, an **iterative method** is a mathematical procedure that uses an initial value to generate a sequence of improving approximate solutions for a class of problems, in which the *i*-th approximation (called an "iterate") is derived from the previous ones.

A specific implementation with termination criteria for a given iterative method like gradient descent, hill climbing, Newton's method, or quasi-Newton methods like BFGS, is an algorithm of an iterative method or a **method of successive approximation**. An iterative method is called *convergent* if the corresponding sequence converges for given initial approximations. A mathematically rigorous convergence analysis of an iterative method is usually performed; however, heuristic-based iterative methods are also common.

In contrast, **direct methods** attempt to solve the problem by a finite sequence of operations. In the absence of rounding errors, direct methods would deliver an exact solution (for example, solving a linear system of equations $A\mathbf {x} =\mathbf {b}$ by Gaussian elimination). Iterative methods are often the only choice for nonlinear equations. However, iterative methods are often useful even for linear problems involving many variables (sometimes on the order of millions), where direct methods would be prohibitively expensive (and in some cases impossible) even with the best available computing power.

## Attractive fixed points

If an equation can be put into the form *f*(*x*) = *x*, and a solution **x** is an attractive fixed point of the function *f*, then one may begin with a point *x*1 in the basin of attraction of **x**, and let *x**n*+1 = *f*(*x**n*) for *n* ≥ 1, and the sequence {*x**n*}*n* ≥ 1 will converge to the solution **x**. Here *x**n* is the *n*th approximation or iteration of *x* and *x**n*+1 is the next or *n* + 1 iteration of *x*. Alternately, superscripts in parentheses are often used in numerical methods, so as not to interfere with subscripts with other meanings. (For example, *x*(*n*+1) = *f*(*x*(*n*)).) If the function *f* is continuously differentiable, a sufficient condition for convergence is that the spectral radius of the derivative is strictly bounded by one in a neighborhood of the fixed point. If this condition holds at the fixed point, then a sufficiently small neighborhood (basin of attraction) must exist.

## Linear systems

In the case of a system of linear equations, the two main classes of iterative methods are the **stationary iterative methods**, and the more general Krylov subspace methods.

### Stationary iterative methods

#### Introduction

Stationary iterative methods solve a linear system with an operator approximating the original one; and based on a measurement of the error in the result (the residual), form a "correction equation" for which this process is repeated. While these methods are simple to derive, implement, and analyze, convergence is only guaranteed for a limited class of matrices.

#### Definition

An *iterative method* is defined by $\mathbf {x} ^{k+1}:=\Psi (\mathbf {x} ^{k}),\quad k\geq 0$ and for a given linear system $A\mathbf {x} =\mathbf {b}$ with exact solution $\mathbf {x} ^{*}$ the *error* by $\mathbf {e} ^{k}:=\mathbf {x} ^{k}-\mathbf {x} ^{*},\quad k\geq 0.$ An iterative method is called *linear* if there exists a matrix $C\in \mathbb {R} ^{n\times n}$ such that $\mathbf {e} ^{k+1}=C\mathbf {e} ^{k}\quad \forall k\geq 0$ and this matrix is called the *iteration matrix*. An iterative method with a given iteration matrix C is called *convergent* if the following holds $\lim _{k\to \infty }C^{k}=0.$

An important theorem states that for a given iterative method and its iteration matrix C it is convergent if and only if its spectral radius $\rho (C)$ is smaller than unity, that is, $\rho (C)<1.$

The basic iterative methods work by splitting the matrix A into $A=M-N$ and here the matrix M should be easily invertible. The iterative methods are now defined as $M\mathbf {x} ^{k+1}=N\mathbf {x} ^{k}+\mathbf {b} ,\quad k\geq 0,$ or, equivalently, $\mathbf {x} ^{k+1}=\mathbf {x} ^{k}+M^{-1}\left(\mathbf {b} -A\mathbf {x} ^{k}\right),\quad k\geq 0.$ From this follows that the iteration matrix is given by $C=I-M^{-1}A=M^{-1}N.$

#### Examples

Basic examples of stationary iterative methods use a splitting of the matrix A such as $A=D+L+U\,,\quad D:=\operatorname {diag} ((a_{ii})_{i})$ where D is only the diagonal part of A , and L is the strict lower triangular part of A . Respectively, U is the strict upper triangular part of A .

- Richardson method: $M:={\frac {1}{\omega }}I\quad (\omega \neq 0)$
- Jacobi method: $M:=D$
- Damped Jacobi method: $M:={\frac {1}{\omega }}D\quad (\omega \neq 0)$
- Gauss–Seidel method: $M:=D+L$
- Successive over-relaxation method (SOR): $M:={\frac {1}{\omega }}D+L\quad (\omega \neq 0)$
- Symmetric successive over-relaxation (SSOR): $M:={\frac {1}{\omega \left(2-\omega \right)}}\left(D+\omega L\right)D^{-1}\left(D+\omega U\right)\quad (\omega \not \in \{0,2\})$

Linear stationary iterative methods are also called relaxation methods.

### Krylov subspace methods

Krylov subspace methods work by forming a basis of the sequence of successive matrix powers times the initial residual (the **Krylov sequence**). The approximations to the solution are then formed by minimizing the residual over the subspace formed. The prototypical method in this class is the conjugate gradient method (CG) which assumes that the system matrix A is symmetric positive-definite. For symmetric (and possibly indefinite) A one works with the minimal residual method (MINRES). In the case of non-symmetric matrices, methods such as the generalized minimal residual method (GMRES) and the biconjugate gradient method (BiCG) have been derived.

#### Convergence of Krylov subspace methods

Since these methods form a basis, it is evident that the method converges in *N* iterations, where *N* is the system size. However, in the presence of rounding errors this statement does not hold; moreover, in practice *N* can be very large, and the iterative process reaches sufficient accuracy already far earlier. The analysis of these methods is hard, depending on a complicated function of the spectrum of the operator.

### Preconditioners

The approximating operator that appears in stationary iterative methods can also be incorporated in Krylov subspace methods such as GMRES (alternatively, preconditioned Krylov methods can be considered as accelerations of stationary iterative methods), where they become transformations of the original operator to a presumably better conditioned one. The construction of preconditioners is a large research area.

## Methods of successive approximation

Mathematical methods relating to successive approximation include:

- Babylonian method, for finding square roots of numbers
- Fixed-point iteration
- Means of finding zeros of functions:
  - Halley's method
  - Newton's method
- Differential-equation matters:
  - Picard–Lindelöf theorem, on existence of solutions of differential equations
  - Runge–Kutta methods, for numerical solution of differential equations

### History

Jamshīd al-Kāshī used iterative methods to calculate the sine of 1° and π in *The Treatise of Chord and Sine* to high precision. An early iterative method for solving a linear system appeared in a letter of Gauss to a student of his. He proposed solving a 4-by-4 system of equations by repeatedly solving the component in which the residual was the largest .

The theory of stationary iterative methods was solidly established with the work of D.M. Young starting in the 1950s. The conjugate gradient method was also invented in the 1950s, with independent developments by Cornelius Lanczos, Magnus Hestenes and Eduard Stiefel, but its nature and applicability were misunderstood at the time. Only in the 1970s was it realized that conjugacy based methods work very well for partial differential equations, especially the elliptic type.
