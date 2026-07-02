---
title: "ACPI"
source: https://en.wikipedia.org/wiki/ACPI
domain: hardware-abstraction
license: CC-BY-SA-4.0
tags: hardware abstraction, embedded systems
fetched: 2026-07-02
---

# ACPI

**Advanced Configuration and Power Interface** (**ACPI**) is an open standard that operating systems can use to discover and configure computer hardware components, to perform power management (e.g. putting unused hardware components to sleep), auto configuration (e.g. plug and play and hot swapping), and status monitoring. Launched in December 1996 and first available in Windows 98 and Windows 2000, ACPI aims to replace Advanced Power Management (APM), the MultiProcessor Specification, and the Plug and Play BIOS (PnP) Specification. ACPI brings power management under the control of the operating system, as opposed to the previous BIOS-centric system that relied on platform-specific firmware to determine power management and configuration policies. The specification is central to the **Operating System-directed configuration and Power Management** (**OSPM**) system. ACPI defines hardware abstraction interfaces between the device's firmware (e.g. BIOS, UEFI), the computer hardware components, and the operating systems.

Internally, ACPI advertises the available components and their functions to the operating system kernel using instruction lists ("methods") provided through the system firmware (UEFI or BIOS), which the kernel parses. ACPI then executes the desired operations written in *ACPI Machine Language* (such as the initialization of hardware components) using an embedded minimal virtual machine.

Intel, Microsoft and Toshiba originally developed the standard, while HP, Huawei and Phoenix also participated later. In October 2013, ACPI Special Interest Group (ACPI SIG), the original developers of the ACPI standard, agreed to transfer all assets to the UEFI Forum, in which all future development will take place. The latest version of the standard 6.6 was released in 13 May 2025.

## Architecture

The firmware-level ACPI has three main components: the ACPI tables, the ACPI BIOS, and the ACPI registers. The ACPI BIOS generates ACPI tables and loads ACPI tables into main memory. Much of the firmware ACPI functionality is provided in bytecode of *ACPI Machine Language* (*AML*), a Turing-complete, domain-specific low-level language, stored in the ACPI tables. To make use of the ACPI tables, the operating system must have an interpreter for the AML bytecode. A reference AML interpreter implementation is provided by the *ACPI Component Architecture* (*ACPICA*). At the BIOS development time, AML bytecode is compiled from *ACPI Source Language* (*ASL*) code.

### ACPI Component Architecture (ACPICA)

The **ACPI Component Architecture** (**ACPICA**), mainly written by Intel's engineers, provides an open-source platform-independent reference implementation of the operating system–related ACPI code. The ACPICA code is used by Linux, Haiku, ArcaOS and FreeBSD, which supplement it with their operating-system specific code.

## History

The first revision of the ACPI specification was released in December 1996, supporting 16, 24 and 32-bit addressing spaces. It was not until August 2000 that ACPI received 64-bit address support as well as support for multiprocessor workstations and servers with revision 2.0.

In 1999, then Microsoft CEO Bill Gates stated in an e-mail that Linux would benefit from ACPI without them having to do work and suggested to make it Windows-only.

In September 2004, revision 3.0 was released, bringing to the ACPI specification support for SATA interfaces, PCI Express bus, multiprocessor support for more than 256 processors, ambient light sensors and user-presence devices, as well as extending the thermal model beyond the previous processor-centric support.

Released in June 2009, revision 4.0 of the ACPI specification added various new features to the design; most notable are the USB 3.0 support, logical processor idling support, and x2APIC support.

Initially ACPI was exclusive to x86 architecture; Revision 5.0 of the ACPI specification was released in December 2011, which added the ARM architecture support. The revision 5.1 was released in July 2014. The latest revision 6.6, which was released in May 2025, added the RISC-V support.

## Operating systems

Microsoft's Windows 98 was the first operating system to implement ACPI, but its implementation was somewhat buggy or incomplete, although some of the problems associated with it were caused by the first-generation ACPI hardware. Other operating systems, including later versions of Windows, macOS (x86 macOS only), eComStation, ArcaOS, FreeBSD (since FreeBSD 5.0), NetBSD (since NetBSD 1.6), OpenBSD (since OpenBSD 3.8), HP-UX, OpenVMS, Linux, GNU/Hurd and PC versions of Solaris, have at least some support for ACPI. Some newer operating systems, like Windows Vista, require the computer to have an ACPI-compliant BIOS, and since Windows 8, the S0ix/Modern Standby state was implemented.

