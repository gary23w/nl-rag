---
title: "Basic hypergeometric series"
source: https://en.wikipedia.org/wiki/Basic_hypergeometric_series
domain: hypergeometric-functions
license: CC-BY-SA-4.0
tags: hypergeometric function, confluent hypergeometric function, pochhammer symbol, hypergeometric series
fetched: 2026-07-02
---

# Basic hypergeometric series

In mathematics, **basic hypergeometric series**, or ***q*-hypergeometric series**, are *q*-analogue generalizations of generalized hypergeometric series, and are in turn generalized by elliptic hypergeometric series. A series *x**n* is called hypergeometric if the ratio of successive terms *x**n*+1/*x**n* is a rational function of *n*. If the ratio of successive terms is a rational function of *q**n*, then the series is called a basic hypergeometric series. The number *q* is called the base.

The basic hypergeometric series ${}_{2}\phi _{1}(q^{\alpha },q^{\beta };q^{\gamma };q,x)$ was first considered by Eduard Heine (1846). It becomes the hypergeometric series ${\displaystyle F(\alpha ,\beta$ in the limit when base $q=1$ .

## Definition

There are two forms of basic hypergeometric series, the **unilateral basic hypergeometric series** φ, and the more general **bilateral basic hypergeometric series** ψ. The **unilateral basic hypergeometric series** is defined as

$\;_{j}\phi _{k}\left[{\begin{matrix}a_{1}&a_{2}&\ldots &a_{j}\\b_{1}&b_{2}&\ldots &b_{k}\end{matrix}};q,z\right]=\sum _{n=0}^{\infty }{\frac {(a_{1},a_{2},\ldots ,a_{j};q)_{n}}{(b_{1},b_{2},\ldots ,b_{k},q;q)_{n}}}\left((-1)^{n}q^{n \choose 2}\right)^{1+k-j}z^{n}$

where

$(a_{1},a_{2},\ldots ,a_{m};q)_{n}=(a_{1};q)_{n}(a_{2};q)_{n}\ldots (a_{m};q)_{n}$

and

$(a;q)_{n}=\prod _{k=0}^{n-1}(1-aq^{k})=(1-a)(1-aq)(1-aq^{2})\cdots (1-aq^{n-1})$

is the *q*-shifted factorial. The most important special case is when *j* = *k* + 1, when it becomes

$\;_{k+1}\phi _{k}\left[{\begin{matrix}a_{1}&a_{2}&\ldots &a_{k}&a_{k+1}\\b_{1}&b_{2}&\ldots &b_{k}\end{matrix}};q,z\right]=\sum _{n=0}^{\infty }{\frac {(a_{1},a_{2},\ldots ,a_{k+1};q)_{n}}{(b_{1},b_{2},\ldots ,b_{k},q;q)_{n}}}z^{n}.$

This series is called *balanced* if *a*1 ... *a**k* + 1 = *b*1 ...*b**k**q*. This series is called *well poised* if *a*1*q* = *a*2*b*1 = ... = *a**k* + 1*b**k*, and *very well poised* if in addition *a*2 = −*a*3 = *qa*11/2. The unilateral basic hypergeometric series is a q-analog of the hypergeometric series since

$\lim _{q\to 1}\;_{j}\phi _{k}\left[{\begin{matrix}q^{a_{1}}&q^{a_{2}}&\ldots &q^{a_{j}}\\q^{b_{1}}&q^{b_{2}}&\ldots &q^{b_{k}}\end{matrix}};q,(q-1)^{1+k-j}z\right]=\;_{j}F_{k}\left[{\begin{matrix}a_{1}&a_{2}&\ldots &a_{j}\\b_{1}&b_{2}&\ldots &b_{k}\end{matrix}};z\right]$

holds (Koekoek & Swarttouw (1996)). The **bilateral basic hypergeometric series**, corresponding to the bilateral hypergeometric series, is defined as

$\;_{j}\psi _{k}\left[{\begin{matrix}a_{1}&a_{2}&\ldots &a_{j}\\b_{1}&b_{2}&\ldots &b_{k}\end{matrix}};q,z\right]=\sum _{n=-\infty }^{\infty }{\frac {(a_{1},a_{2},\ldots ,a_{j};q)_{n}}{(b_{1},b_{2},\ldots ,b_{k};q)_{n}}}\left((-1)^{n}q^{n \choose 2}\right)^{k-j}z^{n}.$

The most important special case is when *j* = *k*, when it becomes

$\;_{k}\psi _{k}\left[{\begin{matrix}a_{1}&a_{2}&\ldots &a_{k}\\b_{1}&b_{2}&\ldots &b_{k}\end{matrix}};q,z\right]=\sum _{n=-\infty }^{\infty }{\frac {(a_{1},a_{2},\ldots ,a_{k};q)_{n}}{(b_{1},b_{2},\ldots ,b_{k};q)_{n}}}z^{n}.$

The unilateral series can be obtained as a special case of the bilateral one by setting one of the *b* variables equal to *q*, at least when none of the *a* variables is a power of *q*, as all the terms with *n* < 0 then vanish.

## Simple series

Some simple series expressions include

${\frac {z}{1-q}}\;_{2}\phi _{1}\left[{\begin{matrix}q\;q\\q^{2}\end{matrix}}\;;q,z\right]={\frac {z}{1-q}}+{\frac {z^{2}}{1-q^{2}}}+{\frac {z^{3}}{1-q^{3}}}+\ldots$

and

${\frac {z}{1-q^{1/2}}}\;_{2}\phi _{1}\left[{\begin{matrix}q\;q^{1/2}\\q^{3/2}\end{matrix}}\;;q,z\right]={\frac {z}{1-q^{1/2}}}+{\frac {z^{2}}{1-q^{3/2}}}+{\frac {z^{3}}{1-q^{5/2}}}+\ldots$

and

$\;_{2}\phi _{1}\left[{\begin{matrix}q\;-1\\-q\end{matrix}}\;;q,z\right]=1+{\frac {2z}{1+q}}+{\frac {2z^{2}}{1+q^{2}}}+{\frac {2z^{3}}{1+q^{3}}}+\ldots .$

## The *q*-binomial theorem

The *q*-binomial theorem (first published in 1811 by Heinrich August Rothe) states that $\;_{1}\phi _{0}(a;q,z)={\frac {(az;q)_{\infty }}{(z;q)_{\infty }}}=\prod _{n=0}^{\infty }{\frac {1-aq^{n}z}{1-q^{n}z}}.$ It can be proved by repeatedly applying the identity $\;_{1}\phi _{0}(a;q,z)={\frac {1-az}{1-z}}\;_{1}\phi _{0}(a;q,qz).$ When ${\textstyle a=q^{-N}}$ is a negative integer power of *q*, the hypergeometric sum is finite and one recovers the finite form $\sum _{n=0}^{N}y^{n}q^{n(n+1)/2}{\begin{bmatrix}N\\n\end{bmatrix}}_{q}=\prod _{k=1}^{N}\left(1+yq^{k}\right)$ of the *q*-binomial theorem (also sometimes known as the Cauchy binomial theorem). Here ${\begin{bmatrix}N\\n\end{bmatrix}}_{q}$ is a *q*-binomial coefficient.

The special case of *a* = 0 is closely related to the *q*-exponential.

## Ramanujan's identity

Srinivasa Ramanujan gave the identity $\;_{1}\psi _{1}\left[{\begin{matrix}a\\b\end{matrix}};q,z\right]=\sum _{n=-\infty }^{\infty }{\frac {(a;q)_{n}}{(b;q)_{n}}}z^{n}={\frac {(b/a,q,q/az,az;q)_{\infty }}{(b,b/az,q/a,z;q)_{\infty }}}$ valid for |*q*| < 1 and |*b*/*a*| < |*z*| < 1. Similar identities for $\;_{6}\psi _{6}$ have been given by Bailey. Such identities can be understood to be generalizations of the Jacobi triple product theorem, which can be written using q-series as

