---
title: "musl"
source: https://en.wikipedia.org/wiki/Musl
domain: apk-alpine-packaging
license: CC-BY-SA-4.0
tags: alpine package keeper, apk package format, musl libc, software repository
fetched: 2026-07-02
---

# musl

**musl** is a C standard library intended for operating systems based on the Linux kernel, released under the MIT License. It was developed by Rich Felker to write a clean, efficient, and standards-conformant libc implementation.

## Overview

musl was designed from scratch to allow efficient static linking and to have realtime-quality robustness by avoiding race conditions, internal failures on resource exhaustion, and various other bad worst-case behaviors present in existing implementations. The dynamic runtime is a single file with stable ABI allowing race-free updates and the static linking support allows an application to be deployed as a single portable binary without significant size overhead.

It claims compatibility with the POSIX 2008 specification and the C11 standard. It also implements most of the widely used non-standard Linux, BSD, and glibc functions. There is partial ABI compatibility with the part of glibc required by Linux Standard Base.

Version 1.2.0 has support for (no longer current) Unicode 12.1.0 (while still having full UTF-8 support, more conformant/strict than glibc), and version 1.2.1 "features the new 'mallocng' malloc implementation, replacing musl's original dlmalloc-like allocator that suffered from fundamental design problems."

## Use

Linux distributions which use musl as their standard C library (some use *only* musl) include but are not limited to:

- Alpine Linux
- Dragora 3
- OpenWrt
- postmarketOS
- Sabotage
- Adélie Linux
- Morpheus Linux
- Chimera Linux
- Void Linux (but not for IA-32)
- KISS Linux

A modified version of musl is available for userspace code written for the seL4 microkernel, requiring users to implement the parts of the Linux system call interface that the subset of musl they wish to use depends on.

Huawei's HarmonyOS NEXT operating system uses a fork of musl as its libc implementation.

For binaries that have been linked against glibc, gcompat and glibmus-hq can be used to execute them on musl-based distros.
