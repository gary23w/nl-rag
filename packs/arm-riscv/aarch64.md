---
title: "AArch64"
source: https://en.wikipedia.org/wiki/AArch64
domain: arm-riscv
license: CC-BY-SA-4.0
tags: arm architecture, aarch64, risc-v, riscv, cortex-m, instruction set
fetched: 2026-07-02
---

# AArch64

**AArch64**, also known as **ARM64**, is a 64-bit version of the ARM architecture family, a widely used set of computer processor designs. It was introduced in 2011 with the ARMv8 architecture and later became part of the ARMv9 series. AArch64 allows processors to handle more memory and perform faster calculations than earlier 32-bit versions. It is designed to work alongside the older 32-bit mode, known as AArch32, allowing compatibility with a wide range of software. Devices that use AArch64 include smartphones, tablets, personal computers, and servers. The AArch64 architecture has continued to evolve through updates that improve performance, security, and support for advanced computing tasks.

## AArch64 Execution state

In ARMv8-A, ARMv8-R, and ARMv9-A, an "Execution state" defines key characteristics of the processor’s environment. This includes the number of bits used in the primary processor registers, the supported instruction sets, and other aspects of the processor's execution environment. These versions of the ARM architecture support two Execution states: the 64-bit AArch64 state and the 32-bit AArch32 state.

### Naming conventions

- 64-bit:
  - Execution state: AArch64
  - Instruction sets: A64
- 32-bit:
  - Execution state: AArch32
  - Instruction sets: A32 + T32
  - Example: ARMv8-R, Cortex-A32

### AArch64 features

- New instruction set, A64:
  - Has 31 general-purpose 64-bit registers
  - Has dedicated zero or stack pointer (SP) register (depending on instruction)
  - The program counter (PC) is no longer directly accessible as a register
  - Instructions are still 32 bits long and mostly the same as A32 (with LDM/STM instructions and most conditional execution dropped)
    - Has paired loads/stores (in place of LDM/STM)
    - No predication for most instructions (except branches)
  - Most instructions can take 32-bit or 64-bit arguments
  - Addresses assumed to be 64-bit
- Advanced SIMD (Neon) enhanced:
  - Has 32 × 128-bit registers (up from 16), also accessible via VFPv4
  - Supports double-precision floating-point format
  - Fully IEEE 754 compliant
  - AES encrypt/decrypt and SHA-1/SHA-2 hashing instructions also use these registers
- A new exception system:
  - Fewer banked registers and modes
- Memory translation from 48-bit virtual addresses based on the existing Large Physical Address Extension (LPAE), which was designed to be easily extended to 64-bit

Extension: Data gathering hint (ARMv8.0-DGH).

AArch64 was introduced in ARMv8-A and is included in subsequent versions of ARMv8-A, and in all versions of ARMv9-A. It was also introduced in ARMv8-R as an option, after its introduction in ARMv8-A; it is not included in ARMv8-M.

#### A64 instruction formats

The main opcode for selecting which group an A64 instruction belongs to is at bits 25–28.

A64 instruction formats

Type

Bit

31

30

29

28

27

26

25

24

23

22

21

20

19

18

17

16

15

14

13

12

11

10

9

8

7

6

5

4

3

2

1

0

Reserved

0

op

0

0

0

0

0

op

1

SME

1

op

0

0

0

0

0

Varies

Unallocated

0

0

0

1

SVE

0

0

1

0

Varies

Unallocated

0

0

1

1

Data Processing — Immediate PC-rel.

op

imm

lo

1

0

0

0

0

imm

hi

Rd

Data Processing — Immediate Others

sf

1

0

0

01–11

Rd

Branches + System Instructions

op0

1

0

1

op1

op2

Load and Store Instructions

op0

1

op1

0

op2

op3

op4

Data Processing — Register

sf

op0

op1

1

0

1

op2

op3

Data Processing — Floating Point and SIMD

op0

1

1

1

op1

op2

op3

## ARM-A (application architecture)