$\sum _{n=-\infty }^{\infty }q^{n(n+1)/2}z^{n}=(q;q)_{\infty }\;(-1/z;q)_{\infty }\;(-zq;q)_{\infty }.$

Gwynneth Coogan and Ken Ono give a related formal power series

$A(z;q){\stackrel {\rm {def}}{=}}{\frac {1}{1+z}}\sum _{n=0}^{\infty }{\frac {(z;q)_{n}}{(-zq;q)_{n}}}z^{n}=\sum _{n=0}^{\infty }(-1)^{n}z^{2n}q^{n^{2}}.$

## Watson's contour integral

As an analogue of the Barnes integral for the hypergeometric series, Watson showed that

${}_{2}\phi _{1}(a,b;c;q,z)={\frac {-1}{2\pi i}}{\frac {(a,b;q)_{\infty }}{(q,c;q)_{\infty }}}\int _{-i\infty }^{i\infty }{\frac {(qq^{s},cq^{s};q)_{\infty }}{(aq^{s},bq^{s};q)_{\infty }}}{\frac {\pi (-z)^{s}}{\sin \pi s}}ds$

where the poles of $(aq^{s},bq^{s};q)_{\infty }$ lie to the left of the contour and the remaining poles lie to the right. There is a similar contour integral for *r*+1φ*r*. This contour integral gives an analytic continuation of the basic hypergeometric function in *z*.

## Matrix version

The basic hypergeometric matrix function can be defined as follows:

${}_{2}\phi _{1}(A,B;C;q,z):=\sum _{n=0}^{\infty }{\frac {(A;q)_{n}(B;q)_{n}}{(C;q)_{n}(q;q)_{n}}}z^{n},\quad (A;q)_{0}:=1,\quad (A;q)_{n}:=\prod _{k=0}^{n-1}(1-Aq^{k}).$

The ratio test shows that this matrix function is absolutely convergent.
