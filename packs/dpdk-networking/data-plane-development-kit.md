---
title: "Data Plane Development Kit"
source: https://en.wikipedia.org/wiki/Data_Plane_Development_Kit
domain: dpdk-networking
license: CC-BY-SA-4.0
tags: data plane development kit, kernel bypass, packet processing, network processor
fetched: 2026-07-02
---

# Data Plane Development Kit

The **Data Plane Development Kit** (**DPDK**) is an open source software project managed by the Linux Foundation. It provides a set of data plane libraries and network interface controller polling-mode drivers for offloading TCP packet processing from the operating system kernel to processes running in user space. This offloading achieves higher computing efficiency and higher packet throughput than is possible using the interrupt-driven processing provided in the kernel.

DPDK provides a programming framework for x86, ARM, and PowerPC processors and enables faster development of high speed data packet networking applications. It scales from mobile processors, such as Intel Atom, to server-grade processors, such as Intel Xeon. It supports instruction set architectures such as Intel, IBM POWER8, EZchip, and ARM. It is provided and supported under the open-source BSD license.

DPDK was created by Intel engineer Venky Venkatesan, who is affectionately known as "The Father of DPDK." He died in 2018 after a long battle with cancer.

## Overview

The DPDK framework creates a set of libraries for specific hardware/software environments through the creation of an Environment Abstraction Layer (EAL). The EAL hides the environment specifics and provides a standard programming interface to libraries, available hardware accelerators and other hardware and operating system (Linux, FreeBSD) elements. Once the EAL is created for a specific environment, developers link to the library to create their applications. For instance, EAL provides the frameworks to support Linux, FreeBSD, Intel IA-32 or 64-bit, IBM POWER9 and ARM 32- or 64-bit.

The EAL also provides additional services including time references, generic bus access, trace and debug functions and alarm operations.

Using DPDK libraries one can implement a low overhead run-to-completion, pipeline or staged, event driven, or hybrid model completely in userspace eliminating kernel and kernel to user copy. Hardware assists from NIC/Regex/Accelerators, libraries enhanced to make use of Intelligence Storage Acceleration (ISA) for bulk performance and accessing devices via polling helps to eliminate the performance overhead of interrupt too. Hugepages are used for large memory pool allocation, to decrease the amount of lookups and page management.

The DPDK also includes software examples that highlight best practices for software architecture, tips for data structure design and storage, application profiling and performance tuning utilities and tips that address common network performance deficits.

## Libraries

The DPDK includes data plane libraries and optimized network interface controller (NIC) drivers for the following:

- A queue manager implements lockless queues
- A buffer manager pre-allocates fixed size buffers
- A memory manager allocates pools of objects in memory and uses a ring to store free objects; ensures that objects are spread equally on all DRAM channels
- Poll mode drivers (PMD) are designed to work without asynchronous notifications, reducing overhead
- A packet framework – a set of libraries that are helpers to develop packet processing

All libraries are stored in the dpdk/lib/librte_* directories

### Plugins

The DPDK includes drivers for many hardware types. There have been some additional out-of-tree plugin drivers in the past, which are now considered deprecated.

- librte_pmd_vmxnet3.so – provides PMD Ethernet layer supporting Vmxnet3 paravirtualized NIC; superseded by full VMXNET3 support in native DPDK.
- librte_pmd_memnic_copy.so – provides a Virtual PMD Ethernet layer through shared memory based on 2 memory copies of packets

## Environment

The DPDK was originally designed to run using a bare-metal mode which is currently deprecated. DPDK's EAL provides support for Linux or FreeBSD userland application.

EAL can be extended in order to support any processors.

## Ecosystem

DPDK is now an open-source project under the Linux Foundation, supported by many companies. DPDK is governed by a Governing Board. The technical activities are overseen by a Technical Board. Beside Intel, which is a contributor to the DPDK, several other vendors also support the DPDK within their products and some offer additional training, support and professional services. The list of vendors who have announced DPDK support includes: 6WIND, ALTEN Calsoft Labs, Advantech, Brocade, Big Switch Networks, Mellanox Technologies, Radisys, Tieto, Wind River, Lanner Inc. and NXP.

## Projects

The pfSense project published a road map on 25 February 2015, in which developer Jim Thompson announced the rewriting of the pfSense core—including pf, network packet forwarding and shaping, link bonding, IPsec—using DPDK: "We have a goal of being able to forward, with packet filtering at rates of at least 14.88 Mpps. This is 'line rate' on a 10 Gbps interface. There is simply no way to use today's FreeBSD (or Linux) in-kernel stacks for this type of load."

Open vSwitch (OVS) has a limited set of features running userland that can be leveraged to bypass the Linux kernel OVS processing. This use case of OVS with DPDK userland is usually named OVS-DPDK. It is mostly deployed with OpenStack Neutron but it assumes that many features and software-defined networking (SDN) capabilities of Openstack are disabled. For instance, when OVS-DPDK is used, Neutron provides a lower level of security than when OVS kernel is used (no stateful firewalling, less security group).

The FD.IO VPP platform is an extensible framework that provides out-of-the-box production quality switch/router functionality. It is the open source version of Cisco's Vector Packet Processing (VPP) technology: a high performance, packet-processing stack that can run on commodity CPUs, and can leverage the Poll Mode Drivers for both NICs and cryptographic acceleration hardware and libraries. VPP supports and uses the DPDK library.

TRex is an open source traffic generator using DPDK. It generates L4–7 traffic based on pre-processing and smart replay of real traffic templates. TRex amplifies both client and server side traffic and can scale to 200 Gbit/s with one UCS using Intel XL710. TRex also supports multiple streams, ability to change any packet field and provides per stream statistics, latency and jitter.

DTS (DPDK Test Suite) is a Python-based framework for functional tests and benchmarks. It is an open-source project, started in 2014, and is hosted on dpdk.org. It supports both software traffic generators like Scapy and dpdk-pktgen, and a hardware traffic generator like Ixia.

DPDK has support for several SRIOV network drivers, enabling creating a PF (Physical Function) and VFs, and also to launch VMs (like QEMU VMs) and assign VFs to them using PCI Passthrough

DDP (Dynamic Device Personalization) is one of the new advanced features implemented with DPDK. It allows you to load firmware for a device dynamically, without resetting the host.
