---
title: "seL4"
source: https://en.wikipedia.org/wiki/SeL4
domain: sel4-microkernel
license: CC-BY-SA-4.0
tags: sel4 microkernel, formally verified kernel, capability-based security, isabelle proof
fetched: 2026-07-02
---

# seL4

**seL4** (security enhanced L4) is an open-source, high-assurance, capability-based microkernel. It inherits the performance and design characteristics of the L4 microkernel lineage but is implemented using high-assurance methods. seL4 uses formal mathematical verification to prove the system's confidentiality, integrity, availability among other properties. The initial paper outlining seL4's verification was inducted into the 2019 ACM SIGOPS Hall of Fame.

## History

seL4 was developed as a from-scratch microkernel design influenced by the L4 microkernel family, with an explicit goal of enabling comprehensive formal verification while maintaining high performance. In 2009, the seL4 project reported a machine-checked proof of functional correctness spanning from formal specification to C implementation.

In July 2014, the seL4 kernel sources and verification artifacts were released as open source by NICTA with industry partners.

On 7 April 2020, the seL4 Foundation was launched to support governance, ecosystem development and long-term stewardship; it was initially hosted as a project of the Linux Foundation.

## Architecture

seL4 is *extremely* minimal, even compared to prior L4 kernels: it only handles memory management/process isolation and process scheduling - everything else is handled outside of kernel mode. At boot time, the seL4 kernel statically allocates enough memory for itself and then hands over all remaining memory and capabilities to an initial user space process. seL4 is more akin to a CPU driver than other commercial microkernels like Mach, QNX, or Minix. The primary motivation was to enable policy and architectural freedom for system builders, but it also helps make verification easier and minimizes cache misses.

### Capability-based access control

seL4 uses a capability-based model to control all access to memory and kernel resources. This enables resources and information flow to be reasoned about and managed in a programmatic manner (as opposed to a one-size-fits all security and architecture policies). In this model, a *capability* is an unforgeable token that both names a kernel object and encodes the operations that may be performed on it. Capabilities are stored in kernel-managed tables called *capability nodes* (CNodes), which form a hierarchical namespace analogous to a file-system directory structure. A CNode contains capability slots and is itself a kernel object accessed only through a capability, allowing authority over resources to be explicitly delegated, subdivided, or revoked.

Physical memory in seL4 is initially represented as *untyped memory* capabilities, which grant authority over raw regions of RAM but do not correspond to usable objects. Untyped memory is converted into typed kernel objects via a *retype* operation. The kernel records the relationships between untyped memory and derived objects in a *capability derivation tree* (CDT), which allows the system to enforce safe memory reuse: all capabilities derived from an untyped region must be removed before that region can be reallocated. This mechanism replaces implicit kernel allocators with an explicit, auditable memory lifecycle under application control.

Virtual memory management is also capability-governed. A capability to a memory frame confers the authority to map that frame into an address space, subject to the access rights encoded in the capability. Address spaces themselves are constructed from page table objects that are likewise created from untyped memory and referenced via capabilities. In addition to general-purpose memory, seL4 distinguishes *device untyped memory*, which is subject to additional restrictions to prevent unsafe retyping or reuse.

### Inter-Process Communication (IPC)

seL4 IPC is *not* intended as a general-purpose message-passing mechanism, but as a way to implement cross-domain invocation of functions or services across protection boundaries. seL4's designers frame it as a Protected Procedure Call (PPC), which carries only small argument and return values (similar to a function call across protection domains) rather than a buffering transport for arbitrary data. seL4's designers explicitly recommend against using IPC for shipping bulk data or for synchronization, instead using IPC primarily for *request–reply invocation of services* and *capability transfer*.

Inter-process communication in seL4 is based on capability-governed kernel objects and is designed to minimize kernel state while making authority explicit. The primary IPC object is the *endpoint*, which represents both the right to communicate and the rendezvous point for communication: a thread may send to or receive from an endpoint only if it holds an appropriate capability.

IPC via endpoints is synchronous and blocking (with other conventions layered on top). A send operation waits until a receiver is ready, and a receive operation waits until a sender arrives. Unlike many traditional message-passing systems, seL4 endpoints do not provide kernel-managed message queues or mailboxes. The kernel maintains only queues of waiting threads, and message data is transferred directly between the communicating threads using a small, fixed-size payload. This avoids implicit kernel memory allocation during communication and is consistent with seL4's explicit resource-management model. Messages may include both data and selected capabilities, allowing IPC to serve not only as a communication mechanism but also as a means of explicitly delegating authority. Transferring a capability during IPC directly transfers the right to access a kernel object, tightly integrating communication and access control.

