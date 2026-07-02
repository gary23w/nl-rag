---
title: "RISC-V (part 3/3)"
source: https://en.wikipedia.org/wiki/RISC-V
domain: arm-riscv
license: CC-BY-SA-4.0
tags: arm architecture, aarch64, risc-v, riscv, cortex-m, instruction set
fetched: 2026-07-02
part: 3/3
---

## Implementations

### Strategic background

The RISC-V organization maintains a list of RISC-V CPU and SoC implementations. Due to trade wars and possible sanctions that would prevent China from accessing proprietary ISAs, as of 2023 the country was planning to shift most of its CPU architectures and designs of microcontrollers (MCUs) to RISC-V cores.

In 2023, the European Union was set to provide 270 million euros within a so-called Framework Partnership Agreement (FPA) to a single company that was able and willing to carry out a RISC-V CPU development project aimed at supercomputers, servers, and data centers. The European Union's aim was to become independent from political developments in other countries and to "strengthen its digital sovereignty and set standards, rather than following those of others."

According to The Register, Chinese media reported in March 2025 from the conference where the server-grade CPU Alibaba DAMO Xuantie C930 was launched that senior Alibaba Cloud executives had predicted that RISC-V would become a mainstream cloud architecture as early as 2030. According to Reuters, Chinese government bodies in 2025 had been working on "guidance" that would promote widespread use of RISC-V throughout China.

### Significant for-market developments

In 2019, SiFive of Santa Clara, California, announced their first RISC-V out-of-order high performance CPU core, the U8 Series Processor IP. SiFive was established specifically for developing RISC-V hardware and began releasing processor models in 2017. These included a quad-core, 64-bit (RV64GC) system on a chip (SoC) capable of running general-purpose operating systems such as Linux.

In July 2019, DAMO Academy, the research arm of Alibaba Group of Hangzhou, China, announced the 2.5 GHz 16-core 64-bit (RV64GC) Xuantie 910 out-of-order processor. In October 2021 the Xuantie 910 was released as an open-source design.

In 2022, Imagination Technologies of Kings Langley, England, announced it had paired its own 64bit Catapult RISC-V core, with its IMG BXE-2-32 GPU, on a SoC, that was validated by Andes Technology. The BXE GPU supporting Vulkan 1.2, OpenGL ES 3.x/2.0/1.1, OpenCL 3.0, and Android NN HAL APIs.

In November 2023, DAMO unveiled three updated processors: the Xuantie C920, Xuantie C907 and Xuantie R910; these processors were aimed at a variety of application areas, including autonomous vehicles, artificial intelligence (AI), enterprise hard drives, and network communications.

In 2024, SpacemiT, a Chinese company headquartered in Hangzhou, developed their "Key Stone K1", an octa-core 64-bit processor that is available in the BPI-F3 computer, as well as the following other devices: LicheePi 3A, the Milk-V Jupiter, the DeepComputing DC-ROMA LAPTOP II, and the SpacemiT MUSEbook featuring the Bianbu OS operating system. The processor is based on the X60 core design, integrates an Imagination Technologies IMG BXE-2-32 graphics unit, and supports the vector extension RVV 1.0.

In January 2025, SpacemiT announced the development of a server processor with up to 64 RISC-V cores, called "VitalStone V100" and made with a 12 nm-class process technology. The VitalStone V100 processor is largely based on the OpenC910 project design, a design which is modelled on the Xuantie C910 processor, designed by Alibaba's DAMO Academy.

In March 2025, Alibaba's DAMO Academy launched the server-grade Xuantie C930 core, which supported the next-generation RVA23 profile family, required by Ubuntu Linux from October 2025. The C930 CPU core was advertised as ideal for servers, personal computers, and autonomous cars. It created significant competition for the California-based company SiFive and its P870 core, the design of which SiFive had already released in October 2023. The P870 was the first SiFive core to support the new RVA23 profile family. Both with regard to the C930 and the P870 design, no physical chips had actually been built for general sale in August 2025, however.

On 26 March 2026, Alibaba released the Xuantie C950, a high-performance 64-bit RISC-V processor core. This core, which was built on the up-to-date RVA23 profile, was designed for high workloads such as edge AI, cloud computing, and other high-performance systems. The C950 had a maximum clock frequency of 3.2 GHz and was ready for production on an advanced 5-nm process node, with sources indicating that TSMC would manufacture the C950. Industry magazine *EE Times* commented that the C950’s performance benchmarks proved that an open-source design could reach performance levels that, up to 2026, only proprietary designs from Intel or Arm were able to reach.

