---
title: "Möbius function"
source: https://en.wikipedia.org/wiki/M%C3%B6bius_function
domain: algebraic-combinatorics
license: CC-BY-SA-4.0
tags: algebraic combinatorics, young tableau, symmetric function, association scheme
fetched: 2026-07-02
---

# Möbius function

The **Möbius function $\mu (n)$** is a multiplicative function in number theory introduced by the German mathematician August Ferdinand Möbius (also transliterated *Moebius*) in 1832. It is ubiquitous in elementary and analytic number theory and most often appears as part of its namesake the Möbius inversion formula. Following work of Gian-Carlo Rota in the 1960s, generalizations of the Möbius function were introduced into combinatorics, and are similarly denoted $\mu (x)$ .

## Definition

The Möbius function is defined by

$\mu (n)={\begin{cases}1&{\text{if }}n=1\\(-1)^{k}&{\text{if }}n{\text{ is the product of }}k{\text{ distinct primes}}\\0&{\text{if }}n{\text{ is divisible by a square}}>1.\end{cases}}$

The Möbius function can alternatively be represented as

$\mu (n)=\delta _{\omega (n)\Omega (n)}\lambda (n),$

where $\delta _{ij}$ is the Kronecker delta, $\lambda (n)$ is the Liouville function, and $\omega (n)$ / $\Omega (n)$ are the Prime omega functions. $\omega (n)$ is the number of distinct prime divisors of n , and $\Omega (n)$ is the number of prime factors of n , counted with multiplicity.

Another characterization by Carl Friedrich Gauss is the sum of all primitive roots.

## Values

The values of $\mu (n)$ for the first 60 positive numbers are

n

1

2

3

4

5

6

7

8

9

10

$\mu (n)$

1

−1

−1

0

−1

1

−1

0

0

1

n

11

12

13

14

15

16

17

18

19

20

$\mu (n)$

−1

0

−1

1

1

0

−1

0

−1

0

n

21

22

23

24

25

26

27

28

29

30

$\mu (n)$

1

1

−1

0

0

1

0

0

−1

−1

n

31

32

33

34

35

36

37

38

39

40

$\mu (n)$

−1

0

1

1

1

0

−1

1

1

0

n

41

42

43

44

45

46

47

48

49

50

$\mu (n)$

−1

−1

−1

0

0

1

−1

0

0

0

n

51

52

53

54

55

56

57

58

59

60

$\mu (n)$

1

0

−1

0

1

0

1

1

−1

0

The first 50 values of the function are plotted below:

Larger values can be checked in:

- Wolframalpha
- the b-file of OEIS

## Applications

### Mathematical series

The Dirichlet series that generates the Möbius function is the (multiplicative) inverse of the Riemann zeta function; if s is a complex number with real part larger than 1 we have

$\sum _{n=1}^{\infty }{\frac {\mu (n)}{n^{s}}}={\frac {1}{\zeta (s)}}.$

This may be seen from its Euler product

${\frac {1}{\zeta (s)}}=\prod _{p{\text{ prime}}}{\left(1-{\frac {1}{p^{s}}}\right)}=\left(1-{\frac {1}{2^{s}}}\right)\left(1-{\frac {1}{3^{s}}}\right)\left(1-{\frac {1}{5^{s}}}\right)\cdots$

Also:

- $\sum \limits _{n=1}^{\infty }{\frac {|\mu (n)|}{n^{s}}}={\frac {\zeta (s)}{\zeta (2s)}};$
- $\sum _{n=1}^{\infty }{\frac {\mu (n)}{n}}=0;$
- $\sum \limits _{n=1}^{\infty }{\frac {\mu (n)\ln n}{n}}=-1;$
- $\sum \limits _{n=1}^{\infty }{\frac {\mu (n)\ln ^{2}n}{n}}=-2\gamma ,$ where $\gamma$ is Euler's constant.

The Lambert series for the Möbius function is

$\sum _{n=1}^{\infty }{\frac {\mu (n)q^{n}}{1-q^{n}}}=q,$

which converges for $|q|<1$ . For prime $\alpha \geq 2$ , we also have

$\sum _{n=1}^{\infty }{\frac {\mu (\alpha n)q^{n}}{q^{n}-1}}=\sum _{n\geq 0}q^{\alpha ^{n}},|q|<1.$

### Algebraic number theory

Gauss proved that for a prime number p the sum of its primitive roots is congruent to $\mu (p-1)\mod p$ .

