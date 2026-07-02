---
title: "List of x86 instructions (part 4/5)"
source: https://en.wikipedia.org/wiki/X86_instruction_listings
domain: x86-assembly
license: CC-BY-SA-4.0
tags: x86 assembly, assembly language, x86, x86-64, amd64, asm
fetched: 2026-07-02
part: 4/5
---

# List of x86 instructions

| Instruction Set Extension | Instruction mnemonics | Opcode | Instruction description | Ring | Added in |
|---|---|---|---|---|---|
|   |   |   |   |   |   |
| *SSE*(non-SIMD) | `PREFETCHNTA m8` | `0F 18 /0` | Prefetch with Non-Temporal Access. Prefetch data under the assumption that the data will be used only once, and attempt to minimize cache pollution from said data. The methods used to minimize cache pollution are implementation-dependent. | 3 | Pentium III, (K7), (Geode GX2), Nehemiah, Efficeon |
| `PREFETCHT0 m8` | `0F 18 /1` | Prefetch data to all levels of the cache hierarchy. |   |   |   |
| `PREFETCHT1 m8` | `0F 18 /2` | Prefetch data to all levels of the cache hierarchy except L1 cache. |   |   |   |
| `PREFETCHT2 m8` | `0F 18 /3` | Prefetch data to all levels of the cache hierarchy except L1 and L2 caches. |   |   |   |
| `SFENCE` | `NP 0F AE F8+x` | Store Fence. |   |   |   |
|   |   |   |   |   |   |
| *SSE2*(non-SIMD) | `LFENCE` | `NP 0F AE E8+x` | Load Fence and Dispatch Serialization. | 3 | Pentium 4, Pentium M, K8, Efficeon, C7 Esther |
| `MFENCE` | `NP 0F AE F0+x` | Memory Fence. |   |   |   |
| `MOVNTI m32,r32` `MOVNTI m64,r64` | `NP 0F C3 /r` `NP REX.W 0F C3 /r` | Non-Temporal Memory Store. |   |   |   |
| `PAUSE` | `F3 90` | Pauses CPU thread for a short time period. Intended for use in spinlocks. |   |   |   |
|   |   |   |   |   |   |
| *CLFSH*Cache Line Flush. | `CLFLUSH m8` | `NP 0F AE /7` | Flush one cache line to memory. In a system with multiple cache hierarchy levels and/or multiple processors each with their own caches, the line is flushed from all of them. | 3 | (SSE2), Geode LX |
|   |   |   |   |   |   |
| *MONITOR*Monitor a memory location for memory writes. | `MONITOR` `MONITOR EAX,ECX,EDX` | `NP 0F 01 C8` | Start monitoring a memory location for memory writes. The memory address to monitor is given by DS:AX/EAX/RAX. ECX and EDX are reserved for extra extension and hint flags, respectively. | Usually 0 | Prescott, Yonah, Bonnell, K10, Nano |
| `MWAIT` `MWAIT EAX,ECX` | `NP 0F 01 C9` | Wait for a write to a monitored memory location previously specified with `MONITOR`. ECX and EAX are used to provide extra extension and hint flags, respectively. `MWAIT` hints are commonly used for CPU power management. |   |   |   |
|   |   |   |   |   |   |
| *SMX*Safer Mode Extensions. Load, authenticate and execute a digitally signed "Authenticated Code Module" as part of Intel Trusted Execution Technology. | `GETSEC` | `NP 0F 37` | Perform an SMX function. The leaf function to perform is given in EAX. Depending on leaf function, the instruction may take additional arguments in RBX, ECX and EDX. | Usually 0 | Conroe/Merom, WuDaoKou, Tremont |
|   |   |   |   |   |   |
| *RDTSCP*Read Time Stamp Counter and Processor ID. | `RDTSCP` | `0F 01 F9` | Read Time Stamp Counter and processor core ID. The TSC value is placed in EDX:EAX and the core ID in ECX. | Usually 3 | K8, Nehalem, Silvermont, Nano |
|   |   |   |   |   |   |
| *POPCNT*Population Count. | `POPCNT r16,r/m16` `POPCNT r32,r/m32` | `F3 0F B8 /r` | Count the number of bits that are set to 1 in its source argument. | 3 | K10, Nehalem, Nano 3000, Gracemont |
| `POPCNT r64,r/m64` | `F3 REX.W 0F B8 /r` |   |   |   |   |
|   |   |   |   |   |   |
| *SSE4.2*(non-SIMD) | `CRC32 r32,r/m8` | `F2 0F 38 F0 /r` | Accumulate CRC value using the CRC-32C (Castagnoli) polynomial 0x11EDC6F41 (normal form 0x1EDC6F41). This is the polynomial used in iSCSI. In contrast to the more popular one used in Ethernet, its parity is even, and it can thus detect any error with an odd number of changed bits. | 3 | Nehalem, Bulldozer, Jaguar, ZhangJiang |
| `CRC32 r32,r/m16` `CRC32 r32,r/m32` | `F2 0F 38 F1 /r` |   |   |   |   |
| `CRC32 r64,r/m64` | `F2 REX.W 0F 38 F1 /r` |   |   |   |   |
|   |   |   |   |   |   |
| *FSGSBASE*Read/write base address of FS and GS segments from user-mode. Available in 64-bit mode only. | `RDFSBASE r32` `RDFSBASE r64` | `F3 0F AE /0` `F3 REX.W 0F AE /0` | Read base address of FS: segment. | 3 | Ivy Bridge, Steamroller, Goldmont, ZhangJiang |
| `RDGSBASE r32` `RDGSBASE r64` | `F3 0F AE /1` `F3 REX.W 0F AE /1` | Read base address of GS: segment. |   |   |   |
| `WRFSBASE r32` `WRFSBASE r64` | `F3 0F AE /2` `F3 REX.W 0F AE /2` | Write base address of FS: segment. |   |   |   |
| `WRGSBASE r32` `WRGSBASE r64` | `F3 0F AE /3` `F3 REX.W 0F AE /3` | Write base address of GS: segment. |   |   |   |
|   |   |   |   |   |   |
| *MOVBE*Move to/from memory with byte order swap. | `MOVBE r16,m16` `MOVBE r32,m32` | `NFx 0F 38 F0 /r` | Load from memory to register with byte-order swap. | 3 | Bonnell, Haswell, Jaguar, Steamroller, ZhangJiang |
| `MOVBE r64,m64` | `NP REX.W 0F 38 F0 /r` |   |   |   |   |
| `MOVBE m16,r16` `MOVBE m32,r32` | `NFx 0F 38 F1 /r` | Store to memory from register with byte-order swap. |   |   |   |
| `MOVBE m64,r64` | `NP REX.W 0F 38 F1 /r` |   |   |   |   |
|   |   |   |   |   |   |
| *INVPCID*Invalidate TLB entries by Process-context identifier. | `INVPCID reg,m128` | `66 0F 38 82 /r` | Invalidate entries in TLB and paging-structure caches based on invalidation type in register and descriptor in m128. The descriptor contains a memory address and a PCID. Instruction is serializing on AMD but not Intel CPUs. | 0 | Haswell, ZhangJiang, Zen 3, Gracemont |
|   |   |   |   |   |   |
| *PREFETCHW*Cache-line prefetch with intent to write. | `PREFETCHW m8` | `0F 0D /1` | Prefetch cache line with intent to write. | 3 | K6-2, (Cedar Mill), Silvermont, Broadwell, ZhangJiang |
| `PREFETCH m8` | `0F 0D /0` | Prefetch cache line. |   |   |   |
|   |   |   |   |   |   |
| *ADX*Enhanced variants of add-with-carry. | `ADCX r32,r/m32` `ADCX r64,r/m64` | `66 0F 38 F6 /r` `66 REX.W 0F 38 F6 /r` | Add-with-carry. Differs from the older `ADC` instruction in that it leaves flags other than `EFLAGS.CF` unchanged. | 3 | Broadwell, Zen 1, ZhangJiang, Gracemont |
| `ADOX r32,r/m32` `ADOX r64,r/m64` | `F3 0F 38 F6 /r` `F3 REX.W 0F 38 F6 /r` | Add-with-carry, with the overflow-flag `EFLAGS.OF` serving as carry input and output, with other flags left unchanged. |   |   |   |
|   |   |   |   |   |   |
| *SMAP*Supervisor Mode Access Prevention. Repurposes the `EFLAGS.AC` (alignment check) flag to a flag that prevents access to user-mode memory while in ring 0, 1 or 2. | `CLAC` | `NP 0F 01 CA` | Clear `EFLAGS.AC`. | 0 | Broadwell, Goldmont, Zen 1, LuJiaZui |
| `STAC` | `NP 0F 01 CB` | Set `EFLAGS.AC`. |   |   |   |
|   |   |   |   |   |   |
| *CLFLUSHOPT*Optimized Cache Line Flush. | `CLFLUSHOPT m8` | `NFx 66 0F AE /7` | Flush cache line. Differs from the older `CLFLUSH` instruction in that it has more relaxed ordering rules with respect to memory stores and other cache line flushes, enabling improved performance. | 3 | Skylake, Goldmont, Zen 1 |
|   |   |   |   |   |   |
| *PREFETCHWT1*Cache-line prefetch into L2 cache with intent to write. | `PREFETCHWT1 m8` | `0F 0D /2` | Prefetch data with T1 locality hint (fetch into L2 cache, but not L1 cache) and intent-to-write hint. | 3 | Knights Landing, YongFeng |
|   |   |   |   |   |   |
| *PKU*Protection Keys for user pages. | `RDPKRU` | `NP 0F 01 EE` | Read User Page Key register into EAX. | 3 | Skylake-X, Comet Lake, Gracemont, Zen 3, LuJiaZui |
| `WRPKRU` | `NP 0F 01 EF` | Write data from EAX into User Page Key Register, and perform a Memory Fence. |   |   |   |
|   |   |   |   |   |   |
| *CLWB*Cache Line Writeback to memory. | `CLWB m8` | `NFx 66 0F AE /6` | Write one cache line back to memory without invalidating the cache line. | 3 | Skylake-X, Zen 2, Tiger Lake, Tremont |
|   |   |   |   |   |   |
| *RDPID*Read processor core ID. | `RDPID r32` | `F3 0F C7 /7` | Read processor core ID into register. | 3 | Goldmont Plus, Zen 2, Ice Lake, LuJiaZui |
|   |   |   |   |   |   |
| *MOVDIRI*Move to memory as Direct Store. | `MOVDIRI m32,r32` `MOVDIRI m64,r64` | `NP 0F 38 F9 /r` `NP REX.W 0F 38 F9 /r` | Store to memory using Direct Store (memory store that is not cached or write-combined with other stores). | 3 | Tiger Lake, Tremont, Zen 5 |
|   |   |   |   |   |   |
| *MOVDIR64B*Move 64 bytes as Direct Store. | `MOVDIR64B reg,m512` | `66 0F 38 F8 /r` | Move 64 bytes of data from m512 to address given by ES:reg. The 64-byte write is done atomically with Direct Store. | 3 | Tiger Lake, Tremont, Zen 5 |
|   |   |   |   |   |   |
| *WBNOINVD*Whole Cache Writeback without invalidate. | `WBNOINVD` | `F3 0F 09` | Write back all dirty cache lines to memory without invalidation. Instruction is serializing. | 0 | Zen 2, Ice Lake-SP |
|   |   |   |   |   |   |
| *PREFETCHI*Instruction prefetch. | `PREFETCHIT0 m8` | `0F 18 /7` | Prefetch code to all levels of the cache hierarchy. | 3 | Zen 5, Granite Rapids |
| `PREFETCHIT1 m8` | `0F 18 /6` | Prefetch code to all levels of the cache hierarchy except first-level cache. |   |   |   |

