---
title: "Arithmetic function"
source: https://en.wikipedia.org/wiki/Arithmetic_function
domain: analytic-number-theory
license: CC-BY-SA-4.0
tags: analytic number theory, prime number theorem, dirichlet series, riemann hypothesis
fetched: 2026-07-02
---

# Arithmetic function

In number theory, an **arithmetic**, **arithmetical**, or **number-theoretic function** is generally any function whose domain is the set of positive integers and whose range is a subset of the complex numbers. Hardy & Wright include in their definition the requirement that an arithmetical function "expresses some arithmetical property of *n*". There is a larger class of number-theoretic functions that do not fit this definition, for example, the prime-counting functions. This article provides links to functions of both classes.

An example of an arithmetic function is the divisor function whose value at a positive integer *n* is equal to the number of divisors of *n*.

Arithmetic functions are often extremely irregular (see table), but some of them have series expansions in terms of Ramanujan's sum.

## Multiplicative and additive functions

An arithmetic function *a* is

- **completely additive** if *a*(*mn*) = *a*(*m*) + *a*(*n*) for all natural numbers *m* and *n*;
- **completely multiplicative** if *a*(1) = 1 and *a*(*mn*) = *a*(*m*)*a*(*n*) for all natural numbers *m* and *n*;

Two whole numbers *m* and *n* are called coprime if their greatest common divisor is 1, that is, if there is no prime number that divides both of them.

Then an arithmetic function *a* is

- **additive** if *a*(*mn*) = *a*(*m*) + *a*(*n*) for all coprime natural numbers *m* and *n*;
- **multiplicative** if *a*(1) = 1 and *a*(*mn*) = *a*(*m*)*a*(*n*) for all coprime natural numbers *m* and *n*.

## Notation

In this article, ${\textstyle \sum _{p}f(p)}$ and ${\textstyle \prod _{p}f(p)}$ mean that the sum or product is over all prime numbers: $\sum _{p}f(p)=f(2)+f(3)+f(5)+\cdots$ and $\prod _{p}f(p)=f(2)f(3)f(5)\cdots .$ Similarly, ${\textstyle \sum _{p^{k}}f(p^{k})}$ and ${\textstyle \prod _{p^{k}}f(p^{k})}$ mean that the sum or product is over all prime powers with strictly positive exponent (so *k* = 0 is not included): $\sum _{p^{k}}f(p^{k})=\sum _{p}\sum _{k>0}f(p^{k})=f(2)+f(3)+f(4)+f(5)+f(7)+f(8)+f(9)+\cdots .$

The notations ${\textstyle \sum _{d\mid n}f(d)}$ and ${\textstyle \prod _{d\mid n}f(d)}$ mean that the sum or product is over all positive divisors of *n*, including 1 and *n*. For example, if *n* = 12, then $\prod _{d\mid 12}f(d)=f(1)f(2)f(3)f(4)f(6)f(12).$

The notations can be combined: ${\textstyle \sum _{p\mid n}f(p)}$ and ${\textstyle \prod _{p\mid n}f(p)}$ mean that the sum or product is over all prime divisors of *n*. For example, if *n* = 18, then $\sum _{p\mid 18}f(p)=f(2)+f(3),$ and similarly ${\textstyle \sum _{p^{k}\mid n}f(p^{k})}$ and ${\textstyle \prod _{p^{k}\mid n}f(p^{k})}$ mean that the sum or product is over all prime powers dividing *n*. For example, if *n* = 24, then $\prod _{p^{k}\mid 24}f(p^{k})=f(2)f(3)f(4)f(8).$

## Ω(*n*), *ω*(*n*), *ν**p*(*n*) – prime power decomposition

The fundamental theorem of arithmetic states that any positive integer *n* can be represented uniquely as a product of powers of primes: $n=p_{1}^{a_{1}}\cdots p_{k}^{a_{k}}$ where *p*1 < *p*2 < ... < *p**k* are primes and the *aj* are positive integers. (1 is given by the empty product.)

It is often convenient to write this as an infinite product over all the primes, where all but a finite number have a zero exponent. Define the *p*-adic valuation **ν*p*(*n*)** to be the exponent of the highest power of the prime *p* that divides *n*. That is, if *p* is one of the *p**i* then *ν**p*(*n*) = *a**i*, otherwise it is zero. Then $n=\prod _{p}p^{\nu _{p}(n)}.$

In terms of the above the prime omega functions *ω* and Ω are defined by

ω

(

n

) =

k

,

Ω(

n

) =

a

1

+

a

2

+ ... +

a

k

.

To avoid repetition, formulas for the functions listed in this article are, whenever possible, given in terms of *n* and the corresponding *p**i*, *a**i*, *ω*, and Ω.

## Multiplicative functions

### *σ**k*(*n*), *τ*(*n*), *d*(*n*) – divisor sums

**σ*k*(*n*)** is the sum of the *k*th powers of the positive divisors of *n*, including 1 and *n*, where *k* is a complex number.

***σ*1(*n*)**, the sum of the (positive) divisors of *n*, is usually denoted by ***σ*(*n*)**.

Since a positive number to the zero power is one, ***σ*0(*n*)** is therefore the number of (positive) divisors of *n*; it is usually denoted by ***d*(*n*)** or ***τ*(*n*)** (for the German *Teiler* = divisors).

$\sigma _{k}(n)=\prod _{i=1}^{\omega (n)}{\frac {p_{i}^{(a_{i}+1)k}-1}{p_{i}^{k}-1}}=\prod _{i=1}^{\omega (n)}\left(1+p_{i}^{k}+p_{i}^{2k}+\cdots +p_{i}^{a_{i}k}\right).$

