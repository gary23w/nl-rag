---
title: "FederatedCredential - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/FederatedCredential
domain: credential-management
license: CC-BY-SA-4.0
tags: credential management api, browser credential store, federated credential login, automatic sign-in
fetched: 2026-07-02
---

# FederatedCredential

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`FederatedCredential`** interface of the Credential Management API provides information about credentials from a federated identity provider. A federated identity provider is an entity that a website trusts to correctly authenticate a user, and that provides an API for that purpose. OpenID Connect is an example of a federated identity provider framework.

**Note:** The Federated Credential Management API (FedCM) provides a more complete solution for handling identity federation in the browser, and uses the `IdentityCredential` type.

In browsers that support it, an instance of this interface may be passed in the `credential` member of the `init` object for global `fetch()`.

## Constructor

**`FederatedCredential()`**

Creates a new `FederatedCredential` object.

## Instance properties

*Inherits properties from its ancestor, `Credential`.*

**`FederatedCredential.provider` Read only**

Returns a string containing a credential's federated identity provider.

**`FederatedCredential.protocol` Read only**

Returns a string containing a credential's federated identity protocol.

## Instance methods

None.

## Examples

```js
const cred = new FederatedCredential({
  id,
  name,
  provider: "https://account.google.com",
  iconURL,
});

// Store it
navigator.credentials.store(cred).then(() => {
  // Do something else.
});
```

## Specifications

| Specification |
|---|
| Credential Management Level 1 # federated |

## Browser compatibility
