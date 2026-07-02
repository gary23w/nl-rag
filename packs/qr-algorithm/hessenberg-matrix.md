---
title: "Hessenberg matrix"
source: https://en.wikipedia.org/wiki/Hessenberg_matrix
domain: qr-algorithm
license: CC-BY-SA-4.0
tags: qr algorithm, qr decomposition, hessenberg matrix, givens rotation
fetched: 2026-07-02
---

# Hessenberg matrix

In linear algebra, a **Hessenberg matrix** is a special kind of square matrix, one that is "almost" triangular. To be exact, an **upper Hessenberg matrix** has zero entries below the first subdiagonal, and a **lower Hessenberg matrix** has zero entries above the first superdiagonal. They are named after Karl Hessenberg.

A **Hessenberg decomposition** is a matrix decomposition of a matrix A into a unitary matrix P and a Hessenberg matrix H such that $PHP^{*}=A$ where $P^{*}$ denotes the conjugate transpose.

## Definitions

### Upper Hessenberg matrix

A square $n\times n$ matrix A is said to be in **upper Hessenberg form** or to be an **upper Hessenberg matrix** if $a_{i,j}=0$ for all $i,j$ with $i>j+1$ .

An upper Hessenberg matrix is called **unreduced** if all subdiagonal entries are nonzero, i.e. if $a_{i+1,i}\neq 0$ for all $i\in \{1,\ldots ,n-1\}$ .

### Lower Hessenberg matrix

A square $n\times n$ matrix A is said to be in **lower Hessenberg form** or to be a **lower Hessenberg matrix** if its transpose {\displaystyle } ({\displaystyle }) is an upper Hessenberg matrix or equivalently if $a_{i,j}=0$ for all $i,j$ with $j>i+1$ .

A lower Hessenberg matrix is called **unreduced** if all superdiagonal entries are nonzero, i.e. if $a_{i,i+1}\neq 0$ for all $i\in \{1,\ldots ,n-1\}$ .

## Examples

Consider the following matrices. $A={\begin{bmatrix}1&4&2&3\\3&4&1&7\\0&2&3&4\\0&0&1&3\\\end{bmatrix}}$ $B={\begin{bmatrix}1&2&0&0\\5&2&3&0\\3&4&3&7\\5&6&1&1\\\end{bmatrix}}$ $C={\begin{bmatrix}1&2&0&0\\5&2&0&0\\3&4&3&7\\5&6&1&1\\\end{bmatrix}}$

The matrix A is an upper unreduced Hessenberg matrix, B is a lower unreduced Hessenberg matrix and C is a lower Hessenberg matrix but is not unreduced.

## Computer programming

