---
title: "Arm architecture family (part 1/2)"
source: https://en.wikipedia.org/wiki/ARM_architecture_family
domain: pointer-authentication
license: CC-BY-SA-4.0
tags: pointer authentication code, cryptographic pointer signing, return address tampering defense, arm memory protection
fetched: 2026-07-02
part: 1/2
---

# Arm architecture family

(Redirected from

ARM architecture family

)

**Arm** (stylised in lowercase as **arm**) is a family of RISC instruction set architectures for computer processors. Arm Holdings develops the instruction set architecture and licenses them to other companies, who build the physical devices that use the instruction set. It also designs and licenses cores that implement these instruction set architectures.

Due to their low costs, low power consumption, and low heat generation, ARM processors are useful for light, portable, battery-powered devices, including smartphones, laptops, and tablet computers, as well as embedded systems. However, ARM processors are also used for desktops and servers, including Fugaku, the world's fastest supercomputer from 2020 to 2022. With over 230 billion ARM chips produced, since at least 2003, and with its dominance increasing every year, ARM is the most widely used family of instruction set architectures.

There have been several generations of the ARM design. The original ARM1 used a 32-bit internal structure but had a 26-bit address space that limited it to 64 MB of main memory. This limitation was removed in the ARMv3 series, which has a 32-bit address space, and several additional generations up to ARMv7 remained 32-bit. Released in 2011, the ARMv8-A architecture added support for a 64-bit address space and 64-bit arithmetic with its new 32-bit fixed-length instruction set. Arm Holdings has also released a series of additional instruction sets for different roles: the "Thumb" extensions add both 32- and 16-bit instructions for improved code density, while Jazelle added instructions for directly handling Java bytecode. More recent changes include the addition of simultaneous multithreading (SMT) for improved performance or fault tolerance.


## History

### BBC Micro

Acorn Computers' first widely successful design was the BBC Micro, introduced in December 1981. This was a relatively conventional machine based on the MOS Technology 6502 CPU but ran at roughly double the performance of competing designs like the Apple II due to its use of faster dynamic random-access memory (DRAM). Typical DRAM of the era ran at about 2 MHz; Acorn arranged a deal with Hitachi for a supply of faster 4 MHz parts.

Machines of the era generally shared memory between the processor and the framebuffer, which allowed the processor to quickly update the contents of the screen without having to perform separate input/output (I/O). As the timing of the video display is exacting, the video hardware had to have priority access to that memory. Due to a quirk of the 6502's design, the CPU left the memory untouched for half of the time. Thus by running the CPU at 1 MHz, the video system could read data during those down times, taking up the total 2 MHz bandwidth of the RAM. In the BBC Micro, the use of 4 MHz RAM allowed the same technique to be used, but running at twice the speed. This allowed it to outperform any similar machine on the market.

### Acorn Business Computer

1981 was also the year that the IBM Personal Computer was introduced. Using the recently introduced Intel 8088, a 16-bit CPU compared to the 6502's 8-bit design, it offered higher overall performance. Its introduction changed the desktop computer market radically: what had been largely a hobby and gaming market emerging over the prior five years began to change to a must-have business tool where the earlier 8-bit designs simply could not compete. Even newer 32-bit designs were also coming to market, such as the Motorola 68000 and National Semiconductor NS32016.

Acorn began considering how to compete in this market and produced a new paper design named the Acorn Business Computer. They set themselves the goal of producing a machine with ten times the performance of the BBC Micro, but at the same price. This would outperform and underprice the PC. At the same time, the recent introduction of the Apple Lisa brought the graphical user interface (GUI) concept to a wider audience and suggested the future belonged to machines with a GUI. The Lisa, however, cost $9,995, as it was packed with support chips, large amounts of memory, and a hard disk drive, all very expensive then.

The engineers then began studying all of the CPU designs available. Their conclusion about the existing 16-bit designs was that they were a lot more expensive and were still "a bit crap", offering only slightly higher performance than their BBC Micro design. They also almost always demanded a large number of support chips to operate even at that level, which drove up the cost of the computer as a whole. These systems would simply not hit the design goal. They also considered the new 32-bit designs, but these cost even more and had the same issues with support chips. According to Sophie Wilson, all the processors tested at that time performed about the same, with about a 4 Mbit/s bandwidth.

