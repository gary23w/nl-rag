---
title: "ARM Cortex-M"
source: https://en.wikipedia.org/wiki/ARM_Cortex-M
domain: arm-riscv
license: CC-BY-SA-4.0
tags: arm architecture, aarch64, risc-v, riscv, cortex-m, instruction set
fetched: 2026-07-02
---

# ARM Cortex-M

The **ARM Cortex-M** is a group of 32-bit RISC ARM processor cores licensed by ARM Limited. These cores are optimized for low-cost and energy-efficient integrated circuits, which have been embedded in tens of billions of consumer devices. Though they are most often the main component of microcontroller chips, sometimes they are embedded inside other types of chips too. The Cortex-M family consists of Cortex-M0, Cortex-M0+, Cortex-M1, Cortex-M3, Cortex-M4, Cortex-M7, Cortex-M23, Cortex-M33, Cortex-M35P, Cortex-M52, Cortex-M55, Cortex-M85. A floating-point unit (FPU) option is available for Cortex-M4 / M7 / M33 / M35P / M52 / M55 / M85 cores, and when included in the silicon these cores are sometimes known as "Cortex-MxF", where 'x' is the core variant.

## Overview

| 32-bit |   |
|---|---|
| Year | Core |
| 2004 | Cortex-M3 |
| 2007 | Cortex-M1 |
| 2009 | Cortex-M0 |
| 2010 | Cortex-M4 |
| 2012 | Cortex-M0+ |
| 2014 | Cortex-M7 |
| 2016 | Cortex-M23 |
| 2016 | Cortex-M33 |
| 2018 | Cortex-M35P |
| 2020 | Cortex-M55 |
| 2022 | Cortex-M85 |
| 2023 | Cortex-M52 |

The ARM Cortex-M family are ARM microprocessor cores that are designed for use in microcontrollers, ASICs, ASSPs, FPGAs, and SoCs. Cortex-M cores are commonly used as dedicated microcontroller chips, but also are "hidden" inside of SoC chips as power management controllers, I/O controllers, system controllers, touch screen controllers, smart battery controllers, and sensor controllers.

The main difference from Cortex-A cores is that Cortex-M cores have no memory management unit (MMU) for virtual memory, considered essential for "full-fledged" operating systems. Cortex-M programs instead run bare metal or on one of the many real-time operating systems which support a Cortex-M.

Though 8-bit microcontrollers were very popular in the past, Cortex-M has slowly been chipping away at the 8-bit market as the prices of low-end Cortex-M chips have moved downward. Cortex-M have become a popular replacements for 8-bit chips in applications that benefit from 32-bit math operations, and replacing older legacy ARM cores such as ARM7 and ARM9.

In particular, the embedded wear-leveling controller inside most SD cards or flash drives is a (8-bit) 8051 microcontroller or ARM CPU.

### License

ARM Limited neither manufactures nor sells CPU devices based on its own designs, but rather licenses the processor architecture to interested parties. Arm offers a variety of licensing terms, varying in cost and deliverables. To all licensees, Arm provides an integratable hardware description of the ARM core, as well as complete software development toolset and the right to sell manufactured silicon containing the ARM CPU.

### Silicon customization

Integrated Device Manufacturers (IDM) receive the ARM Processor IP as synthesizable RTL (written in Verilog). In this form, they have the ability to perform architectural level optimizations and extensions. This allows the manufacturer to achieve custom design goals, such as higher clock speed, very low power consumption, instruction set extensions (including floating point), optimizations for size, debug support, etc. To determine which components have been included in a particular ARM CPU chip, consult the manufacturer datasheet and related documentation.

Some of the silicon options for the Cortex-M cores are:

- SysTick timer: A 24-bit system timer that extends the functionality of both the processor and the Nested Vectored Interrupt Controller (NVIC). When present, it also provides an additional configurable priority SysTick interrupt. Though the SysTick timer is optional for the M0/M0+/M1/M23, it is extremely rare to find a Cortex-M microcontroller without it. If a Cortex-M33/M35P/M52/M55/M85 microcontroller has the Security Extension option, then it optionally can have two SysTicks (one Secure, one Non-secure).
- Bit-Band: Maps a complete word of memory onto a single bit in the bit-band region. For example, writing to an alias word will set or clear the corresponding bit in the bit-band region. This allows every individual bit in the bit-band region to be directly accessible from a word-aligned address. In particular, individual bits can be set, cleared, or toggled from C/C++ without performing a read-modify-write sequence of instructions. Though the bit-band is optional, it is less common to find a Cortex-M3 and Cortex-M4 microcontroller without it. Some Cortex-M0 and Cortex-M0+ microcontrollers have bit-band.
- Memory Protection Unit (MPU): Provides support for protecting regions of memory through enforcing privilege and access rules. It supports up to sixteen different regions, each of which can be split further into equal-size sub-regions.
- Tightly-Coupled Memory (TCM): Low-latency (zero wait state) SRAM that can be used to hold the call stack, RTOS control structures, interrupt data structures, interrupt handler code, and speed critical code. Other than CPU cache, TCM is the fastest memory in an ARM Cortex-M microcontroller. Since TCM isn't cached and accessible at the same speed as the processor and cache, it could be conceptually described as "addressable cache". There is an ITCM (Instruction TCM) and a DTCM (Data TCM) to allow a Harvard architecture processor to read from both simultaneously. The DTCM can't contain any instructions, but the ITCM can contain data. Since TCM is tightly connected to the processor core, DMA engines might not be able to access TCM on some implementations.

ARM Cortex-M optional components

ARM Core

Cortex

M0

Cortex

M0+

Cortex

M1

Cortex

M3

Cortex

M4

Cortex

M7

Cortex

M23

Cortex

M33

Cortex

M35P

Cortex

M52

Cortex

M55

Cortex

M85

SysTick 24-bit

Timer

Optional

(0,1)

Optional

(0, 1)

Optional

(0,1)

Yes

(1)

Yes

(1)

Yes

(1)

Optional

(0, 1, 2)

Yes

(1, 2)

Yes

(1, 2)

Yes

(1, 2)

Yes

(1, 2)

Yes

(1, 2)

Single-cycle I/O port

