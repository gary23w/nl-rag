---
title: "Hyper-V"
source: https://en.wikipedia.org/wiki/Hyper-V
domain: wsl-subsystem
license: CC-BY-SA-4.0
tags: windows subsystem for linux, wsl subsystem, subsystem for android, windows terminal
fetched: 2026-07-02
---

# Hyper-V

**Hyper-V** is a native hypervisor developed by Microsoft; it can create virtual machines on x86-64 systems running Windows. It is included in Pro and Enterprise editions of Windows (since Windows 8) as an optional feature to be manually enabled. A server computer running Hyper-V can be configured to expose individual virtual machines to one or more networks.

## Overview

Codenamed **Viridian** and briefly known before its release as **Windows Server Virtualization**, a beta version was shipped with certain x86-64 editions of Windows Server 2008. The finalized version was released on June 26, 2008 and was delivered through Windows Update. Hyper-V has since been released with every version of Windows Server starting with version 2012, superseding Microsoft Virtual Server, and starting with Windows 8, Hyper-V has been the hardware virtualization component for personal computers, superseding Windows Virtual PC.

Former Hyper-V logo

Former Hyper-V Server wordmark

Microsoft provides Hyper-V through two channels:

1. Part of Windows: Hyper-V is an optional component of Windows Server 2008 and later. It is also available in x64 SKUs of Pro and Enterprise editions of Windows 8, Windows 8.1, Windows 10 and Windows 11.
2. Hyper-V Server: It is a freeware edition of Windows Server with limited functionality and Hyper-V component.

### Hyper-V Server

Hyper-V Server 2008 was released on October 1, 2008. It consists of Windows Server 2008 Server Core and Hyper-V role; other Windows Server 2008 roles are disabled, and there are limited Windows services. Hyper-V Server 2008 is limited to a command-line interface used to configure the host OS, physical hardware, and software. A menu driven command line interface (CLI) and some freely downloadable script files simplify configuration. In addition, Hyper-V Server supports remote access via Remote Desktop Connection. However, administration and configuration of the host OS and the guest virtual machines is generally done over the network, using either Microsoft Management Consoles on another Windows computer or System Center Virtual Machine Manager. This allows much easier "point and click" configuration, and monitoring of the Hyper-V Server.

Hyper-V Server 2008 R2 (an edition of Windows Server 2008 R2) was made available in September 2009 and includes Windows PowerShell v2 for greater CLI control. Remote access to Hyper-V Server requires CLI configuration of network interfaces and Windows Firewall. Also using a Windows Vista PC to administer Hyper-V Server 2008 R2 is not fully supported.

Microsoft ended mainstream support of the free version of Hyper-V Server 2019 on January 9, 2024 and extended support will end on January 9, 2029. Hyper-V Server 2019 will be the last version of the free, standalone product. Hyper-V is still available as a role in Windows Server 2022 and will be supported as long as that operating system is, currently scheduled for end of extended support on October 14, 2031.

## Architecture

Hyper-V implements isolation of virtual machines in terms of a *partition*. A partition is a logical unit of isolation, supported by the hypervisor, in which each guest operating system executes. There must be at least one *parent partition* in a hypervisor instance, running a supported version of Windows. The parent partition creates *child partitions* which host the guest OSs. The Virtualization Service Provider and Virtual Machine Management Service runs in the parent partition and provide support for child partition. A parent partition creates child partitions using the *hypercall* API, which is the application programming interface exposed by Hyper-V.

A child partition does not have access to the physical processor, nor does it handle its real interrupts. Instead, it has a virtual view of the processor and runs in *Guest Virtual Address*, which, depending on the configuration of the hypervisor, might not necessarily be the entire virtual address space. Depending on VM configuration, Hyper-V may expose only a subset of the processors to each partition. The hypervisor handles the interrupts to the processor, and redirects them to the respective partition using a logical *Synthetic Interrupt Controller* (SynIC). Hyper-V can hardware accelerate the address translation of Guest Virtual Address-spaces by using second level address translation provided by the CPU, referred to as EPT on Intel and RVI (formerly NPT) on AMD.

