---
title: "List of x86 instructions (part 2/5)"
source: https://en.wikipedia.org/wiki/X86_instruction_listings
domain: x86-assembly
license: CC-BY-SA-4.0
tags: x86 assembly, assembly language, x86, x86-64, amd64, asm
fetched: 2026-07-02
part: 2/5
---

# List of x86 instructions

| Instruction | Opcode | Description | Ring | Added in |
|---|---|---|---|---|
|   |   |   |   |   |
| `RDMSR` | `0F 32` | Read Model-specific register. The MSR to read is specified in ECX. The value of the MSR is then returned as a 64-bit value in EDX:EAX. Instruction is not serializing. | 0 | IBM 386SLC, Intel Pentium, AMD K5, Cyrix 6x86MX,MediaGXm, IDT WinChip C6, Transmeta Crusoe, DM&P Vortex86DX3 |
| `WRMSR` | `0F 30` | Write Model-specific register. The MSR to write is specified in ECX, and the 64-bit value to write is given in EDX:EAX. Instruction is, with some exceptions, serializing. |   |   |
| `RSM` | `0F AA` | Resume from System Management Mode. Instruction is serializing. | -2 (SMM) | Intel 386SL, 486SL, Intel Pentium, AMD 5x86, Cyrix 486SLC/e, IDT WinChip C6, Transmeta Crusoe, Rise mP6 |
| `CPUID` | `0F A2` | CPU Identification and feature information. Takes as input a CPUID leaf index in EAX and, depending on leaf, a sub-index in ECX. Result is returned in EAX,EBX,ECX,EDX. Instruction is serializing, and causes a mandatory #VMEXIT under virtualization. Support for `CPUID` can be checked by toggling bit 21 of EFLAGS (EFLAGS.ID) – if this bit can be toggled, `CPUID` is present. | Usually 3 | Intel Pentium, AMD 5x86, Cyrix 5x86, IDT WinChip C6, Transmeta Crusoe, Rise mP6, NexGen Nx586, UMC Green CPU |
| `CMPXCHG8B m64` | `0F C7 /1` | Compare and Exchange 8 bytes. Compares EDX:EAX with m64. If equal, set ZF and store ECX:EBX into m64. Else, clear ZF and load m64 into EDX:EAX. Instruction atomic only if used with `LOCK` prefix. | 3 | Intel Pentium, AMD K5, Cyrix 6x86L,MediaGXm, IDT WinChip C6, Transmeta Crusoe, Rise mP6, DM&P Vortex86DX2 |
| `RDTSC` | `0F 31` | Read 64-bit Time Stamp Counter (TSC) into EDX:EAX. In early processors, the TSC was a cycle counter, incrementing by 1 for each clock cycle (which could cause its rate to vary on processors that could change clock speed at runtime) – in later processors, it increments at a fixed rate that doesn't necessarily match the CPU clock speed. | Usually 3 | Intel Pentium, AMD K5, Cyrix 6x86MX,MediaGXm, IDT WinChip C6, Transmeta Crusoe, Rise mP6, DM&P Vortex86DX3 |
|   |   |   |   |   |
| `RDPMC` | `0F 33` | Read Performance Monitoring Counter. The counter to read is specified by ECX and its value is returned in EDX:EAX. | Usually 3 | Intel Pentium MMX, Intel Pentium Pro, AMD K7, Cyrix 6x86MX, IDT WinChip C6, AMD Geode LX, VIA Nano |
| `CMOVcc reg,r/m` | `0F 4x /r` | Conditional move to register. The source operand may be either register or memory. | 3 | Intel Pentium Pro, AMD K7, Cyrix 6x86MX,MediaGXm, Transmeta Crusoe, VIA C3 "Nehemiah", DM&P Vortex86DX3 |
|   |   |   |   |   |
| `NOP r/m`, `NOPL r/m` | `NFx 0F 1F /0` | Official long NOP. Other than AMD K7/K8, broadly unsupported in non-Intel processors released before 2005. | 3 | Intel Pentium Pro, AMD K7, x86-64, VIA C7 |
| `UD2`, `UD2A` | `0F 0B` | Undefined Instructions – will generate an invalid opcode (#UD) exception in all operating modes. These instructions are provided for software testing to explicitly generate invalid opcodes. The opcodes for these instructions are reserved for this purpose. | (3) | (80186), Intel Pentium |
| `UD1 reg,r/m`, `UD2B reg,r/m` | `0F B9`, `0F B9 /r` |   |   |   |
| `OIO`, `UD0`, `UD0 reg,r/m` | `0F FF`, `0F FF /r` | (80186), Cyrix 6x86, AMD K5 |   |   |
|   |   |   |   |   |
| `SYSCALL` | `0F 05` | Fast System call. | 3 | AMD K6, x86-64 |
| `SYSRET` | `0F 07` | Fast Return from System Call. Designed to be used together with `SYSCALL`. | 0 |   |
| `SYSENTER` | `0F 34` | Fast System call. | 3 | Intel Pentium II, AMD K7, Transmeta Crusoe, NatSemi Geode GX2, VIA C3 "Nehemiah", DM&P Vortex86DX3 |
| `SYSEXIT` | `0F 35` | Fast Return from System Call. Designed to be used together with `SYSENTER`. | 0 |   |

1. Early Intel 64 documentation indicated that for the `RDMSR`, `WRMSR` and `RDPMC` instructions in 64-bit mode, the instructions could be encoded with a `REX.W` prefix to make them interpret the RCX register as a full 64-bit MSR/PMC index. This was removed from later Intel 64 documentation (SDM rev 023 and later), which indicates that these instructions always ignore the top 32 bits of RCX regardless of any REX prefixes.On all known x86-64 processors, these instructions will accept but ignore the REX prefix, and ignore the top 32 bits of RCX.
2. In 64-bit mode, the `RDMSR`, `RDTSC` and `RDPMC` instructions will set the top 32 bits of RDX and RAX to zero.
3. For some CPU/MSR combinations, the `RDMSR` and `WRMSR` instructions may make use of registers other than ECX and EDX:EAX. Known examples of this include the use of EDI and ESI for a password, and EBX for a physical memory address.
4. MSR reads done with the `RDMSR` and `RDMSRLIST` instructions can, in general, be reordered with respect to other instructions, including other MSR reads — with the following restrictions: MSR accesses cannot be reordered across serializing instructions (e.g. `CPUID`,`IRET`) or dispatch-serializing instructions (e.g. `LFENCE`). MSR reads of the `IA32_BARRIER` MSR (MSR `2Fh`, introduced with the MSRLIST instruction set extension) cannot be reordered across other MSR reads. Accesses to the x2APIC MSRs cannot be reordered with respect to each other.
5. On Intel, AMD and VIA CPUs, the `WRMSR` instruction is also used to update the CPU microcode. This is done by writing the virtual address of the new microcode to upload to MSR `79h` on Intel and VIA CPUs and MSR `C001_0020h` on AMD CPUs.
6. Writes to the following MSRs are not serializing: NumberName `48h`SPEC_CTRL `49h`PRED_CMD `10Bh`FLUSH_CMD `122h`TSX_CTRL `6E0h`TSC_DEADLINE `6E1h`PKRS `774h`HWP_REQUEST (non-serializing only if the FAST_IA32_­HWP_REQUEST bit it set) `802h` to `83Fh`(x2APIC MSRs) `1B01h`UARCH_MISC_CTL `C001_0100h`FS_BASE (non-serializing on AMD Zen 4 and later) `C001_0101h`GS_BASE (Zen 4 and later) `C001_0102h`KernelGSbase (Zen 4 and later) `C001_011Bh`Doorbell Register (AMD-specific) `WRMSR` to the x2APIC ICR (Interrupt Command Register; MSR `830h`) is commonly used to produce an IPI (Inter-processor interrupt) - on Intel but not AMD CPUs, such an IPI can be reordered before an older memory store.
7. System Management Mode and the `RSM` instruction were made available on non-SL variants of the Intel 486 only after the initial release of the Intel Pentium in 1993.
8. On some older 32-bit processors, executing `CPUID` with a leaf index (EAX) greater than 0 may leave EBX and ECX unmodified, keeping their old values. For this reason, it is recommended to zero out EBX and ECX before executing `CPUID`. Processors noted to exhibit this behavior include Cyrix MII and IDT WinChip 2. In 64-bit mode, `CPUID` will set the top 32 bits of RAX, RBX, RCX and RDX to zero.
9. On some Intel processors starting from Ivy Bridge, there exists MSRs that can be used to restrict `CPUID` to ring 0. Such MSRs are documented for at least Ivy Bridge and Denverton. The ability to restrict `CPUID` to ring 0 also exists on AMD processors supporting the "CpuidUserDis" feature (Zen 4 "Raphael" and later).
10. `CPUID` is also available on some Intel and AMD 486 processor variants that were released after the initial release of the Intel Pentium.
11. On the Cyrix 5x86 and 6x86 CPUs, `CPUID` is not enabled by default and must be enabled through a Cyrix configuration register.
12. On NexGen CPUs, `CPUID` is only supported with some system BIOSes. On some NexGen CPUs that do support `CPUID`, EFLAGS.ID is not supported but EFLAGS.AC is, complicating CPU detection.
13. Unlike the older `CMPXCHG` instruction, the `CMPXCHG8B` instruction does not modify any EFLAGS bits other than ZF.
14. `LOCK CMPXCHG8B` with a register operand (which is an invalid encoding) will, on some Intel Pentium CPUs, cause a hang rather than the expected #UD exception - this is known as the Pentium F00F bug.
15. On IDT WinChip, Transmeta Crusoe and Rise mP6 processors, the `CMPXCHG8B` instruction is always supported, however its CPUID bit may be missing. This is a workaround for a bug in Windows NT.
16. The `RDTSC` and `RDPMC` instructions are not ordered with respect to other instructions, and may sample their respective counters before earlier instructions are executed or after later instructions have executed. Invocations of `RDPMC` (but not `RDTSC`) may be reordered relative to each other even for reads of the same counter. In order to impose ordering with respect to other instructions, `LFENCE` or serializing instructions (e.g. `CPUID`) are needed.
17. On all x86 processors that support both `RDTSC` and MSRs, the TSC is available as MSR `10h`, which can be read and written using the `RDMSR`/`WRMSR` instructions.On the earliest implementations (e.g. P5 Pentium, AMD K5), as well as on all processors that support x86-64, this MSR can be read and written as a full 64-bit register — however, on some non-x86-64 processors (e.g. Intel Pentium Pro, VIA C3, Transmeta Efficeon), attempts at writing a value of $2^{32}$ or larger will cause the written value to be ANDed with `0xFFFFFFFF`, clearing the top 32 bits.On many newer processors (starting from Intel Haswell/Silvermont, Zhaoxin ZX-C and AMD Zen 5), the `TSC_ADJUST` MSR (MSR `3Bh`) is available (indicated by `CPUID.(EAX=7,ECX=0):EBX[1]`). On processors with this MSR, there exists a systemwide/"true" TSC which is shared or synchronized between all CPU cores — reading the TSC with `RDTSC` or MSR `10h` will return the "true" TSC value plus the value of `TSC_ADJUST`; attempts at writing to MSR `10h` will cause the CPU to compute the difference between the provided write-value and the "true" TSC and write that difference to `TSC_ADJUST`; synchronizing the TSC across processor cores can be done by writing the same value to `TSC_ADJUST` on each logical processor.
18. Fixed-rate TSC was introduced in two stages: *Constant TSC*TSC running at a fixed rate as long as the processor core is not in a deep-sleep (C2 or deeper) mode, but not synchronized between CPU cores. Introduced in Intel Prescott, Yonah and Bonnell. Also present in all Transmeta and VIA Nano CPUs, as well as AMD Geode LX. Does not have a CPUID bit.*Invariant TSC (Nonstop TSC)*TSC running at a fixed rate, and incrementing in a synchronized manner between all CPU cores in all P-,C- and T-states (but not necessarily S-states). Present in AMD K10 and later; Intel Nehalem/Saltwell and later; Zhaoxin WuDaoKou and later. Indicated with a CPUID bit (leaf `8000_0007:EDX[8]`).On Intel processors, Intel guarantees that the time-stamp counter will not wraparound within 10 years of being reset.
19. `RDTSC` can be run outside Ring 0 only if `CR4.TSD=0`. On Intel Pentium and AMD K5/K6, `RDTSC` cannot be run in Virtual-8086 mode. Later processors (Pentium Pro, Athlon 64) removed this restriction.
20. `RDPMC` can be run outside Ring 0 only if `CR4.PCE=1`.
21. The `RDPMC` instruction is not present in VIA processors prior to the Nano.
22. The condition codes supported for `CMOV**cc**` instruction (opcode `0F 4**x** /r`, with the **x** nibble specifying the condition) are: xccCondition (EFLAGS) 0OOF=1: "Overflow" 1NOOF=0: "Not Overflow" 2C,B,NAECF=1: "Carry", "Below", "Not Above or Equal" 3NC,NB,AECF=0: "Not Carry", "Not Below", "Above or Equal" 4Z,EZF=1: "Zero", "Equal" 5NZ,NEZF=0: "Not Zero", "Not Equal" 6NA,BE(CF=1 or ZF=1): "Not Above", "Below or Equal" 7A,NBE(CF=0 and ZF=0): "Above", "Not Below or Equal" 8SSF=1: "Sign" 9NSSF=0: "Not Sign" AP,PEPF=1: "Parity", "Parity Even" BNP,POPF=0: "Not Parity", "Parity Odd" CL,NGESF≠OF: "Less", "Not Greater Or Equal" DNL,GESF=OF: "Not Less", "Greater Or Equal" ELE,NG(ZF=1 or SF≠OF): "Less or Equal", "Not Greater" FNLE,G(ZF=0 and SF=OF): "Not Less or Equal", "Greater"
23. In 64-bit mode, `CMOVcc` with a 32-bit operand size will clear the upper 32 bits of the destination register even if the condition is false. For `CMOVcc` with a memory source operand, the CPU will always read the operand from memory – potentially causing memory exceptions and cache line-fills – even if the condition for the move is not satisfied. (The Intel APX extension defines a set of new EVEX-encoded variants of `CMOVcc` that will suppress memory exceptions if the condition is false.)
24. On pre-Nehemiah VIA C3 variants ("Samuel"/"Ezra"), the `reg,reg` but not `reg,[mem]` forms of the `CMOVcc` instructions have been reported to be present as undocumented instructions.
25. Intel's recommended byte encodings for multi-byte NOPs of lengths 2 to 9 bytes in 32/64-bit mode are (in hex): LengthByte Sequence 2`66 90` 3`0F 1F 00` 4`0F 1F 40 00` 5`0F 1F 44 00 00` 6`66 0F 1F 44 00 00` 7`0F 1F 80 00 00 00 00` 8`0F 1F 84 00 00 00 00 00` 9`66 0F 1F 84 00 00 00 00 00` For cases where there is a need to use more than 9 bytes of NOP padding, it is recommended to use multiple NOPs.
26. Unlike other instructions added in Pentium Pro, long NOP does not have a CPUID feature bit.As of April 2026, the Intel SDM indicates that the long NOP is available on Family 6 and 15 CPUs — this holds for Intel CPUs, but some Family 6 CPUs from non-Intel vendors (e.g. Cyrix 6x86MX and VIA C3) do not support it.The Linux kernel (version 2.6.27 and later) treats long NOP as unavailable in 32-bit mode due to a lack of a reliable way to detect it.
27. `0F 1F /0` as long-NOP was introduced in the Pentium Pro, but remained undocumented until 2006. The whole `0F 18..1F` opcode range was `NOP` in Pentium Pro. However, except for `0F 1F /0`, Intel does not guarantee that these opcodes will remain `NOP` in future processors, and have indeed assigned some of these opcodes to other instructions in at least some processors.
28. Documented for AMD x86-64 since 2002.
29. While the `0F 0B` opcode was officially reserved as an invalid opcode from Pentium onwards, it only got assigned the mnemonic `UD2` from Pentium Pro onwards.
30. GNU Binutils have used the `UD2A` and `UD2B` mnemonics for the `0F 0B` and `0F B9` opcodes since version 2.7. Neither `UD2A` nor `UD2B` originally took any arguments - `UD2B` was later modified to accept a ModR/M byte, in Binutils version 2.30.
31. The `UD2` (`0F 0B`) instruction will additionally stop subsequent bytes from being decoded as instructions, even speculatively. For this reason, if an indirect branch instruction is followed by something that is not code, it is recommended to place an `UD2` instruction after the indirect branch.
32. The UD0/1/2 opcodes - `0F 0B`, `0F B9` and `0F FF` - will cause an #UD exception on all x86 processors from the 80186 onwards (except NEC V-series processors), but did not get explicitly reserved for this purpose until P5-class processors.
33. While the `0F B9` opcode was officially reserved as an invalid opcode from Pentium onwards, it only got assigned its mnemonic `UD1` much later – AMD APM started listing `UD1` in its opcode maps from rev 3.17 onwards, while Intel SDM started listing it from rev 061 onwards.
34. For both the `0F B9` and `0F FF` opcodes, different x86 implementations are known to differ regarding whether the opcodes accept a ModR/M byte.
35. For the `0F FF` opcode, the `OIO` mnemonic was introduced by Cyrix, while the `UD0` menmonic (without arguments) was introduced by AMD and Intel at the same time as the `UD1` mnemonic for `0F B9`. Later Intel (but not AMD) documentation modified its description of `UD0` to add a ModR/M byte and take two arguments.
36. The `SYSRET`, `SYSENTER` and `SYSEXIT` instructions are unavailable in Real mode. `SYSENTER` is, however, available in Virtual 8086 mode.On AMD processors, the `SYSCALL` instruction is available in all operating modes, including Real Mode.If FRED (Flexible Return and Event Delivery) is enabled, then the `SYSRET` and `SYSEXIT` instructions are unavailable.
37. On K6, the `SYSCALL`/`SYSRET` instructions were available on Model 7 (250nm "Little Foot") and later, not on the earlier Model 6.
38. `SYSCALL` and `SYSRET` were made an integral part of x86-64 – as a result, the instructions are available in 64-bit mode on all x86-64 processors from AMD, Intel, VIA and Zhaoxin. Outside 64-bit mode, the instructions are available on AMD processors only.
39. The exact semantics of `SYSRET` differs slightly between AMD and Intel processors: non-canonical return addresses cause a #GP exception to be thrown in Ring 3 on AMD CPUs but Ring 0 on Intel CPUs. This has been known to cause security issues.
40. For the `SYSRET` and `SYSEXIT` instructions under x86-64, it is necessary to add the `REX.W` prefix for variants that will return to 64-bit user-mode code.Encodings of these instructions without the `REX.W` prefix are used to return to 32-bit user-mode code. (Neither of these instructions can be used to return to 16-bit user-mode code — for return to 16-bit code, `IRET`/`IRETD`/`IRETQ` should be used.)For variants of the `SYSRET` and `SYSEXIT` instructions encoded with the `REX.W` prefix, some assemblers (e.g. FASM and GNU Binutils) support the mnemonics `SYSRETQ` and `SYSEXITQ`, however these mnemonics are not used in Intel/AMD documentation.
41. The `CPUID` flags that indicate support for `SYSENTER`/`SYSEXIT` are set on the Pentium Pro, even though the processor does not officially support these instructions. Third party testing indicates that the opcodes are present on the Pentium Pro but too buggy to be usable.
42. On AMD CPUs, the `SYSENTER` and `SYSEXIT` instructions are not available in x86-64 long mode (#UD).
43. On Transmeta CPUs, the `SYSENTER` and `SYSEXIT` instructions are only available with version 4.2 or higher of the Transmeta Code Morphing software.
44. On Nehemiah, `SYSENTER` and `SYSEXIT` are available only on stepping 8 and later.

### Added as instruction set extensions

#### Added with x86-64

These instructions can only be encoded in 64 bit mode. They fall in four groups:

- original instructions that reuse existing opcodes for a different purpose (`MOVSXD` replacing `ARPL`)
- original instructions with new opcodes (`SWAPGS`)
- existing instructions extended to a 64 bit address size (`JRCXZ`)
- existing instructions extended to a 64 bit operand size (remaining instructions)

Most instructions with a 64 bit operand size encode this using a `REX.W` prefix; in the absence of the `REX.W` prefix, the corresponding instruction with 32 bit operand size is encoded. This mechanism also applies to most other instructions with 32 bit operand size. These are not listed here as they do not gain a new mnemonic in Intel syntax when used with a 64 bit operand size.

| Instruction | Encoding | Meaning | Ring |
|---|---|---|---|
| `CDQE` | `REX.W 98` | Sign extend EAX into RAX | 3 |
| `CQO` | `REX.W 99` | Sign extend RAX into RDX:RAX |   |
| `CMPSQ` | `REX.W A7` | CoMPare String Quadword |   |
| `CMPXCHG16B m128` | `REX.W 0F C7 /1` | CoMPare and eXCHanGe 16 Bytes. Atomic only if used with LOCK prefix. |   |
| `IRETQ` | `REX.W CF` | 64-bit Return from Interrupt |   |
| `JRCXZ rel8` | `E3 *cb*` | Jump if RCX is zero |   |
| `LODSQ` | `REX.W AD` | LoaD String Quadword |   |
| `MOVSXD r64,r/m32` | `REX.W 63 /r` | MOV with Sign Extend 32-bit to 64-bit |   |
| `MOVSQ` | `REX.W A5` | Move String Quadword |   |
| `POPFQ` | `9D` | POP RFLAGS Register |   |
| `PUSHFQ` | `9C` | PUSH RFLAGS Register |   |
| `SCASQ` | `REX.W AF` | SCAn String Quadword |   |
| `STOSQ` | `REX.W AB` | STOre String Quadword |   |
| `SWAPGS` | `0F 01 F8` | Exchange GS base with KernelGSBase MSR | 0 |
| `UDB` | `D6` | Undefined instruction — will generate an invalid opcode (#UD) exception in 64-bit mode. | (3) |

1. The memory operand to `CMPXCHG16B` must be 16-byte aligned.
2. The `CMPXCHG16B` instruction was absent from a few of the earliest Intel/AMD x86-64 processors. On Intel processors, the instruction was missing from Xeon "Nocona" stepping D, but added in stepping E. On AMD K8 family processors, it was added in stepping F, at the same time as DDR2 support was introduced. For this reason, `CMPXCHG16B` has its own CPUID flag, separate from the rest of x86-64.
3. Encodings of `MOVSXD` without REX.W prefix are permitted but discouraged – such encodings behave identically to 16/32-bit `MOV` (`8B /r`).
4. The `UDB` opcode - `D6` - will cause an #UD (invalid instruction) exception in 64-bit mode on all known x86-64 processors, but was only explicitly reserved for this purpose and assigned the `UDB` mnemonic in 2025. The `D6` opcode will cause #UD in 64-bit mode only - in 16-bit and 32-bit modes (legacy and compatibility), it will, on most x86 processors, execute as the `SALC` instruction.

#### Bit manipulation extensions

Bit manipulation instructions. For all of the VEX-encoded instructions defined by BMI1 and BMI2, the operand size may be 32 or 64 bits, controlled by the VEX.W bit – none of these instructions are available in 16-bit variants. The VEX-encoded instructions are not available in Real Mode and Virtual-8086 mode - other than that, the bit manipulation instructions are available in all operating modes on supported CPUs.

| Bit Manipulation Extension | Instruction mnemonics | Opcode | Instruction description | Added in |
|---|---|---|---|---|
|   |   |   |   |   |
| *ABM (LZCNT)*Advanced Bit Manipulation | `POPCNT r16,r/m16` `POPCNT r32,r/m32` | `F3 0F B8 /r` | Population Count. Counts the number of bits that are set to 1 in its source argument. | K10, Bobcat, Haswell, ZhangJiang, Gracemont |
| `POPCNT r64,r/m64` | `F3 REX.W 0F B8 /r` |   |   |   |
| `LZCNT r16,r/m16` `LZCNT r32,r/m32` | `F3 0F BD /r` | Count Leading zeroes. If source operand is all-0s, then `LZCNT` will return operand size in bits (16/32/64) and set CF=1. |   |   |
| `LZCNT r64,r/m64` | `F3 REX.W 0F BD /r` |   |   |   |
|   |   |   |   |   |
| *BMI1*Bit Manipulation Instruction Set 1 | `TZCNT r16,r/m16` `TZCNT r32,r/m32` | `F3 0F BC /r` | Count Trailing zeroes. If source operand is all-0s, then `TZCNT` will return operand size in bits (16/32/64) and set CF=1. | Haswell, Piledriver, Jaguar, ZhangJiang, Gracemont |
| `TZCNT r64,r/m64` | `F3 REX.W 0F BC /r` |   |   |   |
| `ANDN ra,rb,r/m` | `VEX.LZ.0F38 F2 /r` | Bitwise AND-NOT: `ra = r/m AND NOT(rb)` |   |   |
| `BEXTR ra,r/m,rb` | `VEX.LZ.0F38 F7 /r` | Bitfield extract. Bitfield start position is specified in bits [7:0] of `rb`, length in bits[15:8] of `rb`. The bitfield is then extracted from the `r/m` value with zero-extension, then stored in `ra`. Equivalent tomask = (1 << rb[15:8]) - 1 ra = (r/m >> rb[7:0]) AND mask |   |   |
| `BLSI reg,r/m` | `VEX.LZ.0F38 F3 /3` | Extract lowest set bit in source argument. Returns 0 if source argument is 0. Equivalent to `dst = (-src) AND src` |   |   |
| `BLSMSK reg,r/m` | `VEX.LZ.0F38 F3 /2` | Generate a bitmask of all-1s bits up to the lowest bit position with a 1 in the source argument. Returns all-1s if source argument is 0. Equivalent to `dst = (src-1) XOR src` |   |   |
| `BLSR reg,r/m` | `VEX.LZ.0F38 F3 /1` | Copy all bits of the source argument, then clear the lowest set bit. Equivalent to `dst = (src-1) AND src` |   |   |
|   |   |   |   |   |
| *BMI2*Bit Manipulation Instruction Set 2 | `BZHI ra,r/m,rb` | `VEX.LZ.0F38 F5 /r` | Zero out high-order bits in `r/m` starting from the bit position specified in `rb`, then write result to `rd`. Equivalent to `ra = r/m AND NOT(-1 << rb[7:0])` | Haswell, Excavator, ZhangJiang, Gracemont |
| `MULX ra,rb,r/m` | `VEX.LZ.F2.0F38 F6 /r` | Widening unsigned integer multiply without setting flags. Multiplies EDX/RDX with `r/m`, then stores the low half of the multiplication result in `ra` and the high half in `rb`. If `ra` and `rb` specify the same register, only the high half of the result is stored. |   |   |
| `PDEP ra,rb,r/m` | `VEX.LZ.F2.0F38 F5 /r` | Parallel Bit Deposit. Scatters contiguous bits from `rb` to the bit positions set in `r/m`, then stores result to `ra`. Operation performed is:ra=0; k=0; mask=r/m for i=0 to opsize-1 do if (mask[i] == 1) then ra[i]=rb[k]; k=k+1 |   |   |
| `PEXT ra,rb,r/m` | `VEX.LZ.F3.0F38 F5 /r` | Parallel Bit Extract. Uses `r/m` argument as a bit mask to select bits in `rb`, then compacts the selected bits into a contiguous bit-vector. Operation performed is:ra=0; k=0; mask=r/m for i=0 to opsize-1 do if (mask[i] == 1) then ra[k]=rb[i]; k=k+1 |   |   |
| `RORX reg,r/m,imm8` | `VEX.LZ.F2.0F3A F0 /r *ib*` | Rotate right by immediate without affecting flags. |   |   |
| `SARX ra,r/m,rb` | `VEX.LZ.F3.0F38 F7 /r` | Arithmetic shift right without updating flags. For `SARX`, `SHRX` and `SHLX`, the shift-amount specified in `rb` is masked to 5 bits for 32-bit operand size and 6 bits for 64-bit operand size. |   |   |
| `SHRX ra,r/m,rb` | `VEX.LZ.F2.0F38 F7 /r` | Logical shift right without updating flags. |   |   |
| `SHLX ra,r/m,rb` | `VEX.LZ.66.0F38 F7 /r` | Shift left without updating flags. |   |   |

1. On AMD CPUs, the "ABM" extension provides both `POPCNT` and `LZCNT`. On Intel CPUs, however, the CPUID bit for "ABM" is only documented to indicate the presence of the `LZCNT` instruction and is listed as "LZCNT", while `POPCNT` has its own separate CPUID feature bit. However, all known processors that implement the "ABM"/"LZCNT" extensions also implement `POPCNT` and set the CPUID feature bit for POPCNT, so the distinction is theoretical only. (The converse is not true – there exist processors that support `POPCNT` but not ABM, such as Intel Nehalem and VIA Nano 3000.)
2. The `LZCNT` instruction will execute as `BSR` on systems that do not support the LZCNT or ABM extensions. `BSR` computes the index of the highest set bit in the source operand, producing a different result from `LZCNT` for most input values.
3. The `TZCNT` instruction will execute as `BSF` on systems that do not support the BMI1 extension. `BSF` produces the same result as `TZCNT` for all input operand values except zero – for which `TZCNT` returns input operand size, but `BSF` produces undefined behavior (leaves destination unmodified on most modern CPUs).
4. For `BEXTR`, the start position and length are not masked and can take values from 0 to 255. If the selected bits extend beyond the end of the `r/m` argument (which has the usual 32/64-bit operand size), then the out-of-bounds bits are read out as 0.
5. On AMD processors before Zen 3, the `PEXT` and `PDEP` instructions are quite slow and exhibit data-dependent timing due to the use of a microcoded implementation (about 18 to 300 cycles, depending on the number of bits set in the mask argument). As a result, it is often faster to use other instruction sequences on these processors.

#### Added with Intel TSX

| TSX Subset | Instruction | Opcode | Description | Added in |
|---|---|---|---|---|
|   |   |   |   |   |
| *RTM*Restricted Transactional memory | `XBEGIN rel16` `XBEGIN rel32` | `C7 F8 *cw*` `C7 F8 *cd*` | Start transaction. If transaction fails, perform a branch to the given relative offset. | Haswell (Deprecated on desktop/laptop CPUs from 10th generation (Ice Lake, Comet Lake) onwards, but continues to be available on Xeon-branded server parts (e.g. Ice Lake-SP, Sapphire Rapids)) |
| `XABORT imm8` | `C6 F8 *ib*` | Abort transaction with 8-bit immediate as error code. |   |   |
| `XEND` | `NP 0F 01 D5` | End transaction. |   |   |
| `XTEST` | `NP 0F 01 D6` | Test if in transactional execution. Sets `EFLAGS.ZF` to 0 if executed inside a transaction (RTM or HLE), 1 otherwise. |   |   |
|   |   |   |   |   |
| *HLE*Hardware Lock Elision | `XACQUIRE` | `F2` | Instruction prefix to indicate start of hardware lock elision, used with memory atomic instructions only (for other instructions, the `F2` prefix may have other meanings). When used with such instructions, may start a transaction instead of performing the memory atomic operation. | Haswell (Discontinued – the last processors to support HLE were Coffee Lake and Cascade Lake) |
| `XRELEASE` | `F3` | Instruction prefix to indicate end of hardware lock elision, used with memory atomic/store instructions only (for other instructions, the `F3` prefix may have other meanings). When used with such instructions during hardware lock elision, will end the associated transaction instead of performing the store/atomic. |   |   |
|   |   |   |   |   |
| *TSXLDTRK*Load Address Tracking suspend/resume | `XSUSLDTRK` | `F2 0F 01 E8` | Suspend Tracking Load Addresses | Sapphire Rapids |
| `XRESLDTRK` | `F2 0F 01 E9` | Resume Tracking Load Addresses |   |   |

#### Added with Intel CET
