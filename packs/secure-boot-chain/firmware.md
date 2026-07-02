---
title: "Firmware"
source: https://en.wikipedia.org/wiki/Firmware
domain: secure-boot-chain
license: CC-BY-SA-4.0
tags: secure boot chain, verified boot process, uefi firmware security, chain of trust verification, firmware integrity measurement
fetched: 2026-07-02
---

# Firmware

In computing, **firmware** (**FW**) is software that provides low-level control of computer hardware. For a relatively simple device, firmware may perform all control, monitoring and data manipulation functionality. For a more complex device, firmware may provide only relatively low-level control as well as hardware abstraction to higher-level software such as an operating system.

Firmware is found in a wide range of computing devices, including personal computers, smartphones, home appliances, vehicles, computer peripherals and in many of the integrated circuits inside each of these larger systems.

Firmware is stored in non-volatile memory – either read-only memory (ROM) or programmable memory such as EPROM, EEPROM, or flash. Changing a device's firmware stored in ROM requires physically replacing the memory chip or the device itself. Programmable firmware memory can be reprogrammed via a procedure sometimes called *flashing*. Common reasons for changing firmware include fixing bugs and adding features.

## History and etymology

Ascher Opler used the term *firmware* in a 1967 *Datamation* article, as an intermediary term between *hardware* and *software*. Opler projected that fourth-generation computer systems would have a writable control store (a small specialized high-speed memory) into which microcode firmware would be loaded. Many software functions would be moved to microcode, and instruction sets could be customized, with different firmware loaded for different instruction sets.

As computers began to increase in complexity, it became clear that various programs needed to first be initiated and run to provide a consistent environment necessary for running more complex programs at the user's discretion. This required programming the computer to run those programs automatically. Furthermore, as companies, universities, and marketers wanted to sell computers to laypeople with little technical knowledge, greater automation became necessary to allow a layperson to easily run programs for practical purposes. This gave rise to a kind of software that a user would not consciously run, and it led to software that a lay user would not even know about.

As originally used, firmware contrasted with hardware (the CPU itself) and software (normal instructions executing on a CPU). It was not composed of CPU machine instructions, but of lower-level microcode involved in the implementation of machine instructions. It existed on the boundary between hardware and software; thus the name *firmware*. Over time, popular usage extended the word *firmware* to denote any computer program that is tightly linked to hardware, including BIOS on PCs, boot firmware on smartphones, computer peripherals, or the control systems on simple consumer electronic devices, such as microwave ovens and remote controls.

## Applications

### Computers

In some respects, the various firmware components are as important as the operating system in a working computer. However, unlike most modern operating systems, firmware rarely has a well-evolved automatic mechanism of updating itself to fix any functionality issues detected after shipping the unit.

A computer's firmware may be manually updated by a user via a small utility program. In contrast, firmware in mass storage devices (hard-disk drives, optical disc drives, flash memory storage e.g., solid state drive) is less frequently updated, even when flash memory (rather than ROM, EEPROM) storage is used for the firmware.

Most computer peripherals are themselves special-purpose computers. Devices such as printers, scanners, webcams, and USB flash drives have internally-stored firmware; some devices may also permit field upgrading of their firmware. For modern, simpler devices, such as USB keyboards, USB mouses and USB sound cards, the trend is to store the firmware in on-chip memory in the device's microcontroller, as opposed to storing it in a separate EEPROM chip.

Examples of computer firmware include:

- The BIOS firmware used on PCs
- The (U)EFI-compliant firmware used on Itanium systems, Intel-based Macs, and many newer PCs
- Hard disk drive, solid-state drive, optical disc drive and optical disc recorder firmware
- Video BIOS of a graphics card
- Open Firmware, used in SPARC-based computers from Sun Microsystems and Oracle Corporation, PowerPC-based computers from Apple, and computers from Genesi
- ARCS, used in computers from Silicon Graphics
- Kickstart, used in the Amiga line of computers (POST, hardware init + Plug and Play auto-configuration of peripherals, kernel, etc.)
- RTAS (Run-Time Abstraction Services), used in System i and System p computers from IBM
- The Common Firmware Environment (CFE) for Broadcom systems-on-chip (SoCs)

### Home and personal-use products

Consumer products like digital cameras and portable music players support firmware upgrades. In digital cameras, firmware upgrades address bugs in the operation, along with adding new functions to the camera's operation. Some companies use firmware updates to add new playable file formats (codecs). Other features that may change with firmware updates include the user interface or even the battery life.

