---
title: "Crypto - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Crypto
domain: web-crypto-api
license: CC-BY-SA-4.0
tags: web crypto api, subtle crypto operations, cryptographic key generation, secure random values
fetched: 2026-07-02
---

# Crypto

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`Crypto`** interface represents basic cryptography features available in the current context. It allows access to a cryptographically strong random number generator and to cryptographic primitives.

The `Crypto` is available in windows using the `Window.crypto` property and in workers using the `WorkerGlobalScope.crypto` property.

## Instance properties

**`Crypto.subtle` Read only Secure context**

Returns a `SubtleCrypto` object providing access to common cryptographic primitives, like hashing, signing, encryption, or decryption.

## Instance methods

**`Crypto.getRandomValues()`**

Fills the passed `TypedArray` with cryptographically sound random values.

**`Crypto.randomUUID()` Secure context**

Returns a randomly generated, 36 character long v4 UUID.

## Specifications

| Specification |
|---|
| Web Cryptography Level 2 # crypto-interface |

## Browser compatibility
