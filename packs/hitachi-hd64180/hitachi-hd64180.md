---
title: "Hitachi HD64180"
source: https://en.wikipedia.org/wiki/Hitachi_HD64180
domain: hitachi-hd64180
license: CC-BY-SA-4.0
tags: hitachi hd64180, embedded systems
fetched: 2026-07-02
---

# Hitachi HD64180

The **HD64180** is a Z80-based embedded microprocessor developed by Hitachi with an integrated memory management unit (MMU) and on-chip peripherals. It appeared in 1985. The Hitachi HD64180 "Super Z80" was later licensed to Zilog and sold by them as the Z64180 and with some enhancements as the Zilog Z180.

## Overview

The HD64180 has the following features:

- Execution and bus access clock rates up to 10 MHz.
- Memory Management Unit supporting 512K bytes of memory (one megabyte for the HD64180 packaged in a PLCC)
- I/O space of 64K addresses
- 12 new instructions including 8 bit by 8 bit integer multiply, non-destructive AND and illegal instruction trap vector
- Two channel Direct Memory Access Controller (DMAC)
- Programmable wait state generator
- Programmable DRAM refresh
- Two channel Asynchronous Serial Communication Interface (ASCI)
- Two channel 16-bit Programmable Reload Timer (PRT)
- 1-channel Clocked Serial I/O Port (CSI/O)
- Programmable Vectored Interrupt Controller

The HD64180 has a pipelined execution unit which processes most instructions in fewer clock cycles than the Z80. The most improved instruction group comprises the block instructions; for example those such as LDIR, CPIR, INIR and OTDR. This instruction type takes 21 transition states to execute per iteration; on the HD64180 it takes 14 t-states.

The on-chip DMAC makes block memory transfers possible at a rate faster than the LDIR/LDDR instructions. The on-chip generator for wait states makes it possible to access too-slow hardware on a selective basis using a device filter, as is done for the TRS-80 Model 4's balky keyboard. The on-chip ASCI makes it possible to implement additional RS-232 serial ports.

The HD64180 will not execute the "undocumented" Z80 instructions, particularly the ones that access the index registers IX and IY as 8-bit halves. The Hitachi CPU treats them as illegal instructions and accordingly executes the "illegal instruction trap" behavior of resetting the PC register to zero, which simulates a cold restart by redirecting execution to the power-up location.

## Usage

The Micromint SB180, SemiDisk Systems DT42 CP/M computers, and Olivetti CWP 1 and ETV 210s videotypewriters (also running ROM-based CP/M 2.2) were based on the Hitachi HD64180. The XLR8er upgrade board for the TRS-80 Model 4 also used it. On the Victor HC-90 and HC-95 MSX2 computer, the HD64B180 was used for its turbo mode next to the regular Z80.
