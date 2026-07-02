---
title: "RISC-V (part 1/3)"
source: https://en.wikipedia.org/wiki/RISC-V
domain: chisel-hdl
license: CC-BY-SA-4.0
tags: chisel hardware language, scala hardware, risc-v cores, rtl generation
fetched: 2026-07-02
part: 1/3
---

# RISC-V

**RISC-V** (pronounced "risk-five") is a free and open standard instruction set architecture (ISA) based on reduced instruction set computer (RISC) principles. Unlike proprietary ISAs such as x86 and ARM, RISC-V is described as "free and open" because its specifications are released under permissive open-source licenses and can be implemented without paying royalties.

RISC-V was developed in 2010 at the University of California, Berkeley as the fifth generation of RISC processors created at the university since 1981. In 2015, development and maintenance of the standard was transferred to **RISC-V International**, a non-profit organization based in Switzerland with more than 4,500 members as of 2025.

RISC-V is a popular architecture for microcontrollers and embedded systems, with development of higher-performance implementations targeting mobile, desktop, and server markets ongoing. The ISA is supported by several major Linux distributions, and companies such as SiFive, Andes Technology, SpacemiT, Synopsys, Alibaba (DAMO Academy), StarFive, Espressif Systems, and Raspberry Pi offer commercial systems on a chip (SoCs) and microcontrollers (MCUs) that incorporate one or more RISC-V compatible processor cores.


## History

The term *RISC* dates from about 1980. Before then, there was some knowledge (see John Cocke) that simpler computers can be effective, but the design principles were not widely described. Simple, effective computers have always been of academic interest, and resulted in the RISC instruction set DLX for the first edition of *Computer Architecture: A Quantitative Approach* in 1990 of which David Patterson was a co-author, and he later participated in the RISC-V origination. DLX was intended for educational use; academics and hobbyists implemented it using field-programmable gate arrays (FPGA), but it was never truly intended for commercial deployment.

Krste Asanović at the University of California, Berkeley, had a research requirement for an open-source CPU core, and in 2010, he decided to develop and publish his own, in a "short, three-month project over the summer" with several of his graduate students. Several established open-source alternatives were available, but Asanović chose not to use them. ARM and SuperH CPUs (versions 2 and earlier) had public-domain instruction sets with VHDL implementation files, while complete OpenRISC, OpenPOWER, and OpenSPARC / LEON cores were also available either as VHDL files or from various vendors. All of these existing options were supported by the GNU Compiler Collection (GCC), a popular free-software compiler, and had Linux kernel support. The plan was to aid both academic and industrial users. David Patterson at Berkeley joined the collaboration as he was the originator of the Berkeley RISC, and the RISC-V is the eponymous fifth generation of his long series of cooperative RISC-based research projects at the University of California, Berkeley (RISC-I and RISC-II published in 1981 by Patterson, who refers to the SOAR architecture from 1984 as "RISC-III" and the SPUR architecture from 1988 as "RISC-IV"). At this stage, students provided initial software, simulations, and CPU designs.

The RISC-V authors and their institution originally sourced the ISA documents and several CPU designs under BSD licenses, which allow derivative works—such as RISC-V chip designs—to be either open and free, or closed and proprietary. The ISA specification itself (i.e., the encoding of the instruction set) was published in 2011 as open source, with all rights reserved. The actual technical report (an expression of the specification) was later placed under the license Creative Commons - Attribution 4.0 to permit enhancement by external contributors through the RISC-V Foundation, and later RISC-V International.

A full history of RISC-V has been published on the RISC-V International website.

### Foundations

Commercial users require an ISA to be stable before they can use it in a product that may last many years. To address this issue, the RISC-V Foundation was formed in 2015 to own, maintain, and publish intellectual property related to RISC-V's definition. The original authors and owners have surrendered their rights to the foundation. The foundation was led by CEO Calista Redmond, who took on the role in 2019 after leading open infrastructure projects at IBM. In 2024 she resigned as CEO.

