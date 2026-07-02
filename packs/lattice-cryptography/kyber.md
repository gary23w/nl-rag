---
title: "ML-KEM"
source: https://en.wikipedia.org/wiki/Kyber
domain: lattice-cryptography
license: CC-BY-SA-4.0
tags: lattice based cryptography, learning with errors problem, shortest vector problem, quantum resistant key exchange, ntru lattice scheme
fetched: 2026-07-02
---

# ML-KEM

(Redirected from

Kyber

)

**ML-KEM** (**Module-Lattice-Based Key-Encapsulation Mechanism**), also known by its original name **Kyber**, is a key encapsulation mechanism (KEM) designed to be resistant to cryptanalytic attacks with future powerful quantum computers that was standardized in 2024. It is used to establish a shared secret between two communicating parties without an (IND-CCA2) attacker in the transmission system being able to decrypt it. This asymmetric cryptosystem uses a variant of the learning with errors lattice problem as its basic trapdoor function. It won the NIST competition for the first post-quantum cryptography (PQC) standard. and was subsequently standardized as **FIPS 203**.

## Properties

The system is based on the module learning with errors (M-LWE) problem, in conjunction with cyclotomic rings. Recently, there has also been a tight formal mathematical security reduction of the ring-LWE problem to MLWE. Compared to competing PQ methods, it has typical advantages of lattice-based methods, e.g. in regard to runtime as well as the size of the ciphertexts and the key material.

Variants with different security levels have been defined: ML-KEM-512 (NIST security level 1), ML-KEM-768 (NIST security level 3), and ML-KEM-1024 (NIST security level 5). At the ML-KEM-768 level, the secret keys are 2400 bytes in size, the public keys 1184, and the ciphertexts 1088.

With an accordingly optimized implementation, 4 kilobytes of memory can be sufficient for the cryptographic operations. For a chat encryption scenario using liboqs, replacing the extremely efficient, non-quantum-safe ECDH key exchange using Curve25519 was found to increase runtime by a factor of about 2.3 (1.5–7), an estimated 2.3-fold (1.4–3.1) increase in energy consumption, and have about 70 times (48–92) more data overhead. Internal hashing operations account for the majority of the runtime, which would thus potentially benefit greatly from corresponding hardware acceleration.

## History

Prior to standardization, ML-KEM was known under the name Kyber. Kyber, derived from a method published in 2005 by Oded Regev, was developed by developers from Europe and North America, who are employed by various government universities or research institutions, or by private companies, with funding from the European Commission, Switzerland, the Netherlands, and Germany. They also developed the related and complementary signature scheme *Dilithium* (later standardized as ML-DSA), as another component of their "Cryptographic Suite for Algebraic Lattices" (CRYSTALS). Like other PQC-KEM methods, Kyber makes extensive use of hashing internally. In Kyber's case, variants of Keccak (SHA-3/SHAKE) are used here, to generate pseudorandom numbers, among other things.

In 2017, the method was submitted to the US National Institute of Standards and Technology (NIST) for its public selection process for a first standard for quantum-safe cryptographic primitives (NISTPQC). It was the first key encapsulation mechanism that has been selected for standardization (and the only one at the end of the third round of the NIST standardization process). According to a footnote the report announcing the decision, it is conditional on the execution of various patent-related agreements, with NTRU being a fallback option. In 2025, within a fourth round of the standardization process, the HQC scheme has been selected for standardization as a fallback.

In the second phase of the selection process, several parameters of the algorithm were adjusted and the compression of the public keys was dropped. Most recently, NIST paid particular attention to costs in terms of runtime and complexity for implementations that mask runtimes in order to prevent corresponding side-channel attacks (SCA).

### Evolution

Kyber underwent changes during the NIST standardization process. In particular, in the submission for round 2 (so called *Kyber v2*), the following features were changed:

- Public key compression removed (due to NIST comments on the security proof)
- Parameter *q* reduced to 3329 (from 7681)
- Ciphertext compression parameters changed
- Number-theoretic transform (NTT) definition changed along the lines of NTRU for faster polynomial multiplication
- Noise parameter reduced to *η* = 2 for faster noise sampling
- Public key representation changed to NTT domain in order to save the NTT operations

Submission to round 3 underwent further tweaks:

- The use of Fujisaki–Okamoto transformation (FO transform) modified
- Noise level increased and ciphertext compression reduced for the level 1 parameter set
- Sampling algorithm improved

In the FIPS 203 Initial Public Draft (IPD) more changes were implemented:

- Shared secret key length is fixed to 256 bits
- A different variant of FO transform
- Use of NIST-approved randomness generation and removal of operations which previously guarded against the possibility of flawed randomness generation
- Explicit input checking

Changes made since the Initial Public Draft include:

- Domain separation was added to key generation
- Reversal of an index mismatch created inadvertently in the FIPS 203 IPD

## Usage

The developers have released a reference implementation into the public domain (or under CC0), which is written in C. The program library *liboqs* of the Open Quantum Safe (OQS) project contains an implementation based on that. OQS also maintains a quantum-safe Provider module for OpenSSL 3.x, and has integrated its code into BoringSSL. The wolfSSL library additionally maintains its own implementation of ML-KEM. There are a handful of implementations using various other programming languages from third-party developers, including JavaScript and Java. Various (free) optimized hardware implementations exist, including one that is resistant to side-channel attacks. The German Federal Office for Information Security is aiming for implementation in Thunderbird, and in this context also an implementation in the Botan program library and corresponding adjustments to the OpenPGP standard. Amazon Web Services (AWS) integrated Kyber into their Key Management Service (KMS) in 2020 as a hybrid post-quantum key exchange option for TLS connections. In 2023, the encrypted messaging service Signal implemented PQXDH, a Kyber-based post-quantum encryption algorithm, to their Signal Protocol.

## Implementations

- OpenSSL
- wolfSSL
- libOQS
- libzupt
- IAIK-JCE
- Libgcrypt since 1.11.0 with GNU Privacy Guard 1.5.x
