---
title: "Sparse matrix–vector multiplication"
source: https://en.wikipedia.org/wiki/Sparse_matrix%E2%80%93vector_multiplication
domain: sparse-linear-algebra
license: CC-BY-SA-4.0
tags: sparse matrix, iterative method solver, preconditioner, conjugate gradient method
fetched: 2026-07-02
---

# Sparse matrix–vector multiplication

**Sparse matrix–vector multiplication** (**SpMV**) of the form *y* = *Ax* is a widely used computational kernel existing in many scientific applications. The input matrix A is sparse. The input vector x and the output vector y are dense. In the case of a repeated *y* = *Ax* operation involving the same input matrix A but possibly changing numerical values of its elements, A can be preprocessed to reduce both the parallel and sequential run time of the SpMV kernel.