Setting *k* = 0 in the second product gives $\tau (n)=d(n)=(1+a_{1})(1+a_{2})\cdots (1+a_{\omega (n)}).$

### *φ*(*n*) – Euler totient function

***φ*(*n*)**, the Euler totient function, is the number of positive integers not greater than *n* that are coprime to *n*. $\varphi (n)=n\prod _{p\mid n}\left(1-{\frac {1}{p}}\right)=n\left({\frac {p_{1}-1}{p_{1}}}\right)\left({\frac {p_{2}-1}{p_{2}}}\right)\cdots \left({\frac {p_{\omega (n)}-1}{p_{\omega (n)}}}\right).$

### *J**k*(*n*) – Jordan totient function

***J**k*(*n*)**, the Jordan totient function, is the number of *k*-tuples of positive integers all less than or equal to *n* that form a coprime (*k* + 1)-tuple together with *n*. It is a generalization of Euler's totient, *φ*(*n*) = *J*1(*n*). $J_{k}(n)=n^{k}\prod _{p\mid n}\left(1-{\frac {1}{p^{k}}}\right)=n^{k}\left({\frac {p_{1}^{k}-1}{p_{1}^{k}}}\right)\left({\frac {p_{2}^{k}-1}{p_{2}^{k}}}\right)\cdots \left({\frac {p_{\omega (n)}^{k}-1}{p_{\omega (n)}^{k}}}\right).$

### *μ*(*n*) – Möbius function

***μ*(*n*)**, the Möbius function, is important because of the Möbius inversion formula. See *§ Dirichlet convolution*, below. $\mu (n)={\begin{cases}(-1)^{\omega (n)}=(-1)^{\Omega (n)}&{\text{if }}\;\omega (n)=\Omega (n)\\0&{\text{if }}\;\omega (n)\neq \Omega (n).\end{cases}}$

This implies that *μ*(1) = 1. (Because Ω(1) = *ω*(1) = 0.)

### *τ*(*n*) – Ramanujan tau function

***τ*(*n*)**, the Ramanujan tau function, is defined by its generating function identity: $\sum _{n\geq 1}\tau (n)q^{n}=q\prod _{n\geq 1}(1-q^{n})^{24}.$

Although it is hard to say exactly what "arithmetical property of *n*" it "expresses", (*τ*(*n*) is (2*π*)−12 times the *n*th Fourier coefficient in the *q*-expansion of the modular discriminant function) it is included among the arithmetical functions because it is multiplicative and it occurs in identities involving certain *σ**k*(*n*) and *r**k*(*n*) functions (because these are also coefficients in the expansion of modular forms).

### *c**q*(*n*) – Ramanujan's sum

***c**q*(*n*)**, Ramanujan's sum, is the sum of the *n*th powers of the primitive *q*th roots of unity: $c_{q}(n)=\sum _{\stackrel {1\leq a\leq q}{\gcd(a,q)=1}}e^{2\pi i{\tfrac {a}{q}}n}.$

Even though it is defined as a sum of complex numbers (irrational for most values of *q*), it is an integer. For a fixed value of *n* it is multiplicative in *q*:

If

q

and

r

are coprime

, then

$c_{q}(n)c_{r}(n)=c_{qr}(n).$

### *ψ*(*n*) – Dedekind psi function

The Dedekind psi function, used in the theory of modular functions, is defined by the formula $\psi (n)=n\prod _{p|n}\left(1+{\frac {1}{p}}\right).$

## Completely multiplicative functions

### *λ*(*n*) – Liouville function

***λ*(*n*)**, the Liouville function, is defined by $\lambda (n)=(-1)^{\Omega (n)}.$

### *χ*(*n*) – characters

All **Dirichlet characters *χ*(*n*)** are completely multiplicative. Two characters have special notations:

The **principal character (mod *n*)** is denoted by *χ*0(*a*) (or *χ*1(*a*)). It is defined as $\chi _{0}(a)={\begin{cases}1&{\text{if }}\gcd(a,n)=1,\\0&{\text{if }}\gcd(a,n)\neq 1.\end{cases}}$

The **quadratic character (mod *n*)** is denoted by the Jacobi symbol for odd *n* (it is not defined for even *n*): $\left({\frac {a}{n}}\right)=\left({\frac {a}{p_{1}}}\right)^{a_{1}}\left({\frac {a}{p_{2}}}\right)^{a_{2}}\cdots \left({\frac {a}{p_{\omega (n)}}}\right)^{a_{\omega (n)}}.$

In this formula $({\tfrac {a}{p}})$ is the Legendre symbol, defined for all integers *a* and all odd primes *p* by $\left({\frac {a}{p}}\right)={\begin{cases}\;\;\,0&{\text{if }}a\equiv 0{\pmod {p}},\\+1&{\text{if }}a\not \equiv 0{\pmod {p}}{\text{ and for some integer }}x,\;a\equiv x^{2}{\pmod {p}}\\-1&{\text{if there is no such }}x.\end{cases}}$

Following the normal convention for the empty product, $\left({\frac {a}{1}}\right)=1.$

## Additive functions

### *ω*(*n*) – distinct prime divisors

***ω*(*n*)**, defined above as the number of distinct primes dividing *n*, is additive (see *Prime omega function*).

## Completely additive functions

### Ω(*n*) – prime divisors

**Ω(*n*)**, defined above as the number of prime factors of *n* counted with multiplicities, is completely additive (see Prime omega function).

### *ν**p*(*n*) – *p*-adic valuation of an integer *n*

For a fixed prime *p*, ***ν**p*(*n*)**, defined above as the exponent of the largest power of *p* dividing *n*, is completely additive.

### Logarithmic derivative