No

Optional

No

No

No

No

Optional

No

No

No

No

No

Bit-Band memory

No

No

No*

Optional

Optional

Optional

No

No

No

No

No

No

Memory Protection

Unit (

MPU

)

No

Optional

(0, 8)

No

Optional

(0,8)

Optional

(0, 8)

Optional

(0, 8, 16)

Optional

(0, 4, 8, 12, 16)

Optional

(0, 4, 8, 12, 16)

Optional

(up to 16)*

Optional

(0, 4, 8, 12, 16)

Optional

(0, 4, 8, 12, 16)

Optional

(0, 4, 8, 12, 16)

Security

Attribution

Unit (SAU) and

Stack Limits

No

No

No

No

No

No

Optional

(0, 4, 8)

Optional

(0, 4, 8)

Optional

(up to 8)*

Optional

(0, 4, 8)

Optional

(0, 4, 8)

Optional

(0, 4, 8)

Instruction Cache

No

No

No

No

No

Optional

(up to 64 KB)

No

No

Optional

(up to 16 KB)

Optional

(up to 64 KB)

Optional

(up to 64 KB)

Optional

(up to 64 KB)

Data Cache

No

No

No

No

No

Optional

(up to 64 KB)

No

No

No

Optional

(up to 64 KB)

Optional

(up to 64 KB)

Optional

(up to 64 KB)

Instruction TCM

(ITCM) Memory

No

No

Optional

(up to 1 MB)

No

No

Optional

(up to 16 MB)

No

No

No

Optional

(up to 16 MB)

Optional

(up to 16 MB)

Optional

(up to 16 MB)

Data TCM

(DTCM) Memory

No

No

Optional

(up to 1 MB)

No

No

Optional

(up to 16 MB)

No

No

No

Optional

(up to 16 MB)

Optional

(up to 16 MB)

Optional

(up to 16 MB)

ECC

for TCM

and Cache

No

No

No

No

No

No

No

No

Optional

Optional

Optional

Optional

Vector Table

Offset

Register (VTOR)

No

Optional

(0,1)

Optional

(0,1)

Optional

(0,1)

Optional

(0,1)

Optional

(0,1)

Optional

(0,1,2)

Yes

(1,2)

Yes

(1,2)

Yes

(1,2)

Yes

(1,2)

Yes

(1,2)

- Note: Most Cortex-M3 and M4 chips have bit-band and MPU. The bit-band option can be added to the M0/M0+ using the Cortex-M System Design Kit.
- Note: Software should validate the existence of each feature before attempting to use it.
- Note: Limited public information is available for the Cortex-M35P until its *Technical Reference Manual* is released.

*Additional silicon options:*

- Data endianness: Little-endian or big-endian. Unlike legacy ARM cores, the Cortex-M is permanently fixed in silicon as one of these choices.
- Interrupts: 1 to 32 (M0/M0+/M1), 1 to 240 (M3/M4/M7/M23), 1 to 480 (M33/M35P/M52/M55/M85).
- Wake-up interrupt controller: Optional.
- Vector Table Offset Register: Optional. (not available for M0).
- Instruction fetch width: 16-bit only, or mostly 32-bit.
- User/privilege support: Optional.
- Reset all registers: Optional.
- Single-cycle I/O port: Optional. (M0+/M23).
- Debug Access Port (DAP): None, SWD, JTAG and SWD. (optional for all Cortex-M cores)
- Halting debug support: Optional.
- Number of watchpoint comparators: 0 to 2 (M0/M0+/M1), 0 to 4 (M3/M4/M7/M23/M33/M35P/M52/M55/M85).
- Number of breakpoint comparators: 0 to 4 (M0/M0+/M1/M23), 0 to 8 (M3/M4/M7/M33/M35P/M52/M55/M85).

### Instruction sets

The Cortex-M0 / M0+ / M1 implement the **ARMv6-M** architecture, the Cortex-M3 implements the **ARMv7-M** architecture, the Cortex-M4 / Cortex-M7 implements the **ARMv7E-M** architecture, the Cortex-M23 / M33 / M35P implement the **ARMv8-M** architecture, and the Cortex-M52 / M55 / M85 implements the **ARMv8.1-M** architecture. The architectures are binary instruction upward compatible from ARMv6-M to ARMv7-M to ARMv7E-M. Binary instructions available for the Cortex-M0 / Cortex-M0+ / Cortex-M1 can execute without modification on the Cortex-M3 / Cortex-M4 / Cortex-M7. Binary instructions available for the Cortex-M3 can execute without modification on the Cortex-M4 / Cortex-M7 / Cortex-M33 / Cortex-M35P. Only Thumb-1 and Thumb-2 instruction sets are supported in Cortex-M architectures; the legacy 32-bit ARM instruction set isn't supported.

All Cortex-M cores implement a common subset of instructions that consists of most Thumb-1, some Thumb-2, including a 32-bit result multiply. The Cortex-M0 / Cortex-M0+ / Cortex-M1 / Cortex-M23 were designed to create the smallest silicon die, thus having the fewest instructions of the Cortex-M family.

The Cortex-M0 / M0+ / M1 include Thumb-1 instructions, except new instructions (CBZ, CBNZ, IT) which were added in ARMv7-M architecture. The Cortex-M0 / M0+ / M1 include a minor subset of Thumb-2 instructions (BL, DMB, DSB, ISB, MRS, MSR). The Cortex-M3 / M4 / M7 / M33 / M35P have all base Thumb-1 and Thumb-2 instructions. The Cortex-M3 adds three Thumb-1 instructions, all Thumb-2 instructions, hardware integer divide, and saturation arithmetic instructions. The Cortex-M4 adds DSP instructions and an optional single-precision floating-point unit (VFPv4-SP). The Cortex-M7 adds an optional double-precision FPU (VFPv5). The Cortex-M23 / M33 / M35P / M52 / M55 / M85 add TrustZone instructions.

ARM Cortex-M instruction variations

Arm Core

Cortex

M0

Cortex

M0+

Cortex

M1

Cortex

M3

Cortex

M4

Cortex

M7

Cortex

M23

Cortex

M33

Cortex

M35P

Cortex

