---
title: "ARC (specification)"
source: https://en.wikipedia.org/wiki/ARC_(specification)
domain: fwupd
license: CC-BY-SA-4.0
tags: fwupd, embedded systems
fetched: 2026-07-02
---

# ARC (specification)

**Advanced RISC Computing** (**ARC**) is a specification created by a defunct consortium of computer manufacturers (the Advanced Computing Environment project), setting forth a standard MIPS RISC-based computer hardware and firmware environment. The firmware on Alpha machines that are compatible with ARC is known as **AlphaBIOS**, non-ARC firmware on Alpha is known as SRM.

## History

Although ACE went defunct, and no computer was ever manufactured which fully complied with the ARC standard, the ARC system has a widespread legacy in that all operating systems in the Windows NT family use ARC conventions for naming boot devices. SGI's modified version of the ARC firmware is named ARCS. All SGI computers which run IRIX 6.1 or later, such as the Indy and Octane, boot from an ARCS console, which uses the same drive naming conventions as Windows. Most of the various RISC-based computers designed to run Windows NT have versions of the ARC boot console to boot NT. These include the following:

- MIPS R4000-based systems such as the MIPS Magnum workstation
- all Alpha-based machines with a PCI bus designed prior to the end of support for Windows NT Alpha in September 1999 (the Alpha ARC firmware is also known as AlphaBIOS; non-ARC Alphas use SRM console instead)
- most Windows NT-capable PowerPC computers (such as the IBM RS/6000 40P).

It was predicted that Intel IA-32-based computers would adopt the ARC console, although only SGI ever marketed such machines with ARC firmware (namely, the SGI Visual Workstation series, which launched in 1999).

## Comparison with UEFI

Compared to UEFI, the ARC firmware also included support for FAT, boot variables, C-calling interface. It did not include the same level of extensibility as UEFI and the same level of governance like with the UEFI Forum.

## List of partially ARC compatible computers

Products complying (to some degree) with the ARC standard include these:

- Alpha
  - DEC Multia and AlphaStation/AlphaServer
  - DeskStation Raptor
- i386
  - SGI Visual Workstation
- MIPS
  - Acer PICA
  - Carrera Computers, Inc Cobra R4000 and VIPER
  - Digital DECstation 5000
  - DeskStation Tyne
  - Microsoft Jazz
  - MIPS Magnum
  - Olivetti M700
  - NEC RISCstation
  - NeTpower Fastseries MP
  - SGI Indigo², Indy, Challenge, Onyx, Origin etc. Big-Endian ARCS
  - Siemens-Nixdorf RM200, RM300, RM400
- PowerPC
  - IBM Personal Computer Power Series 850/830 PReP
  - IBM RS/6000 40P, 43P, E20, F30
  - Motorola PowerStack
  - Tangent MediaStar