Two key events led Acorn down the path to ARM. One was the publication of a series of reports from the University of California, Berkeley, which suggested that a simple chip design could nevertheless have extremely high performance, much higher than the latest 32-bit designs on the market. The second was a visit by Steve Furber and Sophie Wilson to the Western Design Center, a company run by Bill Mensch and his sister Kathryn, which had become the logical successor to the MOS team and was offering new versions like the WDC 65C02. The Acorn team saw high school students producing chip layouts on Apple II machines, which suggested that anyone could do it. In contrast, a visit to another design firm working on modern 32-bit CPU revealed a team with over a dozen members who were already on revision H of their design and yet it still contained bugs. This cemented their late 1983 decision to begin their own CPU design, the Acorn RISC Machine.

### Design concepts

The original Berkeley RISC designs were in some sense teaching systems, not designed specifically for outright performance. To the RISC's basic register-heavy and load/store concepts, ARM added a number of the well-received design notes of the 6502. Primary among them was the ability to quickly service interrupts, which allowed the machines to offer reasonable input/output performance with no added external hardware. To offer interrupts with similar performance as the 6502, the ARM design limited its physical address space to 64 MB of total addressable space, requiring 26 bits of address. As instructions were 4 bytes (32 bits) long, and required to be aligned on 4-byte boundaries, the lower 2 bits of an instruction address were always zero. This meant the program counter (PC) only needed to be 24 bits, allowing it to be stored along with the eight bit processor flags in a single 32-bit register. That meant that upon receiving an interrupt, the entire machine state could be saved in a single operation, whereas had the PC been a full 32-bit value, it would require separate operations to store the PC and the status flags. This decision halved the interrupt overhead.

Another change, and among the most important in terms of practical real-world performance, was the modification of the instruction set to take advantage of page mode DRAM. Recently introduced, page mode allowed subsequent accesses of memory to run twice as fast if they were roughly in the same location, or "page", in the DRAM chip. Berkeley's design did not consider page mode and treated all memory equally. The ARM design added special vector-like memory access instructions, the "S-cycles", that could be used to fill or save multiple registers in a single page using page mode. This doubled memory performance when they could be used, and was especially important for graphics performance.

The Berkeley RISC designs used register windows to reduce the number of register saves and restores performed in procedure calls; the ARM design did not adopt this.

Wilson developed the instruction set, writing a simulation of the processor in BBC BASIC that ran on a BBC Micro with a second 6502 processor. This convinced Acorn engineers they were on the right track. Wilson approached Acorn's CEO, Hermann Hauser, and requested more resources. Hauser gave his approval and assembled a small team to design the actual processor based on Wilson's instruction set architecture. The official Acorn RISC Machine project started in October 1983.

### ARM1

Acorn chose VLSI Technology as the "silicon partner", as they were a source of ROMs and custom chips for Acorn. Acorn provided the design and VLSI provided the layout and production. The first samples of ARM silicon worked properly when first received and tested on 26 April 1985. Known as ARM1, these versions ran at 6 MHz.

The first ARM application was as a second processor for the BBC Micro, where it helped in developing simulation software to finish development of the support chips (VIDC, IOC, MEMC), and sped up the CAD software used in ARM2 development. Wilson subsequently rewrote BBC BASIC in ARM assembly language. The in-depth knowledge gained from designing the instruction set enabled the code to be very dense, making ARM BBC BASIC an extremely good test for any ARM emulator.

ARM Evaluations Systems featuring ARM1 CPUs and supplied as second processors for BBC Micro and Master machines, were made available from July 1986 under the Acorn OEM Products brand to developers and researchers.

The A500 Second Processor, an additional ARM1 based BBC Micro and Master second processor, featured the ARM support chipset (VIDC, IOC, MEMC), was capable of producing video output and operating near independently of the host BBC Micro.

### ARM2

The result of the simulations on the ARM1 boards led to the late 1986 introduction of the ARM2 design running at 8 MHz, and the early 1987 speed-bumped version at 10 to 12 MHz. A significant change in the underlying architecture was the addition of a Booth multiplier, whereas formerly multiplication had to be carried out in software. Further, a new Fast Interrupt reQuest mode, FIQ for short, allowed registers 8 to 14 to be replaced as part of the interrupt itself. This meant FIQ requests did not have to save out their registers, further speeding interrupts.

The first use of the ARM2 was in internal Acorn A500 development machines, and the Acorn Archimedes personal computer models A305, A310, and A440, launched on the 6th June 1987.

