---
title: "Volatility (software)"
source: https://en.wikipedia.org/wiki/Volatility_(memory_forensics)
domain: memory-forensics-volatility
license: CC-BY-SA-4.0
tags: memory forensics volatility, volatile memory acquisition, process memory dump analysis, core dump inspection, digital evidence recovery
fetched: 2026-07-02
---

# Volatility (software)

(Redirected from

Volatility (memory forensics)

)

**Volatility** is an open-source memory forensics framework for incident response and malware analysis. It is written in Python and supports Microsoft Windows, Mac OS X, and Linux (as of version 2.5).

Volatility was created by Aaron Walters, drawing on academic research he did in memory forensics.

## Operating system support

Volatility supports investigations of the following memory images:

Windows:

- 32-bit Windows XP (Service Pack 2 and 3)
- 32-bit Windows 2003 Server (Service Pack 0, 1, 2)
- 32-bit Windows Vista (Service Pack 0, 1, 2)
- 32-bit Windows 2008 Server (Service Pack 1, 2)
- 32-bit Windows 7 (Service Pack 0, 1)
- 32-bit Windows 8, 8.1, and 8.1 Update 1
- 32-bit Windows 10 (initial support)
- 64-bit Windows XP (Service Pack 1 and 2)
- 64-bit Windows 2003 Server (Service Pack 1 and 2)
- 64-bit Windows Vista (Service Pack 0, 1, 2)
- 64-bit Windows 2008 Server (Service Pack 1 and 2)
- 64-bit Windows 2008 R2 Server (Service Pack 0 and 1)
- 64-bit Windows 7 (Service Pack 0 and 1)
- 64-bit Windows 8, 8.1, and 8.1 Update 1
- 64-bit Windows Server 2012 and 2012 R2
- 64-bit Windows 10 (including at least 10.0.14393)
- 64-bit Windows Server 2016 (including at least 10.0.14393.0)

Mac OSX:

- 32-bit 10.5.x Leopard (the only 64-bit 10.5 is Server, which isn't supported)
- 32-bit 10.6.x Snow Leopard
- 32-bit 10.7.x Lion
- 64-bit 10.6.x Snow Leopard
- 64-bit 10.7.x Lion
- 64-bit 10.8.x Mountain Lion
- 64-bit 10.9.x Mavericks
- 64-bit 10.10.x Yosemite
- 64-bit 10.11.x El Capitan
- 64-bit 10.12.x Sierra
- 64-bit 10.13.x High Sierra
- 64-bit 10.14.x Mojave
- 64-bit 10.15.x Catalina

Linux:

- 32-bit Linux kernels 2.6.11 to 5.5
- 64-bit Linux kernels 2.6.11 to 5.5
- OpenSuSE, Ubuntu, Debian, CentOS, Fedora, Mandriva, etc.

## Memory format support

Volatility supports a variety of sample file formats and the ability to convert between these formats:

- Raw/Padded Physical Memory
- Firewire (IEEE 1394)
- Expert Witness (EWF)
- 32- and 64-bit Windows Crash Dump
- 32- and 64-bit Windows Hibernation (from Windows 7 or earlier)
- 32- and 64-bit Mach-O files
- Virtualbox Core Dumps
- VMware Saved State (.vmss) and Snapshot (.vmsn)
- HPAK Format (FastDump)
- QEMU memory dumps
- LiME format
