---
title: "Additive function"
source: https://en.wikipedia.org/wiki/Additive_function
domain: linear-circuit
license: CC-BY-SA-4.0
tags: linear circuit
fetched: 2026-07-03
---

# Additive function

In number theory, an **additive function** is an arithmetic function *f*(*n*) of the positive integer variable *n* such that whenever *a* and *b* are coprime, the function applied to the product *ab* is the sum of the values of the function applied to *a* and *b*: $f(ab)=f(a)+f(b).$ It follows that for any additive function, $f(1)=0$ .

## Completely additive

An additive function *f*(*n*) is said to be **completely additive** if $f(ab)=f(a)+f(b)$ holds *for all* positive integers *a* and *b*, even when they are not coprime. **Totally additive** is also used in this sense by analogy with totally multiplicative functions.

Every completely additive function is additive, but not vice versa.

## Examples

Examples of arithmetic functions which are completely additive are:

- The restriction of the logarithmic function to $\mathbb {N} .$
- The **multiplicity** of a prime factor *p* in *n*, that is the largest exponent *m* for which *pm* divides *n*.
- *a*0(*n*) – the sum of primes dividing *n* counting multiplicity, sometimes called sopfr(*n*), the potency of *n* or the **integer logarithm** of *n* (sequence A001414 in the OEIS). For example:

a

0

(4) = 2 + 2 = 4

a

0

(20) =

a

0

(2

2

· 5) = 2 + 2 + 5 = 9

a

0

(27) = 3 + 3 + 3 = 9

a

0

(144) =

a

0

(2

4

· 3

2

) =

a

0

(2

4

) +

a

0

(3

2

) = 8 + 6 = 14

a

0

(2000) =

a

0

(2

4

· 5

3

) =

a

0

(2

4

) +

a

0

(5

3

) = 8 + 15 = 23

a

0

(2003) = 2003

a

0

(54,032,858,972,279) = 1240658

a

0

(54,032,858,972,302) = 1780417

a

0

(20,802,650,704,327,415) = 1240681

- The function Ω(*n*), defined as the total number of prime factors of *n*, counting multiple factors multiple times, sometimes called the "Big Omega function" (sequence A001222 in the OEIS). For example;

Ω(1) = 0, since 1 has no prime factors

Ω(4) = 2

Ω(16) = Ω(2·2·2·2) = 4

Ω(20) = Ω(2·2·5) = 3

Ω(27) = Ω(3·3·3) = 3

Ω(144) = Ω(2

4

· 3

2

) = Ω(2

4

) + Ω(3

2

) = 4 + 2 = 6

Ω(2000) = Ω(2

4

· 5

3

) = Ω(2

4

) + Ω(5

3

) = 4 + 3 = 7

Ω(2001) = 3

Ω(2002) = 4

Ω(2003) = 1

Ω(54,032,858,972,279) = Ω(11 ⋅ 1993

2

⋅ 1236661) = 4

Ω(54,032,858,972,302) = Ω(2 ⋅ 7

2

⋅ 149 ⋅ 2081 ⋅ 1778171) = 6

Ω(20,802,650,704,327,415) = Ω(5 ⋅ 7 ⋅ 11

2

⋅ 1993

2

⋅ 1236661) = 7.

Examples of arithmetic functions which are additive but not completely additive are:

- ω(*n*), defined as the total number of distinct prime factors of *n* (sequence A001221 in the OEIS). For example:

ω(4) = 1

ω(16) = ω(2

4

) = 1

ω(20) = ω(2

2

· 5) = 2

ω(27) = ω(3

3

) = 1

ω(144) = ω(2

4

· 3

2

) = ω(2

4

) + ω(3

2

) = 1 + 1 = 2

ω(2000) = ω(2

4

· 5

3

) = ω(2

4

) + ω(5

3

) = 1 + 1 = 2

ω(2001) = 3

ω(2002) = 4

ω(2003) = 1

