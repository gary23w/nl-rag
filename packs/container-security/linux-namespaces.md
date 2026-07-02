---
title: "Linux namespaces"
source: https://en.wikipedia.org/wiki/Linux_namespaces
domain: container-security
license: CC-BY-SA-4.0
tags: container security, docker security, kubernetes security, linux namespaces, hypervisor isolation
fetched: 2026-07-02
---

# Linux namespaces

**Namespaces** are a feature of the Linux kernel that partition kernel resources such that one set of processes sees one set of resources, while another set of processes sees a different set of resources. The feature works by assigning the same namespace type to a set of resources and processes, but allowing those namespaces to refer to distinctly isolated environments. This provides the illusion that a process or a process group is the sole user of the system's hardware and software resources. Examples of such resources include process IDs, hostnames, user IDs, file names, network interfaces, and inter-process communication (IPC) mechanisms.

Linux namespaces, alongside cgroups (control groups), are the foundational technologies underpinning modern OS-level virtualization and Linux containerization platforms such as Docker, Kubernetes, LXC, and Podman. While cgroups dictate *how much* of a system's resources a process can use (such as CPU, memory, and disk I/O limits), namespaces dictate *what* a process is allowed to see and interact with.

The term "namespace" is often used to denote a specific type of namespace (e.g., process ID namespace) as well as a particular space of names. A Linux system begins with a single initial namespace of each type, which is shared by all processes. Processes can subsequently create additional namespaces or join existing ones, allowing complex, nested isolation boundaries.

## History

Linux namespaces were heavily inspired by the wider namespace functionality utilized throughout the Plan 9 from Bell Labs operating system, which treated everything as a file and provided per-process namespace isolation.

The Linux namespace implementation originated in 2002 with the release of the 2.4.19 kernel. The first namespace introduced was the mount namespace, pioneered by kernel developer Al Viro, which isolated filesystem mount points. Because it was the first of its kind, the system call flag introduced for it was simply named `CLONE_NEWNS` (New Namespace), a name that does not specify "mount" and is often considered a historical artifact.

Subsequent namespaces were introduced progressively over several years:

- **UTS and IPC namespaces** were added in kernel version 2.6.19 in 2006.
- **PID namespaces** were finalized in kernel 2.6.24 in 2008.
- **Network namespaces** were largely completed by kernel 2.6.29 in 2009.
- **User namespaces**, primarily developed by Eric W. Biederman, were considered complete and functional in kernel version 3.8, released in 2013. The introduction of user namespaces was a milestone, as it enabled the creation of "unprivileged containers"—containers that can run safely without requiring underlying superuser (root) privileges on the host system.
- **Cgroup namespaces** were introduced in kernel 4.6 in March 2016, spearheaded by Tejun Heo.
- **Time namespaces** were merged in kernel version 5.6 in March 2020, allowing containers to have their own monotonic and boot times.

## Namespace kinds

As of Linux kernel version 5.6, there are exactly eight kinds of namespaces. Namespace functionality operates uniformly across all kinds: each process is associated with a namespace and can only see or use the resources associated with that specific namespace, including its descendant namespaces where applicable. This provides each process (or group of processes) with a unique, compartmentalized view of the system.

### Mount (mnt)

Mount namespaces, the first namespace to be added to Linux, control mount points. They provide a process with an isolated view of the filesystem hierarchy. Upon creation, the mounts from the current mount namespace are initially copied to the new namespace. However, mount points created or unmounted afterwards do not propagate between namespaces by default.

Using the Linux shared subtrees feature, it is possible to configure specific mount points to propagate events (such as a USB drive being mounted) between the host and the container, or vice versa. The clone flag used to create a new namespace of this type is `CLONE_NEWNS`.

### Process ID (pid)

The PID namespace provides processes with an independent set of process IDs (PIDs). PID namespaces are strictly nested. When a new process is created within a new PID namespace, it will have a distinct PID for each namespace from its current namespace up to the initial (root) PID namespace. Hence, processes in the initial PID namespace (like the host operating system) are able to see all processes across all containers, albeit with different PIDs than those seen inside the containers.

