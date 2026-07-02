---
title: "Credential Management API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Credential_Management_API
domain: credential-management
license: CC-BY-SA-4.0
tags: credential management api, browser credential store, federated credential login, automatic sign-in
fetched: 2026-07-02
---

# Credential Management API

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The Credential Management API enables a website to create, store, and retrieve credentials. A credential is an item which enables a system to make an authentication decision: for example, to decide whether to sign a user into an account. We can think of it as a piece of evidence that a user presents to a website to demonstrate that they really are the person they are claiming to be.

## Concepts and usage

The central interface is the `CredentialsContainer`, which is accessed through the `navigator.credentials` property and provides three main functions:

- `create()`: create a new credential.
- `store()`: store a new credential locally.
- `get()`: retrieve a credential, which can then be used to log a user in.

The API supports four different types of credential, which are all represented as subclasses of `Credential`:

| Type | Interface |
|---|---|
| Password | `PasswordCredential` |
| Federated identity | `IdentityCredential`, `FederatedCredential` (deprecated) |
| One-time password (OTP) | `OTPCredential` |
| Web Authentication | `PublicKeyCredential` |

The guide page Credential types gives an overview of the different credential types and how they are used.

## Interfaces

**`Credential`**

Provides information about an entity as a prerequisite to a trust decision.

**`CredentialsContainer`**

Exposes methods to request credentials and notify the user agent when interesting events occur such as successful sign in or sign out. This interface is accessible from `navigator.credentials`.

**`FederatedCredential`**

Provides information about credentials from a federated identity provider, which is an entity that a website trusts to correctly authenticate a user, and which provides an API for that purpose. OpenID Connect is an example of such a framework.

**`PasswordCredential`**

Provides information about a username/password pair.

### Extensions to other interfaces

**`Navigator.credentials` Read only**

Returns the `CredentialsContainer` interface which exposes methods to request credentials and notify the user agent when interesting events occur such as successful sign in or sign out.

## Specifications

| Specification |
|---|
| Credential Management Level 1 |

## Browser compatibility

### api.Credential

### api.CredentialsContainer

### api.FederatedCredential

### api.PasswordCredential
