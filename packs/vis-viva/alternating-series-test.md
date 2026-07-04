---
title: "Alternating series test"
source: https://en.wikipedia.org/wiki/Alternating_series_test
domain: vis-viva
license: CC-BY-SA-4.0
tags: vis viva
fetched: 2026-07-04
---

# Alternating series test

In mathematical analysis, the **alternating series test** proves that an alternating series is convergent when its terms decrease monotonically in absolute value and approach zero in the limit. The test was devised by Gottfried Leibniz and is sometimes known as **Leibniz's test**, **Leibniz's rule**, or the **Leibniz criterion**. The test is only sufficient, not necessary, so some convergent alternating series may fail the first part of the test.

For a generalization, see Dirichlet's test.

## History

Leibniz discussed the criterion in his unpublished *De quadratura arithmetica* of 1676 and shared his result with Jakob Hermann in June 1705 and with Johann Bernoulli in October, 1713. It was only formally published in 1993.

## Formal statement

### Alternating series test

A series of the form

$\sum _{n=0}^{\infty }(-1)^{n}a_{n}=a_{0}-a_{1}+a_{2}-a_{3}+\cdots$

where either all *a**n* are positive or all *a**n* are negative, is called an alternating series.

The **alternating series test** guarantees that an alternating series converges if the following two conditions are met:

1. $|a_{n}|$ decreases monotonically, i.e., $|a_{n+1}|\leq |a_{n}|$ , and
2. $\lim _{n\to \infty }a_{n}=0$ .

### Alternating series estimation theorem

Moreover, let *L* denote the sum of the series, then the partial sum ${\textstyle S_{k}=\sum _{n=0}^{k}(-1)^{n}a_{n}\!}$ approximates *L* with error bounded by the next omitted term:

$\left|S_{k}-L\right\vert \leq \left|S_{k}-S_{k+1}\right\vert =a_{k+1}.\!$

## Proof

Suppose we are given a series of the form ${\textstyle \sum _{n=1}^{\infty }(-1)^{n-1}a_{n}\!}$ , where $\lim _{n\rightarrow \infty }a_{n}=0$ and $a_{n}\geq a_{n+1}$ for all natural numbers *n*. (The case ${\textstyle \sum _{n=1}^{\infty }(-1)^{n}a_{n}\!}$ follows by taking the negative.)

### Proof of the alternating series test

We will prove that both the partial sums ${\textstyle S_{2m+1}=\sum _{n=1}^{2m+1}(-1)^{n-1}a_{n}}$ with odd number of terms, and ${\textstyle S_{2m}=\sum _{n=1}^{2m}(-1)^{n-1}a_{n}}$ with even number of terms, converge to the same number *L*. Thus the usual partial sum ${\textstyle S_{k}=\sum _{n=1}^{k}(-1)^{n-1}a_{n}}$ also converges to *L*.

The odd partial sums decrease monotonically:

$S_{2(m+1)+1}=S_{2m+1}-a_{2m+2}+a_{2m+3}\leq S_{2m+1}$

while the even partial sums increase monotonically:

$S_{2(m+1)}=S_{2m}+a_{2m+1}-a_{2m+2}\geq S_{2m}$

both because *a**n* decreases monotonically with *n*.

Moreover, since *a**n* are positive, $S_{2m+1}-S_{2m}=a_{2m+1}\geq 0$ . Thus we can collect these facts to form the following suggestive inequality:

$a_{1}-a_{2}=S_{2}\leq S_{2m}\leq S_{2m+1}\leq S_{1}=a_{1}.$

Now, note that *a**1* − *a**2* is a lower bound of the monotonically decreasing sequence *S**2m+1*, the monotone convergence theorem then implies that this sequence converges as *m* approaches infinity. Similarly, the sequence of even partial sum converges too.

Finally, they must converge to the same number because $\lim _{m\to \infty }(S_{2m+1}-S_{2m})=\lim _{m\to \infty }a_{2m+1}=0$ .

Call the limit *L*, then the monotone convergence theorem also tells us extra information that

$S_{2m}\leq L\leq S_{2m+1}$

for any *m*. This means the partial sums of an alternating series also "alternates" above and below the final limit. More precisely, when there is an odd (even) number of terms, i.e. the last term is a plus (minus) term, then the partial sum is above (below) the final limit.

This understanding leads immediately to an error bound of partial sums, shown below.

### Proof of the alternating series estimation theorem

We would like to show $\left|S_{k}-L\right|\leq a_{k+1}\!$ by splitting into two cases.

When *k* = 2*m*+1, i.e. odd, then

$\left|S_{2m+1}-L\right|=S_{2m+1}-L\leq S_{2m+1}-S_{2m+2}=a_{(2m+1)+1}.$

When *k* = 2*m*, i.e. even, then

$\left|S_{2m}-L\right|=L-S_{2m}\leq S_{2m+1}-S_{2m}=a_{2m+1}$

as desired.

Both cases rely essentially on the last inequality derived in the previous proof.

### Newer error bounds

Philip Calabrese (1962) and Richard Johnsonbaugh (1979) have found tighter bounds.

## Examples

### A typical example

The alternating harmonic series

$\sum _{n=1}^{\infty }{\frac {(-1)^{n+1}}{n}}=1-{\frac {1}{2}}+{\frac {1}{3}}-{\frac {1}{4}}+{\frac {1}{5}}-\cdots$

meets both conditions for the alternating series test and converges.

### Monotonicity is needed

Both conditions in the test must be met for the conclusion to be true. For example, take the series

${\frac {1}{{\sqrt {2}}-1}}-{\frac {1}{{\sqrt {2}}+1}}+{\frac {1}{{\sqrt {3}}-1}}-{\frac {1}{{\sqrt {3}}+1}}+\cdots \ .$

The signs are alternating and the terms tend to zero. However, monotonicity is not present and we cannot apply the test. Actually, the series is divergent. Indeed, for the partial sum ${\textstyle S_{2n}}$ we have ${\textstyle S_{2n}={\frac {2}{1}}+{\frac {2}{2}}+{\frac {2}{3}}+\cdots +{\frac {2}{n-1}}}$ which is twice the partial sum of the harmonic series, which is divergent. Hence the original series is divergent.

### The test is sufficient, but not necessary

Leibniz test's monotonicity is not a necessary condition, thus the test itself is only sufficient, but not necessary.

Examples of nonmonotonic series that converge are:

$\sum _{n=2}^{\infty }{\frac {(-1)^{n}}{n+(-1)^{n}}}\quad {\text{and}}\quad \sum _{n=1}^{\infty }(-1)^{n}{\frac {\cos ^{2}n}{n^{2}}}\ .$

In fact, for every monotonic series it is possible to obtain an infinite number of nonmonotonic series that converge to the same sum by permuting its terms with permutations satisfying the condition in Agnew's theorem.
