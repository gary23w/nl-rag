---
title: "HTTP Public Key Pinning"
source: https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning
domain: certificate-pinning
license: CC-BY-SA-4.0
tags: certificate pinning, public key pinning, man in the middle defense, trust anchor validation
fetched: 2026-07-02
---

# HTTP Public Key Pinning

**HTTP Public Key Pinning** (**HPKP**) is an obsolete Internet security mechanism delivered via an HTTP header which allows HTTPS websites to resist impersonation by attackers using misissued or otherwise fraudulent digital certificates. A server uses it to deliver to the client (e.g. a web browser) a set of hashes of public keys that must appear in the certificate chain of future connections to the same domain name.

For example, attackers might compromise a certificate authority, and then mis-issue certificates for a web origin. To combat this risk, the HTTPS web server serves a list of “pinned” public key hashes valid for a given time; on subsequent connections, during that validity time, clients expect the server to use one or more of those public keys in its certificate chain. If it does not, an error message is shown, which cannot be (easily) bypassed by the user.

The technique does not pin certificates, but public key hashes. This means that one can use the key pair to get a certificate from any certificate authority, when one has access to the private key. Also the user can pin public keys of root or intermediate certificates (created by certificate authorities), restricting site to certificates issued by the said certificate authority.

Due to HPKP mechanism complexity and possibility of accidental misuse (potentially causing a lockout condition by system administrators), in 2017 browsers deprecated HPKP and in 2018 removed its support in favor of Certificate Transparency.

## Mechanism

The server communicates the HPKP policy to the user agent via an HTTP response header field named `Public-Key-Pins` (or `Public-Key-Pins-Report-Only` for reporting-only purposes).

The HPKP policy specifies hashes of the subject public key info of one of the certificates in the website's authentic X.509 public key certificate chain (and at least one backup key) in `pin-sha256` directives, and a period of time during which the user agent shall enforce public key pinning in `max-age` directive, optional `includeSubDomains` directive to include all subdomains (of the domain that sent the header) in pinning policy and optional `report-uri` directive with URL where to send pinning violation reports. At least one of the public keys of the certificates in the certificate chain needs to match a pinned public key in order for the chain to be considered valid by the user agent.

At the time of publishing, RFC 7469 only allowed the SHA-256 hash algorithm. (Appendix A. of RFC 7469 mentions some tools and required arguments that can be used to produce hashes for HPKP policies.)

A website operator can choose to either pin the root certificate public key of a particular root certificate authority, allowing only that certificate authority (and all intermediate authorities signed by its key) to issue valid certificates for the website's domain, and/or to pin the key(s) of one or more intermediate issuing certificates, or to pin the end-entity public key.

At least one backup key must be pinned, in case the current pinned key needs to be replaced. The HPKP is not valid without this backup key (a backup key is defined as a public key not present in the current certificate chain).

HPKP is standardized in RFC 7469. It expands on static certificate pinning, which hardcodes public key hashes of well-known websites or services within web browsers and applications.

Most browsers disable pinning for certificate chains with private root certificates to enable various corporate content inspection scanners and web debugging tools (such as mitmproxy or Fiddler). The RFC 7469 standard recommends disabling pinning violation reports for "user-defined" root certificates, where it is "acceptable" for the browser to disable pin validation.

## Reporting

If the user agent performs pin validation and fails to find a valid SPKI fingerprint in the served certificate chain, it will POST a JSON formatted violation report to the host specified in the report-uri directive containing details of the violation. This URI may be served via HTTP or HTTPS; however, the user agent cannot send HPKP violation reports to an HTTPS URI in the same domain as the domain for which it is reporting the violation. Hosts may either use HTTP for the `report-uri`, use an alternative domain, or use a reporting service.

Some browsers also support the `Public-Key-Pins-Report-Only`, which only triggers this reporting while not showing an error to the user.

## Criticism and decline

During its peak adoption, HPKP was reported to be used by 3,500 of top 1 million internet sites, a figure that declined to 650 around the end of 2019.

Criticism and concern revolved around malicious or human error scenarios known as HPKP Suicide and RansomPKP. In such scenarios, a website owner would have their ability to publish new contents to their domain severely hampered by either losing access to their own keys or having new keys announced by a malicious attacker.

## Browser support and deprecation

| Browser | Version added | Version deprecated | Version removed | Notes |
|---|---|---|---|---|
| Google Chrome | 46 | 67 | 72 |   |
| Opera | 33 | 54 | 60 |   |
| Firefox | 35 | 72 | 78 |   |
| Internet Explorer | —N/a | —N/a | —N/a |   |
| Microsoft Edge | —N/a | —N/a | —N/a |   |
| Safari | —N/a | —N/a | —N/a |   |