$\operatorname {ld} (n)={\frac {D(n)}{n}}=\sum _{\stackrel {p\mid n}{p{\text{ prime}}}}{\frac {v_{p}(n)}{p}}$ , where $D(n)$ is the arithmetic derivative.

## Neither multiplicative nor additive

### *π*(*x*), Π(*x*), *ϑ*(*x*), *ψ*(*x*) – prime-counting functions

These important functions (which are not arithmetic functions) are defined for non-negative real arguments, and are used in the various statements and proofs of the prime number theorem. They are summation functions (see the main section just below) of arithmetic functions which are neither multiplicative nor additive.

*π*(*x*), the prime-counting function, is the number of primes not exceeding *x*. It is the summation function of the characteristic function of the prime numbers. $\pi (x)=\sum _{p\leq x}1$

A related function counts prime powers with weight 1 for primes, 1/2 for their squares, 1/3 for cubes, etc. It is the summation function of the arithmetic function which takes the value 1/*k* on integers which are the *k*th power of some prime number, and the value 0 on other integers. $\Pi (x)=\sum _{p^{k}\leq x}{\frac {1}{k}}.$

*ϑ*(*x*) and *ψ*(*x*), the Chebyshev functions, are defined as sums of the natural logarithms of the primes not exceeding *x*. $\vartheta (x)=\sum _{p\leq x}\log p,$ $\psi (x)=\sum _{p^{k}\leq x}\log p.$

The second Chebyshev function *ψ*(*x*) is the summation function of the von Mangoldt function just below.

### Λ(*n*) – von Mangoldt function

**Λ(*n*)**, the von Mangoldt function, is 0 unless the argument *n* is a prime power *p**k*, in which case it is the natural logarithm of the prime *p*: $\Lambda (n)={\begin{cases}\log p&{\text{if }}n=2,3,4,5,7,8,9,11,13,16,\ldots =p^{k}{\text{ is a prime power}}\\0&{\text{if }}n=1,6,10,12,14,15,18,20,21,\dots \;\;\;\;{\text{ is not a prime power}}.\end{cases}}$

### *p*(*n*) – partition function

***p*(*n*)**, the partition function, is the number of ways of representing *n* as a sum of positive integers, where two representations with the same summands in a different order are not counted as being different: $p(n)=\left|\left\{(a_{1},a_{2},\dots a_{k}):0<a_{1}\leq a_{2}\leq \cdots \leq a_{k}\;\land \;n=a_{1}+a_{2}+\cdots +a_{k}\right\}\right|.$

### *λ*(*n*) – Carmichael function

***λ*(*n*)**, the Carmichael function, is the smallest positive number such that $a^{\lambda (n)}\equiv 1{\pmod {n}}$   for all *a* coprime to *n*. Equivalently, it is the least common multiple of the orders of the elements of the multiplicative group of integers modulo *n*.

For powers of odd primes and for 2 and 4, *λ*(*n*) is equal to the Euler totient function of *n*; for powers of 2 greater than 4 it is equal to one half of the Euler totient function of *n*: $\lambda (n)={\begin{cases}\;\;\phi (n)&{\text{if }}n=2,3,4,5,7,9,11,13,17,19,23,25,27,\dots \\{\tfrac {1}{2}}\phi (n)&{\text{if }}n=8,16,32,64,\dots \end{cases}}$ and for general *n* it is the least common multiple of *λ* of each of the prime power factors of *n*: $\lambda (p_{1}^{a_{1}}p_{2}^{a_{2}}\dots p_{\omega (n)}^{a_{\omega (n)}})=\operatorname {lcm} [\lambda (p_{1}^{a_{1}}),\;\lambda (p_{2}^{a_{2}}),\dots ,\lambda (p_{\omega (n)}^{a_{\omega (n)}})].$

### *h*(*n*) – class number

***h*(*n*)**, the class number function, is the order of the ideal class group of an algebraic extension of the rationals with discriminant *n*. The notation is ambiguous, as there are in general many extensions with the same discriminant. See quadratic field and cyclotomic field for classical examples.

### *r**k*(*n*) – sum of *k* squares

***r**k*(*n*)** is the number of ways *n* can be represented as the sum of *k* squares, where representations that differ only in the order of the summands or in the signs of the square roots are counted as different. $r_{k}(n)=\left|\left\{(a_{1},a_{2},\dots ,a_{k}):n=a_{1}^{2}+a_{2}^{2}+\cdots +a_{k}^{2}\right\}\right|$

### *D*(*n*) – Arithmetic derivative

Using the Heaviside notation for the derivative, the arithmetic derivative *D*(*n*) is a function such that

- $D(n)=1$ if *n* prime, and
- $D(mn)=mD(n)+D(m)n$ (the product rule)

## Summation functions

Given an arithmetic function *a*(*n*), its **summation function** *A*(*x*) is defined by $A(x):=\sum _{n\leq x}a(n).$ *A* can be regarded as a function of a real variable. Given a positive integer *m*, *A* is constant along open intervals *m* < *x* < *m* + 1, and has a jump discontinuity at each integer for which *a*(*m*) ≠ 0.

Since such functions are often represented by series and integrals, to achieve pointwise convergence it is usual to define the value at the discontinuities as the average of the values to the left and right: $A_{0}(m):={\frac {1}{2}}\left(\sum _{n<m}a(n)+\sum _{n\leq m}a(n)\right)=A(m)-{\frac {1}{2}}a(m).$

Individual values of arithmetic functions may fluctuate wildly – as in most of the above examples. Summation functions "smooth out" these fluctuations. In some cases it may be possible to find asymptotic behaviour for the summation function for large *x*.

A classical example of this phenomenon is given by the divisor summatory function, the summation function of *d*(*n*), the number of divisors of *n*: $\liminf _{n\to \infty }d(n)=2$ $\limsup _{n\to \infty }{\frac {\log d(n)\log \log n}{\log n}}=\log 2$ $\lim _{n\to \infty }{\frac {d(1)+d(2)+\cdots +d(n)}{\log(1)+\log(2)+\cdots +\log(n)}}=1.$

An **average order of an arithmetic function** is some simpler or better-understood function which has the same summation function asymptotically, and hence takes the same values "on average". We say that *g* is an *average order* of *f* if $\sum _{n\leq x}f(n)\sim \sum _{n\leq x}g(n)$

as *x* tends to infinity. The example above shows that *d*(*n*) has the average order log(*n*).

## Dirichlet convolution

Given an arithmetic function *a*(*n*), let *F**a*(*s*), for complex *s*, be the function defined by the corresponding Dirichlet series (where it converges): $F_{a}(s):=\sum _{n=1}^{\infty }{\frac {a(n)}{n^{s}}}.$ *F**a*(*s*) is called a generating function of *a*(*n*). The simplest such series, corresponding to the constant function *a*(*n*) = 1 for all *n*, is *ζ*(*s*) the Riemann zeta function.

The generating function of the Möbius function is the inverse of the zeta function: $\zeta (s)\,\sum _{n=1}^{\infty }{\frac {\mu (n)}{n^{s}}}=1,\;\;\Re s>1.$

Consider two arithmetic functions *a* and *b* and their respective generating functions *F**a*(*s*) and *F**b*(*s*). The product *F**a*(*s*)*F**b*(*s*) can be computed as follows: $F_{a}(s)F_{b}(s)=\left(\sum _{m=1}^{\infty }{\frac {a(m)}{m^{s}}}\right)\left(\sum _{n=1}^{\infty }{\frac {b(n)}{n^{s}}}\right).$

It is a straightforward exercise to show that if *c*(*n*) is defined by $c(n):=\sum _{ij=n}a(i)b(j)=\sum _{i\mid n}a(i)b\left({\frac {n}{i}}\right),$ then $F_{c}(s)=F_{a}(s)F_{b}(s).$

This function *c* is called the Dirichlet convolution of *a* and *b*, and is denoted by $a*b$ .

A particularly important case is convolution with the constant function *a*(*n*) = 1 for all *n*, corresponding to multiplying the generating function by the zeta function: $g(n)=\sum _{d\mid n}f(d).$

Multiplying by the inverse of the zeta function gives the Möbius inversion formula: $f(n)=\sum _{d\mid n}\mu \left({\frac {n}{d}}\right)g(d).$

If *f* is multiplicative, then so is *g*. If *f* is completely multiplicative, then *g* is multiplicative, but may or may not be completely multiplicative.

## Relations among the functions

There are a great many formulas connecting arithmetical functions with each other and with the functions of analysis, especially powers, roots, and the exponential and log functions. The page divisor sum identities contains many more generalized and related examples of identities involving arithmetic functions.

Here are a few examples:

### Dirichlet convolutions

$\sum _{\delta \mid n}\mu (\delta )=\sum _{\delta \mid n}\lambda \left({\frac {n}{\delta }}\right)|\mu (\delta )|={\begin{cases}1&{\text{if }}n=1\\0&{\text{if }}n\neq 1\end{cases}}$

where

λ

is the Liouville function.

$\sum _{\delta \mid n}\varphi (\delta )=n.$

$\varphi (n)=\sum _{\delta \mid n}\mu \left({\frac {n}{\delta }}\right)\delta =n\sum _{\delta \mid n}{\frac {\mu (\delta )}{\delta }}.$

Möbius inversion

$\sum _{\delta \mid n}J_{k}(\delta )=n^{k}.$

$J_{k}(n)=\sum _{\delta \mid n}\mu \left({\frac {n}{\delta }}\right)\delta ^{k}=n^{k}\sum _{\delta \mid n}{\frac {\mu (\delta )}{\delta ^{k}}}.$

Möbius inversion

$\sum _{\delta \mid n}\delta ^{s}J_{r}(\delta )J_{s}\left({\frac {n}{\delta }}\right)=J_{r+s}(n)$

$\sum _{\delta \mid n}\varphi (\delta )d\left({\frac {n}{\delta }}\right)=\sigma (n).$

$\sum _{\delta \mid n}|\mu (\delta )|=2^{\omega (n)}.$

$|\mu (n)|=\sum _{\delta \mid n}\mu \left({\frac {n}{\delta }}\right)2^{\omega (\delta )}.$

Möbius inversion

$\sum _{\delta \mid n}2^{\omega (\delta )}=d(n^{2}).$

$2^{\omega (n)}=\sum _{\delta \mid n}\mu \left({\frac {n}{\delta }}\right)d(\delta ^{2}).$

Möbius inversion

$\sum _{\delta \mid n}d(\delta ^{2})=d^{2}(n).$

$d(n^{2})=\sum _{\delta \mid n}\mu \left({\frac {n}{\delta }}\right)d^{2}(\delta ).$

Möbius inversion

$\sum _{\delta \mid n}d\left({\frac {n}{\delta }}\right)2^{\omega (\delta )}=d^{2}(n).$

$\sum _{\delta \mid n}\lambda (\delta )={\begin{cases}&1{\text{ if }}n{\text{ is a square }}\\&0{\text{ if }}n{\text{ is not square.}}\end{cases}}$

where λ is the

Liouville function

.

$\sum _{\delta \mid n}\Lambda (\delta )=\log n.$

$\Lambda (n)=\sum _{\delta \mid n}\mu \left({\frac {n}{\delta }}\right)\log(\delta ).$

Möbius inversion

### Sums of squares

For all $k\geq 4,\;\;\;r_{k}(n)>0.$     (Lagrange's four-square theorem).

$r_{2}(n)=4\sum _{d\mid n}\left({\frac {-4}{d}}\right),$

where the Kronecker symbol has the values

$\left({\frac {-4}{n}}\right)={\begin{cases}+1&{\text{if }}n\equiv 1{\pmod {4}}\\-1&{\text{if }}n\equiv 3{\pmod {4}}\\\;\;\;0&{\text{if }}n{\text{ is even}}.\\\end{cases}}$

There is a formula for *r*3 in the section on class numbers below. $r_{4}(n)=8\sum _{\stackrel {d\mid n}{4\,\nmid \,d}}d=8(2+(-1)^{n})\sum _{\stackrel {d\mid n}{2\,\nmid \,d}}d={\begin{cases}8\sigma (n)&{\text{if }}n{\text{ is odd }}\\24\sigma \left({\frac {n}{2^{\nu }}}\right)&{\text{if }}n{\text{ is even }}\end{cases}},$ where *ν* = *ν*2(*n*).     $r_{6}(n)=16\sum _{d\mid n}\chi \left({\frac {n}{d}}\right)d^{2}-4\sum _{d\mid n}\chi (d)d^{2},$ where $\chi (n)=\left({\frac {-4}{n}}\right).$

Define the function *σ**k**(*n*) as $\sigma _{k}^{*}(n)=(-1)^{n}\sum _{d\mid n}(-1)^{d}d^{k}={\begin{cases}\sum _{d\mid n}d^{k}=\sigma _{k}(n)&{\text{if }}n{\text{ is odd }}\\\sum _{\stackrel {d\mid n}{2\,\mid \,d}}d^{k}-\sum _{\stackrel {d\mid n}{2\,\nmid \,d}}d^{k}&{\text{if }}n{\text{ is even}}.\end{cases}}$

That is, if *n* is odd, *σ**k**(*n*) is the sum of the *k*th powers of the divisors of *n*, that is, *σ**k*(*n*), and if *n* is even it is the sum of the *k*th powers of the even divisors of *n* minus the sum of the *k*th powers of the odd divisors of *n*.

$r_{8}(n)=16\sigma _{3}^{*}(n).$

Adopt the convention that Ramanujan's *τ*(*x*) = 0 if *x* is **not an integer.**

$r_{24}(n)={\frac {16}{691}}\sigma _{11}^{*}(n)+{\frac {128}{691}}\left\{(-1)^{n-1}259\tau (n)-512\tau \left({\frac {n}{2}}\right)\right\}$

### Divisor sum convolutions

Here "convolution" does not mean "Dirichlet convolution" but instead refers to the formula for the coefficients of the product of two power series:

$\left(\sum _{n=0}^{\infty }a_{n}x^{n}\right)\left(\sum _{n=0}^{\infty }b_{n}x^{n}\right)=\sum _{i=0}^{\infty }\sum _{j=0}^{\infty }a_{i}b_{j}x^{i+j}=\sum _{n=0}^{\infty }\left(\sum _{i=0}^{n}a_{i}b_{n-i}\right)x^{n}=\sum _{n=0}^{\infty }c_{n}x^{n}.$

The sequence $c_{n}=\sum _{i=0}^{n}a_{i}b_{n-i}$ is called the convolution or the Cauchy product of the sequences *a**n* and *b**n*. These formulas may be proved analytically (see Eisenstein series) or by elementary methods.

$\sigma _{3}(n)={\frac {1}{5}}\left\{6n\sigma _{1}(n)-\sigma _{1}(n)+12\sum _{0<k<n}\sigma _{1}(k)\sigma _{1}(n-k)\right\}.$

$\sigma _{5}(n)={\frac {1}{21}}\left\{10(3n-1)\sigma _{3}(n)+\sigma _{1}(n)+240\sum _{0<k<n}\sigma _{1}(k)\sigma _{3}(n-k)\right\}.$

${\begin{aligned}\sigma _{7}(n)&={\frac {1}{20}}\left\{21(2n-1)\sigma _{5}(n)-\sigma _{1}(n)+504\sum _{0<k<n}\sigma _{1}(k)\sigma _{5}(n-k)\right\}\\&=\sigma _{3}(n)+120\sum _{0<k<n}\sigma _{3}(k)\sigma _{3}(n-k).\end{aligned}}$

${\begin{aligned}\sigma _{9}(n)&={\frac {1}{11}}\left\{10(3n-2)\sigma _{7}(n)+\sigma _{1}(n)+480\sum _{0<k<n}\sigma _{1}(k)\sigma _{7}(n-k)\right\}\\&={\frac {1}{11}}\left\{21\sigma _{5}(n)-10\sigma _{3}(n)+5040\sum _{0<k<n}\sigma _{3}(k)\sigma _{5}(n-k)\right\}.\end{aligned}}$

$\tau (n)={\frac {65}{756}}\sigma _{11}(n)+{\frac {691}{756}}\sigma _{5}(n)-{\frac {691}{3}}\sum _{0<k<n}\sigma _{5}(k)\sigma _{5}(n-k),$

where

τ

(

n

) is Ramanujan's function.

Since *σ**k*(*n*) (for natural number *k*) and *τ*(*n*) are integers, the above formulas can be used to prove congruences for the functions. See Ramanujan tau function for some examples.

Extend the domain of the partition function by setting *p*(0) = 1.

$p(n)={\frac {1}{n}}\sum _{1\leq k\leq n}\sigma (k)p(n-k).$

This recurrence can be used to compute

p

(

n

).

Peter Gustav Lejeune Dirichlet discovered formulas that relate the class number *h* of quadratic number fields to the Jacobi symbol.

An integer *D* is called a **fundamental discriminant** if it is the discriminant of a quadratic number field. This is equivalent to *D* ≠ 1 and either a) *D* is squarefree and *D* ≡ 1 (mod 4) or b) *D* ≡ 0 (mod 4), *D*/4 is squarefree, and *D*/4 ≡ 2 or 3 (mod 4).