Child partitions do not have direct access to hardware resources, but instead have a virtual view of the resources, in terms of *virtual devices*. Any request to the virtual devices is redirected via the *VMBus* to the devices in the parent partition, which will manage the requests. The VMBus is a logical channel which enables inter-partition communication. The response is also redirected via the VMBus. If the devices in the parent partition are also virtual devices, it will be redirected further until it reaches the parent partition, where it will gain access to the physical devices. Parent partitions run a *Virtualization Service Provider* (VSP), which connects to the VMBus and handles device access requests from child partitions. Child partition virtual devices internally run a *Virtualization Service Client* (VSC), which redirect the request to VSPs in the parent partition via the VMBus. This entire process is transparent to the guest OS.

Virtual devices can also take advantage of a Windows Server Virtualization feature, named *Enlightened I/O*, for storage, networking and graphics subsystems, among others. Enlightened I/O is a specialized virtualization-aware implementation of high level communication protocols, like SCSI, that allows bypassing any device emulation layer and takes advantage of VMBus directly. This makes the communication more efficient, but requires the guest OS to support Enlightened I/O.

Currently only the following operating systems support Enlightened I/O, allowing them therefore to run faster as guest operating systems under Hyper-V than other operating systems that need to use slower emulated hardware:

- Windows Server 2008 and later
- Windows Vista and later
- Linux with a 3.4 or later kernel
- FreeBSD

## System requirements

The Hyper-V role is only available in the x86-64 variants of Standard, Enterprise and Datacenter editions of Windows Server 2008 and later, as well as the Pro, Enterprise and Education editions of Windows 8 and later. On Windows Server, it can be installed regardless of whether the installation is a full or core installation. In addition, Hyper-V can be made available as part of the Hyper-V Server operating system, which is a freeware edition of Windows Server. Either way, the host computer needs the following.

- CPU with the following technologies:
  - NX bit
  - x86-64
  - Hardware-assisted virtualization (Intel VT-x or AMD-V)
  - Second Level Address Translation (in Windows 8 and later)
- At least 2 GB memory, in addition to what is assigned to each guest machine

The amount of memory assigned to virtual machines depends on the operating system:

- Windows Server 2008 Standard supports up to 31 GB of memory for running VMs, plus 1 GB for the host OS.
- Windows Server 2008 R2 Standard supports up to 32 GB, but the Enterprise and Datacenter editions support up to 2 TB. Hyper-V Server 2008 R2 supports up to 1 TB.
- Windows Server 2012 supports up to 4 TB.

The number of CPUs assigned to each virtual machine also depends on the OS:

- Windows Server 2008 and 2008 R2 support 1, 2, or 4 CPUs per VM; the same applies to Hyper-V Server 2008 R2
- Windows Server 2012 supports up to 64 CPUs per VM

There is also a maximum for the number of concurrently active virtual machines.

- Windows Server 2008 and 2008 R2 support 384 per server; Hyper-V Server 2008 supports the same
- Windows Server 2012 supports 1024 per server; the same applies to Hyper-V Server 2012
- Windows Server 2016 supports 8000 per cluster and per node

## Supported guests

### Windows Server 2008 R2

The following table lists supported guest operating systems on Windows Server 2008 R2 SP1.

| Guest operating system | Virtual CPUs |   |   |
|---|---|---|---|
| OS | Editions | Number | Architecture |
| Windows Server 2012 | Hyper-V, Standard, Datacenter | 1–4 | x86-64 |
| Windows Home Server 2011 | Standard | 1–4 | x86-64 |
| Windows Server 2008 R2 SP1 | Web, Standard, Enterprise, Datacenter | 1–4 | x86-64 |
| Windows Server 2008 SP2 | Web, Standard, Enterprise, Datacenter | 1–4 | IA-32, x86-64 |
| Windows Server 2003 R2 SP2 | Web, Standard, Enterprise, Datacenter | 1 or 2 | IA-32, x86-64 |
| Windows 2000 SP4 | Professional, Server, Advanced Server | 1 | IA-32 |
| Windows 7 | Professional, Enterprise, Ultimate | 1–4 | IA-32, x86-64 |
| Windows Vista | Business, Enterprise, Ultimate | 1–4 | IA-32, x86-64 |
| Windows XP SP3 | Professional | 1 or 2 | IA-32 |
| Windows XP SP2 | Professional, Professional x64 Edition | 1 | IA-32, x86-64 |
| SUSE Linux Enterprise Server 10 SP4 or 11 SP1–SP3 | —N/a | 1–4 | IA-32, x86-64 |
| Red Hat Enterprise Linux 5.5–7.0 | Red Hat Compatible Kernel | 1–4 | IA-32, x86-64 |
| CentOS 5.5–7.5 | —N/a | 1–4 | IA-32, x86-64 |
| Ubuntu 12.04–20.04 | Debian Compatible Kernel | 1–4 | IA-32, x86-64 |
| Debian 7.0 | Debian Compatible Kernel | 1–4 | IA-32, x86-64 |
| Oracle Linux 6.4 | Red Hat Compatible Kernel | 1–4 | IA-32, x86-64 |

