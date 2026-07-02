---
title: "Perron's formula"
source: https://en.wikipedia.org/wiki/Perron%27s_formula
domain: mellin-transform
license: CC-BY-SA-4.0
tags: mellin transform, mellin inversion theorem, dirichlet series, harmonic sum
fetched: 2026-07-02
---

# Perron's formula

In mathematics, and more particularly in analytic number theory, **Perron's formula** is a formula discovered by Oskar Perron to calculate the sum of an arithmetic function, by means of an inverse Mellin transform.

## Statement

Let $\{a(n)\}$ be an arithmetic function, and let

$g(s)=\sum _{n=1}^{\infty }{\frac {a(n)}{n^{s}}}$

be the corresponding Dirichlet series. Presume the Dirichlet series to be uniformly convergent for $\Re (s)>\sigma$ . Then Perron's formula is

$A(x)={\sum _{n\leq x}}'a(n)={\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }g(z){\frac {x^{z}}{z}}\,dz.$

Here, the prime on the summation indicates that the last term of the sum must be multiplied by 1/2 when *x* is an integer. The integral is not a convergent Lebesgue integral; it is understood as the Cauchy principal value. The formula requires that *c* > 0, *c* > σ, and *x* > 0.

## Proof

An easy sketch of the proof comes from taking Abel's sum formula

$g(s)=\sum _{n=1}^{\infty }{\frac {a(n)}{n^{s}}}=s\int _{1}^{\infty }A(x)x^{-(s+1)}dx.$

This is nothing but a Laplace transform under the variable change $x=e^{t}.$ Inverting it one gets Perron's formula.

Proofs of Perron's formula have been published by Tom M. Apostol and by Gérald Tenenbaum.

## Examples

Because of its general relationship to Dirichlet series, the formula is commonly applied to many number-theoretic sums. Thus, for example, one has the famous integral representation for the Riemann zeta function:

$\zeta (s)=s\int _{1}^{\infty }{\frac {\lfloor x\rfloor }{x^{s+1}}}\,dx$

and a similar formula for Dirichlet *L*-functions:

$L(s,\chi )=s\int _{1}^{\infty }{\frac {A(x)}{x^{s+1}}}\,dx$

where

$A(x)=\sum _{n\leq x}\chi (n)$

and $\chi (n)$ is a Dirichlet character. Other examples appear in the articles on the Mertens function and the von Mangoldt function.

## Generalizations

Perron's formula is a special case of the formula

$\sum _{n=1}^{\infty }a(n)f(n/x)={\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }F(s)G(s)x^{s}ds$

where

$G(s)=\sum _{n=1}^{\infty }{\frac {a(n)}{n^{s}}}$

and

$F(s)=\int _{0}^{\infty }f(x)x^{s-1}dx$

the Mellin transform. The Perron formula is the special case of the test function $f(1/x)=\theta (x-1),$ for $\theta (x)$ the Heaviside step function.
