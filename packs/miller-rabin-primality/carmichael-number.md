---
title: "Carmichael number"
source: https://en.wikipedia.org/wiki/Carmichael_number
domain: miller-rabin-primality
license: CC-BY-SA-4.0
tags: miller rabin primality test, probabilistic primality test, fermat little theorem, carmichael number
fetched: 2026-07-02
---

# Carmichael number

In number theory, a **Carmichael number** is a composite number ⁠ n ⁠ which in modular arithmetic satisfies the congruence relation:

$b^{n}\equiv b{\pmod {n}}$

for all integers ⁠ b ⁠. The relation may also be expressed in the form:

$b^{n-1}\equiv 1{\pmod {n}}$

for all integers b that are relatively prime to ⁠ n ⁠. They are infinite in number.

They constitute the comparatively rare instances where the strict converse of Fermat's Little Theorem does not hold. This fact precludes the use of that theorem as an absolute test of primality.

The Carmichael numbers form the subset *K*1 of the Knödel numbers.

The Carmichael numbers were named after the American mathematician Robert Carmichael by Nicolaas Beeger, in 1950. Øystein Ore had referred to them in 1948 as numbers with the "Fermat property", or "*F* numbers" for short.

## Overview

Fermat's little theorem states that if p is a prime number, then for any integer ⁠ b ⁠, the number $b^{p}-b$ is an integer multiple of ⁠ p ⁠. Carmichael numbers are composite numbers which have the same property. Carmichael numbers are also called Fermat pseudoprimes or **absolute Fermat pseudoprimes**. A Carmichael number will pass a Fermat primality test to every base b relatively prime to the number, even though it is not actually prime. This makes tests based on Fermat's Little Theorem less effective than strong probable prime tests such as the Baillie–PSW primality test and the Miller–Rabin primality test.

However, no Carmichael number is either an Euler–Jacobi pseudoprime or a strong pseudoprime to every base relatively prime to it so, in theory, either an Euler or a strong probable prime test could prove that a Carmichael number is, in fact, composite.

Arnault gives a 397-digit Carmichael number N that is a *strong* pseudoprime to all *prime* bases less than 307:

$N=p\cdot (313(p-1)+1)\cdot (353(p-1)+1)$

where

$p=$

2

‍

9674495668

‍

6855105501

‍

5417464290

‍

5332730771

‍

9917998530

‍

4335099507

‍

5531276838

‍

7531717701

‍

9959423859

‍

6428121188

‍

0336647542

‍

1834556249

‍

3168782883

is a 131-digit prime. p is the smallest prime factor of ⁠ N ⁠, so this Carmichael number is also a (not necessarily strong) pseudoprime to all bases less than ⁠ p ⁠.

As numbers become larger, Carmichael numbers become increasingly rare. For example, there are 20138200 Carmichael numbers between 1 and 1021 (approximately one in 50 trillion (5×1013) numbers).

### Korselt's criterion

An alternative and equivalent definition of Carmichael numbers is given by **Korselt's criterion**.

Theorem

(

A. Korselt

1899): A positive composite integer

n

is a Carmichael number if and only if

n

is

square-free

, and for all

prime divisors

p

of

⁠

n

⁠

, it is true that

⁠

$p-1\mid n-1$

⁠

.

It follows from this theorem that all Carmichael numbers are odd, since any even composite number that is square-free (and hence has only one prime factor of two) will have at least one odd prime factor, and thus $p-1\mid n-1$ results in an even dividing an odd, a contradiction. (The oddness of Carmichael numbers also follows from the fact that $-1$ is a Fermat witness for any even composite number.) From the criterion it also follows that Carmichael numbers are cyclic. Additionally, it follows that there are no Carmichael numbers with exactly two prime divisors.

## Discovery

