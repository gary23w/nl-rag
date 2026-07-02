---
title: "Biconjugate gradient method"
source: https://en.wikipedia.org/wiki/Biconjugate_gradient_method
domain: conjugate-gradient-method
license: CC-BY-SA-4.0
tags: conjugate gradient method, nonlinear conjugate gradient, line search, steepest descent
fetched: 2026-07-02
---

# Biconjugate gradient method

In mathematics, more specifically in numerical linear algebra, the **biconjugate gradient method** is an algorithm to solve systems of linear equations

$Ax=b.\,$

Unlike the conjugate gradient method, this algorithm does not require the matrix A to be self-adjoint, but instead one needs to perform multiplications by the conjugate transpose *A**.

## The Algorithm

1. Choose initial guess $x_{0}\,$ , two other vectors $x_{0}^{*}$ and $b^{*}\,$ and a preconditioner $M\,$
2. $r_{0}\leftarrow b-A\,x_{0}\,$
3. $r_{0}^{*}\leftarrow b^{*}-x_{0}^{*}\,A^{*}$
4. $p_{0}\leftarrow M^{-1}r_{0}\,$
5. $p_{0}^{*}\leftarrow r_{0}^{*}M^{-1}\,$
6. for $k=0,1,\ldots$ do
  1. $\alpha _{k}\leftarrow {r_{k}^{*}M^{-1}r_{k} \over p_{k}^{*}Ap_{k}}\,$
  2. $x_{k+1}\leftarrow x_{k}+\alpha _{k}\cdot p_{k}\,$
  3. $x_{k+1}^{*}\leftarrow x_{k}^{*}+{\overline {\alpha _{k}}}\cdot p_{k}^{*}\,$
  4. $r_{k+1}\leftarrow r_{k}-\alpha _{k}\cdot Ap_{k}\,$
  5. $r_{k+1}^{*}\leftarrow r_{k}^{*}-{\overline {\alpha _{k}}}\cdot p_{k}^{*}\,A^{*}$
  6. $\beta _{k}\leftarrow {r_{k+1}^{*}M^{-1}r_{k+1} \over r_{k}^{*}M^{-1}r_{k}}\,$
  7. $p_{k+1}\leftarrow M^{-1}r_{k+1}+\beta _{k}\cdot p_{k}\,$
  8. $p_{k+1}^{*}\leftarrow r_{k+1}^{*}M^{-1}+{\overline {\beta _{k}}}\cdot p_{k}^{*}\,$

In the above formulation, the computed $r_{k}\,$ and $r_{k}^{*}$ satisfy

$r_{k}=b-Ax_{k},\,$

$r_{k}^{*}=b^{*}-x_{k}^{*}\,A^{*}$

and thus are the respective residuals corresponding to $x_{k}\,$ and $x_{k}^{*}$ , as approximate solutions to the systems

$Ax=b,\,$

$x^{*}\,A^{*}=b^{*}\,;$

$x^{*}$ is the adjoint, and ${\overline {\alpha }}$ is the complex conjugate.

### Unpreconditioned version of the algorithm

1. Choose initial guess $x_{0}\,$ ,
2. $r_{0}\leftarrow b-A\,x_{0}\,$
3. ${\hat {r}}_{0}\leftarrow {\hat {b}}-{\hat {x}}_{0}A^{*}$
4. $p_{0}\leftarrow r_{0}\,$
5. ${\hat {p}}_{0}\leftarrow {\hat {r}}_{0}\,$
6. for $k=0,1,\ldots$ do
  1. $\alpha _{k}\leftarrow {{\hat {r}}_{k}r_{k} \over {\hat {p}}_{k}Ap_{k}}\,$
  2. $x_{k+1}\leftarrow x_{k}+\alpha _{k}\cdot p_{k}\,$
  3. ${\hat {x}}_{k+1}\leftarrow {\hat {x}}_{k}+\alpha _{k}\cdot {\hat {p}}_{k}\,$
  4. $r_{k+1}\leftarrow r_{k}-\alpha _{k}\cdot Ap_{k}\,$
  5. ${\hat {r}}_{k+1}\leftarrow {\hat {r}}_{k}-\alpha _{k}\cdot {\hat {p}}_{k}A^{*}$
  6. $\beta _{k}\leftarrow {{\hat {r}}_{k+1}r_{k+1} \over {\hat {r}}_{k}r_{k}}\,$
  7. $p_{k+1}\leftarrow r_{k+1}+\beta _{k}\cdot p_{k}\,$
  8. ${\hat {p}}_{k+1}\leftarrow {\hat {r}}_{k+1}+\beta _{k}\cdot {\hat {p}}_{k}\,$

