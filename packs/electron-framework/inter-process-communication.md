---
title: "Inter-process communication"
source: https://en.wikipedia.org/wiki/Inter-process_communication
domain: electron-framework
license: CC-BY-SA-4.0
tags: electron framework, chromium desktop app, node desktop runtime, web technology packaging
fetched: 2026-07-02
---

# Inter-process communication

In computer science, **interprocess communication** (**IPC**) is the sharing of data between running processes in a computer system, or between multiple such systems. Mechanisms for IPC may be provided by an operating system. Applications which use IPC are often categorized as clients and servers, where the client requests data and the server responds to client requests. Many applications are both clients and servers, as commonly seen in distributed computing.

IPC is very important to the design process for microkernels and nanokernels, which reduce the number of functionalities provided by the kernel. Those functionalities are then obtained by communicating with servers via IPC, leading to a large increase in communication when compared to a regular monolithic kernel. IPC interfaces generally encompass variable analytic framework structures. These processes ensure compatibility between the multi-vector protocols upon which IPC models rely.

An IPC mechanism is either synchronous or asynchronous. Synchronization primitives may be used to have synchronous behavior with an asynchronous IPC mechanism.

## Disadvantages

Merging data from two processes can often incur significantly higher costs compared to processing the same data on a single thread, potentially by two or more orders of magnitude due to overheads such as inter-process communication and synchronization.

## Approaches

Different approaches to IPC have been tailored to different software requirements, such as performance, modularity, and system circumstances such as network bandwidth and latency.

| Method | Short Description | Provided by (operating systems or other environments) |
|---|---|---|
| File | A record stored on disk, or a record synthesized on demand by a file server, which can be accessed by multiple processes. | Most operating systems |
| Communications file | A unique form of IPC in the late-1960s that most closely resembles Plan 9's 9P protocol | Dartmouth Time-Sharing System |
| Signal; also Asynchronous System Trap | A system message sent from one process to another, not usually used to transfer data but instead used to remotely command the partnered process. | Most operating systems |
| Socket | Data sent over a network interface, either to a different process on the same computer or to another computer on the network. Stream-oriented (TCP; data written through a socket requires formatting to preserve message boundaries) or more rarely message-oriented (UDP, SCTP). | Most operating systems |
| Unix domain socket | Similar to an internet socket, but all communication occurs within the kernel. Domain sockets use the file system as their address space. Processes reference a domain socket as an inode, and multiple processes can communicate with one socket | All POSIX operating systems and Windows 10 |
| Message queue | A data stream similar to a socket, but which usually preserves message boundaries. Typically implemented by the operating system, they allow multiple processes to read and write to the message queue without being directly connected to each other. | Most operating systems |
| Anonymous pipe | A unidirectional data channel using standard input and output. Data written to the write-end of the pipe is buffered by the operating system until it is read from the read-end of the pipe. Two-way communication between processes can be achieved by using two pipes in opposite "directions". | All POSIX systems, Windows |
| Named pipe | A pipe that is treated like a file. Instead of using standard input and output as with an anonymous pipe, processes write to and read from a named pipe, as if it were a regular file. | All POSIX systems, Windows, AmigaOS 2.0+ |
| Shared memory | Multiple processes are given access to the same block of memory, which creates a shared buffer for the processes to communicate with each other. | All POSIX systems, Windows |
| Message passing | Allows multiple programs to communicate using message queues and/or non-OS managed channels. Commonly used in concurrency models. | Used in LPC, RPC, RMI, and MPI paradigms, Java RMI, CORBA, COM, DDS, MSMQ, MailSlots, QNX, others |
| Memory-mapped file | A file mapped to RAM and can be modified by changing memory addresses directly instead of outputting to a stream. This shares the same benefits as a standard file. | All POSIX systems, Windows |

## Applications

### Remote procedure call interfaces

- Java's Remote Method Invocation (RMI)
- ONC RPC
- XML-RPC or SOAP
- JSON-RPC
- Message Bus (Mbus) (specified in RFC 3259) (not to be confused with M-Bus)
- .NET Remoting
- gRPC

### Platform communication stack

The following are messaging, and information systems that utilize IPC mechanisms but don't implement IPC themselves:

- KDE's Desktop Communications Protocol (DCOP) – deprecated by D-Bus
- D-Bus
- OpenWrt uses ubus micro bus architecture
- MCAPI Multicore Communications API
- SIMPL The Synchronous Interprocess Messaging Project for Linux (SIMPL)
- 9P (Plan 9 Filesystem Protocol)
- Distributed Computing Environment (DCE)
- Thrift
- ZeroC's Internet Communications Engine (ICE)
- ØMQ
- YAMI4
- Enlightenment_(software) E16 uses eesh as an IPC

### Operating system communication stack

The following are platform or programming language-specific APIs:

- Apple Computer's Apple events, previously known as Interapplication Communications (IAC)
- ARexx ports
- Enea's LINX for Linux (open source) and various DSP and general-purpose processors under OSE
- The Mach kernel's Mach Ports
- Microsoft's ActiveX, Component Object Model (COM), Microsoft Transaction Server (COM+), Distributed Component Object Model (DCOM), Dynamic Data Exchange (DDE), Object Linking and Embedding (OLE), anonymous pipes, named pipes, Local Procedure Call, MailSlots, Message loop, MSRPC, .NET Remoting, and Windows Communication Foundation (WCF)
- Novell's SPX
- POSIX mmap, message queues, semaphores, and shared memory
- RISC OS's messages
- Solaris Doors
- System V's message queues, semaphores, and shared memory
- Linux Transparent Inter Process Communication (TIPC)
- OpenBinder Open binder
- QNX's PPS (Persistent Publish/Subscribe) service

### Distributed object models

The following are platform or programming language specific-APIs that use IPC, but do not themselves implement it:

- PHP's sessions
- Distributed Ruby
- Common Object Request Broker Architecture (CORBA)
- Electron's asynchronous IPC, shares JSON objects between a main and a renderer process
