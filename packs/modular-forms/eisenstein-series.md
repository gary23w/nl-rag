---
title: "Eisenstein series"
source: https://en.wikipedia.org/wiki/Eisenstein_series
domain: modular-forms
license: CC-BY-SA-4.0
tags: modular form, modular group, eisenstein series, hecke operator
fetched: 2026-07-02
---

# Eisenstein series

In mathematics, **Eisenstein series**, named after German mathematician Gotthold Eisenstein, are particular modular forms with infinite series expansions that may be written down directly. Originally defined for the modular group, Eisenstein series can be generalized in the theory of automorphic forms.

## Eisenstein series for the modular group

Let $\tau$ be a complex number with strictly positive imaginary part. The **holomorphic Eisenstein series** $G_{2k}(\tau )$ of weight $2k$ , where $k\geq 2$ is an integer, is defined by

$G_{2k}(\tau )=\sum _{(m,n)\in \mathbb {Z} ^{2}\setminus \{(0,0)\}}{\frac {1}{(m+n\tau )^{2k}}}.$

This series absolutely converges to a holomorphic function of $\tau$ in the upper half-plane and its Fourier expansion given below shows that it extends to a holomorphic function at $\tau =i\infty$ . It is a remarkable fact that the Eisenstein series is a modular form. Indeed, the key property is its $\operatorname {SL} (2,\mathbb {Z} )$ -invariance. Explicitly, if $a,b,c,d$ are integers and $ad-bc=1$ then

$G_{2k}\left({\frac {a\tau +b}{c\tau +d}}\right)=(c\tau +d)^{2k}G_{2k}(\tau )$

(Proof)

${\begin{aligned}G_{2k}\left({\frac {a\tau +b}{c\tau +d}}\right)&=\sum _{(m,n)\in \mathbb {Z} ^{2}\setminus \{(0,0)\}}{\frac {1}{\left(m+n{\frac {a\tau +b}{c\tau +d}}\right)^{2k}}}\\&=\sum _{(m,n)\in \mathbb {Z} ^{2}\setminus \{(0,0)\}}{\frac {(c\tau +d)^{2k}}{(md+nb+(mc+na)\tau )^{2k}}}\\&=\sum _{\left(m',n'\right)=(m,n){\begin{pmatrix}d\ \ c\\b\ \ a\end{pmatrix}} \atop (m,n)\in \mathbb {Z} ^{2}\setminus \{(0,0)\}}{\frac {(c\tau +d)^{2k}}{\left(m'+n'\tau \right)^{2k}}}\end{aligned}}$

If $ad-bc=1$ then

${\begin{pmatrix}d&c\\b&a\end{pmatrix}}^{-1}={\begin{pmatrix}\ a&-c\\-b&\ d\end{pmatrix}}$

so that

$(m,n)\mapsto (m,n){\begin{pmatrix}d&c\\b&a\end{pmatrix}}$

is a bijection $\mathbb {Z} ^{2}\to \mathbb {Z} ^{2}$ , i.e.:

$\sum _{\left(m',n'\right)=(m,n){\begin{pmatrix}d\ \ c\\b\ \ a\end{pmatrix}} \atop (m,n)\in \mathbb {Z} ^{2}\setminus \{(0,0)\}}{\frac {1}{\left(m'+n'\tau \right)^{2k}}}=\sum _{\left(m',n'\right)\in \mathbb {Z} ^{2}\setminus \{(0,0)\}}{\frac {1}{(m'+n'\tau )^{2k}}}=G_{2k}(\tau )$

Overall, if $ad-bc=1$ then

$G_{2k}\left({\frac {a\tau +b}{c\tau +d}}\right)=(c\tau +d)^{2k}G_{2k}(\tau )$

and

$G_{2k}$

is therefore a modular form of weight

$2k$

.

Note that it is important to assume that $k\geq 2$ to ensure absolute convergence of the series, as otherwise it would be illegitimate to change the order of summation in the proof of $\operatorname {SL} (2,\mathbb {Z} )$ -invariance. In fact, there are no nontrivial modular forms of weight 2. Nevertheless, an analogue of the holomorphic Eisenstein series can be defined even for $k=1$ , although it would only be a quasimodular form. It is also necessary that the weight be even, as otherwise the sum vanishes because the $(-m,-n)$ and $(m,n)$ terms cancel each other.

