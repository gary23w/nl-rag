---
title: "Computational indistinguishability"
source: https://en.wikipedia.org/wiki/Computational_indistinguishability
domain: one-way-functions
license: CC-BY-SA-4.0
tags: one way function, trapdoor function, hard core predicate, computational indistinguishability
fetched: 2026-07-02
---

# Computational indistinguishability

In computational complexity and cryptography, two families of distributions are **computationally indistinguishable** if no efficient algorithm can tell the difference between them except with negligible probability.

## Formal definition

Let $\scriptstyle \{D_{n}\}_{n\in \mathbb {N} }$ and $\scriptstyle \{E_{n}\}_{n\in \mathbb {N} }$ be two distribution ensembles indexed by a security parameter *n* (which usually refers to the length of the input); we say they are computationally indistinguishable if for any non-uniform probabilistic polynomial time algorithm *A*, the following quantity is a negligible function in *n*:

$\delta (n)=\left|\Pr _{x\gets D_{n}}[A(x)=1]-\Pr _{x\gets E_{n}}[A(x)=1]\right|.$

denoted $D_{n}\approx E_{n}$ . In other words, every efficient algorithm *A'*s behavior does not significantly change when given samples according to *D**n* or *E**n* in the limit as $n\to \infty$ . Another interpretation of computational indistinguishability is that polynomial-time algorithms actively trying to distinguish between the two ensembles cannot do so: that any such algorithm will only perform negligibly better than if one were to just guess.

Implicit in the definition is the condition that the algorithm, A , must decide based on a single sample from one of the distributions. One might conceive of a situation in which the algorithm trying to distinguish between two distributions, could access as many samples as it needed. Hence two ensembles that cannot be distinguished by polynomial-time algorithms looking at multiple samples are deemed **indistinguishable by polynomial-time sampling**. If the polynomial-time algorithm can generate samples in polynomial time, or has access to a random oracle that generates samples for it, then indistinguishability by polynomial-time sampling is equivalent to computational indistinguishability.