The founding members of RISC-V were: Andes Technology, Antmicro, Bluespec, Ceva, Codasip, Cortus, Esperanto Technologies, Espressif Systems, ETH Zurich, Google, IBM, ICT, IIT Madras, Lattice Semiconductor, LowRISC, Microchip Technology, the MIT Computer Science and Artificial Intelligence Laboratory, Qualcomm, Rambus, Rumble Development, SiFive, Syntacore and Technolution.

In November 2019, the RISC-V Foundation announced that it would relocate to Switzerland, citing concerns over U.S. trade regulations. As of March 2020, the organization was named RISC-V International, a Swiss nonprofit business association.

As of 2019, RISC-V International freely publishes the documents defining RISC-V and permits unrestricted use of the ISA for design of software and hardware. However, only members of RISC-V International can vote to approve changes, and only member organizations use the trademarked compatibility logo.

The Linux Foundation Europe started the RISC-V Software Ecosystem (RISE) initiative on May 31, 2023. The goal of RISE is to increase the availability of software for high-performance and power-efficient RISC-V processors running high-level operating systems for a range of market segments by bringing together a large number of hardware and software vendors. Red Hat, Samsung, Qualcomm, Nvidia, MediaTek, Intel, and Google are among the initial members.

### Awards

- 2017: The Linley Group's Analyst's Choice Award for Best Technology (for the instruction set)


## Rationale

CPU design requires design expertise in several specialties: electronic digital logic, compilers, and operating systems. To cover the costs of such a team, commercial vendors of processor intellectual property (IP), such as Arm Ltd. and MIPS Technologies, charge royalties for the use of their designs and patents. They also often require non-disclosure agreements before releasing documents that describe their designs' detailed advantages. In many cases, they never describe the reasons for their design choices.

RISC-V was begun with a goal to make a practical ISA that was open-sourced, usable academically, and deployable in any hardware or software design without royalties. Also, justifying rationales for each design decision of the project are explained, at least in broad terms. The RISC-V authors are academics who have substantial experience in computer design, and the RISC-V ISA is a direct development from a series of academic computer-design projects, especially Berkeley RISC. RISC-V was originated in part to aid all such projects.

To build a large, continuing community of users and thereby accumulate designs and software, the RISC-V ISA designers intentionally support a wide variety of practical use cases: compact, performance, and low-power real-world implementations without over-architecting for a given microarchitecture. The requirements of a large base of contributors is part of the reason why RISC-V was engineered to address many possible uses.

The designers' primary assertion is that the instruction set is the key interface in a computer as it is situated at the interface between the hardware and the software. If a good instruction set were open and available for use by all, then it can dramatically reduce the cost of software by enabling far more reuse. It should also trigger increased competition among hardware providers, who can then devote more resources toward design and less for software support.

The designers maintain that new principles are becoming rare in instruction set design, as the most successful designs of the last forty years have grown increasingly similar. Of those that failed, most did so because their sponsoring companies were financially unsuccessful, not because the instruction sets were technically poor. Thus, a well-designed open instruction set designed using well-established principles should attract long-term support by many vendors.

RISC-V also encourages academic usage. The simplicity of the integer subset permits basic student exercises, and is a simple enough ISA to enable software to control research machines. The variable-length ISA provides room for instruction set extensions for both student exercises and research, and the separated privileged instruction set permits research in operating system support without redesigning compilers. RISC-V's open intellectual property paradigm allows derivative designs to be published, reused, and modified.


## ISA base and extensions

RISC-V has a modular design, consisting of alternative base parts, with added optional extensions. The ISA base and its extensions are developed in a collective effort between industry, the research community and educational institutions. The base specifies instructions (and their encoding), control flow, registers (and their sizes), memory and addressing, logic (i.e., integer) manipulation, and ancillaries. The base alone can implement a simplified general-purpose computer, with full software support, including a general-purpose compiler.