The first seven Carmichael numbers, from 561 to 8911, were all found by the Czech mathematician Václav Šimerka in 1885 (thus preceding not just Carmichael but also Korselt, although Šimerka did not find anything like Korselt's criterion). His work, published in Czech scientific journal *Časopis pro pěstování matematiky a fysiky*, however, remained unnoticed.

Korselt was the first who observed the basic properties of Carmichael numbers, but he did not give any examples.

That 561 is a Carmichael number can be seen with Korselt's criterion. The first seven Carmichael numbers are (sequence A002997 in the OEIS):

$~~561=3\cdot 11\cdot 17\qquad (2\mid ~~560;\quad 10\mid ~~560;\quad 16\mid ~~560)$

$1105=5\cdot 13\cdot 17\qquad (4\mid 1104;\quad 12\mid 1104;\quad 16\mid 1104)$

$1729=7\cdot 13\cdot 19\qquad (6\mid 1728;\quad 12\mid 1728;\quad 18\mid 1728)$

$2465=5\cdot 17\cdot 29\qquad (4\mid 2464;\quad 16\mid 2464;\quad 28\mid 2464)$

$2821=7\cdot 13\cdot 31\qquad (6\mid 2820;\quad 12\mid 2820;\quad 30\mid 2820)$

$6601=7\cdot 23\cdot 41\qquad (6\mid 6600;\quad 22\mid 6600;\quad 40\mid 6600)$

$8911=7\cdot 19\cdot 67\qquad (6\mid 8910;\quad 18\mid 8910;\quad 66\mid 8910).$

In 1910, Carmichael himself also published the smallest such number, 561, and the numbers were later named after him.

Jack Chernick proved a theorem in 1939 which can be used to construct a subset of Carmichael numbers. The number $(6k+1)(12k+1)(18k+1)$ is a Carmichael number if its three factors are all prime. Whether this formula produces an infinite quantity of Carmichael numbers is an open question (though it is implied by Dickson's conjecture).

Paul Erdős heuristically argued there should be infinitely many Carmichael numbers. In 1994 W. R. (Red) Alford, Andrew Granville and Carl Pomerance used a bound on Olson's constant to show that there really do exist infinitely many Carmichael numbers. Specifically, they showed that for sufficiently large ⁠ n ⁠, there are at least $n^{2/7}$ Carmichael numbers between 1 and ⁠ n ⁠.

Thomas Wright proved that if a and m are relatively prime, then there are infinitely many Carmichael numbers in the arithmetic progression ⁠ $a+k\cdot m$ ⁠, where ⁠ $k=1,2,\ldots$ ⁠.

Löh and Niebuhr in 1992 found some very large Carmichael numbers, including one with 1101518 factors and over 16 million digits. This has been improved to 10333229505 prime factors and 295486761787 digits, so the largest known Carmichael number is much greater than the largest known prime.

## Properties

### Factorizations

Carmichael numbers have at least three prime factors. The first Carmichael numbers with $k=3,4,5,\ldots$ prime factors are (sequence A006931 in the OEIS):

| *k* |   |
|---|---|
| 3 | $561=3\cdot 11\cdot 17\,$ |
| 4 | $41041=7\cdot 11\cdot 13\cdot 41\,$ |
| 5 | $825265=5\cdot 7\cdot 17\cdot 19\cdot 73\,$ |
| 6 | $321197185=5\cdot 19\cdot 23\cdot 29\cdot 37\cdot 137\,$ |
| 7 | $5394826801=7\cdot 13\cdot 17\cdot 23\cdot 31\cdot 67\cdot 73\,$ |
| 8 | $232250619601=7\cdot 11\cdot 13\cdot 17\cdot 31\cdot 37\cdot 73\cdot 163\,$ |
| 9 | $9746347772161=7\cdot 11\cdot 13\cdot 17\cdot 19\cdot 31\cdot 37\cdot 41\cdot 641\,$ |

The first Carmichael numbers with 4 prime factors are (sequence A074379 in the OEIS):

| *i* |   |
|---|---|
| 1 | $41041=7\cdot 11\cdot 13\cdot 41\,$ |
| 2 | $62745=3\cdot 5\cdot 47\cdot 89\,$ |
| 3 | $63973=7\cdot 13\cdot 19\cdot 37\,$ |
| 4 | $75361=11\cdot 13\cdot 17\cdot 31\,$ |
| 5 | $101101=7\cdot 11\cdot 13\cdot 101\,$ |
| 6 | $126217=7\cdot 13\cdot 19\cdot 73\,$ |
| 7 | $172081=7\cdot 13\cdot 31\cdot 61\,$ |
| 8 | $188461=7\cdot 13\cdot 19\cdot 109\,$ |
| 9 | $278545=5\cdot 17\cdot 29\cdot 113\,$ |
| 10 | $340561=13\cdot 17\cdot 23\cdot 67\,$ |

The second Carmichael number (1105) can be expressed as the sum of two squares in more ways than any smaller number. The third Carmichael number (1729) is the Hardy-Ramanujan Number: the smallest number that can be expressed as the sum of two cubes (of positive numbers) in two different ways.

### Distribution

Let $C(X)$ denote the number of Carmichael numbers less than or equal to ⁠ X ⁠. The distribution of Carmichael numbers by powers of 10 (sequence A055553 in the OEIS):

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

21

$C(10^{n})$

0

0

1

7

16

43

105

255

646

1547

3605

8241

19279

44706

105212

246683

585355

1401644

3381806

8220777

20138200

In 1953, Knödel proved the upper bound:

$C(X)<X\exp \left({-k_{1}\left(\log X\log \log X\right)^{\frac {1}{2}}}\right)$

for some constant ⁠ $k_{1}$ ⁠.

In 1956, Erdős improved the bound to

$C(X)<X\exp \left({\frac {-k_{2}\log X\log \log \log X}{\log \log X}}\right)$

for some constant ⁠ $k_{2}$ ⁠. He further gave a heuristic argument suggesting that this upper bound should be close to the true growth rate of ⁠ $C(X)$ ⁠.

In the other direction, Alford, Granville and Pomerance proved in 1994 that for sufficiently large *X*,

$C(X)>X^{\frac {2}{7}}.$

In 2005, this bound was further improved by Harman to

$C(X)>X^{0.332}$

who subsequently improved the exponent to ⁠ $0.7039\cdot 0.4736=0.33336704>1/3$ ⁠.

Regarding the asymptotic distribution of Carmichael numbers, there have been several conjectures. In 1956, Erdős conjectured that there were $X^{1-o(1)}$ Carmichael numbers for *X* sufficiently large. In 1981, Pomerance sharpened Erdős' heuristic arguments to conjecture that there are at least

$X\cdot L(X)^{-1+o(1)}$

Carmichael numbers up to ⁠ X ⁠, where ⁠ $L(x)=\exp {\left({\frac {\log x\log \log \log x}{\log \log x}}\right)}$ ⁠.

However, inside current computational ranges (such as the count of Carmichael numbers performed by Goutier(sequence A055553 in the OEIS) up to 1022), these conjectures are not yet borne out by the data; empirically, the exponent is $C(X)\approx X^{0.35}$ for the highest available count (*C*(*X*) = 49679870 for *X* = 1022).

In 2021, Daniel Larsen proved an analogue of Bertrand's postulate for Carmichael numbers first conjectured by Alford, Granville, and Pomerance in 1994. Using techniques developed by Yitang Zhang and James Maynard to establish results concerning small gaps between primes, his work yielded the much stronger statement that, for any $\delta >0$ and sufficiently large x in terms of ⁠ $\delta$ ⁠, there will always be at least

$\exp {\left({\frac {\log {x}}{(\log \log {x})^{2+\delta }}}\right)}$

Carmichael numbers between x and

$x+{\frac {x}{(\log {x})^{\frac {1}{2+\delta }}}}.$

## Generalizations

The notion of Carmichael number generalizes to a Carmichael ideal in any number field ⁠ K ⁠. For any nonzero prime ideal ${\mathfrak {p}}$ in ⁠ ${\mathcal {O}}_{K}$ ⁠, we have $\alpha ^{{\rm {N}}({\mathfrak {p}})}\equiv \alpha {\bmod {\mathfrak {p}}}$ for all $\alpha$ in ⁠ ${\mathcal {O}}_{K}$ ⁠, where ${\rm {N}}({\mathfrak {p}})$ is the norm of the ideal ⁠ ${\mathfrak {p}}$ ⁠. (This generalizes Fermat's little theorem, that $m^{p}\equiv m{\bmod {p}}$ for all integers ⁠ m ⁠ when ⁠ p ⁠ is prime.) Call a nonzero ideal ${\mathfrak {a}}$ in ${\mathcal {O}}_{K}$ Carmichael if it is not a prime ideal and $\alpha ^{{\rm {N}}({\mathfrak {a}})}\equiv \alpha {\bmod {\mathfrak {a}}}$ for all ⁠ $\alpha \in {\mathcal {O}}_{K}$ ⁠, where ${\rm {N}}({\mathfrak {a}})$ is the norm of the ideal ⁠ ${\mathfrak {a}}$ ⁠. When ⁠ K ⁠ is ⁠ $\mathbf {Q}$ ⁠, the ideal ${\mathfrak {a}}$ is principal, and if we let ⁠ a ⁠ be its positive generator then the ideal ${\mathfrak {a}}=(a)$ is Carmichael exactly when ⁠ a ⁠ is a Carmichael number in the usual sense.

When ⁠ K ⁠ is larger than the rationals it is easy to write down Carmichael ideals in ⁠ ${\mathcal {O}}_{K}$ ⁠: for any prime number ⁠ p ⁠ that splits completely in ⁠ K ⁠, the principal ideal $p{\mathcal {O}}_{K}$ is a Carmichael ideal. Since infinitely many prime numbers split completely in any number field, there are infinitely many Carmichael ideals in ⁠ ${\mathcal {O}}_{K}$ ⁠. For example, if ⁠ p ⁠ is any prime number that is 1 mod 4, the ideal ⁠ $(p)$ ⁠ in the Gaussian integers $\mathbb {Z} [i]$ is a Carmichael ideal.

Both prime and Carmichael numbers satisfy the following equality:

$\gcd \left(\sum _{x=1}^{n-1}x^{n-1},n\right)=1.$

## Lucas–Carmichael number

A positive composite integer n is a Lucas–Carmichael number if and only if n is square-free, and for all prime divisors p of ⁠ n ⁠, it is true that ⁠ $p+1\mid n+1$ ⁠. The first Lucas–Carmichael numbers are:

399, 935, 2015, 2915, 4991, 5719, 7055, 8855, 12719, 18095, 20705, 20999, 22847, 29315, 31535, 46079, 51359, 60059, 63503, 67199, 73535, 76751, 80189, 81719, 88559, 90287, ...

(sequence

A006972

in the

OEIS

)

## Quasi–Carmichael number

Quasi–Carmichael numbers are squarefree composite numbers ⁠ n ⁠ with the property that for every prime factor ⁠ p ⁠ of ⁠ n ⁠, ⁠ $p+b$ ⁠ divides ⁠ $n+b$ ⁠ positively with ⁠ b ⁠ being any integer besides 0. If ⁠ $b=-1$ ⁠, these are Carmichael numbers, and if ⁠ $b=1$ ⁠, these are Lucas–Carmichael numbers. The first Quasi–Carmichael numbers are:

35, 77, 143, 165, 187, 209, 221, 231, 247, 273, 299, 323, 357, 391, 399, 437, 493, 527, 561, 589, 598, 713, 715, 899, 935, 943, 989, 1015, 1073, 1105, 1147, 1189, 1247, 1271, 1295, 1333, 1517, 1537, 1547, 1591, 1595, 1705, 1729, ...

(sequence

A257750

in the

OEIS

)

## Knödel number

An *n*-**Knödel number** for a given positive integer *n* is a composite number *m* with the property that each ⁠ $i<m$ ⁠ coprime to *m* satisfies ⁠ $i^{m-n}\equiv 1{\pmod {m}}$ ⁠. The ⁠ $n=1$ ⁠ case are Carmichael numbers.

## Higher-order Carmichael numbers

Carmichael numbers can be generalized using concepts of abstract algebra.

The above definition states that a composite integer *n* is Carmichael precisely when the *n*th-power-raising function *p**n* from the ring **Z***n* of integers modulo *n* to itself is the identity function. The identity is the only **Z***n*-algebra endomorphism on **Z***n* so we can restate the definition as asking that *p**n* be an algebra endomorphism of **Z***n*. As above, *p**n* satisfies the same property whenever *n* is prime.

The *n*th-power-raising function *p**n* is also defined on any **Z***n*-algebra **A**. A theorem states that *n* is prime if and only if all such functions *p**n* are algebra endomorphisms.

In-between these two conditions lies the definition of **Carmichael number of order m** for any positive integer *m* as any composite number *n* such that *p**n* is an endomorphism on every **Z***n*-algebra that can be generated as **Z***n*-module by *m* elements. Carmichael numbers of order 1 are just the ordinary Carmichael numbers.

### An order-2 Carmichael number

According to Howe, 17 · 31 · 41 · 43 · 89 · 97 · 167 · 331 is an order 2 Carmichael number. This product is equal to 443372888629441.

### Properties

Korselt's criterion can be generalized to higher-order Carmichael numbers, as shown by Howe.

A heuristic argument, given in the same paper, appears to suggest that there are infinitely many Carmichael numbers of order *m*, for any *m*. However, not a single Carmichael number of order 3 or above is known.
