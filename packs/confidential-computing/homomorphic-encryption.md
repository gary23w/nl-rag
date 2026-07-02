---
title: "Homomorphic encryption"
source: https://en.wikipedia.org/wiki/Homomorphic_encryption
domain: confidential-computing
license: CC-BY-SA-4.0
tags: confidential computing, data in use protection, trusted execution environment, encrypted memory enclave, hardware attestation
fetched: 2026-07-02
---

# Homomorphic encryption

**Homomorphic encryption** is a form of encryption that allows computations to be performed on encrypted data without first having to decrypt it. The resulting computations are left in an encrypted form which, when decrypted, result in an output that is identical to that of the operations performed on the unencrypted data. Homomorphic encryption can be used for privacy-preserving outsourced storage and computation. This allows data to be encrypted and outsourced to commercial cloud environments for processing, all while encrypted.

As an example of a practical application of homomorphic encryption: encrypted photographs can be scanned for points of interest, without revealing the contents of a photo. However, observation of side-channels can see a photograph being sent to a point-of-interest lookup service, revealing the fact that photographs were taken.

Thus, homomorphic encryption eliminates the need for processing data in the clear, thereby preventing attacks that would enable an attacker to access that data while it is being processed, using privilege escalation.

For sensitive data, such as healthcare information, homomorphic encryption can be used to enable new services by removing privacy barriers inhibiting data sharing or increasing security to existing services. For example, predictive analytics in healthcare can be hard to apply via a third-party service provider due to medical data privacy concerns. But if the predictive-analytics service provider could operate on encrypted data instead, without having the decryption keys, these privacy concerns are diminished. Moreover, even if the service provider's system is compromised, the data would remain secure.

## Characteristics

Homomorphic encryption is a form of encryption with an additional evaluation capability for computing over encrypted data without access to the secret key. The result of such a computation remains encrypted. Homomorphic encryption can be viewed as an extension of public-key cryptography, because ciphertexts can be manipulated algebraically to produce an encrypted result corresponding to operations on the underlying plaintexts. *Homomorphic* refers to homomorphism in algebra: the encryption and decryption functions can be thought of as homomorphisms between plaintext and ciphertext spaces.

Homomorphic encryption includes multiple types of encryption schemes that can perform different classes of computations over encrypted data. The computations are represented as either Boolean or arithmetic circuits. Some common types of homomorphic encryption are *partially* homomorphic, *somewhat* homomorphic, *leveled* *fully* homomorphic, and *fully* homomorphic encryption:

- *Partially homomorphic encryption* encompasses schemes that support the evaluation of circuits consisting of only one type of gate, e.g., addition or multiplication.
- *Somewhat homomorphic encryption* schemes can evaluate two types of gates, but only for a subset of circuits.
- *Leveled fully homomorphic encryption* supports the evaluation of arbitrary circuits composed of multiple types of gates of bounded (pre-determined) depth.
- *Fully homomorphic encryption* (FHE) allows the evaluation of arbitrary circuits composed of multiple types of gates of unbounded depth and is the strongest notion of homomorphic encryption.

For the majority of homomorphic encryption schemes, the multiplicative depth of circuits is the main practical limitation in performing computations over encrypted data. Homomorphic encryption schemes are inherently malleable. In terms of malleability, homomorphic encryption schemes have weaker security properties than non-homomorphic schemes.

A cryptosystem that supports *arbitrary computation* on ciphertexts is known as fully homomorphic encryption (FHE). Such a scheme enables the construction of programs for any desirable functionality, which can be run on encrypted inputs to produce an encryption of the result. Since such a program need never decrypt its inputs, it can be run by an untrusted party without revealing its inputs and internal state. Fully homomorphic cryptosystems have great practical implications in the outsourcing of private computations, for instance, in the context of cloud computing.

## History

Homomorphic encryption schemes have been developed using different approaches. Specifically, fully homomorphic encryption schemes are often grouped into generations corresponding to the underlying approach.

### Predecessors

The problem of constructing a fully homomorphic encryption scheme was first proposed in 1978, within a year of publishing of the RSA scheme. For more than 30 years, it was unclear whether a solution existed. During that period, partial results included the following schemes:

- RSA cryptosystem (unbounded number of modular multiplications)
- ElGamal cryptosystem (unbounded number of modular multiplications)
- Goldwasser–Micali cryptosystem (unbounded number of exclusive or operations)
- Benaloh cryptosystem (unbounded number of modular additions)
- Paillier cryptosystem (unbounded number of modular additions)
- Sander-Young-Yung system (after more than 20 years solved the problem for logarithmic depth circuits)
- Boneh–Goh–Nissim cryptosystem (unlimited number of addition operations but at most one multiplication)
- Ishai-Paskin cryptosystem (polynomial-size branching programs)

### First generation

Craig Gentry, using lattice-based cryptography, described the first plausible construction for a fully homomorphic encryption scheme in 2009. Gentry's scheme supports both addition and multiplication operations on ciphertexts, from which it is possible to construct circuits for performing arbitrary computation. The construction starts from a *somewhat homomorphic* encryption scheme, which is limited to evaluating low-degree polynomials over encrypted data; it is limited because each ciphertext is noisy in some sense, and this noise grows as one adds and multiplies ciphertexts, until ultimately the noise makes the resulting ciphertext indecipherable.

Gentry then shows how to slightly modify this scheme to make it *bootstrappable*, i.e., capable of evaluating its own decryption circuit and then at least one more operation. Finally, he shows that any bootstrappable somewhat homomorphic encryption scheme can be converted into a fully homomorphic encryption through a recursive self-embedding. For Gentry's "noisy" scheme, the bootstrapping procedure effectively "refreshes" the ciphertext by applying to it the decryption procedure homomorphically, thereby obtaining a new ciphertext that encrypts the same value as before but has lower noise. By "refreshing" the ciphertext periodically whenever the noise grows too large, it is possible to compute an arbitrary number of additions and multiplications without increasing the noise too much.

Gentry based the security of his scheme on the assumed hardness of two problems: certain worst-case problems over ideal lattices, and the sparse (or low-weight) subset sum problem. Gentry's Ph.D. thesis provides additional details. The Gentry-Halevi implementation of Gentry's original cryptosystem reported a timing of about 30 minutes per basic bit operation. Extensive design and implementation work in subsequent years have improved upon these early implementations by many orders of magnitude runtime performance.

In 2010, Marten van Dijk, Craig Gentry, Shai Halevi and Vinod Vaikuntanathan presented a second fully homomorphic encryption scheme, which uses many of the tools of Gentry's construction, but which does not require ideal lattices. Instead, they show that the somewhat homomorphic component of Gentry's ideal lattice-based scheme can be replaced with a very simple somewhat homomorphic scheme that uses integers. The scheme is therefore conceptually simpler than Gentry's ideal lattice scheme, but has similar properties with regards to homomorphic operations and efficiency. The somewhat homomorphic component in the work of Van Dijk et al. is similar to an encryption scheme proposed by Levieil and Naccache in 2008, and also to one that was proposed by Bram Cohen in 1998.

Cohen's method is not even additively homomorphic, however. The Levieil–Naccache scheme supports only additions, but it can be modified to also support a small number of multiplications. Many refinements and optimizations of the scheme of Van Dijk et al. were proposed in a sequence of works by Jean-Sébastien Coron, Tancrède Lepoint, Avradip Mandal, David Naccache, and Mehdi Tibouchi. Some of these works included also implementations of the resulting schemes.

### Second generation

The homomorphic cryptosystems of this generation are derived from techniques that were developed starting in 2011–2012 by Zvika Brakerski, Craig Gentry, Vinod Vaikuntanathan, and others. These innovations led to the development of much more efficient somewhat and fully homomorphic cryptosystems. These include:

- The Brakerski-Gentry-Vaikuntanathan (BGV, 2011) scheme, building on techniques of Brakerski-Vaikuntanathan;
- The NTRU-based scheme by Lopez-Alt, Tromer, and Vaikuntanathan (LTV, 2012);
- The Brakerski/Fan-Vercauteren (BFV, 2012) scheme, building on Brakerski's *scale-invariant* cryptosystem;
- The NTRU-based scheme by Bos, Lauter, Loftus, and Naehrig (BLLN, 2013), building on LTV and Brakerski's scale-invariant cryptosystem;