1. AMD Athlon processors prior to the Athlon XP did not support full SSE, but did introduce the non-SIMD instructions of SSE as part of "MMX Extensions". These extensions (without full SSE) are also present on Geode GX2 and later Geode processors.
2. All of the `PREFETCH*` instructions are hint instructions with effects only on performance, not program semantics. Providing an invalid address (e.g. address of an unmapped page or a non-canonical address) will cause the instruction to act as a NOP without any exceptions generated.
3. On Intel processors, as well as AMD64 processors, the processor ignores the r/m field of the ModR/M byte for the `SFENCE`, `LFENCE` and `MFENCE` instructions — any value of x in the range 0..7 will result in a valid instruction. (This is not known to be the case on other processors supporting these instructions, so it is recommended to encode them with x=0.)
4. The `SFENCE` instruction ensures that all memory stores after the `SFENCE` instruction are made globally observable after all memory stores before the `SFENCE`. This imposes ordering on stores that can otherwise be reordered, such as non-temporal stores and stores to WC (Write-Combining) memory regions. On Intel CPUs, as well as AMD CPUs from Zen1 onwards (but not older AMD CPUs), `SFENCE` also acts as a reordering barrier on cache flushes/writebacks performed with the `CLFLUSH`, `CLFLUSHOPT` and `CLWB` instructions. (Older AMD CPUs require `MFENCE` to order `CLFLUSH`.) `SFENCE` is not ordered with respect to `LFENCE`, and an `SFENCE+LFENCE` sequence is not sufficient to prevent a load from being reordered past a previous store. To prevent such reordering, it is necessary to execute an `MFENCE`, `LOCK` or a serializing instruction.
5. The `LFENCE` instruction ensures that all memory loads after the `LFENCE` instruction are made globally observable after all memory loads before the `LFENCE`. On all Intel CPUs that support SSE2, the `LFENCE` instruction provides a stronger ordering guarantee: it is *dispatch-serializing*, meaning that instructions after the `LFENCE` instruction are allowed to start executing only after all instructions before it have retired (which will ensure that all preceding loads but not necessarily stores have completed). The effect of dispatch-serialization is that `LFENCE` also acts as a speculation barrier and a reordering barrier for accesses to non-memory resources such as performance counters (accessed through e.g. `RDTSC` or `RDPMC`) and x2apic MSRs. On AMD CPUs, `LFENCE` is not necessarily dispatch-serializing by default – however, on all AMD CPUs that support any form of non-dispatch-serializing `LFENCE`, it can be made dispatch-serializing by setting bit 1 of MSR `C001_1029`.
6. The `MFENCE` instruction ensures that all memory loads, stores and cacheline-flushes after the `MFENCE` instruction are made globally observable after all memory loads, stores and cacheline-flushes before the `MFENCE`. On Intel CPUs, `MFENCE` is *not* dispatch-serializing, and therefore cannot be used on its own to enforce ordering on accesses to non-memory resources such as performance counters and x2apic MSRs. `MFENCE` is still ordered with respect to `LFENCE`, so if there is a need to enforce ordering between memory stores and subsequent non-memory accesses, then such an ordering can be obtained by issuing an `MFENCE` followed by an `LFENCE`. On AMD CPUs, `MFENCE` is serializing.
7. The operation of the `PAUSE` instruction in 64-bit mode is, unlike `NOP`, unaffected by the presence of the `REX.R` prefix. Neither `NOP` nor `PAUSE` are affected by the other bits of the `REX` prefix. A few examples of how opcode `90` interacts with various prefixes in 64-bit mode are:`90` is `NOP``41 90` is `XCHG R8D,EAX``4E 90` is `NOP``49 90` is `XCHG R8,RAX``F3 90` is `PAUSE``F3 41 90` is `PAUSE``F3 4F 90` is `PAUSE`
8. The actual length of the pause performed by the `PAUSE` instruction is implementation-dependent. On systems without SSE2, `PAUSE` will execute as NOP.
9. Under VT-x or AMD-V virtualization, executing `PAUSE` many times in a short time interval may cause a #VMEXIT. The number of `PAUSE` executions and interval length that can trigger #VMEXIT are platform-specific.
10. While the `CLFLUSH` instruction was introduced together with SSE2, it has its own CPUID flag and may be present on processors not otherwise implementing SSE2 and/or absent from processors that otherwise implement SSE2. (E.g. AMD Geode LX supports `CLFLUSH` but not SSE2.)
11. While the `MONITOR` and `MWAIT` instructions were introduced at the same time as SSE3, they have their own CPUID flag that needs to be checked separately from the SSE3 CPUID flag (e.g. Athlon 64 X2 and VIA C7 supported SSE3 but not MONITOR.)
12. For the `MONITOR` and `MWAIT` instructions, older Intel documentation lists instruction mnemonics with explicit operands (`MONITOR EAX,ECX,EDX` and `MWAIT EAX,ECX`), while newer documentation omits these operands. Assemblers/disassemblers may support one or both of these variants.
13. For `MONITOR`, the DS: segment can be overridden with a segment prefix. The memory area that will be monitored will be not just the single byte specified by DS:rAX, but a linear memory region containing the byte – the size and alignment of this memory region is implementation-dependent and can be queried through CPUID. The memory location to monitor should have memory type WB (write-back cacheable), or else monitoring may fail.
14. As of April 2024, no extensions or hints have been defined for the `MONITOR` instruction. As such, the instruction requires ECX=0 and ignores EDX.
15. On some processors, such as Intel Xeon Phi x200 and AMD K10 and later, there exist documented MSRs that can be used to enable `MONITOR` and `MWAIT` to run in Ring 3.
16. The wait performed by `MWAIT`may be ended by system events other than a memory write (e.g. cacheline evictions, interrupts) – the exact set of events that can cause the wait to end is implementation-specific. Regardless of whether the wait was ended by a memory write or some other event, monitoring will have ended and it will be necessary to set up monitoring again with `MONITOR` before using `MWAIT` to wait for memory writes again.
17. The extension flags available for `MWAIT` in the ECX register are: BitsMWAIT Extension 0Treat interrupts as break events, even when masked (EFLAGS.IF=0). (Available on all non-NetBurst implementations of `MWAIT`.) 1Timed MWAIT: end the wait when the TSC reaches or exceeds the value in EDX:EBX. (Undocumented, reportedly present in Intel Skylake and later Intel processors) 2Monitorless MWAIT 31:3Not used, must be set to zero.
18. The hint flags available for `MWAIT` in the EAX register are: BitsMWAIT Hint 3:0Sub-state within a C-state (see bits 7:4) (Intel processors only) 7:4Target CPU power C-state during wait, minus 1. (E.g. 0000b for C1, 0001b for C2, 1111b for C0) 31:8Not used. The C-states are processor-specific power states, which do not necessarily correspond 1:1 to ACPI C-states.
19. For the `GETSEC` instruction, the `REX.W` prefix enables 64-bit addresses for the EXITAC leaf function only - REX prefixes are otherwise permitted but ignored for the instruction.
20. The leaf functions defined for `GETSEC` (selected by EAX) are: EAXFunction 0 (CAPABILITIES)Report SMX capabilities 2 (ENTERACCES)Enter execution of authenticated code module 3 (EXITAC)Exit execution of authenticated code module 4 (SENTER)Enter measured environment 5 (SEXIT)Exit measured environment 6 (PARAMETERS)Report SMX parameters 7 (SMCTRL)SMX Mode Control 8 (WAKEUP)Wake up sleeping processors in measured environment Any unsupported value in EAX causes an #UD exception.
21. For `GETSEC`, most leaf functions are restricted to Ring 0, but the CAPABILITIES (EAX=0) and PARAMETERS (EAX=6) leaf functions are available in Ring 3.
22. The "core ID" value read by `RDTSCP` and `RDPID` is actually the `TSC_AUX` MSR (MSR `C000_0103h`). Whether this value actually corresponds to a processor ID is a matter of operating system convention.
23. Unlike the older `RDTSC` instruction, `RDTSCP` will delay the TSC read until all previous instructions have retired, guaranteeing ordering with respect to preceding memory loads (but not stores). `RDTSCP` is not ordered with respect to subsequent instructions, though.
24. `RDTSCP` can be run outside Ring 0 only if `CR4.TSD=0`.
25. Support for `RDTSCP` was added in stepping F of the AMD K8, and is not available on earlier steppings.
26. While the `POPCNT` instruction was introduced at the same time as SSE4.2, it is not considered to be a part of SSE4.2, but instead a separate extension with its own CPUID flag. On AMD processors, it is considered to be a part of the ABM extension, but still has its own CPUID flag.
27. For the `MOVBE` instruction, encodings that use both the `66h` prefix and the `REX.W` prefix will cause #UD on some processors (e.g. Haswell) and should therefore be avoided.
28. The invalidation types defined for `INVPCID` (selected by register argument) are: ValueFunction 0Invalidate TLB entries matching PCID and virtual memory address in descriptor, excluding global entries 1Invalidate TLB entries matching PCID in descriptor, excluding global entries 2Invalidate all TLB entries, including global entries 3Invalidate all TLB entries, excluding global entries Any unsupported value in the register argument causes a #GP exception.
29. Unlike the older `INVLPG` instruction, `INVPCID` will cause a #GP exception if the provided memory address is non-canonical. This discrepancy has been known to cause security issues.
30. The `PREFETCH` and `PREFETCHW` instructions are mandatory parts of the 3DNow! instruction set extension, but are also available as a standalone extension on systems that do not support 3DNow!
31. The opcodes for `PREFETCH` and `PREFETCHW` (`0F 0D /r`) execute as NOPs on Intel CPUs from Cedar Mill (65nm Pentium 4) onwards, with `PREFETCHW` gaining prefetch functionality from Broadwell onwards.
32. The `PREFETCH` (`0F 0D /0`) instruction is a 3DNow! instruction, present on all processors with 3DNow! but not necessarily on processors with the PREFETCHW extension. On AMD CPUs with PREFETCHW, opcode `0F 0D /0` as well as opcodes `0F 0D /2../7` are all documented to be performing prefetch. On Intel processors with PREFETCHW, these opcodes are documented as performing reserved-NOPs (except `0F 0D /2` being `PREFETCHWT1 m8` on Xeon Phi only) – third party testing indicates that some or all of these opcodes may be performing prefetch on at least some Intel Core CPUs.
33. The SMAP, PKU and RDPID instruction set extensions are supported on stepping 2 and later of Zhaoxin LuJiaZui, but not on earlier steppings.
34. Unlike the older `RDTSCP` instruction which can also be used to read the processor ID, user-mode `RDPID` is not disabled by `CR4.TSD=1`.
35. For `MOVDIR64`, the destination address given by ES:reg must be 64-byte aligned. The operand size for the register argument is given by the address size, which may be overridden by the `67h` prefix. The 64-byte memory source argument does not need to be 64-byte aligned, and is not guaranteed to be read atomically.
36. The `WBNOINVD` instruction will execute as `WBINVD` if run on a system that doesn't support the WBNOINVD extension. `WBINVD` differs from `WBNOINVD` in that `WBINVD` will invalidate all cache lines after writeback.
37. In initial implementations, the `PREFETCHIT0` and `PREFETCHIT1` instructions will perform code prefetch only when using the RIP-relative addressing mode and act as NOPs otherwise. The PREFETCHI instructions are hint instructions only - if an attempt is made to prefetch an invalid address, the instructions will act as NOPs with no exceptions generated. On processors that support Long-NOP but do not support the PREFETCHI instructions, these instructions will always act as NOPs.

