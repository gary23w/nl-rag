---
title: "Integrity (operating system)"
source: https://en.wikipedia.org/wiki/Integrity_(operating_system)
domain: integrity-rtos
license: CC-BY-SA-4.0
tags: integrity rtos, green hills integrity, separation kernel, common criteria eal
fetched: 2026-07-02
---

# Integrity (operating system)

**INTEGRITY** and **INTEGRITY-178B** are real-time operating systems (RTOSes) produced and marketed by Green Hills Software.

## INTEGRITY

INTEGRITY is POSIX-certified and intended for use in embedded systems of 32-bits or 64-bits. Supported computer architectures include variants of: ARM, Blackfin, ColdFire, MIPS, PowerPC, XScale, and x86. INTEGRITY is supported by popular SSL/TLS libraries such as wolfSSL.

## INTEGRITY-178B

INTEGRITY-178B is the DO-178B–compliant version of INTEGRITY. It is used in several military jets such as the B-2, F-16, F-22, and F-35, and the commercial aircraft Airbus A380. Its kernel design guarantees bounded computing times by eliminating features such as dynamic memory allocation.

The auditing and security engineering abilities have allowed it to obtain the Evaluation Assurance Level (EAL) 6 rating by the National Security Agency (NSA). The Target of Evaluation (TOE) Architecture in the Security Target for the evaluation excludes components such as those for file system and networking, from the definition of the TOE, focusing almost solely on the core kernel. Other operating systems, such as Windows, macOS or Linux, though evaluated at lower levels of assurance, generally include these abilities within their TOE.

## Supported processor architectures

The INTEGRITY Architecture Support Package (ASP) provides support for many processor families:

- PowerPC/Power ISA
- AMD and Intel: x86
- ARM Holdings: ARM
- MIPS
