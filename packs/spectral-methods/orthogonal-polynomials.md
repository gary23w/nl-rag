---
title: "Orthogonal polynomials"
source: https://en.wikipedia.org/wiki/Orthogonal_polynomials
domain: spectral-methods
license: CC-BY-SA-4.0
tags: spectral method, pseudo-spectral method, chebyshev polynomials, collocation method
fetched: 2026-07-02
---

# Orthogonal polynomials

In mathematics, an **orthogonal polynomial sequence** is a family of polynomials such that any two different polynomials in the sequence are orthogonal to each other under some inner product.

The most widely used orthogonal polynomials are the classical orthogonal polynomials, consisting of the Hermite polynomials, the Laguerre polynomials and the Jacobi polynomials. The Gegenbauer polynomials form the most important class of Jacobi polynomials; they include the Chebyshev polynomials and the Legendre polynomials as special cases. These are frequently given by the Rodrigues' formula.

The field of orthogonal polynomials developed in the late 19th century from a study of continued fractions by P. L. Chebyshev and was pursued by A. A. Markov and T. J. Stieltjes. They appear in a wide variety of fields: numerical analysis (quadrature rules), probability theory, representation theory (of Lie groups, quantum groups, and related objects), enumerative combinatorics, algebraic combinatorics, mathematical physics (the theory of random matrices, integrable systems, etc.), and number theory. Some of the mathematicians who have worked on orthogonal polynomials include Gábor Szegő, Sergei Bernstein, Naum Akhiezer, Arthur Erdélyi, Yakov Geronimus, Wolfgang Hahn, Theodore Seio Chihara, Mourad Ismail, Waleed Al-Salam, Richard Askey, and Rehuel Lobatto.

## Definition for 1-variable case for a real measure

Given any non-decreasing function *α* on the real numbers, we can define the Lebesgue–Stieltjes integral $\int f(x)\,d\alpha (x)$ of a function *f*. If this integral is finite for all polynomials *f*, we can define an inner product on pairs of polynomials *f* and *g* by $\langle f,g\rangle =\int f(x)g(x)\,d\alpha (x).$

This operation is a positive semidefinite inner product on the vector space of all polynomials, and is positive definite if the function α has an infinite number of points of growth. It induces a notion of orthogonality in the usual way, namely that two polynomials are orthogonal if their inner product is zero.

Then the sequence (*P**n*)∞ *n*=0 of orthogonal polynomials is defined by the relations $\deg P_{n}=n~,\quad \langle P_{m},\,P_{n}\rangle =0\quad {\text{for}}\quad m\neq n~.$

In other words, the sequence is obtained from the sequence of monomials 1, *x*, *x*2, … by the Gram–Schmidt process with respect to this inner product.

Usually the sequence is required to be orthonormal, namely, $\langle P_{n},P_{n}\rangle =1,$ however, other normalisations are sometimes used.

### Absolutely continuous case

Sometimes we have $d\alpha (x)=W(x)\,dx$ where $W:[x_{1},x_{2}]\to \mathbb {R}$ is a non-negative function with support on some interval [*x*1, *x*2] in the real line (where *x*1 = −∞ and *x*2 = ∞ are allowed). Such a *W* is called a **weight function**. Then the inner product is given by $\langle f,g\rangle =\int _{x_{1}}^{x_{2}}f(x)g(x)W(x)\,dx.$ However, there are many examples of orthogonal polynomials where the measure *dα*(*x*) has points with non-zero measure where the function *α* is discontinuous, so cannot be given by a weight function *W* as above.

## Examples of orthogonal polynomials

The most commonly used orthogonal polynomials are orthogonal for a measure with support in a real interval. This includes:

- The classical orthogonal polynomials (Jacobi polynomials, Laguerre polynomials, Hermite polynomials, and their special cases Gegenbauer polynomials, Chebyshev polynomials and Legendre polynomials).
- The Wilson polynomials, which generalize the Jacobi polynomials. They include many orthogonal polynomials as special cases, such as the Meixner–Pollaczek polynomials, the continuous Hahn polynomials, the continuous dual Hahn polynomials, and the classical polynomials, described by the Askey scheme
- The Askey–Wilson polynomials introduce an extra parameter *q* into the Wilson polynomials.

Discrete orthogonal polynomials are orthogonal with respect to some discrete measure. Sometimes the measure has finite support, in which case the family of orthogonal polynomials is finite, rather than an infinite sequence. The Racah polynomials are examples of discrete orthogonal polynomials, and include as special cases the Hahn polynomials and dual Hahn polynomials, which in turn include as special cases the Meixner polynomials, Krawtchouk polynomials, and Charlier polynomials.

Meixner classified all the orthogonal Sheffer sequences: there are only Hermite, Laguerre, Charlier, Meixner, and Meixner–Pollaczek. In some sense Krawtchouk should be on this list too, but they are a finite sequence. These six families correspond to the NEF-QVFs and are martingale polynomials for certain Lévy processes.

Sieved orthogonal polynomials, such as the sieved ultraspherical polynomials, sieved Jacobi polynomials, and sieved Pollaczek polynomials, have modified recurrence relations.