#### Control-plane and data-plane separation

While synchronous IPC is the fundamental communication primitive provided by the kernel, it is not intended as a way to transmit bulk data and its use within seL4 based systems is minimized on performance-critical paths. Systems commonly separate communication into a *control plane* and a *data plane.* IPC is used primarily for control operations such as configuration, request–reply interactions, and capability transfer, while bulk or high-frequency data exchange is implemented in user space using shared memory combined with asynchronous notifications.

Shared memory regions are explicitly created from untyped memory and mapped into multiple address spaces, and notifications are used to signal availability of data or completion of work. This pattern enables the implementation of lock-free or wait-free data structures such as ring buffers without involving the kernel in the data path. By keeping the kernel out of bulk data transfer, seL4 systems reduce copying overhead, avoid unnecessary blocking, and preserve the simplicity required for formal verification. This design approach is promoted by higher-level frameworks in the seL4 ecosystem, including CAmkES, the seL4 Device Driver Framework (sDDF), and the seL4 Microkit.

#### Comparison with other IPC models

- **POSIX message queues**: POSIX message queues expose named, kernel-resident queues that support asynchronous message passing. They rely on implicit kernel memory allocation and a global namespace, and separate message passing from access-control mechanisms. By contrast, seL4 has no global IPC namespace and no kernel-managed message queues; all communication requires possession of an explicit endpoint capability, and buffering policies are implemented in user space if required.
- **Mach ports**: Mach ports combine naming and authority for IPC and are typically associated with kernel-managed message queues and asynchronous buffered communication. In contrast, seL4 endpoints avoid kernel message buffering and instead provide synchronous rendezvous semantics, reducing kernel complexity and hidden resource usage compared with Mach's more flexible but slower IPC mechanisms.
- **L4 IPC**: seL4's IPC model is directly descended from earlier L4 microkernels, which also emphasized synchronous, high-performance message passing. seL4 retains rendezvous-style IPC semantics, however, it decouples message passing from synchronization. This enables optimizing the former for PPC (server invocations) and integrates them more tightly with a formal capability system and a verified kernel design, making authority transfer explicit and amenable to formal reasoning.

#### Notifications and event signalling

In addition to endpoints, seL4 provides *notification* objects: semaphore like objects for asynchronous event signalling and lightweight synchronization. Notifications are commonly used to deliver hardware interrupt events to user-space device drivers or to signal state changes between components, supporting a microkernel architecture in which interrupt handling and drivers execute outside the kernel.

## Formal Verification

seL4's uses specifications written as mathematical models in Isabelle/HOL to describe the correct operation of system calls. These specifications are then connected to the C implementation to prove that it is functionally correct: all system calls perform the correct operations and return the correct results (no logic errors, will not crash, will not hang, etc). This results in a *very* high degree of assurance that the kernel's capability system enforces the key CIA infosec properties for processes: **confidentiality** of information between processes, the **integrity** of kernel state and control flow, and **availability** by preventing denial-of-service to authorized resource usage.

At ~10k LoC and ~500k LoP, it is one of the largest verification products ever produced, for which the initial paper was inducted into ACM SIGOPS Hall of Fame in 2019. The proof overhead of 50 lines of proof per 1 line of C code drastically increases the cost of development and slows development velocity - making changes difficult. However, its authors claim that at $400/LoC, the cost was less than the $1,000/LoC for similar high assurance (but not verified) kernels and only 2x the price of similar but low assurance kernels.

### Limitations

Like other formally verified systems, seL4's guarantees are relative to its specification and underlying assumptions. While this means verification does not address all possible faults, it still substantially improves overall system assurance by eliminating classes of implementation defects and making remaining assumptions explicit (and thus testable).

