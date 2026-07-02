---
title: "RISC-V (part 2/3)"
source: https://en.wikipedia.org/wiki/RISC-V
domain: chisel-hdl
license: CC-BY-SA-4.0
tags: chisel hardware language, scala hardware, risc-v cores, rtl generation
fetched: 2026-07-02
part: 2/3
---

## Design

As a RISC architecture, the RISC-V ISA is a load–store architecture. Its floating-point instructions use IEEE 754 floating-point. Notable features of the RISC-V ISA include: instruction bit field locations chosen to simplify the use of multiplexers in a CPU, a design that is architecturally neutral, and a fixed location for the sign bit of immediate values to speed up sign extension.

The instruction set is designed for a wide range of uses. The base instruction set has a fixed length of 32-bit naturally aligned instructions, and the ISA supports variable length extensions where each instruction can be any number of 16-bit parcels in length. Extensions support small embedded systems, personal computers, supercomputers with vector processors, and warehouse-scale parallel computers.

The instruction set specification defines 32-bit and 64-bit address space variants. The specification includes a description of a 128-bit flat address space variant, as an extrapolation of 32- and 64-bit variants, but the 128-bit ISA remains "not frozen" intentionally, because as of 2023, there is still little practical experience with such large memory systems.

Unlike other academic designs which are typically optimized only for simplicity of exposition, the designers intended that the RISC-V instruction set be usable for practical computers. As of June 2019, version 2.2 of the user-space ISA and version 1.11 of the privileged ISA are frozen, permitting software and hardware development to proceed. The user-space ISA, now renamed the Unprivileged ISA, was updated, ratified and frozen as version 20191213. An external debug specification is available as a draft, version 0.13.2.

### Register sets

| Register name | Symbolic name | Description | Saved by |
|---|---|---|---|
| 32 integer registers |   |   |   |
| x0 | zero | Always zero |   |
| x1 | ra | Return address | Caller |
| x2 | sp | Stack pointer | Callee |
| x3 | gp | Global pointer |   |
| x4 | tp | Thread pointer |   |
| x5 | t0 | Temporary / alternate return address | Caller |
| x6–7 | t1–2 | Temporaries | Caller |
| x8 | s0/fp | Saved register / frame pointer | Callee |
| x9 | s1 | Saved register | Callee |
| x10–11 | a0–1 | Function arguments / return values | Caller |
| x12–17 | a2–7 | Function arguments | Caller |
| x18–27 | s2–11 | Saved registers | Callee |
| x28–31 | t3–6 | Temporaries | Caller |
| 32 floating-point extension registers |   |   |   |
| f0–7 | ft0–7 | Floating-point temporaries | Caller |
| f8–9 | fs0–1 | Floating-point saved registers | Callee |
| f10–11 | fa0–1 | Floating-point arguments/return values | Caller |
| f12–17 | fa2–7 | Floating-point arguments | Caller |
| f18–27 | fs2–11 | Floating-point saved registers | Callee |
| f28–31 | ft8–11 | Floating-point temporaries | Caller |

RISC-V has 32 integer registers (or 16 in the embedded variant), and when the floating-point extension is implemented, an additional 32 floating-point registers. Except for memory access instructions, instructions address only registers.

The first integer register is a zero register, and the remainder are general-purpose registers. A store to the zero register has no effect, and a read always provides 0. Using the zero register as a placeholder makes for a simpler instruction set.

Control and status registers exist, but user-mode programs can access only those used for performance measurement and floating-point management.

No instructions exist to save and restore multiple registers. Those were thought to be needless, too complex, and perhaps too slow.

### Memory access

Like many RISC designs, RISC-V is a load–store architecture: instructions address only registers, with load and store instructions conveying data to and from memory.

Most load and store instructions include a 12-bit offset and two register identifiers. One register is the base register. The other register is the destination (for a load) or the source (for a store).

