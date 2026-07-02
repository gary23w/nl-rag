---
title: "Szemerédi's theorem"
source: https://en.wikipedia.org/wiki/Szemer%C3%A9di's_theorem
domain: ramsey-theory
license: CC-BY-SA-4.0
tags: ramsey theory, ramsey's theorem, van der waerden's theorem, szemeredi theorem
fetched: 2026-07-02
---

# Szemerédi's theorem

In arithmetic combinatorics, **Szemerédi's theorem** is a result concerning arithmetic progressions in subsets of the integers. In 1936, Erdős and Turán conjectured that every set of integers *A* with positive natural density contains a *k*-term arithmetic progression for every *k*. Endre Szemerédi proved the conjecture in 1975.

## Statement

A subset *A* of the natural numbers is said to have positive upper density if

$\limsup _{n\to \infty }{\frac {|A\cap \{1,2,3,\dotsc ,n\}|}{n}}>0.$

Szemerédi's theorem asserts that a subset of the natural numbers with positive upper density contains an arithmetic progression of length *k* for all positive integers *k*.

An often-used equivalent finitary version of the theorem states that for every positive integer *k* and real number $\delta \in (0,1]$ , there exists a positive integer

$N=N(k,\delta )$

such that every subset of {1, 2, ..., *N*} of size at least $\delta N$ contains an arithmetic progression of length *k*.

Another formulation uses the function *r**k*(*N*), the size of the largest subset of {1, 2, ..., *N*} without an arithmetic progression of length *k*. Szemerédi's theorem is equivalent to the asymptotic bound

$r_{k}(N)=o(N).$

That is, *r**k*(*N*) grows less than linearly with *N*.

## History

Van der Waerden's theorem, a precursor of Szemerédi's theorem, was proved in 1927.

The cases *k* = 1 and *k* = 2 of Szemerédi's theorem are trivial. The case *k* = 3, known as Roth's theorem, was established in 1953 by Klaus Roth via an adaptation of the Hardy–Littlewood circle method. Szemerédi next proved the case *k* = 4 through combinatorics. Using an approach similar to the one he used for the case *k* = 3, Roth gave a second proof for *k* = 4 in 1972.

The general case was settled in 1975, also by Szemerédi, who developed an ingenious and complicated extension of his previous combinatorial argument for *k* = 4 (called "a masterpiece of combinatorial reasoning" by Erdős). Several other proofs are now known, the most important being those by Hillel Furstenberg in 1977, using ergodic theory, and by Timothy Gowers in 2001, using both Fourier analysis and combinatorics while also introducing what is now called the Gowers norm. Terence Tao has called the various proofs of Szemerédi's theorem a "Rosetta stone" for connecting disparate fields of mathematics.

## Quantitative bounds

It is an open problem to determine the exact growth rate of *r**k*(*N*). The best known general bounds are

$CN\exp \left(-n2^{(n-1)/2}{\sqrt[{n}]{\log N}}+{\frac {1}{2n}}\log \log N\right)\leq r_{k}(N)\leq {\frac {N}{(\log \log N)^{2^{-2^{k+9}}}}},$

where $n=\lceil \log k\rceil$ . The lower bound is due to O'Bryant building on the work of Behrend, Rankin, and Elkin. The upper bound is due to Gowers.

For small *k*, there are tighter bounds than the general case. When *k* = 3, Bourgain, Heath-Brown, Szemerédi, Sanders, and Bloom established progressively smaller upper bounds, and Bloom and Sisask then proved the first bound that broke the so-called "logarithmic barrier". The current best bounds are

$N2^{-{\sqrt {8\log N}}}\leq r_{3}(N)\leq Ne^{-c(\log N)^{1/9}}$

, for some constant

$c>0$

,

respectively due to O'Bryant, and Bloom and Sisask (the latter built upon the breakthrough result of Kelley and Meka, who obtained the same upper bound, with "1/9" replaced by "1/12").

For *k* = 4, Green and Tao proved that

$r_{4}(N)\leq C{\frac {N}{(\log N)^{c}}}$

For k=5 in 2023 and k≥5 in 2024 Leng, Sah and Sawhney proved in preprints that:

$r_{k}(N)\leq CN\exp(-(\log \log N)^{c})$

## Extensions and generalizations

A multidimensional generalization of Szemerédi's theorem was first proven by Hillel Furstenberg and Yitzhak Katznelson using ergodic theory. Timothy Gowers, Vojtěch Rödl and Jozef Skokan with Brendan Nagle, Rödl, and Mathias Schacht, and Terence Tao provided combinatorial proofs.

Alexander Leibman and Vitaly Bergelson generalized Szemerédi's to polynomial progressions: If $A\subset \mathbb {N}$ is a set with positive upper density and $p_{1}(n),p_{2}(n),\dotsc ,p_{k}(n)$ are integer-valued polynomials such that $p_{i}(0)=0$ , then there are infinitely many $u,n\in \mathbb {Z}$ such that $u+p_{i}(n)\in A$ for all $1\leq i\leq k$ . Leibman and Bergelson's result also holds in a multidimensional setting.

The finitary version of Szemerédi's theorem can be generalized to finite additive groups including vector spaces over finite fields. The finite field analog can be used as a model for understanding the theorem in the natural numbers. The problem of obtaining bounds in the k=3 case of Szemerédi's theorem in the vector space $\mathbb {F} _{3}^{n}$ is known as the cap set problem.

The Green–Tao theorem asserts the prime numbers contain arbitrarily long arithmetic progressions. It is not implied by Szemerédi's theorem because the primes have density 0 in the natural numbers. As part of their proof, Ben Green and Tao introduced a "relative" Szemerédi theorem which applies to subsets of the integers (even those with 0 density) satisfying certain pseudorandomness conditions. A more general relative Szemerédi theorem has since been given by David Conlon, Jacob Fox, and Yufei Zhao.

The Erdős conjecture on arithmetic progressions would imply both Szemerédi's theorem and the Green–Tao theorem.
