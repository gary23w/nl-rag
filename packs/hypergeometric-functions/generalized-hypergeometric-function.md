---
title: "Generalized hypergeometric function"
source: https://en.wikipedia.org/wiki/Generalized_hypergeometric_function
domain: hypergeometric-functions
license: CC-BY-SA-4.0
tags: hypergeometric function, confluent hypergeometric function, pochhammer symbol, hypergeometric series
fetched: 2026-07-02
---

# Generalized hypergeometric function

In mathematics, a **generalized hypergeometric series** is a power series in which the ratio of successive coefficients indexed by *n* is a rational function of *n*. The series, if convergent, defines a **generalized hypergeometric function**, which may then be defined over a wider domain of the argument by analytic continuation. The generalized hypergeometric series is sometimes just called the hypergeometric series, though this term also sometimes just refers to the Gaussian hypergeometric series. Generalized hypergeometric functions include the (Gaussian) hypergeometric function and the confluent hypergeometric function as special cases, which in turn have many particular special functions as special cases, such as elementary functions, Bessel functions, and the classical orthogonal polynomials.

## Notation

A hypergeometric series is formally defined as a power series

$\beta _{0}+\beta _{1}z+\beta _{2}z^{2}+\dots =\sum _{n\geqslant 0}\beta _{n}z^{n}$

in which the ratio of successive coefficients is a rational function of *n*. That is,

${\frac {\beta _{n+1}}{\beta _{n}}}={\frac {A(n)}{B(n)}}$

where *A*(*n*) and *B*(*n*) are polynomials in *n*.

For example, in the case of the series for the exponential function,

$1+{\frac {z}{1!}}+{\frac {z^{2}}{2!}}+{\frac {z^{3}}{3!}}+\cdots ,$

we have:

$\beta _{n}={\frac {1}{n!}},\qquad {\frac {\beta _{n+1}}{\beta _{n}}}={\frac {1}{n+1}}.$

So this satisfies the definition with *A*(*n*) = 1 and *B*(*n*) = *n* + 1.

It is customary to factor out the leading term, so β0 is assumed to be 1. The polynomials can be factored into linear factors of the form (*aj* + *n*) and (*b**k* + *n*) respectively, where the *a**j* and *b**k* are complex numbers.

For historical reasons, it is assumed that (1 + *n*) is a factor of *B*. If this is not already the case then both *A* and *B* can be multiplied by this factor; the factor cancels so the terms are unchanged and there is no loss of generality.

The ratio between consecutive coefficients now has the form

${\frac {c(a_{1}+n)\cdots (a_{p}+n)}{d(b_{1}+n)\cdots (b_{q}+n)(1+n)}}$

,

where *c* and *d* are the leading coefficients of *A* and *B*. The series then has the form

$1+{\frac {a_{1}\cdots a_{p}}{b_{1}\cdots b_{q}\cdot 1}}{\frac {cz}{d}}+{\frac {a_{1}\cdots a_{p}}{b_{1}\cdots b_{q}\cdot 1}}{\frac {(a_{1}+1)\cdots (a_{p}+1)}{(b_{1}+1)\cdots (b_{q}+1)\cdot 2}}\left({\frac {cz}{d}}\right)^{2}+\cdots$

,

or, by scaling *z* by the appropriate factor and rearranging,

$1+{\frac {a_{1}\cdots a_{p}}{b_{1}\cdots b_{q}}}{\frac {z}{1!}}+{\frac {a_{1}(a_{1}+1)\cdots a_{p}(a_{p}+1)}{b_{1}(b_{1}+1)\cdots b_{q}(b_{q}+1)}}{\frac {z^{2}}{2!}}+\cdots$

.

This has the form of an exponential generating function. This series is usually denoted by

${}_{p}F_{q}(a_{1},\ldots ,a_{p};b_{1},\ldots ,b_{q};z)$

or

$\,{}_{p}F_{q}\left[{\begin{matrix}a_{1}&a_{2}&\cdots &a_{p}\\b_{1}&b_{2}&\cdots &b_{q}\end{matrix}};z\right].$

We can then use the rising factorial (typically written with a Pochhammer symbol in this context, even though the Pochhammer symbol normally denotes the falling factorial) defined by

${\begin{aligned}(a)_{0}&=1,\\(a)_{n}&=a(a+1)(a+2)\cdots (a+n-1)={\frac {\Gamma (a+n)}{\Gamma (a)}},&&n\geq 1,\end{aligned}}$

