---
title: "cgroups"
source: https://en.wikipedia.org/wiki/Cgroups
domain: container-security-deep
license: CC-BY-SA-4.0
tags: container security, container image hardening, namespace isolation, cgroups resource limits, kubernetes runtime security
fetched: 2026-07-02
---

# cgroups

**cgroups** (abbreviated from **control groups**) is a Linux kernel feature that limits, accounts for, and isolates the resource usage (CPU, memory, disk I/O, etc.) of a collection of processes.

Engineers at Google started the work on this feature in 2006 under the name "process containers". In late 2007, the nomenclature changed to "control groups" to avoid confusion caused by multiple meanings of the term "container" in the Linux kernel context, and the control groups functionality was merged into the Linux kernel mainline in kernel version 2.6.24, which was released in January 2008. Since then, developers have added controllers for the kernel's own memory allocation, netfilter firewalling, the OOM killer, and many other parts.

A major change in the history of cgroups is **cgroup v2**, which removes the ability to use multiple process hierarchies and to discriminate between threads as found in the original cgroup (now called "v1"). Work on the single, unified hierarchy started with the repurposing of v1's dummy hierarchy as a place for holding all controllers not yet used by others in 2014. cgroup v2 was merged in Linux kernel 4.5 (2016).

## Versions

There are two versions of cgroups. They can co-exist in a system.

- The original version of cgroups was written by Paul Menage and Rohit Seth. It was merged into the mainline Linux kernel in 2007 (2.6.2). Development and maintenance of cgroups was then taken over by Tejun Heo, who instituted major redesigns without breaking the interface (see § Redesigns of v1). It was renamed "Control Group version 1" (cgroup-v1) after cgroups-v2 appeared in Linux 4.5.
- Tejun Heo found that further redesign of v1 could not proceed without breaking the interface. As a result, he added a separate, new system called "Control Group version 2" (cgroup-v2). Unlike v1, cgroup v2 has only a single process hierarchy (because a controller can only be assigned to one hierarchy, processes in separate hierarchies cannot be managed by the same controller; this change sidesteps the issue). It also removes the ability to discriminate between threads, choosing to work on a granularity of processes instead (disabling an "abuse" of the system which led to convoluted APIs). Linux kernel 4.5 released on 14 March 2016 is the first version that supports cgroup v2.

## Features

One of the design goals of cgroups is to provide a unified interface to many different use cases, from controlling single processes (by using nice, for example) to full operating system-level virtualization (as provided by OpenVZ, Linux-VServer or LXC, for example). Cgroups provides:

**Resource limiting**

groups can be set not to exceed a configured

memory

limit, which also includes the

file system cache

,

I/O bandwidth limit,

CPU quota limit,

CPU set limit,

or

maximum open files

.

**Prioritization**

some groups may get a larger share of CPU utilization

or disk I/O throughput

**Accounting**

measures a group's resource usage, which may be used, for example, for billing purposes

**Control**

freezing groups of processes, their

checkpointing

and restarting

## Use

A control group (abbreviated as cgroup) is a collection of processes that are bound by the same criteria and associated with a set of parameters or limits. These groups can be hierarchical, meaning that each group inherits limits from its parent group. The kernel provides access to multiple controllers (also called subsystems) through the cgroup interface; for example, the "memory" controller limits memory use, "cpuacct" accounts CPU usage, etc.

Control groups can be used in multiple ways:

- By accessing the cgroup virtual file system manually.
- By creating and managing groups on the fly using tools like `cgcreate`, `cgexec`, and `cgclassify` (from `libcgroup`).
- Through the "rules engine daemon" that can automatically move processes of certain users, groups, or commands to cgroups as specified in its configuration.
- Indirectly through other software that uses cgroups, such as Docker, Firejail, LXC, libvirt, systemd, Open Grid Scheduler/Grid Engine, and Google's developmentally defunct lmctfy.

The Linux kernel documentation contains some technical details of the setup and use of control groups version 1 and version 2.

