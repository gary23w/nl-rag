---
title: "Hermite polynomials"
source: https://en.wikipedia.org/wiki/Hermite_polynomials
domain: orthogonal-polynomials
license: CC-BY-SA-4.0
tags: orthogonal polynomials, hermite polynomials, chebyshev polynomials, jacobi polynomials
fetched: 2026-07-02
---

# Hermite polynomials

In mathematics, the **Hermite polynomials** are a classical orthogonal polynomial sequence.

The polynomials arise in:

- signal processing as Hermitian wavelets for wavelet transform analysis
- probability, such as the Edgeworth series, as well as in connection with Brownian motion;
- combinatorics, as an example of an Appell sequence, obeying the umbral calculus;
- numerical analysis as Gaussian quadrature;
- physics, where they give rise to the eigenstates of the quantum harmonic oscillator; and they also occur in some cases of the heat equation (when the term ${\begin{aligned}xu_{x}\end{aligned}}$ is present);
- systems theory in connection with nonlinear operations on Gaussian noise.
- random matrix theory in Gaussian ensembles.

Hermite polynomials were defined by Pierre-Simon Laplace in 1810, though in scarcely recognizable form, and studied in detail by Pafnuty Chebyshev in 1859. Chebyshev's work was overlooked, and they were named later after Charles Hermite, who wrote on the polynomials in 1864, describing them as new. They were not new, although Hermite was the first to define the multidimensional polynomials.

## Definition

Like the other classical orthogonal polynomials, the Hermite polynomials can be defined from several different starting points. Noting from the outset that there are two different standardizations in common use, one convenient method is as follows:

- The **"probabilist's Hermite polynomials"** are given by $\operatorname {He} _{n}(x)=(-1)^{n}e^{\frac {x^{2}}{2}}{\frac {d^{n}}{dx^{n}}}e^{-{\frac {x^{2}}{2}}},$
- while the **"physicist's Hermite polynomials"** are given by $H_{n}(x)=(-1)^{n}e^{x^{2}}{\frac {d^{n}}{dx^{n}}}e^{-x^{2}}.$

These equations have the form of a Rodrigues' formula and can also be written as, $\operatorname {He} _{n}(x)=\left(x-{\frac {d}{dx}}\right)^{n}\cdot 1,\quad H_{n}(x)=\left(2x-{\frac {d}{dx}}\right)^{n}\cdot 1.$

The two definitions are not exactly identical; each is a rescaling of the other: $H_{n}(x)=2^{\frac {n}{2}}\operatorname {He} _{n}\left({\sqrt {2}}\,x\right),\quad \operatorname {He} _{n}(x)=2^{-{\frac {n}{2}}}H_{n}\left({\frac {x}{\sqrt {2}}}\right).$

These are Hermite polynomial sequences of different variances; see the material on variances below.

The notation $\operatorname {He}$ and H is that used in the standard references. The polynomials $\operatorname {He} _{n}$ are sometimes denoted by $H_{n}$ , especially in probability theory, because ${\frac {1}{\sqrt {2\pi }}}e^{-{\frac {x^{2}}{2}}}$ is the probability density function for the normal distribution with expected value 0 and standard deviation 1. The probabilist's Hermite polynomials are also called the **monic Hermite polynomials**, because they are monic.

- The first eleven probabilist's Hermite polynomials are: ${\begin{aligned}\operatorname {He} _{0}(x)&=1,\\\operatorname {He} _{1}(x)&=x,\\\operatorname {He} _{2}(x)&=x^{2}-1,\\\operatorname {He} _{3}(x)&=x^{3}-3x,\\\operatorname {He} _{4}(x)&=x^{4}-6x^{2}+3,\\\operatorname {He} _{5}(x)&=x^{5}-10x^{3}+15x,\\\operatorname {He} _{6}(x)&=x^{6}-15x^{4}+45x^{2}-15,\\\operatorname {He} _{7}(x)&=x^{7}-21x^{5}+105x^{3}-105x,\\\operatorname {He} _{8}(x)&=x^{8}-28x^{6}+210x^{4}-420x^{2}+105,\\\operatorname {He} _{9}(x)&=x^{9}-36x^{7}+378x^{5}-1260x^{3}+945x,\\\operatorname {He} _{10}(x)&=x^{10}-45x^{8}+630x^{6}-3150x^{4}+4725x^{2}-945.\end{aligned}}$
- The first eleven physicist's Hermite polynomials are: ${\begin{aligned}H_{0}(x)&=1,\\H_{1}(x)&=2x,\\H_{2}(x)&=4x^{2}-2,\\H_{3}(x)&=8x^{3}-12x,\\H_{4}(x)&=16x^{4}-48x^{2}+12,\\H_{5}(x)&=32x^{5}-160x^{3}+120x,\\H_{6}(x)&=64x^{6}-480x^{4}+720x^{2}-120,\\H_{7}(x)&=128x^{7}-1344x^{5}+3360x^{3}-1680x,\\H_{8}(x)&=256x^{8}-3584x^{6}+13440x^{4}-13440x^{2}+1680,\\H_{9}(x)&=512x^{9}-9216x^{7}+48384x^{5}-80640x^{3}+30240x,\\H_{10}(x)&=1024x^{10}-23040x^{8}+161280x^{6}-403200x^{4}+302400x^{2}-30240.\end{aligned}}$

|   | physicist's | probabilist's |
|---|---|---|
| symbol | $H_{n}$ | $\operatorname {He} _{n}$ |
| head coefficient | $2^{n}$ | 1 |
| differential operator | $(-1)^{n}e^{x^{2}}{\frac {d^{n}}{dx^{n}}}e^{-x^{2}}$ | $(-1)^{n}e^{\frac {x^{2}}{2}}{\frac {d^{n}}{dx^{n}}}e^{-{\frac {x^{2}}{2}}}$ |
| orthogonal to | $e^{-x^{2}}$ | $e^{-{\frac {1}{2}}x^{2}}$ |
| inner product | $\int H_{m}(x)H_{n}(x){\frac {e^{-x^{2}}}{\sqrt {\pi }}}dx=2^{n}n!\,\delta _{mn}$ | $\int \operatorname {He} _{m}(x)\operatorname {He} _{n}(x)\,{\frac {e^{-{\frac {x^{2}}{2}}}}{\sqrt {2\pi }}}\,dx=n!\,\delta _{nm}$ |
| generating function | $e^{2xt-t^{2}}=\sum _{n=0}^{\infty }H_{n}(x){\frac {t^{n}}{n!}}$ | $e^{xt-{\frac {1}{2}}t^{2}}=\sum _{n=0}^{\infty }\operatorname {He} _{n}(x){\frac {t^{n}}{n!}}$ |
| Rodrigues' formula | $\left(2x-{\frac {d}{dx}}\right)^{n}\cdot 1$ | $\left(x-{\frac {d}{dx}}\right)^{n}\cdot 1$ |
| recurrence relation | $H_{n+1}(x)=2xH_{n}(x)-2nH_{n-1}(x)$ | $\operatorname {He} _{n+1}(x)=x\operatorname {He} _{n}(x)-n\operatorname {He} _{n-1}(x)$ |