Extend the Jacobi symbol to accept even numbers in the "denominator" by defining the Kronecker symbol: $\left({\frac {a}{2}}\right)={\begin{cases}\;\;\,0&{\text{ if }}a{\text{ is even}}\\(-1)^{\frac {a^{2}-1}{8}}&{\text{ if }}a{\text{ is odd. }}\end{cases}}$

Then if *D* < −4 is a fundamental discriminant ${\begin{aligned}h(D)&={\frac {1}{D}}\sum _{r=1}^{|D|}r\left({\frac {D}{r}}\right)\\&={\frac {1}{2-\left({\tfrac {D}{2}}\right)}}\sum _{r=1}^{|D|/2}\left({\frac {D}{r}}\right).\end{aligned}}$

There is also a formula relating *r*3 and *h*. Again, let *D* be a fundamental discriminant, *D* < −4. Then $r_{3}(|D|)=12\left(1-\left({\frac {D}{2}}\right)\right)h(D).$

Let $H_{n}=1+{\frac {1}{2}}+{\frac {1}{3}}+\cdots +{\frac {1}{n}}$   be the *n*th harmonic number. Then

$\sigma (n)\leq H_{n}+e^{H_{n}}\log H_{n}$

is true for every natural number

n

if and only if the

Riemann hypothesis

