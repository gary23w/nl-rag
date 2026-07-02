---
title: "Capability-based addressing"
source: https://en.wikipedia.org/wiki/Capability-based_addressing
domain: hardware-memory-safety
license: CC-BY-SA-4.0
tags: hardware enforced memory safety, capability based addressing, fat pointer hardware, cheri capability model
fetched: 2026-07-02
---

# Capability-based addressing

In computer science, **capability-based addressing** is a scheme used by some computers to control access to memory as an efficient implementation of capability-based security. Under a capability-based addressing scheme, pointers are replaced by protected objects (named **capabilities**) which specify both a location in memory, along with access rights which define the set of operations which can be carried out on the memory location. Capabilities can only be created or modified through the use of privileged instructions which may be executed only by either the kernel or some other privileged process authorised to do so. Thus, a kernel can limit application code and other subsystems access to the minimum necessary portions of memory (and disable write access where appropriate), without the need to use separate address spaces and therefore require a context switch when an access occurs.

## Practical implementations

Two techniques are available for implementation:

- Require capabilities to be stored in a particular area of memory that cannot be written to by the process that will use them. For example, the Plessey System 250 required that all capabilities be stored in capability-list segments.
- Extend memory with an additional bit, writable only in supervisor mode, that indicates that a particular location is a capability. This is a generalization of the use of tag bits to protect segment descriptors in the Burroughs Large Systems, and it was used to protect capabilities in the IBM System/38.

### Capability addressing in the IBM System/38 and AS/400

The System/38 supported two types of object pointer – *authorized pointers*, and *unauthorized pointers*, the former was the platform's implementation of capability-based addressing. Both types of pointer could only be manipulated using privileged instructions, and differed by whether object authorizations (i.e. access rights) were encoded in the contents of the pointer. Unauthorized pointers did not encode object authorizations, and required the operating system to check the object's authorization separately to determine if access to the object was allowed. Authorized pointers encoded object authorizations, meaning that possession of the pointer implied access, and the operating system was not required to verify authorization separately. Authorized pointers were irrevocable by design - if the object's authorizations were altered, it would not alter the encoded authorizations in any authorized pointers which already existed.

Early versions of the OS/400 operating system for the AS/400 also supported authorized pointers, and by extension capability-based addressing. However, authorized pointers were removed in the V1R3 release of OS/400 as their irrevocable nature became seen as a security liability. All versions of OS/400 (later IBM i) since rely solely on unauthorized pointers which do not support capability-based addressing.

## Chronology of systems adopting capability-based addressing

- 1969: System 250 – Plessey Company
- 1970–77: CAP computer – University of Cambridge Computer Laboratory
- 1978: System/38 – IBM
- 1980: Flex machine – Royal Signals and Radar Establishment (RSRE) Malvern
- 1981: Intel iAPX 432 – Intel
- 2014: CHERI (adds capabilities to existing ISAs for safer programming, even in C and C++)
- 2020: CHEx86
- 2022: ARM Morello (AArch64 with CHERI capabilities)