The offset is added to a base register to get the address. Forming the address as a base register plus offset allows single instructions to access data structures. For example, if the base register points to the top of a stack, single instructions can access a subroutine's local variables in the stack. Likewise the load and store instructions can access a record-style structure or a memory-mapped I/O device. Using the constant zero register as a base address allows single instructions to access memory near address zero.

Memory is addressed as 8-bit bytes, with instructions being in little-endian order, and with data being in the byte order defined by the execution environment interface in which code is running. Words, up to the register size, can be accessed with the load and store instructions.

RISC-V was originally specified as little-endian to resemble other familiar, successful computers, for example, x86. This also reduces a CPU's complexity and costs slightly less because it reads all sizes of words in the same order. For example, the RISC-V instruction set decodes starting at the lowest-addressed byte of the instruction. Big-endian and bi-endian variants were defined for support of legacy code bases that assume big-endianness. The privileged ISA defines bits in the mstatus and mstatush registers that indicate and, optionally, control whether M-mode, S-mode, and U-mode memory accesses other than instruction fetches are little-endian or big-endian; those bits may be read-only, in which case the endianness of the implementation is hardwired, or may be writable.

An execution environment interface may allow accessed memory addresses not to be aligned to their word width, but accesses to aligned addresses may be faster; for example, simple CPUs may implement unaligned accesses with slow software emulation driven from an alignment failure interrupt.

Like many RISC instruction sets (and some complex instruction set computer (CISC) instruction sets, such as x86 and IBM System/360 and its successors through z/Architecture), RISC-V lacks address-modes that write back to the registers. For example, it does not auto-increment.

RISC-V manages memory systems that are shared between CPUs or threads by ensuring a thread of execution always sees its memory operations in the programmed order. But between threads and I/O devices, RISC-V is simplified: it doesn't guarantee the order of memory operations, except by specific instructions, such as `fence`.

A `fence` instruction guarantees that the results of predecessor operations are visible to successor operations of other threads or I/O devices. `fence` can guarantee the order of combinations of both memory and memory-mapped I/O operations. E.g. it can separate memory read and write operations, without affecting I/O operations. Or, if a system can operate I/O devices in parallel with memory, `fence` doesn't force them to wait for each other. One CPU with one thread may decode `fence` as `nop`.

Some RISC CPUs (such as MIPS, PowerPC, DLX, and Berkeley's RISC-I) place 16 bits of offset in the loads and stores. They set the upper 16 bits by a *load upper word* instruction. This permits upper-halfword values to be set easily, without shifting bits. However, most use of the upper half-word instruction makes 32-bit constants, like addresses. RISC-V uses a SPARC-like combination of 12-bit offsets and 20-bit *set upper* instructions. The smaller 12-bit offset helps compact, 32-bit load and store instructions select two of 32 registers yet still have enough bits to support RISC-V's variable-length instruction coding.

### Immediates

RISC-V handles 32-bit constants and addresses with instructions that set the upper 20 bits of a 32-bit register. Load upper immediate `lui` loads 20 bits into bits 31 through 12. Then a second instruction such as `addi` can set the bottom 12 bits. Small numbers or addresses can be formed by using the zero register instead of `lui`.

This method is extended to permit position-independent code by adding an instruction, `auipc` that generates 20 upper address bits by adding an offset to the program counter and storing the result into a base register. This permits a program to generate 32-bit addresses that are relative to the program counter.

The base register can often be used as-is with the 12-bit offsets of the loads and stores. If needed, `addi` can set the lower 12 bits of a register. In 64-bit and 128-bit ISAs,`lui` and `auipc` sign-extend the result to get the larger address.

Some fast CPUs may interpret combinations of instructions as single *fused* instructions. `lui` or `auipc` are good candidates to fuse with `jalr`, `addi`, loads or stores.

### Subroutine calls, jumps, and branches

RISC-V's subroutine call `jal` (jump and link) places its return address in a register. This is faster in many computer designs, because it saves a memory access compared to systems that push a return address directly on a stack in memory. `jal` has a 20-bit signed (two's complement) offset. The offset is multiplied by 2, then added to the PC (program counter) to generate a relative address to a 32-bit instruction. If the resulting address is not 32-bit aligned (i.e. evenly divisible by 4), the CPU may force an exception.

