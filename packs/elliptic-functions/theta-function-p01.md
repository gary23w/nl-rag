---
title: "Theta function (part 1/2)"
source: https://en.wikipedia.org/wiki/Theta_function
domain: elliptic-functions
license: CC-BY-SA-4.0
tags: elliptic function, jacobi elliptic functions, weierstrass elliptic function, theta function
fetched: 2026-07-02
part: 1/2
---

# Theta function

In mathematics, **theta functions** are special functions of several complex variables. Fundamentally, they are a family of *continuous* functions which encode the behavior of *discrete* multi-dimensional periodic systems, such as crystal lattices or points on a torus. Because they are smooth, they allow the study and manipulation of discrete combinatorial systems using the tools of analysis.

For this reason, theta functions have useful applications in topics such as

- number theory: "in how many ways can a number be written as a sum of squares?"
- physics: "how does heat flow on a toroidal ring?", "how do quantum particles behave when arranged in a lattice?"
- geometry: "what are the shape properties of elliptic curves?"

and others, including abelian varieties, moduli spaces, quadratic forms, and solitons.

Theta functions in two dimensions are functions of two complex arguments. In one choice of parameter, for example, z encodes position on a two-dimensional lattice, and $\tau$ or q encodes the shape of the lattice. In higher dimensions, the shape of the lattice is dictated by a matrix; in general, theta functions are parametrized by points in a tube domain inside a complex Lagrangian Grassmannian, namely the Siegel upper half space.


## Basic example

One example of a theta function is

$\theta (z,q)\equiv \sum _{n=-\infty }^{\infty }q^{n^{2}}\exp {(2\pi inz)}$

,

where z and q are complex numbers and $|q|<1$ so that the sum converges.

This analytic function can be used to solve a combinatorics problem: in how many different ways can an integer be written as the sum of two squares? When $z=0$ , we have

$\theta (0,q)=\sum _{n=-\infty }^{\infty }q^{n^{2}}=1+2q+2q^{4}+2q^{9}+\ldots +2q^{n^{2}}+\ldots$

This is a generating function where the coefficient of $q^{k}$ represents how many ways there are to write k as a perfect square: when $k=0$ , there is just one way. When k is any other perfect square, there are two ways: $n^{2}=(-n)^{2}$ . When k is not a perfect square, there are zero ways.

Squaring this generating function, we obtain

$\theta (0,q)^{2}={\Bigl (}\sum _{m}q^{m^{2}}{\Bigr )}{\Bigl (}\sum _{n}q^{n^{2}}{\Bigr )}=\sum _{m,n}q^{m^{2}+n^{2}}$

.

Collecting terms by exponent, we find that $\theta (0,q)^{2}$ is a generating function where the coefficient of $q^{k}$ counts how many ways there are to write k as the sum of any two squares. This count includes negative integers and order, such that $(3,4)$ , $(4,3)$ , and $(-3,4)$ : each count as separate ways of making $3^{2}+4^{2}=25$ .

### Application to elliptic functions

Theta functions occur most commonly in the theory of elliptic functions. With respect to one of the complex variables z , a theta function has a property expressing its behavior with respect to the addition of a period of the associated elliptic functions, making it a quasiperiodic function. Abstractly, this quasiperiodicity comes from the cohomology class of a line bundle on a complex torus, a condition of descent.

One interpretation of theta functions when dealing with the heat equation is that "a theta function is a special function that describes the evolution of temperature on a segment domain subject to certain boundary conditions".

Throughout this article, $(e^{\pi i\tau })^{\alpha }$ should be interpreted as $e^{\alpha \pi i\tau }$ (in order to resolve issues of choice of branch).


## Jacobi theta function

There are several closely related functions called Jacobi theta functions, and many different and incompatible systems of notation for them. One **Jacobi theta function** (named after Carl Gustav Jacob Jacobi) is a function defined for two complex variables z and τ, where z can be any complex number and τ is the half-period ratio, confined to the upper half-plane, which means it has a positive imaginary part. It is given by the formula

${\begin{aligned}\vartheta (z;\tau )&=\sum _{n=-\infty }^{\infty }\exp \left(\pi in^{2}\tau +2\pi inz\right)\\&=1+2\sum _{n=1}^{\infty }q^{n^{2}}\cos(2\pi nz)\\&=\sum _{n=-\infty }^{\infty }q^{n^{2}}\eta ^{n}\end{aligned}}$

where *q* = exp(*πiτ*) is the nome and *η* = exp(2*πiz*). It is a Jacobi form. The restriction ensures that it is an absolutely convergent series. At fixed τ, this is a Fourier series for a 1-periodic entire function of z. Accordingly, the theta function is 1-periodic in z:

$\vartheta (z+1;\tau )=\vartheta (z;\tau ).$

By completing the square, it is also τ-quasiperiodic in z, with

$\vartheta (z+\tau ;\tau )=\exp {\bigl (}-\pi i(\tau +2z){\bigr )}\vartheta (z;\tau ).$

Thus, in general,

$\vartheta (z+a+b\tau ;\tau )=\exp \left(-\pi ib^{2}\tau -2\pi ibz\right)\vartheta (z;\tau )$

for any integers a and b.

For any fixed $\tau$ , the function is an entire function on the complex plane, so by Liouville's theorem, it cannot be doubly periodic in $1,\tau$ unless it is constant, and so the best we can do is to make it periodic in 1 and quasi-periodic in $\tau$ . Indeed, since $\left|{\frac {\vartheta (z+a+b\tau ;\tau )}{\vartheta (z;\tau )}}\right|=\exp \left(\pi (b^{2}\Im (\tau )+2b\Im (z))\right)$ and $\Im (\tau )>0$ , the function $\vartheta (z,\tau )$ is unbounded, as required by Liouville's theorem.

It is in fact the most general entire function with 2 quasi-periods, in the following sense:

**Theorem**—If $f:\mathbb {C} \to \mathbb {C}$ is entire and nonconstant, and satisfies the functional equations ${\begin{cases}f(z+1)=f(z)\\f(z+\tau )=e^{az+2\pi ib}f(z)\end{cases}}$ for some constant $a,b\in \mathbb {C}$ .

If $a=0$ , then $b=\tau$ and $f(z)=e^{2\pi iz}$ . If $a=-2\pi i$ , then $f(z)=C\vartheta (z+{\frac {1}{2}}\tau +b,\tau )$ for some nonzero $C\in \mathbb {C}$ .


## Auxiliary functions

The Jacobi theta function defined above is sometimes considered along with three auxiliary theta functions, in which case it is written with a double 0 subscript:

$\vartheta _{00}(z;\tau )=\vartheta (z;\tau )$

The auxiliary (or half-period) functions are defined by

${\begin{aligned}\vartheta _{01}(z;\tau )&=\vartheta \left(z+{\tfrac {1}{2}};\tau \right)\\[3pt]\vartheta _{10}(z;\tau )&=\exp \left({\tfrac {1}{4}}\pi i\tau +\pi iz\right)\vartheta \left(z+{\tfrac {1}{2}}\tau ;\tau \right)\\[3pt]\vartheta _{11}(z;\tau )&=\exp \left({\tfrac {1}{4}}\pi i\tau +\pi i\left(z+{\tfrac {1}{2}}\right)\right)\vartheta \left(z+{\tfrac {1}{2}}\tau +{\tfrac {1}{2}};\tau \right).\end{aligned}}$

This notation follows Riemann and Mumford; Jacobi's original formulation was in terms of the nome *q* = *e**iπτ* rather than τ. In Jacobi's notation the θ-functions are written:

${\begin{aligned}\theta _{1}(z;q)&=\theta _{1}(\pi z,q)=-\vartheta _{11}(z;\tau )\\\theta _{2}(z;q)&=\theta _{2}(\pi z,q)=\vartheta _{10}(z;\tau )\\\theta _{3}(z;q)&=\theta _{3}(\pi z,q)=\vartheta _{00}(z;\tau )\\\theta _{4}(z;q)&=\theta _{4}(\pi z,q)=\vartheta _{01}(z;\tau )\end{aligned}}$

The above definitions of the Jacobi theta functions are by no means unique. See Jacobi theta functions (notational variations) for further discussion.

If we set *z* = 0 in the above theta functions, we obtain four functions of τ only, defined on the upper half-plane. These functions are called *Theta Nullwert* functions, based on the German term for *zero value* because of the annullation of the left entry in the theta function expression. Alternatively, we obtain four functions of q only, defined on the unit disk $|q|<1$ . They are sometimes called theta constants:

