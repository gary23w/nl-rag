---
title: "x86 assembly language"
source: https://en.wikipedia.org/wiki/X86_assembly_language
domain: x86-assembly
license: CC-BY-SA-4.0
tags: x86 assembly, assembly language, x86, x86-64, amd64, asm
fetched: 2026-07-02
---

# x86 assembly language

**x86 assembly language** is a family of low-level programming languages that are used to produce object code for the x86 class of processors. Previous evolutions of this family of languages provide backward compatibility with CPUs dating back to the Intel 8008 microprocessor, introduced in April 1972. As assembly languages, they are closely tied to the architecture's machine code instructions, allowing for precise control over hardware.

In x86 assembly languages, mnemonics are used to represent fundamental CPU instructions, making the code more human-readable compared to raw machine code. Each machine code instruction is an opcode which, in assembly, is replaced with a mnemonic. Each mnemonic corresponds to a basic operation performed by the processor, such as arithmetic calculations, data movement, or control flow decisions. Assembly languages are most commonly used in applications where performance and efficiency are critical. This includes real-time embedded systems, operating-system kernels, and device drivers, all of which may require direct manipulation of hardware resources.

Additionally, compilers for high-level programming languages sometimes generate assembly code as an intermediate step during the compilation process. This allows for optimization at the assembly level before producing the final machine code that the processor executes.

## Mnemonics and opcodes

Each instruction in the x86 assembly language is represented by a mnemonic which often combines with one or more operands to translate into one or more bytes known as an opcode. For example, the NOP instruction translates to the opcode 0x90, and the HLT instruction translates to 0xF4. There are potential opcodes without documented mnemonics, which different processors may interpret differently. Using such opcodes can cause a program to behave inconsistently or even generate exceptions on some processors.

## Syntax

x86 assembly language has two primary syntax branches: *Intel syntax* and *AT&T syntax*. Intel syntax is dominant in the DOS and Windows environments, while AT&T syntax is dominant in Unix-like systems, as Unix was originally developed at AT&T Bell Labs. Below is a summary of the main differences between *Intel syntax* and *AT&T syntax*:

|   | AT&T | Intel |
|---|---|---|
| Parameter order | movl $5, %eax Source before the destination. | mov eax, 5 Destination before source. |
| Parameter size | addl $0x24, %esp movslq %ecx, %rax paddd %xmm1, %xmm2 Mnemonics are suffixed with a letter indicating the size of the operands: *q* for qword (64 bits), *l* for long (dword, 32 bits), *w* for word (16 bits), and *b* for byte (8 bits). | add esp, 24h movsxd rax, ecx paddd xmm2, xmm1 Derived from the name of the register that is used (e.g. *rax, eax, ax, al* imply *q, l, w, b*, respectively). If the source or destination is not a register, the parameter size cannot be inferred and must be declared explicitly. sub byte ptr [esi], 20h Width-based names may still appear in instructions when they define a different operation. MOVSXD refers to sign extension with dword input, unlike MOVSX. SIMD registers have width-named instructions that determine how to split up the register. AT&T tends to keep the names unchanged, so PADDD is not renamed to "paddl". |
| Sigils | Immediate values prefixed with a "$", registers prefixed with a "%". | The assembler automatically detects the type of symbols; i.e., whether they are registers, constants or something else. |
| Effective addresses | movl offset(%ebx, %ecx, 4), %eax General syntax of `*displacement*(*base*, *index*, *scale*)`. | mov eax, [ebx + ecx*4 + offset] Arithmetic expressions in square brackets; additionally, size keywords like *byte*, *word*, or *dword* have to be used if the size cannot be determined from the operands. |

Many x86 assemblers use *Intel syntax*, including FASM, MASM, NASM, TASM, and YASM. The GNU Assembler, which originally used *AT&T syntax*, has supported both syntaxes since version 2.10 via the *`.intel_syntax`* directive. A quirk in the AT&T syntax for x86 is that x87 floating-point operands are reversed, an inherited bug from the original AT&T assembler.

The AT&T syntax is nearly universal across other architectures (retaining the same operand order for the `mov` instruction); it was originally designed for PDP-11 assembly and was inherited onto Unix-like systems. In contrast, the Intel syntax is specific to the x86 architecture and is the one used in the x86 platform's official documentation. The Intel 8080, which predates the x86 architecture, also uses the "destination-first" order for `mov` instruction.

### Reserved words

In most x86 assembly languages, the reserved words consist of two parts: mnemonics that translate to opcodes, and directives (or "pseudo-ops") that access features in the assembler program beyond the simple translation of opcodes. For a list of the former part, see x86 instruction listings. The latter part is highly assembler-dependent, with no such thing as a standard among Intel-syntax assemblers. AT&T-syntax assemblers share a common way of naming directives (all directives starts with a dot, like `.ascii`), and a number of basic directives such as `.ascii` and `.string` are broadly supported.

## Registers