## Relation to modular invariants

The modular invariants $g_{2}$ and $g_{3}$ of an elliptic curve are given by the first two Eisenstein series:

${\begin{aligned}g_{2}&=60G_{4}\\g_{3}&=140G_{6}.\end{aligned}}$

The article on modular invariants provides expressions for these two functions in terms of theta functions.

## Recurrence relation

Any holomorphic modular form for the modular group can be written as a polynomial in $G_{4}$ and $G_{6}$ . Specifically, the higher order $G_{2k}$ can be written in terms of $G_{4}$ and $G_{6}$ through a recurrence relation. Let $d_{k}=(2k+3)!G_{2k+4}$ . Then the $d_{k}$ satisfy the relation

$\sum _{k=0}^{n}{n \choose k}d_{k}d_{n-k}={\frac {2n+9}{3n+6}}d_{n+2}$

for all $n\geq 0$ .

The $d_{k}$ occur in the series expansion for Weierstrass's elliptic functions:

${\begin{aligned}\wp (z)&={\frac {1}{z^{2}}}+z^{2}\sum _{k=0}^{\infty }{\frac {d_{k}z^{2k}}{k!}}\\&={\frac {1}{z^{2}}}+\sum _{k=1}^{\infty }(2k+1)G_{2k+2}z^{2k}.\end{aligned}}$

## Fourier series

Let $q=e^{2\pi i\tau }$ . Then the Fourier series of the Eisenstein series is

$G_{2k}(\tau )=2\zeta (2k){\Big (}1+c_{2k}\sum _{n=1}^{\infty }\sigma _{2k-1}(n)q^{n}{\Big )}.$

The coefficients $c_{2k}$ are given by

$c_{2k}={\frac {(2\pi i)^{2k}}{(2k-1)!\zeta (2k)}}={\frac {-4k}{B_{2k}}}={\frac {2}{\zeta (1-2k)}},$

where $B_{n}$ are the Bernoulli numbers, $\zeta$ is the Riemann zeta function and $\sigma _{p}(n)$ is the divisor sum function, i.e. the sum of the p -th powers of the divisors of n . In particular, one has

$G_{4}(\tau )={\frac {\pi ^{4}}{45}}{\bigg (}1+240\sum _{n=1}^{\infty }\sigma _{3}(n)q^{n}{\bigg )}$

and

$G_{6}(\tau )={\frac {2\pi ^{6}}{945}}{\bigg (}1-504\sum _{n=1}^{\infty }\sigma _{5}(n)q^{n}{\bigg )}.$

The summation over q can be resummed as a Lambert series; that is, one has

$\sum _{n=1}^{\infty }q^{n}\sigma _{a}(n)=\sum _{n=1}^{\infty }{\frac {n^{a}q^{n}}{1-q^{n}}}$

for arbitrary complex $|q|<1$ and a . When working with the *q*-expansion of the Eisenstein series, this alternate notation is frequently introduced:

${\begin{aligned}E_{2k}(\tau )&={\frac {G_{2k}(\tau )}{2\zeta (2k)}}\\&=1+{\frac {2}{\zeta (1-2k)}}\sum _{n=1}^{\infty }{\frac {n^{2k-1}q^{n}}{1-q^{n}}}\\&=1-{\frac {4k}{B_{2k}}}\sum _{n=1}^{\infty }\sigma _{2k-1}(n)q^{n}\\&=1-{\frac {4k}{B_{2k}}}\sum _{d,n\geq 1}n^{2k-1}q^{nd}.\end{aligned}}$

## Identities involving Eisenstein series

### Theta functions

Given $q=e^{2\pi i\tau }$ , let

