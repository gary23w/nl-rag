---
title: "Domain-validated certificate"
source: https://en.wikipedia.org/wiki/Domain_validation
domain: acme-protocol
license: CC-BY-SA-4.0
tags: acme protocol, automated certificate issuance, lets encrypt automation, domain validation challenge, certificate renewal automation
fetched: 2026-07-02
---

# Domain-validated certificate

(Redirected from

Domain validation

)

A **domain validated certificate** (**DV**) is an X.509 public key certificate typically used for Transport Layer Security (TLS) where the domain name of the applicant is validated by proving some control over a DNS domain. Domain validated certificates were first distributed by GeoTrust in 2002 before becoming a widely accepted method.

## Issuing criteria

The sole criterion for a domain validated certificate is proof of control over whois records, DNS records file, email or web hosting account of a domain. Typically control over a domain is determined using one of the following:

- Response to email sent to the email contact in the domain's whois details
- Response to email sent to a well-known administrative contact in the domain, e.g. (admin@, postmaster@, etc.)
- Publishing a DNS TXT record
- Publishing a nonce provided by an automated certificate issuing system

A domain validated certificate is distinct from an Extended Validation Certificate in that this is the only requirement for issuing the certificate. In particular, domain validated certificates do not assure that any particular legal entity is connected to the certificate, even if the domain name may imply a particular legal entity controls the domain.

## User interface

As of 2020, all major browsers user interfaces display EV, OV, and DV certificates identically, but provide options to query the type of certificate via multiple clicks.

## Characteristics

As the low assurance requirements allow domain validated certificates to be issued quickly without requiring human intervention, domain validated certificates have a number of unique characteristics:

- Domain validated certificates are used in automated X.509 certificate issuing systems, such as Let's Encrypt.
- Domain validated certificates are often cheap or free.
- Domain validated certificates can be generated and validated without any documentation.
- Most domain validated certificates can be issued instantly (in less than a minute) via special tools which automate issuing process.
