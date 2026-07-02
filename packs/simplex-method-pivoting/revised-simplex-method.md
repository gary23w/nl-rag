---
title: "Revised simplex method"
source: https://en.wikipedia.org/wiki/Revised_simplex_method
domain: simplex-method-pivoting
license: CC-BY-SA-4.0
tags: simplex method, pivot rule, bland rule, revised simplex
fetched: 2026-07-02
---

# Revised simplex method

In mathematical optimization, the **revised simplex method** is a variant of George Dantzig's simplex method for linear programming.

The revised simplex method is mathematically equivalent to the standard simplex method but differs in implementation. Instead of maintaining a tableau which explicitly represents the constraints adjusted to a set of basic variables, it maintains a representation of a basis of the matrix representing the constraints. The matrix-oriented approach allows for greater computational efficiency by enabling sparse matrix operations.

## Problem formulation

For the rest of the discussion, it is assumed that a linear programming problem has been converted into the following standard form:

${\begin{array}{rl}{\text{minimize}}&{\boldsymbol {c}}^{\mathrm {T} }{\boldsymbol {x}}\\{\text{subject to}}&{\boldsymbol {Ax}}={\boldsymbol {b}},{\boldsymbol {x}}\geq {\boldsymbol {0}}\end{array}}$

where ***A*** ∈ ℝ*m*×*n*. Without loss of generality, it is assumed that the constraint matrix ***A*** has full row rank and that the problem is feasible, i.e., there is at least one ***x*** ≥ **0** such that ***Ax*** = ***b***. If ***A*** is rank-deficient, either there are redundant constraints, or the problem is infeasible. Both situations can be handled by a presolve step.

## Algorithmic description

### Optimality conditions

For linear programming, the Karush–Kuhn–Tucker conditions are both necessary and sufficient for optimality. The KKT conditions of a linear programming problem in the standard form is

${\begin{aligned}{\boldsymbol {Ax}}&={\boldsymbol {b}},\\{\boldsymbol {A}}^{\mathrm {T} }{\boldsymbol {\lambda }}+{\boldsymbol {s}}&={\boldsymbol {c}},\\{\boldsymbol {x}}&\geq {\boldsymbol {0}},\\{\boldsymbol {s}}&\geq {\boldsymbol {0}},\\{\boldsymbol {s}}^{\mathrm {T} }{\boldsymbol {x}}&=0\end{aligned}}$

where ***λ*** and ***s*** are the Lagrange multipliers associated with the constraints ***Ax*** = ***b*** and ***x*** ≥ **0**, respectively. The last condition, which is equivalent to *sixi* = 0 for all 1 < *i* < *n*, is called the *complementary slackness condition*.

By what is sometimes known as the *fundamental theorem of linear programming*, a vertex ***x*** of the feasible polytope can be identified by being a basis ***B*** of ***A*** chosen from the latter's columns. Since ***A*** has full rank, ***B*** is nonsingular. Without loss of generality, assume that ***A*** = [***B*** ***N***]. Then ***x*** is given by

${\boldsymbol {x}}={\begin{bmatrix}{\boldsymbol {x_{B}}}\\{\boldsymbol {x_{N}}}\end{bmatrix}}={\begin{bmatrix}{\boldsymbol {B}}^{-1}{\boldsymbol {b}}\\{\boldsymbol {0}}\end{bmatrix}}$

where ***xB*** ≥ **0**. Partition ***c*** and ***s*** accordingly into

${\begin{aligned}{\boldsymbol {c}}&={\begin{bmatrix}{\boldsymbol {c_{B}}}\\{\boldsymbol {c_{N}}}\end{bmatrix}},\\{\boldsymbol {s}}&={\begin{bmatrix}{\boldsymbol {s_{B}}}\\{\boldsymbol {s_{N}}}\end{bmatrix}}.\end{aligned}}$

To satisfy the complementary slackness condition, let ***sB*** = **0**. It follows that

${\begin{aligned}{\boldsymbol {B}}^{\mathrm {T} }{\boldsymbol {\lambda }}&={\boldsymbol {c_{B}}},\\{\boldsymbol {N}}^{\mathrm {T} }{\boldsymbol {\lambda }}+{\boldsymbol {s_{N}}}&={\boldsymbol {c_{N}}},\end{aligned}}$

which implies that

${\begin{aligned}{\boldsymbol {\lambda }}&=({\boldsymbol {B}}^{\mathrm {T} })^{-1}{\boldsymbol {c_{B}}},\\{\boldsymbol {s_{N}}}&={\boldsymbol {c_{N}}}-{\boldsymbol {N}}^{\mathrm {T} }{\boldsymbol {\lambda }}.\end{aligned}}$

If ***sN*** ≥ **0** at this point, the KKT conditions are satisfied, and thus ***x*** is optimal.

### Pivot operation

If the KKT conditions are violated, a *pivot operation* consisting of introducing a column of ***N*** into the basis at the expense of an existing column in ***B*** is performed. In the absence of degeneracy, a pivot operation always results in a strict decrease in ***c***T***x***. Therefore, if the problem is bounded, the revised simplex method must terminate at an optimal vertex after repeated pivot operations because there are only a finite number of vertices.

