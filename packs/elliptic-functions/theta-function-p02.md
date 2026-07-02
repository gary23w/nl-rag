---
title: "Theta function (part 2/2)"
source: https://en.wikipedia.org/wiki/Theta_function
domain: elliptic-functions
license: CC-BY-SA-4.0
tags: elliptic function, jacobi elliptic functions, weierstrass elliptic function, theta function
fetched: 2026-07-02
part: 2/2
---

## Derivation of the theta values

### Identity of the Euler beta function

In the following, three important theta function values are to be derived as examples:

This is how the Euler beta function is defined in its reduced form:

$\beta (x)={\frac {\Gamma (x)^{2}}{\Gamma (2x)}}$

In general, for all natural numbers $n\in \mathbb {N}$ this formula of the Euler beta function is valid:

${\frac {4^{-1/(n+2)}}{n+2}}\csc {\bigl (}{\frac {\pi }{n+2}}{\bigr )}\beta {\biggl [}{\frac {n}{2(n+2)}}{\biggr ]}=\int _{0}^{\infty }{\frac {1}{\sqrt {x^{n+2}+1}}}\,\mathrm {d} x$

### Exemplary elliptic integrals

In the following some *Elliptic Integral Singular Values* are derived:

| The ensuing function has the following lemniscatically elliptic antiderivative: ${\frac {1}{\sqrt {x^{4}+1}}}={\frac {\mathrm {d} }{\mathrm {d} x}}\,{\frac {1}{2}}F{\biggl [}2\arctan(x);{\frac {1}{2}}{\sqrt {2}}\,{\biggr ]}$ For the value $n=2$ this identity appears: ${\frac {1}{4{\sqrt {2}}}}\csc {\bigl (}{\frac {\pi }{4}}{\bigr )}\beta {\bigl (}{\frac {1}{4}}{\bigr )}=\int _{0}^{\infty }{\frac {1}{\sqrt {x^{4}+1}}}\,\mathrm {d} x={\biggl \{}{\color {blue}{\frac {1}{2}}F{\biggl [}2\arctan(x);{\frac {1}{2}}{\sqrt {2}}\,{\biggr ]}}{\biggr \}}_{x=0}^{x=\infty }=$ $={\frac {1}{2}}F{\bigl (}\pi ;{\frac {1}{2}}{\sqrt {2}}{\bigr )}=K{\bigl (}{\frac {1}{2}}{\sqrt {2}}{\bigr )}$ This result follows from that equation chain: ${\color {ForestGreen}K{\bigl (}{\frac {1}{2}}{\sqrt {2}}{\bigr )}={\frac {1}{4}}\beta {\bigl (}{\frac {1}{4}}{\bigr )}}$ |
|---|

| The following function has the following equianharmonic elliptic antiderivative: ${\frac {1}{\sqrt {x^{6}+1}}}={\frac {\mathrm {d} }{\mathrm {d} x}}\,{\frac {1}{6}}{\sqrt[{4}]{27}}F{\biggl [}2\arctan {\biggl (}{\frac {{\sqrt[{4}]{3}}\,x}{\sqrt {x^{2}+1}}}{\biggr )};{\frac {1}{4}}({\sqrt {6}}+{\sqrt {2}}){\biggr ]}$ For the value $n=4$ that identity appears: ${\frac {1}{6{\sqrt[{3}]{2}}}}\csc {\bigl (}{\frac {\pi }{6}}{\bigr )}\beta {\bigl (}{\frac {1}{3}}{\bigr )}=\int _{0}^{\infty }{\frac {1}{\sqrt {x^{6}+1}}}\,\mathrm {d} x={\biggl \{}{\color {blue}{\frac {1}{6}}{\sqrt[{4}]{27}}F{\biggl [}2\arctan {\biggl (}{\frac {{\sqrt[{4}]{3}}\,x}{\sqrt {x^{2}+1}}}{\biggr )};{\frac {1}{4}}({\sqrt {6}}+{\sqrt {2}}){\biggr ]}}{\biggr \}}_{x=0}^{x=\infty }=$ $={\frac {1}{6}}{\sqrt[{4}]{27}}F{\bigl [}2\arctan({\sqrt[{4}]{3}});{\frac {1}{4}}({\sqrt {6}}+{\sqrt {2}}){\bigr ]}={\frac {2}{9}}{\sqrt[{4}]{27}}K{\bigl [}{\frac {1}{4}}({\sqrt {6}}+{\sqrt {2}}){\bigr ]}={\frac {2}{3}}{\sqrt[{4}]{3}}K{\bigl [}{\frac {1}{4}}({\sqrt {6}}-{\sqrt {2}}){\bigr ]}$ This result follows from that equation chain: ${\color {ForestGreen}K{\bigl [}{\frac {1}{4}}({\sqrt {6}}-{\sqrt {2}}){\bigr ]}={\frac {1}{2{\sqrt[{3}]{2}}{\sqrt[{4}]{3}}}}\beta {\bigl (}{\frac {1}{3}}{\bigr )}}$ |
|---|

