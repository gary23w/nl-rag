---
title: "Galois/Counter Mode"
source: https://en.wikipedia.org/wiki/Galois/Counter_Mode
domain: authenticated-encryption
license: CC-BY-SA-4.0
tags: authenticated encryption, aead cipher mode, galois counter mode, encrypt then mac
fetched: 2026-07-02
---

# Galois/Counter Mode

In cryptography, **Galois/Counter Mode** (**GCM**) is a mode of operation for symmetric-key cryptographic block ciphers. The proposal was first published in 2007. The GCM algorithm belongs to the class of authenticated encryption with associated data (AEAD) methods. Given a key K , plaintext P , and associated data $AD$ , GCM encrypts P to produce ciphertext C and an authentication tag T . T is computed from the ciphertext and the unencrypted associated data. A recipient who knows K can use the tag to verify that neither the ciphertext nor the associated data had been modified, and then decrypt the ciphertext to recover the plaintext.

GCM uses a block cipher with a block size of 128 bits, (commonly AES-128) run in counter mode for encryption and uses arithmetic in the Galois field GF(2128) to compute the authentication tag, hence its name.

**Galois Message Authentication Code** (**GMAC**) is an authentication-only variant of GCM that can form an incremental message authentication code. Both GCM and GMAC can accept initialization vectors of arbitrary length.

Different block cipher modes of operation can have significantly different performance with the same block cipher. As a counter mode, GCM blocks are independent. This allows encryption and decryption to be parallelized, in contrast to modes like cipher block chaining (CBC) where each block relies on the previous one.

GCM was explicitly designed to be patent-free.

## Basic operation

GCM operates as a counter mode block cipher to produce ciphertext.

For authentication, the ciphertext blocks are treated as coefficients of a polynomial evaluated at a key-dependent point *H* using finite field arithmetic. The result is then encrypted, producing an authentication tag that can be used to verify the integrity of the data, so that the encrypted text has the IV, ciphertext, and authentication tag.

## Mathematical basis

GCM combines the counter mode of encryption with the Galois mode of authentication. The central feature is the ease of parallel computation of the Galois field multiplication used for authentication. This feature has higher throughput than encryption algorithms like CBC that use chaining modes. The GF(2128) field used is defined by the polynomial

$x^{128}+x^{7}+x^{2}+x+1$

.

The authentication tag is constructed by feeding blocks of data into the GHASH function and encrypting the result. This GHASH function is defined by

$\operatorname {GHASH} (H,A,C)=X_{m+n+1}$

,

where $H=E_{k}(0^{128})$ is the *hash key*, a string of 128 zero bits encrypted using the block cipher; A is data that is only authenticated (not encrypted); C is the ciphertext; m is the number of 128-bit blocks in A (rounded up); n is the number of 128-bit blocks in C (rounded up); and the variable $X_{i}$ for $i=0,\dots m+n+1$ is defined below.

First, the authenticated text and the ciphertext are separately zero-padded to multiples of 128 bits and combined into a single message, $S_{i}$ , defined as

$S_{i}={\begin{cases}A_{i}&{\text{for }}i=1,\ldots ,m-1\\A_{m}^{*}\parallel 0^{128-v}&{\text{for }}i=m\\C_{i-m}&{\text{for }}i=m+1,\ldots ,m+n-1\\C_{n}^{*}\parallel 0^{128-u}&{\text{for }}i=m+n\\\operatorname {len} (A)\parallel \operatorname {len} (C)&{\text{for }}i=m+n+1\end{cases}}$

,

where $\operatorname {len} (A)$ and $\operatorname {len} (C)$ are the 64-bit representations of the bit lengths of A and C , respectively; $v=\operatorname {len} (A)\ \operatorname {mod} \ 128$ is the bit length of the final block of A *;* $u=\operatorname {len} (C)\ \operatorname {mod} \ 128$ is the bit length of the final block of C *;* and $\parallel$ denotes concatenation of bit strings.

