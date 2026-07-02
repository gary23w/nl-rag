---
title: "Mbed"
source: https://en.wikipedia.org/wiki/Mbed
domain: mbed-os
license: CC-BY-SA-4.0
tags: mbed os, arm mbed, cortex-m platform, cmsis abstraction
fetched: 2026-07-02
---

# Mbed

**Mbed** is a development platform and operating system for internet-connected devices (Internet of Things devices) based on 32-bit ARM Cortex-M microcontrollers. The project was a collaboratively developed by Arm and its technology partners. As of July 2024 Mbed is no longer actively developed by Arm.

The full version is a real-time operating system (RTOS) while more resource constrained devices can opt to use a non-RTOS subset.

## Development Environment

The platform offers a development environment that includes:

- Mbed OS: The core operating system that offers standardized APIs and supports C/C++ programming languages.
- Mbed Studio: An IDE (Integrated Development Environment) that provides debugging tools and code editors.
- Mbed CLI: Command-line tools.

## Software development

### Applications

The primary way of developing Mbed applications is with the Arm Online Ide "Keil Studio Cloud" which is an online ide that uses cloud services to build and compile mbed applications. Applications can be developed also with other development environments such as Keil μVision, IAR Embedded Workbench, Arduino IDE and Eclipse with GCC ARM Embedded tools.

### Mbed OS

Mbed OS provides the Mbed C/C++ software platform and tools for creating microcontroller firmware that runs on IoT devices. It consists of the core libraries that provide the microcontroller peripheral drivers, networking, RTOS and runtime environment, build tools and test and debug scripts. These connections can be secured by compatible SSL/TLS libraries such as Mbed TLS or wolfSSL, which supports mbed-rtos.

A components database provides driver libraries for components and services that can be connected to the microcontrollers to build a final product.

Mbed OS, the RTOS, is based on Keil RTX5.

## Major Release History

| Series | Status | First Release | Last Release | Description |
|---|---|---|---|---|
| Mbed 2 ("mbedlib" or "mbed SDK") | Deprecated, but still supported by Keil Studio Cloud | Oct 8, 2009 | r163 (Feb 2019) | The original release series of Mbed. Initially it ran on the Mbed NXP LPC1768 board, but support was soon added for other boards from a number of manufacturers. It did not contain a real-time OS and relied on community libraries for many common features such as networking and threading. |
| Mbed OS 3 | Abandoned | 15.09 (September 2015) | 16.03 (March 2016) | Mbed 3.0 was a significant rewrite of the original Mbed codebase to add features key for Internet of Things (IoT) functionality, such as wireless networking and TLS encryption. However, it relied on writing event-driven programs and did not support traditional multithreading, limiting its adoption. Mbed 3.0 introduced a new build system called Yotta. This allowed Mbed to be broken down into a large number of individual modules, each with their own repository. However, Yotta was not used by Mbed after the Mbed 3.x release series. |
| Mbed OS 5.x | Deprecated, but still supported by Keil Studio Cloud | 5.1.0 (August 2016) | 5.15.9 (May 2022) | Mbed OS 5 combined functionality from the original Mbed 2 codebase, the mbed-rtos project, and Mbed OS 3.0 into a single codebase which could support a wide range of use cases, from basic microcontroller functionality to wireless communications and advanced IoT features. Mbed OS 5 once again used a new custom build system, "Mbed CLI". However, it returned to a monolithic repository structure, with all drivers and first-party functionality integrated in a single Git repository. |
| Mbed OS 6.x | Abandoned | 6.0.0 (June 2020) | 6.17.0 (Feb 2023) | Mbed OS 6 was a more incremental change from Mbed OS 5. It reorganized and cleaned up the codebase in a number of ways, such as deprecating old APIs and reshuffling the directory structure to group together code more logically. It also pared down the list of supported boards, focusing effort on a smaller number of target devices with which ARM had an active relationship with the manufacturer. Mbed OS 6 still supports the Mbed CLI build system, but later versions also added support for a new build system, "Mbed CLI 2". This build system uses modified CMake scripts to compile Mbed, with a Python wrapper on top for users to interact with. In order to support their ARM Clang compiler in this build system, ARM contributed a port of CMake to ARM Clang. On July the 9th 2024 it was announced that *The Mbed platform and OS will reach end of life in July 2026 ...* and *Arm has already halted active maintenance and CI on the Mbed OS codebase. You should not expect to see any fixes or improvements before July 2026. After July 2026, the codebase will be archived in GitHub.* |

## Hardware development

### Demo-boards

