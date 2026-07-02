---
title: "Linux kernel (part 2/2)"
source: https://en.wikipedia.org/wiki/Linux_kernel
domain: linux-capabilities
license: CC-BY-SA-4.0
tags: linux capability model, privilege decomposition capabilities, capability bounding set, least privilege capability drop
fetched: 2026-07-02
part: 2/2
---

## Architecture and features

Even though seemingly contradictory, the Linux kernel is both monolithic and modular. The kernel is classified as a monolithic kernel architecturally since the entire OS runs in kernel space. The design is modular since it can be assembled from modules that in some cases are loaded and unloaded at runtime. It supports features once only available in closed source kernels of non-free operating systems.

The rest of the article makes use of the UNIX and Unix-like operating systems convention of the manual pages. The number that follows the name of a command, interface, or other feature specifies the section (i.e. the type of the OS' component or feature) it belongs to. For example execve(2) refers to a system call, and exec(3) refers to a userspace library wrapper.

The following is an overview of architectural design and of noteworthy features.

- Concurrent computing and (with the availability of enough CPU cores for tasks that are ready to run) even true parallel execution of many processes at once (each of them having one or more threads of execution) on SMP and NUMA architectures.
- Selection and configuration of hundreds of kernel features and drivers (using one of the make *config family of commands before building), modification of kernel parameters before boot (usually by inserting instructions into the lines of a bootloader menu or configuration file), and fine tuning of kernel behavior at run-time (using the sysctl(8) interface to /proc/sys/).
- Configuration (again using the make *config commands) and run-time modifications of the policies (via nice(2), setpriority(2), and the family of sched_*(2) syscalls) of the task schedulers that allow preemptive multitasking (both in user mode and, since the 2.6 series, in kernel mode); the earliest eligible virtual deadline first scheduling (EEVDF) scheduler, is the default scheduler of Linux since 2023 and it uses a red-black tree that can search, insert and delete process information (task struct) with O(log n) time complexity, where *n* is the number of runnable tasks.
- Advanced memory management with paged virtual memory and a multi-generational least recently used (MGLRU) page replacement algorithm.
- Inter-process communications and synchronization mechanism.
- A virtual filesystem on top of several concrete filesystems (ext4, Btrfs, XFS, JFS, FAT32, and many more).
- Configurable I/O schedulers, ioctl(2) syscall that manipulates the underlying device parameters of special files (it is a non standard system call, since arguments, returns, and semantics depends on the device driver in question), support for POSIX asynchronous I/O (because they scale poorly with multithreaded applications, however, a family of Linux specific I/O system calls (io_*(2)) had to be created for the management of asynchronous I/O contexts suitable for concurrent processing).
- OS-level virtualization (with Linux-VServer), paravirtualization and hardware-assisted virtualization (with KVM or Xen, and using QEMU for hardware emulation); On the Xen hypervisor, the Linux kernel provides support to build Linux distributions (such as openSUSE Leap and many others) that work as *Dom0*, that are virtual machine host servers that provide the management environment for the user's virtual machines (*DomU*).
- I/O Virtualization with VFIO and SR-IOV. Virtual Function I/O (VFIO) exposes direct device access to user space in a secure memory (IOMMU) protected environment. With VFIO, a VM Guest can directly access hardware devices on the VM Host Server. This technique improves performance, if compared both to Full virtualization and Paravirtualization. With VFIO, however, devices cannot be shared with multiple VM guests. Single Root I/O Virtualization (SR-IOV) combines the performance gains of VFIO and the ability to share a device with several VM Guests (but it requires special hardware that must be capable to appear to two or more VM guests as different devices).
- Security mechanisms for discretionary and mandatory access control (SELinux, AppArmor, POSIX ACLs, and others).
- Several types of layered communication protocols (including the Internet protocol suite).
- Asymmetric multiprocessing via the RPMsg subsystem.

Most device drivers and kernel extensions run in kernel space (ring 0 in many CPU architectures), with full access to the hardware. Some exceptions run in user space; notable examples are filesystems based on FUSE/CUSE, and parts of UIO. Furthermore, the X Window System and Wayland, the windowing system and display server protocols that most people use with Linux, do not run within the kernel. Differently, the actual interfacing with GPUs of graphics cards is an in-kernel subsystem called Direct Rendering Manager (DRM).

Unlike standard monolithic kernels, device drivers are easily configured as modules, and loaded or unloaded while the system is running and can also be pre-empted under certain conditions in order to handle hardware interrupts correctly and to better support symmetric multiprocessing. By choice, Linux has no stable device driver application binary interface.

Linux typically makes use of memory protection and virtual memory and can also handle non-uniform memory access, the project has absorbed μClinux, which also makes it possible to run Linux on microcontrollers without virtual memory.

The hardware is represented in the file hierarchy. User applications interact with device drivers via entries in the /dev or /sys directories. Process information is mapped into the /proc directory.

| User mode | **User applications** | *bash, LibreOffice, GIMP, Blender, 0 A.D., Mozilla Firefox, ...* |   |   |   |
|---|---|---|---|---|---|
| **System components** | **init daemon**: *OpenRC, runit, systemd, ...* | **System daemons**: *polkitd, smbd, sshd, udevd, ...* | **Windowing system**: *X11, Wayland, SurfaceFlinger (Android)* | **Graphics**: *Mesa*, *AMD Software, ...* | **Other libraries:** *GTK, Qt, EFL, SDL, SFML, FLTK, GNUstep, ...* |
| **C standard library** | `fopen`, `execv`, `malloc`, `memcpy`, `localtime`, `pthread_create`, ... (up to 2000 subroutines) *glibc* aims to be fast, *musl* aims to be lightweight, *uClibc* targets embedded systems, *bionic* was written for Android, etc. All aim to be POSIX/SUS-compatible. |   |   |   |   |
| Kernel mode | **Linux kernel** | `stat`, `splice`, `dup`, `read`, `open`, `ioctl`, `write`, `mmap`, `close`, `exit`, etc. (about 380 system calls) The Linux kernel System Call Interface (SCI), aims to be POSIX/SUS-compatible |   |   |   |
| Process scheduling subsystem | IPC subsystem | Memory management subsystem | Virtual files subsystem | Networking subsystem |   |
| Other components: ALSA, DRI, evdev, klibc, LVM, device mapper, Linux Network Scheduler, Netfilter Linux Security Modules: *SELinux*, *TOMOYO*, *AppArmor*, *Smack* |   |   |   |   |   |
| Hardware (CPU, main memory, data storage devices, etc.) |   |   |   |   |   |

### Interfaces

Linux started as a clone of UNIX, and aims toward POSIX and Single UNIX Specification compliance. The kernel provides system calls and other interfaces that are Linux-specific. In order to be included in the official kernel, the code must comply with a set of licensing rules.

The Linux application binary interface (ABI) between the kernel and the user space has four degrees of stability (stable, testing, obsolete, removed); The system calls are expected to never change in order to preserve compatibility for userspace programs that rely on them.

Loadable kernel modules (LKMs), by design, cannot rely on a stable ABI. Therefore, they must always be recompiled whenever a new kernel executable is installed in a system, otherwise they will not be loaded. In-tree drivers that are configured to become an integral part of the kernel executable (vmlinux) are statically linked by the build process.

There is no guarantee of stability of source-level in-kernel API and, because of this, device driver code, as well as the code of any other kernel subsystem, must be kept updated with kernel evolution. Any developer who makes an API change is required to fix any code that breaks as the result of their change.

#### Kernel-to-userspace API

The set of the Linux kernel API that regards the interfaces exposed to user applications is fundamentally composed of UNIX and Linux-specific system calls. A system call is an entry point into the Linux kernel. For example, among the Linux-specific ones there is the family of the clone(2) system calls. Most extensions must be enabled by defining the `_GNU_SOURCE` macro in a header file or when the user-land code is being compiled.

System calls can only be invoked via assembly instructions that enable the transition from unprivileged user space to privileged kernel space in ring 0. For this reason, the C standard library (libC) acts as a wrapper to most Linux system calls, by exposing C functions that, if needed, transparently enter the kernel, which will execute on behalf of the calling process. For system calls not exposed by libC, such as the fast userspace mutex, the library provides a function called syscall(2), which can be used to explicitly invoke them.

Pseudo filesystems (e.g., the sysfs and procfs filesystems) and special files (e.g., `/dev/random`, `/dev/sda`, `/dev/tty`, and many others) constitute another layer of interface to kernel data structures representing hardware or logical (software) devices.

#### Kernel-to-userspace ABI

Because of the differences existing between the hundreds of various implementations of the Linux OS, executable objects, even though they are compiled, assembled, and linked for running on a specific hardware architecture (that is, they use the ISA of the target hardware), often cannot run on different Linux distributions. This issue is mainly due to distribution-specific configurations and a set of patches applied to the code of the Linux kernel, differences in system libraries, services (daemons), filesystem hierarchies, and environment variables.

The main standard concerning application and binary compatibility of Linux distributions is the Linux Standard Base (LSB). The LSB goes beyond what concerns the Linux kernel, because it also defines the desktop specifications, the X libraries and Qt that have little to do with it. The LSB version 5 is built upon several standards and drafts (POSIX, SUS, X/Open, File System Hierarchy (FHS), and others).

The parts of the LSB more relevant to the kernel are the *General ABI* (gABI), especially the System V ABI and the Executable and Linking Format (ELF), and the *Processor Specific ABI* (psABI), for example the *Core Specification for X86-64.*

The standard ABI for how x86_64 user programs invoke system calls is to load the syscall number into the *rax* register, and the other parameters into *rdi*, *rsi*, *rdx*, *r10*, *r8*, and *r9*, and finally to put the *syscall* assembly instruction in the code.

#### In-kernel API

There are several internal kernel APIs between kernel subsystems. Some are available only within the kernel subsystems, while a somewhat limited set of in-kernel symbols (i.e., variables, data structures, and functions) is exposed to dynamically loadable modules (e.g., device drivers loaded on demand) whether they're exported with the EXPORT_SYMBOL() and EXPORT_SYMBOL_GPL() macros (the latter reserved to modules released under a GPL-compatible license).

Linux provides in-kernel APIs that manipulate data structures (e.g., linked lists, radix trees, red-black trees, queues) or perform common routines (e.g., copy data from and to user space, allocate memory, print lines to the system log, and so on) that have remained stable at least since Linux version 2.6.

In-kernel APIs include libraries of low-level common services used by device drivers:

- SCSI Interfaces and libATA – respectively, a peer-to-peer packet based communication protocol for storage devices attached to USB, SATA, SAS, Fibre Channel, FireWire, ATAPI device, and an in-kernel library to support [S]ATA host controllers and devices.
- Direct Rendering Manager (DRM) and Kernel Mode Setting (KMS) – for interfacing with GPUs and supporting the needs of modern 3D-accelerated video hardware, and for setting screen resolution, color depth and refresh rate
- DMA buffers (DMA-BUF) – for sharing buffers for hardware direct memory access across multiple device drivers and subsystems
- Video4Linux – for video capture hardware
- Advanced Linux Sound Architecture (ALSA) – for sound cards
- New API – for network interface controllers
- mac80211 and cfg80211 – for wireless network interface controllers

#### In-kernel ABI

The Linux developers chose not to maintain a stable in-kernel ABI. Modules compiled for a specific version of the kernel cannot be loaded into another version without being recompiled.

### Process management

Linux, as other kernels, has the ability to manage processes including creating, suspending, resuming and terminating. Unlike other operating systems, the Linux kernel implements processes as a group of threads called tasks. If two tasks share the same TGID, then they are called in the kernel terminology a task group. Each task is represented by a *task_struct* data structure. When a process is created it is assigned a globally unique identifier called *PID* and cannot be shared

A new process can be created by calling clone family of system calls or fork system call. Processes can be suspended and resumed by the kernel by sending signals like SIGSTOP and SIGCONT. A process can terminate itself by calling exit system call, or terminated by another process by sending signals like SIGKILL, SIGABRT or SIGINT.

If the executable is dynamically linked to shared libraries, a dynamic linker is used to find and load the needed objects, prepare the program to run and then run it.

The Native POSIX Thread Library (NPTL) provides the POSIX standard thread interface (*pthreads*) to userspace. The kernel isn't aware of processes nor threads but it is aware of *tasks*, thus threads are implemented in userspace. Threads in Linux are implemented as *tasks* sharing resources, while if they aren't sharing called to be independent processes.

The kernel provides the futex(7) (fast user-space mutex) mechanisms for user-space locking and synchronization. The majority of the operations are performed in userspace but it may be necessary to communicate with the kernel using the futex(2) system call.

As opposed to userspace threads described above, *kernel threads* run in kernel space. They are threads created by the kernel itself for specialized tasks; they are privileged like the kernel and aren't bound to any process or application.

### Scheduling

The Linux process scheduler is modular, in the sense that it enables different scheduling classes and policies. Scheduler classes are pluggable scheduler algorithms that can be registered with the base scheduler code. Each class schedules different types of processes. The core code of the scheduler iterates over each class in order of priority and chooses the highest priority scheduler that has a schedulable entity of type struct sched_entity ready to run. Entities may be threads, group of threads, and even all the processes of a specific user.

Linux provides both user preemption as well as (selectable, up to) full kernel preemption. Preemption reduces latency, increases responsiveness, and makes Linux more suitable for desktop and real-time applications. This comes at a cost of throughput, as work being interrupted worsens cache behavior.

For normal tasks, by default, the kernel uses the Completely Fair Scheduler (CFS) class, introduced in version 2.6.23. The scheduler is defined as a macro in a C header as `SCHED_NORMAL`. In other POSIX kernels, a similar policy known as `SCHED_OTHER` allocates CPU timeslices (i.e, it assigns absolute slices of the processor time depending on either predetermined or dynamically computed priority of each process). The Linux CFS does away with absolute timeslices and assigns a fair proportion of CPU time, as a function of parameters like the total number of runnable processes and the time they have already run; this function also takes into account a kind of weight that depends on their relative priorities (nice values).

With user preemption, the kernel scheduler can replace the current process with the execution of a context switch to a different one that therefore acquires the computing resources for running (CPU, memory, and more). It makes it according to the CFS algorithm (in particular, it uses a variable called vruntime for sorting entities and then chooses the one that has the smaller vruntime, - i.e., the schedulable entity that has had the least share of CPU time), to the active scheduler policy and to the relative priorities. With kernel preemption, the kernel can preempt itself when an interrupt handler returns, when kernel tasks block, and whenever a subsystem explicitly calls the schedule() function.

The kernel also contains two POSIX-compliant real-time scheduling classes named `SCHED_FIFO` (realtime first-in-first-out) and `SCHED_RR` (realtime round-robin), both of which take precedence over the default class. An additional scheduling policy known as `SCHED_DEADLINE`, implementing the earliest deadline first algorithm (EDF), was added in kernel version 3.14, released on 30 March 2014. `SCHED_DEADLINE` takes precedence over all the other scheduling classes.

Real-time `PREEMPT_RT` patches, included into the mainline Linux since version 2.6, provide a deterministic scheduler, the removal of preemption and interrupt disabling (where possible), PI Mutexes (i.e., locking primitives that avoid priority inversion), support for High Precision Event Timers (HPET), preemptive read-copy-update (RCU), (forced) IRQ threads, and other minor features.

In 2023, Peter Zijlstra proposed replacing CFS with an earliest eligible virtual deadline first scheduling (EEVDF) scheduler, to prevent the need for CFS "latency nice" patches. The EEVDF scheduler replaced CFS in version 6.6 of the Linux kernel.

### Synchronization

The kernel has different causes of concurrency (e.g., interrupts, bottom halves, preemption of kernel and users tasks, symmetrical multiprocessing).

For protecting critical regions (sections of code that must be executed atomically), shared memory locations (like global variables and other data structures with global scope), and regions of memory that are asynchronously modifiable by hardware (e.g., having the C volatile type qualifier), Linux provides a large set of tools. They consist of atomic types (which can only be manipulated by a set of specific operators), spinlocks, semaphores, mutexes, and lockless algorithms (e.g., RCUs). Most lock-less algorithms are built on top of memory barriers for the purpose of enforcing memory ordering and prevent undesired side effects due to compiler optimization.

PREEMPT_RT code included in mainline Linux provide *RT-mutexes*, a special kind of Mutex that do not disable preemption and have support for priority inheritance. Almost all locks are changed into sleeping locks when using configuration for realtime operation. Priority inheritance avoids priority inversion by granting a low-priority task that holds a contended lock the priority of a higher-priority waiter until that lock is released.

Linux includes a kernel lock validator called *Lockdep*.

### Interrupts

Although the management of interrupts could be seen as a single job, it is divided into two. This split in two is due to the different time constraints and to the synchronization needs of the tasks whose the management is composed of. The first part is made up of an asynchronous interrupt service routine (ISR) that in Linux is known as the *top half*, while the second part is carried out by one of three types of the so-called *bottom halves* (*softirq*, *tasklets,* and *work queues*).

Linux interrupt service routines can be nested. A new IRQ can trap into a high priority ISR that preempts any other lower priority ISR.

### Memory

The Linux kernel manages both physical and virtual memory. It divides physical memory into zones, each of which has a specific purpose.

- ZONE_DMA: this zone is suitable for DMA.
- ZONE_NORMAL: for normal memory operations.
- ZONE_HIGHMEM: part of physical memory that is only accessible to the kernel using temporary mapping.

Those zones are the most common, but others exist.

Linux implements virtual memory with 4 or 5-level page tables. The kernel is not pageable (meaning it is always resident in physical memory and cannot be swapped to the disk) and there is no memory protection (no SIGSEGV signals, unlike in user space), therefore memory violations lead to instability and system crashes. User memory is pageable by default, although paging for specific memory areas can be disabled with the `mlock()` system call family.

Page frame information is maintained in apposite data structures (of type `struct page`) that are populated immediately after boot and kept until shutdown, regardless of whether they are associated with virtual pages. The physical address space is divided into different zones, according to architectural constraints and intended use. NUMA systems with multiple memory banks are also supported.

Small chunks of memory can be dynamically allocated in kernel space via the family of `kmalloc()` APIs and freed with the appropriate variant of `kfree()`. `vmalloc()` and `kvfree()` are used for large virtually contiguous chunks. `alloc_pages()` allocates the desired number of entire pages.

The kernel used to include the SLAB, SLUB and SLOB allocators as configurable alternatives. The SLOB allocator was removed in Linux 6.4 and the SLAB allocator was removed in Linux 6.8. The sole remaining allocator is SLUB, which aims for simplicity and efficiency, is PREEMPT_RT compatible and was introduced in Linux 2.6.

### Virtual filesystem

Since Linux supports numerous filesystems with different features and functionality, it is necessary to implement a generic filesystem that is independent from underlying filesystems. The virtual file system interfaces with other Linux subsystems, userspace, or APIs and abstracts away the different implementations of underlying filesystems. VFS implements system calls like `create`, `open`, `read`, `write` and `close`. VFS implements a generic superblock and inode block that is independent from the one that the underlying filesystem has.

In this subsystem directories and files are represented by a `struct file` data structure. When userspace requests access to a file it is returned a file descriptor (non negative integer value) but in kernel space it is a `struct file` structure. This structure stores all the information the kernel knows about a file or directory.

sysfs and procfs are virtual filesystems that expose hardware information and userspace programs' runtime information. These filesystems aren't present on disk and instead the kernel implements them as a callback or routine that gets called when they are accessed by userspace.

### Supported architectures

While not originally designed to be portable, Linux is now one of the most widely ported operating system kernels, running on a diverse range of systems from the ARM architecture to IBM z/Architecture mainframe computers. The first port was performed on the Motorola 68000 platform. The modifications to the kernel were so fundamental that Torvalds viewed the Motorola version as a fork and a "Linux-like operating system". That moved Torvalds to lead a major restructure of the code to facilitate porting to more computing architectures. The first Linux that, in a single source tree, had code for more than i386 alone, supported the DEC Alpha AXP 64-bit platform.

Linux is used as the primary operating system on IBM’s Summit supercomputer. In October 2019, all systems on the TOP500 list of the world’s fastest supercomputers ran operating systems based on the Linux kernel, whereas the first Linux-based supercomputer appeared on the list in 1998.

Linux has also been ported to various handheld devices such as iPhone 3G and iPod.

### Supported devices

In 2007, the LKDDb project has been started to build a comprehensive database of hardware and protocols known by Linux kernels. The database is built automatically by static analysis of the kernel sources. Later in 2014, the Linux Hardware project was launched to automatically collect a database of all tested hardware configurations with the help of users of various Linux distributions.

### Live patching

Kernel updates can be applied without rebooting by using live patching technologies such as Ksplice, kpatch and kGraft. Initial support for live kernel patching was merged into the Linux kernel mainline in version 4.0, released on 12 April 2015. The feature, known as *livepatch*, uses the kernel's ftrace functionality and provides a common infrastructure for hot patches supplied through kernel modules, together with interfaces for userspace management tools. In its initial Linux 4.0 implementation, livepatch support was limited to the x86 architecture and provided basic infrastructure rather than a complete live-patching consistency model.

### Security

Kernel bugs present potential security issues. For example, they may allow for privilege escalation or create denial-of-service attack vectors. Over the years, numerous bugs affecting system security were found and fixed. New features are frequently implemented to improve the kernel's security.

Capabilities(7) have already been introduced in the section about the processes and threads. Android makes use of them and systemd gives administrators detailed control over the capabilities of processes.

Linux offers a wealth of mechanisms to reduce kernel attack surface and improve security that are collectively known as the Linux Security Modules (LSM). They comprise the Security-Enhanced Linux (SELinux) module, whose code has been originally developed and then released to the public by the NSA, and AppArmor among others. SELinux is now actively developed and maintained on GitHub. SELinux and AppArmor provide support to access control security policies, including mandatory access control (MAC), though they profoundly differ in complexity and scope.

Another security feature is the Seccomp BPF (SECure COMPuting with Berkeley Packet Filters), which works by filtering parameters and reducing the set of system calls available to user-land applications.

Critics have accused kernel developers of covering up security flaws, or at least not announcing them; in 2008, Torvalds responded to this with the following:

> I personally consider security bugs to be just "normal bugs". I don't cover them up, but I also don't have any reason what-so-ever to think it's a good idea to track them and announce them as something special...one reason I refuse to bother with the whole security circus is that I think it glorifies—and thus encourages—the wrong behavior. It makes "heroes" out of security people, as if the people who don't just fix normal bugs aren't as important. In fact, all the boring normal bugs are *way* more important, just because there's[sic] a lot more of them. I don't think some spectacular security hole should be glorified or cared about as being any more "special" than a random spectacular crash due to bad locking.

Linux distributions typically release security updates to fix vulnerabilities in the Linux kernel. Many offer long-term support releases that receive security updates for a certain Linux kernel version for an extended period of time.

In 2024, researchers disclosed that the Linux kernel contained a serious vulnerability, CVE-2024-50264, located in the AF_VSOCK subsystem. This bug is a use-after-free flaw, a class of memory corruption issue that occurs when a program continues to use memory after it has been freed. Such flaws are particularly dangerous in the kernel, as they can allow attackers to escalate privileges. The bug was resolved in May 2025.


## Legal

### Licensing terms

Initially, Torvalds released Linux under a license that forbade any commercial use. This was changed in version 0.12 by a switch to the GNU General Public License version 2 (GPLv2). This license allows distribution and sale of possibly modified and unmodified versions of Linux but requires that all those copies be released under the same license and be accompanied by - or that, on request, free access is given to - the complete corresponding source code. Torvalds has described licensing Linux under the GPLv2 as the "best thing I ever did".

The Linux kernel is licensed explicitly under GNU General Public License version 2 only (GPL-2.0-only) with an explicit syscall exception (Linux-syscall-note), without offering the licensee the option to choose any later version, which is a common GPL extension. Contributed code must be available under GPL-compatible license.

There was considerable debate about how easily the license could be changed to use later GPL versions (including version 3), and whether this change is even desirable. Torvalds himself specifically indicated upon the release of version 2.4.0 that his own code is released only under version 2. The terms of the GPL state that if no version is specified, then any version may be used, and Alan Cox pointed out that very few other Linux contributors had specified a particular version of the GPL.

In September 2006, a survey of 29 key kernel programmers indicated that 28 preferred GPLv2 to the then-current GPLv3 draft. Torvalds commented, "I think a number of outsiders... believed that I personally was just the odd man out because I've been so publicly not a huge fan of the GPLv3." This group of high-profile kernel developers, including Torvalds, Greg Kroah-Hartman and Andrew Morton, commented on mass media about their objections to the GPLv3. They referred to clauses regarding DRM/tivoization, patents, "additional restrictions" and warned a Balkanisation of the "Open Source Universe" by the GPLv3. Torvalds, who decided not to adopt the GPLv3 for the Linux kernel, reiterated his criticism even years later.

### Loadable kernel modules

It is debated whether some loadable kernel modules (LKMs) are to be considered derivative works under copyright law, and thereby whether or not they fall under the terms of the GPL.

In accordance with the license rules, LKMs using only a public subset of the kernel interfaces are non-derived works, thus Linux gives system administrators the mechanisms to load out-of-tree binary objects into the kernel address space.

There are some out-of-tree loadable modules that make legitimate use of the *dma_buf* kernel feature. GPL compliant code can certainly use it. A different possible use case would be Nvidia Optimus that pairs a fast GPU with an Intel integrated GPU, where the Nvidia GPU writes into the Intel framebuffer when it is active. But, Nvidia cannot use this infrastructure because it necessitates bypassing a rule that can only be used by LKMs that are also GPL. Alan Cox replied on LKML, rejecting a request from one of Nvidia's engineers to remove this technical enforcement from the API. Torvalds clearly stated on the LKML that "[I] claim that binary-only kernel modules ARE derivative "by default"'".

On the other hand, Torvalds has also said that "[one] gray area in particular is something like a driver that was originally written for another operating system (i.e., clearly not a derived work of Linux in origin). THAT is a gray area, and _that_ is the area where I personally believe that some modules may be considered to not be derived works simply because they weren't designed for Linux and don't depend on any special Linux behaviour". Proprietary graphics drivers, in particular, are heavily discussed.

Whenever proprietary modules are loaded into Linux, the kernel marks itself as being "tainted", and therefore bug reports from tainted kernels will often be ignored by developers.

### Firmware binary blobs

The official kernel, that is, Torvalds's git branch at the kernel.org repository, contains binary blobs released under the terms of the GNU GPLv2 license. Linux can also load binary blobs, proprietary firmware, drivers, or other executable modules from the filesystem, and link them into kernel space.

When necessary (e.g., for accessing boot devices or for speed), firmware can be built-in to the kernel, meaning building the firmware into vmlinux; nonetheless, this is not always a viable option for technical or legal issues (e.g., it is not permitted to do this with firmware that is not GPL compatible, although this is quite common nonetheless).

### Trademark

Linux is a registered trademark of Linus Torvalds in the United States, the European Union, and some other countries. A legal battle over the trademark began in 1996, when William Della Croce, a lawyer who was never involved in the development of Linux, started requesting licensing fees for the use of the word *Linux*. After it was proven that the word was in common use long before Della Croce's claimed first use, the trademark was awarded to Torvalds.

### Removal of Russian maintainers

In October 2024, during the Russian invasion of Ukraine, kernel developer Greg Kroah-Hartman removed some kernel developers whose email addresses suggested a connection to Russia from their roles as maintainers. Linus Torvalds responded that he did not support Russian aggression and would not revert the patch, insinuating that opponents of the patch were Russian trolls. James Bottomley, a kernel developer, issued an apology for the handling of the situation and clarified that the action was a consequence of U.S. sanctions against Russia.
