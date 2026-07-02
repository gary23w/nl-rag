---
title: "Functional encryption"
source: https://en.wikipedia.org/wiki/Functional_encryption
domain: homomorphic-encryption-applied
license: CC-BY-SA-4.0
tags: homomorphic encryption, fully homomorphic encryption, paillier cryptosystem, learning with errors, lattice based cryptography
fetched: 2026-07-02
---

# Functional encryption

**Functional encryption** (**FE**) is a generalization of public-key encryption in which possessing a secret key allows one to learn a function of what the ciphertext is encrypting.

## Formal definition

More precisely, a functional encryption scheme for a given functionality f consists of the following four algorithms:

- $({\text{pk}},{\text{msk}})\leftarrow {\textsf {Setup}}(1^{\lambda })$ : creates a public key ${\text{pk}}$ and a master secret key ${\text{msk}}$ .
- ${\text{sk}}\leftarrow {\textsf {Keygen}}({\text{msk}},f)$ : uses the master secret key to generate a new secret key ${\text{sk}}$ for the function f .
- $c\leftarrow {\textsf {Enc}}({\text{pk}},x)$ : uses the public key to encrypt a message x .
- $y\leftarrow {\textsf {Dec}}({\text{sk}},c)$ : uses secret key to calculate $y=f(x)$ where x is the value that c encrypts.

The security of FE requires that any information an adversary learns from an encryption of x is revealed by $f(x)$ . Formally, this is defined by simulation.

## Applications

Functional encryption generalizes several existing primitives including Identity-based encryption (IBE) and attribute-based encryption (ABE). In the IBE case, define $F(k,x)$ to be equal to x when k corresponds to an identity that is allowed to decrypt, and $\perp$ otherwise. Similarly, in the ABE case, define $F(k,x)=x$ when k encodes attributes with permission to decrypt and $\perp$ otherwise.

## History

Functional encryption was proposed by Amit Sahai and Brent Waters in 2005 and formalized by Dan Boneh, Amit Sahai and Brent Waters in 2010. Until recently, however, most instantiations of Functional Encryption supported only limited function classes such as boolean formulae. In 2012, several researchers developed Functional Encryption schemes that support arbitrary functions.
