---
title: "Contraction mapping"
source: https://en.wikipedia.org/wiki/Contraction_mapping
domain: fixed-point-iteration
license: CC-BY-SA-4.0
tags: fixed-point iteration, banach fixed-point theorem, contraction mapping, anderson acceleration
fetched: 2026-07-02
---

# Contraction mapping

In mathematics, a **contraction mapping**, or **contraction** or **contractor**, on a metric space (*M*, *d*) is a function *f* from *M* to itself, with the property that there is some real number $0\leq k<1$ such that for all *x* and *y* in *M*,

$d(f(x),f(y))\leq k\,d(x,y).$ The smallest such value of *k* is called the **Lipschitz constant** of *f*. Contractive maps are sometimes called **Lipschitzian maps**. If the above condition is instead satisfied for *k* ≤ 1, then the mapping is said to be a non-expansive map.

More generally, the idea of a contractive mapping can be defined for maps between metric spaces. Thus, if (*M*, *d*) and (*N*, *d'*) are two metric spaces, then $f:M\rightarrow N$ is a contractive mapping if there is a constant $0\leq k<1$ such that $d'(f(x),f(y))\leq k\,d(x,y)$ for all *x* and *y* in *M*.

Every contraction mapping is Lipschitz continuous and hence uniformly continuous (for a Lipschitz continuous function, the constant *k* is no longer necessarily less than 1).

A contraction mapping has at most one fixed point. Moreover, the Banach fixed-point theorem states that every contraction mapping on a non-empty complete metric space has a unique fixed point, and that for any *x* in *M* the iterated function sequence *x*, *f* (*x*), *f* (*f* (*x*)), *f* (*f* (*f* (*x*))), ... converges to the fixed point. This concept is very useful for iterated function systems where contraction mappings are often used. Banach's fixed-point theorem is also applied in proving the existence of solutions of ordinary differential equations, and is used in one proof of the inverse function theorem.

Contraction mappings play an important role in dynamic programming problems.

## Firmly non-expansive mapping

A non-expansive mapping with $k=1$ can be generalized to a **firmly non-expansive mapping** in a Hilbert space ${\mathcal {H}}$ if the following holds for all *x* and *y* in ${\mathcal {H}}$ : $\|f(x)-f(y)\|^{2}\leq \,\langle x-y,f(x)-f(y)\rangle ,$ where $d(x,y)=\|x-y\|.$ This is a special case of $\alpha$ averaged nonexpansive operators with $\alpha =1/2$ . A firmly non-expansive mapping is always non-expansive, via the Cauchy–Schwarz inequality.

The class of firmly non-expansive maps is closed under convex combinations, but not compositions. This class includes proximal mappings of proper, convex, lower-semicontinuous functions, hence it also includes orthogonal projections onto non-empty closed convex sets. The class of firmly nonexpansive operators is equal to the set of resolvents of maximally monotone operators. Surprisingly, while iterating non-expansive maps has no guarantee to find a fixed point (e.g. multiplication by -1), firm non-expansiveness is sufficient to guarantee global convergence to a fixed point, provided a fixed point exists. More precisely, if $\operatorname {Fix} f:=\{x\in {\mathcal {H}}\ |\ f(x)=x\}\neq \varnothing ,$ then for any initial point $x_{0}\in {\mathcal {H}}$ , iterating $x_{n+1}=f(x_{n}),\quad \forall n\in \mathbb {N}$ yields convergence to a fixed point $x_{n}\to z\in \operatorname {Fix} f$ . This convergence might be weak in an infinite-dimensional setting.

## Subcontraction map

A **subcontraction map** or **subcontractor** is a map *f* on a metric space (*M*, *d*) such that $d(f(x),f(y))\leq d(x,y);$ $d(f(f(x)),f(x))<d(f(x),x)\quad {\text{unless}}\quad x=f(x).$ If the image of a subcontractor *f* is compact, then *f* has a fixed point.

## Locally convex spaces

In a locally convex space (*E*, *P*) with topology given by a set *P* of seminorms, one can define for any *p* ∈ *P* a *p*-contraction as a map *f* such that there is some *k**p* < 1 such that *p*(*f*(*x*) − *f*(*y*)) ≤ *kp p*(*x* − *y*). If *f* is a *p*-contraction for all *p* ∈ *P* and (*E*, *P*) is sequentially complete, then *f* has a fixed point, given as limit of any sequence *x**n*+1 = *f*(*x**n*), and if (*E*, *P*) is Hausdorff, then the fixed point is unique.
