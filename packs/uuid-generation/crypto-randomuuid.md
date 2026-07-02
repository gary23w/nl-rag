---
title: "Crypto: randomUUID() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Crypto/randomUUID
domain: uuid-generation
license: CC-BY-SA-4.0
tags: uuid generation, universally unique identifier, rfc 4122 uuid, random identifier
fetched: 2026-07-02
---

# Crypto: randomUUID() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The **`randomUUID()`** method of the `Crypto` interface is used to generate a v4 UUID using a cryptographically secure random number generator.

## Syntax

```js
randomUUID()
```

### Parameters

None.

### Return value

A string containing a randomly generated, 36 character long v4 UUID.

## Examples

```js
/* Assuming that self.crypto.randomUUID() is available */

let uuid = self.crypto.randomUUID();
console.log(uuid); // for example "36b8f84d-df4e-4d49-b662-bcde71a8764f"
```

## Specifications

| Specification |
|---|
| Web Cryptography Level 2 # Crypto-method-randomUUID |

## Browser compatibility