RISC-V CPUs jump to calculated addresses using a *jump and link-register*, `jalr` instruction. `jalr` is similar to `jal`, but gets its destination address by adding a 12-bit offset to a base register. (In contrast,`jal` adds a larger 20-bit offset to the PC.)

`jalr`'s bit format is like the register-relative loads and stores. Like them, `jalr` can be used with the instructions that set the upper 20 bits of a base register to make 32-bit branches, either to an absolute address (using `lui`) or a PC-relative one (using `auipc` for position-independent code). (Using a constant zero base address allows single-instruction calls to a small (the offset), fixed positive or negative address.)

RISC-V recycles `jal` and `jalr` to get unconditional 20-bit PC-relative jumps and unconditional register-based 12-bit jumps. Jumps just make the linkage register 0 so that no return address is saved.

RISC-V also recycles `jalr` to return from a subroutine: To do this, `jalr`'s base register is set to be the linkage register saved by `jal` or `jalr`. `jalr`'s offset is zero and the linkage register is zero, so that there is no offset, and no return address is saved.

Like many RISC designs, in a subroutine call, a RISC-V compiler must use individual instructions to save registers to the stack at the start, and then restore these from the stack on exit. RISC-V has no *save multiple* or *restore multiple* register instructions. These were thought to make the CPU too complex, and possibly slow. This can take more code space. Designers planned to reduce code size with library routines to save and restore registers.

RISC-V has no condition code register or carry bit. The designers believed that condition codes make fast CPUs more complex by forcing interactions between instructions in different stages of execution. This choice makes multiple-precision arithmetic more complex. Also, a few numerical tasks need more energy. As a result, predication (the conditional execution of instructions) is not supported. The designers claim that very fast, out-of-order CPU designs do predication anyway, by doing the comparison branch and conditional code in parallel, then discarding the unused path's effects. They also claim that even in simpler CPUs, predication is less valuable than branch prediction, which can prevent most stalls associated with conditional branches. Code without predication is larger, with more branches, but they also claim that a compressed instruction set (such as RISC-V's set *C*) solves that problem in most cases.

Instead, RISC-V has short branches that perform comparisons: equal, not-equal, less-than, unsigned less-than, greater-than or equal and unsigned greater-than or equal. Ten comparison-branch operations are implemented with only six instructions, by reversing the order of operands in the assembler. For example, *branch if greater than* can be done by *less-than* with a reversed order of operands.

The comparing branches have a twelve-bit signed range, and jump relative to the PC.

Unlike some RISC architectures, RISC-V does not include a branch delay slot, a position after a branch instruction that can be filled with an instruction that is executed whether or not the branch is taken. RISC-V omits a branch delay slot because it complicates multicycle CPUs, superscalar CPUs, and long pipelines. Dynamic branch predictors have succeeded well enough to reduce the need for delayed branches.

On the first encounter with a branch, RISC-V CPUs should assume that a negative relative branch (i.e. the sign bit of the offset is "1") will be taken. This assumes that a backward branch is a loop, and provides a default direction so that simple pipelined CPUs can fill their pipeline of instructions. Other than this, RISC-V does not require branch prediction, but core implementations are allowed to add it. RV32I reserves a "HINT" instruction space that presently does not contain any hints on branches; RV64I does the same.

### Arithmetic and logic sets