where $\Gamma (x)$ represents the gamma function. The series can then be written using either the rising factorial or the Gamma function as

$\,{}_{p}F_{q}(a_{1},\ldots ,a_{p};b_{1},\ldots ,b_{q};z)=\sum _{n=0}^{\infty }{\frac {(a_{1})_{n}\cdots (a_{p})_{n}}{(b_{1})_{n}\cdots (b_{q})_{n}}}\,{\frac {z^{n}}{n!}}={\frac {\Gamma (b_{1})\cdots \Gamma (b_{q})}{\Gamma (a_{1})\cdots \Gamma (a_{p})}}\sum _{n=0}^{\infty }{\frac {\Gamma (n+a_{1})\cdots \Gamma (n+a_{p})}{\Gamma (n+b_{1})\cdots \Gamma (n+b_{q})}}{\frac {z^{n}}{n!}}.$

## Terminology

When all the terms of the series are defined and it has a non-zero radius of convergence, then the series defines an analytic function. Such a function, and its analytic continuations, is called the **hypergeometric function**.

The case when the radius of convergence is 0 yields many interesting series in mathematics, for example the incomplete gamma function has the asymptotic expansion

$\Gamma (a,z)\sim z^{a-1}e^{-z}\left(1+{\frac {a-1}{z}}+{\frac {(a-1)(a-2)}{z^{2}}}+\cdots \right)$

which could be written *z**a*−1*e*−z 2*F*0(1−*a*,1;;−*z*−1). However, the use of the term *hypergeometric series* is usually restricted to the case where the series defines an actual analytic function.

The ordinary hypergeometric series should not be confused with the basic hypergeometric series, which, despite its name, is a rather more complicated and recondite series. The "basic" series is the q-analog of the ordinary hypergeometric series. There are several such generalizations of the ordinary hypergeometric series, including the ones coming from zonal spherical functions on Riemannian symmetric spaces.

The series without the factor of *n*! in the denominator (summed over all integers *n*, including negative) is called the bilateral hypergeometric series.

## Convergence conditions

There are certain values of the *a**j* and *b**k* for which the numerator or the denominator of the coefficients is 0.

- If any *a**j* is a non-positive integer (0, −1, −2, etc.) then the series only has a finite number of terms and is, in fact, a polynomial of degree −*a**j*.
- If any *b**k* is a non-positive integer (excepting the previous case with *b**k* < *a**j*) then the denominators become 0 and the series is undefined.

Excluding these cases, the ratio test can be applied to determine the radius of convergence.

- If *p* < *q* + 1 then the ratio of coefficients tends to zero. This implies that the series converges for any finite value of *z* and thus defines an entire function of *z*. An example is the power series for the exponential function.
- If *p* = *q* + 1 then the ratio of coefficients tends to one. This implies that the series converges for |*z*| < 1 and diverges for |*z*| > 1. Whether it converges for |*z*| = 1 is more difficult to determine. Analytic continuation can be employed for larger values of *z*.
- If *p* > *q* + 1 then the ratio of coefficients grows without bound. This implies that, besides *z* = 0, the series diverges. This is then a divergent or asymptotic series, or it can be interpreted as a symbolic shorthand for a differential equation that the sum satisfies formally.

The question of convergence for *p*=*q*+1 when *z* is on the unit circle is more difficult. It can be shown that the series converges absolutely at *z* = 1 if

$\Re \left(\sum b_{k}-\sum a_{j}\right)>0$

.

Further, if *p*=*q*+1, $\sum _{i=1}^{p}a_{i}\geq \sum _{j=1}^{q}b_{j}$ and *z* is real, then the following convergence result holds Quigley et al. (2013):

$\lim _{z\rightarrow 1}(1-z){\frac {d\log(_{p}F_{q}(a_{1},\ldots ,a_{p};b_{1},\ldots ,b_{q};z^{p}))}{dz}}=\sum _{i=1}^{p}a_{i}-\sum _{j=1}^{q}b_{j}$

.

## Basic properties

It is immediate from the definition that the order of the parameters *aj*, or the order of the parameters *bk* can be changed without changing the value of the function. Also, if any of the parameters *aj* is equal to any of the parameters *bk*, then the matching parameters can be "cancelled out", with certain exceptions when the parameters are non-positive integers. For example,

$\,{}_{2}F_{1}(3,1;1;z)=\,{}_{2}F_{1}(1,3;1;z)=\,{}_{1}F_{0}(3;;z)$

.

This cancelling is a special case of a reduction formula that may be applied whenever a parameter on the top row differs from one on the bottom row by a non-negative integer.

