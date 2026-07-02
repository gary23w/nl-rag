---
title: "Processor register"
source: https://en.wikipedia.org/wiki/Processor_register
domain: mips-assembly
license: CC-BY-SA-4.0
tags: mips assembly, mips architecture, mips isa, mips instruction set
fetched: 2026-07-02
---

# Processor register

A **processor register** is a quickly accessible storage location available to a computer's processor. Registers usually consist of a small amount of fast storage, although some registers have specific hardware functions, and may be read-only or write-only. In computer architecture, registers are typically addressed by mechanisms other than main memory, but may in some cases be assigned a memory address e.g. the DEC PDP-6/PDP-10 and the ICT 1900.

Almost all computers, whether load/store architecture or not, load items of data from a larger memory into registers where they are used for arithmetic operations, bitwise operations, and other operations, and are manipulated or tested by machine instructions. Manipulated items are then often stored back to main memory, either by the same instruction or by a subsequent one. Modern processors use either static or dynamic random-access memory (RAM) as main memory, with the latter usually accessed via one or more cache levels.

Processor registers are normally at the top of the memory hierarchy, and provide the fastest way to access data. The term normally refers only to the group of registers that are directly encoded as part of an instruction, as defined by the instruction set. However, modern high-performance CPUs often have duplicates of these "architectural registers" in order to improve performance via register renaming, allowing parallel and speculative execution. Modern x86 design acquired these techniques around 1995 with the releases of Pentium Pro, Cyrix 6x86, Nx586, and AMD K5.

When a computer program accesses the same data repeatedly, this is called locality of reference. Holding frequently used values in registers can be critical to a program's performance. Register allocation is performed either by a compiler in the code generation phase, or manually by an assembly language programmer.

## Size

Registers are normally measured by the number of bits they can hold, for example, an *8-bit register*, *32-bit register*, *64-bit register*, *128-bit register*, or more. In some instruction sets, the registers can operate in various modes, breaking down their storage memory into smaller parts (32-bit into four 8-bit ones, for instance) to which multiple data (vector, or one-dimensional array of data) can be loaded and operated upon at the same time. Typically it is implemented by adding extra registers that map their memory into a larger register. Processors that have the ability to execute single instructions on multiple data are called SIMD processors.

## Types

A processor often contains several kinds of registers, which can be classified according to the types of values they can store or the instructions that operate on them:

- ***User-accessible registers*** can be read or written by machine instructions. The most common division of user-accessible registers is a division into data registers and address registers.
  - ***Data registers*** can hold numeric data values such as integers and, in some architectures, floating-point numbers, as well as characters, small bit arrays, and other data.
    - On some older computers, a special data register known as the accumulator is used implicitly for many operations. Examples include IBM 704, the IBM 709 and successors, the PDP-1, the PDP-4/PDP-7/PDP-9/PDP-15, the PDP-5/PDP-8, HP 2100, and the Intel 8080.
  - ***Address registers*** hold addresses and are used by instructions that indirectly access primary memory.
    - Some processors contain registers that may only be used to hold an *address* or only to hold *numeric values* (in some cases used as an index register whose value is added as an offset from some address); others allow registers to hold either kind of quantity. A wide variety of possible addressing modes, used to specify the effective address of an operand, exist.
    - The ***stack and frame pointers*** are used to manage the call stack. Rarely, other data stacks are addressed by dedicated address registers (see stack machine).
  - ***General-purpose registers*** (*GPR*s) can store both data and addresses, i.e., they are combined data/address registers; in some architectures, the register file is *unified* so that the GPRs can store floating-point numbers as well.
  - ***Floating-point registers*** (*FPR*s) store floating-point numbers in many architectures.
  - ***Constant registers*** hold read-only values such as zero, one, or pi.
  - ***Vector registers*** hold data for vector processing done by SIMD instructions (Single Instruction, Multiple Data).
  - ***Status registers*** hold truth values often used to determine whether some instruction should or should not be executed.
  - ***Special-purpose registers*** (*SPR*s) hold some elements of the program state; they usually include the program counter, also called the instruction pointer, and the status register; the program counter and status register might be combined in a program status word (PSW) register. The aforementioned stack pointer is sometimes also included in this group. Embedded microprocessors, such as microcontrollers, can also have *special function registers* corresponding to specialized hardware elements.
  - ***Control registers*** are used to set the behaviour of system components such as the CPU.
    - ***Model-specific registers*** (also called *machine-specific registers*) store data and settings related to the processor itself. Because their meanings are attached to the design of a specific processor, they are not expected to remain standard between processor generations.
    - ***Memory type range registers*** (*MTRR*s)
