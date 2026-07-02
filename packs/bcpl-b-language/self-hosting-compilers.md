---
title: "Self-hosting (compilers)"
source: https://en.wikipedia.org/wiki/Self-hosting_(compilers)
domain: bcpl-b-language
license: CC-BY-SA-4.0
tags: bcpl language, b language, martin richards, bootstrapping compilers, systems programming
fetched: 2026-07-02
---

# Self-hosting (compilers)

In computer programming, **self-hosting** is the use of a program as part of the toolchain or operating system that produces new versions of that same program—for example, a compiler that can compile its own source code. Self-hosting software is commonplace on personal computers and larger systems. Other programs that are typically self-hosting include kernels, assemblers, command-line interpreters and revision control software.

## Operating systems

An operating system is self-hosted when the toolchain to build the operating system runs on that same operating system. For example, Windows can be built on a computer running Windows.

Before a system can become self-hosted, another system is needed to develop it until it reaches a stage where self-hosting is possible. When developing for a new computer or operating system, a system to run the development software is needed, but development software used to write and build the operating system is also necessary. This is called a bootstrapping problem or, more generically, a chicken or the egg dilemma.

A solution to this problem is the cross compiler (or cross assembler when working with assembly language). A cross compiler allows source code on one platform to be compiled for a different machine or operating system, making it possible to create an operating system for a machine for which a self-hosting compiler does not yet exist. Once written, software can be deployed to the target system using means such as an EPROM, floppy diskette, flash memory (such as a USB thumb drive), or JTAG device. This is similar to the method used to write software for gaming consoles or for handheld devices like cellular phones or tablets, which do not host their own development tools.

Once the system is mature enough to compile its own code, the cross-development dependency ends. At this point, an operating system is said to be self-hosted.

## Compilers

Software development using compiler or interpreters can also be self hosted when the compiler is capable of compiling itself.

Since self-hosted compilers suffer from the same bootstrap problems as operating systems, a compiler for a new programming language needs to be written in an existing language. So the developer may use something like assembly language, C/C++, or even a scripting language like Python or Lua to build the first version of the compiler. Once the language is mature enough, development of the compiler can shift to the compiler's native language, allowing the compiler to build itself.

### Advantages

Self-hosting a compiler has the following advantages:

- It is a non-trivial test of the language being compiled, and as such is a form of dogfooding.
- Compiler developers and bug reporters only need to know the language being compiled.
- Compiler development can be performed in the higher-level language being compiled.
- Improvements to the compiler's back-end improve not only general-purpose programs but also the compiler itself.
- It is a comprehensive consistency check as it should be able to reproduce its own object code.

Note that some of these points assume that the language runtime is also written in the same language.

## History

The first self-hosting compiler (excluding assemblers) was written for Lisp by Hart and Levin at MIT in 1962. They wrote a Lisp compiler in Lisp, testing it inside an existing Lisp Interpreter. Once they had improved the compiler to the point where it could compile its own source code, it was self-hosting.

> The compiler as it exists on the standard compiler tape is a machine language program that was obtained by having the S-expression definition of the compiler work on itself through the interpreter.

— AI Memo 39

This technique is usually only practicable when an interpreter already exists for the very same language that is to be compiled; though possible, it is extremely uncommon to humanly compile a compiler with itself. The concept borrows directly from and is an example of the broader notion of running a program on itself as input, used also in various proofs in theoretical computer science, such as the proof that the halting problem is undecidable.

## Examples

Ken Thompson started development on Unix in 1968 by writing and compiling programs on the GE-635 and carrying them over to the PDP-7 for testing. After the initial Unix kernel, a command interpreter, an editor, an assembler, and a few utilities were completed, the Unix operating system was self-hosting – programs could be written and tested on the PDP-7 itself.

Douglas McIlroy wrote TMG (a compiler-compiler) in TMG on a piece of paper and "decided to give his piece of paper to his piece of paper", doing the computation himself, thus compiling a TMG compiler into assembly, which he typed up and assembled on Ken Thompson's PDP-7.

Development of the GNU system relies largely on GCC (the GNU Compiler Collection) and GNU Emacs (a popular editor), making possible the self contained, maintained and sustained development of free software for the GNU Project.

Many programming languages have self-hosted implementations: compilers that are both in and for the same language. An approach is bootstrapping, where a core version of the language is initially implemented using another high-level language, assembler, or even machine language; the resulting compiler is then used to start building successive expanded versions of itself.

## List of languages having self-hosting compilers

The following programming languages have self-hosting compilers:

- Ada
- ALGOL (Burroughs B5000)
- BASIC
- BCPL
- C
- C++ (Visual C++, clang, gcc 4.8)
- C# (Microsoft Roslyn, Mono)
- ClojureScript
- CoffeeScript
- Crystal
- Curry
- D
- Dart
- Delphi
- Dylan
- Eiffel
- Elixir
- F#
- FASM
- Factor
- Forth
- Gambas
- Go
- Haskell
- Idris
- Java
- Kotlin
- Lisp (Common Lisp)
- LiveScript
- Mercury
- Nemerle
- Nim
- Oberon
- Object Pascal (Free Pascal)
- OCaml
- Pascal (Free Pascal)
- Pyret
- Python (PyPy)
- Raku (Rakudo)
- Rust
- Scala
- Scheme
- Smalltalk
- Standard ML (MLton)
- Tcl
- TMG
- TypeScript
- V (Vlang)
- Vala
- Virgil
- Visual Basic .NET (Microsoft Roslyn, Mono)
- Zig