Announced in October 2011, **ARMv8-A** represents a fundamental change to the ARM architecture. It adds an optional 64-bit Execution state, named "AArch64", and the associated new "A64" instruction set, in addition to a 32-bit Execution state, "AArch32", supporting the 32-bit "A32" (original 32-bit ARM) and "T32" (Thumb/Thumb-2) instruction sets. The latter instruction sets provide user-space compatibility with the existing 32-bit ARMv7-A architecture. ARMv8-A allows 32-bit applications to be executed in a 64-bit OS, and a 32-bit OS to be under the control of a 64-bit hypervisor. ARM announced their Cortex-A53 and Cortex-A57 cores on 30 October 2012. Apple was the first to release an ARMv8-A compatible core (Cyclone) in a consumer product (iPhone 5S). AppliedMicro, using an FPGA, was the first to demo ARMv8-A. The first ARMv8-A SoC from Samsung is the Exynos 5433 used in the Galaxy Note 4, which features two clusters of four Cortex-A57 and Cortex-A53 cores in a big.LITTLE configuration; but it only runs in AArch32 mode. ARMv8-A includes VFPv3/v4 and advanced SIMD (Neon) as standard features in both AArch32 and AArch64. It also adds cryptography instructions supporting AES, SHA-1/SHA-256 and finite field arithmetic.

An ARMv8-A processor can support one or both of AArch32 and AArch64; it may support AArch32 and AArch64 at lower Exception levels and only AArch64 at higher Exception levels. For example, the ARM Cortex-A32 supports only AArch32, the ARM Cortex-A34 supports only AArch64, and the ARM Cortex-A72 supports both AArch64 and AArch32. An ARMv9-A processor must support AArch64 at all Exception levels, and may support AArch32 at EL0.

### ARMv8.1-A

In December 2014, ARMv8.1-A, an update with "incremental benefits over v8.0", was announced. The enhancements fell into two categories: changes to the instruction set, and changes to the exception model and memory translation.

Instruction set enhancements included the following:

- A set of AArch64 atomic read-write instructions.
- Additions to the Advanced SIMD instruction set for both AArch32 and AArch64 to enable opportunities for some library optimizations:
  - Signed Saturating Rounding Doubling Multiply Accumulate, Returning High Half.
  - Signed Saturating Rounding Doubling Multiply Subtract, Returning High Half.
  - The instructions are added in vector and scalar forms.
- A set of AArch64 load and store instructions that can provide a memory access order that is limited to configurable address regions.
- The optional CRC instructions in v8.0 become a requirement in ARMv8.1.

Enhancements for the exception model and memory translation system included the following:

- A new Privileged Access Never (PAN) state bit provides control that prevents privileged access to user data unless explicitly enabled.
- An increased VMID range for virtualization; supports a larger number of virtual machines.
- Optional support for hardware update of the page table access flag, and the standardization of an optional, hardware updated, dirty bit mechanism.
- The Virtualization Host Extensions (VHE). These enhancements improve the performance of Type 2 hypervisors by reducing the software overhead associated when transitioning between the Host and Guest operating systems. The extensions allow the Host OS to execute at EL2, as opposed to EL1, without substantial modification.
- A mechanism to free up some translation table bits for operating system use, where the hardware support is not needed by the OS.
- Top byte ignore for memory tagging.

### ARMv8.2-A

ARMv8.2-A was announced in January 2016. Its enhancements fall into four categories:

- Optional half-precision floating-point data processing (half-precision was already supported, but not for processing, just as a storage format.)
- Memory model enhancements.
- Introduction of Reliability, Availability and Serviceability Extension (RAS Extension).
- Introduction of statistical profiling.

#### Scalable Vector Extension (SVE)

The Scalable Vector Extension (SVE) is licensed as "an optional extension to the ARMv8.2-A architecture and newer" developed specifically for vectorization of high-performance computing scientific workloads. The specification allows for ARM licensees to choose a hard-coded architectural register width between 128 and 2048 bits in multiples of 128. The extension is complementary to and does not replace the NEON extensions.

A 512-bit SVE variant has already been implemented on the Fugaku supercomputer using the Fujitsu A64FX ARM processor; this computer was the fastest supercomputer in the world for two years, from June 2020 to May 2022. A more flexible version, 2x256 SVE, was implemented by the AWS Graviton3 ARM processor.

