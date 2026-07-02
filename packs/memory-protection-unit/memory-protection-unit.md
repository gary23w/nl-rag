---
title: "Memory protection unit"
source: https://en.wikipedia.org/wiki/Memory_protection_unit
domain: memory-protection-unit
license: CC-BY-SA-4.0
tags: memory protection unit, mpu region, memory management unit, protection ring
fetched: 2026-07-02
---

# Memory protection unit

A **memory protection unit** (**MPU**) is a computer hardware unit that provides memory protection. It is usually implemented as part of the central processing unit (CPU). MPU is a trimmed down version of memory management unit (MMU) providing only memory protection support. It is usually implemented in low power processors that require only memory protection and do not need the full-fledged feature of a MMU like virtual memory management.

## Overview

The MPU allows the privileged software to define memory regions and assign memory access permission and memory attributes to each of them. Depending on the implementation of the processor, the number of supported memory regions will vary. The MPU on ARMv8-M processors supports up to 16 regions. The memory attributes define the ordering and merging behaviors of these regions, as well as caching and buffering attributes. Cache attributes can be used by internal caches, if available, and can be exported for use by system caches.

MPU monitors transactions, including instruction fetches and data accesses from the processor, which can trigger a fault exception when an access violation is detected. The main purpose of memory protection is to prevent a process from accessing memory that has not been allocated to it. This prevents a bug or malware within a process from affecting other processes, or the operating system itself.
