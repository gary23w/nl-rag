---
title: "Prime-counting function"
source: https://en.wikipedia.org/wiki/Prime-counting_function
domain: analytic-number-theory
license: CC-BY-SA-4.0
tags: analytic number theory, prime number theorem, dirichlet series, riemann hypothesis
fetched: 2026-07-02
---

# Prime-counting function

In mathematics, the **prime-counting function** is the function counting the number of prime numbers less than or equal to some real number x. It is denoted by *π*(*x*) (unrelated to the number π).

A symmetric variant seen sometimes is *π*0(*x*), which is equal to *π*(*x*) − 1⁄2 if x is exactly a prime number, and equal to *π*(*x*) otherwise. That is, the number of prime numbers less than x, plus half if x equals a prime.

## Growth rate

Of great interest in number theory is the growth rate of the prime-counting function. It was conjectured in the end of the 18th century by Gauss and by Legendre to be approximately ${\frac {x}{\log x}}$ where log is the natural logarithm, in the sense that $\lim _{x\rightarrow \infty }{\frac {\pi (x)}{x/\log x}}=1.$ This statement is the prime number theorem. An equivalent statement is $\lim _{x\rightarrow \infty }{\frac {\pi (x)}{\operatorname {li} (x)}}=1$ where li is the logarithmic integral function. The prime number theorem was first proved in 1896 by Jacques Hadamard and by Charles de la Vallée Poussin independently, using properties of the Riemann zeta function introduced by Riemann in 1859. Proofs of the prime number theorem not using the zeta function or complex analysis were found around 1948 by Atle Selberg and by Paul Erdős (for the most part independently).

### More precise estimates

In 1899, de la Vallée Poussin proved that $\pi (x)=\operatorname {li} (x)+O\left(xe^{-a{\sqrt {\log x}}}\right)\quad {\text{as }}x\to \infty$ for some positive constant a. Here, *O*(...) is the big O notation.

More precise estimates of *π*(*x*) are now known. For example, in 2002, Kevin Ford proved that $\pi (x)=\operatorname {li} (x)+O\left(x\exp \left(-0.2098(\log x)^{3/5}(\log \log x)^{-1/5}\right)\right).$

Mossinghoff and Trudgian proved an explicit upper bound for the difference between *π*(*x*) and li(*x*): ${\bigl |}\pi (x)-\operatorname {li} (x){\bigr |}\leq 0.2593{\frac {x}{(\log x)^{3/4}}}\exp \left(-{\sqrt {\frac {\log x}{6.315}}}\right)\quad {\text{for }}x\geq 229.$

For values of x that are not unreasonably large, li(*x*) is greater than *π*(*x*). However, *π*(*x*) − li(*x*) is known to change sign infinitely many times. For a discussion of this, see Skewes' number.

### Exact form

For *x* > 1 let *π*0(*x*) = *π*(*x*) − ⁠1/2⁠ when x is a prime number, and *π*0(*x*) = *π*(*x*) otherwise. Bernhard Riemann, in his work *On the Number of Primes Less Than a Given Magnitude*, proved that *π*0(*x*) is equal to

$\pi _{0}(x)=\operatorname {R} (x)-\sum _{\rho }\operatorname {R} (x^{\rho }),$ where $\operatorname {R} (x)=\sum _{n=1}^{\infty }{\frac {\mu (n)}{n}}\operatorname {li} \left(x^{1/n}\right),$ *μ*(*n*) is the Möbius function, li(*x*) is the logarithmic integral function, ρ indexes every zero of the Riemann zeta function, and li(*x*⁠*ρ*/*n*⁠) is not evaluated with a branch cut but instead considered as Ei(⁠*ρ*/*n*⁠ log *x*) where Ei(*x*) is the exponential integral. If the trivial zeros are collected and the sum is taken *only* over the non-trivial zeros ρ of the Riemann zeta function, then *π*0(*x*) may be approximated by $\pi _{0}(x)\approx \operatorname {R} (x)-\sum _{\rho }\operatorname {R} \left(x^{\rho }\right)-{\frac {1}{\log x}}+{\frac {1}{\pi }}\arctan {\frac {\pi }{\log x}}.$

