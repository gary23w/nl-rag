---
title: "Conjugate residual method"
source: https://en.wikipedia.org/wiki/Conjugate_residual_method
domain: krylov-subspace-methods
license: CC-BY-SA-4.0
tags: krylov subspace, generalized minimal residual method, arnoldi iteration, lanczos algorithm
fetched: 2026-07-02
---

# Conjugate residual method

The **conjugate residual method** is an iterative numeric method used for solving systems of linear equations. It's a Krylov subspace method very similar to the much more popular conjugate gradient method, with similar construction and convergence properties.

This method is used to solve linear equations of the form

$\mathbf {A} \mathbf {x} =\mathbf {b}$

where **A** is an invertible and Hermitian matrix, and **b** is nonzero.

The conjugate residual method differs from the closely related conjugate gradient method. It involves more numerical operations and requires more storage.

Given an (arbitrary) initial estimate of the solution $\mathbf {x} _{0}$ , the method is outlined below:

${\begin{aligned}&\mathbf {x} _{0}:={\text{Some initial guess}}\\&\mathbf {r} _{0}:=\mathbf {b} -\mathbf {Ax} _{0}\\&\mathbf {p} _{0}:=\mathbf {r} _{0}\\&{\text{Iterate, with }}k{\text{ starting at }}0:\\&\qquad \alpha _{k}:={\frac {\mathbf {r} _{k}^{\mathrm {T} }\mathbf {Ar} _{k}}{(\mathbf {Ap} _{k})^{\mathrm {T} }\mathbf {Ap} _{k}}}\\&\qquad \mathbf {x} _{k+1}:=\mathbf {x} _{k}+\alpha _{k}\mathbf {p} _{k}\\&\qquad \mathbf {r} _{k+1}:=\mathbf {r} _{k}-\alpha _{k}\mathbf {Ap} _{k}\\&\qquad \beta _{k}:={\frac {\mathbf {r} _{k+1}^{\mathrm {T} }\mathbf {Ar} _{k+1}}{\mathbf {r} _{k}^{\mathrm {T} }\mathbf {Ar} _{k}}}\\&\qquad \mathbf {p} _{k+1}:=\mathbf {r} _{k+1}+\beta _{k}\mathbf {p} _{k}\\&\qquad \mathbf {Ap} _{k+1}:=\mathbf {Ar} _{k+1}+\beta _{k}\mathbf {Ap} _{k}\\&\qquad k:=k+1\end{aligned}}$

the iteration may be stopped once $\mathbf {x} _{k}$ has been deemed converged. The only difference between this and the conjugate gradient method is the calculation of $\alpha _{k}$ and $\beta _{k}$ (plus the optional incremental calculation of $\mathbf {Ap} _{k}$ at the end).

Note: the above algorithm can be transformed so to make only one symmetric matrix-vector multiplication in each iteration.

## Preconditioning

By making a few substitutions and variable changes, a preconditioned conjugate residual method may be derived in the same way as done for the conjugate gradient method:

${\begin{aligned}&\mathbf {x} _{0}:={\text{Some initial guess}}\\&\mathbf {r} _{0}:=\mathbf {M} ^{-1}(\mathbf {b} -\mathbf {Ax} _{0})\\&\mathbf {p} _{0}:=\mathbf {r} _{0}\\&{\text{Iterate, with }}k{\text{ starting at }}0:\\&\qquad \alpha _{k}:={\frac {\mathbf {r} _{k}^{\mathrm {T} }\mathbf {A} \mathbf {r} _{k}}{(\mathbf {Ap} _{k})^{\mathrm {T} }\mathbf {M} ^{-1}\mathbf {Ap} _{k}}}\\&\qquad \mathbf {x} _{k+1}:=\mathbf {x} _{k}+\alpha _{k}\mathbf {p} _{k}\\&\qquad \mathbf {r} _{k+1}:=\mathbf {r} _{k}-\alpha _{k}\mathbf {M} ^{-1}\mathbf {Ap} _{k}\\&\qquad \beta _{k}:={\frac {\mathbf {r} _{k+1}^{\mathrm {T} }\mathbf {A} \mathbf {r} _{k+1}}{\mathbf {r} _{k}^{\mathrm {T} }\mathbf {A} \mathbf {r} _{k}}}\\&\qquad \mathbf {p} _{k+1}:=\mathbf {r} _{k+1}+\beta _{k}\mathbf {p} _{k}\\&\qquad \mathbf {Ap} _{k+1}:=\mathbf {A} \mathbf {r} _{k+1}+\beta _{k}\mathbf {Ap} _{k}\\&\qquad k:=k+1\\\end{aligned}}$

The preconditioner $\mathbf {M} ^{-1}$ must be symmetric positive definite. Note that the residual vector here is different from the residual vector without preconditioning.