### Standard extensions

The standard extensions are specified to work with all of the standard bases, and with each other without conflict.

Many RISC-V computers might implement the compressed instructions extension, C, to reduce power consumption, code size, and memory use. There are also future plans to support hypervisors and virtualization.

Together with the supervisor extension, S, an RVG instruction set, which includes one of the RV base instruction sets, and the G collection of extensions (which includes "I", meaning that the base is non-embedded), defines all instructions needed to conveniently support a general purpose operating system.

| Name | Description | Version | Status | Instruction count |
|---|---|---|---|---|
| Base |   |   |   |   |
| RVWMO | Weak memory ordering | 2.0 | Ratified |   |
| RV32I | Base integer instruction set, 32-bit | 2.1 | Ratified | 40 |
| RV32E | Base integer instruction set (embedded), 32-bit, 16 registers | 2.0 | Ratified | 40 |
| RV64I | Base integer instruction set, 64-bit | 2.1 | Ratified | 52 |
| RV64E | Base integer instruction set (embedded), 64-bit | 2.0 | Ratified | 52 |
| RV128I | Base integer instruction set, 128-bit | 1.7 | Open | 64 |
| Extension |   |   |   |   |
| M | Standard extension for integer multiplication and division | 2.0 | Ratified | 8 (RV32) 13 (RV64) |
| A | Standard extension for atomic instructions | 2.1 | Ratified | 11 (RV32) 22 (RV64) |
| F | Standard extension for single-precision floating-point | 2.2 | Ratified | 26 (RV32) 30 (RV64) |
| D | Standard extension for double-precision floating-point | 2.2 | Ratified | 26 (RV32) 32 (RV64) |
| Zicsr | Control and status register (CSR) instructions | 2.0 | Ratified | 6 |
| Zifencei | Instruction-fetch fence | 2.0 | Ratified | 1 |
| G | Shorthand for the IMAFD_Zicsr_Zifencei base and extensions | —N/a | —N/a |   |
| Q | Standard extension for quad-precision floating-point | 2.2 | Ratified | 28 (RV32) 32 (RV64) |
| L | Standard extension for decimal floating-point | 0.0 | Open |   |
| C | Standard extension for compressed instructions | 2.0 | Ratified | 40 |
| B | Standard extension for bit manipulation | 1.0 | Ratified | 29 (RV32) 41 (RV64) |
| J | Standard extension for dynamically translated languages | 0.0 | Open |   |
| T | Standard extension for transactional memory | 0.0 | Open |   |
| P | Standard extension for packed-SIMD instructions | 0.9.10 | Open |   |
| V | Standard extension for vector operations | 1.0 | Ratified | 187 |
| Zk | Standard extension for scalar cryptography | 1.0.1 | Ratified | 49 |
| H | Standard extension for hypervisor | 1.0 | Ratified | 15 |
| S | Standard extension for supervisor-level instructions | 1.12 | Ratified | 4 |
| Zam | Misaligned atomics | 0.1 | Open |   |
| Zihintpause | Pause hint | 2.0 | Ratified |   |
| Zihintntl | Non-temporal locality hints | 0.3 | Ratified |   |
| Zfa | Additional floating-point instructions | 1.0 | Ratified |   |
| Zfh | Half-precision floating-point | 1.0 | Ratified |   |
| Zfhmin | Minimal half-precision floating-point | 1.0 | Ratified |   |
| Zfinx | Single-precision floating-point in integer register | 1.0 | Ratified |   |
| Zdinx | Double-precision floating-point in integer register | 1.0 | Ratified |   |
| Zhinx | Half-precision floating-point in integer register | 1.0 | Ratified |   |
| Zhinxmin | Minimal half-precision floating-point in integer register | 1.0 | Ratified |   |
| Zmmul | Multiplication subset of the M extension | 1.0 | Ratified |   |
| Ztso | Total store ordering | 1.0 | Ratified |   |