RISC-V segregates math into a minimal set of integer instructions (set *I*) with add, subtract, shift, bitwise logic and comparing-branches. These can simulate most of the other RISC-V instruction sets with software. (The atomic instructions are a notable exception.) RISC-V integer instructions lack the *count leading zero* and bit-field operations normally used to speed up software floating-point in a pure-integer processor, however, while nominally in the bit manipulation extension, the ratified Zbb, Zba and Zbs extensions contain further integer instructions including a count leading zero instruction.

The integer multiplication instructions (set *M*) include signed and unsigned multiply and divide. Double-precision integer multiplies and divides are included, as multiplies and divides that produce the *high word* of the result. The ISA document recommends that implementors of CPUs and compilers *fuse* a standardized sequence of high and low multiply and divide instructions to one operation if possible.

The floating-point instructions (set *F*) include single-precision arithmetic and also comparison-branches similar to the integer arithmetic. It requires an additional set of 32 floating-point registers. These are separate from the integer registers. The double-precision floating point instructions (set *D*) generally assume that the floating-point registers are 64-bit (i.e., double-width), and the *F* subset is coordinated with the *D* set. A quad-precision 128-bit floating-point ISA (*Q*) is also defined. RISC-V computers without floating-point can use a floating-point software library.

RISC-V does not cause exceptions on arithmetic errors, including overflow, underflow, subnormal, and divide by zero. Instead, both integer and floating-point arithmetic produce reasonable default values, and floating-point instructions set status bits. Divide-by-zero can be discovered by one branch after the division. The status bits can be tested by an operating system or periodic interrupt.

### Atomic memory operations

RISC-V supports computers that share memory between multiple CPUs and threads. RISC-V's standard memory consistency model is release consistency. That is, loads and stores may generally be reordered, but some loads may be designated as *acquire* operations which must precede later memory accesses, and some stores may be designated as *release* operations which must follow earlier memory accesses.

The base instruction set includes minimal support in the form of a `fence` instruction to enforce memory ordering. Although this is sufficient (`fence r, rw` provides *acquire* and `fence rw, w` provides *release*), combined operations can be more efficient.

The atomic memory operation extension supports two types of atomic memory operations for release consistency. First, it provides general purpose *load-reserved* `lr` and *store-conditional* `sc` instructions. `lr` performs a load, and tries to reserve that address for its thread. A later store-conditional `sc` to the reserved address will be performed only if the reservation is not broken by an intervening store from another source. If the store succeeds, a zero is placed in a register. If it failed, a non-zero value indicates that software needs to retry the operation. In either case, the reservation is released.

The second group of atomic instructions perform read-modify-write sequences: a load (which is optionally a load-acquire) to a destination register, then an operation between the loaded value and a source register, then a store of the result (which may optionally be a store-release). Making the memory barriers optional permits combining the operations. The optional operations are enabled by *acquire* and *release* bits which are present in every atomic instruction. RISC-V defines nine possible operations: swap (use source register value directly); add; bitwise and, or, and exclusive-or; and signed and unsigned minimum and maximum.

A system design may optimize these combined operations more than `lr` and `sc`. For example, if the destination register for a swap is the constant zero, the load may be skipped. If the value stored is unmodified since the load, the store may be skipped.

The IBM System/370 and its successors including z/Architecture, and x86, both implement a compare-and-swap (`cas`) instruction, which tests and conditionally updates a location in memory: if the location contains an expected old value, `cas` replaces it with a given new value; it then returns an indication of whether it made the change. However, a simple load-type instruction is usually performed before the `cas` to fetch the old value. The classic problem is that if a thread reads (loads) a value *A*, calculates a new value *C*, and then uses (`cas`) to replace *A* with *C*, it has no way to know whether concurrent activity in another thread has replaced *A* with some other value *B* and then restored the *A* in between. In some algorithms (e.g., ones in which the values in memory are pointers to dynamically allocated blocks), this ABA problem can lead to incorrect results. The most common solution employs a *double-wide `cas`* instruction to update both the pointer and an adjacent counter; unfortunately, such an instruction requires a special instruction format to specify multiple registers, performs several reads and writes, and can have complex bus operation.