is true.

The Riemann hypothesis is also equivalent to the statement that, for all *n* > 5040, $\sigma (n)<e^{\gamma }n\log \log n$ (where γ is the Euler–Mascheroni constant). This is Robin's theorem.

$\sum _{p}\nu _{p}(n)=\Omega (n).$

$\psi (x)=\sum _{n\leq x}\Lambda (n).$

$\Pi (x)=\sum _{n\leq x}{\frac {\Lambda (n)}{\log n}}.$

$e^{\theta (x)}=\prod _{p\leq x}p.$

$e^{\psi (x)}=\operatorname {lcm} [1,2,\dots ,\lfloor x\rfloor ].$

### Menon's identity

In 1965 P Kesava Menon proved $\sum _{\stackrel {1\leq k\leq n}{\gcd(k,n)=1}}\gcd(k-1,n)=\varphi (n)d(n).$

This has been generalized by a number of mathematicians. For example,

- B. Sury $\sum _{\stackrel {1\leq k_{1},k_{2},\dots ,k_{s}\leq n}{\gcd(k_{1},n)=1}}\gcd(k_{1}-1,k_{2},\dots ,k_{s},n)=\varphi (n)\sigma _{s-1}(n).$
- N. Rao $\sum _{\stackrel {1\leq k_{1},k_{2},\dots ,k_{s}\leq n}{\gcd(k_{1},k_{2},\dots ,k_{s},n)=1}}\gcd(k_{1}-a_{1},k_{2}-a_{2},\dots ,k_{s}-a_{s},n)^{s}=J_{s}(n)d(n),$ where *a*1, *a*2, ..., *a**s* are integers, gcd(*a*1, *a*2, ..., *a**s*, *n*) = 1.
- László Fejes Tóth $\sum _{\stackrel {1\leq k\leq m}{\gcd(k,m)=1}}\gcd(k^{2}-1,m_{1})\gcd(k^{2}-1,m_{2})=\varphi (n)\sum _{\stackrel {d_{1}\mid m_{1}}{d_{2}\mid m_{2}}}\varphi (\gcd(d_{1},d_{2}))2^{\omega (\operatorname {lcm} (d_{1},d_{2}))},$ where *m*1 and *m*2 are odd, *m* = lcm(*m*1, *m*2).