### Other developments

#### Existing

Existing proprietary implementations include:

- Akeana of Santa Clara, CA, a Premier member of RISC-V International, offers a wide range of RISC-V-based IP. Its offerings range from tiny 32-bit cores to advanced datacenter-class 64-bit cores with FPU, Vector, Hypervisor, and multicore capabilities, as well as IOMMU, high-speed interconnect fabric, AI accelerators, and related IP.
- Andes Technology Corporation of Hsinchu, Taiwan, a Founding Premier member of RISC-V International. Its RISC-V CPU families range from tiny 32-bit cores to advanced 64-bit cores with DSP, FPU, vector, superscalar, and/or multicore capabilities.
- Bouffalo Lab has a series of MCUs based on RISC-V (RV32IMACF, BL60x/BL70x series).
- CloudBEAR is a processor IP company that develops its own RISC-V cores for a range of applications.
- Codasip of Munich, Germany, a founding member of RISC-V International, started developing a range of low-power embedded, high-performance embedded and application processor cores in 2015. In 2016, Codasip and UltraSoC developed fully supported intellectual property for RISC-V embedded SOCs that combine Codasip's RISC-V cores and other IP with UltraSoC's debug, optimization and analytics.
- Cortus of Mauguio in the Montpellier area, France, is an original founding Platinum member of the RISC-V foundation and the RISC-V International. The company offers several RISC-V implementations. Cortus offers ASIC design services using its IP portfolio including RISC-V 32/64-bit processors from low-end to very high performance RISC-V processors, digital, analog, RF, security and a complete IDE/toolchain/debug eco-system.
- Espressif of Shanghai, China, added a RISC-V ULP coprocessor to their ESP32-S2 microcontroller. In November 2020 Espressif announced its ESP32-C3, a single-core, 32-bit, RISC-V-based MCU (RV32IMC).
- The Fraunhofer Institute for Photonic Microsystems, based in Dresden, Germany, was the first organization to develop a RISC-V core that can meet functional safety requirements. The IP Core EMSA5 is a 32-bit processor with a five-stage pipeline and is available as a general purpose variant (EMSA5-GP) and as a safety variant (EMSA5-FS) that can meet an ISO 26262 Automotive Safety Integrity Level-D standard.
- GigaDevice of Beijing, China, developed a series of MCUs based on RISC-V (RV32IMAC, GD32V series) in 2019, with one of them used on the Longan Nano board produced by a Chinese electronic company *Sipeed*.
- Google has developed the Titan M2 security module for the Pixel 6 and Pixel 7
- GreenWaves Technologies announced the availability of GAP8, a 32-bit 1 controller plus 8 compute cores, 32-bit SoC (RV32IMC) and developer board in February 2018. Their GAPuino GAP8 development board started shipping in May 2018.
- Imagination Technologies of Kings Langley, England, UK, released the RTXM-2200 in 2023, their first core from their Catapult range. This is a real-time, deterministic, 32-bit embedded CPU.
- Instant SoC RISC-V cores from FPGA cores. System on chip, including RISC-V cores, defined by C++.
- Micro Magic Inc. announced the world's fastest 64-bit RISC-V core achieving 5 GHz and 13 000 CoreMarks in October 2020.
- MIPS Technologies of San Jose, California, pivoted to developing RISC-V cores in 2021. It rolled out its first implementation eVocore P8700 in December 2022.
- Nordic Semiconductor has announced its nRF54H20 family of Bluetooth radio chips that include multiple RISC-V coprocessor cores in addition to their more-usual ARM cores.
- Seagate, in December 2020, announced that it had developed two RISC-V general-purpose cores for use in upcoming controllers for its storage devices.
- StarFive, (initially an exclusive distributor of SiFive RISC-V core IP products in the greater China region) of Shanghai, China, offers two RISC-V implementations – one for big data applications and the other for computational storage.
- Syntacore, a founding member of RISC-V International and one of the first commercial RISC-V IP vendors, develops and licenses family of RISC-V IP since 2015. As of 2018, product line includes eight 32- and 64-bit cores, including open-source SCR1 MCU core (RV32I/E[MC]). First commercial SoCs, based on the Syntacore IP were demonstrated in 2016.
- WinChipHead (WCH), a Chinese semiconductor manufacturer of popular and inexpensive USB chips such as CH340 and ARM microcontrollers introduced a simple, inexpensive RISC-V microcontroller line CH32Vxxx, headed by US$0.10 CH32V003.
- As of 2020, the Indian defence and strategic sector started using the 64-bit RISC-V based 100–350 MHz Risecreek processor developed by IIT Madras which is fabricated by Intel with 22 nm FinFET process. IIT Madras and ISRO Inertial Systems Unit successfully designed and booted a 64-bit RISC-V Controller for Space Applications (IRIS) chip based on the SHAKTI baseline processor in February 2025. The chip configuration takes into account the processing power and functional needs of the devices and sensors utilized in ISRO missions. To improve dependability, fault-tolerant internal memory were interfaced with the SHAKTI core.
- RIES v3.0d development boards are the first to use DIR-V VEGA RISC-V processors. It contains the VEGA ET1031, a 32-bit RISC-V CPU with three UART serial ports, four Serial Peripheral Interface ports, two megabytes of flash memory, 256KB of SRAM, and three 32-bit timers. It operates at 100 MHz. It is advised for usage in wearables, toys, small IoT devices, and sensors by C-DAC in Indian market.
- For efficiency and multitasking capabilities in consumer electronics, automotive systems, 5G infrastructure, industrial automation, and the IoT, C-DAC introduced the dual-core 1.0 GHz DHRUV RISC-V 64-bit processor in 2025 using 28 nm process.