M52

Cortex

M55

Cortex

M85

ARM architecture

ARMv6-M

ARMv6-M

ARMv6-M

ARMv7-M

ARMv7E-M

ARMv7E-M

ARMv8-M

Baseline

ARMv8-M

Mainline

ARMv8-M

Mainline

Armv8.1-M

Mainline

Armv8.1-M

Mainline

Armv8.1-M

Mainline

Computer architecture

Von

Neumann

Von

Neumann

Von

Neumann

Harvard

Harvard

Harvard

Von

Neumann

Harvard

Harvard

Harvard

Harvard

Harvard

Instruction pipeline

3 stages

2 stages

3 stages

3 stages

3 stages

6 stages

2 stages

3 stages

3 stages

4 stages

4-5 stages

7 stages

Interrupt latency

(zero

wait state

memory)

16 cycles

15 cycles

23 for NMI,

26 for IRQ

12 cycles

12 cycles

12 cycles,

14 worst

case

15 cycles,

24 secure

to NS IRQ

12 cycles,

21 secure

to NS IRQ

TBD

TBD

TBD

TBD

Thumb-1

instructions

Most

Most

Most

Entire

Entire

Entire

Most

Entire

Entire

Entire

Entire

Entire

Thumb-2

instructions

Some

Some

Some

Entire

Entire

Entire

Some

Entire

Entire

Entire

Entire

Entire

Multiply

instructions

32×32 = 32-bit result

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Multiply instructions

32×32 = 64-bit result

No

No

No

Yes

Yes

Yes

No

Yes

Yes

Yes

Yes

Yes

Divide

instructions

32/32 = 32-bit quotient

No

No

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Saturated

math instructions

No

No

No

Some

Yes

Yes

No

Yes

Yes

Yes

Yes

Yes

DSP

instructions

No

No

No

No

Yes

Yes

No

Optional

Optional

Yes

Yes

Yes

Half-Precision

(HP)

floating-point

instructions

No

No

No

No

No

No

No

No

No

Optional

Optional

Optional

Single-Precision

(SP)

floating-point instructions

No

No

No

No

Optional

Optional

No

Optional

Optional

Optional

Optional

Optional

Double-Precision

(DP)

floating-point instructions

No

No

No

No

No

Optional

No

No

No

Optional

Optional

Optional

Helium vector instructions

No

No

No

No

No

No

No

No

No

Optional

Optional

Optional

TrustZone

security instructions

No

No

No

No

No

No

Optional

Optional

Optional

Optional

Optional

Yes

Co-processor

instructions

No

No

No

No

No

No

No

Optional

Optional

Optional

Optional

Optional

ARM Custom Instructions (ACI)

No

No

No

No

No

No

No

Optional

No

Optional

Optional

Optional

Pointer Authentication and Branch Target

Identification (PACBTI) instructions

No

No

No

No

No

No

No

No

No

Optional

No

Optional

- Note: Interrupt latency cycle count assumes: 1) stack located in zero-wait state RAM, 2) another interrupt function not currently executing, 3) Security Extension option doesn't exist, because it adds additional cycles. The Cortex-M cores with a Harvard computer architecture have a shorter interrupt latency than Cortex-M cores with a Von Neumann computer architecture.
- Note: The Cortex-M series includes three new 16-bit **Thumb-1** instructions for sleep mode: SEV, WFE, WFI.
- Note: The Cortex-M0 / M0+ / M1 doesn't include these 16-bit **Thumb-1** instructions: CBZ, CBNZ, IT.
- Note: The Cortex-M0 / M0+ / M1 only include these 32-bit **Thumb-2** instructions: BL, DMB, DSB, ISB, MRS, MSR.
- Note: The Cortex-M0 / M0+ / M1 / M23 only has 32-bit **multiply** instructions with a lower-32-bit result (32 bit × 32 bit = lower 32 bit), where as the Cortex-M3 / M4 / M7 / M33 / M35P includes additional 32-bit multiply instructions with 64-bit results (32 bit × 32 bit = 64 bit). The Cortex-M4 / M7 (optionally M33 / M35P) include DSP instructions for (16 bit × 16 bit = 32 bit), (32 bit × 16 bit = upper 32 bit), (32 bit × 32 bit = upper 32 bit) multiplications.
- Note: The number of cycles to complete multiply and divide instructions vary across ARM Cortex-M core designs. Some cores have a silicon option for the choice of fast speed or small size (slow speed), so cores have the option of using less silicon with the downside of higher cycle count. An interrupt occurring during the execution of a divide instruction or slow-iterative multiply instruction will cause the processor to abandon the instruction, then restart it after the interrupt returns.
  - Multiply instructions "32-bit result" – Cortex-M0/M0+/M23 is 1 or 32 cycle silicon option, Cortex-M1 is 3 or 33 cycle silicon option, Cortex-M3/M4/M7/M33/M35P is 1 cycle.
  - Multiply instructions "64-bit result" – Cortex-M3 is 3–5 cycles (depending on values), Cortex-M4/M7/M33/M35P is 1 cycle.
  - Divide instructions – Cortex-M3/M4 is 2–12 cycles (depending on values), Cortex-M7 is 3–20 cycles (depending on values), Cortex-M23 is 17 or 34 cycle option, Cortex-M33 is 2–11 cycles (depending on values), Cortex-M35P is TBD.
- Note: Some Cortex-M cores have silicon options for various types of floating point units (**FPU**). The Cortex-M55 / M85 has an option for half-precision (**HP**), the Cortex-M4 / M7 / M33 / M35P / M52 / M55 / M85 has an option for single-precision (**SP**), the Cortex-M7 / M52 / M55 / M85 has an option for double-precision (**DP**). When an FPU is included, the core is sometimes referred as "Cortex-MxF", where 'x' is the core variant, such as Cortex-M4**F**.

ARM Cortex-M instruction groups

Group

Instr

bits

Instructions

Cortex

M0, M0+, M1

Cortex

M3

Cortex

M4

Cortex

M7

Cortex

M23

Cortex

M33

Cortex

M35P

Cortex

M52

Cortex

M55

Cortex

M85

Thumb-1

16

