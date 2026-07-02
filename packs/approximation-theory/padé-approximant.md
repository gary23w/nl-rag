---
title: "Padé approximant"
source: https://en.wikipedia.org/wiki/Pad%C3%A9_approximant
domain: approximation-theory
license: CC-BY-SA-4.0
tags: approximation theory, remez algorithm, pade approximant, minimax approximation
fetched: 2026-07-02
---

# Padé approximant

In mathematics, a **Padé approximant** is the "best" approximation of a function near a specific point by a rational function of given order. Under this technique, the approximant's power series agrees with the power series of the function it is approximating. The technique was developed around 1890 by Henri Padé, but goes back to Georg Frobenius, who introduced the idea and investigated the features of rational approximations of power series.

The Padé approximant often gives better approximation of the function than truncating its Taylor series, and it may still work where the Taylor series does not converge. For these reasons Padé approximants are used extensively in computer calculations. They have also been used as auxiliary functions in Diophantine approximation and transcendental number theory, though for sharp results, ad hoc methods—in some sense inspired by the Padé theory—typically replace them. Since a Padé approximant is a rational function, an artificial singular point may occur as an approximation, but this can be avoided by Borel–Padé analysis.

The reason the Padé approximant tends to be a better approximation than a truncating Taylor series is clear from the viewpoint of the multi-point summation method. Since there are many cases in which the asymptotic expansion at infinity becomes 0 or a constant, it can be interpreted as the "incomplete two-point Padé approximation", in which the ordinary Padé approximation improves on the method of truncating a Taylor series.

## Definition

Given a function *f* and two integers *m* ≥ 0 and *n* ≥ 1, the *Padé approximant* of order [*m*/*n*] is the rational function

$R(x)={\frac {\sum _{j=0}^{m}a_{j}x^{j}}{1+\sum _{k=1}^{n}b_{k}x^{k}}}={\frac {a_{0}+a_{1}x+a_{2}x^{2}+\dots +a_{m}x^{m}}{1+b_{1}x+b_{2}x^{2}+\dots +b_{n}x^{n}}},$ which agrees with *f*(*x*) to the highest possible order, which amounts to ${\begin{aligned}f(0)&=R(0),\\f'(0)&=R'(0),\\f''(0)&=R''(0),\\&\mathrel {\;\vdots } \\f^{(m+n)}(0)&=R^{(m+n)}(0).\end{aligned}}$

Equivalently, if $R(x)$ is expanded in a Maclaurin series (Taylor series at 0), its first $m+n$ terms would equal the first $m+n$ terms of $f(x)$ , and thus $f(x)-R(x)=c_{m+n+1}x^{m+n+1}+c_{m+n+2}x^{m+n+2}+\cdots$

When it exists, the Padé approximant is unique as a formal power series for the given *m* and *n*.

The Padé approximant defined above is also denoted as $[m/n]_{f}(x).$

## Computation

For given *f*, Padé approximants can be computed by Wynn's epsilon algorithm and also other sequence transformations from the partial sums $T_{N}(x)=c_{0}+c_{1}x+c_{2}x^{2}+\cdots +c_{N}x^{N}$ of the Taylor series of *f*, i.e., we have $c_{k}={\frac {f^{(k)}(0)}{k!}}.$ *f* can also be a formal power series, and, hence, Padé approximants can also be applied to the summation of divergent series.

One way to compute a Padé approximant is via the extended Euclidean algorithm for the polynomial greatest common divisor. The relation $R(x)=P(x)/Q(x)=T_{m+n}(x){\bmod {x}}^{m+n+1}$ is equivalent to the existence of some factor $K(x)$ such that $P(x)=Q(x)T_{m+n}(x)+K(x)x^{m+n+1},$ which can be interpreted as the Bézout identity of one step in the computation of the extended greatest common divisor of the polynomials $T_{m+n}(x)$ and $x^{m+n+1}$ .

Recall that, to compute the greatest common divisor of two polynomials *p* and *q*, one computes via long division the remainder sequence $r_{0}=p,\;r_{1}=q,\quad r_{k-1}=q_{k}r_{k}+r_{k+1},$ *k* = 1, 2, 3, ... with $\deg r_{k+1}<\deg r_{k}\,$ , until $r_{k+1}=0$ . For the Bézout identities of the extended greatest common divisor one computes simultaneously the two polynomial sequences $u_{0}=1,\;v_{0}=0,\quad u_{1}=0,\;v_{1}=1,\quad u_{k+1}=u_{k-1}-q_{k}u_{k},\;v_{k+1}=v_{k-1}-q_{k}v_{k}$ to obtain in each step the Bézout identity $r_{k}(x)=u_{k}(x)p(x)+v_{k}(x)q(x).$

For the [*m*/*n*] approximant, one thus carries out the extended Euclidean algorithm for $r_{0}=x^{m+n+1},\;r_{1}=T_{m+n}(x)$ and stops it at the last instant that $v_{k}$ has degree *n* or smaller.

