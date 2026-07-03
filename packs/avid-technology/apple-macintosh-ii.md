---
title: "Macintosh II"
source: https://en.wikipedia.org/wiki/Apple_Macintosh_II
domain: avid-technology
license: CC-BY-SA-4.0
tags: avid technology
fetched: 2026-07-03
---

# Macintosh II

(Redirected from

Apple Macintosh II

)

The **Macintosh II** is a personal computer designed, manufactured, and sold by Apple Computer from March 1987 to January 1990. Based on the Motorola 68020 32-bit CPU, it is the first Macintosh supporting color graphics. When introduced, a basic system with monitor and 20 MB hard drive cost US$5,498 (equivalent to $15,580 in 2025). With a 13-inch color monitor and 8-bit display card, the price was about US$7,145 (equivalent to $20,250 in 2025). This placed it in competition with workstations from Silicon Graphics, Sun Microsystems, and Hewlett-Packard.

The Macintosh II was the first computer in the Macintosh line without a built-in display; a monitor rested on top of the case like the IBM Personal Computer and Amiga 1000. It was designed by hardware engineers Michael Dhuey (computer) and Brian Berkeley (monitor) and industrial designer Hartmut Esslinger (case).

Eighteen months after its introduction, the Macintosh II was updated with a more powerful CPU and sold as the Macintosh IIx. In early 1989, the more compact Macintosh IIcx was introduced at a price similar to the original Macintosh II, and by the beginning of 1990 sales stopped altogether. Motherboard upgrades to turn a Macintosh II into a IIx or Macintosh IIfx were offered by Apple.

## Development

Two common criticisms of the original Macintosh, starting from its introduction in 1984, were the closed architecture and lack of color; rumors of a potential color Macintosh began almost immediately.

The Macintosh II project was begun by Dhuey and Berkeley during 1985 without the knowledge of Apple co-founder and Macintosh division head Steve Jobs, who opposed expansion slots and color, on the basis that expansion slots complicated the user experience and that color did not conform to WYSIWYG, as color printers were not common. Jobs instead wanted higher-resolution monochrome displays such as the ones chosen for his own "BigMac" project begun in 1984 to develop a Macintosh successor.

Initially referred to as "Little Big Mac", the Macintosh II was codenamed "Milwaukee" after Dhuey's hometown, and it later went through a series of new names. After Jobs was ousted by Apple in September 1985, the Milwaukee project could proceed openly (while Jobs' own BigMac project was cancelled).

The Macintosh II was introduced at the AppleWorld 1987 conference in Los Angeles, with low-volume initial shipments starting two months later. Retailing for US $5,498, the Macintosh II was the first modular Macintosh model, so called because it came in a horizontal desktop case like many IBM PC compatibles of the time. Previous Macintosh computers use an all-in-one design with a black-and-white CRT.

The Macintosh II has drive bays for an internal hard disk (originally 40 MB or 80 MB) and an optional second floppy disk drive. Along with the Macintosh SE, it was the first Macintosh to use the Apple Desktop Bus (ADB) introduced with the Apple IIGS for keyboard and mouse connection.

The primary improvement in the Macintosh II was Color QuickDraw in ROM, a color version of the Macintosh graphics routines. Color QuickDraw can handle any display size, up to 8-bit color depth, and multiple monitors. Because Color QuickDraw is included in the Macintosh II's ROM and relies on 68020 instructions, earlier systems could not be upgraded to display color.

In September 1988, shortly before the introduction of the Macintosh IIx, Apple increased the list price of the Macintosh II by roughly 20%. AnimEigo notably used the Macintosh II for subtitling their earliest releases, including *MADOX-01*, *Riding Bean*, and *Vampire Princess Miyu*, and Industrial Light & Magic used the Macintosh II for image processing on films such as *The Abyss*.

## Hardware

### CPU

The Macintosh II is built around the Motorola 68020 processor operating at 16 MHz, teamed with a Motorola 68881 floating-point unit. The machine shipped with a socket for an optional Motorola 68851 MMU, but an "Apple HMMU Chip" (VLSI VI475 chip) was installed by default and could not implement virtual memory (instead, it translated 24-bit addresses to 32-bit addresses for the Mac OS, which would not be 32-bit clean until System 7).

### Memory

The standard memory was 1 megabyte, expandable to 8 MB. The Mac II had eight 30-pin SIMMs, and memory was installed in groups of four (called "Bank A" and "Bank B").

