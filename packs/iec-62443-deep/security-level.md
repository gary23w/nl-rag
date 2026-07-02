---
title: "Security level"
source: https://en.wikipedia.org/wiki/Security_level
domain: iec-62443-deep
license: CC-BY-SA-4.0
tags: iec 62443 standard, ics security levels, defense in depth zones, operational technology segmentation, industrial security lifecycle
fetched: 2026-07-02
---

# Security level

In cryptography, **security level** is a measure of the strength that a cryptographic primitive — such as a cipher or hash function — achieves. Security level is usually expressed as a number of "bits of security" (also **security strength**), where *n*-bit security means that the attacker would have to perform 2*n* operations to break it, but other methods have been proposed that more closely model the costs for an attacker. This allows for convenient comparison between algorithms and is useful when combining multiple primitives in a hybrid cryptosystem, so there is no clear weakest link. For example, AES-128 (key size 128 bits) is designed to offer a 128-bit security level, which is considered roughly equivalent to a RSA using 3072-bit key.

In this context, **security claim** or **target security level** is the security level that a primitive was initially designed to achieve, although "security level" is also sometimes used in those contexts. When attacks are found that have lower cost than the security claim, the primitive is considered **broken**.

## In symmetric cryptography

Symmetric algorithms usually have a strictly defined security claim. For symmetric ciphers, it is typically equal to the key size of the cipher — equivalent to the complexity of a brute-force attack. Cryptographic hash functions with output size of *n* bits usually have a collision resistance security level *n*/2 and a preimage resistance level *n*. This is because the general birthday attack can always find collisions in 2*n/2* steps. For example, SHA-256 offers 128-bit collision resistance and 256-bit preimage resistance.

However, there are some exceptions to this. The Phelix and Helix are 256-bit ciphers offering a 128-bit security level. The SHAKE variants of SHA-3 are also different: for a 256-bit output size, SHAKE-128 provides 128-bit security level for both collision and preimage resistance.

## In asymmetric cryptography

The design of most asymmetric algorithms (i.e. public-key cryptography) relies on neat mathematical problems that are efficient to compute in one direction, but inefficient to reverse by the attacker. However, attacks against current public-key systems are always faster than brute-force search of the key space. Their security level isn't set at design time, but represents a computational hardness assumption, which is adjusted to match the best currently known attack.

Various recommendations have been published that estimate the security level of asymmetric algorithms, which differ slightly due to different methodologies.

- For the RSA cryptosystem at 128-bit security level, NIST and ENISA recommend using 3072-bit keys and IETF 3253 bits. The conversion from key length to a security level estimate is based on the complexity of the GNFS.
- Diffie–Hellman key exchange and DSA are similar to RSA in terms of the conversion from key length to a security level estimate.
- Elliptic curve cryptography requires shorter keys, so the recommendations for 128-bit are 256-383 (NIST), 256 (ENISA) and 242 bits (IETF). The conversion from key size *f* to security level is approximately *f* / 2: this is because the method to break the Elliptic Curve Discrete Logarithm Problem, the rho method, finishes in 0.886 sqrt(2*f*) additions.

## Typical levels

The following table are examples of typical security levels for types of algorithms as found in s5.6.1.1 of the US NIST SP-800-57 Recommendation for Key Management.

| Security Bits | Symmetric Key | Finite Field/Discrete Logarithm (DSA, DH, MQV) | Integer Factorization (RSA) | Elliptic Curve (ECDSA, EdDSA, ECDH, ECMQV) |
|---|---|---|---|---|
| 80 | 2TDEA | *L* = 1024, *N* = 160 | *k* = 1024 | 160 ≤ *f* ≤ 223 |
| 112 | 3TDEA | *L* = 2048, *N* =224 | *k* = 2048 | 224 ≤ *f* ≤ 255 |
| 128 | AES-128 | *L* = 3072, *N* = 256 | *k* = 3072 | 256 ≤ *f* ≤ 383 |
| 192 | AES-192 | *L* = 7680, *N* = 384 | *k* = 7680 | 384 ≤ *f* ≤ 511 |
| 256 | AES-256 | *L* = 15360, *N* = 512 | *k* = 15360 | *f* ≥ 512 |

1. DEA (DES) was deprecated in 2003 in the context of NIST recommendations.

Under NIST recommendation, a key of a given security level should only be transported under protection using an algorithm of equivalent or higher security level.

The security level is given for the cost of breaking one target, not the amortized cost for group of targets. It takes 2128 operations to find a AES-128 key, yet the same number of amortized operations is required for any number *m* of keys. On the other hand, breaking *m* ECC keys using the rho method require sqrt(*m*) times the base cost.

### Meaning of "broken"

A cryptographic primitive is considered broken when an attack is found to have less than its advertised level of security. However, not all such attacks are practical: most currently demonstrated attacks take fewer than 240 operations, which translates to a few hours on an average PC. The costliest demonstrated attack on hash functions is the 261.2 attack on SHA-1, which took 2 months on 900 GTX 1060 GPUs, and cost US$75,000 (although the researchers estimate only $11,000 was needed to find a collision).

Aumasson draws the line between practical and impractical attacks at 280 operations. He proposes a new terminology:

- A *broken* primitive has an attack taking ≤ 280 operations. An attack can be plausibly carried out.
- A *wounded* primitive has an attack taking between 280 and around 2100 operations. An attack is not possible right now, but future improvements are likely to make it possible.
- An *attacked* primitive has an attack that is cheaper than the security claim, but much costlier than 2100. Such an attack is too far from being practical.
- Finally, an *analyzed* primitive is one with no attacks cheaper than its security claim.

## Quantum attacks

The field of post-quantum cryptography considers the security level of cryptographic algorithms in the face of a hypothetical attacker possessing a quantum computer.

- Most quantum attacks on symmetric ciphers provide a square-root speedup to their classical counterpart, thereby halving the security level provided. (The exception is the slide attack with Simon's algorithm, though it has not proved useful in attacking AES.) For example, AES-256 would provide 128 bits of quantum security, which is still considered plenty.
- Shor's algorithm promises a massive speedup in solving the factoring problem, the discrete logarithm problem, and the period-finding problem, so long as a sufficiently large quantum computer on the order of millions of qubits is available. This would spell the end of RSA, DSA, DH, MQV, ECDSA, EdDSA, ECDH, and ECMQV in their current forms.

Even though quantum computers capable of these operations have yet to appear, adversaries of today may choose to "harvest now, decrypt later": to store intercepted ciphertexts so that they can be decrypted when sufficiently powerful quantum computers become available. As a result, governments and businesses have already begun work on moving to quantum-resistant algorithms. Examples of these effort include Google and Cloudflare's tests of hybrid post-quantum TLS on the Internet and NSA's release of Commercial National Security Algorithm Suite 2.0 in 2022.
