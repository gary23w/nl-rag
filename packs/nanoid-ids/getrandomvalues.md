---
title: "Crypto: getRandomValues() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues
domain: nanoid-ids
license: CC-BY-SA-4.0
tags: nanoid generator, compact unique id, url-safe identifier, collision resistant id
fetched: 2026-07-02
---

# Crypto: getRandomValues() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`Crypto.getRandomValues()`** method lets you get cryptographically strong random values. The array given as the parameter is filled with random numbers (random in its cryptographic meaning).

To guarantee enough performance, implementations are not using a truly random number generator, but they are using a pseudo-random number generator *seeded* with a value with enough entropy. The pseudo-random number generator algorithm (PRNG) may vary across user agents, but is suitable for cryptographic purposes.

`getRandomValues()` is the only member of the `Crypto` interface which can be used from an insecure context.

## Syntax

```js
getRandomValues(typedArray)
```

### Parameters

**`typedArray`**

An integer-based `TypedArray`, that is one of: `Int8Array`, `Uint8Array`, `Uint8ClampedArray`, `Int16Array`, `Uint16Array`, `Int32Array`, `Uint32Array`, `BigInt64Array`, `BigUint64Array` (but **not** `Float16Array`, `Float32Array` nor `Float64Array`). All elements in the array will be overwritten with random numbers.

### Return value

The same array passed as `typedArray` but with its contents replaced with the newly generated random numbers. Note that `typedArray` is modified in-place, and no copy is made.

### Exceptions

**`QuotaExceededError`**

Thrown if the `byteLength` of `typedArray` exceeds 65,536.

## Usage notes

Prefer the `generateKey()` method for key generation, which is guaranteed to be running in a secure context.

There is no minimum degree of entropy mandated by the Web Cryptography specification. User agents are instead urged to provide the best entropy they can when generating random numbers, using a well-defined, efficient pseudorandom number generator built into the user agent itself, but seeded with values taken from an external source of pseudorandom numbers, such as a platform-specific random number function, the Unix `/dev/urandom` device, or other source of random or pseudorandom data.

## Examples

```js
const array = new Uint32Array(10);
self.crypto.getRandomValues(array);

console.log("Your lucky numbers:");
for (const num of array) {
  console.log(num);
}
```

## Specifications

| Specification |
|---|
| Web Cryptography Level 2 # Crypto-method-getRandomValues |

## Browser compatibility
