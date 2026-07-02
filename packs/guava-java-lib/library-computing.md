---
title: "Library (computing)"
source: https://en.wikipedia.org/wiki/Library_(computing)
domain: guava-java-lib
license: CC-BY-SA-4.0
tags: guava library, java core utilities, guava collections, guava immutable collections
fetched: 2026-07-02
---

# Library (computing)

In computing, a **library** is a collection of resources that can be used during software development to implement a computer program. Commonly, a library consists of executable code such as compiled functions and classes, or a library can be a collection of source code. A resource library may contain data such as images and text.

A library can be used by multiple, independent consumers (programs and other libraries). This differs from resources defined in a program which can usually only be used by that program. When a consumer uses a library resource, it gains the value of the library without having to implement it itself. Libraries encourage software reuse in a modular fashion. Libraries can use other libraries resulting in a hierarchy of libraries in a program.

When writing code that uses a library, a programmer only needs to know how to use that library's application programming interface (API) without understanding its internal mechanics. For example, a program could use a library that abstracts a complicated system call so that the programmer can use the system feature without spending time to learn the intricacies of the system function.

## History

The idea of a computer library dates back to the first computers created by Charles Babbage. An 1888 paper on his Analytical Engine suggested that computer operations could be punched on separate cards from numerical input. If these operation punch cards were saved for reuse then "by degrees the engine would have a library of its own."

In 1947 Goldstine and von Neumann speculated that it would be useful to create a "library" of subroutines for their work on the IAS machine, an early computer that was not yet operational at that time. They envisioned a physical library of magnetic wire recordings, with each wire storing reusable computer code.

Inspired by von Neumann, Wilkes and his team constructed EDSAC. A filing cabinet of punched tape held the subroutine library for this computer. Programs for EDSAC consisted of a main program and a sequence of subroutines copied from the subroutine library. In 1951 the team published the first textbook on programming, *The Preparation of Programs for an Electronic Digital Computer*, which detailed the creation and the purpose of the library.

COBOL included "primitive capabilities for a library system" in 1959, but Jean Sammet described them as "inadequate library facilities" in retrospect.

JOVIAL has a Communication Pool (COMPOOL), roughly a library of header files.

Another major contributor to the modern library concept came in the form of the subprogram innovation of FORTRAN. FORTRAN subprograms can be compiled independently of each other, but the compiler lacked a linker. So prior to the introduction of modules in Fortran-90, type checking between FORTRAN subprograms was impossible.

By the mid 1960s, copy and macro libraries for assemblers were common. Starting with the popularity of the IBM System/360, libraries containing other types of text elements, e.g., system parameters, also became common.

In IBM's OS/360 and its successors this is called a partitioned data set.

The first object-oriented programming language, Simula, developed in 1965, supported adding classes to libraries via its compiler.

## Linking

The *linking* (or *binding*) process resolves references known as *symbols* (or *links*) by searching for them in various locations including configured libraries. If a linker (or binder) does not find a symbol, then it fails, but multiple matches may or may not cause failure.

*Static linking* is linking at build time, such that the library executable code is included in the program. *Dynamic linking* is linking at run time; it involves building the program with information that supports run-time linking to a dynamic link library (DLL). For dynamic linking, a compatible DLL file must be available to the program at run time, but for static linking, the program is standalone.

*Smart linking* is performed by a build tool that excludes unused code in the linking process. For example, a program that only uses integers for arithmetic, or does no arithmetic operations at all, can exclude floating-point library routines. This can lead to smaller program file size and reduced memory usage.

## Relocation

Some references in a program or library module are stored in a relative or symbolic form which cannot be resolved until all code and libraries are assigned final static addresses. Relocation is the process of adjusting these references, and is done either by the linker or the loader. In general, relocation cannot be done to individual libraries themselves because the addresses in memory may vary depending on the program using them and other libraries they are combined with. Position-independent code avoids references to absolute addresses and therefore does not require relocation.

## Categories

### Executable

An executable library consists of code that has been converted from source code into machine code or an intermediate form such as bytecode. A linker allows for using library objects by associating each reference with an address at which the object is located. For example, in C, a library function is invoked via C's normal function call syntax and semantics.

A variant is a library containing compiled code (object code in IBM's nomenclature) in a form that cannot be loaded by the OS but that can be read by the linker.

### Static

A static library is an executable library that is linked into a program at build-time by a linker (or whatever the build tool is called that does linking). This process, and the resulting stand-alone file, is known as a static build of the program. A static build may not need any further relocation if virtual memory is used and no address space layout randomization is desired.

A static library is sometimes called an *archive* on Unix-like systems.

### Dynamic

A dynamic library is linked when the program is run – either at load-time or runtime. The dynamic library was intended after the static library to support additional software deployment flexibility.