### Automobiles

Since 1996, most automobiles have employed an on-board computer and various sensors to detect mechanical problems. As of 2010, modern vehicles also employ computer-controlled anti-lock braking systems (ABS) and computer-operated transmission control units (TCUs). The driver can also get in-dash information while driving in this manner, such as real-time fuel economy and tire pressure readings. Local dealers can update most vehicle firmware.

### Other examples

Other firmware applications include:

- In home and personal-use products:
  - Timing and control systems for washing machines
  - Controlling sound and video attributes, as well as the channel list, in modern televisions
- In routers, switches, and firewalls:
  - LibreCMC – a 100% free software router distribution based on the Linux-libre kernel
  - IPFire – an open-source firewall/router distribution based on the Linux kernel
  - fli4l – an open-source firewall/router distribution based on the Linux kernel
  - OpenWrt – an open-source firewall/router distribution based on the Linux kernel
  - m0n0wall – an embedded firewall distribution of FreeBSD
  - Proprietary firmware
- In NAS systems:
  - NAS4Free – an open-source NAS operating system based on FreeBSD
  - Openfiler – an open-source NAS operating system based on the Linux kernel
  - Proprietary firmware
- CPLD or FPGA code may be referred to as firmware

## Flashing

*Flashing* is a process that involves the overwriting of existing firmware or data, contained in EEPROM or flash memory module present in an electronic device, with new data. This can be done to upgrade a device or to change the provider of a service associated with the function of the device, such as changing from one mobile phone service provider to another or installing a new operating system. If firmware is upgradable, it is often done via a program from the provider, and will often allow the old firmware to be saved before upgrading so it can be reverted to if the process fails, or if the newer version performs worse. Free software replacements for vendor flashing tools have been developed, such as Flashrom.

## Firmware hacking

Sometimes, third parties develop an unofficial new or modified ("aftermarket") version of firmware to provide new features or to unlock hidden functionality; this is referred to as custom firmware. An example is Rockbox as a firmware replacement for portable media players. There are many homebrew projects for various devices, which often unlock general-purpose computing functionality in previously limited devices (e.g., running Doom on iPods).

Firmware hacks usually take advantage of the firmware update facility on many devices to install or run themselves. Some, however, must resort to exploits to run, because the manufacturer has attempted to lock the hardware to stop it from running unlicensed code.

Most firmware hacks are free software.

### HDD firmware hacks

The Moscow-based Kaspersky Lab discovered that a group of developers it refers to as the Equation Group has developed hard disk drive firmware modifications for various drive models, containing a trojan horse that allows data to be stored on the drive in locations that will not be erased even if the drive is formatted or wiped. Although the Kaspersky Lab report did not explicitly claim that this group is part of the United States National Security Agency (NSA), evidence obtained from the code of various Equation Group software suggests that they are part of the NSA.

Researchers from the Kaspersky Lab categorized the undertakings by Equation Group as the most advanced hacking operation ever uncovered, also documenting around 500 infections caused by the Equation Group in at least 42 countries.

## Security risks

Mark Shuttleworth, the founder of the company Canonical, which created the Ubuntu Linux distribution, has described proprietary firmware as a security risk, saying that "firmware on your device is the NSA's best friend" and calling firmware "a trojan horse of monumental proportions". He has asserted that low-quality, closed source firmware is a major threat to system security: "Your biggest mistake is to assume that the NSA is the only institution abusing this position of trust – in fact, it's reasonable to assume that all firmware is a cesspool of insecurity, courtesy of incompetence of the highest degree from manufacturers, and competence of the highest degree from a very wide range of such agencies". As a potential solution to this problem, he has called for declarative firmware, which would describe "hardware linkage and dependencies" and "should not include executable code". Firmware should be open-source so that the code can be checked and verified.

Custom firmware hacks have also focused on injecting malware into devices such as smartphones or USB devices. One such smartphone injection was demonstrated on the Symbian OS at MalCon, a hacker convention. A USB device firmware hack called BadUSB was presented at the Black Hat USA 2014 conference, demonstrating how a USB flash drive microcontroller can be reprogrammed to spoof various other device types to take control of a computer, exfiltrate data, or spy on the user. Other security researchers have worked further on how to exploit the principles behind BadUSB, releasing at the same time the source code of hacking tools that can be used to modify the behavior of different USB devices.
