---
title: "X.509"
source: https://cryptography.io/en/latest/x509/
domain: cryptography-pyca
license: CC-BY-SA-4.0
tags: python cryptography, pyca cryptography library, encryption python
fetched: 2026-07-02
---

# X.509

X.509 is a standard for public key infrastructure. `cryptography` implements X.509 in accordance with **RFC 5280**, and is principally focused on WebPKI use cases. X.509 certificates are commonly used in protocols like TLS.

In some cases we tolerate divergences from the these specifications, however these should be regarded as exceptional cases.

- Tutorial
  - Creating a Certificate Signing Request (CSR)
  - Creating a self-signed certificate
  - Creating a CA hierarchy
  - Determining Certificate or Certificate Signing Request Key Type
- Certificate Transparency
  - `SignedCertificateTimestamp`
  - `Version`
  - `LogEntryType`
  - `SignatureAlgorithm`
- OCSP
  - Loading Requests
  - Creating Requests
  - Loading Responses
  - Creating Responses
  - Interfaces
- X.509 Verification
  - `Store`
  - `Subject`
  - `VerifiedClient`
  - `ClientVerifier`
  - `ServerVerifier`
  - `VerificationError`
  - `PolicyBuilder`
  - `ExtensionPolicy`
  - `Criticality`
  - `Policy`
  - `MaybeExtensionValidatorCallback`
  - `PresentExtensionValidatorCallback`
- X.509 Reference
  - Loading Certificates
  - Loading Certificate Revocation Lists
  - Loading Certificate Signing Requests
  - X.509 Certificate Object
  - X.509 CRL (Certificate Revocation List) Object
  - X.509 Certificate Builder
  - X.509 CSR (Certificate Signing Request) Object
  - X.509 Certificate Revocation List Builder
  - X.509 Revoked Certificate Object
  - X.509 Revoked Certificate Builder
  - X.509 CSR (Certificate Signing Request) Builder Object
  - General Name Classes
  - X.509 Extensions
  - Certificate Policies Classes
  - Admissions Classes
  - CRL Entry Extensions
  - OCSP Extensions
  - X.509 Request Attributes
  - Object Identifiers
  - Helper Functions
  - Exceptions