${}_{A+1}F_{B+1}\left[{\begin{array}{c}a_{1},\ldots ,a_{A},c+n\\b_{1},\ldots ,b_{B},c\end{array}};z\right]=\sum _{j=0}^{n}{\binom {n}{j}}{\frac {z^{j}}{(c)_{j}}}{\frac {\prod _{i=1}^{A}(a_{i})_{j}}{\prod _{i=1}^{B}(b_{i})_{j}}}{}_{A}F_{B}\left[{\begin{array}{c}a_{1}+j,\ldots ,a_{A}+j\\b_{1}+j,\ldots ,b_{B}+j\end{array}};z\right]$

### Euler's integral transform

The following basic identity is very useful as it relates the higher-order hypergeometric functions in terms of integrals over the lower order ones

${}_{A+1}F_{B+1}\left[{\begin{array}{c}a_{1},\ldots ,a_{A},c\\b_{1},\ldots ,b_{B},d\end{array}};z\right]={\frac {\Gamma (d)}{\Gamma (c)\Gamma (d-c)}}\int _{0}^{1}t^{c-1}(1-t)_{}^{d-c-1}\ {}_{A}F_{B}\left[{\begin{array}{c}a_{1},\ldots ,a_{A}\\b_{1},\ldots ,b_{B}\end{array}};tz\right]dt$

### Differentiation

The generalized hypergeometric function satisfies

${\begin{aligned}\left(z{\frac {\rm {d}}{{\rm {d}}z}}+a_{j}\right){}_{p}F_{q}\left[{\begin{array}{c}a_{1},\dots ,a_{j},\dots ,a_{p}\\b_{1},\dots ,b_{q}\end{array}};z\right]&=a_{j}\;{}_{p}F_{q}\left[{\begin{array}{c}a_{1},\dots ,a_{j}+1,\dots ,a_{p}\\b_{1},\dots ,b_{q}\end{array}};z\right]\\\end{aligned}}$

and

${\begin{aligned}\left(z{\frac {\rm {d}}{{\rm {d}}z}}+b_{k}-1\right){}_{p}F_{q}\left[{\begin{array}{c}a_{1},\dots ,a_{p}\\b_{1},\dots ,b_{k},\dots ,b_{q}\end{array}};z\right]&=(b_{k}-1)\;{}_{p}F_{q}\left[{\begin{array}{c}a_{1},\dots ,a_{p}\\b_{1},\dots ,b_{k}-1,\dots ,b_{q}\end{array}};z\right]{\text{ for }}b_{k}\neq 1\end{aligned}}$

Additionally,

${\begin{aligned}{\frac {\rm {d}}{{\rm {d}}z}}\;{}_{p}F_{q}\left[{\begin{array}{c}a_{1},\dots ,a_{p}\\b_{1},\dots ,b_{q}\end{array}};z\right]&={\frac {\prod _{i=1}^{p}a_{i}}{\prod _{j=1}^{q}b_{j}}}\;{}_{p}F_{q}\left[{\begin{array}{c}a_{1}+1,\dots ,a_{p}+1\\b_{1}+1,\dots ,b_{q}+1\end{array}};z\right]\end{aligned}}$

Combining these gives a differential equation satisfied by *w* = *p**F**q*:

$z\prod _{n=1}^{p}\left(z{\frac {\rm {d}}{{\rm {d}}z}}+a_{n}\right)w=z{\frac {\rm {d}}{{\rm {d}}z}}\prod _{n=1}^{q}\left(z{\frac {\rm {d}}{{\rm {d}}z}}+b_{n}-1\right)w$

.

Take the following operator:

$\vartheta =z{\frac {\rm {d}}{{\rm {d}}z}}.$

From the differentiation formulas given above, the linear space spanned by

${}_{p}F_{q}(a_{1},\dots ,a_{p};b_{1},\dots ,b_{q};z),\vartheta \;{}_{p}F_{q}(a_{1},\dots ,a_{p};b_{1},\dots ,b_{q};z)$

contains each of

${}_{p}F_{q}(a_{1},\dots ,a_{j}+1,\dots ,a_{p};b_{1},\dots ,b_{q};z),$

${}_{p}F_{q}(a_{1},\dots ,a_{p};b_{1},\dots ,b_{k}-1,\dots ,b_{q};z),$

$z\;{}_{p}F_{q}(a_{1}+1,\dots ,a_{p}+1;b_{1}+1,\dots ,b_{q}+1;z),$

