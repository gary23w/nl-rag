---
title: "p-adic valuation"
source: https://en.wikipedia.org/wiki/P-adic_valuation
domain: p-adic-analysis
license: CC-BY-SA-4.0
tags: p-adic analysis, p-adic number, hensel's lemma, local field
fetched: 2026-07-02
---

# p-adic valuation

In number theory, the **p-adic valuation** or **p-adic order** of an integer n is the exponent of the highest power of the prime number p that divides n. It is denoted $\nu _{p}(n)$ or $\operatorname {val} _{p}(n)$ . Equivalently, $\nu _{p}(n)$ is the exponent to which p appears in the prime factorization of n .

The p-adic valuation is a valuation and gives rise to an analogue of the usual absolute value, though unlike the latter, the p-adic absolute value is not Archimedean. Whereas the completion of the rational numbers with respect to the usual absolute value results in the real numbers $\mathbb {R}$ , the completion of the rational numbers with respect to the p-adic absolute value results in the p-adic numbers $\mathbb {Q} _{p}$ .

## Definition and properties

Let p be a prime number.

### Integers

The **p-adic valuation** of an integer n is defined to be

$\nu _{p}(n)={\begin{cases}\mathrm {max} \{k\in \mathbb {N} _{0}:p^{k}\mid n\}&{\text{if }}n\neq 0\\\infty &{\text{if }}n=0,\end{cases}}$

where $\mathbb {N} _{0}$ denotes the set of natural numbers (including zero) and $m\mid n$ denotes divisibility of n by m . In particular, $\nu _{p}$ is a function $\nu _{p}\colon \mathbb {Z} \to \mathbb {N} _{0}\cup \{\infty \}$ .

For example, $\nu _{2}(-12)=2$ , $\nu _{3}(-12)=1$ , and $\nu _{5}(-12)=0$ since $|{-12}|=12=2^{2}\cdot 3^{1}\cdot 5^{0}$ .

The notation $p^{k}\parallel n$ is sometimes used to mean $k=\nu _{p}(n)$ .

If n is a positive integer, then $\nu _{p}(n)\leq \log _{p}n$ ; this follows directly from $n\geq p^{\nu _{p}(n)}$ .

### Rational numbers

The p-adic valuation can be extended to the rational numbers as the function

$\nu _{p}:\mathbb {Q} \to \mathbb {Z} \cup \{\infty \}$

defined by

$\nu _{p}\left({\frac {r}{s}}\right)=\nu _{p}(r)-\nu _{p}(s).$

For example, $\nu _{2}{\bigl (}{\tfrac {9}{8}}{\bigr )}=-3$ and $\nu _{3}{\bigl (}{\tfrac {9}{8}}{\bigr )}=2$ since ${\tfrac {9}{8}}=2^{-3}\cdot 3^{2}$ .

Some properties are:

$\nu _{p}(r\cdot s)=\nu _{p}(r)+\nu _{p}(s)$

$\nu _{p}(r+s)\geq \min {\bigl \{}\nu _{p}(r),\nu _{p}(s){\bigr \}}$

Moreover, if $\nu _{p}(r)\neq \nu _{p}(s)$ , then

$\nu _{p}(r+s)=\min {\bigl \{}\nu _{p}(r),\nu _{p}(s){\bigr \}}$

where $\min$ is the minimum (i.e. the smaller of the two).

### Formula for the p-adic valuation of integers

Legendre's formula shows that $\nu _{p}(n!)=\sum _{i=1}^{\infty {}}{\left\lfloor {\frac {n}{p^{i}}}\right\rfloor {}}$ .

For any positive integer n, $n={\frac {n!}{(n-1)!}}$ and so $\nu _{p}(n)=\nu _{p}(n!)-\nu _{p}((n-1)!)$ .

Therefore, $\nu {}_{p}(n)=\sum _{i=1}^{\infty {}}{{\bigg (}\left\lfloor {\frac {n}{p^{i}}}\right\rfloor {}-\left\lfloor {\frac {n-1}{p^{i}}}\right\rfloor {}{\bigg )}}$ .

This infinite sum can be reduced to $\sum _{i=1}^{\lfloor {\log _{p}{(n)}\rfloor {}}}{{\bigg (}\left\lfloor {\frac {n}{p^{i}}}\right\rfloor {}-\left\lfloor {\frac {n-1}{p^{i}}}\right\rfloor {}{\bigg )}}$ .

This formula can be extended to negative integer values to give:

$\nu {}_{p}(n)=\sum _{i=1}^{\lfloor {\log _{p}{(|n|)}\rfloor {}}}{{\bigg (}\left\lfloor {\frac {|n|}{p^{i}}}\right\rfloor {}-\left\lfloor {\frac {|n|-1}{p^{i}}}\right\rfloor {}{\bigg )}}$

## p-adic absolute value

The p-adic absolute value (or p-adic norm, though not a norm in the sense of analysis) on $\mathbb {Q}$ is the function

$|\cdot |_{p}\colon \mathbb {Q} \to \mathbb {R} _{\geq 0}$

defined by

$|r|_{p}=p^{-\nu _{p}(r)}.$

Thereby, $|0|_{p}=p^{-\infty }=0$ for all p and for example, $|{-12}|_{2}=2^{-2}={\tfrac {1}{4}}$ and ${\bigl |}{\tfrac {9}{8}}{\bigr |}_{2}=2^{-(-3)}=8.$

The p-adic absolute value satisfies the following properties.

| Non-negativity | $\|r\|_{p}\geq 0$ |
|---|---|
| Positive-definiteness | $\|r\|_{p}=0\iff r=0$ |
| Multiplicativity | $\|rs\|_{p}=\|r\|_{p}\|s\|_{p}$ |
| Non-Archimedean | $\|r+s\|_{p}\leq \max \left(\|r\|_{p},\|s\|_{p}\right)$ |

From the multiplicativity $|rs|_{p}=|r|_{p}|s|_{p}$ it follows that $|1|_{p}=1=|{-1}|_{p}$ for the roots of unity 1 and $-1$ and consequently also $|{-r}|_{p}=|r|_{p}.$ The subadditivity $|r+s|_{p}\leq |r|_{p}+|s|_{p}$ follows from the non-Archimedean triangle inequality $|r+s|_{p}\leq \max \left(|r|_{p},|s|_{p}\right)$ .

### Product formula

The choice of base p in the exponentiation $p^{-\nu _{p}(r)}$ makes no difference for most of the properties, but supports the product formula:

$\prod _{0,p}|r|_{p}=1$

where the product is taken over all primes p and the usual absolute value, denoted $|r|_{0}$ . This follows from simply taking the prime factorization: each prime power factor $p^{k}$ contributes its reciprocal to its p-adic absolute value, and then the usual Archimedean absolute value cancels all of them.

By Ostrowski's theorem, the usual and p-adic absolute values occurring in the formula are all the absolute values on the rational numbers up to equivalence. An analogous product formula can be used to axiomatically define global fields, of which the rational numbers are the simplest example.

### Metric and completion

A metric space can be formed on the set $\mathbb {Q}$ with a (non-Archimedean, translation-invariant) metric

$d\colon \mathbb {Q} \times \mathbb {Q} \to \mathbb {R} _{\geq 0}$

defined by

$d(r,s)=|r-s|_{p}.$

The completion of $\mathbb {Q}$ with respect to this metric leads to the set $\mathbb {Q} _{p}$ of p-adic numbers. Like the rationals, they form a field, and the p-adic valuation and absolute value can be extended to $\mathbb {Q} _{p}$ , making it a complete valued field.
