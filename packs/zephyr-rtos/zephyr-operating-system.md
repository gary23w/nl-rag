---
title: "Zephyr (operating system)"
source: https://en.wikipedia.org/wiki/Zephyr_(operating_system)
domain: zephyr-rtos
license: CC-BY-SA-4.0
tags: zephyr rtos, zephyr project, device tree, kconfig build
fetched: 2026-07-02
---

# Zephyr (operating system)

**Zephyr** (/ˈzɛf ər/) is a small real-time operating system (RTOS) for connected, resource-constrained and embedded devices (with an emphasis on microcontrollers) supporting multiple architectures and released under the Apache License 2.0. Zephyr includes a kernel, and all components and libraries, device drivers, protocol stacks, file systems, and firmware updates, needed to develop full application software.

It is named after Zephyrus, the ancient Greek god of the west wind.

## History

Zephyr originated from Virtuoso RTOS for digital signal processors (DSPs). In 2001, Wind River Systems acquired Belgian software company Eonic Systems, the developer of Virtuoso. In November 2015, Wind River Systems renamed the operating system to *Rocket*, made it open-source and royalty-free. Compared to Wind River's other RTOS, VxWorks, Rocket had much smaller memory needs, especially suitable for sensors and single-function embedded devices. Rocket could fit into as little as 4 KB of memory, while VxWorks needed 200 KB or more.

In February 2016, Rocket became a hosted collaborative project of the Linux Foundation under the name *Zephyr*. Wind River Systems contributed the Rocket kernel to Zephyr, but still provided Rocket to its clients, charging them for the cloud services. As a result, Rocket became "essentially the commercial version of Zephyr".

Since then, early members and supporters of Zephyr include Intel, NXP Semiconductors, Synopsys, Linaro, Texas Instruments, Nordic Semiconductor, Oticon, and Bose.

As of January 2025, Zephyr had the largest number of contributors and commits compared to other RTOSes (including Mbed, RT-Thread, NuttX, and RIOT).

## Features

Zephyr intends to provide all components needed to develop resource-constrained and embedded or microcontroller-based applications. This includes:

- A small kernel
- A flexible configuration and build system for compile-time definition of required resources and modules
- A set of protocol stacks (IPv4 and IPv6, Constrained Application Protocol (CoAP), LwM2M, MQTT, 802.15.4, Thread, Bluetooth Low Energy, CAN)
- A virtual file system interface with several flash file systems for non-volatile storage (FatFs, LittleFS, NVS)
- Management and device firmware update mechanisms

### Configuration and build system

Zephyr uses Kconfig and devicetree as its configuration systems, inherited from the Linux kernel, but implemented in Python programming language for portability to non-Unix operating systems. The RTOS build system is based on CMake, which allows Zephyr applications to be built on Linux, macOS, and Microsoft Windows.

### *West* utility tool

Zephyr has a general-purpose tool called *West* for managing repositories, downloading programs to hardware, etc.

### Kernel

Early Zephyr kernels used a dual nanokernel plus microkernel design. In December 2016, with Zephyr 1.6, this changed to a monolithic kernel.

The kernel offers several features that distinguish it from other small OSes:

- Single address space
- Multiple scheduling algorithms
- Highly configurable and modular for flexibility, with resources defined at compile-time
- Memory protection unit (MPU) based protection
- Asymmetric multiprocessing (AMP, based on OpenAMP) and symmetric multiprocessing (SMP) support

### Security

A group is dedicated to maintaining and improving the security. Also, being owned and supported by a community means the world's open source developers are vetting the code, which significantly increases security.
