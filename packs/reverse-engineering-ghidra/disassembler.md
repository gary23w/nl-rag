---
title: "Disassembler"
source: https://en.wikipedia.org/wiki/Disassembler
domain: reverse-engineering-ghidra
license: CC-BY-SA-4.0
tags: ghidra reverse engineering, software reverse engineering, binary decompiler analysis, disassembly workflow, malware code analysis
fetched: 2026-07-02
---

# Disassembler

A **disassembler** is a computer program that translates machine language into assembly language—the inverse operation to that of an assembler. The output of disassembly is typically formatted for human-readability rather than for input to an assembler, making disassemblers primarily a reverse-engineering tool. Common uses include analyzing the output of high-level programming language compilers and their optimizations, recovering source code when the original is lost, performing malware analysis, modifying software (such as binary patching), and software cracking.

A disassembler differs from a decompiler, which targets a high-level language rather than an assembly language. A fundamental method of software analysis is disassembly. Unlike decompilers, which make attempts at recreating high-level human readable structures using binaries, disassemblers are aimed at generating a symbolic assembly, meaning it's attempting to reconstruct the assembly closest to its executions. Disassembled code is hence normally more accurate but also lower level and less abstract than decompiled code and thus it can be much more easily analyzed.

Assembly language source code generally permits the use of constants and programmer comments. These are usually removed from the assembled machine code by the assembler. If so, a disassembler operating on the machine code would produce disassembly lacking these constants and comments; the disassembled output becomes more difficult for a human to interpret than the original annotated source code. Some disassemblers provide a built-in code commenting feature where the generated output is enriched with comments regarding called API functions or parameters of called functions. Some disassemblers make use of the symbolic debugging information present in object files such as ELF. For example, IDA allows the human user to make up mnemonic symbols for values or regions of code in an interactive session: human insight applied to the disassembly process often parallels human creativity in the code writing process.

## Challenges

It is not always possible to distinguish executable code from data within a binary. While common executable formats, such as ELF and PE, separate code and data into distinct sections, flat binaries do not, making it unclear whether a given location contains executable instructions or non-executable data. This ambiguity might complicate the disassembly process.

Additionally, CPUs often allow dynamic jumps computed at runtime, which makes it impossible to identify all possible locations in the binary that might be executed as instructions.

On computer architectures with variable-width instructions, such as in many CISC architectures, more than one valid disassembly may exist for the same binary.

Disassemblers also cannot handle code that changes during execution, as static analysis cannot account for runtime modifications.

Encryption, packing, or obfuscation are often applied to computer programs, especially as part of digital rights management to deter reverse engineering and cracking. These techniques pose additional challenges for disassembly, as the code must first be unpacked or decrypted before meaningful analysis can begin.

## Static vs. dynamic disassembly

Disassembly can be performed statically or dynamically. **Static disassembly** analyzes the binary without executing it, which enables offline inspection. However, static disassembly may misinterpret some operations or obfuscation.

**Dynamic disassembly** observes executed instructions at runtime, typically by monitoring CPU registers and CPU flags. Dynamic analysis can capture executed control paths and runtime-resolved addresses, which while being the major upside to decompilers they may miss code paths not triggered during execution.

While both are respectively powerful, modern disassemblers often combine both approaches to improve accuracy in more complex binaries.

## Examples of disassemblers

A disassembler can be either stand-alone or interactive. A stand-alone disassembler generates an assembly language file upon execution, which can then be examined. In contrast, an interactive disassembler immediately reflects any changes made by the user. For example, if the disassembler initially treats a section of the program as data rather than code, the user can specify it as code. The disassembled code will then be updated and displayed instantly, allowing the user to analyze it and make further changes during the same session.

Any interactive debugger will include some way of viewing the disassembly of the program being debugged. Often, the same disassembly tool will be packaged as a standalone disassembler distributed along with the debugger. For example, objdump, part of GNU Binutils, is related to the interactive debugger gdb.

- Binary Ninja
- DEBUG
- Interactive Disassembler (IDA)
- Ghidra
- Hiew
- Hopper Disassembler
- PE Explorer Disassembler
- Netwide Disassembler (Ndisasm), companion to the Netwide Assembler (NASM).
- OLIVER (CICS interactive test/debug) includes disassemblers for Assembler, COBOL, and PL/1
- x64dbg, a debugger for Windows that also performs dynamic disassembly
- OllyDbg is a 32-bit assembler level analysing debugger
- Radare2
- Rizin and Cutter (graphical interface for Rizin)
- SIMON (batch interactive test/debug) includes disassemblers for Assembler, COBOL, and PL/1
- Sourcer, a commenting 16-bit/32-bit x86 disassembler sold by V Communications in the 1990s

## Disassemblers and emulators

A dynamic disassembler can be integrated into the output of an emulator or hypervisor to trace the real-time execution of machine instructions, displaying them line-by-line. In this setup, along with the disassembled machine code, the disassembler can show changes to registers, data, or other state elements (such as condition codes) caused by each instructions. This provides powerful debugging information for problem resolution. However, the output size can become quite large, particularly if the tracing is active throughout the entire execution of a program. These features were first introduced in the early 1970s by OLIVER as part of its CICS debugging product and are now incorporated into the XPEDITER product from Compuware.

## Length disassembler

A **length disassembler**, also known as **length disassembler engine** (**LDE**), is a tool that, given a sequence of bytes (instructions), outputs the number of bytes taken by the parsed instruction. Notable open source projects for the x86 architecture include ldisasm, Tiny x86 Length Disassembler and Extended Length Disassembler Engine for x86-64.
