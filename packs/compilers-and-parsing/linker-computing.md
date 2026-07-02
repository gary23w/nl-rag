---
title: "Linker (computing)"
source: https://en.wikipedia.org/wiki/Linker_(computing)
domain: compilers-and-parsing
license: CC-BY-SA-4.0
tags: compiler construction, parser generator, syntax analysis, lexer, lexical analysis, abstract syntax tree
fetched: 2026-07-02
---

# Linker (computing)

A **linker** or **link editor** is a computer program that combines intermediate software build files such as object and library files into a single executable file such as a program or library. A linker is often part of a toolchain that includes a compiler and/or assembler that generates intermediate files that the linker processes. The linker may be integrated with other toolchain tools such that the user does not interact with the linker directly.

A simpler version that writes its output directly to memory is called the *loader*, though loading is typically considered a separate process.

## Overview

Computer programs typically are composed of several parts or modules; these parts/modules do not need to be contained within a single object file, and in such cases refer to each other using symbols as addresses into other modules, which are mapped into memory addresses when linked for execution.

While the process of linking is meant to ultimately combine these independent parts, there are many good reasons to develop those separately at the source-level. Among these reasons are the ease of organizing several smaller pieces over a monolithic whole and the ability to better define the purpose and responsibilities of each individual piece, which is essential for managing complexity and increasing long-term maintainability in software architecture.

Typically, an object file can contain three kinds of symbols:

- defined "external" symbols, sometimes called "public" or "entry" symbols, which allow it to be called by other modules,
- undefined "external" symbols, which reference other modules where these symbols are defined, and
- local symbols, used internally within the object file to facilitate relocation.

For most compilers, each object file is the result of compiling one input source code file. When a program comprises multiple object files, the linker combines these files into a unified executable program, resolving the symbols as it goes along.

Linkers can take objects from a collection called a library or runtime library. Most linkers do not include all the object files in a static library in the output executable; they include only those object files from the library that are referenced by other object files or libraries directly or indirectly. But for a shared library, the entire library has to be loaded during runtime as it is not known which functions or methods will be called during runtime. Library linking may thus be an iterative process, with some referenced modules requiring additional modules to be linked, and so on. Libraries exist for diverse purposes, and one or more system libraries are usually linked in by default.

The linker also takes care of arranging the objects in a program's address space. This may involve *relocating* code that assumes a specific base address into another base. Since a compiler seldom knows where an object will reside, it often assumes a fixed base location (for example, zero). Relocating machine code may involve re-targeting absolute jumps, loads, and stores.

The executable output by the linker may need another relocation pass when it is finally loaded into memory (just before execution). This pass is usually omitted on hardware offering virtual memory: every program is put into its own address space, so there is no conflict even if all programs load at the same base address. This pass may also be omitted if the executable is a position independent executable.

Additionally, in some operating systems, the same program handles both the jobs of linking and loading a program (dynamic linking).

## Dynamic linking

Many operating system environments allow dynamic linking, deferring the resolution of some undefined symbols until a program is run. That means that the executable code still contains undefined symbols, plus a list of objects or libraries that will provide definitions for these. Loading the program will load these objects/libraries as well, and perform a final linking.

This approach offers two advantages:

- Often-used libraries (for example the standard system libraries) need to be stored in only one location, not duplicated in every single executable file, thus saving limited memory and disk space.
- If a bug in a library function is corrected by replacing the library or performance is improved, all programs using it dynamically will benefit from the correction after restarting them. Programs that included this function by static linking would have to be re-linked first.

There are also a few disadvantages:

- Known on the Windows platform as "DLL hell", an incompatible updated library will break executables that depended on the behavior of the previous version of the library if the newer version is not correctly backward compatible.
- A program, together with the libraries it uses, might be certified (e.g. as to correctness, documentation requirements, or performance) as a package, but not if components can be replaced (this also argues against automatic OS updates in critical systems; in both cases, the OS and libraries form part of a *qualified* environment).

Contained or virtual environments may further allow system administrators to mitigate or trade-off these individual pros and cons.

## Static linking