ADC, ADD, ADR, AND, ASR, B, BIC, BKPT, BLX, BX, CMN, CMP, CPS, EOR, LDM, LDR, LDRB, LDRH, LDRSB, LDRSH, LSL, LSR, MOV, MUL, MVN, NOP, ORR, POP, PUSH, REV, REV16, REVSH, ROR, RSB, SBC, SEV, STM, STR, STRB, STRH, SUB, SVC, SXTB, SXTH, TST, UXTB, UXTH, WFE, WFI, YIELD

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Thumb-1

16

CBNZ, CBZ

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Thumb-1

16

IT

No

Yes

Yes

Yes

No

Yes

Yes

Yes

Yes

Yes

Thumb-2

32

BL, DMB, DSB, ISB, MRS, MSR

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Thumb-2

32

SDIV, UDIV, MOVT, MOVW, B.W, LDREX, LDREXB, LDREXH, STREX, STREXB, STREXH

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Thumb-2

32

ADC, ADD, ADR, AND, ASR, B, BFC, BFI, BIC, CDP, CLREX,

CLZ

, CMN, CMP, DBG, EOR, LDC, LDM, LDR, LDRB, LDRBT, LDRD, LDRH, LDRHT, LDRSB, LDRSBT, LDRSH, LDRSHT, LDRT, LSL, LSR, MCR, MCRR, MLA, MLS, MRC, MRRC, MUL, MVN, NOP, ORN, ORR, PLD, PLDW, PLI, POP, PUSH, RBIT, REV, REV16, REVSH, ROR, RRX, RSB, SBC, SBFX, SEV, SMLAL, SMULL, SSAT, STC, STM, STR, STRB, STRBT, STRD, STRH, STRHT, STRT, SUB, SXTB, SXTH, TBB, TBH, TEQ, TST, UBFX, UMLAL, UMULL, USAT, UXTB, UXTH, WFE, WFI, YIELD

No

Yes

Yes

Yes

No

Yes

Yes

Yes

Yes

Yes

DSP

32

PKH, QADD, QADD16, QADD8, QASX, QDADD, QDSUB, QSAX, QSUB, QSUB16, QSUB8, SADD16, SADD8, SASX, SEL, SHADD16, SHADD8, SHASX, SHSAX, SHSUB16, SHSUB8, SMLABB, SMLABT, SMLATB, SMLATT, SMLAD, SMLALBB, SMLALBT, SMLALTB, SMLALTT, SMLALD, SMLAWB, SMLAWT, SMLSD, SMLSLD, SMMLA, SMMLS, SMMUL, SMUAD, SMULBB, SMULBT, SMULTT, SMULTB, SMULWT, SMULWB, SMUSD, SSAT16, SSAX, SSUB16, SSUB8, SXTAB, SXTAB16, SXTAH, SXTB16, UADD16, UADD8, UASX, UHADD16, UHADD8, UHASX, UHSAX, UHSUB16, UHSUB8, UMAAL, UQADD16, UQADD8, UQASX, UQSAX, UQSUB16, UQSUB8, USAD8, USADA8, USAT16, USAX, USUB16, USUB8, UXTAB, UXTAB16, UXTAH, UXTB16

No

No

Yes

Yes

No

Optional

Optional

Yes

Yes

Yes

SP Float

32

VABS, VADD, VCMP, VCMPE, VCVT, VCVTR, VDIV, VLDM, VLDR, VMLA, VMLS, VMOV, VMRS, VMSR, VMUL, VNEG, VNMLA, VNMLS, VNMUL, VPOP, VPUSH, VSQRT, VSTM, VSTR, VSUB

No

No

Optional

Optional

No

Optional

Optional

Optional

Optional

Optional

DP Float

32

VCVTA, VCVTM, VCVTN, VCVTP, VMAXNM, VMINNM, VRINTA, VRINTM, VRINTN, VRINTP, VRINTR, VRINTX, VRINTZ, VSEL

No

No

No

Optional

No

No

No

Optional

Optional

Optional

Acquire/Release

32

LDA, LDAB, LDAH, LDAEX, LDAEXB, LDAEXH, STL, STLB, STLH, STLEX, STLEXB, STLEXH

No

No

No

No

Yes

Yes

Yes

Yes

Yes

Yes

TrustZone

16

BLXNS, BXNS

No

No

No

No

Optional

Optional

Optional

Optional

Optional

Yes

32

SG, TT, TTT, TTA, TTAT

Co-processor

16

CDP, CDP2, MCR, MCR2, MCRR, MCRR2, MRC, MRC2, MRRC, MRRC2

No

No

No

No

No

Optional

Optional

Optional

Optional

Optional

ACI

32

CX1, CX1A, CX2, CX2A, CX3, CX3A, CX1D, CX1DA, CX2D, CX2DA, CX3D, CX3DA, VCX1, VCX1A, VCX2, VCX2A, VCX3, VCX3A

No

No

No

No

No

Optional

No

Optional

Optional

Optional

PACBTI

32

AUT, AUTG, BTI, BXAUT, PAC, PACBTI, PACG

No

No

No

No

No

No

No

Optional

No

Optional

- Note: MOVW is an alias that means 32-bit "wide" MOV instruction.
- Note: B.W is a long-distance unconditional branch (similar in encoding, operation, and range to BL, minus setting of the LR register).
- Note: For Cortex-M1, WFE / WFI / SEV instructions exist, but execute as a NOP instruction.
- Note: The half-precision (HP) FPU instructions are valid in the Cortex-M52 / M55 / M85 only when the HP FPU option exists in the silicon.
- Note: The single-precision (SP) FPU instructions are valid in the Cortex-M4 / M7 / M33 / M35P / M52 / M55 / M85 only when the SP FPU option exists in the silicon.
- Note: The double-precision (DP) FPU instructions are valid in the Cortex-M7 / M52 / M55 / M85 only when the DP FPU option exists in the silicon.

### Deprecations

The ARM architecture for ARM Cortex-M series removed some features from older legacy cores:

- The 32-bit ARM instruction set is not included in Cortex-M cores.
- Endianness is chosen at silicon implementation in Cortex-M cores. Legacy cores allowed "on-the-fly" changing of the data endian mode.
- Co-processors were not supported on Cortex-M cores, until the silicon option was reintroduced in "ARMv8-M Mainline" for ARM Cortex-M33/M35P cores.