### Interfaces

Both versions of cgroup act through a pseudo-filesystem (`cgroup` for v1 and `cgroup2` for v2). Like all filesystems they can be mounted on any path, but the general convention is to mount one of the versions (generally v2) on `/sys/fs/cgroup` under the sysfs default location of `/sys`. As mentioned before the two cgroup versions can be active at the same time; this too applies to the filesystems so long as they are mounted to a different path. For the description below we assume a setup where the v2 hierarchy lies in `/sys/fs/cgroup`. The v1 hierarchy, if ever required, will be mounted at a different location.

At initialization cgroup2 should have no defined control groups except the top-level one. In other words, `/sys/fs/cgroup` should have no directories, only a number of files that control the system as a whole. At this point, running `ls /sys/fs/cgroup` could list the following on one example system:

- `cgroup.controllers`
- `cgroup.max.depth`
- `cgroup.max.descendants`
- `cgroup.pressure`
- `cgroup.procs`
- `cgroup.stat`
- `cgroup.subtree_control`
- `cgroup.threads`
- `cpu.pressure`
- `cpuset.cpus.effective`
- `cpuset.cpus.isolated`
- `cpuset.mems.effective`
- `cpu.stat`
- `cpu.stat.local`
- `io.cost.model`
- `io.cost.qos`
- `io.pressure`
- `io.prio.class`
- `io.stat`
- `irq.pressure`
- `memory.numa_stat`
- `memory.pressure`
- `memory.reclaim`
- `memory.stat`
- `memory.zswap.writeback`
- `misc.capacity`
- `misc.current`
- `misc.peak`

These files are named according to the controllers that handle them. For example, `cgroup.*` deal with the cgroup system itself and `memory.*` deal with the memory subsystem. Example: to request the kernel to 1 gigabyte of memory from anywhere in the system, one can run `echo "1G swappiness=50" > /sys/fs/cgroup/memory.reclaim`.

To create a subgroup, one simply creates a new directory under an existing group (including the top-level one). The files corresponding to available controls for this group are automatically created. For example, running `mkdir /sys/fs/cgroup/example; ls /sys/fs/cgroup/example` would produce a list of files largely similar to the one above, but with noticeable changes. On one example system, these files are added:

- `cgroup.events`
- `cgroup.freeze`
- `cgroup.kill`
- `cgroup.type`
- `cpu.idle`
- `cpu.max`
- `cpu.max.burst`
- `cpu.pressure`
- `cpu.uclamp.max`
- `cpu.uclamp.min`
- `cpu.weight`
- `cpu.weight.nice`
- `memory.current`
- `memory.events`
- `memory.events.local`
- `memory.high`
- `memory.low`
- `memory.max`
- `memory.min`
- `memory.oom.group`
- `memory.peak`
- `memory.swap.current`
- `memory.swap.events`
- `memory.swap.high`
- `memory.swap.max`
- `memory.swap.peak`
- `memory.zswap.current`
- `memory.zswap.max`
- `pids.current`
- `pids.events`
- `pids.events.local`
- `pids.max`
- `pids.peak`

These changes are not unexpected because some controls and statistics only make sense on a subset of processes (e.g. nice level being the CPU priority of processes relative to the rest of the system).

Processes are assigned to subgroups by writing to `/proc/<PID>/cgroup`. The cgroup a process is in can be found by reading the same file.

On systems based on systemd, a hierarchy of subgroups is predefined to encapsulate every process directly and indirectly launched by systemd under a subgroup: the very basis of how systemd manages processes. An explanation of the nomenclature of these groups can be found in the Red Hat Enterprise Linux 7 manual. Red Hat also provides a guide on creating a systemd service file that causes a process to run in a separate cgroup.

`systemd-cgtop` command can be used to show top control groups by their resource usage.

#### V1 coexistence

