---
title: "Format-preserving encryption"
source: https://en.wikipedia.org/wiki/Format-preserving_encryption
domain: format-preserving-encryption
license: CC-BY-SA-4.0
tags: format preserving encryption, feistel network cipher, fpe ff1 ff3, ciphertext format retention, aes based fpe
fetched: 2026-07-02
---

# Format-preserving encryption

In cryptography, **format-preserving encryption** (**FPE**), refers to encrypting in such a way that the output (the ciphertext) is in the same format as the input (the plaintext). The meaning of "format" varies. Typically only finite sets of characters are used; numeric, alphabetic or alphanumeric. For example:

- Encrypting a 16-digit credit card number so that the ciphertext is another 16-digit number.
- Encrypting an English word so that the ciphertext is another English word.
- Encrypting an *n*-bit number so that the ciphertext is another *n*-bit number (this is the definition of an *n*-bit block cipher).

For such finite domains, and for the purposes of the discussion below, the cipher is equivalent to a permutation of *N* integers {0, ... , *N*−1} where *N* is the size of the domain.

## Motivation

### Restricted field lengths or formats

One motivation for using FPE comes from the problems associated with integrating encryption into existing applications, with well-defined data models. A typical example would be a credit card number, such as `1234567812345670` (16 bytes long, digits only).

Adding encryption to such applications might be challenging if data models are to be changed, as it usually involves changing field length limits or data types. For example, output from a typical block cipher would turn credit card number into a hexadecimal (e.g.`0x96a45cbcf9c2a9425cde9e274948cb67`, 34 bytes, hexadecimal digits) or Base64 value (e.g. `lqRcvPnCqUJc3p4nSUjLZw==`, 24 bytes, alphanumeric and special characters), which will break any existing applications expecting the credit card number to be a 16-digit number.

Apart from simple formatting problems, using AES-128-CBC, this credit card number might get encrypted to the hexadecimal value `0xde015724b081ea7003de4593d792fd8b695b39e095c98f3a220ff43522a2df02`. In addition to the problems caused by creating invalid characters and increasing the size of the data, data encrypted using the CBC mode of an encryption algorithm also changes its value when it is decrypted and encrypted again. This happens because the random seed value that is used to initialize the encryption algorithm and is included as part of the encrypted value is different for each encryption operation. Because of this, it is impossible to use data that has been encrypted with the CBC mode as a unique key to identify a row in a database.

FPE attempts to simplify the transition process by preserving the formatting and length of the original data, allowing a drop-in replacement of plaintext values with their ciphertexts in legacy applications.

## Comparison to truly random permutations

Although a truly random permutation is the ideal FPE cipher, for large domains it is infeasible to pre-generate and remember a truly random permutation. So the problem of FPE is to generate a pseudorandom permutation from a secret key, in such a way that the computation time for a single value is small (ideally constant, but most importantly smaller than *O(N)*).

## Comparison to block ciphers

An *n*-bit block cipher technically *is* a FPE on the set {0, ..., 2*n*-1}. If an FPE is needed on one of these standard sized sets (for example, *n* = 64 for DES and *n* = 128 for AES) a block cipher of the right size can be used.

However, in typical usage, a block cipher is used in a mode of operation that allows it to encrypt arbitrarily long messages, and with an initialization vector as discussed above. In this mode, a block cipher is not an FPE.

## Definition of security

In cryptographic literature (see most of the references below), the measure of a "good" FPE is whether an attacker can distinguish the FPE from a truly random permutation. Various types of attackers are postulated, depending on whether they have access to oracles or known ciphertext/plaintext pairs.

## Algorithms

In most of the approaches listed here, a well-understood block cipher (such as AES) is used as a primitive to take the place of an ideal random function. This has the advantage that incorporation of a secret key into the algorithm is easy. Where AES is mentioned in the following discussion, any other good block cipher would work as well.

### The FPE constructions of Black and Rogaway

Implementing FPE with security provably related to that of the underlying block cipher was first undertaken in a paper by cryptographers John Black and Phillip Rogaway, which described three ways to do this. They proved that each of these techniques is as secure as the block cipher that is used to construct it. This means that if the AES algorithm is used to create an FPE algorithm, then the resulting FPE algorithm is as secure as AES because an adversary capable of defeating the FPE algorithm can also defeat the AES algorithm. Therefore, if AES is secure, then the FPE algorithms constructed from it are also secure. In all of the following, *E* denotes the AES encryption operation that is used to construct an FPE algorithm and *F* denotes the FPE encryption operation.

#### FPE from a prefix cipher

One simple way to create an FPE algorithm on {0, ..., *N*-1} is to assign a pseudorandom weight to each integer, then sort by weight. The weights are defined by applying an existing block cipher to each integer. Black and Rogaway call this technique a "prefix cipher" and showed it was provably as good as the block cipher used.

