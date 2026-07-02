---
title: "Band matrix"
source: https://en.wikipedia.org/wiki/Band_matrix
domain: sparse-linear-algebra
license: CC-BY-SA-4.0
tags: sparse matrix, iterative method solver, preconditioner, conjugate gradient method
fetched: 2026-07-02
---

# Band matrix

In mathematics, particularly matrix theory, a **band matrix** or **banded matrix** is a sparse matrix whose non-zero entries are confined to a diagonal *band*, comprising the main diagonal and zero or more diagonals on either side.

## Band matrix

### Bandwidth

Formally, consider an *n*×*n* matrix *A*=(*a**i,j* ). If all matrix elements are zero outside a diagonally bordered band whose range is determined by constants *k*1 and *k*2:

$a_{i,j}=0\quad {\mbox{if}}\quad j<i-k_{1}\quad {\mbox{ or }}\quad j>i+k_{2};\quad k_{1},k_{2}\geq 0.\,$

then the quantities *k*1 and *k*2 are called the **lower bandwidth** and **upper bandwidth**, respectively. The **bandwidth** of the matrix is the maximum of *k*1 and *k*2; in other words, it is the number *k* such that $a_{i,j}=0$ if $|i-j|>k$ .

## Examples

- A band matrix with *k*1 = *k*2 = 0 is a diagonal matrix, with bandwidth 0.
- A band matrix with *k*1 = *k*2 = 1 is a tridiagonal matrix, with bandwidth 1.
- For *k*1 = *k*2 = 2 one has a pentadiagonal matrix and so on.
- Triangular matrices
  - For *k*1 = 0, *k*2 = *n*−1, one obtains the definition of an upper triangular matrix
  - similarly, for *k*1 = *n*−1, *k*2 = 0 one obtains a lower triangular matrix.
- Upper and lower Hessenberg matrices
- Toeplitz matrices when bandwidth is limited.
- Block diagonal matrices
- Shift matrices and shear matrices
- Matrices in Jordan normal form
- A skyline matrix, also called "variable band matrix" – a generalization of band matrix
- The inverses of Lehmer matrices are constant tridiagonal matrices, and are thus band matrices.

## Applications

In numerical analysis, matrices from finite element or finite difference problems are often banded. Such matrices can be viewed as descriptions of the coupling between the problem variables; the banded property corresponds to the fact that variables are not coupled over arbitrarily large distances. Such matrices can be further divided – for instance, banded matrices exist where every element in the band is nonzero.

Problems in higher dimensions also lead to banded matrices, in which case the band itself also tends to be sparse. For instance, a partial differential equation on a square domain (using central differences) will yield a matrix with a bandwidth equal to the square root of the matrix dimension, but inside the band only 5 diagonals are nonzero. Unfortunately, applying Gaussian elimination (or equivalently an LU decomposition) to such a matrix results in the band being filled in by many non-zero elements.

## Band storage

Band matrices are usually stored by storing the diagonals in the band; the rest is implicitly zero.

For example, a tridiagonal matrix has bandwidth 1. The 6-by-6 matrix

${\begin{bmatrix}B_{11}&B_{12}&0&\cdots &\cdots &0\\B_{21}&B_{22}&B_{23}&\ddots &\ddots &\vdots \\0&B_{32}&B_{33}&B_{34}&\ddots &\vdots \\\vdots &\ddots &B_{43}&B_{44}&B_{45}&0\\\vdots &\ddots &\ddots &B_{54}&B_{55}&B_{56}\\0&\cdots &\cdots &0&B_{65}&B_{66}\end{bmatrix}}$

is stored as the 6-by-3 matrix

${\begin{bmatrix}0&B_{11}&B_{12}\\B_{21}&B_{22}&B_{23}\\B_{32}&B_{33}&B_{34}\\B_{43}&B_{44}&B_{45}\\B_{54}&B_{55}&B_{56}\\B_{65}&B_{66}&0\end{bmatrix}}.$

A further saving is possible when the matrix is symmetric. For example, consider a symmetric 6-by-6 matrix with an upper bandwidth of 2:

${\begin{bmatrix}A_{11}&A_{12}&A_{13}&0&\cdots &0\\&A_{22}&A_{23}&A_{24}&\ddots &\vdots \\&&A_{33}&A_{34}&A_{35}&0\\&&&A_{44}&A_{45}&A_{46}\\&sym&&&A_{55}&A_{56}\\&&&&&A_{66}\end{bmatrix}}.$

This matrix is stored as the 6-by-3 matrix:

${\begin{bmatrix}A_{11}&A_{12}&A_{13}\\A_{22}&A_{23}&A_{24}\\A_{33}&A_{34}&A_{35}\\A_{44}&A_{45}&A_{46}\\A_{55}&A_{56}&0\\A_{66}&0&0\end{bmatrix}}.$

## Band form of sparse matrices

From a computational point of view, working with band matrices is always preferential to working with similarly dimensioned square matrices. A band matrix can be likened in complexity to a rectangular matrix whose row dimension is equal to the bandwidth of the band matrix. Thus the work involved in performing operations such as multiplication falls significantly, often leading to huge savings in terms of calculation time and complexity.

As sparse matrices lend themselves to more efficient computation than dense matrices, as well as in more efficient utilization of computer storage, there has been much research focused on finding ways to minimise the bandwidth (or directly minimise the fill-in) by applying permutations to the matrix, or other such equivalence or similarity transformations.

The Cuthill–McKee algorithm can be used to reduce the bandwidth of a sparse symmetric matrix. There are, however, matrices for which the reverse Cuthill–McKee algorithm performs better. There are many other methods in use.

The problem of finding a representation of a matrix with minimal bandwidth by means of permutations of rows and columns is NP-hard.
