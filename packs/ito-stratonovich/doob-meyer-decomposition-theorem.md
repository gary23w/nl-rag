---
title: "Doob–Meyer decomposition theorem"
source: https://en.wikipedia.org/wiki/Doob%E2%80%93Meyer_decomposition_theorem
domain: ito-stratonovich
license: CC-BY-SA-4.0
tags: ito calculus, stratonovich integral, quadratic variation, wiener process
fetched: 2026-07-02
---

# Doob–Meyer decomposition theorem

The **Doob–Meyer decomposition theorem** is a theorem in stochastic calculus stating the conditions under which a submartingale may be decomposed in a unique way as the sum of a martingale and an increasing predictable process. It is named for Joseph L. Doob and Paul-André Meyer.

## History

In 1953, Doob published the Doob decomposition theorem which gives a unique decomposition for certain discrete time martingales. He conjectured a continuous time version of the theorem and in two publications in 1962 and 1963 Paul-André Meyer proved such a theorem, which became known as the Doob-Meyer decomposition. In honor of Doob, Meyer used the term "class D" to refer to the class of supermartingales for which his unique decomposition theorem applied.

## Class D supermartingales

A càdlàg supermartingale Z is of Class D if $Z_{0}=0$ and the collection

$\{Z_{T}\mid T{\text{ a finite-valued stopping time}}\}$

is uniformly integrable.

## Theorem

Let $(\Omega ,{\mathcal {F}},({\mathcal {F}}_{t})_{t\geq 0},\mathbb {P} )$ be a filtered probability space satisfying the usual conditions (i.e. the filtration is right-continuous and complete; see Filtration (probability theory)). If $X=(X_{t})_{t\geq 0}$ is a right-continuous submartingale of class D, then there exist unique adapted processes M and A such that

$X_{t}=M_{t}+A_{t},\qquad t\geq 0,$

where

- M is a uniformly integrable martingale,
- A is a predictable, right-continuous, increasing process with $A_{0}=0$ .

The decomposition $(M,A)$ is unique up to indistinguishability.

*Remark*. For a class D supermartingale, the process A is integrable and of finite variation on bounded intervals.