Static linking is the result of the linker copying all library routines used in the program into the executable image. This may require more disk space and memory than dynamic linking, but is more portable, since it does not require the presence of the library on the system where it runs. Static linking also prevents "DLL hell", since each program includes exactly the versions of library routines that it requires, with no conflict with other programs. A program using just a few routines from a library does not require the entire library to be installed.

## Relocation

As the compiler has no information on the layout of objects in the final output, it cannot take advantage of shorter or more efficient instructions that place a requirement on the address of another object. For example, a jump instruction can reference an absolute address or an offset from the current location, and the offset could be expressed with different lengths depending on the distance to the target. By first generating the most conservative instruction (usually the largest relative or absolute variant, depending on platform) and adding *relaxation hints*, it is possible to substitute shorter or more efficient instructions during the final link. In regard to jump optimizations this is also called *automatic jump-sizing*. This step can be performed only after all input objects have been read and assigned temporary addresses; the **linker relaxation** pass subsequently reassigns addresses, which may in turn allow more potential relaxations to occur. In general, the substituted sequences are shorter, which allows this process to always converge on the best solution given a fixed order of objects; if this is not the case, relaxations can conflict, and the linker needs to weigh the advantages of either option.

While instruction relaxation typically occurs at link-time, inner-module relaxation can already take place as part of the optimizing process at compile-time. In some cases, relaxation can also occur at load-time as part of the relocation process or combined with dynamic dead-code elimination techniques.

## Linkage editor

In IBM System/360 through IBM Z mainframe operating systems such as OS/360 and its successors, this type of program is known as a *linkage editor*. As the name implies a linkage *editor* has the additional capability of allowing the addition, replacement, and/or deletion of individual program sections. Operating systems such as OS/360 have format for executable load-modules containing supplementary data about the component sections of a program, so that an individual program section can be replaced, and other parts of the program updated so that relocatable addresses and other references can be corrected by the linkage editor, as part of the process.

One advantage of this is that it allows a program to be maintained without having to keep all of the intermediate object files, or without having to re-compile program sections that haven't changed. It also permits program updates to be distributed in the form of small files (originally card decks), containing only the object module to be replaced. In such systems, object code is in the form and format of 80-byte punched-card images, so that updates can be introduced into a system using that medium. In later releases of OS/360 and in subsequent systems, load-modules contain additional data about versions of components modules, to create a traceable record of updates. It also allows one to add, change, or remove an overlay structure from an already linked load module.

The term "linkage editor" should not be construed as implying that the program operates in a user-interactive mode like a text editor. It is intended for batch-mode execution, with the editing commands being supplied by the user in sequentially organized files, such as punched cards, DASD, or magnetic tape.

*Linkage editing* (IBM nomenclature) or *consolidation* or *collection* (ICL nomenclature) refers to the *linkage editor's* or *consolidator's* act of combining the various pieces into a relocatable binary, whereas the loading and relocation into an absolute binary at the target address is normally considered a separate step.

## Linker control scripts

Early linkers gave users very limited control over the arrangement of generated output object files. As the target systems became more complex with different memory requirements, such as in embedded systems, it became necessary to give users control to generate output object files with their specific requirements such as defining base addresses of segments. Linker control scripts were used for this.

## Notable implementations

### Unix & Unix-like

On Unix and Unix-like systems, the static linker is usually invoked via the command `ld` which is an abbreviation of *LoaDer* or *Link eDitor*. The term "loader" was used to describe the process of loading external symbols from other programs during the process of linking. (This terminology has been used in other operating systems as well. For example, in SINTRAN III, linking (assembling object files into a program) was called *loading* – as in loading executable code into a file.)

### GNU

GNU ld, part of the GNU Binary Utilities (binutils), is the GNU Project version of the Unix static linker. A *linker script* may be passed to GNU ld to exercise fine grain control of the linking process. Two versions of ld are provided in binutils: the traditional GNU ld based on bfd, and a streamlined ELF-only version called gold.

The LLVM project's linker, *lld*, is designed to be drop-in compatible, and may be used directly with the GNU compiler. Another drop-in replacement, mold, is a highly parallelized and faster alternative which is also supported by GNU tools.