The capabilities of the 32-bit ARM instruction set is duplicated in many ways by the Thumb-1 and Thumb-2 instruction sets, but some ARM features don't have a similar feature:

- The SWP and SWPB (swap) ARM instructions don't have a similar feature in Cortex-M.

The 16-bit Thumb-1 instruction set has evolved over time since it was first released in the legacy ARM7T cores with the ARMv4T architecture. New Thumb-1 instructions were added as each legacy ARMv5 / ARMv6 / ARMv6T2 architectures were released. Some 16-bit Thumb-1 instructions were removed from the Cortex-M cores:

- The "BLX <immediate>" instruction doesn't exist because it was used to switch from Thumb-1 to ARM instruction set. The "BLX <register>" instruction is still available in the Cortex-M.
- SETEND doesn't exist because on-the-fly switching of data endian mode is no longer supported.
- Co-processor instructions were not supported on Cortex-M cores, until the silicon option was reintroduced in "ARMv8-M Mainline" for ARM Cortex-M33/M35P cores.
- The SWI instruction was renamed to SVC, though the instruction binary coding is the same. However, the SVC handler code is different from the SWI handler code, because of changes to the exception models.

## Cortex-M0

The Cortex-M0 core is optimized for small silicon die size and use in the lowest price chips.

Key features of the Cortex-M0 core are:

- ARMv6-M architecture
- 3-stage pipeline
- Instruction sets:
  - Thumb-1 (most), missing CBZ, CBNZ, IT
  - Thumb-2 (some), only BL, DMB, DSB, ISB, MRS, MSR
  - 32-bit hardware integer multiply with 32-bit result
- 1 to 32 interrupts, plus NMI

**Silicon options:**

- Hardware integer multiply speed: 1 or 32 cycles.

### Chips

The following microcontrollers are based on the Cortex-M0 core:

- ABOV AC30M1x64
- Cypress PSoC 4000, 4100, 4100M, 4200, 4200DS, 4200L, 4200M
- Infineon XMC1100, XMC1200, XMC1300, XMC1400, TLE984x
- Dialog DA1458x, DA1468x
- Nordic nRF51
- NXP LPC1100, LPC1200
- Nuvoton NuMicro
- Sonix SN32F700
- ST STM32 F0
- Toshiba TX00
- Vorago VA10800 (extreme temperature), VA10820 (radiation hardened)

The following chips have a Cortex-M0 as a secondary core:

- NXP LPC4300 (one Cortex-M4F + one Cortex-M0)
- Texas Instruments SimpleLink Wireless MCUs CC1310 and CC2650 (one programmable Cortex-M3 + one Cortex-M0 network processor + one proprietary Sensor Controller Engine)

## Cortex-M0+

The Cortex-M0+ is an optimized superset of the Cortex-M0. The Cortex-M0+ has complete instruction set compatibility with the Cortex-M0 thus allowing the use of the same compiler and debug tools. The Cortex-M0+ pipeline was reduced from 3 to 2 stages, which lowers the power usage and increases performance (higher average IPC due to branches taking one fewer cycle). In addition to debug features in the existing Cortex-M0, a silicon option can be added to the Cortex-M0+ called the Micro Trace Buffer (MTB) which provides a simple instruction trace buffer. The Cortex-M0+ also received Cortex-M3 and Cortex-M4 features, which can be added as silicon options, such as the memory protection unit (MPU) and the vector table relocation.

Key features of the Cortex-M0+ core are:

- ARMv6-M architecture
- 2-stage pipeline (one fewer than Cortex-M0)
- Instruction sets: (same as Cortex-M0)
  - Thumb-1 (most), missing CBZ, CBNZ, IT
  - Thumb-2 (some), only BL, DMB, DSB, ISB, MRS, MSR
  - 32-bit hardware integer multiply with 32-bit result
- 1 to 32 interrupts, plus NMI

**Silicon options:**

- Hardware integer multiply speed: 1 or 32 cycles
- 8-region memory protection unit (MPU) (same as M3 and M4)
- Vector table relocation (same as M3, M4)
- Single-cycle I/O port (available in M0+/M23)
- Micro Trace Buffer (MTB) (available in M0+/M23/M33/M35P)

### Chips

The following microcontrollers are based on the Cortex-M0+ core:

- ABOV Semiconductor A31G11x, A31G12x, A31G314
- Cypress PSoC 4000S, 4100S, 4100S+, 4100PS, 4700S, FM0+
- Epson S1C31W74, S1C31D01, S1C31D50
- Holtek HT32F52000
- Microchip SAM C2, D0, D1, D2, DA, L2, R2, R3; and PIC32CM JH and MC
- NXP LPC800, LPC11E60, LPC11U60
- NXP (Freescale) Kinetis E, EA, L, M, V1, W0, S32K11x
- Puya PY32F0xx, PY32L0xx, PY32T0xx
- Raspberry Pi RP2040 (two M0+ cores)
- Renesas S124, S128, RE, RE01
- Silicon Labs (Energy Micro) EFM32 Zero, Happy
- ST STM32 L0, G0, C0, WL (one Cortex-M4 + one Cortex-M0+)

The following chips have a Cortex-M0+ as a secondary core:

- Cypress PSoC 6200 (one Cortex-M4F + one Cortex-M0+)
- ST WB (one Cortex-M4F + one Cortex-M0+)

The smallest ARM microcontrollers are of the Cortex-M0+ type (as of 2014, smallest at 1.6 mm by 2 mm in a chip-scale package is Kinetis KL03).

On 21 June 2018, the "world's smallest computer'", or computer device was announced – based on the ARM Cortex-M0+ (and including RAM and wireless transmitters and receivers based on photovoltaics) – by University of Michigan researchers at the 2018 Symposia on VLSI Technology and Circuits with the paper "A 0.04mm3 16nW Wireless and Batteryless Sensor System with Integrated Cortex-M0+ Processor and Optical Communication for Cellular Temperature Measurement." The device is one-tenth the size of IBM's previously claimed world-record-sized computer from months back in March 2018, which is smaller than a grain of salt.

