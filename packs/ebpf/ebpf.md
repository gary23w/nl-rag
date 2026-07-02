---
title: "eBPF"
source: https://en.wikipedia.org/wiki/EBPF
domain: ebpf
license: CC-BY-SA-4.0
tags: ebpf, berkeley packet filter, xdp, express data path
fetched: 2026-07-02
---

# eBPF

**eBPF** is a technology that can run programs in a privileged context such as the operating system kernel. It is the successor to the Berkeley Packet Filter (BPF, with the "e" originally meaning "extended") filtering mechanism in Linux and is also used in non-networking parts of the Linux kernel.

It is used to safely and efficiently extend the capabilities of the kernel at runtime without requiring changes to kernel source code or loading kernel modules. Safety is provided through an in-kernel verifier which performs static code analysis and rejects programs which crash, hang or otherwise interfere with the kernel negatively.

This validation model differs from sandboxed environments, where the execution environment is restricted and the runtime has no insight about the program. Examples of programs that are automatically rejected are programs without strong exit guarantees (i.e. for/while loops without exit conditions) and programs dereferencing pointers without safety checks.

## Design

Loaded programs which passed the verifier are either interpreted or in-kernel just-in-time compiled (JIT compiled) for native execution performance. The execution model is event-driven and with few exceptions run-to-completion, meaning, programs can be attached to various hook points in the operating system kernel and are run upon triggering of an event. eBPF use cases include (but are not limited to) networking such as XDP, tracing and security subsystems. Given eBPF's efficiency and flexibility opened up new possibilities to solve production issues, Brendan Gregg famously dubbed eBPF "superpowers for Linux". Linus Torvalds said, "BPF has actually been really useful, and the real power of it is how it allows people to do specialized code that isn't enabled until asked for". Due to its success in Linux, the eBPF runtime has been ported to other operating systems such as Windows.

## History

eBPF evolved from the classic Berkeley Packet Filter (cBPF, a retroactively-applied name). At the most basic level, it introduced the use of ten 64-bit registers (instead of two 32-bit long registers for cBPF), different jump semantics, a call instruction and corresponding register passing convention, new instructions, and a different encoding for these instructions.

| Date | Event |
|---|---|
| April 2011 | The first in-kernel Linux just-in-time compiler (JIT compiler) for the classic Berkeley Packet Filter was merged. |
| January 2012 | The first non-networking use case of the classic Berkeley Packet Filter, seccomp-bpf, appeared; it allows filtering of system calls using a configurable policy implemented through BPF instructions. |
| March 2014 | David S. Miller, primary maintainer of the Linux networking stack, accepted the rework of the old in-kernel BPF interpreter. It was replaced by an eBPF interpreter and the Linux kernel internally translates classic BPF (cBPF) into eBPF instructions. It was released in version 3.18 of the Linux kernel. |
| March 2015 | The ability to attach eBPF to kprobes as first tracing use case was merged. In the same month, initial infrastructure work got accepted to attach eBPF to the networking traffic control (tc) layer allowing to attach eBPF to the core ingress and later also egress paths of the network stack, later heavily used by projects such as Cilium. |
| August 2015 | The eBPF compiler backend got merged into LLVM 3.7.0 release. |
| September 2015 | Brendan Gregg announced a collection of new eBPF-based tracing tools as the bcc project, providing a front-end for eBPF to make it easier to write programs. |
| July 2016 | eBPF got the ability to be attached into network driver's core receive path. This layer is known today as eXpress DataPath (XDP) and was added as a response to DPDK to create a fast data path which works in combination with the Linux kernel rather than bypassing it. |
| August 2016 | Cilium was initially announced during LinuxCon as a project providing fast IPv6 container networking with eBPF and XDP. Today, Cilium has been adopted by major cloud provider's Kubernetes offerings and is one of the most widely used CNIs. |
| November 2016 | Netronome added offload of eBPF programs for XDP and tc BPF layer to their NIC. |
| May 2017 | Meta's layer 4 load-balancer, Katran, went live. Every packet towards facebook.com since then has been processed by eBPF & XDP. |
| November 2017 | eBPF becomes its own kernel subsystem to ease the continuously growing kernel patch management. The first pull request by eBPF maintainers was submitted. |
| September 2017 | Bpftool was added to the Linux kernel as a user space utility to introspect the eBPF subsystem. |
| January 2018 | A new socket family called AF_XDP was published, allowing for high performance packet processing with zero-copy semantics at the XDP layer. Today, DPDK has an official AF_XDP poll-mode driver support. |
| February 2018 | The bpfilter prototype has been published, allowing translation of a subset of iptables rulesets into eBPF via a newly developed user mode driver. The work has caused controversies due to the ongoing nftables development effort and has not been merged into mainline. |
| October 2018 | The new bpftrace tool has been announced by Brendan Gregg as DTrace 2.0 for Linux. |
| November 2018 | eBPF introspection has been added for kTLS in order to support the ability for in-kernel TLS policy enforcement. |
| November 2018 | BTF (BPF Type Format) has been added to the Linux kernel as an efficient meta data format which is approximately 100x smaller in size than DWARF. |
| December 2019 | The first 880-page long book on BPF, written by Brendan Gregg, was released. |
| March 2020 | Google upstreamed BPF LSM support into the Linux kernel, enabling programmable Linux Security Modules (LSMs) through eBPF. |
| September 2020 | The eBPF compiler backend for GNU Compiler Collection (GCC) was merged. |
| July 2022 | Microsoft released eBPF for Windows, which runs code in the NT kernel. |
| October 2024 | The eBPF instruction set architecture (ISA) is published as RFC 9669. |

