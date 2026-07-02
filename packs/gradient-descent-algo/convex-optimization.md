---
title: "Convex optimization"
source: https://en.wikipedia.org/wiki/Convex_optimization
domain: gradient-descent-algo
license: CC-BY-SA-4.0
tags: gradient descent, stochastic gradient descent, backpropagation algorithm, convex optimization
fetched: 2026-07-02
---

# Convex optimization

**Convex optimization** is a subfield of mathematical optimization that studies the problem of minimizing convex functions over convex sets (or, equivalently, maximizing concave functions over convex sets). Many classes of convex optimization problems admit polynomial-time algorithms, whereas mathematical optimization is in general NP-hard.

## Definition

### Abstract form

A convex optimization problem is defined by two ingredients:

- The *objective function*, which is a real-valued convex function of *n* variables, $f:{\mathcal {D}}\subseteq \mathbb {R} ^{n}\to \mathbb {R}$ ;
- The *feasible set*, which is a convex subset $C\subseteq \mathbb {R} ^{n}$ .

The goal of the problem is to find some $\mathbf {x^{\ast }} \in C$ attaining

$\inf\{f(\mathbf {x} ):\mathbf {x} \in C\}$

.

In general, there are three options regarding the existence of a solution:

- If such a point *x** exists, it is referred to as an *optimal point* or *solution*; the set of all optimal points is called the *optimal set*; and the problem is called *solvable*.
- If f is unbounded below over C , or the infimum is not attained, then the optimization problem is said to be *unbounded*.
- Otherwise, if C is the empty set, then the problem is said to be *infeasible*.

### Standard form

A convex optimization problem is in *standard form* if it is written as

${\begin{aligned}&{\underset {\mathbf {x} }{\operatorname {minimize} }}&&f(\mathbf {x} )\\&\operatorname {subject\ to} &&g_{i}(\mathbf {x} )\leq 0,\quad i=1,\dots ,m\\&&&h_{i}(\mathbf {x} )=0,\quad i=1,\dots ,p,\end{aligned}}$

where:

- $\mathbf {x} \in \mathbb {R} ^{n}$ is the vector of optimization variables;
- The objective function $f:{\mathcal {D}}\subseteq \mathbb {R} ^{n}\to \mathbb {R}$ is a convex function;
- The inequality constraint functions $g_{i}:\mathbb {R} ^{n}\to \mathbb {R}$ , $i=1,\ldots ,m$ , are convex functions;
- The equality constraint functions $h_{i}:\mathbb {R} ^{n}\to \mathbb {R}$ , $i=1,\ldots ,p$ , are affine transformations, that is, of the form: $h_{i}(\mathbf {x} )=\mathbf {a_{i}} \cdot \mathbf {x} -b_{i}$ , where $\mathbf {a_{i}}$ is a vector and $b_{i}$ is a scalar.

The feasible set C of the optimization problem consists of all points $\mathbf {x} \in {\mathcal {D}}$ satisfying the inequality and the equality constraints. This set is convex because ${\mathcal {D}}$ is convex, the sublevel sets of convex functions are convex, affine sets are convex, and the intersection of convex sets is convex.

Many optimization problems can be equivalently formulated in this standard form. For example, the problem of maximizing a concave function f can be re-formulated equivalently as the problem of minimizing the convex function $-f$ . The problem of maximizing a concave function over a convex set is commonly called a convex optimization problem.

### Epigraph form (standard form with linear objective)

In the standard form it is possible to assume, without loss of generality, that the objective function *f* is a linear function. This is because any program with a general objective can be transformed into a program with a linear objective by adding a single variable t and a single constraint, as follows:

${\begin{aligned}&{\underset {\mathbf {x} ,t}{\operatorname {minimize} }}&&t\\&\operatorname {subject\ to} &&f(\mathbf {x} )-t\leq 0\\&&&g_{i}(\mathbf {x} )\leq 0,\quad i=1,\dots ,m\\&&&h_{i}(\mathbf {x} )=0,\quad i=1,\dots ,p,\end{aligned}}$

### Conic form

Every convex program can be presented in a *conic form*, which means minimizing a linear objective over the intersection of an affine plane and a convex cone:

${\begin{aligned}&{\underset {\mathbf {x} }{\operatorname {minimize} }}&&c^{T}x\\&\operatorname {subject\ to} &&x\in (b+L)\cap K\end{aligned}}$

where K is a closed pointed convex cone, L is a linear subspace of R*n*, and b is a vector in R*n*. A linear program in standard form is the special case in which K is the nonnegative orthant of R*n*.

### Eliminating linear equality constraints

It is possible to convert a convex program in standard form, to a convex program with no equality constraints. Denote the equality constraints *hi*(*x*)=0 as *Ax*=*b*, where *A* has *n* columns. If *Ax*=*b* is infeasible, then of course the original problem is infeasible. Otherwise, it has some solution *x*0 , and the set of all solutions can be presented as: *Fz*+*x*0, where *z* is in *Rk*, *k*=*n*-rank(*A*), and *F* is an *n*-by-*k* matrix. Substituting *x* = *Fz*+*x*0 in the original problem gives:

> ${\begin{aligned}&{\underset {\mathbf {x} }{\operatorname {minimize} }}&&f(\mathbf {F\mathbf {z} +\mathbf {x} _{0}} )\\&\operatorname {subject\ to} &&g_{i}(\mathbf {F\mathbf {z} +\mathbf {x} _{0}} )\leq 0,\quad i=1,\dots ,m\\\end{aligned}}$

where the variables are **z**. Note that there are rank(*A*) fewer variables. This means that, in principle, one can restrict attention to convex optimization problems without equality constraints. In practice, however, it is often preferred to retain the equality constraints, since they might make some algorithms more efficient, and also make the problem easier to understand and analyze.

## Special cases

The following problem classes are all convex optimization problems, or can be reduced to convex optimization problems via simple transformations:

- Linear programming problems are the simplest convex programs. In LP, the objective and constraint functions are all linear.
- Quadratic programming are the next-simplest. In QP, the constraints are all linear, but the objective may be a convex quadratic function.
- Second order cone programming are more general.
- Semidefinite programming are more general.
- Conic optimization are even more general - see figure to the right,

Other special cases include;

- Least squares
- Quadratic minimization with convex quadratic constraints
- Geometric programming
- Entropy maximization with appropriate constraints.

## Properties

The following are useful properties of convex optimization problems:

- every point that is local minimum is also a global minimum;
- the optimal set is convex;
- if the objective function is *strictly* convex, then the problem has at most one optimal point.

These results are used by the theory of convex minimization along with geometric notions from functional analysis (in Hilbert spaces) such as the Hilbert projection theorem, the separating hyperplane theorem, and Farkas' lemma.

## Algorithms

### Unconstrained and equality-constrained problems

The convex programs easiest to solve are the *unconstrained* problems, or the problems with only equality constraints. As the equality constraints are all linear, they can be eliminated with linear algebra and integrated into the objective, thus converting an equality-constrained problem into an unconstrained one.

In the class of unconstrained (or equality-constrained) problems, the simplest ones are those in which the objective is quadratic. For these problems, the KKT conditions (which are necessary for optimality) are all linear, so they can be solved analytically.

For unconstrained (or equality-constrained) problems with a general convex objective that is twice-differentiable, Newton's method can be used. It can be seen as reducing a general unconstrained convex problem, to a sequence of quadratic problems.Newton's method can be combined with line search for an appropriate step size, and it can be mathematically proven to converge quickly.

Other efficient algorithms for unconstrained minimization are gradient descent (a special case of steepest descent).

### General problems

The more challenging problems are those with inequality constraints. A common way to solve them is to reduce them to unconstrained problems by adding a barrier function, enforcing the inequality constraints, to the objective function. Such methods are called interior point methods.They have to be initialized by finding a feasible interior point using by so-called *phase I* methods, which either find a feasible point or show that none exist. Phase I methods generally consist of reducing the search in question to a simpler convex optimization problem.

Convex optimization problems can also be solved by the following contemporary methods:

- Bundle methods (Wolfe, Lemaréchal, Kiwiel), and
- Subgradient projection methods (Polyak),
- Interior-point methods, which make use of self-concordant barrier functions and self-regular barrier functions.
- Cutting-plane methods
- Ellipsoid method
- Subgradient method
- Dual subgradients and the drift-plus-penalty method

Subgradient methods can be implemented simply and so are widely used. Dual subgradient methods are subgradient methods applied to a dual problem. The drift-plus-penalty method is similar to the dual subgradient method, but takes a time average of the primal variables.

## Lagrange multipliers

Consider a convex minimization problem given in standard form by a cost function $f(x)$ and inequality constraints $g_{i}(x)\leq 0$ for $1\leq i\leq m$ . Then the domain ${\mathcal {X}}$ is:

${\mathcal {X}}=\left\{x\in X\vert g_{1}(x),\ldots ,g_{m}(x)\leq 0\right\}.$

The Lagrangian function for the problem is

$L(x,\lambda _{0},\lambda _{1},\ldots ,\lambda _{m})=\lambda _{0}f(x)+\lambda _{1}g_{1}(x)+\cdots +\lambda _{m}g_{m}(x).$

For each point x in X that minimizes f over X , there exist real numbers $\lambda _{0},\lambda _{1},\ldots ,\lambda _{m},$ called Lagrange multipliers, that satisfy these conditions simultaneously:

1. x minimizes $L(y,\lambda _{0},\lambda _{1},\ldots ,\lambda _{m})$ over all $y\in X,$
2. $\lambda _{0},\lambda _{1},\ldots ,\lambda _{m}\geq 0,$ with at least one $\lambda _{k}>0,$
3. $\lambda _{1}g_{1}(x)=\cdots =\lambda _{m}g_{m}(x)=0$ (complementary slackness).

If there exists a "strictly feasible point", that is, a point z satisfying

$g_{1}(z),\ldots ,g_{m}(z)<0,$

then the statement above can be strengthened to require that $\lambda _{0}=1$ .

Conversely, if some x in X satisfies (1)–(3) for scalars $\lambda _{0},\ldots ,\lambda _{m}$ with $\lambda _{0}=1$ then x is certain to minimize f over X .

