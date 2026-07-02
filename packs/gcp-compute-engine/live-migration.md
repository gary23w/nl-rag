---
title: "Live migration"
source: https://en.wikipedia.org/wiki/Live_migration
domain: gcp-compute-engine
license: CC-BY-SA-4.0
tags: gcp compute engine, google compute engine, cloud virtual machine, gcp vm
fetched: 2026-07-02
---

# Live migration

**Live migration**, also called **migration**, refers to the process of moving a running virtual machine (VM) between different physical machines in a manner that the VM and applications running within the VM are mostly unaffected. Memory, storage, and network connectivity of the virtual machine are transferred from the original host machine to the destination. The time between stopping the VM or application on the source and resuming it on destination is called "downtime" or "blackout".

## Live migration basics

Live migration requires the entire VM's state to be transferred from the source host to the target host. This state includes the state of any components of the VM, for example, the register contents of the virtual CPUs (vCPUs). The state of the VM is not stable until the VM is paused. For example, until the vCPUs have been paused, the state in the virtual registers may be changing.

The simplest way to implement live migration is to pause the VM, serialize and send the state to the target host, and resume the VM on the target host. Serializing and sending certain state, like the state of the VM's main memory or locally-attached storage devices, can be slow.

## Memory live migration

If the entire contents of the VM's main memory must be copied while the VM is paused, the VM will have to remain paused for an extended period of time, depending on the size of the VM's main memory. There are several techniques for reducing blackout for large-memory VMs.

### Pre-copy memory migration

Pre-copy memory migration requires the hypervisor to track which pages the guest is writing to. With this ability, the following strategy is possible:

1. Copy all of the VM's main memory pages to the target host.
2. Before copying any particular page, track any subsequent writes to the page (e.g. by write-protecting the corresponding SLAT entry).
3. After all pages have been copied, start a new copying pass, but only copy pages that were written to since it was last copied to the target host (i.e., pages that are "dirty").
4. Repeat step 3 until the set of remaining dirty pages is small.
5. Pause the VM, and transfer the remaining dirty pages to the target host.

This is the basic pre-copy strategy. Other optimizations can be applied, like not re-sending pages that will likely be dirtied again quickly.

The guest is usually able to write to memory faster than it can be copied to the target, which means that pre-copy might never converge to a small dirty set. If the hypervisor does not throttle writes to guest memory, blackout time may remain large, even with pre-copy memory migration.

### Post-copy memory migration

Post-copy memory migration is a strategy for transferring a VM's main memory outside of blackout. It can complement pre-copy by reducing pause time when pre-copy does not converge on a small set of dirty pages.

It requires the hypervisor to intercept guest memory accesses, allowing the VM to resume on the target host without a complete memory copy. Accesses to pages not yet present on the target (e.g., pages dirtied during pre-copy) are fetched on demand by the hypervisor.

To ensure that all dirty pages are eventually transferred, a hypervisor implementing post-copy live migration will also fetch outstanding dirty pages in the background, concurrently with on-demand fetching of dirty pages.

Post-copy transfers each page only once, whereas pre-copy may resend pages multiple times if they are repeatedly modified. However, pre-copy maintains a consistent VM state on the source, while post-copy splits state between source and destination. As a result, failures during post-copy cannot be recovered, unlike pre-copy, which can be restarted.

## VM managers with live migration support

- Virtuozzo
- Xen since version 2.0, 2004 for PV guests; since version 3.1, May 18, 2007 for HVM guests
- OpenVZ
- Parallels Cloud Server
- Workload Partitions
- Integrity Virtual Machines
- KVM since February 2007, with different techniques.
- Oracle VM Server for x86
- Oracle VM Server for SPARC
- OVirt
- Red Hat Virtualisation
- POWER Hypervisor (PHYP)
- VMware ESXi
- IBM Live Partition Mobility, since 2007
- Hyper-V Server 2008 R2
- VirtualBox
- Proxmox Virtual Environment

## Cloud Platforms with live migration support

- Microsoft Azure
- Jelastic
- Google Cloud Platform
- CloudEndure
- Oracle Cloud Infrastructure

## Systems providing software live migration

- OpenSSI
- MOSIX
- Single-system image