1. Windows Server 2012 is supported and runs only on a host system Windows Server 2008 R2 RTM or SP1, with a hotfix applied.
2. Web edition does not have an x64 version.

Fedora 8 or 9 are unsupported; however, they have been reported to run.

Third-party support for FreeBSD 8.2 and later guests is provided by a partnership between NetApp and Citrix. This includes both emulated and paravirtualized modes of operation, as well as several HyperV integration services.

Desktop virtualization (VDI) products from third-party companies (such as Quest Software vWorkspace, Citrix XenDesktop, Systancia AppliDis Fusion and Ericom PowerTerm WebConnect) provide the ability to host and centrally manage desktop virtual machines in the data center while giving end users a full PC desktop experience.

Guest operating systems with *Enlightened I/O* and a hypervisor-aware kernel such as Windows Server 2008 and later server versions, Windows Vista SP1 and later clients and offerings from Citrix XenServer and Novell will be able to use the host resources better since VSC drivers in these guests communicate with the VSPs directly over VMBus. Non-"enlightened" operating systems will run with emulated I/O; however, *integration components* (which include the VSC drivers) are available for Windows Server 2003 SP2, Windows Vista SP1 and Linux to achieve better performance.

### Linux support

On July 20, 2009, Microsoft submitted Hyper-V drivers for inclusion in the Linux kernel under the terms of the GPL. Microsoft was required to submit the code when it was discovered that they had incorporated a Hyper-V network driver with GPL-licensed components statically linked to closed-source binaries. Kernels beginning with 2.6.32 may include inbuilt Hyper-V paravirtualization support which improves the performance of virtual Linux guest systems in a Windows host environment. Hyper-V provides basic virtualization support for Linux guests out of the box. Paravirtualization support requires installing the Linux Integration Components or Satori InputVSC drivers. Xen-enabled Linux guest distributions may also be paravirtualized in Hyper-V. As of 2013 Microsoft officially supported only SUSE Linux Enterprise Server 10 SP1/SP2 (x86 and x64) in this manner, though any Xen-enabled Linux should be able to run. In February 2008, Red Hat and Microsoft signed a virtualization pact for hypervisor interoperability with their respective server operating systems, to enable Red Hat Enterprise Linux 5 to be officially supported on Hyper-V.

### Windows Server 2012

Hyper-V in Windows Server 2012 and Windows Server 2012 R2 changes the support list above as follows:

1. Hyper-V in Windows Server 2012 adds support for Windows 8.1 (up to 32 CPUs) and Windows Server 2012 R2 (64 CPUs); Hyper-V in Windows Server 2012 R2 adds support for Windows 10 (32 CPUs) and Windows Server 2016 (64 CPUs).
2. Minimum supported version of CentOS is 6.0.
3. Minimum supported version of Red Hat Enterprise Linux is 5.7.
4. Maximum number of supported CPUs for Windows Server and Linux operating systems is increased from four to 64.

### Windows Server 2012 R2

Hyper-V on Windows Server 2012 R2 added the Generation 2 VM.

## Backward compatibility

Hyper-V, like Microsoft Virtual Server and Windows Virtual PC, saves each guest OS to a single virtual hard disk file. It supports the older .vhd format, as well as the newer .vhdx. Older .vhd files from Virtual Server 2005, Virtual PC 2004 and Virtual PC 2007 can be copied and used in Hyper-V, but any old virtual machine integration software (equivalents of Hyper-V Integration Services) must be removed from the virtual machine. After the migrated guest OS is configured and started using Hyper-V, the guest OS will detect changes to the (virtual) hardware. Installing "Hyper-V Integration Services" installs five services to improve performance, at the same time adding the new guest video and network card drivers.