${\begin{aligned}\vartheta _{11}(0;\tau )&=-\theta _{1}(q)=-\sum _{n=-\infty }^{\infty }(-1)^{n-1/2}q^{(n+1/2)^{2}}\\\vartheta _{10}(0;\tau )&=\theta _{2}(q)=\sum _{n=-\infty }^{\infty }q^{(n+1/2)^{2}}\\\vartheta _{00}(0;\tau )&=\theta _{3}(q)=\sum _{n=-\infty }^{\infty }q^{n^{2}}\\\vartheta _{01}(0;\tau )&=\theta _{4}(q)=\sum _{n=-\infty }^{\infty }(-1)^{n}q^{n^{2}}\end{aligned}}$

with the nome *q* = *e**iπτ*. Observe that $\theta _{1}(q)=0$ . These can be used to define a variety of modular forms, and to parametrize certain curves; in particular, the **Jacobi identity** is

$\theta _{2}(q)^{4}+\theta _{4}(q)^{4}=\theta _{3}(q)^{4}$

or equivalently,

$\vartheta _{01}(0;\tau )^{4}+\vartheta _{10}(0;\tau )^{4}=\vartheta _{00}(0;\tau )^{4}$

which is the Fermat curve of degree four.


## Jacobi identities

Jacobi's identities describe how theta functions transform under the modular group, which is generated by *τ* ↦ *τ* + 1 and *τ* ↦ −⁠1/*τ*⁠. Equations for the first transform are easily found since adding one to τ in the exponent has the same effect as adding ⁠1/2⁠ to z (*n* ≡ *n*2 mod 2). For the second, let

$\alpha =(-i\tau )^{\frac {1}{2}}\exp \left({\frac {\pi }{\tau }}iz^{2}\right).$

Then

${\begin{aligned}\vartheta _{00}\!\left({\frac {z}{\tau }};{\frac {-1}{\tau }}\right)&=\alpha \,\vartheta _{00}(z;\tau )\quad &\vartheta _{01}\!\left({\frac {z}{\tau }};{\frac {-1}{\tau }}\right)&=\alpha \,\vartheta _{10}(z;\tau )\\[3pt]\vartheta _{10}\!\left({\frac {z}{\tau }};{\frac {-1}{\tau }}\right)&=\alpha \,\vartheta _{01}(z;\tau )\quad &\vartheta _{11}\!\left({\frac {z}{\tau }};{\frac {-1}{\tau }}\right)&=-i\alpha \,\vartheta _{11}(z;\tau ).\end{aligned}}$


## Theta functions in terms of the nome

Instead of expressing the Theta functions in terms of z and τ, we may express them in terms of arguments w and the nome q, where *w* = *e**πiz* and *q* = *e**πiτ*. In this form, the functions become

${\begin{aligned}\vartheta _{00}(w,q)&=\sum _{n=-\infty }^{\infty }\left(w^{2}\right)^{n}q^{n^{2}}\quad &\vartheta _{01}(w,q)&=\sum _{n=-\infty }^{\infty }(-1)^{n}\left(w^{2}\right)^{n}q^{n^{2}}\\[3pt]\vartheta _{10}(w,q)&=\sum _{n=-\infty }^{\infty }\left(w^{2}\right)^{n+{\frac {1}{2}}}q^{\left(n+{\frac {1}{2}}\right)^{2}}\quad &\vartheta _{11}(w,q)&=i\sum _{n=-\infty }^{\infty }(-1)^{n}\left(w^{2}\right)^{n+{\frac {1}{2}}}q^{\left(n+{\frac {1}{2}}\right)^{2}}.\end{aligned}}$

We see that the theta functions can also be defined in terms of w and q, without a direct reference to the exponential function. These formulas can, therefore, be used to define the Theta functions over other fields where the exponential function might not be everywhere defined, such as fields of p-adic numbers.


## Product representations

The Jacobi triple product (a special case of the Macdonald identities) tells us that for complex numbers w and q with |*q*| < 1 and *w* ≠ 0 we have

$\prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1+w^{2}q^{2m-1}\right)\left(1+w^{-2}q^{2m-1}\right)=\sum _{n=-\infty }^{\infty }w^{2n}q^{n^{2}}.$

It can be proven by elementary means, as for instance in Hardy and Wright's *An Introduction to the Theory of Numbers*.

If we express the theta function in terms of the nome *q* = *e**πiτ* (noting some authors instead set *q* = *e*2*πiτ*) and take *w* = *e**πiz* then

$\vartheta (z;\tau )=\sum _{n=-\infty }^{\infty }\exp(\pi i\tau n^{2})\exp(2\pi izn)=\sum _{n=-\infty }^{\infty }w^{2n}q^{n^{2}}.$

We therefore obtain a product formula for the theta function in the form

$\vartheta (z;\tau )=\prod _{m=1}^{\infty }{\big (}1-\exp(2m\pi i\tau ){\big )}{\Big (}1+\exp {\big (}(2m-1)\pi i\tau +2\pi iz{\big )}{\Big )}{\Big (}1+\exp {\big (}(2m-1)\pi i\tau -2\pi iz{\big )}{\Big )}.$

In terms of w and q:

${\begin{aligned}\vartheta (z;\tau )&=\prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1+q^{2m-1}w^{2}\right)\left(1+{\frac {q^{2m-1}}{w^{2}}}\right)\\&=\left(q^{2};q^{2}\right)_{\infty }\,\left(-w^{2}q;q^{2}\right)_{\infty }\,\left(-{\frac {q}{w^{2}}};q^{2}\right)_{\infty }\\&=\left(q^{2};q^{2}\right)_{\infty }\,\theta \left(-w^{2}q;q^{2}\right)\end{aligned}}$

where (  ;  )∞ is the q-Pochhammer symbol and *θ*(  ;  ) is the q-theta function. Expanding terms out, the Jacobi triple product can also be written

$\prod _{m=1}^{\infty }\left(1-q^{2m}\right){\Big (}1+\left(w^{2}+w^{-2}\right)q^{2m-1}+q^{4m-2}{\Big )},$

which we may also write as

$\vartheta (z\mid q)=\prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1+2\cos(2\pi z)q^{2m-1}+q^{4m-2}\right).$

This form is valid in general but clearly is of particular interest when z is real. Similar product formulas for the auxiliary theta functions are

${\begin{aligned}\vartheta _{01}(z\mid q)&=\prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1-2\cos(2\pi z)q^{2m-1}+q^{4m-2}\right),\\[3pt]\vartheta _{10}(z\mid q)&=2q^{\frac {1}{4}}\cos(\pi z)\prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1+2\cos(2\pi z)q^{2m}+q^{4m}\right),\\[3pt]\vartheta _{11}(z\mid q)&=-2q^{\frac {1}{4}}\sin(\pi z)\prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1-2\cos(2\pi z)q^{2m}+q^{4m}\right).\end{aligned}}$

In particular, $\lim _{q\to 0}{\frac {\vartheta _{10}(z\mid q)}{2q^{\frac {1}{4}}}}=\cos(\pi z),\quad \lim _{q\to 0}{\frac {-\vartheta _{11}(z\mid q)}{2q^{\frac {1}{4}}}}=\sin(\pi z)$ so we may interpret them as one-parameter deformations of the periodic functions $\sin ,\cos$ , again validating the interpretation of the theta function as the most general 2 quasi-period function.


## Integral representations

The Jacobi theta functions have the following integral representations:

${\begin{aligned}\vartheta _{00}(z;\tau )&=-i\int _{i-\infty }^{i+\infty }e^{i\pi \tau u^{2}}{\frac {\cos(2\pi uz+\pi u)}{\sin(\pi u)}}\mathrm {d} u;\\[6pt]\vartheta _{01}(z;\tau )&=-i\int _{i-\infty }^{i+\infty }e^{i\pi \tau u^{2}}{\frac {\cos(2\pi uz)}{\sin(\pi u)}}\mathrm {d} u;\\[6pt]\vartheta _{10}(z;\tau )&=-ie^{i\pi z+{\frac {1}{4}}i\pi \tau }\int _{i-\infty }^{i+\infty }e^{i\pi \tau u^{2}}{\frac {\cos(2\pi uz+\pi u+\pi \tau u)}{\sin(\pi u)}}\mathrm {d} u;\\[6pt]\vartheta _{11}(z;\tau )&=e^{i\pi z+{\frac {1}{4}}i\pi \tau }\int _{i-\infty }^{i+\infty }e^{i\pi \tau u^{2}}{\frac {\cos(2\pi uz+\pi \tau u)}{\sin(\pi u)}}\mathrm {d} u.\end{aligned}}$