Windows operating systems use acpi.sys to access ACPI events.

The 2.4 series of the Linux kernel had only minimal support for ACPI, with better support implemented (and enabled by default) from kernel version 2.6.0 onwards. Old ACPI BIOS implementations tend to be quite buggy, and consequently are not supported by later operating systems. For example, Windows 2000, Windows XP, and Windows Server 2003 only use ACPI if the BIOS date is after January 1, 1999. Similarly, Linux kernel 2.6 may not use ACPI if the BIOS date is before January 1, 2001.

Linux-based operating systems can provide handling of ACPI events via acpid.

## OSPM responsibilities

Once an OSPM-compatible operating system activates ACPI, it takes exclusive control of all aspects of power management and device configuration. The OSPM implementation must expose an ACPI-compatible environment to device drivers, which exposes certain system, device and processor states.

### Power states

#### Global states

The ACPI Specification defines the following four global "Gx" states and six sleep "Sx" states for an ACPI-compliant computer system:

| Gx | Name | Sx | Description |
|---|---|---|---|
| G0 | Working | S0 | The computer is running and the CPU executes instructions. "Away mode" is a subset of S0, where monitor is off but background tasks are running. |
| G1 | Sleeping | S0ix | Modern Standby, or "Low Power S0 Idle". Partial processor SoC sleep. Sub states include S0i1, S0i2 and S0i3. Known to ARM and x86 devices. |
| S1 | *Power on Suspend (POS):* The CPU stops executing instructions and enters a low‑power idle state, and the power to the RAM is maintained. Peripherals such as monitor and hard disk may be turned off. |   |   |
| S2 | CPU powered off. CPU cache is flushed to RAM. |   |   |
| S3 | Commonly referred to as *Standby*, *Sleep*, or *Suspend to RAM (STR)*: RAM remains powered, and RAM enters self refresh mode. Most peripherals are turned off. Fans are usually turned off. Requires GPU drivers on Windows. |   |   |
| S4 | *Hibernation* or *Suspend to Disk:* All content of the main memory is saved to non-volatile memory such as a hard drive, and the system is powered down. |   |   |
| G2 | Soft Off | S5 | *Shutdown:* system is powered down. |
| G3 | Mechanical Off |   | The computer's power has been totally removed via a mechanical switch (as on the rear of a PSU). The power cord can be removed and the system is safe for disassembly (typically, only the real-time clock continues to run using its own small battery). |

The specification also defines a *Legacy* state: the state of an operating system which does not support ACPI. In this state, the hardware and power are not managed via ACPI, effectively disabling ACPI.

#### Device states

The device states *D0*–*D3* are device dependent:

- *D0* or *Fully On* is the operating state.
  - As with S0ix, Intel has *D0ix* states for intermediate levels on the SoC.
- *D1* and *D2* are intermediate power-states whose definition varies by device.
- *D3*: The D3 state is further divided into *D3 Hot* (has auxiliary power), and *D3 Cold* (no power provided):
  - *Hot*: A device can assert power management requests to transition to higher power states.
  - *Cold* or *Off* has the device powered off and unresponsive to its bus.

### Processor states

The CPU power states *C0*–*C3* are defined as follows:

- *C0* is the operating state.
- *C1* (often known as *Halt*) is a state where the processor is not executing instructions, but can return to an executing state essentially instantaneously. All ACPI-conformant processors must support this power state. Some processors, such as the Pentium 4 and AMD Athlon, also support an Enhanced C1 state (*C1E* or Enhanced Halt State) for lower power consumption, however this proved to be buggy on some systems.
- *C2* (often known as *Stop-Clock*) is a state where the processor maintains all software-visible state, but may take longer to wake up. This processor state is optional.
- *C3* (often known as *Sleep*) is a state where the processor does not need to keep its cache coherent, but maintains other state. Some processors have variations on the C3 state (Deep Sleep, Deeper Sleep, etc.) that differ in how long it takes to wake the processor. This processor state is optional.