## Cortex-M1

The Cortex-M1 is an optimized core especially designed to be loaded into FPGA chips.

Key features of the Cortex-M1 core are:

- ARMv6-M architecture
- 3-stage pipeline.
- Instruction sets:
  - Thumb-1 (most), missing CBZ, CBNZ, IT.
  - Thumb-2 (some), only BL, DMB, DSB, ISB, MRS, MSR.
  - 32-bit hardware integer multiply with 32-bit result.
- 1 to 32 interrupts, plus NMI.

**Silicon options:**

- Hardware integer multiply speed: 3 or 33 cycles.
- Optional Tightly-Coupled Memory (TCM): 0 to 1 MB instruction-TCM, 0 to 1 MB data-TCM, each with optional ECC.
- External interrupts: 0, 1, 8, 16, 32.
- Debug: none, reduced, full.
- Data endianness: little-endian or BE-8 big-endian.
- OS extension: present or absent.

### Chips

The following vendors support the Cortex-M1 as soft-cores on their FPGA chips:

- Altera Cyclone-II, Cyclone-III, Stratix-II, Stratix-III
- GOWIN M1
- Actel/Microsemi/Microchip Fusion, IGLOO/e, ProASIC3L, ProASIC3/E
- Xilinx Spartan-3, Virtex-2, Virtex-3, Virtex-4, Artix-7

## Cortex-M3

Key features of the Cortex-M3 core are:

- ARMv7-M architecture
- 3-stage pipeline with branch speculation.
- Instruction sets:
  - Thumb-1 (entire).
  - Thumb-2 (entire).
  - 32-bit hardware integer multiply with 32-bit or 64-bit result, signed or unsigned, add or subtract after the multiply. 32-bit multiply is 1 cycle, but 64-bit multiply and MAC instructions require extra cycles.
  - 32-bit hardware integer divide (2–12 cycles).
  - saturation arithmetic support.
- 1 to 240 interrupts, plus NMI.
- 12 cycle interrupt latency.
- Integrated sleep modes.

**Silicon options:**

- Optional Memory Protection Unit (MPU): 0 or 8 regions.

### Chips

The following microcontrollers are based on the Cortex-M3 core:

- ABOV AC33Mx128, AC33Mx064
- Actel/Microsemi/Microchip SmartFusion, SmartFusion 2 (FPGA)
- Analog Devices ADUCM360, ADUCM361, ADUCM3029
- Broadcom Wi-Fi Chip BCM4319XKUBG
- Cypress PSoC 5000, 5000LP, FM3
- Holtek HT32F
- Infineon TLE9860, TLE987x

- Maxim Integrated MAX32550
- Microchip (Atmel) SAM 3A, 3N, 3S, 3U, 3X
- NXP LPC1300, LPC1700, LPC1800
- ON Q32M210
- Realtek RTL8710
- Silicon Labs Precision32
- Silicon Labs (Energy Micro) EFM32 Tiny, Gecko, Leopard, Giant

- ST STM32 F1, F2, L1, W
- TDK-Micronas HVC4223F
- Texas Instruments F28, LM3, TMS470, OMAP 4, SimpleLink Wireless MCUs (CC1310 Sub-GHz and CC2650 BLE+Zigbee+6LoWPAN)
- Toshiba TX03
- mindmotion mindmotion MM32

The following chips have a Cortex-M3 as a secondary core:

- Apple A9 (Cortex-M3 as integrated M9 motion co-processor)
- CSR Quatro 5300 (Cortex-M3 as co-processor)
- Samsung Exynos 7420 (Cortex-M3 as a DVS microcontroller)
- Texas Instruments F28, LM3, TMS470, OMAP 4470 (one Cortex-A9 + two Cortex-M3)
- XMOS XS1-XA (seven xCORE + one Cortex-M3)

The following FPGAs include a Cortex-M3 core:

- Microsemi SmartFusion2 SoC

The following vendors support the Cortex-M3 as soft-cores on their FPGA chips:

- Altera Cyclone-II, Cyclone-III, Stratix-II, Stratix-III
- Xilinx Spartan-3, Virtex-2, Virtex-3, Virtex-4, Artix-7

## Cortex-M4

Conceptually the Cortex-M4 is a Cortex-M3 plus DSP instructions, and optional floating-point unit (FPU). A core with an FPU is known as Cortex-M4F.

Key features of the Cortex-M4 core are:

- ARMv7E-M architecture
- 3-stage pipeline with branch speculation.
- Instruction sets:
  - Thumb-1 (entire).
  - Thumb-2 (entire).
  - 32-bit hardware integer multiply with 32-bit or 64-bit result, signed or unsigned, add or subtract after the multiply. 32-bit Multiply and MAC are 1 cycle.
  - 32-bit hardware integer divide (2–12 cycles).
  - Saturation arithmetic support.
  - DSP extension: Single cycle 16/32-bit MAC, single cycle dual 16-bit MAC, 8/16-bit SIMD arithmetic.
- 1 to 240 interrupts, plus NMI.
- 12 cycle interrupt latency.
- Integrated sleep modes.

**Silicon options:**

- Optional floating-point unit (FPU): single-precision only IEEE-754 compliant. It is called the FPv4-SP extension.
- Optional memory protection unit (MPU): 0 or 8 regions.

### Chips

The following microcontrollers are based on the Cortex-M4 core:

- Ambiq Apollo, Apollo2, Apollo3, Apollo4
- Analog Devices ADSP-CM40x
- Microchip (Atmel) SAM 4L, 4N, 4S
- NXP (Freescale) Kinetis K, W2
- ST (STM32) WL (one Cortex-M4 + one Cortex-M0+)
- Texas Instruments SimpleLink Wi-Fi CC32xx, CC32xxMOD

The following microcontrollers are based on the Cortex-M4F (M4 + FPU) core:

- Analog Devices ADUCM4050
- Cypress 6200 (one Cortex-M4F + one Cortex-M0+), FM4
- Infineon XMC4000
- Maxim Darwin
- Microchip (Atmel) SAM4C (Dual core: one Cortex-M4F + one Cortex-M4), SAM4E, SAM4L, SAM4N, SAM4S, SAMG5, SAMD5/E5x

