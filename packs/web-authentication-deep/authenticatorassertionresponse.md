---
title: "AuthenticatorAssertionResponse - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/AuthenticatorAssertionResponse
domain: web-authentication-deep
license: CC-BY-SA-4.0
tags: web authentication ceremony, public key credential, authenticator attestation, assertion signature verify
fetched: 2026-07-02
---

# AuthenticatorAssertionResponse

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2021.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`AuthenticatorAssertionResponse`** interface of the Web Authentication API contains a digital signature from the private key of a particular WebAuthn credential. The relying party's server can verify this signature to authenticate a user, for example when they sign in.

An `AuthenticatorAssertionResponse` object instance is available in the `response` property of a `PublicKeyCredential` object returned by a successful `navigator.credentials.get()` call.

This interface inherits from `AuthenticatorResponse`.

**Note:** This interface is restricted to top-level contexts. Use from within an `<iframe>` element will not have any effect.

## Instance properties

*Also inherits properties from its parent, `AuthenticatorResponse`.*

**`AuthenticatorAssertionResponse.authenticatorData` Read only**

An `ArrayBuffer` containing information from the authenticator such as the Relying Party ID Hash (rpIdHash), a signature counter, test of user presence and user verification flags, and any extensions processed by the authenticator.

**`AuthenticatorResponse.clientDataJSON` Read only**

Contains the JSON-compatible serialization of the data passed from the browser to the authenticator in order to authenticate with this credential — i.e., when `CredentialsContainer.get()` is called with a `publicKey` option. This data contains some information from the options passed into the `get()` call, and some information controlled by the browser.

**`AuthenticatorAssertionResponse.signature` Read only**

An assertion signature over `AuthenticatorAssertionResponse.authenticatorData` and `AuthenticatorResponse.clientDataJSON`. The assertion signature is created with the private key of the key pair that was created during the originating `navigator.credentials.create()` call and verified using the public key of that same key pair.

**`AuthenticatorAssertionResponse.userHandle` Read only**

An `ArrayBuffer` containing an opaque user identifier, specified as `user.id` in the options passed to the originating `navigator.credentials.create()` call.

## Instance methods

None.

## Examples

See Retrieving a public key credential for a detailed example.

## Specifications

| Specification |
|---|
| Web Authentication: An API for accessing Public Key Credentials - Level 3 # iface-authenticatorassertionresponse |

## Browser compatibility
