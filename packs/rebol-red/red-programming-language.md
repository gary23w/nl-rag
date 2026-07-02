---
title: "Red (programming language)"
source: https://en.wikipedia.org/wiki/Red_(programming_language)
domain: rebol-red
license: CC-BY-SA-4.0
tags: rebol language, red language, carl sassenrath, domain specific language, homoiconic language
fetched: 2026-07-02
---

# Red (programming language)

**Red** is a programming language designed to overcome the limits of the programming language Rebol. Red was introduced in 2011 by Nenad Rakočević, and is both an imperative and functional programming language. Its syntax and general usage overlaps that of the interpreted Rebol language.

The implementation choices of Red intend to create a full stack programming language: Red can be used for extremely high-level programming (domain-specific languages (DSLs) and graphical user interfaces (GUIs) and low-level programming (operating systems and device drivers). Key to the approach is that the language has two parts: *Red/System* and *Red*.

- *Red/System* is similar to C, but packaged into a Rebol lexical structure – for example, one would write `if x > y [print "Hello"]` instead of `if (x > y) {printf("Hello\n");}`.
- *Red* is a homoiconic language, which is capable of metaprogramming with Rebol-like semantics. Red's runtime library is written in Red/System, and uses a hybrid approach: it compiles what it can deduce statically and uses an embedded interpreter otherwise. The project roadmap includes a just-in-time compiler for cases in between, but this has not yet been implemented.

Red seeks to remain independent of any other toolchain; it does its own code generation. It is therefore possible to cross-compile Red programs from any platform it supports to any other, via a command-line switch. Both Red and Red/System are distributed as open-source software under the BSD 3-clause (modified) license. The runtime library is distributed under the more permissive Boost Software License.

As of version 0.6.4 Red includes a garbage collector "the Simple GC".

## Introduction

Red was introduced in the Netherlands in February 2011 at the *Rebol & Boron conference* by its author Nenad Rakočević. In September 2011, the Red programming language was presented to a larger audience during the Software Freedom Day 2011. Rakočević is a long-time Rebol developer known as the creator of the Cheyenne HTTP server.

## Features

Red's syntax and semantics are very close to those of Rebol. Like Rebol, it strongly supports metaprogramming and domain-specific languages (DSLs) and is therefore an efficient tool for dialecting (creating embedded DSLs). Red includes a dialect named Red/System, a C-level language which provides systems programming facilities. Red is easy to integrate with other tools and languages as a dynamic-link library (DLL) (libRed) and very lightweight (around 1 MB). It is also able to cross-compile to various platforms (see #Cross compiling section below) and create packages for platforms that require them (e.g., .APK on Android). Red also includes a fully reactive cross-platform GUI system based on an underlying reactive dataflow engine, a 2D drawing dialect comparable to SVG, compile-time and runtime macro support, and more than 40 standard datatypes.

## Goals

The following is the list of Red's Goals as presented on the Software Freedom Day 2011:

- Simplicity ("An IDE should not be necessary to write code.")
- Compactness ("Being highly expressive maximizes productivity.")
- Speed ("If too slow, it cannot be general-purpose enough.")
- Be "Green", Have a Small Footprint ("Because resources are not limitless.")
- Ubiquity ("Spread everywhere.")
- Portability, Write once run everywhere ("That's the least expected from a programming language.")
- Flexibility ("Not best but good fit for any task!")

## Commercial applications

The following commercial applications are currently developed on Red:

- DiaGrammar – Live coded diagramming
- SmartXML – XML parsing tool

## Development

Red's development is planned to be in two phases:

1. Initial phase: Red and Red/System compilers written in Rebol 2
2. Bootstrap phase: Red and Red/System compilers complemented by a Red just-in-time compilation (JIT) compiler, all written in Red.

## Cross compiling

As of 2018, supported cross-compiling targets include:

- DOS: Windows, x86, console (and GUI) applications
- Windows: Windows, x86, GUI applications
- Linux: Linux, x86
- Linux-ARM: Linux, ARMv5, armel (soft-float)
- Raspberry Pi: Linux, ARMv5, armhf (hard-float)
- FreeBSD: x86
- Darwin: macOS Intel, console (and GUI) applications
- Android: Android, ARMv5
- Android-x86: Android, x86

(As of 2018, Red applications are 32-bit. Plans are to move to 64-bit in future.)