The `lr`/`sc` alternative is more efficient. It usually requires only one memory load, and minimizing slow memory operations is desirable. It's also exact: it controls all accesses to the memory cell, rather than just assuring a bit pattern. However, unlike `cas`, it can permit livelock, in which two or more threads repeatedly cause each other's instructions to fail. RISC-V guarantees forward progress (no livelock) if the code follows rules on the timing and sequence of instructions: 1) It must use only the *I* subset. 2) To prevent repetitive cache misses, the code (including the retry loop) must occupy no more than 16 consecutive instructions. 3) It must include no system or fence instructions, or taken backward branches between the `lr` and `sc`. 4) The backward branch to the retry loop must be to the original sequence.

The specification gives an example of how to use the read-modify-write atomic instructions to lock a data structure.

### Compressed subset

The standard RISC-V ISA specifies that all instructions are 32 bits. This makes for a particularly simple implementation, but like other RISC processors with 32-bit instruction encoding, results in larger code size than in instruction sets with variable-length instructions.

To compensate, RISC-V's *32-bit* instructions are actually 30 bits; 3⁄4 of the opcode space is reserved for an optional (but recommended) variable-length *compressed* instruction set, RVC, that includes 16-bit instructions. As in SuperH, ARM Thumb, and MIPS16, the compressed instructions are simply alternative encodings for a subset of the larger instructions. Like SuperH, but unlike the ARM or MIPS compressed sets, space was reserved from the start so there is no separate operating mode. Standard and compressed instructions may be intermixed freely. (Extension letter is *C*.)

Because (like Thumb-1 and MIPS16) the compressed instructions are simply alternate encodings (aliases) for a selected subset of larger instructions, the compression can be implemented in the assembler, and it is not essential for the compiler to even know about it.

A prototype of RVC was tested in 2011. The prototype code was 20% smaller than an x86 PC and MIPS compressed code, and 2% larger than ARM Thumb-2 code. It also substantially reduced both the needed cache memory and the estimated power use of the memory system.

The researcher intended to reduce the code's binary size for small computers, especially embedded computer systems. The prototype included 33 of the most frequently used instructions, recoded as compact 16-bit formats using operation codes previously reserved for the compressed set. The compression was done in the assembler, with no changes to the compiler. Compressed instructions omitted fields that are often zero, used small immediate values or accessed subsets (16 or 8) of the registers. `addi` is very common and often compressible.

Much of the difference in size compared to ARM's Thumb set occurred because RISC-V, and the prototype, have no instructions to save and restore multiple registers. Instead, the compiler generated conventional instructions that access the stack. The prototype RVC assembler then often converted these to compressed forms that were half the size. However, this still took more code space than the ARM instructions that save and restore multiple registers. The researcher proposed to modify the compiler to call library routines to save and restore registers. These routines would tend to remain in a code cache and thus run fast, though probably not as fast as a save-multiple instruction.

Standard RVC requires occasional use of 32-bit instructions. Several nonstandard RVC proposals are complete, requiring no 32-bit instructions, and are said to have higher densities than standard RVC. Another proposal builds on these, and claims to use less coding range as well.

### Embedded subset

An instruction set for the smallest *embedded* CPUs (set E) is reduced in other ways: Only 16 of the 32 integer registers are supported. All current extensions may be used; a floating-point extension to use the integer registers for floating-point values is being considered. The privileged instruction set supports only machine mode, user mode and memory schemes that use base-and-bound address relocation.

Discussion has occurred for a microcontroller profile for RISC-V, to ease development of deeply embedded systems. It centers on faster, simple C-language support for interrupts, simplified security modes and a simplified POSIX application binary interface.

Correspondents have also proposed smaller, non-standard, 16-bit *RV16E* ISAs: Several serious proposals would use the 16-bit *C* instructions with 8 × 16-bit registers. An April fools' joke proposed a very practical arrangement: Utilize 16 × 16-bit integer registers, with the standard *EIMC* ISAs (including 32-bit instructions.) The joke was to use bank switching when a 32-bit CPU would be clearly superior with the larger address space.