#### In development

- ASTC developed a RISC-V CPU for embedded ICs.
- Centre for Development of Advanced Computing (C-DAC) in India is developing a single core 32-bit in-order, a single core 64-bit in-order and three out-of-order single, dual and quad-core RISC-V processor under VEGA Microprocessors series.
- Cobham Gaisler NOEL-V 64-bit.
- Computer Laboratory, University of Cambridge, in collaboration with the FreeBSD Project, has ported that operating system to 64-bit RISC-V to use as a hardware-software research platform.
- Esperanto Technologies announced that they are developing three RISC-V based processors: the *ET-Maxion* high-performance core, *ET-Minion* energy-efficient core, and *ET-Graphics* graphics processor.
  - Esperanto ET-SoC-1, a 200 TOPS "kilocore" supercomputer on a chip, with 1088 small 64-bit in-order ET-Minion cores with tensor/vector units and 4 big 64-bit out-of-order ET-Maxion cores
- ETH Zurich and the University of Bologna have cooperatively developed the open-source RISC-V PULPino processor as part of the Parallel Ultra-Low Power (PULP) project for energy-efficient IoT computing.
- European Processor Initiative (EPI), RISC-V Accelerator Stream.
- Reconfigurable Intelligent Systems Engineering Group (RISE) of IIT-Madras is developing six Shakti series RISC-V open-source CPU designs for six distinct uses, from a small 32-bit CPU for the Internet of things (IoT) to large, 64-bit CPUs designed for warehouse-scale computers such as server farms based on RapidIO and Hybrid Memory Cube technologies. 32-bit Moushik successfully booted by RISE for the application of credit cards, electronic voting machines (EVMs), surveillance cameras, safe locks, personalized health management systems.
- lowRISC is a non profit project to implement a fully open-source hardware system on a chip (SoC) based on the 64-bit RISC-V ISA.
- Nvidia plans to use RISC-V to replace their Falcon processor on their GeForce graphics cards.
- RV64X consortium is working on a set of graphics extensions to RISC-V and has announced that they are developing an open source RISC-V core with a GPU unit.
- Ventana Micro Systems revealed it is developing high performance RISC-V CPU IP and chiplet technology targeting data center applications.

#### Open source

- The Berkeley CPUs are implemented in a unique hardware design language, Chisel, and some are named for famous train engines:
  - 64-bit Rocket. Rocket may suit compact, low-power intermediate computers such as personal devices. Named for Stephenson's *Rocket*.
  - The 64-bit Berkeley Out of Order Machine (BOOM). The Berkeley Out-of-Order Machine (BOOM) is a synthesizable and parameterizable open source RV64GC RISC-V core written in the Chisel hardware construction language. BOOM uses much of the infrastructure created for Rocket, and may be usable for personal, supercomputer, and warehouse-scale computers.
  - Five 32-bit Sodor CPU designs from Berkeley, designed for student projects. Sodor is the fictional island of The Railway Series.
