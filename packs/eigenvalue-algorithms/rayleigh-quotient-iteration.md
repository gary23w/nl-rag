---
title: "Rayleigh quotient iteration"
source: https://en.wikipedia.org/wiki/Rayleigh_quotient_iteration
domain: eigenvalue-algorithms
license: CC-BY-SA-4.0
tags: eigenvalue algorithm, power iteration, rayleigh quotient iteration, jacobi eigenvalue algorithm
fetched: 2026-07-02
---

# Rayleigh quotient iteration

**Rayleigh quotient iteration** is an eigenvalue algorithm which extends the idea of the inverse iteration by using the Rayleigh quotient to obtain increasingly accurate eigenvalue estimates.

Rayleigh quotient iteration is an iterative method, that is, it delivers a sequence of approximate solutions that converges to a true solution in the limit. Very rapid convergence is guaranteed and no more than a few iterations are needed in practice to obtain a reasonable approximation. The Rayleigh quotient iteration algorithm converges cubically for Hermitian or symmetric matrices, given an initial vector that is sufficiently close to an eigenvector of the matrix that is being analyzed.

## Algorithm

The algorithm is very similar to inverse iteration, but replaces the estimated eigenvalue at the end of each iteration with the Rayleigh quotient. Begin by choosing some value $\mu _{0}$ as an initial eigenvalue guess for the Hermitian matrix A . An initial vector $b_{0}$ must also be supplied as initial eigenvector guess.

Calculate the next approximation of the eigenvector $b_{i+1}$ by $b_{i+1}={\frac {(A-\mu _{i}I)^{-1}b_{i}}{\|(A-\mu _{i}I)^{-1}b_{i}\|}},$ where I is the identity matrix, and set the next approximation of the eigenvalue to the Rayleigh quotient of the current iteration equal to $\mu _{i+1}={\frac {b_{i+1}^{*}Ab_{i+1}}{b_{i+1}^{*}b_{i+1}}}.$

To compute more than one eigenvalue, the algorithm can be combined with a deflation technique.

Note that for very small problems it is beneficial to replace the matrix inverse with the adjugate, which will yield the same iteration because it is equal to the inverse up to an irrelevant scale (the inverse of the determinant, specifically). The adjugate is easier to compute explicitly than the inverse (though the inverse is easier to apply to a vector for problems that aren't small), and is more numerically sound because it remains well defined as the eigenvalue converges.

## Example

Consider the matrix

$A=\left[{\begin{matrix}1&2&3\\1&2&1\\3&2&1\\\end{matrix}}\right]$

for which the exact eigenvalues are $\lambda _{1}=3+{\sqrt {5}}$ , $\lambda _{2}=3-{\sqrt {5}}$ and $\lambda _{3}=-2$ , with corresponding eigenvectors

$v_{1}=\left[{\begin{matrix}1\\\varphi -1\\1\\\end{matrix}}\right]$

,

$v_{2}=\left[{\begin{matrix}1\\-\varphi \\1\\\end{matrix}}\right]$

and

$v_{3}=\left[{\begin{matrix}1\\0\\1\\\end{matrix}}\right]$

.

(where $\textstyle \varphi ={\frac {1+{\sqrt {5}}}{2}}$ is the golden ratio).

The largest eigenvalue is $\lambda _{1}\approx 5.2361$ and corresponds to any eigenvector proportional to $v_{1}\approx \left[{\begin{matrix}1\\0.6180\\1\\\end{matrix}}\right].$

We begin with an initial eigenvalue guess of

$b_{0}=\left[{\begin{matrix}1\\1\\1\\\end{matrix}}\right],~\mu _{0}=200$

.

Then, the first iteration yields

$b_{1}\approx \left[{\begin{matrix}-0.57927\\-0.57348\\-0.57927\\\end{matrix}}\right],~\mu _{1}\approx 5.3355$

the second iteration,

$b_{2}\approx \left[{\begin{matrix}0.64676\\0.40422\\0.64676\\\end{matrix}}\right],~\mu _{2}\approx 5.2418$

and the third,

$b_{3}\approx \left[{\begin{matrix}-0.64793\\-0.40045\\-0.64793\\\end{matrix}}\right],~\mu _{3}\approx 5.2361$

from which the cubic convergence is evident.

## Octave implementation

The following is a simple implementation of the algorithm in Octave.

```mw
function x = rayleigh(A, epsilon, mu, x)
  x = x / norm(x);
  % the backslash operator in Octave solves a linear system
  y = (A - mu * eye(rows(A))) \ x; 
  lambda = y' * x;
  mu = mu + 1 / lambda
  err = norm(y - lambda * x) / norm(y)

  while err > epsilon
    x = y / norm(y);
    y = (A - mu * eye(rows(A))) \ x;
    lambda = y' * x;
    mu = mu + 1 / lambda
    err = norm(y - lambda * x) / norm(y)
  end

end
```
