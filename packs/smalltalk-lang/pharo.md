---
title: "Pharo"
source: https://en.wikipedia.org/wiki/Pharo
domain: smalltalk-lang
license: CC-BY-SA-4.0
tags: smalltalk language, smalltalk lang, pharo smalltalk, squeak smalltalk
fetched: 2026-07-02
---

# Pharo

**Pharo** is a cross-platform implementation of the classic Smalltalk-80 programming language and runtime system. It is based on the OpenSmalltalk virtual machine (VM) named Cog, which evaluates a dynamic, reflective, and object-oriented programming language with a syntax closely resembling Smalltalk-80. It is free and open-source software, released under a mix of MIT, and Apache 2 licenses.

Pharo is shipped with source code compiled into a *system image* that contains all software needed to run Pharo. Like the original Smalltalk-80, Pharo provides several live programming features such as immediate object manipulation, live updates, and just-in-time compilation (JIT). The system image includes an integrated development environment (IDE) to modify its components.

Pharo was forked from Squeak v3.9 in March 2008.

## Overview

Pharo is a pure object-oriented, dynamically typed, and reflective language. The stated project goal is to revisit Smalltalk design and enhance it.

The name Pharo comes from the French word "phare" (French pronunciation: [faʁ]) which means lighthouse. This is why the Pharo logo shows a drawing of a lighthouse inside the final letter *O* of the name.

## Key features

### Virtual machine

- Multiplatform virtual machine with just-in-time compilation (JIT), combined generational garbage collector, ephemerons, forwarders
- Fast object enumeration
- Easy call stack manipulation
- AST metalinks
- Relatively low memory consumption
- Customizable compiler
- Optional complete object memory persistence
- Resumable exceptions
- Fast object serialization

### Built-in software

- Optional fusion of developed program and development environment
- Live object inspection

### Language features

- Simple syntax
- Object-oriented programming
- Immediate object identity swapping
- Dynamic inheritance
- Objects as methods
- Optional Green threads
- Customizable metaclasses
- Easy to use proxy objects

## Relation to Smalltalk

Pharo is based on general concepts of Smalltalk but seeks to improve on them, so does not limit itself to them. The basic syntax of the language has a close resemblance to Smalltalk. However, the way classes are defined in Pharo differs from other Smalltalk dialects.

## Language syntax

The Pharo syntax is based on Smalltalk-80 language syntax with several extensions. Some of these are common among modern Smalltalk dialects.

- literals for dynamic arrays. The expressions that specify the array content are evaluated during program execution

```mw
{1. 2. 1+2}
```

- literals for byte arrays that can be composed only of integer numbers in the range from 0 to 255

```mw
#[1 2 3 4]
```

- literals for scaled decimals, a representation of fixed point decimal numbers able to accurately represent decimal fractions

```mw
3.14s2
```

- pragmas. In Smalltalk-80 the pragmas are used only for primitive methods. In Pharo they are fully capable method annotations

```mw
<gtInspectorPresentationOrder: 30>
```

- two double quotes inside a comment are interpreted as one double quote character that is part of the content of the comment

The Pharo language syntax is supposed to be very simple and minimalist. The basic language elements are often presented on one postcard as a showcase for the language's brevity. The grammar is classified as LL(1).

The language grammar does not specify directly how the code should be stored in files. Pharo uses Tonel as the preferred code serializing format.

## History

Pharo emerged as a fork of Squeak, an open-source Smalltalk environment created by the original Smalltalk-80 team (Dan Ingalls and Alan Kay). Pharo was created by S. Ducasse [1] and M. Denker in March 2008. It focuses on modern software engineering and development techniques. Pharo is supported by the Pharo consortium (for legal entities) [2] and the Pharo association for physical persons [3].

| Pharo version | Release date | Major features |
|---|---|---|
|   | March 16, 2008 | Fork of Squeak environment |
| 1.0 | April 15, 2010 | real closures, EToys and MVC removed |
| 1.1 | July 26, 2010 | Cog JIT VM, Settings framework |
| 1.2 | March 29, 2011 | new Finder, Recent changes tool, improved Help, better themes |
| 1.3 | August 2011 | Zinc, headless images |
| 1.4 | April 2012 | Ring metamodel, better code simulator |
| 2.0 | March 18, 2013 | browser improvements, QA tools, Fuel serializer, better files API |
| 3.0 | April 2014 | new modular compiler (Opal) and debugger, continuations |
| 4.0 | April 2015 | GTools, slots |
| 5.0 | May 2016 | Spur VM, UFFI, improved reflectivity |
| 6.0 | 6 June 2017 | 64-bit and Git support |
| 6.1 | 24 July 2017 | improved Git support |
| 7.0 | 22 January 2019 | bootstrapping, new code browser (Calypso), stateful traits |
| 8.0 | 20 January 2020 | improved support of Git, testing, refactoring and Windows |
| 9.0 | 15 July 2021 | GTK3 support, object-centric debugger and inspector, refactorings, official ARM VMs |
| 10.0 | 5 April 2022 | Cleanups, modularization, many rewritten and improved tools |
| 11.0 | 11 May 2023 | Ephemerons, SIMD, more efficient closures, improved tools |
| 12.0 | 26 May 2024 | New debug points system, new class definitions, permanent space |
| Latest version: 13.0 | 21 May 2025 | HDPI support, Zoomable UI, New Process Browser, Organic window manager, Async IO using epoll on unixes |
| Latest version: 13.1 | 26 June 2025 | Improvements merged since version 13.0 |

## Use of Pharo

### Companies and consultants

Some companies use Pharo for their development projects. In particular, they use:

- Seaside for dynamic web development
- Zinc for server architectures
- Moose to analyse data and software from all programming languages
- Graphic libraries for evolved user interfaces
- Roassal to visualize data

The Pharo consortium was created for companies wishing to support the Pharo project. The Pharo association was created in 2011 for users wishing to support the project.

## Performance and virtual machine (VM)

Pharo relies on a virtual machine that is written almost entirely in Smalltalk. Beginning in 2008, a new virtual machine (Cog) for Squeak, Pharo and Newspeak has been developed that performs nearly as well as the fastest Smalltalk virtual machine. In 2014/2015 the VM community is working on Spur, a new Memory Manager for Cog that should again increase performance and provide better 64-bit VM support.