- Nordic nRF52
- Nuvoton NuMicro M480
- NXP LPC4000, LPC4300 (one Cortex-M4F + one Cortex-M0), LPC54000
- NXP (Freescale) Kinetis K, V3, V4, S32K14x
- Puya PY32F4xx, PY32E4xx
- Renesas S3, S5, S7, RA4, RA6
- Silicon Labs (Energy Micro) EFM32 Wonder

- ST STM32 F3, F4, L4, L4+, G4, WB (one Cortex-M4F + one Cortex-M0+)
- Texas Instruments LM4F, TM4C, MSP432, CC13x2R, CC1352P, CC26x2R
- Toshiba TX04

The following chips have either a Cortex-M4 or M4F as a secondary core:

- NXP (Freescale) Vybrid VF6 (one Cortex-A5 + one Cortex-M4F)
- NXP (Freescale) i.MX 6 SoloX (one Cortex-A9 + one Cortex-M4F)
- NXP (Freescale) i.MX 7 Solo/Dual (one or two Cortex-A7 + one Cortex-M4F)
- NXP (Freescale) i.MX 8 (two Cortex-A72 + four Cortex-A53 + two Cortex-M4F)
- NXP (Freescale) i.MX 8M and 8M Mini (four Cortex-A53 + one Cortex-M4F)
- NXP (Freescale) i.MX 8X (four Cortex-A35 + one Cortex-M4F)
- ST STM32MP1 (one or two Cortex-A7 + one Cortex-M4)
- Texas Instruments OMAP 5 (two Cortex-A15s + two Cortex-M4)
- Texas Instruments Sitara AM5700 (one or two Cortex-A15s + two Cortex-M4s as image processing units + two Cortex-M4s as general purpose units)

## Cortex-M7

The Cortex-M7 is a high-performance core with almost double the power efficiency of the older Cortex-M4. It features a 6-stage superscalar pipeline with branch prediction and an optional floating-point unit capable of single-precision and optionally double-precision operations. The instruction and data buses have been enlarged to 64-bit wide over the previous 32-bit buses. If a core contains an FPU, it is known as a Cortex-M7F, otherwise it is a Cortex-M7.

Key features of the Cortex-M7 core are:

- ARMv7E-M architecture.
- 6-stage pipeline with branch speculation. Second-longest of all ARM Cortex-M cores, with the first being Cortex-M85.
- Instruction sets:
  - Thumb-1 (entire).
  - Thumb-2 (entire).
  - 32-bit hardware integer multiply with 32-bit or 64-bit result, signed or unsigned, add or subtract after the multiply. 32-bit Multiply and MAC are 1 cycle.
  - 32-bit hardware integer divide (2–12 cycles).
  - Saturation arithmetic support.
  - DSP extension: Single cycle 16/32-bit MAC, single cycle dual 16-bit MAC, 8/16-bit SIMD arithmetic.
- 1 to 240 interrupts, plus NMI.
- 12 cycle interrupt latency.
- Integrated sleep modes.

**Silicon options:**

- Optional floating-point unit (FPU): (single precision) or (single and double-precision), both IEEE-754-2008 compliant. It is called the FPv5 extension.
- Optional CPU cache: 0 to 64 KB instruction-cache, 0 to 64 KB data-cache, each with optional ECC.
- Optional Tightly-Coupled Memory (TCM): 0 to 16 MB instruction-TCM, 0 to 16 MB data-TCM, each with optional ECC.
- Optional Memory Protection Unit (MPU): 8 or 16 regions.
- Optional Embedded Trace Macrocell (ETM): instruction-only, or instruction and data.
- Optional Retention Mode (with Arm Power Management Kit) for Sleep Modes.
- Optional dual-redundant lock-step operation.

### Chips

The following microcontrollers are based on the Cortex-M7 core:

- Microchip (Atmel) SAM E7, S7, V7
- NXP (Freescale) Kinetis KV5x, i.MX RT, S32K3xx
- ST STM32 F7, H7

The following chips have a Cortex-M7 as a secondary core:

- NXP (Freescale) i.MX 95 (up to 6 Cortex-A55 + one Cortex-M7 + one Cortex M33)

## Cortex-M23

The Cortex-M23 core was announced in October 2016 and based on the ARMv8-M architecture that was previously announced in November 2015. Conceptually the Cortex-M23 is similar to a Cortex-M0+ plus integer divide instructions and TrustZone security features, and also has a 2-stage instruction pipeline.

Key features of the Cortex-M23 core are:

- ARMv8-M Baseline architecture.
- 2-stage pipeline. (similar to Cortex-M0+)
- TrustZone security instructions.
- 32-bit hardware integer divide (17 or 34 cycles).(slower than divide in all other cores)
- Stack limit boundaries. (available only with SAU option)

**Silicon options:**

- Hardware integer multiply speed: 1 or 32 cycles.
- Hardware integer divide speed: 17 or 34 cycles maximum. Depending on divisor, instruction may complete in fewer cycles.
- Optional Memory Protection Unit (MPU): 0, 4, 8, 12, 16 regions.
- Optional Security Attribution Unit (SAU): 0, 4, 8 regions.
- Single-cycle I/O port (available in M0+/M23).
- Micro Trace Buffer (MTB)

### Chips

The following microcontrollers are based on the Cortex-M23 core:

- GigaDevice GD32E2xx
- Microchip SAM L10, L11, and PIC 32CM-LE 32CM-LS
- Nuvoton M23xx family, M2xx family, NUC1262, M2L31
- Renesas S1JA, RA0xx, RA2xx

## Cortex-M33

The Cortex-M33 core was announced in October 2016 and based on the ARMv8-M architecture that was previously announced in November 2015. Conceptually the Cortex-M33 is similar to a cross of Cortex-M4 and Cortex-M23, and also has a 3-stage instruction pipeline.

Key features of the Cortex-M33 core are:

- ARMv8-M Mainline architecture.
- 3-stage pipeline.
- TrustZone security instructions.
- 32-bit hardware integer divide (11 cycles maximum).
- Stack limit boundaries. (available only with SAU option)