x86 processors feature a set of registers that serve as storage for binary data and addresses during program execution. These registers are categorized into general-purpose registers, segment registers, the instruction pointer, the FLAGS register, and various extension registers introduced in later processor models. Each register has specific functions in addition to their general capabilities:

### General-purpose registers

These registers have conventional roles, but usage is not strictly enforced. Programs are generally free to use them for other purposes.

- AX (Accumulator register): Primarily used in arithmetic, logic, and data transfer operations. It is favored by instructions that perform multiplication and division, and by string load and store operations. Immediate ALU operations and exchanges with AX can be encoded more compactly.
- BX (Base register): Base pointer for memory access. It can hold the base address of data structures and is useful in indexed addressing modes. It is used with `XLAT`.
- CX (Count register): Serves as a counter in loop, string, and shift/rotate instructions. Iterative operations often use CX to determine the number of times a loop or operation should execute.
- DX (Data register): Used in conjunction with AX for multiplication and division operations that produce results larger than 16 bits. It also holds I/O port addresses for `IN` and `OUT` instructions.
- SP (Stack pointer): Points to the top of stack in memory. It is automatically updated during `PUSH` and `POP` operations.
- BP (Base Pointer): Points to the top of the call stack. It is primarily used to access function parameters and local variables within the call stack.
- SI (Source Index): Used as a pointer to the source in string and memory array operations. Instructions like `MOVS` (move string) use SI to read data from memory. Like BX, it can be used for indexing. It can be added to BP or BX for double indexing.
- DI (Destination Index): Serves as a pointer to the destination in string and memory array operations. It works alongside SI in instructions that copy or compare data, writing results to memory. Like BX, it can be used for indexing. It can be added to BP or BX for double indexing.

Along with the general registers there are additionally the:

- Instruction Pointer (IP): Holds the offset address of the next instruction to be executed within the code segment (CS). It points to the first byte of the next instruction. While the IP register cannot be read directly by programmers, its value changes through control flow instructions such as jumps, calls, and interrupts, which alter the flow of execution.
- FLAGS register: Contains a set of status, control, and system flags that reflect the outcome of operations and control the processor's operations.
- Segment registers (CS, DS, ES, SS): Determines where a 64k segment starts (FS and GS in were added to 80386 and later)
- Extra extension registers (MMX, 3DNow!, SSE, etc.) (Pentium & later only).

The x86 registers can be used by most instructions. For example, in Intel syntax:

```mw
mov ax, 1234h ; copies the value 1234hex (4660d) into register AX
```

```mw
mov bx, ax    ; copies the value of the AX register into the BX register
```

## Segmented addressing

The x86 architecture in real and virtual 8086 mode uses a process known as **segmentation** to address memory, not the **flat memory model** used in many other environments. Segmentation involves composing a memory address from two parts, a *segment* and an *offset*; the segment points to the beginning of a 64 KiB (64×210) group of addresses and the offset determines how far from this beginning address the desired address is. In segmented addressing, two registers are required for a complete memory address. One to hold the segment, the other to hold the offset. In order to translate back into a flat address, the segment value is shifted four bits left (equivalent to multiplication by 24 or 16) then added to the offset to form the full address, which allows breaking the 64k barrier through clever choice of addresses, though it makes programming considerably more complex.

In real mode/protected only, for example, if DS contains the hexadecimal number 0xDEAD and DX contains the number 0xCAFE they would together point to the memory address `0xDEAD * 0x10 + 0xCAFE == 0xEB5CE`. Therefore, the CPU can address up to 1,048,576 bytes (1 MiB) in real mode. By combining *segment* and *offset* values we find a 20-bit address.

The original IBM PC restricted programs to 640 KB but an expanded memory specification was used to implement a bank switching scheme that fell out of use when later operating systems, such as Windows, used the larger address ranges of newer processors and implemented their own virtual memory schemes.

Protected mode, starting with the Intel 80286, was utilized by OS/2. Several shortcomings, such as the inability to access the BIOS and the inability to switch back to real mode without resetting the processor, prevented widespread usage. The 80286 was also still limited to addressing memory in 16-bit segments, meaning only 216 bytes (64 kilobytes) could be accessed at a time. To access the extended functionality of the 80286, the operating system would set the processor into protected mode, enabling 24-bit addressing and thus 224 bytes of memory (16 megabytes).

In protected mode, the segment selector can be broken down into three parts: a 13-bit index, a *Table Indicator* bit that determines whether the entry is in the GDT or LDT and a 2-bit *Requested Privilege Level*; see x86 memory segmentation.

When referring to an address with a segment and an offset the notation of *segment:offset* is used, so in the above example the *flat address* 0xEB5CE can be written as 0xDEAD:0xCAFE or as a segment and offset register pair; DS:DX.

There are some special combinations of segment registers and general registers that point to important addresses:

