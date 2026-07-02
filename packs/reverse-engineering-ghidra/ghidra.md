---
title: "Ghidra"
source: https://en.wikipedia.org/wiki/Ghidra
domain: reverse-engineering-ghidra
license: CC-BY-SA-4.0
tags: ghidra reverse engineering, software reverse engineering, binary decompiler analysis, disassembly workflow, malware code analysis
fetched: 2026-07-02
---

# Ghidra

**Ghidra** (/ˈɡiːdrə/ *GEE-druh*) is a free and open source reverse engineering tool developed by the National Security Agency (NSA) of the United States. The binaries were released at the RSA Conference in March 2019; the source code was published one month later on GitHub. Ghidra is seen by many security researchers as a competitor to IDA Pro. The software is written in Java using the Swing framework for the GUI. The decompiler component is written in C++, and is therefore usable in a stand-alone form.

Scripts to perform automated analysis with Ghidra can be written in Java or Python (via Jython). Plugins adding new features to Ghidra itself can be developed using a Java-based extension framework.

## History

Ghidra's existence was originally revealed to the public via Vault 7 in March 2017, but the software itself remained unavailable until its declassification and official release two years later. Some comments in its source code indicate that it existed as early as 1999.

| Version | Year | Major features |
|---|---|---|
| 1.0 | 2003 | Proof of concept |
| 2.0 | 2004 | Database, docking windows |
| 3.0 | 2006 | SLEIGH, decompiler, version control |
| 4.0 | 2007 | Scripting, version tracking |
| 5.0 | 2010 | File system browser |
| 6.0 | 2014 | First unclassified version |
| 9.0 | 2019 | First public release |
| 9.2 | 2020 | Graph visualization, new PDB parser |
| 10.0 | 2021 | Debugger |
| 11.0 | 2023 | Rust and Go binaries support, BSim |
| 11.1 | 2024 | Swift and DWARF 5 support, Mach-O improvements |

In June 2019, coreboot began to use Ghidra for its reverse engineering efforts on firmware-specific problems following the open source release of the Ghidra software suite.

Ghidra can be used as a debugger since Ghidra 10.0. Ghidra's debugger supports debugging user-mode Windows programs via WinDbg, Linux programs via GDB and macOS programs via LLDB.

## Supported architectures

The following architectures or binary formats are supported:

- x86 16, 32 and 64 bit
- ARM and AARCH64
- PowerPC 32/64 and VLE
- MIPS 16/32/64
- MicroMIPS
- 68xxx
- Java and DEX bytecode
- PA-RISC
- RISC-V
- eBPF
- BPF
- Tricore
- PIC 12/16/17/18/24
- SPARC 32/64
- CR16C
- Z80
- 6502
- MC6805/6809, HC05/HC08/HC12
- 8048, 8051, 8085
- CP1600
- MSP430
- AVR8, AVR32
- SuperH
- V850
- LoongArch
- Xtensa
