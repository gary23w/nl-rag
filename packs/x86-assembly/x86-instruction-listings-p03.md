---
title: "List of x86 instructions (part 3/5)"
source: https://en.wikipedia.org/wiki/X86_instruction_listings
domain: x86-assembly
license: CC-BY-SA-4.0
tags: x86 assembly, assembly language, x86, x86-64, amd64, asm
fetched: 2026-07-02
part: 3/5
---

# List of x86 instructions

Intel CET (Control-Flow Enforcement Technology) adds two distinct features to help protect against security exploits such as return-oriented programming: a shadow stack (CET_SS), and indirect branch tracking (CET_IBT).

| CET Subset | Instruction | Opcode | Description | Ring | Added in |
|---|---|---|---|---|---|
|   |   |   |   |   |   |
| *CET_SS*Shadow stack. When shadow stacks are enabled, return addresses are pushed on both the regular stack and the shadow stack when a function call is made. They are then both popped on return from the function call – if they do not match, then the stack is assumed to be corrupted, and a #CP exception is issued. The shadow stack is additionally required to be stored in specially marked memory pages which cannot be modified by normal memory store instructions. | `INCSSPD r32` | `F3 0F AE /5` | Increment shadow stack pointer | 3 | Tiger Lake, Zen 3 |
| `INCSSPQ r64` | `F3 REX.W 0F AE /5` |   |   |   |   |
| `RDSSPD r32` | `F3 0F 1E /1` | Read shadow stack pointer into register (low 32 bits) |   |   |   |
| `RDSSPQ r64` | `F3 REX.W 0F 1E /1` | Read shadow stack pointer into register (full 64 bits) |   |   |   |
| `SAVEPREVSSP` | `F3 0F 01 EA` | Save previous shadow stack pointer |   |   |   |
| `RSTORSSP m64` | `F3 0F 01 /5` | Restore saved shadow stack pointer |   |   |   |
| `WRSSD m32,r32` | `NP 0F 38 F6 /r` | Write 4 bytes to shadow stack |   |   |   |
| `WRSSQ m64,r64` | `NP REX.W 0F 38 F6 /r` | Write 8 bytes to shadow stack |   |   |   |
| `WRUSSD m32,r32` | `66 0F 38 F5 /r` | Write 4 bytes to user shadow stack | 0 |   |   |
| `WRUSSQ m64,r64` | `66 REX.W 0F 38 F5 /r` | Write 8 bytes to user shadow stack |   |   |   |
| `SETSSBSY` | `F3 0F 01 E8` | Mark shadow stack busy |   |   |   |
| `CLRSSBSY m64` | `F3 0F AE /6` | Clear shadow stack busy flag |   |   |   |
|   |   |   |   |   |   |
| *CET_IBT*Indirect Branch Tracking. When IBT is enabled, an indirect branch (jump, call, return) to any instruction that is not an `ENDBR32/64` instruction will cause a #CP exception. | `ENDBR32` | `F3 0F 1E FB` | Terminate indirect branch in 32-bit mode | 3 | Tiger Lake |
| `ENDBR64` | `F3 0F 1E FA` | Terminate indirect branch in 64-bit mode |   |   |   |
| `NOTRACK` | `3E` | Prefix used with indirect `CALL`/`JMP` near instructions (opcodes `FF /2` and `FF /4`) to indicate that the branch target is not required to start with an `ENDBR32/64` instruction. Prefix only honored when NO_TRACK_EN flag is set. |   |   |   |

1. The `RDSSPD` and `RDSSPQ` instructions act as NOPs on processors where shadow stacks are disabled or CET is not supported.
2. `ENDBR32` and `ENDBR64` act as NOPs on processors that don't support CET_IBT or where IBT is disabled.
3. This prefix has the same encoding as the DS: segment override prefix – as of April 2022, Intel documentation does not appear to specify whether this prefix also retains its old segment-override function when used as a no-track prefix, nor does it provide an official mnemonic for this prefix. (GNU binutils use "notrack")

#### Added with XSAVE