- CS:IP (CS is *Code Segment*, IP is *Instruction Pointer*) points to the address where the processor will fetch the next byte of code.
- SS:SP (SS is *Stack Segment*, SP is *Stack Pointer*) points to the address of the top of the stack, i.e. the most recently pushed byte.
- SS:BP (SS is *Stack Segment*, BP is *Stack Frame Pointer*) points to the address of the top of the stack frame, i.e. the base of the data area in the call stack for the currently active subprogram.
- DS:SI (DS is *Data Segment*, SI is *Source Index*) is often used to point to string data that is about to be copied to ES:DI.
- ES:DI (ES is *Extra Segment*, DI is *Destination Index*) is typically used to point to the destination for a string copy, as mentioned above.

The Intel 80386 featured three operating modes: real mode, protected mode and virtual mode. The protected mode which debuted in the 80286 was extended to allow the 80386 to address up to 4 GB of memory, the all new virtual 8086 mode (*VM86*) made it possible to run one or more real mode programs in a protected environment which largely emulated real mode, though some programs were not compatible (typically as a result of memory addressing tricks or using unspecified op-codes).

The 32-bit flat memory model of the 80386's extended protected mode may be the most important feature change for the x86 processor family until AMD released x86-64 in 2003, as it helped drive large scale adoption of Windows 3.1 (which relied on protected mode) since Windows could now run many applications at once, including DOS applications, by using virtual memory and simple multitasking.

## Execution modes

The x86 processors support five modes of operation for x86 code, **Real Mode**, **Protected Mode**, **Long Mode**, **Virtual 86 Mode**, and **System Management Mode**, in which some instructions are available and others are not. A 16-bit subset of instructions is available on the 16-bit x86 processors, which are the 8086, 8088, 80186, 80188, and 80286. These instructions are available in real mode on all x86 processors, and in 16-bit protected mode (80286 onwards), additional instructions relating to protected mode are available. On the 80386 and later, 32-bit instructions (including later extensions) are also available in all modes, including real mode; on these CPUs, V86 mode and 32-bit protected mode are added, with additional instructions provided in these modes to manage their features. SMM, with some of its own special instructions, is available on some Intel i386SL, i486 and later CPUs. Finally, in long mode (AMD Opteron onwards), 64-bit instructions, and more registers, are also available. The instruction set is similar in each mode but memory addressing and word size vary, requiring different programming strategies.

The modes in which x86 code can be executed in are:

- Real mode (16-bit)
  - 20-bit segmented memory address space (meaning that only 1 MB of memory can be addressed— actually since 80286 a little more through HMA), direct software access to peripheral hardware, and no concept of memory protection or multitasking at the hardware level. Computers that use BIOS start up in this mode.
- Protected mode (16-bit and 32-bit)
  - Expands addressable physical memory to 16 MB and addressable virtual memory to 1 GB. Provides privilege levels and protected memory, which prevents programs from corrupting one another. 16-bit protected mode (used during the end of the DOS era) used a complex, multi-segmented memory model. 32-bit protected mode uses a simple, flat memory model.
- Long mode (64-bit)
  - Mostly an extension of the 32-bit (protected mode) instruction set, but unlike the 16–to–32-bit transition, many instructions were dropped in the 64-bit mode. Pioneered by AMD.
- Virtual 8086 mode (16-bit)
  - A special hybrid operating mode that allows real mode programs and operating systems to run while under the control of a protected mode supervisor operating system