${\begin{aligned}E_{4}(\tau )&=1+240\sum _{n=1}^{\infty }{\frac {n^{3}q^{n}}{1-q^{n}}},\\[5pt]E_{6}(\tau )&=1-504\sum _{n=1}^{\infty }{\frac {n^{5}q^{n}}{1-q^{n}}},\\[5pt]E_{8}(\tau )&=1+480\sum _{n=1}^{\infty }{\frac {n^{7}q^{n}}{1-q^{n}}},\end{aligned}}$

and define the Jacobi theta functions (which normally use the nome $e^{\pi i\tau }$ )

${\begin{aligned}a&=\theta _{2}\left(0;e^{\pi i\tau }\right)=\vartheta _{10}(0;\tau ),\\b&=\theta _{3}\left(0;e^{\pi i\tau }\right)=\vartheta _{00}(0;\tau ),\\c&=\theta _{4}\left(0;e^{\pi i\tau }\right)=\vartheta _{01}(0;\tau )\end{aligned}},$

where $\theta _{m}$ and $\vartheta _{ij}$ are alternative notations. Then we have the symmetric relations

${\begin{aligned}E_{4}(\tau )&={\frac {1}{2}}\left(a^{8}+b^{8}+c^{8}\right),\\[5pt]E_{6}(\tau )&={\frac {1}{2}}{\sqrt {\frac {\left(a^{8}+b^{8}+c^{8}\right)^{3}-54(abc)^{8}}{2}}},\\[5pt]E_{8}(\tau )&={\frac {1}{2}}\left(a^{16}+b^{16}+c^{16}\right)=a^{8}b^{8}+a^{8}c^{8}+b^{8}c^{8}.\end{aligned}}$

Basic algebra immediately implies

$E_{4}^{3}-E_{6}^{2}={\frac {27}{4}}(abc)^{8},$

an expression related to the modular discriminant

$\Delta =g_{2}^{3}-27g_{3}^{2}=(2\pi )^{12}{\Big (}{\frac {abc}{2}}{\Big )}^{8}$

The third symmetric relation is a consequence of $E_{8}=E_{4}^{2}$ and $a^{4}-b^{4}+c^{4}=0$ .

### Products of Eisenstein series

Eisenstein series form the most explicit examples of modular forms for the full modular group $\operatorname {SL} (2,\mathbb {Z} )$ . Since the space of modular forms of weight $2k$ has dimension 1 for $2k=4,6,8,10,14$ , different products of Eisenstein series having those weights have to be equal up to a scalar multiple. In fact, we obtain the identities

$E_{4}^{2}=E_{8},\quad E_{4}E_{6}=E_{10},\quad E_{4}E_{10}=E_{14},\quad E_{6}E_{8}=E_{14}.$

Using the q -expansions of the Eisenstein series given above, they may be restated as identities involving the sums of powers of divisors:

${\bigg (}1+240\sum _{n=1}^{\infty }\sigma _{3}(n)q^{n}{\bigg )}^{2}=1+480\sum _{n=1}^{\infty }\sigma _{7}(n)q^{n},$

hence

$\sigma _{7}(n)=\sigma _{3}(n)+120\sum _{m=1}^{n-1}\sigma _{3}(m)\sigma _{3}(n-m),$

and similarly for the others. The theta function of an eight-dimensional even unimodular lattice $\Gamma$ is a modular form of weight 4 for the full modular group, which gives the following identities:

$\theta _{\Gamma }(\tau )=1+\sum _{n=1}^{\infty }r_{\Gamma }(2n)q^{n}=E_{4}(\tau ),\qquad r_{\Gamma }(n)=240\sigma _{3}(n)$

for the number $r_{\Gamma }(n)$ of vectors of the squared length $2n$ in the root lattice of the type *E*8.

Similar techniques involving holomorphic Eisenstein series twisted by a Dirichlet character produce formulas for the number of representations of a positive integer n ' as a sum of two, four, or eight squares in terms of the divisors of n .

Using the above recurrence relation, all higher $E_{2k}$ can be expressed as polynomials in $E_{4}$ and $E_{6}$ . For example,