The first process created in a PID namespace is assigned process ID number 1. It receives much of the same special treatment as the host system's normal init process. Most notably, any orphaned processes within the namespace are automatically reparented to this PID 1 process. If this PID 1 process terminates, the kernel will immediately terminate all other processes within that PID namespace and any of its descendants by sending them a `SIGKILL` signal.

### Network (net)

Network namespaces virtualize the network stack. Upon creation, a new network namespace contains only a loopback interface (`lo`), which is initially down. Each network interface—whether physical or virtual—can only be present in exactly one network namespace at a time, but interfaces can be actively moved between namespaces by an administrator.

Each network namespace maintains a private set of IP addresses, its own routing table, socket listing, connection tracking table, firewall rules (such as iptables or nftables), and other network-related resources. To grant a container network connectivity, administrators typically create a Virtual Ethernet (`veth`) pair, placing one end in the host namespace and the other inside the container's network namespace, and then bridge the host end to a physical network. Destroying a network namespace automatically destroys any virtual interfaces within it and moves any physical interfaces back to the initial network namespace.

### Inter-process Communication (ipc)

IPC namespaces isolate processes from SysV style inter-process communication mechanisms, as well as POSIX message queues. This prevents processes in different IPC namespaces from interacting with each other using common IPC identifiers. For example, two processes in different namespaces can use the same shared memory segment identifier to allocate memory via the SHM family of functions, and the kernel will guarantee that they are provided with two distinct, fully isolated regions of shared memory.

### UTS

UTS namespaces isolate two system identifiers: the hostname and the NIS domain name. The name "UTS" originates from the data structure passed to the `uname` system call, which historically stands for UNIX Time-Sharing System. When a process creates a new UTS namespace, the hostname and domain name are copied from the caller's namespace. The processes inside the new namespace can then change their hostname without affecting the host machine or other containers.

### User ID (user)

User namespaces are a critical security feature designed to provide both privilege isolation and user identification segregation across multiple sets of processes. Introduced completely in kernel 3.8, they are the backbone of unprivileged containers. Like PID namespaces, user namespaces are nested, with each new namespace considered a child of the one that created it.

A user namespace maintains a mapping table that converts user IDs (UIDs) and group IDs (GIDs) from the container's internal perspective to the host system's global perspective. This allows a process to possess root privileges (UID 0) inside the container, but mathematically map to an unprivileged, restricted user ID (e.g., UID 100000) on the underlying host machine. If a vulnerability allows the container's "root" process to break out of the namespace, the host system will still treat it as the restricted user ID, severely limiting the potential damage.

### Control group (cgroup) Namespace

The cgroup namespace hides the identity of the control group hierarchy to which a process belongs. Before this namespace existed, a process inside a container could inspect `/proc/self/cgroup` and see the entire path of its cgroup relative to the host system (e.g., `/sys/fs/cgroup/memory/docker/container_id`).

By virtualizing the cgroup filesystem view, a process inside a cgroup namespace will see its own cgroup directory as the root (`/`). This prevents information leaks about the host's underlying infrastructure and allows container orchestration tools to seamlessly migrate containers between nodes without conflicting cgroup paths. This namespace type has existed since March 2016 in Linux 4.6.

### Time

The time namespace allows processes to observe different system times. It was introduced in Linux 5.6 in March 2020. Specifically, it isolates two specific kernel clocks: `CLOCK_MONOTONIC` and `CLOCK_BOOTTIME`.

When a container is migrated from one physical host to another or restored from a snapshot, the system uptime and monotonic clock values of the new host will naturally differ from the old one. The time namespace allows the container runtime to set clock offsets, ensuring that applications inside the container do not experience sudden, disruptive jumps in time.

### Proposed namespaces

#### syslog namespace

The syslog namespace was proposed by Rui Xiang, an engineer at Huawei, to isolate kernel logging rings. However, the proposal was not merged into the mainline Linux kernel. Instead, user-space solutions largely fulfilled this requirement; for instance, systemd introduced the concept of "journal namespaces" in February 2020 to provide isolated log environments.

#### IMA namespace

The Integrity Measurement Architecture (IMA) is a kernel security subsystem that measures files before they are accessed to ensure they have not been tampered with. Standard IMA operates globally, which causes conflicts in containerized environments. Ongoing development by the kernel community—with significant contributions from IBM and Huawei—aims to introduce an IMA namespace. This would allow each container to maintain isolated Platform Configuration Registers (PCR), unique Measurement Logs (ML), and independent appraisal keys, thereby bringing hardware-level cryptographic attestation directly to individual containers.

