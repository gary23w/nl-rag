---
title: "menuconfig"
source: https://en.wikipedia.org/wiki/Kconfig
domain: zephyr-rtos
license: CC-BY-SA-4.0
tags: zephyr rtos, zephyr project, device tree, kconfig build
fetched: 2026-07-02
---

# menuconfig

(Redirected from

Kconfig

)

`**make menuconfig**` is one of five similar tools that can assist a user in configuring the Linux kernel before building, a necessary step needed to compile the source code. `make menuconfig`, with a menu-driven user interface, allows the user to choose which features and modules to compile. It is normally invoked using the command `make menuconfig`; menuconfig is a target in the Linux Makefile.

## Overview

`make menuconfig` was not in the first version of Linux. Prior to 2.5.45, the predecessor tool used Configuration Menu Language (CML) and was a question-and-answer-based utility (`make config`, `make oldconfig`).

Variations of the tool for Linux configuration include:

- `make xconfig`, which requires Qt
- `make gconfig`, which uses GTK+
- `make nconfig`, which is similar to `make menuconfig`.

All these tools use the **Kconfig** language internally. Kconfig is also used in other projects, such as Das U-Boot, a bootloader for embedded devices, Buildroot, a tool for generating embedded Linux systems, and BusyBox, a single-executable shell utility toolbox for embedded systems.

`make menuconfig` is generally more user-friendly compared to the question-and-answer-based configuration tool `make config`, and has a basic search system.

If the user is satisfied with a previous `.config` file, using `make oldconfig` uses this previous file to answer all questions that it can, only interactively presenting the new features.

## Dependencies

To use `make menuconfig`, Linux source is a requirement, a make tool, a C compiler, and the ncurses library.
