---
title: "Minimal residual method"
source: https://en.wikipedia.org/wiki/Minimal_residual_method
domain: krylov-subspace-methods
license: CC-BY-SA-4.0
tags: krylov subspace, generalized minimal residual method, arnoldi iteration, lanczos algorithm
fetched: 2026-07-02
---

# Minimal residual method

The **Minimal Residual Method** or **MINRES** is a Krylov subspace method for the iterative solution of symmetric linear equation systems. It was proposed by mathematicians Christopher Conway Paige and Michael Alan Saunders in 1975.

In contrast to the popular CG method, the MINRES method does not assume that the matrix is positive definite, only the symmetry of the matrix is mandatory.

## GMRES vs. MINRES

The GMRES method is essentially a generalization of MINRES for arbitrary matrices. Both minimize the 2-norm of the residual and do the same calculations in exact arithmetic when the matrix is symmetric. MINRES is a short-recurrence method with a constant memory requirement, whereas GMRES requires storing the whole Krylov space, so its memory requirement is roughly proportional to the number of iterations. On the other hand, GMRES tends to suffer less from loss of orthogonality.

## Properties of the MINRES method

The MINRES method iteratively calculates an approximate solution of a linear system of equations of the form $Ax=b,$ where $A\in \mathbb {R} ^{n\times n}$ is a symmetric matrix and $b\in \mathbb {R} ^{n}$ a vector.

For this, the norm of the residual $r(x):=b-Ax$ in a k -dimensional Krylov subspace $V_{k}=x_{0}+\operatorname {span} \{r_{0},Ar_{0}\ldots ,A^{k-1}r_{0}\}$ is minimized. Here $x_{0}\in \mathbb {R} ^{n}$ is an initial value (often zero) and $r_{0}:=r(x_{0})$ .

More precisely, we define the approximate solutions $x_{k}$ through $x_{k}:=\mathrm {argmin} _{x\in V_{k}}\|r(x)\|,$ where $\|\cdot \|$ is the standard Euclidean norm on $\mathbb {R} ^{n}$ .

Because of the symmetry of A , unlike in the GMRES method, it is possible to carry out this minimization process recursively, storing only two previous steps (short recurrence). This saves memory.

## MINRES algorithm

Note: The MINRES method is more complicated than the algebraically equivalent Conjugate Residual method. The Conjugate Residual (CR) method was therefore produced below as a substitute. It differs from MINRES is that in MINRES, the columns of a basis of the Krylov space (denoted below by $p_{k}$ ) can be orthogonalized, whereas in CR their images (below labeled with $s_{k}$ ) can be orthogonalized via the Lanczos recursion. There are more efficient and preconditioned variants with fewer AXPYs. Compare with the article.

First you choose $x_{0}\in \mathbb {R} ^{n}$ arbitrary and compute ${\begin{aligned}r_{0}&=b-Ax_{0}\\p_{0}&=r_{0}\\s_{0}&=Ap_{0}\end{aligned}}$

Then we iterate for $k=1,2,\dots$ in the following steps:

- Compute $x_{k},r_{k}$ through $\alpha _{k-1}={\frac {\langle r_{k-1},s_{k-1}\rangle }{\langle s_{k-1},s_{k-1}\rangle }}$ $x_{k}=x_{k-1}+\alpha _{k-1}p_{k-1}$ $r_{k}=r_{k-1}-\alpha _{k-1}s_{k-1}$ if $\|r_{k}\|$ is smaller than a specified tolerance, the algorithm is interrupted with the approximate solution $x_{k}$ . Otherwise, a new descent direction $p_{k}$ is calculated through $p_{k}\leftarrow s_{k-1}$ $s_{k}\leftarrow As_{k-1}$
- for $l=1,2$ (the step $l=2$ is not carried out in the first iteration step) calculate: $\beta _{k,l}={\frac {\langle s_{k},s_{k-l}\rangle }{\langle s_{k-l},s_{k-l}\rangle }}$ $p_{k}\leftarrow p_{k}-\beta _{k,l}p_{k-l}$ $s_{k}\leftarrow s_{k}-\beta _{k,l}s_{k-l}$

## Convergence rate of the MINRES method

In the case of positive definite matrices, the convergence rate of the MINRES method can be estimated in a way similar to that of the CG method. In contrast to the CG method, however, the estimation does not apply to the errors of the iterates, but to the residual. The following applies:

$\|r_{k}\|\leq 2\left({\frac {{\sqrt {\kappa (A)}}-1}{{\sqrt {\kappa (A)}}+1}}\right)^{k}\|r_{0}\|,$

where $\kappa (A)$ is the condition number of matrix A . Because A is normal, we have $\kappa (A)={\frac {\left|\lambda _{\text{max}}(A)\right|}{\left|\lambda _{\text{min}}(A)\right|}},$ where $\lambda _{\text{max}}(A)$ and $\lambda _{\text{min}}(A)$ are maximal and minimal eigenvalues of A , respectively.

## Implementation in GNU Octave / MATLAB

```mw
function [x, r] = minres(A, b, x0, maxit, tol)
  x = x0;
  r = b - A * x0;
  p0 = r;
  s0 = A * p0;
  p1 = p0;
  s1 = s0;
  for iter = 1:maxit
    p2 = p1; p1 = p0;
    s2 = s1; s1 = s0;
    alpha = r'*s1 / (s1'*s1);
    x = x + alpha * p1;
    r = r - alpha * s1;
    if (r'*r < tol^2)
      break
    end
    p0 = s1;
    s0 = A * s1;
    beta1 = s0'*s1 / (s1'*s1);
    p0 = p0 - beta1 * p1;
    s0 = s0 - beta1 * s1;
    if iter > 1
      beta2 = s0'*s2 / (s2'*s2);
      p0 = p0 - beta2 * p2;
      s0 = s0 - beta2 * s2;
    end
  end
end
```
