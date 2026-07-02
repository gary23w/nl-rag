---
title: "Incomplete LU factorization"
source: https://en.wikipedia.org/wiki/Incomplete_LU_factorization
domain: preconditioning-numerical
license: CC-BY-SA-4.0
tags: preconditioner matrix, incomplete lu factorization, condition number, schur complement
fetched: 2026-07-02
---

# Incomplete LU factorization

In numerical linear algebra, an **incomplete LU factorization** (abbreviated as **ILU**) of a matrix is a sparse approximation of the LU factorization often used as a preconditioner.

## Introduction

Consider a sparse linear system $Ax=b$ . These are often solved by computing the factorization $A=LU$ , with *L* lower unitriangular and *U* upper triangular. One then solves $Ly=b$ , $Ux=y$ , which can be done efficiently because the matrices are triangular.

For a typical sparse matrix, the LU factors can be much less sparse than the original matrix — a phenomenon called *fill-in*. The memory requirements for using a direct solver can then become a bottleneck in solving linear systems. One can combat this problem by using fill-reducing reorderings of the matrix's unknowns, such as the Minimum degree algorithm.

An incomplete factorization instead seeks triangular matrices *L*, *U* such that $A\approx LU$ rather than $A=LU$ . Solving for $LUx=b$ can be done quickly but does not yield the exact solution to $Ax=b$ . So, we instead use the matrix $M=LU$ as a preconditioner in another iterative solution algorithm such as the conjugate gradient method or GMRES.

## Definition

For a given matrix $A\in \mathbb {R} ^{n\times n}$ one defines the graph $G(A)$ as

$G(A):=\left\lbrace (i,j)\in \mathbb {N} ^{2}:A_{ij}\neq 0\right\rbrace \,,$

which is used to define the conditions a *sparsity pattern* S needs to fulfill

$S\subset \left\lbrace 1,\dots ,n\right\rbrace ^{2}\,,\quad \left\lbrace (i,i):1\leq i\leq n\right\rbrace \subset S\,,\quad G(A)\subset S\,.$

A decomposition of the form $A=LU-R$ where the following hold

- $L\in \mathbb {R} ^{n\times n}$ is a lower unitriangular matrix
- $U\in \mathbb {R} ^{n\times n}$ is an upper triangular matrix
- $L,U$ are zero outside of the sparsity pattern: $L_{ij}=U_{ij}=0\quad \forall \;(i,j)\notin S$
- $R\in \mathbb {R} ^{n\times n}$ is zero within the sparsity pattern: $R_{ij}=0\quad \forall \;(i,j)\in S$

is called an **incomplete LU decomposition** (with respect to the sparsity pattern S ).

The sparsity pattern of *L* and *U* is often chosen to be the same as the sparsity pattern of the original matrix *A*. If the underlying matrix structure can be referenced by pointers instead of copied, the only extra memory required is for the entries of *L* and *U*. This preconditioner is called ILU(0).

## Stability

Concerning the stability of the ILU the following theorem was proven by Meijerink and van der Vorst.

Let A be an M-matrix, the (complete) LU decomposition given by $A={\hat {L}}{\hat {U}}$ , and the ILU by $A=LU-R$ . Then

$|L_{ij}|\leq |{\hat {L}}_{ij}|\quad \forall \;i,j$

holds. Thus, the ILU is at least as stable as the (complete) LU decomposition.

## Generalizations

One can obtain a more accurate preconditioner by allowing some level of extra fill in the factorization. A common choice is to use the sparsity pattern of *A2* instead of *A*; this matrix is appreciably more dense than *A*, but still sparse over all. This preconditioner is called ILU(1). One can then generalize this procedure; the ILU(k) preconditioner of a matrix *A* is the incomplete LU factorization with the sparsity pattern of the matrix *Ak+1*.

More accurate ILU preconditioners require more memory, to such an extent that eventually the running time of the algorithm increases even though the total number of iterations decreases. Consequently, there is a cost/accuracy trade-off that users must evaluate, typically on a case-by-case basis depending on the family of linear systems to be solved.

An approximation to the ILU factorization can be performed as a fixed-point iteration in a highly parallel way.
