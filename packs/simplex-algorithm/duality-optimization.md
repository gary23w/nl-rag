---
title: "Duality (optimization)"
source: https://en.wikipedia.org/wiki/Duality_(optimization)
domain: simplex-algorithm
license: CC-BY-SA-4.0
tags: simplex algorithm, linear programming, interior point method, duality theorem
fetched: 2026-07-02
---

# Duality (optimization)

In mathematical optimization theory, **duality** or the **duality principle** is the principle that optimization problems may be viewed from either of two perspectives, the **primal problem** or the **dual problem**. If the primal is a minimization problem then the dual is a maximization problem (and vice versa). Any feasible solution to the primal (minimization) problem is at least as large as any feasible solution to the dual (maximization) problem. Therefore, the solution to the primal is an upper bound to the solution of the dual, and the solution of the dual is a lower bound to the solution of the primal. This fact is called **weak duality**.

In general, the optimal values of the primal and dual problems need not be equal. Their difference is called the duality gap. For convex optimization problems, the duality gap is zero under a constraint qualification condition. This fact is called **strong duality**.

## Dual problem

Usually the term "dual problem" refers to the *Lagrangian dual problem* but other dual problems are used – for example, the Wolfe dual problem and the Fenchel dual problem. The Lagrangian dual problem is obtained by forming the Lagrangian of a minimization problem by using nonnegative Lagrange multipliers to add the constraints to the objective function, and then solving for the primal variable values that minimize the original objective function. This solution gives the primal variables as functions of the Lagrange multipliers, which are called dual variables, so that the new problem is to maximize the objective function with respect to the dual variables under the derived constraints on the dual variables (including at least the nonnegativity constraints).

In general given two dual pairs of separated locally convex spaces $\left(X,X^{*}\right)$ and $\left(Y,Y^{*}\right)$ and the function $f:X\to \mathbb {R} \cup \{+\infty \}$ , we can define the primal problem as finding ${\hat {x}}$ such that $f({\hat {x}})=\inf _{x\in X}f(x).\,$ In other words, if ${\hat {x}}$ exists, $f({\hat {x}})$ is the minimum of the function f and the infimum (greatest lower bound) of the function is attained.

If there are constraint conditions, these can be built into the function f by letting ${\tilde {f}}=f+I_{\mathrm {constraints} }$ where $I_{\mathrm {constraints} }$ is a suitable function on X that has a minimum 0 on the constraints, and for which one can prove that $\inf _{x\in X}{\tilde {f}}(x)=\inf _{x\ \mathrm {constrained} }f(x)$ . The latter condition is trivially, but not always conveniently, satisfied for the characteristic function (i.e. $I_{\mathrm {constraints} }(x)=0$ for x satisfying the constraints and $I_{\mathrm {constraints} }(x)=\infty$ otherwise). Then extend ${\tilde {f}}$ to a perturbation function $F:X\times Y\to \mathbb {R} \cup \{+\infty \}$ such that $F(x,0)={\tilde {f}}(x)$ .

The duality gap is the difference of the right and left hand sides of the inequality

$\sup _{y^{*}\in Y^{*}}-F^{*}(0,y^{*})\leq \inf _{x\in X}F(x,0),\,$

where $F^{*}$ is the convex conjugate in both variables and $\sup$ denotes the supremum (least upper bound).

### Duality gap

The duality gap is the difference between the values of any primal solutions and any dual solutions. If $d^{*}$ is the optimal dual value and $p^{*}$ is the optimal primal value, then the duality gap is equal to $p^{*}-d^{*}$ . This value is always greater than or equal to 0 (for minimization problems). The duality gap is zero if and only if strong duality holds. Otherwise the gap is strictly positive and weak duality holds.

In computational optimization, another "duality gap" is often reported, which is the difference in value between any dual solution and the value of a feasible but suboptimal iterate for the primal problem. This alternative "duality gap" quantifies the discrepancy between the value of a current feasible but suboptimal iterate for the primal problem and the value of the dual problem; the value of the dual problem is, under regularity conditions, equal to the value of the *convex relaxation* of the primal problem: The convex relaxation is the problem arising replacing a non-convex feasible set with its closed convex hull and with replacing a non-convex function with its convex closure, that is the function that has the epigraph that is the closed convex hull of the original primal objective function.

## Linear case

Linear programming problems are optimization problems in which the objective function and the constraints are all linear. In the primal problem, the objective function is a linear combination of *n* variables. There are *m* constraints, each of which places an upper bound on a linear combination of the *n* variables. The goal is to maximize the value of the objective function subject to the constraints. A *solution* is a vector (a list) of *n* values that achieves the maximum value for the objective function.