The XSAVE instruction set extensions are designed to save/restore CPU extended state (typically for the purpose of context switching) in a manner that can be extended to cover new instruction set extensions without the OS context-switching code needing to understand the specifics of the new extensions. This is done by defining a series of *state-components*, each with a size and offset within a given save area, and each corresponding to a subset of the state needed for one CPU extension or another. The `EAX=0Dh` CPUID leaf is used to provide information about which state-components the CPU supports and what their sizes/offsets are, so that the OS can reserve the proper amount of space and set the associated enable-bits.

| XSAVE Extension | Instruction mnemonics | Opcode | Instruction description | Ring | Added in |
|---|---|---|---|---|---|
|   |   |   |   |   |   |
| *XSAVE*Processor Extended State Save/Restore. | `XSAVE mem` `XSAVE64 mem` | `NP 0F AE /4` `NP REX.W 0F AE /4` | Save state components specified by bitmap in EDX:EAX to memory. | 3 | Penryn, Bulldozer, Jaguar, Goldmont, ZhangJiang |
| `XRSTOR mem` `XRSTOR64 mem` | `NP 0F AE /5` `NP REX.W 0F AE /5` | Restore state components specified by EDX:EAX from memory. |   |   |   |
| `XGETBV` | `NP 0F 01 D0` | Get value of Extended Control Register. Reads an XCR specified by ECX into EDX:EAX. |   |   |   |
| `XSETBV` | `NP 0F 01 D1` | Set Extended Control Register. Write the value in EDX:EAX to the XCR specified by ECX. | 0 |   |   |
|   |   |   |   |   |   |
| *XSAVEOPT*Processor Extended State Save/Restore Optimized | `XSAVEOPT mem` `XSAVEOPT64 mem` | `NP 0F AE /6` `NP REX.W 0F AE /6` | Save state components specified by EDX:EAX to memory. Unlike the older `XSAVE` instruction, `XSAVEOPT` may abstain from writing processor state items to memory when the CPU can determine that they haven't been modified since the most recent corresponding `XRSTOR`. | 3 | Sandy Bridge, Steamroller, Puma, Goldmont, ZhangJiang |
|   |   |   |   |   |   |
| *XSAVEC*Processor Extended State save/restore with compaction. | `XSAVEC mem` `XSAVEC64 mem` | `NP 0F C7 /4` `NP REX.W 0F C7 /4` | Save processor extended state components specified by EDX:EAX to memory with compaction. | 3 | Skylake, Goldmont, Zen 1, Shijidadao |
|   |   |   |   |   |   |
| *XSS*Processor Extended State save/restore, including supervisor state. | `XSAVES mem` `XSAVES64 mem` | `NP 0F C7 /5` `NP REX.W 0F C7 /5` | Save processor extended state components specified by EDX:EAX to memory with compaction and optimization if possible. | 0 | Skylake, Goldmont, Zen 1, Shijidadao |
| `XRSTORS mem` `XRSTORS64 mem` | `NP 0F C7 /3` `NP REX.W 0F C7 /3` | Restore state components specified by EDX:EAX from memory. |   |   |   |

1. Under Intel APX, the `XSAVE*` and `XRSTOR*` instructions cannot be encoded with the REX2 prefix.
2. XSAVE was added in steppings E0/R0 of Penryn and is not available in earlier steppings.
3. On some processors (starting with Skylake, Goldmont, Zen 1 and Shijidadao v2), executing `XGETBV` with ECX=1 is permitted – this will not return `XCR1` (no such register exists) but instead return `XCR0` bitwise-ANDed with the current value of the "XINUSE" state-component bitmap (a bitmap of XSAVE state-components that are not known to be in their initial state). The presence of this functionality of `XGETBV` is indicated by CPUID.(EAX=0Dh,ECX=1):EAX[bit 2].
4. The `XSETBV` instruction will cause a mandatory #VMEXIT if executed under Intel VT-x virtualization.
5. XSAVEC and XSAVES were added in revision v2 of Zhaoxin Shijidadao and are not available in revision v1.

#### Added with other cross-vendor extensions