According to the Dhrystone benchmark, the ARM2 was roughly seven times the performance of a typical 7 MHz 68000-based system like the Amiga or Macintosh SE. It was twice as fast as an Intel 80386 running at 16 MHz, and about the same speed as a multi-processor VAX-11/784 superminicomputer. The only systems that beat it were the Sun SPARC and MIPS R2000 RISC-based workstations. Further, as the CPU was designed for high-speed I/O, it dispensed with many of the support chips seen in these machines; notably, it lacked any dedicated direct memory access (DMA) controller which was often found on workstations. The graphics system was also simplified based on the same set of underlying assumptions about memory and timing. The result was a dramatically simplified design, offering performance on par with expensive workstations but at a price point similar to contemporary desktops.

The ARM2 featured a 32-bit data bus, 26-bit address space and 27 32-bit registers, of which 16 are accessible at any one time (including the PC). The ARM2 had a transistor count of just 30,000, compared to Motorola's six-year-older 68000 model with around 68,000. Much of this simplicity came from the lack of microcode, which represents about one-quarter to one-third of the 68000's transistors, and the lack of (like most CPUs of the day) a cache. This simplicity enabled the ARM2 to have a low power consumption and simpler thermal packaging by having fewer powered transistors. Nevertheless, ARM2 offered better performance than the contemporary 1987 IBM PS/2 Model 50, which initially utilised an Intel 80286, offering 1.8 MIPS @ 10 MHz, and later in 1987, the 2 MIPS of the PS/2 70, with its Intel 386 DX @ 16 MHz.

A successor, ARM3, was produced with a 4 KB cache, which further improved performance. The address bus was extended to 32 bits in the ARM6, but program code still had to lie within the first 64 MB of memory in 26-bit compatibility mode, due to the reserved bits for the status flags.

In 1988, Sanyo became a worldwide second source for the ARM2 and associated chipset under an agreement with VLSI Technology.

### Advanced RISC Machines Ltd. – ARM6

In the late 1980s, Apple Computer and VLSI Technology started working with Acorn on newer versions of the ARM core. In 1990, Acorn spun off the design team into a new company named Advanced RISC Machines Ltd., which became ARM Ltd. when its parent company, Arm Holdings plc, floated on the London Stock Exchange and Nasdaq in 1998. The new Apple–ARM work would eventually evolve into the ARM6, first released in early 1992. Apple used the ARM6-based ARM610 as the basis for their Apple Newton PDA.

### Early licensees

In 1994, Acorn used the ARM610 as the main central processing unit (CPU) in their RiscPC computers. DEC licensed the ARMv4 architecture and produced the StrongARM. At 233 MHz, this CPU drew only one watt (newer versions draw far less). This work was later passed to Intel as part of a lawsuit settlement, and Intel took the opportunity to supplement their i960 line with the StrongARM. Intel later developed its own high performance implementation named XScale, which it has since sold to Marvell. Transistor count of the ARM core remained essentially the same throughout these changes; ARM2 had 30,000 transistors, while ARM6 grew only to 35,000.

In 2005, about 98% of all mobile phones sold used at least one ARM processor. In 2010, producers of chips based on ARM architectures reported shipments of 6.1 billion ARM-based processors, representing 95% of smartphones, 35% of digital televisions and set-top boxes, and 10% of mobile computers. In 2011, the 32-bit ARM architecture was the most widely used architecture in mobile devices and the most popular 32-bit one in embedded systems. In 2013, 10 billion were produced and "ARM-based chips are found in nearly 60 percent of the world's mobile devices".


## Licensing

### Core licence

Arm Holdings's primary business is selling IP cores, which licensees use to create microcontrollers (MCUs), CPUs, and systems-on-chips based on those cores. The original design manufacturer combines the ARM core with other parts to produce a complete device, typically one that can be built in existing semiconductor fabrication plants (fabs) at low cost and still deliver substantial performance. The most successful implementation has been the ARM7TDMI with hundreds of millions sold. Atmel has been a precursor design center in the ARM7TDMI-based embedded system.

The ARM architectures used in smartphones, PDAs and other mobile devices range from ARMv5 to ARMv8-A.

In 2009, some manufacturers introduced netbooks based on ARM architecture CPUs, in direct competition with netbooks based on Intel Atom.

