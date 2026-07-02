---
title: "Zeros and poles"
source: https://en.wikipedia.org/wiki/Zeros_and_poles
domain: z-transform
license: CC-BY-SA-4.0
tags: z-transform, bilinear transform, region of convergence, digital filter
fetched: 2026-07-02
---

# Zeros and poles

In complex analysis (a branch of mathematics), a **pole** is a certain type of singularity of a complex-valued function of a complex variable. It is the simplest type of non-removable singularity of such a function (see essential singularity). Technically, a point *z*0 is a pole of a function f if it is a zero of the function 1/*f* and 1/*f* is holomorphic (i.e. complex differentiable) in some neighbourhood of *z*0.

A function f is meromorphic in an open set U if for every point z of U there is a neighborhood of z in which at least one of f and 1/*f* is holomorphic.

If f is meromorphic in U, then a zero of f is a pole of 1/*f*, and a pole of f is a zero of 1/*f*. This induces a duality between *zeros* and *poles*, that is fundamental for the study of meromorphic functions. For example, if a function is meromorphic on the whole complex plane plus the point at infinity, then the sum of the multiplicities of its poles equals the sum of the multiplicities of its zeros.

## Definitions

A function of a complex variable z is holomorphic in an open domain U if it is differentiable with respect to z at every point of U. Equivalently, it is holomorphic if it is analytic, that is, if its Taylor series exists at every point of U, and converges to the function in some neighbourhood of the point. A function is meromorphic in U if every point of U has a neighbourhood such that at least one of f and 1/*f* is holomorphic in it.

A **zero** of a meromorphic function f is a complex number z such that *f*(*z*) = 0. A **pole** of f is a zero of 1/*f*.

If f is a function that is meromorphic in a neighbourhood of a point $z_{0}$ of the complex plane, then there exists an integer n such that

$(z-z_{0})^{n}f(z)$

is holomorphic and nonzero in a neighbourhood of $z_{0}$ (this is a consequence of the analytic property). If *n* > 0, then $z_{0}$ is a *pole* of **order** (or multiplicity) n of f. If *n* < 0, then $z_{0}$ is a zero of order $|n|$ of f. *Simple zero* and *simple pole* are terms used for zeroes and poles of order $|n|=1.$ *Degree* is sometimes used synonymously to order.

This characterization of zeros and poles implies that zeros and poles are isolated, that is, every zero or pole has a neighbourhood that does not contain any other zero and pole.

Because of the *order* of zeros and poles being defined as a non-negative number n and the symmetry between them, it is often useful to consider a pole of order n as a zero of order −*n* and a zero of order n as a pole of order −*n*. In this case a point that is neither a pole nor a zero is viewed as a pole (or zero) of order 0.

A meromorphic function may have infinitely many zeros and poles. This is the case for the gamma function (see the image in the infobox), which is meromorphic in the whole complex plane, and has a simple pole at every non-positive integer. The Riemann zeta function is also meromorphic in the whole complex plane, with a single pole of order 1 at *z* = 1. Its zeros in the left halfplane are all the negative even integers, and the Riemann hypothesis is the conjecture that all other zeros are along Re(*z*) = 1/2.

In a neighbourhood of a point $z_{0},$ a nonzero meromorphic function f is the sum of a Laurent series with at most finite *principal part* (the terms with negative index values):

$f(z)=\sum _{k\geq -n}a_{k}(z-z_{0})^{k},$

where n is an integer, and $a_{-n}\neq 0.$ Again, if *n* > 0 (the sum starts with $a_{-|n|}(z-z_{0})^{-|n|}$ , the principal part has n terms), one has a pole of order n, and if *n* ≤ 0 (the sum starts with $a_{|n|}(z-z_{0})^{|n|}$ , there is no principal part), one has a zero of order $|n|$ .

## At infinity

A function $z\mapsto f(z)$ is *meromorphic at infinity* if it is meromorphic in some neighbourhood of infinity (that is outside some disk), and there is an integer n such that

$\lim _{z\to \infty }{\frac {f(z)}{z^{n}}}$

exists and is a nonzero complex number.

In this case, the point at infinity is a pole of order n if *n* > 0, and a zero of order $|n|$ if *n* < 0.

For example, a polynomial of degree n has a pole of degree n at infinity.

The complex plane extended by a point at infinity is called the Riemann sphere.

If f is a function that is meromorphic on the whole Riemann sphere, then it has a finite number of zeros and poles, and the sum of the orders of its poles equals the sum of the orders of its zeros.

Every rational function is meromorphic on the whole Riemann sphere, and, in this case, the sum of orders of the zeros or of the poles is the maximum of the degrees of the numerator and the denominator.

## Examples

- The function

$f(z)={\frac {3}{z}}$

is meromorphic on the whole Riemann sphere. It has a pole of order 1 or simple pole at

$z=0,$

and a simple zero at infinity.

- The function

$f(z)={\frac {z+2}{(z-5)^{2}(z+7)^{3}}}$

is meromorphic on the whole Riemann sphere. It has a pole of order 2 at

$z=5,$

and a pole of order 3 at

$z=-7$

. It has a simple zero at

$z=-2,$

and a quadruple zero at infinity.

- The function

$f(z)={\frac {z-4}{e^{z}-1}}$

is meromorphic in the whole complex plane, but not at infinity. It has poles of order 1 at

$z=2\pi ni{\text{ for }}n\in \mathbb {Z}$

. This can be seen from

Euler's formula

.

- The function

$f(z)=z$

has a single pole at infinity of order 1, and a single zero at the origin.

All above examples except for the third are rational functions. For a general discussion of zeros and poles of such functions, see Pole–zero plot § Continuous-time systems.

## Function on a curve

The concept of zeros and poles extends naturally to functions on a *complex curve*, that is complex analytic manifold of dimension one (over the complex numbers). The simplest examples of such curves are the complex plane and the Riemann surface. This extension is done by transferring structures and properties through charts, which are analytic isomorphisms.

More precisely, let f be a function from a complex curve M to the complex numbers. This function is holomorphic (resp. meromorphic) in a neighbourhood of a point z of M if there is a chart $\phi$ such that $f\circ \phi ^{-1}$ is holomorphic (resp. meromorphic) in a neighbourhood of $\phi (z).$ Then, z is a pole or a zero of order n if the same is true for $\phi (z).$

If the curve is compact, and the function f is meromorphic on the whole curve, then the number of zeros and poles is finite, and the sum of the orders of the poles equals the sum of the orders of the zeros. This is one of the basic facts that are involved in Riemann–Roch theorem.
