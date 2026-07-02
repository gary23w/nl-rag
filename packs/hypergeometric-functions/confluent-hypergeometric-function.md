---
title: "Confluent hypergeometric function"
source: https://en.wikipedia.org/wiki/Confluent_hypergeometric_function
domain: hypergeometric-functions
license: CC-BY-SA-4.0
tags: hypergeometric function, confluent hypergeometric function, pochhammer symbol, hypergeometric series
fetched: 2026-07-02
---

# Confluent hypergeometric function

In mathematics, a **confluent hypergeometric function** is a solution of a **confluent hypergeometric equation**, which is a degenerate form of a hypergeometric differential equation where two of the three regular singularities merge into an irregular singularity. The term *confluent* refers to the merging of singular points of families of differential equations; *confluere* is Latin for "to flow together". There are several common standard forms of confluent hypergeometric functions:

- **Kummer's (confluent hypergeometric) function** *M*(*a*, *b*, *z*), introduced by Kummer (1837), is a solution to **Kummer's differential equation**. This is also known as the confluent hypergeometric function of the first kind. There is a different and unrelated Kummer's function bearing the same name.
- **Tricomi's (confluent hypergeometric) function** *U*(*a*, *b*, *z*) introduced by Francesco Tricomi (1947), sometimes denoted by Ψ(*a*; *b*; *z*), is another solution to Kummer's equation. This is also known as the confluent hypergeometric function of the second kind.
- **Whittaker functions** (for Edmund Taylor Whittaker) are solutions to **Whittaker's equation**.
- **Coulomb wave functions** are solutions to the **Coulomb wave equation**.

The Kummer functions, Whittaker functions, and Coulomb wave functions are essentially the same, and differ from each other only by elementary functions and change of variables.

## Kummer's equation

Kummer's equation may be written as:

$z{\frac {d^{2}w}{dz^{2}}}+(b-z){\frac {dw}{dz}}-aw=0,$

with a regular singular point at *z* = 0 and an irregular singular point at *z* = ∞. It has two (usually) linearly independent solutions *M*(*a*, *b*, *z*) and *U*(*a*, *b*, *z*).

Kummer's function of the first kind M is a generalized hypergeometric series introduced in (Kummer 1837), given by:

$M(a,b,z)=\sum _{n=0}^{\infty }{\frac {a^{(n)}z^{n}}{b^{(n)}n!}}={}_{1}F_{1}(a;b;z),$

where:

$a^{(0)}=1,$

$a^{(n)}=a(a+1)(a+2)\cdots (a+n-1)\,,$

is the rising factorial. Another common notation for this solution is Φ(*a*, *b*, *z*). Considered as a function of a, b, or z with the other two held constant, this defines an entire function of a or z, except when *b* = 0, −1, −2, ... As a function of b it is analytic except for poles at the non-positive integers.

Some values of a and b yield solutions that can be expressed in terms of other known functions. See #Special cases. When a is a non-positive integer, then Kummer's function (if it is defined) is a generalized Laguerre polynomial.

Just as the confluent differential equation is a limit of the hypergeometric differential equation as the singular point at 1 is moved towards the singular point at ∞, the confluent hypergeometric function can be given as a limit of the hypergeometric function

$M(a,c,z)=\lim _{b\to \infty }{}_{2}F_{1}(a,b;c;z/b)$

and many of the properties of the confluent hypergeometric function are limiting cases of properties of the hypergeometric function.

Since Kummer's equation is second order there must be another, independent, solution. The indicial equation of the method of Frobenius tells us that the lowest power of a power series solution to the Kummer equation is either 0 or 1 − *b*. If we let *w*(*z*) be

$w(z)=z^{1-b}v(z)$

then the differential equation gives

$z^{2-b}{\frac {d^{2}v}{dz^{2}}}+2(1-b)z^{1-b}{\frac {dv}{dz}}-b(1-b)z^{-b}v+(b-z)\left[z^{1-b}{\frac {dv}{dz}}+(1-b)z^{-b}v\right]-az^{1-b}v=0$

which, upon dividing out *z*1−*b* and simplifying, becomes

$z{\frac {d^{2}v}{dz^{2}}}+(2-b-z){\frac {dv}{dz}}-(a+1-b)v=0.$