- The Institute of Computing Technology of the Chinese Academy of Sciences (ICT CAS) in June 2020 launched the XiangShan high-performance RISC-V processor project. In summer 2021, a CPU prototype produced at TSMC on a 28 nm process node, with speeds of up to 1.3 GHz, was presented at a RISC-V conference in China. An updated prototype was to be produced at SMIC on a 14 nm process node with speeds of up to 2 GHz. The capabilities of the second XiangShan processor, called “Nanhu”, which was released in August 2022, may have surpassed those of the ARM Cortex-A76, a current CPU at the time, making Nanhu the most powerful open-source CPU in the world in 2023. For 2022 the Institute of Computing Technology was planning to announce a new XiangShan design with the RISC-V Vector extension for applications such as AI acceleration; in the future it hoped to find a "Red Hat" type company that would engage in commercialization of its XiangShan cores.
- PicoRV32 by Claire Wolf, a 32-bit microcontroller unit (MCU) class RV32IMC implementation in Verilog.
- The CORE-V family of open-source RISC-V cores is curated by the OpenHW Foundation.
- SCR1 from Syntacore, a 32-bit microcontroller unit (MCU) class RV32IMC implementation in Verilog.
- MIPT-MIPS by MIPT-ILab (MIPT Lab for CPU Technologies created with help of Intel). MIPT-MIPS is a cycle-accurate pre-silicon simulator of RISC-V and MIPS CPUs. It measures *performance* of program running on CPU. Among key features are: compatibility with interactive MARS system calls, interactive simulation with GDB, configurable branch prediction unit with several prediction algorithms and instruction cache and interstage data bypassing. Implementation in C++.
- SERV by Olof Kindgren, a physically small, validated bit-serial RV32I core in Verilog, is the world's smallest RISC-V CPU. It is integrated with both the LiteX and FuseSoC SoC construction systems. An FPGA implementation was 125 lookup tables (LUTs) and 164 flip-flops, running at 1.5 MIPS, In a 130 nm-node ASIC, it was 2.1kGE and a high-end FPGA could hold 10,000 cores.
- PULPino (Riscy and Zero-Riscy) from ETH Zürich / University of Bologna. The cores in PULPino implement a simple RV32IMC ISA for microcontrollers (Zero-Riscy) or a more powerful RV32IMFC ISA with custom DSP extensions for embedded signal processing.
- Western Digital, in December 2018 announced an RV32IMC core called SweRV EH1 featuring an in-order 2-way superscalar and nine-stage pipeline design. In December 2019, WD announced the SweRV EH2 an in-order core with two hardware threads and a nine-stage pipeline and the SweRV EL2 a single issue core with a 4-stage pipeline WD plans to use SweRV based processors in its flash controllers and SSDs, and released it as open-source to third parties in January 2019.
- NEORV32 by Stephan Nolting, a highly-configurable 32-bit microcontroller unit (MCU) class RV32[I/E]MACUX_Zbb_Zfinx_Zicsr_Zifencei CPU with on-chip debugger support written in platform-independent VHDL. The project includes a microcontroller-like SoC that already includes common modules like UART, timers, SPI, TWI, a TRNG and embedded memories.
- Hazard3 by Luke Wren, a RV32I processor with a three-stage pipeline. Two Hazard3 cores are implemented in the RP2350 microcontroller.


## End-user hardware

In 2022, ClockworkPi released two hobbyist computing kits, the DevTerm terminal and uConsole handheld computer. Both kits offered a single core 64-bit RISC-V module as an option, using the RV64IMAFDCVU based on the Allwinner D1 SoC.

DeepComputing, a hardware company based in Hong Kong, announced the release on 13 April 2023 of the "world's first laptop with RISC-V processor"; the notebook, called "DC-ROMA", was delivered to its first customers in August 2023 and came pre-installed with the Chinese openKylin Linux operating system. The device's basic model, available from Alibaba, was still expensive at roughly US$1500 considering it was powered by the relatively slow Alibaba (DAMO) CPU "XuanTie C910".

An upgrade in June 2024 doubled the core count to 8 cores and increased the clock speed to 2 GHz (from 1.5 GHz), while dropping the price to US$1,000. The processor used was a SpacemiT SoC K1. A collaboration with Canonical meant that the ROMA II came pre-installed with the major international Linux distribution Ubuntu.

In 2024, DeepComputing announced a collaboration with Framework Computer to produce a mainboard for its Framework Laptop 13. On 4 February 2025 the laptop was ready to ship; it was mainly targeted at developers. It features a 4-core StarFive JH7110 processor.

In 2025, DeepComputing announced DC-ROMA AI PC, a second mainboard for the Framework Laptop 13. Its based on ESWIN's EIC7702X SoC that has AI capabilities up to 50 TOPS when NPU (Neural Processing Unit) is enabled.