${\begin{aligned}E_{8}&=E_{4}^{2}\\E_{10}&=E_{4}\cdot E_{6}\\691\cdot E_{12}&=441\cdot E_{4}^{3}+250\cdot E_{6}^{2}\\E_{14}&=E_{4}^{2}\cdot E_{6}\\3617\cdot E_{16}&=1617\cdot E_{4}^{4}+2000\cdot E_{4}\cdot E_{6}^{2}\\43867\cdot E_{18}&=38367\cdot E_{4}^{3}\cdot E_{6}+5500\cdot E_{6}^{3}\\174611\cdot E_{20}&=53361\cdot E_{4}^{5}+121250\cdot E_{4}^{2}\cdot E_{6}^{2}\\77683\cdot E_{22}&=57183\cdot E_{4}^{4}\cdot E_{6}+20500\cdot E_{4}\cdot E_{6}^{3}\\236364091\cdot E_{24}&=49679091\cdot E_{4}^{6}+176400000\cdot E_{4}^{3}\cdot E_{6}^{2}+10285000\cdot E_{6}^{4}\end{aligned}}$

Many relationships between products of Eisenstein series can be written in an elegant way using Hankel determinants, such as Garvan's identity

$\left({\frac {\Delta }{(2\pi )^{12}}}\right)^{2}=-{\frac {691}{1728^{2}\cdot 250}}\,{\begin{vmatrix}E_{4}&E_{6}&E_{8}\\E_{6}&E_{8}&E_{10}\\E_{8}&E_{10}&E_{12}\end{vmatrix}},$

where

$\Delta =(2\pi )^{12}{\frac {E_{4}^{3}-E_{6}^{2}}{1728}}$

is the modular discriminant.

### Ramanujan identities

Srinivasa Ramanujan gave several interesting identities between the first few Eisenstein series involving differentiation. Let

${\begin{aligned}L(q)&=1-24\sum _{n=1}^{\infty }{\frac {nq^{n}}{1-q^{n}}}=E_{2}(\tau ),\\[4pt]M(q)&=1+240\sum _{n=1}^{\infty }{\frac {n^{3}q^{n}}{1-q^{n}}}=E_{4}(\tau ),\\[4pt]N(q)&=1-504\sum _{n=1}^{\infty }{\frac {n^{5}q^{n}}{1-q^{n}}}=E_{6}(\tau ),\end{aligned}}$

then

${\begin{aligned}q{\frac {dL}{dq}}&={\frac {L^{2}-M}{12}},\\[5pt]q{\frac {dM}{dq}}&={\frac {LM-N}{3}},\\[5pt]q{\frac {dN}{dq}}&={\frac {LN-M^{2}}{2}}.\end{aligned}}$

These identities, like the identities between the series, yield arithmetical convolution identities involving the sum-of-divisor function. Following Ramanujan, to put these identities in the simplest form it is necessary to extend the domain of $\sigma _{p}(n)$ to include zero, by setting

$\sigma _{p}(0)={\frac {\zeta (-p)}{2}}.$

Then, for example,

$\sum _{k=0}^{n}\sigma (k)\sigma (n-k)={\frac {5}{12}}\sigma _{3}(n)-{\frac {n\sigma (n)}{2}}.$

Other identities of this type, but not directly related to the preceding relations between L , M and N functions, have been proved, as for example

${\begin{aligned}&\sum _{k=0}^{n}\sigma _{3}(k)\sigma _{3}(n-k)={\tfrac {1}{120}}\sigma _{7}(n),\\[4pt]&\sum _{k=0}^{n}\sigma (2k+1)\sigma _{3}(n-k)={\tfrac {1}{240}}\sigma _{5}(2n+1),\\[4pt]&\sum _{k=0}^{n}\sigma (3k+1)\sigma (3n-3k+1)={\tfrac {1}{9}}\sigma _{3}(3n+2).\end{aligned}}$

## Generalizations

Automorphic forms generalize the idea of modular forms for general semisimple Lie groups, where the modular group is replaced by an arithmetic group. Robert Langlands generalised the theory of Eisenstein series to this setting.

When the Lie group is of type A1 the theory resembles the classical case. For example, Hilbert modular forms are well-studied.