Arm Holdings offers a variety of licensing terms, varying in cost and deliverables. Arm Holdings provides to all licensees an integratable hardware description of the ARM core as well as complete software development toolset (compiler, debugger, software development kit), and the right to sell manufactured silicon containing the ARM CPU.

SoC packages integrating ARM's core designs include Nvidia Tegra's first three generations, CSR plc's Quatro family, ST-Ericsson's Nova and NovaThor, Silicon Labs's Precision32 MCU, Texas Instruments's OMAP products, Samsung's Hummingbird and Exynos products, Apple's A4, A5, and A5X, and NXP's i.MX.

Fabless licensees, who wish to integrate an ARM core into their own chip design, are usually only interested in acquiring a ready-to-manufacture verified semiconductor intellectual property core. For these customers, Arm Holdings delivers a gate netlist description of the chosen ARM core, along with an abstracted simulation model and test programs to aid design integration and verification. More ambitious customers, including integrated device manufacturers (IDM) and foundry operators, choose to acquire the processor IP in synthesizable RTL (Verilog) form. With the synthesizable RTL, the customer has the ability to perform architectural level optimisations and extensions. This allows the designer to achieve exotic design goals not otherwise possible with an unmodified netlist (high clock speed, very low power consumption, instruction set extensions, etc.). While Arm Holdings does not grant the licensee the right to resell the ARM architecture itself, licensees may freely sell manufactured products such as chip devices, evaluation boards and complete systems. Merchant foundries can be a special case; not only are they allowed to sell finished silicon containing ARM cores, they generally hold the right to re-manufacture ARM cores for other customers.

Arm Holdings prices its IP based on perceived value. Lower performing ARM cores typically have lower licence costs than higher performing cores. In implementation terms, a synthesisable core costs more than a hard macro (blackbox) core. Complicating price matters, a merchant foundry that holds an ARM licence, such as Samsung or Fujitsu, can offer fab customers reduced licensing costs. In exchange for acquiring the ARM core through the foundry's in-house design services, the customer can reduce or eliminate payment of ARM's upfront licence fee.

Compared to dedicated semiconductor foundries (such as TSMC and UMC) without in-house design services, Fujitsu/Samsung charge two- to three-times more per manufactured wafer. For low to mid volume applications, a design service foundry offers lower overall pricing (through subsidisation of the licence fee). For high volume mass-produced parts, the long term cost reduction achievable through lower wafer pricing reduces the impact of ARM's NRE (non-recurring engineering) costs, making the dedicated foundry a better choice.

Companies that have developed chips with cores designed by Arm include Amazon.com's Annapurna Labs subsidiary, Analog Devices, Apple, AppliedMicro (now: MACOM Technology Solutions), Atmel, Broadcom, Cavium, Cypress Semiconductor, Freescale Semiconductor (now NXP Semiconductors), Huawei, Intel, Maxim Integrated, Nvidia, NXP, Qualcomm, Renesas, Samsung Electronics, ST Microelectronics, Texas Instruments, and Xilinx.

### Built on ARM Cortex Technology licence

In February 2016, ARM announced the Built on ARM Cortex Technology licence, often shortened to Built on Cortex (BoC) licence. This licence allows companies to partner with ARM and make modifications to ARM Cortex designs. These design modifications will not be shared with other companies. These semi-custom core designs also have brand freedom, for example Kryo 280.

Companies that are current licensees of Built on ARM Cortex Technology include Qualcomm.

### Architectural licence

Companies can also obtain an ARM *architectural licence* for designing their own CPU cores using the ARM instruction sets. These cores must comply fully with the ARM architecture. Companies that have designed cores that implement an ARM architecture include Apple, AppliedMicro (now: Ampere Computing), Broadcom, Cavium (now: Marvell), Digital Equipment Corporation, Intel, Nvidia, Qualcomm, Samsung Electronics, Fujitsu, and NUVIA Inc. (acquired by Qualcomm in 2021).

### ARM Flexible Access

On 16 July 2019, ARM announced ARM Flexible Access. ARM Flexible Access provides unlimited access to included ARM intellectual property (IP) for development. Per product licence fees are required once a customer reaches foundry tapeout or prototyping.

75% of ARM's most recent IP over the last two years are included in ARM Flexible Access. As of October 2019:

