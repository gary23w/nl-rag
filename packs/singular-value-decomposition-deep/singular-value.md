---
title: "Singular value"
source: https://en.wikipedia.org/wiki/Singular_value
domain: singular-value-decomposition-deep
license: CC-BY-SA-4.0
tags: singular value decomposition, moore-penrose inverse, low-rank approximation, polar decomposition
fetched: 2026-07-02
---

# Singular value

In mathematics, in particular in functional analysis, the **singular values** of a compact operator $\,T\!:X\rightarrow Y$ acting between Hilbert spaces X and Y , are the square roots of the (necessarily non-negative) eigenvalues of the self-adjoint operator $T^{*}T$ (where $T^{*}$ denotes the adjoint of ⁠ T ⁠).

The singular values are non-negative real numbers, usually listed in decreasing order ⁠ ${\big (}\sigma _{1}(T)\geq \sigma _{2}(T)\geq \dots {\big )}$ ⁠. The largest singular value $\sigma _{1}(T)$ is equal to the operator norm of T (see Min-max theorem).

If T acts on a Euclidean space ⁠ $\mathbb {R} ^{n}$ ⁠, there is a simple geometric interpretation for the singular values: Consider the image by T of the unit sphere; this is an ellipsoid, and the lengths of its semi-axes are the singular values of T (the figure provides an example in $\mathbb {R} ^{2}$ ).

The singular values are the absolute values of the eigenvalues of a normal matrix ⁠ A ⁠, because the spectral theorem can be applied to obtain unitary diagonalization of A as ⁠ $A=U\varLambda \,U^{*}$ ⁠. Therefore, ${\textstyle {\sqrt {A^{*}A}}={\sqrt {U\varLambda ^{*}\varLambda \,U^{*}}}=U\left|\varLambda \right|U^{*}}$ .

Most norms on Hilbert space operators studied are defined using singular values. For example, the Ky Fan ⁠ k ⁠-norm is the sum of first k singular values, the trace norm is the sum of all singular values, and the Schatten norm is the ⁠ p ⁠-th root of the sum of the ⁠ p ⁠-th powers of the singular values. Note that each norm is defined only on a special class of operators, hence singular values can be useful in classifying different operators.

In the finite-dimensional case, a matrix can always be decomposed in the form ⁠ $\mathbf {U\Sigma V^{*}}$ ⁠, where $\mathbf {U}$ and $\mathbf {V^{*}}$ are unitary matrices and $\mathbf {\Sigma }$ is a rectangular diagonal matrix with the singular values lying on the diagonal. This is the singular value decomposition.

## Basic properties

For $A\in \mathbb {C} ^{m\times n}$ and ⁠ $i=1,2,\ldots ,\min\{m,n\}$ ⁠:

Min-max theorem for singular values: Here, U is a subspace of ⁠ $\mathbb {C} ^{n}$ ⁠;

$\sigma _{i}(A)=\min _{\dim(U)=n-i+1}\max _{\underset {\|x\|_{2}=1}{x\in U}}\left\|Ax\right\|_{2}.$

$\sigma _{i}(A)=\max _{\dim(U)=i}\min _{\underset {\|x\|_{2}=1}{x\in U}}\left\|Ax\right\|_{2}.$

Matrix transpose and conjugate do not alter singular values:

⁠

$\sigma _{i}(A)=\sigma _{i}\!\left(A^{\textsf {T}}\right)=\sigma _{i}\!\left(A^{*}\right)$

⁠

.

For any unitary matrices $U\in \mathbb {C} ^{m\times m}$ and ⁠ $V\in \mathbb {C} ^{n\times n}$ ⁠,

⁠

$\sigma _{i}(A)=\sigma _{i}(UAV)$

⁠

.

Relation to eigenvalues:

⁠

$\sigma _{i}^{2}(A)=\lambda _{i}\!\left(AA^{*}\right)=\lambda _{i}\!\left(A^{*}A\right)$

⁠

.

Relation to trace:

⁠

$\sum _{i=1}^{n}\sigma _{i}^{2}={\text{tr}}(A^{*}A)$

⁠

.

If $A^{*}A$ has full rank, the product of singular values is ⁠ $\det {\sqrt {A^{*}A}}$ ⁠.

If $AA^{*}$ has full rank, the product of singular values is ⁠ $\det {\sqrt {AA^{*}}}$ ⁠.

If A is square and has full rank, the product of singular values is ⁠ $\vert \!\det A\vert$ ⁠.

If A is normal, then ⁠ $\sigma _{i}(A)=\vert \lambda _{i}(A)\vert$ ⁠, that is, its singular values are the absolute values of its eigenvalues.

For a generic rectangular matrix ⁠ A ⁠, let ${\textstyle {\tilde {A}}={\begin{bmatrix}0&A\\A^{*}&0\end{bmatrix}}}$ be its augmented matrix. It has eigenvalues ${\textstyle \pm \sigma _{i}(A)}$ (where the ${\textstyle \sigma _{i}(A)}$ are the singular values of ${\textstyle A}$ ) and the remaining eigenvalues are zero. Let ${\textstyle A=U\varSigma \,V^{*}}$ be the singular value decomposition, then the eigenvectors of ${\textstyle {\tilde {A}}}$ are ${\textstyle {\begin{bmatrix}\mathbf {u} _{i}\\\pm \mathbf {v} _{i}\end{bmatrix}}}$ for ⁠ $\pm \sigma _{i}$ ⁠.

