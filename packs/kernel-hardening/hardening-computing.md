---
title: "Hardening (computing)"
source: https://en.wikipedia.org/wiki/Hardening_(computing)
domain: kernel-hardening
license: CC-BY-SA-4.0
tags: linux kernel hardening, kernel self protection, kernel attack surface reduction, kernel address space isolation
fetched: 2026-07-02
---

# Hardening (computing)

In computer security, **hardening** or **system hardening** is usually the process of securing a system by making it a 'hard target' by reducing its attack surface vulnerabilities. The attack surface is larger when a system performs more functions; in principle a single-function system is more secure than a multipurpose one. Hardening is considered an important component of cybersecurity.

Reducing available ways of attack typically includes changing default passwords, the removal of unnecessary software, unnecessary usernames or logins, and the disabling or removal of unnecessary services. It may also involve patching vulnerabilities and switching off ancillary services that are not essential. Hardening measures can also include setting up intrusion prevention systems, disabling or restricting accounts, reducing file system permissions, using encrypted network connections and enabling host-based network security.

## Binary hardening

Binary hardening is a security technique in which binary executables are analyzed and modified to protect against common exploits. Binary hardening is independent of compilers and involves the entire toolchain. For example, one binary hardening technique is to detect potential buffer overflows and to substitute the existing code with safer code. The advantage of manipulating binaries is that vulnerabilities in legacy code can be fixed automatically without the need for source code, which may be unavailable or obfuscated. Secondly, the same techniques can be applied to binaries from multiple compilers, some of which may be less secure than others.

Binary hardening often involves the non-deterministic modification of control flow and instruction addresses so as to prevent attackers from successfully reusing program code to perform exploits. Common hardening techniques are:

- Buffer overflow protection
- Stack overwriting protection
- Position independent executables and address space layout randomization
- Binary stirring (randomizing the address of basic blocks)
- Pointer masking (protection against code injection)
- Control flow randomization (to protect against control flow diversion)