- seL4 is *only* a microkernel which full operating systems are built on top of. However, a case study of critical Linux kernel CVEs show that isolation of its unverified subsystems would have downgraded the severity of every CVE sampled that wasn't linked to the pre-boot environment.
- The proofs do not cover all aspects of a functioning computer running seL4 and do not extend to all supported platforms and configurations. The initial proofs (for example) only pertained to the C code base, but later work extended the proofs to compiled binaries (binary verification is *not* supported on all platforms).
- While seL4 can link their specifications against hardware specifications, there may be bugs in the specifications or the physical hardware. However, no bugs have been publicly reported in the verified portions of the kernel in over 15 years. While buggy hardware impacts *all* operating systems and seL4 does have mitigations for some known hardware bugs, the project currently does not have the resources to implement as many mitigations as more mature commercial operating systems. This is not, however, a fundamental limitation of seL4.

#### Verification and feature timeline / roadmap (selected milestones)

Verified (machine-checked proofs for specific configurations)

Feature complete (further verification not expected to break compatibility)

In progress

Research ongoing

| Date | Milestone / scope | Status | Notes |
|---|---|---|---|
| 29 July 2009 | Functional correctness proof of C code corresponds to abstract specification. | Verified | Single core and did not extend to the binary. |
| 2011–2012 | Sound worst-case execution time (WCET) analysis of seL4 kernel system calls and interrupt latency for specific, single-core Arm platforms. | Stable (analysed; higher level proofs later used to improve WCET bounds) | First such analysis performed on a memory protected system. Arm has since stopped specifying worst-case instruction latencies, but the work can be applied to future platforms. |
| 2012–present | Security enforcement proofs (integrity and information-flow confidentiality) and binary correctness extensions (later extended to Intel x64 and RISC-V 64) | Verified (support varies by platform) | Verifies that the binary produced by GCC at -O2 still enforces high level proofs without verifying/trusting the compiler. |
| 2014–2017 | High-assurance analysis techniques (loop bounds, infeasible paths, toolchain integration) extended from the higher level proofs, which further improves WCET of the binary. | Stable (analysed; research-level assurance) |   |
| 19 Nov 2019 | Mixed-Criticality Systems (MCS:temporal isolation / scheduling contexts) integrated into mainline. | Stable (unverified) |   |
| 2019–present | Timing side channels / "time protection" mechanisms evaluated; formalisation and verification work ongoing. | In progress | Will require hardware support. |
| 2024–present | Multicore: verified "static multikernel" roadmap and concurrency verification framework (incremental assurance approach) | In progress |   |
| Q3 2027 | MCS: C-level functional correctness verification scheduled to complete. | Planned |   |

*Note:* The verification status of seL4 varies by architecture and configuration; the seL4 documentation provides a matrix of which properties are covered per configuration (e.g., functional correctness, integrity/availability, confidentiality, and binary correctness coverage).

## Ecosystem

seL4 is commonly used as the kernel foundation for componentised embedded systems, and the seL4 Foundation supports a set of associated tools and frameworks. Ecosystem artefacts (including code, tools and proofs) are generally provided under permissive licenses (BSD).

### Microkit

The seL4 Microkit is an operating-system framework built on top of seL4 that provides a small set of abstractions aimed at lowering the barrier to building statically structured systems while preserving performance and memory efficiency goals.

### Device Driver Framework (sDDF)

The seL4 Device Driver Framework (sDDF) is a driver architecture for seL4-based systems discussed in multiple summits; summit materials describe a design emphasizing separation of concerns and event-based/asynchronous communication with shared-memory data paths.

### LionsOS

LionsOS is under current development by the Trustworthy Systems at University of New South Wales (UNSW) and aims to provide application-oriented OS services, such as networking, file systems and other I/O. While primarily aimed at static architectures were resources that are allocated at boot time (ex embedded), support for more dynamic operating systems are planned.

Primary objectives of LionsOS are to compete with Linux by using seL4 microkernel that keeps system performance while also providing correct implementation of the sel4 hardware by using Satisfiability Modulo Theories (SMT) verification tools. Main building blocks of the proposed system are the seL4 microkit and seL4 device driver framework (sDDF). Currently 0.3.0 version is released on 25 March 2025.

## Governance and community

The seL4 Foundation coordinates aspects of project governance and promotes a vendor-neutral ecosystem. It was initially launched under the umbrella of the Linux Foundation to support broader adoption and long-term vendor-neutral stewardship of seL4 technology. It has since transitioned to its own independent organization. The choice of the GPL for licensing was made to encourage reciprocity of commercial investments and discourage forking. The annual seL4 Summit is a primary venue for presenting ecosystem development, research directions, experience reports, and industry-oriented sessions to foster commercial investment in seL4.
