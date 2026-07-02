---
title: "Single-board computer"
source: https://en.wikipedia.org/wiki/Single-board_computer
domain: raspberry-pi
license: CC-BY-SA-4.0
tags: raspberry pi, raspberry pi os, raspbian, pi pico, rp2040
fetched: 2026-07-02
---

# Single-board computer

A **single-board computer** (**SBC**) is a complete computer built on a single circuit board, with microprocessor(s), memory, input/output (I/O) and other features required of a functional computer. Single-board computers are commonly made as demonstration or development systems, for educational systems, or for use as embedded computer controllers. Many types of home computers or portable computers integrate all their functions onto a single printed circuit board.

Unlike a desktop personal computer, single-board computers often do not rely on expansion slots for peripheral functions or expansion. Single-board computers have been built using a wide range of microprocessors. Simple designs, such as those built by computer hobbyists, often use static RAM and low-cost 32- or 64-bit processors like ARM. Other types, such as blade servers, would perform similar to a server computer, only in a more compact format.

A computer-on-module is a type of single-board computer made to plug into a carrier board, baseboard, or backplane for system expansion.

## History

It did not take long after the first microprocessors to arrive on the market before the first single-board computers arrived, for instance Intel's own SIM4-01 and SIM8-01 development boards from 1971 and 1972 respectively. The SIM8-01 board is based on the Intel 8008 and contains a CPU, RAM, ROM, and a TTY terminal interface. It features 1K byte of RAM in 32 P1101A chips and 2K bytes of EPROM in eight C1701 chips. The SIM8-01 has input and output capabilities in the form of a serial port for an external terminal, and it can be argued that this is the first true single-board computer in that sense. Following a similar concept with CPU/RAM/ROM and a terminal interface, there was the Intel 8080-based MYCRO-1 released in December 1974, and both the Intel SDK-80 and the Motorola MEK6800D1 of 1975. A cheaper and subsequently more popular single-board computer, the KIM-1 based on the MOS 6502, would be announced later in 1975 and released in 1976.

Early SBCs figured heavily in the early history of home computers, such as the Acorn Electron and the BBC Micro, also developed by Acorn. Other typical early single-board computers like the KIM-1 were often shipped without enclosure, which had to be added by the owner. Other early examples are the Ferguson Big Board, the Ampro Little Board, and the Nascom. Many home computers in the 1980s were single-board computers, with some even encouraging owners to solder upgraded components directly to pre-marked points on the board.

As the PC became more prevalent, SBCs decreased in market share due to their low extensibility. The rapid adoption of IBM's standards for peripherals and the standardization of the PCI bus in the 1990s made motherboards and compatible components and peripherals cheap and ubiquitous, while the development of multimedia platforms such as the CD-ROM and Sound Blaster cards had begun to fast outpace the rate at which users needed to replace their personal computers. These two trends disincentivized single-board computers, and instead encouraged the proliferation of motherboards, which typically housed the CPU and other core components, with peripheral components such as hard disk drive controllers and graphics processors, and even some core components such as RAM modules, located on daughterboards.

Computers began to move back towards fewer boards in the 2000s. As new standards like USB dramatically reduced the variety of peripheral standards motherboards were expected to support, advances in integrated circuit manufacturing provided new chipsets which could provide the functionality of many daughterboards, particularly I/O, in a single chip. By the end of the decade, PC motherboards offered on-board support for disk drives including IDE, SATA, NVMe, RAID, integrated GPU, Ethernet, and traditional I/O such as serial port and parallel port, USB, and keyboard/mouse support. Plug-in "cards" retained their importance as high performance components, such as physically large and complex graphics coprocessors, high-end RAID controllers, and specialized I/O cards such as data acquisition and DSP boards.

The 2010s were defined by rapid and sustained growth in single-board computers, enabled largely by advances in integrated circuit production techniques that made it possible for the first time to include most or all of the core components of a motherboard on a single integrated circuit die. One of the more well known single-board-computers of the decade was the Raspberry Pi, which was built around a custom Broadcom SoC with open-source drivers. Originally intended for education, the Raspberry Pi contained a number of features, such as optimized Linux support and programmable GPIO pins, that were also greatly appealing to hobbyists, who used the Pi, and other comparable SBCs, for projects such as home automation, video game emulation, media streaming, and other experimentation. In industry, the rapid growth of smartphones and other small-scale devices encouraged hardware manufacturers to move towards more frequent use of SoCs and the reduction of motherboards in size, extensibility and complexity, while the proliferation of the Internet of Things increased demand for small, cheap components that would allow unconventional devices to access the Internet. Both of these factors dramatically increased production of single-board computers throughout the decade.