${}_{p}F_{q}(a_{1},\dots ,a_{p};b_{1},\dots ,b_{q};z).$

Since the space has dimension 2, any three of these *p*+*q*+2 functions are linearly dependent:

$(a_{i}-b_{j}+1){}_{p}F_{q}(...a_{i}..;...,b_{j}...;z)=a_{i}\,{}_{p}F_{q}(...a_{i}+1..;...,b_{j}...;z)-(b_{j}-1){}_{p}F_{q}(...a_{i}..;...,b_{j}-1...;z).$

$(a_{i}-a_{j}){}_{p}F_{q}(...a_{i}..a_{j}..;.....;z)=a_{i}\,{}_{p}F_{q}(...a_{i}+1..a_{j}..;......;z)-a_{j}\,{}_{p}F_{q}(...a_{i}..a_{j}+1...;....;z).$

$b_{j}\,{}_{p}F_{q}(...a_{i}....;..b_{j}...;z)=a_{i}\,{}_{p}F_{q}(...a_{i}+1....;..b_{j}+1...;z)+(b_{j}-a_{i}){}_{p}F_{q}(...a_{i}....;..b_{j}+1...;z).$

$(a_{i}-1){}_{p}F_{q}(...a_{i}..a_{j};...;z)=(a_{i}-a_{j}-1){}_{p}F_{q}(...a_{i}-1..a_{j};...;z)+a_{j}\,{}_{p}F_{q}(...a_{i}-1..a_{j}+1;...;z).$

These dependencies can be written out to generate a large number of identities involving ${}_{p}F_{q}$ .

For example, in the simplest non-trivial case,

$\;{}_{0}F_{1}(;a;z)=(1)\;{}_{0}F_{1}(;a;z)$

,

$\;{}_{0}F_{1}(;a-1;z)=({\frac {\vartheta }{a-1}}+1)\;{}_{0}F_{1}(;a;z)$

,

$z\;{}_{0}F_{1}(;a+1;z)=(a\vartheta )\;{}_{0}F_{1}(;a;z)$

,

So

$\;{}_{0}F_{1}(;a-1;z)-\;{}_{0}F_{1}(;a;z)={\frac {z}{a(a-1)}}\;{}_{0}F_{1}(;a+1;z)$

.

This, and other important examples,

$\;{}_{1}F_{1}(a+1;b;z)-\,{}_{1}F_{1}(a;b;z)={\frac {z}{b}}\;{}_{1}F_{1}(a+1;b+1;z)$

,

$\;{}_{1}F_{1}(a;b-1;z)-\,{}_{1}F_{1}(a;b;z)={\frac {az}{b(b-1)}}\;{}_{1}F_{1}(a+1;b+1;z)$

,

$\;{}_{1}F_{1}(a;b-1;z)-\,{}_{1}F_{1}(a+1;b;z)={\frac {(a-b+1)z}{b(b-1)}}\;{}_{1}F_{1}(a+1;b+1;z)$

$\;{}_{2}F_{1}(a+1,b;c;z)-\,{}_{2}F_{1}(a,b;c;z)={\frac {bz}{c}}\;{}_{2}F_{1}(a+1,b+1;c+1;z)$

,

$\;{}_{2}F_{1}(a+1,b;c;z)-\,{}_{2}F_{1}(a,b+1;c;z)={\frac {(b-a)z}{c}}\;{}_{2}F_{1}(a+1,b+1;c+1;z)$

,

$\;{}_{2}F_{1}(a,b;c-1;z)-\,{}_{2}F_{1}(a+1,b;c;z)={\frac {(a-c+1)bz}{c(c-1)}}\;{}_{2}F_{1}(a+1,b+1;c+1;z)$

,

can be used to generate continued fraction expressions known as Gauss's continued fraction.

Similarly, by applying the differentiation formulas twice, there are ${\binom {p+q+3}{2}}$ such functions contained in

$\{1,\vartheta ,\vartheta ^{2}\}\;{}_{p}F_{q}(a_{1},\dots ,a_{p};b_{1},\dots ,b_{q};z),$

which has dimension three so any four are linearly dependent. This generates more identities and the process can be continued. The identities thus generated can be combined with each other to produce new ones in a different way.

A function obtained by adding ±1 to exactly one of the parameters *a**j*, *b**k* in

${}_{p}F_{q}(a_{1},\dots ,a_{p};b_{1},\dots ,b_{q};z)$

is called **contiguous** to

