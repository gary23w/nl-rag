---
title: "Kernel (operating system) (part 2/2)"
source: https://en.wikipedia.org/wiki/Kernel_(operating_system)
domain: kernel-hardening
license: CC-BY-SA-4.0
tags: linux kernel hardening, kernel self protection, kernel attack surface reduction, kernel address space isolation
fetched: 2026-07-02
part: 2/2
---

## History of kernel development

### Early operating system kernels

Strictly speaking, an operating system (and thus, a kernel) is not *required* to run a computer. Programs can be directly loaded and executed on the "bare metal" machine, provided that the authors of those programs are willing to work without any hardware abstraction or operating system support. Most early computers operated this way during the 1950s and early 1960s, which were reset and reloaded between the execution of different programs. Eventually, small ancillary programs such as program loaders and debuggers were left in memory between runs, or loaded from ROM. As these were developed, they formed the basis of what became early operating system kernels. The "bare metal" approach is still used today on some video game consoles and embedded systems, but in general, newer computers use modern operating systems and kernels.

In 1969, the RC 4000 Multiprogramming System introduced the system design philosophy of a small nucleus "upon which operating systems for different purposes could be built in an orderly manner", what would be called the microkernel approach.

### Time-sharing operating systems

In the decade preceding Unix, computers had grown enormously in power – to the point where computer operators were looking for new ways to get people to use their spare time on their machines. One of the major developments during this era was time-sharing, whereby a number of users would get small slices of computer time, at a rate at which it appeared they were each connected to their own, slower, machine.

The development of time-sharing systems led to a number of problems. One was that users, particularly at universities where the systems were being developed, wanted to hack the system to get more CPU time. For this reason, security and access control became a major focus of the Multics project in 1965. Another ongoing issue was properly handling computing resources: users spent most of their time staring at the terminal and thinking about what to input instead of actually using the resources of the computer, and a time-sharing system should give the CPU time to an active user during these periods. Finally, the systems typically offered a memory hierarchy several layers deep, and partitioning this expensive resource led to major developments in virtual memory systems.

### Amiga

The Commodore Amiga was released in 1985, and was among the first – and certainly most successful – home computers to feature an advanced kernel architecture. The AmigaOS kernel's executive component, *exec.library*, uses a microkernel message-passing design, but there are other kernel components, like *graphics.library*, that have direct access to the hardware. There is no memory protection, and the kernel is almost always running in user mode. Only special actions are executed in kernel mode, and user-mode applications can ask the operating system to execute their code in kernel mode.

### Unix

During the design phase of Unix, programmers decided to model every high-level device as a file, because they believed the purpose of computation was data transformation.

For instance, printers were represented as a "file" at a known location – when data was copied to the file, it printed out. Other systems, to provide a similar functionality, tended to virtualize devices at a lower level – that is, both devices *and* files would be instances of some lower level concept. Virtualizing the system at the file level allowed users to manipulate the entire system using their existing file management utilities and concepts, dramatically simplifying operation. As an extension of the same paradigm, Unix allows programmers to manipulate files using a series of small programs, using the concept of pipes, which allowed users to complete operations in stages, feeding a file through a chain of single-purpose tools. Although the end result was the same, using smaller programs in this way dramatically increased flexibility as well as ease of development and use, allowing the user to modify their workflow by adding or removing a program from the chain.

In the Unix model, the *operating system* consists of two parts: first, the huge collection of utility programs that drive most operations; second, the kernel that runs the programs. Under Unix, from a programming standpoint, the distinction between the two is fairly thin; the kernel is a program, running in supervisor mode, that acts as a program loader and supervisor for the small utility programs making up the rest of the system, and to provide locking and I/O services for these programs; beyond that, the kernel did not intervene at all in user space.

Over the years the computing model changed, and Unix's treatment of everything as a file or byte stream no longer was as universally applicable as it was before. Although a terminal could be treated as a file or a byte stream, which is printed to or read from, the same did not seem to be true for a graphical user interface. Networking posed another problem. Even if network communication can be compared to file access, the low-level packet-oriented architecture dealt with discrete chunks of data and not with whole files. As the capability of computers grew, Unix became increasingly cluttered with code. It is also because the modularity of the Unix kernel is extensively scalable. While kernels might have had 100,000 lines of code in the seventies and eighties, kernels like Linux, of modern Unix successors like GNU, have more than 13 million lines.

Modern Unix-derivatives are generally based on module-loading monolithic kernels. Examples of this are the Linux kernel in the many distributions of GNU, IBM AIX, as well as the Berkeley Software Distribution variant kernels such as FreeBSD, DragonFly BSD, OpenBSD, NetBSD, and macOS. Apart from these alternatives, amateur developers maintain an active operating system development community, populated by self-written hobby kernels that mostly end up sharing many features with Linux, FreeBSD, DragonflyBSD, OpenBSD, or NetBSD kernels and/or being compatible with them.

### Classic Mac OS and macOS

Apple first launched its classic Mac OS in 1984, bundled with its Macintosh personal computer. Apple moved to a nanokernel design in Mac OS 8.6. Against this, the modern macOS (originally named Mac OS X) is based on Darwin, which uses a hybrid kernel called XNU, which was created by combining the 4.3BSD kernel and the Mach kernel.

### Microsoft Windows

Microsoft Windows was first released in 1985 as an add-on to MS-DOS. Because of its dependence on another operating system, initial releases of Windows, prior to Windows 95, were considered an operating environment (not to be confused with an operating system). This product line continued to evolve through the 1980s and 1990s, with the Windows 9x series adding 32-bit addressing and pre-emptive multitasking; but ended with the release of Windows Me in 2000.

Microsoft also developed Windows NT, an operating system with a very similar interface, but intended for high-end and business users. This line started with the release of Windows NT 3.1 in 1993, and was introduced to general users with the release of Windows XP in October 2001—replacing Windows 9x with a completely different, much more sophisticated operating system. This is the line that continues with Windows 11.

The architecture of Windows NT's kernel is considered a hybrid kernel because the kernel itself contains tasks such as the Window Manager and the IPC Managers, with a client/server layered subsystem model. It was designed as a modified microkernel, as the Windows NT kernel was influenced by the Mach microkernel but does not meet all of the criteria of a pure microkernel.

### IBM Supervisor

Supervisory program or supervisor is a computer program, usually part of an operating system, that controls the execution of other routines and regulates work scheduling, input/output operations, error actions, and similar functions and regulates the flow of work in a data processing system.

Historically, this term was essentially associated with IBM's line of mainframe operating systems starting with OS/360. In other operating systems, the supervisor is generally called the kernel.

In the 1970s, IBM further abstracted the supervisor state from the hardware, resulting in a hypervisor that enabled full virtualization, i.e. the capacity to run multiple operating systems on the same machine totally independent of each other. Hence the first such system was called *Virtual Machine* or *VM*.

### Development of microkernels

Although Mach, developed by Richard Rashid at Carnegie Mellon University, is the best-known general-purpose microkernel, other microkernels have been developed with more specific aims. The L4 microkernel family (mainly the L3 and the L4 kernel) was created to demonstrate that microkernels are not necessarily slow. Newer implementations such as Fiasco and Pistachio are able to run Linux next to other L4 processes in separate address spaces.

Additionally, QNX is a microkernel that is principally used in embedded systems, and the open-source software MINIX, while originally created for educational purposes, is now focused on being a highly reliable and self-healing microkernel OS.