By the end of the 2010s and the early 2020s, many devices, including smartphones, tablet computers, laptops and other smart devices, are powered by single-board computers which utilize advanced SoCs (System on a Chip). While this has greatly increased performance and power efficiency, it has raised concerns that single-board computers, particularly those built around SoCs, are harder to repair and may be less friendly to attempts to monitor or modify instructions programmed into the boards by manufacturers.

## Applications

Single-board computers were made possible by increasing the density of integrated circuits. A single-board configuration reduces a system's overall cost, by reducing the number of circuit boards required, and by eliminating connectors and bus driver circuits that would otherwise be used. By putting all the functions on one board, a smaller overall system can be obtained, for example, as in notebook computers. Connectors are a frequent source of reliability problems, so a single-board system eliminates these problems.

Single-board computers are now commonly defined across two distinct architectures: no slots and slot support.

Embedded SBCs are units providing all the required I/O with no provision for plug-in cards. Applications are typically gaming (slot machines, video poker), kiosk, and machine control automation. Embedded SBCs are much smaller than the ATX-type motherboard found in PCs, and provide an I/O mix more targeted to an industrial application, such as on-board digital and analog I/O, on-board bootable flash memory (eliminating the need for a disk drive), no video, etc.

The term *single-board computer* now generally applies to an architecture where the single-board computer is plugged into a backplane to provide for I/O cards. In the case of PC104, the bus is not a backplane in the traditional sense but is a series of pin connectors allowing I/O boards to be stacked.

Single-board computers are most commonly used in industrial situations where they are used in rackmount format for process control or embedded within other devices to provide control and interfacing. They are used in deep-sea exploration on the ALICE deep sea probes and in outer space, on the Ariane and Pegasus rockets and Space Shuttle. Because of the very high levels of integration, reduced component counts and reduced connector counts, SBCs are often smaller, lighter, more power efficient and more reliable than comparable multi-board computers.

The primary advantage of an ATX motherboard as compared to an SBC is cost. Motherboards are manufactured by the millions for the consumer and office markets allowing tremendous economies of scale. Single-board computers are a market niche and are manufactured less often and at a higher cost. Motherboards and SBCs now offer similar levels of feature integration meaning that a motherboard failure in either standard will require equivalent replacement.

## Types, standards

Ranges of single-board computers include Raspberry Pi, BeagleBoard, LattePanda, Nano Pi, ODROID, Orange Pi, PINE64, and Banana Pi.

One common variety of single-board computer uses standardized computer form factors intended for use in a backplane enclosure. Some of these types are CompactPCI, PXI, VMEbus, VXI, and PICMG. SBCs have been built around various internal processing structures including the Intel architecture, multiprocessing architectures, and lower power processing systems like RISC and SPARC. In the Intel PC world, the intelligence and interface/control circuitry is placed on a plug-in board that is then inserted into a passive (or active) backplane. The result is similar to having a system built with a motherboard, except that the backplane determines the slot configuration. Backplanes are available with a mix of slots (ISA, PCI, PCI-X, PCI-Express, etc.), usually totaling 20 or fewer, meaning it will fit in a 19" rackmount enclosure (17" wide chassis).

Some single-board computers have connectors that allow a stack of circuit boards, each containing expansion hardware, to be assembled without a traditional backplane. Examples of stacking SBC form factors include PC/104, PC/104-*Plus*, PCI-104, EPIC, and EBX; these systems are commonly available for use in embedded control systems.

Stack-type SBCs often have memory provided on plug-cards such as SIMMs and DIMMs. Hard drive circuit boards are also not counted for determining if a computer is an SBC or not for two reasons, firstly because the HDD is regarded as a single block storage unit, and secondly because the SBC may not require a hard drive at all as most can be booted from their network connections.

## Form factors

- AdvancedTCA
- CompactPCI
- Embedded Compact Extended (ECX)
- Mini-ITX
- Multibus
- PC/104
- PICMG
- Pico-ITX
- PXI
- Qseven
- VMEbus
- VPX
- VXI
- 96Boards (CE, EE, EETV and IE)
