---
title: "Client to Authenticator Protocol"
source: https://en.wikipedia.org/wiki/Client_to_Authenticator_Protocol
domain: webauthn-fido2
license: CC-BY-SA-4.0
tags: webauthn, fido2 authentication, fido alliance, client to authenticator protocol, hardware security key
fetched: 2026-07-02
---

# Client to Authenticator Protocol

The **Client to Authenticator Protocol** (**CTAP**) enables a roaming, user-controlled cryptographic authenticator (such as a smartphone or a hardware security key) to interoperate with a client platform such as a laptop. The standard is also adopted as ITU-T **Recommendation X.1278**.

## Standard

CTAP is complementary to the Web Authentication (WebAuthn) standard published by the World Wide Web Consortium (W3C). WebAuthn and CTAP are the primary outputs of the FIDO2 Project, a joint effort between the FIDO Alliance and the W3C.

CTAP is based upon previous work done by the FIDO Alliance, in particular the Universal 2nd Factor (U2F) authentication standard. Specifically, the FIDO U2F 1.2 Proposed Standard (July 11, 2017) became the starting point for the CTAP Proposed Standard, the latest version 2.2 of which was published on February 28, 2025.

The CTAP specification refers to two protocol versions, the **CTAP1**/U2F protocol and the **CTAP2** protocol. An authenticator that implements CTAP2 is called a FIDO2 authenticator (also called a WebAuthn authenticator). If that authenticator implements CTAP1/U2F as well, it is backward compatible with U2F.

The protocol uses the CBOR binary data serialization format.