The security of most of these schemes is based on the hardness of the (Ring) Learning With Errors (RLWE) problem, except for the LTV and BLLN schemes that rely on an *overstretched* variant of the NTRU computational problem. This NTRU variant was subsequently shown vulnerable to subfield lattice attacks, which is why these two schemes are no longer used in practice.

All the second-generation cryptosystems still follow the basic blueprint of Gentry's original construction, namely they first construct a somewhat homomorphic cryptosystem and then convert it to a fully homomorphic cryptosystem using bootstrapping.

A distinguishing characteristic of the second-generation cryptosystems is that they all feature a much slower growth of the noise during the homomorphic computations. Additional optimizations by Craig Gentry, Shai Halevi, and Nigel Smart resulted in cryptosystems with nearly optimal asymptotic complexity: Performing T operations on data encrypted with security parameter k has complexity of only $T\cdot \mathrm {polylog} (k)$ . These optimizations build on the Smart-Vercauteren techniques that enable packing of many plaintext values in a single ciphertext and operating on all these plaintext values in a SIMD fashion. Many of the advances in these second-generation cryptosystems were also ported to the cryptosystem over the integers.

Another distinguishing feature of second-generation schemes is that they are efficient enough for many applications even without invoking bootstrapping, instead operating in the leveled FHE mode.

### Third generation

In 2013, Craig Gentry, Amit Sahai, and Brent Waters (GSW) proposed a new technique for building FHE schemes that avoids an expensive "relinearization" step in homomorphic multiplication. Zvika Brakerski and Vinod Vaikuntanathan observed that for certain types of circuits, the GSW cryptosystem features an even slower growth rate of noise, and hence better efficiency and stronger security. Jacob Alperin-Sheriff and Chris Peikert then described a very efficient bootstrapping technique based on this observation.

These techniques were further improved to develop efficient ring variants of the GSW cryptosystem: FHEW (2014) and TFHE (2016). The FHEW scheme was the first to show that by refreshing the ciphertexts after every single operation, it is possible to reduce the bootstrapping time to a fraction of a second. FHEW introduced a new method to compute Boolean gates on encrypted data that greatly simplifies bootstrapping and implemented a variant of the bootstrapping procedure. The efficiency of FHEW was further improved by the TFHE scheme, which implements a ring variant of the bootstrapping procedure using a method similar to the one in FHEW.

### Fourth generation

In 2016, Jung Hee Cheon, Andrey Kim, Miran Kim, and Yongsoo Song (CKKS) proposed an approximate homomorphic encryption scheme that supports a special kind of fixed-point arithmetic that is commonly referred to as block floating point arithmetic. The CKKS scheme includes an efficient rescaling operation that scales down an encrypted message after a multiplication. For comparison, such rescaling requires bootstrapping in the BGV and BFV schemes. The rescaling operation makes CKKS scheme the most efficient method for evaluating polynomial approximations, and is the preferred approach for implementing privacy-preserving machine learning applications. The scheme introduces several approximation errors, both nondeterministic and deterministic, that require special handling in practice.

A 2020 article by Baiyu Li and Daniele Micciancio discusses passive attacks against CKKS, suggesting that the standard IND-CPA definition may not be sufficient in scenarios where decryption results are shared. The authors apply the attack to four modern homomorphic encryption libraries (HEAAN, SEAL, HElib and PALISADE) and report that it is possible to recover the secret key from decryption results in several parameter configurations. The authors also propose mitigation strategies for these attacks, and include a Responsible Disclosure in the paper suggesting that the homomorphic encryption libraries already implemented mitigations for the attacks before the article became publicly available. Further information on the mitigation strategies implemented in the homomorphic encryption libraries has also been published.

## Partially homomorphic cryptosystems

In the following examples, the notation ${\mathcal {E}}(x)$ is used to denote the encryption of the message x .

**Unpadded RSA**

If the

RSA

public key has modulus

n

and encryption exponent

e

, then the encryption of a message

m

is given by

${\mathcal {E}}(m)=m^{e}\;{\bmod {\;}}n$

. The homomorphic property is then