## Software

In addition to having a large number of CPU hardware designs, RISC-V is also supported by toolchains, operating systems (e.g. Linux), middleware, and design software:

Available RISC-V software tools include a GNU Compiler Collection (GCC) toolchain (with GDB, the debugger), an LLVM toolchain, the OVPsim simulator (and library of RISC-V Fast Processor Models), the Spike simulator, and a simulator in QEMU (RV32GC/RV64GC). A port of OpenJDK is already integrated into the mainline OpenJDK repository.

Operating system support exists for the Linux kernel, FreeBSD, NetBSD, and OpenBSD. The preliminary FreeBSD port to the RISC-V architecture was upstreamed in February 2016, and shipped in FreeBSD 11.0.

As one of only seven CPU architectures (e.g. ARM or x86), Debian Linux has officially supported RISC-V since Debian Trixie, which was released in August 2025. Ports of Linux distributions Fedora, and openSUSE, and a port of Haiku, also exist (64-bit versions only, not 32-bit versions). In June 2024, Hong Kong company DeepComputing announced the commercial availability of the first RISC-V laptop in the world to run the popular Linux operating system Ubuntu in its standard form ("out of the box").

In August 2025, Ubuntu decided, however, to drop support for older "profiles" (e.g. RV64GC or RVA20), meaning then-existing RISC-V CPUs were no longer supported from Ubuntu version 25.10 (i.e. from October 2025; older Ubuntu versions still supported older profiles and CPUs, of course). In September 2025, there were no actual processors to be had on the market for the "RVA23" profile newly required by Ubuntu, only a couple of designs (e.g. the XuanTie C930 from DAMO Academy, or the SiFive P870). The computer news website Heise Online explained the sudden cut-off by the fact that processors using the older RV64GC technology had usually turned out to be very weak in benchmarks (and therefore of limited use to an up-to-date end-user operating system), and that the newer RVA23 design would lead to much faster processors (e.g. clock frequencies well above 2 GHz).

A port of Das U-Boot exists. UEFI Spec v2.7 has defined the RISC-V binding and a TianoCore port has been done by HPE engineers and is expected to be upstreamed. A RISC-V boot deep dive was done as part of openSUSE Hackweek 20. There is a port of the seL4 microkernel with functional correctness, integrity and information flow properties formally verified. Hex Five released the first Secure IoT Stack for RISC-V with FreeRTOS support. Also xv6, a modern reimplementation of Sixth Edition Unix in ANSI C used for pedagogical purposes in MIT, was ported. Pharos RTOS has been ported to 64-bit RISC-V (including time and memory protection). *Also see* Comparison of real-time operating systems.

A simulator exists to run a RISC-V Linux system on a web browser using JavaScript.

QEMU supports running (using binary translation) 32- and 64-bit RISC-V systems (e.g. Linux) with many emulated or virtualized devices (serial, parallel, USB, network, storage, real time clock, watchdog, audio), as well as running RISC-V Linux binaries (translating syscalls to the host kernel). It does support multi-core emulation (SMP).

The CREATOR simulator is portable and allows the user to learn various assembly languages of different processors (CREATOR has examples with an implementation of RISC-V and MIPS32 instructions).

Several languages have been applied to creating RISC-V IP cores including a Scala-based hardware description language, Chisel, which can reduce the designs to Verilog for use in devices, and the CodAL processor description language which has been used in to describe RISC-V processor cores and to generate corresponding HDKs (RTL, testbench and UVM) and SDKs. The RISC-V International Compliance Task Group has a GitHub repository for RV32IMC.

The extensible educational simulator WepSIM implements a microprogrammed subset of RISC-V instructions (RV32I+M) and allows the execution of subroutines on both, at assembly and microprogramming level.


## Development tools

- IAR Systems released the first version of IAR Embedded Workbench for RISC-V, which supports RV32 32-bit RISC-V cores and extensions in the first version. Future releases will include 64-bit support and support for the smaller RV32E base instruction set, as well as functional safety certification and security solutions.
- Lauterbach added support for RISC-V to its TRACE32 JTAG debuggers. Lauterbach also announced support for SiFives RISC-V NEXUS based processor trace.
- SEGGER released a new product named "J-Trace PRO RISC-V", added support for RISC-V cores to its J-Link debugging probe family, their integrated development environment Embedded Studio, and their RTOS embOS and embedded software.
- UltraSOC Archived 22 September 2020 at the Wayback Machine, now part of Siemens, proposed a standard trace system and donated an implementation.