${}_{p}F_{q}(a_{1},\dots ,a_{p};b_{1},\dots ,b_{q};z).$

Using the technique outlined above, an identity relating ${}_{0}F_{1}(;a;z)$ and its two contiguous functions can be given, six identities relating ${}_{1}F_{1}(a;b;z)$ and any two of its four contiguous functions, and fifteen identities relating ${}_{2}F_{1}(a,b;c;z)$ and any two of its six contiguous functions have been found. The first one was derived in the previous paragraph. The last fifteen were given by (Gauss 1813).

## Identities

A number of other hypergeometric function identities were discovered in the nineteenth and twentieth centuries. A 20th century contribution to the methodology of proving these identities is the Egorychev method.

### Saalschütz's theorem

Saalschütz's theorem (Saalschütz 1890) is

${}_{3}F_{2}(a,b,-n;c,1+a+b-c-n;1)={\frac {(c-a)_{n}(c-b)_{n}}{(c)_{n}(c-a-b)_{n}}}.$

For extension of this theorem, see a research paper by Rakha & Rathie. According to (Andrews, Askey & Roy 1999, p. 69), it was in fact first discovered by Pfaff in 1797.

### Dixon's identity

Dixon's identity, first proved by Dixon (1902), gives the sum of a well-poised 3*F*2 at 1:

${}_{3}F_{2}(a,b,c;1+a-b,1+a-c;1)={\frac {\Gamma (1+{\frac {a}{2}})\Gamma (1+{\frac {a}{2}}-b-c)\Gamma (1+a-b)\Gamma (1+a-c)}{\Gamma (1+a)\Gamma (1+a-b-c)\Gamma (1+{\frac {a}{2}}-b)\Gamma (1+{\frac {a}{2}}-c)}}.$

For generalization of Dixon's identity, see a paper by Lavoie, et al.

### Dougall's formula

Dougall's formula (Dougall 1907) gives the sum of a very well-poised series that is terminating and 2-balanced.

${\begin{aligned}{}_{7}F_{6}&\left({\begin{matrix}a&1+{\frac {a}{2}}&b&c&d&e&-m\\&{\frac {a}{2}}&1+a-b&1+a-c&1+a-d&1+a-e&1+a+m\\\end{matrix}};1\right)=\\&={\frac {(1+a)_{m}(1+a-b-c)_{m}(1+a-c-d)_{m}(1+a-b-d)_{m}}{(1+a-b)_{m}(1+a-c)_{m}(1+a-d)_{m}(1+a-b-c-d)_{m}}}.\end{aligned}}$

Terminating means that *m* is a non-negative integer and 2-balanced means that

$1+2a=b+c+d+e-m.$

Many of the other formulas for special values of hypergeometric functions can be derived from this as special or limiting cases. It is also called the Dougall-Ramanujan identity. It is a special case of Jackson's identity, and it gives Dixon's identity and Saalschütz's theorem as special cases.

### Generalization of Kummer's transformations and identities for 2*F*2

**Identity 1.**

$e^{-x}\;{}_{2}F_{2}(a,1+d;c,d;x)={}_{2}F_{2}(c-a-1,f+1;c,f;-x)$

where

$f={\frac {d(a-c+1)}{a-d}}$

;

**Identity 2.**

$e^{-{\frac {x}{2}}}\,{}_{2}F_{2}\left(a,1+b;2a+1,b;x\right)={}_{0}F_{1}\left(;a+{\tfrac {1}{2}};{\tfrac {x^{2}}{16}}\right)-{\frac {x\left(1-{\tfrac {2a}{b}}\right)}{2(2a+1)}}\;{}_{0}F_{1}\left(;a+{\tfrac {3}{2}};{\tfrac {x^{2}}{16}}\right),$

which links Bessel functions to 2*F*2; this reduces to Kummer's second formula for *b* = 2*a*:

**Identity 3.**

$e^{-{\frac {x}{2}}}\,{}_{1}F_{1}(a,2a,x)={}_{0}F_{1}\left(;a+{\tfrac {1}{2}};{\tfrac {x^{2}}{16}}\right)$

.

**Identity 4.**

${\begin{aligned}{}_{2}F_{2}(a,b;c,d;x)=&\sum _{i=0}{\frac {{b-d \choose i}{a+i-1 \choose i}}{{c+i-1 \choose i}{d+i-1 \choose i}}}\;{}_{1}F_{1}(a+i;c+i;x){\frac {x^{i}}{i!}}\\=&e^{x}\sum _{i=0}{\frac {{b-d \choose i}{a+i-1 \choose i}}{{c+i-1 \choose i}{d+i-1 \choose i}}}\;{}_{1}F_{1}(c-a;c+i;-x){\frac {x^{i}}{i!}},\end{aligned}}$

