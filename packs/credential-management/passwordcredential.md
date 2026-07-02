---
title: "PasswordCredential - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PasswordCredential
domain: credential-management
license: CC-BY-SA-4.0
tags: credential management api, browser credential store, federated credential login, automatic sign-in
fetched: 2026-07-02
---

# PasswordCredential

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`PasswordCredential`** interface of the Credential Management API provides information about a username/password pair. In supporting browsers an instance of this class may be passed in the `credential` member of the `init` object for global `fetch()`.

**Note:** This interface is restricted to top-level contexts and cannot be used from an `<iframe>`.

## Constructor

**`PasswordCredential()`**

Creates a new `PasswordCredential` object.

## Instance properties

*Inherits properties from its ancestor, `Credential`.*

**`PasswordCredential.iconURL` Read only**

A string containing a URL pointing to an image for an icon. This image is intended for display in a credential chooser. The URL must be accessible without authentication.

**`PasswordCredential.name` Read only**

A human-readable string that provides public name for display in a credential chooser.

**`PasswordCredential.password` Read only**

A string containing the password of the credential.

## Instance methods

None.

## Examples

```js
const cred = new PasswordCredential({
  id,
  password,
  name,
  iconURL,
});

navigator.credentials.store(cred).then(() => {
  // Do something else.
});
```

## Specifications

| Specification |
|---|
| Credential Management Level 1 # passwordcredential-interface |

## Browser compatibility