SVE is supported by GCC, with GCC 8 supporting automatic vectorization and GCC 10 supporting C intrinsics. As of July 2020, LLVM and clang support C and IR intrinsics. ARM's own fork of LLVM supports auto-vectorization.

### ARMv8.3-A

In October 2016, ARMv8.3-A was announced. Its enhancements fell into six categories:

- Pointer authentication (PAC) (AArch64 only); mandatory extension (based on a new block cipher, QARMA) to the architecture (compilers need to exploit the security feature, but as the instructions are in NOP space, they are backwards compatible albeit providing no extra security on older chips).
- Nested virtualization (AArch64 only).
- Advanced SIMD complex number support (AArch64 and AArch32); e.g. rotations by multiples of 90 degrees.
- New FJCVTZS (Floating-point JavaScript Convert to Signed fixed-point, rounding toward Zero) instruction.
- A change to the memory consistency model (AArch64 only) to support the (non-default) weaker RCpc (Release Consistent processor consistent) model of C++11/C11 (the default C++11/C11 consistency model was already supported in previous ARMv8).
- ID mechanism support for larger system-visible caches (AArch64 and AArch32).

ARMv8.3-A architecture is now supported by (at least) GCC 7.0.

### ARMv8.4-A

In November 2017, ARMv8.4-A was announced. Its enhancements fell into these categories:

- "SHA3 / SHA512 / SM3 / SM4 crypto extensions", i.e. optional instructions.
- Improved virtualization support.
- Memory Partitioning and Monitoring (MPAM) capabilities.
- A new Secure EL2 state and Activity Monitors.
- Signed and unsigned integer dot product (SDOT and UDOT) instructions.

### ARMv8.5-A and ARMv9.0-A

In September 2018, ARMv8.5-A was announced. Its enhancements fell into these categories:

- Memory Tagging Extension (MTE) (AArch64).
- Branch Target Indicators (BTI) (AArch64) to reduce "the ability of an attacker to execute arbitrary code". Like pointer authentication, the relevant instructions are no-ops on earlier versions of ARMv8-A.
- Random Number Generator instructions – "providing Deterministic and True Random Numbers conforming to various National and International Standards".

On 2 August 2019, Google announced Android will adopt Memory Tagging Extension (MTE).

In March 2021, ARMv9-A was announced. ARMv9-A's baseline is all features from ARMv8.5. ARMv9-A also adds:

- Scalable Vector Extension 2 (SVE2). SVE2 builds on SVE's scalable vectorization for increased fine-grain Data Level Parallelism (DLP) to allow more work done per instruction. SVE2 aims are stated in marketing material to bring these benefits to a wider range of software including DSP and multimedia SIMD code that currently use NEON. LLVM/Clang 9.0 and GCC 10.0 were updated to support SVE2.
- Transactional Memory Extension (TME). Following the x86 extensions, TME brings support for Hardware Transactional Memory (HTM) and Transactional Lock Elision (TLE). TME aims to bring scalable concurrency to increase coarse-grained Thread Level Parallelism (TLP), to allow more work done per thread.LLVM/Clang 9.0 and GCC 10.0 were updated to support TME.
- Confidential Compute Architecture (CCA).

### ARMv8.6-A and ARMv9.1-A

In September 2019, ARMv8.6-A was announced. Its enhancements fell into these categories:

- General Matrix Multiply (GEMM).
- Bfloat16 format support.
- SIMD matrix manipulation instructions (added to NEON):
  - BFDOT* (BFloat16 dot product)
  - BFMMLA (BFloat16 matrix multiply and accumulate)
  - BFMLAL* (BFloat16 multiply and accumulate, widening to long)
  - BFCVT* (BFloat16 conversion)
- Enhancements for virtualization, system management and security.
- And the following extensions (that LLVM 11 already added support for):
  - Enhanced Counter Virtualization (ARMv8.6-ECV).
  - Fine-Grained Traps (ARMv8.6-FGT).
  - Activity Monitors virtualization (ARMv8.6-AMU).