The Riemann hypothesis suggests that every such non-trivial zero lies along Re(*s*) = ⁠1/2⁠.

## Table of *π*(*x*), ⁠*x*/log *x* ⁠, and li(*x*)

The table shows how the three functions *π*(*x*), ⁠*x*/log *x*⁠, and li(*x*) compared at powers of 10. See also, and

| x | *π*(*x*) | *π*(*x*) − ⁠*x*/log *x*⁠ | li(*x*) − *π*(*x*) | ⁠*x*/*π*(*x*)⁠ | ⁠*x*/log *x*⁠  % error |
|---|---|---|---|---|---|
| 10 | 4 | 0 | 2 | 2.500 | −8.57% |
| 102 | 25 | 3 | 5 | 4.000 | +13.14% |
| 103 | 168 | 23 | 10 | 5.952 | +13.83% |
| 104 | 1,229 | 143 | 17 | 8.137 | +11.66% |
| 105 | 9,592 | 906 | 38 | 10.425 | +9.45% |
| 106 | 78,498 | 6,116 | 130 | 12.739 | +7.79% |
| 107 | 664,579 | 44,158 | 339 | 15.047 | +6.64% |
| 108 | 5,761,455 | 332,774 | 754 | 17.357 | +5.78% |
| 109 | 50,847,534 | 2,592,592 | 1,701 | 19.667 | +5.10% |
| 1010 | 455,052,511 | 20,758,029 | 3,104 | 21.975 | +4.56% |
| 1011 | 4,118,054,813 | 169,923,159 | 11,588 | 24.283 | +4.13% |
| 1012 | 37,607,912,018 | 1,416,705,193 | 38,263 | 26.590 | +3.77% |
| 1013 | 346,065,536,839 | 11,992,858,452 | 108,971 | 28.896 | +3.47% |
| 1014 | 3,204,941,750,802 | 102,838,308,636 | 314,890 | 31.202 | +3.21% |
| 1015 | 29,844,570,422,669 | 891,604,962,452 | 1,052,619 | 33.507 | +2.99% |
| 1016 | 279,238,341,033,925 | 7,804,289,844,393 | 3,214,632 | 35.812 | +2.79% |
| 1017 | 2,623,557,157,654,233 | 68,883,734,693,928 | 7,956,589 | 38.116 | +2.63% |
| 1018 | 24,739,954,287,740,860 | 612,483,070,893,536 | 21,949,555 | 40.420 | +2.48% |
| 1019 | 234,057,667,276,344,607 | 5,481,624,169,369,961 | 99,877,775 | 42.725 | +2.34% |
| 1020 | 2,220,819,602,560,918,840 | 49,347,193,044,659,702 | 222,744,644 | 45.028 | +2.22% |
| 1021 | 21,127,269,486,018,731,928 | 446,579,871,578,168,707 | 597,394,254 | 47.332 | +2.11% |
| 1022 | 201,467,286,689,315,906,290 | 4,060,704,006,019,620,994 | 1,932,355,208 | 49.636 | +2.02% |
| 1023 | 1,925,320,391,606,803,968,923 | 37,083,513,766,578,631,309 | 7,250,186,216 | 51.939 | +1.93% |
| 1024 | 18,435,599,767,349,200,867,866 | 339,996,354,713,708,049,069 | 17,146,907,278 | 54.243 | +1.84% |
| 1025 | 176,846,309,399,143,769,411,680 | 3,128,516,637,843,038,351,228 | 55,160,980,939 | 56.546 | +1.77% |
| 1026 | 1,699,246,750,872,437,141,327,603 | 28,883,358,936,853,188,823,261 | 155,891,678,121 | 58.850 | +1.70% |
| 1027 | 16,352,460,426,841,680,446,427,399 | 267,479,615,610,131,274,163,365 | 508,666,658,006 | 61.153 | +1.64% |
| 1028 | 157,589,269,275,973,410,412,739,598 | 2,484,097,167,669,186,251,622,127 | 1,427,745,660,374 | 63.456 | +1.58% |
| 1029 | 1,520,698,109,714,272,166,094,258,063 | 23,130,930,737,541,725,917,951,446 | 4,551,193,622,464 | 65.759 | +1.52% |

