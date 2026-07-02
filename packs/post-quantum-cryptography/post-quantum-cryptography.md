---
title: "Post-quantum cryptography"
source: https://en.wikipedia.org/wiki/Post-quantum_cryptography
domain: post-quantum-cryptography
license: CC-BY-SA-4.0
tags: post quantum cryptography, quantum resistant algorithm, shor algorithm threat, nist pqc standardization, quantum safe encryption
fetched: 2026-07-02
---

# Post-quantum cryptography

**Post-quantum cryptography** (**PQC**), sometimes referred to as **quantum-proof**, **quantum-safe**, or **quantum-resistant**, is the development of cryptographic algorithms (usually public-key algorithms) that are currently thought, but not proven, to be secure against a cryptanalytic attack by a quantum computer. Most widely used public-key algorithms rely on the difficulty of one of three mathematical problems: the integer factorization problem, the discrete logarithm problem, or the elliptic-curve discrete logarithm problem. All of these problems could be easily solved on a sufficiently powerful quantum computer running Shor's algorithm or possibly alternatives.

As of 2026, quantum computers lack the processing power to break widely used cryptographic algorithms; however, because of the length of time required for migration to quantum-safe cryptography, cryptographers are already designing new algorithms to prepare for Y2Q or "Q-Day", the day when current algorithms will be vulnerable to quantum computing attacks. Mosca's theorem provides the risk analysis framework that helps organizations identify how quickly they need to start migrating.

Their work has gained attention from academics and industry through the PQCrypto conference series hosted since 2006, several workshops on Quantum Safe Cryptography hosted by the European Telecommunications Standards Institute (ETSI), and the Institute for Quantum Computing. The rumoured existence of widespread harvest now, decrypt later programs has also been seen as a motivation for the early introduction of post-quantum algorithms, as data recorded now may still remain sensitive many years into the future.

In contrast to the threat quantum computing poses to current public-key algorithms, most current symmetric cryptographic algorithms and hash functions are considered to be relatively secure against attacks by quantum computers. While the quantum Grover's algorithm does speed up attacks against symmetric ciphers, doubling the key size can effectively counteract these attacks. Thus post-quantum symmetric cryptography does not need to differ significantly from current symmetric cryptography.

In 2024, the U.S. National Institute of Standards and Technology (NIST) released final versions of its first three Post-Quantum Cryptography Standards.

## Migration

The transition from classical public-key cryptography to post-quantum cryptography (PQC) is considered a long-term, multi-phase process due to the widespread deployment of cryptographic infrastructure across digital systems. Migration planning is influenced by factors such as data longevity requirements, regulatory guidance, interoperability constraints, and the operational complexity of replacing embedded cryptographic components.

One commonly cited risk model is Mosca’s theorem, which estimates the urgency of migration by comparing three time horizons: the time required to transition systems (X), the time during which data must remain secure (Y), and the estimated arrival of cryptographically relevant quantum computers (Z). If X + Y > Z, migration is considered urgent.

A major concern motivating early transition is the “harvest now, decrypt later” threat model, in which encrypted data is intercepted and stored with the intention of decrypting it once large-scale quantum computers become available.

Migration strategies frequently emphasize crypto-agility, the capability of systems to rapidly replace cryptographic primitives without major architectural changes. Hybrid cryptographic deployments where classical and post-quantum algorithms are used simultaneously have been tested in protocols such as Transport Layer Security (TLS) to reduce transitional risk.

In 2024, the National Institute of Standards and Technology (NIST) finalized its first post-quantum cryptography standards, including module-lattice-based key encapsulation and digital signature schemes, providing a foundation for structured migration in governmental and commercial systems.

International organizations and national cybersecurity agencies have published coordinated roadmaps outlining phased adoption timelines, risk assessments, and procurement guidelines to facilitate a systematic transition.

## Monitoring Cryptographically Relevant Quantum Computing Progress

Because the transition to post-quantum cryptography is expected to take many years, organizations increasingly monitor advances in quantum computing to assess whether migration timelines remain appropriate. Rather than relying on a single measurement, researchers and cybersecurity agencies evaluate multiple technical indicators that together provide a more meaningful assessment of progress toward cryptographically relevant quantum computers (CRQCs).