## Limitations

### Audio

Hyper-V does not virtualize audio hardware. Before Windows 8.1 and Windows Server 2012 R2, it was possible to work around this issue by connecting to the virtual machine with Remote Desktop Connection over a network connection and use its audio redirection feature. Windows 8.1 and Windows Server 2012 R2 add the enhanced session mode which provides redirection without a network connection.

### Optical drives pass-through

Optical drives virtualized in the guest VM are read-only. Officially Hyper-V does not support the host/root operating system's optical drives to pass-through in guest VMs. As a result, burning to discs, audio CDs, video CD/DVD-Video playback are not supported; however, a workaround exists using the iSCSI protocol. Setting up an iSCSI target on the host machine with the optical drive can then be talked to by the standard Microsoft iSCSI initiator. Microsoft produces their own iSCSI Target software or alternative third party products can be used.

### VT-x/AMD-V handling

Hyper-V uses the VT-x on Intel or AMD-V on AMD x86 virtualization. Since Hyper-V is a native hypervisor, as long as it is installed, third-party software cannot use VT-x or AMD-V. For instance, the Intel HAXM Android device emulator (used by Android Studio or Microsoft Visual Studio) cannot run while Hyper-V is installed.

### Performance degradation

Hyper-V is a native hypervisor, and enabling Hyper-V on host Windows operating system downloads and installs additional components to the operating system. Enabling Hyper-V may cause performance degradation on hosts, even if no Hyper-V virtual machine is running.

## Client operating systems

Hyper-V is also available in x64 SKUs of Windows 8, 8.1, 10 Pro, Enterprise, Education. The following features are not available on client versions of Windows:

- Live migration of virtual machines from one host to another
- Hyper-V Replica
- Virtual Fiber Channel
- SR-IOV networking
- Shared .VHDX

The following features are not available on server versions of Windows:

- Quick Create and the VM Gallery
- Default network (NAT switch)

## Feature changes per version

### Windows Server 2012

Windows Server 2012 introduced many new features in Hyper-V.

- Hyper-V Extensible Virtual Switch
- Network virtualization
- Multi-tenancy
- Storage Resource Pools
- .vhdx disk format supporting virtual hard disks as large as 64 TB with power failure resiliency
- Virtual Fibre Channel
- Offloaded data transfer
- Virtual Machine Queue (VMQ)
- Hyper-V replica
- Cross-premises connectivity
- Cloud backup

### Windows Server 2012 R2

With Windows Server 2012 R2 Microsoft introduced another set of new features.

- Shared virtual hard disk
- Storage quality of service
- Generation 2 Virtual Machine
- Enhanced session mode
- Automatic virtual machine activation

### Windows Server 2016

Hyper-V in Windows Server 2016 and Windows 10 1607 adds

- Nested virtualization (Intel processors only, both the host and guest instances of Hyper-V must be Windows Server 2016 or Windows 10 or later)
- Discrete Device Assignment (DDA), allowing direct pass-through of compatible PCI Express devices to guest Virtual Machines
- Windows containers (to achieve isolation at the app level rather than the OS level)
- Shielded VMs using remote attestation servers
- Monitoring of host CPU resource utilization by guests and protection (limiting CPU usage by guests)

### Windows Server 2019

Hyper-V in Windows Server 2019 and Windows 10 1809 adds

- Shielded Virtual Machines improvements including Linux compatibility
- Virtual Machine Encrypted Networks
- vSwitch Receive Segment Coalescing
- Dynamic Virtual Machine Multi-Queue (d. VMMQ)
- Persistent Memory support
- Significant feature and performance improvements to Storage Spaces Direct and Failover Clustering

### Windows Server 2022

Hyper-V in Windows Server 2022 added:

- nested virtualization for AMD processors
- updated Receive Segment Coalescing (RSC) for virtual switches

### Windows Server 2025

Hyper-V in Windows Server 2025 changes:

- Generation 2 is now the default option in the New Virtual Machine Wizard in Hyper-V Manager
- GPU Partitioning (share a GPU between VMs)
- Hypervisor-enforced paging translation (HPVT)
- Support for 4 petabytes of memory and 2,048 logical processors per Hyper-V host
- Workgroup clusters (support for failover clusters without an Active Directory)