which is a finite sum if *b-d* is a non-negative integer.

### Kummer's relation

Kummer's relation is

${}_{2}F_{1}\left(2a,2b;a+b+{\tfrac {1}{2}};x\right)={}_{2}F_{1}\left(a,b;a+b+{\tfrac {1}{2}};4x(1-x)\right).$

### Clausen's formula

Clausen's formula

${}_{3}F_{2}(2c-2s-1,2s,c-{\tfrac {1}{2}};2c-1,c;x)=\,{}_{2}F_{1}(c-s-{\tfrac {1}{2}},s;c;x)^{2}$

was used by de Branges to prove the Bieberbach conjecture.

## Special cases

Many of the special functions in mathematics are special cases of the confluent hypergeometric function or the hypergeometric function; see the corresponding articles for examples.

### The series 0*F*0

As noted earlier, ${}_{0}F_{0}(;;z)=e^{z}$ . The differential equation for this function is ${\frac {d}{dz}}w=w$ , which has solutions $w=ke^{z}$ where *k* is a constant.

### The series 0*F*1

The functions of the form ${}_{0}F_{1}(;a;z)$ are called **confluent hypergeometric limit functions** and are closely related to Bessel functions.

The relationship is:

$J_{\alpha }(x)={\frac {({\tfrac {x}{2}})^{\alpha }}{\Gamma (\alpha +1)}}{}_{0}F_{1}\left(;\alpha +1;-{\tfrac {1}{4}}x^{2}\right).$

$I_{\alpha }(x)={\frac {({\tfrac {x}{2}})^{\alpha }}{\Gamma (\alpha +1)}}{}_{0}F_{1}\left(;\alpha +1;{\tfrac {1}{4}}x^{2}\right).$

The differential equation for this function is

$w=\left(z{\frac {d}{dz}}+a\right){\frac {dw}{dz}}$

or

$z{\frac {d^{2}w}{dz^{2}}}+a{\frac {dw}{dz}}-w=0.$

When *a* is not a positive integer, the substitution

$w=z^{1-a}u,$

gives a linearly independent solution

$z^{1-a}\;{}_{0}F_{1}(;2-a;z),$

so the general solution is

$k\;{}_{0}F_{1}(;a;z)+lz^{1-a}\;{}_{0}F_{1}(;2-a;z)$

where *k*, *l* are constants. (If *a* is a positive integer, the independent solution is given by the appropriate Bessel function of the second kind.)

A special case is:

${}_{0}F_{1}\left(;{\frac {1}{2}};-{\frac {z^{2}}{4}}\right)=\cos z$

### The series 1*F*0

An important case is:

${}_{1}F_{0}(a;;z)=(1-z)^{-a}.$

The differential equation for this function is

${\frac {d}{dz}}w=\left(z{\frac {d}{dz}}+a\right)w,$

or

$(1-z){\frac {dw}{dz}}=aw,$

which has solutions

$w=k(1-z)^{-a}$

where *k* is a constant.

${}_{1}F_{0}(1;;z)=\sum _{n\geqslant 0}z^{n}=(1-z)^{-1}$

is the

geometric series

with ratio

z

and coefficient 1.

$z~{}_{1}F_{0}(2;;z)=\sum _{n\geqslant 0}nz^{n}=z(1-z)^{-2}$

is also useful.

### The series 1*F*1

The functions of the form ${}_{1}F_{1}(a;b;z)$ are called **confluent hypergeometric functions of the first kind**, also written $M(a;b;z)$ . The incomplete gamma function $\gamma (a,z)$ is a special case.

The differential equation for this function is

$\left(z{\frac {d}{dz}}+a\right)w=\left(z{\frac {d}{dz}}+b\right){\frac {dw}{dz}}$

or

$z{\frac {d^{2}w}{dz^{2}}}+(b-z){\frac {dw}{dz}}-aw=0.$

When *b* is not a positive integer, the substitution

$w=z^{1-b}u,$

gives a linearly independent solution

$z^{1-b}\;{}_{1}F_{1}(1+a-b;2-b;z),$

so the general solution is

$k\;{}_{1}F_{1}(a;b;z)+lz^{1-b}\;{}_{1}F_{1}(1+a-b;2-b;z)$

where *k*, *l* are constants.

