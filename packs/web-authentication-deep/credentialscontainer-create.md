---
title: "CredentialsContainer: create() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CredentialsContainer/create
domain: web-authentication-deep
license: CC-BY-SA-4.0
tags: web authentication ceremony, public key credential, authenticator attestation, assertion signature verify
fetched: 2026-07-02
---

# CredentialsContainer: create() method

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2019.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`create()`** method of the `CredentialsContainer` interface creates a new credential, which can then be stored and later retrieved using the `navigator.credentials.get()` method. The retrieved credential can then be used by a website to authenticate a user.

This method supports three different types of credential:

- A password credential, which enables a user to sign in using a password.
- A federated credential, which enables a user to sign in using a federated identity provider.
- A public key credential, which enables a user to sign in with an authenticator such as a biometric reader built into the platform or a removable hardware token.

Note that the Federated Credential Management API (FedCM) supersedes the federated credential type.

## Syntax

```js
create()
create(options)
```

### Parameters

**`options` Optional**

An object that contains options for the requested new `Credentials` object. It can contain the following properties:

**`signal` Optional**

An `AbortSignal` object instance that allows an ongoing `create()` operation to be aborted. An aborted operation may complete normally (generally if the abort was received after the operation finished) or reject with an `AbortError` `DOMException`.

Each of the following properties represents a *credential type* being created. One and only one of them must be specified:

**`federated` Optional**

A `FederatedCredentialInit` object containing requirements for creating a federated identify provider credential.

**`password` Optional**

A `PasswordCredentialInit` object containing requirements for creating a password credential.

**`publicKey` Optional**

A `PublicKeyCredentialCreationOptions` object containing requirements for creating a public key credential. Causes the `create()` call to request that the user agent creates new credentials via an authenticator — either for registering a new account or for associating a new asymmetric key pair with an existing account.

**Note:** Usage of `create()` with the `publicKey` parameter may be blocked by a `publickey-credentials-create` Permissions Policy set on your server.

### Return value

A `Promise` that resolves with one of the following:

- A `FederatedCredential`, if the credential type was `federated`.
- A `PasswordCredential`, if the credential type was `password`.
- A `PublicKeyCredential`, if the credential type was `publicKey`.

If no credential object can be created, the promise resolves with `null`.

### Exceptions

**`TypeError`**

In the case of a `PasswordCredential` creation request, `id`, `origin`, or `password` were not provided (empty).

**`NotAllowedError` `DOMException`**

Possible causes include:

- Usage was blocked by a `publickey-credentials-create` Permissions Policy.
- The function is called cross-origin but the iframe's `allow` attribute does not set an appropriate `publickey-credentials-create` policy.
- The function is called cross-origin and the `<iframe>` does not have transient activation.
- The function tried to create a discoverable credential (`residentKey` is set to `required` in the `create()` call's `PublicKeyCredentialCreationOptions` option), but the user does not have an authenticator that supports discoverable credentials.

**`AbortError` `DOMException`**

The operation was aborted.

## Examples

### Creating a password credential

This example creates a password credential from a `PasswordCredentialInit` object.

```js
const credInit = {
  id: "serpent1234", // "username" in a typical username/password pair
  name: "Serpentina", // display name for credential
  origin: "https://example.org",
  password: "the last visible dog",
};

const makeCredential = document.querySelector("#make-credential");

makeCredential.addEventListener("click", async () => {
  const cred = await navigator.credentials.create({
    password: credInit,
  });
  console.log(cred.name);
  // Serpentina
  console.log(cred.id);
  // serpent1234
  console.log(cred.password);
  // the last visible dog
});
```

### Creating a federated credential

This example creates a federated credential from a `FederatedCredentialInit` object.

```js
const credInit = {
  id: "1234",
  name: "Serpentina",
  origin: "https://example.org",
  protocol: "openidconnect",
  provider: "https://provider.example.org",
};

const makeCredential = document.querySelector("#make-credential");

makeCredential.addEventListener("click", async () => {
  const cred = await navigator.credentials.create({
    federated: credInit,
  });
  console.log(cred.name);
  console.log(cred.provider);
});
```

### Creating a public key credential

This example creates a public key credential from a `PublicKeyCredentialCreationOptions` object.

```js
const publicKey = {
  challenge: challengeFromServer,
  rp: { id: "acme.com", name: "ACME Corporation" },
  user: {
    id: new Uint8Array([79, 252, 83, 72, 214, 7, 89, 26]),
    name: "jamiedoe",
    displayName: "Jamie Doe",
  },
  pubKeyCredParams: [{ type: "public-key", alg: -7 }],
};

const publicKeyCredential = await navigator.credentials.create({ publicKey });
```

The `create()` call, if successful, returns a promise that resolves with a `PublicKeyCredential` object instance, representing a public key credential that can later be used to authenticate a user via a WebAuthn `get()` call. Its `PublicKeyCredential.response` property contains an `AuthenticatorAttestationResponse` object providing access to several useful pieces of information including the authenticator data, public key, transport mechanisms, and more.

```js
navigator.credentials.create({ publicKey }).then((publicKeyCredential) => {
  const response = publicKeyCredential.response;

  // Access attestationObject ArrayBuffer
  const attestationObj = response.attestationObject;

  // Access client JSON
  const clientJSON = response.clientDataJSON;

  // Return authenticator data ArrayBuffer
  const authenticatorData = response.getAuthenticatorData();

  // Return public key ArrayBuffer
  const pk = response.getPublicKey();

  // Return public key algorithm identifier
  const pkAlgo = response.getPublicKeyAlgorithm();

  // Return permissible transports array
  const transports = response.getTransports();
});
```

Some of this data will need to be stored on the server for future authentication operations against this credential — for example the public key, the algorithm used, and the permissible transports.

**Note:** See Creating a key pair and registering a user for more information about how the overall flow works.

## Specifications

| Specification |
|---|
| Credential Management Level 1 # dom-credentialscontainer-create |

## Browser compatibility
