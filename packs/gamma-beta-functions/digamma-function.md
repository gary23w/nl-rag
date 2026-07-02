---
title: "Digamma function"
source: https://en.wikipedia.org/wiki/Digamma_function
domain: gamma-beta-functions
license: CC-BY-SA-4.0
tags: gamma function, beta function, digamma function, incomplete gamma function
fetched: 2026-07-02
---

# Digamma function

In mathematics, the **digamma function** is defined as the logarithmic derivative of the gamma function:

$\psi (z)={\frac {d}{dz}}\ln \Gamma (z)={\frac {\Gamma '(z)}{\Gamma (z)}}.$

It is the first of the polygamma functions. This function is strictly increasing and strictly concave on $(0,\infty )$ , and it asymptotically behaves as

$\psi (z)\sim \ln {z}-{\frac {1}{2z}},$

for complex numbers with large modulus ( $|z|\rightarrow \infty$ ) in the sector $\left|\arg z\right|<\pi -\varepsilon$ for any $\varepsilon >0$ .

The digamma function is often denoted as $\psi _{0}(x),\psi ^{(0)}(x)$ or Ϝ (the uppercase form of the archaic Greek letter digamma meaning double-gamma).

## Relation to harmonic numbers

The gamma function obeys the equation

$\Gamma (z+1)=z\Gamma (z).\,$

Taking the logarithm on both sides and using the functional equation property of the log-gamma function gives:

$\log \Gamma (z+1)=\log(z)+\log \Gamma (z),$

Differentiating both sides with respect to z gives:

$\psi (z+1)=\psi (z)+{\frac {1}{z}}$

Since the harmonic numbers are defined for positive integers n as

$H_{n}=\sum _{k=1}^{n}{\frac {1}{k}},$

the digamma function is related to them by

$\psi (n)=H_{n-1}-\gamma ,$

where *H*0 = 0, and γ is the Euler–Mascheroni constant. For half-integer arguments the digamma function takes the values

$\psi \left(n+{\tfrac {1}{2}}\right)=-\gamma -2\ln 2+\sum _{k=1}^{n}{\frac {2}{2k-1}}=-\gamma -2\ln 2+2H_{2n}-H_{n}.$

## Integral representations

If the real part of z is positive then the digamma function has the following integral representation due to Gauss:

$\psi (z)=\int _{0}^{\infty }\left({\frac {e^{-t}}{t}}-{\frac {e^{-zt}}{1-e^{-t}}}\right)\,dt.$

Combining this expression with an integral identity for the Euler–Mascheroni constant $\gamma$ gives:

$\psi (z+1)=-\gamma +\int _{0}^{1}\left({\frac {1-t^{z}}{1-t}}\right)\,dt.$

The integral is Euler's harmonic number $H_{z}$ , so the previous formula may also be written

$\psi (z+1)=\psi (1)+H_{z}.$

A consequence is the following generalization of the recurrence relation:

$\psi (w+1)-\psi (z+1)=H_{w}-H_{z}.$

An integral representation due to Dirichlet is:

$\psi (z)=\int _{0}^{\infty }\left(e^{-t}-{\frac {1}{(1+t)^{z}}}\right)\,{\frac {dt}{t}}.$

Gauss's integral representation can be manipulated to give the start of the asymptotic expansion of $\psi$ .

$\psi (z)=\log z-{\frac {1}{2z}}-\int _{0}^{\infty }\left({\frac {1}{2}}-{\frac {1}{t}}+{\frac {1}{e^{t}-1}}\right)e^{-tz}\,dt.$

This formula is also a consequence of Binet's first integral for the gamma function. The integral may be recognized as a Laplace transform.

Binet's second integral for the gamma function gives a different formula for $\psi$ which also gives the first few terms of the asymptotic expansion:

$\psi (z)=\log z-{\frac {1}{2z}}-2\int _{0}^{\infty }{\frac {t\,dt}{(t^{2}+z^{2})(e^{2\pi t}-1)}}.$

From the definition of $\psi$ and the integral representation of the gamma function, one obtains

$\psi (z)={\frac {1}{\Gamma (z)}}\int _{0}^{\infty }t^{z-1}\ln(t)e^{-t}\,dt,$

with $\Re z>0$ .

## Infinite product representation

The function $\psi (z)/\Gamma (z)$ is an entire function, and it can be represented by the infinite product

${\frac {\psi (z)}{\Gamma (z)}}=-e^{2\gamma z}\prod _{k=0}^{\infty }\left(1-{\frac {z}{x_{k}}}\right)e^{\frac {z}{x_{k}}}.$

Here $x_{k}$ is the *k*th zero of $\psi$ (see below), and $\gamma$ is the Euler–Mascheroni constant.

Note: This is also equal to $-{\frac {d}{dz}}{\frac {1}{\Gamma (z)}}$ due to the definition of the digamma function: ${\frac {\Gamma '(z)}{\Gamma (z)}}=\psi (z)$ .

## Series representation

### Series formula

Euler's product formula for the gamma function, combined with the functional equation and an identity for the Euler–Mascheroni constant, yields the following expression for the digamma function, valid in the complex plane outside the negative integers (Abramowitz and Stegun 6.3.16):

${\begin{aligned}\psi (z+1)&=-\gamma +\sum _{n=1}^{\infty }\left({\frac {1}{n}}-{\frac {1}{n+z}}\right),\qquad z\neq -1,-2,-3,\ldots ,\\&=-\gamma +\sum _{n=1}^{\infty }\left({\frac {z}{n(n+z)}}\right),\qquad z\neq -1,-2,-3,\ldots .\end{aligned}}$

Equivalently,

${\begin{aligned}\psi (z)&=-\gamma +\sum _{n=0}^{\infty }\left({\frac {1}{n+1}}-{\frac {1}{n+z}}\right),\qquad z\neq 0,-1,-2,\ldots ,\\&=-\gamma +\sum _{n=0}^{\infty }{\frac {z-1}{(n+1)(n+z)}},\qquad z\neq 0,-1,-2,\ldots .\end{aligned}}$

#### Evaluation of sums of rational functions

The above identity can be used to evaluate sums of the form

$\sum _{n=0}^{\infty }u_{n}=\sum _{n=0}^{\infty }{\frac {p(n)}{q(n)}},$

where *p*(*n*) and *q*(*n*) are polynomials of n.

Performing partial fraction decomposition on un in the complex field, in the case when all roots of *q*(*n*) are simple roots,

$u_{n}={\frac {p(n)}{q(n)}}=\sum _{k=1}^{m}{\frac {a_{k}}{n+b_{k}}}.$

For the series to converge,

$\lim _{n\to \infty }nu_{n}=0,$

otherwise the series will be greater than the harmonic series and thus diverge. Hence

$\sum _{k=1}^{m}a_{k}=0,$

and

${\begin{aligned}\sum _{n=0}^{\infty }u_{n}&=\sum _{n=0}^{\infty }\sum _{k=1}^{m}{\frac {a_{k}}{n+b_{k}}}\\&=\sum _{n=0}^{\infty }\sum _{k=1}^{m}a_{k}\left({\frac {1}{n+b_{k}}}-{\frac {1}{n+1}}\right)\\&=\sum _{k=1}^{m}\left(a_{k}\sum _{n=0}^{\infty }\left({\frac {1}{n+b_{k}}}-{\frac {1}{n+1}}\right)\right)\\&=-\sum _{k=1}^{m}a_{k}{\big (}\psi (b_{k})+\gamma {\big )}\\&=-\sum _{k=1}^{m}a_{k}\psi (b_{k}).\end{aligned}}$

With the series expansion of higher rank polygamma function a generalized formula can be given as

$\sum _{n=0}^{\infty }u_{n}=\sum _{n=0}^{\infty }\sum _{k=1}^{m}{\frac {a_{k}}{(n+b_{k})^{r_{k}}}}=\sum _{k=1}^{m}{\frac {(-1)^{r_{k}}}{(r_{k}-1)!}}a_{k}\psi ^{(r_{k}-1)}(b_{k}),$

provided the series on the left converges.

### Taylor series

The digamma has a rational zeta series, given by the Taylor series at *z* = 1. This is

$\psi (z+1)=-\gamma -\sum _{k=1}^{\infty }(-1)^{k}\,\zeta (k+1)\,z^{k},$

which converges for |*z*| < 1. Here, *ζ*(*n*) is the Riemann zeta function. This series is easily derived from the corresponding Taylor's series for the Hurwitz zeta function.

### Newton series

The Newton series for the digamma, sometimes referred to as *Stern series*, derived by Moritz Abraham Stern in 1847, reads

${\begin{aligned}\psi (s)&=-\gamma +(s-1)-{\frac {(s-1)(s-2)}{2\cdot 2!}}+{\frac {(s-1)(s-2)(s-3)}{3\cdot 3!}}\cdots ,\quad \Re (s)>0,\\&=-\gamma -\sum _{k=1}^{\infty }{\frac {(-1)^{k}}{k}}{\binom {s-1}{k}}\cdots ,\quad \Re (s)>0.\end{aligned}}$

where (*s* *k*) is the binomial coefficient. It may also be generalized to

$\psi (s+1)=-\gamma -{\frac {1}{m}}\sum _{k=1}^{m-1}{\frac {m-k}{s+k}}-{\frac {1}{m}}\sum _{k=1}^{\infty }{\frac {(-1)^{k}}{k}}\left\{{\binom {s+m}{k+1}}-{\binom {s}{k+1}}\right\},\qquad \Re (s)>-1,$

where *m* = 2, 3, 4, ...

### Series with Gregory's coefficients, Cauchy numbers and Bernoulli polynomials of the second kind

There exist various series for the digamma containing rational coefficients only for the rational arguments. In particular, the series with Gregory's coefficients *G**n* is

$\psi (v)=\ln v-\sum _{n=1}^{\infty }{\frac {{\big |}G_{n}{\big |}(n-1)!}{(v)_{n}}},\qquad \Re (v)>0,$

$\psi (v)=2\ln \Gamma (v)-2v\ln v+2v+2\ln v-\ln 2\pi -2\sum _{n=1}^{\infty }{\frac {{\big |}G_{n}(2){\big |}}{(v)_{n}}}\,(n-1)!,\qquad \Re (v)>0,$

$\psi (v)=3\ln \Gamma (v)-6\zeta '(-1,v)+3v^{2}\ln {v}-{\frac {3}{2}}v^{2}-6v\ln(v)+3v+3\ln {v}-{\frac {3}{2}}\ln 2\pi +{\frac {1}{2}}-3\sum _{n=1}^{\infty }{\frac {{\big |}G_{n}(3){\big |}}{(v)_{n}}}\,(n-1)!,\qquad \Re (v)>0,$

where (*v*)*n* is the *rising factorial* (*v*)*n* = *v*(*v*+1)(*v*+2) ... (*v*+*n*-1), *G**n*(*k*) are the Gregory coefficients of higher order with *G**n*(1) = *G**n*, Γ is the gamma function and ζ is the Hurwitz zeta function. Similar series with the Cauchy numbers of the second kind *C**n* reads

$\psi (v)=\ln(v-1)+\sum _{n=1}^{\infty }{\frac {C_{n}(n-1)!}{(v)_{n}}},\qquad \Re (v)>1,$

A series with the Bernoulli polynomials of the second kind has the following form

$\psi (v)=\ln(v+a)+\sum _{n=1}^{\infty }{\frac {(-1)^{n}\psi _{n}(a)\,(n-1)!}{(v)_{n}}},\qquad \Re (v)>-a,$

where *ψn*(*a*) are the *Bernoulli polynomials of the second kind* defined by the generating equation

${\frac {z(1+z)^{a}}{\ln(1+z)}}=\sum _{n=0}^{\infty }z^{n}\psi _{n}(a)\,,\qquad |z|<1\,,$

It may be generalized to

$\psi (v)={\frac {1}{r}}\sum _{l=0}^{r-1}\ln(v+a+l)+{\frac {1}{r}}\sum _{n=1}^{\infty }{\frac {(-1)^{n}N_{n,r}(a)(n-1)!}{(v)_{n}}},\qquad \Re (v)>-a,\quad r=1,2,3,\ldots$

where the polynomials *Nn,r*(*a*) are given by the following generating equation

${\frac {(1+z)^{a+m}-(1+z)^{a}}{\ln(1+z)}}=\sum _{n=0}^{\infty }N_{n,m}(a)z^{n},\qquad |z|<1,$

so that *Nn,1*(*a*) = *ψn*(*a*). Similar expressions with the logarithm of the gamma function involve these formulas

$\psi (v)={\frac {1}{v+a-{\tfrac {1}{2}}}}\left\{\ln \Gamma (v+a)+v-{\frac {1}{2}}\ln 2\pi -{\frac {1}{2}}+\sum _{n=1}^{\infty }{\frac {(-1)^{n}\psi _{n+1}(a)}{(v)_{n}}}(n-1)!\right\},\qquad \Re (v)>-a,$

and

$\psi (v)={\frac {1}{{\tfrac {1}{2}}r+v+a-1}}\left\{\ln \Gamma (v+a)+v-{\frac {1}{2}}\ln 2\pi -{\frac {1}{2}}+{\frac {1}{r}}\sum _{n=0}^{r-2}(r-n-1)\ln(v+a+n)+{\frac {1}{r}}\sum _{n=1}^{\infty }{\frac {(-1)^{n}N_{n+1,r}(a)}{(v)_{n}}}(n-1)!\right\},$

where $\Re (v)>-a$ and $r=2,3,4,\ldots$ .

## Reflection formula

The digamma and polygamma functions satisfy reflection formulas similar to that of the gamma function:

$\psi (1-x)-\psi (x)=\pi \cot \pi x$

.

$\psi '(-x)+\psi '(x)={\frac {\pi ^{2}}{\sin ^{2}(\pi x)}}+{\frac {1}{x^{2}}}$

.

$\psi ''(-x)-\psi ''(x)={\frac {2\pi ^{3}\cot(\pi x)}{\sin ^{2}(\pi x)}}+{\frac {2}{x^{3}}}$

.

## Recurrence formula and characterization

The digamma function satisfies the recurrence relation

$\psi (x+1)=\psi (x)+{\frac {1}{x}}.$

Thus, it can be said to "telescope" ⁠1/*x*⁠, for one has

$\Delta [\psi ](x)={\frac {1}{x}}$

where Δ is the forward difference operator. This satisfies the recurrence relation of a partial sum of the harmonic series, thus implying the formula

$\psi (n)=H_{n-1}-\gamma$

where γ is the Euler–Mascheroni constant.

Actually, ψ is the only solution of the functional equation

$F(x+1)=F(x)+{\frac {1}{x}}$

that is monotonic on **R**+ and satisfies *F*(1) = −*γ*. This fact follows immediately from the uniqueness of the Γ function given its recurrence equation and convexity restriction. This implies the useful difference equation:

$\psi (x+N)-\psi (x)=\sum _{k=0}^{N-1}{\frac {1}{x+k}}$

## Some finite sums involving the digamma function

There are numerous finite summation formulas for the digamma function. Basic summation formulas, such as

$\sum _{r=1}^{m}\psi \left({\frac {r}{m}}\right)=-m(\gamma +\ln m),$

$\sum _{r=1}^{m}\psi \left({\frac {r}{m}}\right)\cdot \exp {\dfrac {2\pi rki}{m}}=m\ln \left(1-\exp {\frac {2\pi ki}{m}}\right),\qquad k\in \mathbb {Z} ,\quad m\in \mathbb {N} ,\ k\neq m$

$\sum _{r=1}^{m-1}\psi \left({\frac {r}{m}}\right)\cdot \cos {\dfrac {2\pi rk}{m}}=m\ln \left(2\sin {\frac {k\pi }{m}}\right)+\gamma ,\qquad k=1,2,\ldots ,m-1$

$\sum _{r=1}^{m-1}\psi \left({\frac {r}{m}}\right)\cdot \sin {\frac {2\pi rk}{m}}={\frac {\pi }{2}}(2k-m),\qquad k=1,2,\ldots ,m-1$

are due to Gauss. More complicated formulas, such as

$\sum _{r=0}^{m-1}\psi \left({\frac {2r+1}{2m}}\right)\cdot \cos {\frac {(2r+1)k\pi }{m}}=m\ln \left(\tan {\frac {\pi k}{2m}}\right),\qquad k=1,2,\ldots ,m-1$

$\sum _{r=0}^{m-1}\psi \left({\frac {2r+1}{2m}}\right)\cdot \sin {\dfrac {(2r+1)k\pi }{m}}=-{\frac {\pi m}{2}},\qquad k=1,2,\ldots ,m-1$

$\sum _{r=1}^{m-1}\psi \left({\frac {r}{m}}\right)\cdot \cot {\frac {\pi r}{m}}=-{\frac {\pi (m-1)(m-2)}{6}}$

$\sum _{r=1}^{m-1}\psi \left({\frac {r}{m}}\right)\cdot {\frac {r}{m}}=-{\frac {\gamma }{2}}(m-1)-{\frac {m}{2}}\ln m-{\frac {\pi }{2}}\sum _{r=1}^{m-1}{\frac {r}{m}}\cdot \cot {\frac {\pi r}{m}}$

$\sum _{r=1}^{m-1}\psi \left({\frac {r}{m}}\right)\cdot \cos {\dfrac {(2\ell +1)\pi r}{m}}=-{\frac {\pi }{m}}\sum _{r=1}^{m-1}{\frac {r\cdot \sin {\dfrac {2\pi r}{m}}}{\cos {\dfrac {2\pi r}{m}}-\cos {\dfrac {(2\ell +1)\pi }{m}}}},\qquad \ell \in \mathbb {Z}$

$\sum _{r=1}^{m-1}\psi \left({\frac {r}{m}}\right)\cdot \sin {\dfrac {(2\ell +1)\pi r}{m}}=-(\gamma +\ln 2m)\cot {\frac {(2\ell +1)\pi }{2m}}+\sin {\dfrac {(2\ell +1)\pi }{m}}\sum _{r=1}^{m-1}{\frac {\ln \sin {\dfrac {\pi r}{m}}}{\cos {\dfrac {2\pi r}{m}}-\cos {\dfrac {(2\ell +1)\pi }{m}}}},\qquad \ell \in \mathbb {Z}$

$\sum _{r=1}^{m-1}\psi ^{2}\left({\frac {r}{m}}\right)=(m-1)\gamma ^{2}+m(2\gamma +\ln 4m)\ln {m}-m(m-1)\ln ^{2}2+{\frac {\pi ^{2}(m^{2}-3m+2)}{12}}+m\sum _{\ell =1}^{m-1}\ln ^{2}\sin {\frac {\pi \ell }{m}}$

are due to works of certain modern authors (see e.g. Appendix B in Blagouchine (2014)).

We also have

$1+{\frac {1}{2}}+{\frac {1}{3}}+...+{\frac {1}{k-1}}-\gamma -\ln k={\frac {1}{k}}\sum _{n=0}^{k-1}\psi \left(1+{\frac {n}{k}}\right),k=2,3,...$

## Gauss's digamma theorem

For positive integers r and m (*r* < *m*), the digamma function may be expressed in terms of Euler's constant and a finite number of elementary functions

$\psi \left({\frac {r}{m}}\right)=-\gamma -\ln(2m)-{\frac {\pi }{2}}\cot \left({\frac {r\pi }{m}}\right)+2\sum _{n=1}^{\left\lfloor {\frac {m-1}{2}}\right\rfloor }\cos \left({\frac {2\pi nr}{m}}\right)\ln \sin \left({\frac {\pi n}{m}}\right)$

which holds, because of its recurrence equation, for all rational arguments.

## Multiplication theorem

The multiplication theorem of the $\Gamma$ -function is equivalent to

$\psi (nz)={\frac {1}{n}}\sum _{k=0}^{n-1}\psi \left(z+{\frac {k}{n}}\right)+\ln n.$

## Asymptotic expansion

The digamma function has the asymptotic expansion

$\psi (z)\sim \ln z+\sum _{n=1}^{\infty }{\frac {\zeta (1-n)}{z^{n}}}=\ln z-\sum _{n=1}^{\infty }{\frac {B_{n}}{nz^{n}}},$

where *B**k* is the *k*th Bernoulli number and ζ is the Riemann zeta function. The first few terms of this expansion are:

$\psi (z)\sim \ln z-{\frac {1}{2z}}-{\frac {1}{12z^{2}}}+{\frac {1}{120z^{4}}}-{\frac {1}{252z^{6}}}+{\frac {1}{240z^{8}}}-{\frac {1}{132z^{10}}}+{\frac {691}{32760z^{12}}}-{\frac {1}{12z^{14}}}+\cdots .$

Although the infinite sum does not converge for any *z*, any finite partial sum becomes increasingly accurate as *z* increases.

The expansion can be found by applying the Euler–Maclaurin formula to the sum

$\sum _{n=1}^{\infty }\left({\frac {1}{n}}-{\frac {1}{z+n}}\right)$

The expansion can also be derived from the integral representation coming from Binet's second integral formula for the gamma function. Expanding $t/(t^{2}+z^{2})$ as a geometric series and substituting an integral representation of the Bernoulli numbers leads to the same asymptotic series as above. Furthermore, expanding only finitely many terms of the series gives a formula with an explicit error term:

$\psi (z)=\ln z-{\frac {1}{2z}}-\sum _{n=1}^{N}{\frac {B_{2n}}{2nz^{2n}}}+(-1)^{N+1}{\frac {2}{z^{2N}}}\int _{0}^{\infty }{\frac {t^{2N+1}\,dt}{(t^{2}+z^{2})(e^{2\pi t}-1)}}.$

## Inequalities

When *x* > 0, the function

$\ln x-{\frac {1}{2x}}-\psi (x)$

is completely monotonic and in particular positive. This is a consequence of Bernstein's theorem on monotone functions applied to the integral representation coming from Binet's first integral for the gamma function. Additionally, by the convexity inequality $1+t\leq e^{t}$ , the integrand in this representation is bounded above by $e^{-tz}/2$ . Consequently

${\frac {1}{x}}-\ln x+\psi (x)$

is also completely monotonic. It follows that, for all *x* > 0,

$\ln x-{\frac {1}{x}}\leq \psi (x)\leq \ln x-{\frac {1}{2x}}.$

This recovers a theorem of Horst Alzer. Alzer also proved that, for *s* ∈ (0, 1),

${\frac {1-s}{x+s}}<\psi (x+1)-\psi (x+s),$

Related bounds were obtained by Elezovic, Giordano, and Pecaric, who proved that, for *x* > 0 ,

$\ln(x+{\tfrac {1}{2}})-{\frac {1}{x}}<\psi (x)<\ln(x+e^{-\gamma })-{\frac {1}{x}},$

where $\gamma =-\psi (1)$ is the Euler–Mascheroni constant. The constants ( $0.5$ and $e^{-\gamma }\approx 0.56$ ) appearing in these bounds are the best possible.

The mean value theorem implies the following analog of Gautschi's inequality: If *x* > *c*, where *c* ≈ 1.461 is the unique positive real root of the digamma function, and if *s* > 0, then

$\exp \left((1-s){\frac {\psi '(x+1)}{\psi (x+1)}}\right)\leq {\frac {\psi (x+1)}{\psi (x+s)}}\leq \exp \left((1-s){\frac {\psi '(x+s)}{\psi (x+s)}}\right).$

Moreover, equality holds if and only if *s* = 1.

Inspired by the harmonic mean value inequality for the classical gamma function, Horzt Alzer and Graham Jameson proved, among other things, a harmonic mean-value inequality for the digamma function:

$-\gamma \leq {\frac {2\psi (x)\psi ({\frac {1}{x}})}{\psi (x)+\psi ({\frac {1}{x}})}}$ for $x>0$

Equality holds if and only if $x=1$ .

## Computation and approximation

The asymptotic expansion gives an easy way to compute *ψ*(*x*) when the real part of *x* is large. To compute *ψ*(*x*) for small x, the recurrence relation

$\psi (x+1)={\frac {1}{x}}+\psi (x)$

can be used to shift the value of x to a higher value. Beal suggests using the above recurrence to shift x to a value greater than 6 and then applying the above expansion with terms above *x*14 cut off, which yields "more than enough precision" (at least 12 digits except near the zeroes).

As x goes to infinity, *ψ*(*x*) gets arbitrarily close to both ln(*x* − ⁠1/2⁠) and ln *x*. Going down from *x* + 1 to x, ψ decreases by ⁠1/*x*⁠, ln(*x* − ⁠1/2⁠) decreases by ln(*x* + ⁠1/2⁠) / (*x* − ⁠1/2⁠), which is more than ⁠1/*x*⁠, and ln *x* decreases by ln(1 + ⁠1/*x*⁠), which is less than ⁠1/*x*⁠. From this we see that for any positive x greater than ⁠1/2⁠,

$\psi (x)\in \left(\ln \left(x-{\tfrac {1}{2}}\right),\ln x\right)$

or, for any positive x,

$\exp \psi (x)\in \left(x-{\tfrac {1}{2}},x\right).$

The exponential exp *ψ*(*x*) is approximately *x* − ⁠1/2⁠ for large x, but gets closer to x at small x, approaching 0 at *x* = 0.

For *x* < 1, we can calculate limits based on the fact that between 1 and 2, *ψ*(*x*) ∈ [−*γ*, 1 − *γ*], so

$\psi (x)\in \left(-{\frac {1}{x}}-\gamma ,1-{\frac {1}{x}}-\gamma \right),\quad x\in (0,1)$

or

$\exp \psi (x)\in \left(\exp \left(-{\frac {1}{x}}-\gamma \right),e\exp \left(-{\frac {1}{x}}-\gamma \right)\right).$

From the above asymptotic series for ψ, one can derive an asymptotic series for exp(−*ψ*(*x*)). The series matches the overall behaviour well, that is, it behaves asymptotically as it should for large arguments, and has a zero of unbounded multiplicity at the origin too.

${\frac {1}{\exp \psi (x)}}\sim {\frac {1}{x}}+{\frac {1}{2\cdot x^{2}}}+{\frac {5}{4\cdot 3!\cdot x^{3}}}+{\frac {3}{2\cdot 4!\cdot x^{4}}}+{\frac {47}{48\cdot 5!\cdot x^{5}}}-{\frac {5}{16\cdot 6!\cdot x^{6}}}+\cdots$

This is similar to a Taylor expansion of exp(−*ψ*(1 / *y*)) at *y* = 0, but it does not converge. (The function is not analytic at infinity.) A similar series exists for exp(*ψ*(*x*)) which starts with $\exp \psi (x)\sim x-{\frac {1}{2}}.$

If one calculates the asymptotic series for *ψ*(*x*+1/2) it turns out that there are no odd powers of x (there is no x−1 term). This leads to the following asymptotic expansion, which saves computing terms of even order.

$\exp \psi \left(x+{\tfrac {1}{2}}\right)\sim x+{\frac {1}{4!\cdot x}}-{\frac {37}{8\cdot 6!\cdot x^{3}}}+{\frac {10313}{72\cdot 8!\cdot x^{5}}}-{\frac {5509121}{384\cdot 10!\cdot x^{7}}}+\cdots$

Similar in spirit to the Lanczos approximation of the $\Gamma$ -function is Spouge's approximation.

Another alternative is to use the recurrence relation or the multiplication formula to shift the argument of $\psi (x)$ into the range $1\leq x\leq 3$ and to evaluate the Chebyshev series there.

## Special values

The digamma function has values in closed form for rational numbers, as a result of Gauss's digamma theorem. Some are listed below:

${\begin{aligned}\psi (1)&=-\gamma \\\psi \left({\tfrac {1}{2}}\right)&=-2\ln {2}-\gamma \\\psi \left({\tfrac {1}{3}}\right)&=-{\frac {\pi }{2{\sqrt {3}}}}-{\frac {3\ln {3}}{2}}-\gamma \\\psi \left({\tfrac {1}{4}}\right)&=-{\frac {\pi }{2}}-3\ln {2}-\gamma \\\psi \left({\tfrac {1}{6}}\right)&=-{\frac {\pi {\sqrt {3}}}{2}}-2\ln {2}-{\frac {3\ln {3}}{2}}-\gamma \\\psi \left({\tfrac {1}{8}}\right)&=-{\frac {\pi }{2}}-4\ln {2}-{\frac {\pi +\ln \left({\sqrt {2}}+1\right)-\ln \left({\sqrt {2}}-1\right)}{\sqrt {2}}}-\gamma .\end{aligned}}$

Moreover, by taking the logarithmic derivative of $|\Gamma (bi)|^{2}$ or $|\Gamma ({\tfrac {1}{2}}+bi)|^{2}$ where b is real-valued, it can easily be deduced that

$\operatorname {Im} \psi (bi)={\frac {1}{2b}}+{\frac {\pi }{2}}\coth(\pi b),$

$\operatorname {Im} \psi ({\tfrac {1}{2}}+bi)={\frac {\pi }{2}}\tanh(\pi b).$

Apart from Gauss's digamma theorem, no such closed formula is known for the real part in general. We have, for example, at the imaginary unit the numerical approximation OEIS: A248177

$\operatorname {Re} \psi (i)=-\gamma -\sum _{n=0}^{\infty }{\frac {n-1}{n^{3}+n^{2}+n+1}}\approx 0.09465.$

## Roots of the digamma function

The roots of the digamma function are the saddle points of the complex-valued gamma function. Thus they lie all on the real axis. The only one on the positive real axis is the unique minimum of the real-valued gamma function on **R**+ at *x*0 = 1.46163214496836234126.... All others occur single between the poles on the negative axis:

x

1

=

−0.504

083

008

264

455

409

25

...

x

2

=

−1.573

498

473

162

390

458

77

...

x

3

=

−2.610

720

868

444

144

650

00

...

x

4

=

−3.635

293

366

436

901

097

83

...

$\vdots$

Already in 1881, Charles Hermite observed that

$x_{n}=-n+{\frac {1}{\ln n}}+O\left({\frac {1}{(\ln n)^{2}}}\right)$

holds asymptotically. A better approximation of the location of the roots is given by

$x_{n}\approx -n+{\frac {1}{\pi }}\arctan \left({\frac {\pi }{\ln n}}\right)\qquad n\geq 2$

and using a further term it becomes still better

$x_{n}\approx -n+{\frac {1}{\pi }}\arctan \left({\frac {\pi }{\ln n+{\frac {1}{8n}}}}\right)\qquad n\geq 1$

which both spring off the reflection formula via

$0=\psi (1-x_{n})=\psi (x_{n})+{\frac {\pi }{\tan \pi x_{n}}}$

and substituting *ψ*(*xn*) by its not convergent asymptotic expansion. The correct second term of this expansion is ⁠1/2*n*⁠, where the given one works well to approximate roots with small n.

Another improvement of Hermite's formula can be given:

$x_{n}=-n+{\frac {1}{\log n}}-{\frac {1}{2n(\log n)^{2}}}+O\left({\frac {1}{n^{2}(\log n)^{2}}}\right).$

Regarding the zeros, the following infinite sum identities were recently proved by István Mező and Michael Hoffman

${\begin{aligned}\sum _{n=0}^{\infty }{\frac {1}{x_{n}^{2}}}&=\gamma ^{2}+{\frac {\pi ^{2}}{2}},\\\sum _{n=0}^{\infty }{\frac {1}{x_{n}^{3}}}&=-4\zeta (3)-\gamma ^{3}-{\frac {\gamma \pi ^{2}}{2}},\\\sum _{n=0}^{\infty }{\frac {1}{x_{n}^{4}}}&=\gamma ^{4}+{\frac {\pi ^{4}}{9}}+{\frac {2}{3}}\gamma ^{2}\pi ^{2}+4\gamma \zeta (3).\end{aligned}}$

In general, the function

$Z(k)=\sum _{n=0}^{\infty }{\frac {1}{x_{n}^{k}}}$

can be determined and it is studied in detail by the cited authors.

The following results

${\begin{aligned}\sum _{n=0}^{\infty }{\frac {1}{x_{n}^{2}+x_{n}}}&=-2,\\\sum _{n=0}^{\infty }{\frac {1}{x_{n}^{2}-x_{n}}}&=\gamma +{\frac {\pi ^{2}}{6\gamma }}\end{aligned}}$

also hold true.

## Regularization

The digamma function appears in the regularization of divergent integrals

$\int _{0}^{\infty }{\frac {dx}{x+a}},$

this integral can be approximated by a divergent general Harmonic series, but the following value can be attached to the series

$\sum _{n=0}^{\infty }{\frac {1}{n+a}}=-\psi (a).$

## In applied mathematics

Many notable probability distributions use the gamma function in the definition of their probability density or mass functions. Then in statistics when doing maximum likelihood estimation on models involving such distributions, the digamma function naturally appears when the derivative of the log-likelihood is taken for finding the maxima.