In the On-Line Encyclopedia of Integer Sequences, the *π*(*x*) column is sequence OEIS: A006880, *π*(*x*) − ⁠*x*/log *x*⁠ is sequence OEIS: A057835, and li(*x*) − *π*(*x*) is sequence OEIS: A057752.

The value for *π*(1024) was originally computed by J. Buethe, J. Franke, A. Jost, and T. Kleinjung assuming the Riemann hypothesis. It was later verified unconditionally in a computation by D. J. Platt. The value for *π*(1025) is by the same four authors. The value for *π*(1026) was computed by D. B. Staple. All other prior entries in this table were also verified as part of that work.

The values for 1027, 1028, and 1029 were announced by David Baugh and Kim Walisch in 2015, 2020, and 2022, respectively.

## Algorithms for evaluating *π*(*x*)

A simple way to find *π*(*x*), if x is not too large, is to use the sieve of Eratosthenes to produce the primes less than or equal to x and then to count them.

A more elaborate way of finding *π*(*x*) is due to Legendre (using the inclusion–exclusion principle): given x, if *p*1, *p*2,…, *pn* are distinct prime numbers, then the number of integers less than or equal to x which are divisible by no pi is

$\lfloor x\rfloor -\sum _{i}\left\lfloor {\frac {x}{p_{i}}}\right\rfloor +\sum _{i<j}\left\lfloor {\frac {x}{p_{i}p_{j}}}\right\rfloor -\sum _{i<j<k}\left\lfloor {\frac {x}{p_{i}p_{j}p_{k}}}\right\rfloor +\cdots$

(where ⌊*x*⌋ denotes the floor function). This number is therefore equal to

$\pi (x)-\pi \left({\sqrt {x}}\right)+1$

when the numbers *p*1, *p*2,…, *pn* are the prime numbers less than or equal to the square root of x.

### The Meissel–Lehmer algorithm

In a series of articles published between 1870 and 1885, Ernst Meissel described (and used) a practical combinatorial way of evaluating *π*(*x*): Let *p*1, *p*2,…, *pn* be the first n primes and denote by Φ(*m*,*n*) the number of natural numbers not greater than m which are divisible by none of the pi for any *i* ≤ *n*. Then

$\Phi (m,n)=\Phi (m,n-1)-\Phi \left({\frac {m}{p_{n}}},n-1\right).$

Given a natural number m, if *n* = *π*(3√*m*) and if *μ* = *π*(√*m*) − *n*, then

$\pi (m)=\Phi (m,n)+n(\mu +1)+{\frac {\mu ^{2}-\mu }{2}}-1-\sum _{k=1}^{\mu }\pi \left({\frac {m}{p_{n+k}}}\right).$

Using this approach, Meissel computed *π*(*x*), for x equal to 5×105, 106, 107, and 108.

In 1959, Derrick Henry Lehmer extended and simplified Meissel's method. Define, for real m and for natural numbers n and k, *Pk*(*m*,*n*) as the number of numbers not greater than m with exactly k prime factors, all greater than pn. Furthermore, set *P*0(*m*,*n*) = 1. Then

$\Phi (m,n)=\sum _{k=0}^{+\infty }P_{k}(m,n)$

where the sum actually has only finitely many nonzero terms. Let y denote an integer such that 3√*m* ≤ *y* ≤ √*m*, and set *n* = *π*(*y*). Then *P*1(*m*,*n*) = *π*(*m*) − *n* and *Pk*(*m*,*n*) = 0 when *k* ≥ 3. Therefore,

$\pi (m)=\Phi (m,n)+n-1-P_{2}(m,n)$

The computation of *P*2(*m*,*n*) can be obtained this way:

$P_{2}(m,n)=\sum _{y<p\leq {\sqrt {m}}}\left(\pi \left({\frac {m}{p}}\right)-\pi (p)+1\right)$

where the sum is over prime numbers.

On the other hand, the computation of Φ(*m*,*n*) can be done using the following rules:

1. $\Phi (m,0)=\lfloor m\rfloor$
2. $\Phi (m,b)=\Phi (m,b-1)-\Phi \left({\frac {m}{p_{b}}},b-1\right)$

Using his method and an IBM 701, Lehmer was able to compute the correct value of *π*(109) and missed the correct value of *π*(1010) by 1.

Further improvements to this method were made by Lagarias, Miller, Odlyzko, Deléglise, and Rivat.

## Other prime-counting functions

Other prime-counting functions are also used because they are more convenient to work with.

### Riemann's prime-power counting function

Riemann's prime-power counting function is usually denoted as Π0(*x*) or *J*0(*x*). It has jumps of ⁠1/*n*⁠ at prime powers pn and it takes a value halfway between the two sides at the discontinuities of *π*(*x*). That added detail is used because the function may then be defined by an inverse Mellin transform.

Formally, we may define Π0(*x*) by

$\Pi _{0}(x)={\frac {1}{2}}\left(\sum _{p^{n}<x}{\frac {1}{n}}+\sum _{p^{n}\leq x}{\frac {1}{n}}\right)\$

where the variable p in each sum ranges over all primes within the specified limits.

We may also write

$\ \Pi _{0}(x)=\sum _{n=2}^{x}{\frac {\Lambda (n)}{\log n}}-{\frac {\Lambda (x)}{2\log x}}=\sum _{n=1}^{\infty }{\frac {1}{n}}\pi _{0}\left(x^{1/n}\right)$

where Λ is the von Mangoldt function and

$\pi _{0}(x)=\lim _{\varepsilon \to 0}{\frac {\pi (x-\varepsilon )+\pi (x+\varepsilon )}{2}}.$

The Möbius inversion formula then gives

$\pi _{0}(x)=\sum _{n=1}^{\infty }{\frac {\mu (n)}{n}}\ \Pi _{0}\left(x^{1/n}\right),$

where *μ*(*n*) is the Möbius function.

Knowing the relationship between the logarithm of the Riemann zeta function and the von Mangoldt function Λ, and using the Perron formula we have

$\log \zeta (s)=s\int _{0}^{\infty }\Pi _{0}(x)x^{-s-1}\,\mathrm {d} x$

### Chebyshev's function

The Chebyshev function weights primes or prime powers pn by log *p*:

${\begin{aligned}\vartheta (x)&=\sum _{p\leq x}\log p\\\psi (x)&=\sum _{p^{n}\leq x}\log p=\sum _{n=1}^{\infty }\vartheta \left(x^{1/n}\right)=\sum _{n\leq x}\Lambda (n).\end{aligned}}$

For *x* ≥ 2,

$\vartheta (x)=\pi (x)\log x-\int _{2}^{x}{\frac {\pi (t)}{t}}\,\mathrm {d} t$

and

$\pi (x)={\frac {\vartheta (x)}{\log x}}+\int _{2}^{x}{\frac {\vartheta (t)}{t\log ^{2}(t)}}\mathrm {d} t.$

## Formulas for prime-counting functions

Formulas for prime-counting functions come in two kinds: arithmetic formulas and analytic formulas. Analytic formulas for prime-counting were the first used to prove the prime number theorem. They stem from the work of Riemann and von Mangoldt, and are generally known as explicit formulae.

We have the following expression for the second Chebyshev function ψ:

$\psi _{0}(x)=x-\sum _{\rho }{\frac {x^{\rho }}{\rho }}-\log 2\pi -{\frac {1}{2}}\log \left(1-x^{-2}\right),$

where

$\psi _{0}(x)=\lim _{\varepsilon \to 0}{\frac {\psi (x-\varepsilon )+\psi (x+\varepsilon )}{2}}.$

