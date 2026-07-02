---
title: "Single-root input/output virtualization"
source: https://en.wikipedia.org/wiki/Single-root_input/output_virtualization
domain: smartnic
license: CC-BY-SA-4.0
tags: smart network adapter, network offload, programmable nic, io virtualization
fetched: 2026-07-02
---

# Single-root input/output virtualization

In virtualization, **single root input/output virtualization** (**SR-IOV**) is a specification that allows the isolation of PCI Express resources for manageability and performance reasons.

## Details

A single physical PCI Express bus can be shared in a virtual environment using the SR-IOV specification. The SR-IOV offers different virtual functions to different virtual components (e.g. network adapter) on a physical server machine. SR-IOV uses physical and virtual functions to control or configure PCIe devices. Physical functions have the ability to move data in and out of the device while virtual functions are lightweight PCIe functions that support data flowing but also have a restricted set of configuration resources. The virtual or physical functions available to the hypervisor or guest operating system depend on the PCIe device.

The SR-IOV allows different virtual machines (VMs) in a virtual environment to share a single PCI Express hardware interface. In contrast, MR-IOV allows I/O PCI Express to share resources among different VMs on different physical machines.

## InfiniBand

A major field of application for SR-IOV is within high-performance computing (HPC). The use of high-performance InfiniBand networking cards is growing within the HPC sector, and there is early research into the use of SR-IOV to allow for the use of InfiniBand within virtual machines such as Xen.
