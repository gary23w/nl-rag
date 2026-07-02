---
title: "Rayleigh quotient"
source: https://en.wikipedia.org/wiki/Rayleigh_quotient
domain: sturm-liouville-theory
license: CC-BY-SA-4.0
tags: sturm-liouville theory, eigenfunction expansion, oscillation theory, rayleigh quotient
fetched: 2026-07-02
---

# Rayleigh quotient

In mathematics, the **Rayleigh quotient** (/ˈreɪ.li/) for a given complex Hermitian matrix M and nonzero vector *x* is defined as: $R(M,x)={x^{*}Mx \over x^{*}x}.$ For real matrices and vectors, the condition of being Hermitian reduces to that of being symmetric, and the conjugate transpose $x^{*}$ to the usual transpose $x'$ . Note that $R(M,cx)=R(M,x)$ for any non-zero scalar *c*. Recall that a Hermitian (or real symmetric) matrix is diagonalizable with only real eigenvalues. It can be shown that, for a given matrix, the Rayleigh quotient reaches its minimum value $\lambda _{\min }$ (the smallest eigenvalue of *M*) when *x* is $v_{\min }$ (the corresponding eigenvector). Similarly, $R(M,x)\leq \lambda _{\max }$ and $R(M,v_{\max })=\lambda _{\max }$ .

The Rayleigh quotient is used in the min-max theorem to get exact values of all eigenvalues. It is also used in eigenvalue algorithms (such as Rayleigh quotient iteration) to obtain an eigenvalue approximation from an eigenvector approximation.

The range of the Rayleigh quotient (for any matrix, not necessarily Hermitian) is called a numerical range and contains its spectrum. When the matrix is Hermitian, the numerical radius is equal to the spectral norm. Still in functional analysis, $\lambda _{\max }$ is known as the spectral radius. In the context of $C^{\star }$ -algebras or algebraic quantum mechanics, the function that to *M* associates the Rayleigh–Ritz quotient $R(M,x)$ for a fixed *x* and *M* varying through the algebra would be referred to as *vector state* of the algebra.

In quantum mechanics, the Rayleigh quotient gives the expectation value of the observable corresponding to the operator *M* for a system whose state is given by *x*.

If we fix the complex matrix *M*, then the resulting Rayleigh quotient map (considered as a function of *x*) completely determines *M* via the polarization identity; indeed, this remains true even if we allow *M* to be non-Hermitian. However, if we restrict the field of scalars to the real numbers, then the Rayleigh quotient only determines the symmetric part of *M*.

## Bounds for Hermitian *M*

As stated in the introduction, for any vector *x*, one has $R(M,x)\in \left[\lambda _{\min },\lambda _{\max }\right]$ , where $\lambda _{\min },\lambda _{\max }$ are respectively the smallest and largest eigenvalues of M (This result is known as the Rayleigh–Ritz principle). This is immediate after observing that the Rayleigh quotient is a weighted average of eigenvalues of *M*: $R(M,x)={x^{*}Mx \over x^{*}x}={\frac {\sum _{i=1}^{n}\lambda _{i}y_{i}^{2}}{\sum _{i=1}^{n}y_{i}^{2}}}$ where $(\lambda _{i},v_{i})$ is the i -th eigenpair after orthonormalization and $y_{i}=v_{i}^{*}x$ is the i th coordinate of *x* in the eigenbasis. It is then easy to verify that the bounds are attained at the corresponding eigenvectors $v_{\min },v_{\max }$ .

The fact that the quotient is a weighted average of the eigenvalues can be used to identify the second, the third, ... largest eigenvalues. Let $\lambda _{\max }=\lambda _{1}\geq \lambda _{2}\geq \cdots \geq \lambda _{n}=\lambda _{\min }$ be the eigenvalues in decreasing order. If $n=2$ and x is constrained to be orthogonal to $v_{1}$ , in which case $y_{1}=v_{1}^{*}x=0$ , then $R(M,x)$ has maximum value $\lambda _{2}$ , which is achieved when $x=v_{2}$ .

## Special case of covariance matrices

An empirical covariance matrix M can be represented as the product $A'A$ of the normalized data matrix A pre-multiplied by its transpose $A'$ . Being a positive semi-definite matrix, M has non-negative eigenvalues, and orthogonal (or orthogonalisable) eigenvectors, which can be demonstrated as follows.

Firstly, that the eigenvalues $\lambda _{i}$ are non-negative: ${\begin{aligned}&Mv_{i}=A'Av_{i}=\lambda _{i}v_{i}\\\Rightarrow {}&v_{i}'A'Av_{i}=v_{i}'\lambda _{i}v_{i}\\\Rightarrow {}&\left\|Av_{i}\right\|^{2}=\lambda _{i}\left\|v_{i}\right\|^{2}\\\Rightarrow {}&\lambda _{i}={\frac {\left\|Av_{i}\right\|^{2}}{\left\|v_{i}\right\|^{2}}}\geq 0.\end{aligned}}$

