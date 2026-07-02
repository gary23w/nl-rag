---
title: "ThreadX"
source: https://en.wikipedia.org/wiki/ThreadX
domain: threadx-rtos
license: CC-BY-SA-4.0
tags: threadx rtos, azure rtos, preemptive scheduler, priority inheritance
fetched: 2026-07-02
---

# ThreadX

**ThreadX** is an embedded real-time operating system (RTOS) programmed mostly in the C language. It was originally released in 1997 as **ThreadX** when Express Logic first developed it, later it was renamed to **Azure RTOS** (2019) after Express Logic was purchased by Microsoft, then most recently it was renamed again to **Eclipse ThreadX** (2023), or "ThreadX" in its short form, after it transitioned to free open source model under the stewardship of the Eclipse Foundation.

## History

In 1997, **ThreadX** was first released and marketed by Express Logic of San Diego, California, United States. It was developed by William Lamie, who was also the original author of Nucleus and PX5 RTOS, and was president and CEO of Express Logic. ThreadX version 4 was introduced in 2001, version 5 was introduced in 2005, and then version 6 was introduced in 2020 (the latest major version). FileX – the embedded file system for ThreadX was introduced in 1999. NetX – the embedded TCP/IP networking stack for ThreadX was introduced in 2002. USBX – the embedded USB support for ThreadX was introduced in 2004. ThreadX SMP for SMP multi-core environments was introduced in 2009. ThreadX Modules was introduced in 2011. ThreadX achieved safety certifications for: TÜV IEC 61508 in 2013, and UL 60730 in 2014. GUIX – the embedded UI for ThreadX was introduced in 2014.

On April 18, 2019, Microsoft purchased Express Logic for an undisclosed sum and it was renamed to **Azure RTOS**.

On November 21, 2023, Microsoft announced Azure RTOS would be transitioning to an open source model under the stewardship of the Eclipse Foundation, and making the project available under the permissive MIT License. With Eclipse Foundation as the new home, Azure RTOS was renamed to **Eclipse ThreadX**, or "ThreadX" in its short form.

## Overview

The name ThreadX refers to the threads used as the executable elements, with *X* representing context switching.

ThreadX provides priority-based, pre-emptive scheduling; fast interrupt response; memory management; interthread communication; mutual exclusion; event notification; and thread synchronization features. Major distinguishing technological characteristics of ThreadX include a preemption-threshold, priority inheritance, efficient timer management, fast software timers, picokernel design, event-chaining, and small size (minimal size on an ARM architecture processor is about 2 KB).

ThreadX supports multi-core processor environments via either asymmetric multiprocessing (AMP) or symmetric multiprocessing (SMP). Application thread isolation with memory management unit (MMU) or memory protection unit (MPU) memory protection is available with ThreadX Modules.

ThreadX has safety certifications from TÜV and UL and is Motor Industry Software Reliability Association and MISRA C compliant.

ThreadX is the foundation of Express Logic's X-Ware Internet of things (IoT) platform, which includes embedded file system support (FileX), embedded UI support (GUIX), embedded Internet protocol suite (TCP/IP), cloud connectivity (NetX/NetX Duo), and Universal Serial Bus (USB) support (USBX). ThreadX is liked by developers and is a popular RTOS.

As of 2017, ThreadX RTOS has become one of the most popular RTOSs in the world, deployed in over 6.2 billion devices, including consumer electronics, medical devices, data networking applications, and SoCs.

### Technology

ThreadX implements a priority-based, pre-emptive scheduling algorithm with a proprietary feature called preemption-threshold. The threshold provides greater granularity within critical sections, reduces context switching, and has been the subject of academic research on guaranteeing scheduling.

ThreadX provides a unique construct called event chaining, where the application can register a callback function on all APIs that can signal an external event. This helps applications chain together various public objects in ThreadX allowing one thread to block on multiple objects.

ThreadX also provides counting semaphores, mutexes with optional priority inheritance, event flags, message queues, software timers, fixed-sized block memory, and variable-sized block memory. All APIs in ThreadX that block on resources also have an optional timeout.

ThreadX offers multi-core processor support via either AMP or SMP. Application code isolation is available through the ThreadX Modules component.

### Safety certification

ThreadX (and FileX and NetX Duo) have been precertified by SGS-TÜV Saar to the following safety standards: IEC 61508 SIL 4, IEC 62304 Class C, ISO 26262 ASIL D, and EN 50128 SW-SIL 4.

