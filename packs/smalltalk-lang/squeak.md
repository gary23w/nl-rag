---
title: "Squeak"
source: https://en.wikipedia.org/wiki/Squeak
domain: smalltalk-lang
license: CC-BY-SA-4.0
tags: smalltalk language, smalltalk lang, pharo smalltalk, squeak smalltalk
fetched: 2026-07-02
---

# Squeak

**Squeak** is an object-oriented, class-based, and reflective programming language. It was derived from Smalltalk-80 by a group that included some of Smalltalk-80's original developers, initially at Apple Computer, then at Walt Disney Imagineering, where it was intended for use in internal Disney projects. The group later was supported by HP Labs and SAP.

Squeak runs on a stack virtual machine (VM), allowing for a high degree of portability. The Squeak system includes code for generating a new version of the VM on which it runs, along with a VM simulator written in Squeak.

## Developers

Dan Ingalls, an important contributor to the Squeak project, wrote the paper upon which Squeak is built, and constructed the architecture for five generations of the Smalltalk language.

Alan Kay is an important contributor to the Squeak project, and Squeak incorporates many elements of his proposed Dynabook concept.

## User interface frameworks

Squeak includes four user interface frameworks:

- An implementation of Morphic, Self's graphical direct manipulation interface framework. This is Squeak's main interface.
- Tile-based, limited visual programming scripting in Etoys, based on Morphic.
- A novel, experimental interface called Tweak. In 2001 it became clear that the Etoy architecture in Squeak had reached its limits in what the Morphic interface infrastructure could do. Hewlett-Packard researcher Andreas Raab proposed defining a "script process" and providing a default scheduling-mechanism that avoids several more general problems. This resulted in a new user interface, proposed to replace the Squeak Morphic user interface in the future. Tweak added mechanisms of islands, asynchronous messaging, players and costumes, language extensions, projects, and tile scripting. Its underlying object system is class-based, but to users, during programming (scripting), it acts like it is prototype-based. Tweak objects are created and run in Tweak project windows.
- A model–view–controller (MVC) interface was the primary UI in Squeak versions 3.8 and earlier. It derived from the original Smalltalk-80 user interface framework which first introduced and popularized the MVC architectural pattern. MVC takes its name from the three core classes of the framework. Thus, the term "MVC" in the context of Squeak refers to both one of the available user interface frameworks and the pattern the framework follows. MVC is still provided for those wishing to use this older type of interface.

## Uses

Many Squeak contributors collaborate on Open Cobalt, a free and open source virtual world browser and construction toolkit built on Squeak.

The first version of Scratch was implemented in Squeak.

OpenQwaq, a virtual conferencing and collaboration system, is based on Squeak.

Squeak is also used in the Nintendo ES operating system.

## License

Squeak 4.0 and later may be downloaded at no cost, including source code, as a prebuilt virtual machine image licensed under the MIT License, with the exception of some of the original Apple code, which is governed by the Apache License.

Squeak was originally released by Apple under its own *Squeak License*. While source code was available and modification permitted, the Squeak License contained an indemnity clause that prevented it from qualifying as true free and open-source software.

In 2006, Apple relicensed Squeak twice. First, in May, Apple used its own Apple Public Source License, which satisfies the Free Software Foundation's concept of a Free Software License and has attained official approval from the Open Source Initiative as an Open Source License. However, The Apple Public Source License fails to conform to the Debian Free Software Guidelines. To enable inclusion of Etoys in the One Laptop Per Child project, a second relicensing was undertaken using the Apache License. At this point, an effort was also made to address the issue of code contributed by members of the Squeak community, which it was not in Apple's power to unilaterally relicense.

For each contribution made under the Squeak License since 1996, a relicensing statement was obtained authorizing distribution under the MIT license, and finally in March 2010, the result was released as Squeak 4.0, now under combined MIT and Apache licenses.