If $\mathbb {F} _{q}$ denotes the finite field of order q (where q is necessarily a prime power), then the number N of monic irreducible polynomials of degree n over $\mathbb {F} _{q}$ is given by

$N(q,n)={\frac {1}{n}}\sum _{d\mid n}\mu (d)q^{\frac {n}{d}}.$

The Möbius function is used in the Möbius inversion formula.

### Physics

The Möbius function also arises in the primon gas or free Riemann gas model of supersymmetry. In this theory, the fundamental particles or "primons" have energies $\log(p)$ . Under second quantization, multiparticle excitations are considered; these are given by $\log(n)$ for any natural number n . This follows from the fact that the factorization of the natural numbers into primes is unique.

In the free Riemann gas, any natural number can occur, if the primons are taken as bosons. If they are taken as fermions, then the Pauli exclusion principle excludes squares. The operator $(-1)^{F}$ that distinguishes fermions and bosons is then none other than the Möbius function $\mu (n)$ .

The free Riemann gas has a number of other interesting connections to number theory, including the fact that the partition function is the Riemann zeta function. This idea underlies Alain Connes's attempted proof of the Riemann hypothesis.

## Properties

The Möbius function is multiplicative (i.e., $\mu (ab)=\mu (a)\mu (b)$ whenever a and b are coprime).

> **Proof**: Given two coprime numbers $m\geq n$ , we induct on $mn$ . If $mn=1$ , then $\mu (mn)=1=\mu (m)\mu (n)$ . Otherwise, $m>n\geq 1$ , so
> 
> ${\begin{aligned}0&=\sum _{d|mn}\mu (d)\\&=\mu (mn)+\sum _{d|mn;d<mn}\mu (d)\\&{\stackrel {\text{induction}}{=}}\mu (mn)-\mu (m)\mu (n)+\sum _{d|m;d'|n}\mu (d)\mu (d')\\&=\mu (mn)-\mu (m)\mu (n)+\sum _{d|m}\mu (d)\sum _{d'|n}\mu (d')\\&=\mu (mn)-\mu (m)\mu (n)+0\end{aligned}}$

The sum of the Möbius function over all positive divisors of n (including n itself and 1) is zero except when $n=1$ :

$\sum _{d\mid n}\mu (d)={\begin{cases}1&{\text{if }}n=1,\\0&{\text{if }}n>1.\end{cases}}$

The equality above leads to the important Möbius inversion formula and is the main reason why $\mu$ is of relevance in the theory of multiplicative and arithmetic functions.

Other applications of $\mu (n)$ in combinatorics are connected with the use of the Pólya enumeration theorem in combinatorial groups and combinatorial enumerations.

There is a formula for calculating the Möbius function without directly knowing the factorization of its argument:

$\mu (n)=\sum _{\stackrel {1\leq k\leq n}{\gcd(k,\,n)=1}}e^{2\pi i{\frac {k}{n}}},$

i.e. $\mu (n)$ is the sum of the primitive n -th roots of unity. (However, the computational complexity of this definition is at least the same as that of the Euler product definition.)

Other identities satisfied by the Möbius function include

$\sum _{k\leq n}\left\lfloor {\frac {n}{k}}\right\rfloor \mu (k)=1$

and

$\sum _{jk\leq n}\sin \left({\frac {\pi jk}{2}}\right)\mu (k)=1$

.

The first of these is a classical result while the second was published in 2020. Similar identities hold for the Mertens function.

### Proof of the formula for the sum of $\mu$ over divisors

The formula

$\sum _{d\mid n}\mu (d)={\begin{cases}1&{\text{if }}n=1,\\0&{\text{if }}n>1\end{cases}}$

can be written using Dirichlet convolution as: $1*\mu =\varepsilon$ where $\varepsilon$ is the identity under the convolution.

One way of proving this formula is by noting that the Dirichlet convolution of two multiplicative functions is again multiplicative. Thus it suffices to prove the formula for powers of primes. Indeed, for any prime p and for any $k>0$

$1*\mu (p^{k})=\sum _{d\mid p^{k}}\mu (d)=\mu (1)+\mu (p)+\sum _{1<m<=k}\mu (p^{m})=1-1+\sum 0=0=\varepsilon (p^{k})$

,

while for $n=1$

$1*\mu (1)=\sum _{d\mid 1}\mu (d)=\mu (1)=1=\varepsilon (1)$

.

#### Other proofs

Another way of proving this formula is by using the identity

$\mu (n)=\sum _{\stackrel {1\leq k\leq n}{\gcd(k,\,n)=1}}e^{2\pi i{\frac {k}{n}}},$

