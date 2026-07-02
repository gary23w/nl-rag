---
title: "Linear-fractional programming"
source: https://en.wikipedia.org/wiki/Linear-fractional_programming
domain: convex-hull-trick
license: CC-BY-SA-4.0
tags: convex hull trick, dynamic programming optimization, lower envelope of lines, monotone stack
fetched: 2026-07-02
---

# Linear-fractional programming

In mathematical optimization, **linear-fractional programming** (**LFP**) is a generalization of linear programming (LP). Whereas the objective function in a linear program is a linear function, the objective function in a linear-fractional program is a ratio of two linear functions. A linear program can be regarded as a special case of a linear-fractional program in which the denominator is the constant function 1.

Formally, a linear-fractional program is defined as the problem of maximizing (or minimizing) a ratio of affine functions over a polyhedron,

${\begin{aligned}{\text{maximize}}\quad &{\frac {\mathbf {c} ^{T}\mathbf {x} +\alpha }{\mathbf {d} ^{T}\mathbf {x} +\beta }}\\{\text{subject to}}\quad &A\mathbf {x} \leq \mathbf {b} ,\end{aligned}}$

where $\mathbf {x} \in \mathbb {R} ^{n}$ represents the vector of variables to be determined, $\mathbf {c} ,\mathbf {d} \in \mathbb {R} ^{n}$ and $\mathbf {b} \in \mathbb {R} ^{m}$ are vectors of (known) coefficients, $A\in \mathbb {R} ^{m\times n}$ is a (known) matrix of coefficients and $\alpha ,\beta \in \mathbb {R}$ are constants. The constraints have to restrict the feasible region to $\{\mathbf {x} |\mathbf {d} ^{T}\mathbf {x} +\beta >0\}$ , i.e. the region on which the denominator is positive. Alternatively, the denominator of the objective function has to be strictly negative in the entire feasible region.

## Motivation by comparison to linear programming

Both linear programming and linear-fractional programming represent optimization problems using linear equations and linear inequalities, which for each problem-instance define a feasible set. Fractional linear programs have a richer set of objective functions. Informally, linear programming computes a policy delivering the best outcome, such as maximum profit or lowest cost. In contrast, a linear-fractional programming is used to achieve the highest *ratio* of outcome to cost, the ratio representing the highest efficiency. For example, in the context of LP we maximize the objective function **profit = income − cost** and might obtain maximum profit of $100 (= $1100 of income − $1000 of cost). Thus, in LP we have an efficiency of $100/$1000 = 0.1. Using LFP we might obtain an efficiency of $10/$50 = 0.2 with a profit of only $10, but only requiring $50 of investment.

## Transformation to a linear program

Any linear-fractional program can be transformed into a linear program, assuming that the feasible region is non-empty and bounded, using the **Charnes–Cooper transformation**. The main idea is to introduce a new non-negative variable t to the program which will be used to rescale the constants involved in the program ( $\alpha ,\beta ,\mathbf {b}$ ). This allows us to require that the denominator of the objective function ( $\mathbf {d} ^{T}\mathbf {x} +\beta$ ) equals 1. (To understand the transformation, it is instructive to consider the simpler special case with $\alpha =\beta =0$ .)

Formally, the linear program obtained via the Charnes–Cooper transformation uses the transformed variables $\mathbf {y} \in \mathbb {R} ^{n}$ and $t\geq 0$ :

${\begin{aligned}{\text{maximize}}\quad &\mathbf {c} ^{T}\mathbf {y} +\alpha t\\{\text{subject to}}\quad &A\mathbf {y} \leq \mathbf {b} t\\&\mathbf {d} ^{T}\mathbf {y} +\beta t=1\\&t\geq 0.\end{aligned}}$

A solution $\mathbf {x}$ to the original linear-fractional program can be translated to a solution of the transformed linear program via the equalities

$\mathbf {y} ={\frac {1}{\mathbf {d} ^{T}\mathbf {x} +\beta }}\cdot \mathbf {x} \quad {\text{and}}\quad t={\frac {1}{\mathbf {d} ^{T}\mathbf {x} +\beta }}.$

Conversely, a solution for $\mathbf {y}$ and t of the transformed linear program can be translated to a solution of the original linear-fractional program via

$\mathbf {x} ={\frac {1}{t}}\mathbf {y} .$

## Duality

Let the dual variables associated with the constraints $A\mathbf {y} -\mathbf {b} t\leq \mathbf {0}$ and $\mathbf {d} ^{T}\mathbf {y} +\beta t-1=0$ be denoted by $\mathbf {u}$ and $\lambda$ , respectively. Then the dual of the LFP above is

${\begin{aligned}{\text{minimize}}\quad &\lambda \\{\text{subject to}}\quad &A^{T}\mathbf {u} +\lambda \mathbf {d} =\mathbf {c} \\&-\mathbf {b} ^{T}\mathbf {u} +\lambda \beta \geq \alpha \\&\mathbf {u} \in \mathbb {R} _{+}^{m},\lambda \in \mathbb {R} ,\end{aligned}}$

which is an LP and which coincides with the dual of the equivalent linear program resulting from the Charnes–Cooper transformation.

## Properties and algorithms

The objective function in a linear-fractional problem is both quasiconcave and quasiconvex (hence quasilinear) with a monotone property, pseudoconvexity, which is a stronger property than quasiconvexity. A linear-fractional objective function is both pseudoconvex and pseudoconcave, hence pseudolinear. Since an LFP can be transformed to an LP, it can be solved using any LP solution method, such as the simplex algorithm (of George B. Dantzig), the criss-cross algorithm, or interior-point methods.
