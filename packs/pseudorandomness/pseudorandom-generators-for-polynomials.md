---
title: "Pseudorandom generators for polynomials"
source: https://en.wikipedia.org/wiki/Pseudorandom_generators_for_polynomials
domain: pseudorandomness
license: CC-BY-SA-4.0
tags: pseudorandomness theory, pseudorandom generator, randomness extractor, expander construction
fetched: 2026-07-02
---

# Pseudorandom generators for polynomials

In theoretical computer science, a **pseudorandom generator for low-degree polynomials** is an efficient procedure that maps a short truly random seed to a longer pseudorandom string in such a way that low-degree polynomials cannot distinguish the output distribution of the generator from the truly random distribution. That is, evaluating any low-degree polynomial at a point determined by the pseudorandom string is statistically close to evaluating the same polynomial at a point that is chosen uniformly at random.

Pseudorandom generators for low-degree polynomials are a particular instance of pseudorandom generators for statistical tests, where the statistical tests considered are evaluations of low-degree polynomials.

## Definition

A pseudorandom generator $G:\mathbb {F} ^{\ell }\rightarrow \mathbb {F} ^{n}$ for polynomials of degree d over a finite field $\mathbb {F}$ is an efficient procedure that maps a sequence of $\ell$ field elements to a sequence of n field elements such that any n -variate polynomial over $\mathbb {F}$ of degree d is fooled by the output distribution of G . In other words, for every such polynomial $p(x_{1},\dots ,x_{n})$ , the statistical distance between the distributions $p(U_{n})$ and $p(G(U_{\ell }))$ is at most a small $\epsilon$ , where $U_{k}$ is the uniform distribution over $\mathbb {F} ^{k}$ .

## Construction

The case $d=1$ corresponds to pseudorandom generators for linear functions and is solved by small-bias generators. For example, the construction of Naor & Naor (1990) achieves a seed length of $\ell =\log n+O(\log(\epsilon ^{-1}))$ , which is optimal up to constant factors.

Bogdanov & Viola (2007) conjectured that the sum of small-bias generators fools low-degree polynomials and were able to prove this under the Gowers inverse conjecture. Lovett (2009) proved unconditionally that the sum of $2^{d}$ small-bias spaces fools polynomials of degree d . Viola (2008) proves that, in fact, taking the sum of only d small-bias generators is sufficient to fool polynomials of degree d . The analysis of Viola (2008) gives a seed length of $\ell =d\cdot \log n+O(2^{d}\cdot \log(\epsilon ^{-1}))$ .