## Discussion

The biconjugate gradient method is numerically unstable (compare to the biconjugate gradient stabilized method), but very important from a theoretical point of view. Define the iteration steps by

$x_{k}:=x_{j}+P_{k}A^{-1}\left(b-Ax_{j}\right),$

$x_{k}^{*}:=x_{j}^{*}+\left(b^{*}-x_{j}^{*}A\right)P_{k}A^{-1},$

where $j<k$ using the related projection

$P_{k}:=\mathbf {u} _{k}\left(\mathbf {v} _{k}^{*}A\mathbf {u} _{k}\right)^{-1}\mathbf {v} _{k}^{*}A,$

with

$\mathbf {u} _{k}=\left[u_{0},u_{1},\dots ,u_{k-1}\right],$

$\mathbf {v} _{k}=\left[v_{0},v_{1},\dots ,v_{k-1}\right].$

These related projections may be iterated themselves as

$P_{k+1}=P_{k}+\left(1-P_{k}\right)u_{k}\otimes {v_{k}^{*}A\left(1-P_{k}\right) \over v_{k}^{*}A\left(1-P_{k}\right)u_{k}}.$

A relation to Quasi-Newton methods is given by $P_{k}=A_{k}^{-1}A$ and $x_{k+1}=x_{k}-A_{k+1}^{-1}\left(Ax_{k}-b\right)$ , where

$A_{k+1}^{-1}=A_{k}^{-1}+\left(1-A_{k}^{-1}A\right)u_{k}\otimes {v_{k}^{*}\left(1-AA_{k}^{-1}\right) \over v_{k}^{*}A\left(1-A_{k}^{-1}A\right)u_{k}}.$

The new directions

$p_{k}=\left(1-P_{k}\right)u_{k},$

$p_{k}^{*}=v_{k}^{*}A\left(1-P_{k}\right)A^{-1}$

are then orthogonal to the residuals:

$v_{i}^{*}r_{k}=p_{i}^{*}r_{k}=0,$

$r_{k}^{*}u_{j}=r_{k}^{*}p_{j}=0,$

which themselves satisfy

$r_{k}=A\left(1-P_{k}\right)A^{-1}r_{j},$

$r_{k}^{*}=r_{j}^{*}\left(1-P_{k}\right)$

where $i,j<k$ .

The biconjugate gradient method now makes a special choice and uses the setting

$u_{k}=M^{-1}r_{k},\,$

$v_{k}^{*}=r_{k}^{*}\,M^{-1}.\,$

With this particular choice, explicit evaluations of $P_{k}$ and *A*−1 are avoided, and the algorithm takes the form stated above.

## Properties

- If $A=A^{*}\,$ is self-adjoint, $x_{0}^{*}=x_{0}$ and $b^{*}=b$ , then $r_{k}=r_{k}^{*}$ , $p_{k}=p_{k}^{*}$ , and the conjugate gradient method produces the same sequence $x_{k}=x_{k}^{*}$ at half the computational cost.
- The sequences produced by the algorithm are biorthogonal, i.e., $p_{i}^{*}Ap_{j}=r_{i}^{*}M^{-1}r_{j}=0$ for $i\neq j$ .
- if $P_{j'}\,$ is a polynomial with $\deg \left(P_{j'}\right)+j<k$ , then $r_{k}^{*}P_{j'}\left(M^{-1}A\right)u_{j}=0$ . The algorithm thus produces projections onto the Krylov subspace.
- if $P_{i'}\,$ is a polynomial with $i+\deg \left(P_{i'}\right)<k$ , then $v_{i}^{*}P_{i'}\left(AM^{-1}\right)r_{k}=0$ .