#### Added with other Intel-specific extensions

| Instruction Set Extension | Instruction mnemonics | Opcode | Instruction description | Ring | Added in |
|---|---|---|---|---|---|
|   |   |   |   |   |   |
| *SSE2 branch hints*Instruction prefixes that can be used with the `Jcc` instructions to provide branch taken/not-taken hints. | `HWNT`, `hint-not-taken`, (`,pn`) | `2E` | Instruction prefix: branch hint weakly not taken. | 3 | Pentium 4, Meteor Lake |
| `HST`, `hint-taken`, (`,pt`) | `3E` | Instruction prefix: branch hint strongly taken. |   |   |   |
|   |   |   |   |   |   |
| *SGX*Software Guard Extensions. Set up an encrypted enclave in which a guest can execute code that a compromised or malicious host cannot inspect or tamper with. | `ENCLS` | `NP 0F 01 CF` | Perform an SGX Supervisor function. The function to perform is given in EAX — depending on function, the instruction may take additional input operands in RBX, RCX and RDX. Depending on function, the instruction may return data in RBX and/or an error code in EAX. | 0 | *SGX1*Skylake, Goldmont Plus*SGX2*Goldmont Plus, Ice Lake-SP*OVERSUB*(Ice Lake-SP), (Tremont), Ice Lake-U |
| `ENCLU` | `NP 0F 01 D7` | Perform an SGX User function. The function to perform is given in EAX — depending on function, the instruction may take additional input operands in RBX, RCX and RDX. Depending on function, the instruction may return data/status information in EAX and/or RCX. | 3 |   |   |
| `ENCLV` | `NP 0F 01 C0` | Perform an SGX Virtualization function. The function to perform is given in EAX — depending on function, the instruction may take additional input operands in RBX, RCX and RDX. Instruction returns status information in EAX. | 0 |   |   |
|   |   |   |   |   |   |
| *PTWRITE*Write data to a Processor Trace Packet. | `PTWRITE r/m32` `PTWRITE r/m64` | `F3 0F AE /4` `F3 REX.W 0F AE /4` | Read data from register or memory to encode into a PTW packet. | 3 | Kaby Lake, Goldmont Plus |
|   |   |   |   |   |   |
| *PCONFIG*Platform Configuration, including TME-MK ("Total Memory Encryption – Multi-Key") and TSE ("Total Storage Encryption"). | `PCONFIG` | `NP 0F 01 C5` | Perform a platform feature configuration function. The function to perform is specified in EAX - depending on function, the instruction may take additional input operands in RBX, RCX and RDX. If the instruction fails, it will set EFLAGS.ZF=1 and return an error code in EAX. If it is successful, it sets EFLAGS.ZF=0 and EAX=0. | 0 | Ice Lake-SP |
|   |   |   |   |   |   |
| *CLDEMOTE*Cache Line Demotion Hint. | `CLDEMOTE m8` | `NP 0F 1C /0` | Move cache line containing m8 from CPU L1 cache to a more distant level of the cache hierarchy. | 3 | (Tremont), (Alder Lake), Sapphire Rapids |
|   |   |   |   |   |   |
| *WAITPKG*User-mode memory monitoring and waiting. | `UMONITOR r16/32/64` | `F3 0F AE /6` | Start monitoring a memory location for memory writes. The memory address to monitor is given by the register argument. | 3 | Tremont, Alder Lake |
| `UMWAIT r32` `UMWAIT r32,EDX,EAX` | `F2 0F AE /6` | Timed wait for a write to a monitored memory location previously specified with `UMONITOR`. In the absence of a memory write, the wait will end when either the TSC reaches the value specified by EDX:EAX or the wait has been going on for an OS-controlled maximum amount of time. | Usually 3 |   |   |
| `TPAUSE r32` `TPAUSE r32,EDX,EAX` | `66 0F AE /6` | Wait until the Time Stamp Counter reaches the value specified in EDX:EAX. The register argument to the `UMWAIT` and `TPAUSE` instructions specifies extra flags to control the operation of the instruction. |   |   |   |
|   |   |   |   |   |   |
| *SERIALIZE*Instruction Execution Serialization. | `SERIALIZE` | `NP 0F 01 E8` | Serialize instruction fetch and execution. | 3 | Alder Lake |
|   |   |   |   |   |   |
| *HRESET*Processor History Reset. | `HRESET imm8` | `F3 0F 3A F0 C0 *ib*` | Request that the processor reset selected components of hardware-maintained prediction history. A bitmap of which components of the CPU's prediction history to reset is given in EAX (the imm8 argument is ignored). | 0 | Alder Lake |
|   |   |   |   |   |   |
| *IBHF*Indirect Branch History Fence. Available in 64-bit mode only. | `IBHF` | `F3 REX.W 0F 1E F8` | Indirect Branch History Fence. Executing `IBHF` prevents predicted targets of later indirect branches executed while BHI_DIS_S is enabled in CPL0, CPL1, or CPL2 from being selected based on branch history from branches executed prior to `IBHF`, other than RSB-based return predictions. | (0) | Alder Lake |
|   |   |   |   |   |   |
| *UINTR*User Interprocessor interrupt. Available in 64-bit mode only. | `SENDUIPI reg` | `F3 0F C7 /6` | Send Interprocessor User Interrupt. | 3 | Sapphire Rapids |
| `UIRET` | `F3 0F 01 EC` | User Interrupt Return. Pops RIP, RFLAGS and RSP off the stack, in that order. |   |   |   |
| `TESTUI` | `F3 0F 01 ED` | Test User Interrupt Flag. Copies UIF to EFLAGS.CF . |   |   |   |
| `CLUI` | `F3 0F 01 EE` | Clear User Interrupt Flag. |   |   |   |
| `STUI` | `F3 0F 01 EF` | Set User Interrupt Flag. |   |   |   |
|   |   |   |   |   |   |
| *ENQCMD*Enqueue Store.Part of Intel DSA (Data Streaming Accelerator Architecture). | `ENQCMD reg,m512` | `F2 0F 38 F8 /r` | Enqueue Command. Reads a 64-byte "command data" structure from memory (m512 argument) and writes atomically to a memory-mapped Enqueue Store device (register argument provides the memory address of this device, using ES segment and requiring 64-byte alignment.) Sets ZF=0 to indicate that device accepted the command, or ZF=1 to indicate that command was not accepted (e.g. queue full or the memory location was not an Enqueue Store device.) | 3 | Sapphire Rapids |
| `ENQCMDS reg,m512` | `F3 0F 38 F8 /r` | Enqueue Command Supervisor. Differs from `ENQCMD` in that it can place an arbitrary PASID (process address-space identifier) and a privilege-bit in the "command data" to enqueue. | 0 |   |   |
|   |   |   |   |   |   |
| *WRMSRNS*Non-serializing Write to Model-specific register. | `WRMSRNS` | `NP 0F 01 C6` | Write Model-specific register. The MSR to write is specified in ECX, and the data to write is given in EDX:EAX. The instruction differs from the older `WRMSR` instruction in that it is not serializing. | 0 | Sierra Forest |
|   |   |   |   |   |   |
| *MSRLIST*Read/write multiple Model-specific registers. Available in 64-bit mode only. | `RDMSRLIST` | `F2 0F 01 C6` | Read multiple MSRs. RSI points to a table of up to 64 MSR indexes to read (64 bits each), RDI points to a table of up to 64 data items that the MSR read-results will be written to (also 64 bits each), and RCX provides a 64-entry bitmap of which of the table entries to actually perform an MSR read for. | 0 | Sierra Forest |
| `WRMSRLIST` | `F3 0F 01 C6` | Write multiple MSRs. RSI points to a table of up to 64 MSR indexes to write (64 bits each), RDI points to a table of up to 64 data items to write into the MSRs (also 64 bits each), and RCX provides a 64-entry bitmap of which of the table entries to actually perform an MSR write for. The MSRs are written in table order.The instruction is not serializing. |   |   |   |
|   |   |   |   |   |   |
| *CMP*cc*XADD*Atomically perform a compare - and a fetch-and-add if the condition is met. Available in 64-bit mode only. | `CMPccXADD m32,r32,r32` `CMPccXADD m64,r64,r64` | `VEX.128.66.0F38.W0 E**x** /r` `VEX.128.66.0F38.W1 E**x** /r` | Read value from memory, then compare to first register operand. If the comparison passes, then add the second register operand to the memory value. The instruction as a whole is performed atomically. The operation of `CMPccXADD [mem],reg1,reg2` is:tmpmem := [mem] EFLAGS := CMP tmpmem, reg1 // sets EFLAGS like regular compare reg1 := tmpmem if (condition) [mem] := tmpmem + reg2 | 3 | Sierra Forest, Lunar Lake |
|   |   |   |   |   |   |
| *PBNDKB*Platform Bind Key to Binary Large Object.Part of Intel TSE (Total Storage Encryption), and available in 64-bit mode only. | `PBNDKB` | `NP 0F 01 C7` | Bind information to a platform by encrypting it with a platform-specific wrapping key. The instruction takes as input the addresses to two 256-byte-aligned "bind structures" in RBX and RCX, reads the structure pointed to by RBX and writes a modified structure to the address given in RCX. If the instruction fails, it will set EFLAGS.ZF=1 and return an error code in EAX. If it is successful, it sets EFLAGS.ZF=0 and EAX=0. | 0 | Lunar Lake |
|   |   |   |   |   |   |
| *FRED*Flexible Return and Event Delivery.Provides an interrupt/exception/system-call handling mechanism that does not use the Interrupt descriptor table. | `ERETS` | `F2 0F 01 CA` | Event Return To Supervisor.Return from FRED event handler for events/syscalls that occurred in Ring 0. | 0 | Panther Lake |
| `ERETU` | `F3 0F 01 CA` | Event Return To User.Return from FRED event handler for events/syscalls that occurred in Ring 3 — causes a transition from Ring 0 to Ring 3. |   |   |   |
| `LKGS r/m16` | `F2 0F 00 /6` | Load Kernel GS Base.Loads the `GS` segment register in the same manner as `MOV` to `GS`, except that the base address of the segment descriptor selected by the instruction's r/m16 argument is loaded into the `IA32_KERNEL_GS_BASE` MSR instead of into the `GS` segment descriptor cache. |   |   |   |