One can also consider orthogonal polynomials for some curve in the complex plane. The most important case (other than real intervals) is when the curve is the unit circle, giving orthogonal polynomials on the unit circle, such as the Rogers–Szegő polynomials.

There are some families of orthogonal polynomials that are orthogonal on plane regions such as triangles or disks. They can sometimes be written in terms of Jacobi polynomials. For example, Zernike polynomials are orthogonal on the unit disk.

The advantage of orthogonality between different orders of Hermite polynomials is applied to Generalized frequency division multiplexing (GFDM) structure. More than one symbol can be carried in each grid of time-frequency lattice.

## Properties

Orthogonal polynomials of one variable defined by a non-negative measure on the real line have the following properties.

### Relation to moments

The orthogonal polynomials *P**n* can be expressed in terms of the moments

$m_{n}=\int x^{n}\,d\alpha (x)$

as follows:

$P_{n}(x)=c_{n}\,\det {\begin{bmatrix}m_{0}&m_{1}&m_{2}&\cdots &m_{n}\\m_{1}&m_{2}&m_{3}&\cdots &m_{n+1}\\\vdots &\vdots &\vdots &\ddots &\vdots \\m_{n-1}&m_{n}&m_{n+1}&\cdots &m_{2n-1}\\1&x&x^{2}&\cdots &x^{n}\end{bmatrix}}~,$

where the constants *c**n* are arbitrary (depend on the normalization of *P**n*).

This comes directly from applying the Gram–Schmidt process to the monomials, imposing each polynomial to be orthogonal with respect to the previous ones. For example, orthogonality with $P_{0}$ prescribes that $P_{1}$ must have the form $P_{1}(x)=c_{1}\left(x-{\frac {\langle P_{0},x\rangle P_{0}}{\langle P_{0},P_{0}\rangle }}\right)=c_{1}(x-m_{1}),$ which can be seen to be consistent with the previously given expression with the determinant.

### Recurrence relation

The polynomials *P**n* satisfy a three-term recurrence relation of the form

$P_{n}(x)=(A_{n}x+B_{n})P_{n-1}(x)+C_{n}P_{n-2}(x)$

where *An* is not 0. The converse is also true; see Favard's theorem. These recurrence relations are key for deriving properties of orthogonal polynomials.

### Christoffel–Darboux formula

### Zeros

If the measure d*α* is supported on an interval [*a*, *b*], all the zeros of *P**n* lie in [*a*, *b*]. Moreover, the zeros have the following interlacing property: if *m* < *n*, there is a zero of *P**n* between any two zeros of *P**m*.

### Combinatorial interpretation

From the 1980s, with the work of X. G. Viennot, J. Labelle, Y.-N. Yeh, D. Foata, and others, combinatorial interpretations were found for all the classical orthogonal polynomials.

## Other types of orthogonal polynomials

### Multivariate orthogonal polynomials

The Macdonald polynomials are orthogonal polynomials in several variables, depending on the choice of an affine root system. They include many other families of multivariable orthogonal polynomials as special cases, including the Jack polynomials, the Hall–Littlewood polynomials, the Heckman–Opdam polynomials, and the Koornwinder polynomials. The Askey–Wilson polynomials are the special case of Macdonald polynomials for a certain non-reduced root system of rank 1.

### Multiple orthogonal polynomials

Multiple orthogonal polynomials are polynomials in one variable that are orthogonal with respect to a finite family of measures.

### Sobolev orthogonal polynomials

These are orthogonal polynomials with respect to a Sobolev inner product, i.e. an inner product with derivatives. Including derivatives has big consequences for the polynomials, in general they no longer share some of the nice features of the classical orthogonal polynomials.

### Orthogonal polynomials with matrices

Orthogonal polynomials with matrices have either coefficients that are matrices or the indeterminate is a matrix.

There are two popular examples: either the coefficients $\{a_{i}\}$ are matrices or x :

- Variante 1: $P(x)=A_{n}x^{n}+A_{n-1}x^{n-1}+\cdots +A_{1}x+A_{0}$ , where $\{A_{i}\}$ are $p\times p$ matrices.
- Variante 2: $P(X)=a_{n}X^{n}+a_{n-1}X^{n-1}+\cdots +a_{1}X+a_{0}I_{p}$ where X is a $p\times p$ -matrix and $I_{p}$ is the identity matrix.

### Quantum polynomials

Quantum polynomials or q-polynomials are the q-analogs of orthogonal polynomials.

### Skew-orthogonal polynomials

Orthogonal polynomials can be defined as a vector basis set $P_{0},P_{1},P_{2},\dots$ of a symmetric bilinear form B on polynomials. In the basis of the orthogonal polynomials, the bilinear form diagonalizes as $B(P_{i},P_{j})=B(P_{i},P_{i})\delta _{ij}$ . Similarly, given a nondegenerate skew-symmetric bilinear form on polynomials, we can find a pair of vector basis sets $P_{0},P_{1},P_{2},\dots$ and $Q_{0},Q_{1},Q_{2},\dots$ , such that the bilinear form skew-diagonalizes as $B(P_{i},Q_{j})=B(P_{i},Q_{i})\delta _{ij}$ .
