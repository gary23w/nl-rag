---
title: "HKDF"
source: https://en.wikipedia.org/wiki/HKDF
domain: key-derivation-functions
license: CC-BY-SA-4.0
tags: key derivation function, password based key derivation, kdf salt stretching, hkdf extract expand
fetched: 2026-07-02
---

# HKDF

**HKDF** is a multi-purpose key derivation function (KDF) based on the HMAC message authentication code. HKDF follows "extract-then-expand" paradigm, where the KDF logically consists of two modules: the first stage takes the input keying material and "extracts" from it a fixed-length pseudorandom key, and then the second stage "expands" this key into several additional, independent pseudorandom keys as the output of the KDF.

## Mechanism

HKDF is the composition of two functions, HKDF-Extract and HKDF-Expand:

```
HKDF(salt, IKM, info, length) = HKDF-Expand(HKDF-Extract(salt, IKM), info, length)
```

### HKDF-Extract

HKDF-Extract (*XTR*) takes "input key material" or "source key material" (*IKM* or *SKM*) such as a shared secret generated using Diffie-Hellman; an optional, non-secret, random or pseudorandom salt (*r*); and generates a cryptographic key called the PRK ("pseudorandom key"). HKDF-Extract acts as a "randomness extractor", specifically a "computational extractor", taking a potentially non-uniform value of sufficient min-entropy and generating a value indistinguishable from a uniform random value (pseudorandom). Computational extractors assume attackers are computationally bounded and source entropy may only exist in a computational sense. Such extractors can be built using cryptographic functions under suitable assumptions, modeled as universal hash function (in the generic case) or a random oracle (in constrained scenarios like sources with weak entropy).

Salt (*r*) acts as a "source-independent extractor", strengthening HKDF's security guarantees. Using a fixed public *r* is safe for multiple invocations of HKDF (on "independent" but secret *IKM*s which may or may not be derived from the same source), provided *r* isn't chosen or manipulated by an attacker. Ideally, *r* is a random string of hash function's output length. Even low quality *r* (weak entropy or shorter length) is recommended as they contribute "significantly" to the security of the *OKM*. Without or with a low-entropy, non-secret *r*, if an attacker can influence the *IKM*s source in a way that specifically exploits HKDF-Extract's underlying hash function (finding a collision or a specific bias), *XTR* provides no protection. A random *r*, even if fixed by the application (for example, random number generators using *r* as seed), would strengthen protections for that specific extractor session. In such a setting, sufficiently long *IKM*s also provide better entropy extraction. However, allowing the attacker to influence enough of the *IKM* after seeing *r* may result in a completely insecure KDF.

HKDF-Extract is the result of HMAC with *r* as the key (all zeros up to length of the underlying extractor hash function, if not provided) and the *IKM* as the message. The underlying hash function used for HKDF-Extract step may be different to the one used by HKDF-Expand. It is recommended that HKDF-Extract uses strongest hash function available to the application, as it "concentrates" the entropy already present in *IKM* but may not necessarily "add" to it. Truncated output from a stronger underlying hash function for *XTR* (for example, SHA512/256) offers stronger extraction properties. The attacker is assumed to have partial knowledge about *IKM* (publicly known values in the case of Diffie-Hellman) or partial control over it (entropy pools).

HKDF-Extract may be skipped if the *IKM* is itself a cryptographically strong key (and hence can assume the role of *PRK*), though it is recommended that HKDF-Extract be applied for the sake of compatibility with the general case, especially if *r* is available to the application.

### HKDF-Expand

HKDF-Expand (*PRF**) takes the *PRK* (or any random key-derivation key if HKDF-Extract step is skipped), optional info (*CTXinfo*), and a length (*L*), to generate output key material (*OKM*) of length *L*. Multiple OKMs can be generated from a single PRK by using different values for *CTXinfo*, which must be "independent" of the *IKM* passed in HKDF-Extract. Even if an attacker, who knows *r* and some auxillary information about the secret *IKM*, can force the use of the same *IKM* (and *PRK*, by extension), in two or more HKDF-Expand contexts (represented by *CTXinfo*), the *OKM*s output are computationally independent (leak no useful information on each other).

