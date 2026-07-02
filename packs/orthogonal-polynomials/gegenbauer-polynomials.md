---
title: "Gegenbauer polynomials"
source: https://en.wikipedia.org/wiki/Gegenbauer_polynomials
domain: orthogonal-polynomials
license: CC-BY-SA-4.0
tags: orthogonal polynomials, hermite polynomials, chebyshev polynomials, jacobi polynomials
fetched: 2026-07-02
---

# Gegenbauer polynomials

In mathematics, **Gegenbauer polynomials** or **ultraspherical polynomials** *C*(α) *n*(*x*) are orthogonal polynomials on the interval [−1,1] with respect to the weight function (1 − *x*2)*α*–1/2. They generalize Legendre polynomials and Chebyshev polynomials, and are special cases of Jacobi polynomials. They are named after Leopold Gegenbauer.

## Characterizations

- (Plot of the Gegenbauer polynomial C n^(m)(x) with n=10 and m=1 in the complex plane from -2-2i to 2+2i with colors created with Mathematica 13.1 function ComplexPlot3D) Plot of the Gegenbauer polynomial C n^(m)(x) with n=10 and m=1 in the complex plane from -2-2i to 2+2i with colors created with Mathematica 13.1 function ComplexPlot3D
- (Gegenbauer polynomials with α=1) Gegenbauer polynomials with *α*=1
- (Gegenbauer polynomials with α=2) Gegenbauer polynomials with *α*=2
- (Gegenbauer polynomials with α=3) Gegenbauer polynomials with *α*=3
- (An animation showing the polynomials on the xα-plane for the first 4 values of n.) An animation showing the polynomials on the *xα*-plane for the first 4 values of *n*.

A variety of characterizations of the Gegenbauer polynomials are available.

- The polynomials can be defined in terms of their generating function:

${\frac {1}{(1-2xt+t^{2})^{\alpha }}}=\sum _{n=0}^{\infty }C_{n}^{(\alpha )}(x)t^{n}\qquad (0\leq |x|<1,|t|\leq 1,\alpha >0)$

- The polynomials satisfy the recurrence relation:

${\begin{aligned}C_{0}^{(\alpha )}(x)&=1\\C_{1}^{(\alpha )}(x)&=2\alpha x\\(n+1)C_{n+1}^{(\alpha )}(x)&=2(n+\alpha )xC_{n}^{(\alpha )}(x)-(n+2\alpha -1)C_{n-1}^{(\alpha )}(x).\end{aligned}}$

- Gegenbauer polynomials are particular solutions of the Gegenbauer differential equation:

$(1-x^{2})y''-(2\alpha +1)xy'+n(n+2\alpha )y=0.\,$

When

α

= 1/2, the equation reduces to the Legendre equation, and the Gegenbauer polynomials reduce to the

Legendre polynomials

.

When

α

= 1, the equation reduces to the

Chebyshev differential equation

, and the Gegenbauer polynomials reduce to the

Chebyshev polynomials

of the second kind.

- They are given as Gaussian hypergeometric series in certain cases where the series is in fact finite:

$C_{n}^{(\alpha )}(z)={\frac {(2\alpha )_{n}}{n!}}\,_{2}F_{1}\left(-n,2\alpha +n;\alpha +{\frac {1}{2}};{\frac {1-z}{2}}\right).$

Here (2α)

n

is the

rising factorial

. Explicitly,

$C_{n}^{(\alpha )}(z)=\sum _{k=0}^{\lfloor n/2\rfloor }(-1)^{k}{\frac {\Gamma (n-k+\alpha )}{\Gamma (\alpha )k!(n-2k)!}}(2z)^{n-2k}.$

From this it is also easy to obtain the value at unit argument:

$C_{n}^{(\alpha )}(1)={\frac {\Gamma (2\alpha +n)}{\Gamma (2\alpha )n!}}.$

- They are special cases of the Jacobi polynomials:

$C_{n}^{(\alpha )}(x)={\frac {(2\alpha )_{n}}{(\alpha +{\frac {1}{2}})_{n}}}P_{n}^{(\alpha -1/2,\alpha -1/2)}(x).$

in which