Physical qubit counts alone are generally considered an incomplete measure of cryptographic capability because large numbers of noisy physical qubits may not be able to perform the long, fault-tolerant computations required for practical cryptanalysis. Consequently, greater emphasis is often placed on advances in logical qubits, quantum error correction, gate fidelity, circuit depth, and the successful implementation of quantum algorithms such as Shor's algorithm on increasingly complex problems.

Progress is also assessed through publicly demonstrated cryptographic milestones, including successful attacks against progressively larger instances of integer factorization and elliptic-curve cryptography, improvements in fault-tolerant quantum architectures, and the continued development of post-quantum cryptographic standards by organizations such as the National Institute of Standards and Technology (NIST). Together, these technical and institutional indicators help governments, industry, and researchers evaluate the pace of quantum computing development and adjust long-term migration strategies as new evidence becomes available.

## Preparation

Digital infrastructures require robust cybersecurity. Cryptographic systems are vital to protect the confidentiality and authenticity of data. Quantum computing will be a threat to many of the classical cryptographic algorithms, which are used to achieve these protection goals but are only secure against classical computers. Data that is currently not quantum-safe, whether it is stored or transmitted, and that must remain confidential for a long time, may be compromised in the future by quantum computers (“harvest now, decrypt later” attacks). In addition, authenticity will also be jeopardised by quantum computers. The threat that quantum computing poses to cybersecurity can be countered by a timely, comprehensive and coordinated transition to post-quantum cryptography (PQC).

## Algorithms

Post-quantum cryptography research is mostly focused on six different approaches:

### Lattice-based cryptography

This approach includes cryptographic systems such as learning with errors, ring learning with errors (ring-LWE), the ring learning with errors key exchange and the ring learning with errors signature, the older NTRU or GGH encryption schemes, and the newer NTRU signature and BLISS signatures. Some of these schemes like NTRU encryption have been studied for many years without anyone finding a feasible attack. Others like the ring-LWE algorithms have proofs that their security reduces to a worst-case problem. The Post-Quantum Cryptography Study Group sponsored by the European Commission suggested that the Stehle–Steinfeld variant of NTRU be studied for standardization rather than the NTRU algorithm. At that time, NTRU was still patented. Studies have indicated that NTRU may have more secure properties than other lattice based algorithms. Two lattice-based algorithms, ML-KEM (commonly known as Kyber) and ML-DSA (commonly known as Dilithium) were among the first post-quantum algorithms standardised by NIST.

### Multivariate cryptography

This includes cryptographic systems such as the Unbalanced Oil and Vinegar signature scheme which is based on the difficulty of solving systems of multivariate equations. Various attempts to build secure multivariate equation encryption schemes have been broken, notably the Rainbow signature.

### Hash-based cryptography

This includes cryptographic systems such as Lamport signatures, the Merkle signature scheme, the XMSS, the SPHINCS, the WOTS and the SPHINCS+ schemes. Hash based digital signatures were invented in the late 1970s by Ralph Merkle and have been studied ever since as an interesting alternative to number-theoretic digital signatures like RSA and DSA. Their primary drawback is that for any hash-based public key, there is a limit on the number of signatures that can be signed using the corresponding set of private keys. This fact reduced interest in these signatures until interest was revived due to the desire for cryptography that was resistant to attack by quantum computers. There appear to be no patents on the Merkle signature scheme and there exist many non-patented hash functions that could be used with these schemes. The stateful hash-based signature scheme XMSS developed by a team of researchers under the direction of Johannes Buchmann is described in RFC 8391.

Note that all the above schemes are one-time or bounded-time signatures. Moni Naor and Moti Yung invented UOWHF hashing in 1989 and designed a signature based on hashing (the Naor-Yung scheme) which can be unlimited-time in use (the first such signature that does not require trapdoor properties).

### Code-based cryptography

This includes cryptographic systems which rely on error-correcting codes, such as the McEliece and Niederreiter encryption algorithms and the related Courtois, Finiasz and Sendrier Signature scheme. The original McEliece signature using random Goppa codes has withstood scrutiny for over 40 years. However, many variants of the McEliece scheme, which seek to introduce more structure into the code used in order to reduce the size of the keys, have been shown to be insecure. The Post-Quantum Cryptography Study Group sponsored by the European Commission has recommended the McEliece public key encryption system as a candidate for long term protection against attacks by quantum computers. In 2025, NIST announced plans to standardize the code-based HQC encryption algorithm.