Many linear algebra algorithms require significantly less computational effort when applied to triangular matrices, and this improvement often carries over to Hessenberg matrices as well. If the constraints of a linear algebra problem do not allow a general matrix to be conveniently reduced to a triangular one, reduction to Hessenberg form is often the next best thing. In fact, reduction of any matrix to a Hessenberg form can be achieved in a finite number of steps (for example, through Householder's transformation of unitary similarity transforms). Subsequent reduction of Hessenberg matrix to a triangular matrix can be achieved through iterative procedures, such as shifted QR-factorization. In eigenvalue algorithms, the Hessenberg matrix can be further reduced to a triangular matrix through Shifted QR-factorization combined with deflation steps. Reducing a general matrix to a Hessenberg matrix and then reducing further to a triangular matrix, instead of directly reducing a general matrix to a triangular matrix, often economizes the arithmetic involved in the QR algorithm for eigenvalue problems.

## Reduction to Hessenberg matrix

### Householder transformations

Any $n\times n$ matrix can be transformed into a Hessenberg matrix by a similarity transformation using Householder transformations. The following procedure for such a transformation is adapted from **A Second Course In Linear Algebra** by *Garcia & Horn*.

Let A be any real or complex $n\times n$ matrix, then let $A^{\prime }$ be the $(n-1)\times n$ submatrix of A constructed by removing the first row in A and let $\mathbf {a} _{1}^{\prime }$ be the first column of $A'$ . Construct the $(n-1)\times (n-1)$ householder matrix $V_{1}=I_{(n-1)}-2{\frac {ww^{*}}{\|w\|^{2}}}$ where $w={\begin{cases}\|\mathbf {a} _{1}^{\prime }\|_{2}\mathbf {e} _{1}-\mathbf {a} _{1}^{\prime }\;\;\;\;\;\;\;\;,\;\;\;a_{11}^{\prime }=0\\\|\mathbf {a} _{1}^{\prime }\|_{2}\mathbf {e} _{1}+{\frac {\overline {a_{11}^{\prime }}}{|a_{11}^{\prime }|}}\mathbf {a} _{1}^{\prime }\;\;\;,\;\;\;a_{11}^{\prime }\neq 0\\\end{cases}}$

This householder matrix will map $\mathbf {a} _{1}^{\prime }$ to $\|\mathbf {a} _{1}^{\prime }\|\mathbf {e} _{1}$ and as such, the block matrix $U_{1}={\begin{bmatrix}1&\mathbf {0} \\\mathbf {0} &V_{1}\end{bmatrix}}$ will map the matrix A to the matrix $U_{1}A$ which has only zeros below the second entry of the first column. Now construct $(n-2)\times (n-2)$ householder matrix $V_{2}$ in a similar manner as $V_{1}$ such that $V_{2}$ maps the first column of $A^{\prime \prime }$ to $\|\mathbf {a} _{1}^{\prime \prime }\|\mathbf {e} _{1}$ , where $A^{\prime \prime }$ is the submatrix of $A^{\prime }$ constructed by removing the first row and the first column of $A^{\prime }$ , then let $U_{2}={\begin{bmatrix}1&0&0\\0&1&0\\0&0&V_{2}\end{bmatrix}}$ which maps $U_{1}A$ to the matrix $U_{2}U_{1}A$ which has only zeros below the first and second entry of the subdiagonal. Now construct $V_{3}$ and then $U_{3}$ in a similar manner, but for the matrix $A^{\prime \prime \prime }$ constructed by removing the first row and first column of $A^{\prime \prime }$ and proceed as in the previous steps. Continue like this for a total of $n-2$ steps.

By construction of $U_{k}$ , the first k columns of any $n\times n$ matrix are invariant under multiplication by $U_{k}^{*}$ from the right. Hence, any matrix can be transformed to an upper Hessenberg matrix by a similarity transformation of the form $U_{(n-2)}(\dots (U_{2}(U_{1}AU_{1}^{*})U_{2}^{*})\dots )U_{(n-2)}^{*}=U_{(n-2)}\dots U_{2}U_{1}A(U_{(n-2)}\dots U_{2}U_{1})^{*}=UAU^{*}$ .

### Jacobi (Givens) rotations

A Jacobi rotation (also called Givens rotation) is an orthogonal matrix transformation in the form

$A\to A'=J(p,q,\theta )^{T}AJ(p,q,\theta )\;,$

where $J(p,q,\theta )$ , $p<q$ , is the Jacobi rotation matrix with all matrix elements equal zero except for

$\left\{{\begin{aligned}J(p,q,\theta )_{ii}&{}=1\;\forall i\neq p,q\\J(p,q,\theta )_{pp}&{}=\cos(\theta )\\J(p,q,\theta )_{qq}&{}=\cos(\theta )\\J(p,q,\theta )_{pq}&{}=\sin(\theta )\\J(p,q,\theta )_{qp}&{}=-\sin(\theta )\;.\end{aligned}}\right.$

One can zero the matrix element $A'_{p-1,q}$ by choosing the rotation angle $\theta$ to satisfy the equation

$A_{p-1,p}\sin \theta +A_{p-1,q}\cos \theta =0\;,$

Now, the sequence of such Jacobi rotations with the following $(p,q)$

$(p,q)=(2,3),(2,4),\dots ,(2,n),(3,4),\dots ,(3,n),\dots ,(n-1,n)$

reduces the matrix A to the lower Hessenberg form.

## Properties

For $n\in \{1,2\}$ , every $n\times n$ matrix is both upper Hessenberg, and lower Hessenberg.

The product of a Hessenberg matrix with a triangular matrix is again Hessenberg. More precisely, if A is upper Hessenberg and T is upper triangular, then $AT$ and $TA$ are upper Hessenberg. The Hessenberg matrix can be presented in a Jordan canonical form, with confluent Vandermonde matrix as the similarity matrix (chapter 1.4.2 of ).

A matrix that is both upper Hessenberg and lower Hessenberg is a tridiagonal matrix, of which the Jacobi matrix is an important example. This includes the symmetric or Hermitian Hessenberg matrices. A Hermitian matrix can be reduced to tri-diagonal real symmetric matrices.

## Hessenberg operator

The Hessenberg operator is an infinite dimensional Hessenberg matrix. It commonly occurs as the generalization of the Jacobi operator to a system of orthogonal polynomials for the space of square-integrable holomorphic functions over some domain—that is, a Bergman space. In this case, the Hessenberg operator is the right-shift operator S , given by $[Sf](z)=zf(z).$

The eigenvalues of each principal submatrix of the Hessenberg operator are given by the characteristic polynomial for that submatrix. These polynomials are called the Bergman polynomials, and provide an orthogonal polynomial basis for Bergman space.
