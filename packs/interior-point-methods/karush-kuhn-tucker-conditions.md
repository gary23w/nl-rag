---
title: "Karush–Kuhn–Tucker conditions"
source: https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions
domain: interior-point-methods
license: CC-BY-SA-4.0
tags: interior-point method, karmarkar algorithm, barrier function, ellipsoid method
fetched: 2026-07-02
---

# Karush–Kuhn–Tucker conditions

In mathematical optimization, the **Karush–Kuhn–Tucker** (**KKT**) **conditions**, also known as the **Kuhn–Tucker conditions**, are first derivative tests (sometimes called first-order necessary conditions) for a solution in nonlinear programming to be optimal, provided that some regularity conditions are satisfied.

Allowing inequality constraints, the KKT approach to nonlinear programming generalizes the method of Lagrange multipliers, which allows only equality constraints. Similar to the Lagrange approach, the constrained maximization (minimization) problem is rewritten as a Lagrange function whose optimal point is a global maximum or minimum over the domain of the choice variables and a global minimum (maximum) over the multipliers. The Karush–Kuhn–Tucker theorem is sometimes referred to as the saddle-point theorem.

The KKT conditions were originally named after Harold W. Kuhn and Albert W. Tucker, who first published the conditions in 1951. Later scholars discovered that the necessary conditions for this problem had been stated in an unpublished master's thesis by William Karush in 1939.

## Nonlinear optimization problem

Consider the following nonlinear optimization problem in standard form:

minimize

$f(\mathbf {x} )$

subject to

$g_{i}(\mathbf {x} )\leq 0,$

$h_{j}(\mathbf {x} )=0.$

where $\mathbf {x} \in \mathbf {X}$ is the optimization variable chosen from a convex subset of $\mathbb {R} ^{n}$ , f is the objective or utility function, $g_{i}\ (i=1,\ldots ,m)$ are the inequality constraint functions and $h_{j}\ (j=1,\ldots ,\ell )$ are the equality constraint functions. The numbers of inequalities and equalities are denoted by m and $\ell$ respectively. Corresponding to the constrained optimization problem one can form the Lagrangian function

${\mathcal {L}}(\mathbf {x} ,\mathbf {\mu } ,\mathbf {\lambda } )=f(\mathbf {x} )+\mathbf {\mu } ^{\top }\mathbf {g} (\mathbf {x} )+\mathbf {\lambda } ^{\top }\mathbf {h} (\mathbf {x} )=L(\mathbf {x} ,\mathbf {\alpha } )=f(\mathbf {x} )+\mathbf {\alpha } ^{\top }{\begin{pmatrix}\mathbf {g} (\mathbf {x} )\\\mathbf {h} (\mathbf {x} )\end{pmatrix}}$

where

$\mathbf {g} \left(\mathbf {x} \right)={\begin{bmatrix}g_{1}\left(\mathbf {x} \right)\\\vdots \\g_{i}\left(\mathbf {x} \right)\\\vdots \\g_{m}\left(\mathbf {x} \right)\end{bmatrix}},\quad \mathbf {h} \left(\mathbf {x} \right)={\begin{bmatrix}h_{1}\left(\mathbf {x} \right)\\\vdots \\h_{j}\left(\mathbf {x} \right)\\\vdots \\h_{\ell }\left(\mathbf {x} \right)\end{bmatrix}},\quad \mathbf {\mu } ={\begin{bmatrix}\mu _{1}\\\vdots \\\mu _{i}\\\vdots \\\mu _{m}\\\end{bmatrix}},\quad \mathbf {\lambda } ={\begin{bmatrix}\lambda _{1}\\\vdots \\\lambda _{j}\\\vdots \\\lambda _{\ell }\end{bmatrix}}\quad {\text{and}}\quad \mathbf {\alpha } ={\begin{bmatrix}\mu \\\lambda \end{bmatrix}}.$ The **Karush–Kuhn–Tucker theorem** then states the following.