### Isogeny-based cryptography

These cryptographic systems rely on the properties of isogeny graphs of elliptic curves (and higher-dimensional abelian varieties) over finite fields, in particular supersingular isogeny graphs, to create cryptographic systems. Among the more well-known representatives of this field are the Diffie–Hellman-like key exchange *CSIDH*, which can serve as a straightforward quantum-resistant replacement for the Diffie–Hellman and elliptic curve Diffie–Hellman key-exchange methods that are in widespread use today, and the signature scheme SQIsign which is based on the categorical equivalence between supersingular elliptic curves and maximal orders in particular types of quaternion algebras. Another widely noticed construction, *SIDH/SIKE*, was spectacularly broken in 2022. The attack is however specific to the SIDH/SIKE family of schemes and does not generalize to other isogeny-based constructions.

### Symmetric key quantum resistance

Using sufficiently large key sizes, the symmetric key cryptographic systems like AES and SNOW 3G are already resistant to attack by a quantum computer. Further, key management systems and protocols that use symmetric key cryptography instead of public key cryptography, like Kerberos and the 3GPP Mobile Network Authentication Structure, are also inherently secure against attack by a quantum computer. Given its widespread deployment in the world, some researchers recommend expanded use of Kerberos-like symmetric key management as an efficient way to get post-quantum cryptography today.

## Security reductions

In cryptography research, it is desirable to prove the equivalence of a cryptographic algorithm and a known hard mathematical problem. These proofs are often called "security reductions", and are used to demonstrate the difficulty of cracking the encryption algorithm. In other words, the security of a given cryptographic algorithm is reduced to the security of a known hard problem. Researchers are actively looking for security reductions in the prospects for post-quantum cryptography. Current results are given here:

### Lattice-based cryptography – Ring-LWE Signature

In some versions of Ring-LWE there is a security reduction to the shortest-vector problem (SVP) in a lattice as a lower bound on the security. The SVP is known to be NP-hard. Specific ring-LWE systems that have provable security reductions include a variant of Lyubashevsky's ring-LWE signatures defined in a paper by Güneysu, Lyubashevsky, and Pöppelmann. The GLYPH signature scheme is a variant of the Güneysu, Lyubashevsky, and Pöppelmann (GLP) signature which takes into account research results that have come after the publication of the GLP signature in 2012. Another Ring-LWE signature is Ring-TESLA. There also exists a "derandomized variant" of LWE, called Learning with Rounding (LWR), which yields "improved speedup (by eliminating sampling small errors from a Gaussian-like distribution with deterministic errors) and bandwidth". While LWE uses the addition of a small error to conceal the lower bits, LWR uses rounding for the same purpose.

### Lattice-based cryptography – NTRU, BLISS

The security of the NTRU encryption scheme and the BLISS signature is believed to be related to, but not provably reducible to, the closest vector problem (CVP) in a lattice. The CVP is known to be NP-hard. The Post-Quantum Cryptography Study Group sponsored by the European Commission suggested that the Stehle–Steinfeld variant of NTRU, which *does* have a security reduction, be studied for long term use instead of the original NTRU algorithm.

### Multivariate cryptography – Unbalanced oil and vinegar

Unbalanced Oil and Vinegar signature schemes are asymmetric cryptographic primitives based on multivariate polynomials over a finite field ⁠ $\mathbb {F}$ ⁠. Bulygin, Petzoldt, and Buchmann have shown a reduction of generic multivariate quadratic UOV systems to the NP-Hard multivariate quadratic equation solving problem.

### Hash-based cryptography – Merkle signature scheme

In 2005, Luis Garcia proved that there was a security reduction of Merkle Hash Tree signatures to the security of the underlying hash function. Garcia showed in his paper that if computationally one-way hash functions exist then the Merkle Hash Tree signature is provably secure.

Therefore, use of a hash function with a provable reduction of security to a known hard problem would have a provable security reduction of the Merkle tree signature to that known hard problem.

The Post-Quantum Cryptography Study Group sponsored by the European Commission has recommended use of the Merkle signature scheme for long term security protection against quantum computers.