This means that *z*1−*b**M*(*a* + 1 − *b*, 2 − *b*, *z*) is a solution so long as b is not an integer greater than 1, just as *M*(*a*, *b*, *z*) is a solution so long as b is not an integer less than 1. We can also use the Tricomi confluent hypergeometric function *U*(*a*, *b*, *z*) introduced by Francesco Tricomi (1947), and sometimes denoted by Ψ(*a*; *b*; *z*). It is a combination of the above two solutions, defined by

$U(a,b,z)={\frac {\Gamma (1-b)}{\Gamma (a+1-b)}}M(a,b,z)+{\frac {\Gamma (b-1)}{\Gamma (a)}}z^{1-b}M(a+1-b,2-b,z).$

Although this expression is undefined for integer b, it has the advantage that it can be extended to any integer b by continuity. Unlike Kummer's function which is an entire function of z, *U*(*z*) usually has a singularity at zero. For example, if *b* = 0 and *a* ≠ 0 then Γ(*a*+1)*U*(*a*, *b*, *z*) − 1 is asymptotic to *az* ln *z* as z goes to zero. But see #Special cases for some examples where it is an entire function (polynomial).

Note that the solution *z*1−*b**U*(*a* + 1 − *b*, 2 − *b*, *z*) to Kummer's equation is the same as the solution *U*(*a*, *b*, *z*), see #Kummer's transformation.

For most combinations of real or complex a and b, the functions *M*(*a*, *b*, *z*) and *U*(*a*, *b*, *z*) are independent, and if b is a non-positive integer, so *M*(*a*, *b*, *z*) doesn't exist, then we may be able to use *z*1−*b**M*(*a*+1−*b*, 2−*b*, *z*) as a second solution. But if a is a non-positive integer and b is not a non-positive integer, then *U*(*z*) is a multiple of *M*(*z*). In that case as well, *z*1−*b**M*(*a*+1−*b*, 2−*b*, *z*) can be used as a second solution if it exists and is different. But when b is an integer greater than 1, this solution doesn't exist, and if *b* = 1 then it exists but is a multiple of *U*(*a*, *b*, *z*) and of *M*(*a*, *b*, *z*) In those cases a second solution exists of the following form and is valid for any real or complex a and any positive integer b except when a is a positive integer less than b:

$M(a,b,z)\ln z+z^{1-b}\sum _{k=0}^{\infty }C_{k}z^{k}$

When *a* = 0 we can alternatively use:

$\int _{-\infty }^{z}(-u)^{-b}e^{u}\mathrm {d} u.$

When *b* = 1 this is the exponential integral *E*1(*−z*).

A similar problem occurs when *a*−*b* is a negative integer and b is an integer less than 1. In this case *M*(*a*, *b*, *z*) doesn't exist, and *U*(*a*, *b*, *z*) is a multiple of *z*1−*b**M*(*a*+1−*b*, 2−*b*, *z*). A second solution is then of the form:

$z^{1-b}M(a+1-b,2-b,z)\ln z+\sum _{k=0}^{\infty }C_{k}z^{k}$

### Other equations

Confluent Hypergeometric Functions can be used to solve the Extended Confluent Hypergeometric Equation whose general form is given as:

$z{\frac {d^{2}w}{dz^{2}}}+(b-z){\frac {dw}{dz}}-\left(\sum _{m=0}^{M}a_{m}z^{m}\right)w=0$

Note that for *M* = 0 or when the summation involves just one term, it reduces to the conventional Confluent Hypergeometric Equation.

Thus Confluent Hypergeometric Functions can be used to solve "most" second-order ordinary differential equations whose variable coefficients are all linear functions of z, because they can be transformed to the Extended Confluent Hypergeometric Equation. Consider the equation:

$(A+Bz){\frac {d^{2}w}{dz^{2}}}+(C+Dz){\frac {dw}{dz}}+(E+Fz)w=0$

First we move the regular singular point to 0 by using the substitution of *A* + *Bz* ↦ *z*, which converts the equation to:

$z{\frac {d^{2}w}{dz^{2}}}+(C+Dz){\frac {dw}{dz}}+(E+Fz)w=0$

with new values of C, D, E, and F. Next we use the substitution:

$z\mapsto {\frac {1}{\sqrt {D^{2}-4F}}}z$