In the dual problem, the objective function is a linear combination of the *m* values that are the limits in the *m* constraints from the primal problem. There are *n* dual constraints, each of which places a lower bound on a linear combination of *m* dual variables.

### Relationship between the primal problem and the dual problem

In the linear case, in the primal problem, from each sub-optimal point that satisfies all the constraints, there is a direction or subspace of directions to move that increases the objective function. Moving in any such direction is said to remove slack between the candidate solution and one or more constraints. An *infeasible* value of the candidate solution is one that exceeds one or more of the constraints.

In the dual problem, the dual vector multiplies the constraints that determine the positions of the constraints in the primal. Varying the dual vector in the dual problem is equivalent to revising the upper bounds in the primal problem. The lowest upper bound is sought. That is, the dual vector is minimized in order to remove slack between the candidate positions of the constraints and the actual optimum. An infeasible value of the dual vector is one that is too low. It sets the candidate positions of one or more of the constraints in a position that excludes the actual optimum.

This intuition is made formal by the equations in Linear programming: Duality.

## Nonlinear case

In nonlinear programming, the constraints are not necessarily linear. Nonetheless, many of the same principles apply.

To ensure that the global maximum of a non-linear problem can be identified easily, the problem formulation often requires that the functions be convex and have compact lower level sets. This is the significance of the Karush–Kuhn–Tucker conditions. They provide necessary conditions for identifying local optima of non-linear programming problems. There are additional conditions (constraint qualifications) that are necessary so that it will be possible to define the direction to an *optimal* solution. An optimal solution is one that is a local optimum, but possibly not a global optimum.

### Lagrange duality

**Motivation**

Suppose we want to solve the following nonlinear programming problem:

> ${\begin{aligned}{\text{minimize }}&f_{0}(x)\\{\text{subject to }}&f_{i}(x)\leq 0,\ i\in \left\{1,\ldots ,m\right\}\\\end{aligned}}$

The problem has constraints; we would like to convert it to a program without constraints. Theoretically, it is possible to do it by minimizing the function $J(x)$ , defined as

> $J(x)=f_{0}(x)+\sum _{i}I[f_{i}(x)]$

where I is an infinite step function: $I[u]=0$ if $u\leq 0$ , and $I[u]=\infty$ otherwise. But $J(x)$ is hard to solve as it is not continuous. It is possible to "approximate" $I[u]$ by $\lambda u$ , where $\lambda$ is a positive constant. This yields a function known as the Lagrangian:

> $L(x,\lambda )=f_{0}(x)+\sum _{i}\lambda _{i}f_{i}(x)$

Note that, for every x ,

> $\max _{\lambda \geq 0}L(x,\lambda )=J(x)$ .

*Proof*:

- If x satisfies all constraints $f_{i}(x)\leq 0$ , then $L(x,\lambda )$ is maximized when taking $\lambda =0$ , and its value is then $f(x)$ ;
- If x violates some constraint, $f_{i}(x)>0$ for some i , then $L(x,\lambda )\to \infty$ when $\lambda _{i}\to \infty$ .

Therefore, the original problem is equivalent to:

> $\min _{x}\max _{\lambda \geq 0}L(x,\lambda )$ .

By reversing the order of min and max, we get:

> $\max _{\lambda \geq 0}\min _{x}L(x,\lambda )$ .

The *dual function* is the inner problem in the above formula:

> $g(\lambda ):=\min _{x}L(x,\lambda )$ .

The **Lagrangian dual program** is the program of maximizing g:

> $\max _{\lambda \geq 0}g(\lambda )$ .