- ***Internal registers*** are not accessible by instructions and are used internally for processor operations.
  - The ***instruction register*** holds the instruction currently being executed.
  - Registers related to fetching information from RAM, a collection of storage registers located on separate chips from the CPU:
    - ***Memory buffer register*** (*MBR*), also known as *memory data register* (*MDR*)
    - ***Memory address register*** (*MAR*)
- ***Architectural registers*** are the registers visible to software and are defined by an architecture. They may not correspond to the physical hardware if register renaming is being performed by the underlying hardware.

**Hardware registers** are similar, but occur outside CPUs.

In some architectures (such as SPARC and MIPS), the first or last register in the integer register file is a *pseudo-register* in that it is hardwired to always return zero when read (mostly to simplify indexing modes), and it cannot be overwritten. In Alpha, this is also done for the floating-point register file. As a result of this, register files are commonly quoted as having one register more than how many of them are actually usable; for example, 32 registers are quoted when only 31 of them fit within the above definition of a register.

## Examples

The following table shows the number of registers in several mainstream CPU architectures. Although all of the below-listed architectures are different, almost all are in a basic arrangement known as the von Neumann architecture, first proposed by the Hungarian-American mathematician John von Neumann. It is also noteworthy that the number of registers on GPUs is much higher than that on CPUs.