The Macintosh II does not have a PMMU installed by default. Instead, it relies on the memory controller hardware to map the installed memory into a contiguous address space. This hardware has the restriction that the address space dedicated to Bank A must be larger than that of Bank B. Though this memory controller was designed to support 16 Megabyte, 30-pin SIMMs in each available slot (for a total of up to 128 MB of RAM), the original Macintosh II ROMs have problems that limit the amount of RAM that can be installed into each slot to just 8 MB SIMMs. Although the later Macintosh IIx ROMs that shipped with the Macintosh II FDHD upgrade fixes this initial problem, these newer ROMs still do not have a 32-bit memory manager and cannot boot into 32-bit address mode, at least, not without software assistance in the form of "MODE32", thus limiting the *total* amount of RAM to a mere 8MB. MODE32 (originally published by Connectix, and later licensed by Apple) contains a workaround that allows for larger SIMMs to be installed in Bank B if a PMMU is also installed. With this configuration, the Macintosh II boot ROMs will believe that the computer has 8 MB or less of RAM installed. Meanwhile, MODE32 then reprograms the memory controller on the fly to dedicate more address space to Bank A, thus allowing access to the additional memory installed in Bank B. Since this makes the physical address space discontiguous, the PMMU is then used to remap the address space into a contiguous block.

### Graphics

The Macintosh II includes a graphics card that supports a true-color 16.7-million-color palette and was available in two configurations: 4-bit and 8-bit. The 4-bit model supports 16 colors on a 640×480 display and 256 colors (8-bit video) on a 512×384 display, which means that VRAM was 256 KB. The 8-bit model supports 256-color video on a 640×480 display, which means that VRAM was 512 KB in size. With an optional RAM upgrade (requiring 120 ns DIP chips), the 4-bit version supports 640×480 in 8-bit color. The video card does not include hardware acceleration of drawing operations.

**Display**: Apple offered a choice of two displays, a 12" black and white unit, and a more expensive 13" high-resolution color display based on Sony's Trinitron technology. More than one display could be attached to the computer, and objects could be easily dragged from one screen to the next. Third-party displays quickly became available. The Los Angeles Times reviewer called the color "spectacular." The operating system user interface remained black and white even on color monitors with the exception of the Apple logo, which appeared in rainbow color.

### Storage

A 5.25-inch 40 MB internal SCSI hard disk was optional, as was a second internal 800 kilobyte 3.5-inch floppy disk drive.

### Expansion

Six NuBus slots were available for expansion (at least one of which had to be used for a graphics card, as the Mac II had no onboard graphics chipset and the OS didn't support headless booting). It is possible to connect as many as six displays to a Macintosh II by filling all of the NuBus slots with graphics cards. Another option for expansion included the Mac286, which included an Intel 80286 chip and could be used for MS-DOS compatibility.

The original ROMs in the Macintosh II contained a bug that prevented the system from recognizing more than one megabyte of memory address space on a Nubus card. Every Macintosh II manufactured until approximately November 1987 had this defect. This happened because Slot Manager was not 32-bit clean. Apple offered a well-publicized recall of the faulty ROMs and released a program to test whether a particular Macintosh II had the defect.

Integrated Device Technology utilised the NuBus expansion slot in the Macintosh II with its MacStation development board for the MIPS R3000, providing the RISC processor on the board and supplying a port of Unix to run on it, requiring a Macintosh II with at least 8 MB of RAM and various other storage requirements. IDT sold MacStation products as complete systems based on the Macintosh II, following up with the MacStation 2 employing the 16 MHz R3000 on its RISC CPU board, with 8 MB of RAM supplied on another NuBus card, upgradable to 16 MB, and supplied with a 160 MB hard drive if desired.

The MacStation 3 upgraded the CPU to either a 20 MHz R3000 coupled with 8 MB of RAM or a 25 MHz R3000 with 16 MB of RAM, with the RAM being located on the CPU board itself, and the board gaining dedicated SCSI and serial input/output ports. The Unix filesystems accessed by the R3000 were encapsulated in Macintosh files if the host machine's storage were to be used. Otherwise, storage attached to the dedicated SCSI port could host the Unix filesystem with higher performance. With Apple's MacX software running on the host, Unix software utilising the X Window System and the Motif graphical toolkit could be used. IDT was an "authorized Apple VAR" in offering the MacStation systems.

### Accessories

The Macintosh II and Macintosh SE were the first Apple computers since the Apple I to be sold without a keyboard. Instead the customer was offered a choice of the new ADB Apple Keyboard or the Apple Extended Keyboard as a separate purchase. Dealers could bundle a third-party keyboard or attempt to upsell a customer to the more expensive (and higher-profit) Extended Keyboard.

### Audio

The Macintosh II was the first Macintosh to have the Chimes of Death accompany the Sad Mac logo whenever a serious hardware error occurred.

The new extensions featured for the Macintosh II at the time were A/ROSE and Sound Manager.

## Models

The Macintosh II was offered in three configurations. All systems included a mouse and a single 800 KB 3.5-inch floppy disk drive; a Motorola 68851 PMMU was available as an option and required for running A/UX.

- **Macintosh II CPU**: 1 MB RAM.
- **Macintosh II 1/40 CPU**: 1 MB RAM, internal 40-megabyte SCSI HDD.
- **Macintosh II 4/40 CPU**: 4 MB RAM, internal 40-megabyte SCSI HDD.

## Timeline

| Timeline of Macintosh II family models |
|---|
|   |