In fact, if *f* is any arithmetical function $\sum _{\stackrel {1\leq k\leq n}{\gcd(k,n)=1}}f(\gcd(k-1,n))=\varphi (n)\sum _{d\mid n}{\frac {(\mu *f)(d)}{\varphi (d)}},$ where * stands for Dirichlet convolution.

### Miscellaneous

Let *m* and *n* be distinct, odd, and positive. Then the Jacobi symbol satisfies the law of quadratic reciprocity: $\left({\frac {m}{n}}\right)\left({\frac {n}{m}}\right)=(-1)^{(m-1)(n-1)/4}.$

Let *D*(*n*) be the arithmetic derivative. Then the logarithmic derivative ${\frac {D(n)}{n}}=\sum _{\stackrel {p\mid n}{p{\text{ prime}}}}{\frac {v_{p}(n)}{p}}.$ See *Arithmetic derivative* for details.

Let *λ*(*n*) be Liouville's function. Then

$|\lambda (n)|\mu (n)=\lambda (n)|\mu (n)|=\mu (n),$

and

$\lambda (n)\mu (n)=|\mu (n)|=\mu ^{2}(n).$

Let *λ*(*n*) be Carmichael's function. Then

$\lambda (n)\mid \phi (n).$

Further,

$\lambda (n)=\phi (n){\text{ if and only if }}n={\begin{cases}1,2,4;\\3,5,7,9,11,\ldots {\text{ (that is, }}p^{k}{\text{, where }}p{\text{ is an odd prime)}};\\6,10,14,18,\ldots {\text{ (that is, }}2p^{k}{\text{, where }}p{\text{ is an odd prime)}}.\end{cases}}$

See Multiplicative group of integers modulo n and Primitive root modulo n.

$2^{\omega (n)}\leq d(n)\leq 2^{\Omega (n)}.$

