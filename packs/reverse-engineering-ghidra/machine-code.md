---
title: "Machine code"
source: https://en.wikipedia.org/wiki/Machine_code
domain: reverse-engineering-ghidra
license: CC-BY-SA-4.0
tags: ghidra reverse engineering, software reverse engineering, binary decompiler analysis, disassembly workflow, malware code analysis
fetched: 2026-07-02
---

# Machine code

In computing, **machine code** is data encoded and structured to control a computer's central processing unit (CPU) via its programmable interface. A computer program consists primarily of sequences of machine-code instructions. Machine code is classified as native with respect to its host CPU since it is the language that the CPU interprets directly. Some software interpreters translate the programming language that they interpret into a virtual machine code (bytecode) and process it with a P-code machine.

A machine-code instruction causes the CPU to perform a specific task such as:

- Load a word from memory to a CPU register
- Execute an arithmetic logic unit (ALU) operation on one or more registers or memory locations
- Jump or skip to an instruction that is not the next one

An instruction set architecture (ISA) defines the interface to a CPU and varies by groupings or families of CPU design such as x86 and ARM. Generally, machine code compatible with one family is not with others, but there are exceptions. The VAX architecture includes optional support of the PDP-11 instruction set. The IA-64 architecture includes optional support of the IA-32 instruction set. And, the PowerPC 615 can natively process both PowerPC and x86 instructions.

## Assembly language

Assembly language provides a relatively direct mapping from a human-readable source code to machine code. The assembly language source code represents numerical codes in machine code, as mnemonics and labels. For example, `NOP` in assembly for an x86 processor represents the x86 architecture opcode 0x90 in machine code. While it is possible to write a program in machine code, doing so is tedious and error-prone. Therefore, programs are usually written in assembly or, more commonly, in a high-level programming language.

## Instruction set

A machine instruction encodes an operation as a pattern of bits based on the specified format for the machine's instruction set.

Instruction sets differ in various ways. Instructions of a set might all be the same length or different instructions might have different lengths; they might be smaller than, the same size as, or larger than the word size of the architecture. The number of instructions may be relatively small or large. Instructions may or may not have to be aligned on particular memory boundaries, such as the architecture's word boundary.

An instruction set needs to execute the circuits of a computer's digital logic level. At the digital level, the program needs to control the computer's registers, bus, memory, ALU, and other hardware components. To control a computer's architectural features, machine instructions are created. Examples of features that are controlled using machine instructions:

- segment registers
- protected address mode
- binary-coded decimal (BCD) arithmetic

The criteria for instruction formats include:

- Instructions most commonly used should be shorter than instructions rarely used.
- The memory transfer rate of the underlying hardware determines the flexibility of the memory fetch instructions.
- The number of bits in the address field requires special consideration.

Determining the size of the address field is a choice between space and speed. On some computers, the number of bits in the address field may be too small to access all of the physical memory. Also, virtual address space needs to be considered. Another constraint may be a limitation on the size of registers used to construct the address. Whereas a shorter address field allows the instructions to execute more quickly, other physical properties need to be considered when designing the instruction format.

Instructions can be separated into two types: general-purpose and special-purpose. Special-purpose instructions exploit architectural features that are unique to a computer. General-purpose instructions control architectural features common to all computers.

General-purpose instructions control:

- Data movement from one place to another
- Monadic operations that have one operand to produce a result
- Dyadic operations that have two operands to produce a result
- Comparisons and conditional jumps
- Procedure calls
- Loop control
- Input/output

### Overlapping instruction