${\begin{aligned}{\mathcal {E}}(m_{1})\cdot {\mathcal {E}}(m_{2})&=m_{1}^{e}m_{2}^{e}\;{\bmod {\;}}n\\[6pt]&=(m_{1}m_{2})^{e}\;{\bmod {\;}}n\\[6pt]&={\mathcal {E}}(m_{1}\cdot m_{2})\end{aligned}}$

**ElGamal**

In the

ElGamal cryptosystem

, in a cyclic group

G

of order

q

with generator

g

, if the public key is

$(G,q,g,h)$

, where

$h=g^{x}$

, and

x

is the secret key, then the encryption of a message

m

is

${\mathcal {E}}(m)=(g^{r},m\cdot h^{r})$

, for some random

$r\in \{0,\ldots ,q-1\}$

. The homomorphic property is then

${\begin{aligned}{\mathcal {E}}(m_{1})\cdot {\mathcal {E}}(m_{2})&=(g^{r_{1}},m_{1}\cdot h^{r_{1}})(g^{r_{2}},m_{2}\cdot h^{r_{2}})\\[6pt]&=(g^{r_{1}+r_{2}},(m_{1}\cdot m_{2})h^{r_{1}+r_{2}})\\[6pt]&={\mathcal {E}}(m_{1}\cdot m_{2}).\end{aligned}}$

**Goldwasser–Micali**

In the

Goldwasser–Micali cryptosystem

, if the public key is the modulus

n

and quadratic non-residue

x

, then the encryption of a bit

b

is

${\mathcal {E}}(b)=x^{b}r^{2}\;{\bmod {\;}}n$

, for some random

$r\in \{0,\ldots ,n-1\}$

. The homomorphic property is then

${\begin{aligned}{\mathcal {E}}(b_{1})\cdot {\mathcal {E}}(b_{2})&=x^{b_{1}}r_{1}^{2}x^{b_{2}}r_{2}^{2}\;{\bmod {\;}}n\\[6pt]&=x^{b_{1}+b_{2}}(r_{1}r_{2})^{2}\;{\bmod {\;}}n\\[6pt]&={\mathcal {E}}(b_{1}\oplus b_{2}).\end{aligned}}$

where $\oplus$ denotes addition modulo 2, (i.e., exclusive-or).

**Benaloh**

In the

Benaloh cryptosystem

, if the public key is the modulus

n

and the base

g

with a blocksize of

c

, then the encryption of a message

m

is

${\mathcal {E}}(m)=g^{m}r^{c}\;{\bmod {\;}}n$

, for some random

$r\in \{0,\ldots ,n-1\}$

. The homomorphic property is then

${\begin{aligned}{\mathcal {E}}(m_{1})\cdot {\mathcal {E}}(m_{2})&=(g^{m_{1}}r_{1}^{c})(g^{m_{2}}r_{2}^{c})\;{\bmod {\;}}n\\[6pt]&=g^{m_{1}+m_{2}}(r_{1}r_{2})^{c}\;{\bmod {\;}}n\\[6pt]&={\mathcal {E}}(m_{1}+m_{2}\;{\bmod {\;}}c).\end{aligned}}$

**Paillier**

In the

Paillier cryptosystem

, if the public key is the modulus

n

and the base

g

, then the encryption of a message

m

is

${\mathcal {E}}(m)=g^{m}r^{n}\;{\bmod {\;}}n^{2}$

, for some random

$r\in \{0,\ldots ,n-1\}$

. The homomorphic property is then

${\begin{aligned}{\mathcal {E}}(m_{1})\cdot {\mathcal {E}}(m_{2})&=(g^{m_{1}}r_{1}^{n})(g^{m_{2}}r_{2}^{n})\;{\bmod {\;}}n^{2}\\[6pt]&=g^{m_{1}+m_{2}}(r_{1}r_{2})^{n}\;{\bmod {\;}}n^{2}\\[6pt]&={\mathcal {E}}(m_{1}+m_{2}).\end{aligned}}$

**Other partially homomorphic cryptosystems**

- Okamoto–Uchiyama cryptosystem
- Naccache–Stern cryptosystem
- Damgård–Jurik cryptosystem
- Sander–Young–Yung encryption scheme
- Boneh–Goh–Nissim cryptosystem
- Ishai–Paskin cryptosystem
- Joye-Libert cryptosystem
- Castagnos–Laguillaumie cryptosystem

