---
title: "Conic optimization"
source: https://en.wikipedia.org/wiki/Conic_optimization
domain: semidefinite-programming
license: CC-BY-SA-4.0
tags: semidefinite programming, conic optimization, linear matrix inequality, sum-of-squares optimization
fetched: 2026-07-02
---

# Conic optimization

**Conic optimization** is a subfield of convex optimization that studies problems consisting of minimizing a convex function over the intersection of an affine subspace and a convex cone.

The class of conic optimization problems includes some of the most well known classes of convex optimization problems, namely linear and semidefinite programming.

## Definition

Given a real vector space *X*, a convex, real-valued function

$f:C\to \mathbb {R}$

defined on a convex cone $C\subset X$ , and an affine subspace ${\mathcal {H}}$ defined by a set of affine constraints $h_{i}(x)=0\$ , a conic optimization problem is to find the point x in $C\cap {\mathcal {H}}$ for which the number $f(x)$ is smallest.

Examples of C include the positive orthant $\mathbb {R} _{+}^{n}=\left\{x\in \mathbb {R} ^{n}:\,x\geq \mathbf {0} \right\}$ , positive semidefinite matrices $\mathbb {S} _{+}^{n}$ , and the **second-order cone** $\left\{(x,t)\in \mathbb {R} ^{n}\times \mathbb {R} :\lVert x\rVert \leq t\right\}$ . Often $f\$ is a linear function, in which case the conic optimization problem reduces to a linear program, a semidefinite program, and a second order cone program, respectively.

## Duality

Certain special cases of conic optimization problems have notable closed-form expressions of their dual problems.

### Conic LP

The dual of the conic linear program

minimize

$c^{T}x\$

subject to

$Ax=b,x\in C\$

is

maximize

$b^{T}y\$

subject to

$A^{T}y+s=c,s\in C^{*}\$

where $C^{*}$ denotes the dual cone of $C\$ .

Whilst weak duality holds in conic linear programming, strong duality does not necessarily hold.

### Semidefinite Program

The dual of a semidefinite program in inequality form

minimize

$c^{T}x\$

subject to

$x_{1}F_{1}+\cdots +x_{n}F_{n}+G\leq 0$

is given by

maximize

$\mathrm {tr} \ (GZ)\$

subject to

$\mathrm {tr} \ (F_{i}Z)+c_{i}=0,\quad i=1,\dots ,n$

$Z\geq 0$
