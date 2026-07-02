---
title: "Toda's theorem"
source: https://en.wikipedia.org/wiki/Toda's_theorem
domain: counting-complexity
license: CC-BY-SA-4.0
tags: counting complexity, permanent computation, toda theorem, counting problem
fetched: 2026-07-02
---

# Toda's theorem

**Toda's theorem** is a result in computational complexity theory that was proven by Seinosuke Toda in his paper "PP is as Hard as the Polynomial-Time Hierarchy" and was given the 1998 Gödel Prize.

## Statement

The theorem states that the entire polynomial hierarchy PH is contained in PPP; this implies a closely related statement, that PH is contained in P#P.

## Definitions

#P is the class of problems of the form of exactly counting the number of solutions to a polynomially-verifiable question (that is, to a question in NP), while loosely speaking, PP is the class of problems for which there is a polynomial-time algorithm that gives a correct answer more than half the time. The class P#P consists of all problems that can be solved in polynomial time if you have access to instantaneous answers to any counting problem in #P (polynomial time relative to a #P oracle). Thus Toda's theorem implies that for any problem in the polynomial hierarchy there is a deterministic polynomial-time Turing reduction to a counting problem.

An analogous result in the complexity theory over the reals (in the sense of Blum–Shub–Smale real Turing machines) was proved by Saugata Basu and Thierry Zell in 2010 and a complex analogue of Toda's theorem was proved by Saugata Basu in 2011.

## Proof

The proof is broken into two parts.

- First, it is established that

$\Sigma ^{P}\cdot {\mathsf {BP}}\cdot \oplus {\mathsf {P}}\subseteq {\mathsf {BP}}\cdot \oplus {\mathsf {P}}$

The proof uses a variation of

Valiant–Vazirani theorem

. Because

${\mathsf {BP}}\cdot \oplus {\mathsf {P}}$

contains

${\mathsf {P}}$

and is closed under complement, it follows by induction that

${\mathsf {PH}}\subseteq {\mathsf {BP}}\cdot \oplus {\mathsf {P}}$

.

- Second, it is established that

${\mathsf {BP}}\cdot \oplus {\mathsf {P}}\subseteq {\mathsf {P}}^{\#P}$

Together, the two parts imply

${\mathsf {PH}}\subseteq {\mathsf {BP}}\cdot \oplus {\mathsf {P}}\subseteq {\mathsf {P}}\cdot \oplus {\mathsf {P}}\subseteq {\mathsf {P}}^{\#P}$

See Fortnow 2009 for details. A more leisurely proof is in the textbook Arora & Barak 2009.