${\frac {6}{\pi ^{2}}}<{\frac {\phi (n)\sigma (n)}{n^{2}}}<1.$

${\begin{aligned}c_{q}(n)&={\frac {\mu \left({\frac {q}{\gcd(q,n)}}\right)}{\phi \left({\frac {q}{\gcd(q,n)}}\right)}}\phi (q)\\&=\sum _{\delta \mid \gcd(q,n)}\mu \left({\frac {q}{\delta }}\right)\delta .\end{aligned}}$

Note that

$\phi (q)=\sum _{\delta \mid q}\mu \left({\frac {q}{\delta }}\right)\delta .$

$c_{q}(1)=\mu (q).$

$c_{q}(q)=\phi (q).$

$\sum _{\delta \mid n}d^{3}(\delta )=\left(\sum _{\delta \mid n}d(\delta )\right)^{2}.$

Compare this with

1

3

+ 2

3

+ 3

3

+ ... +

n

3

= (1 + 2 + 3 + ... +

n

)

2

$d(uv)=\sum _{\delta \mid \gcd(u,v)}\mu (\delta )d\left({\frac {u}{\delta }}\right)d\left({\frac {v}{\delta }}\right).$

$\sigma _{k}(u)\sigma _{k}(v)=\sum _{\delta \mid \gcd(u,v)}\delta ^{k}\sigma _{k}\left({\frac {uv}{\delta ^{2}}}\right).$

$\tau (u)\tau (v)=\sum _{\delta \mid \gcd(u,v)}\delta ^{11}\tau \left({\frac {uv}{\delta ^{2}}}\right),$

where

τ

(

n

) is Ramanujan's function.

## First 100 values of some arithmetic functions

n

factorization

φ

(

n

)

ω

(

n

)

Ω(

n

)

λ

(

n

)

μ

(

n

)

Λ(

n

)

π

(

n

)

σ

0

(

n

)

σ

1

(

n

)

σ

2

(

n

)

r

2

(

n

)

r

3

(

n

)

r

4

(

n

)

1

1

1

0

0

1

1

0

0

1

1

1

4

6

8

2

2

1

1

1

−1

−1

0.69

1

2

3

5

4

12

24

3

3

2

1

1

−1

−1

1.10

2

2

4

10

0

8

32

4

2

2

2

1

2

1

0

0.69

2

3

7

21

4

6

24

5

5

4

1

1

−1

−1

1.61

3

2

6

26

8

24

48

6

2 · 3

2

2

2

1

1

0

3

4

12

50

0

24

96

7

7

6

1

1

−1

−1

1.95

4

2

8

50

0

0

64

8

2

3

4

1

3

−1

0

0.69

4

4

15

85

4

12

24

9

3

2

6

1

2

1

0

1.10

4

3

13

91

4

30

104

10

2 · 5

4

2

2

1

1

0

4

4

18

130

8

24

144

11

11

10

1

1

−1

−1

2.40

5

2

12

122

0

24

96

12

2

2

· 3

4

2

3

−1

0

0

5

6

28

210

0

8

96

13

13

12

1

1

−1

−1

2.56

6

2

14

170

8

24

112

14

2 · 7

6

2

2

1

1

0

6

4

24

250

0

48

192

15

3 · 5

8

2

2

1

1

0

6

4

24

260

0

0

192

16

2

4

8

1

4

1

0

0.69

6

5

31

341

4

6

24

17

17

16

1

1

−1

−1

2.83

7

2

18

290

8

48

144

18

2 · 3

2

6

2

3

−1

0

0

7

6

39

455

4

36

312

19

19

18

1

1

−1

−1

2.94

8

2

20

362

0

24

160

20

2

2

· 5

8

2

3

−1

0

0

8

6

42

546

8

24

144

21

3 · 7

12

2

2

1

1

0

8

4

32

500

0

48

256

22

2 · 11

10

2

2

1

1

0

8

4

36

610

0

24

288

23

23

22

1

1

−1

−1

3.14

9

2

24

530

0

0

192

24

2

3

· 3

8

2

4

1

0

0

9

8

60

850

0

24

96

25

5

2

20

1

2

1

0

1.61

9

3

31

651

12

30

248

26

2 · 13

12

2

2

1

1

0

9

4

42

850

8

72

336

27

3

3

18

1

3

−1

0

1.10

9

4

40

820

0

32

320

28

2

2

· 7

12

2

3

−1

0

0

9

6

56

1050

0

0

192

29

29

28

1

1

−1

−1

3.37

10

2

30

842

8

72

240

30

2 · 3 · 5

8

3

3

−1

−1

0

10

8

72

1300

0

48

576

31

31

30

1

1

−1

−1

3.43

11

2

32

962

0

0

256

32

2

5

16

1

5

−1

0

0.69

11

6

63

1365

4

12

24

33

3 · 11

20

2

2

1

1

0

11

4

48

1220

0

48

384

34

2 · 17

16

2

2

1

1

0

11

4

54

1450

8

48

432

35

5 · 7

24

2

2

1

1

0

11

4

48

1300

0

48

384

36

2

2

· 3

2

12

2

4

1

0

0

11

9

91

1911

4

30

312

37

37

36

1

1

−1

−1

3.61

12

2

38

1370

8

24

304

38

2 · 19

18

2

2

1

1

0

12

4

60

1810

0

72

480

39

3 · 13

24

2

2

1

1

0

12

4

56

1700

0

0

448

40

2

3

· 5

16

2

4

1

0

0

12

8

90

2210

8

24

144

41

41

40

1

1

−1

−1

3.71

13

2

42

1682

8

96

336

42

2 · 3 · 7

12

3

3

−1

−1

0

13

8

96

