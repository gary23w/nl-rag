---
title: "Certificate revocation list"
source: https://en.wikipedia.org/wiki/Certificate_revocation_list
domain: x509-certificates
license: CC-BY-SA-4.0
tags: x.509 certificate, public key certificate, certificate revocation list, cipher suite
fetched: 2026-07-02
---

# Certificate revocation list

In cryptography, a **certificate revocation list** (**CRL**) is "a list of digital certificates that have been revoked by the issuing certificate authority (CA) before their scheduled expiration date and should no longer be trusted".

Publicly trusted CAs in the Web PKI are required (including by the CA/Browser forum) to issue CRLs for their certificates, and they widely do.

Browsers and other relying parties might use CRLs, or might use alternate certificate revocation technologies (such as OCSP) or CRLSets (a dataset derived from CRLs) to check certificate revocation status. Note that OCSP is falling out of favor due to privacy and performance concerns, resulting in a return to CRLs.

Subscribers and other parties can also use ARI.

## Revocation states

There are two different states of revocation:

**Revoked**

A certificate is irreversibly revoked if, for example, it is discovered that the certificate authority (CA) had improperly issued a certificate, or if a private-key is thought to have been compromised. Certificates may also be revoked for failure of the identified entity to adhere to policy requirements, such as publication of false documents, misrepresentation of software behaviour, or violation of any other policy specified by the CA operator or its customer. The most common reason for revocation is the user no longer being in sole possession of the private key (e.g., the token containing the private key has been lost or stolen).

**Hold**

This reversible status can be used to note the temporary invalidity of the certificate (e.g., if the user is unsure if the private key has been lost). If, in this example, the private key was found and nobody had access to it, the status could be reinstated, and the certificate is valid again, thus removing the certificate from future CRLs.

## Reasons for revocation

Reasons to revoke, hold, or unlist a certificate according to RFC 5280 are:

- `unspecified` (0)
- `keyCompromise` (1)
- `cACompromise` (2)
- `affiliationChanged` (3)
- `superseded` (4)
- `cessationOfOperation` (5)
- `certificateHold` (6)
- `removeFromCRL` (8)
- `privilegeWithdrawn` (9)
- `aACompromise` (10)

Note that value 7 is not used.

## Publishing revocation lists

A CRL is generated and published periodically, often at a defined interval. A CRL can also be published immediately after a certificate has been revoked. A CRL is issued by a CRL issuer, which is typically the CA which also issued the corresponding certificates, but could alternatively be some other trusted authority. All CRLs have a lifetime during which they are valid; this timeframe is often 24 hours or less. During a CRL's validity period, it may be consulted by a PKI-enabled application to verify a certificate prior to use.

To prevent spoofing or denial-of-service attacks, CRLs usually carry a digital signature associated with the CA by which they are published. To validate a specific CRL prior to relying on it, the certificate of its corresponding CA is needed.

The certificates for which a CRL should be maintained are often X.509/public key certificates, as this format is commonly used by PKI schemes.

## Revocation versus expiration

Expiration dates are not a substitute for a CRL. While all expired certificates are considered invalid, not all unexpired certificates should be valid. CRLs or other certificate validation techniques are a necessary part of any properly operated PKI, as mistakes in certificate vetting and key management are expected to occur in real world operations.

In a noteworthy example, a certificate for Microsoft was mistakenly issued to an unknown individual, who had successfully posed as Microsoft to the CA contracted to maintain the ActiveX 'publisher certificate' system (VeriSign). Microsoft saw the need to patch their cryptography subsystem so it would check the status of certificates before trusting them. As a short-term fix, a patch was issued for the relevant Microsoft software (most importantly Windows) specifically listing the two certificates in question as "revoked".

## Problems with certificate revocation lists

Best practices require that wherever and however certificate status is maintained, it must be checked whenever one wants to rely on a certificate. Failing this, a revoked certificate may be incorrectly accepted as valid. This means that to use a PKI effectively, one must have access to current CRLs. This requirement of on-line validation negates one of the original major advantages of PKI over symmetric cryptography protocols, namely that the certificate is "self-authenticating". Symmetric systems such as Kerberos also depend on the existence of on-line services (a key distribution center in the case of Kerberos).

The existence of a CRL implies the need for someone (or some organization) to enforce policy and revoke certificates deemed counter to operational policy. If a certificate is mistakenly revoked, significant problems can arise. As the certificate authority is tasked with enforcing the operational policy for issuing certificates, they typically are responsible for determining if and when revocation is appropriate by interpreting the operational policy.

The necessity of consulting a CRL (or other certificate status service) prior to accepting a certificate raises a potential denial-of-service attack against the PKI. If acceptance of a certificate fails in the absence of an available valid CRL, then no operations depending upon certificate acceptance can take place. This issue exists for Kerberos systems as well, where failure to retrieve a current authentication token will prevent system access.

An alternative to using CRLs is the certificate validation protocol known as Online Certificate Status Protocol (OCSP). OCSP has the primary benefit of requiring less network bandwidth, enabling real-time and near real-time status checks for high volume or high-value operations.

As of Firefox 28, Mozilla has announced they are deprecating CRL in favour of OCSP.

CRL files may grow quite large over time e.g. in US government, for certain institution multiple megabytes. Therefore, incremental CRLs have been designed sometimes referred to as "delta CRLs". However, only a few clients implement them.

## Authority revocation lists

An *authority revocation list* (ARL) is a form of CRL containing revoked certificates issued to certificate authorities, contrary to CRLs which contain revoked end-entity certificates.
