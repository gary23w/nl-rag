---
title: "List of x86 instructions (part 6/6)"
source: https://en.wikipedia.org/wiki/X86_instruction_listings
domain: x86-assembly
license: CC-BY-SA-4.0
tags: x86 assembly, assembly language, x86, x86-64, amd64, asm
fetched: 2026-07-02
part: 6/6
---

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