Then, $X_{i}$ is defined as:

$X_{i}=\sum _{j=1}^{i}S_{j}\cdot H^{i-j+1}={\begin{cases}0&{\text{for }}i=0\\\left(X_{i-1}\oplus S_{i}\right)\cdot H&{\text{for }}i=1,\ldots ,m+n+1\end{cases}}$

.

The second form is an efficient iterative algorithm (each $X_{i}$ depends on $X_{i-1}$ ) produced by applying Horner's method to the first. Only the final $X_{m+n+1}$ stays an output.

If it is necessary to parallelize the hash computation, this can be done by interleaving k times:

${\begin{aligned}X_{i}^{'}&={\begin{cases}0&{\text{for }}i\leq 0\\\left(X_{i-k}^{'}\oplus S_{i}\right)\cdot H^{k}&{\text{for }}i=1,\ldots ,m+n+1-k\\\end{cases}}\\[6pt]X_{i}&=\sum _{j=1}^{k}\left(X_{i+j-2k}^{'}\oplus S_{i+j-k}\right)\cdot H^{k-j+1}\end{aligned}}$

.

If the length of the IV is not 96, the GHASH function is used to calculate *Counter 0*:

$\mathrm {Counter0} ={\begin{cases}IV\parallel 0^{31}\parallel 1&{\text{for }}\operatorname {len} (IV)=96\\\operatorname {GHASH} \left(IV\parallel 0^{s}\parallel 0^{64}\parallel \operatorname {len} _{64}(IV)\right){\text{ with }}s=128-\operatorname {len} (IV)\mod 128&{\text{otherwise}}\end{cases}}$

.

GCM was designed by John Viega and David A. McGrew as a development based on earlier counter-mode authenticated encryption designs, including Carter–Wegman counter mode (CWC mode).

In November 2007, NIST announced the release of NIST Special Publication 800-38D *Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC*, making GCM and GMAC official standards.

## Use

GCM mode is used in the IEEE 802.1AE (MACsec) Ethernet security, WPA3-Enterprise Wi-Fi security protocol, IEEE 802.11ad (also dubbed WiGig), ANSI (INCITS) Fibre Channel Security Protocols (FC-SP), IEEE P1619.1 tape storage, IETF IPsec standards, SSH, TLS 1.2 and TLS 1.3. AES-GCM is included in the NSA Suite B Cryptography and its latest replacement in 2018 Commercial National Security Algorithm (CNSA) suite. GCM mode is used in the SoftEther VPN server and client, as well as OpenVPN, where AES-GCM ciphers are available via configuration and cipher negotiation since version 2.4.

## Performance

GCM requires one block cipher operation and one 128-bit multiplication in the Galois field for each block (128 bits) of encrypted and authenticated data. The block cipher operations are pipelined or parallelized; the multiplication operations are pipelined and can be parallelized (either by parallelizing the actual operation, by adapting Horner's method per the original NIST submission, or both).

Intel has added the PCLMULQDQ instruction, which supports carry-less multiplication used in GCM implementations. In 2011, SPARC added the XMULX and XMULXHI instructions, which also perform 64 × 64-bit carry-less multiplication. In 2015, SPARC added the XMPMUL instruction, which performs XOR multiplication of much larger values, up to 2048 × 2048-bit input values, producing a 4096-bit result. These instructions enable fast multiplication over GF(2*n*) and can be used with any field representation.

Performance results are published for GCM on a number of platforms. Käsper and Schwabe described a "Faster and Timing-Attack Resistant AES-GCM" that achieves 10.68 cycles per byte of AES-GCM authenticated encryption on 64-bit Intel processors. Dai et al. report 3.5 cycles per byte for the same algorithm when using Intel's AES-NI and PCLMULQDQ instructions. Shay Gueron and Vlad Krasnov achieved 2.47 cycles per byte on the third-generation Intel processors. Appropriate patches were prepared for the OpenSSL and NSS libraries.

When both authentication and encryption need to be performed on a message, interleaving those operations using instruction-level parallelism can increase performance. This process is called function stitching, and while in principle it can be applied to any combination of cryptographic algorithms, GCM supports parallel computation which can simplify optimization on some processors. Manley and Gregg show the ease of optimizing when using function stitching with GCM. They present a program generator that takes an annotated C version of a cryptographic algorithm and generates code that runs well on the target processor.

GCM has been criticized in the embedded world (for example, by Silicon Labs) because the parallel processing is not suited for performant use of cryptographic hardware engines. As a result, GCM reduces the performance of encryption for some of the most performance-sensitive devices. Specialized hardware accelerators for ChaCha20-Poly1305 are less complex compared to AES accelerators.

## Security

GCM is proven to be secure in the concrete security model. It is secure when it is used with a block cipher that is indistinguishable from a random permutation; however, security depends on choosing a unique initialization vector for every encryption performed with the same key (*see* stream cipher attack). For any given key and initialization vector value, GCM is limited to encrypting 239−256 bits of plain text (64 GiB). NIST Special Publication 800-38D includes guidelines for initialization vector choice and limits the number of possible initialization vector values for a single key. As the security assurance of GCM degrades with more data being processed using the same key, the total number of blocks of plaintext and AD protected during the lifetime of a single key should be limited by 264.

The authentication strength depends on the length of the authentication tag, like with all symmetric message authentication codes. Using shorter authentication tags with GCM is discouraged. The bit-length of the tag, denoted *t*, is a security parameter. In general, *t* may be any one of the following five values: 128, 120, 112, 104, or 96. For certain applications, *t* may be 64 or 32, but the use of these two tag lengths constrains the length of the input data and the lifetime of the key. Appendix C in NIST SP 800-38D provides guidance for these constraints (for example, if *t* = 32 and the maximal packet size is 210 bytes, the authentication decryption function should be invoked no more than 211 times; if *t* = 64 and the maximal packet size is 215 bytes, the authentication decryption function should be invoked no more than 232 times).

Like with any message authentication code, if the adversary chooses a *t*-bit tag at random, it is expected to be correct for given data with probability measure 2−*t*. With GCM, however, an adversary can increase their likelihood of success by choosing tags with *n* words—the total length of the ciphertext plus any added authenticated data (AAD)—with probability measure 2−*t* by a factor of *n*. However, these best tags are still dominated by the algorithm's survival measure 1 − *n*⋅2−*t* for arbitrarily large *t*. Moreover, GCM is not well-suited for use with short tag-lengths or long messages.

Ferguson and Saarinen independently described how an attacker can perform best attacks against GCM authentication, which meets the lower bound on its security. Ferguson showed that, if *n* denotes the total number of blocks in the encoding (the input to the GHASH function), then there is a method of constructing a targeted ciphertext forgery that is expected to succeed with a probability of approximately *n*⋅2−*t*. If the tag length *t* is shorter than 128, then each successful forgery in this attack increases the probability that subsequent targeted forgeries will succeed, and leaks information about the hash subkey *H*. Eventually, *H* may be compromised entirely, at which point the authentication assurance is completely lost.

Independent of this attack, an adversary may try to systematically guess many different tags for a given input to authenticated decryption and thereby increase the probability that one (or more) of them, eventually, will be considered valid. For this reason, the system or protocol that implements GCM should watch and, if necessary, limit the number of unsuccessful verification attempts for each key.

Saarinen described GCM as having weak keys, offering some added analysis into how polynomial hash-based authentication works. More precisely, this work describes a particular way of forging a GCM message, given a valid GCM message, that works with probability of about *n*⋅2−128 for messages that are *n* × 128 bits long. However, this work does not show a more effective attack than was previously known; the success probability in observation 1 of this paper matches that of lemma 2 from the INDOCRYPT 2004 analysis (setting *w* = 128 and *l* = *n* × 128). Saarinen also described a GCM variant Sophie Germain Counter Mode (SGCM) based on Sophie Germain primes.
