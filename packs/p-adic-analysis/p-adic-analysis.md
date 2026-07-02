---
title: "p-adic analysis"
source: https://en.wikipedia.org/wiki/P-adic_analysis
domain: p-adic-analysis
license: CC-BY-SA-4.0
tags: p-adic analysis, p-adic number, hensel's lemma, local field
fetched: 2026-07-02
---

# *p*-adic analysis

In mathematics, ***p*-adic analysis** is a branch of number theory that studies functions of *p*-adic numbers. Along with the more classical fields of real and complex analysis, which deal, respectively, with functions on the real and complex numbers, it belongs to the discipline of mathematical analysis.

The theory of complex-valued numerical functions on the *p*-adic numbers is part of the theory of locally compact groups (abstract harmonic analysis). The usual meaning taken for *p*-adic analysis is the theory of *p*-adic-valued functions on spaces of interest.

Applications of *p*-adic analysis have mainly been in number theory, where it has a significant role in diophantine geometry and diophantine approximation. Some applications have required the development of *p*-adic functional analysis and spectral theory. In many ways *p*-adic analysis is less subtle than classical analysis, since the ultrametric inequality means, for example, that convergence of infinite series of *p*-adic numbers is much simpler. Topological vector spaces over *p*-adic fields show distinctive features; for example aspects relating to convexity and the Hahn–Banach theorem are different.

## Important results

### Ostrowski's theorem

Ostrowski's theorem, due to Alexander Ostrowski (1916), states that every non-trivial absolute value on the rational numbers **Q** is equivalent to either the usual real absolute value or a p-adic absolute value.

### Mahler's theorem

**Mahler's theorem**, introduced by Kurt Mahler, expresses continuous *p*-adic functions in terms of polynomials.

In any field of characteristic 0, one has the following result. Let

$(\Delta f)(x)=f(x+1)-f(x)$

be the forward difference operator. Then for polynomial functions *f* we have the Newton series:

$f(x)=\sum _{k=0}^{\infty }(\Delta ^{k}f)(0){x \choose k},$

where

${x \choose k}={\frac {x(x-1)(x-2)\cdots (x-k+1)}{k!}}$

is the *k*th binomial coefficient polynomial.

Over the field of real numbers, the assumption that the function *f* is a polynomial can be weakened, but it cannot be weakened all the way down to mere continuity.

Mahler proved the following result:

**Mahler's theorem**: If *f* is a continuous *p*-adic-valued function on the *p*-adic integers then the same identity holds.

### Hensel's lemma

Hensel's lemma, also known as Hensel's lifting lemma, named after Kurt Hensel, is a result in modular arithmetic, stating that if a polynomial equation has a simple root modulo a prime number *p*, then this root corresponds to a unique root of the same equation modulo any higher power of *p*, which can be found by iteratively "lifting" the solution modulo successive powers of *p*. More generally it is used as a generic name for analogues for complete commutative rings (including *p*-adic fields in particular) of the Newton method for solving equations. Since *p*-adic analysis is in some ways simpler than real analysis, there are relatively easy criteria guaranteeing a root of a polynomial.

To state the result, let $f(x)$ be a polynomial with integer (or *p*-adic integer) coefficients, and let *m*,*k* be positive integers such that *m* ≤ *k*. If *r* is an integer such that

$f(r)\equiv 0{\pmod {p^{k}}}$

and

$f'(r)\not \equiv 0{\pmod {p}}$

then there exists an integer *s* such that

$f(s)\equiv 0{\pmod {p^{k+m}}}$

and

$r\equiv s{\pmod {p^{k}}}.$

Furthermore, this *s* is unique modulo *p**k*+m, and can be computed explicitly as

$s=r+tp^{k}$

where

$t=-{\frac {f(r)}{p^{k}}}\cdot (f'(r)^{-1}).$

## Applications

### Local–global principle

Helmut Hasse's local–global principle, also known as the Hasse principle, is the idea that one can find an integer solution to an equation by using the Chinese remainder theorem to piece together solutions modulo powers of each different prime number. This is handled by examining the equation in the completions of the rational numbers: the real numbers and the *p*-adic numbers. A more formal version of the Hasse principle states that certain types of equations have a rational solution if and only if they have a solution in the real numbers *and* in the *p*-adic numbers for each prime *p*.