For example, fine-grained traps, Wait-for-Event (WFE) instructions, EnhancedPAC2 and FPAC. The bfloat16 extensions for SVE and Neon are mainly for deep learning use.

### ARMv8.7-A and ARMv9.2-A

In September 2020, ARMv8.7-A was announced. Its enhancements fell into these categories:

- Scalable Matrix Extension (SME)(ARMv9.2 only). SME adds new features to process matrices efficiently, such as:
  - Matrix tile storage.
  - On-the-fly matrix transposition.
  - Load/store/insert/extract tile vectors.
  - Matrix outer product of SVE vectors.
  - "Streaming mode" SVE.
- Enhanced support for PCIe hot plug (AArch64).
- Atomic 64-byte load and stores to accelerators (AArch64).
- Wait For Interrupt (WFI) and Wait For Event (WFE) with timeout (AArch64).
- Branch-Record recording (ARMv9.2 only).
- Call Stack Recorder

### ARMv8.8-A and ARMv9.3-A

In September 2021, ARMv8.8-A and ARMv9.3-A were announced. Their enhancements fell into these categories:

- Non-maskable interrupts (AArch64).
- Instructions to optimize memcpy() and memset() style operations (AArch64).
- Enhancements to PAC (AArch64).
- Hinted conditional branches (AArch64).

LLVM 15 supports ARMv8.8-A and ARMv9.3-A.

### ARMv8.9-A and ARMv9.4-A

In September 2022, ARMv8.9-A and ARMv9.4-A were announced, including:

- Virtual Memory System Architecture (VMSA) enhancements.
  - Permission indirection and overlays.
  - Translation hardening.
  - 128-bit translation tables (ARMv9 only).
- Scalable Matrix Extension 2 (SME2) (ARMv9 only).
  - Multi-vector instructions.
  - Multi-vector predicates.
  - 2b/4b weight compression.
  - 1b binary networks.
  - Range Prefetch.
- Guarded Control Stack (GCS) (ARMv9 only).
- Confidential computing.
  - Memory encryption contexts.
  - Device assignment.

### ARMv9.5-A

In October 2023, ARMv9.5-A was announced, including:

- FP8 support (E5M2 and E4M3 formats) added to:
  - SME2
  - SVE2
  - Advanced SIMD (Neon)
- Live migration of virtual machines using hardware dirty state tracking structures (FEAT_HDBSS)
- Checked point arithmetic
- Support for using a combination of the PC and SP as the modifier when generating or checking Pointer Authentication codes.
- Support for Realm Management Extension (RME) enabled designs, support for non-secure only in the Granule Protection Tables and the ability to disable certain Physical Address Spaces (PAS).
- EL3 configuration write-traps.
- Breakpoint support for address range and mismatch triggering without the need for linking.
- Support for efficiently delegating SErrors from EL3 to EL2 or EL1.

### ARMv9.6-A

In October 2024, ARMv9.6-A was announced, including:

- Improved SME efficiency with structured sparsity and quarter tile operations
- MPAM domains to better support shared-memory computer systems on multi-chiplet and multi-chip systems
- Hypervisor memory control for trace and statistical profiling on virtual machines
- Improved caching and data placement
- Granular data isolation for confidential compute
- Bitwise locking of EL1 system registers
- Improved scaling of Granular Protection Tables (GPT) for large memory systems
- New SVE instructions for expand/compact and finding first/last active element
- Additional unprivileged load and store instructions to enable OS to interact with application memory (LDL(U)R* and STL(U)R*)
- Injection of undefined-instruction exceptions from EL3

### ARMv9.7-A

In October 2025, ARMv9.7-A was announced, including:

- Targeted memory invalidation broadcasts
- Flexible resource management (MPAMv2)
- 6-bit data types for artificial intelligence
- Video codecs
- GICv5

## ARM-R (real-time architecture)

Optional AArch64 support was added to the Armv8-R profile, with the first Arm core implementing it being the Cortex-R82. It adds the A64 instruction set, with some changes to the memory barrier instructions.
