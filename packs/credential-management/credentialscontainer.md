---
title: "CredentialsContainer - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CredentialsContainer
domain: credential-management
license: CC-BY-SA-4.0
tags: credential management api, browser credential store, federated credential login, automatic sign-in
fetched: 2026-07-02
---

# CredentialsContainer

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2019.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`CredentialsContainer`** interface of the Credential Management API exposes methods to request credentials and notify the user agent when events such as successful sign in or sign out happen. This interface is accessible from `Navigator.credentials`.

## Instance properties

None.

## Instance methods

**`CredentialsContainer.create()`**

Returns a `Promise` that resolves with a new `Credential` instance based on the provided options, or `null` if no `Credential` object can be created. In exceptional circumstances, the `Promise` may reject.

**`CredentialsContainer.get()`**

Returns a `Promise` that resolves with the `Credential` instance that matches the provided parameters.

**`CredentialsContainer.preventSilentAccess()`**

Sets a flag that specifies whether automatic log in is allowed for future visits to the current origin, then returns an empty `Promise`. For example, you might call this, after a user signs out of a website to ensure that they aren't automatically signed in on the next site visit. Earlier versions of the spec called this method `requireUserMediation()`. See Browser compatibility for support details.

**`CredentialsContainer.store()`**

Stores a set of credentials for a user, inside a provided `Credential` instance and returns that instance in a `Promise`.

## Specifications

| Specification |
|---|
| Credential Management Level 1 # credentialscontainer |

## Browser compatibility