$(\theta )_{n}$

represents the

rising factorial

of

$\theta$

.

One therefore also has the

Rodrigues formula

$C_{n}^{(\alpha )}(x)={\frac {(-1)^{n}}{2^{n}n!}}{\frac {\Gamma (\alpha +{\frac {1}{2}})\Gamma (n+2\alpha )}{\Gamma (2\alpha )\Gamma (\alpha +n+{\frac {1}{2}})}}(1-x^{2})^{-\alpha +1/2}{\frac {d^{n}}{dx^{n}}}\left[(1-x^{2})^{n+\alpha -1/2}\right].$

- An alternative normalization sets $C_{n}^{(\alpha )}(1)=1$ . Assuming this alternative normalization, the derivatives of Gegenbauer are expressed in terms of Gegenbauer:

${\begin{aligned}{\frac {d^{q}}{dx^{q}}}C_{q+2j+1}^{(\alpha )}(x)={\frac {2^{q}(q+2j+1)!}{(q-1)!\Gamma (q+2j+2\alpha +1)}}&\sum _{i=0}^{j}{\frac {(2i+\alpha +1)\Gamma (2i+2\alpha +1)}{(2i+1)!(j-i)!}}\\&\times {\frac {\Gamma (q+j+i+\alpha +1)}{\Gamma (j+i+\alpha +2)}}(q+j-i-1)!C_{2i+1}^{(\alpha )}(x)\end{aligned}}$

## Orthogonality and normalization

For a fixed *α > -1/2*, the polynomials are orthogonal on [−1, 1] with respect to the weighting function

$w(z)=\left(1-z^{2}\right)^{\alpha -{\frac {1}{2}}}.$

To wit, for *n* ≠ *m*,

$\int _{-1}^{1}C_{n}^{(\alpha )}(x)C_{m}^{(\alpha )}(x)(1-x^{2})^{\alpha -{\frac {1}{2}}}\,dx=0.$

They are normalized by

$\int _{-1}^{1}\left[C_{n}^{(\alpha )}(x)\right]^{2}(1-x^{2})^{\alpha -{\frac {1}{2}}}\,dx={\frac {\pi 2^{1-2\alpha }\Gamma (n+2\alpha )}{n!(n+\alpha )[\Gamma (\alpha )]^{2}}}.$

## Applications

The Gegenbauer polynomials appear naturally as extensions of Legendre polynomials in the context of potential theory and harmonic analysis. The Newtonian potential in **R***n* has the expansion, valid with α = (*n* − 2)/2,

${\frac {1}{|\mathbf {x} -\mathbf {y} |^{n-2}}}=\sum _{k=0}^{\infty }{\frac {|\mathbf {x} |^{k}}{|\mathbf {y} |^{k+n-2}}}C_{k}^{(\alpha )}({\frac {\mathbf {x} \cdot \mathbf {y} }{|\mathbf {x} ||\mathbf {y} |}}).$

When *n* = 3, this gives the Legendre polynomial expansion of the gravitational potential. Similar expressions are available for the expansion of the Poisson kernel in a ball.

It follows that the quantities $C_{k}^{((n-2)/2)}(\mathbf {x} \cdot \mathbf {y} )$ are spherical harmonics, when regarded as a function of **x** only. They are, in fact, exactly the zonal spherical harmonics, up to a normalizing constant.

Gegenbauer polynomials also appear in the theory of positive-definite functions.

The Askey–Gasper inequality reads

$\sum _{j=0}^{n}{\frac {C_{j}^{\alpha }(x)}{2\alpha +j-1 \choose j}}\geq 0\qquad (x\geq -1,\,\alpha \geq 1/4).$

In spectral methods for solving differential equations, if a function is expanded in the basis of Chebyshev polynomials and its derivative is represented in a Gegenbauer/ultraspherical basis, then the derivative operator becomes a diagonal matrix, leading to fast banded matrix methods for large problems.

## Other properties

