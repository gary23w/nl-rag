---
title: "Self-signed certificate"
source: https://en.wikipedia.org/wiki/Self-signed_certificate
domain: x509-certificates
license: CC-BY-SA-4.0
tags: x.509 certificate, certificate signing request, certificate transparency, extended validation certificate, wildcard certificate
fetched: 2026-07-02
---

# Self-signed certificate

In cryptography and computer security, **self-signed certificates** are public key certificates that are not issued by a certificate authority (CA). These self-signed certificates are easy to make and do not cost money. However, they do not provide any trust value.

For instance, if a website owner uses a self-signed certificate to provide HTTPS services, people who visit that website cannot be certain that they are connected to their intended destination. For all they know, a malicious third-party could be redirecting the connection using another self-signed certificate bearing the same holder name. The connection is still encrypted, but does not necessarily lead to its intended target. In comparison, a certificate signed by a trusted CA prevents this attack because the user's web browser separately validates the certificate against the issuing CA. The attacker's certificate fails this validation.

## Benefits

Self-signed certificates can be created for free, using a wide variety of tools including OpenSSL, Java's keytool, Adobe Reader, wolfSSL and Apple's Keychain. They are easy to customize; e.g, they can have larger key sizes or hold additional metadata. Their use doesn't involve the problems of trusting third parties that may improperly sign certificates. Self-signed certificate transactions usually present a far smaller attack surface by eliminating both the complex certificate chain validation, and certificate revocation checks like CRL and OCSP.

## Trust issues

In a CA-based PKI system, parties engaged in secure communication must trust a CA, i.e. place the CA certificates in a whitelist of trusted certificates. Developers of web browsers may use procedures specified by the CA/Browser Forum to whitelist well-known, public certificate authorities. Individual groups and companies may whitelist additional, private CA certificates. The trust issues of an entity accepting a new self-signed certificate are similar to the issues of an entity trusting the addition of a new CA certificate. The parties in a self-signed PKI must establish trust with each other (using procedures outside the PKI), and confirm the accurate transfer of public keys e.g. compare the certificate's cryptographic hash out of band.

There are many subtle differences between CA signed and self-signed certificates, especially in the amount of trust that can be placed in the security assertions of the certificate. Some CAs can verify the identity of the person to whom they issue a certificate; for example the US military issues their Common Access Cards in person, with multiple forms of other ID. The CA can attest identity values like these by including them in the signed certificate. The entity that validates the certificate can trust the information in that certificate, to the same extent that they trust the CA that signed it (and by implication, the security procedures the CA used to verify the attested information).

With a self-signed certificate by contrast, trust of the values in the certificate are more complicated because the entity possesses the signing key, and can always generate a new certificate with different values. For example, the validity dates of a self-signed certificate might not be trusted because the entity could always create and sign a new certificate that contained a valid date range.

The values in a self-signed certificate can only be trusted when the values were verified out-of-band during the acceptance of the certificate, and there is a method to verify the self-signed certificate has not changed after it was trusted. For example, the procedure of trusting a self-signed certificate includes a manual verification of validity dates, and a hash of the certificate is incorporated into the white list. When the certificate is presented for an entity to validate, they first verify the hash of the certificate matches the reference hash in the white-list, and if they match (indicating the self-signed certificate is the same as the one that was formerly trusted) then the certificate's validity dates can be trusted. Special treatment of X.509 certificate fields for self-signed certificate can be found in RFC 3280.

Revocation of self-signed certificates differs from CA-signed certificates. By nature, no entity (CA or others) can revoke a self-signed certificate. But one could invalidate a self-signed CA by removing it from the trust whitelist.

## Uses

Self-signed certificates have limited uses, e.g. in the cases where the issuer and the sole user are the same entity. For example, the Encrypting File System on Microsoft Windows issues a self-signed certificate on behalf of a user account to transparently encrypt and decrypt files on the fly. Another example is a root certificate, which is a form of self-signed certificate.

## Name confusion

The terms "self-signed" and "self-issued" are occasionally used interchangeably and "self-signed certificate" is sometimes even incorrectly used to indicate a certificate issued by a private (not publicly trusted) CA.

RFC 5280 defines self-signed certificates as "self-issued certificates where the digital signature may be verified by the public key bound into the certificate", whereas a self-issued certificate is a certificate "in which the issuer and subject are the same entity". While in the strict sense the RFC makes this definition only for CA certificates, there is no reason to also adopt that definition for end-entity certificates.
