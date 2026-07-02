---
title: "Sequential quadratic programming"
source: https://en.wikipedia.org/wiki/Sequential_quadratic_programming
domain: nonlinear-optimization-methods
license: CC-BY-SA-4.0
tags: nonlinear programming, sequential quadratic programming, trust region, gauss-newton algorithm
fetched: 2026-07-02
---

# Sequential quadratic programming

**Sequential quadratic programming** (**SQP**) is an iterative method for constrained nonlinear optimization, also known as Lagrange-Newton method. SQP methods are used on mathematical problems for which the objective function and the constraints are twice continuously differentiable, but not necessarily convex.

SQP methods solve a sequence of optimization subproblems, each of which optimizes a quadratic model of the objective subject to a linearization of the constraints. If the problem is unconstrained, then the method reduces to Newton's method for finding a point where the gradient of the objective vanishes. If the problem has only equality constraints, then the method is equivalent to applying Newton's method to the first-order optimality conditions, or Karush–Kuhn–Tucker conditions, of the problem.

## Algorithm basics

Consider a nonlinear programming problem of the form:

${\begin{array}{rl}\min \limits _{x}&f(x)\\{\mbox{subject to}}&h(x)\geq 0\\&g(x)=0.\end{array}}$

where $x\in \mathbb {R} ^{n}$ , $f:\mathbb {R} ^{n}\rightarrow \mathbb {R}$ , $h:\mathbb {R} ^{n}\rightarrow \mathbb {R} ^{m_{I}}$ and $g:\mathbb {R} ^{n}\rightarrow \mathbb {R} ^{m_{E}}$ .

The Lagrangian for this problem is

${\mathcal {L}}(x,\lambda ,\sigma )=f(x)+\lambda h(x)+\sigma g(x),$

where $\lambda$ and $\sigma$ are Lagrange multipliers.

### The equality constrained case

If the problem does not have inequality constraints (that is, $m_{I}=0$ ), the first-order optimality conditions (aka KKT conditions) $\nabla {\mathcal {L}}(x,\sigma )=0$ are a set of nonlinear equations that may be iteratively solved with Newton's Method. Newton's method linearizes the KKT conditions at the current iterate $\left[x_{k},\sigma _{k}\right]^{T}$ , which provides the following expression for the Newton step $\left[d_{x},d_{\sigma }\right]^{T}$ :

${\begin{bmatrix}d_{x}\\d_{\sigma }\end{bmatrix}}=-[\nabla _{xx}^{2}{\mathcal {L}}(x_{k},\sigma _{k})]^{-1}\nabla _{x}{\mathcal {L}}(x_{k},\sigma _{k})=-{\begin{bmatrix}\nabla _{xx}^{2}{\mathcal {L}}(x_{k},\sigma _{k})&\nabla g(x_{k},\sigma _{k})\\\nabla g^{T}(x_{k},\sigma _{k})&0\end{bmatrix}}^{-1}{\begin{bmatrix}\nabla f(x_{k})+\sigma _{k}\nabla g(x_{k})\\g(x_{k})\end{bmatrix}}$ ,

where $\nabla _{xx}^{2}{\mathcal {L}}(x_{k},\sigma _{k})$ denotes the Hessian matrix of the Lagrangian, and $d_{x}$ and $d_{\sigma }$ are the primal and dual displacements, respectively. Note that the Lagrangian Hessian is not explicitly inverted and a linear system is solved instead.

When the Lagrangian Hessian $\nabla ^{2}{\mathcal {L}}(x_{k},\sigma _{k})$ is not positive definite, the Newton step may not exist or it may characterize a stationary point that is not a local minimum (but rather, a local maximum or a saddle point). In this case, the Lagrangian Hessian must be regularized, for example one can add a multiple of the identity to it such that the resulting matrix is positive definite.

An alternative view for obtaining the primal-dual displacements is to construct and solve a local quadratic model of the original problem at the current iterate:

${\begin{array}{rl}\min \limits _{d_{x}}&f(x_{k})+\nabla f(x_{k})^{T}d_{x}+{\frac {1}{2}}d_{x}^{T}\nabla _{xx}^{2}{\mathcal {L}}(x_{k},\sigma _{k})d_{x}\\\mathrm {s.t.} &g(x_{k})+\nabla g(x_{k})^{T}d_{x}=0.\end{array}}$

The optimality conditions of this quadratic problem correspond to the linearized KKT conditions of the original problem. Note that the term $f(x_{k})$ in the expression above may be left out, since it is constant under the $\min \limits _{d}$ operator.

### The inequality constrained case

In the presence of inequality constraints ( $m_{I}>0$ ), we can naturally extend the definition of the local quadratic model introduced in the previous section:

${\begin{array}{rl}\min \limits _{d}&f(x_{k})+\nabla f(x_{k})^{T}d+{\frac {1}{2}}d^{T}\nabla _{xx}^{2}{\mathcal {L}}(x_{k},\lambda _{k},\sigma _{k})d\\\mathrm {s.t.} &h(x_{k})+\nabla h(x_{k})^{T}d\geq 0\\&g(x_{k})+\nabla g(x_{k})^{T}d=0.\end{array}}$

### The SQP algorithm

The SQP algorithm starts from the initial iterate $(x_{0},\lambda _{0},\sigma _{0})$ . At each iteration, the QP subproblem is built and solved; the resulting Newton step direction $[d_{x},d_{\lambda },d_{\sigma }]^{T}$ is used to update current iterate:

$\left[x_{k+1},\lambda _{k+1},\sigma _{k+1}\right]^{T}=\left[x_{k},\lambda _{k},\sigma _{k}\right]^{T}+[d_{x},d_{\lambda },d_{\sigma }]^{T}.$

This process is repeated for $k=0,1,2,\ldots$ until some convergence criterion is satisfied.

## Practical implementations

Practical implementations of the SQP algorithm are significantly more complex than its basic version above. To adapt SQP for real-world applications, the following challenges must be addressed:

- The possibility of an infeasible QP subproblem.
- QP subproblem yielding a bad step: one that either fails to reduce the target or increases constraints violation.
- Breakdown of iterations due to significant deviation of the target/constraints from their quadratic/linear models.

To overcome these challenges, various strategies are typically employed:

- Use of merit functions, which assess progress towards a constrained solution, non-monotonic steps or filter methods.
- Trust region or line search methods to manage deviations between the quadratic model and the actual target.
- Special feasibility restoration phases to handle infeasible subproblems, or the use of L1-penalized subproblems to gradually decrease infeasibility

These strategies can be combined in numerous ways, resulting in a diverse range of SQP methods.

## Alternative approaches

- Sequential linear programming
- Sequential linear-quadratic programming
- Augmented Lagrangian method

## Implementations

SQP methods have been implemented in well known numerical environments such as MATLAB and GNU Octave. There also exist numerous software libraries, including open source:

- SciPy (de facto standard for scientific Python) has scipy.optimize.minimize(method='SLSQP') solver.
- NLopt (C/C++ implementation, with numerous interfaces including Julia, Python, R, MATLAB/Octave), implemented by Dieter Kraft as part of a package for optimal control, and modified by S. G. Johnson.
- ALGLIB SQP solver (C++, C#, Java, Python API)
- acados (C with interfaces to Python, MATLAB, Simulink, Octave) implements a SQP method tailored to the problem structure arising in optimal control, but tackles also general nonlinear programs.

and commercial

- LabVIEW
- KNITRO (C, C++, C#, Java, Python, Julia, Fortran)
- NPSOL (Fortran)
- SNOPT (Fortran)
- NLPQL (Fortran)
- MATLAB
- SuanShu (Java)
