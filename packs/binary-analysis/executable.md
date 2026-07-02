---
title: "Executable"
source: https://en.wikipedia.org/wiki/Executable
domain: binary-analysis
license: CC-BY-SA-4.0
tags: static binary analysis, executable format inspection, control flow graph recovery, symbol table analysis, machine code inspection
fetched: 2026-07-02
---

# Executable

In computing, an **executable** is a resource that a computer can use to control its behavior. As with all information in computing, it is data, but distinct from data that does not imply a flow of control. Terms such as **executable code**, **executable file**, **executable program**, and **executable image** describe forms in which the information is represented and stored. A **native executable** is machine code and is directly executable at the instruction level of a CPU. A script is also executable although indirectly via an interpreter. Intermediate executable code (such as bytecode) may be interpreted or converted to native code at runtime via just-in-time compilation.

## Native executable

Even though it is technically possible to write a native executable directly in machine language, it is generally not done. It is far more convenient to develop software as human readable source code and to automate the generation of machine code via a build toolchain. Today, most source code is a high-level language although it is still possible to use assembly language which is closely associated with machine code instructions. Many toolchains consist of a compiler that generates native code as a set of object files and a linker that generates a native executable from the object and other files. For assembly language, typically the translation tool is called an assembler instead of a compiler.

Object files are typically stored in a digital container format that supports structure in the machine code – such as Executable and Linkable Format (ELF) or Portable Executable (PE), depending on the computing context. The format may support segregating code into sections such as .text (executable code), .data (initialized global and static variables), and .rodata (read-only data, such as constants and strings).

Executable files typically include a runtime system, which implements runtime language features (such as task scheduling, exception handling, calling static constructors and destructors, etc.) and interactions with the operating system, notably passing arguments, environment, and returning an exit status, together with other startup and shutdown features such as releasing resources like file handles. For C, this is done by linking in the crt0 object, which contains the actual entry point and does setup and shutdown by calling the runtime library. Executable files thus may contain significant code beyond that directly generated from the source code. In some cases, it is desirable to omit this, for example for embedded systems. In C, this can be done by omitting the usual runtime, and instead explicitly specifying a linker script, which generates the entry point and handles startup and shutdown, such as calling `main` to start and returning exit status to the kernel at the end.

To be executable, a file must conform to the system's application binary interface (ABI). In simple interfaces, a file is executed by loading it into memory and jumping to the start of the address space and executing from there. In more complicated interfaces, executable files have additional metadata, which may specify relocations to be performed when the program is loaded, or the entry point address at which to start execution.