### Privileged instruction set

RISC-V's ISA includes a separate privileged instruction set specification, which mostly describes three privilege levels plus an orthogonal hypervisor mode. As of December 2021, version 1.12 is ratified by RISC-V International.

Version 1.12 of the specification supports several types of computer systems:

1. Systems that have only *machine mode*, perhaps for simple embedded systems,
2. Systems with both machine mode (for a simple supervisor) and user-mode to implement relatively secure embedded systems,
3. Systems with machine-mode, supervisor mode (for operating system) and user-modes for typical operating systems.

These correspond roughly to systems with up to four ‘’rings’’ of privilege and security, at most: machine, hypervisor, supervisor and user. Each layer also is expected to have a thin layer of standardized supporting software that communicates to a more-privileged layer, or hardware.

The ISA also includes a hypervisor mode that is orthogonal to the user and supervisor modes. The basic feature is a configuration bit that either permits supervisor-level code to access hypervisor registers, or causes an interrupt on accesses. This bit lets supervisor mode directly handle the hardware needed by a hypervisor. This simplifies the implementation of hypervisors that are hosted by an operating system. This is a popular mode to run warehouse-scale computers. To support non-hosted hypervisors, the bit can cause these accesses to interrupt to a hypervisor. The design also simplifies nesting of hypervisors, in which a hypervisor runs under a hypervisor, and if necessary it lets the kernel use hypervisor features within its own kernel code. As a result, the hypervisor form of the ISA supports five modes: machine, supervisor, user, supervisor-under-hypervisor and user-under-supervisor.

The privileged instruction set specification explicitly defines *hardware threads*, or *harts*. Multiple hardware threads are a common practice in more-capable computers. When one thread is stalled, waiting for memory, others can often proceed. Hardware threads can help make better use of the large number of registers and execution units in fast out-of-order CPUs. Finally, hardware threads can be a simple, powerful way to handle interrupts: No saving or restoring of registers is required, simply executing a different hardware thread. However, the only hardware thread required in a RISC-V computer is thread zero.

Interrupts and exceptions are handled together. Exceptions are caused by instruction execution including illegal instructions and system calls, while interrupts are caused by external events. The existing control and status register definitions support RISC-V's error and memory exceptions, and a small number of interrupts, typically via an "advanced core local interruptor" (ACLINT). For systems with more interrupts, the specification also defines a platform-level interrupt controller (PLIC) to coordinate large number of interrupts among multiple processors. Interrupts always start at the highest-privileged machine level, and the control registers of each level have explicit *forwarding* bits to route interrupts to less-privileged code. For example, the hypervisor need not include software that executes on each interrupt to forward an interrupt to an operating system. Instead, on set-up, it can set bits to forward the interrupt.

Several memory systems are supported in the specification. Physical-only is suited to the simplest embedded systems. There are also four UNIX-style virtual memory systems for memory cached in mass-storage systems. The virtual memory systems support MMU with four sizes, with addresses sized 32, 39, 48 and 57 bits. All virtual memory systems support 4 KiB pages, multilevel page-table trees and use very similar algorithms to walk the page table trees. All are designed for either hardware or software page-table walking. To optionally reduce the cost of page table walks, super-sized pages may be leaf pages in higher levels of a system's page table tree. SV32 is only supported on 32-bit implementations, has a two-layer page table tree and supports 4 MiB superpages. SV39 has a three level page table, and supports 2 MiB superpages and 1 GiB gigapages. SV48 is required to support SV39. It also has a 4-level page table and supports 2 MiB superpages, 1 GiB gigapages, and 512 GiB terapages. SV57 has a 5-level page table and supports 2 MiB superpages, 1 GiB gigapages, 512 GiB terapages and 256 TiB petapages. Superpages are aligned on the page boundaries for the next-lowest size of page.

