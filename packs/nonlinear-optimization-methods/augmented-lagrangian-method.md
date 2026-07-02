---
title: "Augmented Lagrangian method"
source: https://en.wikipedia.org/wiki/Augmented_Lagrangian_method
domain: nonlinear-optimization-methods
license: CC-BY-SA-4.0
tags: nonlinear programming, sequential quadratic programming, trust region, gauss-newton algorithm
fetched: 2026-07-02
---

# Augmented Lagrangian method

**Augmented Lagrangian methods** are a certain class of algorithms for solving constrained optimization problems. They have similarities to penalty methods in that they replace a constrained optimization problem by a series of unconstrained problems and add a penalty term to the objective, but the augmented Lagrangian method adds yet another term designed to mimic a Lagrange multiplier. The augmented Lagrangian is related to, but not identical with, the method of Lagrange multipliers.

Viewed differently, the unconstrained objective is the Lagrangian of the constrained problem, with an additional penalty term (the **augmentation**).

The method was originally known as the **method of multipliers** and was studied in the 1970s and 1980s as a potential alternative to penalty methods. It was first discussed by Magnus Hestenes and then by Michael Powell in 1969. The method was studied by R. Tyrrell Rockafellar in relation to Fenchel duality, particularly in relation to proximal-point methods, Moreau–Yosida regularization, and maximal monotone operators; these methods were used in structural optimization. The method was also studied by Dimitri Bertsekas, notably in his 1982 book, together with extensions involving non-quadratic regularization functions (e.g., entropic regularization). This combined study gives rise to the "exponential method of multipliers" which handles inequality constraints with a twice-differentiable augmented Lagrangian function.

Since the 1970s, sequential quadratic programming (SQP) and interior point methods (IPM) have been given more attention, in part because they more easily use sparse matrix subroutines from numerical software libraries, and in part because IPMs possess proven complexity results via the theory of self-concordant functions. The augmented Lagrangian method was rejuvenated by the optimization systems LANCELOT, ALGENCAN and AMPL, which allowed sparse matrix techniques to be used on seemingly dense but "partially-separable" problems. The method is still useful for some problems.

Around 2007, there was a resurgence of augmented Lagrangian methods in fields such as total variation denoising and compressed sensing. In particular, a variant of the standard augmented Lagrangian method that uses partial updates (similar to the Gauss–Seidel method for solving linear equations) known as the **alternating direction method of multipliers** or **ADMM** gained some attention.

## General method

Consider solving the following constrained optimization problem:

$\min f(\mathbf {x} )$

subject to

$c_{i}(\mathbf {x} )=0~\forall i\in {\mathcal {E}},$

where ${\mathcal {E}}$ denotes the indices for equality constraints. This problem can be solved as a series of unconstrained minimization problems. For reference, we first list the *k*th step of the penalty method approach:

$\min \Phi _{k}(\mathbf {x} )=f(\mathbf {x} )+\mu _{k}~\sum _{i\in {\mathcal {E}}}~c_{i}(\mathbf {x} )^{2}.$

The penalty method solves this problem, then at the next iteration it re-solves the problem using a larger value of $\mu _{k}$ and using the old solution as the initial guess or "warm start".

The augmented Lagrangian method uses the following unconstrained objective:

$\min \Phi _{k}(\mathbf {x} )=f(\mathbf {x} )+{\frac {\mu _{k}}{2}}~\sum _{i\in {\mathcal {E}}}~c_{i}(\mathbf {x} )^{2}+\sum _{i\in {\mathcal {E}}}~\lambda _{i}c_{i}(\mathbf {x} )$

and after each iteration, in addition to updating $\mu _{k}$ , the variable $\lambda$ is also updated according to the rule

$\lambda _{i}\leftarrow \lambda _{i}+\mu _{k}c_{i}(\mathbf {x} _{k})$

where $\mathbf {x} _{k}$ is the solution to the unconstrained problem at the *k*th step (i.e. $\mathbf {x} _{k}={\text{argmin}}\Phi _{k}(\mathbf {x} )$ ).