The Theta Nullwert function $\theta _{3}(q)$ as this integral identity:

$\theta _{3}(q)=1+{\frac {4q{\sqrt {\ln(1/q)}}}{\sqrt {\pi }}}\int _{0}^{\infty }{\frac {\exp[-\ln(1/q)\,x^{2}]\{1-q^{2}\cos[2\ln(1/q)\,x]\}}{1-2q^{2}\cos[2\ln(1/q)\,x]+q^{4}}}\,\mathrm {d} x$

This formula was discussed in the essay *Square series generating function transformations* by the mathematician Maxie Schmidt from Georgia in Atlanta.

Based on this formula following three eminent examples are given:

${\biggl [}{\frac {2}{\pi }}K{\bigl (}{\frac {1}{2}}{\sqrt {2}}{\bigr )}{\biggr ]}^{1/2}=\theta _{3}{\bigl [}\exp(-\pi ){\bigr ]}=1+4\exp(-\pi )\int _{0}^{\infty }{\frac {\exp(-\pi x^{2})[1-\exp(-2\pi )\cos(2\pi x)]}{1-2\exp(-2\pi )\cos(2\pi x)+\exp(-4\pi )}}\,\mathrm {d} x$

${\biggl [}{\frac {2}{\pi }}K({\sqrt {2}}-1){\biggr ]}^{1/2}=\theta _{3}{\bigl [}\exp(-{\sqrt {2}}\,\pi ){\bigr ]}=1+4\,{\sqrt[{4}]{2}}\exp(-{\sqrt {2}}\,\pi )\int _{0}^{\infty }{\frac {\exp(-{\sqrt {2}}\,\pi x^{2})[1-\exp(-2{\sqrt {2}}\,\pi )\cos(2{\sqrt {2}}\,\pi x)]}{1-2\exp(-2{\sqrt {2}}\,\pi )\cos(2{\sqrt {2}}\,\pi x)+\exp(-4{\sqrt {2}}\,\pi )}}\,\mathrm {d} x$

${\biggl \{}{\frac {2}{\pi }}K{\bigl [}\sin {\bigl (}{\frac {\pi }{12}}{\bigr )}{\bigr ]}{\biggr \}}^{1/2}=\theta _{3}{\bigl [}\exp(-{\sqrt {3}}\,\pi ){\bigr ]}=1+4\,{\sqrt[{4}]{3}}\exp(-{\sqrt {3}}\,\pi )\int _{0}^{\infty }{\frac {\exp(-{\sqrt {3}}\,\pi x^{2})[1-\exp(-2{\sqrt {3}}\,\pi )\cos(2{\sqrt {3}}\,\pi x)]}{1-2\exp(-2{\sqrt {3}}\,\pi )\cos(2{\sqrt {3}}\,\pi x)+\exp(-4{\sqrt {3}}\,\pi )}}\,\mathrm {d} x$

Furthermore, the theta examples $\theta _{3}({\tfrac {1}{2}})$ and $\theta _{3}({\tfrac {1}{3}})$ shall be displayed:

$\theta _{3}\left({\frac {1}{2}}\right)=1+2\sum _{n=1}^{\infty }{\frac {1}{2^{n^{2}}}}=1+2\pi ^{-1/2}{\sqrt {\ln(2)}}\int _{0}^{\infty }{\frac {\exp[-\ln(2)\,x^{2}]\{16-4\cos[2\ln(2)\,x]\}}{17-8\cos[2\ln(2)\,x]}}\,\mathrm {d} x$

$\theta _{3}\left({\frac {1}{2}}\right)=2.128936827211877158669\ldots$

$\theta _{3}\left({\frac {1}{3}}\right)=1+2\sum _{n=1}^{\infty }{\frac {1}{3^{n^{2}}}}=1+{\frac {4}{3}}\pi ^{-1/2}{\sqrt {\ln(3)}}\int _{0}^{\infty }{\frac {\exp[-\ln(3)\,x^{2}]\{81-9\cos[2\ln(3)\,x]\}}{82-18\cos[2\ln(3)\,x]}}\,\mathrm {d} x$

$\theta _{3}\left({\frac {1}{3}}\right)=1.691459681681715341348\ldots$


## Explicit values

### Lemniscatic values

Proper credit for most of these results goes to Ramanujan. See Ramanujan's lost notebook and a relevant reference at Euler function. The Ramanujan results quoted at Euler function plus a few elementary operations give the results below, so they are either in Ramanujan's lost notebook or follow immediately from it. See also Yi (2004). Define,

$\quad \varphi (q)=\vartheta _{00}(0;\tau )=\theta _{3}(0;q)=\sum _{n=-\infty }^{\infty }q^{n^{2}}$

with the nome $q=e^{\pi i\tau },$ $\tau =n{\sqrt {-1}},$ and Dedekind eta function $\eta (\tau ).$ Then for $n=1,2,3,\dots$