1. Frozen parts are expected to have their final feature set and to receive only clarifications before being ratified.

32-bit RISC-V instruction formats

Format

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

Store

imm[11:5]

rs2

rs1

funct3

imm[4:0]

opcode

Branch

[12]

imm[10:5]

imm[4:1]

[11]

Register/register

funct7

rd

Immediate

imm[11:0]

Upper immediate

imm[31:12]

Jump

[20]

imm[10:1]

[11]

imm[19:12]

- ***opcode* (7 bits):** Partially specifies one of the 6 types of *instruction formats*.
- ***funct7* (7 bits) and *funct3* (3 bits):** These two fields extend the *opcode* field to specify the operation to be performed.
- ***rs1* (5 bits) and *rs2* (5 bits):** Specify, by index, the first and second operand registers respectively (i.e., source registers).
- ***rd* (5 bits):** Specifies, by index, the destination register to which the computation result will be directed.

To name the combinations of functions that may be implemented, a nomenclature is defined to specify them in Chapter 27 of the current ratified Unprivileged ISA Specification. The instruction set base is specified first, coding for RISC-V, the register bit-width, and the variant; e.g., RV64I or RV32E. Then follows letters specifying implemented extensions, in the order of the above table. Each letter may be followed by a major optionally followed by "p" and a minor option number. It defaults to 0 if a minor version number is absent, and 1.0 if all of a version number is absent. Thus RV64IMAFD may be written as RV64I1p0M1p0A1p0F1p0D1p0 or more simply as RV64I1M1A1F1D1. Underscores may be used between extensions for readability, for example RV32I2_M2_A2.

The base, extended integer & floating-point calculations, with synchronization primitives for multi-core computing, are considered to be necessary for general-purpose computing, and thus we have the shorthand, "G".

A small 32-bit computer for an embedded system might be RV32EC. A large 64-bit computer might be RV64GC; i.e., RV64IMAFDCZicsr_Zifencei.

With the growth in the number of extensions, the standard now provides for extensions to be named by a single "Z" followed by an alphabetical name and an optional version number. For example, Zifencei names the instruction-fetch extension. Zifencei2 and Zifencei2p0 name version 2.0 of the same. The first letter following the "Z" by convention indicates the most closely related alphabetical extension category, IMAFDQLCBJTPVN. Thus the Zam extension for misaligned atomics relates to the "A" standard extension. Unlike single character extensions, Z extensions must be separated by underscores, grouped by category and then alphabetically within each category. For example, Zicsr_Zifencei_Zam.

Extensions specific to supervisor privilege level are named in the same way using "S" for prefix. Extensions specific to hypervisor level are named using "H" for prefix. Machine level extensions are prefixed with the three letters "Zxm". Supervisor, hypervisor and machine level instruction set extensions are named after less privileged extensions.

RISC-V developers may create their own non-standard instruction set extensions. These follow the "Z" naming convention, but with "X" as the prefix. They should be specified after all standard extensions, and if multiple non-standard extensions are listed, they should be listed alphabetically.

### Profiles and platforms

Profiles and platforms for standard ISA choice lists are under discussion.

> This flexibility can be used to highly optimize a specialized design by including only the exact set of ISA features required for an application, but the same flexibility also leads to a combinatorial explosion in possible ISA choices. Profiles specify a much smaller common set of ISA choices that capture the most value for most users, and which thereby enable the software community to focus resources on building a rich software ecosystem.

> The platform specification defines a set of platforms that specify requirements for interoperability between software and hardware. The Platform Policy defines the various terms used in this platform specification. The platform policy also provides the needed detail regarding the scope, coverage, naming, versioning, structure, life cycle and compatibility claims for the platform specification.

- The RISC-V Profiles RVI20, RVA20, RVA22 are version 1.0 as at March 2023.
- The RVA23 and RVB23 Profiles are version 1.0 as at October 2024. RVA23U64 makes the V Vector extensions mandatory, it was optional in RVA22U64.
