---
title: "Linear matrix inequality"
source: https://en.wikipedia.org/wiki/Linear_matrix_inequality
domain: semidefinite-programming
license: CC-BY-SA-4.0
tags: semidefinite programming, conic optimization, linear matrix inequality, sum-of-squares optimization
fetched: 2026-07-02
---

# Linear matrix inequality

In convex optimization, a **linear matrix inequality** (**LMI**) is an expression of the form

$\operatorname {LMI} (y):=A_{0}+y_{1}A_{1}+y_{2}A_{2}+\cdots +y_{m}A_{m}\succeq 0\,$

where

- $y=[y_{i}\,,~i\!=\!1,\dots ,m]$ is a real vector,
- $A_{0},A_{1},A_{2},\dots ,A_{m}$ are $n\times n$ symmetric matrices $\mathbb {S} ^{n}$ ,
- $B\succeq 0$ is a generalized inequality meaning B is a positive semidefinite matrix belonging to the positive semidefinite cone $\mathbb {S} _{+}$ in the subspace of symmetric matrices $\mathbb {S}$ .

This linear matrix inequality specifies a convex constraint on  y .

## Applications

There are efficient numerical methods to determine whether an LMI is feasible (*e.g.*, whether there exists a vector *y* such that LMI(*y*) ≥ 0), or to solve a convex optimization problem with LMI constraints. Many optimization problems in control theory, system identification and signal processing can be formulated using LMIs. Also LMIs find application in Polynomial Sum-Of-Squares. The prototypical primal and dual semidefinite program is a minimization of a real linear function respectively subject to the primal and dual convex cones governing this LMI.

## Solving LMIs

A major breakthrough in convex optimization was the introduction of interior-point methods. These methods were developed in a series of papers and became of true interest in the context of LMI problems in the work of Yurii Nesterov and Arkadi Nemirovski.