**Dirichlet–Mehler-type** integral representation: ${\frac {P_{n}^{(\alpha ,\alpha )}\left(\cos \theta \right)}{P_{n}^{(\alpha ,\alpha )}\left(1\right)}}={\frac {C_{n}^{(\alpha +{\frac {1}{2}})}\left(\cos \theta \right)}{C_{n}^{(\alpha +{\frac {1}{2}})}\left(1\right)}}={\frac {2^{\alpha +{\frac {1}{2}}}\Gamma \left(\alpha +1\right)}{{\pi }^{\frac {1}{2}}\Gamma \left(\alpha +{\frac {1}{2}}\right)}}(\sin \theta )^{-2\alpha }\int _{0}^{\theta }{\frac {\cos \left((n+\alpha +{\tfrac {1}{2}})\phi \right)}{(\cos \phi -\cos \theta )^{-\alpha +{\frac {1}{2}}}}}\,\mathrm {d} \phi ,$ **Laplace-type** integral representation ${\begin{aligned}{\frac {P_{n}^{(\alpha ,\alpha )}(\cos \theta )}{P_{n}^{(\alpha ,\alpha )}(1)}}&={\frac {C_{n}^{\left(\alpha +{\frac {1}{2}}\right)}(\cos \theta )}{C_{n}^{\left(\alpha +{\frac {1}{2}}\right)}(1)}}\\&={\frac {\Gamma (\alpha +1)}{\pi ^{\frac {1}{2}}\Gamma \left(\alpha +{\frac {1}{2}}\right)}}\int _{0}^{\pi }(\cos \theta +i\sin \theta \cos \phi )^{n}(\sin \phi )^{2\alpha }\mathrm {~d} \phi \end{aligned}}$ **Addition formula**:

${\begin{aligned}&C_{n}^{\lambda }\left(\cos \theta _{1}\cos \theta _{2}+\sin \theta _{1}\sin \theta _{2}\cos \phi \right)\\&\quad =\sum _{k=0}^{n}a_{n,k}^{\lambda }\left(\sin \theta _{1}\right)^{k}C_{n-k}^{\lambda +k}\left(\cos \theta _{1}\right)\left(\sin \theta _{2}\right)^{k}C_{n-k}^{\lambda +k}\left(\cos \theta _{2}\right)\\&\quad \cdot C_{k}^{\lambda -1/2}(\cos \phi ),\quad a_{n,k}^{\lambda }{\text{ constants }}\end{aligned}}$

## Asymptotics

Given fixed $\lambda \in (0,1),M\in \{1,2,\dots \},\delta \in (0,\pi /2)$ , uniformly for all $\theta \in [\delta ,\pi -\delta ]$ , for $n\to \infty$ , $C_{n}^{(\lambda )}\left(\cos \theta \right)={\frac {2^{2\lambda }\Gamma \left(\lambda +{\frac {1}{2}}\right)}{{\pi }^{\frac {1}{2}}\Gamma \left(\lambda +1\right)}}{\frac {\left(2\lambda \right)_{n}}{\left(\lambda +1\right)_{n}}}\left(\sum _{m=0}^{M-1}{\dfrac {{\left(\lambda \right)_{m}}{\left(1-\lambda \right)_{m}}}{m!\,{\left(n+\lambda +1\right)_{m}}}}{\dfrac {\cos \theta _{n,m}}{(2\sin \theta )^{m+\lambda }}}+R_{M}(\theta )\right)$

where $(\cdot )_{m}$ is the Pochhammer symbol, and $\theta _{n,m}=(n+m+\lambda )\theta -{\tfrac {1}{2}}(m+\lambda )\pi$ The remainder $R_{M}=O\left({\frac {1}{n^{M}}}\right)$ has an explicit upper bound: $|R_{M}(\theta )|\leq (2/\pi )\sin(\lambda \pi ){\frac {\Gamma (n+2\lambda )}{\Gamma (\lambda )}}{\frac {\Gamma (M+\lambda )\Gamma (M-\lambda +1)}{M!\Gamma (n+M+\lambda +1)}}{\frac {\max \left(|\cos \theta |^{-1},2\sin \theta \right)}{(2\sin \theta )^{M+\lambda }}}$ where $\Gamma$ is the Gamma function.

Other asymptotic formulas can be obtained as special cases of asymptotic formulas for the more general Jacobi polynomials.