ThreadX (and FileX and NetX Duo) have been precertified by UL to the following safety standards: UL/IEC 60730, UL/IEC 60335, UL 1998

ThreadX has also been certified to DO-178 standards by various military and aerospace companies. It is supported by popular Transport Layer Security (SSL/TLS) libraries such as wolfSSL.

### Packaging

As of 2017, ThreadX is packaged as part of X-Ware IoT Platform in full source code and with no runtime royalty payment.

## Major components

The major ThreadX components are:

### ThreadX

ThreadX is the real-time operating system (RTOS).

### FileX and LevelX

FileX is an optional file system for ThreadX. It supports FAT12, FAT16, FAT32, and exFAT file systems. The latter extends FAT file sizes beyond 4 GB, which is useful for large video files.

It also offers fault tolerance and supports direct NOR and NAND flash memory media through an optional flash wear leveling product called **LevelX**.

### GUIX

GUIX is an optional graphical user interface (GUI) for ThreadX. It provides a 2D computer graphics system that supports multiple display devices with a variety of screen resolutions and color depths. Many predefined graphical widgets are available. A Windows WYSIWYG host tool called GUIX Studio automatically generates C code for GUIX to execute at runtime.

### NetX Duo

NetX Duo is an optional TCP/IP network system for ThreadX. It supports both IPv4 and IPv6 networking with IPsec network security. TCP and UDP socket layers are provided by TLS / DTLS. Optional protocols include ARP, Auto IP, DHCP, DNS, DNS-SD, FTP, HTTP, ICMP, IGMP, mDNS, POP3, PPP, PPPoE, RARP, TFTP, SNTP, SMTP, SNMP, and Telnet. IoT Cloud protocol support includes CoAP, MQTT, and LWM2M. NetX Duo also supports Thread and 6LoWPAN. In 2017, ThreadX and NetX Duo became a Thread Certified Product.

### USBX

USBX is an optional Universal Serial Bus (USB) system for ThreadX. It supports both host/device/on-the-go (OTG). Host controller support includes EHCI, OHCI, and proprietary USB host controllers.

It supports these USB Device Classes: Audio, Asix, CDC/ACM, CDC/ECM, DFU, GSER, HID, PIMA, Printer, Prolific, RNDIS, and Storage.

### TraceX

TraceX is an optional host software that provides a graphical view of ThreadX RTOS events. It requires Windows XP or later.

## Supported ports

- ARM classic cores (32bit)
  - ARM7
  - ARM9
  - ARM11
- ARM microcontroller cores (32bit)
  - ARM Cortex-M0
  - ARM Cortex-M0+
  - ARM Cortex-M3
  - ARM Cortex-M4
  - ARM Cortex-M7
  - ARM Cortex-M23
  - ARM Cortex-M33
  - ARM Cortex-M55
  - ARM Cortex-M85
- ARM real time cores (32bit)
  - ARM Cortex-R4
  - ARM Cortex-R5
  - ARM Cortex-R7
- ARM application cores (32bit)
  - ARM Cortex-A5
  - ARM Cortex-A7
  - ARM Cortex-A8
  - ARM Cortex-A9
  - ARM Cortex-A12
  - ARM Cortex-A15
  - ARM Cortex-A17
  - ARM Cortex-A35
- ARM application cores (32bit)
  - ARM Cortex-A53
  - ARM Cortex-A55
  - ARM Cortex-A57
  - ARM Cortex-A72
  - ARM Cortex-A73
  - ARM Cortex-A75
  - ARM Cortex-A76
  - ARM Cortex-A77
- ARM application cores (64bit)
  - ARM Cortex-A34
  - ARM Cortex-A53
  - ARM Cortex-A55
  - ARM Cortex-A57
  - ARM Cortex-A65
  - ARM Cortex-A76
- Other cores
  - ARC EM / HS
  - Intel x86 (32bit)
  - Renesas RXv1 / RXv2 / RXv3
  - RISC-V (32bit)
  - Tensilica Xtensa
  - TI TMS320C667x (DSP)
- Operating systems
  - Linux
  - Windows (32bit)

## Products using ThreadX

Some examples of products that use ThreadX:

- Small wearable devices.
- Hewlett-Packard inkjet printers and all-in-one devices.
- Intel Management Engine (ME).
- NASA Deep Impact space probe.
- Raspberry Pi line of single-board computers runs ThreadX as a binary blob on the graphics processing unit (GPU). This controls initial booting, which in turn is used to boot secondary operating systems such as Linux, and continues to operate in a more privileged role even after the boot process.
- AGM M11 mobile phone