The formula above is then a consequence of the fact that the n th roots of unity sum to 0, since each n th root of unity is a primitive d th root of unity for exactly one divisor d of n .

However it is also possible to prove this identity from first principles. First note that it is trivially true when $n=1$ . Suppose then that $n>1$ . Then there is a bijection between the factors d of n for which $\mu (d)\neq 0$ and the subsets of the set of all prime factors of n . The asserted result follows from the fact that every non-empty finite set has an equal number of odd- and even-cardinality subsets.

This last fact can be shown easily by induction on the cardinality $|S|$ of a non-empty finite set S . First, if $|S|=1$ , there is exactly one odd-cardinality subset of S , namely S itself, and exactly one even-cardinality subset, namely $\emptyset$ . Next, if $|S|>1$ , then divide the subsets of S into two subclasses depending on whether they contain or not some fixed element x in S . There is an obvious bijection between these two subclasses, pairing those subsets that have the same complement relative to the subset $\{x\}$ . Also, one of these two subclasses consists of all the subsets of the set $S\setminus \{x\}$ , and therefore, by the induction hypothesis, has an equal number of odd- and even-cardinality subsets. These subsets in turn correspond bijectively to the even- and odd-cardinality $\{x\}$ -containing subsets of S . The inductive step follows directly from these two bijections.

A related result is that the binomial coefficients exhibit alternating entries of odd and even power which sum symmetrically.

### Average order

The mean value (in the sense of average orders) of the Möbius function is zero. This statement is, in fact, equivalent to the prime number theorem.

### $\mu (n)$ sections

$\mu (n)=0$ if and only if n is divisible by the square of a prime. The first numbers with this property are

4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28, 32, 36, 40, 44, 45, 48, 49, 50, 52, 54, 56, 60, 63, ...

(sequence

A013929

in the

OEIS

)

.

If n is prime, then $\mu (n)=-1$ , but the converse is not true. The first non prime n for which $\mu (n)=-1$ is $30=2\times 3\times 5$ . The first such numbers with three distinct prime factors (sphenic numbers) are

30, 42, 66, 70, 78, 102, 105, 110, 114, 130, 138, 154, 165, 170, 174, 182, 186, 190, 195, 222, ...

(sequence

A007304

in the

OEIS

)

.

and the first such numbers with 5 distinct prime factors are

2310, 2730, 3570, 3990, 4290, 4830, 5610, 6006, 6090, 6270, 6510, 6630, 7410, 7590, 7770, 7854, 8610, 8778, 8970, 9030, 9282, 9570, 9690, ...

(sequence

A046387

in the

OEIS

)

.

## Mertens function

In number theory another arithmetic function closely related to the Möbius function is the Mertens function, defined by

$M(n)=\sum _{k=1}^{n}\mu (k)$

for every natural number n. This function is closely linked with the positions of zeroes of the Riemann zeta function. See the article on the Mertens conjecture for more information about the connection between $M(n)$ and the Riemann hypothesis.

From the formula

$\mu (n)=\sum _{\stackrel {1\leq k\leq n}{\gcd(k,n)=1}}e^{2\pi i{\frac {k}{n}}},$

it follows that the Mertens function is given by

$M(n)=-1+\sum _{a\in {\mathcal {F}}_{n}}e^{2\pi ia},$

where ${\mathcal {F}}_{n}$ is the Farey sequence of order n .

This formula is used in the proof of the Franel–Landau theorem.

## Generalizations

### Incidence algebras

In combinatorics, every locally finite partially ordered set (poset) is assigned an incidence algebra. One distinguished member of this algebra is that poset's "Möbius function". The classical Möbius function treated in this article is essentially equal to the Möbius function of the set of all positive integers partially ordered by divisibility. See the article on incidence algebras for the precise definition and several examples of these general Möbius functions.

Because the Möbius function is multipliciative, so is its (iterated) Dirichlet convolution $\mu _{k}=\mu *\cdots *\mu$ to be the k -fold Dirichlet convolution of the Möbius function with itself. We then have $\mu _{k}\left(p^{a}\right)=(-1)^{a}{\binom {k}{a}}$ where the binomial coefficient is taken to be zero if $a>k$ . The definition may be extended to complex k by reading the binomial as a polynomial in k .

## Implementations

- Mathematica
- Maxima
- geeksforgeeks C++, Python3, Java, C#, PHP, JavaScript
- Rosetta Code
- Sage
