---
title: "Tagged architecture"
source: https://en.wikipedia.org/wiki/Tagged_architecture
domain: memory-tagging-extension
license: CC-BY-SA-4.0
tags: memory tagging extension, hardware memory tagging, tagged pointer safety, lock and key memory model
fetched: 2026-07-02
---

# Tagged architecture

In computer science, a **tagged architecture** is a type of computer architecture where every word of memory constitutes a tagged union, being divided into a number of bits of data, and a *tag* section that describes the type of the data: how it is to be interpreted, and, if it is a reference, the type of the object that it points to.

## Precursors

Some early systems use tagging of data in memory but do not have all of the characteristics now considered to be part of tagged architectures.

### RCA 601

The RCA 601 has a 3-bit tag register and a 3-bit tag for every 24-bit half-word. Every instruction can request a test for equal or unequal tag, and cause a maskable interrupt if the specified match fails. There is no architectural connection between the tag and the contents of the half-word; it is strictly determined by the software.

### Burroughs B5000, B5500 and B5700

The Burroughs B5000, B5500 and B5700 have 48-bit words with no appended tag field. However, while there are no tag fields for character, instruction or numeric (floating point) words, all of the control word formats include a 3-bit tag.

## Burroughs B6500 and successors

The Burroughs B6500 and its successors have a 3-bit tag for every word.

## Architecture

In contrast, program and data memory are indistinguishable in the von Neumann architecture, making the way the memory is referenced critical to interpret the correct meaning.

Notable examples of American tagged architectures were the Lisp machines, which had tagged pointer support at the hardware and opcode level, the Burroughs B6500 and successors, which have a data-driven tagged and descriptor-based architecture, and the non-commercial Rice Computer. Both the Burroughs and Lisp machine are examples of high-level language computer architectures, where the tagging is used to support types from a high-level language at the hardware level.

In addition to this, the original Xerox Smalltalk implementation used the least-significant bit of each 16-bit word as a tag bit: if it was clear then the hardware would accept it as an aligned memory address while if it was set it was treated as a (shifted) 15-bit integer. Current Intel documentation mentions that the lower bits of a memory address might be similarly used by some interpreter-based systems.

In the Soviet Union, the Elbrus series of supercomputers pioneered the use of tagged architectures in 1973.

The RISC-V J extension and memory-tagging extension (Zimt) both propose adding some support for tagged architecture at the instruction level.

CHERI (Capability Hardware Enhanced RISC Instructions) uses a tagged architecture to add capability-based addressing to several existing ISAs such as x86, MIPS, and RISC-V.