Thus, to create an FPE on the domain {0,1,2,3}, given a key *K* apply AES(*K*) to each integer, giving, for example,

```
weight(0) = 0x56c644080098fc5570f2b329323dbf62
weight(1) = 0x08ee98c0d05e3dad3eb3d6236f23e7b7
weight(2) = 0x47d2e1bf72264fa01fb274465e56ba20
weight(3) = 0x077de40941c93774857961a8a772650d
```

Sorting [0,1,2,3] by weight gives [3,1,2,0], so the cipher is

```
F(0) = 3
F(1) = 1
F(2) = 2
F(3) = 0
```

This method is only useful for small values of *N*. For larger values, the size of the lookup table and the required number of encryptions to initialize the table gets too big to be practical.

#### FPE from cycle walking

If there is a set *M* of allowed values within the domain of a pseudorandom permutation *P* (for example *P* can be a block cipher like AES), an FPE algorithm can be created from the block cipher by repeatedly applying the block cipher until the result is one of the allowed values (within *M*).

```
CycleWalkingFPE(x) {
    if P(x) is an element of M then
        return P(x)
    else
        return CycleWalkingFPE(P(x))
}
```

The recursion is guaranteed to terminate. (Because *P* is one-to-one and the domain is finite, repeated application of *P* forms a cycle, so starting with a point in *M* the cycle will eventually terminate in *M*.)

This has the advantage that the elements of *M* do not have to be mapped to a consecutive sequence {0,...,*N*-1} of integers. It has the disadvantage, when *M* is much smaller than *P*'s domain, that too many iterations might be required for each operation. If *P* is a block cipher of a fixed size, such as AES, this is a severe restriction on the sizes of *M* for which this method is efficient.

For example, an application may want to encrypt 100-bit values with AES in a way that creates another 100-bit value. With this technique, AES-128-ECB encryption can be applied until it reaches a value which has all of its 28 highest bits set to 0, which will take an average of 228 iterations to happen.

#### FPE from a Feistel network

It is also possible to make a FPE algorithm using a Feistel network. A Feistel network needs a source of pseudo-random values for the sub-keys for each round, and the output of the AES algorithm can be used as these pseudo-random values. When this is done, the resulting Feistel construction is good if enough rounds are used.

One way to implement an FPE algorithm using AES and a Feistel network is to use as many bits of AES output as are needed to equal the length of the left or right halves of the Feistel network. If a 24-bit value is needed as a sub-key, for example, it is possible to use the lowest 24 bits of the output of AES for this value.

This may not result in the output of the Feistel network preserving the format of the input, but it is possible to iterate the Feistel network in the same way that the cycle-walking technique does to ensure that format can be preserved. Because it is possible to adjust the size of the inputs to a Feistel network, it is possible to make it very likely that this iteration ends very quickly on average. In the case of credit card numbers, for example, there are 1015 possible 16-digit credit card numbers (accounting for the redundant check digit), and because the 1015 ≈ 249.8, using a 50-bit wide Feistel network along with cycle walking will create an FPE algorithm that encrypts fairly quickly on average.

### The Thorp shuffle

A Thorp shuffle is like an idealized card-shuffle, or equivalently a maximally-unbalanced Feistel cipher where one side is a single bit. It is easier to prove security for unbalanced Feistel ciphers than for balanced ones.

### VIL mode

For domain sizes that are a power of two, and an existing block cipher with a smaller block size, a new cipher may be created using VIL mode as described by Bellare, Rogaway.

### Hasty Pudding Cipher

The Hasty Pudding Cipher uses custom constructions (not depending on existing block ciphers as primitives) to encrypt arbitrary finite small domains.

### The FFSEM/FFX mode of AES

The FFSEM mode of AES (specification) that has been accepted for consideration by NIST uses the Feistel network construction of Black and Rogaway described above, with AES for the round function, with one slight modification: a single key is used and is tweaked slightly for each round.

As of February 2010, FFSEM has been superseded by the FFX mode written by Mihir Bellare, Phillip Rogaway, and Terence Spies. (specification, **NIST Block Cipher Modes Development*, 2010*).

### FPE for JPEG 2000 encryption

In JPEG 2000 standard, the marker codes (in the range 0xFF90 through 0xFFFF) should not appear in the plaintext and ciphertext. The simple modular-0xFF90 technique cannot be applied to solve the JPEG 2000 encryption problem. For example, the ciphertext words 0x23FF and 0x9832 are valid, but their combination 0x23FF9832 becomes invalid since it introduces the marker code 0xFF98. Similarly, the simple cycle-walking technique cannot be applied to solve the JPEG2000 encryption problem since two valid ciphertext blocks may give invalid ciphertext when they get combined. For example, if the first ciphertext block ends with bytes "...30FF" and the second ciphertext block starts with bytes "9832...", then the marker code "0xFF98" would appear in the ciphertext.