- CPUs: Cortex-A5, Cortex-A7, Cortex-A32, Cortex-A34, Cortex-A35, Cortex-A53, Cortex-R5, Cortex-R8, Cortex-R52, Cortex-M0, Cortex-M0+, Cortex-M3, Cortex-M4, Cortex-M7, Cortex-M23, Cortex-M33
- GPUs: Mali-G52, Mali-G31. Includes Mali Driver Development Kits (DDK).
- Interconnect: CoreLink NIC-400, CoreLink NIC-450, CoreLink CCI-400, CoreLink CCI-500, CoreLink CCI-550, ADB-400 AMBA, XHB-400 AXI-AHB
- System Controllers: CoreLink GIC-400, CoreLink GIC-500, PL192 VIC, BP141 TrustZone Memory Wrapper, CoreLink TZC-400, CoreLink L2C-310, CoreLink MMU-500, BP140 Memory Interface
- Security IP: CryptoCell-312, CryptoCell-712, TrustZone True Random Number Generator
- Peripheral Controllers: PL011 UART, PL022 SPI, PL031 RTC
- Debug & Trace: CoreSight SoC-400, CoreSight SDC-600, CoreSight STM-500, CoreSight System Trace Macrocell, CoreSight Trace Memory Controller
- Design Kits: Corstone-101, Corstone-201
- Physical IP: Artisan PIK for Cortex-M33 TSMC 22ULL including memory compilers, logic libraries, GPIOs and documentation
- Tools & Materials: Socrates IP ToolingARM Design Studio, Virtual System Models
- Support: Standard ARM Technical support, ARM online training, maintenance updates, credits toward onsite training and design reviews


## Cores

