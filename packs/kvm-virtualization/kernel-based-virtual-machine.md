---
title: "Kernel-based Virtual Machine"
source: https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine
domain: kvm-virtualization
license: CC-BY-SA-4.0
tags: kvm, kernel-based virtual machine, hardware-assisted virtualization, libvirt
fetched: 2026-07-02
---

# Kernel-based Virtual Machine

**Kernel-based Virtual Machine** (**KVM**) is a free and open-source virtualization module in the Linux kernel that allows the kernel to function as a hypervisor. It was merged into the mainline Linux kernel in version 2.6.20, which was released on February 5, 2007. KVM requires a processor with hardware virtualization extensions, such as Intel VT or AMD-V. KVM has also been ported to other operating systems such as FreeBSD and illumos in the form of loadable kernel modules.

KVM was originally designed for x86 processors but has since been ported to z/Architecture, PowerPC, IA-64, and ARM. The IA-64 port was removed in 2014.

KVM supports hardware-assisted virtualization for a wide variety of guest operating systems including BSD, Solaris, Windows, Haiku, ReactOS, Plan 9, AROS, macOS, and even other Linux systems. In addition, Android 2.2, GNU/Hurd (Debian K16), Minix 3.1.2a, Solaris 10 U3 and Darwin 8.0.1, together with other operating systems and some newer versions of these listed, are known to work with certain limitations.

Additionally, KVM provides paravirtualization support for Linux, OpenBSD, FreeBSD, NetBSD, Plan 9 and Windows guests using the VirtIO API. This includes a paravirtual Ethernet card, disk I/O controller, balloon driver, and a VGA graphics interface using SPICE or VMware drivers.

## History

Avi Kivity began the development of KVM in mid-2006 at Qumranet, a technology startup company that was acquired by Red Hat in 2008.

KVM surfaced in October 2006 and was merged into the Linux kernel mainline in version 2.6.20, released on 5 February 2007.

KVM is maintained by Paolo Bonzini.

## Internals

KVM provides device abstraction but no processor emulation. It exposes the /dev/kvm interface, which a user mode host can then use to:

- Set up the guest VM's address space. The host must also supply a firmware image (usually a custom BIOS when emulating PCs) that the guest can use to bootstrap into its main OS.
- Feed the guest simulated I/O.
- Map the guest's video display back onto the system host.

Originally, a forked version of QEMU was provided to launch guests and deal with hardware emulation that is not handled by the kernel. That support was eventually merged into the upstream project. There are now numerous Virtual Machine Monitors (VMMs) which can utilise the KVM interface including kvmtool, crosvm and Firecracker and numerous specialised VMMs built with frameworks such as rust-vmm.

Internally, KVM uses SeaBIOS as an open source implementation of a 16-bit x86 BIOS.

## Features

KVM has had support for hot swappable vCPUs, dynamic memory management, and Live Migration since February 2007. It also reduces the impact that memory write-intensive workloads have on the migration process.

## Emulated hardware

KVM itself emulates very little hardware, instead deferring to a higher level client application such as QEMU, crosvm, or Firecracker for device emulation.

KVM provides the following emulated devices:

- Virtual CPU and memory
- VirtIO

## Graphical management tools

- Kimchi – web-based virtualization management tool for KVM
- Virtual Machine Manager – supports creating, editing, starting, and stopping KVM-based virtual machines, as well as live or cold drag-and-drop migration of VMs between hosts.
- Proxmox Virtual Environment – an open-source virtualization management package including KVM and LXC. It has a bare-metal installer, a web-based remote management GUI, a HA cluster stack, unified storage, flexible network, and optional commercial support.
- OpenQRM – management platform for managing heterogeneous data center infrastructures
- GNOME Boxes – Gnome interface for managing libvirt guests on Linux
- oVirt – open-source virtualization management tool for KVM built on top of libvirt

## Licensing

The kernel-mode component of KVM is a part of the Linux kernel, itself licensed under GNU General Public License, version 2.