Select an index *m* < *q* ≤ *n* such that *sq* < 0 as the *entering index*. The corresponding column of ***A***, ***A**q*, will be moved into the basis, and *xq* will be allowed to increase from zero. It can be shown that

${\frac {\partial ({\boldsymbol {c}}^{\mathrm {T} }{\boldsymbol {x}})}{\partial x_{q}}}=s_{q},$

i.e., every unit increase in *xq* results in a decrease by −*sq* in ***c***T***x***. Since

${\boldsymbol {Bx_{B}}}+{\boldsymbol {A}}_{q}x_{q}={\boldsymbol {b}},$

***xB*** must be correspondingly decreased by Δ***xB*** = ***B***−1***A**qxq* subject to ***xB*** − Δ***xB*** ≥ **0**. Let ***d*** = ***B***−1***A**q*. If ***d*** ≤ **0**, no matter how much *xq* is increased, ***xB*** − Δ***xB*** will stay nonnegative. Hence, ***c***T***x*** can be arbitrarily decreased, and thus the problem is unbounded. Otherwise, select an index *p* = argmin1≤*i*≤*m* {*xi*/*di* | *di* > 0} as the *leaving index*. This choice effectively increases *xq* from zero until *xp* is reduced to zero while maintaining feasibility. The pivot operation concludes with replacing ***A**p* with ***A**q* in the basis.

## Numerical example

Consider a linear program where

${\begin{aligned}{\boldsymbol {c}}&={\begin{bmatrix}-2&-3&-4&0&0\end{bmatrix}}^{\mathrm {T} },\\{\boldsymbol {A}}&={\begin{bmatrix}3&2&1&1&0\\2&5&3&0&1\end{bmatrix}},\\{\boldsymbol {b}}&={\begin{bmatrix}10\\15\end{bmatrix}}.\end{aligned}}$

Let

${\begin{aligned}{\boldsymbol {B}}&={\begin{bmatrix}{\boldsymbol {A}}_{4}&{\boldsymbol {A}}_{5}\end{bmatrix}},\\{\boldsymbol {N}}&={\begin{bmatrix}{\boldsymbol {A}}_{1}&{\boldsymbol {A}}_{2}&{\boldsymbol {A}}_{3}\end{bmatrix}}\end{aligned}}$

initially, which corresponds to a feasible vertex ***x*** = [0 0 0 10 15]T. At this moment,

${\begin{aligned}{\boldsymbol {\lambda }}&={\begin{bmatrix}0&0\end{bmatrix}}^{\mathrm {T} },\\{\boldsymbol {s_{N}}}&={\begin{bmatrix}-2&-3&-4\end{bmatrix}}^{\mathrm {T} }.\end{aligned}}$

Choose *q* = 3 as the entering index. Then ***d*** = [1 3]T, which means a unit increase in *x*3 results in *x*4 and *x*5 being decreased by 1 and 3, respectively. Therefore, *x*3 is increased to 5, at which point *x*5 is reduced to zero, and *p* = 5 becomes the leaving index.

After the pivot operation,

${\begin{aligned}{\boldsymbol {B}}&={\begin{bmatrix}{\boldsymbol {A}}_{3}&{\boldsymbol {A}}_{4}\end{bmatrix}},\\{\boldsymbol {N}}&={\begin{bmatrix}{\boldsymbol {A}}_{1}&{\boldsymbol {A}}_{2}&{\boldsymbol {A}}_{5}\end{bmatrix}}.\end{aligned}}$

Correspondingly,

${\begin{aligned}{\boldsymbol {x}}&={\begin{bmatrix}0&0&5&5&0\end{bmatrix}}^{\mathrm {T} },\\{\boldsymbol {\lambda }}&={\begin{bmatrix}0&-4/3\end{bmatrix}}^{\mathrm {T} },\\{\boldsymbol {s_{N}}}&={\begin{bmatrix}2/3&11/3&4/3\end{bmatrix}}^{\mathrm {T} }.\end{aligned}}$

A positive ***sN*** indicates that ***x*** is now optimal.

## Practical issues

### Degeneracy

Because the revised simplex method is mathematically equivalent to the simplex method, it also suffers from degeneracy, where a pivot operation does not result in a decrease in ***c***T***x***, and a chain of pivot operations causes the basis to cycle. A perturbation or lexicographic strategy can be used to prevent cycling and guarantee termination.

### Basis representation

Two types of linear systems involving ***B*** are present in the revised simplex method:

${\begin{aligned}{\boldsymbol {Bz}}&={\boldsymbol {y}},\\{\boldsymbol {B}}^{\mathrm {T} }{\boldsymbol {z}}&={\boldsymbol {y}}.\end{aligned}}$

Instead of refactorizing ***B***, usually an LU factorization is directly updated after each pivot operation, for which purpose there exist several strategies such as the Forrest−Tomlin and Bartels−Golub methods. However, the amount of data representing the updates as well as numerical errors builds up over time and makes periodic refactorization necessary.

## Notes and references