${\begin{aligned}\varphi \left(e^{-\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}={\sqrt {2}}\,\eta \left({\sqrt {-1}}\right)\\\varphi \left(e^{-2\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {\sqrt {2+{\sqrt {2}}}}{2}}\\\varphi \left(e^{-3\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {\sqrt {1+{\sqrt {3}}}}{\sqrt[{8}]{108}}}\\\varphi \left(e^{-4\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {2+{\sqrt[{4}]{8}}}{4}}\\\varphi \left(e^{-5\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\sqrt {\frac {2+{\sqrt {5}}}{5}}}\\\varphi \left(e^{-6\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {\sqrt {{\sqrt[{4}]{1}}+{\sqrt[{4}]{3}}+{\sqrt[{4}]{4}}+{\sqrt[{4}]{9}}}}{\sqrt[{8}]{12^{3}}}}\\\varphi \left(e^{-7\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {\sqrt {{\sqrt {13+{\sqrt {7}}}}+{\sqrt {7+3{\sqrt {7}}}}}}{{\sqrt[{8}]{14^{3}}}\cdot {\sqrt[{16}]{7}}}}\\\varphi \left(e^{-8\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {{\sqrt {2+{\sqrt {2}}}}+{\sqrt[{8}]{128}}}{4}}\\\varphi \left(e^{-9\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {1+{\sqrt[{3}]{2+2{\sqrt {3}}}}}{3}}\\\varphi \left(e^{-10\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {\sqrt {{\sqrt[{4}]{64}}+{\sqrt[{4}]{80}}+{\sqrt[{4}]{81}}+{\sqrt[{4}]{100}}}}{\sqrt[{4}]{200}}}\\\varphi \left(e^{-11\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {\sqrt {11+{\sqrt {11}}+(5+3{\sqrt {3}}+{\sqrt {11}}+{\sqrt {33}}){\sqrt[{3}]{-44+33{\sqrt {3}}}}+(-5+3{\sqrt {3}}-{\sqrt {11}}+{\sqrt {33}}){\sqrt[{3}]{44+33{\sqrt {3}}}}}}{\sqrt[{8}]{52180524}}}\\\varphi \left(e^{-12\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {\sqrt {{\sqrt[{4}]{1}}+{\sqrt[{4}]{2}}+{\sqrt[{4}]{3}}+{\sqrt[{4}]{4}}+{\sqrt[{4}]{9}}+{\sqrt[{4}]{18}}+{\sqrt[{4}]{24}}}}{2{\sqrt[{8}]{108}}}}\\\varphi \left(e^{-13\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {\sqrt {13+8{\sqrt {13}}+(11-6{\sqrt {3}}+{\sqrt {13}}){\sqrt[{3}]{143+78{\sqrt {3}}}}+(11+6{\sqrt {3}}+{\sqrt {13}}){\sqrt[{3}]{143-78{\sqrt {3}}}}}}{\sqrt[{4}]{19773}}}\\\varphi \left(e^{-14\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {\sqrt {{\sqrt {13+{\sqrt {7}}}}+{\sqrt {7+3{\sqrt {7}}}}+{\sqrt {10+2{\sqrt {7}}}}+{\sqrt[{8}]{28}}{\sqrt {4+{\sqrt {7}}}}}}{\sqrt[{16}]{28^{7}}}}\\\varphi \left(e^{-15\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {\sqrt {7+3{\sqrt {3}}+{\sqrt {5}}+{\sqrt {15}}+{\sqrt[{4}]{60}}+{\sqrt[{4}]{1500}}}}{{\sqrt[{8}]{12^{3}}}\cdot {\sqrt {5}}}}\\2\varphi \left(e^{-16\pi }\right)&=\varphi \left(e^{-4\pi }\right)+{\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {\sqrt[{4}]{1+{\sqrt {2}}}}{\sqrt[{16}]{128}}}\\\varphi \left(e^{-17\pi }\right)&={\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\frac {{\sqrt {2}}(1+{\sqrt[{4}]{17}})+{\sqrt[{8}]{17}}{\sqrt {5+{\sqrt {17}}}}}{\sqrt {17+17{\sqrt {17}}}}}\\2\varphi \left(e^{-20\pi }\right)&=\varphi \left(e^{-5\pi }\right)+{\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\sqrt {\frac {3+2{\sqrt[{4}]{5}}}{5{\sqrt {2}}}}}\\6\varphi \left(e^{-36\pi }\right)&=3\varphi \left(e^{-9\pi }\right)+2\varphi \left(e^{-4\pi }\right)-\varphi \left(e^{-\pi }\right)+{\frac {\sqrt[{4}]{\pi }}{\Gamma \left({\frac {3}{4}}\right)}}{\sqrt[{3}]{{\sqrt[{4}]{2}}+{\sqrt[{4}]{18}}+{\sqrt[{4}]{216}}}}\end{aligned}}$

If the reciprocal of the Gelfond constant is raised to the power of the reciprocal of an odd number, then the corresponding $\vartheta _{00}$ values or $\phi$ values can be represented in a simplified way by using the hyperbolic lemniscatic sine:

$\varphi {\bigl [}\exp(-{\tfrac {1}{5}}\pi ){\bigr ]}={\sqrt[{4}]{\pi }}\,{\Gamma \left({\tfrac {3}{4}}\right)}^{-1}\operatorname {slh} {\bigl (}{\tfrac {1}{5}}{\sqrt {2}}\,\varpi {\bigr )}\operatorname {slh} {\bigl (}{\tfrac {2}{5}}{\sqrt {2}}\,\varpi {\bigr )}$

$\varphi {\bigl [}\exp(-{\tfrac {1}{7}}\pi ){\bigr ]}={\sqrt[{4}]{\pi }}\,{\Gamma \left({\tfrac {3}{4}}\right)}^{-1}\operatorname {slh} {\bigl (}{\tfrac {1}{7}}{\sqrt {2}}\,\varpi {\bigr )}\operatorname {slh} {\bigl (}{\tfrac {2}{7}}{\sqrt {2}}\,\varpi {\bigr )}\operatorname {slh} {\bigl (}{\tfrac {3}{7}}{\sqrt {2}}\,\varpi {\bigr )}$

$\varphi {\bigl [}\exp(-{\tfrac {1}{9}}\pi ){\bigr ]}={\sqrt[{4}]{\pi }}\,{\Gamma \left({\tfrac {3}{4}}\right)}^{-1}\operatorname {slh} {\bigl (}{\tfrac {1}{9}}{\sqrt {2}}\,\varpi {\bigr )}\operatorname {slh} {\bigl (}{\tfrac {2}{9}}{\sqrt {2}}\,\varpi {\bigr )}\operatorname {slh} {\bigl (}{\tfrac {3}{9}}{\sqrt {2}}\,\varpi {\bigr )}\operatorname {slh} {\bigl (}{\tfrac {4}{9}}{\sqrt {2}}\,\varpi {\bigr )}$

$\varphi {\bigl [}\exp(-{\tfrac {1}{11}}\pi ){\bigr ]}={\sqrt[{4}]{\pi }}\,{\Gamma \left({\tfrac {3}{4}}\right)}^{-1}\operatorname {slh} {\bigl (}{\tfrac {1}{11}}{\sqrt {2}}\,\varpi {\bigr )}\operatorname {slh} {\bigl (}{\tfrac {2}{11}}{\sqrt {2}}\,\varpi {\bigr )}\operatorname {slh} {\bigl (}{\tfrac {3}{11}}{\sqrt {2}}\,\varpi {\bigr )}\operatorname {slh} {\bigl (}{\tfrac {4}{11}}{\sqrt {2}}\,\varpi {\bigr )}\operatorname {slh} {\bigl (}{\tfrac {5}{11}}{\sqrt {2}}\,\varpi {\bigr )}$

With the letter $\varpi$ the Lemniscate constant is represented.

Note that the following modular identities hold:

${\begin{aligned}2\varphi \left(q^{4}\right)&=\varphi (q)+{\sqrt {2\varphi ^{2}\left(q^{2}\right)-\varphi ^{2}(q)}}\\3\varphi \left(q^{9}\right)&=\varphi (q)+{\sqrt[{3}]{9{\frac {\varphi ^{4}\left(q^{3}\right)}{\varphi (q)}}-\varphi ^{3}(q)}}\\{\sqrt {5}}\varphi \left(q^{25}\right)&=\varphi \left(q^{5}\right)\cot \left({\frac {1}{2}}\arctan \left({\frac {2}{\sqrt {5}}}{\frac {\varphi (q)\varphi \left(q^{5}\right)}{\varphi ^{2}(q)-\varphi ^{2}\left(q^{5}\right)}}{\frac {1+s(q)-s^{2}(q)}{s(q)}}\right)\right)\end{aligned}}$

where $s(q)=s\left(e^{\pi i\tau }\right)=-R\left(-e^{-\pi i/(5\tau )}\right)$ is the Rogers–Ramanujan continued fraction:

${\begin{aligned}s(q)&={\sqrt[{5}]{\tan \left({\frac {1}{2}}\arctan \left({\frac {5}{2}}{\frac {\varphi ^{2}\left(q^{5}\right)}{\varphi ^{2}(q)}}-{\frac {1}{2}}\right)\right)\cot ^{2}\left({\frac {1}{2}}\operatorname {arccot} \left({\frac {5}{2}}{\frac {\varphi ^{2}\left(q^{5}\right)}{\varphi ^{2}(q)}}-{\frac {1}{2}}\right)\right)}}\\&={\cfrac {e^{-\pi i/(25\tau )}}{1-{\cfrac {e^{-\pi i/(5\tau )}}{1+{\cfrac {e^{-2\pi i/(5\tau )}}{1-\ddots }}}}}}\end{aligned}}$

### Equianharmonic values

The mathematician Bruce Berndt found out further values of the theta function:

${\begin{array}{lll}\varphi \left(\exp(-{\sqrt {3}}\,\pi )\right)&=&\pi ^{-1}{\Gamma \left({\tfrac {4}{3}}\right)}^{3/2}2^{-2/3}3^{13/8}\\\varphi \left(\exp(-2{\sqrt {3}}\,\pi )\right)&=&\pi ^{-1}{\Gamma \left({\tfrac {4}{3}}\right)}^{3/2}2^{-2/3}3^{13/8}\cos({\tfrac {1}{24}}\pi )\\\varphi \left(\exp(-3{\sqrt {3}}\,\pi )\right)&=&\pi ^{-1}{\Gamma \left({\tfrac {4}{3}}\right)}^{3/2}2^{-2/3}3^{7/8}({\sqrt[{3}]{2}}+1)\\\varphi \left(\exp(-4{\sqrt {3}}\,\pi )\right)&=&\pi ^{-1}{\Gamma \left({\tfrac {4}{3}}\right)}^{3/2}2^{-5/3}3^{13/8}{\Bigl (}1+{\sqrt {\cos({\tfrac {1}{12}}\pi )}}{\Bigr )}\\\varphi \left(\exp(-5{\sqrt {3}}\,\pi )\right)&=&\pi ^{-1}{\Gamma \left({\tfrac {4}{3}}\right)}^{3/2}2^{-2/3}3^{5/8}\sin({\tfrac {1}{5}}\pi )({\tfrac {2}{5}}{\sqrt[{3}]{100}}+{\tfrac {2}{5}}{\sqrt[{3}]{10}}+{\tfrac {3}{5}}{\sqrt {5}}+1)\end{array}}$

### Further values

Many values of the theta function and especially of the shown phi function can be represented in terms of the gamma function:

${\begin{array}{lll}\varphi \left(\exp(-{\sqrt {2}}\,\pi )\right)&=&\pi ^{-1/2}\Gamma \left({\tfrac {9}{8}}\right){\Gamma \left({\tfrac {5}{4}}\right)}^{-1/2}2^{7/8}\\\varphi \left(\exp(-2{\sqrt {2}}\,\pi )\right)&=&\pi ^{-1/2}\Gamma \left({\tfrac {9}{8}}\right){\Gamma \left({\tfrac {5}{4}}\right)}^{-1/2}2^{1/8}{\Bigl (}1+{\sqrt {{\sqrt {2}}-1}}{\Bigr )}\\\varphi \left(\exp(-3{\sqrt {2}}\,\pi )\right)&=&\pi ^{-1/2}\Gamma \left({\tfrac {9}{8}}\right){\Gamma \left({\tfrac {5}{4}}\right)}^{-1/2}2^{3/8}3^{-1/2}({\sqrt {3}}+1){\sqrt {\tan({\tfrac {5}{24}}\pi )}}\\\varphi \left(\exp(-4{\sqrt {2}}\,\pi )\right)&=&\pi ^{-1/2}\Gamma \left({\tfrac {9}{8}}\right){\Gamma \left({\tfrac {5}{4}}\right)}^{-1/2}2^{-1/8}{\Bigl (}1+{\sqrt[{4}]{2{\sqrt {2}}-2}}{\Bigr )}\\\varphi \left(\exp(-5{\sqrt {2}}\,\pi )\right)&=&\pi ^{-1/2}\Gamma \left({\tfrac {9}{8}}\right){\Gamma \left({\tfrac {5}{4}}\right)}^{-1/2}{\frac {1}{15}}\,2^{3/8}\times \\&&\times {\biggl [}{\sqrt[{3}]{5}}\,{\sqrt {10+2{\sqrt {5}}}}{\biggl (}{\sqrt[{3}]{5+{\sqrt {2}}+3{\sqrt {3}}}}+{\sqrt[{3}]{5+{\sqrt {2}}-3{\sqrt {3}}}}\,{\biggr )}-{\bigl (}2-{\sqrt {2}}\,{\bigr )}{\sqrt {25-10{\sqrt {5}}}}\,{\biggr ]}\\\varphi \left(\exp(-{\sqrt {6}}\,\pi )\right)&=&\pi ^{-1/2}\Gamma \left({\tfrac {5}{24}}\right){\Gamma \left({\tfrac {5}{12}}\right)}^{-1/2}2^{-13/24}3^{-1/8}{\sqrt {\sin({\tfrac {5}{12}}\pi )}}\\\varphi \left(\exp(-{\tfrac {1}{2}}{\sqrt {6}}\,\pi )\right)&=&\pi ^{-1/2}\Gamma \left({\tfrac {5}{24}}\right){\Gamma \left({\tfrac {5}{12}}\right)}^{-1/2}2^{5/24}3^{-1/8}\sin({\tfrac {5}{24}}\pi )\end{array}}$


## Nome power theorems

### Direct power theorems

For the transformation of the nome in the theta functions these formulas can be used:

$\theta _{2}(q^{2})={\tfrac {1}{2}}{\sqrt {2[\theta _{3}(q)^{2}-\theta _{4}(q)^{2}]}}$

$\theta _{3}(q^{2})={\tfrac {1}{2}}{\sqrt {2[\theta _{3}(q)^{2}+\theta _{4}(q)^{2}]}}$

$\theta _{4}(q^{2})={\sqrt {\theta _{4}(q)\theta _{3}(q)}}$

The squares of the three theta zero-value functions with the square function as the inner function are also formed in the pattern of the Pythagorean triples according to the Jacobi identity. Furthermore, those transformations are valid:

$\theta _{3}(q^{4})={\tfrac {1}{2}}\theta _{3}(q)+{\tfrac {1}{2}}\theta _{4}(q)$

These formulas can be used to compute the theta values of the cube of the nome:

$27\,\theta _{3}(q^{3})^{8}-18\,\theta _{3}(q^{3})^{4}\theta _{3}(q)^{4}-\,\theta _{3}(q)^{8}=8\,\theta _{3}(q^{3})^{2}\theta _{3}(q)^{2}[2\,\theta _{4}(q)^{4}-\theta _{3}(q)^{4}]$

$27\,\theta _{4}(q^{3})^{8}-18\,\theta _{4}(q^{3})^{4}\theta _{4}(q)^{4}-\,\theta _{4}(q)^{8}=8\,\theta _{4}(q^{3})^{2}\theta _{4}(q)^{2}[2\,\theta _{3}(q)^{4}-\theta _{4}(q)^{4}]$

And the following formulas can be used to compute the theta values of the fifth power of the nome:

$[\theta _{3}(q)^{2}-\theta _{3}(q^{5})^{2}][5\,\theta _{3}(q^{5})^{2}-\theta _{3}(q)^{2}]^{5}=256\,\theta _{3}(q^{5})^{2}\theta _{3}(q)^{2}\theta _{4}(q)^{4}[\theta _{3}(q)^{4}-\theta _{4}(q)^{4}]$

$[\theta _{4}(q^{5})^{2}-\theta _{4}(q)^{2}][5\,\theta _{4}(q^{5})^{2}-\theta _{4}(q)^{2}]^{5}=256\,\theta _{4}(q^{5})^{2}\theta _{4}(q)^{2}\theta _{3}(q)^{4}[\theta _{3}(q)^{4}-\theta _{4}(q)^{4}]$

### Transformation at the cube root of the nome

The formulas for the theta Nullwert function values from the cube root of the elliptic nome are obtained by contrasting the two real solutions of the corresponding quartic equations:

${\biggl [}{\frac {\theta _{3}(q^{1/3})^{2}}{\theta _{3}(q)^{2}}}-{\frac {3\,\theta _{3}(q^{3})^{2}}{\theta _{3}(q)^{2}}}{\biggr ]}^{2}=4-4{\biggl [}{\frac {2\,\theta _{2}(q)^{2}\theta _{4}(q)^{2}}{\theta _{3}(q)^{4}}}{\biggr ]}^{2/3}$

${\biggl [}{\frac {3\,\theta _{4}(q^{3})^{2}}{\theta _{4}(q)^{2}}}-{\frac {\theta _{4}(q^{1/3})^{2}}{\theta _{4}(q)^{2}}}{\biggr ]}^{2}=4+4{\biggl [}{\frac {2\,\theta _{2}(q)^{2}\theta _{3}(q)^{2}}{\theta _{4}(q)^{4}}}{\biggr ]}^{2/3}$

### Transformation at the fifth root of the nome

The Rogers-Ramanujan continued fraction can be defined in terms of the **Jacobi theta function** in the following way:

$R(q)=\tan {\biggl \{}{\frac {1}{2}}\arctan {\biggl [}{\frac {1}{2}}-{\frac {\theta _{4}(q)^{2}}{2\,\theta _{4}(q^{5})^{2}}}{\biggr ]}{\biggr \}}^{1/5}\tan {\biggl \{}{\frac {1}{2}}\operatorname {arccot} {\biggl [}{\frac {1}{2}}-{\frac {\theta _{4}(q)^{2}}{2\,\theta _{4}(q^{5})^{2}}}{\biggr ]}{\biggr \}}^{2/5}$

$R(q^{2})=\tan {\biggl \{}{\frac {1}{2}}\arctan {\biggl [}{\frac {1}{2}}-{\frac {\theta _{4}(q)^{2}}{2\,\theta _{4}(q^{5})^{2}}}{\biggr ]}{\biggr \}}^{2/5}\cot {\biggl \{}{\frac {1}{2}}\operatorname {arccot} {\biggl [}{\frac {1}{2}}-{\frac {\theta _{4}(q)^{2}}{2\,\theta _{4}(q^{5})^{2}}}{\biggr ]}{\biggr \}}^{1/5}$

$R(q^{2})=\tan {\biggl \{}{\frac {1}{2}}\arctan {\biggl [}{\frac {\theta _{3}(q)^{2}}{2\,\theta _{3}(q^{5})^{2}}}-{\frac {1}{2}}{\biggr ]}{\biggr \}}^{2/5}\tan {\biggl \{}{\frac {1}{2}}\operatorname {arccot} {\biggl [}{\frac {\theta _{3}(q)^{2}}{2\,\theta _{3}(q^{5})^{2}}}-{\frac {1}{2}}{\biggr ]}{\biggr \}}^{1/5}$

The alternating Rogers-Ramanujan continued fraction function S(q) has the following two identities:

$S(q)={\frac {R(q^{4})}{R(q^{2})R(q)}}=\tan {\biggl \{}{\frac {1}{2}}\arctan {\biggl [}{\frac {\theta _{3}(q)^{2}}{2\,\theta _{3}(q^{5})^{2}}}-{\frac {1}{2}}{\biggr ]}{\biggr \}}^{1/5}\cot {\biggl \{}{\frac {1}{2}}\operatorname {arccot} {\biggl [}{\frac {\theta _{3}(q)^{2}}{2\,\theta _{3}(q^{5})^{2}}}-{\frac {1}{2}}{\biggr ]}{\biggr \}}^{2/5}$

The theta function values from the fifth root of the nome can be represented as a rational combination of the continued fractions R and S and the theta function values from the fifth power of the nome and the nome itself. The following four equations are valid for all values q between 0 and 1:

${\frac {\theta _{3}(q^{1/5})}{\theta _{3}(q^{5})}}-1={\frac {1}{S(q)}}{\bigl [}S(q)^{2}+R(q^{2}){\bigr ]}{\bigl [}1+R(q^{2})S(q){\bigr ]}$

$1-{\frac {\theta _{4}(q^{1/5})}{\theta _{4}(q^{5})}}={\frac {1}{R(q)}}{\bigl [}R(q^{2})+R(q)^{2}{\bigr ]}{\bigl [}1-R(q^{2})R(q){\bigr ]}$

$\theta _{3}(q^{1/5})^{2}-\theta _{3}(q)^{2}={\bigl [}\theta _{3}(q)^{2}-\theta _{3}(q^{5})^{2}{\bigr ]}{\biggl [}1+{\frac {1}{R(q^{2})S(q)}}+R(q^{2})S(q)+{\frac {1}{R(q^{2})^{2}}}+R(q^{2})^{2}+{\frac {1}{S(q)}}-S(q){\biggr ]}$

$\theta _{4}(q)^{2}-\theta _{4}(q^{1/5})^{2}={\bigl [}\theta _{4}(q^{5})^{2}-\theta _{4}(q)^{2}{\bigr ]}{\biggl [}1-{\frac {1}{R(q^{2})R(q)}}-R(q^{2})R(q)+{\frac {1}{R(q^{2})^{2}}}+R(q^{2})^{2}-{\frac {1}{R(q)}}+R(q){\biggr ]}$

### Modulus dependent theorems

In combination with the elliptic modulus, the following formulas can be displayed:

These are the formulas for the square of the elliptic nome:

$\theta _{4}[q(k)]=\theta _{4}[q(k)^{2}]{\sqrt[{8}]{1-k^{2}}}$

$\theta _{4}[q(k)^{2}]=\theta _{3}[q(k)]{\sqrt[{8}]{1-k^{2}}}$

$\theta _{3}[q(k)^{2}]=\theta _{3}[q(k)]\cos[{\tfrac {1}{2}}\arcsin(k)]$

And this is an efficient formula for the cube of the nome:

$\theta _{4}{\biggl \langle }q{\bigl \{}\tan {\bigl [}{\tfrac {1}{2}}\arctan(t^{3}){\bigr ]}{\bigr \}}^{3}{\biggr \rangle }=\theta _{4}{\biggl \langle }q{\bigl \{}\tan {\bigl [}{\tfrac {1}{2}}\arctan(t^{3}){\bigr ]}{\bigr \}}{\biggr \rangle }\,3^{-1/2}{\bigl (}{\sqrt {2{\sqrt {t^{4}-t^{2}+1}}-t^{2}+2}}+{\sqrt {t^{2}+1}}\,{\bigr )}^{1/2}$

For all real values $t\in \mathbb {R}$ the now mentioned formula is valid.

And for this formula two examples shall be given:

First calculation example with the value $t=1$ inserted:

| $\theta _{4}{\biggl \langle }q{\bigl \{}\tan {\bigl [}{\tfrac {1}{2}}\arctan(1){\bigr ]}{\bigr \}}^{3}{\biggr \rangle }=\theta _{4}{\biggl \langle }q{\bigl \{}\tan {\bigl [}{\tfrac {1}{2}}\arctan(1){\bigr ]}{\bigr \}}{\biggr \rangle }\,3^{-1/2}{\bigl (}{\sqrt {3}}+{\sqrt {2}}\,{\bigr )}^{1/2}$ |
|---|
| $\theta _{4}{\bigl [}\exp(-3{\sqrt {2}}\,\pi ){\bigr ]}=\theta _{4}{\bigl [}\exp(-{\sqrt {2}}\,\pi ){\bigr ]}\,3^{-1/2}{\bigl (}{\sqrt {3}}+{\sqrt {2}}\,{\bigr )}^{1/2}$ |

Second calculation example with the value $t=\Phi ^{-2}$ inserted:

| $\theta _{4}{\biggl \langle }q{\bigl \{}\tan {\bigl [}{\tfrac {1}{2}}\arctan(\Phi ^{-6}){\bigr ]}{\bigr \}}^{3}{\biggr \rangle }=\theta _{4}{\biggl \langle }q{\bigl \{}\tan {\bigl [}{\tfrac {1}{2}}\arctan(\Phi ^{-6}){\bigr ]}{\bigr \}}{\biggr \rangle }\,3^{-1/2}{\bigl (}{\sqrt {2{\sqrt {\Phi ^{-8}-\Phi ^{-4}+1}}-\Phi ^{-4}+2}}+{\sqrt {\Phi ^{-4}+1}}\,{\bigr )}^{1/2}$ |
|---|
| $\theta _{4}{\bigl [}\exp(-3{\sqrt {10}}\,\pi ){\bigr ]}=\theta _{4}{\bigl [}\exp(-{\sqrt {10}}\,\pi ){\bigr ]}\,3^{-1/2}{\bigl (}{\sqrt {2{\sqrt {\Phi ^{-8}-\Phi ^{-4}+1}}-\Phi ^{-4}+2}}+{\sqrt {\Phi ^{-4}+1}}\,{\bigr )}^{1/2}$ |

The constant $\Phi$ represents the golden ratio number $\Phi ={\tfrac {1}{2}}({\sqrt {5}}+1)$ exactly.


## Some series identities

### Sums with theta function in the result

The infinite sum of the reciprocals of Fibonacci numbers with odd indices has the identity:

$\sum _{n=1}^{\infty }{\frac {1}{F_{2n-1}}}={\frac {\sqrt {5}}{2}}\,\sum _{n=1}^{\infty }{\frac {2(\Phi ^{-2})^{n-1/2}}{1+(\Phi ^{-2})^{2n-1}}}={\frac {\sqrt {5}}{4}}\sum _{a=-\infty }^{\infty }{\frac {2(\Phi ^{-2})^{a-1/2}}{1+(\Phi ^{-2})^{2a-1}}}=$

$={\frac {\sqrt {5}}{4}}\,\theta _{2}(\Phi ^{-2})^{2}={\frac {\sqrt {5}}{8}}{\bigl [}\theta _{3}(\Phi ^{-1})^{2}-\theta _{4}(\Phi ^{-1})^{2}{\bigr ]}$

By not using the theta function expression, following identity between two sums can be formulated:

$\sum _{n=1}^{\infty }{\frac {1}{F_{2n-1}}}={\frac {\sqrt {5}}{4}}\,{\biggl [}\sum _{n=1}^{\infty }2\,\Phi ^{-(2n-1)^{2}/2}{\biggr ]}^{2}$

$\sum _{n=1}^{\infty }{\frac {1}{F_{2n-1}}}=1.82451515740692456814215840626732817332\ldots$

Also in this case $\Phi ={\tfrac {1}{2}}({\sqrt {5}}+1)$ is Golden ratio number again.

Infinite sum of the reciprocals of the Fibonacci number squares:

$\sum _{n=1}^{\infty }{\frac {1}{F_{n}^{2}}}={\frac {5}{24}}{\bigl [}2\,\theta _{2}(\Phi ^{-2})^{4}-\theta _{3}(\Phi ^{-2})^{4}+1{\bigr ]}={\frac {5}{24}}{\bigl [}\theta _{3}(\Phi ^{-2})^{4}-2\,\theta _{4}(\Phi ^{-2})^{4}+1{\bigr ]}$

Infinite sum of the reciprocals of the Pell numbers with odd indices:

$\sum _{n=1}^{\infty }{\frac {1}{P_{2n-1}}}={\frac {1}{\sqrt {2}}}\,\theta _{2}{\bigl [}({\sqrt {2}}-1)^{2}{\bigr ]}^{2}={\frac {1}{2{\sqrt {2}}}}{\bigl [}\theta _{3}({\sqrt {2}}-1)^{2}-\theta _{4}({\sqrt {2}}-1)^{2}{\bigr ]}$

### Sums with theta function in the summand

The next two series identities were proved by István Mező:

${\begin{aligned}\theta _{4}^{2}(q)&=iq^{\frac {1}{4}}\sum _{k=-\infty }^{\infty }q^{2k^{2}-k}\theta _{1}\left({\frac {2k-1}{2i}}\ln q,q\right),\\[6pt]\theta _{4}^{2}(q)&=\sum _{k=-\infty }^{\infty }q^{2k^{2}}\theta _{4}\left({\frac {k\ln q}{i}},q\right).\end{aligned}}$

These relations hold for all 0 < *q* < 1. Specializing the values of q, we have the next parameter free sums

${\sqrt {\frac {\pi {\sqrt {e^{\pi }}}}{2}}}\cdot {\frac {1}{\Gamma ^{2}\left({\frac {3}{4}}\right)}}=i\sum _{k=-\infty }^{\infty }e^{\pi \left(k-2k^{2}\right)}\theta _{1}\left({\frac {i\pi }{2}}(2k-1),e^{-\pi }\right)$

${\sqrt {\frac {\pi }{2}}}\cdot {\frac {1}{\Gamma ^{2}\left({\frac {3}{4}}\right)}}=\sum _{k=-\infty }^{\infty }{\frac {\theta _{4}\left(ik\pi ,e^{-\pi }\right)}{e^{2\pi k^{2}}}}$


## Zeros of the Jacobi theta functions

All zeros of the Jacobi theta functions are simple zeros and are given by the following:

${\begin{aligned}\vartheta (z;\tau )=\vartheta _{00}(z;\tau )&=0\quad &\Longleftrightarrow &&\quad z&=m+n\tau +{\frac {1}{2}}+{\frac {\tau }{2}}\\[3pt]\vartheta _{11}(z;\tau )&=0\quad &\Longleftrightarrow &&\quad z&=m+n\tau \\[3pt]\vartheta _{10}(z;\tau )&=0\quad &\Longleftrightarrow &&\quad z&=m+n\tau +{\frac {1}{2}}\\[3pt]\vartheta _{01}(z;\tau )&=0\quad &\Longleftrightarrow &&\quad z&=m+n\tau +{\frac {\tau }{2}}\end{aligned}}$

where m, n are arbitrary integers.


## Relation to the Riemann zeta function

The relation

$\vartheta \left(0;-{\frac {1}{\tau }}\right)=\left(-i\tau \right)^{\frac {1}{2}}\vartheta (0;\tau )$

was used by Riemann to prove the functional equation for the Riemann zeta function, by means of the Mellin transform

$\Gamma \left({\frac {s}{2}}\right)\pi ^{-{\frac {s}{2}}}\zeta (s)={\frac {1}{2}}\int _{0}^{\infty }{\bigl (}\vartheta (0;it)-1{\bigr )}t^{\frac {s}{2}}{\frac {\mathrm {d} t}{t}}$

which can be shown to be invariant under substitution of s by 1 − *s*. The corresponding integral for *z* ≠ 0 is given in the article on the Hurwitz zeta function.


## Relation to the Weierstrass elliptic function

The theta function was used by Jacobi to construct (in a form adapted to easy calculation) his elliptic functions as the quotients of the above four theta functions, and could have been used by him to construct Weierstrass's elliptic functions also, since

$\wp (z;\tau )=-{\big (}\log \vartheta _{11}(z;\tau ){\big )}''+c$

where the second derivative is with respect to z and the constant c is defined so that the Laurent expansion of ℘(*z*) at *z* = 0 has zero constant term.


## Relation to the *q*-gamma function

The fourth theta function – and thus the others too – is intimately connected to the Jackson q-gamma function via the relation

$\left(\Gamma _{q^{2}}(x)\Gamma _{q^{2}}(1-x)\right)^{-1}={\frac {q^{2x(1-x)}}{\left(q^{-2};q^{-2}\right)_{\infty }^{3}\left(q^{2}-1\right)}}\theta _{4}\left({\frac {1}{2i}}(1-2x)\log q,{\frac {1}{q}}\right).$


## Relations to Dedekind eta function

Let *η*(*τ*) be the Dedekind eta function, and the argument of the theta function as the nome *q* = *e**πiτ*. Then,

${\begin{aligned}\theta _{2}(q)=\vartheta _{10}(0;\tau )&={\frac {2\eta ^{2}(2\tau )}{\eta (\tau )}},\\[3pt]\theta _{3}(q)=\vartheta _{00}(0;\tau )&={\frac {\eta ^{5}(\tau )}{\eta ^{2}\left({\frac {1}{2}}\tau \right)\eta ^{2}(2\tau )}}={\frac {\eta ^{2}\left({\frac {1}{2}}(\tau +1)\right)}{\eta (\tau +1)}},\\[3pt]\theta _{4}(q)=\vartheta _{01}(0;\tau )&={\frac {\eta ^{2}\left({\frac {1}{2}}\tau \right)}{\eta (\tau )}},\end{aligned}}$

and,

$\theta _{2}(q)\,\theta _{3}(q)\,\theta _{4}(q)=2\eta ^{3}(\tau ).$

See also the Weber modular functions.


## Elliptic modulus

The elliptic modulus is

$k(\tau )={\frac {\vartheta _{10}(0;\tau )^{2}}{\vartheta _{00}(0;\tau )^{2}}}$

and the complementary elliptic modulus is

$k'(\tau )={\frac {\vartheta _{01}(0;\tau )^{2}}{\vartheta _{00}(0;\tau )^{2}}}$


## Derivatives of theta functions

These are two identical definitions of the complete elliptic integral of the second kind:

$E(k)=\int _{0}^{\pi /2}{\sqrt {1-k^{2}\sin(\varphi )^{2}}}d\varphi$

$E(k)={\frac {\pi }{2}}\sum _{a=0}^{\infty }{\frac {[(2a)!]^{2}}{(1-2a)16^{a}(a!)^{4}}}k^{2a}$

The derivatives of the Theta Nullwert functions have these MacLaurin series:

$\theta _{2}'(x)={\frac {\mathrm {d} }{\mathrm {d} x}}\,\theta _{2}(x)={\frac {1}{2}}x^{-3/4}+\sum _{n=1}^{\infty }{\frac {1}{2}}(2n+1)^{2}x^{(2n-1)(2n+3)/4}$

$\theta _{3}'(x)={\frac {\mathrm {d} }{\mathrm {d} x}}\,\theta _{3}(x)=2+\sum _{n=1}^{\infty }2(n+1)^{2}x^{n(n+2)}$

$\theta _{4}'(x)={\frac {\mathrm {d} }{\mathrm {d} x}}\,\theta _{4}(x)=-2+\sum _{n=1}^{\infty }2(n+1)^{2}(-1)^{n+1}x^{n(n+2)}$

The derivatives of theta zero-value functions are as follows:

$\theta _{2}'(x)={\frac {\mathrm {d} }{\mathrm {d} x}}\,\theta _{2}(x)={\frac {1}{2\pi x}}\theta _{2}(x)\theta _{3}(x)^{2}E{\biggl [}{\frac {\theta _{2}(x)^{2}}{\theta _{3}(x)^{2}}}{\biggr ]}$

$\theta _{3}'(x)={\frac {\mathrm {d} }{\mathrm {d} x}}\,\theta _{3}(x)=\theta _{3}(x){\bigl [}\theta _{3}(x)^{2}+\theta _{4}(x)^{2}{\bigr ]}{\biggl \{}{\frac {1}{2\pi x}}E{\biggl [}{\frac {\theta _{3}(x)^{2}-\theta _{4}(x)^{2}}{\theta _{3}(x)^{2}+\theta _{4}(x)^{2}}}{\biggr ]}-{\frac {\theta _{4}(x)^{2}}{4\,x}}{\biggr \}}$

$\theta _{4}'(x)={\frac {\mathrm {d} }{\mathrm {d} x}}\,\theta _{4}(x)=\theta _{4}(x){\bigl [}\theta _{3}(x)^{2}+\theta _{4}(x)^{2}{\bigr ]}{\biggl \{}{\frac {1}{2\pi x}}E{\biggl [}{\frac {\theta _{3}(x)^{2}-\theta _{4}(x)^{2}}{\theta _{3}(x)^{2}+\theta _{4}(x)^{2}}}{\biggr ]}-{\frac {\theta _{3}(x)^{2}}{4\,x}}{\biggr \}}$

The two last mentioned formulas are valid for all real numbers of the real definition interval: $-1<x<1\,\cap \,x\in \mathbb {R}$

And these two last named theta derivative functions are related to each other in this way:

$\vartheta _{4}(x){\biggl [}{\frac {\mathrm {d} }{\mathrm {d} x}}\,\vartheta _{3}(x){\biggr ]}-\vartheta _{3}(x){\biggl [}{\frac {\mathrm {d} }{\mathrm {d} x}}\,\theta _{4}(x){\biggr ]}={\frac {1}{4\,x}}\,\theta _{3}(x)\,\theta _{4}(x){\bigl [}\theta _{3}(x)^{4}-\theta _{4}(x)^{4}{\bigr ]}$

The derivatives of the quotients from two of the three theta functions mentioned here always have a rational relationship to those three functions:

${\frac {\mathrm {d} }{\mathrm {d} x}}\,{\frac {\theta _{2}(x)}{\theta _{3}(x)}}={\frac {\theta _{2}(x)\,\theta _{4}(x)^{4}}{4\,x\,\theta _{3}(x)}}$

${\frac {\mathrm {d} }{\mathrm {d} x}}\,{\frac {\theta _{2}(x)}{\theta _{4}(x)}}={\frac {\theta _{2}(x)\,\theta _{3}(x)^{4}}{4\,x\,\theta _{4}(x)}}$

${\frac {\mathrm {d} }{\mathrm {d} x}}\,{\frac {\theta _{3}(x)}{\theta _{4}(x)}}={\frac {\theta _{3}(x)^{5}-\theta _{3}(x)\,\theta _{4}(x)^{4}}{4\,x\,\theta _{4}(x)}}$

For the derivation of these derivation formulas see the articles Nome (mathematics) and Modular lambda function!


## Integrals of theta functions

For the theta functions these integrals are valid:

$\int _{0}^{1}\theta _{2}(x)\,\mathrm {d} x=\sum _{k=-\infty }^{\infty }{\frac {4}{(2k+1)^{2}+4}}=\pi \tanh(\pi )\approx 3.129881$

$\int _{0}^{1}\theta _{3}(x)\,\mathrm {d} x=\sum _{k=-\infty }^{\infty }{\frac {1}{k^{2}+1}}=\pi \coth(\pi )\approx 3.153348$

$\int _{0}^{1}\theta _{4}(x)\,\mathrm {d} x=\sum _{k=-\infty }^{\infty }{\frac {(-1)^{k}}{k^{2}+1}}=\pi \,\operatorname {csch} (\pi )\approx 0.272029$

The final results now shown are based on the general Cauchy sum formulas.


## A solution to the heat equation

The Jacobi theta function is the fundamental solution of the one-dimensional heat equation with spatially periodic boundary conditions. Taking *z* = *x* to be real and *τ* = *it* with t real and positive, we can write

$\vartheta (x;it)=1+2\sum _{n=1}^{\infty }\exp \left(-\pi n^{2}t\right)\cos(2\pi nx)$

which solves the heat equation

${\frac {\partial }{\partial t}}\vartheta (x;it)={\frac {1}{4\pi }}{\frac {\partial ^{2}}{\partial x^{2}}}\vartheta (x;it).$

This theta-function solution is 1-periodic in x, and as *t* → 0 it approaches the periodic delta function, or Dirac comb, in the sense of distributions

$\lim _{t\to 0}\vartheta (x;it)=\sum _{n=-\infty }^{\infty }\delta (x-n)$

.

General solutions of the spatially periodic initial value problem for the heat equation may be obtained by convolving the initial data at *t* = 0 with the theta function.


## Relation to the Heisenberg group

The Jacobi theta function is invariant under the action of a discrete subgroup of the Heisenberg group. This invariance is presented in the article on the theta representation of the Heisenberg group.


## Generalizations

If F is a positive-definite quadratic form in n variables, then the theta function associated with F is

$\theta _{F}(z)=\sum _{m\in \mathbb {Z} ^{n}}e^{-\pi zF(m)}$

with the sum extending over the lattice of integers $\mathbb {Z} ^{n}$ . This theta function is a modular form of weight ⁠*n*/2⁠ (on an appropriately defined subgroup) of the modular group. In the Fourier expansion,

${\hat {\theta }}_{F}(z)=\sum _{k=0}^{\infty }R_{F}(k)e^{2\pi ikz},$

the numbers *RF*(*k*) are called the *representation numbers* of the form.

### Theta series of a Dirichlet character

For χ a primitive Dirichlet character modulo q and *ν* = ⁠1 − *χ*(−1)/2⁠ then

$\theta _{\chi }(z)={\frac {1}{2}}\sum _{n=-\infty }^{\infty }\chi (n)n^{\nu }e^{2i\pi n^{2}z}$

is a weight ⁠1/2⁠ + *ν* modular form of level 4*q*2 and character

$\chi (d)\left({\frac {-1}{d}}\right)^{\nu },$

which means

$\theta _{\chi }\left({\frac {az+b}{cz+d}}\right)=\chi (d)\left({\frac {-1}{d}}\right)^{\nu }\left({\frac {\theta _{1}\left({\frac {az+b}{cz+d}}\right)}{\theta _{1}(z)}}\right)^{1+2\nu }\theta _{\chi }(z)$

whenever

$a,b,c,d\in \mathbb {Z} ^{4},ad-bc=1,c\equiv 0{\bmod {4}}q^{2}.$

### Ramanujan theta function

### Riemann theta function

Let

$\mathbb {H} _{n}=\left\{F\in M(n,\mathbb {C} )\,{\big |}\,F=F^{\mathsf {T}}\,,\,\operatorname {Im} F>0\right\}$

be the set of symmetric square matrices whose imaginary part is positive definite. $\mathbb {H} _{n}$ is called the Siegel upper half-space and is the multi-dimensional analog of the upper half-plane. The n-dimensional analogue of the modular group is the symplectic group $\operatorname {Sp} (2n,\mathbb {Z} )$ ; for *n* = 1, $\operatorname {Sp} (2,\mathbb {Z} )=\operatorname {SL} (2,\mathbb {Z} )$ . The n-dimensional analogue of the congruence subgroups is played by

$\ker {\big \{}\operatorname {Sp} (2n,\mathbb {Z} )\to \operatorname {Sp} (2n,\mathbb {Z} /k\mathbb {Z} ){\big \}}.$

Then, given $\tau \in \mathbb {H} _{n}$ , the **Riemann theta function** is defined as

$\theta (z,\tau )=\sum _{m\in \mathbb {Z} ^{n}}\exp \left(2\pi i\left({\tfrac {1}{2}}m^{\mathsf {T}}\tau m+m^{\mathsf {T}}z\right)\right).$

Here, $z\in \mathbb {C} ^{n}$ is an n-dimensional complex vector, and the superscript **T** denotes the transpose. The Jacobi theta function is then a special case, with *n* = 1 and $\tau \in \mathbb {H}$ where $\mathbb {H}$ is the upper half-plane. One major application of the Riemann theta function is that it allows one to give explicit formulas for meromorphic functions on compact Riemann surfaces, as well as other auxiliary objects that figure prominently in their function theory, by taking τ to be the period matrix with respect to a canonical basis for its first homology group.

The Riemann theta converges absolutely and uniformly on compact subsets of $\mathbb {C} ^{n}\times \mathbb {H} _{n}$ .

The functional equation is

$\theta (z+a+\tau b,\tau )=\exp \left(2\pi i\left(-b^{\mathsf {T}}z-{\tfrac {1}{2}}b^{\mathsf {T}}\tau b\right)\right)\theta (z,\tau )$

which holds for all vectors $a,b\in \mathbb {Z} ^{n}$ , and for all $z\in \mathbb {C} ^{n}$ and $\tau \in \mathbb {H} _{n}$ .

### Poincaré series

The Poincaré series generalizes the theta series to automorphic forms with respect to arbitrary Fuchsian groups.
