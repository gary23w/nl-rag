---
title: "Certificate Transparency"
source: https://en.wikipedia.org/wiki/Certificate_Transparency
domain: certificate-transparency
license: CC-BY-SA-4.0
tags: certificate transparency log, merkle tree audit log, public key certificate monitoring, certificate authority accountability, misissued certificate detection
fetched: 2026-07-02
---

# Certificate Transparency

**Certificate Transparency** (**CT**) is an Internet security standard for monitoring and auditing the issuance of digital certificates. When an internet user interacts with a website, a trusted third party is needed for assurance that the website is legitimate and that the website's encryption key is valid. This third party, called a certificate authority (CA), will issue a certificate for the website that the user's browser can validate. The security of encrypted internet traffic depends on the trust that certificates are only given out by the certificate authority and that the certificate authority has not been compromised.

Certificate Transparency makes public all issued certificates in the form of a distributed ledger, giving website owners and auditors the ability to detect and expose inappropriately issued certificates.

Work on Certificate Transparency first began in 2011 after the certificate authority DigiNotar became compromised and started issuing malicious certificates. Google engineers submitted a draft to the Internet Engineering Task Force (IETF) in 2012. This effort resulted in IETF RFC 6962, a standard defining a system of public logs to record all certificates issued by publicly trusted certificate authorities, allowing efficient identification of mistakenly or maliciously issued certificates.

## Technical overview

The certificate transparency system consists of a system of append-only certificate logs. Logs are operated by many parties, including browser vendors and certificate authorities. Certificates that support certificate transparency must include one or more *signed certificate timestamps* (SCTs), which is a promise from a log operator to include the certificate in their log within a *maximum merge delay* (MMD). At some point within the maximum merge delay, the log operator adds the certificate to their log. Each entry in a log references the hash of a previous one, forming a Merkle tree. The *signed tree head* (STH) references the current root of the Merkle tree.

### Logging procedure

Although anyone can submit a certificate to a CT log, this task is commonly carried out by a CA as follows:

1. An applicant, "The natural person or Legal Entity that applies for (or seeks renewal of) a Certificate", requests a certificate from a CA.
2. The CA issues a special *precertificate*, a certificate which carries a poison extension signaling that it should not be accepted by user agents.
3. The CA sends the precertificate to logs.
4. Logs return corresponding SCTs to the CA.
5. The CA attaches SCTs collected from logs as an X.509 extension to the final certificate and provides it to the applicant.

Finally, the CA may decide to log the final certificate as well. Let's Encrypt E1 CA, for example, logs both precertificates and final certificates (see CA crt.sh profile page under 'issued certificates' section), whereas Google GTS CA 2A1 does not (see crt.sh profile page).

### Mandatory certificate transparency

Some browsers require Transport Layer Security (TLS) certificates to have proof of being logged with certificate transparency, either through SCTs embedded into the certificate, an extension during the TLS handshake, or through OCSP:

| Browser | Current SCT requirements | Current OCSP/TLS extension requirements |
|---|---|---|
| Chrome/Chromium | One SCT from a currently approved log Duration ≤ 180 days: 2 SCTs from once-approved logs Duration > 180 days: 3 SCTs from once-approved logs | 1 SCT from a current Google log 1 SCT from a current non-Google log |
| Firefox | desktop: 2 SCTs from once-approved logs, since v135 (released 2025-02-04) Firefox for Android: 2 SCTs from once-approved logs, since v145 (released 2025-11-11) | Two SCTs from currently approved logs |
| Safari | One SCT from a currently approved log Duration ≤ 180 days: 2 SCTs from once-approved logs Duration > 180 days: 3 SCTs from once-approved logs | Two SCTs from currently approved logs |

- NOTE: Apple platforms that use system libraries for TLS enforce CT for free on **any** TLS connection (not just Safari).

### Log sharding

Due to the large quantities of certificates issued with the Web PKI, certificate transparency logs can grow to contain many certificates. This large quantity of certificates can cause strain on logs. Temporal sharding is a method to reduce the strain on logs by sharding a log into multiple logs, and having each shard only accept precertificates and certificates with an expiration date in a particular time period (usually a calendar year). Cloudflare's Nimbus series of logs was the first to use temporal sharding.

## Background

### Advantages

One of the problems with digital certificate management is that fraudulent certificates take a long time to be spotted, reported and revoked. An issued certificate not logged using Certificate Transparency may never be spotted at all. The main advantage with Certificate Transparency is the ability for cyber security teams to defend companies and organisations by monitoring for suspicious domains registering certificates. The new certificates for these suspicious domains may have similar names to other legitimate domains and are designed to be used to support malicious activities such as phishing attacks. Certificate Transparency puts cyber security teams in control and enables them to issue domain take down orders for suspicious domains and allows them to apply cyber security controls on web proxies and email gateways for immediate protection.

### Side Effects

