---
title: "Trust anchor"
source: https://en.wikipedia.org/wiki/Root_of_trust
domain: secure-boot-measured
license: CC-BY-SA-4.0
tags: measured boot integrity, boot chain of trust, platform configuration register, trusted boot measurement
fetched: 2026-07-02
---

# Trust anchor

(Redirected from

Root of trust

)

In cryptographic systems with hierarchical structure, a **trust anchor** is an authoritative entity for which trust is assumed and not derived.

In the X.509 architecture, a root certificate would be the trust anchor from which the whole chain of trust is derived. The trust anchor must be in the possession of the trusting party beforehand to make any further certificate path validation possible.

Most operating systems provide a built-in list of self-signed root certificates to act as trust anchors for applications. The Firefox web browser also provides its own list of trust anchors. The end-user of an operating system or web browser is implicitly trusting in the correct operation of that software, and the software manufacturer in turn is delegating trust for certain cryptographic operations to the certificate authorities responsible for the root certificates.