## Architecture and concepts

### eBPF maps

eBPF maps are efficient key/value stores that reside in kernel space and can be used to share data among multiple eBPF programs or to communicate between a user space application and eBPF code running in the kernel. eBPF programs can leverage eBPF maps to store and retrieve data in a wide set of data structures. Map implementations are provided by the core kernel. There are various types, including hash maps, arrays, and ring buffers.

In practice, eBPF maps are typically used for scenarios such as a user space program writing configuration information to be retrieved by an eBPF program, an eBPF program storing state for later retrieval by another eBPF program (or a future run of the same program), or an eBPF program writing results or metrics into a map for retrieval by a user space program that will present results.

### eBPF virtual machine

The eBPF virtual machine runs within the kernel and takes in a program in the form of eBPF bytecode instructions which are converted to native machine instructions that run on the CPU. Early implementations of eBPF saw eBPF bytecode interpreted, but this has now been replaced with a Just-in-Time (JIT) compilation process for performance and security-related reasons.

The eBPF virtual machine consists of eleven 64-bit registers with 32-bit subregisters, a program counter and a 512-byte large BPF stack space. These general purpose registers keep track of state when eBPF programs are executed.

### Tail calls

Tail calls can call and execute another eBPF program and replace the execution context, similar to how the execve() system call operates for regular processes. This basically allows an eBPF program to call another eBPF program. Tail calls are implemented as a long jump, reusing the same stack frame. Tail calls are particularly useful in eBPF, where the stack is limited to 512 bytes. During runtime, functionality can be added or replaced atomically, thus altering the BPF program’s execution behavior. A popular use case for tail calls is to spread the complexity of eBPF programs over several programs. Another use case is for replacing or extending logic by replacing the contents of the program array while it is in use. For example, to update a program version without downtime or to enable/disable logic.

### BPF to BPF calls

It is generally considered good practice in software development to group common code into a function, encapsulating logic for reusability. Prior to Linux kernel 4.16 and LLVM 6.0, a typical eBPF C program had to explicitly direct the compiler to inline a function, resulting in a BPF object file that had duplicate functions. This restriction was lifted, and mainstream eBPF compilers now support writing functions naturally in eBPF programs. This reduces the generated eBPF code size, making it friendlier to a CPU instruction cache.

### eBPF verifier

The verifier is a core component of eBPF, and its main responsibility is to ensure that an eBPF program is safe to execute. It performs a static analysis of the eBPF bytecode to guarantee its safety. The verifier analyzes the program to assess all possible execution paths. It steps through the instructions in order and evaluates them. The verification process starts with a depth-first search through all possible paths of the program, the verifier simulates the execution of each instruction using abstract interpretation, tracking the state of registers and stack if any instruction could lead to an unsafe state, verification fails. This process continues until all paths have been analyzed or a violation is found. Depending on the type of program, the verifier checks for violations of specific rules. These rules can include checking that an eBPF program always terminates within a reasonable amount of time (no infinite loops or infinite recursion), checking that an eBPF program is not allowed to read arbitrary memory because being able to arbitrary read memory could allow a program to leak sensitive information, checking that network programs are not allowed to access memory outside of packet bounds because adjacent memory could contain sensitive information, checking that programs are not allowed to deadlock, so any held spinlocks must be released and only one lock can be held at a time to avoid deadlocks over multiple programs, checking that programs are not allowed to read uninitialized memory.  This is not an exhaustive list of the checks the verifier does, and there are exceptions to these rules. An example is that tracing programs have access to helpers that allow them to read memory in a controlled way, but these program types require root privileges and thus do not pose a security risk.

Over time the eBPF verifier has evolved to include newer features and optimizations, such as support for bounded loops, dead-code elimination, function-by-function verification, and callbacks.

### eBPF CO-RE (compile once - run everywhere)