**Silicon options:**

- Optional Floating-Point Unit (FPU): single-precision only IEEE-754 compliant. It is called the FPv5 extension.
- Optional Memory Protection Unit (MPU): 0, 4, 8, 12, 16 regions.
- Optional Security Attribution Unit (SAU): 0, 4, 8 regions.
- Micro Trace Buffer (MTB)

### Chips

The following microcontrollers are based on the Cortex-M33 core:

- Analog Devices ADUCM4
- Dialog DA1469x
- GigaDevice GD32E5, GD32W5
- Nordic nRF91, nRF5340, nRF54, nRF54H20
- NXP LPC5500, i.MX RT600, MCX N94x/54x (dual core)
- ON RSL15
- Renesas RA4, RA6
- ST STM32 C5, H5, L5, U3, U5, WBA
- Silicon Labs Wireless Gecko Series 2
- Texas Instruments CC3501E, CC3551E
- Raspberry Pi RP2350

The following chips have a Cortex-M33 or M33F as a secondary core:

- Infineon PSoC Edge
- ST STM32MP2 (one or two Cortex-A35 + one Cortex-M33)

## Cortex-M35P

The Cortex-M35P core was announced in May 2018 and based on the Armv8-M architecture. It is conceptually a Cortex-M33 core with a new instruction cache, plus new tamper-resistant hardware concepts borrowed from the ARM SecurCore family, and configurable parity and ECC features.

Currently, information about the Cortex-M35P is limited, because its *Technical Reference Manual* and *Generic User Guide* haven't been released yet.

### Chips

The following microcontrollers are based on the Cortex-M35P core:

- STMicroelectronics ST33K

## Cortex-M52

The Cortex-M52 core was announced in November 2023 and based on the Armv8.1-M architecture. Conceptually, it can be seen as a cross between the Cortex-M33 and the Cortex-M55. Key differences are that its Helium co-processor is single beat (the M55 is dual beat), and it has a 32-bit main bus similar to the M33 to ease transition of applications. It has a 4 stage instruction pipeline.

Key features of the Cortex-M52 core include:

- ARMv8.1-M Mainline/Helium architecture.
- 4-stage pipeline.
- Stack limit boundaries (available only with SAU option).
- 32-bit main bus (AHB or AXI)

**Silicon options:**

- Helium (M-Profile Vector Extension, MVE)
- Pointer Authentication and Branch Target Identification Extension
- Single-Precision and Double-Precision floating-point
- Digital Signal Processing (DSP) extension support
- TrustZone security extension support
- Safety and reliability (RAS) support
- Coprocessor support
- Secure and Non-secure MPU with 0, 4, 8, 12, or 16 regions
- SAU with 0, 4, or 8 regions
- Instruction cache with size of up to 64 KB
- Data cache with size of up to 64 KB
- ECC on caches and TCMs
- 1–480 interrupts
- 3–8 exception priority bits
- Internal and external WIC options, optional CTI, ITM, and DWT
- ARM Custom Instructions

### Chips

The following microcontrollers are based on the Cortex M52 core

- Geehy Semiconductor G32R5, G32R430

## Cortex-M55

The Cortex-M55 core was announced in February 2020 and based on the Armv8.1-M architecture. It has a 4 or 5 stage instruction pipeline.

Key features of the Cortex-M55 core include:

- ARMv8.1-M Mainline/Helium architecture.
- 4-stage pipeline.
- Stack limit boundaries (available only with SAU option).
- 64-bit AXI main bus

**Silicon options:**

- Helium (M-Profile Vector Extension, MVE)
- Single-Precision and Double-Precision floating-point
- Digital Signal Processing (DSP) extension support
- TrustZone security extension support
- Safety and reliability (RAS) support
- Coprocessor support
- Secure and Non-secure MPU with 0, 4, 8, 12, or 16 regions
- SAU with 0, 4, or 8 regions
- Instruction cache with size of 4 KB, 8 KB, 16 KB, 32 KB, 64 KB
- Data cache with size of 4 KB, 8 KB, 16 KB, 32 KB, 64 KB
- ECC on caches and TCMs
- 1–480 interrupts
- 3–8 exception priority bits
- Internal and external WIC options, optional CTI, ITM, and DWT
- ARM Custom Instructions

### Chips

- Alif Semiconductor Ensemble & Balletto MCU families offer single or dual Cortex-M55 cores, each paired with Ethos-U55 NPUs
- Ambiq Apollo330 Plus, Apollo510
- Infineon PSoC Edge
- ST STM32 N6

## Cortex-M85

The Cortex-M85 core was announced in April 2022 and based on the Armv8.1-M architecture. It has a 7-stage instruction pipeline.

**Silicon options:**

- Optional CPU cache: 0 to 64 KB instruction-cache, 0 to 64 KB data-cache, each with optional ECC.
- Optional Tightly-Coupled Memory (TCM): 0 to 16 MB instruction-TCM, 0 to 16 MB data-TCM, each with optional ECC.
- Optional Memory Protection Unit (MPU): 16 regions. Can have separate ones for secure and non-secure mode if TrustZone is implemented.
- Up to 480 interrupts and NMI
- 3–8 exception priority bits
- Optional dual-redundant lock-step operation.

### Chips

- Renesas RA8
- ST STM32 V8

## Development tools

## Documentation

The documentation for ARM chips is extensive. In the past, 8-bit microcontroller documentation would typically fit in a single document, but as microcontrollers have evolved, so has everything required to support them. A documentation package for ARM chips typically consists of a collection of documents from the IC manufacturer as well as the CPU core vendor (ARM Limited).

A typical top-down documentation tree is:

**Documentation tree (top to bottom)**

1. IC manufacturer website.
2. IC manufacturer marketing slides.
3. IC manufacturer datasheet for the exact physical chip.
4. IC manufacturer reference manual that describes common peripherals and aspects of a physical chip family.
5. ARM core website.
6. ARM core generic user guide.
7. ARM core technical reference manual.
8. ARM architecture reference manual.

IC manufacturers have additional documents, such as: evaluation board user manuals, application notes, getting started guides, software library documents, errata, and more. See External links section for links to official Arm documents.
