---
title: "Binary Ninja"
source: https://en.wikipedia.org/wiki/Binary_Ninja
domain: disassembly-analysis
license: CC-BY-SA-4.0
tags: disassembly analysis, interactive disassembler workflow, assembly instruction decoding, opcode instruction set, binary code inspection
fetched: 2026-07-02
---

# Binary Ninja

**Binary Ninja** is a reverse-engineering platform developed by Vector 35 Inc. It allows users to disassemble a binary file and visualize the disassembly in both linear and graph-based views. The software performs automated, in-depth code analysis, generating information that helps to analyze a binary. It lifts assembly instructions into intermediate languages, generating decompiled code.

Binary Ninja supports various CPU architectures and binary executable formats, and runs on Windows, macOS, and Linux. It also offers a free-to-use cloud version and a native commercial version.

## History

Originally developed as an internal tool for a CTF team, the developers later formed Vector 35 Inc. to turn Binary Ninja into a commercial product. Development began in 2015, and the first public version was released in July 2016.

The commercial version was developed from scratch and does not share code with the original internal tool. The latter one is now open-sourced under the GPLv2 license.

## Features and usage

### User interface

Binary Ninja's user interface is built using Qt and comprises several components such as a symbol list, a cross-reference window, and disassembly views (both linear and graph-based), a mini-graph, and a feature map. It also includes tools like a hex editor, strings listing, and a triage view.

Binary Ninja generates extensive annotations in the UI to assist binary analysis and also supports user-defined themes for customization.

### API and plugins

Binary Ninja offers an API that can be accessed via Python, C++, or Rust. The API is open-sourced under the MIT License. It can interact with most of Binary Ninja's functionality, including the user interface, analysis tools, and intermediate languages (see below). It can be used to add support for new architectures or to automate tasks,

Plugins can be developed using the API to enhance Binary Ninja. Vector35 maintains a collection of official plugins, while the community has created numerous additional plugins.

Some notable plugins include the debugger, and the signature kit.

### Binary Ninja Intermediate Languages (BNIL)

Binary Ninja offers three intermediate languages (ILs).

- The low-level IL (LLIL) provides a detailed lifting of the underlying instructions from various architectures to a unified representation.
- The medium-level IL (MLIL) creates variables with types and abstracts away the notion of the stack.
- The high-level IL (HLIL, also known as the decompiler), offers a representation of the code that is similar to C source code.

### Core analysis

Binary Ninja automatically performs various analyses on the binary. Some examples are:

- function detection
- cross-references for code and data
- type inference
- constant propagation
- value-set analysis
- jump table resolution

### Binary editing and patching, shellcode compiler (SCC)

Binary Ninja offers binary patching and editing features. It can assemble an instruction at the current line, flip a conditional jump, etc. Edits and updated analysis are immediately reflected in the UI.

Binary Ninja can be used as a general binary editor. It supports several commonly used transformations and encryption algorithms.

The shellcode compiler allows the user to compile and insert code via C syntax.

## Supported architectures and executable file formats

### Architectures

Binary Ninja supports the following CPU architectures officially:

- x86 32-bit
- x86 64-bit
- ARMv7
- Thumb2
- ARMv8
- PowerPC
- MIPS
- RISC-V
- 6502
- nanoMIPS (Ultimate only)
- TriCore (Ultimate only)
- Hexagon (Ultimate only)

The support for these architectures vary and details can be found in the official FAQ.

Community-authored plugins add support for various other architectures.

### Executable file formats

Binary Ninja supports the following executable file formats officially:

- PE/COFF
- ELF
- Mach-O
- .NES binary (via a plugin)
- Raw binary
- md1rom