### Bit manipulation

Some bit-manipulation ISA extensions were ratified in November 2021 (Zba, Zbb, Zbc, Zbs). The Zba, Zbb, and Zbs extensions are arguably extensions of the standard I integer instructions: Zba contains instructions to speed up the computation of the addresses of array elements in arrays of datatypes of size 2, 4, or 8 bytes (sh1add, sh2add, sh3add), and for 64 (and 128) bit processors when indexed with unsigned integers (add.uw, sh1add.uw, sh2add.uw, sh3add.uw and slli.uw). The Zbb instructions contains operations to count leading, trailing 0 bits or all 1 bits in a full and 32 word operations (clz, clzw, ctz, ctzw, cpop, cpopw), byte order reversion (rev8), logical instructions with negation of the second input (andn,orn, xnor), sign and zero extension (sext.b, sext.h, zext.h) that could not be provided as special cases of other instructions (andi, addiw, add.wu), min and max of (signed and unsigned) integers, (left and right) rotation of bits in a register and 32-bit words (rori,roriw, ror, rorw, rol, rolw), and a byte wise "or combine" operation which allows detection of a zero byte in a full register, useful for handling C-style null terminated strings functions. The Zbs extension allows setting, getting, clearing, and toggling individual bits in a register by their index (bseti, bset, bexti, bext, bclri, bclr, binvi,binv).

The Zbc extension has instructions for "carryless multiplication", which does the multiplication of polynomials over the Galois field GF(2) (clmul, clmulh, clmulr). These are useful for cryptography and CRC checks of data integrity.

Done well, a more specialised bit-manipulation subset can aid cryptographic, graphic, and mathematical operations. Further instructions that have been discussed include instructions to shift in ones, a generalized bit-reverse, shuffle and crossbar permutations, bit-field place, extract and deposit pack two words, bytes or halfwords in one register, CRC instructions, bit-matrix operations (RV64 only), conditional mix, conditional move, funnel shifts. The criteria for inclusion documented in the draft were compliant with RISC-V philosophies and ISA formats, substantial improvements in code density or speed (i.e., at least a 3-for-1 reduction in instructions), and substantial real-world applications, including preexisting compiler support. Version 0.93 of the bit-manipulation extension includes those instructions; some of them are now in version 1.0.1 of the scalar and entropy source instructions cryptography extension.

### Packed SIMD

Packed-SIMD instructions are widely used by commercial CPUs to inexpensively accelerate multimedia and other digital signal processing. For simple, cost-reduced RISC-V systems, the base ISA's specification proposed to use the floating-point registers' bits to perform parallel single instruction, multiple data (SIMD) sub-word arithmetic.

In 2017 a vendor published a more detailed proposal to the mailing list, and this can be cited as version 0.1. As of 2019, the efficiency of this proposed ISA varies from 2x to 5x a base CPU for a variety of DSP codecs. The proposal lacked instruction formats and a license assignment to RISC-V International, but it was reviewed by the mailing list. Some unpopular parts of this proposal were that it added a condition code, the first in a RISC-V design, linked adjacent registers (also a first), and has a loop counter that can be difficult to implement in some microarchitectures.

### Vector set

The proposed vector-processing instruction set may make the packed SIMD set obsolete. The designers hope to have enough flexibility that a CPU can implement vector instructions in a standard processor's registers. This would enable minimal implementations with similar performance to a multimedia ISA, as above. However, a true vector coprocessor could execute the same code with higher performance.

As of 19 September 2021, the vector extension is at version 1.0. It is a conservative, flexible design of a general-purpose mixed-precision vector processor, suitable to execute compute kernels. Code would port easily to CPUs with differing vector lengths, ideally without recompiling.