| And the following function has the following elliptic antiderivative: ${\frac {1}{\sqrt {x^{8}+1}}}=$ $={\frac {\mathrm {d} }{\mathrm {d} x}}\,{\frac {1}{4}}\sec {\bigl (}{\frac {\pi }{8}}{\bigr )}F{\biggl \{}2\arctan {\biggl [}{\frac {2\cos(\pi /8)\,x}{{\sqrt {x^{4}+{\sqrt {2}}\,x^{2}+1}}-x^{2}+1}}{\biggr ]};2{\sqrt[{4}]{2}}\sin {\bigl (}{\frac {\pi }{8}}{\bigr )}{\biggr \}}+{\frac {1}{4}}\sec {\bigl (}{\frac {\pi }{8}}{\bigr )}F{\biggl \{}\arcsin {\biggl [}{\frac {2\cos(\pi /8)\,x}{x^{2}+1}}{\biggr ]};\tan {\bigl (}{\frac {\pi }{8}}{\bigr )}{\biggr \}}$ For the value $n=6$ the following identity appears: ${\frac {1}{8{\sqrt[{4}]{2}}}}\csc {\bigl (}{\frac {\pi }{8}}{\bigr )}\beta {\bigl (}{\frac {3}{8}}{\bigr )}=\int _{0}^{\infty }{\frac {1}{\sqrt {x^{8}+1}}}\,\mathrm {d} x=$ $={\biggl \langle }{\color {blue}{\frac {1}{4}}\sec {\bigl (}{\frac {\pi }{8}}{\bigr )}F{\biggl \{}2\arctan {\biggl [}{\frac {2\cos(\pi /8)\,x}{{\sqrt {x^{4}+{\sqrt {2}}\,x^{2}+1}}-x^{2}+1}}{\biggr ]};2{\sqrt[{4}]{2}}\sin {\bigl (}{\frac {\pi }{8}}{\bigr )}{\biggr \}}+{\frac {1}{4}}\sec {\bigl (}{\frac {\pi }{8}}{\bigr )}F{\biggl \{}\arcsin {\biggl [}{\frac {2\cos(\pi /8)\,x}{x^{2}+1}}{\biggr ]};\tan {\bigl (}{\frac {\pi }{8}}{\bigr )}{\biggr \}}}{\biggr \rangle }_{x=0}^{x=\infty }=$ $={\frac {1}{4}}\sec {\bigl (}{\frac {\pi }{8}}{\bigr )}F{\bigl [}\pi ;2{\sqrt[{4}]{2}}\sin {\bigl (}{\frac {\pi }{8}}{\bigr )}{\bigr ]}={\frac {1}{2}}\sec {\bigl (}{\frac {\pi }{8}}{\bigr )}K({\sqrt {2{\sqrt {2}}-2}}{\bigr )}=2\sin {\bigl (}{\frac {\pi }{8}}{\bigr )}K({\sqrt {2}}-1)$ This result follows from that equation chain: ${\color {ForestGreen}K({\sqrt {2}}-1)={\frac {1}{8}}{\sqrt[{4}]{2}}\,({\sqrt {2}}+1)\,\beta {\bigl (}{\frac {3}{8}}{\bigr )}}$ |
|---|

### Combination of the integral identities with the nome

The elliptic nome function has these important values:

$q({\tfrac {1}{2}}{\sqrt {2}})=\exp(-\pi )$

$q[{\tfrac {1}{4}}({\sqrt {6}}-{\sqrt {2}})]=\exp(-{\sqrt {3}}\,\pi )$

$q({\sqrt {2}}-1)=\exp(-{\sqrt {2}}\,\pi )$

For the proof of the correctness of these nome values, see the article Nome (mathematics)!

On the basis of these integral identities and the above-mentioned **Definition and identities to the theta functions** in the same section of this article, exemplary theta zero values shall be determined now:

| $\theta _{3}[q(k)]={\sqrt {2\pi ^{-1}K(k)}}$ |
|---|

$\theta _{3}[\exp(-\pi )]=\theta _{3}[q({\tfrac {1}{2}}{\sqrt {2}})]={\sqrt {2\pi ^{-1}K({\tfrac {1}{2}}{\sqrt {2}})}}=2^{-1/2}\pi ^{-1/2}\beta ({\tfrac {1}{4}})^{1/2}=2^{-1/4}{\sqrt[{4}]{\pi }}\,{\Gamma {\bigl (}{\tfrac {3}{4}}{\bigr )}}^{-1}$

