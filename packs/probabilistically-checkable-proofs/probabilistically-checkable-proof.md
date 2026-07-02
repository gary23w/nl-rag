---
title: "Probabilistically checkable proof"
source: https://en.wikipedia.org/wiki/Probabilistically_checkable_proof
domain: probabilistically-checkable-proofs
license: CC-BY-SA-4.0
tags: probabilistically checkable proof, pcp theorem, proof verification, hardness of approximation
fetched: 2026-07-02
---

# Probabilistically checkable proof

In computational complexity theory, a **probabilistically checkable proof** (**PCP**) is a type of proof that can be checked by a randomized algorithm using a bounded amount of randomness and reading a bounded number of bits of the proof. The algorithm is then required to accept correct proofs and reject incorrect proofs with very high probability. A standard proof (or certificate), as used in the verifier-based definition of the complexity class NP, also satisfies these requirements, since the checking procedure deterministically reads the whole proof, always accepts correct proofs and rejects incorrect proofs. However, what makes them interesting is the existence of probabilistically checkable proofs that can be checked by reading only a few bits of the proof using randomness in an essential way.

Probabilistically checkable proofs give rise to many complexity classes depending on the number of queries required and the amount of randomness used. The class PCP[*r*(*n*), *q*(*n*)] refers to the set of decision problems that have probabilistically checkable proofs that can be verified in polynomial time using at most *r*(*n*) random bits and by reading at most *q*(*n*) bits of the proof. Unless specified otherwise, correct proofs should always be accepted, and incorrect proofs should be rejected with probability greater than 1/2. The PCP theorem, a major result in computational complexity theory, states that PCP[*O*(log *n*), *O*(1)] = NP.

## Definition

Given a decision problem *L* (a language over an alphabet Σ), a **probabilistically checkable proof system** for *L* with completeness *c*(*n*) and soundness *s*(*n*), where 0 ≤ *s*(*n*) ≤ *c*(*n*) ≤ 1, consists of a prover and a verifier. Given a claimed solution *x* of length *n*, which might be false, the prover produces a proof *π* which states *x* solves L (*x* ∈ *L*, the proof is a string in Σ∗). And the verifier is a randomized oracle Turing Machine *V* (the *verifier*) that checks the proof *π* for the statement that *x* solves L (or *x* ∈ *L*) and decides whether to accept the statement. The system has the following properties:

- **Completeness**: For any *x* ∈ *L*, given the proof *π* produced by the prover of the system, the verifier accepts the statement with probability at least *c*(*n*),
- **Soundness**: For any *x* ∉ *L*, then for any proof *π*, the verifier mistakenly accepts the statement with probability at most *s*(*n*).

For the computational complexity of the verifier, the verifier is polynomial time, and we have the *randomness complexity* *r*(*n*) to measure the maximum number of random bits that *V* uses over all *x* of length *n* and the *query complexity* *q*(*n*) of the verifier is the maximum number of queries that *V* makes to π over all *x* of length *n*.

In the above definition, the length of proof is not mentioned since usually it includes the alphabet set and all the witnesses. For the prover, we do not care how it arrives at the solution to the problem; we care only about the proof it gives of the solution's membership in the language.

The verifier is said to be *non-adaptive* if it makes all its queries before it receives any of the answers to previous queries.

The complexity class PCP*c*(*n*), *s*(*n*)[*r*(*n*), *q*(*n*)] is the class of all decision problems having probabilistically checkable proof systems over binary alphabet of completeness *c*(*n*) and soundness *s*(*n*), where the verifier is non-adaptive, runs in polynomial time, and it has randomness complexity *r*(*n*) and query complexity *q*(*n*).

The shorthand notation PCP[*r*(*n*), *q*(*n*)] is sometimes used for PCP1, 1/2[*r*(*n*), *q*(*n*)]. The complexity class **PCP** is defined as PCP1, 1/2[*O*(log *n*), *O*(1)].

## History and significance

The theory of probabilistically checkable proofs studies the power of probabilistically checkable proof systems under various restrictions of the parameters (completeness, soundness, randomness complexity, query complexity, and alphabet size). It has applications to computational complexity (in particular hardness of approximation) and cryptography.

The definition of a probabilistically checkable proof was explicitly introduced by Arora and Safra in 1992, although their properties were studied earlier. In 1990 Babai, Fortnow, and Lund proved that **PCP**[poly(*n*), poly(*n*)] = **NEXP**, providing the first nontrivial equivalence between standard proofs (**NEXP**) and probabilistically checkable proofs. The PCP theorem proved in 1992 states that PCP[*O*(log *n*),*O*(1)] = NP.

The theory of hardness of approximation requires a detailed understanding of the role of completeness, soundness, alphabet size, and query complexity in probabilistically checkable proofs.

## Properties

From computational complexity point of view, for extreme settings of the parameters, the definition of probabilistically checkable proofs is easily seen to be equivalent to standard complexity classes. For example, we have the following for different setting of PCP[*r*(*n*), *q*(*n*)]:

- PCP[0, 0] = P (P is defined to have no randomness and no access to a proof.)
- PCP[*O*(log *n*), 0] = P (A logarithmic number of random bits doesn't help a polynomial time Turing machine, since it could try all possibly random strings of logarithmic length in polynomial time.)
- PCP[O(1),*O*(log *n*)] = P (Without randomness, the proof can be thought of as a fixed logarithmic sized string. A polynomial time machine could try all possible logarithmic sized proofs and constant-length random strings in polynomial time.)
- PCP[poly(*n*), 0] = coRP (By definition of coRP.)
- PCP[0, poly(*n*)] = NP (By the verifier-based definition of NP.)

The PCP theorem and MIP = NEXP can be characterized as follows:

- PCP [*O*(log *n*),*O*(1)] = NP (the PCP theorem)
- PCP [poly(*n*),*O*(1)] = PCP [poly(*n*),poly(*n*)] = NEXP (MIP = NEXP).

| ⁠ ${\mathsf {PCP}}[r(n),q(n)]$ ⁠ | 0 | ⁠ $O(1)$ ⁠ | ⁠ $O(\log n)$ ⁠ | ⁠ $\operatorname {poly} (n)$ ⁠ |
|---|---|---|---|---|
| 0 | P | P | P | NP |
| ⁠ $O(1)$ ⁠ | P | P | P | NP |
| ⁠ $O(\log n)$ ⁠ | P | NP | NP | NP |
| ⁠ $\operatorname {poly} (n)$ ⁠ | coRP | MIP = NEXP | NEXP | NEXP |

It is also known that PCP[*r*(*n*), *q*(*n*)] ⊆ NTIME(poly(*n*,2*O*(*r*(*n*))*q*(*n*))). In particular, PCP[O(log *n*), poly(*n*)] = NP. On the other hand, if NP ⊆ PCP [*o*(log *n*),*o*(log *n*)] then P = NP.

## Linear PCP

A Linear PCP is a PCP in which the proof is a vector of elements of a finite field $\pi \in \mathbb {F} ^{n}$ , and such that the PCP oracle is only allowed to do linear operations on the proof. Namely, the response from the oracle to a verifier query $q\in \mathbb {F} ^{n}$ is a linear function $f(q,\pi )$ . Linear PCPs have important applications in proof systems that can be compiled into SNARKs.
