---
title: "Divide-and-conquer eigenvalue algorithm"
source: https://en.wikipedia.org/wiki/Divide-and-conquer_eigenvalue_algorithm
domain: eigenvalue-solvers
license: CC-BY-SA-4.0
tags: eigenvalue algorithm, lanczos algorithm, arnoldi iteration, qr algorithm
fetched: 2026-07-02
---

# Divide-and-conquer eigenvalue algorithm

**Divide-and-conquer eigenvalue algorithms** are a class of eigenvalue algorithms for Hermitian or real symmetric matrices that have recently (circa 1990s) become competitive in terms of stability and efficiency with more traditional algorithms such as the QR algorithm. The basic concept behind these algorithms is the divide-and-conquer approach from computer science. An eigenvalue problem is divided into two problems of roughly half the size, each of these are solved recursively, and the eigenvalues of the original problem are computed from the results of these smaller problems.

This article covers the basic idea of the algorithm as originally proposed by Cuppen in 1981, which is not numerically stable without additional refinements.

## Background

As with most eigenvalue algorithms for Hermitian matrices, divide-and-conquer begins with a reduction to tridiagonal form. For an $m\times m$ matrix, the standard method for this, via Householder reflections, takes ${\frac {4}{3}}m^{3}$ floating point operations, or ${\frac {8}{3}}m^{3}$ if eigenvectors are needed as well. There are other algorithms, such as the Arnoldi iteration, which may do better for certain classes of matrices; we will not consider this further here.

In certain cases, it is possible to *deflate* an eigenvalue problem into smaller problems. Consider a block diagonal matrix

$T={\begin{bmatrix}T_{1}&0\\0&T_{2}\end{bmatrix}}.$

The eigenvalues and eigenvectors of T are simply those of $T_{1}$ and $T_{2}$ , and it will almost always be faster to solve these two smaller problems than to solve the original problem all at once. This technique can be used to improve the efficiency of many eigenvalue algorithms, but it has special significance to divide-and-conquer.

For the rest of this article, we will assume the input to the divide-and-conquer algorithm is an $m\times m$ real symmetric tridiagonal matrix T . The algorithm can be modified for Hermitian matrices.

## Divide

The *divide* part of the divide-and-conquer algorithm comes from the realization that a tridiagonal matrix is "almost" block diagonal.

The size of submatrix $T_{1}$ we will call $n\times n$ , and then $T_{2}$ is $(m-n)\times (m-n)$ . T is almost block diagonal regardless of how n is chosen. For efficiency we typically choose $n\approx m/2$ .

We write T as a block diagonal matrix, plus a rank-1 correction:

The only difference between $T_{1}$ and ${\hat {T}}_{1}$ is that the lower right entry $t_{nn}$ in ${\hat {T}}_{1}$ has been replaced with $t_{nn}-\beta$ and similarly, in ${\hat {T}}_{2}$ the top left entry $t_{n+1,n+1}$ has been replaced with $t_{n+1,n+1}-\beta$ .

The remainder of the divide step is to solve for the eigenvalues (and if desired the eigenvectors) of ${\hat {T}}_{1}$ and ${\hat {T}}_{2}$ , that is to find the diagonalizations ${\hat {T}}_{1}=Q_{1}D_{1}Q_{1}^{T}$ and ${\hat {T}}_{2}=Q_{2}D_{2}Q_{2}^{T}$ . This can be accomplished with recursive calls to the divide-and-conquer algorithm, although practical implementations often switch to the implicitly shifted QR algorithm for small enough submatrices.

## Conquer

The *conquer* part of the algorithm is the unintuitive part. Given the diagonalizations of the submatrices, calculated above, how do we find the diagonalization of the original matrix?

First, define $z^{T}=(q_{1}^{T},q_{2}^{T})$ , where $q_{1}^{T}$ is the last row of $Q_{1}$ and $q_{2}^{T}$ is the first row of $Q_{2}$ . It is now elementary to show that

$T={\begin{bmatrix}Q_{1}&\\&Q_{2}\end{bmatrix}}\left({\begin{bmatrix}D_{1}&\\&D_{2}\end{bmatrix}}+\beta zz^{T}\right){\begin{bmatrix}Q_{1}^{T}&\\&Q_{2}^{T}\end{bmatrix}}$