Here ρ are the zeros of the Riemann zeta function in the critical strip, where the real part of ρ is between zero and one. The formula is valid for values of x greater than one, which is the region of interest. The sum over the roots is conditionally convergent, and should be taken in order of increasing absolute value of the imaginary part. Note that the same sum over the trivial roots gives the last subtrahend in the formula.

For *Π*0(*x*) we have a more complicated formula

$\Pi _{0}(x)=\operatorname {li} (x)-\sum _{\rho }\operatorname {li} \left(x^{\rho }\right)-\log 2+\int _{x}^{\infty }{\frac {\mathrm {d} t}{t\left(t^{2}-1\right)\log t}}.$

Again, the formula is valid for *x* > 1, while ρ are the nontrivial zeros of the zeta function ordered according to their absolute value. The first term li(*x*) is the usual logarithmic integral function; the expression li(*xρ*) in the second term should be considered as Ei(*ρ* log *x*), where Ei is the analytic continuation of the exponential integral function from negative reals to the complex plane with branch cut along the positive reals. The final integral is equal to the series over the trivial zeros:

$\int _{x}^{\infty }{\frac {\mathrm {d} t}{t\left(t^{2}-1\right)\log t}}=\int _{x}^{\infty }{\frac {1}{t\log t}}\left(\sum _{m}t^{-2m}\right)\,\mathrm {d} t=\sum _{m}\int _{x}^{\infty }{\frac {t^{-2m}}{t\log t}}\,\mathrm {d} t\,\,{\overset {\left(u=t^{-2m}\right)}{=}}-\sum _{m}\operatorname {li} \left(x^{-2m}\right)$

Thus, Möbius inversion formula gives us

$\pi _{0}(x)=\operatorname {R} (x)-\sum _{\rho }\operatorname {R} \left(x^{\rho }\right)-\sum _{m}\operatorname {R} \left(x^{-2m}\right)$

valid for *x* > 1, where

$\operatorname {R} (x)=\sum _{n=1}^{\infty }{\frac {\mu (n)}{n}}\operatorname {li} \left(x^{1/n}\right)=1+\sum _{k=1}^{\infty }{\frac {\left(\log x\right)^{k}}{k!k\zeta (k+1)}}$

is Riemann's R-function and *μ*(*n*) is the Möbius function. The latter series for it is known as Gram series. Because log *x* < *x* for all *x* > 0, this series converges for all positive x by comparison with the series for ex. The logarithm in the Gram series of the sum over the non-trivial zero contribution should be evaluated as *ρ* log *x* and not log *xρ*.

Folkmar Bornemann proved, when assuming the conjecture that all zeros of the Riemann zeta function are simple, that

