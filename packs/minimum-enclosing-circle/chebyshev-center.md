---
title: "Chebyshev center"
source: https://en.wikipedia.org/wiki/Chebyshev_center
domain: minimum-enclosing-circle
license: CC-BY-SA-4.0
tags: smallest enclosing circle, welzl algorithm, bounding sphere, minimum enclosing ball
fetched: 2026-07-02
---

# Chebyshev center

In geometry, the **Chebyshev center** of a bounded set Q having non-empty interior is the center of the minimal-radius ball enclosing the entire set Q , or alternatively (and non-equivalently) the center of largest inscribed ball of Q .

In the field of parameter estimation, the Chebyshev center approach tries to find an estimator ${\hat {x}}$ for x given the feasibility set Q , such that ${\hat {x}}$ minimizes the worst possible estimation error for x (e.g. best worst case).

## Mathematical representation

There exist several alternative representations for the Chebyshev center. Consider the set Q and denote its Chebyshev center by ${\hat {x}}$ . ${\hat {x}}$ can be computed by solving:

$\min _{{\hat {x}},r}\left\{r:\left\|{\hat {x}}-x\right\|^{2}\leq r,\forall x\in Q\right\}$

with respect to the Euclidean norm $\|\cdot \|$ , or alternatively by solving:

$\operatorname {\underset {\mathit {\hat {x}}}{argmin}} \max _{x\in Q}\left\|x-{\hat {x}}\right\|^{2}.$

Despite these properties, finding the Chebyshev center may be a hard numerical optimization problem. For example, in the second representation above, the inner maximization is non-convex if the set *Q* is not convex.

## Properties

In inner product spaces and two-dimensional spaces, if Q is closed, bounded and convex, then the Chebyshev center is in Q . In other words, the search for the Chebyshev center can be conducted inside Q without loss of generality.

In other spaces, the Chebyshev center may not be in Q , even if Q is convex. For instance, if Q is the tetrahedron formed by the convex hull of the points (1,1,1), (-1,1,1), (1,-1,1) and (1,1,-1), then computing the Chebyshev center using the $\ell _{\infty }$ norm yields

$0=\operatorname {\underset {\mathit {\hat {x}}}{argmin}} \max _{x\in Q}\left\|x-{\hat {x}}\right\|_{\infty }^{2}.$

## Relaxed Chebyshev center

Consider the case in which the set Q can be represented as the intersection of k ellipsoids.

$\min _{\hat {x}}\max _{x}\left\{\left\|{\hat {x}}-x\right\|^{2}:f_{i}(x)\leq 0,0\leq i\leq k\right\}$

with

$f_{i}(x)=x^{T}Q_{i}x+2g_{i}^{T}x+d_{i}\leq 0,0\leq i\leq k.\,$

By introducing an additional matrix variable $\Delta =xx^{T}$ , we can write the inner maximization problem of the Chebyshev center as:

$\min _{\hat {x}}\max _{(\Delta ,x)\in G}\left\{\left\|{\hat {x}}\right\|^{2}-2{\hat {x}}^{T}x+\operatorname {Tr} (\Delta )\right\}$

where $\operatorname {Tr} (\cdot )$ is the trace operator and

$G=\left\{(\Delta ,x):{\rm {f}}_{i}(\Delta ,x)\leq 0,0\leq i\leq k,\Delta =xx^{T}\right\}$

$f_{i}(\Delta ,x)=\operatorname {Tr} (Q_{i}\Delta )+2g_{i}^{T}x+d_{i}.$

Relaxing our demand on $\Delta$ by demanding $\Delta \geq xx^{T}$ , i.e. $\Delta -xx^{T}\in S_{+}$ where $S_{+}$ is the set of positive semi-definite matrices, and changing the order of the min max to max min (see the references for more details), the optimization problem can be formulated as:

$RCC=\max _{(\Delta ,x)\in {T}}\left\{-\left\|x\right\|^{2}+\operatorname {Tr} (\Delta )\right\}$

with

${T}=\left\{(\Delta ,x):f_{i}(\Delta ,x)\leq 0,0\leq i\leq k,\Delta \geq xx^{T}\right\}.$

This last **convex** optimization problem is known as the **relaxed Chebyshev center** (RCC). The RCC has the following important properties:

- The RCC is an upper bound for the exact Chebyshev center.
- The RCC is unique.
- The RCC is feasible.

## Constrained least squares

It can be shown that the well-known constrained least squares (CLS) problem is a relaxed version of the Chebyshev center.

The original CLS problem can be formulated as:

${\hat {x}}_{CLS}=\operatorname {*} {\arg \min }_{x\in C}\left\|y-Ax\right\|^{2}$

with

${C}=\left\{x:f_{i}(x)=x^{T}Q_{i}x+2g_{i}^{T}x+d_{i}\leq 0,1\leq i\leq k\right\}$

$Q_{i}\geq 0,g_{i}\in R^{m},d_{i}\in R.$

It can be shown that this problem is equivalent to the following optimization problem:

$\max _{(\Delta ,{x})\in {V}}\left\{{-\left\|{x}\right\|^{2}+\operatorname {Tr} (\Delta )}\right\}$

with

$V=\left\{{\begin{array}{c}(\Delta ,x):x\in C{\rm {}}\\\operatorname {Tr} (A^{T}A\Delta )-2y^{T}A^{T}x+\left\|y\right\|^{2}-\rho \leq 0,{\rm {{}\Delta \geq xx^{T}}}\\\end{array}}\right\}.$

One can see that this problem is a relaxation of the Chebyshev center (though different than the RCC described above).

## RCC vs. CLS

A solution set $(x,\Delta )$ for the RCC is also a solution for the CLS, and thus $T\in V$ . This means that the CLS estimate is the solution of a looser relaxation than that of the RCC. Hence the **CLS is an upper bound for the RCC**, which is an upper bound for the real Chebyshev center.

## Modeling constraints

Since both the RCC and CLS are based upon relaxation of the real feasibility set Q , the form in which Q is defined affects its relaxed versions. This of course affects the quality of the RCC and CLS estimators. As a simple example consider the linear box constraints:

$l\leq a^{T}x\leq u$

which can alternatively be written as

$(a^{T}x-l)(a^{T}x-u)\leq 0.$

It turns out that the first representation results with an upper bound estimator for the second one, hence using it may dramatically decrease the quality of the calculated estimator.

This simple example shows us that great care should be given to the formulation of constraints when relaxation of the feasibility region is used.

## Linear programming problem

This problem can be formulated as a linear programming problem, provided that the region Q is an intersection of finitely many hyperplanes. Given a polytope, Q, defined as follows then it can be solved via the following linear program.

$Q=\{x\in R^{n}:Ax\leq b\}$

${\begin{aligned}&\max _{r,{\hat {x}}}&&r\\&{\text{s.t.}}&&a_{i}{\hat {x}}+\|a_{i}\|r\leq b_{i}\\&{\text{and}}&&r\geq 0\end{aligned}}$