and multiply the equation by the same factor, obtaining:

$z{\frac {d^{2}w}{dz^{2}}}+\left(C+{\frac {D}{\sqrt {D^{2}-4F}}}z\right){\frac {dw}{dz}}+\left({\frac {E}{\sqrt {D^{2}-4F}}}+{\frac {F}{D^{2}-4F}}z\right)w=0$

whose solution is

$\exp \left(-\left(1+{\frac {D}{\sqrt {D^{2}-4F}}}\right){\frac {z}{2}}\right)w(z),$

where *w*(*z*) is a solution to Kummer's equation with

$a=\left(1+{\frac {D}{\sqrt {D^{2}-4F}}}\right){\frac {C}{2}}-{\frac {E}{\sqrt {D^{2}-4F}}},\qquad b=C.$

Note that the square root may give an imaginary or complex number. If it is zero, another solution must be used, namely

$\exp \left(-{\tfrac {1}{2}}Dz\right)w(z),$

where *w*(*z*) is a confluent hypergeometric limit function satisfying

$zw''(z)+Cw'(z)+\left(E-{\tfrac {1}{2}}CD\right)w(z)=0.$

As noted below, even the Bessel equation can be solved using confluent hypergeometric functions.

## Integral representations

If Re *b* > Re *a* > 0, *M*(*a*, *b*, *z*) can be represented as an integral

$M(a,b,z)={\frac {\Gamma (b)}{\Gamma (a)\Gamma (b-a)}}\int _{0}^{1}e^{zu}u^{a-1}(1-u)^{b-a-1}\,du.$

thus *M*(*a*, *a*+*b*, *it*) is the characteristic function of the beta distribution. For a with positive real part U can be obtained by the Laplace integral

$U(a,b,z)={\frac {1}{\Gamma (a)}}\int _{0}^{\infty }e^{-zt}t^{a-1}(1+t)^{b-a-1}\,dt,\quad (\operatorname {Re} \ a>0)$

The integral defines a solution in the right half-plane Re *z* > 0.

They can also be represented as Barnes integrals

$M(a,b,z)={\frac {1}{2\pi i}}{\frac {\Gamma (b)}{\Gamma (a)}}\int _{-i\infty }^{i\infty }{\frac {\Gamma (-s)\Gamma (a+s)}{\Gamma (b+s)}}(-z)^{s}ds$

where the contour passes to one side of the poles of Γ(−*s*) and to the other side of the poles of Γ(*a* + *s*).

## Asymptotic behavior

If a solution to Kummer's equation is asymptotic to a power of z as *z* → ∞, then the power must be −*a*. This is in fact the case for Tricomi's solution *U*(*a*, *b*, *z*). Its asymptotic behavior as *z* → ∞ can be deduced from the integral representations. If *z* = *x* ∈ **R**, then making a change of variables in the integral followed by expanding the binomial series and integrating it formally term by term gives rise to an asymptotic series expansion, valid as *x* → ∞:

$U(a,b,x)\sim x^{-a}\,_{2}F_{0}\left(a,a-b+1;\,;-{\frac {1}{x}}\right),$

where $_{2}F_{0}(\cdot ,\cdot ;;-1/x)$ is a generalized hypergeometric series with 1 as leading term, which generally converges nowhere, but exists as a formal power series in 1/*x*. This asymptotic expansion is also valid for complex z instead of real x, with |arg *z*| < 3*π*/2.

The asymptotic behavior of Kummer's solution for large |*z*| is:

$M(a,b,z)\sim \Gamma (b)\left({\frac {e^{z}z^{a-b}}{\Gamma (a)}}+{\frac {(-z)^{-a}}{\Gamma (b-a)}}\right)$

The powers of z are taken using −3*π*/2 < arg *z* ≤ *π*/2. The first term is not needed when Γ(*b* − *a*) is finite, that is when *b* − *a* is not a non-positive integer and the real part of z goes to negative infinity, whereas the second term is not needed when Γ(*a*) is finite, that is, when a is a not a non-positive integer and the real part of z goes to positive infinity.

There is always some solution to Kummer's equation asymptotic to *ezz**a*−*b* as *z* → −∞. Usually this will be a combination of both *M*(*a*, *b*, *z*) and *U*(*a*, *b*, *z*) but can also be expressed as *ez* (−1)*a*-*b* *U*(*b* − *a*, *b*, −*z*).