On a system with v2, v1 can still be mounted and given access to controllers *not* in use by v2. However, a modern system typically already places all controllers in use in v2, so there is no controller available for v1 at all even if a hierarchy is created. It is possible to clear all uses of a controller from v2 and hand it to v1, but moving controllers between hierarchies after the system is up and running is cumbersome and not recommended.

## Major evolutions

### Redesigns of v1

Redesign of cgroups started in 2013, with additional changes brought by versions 3.15 and 3.16 of the Linux kernel.

The following changes concern the kernel before 4.5/4.6, i.e. when cgroups-v2 were added. In other words they describe how cgroups-v1 had been changed, though most of them have also been inherited into v2 (after all, v1 and v2 share the same codebase).

#### Namespace isolation

While not technically part of the cgroups work, a related feature of the Linux kernel is *namespace isolation*, where groups of processes are separated such that they cannot "see" resources in other groups. For example, a PID namespace provides a separate enumeration of process identifiers within each namespace. Also available are mount, user, UTS (Unix Time Sharing), network and SysV IPC namespaces.

- The *PID namespace* provides isolation for the allocation of process identifiers (PIDs), lists of processes and their details. While the new namespace is isolated from other siblings, processes in its "parent" namespace still see all processes in child namespaces—albeit with different PID numbers.
- *Network namespace* isolates the network interface controllers (physical or virtual), iptables firewall rules, routing tables etc. Network namespaces can be connected with each other using the "veth" virtual Ethernet device.
- *"UTS" namespace* allows changing the hostname.
- *Mount namespace* allows creating a different file system layout, or making certain mount points read-only.
- *IPC namespace* isolates the System V inter-process communication between namespaces.
- *User namespace* isolates the user IDs between namespaces.
- *Cgroup namespace*

Namespaces are created with the "unshare" command or syscall, or as "new" flags in a "clone" syscall.

The "ns" subsystem was added early in cgroups development to integrate namespaces and control groups. If the "ns" cgroup was mounted, each namespace would also create a new group in the cgroup hierarchy. This was an experiment that was later judged to be a poor fit for the cgroups API, and removed from the kernel.

Linux namespaces were inspired by the more general namespace functionality used heavily throughout Plan 9 from Bell Labs.

#### Conversion to kernfs

Kernfs was introduced into the Linux kernel with version 3.14 in March 2014, the main author being Tejun Heo. One of the main motivators for a separate kernfs is the cgroups file system. Kernfs is basically created by splitting off some of the sysfs logic into an independent entity, thus easing for other kernel subsystems the implementation of their own virtual file system with handling for device connect and disconnect, dynamic creation and removal, and other attributes. This does not affect how cgroups is used, but makes maintaining the code easier.

#### New features introduced during v1

*Kernel memory control groups* (*kmemcg*) were merged into version 3.8 (2013 February 18 (18-02-2013)) of the Linux kernel mainline. The kmemcg controller can limit the amount of memory that the kernel can utilize to manage its own internal processes.

Support for per-group netfilter setup was added in 2014.

The unified hierarchy was added in 2014. It repurposes of v1's dummy hierarchy to hold all controllers not yet used by others. This changed dummy hierarchy would become the only available hierarchy in v2.

### Changes after v2

Unlike v1, cgroup v2 has only a single process hierarchy and discriminates between processes, not threads.

#### cgroup awareness of OOM killer

Linux Kernel 4.19 (October 2018) introduced cgroup awareness of OOM killer implementation which adds an ability to kill a cgroup as a single unit and so guarantee the integrity of the workload.

## Adoption

Various projects use cgroups as their basis, including CoreOS, Docker (in 2013), Hadoop, Jelastic, Kubernetes, lmctfy (Let Me Contain That For You), LXC (Linux Containers), systemd, Mesos and Mesosphere, HTCondor, and Flatpak.

Major Linux distributions also adopted it such as Red Hat Enterprise Linux (RHEL) 6.0 in November 2010, three years before adoption by the mainline Linux kernel.

On 29 October 2019, the Fedora Project modified Fedora 31 to use CgroupsV2 by default.