### Code-based cryptography – McEliece

The McEliece Encryption System has a security reduction to the syndrome decoding problem (SDP). The SDP is known to be NP-hard. The Post-Quantum Cryptography Study Group sponsored by the European Commission has recommended the use of this cryptography for long term protection against attack by a quantum computer.

### Code-based cryptography – RLCE

In 2016, Wang proposed a random linear code encryption scheme RLCE which is based on McEliece schemes. A RLCE scheme can be constructed using any linear code such as Reed-Solomon code by inserting random columns in the underlying linear code generator matrix.

### Supersingular elliptic curve isogeny cryptography

Security is related to the problem of constructing an isogeny between two supersingular curves with the same number of points. The most recent published investigation of the difficulty of this problem, by Delfs and Galbraith, indicates that this problem is as hard as the inventors of the key exchange suggest that it is. There is no security reduction to a known NP-hard problem.

## Comparison

One common characteristic of many post-quantum cryptography algorithms is that they require larger key sizes than commonly used "pre-quantum" public key algorithms. There are often tradeoffs to be made in key size, computational efficiency and ciphertext or signature size. The table below lists some values for different schemes at a 128-bit post-quantum security level.

| Algorithm | Type | Public key | Private key | Signature |
|---|---|---|---|---|
| ML-DSA | Lattice | 1,312 B | 2,560 B | 2,420 B |
| NTRUEncrypt | Lattice | 699 B | 935 B |   |
| Streamlined NTRU Prime | Lattice | 154 B |   |   |
| SPHINCS | Hash Signature | 1,000 B | 1,000 B | 41,000 B |
| SPHINCS+ | Hash Signature | 32 B | 64 B | 8,000 B |
| BLISS-II | Lattice | 7,000 B | 2,000 B | 5,000 B |
| GLP-Variant GLYPH Signature | Ring-LWE | 2,000 B | 400 B | 1,800 B |
| NewHope | Ring-LWE | 2,000 B | 2,000 B |   |
| Goppa-based McEliece | Code-based | 1,000,000 B | 11,500 B |   |
| Random Linear Code based encryption | RLCE | 115,000 B | 3,000 B |   |
| Quasi-cyclic MDPC-based McEliece | Code-based | 1,232 B | 2,464 B |   |
| SIDH | Isogeny | 564 B | 48 B |   |
| SIDH (compressed keys) | Isogeny | 330 B | 48 B |   |
| 3072-bit Discrete Log | **not PQC** | 384 B | 32 B | 96 B |
| 256-bit Elliptic Curve | **not PQC** | 32 B | 32 B | 65 B |

A practical consideration on a choice among post-quantum cryptographic algorithms is the effort required to send public keys over the internet. From this point of view, the Ring-LWE, NTRU, and SIDH algorithms provide key sizes conveniently under 1 kB, hash-signature public keys come in under 5 kB, and MDPC-based McEliece takes about 1 kB. On the other hand, Goppa-based McEliece requires a nearly 1 MB key.

### Lattice-based cryptography – LWE key exchange and Ring-LWE key exchange

The fundamental idea of using LWE and Ring LWE for key exchange was proposed and filed at the University of Cincinnati in 2011 by Jintai Ding. The basic idea comes from the associativity of matrix multiplications, and the errors are used to provide the security. The paper appeared in 2012 after a provisional patent application was filed in 2012.

In 2014, Peikert presented a key transport scheme following the same basic idea of Ding's, where the new idea of sending an additional 1 bit signal for rounding in Ding's construction is also used. For somewhat greater than 128 bits of security, Singh presents a set of parameters which have 6956-bit public keys for the Peikert's scheme. The corresponding private key would be roughly 14,000 bits.

In 2015, an authenticated key exchange with provable forward security following the same basic idea of Ding's was presented at Eurocrypt 2015, which is an extension of the HMQV construction in Crypto2005. The parameters for different security levels from 80 bits to 350 bits, along with the corresponding key sizes are provided in the paper.

### Lattice-based cryptography – NTRU encryption

For 128 bits of security in NTRU, `ntruhps2048509` with n = 509 and q = 2048 was selected in the NIST submission in September 2020. This results in a public key of 699 bytes and a corresponding private key of 935 bytes.

