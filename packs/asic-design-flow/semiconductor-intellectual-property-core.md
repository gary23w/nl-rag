---
title: "Semiconductor intellectual property core"
source: https://en.wikipedia.org/wiki/Semiconductor_intellectual_property_core
domain: asic-design-flow
license: CC-BY-SA-4.0
tags: asic design flow, chip tape-out, semiconductor ip core, eda sign-off
fetched: 2026-07-02
---

# Semiconductor intellectual property core

In electronic design, a **semiconductor intellectual property core** (**SIP core**), **IP core** or **IP block** is a reusable unit of logic, cell, or integrated circuit layout design that is the intellectual property of one party. IP cores can be licensed to another party or owned and used by a single party. The term comes from the licensing of the patent or source code copyright that exists in the design. Designers of system on chip (SoC), application-specific integrated circuits (ASIC) and systems of field-programmable gate array (FPGA) logic can use IP cores as building blocks. This allows for faster design cycles and reduced development costs by leveraging pre-verified and tested components.[2]

## History

The licensing and use of IP cores in chip design came into common practice in the 1990s. There were many licensors and also many foundries competing on the market. In 2013, the most widely licensed IP cores were from Arm Holdings (43.2% market share), Synopsys Inc. (13.9% market share), Imagination Technologies (9% market share) and Cadence Design Systems (5.1% market share).

## Types of IP cores

The use of an IP core in chip design is comparable to the use of a library for computer programming or a discrete integrated circuit component for printed circuit board design. Each is a reusable component of design logic with a defined interface and behavior that has been verified by its creator and is integrated into a larger design.

### Soft cores

IP cores are commonly offered as synthesizable RTL in a hardware description language such as Verilog or VHDL. These are analogous to low-level languages such as C in the field of computer programming. IP cores delivered to chip designers as RTL permit chip designers to modify designs at the functional level, though many IP vendors offer no warranty or support for modified designs.

IP cores are also sometimes offered as generic gate-level netlists. The netlist is a Boolean-algebra representation of the IP's logical function implemented as generic gates or process-specific standard cells. An IP core implemented as generic gates can be compiled for any process technology. A gate-level netlist is analogous to an assembly code listing in the field of computer programming. A netlist gives the IP core vendor reasonable protection against reverse engineering. See also Integrated circuit layout design protection.

Both netlist and synthesizable cores are called soft cores since both allow a synthesis, placement and routing (SPR) design flow.

### Hard cores

Hard cores (or hard macros) are analog or digital IP cores whose function cannot be significantly modified by chip designers. These are generally defined as a lower-level physical description that is specific to a particular process technology. Hard cores usually offer better predictability of chip timing performance and area for their particular technology.

Analog and mixed-signal logic are generally distributed as hard cores. Hence, analog IP (SerDes, PLLs, DAC, ADC, PHYs, etc.) are provided to chip makers in transistor-layout format (such as GDSII). Digital IP cores are sometimes offered in layout format as well.

Low-level transistor layouts must obey the target foundry's process design rules. Therefore, hard cores delivered for one foundry's process cannot be easily ported to a different process or foundry. Merchant foundry operators (such as IBM, Fujitsu, Samsung, TI, etc.) offer various hard-macro IP functions built for their own foundry processes, helping to ensure customer lock-in.

## Sources of IP cores

### Licensed functionality

Many of the best known IP cores are soft microprocessor designs. Their instruction sets vary from small 8-bit processors, such as the 8051 and PIC, to 32-bit and 64-bit processors such as the ARM architectures or RISC-V architectures. Such processors form the "brains" of many embedded systems. They are usually RISC instruction sets rather than CISC instruction sets like x86 because less logic is required. Therefore, designs are smaller. Further, x86 leaders Intel and AMD heavily protect their processor designs' intellectual property and don't use this business model for their x86-64 lines of microprocessors.

IP cores are also licensed for various peripheral controllers such as for PCI Express, SDRAM, Ethernet, LCD, AC'97 audio, IEEE 1394, AGP and USB. Many of those interfaces require both digital logic and analog IP cores to drive and receive high speed, high voltage, or high impedance signals outside of the chip.

"Hardwired" (as opposed to software programmable soft microprocessors described above) digital logic IP cores are also licensed for fixed functions such as MP3 audio decode, 3D GPU, digital video encode/decode, and other DSP functions such as FFT, DCT, or Viterbi coding.

### Vendors

IP core developers and licensors range in size from individuals to multi-billion-dollar corporations. Developers, as well as their chip-making customers, are located throughout the world.

*Silicon intellectual property* (*SIP*, *silicon IP*) is a business model for a semiconductor company where it licenses its technology to a customer as intellectual property. A company with such a business model is a fabless semiconductor company, which doesn't provide physical chips to its customers but merely facilitates the customer's development of chips by offering certain functional blocks. Typically, the customers are semiconductor companies or module developers with in-house semiconductor development. A company wishing to fabricate a complex device may license in the rights to use another company's well-tested functional blocks such as a microprocessor, instead of developing their own design, which would require additional time and cost.

The silicon IP industry has had stable growth for many years. The earliest silicon IP companies that were established in the 1990s and 2000s included Virtual Chips, Sand Microelectronics (both acquired by Phoenix Technologies), Integrated Intellectual Property (I2P) (acquired by Lattice Semiconductor) and Ingot Systems (acquired by Virage Logic). The silicon IP developed by these companies focused on standards such as PCI, USB, IEEE 1394 (Firewire), AGP and DDR3. In the recent times, the most successful silicon IP companies, often referred to as the *star IP*, include ARM Holdings and Synopsys. Gartner Group estimated the total value of sales related to silicon intellectual property at US $1.5 billion in 2005 with annual growth expected around 30%.

#### IP hardening

IP hardening is a process to re-use proven designs and generate fast time-to-market, low-risk-in-fabrication solutions to provide intellectual property (IP) (or silicon intellectual property) of design cores.

For example, a digital signal processor (DSP) is developed from soft cores of RTL format, and it can be targeted to various technologies or different foundries to yield different implementations. The process of IP hardening is from soft core to generate re-usable hard (hardware) cores. A main advantage of such hard IP is its predictable characteristics as the IP has been pre-implemented, while it offers flexibility of soft cores. It might come with a set of models for simulations for verification.

Hardening soft IP involves evaluating the quality of the target technology, the design goals, and the chosen methodology. Hard IP has already been verified for use in a specific technology and application. For example, a hard core in GDSII format is considered 'clean' if it passes DRC (Design rule checking) and LVS (Layout Versus Schematic). In other words, it meets all the manufacturing requirements set by the foundry.

### Free and open-source

Since around 2000, OpenCores.org has offered various soft cores, mostly written in VHDL and Verilog. All of these cores are provided under free and open-source software-license such as GNU General Public License or BSD-like licenses. Since 2010, initiatives such as RISC-V have caused a massive expansion in the number of IP cores available (almost 50 by 2019). This has helped to increase collaboration in developing secure and efficient designs.
