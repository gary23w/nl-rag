---
title: "Schur's theorem"
source: https://en.wikipedia.org/wiki/Schur's_theorem
domain: ramsey-theory
license: CC-BY-SA-4.0
tags: ramsey theory, ramsey's theorem, van der waerden's theorem, szemeredi theorem
fetched: 2026-07-02
---

# Schur's theorem

In discrete mathematics, **Schur's theorem** is any of several theorems of the mathematician Issai Schur. In differential geometry, **Schur's theorem** is a theorem of Axel Schur. In functional analysis, **Schur's theorem** is often called Schur's property, also due to Issai Schur.

## Ramsey theory

In Ramsey theory, **Schur's theorem** states that for every positive integer *c*, there exists a positive integer *S*, such that for every partition of the integers $\{1,\ldots ,S\}$ into *c* parts, one of the parts contains integers *x*, *y* and *z* with $x+y=z$ .

For every positive integer *c*, *S*(*c*) denotes the smallest number *S* such that for every partition of the integers $\{1,\ldots ,S\}$ into *c* parts, one of the parts contains integers *x*, *y*, and *z* with $x+y=z$ . Schur's theorem ensures that *S*(*c*) is well-defined for every positive integer *c*. The numbers of the form *S*(*c*) are called **Schur's numbers**.

Folkman's theorem generalizes Schur's theorem by stating that there exist arbitrarily large sets of integers, all of whose nonempty sums belong to the same part.

Using this definition, the only known Schur numbers are *S*(*n*) = 2, 5, 14, 45, and 161 (sequence A030126 in the OEIS). The proof that *S*(5) = 161 was announced in 2017 and required 2 petabytes of space.

## Combinatorics

In combinatorics, **Schur's theorem** tells the number of ways for expressing a given number as a (non-negative, integer) linear combination of a fixed set of relatively prime numbers. In particular, if $\{a_{1},\ldots ,a_{n}\}$ is a set of integers such that $\gcd(a_{1},\ldots ,a_{n})=1$ , the number of different multiples of non-negative integer numbers $(c_{1},\ldots ,c_{n})$ such that $x=c_{1}a_{1}+\cdots +c_{n}a_{n}$ when x goes to infinity is:

${\frac {x^{n-1}}{(n-1)!a_{1}\cdots a_{n}}}(1+o(1)).$

As a result, for every set of relatively prime numbers $\{a_{1},\ldots ,a_{n}\}$ there exists a value of x such that every larger number is representable as a linear combination of $\{a_{1},\ldots ,a_{n}\}$ in at least one way. This consequence of the theorem can be recast in a familiar context considering the problem of changing an amount using a set of coins. If the denominations of the coins are relatively prime numbers (such as 2 and 5) then any sufficiently large amount can be changed using only these coins. (See Coin problem.)

## Differential geometry

In differential geometry, **Schur's theorem** compares the distance between the endpoints of a space curve $C^{*}$ to the distance between the endpoints of a corresponding plane curve C of less curvature.

Suppose $C(s)$ is a plane curve with curvature $\kappa (s)$ which makes a convex curve when closed by the chord connecting its endpoints, and $C^{*}(s)$ is a curve of the same length with curvature $\kappa ^{*}(s)$ . Let d denote the distance between the endpoints of C and $d^{*}$ denote the distance between the endpoints of $C^{*}$ . If $\kappa ^{*}(s)\leq \kappa (s)$ then $d^{*}\geq d$ .

Schur's theorem is usually stated for $C^{2}$ curves, but John M. Sullivan has observed that the standard proof applies to curves of finite total curvature (the statement is slightly different).

Mohammad Ghomi generalized Schur's theorem to curves in Cartan-Hadamard manifolds.

## Linear algebra

In linear algebra, Schur’s theorem is referred to as either the triangularization of a square matrix with complex entries, or of a square matrix with real entries and real eigenvalues.

## Functional analysis

In functional analysis and the study of Banach spaces, Schur's theorem, due to I. Schur, often refers to Schur's property, that for certain spaces, weak convergence implies convergence in the norm.

## Number theory

In number theory, Issai Schur showed in 1912 that for every nonconstant polynomial *p*(*x*) with integer coefficients, if *S* is the set of all nonzero values ${\begin{Bmatrix}p(n)\neq 0:n\in \mathbb {N} \end{Bmatrix}}$ , then the set of primes that divide some member of *S* is infinite.