1. The branch hint mnemonics `HWNT` and `HST` are listed in early Willamette documentation only - later Intel documentation lists the branch hint prefixes without assigning them a mnemonic.Intel XED uses the mnemonics `hint-taken` and `hint-not-taken` for these branch hints.GNU Binutils 2.12 and later allows the SSE2 branch hints to be specified as a second argument to the `Jcc` assembly instructions: "`,pt`" for the predicted-taken prefix, and "`,pn`" for the predicted-not-taken prefix.
2. The `2E` and `3E` prefixes are interpreted as branch hints only when used with the `Jcc` conditional branch instructions (opcodes `70..7F` and `0F 80..8F`) - when used with other opcodes, they may take other meanings (e.g. for instructions with memory operands outside 64-bit mode, they will work as segment-override prefixes `CS:` and `DS:`, respectively). On processors that don't support branch hints, these prefixes are accepted but ignored when used with `Jcc`.
3. Branch hints are supported on all NetBurst (Pentium 4 family) processors - but not supported on any other known processor prior to their re-introduction in "Redwood Cove" CPUs, starting with "Meteor Lake" in 2023.
4. The leaf functions defined for `ENCLS` (selected by EAX) are: EAXFunction 0 (ECREATE)Create an enclave 1 (EADD)Add a page 2 (EINIT)Initialize an enclave 3 (EREMOVE)Remove a page from EPC (Enclave Page Cache) 4 (EDBGRD)Read data by debugger 5 (EDBGWR)Write data by debugger 6 (EEXTEND)Extend EPC page measurement 7 (ELDB)Load an EPC page as blocked 8 (ELDU)Load an EPC page as unblocked 9 (EBLOCK)Block an EPC page A (EPA)Add version array B (EWB)Writeback/invalidate EPC page C (ETRACK)Activate EBLOCK checks Added with SGX2 D (EAUG)Add page to initialized enclave E (EMODPTR)Restrict permissions of EPC page F (EMODT)Change type of EPC page Added with OVERSUB 10 (ERDINFO)Read EPC page type/status info 11 (ETRACKC)Activate EBLOCK checks 12 (ELDBC)Load EPC page as blocked with enhanced error reporting 13 (ELDUC)Load EPC page as unblocked with enhanced error reporting Other 18 (EUPDATESVN)Update SVN (Security Version Number) after live microcode update Any unsupported value in EAX causes a #GP exception.
5. SGX is deprecated on desktop/laptop processors from 11th generation (Rocket Lake, Tiger Lake) onwards, but continues to be available on Xeon-branded server parts.
6. Intel documentation lists Ice Lake-SP and Tremont as the processors in which SGX oversubscription was introduced. However, as of February 2026, no Ice Lake-SP or Tremont variants have been observed to have the SGX oversubscription extension CPUID feature bits set, while several have them cleared — the only processors to have been observed to have these feature bits set are some Ice Lake-U variants.
7. The leaf functions defined for `ENCLU` (selected by EAX) are: EAXFunction 0 (EREPORT)Create a cryptographic report 1 (EGETKEY)Create a cryptographic key 2 (EENTER)Enter an Enclave 3 (ERESUME)Re-enter an Enclave 4 (EEXIT)Exit an Enclave Added with SGX2 5 (EACCEPT)Accept changes to EPC page 6 (EMODPE)Extend EPC page permissions 7 (EACCEPTCOPY)Initialize pending page Added with TDX 8 (EVERIFYREPORT2)Verify a cryptographic report of a trust domain Added with AEX-Notify 9 (EDECCSSA)Decrement TCS.CSSA Added with 256BITSGX A (EREPORT2)Create a cryptographic report that contains SHA384 measurements B (EGETKEY256)Create a 256-bit cryptographic key Any unsupported value in EAX causes a #GP exception. The `EENTER` and `ERESUME` functions cannot be executed inside an SGX enclave – the other functions can only be executed inside an enclave.
8. `ENCLU` can only be executed in ring 3, not rings 0/1/2.
9. The leaf functions defined for `ENCLV` (selected by EAX) are: EAXFunction Added with OVERSUB 0 (EDECVIRTCHILD)Decrement VIRTCHILDCNT in SECS 1 (EINCVIRTCHILD)Increment VIRTCHILDCNT in SECS 2 (ESETCONTEXT)Set ENCLAVECONTEXT field in SECS Any unsupported value in EAX causes a #GP exception. The `ENCLV` instruction is only present on systems that support the EPC Oversubscription Extensions to SGX ("OVERSUB").
10. `ENCLV` is only available if Intel VMX operation is enabled with `VMXON`, and will produce #UD otherwise.
11. For `PTWRITE`, the write to the Processor Trace Packet will only happen if a set of enable-bits (the "TriggerEn", "ContextEn", "FilterEn" bits of the `RTIT_STATUS` MSR and the "PTWEn" bit of the `RTIT_CTL` MSR) are all set to 1. The `PTWRITE` instruction is indicated in the SDM to cause an #UD exception if the 66h instruction prefix is used, regardless of other prefixes.
12. The leaf functions defined for `PCONFIG` (selected by EAX) are: EAXFunction 0MKTME_KEY_PROGRAM: Program key and encryption mode to use with an TME-MK Key ID. Added with TSE 1TSE_KEY_PROGRAM: Direct key programming for TSE. 2TSE_KEY_PROGRAM_WRAPPED: Wrapped key programming for TSE. Any unsupported value in EAX causes a #GP(0) exception.
13. For `CLDEMOTE`, the cache level that it will demote a cache line to is implementation-dependent. Since the instruction is considered a hint, it will execute as a NOP without any exceptions if the provided memory address is invalid or not in the L1 cache. It may also execute as a NOP under other implementation-dependent circumstances as well. On systems that do not support the CLDEMOTE extension, it executes as a NOP.
14. Intel documentation lists Tremont and Alder Lake as the processors in which CLDEMOTE was introduced. However, as of May 2022, no Tremont or Alder Lake models have been observed to have the CPUID feature bit for CLDEMOTE set, while several of them have the CPUID bit cleared. As of April 2023, the CPUID feature bit for CLDEMOTE has been observed to be set for Sapphire Rapids.
15. For `UMONITOR`, the operand size of the address argument is given by the address size, which may be overridden by the `67h` prefix. The default segment used is DS:, which can be overridden with a segment prefix.
16. For the `UMWAIT` and `TPAUSE` instructions, the operating system can use the `IA32_UMWAIT_CONTROL` MSR to limit the maximum amount of time that a single `UMWAIT`/`TPAUSE` invocation is permitted to wait. The `UMWAIT` and `TPAUSE` instructions will set `RFLAGS.CF` to 1 if they reached the `IA32_UMWAIT_CONTROL`-defined time limit and 0 otherwise.
17. `TPAUSE` and `UMWAIT` can be run outside Ring 0 only if `CR4.TSD=0`.
18. For the register argument to the `UMWAIT` and `TPAUSE` instructions, the following flag bits are supported: BitsUsage 0Preferred optimization state. 0 = C0.2 (slower wakeup, improves performance of other SMT threads on same core) 1 = C0.1 (faster wakeup) 31:1(Reserved)
19. While serialization can be performed with older instructions such as e.g. `CPUID` and `IRET`, these instructions perform additional functions, causing side-effects and reduced performance when stand-alone instruction serialization is needed. (`CPUID` additionally has the issue that it causes a mandatory #VMEXIT when executed under virtualization, which causes a very large overhead.) The `SERIALIZE` instruction performs serialization only, avoiding these added costs.
20. A bitmap of CPU history components that can be reset through `HRESET` is provided by CPUID.(EAX=20h,ECX=0):EBX. As of July 2023, the following bits are defined: BitUsage 0Intel Thread Director history 31:1(Reserved)
21. The `IBHF` instruction is only effective in Ring 0. Executing the `IBHF` instruction in rings 1/2/3 is permitted, but will execute as a `NOP` with no branch history fence functionality.On processors that don't support IBHF, the instruction will execute as `NOP` regardless of ring.
22. The `IBHF` instruction was added to Alder Lake and later Intel processors with a microcode update in May 2025.
23. The register argument to `SENDUIPI` is an index to pick an entry from the UITT (User-Interrupt Target Table, a table specified by the new `UINTR_TT` and `UINT_MISC` MSRs.)
24. On Sapphire Rapids processors, the `UIRET` instruction always sets UIF (User Interrupt Flag) to 1. On Sierra Forest and later processors, `UIRET` will set UIF to the value of bit 1 of the value popped off the stack for RFLAGS - this functionality is indicated by `CPUID.(EAX=7,ECX=1):EDX[17]`.
25. For `ENQCMD` and `EMQCMDS`, the operand-size of the register argument is given by the current address-size, which can be overridden with the `67h` prefix.
26. For the `RDMSRLIST` and `WRMSRLIST` instructions, the addresses specified in the RSI and RDI registers must be 8-byte aligned.
27. The condition codes supported for the `CMP**cc**XADD` instructions (opcode `VEX.128.66.0F38 E**x** /r` with the **x** nibble specifying the condition) are: xccCondition (EFLAGS) 0OOF=1: "Overflow" 1NOOF=0: "Not Overflow" 2BCF=1: "Below" 3NBCF=0: "Not Below" 4ZZF=1: "Zero" 5NZZF=0: "Not Zero" 6BE(CF=1 or ZF=1): "Below or Equal" 7NBE(CF=0 and ZF=0): "Not Below or Equal" 8SSF=1: "Sign" 9NSSF=0: "Not Sign" APPF=1: "Parity" BNPPF=0: "Not Parity" CLSF≠OF: "Less" DNLSF=OF: "Not Less" ELE(ZF=1 or SF≠OF): "Less or Equal" FNLE(ZF=0 and SF=OF): "Not Less or Equal"
28. Even though the `CMPccXADD` instructions perform a locked memory operation, they do not require or accept the `LOCK` (`F0h`) prefix - attempting to use this prefix results in #UD.

#### Added with other AMD-specific extensions

| Instruction Set Extension | Instruction mnemonics | Opcode | Instruction description | Ring | Added in |
|---|---|---|---|---|---|
|   |   |   |   |   |   |
| *AltMovCr8*Alternative mechanism to access the CR8 control register. | `MOV reg,CR8` | `F0 0F 20 /0` | Read the CR8 register. | 0 | K8 |
| `MOV CR8,reg` | `F0 0F 22 /0` | Write to the CR8 register. |   |   |   |
|   |   |   |   |   |   |
| *MONITORX*Monitor a memory location for writes in user mode. | `MONITORX` | `NP 0F 01 FA` | Start monitoring a memory location for memory writes. Similar to older `MONITOR`, except available in user mode. | 3 | Excavator |
| `MWAITX` | `NP 0F 01 FB` | Wait for a write to a monitored memory location previously specified with `MONITORX`. `MWAITX` differs from the older `MWAIT` instruction mainly in that it runs in user mode and that it can accept an optional timeout argument (given in TSC time units) in EBX (enabled by setting bit[1] of ECX to 1.) |   |   |   |
|   |   |   |   |   |   |
| *CLZERO*Zero out full cache line. | `CLZERO rAX` | `NP 0F 01 FC` | Write zeroes to all bytes in a memory region that has the size and alignment of a CPU cache line and contains the byte addressed by DS:rAX. | 3 | Zen 1 |
|   |   |   |   |   |   |
| *RDPRU*Read processor register in user mode. | `RDPRU` | `NP 0F 01 FD` | Read selected MSRs (mainly performance counters) in user mode. ECX specifies which register to read. The value of the MSR is returned in EDX:EAX. | Usually 3 | Zen 2 |
|   |   |   |   |   |   |
| *MCOMMIT*Commit Stores To Memory. | `MCOMMIT` | `F3 0F 01 FA` | Ensure that all preceding stores in thread have been committed to memory, and that any errors encountered by these stores have been signalled to any associated error logging resources. The set of errors that can be reported and the logging mechanism are platform-specific. Sets `EFLAGS.CF` to 0 if any errors occurred, 1 otherwise. | 3 | Zen 2 |
|   |   |   |   |   |   |
| *INVLPGB*Invalidate TLB Entries with broadcast. | `INVLPGB` | `NP 0F 01 FE` | Invalidate TLB Entries for a range of pages, with broadcast. The invalidation is performed on the processor executing the instruction, and also broadcast to all other processors in the system. rAX takes the virtual address to invalidate and some additional flags, ECX takes the number of pages to invalidate, and EDX specifies ASID and PCID to perform TLB invalidation for. | 0 | Zen 3 |
| `TLBSYNC` | `NP 0F 01 FF` | Synchronize TLB invalidations. Wait until all TLB invalidations signalled by preceding invocations of the `INVLPGB` instruction on the same logical processor have been responded to by all processors in the system. Instruction is serializing. |   |   |   |

1. The standard way to access the CR8 register is to use an encoding that makes use of the `REX.R` prefix, e.g. `44 0F 20 07` (`MOV RDI,CR8`). However, the `REX.R` prefix is only available in 64-bit mode. The AltMovCr8 extension adds an additional method to access CR8, using the `F0` (`LOCK`) prefix instead of `REX.R` – this provides access to CR8 outside 64-bit mode.
2. Like other variants of MOV to/from the CRx registers, the AltMovCr8 encodings ignore the top 2 bits of the instruction's ModR/M byte, and always execute as if these two bits are set to `11b`. The AltMovCr8 encodings are available in 64-bit mode. However, combining the `LOCK` prefix with the `REX.R` prefix is not permitted and will cause an #UD exception.
3. Support for AltMovCR8 was added in stepping F of the AMD K8, and is not available on earlier steppings.
4. For `CLZERO`, the address size and 67h prefix control whether to use AX, EAX or RAX as address. The default segment DS: can be overridden by a segment-override prefix. The provided address does not need to be aligned – hardware will align it as necessary. The `CLZERO` instruction is intended for recovery from otherwise-fatal Machine Check errors. It is non-cacheable, cannot be used to allocate a cache line without a memory access, and should not be used for fast memory clears.
5. The register numbering used by `RDPRU` does not necessarily match that of `RDMSR`/`WRMSR`. The registers supported by `RDPRU` as of December 2022 are: ECXRegister 0MPERF (MSR 0E7h: Maximum Performance Frequency Clock Count) 1APERF (MSR 0E8h: Actual Performance Frequency Clock Count) Unsupported values in ECX return 0.
6. If `CR4.TSD=1`, then the `RDPRU` instruction can only run in ring 0.
