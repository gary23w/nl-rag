---
title: "Ostrowski's theorem"
source: https://en.wikipedia.org/wiki/Ostrowski's_theorem
domain: p-adic-analysis
license: CC-BY-SA-4.0
tags: p-adic analysis, p-adic number, hensel's lemma, local field
fetched: 2026-07-02
---

# Ostrowski's theorem

In number theory, **Ostrowski's theorem**, due to Alexander Ostrowski (1916), states that every non-trivial absolute value on the rational numbers $\mathbb {Q}$ is equivalent to either the usual real absolute value or a p-adic absolute value.

## Theorem statement

An **absolute value** on the rational numbers is a function $|\cdot |_{*}:\mathbb {Q} \to \mathbb {R}$ satisfying for all $x,y\in \mathbb {Q}$

1. $|x|_{*}\geq 0$ , with equality if and only if $x=0$
2. $|xy|_{*}=|x|_{*}|y|_{*}$
3. $|x+y|_{*}\leq |x|_{*}+|y|_{*}$

Two absolute values $|\cdot |$ and $|\cdot |_{*}$ on the rationals are defined to be **equivalent** if they induce the same topology; this can be shown to be equivalent to the existence of a positive real number $\lambda \in (0,\infty )$ such that

$|x|_{*}=|x|^{\lambda }$

for all rational x . (Note: In general, if $|x|$ is an absolute value, $|x|^{\lambda }$ is not necessarily an absolute value anymore; however *if* two absolute values are equivalent, then each is a positive power of the other.) The **trivial absolute value** on any field *K* is defined to be

$|x|_{0}:={\begin{cases}0,&x=0,\\1,&x\neq 0.\end{cases}}$

The **real absolute value** on the rationals $\mathbb {Q}$ is the standard absolute value on the reals, defined to be

$|x|_{\infty }:={\begin{cases}x,&x\geq 0,\\-x,&x<0.\end{cases}}$

This is sometimes written with a subscript 1 instead of infinity.

For a prime number p, the p-adic absolute value on $\mathbb {Q}$ is defined as follows: any non-zero rational x can be written uniquely as $x=p^{n}{\tfrac {a}{b}}$ , where a and b are coprime integers not divisible by p, and n is an integer; so we define

$|x|_{p}:={\begin{cases}0,&x=0,\\p^{-n},&x,\neq 0.\end{cases}}$

Ostrowski's theorem then states that if $|\cdot |_{*}:\mathbb {Q} \to \mathbb {R}$ is any absolute value on the rational numbers, then either $|\cdot |_{*}=|\cdot |_{0}$ , or $|\cdot |_{*}$ is equivalent to $|\cdot |$ , or $|\cdot |_{*}$ is equivalent to $|\cdot |_{p}$ .

## Proof

The following proof follows the one of Theorem 10.1 in Schikhof (2007).

Let $|\cdot |_{*}$ be an absolute value on the rationals. We start the proof by showing that it is entirely determined by the values it takes on prime numbers.

From the fact that $1\times 1=1$ and the multiplicativity property of the absolute value, we infer that $|1|_{*}^{2}=|1|_{*}$ . In particular, $|1|_{*}$ has to be 0 or 1 and since $1\neq 0$ , one must have $|1|_{*}=1$ . A similar argument shows that $|-1|_{*}=1$ .

For all positive integer n, the multiplicativity property entails $|-n|_{*}=|-1|_{*}\times |n|_{*}=|n|_{*}$ . In other words, the absolute value of a negative integer coincides with that of its opposite.

Let n be a positive integer. From the fact that $n^{-1}\times n=1$ and the multiplicativity property, we conclude that $|n^{-1}|_{*}=|n|_{*}^{-1}$ .

Let now r be a positive rational. There exist two coprime positive integers p and q such that $r=pq^{-1}$ . The properties above show that $|r|_{*}=|p|_{*}|q^{-1}|_{*}=|p|_{*}|q|_{*}^{-1}$ . Altogether, the absolute value of a positive rational is entirely determined from that of its numerator and denominator.

Finally, let $\mathbb {P}$ be the set of prime numbers. For all positive integer n, we can write

$n=\prod _{p\in \mathbb {P} }p^{v_{p}(n)},$

where $v_{p}(n)$ is the p-adic valuation of n. The multiplicativity property enables one to compute the absolute value of n from that of the prime numbers using the following relationship

$|n|_{*}=\left|\prod _{p\in \mathbb {P} }p^{v_{p}(n)}\right|_{*}=\prod _{p\in \mathbb {P} }|p|_{*}^{v_{p}(n)}.$

We continue the proof by separating two cases:

1. There exists a positive integer n such that $|n|_{*}>1$ ; or
2. For all integer n, one has $|n|_{*}\leq 1$ .

### First case