On processor architectures with variable-length instruction sets (such as Intel's x86 processor family) it is, within the limits of the control-flow resynchronizing phenomenon known as the Kruskal count, sometimes possible through opcode-level programming to deliberately arrange the resulting code so that two code paths share a common fragment of opcode sequences. These are called *overlapping instructions*, *overlapping opcodes*, *overlapping code*, *overlapped code*, *instruction scission*, or *jump into the middle of an instruction*.

In the 1970s and 1980s, overlapping instructions were sometimes used to preserve memory space. One example was in the implementation of error tables in Microsoft's Altair BASIC, where *interleaved instructions* mutually shared their instruction bytes. The technique is rarely used today, but might still be necessary to resort to in areas where extreme optimization for size is necessary on the byte level such as in the implementation of boot loaders which have to fit into boot sectors.

It is also sometimes used as a code obfuscation technique as a measure against disassembly and tampering.

The principle is also used in shared code sequences of fat binaries which must run on multiple instruction-set-incompatible processor platforms.

This property is also used to find unintended instructions called gadgets in existing code repositories and is used in return-oriented programming as alternative to code injection for exploits such as return-to-libc attacks.

### Microcode

In some computers, the machine code of the architecture is implemented by an even more fundamental underlying layer called microcode, providing a common machine language interface across a line or family of different models of computer with widely different underlying dataflows. This is done to facilitate porting of machine language programs between different models. An example of this use is the IBM System/360 family of computers and their successors.

## Examples

### IBM 650

The IBM 650, introduced in 1954, was a decimal, word addressed computer with instructions and data stored on a magnetic drum. Each word included ten digits plus sign. Instructions divided the words into a two digit operation code, a four digit address of the data word to be processed and a four digit address of the next instruction to execute. The second address allowed instructions to be placed on the drum near where the drum would be positioned after the previous instruction completed, a practice called optimization.

With the aid of a physical table of op codes, it was quite feasible to write programs in machine code. IBM provided a form with a grid showing each memory location, so a programmer could keep track of which locations were still available. There was a single-instruction-per-card format that could be loaded directly into the machine and executed. Later IBM introduced an assembler (SOAP) that allowed symbolic address and also performed a rough optimization pass.

### IBM 709x

The IBM 704, 709, 704x and 709x store one instruction in each instruction word; IBM numbers the bit from the left as S, 1, ..., 35. Most instructions have one of two formats:

**Generic**

S,1-11

12-13 Flag, ignored in some instructions

14-17 unused

18-20 Tag

21-35 Y

**Index register control, other than TSX**

S,1-2 Opcode

3-17 Decrement

18-20 Tag

21-35 Y

For all but the IBM 7094 and 7094 II, there are three index registers designated A, B and C; indexing with multiple 1 bits in the tag subtracts the logical or of the selected index registers and loading with multiple 1 bits in the tag loads all of the selected index registers. The 7094 and 7094 II have seven index registers, but when they are powered on they are in *multiple tag mode*, in which they use only the three of the index registers in a fashion compatible with earlier machines, and require a Leave Multiple Tag Mode (**LMTM**) instruction in order to access the other four index registers.

The effective address is normally Y-C(T), where C(T) is either 0 for a tag of 0, the logical or of the selected index registers in multiple tag mode or the selected index register if not in multiple tag mode. However, the effective address for index register control instructions is just Y.

A flag with both bits 1 selects indirect addressing; the indirect address word has both a tag and a Y field.

In addition to *transfer* (branch) instructions, these machines have skip instruction that conditionally skip one or two words, e.g., Compare Accumulator with Storage (CAS) does a three way compare and conditionally skips to NSI, NSI+1 or NSI+2, depending on the result.

### MIPS

The MIPS architecture provides a specific example for a machine code whose instructions are always 32 bits long. The general type of instruction is given by the *op* (operation) field, the highest 6 bits. J-type (jump) and I-type (immediate) instructions are fully specified by *op*. R-type (register) instructions include an additional *funct* (function) field to determine the exact operation. The fields used in these types are:

| Type | -31-                                 format (bits)                                 -0- |   |   |   |   |   |
|---|---|---|---|---|---|---|
| **R** | opcode (6) | rs (5) | rt (5) | rd (5) | shamt (5) | funct (6) |
| **I** | opcode (6) | rs (5) | rt (5) | immediate (16) |   |   |
| **J** | opcode (6) | address (26) |   |   |   |   |

*rs*, *rt*, and *rd* indicate register operands; *shamt* gives a shift amount; and the *address* or *immediate* fields contain an operand directly.

For example, adding the registers 1 and 2 and placing the result in register 6 is encoded:

```
[  op  |  rs |  rt |  rd |shamt| funct]
    0     1     2     6     0     32     decimal
 000000 00001 00010 00110 00000 100000   binary
```

Load a value into register 8, taken from the memory cell 68 cells after the location listed in register 3:

```
[  op  |  rs |  rt | address/immediate]
   35     3     8           68           decimal
 100011 00011 01000 00000 00001 000100   binary
```

Jumping to the address 1024:

```
[  op  |        target address        ]
    2                 1024               decimal
 000010 00000 00000 00000 10000 000000   binary
```

## Bytecode

Machine code is similar to yet fundamentally different from bytecode. Like machine code, bytecode is typically generated (i.e. by a compiler) from source code. But, unlike machine code, bytecode is not directly executable by a CPU. An exception is if a processor is designed to use bytecode as its machine code, such as the Pascal MicroEngine or a Java processor. If bytecode is processed by a software interpreter, then that interpreter is a virtual machine for which the bytecode is its machine code.

## Storage

During execution, machine code is generally stored in RAM although running from ROM is supported by some devices. Regardless, the code may also be cached in more specialized memory to enhance performance. There may be different caches for instructions and data, depending on the architecture.

From the point of view of a process, the machine code lives in *code space*, a designated part of its address space. In a multi-threading environment, different threads of one process share code space along with data space, which reduces the overhead of context switching considerably as compared to process switching.

## Readability

Machine code is generally considered to be not human readable, with Douglas Hofstadter comparing it to examining the atoms of a DNA molecule. However, various tools and methods support understanding machine code.

Disassembly decodes machine code to assembly language which is possible since assembly instructions can often be mapped one-to-one to machine instructions.

A decompiler converts machine code to a high-level language, but the result can be relatively obfuscated (hard to understand).

A program can be associated with debug symbols (either embedded in the native executable or in a separate file) that allow it to be mapped to external source code. A debugger reads the symbols to help a programmer interactively debug the program. Examples include:

- The SHARE Operating System (1959) for the IBM 709, IBM 7090, and IBM 7094 computers allowed for an loadable code format named SQUOZE. SQUOZE was a compressed binary form of assembly language code and included a symbol table.
- Modern IBM mainframe operating systems, such as z/OS, have available a symbol table named *Associated data* (ADATA). The table is stored in a file that can be produced by the IBM High-Level Assembler (HLASM), IBM's COBOL compiler, and IBM's PL/I compiler, either as a separate SYSADATA file or as ADATA records in a Generalized object output file (GOFF). This obsoletes the TEST records from OS/360, although it is still possible to request them and to use them in the TSO TEST command.
- Windows uses a symbol table that is stored in a program database (.pdb) file.
- Most Unix-like operating systems have available symbol table formats named stabs and DWARF. In macOS and other Darwin-based operating systems, the debug symbols are stored in DWARF format in a separate .dSYM file.
