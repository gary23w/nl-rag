---
title: "Devicetree"
source: https://en.wikipedia.org/wiki/Device_tree
domain: barebox
license: CC-BY-SA-4.0
tags: barebox bootloader, second-stage loader, device tree boot, u-boot alternative
fetched: 2026-07-02
---

# Devicetree

(Redirected from

Device tree

)

In computing, a **devicetree** (also written **device tree**) is a data structure describing the hardware components of a particular computer so that the operating system's kernel can use and manage those components, including the CPU or CPUs, the memory, the buses and the integrated peripherals.

The device tree was derived from SPARC-based and PowerPC-based computers via the Open Firmware project. The current Devicetree specification is targeted at smaller systems and embedded systems, but is still used with some server-class systems (for instance, those described by the Power Architecture Platform Reference).

Personal computers with the x86 architecture generally do not use device trees, relying instead on various auto configuration protocols (e.g. ACPI) to discover hardware. Systems which use device trees usually pass a static device tree (perhaps stored in EEPROM, or stored in NAND device like eUFS) to the operating system, but can also generate a device tree in the early stages of booting. As an example, Das U-Boot and kexec can pass a device tree when launching a new operating system. On systems with a boot loader that does not support device trees, a static device tree may be installed along with the operating system; the Linux kernel supports this approach.

The Devicetree specification is currently managed by a community named devicetree.org, which is associated with, among others, Linaro and Arm.

## Formats

A device tree can hold any kind of data as internally it is a tree of named nodes and properties. Nodes contain properties and child nodes, while properties are name–value pairs.

Device trees have both a binary format for operating systems to use and a textual format for convenient editing and management.

## Usage

### Linux

Given the correct device tree, the same compiled kernel can support different hardware configurations within a wider architecture family. The Linux kernel for the ARC, ARM, C6x, H8/300, MicroBlaze, MIPS, NDS32, Nios II, OpenRISC, PowerPC, Power ISA, RISC-V, SuperH, and Xtensa architectures reads device tree information; on ARM, device trees have been mandatory for all new SoCs since 2012. This can be seen as a remedy to the vast number of forks (of Linux and Das U-Boot) that have historically been created to support (marginally) different ARM boards. The purpose is to move a significant part of the hardware description out of the kernel binary, and into the compiled device tree blob, which is handed to the kernel by the boot loader, replacing a range of board-specific C source files and compile-time options in the kernel.

It is specified in a Devicetree Source file (.dts) and is compiled into a Devicetree Blob or device tree binary (.dtb) file (also known as the flattened device tree) through the Devicetree compiler (DTC). Device tree source files can include other files, referred to as device tree source includes.

It has been customary for ARM-based Linux distributions to include a boot loader that necessarily was customized for specific boards, for example Raspberry Pi or Hackberry A10. This has created problems for the creators of Linux distributions as some part of the operating system must be compiled specifically for every board variant, or updated to support new boards. However, some modern SoCs (for example, Freescale i.MX6) have a vendor-provided boot loader with device tree on a separate chip from the operating system.

A proprietary configuration file format used for similar purposes, the FEX file format, is a de facto standard among Allwinner SoCs.

Devicetree is widely used for ARM-based Android devices.

### BSD

BSD can support device tree, as device tree usually adopted on embedded devices.

### Windows

Windows does not use Devicetree (DTB file) as described here. Instead, it uses ACPI to discover and manage devices.

### Apple

On the boot process of iOS, iPadOS and ARM macOS, the Low-Level Bootloader (LLB) will load Apple-encrypted devicetree to main memory, then loads iBoot.

### Coreboot

The coreboot project makes use of device trees, but they are different from the flattened device trees used in the Linux kernel.

## Example

Example of Devicetree Source (DTS) format:

```mw
/dts-v1/;

/ {
    soc {
        flash_controller: flash-controller@4001e000 {
            reg = <0x4001e000 0x1000>;
            flash0: flash@0 {
                label = "SOC_FLASH";
                erase-block = <4096>;
            };
        };
    };
};
```

In the example above, the line `/dts-v1/;` signifies version 1 of the DTS syntax.

The tree has four nodes: `/` (root node), `soc` (stands for "system on a chip"), `flash-controller@4001e000` and `flash@0` (instance of flash which uses the flash controller). Besides these *node names*, the latter two nodes have *labels* `flash_controller` and `flash0` respectively.

The latter two nodes have *properties*, which represent name/value pairs. Property `label` has string type, property `erase-block` has integer type and property `reg` is an array of integers (32-bit unsigned values). Property values can refer to other nodes in the devicetree by their *phandles*. Phandle for a node with label `flash0` would be written as `&flash0`. Phandles are also 32-bit values.

Parts of the node names after the "at" sign (`@`) are *unit addresses*. Unit addresses specify a node's resource address in the address space of its parent node.

The above tree could be compiled by the standard DTC compiler to binary DTB format or assembly. In Zephyr RTOS, however, DTS files are compiled into C header files (.h), which are then used by the build system to compile code for a specific board.
