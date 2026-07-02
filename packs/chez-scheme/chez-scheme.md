---
title: "Chez Scheme"
source: https://en.wikipedia.org/wiki/Chez_Scheme
domain: chez-scheme
license: CC-BY-SA-4.0
tags: chez scheme, kent dybvig, scheme language, r6rs standard, just in time compilation
fetched: 2026-07-02
---

# Chez Scheme

**Chez Scheme** is a programming language, a dialect and implementation of the language Scheme which is a type of Lisp. It uses an incremental native-code compiler to produce native binary files for the x86 (IA-32, x86-64), PowerPC, SPARC, and AArch64 processor architectures.

## History

The first version of Chez Scheme was developed by R. Kent Dybvig and completed in 1984. Some copies of the original version were distributed in 1985.

Cadence Research Systems developed Chez Scheme until the company was purchased by Cisco Systems in 2011. Cisco open-sourced Chez Scheme in 2016.

It has supported the R6RS standard since version 7.9.1. It is free and open-source software released under an Apache License, version 2.0. It was first released in 1985, by R. Kent Dybvig, originally licensed as proprietary software, and then released as open-source software on GitHub on 2016-05-13 with version 9.4.

## Petite Chez Scheme

**Petite Chez Scheme** is a sibling implementation which uses a threaded interpreter design instead of Chez Scheme's incremental native-code compiler. Programs written for Chez Scheme run unchanged in Petite Chez Scheme, as long as they do not depend on using the compiler (for example foreign function interface is only available in the compiler). Petite Chez Scheme was originally freely distributable and is now distributed open-source as part of Chez Scheme.

## Performance

In one series of benchmarks, Chez Scheme was among the fastest available Scheme implementations on the Sun SPARC processor architecture, while Petite Chez Scheme was among the slowest implementations on the more common x86 (Pentium 32-bit) processor architecture.

## Libraries

Chez Scheme has a windowing system and computer graphics package called the Scheme Widget Library, and is supported by the portable SLIB library.. However the widget library is no longer maintained.
