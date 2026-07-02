---
title: "Discrete Fourier transform over a ring"
source: https://en.wikipedia.org/wiki/Number-theoretic_transform
domain: fft-algorithm
license: CC-BY-SA-4.0
tags: fast fourier transform, cooley tukey algorithm, discrete fourier transform, convolution theorem
fetched: 2026-07-02
---

# Discrete Fourier transform over a ring

(Redirected from

Number-theoretic transform

)

In mathematics, the **discrete Fourier transform over a ring** generalizes the discrete Fourier transform (DFT), of a function whose values are commonly complex numbers, over an arbitrary ring.

## Definition

Let R be any ring, let $n\geq 1$ be an integer, and let $\alpha \in R$ be a principal *n*th root of unity, defined by:

| ${\begin{aligned}&\alpha ^{n}=1\\&\sum _{j=0}^{n-1}\alpha ^{jk}=0{\text{ for }}1\leq k<n\end{aligned}}$ |   | 1 |
|---|---|---|

The discrete Fourier transform maps an *n*-tuple $(v_{0},\ldots ,v_{n-1})$ of elements of R to another *n*-tuple $(f_{0},\ldots ,f_{n-1})$ of elements of R according to the following formula:

| $f_{k}=\sum _{j=0}^{n-1}v_{j}\alpha ^{jk}.$ |   | 2 |
|---|---|---|

By convention, the tuple $(v_{0},\ldots ,v_{n-1})$ is said to be in the *time domain* and the index j is called *time*. The tuple $(f_{0},\ldots ,f_{n-1})$ is said to be in the *frequency domain* and the index k is called *frequency*. The tuple $(f_{0},\ldots ,f_{n-1})$ is also called the *spectrum* of $(v_{0},\ldots ,v_{n-1})$ . This terminology derives from the applications of Fourier transforms in signal processing.

If R is an integral domain (which includes fields), it is sufficient to choose $\alpha$ as a primitive *n*th root of unity, which replaces the condition (**1**) by:

$\alpha ^{k}\neq 1$

for

$1\leq k<n$

Proof

Take $\beta =\alpha ^{k}$ with $1\leq k<n$ . Since $\alpha ^{n}=1$ , $\beta ^{n}=(\alpha ^{n})^{k}=1$ , giving:

$\beta ^{n}-1=(\beta -1)\left(\sum _{j=0}^{n-1}\beta ^{j}\right)=0$

where the sum matches (**1**). Since $\alpha$ is a primitive root of unity, $\beta -1\neq 0$ . Since R is an integral domain, the sum must be zero. ∎

Another simple condition applies in the case where *n* is a power of two: (**1**) may be replaced by $\alpha ^{n/2}=-1$ .

## Inverse

The inverse of the discrete Fourier transform is given as:

| $v_{j}={\frac {1}{n}}\sum _{k=0}^{n-1}f_{k}\alpha ^{-jk}.$ |   | 3 |
|---|---|---|

where $1/n$ is the multiplicative inverse of n in R (if this inverse does not exist, the DFT cannot be inverted).

Proof

Substituting (**2**) into the right-hand-side of (**3**), we get

${\begin{aligned}&{\frac {1}{n}}\sum _{k=0}^{n-1}f_{k}\alpha ^{-jk}\\={}&{\frac {1}{n}}\sum _{k=0}^{n-1}\sum _{j'=0}^{n-1}v_{j'}\alpha ^{j'k}\alpha ^{-jk}\\={}&{\frac {1}{n}}\sum _{j'=0}^{n-1}v_{j'}\sum _{k=0}^{n-1}\alpha ^{(j'-j)k}.\end{aligned}}$

