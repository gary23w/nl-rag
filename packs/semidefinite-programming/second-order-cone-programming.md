---
title: "Second-order cone programming"
source: https://en.wikipedia.org/wiki/Second-order_cone_programming
domain: semidefinite-programming
license: CC-BY-SA-4.0
tags: semidefinite programming, conic optimization, linear matrix inequality, sum-of-squares optimization
fetched: 2026-07-02
---

# Second-order cone programming

A **second-order cone program** (**SOCP**) is a convex optimization problem of the form

minimize

$\ f^{T}x\$

subject to

$\lVert A_{i}x+b_{i}\rVert _{2}\leq c_{i}^{T}x+d_{i},\quad i=1,\dots ,m$

$Fx=g\$

where the problem parameters are $f\in \mathbb {R} ^{n},\ A_{i}\in \mathbb {R} ^{{n_{i}}\times n},\ b_{i}\in \mathbb {R} ^{n_{i}},\ c_{i}\in \mathbb {R} ^{n},\ d_{i}\in \mathbb {R} ,\ F\in \mathbb {R} ^{p\times n}$ , and $g\in \mathbb {R} ^{p}$ . $x\in \mathbb {R} ^{n}$ is the optimization variable. $\lVert x\rVert _{2}$ is the Euclidean norm and $^{T}$ indicates transpose.

The name "second-order cone programming" comes from the nature of the individual constraints, which are each of the form:

$\lVert Ax+b\rVert _{2}\leq c^{T}x+d$

These each define a subspace that is bounded by an inequality based on a second-order polynomial function defined on the optimization variable x ; this can be shown to define a convex cone, hence the name "**second-order cone**". By the definition of convex cones, their intersection can also be shown to be a convex cone, although not necessarily one that can be defined by a single second-order inequality. See below for a more detailed treatment.

SOCPs can be solved by interior point methods and in general, can be solved more efficiently than semidefinite programming (SDP) problems. Some engineering applications of SOCP include filter design, antenna array weight design, truss design, and grasping force optimization in robotics. Applications in quantitative finance include portfolio optimization; some market impact constraints, because they are not linear, cannot be solved by quadratic programming but can be formulated as SOCP problems.

## Second-order cones

The standard or unit second-order cone of dimension $n+1$ is defined as

${\mathcal {C}}_{n+1}=\left\{{\begin{bmatrix}x\\t\end{bmatrix}}{\Bigg |}x\in \mathbb {R} ^{n},t\in \mathbb {R} ,\|x\|_{2}\leq t\right\}$

.

The second-order cone is also known by the names **quadratic cone**, **ice-cream cone**, or **Lorentz cone**. For example, the standard second-order cone in $\mathbb {R} ^{3}$ is

$\left\{(x,y,z){\Big |}{\sqrt {x^{2}+y^{2}}}\leq z\right\}$

.

The set of points satisfying a second-order cone constraint is the inverse image of the unit second-order cone under an affine mapping:

$\lVert A_{i}x+b_{i}\rVert _{2}\leq c_{i}^{T}x+d_{i}\Leftrightarrow {\begin{bmatrix}A_{i}\\c_{i}^{T}\end{bmatrix}}x+{\begin{bmatrix}b_{i}\\d_{i}\end{bmatrix}}\in {\mathcal {C}}_{n_{i}+1}$

and hence is convex.

The second-order cone can be embedded in the cone of the positive semidefinite matrices since

$||x||\leq t\Leftrightarrow {\begin{bmatrix}tI&x\\x^{T}&t\end{bmatrix}}\succcurlyeq 0,$

i.e., a second-order cone constraint is equivalent to a linear matrix inequality. The nomenclature here can be confusing; here $M\succcurlyeq 0$ means M is a semidefinite matrix: that is to say

$x^{T}Mx\geq 0{\text{ for all }}x\in \mathbb {R} ^{n}$

which is not a linear inequality in the conventional sense.

Similarly, we also have,

$\lVert A_{i}x+b_{i}\rVert _{2}\leq c_{i}^{T}x+d_{i}\Leftrightarrow {\begin{bmatrix}(c_{i}^{T}x+d_{i})I&A_{i}x+b_{i}\\(A_{i}x+b_{i})^{T}&c_{i}^{T}x+d_{i}\end{bmatrix}}\succcurlyeq 0$

.

## Relation with other optimization problems

When $A_{i}=0$ for $i=1,\dots ,m$ , the SOCP reduces to a linear program. When $c_{i}=0$ for $i=1,\dots ,m$ , the SOCP is equivalent to a convex quadratically constrained linear program.

Convex quadratically constrained quadratic programs can also be formulated as SOCPs by reformulating the objective function as a constraint. Semidefinite programming subsumes SOCPs as the SOCP constraints can be written as linear matrix inequalities (LMI) and can be reformulated as an instance of semidefinite program. The converse, however, is not valid: there are positive semidefinite cones that do not admit any second-order cone representation.

Any closed convex semialgebraic set in the plane can be written as a feasible region of a SOCP. However, it is known that there exist convex semialgebraic sets of higher dimension that are not representable by SDPs; that is, there exist convex semialgebraic sets that can not be written as the feasible region of a SDP (nor, *a fortiori*, as the feasible region of a SOCP).

## Examples

### Quadratic constraint

Consider a convex quadratic constraint of the form

$x^{T}Ax+b^{T}x+c\leq 0.$

This is equivalent to the SOCP constraint

$\lVert A^{1/2}x+{\frac {1}{2}}A^{-1/2}b\rVert \leq \left({\frac {1}{4}}b^{T}A^{-1}b-c\right)^{\frac {1}{2}}$

### Stochastic linear programming

Consider a stochastic linear program in inequality form

minimize

$\ c^{T}x\$

subject to

$\mathbb {P} (a_{i}^{T}x\leq b_{i})\geq p,\quad i=1,\dots ,m$

where the parameters $a_{i}\$ are independent Gaussian random vectors with mean ${\bar {a}}_{i}$ and covariance $\Sigma _{i}\$ and $p\geq 0.5$ . This problem can be expressed as the SOCP

minimize

$\ c^{T}x\$

subject to

${\bar {a}}_{i}^{T}x+\Phi ^{-1}(p)\lVert \Sigma _{i}^{1/2}x\rVert _{2}\leq b_{i},\quad i=1,\dots ,m$

where $\Phi ^{-1}(\cdot )\$ is the inverse normal cumulative distribution function.

### Stochastic second-order cone programming

We refer to second-order cone programs as deterministic second-order cone programs since data defining them are deterministic. Stochastic second-order cone programs are a class of optimization problems that are defined to handle uncertainty in data defining deterministic second-order cone programs.

### Other examples

Other modeling examples are available at the MOSEK modeling cookbook.

## Solvers and scripting (programming) languages

| Name | License | Brief info |
|---|---|---|
| ALGLIB | free/commercial | A dual-licensed C++/C#/Java/Python numerical analysis library with parallel SOCP solver. |
| AMPL | commercial | An algebraic modeling language with SOCP support |
| Artelys Knitro | commercial |   |
| CPLEX | commercial |   |
| FICO Xpress | commercial |   |
| Gurobi Optimizer | commercial |   |
| MATLAB | commercial | The `coneprog` function solves SOCP problems using an interior-point algorithm |
| MOSEK | commercial | parallel interior-point algorithm |
| NAG Numerical Library | commercial | General purpose numerical library with SOCP solver |
