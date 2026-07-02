---
title: "Orthogonal functions"
source: https://en.wikipedia.org/wiki/Orthogonal_functions
domain: sturm-liouville-theory
license: CC-BY-SA-4.0
tags: sturm-liouville theory, eigenfunction expansion, oscillation theory, rayleigh quotient
fetched: 2026-07-02
---

# Orthogonal functions

In mathematics, **orthogonal functions** belong to a function space that is a vector space equipped with a bilinear form. When the function space has an interval as the domain, the bilinear form may be the integral of the product of functions over the interval:

$\langle f,g\rangle =\int {\overline {f(x)}}g(x)\,dx.$

The functions f and g are orthogonal when this integral is zero, i.e. $\langle f,\,g\rangle =0$ whenever $f\neq g$ . As with a basis of vectors in a finite-dimensional space, orthogonal functions can form an infinite basis for a function space. Conceptually, the above integral is the equivalent of a vector dot product; two vectors are mutually independent (orthogonal) if their dot-product is zero.

Suppose $\{f_{0},f_{1},\ldots \}$ is a sequence of orthogonal functions of nonzero *L*2-norms ${\textstyle \left\|f_{n}\right\|_{2}={\sqrt {\langle f_{n},f_{n}\rangle }}=\left(\int f_{n}^{2}\ dx\right)^{\frac {1}{2}}}$ . It follows that the sequence $\left\{f_{n}/\left\|f_{n}\right\|_{2}\right\}$ is of functions of *L*2-norm one, forming an orthonormal sequence. To have a defined *L*2-norm, the integral must be bounded, which restricts the functions to being square-integrable.

## Trigonometric functions

Several sets of orthogonal functions have become standard bases for approximating functions. For example, the sine functions sin *nx* and sin *mx* are orthogonal on the interval $x\in (-\pi ,\pi )$ when $m\neq n$ and *n* and *m* are positive integers. For then

$2\sin \left(mx\right)\sin \left(nx\right)=\cos \left(\left(m-n\right)x\right)-\cos \left(\left(m+n\right)x\right),$

and the integral of the product of the two sine functions vanishes. Together with cosine functions, these orthogonal functions may be assembled into a trigonometric polynomial to approximate a given function on the interval with its Fourier series.

## Polynomials

If one begins with the monomial sequence $\left\{1,x,x^{2},\dots \right\}$ on the interval $[-1,1]$ and applies the Gram–Schmidt process, then one obtains the Legendre polynomials. Another collection of orthogonal polynomials are the associated Legendre polynomials.

The study of orthogonal polynomials involves weight functions $w(x)$ that are inserted in the bilinear form:

$\langle f,g\rangle =\int w(x)f(x)g(x)\,dx.$

For Laguerre polynomials on $(0,\infty )$ the weight function is $w(x)=e^{-x}$ .

Both physicists and probability theorists use Hermite polynomials on $(-\infty ,\infty )$ , where the weight function is $w(x)=e^{-x^{2}}$ or $w(x)=e^{-x^{2}/2}$ .

Chebyshev polynomials are defined on $[-1,1]$ and use weights ${\textstyle w(x)={\frac {1}{\sqrt {1-x^{2}}}}}$ or ${\textstyle w(x)={\sqrt {1-x^{2}}}}$ .

Zernike polynomials are defined on the unit disk and have orthogonality of both radial and angular parts.

## Binary-valued functions

Walsh functions and Haar wavelets are examples of orthogonal functions with discrete ranges.

## Rational functions

Legendre and Chebyshev polynomials provide orthogonal families for the interval [−1, 1] while occasionally orthogonal families are required on [0, ∞). In this case it is convenient to apply the Cayley transform first, to bring the argument into [−1, 1]. This procedure results in families of rational orthogonal functions called Legendre rational functions and Chebyshev rational functions.

## In differential equations

Solutions of linear differential equations with boundary conditions can often be written as a weighted sum of orthogonal solution functions (a.k.a. eigenfunctions), leading to generalized Fourier series.