Then the polynomials $P=r_{k},\;Q=v_{k}$ give the [*m*/*n*] Padé approximant. If one were to compute all steps of the extended greatest common divisor computation, one would obtain an anti-diagonal of the Padé table.

## Riemann–Padé zeta function

To study the resummation of a divergent series, say $\sum _{z=1}^{\infty }f(z),$ it can be useful to introduce the Padé or simply rational zeta function as $\zeta _{R}(s)=\sum _{z=1}^{\infty }{\frac {R(z)}{z^{s}}},$ where $R(x)=[m/n]_{f}(x)$ is the Padé approximation of order (*m*, *n*) of the function *f*(*x*). The zeta regularization value at *s* = 0 is taken to be the sum of the divergent series.

The functional equation for this Padé zeta function is $\sum _{j=0}^{n}a_{j}\zeta _{R}(s-j)=\sum _{j=0}^{m}b_{j}\zeta _{0}(s-j),$ where *aj* and *bj* are the coefficients in the Padé approximation. The subscript '0' means that the Padé is of order [0/0] and hence, we have the Riemann zeta function.

## DLog Padé method

Padé approximants can be used to extract critical points and exponents of functions. In thermodynamics, if a function *f*(*x*) behaves in a non-analytic way near a point *x* = *r* like $f(x)\sim |x-r|^{p}$ , one calls *x* = *r* a critical point and *p* the associated critical exponent of *f*. If sufficient terms of the series expansion of *f* are known, one can approximately extract the critical points and the critical exponents from respectively the poles and residues of the Padé approximants $[n/n+1]_{g}(x)$ , where $g=f'/f$ .

## Generalizations

A Padé approximant approximates a function in one variable. An approximant in two variables is called a Chisholm approximant (after J. S. R. Chisholm), in multiple variables a Canterbury approximant (after Graves-Morris at the University of Kent).

## Two-points Padé approximant

The conventional Padé approximation is determined to reproduce the Maclaurin expansion up to a given order. Therefore, the approximation at the value apart from the expansion point may be poor. This is avoided by the 2-point Padé approximation, which is a type of multipoint summation method. At $x=0$ , consider a case that a function $f(x)$ which is expressed by asymptotic behavior $f_{0}(x)$ : $f\sim f_{0}(x)+o{\big (}f_{0}(x){\big )},\quad x\to 0,$ and at $x\to \infty$ , additional asymptotic behavior $f_{\infty }(x)$ : $f(x)\sim f_{\infty }(x)+o{\big (}f_{\infty }(x){\big )},\quad x\to \infty .$

By selecting the major behavior of $f_{0}(x),f_{\infty }(x)$ , approximate functions $F(x)$ such that simultaneously reproduce asymptotic behavior by developing the Padé approximation can be found in various cases. As a result, at the point $x\to \infty$ , where the accuracy of the approximation may be the worst in the ordinary Padé approximation, good accuracy of the 2-point Padé approximant is guaranteed. Therefore, the 2-point Padé approximant can be a method that gives a good approximation globally for $x=0\sim \infty$ .

In cases where $f_{0}(x),f_{\infty }(x)$ are expressed by polynomials or series of negative powers, exponential function, logarithmic function or $x\ln x$ , we can apply 2-point Padé approximant to $f(x)$ . There is a method of using this to give an approximate solution of a differential equation with high accuracy. Also, for the nontrivial zeros of the Riemann zeta function, the first nontrivial zero can be estimated with some accuracy from the asymptotic behavior on the real axis.

## Multi-point Padé approximant

A further extension of the 2-point Padé approximant is the multi-point Padé approximant. This method treats singularity points $x=x_{j}(j=1,2,3,\dots ,N)$ of a function $f(x)$ which is to be approximated. Consider the cases when singularities of a function are expressed with index $n_{j}$ by $f(x)\sim {\frac {A_{j}}{(x-x_{j})^{n_{j}}}},\quad x\to x_{j}.$

Besides the 2-point Padé approximant, which includes information at $x=0,x\to \infty$ , this method approximates to reduce the property of diverging at $x\sim x_{j}$ . As a result, since the information of the peculiarity of the function is captured, the approximation of a function $f(x)$ can be performed with higher accuracy.

## Examples

**sin(*x*)**

$\sin(x)\approx {\frac {{\frac {12671}{4363920}}x^{5}-{\frac {2363}{18183}}x^{3}+x}{1+{\frac {445}{12122}}x^{2}+{\frac {601}{872784}}x^{4}+{\frac {121}{16662240}}x^{6}}}$

**exp(*x*)**

$\exp(x)\approx {\frac {1+{\frac {1}{2}}x+{\frac {1}{9}}x^{2}+{\frac {1}{72}}x^{3}+{\frac {1}{1008}}x^{4}+{\frac {1}{30240}}x^{5}}{1-{\frac {1}{2}}x+{\frac {1}{9}}x^{2}-{\frac {1}{72}}x^{3}+{\frac {1}{1008}}x^{4}-{\frac {1}{30240}}x^{5}}}$

**ln(1+*x*)**

$\ln(1+x)\approx {\frac {x+{\frac {1}{2}}x^{2}}{1+x+{\frac {1}{6}}x^{2}}}$

**Jacobi sn(*z*|3)**

$\mathrm {sn} (z|3)\approx {\frac {-{\frac {9851629}{283609260}}z^{5}-{\frac {572744}{4726821}}z^{3}+z}{1+{\frac {859490}{1575607}}z^{2}-{\frac {5922035}{56721852}}z^{4}+{\frac {62531591}{2977897230}}z^{6}}}$

**Bessel *J*5(*x*)**

$J_{5}(x)\approx {\frac {-{\frac {107}{28416000}}x^{7}+{\frac {1}{3840}}x^{5}}{1+{\frac {151}{5550}}x^{2}+{\frac {1453}{3729600}}x^{4}+{\frac {1339}{358041600}}x^{6}+{\frac {2767}{120301977600}}x^{8}}}$

**Error erf(*x*)**

$\operatorname {erf} (x)\approx {\frac {2}{15{\sqrt {\pi }}}}\cdot {\frac {49140x+3570x^{3}+739x^{5}}{165x^{4}+1330x^{2}+3276}}$

**Fresnel *C*(*x*)**

$C(x)\approx {\frac {1}{135}}\cdot {\frac {990791\pi ^{4}x^{9}-147189744\pi ^{2}x^{5}+8714684160x}{1749\pi ^{4}x^{8}+523536\pi ^{2}x^{4}+64553216}}$
