---
title: "Fiat–Shamir heuristic"
source: https://en.wikipedia.org/wiki/Fiat%E2%80%93Shamir_heuristic
domain: zero-knowledge-proofs-theory
license: CC-BY-SA-4.0
tags: zero knowledge proof, soundness property, completeness property, sigma protocol
fetched: 2026-07-02
---

# Fiat–Shamir heuristic

In cryptography, the **Fiat–Shamir heuristic**, or **Fiat–Shamir transformation**, is a technique for taking an interactive proof of knowledge and creating a digital signature based on it. This way, some fact (for example, knowledge of a certain secret number) can be publicly proven without revealing underlying information. The technique is due to Amos Fiat and Adi Shamir (1986). For the method to work, the original interactive proof must have the property of being public-coin, i.e. verifier's random coins are made public throughout the proof protocol.

## Overview

The heuristic was originally presented without a proof of security; later, Pointcheval and Stern proved its security against chosen message attacks in the *random oracle model*, that is, assuming random oracles exist. This result was generalized to the quantum-accessible random oracle (QROM) by Don, Fehr, Majenz and Schaffner, and concurrently by Liu and Zhandry. In the case that random oracles do not exist, the Fiat–Shamir heuristic has been proven insecure by Shafi Goldwasser and Yael Tauman Kalai. The Fiat–Shamir heuristic thus demonstrates a major application of random oracles. More generally, the Fiat–Shamir heuristic may also be viewed as converting a public-coin interactive proof of knowledge into a non-interactive proof of knowledge. If the interactive proof is used as an identification tool, then the non-interactive version can be used directly as a digital signature by using the message as part of the input to the random oracle.

## Example

For the algorithm specified below, readers should be familiar with the multiplicative groups $\mathbb {Z} _{q}^{*}$ , where *q* is a prime number, and Euler's totient theorem on the Euler's totient function *φ*.

Here is an **interactive** proof of knowledge of a discrete logarithm in $\mathbb {Z} _{q}^{*}$ , based on Schnorr signature. The public values are $y\in \mathbb {Z} _{q}^{*}$ and a generator *g* of $\mathbb {Z} _{q}^{*}$ , while the secret value is the discrete logarithm of *y* to the base *g*.

1. Peggy wants to prove to Victor, the verifier, that she knows x satisfying $y\equiv g^{x}$ without revealing x .
2. Peggy picks a random $v\in \mathbb {Z} _{q}^{*}$ , computes $t=g^{v}$ and sends t to Victor.
3. Victor picks a random $c\in \mathbb {Z} _{q}^{*}$ and sends it to Peggy.
4. Peggy computes $r=v-cx{\bmod {\varphi }}(q)$ and returns r to Victor.
5. Victor checks whether $t\equiv g^{r}y^{c}$ . This holds because $g^{r}y^{c}\equiv g^{v-cx}g^{xc}\equiv g^{v}\equiv t$ and $g^{\varphi (q)}\equiv 1$ .

Fiat–Shamir heuristic allows to replace the interactive step 3 with a **non-interactive** random oracle access. In practice, we can use a cryptographic hash function instead.

1. Peggy wants to prove that she knows x such that $y\equiv g^{x}$ without revealing x .
2. Peggy picks a random $v\in \mathbb {Z} _{q}^{*}$ and computes $t=g^{v}$ .
3. Peggy computes $c=H(g,y,t)$ , where H is a cryptographic hash function.
4. Peggy computes $r=v-cx{\bmod {\varphi }}(q)$ . The resulting proof is the pair $(t,r)$ .
5. Anyone can use this proof to calculate c and check whether $t\equiv g^{r}y^{c}$ .

If the hash value used below does not depend on the (public) value of *y*, the security of the scheme is weakened, as a malicious prover can then select a certain value *t* so that the product *cx* is known.

## Extension of this method

As long as a fixed random generator can be constructed with the data known to both parties, then any interactive protocol can be transformed into a non-interactive one.