This is exactly equal to $v_{j}$ , because $\sum _{k=0}^{n-1}\alpha ^{(j'-j)k}=0$ when $j'\neq j$ (by (**1**) with $k=j'-j$ ), and $\sum _{k=0}^{n-1}\alpha ^{(j'-j)k}=n$ when $j'=j$ . ∎

## Matrix formulation

Since the discrete Fourier transform is a linear operator, it can be described by matrix multiplication. In matrix notation, the discrete Fourier transform is expressed as follows:

${\begin{bmatrix}f_{0}\\f_{1}\\\vdots \\f_{n-1}\end{bmatrix}}={\begin{bmatrix}1&1&1&\cdots &1\\1&\alpha &\alpha ^{2}&\cdots &\alpha ^{n-1}\\1&\alpha ^{2}&\alpha ^{4}&\cdots &\alpha ^{2(n-1)}\\\vdots &\vdots &\vdots &\ddots &\vdots \\1&\alpha ^{n-1}&\alpha ^{2(n-1)}&\cdots &\alpha ^{(n-1)(n-1)}\\\end{bmatrix}}{\begin{bmatrix}v_{0}\\v_{1}\\\vdots \\v_{n-1}\end{bmatrix}}.$

The matrix for this transformation is called the DFT matrix.

Similarly, the matrix notation for the inverse Fourier transform is

${\begin{bmatrix}v_{0}\\v_{1}\\\vdots \\v_{n-1}\end{bmatrix}}={\frac {1}{n}}{\begin{bmatrix}1&1&1&\cdots &1\\1&\alpha ^{-1}&\alpha ^{-2}&\cdots &\alpha ^{-(n-1)}\\1&\alpha ^{-2}&\alpha ^{-4}&\cdots &\alpha ^{-2(n-1)}\\\vdots &\vdots &\vdots &\ddots &\vdots \\1&\alpha ^{-(n-1)}&\alpha ^{-2(n-1)}&\cdots &\alpha ^{-(n-1)(n-1)}\end{bmatrix}}{\begin{bmatrix}f_{0}\\f_{1}\\\vdots \\f_{n-1}\end{bmatrix}}.$

## Polynomial formulation

Sometimes it is convenient to identify an n-tuple $(v_{0},\ldots ,v_{n-1})$ with a formal polynomial

$p_{v}(x)=v_{0}+v_{1}x+v_{2}x^{2}+\cdots +v_{n-1}x^{n-1}.\,$

By writing out the summation in the definition of the discrete Fourier transform (**2**), we obtain:

$f_{k}=v_{0}+v_{1}\alpha ^{k}+v_{2}\alpha ^{2k}+\cdots +v_{n-1}\alpha ^{(n-1)k}.\,$

This means that $f_{k}$ is just the value of the polynomial $p_{v}(x)$ for $x=\alpha ^{k}$ , i.e.,

| $f_{k}=p_{v}(\alpha ^{k}).\,$ |   | 4 |
|---|---|---|

The Fourier transform can therefore be seen to relate the *coefficients* and the *values* of a polynomial: the coefficients are in the time-domain, and the values are in the frequency domain. Here, of course, it is important that the polynomial is evaluated at the nth roots of unity, which are exactly the powers of $\alpha$ .

Similarly, the definition of the inverse Fourier transform (**3**) can be written:

| $v_{j}={\frac {1}{n}}(f_{0}+f_{1}\alpha ^{-j}+f_{2}\alpha ^{-2j}+\cdots +f_{n-1}\alpha ^{-(n-1)j}).$ |   | 5 |
|---|---|---|

With

$p_{f}(x)=f_{0}+f_{1}x+f_{2}x^{2}+\cdots +f_{n-1}x^{n-1},$

this means that

$v_{j}={\frac {1}{n}}p_{f}(\alpha ^{-j}).$

We can summarize this as follows: if the *values* of $p_{v}(x)$ are the *coefficients* of $p_{f}(x)$ , then the *values* of $p_{f}(x)$ are the *coefficients* of $p_{v}(x)$ , up to a scalar factor and reordering.

## Special cases

### Complex numbers

If $F={\mathbb {C} }$ is the field of complex numbers, then the n th roots of unity can be visualized as points on the unit circle of the complex plane. In this case, one usually takes

$\alpha =e^{\frac {-2\pi i}{n}},$

which yields the usual formula for the complex discrete Fourier transform:

$f_{k}=\sum _{j=0}^{n-1}v_{j}e^{{\frac {-2\pi i}{n}}jk}.$

Over the complex numbers, it is often customary to normalize the formulas for the DFT and inverse DFT by using the scalar factor ${\frac {1}{\sqrt {n}}}$ in both formulas, rather than 1 in the formula for the DFT and ${\frac {1}{n}}$ in the formula for the inverse DFT. With this normalization, the DFT matrix is then unitary. Note that ${\sqrt {n}}$ does not make sense in an arbitrary field.

### Finite fields

If $F=\mathrm {GF} (q)$ is a finite field, where q is a prime power, then the existence of a primitive nth root automatically implies that n divides $q-1$ , because the multiplicative order of each element must divide the size of the multiplicative group of F, which is $q-1$ . This in particular ensures that $n=\underbrace {1+1+\cdots +1} _{n\ {\rm {times}}}$ is invertible, so that the notation ${\frac {1}{n}}$ in (**3**) makes sense.

An application of the discrete Fourier transform over $\mathrm {GF} (q)$ is the reduction of Reed–Solomon codes to BCH codes in coding theory. Such transform can be carried out efficiently with proper fast algorithms, for example, cyclotomic fast Fourier transform.

#### Polynomial formulation without nth root

Suppose $F=\mathrm {GF} (p)$ . If $p\nmid n$ , it may be the case that $n\nmid p-1$ . This means we cannot find an $n^{th}$ root of unity in F . We may view the Fourier transform as an isomorphism $\mathrm {F} [C_{n}]=\mathrm {F} [x]/(x^{n}-1)\cong \bigoplus _{i}\mathrm {F} [x]/(P_{i}(x))$ for some polynomials $P_{i}(x)$ , in accordance with Maschke's theorem. The map is given by the Chinese remainder theorem, and the inverse is given by applying Bézout's identity for polynomials.

$x^{n}-1=\prod _{d|n}\Phi _{d}(x)$ , a product of cyclotomic polynomials. Factoring $\Phi _{d}(x)$ in $F[x]$ is equivalent to factoring the prime ideal $(p)$ in $\mathrm {Z} [\zeta ]=\mathrm {Z} [x]/(\Phi _{d}(x))$ . We obtain g polynomials $P_{1}\ldots P_{g}$ of degree f where $fg=\varphi (d)$ and f is the order of $p{\text{ mod }}d$ .

As above, we may extend the base field to $\mathrm {GF} (q)$ in order to find a primitive root, i.e. a splitting field for $x^{n}-1$ . Now $x^{n}-1=\prod _{k}(x-\alpha ^{k})$ , so an element $\sum _{j=0}^{n-1}v_{j}x^{j}\in F[x]/(x^{n}-1)$ maps to $\sum _{j=0}^{n-1}v_{j}x^{j}\mod (x-\alpha ^{k})\equiv \sum _{j=0}^{n-1}v_{j}(\alpha ^{k})^{j}$ for each k .

#### When p divides n

When $p|n$ , we may still define an $F_{p}$ -linear isomorphism as above. Note that $(x^{n}-1)=(x^{m}-1)^{p^{s}}$ where $n=mp^{s}$ and $p\nmid m$ . We apply the above factorization to $x^{m}-1$ , and now obtain the decomposition $F[x]/(x^{n}-1)\cong \bigoplus _{i}F[x]/(P_{i}(x)^{p^{s}})$ . The modules occurring are now indecomposable rather than irreducible.

#### Order of the DFT matrix

Suppose $p\nmid n$ so we have an $n^{th}$ root of unity $\alpha$ . Let A be the above DFT matrix, a Vandermonde matrix with entries $A_{ij}=\alpha ^{ij}$ for $0\leq i,j<n$ . Recall that $\sum _{j=0}^{n-1}\alpha ^{(k-l)j}=n\delta _{k,l}$ since if $k=l$ , then every entry is 1. If $k\neq l$ , then we have a geometric series with common ratio $\alpha ^{k-l}$ , so we obtain ${\frac {1-\alpha ^{n(k-l)}}{1-\alpha ^{k-l}}}$ . Since $\alpha ^{n}=1$ the numerator is zero, but $k-l\neq 0$ so the denominator is nonzero.

First computing the square, $(A^{2})_{ik}=\sum _{j=0}^{n-1}\alpha ^{j(i+k)}=n\delta _{i,-k}$ . Computing $A^{4}=(A^{2})^{2}$ similarly and simplifying the deltas, we obtain $(A^{4})_{ik}=n^{2}\delta _{i,k}$ . Thus, $A^{4}=n^{2}I_{n}$ and the order is $4\cdot {\text{ord}}(n^{2})$ .

#### Normalizing the DFT matrix

In order to align with the complex case and ensure the matrix is order 4 exactly, we can normalize the above DFT matrix A with ${\frac {1}{\sqrt {n}}}$ . Note that though ${\sqrt {n}}$ may not exist in the splitting field $F_{q}$ of $x^{n}-1$ , we may form a quadratic extension $F_{q^{2}}\cong F_{q}[x]/(x^{2}-n)$ in which the square root exists. We may then set $U={\frac {1}{\sqrt {n}}}A$ , and $U^{4}=I_{n}$ .

#### Unitarity

Suppose $p\nmid n$ . One can ask whether the DFT matrix is unitary over a finite field. If the matrix entries are over $F_{q}$ , then one must ensure q is a perfect square or extend to $F_{q^{2}}$ in order to define the order two automorphism $x\mapsto x^{q}$ . Consider the above DFT matrix $A_{ij}=\alpha ^{ij}$ . Note that A is symmetric. Conjugating and transposing, we obtain $A_{ij}^{*}=\alpha ^{qji}$ .

$(AA^{*})_{ik}=\sum _{j=0}^{n-1}\alpha ^{j(i+qk)}=n\delta _{i,-qk}$

by a similar geometric series argument as above. We may remove the n by normalizing so that $U={\frac {1}{\sqrt {n}}}A$ and $(UU^{*})_{ik}=\delta _{i,-qk}$ . Thus U is unitary iff $q\equiv -1\,({\text{mod}}\,n)$ . Recall that since we have an $n^{th}$ root of unity, $n|q^{2}-1$ . This means that $q^{2}-1\equiv (q+1)(q-1)\equiv 0\,({\text{mod}}\,n)$ . Note if q was not a perfect square to begin with, then $n|q-1$ and so $q\equiv 1\,({\text{mod}}\,n)$ .

For example, when $p=3,n=5$ we need to extend to $q^{2}=3^{4}$ to get a 5th root of unity. $q=9\equiv -1\,({\text{mod}}\,5)$ .

For a nonexample, when $p=3,n=8$ we extend to $F_{3^{2}}$ to get an 8th root of unity. $q^{2}=9$ , so $q\equiv 3\,({\text{mod}}\,8)$ , and in this case $q+1\not \equiv 0$ and $q-1\not \equiv 0$ . $UU^{*}$ is a square root of the identity, so U is not unitary.

#### Eigenvalues of the DFT matrix

When $p\nmid n$ , we have an $n^{th}$ root of unity $\alpha$ in the splitting field $F_{q}\cong F_{p}[x]/(x^{n}-1)$ . Note that the characteristic polynomial of the above DFT matrix may not split over $F_{q}$ . The DFT matrix is order 4. We may need to go to a further extension $F_{q'}$ , the splitting extension of the characteristic polynomial of the DFT matrix, which at least contains fourth roots of unity. If a is a generator of the multiplicative group of $F_{q'}$ , then the eigenvalues are $\{\pm 1,\pm a^{(q'-1)/4}\}$ , in exact analogy with the complex case. They occur with some nonnegative multiplicity.

### Number-theoretic transform

The **number-theoretic transform (NTT)** is obtained by specializing the discrete Fourier transform to $F={\mathbb {Z} }/p$ , the integers modulo a prime p. This is a finite field, and primitive nth roots of unity exist whenever n divides $p-1$ , so we have $p=\xi n+1$ for a positive integer ξ. Specifically, let $\omega$ be a primitive $(p-1)$ th root of unity, then an nth root of unity $\alpha$ can be found by letting $\alpha =\omega ^{\xi }$ .

e.g. for $p=5$ , $\alpha =2$

${\begin{aligned}2^{1}&=2{\pmod {5}}\\2^{2}&=4{\pmod {5}}\\2^{3}&=3{\pmod {5}}\\2^{4}&=1{\pmod {5}}\end{aligned}}$

when $N=4$

${\begin{bmatrix}F(0)\\F(1)\\F(2)\\F(3)\end{bmatrix}}={\begin{bmatrix}1&1&1&1\\1&2&4&3\\1&4&1&4\\1&3&4&2\end{bmatrix}}{\begin{bmatrix}f(0)\\f(1)\\f(2)\\f(3)\end{bmatrix}}$

The number theoretic transform may be meaningful in the ring $\mathbb {Z} /m$ , even when the modulus m is not prime, provided a principal root of order n exists. Special cases of the number theoretic transform such as the Fermat Number Transform (*m* = 2*k*+1), used by the Schönhage–Strassen algorithm, or Mersenne Number Transform (*m* = 2*k* − 1) use a composite modulus.

In general, if ${\textstyle m=\prod _{i}p_{i}^{e_{i}}}$ , then one may find an ${\textstyle n^{th}}$ root of unity mod m by finding primitive ${\textstyle n^{th}}$ roots of unity $g_{i}$ mod ${\textstyle p_{i}^{e_{i}}}$ , yielding a tuple ${\textstyle g=\left(g_{i}\right)_{i}\in \prod _{i}\left(\mathbb {Z} /p_{i}^{e_{i}}\mathbb {Z} \right)^{\ast }}$ . The preimage of g under the Chinese remainder theorem isomorphism is an ${\textstyle n^{th}}$ root of unity ${\textstyle \alpha }$ such that ${\textstyle \alpha ^{n/2}=-1\mod m}$ . This ensures that the above summation conditions are satisfied. We must have that ${\textstyle n|\varphi (p_{i}^{e_{i}})}$ for each i , where $\varphi$ is the Euler's totient function.

Fast Fourier transform can be adapted to NTT and implemented with only integer operations. Some choices of *m* such as the Solinas prime $2^{64}-2^{32}+1$ are even easier to calculate on computers as they require no division operation for reduction.

### Discrete weighted transform

The **discrete weighted transform (DWT)** is a variation on the discrete Fourier transform over arbitrary rings involving weighting the input before transforming it by multiplying elementwise by a weight vector, then weighting the result by another vector. The Irrational base discrete weighted transform is a special case of this.

## Properties

Most of the important attributes of the complex DFT, including the inverse transform, the convolution theorem, and most fast Fourier transform (FFT) algorithms, depend only on the property that the kernel of the transform is a principal root of unity. These properties also hold, with identical proofs, over arbitrary rings. In the case of fields, this analogy can be formalized by the field with one element, considering any field with a primitive *n*th root of unity as an algebra over the extension field $\mathbf {F} _{1^{n}}.$

In particular, the applicability of $O(n\log n)$ fast Fourier transform algorithms to compute the NTT, combined with the convolution theorem, mean that the number-theoretic transform gives an efficient way to compute exact convolutions of integer sequences. While the complex DFT can perform the same task, it is susceptible to round-off error in finite-precision floating point arithmetic; the NTT has no round-off because it deals purely with fixed-size integers that can be exactly represented.

## Fast algorithms

For the implementation of a "fast" algorithm (similar to how FFT computes the DFT), it is often desirable that the transform length is also highly composite, e.g., a power of two. However, there are specialized fast Fourier transform algorithms for finite fields, such as Wang and Zhu's algorithm, that are efficient regardless of the transform length factors.
