---
title: "Frank–Wolfe algorithm"
source: https://en.wikipedia.org/wiki/Frank–Wolfe_algorithm
domain: gradient-descent-variants
license: CC-BY-SA-4.0
tags: gradient descent variants, momentum method, nesterov acceleration, adagrad rmsprop
fetched: 2026-07-02
---

# Frank–Wolfe algorithm

The **Frank–Wolfe algorithm** is an iterative first-order optimization algorithm for constrained convex optimization. Also known as the **conditional gradient method**, **reduced gradient algorithm** and the **convex combination algorithm**, the method was originally proposed by Marguerite Frank and Philip Wolfe in 1956. In each iteration, the Frank–Wolfe algorithm considers a linear approximation of the objective function, and moves towards a minimizer of this linear function (taken over the same domain).

## Problem statement

Suppose ${\mathcal {D}}$ is a compact convex set in a vector space and $f\colon {\mathcal {D}}\to \mathbb {R}$ is a convex, differentiable real-valued function. The Frank–Wolfe algorithm solves the optimization problem

Minimize

$f(\mathbf {x} )$

subject to

$\mathbf {x} \in {\mathcal {D}}$

.

## Algorithm

Initialization:

Let

$k\leftarrow 0$

, and let

$\mathbf {x} _{0}\!$

be any point in

${\mathcal {D}}$

.

Step 1.

Direction-finding subproblem:

Find

$\mathbf {s} _{k}$

solving

Minimize

$\mathbf {s} ^{T}\nabla f(\mathbf {x} _{k})$

Subject to

$\mathbf {s} \in {\mathcal {D}}$

(Interpretation: Minimize the linear approximation of the problem given by the first-order

Taylor approximation

of

f

around

$\mathbf {x} _{k}\!$

constrained to stay within

${\mathcal {D}}$

.)

Step 2.

Step size determination:

Set

$\alpha \leftarrow {\frac {2}{k+2}}$

, or alternatively find

$\alpha$

that minimizes

$f(\mathbf {x} _{k}+\alpha (\mathbf {s} _{k}-\mathbf {x} _{k}))$

subject to

$0\leq \alpha \leq 1$

.

Step 3.

Update:

Let

$\mathbf {x} _{k+1}\leftarrow \mathbf {x} _{k}+\alpha (\mathbf {s} _{k}-\mathbf {x} _{k})$

, let

$k\leftarrow k+1$

and go to Step 1.

## Properties

While competing methods such as gradient descent for constrained optimization require a projection step back to the feasible set in each iteration, the Frank–Wolfe algorithm only needs the solution of a convex problem over the same set in each iteration, and automatically stays in the feasible set.

The convergence of the Frank–Wolfe algorithm is sublinear in general: the error in the objective function to the optimum is $O(1/k)$ after *k* iterations, so long as the gradient is Lipschitz continuous with respect to some norm. The same convergence rate can also be shown if the sub-problems are only solved approximately.

The iterations of the algorithm can always be represented as a sparse convex combination of the extreme points of the feasible set, which has helped to the popularity of the algorithm for sparse greedy optimization in machine learning and signal processing problems, as well as for example the optimization of minimum–cost flows in transportation networks.

If the feasible set is given by a set of linear constraints, then the subproblem to be solved in each iteration becomes a linear program.

While the worst-case convergence rate with $O(1/k)$ can not be improved in general, faster convergence can be obtained for special problem classes, such as some strongly convex problems.

## Lower bounds on the solution value, and primal-dual analysis

Since f is convex, for any two points $\mathbf {x} ,\mathbf {y} \in {\mathcal {D}}$ we have:

$f(\mathbf {y} )\geq f(\mathbf {x} )+(\mathbf {y} -\mathbf {x} )^{T}\nabla f(\mathbf {x} )$

This also holds for the (unknown) optimal solution $\mathbf {x} ^{*}$ . That is, $f(\mathbf {x} ^{*})\geq f(\mathbf {x} )+(\mathbf {x} ^{*}-\mathbf {x} )^{T}\nabla f(\mathbf {x} )$ . The best lower bound with respect to a given point $\mathbf {x}$ is given by

${\begin{aligned}f(\mathbf {x} ^{*})&\geq f(\mathbf {x} )+(\mathbf {x} ^{*}-\mathbf {x} )^{T}\nabla f(\mathbf {x} )\\&\geq \min _{\mathbf {y} \in D}\left\{f(\mathbf {x} )+(\mathbf {y} -\mathbf {x} )^{T}\nabla f(\mathbf {x} )\right\}\\&=f(\mathbf {x} )-\mathbf {x} ^{T}\nabla f(\mathbf {x} )+\min _{\mathbf {y} \in D}\mathbf {y} ^{T}\nabla f(\mathbf {x} )\end{aligned}}$

The latter optimization problem is solved in every iteration of the Frank–Wolfe algorithm, therefore the solution $\mathbf {s} _{k}$ of the direction-finding subproblem of the k -th iteration can be used to determine increasing lower bounds $l_{k}$ during each iteration by setting $l_{0}=-\infty$ and

$l_{k}:=\max(l_{k-1},f(\mathbf {x} _{k})+(\mathbf {s} _{k}-\mathbf {x} _{k})^{T}\nabla f(\mathbf {x} _{k}))$

Such lower bounds on the unknown optimal value are important in practice because they can be used as a stopping criterion, and give an efficient certificate of the approximation quality in every iteration, since always $l_{k}\leq f(\mathbf {x} ^{*})\leq f(\mathbf {x} _{k})$ .

It has been shown that this corresponding duality gap, that is the difference between $f(\mathbf {x} _{k})$ and the lower bound $l_{k}$ , decreases with the same convergence rate, i.e. $f(\mathbf {x} _{k})-l_{k}=O(1/k).$

## Applications

The Frank-Wolfe algorithm can be used to compute a Wardrop equilibrium.