*Additional states* are defined by manufacturers for some processors. They are reported to the system via the _CST method. For example, Intel's Haswell platform has states up to *C10*, where it distinguishes *core* states and *package* states: the difference being that the *package* not only includes the processor cores, but also components such as the L3 cache, memory controller, and other I/O functions. Similarly, AMD Zen 2 CPUs diffentiate between C-states and P-states for the Core Complex and the Infinity Fabric.

For describing the idle states of groupings of components (e.g. a package containing several cores), the _LPI (low power idle) method is used. This should not be confused with Intel's private LPIT table, used to describe S0ix sleep in package C10 or PCH SLP_S0 state.

### Performance state

While a device or processor operates (D0 and C0, respectively), it can be in one of several power-performance states. These states are implementation-dependent. P0 is always the highest-performance state, with P1 to P*n* being successively lower-performance states. The total number of states is device or processor dependent, but can be no greater than 16.

P-states have become known as SpeedStep in Intel processors, as PowerNow! or Cool'n'Quiet in AMD processors, and as PowerSaver in VIA processors.

- *P0* maximum power and frequency
- *P1* less than *P0*, voltage and frequency scaled
- *P2* less than *P1*, voltage and frequency scaled
- *Pn* less than *P(n–1)*, voltage and frequency scaled

See Dynamic frequency scaling § Autonomous frequency scaling for a brief description of a newer control method based on the ACPI Collaborative Processor Performance Control (CPPC). This new method allows hundreds of possible states, and for the processor to autonomously to choose from a given range of states.

## Interfaces

### Hardware

ACPI-compliant systems interact with hardware through either a "Function Fixed Hardware (FFH) Interface", or a platform-independent hardware programming model which relies on platform-specific ACPI Machine Language (AML) provided by the original equipment manufacturer (OEM).

Function Fixed Hardware interfaces are platform-specific features, provided by platform manufacturers for the purposes of performance and failure recovery. Standard Intel-based PCs have a fixed function interface defined by Intel, which provides a set of core functionality that reduces an ACPI-compliant system's need for full driver stacks for providing basic functionality during boot time or in the case of major system failure.

ACPI Platform Error Interface (APEI) is a specification for reporting of hardware errors, e.g. chipset, RAM to the operating system.

### Firmware

ACPI defines many tables that provide the interface between an ACPI-compliant operating system and system firmware (BIOS or UEFI). This includes RSDP, RSDT, XSDT, FADT, FACS, DSDT, SSDT, MADT, and MCFG, for example.

The tables allow description of system hardware in a platform-independent manner, and are presented as either fixed-formatted data structures or in AML. The main AML table is the DSDT (differentiated system description table). The AML can be decompiled by tools like Intel's iASL (open-source, part of ACPICA) for purposes like patching the tables for expanding OS compatibility.

The Root System Description Pointer (RSDP) is located in a platform-dependent manner, and describes the rest of the tables.

A custom ACPI table called the Windows Platform Binary Table (WPBT) is used by Microsoft to allow vendors to add software into the Windows OS automatically. Lenovo have been caught using this feature to install harmful software such as Superfish. Also, Gigabyte Technology have been found using this feature to install its OEM software. Samsung shipped PCs with Windows Update disabled. Windows versions older than Windows 7 do not support this feature, but alternative techniques can be used. This behavior has been compared to rootkits.

## Criticism

Ubuntu founder Mark Shuttleworth says ACPI is a security risk. He says "arguing for ACPI on your next-generation device is arguing for a trojan horse of monumental proportions to be installed in your living room and in your data centre" and "firmware on your device is the NSA's best friend". He goes on to say, "Your biggest mistake is to assume that the NSA is the only institution abusing this position of trust – in fact, it's reasonable to assume that all firmware is a cesspool of insecurity, courtesy of incompetence of the highest degree from manufacturers, and competence of the highest degree from a very wide range of such agencies." He suggests open-source, declarative firmware (ACPI or non-ACPI) as a solution.

In November 2003, Linus Torvalds—author of the Linux kernel—described ACPI as "a complete design disaster in every way".