2500

0

48

768

43

43

42

1

1

−1

−1

3.76

14

2

44

1850

0

24

352

44

2

2

· 11

20

2

3

−1

0

0

14

6

84

2562

0

24

288

45

3

2

· 5

24

2

3

−1

0

0

14

6

78

2366

8

72

624

46

2 · 23

22

2

2

1

1

0

14

4

72

2650

0

48

576

47

47

46

1

1

−1

−1

3.85

15

2

48

2210

0

0

384

48

2

4

· 3

16

2

5

−1

0

0

15

10

124

3410

0

8

96

49

7

2

42

1

2

1

0

1.95

15

3

57

2451

4

54

456

50

2 · 5

2

20

2

3

−1

0

0

15

6

93

3255

12

84

744

51

3 · 17

32

2

2

1

1

0

15

4

72

2900

0

48

576

52

2

2

· 13

24

2

3

−1

0

0

15

6

98

3570

8

24

336

53

53

52

1

1

−1

−1

3.97

16

2

54

2810

8

72

432

54

2 · 3

3

18

2

4

1

0

0

16

8

120

4100

0

96

960

55

5 · 11

40

2

2

1

1

0

16

4

72

3172

0

0

576

56

2

3

· 7

24

2

4

1

0

0

16

8

120

4250

0

48

192

57

3 · 19

36

2

2

1

1

0

16

4

80

3620

0

48

640

58

2 · 29

28

2

2

1

1

0

16

4

90

4210

8

24

720

59

59

58

1

1

−1

−1

4.08

17

2

60

3482

0

72

480

60

2

2

· 3 · 5

16

3

4

1

0

0

17

12

168

5460

0

0

576

61

61

60

1

1

−1

−1

4.11

18

2

62

3722

8

72

496

62

2 · 31

30

2

2

1

1

0

18

4

96

4810

0

96

768

63

3

2

· 7

36

2

3

−1

0

0

18

6

104

4550

0

0

832

64

2

6

32

1

6

1

0

0.69

18

7

127

5461

4

6

24

65

5 · 13

48

2

2

1

1

0

18

4

84

4420

16

96

672

66

2 · 3 · 11

20

3

3

−1

−1

0

18

8

144

6100

0

96

1152

67

67

66

1

1

−1

−1

4.20

19

2

68

4490

0

24

544

68

2

2

· 17

32

2

3

−1

0

0

19

6

126

6090

8

48

432

69

3 · 23

44

2

2

1

1

0

19

4

96

5300

0

96

768

70

2 · 5 · 7

24

3

3

−1

−1

0

19

8

144

6500

0

48

1152

71

71

70

1

1

−1

−1

4.26

20

2

72

5042

0

0

576

72

2

3

· 3

2

24

2

5

−1

0

0

20

12

195

7735

4

36

312

73

73

72

1

1

−1

−1

4.29

21

2

74

5330

8

48

592

74

2 · 37

36

2

2

1

1

0

21

4

114

6850

8

120

912

75

3 · 5

2

40

2

3

−1

0

0

21

6

124

6510

0

56

992

76

2

2

· 19

36

2

3

−1

0

0

21

6

140

7602

0

24

480

77

7 · 11

60

2

2

1

1

0

21

4

96

6100

0

96

768

78

2 · 3 · 13

24

3

3

−1

−1

0

21

8

168

8500

0

48

1344

79

79

78

1

1

−1

−1

4.37

22

2

80

6242

0

0

640

80

2

4

· 5

32

2

5

−1

0

0

22

10

186

8866

8

24

144

81

3

4

54

1

4

1

0

1.10

22

5

121

7381

4

102

968

82

2 · 41

40

2

2

1

1

0

22

4

126

8410

8

48

1008

83

83

82

1

1

−1

−1

4.42

23

2

84

6890

0

72

672

84

2

2

· 3 · 7

24

3

4

1

0

0

23

12

224

10500

0

48

768

85

5 · 17

64

2

2

1

1

0

23

4

108

7540

16

48

864

86

2 · 43

42

2

2

1

1

0

23

4

132

9250

0

120

1056

87

3 · 29

56

2

2

1

1

0

23

4

120

8420

0

0

960

88

2

3

· 11

40

2

4

1

0

0

23

8

180

10370

0

24

288

89

89

88

1

1

−1

−1

4.49

24

2

90

7922

8

144

720

90

2 · 3

2

· 5

24

3

4

1

0

0

24

12

234

11830

8

120

1872

91

7 · 13

72

2

2

1

1

0

24

4

112

8500

0

48

896

92

2

2

· 23

44

2

3

−1

0

0

24

6

168

11130

0

0

576

93

3 · 31

60

2

2

1

1

0

24

4

128

9620

0

48

1024

94

2 · 47

46

2

2

1

1

0

24

4

144

11050

0

96

1152

95

5 · 19

72

2

2

1

1

0

24

4

120

9412

0

0

960

96

2

5

· 3

32

2

6

1

0

0

24

12

252

13650

0

24

96

97

97

96

1

1

−1

−1

4.57

25

2

98

9410

8

48

784

98

2 · 7

2

42

2

3

−1

0

0

25

6

171

12255

4

108

1368

99

3

2

· 11

60

2

3

−1

0

0

25

6

156

11102

0

72

1248

100

2

2

· 5

2

40

2

4

1

0

0

25

9

217

13671

12

30

744

n

factorization

φ

(

n

)

ω

(

n

)

Ω(

n

)

𝜆(

n

)

𝜇(

n

)

Λ(

n

)

π

(

n

)

σ

0

(

n

)

σ

1

(

n

)

σ

2

(

n

)

r

2

(

n

)

r

3

(

n

)

r

4

(

n

)