| Architecture | GPRs/data+address registers | FP registers | Notes |
|---|---|---|---|
| AT&T Hobbit | 000 | stack of 7 | All data manipulation instructions work solely within registers, and data must be moved into a register before processing. |
| Cray-1 | 8 scalar data, 8 address | 8 scalar, 8 vector (64 elements) | Scalar data registers can be integer or floating-point; also 64 scalar scratch-pad T registers and 64 address scratch-pad B registers |
| 4004 | 1 accumulator, 16 others | 000 |   |
| 8008 | 1 accumulator, 6 others | 000 | The A register is an accumulator to which all arithmetic is done; the H and L registers can be used in combination as an address register; all registers can be used as operands in load/store/move/increment/decrement instructions and as the source operand in arithmetic instructions. There is no floating-point unit (FPU) available. |
| 8080 | 1 accumulator, 6 others, 1 stack pointer | 000 | The A register is an accumulator to which all arithmetic is done. The register pairs B·C, D·E, and H·L can be used as address registers in some instructions but ALU instructions can only use H·L as a pointer to memory operands. All registers can be used as operands in load/store/move/increment/decrement instructions and as the source operand in arithmetic instructions. Floating-point processors intended for the 8080 were Intel 8231, AMD Am9511, and Intel 8232. They were also readily usable with the Z80 and similar processors. |
| Z80 | 17: 1 accumulator, 6 others, alternate set of 1 accumulator and 6 others, 2 index registers, 1 stack pointer | 000 | The Z80 expands on the register set of the 8080. The accumulator and flags can be swapped with an alternate. The other 6 registers can be swapped as a group with alternates. The new index registers (IX or IY plus displacement) can generally be substituted for HL. |
| 1802 | 1 8-bit accumulator, 16 16-bit registers | 000 | Any of the registers can be the program counter or the stack pointer. |
| iAPX432 | 000 | stack of 6 | Stack machine |
| 16-bit x86 | 008 | stack of 8 (if FP present) | The 8086/8088, 80186/80188, and 80286 processors, if provided an 8087, 80187 or 80287 co-processor for floating-point operations, support an 80-bit wide, 8 deep register stack with some instructions able to use registers relative to the top of the stack as operands; without a co-processor, no floating-point registers are supported. |
| IA-32 | 008 | stack of 8 (if FP present), 8 (if SSE/MMX present) | The 80386 processor requires an 80387 for floating-point operations, later processors had built-in floating-point, with both having an 80-bit wide, 8 deep register stack with some instructions able to use registers relative to the top of the stack as operands. The Pentium III and later had the SSE with additional 128-bit XMM registers. |
| x86-64 | 16 (or 32 if APX available) | 16 or 32 (if AVX-512 available) | FP registers are 128-bit XMM registers, later extended to 256-bit YMM registers with AVX/AVX2 and 512-bit ZMM0–ZMM31 registers with AVX-512. |
| Fairchild F8 | 1 accumulator, 64 scratchpad registers, 1 indirect scratchpad register (ISAR) | 000 | Instructions can directly reference the first 16 scratchpad registers and can access all scratchpad registers indirectly through the ISAR |
| COP400 | 1 accumulator, 1 pointer | 000 | Some later versions include a 2-bit stack pointer |
| Geode GX | 1 data, 1 address | 008 | Geode GX/Media GX/4x86/5x86 is the emulation of 486/Pentium compatible processor made by Cyrix/National Semiconductor. Like Transmeta, the processor had a translation layer that translated x86 code to native code and executed it. It does not support 128-bit SSE registers, just the 80387 stack of eight 80-bit floating-point registers, and partially supports 3DNow! from AMD. The native processor only contains 1 data and 1 address register for all purposes and it is translated into 4 paths of 32-bit naming registers r1 (base), r2 (data), r3 (back pointer), and r4 (stack pointer) within scratchpad SRAM for integer operations. |
| Sunplus μ'nSP | 8 (sp, r1-r4, bp, sr, pc) | 000 | A 16-bit processor from the Taiwanese company Sunplus Technology, notably used in VTech's V.Smile line of educational video game consoles, in addition to many plug-in TV games and off-brand consoles starting from the mid-2000s. |
| VM Labs Nuon | 000 | 001 | A 32-bit stack machine processor developed by VM Labs and specialized for multimedia. It can be found on the company's own Nuon DVD player console line and the Game Wave Family Entertainment System from ZaPit games. The design was heavily influenced by Intel's MMX technology; it contained a 128-byte unified stack cache for both vector and scalar instructions. The unified cache can be divided as eight 128-bit vector registers or thirty-two 32-bit SIMD scalar registers through bank renaming; there is no integer register in this architecture. |
| Nios II | 031 | 008 | Nios II is based on the MIPS IV instruction set and has 31 32-bit GPRs, with register 0 being hardwired to zero, and eight 64-bit floating-point registers |
| Motorola 6800 | 2 accumulators, 1 index, 1 stack | 000 |   |
| Motorola 68k | 8 data (d0–d7), 8 address (a0–a7) | 008 (if FP present) | Address register 8 (a7) is the stack pointer. 68000, 68010, 68012, 68020, and 68030 require an FPU for floating-point; 68040 had FPU built in. FP registers are 80-bit. |
| MSP430 | 0013 | 000 | 13 general purpose registers including stack pointer. Others: program counter, status register, and constant generator. |
| SuperH | 0016 | 006 | 16-bit instruction version (pre-SH-5) |
| Emotion Engine | 3(VU0)+ 32(VU1) | 32 SIMD (integrated in UV1) + 2 × 32 Vector (dedicated vector co-processor located nearby its GPU) | The Emotion Engine's main core (VU0) is a heavily modified DSP general core intended for general background tasks and it contains one 64-bit accumulator, two general data registers, and one 32-bit program counter. A modified MIPS III executable core (VU1) is for game data and protocol control, and it contains thirty-two 32-bit general-purpose registers for integer computation and thirty-two 128-bit SIMD registers for storing SIMD instructions, streaming data value and some integer calculation value, and one accumulator register for connecting general floating-point computation to the vector register file on the co-processor. The coprocessor is built via a 32-entry 128-bit vector register file (can only store vector values that pass from the accumulator in the CPU) and no integer registers are built in. Both the vector co-processor (VPU 0/1) and the Emotion Engine's entire main processor module (VU0 + VU1 + VPU0 + VPU1) are built based on a modified MIPS instructions set. The accumulator in this case is not general-purpose but control status. |
| CUDA | configurable, up to 255 per thread | Earlier generations allowed up to 127/63 registers per thread (Tesla/Fermi). The more registers are configured per thread, the fewer threads can run at the same time. Registers are 32 bits wide; double-precision floating-point numbers and 64-bit pointers therefore require two registers. It additionally has up to 8 predicate registers per thread. |   |
| CDC 6000 series | 016 | 008 | 8 'A' registers, A0–A7, hold 18-bit addresses; 8 'B' registers, B0–B7, hold 18-bit integer values (with B0 permanently set to zero); 8 'X' registers, X0–X7, hold 60 bits of integer or floating-point data. Seven of the eight 18-bit A registers were coupled to their corresponding X registers: setting any of the A1–A5 registers to a value caused a memory load of the contents of that address into the corresponding X register. Likewise, setting an address into registers A6 or A7 caused a memory store into that location in memory from X6 or X7. (Registers A0 and X0 were not coupled like this). |
| System/360, System/370, System/390, z/Architecture | 016 | 4 (if FP present); 16 in G5 and later S/390 models and z/Architecture | FP was optional in System/360, and always present in S/370 and later. In processors with the Vector Facility, there are 16 vector registers containing a machine-dependent number of 32-bit elements. Some registers are assigned a fixed purpose by calling conventions; for example, register 14 is used for subroutine return addresses and, for ELF ABIs, register 15 is used as a stack pointer. The S/390 G5 processor increased the number of floating-point registers to 16. |
| MMIX | 256 | 256 | An instruction set designed by Donald Knuth in the late 1990s for pedagogical purposes. |
| NS320xx | 008 | 008 (if FP present) |   |
| Xelerated X10 | 001 | 032 | A 32/40-bit stack machine-based network processor with a modified MIPS instruction set and a 128-bit floating-point unit. |
| Parallax Propeller | 000 | 002 | An eight-core 8/16-bit sliced stack machine controller with a simple logic circuit inside, it has 8 cog counters (cores), each containing three 8/16 bit special control registers with 32 bit x 512 stack RAM. However, it does not contain any general register for integer purposes. Unlike most shadow register files in modern processors and multi-core systems, all of the stack RAM in cog can be accessed in instruction level, which allows all of these cogs to act as a single general-purpose core if necessary. Floating-point unit is external and it contains two 80-bit vector registers. |
| Itanium | 128 | 128 | And 64 1-bit predicate registers and 8 branch registers. The FP registers are 82-bit. |
| SPARC | 031 | 032 | Global register 0 is hardwired to 0. Uses register windows. |
| IBM POWER | 032 | 032 | Also included are a link register, a count register, and a multiply quotient (MQ) register. |
| PowerPC/Power ISA | 032 | 032 | Also included are a link register and a count register. Processors supporting the Vector facility also have 32 128-bit vector registers. |
| Blackfin | 8 data, 2 accumulator, 6 address | 000 | Also included are a stack pointer and a frame pointer. Additional registers are used to implement zero-overhead loops and circular buffer DAGs (data address generators). |
| IBM Cell SPE | 128 | 128 general purpose registers, which can hold integer, address, or floating-point values |   |
| PDP-10 | 016 | All of the registers may be used generally (integer, float, stack pointer, jump, indexing, etc.). Every 36-bit memory (or register) word can also be manipulated as a half-word, which can be considered an (18-bit) address. Other word interpretations are used by certain instructions. In the original PDP-10 processors, these 16 GPRs also corresponded to main (i.e. core) memory locations 0–15; a hardware option called "fast memory" implemented the registers as separate ICs, and references to memory locations 0–15 referred to the IC registers. Later models implemented the registers as "fast memory" and continued to make memory locations 0–15 refer to them. Movement instructions take *(register, memory)* operands: `MOVE 1,2` is register-register, and `MOVE 1,1000` is memory-to-register. |   |
| PDP-11 | 007 | 006 (if FPP present) | R7 is the program counter. Any register can be a stack pointer but R6 is used for hardware interrupts and traps. |
| VAX | 016 | The general purpose registers are used for floating-point values as well. Three of the registers have special uses: R12 (Argument Pointer), R13 (Frame Pointer), and R14 (Stack Pointer), while R15 refers to the Program Counter. |   |
| Alpha | 031 | 031 | Registers R31 (integer) and F31 (floating-point) are hardwired to zero. |
| 6502 | 1 accumulator, 2 index, 1 stack | 000 | The A (accumulator) register is the destination for all ALU operations. X and Y are indirect and direct index registers (respectively). The S (stack pointer) register points to the top of stack. |
| W65C816S | 001 | 000 | 65c816 is the 16-bit successor of the 6502. X, Y, and D (Direct Page register) are condition registers and SP register are specific index only. Main accumulator extended to 16-bit (C) while keeping 8-bit (A) for compatibility and main registers can now address up to 24-bit (16-bit wide data instruction/24-bit memory address). |
| MeP | 004 | 008 | Media-embedded processor was a 32-bit processor developed by Toshiba with a modded 8080 instruction set. Only the A, B, C, and D registers are available through all modes (8/16/32-bit). It is incompatible with x86; however, it contains an 80-bit floating-point unit that is x87-compatible. |
| PIC microcontroller | 001 | 000 | The base PIC architecture has no mechanism to index memory. |
| AVR microcontroller | 032 | 000 |   |
| ARM 32-bit (ARM/A32, Thumb-2/T32) | 014 | Varies (up to 32) | r15 is the program counter, and not usable as a general purpose register; r13 is the stack pointer; r8–r13 can be switched out for others (banked) on a processor mode switch. Older versions had 26-bit addressing, and used upper bits of the program counter (r15) for status flags, making that register 32-bit. |
| ARM 32-bit (Thumb) | 008 | 016 | Version 1 of Thumb, which only supported access to registers r0 through r7 |
| ARM 64-bit (A64) | 031 | 032 | Register r31 is the stack pointer or hardwired to 0, depending on the context. |
| MIPS | 031 | 032 | Integer register 0 is hardwired to 0. |
| RISC-V | 031 | 032 | Integer register 0 is hardwired to 0. The RV32E variant, intended for systems with very limited resources, has 15 integer registers. |
| Epiphany | 64 (per core) | Each instruction controls whether registers are interpreted as integers or single precision floating point. Architecture is scalable to 4096 cores with 16 and 64 core implementations currently available. |   |

## Usage

The number of registers available on a processor and the operations that can be performed using those registers has a significant impact on the efficiency of code generated by optimizing compilers. The Strahler number of an expression tree gives the minimum number of registers required to evaluate that expression tree.
