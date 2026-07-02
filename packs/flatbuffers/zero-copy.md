---
title: "Zero-copy"
source: https://en.wikipedia.org/wiki/Zero-copy
domain: flatbuffers
license: CC-BY-SA-4.0
tags: google flatbuffers, zero-copy serialization, flatbuffers schema, memory-efficient format
fetched: 2026-07-02
---

# Zero-copy

In computer science, **zero-copy** refers to techniques that enable data transfer between memory spaces without requiring the CPU to copy the data. By avoiding redundant copying, zero-copy methods minimize CPU usage and memory bandwidth, leading to substantial performance gains. This is crucial for applications demanding high data throughput, such as network communication, file I/O, and multimedia processing.

## Principle

Zero-copy programming techniques can be used when exchanging data within a user space process (i.e. between two or more threads, etc.) and/or between two or more processes (see also producer–consumer problem) and/or when data has to be accessed / copied / moved inside kernel space or between a user space process and kernel space portions of operating systems (OS).

Usually when a user space process has to execute system operations like reading or writing data from/to a device (i.e. a disk, a NIC, etc.) through their high level software interfaces or like moving data from one device to another, etc., it has to perform one or more system calls that are then executed in kernel space by the operating system.

If data has to be copied or moved from source to destination and both are located inside kernel space (i.e. two files, a file and a network card, etc.) then unnecessary data copies, from kernel space to user space and from user space to kernel space, can be avoided by using special (zero-copy) system calls, usually available in most recent versions of popular operating systems.

Zero-copy versions of operating system elements, such as device drivers, file systems, network protocol stacks, etc., greatly increase the performance of certain application programs (that become processes when executed) and more efficiently utilize system resources. Performance is enhanced by allowing the CPU to move on to other tasks while data copies / processing proceed in parallel in another part of the machine. Also, zero-copy operations reduce the number of time-consuming context switches between user space and kernel space. System resources are utilized more efficiently since using a sophisticated CPU to perform extensive data copy operations, which is a relatively simple task, is wasteful if other simpler system components can do the copying.

As an example, reading a file and then sending it over a network the traditional way requires 2 extra data copies (1 to read from kernel to user space + 1 to write from user to kernel space) and 4 context switches per read/write cycle. Those extra data copies use the CPU. Sending that file by using mmap of file data and a cycle of write calls, reduces the context switches to 2 per write call and avoids those previous 2 extra user data copies. Sending the same file via zero copy reduces the context switches to 2 per sendfile call and eliminates all CPU extra data copies (both in user and in kernel space).

Zero-copy protocols are especially important for very high-speed networks in which the capacity of a network link approaches or exceeds the CPU's processing capacity. In such a case the CPU may spend nearly all of its time copying transferred data, and thus becomes a bottleneck which limits the communication rate to below the link's capacity. A rule of thumb used in the industry is that roughly one CPU clock cycle is needed to process one bit of incoming data.

## Hardware implementations

An early implementation was IBM OS/360 where a program can instruct the channel subsystem to read blocks of data from one file or device into a buffer and write to another from the same buffer without moving the data.

Techniques for creating zero-copy software include the use of direct memory access (DMA)-based copying and memory-mapping through a memory management unit (MMU). These features require specific hardware support and usually involve particular memory alignment requirements.

A newer approach used by the Heterogeneous System Architecture (HSA) facilitates the passing of pointers between the CPU and the GPU and also other processors. This requires a unified address space for the CPU and the GPU.

## Program interfaces

Several operating systems support zero-copying of user data and file contents through specific APIs.

Here are listed only a few well known system calls / APIs available in most popular OSs.

Novell NetWare supports a form of zero-copy through Event Control Blocks (ECBs), see NCOPY.

The internal COPY command in some versions of DR-DOS since 1992 initiates this as well when COMMAND.COM detects that the files to be copied are stored on a NetWare file server, otherwise it falls back to normal file copying. The external MOVE command since DR DOS 6.0 (1991) and MS-DOS 6.0 (1993) internally performs a RENAME (causing just the directory entries to be modified in the file system instead of physically copying the file data) when the source and destination are located on the same logical volume.

The Linux kernel supports zero-copy through various system calls, such as:

- sendfile, sendfile64;
- splice;
- tee;
- vmsplice;
- process_vm_readv;
- process_vm_writev;
- copy_file_range;
- raw sockets with packet mmap or AF_XDP.

Some of them are specified in POSIX and thus also present in the BSD kernels or IBM AIX, some are unique to the Linux kernel API.

FreeBSD, NetBSD, OpenBSD, DragonFly BSD, etc. support zero-copy through at least these system calls:

- sendfile;
- write, writev + mmap when writing data to a network socket.

MacOS should support zero-copy through the FreeBSD portion of the kernel because it offers the same system calls (and its manual pages are still tagged BSD) such as:

- sendfile.

Oracle Solaris supports zero-copy through at least these system calls:

- sendfile;
- sendfilev;
- write, writev + mmap.

Microsoft Windows supports zero-copy through at least this system call:

- TransmitFile.

Java input streams can support zero-copy through the java.nio.channels.FileChannel's transferTo() method if the underlying operating system also supports zero copy.

RDMA (Remote Direct Memory Access) protocols deeply rely on zero-copy techniques.