The remaining task has been reduced to finding the eigenvalues of a diagonal matrix plus a rank-one correction. Before showing how to do this, let us simplify the notation. We are looking for the eigenvalues of the matrix $D+ww^{T}$ , where D is diagonal with distinct entries and w is any vector with nonzero entries. In this case $w={\sqrt {|\beta |}}\cdot z$ .

The case of a zero entry is simple, since if wi is zero, ( $e_{i}$ ,di) is an eigenpair ( $e_{i}$ is in the standard basis) of $D+ww^{T}$ since $(D+ww^{T})e_{i}=De_{i}=d_{i}e_{i}$ .

If $\lambda$ is an eigenvalue, we have:

$(D+ww^{T})q=\lambda q$

where q is the corresponding eigenvector. Now

$(D-\lambda I)q+w(w^{T}q)=0$

$q+(D-\lambda I)^{-1}w(w^{T}q)=0$

$w^{T}q+w^{T}(D-\lambda I)^{-1}w(w^{T}q)=0$

Keep in mind that $w^{T}q$ is a nonzero scalar. Neither w nor q are zero. If $w^{T}q$ were to be zero, q would be an eigenvector of D by $(D+ww^{T})q=\lambda q$ . If that were the case, q would contain only one nonzero position since D is distinct diagonal and thus the inner product $w^{T}q$ can not be zero after all. Therefore, we have:

$1+w^{T}(D-\lambda I)^{-1}w=0$

or written as a scalar equation,

$1+\sum _{j=1}^{m}{\frac {w_{j}^{2}}{d_{j}-\lambda }}=0.$

This equation is known as the *secular equation*. The problem has therefore been reduced to finding the roots of the rational function defined by the left-hand side of this equation.

Solving the nonlinear secular equation can be done using an iterative technique, such as the Newton–Raphson method. However, each root can be found in O(1) iterations, each of which requires $\Theta (m)$ flops (for an m -degree rational function), making the cost of the iterative part of this algorithm $\Theta (m^{2})$ . The fast multipole method has also been employed to solve the secular equation in $\Theta (m\log(m))$ operations.

## Analysis

W will use the master theorem for divide-and-conquer recurrences to analyze the running time. Remember that above we stated we choose $n\approx m/2$ . We can write the recurrence relation:

$T(m)=2\times T\left({\frac {m}{2}}\right)+\Theta (m^{2})$

In the notation of the Master theorem, $a=b=2$ and thus $\log _{b}a=1$ . Clearly, $\Theta (m^{2})=\Omega (m^{1})$ , so we have

$T(m)=\Theta (m^{2})$

Above, we pointed out that reducing a Hermitian matrix to tridiagonal form takes ${\frac {4}{3}}m^{3}$ flops. This dwarfs the running time of the divide-and-conquer part, and at this point it is not clear what advantage the divide-and-conquer algorithm offers over the QR algorithm (which also takes $\Theta (m^{2})$ flops for tridiagonal matrices).

The advantage of divide-and-conquer comes when eigenvectors are needed as well. If this is the case, reduction to tridiagonal form takes ${\frac {8}{3}}m^{3}$ , but the second part of the algorithm takes $\Theta (m^{3})$ as well. For the QR algorithm with a reasonable target precision, this is $\approx 6m^{3}$ , whereas for divide-and-conquer it is $\approx {\frac {4}{3}}m^{3}$ . The reason for this improvement is that in divide-and-conquer, the $\Theta (m^{3})$ part of the algorithm (multiplying Q matrices) is separate from the iteration, whereas in QR, this must occur in every iterative step. Adding the ${\frac {8}{3}}m^{3}$ flops for the reduction, the total improvement is from $\approx 9m^{3}$ to $\approx 4m^{3}$ flops.

Practical use of the divide-and-conquer algorithm has shown that in most realistic eigenvalue problems, the algorithm actually does better than this. The reason is that very often the matrices Q and the vectors z tend to be *numerically sparse*, meaning that they have many entries with values smaller than the floating point precision, allowing for *numerical deflation*, i.e. breaking the problem into uncoupled subproblems.

## Variants and implementation

The algorithm presented here is the simplest version. In many practical implementations, more complicated rank-1 corrections are used to guarantee stability; some variants even use rank-2 corrections.

There exist specialized root-finding techniques for rational functions that may do better than the Newton-Raphson method in terms of both performance and stability. These can be used to improve the iterative part of the divide-and-conquer algorithm.

The divide-and-conquer algorithm is readily parallelized, and linear algebra computing packages such as LAPACK contain high-quality parallel implementations.