Domain names that are used on internal networks and have certificates issued by certificate authorities become publicly searchable as their certificates are added to CT logs.

### Certificate Transparency logs

Certificate Transparency depends on verifiable Certificate Transparency logs. A log appends new certificates to an ever-growing Merkle hash tree. To be seen as behaving correctly, a log must:

- Verify that each submitted certificate or precertificate has a valid signature chain leading back to a trusted root certificate authority certificate.
- Refuse to publish certificates without this valid signature chain.
- Store the entire verification chain from the newly accepted certificate back to the root certificate.
- Present this chain for auditing upon request.

A log may accept certificates that are not yet fully valid and certificates that have expired.

### Certificate Transparency monitors and auditors

There are two primary categories of monitors: log integrity monitors (also referred to as log verifiers or log auditors) and tracking monitors. Some companies offering monitoring services collect data from all logs and provide paid services for domain tracking. For example, a domain owner can register for Cloudflare's services, which globally monitor all logs and send email updates whenever a certificate is issued for their domain, allowing them control over all certificates issued.

Large organizations can maintain their own monitors, which continuously scan for new certificate issued for their domains. If a certificate authority (CA) attempts to issue a "bad" certificate for one of these domains (intentionally or unintentionally), the monitor will quickly detect it. Two popular APIs for research and tracking are Sectigo's crt.sh and Cloudflare MerkleTown. These tools facilitate the monitoring of certificate issuance and help organizations stay on top of the security of their domains.

While there is an additional consideration of monitoring the monitors themselves, the likelihood of a significant impact on system performance or security due to misbehavior of a single monitor is low. This is because there are numerous log monitors, providing a layered approach to security and minimizing the risk of a single point of failure.

### Certificate Transparency log programs

Apple and Google have separate log programs with distinct policies and lists of trusted logs.

### Root stores of Certificate Transparency logs

Certificate Transparency logs maintain their own root stores and only accept certificates that chain back to the trusted roots. A number of misbehaving logs have been publishing inconsistent root stores in the past.

## Static CT API

A new structure for logs is based on dividing the Merkle Tree into tiles. This structure is expected to be faster, easier to operate, and to provide much smaller merge delays (the current Maximum Merge Delay is 24 hours). Chrome has updated its Certificate Transparency (CT) policy to accept SCTs from the new static-CT-API logs only if an SCT from an RFC 6962 log is also present, and it intends to complete the migration to static-CT-API CT logs by the end of 2025.

## History

In 2011, a reseller of the certificate authority Comodo was attacked and the certificate authority DigiNotar was compromised, demonstrating existing flaws in the certificate authority ecosystem and prompting work on various mechanisms to prevent or monitor unauthorized certificate issuance. Google employees Ben Laurie, Adam Langley and Emilia Kasper began work on an open source framework for detecting mis-issued certificates the same year. In 2012, they submitted the first draft of the standard to IETF under the code-name "Sunlight".

In March 2013, Google launched its first certificate transparency log.

In June 2013, RFC 6962 "Certificate Transparency" was published, based on the 2012 draft.

In September 2013, DigiCert became the first certificate authority to implement Certificate Transparency.

In 2015, Google Chrome began requiring Certificate Transparency for newly issued Extended Validation Certificates. It began requiring Certificate Transparency for all certificates newly issued by Symantec from June 1, 2016, after they were found to have issued 187 certificates without the domain owners' knowledge. Since April 2018, this requirement has been extended to all certificates.

On March 23, 2018, Cloudflare announced its own CT log named *Nimbus*.

In May 2019, certificate authority Let's Encrypt launched its own CT log called Oak. Since February 2020, it is included in approved log lists and is usable by all publicly trusted certificate authorities.

In December 2021, RFC 9162 "Certificate Transparency Version 2.0" was published. Version 2.0 includes major changes to the required structure of the log certificate, as well as support for Ed25519 as a signature algorithm of SCTs and support for including certificate inclusion proofs with the SCT. However, it has not seen industry adoption and is considered dead on arrival.

In February 2022, Google published an update to their CT policy, which removes the requirement for certificates to include a SCT from their own CT log service, matching all the requirements for certificates to those previously published by Apple.

In February 2025, Mozilla Firefox desktop version 135 began requiring Certificate Transparency for all certificates issued by a certificate authority in Mozilla's Root CA Program.

## Signature algorithms

In Certificate Transparency Version 2.0, a log must use one of the algorithms in the IANA registry "Signature Algorithms".

## Tools for inspecting CT logs

- crt.sh by Sectigo
- Censys Search by Censys
- Cert Spotter by sslmate
- certstream.calidog.io
- ct.cloudflare.com - Merkle Town by Cloudflare
- Meta Certificate Transparency Monitoring by Meta
- Merklemap
- Certificate Transparency Root Explorer
- EZMonitor by Keytos
- CertObserver Certificate Transparency search