When a is a non-positive integer, −*n*, ${}_{1}F_{1}(-n;b;z)$ is a polynomial. Up to constant factors, these are the Laguerre polynomials. This implies Hermite polynomials can be expressed in terms of 1*F*1 as well.

### The series 1*F*2

Relations to other functions are known for certain parameter combinations only.

The function $x\;{}_{1}F_{2}\left({\frac {1}{2}};{\frac {3}{2}},{\frac {3}{2}};-{\frac {x^{2}}{4}}\right)$ is the antiderivative of the cardinal sine. With modified values of $a_{1}$ and $b_{1}$ , one obtains the antiderivative of $\sin(x^{\beta })/x^{\alpha }$ .

The Lommel function is $s_{\mu ,\nu }(z)={\frac {z^{\mu +1}}{(\mu -\nu +1)(\mu +\nu +1)}}{}_{1}F_{2}\left(1;{\frac {\mu }{2}}-{\frac {\nu }{2}}+{\frac {3}{2}},{\frac {\mu }{2}}+{\frac {\nu }{2}}+{\frac {3}{2}};-{\frac {z^{2}}{4}}\right)$ .

### The series 2*F*0

The confluent hypergeometric function of the second kind can be written as:

$U(a,b,z)=z^{-a}\;{}_{2}F_{0}\left(a,a-b+1;;-{\frac {1}{z}}\right).$

### The series 2*F*1

Historically, the most important are the functions of the form ${}_{2}F_{1}(a,b;c;z)$ . These are sometimes called **Gauss's hypergeometric functions**, classical standard hypergeometric or often simply hypergeometric functions. The term **Generalized hypergeometric function** is used for the functions *p**F**q* if there is risk of confusion. This function was first studied in detail by Carl Friedrich Gauss, who explored the conditions for its convergence.

The differential equation for this function is

$\left(z{\frac {d}{dz}}+a\right)\left(z{\frac {d}{dz}}+b\right)w=\left(z{\frac {d}{dz}}+c\right){\frac {dw}{dz}}$

or

$z(1-z){\frac {d^{2}w}{dz^{2}}}+\left[c-(a+b+1)z\right]{\frac {dw}{dz}}-ab\,w=0.$

It is known as the hypergeometric differential equation. When *c* is not a positive integer, the substitution

$w=z^{1-c}u$

gives a linearly independent solution

$z^{1-c}\;{}_{2}F_{1}(1+a-c,1+b-c;2-c;z),$

so the general solution for |*z*| < 1 is

$k\;{}_{2}F_{1}(a,b;c;z)+lz^{1-c}\;{}_{2}F_{1}(1+a-c,1+b-c;2-c;z)$

where *k*, *l* are constants. Different solutions can be derived for other values of *z*. In fact there are 24 solutions, known as the Kummer solutions, derivable using various identities, valid in different regions of the complex plane.

When *a* is a non-positive integer, −*n*,

${}_{2}F_{1}(-n,b;c;z)$

is a polynomial. Up to constant factors and scaling, these are the Jacobi polynomials. Several other classes of orthogonal polynomials, up to constant factors, are special cases of Jacobi polynomials, so these can be expressed using 2*F*1 as well. This includes Legendre polynomials and Chebyshev polynomials.

A wide range of integrals of elementary functions can be expressed using the hypergeometric function, e.g.:

$\int _{0}^{x}{\sqrt {1+y^{\alpha }}}\,\mathrm {d} y={\frac {x}{2+\alpha }}\left\{\alpha \;{}_{2}F_{1}\left({\tfrac {1}{\alpha }},{\tfrac {1}{2}};1+{\tfrac {1}{\alpha }};-x^{\alpha }\right)+2{\sqrt {x^{\alpha }+1}}\right\},\qquad \alpha \neq 0.$

### The series 2*F*2

The hypergeometric series ${}_{2}F_{2}$ is generally associated with integrals of products of power functions and the exponential function. As such, the exponential integral can be written as:

$\operatorname {Ei} (x)=x{}_{2}F_{2}(1,1;2,2;x)+\ln x+\gamma .$

### The series 3*F*0

The Mott polynomials can be written as:

$s_{n}(x)=(-x/2)^{n}{}_{3}F_{0}(-n,{\frac {1-n}{2}},1-{\frac {n}{2}};;-{\frac {4}{x^{2}}}).$

### The series 3*F*2

The function

$\operatorname {Li} _{2}(x)=\sum _{n>0}\,{x^{n}}{n^{-2}}=x\;{}_{3}F_{2}(1,1,1;2,2;x)$

