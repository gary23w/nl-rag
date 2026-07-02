---
title: "Affine scaling"
source: https://en.wikipedia.org/wiki/Affine_scaling
domain: karmarkar-interior-point
license: CC-BY-SA-4.0
tags: karmarkar algorithm, interior point method, projective scaling, polynomial linear programming
fetched: 2026-07-02
---

# Affine scaling

In mathematical optimization, **affine scaling** is an algorithm for solving linear programming problems. Specifically, it is an interior point method, discovered by Soviet mathematician I. I. Dikin in 1967 and reinvented in the U.S. in the mid-1980s.

## History

Affine scaling has a history of multiple discovery. It was first published by I. I. Dikin at Energy Systems Institute of Russian Academy of Sciences (Siberian Energy Institute, USSR Academy of Sc. at that time) in the 1967 *Doklady Akademii Nauk SSSR*, followed by a proof of its convergence in 1974. Dikin's work went largely unnoticed until the 1984 discovery of Karmarkar's algorithm, the first practical polynomial time algorithm for linear programming. The importance and complexity of Karmarkar's method prompted mathematicians to search for a simpler version.

Several groups then independently came up with a variant of Karmarkar's algorithm. E. R. Barnes at IBM, a team led by R. J. Vanderbei at AT&T, and several others replaced the projective transformations that Karmarkar used by affine ones. After a few years, it was realized that the "new" affine scaling algorithms were in fact reinventions of the decades-old results of Dikin. Of the re-discoverers, only Barnes and Vanderbei *et al.* managed to produce an analysis of affine scaling's convergence properties. Karmarkar, who had also came with affine scaling in this timeframe, mistakenly believed that it converged as quickly as his own algorithm.

## Algorithm

Affine scaling works in two phases, the first of which finds a feasible point from which to start optimizing, while the second does the actual optimization while staying strictly inside the feasible region.

Both phases solve linear programs in equality form, viz.

minimize

c

⋅

x

subject to

Ax

=

b

,

x

≥ 0

.

These problems are solved using an iterative method, which conceptually proceeds by plotting a trajectory of points strictly inside the feasible region of a problem, computing projected gradient descent steps in a re-scaled version of the problem, then scaling the step back to the original problem. The scaling ensures that the algorithm can continue to do large steps even when the point under consideration is close to the feasible region's boundary.

Formally, the iterative method at the heart of affine scaling takes as inputs A, b, c, an initial guess *x*0 > 0 that is strictly feasible (i.e., *Ax*0 = *b*), a tolerance ε and a stepsize β. It then proceeds by iterating

- Let Dk be the diagonal matrix with xk on its diagonal.
- Compute a vector of dual variables: $w^{k}=(AD_{k}^{2}A^{\operatorname {T} })^{-1}AD_{k}^{2}c.$
- Compute a vector of *reduced costs*, which measure the slackness of inequality constraints in the dual: $r^{k}=c-A^{\operatorname {T} }w^{k}.$
- If $r^{k}>0$ and $\mathbf {1} ^{\operatorname {T} }D_{k}r^{k}<\varepsilon$ , the current solution *xk* is ε-optimal.
- If $-D_{k}r^{k}\geq 0$ , the problem is unbounded.
- Update $x^{k+1}=x^{k}-\beta {\frac {D_{k}^{2}r^{k}}{\|D_{k}r^{k}\|}}$

### Initialization

Phase I, the initialization, solves an auxiliary problem with an additional variable u and uses the result to derive an initial point for the original problem. Let *x*0 be an arbitrary, strictly positive point; it need not be feasible for the original problem. The infeasibility of *x*0 is measured by the vector

$v=b-Ax^{0}$

.

If *v* = 0, *x*0 is feasible. If it is not, phase I solves the auxiliary problem

minimize

u

subject to

Ax

+

uv

=

b

,

x

≥ 0

,

u

≥ 0

.

This problem has the right form for solution by the above iterative algorithm, and

${\begin{pmatrix}x^{0}\\1\end{pmatrix}}$

is a feasible initial point for it. Solving the auxiliary problem gives

${\begin{pmatrix}x^{*}\\u^{*}\end{pmatrix}}$

.

If *u** = 0, then *x** ≥0 is feasible in the original problem (though not necessarily strictly interior), while if *u** > 0, the original problem is infeasible.

## Analysis

While easy to state, affine scaling was found hard to analyze. Its convergence depends on the step size, β. For step sizes *β* ≤ ⁠2/3⁠, Vanderbei's variant of affine scaling has been proven to converge, while for *β* > 0.995, an example problem is known that converges to a suboptimal value. Other variants of the algorithm have been shown to exhibit chaotic behavior even on small problems when *β* > ⁠2/3⁠.