- System Management Mode (16-bit)
  - Handles system-wide functions like power management, system hardware control, and proprietary OEM designed code. It is intended for use only by system firmware. All normal execution, including the operating system, is suspended. An alternate software system (which usually resides in the computer's firmware, or a hardware-assisted debugger) is then executed with high privileges.

### Switching modes

The processor runs in real mode immediately after power on, so an operating system kernel, or other program, must explicitly switch to another mode if it wishes to run in anything but real mode. Switching modes is accomplished by modifying certain bits of the processor's control registers after some preparation, and some additional setup may be required after the switch.

### Examples

With a computer running legacy BIOS, the BIOS and the boot loader run in Real mode. The 64-bit operating system kernel checks and switches the CPU into Long mode and then starts new kernel-mode threads running 64-bit code.

With a computer running UEFI, the UEFI firmware (except CSM and legacy Option ROM), the UEFI boot loader and the UEFI operating system kernel all run in Long mode.

## Instruction types

In general, the features of the modern x86 instruction set are:

- A compact encoding
  - Variable length and alignment independent (encoded as little endian, as is all data in the x86 architecture)
  - Mainly one-address and two-address instructions, that is to say, the first operand is also the destination.
  - Memory operands as both source and destination are supported (frequently used to read/write stack elements addressed using small immediate offsets).
  - Both general and implicit register usage; although all seven (counting `ebp`) general registers in 32-bit mode, and all fifteen (counting `rbp`) general registers in 64-bit mode, can be freely used as accumulators or for addressing, most of them are also *implicitly* used by certain (more or less) special instructions; affected registers must therefore be temporarily preserved (normally stacked), if active during such instruction sequences.
- Produces conditional flags implicitly through most integer ALU instructions.
- Supports various addressing modes including immediate, offset, and scaled index but not PC-relative, except jumps (introduced as an improvement in the x86-64 architecture).
- Includes floating point to a stack of registers.
- Contains special support for atomic read-modify-write instructions (`xchg`, `cmpxchg`/`cmpxchg8b`, `xadd`, and integer instructions which combine with the `lock` prefix)
- SIMD instructions (instructions which perform parallel simultaneous single instructions on many operands encoded in adjacent cells of wider registers).

### Stack instructions

The x86 architecture has hardware support for an execution stack mechanism. Instructions such as `push`, `pop`, `call` and `ret` are used with the properly set up stack to pass parameters, to allocate space for local data, and to save and restore call-return points. The `ret` *size* instruction is very useful for implementing space efficient (and fast) calling conventions where the callee is responsible for reclaiming stack space occupied by parameters.

When setting up a stack frame to hold local data of a recursive procedure there are several choices; the high level `enter` instruction (introduced with the 80186) takes a *procedure-nesting-depth* argument as well as a *local size* argument, and *may* be faster than more explicit manipulation of the registers (such as `push bp` ; `mov bp, sp` ; `sub sp, *size*`). Whether it is faster or slower depends on the particular x86-processor implementation as well as the calling convention used by the compiler, programmer or particular program code; most x86 code is intended to run on x86-processors from several manufacturers and on different technological generations of processors, which implies highly varying microarchitectures and microcode solutions as well as varying gate- and transistor-level design choices.

The full range of addressing modes (including *immediate* and *base+offset*) even for instructions such as `push` and `pop`, makes direct usage of the stack for integer, floating point and address data simple, as well as keeping the ABI specifications and mechanisms relatively simple compared to some RISC architectures (require more explicit call stack details).

### Integer ALU instructions

x86 assembly has the standard mathematical operations, `add`, `sub`, `neg`, `imul` and `idiv` (for signed integers), with `mul` and `div` (for unsigned integers); the logical operators `and`, `or`, `xor`, `not`; bitshift arithmetic and logical, `sal`/`sar` (for signed integers), `shl`/`shr` (for unsigned integers); rotate with and without carry, `rcl`/`rcr`, `rol`/`ror`, and a complement of BCD arithmetic instructions, `aaa`, `aad`, `daa`. Instructions such as `cmp` and `test` set the flags without altering operands.

### Floating-point instructions

x86 assembly language includes instructions for a stack-based floating-point unit (FPU). The FPU was an optional separate coprocessor for the 8086 through the 80386, it was an on-chip option for the 80486 series, and it is a standard feature in every Intel x86 CPU since the 80486, starting with the Pentium. The FPU instructions include addition, subtraction, negation, multiplication, division, remainder, square roots, integer truncation, fraction truncation, and scale by power of two. The operations also include conversion instructions, which can load or store a value from memory in any of the following formats: binary-coded decimal, 32-bit integer, 64-bit integer, 32-bit floating-point, 64-bit floating-point or 80-bit floating-point (upon loading, the value is converted to the currently used floating-point mode). x86 also includes a number of transcendental functions, including sine, cosine, tangent, arctangent, exponentiation with the base 2 and logarithms to bases 2, 10, or *e*.

The stack register to stack register format of the instructions is usually `f*op* st, st(*n*)` or `f*op* st(*n*), st`, where `st` is equivalent to `st(0)`, and `st(*n*)` is one of the 8 stack registers (`st(0)`, `st(1)`, ..., `st(7)`). Like the integers, the first operand is both the first source operand and the destination operand. `fsubr` and `fdivr` should be singled out as first swapping the source operands before performing the subtraction or division. The addition, subtraction, multiplication, division, store and comparison instructions include instruction modes that pop the top of the stack after their operation is complete. So, for example, `faddp st(1), st` performs the calculation `st(1) = st(1) + st(0)`, then removes `st(0)` from the top of stack, thus making what was the result in `st(1)` the top of the stack in `st(0)`.

### SIMD instructions

Modern x86 CPUs contain SIMD instructions, which largely perform the same operation in parallel on many values encoded in a wide SIMD register. Various instruction technologies support different operations on different register sets, but taken as complete whole (from MMX to SSE4.2) they include general computations on integer or floating-point arithmetic (addition, subtraction, multiplication, shift, minimization, maximization, comparison, division or square root). So for example, `paddw mm0, mm1` performs 4 parallel 16-bit (indicated by the `w`) integer adds (indicated by the `padd`) of `mm0` values to `mm1` and stores the result in `mm0`. Streaming SIMD Extensions or SSE also includes a floating-point mode in which only the very first value of the registers is actually modified (expanded in SSE2). Some other unusual instructions have been added including a sum of absolute differences (used for motion estimation in video compression, such as is done in MPEG) and a 16-bit multiply accumulation instruction (useful for software-based alpha-blending and digital filtering). SSE (since SSE3) and 3DNow! extensions include addition and subtraction instructions for treating paired floating-point values like complex numbers.

These instruction sets also include numerous fixed sub-word instructions for shuffling, inserting and extracting the values around within the registers. In addition there are instructions for moving data between the integer registers and XMM (used in SSE)/FPU (used in MMX) registers.

### Memory instructions

The x86 processor also includes complex addressing modes for addressing memory with an immediate offset, a register, a register with an offset, a scaled register with or without an offset, and a register with an optional offset and another scaled register. So for example, one can encode `mov eax, [Table + ebx + esi*4]` as a single instruction which loads 32 bits of data from the address computed as `(Table + ebx + esi * 4)` offset from the `ds` selector, and stores it to the `eax` register. In general x86 processors can load and use memory matched to the size of any register it is operating on. (The SIMD instructions also include half-load instructions.)

Most 2-operand x86 instructions, including integer ALU instructions, use a standard "addressing mode byte" often called the MOD-REG-R/M byte. Many 32-bit x86 instructions also have a SIB addressing mode byte that follows the MOD-REG-R/M byte.

In principle, because the instruction opcode is separate from the addressing mode byte, those instructions are orthogonal because any of those opcodes can be mixed-and-matched with any addressing mode. However, the x86 instruction set is generally considered non-orthogonal because most dyadic operations cannot operate memory to memory, other opcodes have some fixed addressing mode (they have no addressing mode byte), and every register has a preferred use.

The x86 instruction set includes string load, store, move, scan and compare instructions (`lods`, `stos`, `movs`, `scas` and `cmps`) which perform each operation to a specified size (`b` for 8-bit byte, `w` for 16-bit word, `d` for 32-bit double word) then increments/decrements (depending on DF, direction flag) the implicit address register (`si` for `lods`, `di` for `stos` and `scas`, and both for `movs` and `cmps`). For the load, store and scan operations, the implicit target/source/comparison register is in the `al`, `ax` or `eax` register (depending on size). The implicit segment registers used are `ds` for `si` and `es` for `di`. The `cx` or `ecx` register is used as a decrementing counter, and the operation stops when the counter reaches zero or, for scans and comparisons, when equality or inequality is detected. Unfortunately, over the years the performance of some of these instructions became neglected and in certain cases it is possible to get faster results by coding using more elemental instructions. Intel and AMD have refreshed some of the instructions though, and as of 2025 some have very respectable performance.

The stack is a region of memory and an associated *stack pointer*, which points to the last item pushed on the stack. The stack pointer is decremented before items are added, `push`, and incremented after things are removed, `pop`. In 16-bit mode, this implicit stack pointer is addressed as SS:[SP], in 32-bit mode it is SS:[ESP], and in 64-bit mode it is [RSP]. The stack pointer points to the last value that was stored, under the assumption that its size will match the operating mode of the processor (i.e., 16, 32, or 64 bits) to match the default width of the `push`/`pop`/`call`/`ret` instructions. Also included are the instructions `enter` and `leave` which reserve and remove data from the top of the stack while setting up a stack frame pointer in `bp`/`ebp`/`rbp`. However, direct setting, or addition and subtraction to the `sp`/`esp`/`rsp` register is also supported, so the `enter`/`leave` instructions are generally unnecessary.

This code is the beginning of a function typical for a high-level language when compiler optimisation is turned off for ease of debugging:

```mw
 push    rbp       ; Save the calling function’s stack frame pointer (rbp register)
 mov     rbp, rsp  ; Make a new stack frame below our caller’s stack
 sub     rsp, 32   ; Reserve 32 bytes of stack space for this function’s local variables.
                   ; Local variables will be below rbp and can be referenced relative to rbp,
                   ; again best for ease of debugging, but for best performance rbp will not
                   ; be used at all, and local variables would be referenced relative to rsp
                   ; because, apart from the code saving, rbp then is free for other uses.
  …       …        ; However, if rbp is altered here, its value should be preserved for the caller.
 mov [rbp-8], rdx  ; Example of writing to a local variable (by its memory location) from register rdx
```

...is functionally equivalent to just:

```mw
 enter   32, 0
```

Other instructions for manipulating the stack include `pushfd`(32-bit) / `pushfq`(64-bit) and `popfd/popfq` for storing and retrieving the EFLAGS (32-bit) / RFLAGS (64-bit) register.

Values for a SIMD load or store are assumed to be packed in adjacent positions for the SIMD register and will align them in sequential little-endian order. Some SSE load and store instructions require 16-byte alignment to function properly. The SIMD instruction sets also include "prefetch" instructions which perform the load but do not target any register, used for cache loading. The SSE instruction sets also include non-temporal store instructions which will perform stores straight to memory without performing a cache allocate if the destination is not already cached (otherwise it will behave like a regular store.)

Most generic integer and floating-point (but no SIMD) instructions can use one parameter as a complex address as the second source parameter. Integer instructions can also accept one memory parameter as a destination operand.

## Program flow

The x86 assembly has an unconditional jump operation, `jmp`, which can take an immediate address, a register or an indirect address as a parameter (note that most RISC processors only support a link register or short immediate displacement for jumping).

Also supported are several conditional jumps, including `jz` (jump on zero), `jnz` (jump on non-zero), `jg` (jump on greater than, signed), `jl` (jump on less than, signed), `ja` (jump on above/greater than, unsigned), `jb` (jump on below/less than, unsigned). These conditional operations are based on the state of specific bits in the (E)FLAGS register. Many arithmetic and logic operations set, clear or complement these flags depending on their result. The comparison `cmp` (compare) and `test` instructions set the flags as if they had performed a subtraction or a bitwise AND operation, respectively, without altering the values of the operands. There are also instructions such as `clc` (clear carry flag) and `cmc` (complement carry flag) which work on the flags directly. Floating point comparisons are performed via `fcom` or `ficom` instructions which eventually have to be converted to integer flags.

Each jump operation has three different forms, depending on the size of the operand. A *short* jump uses an 8-bit signed operand, which is a relative offset from the current instruction. A *near* jump is similar to a short jump but uses a 16-bit signed operand (in real or protected mode) or a 32-bit signed operand (in 32-bit protected mode only). A *far* jump is one that uses the full segment base:offset value as an absolute address. There are also indirect and indexed forms of each of these.

In addition to the simple jump operations, there are the `call` (call a subroutine) and `ret` (return from subroutine) instructions. Before transferring control to the subroutine, `call` pushes the offset address of the instruction following the `call` onto the stack; `ret` pops this value off the stack, and jumps to it, effectively returning the flow of control to that part of the program. In the case of a `far call`, the segment base is pushed followed by the offset; `far ret` pops the offset and then the segment base to return.

There are also two similar instructions, `int` (interrupt), which saves the current (E)FLAGS register value on the stack, then performs a `far call`, except that instead of an address, it uses an *interrupt vector*, an index into a table of interrupt handler addresses. Typically, the interrupt handler saves all other CPU registers it uses, unless they are used to return the result of an operation to the calling program (in software called interrupts). The matching return from interrupt instruction is `iret`, which restores the flags after returning. *Soft Interrupts* of the type described above are used by some operating systems for system calls, and can also be used in debugging hard interrupt handlers. *Hard interrupts* are triggered by external hardware events, and must preserve all register values as the state of the currently executing program is unknown. In Protected Mode, interrupts may be set up by the OS to trigger a task switch, which will automatically save all registers of the active task.

## Examples

The following examples use the so-called *Intel-syntax flavor*as used by the assemblers Microsoft MASM, NASM and many others. (Note: There is also an alternative *AT&T-syntax flavor* where the order of source and destination operands are swapped, among many other differences.)

### "Hello, world!" program with no OS

"Hello, world!" can be output with little help from an operating system. "Call outchr" calls some mechanism that prints a character in AL to the console. A non-zero length string must be terminated with a byte of zero. Note that this example is for a 16-bit Intel 8086.

```mw
hello:	        
   mov	si,msg      ; address of string into SI
   cld              ; Clear direction to increment SI
   lodsb            ; Load first char in AL, inc SI 
chrlp:
   call outchr      ; Print character in AL
   lodsb            ; Load next character in AL, inc SI 
   or al, al        ; Is it a zero terminator?
   jnz chrlp        ; If not, continue
   ret              ; Return to caller

msg: db 'Hello, world!', 0xa, 0x0  ; string to be printed
```

### "Hello world!" program for MS-DOS in MASM-style assembly

Using the software interrupt 21h instruction to call the MS-DOS operating system for output to the display – other samples use libc's C printf() routine to write to stdout. Note that this example uses 16-bit mode as on an Intel 8086. The next example is Intel 386 code in 32-bit mode. Modern code will be in 64-bit mode.

```mw
.model small
.stack 100h

.data
msg	db	'Hello world!$'

.code
start:
	mov	ah, 09h    ; Sets 8-bit register ‘ah’, the high byte of register ax, to 9, to
                   ; select a sub-function number of an MS-DOS routine called below
                   ; via the software interrupt int 21h to display a message
	lea	dx, msg    ; Takes the address of msg, stores the address in 16-bit register dx
	int	21h        ; Various MS-DOS routines are callable by the software interrupt 21h
                   ; Our required sub-function was set in register ah above

	mov	ax, 4C00h  ; Sets register ax to the sub-function number for MS-DOS’s software
                   ; interrupt int 21h for the service ‘terminate program’.
	int	21h        ; Calling this MS-DOS service never returns, as it ends the program.

end start
```

### "Hello world!" program for Windows in MASM and NASM style assembly

| ! MASM | NASM | Description |
|---|---|---|
| ; requires /coff switch on 6.15 and earlier versions .386 .model small,c .stack 1000h | ; Image base = 0x00400000 %define RVA(x) (x-0x00400000) | Preamble. MASM requires defining the address model and stack size. |
| .data msg db "Hello world!",0 | section .data msg db "Hello world!" | Data section. We use the db (define byte) pseudo-op to define a string. |
| .code includelib libcmt.lib includelib libvcruntime.lib includelib libucrt.lib includelib legacy_stdio_definitions.lib extrn printf:near extrn exit:near public main main proc push offset msg call printf push 0 call exit main endp end | section .text push dword msg call dword [printf] push byte +0 call dword [exit] ret section .idata dd RVA(msvcrt_LookupTable) dd -1 dd 0 dd RVA(msvcrt_string) dd RVA(msvcrt_imports) times 5 dd 0 ; ends the descriptor table msvcrt_string dd "msvcrt.dll", 0 msvcrt_LookupTable: dd RVA(msvcrt_printf) dd RVA(msvcrt_exit) dd 0 msvcrt_imports: printf dd RVA(msvcrt_printf) exit dd RVA(msvcrt_exit) dd 0 msvcrt_printf: dw 1 dw "printf", 0 msvcrt_exit: dw 2 dw "exit", 0 dd 0 | The code (.text section) and the import table. In NASM the import table is manually constructed, while in the MASM example directives are used to simplify the process. |

### "Hello world!" program for Linux in AT&T and NASM assembly

| AT&T (GNU as) | Intel (NASM) | Description |
|---|---|---|
| .data | section .data | Like in the Windows example, `.data` is the section for initialized data. |
| str: .ascii "Hello, world!\n" | str: db 'Hello world!', 0Ah | Define a string of text containing "Hello, world!" and then a new line (`\n`, which is `0x0A`). Bind the label "str" to the address of the defined string. |
| str_len = . - str | str_len: equ $ - str | Calculate the length of `str`. `.` means "here" in gas and `$` means the same in nasm. By subtracting "str" from "here", one gets the length of the previously defined string. |
| .text | section .text | Like in the Windows example, `.text` is the section for program code. |
| .globl _start | global _start | export the _start function to the global scope for it to be "seen" by the linker |
| _start: | _start: | Define a label called `_start`, to which we will write our subroutine. The name `_start`, by Linux convention, defines the entry point. |
| movl $4, %eax movl $1, %ebx movl $str, %ecx movl $str_len, %edx | mov eax, 4 mov ebx, 1 mov ecx, str mov edx, str_len | Prepare a system call. EAX=4 requests the "sys_write" call on Linux x86. EBX=1 means "stdout" for sys_write. ECX holds the string to write, and EDX holds the number of bytes to write. The is equivalent to the libc-wrapped version `write(1, str, str_len)`. |
| int $0x80 | int 80h | On x86, the system interrupt "80h" is used for invoking a system call according to the values of eax, ebx, ecx, and edx. |
| movl $1, %eax movl $0, %ebx int $0x80 | mov eax, 1 mov ebx, 0 int 80h | Load another system call, then call it with INT 80h: EAX=1 is sys_exit, and EBX for sys_exit holds the return value. A return value of 0 means a normal exit. In C syntax, `_exit(0);`. |

Note for NASM:

```mw
; This program runs in 32-bit protected mode.
;  build: nasm -f elf -F stabs name.asm
;  link:  ld -o name name.o
;
; In 64-bit long mode you can use 64-bit registers (e.g. rax instead of eax, rbx instead of ebx, etc.)
; Also change "-f elf " for "-f elf64" in build command.
; For 64-bit long mode, "lea rcx, str" would be the address of the message, note 64-bit register rcx.
```

### "Hello world!" program for Linux in NASM style assembly using the C standard library

```mw
;
;  This program runs in 32-bit protected mode.
;  gcc links the standard-C library by default

;  build: nasm -f elf -F stabs name.asm
;  link:  gcc -o name name.o
;
; In 64-bit long mode you can use 64-bit registers (e.g. rax instead of eax, rbx instead of ebx, etc..)
; Also change "-f elf " for "-f elf64" in build command.
;
        global  main                            ; ‘main’ must be defined, as it being compiled
                                                ; against the C Standard Library
        extern  printf                          ; declares the use of external symbol, as printf
                                                ; printf is declared in a different object-module.
                                                ; The linker resolves this symbol later.

segment .data                                   ; section for initialized data
	string db 'Hello world!', 0Ah, 0            ; message string ending with a newline char (10
                                                ; decimal) and the zero byte ‘NUL’ terminator
                                                ; ‘string’ now refers to the starting address
                                                ; at which 'Hello, World' is stored.

segment .text
main:
        push    string                          ; Push the address of ‘string’ onto the stack.
                                                ; This reduces esp by 4 bytes before storing
                                                ; the 4-byte address ‘string’ into memory at
                                                ; the new esp, the new bottom of the stack.
                                                ; This will be an argument to printf()

        call    printf                          ; calls the C printf() function.
        add     esp, 4                          ; Increases the stack-pointer by 4 to put it back
                                                ; to where it was before the ‘push’, which
                                                ; reduced it by 4 bytes.
        ret                                     ; Return to our caller.
```

Because the C runtime is used, we define a main() function as the C runtime expects. Instead of calling exit, we simply return from the main function to have the runtime perform the clean-up.

### "Hello world!" program for 64-bit mode Linux in NASM style assembly

This example is in modern 64-bit mode.

```mw
;  build: nasm -f elf64 -F dwarf hello.asm
;  link:  ld -o hello hello.o

DEFAULT REL			    ; use RIP-relative addressing modes by default, so [foo] = [rel foo]

SECTION .rodata			; read-only data should go in the .rodata section on GNU/Linux, like .rdata on Windows
Hello:		db "Hello world!", 10   ; Ending with a byte 10 = newline (ASCII LF)
len_Hello:	equ $-Hello             ; Get NASM to calculate the length as an assembly-time constant
                                    ; the ‘$’ symbol means ‘here’. write() takes a length so that
                                    ; a zero-terminated C-style string isn't needed.
                                    ; It would be for C puts()

SECTION .text

global _start
_start:
	mov eax, 1				; __NR_write syscall number from Linux asm/unistd_64.h (x86_64)
	mov edi, 1				; int fd = STDOUT_FILENO
	lea rsi, [rel Hello]			; x86-64 uses RIP-relative LEA to put static addresses into regs
	mov rdx, len_Hello		; size_t count = len_Hello
	syscall					; write(1, Hello, len_Hello);  call into the kernel to actually do the system call
     ;; return value in RAX.  RCX and R11 are also overwritten by syscall

	mov eax, 60				; __NR_exit call number (x86_64) is stored in register eax.
	xor edi, edi		    ; This zeros edi and also rdi.
                            ; This xor-self trick is the preferred common idiom for zeroing
                            ; a register, and is always by far the fastest method.
                            ; When a 32-bit value is stored into eg edx, the high bits 63:32 are
                            ; automatically zeroed too in every case. This saves you having to set
                            ; the bits with an extra instruction, as this is a case very commonly
                            ; needed, for an entire 64-bit register to be filled with a 32-bit value.
                            ; This sets our routine’s exit status = 0 (exit normally)
	syscall					; _exit(0)
```

Running it under strace verifies that no extra system calls are made in the process. The printf version would make many more system calls to initialize libc and do dynamic linking. But this is a static executable because we linked using ld without -pie or any shared libraries; the only instructions that run in user-space are the ones you provide.

```mw
$ strace ./hello > /dev/null                    # without a redirect, your program's stdout is mixed with strace's logging on stderr.  Which is normally fine
execve("./hello", ["./hello"], 0x7ffc8b0b3570 /* 51 vars */) = 0
write(1, "Hello world!\n", 13)          = 13
exit(0)                                 = ?
+++ exited with 0 +++
```

### Using the flags register

Flags are heavily used for comparisons in the x86 architecture. When a comparison is made between two data, the CPU sets the relevant flag or flags. Following this, conditional jump instructions can be used to check the flags and branch to code that should run, e.g.:

```mw
	cmp	eax, ebx
	jne	do_something
	; ...
do_something:
	; do something here
```

Aside, from compare instructions, there are a great many arithmetic and other instructions that set bits in the flags register. Other examples are the instructions sub, test and add and there are many more. Common combinations such as cmp + conditional jump are internally ‘fused’ (‘macro fusion’) into one single micro-instruction (μ-op) and are fast provided the processor can guess which way the conditional jump will go, jump vs continue.

The flags register are also used in the x86 architecture to turn on and off certain features or execution modes. For example, to disable all maskable interrupts, you can use the instruction:

```mw
	cli
```

The flags register can also be directly accessed. The low 8 bits of the flag register can be loaded into `ah` using the `lahf` instruction. The entire flags register can also be moved on and off the stack using the instructions `pushfd/pushfq`, `popfd/popfq`, `int` (including `into`) and `iret`.

The x87 floating point maths subsystem also has its own independent ‘flags’-type register the fp status word. In the 1990s it was an awkward and slow procedure to access the flag bits in this register, but on modern processors there are ‘compare two floating point values’ instructions that can be used with the normal conditional jump/branch instructions directly without any intervening steps.

### Using the instruction pointer register

The instruction pointer is called `ip` in 16-bit mode, `eip` in 32-bit mode, and `rip` in 64-bit mode. The instruction pointer register points to the address of the next instruction that the processor will attempt to execute. It cannot be directly accessed in 16-bit or 32-bit mode, but a sequence like the following can be written to put the address of `next_line` into `eax` (32-bit code):

```mw
	call	next_line
next_line:
	pop	eax
```

Writing to the instruction pointer is simple — a `jmp` instruction stores the given target address into the instruction pointer to, so, for example, a sequence like the following will put the contents of `rax` into `rip` (64-bit code):

```mw
	jmp	rax
```

In 64-bit mode, instructions can reference data relative to the instruction pointer, so there is less need to copy the value of the instruction pointer to another register.