### Multivariate cryptography

### Hash-based cryptography – Merkle signature scheme

In order to get 128 bits of security for hash based signatures to sign 1 million messages using the fractal Merkle tree method of Naor Shenhav and Wool the public and private key sizes are roughly 36,000 bits in length.

### Code-based cryptography – McEliece

For 128 bits of security in a McEliece scheme, The European Commission's Post-Quantum Cryptography Study group recommends using a binary Goppa code of length at least *n* = 6960 and dimension at least *k* = 5413, and capable of correcting *t* = 119 errors. With these parameters the public key for the McEliece system will be a systematic generator matrix whose non-identity part takes *k* × (*n* − *k*) = 8373911 bits. The corresponding private key, which consists of the code support with *n* = 6960 elements from GF(213) and a generator polynomial of with *t* = 119 coefficients from GF(213), will be 92,027 bits in length.

The group is also investigating the use of Quasi-cyclic MDPC codes of length at least *n* = 216 + 6 = 65542 and dimension at least *k* = 215 + 3 = 32771, and capable of correcting *t* = 264 errors. With these parameters the public key for the McEliece system will be the first row of a systematic generator matrix whose non-identity part takes *k* = 32771 bits. The private key, a quasi-cyclic parity-check matrix with *d* = 274 nonzero entries on a column (or twice as much on a row), takes no more than *d* × 16 = 4384 bits when represented as the coordinates of the nonzero entries on the first row.

Barreto et al. recommend using a binary Goppa code of length at least *n* = 3307 and dimension at least *k* = 2515, and capable of correcting *t* = 66 errors. With these parameters the public key for the McEliece system will be a systematic generator matrix whose non-identity part takes *k* × (*n* − *k*) = 1991880 bits. The corresponding private key, which consists of the code support with *n* = 3307 elements from GF(212) and a generator polynomial of *t* = 66 coefficients from GF(212), will be 40,476 bits in length.

### Supersingular elliptic curve isogeny cryptography

For 128 bits of security in the supersingular isogeny Diffie–Hellman (SIDH) method, De Feo, Jao and Plut recommend using a supersingular curve modulo of a 768-bit prime. If one uses elliptic curve point compression, the public key will need to be no more than 8x768 or 6144 bits in length. A March 2016 paper by authors Azarderakhsh, Jao, Kalach, Koziel, and Leonardi showed how to cut the number of bits transmitted in half, which was further improved by authors Costello, Jao, Longa, Naehrig, Renes and Urbanik resulting in a compressed-key version of the SIDH protocol with public keys only 2640 bits in size. This makes the number of bits transmitted roughly equivalent to the non-quantum secure RSA and Diffie–Hellman at the same classical security level.

### Symmetric-key–based cryptography

As a general rule, for 128 bits of security in a symmetric-key–based system, one can safely use key sizes of 256 bits. The best quantum attack against arbitrary symmetric-key systems is an application of Grover's algorithm, which requires work proportional to the square root of the size of the key space. To transmit an encrypted key to a device that possesses the symmetric key necessary to decrypt that key requires roughly 256 bits as well. It is clear that symmetric-key systems offer the smallest key sizes for post-quantum cryptography.

## Forward secrecy

A public-key system demonstrates a property referred to as perfect forward secrecy when it generates random public keys per session for the purposes of key agreement. This means that the compromise of one message cannot lead to the compromise of others, and also that there is not a single secret value which can lead to the compromise of multiple messages. Security experts recommend using cryptographic algorithms that support forward secrecy over those that do not. The reason for this is that forward secrecy can protect against the compromise of long term private keys associated with public/private key pairs. This is viewed as a means of preventing mass surveillance by intelligence agencies.

Both the Ring-LWE key exchange and supersingular isogeny Diffie–Hellman (SIDH) key exchange can support forward secrecy in one exchange with the other party. Both the Ring-LWE and SIDH can also be used without forward secrecy by creating a variant of the classic ElGamal encryption variant of Diffie–Hellman.

The other algorithms in this article, such as NTRU, do not support forward secrecy as is.

Any authenticated public key encryption system can be used to build a key exchange with forward secrecy.

## Open Quantum Safe project