## Administrative hierarchy

To facilitate privilege isolation for administrative actions, every namespace type is tied to a user namespace. When a non-user namespace is created, it is considered "owned" by the user namespace that was active at the moment of its creation.

A user with administrative privileges (specifically, possessing the `CAP_SYS_ADMIN` capability) in the owning user namespace is allowed to perform administrative actions on that namespace. For example, if a process has administrative permissions to change the IP address of a network interface, it may do so, but only if its active user namespace owns that specific network namespace. Because the initial (host) user namespace is the ancestor of all other namespaces, the host's root user inherently retains administrative control over all namespace types across the entire system.

## Implementation details

Namespaces are represented as virtual file objects within the kernel, accessible via the `procfs` pseudo-filesystem.

### Visibility in /proc

The kernel exposes the namespace associations of each running process at the path `/proc/*pid*/ns/*kind*`. Like many non-file resources in `/proc`, these entries manifest as special symbolic links. Reading the link yields a string formatted as `*kind*:[*inode_number*]`.

These inode numbers correspond one-to-one with unique namespace objects in the kernel memory. If two processes show the same inode number for a specific namespace kind (e.g., `net:[4026531969]`), they share that namespace.

As of Linux 6.1.0, the `*kind*` string can be any of `cgroup`, `ipc`, `mnt`, `net`, `pid`, `time`, `user`, or `uts`. Additionally, for namespaces where children processes might inherit different traits than the parent itself (such as PID or user namespaces), the kernel provides `/proc/*pid*/ns/*kind*_for_children` links.

### Syscalls

Four core system calls directly manipulate namespaces:

- `clone`: Used to spawn a new process. By passing specific flags (such as `CLONE_NEWPID` or `CLONE_NEWNET`), the kernel will create the specified new namespaces and place the child process inside them.
- `unshare`: Allows a process to disassociate parts of its execution context from its parent, effectively moving the calling process into a brand new namespace.
- `setns`: Allows a running process to enter an already existing namespace. It requires a file descriptor pointing to one of the namespace symbolic links in `/proc`.
- `ioctl`: Used with specific namespace requests (like `NS_GET_PARENT` or `NS_GET_USERNS`) to discover the hierarchical relationships between different namespaces.

### Destruction

If a namespace is no longer referenced by any part of the system, the kernel will automatically destroy it. The cleanup process for the contained resources varies depending on the namespace kind. A namespace is considered actively *referenced* and kept alive as long as any of the following conditions are met:

- It contains at least one living member process.
- It has at least one referenced child namespace (for nested types like PID and User).
- Its virtual file (`/proc/*pid*/ns/*kind*`) is currently held open via a file descriptor.
- It underpins a bind mount created in the filesystem (a common technique used by networking tools like `iproute2` to keep network namespaces alive without running processes).

## Adoption

Linux namespaces are ubiquitously adopted across the modern software landscape. They are universally combined with cgroups to build container technologies. Examples include Docker, LXC (Linux Containers), Podman, and container orchestration systems like Kubernetes.

Beyond pure containers, namespaces are extensively utilized for process sandboxing and security. Google Chrome and Chromium heavily rely on user, PID, and network namespaces to sandbox web rendering processes, severely limiting the damage an attacker can inflict if a renderer is compromised. Package formats like Flatpak and Snap employ namespaces to isolate desktop applications from the host filesystem and user data.

Furthermore, the init system systemd uses namespaces to secure system services. Directives such as `PrivateNetwork=yes` or `PrivateTmp=yes` in a systemd service file instruct the kernel to spawn the daemon inside isolated network and mount namespaces, respectively.

Command-line utilities also make use of these features. The `util-linux` package includes the `unshare` command, which allows users to start shells or scripts inside newly created namespaces. An example of utilizing namespaces to create an isolated, unprivileged root-like environment:

```mw
unshare --map-root-user --fork --pid --mount-proc --root="${chrootdir}" "$@"
```

This command spawns a process in new user, PID, and mount namespaces, effectively acting as a modern, far more secure equivalent to the traditional `chroot`.