ω(54,032,858,972,279) = 3

ω(54,032,858,972,302) = 5

ω(20,802,650,704,327,415) = 5

- *a*1(*n*) – the sum of the distinct primes dividing *n*, sometimes called sopf(*n*) (sequence A008472 in the OEIS). For example:

a

1

(1) = 0

a

1

(4) = 2

a

1

(20) = 2 + 5 = 7

a

1

(27) = 3

a

1

(144) =

a

1

(2

4

· 3

2

) =

a

1

(2

4

) +

a

1

(3

2

) = 2 + 3 = 5

a

1

(2000) =

a

1

(2

4

· 5

3

) =

a

1

(2

4

) +

a

1

(5

3

) = 2 + 5 = 7

a

1

(2001) = 55

a

1

(2002) = 33

a

1

(2003) = 2003

a

1

(54,032,858,972,279) = 1238665

a

1

(54,032,858,972,302) = 1780410

a

1

(20,802,650,704,327,415) = 1238677

## Multiplicative functions

From any additive function $f(n)$ it is possible to create a related *multiplicative function* $g(n),$ which is a function with the property that whenever a and b are coprime then: $g(ab)=g(a)\times g(b).$ One such example is $g(n)=2^{f(n)}.$ Likewise if $f(n)$ is completely additive, then $g(n)=2^{f(n)}$ is completely multiplicative. More generally, we could consider the function $g(n)=c^{f(n)}$ , where c is a nonzero real constant.

## Summatory functions

Given an additive function f , let its summatory function be defined by ${\textstyle {\mathcal {M}}_{f}(x):=\sum _{n\leq x}f(n)}$ . The average of f is given exactly as ${\mathcal {M}}_{f}(x)=\sum _{p^{\alpha }\leq x}f(p^{\alpha })\left(\left\lfloor {\frac {x}{p^{\alpha }}}\right\rfloor -\left\lfloor {\frac {x}{p^{\alpha +1}}}\right\rfloor \right).$

The summatory functions over f can be expanded as ${\mathcal {M}}_{f}(x)=xE(x)+O({\sqrt {x}}\cdot D(x))$ where ${\begin{aligned}E(x)&=\sum _{p^{\alpha }\leq x}f(p^{\alpha })p^{-\alpha }(1-p^{-1})\\D^{2}(x)&=\sum _{p^{\alpha }\leq x}|f(p^{\alpha })|^{2}p^{-\alpha }.\end{aligned}}$

The average of the function $f^{2}$ is also expressed by these functions as ${\mathcal {M}}_{f^{2}}(x)=xE^{2}(x)+O(xD^{2}(x)).$

There is always an absolute constant $C_{f}>0$ such that for all natural numbers $x\geq 1$ , $\sum _{n\leq x}|f(n)-E(x)|^{2}\leq C_{f}\cdot xD^{2}(x).$

Let $\nu (x;z):={\frac {1}{x}}\#\!\left\{n\leq x:{\frac {f(n)-A(x)}{B(x)}}\leq z\right\}\!.$

Suppose that f is an additive function with $-1\leq f(p^{\alpha })=f(p)\leq 1$ such that as $x\rightarrow \infty$ , $B(x)=\sum _{p\leq x}f^{2}(p)/p\rightarrow \infty .$

Then $\nu (x;z)\sim G(z)$ where $G(z)$ is the Gaussian distribution function $G(z)={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{z}e^{-t^{2}/2}dt.$

Examples of this result related to the prime omega function and the numbers of prime divisors of shifted primes include the following for fixed $z\in \mathbb {R}$ where the relations hold for $x\gg 1$ : $\#\{n\leq x:\omega (n)-\log \log x\leq z(\log \log x)^{1/2}\}\sim xG(z),$ $\#\{p\leq x:\omega (p+1)-\log \log x\leq z(\log \log x)^{1/2}\}\sim \pi (x)G(z).$