HKDF-Expand, acting as a variable-output-length pseudorandom function (*PRF**) keyed on *PRK*, calls HMAC on *CTXinfo* as the message (empty string, if unspecified) appended to a 8-bit counter *i* initialized to 1. Subsequent calls to HMAC are chained in "feedback mode" by prepending the previous HMAC output to *CTXinfo* and incrementing *i*. *OKM* is a function of the output size (*k* bits) of HMAC's underlying hash function; i.e., SHA-256 outputs *OKM* in segments of *k*=256 bits for up to a maximum of length *i* × *k* bits (255 × 256 bits = 8160 bytes) truncated to desired length *L*.

HKDF-Expand may be skipped if *PRK* is at least desired length *L*, though it is recommended that HKDF-Expand be applied for additional "smoothing" of the *OKM*.

## Standardization

HKDF was proposed as a building block in various protocols and applications, as well as to discourage the proliferation of multiple KDF mechanisms by its authors.

It is formally described in RFC 5869 with detailed analysis in a paper published in 2010. NIST SP800-56Cr2 specifies a parameterizable extract-then-expand scheme, noting that RFC 5869 HKDF is a version of it and citing its paper for the rationale for the recommendations' extract-and-expand mechanisms.

## Applications

HKDF is used in the Signal Protocol for end-to-end encrypted messaging where it generates the message keys, in conjunction with the triple Elliptic-curve Diffie-Hellman handshake (X3DH) key agreement protocol. Signal's "Secure Value Recovery" and "Sealed Sender" are based on HKDF. HKDF is a main component in the Noise Protocol Framework, Message Layer Security, and is used in widely deployed protocols like IPsec Internet Key Exchange and TLS 1.3.

The "multi-purpose" nature of HKDF is meant to serve applications that require key extraction, key expansion, and key hierarchies in key wrapping, key exchange, PRNG, and password-based key derivation schemes.

## Implementations

There are implementations of HKDF for C#, Go, Java, JavaScript, Perl, PHP, Python, Ruby, Rust, and other programming languages. RFC6234 lays out a reference C implementation of HKDF based on the Secure Hash Standard.

### Example in Python

```mw
#!/usr/bin/env python3

import hashlib
import hmac

# nb: unused here; but SHA512/256 in extract phase provides stronger 
# extraction guarantees when expand is SHA256.
# hash_function_extract = hashlib.sha512
# RFC5869 includes SHA-1 test vectors
hash_function = hashlib.sha256

def hmac_digest(key: bytes, data: bytes) -> bytes:
    return hmac.new(key, data, hash_function).digest()

def hkdf_extract(salt: bytes, ikm: bytes) -> bytes:
    if len(salt) == 0:
        salt = bytes([0] * hash_function().digest_size)
    return hmac_digest(salt, ikm)

def hkdf_expand(prk: bytes, info: bytes, length: int) -> bytes:
    t = b""
    okm = b""
    i = 0
    while len(okm) < length:
        i += 1
        t = hmac_digest(prk, t + info + bytes([i]))
        okm += t
    return okm[:length]

def hkdf(salt: bytes, ikm: bytes, info: bytes, length: int) -> bytes:
    prk = hkdf_extract(salt, ikm)
    return hkdf_expand(prk, info, length)

okm = hkdf(
    salt=bytes.fromhex("000102030405060708090a0b0c"),
    ikm=bytes.fromhex("0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"),
    info=bytes.fromhex("f0f1f2f3f4f5f6f7f8f9"),
    length=42,
)
assert okm == bytes.fromhex(
    "3cb25f25faacd57a90434f64d0362f2a"
    "2d2d0a90cf1a5a4c5db02d56ecc4c5bf"
    "34007208d5b887185865"
)

# Zero-length salt
assert hkdf(
    salt=b"",
    ikm=bytes.fromhex("0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"),
    info=b"",
    length=42,
) == bytes.fromhex(
    "8da4e775a563c18f715f802a063c5a31"
    "b8a11f5c5ee1879ec3454e5f3c738d2d"
    "9d201395faa4b61a96c8"
)
```