$\operatorname {R} \left(e^{-2\pi t}\right)={\frac {1}{\pi }}\sum _{k=1}^{\infty }{\frac {(-1)^{k-1}t^{-2k-1}}{(2k+1)\zeta (2k+1)}}+{\frac {1}{2}}\sum _{\rho }{\frac {t^{-\rho }}{\rho \cos {\frac {\pi \rho }{2}}\zeta '(\rho )}}$

where ρ runs over the non-trivial zeros of the Riemann zeta function and *t* > 0.

The sum over non-trivial zeta zeros in the formula for *π*0(*x*) describes the fluctuations of *π*0(*x*) while the remaining terms give the "smooth" part of prime-counting function, so one can use

$\operatorname {R} (x)-\sum _{m=1}^{\infty }\operatorname {R} \left(x^{-2m}\right)$

as a good estimator of *π*(*x*) for *x* > 1. In fact, since the second term approaches 0 as *x* → ∞, while the amplitude of the "noisy" part is heuristically about ⁠√*x*/log *x*⁠, estimating *π*(*x*) by R(*x*) alone is just as good, and fluctuations of the distribution of primes may be clearly represented with the function

${\bigl (}\pi _{0}(x)-\operatorname {R} (x){\bigr )}{\frac {\log x}{\sqrt {x}}}.$

## Inequalities

Ramanujan proved that the inequality

$\pi (x)^{2}<{\frac {ex}{\log x}}\pi \left({\frac {x}{e}}\right)$

holds for all sufficiently large values of x.

Here are some useful inequalities for *π*(*x*).

${\frac {x}{\log x}}<\pi (x)<1.25506{\frac {x}{\log x}}\quad {\text{for }}x\geq 17.$

The left inequality holds for *x* ≥ 17 and the right inequality holds for *x* > 1. The constant 1.25506 is 30⁠log 113/113⁠ to 5 decimal places, as *π*(*x*) ⁠log *x*/*x*⁠ has its maximum value at *x* = *p*30 = 113.

Pierre Dusart proved in 2010:

${\frac {x}{\log x-1}}<\pi (x)<{\frac {x}{\log x-1.1}}\quad {\text{for }}x\geq 5393{\text{ and }}x\geq 60184,{\text{ respectively.}}$

More recently, Dusart has proved (Theorem 5.1) that

${\frac {x}{\log x}}\left(1+{\frac {1}{\log x}}+{\frac {2}{\log ^{2}x}}\right)\leq \pi (x)\leq {\frac {x}{\log x}}\left(1+{\frac {1}{\log x}}+{\frac {2}{\log ^{2}x}}+{\frac {7.59}{\log ^{3}x}}\right),$

for *x* ≥ 88789 and *x* > 1, respectively.

Going in the other direction, an approximation for the nth prime, pn, is

$p_{n}=n\left(\log n+\log \log n-1+{\frac {\log \log n-2}{\log n}}+O\left({\frac {(\log \log n)^{2}}{(\log n)^{2}}}\right)\right).$

Here are some inequalities for the nth prime. The lower bound is due to Dusart (1999) and the upper bound to Rosser (1941).

$n(\log n+\log \log n-1)<p_{n}<n(\log n+\log \log n)\quad {\text{for }}n\geq 6.$

The left inequality holds for *n* ≥ 2 and the right inequality holds for *n* ≥ 6. A variant form sometimes seen substitutes $\log n+\log \log n=\log(n\log n).$ An even simpler lower bound is

$n\log n<p_{n},$

which holds for all *n* ≥ 1, but the lower bound above is tighter for *n* > *ee* ≈15.154.

In 2010 Dusart proved (Propositions 6.7 and 6.6) that

$n\left(\log n+\log \log n-1+{\frac {\log \log n-2.1}{\log n}}\right)\leq p_{n}\leq n\left(\log n+\log \log n-1+{\frac {\log \log n-2}{\log n}}\right),$

for *n* ≥ 3 and *n* ≥ 688383, respectively.

In 2024, Axler further tightened this (equations 1.12 and 1.13) using bounds of the form

$f(n,g(w))=n\left(\log n+\log \log n-1+{\frac {\log \log n-2}{\log n}}-{\frac {g(\log \log n)}{2\log ^{2}n}}\right)$

proving that

$f(n,w^{2}-6w+11.321)\leq p_{n}\leq f(n,w^{2}-6w)$

for *n* ≥ 2 and *n* ≥ 3468, respectively. The lower bound may also be simplified to *f*(*n*, *w*2) without altering its validity. The upper bound may be tightened to *f*(*n*, *w*2 − 6*w* + 10.667) if *n* ≥ 46254381.

There are additional bounds of varying complexity.

## The Riemann hypothesis

The Riemann hypothesis implies a much tighter bound on the error in the estimate for *π*(*x*), and hence to a more regular distribution of prime numbers,

$\pi (x)=\operatorname {li} (x)+O({\sqrt {x}}\log {x}).$

Specifically,

$|\pi (x)-\operatorname {li} (x)|<{\frac {\sqrt {x}}{8\pi }}\,\log {x},\quad {\text{for all }}x\geq 2657.$

Dudek (2015) proved that the Riemann hypothesis implies that for all *x* ≥ 2 there is a prime p satisfying

$x-{\frac {4}{\pi }}{\sqrt {x}}\log x<p\leq x.$