- (The first six probabilist's Hermite polynomials '"`UNIQ--postMath-0000001D-QINU`"') The first six probabilist's Hermite polynomials $\operatorname {He} _{n}(x)$
- (The first six physicist's Hermite polynomials '"`UNIQ--postMath-0000001E-QINU`"') The first six physicist's Hermite polynomials $H_{n}(x)$

## Properties

The nth-order Hermite polynomial is a polynomial of degree n. The probabilist's version Hen has leading coefficient 1, while the physicist's version Hn has leading coefficient 2*n*.

### Symmetry

From the Rodrigues formulae given above, we can see that *Hn*(*x*) and *Hen*(*x*) are even or odd functions, with the same parity as n: $H_{n}(-x)=(-1)^{n}H_{n}(x),\quad \operatorname {He} _{n}(-x)=(-1)^{n}\operatorname {He} _{n}(x).$

### Orthogonality

*Hn*(*x*) and *Hen*(*x*) are nth-degree polynomials for *n* = 0, 1, 2, 3,.... These polynomials are orthogonal with respect to the *weight function* (measure) $w(x)=e^{-{\frac {x^{2}}{2}}}\quad ({\text{for }}\operatorname {He} )$ or $w(x)=e^{-x^{2}}\quad ({\text{for }}H),$ i.e., we have $\int _{-\infty }^{\infty }H_{m}(x)H_{n}(x)\,w(x)\,dx=0\quad {\text{for all }}m\neq n.$

Furthermore, $\int _{-\infty }^{\infty }H_{m}(x)H_{n}(x)\,e^{-x^{2}}\,dx={\sqrt {\pi }}\,2^{n}n!\,\delta _{nm},$ and $\int _{-\infty }^{\infty }\operatorname {He} _{m}(x)\operatorname {He} _{n}(x)\,e^{-{\frac {x^{2}}{2}}}\,dx={\sqrt {2\pi }}\,n!\,\delta _{nm},$ where $\delta _{nm}$ is the Kronecker delta.

The probabilist polynomials are thus orthogonal with respect to the standard normal probability density function.

### Completeness

The Hermite polynomials (probabilist's or physicist's) form an orthogonal basis of the Hilbert space of functions satisfying $\int _{-\infty }^{\infty }{\bigl |}f(x){\bigr |}^{2}\,w(x)\,dx<\infty ,$ in which the inner product is given by the integral $\langle f,g\rangle =\int _{-\infty }^{\infty }f(x){\overline {g(x)}}\,w(x)\,dx$ including the Gaussian weight function *w*(*x*) defined in the preceding section.

An orthogonal basis for *L*2(**R**, *w*(*x*) *dx*) is a *complete* orthogonal system. For an orthogonal system, *completeness* is equivalent to the fact that the 0 function is the only function *f* ∈ *L*2(**R**, *w*(*x*) *dx*) orthogonal to *all* functions in the system.

Since the linear span of Hermite polynomials is the space of all polynomials, one has to show (in physicist case) that if f satisfies $\int _{-\infty }^{\infty }f(x)x^{n}e^{-x^{2}}\,dx=0$ for every *n* ≥ 0, then *f* = 0.

One possible way to do this is to appreciate that the entire function $F(z)=\int _{-\infty }^{\infty }f(x)e^{zx-x^{2}}\,dx=\sum _{n=0}^{\infty }{\frac {z^{n}}{n!}}\int f(x)x^{n}e^{-x^{2}}\,dx=0$ vanishes identically. The fact then that *F*(*it*) = 0 for every real t means that the Fourier transform of *f*(*x*)*e*−*x*2 is 0, hence f is 0 almost everywhere. Variants of the above completeness proof apply to other weights with exponential decay.

In the Hermite case, it is also possible to prove an explicit identity that implies completeness (see section on the Completeness relation below).

An equivalent formulation of the fact that Hermite polynomials are an orthogonal basis for *L*2(**R**, *w*(*x*) *dx*) consists in introducing Hermite *functions* (see below), and in saying that the Hermite functions are an orthonormal basis for *L*2(**R**).

### Hermite's differential equation

The probabilist's Hermite polynomials are solutions of the Sturm–Liouville differential equation $\left(e^{-{\frac {1}{2}}x^{2}}u'\right)'+\lambda e^{-{\frac {1}{2}}x^{2}}u=0,$ where λ is a constant. Imposing the boundary condition that u should be polynomially bounded at infinity, the equation has solutions only if λ is a non-negative integer, and the solution is uniquely given by $u(x)=C_{1}\operatorname {He} _{\lambda }(x)$ , where $C_{1}$ denotes a constant.

Rewriting the differential equation as an eigenvalue problem $L[u]=u''-xu'=-\lambda u,$ the Hermite polynomials $\operatorname {He} _{\lambda }(x)$ may be understood as eigenfunctions of the differential operator $L[u]$ . This eigenvalue problem is called the **Hermite equation**, although the term is also used for the closely related equation $u''-2xu'=-2\lambda u.$ whose solution is uniquely given in terms of physicist's Hermite polynomials in the form $u(x)=C_{1}H_{\lambda }(x)$ , where $C_{1}$ denotes a constant, after imposing the boundary condition that u should be polynomially bounded at infinity.

The general solutions to the above second-order differential equations are in fact linear combinations of both Hermite polynomials and confluent hypergeometric functions of the first kind. For example, for the physicist's Hermite equation $u''-2xu'+2\lambda u=0,$ the general solution takes the form $u(x)=C_{1}H_{\lambda }(x)+C_{2}h_{\lambda }(x),$ where $C_{1}$ and $C_{2}$ are constants, $H_{\lambda }(x)$ are physicist's Hermite polynomials (of the first kind), and $h_{\lambda }(x)$ are physicist's Hermite functions (of the second kind). The latter functions are compactly represented as $h_{\lambda }(x)={}_{1}F_{1}(-{\tfrac {\lambda }{2}};{\tfrac {1}{2}};x^{2})$ where ${}_{1}F_{1}(a;b;z)$ are Confluent hypergeometric functions of the first kind. The conventional Hermite polynomials may also be expressed in terms of confluent hypergeometric functions, see below.

With more general boundary conditions, the Hermite polynomials can be generalized to obtain more general analytic functions for complex-valued λ. An explicit formula of Hermite polynomials in terms of contour integrals (Courant & Hilbert 1989) is also possible.

### Recurrence relation

The sequence of probabilist's Hermite polynomials also satisfies the recurrence relation $\operatorname {He} _{n+1}(x)=x\operatorname {He} _{n}(x)-\operatorname {He} _{n}'(x).$ Individual coefficients are related by the following recursion formula: $a_{n+1,k}={\begin{cases}-(k+1)a_{n,k+1}&k=0,\\a_{n,k-1}-(k+1)a_{n,k+1}&k>0,\end{cases}}$ and *a*0,0 = 1, *a*1,0 = 0, *a*1,1 = 1.

For the physicist's polynomials, assuming $H_{n}(x)=\sum _{k=0}^{n}a_{n,k}x^{k},$ we have $H_{n+1}(x)=2xH_{n}(x)-H_{n}'(x).$ Individual coefficients are related by the following recursion formula: $a_{n+1,k}={\begin{cases}-a_{n,k+1}&k=0,\\2a_{n,k-1}-(k+1)a_{n,k+1}&k>0,\end{cases}}$ and *a*0,0 = 1, *a*1,0 = 0, *a*1,1 = 2.

The Hermite polynomials constitute an Appell sequence, i.e., they are a polynomial sequence satisfying the identity ${\begin{aligned}\operatorname {He} _{n}'(x)&=n\operatorname {He} _{n-1}(x),\\H_{n}'(x)&=2nH_{n-1}(x).\end{aligned}}$

An integral recurrence that is deduced and demonstrated in is as follows: $\operatorname {He} _{n+1}(x)=(n+1)\int _{0}^{x}\operatorname {He} _{n}(t)dt-He'_{n}(0),$

$H_{n+1}(x)=2(n+1)\int _{0}^{x}H_{n}(t)dt-H'_{n}(0).$

Equivalently, by Taylor-expanding, ${\begin{aligned}\operatorname {He} _{n}(x+y)&=\sum _{k=0}^{n}{\binom {n}{k}}x^{n-k}\operatorname {He} _{k}(y)&&=2^{-{\frac {n}{2}}}\sum _{k=0}^{n}{\binom {n}{k}}\operatorname {He} _{n-k}\left(x{\sqrt {2}}\right)\operatorname {He} _{k}\left(y{\sqrt {2}}\right),\\H_{n}(x+y)&=\sum _{k=0}^{n}{\binom {n}{k}}H_{k}(x)(2y)^{n-k}&&=2^{-{\frac {n}{2}}}\cdot \sum _{k=0}^{n}{\binom {n}{k}}H_{n-k}\left(x{\sqrt {2}}\right)H_{k}\left(y{\sqrt {2}}\right).\end{aligned}}$ These umbral identities are self-evident and included in the differential operator representation detailed below, ${\begin{aligned}\operatorname {He} _{n}(x)&=e^{-{\frac {D^{2}}{2}}}x^{n},\\H_{n}(x)&=2^{n}e^{-{\frac {D^{2}}{4}}}x^{n}.\end{aligned}}$

In consequence, for the mth derivatives the following relations hold: ${\begin{aligned}\operatorname {He} _{n}^{(m)}(x)&={\frac {n!}{(n-m)!}}\operatorname {He} _{n-m}(x)&&=m!{\binom {n}{m}}\operatorname {He} _{n-m}(x),\\H_{n}^{(m)}(x)&=2^{m}{\frac {n!}{(n-m)!}}H_{n-m}(x)&&=2^{m}m!{\binom {n}{m}}H_{n-m}(x).\end{aligned}}$

It follows that the Hermite polynomials also satisfy the recurrence relation ${\begin{aligned}\operatorname {He} _{n+1}(x)&=x\operatorname {He} _{n}(x)-n\operatorname {He} _{n-1}(x),\\H_{n+1}(x)&=2xH_{n}(x)-2nH_{n-1}(x).\end{aligned}}$

These last relations, together with the initial polynomials *H*0(*x*) and *H*1(*x*), can be used in practice to compute the polynomials quickly.

Turán's inequalities are ${\mathit {H}}_{n}(x)^{2}-{\mathit {H}}_{n-1}(x){\mathit {H}}_{n+1}(x)=(n-1)!\sum _{i=0}^{n-1}{\frac {2^{n-i}}{i!}}{\mathit {H}}_{i}(x)^{2}>0.$

Moreover, the following multiplication theorem holds: ${\begin{aligned}H_{n}(\gamma x)&=\sum _{i=0}^{\left\lfloor {\tfrac {n}{2}}\right\rfloor }\gamma ^{n-2i}(\gamma ^{2}-1)^{i}{\binom {n}{2i}}{\frac {(2i)!}{i!}}H_{n-2i}(x),\\\operatorname {He} _{n}(\gamma x)&=\sum _{i=0}^{\left\lfloor {\tfrac {n}{2}}\right\rfloor }\gamma ^{n-2i}(\gamma ^{2}-1)^{i}{\binom {n}{2i}}{\frac {(2i)!}{i!}}2^{-i}\operatorname {He} _{n-2i}(x).\end{aligned}}$

### Explicit expression

The physicist's Hermite polynomials can be written explicitly as $H_{n}(x)={\begin{cases}\displaystyle n!\sum _{l=0}^{\frac {n}{2}}{\frac {(-1)^{{\tfrac {n}{2}}-l}}{(2l)!\left({\tfrac {n}{2}}-l\right)!}}(2x)^{2l}&{\text{for even }}n,\\\displaystyle n!\sum _{l=0}^{\frac {n-1}{2}}{\frac {(-1)^{{\frac {n-1}{2}}-l}}{(2l+1)!\left({\frac {n-1}{2}}-l\right)!}}(2x)^{2l+1}&{\text{for odd }}n.\end{cases}}$

These two equations may be combined into one using the floor function: $H_{n}(x)=n!\sum _{m=0}^{\left\lfloor {\tfrac {n}{2}}\right\rfloor }{\frac {(-1)^{m}}{m!(n-2m)!}}(2x)^{n-2m}.$

The probabilist's Hermite polynomials He have similar formulas, which may be obtained from these by replacing the power of 2*x* with the corresponding power of √2 *x* and multiplying the entire sum by 2−⁠*n*/2⁠: $\operatorname {He} _{n}(x)=n!\sum _{m=0}^{\left\lfloor {\tfrac {n}{2}}\right\rfloor }{\frac {(-1)^{m}}{m!(n-2m)!}}{\frac {x^{n-2m}}{2^{m}}}.$

### Inverse explicit expression

The inverse of the above explicit expressions, that is, those for monomials in terms of probabilist's Hermite polynomials He are $x^{n}=n!\sum _{m=0}^{\left\lfloor {\tfrac {n}{2}}\right\rfloor }{\frac {1}{2^{m}m!(n-2m)!}}\operatorname {He} _{n-2m}(x).$

The corresponding expressions for the physicist's Hermite polynomials H follow directly by properly scaling this: $x^{n}={\frac {n!}{2^{n}}}\sum _{m=0}^{\left\lfloor {\tfrac {n}{2}}\right\rfloor }{\frac {1}{m!(n-2m)!}}H_{n-2m}(x).$

### Generating function

The Hermite polynomials are given by the exponential generating function ${\begin{aligned}e^{xt-{\frac {1}{2}}t^{2}}&=\sum _{n=0}^{\infty }\operatorname {He} _{n}(x){\frac {t^{n}}{n!}},\\e^{2xt-t^{2}}&=\sum _{n=0}^{\infty }H_{n}(x){\frac {t^{n}}{n!}}.\end{aligned}}$

This equality is valid for all complex values of x and t, and can be obtained by writing the Taylor expansion at x of the entire function *z* → *e*−*z*2 (in the physicist's case). One can also derive the (physicist's) generating function by using Cauchy's integral formula to write the Hermite polynomials as $H_{n}(x)=(-1)^{n}e^{x^{2}}{\frac {d^{n}}{dx^{n}}}e^{-x^{2}}=(-1)^{n}e^{x^{2}}{\frac {n!}{2\pi i}}\oint _{\gamma }{\frac {e^{-z^{2}}}{(z-x)^{n+1}}}\,dz.$

Using this in the sum $\sum _{n=0}^{\infty }H_{n}(x){\frac {t^{n}}{n!}},$ one can evaluate the remaining integral using the calculus of residues and arrive at the desired generating function.

A slight generalization states $e^{2xt-t^{2}}H_{k}(x-t)=\sum _{n=0}^{\infty }{\frac {H_{n+k}(x)t^{n}}{n!}}$

### Expected values

If X is a random variable with a normal distribution with standard deviation 1 and expected value μ, then $\operatorname {\mathbb {E} } \left[\operatorname {He} _{n}(X)\right]=\mu ^{n}.$

The moments of the standard normal (with expected value zero) may be read off directly from the relation for even indices: $\operatorname {\mathbb {E} } \left[X^{2n}\right]=(-1)^{n}\operatorname {He} _{2n}(0)=(2n-1)!!,$ where (2*n* − 1)!! is the double factorial. Note that the above expression is a special case of the representation of the probabilist's Hermite polynomials as moments: $\operatorname {He} _{n}(x)={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{\infty }(x+iy)^{n}e^{-{\frac {y^{2}}{2}}}\,dy.$

### Integral representations

From the generating-function representation above, we see that the Hermite polynomials have a representation in terms of a contour integral, as ${\begin{aligned}\operatorname {He} _{n}(x)&={\frac {n!}{2\pi i}}\oint _{C}{\frac {e^{tx-{\frac {t^{2}}{2}}}}{t^{n+1}}}\,dt,\\H_{n}(x)&={\frac {n!}{2\pi i}}\oint _{C}{\frac {e^{2tx-t^{2}}}{t^{n+1}}}\,dt,\end{aligned}}$ with the contour encircling the origin.

Using the Fourier transform of the gaussian $e^{-x^{2}}={\frac {1}{\sqrt {\pi }}}\int e^{-t^{2}+2ixt}dt$ , we have ${\begin{aligned}H_{n}(x)&=(-1)^{n}e^{x^{2}}{\frac {d^{n}}{dx^{n}}}e^{-x^{2}}={\frac {(-2i)^{n}e^{x^{2}}}{\sqrt {\pi }}}\int t^{n}e^{-t^{2}+2ixt}dt\\\operatorname {He} _{n}(x)&={\frac {(-i)^{n}e^{x^{2}/2}}{\sqrt {2\pi }}}\int t^{n}\,e^{-t^{2}/2+ixt}\,dt.\end{aligned}}$

### Other properties

The discriminant is expressed as a hyperfactorial:

${\begin{aligned}\operatorname {Disc} (H_{n})&=2^{{\frac {3}{2}}n(n-1)}\prod _{j=1}^{n}j^{j}\\\operatorname {Disc} (\operatorname {He} _{n})&=\prod _{j=1}^{n}j^{j}\end{aligned}}$

The addition theorem, or the summation theorem, states that ${\frac {\left(\sum _{k=1}^{r}a_{k}^{2}\right)^{\frac {n}{2}}}{n!}}H_{n}\left({\frac {\sum _{k=1}^{r}a_{k}x_{k}}{\sqrt {\sum _{k=1}^{r}a_{k}^{2}}}}\right)=\sum _{m_{1}+m_{2}+\ldots +m_{r}=n,m_{i}\geq 0}\prod _{k=1}^{r}\left\{{\frac {a_{k}^{m_{k}}}{m_{k}!}}H_{m_{k}}\left(x_{k}\right)\right\}$ for any nonzero vector $a_{1:r}$ .

The multiplication theorem states that $H_{n}\left(\lambda x\right)=\lambda ^{n}\sum _{\ell =0}^{\left\lfloor n/2\right\rfloor }{\frac {\left(-n\right)_{2\ell }}{\ell !}}(1-\lambda ^{-2})^{\ell }H_{n-2\ell }\left(x\right)$ for any nonzero $\lambda$ .

Feldheim formula ${\begin{aligned}{\frac {1}{\sqrt {a\pi }}}&\int _{-\infty }^{+\infty }e^{-{\frac {x^{2}}{a}}}H_{m}\left({\frac {x+y}{\lambda }}\right)H_{n}\left({\frac {x+z}{\mu }}\right)dx\\&=\left(1-{\frac {a}{\lambda ^{2}}}\right)^{\frac {m}{2}}\left(1-{\frac {a}{\mu ^{2}}}\right)^{\frac {n}{2}}\sum _{r=0}^{\min(m,n)}r!{\binom {m}{r}}{\binom {n}{r}}\left({\frac {2a}{\sqrt {\left(\lambda ^{2}-a\right)\left(\mu ^{2}-a\right)}}}\right)^{r}H_{m-r}\left({\frac {y}{\sqrt {\lambda ^{2}-a}}}\right)H_{n-r}\left({\frac {z}{\sqrt {\mu ^{2}-a}}}\right)\end{aligned}}$ where $a\in \mathbb {C}$ has a positive real part. As a special case, ${\frac {1}{\sqrt {\pi }}}\int _{-\infty }^{+\infty }e^{-t^{2}}H_{m}(t\sin \theta +v\cos \theta )H_{n}(t\cos \theta -v\sin \theta )dt=(-1)^{n}\cos ^{m}\theta \sin ^{n}\theta H_{m+n}(v)$

### Asymptotics

As *n* → ∞, $e^{-{\frac {x^{2}}{2}}}\cdot H_{n}(x)\sim {\frac {2^{n}}{\sqrt {\pi }}}\Gamma \left({\frac {n+1}{2}}\right)\cos \left(x{\sqrt {2n}}-{\frac {n\pi }{2}}\right)$ For certain cases concerning a wider range of evaluation, it is necessary to include a factor for changing amplitude: $e^{-{\frac {x^{2}}{2}}}\cdot H_{n}(x)\sim {\frac {2^{n}}{\sqrt {\pi }}}\Gamma \left({\frac {n+1}{2}}\right)\cos \left(x{\sqrt {2n}}-{\frac {n\pi }{2}}\right)\left(1-{\frac {x^{2}}{2n+1}}\right)^{-{\frac {1}{4}}}={\frac {\Gamma (n+1)}{\Gamma \left({\frac {n}{2}}+1\right)}}\cos \left(x{\sqrt {2n}}-{\frac {n\pi }{2}}\right)\left(1-{\frac {x^{2}}{2n+1}}\right)^{-{\frac {1}{4}}},$ which, using Stirling's approximation, can be further simplified, in the limit, to $e^{-{\frac {x^{2}}{2}}}\cdot H_{n}(x)\sim \left({\frac {2n}{e}}\right)^{\frac {n}{2}}{\sqrt {2}}\cos \left(x{\sqrt {2n}}-{\frac {n\pi }{2}}\right)\left(1-{\frac {x^{2}}{2n+1}}\right)^{-{\frac {1}{4}}}.$ This expansion is needed to resolve the wavefunction of a quantum harmonic oscillator such that it agrees with the classical approximation in the limit of the correspondence principle. The term $\left(1-{\frac {x^{2}}{2n+1}}\right)^{-{\frac {1}{2}}}$ corresponds to the probability of finding a classical particle in a potential well of shape $V(x)={\frac {1}{2}}x^{2}$ at location x , if its total energy is $n+{\frac {1}{2}}$ . This is a general method in semiclassical analysis. The semiclassical approximation breaks down near $\pm {\sqrt {2n+1}}$ , the location where the classical particle would be turned back. This is a fold catastrophe, at which point the Airy function is needed.

A better approximation, which accounts for the variation in frequency, is given by $e^{-{\frac {x^{2}}{2}}}\cdot H_{n}(x)\sim \left({\frac {2n}{e}}\right)^{\frac {n}{2}}{\sqrt {2}}\cos \left(x{\sqrt {2n+1-{\frac {x^{2}}{3}}}}-{\frac {n\pi }{2}}\right)\left(1-{\frac {x^{2}}{2n+1}}\right)^{-{\frac {1}{4}}}.$

The Plancherel–Rotach asymptotics method, applied to Hermite polynomials, takes into account the uneven spacing of the zeros near the edges. It makes use of the substitution $x={\sqrt {2n+1}}\cos(\varphi ),\quad 0<\varepsilon \leq \varphi \leq \pi -\varepsilon ,$ with which one has the uniform approximation $e^{-{\frac {x^{2}}{2}}}\cdot H_{n}(x)=2^{{\frac {n}{2}}+{\frac {1}{4}}}{\sqrt {n!}}(\pi n)^{-{\frac {1}{4}}}(\sin \varphi )^{-{\frac {1}{2}}}\cdot \left(\sin \left({\frac {3\pi }{4}}+\left({\frac {n}{2}}+{\frac {1}{4}}\right)\left(\sin 2\varphi -2\varphi \right)\right)+O\left(n^{-1}\right)\right).$

Similar approximations hold for the monotonic and transition regions. Specifically, if $x={\sqrt {2n+1}}\cosh(\varphi ),\quad 0<\varepsilon \leq \varphi \leq \omega <\infty ,$ then $e^{-{\frac {x^{2}}{2}}}\cdot H_{n}(x)=2^{{\frac {n}{2}}-{\frac {3}{4}}}{\sqrt {n!}}(\pi n)^{-{\frac {1}{4}}}(\sinh \varphi )^{-{\frac {1}{2}}}\cdot e^{\left({\frac {n}{2}}+{\frac {1}{4}}\right)\left(2\varphi -\sinh 2\varphi \right)}\left(1+O\left(n^{-1}\right)\right),$ while for $x={\sqrt {2n+1}}+t$ with t complex and bounded, the approximation is $e^{-{\frac {x^{2}}{2}}}\cdot H_{n}(x)=\pi ^{\frac {1}{4}}2^{{\frac {n}{2}}+{\frac {1}{4}}}{\sqrt {n!}}\,n^{-{\frac {1}{12}}}\left(\operatorname {Ai} \left(2^{\frac {1}{2}}n^{\frac {1}{6}}t\right)+O\left(n^{-{\frac {2}{3}}}\right)\right),$ where Ai is the Airy function of the first kind.

### Special values

The physicist's Hermite polynomials evaluated at zero argument *Hn*(0) are called Hermite numbers.

$H_{n}(0)={\begin{cases}0&{\text{for odd }}n,\\(-2)^{\frac {n}{2}}(n-1)!!&{\text{for even }}n,\end{cases}}$ which satisfy the recursion relation *Hn*(0) = −2(*n* − 1)*H**n* − 2(0). Equivalently, $H_{2n}(0)=(-2)^{n}(2n-1)!!$ .

In terms of the probabilist's polynomials this translates to $\operatorname {He} _{n}(0)={\begin{cases}0&{\text{for odd }}n,\\(-1)^{\frac {n}{2}}(n-1)!!&{\text{for even }}n.\end{cases}}$

### Kibble–Slepian formula

Let ${\textstyle M}$ be a real ${\textstyle n\times n}$ symmetric matrix, then the **Kibble–Slepian formula** states that $\det(I+M)^{-{\frac {1}{2}}}e^{x^{T}M(I+M)^{-1}x}=\sum _{K}\left[\prod _{1\leq i\leq j\leq n}{\frac {(M_{ij}/2)^{k_{ij}}}{k_{ij}!}}\right]2^{-tr(K)}H_{k_{1}}(x_{1})\cdots H_{k_{n}}(x_{n})$ where ${\textstyle \sum _{K}}$ is the ${\frac {n(n+1)}{2}}$ -fold summation over all ${\textstyle n\times n}$ symmetric matrices with non-negative integer entries, $tr(K)$ is the trace of K , and ${\textstyle k_{i}}$ is defined as ${\textstyle k_{ii}+\sum _{j=1}^{n}k_{ij}}$ . This gives Mehler's formula when $M={\begin{bmatrix}0&u\\u&0\end{bmatrix}}$ .

Equivalently stated, if ${\textstyle T}$ is a positive semidefinite matrix, then set ${\textstyle M=-T(I+T)^{-1}}$ , we have ${\textstyle M(I+M)^{-1}=-T}$ , so $e^{-x^{T}Tx}=\det(I+T)^{-{\frac {1}{2}}}\sum _{K}\left[\prod _{1\leq i\leq j\leq n}{\frac {(M_{ij}/2)^{k_{ij}}}{k_{ij}!}}\right]2^{-tr(K)}H_{k_{1}}(x_{1})\dots H_{k_{n}}(x_{n})$ Equivalently stated in a form closer to the boson quantum mechanics of the harmonic oscillator: $\pi ^{-n/4}\det(I+M)^{-{\frac {1}{2}}}e^{-{\frac {1}{2}}x^{T}(I-M)(I+M)^{-1}x}=\sum _{K}\left[\prod _{1\leq i\leq j\leq n}M_{ij}^{k_{ij}}/k_{ij}!\right]\left[\prod _{1\leq i\leq n}k_{i}!\right]^{1/2}2^{-\operatorname {tr} K}\psi _{k_{1}}\left(x_{1}\right)\cdots \psi _{k_{n}}\left(x_{n}\right).$ where each ${\textstyle \psi _{n}(x)}$ is the ${\textstyle n}$ -th eigenfunction of the harmonic oscillator, defined as $\psi _{n}(x):={\frac {1}{\sqrt {2^{n}n!}}}\left({\frac {1}{\pi }}\right)^{\frac {1}{4}}e^{-{\frac {1}{2}}x^{2}}H_{n}(x)$ The Kibble–Slepian formula was proposed by Kibble in 1945 and proven by Slepian in 1972 using Fourier analysis. Foata gave a combinatorial proof while Louck gave a proof via boson quantum mechanics. It has a generalization for complex-argument Hermite polynomials.

### Zeroes

Let $x_{n,1}>\dots >x_{n,n}$ be the roots of $H_{n}$ in descending order. Let $a_{m}$ be the m -th zero of the Airy function $\operatorname {Ai} (x)$ in descending order: $0>a_{1}>a_{2}>\cdots$ . By the symmetry of $H_{n}$ , we need only consider the positive half of its roots.

We have $(2n+1)^{\frac {1}{2}}>x_{n,1}>x_{n,2}>\cdots >x_{n,\lfloor n/2\rfloor }>0.$ For each m , asymptotically at $n\to \infty$ , $x_{n,m}=(2n+1)^{\frac {1}{2}}+2^{-{\frac {1}{3}}}(2n+1)^{-{\frac {1}{6}}}a_{m}+\epsilon _{n,m},$ where $\epsilon _{n,m}=O\left(n^{-{\frac {5}{6}}}\right)$ , and $\epsilon _{n,m}<0$ .

See also, and the formulas involving the zeroes of Laguerre polynomials.

Let $F_{n}(t):={\frac {1}{n}}\#\{i:x_{n,i}\leq t\}$ be the cumulative distribution function for the roots of $H_{n}$ , then we have the semicircle law $\lim _{n\to \infty }F_{n}({\sqrt {2n}}t)={\frac {2}{\pi }}\int _{-1}^{t}{\sqrt {1-s^{2}}}ds\quad t\in (-1,+1)$ The **Stieltjes relation** states that $-x_{n,i}+\sum _{1\leq j\leq n,i\neq j}{\frac {1}{x_{n,i}-x_{n,j}}}=0$ and can be physically interpreted as the equilibrium position of n particles on a line, such that each particle i is attracted to the origin by a linear force $-x_{n,i}$ , and repelled by each other particle j by a reciprocal force ${\frac {1}{x_{n,i}-x_{n,j}}}$ . This can be constructed by confining n positively charged particles in $\mathbb {R} ^{2}$ to the real line, and connecting each particle to the origin by a spring. This is also called the **electrostatic model**, and relates to the Coulomb gas interpretation of the eigenvalues of gaussian ensembles.

As the zeroes specify the polynomial up to scaling, the Stieltjes relation provides an alternative way to uniquely characterize the Hermite polynomials.

Similarly, we have ${\begin{aligned}\sum _{i}x_{n,i}^{2}&=\sum _{1\leq i\leq n}^{n}\sum _{1\leq j\leq n,i\neq j}{\frac {1}{(x_{n,i}-x_{n,j})^{2}}}\\x_{n,i}&=\sum _{1\leq j\leq n,i\neq j}{\frac {1}{x_{n,i}-x_{n,j}}}\\{\frac {2n-2-x_{n,i}^{2}}{3}}&=\sum _{1\leq j\leq n,i\neq j}{\frac {1}{(x_{n,i}-x_{n,j})^{2}}}\\{\frac {1}{2}}x_{n,i}&=\sum _{1\leq j\leq n,i\neq j}{\frac {1}{(x_{n,i}-x_{n,j})^{3}}}\end{aligned}}$

## Relations to other functions

### Laguerre polynomials

The Hermite polynomials can be expressed as a special case of the Laguerre polynomials: ${\begin{aligned}H_{2n}(x)&=(-4)^{n}n!L_{n}^{\left(-{\frac {1}{2}}\right)}(x^{2})&&=4^{n}n!\sum _{k=0}^{n}(-1)^{n-k}{\binom {n-{\frac {1}{2}}}{n-k}}{\frac {x^{2k}}{k!}},\\H_{2n+1}(x)&=2(-4)^{n}n!xL_{n}^{\left({\frac {1}{2}}\right)}(x^{2})&&=2\cdot 4^{n}n!\sum _{k=0}^{n}(-1)^{n-k}{\binom {n+{\frac {1}{2}}}{n-k}}{\frac {x^{2k+1}}{k!}}.\end{aligned}}$

### Hypergeometric functions

The physicist's Hermite polynomials can be expressed as a special case of the parabolic cylinder functions: $H_{n}(x)=2^{n}U\left(-{\tfrac {1}{2}}n,{\tfrac {1}{2}},x^{2}\right)$ in the right half-plane, where *U*(*a*, *b*, *z*) is Tricomi's confluent hypergeometric function. Similarly, ${\begin{aligned}H_{2n}(x)&=(-1)^{n}{\frac {(2n)!}{n!}}\,_{1}F_{1}{\big (}-n,{\tfrac {1}{2}};x^{2}{\big )},\\H_{2n+1}(x)&=(-1)^{n}{\frac {(2n+1)!}{n!}}\,2x\,_{1}F_{1}{\big (}-n,{\tfrac {3}{2}};x^{2}{\big )},\end{aligned}}$ where 1*F*1(*a*, *b*; *z*) = *M*(*a*, *b*; *z*) is Kummer's confluent hypergeometric function. ${\begin{aligned}\mathrm {He} _{2n}(x)&=(-1)^{n}(2n-1)!!\;{}_{1}F_{1}\!\left(-n,{\tfrac {1}{2}};{\tfrac {x^{2}}{2}}\right),\\\mathrm {He} _{2n+1}(x)&=(-1)^{n}(2n+1)!!\;x\;{}_{1}F_{1}\!\left(-n,{\tfrac {3}{2}};{\tfrac {x^{2}}{2}}\right).\end{aligned}}$ There is also $H_{n}\left(x\right)=(2x)^{n}{{}_{2}F_{0}}\left({-{\tfrac {1}{2}}n,-{\tfrac {1}{2}}n+{\tfrac {1}{2}} \atop -};-{\frac {1}{x^{2}}}\right).$

### Limit relations

The Hermite polynomials can be obtained as the limit of various other polynomials.

As a limit of Jacobi polynomials: $\lim _{\alpha \to \infty }\alpha ^{-{\frac {1}{2}}n}P_{n}^{(\alpha ,\alpha )}\left(\alpha ^{-{\frac {1}{2}}}x\right)={\frac {H_{n}\left(x\right)}{2^{n}n!}}.$ As a limit of ultraspherical polynomials: $\lim _{\lambda \to \infty }\lambda ^{-{\frac {1}{2}}n}C_{n}^{(\lambda )}\left(\lambda ^{-{\frac {1}{2}}}x\right)={\frac {H_{n}\left(x\right)}{n!}}.$ As a limit of associated Laguerre polynomials: $\lim _{\alpha \to \infty }\left({\frac {2}{\alpha }}\right)^{{\frac {1}{2}}n}L_{n}^{(\alpha )}\left((2\alpha )^{\frac {1}{2}}x+\alpha \right)={\frac {(-1)^{n}}{n!}}H_{n}\left(x\right).$

## Hermite polynomial expansion

Similar to Taylor expansion, some functions are expressible as an infinite sum of Hermite polynomials. Specifically, if $\int e^{-x^{2}}f(x)^{2}dx<\infty$ , then it has an expansion in the physicist's Hermite polynomials.

For f that does not grow too fast, it has Hermite expansion $f(x)=\sum _{k}{\frac {\mathbb {E} _{X\sim {\mathcal {N}}(0,1)}[f^{(k)}(X)]}{k!}}\operatorname {He} _{k}(x)$ .

Given such f , the partial sums of the Hermite expansion of f converges to in the $L^{p}$ norm if and only if $4/3<p<4$ . $x^{n}={\frac {n!}{2^{n}}}\,\sum _{k=0}^{\left\lfloor n/2\right\rfloor }{\frac {1}{k!\,(n-2k)!}}\,H_{n-2k}(x)=n!\sum _{k=0}^{\left\lfloor n/2\right\rfloor }{\frac {1}{k!\,2^{k}\,(n-2k)!}}\,\operatorname {He} _{n-2k}(x),\qquad n\in \mathbb {Z} _{+}.$ $e^{ax}=e^{a^{2}/4}\sum _{n\geq 0}{\frac {a^{n}}{n!\,2^{n}}}\,H_{n}(x),\qquad a\in \mathbb {C} ,\quad x\in \mathbb {R} .$ $e^{-a^{2}x^{2}}=\sum _{n\geq 0}{\frac {(-1)^{n}a^{2n}}{n!\left(1+a^{2}\right)^{n+1/2}2^{2n}}}\,H_{2n}(x).$ $\operatorname {erf} (x)={\frac {2}{\sqrt {\pi }}}\int _{0}^{x}e^{-t^{2}}~dt={\frac {1}{\sqrt {2\pi }}}\sum _{k\geq 0}{\frac {(-1)^{k}}{k!(2k+1)2^{3k}}}H_{2k+1}(x).$ $\cosh(ax)=e^{a^{2}/2}\sum _{m=0}^{\infty }{\frac {a^{2m}}{(2m)!}}\,\mathrm {He} _{2m}(x),\quad \sinh(ax)=e^{a^{2}/2}\sum _{m=0}^{\infty }{\frac {a^{2m+1}}{(2m+1)!}}\,\mathrm {He} _{2m+1}(x)$ $\cos(ax)=e^{-a^{2}/2}\sum _{m=0}^{\infty }{\frac {(-1)^{m}a^{2m}}{(2m)!}}\,\mathrm {He} _{2m}(x),\quad \sin(ax)=e^{-a^{2}/2}\sum _{m=0}^{\infty }{\frac {(-1)^{m}a^{2m+1}}{(2m+1)!}}\,\mathrm {He} _{2m+1}(x)$ $\delta ={\frac {1}{\sqrt {2\pi }}}\sum _{k=0}^{\infty }{\frac {(-1)^{k}}{(2k)!!}}\operatorname {He} _{2k}$ $1_{x>0}={\frac {1}{2}}\operatorname {He} _{0}+{\frac {1}{\sqrt {2\pi }}}\sum _{k=0}^{\infty }{\frac {(-1)^{k}}{(2k)!!(2k+1)}}\operatorname {He} _{2k+1}$ The probabilist's Hermite expansion for the power functions are the same as the power expansions for the probabilist's Hermite polynomials, except with positive signs. For example: $\operatorname {He} _{3}(x)=x^{3}-3x,\quad x^{3}=\operatorname {He} _{3}(x)+3\operatorname {He} _{1}(x)$

## Differential-operator representation

The probabilist's Hermite polynomials satisfy the identity $\operatorname {He} _{n}(x)=e^{-{\frac {D^{2}}{2}}}x^{n},$ where D represents differentiation with respect to x, and the exponential is interpreted by expanding it as a power series. There are no delicate questions of convergence of this series when it operates on polynomials, since all but finitely many terms vanish.

Since the power-series coefficients of the exponential are well known, and higher-order derivatives of the monomial *x**n* can be written down explicitly, this differential-operator representation gives rise to a concrete formula for the coefficients of *Hn* that can be used to quickly compute these polynomials.

Since the formal expression for the Weierstrass transform W is *e**D*2, we see that the Weierstrass transform of (√2)*n**Hen*(⁠*x*/√2⁠) is *xn*. Essentially the Weierstrass transform thus turns a series of Hermite polynomials into a corresponding Maclaurin series.

The existence of some formal power series *g*(*D*) with nonzero constant coefficient, such that *Hen*(*x*) = *g*(*D*)*xn*, is another equivalent to the statement that these polynomials form an Appell sequence. Since they are an Appell sequence, they are *a fortiori* a Sheffer sequence.

## Generalizations

### Variance

The probabilist's Hermite polynomials defined above are orthogonal with respect to the standard normal probability distribution, whose density function is ${\frac {1}{\sqrt {2\pi }}}e^{-{\frac {x^{2}}{2}}},$ which has expected value 0 and variance 1.

Scaling, one may analogously speak of **generalized Hermite polynomials** $\operatorname {He} _{n}^{[\alpha ]}(x)$ of variance α, where α is any positive number. These are then orthogonal with respect to the normal probability distribution whose density function is ${\frac {1}{\sqrt {2\pi \alpha }}}e^{-{\frac {x^{2}}{2\alpha }}}.$ They are given by $\operatorname {He} _{n}^{[\alpha ]}(x)=\alpha ^{\frac {n}{2}}\operatorname {He} _{n}\left({\frac {x}{\sqrt {\alpha }}}\right)=\left({\frac {\alpha }{2}}\right)^{\frac {n}{2}}H_{n}\left({\frac {x}{\sqrt {2\alpha }}}\right)=e^{-{\frac {\alpha D^{2}}{2}}}\left(x^{n}\right).$

Now, if $\operatorname {He} _{n}^{[\alpha ]}(x)=\sum _{k=0}^{n}h_{n,k}^{[\alpha ]}x^{k},$ then the polynomial sequence whose nth term is $\left(\operatorname {He} _{n}^{[\alpha ]}\circ \operatorname {He} ^{[\beta ]}\right)(x)\equiv \sum _{k=0}^{n}h_{n,k}^{[\alpha ]}\,\operatorname {He} _{k}^{[\beta ]}(x)$ is called the umbral composition of the two polynomial sequences. It can be shown to satisfy the identities $\left(\operatorname {He} _{n}^{[\alpha ]}\circ \operatorname {He} ^{[\beta ]}\right)(x)=\operatorname {He} _{n}^{[\alpha +\beta ]}(x)$ and $\operatorname {He} _{n}^{[\alpha +\beta ]}(x+y)=\sum _{k=0}^{n}{\binom {n}{k}}\operatorname {He} _{k}^{[\alpha ]}(x)\operatorname {He} _{n-k}^{[\beta ]}(y).$ The last identity is expressed by saying that this parameterized family of polynomial sequences is known as a cross-sequence. (See the above section on Appell sequences and on the differential-operator representation, which leads to a ready derivation of it. This binomial type identity, for *α* = *β* = ⁠1/2⁠, has already been encountered in the above section on #Recursion relations.)

### "Negative variance"

Since polynomial sequences form a group under the operation of umbral composition, one may denote by $\operatorname {He} _{n}^{[-\alpha ]}(x)$ the sequence that is inverse to the one similarly denoted, but without the minus sign, and thus speak of Hermite polynomials of negative variance. For α > 0, the coefficients of $\operatorname {He} _{n}^{[-\alpha ]}(x)$ are just the absolute values of the corresponding coefficients of $\operatorname {He} _{n}^{[\alpha ]}(x)$ .

These arise as moments of normal probability distributions: The nth moment of the normal distribution with expected value μ and variance *σ*2 is $E[X^{n}]=\operatorname {He} _{n}^{[-\sigma ^{2}]}(\mu ),$ where X is a random variable with the specified normal distribution. A special case of the cross-sequence identity then says that $\sum _{k=0}^{n}{\binom {n}{k}}\operatorname {He} _{k}^{[\alpha ]}(x)\operatorname {He} _{n-k}^{[-\alpha ]}(y)=\operatorname {He} _{n}^{[0]}(x+y)=(x+y)^{n}.$

## Hermite functions

### Definition

One can define the **Hermite functions** (often called Hermite-Gaussian functions) from the physicist's polynomials: $\psi _{n}(x)=\left(2^{n}n!{\sqrt {\pi }}\right)^{-{\frac {1}{2}}}e^{-{\frac {x^{2}}{2}}}H_{n}(x)=(-1)^{n}\left(2^{n}n!{\sqrt {\pi }}\right)^{-{\frac {1}{2}}}e^{\frac {x^{2}}{2}}{\frac {d^{n}}{dx^{n}}}e^{-x^{2}}.$ Thus, ${\sqrt {2(n+1)}}~~\psi _{n+1}(x)=\left(x-{d \over dx}\right)\psi _{n}(x).$

Since these functions contain the square root of the weight function and have been scaled appropriately, they are orthonormal: $\int _{-\infty }^{\infty }\psi _{n}(x)\psi _{m}(x)\,dx=\delta _{nm},$ and they form an orthonormal basis of *L*2(**R**). This fact is equivalent to the corresponding statement for Hermite polynomials (see above).

The Hermite functions are closely related to the Whittaker function (Whittaker & Watson 1996) *D**n*(*z*): $D_{n}(z)=\left(n!{\sqrt {\pi }}\right)^{\frac {1}{2}}\psi _{n}\left({\frac {z}{\sqrt {2}}}\right)=(-1)^{n}e^{\frac {z^{2}}{4}}{\frac {d^{n}}{dz^{n}}}e^{\frac {-z^{2}}{2}}$ and thereby to other parabolic cylinder functions.

The Hermite functions satisfy the differential equation $\psi _{n}''(x)+\left(2n+1-x^{2}\right)\psi _{n}(x)=0.$ This equation is equivalent to the Schrödinger equation for a harmonic oscillator in quantum mechanics, so these functions are the eigenfunctions.

${\begin{aligned}\psi _{0}(x)&=\pi ^{-{\frac {1}{4}}}\,e^{-{\frac {1}{2}}x^{2}},\\\psi _{1}(x)&={\sqrt {2}}\,\pi ^{-{\frac {1}{4}}}\,x\,e^{-{\frac {1}{2}}x^{2}},\\\psi _{2}(x)&=\left({\sqrt {2}}\,\pi ^{\frac {1}{4}}\right)^{-1}\,\left(2x^{2}-1\right)\,e^{-{\frac {1}{2}}x^{2}},\\\psi _{3}(x)&=\left({\sqrt {3}}\,\pi ^{\frac {1}{4}}\right)^{-1}\,\left(2x^{3}-3x\right)\,e^{-{\frac {1}{2}}x^{2}},\\\psi _{4}(x)&=\left(2{\sqrt {6}}\,\pi ^{\frac {1}{4}}\right)^{-1}\,\left(4x^{4}-12x^{2}+3\right)\,e^{-{\frac {1}{2}}x^{2}},\\\psi _{5}(x)&=\left(2{\sqrt {15}}\,\pi ^{\frac {1}{4}}\right)^{-1}\,\left(4x^{5}-20x^{3}+15x\right)\,e^{-{\frac {1}{2}}x^{2}}.\end{aligned}}$

### Recursion relation

Following recursion relations of Hermite polynomials, the Hermite functions obey $\psi _{n}'(x)={\sqrt {\frac {n}{2}}}\,\psi _{n-1}(x)-{\sqrt {\frac {n+1}{2}}}\psi _{n+1}(x)$ and $x\psi _{n}(x)={\sqrt {\frac {n}{2}}}\,\psi _{n-1}(x)+{\sqrt {\frac {n+1}{2}}}\psi _{n+1}(x).$

Extending the first relation to the arbitrary mth derivatives for any positive integer m leads to $\psi _{n}^{(m)}(x)=\sum _{k=0}^{m}{\binom {m}{k}}(-1)^{k}2^{\frac {m-k}{2}}{\sqrt {\frac {n!}{(n-m+k)!}}}\psi _{n-m+k}(x)\operatorname {He} _{k}(x).$

This formula can be used in connection with the recurrence relations for *Hen* and *ψ**n* to calculate any derivative of the Hermite functions efficiently.

### Cramér's inequality

For real x, the Hermite functions satisfy the following bound due to Harald Cramér and Jack Indritz: ${\bigl |}\psi _{n}(x){\bigr |}\leq \pi ^{-{\frac {1}{4}}}.$

### As eigenfunctions of the Fourier transform

The Hermite functions *ψ**n*(*x*) are a set of eigenfunctions of the continuous Fourier transform F. To see this, take the physicist's version of the generating function and multiply by *e*−⁠1/2⁠*x*2. This gives $e^{-{\frac {1}{2}}x^{2}+2xt-t^{2}}=\sum _{n=0}^{\infty }e^{-{\frac {1}{2}}x^{2}}H_{n}(x){\frac {t^{n}}{n!}}.$

The Fourier transform of the left side is given by ${\begin{aligned}{\mathcal {F}}\left\{e^{-{\frac {1}{2}}x^{2}+2xt-t^{2}}\right\}(k)&={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{\infty }e^{-ixk}e^{-{\frac {1}{2}}x^{2}+2xt-t^{2}}\,dx\\&=e^{-{\frac {1}{2}}k^{2}-2kit+t^{2}}\\&=\sum _{n=0}^{\infty }e^{-{\frac {1}{2}}k^{2}}H_{n}(k){\frac {(-it)^{n}}{n!}}.\end{aligned}}$

The Fourier transform of the right side is given by ${\mathcal {F}}\left\{\sum _{n=0}^{\infty }e^{-{\frac {1}{2}}x^{2}}H_{n}(x){\frac {t^{n}}{n!}}\right\}=\sum _{n=0}^{\infty }{\mathcal {F}}\left\{e^{-{\frac {1}{2}}x^{2}}H_{n}(x)\right\}{\frac {t^{n}}{n!}}.$

Equating like powers of t in the transformed versions of the left and right sides finally yields ${\mathcal {F}}\left\{e^{-{\frac {1}{2}}x^{2}}H_{n}(x)\right\}=(-i)^{n}e^{-{\frac {1}{2}}k^{2}}H_{n}(k).$

The Hermite functions *ψn*(*x*) are thus an orthonormal basis of *L*2(**R**), which *diagonalizes the Fourier transform operator*. In short, we have: ${\frac {1}{\sqrt {2\pi }}}\int e^{-ikx}\psi _{n}(x)dx=(-i)^{n}\psi _{n}(k),\quad {\frac {1}{\sqrt {2\pi }}}\int e^{+ikx}\psi _{n}(k)dk=i^{n}\psi _{n}(x)$

### Wigner distribution functions

The Wigner distribution function of the nth-order Hermite function is related to the nth-order Laguerre polynomial. The Laguerre polynomials are $L_{n}(x):=\sum _{k=0}^{n}{\binom {n}{k}}{\frac {(-1)^{k}}{k!}}x^{k},$ leading to the oscillator Laguerre functions $l_{n}(x):=e^{-{\frac {x}{2}}}L_{n}(x).$ For all natural integers n, one can prove that that $W_{\psi _{n}}(t,f)=2\,(-1)^{n}\,l_{n}{\big (}4\pi (t^{2}+f^{2}){\big )},$ where the Wigner distribution of a function *ψ* ∈ *L*2(**R**, **C**) is defined as $W_{\psi }(t,f)=\int _{-\infty }^{\infty }\psi \left(t+{\frac {\tau }{2}}\right)\,\psi \left(t-{\frac {\tau }{2}}\right)^{*}\,e^{-2\pi i\tau f}\,d\tau .$ This is a fundamental result for the quantum harmonic oscillator discovered by Hip Groenewold in 1946 in his PhD thesis. It is the standard paradigm of quantum mechanics in phase space.

There are further relations between the two families of polynomials.

### Partial overlap integrals

It can be shown that the overlap between two different Hermite functions ( $k\neq \ell$ ) over a given interval has the exact result: $\int _{x_{1}}^{x_{2}}\psi _{k}(x)\psi _{\ell }(x)\,dx={\frac {1}{2(\ell -k)}}\left(\psi _{k}'(x_{2})\psi _{\ell }(x_{2})-\psi _{\ell }'(x_{2})\psi _{k}(x_{2})-\psi _{k}'(x_{1})\psi _{\ell }(x_{1})+\psi _{\ell }'(x_{1})\psi _{k}(x_{1})\right).$

### Combinatorial interpretation of coefficients

In the Hermite polynomial *He**n*(*x*) of variance 1, the absolute value of the coefficient of *x**k* is the number of (unordered) partitions of an n-element set into k singletons and ⁠*n* − *k*/2⁠ (unordered) pairs. Equivalently, it is the number of involutions of an n-element set with precisely k fixed points, or in other words, the number of matchings in the complete graph on n vertices that leave k vertices uncovered (indeed, the Hermite polynomials are the matching polynomials of these graphs). The sum of the absolute values of the coefficients gives the total number of partitions into singletons and pairs, the so-called telephone numbers

1, 1, 2, 4, 10, 26, 76, 232, 764, 2620, 9496,... (sequence

A000085

in the

OEIS

).

This combinatorial interpretation can be related to complete exponential Bell polynomials as $\operatorname {He} _{n}(x)=B_{n}(x,-1,0,\ldots ,0),$ where *x**i* = 0 for all *i* > 2.

These numbers may also be expressed as a special value of the Hermite polynomials: $T(n)={\frac {\operatorname {He} _{n}(i)}{i^{n}}}.$

### Completeness relation

The Christoffel–Darboux formula for Hermite polynomials reads $\sum _{k=0}^{n}{\frac {H_{k}(x)H_{k}(y)}{k!2^{k}}}={\frac {1}{n!2^{n+1}}}\,{\frac {H_{n}(y)H_{n+1}(x)-H_{n}(x)H_{n+1}(y)}{x-y}}.$

Moreover, the following completeness identity for the above Hermite functions holds in the sense of distributions: $\sum _{n=0}^{\infty }\psi _{n}(x)\psi _{n}(y)=\delta (x-y),$ where δ is the Dirac delta function, *ψ**n* the Hermite functions, and *δ*(*x* − *y*) represents the Lebesgue measure on the line *y* = *x* in **R**2, normalized so that its projection on the horizontal axis is the usual Lebesgue measure.

This distributional identity follows Wiener (1958) by taking *u* → 1 in Mehler's formula, valid when −1 < *u* < 1: $E(x,y;u):=\sum _{n=0}^{\infty }u^{n}\,\psi _{n}(x)\,\psi _{n}(y)={\frac {1}{\sqrt {\pi (1-u^{2})}}}\,\exp \left(-{\frac {1-u}{1+u}}\,{\frac {(x+y)^{2}}{4}}-{\frac {1+u}{1-u}}\,{\frac {(x-y)^{2}}{4}}\right),$ which is often stated equivalently as a separable kernel, $\sum _{n=0}^{\infty }{\frac {H_{n}(x)H_{n}(y)}{n!}}\left({\frac {u}{2}}\right)^{n}={\frac {1}{\sqrt {1-u^{2}}}}e^{{\frac {2u}{1+u}}xy-{\frac {u^{2}}{1-u^{2}}}(x-y)^{2}}.$

The function (*x*, *y*) → *E*(*x*, *y*; *u*) is the bivariate Gaussian probability density on **R**2, which is, when u is close to 1, very concentrated around the line *y* = *x*, and very spread out on that line. It follows that $\sum _{n=0}^{\infty }u^{n}\langle f,\psi _{n}\rangle \langle \psi _{n},g\rangle =\iint E(x,y;u)f(x){\overline {g(y)}}\,dx\,dy\to \int f(x){\overline {g(x)}}\,dx=\langle f,g\rangle$ when *f* and *g* are continuous and compactly supported.

This yields that f can be expressed in Hermite functions as the sum of a series of vectors in *L*2(**R**), namely, $f=\sum _{n=0}^{\infty }\langle f,\psi _{n}\rangle \psi _{n}.$

In order to prove the above equality for *E*(*x*,*y*;*u*), the Fourier transform of Gaussian functions is used repeatedly: $\rho {\sqrt {\pi }}e^{-{\frac {\rho ^{2}x^{2}}{4}}}=\int e^{isx-{\frac {s^{2}}{\rho ^{2}}}}\,ds\quad {\text{for }}\rho >0.$

The Hermite polynomial is then represented as $H_{n}(x)=(-1)^{n}e^{x^{2}}{\frac {d^{n}}{dx^{n}}}\left({\frac {1}{2{\sqrt {\pi }}}}\int e^{isx-{\frac {s^{2}}{4}}}\,ds\right)=(-1)^{n}e^{x^{2}}{\frac {1}{2{\sqrt {\pi }}}}\int (is)^{n}e^{isx-{\frac {s^{2}}{4}}}\,ds.$

With this representation for *Hn*(*x*) and *Hn*(*y*), it is evident that ${\begin{aligned}E(x,y;u)&=\sum _{n=0}^{\infty }{\frac {u^{n}}{2^{n}n!{\sqrt {\pi }}}}\,H_{n}(x)H_{n}(y)e^{-{\frac {x^{2}+y^{2}}{2}}}\\&={\frac {e^{\frac {x^{2}+y^{2}}{2}}}{4\pi {\sqrt {\pi }}}}\iint \left(\sum _{n=0}^{\infty }{\frac {1}{2^{n}n!}}(-ust)^{n}\right)e^{isx+ity-{\frac {s^{2}}{4}}-{\frac {t^{2}}{4}}}\,ds\,dt\\&={\frac {e^{\frac {x^{2}+y^{2}}{2}}}{4\pi {\sqrt {\pi }}}}\iint e^{-{\frac {ust}{2}}}\,e^{isx+ity-{\frac {s^{2}}{4}}-{\frac {t^{2}}{4}}}\,ds\,dt,\end{aligned}}$ and this yields the desired resolution of the identity result, using again the Fourier transform of Gaussian kernels under the substitution $s={\frac {\sigma +\tau }{\sqrt {2}}},\quad t={\frac {\sigma -\tau }{\sqrt {2}}}.$
