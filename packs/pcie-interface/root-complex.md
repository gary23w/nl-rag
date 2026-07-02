---
title: "Root complex"
source: https://en.wikipedia.org/wiki/Root_complex
domain: pcie-interface
license: CC-BY-SA-4.0
tags: pci express, pcie root complex, message signaled interrupts, serial expansion bus
fetched: 2026-07-02
---

# Root complex

In a PCI Express (PCIe) system, a **root complex** device connects the CPU and memory subsystem to the PCI Express switch fabric composed of one or more PCIe or PCI devices. A root complex is sometimes referred to **PCI root bridge**.

The root complex generates transaction requests on behalf of the CPU, which is interconnected through a local bus. Root complex functionality may be integrated in the chipset and/or the CPU. A root complex may contain more than one PCI Express port and multiple switch devices can be connected to ports on the root complex or cascaded.

## Device Memory Map

The PCIe Root Complex holds a master copy of a 'Type 1 Configuration Table' that defines the host memory space that is accessible from each Endpoint device. In addition, each PCIe Endpoint device holds a master copy of its own memory space map in the host system memory as a 'Type 0 Configuration Table', this configuration table in each device allows the host to access the local memory of a PCIe device. Both the Type 1 and Type 0 configuration tables are set up by the Host Operating System that controls the Root Complex by a process known as enumeration and which acts to build a device memory map for the system by querying each bridge, and endpoint device connected on the bus network. Similarly, a PCIe Bridge acts a tiered root complex with a "Type 0 Configuration Table".