Suppose that there exists a positive integer n such that $|n|_{*}>1.$ Let k be a non-negative integer and b be a positive integer greater than 1 . We express $n^{k}$ in base b: there exist a positive integer m and integers $(c_{i})_{0\leq i<m}$ such that for all i, $0\leq c_{i}<b$ and $n^{k}=\sum _{i<m}c_{i}b^{i}$ . In particular, $n^{k}\geq b^{m-1}$ so $m\leq 1+k\log _{b}n$ .

Each term $|c_{i}b^{i}|_{*}$ is at most $(b-1)|b|_{*}^{i}$ . (By the multiplicative property, $|c_{i}b^{i}|_{*}=|c_{i}|_{*}|b|_{*}^{i}$ , then using the fact that $c_{i}$ is a digit, write $c_{i}=1+1+\cdots +1$ so by the triangle inequality, $|c_{i}|\leq |1|+|1|+\cdots +|1|=c_{i}\leq b-1$ .) Besides, $|b|_{*}^{i}$ is at most $\max\{1,|b|_{*}^{m-1}\}$ . By the triangle inequality and the above bound on m, it follows:

${\begin{aligned}|n|_{*}^{k}&\leq m\max _{i<m}\{|c_{i}b^{i}|_{*}\}\\&\leq m(b-1)\max\{1,|b|_{*}^{m-1}\}\\&\leq (1+k\log _{b}n)(b-1)\max\{1,|b|_{*}^{k\log _{b}n}\}.\end{aligned}}$

Therefore, raising both sides to the power $1/k$ , we obtain

$|n|_{*}\leq \left((1+k\log _{b}n)(b-1)\right)^{1/k}\max\{1,|b|_{*}^{\log _{b}n}\}.$

Finally, taking the limit as k tends to infinity shows that

$|n|_{*}\leq \max\{1,|b|_{*}^{\log _{b}n}\}.$

Together with the condition $|n|_{*}>1,$ the above argument leads to $|b|_{*}>1$ regardless of the choice of b (otherwise $|b|_{*}^{\log _{b}n}\leq 1$ implies $|n|_{*}\leq 1$ ). As a result, all integers greater than one have an absolute value strictly greater than one. Thus generalizing the above, for any choice of integers n and b greater than or equal to 2, we get

$|n|_{*}\leq |b|_{*}^{\log _{b}n},$

i.e.

$\log _{n}|n|_{*}\leq \log _{b}|b|_{*}.$

By symmetry, this inequality is an equality. In particular, for all $n\geq 2$ , $\log _{n}|n|_{*}=\log _{2}|2|_{*}=\lambda$ , i.e. $|n|_{*}=n^{\lambda }=|n|_{\infty }^{\lambda }$ . Because the triangle inequality implies that for all positive integers n we have $|n|_{*}\leq n$ , in this case we obtain more precisely that $0<\lambda \leq 1$ .

As per the above result on the determination of an absolute value by its values on the prime numbers, we easily see that $|r|_{*}=|r|_{\infty }^{\lambda }$ for all rational r, thus demonstrating equivalence to the real absolute value.

### Second case

Suppose that for all integer n, one has $|n|_{*}\leq 1$ . As our absolute value is non-trivial, there must exist a positive integer n for which $|n|_{*}<1.$ Decomposing $|n|_{*}$ on the prime numbers shows that there exists $p\in \mathbb {P}$ such that $|p|_{*}<1$ . We claim that in fact this is so for one prime number only.

Suppose *by way of contradiction* that p and q are two distinct primes with absolute value strictly less than 1. Let k be a positive integer such that $|p|_{*}^{k}$ and $|q|_{*}^{k}$ are smaller than $1/2$ . By Bézout's identity, since $p^{k}$ and $q^{k}$ are coprime, there exist two integers a and b such that $ap^{k}+bq^{k}=1.$ This yields a contradiction, as

$1=|1|_{*}\leq |a|_{*}|p|_{*}^{k}+|b|_{*}|q|_{*}^{k}<{\frac {|a|_{*}+|b|_{*}}{2}}\leq 1.$

This means that there exists a unique prime p such that $|p|_{*}<1$ and that for all other primes q, one has $|q|_{*}=1$ (from the hypothesis of this second case). Let $\lambda =-\log _{p}|p|_{*}$ . From $|p|_{*}<1$ , we infer that $0<\lambda <\infty$ . (And indeed in this case, all positive $\lambda$ give absolute values equivalent to the p-adic one.)

We finally verify that $|p|_{p}^{\lambda }=p^{-\lambda }=|p|_{*}$ and that for all other primes q, $|q|_{p}^{\lambda }=1=|q|_{*}$ . As per the above result on the determination of an absolute value by its values on the prime numbers, we conclude that $|r|_{*}=|r|_{p}^{\lambda }$ for all rational r, implying that this absolute value is equivalent to the p-adic one. $\blacksquare$

## Another Ostrowski's theorem

Another theorem states that any field, complete with respect to an Archimedean absolute value, is (algebraically and topologically) isomorphic to either the real numbers or the complex numbers. This is sometimes also referred to as Ostrowski's theorem.