## Relations

There are many relations between Kummer functions for various arguments and their derivatives. This section gives a few typical examples.

### Contiguous relations

Given *M*(*a*, *b*, *z*), the four functions *M*(*a* ± 1, *b*, *z*), *M*(*a*, *b* ± 1, *z*) are called contiguous to *M*(*a*, *b*, *z*). The function *M*(*a*, *b*, *z*) can be written as a linear combination of any two of its contiguous functions, with rational coefficients in terms of a, b, and z. This gives (4 2) = 6 relations, given by identifying any two lines on the right hand side of

${\begin{aligned}z{\frac {dM}{dz}}=z{\frac {a}{b}}M(a+,b+)&=a(M(a+)-M)\\&=(b-1)(M(b-)-M)\\&=(b-a)M(a-)+(a-b+z)M\\&=z(a-b)M(b+)/b+zM\\\end{aligned}}$

In the notation above, *M* = *M*(*a*, *b*, *z*), *M*(*a*+) = *M*(*a* + 1, *b*, *z*), and so on.

Repeatedly applying these relations gives a linear relation between any three functions of the form *M*(*a* + *m*, *b* + *n*, *z*) (and their higher derivatives), where m, n are integers.

There are similar relations for U.

### Kummer's transformation

Kummer's functions are also related by Kummer's transformations:

$M(a,b,z)=e^{z}\,M(b-a,b,-z)$

$U(a,b,z)=z^{1-b}U\left(1+a-b,2-b,z\right)$

.

## Multiplication theorem

The following multiplication theorems hold true:

${\begin{aligned}U(a,b,z)&=e^{(1-t)z}\sum _{i=0}{\frac {(t-1)^{i}z^{i}}{i!}}U(a,b+i,zt)\\&=e^{(1-t)z}t^{b-1}\sum _{i=0}{\frac {\left(1-{\frac {1}{t}}\right)^{i}}{i!}}U(a-i,b-i,zt).\end{aligned}}$

## Connection with Laguerre polynomials and similar representations

In terms of Laguerre polynomials, Kummer's functions have several expansions, for example

$M\left(a,b,{\frac {xy}{x-1}}\right)=(1-x)^{a}\cdot \sum _{n}{\frac {a^{(n)}}{b^{(n)}}}L_{n}^{(b-1)}(y)x^{n}$

(

Erdélyi et al. 1953

, 6.12)

or

$M\left(a,\,b,\,z\right)={\frac {\Gamma \left(1-a\right)\cdot \Gamma \left(b\right)}{\Gamma \left(b-a\right)}}\cdot L_{-a}^{(b-1)}\left(z\right)$

[1]

## Special cases

Functions that can be expressed as special cases of the confluent hypergeometric function include:

- Some elementary functions where the left-hand side is not defined when b is a non-positive integer, but the right-hand side is still a solution of the corresponding Kummer equation:

$M(0,b,z)=1$

$U(0,c,z)=1$

$M(b,b,z)=e^{z}$

$U(a,a,z)=e^{z}\int _{z}^{\infty }u^{-a}e^{-u}du$

(a polynomial if

a

is a non-positive integer)

${\frac {U(1,b,z)}{\Gamma (b-1)}}+{\frac {M(1,b,z)}{\Gamma (b)}}=z^{1-b}e^{z}$

$M(n,b,z)$

for non-positive integer

n

is a

generalized Laguerre polynomial

.

$U(n,c,z)$

for non-positive integer

n

is a multiple of a generalized Laguerre polynomial, equal to

${\tfrac {\Gamma (1-c)}{\Gamma (n+1-c)}}M(n,c,z)$

when the latter exists.

$U(c-n,c,z)$

when

n

is a positive integer is a closed form with powers of

z

, equal to

${\tfrac {\Gamma (c-1)}{\Gamma (c-n)}}z^{1-c}M(1-n,2-c,z)$

when the latter exists.

$U(a,a+1,z)=z^{-a}$

$U(-n,-2n,z)$

for non-negative integer

n

is a Bessel polynomial (see lower down).

$M(1,2,z)=(e^{z}-1)/z,\ \ M(1,3,z)=2!(e^{z}-1-z)/z^{2}$

