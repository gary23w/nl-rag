---
title: "Dirichlet's theorem on arithmetic progressions"
source: https://en.wikipedia.org/wiki/Dirichlet's_theorem_on_arithmetic_progressions
domain: analytic-number-theory
license: CC-BY-SA-4.0
tags: analytic number theory, prime number theorem, dirichlet series, riemann hypothesis
fetched: 2026-07-02
---

# Dirichlet's theorem on arithmetic progressions

In number theory, **Dirichlet's theorem**, also called the **Dirichlet prime number theorem**, states that for any two positive coprime integers *a* and *d*, there are infinitely many primes of the form *a* + *nd*, where *n* is also a positive integer. In other words, there are infinitely many primes that are congruent to *a* modulo *d*. The numbers of the form *a* + *nd* form an arithmetic progression

$a,\ a+d,\ a+2d,\ a+3d,\ \dots ,\$

and Dirichlet's theorem states that this sequence contains infinitely many prime numbers. The theorem extends Euclid's theorem that there are infinitely many prime numbers (of the form 1 + 2*n*). Stronger forms of Dirichlet's theorem state that for any such arithmetic progression, the sum of the reciprocals of the prime numbers in the progression diverges and that different such arithmetic progressions with the same modulus have approximately the same proportions of primes. Equivalently, the primes are evenly distributed (asymptotically) among the congruence classes modulo *d* containing *a* coprime to *d*.

The theorem is named after the German mathematician Peter Gustav Lejeune Dirichlet, who proved it in 1837.

## Examples

The primes of the form 4*n* + 3 are (sequence A002145 in the OEIS)

3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103, 107, 127, 131, 139, 151, 163, 167, 179, 191, 199, 211, 223, 227, 239, 251, 263, 271, 283, ...

They correspond to the following values of *n*: (sequence A095278 in the OEIS)

0, 1, 2, 4, 5, 7, 10, 11, 14, 16, 17, 19, 20, 25, 26, 31, 32, 34, 37, 40, 41, 44, 47, 49, 52, 55, 56, 59, 62, 65, 67, 70, 76, 77, 82, 86, 89, 91, 94, 95, ...

The strong form of Dirichlet's theorem implies that

${\frac {1}{3}}+{\frac {1}{7}}+{\frac {1}{11}}+{\frac {1}{19}}+{\frac {1}{23}}+{\frac {1}{31}}+{\frac {1}{43}}+{\frac {1}{47}}+{\frac {1}{59}}+{\frac {1}{67}}+\cdots$

is a divergent series.

Sequences *dn* + *a* with odd *d* are often ignored because half the numbers are even and the other half is the same numbers as a sequence with 2*d*, if we start with *n* = 0. For example, 6*n* + 1 produces the same primes as 3*n* + 1, while 6*n* + 5 produces the same as 3*n* + 2 except for the only even prime 2. The following table lists several arithmetic progressions with infinitely many primes and the first few ones in each of them.

| Arithmetic progression | First 10 of infinitely many primes | OEIS sequence |
|---|---|---|
| 2*n* + 1 | 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, … | A065091 |
| 4*n* + 1 | 5, 13, 17, 29, 37, 41, 53, 61, 73, 89, … | A002144 |
| 4*n* + 3 | 3, 7, 11, 19, 23, 31, 43, 47, 59, 67, … | A002145 |
| 6*n* + 1 | 7, 13, 19, 31, 37, 43, 61, 67, 73, 79, … | A002476 |
| 6*n* + 5 | 5, 11, 17, 23, 29, 41, 47, 53, 59, 71, … | A007528 |
| 8*n* + 1 | 17, 41, 73, 89, 97, 113, 137, 193, 233, 241, … | A007519 |
| 8*n* + 3 | 3, 11, 19, 43, 59, 67, 83, 107, 131, 139, … | A007520 |
| 8*n* + 5 | 5, 13, 29, 37, 53, 61, 101, 109, 149, 157, … | A007521 |
| 8*n* + 7 | 7, 23, 31, 47, 71, 79, 103, 127, 151, 167, … | A007522 |
| 10*n* + 1 | 11, 31, 41, 61, 71, 101, 131, 151, 181, 191, … | A030430 |
| 10*n* + 3 | 3, 13, 23, 43, 53, 73, 83, 103, 113, 163, … | A030431 |
| 10*n* + 7 | 7, 17, 37, 47, 67, 97, 107, 127, 137, 157, … | A030432 |
| 10*n* + 9 | 19, 29, 59, 79, 89, 109, 139, 149, 179, 199, … | A030433 |
| 12*n* + 1 | 13, 37, 61, 73, 97, 109, 157, 181, 193, 229, ... | A068228 |
| 12*n* + 5 | 5, 17, 29, 41, 53, 89, 101, 113, 137, 149, ... | A040117 |
| 12*n* + 7 | 7, 19, 31, 43, 67, 79, 103, 127, 139, 151, ... | A068229 |
| 12*n* + 11 | 11, 23, 47, 59, 71, 83, 107, 131, 167, 179, ... | A068231 |

We can generate some forms of primes by using an iterative method. For example, we can generate primes of the form 4*n* + 3 by using the following method:

Let *a*0 = 4(1) + 3 = 7. Then we let *a*1 = 4*a*0 + 3 = 4(7) + 3 = 31, which is prime. We continue by computing 4(7)(31) + 3 = 871 = 13(67). Because 4(7)(31) + 3 is of the form 4*n* + 3, either 13 or 67 is of the form 4*n* + 3. We have that 67 = 4(16) + 3 and is prime, so *a*3 = 67. We then continue this process to find successive primes of the form 4*n* + 3 (Silverman 2013).

