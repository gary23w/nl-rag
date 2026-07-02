---
title: "Multi-chip module"
source: https://en.wikipedia.org/wiki/Multi-chip_module
domain: chiplet-architecture
license: CC-BY-SA-4.0
tags: chiplet architecture, multi-chip module, die-to-die interconnect, 2.5d integration
fetched: 2026-07-02
---

# Multi-chip module

A **multi-chip module** (**MCM**) is generically an electronic assembly (such as a package with a number of conductor terminals or "pins") where multiple integrated circuits (ICs or "chips"), semiconductor dice and/or other discrete components are integrated, usually onto a unifying substrate, so that in use it can be treated as if it were a larger IC. Other terms for MCM packaging include "heterogeneous integration" or "hybrid integrated circuit". The advantage of using MCM packaging is it allows a manufacturer to use multiple components for modularity and/or to improve yields over a conventional monolithic IC approach.

A **Flip Chip Multi-Chip Module** (**FCMCM**) is a multi-chip module that uses flip chip technology. A FCMCM may have one large die and several smaller dice all on the same module.

## Overview

Multi-chip modules come in a variety of forms depending on the complexity and development philosophies of their designers. These can range from using pre-packaged ICs on a small printed circuit board (PCB) meant to mimic the package footprint of an existing chip package to fully custom chip packages integrating many chip dies on a high density interconnection (HDI) substrate. The final assembled MCM substrate may be done in one of the following ways:

- The substrate is a multi-layer laminated printed circuit board (PCB), such as those used in AMD's Zen 2 processors.
- The substrate is built on ceramic, such as low temperature co-fired ceramic
- The ICs are deposited on the base substrate using Thin Film technology.

The ICs that make up the MCM package may be:

- ICs that can perform most, if not all of the functions of a component of a computer, such as the CPU. Examples of this include implementations of IBM's POWER5 and Intel's Core 2 Quad. Multiple copies of the same IC are used to build the final product. In the case of POWER5, multiple POWER5 processors and their associated off-die L3 cache are used to build the final package. With the Core 2 Quad, effectively two Core 2 Duo dies were packaged together.
- ICs that perform only some of the functions, or "Intellectual Property Blocks" ("IP Blocks"), of a component in a computer. These are known as chiplets. An example of this are the processing ICs and I/O IC of AMD's Zen 2-based processors.

An interposer connects the ICs. This is often either organic (a laminated circuit board that contains carbon, hence *organic*) or is made of silicon (as in High Bandwidth Memory). Each has advantages and limitations. Using interposers to connect several ICs instead of connecting several monolithic ICs in separate packages reduces the power needed to transmit signals between ICs, increases the number of transmission channels, and reduces delays caused by resistance and capacitance (RC delays). However, communication between chiplets consumes more power and has higher latency than components within monolithic ICs.

## Chip stack MCMs

A relatively new development in MCM technology is the so-called "chip-stack" package. Certain ICs, memories in particular, have very similar or identical pinouts when used multiple times within systems. A carefully designed substrate can allow these dies to be stacked in a vertical configuration making the resultant MCM's footprint much smaller (albeit at the cost of a thicker or taller chip). Since area is more often at a premium in miniature electronics designs, the chip-stack is an attractive option in many applications such as cell phones and personal digital assistants (PDAs). With the use of a 3D integrated circuit and a thinning process, as many as ten dies can be stacked to create a high capacity SD memory card. This technique can also be used for High Bandwidth Memory.

The possible way to increasing the performance of data transfer in the Chip stack is use Wireless Networks on Chip (WiNoC).

## Examples of multi-chip packages

- IBM Bubble memory MCMs (1970s)
- IBM 3081 mainframe's thermal conduction module (1980s)
- Superconducting Multichip modules (1990s)
- Intel Pentium Pro, Pentium II OverDrive, Pentium D Presler, Xeon Dempsey, Clovertown, Harpertown and Tigerton, Core 2 Quad (Kentsfield, Penryn-QC and Yorkfield), Clarkdale, Arrandale, Kaby Lake-G, and models with Crystalwell (those with the GT3e or GT4e graphics)
- SD cards, microSD cards and Sony memory sticks
- eMMC, eUFS, and NVMe with single-package solution
- Xenos, a GPU designed by ATI Technologies for the Xbox 360, with eDRAM
- POWER2, POWER4, POWER5, POWER7, POWER8, and Power10 from IBM
- IBM z196
- Nintendo's Wii U Espresso (microprocessor) has its CPU, GPU, and onboard VRAM (integrated into the GPU) on one MCM.
- VIA Nano QuadCore
- Flash and RAM memory combined on a PoP by Micron
- Samsung MCP solutions combining mobile DRAM and NAND storage.
- AMD Ryzen Threadripper and Epyc CPUs based on Zen or Zen+ architecture are MCMs of two or four chips (Ryzen based on Zen or Zen+ is not MCM and consist of one chip)
- AMD's non-APU Ryzen, Ryzen Threadripper and Epyc CPUs based on the Zen 2 or Zen 3 architecture are MCMs of one, two, four or eight chips containing CPU cores and one bigger I/O chip
- AMD Instinct MI series GPUs based on CDNA 2 architecture are MCMs of one or two graphics compute die (GCD) chips.
- AMD Radeon RX 7000 series GPUs based on RDNA 3 architecture are MCMs with one GCD and up to six memory cache die (MCD) chips.
- Intel Xe Ponte Vecchio GPUs
- Intel Meteor Lake CPUs
- Intel Arrow Lake CPUs
- Any other processor with High Bandwidth Memory
- Apple M series with CPU and memory
- Intel Lunar Lake with CPU and memory

## 3D multi-chip modules