eBPF programs use the memory and data structures from the kernel. Some structures can be modified between different kernel versions, altering the memory layout. Since the Linux kernel is continuously developed, there is no guarantee that the internal data structures will remain the same across different versions. CO-RE is a fundamental concept in modern eBPF development that allows eBPF programs to be portable across different kernel versions and configurations. It addresses the challenge of kernel structure variations between different Linux distributions and versions. CO-RE comprises BTF (BPF Type Format) - a metadata format that describes the types used in the kernel and eBPF programs and provides detailed information about struct layouts, field offsets, and data types. It enables runtime accessibility of kernel types, which is crucial for BPF program development and verification. BTF is included in the kernel image of BTF-enabled kernels. Special relocations are emitted by the compiler (e.g., LLVM). These relocations capture high-level descriptions of what information the eBPF program intends to access. The libbpf library adapts eBPF programs to work with the data structure layout on the target kernel where they run, even if this layout is different from the kernel where the code was compiled. To do this, libbpf needs the BPF CO-RE relocation information generated by Clang as part of the compilation process. The compiled eBPF program is stored in an Executable and Linkable Format (ELF) object file. This file contains BTF-type information and Clang-generated relocations. The ELF format allows the eBPF loader (e.g., libbpf) to process and adjust the BPF program dynamically for the target kernel.

## Branding

The alias eBPF is often interchangeably used with BPF, for example by the Linux kernel community. eBPF and BPF is referred to as a technology name like LLVM. eBPF evolved from the machine language for the filtering virtual machine in the Berkeley Packet Filter as an extended version, but as its use cases outgrew networking, today "eBPF" is preferentially interpreted as a pseudo-acronym.

The bee is the official logo for eBPF. At the first eBPF Summit there was a vote taken and the bee mascot was named "eBee". The logo was originally created by Vadim Shchekoldin. Earlier unofficial eBPF mascots have existed in the past, but have not seen widespread adoption.

## Governance

The eBPF Foundation was created in August 2021 with the goal to expand the contributions being made to extend the powerful capabilities of eBPF and grow beyond Linux. Founding members include Meta, Google, Isovalent, Microsoft and Netflix. The purpose is to raise, budget, and spend funds in support of various open source, open data and/or open standards projects relating to eBPF technologies to further drive the growth and adoption of the eBPF ecosystem. Since inception, Red Hat, Huawei, Crowdstrike, Tigera, DaoCloud, Datoms, FutureWei also joined.

## Adoption

eBPF has been adopted by a number of large-scale production users, for example:

- Meta uses eBPF through their Katran layer 4 load balancer for all traffic going to facebook.com
- Google uses eBPF in GKE, developed and uses BPF LSM to replace audit and it uses eBPF for networking
- Cloudflare uses eBPF for load balancing and DDoS protection and security enforcement
- Netflix uses eBPF for fleet-wide network observability and performance diagnosis
- Dropbox uses eBPF through Katran for layer 4 load balancing
- Android uses eBPF for NAT46 and traffic monitoring
- Samsung Galaxy uses eBPF for networking solutions
- Yahoo! Inc uses eBPF through Cilium for layer 4 load balancing
- LinkedIn uses eBPF for infrastructure observability
- Alibaba uses eBPF for Kubernetes Pod load balancing
- Datadog uses eBPF for Kubernetes Pod networking and security enforcement
- Trip.com uses eBPF for Kubernetes Pod networking
- Shopify uses eBPF for intrusion detection through Falco
- DoorDash uses eBPF through BPFAgent for kernel-level monitoring
- Microsoft ported eBPF and XDP to Windows
- Seznam uses eBPF through Cilium for layer 4 load balancing
- DigitalOcean uses eBPF and XDP to rate limit access to internal services in their virtual network
- CapitalOne uses eBPF for Kubernetes Pod networking
- Bell Canada uses eBPF to modernize telco networking with SRv6
- Elastic_NV uses eBPF for code profiling as part of their observability offering
- Apple uses eBPF for Kubernetes Pod security
- Sky uses eBPF for Kubernetes Pod networking
- Walmart uses eBPF for layer 4 load balancing
- Huawei uses eBPF through their DIGLIM secure boot system
- Ikea uses eBPF for Kubernetes Pod networking
- The New York Times uses eBPF for networking
- Red Hat uses eBPF at scale for load balancing and tracing in their private cloud
- Palantir Technologies uses eBPF to debug networking problems in large scale Kubernetes clusters
- Bloombase uses eBPF for threat detection and mitigation on networked storage layer

## Security

Due to the ease of programmability, eBPF has been used as a tool for implementing microarchitectural timing side-channel attacks such as Spectre against vulnerable microprocessors. While unprivileged eBPF implements mitigations against Spectre v1, v2, and v4 for x86-64, unprivileged use has ultimately been disabled by the kernel community by default to protect users of unsupported architectures and limit the impact of future hardware vulnerabilities. On x86-64, Spectre v1 is mitigated through a combination of branchless bounds-enforcement (e.g., masking instructions) and the verification of speculative execution paths. Spectre v4 is mitigated exclusively through speculation barriers (i.e., lfence) and Spectre v2 is mitigated through retpoline when available or speculation barriers. These mitigations prevent sensitive information owned by the kernel (e.g., kernel addresses) from being leaked by malicious eBPF programs, but are not designed to prevent innocuous eBPF programs from accidentally leaking sensitive information they own/process (e.g., cryptographic keys stored as numbers).