## Distribution

Since the primes thin out, on average, in accordance with the prime number theorem, the same must be true for the primes in arithmetic progressions. It is natural to ask about the way the primes are shared between the various arithmetic progressions for a given value of *d* (there are *d* of those, essentially, if we do not distinguish two progressions sharing almost all their terms). The answer is given in this form: the number of feasible progressions *modulo* *d* – those where *a* and *d* do not have a common factor other than 1 – is given by Euler's totient function

$\varphi (d).$

Further, the proportion of primes in each of those is

${\frac {1}{\varphi (d)}}.$

For example, if *d* is a prime number *q*, each of the *q* − 1 progressions

$q+1,2q+1,3q+1,\dots$

$q+2,2q+2,3q+2,\dots$

$\dots \$

$q+q-1,2q+q-1,3q+q-1,\dots$

(all except

$q,2q,3q,\dots$

)

contains a proportion 1/(*q* − 1) of the primes.

When compared to each other, progressions with a quadratic nonresidue remainder have typically slightly more elements than those with a quadratic residue remainder (Chebyshev's bias).

## History

In 1737, Euler related the study of prime numbers to what is known now as the Riemann zeta function: he showed that the value *ζ*(1) reduces to a ratio of two infinite products, Π *p* / Π (*p* − 1), for all primes *p*, and that the ratio is infinite. In 1775, Euler stated the theorem for the cases of *a* + *nd*, where *a* = 1. This special case of Dirichlet's theorem can be proven using cyclotomic polynomials. The general form of the theorem was first conjectured by Legendre in his attempted unsuccessful proofs of quadratic reciprocity — as Gauss noted in his *Disquisitiones Arithmeticae* — but it was proved by Dirichlet (1837) with Dirichlet *L*-series. The proof is modeled on Euler's earlier work relating the Riemann zeta function to the distribution of primes. The theorem represents the beginning of rigorous analytic number theory. Atle Selberg gave an elementary proof of this theorem in 1949.

## Proof

Dirichlet's theorem is proved by showing that the value of the Dirichlet L-function (of a non-trivial character) at 1 is nonzero. The proof of this statement requires some calculus and analytic number theory (Serre 1973). The particular case *a* = 1 (i.e., concerning the primes that are congruent to 1 modulo some *n*) can be proven by analyzing the splitting behavior of primes in cyclotomic extensions, without making use of calculus (Neukirch 1999, §VII.6).

Although the proof of Dirichlet's Theorem makes use of calculus and analytic number theory, some proofs of examples are much more straightforward. In particular, the proof of the example of infinitely many primes of the form 4*n* + 3 makes an argument similar to the one made in the proof of Euclid's theorem (Silverman 2013). The proof is given below:

We want to prove that there are infinitely many primes of the form 4*n* + 3. Assume, for contradiction, that there are only finitely many primes of the form 4*n* + 3. We then compile a list of all such primes 3, *p*1, *p*2, ..., *p**m*, where *p*1 < *p*2 < ... < *p**m*. Let *N* = 4*p*1*p*2...*p**m* + 3. It is clear that none of the primes in the list 3, *p*1, *p*2, ..., *p**m* divide *N*. By cases, *N* is either composite or prime. If *N* is composite, then *N* has a unique prime factorization *N* = *a*1*a*2...*a**r*, where each *a**i* is prime. Because *N* ≡ 3 (mod 4), *N* is odd and must be the product of only odd primes. Any odd prime *p* must be such that *p* ≡ 1 (mod 4) or *p* ≡ 3 (mod 4). It cannot be that *a**i* ≡ 1 (mod 4) ∀*a**i* because if this were the case, then *N* ≡ 1 (mod 4). So there exists a prime *a*′ ≡ 3 (mod 4) such that *a*′ | *N* and *a*′ < *N*. Otherwise, if *N* is prime, then by definition *N* ≡ 3 (mod 4). So in both cases respectively, *a*′ and *N* satisfy the form 4*n* + 3, but are not in the list 3, *p*1, *p*2, ..., *p**m* since they both divide *N*, which is a contradiction. Therefore, this list doesn't contain all such primes and there must be infinitely many primes of the form 4*n* + 3 (Silverman 2013).

## Generalizations

The Bunyakovsky conjecture generalizes Dirichlet's theorem to higher-degree polynomials. Whether or not even simple quadratic polynomials such as *x*2 + 1 (known from Landau's fourth problem) attain infinitely many prime values is an important open problem.

Dickson's conjecture generalizes Dirichlet's theorem to more than one polynomial.

Schinzel's hypothesis H generalizes these two conjectures, i.e. generalizes to more than one polynomial with degree larger than one.

In algebraic number theory, Dirichlet's theorem generalizes to the Chebotarev's density theorem.

Linnik's theorem (1944) concerns the size of the smallest prime in a given arithmetic progression. Linnik proved that the progression *a* + *nd* (as *n* ranges through the positive integers) contains a prime of magnitude at most *cdL* for absolute constants *c* and *L*. Subsequent researchers have reduced *L* to 5.

An analogue of Dirichlet's theorem holds in the framework of dynamical systems (T. Sunada and A. Katsuda, 1990).

Shiu showed that any arithmetic progression satisfying the hypothesis of Dirichlet's theorem will in fact contain arbitrarily long runs of *consecutive* prime numbers.