The **Open Quantum Safe** (**OQS**) project was started in late 2016 and has the goal of developing and prototyping quantum-resistant cryptography. It aims to integrate current post-quantum schemes in one library: **liboqs**. liboqs is an open source C library for quantum-resistant cryptographic algorithms. It initially focuses on key exchange algorithms but by now includes several signature schemes. It provides a common application programming interface (API) suitable for post-quantum key exchange algorithms, and will collect together various implementations. liboqs will also include a test harness and benchmarking routines to compare performance of post-quantum implementations. Furthermore, OQS also provides integration of liboqs into OpenSSL.

As of March 2023, the following key exchange algorithms are supported:

As of August 2024, NIST has published 3 algorithms below as FIPS standards and the 4th is expected near end of the year:

| Algorithm | Type |
|---|---|
| BIKE | codes |
| Classic McEliece | goppa codes |
| FIPS-203: CRYSTALS-Kyber | ML-KEM: Module Learning With Error |
| FIPS-204: CRYSTALS-Dilithium | ML-DSA: Module Short Integer Solution |
| FIPS-205: SPHINCS+ | SLH-DSA: hash based |
| FIPS-206: Falcon | FN-DSA: Short Integer Solution |
| Frodo | Learning with errors |
| HQC | codes |
| NTRU | Lattice-based cryptography |

Older supported versions that have been removed because of the progression of the NIST Post-Quantum Cryptography Standardization Project are:

| Algorithm | Type |
|---|---|
| BCNS15 | Ring learning with errors key exchange |
| McBits | Error-correcting codes |
| NewHope | Ring learning with errors key exchange |
| SIDH | Supersingular isogeny key exchange |

## Implementation

A challenge in post-quantum cryptography is the implementation of potentially quantum safe algorithms into existing systems. There are tests done, for example by Microsoft Research implementing PICNIC in a PKI using Hardware security modules. Test implementations for Google's NewHope algorithm have also been done by HSM vendors. In August 2023, Google released a FIDO2 security key implementation of an ECC/Dilithium hybrid signature schema which was done in partnership with ETH Zürich.

The Signal Protocol has used Post-Quantum Extended Diffie–Hellman (PQXDH) since 2023.

On February 21, 2024, Apple announced that they were going to upgrade their iMessage protocol with a new PQC protocol called "PQ3", which will use ongoing keying. Apple stated that, although capable quantum computers do not yet exist, they wanted to mitigate risks from future quantum computers as well as so-called "Harvest now, decrypt later" attack scenarios. Apple stated that they believe their PQ3 implementation provides protections that "surpass those in all other widely deployed messaging apps", because it uses ongoing keying. Apple intended to replace the existing iMessage protocol within all supported conversations with PQ3 by the end of 2024. Apple also defined a scale to make it easier to compare the security properties of messaging apps, with a scale represented by levels ranging from 0 to 3: 0 for no end-to-end by default, 1 for pre-quantum end-to-end by default, 2 for PQC key establishment only (e.g. PQXDH), and 3 for PQC key establishment *and* ongoing rekeying (PQ3).

The Internet Engineering Task Force has prepared an Internet-Draft using PQC algorithms in Messaging Layer Security (MLS). MLS will be used in RCS text messaging in Google Messages and Messages (Apple).

Other notable implementations include:

- bouncycastle
- liboqs

## Post-quantum cryptography in blockchain systems

Blockchain systems commonly rely on public-key cryptography, particularly elliptic-curve digital signature algorithms (ECDSA), to authenticate transactions and control asset ownership. These cryptographic schemes are vulnerable to quantum attacks, as Shor’s algorithm can efficiently solve the discrete logarithm problem on which they are based.

In many blockchain protocols, public keys are not revealed until a transaction is executed; however, once exposed, they may become susceptible to quantum attacks if adversaries possess sufficiently advanced quantum capabilities. This has led to recommendations that users migrate assets to quantum-resistant address schemes prior to the emergence of large-scale quantum computers.

The integration of post-quantum cryptographic algorithms into blockchain systems presents several technical challenges. Many post-quantum signature schemes require larger key and signature sizes, which can increase transaction size, storage requirements, and network bandwidth usage. Additionally, higher computational costs for verification may affect scalability and throughput in distributed networks.