## Implementations

There are several open-source implementations of partially, somewhat and fully homomorphic encryption schemes. Second-generation and fourth-generation FHE scheme implementations typically operate in the leveled FHE mode (though bootstrapping is still available in some libraries) and support efficient SIMD-like packing of data; they are typically used to compute on encrypted integers or real/complex numbers. Third-generation FHE scheme implementations often bootstrap after each operation but have limited support for packing; they were initially used to compute Boolean circuits over encrypted bits, but have been extended to support integer arithmetics and univariate function evaluation. The choice of using a second-generation vs. third-generation vs fourth-generation scheme depends on the input data types and the desired computation.

PHE & SWHE libraries

Library

Language

RSA

ElGamal

Exponential ElGamal

Elliptic Curve ElGamal

Paillier

Damgård–Jurik

Okamoto–Uchiyama

Benaloh

Naccache–Stern

Goldwasser–Micali

Sander–Young–Yung

Boneh–Goh–Nissim

Ishai–Paskin

Joye-Libert

Castagnos–Laguillaumie

Notes

LightPHE

Python

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

FHE libraries

Name

Developer

BGV

CKKS

BFV

FHEW

CKKS Bootstrapping

TFHE

Description

HElib

IBM

Yes

Yes

No

No

No

No

BGV scheme with the GHS optimizations.

Microsoft SEAL

Microsoft

Yes

Yes

Yes

No

No

No

OpenFHE

Duality Technologies

,

Samsung Advanced Institute of Technology

,

Intel

,

MIT

,

University of California, San Diego

and others.

Yes

Yes

Yes

Yes

Yes

Yes

Successor to

PALISADE

.

PALISADE

New Jersey Institute of Technology

, Duality Technologies,

Raytheon BBN Technologies

,

MIT

,

University of California, San Diego

and others.

Yes

Yes

Yes

Yes

No

Yes

General-purpose lattice cryptography library. Predecessor of

OpenFHE

.

HEAAN

CryptoLab

No

Yes

No

No

Yes

No

FHEW

Leo Ducas and Daniele Micciancio

No

No

No

Yes

No

No

TFHE

Ilaria Chillotti, Nicolas Gama, Mariya Georgieva and Malika Izabachene

No

No

No

No

No

Yes

FV-NFLlib

CryptoExperts

No

No

Yes

No

No

No

NuFHE

NuCypher

No

No

No

No

No

Yes

Provides a GPU implementation of TFHE.

REDcuFHE

TwC Group

No

No

No

No

No

Yes

A multi-GPU implementation of TFHE.

Lattigo

EPFL-LDS, Tune Insight

Yes

Yes

Yes

No

Yes

No

Implementation in

Go

along with their

distributed

variants

enabling

Secure multi-party computation

.

TFHE-rs

Zama

No

No

No

No

No

Yes

Rust implementation of TFHE-extended. Supporting Boolean, integer operation and univariate function evaluation (via Programmable Bootstrapping

).

Liberate.FHE

Desilo

No

Yes

No

No

No

No

A multi-GPU implementation of CKKS.

FHE frameworks

Name

Developer

FHEW

TFHE

HElib

SEAL

PALISADE

Lattigo

Description

Concrete

Zama

No

Yes

No

No

No

No

TFHE-extended compiler with a Python Frontend.

E3

MoMA Lab at NYU Abu Dhabi

Yes

Yes

Yes

Yes

Yes

No

SHEEP

Alan Turing Institute

No

Yes

Yes

Yes

Yes

No

T2

TwC Group

No

Yes

Yes

Yes

Yes

Yes

HELM

TwC Group

No

Yes

No

No

No

No

Juliet

TwC Group

No

Yes

No

No

No

No

PEEV

TwC Group

No

No

No

Yes

No

No

Verifiable encrypted computations based on Rinocchio ZKP and BGV homomorphic Encryption.

## Standardization

In 2017, researchers from IBM, Microsoft, Intel, the NIST, and others formed the open Homomorphic Encryption Standardization Consortium, which maintains a community security Homomorphic Encryption Standard.