There are various hardware demo-boards for the Mbed platform, with the first being the original Mbed Microcontroller board. The Mbed Microcontroller Board (marketed as the "mbed NXP LPC1768") is a demo-board based on an NXP microcontroller, which has an ARM Cortex M3 core, running at 96 MHz, with 512 KB flash, 32 KB RAM, as well as several interfaces including Ethernet, USB Device, CAN, SPI, I2C and other I/O. The Mbed microcontroller received first prize in the annual EDN Innovation Awards' Software/Embedded Tools category in 2010.

Various versions of the board were released, with NXP LPC2368 (ARM7TDMI-S), NXP LPC1768 (Cortex-M3), NXP LPC11U24 (Cortex-M0) microcontrollers.

### HDK

The Mbed hardware development kit (HDK) is designed for OEMs, and provides information to build custom hardware to support Mbed OS. This consists of interface firmware and schematics that can be used to easily create development boards, OEM modules and re-programmable products suitable for production.

## Project development

The project is developed by Arm in conjunction with other major technology companies and the Mbed developer community. Development and contributions happen at different levels:

- Core Platform – The core software platform, developed by core contributors and partner companies and managed and maintained by the Mbed team. This core platform is developed under the Apache License 2.0 via a contributor agreement. This includes all the core generic software components the platform provides, plus the HAL ports that allow Mbed to transparently run on different manufacturers microcontrollers and the toolchain ports that allow development using different embedded toolchains.
- Component Database – Library components, developed by companies and the wider community, to provide support for peripheral components, sensors, radios, protocols and cloud service apis needed to build end devices. These are contributed under the Apache License 2.0 (encouraged) or other licenses chosen by the creators, and supported by those individual companies and members of the developer community

## Development Tools

Mbed OS supports, and has supported, a number of different development tools.

### Mbed Online Compiler (Deprecated since 2022)

Applications for the Mbed platform could be developed using the Mbed online IDE, a free online code editor and compiler. Only a web browser is needed to be installed on the local PC, since projects were compiled on the cloud, i.e. on a remote server, using the ARMCC C/C++ compiler. The Mbed IDE provided private workspaces with ability to import, export, and share code with distributed Mercurial version control, and could be used also for code documentation generation.

Mbed Online Compiler did not include any debugging functionality, and relied on a development cycle where users would download their compiled code as a .bin file, then manually copy it to an Mbed board (which appears as a USB flash drive).

Mbed Online Compiler was shut down on March 1, 2023, and replaced by Keil Studio Cloud.

### Mbed CLI

To satisfy the need for offline development of Mbed OS, ARM made available the Mbed CLI. This is a Python package that allows creating, importing, and compiling Mbed OS programs from the command line. It also integrates with external Git repositories and with Mbed's library repository, offering commands to download and update libraries from remote sources.

Internally, Mbed CLI consists of two different codebases. The mbed-cli pip package, offering the mbed command, acts as a frontend that accepts commands from the user and is capable of downloading Mbed OS and libraries. In order to compile Mbed and software using it, the mbed-cli frontend calls into build tool scripts inside the mbed-os repository. These scripts are responsible for determining the correct compile options and executing the compiler and linker.

After years of development, maintenance of the complex build tool scripts had become a significant burden to the Mbed OS developers. This led them to freeze the build tool code and work towards creating Mbed CLI 2 instead.

### Mbed Studio

Mbed Studio is a desktop IDE designed specifically to work with Mbed OS. First released in February 2019, Mbed Studio offered a more fully featured editing experience than the online compiler, including intelligent code completion functionality and debugging support. Like the online compiler, it contains built-in support for creating new Mbed projects and declaring dependencies on libraries from Git repositories and Mbed's library repository.

For its C/C++ compiler, Mbed Studio uses Arm Compiler 6, specially licensed by ARM for inclusion in the IDE. For debugging functionality, Mbed Studio uses the pyOCD debug bridge software and can only debug the devices that pyOCD supports. The IDE itself is based on Eclipse Theia, and was designed to be easily adapted to running in a web browser -- a project that later came into existence as Keil Studio Cloud. Mbed Studio initially supported Windows and Mac host platforms, and was later ported to run on Ubuntu Linux with its 1.0 release in June 2020.

### Keil Studio Cloud

Similar to Mbed Online Compiler, Keil Studio Cloud allows development of Mbed OS applications without installation of any development tools on the local machine. However, it supports many additional features, such as improved intelligent code completion functionality and built-in version control using Git. Unlike the Online Compiler, Keil Studio Cloud is capable of downloading to and debugging supported Mbed boards directly from the browser using WebUSB functionality. This allows a truly one-click build and debug experience comparable to what is offered by desktop IDEs. However, this functionality does not support all Mbed boards or debug probes.
