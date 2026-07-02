---
title: "μClinux"
source: https://en.wikipedia.org/wiki/%CE%9CClinux
domain: freertos
license: CC-BY-SA-4.0 / MIT (FreeRTOS docs)
tags: freertos, zephyr, task scheduler, embedded os
fetched: 2026-07-02
---

# μClinux

**μClinux** is a variation of the Linux kernel, previously maintained as a fork, that targets microcontrollers without a memory management unit (MMU). It was integrated into the mainline kernel as of 2.5.46 (2002) in the form of a NOMMU option.

After the mainline merge, the μClinux project continued to develop patches and tools for microcontrollers. The last Wayback Machine archive of the homepage (from 2018) lists Linux kernel releases for 2.0, 2.4 and 2.6 (all of which are end-of-life in mainline, 2.6 being the last to go in 2016), with the last news entry dated May 2016 concerning a new release of the kernel distribution. The website remained unchanged through 2021, when it went offline.

The letters "μC" are for "microcontroller": the name is pronounced "you-see-Linux", rather than pronouncing the letter mu as in Greek.

## History

μClinux was originally created by D. Jeff Dionne and Kenneth Albanowski in 1998. Initially, they targeted the Motorola DragonBall family of embedded 68k processors (specifically the 68EZ328 series used in the 3Com PalmPilot) on a 2.0.33 Linux kernel. After releasing their initial work, a developer community quickly sprang up extending their work to newer kernels and other microprocessor architectures. In early 1999, support was added for the Motorola (now NXP) ColdFire family of embedded microprocessors. ARM processor support was added later.

Although originally targeting 2.0 series Linux kernels, it now has ports based on Linux 2.4 and Linux 2.6. The Linux 2.4 ports were forward ported from the 2.0.36 Linux kernel by Michael Leslie and Evan Stawnyczy during their work at Rt-Control. There were never any μClinux extensions applied to the 2.2 series kernels.

Since version 2.5.46 of the Linux kernel, the major parts of μClinux have been integrated with the mainline kernel for a number of processor architectures.

Greg Ungerer (who originally ported μClinux to the Motorola ColdFire family of processors) continued to maintain and actively push core μClinux support into the 2.6 series Linux kernels. In this regard, μClinux is essentially no longer a separate fork of Linux.

μClinux had support for many architectures, and forms the basis of many products, like network routers, security cameras, DVD or MP3 players, VoIP phone or gateways, scanners, and card readers.

### 2010s

The volume of mails on the μClinux mailing list greatly decreased in the 2010s, with very few months producing more than 100 KB of mail in total.

View

chart definition

.

The Linux kernel upstream marked version 2.6 as end-of-life in February 2016. The last "uclinux-dist", a distribution package containing the source code of the patched kernel, was released on SourceForge September 2016. It contained not only 2.6 but also those based on newer upstream versions 3.x and 4.x. The last update of most tools on SourceForge also date back to February and September 2016.

Support for several of the original target architectures was dropped in April 2018 by the Linux upstream. The obsolete CPU architectures set to be removed in Linux 4.17 and subsequent releases included ADI Blackfin, Etrax CRIS, Fujitsu FR-V, Mitsubishi M32R, Matsushita/Panasonic MN10300, Imagination META (Metag), and Tilera TILE.

The homepage was last seen updated in 2018 per Wayback Machine. Tools for arm-linux-gnueabi and mips64 were updated in 2018.

### 2020s

The last accessible archives of the project's website date to 2021. The website presumably went offline after this point.

The GitHub page of the project continued to receive occasional updates, with the elf2flt tool last updated in August 2024. The SourceForge page was last updated in 2023, a with new tool build for m68k.

## Supported architectures

The current list includes:

- Altera Nios/Nios II
- Amber (open FPGA core)
- ARM ARM7TDMI, ARM Cortex-M3/M4/M7, ARM Cortex-R
- Lattice Mico32
- NXP 680x0 (Motorola/Freescale 680x0)
- Hyperstone E1/E2 (called hyLinux)
- Intel i960
- MIPS
- NXP ColdFire (Motorola/Freescale ColdFire)
- Xilinx MicroBlaze

### No longer supported

- NEC V850E - removed in Linux 2.6.27.
- ADI Blackfin (blackfin) – removed in 4.17
- Axis ETRAX (cris) – removed in 4.17
- Fujitsu FR-V (frv) – removed in 4.17
- Mitsubishi/Renesas M32R (m32r) – removed in 4.17
- Hitachi/Renesas H8 (h8300) - removed in Linux 5.19.

## Hardware projects

The leanXCam was an open-source programmable smart camera used for industrial applications in the field of machine vision that ran under μClinux; the camera won an award at the 2008 VISION tradeshow. As of 2015, the project was discontinued.
