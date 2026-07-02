---
title: "List of x86 instructions (part 5/5)"
source: https://en.wikipedia.org/wiki/X86_instruction_listings
domain: x86-assembly
license: CC-BY-SA-4.0
tags: x86 assembly, assembly language, x86, x86-64, amd64, asm
fetched: 2026-07-02
part: 5/5
---

## x87 floating-point instructions

The x87 coprocessor, if present, provides support for floating-point arithmetic. The coprocessor provides eight data registers, each holding one 80-bit floating-point value (1 sign bit, 15 exponent bits, 64 mantissa bits) – these registers are organized as a stack, with the top-of-stack register referred to as "st" or "st(0)", and the other registers referred to as st(1), st(2), ...st(7). It additionally provides a number of control and status registers, including "PC" (precision control, to control whether floating-point operations should be rounded to 24, 53 or 64 mantissa bits) and "RC" (rounding control, to pick rounding-mode: round-to-zero, round-to-positive-infinity, round-to-negative-infinity, round-to-nearest-even) and a 4-bit condition code register "CC", whose four bits are individually referred to as C0, C1, C2 and C3). Not all of the arithmetic instructions provided by x87 obey PC and RC.

### Original 8087 instructions

| Instruction description | Mnemonic | Opcode | Additional items |   |
|---|---|---|---|---|
|   |   |   |   |   |
| x87 Non-Waiting FPU Control Instructions | Waiting mnemonic |   |   |   |
| Initialize x87 FPU | `FNINIT` | `DB E3` | `FINIT` |   |
| Load x87 Control Word | `FLDCW m16` | `D9 /5` | (none) |   |
| Store x87 Control Word | `FNSTCW m16` | `D9 /7` | `FSTCW` |   |
| Store x87 Status Word | `FNSTSW m16` | `DD /7` | `FSTSW` |   |
| Clear x87 Exception Flags | `FNCLEX` | `DB E2` | `FCLEX` |   |
| Load x87 FPU Environment | `FLDENV m112/m224` | `D9 /4` | (none) |   |
| Store x87 FPU Environment, then mask all x87 exceptions | `FNSTENV m112/m224` | `D9 /6` | `FSTENV` |   |
| Save x87 FPU State, then initialize x87 FPU | `FNSAVE m752/m864` | `DD /6` | `FSAVE` |   |
| Restore x87 FPU State | `FRSTOR m752/m864` | `DD /4` | (none) |   |
| Enable Interrupts (8087 only) | `FNENI` | `DB E0` | `FENI` |   |
| Disable Interrupts (8087 only) | `FNDISI` | `DB E1` | `FDISI` |   |
|   |   |   |   |   |
| x87 Floating-point Load/Store/Move Instructions | precision control | rounding control |   |   |
| Load floating-point value onto stack | `FLD m32` | `D9 /0` | No | —N/a |
| `FLD m64` | `DD /0` |   |   |   |
| `FLD m80` | `DB /5` |   |   |   |
| `FLD st(i)` | `D9 C0+i` |   |   |   |
| Store top-of-stack floating-point value to memory or stack register | `FST m32` | `D9 /2` | No | Yes |
| `FST m64` | `DD /2` |   |   |   |
| `FST st(i)` | `DD D0+i` | No | —N/a |   |
| Store top-of-stack floating-point value to memory or stack register, then pop | `FSTP m32` | `D9 /3` | No | Yes |
| `FSTP m64` | `DD /3` |   |   |   |
| `FSTP m80` | `DB /7` | No | —N/a |   |
| `FSTP st(i)` | `DD D8+i` |   |   |   |
| DF D0+i |   |   |   |   |
| DF D8+i |   |   |   |   |
| Push +0.0 onto stack | `FLDZ` | `D9 EE` | No | —N/a |
| Push +1.0 onto stack | `FLD1` | `D9 E8` |   |   |
| Push π (approximately 3.14159) onto stack | `FLDPI` | `D9 EB` | No | 387 |
| Push $\log _{2}\left(10\right)$ (approximately 3.32193) onto stack | `FLDL2T` | `D9 E9` |   |   |
| Push $\log _{2}\left(e\right)$ (approximately 1.44269) onto stack | `FLDL2E` | `D9 EA` |   |   |
| Push $\log _{10}\left(2\right)$ (approximately 0.30103) onto stack | `FLDLG2` | `D9 EC` |   |   |
| Push $\ln \left(2\right)$ (approximately 0.69315) onto stack | `FLDLN2` | `D9 ED` |   |   |
| Exchange top-of-stack register with other stack register | `FXCH st(i)` | `D9 C8+i` | No | —N/a |
| DD C8+i |   |   |   |   |
| DF C8+i |   |   |   |   |
| x87 Integer Load/Store Instructions | precision control | rounding control |   |   |
| Load signed integer value onto stack from memory, with conversion to floating-point | `FILD m16` | `DF /0` | No | —N/a |
| `FILD m32` | `DB /0` |   |   |   |
| `FILD m64` | `DF /5` |   |   |   |
| Store top-of-stack value to memory, with conversion to signed integer | `FIST m16` | `DF /2` | No | Yes |
| `FIST m32` | `DB /2` |   |   |   |
| Store top-of-stack value to memory, with conversion to signed integer, then pop stack | `FISTP m16` | `DF /3` | No | Yes |
| `FISTP m32` | `DB /3` |   |   |   |
| `FISTP m64` | `DF /7` |   |   |   |
| Load 18-digit Binary-Coded-Decimal integer value onto stack from memory, with conversion to floating-point | `FBLD m80` | `DF /4` | No | —N/a |
| Store top-of-stack value to memory, with conversion to 18-digit Binary-Coded-Decimal integer, then pop stack | `FBSTP m80` | `DF /6` | No | 387 |
| x87 Basic Arithmetic Instructions | precision control | rounding control |   |   |
| Floating-point add `dst <- dst + src` | `FADD m32` | `D8 /0` | Yes | Yes |
| `FADD m64` | `DC /0` |   |   |   |
| `FADD st,st(i)` | `D8 C0+i` |   |   |   |
| `FADD st(i),st` | `DC C0+i` |   |   |   |
| Floating-point multiply `dst <- dst * src` | `FMUL m32` | `D8 /1` | Yes | Yes |
| `FMUL m64` | `DC /1` |   |   |   |
| `FMUL st,st(i)` | `D8 C8+i` |   |   |   |
| `FMUL st(i),st` | `DC C8+i` |   |   |   |
| Floating-point subtract `dst <- dst – src` | `FSUB m32` | `D8 /4` | Yes | Yes |
| `FSUB m64` | `DC /4` |   |   |   |
| `FSUB st,st(i)` | `D8 E0+i` |   |   |   |
| `FSUB st(i),st` | `DC E8+i` |   |   |   |
| Floating-point reverse subtract `dst <- src – dst` | `FSUBR m32` | `D8 /5` | Yes | Yes |
| `FSUBR m64` | `DC /5` |   |   |   |
| `FSUBR st,st(i)` | `D8 E8+i` |   |   |   |
| `FSUBR st(i),st` | `DC E0+i` |   |   |   |
| Floating-point divide `dst <- dst / src` | `FDIV m32` | `D8 /6` | Yes | Yes |
| `FDIV m64` | `DC /6` |   |   |   |
| `FDIV st,st(i)` | `D8 F0+i` |   |   |   |
| `FDIV st(i),st` | `DC F8+i` |   |   |   |
| Floating-point reverse divide `dst <- src / dst` | `FDIVR m32` | `D8 /7` | Yes | Yes |
| `FDIVR m64` | `DC /7` |   |   |   |
| `FDIVR st,st(i)` | `D8 F8+i` |   |   |   |
| `FDIVR st(i),st` | `DC F0+i` |   |   |   |
| Floating-point compare `CC <- result_of( st(0) – src )` Same operation as subtract, except that it updates the x87 CC status register instead of any of the FPU stack registers | `FCOM m32` | `D8 /2` | No | —N/a |
| `FCOM m64` | `DC /2` |   |   |   |
| `FCOM st(i)` | `D8 D0+i` |   |   |   |
| DC D0+i |   |   |   |   |
| x87 Basic Arithmetic Instructions with Stack Pop | precision control | rounding control |   |   |
| Floating-point add and pop | `FADDP st(i),st` | `DE C0+i` | Yes | Yes |
| Floating-point multiply and pop | `FMULP st(i),st` | `DE C8+i` | Yes | Yes |
| Floating-point subtract and pop | `FSUBP st(i),st` | `DE E8+i` | Yes | Yes |
| Floating-point reverse-subtract and pop | `FSUBRP st(i),st` | `DE E0+i` | Yes | Yes |
| Floating-point divide and pop | `FDIVP st(i),st` | `DE F8+i` | Yes | Yes |
| Floating-point reverse-divide and pop | `FDIVRP st(i),st` | `DE F0+i` | Yes | Yes |
| Floating-point compare and pop | `FCOMP m32` | `D8 /3` | No | —N/a |
| `FCOMP m64` | `DC /3` |   |   |   |
| `FCOMP st(i)` | `D8 D8+i` |   |   |   |
| DC D8+i |   |   |   |   |
| DE D0+i |   |   |   |   |
| Floating-point compare to st(1), then pop twice | `FCOMPP` | `DE D9` | No | —N/a |
| x87 Basic Arithmetic Instructions with Integer Source Argument | precision control | rounding control |   |   |
| Floating-point add by integer | `FIADD m16` | `DA /0` | Yes | Yes |
| `FIADD m32` | `DE /0` |   |   |   |
| Floating-point multiply by integer | `FIMUL m16` | `DA /1` | Yes | Yes |
| `FIMUL m32` | `DE /1` |   |   |   |
| Floating-point subtract by integer | `FISUB m16` | `DA /4` | Yes | Yes |
| `FISUB m32` | `DE /4` |   |   |   |
| Floating-point reverse-subtract by integer | `FISUBR m16` | `DA /5` | Yes | Yes |
| `FISUBR m32` | `DE /5` |   |   |   |
| Floating-point divide by integer | `FIDIV m16` | `DA /6` | Yes | Yes |
| `FIDIV m32` | `DE /6` |   |   |   |
| Floating-point reverse-divide by integer | `FIDIVR m16` | `DA /7` | Yes | Yes |
| `FIDIVR m32` | `DE /7` |   |   |   |
| Floating-point compare to integer | `FICOM m16` | `DA /2` | No | —N/a |
| `FICOM m32` | `DE /2` |   |   |   |
| Floating-point compare to integer, and stack pop | `FICOMP m16` | `DA /3` | No | —N/a |
| `FICOMP m32` | `DE /3` |   |   |   |
| x87 Additional Arithmetic Instructions | precision control | rounding control |   |   |
| Floating-point change sign | `FCHS` | `D9 E0` | No | —N/a |
| Floating-point absolute value | `FABS` | `D9 E1` | No | —N/a |
| Floating-point compare top-of-stack value to 0 | `FTST` | `D9 E4` | No | —N/a |
| Classify top-of-stack st(0) register value. The classification result is stored in the x87 CC register. | `FXAM` | `D9 E5` | No | —N/a |
| Split the st(0) value into two values E and M representing the exponent and mantissa of st(0). The split is done such that $M*2^{E}=st(0)$ , where E is an integer and M is a number whose absolute value is within the range $1\leq \left\|M\right\|<2$ .   st(0) is then replaced with E, after which M is pushed onto the stack. | `FXTRACT` | `D9 F4` | No | —N/a |
| Floating-point partial remainder (not IEEE 754 compliant): $Q\leftarrow {\mathtt {IntegerRoundToZero}}\left({\frac {st(0)}{st(1)}}\right)$ $st(0)\leftarrow st(0)-st(1)*Q$ | `FPREM` | `D9 F8` | No | —N/a |
| Floating-point square root | `FSQRT` | `D9 FA` | Yes | Yes |
| Floating-point round to integer | `FRNDINT` | `D9 FC` | No | Yes |
| Floating-point power-of-2 scaling. Rounds the value of st(1) to integer with round-to-zero, then uses it as a scale factor for st(0): $st(0)\leftarrow st(0)*2^{{\mathtt {IntegerRoundToZero}}\left(st(1)\right)}$ | `FSCALE` | `D9 FD` | No | Yes |
|   |   |   |   |   |
| x87 Transcendental Instructions | Source operand range restriction |   |   |   |
| Base-2 exponential minus 1, with extra precision for st(0) close to 0: $st(0)\leftarrow 2^{st(0)}-1$ | `F2XM1` | `D9 F0` | 8087:  $0\leq st(0)\leq {\frac {1}{2}}$ 80387:  $-1\leq st(0)\leq 1$ |   |
| Base-2 Logarithm and multiply: $st(1)\leftarrow st(1)*\log _{2}\left(st(0)\right)$ followed by stack pop | `FYL2X` | `D9 F1` | no restrictions |   |
| Partial Tangent: Computes from st(0) a pair of values X and Y, such that $\tan \left(st(0)\right)={\frac {Y}{X}}$ The Y value replaces the top-of-stack value, and then X is pushed onto the stack. On 80387 and later x87, but not original 8087, X is always 1.0 | `FPTAN` | `D9 F2` | 8087:  $0\leq \left\|st(0)\right\|\leq {\frac {\pi }{4}}$ 80387:  $0\leq \left\|st(0)\right\|<2^{63}$ |   |
| Two-argument arctangent with quadrant adjustment: $st(1)\leftarrow \arctan \left({\frac {st(1)}{st(0)}}\right)$ followed by stack pop | `FPATAN` | `D9 F3` | 8087:  $\left\|st(1)\right\|\leq \left\|st(0)\right\|<\infty$ 80387: no restrictions |   |
| Base-2 Logarithm plus 1 with extra precision for st(0) close to 0, followed by multiply: $st(1)\leftarrow st(1)*\log _{2}\left(st(0)+1\right)$ followed by stack pop | `FYL2XP1` | `D9 F9` | Intel:  $\left\|st(0)\right\|<\left(1-{\sqrt {\frac {1}{2}}}\right)$ AMD:  $\left({\sqrt {\frac {1}{2}}}-1\right)<st(0)<\left({\sqrt {2}}-1\right)$ |   |
|   |   |   |   |   |
| Other x87 Instructions |   |   |   |   |
| No operation | `FNOP` | `D9 D0` |   |   |
| Decrement x87 FPU Register Stack Pointer | `FDECSTP` | `D9 F6` |   |   |
| Increment x87 FPU Register Stack Pointer | `FINCSTP` | `D9 F7` |   |   |
| Free x87 FPU Register | `FFREE st(i)` | `DD C0+i` |   |   |
| Check and handle pending unmasked x87 FPU exceptions | `WAIT`, `FWAIT` | `9B` |   |   |
| Floating-point store and pop, without stack underflow exception | FSTPNCE st(i) | D9 D8+i |   |   |
| Free x87 register, then stack pop | FFREEP st(i) | DF C0+i |   |   |