Hybrid cryptographic approaches combining classical and post-quantum signatures have been proposed as transitional solutions. These approaches aim to maintain backward compatibility while gradually introducing quantum-resistant security mechanisms. Ongoing research is focused on optimizing post-quantum schemes for decentralized environments while balancing security, efficiency, and scalability requirements.

### Physical layer complements

While post-quantum algorithms protect data content from future decryption, they do not prevent the interception and storage of the encrypted ciphertext itself (a threat model known as "Harvest now, decrypt later"). To mitigate this risk, some network architectures incorporate physical layer security (PLS) or optical chaos alongside PQC.

By burying the optical signal within the noise floor (negative OSNR) using spectral phase encoding, these physical countermeasures aim to make the transmission unrecordable. This creates a "defense-in-depth" strategy: physical obfuscation prevents the harvesting of ciphertext entirely, ensuring that no data exists for future quantum decryption, while PQC algorithms provide necessary protection for data stored at the endpoints.

### Hybrid encryption

Google has maintained the use of "hybrid encryption" in its use of post-quantum cryptography: whenever a relatively new post-quantum scheme is used, it is combined with a more proven, non-PQ scheme. This is to ensure that the data are not compromised even if the relatively new PQ algorithm turns out to be vulnerable to non-quantum attacks before Y2Q. This type of scheme is used in its 2016 and 2019 tests for post-quantum TLS, and in its 2023 FIDO2 key. One of the algorithms used in the 2019 test, SIKE, was broken in 2022, but the non-PQ X25519 layer (already used widely in TLS) still protected the data. Apple's PQ3 and Signal's PQXDH are also hybrid.

The NSA and GCHQ argue against hybrid encryption, claiming that it adds complexity to implementation and transition. Daniel J. Bernstein, who supports hybrid encryption, argues that the claims are bogus.

## Criticisms

Post-quantum cryptography's need is predicated on traditional, established cryptographic problems being quickly solved by a quantum computer. However, quantum computers are still under development, and have yet to demonstrate a large scale test of Shor's algorithm, verifying that a quantum speed-up mechanism is possible, and out-performs a classical computer on such problems. In 2019, a team using the *IBM Q* quantum computer could factor the numbers 15 and 21, but *not* 35. Other attempts have been made to simulate quantum computers for larger numbers, but the simulations had no quantum advantage (i.e a speed-up over a classical computer).

While the *integer factorization*, *discrete logarithm*, and *elliptic-curve discrete logarithm problems* are potentially broken by the proposed quantum speed-up mechanism, none of the cryptography based on these mathematically difficult problems have been proven unsafe, nor mathematically broken outside of Shor's algorithm, or its derivatives. These cryptograpic systems are used worldwide, and have been extensively tested for vulnerabilities for several decades. Additionally, while Shor's algorithm proposes a polynomial time (i.e. fast) solution, via a quantum period-finding mechanism (i.e. finding a repeating period where the quantum computer tests all possible periods in parallel, then collapsing on correct a solution, or solutions), such a speed-up has never been proven to exist at scale.

Mathematicians Stephen Wolfram and Christopher Wolfram have created simulated models based on Branchial Graphs to mimic quantum mechanics, and by extension can emulate systems utilized by quantum computers. Their research lead Stephen to publicly express mild doubts about the proposed *quantum speed-up mechanism*'s existence, related to the systematic collapse/unwinding of the entangle quantum states down to a usable, error-corrected solution. That is, *doubts* about the mechanism responsible for the *theoretical quantum advantage* utilized by future quantum computers, at scale, where a large number of fully entangled qubits are capable of running Shor's Algorithm against a modern classical problem (e.g. RSA-2048, utilizing *integer factorization*).

In 2013, Edward Snowden's NSA leaks confirmed that the largest supercomputers of the time could not break *correctly implemented* public key crypto systems. Also, the NSA had not found a mathematical shortcut, despite being the largest employer of mathematicians in the world. Security analyst and cryptographer, Bruce Schneier, who had access to the Snowden archive, concluded that the math was never broken. Taken in aggregate, if the above criticisms prove to be true, then the need for *post-quantum cryptography* is put into question, along with the need to switch modern business infrastructure onto *less-proven* cryptographic schemes.
