---
title: "Monolithic kernel"
source: https://en.wikipedia.org/wiki/Monolithic_kernel
domain: linux-kernel
license: CC-BY-SA-4.0
tags: linux kernel, loadable kernel module, monolithic kernel, kernel preemption
fetched: 2026-07-02
---

# Monolithic kernel

A **monolithic kernel** is an operating system architecture with the entire operating system running in kernel space. The monolithic model differs from other architectures such as the microkernel in that it alone defines a high-level virtual interface over computer hardware. A set of primitives or system calls implement all operating system services such as process management, concurrency, and memory management.

Device drivers can be added to the kernel as loadable kernel modules.

## Examples

- Most BSD kernels
  - FreeBSD
  - OpenBSD
  - NetBSD
- Linux kernel
  - Android
- Other Unix/Unix-like kernels
  - AIX
  - Oracle Solaris
- MS-DOS
  - Windows 1.0 to Windows 3.1
  - Windows 9x
- Windows Mobile
- Classic Mac OS (System 1.0 to Mac OS 8) within 68K
- OpenVMS
- Palm OS (version ≤ 5.0)

## Loadable modules

Modular operating systems such as OS-9 and most modern monolithic-kernel operating systems such as OpenVMS, Linux, FreeBSD, NetBSD, Solaris, and AIX can dynamically load (and unload) executable kernel modules at runtime.

This modularity of the operating system is at the binary (image) level and not at the architecture level. Modular monolithic operating systems are not to be confused with the architectural level of modularity inherent in server-client operating systems (and its derivatives sometimes marketed as hybrid kernel) which use microkernels and servers (not to be mistaken for modules or daemons).

Practically speaking, dynamically loading modules is simply a more flexible way of handling the operating system image at runtime—as opposed to rebooting with a different operating system image. The modules allow easy extension of the operating systems' capabilities as required. Dynamically loadable modules incur a small overhead when compared to building the module into the operating system image.

However, in some cases, loading modules dynamically (as-needed) helps to keep the amount of code running in kernel space to a minimum; for example, to minimize operating system footprint for embedded devices or those with limited hardware resources. Namely, an unloaded module need not be stored in scarce random access memory.