$\theta _{3}[\exp(-{\sqrt {3}}\,\pi )]=\theta _{3}{\bigl \{}q{\bigl [}{\tfrac {1}{4}}({\sqrt {6}}-{\sqrt {2}}){\bigr ]}{\bigr \}}={\sqrt {2\pi ^{-1}K{\bigl [}{\tfrac {1}{4}}({\sqrt {6}}-{\sqrt {2}}){\bigr ]}}}=2^{-1/6}3^{-1/8}\pi ^{-1/2}\beta ({\tfrac {1}{3}})^{1/2}$

$\theta _{3}[\exp(-{\sqrt {2}}\,\pi )]=\theta _{3}[q({\sqrt {2}}-1)]={\sqrt {2\pi ^{-1}K({\sqrt {2}}-1)}}=2^{-1/8}\cos({\tfrac {1}{8}}\pi )\,\pi ^{-1/2}\beta ({\tfrac {3}{8}})^{1/2}$

| $\theta _{4}[q(k)]={\sqrt[{4}]{1-k^{2}}}\,{\sqrt {2\pi ^{-1}K(k)}}$ |
|---|

$\theta _{4}[\exp(-{\sqrt {2}}\,\pi )]=\theta _{4}[q({\sqrt {2}}-1)]={\sqrt[{4}]{2{\sqrt {2}}-2}}\,{\sqrt {2\pi ^{-1}K({\sqrt {2}}-1)}}=2^{-1/4}\cos({\tfrac {1}{8}}\pi )^{1/2}\,\pi ^{-1/2}\beta ({\tfrac {3}{8}})^{1/2}$


## Partition sequences and Pochhammer products

### Regular partition number sequence

The regular partition sequence $P(n)$ itself indicates the number of ways in which a positive integer number n can be split into positive integer summands. For the numbers $n=1$ to $n=5$ , the associated partition numbers P with all associated number partitions are listed in the following table:

| n | P(n) | paying partitions |
|---|---|---|
| 0 | 1 | () empty partition/empty sum |
| 1 | 1 | (1) |
| 2 | 2 | (1+1), (2) |
| 3 | 3 | (1+1+1), (1+2), (3) |
| 4 | 5 | (1+1+1+1), (1+1+2), (2+2), (1+3), (4) |
| 5 | 7 | (1+1+1+1+1), (1+1+1+2), (1+2+2), (1+1+3), (2+3), (1+4), (5) |

The generating function of the regular partition number sequence can be represented via Pochhammer product in the following way:

$\sum _{k=0}^{\infty }P(k)x^{k}={\frac {1}{(x;x)_{\infty }}}=\theta _{3}(x)^{-1/6}\theta _{4}(x)^{-2/3}{\biggl [}{\frac {\theta _{3}(x)^{4}-\theta _{4}(x)^{4}}{16\,x}}{\biggr ]}^{-1/24}$

The summandization of the now mentioned Pochhammer product is described by the pentagonal number theorem in this way:

$(x;x)_{\infty }=1+\sum _{n=1}^{\infty }{\bigl [}-x^{{\text{Fn}}(2n-1)}-x^{{\text{Kr}}(2n-1)}+x^{{\text{Fn}}(2n)}+x^{{\text{Kr}}(2n)}{\bigr ]}$

The following basic definitions apply to the pentagonal numbers and the card house numbers:

${\text{Fn}}(z)={\tfrac {1}{2}}z(3z-1)$

${\text{Kr}}(z)={\tfrac {1}{2}}z(3z+1)$

As a further application one obtains a formula for the third power of the Euler product:

$(x;x)^{3}=\prod _{n=1}^{\infty }(1-x^{n})^{3}=\sum _{m=0}^{\infty }(-1)^{m}(2m+1)x^{m(m+1)/2}$

### Strict partition number sequence

And the strict partition sequence $Q(n)$ indicates the number of ways in which such a positive integer number n can be split into positive integer summands such that each summand appears at most once and no summand value occurs repeatedly. Exactly the same sequence is also generated if in the partition only odd summands are included, but these odd summands may occur more than once. Both representations for the strict partition number sequence are compared in the following table:

| n | Q(n) | Number partitions without repeated summands | Number partitions with only odd addends |
|---|---|---|---|
| 0 | 1 | () empty partition/empty sum | () empty partition/empty sum |
| 1 | 1 | (1) | (1) |
| 2 | 1 | (2) | (1+1) |
| 3 | 2 | (1+2), (3) | (1+1+1), (3) |
| 4 | 2 | (1+3), (4) | (1+1+1+1), (1+3) |
| 5 | 3 | (2+3), (1+4), (5) | (1+1+1+1+1), (1+1+3), (5) |
| 6 | 4 | (1+2+3), (2+4), (1+5), (6) | (1+1+1+1+1+1), (1+1+1+3), (3+3), (1+5) |
| 7 | 5 | (1+2+4), (3+4), (2+5), (1+6), (7) | (1+1+1+1+1+1+1), (1+1+1+1+3), (1+3+3), (1+1+5), (7) |
| 8 | 6 | (1+3+4), (1+2+5), (3+5), (2+6), (1+7), (8) | (1+1+1+1+1+1+1+1), (1+1+1+1+1+3), (1+1+3+3), (1+1+1+ 5), (3+5), (1+7) |

The generating function of the strict partition number sequence can be represented using Pochhammer's product:

$\sum _{k=0}^{\infty }Q(k)x^{k}={\frac {1}{(x;x^{2})_{\infty }}}=\theta _{3}(x)^{1/6}\theta _{4}(x)^{-1/3}{\biggl [}{\frac {\theta _{3}(x)^{4}-\theta _{4}(x)^{4}}{16\,x}}{\biggr ]}^{1/24}$

### Overpartition number sequence

The Maclaurin series for the reciprocal of the function *ϑ01* has the numbers of over partition sequence as coefficients with a positive sign:

${\frac {1}{\theta _{4}(x)}}=\prod _{n=1}^{\infty }{\frac {1+x^{n}}{1-x^{n}}}=\sum _{k=0}^{\infty }{\overline {P}}(k)x^{k}$

${\frac {1}{\theta _{4}(x)}}=1+2x+4x^{2}+8x^{3}+14x^{4}+24x^{5}+40x^{6}+64x^{7}+100x^{8}+154x^{9}+232x^{10}+\dots$

If, for a given number k , all partitions are set up in such a way that the summand size never increases, and all those summands that do not have a summand of the same size to the left of themselves can be marked for each partition of this type, then it will be the resulting number of the marked partitions depending on k by the overpartition function ${\overline {P}}(k)$ .

First example:

${\overline {P}}(4)=14$

These 14 possibilities of partition markings exist for the sum 4:

| (4), (**4**), (3+1), (**3**+1), (3+**1**), (**3**+**1**), (2+2), (**2**+2), (2+1+1), (**2**+1+1), (2+**1**+1), (**2**+**1**+1), (1+1+1+1), (**1**+1+1+1) |
|---|

Second example:

${\overline {P}}(5)=24$

These 24 possibilities of partition markings exist for the sum 5:

| (5), (**5**), (4+1), (**4**+1), (4+**1**), (**4**+**1**), (3+2), (**3**+2), (3+**2**), (**3**+**2**), (3+1+1), (**3**+1+1), (3+**1**+1), (**3**+**1**+1), (2+2+1), (**2**+2+1), (2+2+**1**), (**2**+2+**1**), (2+1+1+1), (**2**+1+1+1), (2+**1**+1+1), (**2**+**1**+1+1), (1+1+1+1+1), (**1**+1+1+1+1) |
|---|

### Relations of the partition number sequences to each other

In the Online Encyclopedia of Integer Sequences (OEIS), the sequence of regular partition numbers $P(n)$ is under the code A000041, the sequence of strict partitions is $Q(n)$ under the code A000009 and the sequence of superpartitions ${\overline {P}}(n)$ under the code A015128. All parent partitions from index $n=1$ are even.

The sequence of superpartitions ${\overline {P}}(n)$ can be written with the regular partition sequence P and the strict partition sequence Q can be generated like this:

${\overline {P}}(n)=\sum _{k=0}^{n}P(n-k)Q(k)$

In the following table of sequences of numbers, this formula should be used as an example:

| n | P(n) | Q(n) | ${\overline {P}}(n)$ |
|---|---|---|---|
| 0 | 1 | 1 | 1 = 1*1 |
| 1 | 1 | 1 | 2 = 1 * 1 + 1 * 1 |
| 2 | 2 | 1 | 4 = 2 * 1 + 1 * 1 + 1 * 1 |
| 3 | 3 | 2 | 8 = 3 * 1 + 2 * 1 + 1 * 1 + 1 * 2 |
| 4 | 5 | 2 | 14 = 5 * 1 + 3 * 1 + 2 * 1 + 1 * 2 + 1 * 2 |
| 5 | 7 | 3 | 24 = 7 * 1 + 5 * 1 + 3 * 1 + 2 * 2 + 1 * 2 + 1 * 3 |

Related to this property, the following combination of two series of sums can also be set up via the function ϑ01:

$\theta _{4}(x)={\biggl [}\sum _{k=0}^{\infty }P(k)x^{k}{\biggr ]}^{-1}{\biggl [}\sum _{k=0}^{\infty }Q(k)x^{k}{\biggr ]}^{-1}$