## The smallest singular value

The smallest singular value of a matrix ⁠ A ⁠ is ⁠ $\sigma _{\mathrm {n} }(A)$ ⁠. For a non-singular matrix ⁠ A ⁠, it has the following properties:

- $\|A^{-1}\|_{2}=\sigma _{\mathrm {n} }^{-1}(A)$ .
- For all indices ⁠ $1\!\leq i,j\leq \!n$ ⁠, ⁠ ~ ⁠ $|A_{i,j}^{-1}|\leq \sigma _{\mathrm {n} }^{-1}(A)$ .

Intuitively, if ⁠ $\sigma _{\mathrm {n} }(A)$ ⁠ is small, then the rows of ⁠ A ⁠ are "almost" linearly dependent. If it is ⁠ $\sigma _{\mathrm {n} }(A)=0$ ⁠, then the rows of ⁠ A ⁠ are linearly dependent and ⁠ A ⁠ is not invertible.

## Inequalities about singular values

See also:

### Singular values of sub-matrices

For $A\in \mathbb {C} ^{m\times n}$ ,

1. Let B denote A with one of its rows *or* columns deleted. Then $\sigma _{i+1}(A)\leq \sigma _{i}(B)\leq \sigma _{i}(A)$
2. Let B denote A with two of its rows *and* columns deleted. Then $\sigma _{i+2}(A)\leq \sigma _{i}(B)\leq \sigma _{i}(A)$
3. Let B denote an $(m-k)\times (n-\ell )$ submatrix of A . Then $\sigma _{i+k+\ell }(A)\leq \sigma _{i}(B)\leq \sigma _{i}(A)$

### Singular values of *A* + *B*

For $A,B\in \mathbb {C} ^{m\times n}$ ,

1. $\sum _{i=1}^{k}\sigma _{i}(A+B)\leq \sum _{i=1}^{k}{\big (}\sigma _{i}(A)+\sigma _{i}(B){\big )},~{\text{where}}~k=\min\{m,n\}.$
2. $\sigma _{i+j-1}(A+B)\leq \sigma _{i}(A)+\sigma _{j}(B),\quad \forall \,i,j\in \mathbb {N} ^{*},\ i+j-1\leq \min\{m,n\}.$

### Singular values of *AB*

For $A,B\in \mathbb {C} ^{n\times n}$ ,

1. ${\begin{aligned}\prod _{i=n}^{i=n-k+1}\sigma _{i}(A)\sigma _{i}(B)&\leq \prod _{i=n}^{i=n-k+1}\sigma _{i}(AB).\\\prod _{i=1}^{k}\sigma _{i}(AB)&\leq \prod _{i=1}^{k}\sigma _{i}(A)\sigma _{i}(B).\\\sum _{i=1}^{k}\sigma _{i}^{p}(AB)&\leq \sum _{i=1}^{k}\sigma _{i}^{p}(A)\sigma _{i}^{p}(B).\end{aligned}}$
2. $\sigma _{n}(A)\sigma _{i}(B)\leq \sigma _{i}(AB)\leq \sigma _{1}(A)\sigma _{i}(B),\quad \forall i=1,2,\ldots ,n.$

For $A,B\in \mathbb {C} ^{m\times n}$ , $2\sigma _{i}(AB^{*})\leq \sigma _{i}\left(A^{*}A+B^{*}B\right),\quad \forall i=1,2,\ldots ,n.$

### Singular values and eigenvalues

For $A\in \mathbb {C} ^{n\times n}$ ,

1. See:. $\lambda _{i}\left(A+A^{*}\right)\leq 2\sigma _{i}(A),\quad \forall i=1,2,\ldots ,n.$
2. Assume $\left|\lambda _{1}(A)\right|\geq \cdots \geq \left|\lambda _{n}(A)\right|$ . Then for $k=1,2,\ldots ,n$ ,
  1. Weyl's theorem: $\prod _{i=1}^{k}\left|\lambda _{i}(A)\right|\leq \prod _{i=1}^{k}\sigma _{i}(A).$
  2. For $p>0$ , $\sum _{i=1}^{k}\left|\lambda _{i}^{p}(A)\right|\leq \sum _{i=1}^{k}\sigma _{i}^{p}(A).$

## History

This concept was introduced by Erhard Schmidt in 1907. Schmidt called singular values "eigenvalues" at that time. The name "singular value" was first quoted by Smithies in 1937. In 1957, Allahverdiev proved the following characterization of the ⁠ n ⁠-th singular number:

$\sigma _{n}(T)=\inf {\big \{}\,\|T-L\|:L{\text{ is an operator of finite rank }}<n\,{\big \}}.$

This formulation made it possible to extend the notion of singular values to operators in Banach space.

Note that there is a more general concept of *s-numbers*, which also includes Gelfand and Kolmogorov width.
