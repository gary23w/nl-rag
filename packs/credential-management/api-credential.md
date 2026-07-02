---
title: "Credential - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Credential
domain: credential-management
license: CC-BY-SA-4.0
tags: credential management api, browser credential store, federated credential login, automatic sign-in
fetched: 2026-07-02
---

# Credential

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2019.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`Credential`** interface of the Credential Management API provides information about an entity (usually a user) normally as a prerequisite to a trust decision.

`Credential` objects may be of the following types:

- `FederatedCredential`
- `IdentityCredential`
- `PasswordCredential`
- `PublicKeyCredential`
- `OTPCredential`

## Instance properties

**`Credential.id` Read only**

Returns a string containing the credential's identifier. This might be any one of a GUID, username, or email address.

**`Credential.type` Read only**

Returns a string containing the credential's type. Valid values are `password`, `federated`, `public-key`, `identity` and `otp`. (For `PasswordCredential`, `FederatedCredential`, `PublicKeyCredential`, `IdentityCredential` and `OTPCredential`)

## Static methods

**`Credential.isConditionalMediationAvailable()`**

Returns a `Promise` which always resolves to `false`. Subclasses may override this value.

## Examples

```js
const pwdCredential = new PasswordCredential({
  id: "example-username", // Username/ID
  name: "Carina Anand", // Display name
  password: "correct horse battery staple", // Password
});

console.assert(pwdCredential.type === "password");
```

## Specifications

| Specification |
|---|
| Credential Management Level 1 # the-credential-interface |

## Browser compatibility