## Software

There is a large software ecosystem for convex optimization. This ecosystem has two main categories: *solvers* on the one hand and *modeling tools* (or *interfaces*) on the other hand.

Solvers implement the algorithms themselves and are usually written in C. They require users to specify optimization problems in very specific formats which may not be natural from a modeling perspective. Modeling tools are separate pieces of software that let the user specify an optimization in higher-level syntax. They manage all transformations to and from the user's high-level model and the solver's input/output format.

Below are two tables. The first shows modelling tools (such as CVXPY and JuMP.jl) and the second shows solvers (such as SCS and MOSEK). They are by no means exhaustive.

| Program | Language | Description | FOSS? | Ref. |
|---|---|---|---|---|
| CVX | MATLAB | Interfaces with SeDuMi and SDPT3 solvers; designed to only express convex optimization problems. | Yes |   |
| CVXPY | Python |   | Yes |   |
| Convex.jl | Julia | Disciplined convex programming, supports many solvers. | Yes |   |
| CVXR | R |   | Yes |   |
| GAMS |   | Modeling system for linear, nonlinear, mixed integer linear/nonlinear, and second-order cone programming problems. | No |   |
| GloptiPoly | MATLAB, Octave | Modeling system for polynomial optimization. | Yes |   |
| JuMP.jl | Julia | Supports many solvers. Also supports integer and nonlinear optimization, and some nonconvex optimization. | Yes |   |
| ROME |   | Modeling system for robust optimization. Supports distributionally robust optimization and uncertainty sets. | Yes |   |
| SOSTOOLS |   | Modeling system for polynomial optimization. Uses SDPT3 and SeDuMi. Requires Symbolic Computation Toolbox. | Yes |   |
| SparsePOP |   | Modeling system for polynomial optimization. Uses the SDPA or SeDuMi solvers. | Yes |   |
| YALMIP | MATLAB, Octave | Interfaces with CPLEX, GUROBI, MOSEK, SDPT3, SEDUMI, CSDP, SDPA, PENNON solvers; also supports integer and nonlinear optimization, and some nonconvex optimization. Can perform robust optimization with uncertainty in LP/SOCP/SDP constraints. | Yes |   |

| Program | Language | Description | FOSS? | Ref. |
|---|---|---|---|---|
| AIMMS |   | Can do robust optimization on linear programming (with MOSEK to solve second-order cone programming) and mixed integer linear programming. Modeling package for LP + SDP and robust versions. | No |   |
| CPLEX |   | Supports primal-dual methods for LP + SOCP. Can solve LP, QP, SOCP, and mixed integer linear programming problems. | No |   |
| CSDP | C | Supports primal-dual methods for LP + SDP. Interfaces available for MATLAB, R, and Python. Parallel version available. SDP solver. | Yes |   |
| CVXOPT | Python | Supports primal-dual methods for LP + SOCP + SDP. Uses Nesterov-Todd scaling. Interfaces to MOSEK and DSDP. | Yes |   |
| MOSEK |   | Supports primal-dual methods for LP + SOCP. | No |   |
| SeDuMi | MATLAB, Octave, MEX | Solves LP + SOCP + SDP. Supports primal-dual methods for LP + SOCP + SDP. | Yes |   |
| SDPA | C++ | Solves LP + SDP. Supports primal-dual methods for LP + SDP. Parallelized and extended precision versions are available. | Yes |   |
| SDPT3 | MATLAB, Octave, MEX | Solves LP + SOCP + SDP. Supports primal-dual methods for LP + SOCP + SDP. | Yes |   |
| ConicBundle |   | Supports general-purpose codes for LP + SOCP + SDP. Uses a bundle method. Special support for SDP and SOCP constraints. | Yes |   |
| DSDP |   | Supports general-purpose codes for LP + SDP. Uses a dual interior point method. | Yes |   |
| LOQO |   | Supports general-purpose codes for SOCP, which it treats as a nonlinear programming problem. | No |   |
| PENNON |   | Supports general-purpose codes. Uses an augmented Lagrangian method, especially for problems with SDP constraints. | No |   |
| SDPLR |   | Supports general-purpose codes. Uses low-rank factorization with an augmented Lagrangian method. | Yes |   |

## Applications

Convex optimization can be used to model problems in a wide range of disciplines, such as automatic control systems, estimation and signal processing, communications and networks, electronic circuit design, data analysis and modeling, finance, statistics (optimal experimental design), and structural optimization, where the approximation concept has proven to be efficient. Convex optimization can be used to model problems in the following fields:

- Portfolio optimization.
- Worst-case risk analysis.
- Optimal advertising.
- Variations of statistical regression (including regularization and quantile regression).
- Model fitting (particularly multiclass classification).
- Electricity generation optimization.
- Combinatorial optimization.
- Non-probabilistic modelling of uncertainty.
- Localization using wireless signals

## Extensions

Extensions of convex optimization include the optimization of biconvex, pseudo-convex, and quasiconvex functions. Extensions of the theory of convex analysis and iterative methods for approximately solving non-convex minimization problems occur in the field of generalized convexity, also known as abstract convex analysis.