Two mechanisms for format-preserving encryption of JPEG 2000 were given in the paper "Efficient and Secure Encryption Schemes for JPEG2000" by Hongjun Wu and Di Ma. To perform format-preserving encryption of JPEG 2000, the technique is to exclude the byte "0xFF" in the encryption and decryption. Then a JPEG 2000 encryption mechanism performs modulo-n addition with stream cipher; another JPEG 2000 encryption mechanism performs the cycle-walking technique with block cipher.

### Other FPE constructions

Several FPE constructs are based on adding the output of a standard cipher, modulo n, to the data to be encrypted, with various methods of unbiasing the result. The modulo-n addition shared by many of the constructs is the immediately obvious solution to the FPE problem (thus its use in a number of cases), with the main differences being the unbiasing mechanisms used.

Section 8 of the FIPS 74, *Federal Information Processing Standards Publication 1981 Guidelines for Implementing and Using the NBS Data Encryption Standard*, describes a way to use the DES encryption algorithm in a manner that preserves the format of the data via modulo-n addition followed by an unbiasing operation. This standard was withdrawn on May 19, 2005, so the technique should be considered obsolete in terms of being a formal standard.

Another early mechanism for format-preserving encryption was Peter Gutmann's "Encrypting data with a restricted range of values" which again performs modulo-n addition on any cipher with some adjustments to make the result uniform, with the resulting encryption being as strong as the underlying encryption algorithm on which it is based.

The paper "Using Datatype-Preserving Encryption to Enhance Data Warehouse Security" by Michael Brightwell and Harry Smith describes a way to use the DES encryption algorithm in a way that preserves the format of the plaintext. This technique doesn't appear to apply an unbiasing step as do the other modulo-n techniques referenced here.

The paper "Format-Preserving Encryption" by Mihir Bellare and Thomas Ristenpart describes using "nearly balanced" Feistel networks to create secure FPE algorithms.

The paper "Format Controlling Encryption Using Datatype Preserving Encryption" by Ulf Mattsson describes other ways to create FPE algorithms.

An example of FPE algorithm is FNR (*Flexible Naor and Reingold*).

## Acceptance of FPE algorithms by standards authorities

NIST Special Publication 800-38G, "Recommendation for Block Cipher Modes of Operation: Methods for Format-Preserving Encryption" specifies two methods: FF1 and FF3. Details on the proposals submitted for each can be found at the NIST Block Cipher Modes Development site, including patent and test vector information. Sample values are available for both FF1 and FF3.

- FF1 is FFX[Radix] "Format-preserving Feistel-based Encryption Mode" which is also in standards processes under ANSI X9 as X9.119 and X9.124. It was submitted to NIST by Mihir Bellare of University of California, San Diego, Phillip Rogaway of University of California, Davis, and Terence Spies of Voltage Security Inc. Test vectors are supplied and parts of it are patented. (DRAFT SP 800-38G Rev 1) requires the minimum domain size of the data being encrypted to be 1 million (previously 100).

- FF3 is BPS named after the authors. It was submitted to NIST by Éric Brier, Thomas Peyrin and Jacques Stern of Ingenico in France. Authors declared to NIST that their algorithm is not patented. The CyberRes Voltage product, although claims to own patents also for BPS mode. On 12 April 2017, NIST concluded that FF3 is "no longer suitable as a general-purpose FPE method" because researchers found a vulnerability.
- FF3-1 (DRAFT SP 800-38G Rev 1) replaces FF3 and requires the minimum domain size of the data being encrypted to be 1 million (previously 100). On 3 February 2025, NIST withdrew FF3 entirely in the second draft revision (DRAFT SP 800-38G Rev 2) stating "An attack by Beyne [2021] on both FF3 and FF3-1 led to the removal of FF3".

Another mode was included in the draft NIST guidance but was removed before final publication.

- FF2 is VAES3 scheme for FFX: An addendum to "The FFX Mode of Operation for Preserving Encryption": A parameter collection for encipher strings of arbitrary radix with subkey operation to lengthen life of the enciphering key. It was submitted to NIST by Joachim Vance of VeriFone Systems Inc. Test vectors are not supplied separately from FF1 and parts of it are patented. Authors have submitted a modified algorithm as DFF which is under active consideration by NIST.

Korea has also developed a FPE standard, FEA-1 and FEA-2.

### Implementations

Open Source implementations of FF1 and FF3 are publicly available in C language, Go language, Java, Node.js, Python, C#/.Net and Rust
