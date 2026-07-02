---
title: "Berkeley Packet Filter"
source: https://en.wikipedia.org/wiki/Berkeley_Packet_Filter
domain: ebpf-security-monitoring
license: CC-BY-SA-4.0
tags: ebpf security monitoring, kernel event tracing, system call observability, kernel level instrumentation, runtime threat detection
fetched: 2026-07-02
---

# Berkeley Packet Filter

The **Berkeley Packet Filter** (**BPF**; also **BSD Packet Filter**, **classic BPF** or **cBPF**) is a network tap mechanism and packet filter which permits computer network packets to be captured and filtered at the operating system level. It provides a raw interface to data link layers, permitting raw link-layer packets to be sent and received, and allows a userspace process to supply a filter program that specifies which packets it wants to receive. For example, a tcpdump process may want to receive only packets that initiate a TCP connection. BPF returns only packets that pass the filter that the process supplies. This avoids copying unwanted packets from the operating system kernel to the process, greatly improving performance. The filter program is in the form of instructions for a virtual machine, which are interpreted, or compiled into machine code by a just-in-time (JIT) mechanism and executed, in the kernel.

BPF is used by programs that need to, among other things, analyze network traffic. If the driver for the network interface supports promiscuous mode, it allows the interface to be put into that mode so that all packets on the network can be received, even those destined to other hosts.

The BPF filtering mechanism is available on most Unix-like operating systems. BPF is sometimes used to refer to just the filtering mechanism, rather than to the entire interface. Some systems, such as Linux and Tru64 UNIX, provide a raw interface to the data link layer other than the BPF raw interface but use the BPF filtering mechanisms for that raw interface.

The Linux kernel provides an extended version of the BPF filtering mechanism, called eBPF, which uses a JIT mechanism, and which is used for packet filtering, as well as for other purposes in the kernel. eBPF is also available for Microsoft Windows.

## History

The original paper was written by Steven McCanne and Van Jacobson in 1992 while at Lawrence Berkeley Laboratory.

## Raw data-link interface

BPF provides pseudo-devices that can be bound to a network interface; reads from the device will read buffers full of packets received on the network interface, and writes to the device will inject packets on the network interface.

In 2007, Robert Watson and Christian Peron added zero-copy buffer extensions to the BPF implementation in the FreeBSD operating system, allowing kernel packet capture in the device driver interrupt handler to write directly to user process memory in order to avoid the requirement for two copies for all packet data received via the BPF device. While one copy remains in the receipt path for user processes, this preserves the independence of different BPF device consumers, as well as allowing the packing of headers into the BPF buffer rather than copying complete packet data.

## Filtering

BPF's filtering capabilities are implemented as an interpreter for a machine language for the BPF virtual machine, a 32-bit machine with fixed-length instructions, one accumulator, and one index register. Programs in that language can fetch data from the packet, perform arithmetic operations on data from the packet, and compare the results against constants or against data in the packet or test bits in the results, accepting or rejecting the packet based on the results of those tests.

BPF is often extended by "overloading" the load (ld) and store (str) instructions.

Traditional Unix-like BPF implementations can be used in userspace, despite being written for kernel-space. This is accomplished using preprocessor conditions.

Since version 3.18, the Linux kernel includes an extended BPF virtual machine with ten 64-bit registers, termed eBPF. It can be used for non-networking purposes, such as for attaching eBPF programs to various tracepoints. Since kernel version 3.19, eBPF filters can be attached to sockets, and, since kernel version 4.1, to traffic control classifiers for the ingress and egress networking data path. The original and obsolete version has been retroactively renamed to *classic BPF* (*cBPF*). Nowadays, the Linux kernel runs eBPF only and loaded cBPF bytecode is transparently translated into an eBPF representation in the kernel before program execution. All bytecode is verified before running to prevent denial-of-service attacks. Until Linux 5.3, the verifier prohibited the use of loops, to prevent potentially unbounded execution times; loops with bounded execution time are now permitted in more recent kernels.

## Extensions and optimizations

Some projects use BPF instruction sets or execution techniques different from the originals.

Some platforms, including FreeBSD, NetBSD, and WinPcap, use a just-in-time compiler (JIT) to convert BPF instructions into native code in order to improve performance. Linux includes a BPF JIT compiler which is disabled by default.

Kernel-mode interpreters for that same virtual machine language are used in raw data link layer mechanisms in other operating systems, such as Tru64 Unix, and for socket filters in the Linux kernel and in the WinPcap and Npcap packet capture mechanism.

## Implementations

A user-mode interpreter for BPF is provided with the libpcap/WinPcap/Npcap implementation of the pcap API, so that, when capturing packets on systems without kernel-mode support for that filtering mechanism, packets can be filtered in user mode; code using the pcap API will work on both types of systems, although, on systems where the filtering is done in user mode, all packets, including those that will be filtered out, are copied from the kernel to user space. That interpreter can also be used when reading a file containing packets captured using pcap.

Another user-mode interpreter is *uBPF*, which supports JIT and eBPF (without cBPF). Its code has been reused to provide eBPF support in non-Linux systems. Microsoft's *eBPF on Windows* builds on uBPF and the PREVAIL formal verifier. *rBPF*, a Rust rewrite of uBPF, is used by the Solana blockchain platform as the execution engine.

## Programming

Classic BPF is generally emitted by a program from some very high-level textual rule describing the pattern to match. One such representation is found in libpcap. Classic BPF and eBPF can also be written either directly as machine code, or using an assembly language for a textual representation. Notable assemblers include Linux kernel's `bpf_asm` tool (cBPF), `bpfc` (cBPF), and the `ubpf` assembler (eBPF). The `bpftool` command can also act as a disassembler for both flavors of BPF. The assembly languages are not necessarily compatible with each other.

eBPF bytecode has recently become a target of higher-level languages. LLVM added eBPF support in 2014, and GCC followed in 2019. Both toolkits allow compiling C and other supported languages to eBPF. A subset of P4 can also be compiled into eBPF using BCC, an LLVM-based compiler kit.

## Security

The Spectre attack could leverage the Linux kernel's eBPF interpreter or JIT compiler to extract data from other kernel processes. A JIT hardening feature in the kernel mitigates this vulnerability.

Chinese computer security group Pangu Lab said the NSA used BPF to conceal network communications as part of a complex Linux backdoor.
