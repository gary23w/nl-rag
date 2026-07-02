---
title: "Root certificate"
source: https://en.wikipedia.org/wiki/Root_certificate
domain: hsm-key-ceremony
license: CC-BY-SA-4.0
tags: hardware security module, key ceremony procedure, root key generation, dnssec key signing, trust anchor provisioning
fetched: 2026-07-02
---

# Root certificate

In cryptography and computer security, a **root certificate** is a public key certificate that identifies a root certificate authority (CA). Root certificates are self-signed (and it is possible for a certificate to have multiple trust paths, say if the certificate was issued by a root that was cross-signed) and form the basis of an X.509-based public key infrastructure (PKI). Either it has matched Authority Key Identifier with Subject Key Identifier, in some cases there is no Authority Key identifier, then Issuer string should match with Subject string (RFC 5280). For instance, the PKIs supporting HTTPS for secure web browsing and electronic signature schemes depend on a set of root certificates.

A certificate authority can issue multiple certificates in the form of a tree structure. A root certificate is the top-most certificate of the tree, the private key which is used to "sign" other certificates. All certificates signed by the root certificate, with the "CA" field set to true, inherit the trustworthiness of the root certificate—a signature by a root certificate is somewhat analogous to "notarizing" identity in the physical world. Such a certificate is called an intermediate certificate or subordinate CA certificate. Certificates further down the tree also depend on the trustworthiness of the intermediates.

The root certificate is usually made trustworthy by some mechanism other than a certificate, such as by secure physical distribution. For example, some of the best-known root certificates are distributed in operating systems by their manufacturers. Microsoft distributes root certificates belonging to members of the Microsoft Root Certificate Program to Windows desktops and Windows Phone 8. Apple distributes root certificates belonging to members of its own root program.

## Incidents of root certificate misuse

### DigiNotar hack of 2011

In 2011, the Dutch certificate authority DigiNotar suffered a security breach. This led to the issuing of various fraudulent certificates, which was among others abused to target Iranian Gmail users. The trust in DigiNotar certificates was retracted and the operational management of the company was taken over by the Dutch government.

### China Internet Network Information Center (CNNIC) issuance of fake certificates

In 2009, an employee of the China Internet Network Information Center (CNNIC) applied to Mozilla to add CNNIC to Mozilla's root certificate list and was approved. Later, Microsoft also added CNNIC to the root certificate list of Windows.

In 2015, many users chose not to trust the digital certificates issued by CNNIC because an intermediate CA issued by CNNIC was found to have issued fake certificates for Google domain names and raised concerns about CNNIC's abuse of certificate issuing power.

On April 2, 2015, Google announced that it no longer recognized the electronic certificate issued by CNNIC. On April 4, following Google, Mozilla also announced that it no longer recognized the electronic certificate issued by CNNIC.

### WoSign and StartCom: Issuing fake and backdated certificates

In 2016, WoSign, China's largest CA certificate issuer owned by Qihoo 360 and its Israeli subsidiary StartCom, were denied recognition of their certificates by Google. Microsoft removed the relevant certificates in 2017.

WoSign and StartCom issued hundreds of certificates with the same serial number in just five days, as well as issuing backdated certificates. In 2016, a system administrator in Florida was able to get WoSign and StartCom to issue fake certificates for multiple GitHub domains.
