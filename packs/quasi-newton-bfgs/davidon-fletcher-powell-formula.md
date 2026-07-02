---
title: "Davidon–Fletcher–Powell formula"
source: https://en.wikipedia.org/wiki/Davidon–Fletcher–Powell_formula
domain: quasi-newton-bfgs
license: CC-BY-SA-4.0
tags: quasi newton method, bfgs update, limited memory bfgs, hessian approximation
fetched: 2026-07-02
---

# Davidon–Fletcher–Powell formula

The **Davidon–Fletcher–Powell formula** (or **DFP**; named after William C. Davidon, Roger Fletcher, and Michael J. D. Powell) finds the solution to the secant equation that is closest to the current estimate and satisfies the curvature condition. It was the first quasi-Newton method to generalize the secant method to a multidimensional problem. This update maintains the symmetry and positive definiteness of the Hessian matrix.

Given a smooth function $f(x)$ , its gradient ( $\nabla f$ ), and positive-definite Hessian matrix B , the Taylor series is

$f(x_{k}+s_{k})=f(x_{k})+\nabla f(x_{k})^{T}s_{k}+{\frac {1}{2}}s_{k}^{T}{B}s_{k}+\dots ,$

and the Taylor series of the gradient itself (secant equation)

$\nabla f(x_{k}+s_{k})=\nabla f(x_{k})+Bs_{k}+\dots$

is used to update B .

The DFP formula finds a solution that is symmetric, positive-definite and closest to the current approximate value of $B_{k}$ :

$B_{k+1}=(I-\gamma _{k}y_{k}s_{k}^{T})B_{k}(I-\gamma _{k}s_{k}y_{k}^{T})+\gamma _{k}y_{k}y_{k}^{T},$

where

$y_{k}=\nabla f(x_{k}+s_{k})-\nabla f(x_{k}),$

$\gamma _{k}={\frac {1}{y_{k}^{T}s_{k}}},$

and $B_{k}$ is a symmetric and positive-definite matrix.

The corresponding update to the inverse Hessian approximation $H_{k}=B_{k}^{-1}$ is given by

$H_{k+1}=H_{k}-{\frac {H_{k}y_{k}y_{k}^{T}H_{k}}{y_{k}^{T}H_{k}y_{k}}}+{\frac {s_{k}s_{k}^{T}}{y_{k}^{T}s_{k}}}.$

B is assumed to be positive-definite, and the vectors $s_{k}^{T}$ and y must satisfy the curvature condition

$s_{k}^{T}y_{k}=s_{k}^{T}Bs_{k}>0.$

The DFP formula is quite effective, but it was soon superseded by the Broyden–Fletcher–Goldfarb–Shanno formula, which is its dual (interchanging the roles of *y* and *s*).

## Compact representation

By unwinding the matrix recurrence for $B_{k}$ , the DFP formula can be expressed as a compact matrix representation. Specifically, defining

$S_{k}={\begin{bmatrix}s_{0}&s_{1}&\ldots &s_{k-1}\end{bmatrix}},$ $Y_{k}={\begin{bmatrix}y_{0}&y_{1}&\ldots &y_{k-1}\end{bmatrix}},$

and upper triangular and diagonal matrices

${\big (}R_{k}{\big )}_{ij}:={\big (}R_{k}^{\text{SY}}{\big )}_{ij}=s_{i-1}^{T}y_{j-1},\quad {\big (}R_{k}^{\text{YS}}{\big )}_{ij}=y_{i-1}^{T}s_{j-1},\quad (D_{k})_{ii}:={\big (}D_{k}^{\text{SY}}{\big )}_{ii}=s_{i-1}^{T}y_{i-1}\quad \quad {\text{ for }}1\leq i\leq j\leq k$

the DFP matrix has the equivalent formula

$B_{k}=B_{0}+J_{k}N_{k}^{-1}J_{k}^{T},$

$J_{k}={\begin{bmatrix}Y_{k}&Y_{k}-B_{0}S_{k}\end{bmatrix}}$

$N_{k}={\begin{bmatrix}0_{k\times k}&R_{k}^{\text{YS}}\\{\big (}R_{k}^{\text{YS}}{\big )}^{T}&R_{k}+R_{k}^{T}-(D_{k}+S_{k}^{T}B_{0}S_{k})\end{bmatrix}}$

The inverse compact representation can be found by applying the Sherman-Morrison-Woodbury inverse to $B_{k}$ . The compact representation is particularly useful for limited-memory and constrained problems.