is the dilogarithm

Furthermore,

$_{3}F_{2}(1,1,1+n;2,2;x)={\frac {1}{n!}}\sum _{k=0}^{n}{\biggl [}{n \atop k}{\biggr ]}{\frac {\operatorname {Li} _{2-k}(x)}{x}}$

,

where ${\biggl [}{n \atop k}{\biggr ]}$ is the unsigned Stirling number of the first kind.

The function

$Q_{n}(x;a,b,N)={}_{3}F_{2}(-n,-x,n+a+b+1;a+1,-N+1;1)$

is a Hahn polynomial.

### The series 4*F*3

The function

$p_{n}(t^{2})=(a+b)_{n}(a+c)_{n}(a+d)_{n}\;{}_{4}F_{3}\left(-n,a+b+c+d+n-1,a-t,a+t;a+b,a+c,a+d;1\right)$

is a Wilson polynomial.

All roots of a quintic equation can be expressed in terms of radicals and the Bring radical, which is the real solution to $x^{5}+x+a=0$ . The Bring radical can be written as:

$\operatorname {BR} (a)=-a\;{}_{4}F_{3}\left({\frac {1}{5}},{\frac {2}{5}},{\frac {3}{5}},{\frac {4}{5}};{\frac {1}{2}},{\frac {3}{4}},{\frac {5}{4}};-{\frac {3125a^{4}}{256}}\right).$

The partition function $Z(K)$ of the 2D isotropic Ising model with no external magnetic field was found by Onsager in the 1940s and can be expressed as

$\ln Z(K)=\ln(2\cosh 2K)-k^{2}{}_{4}F_{3}\left(1,1,{\frac {3}{2}},{\frac {3}{2}};2,2,2;16k^{2}\right),$

with $K={\frac {J}{k_{\mathrm {B} }T}}$ and $k={\frac {1}{2}}\tanh 2K\,\operatorname {sech} 2K$ .

### The series q+1*F*q

The functions

$\operatorname {Li} _{q}(z)=z\;{}_{q+1}F_{q}\left(1,1,\ldots ,1;2,2,\ldots ,2;z\right)$

$\operatorname {Li} _{-p}(z)=z\;{}_{p}F_{p-1}\left(2,2,\ldots ,2;1,1,\ldots ,1;z\right)$

for $q\in \mathbb {N} _{0}$ and $p\in \mathbb {N}$ are the Polylogarithm.

For each integer *n*≥2, the roots of the polynomial *x**n*−*x*+t can be expressed as a sum of at most *N*−1 hypergeometric functions of type *n*+1F*n*, which can always be reduced by eliminating at least one pair of *a* and *b* parameters.

## Generalizations

The generalized hypergeometric function is linked to the Meijer G-function and the MacRobert E-function. Hypergeometric series were generalised to several variables, for example by Paul Emile Appell and Joseph Kampé de Fériet; but a comparable general theory took long to emerge. Many identities were found, some quite remarkable. A generalization, the q-series analogues, called the basic hypergeometric series, were given by Eduard Heine in the late nineteenth century. Here, the ratios considered of successive terms, instead of a rational function of *n*, are a rational function of *qn*. Another generalization, the elliptic hypergeometric series, are those series where the ratio of terms is an elliptic function (a doubly periodic meromorphic function) of *n*.

During the twentieth century this was a fruitful area of combinatorial mathematics, with numerous connections to other fields. There are a number of new definitions of general hypergeometric functions, by Aomoto, Israel Gelfand and others; and applications for example to the combinatorics of arranging a number of hyperplanes in complex *N*-space (see arrangement of hyperplanes).

Special hypergeometric functions occur as zonal spherical functions on Riemannian symmetric spaces and semi-simple Lie groups. Their importance and role can be understood through the following example: the hypergeometric series 2*F*1 has the Legendre polynomials as a special case, and when considered in the form of spherical harmonics, these polynomials reflect, in a certain sense, the symmetry properties of the two-sphere or, equivalently, the rotations given by the Lie group SO(3). In tensor product decompositions of concrete representations of this group Clebsch–Gordan coefficients are met, which can be written as 3*F*2 hypergeometric series.

Bilateral hypergeometric series are a generalization of hypergeometric functions where one sums over all integers, not just the positive ones.

Fox–Wright functions are a generalization of generalized hypergeometric functions where the Pochhammer symbols in the series expression are generalised to gamma functions of linear expressions in the index *n*.
