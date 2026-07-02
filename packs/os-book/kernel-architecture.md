---
title: "Operating System Design/Kernel Architecture"
source: https://en.wikibooks.org/wiki/Operating_System_Design/Kernel_Architecture
domain: os-book
license: CC-BY-SA-4.0 (Wikibooks OS Design)
tags: operating system design, kernel design, process management
fetched: 2026-07-02
---

# Operating System Design/Kernel Architecture

<

Operating System Design

The kernel is the core of an operating system. It is the software responsible for running programs and providing secure access to the machine's hardware. Since there are many programs, and resources are limited, the kernel also decides when and how long a program should run. This is called scheduling. Accessing the hardware directly can be very complex, since there are many different hardware designs for the same type of component. Kernels usually implement some level of hardware abstraction (a set of instructions universal to all devices of a certain type) to hide the underlying complexity from applications and provide a clean and uniform interface. This helps application programmers to develop programs without having to know how to program for specific devices. The kernel relies upon software drivers that translate the generic command into instructions specific to that device.

An operating system kernel is not strictly needed to run a computer. Programs can be directly loaded and executed on the "bare metal" machine, provided that the authors of those programs are willing to do without any hardware abstraction or operating system support. This was the normal operating method of many early computers, which were reset and reloaded between the running of different programs. Eventually, small ancillary programs such as program loaders and debuggers were typically left in-core between runs, or loaded from read-only memory. As these were developed, they formed the basis of what became early operating system kernels. The "bare metal" approach is still used today on many video game consoles and embedded systems, but in general, newer systems use kernels and operating systems.

Four broad categories of kernels:

- *Monolithic kernels* provide rich and powerful abstractions of the underlying hardware.
- *Microkernels* provide a small set of simple hardware abstractions and use applications called servers to provide more functionality.
- *Exokernels* provide minimal abstractions, allowing low-level hardware access. In exokernel systems, library operating systems provide the abstractions typically present in monolithic kernels.
- *Hybrid* (*modified microkernels*) are much like pure microkernels, except that they include some additional code in kernelspace to increase performance.

Retrieved from "

https://en.wikibooks.org/w/index.php?title=Operating_System_Design/Kernel_Architecture&oldid=4435404

"