**Theorem**—(sufficiency) If $(\mathbf {x} ^{\ast },\mathbf {\alpha } ^{\ast })$ is a saddle point of $L(\mathbf {x} ,\mathbf {\alpha } )$ in $\mathbf {x} \in \mathbf {X}$ , $\mathbf {\mu } \geq \mathbf {0}$ , then $\mathbf {x} ^{\ast }$ is an optimal vector for the above optimization problem.

(necessity) Suppose that $f(\mathbf {x} )$ and $g_{i}(\mathbf {x} )$ , $i=1,\ldots ,m$ , are convex in $\mathbf {X}$ and that there exists $\mathbf {x} _{0}\in \operatorname {relint} (\mathbf {X} )$ such that $\mathbf {g} (\mathbf {x} _{0})<\mathbf {0}$ (i.e., Slater's condition holds). Then with an optimal vector $\mathbf {x} ^{\ast }$ for the above optimization problem there is associated a vector $\mathbf {\alpha } ^{\ast }={\begin{bmatrix}\mu ^{*}\\\lambda ^{*}\end{bmatrix}}$ satisfying $\mathbf {\mu } ^{*}\geq \mathbf {0}$ such that $(\mathbf {x} ^{\ast },\mathbf {\alpha } ^{\ast })$ is a saddle point of $L(\mathbf {x} ,\mathbf {\alpha } )$ .

Since the idea of this approach is to find a supporting hyperplane on the feasible set $\mathbf {\Gamma } =\left\{\mathbf {x} \in \mathbf {X} :g_{i}(\mathbf {x} )\leq 0,i=1,\ldots ,m\right\}$ , the proof of the Karush–Kuhn–Tucker theorem makes use of the hyperplane separation theorem.

The system of equations and inequalities corresponding to the KKT conditions is usually not solved directly, except in the few special cases where a closed-form solution can be derived analytically. In general, many optimization algorithms can be interpreted as methods for numerically solving the KKT system of equations and inequalities.

## Necessary conditions

Suppose that the objective function $f\colon \mathbb {R} ^{n}\rightarrow \mathbb {R}$ and the constraint functions $g_{i}\colon \mathbb {R} ^{n}\rightarrow \mathbb {R}$ and $h_{j}\colon \mathbb {R} ^{n}\rightarrow \mathbb {R}$ have subderivatives at a point $x^{*}\in \mathbb {R} ^{n}$ . If $x^{*}$ is a local optimum and the optimization problem satisfies some regularity conditions (see below), then there exist constants $\mu _{i}\ (i=1,\ldots ,m)$ and $\lambda _{j}\ (j=1,\ldots ,\ell )$ , called KKT multipliers, such that the following four groups of conditions hold:

**Stationarity**

For minimizing

$f(x)$

:

$\partial f(x^{*})+\sum _{j=1}^{\ell }\lambda _{j}\partial h_{j}(x^{*})+\sum _{i=1}^{m}\mu _{i}\partial g_{i}(x^{*})\ni \mathbf {0}$

For maximizing

$f(x)$

:

$-\partial f(x^{*})+\sum _{j=1}^{\ell }\lambda _{j}\partial h_{j}(x^{*})+\sum _{i=1}^{m}\mu _{i}\partial g_{i}(x^{*})\ni \mathbf {0}$

**Primal feasibility**

$h_{j}(x^{*})=0,{\text{ for }}j=1,\ldots ,\ell \,\!$

$g_{i}(x^{*})\leq 0,{\text{ for }}i=1,\ldots ,m$

**Dual feasibility**

$\mu _{i}\geq 0,{\text{ for }}i=1,\ldots ,m$

**Complementary slackness**

$\sum _{i=1}^{m}\mu _{i}g_{i}(x^{*})=0.$

The last condition is sometimes written in the equivalent form: $\mu _{i}g_{i}(x^{*})=0,{\text{ for }}i=1,\ldots ,m.$

In the particular case $m=0$ , i.e., when there are no inequality constraints, the KKT conditions turn into the Lagrange conditions, and the KKT multipliers are called Lagrange multipliers.

### Interpretation: KKT conditions as balancing constraint-forces in state space

The primal problem can be interpreted as moving a particle in the space of x , and subjecting it to three kinds of force fields:

- f is a potential field that the particle is minimizing. The force generated by f is $-\partial f$ .
- $g_{i}$ are one-sided constraint surfaces. The particle is allowed to move inside $g_{i}\leq 0$ , but whenever it touches $g_{i}=0$ , it is pushed inwards.
- $h_{j}$ are two-sided constraint surfaces. The particle is allowed to move only on the surface $h_{j}$ .

Primal stationarity states that the "force" of $\partial f(x^{*})$ is exactly balanced by a linear sum of forces $\partial h_{j}(x^{*})$ and $\partial g_{i}(x^{*})$ .

Dual feasibility additionally states that all the $\partial g_{i}(x^{*})$ forces must be one-sided, pointing inwards into the feasible set for x .

Complementary slackness states that if $g_{i}(x^{*})<0$ , then the force coming from $\partial g_{i}(x^{*})$ must be zero i.e., $\mu _{i}(x^{*})=0$ , since the particle is not on the boundary, the one-sided constraint force cannot activate.

### Matrix representation

The necessary conditions can be written with Jacobian matrices of the constraint functions. Let $\mathbf {g} (x):\,\!\mathbb {R} ^{n}\rightarrow \mathbb {R} ^{m}$ be defined as $\mathbf {g} (x)=\left(g_{1}(x),\ldots ,g_{m}(x)\right)^{\top }$ and let $\mathbf {h} (x):\,\!\mathbb {R} ^{n}\rightarrow \mathbb {R} ^{\ell }$ be defined as $\mathbf {h} (x)=\left(h_{1}(x),\ldots ,h_{\ell }(x)\right)^{\top }$ . Let ${\boldsymbol {\mu }}=\left(\mu _{1},\ldots ,\mu _{m}\right)^{\top }$ and ${\boldsymbol {\lambda }}=\left(\lambda _{1},\ldots ,\lambda _{\ell }\right)^{\top }$ . Then the necessary conditions can be written as:

**Stationarity**

For maximizing

$f(x)$

:

$\partial f(x^{*})-D\mathbf {g} (x^{*})^{\top }{\boldsymbol {\mu }}-D\mathbf {h} (x^{*})^{\top }{\boldsymbol {\lambda }}=\mathbf {0}$

For minimizing

$f(x)$

:

$\partial f(x^{*})+D\mathbf {g} (x^{*})^{\top }{\boldsymbol {\mu }}+D\mathbf {h} (x^{*})^{\top }{\boldsymbol {\lambda }}=\mathbf {0}$

**Primal feasibility**

$\mathbf {g} (x^{*})\leq \mathbf {0}$

$\mathbf {h} (x^{*})=\mathbf {0}$

**Dual feasibility**

${\boldsymbol {\mu }}\geq \mathbf {0}$

**Complementary slackness**

${\boldsymbol {\mu }}^{\top }\mathbf {g} (x^{*})=0.$

## Regularity conditions (or constraint qualifications)

One can ask whether a minimizer point $x^{*}$ of the original, constrained optimization problem (assuming one exists) has to satisfy the above KKT conditions. This is similar to asking under what conditions the minimizer $x^{*}$ of a function $f(x)$ in an unconstrained problem has to satisfy the condition $\nabla f(x^{*})=0$ . For the constrained case, the situation is more complicated, and one can state a variety of (increasingly complicated) "regularity" conditions under which a constrained minimizer also satisfies the KKT conditions. Some common examples for conditions that guarantee this are tabulated in the following, with the LICQ the most frequently used one:

| Constraint | Acronym | Statement |
|---|---|---|
| Linearity constraint qualification | LCQ | If $g_{i}$ and $h_{j}$ are affine functions, then no other condition is needed. |
| Linear independence constraint qualification | LICQ | The gradients of the active inequality constraints and the gradients of the equality constraints are linearly independent at $x^{*}$ . |
| Mangasarian–Fromovitz constraint qualification | MFCQ | The gradients of the equality constraints are linearly independent at $x^{*}$ and there exists a vector $d\in \mathbb {R} ^{n}$ such that $\nabla g_{i}(x^{*})^{\top }d<0$ for all active inequality constraints and $\nabla h_{j}(x^{*})^{\top }d=0$ for all equality constraints. |
| Constant rank constraint qualification | CRCQ | For each subset of the gradients of the active inequality constraints and the gradients of the equality constraints the rank at a vicinity of $x^{*}$ is constant. |
| Constant positive linear dependence constraint qualification | CPLD | For each subset of gradients of active inequality constraints and gradients of equality constraints, if the subset of vectors is linearly dependent at $x^{*}$ with non-negative scalars associated with the inequality constraints, then it remains linearly dependent in a neighborhood of $x^{*}$ . |
| Quasi-normality constraint qualification | QNCQ | If the gradients of the active inequality constraints and the gradients of the equality constraints are linearly dependent at $x^{*}$ with associated multipliers $\lambda _{j}$ for equalities and $\mu _{i}\geq 0$ for inequalities, then there is no sequence $x_{k}\to x^{*}$ such that $\lambda _{j}\neq 0\Rightarrow \lambda _{j}h_{j}(x_{k})>0$ and $\mu _{i}\neq 0\Rightarrow \mu _{i}g_{i}(x_{k})>0.$ |
| Slater's condition | SC | For a convex problem (i.e., assuming minimization, $f,g_{i}$ are convex and $h_{j}$ is affine), there exists a point x such that $h_{j}(x)=0$ and $g_{i}(x)<0.$ |

The strict implications can be shown

LICQ ⇒ MFCQ ⇒ CPLD ⇒ QNCQ

and

LICQ ⇒ CRCQ ⇒ CPLD ⇒ QNCQ

In practice weaker constraint qualifications are preferred since they apply to a broader selection of problems.

## Sufficient conditions

In some cases, the necessary conditions are also sufficient for optimality. In general, the necessary conditions are not sufficient for optimality and additional information is required, such as the Second Order Sufficient Conditions (SOSC). For smooth functions, SOSC involve the second derivatives, which explains its name.

The necessary conditions are sufficient for optimality if the objective function f of a maximization problem is a differentiable concave function, the inequality constraints $g_{j}$ are differentiable convex functions, the equality constraints $h_{i}$ are affine functions, and Slater's condition holds. Similarly, if the objective function f of a minimization problem is a differentiable convex function, the necessary conditions are also sufficient for optimality.

It was shown by Martin in 1985 that the broader class of functions in which KKT conditions guarantees global optimality are the so-called Type 1 **invex functions**.

### Second-order sufficient conditions

For smooth, non-linear optimization problems, a second order sufficient condition is given as follows.

The solution $x^{*},\lambda ^{*},\mu ^{*}$ found in the above section is a constrained local minimum if for the Lagrangian,

$L(x,\lambda ,\mu )=f(x)+\sum _{i=1}^{m}\mu _{i}g_{i}(x)+\sum _{j=1}^{\ell }\lambda _{j}h_{j}(x)$

then,

$s^{T}\nabla _{xx}^{2}L(x^{*},\lambda ^{*},\mu ^{*})s\geq 0$

where $s\neq 0$ is a vector satisfying the following,

$\left[\nabla _{x}g_{i}(x^{*}),\nabla _{x}h_{j}(x^{*})\right]^{T}s=0_{\mathbb {R} ^{2}}$

where only those active inequality constraints $g_{i}(x)$ corresponding to strict complementarity (i.e. where $\mu _{i}>0$ ) are applied. The solution is a strict constrained local minimum in the case the inequality is also strict.

If $s^{T}\nabla _{xx}^{2}L(x^{*},\lambda ^{*},\mu ^{*})s=0$ , the third order Taylor expansion of the Lagrangian should be used to verify if $x^{*}$ is a local minimum. The minimization of $f(x_{1},x_{2})=(x_{2}-x_{1}^{2})(x_{2}-3x_{1}^{2})$ is a good counter-example, see also Peano surface.

## Economics

Often in mathematical economics the KKT approach is used in theoretical models in order to obtain qualitative results. For example, consider a firm that maximizes its sales revenue subject to a minimum profit constraint. Letting Q be the quantity of output produced (to be chosen), $R(Q)$ be sales revenue with a positive first derivative and with a zero value at zero output, $C(Q)$ be production costs with a positive first derivative and with a non-negative value at zero output, and $G_{\min }$ be the positive minimal acceptable level of profit, then the problem is a meaningful one if the revenue function levels off so it eventually is less steep than the cost function. The problem expressed in the previously given minimization form is

Minimize

$-R(Q)$

subject to

$G_{\min }\leq R(Q)-C(Q)$

$Q\geq 0,$

and the KKT conditions are

${\begin{aligned}&\left({\frac {{\text{d}}R}{{\text{d}}Q}}\right)(1+\mu )-\mu \left({\frac {{\text{d}}C}{{\text{d}}Q}}\right)\leq 0,\\[5pt]&Q\geq 0,\\[5pt]&Q\left[\left({\frac {{\text{d}}R}{{\text{d}}Q}}\right)(1+\mu )-\mu \left({\frac {{\text{d}}C}{{\text{d}}Q}}\right)\right]=0,\\[5pt]&R(Q)-C(Q)-G_{\min }\geq 0,\\[5pt]&\mu \geq 0,\\[5pt]&\mu [R(Q)-C(Q)-G_{\min }]=0.\end{aligned}}$

Since $Q=0$ would violate the minimum profit constraint, we have $Q>0$ and hence the third condition implies that the first condition holds with equality. Solving that equality gives

${\frac {{\text{d}}R}{{\text{d}}Q}}={\frac {\mu }{1+\mu }}\left({\frac {{\text{d}}C}{{\text{d}}Q}}\right).$

Because it was given that ${\text{d}}R/{\text{d}}Q$ and ${\text{d}}C/{\text{d}}Q$ are strictly positive, this inequality along with the non-negativity condition on $\mu$ guarantees that $\mu$ is positive and so the revenue-maximizing firm operates at a level of output at which marginal revenue ${\text{d}}R/{\text{d}}Q$ is less than marginal cost ${\text{d}}C/{\text{d}}Q$ — a result that is of interest because it contrasts with the behavior of a profit maximizing firm, which operates at a level at which they are equal.

## Value function

If we reconsider the optimization problem as a maximization problem with constant inequality constraints:

${\text{Maximize }}\;f(x)$

${\text{subject to }}\$

$g_{i}(x)\leq a_{i},h_{j}(x)=0.$

The value function is defined as

$V(a_{1},\ldots ,a_{n})=\sup \limits _{x}f(x)$

${\text{subject to }}\$

$g_{i}(x)\leq a_{i},h_{j}(x)=0$

$j\in \{1,\ldots ,\ell \},i\in \{1,\ldots ,m\},$

so the domain of V is $\{a\in \mathbb {R} ^{m}\mid {\text{for some }}x\in X,g_{i}(x)\leq a_{i},i\in \{1,\ldots ,m\}\}.$

Given this definition, each coefficient $\mu _{i}$ is the rate at which the value function increases as $a_{i}$ increases. Thus if each $a_{i}$ is interpreted as a resource constraint, the coefficients tell you how much increasing a resource will increase the optimum value of our function f . This interpretation is especially important in economics and is used, for instance, in utility maximization problems.

## Generalizations

With an extra multiplier $\mu _{0}\geq 0$ , which may be zero (as long as $(\mu _{0},\mu ,\lambda )\neq 0$ ), in front of $\nabla f(x^{*})$ the KKT stationarity conditions turn into

${\begin{aligned}&\mu _{0}\,\nabla f(x^{*})+\sum _{i=1}^{m}\mu _{i}\,\nabla g_{i}(x^{*})+\sum _{j=1}^{\ell }\lambda _{j}\,\nabla h_{j}(x^{*})=0,\\[4pt]&\mu _{j}g_{i}(x^{*})=0,\quad i=1,\dots ,m,\end{aligned}}$

which are called the Fritz John conditions. This optimality conditions holds without constraint qualifications and it is equivalent to the optimality condition *KKT or (not-MFCQ)*.

The KKT conditions belong to a wider class of the first-order necessary conditions (FONC), which allow for non-smooth functions using subderivatives.
