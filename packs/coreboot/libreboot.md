---
title: "Libreboot"
source: https://en.wikipedia.org/wiki/Libreboot
domain: coreboot
license: CC-BY-SA-4.0
tags: coreboot firmware, libreboot project, open-source bios, firmware payload
fetched: 2026-07-02
---

# Libreboot

**Libreboot** (briefly known as **GNU Libreboot**) is a free and open-source software project based on coreboot, aimed at replacing some of the proprietary BIOS or UEFI firmware on supported x86-64 and AArch64 computers. Libreboot performs the basic machine setup such as CPU initialization or memory controller initialization necessary to load and run a 32-bit or 64-bit operating system, such as Linux or BSD. It was tested on FreeBSD, NetBSD, and OpenBSD.

## Characteristics

Libreboot is established as a distribution of coreboot, but with some proprietary binary blobs removed from coreboot. Libreboot makes coreboot easy to use by automating the build and installation processes.

On some devices, Libreboot developers have reverse engineered the firmware from Intel and created a utility to create a free firmware that meets the specifications from Intel. Hardware support includes but is not limited to the ASUS KGPE-D16, ThinkPad T400, X60 and X200. Libreboot is officially endorsed by the upstream coreboot project.

## Installation

Internal flashing is possible, but it's recommended to have a working external flashing setup that could be used to recover from mistakes when flashing internally.

It is strongly advised not to use the CH341A programmer, as it can easily damage BIOS chips. For safety, use the Raspberry Pi Pico with a SOIC clip.

Installation usually goes as follows:

- Compile or download the necessary tools and dependencies
- Build or download the BIOS image
- Insert binary files if the image has been downloaded from a repository
- Flash your images with flashprog or internally

## Security

Probably the most famous feature of Libreboot, and one that also highly impacts the security and possibly the privacy of the user, is that on most machines, Libreboot disables the Intel Management Engine by default. On older machines (before ME version 6.0), the Intel ME code could be entirely removed from the flash memory, thus completely disabling the ME. This is the case on devices like the ThinkPad X200 or ThinkPad T400. On newer devices, the Intel ME is needed to boot the machine, because of this, the ME is not completely disabled, but rather put into a inactive or "disabled" state after the machine boots.

Other optional security features include, but are not limited to:

- Full disk encryption
- Software flash memory write protection

## History

The Libreboot project was started in December 2013 as a distribution of coreboot, which excludes non-free binary blobs. Coreboot began as LinuxBIOS in 1999 at Los Alamos National Labs (LANL), and was renamed "coreboot" in 2008.

Libreboot has been endorsed by the Free Software Foundation, and was an official part of the GNU Project starting in May 2016. In January 2017, the project's maintainer Leah Rowe pulled Libreboot from the GNU Project, after a months-long dispute with the Free Software Foundation which oversees GNU.

## Reception

In 2015, Kyle Rankin stated in *Linux Journal* that Libreboot "greatly simplified and automated" the flashing process, "with a few caveats". In 2016, Bryan Cockfield stated in Hackaday that Libreboot installation was "harrowing" and "not as easy as you'd think".