The variable $\lambda$ is an estimate of the Lagrange multiplier, and the accuracy of this estimate improves at every step. The major advantage of the method is that unlike the penalty method, it is not necessary to take $\mu \rightarrow \infty$ in order to solve the original constrained problem. Because of the presence of the Lagrange multiplier term, $\mu$ can stay much smaller, and thus avoiding ill-conditioning. Nevertheless, it is common in practical implementations to project multipliers estimates in a large bounded set (safeguards) which avoids numerical instabilities and leads to strong theoretical convergence.

The method can be extended to handle inequality constraints. For a discussion of practical improvements, see refs.

## Alternating direction method of multipliers

The alternating direction method of multipliers (ADMM) is a variant of the augmented Lagrangian scheme that uses partial updates for the dual variables. This method is often applied to solve problems such as,

$\min _{x}f(x)+g(Mx).$

This is equivalent to the constrained problem,

$\min _{x,y}f(x)+g(y),\quad {\text{subject to}}\quad Mx=y.$

Though this change may seem trivial, the problem can now be attacked using methods of constrained optimization (in particular, the augmented Lagrangian method), and the objective function is separable in *x* and *y*. The dual update requires solving a proximity function in *x* and *y* at the same time; the ADMM technique allows this problem to be solved approximately by first solving for *x* with *y* fixed and then solving for *y* with *x* fixed. Rather than iterating this process until convergence (like the Jacobi method), the ADMM algorithm proceeds directly to updating the dual variable and then repeats the process. This is not equivalent to the exact minimization, but the method still converges to the correct solution under some assumptions. Because it does not minimize or approximately minimize the augmented Lagrangian, the algorithm is distinct from the ordinary augmented Lagrangian method.

The ADMM can be viewed as an application of the Douglas-Rachford splitting algorithm, and the Douglas-Rachford algorithm is in turn an instance of the Proximal point algorithm; details can be found in ref. There are several modern software packages, including YALL1 (2009), SpaRSA (2009) and SALSA (2009), which solve Basis pursuit and variants and use the ADMM. There are also packages which use the ADMM to solve more general problems, some of which can exploit multiple computing cores (e.g., SNAPVX (2015), parADMM (2016)).

## Stochastic optimization

Stochastic optimization considers the problem of minimizing a loss function with access to noisy samples of the (gradient of the) function. The goal is to have an estimate of the optimal parameter (minimizer) per new sample. With some modifications, ADMM can be used for stochastic optimization. In a stochastic setting, only noisy samples of a gradient are accessible, so an inexact approximation of the Lagrangian is used:

${\hat {\mathcal {L}}}_{\rho ,k}=f_{1}(x_{k})+\langle \nabla f(x_{k},\zeta _{k+1}),x\rangle +g(y)-z^{T}(Ax+By-c)+{\frac {\rho }{2}}\Vert Ax+By-c\Vert ^{2}+{\frac {\Vert x-x_{k}\Vert ^{2}}{2\eta _{k+1}}},$

where $\eta _{k+1}$ is a time-varying step size.

ADMM has been applied to solve regularized problems, where the function optimization and regularization can be carried out locally and then coordinated globally via constraints.

Regularized optimization problems are especially relevant in the high-dimensional regime as regularization is a natural mechanism to overcome ill-posedness and to encourage parsimony in the optimal solution (e.g., sparsity and low rank). ADMM's effectiveness for solving regularized problems may mean it could be useful for solving high-dimensional stochastic optimization problems.

## Alternative approaches

- Sequential quadratic programming
- Sequential linear programming
- Sequential linear-quadratic programming

## Software

Open source and non-free/commercial implementations of the augmented Lagrangian method:

- Accord.NET (C# implementation of augmented Lagrangian optimizer)
- ALGLIB (C# and C++ implementations of preconditioned augmented Lagrangian solver)
- PENNON (GPL 3, commercial license available)
- LANCELOT (free "internal use" license, paid commercial options)
- MINOS (also uses an augmented Lagrangian method for some types of problems).
- The code for Apache 2.0 licensed REASON is available online.
- ALGENCAN (Fortran implementation of augmented Lagrangian method with safeguards). Available online.
- NLOPT (C++ implementation of augmented Lagrangian optimizer, accessible from different programming languages)
- PyProximal (Python implementation of augmented Lagrangian method).