The optimal solution to the dual program is a lower bound for the optimal solution of the original (primal) program; this is the *weak duality* principle. If the primal problem is convex and bounded from below, and there exists a point in which all nonlinear constraints are strictly satisfied (Slater's condition), then the optimal solution to the dual program *equals* the optimal solution of the primal program; this is the *strong duality* principle. In this case, we can solve the primal program by finding an optimal solution $\lambda ^{*}$ to the dual program, and then solving:

> $\min _{x}L(x,\lambda ^{*})$ .

Note that, to use either the weak or the strong duality principle, we need a way to compute $g(\lambda )$ . In general this may be hard, as we need to solve a different minimization problem for every $\lambda$ . But for some classes of functions, it is possible to get an explicit formula for $g(\lambda )$ . Solving the primal and dual programs together is often easier than solving only one of them. Examples are linear programming and quadratic programming. A better and more general approach to duality is provided by Fenchel's duality theorem.

Another condition in which the min-max and max-min are equal is when the Lagrangian has a saddle point: $(x^{*},\lambda ^{*})$ is a saddle point of the Lagrange function L if and only if $x^{*}$ is an optimal solution to the primal, $\lambda ^{*}$ is an optimal solution to the dual, and the optimal values in the indicated problems are equal to each other.

### The strong Lagrange principle

Given a nonlinear programming problem in standard form

${\begin{aligned}{\text{minimize }}&f_{0}(x)\\{\text{subject to }}&f_{i}(x)\leq 0,\ i\in \left\{1,\ldots ,m\right\}\\&h_{i}(x)=0,\ i\in \left\{1,\ldots ,p\right\}\end{aligned}}$

with the domain ${\mathcal {D}}\subset \mathbb {R} ^{n}$ having non-empty interior, the *Lagrangian function* ${\mathcal {L}}:\mathbb {R} ^{n}\times \mathbb {R} ^{m}\times \mathbb {R} ^{p}\to \mathbb {R}$ is defined as

${\mathcal {L}}(x,\lambda ,\nu )=f_{0}(x)+\sum _{i=1}^{m}\lambda _{i}f_{i}(x)+\sum _{i=1}^{p}\nu _{i}h_{i}(x).$

The vectors $\lambda$ and $\nu$ are called the *dual variables* or *Lagrange multiplier vectors* associated with the problem. The *Lagrange dual function* $g:\mathbb {R} ^{m}\times \mathbb {R} ^{p}\to \mathbb {R}$ is defined as

$g(\lambda ,\nu )=\inf _{x\in {\mathcal {D}}}{\mathcal {L}}(x,\lambda ,\nu )=\inf _{x\in {\mathcal {D}}}\left\{f_{0}(x)+\sum _{i=1}^{m}\lambda _{i}f_{i}(x)+\sum _{i=1}^{p}\nu _{i}h_{i}(x)\right\}.$

The dual function g is concave, even when the initial problem is not convex, because it is a point-wise infimum of affine functions. The dual function yields lower bounds on the optimal value $p^{*}$ of the initial problem; for any $\lambda \geq 0$ and any $\nu$ we have $g(\lambda ,\nu )\leq p^{*}$ .

If a constraint qualification such as Slater's condition holds and the original problem is convex, then we have strong duality, i.e. $d^{*}=\max _{\lambda \geq 0,\nu }g(\lambda ,\nu )=\inf f_{0}=p^{*}$ .

### Convex problems

For a convex minimization problem with inequality constraints,

${\begin{aligned}&{\underset {x}{\operatorname {minimize} }}&&f(x)\\&\operatorname {subject\;to} &&g_{i}(x)\leq 0,\quad i=1,\ldots ,m\end{aligned}}$

the Lagrangian dual problem is

${\begin{aligned}&{\underset {u}{\operatorname {maximize} }}&&\inf _{x}\left(f(x)+\sum _{j=1}^{m}u_{j}g_{j}(x)\right)\\&\operatorname {subject\;to} &&u_{i}\geq 0,\quad i=1,\ldots ,m\end{aligned}}$

where the objective function is the Lagrange dual function. Provided that the functions f and $g_{1},\ldots ,g_{m}$ are continuously differentiable, the infimum occurs where the gradient is equal to zero. The problem

${\begin{aligned}&{\underset {x,u}{\operatorname {maximize} }}&&f(x)+\sum _{j=1}^{m}u_{j}g_{j}(x)\\&\operatorname {subject\;to} &&\nabla f(x)+\sum _{j=1}^{m}u_{j}\,\nabla g_{j}(x)=0\\&&&u_{i}\geq 0,\quad i=1,\ldots ,m\end{aligned}}$

is called the Wolfe dual problem. This problem may be difficult to deal with computationally, because the objective function is not concave in the joint variables $(u,x)$ . Also, the equality constraint $\nabla f(x)+\sum _{j=1}^{m}u_{j}\,\nabla g_{j}(x)$ is nonlinear in general, so the Wolfe dual problem is typically a nonconvex optimization problem. In any case, weak duality holds.

## History

According to George Dantzig, the duality theorem for linear optimization was conjectured by John von Neumann immediately after Dantzig presented the linear programming problem. Von Neumann noted that he was using information from his game theory, and conjectured that two person zero sum matrix game was equivalent to linear programming. Rigorous proofs were first published in 1948 by Albert W. Tucker and his group. (Dantzig's foreword to Nering and Tucker, 1993)

## Applications

In support vector machines (SVMs), formulating the primal problem of SVMs as the dual problem can be used to implement the Kernel trick, but the latter has higher time complexity in the historical cases.