Secondly, that the eigenvectors $v_{i}$ are orthogonal to one another: ${\begin{aligned}&Mv_{i}=\lambda _{i}v_{i}\\\Rightarrow {}&v_{j}'Mv_{i}=v_{j}'\lambda _{i}v_{i}\\\Rightarrow {}&\left(Mv_{j}\right)'v_{i}=\lambda _{j}v_{j}'v_{i}\\\Rightarrow {}&\lambda _{j}v_{j}'v_{i}=\lambda _{i}v_{j}'v_{i}\\\Rightarrow {}&\left(\lambda _{j}-\lambda _{i}\right)v_{j}'v_{i}=0\\\Rightarrow {}&v_{j}'v_{i}=0\end{aligned}}$ if the eigenvalues are different – in the case of multiplicity, the basis can be orthogonalized.

To now establish that the Rayleigh quotient is maximized by the eigenvector with the largest eigenvalue, consider decomposing an arbitrary vector x on the basis of the eigenvectors $v_{i}$ : $x=\sum _{i=1}^{n}\alpha _{i}v_{i},$ where $\alpha _{i}={\frac {x'v_{i}}{v_{i}'v_{i}}}={\frac {\langle x,v_{i}\rangle }{\left\|v_{i}\right\|^{2}}}$ is the coordinate of x orthogonally projected onto $v_{i}$ . Therefore, we have: ${\begin{aligned}R(M,x)&={\frac {x'A'Ax}{x'x}}\\&={\frac {{\Bigl (}\sum _{j=1}^{n}\alpha _{j}v_{j}{\Bigr )}'\left(A'A\right){\Bigl (}\sum _{i=1}^{n}\alpha _{i}v_{i}{\Bigr )}}{{\Bigl (}\sum _{j=1}^{n}\alpha _{j}v_{j}{\Bigr )}'{\Bigl (}\sum _{i=1}^{n}\alpha _{i}v_{i}{\Bigr )}}}\\&={\frac {{\Bigl (}\sum _{j=1}^{n}\alpha _{j}v_{j}{\Bigr )}'{\Bigl (}\sum _{i=1}^{n}\alpha _{i}(A'A)v_{i}{\Bigr )}}{{\Bigl (}\sum _{i=1}^{n}\alpha _{i}^{2}{v_{i}}'{v_{i}}{\Bigr )}}}\\&={\frac {{\Bigl (}\sum _{j=1}^{n}\alpha _{j}v_{j}{\Bigr )}'{\Bigl (}\sum _{i=1}^{n}\alpha _{i}\lambda _{i}v_{i}{\Bigr )}}{{\Bigl (}\sum _{i=1}^{n}\alpha _{i}^{2}\|{v_{i}}\|^{2}{\Bigr )}}}\end{aligned}}$ which, by orthonormality of the eigenvectors, becomes: ${\begin{aligned}R(M,x)&={\frac {\sum _{i=1}^{n}\alpha _{i}^{2}\lambda _{i}}{\sum _{i=1}^{n}\alpha _{i}^{2}}}\\&=\sum _{i=1}^{n}\lambda _{i}{\frac {(x'v_{i})^{2}}{(x'x)(v_{i}'v_{i})^{2}}}\\&=\sum _{i=1}^{n}\lambda _{i}{\frac {(x'v_{i})^{2}}{(x'x)}}\end{aligned}}$

The last representation establishes that the Rayleigh quotient is the sum of the squared cosines of the angles formed by the vector x and each eigenvector $v_{i}$ , weighted by corresponding eigenvalues.

If a vector x maximizes $R(M,x)$ , then any non-zero scalar multiple $kx$ also maximizes R , so the problem can be reduced to the Lagrange problem of maximizing ${\textstyle \sum _{i=1}^{n}\alpha _{i}^{2}\lambda _{i}}$ under the constraint that ${\textstyle \sum _{i=1}^{n}\alpha _{i}^{2}=1}$ .

Define: $\beta _{i}=\alpha _{i}^{2}$ . This then becomes a linear program, which always attains its maximum at one of the corners of the domain. A maximum point will have $\alpha _{1}=\pm 1$ and $\alpha _{i}=0$ for all $i>1$ (when the eigenvalues are ordered by decreasing magnitude).

Thus, the Rayleigh quotient is maximized by the eigenvector with the largest eigenvalue.

### Formulation using Lagrange multipliers

Alternatively, this result can be arrived at by the method of Lagrange multipliers. The first part is to show that the quotient is constant under scaling $x\to cx$ , where c is a scalar $R(M,cx)={\frac {(cx)^{*}Mcx}{(cx)^{*}cx}}={\frac {c^{*}c}{c^{*}c}}{\frac {x^{*}Mx}{x^{*}x}}=R(M,x).$

Because of this invariance, it is sufficient to study the special case $\|x\|^{2}=x^{T}x=1$ . The problem is then to find the critical points of the function $R(M,x)=x^{\mathsf {T}}Mx,$ subject to the constraint $\|x\|^{2}=x^{T}x=1.$ In other words, it is to find the critical points of ${\mathcal {L}}(x)=x^{\mathsf {T}}Mx-\lambda \left(x^{\mathsf {T}}x-1\right),$ where $\lambda$ is a Lagrange multiplier. The stationary points of ${\mathcal {L}}(x)$ occur at ${\begin{aligned}&{\frac {d{\mathcal {L}}(x)}{dx}}=0\\\Rightarrow {}&2x^{\mathsf {T}}M-2\lambda x^{\mathsf {T}}=0\\\Rightarrow {}&2Mx-2\lambda x=0{\text{ (taking the transpose of both sides and noting that }}M{\text{ is Hermitian)}}\\\Rightarrow {}&Mx=\lambda x\end{aligned}}$ and $\therefore R(M,x)={\frac {x^{\mathsf {T}}Mx}{x^{\mathsf {T}}x}}=\lambda {\frac {x^{\mathsf {T}}x}{x^{\mathsf {T}}x}}=\lambda .$

Therefore, the eigenvectors $x_{1},\ldots ,x_{n}$ of M are the critical points of the Rayleigh quotient and their corresponding eigenvalues $\lambda _{1},\ldots ,\lambda _{n}$ are the stationary values of ${\mathcal {L}}$ . This property is the basis for principal components analysis and canonical correlation.

## Use in Sturm–Liouville theory

Sturm–Liouville theory concerns the action of the linear operator $L(y)={\frac {1}{w(x)}}\left(-{\frac {d}{dx}}\left[p(x){\frac {dy}{dx}}\right]+q(x)y\right)$ on the inner product space defined by $\langle {y_{1},y_{2}}\rangle =\int _{a}^{b}w(x)y_{1}(x)y_{2}(x)\,dx$ of functions satisfying some specified boundary conditions at *a* and *b*. In this case the Rayleigh quotient is ${\frac {\langle {y,Ly}\rangle }{\langle {y,y}\rangle }}={\frac {\int _{a}^{b}y(x)\left(-{\frac {d}{dx}}\left[p(x){\frac {dy}{dx}}\right]+q(x)y(x)\right)dx}{\int _{a}^{b}{w(x)y(x)^{2}}dx}}.$

This is sometimes presented in an equivalent form, obtained by separating the integral in the numerator and using integration by parts: ${\begin{aligned}{\frac {\langle {y,Ly}\rangle }{\langle {y,y}\rangle }}&={\frac {\left\{\int _{a}^{b}y(x)\left(-{\frac {d}{dx}}\left[p(x)y'(x)\right]\right)dx\right\}+\left\{\int _{a}^{b}{q(x)y(x)^{2}}\,dx\right\}}{\int _{a}^{b}{w(x)y(x)^{2}}\,dx}}\\&={\frac {\left\{\left.-y(x)\left[p(x)y'(x)\right]\right|_{a}^{b}\right\}+\left\{\int _{a}^{b}y'(x)\left[p(x)y'(x)\right]\,dx\right\}+\left\{\int _{a}^{b}{q(x)y(x)^{2}}\,dx\right\}}{\int _{a}^{b}w(x)y(x)^{2}\,dx}}\\&={\frac {\left\{\left.-p(x)y(x)y'(x)\right|_{a}^{b}\right\}+\left\{\int _{a}^{b}\left[p(x)y'(x)^{2}+q(x)y(x)^{2}\right]\,dx\right\}}{\int _{a}^{b}{w(x)y(x)^{2}}\,dx}}.\end{aligned}}$

## Generalizations

1. For a given pair (*A*, *B*) of matrices, and a given non-zero vector *x*, the **generalized Rayleigh quotient** is defined as: $R(A,B;x):={\frac {x^{*}Ax}{x^{*}Bx}}.$ The generalized Rayleigh quotient can be reduced to the Rayleigh quotient $R(D,C^{*}x)$ through the transformation $D=C^{-1}A{C^{*}}^{-1}$ where $CC^{*}$ is the Cholesky decomposition of the Hermitian positive-definite matrix *B*.
2. For a given pair (*x*, *y*) of non-zero vectors, and a given Hermitian matrix *H*, the **generalized Rayleigh quotient** or sometimes **two-sided Rayleigh quotient** can be defined as: $R(H;x,y):={\frac {y^{*}Hx}{\sqrt {y^{*}y\cdot x^{*}x}}}$ or $R(H;x,y):={\frac {y^{*}Hx}{y^{*}x}}$ which both coincide with *R*(*H*,*x*) when *x* = *y*. In quantum mechanics, this quantity is called a "matrix element" or sometimes a "transition amplitude".