| Architecture | Core bit-width | Cores | Profile | Ref. |   |
|---|---|---|---|---|---|
| Arm Ltd. | Third-party |   |   |   |   |
| ARMv1 | 32 | ARM1 |   | Classic |   |
| ARMv2 | 32 | ARM2, ARM250, ARM3 | Amber, STORM Open Soft Core | Classic |   |
| ARMv3 | 32 | ARM6, ARM7 |   | Classic |   |
| ARMv4 | 32 | ARM8 | StrongARM, FA526, ZAP Open Source Processor Core | Classic |   |
| ARMv4T | 32 | ARM7TDMI, ARM9TDMI, SecurCore SC100 |   | Classic |   |
| ARMv5TE | 32 | ARM7EJ, ARM9E, ARM10E | XScale, FA626TE, Feroceon, PJ1/Mohawk | Classic |   |
| ARMv6 | 32 | ARM11 |   | Classic |   |
| ARMv6-M | 32 | ARM Cortex-M0, ARM Cortex-M0+, ARM Cortex-M1, SecurCore SC000 |   | Microcontroller |   |
| ARMv7-M | 32 | ARM Cortex-M3, SecurCore SC300 | Apple M7 motion coprocessor | Microcontroller |   |
| ARMv7E-M | 32 | ARM Cortex-M4, ARM Cortex-M7 |   | Microcontroller |   |
| ARMv8-M | 32 | ARM Cortex-M23, ARM Cortex-M33 |   | Microcontroller |   |
| ARMv8.1-M | 32 | ARM Cortex-M55, ARM Cortex-M85 |   | Microcontroller |   |
| ARMv7-R | 32 | ARM Cortex-R4, ARM Cortex-R5, ARM Cortex-R7, ARM Cortex-R8 |   | Real-time |   |
| ARMv8-R | 32 | ARM Cortex-R52 |   | Real-time |   |
| 64 | ARM Cortex-R82 |   | Real-time |   |   |
| ARMv7-A | 32 | ARM Cortex-A5, ARM Cortex-A7, ARM Cortex-A8, ARM Cortex-A9, ARM Cortex-A12, ARM Cortex-A15, ARM Cortex-A17 | Qualcomm Scorpion/Krait, PJ4/Sheeva, Apple Swift (A6, A6X) | Application |   |
| ARMv8-A | 32 | ARM Cortex-A32 |   | Application |   |
| 64/32 | ARM Cortex-A35, ARM Cortex-A53, ARM Cortex-A57, ARM Cortex-A72, ARM Cortex-A73 | X-Gene, Nvidia Denver 1/2, Cavium ThunderX, AMD K12, Apple Cyclone (A7)/Typhoon (A8, A8X)/Twister (A9, A9X)/Hurricane+Zephyr (A10, A10X), Qualcomm Kryo, Samsung M1/M2 ("Mongoose") /M3 ("Meerkat") | Application |   |   |
| 64 | ARM Cortex-A34 |   | Application |   |   |
| ARMv8.1-A | 64/32 |   | Cavium ThunderX2 | Application |   |
| ARMv8.2-A | 64/32 | ARM Cortex-A55, ARM Cortex-A75, ARM Cortex-A76, ARM Cortex-A77, ARM Cortex-A78, ARM Cortex-X1, ARM Neoverse N1 | Nvidia Carmel, Samsung M4 ("Cheetah"), Fujitsu A64FX (ARMv8 SVE 512-bit) | Application |   |
| 64 | ARM Cortex-A65, ARM Neoverse E1 with simultaneous multithreading (SMT), ARM Cortex-A65AE (also having e.g. ARMv8.4 Dot Product; made for safety critical tasks such as advanced driver-assistance systems (ADAS)) | Apple Monsoon+Mistral (A11) (September 2017) | Application |   |   |
| ARMv8.3-A | 64/32 |   |   | Application |   |
| 64 |   | Apple Vortex+Tempest (A12, A12X, A12Z), Marvell ThunderX3 (v8.3+) | Application |   |   |
| ARMv8.4-A | 64/32 |   |   | Application |   |
| 64 | ARM Neoverse V1 | Apple Lightning+Thunder (A13), Apple Firestorm+Icestorm (A14, M1) | Application |   |   |
| ARMv8.5-A | 64/32 |   |   | Application |   |
| 64 |   |   | Application |   |   |
| ARMv8.6-A | 64 |   | Apple Avalanche+Blizzard (A15, M2), Apple Everest+Sawtooth (A16), Apple Coll (A17), Apple Ibiza/Lobos/Palma (M3) | Application |   |
| ARMv8.7-A | 64 |   |   | Application |   |
| ARMv8.8-A | 64 |   |   | Application |   |
| ARMv8.9-A | 64 |   |   | Application |   |
| ARMv9.0-A | 32/64 | ARM Cortex-A510 (A510 r1 / 2024 Refresh) |   | Application |   |
| 64 | ARM Cortex-A510, ARM Cortex-A710, ARM Cortex-A715, ARM Cortex-X2, ARM Cortex-X3, ARM Neoverse E2, ARM Neoverse N2, ARM Neoverse V2 |   | Application |   |   |
| ARMv9.1-A | 64 |   |   | Application |   |
| ARMv9.2-A | 64 | ARM Cortex-A520, ARM Cortex-A720, ARM Cortex-X4, ARM Neoverse V3, ARM Cortex-X925, ARM Cortex-A320 | Apple Donan/BravaChop/Brava (Apple M4), Apple Tupai/Tahiti (A18) | Application |   |
| ARMv9.3-A | 64 | TBA |   | Application |   |
| ARMv9.4-A | 64 | TBA |   | Application |   |
| ARMv9.5-A | 64 | TBA |   | Application |   |
| ARMv9.6-A | 64 | TBA |   | Application |   |
| ARMv9.7-A | 64 | TBA |   | Application |   |

1. Although most datapaths and CPU registers in the early ARM processors were 32-bit, addressable memory was limited to 26 bits; with upper bits, then, used for status flags in the program counter register.
2. ARMv3 included a compatibility mode to support the 26-bit addresses of earlier versions of the architecture. This compatibility mode is *optional* in ARMv4, and removed entirely in ARMv5.

Arm provides a list of vendors who implement ARM cores in their design (application specific standard products (ASSP), microprocessor and microcontrollers).

### Example applications of ARM cores

ARM cores are used in a number of products, particularly PDAs and smartphones. Some computing examples are Microsoft's first generation Surface, Surface 2 and Pocket PC devices (following 2002), Apple's iPads, and Asus's Eee Pad Transformer tablet computers, and several Chromebook laptops. Others include Apple's iPhone smartphones and iPod portable media players, Canon PowerShot digital cameras, Nintendo Switch hybrid, the Wii security processor and 3DS handheld game consoles, and TomTom turn-by-turn navigation systems.

In 2005, Arm took part in the development of Manchester University's computer SpiNNaker, which used ARM cores to simulate the human brain.

ARM chips are also used in Raspberry Pi, BeagleBoard, BeagleBone, PandaBoard, and other single-board computers, because they are very small, inexpensive, and consume very little power.