1. x87 coprocessors (other than the 8087) handle exceptions in a fairly unusual way. When an x87 instruction generates an unmasked arithmetic exception, it will still complete without causing a CPU fault – instead of causing a fault, it will record within the coprocessor information needed to handle the exception (instruction pointer, opcode, data pointer if the instruction had a memory operand) and set FPU status-word flag to indicate that a pending exception is present. This pending exception will then cause a CPU fault when the next x87, MMX or `WAIT` instruction is executed. The exception to this is x87's "Non-Waiting" instructions, which will execute without causing such a fault even if a pending exception is present (with some caveats, see application note AP-578). These instructions are mostly control instructions that can inspect and/or modify the pending-exception state of the x87 FPU.
2. For each non-waiting x87 instruction whose mnemonic begins with `FN`, there exists a pseudo-instruction that has the same mnemonic except without the N. These pseudo-instructions consist of a `WAIT` instruction (opcode `9B`) followed by the corresponding non-waiting x87 instruction. For example:`FNCLEX` is an instruction with the opcode `DB E2`. The corresponding pseudo-instruction `FCLEX` is then encoded as `**9B** DB E2`.`FNSAVE ES:[BX+6]` is an instruction with the opcode `26 DD 77 06`. The corresponding pseudo-instruction `FSAVE ES:[BX+6]` is then encoded as `**9B** 26 DD 77 06`These pseudo-instructions are commonly recognized by x86 assemblers and disassemblers and treated as single instructions, even though all x86 CPUs with x87 coprocessors execute them as a sequence of two instructions.
3. The FPU initialization performed by the `F(N)INIT` and `F(N)SAVE` instructions will set x87 FPU registers as follows: The FPU Control Word id set to `0x03FF` on the 8087, or `0x037F` on 80287 and later FPUs (64-bit precision, round-to-nearest, all exceptions masked, interrupts enabled for the 8087) The FPU Status Word is set to all-0s (except that on 8087/80287 FPUs, the CC bits may be left unmodified) The FPU Tag Word is set to `0xFFFF` (marking all registers as Empty) On i486 and later processors, the FPU exception pointer registers (FCS,FIP,FDS,FDP,FOP) are set to 0. The data registers are marked as Empty but not otherwise modified.
4. On 80387 and earlier FPUs, if an `FNINIT` instruction is issued before a previous memory-referencing x87 instruction has completed, then any memory bus cycles associated with that previous x87 instruction may be aborted.
5. For detection of x87 coprocessors on systems that don't support `CPUID`, it is common to issue an `FNINIT` followed by an `FNSTCW` or `FNSTSW` and then check that the `FNSTCW`/`FNSTSW` wrote the expected value to memory. On the 8087, such a detection procedure requires at least two intervening integer instructions between the `FNINIT` and the following `FNSTCW`/`FNSTSW` to work correctly.
6. `F(N)STSW` with the AX register as a destination is available on 80287 and later, but not on the 8087.
7. On 80387 and later x87 FPUs, `FLDENV`, `F(N)STENV`, `FRSTOR` and `F(N)SAVE` exist in 16-bit and 32-bit variants. The 16-bit variants will load/store a 14-byte floating-point environment data structure to/from memory – the 32-bit variants will load/store a 28-byte data structure instead. (`F(N)SAVE`/`FRSTOR` will additionally load/store an additional 80 bytes of FPU data register content after the FPU environment, for a total of 94 or 108 bytes). The choice between the 16-bit and 32-bit variants is based on the `CS.D` bit and the presence of the `66h` instruction prefix. On 8087 and 80287, only the 16-bit variants are available. 64-bit variants of these instructions do not exist – using `REX.W` under x86-64 will cause the 32-bit variants to be used. Since these can only load/store the bottom 32 bits of FIP and FDP, it is recommended to use `FXSAVE64`/`FXRSTOR64` instead if 64-bit operation is desired.
8. In the case of an x87 instruction producing an unmasked FPU exception, the 8087 FPU will signal an IRQ some indeterminate time after the instruction was issued. This may not always be possible to handle, and so the FPU offers the `F(N)DISI` and `F(N)ENI` instructions to set/clear the Interrupt Mask bit (bit 7) of the x87 Control Word, to control the interrupt. Later x87 FPUs, from 80287 onwards, changed the FPU exception mechanism to instead produce a CPU exception on the next x87 instruction. This made the Interrupt Mask bit unnecessary, so it was removed. In later Intel x87 FPUs, the `F(N)ENI` and `F(N)DISI` instructions were kept for backwards compatibility, executing as NOPs that do not modify any x87 state.
9. `FST`/`FSTP` with an 80-bit destination (m80 or st(i)) and an sNaN source value is documented to produce exceptions on AMD but not Intel FPUs.
10. `FSTP ST(0)` is a commonly used idiom for popping a single register off the x87 register stack.
11. Intel x87 alias opcode. Use of this opcode is not recommended. On the Intel 8087 coprocessor, several reserved opcodes would perform operations behaving similarly to existing defined x87 instructions. These opcodes were documented for the 8087 and 80287, but then omitted from later manuals until the October 2017 update of the Intel SDM. They are present on all known Intel x87 FPUs but unavailable on some older non-Intel FPUs, such as AMD Geode GX/LX, DM&P Vortex86 and NexGen 586PF.
12. On the 8087 and 80287, `FBSTP` and the load-constant instructions always use the round-to-nearest rounding mode. On the 80387 and later x87 FPUs, these instructions will use the rounding mode specified in the x87 RC register.
13. For the `FADDP`, `FSUBP`, `FSUBRP`, `FMULP`, `FDIVP`, `FDIVRP`, `FCOM`, `FCOMP` and `FXCH` instructions, x86 assemblers/disassemblers may recognize variants of the instructions with no arguments. Such variants are equivalent to variants using st(1) as their first argument.
14. On Intel Pentium and later processors, `FXCH` is implemented as a register renaming rather than a true data move. This has no semantic effect, but enables zero-cycle-latency operation. It also allows the instruction to break data dependencies for the x87 top-of-stack value, improving attainable performance for code optimized for these processors.
15. On Intel Pentium processors without MMX, the fastest way to copy data from system memory to uncached memory (such as video memory) was to use the m64 forms of `FILD` and `FISTP` in a loop. This method has been used in some MS-DOS games such as Carmageddon and Pete Sampras Tennis '97.A recurring problem in x86 emulators that emulate the x87 FPU registers with a data-format that has less than 64 bits of mantissa precision (e.g. FP64 numbers, which have only 53 mantissa bits) is that when such `FILD`/`FISTP` loops are mapped to int64↔FP64 conversions, some low-order data bits of each 64-bit data item will be lost. In the case of e.g. framebuffer data, such data loss will show up as vertical stripes every 8 pixels.
16. For the `FIST` and `FISTP` instructions, if the top-of-stack value, after being rounded to integer, is too small or too large to be represented in the destination memory format, then the value stored to memory will *not* be clamped - instead, the x87 "Integer Indefinite" value will be stored. This is a value that has the top bit set to 1 and all other bits set to 0. (e.g. `0x8000` for 16-bit integers.) The Integer Indefinite value will also be used if the top-of-stack value is Empty, NaN or ±∞.
17. The result of executing the `FBLD` instruction on non-BCD data is undefined.
18. For the `FBSTP` instruction, if the top-of-stack value is NaN or has a value that $10^{18}$ or greater after rounding, the x87 "BCD Indefinite" value will be stored. On 486 and later, this is `0xFFFFC000000000000000`, while earlier x87 FPUs used `0xFFFF8000000000000000`.
19. On early Intel Pentium processors, floating-point divide was subject to the Pentium FDIV bug. This also affected instructions that perform divide as part of their operations, such as `FPREM`, `FPTAN` and `FPATAN`.
20. The `FXAM` instruction will set C0, C2 and C3 based on value type in st(0) as follows: C3C2C0Classification 000Unsupported (unnormal or pseudo-NaN) 001NaN 010Normal finite number 011Infinity 100Zero 101Empty 110Denormal number 111Empty (may occur on 8087/80287 only) C1 is set to the sign-bit of st(0), regardless of whether st(0) is Empty or not.
21. For `FXTRACT`, the behavior that results from st(0) being zero or ±∞, differs between 8087 and 80387: If st(0) is ±0, then on 8087/80287, E and M are both set equal to st(0) with no exception reported — on 80387 and later, M is set equal to st(0), E is set to -∞, and a zero-divide exception is raised. If st(0) is ±∞, then on 8087/80287, an invalid-operation exception is raised and both M and E are set to NaN — on 80387 and later, M is set equal to st(0) and E is set to +∞ with no exception reported.
22. For `FPREM`, if the quotient Q is larger than $2^{63}$ , then the remainder calculation may have been done only partially – in this case, the `FPREM` instruction will need to be run again in order to complete the remainder calculation. This is indicated by the instruction setting `C2` to 1. If the instruction did complete the remainder calculation, it will set `C2` to 0 and set the three bits `{C0,C3,C1}` to the bottom three bits of the quotient Q. On 80387 and later, if the instruction didn't complete the remainder calculation, then the computed remainder Q used for argument reduction will have been rounded to a multiple of 8 (or larger power-of-2), so that the bottom 3 bits of the quotient can still be correctly retrieved in a later pass that does complete the remainder calculation.
23. The remainder computation done by the `FPREM` instruction is always exact with no roundoff errors.
24. For the `FSCALE` instruction on 8087 and 80287, st(1) is required to be in the range $-2^{15}\leq st(1)<2^{15}$ . Also, its absolute value must be either 0 or at least 1. If these requirements are not satisfied, the result is undefined. These restrictions were removed in the 80387.
25. For `FSCALE`, rounding is only applied in the case of overflow, underflow or subnormal result.
26. The x87 transcendental instructions do not obey PC or RC, but instead compute full 80-bit results. These results are not necessarily correctly rounded (see Table-maker's dilemma) – they may have an error of up to ±1 ulp on Pentium or later, or up to ±1.5 ulps on earlier x87 coprocessors.
27. For the `FYL2X` and `FYL2XP1` instructions, the maximum error bound of ±1 ulp only holds for st(1)=1.0 – for other values of st(1), the error bound is increased to ±1.35 ulps. `FYL2X` can produce a #Z (divide-by-zero exception) if st(0)=0 and st(1) is a finite nonzero value. `FYL2XP1`, however, cannot produce #Z.
28. For `FPATAN`, the following adjustments are done as compared to just computing a one-argument arctangent of the ratio ${\frac {st(1)}{st(0)}}$ :If both st(0) and st(1) are ±∞, then the arctangent is computed as if each of st(0) and st(1) had been replaced with ±1 of the same sign. This produces a result that is an odd multiple of ${\frac {\pi }{4}}$ .If both st(0) and st(1) are ±0, then the arctangent is computed as if st(0) but not st(1) had been replaced with ±1 of the same sign, producing a result of ±0 or $\pm \pi$ .If st(0) is negative (has sign bit set), then an addend of $\pm \pi$ with the same sign as st(1) is added to the result.
29. While `FNOP` is a no-op in the sense that will leave the x87 FPU register stack unmodified, it may still modify FIP and CC, and it may fault if a pending x87 FPU exception is present.
30. On the 8087 FPU (but not any later x87 FPU), the `WAIT` instruction was needed before every x87 instruction (except the "non-waiting" instructions) to help ensure that a new x87 instruction was not issued to the FPU before the preceding instruction had completed.On some early x87 coprocessors — in particular the 8087 FPU, as well as the 80287 FPU when used in a 80286 system — the `WAIT` instruction was also required to be used before a CPU instruction that attempts to access a memory location that's previously been used as an operand to an x87 data instruction.On 386 and 486 systems with x87 FPUs, this requirement was removed for most x87 instructions that accessed memory, but continued to exist for the `F(N)SAVE` instruction. On Pentium and later processors, this requirement was removed for `F(N)SAVE` as well.
31. If the top-of-stack register st(0) is Empty, then the `FSTPNCE` instruction will behave like `FINCSTP`, incrementing the stack pointer with no data movement and no exceptions reported.

### x87 instructions added in later processors

| Instruction description | Mnemonic | Opcode | Additional items |
|---|---|---|---|
|   |   |   |   |
| x87 Non-Waiting Control Instructions added in 80287 | Waiting mnemonic |   |   |
| Notify FPU of entry into Protected Mode | `FNSETPM` | `DB E4` | `FSETPM` |
| Store x87 Status Word to AX | `FNSTSW AX` | `DF E0` | `FSTSW AX` |
|   |   |   |   |
| x87 Instructions added in 80387 | Source operand range restriction |   |   |
| Floating-point unordered compare. Similar to the regular floating-point compare instruction `FCOM`, except will not produce an exception in response to any qNaN operands. | `FUCOM st(i)` | `DD E0+i` | no restrictions |
| Floating-point unordered compare and pop | `FUCOMP st(i)` | `DD E8+i` |   |
| Floating-point unordered compare to st(1), then pop twice | `FUCOMPP` | `DA E9` |   |
| IEEE 754 compliant floating-point partial remainder. | `FPREM1` | `D9 F5` |   |
| Floating-point sine and cosine. Computes two values $S=\sin \left(k*st(0)\right)$ and $C=\cos \left(k*st(0)\right)$   Top-of-stack st(0) is replaced with S, after which C is pushed onto the stack. | `FSINCOS` | `D9 FB` | $\left\|st(0)\right\|<2^{63}$ |
| Floating-point sine. $st(0)\leftarrow \sin \left(k*st(0)\right)$ | `FSIN` | `D9 FE` |   |
| Floating-point cosine. $st(0)\leftarrow \cos \left(k*st(0)\right)$ | `FCOS` | `D9 FF` |   |
|   |   |   |   |
| x87 Instructions added in Pentium Pro | Condition for conditional moves |   |   |
| Floating-point conditional move to st(0) based on EFLAGS | `FCMOVB st(0),st(i)` | `DA C0+i` | below (CF=1) |
| `FCMOVE st(0),st(i)` | `DA C8+i` | equal (ZF=1) |   |
| `FCMOVBE st(0),st(i)` | `DA D0+i` | below or equal (CF=1 or ZF=1) |   |
| `FCMOVU st(0),st(i)` | `DA D8+i` | unordered (PF=1) |   |
| `FCMOVNB st(0),st(i)` | `DB C0+i` | not below (CF=0) |   |
| `FCMOVNE st(0),st(i)` | `DB C8+i` | not equal (ZF=0) |   |
| `FCMOVNBE st(0),st(i)` | `DB D0+i` | not below or equal (CF=0 and ZF=0) |   |
| `FCMOVNU st(0),st(i)` | `DB D8+i` | not unordered (PF=0) |   |
| Floating-point compare and set `EFLAGS`. Differs from the older `FCOM` floating-point compare instruction in that it puts its result in the integer `EFLAGS` register rather than the x87 CC register. | `FCOMI st(0),st(i)` | `DB F0+i` |   |
| Floating-point compare and set `EFLAGS`, then pop | `FCOMIP st(0),st(i)` | `DF F0+i` |   |
| Floating-point unordered compare and set `EFLAGS` | `FUCOMI st(0),st(i)` | `DB E8+i` |   |
| Floating-point unordered compare and set `EFLAGS`, then pop | `FUCOMIP st(0),st(i)` | `DF E8+i` |   |
|   |   |   |   |
| x87 Non-Waiting Instructions added in Pentium II, AMD K7 and SSE | 64-bit mnemonic (`REX.W` prefix) |   |   |
| Save x87, MMX and SSE state to a 464-byte data structure | `FXSAVE m464byte` | `NP 0F AE /0` | `FXSAVE64 m464byte` |
| Restore x87, MMX and SSE state from 464-byte data structure | `FXRSTOR m464byte` | `NP 0F AE /1` | `FXRSTOR64 m464byte` |
|   |   |   |   |
| x87 Instructions added as part of SSE3 |   |   |   |
| Floating-point store integer and pop, with round-to-zero | `FISTTP m16` | `DF /1` |   |
| `FISTTP m32` | `DB /1` |   |   |
| `FISTTP m64` | `DD /1` |   |   |

1. The x87 FPU needs to know whether it is operating in Real Mode or Protected Mode because the floating-point environment accessed by the `F(N)SAVE`, `FRSTOR`, `FLDENV` and `F(N)STENV` instructions has different formats in Real Mode and Protected Mode. On 80287, the `F(N)SETPM` instruction is required to communicate the real-to-protected mode transition to the FPU. On 80387 and later x87 FPUs, real↔protected mode transitions are handled automatically between the CPU and the FPU without the need for any dedicated instructions – therefore, on these FPUs, `FNSETPM` executes as a NOP that does not modify any FPU state.On the 80287, once the FPU has been brought into Protected Mode operation with the `F(N)SETPM` instruction, it cannot be brought back to Real Mode operation without an FPU reset — on IBM-compatible PCs with 80287/80387 FPUs (but not 80486 and later), such an FPU reset could be performed by writing a byte with the value 0 to I/O port `F1h`.
2. Not including discontinued instructions specific to particular 80387-compatible FPU models.
3. For the `FUCOM` and `FUCOMP` instructions, x86 assemblers/disassemblers may recognize variants of the instructions with no arguments. Such variants are equivalent to variants using st(1) as their first argument.
4. The 80387 `FPREM1` instruction differs from the older `FPREM` (`D9 F8`) instruction in that the quotient Q is rounded to integer with round-to-nearest-even rounding rather than the round-to-zero rounding used by `FPREM`. Like `FPREM`, `FPREM1` always computes an exact result with no roundoff errors. Like `FPREM`, it may also perform a partial computation if the quotient is too large, in which case it must be run again.
5. Due to the x87 FPU performing argument reduction for sin/cos with only about 68 bits of precision, the value of k used in the calculation of `FSIN`, `FCOS` and `FSINCOS` is not precisely 1.0, but instead given by $k{=}{\frac {2^{66}*\pi }{\lfloor 2^{66}*\pi \rfloor }}\approx 1.0000000000000000000012874$ This argument reduction inaccuracy also affects the `FPTAN` instruction.Examples of numbers that produce large relative differences between the `FSIN` instruction and the mathematical sine function include: For $x=2646693125139304345$ , `FSIN` will produce a result of approximately $-0.003407$ while the true value of $\sin \left(x\right)$ is approximately $1.188*10^{-20}$ . For $x=1838419787915897336$ , `FSIN` will produce a result of approximately $1.084*10^{-19}$ while the true value of $\sin \left(x\right)$ is approximately $0.002366$ .
6. If st(0) is finite and its absolute value is $2^{63}$ or greater, then the top-of-stack value st(0) is left unmodified and C2 is set, with no exception raised. This applies to the `FSIN`, `FCOS` and `FSINCOS` instructions, as well as `FPTAN` on 80387 and later. In this case, the `FSINCOS` and `FPTAN` instructions will also abstain from pushing a value onto the x87 register-stack.
7. The `FCOMI`, `FCOMIP`, `FUCOMI` and `FUCOMIP` instructions write their results to the `ZF`, `CF` and `PF` bits of the `EFLAGS` register. On Intel but not AMD processors, the `SF`, `AF` and `OF` bits of `EFLAGS` are also zeroed out by these instructions.
8. The `FXSAVE` and `FXRSTOR` instructions were added in the "Deschutes" revision of Pentium II, and are not present in earlier "Klamath" revision. They are also present in AMD K7. They are also considered an integral part of SSE and are therefore present in all processors with SSE.
9. The `FXSAVE` and `FXRSTOR` instructions will save/restore SSE state only on processors that support SSE. Otherwise, they will only save/restore x87 and MMX state. The x87 section of the state saved/restored by `FXSAVE(64)`/`FXRSTOR(64)` has a completely different layout than the data structure of the older `F(N)SAVE`/`FRSTOR` instructions, enabling faster save/restore by avoiding misaligned loads and stores. `FXSAVE` and `FXRSTOR` require their memory argument to be 16-byte aligned.
10. When floating-point emulation is enabled with `CR0.EM=1`, `FXSAVE(64)` and `FXRSTOR(64)` are considered to be x87 instructions and will accordingly produce an #NM (device-not-available) exception. Other than `WAIT`, these are the only opcodes outside the `D8..DF` ESC opcode space that exhibit this behavior. Except on Netburst (Pentium 4 family) CPUs, all opcodes in `D8..DF` will produce #NM if `CR0.EM=1`, even for undefined opcodes that would produce #UD otherwise.
11. Unlike the older `F(N)SAVE` instruction, `FXSAVE` will not initialize the FPU after saving its state to memory, but instead leave the x87 coprocessor state unmodified.
12. The `FXSAVE64`/`FXRSTOR64` instruction differ from the `FXSAVE`/`FXRSTOR` instructions in that: `FXSAVE`/`FXRSTOR` will save/restore FIP and FDP as 32-bit items, and will also save/restore FCS and FDS as 16-bit items. `FXSAVE64`/`FXRSTOR64` will save/restore FIP and FDP as 64-bit items while not saving/restoring FCS and FDS. This difference also applies to the later `XSAVE`/`XRSTOR` vs `XSAVE64`/`XRSTOR64` instructions. As a result, saving both FCS/FDS and the top 32 bits of 64-bit FIP/FDP cannot be accomplished with 1 instruction, but instead requires running both `(F)XSAVE` and `(F)XSAVE64`. This has been known to cause problems, especially for 64-bit hypervisors running 16/32-bit guests.
13. The `FISTTP` instruction will, like the older `FIST` and `FISTP` instructions, store the x87 "Integer Indefinite" value if the top-of-stack value is too small/large to be represented in the memory destination format.


## SIMD instructions


## Cryptographic instructions


## Virtualization instructions


## Other instructions

x86 also includes discontinued instruction sets which are no longer supported by Intel and AMD, and undocumented instructions which execute but are not officially documented.

### Undocumented x86 instructions

The x86 CPUs contain undocumented instructions which are implemented on the chips but not listed in some official documents. They can be found in various sources across the Internet, such as Ralf Brown's Interrupt List and at sandpile.org

Some of these instructions are widely available across many/most x86 CPUs, while others are specific to a narrow range of CPUs.

#### Undocumented instructions that are widely available across many x86 CPUs include

| Mnemonics | Opcodes | Description | Status |
|---|---|---|---|
| `AAM imm8` | `D4 *ib*` | ASCII-Adjust-after-Multiply. On the 8086, documented for imm8=0Ah only, which is used to convert a binary multiplication result to BCD. The actual operation is `AH ← AL/imm8; AL ← AL mod imm8` for any imm8 value (except zero, which produces a divide-by-zero exception). | Available beginning with 8086, documented for imm8 values other than `0Ah` since Pentium (earlier documentation lists no arguments). |
| `AAD imm8` | `D5 *ib*` | ASCII-Adjust-Before-Division. On the 8086, documented for imm8=0Ah only, which is used to convert a BCD value to binary for a following division instruction. The actual operation is `AL ← (AL+(AH*imm8)) & 0FFh; AH ← 0` for any imm8 value. |   |
| `SALC`, `SETALC` | `D6` | Set AL depending on the value of the Carry Flag (a 1-byte alternative of `SBB AL, AL`) | Available beginning with 8086, but only documented since Pentium Pro. |
| `ICEBP`, `INT1` | `F1` | Single byte single-step exception / Invoke ICE | Available beginning with 80386, documented (as `INT1`) since Pentium Pro. Executes as undocumented instruction prefix on 8086 and 80286. |
|   |   |   |   |
| `TEST r/m8,imm8` | `F6 /1 *ib*` | Undocumented variants of the `TEST` instruction. Performs the same operation as the documented `F6 /0` and `F7 /0` variants, respectively. | Available since the 8086. Unavailable on some 80486 steppings. |
| `TEST r/m16,imm16`, `TEST r/m32,imm32` | `F7 /1 *iw*`, `F7 /1 *id*` |   |   |
| `SHL`, `SAL` | `(D0..D3) /6`, `(C0..C1) /6 *ib*` | Undocumented variants of the `SHL` instruction. Performs the same operation as the documented `(D0..D3) /4` and `(C0..C1) /4 *ib*` variants, respectively. | Available since the 80186 (performs different operation on the 8086) |
| (multiple) | `82 /(0..7) *ib*` | Alias of opcode `80h`, which provides variants of 8-bit integer instructions (`ADD`, `OR`, `ADC`, `SBB`, `AND`, `SUB`, `XOR`, `CMP`) with an 8-bit immediate argument. | Available since the 8086. Explicitly unavailable in 64-bit mode but kept and reserved for compatibility. |
| `OR/AND/XOR r/m16,imm8` | `83 /(1,4,6) *ib*` | 16-bit `OR`/`AND`/`XOR` with a sign-extended 8-bit immediate. | Available on 8086, but only documented from 80386 onwards. |
|   |   |   |   |
| `REPNZ MOVS` | `F2 (A4..A5)` | The behavior of the `F2` prefix (`REPNZ`, `REPNE`) when used with string instructions other than `CMPS`/`SCAS` is officially undefined, but there exists commercial software (e.g. the version of FDISK distributed with MS-DOS versions 3.30 to 6.22) that rely on it to behave in the same way as the documented `F3` (`REP`) prefix. | Available since the 8086. |
| `REPNZ STOS` | `F2 (AA..AB)` |   |   |
| `REP RET` | `F3 C3` | The use of the `REP` prefix with the `RET` instruction is not listed as supported in either the Intel SDM or the AMD APM. However, AMD's optimization guide for the AMD-K8 describes the `F3 C3` encoding as a way to encode a two-byte `RET` instruction – this is the recommended workaround for an issue in the AMD-K8's branch predictor that can cause branch prediction to fail for some 1-byte `RET` instructions. At least some versions of gcc are known to use this encoding. | Executes as `RET` on all known x86 CPUs. |
| `NOP` | `67 90` | `NOP` with address-size override prefix. The use of the `67h` prefix for instructions without memory operands is listed by the Intel SDM (vol 2, section 2.1.1) as "reserved", but it is used in Microsoft Windows 95 as a workaround for a bug in the B1 stepping of Intel 80386. | Executes as `NOP` on 80386 and later. |
|   |   |   |   |
| `NOP r/m` | `0F 1F /0` | Official long NOP. Introduced in the Pentium Pro in 1995, but remained undocumented until March 2006. | Available on Pentium Pro and AMD K7 and later. Unavailable on AMD K6, AMD Geode LX, VIA Nehemiah. |
| `NOP r/m` | `0F 0D /r` | Reserved-NOP. Introduced in 65 nm Pentium 4. Intel documentation lists this opcode as `NOP` in opcode tables but not instruction listings since June 2005. From Broadwell onwards, `0F 0D /1` has been documented as `PREFETCHW`, while `0F 0D /0` and `/2../7` have been reported to exhibit undocumented prefetch functionality. On AMD CPUs, `0F 0D /r` with a memory argument is documented as `PREFETCH`/`PREFETCHW` since K6-2 – originally as part of 3Dnow!, but has been kept in later AMD CPUs even after the rest of 3Dnow! was dropped. | Available on Intel CPUs since 65 nm Pentium 4. |
| `UD1` | `0F B9 /r` | Intentionally undefined instructions, but unlike `UD2` (`0F 0B`) these instructions were left unpublished until December 2016. Microsoft Windows 95 Setup is known to depend on `0F FF` being invalid – it is used as a self check to test that its #UD exception handler is working properly. Other invalid opcodes that are being relied on by commercial software to produce #UD exceptions include `FF FF` (DIF-2, LaserLok) and `C4 C4` (`"BOP"`), however as of January 2022 they are not published as intentionally invalid opcodes. | All of these opcodes produce #UD exceptions on 80186 and later (except on NEC V20/V30, which assign at least `0F FF` to the NEC-specific `BRKEM` instruction.) |
| `UD0` | `0F FF` |   |   |

#### Undocumented instructions that appear only in a limited subset of x86 CPUs include

| Mnemonics | Opcodes | Description | Status |
|---|---|---|---|
| `REP MUL` | `F3 F6 /4`, `F3 F7 /4` | On 8086/8088, a `REP` or `REPNZ` prefix on a `MUL` or `IMUL` instruction causes the result to be negated. This is due to the microcode using the “REP prefix present” bit to store the sign of the result. | 8086/8088 only. |
| `REP IMUL` | `F3 F6 /5`, `F3 F7 /5` |   |   |
| `REP IDIV` | `F3 F6 /7`, `F3 F7 /7` | On 8086/8088, a `REP` or `REPNZ` prefix on an `IDIV` (but not `DIV`) instruction causes the quotient to be negated. This is due to the microcode using the “REP prefix present” bit to store the sign of the quotient. | 8086/8088 only. |
| `SAVEALL`, `STOREALL` | `(F1) 0F 04` | Exact purpose unknown, causes CPU hang (HCF). The only way out is CPU reset. In some implementations, emulated through BIOS as a halting sequence. In a forum post at the Vintage Computing Federation, this instruction (with `F1` prefix) is explained as `SAVEALL`. It interacts with ICE mode. | Only available on 80286. |
| `LOADALL` | `0F 05` | Loads All Registers from Memory Address 0x000800H | Only available on 80286. Opcode reused for `SYSCALL` in AMD K6 and later CPUs. |
| `LOADALLD` | `0F 07` | Loads All Registers from Memory Address ES:EDI | Only available on 80386. Opcode reused for `SYSRET` in AMD K6 and later CPUs. |
| `CL1INVMB` | `0F 0A` | On the Intel SCC (Single-chip Cloud Computer), invalidate all message buffers. The mnemonic and operation of the instruction, but not its opcode, are described in Intel's SCC architecture specification. | Available on the SCC only. |
| `PATCH2` | `0F 0E` | On AMD K6 and later maps to `FEMMS` operation (fast clear of MMX state) but on Intel identified as uarch data read on Intel | Only available in Red unlock state (`0F 0F` too) |
| `PATCH3` | `0F 0F` | Write uarch | Can change RAM part of microcode on Intel |
| `UMOV r,r/m`, `UMOV r/m,r` | `0F (10..13) /r` | Moves data to/from user memory when operating in ICE HALT mode. Acts as regular `MOV` otherwise. | Available on some 386 and 486 processors only. Opcodes reused for SSE instructions in later CPUs. |
| `NXOP` | `0F 55` | NexGen hypercode interface. | Available on NexGen Nx586 only. |
| (multiple) | `0F (E0..FB)` | NexGen Nx586 "hyper mode" instructions. The NexGen Nx586 CPU uses "hyper code" (x86 code sequences unpacked at boot time and only accessible in a special "hyper mode" operation mode, similar to DEC Alpha's PALcode and Intel's XuCode) for many complicated operations that are implemented with microcode in most other x86 CPUs. The Nx586 provides a large number of undocumented instructions to assist hyper mode operation. | Available in Nx586 hyper mode only. |
| `PSWAPW mm,mm/m64` | `0F 0F /r BB` | Undocumented AMD 3DNow! instruction on K6-2 and K6-3. Swaps 16-bit words within 64-bit MMX register. Instruction known to be recognized by MASM 6.13 and 6.14. | Available on K6-2 and K6-3 only. Opcode reused for documented `PSWAPD` instruction from AMD K7 onwards. |
| Unknown mnemonic | `64 D6` | Using the `64` (FS: segment) prefix with the undocumented `D6` (`SALC`/`SETALC`) instruction will, on UMC CPUs only, cause EAX to be set to `0xAB6B1B07`. | Available on the UMC Green CPU only. Executes as `SALC` on non-UMC CPUs. |
| `FS: Jcc` | `64 (70..7F) rel8`, `64 0F (80..8F) rel16/32` | On Intel NetBurst (Pentium 4) CPUs, the 64h (FS: segment) instruction prefix will, when used with conditional branch instructions, act as a branch hint to indicate that the branch will be alternating between taken and not-taken. Unlike other NetBurst branch hints (CS: and DS: segment prefixes), this hint is not documented. | Available on NetBurst CPUs only. Segment prefixes on conditional branches are accepted but ignored by non-NetBurst CPUs. |
| `JMPAI` | `0F 3F` | Jump and execute instructions in the undocumented Alternate Instruction Set. | Only available on some x86 processors made by VIA Technologies. |
| (FMA4) | `VEX.66.0F38 (5C..5F,68..6F,78..7F) /r imm8` | On AMD Zen1, FMA4 instructions are present but undocumented (missing CPUID flag). The reason for leaving the feature undocumented may or may not have been due to a buggy implementation. | Removed from Zen2 onwards. |
| (unknown, multiple) | `0F 0F /r ??` | The whitepapers for SandSifter and UISFuzz report the detection of large numbers of undocumented instructions in the 3DNow! opcode range on several different AMD CPUs (at least Geode NX and C-50). Their operation is not known. On at least AMD K6-2, all of the unassigned 3DNow! opcodes (other than the undocumented `PF2IW`, `PI2FW` and `PSWAPW` instructions) are reported to execute as equivalents of `POR` (MMX bitwise-OR instruction). | Present on some AMD CPUs with 3DNow!. |
| `MOVDB`, `GP2MEM` | Unknown | Microprocessor Report's article "MediaGX Targets Low-Cost PCs" from 1997, covering the introduction of the Cyrix MediaGX processor, lists several new instructions that are said to have been added to this processor in order to support its new "Virtual System Architecture" features, including `MOVDB` and `GP2MEM` – and also mentions that Cyrix did not intend to publish specifications for these instructions. | Unknown. No specification known to have been published. |
|   |   |   |   |
| `REP XSHA512` | `F3 0F A6 E0` | Perform SHA-512 hashing. Supported by OpenSSL as part of its VIA PadLock support, and listed in a Zhaoxin-supplied Linux kernel patch, but not documented by the VIA PadLock Programming Guide. | Only available on some x86 processors made by VIA Technologies and Zhaoxin. |
| `REP XMODEXP` | `F3 0F A6 F8` | Instructions to perform modular exponentiation and random number generation, respectively. Listed in a VIA-supplied patch to add support for VIA Nano-specific PadLock instructions to OpenSSL, but not documented by the VIA PadLock Programming Guide. |   |
| `XRNG2` | `F3 0F A7 F8` |   |   |
| Unknown mnemonic | `0F A7 (C1..C7)` | Detected by CPU fuzzing tools such as SandSifter and UISFuzz as executing without causing #UD on several different VIA and Zhaoxin CPUs. Unknown operation, may be related to the documented `XSTORE` (`0F A7 C0`) instruction. |   |
| Unknown mnemonic | `F2 0F A6 C0` | Zhaoxin SM2 instruction. CPUID flags listed in a Linux kernel patch for OpenEuler, description and opcode (but no instruction mnemonic) provided in a Zhaoxin patent application and a Zhaoxin-provided Linux kernel patch. | Present in Zhaoxin KX-6000G. |
| `ZXPAUSE` | `F2 0F A6 D0` | Pause the processor until the Time Stamp Counter reaches or exceeds the value specified in EDX:EAX. Low-power processor C-state can be requested in ECX. Listed in OpenEuler kernel patch. | Present in Zhaoxin KX-7000. |
| `MONTMUL2` | Unknown | Zhaoxin RSA/"xmodx" instructions. Mnemonics and CPUID flags are listed in a Linux kernel patch for OpenEuler, but opcodes and instruction descriptions are not available. | Unknown. Some Zhaoxin CPUs have the CPUID flags for these instructions set. |

### Undocumented x87 instructions

| Mnemonics | Opcodes | Description | Status |
|---|---|---|---|
| `FENI`, `FENI8087_NOP` | `DB E0` | FPU Enable Interrupts (8087) | Documented for the Intel 80287. Present on all Intel x87 FPUs from 80287 onwards. For FPUs other than the ones where they were introduced on (8087 for `FENI`/`FDISI` and 80287 for `FSETPM`), they act as `NOP`s. These instructions and their operation on modern CPUs are commonly mentioned in later Intel documentation, but with opcodes omitted and opcode table entries left blank (e.g. Intel SDM 325462-077, April 2022 mentions them twice without opcodes). The opcodes are, however, recognized by Intel XED. |
| `FDISI`, `FDISI8087_NOP` | `DB E1` | FPU Disable Interrupts (8087) |   |
| `FSETPM`, `FSETPM287_NOP` | `DB E4` | FPU Set Protected Mode (80287) |   |
| (no mnemonic) | `D9 D7`,  `D9 E2`, `D9 E7`,  `DD FC`, `DE D8`,  `DE DA`, `DE DC`,  `DE DD`, `DE DE`,  `DF FC` | "Reserved by Cyrix" opcodes | These opcodes are listed as reserved opcodes that will produce "unpredictable results" without generating exceptions on at least Cyrix 6x86, 6x86MX, MII, MediaGX, and AMD Geode GX/LX. (The documentation for these CPUs all list the same ten opcodes.) Their actual operation is not known, nor is it known whether their operation is the same on all of these CPUs. |