etc.

Using the contiguous relation

$aM(a+)=(a+z)M+z(a-b)M(b+)/b$

we get, for example,

$M(2,1,z)=(1+z)e^{z}.$

- Bateman's function
- Bessel functions and many related functions such as Airy functions, Kelvin functions, Hankel functions. For example, in the special case *b* = 2*a* the function reduces to a Bessel function:

${}_{1}F_{1}(a,2a,x)=e^{x/2}\,{}_{0}F_{1}\left(;a+{\tfrac {1}{2}};{\tfrac {x^{2}}{16}}\right)=e^{x/2}\left({\tfrac {x}{4}}\right)^{1/2-a}\Gamma \left(a+{\tfrac {1}{2}}\right)I_{a-1/2}\left({\tfrac {x}{2}}\right).$

This identity is sometimes also referred to as

Kummer's

second transformation. Similarly

$U(a,2a,x)={\frac {e^{x/2}}{\sqrt {\pi }}}x^{1/2-a}K_{a-1/2}(x/2),$

When

a

is a non-positive integer, this equals

2

−

a

θ

−

a

(

x

/2)

where

θ

is a

Bessel polynomial

.

- The error function can be expressed as

$\mathrm {erf} (x)={\frac {2}{\sqrt {\pi }}}\int _{0}^{x}e^{-t^{2}}dt={\frac {2x}{\sqrt {\pi }}}\ {}_{1}F_{1}\left({\tfrac {1}{2}},{\tfrac {3}{2}},-x^{2}\right).$

- Coulomb wave function
- Cunningham functions
- Exponential integral and related functions such as the sine integral, logarithmic integral
- Hermite polynomials
- Incomplete gamma function
- Laguerre polynomials
- Parabolic cylinder function (or Weber function)
- Poisson–Charlier function
- Toronto functions
- Whittaker functions *Mκ,μ*(*z*), *Wκ,μ*(*z*) are solutions of Whittaker's equation that can be expressed in terms of Kummer functions M and U by

$M_{\kappa ,\mu }(z)=e^{-{\tfrac {z}{2}}}z^{\mu +{\tfrac {1}{2}}}M\left(\mu -\kappa +{\tfrac {1}{2}},1+2\mu ;z\right)$

$W_{\kappa ,\mu }(z)=e^{-{\tfrac {z}{2}}}z^{\mu +{\tfrac {1}{2}}}U\left(\mu -\kappa +{\tfrac {1}{2}},1+2\mu ;z\right)$

- The general p-th raw moment (p not necessarily an integer) can be expressed as

${\begin{aligned}\operatorname {E} \left[\left|N\left(\mu ,\sigma ^{2}\right)\right|^{p}\right]&={\frac {\left(2\sigma ^{2}\right)^{p/2}\Gamma \left({\tfrac {1+p}{2}}\right)}{\sqrt {\pi }}}\ {}_{1}F_{1}\left(-{\tfrac {p}{2}},{\tfrac {1}{2}},-{\tfrac {\mu ^{2}}{2\sigma ^{2}}}\right)\\\operatorname {E} \left[N\left(\mu ,\sigma ^{2}\right)^{p}\right]&=\left(-2\sigma ^{2}\right)^{p/2}U\left(-{\tfrac {p}{2}},{\tfrac {1}{2}},-{\tfrac {\mu ^{2}}{2\sigma ^{2}}}\right)\end{aligned}}$

In the second formula the function's second

branch cut

can be chosen by multiplying with

(−1)

p

.

## Application to continued fractions

By applying a limiting argument to Gauss's continued fraction it can be shown that

${\frac {M(a+1,b+1,z)}{M(a,b,z)}}={\cfrac {1}{1-{\cfrac {\displaystyle {\frac {b-a}{b(b+1)}}z}{1+{\cfrac {\displaystyle {\frac {a+1}{(b+1)(b+2)}}z}{1-{\cfrac {\displaystyle {\frac {b-a+1}{(b+2)(b+3)}}z}{1+{\cfrac {\displaystyle {\frac {a+2}{(b+3)(b+4)}}z}{1-\ddots }}}}}}}}}}$

and that this continued fraction converges uniformly to a meromorphic function of z in every bounded domain that does not include a pole.