In contrast, short-vector SIMD extensions are less convenient. These are used in x86, ARM and PA-RISC. In these, a change in word-width forces a change to the instruction set to expand the vector registers (in the case of x86, from 64-bit MMX registers to 128-bit Streaming SIMD Extensions (SSE), to 256-bit Advanced Vector Extensions (AVX), and AVX-512). The result is a growing instruction set, and a need to port working code to the new instructions.

In the RISC-V vector ISA, rather than fix the vector length in the architecture, instructions (`vsetvli`, `vsetivli`, and `vsetvl`) are available which take a requested size and sets the vector length to the minimum of the hardware limit and the requested size. So, the RISC-V proposal is more like a Cray's long-vector design or ARM's Scalable Vector Extension. That is, each vector in up to 32 vectors is the same length.

The application specifies the total vector width it requires, and the processor determines the vector length it can provide with available on-chip resources. This takes the form of an instruction (`vsetcfg`) with four immediate operands, specifying the number of vector registers of each available width needed. The total must be no more than the addressable limit of 32, but may be less if the application does not require them all. The vector length is limited by the available on-chip storage divided by the number of bytes of storage needed for each entry. (Added hardware limits may also exist, which in turn may permit SIMD-style implementations.)

Outside of vector loops, the application can zero the number of requested vector registers, saving the operating system the work of preserving them on context switches.

The vector length is not only architecturally variable, but designed to vary at run time also. To achieve this flexibility, the instruction set is likely to use variable-width data paths and variable-type operations using polymorphic overloading. The plan is that these can reduce the size and complexity of the ISA and compiler.

Recent experimental vector processors with variable-width data paths also show profitable increases in operations per: second (speed), area (lower cost), and watt (longer battery life).

Unlike a typical modern graphics processing unit, there are no plans to provide special hardware to support branch predication. Instead, lower cost compiler-based predication will be used.

### External debug system

There is a preliminary specification for RISC-V's hardware-assisted debugger. The debugger will use a transport system such as Joint Test Action Group (JTAG) or Universal Serial Bus (USB) to access debug registers. A standard hardware debug interface may support either a *standardized abstract interface* or *instruction feeding*.

As of January 2017, the exact form of the *abstract interface* remains undefined, but proposals include a memory mapped system with standardized addresses for the registers of debug devices or a command register and a data register accessible to the communication system. Correspondents claim that similar systems are used by Freescale's background debug mode interface (BDM) for some CPUs, ARM, OpenRISC, and Aeroflex's LEON.

In *instruction feeding*, the CPU will process a debug exception to execute individual instructions written to a register. This may be supplemented with a data-passing register and a module to directly access the memory. Instruction feeding lets the debugger access the computer exactly as software would. It also minimizes changes in the CPU, and adapts to many types of CPU. This was said to be especially apt for RISC-V because it is designed explicitly for many types of computers. The data-passing register allows a debugger to write a data-movement loop to RAM, and then execute the loop to move data into or out of the computer at a speed near the maximum speed of the debug system's data channel. Correspondents say that similar systems are used by MIPS Technologies MIPS, Intel Quark, Tensilica's Xtensa, and for Freescale Power ISA CPUs' background debug mode interface (BDM).

A vendor proposed a hardware trace subsystem for standardization, donated a conforming design, and initiated a review. The proposal is for a hardware module that can trace code execution on most RISC-V CPUs. To reduce the data rate, and permit simpler or less-expensive paths for the trace data, the proposal does not generate trace data that can be calculated from a binary image of the code. It sends only data that indicates "uninferrable" paths through the program, such as which conditional branches are taken. To reduce the data rates, branches that can be calculated, such as unconditional branches, are not traced. The proposed interface between the module and the control unit is a logic signal for each uninferrable type of instruction. Addresses and other data are to be provided in a specialized bus attached to appropriate data sources in a CPU. The data structure sent to an external trace unit is a series of short messages with the needed data. The details of the data channel are intentionally not described in the proposal, because several are likely to make sense.
