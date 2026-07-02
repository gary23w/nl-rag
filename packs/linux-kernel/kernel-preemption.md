---
title: "Kernel preemption"
source: https://en.wikipedia.org/wiki/Kernel_preemption
domain: linux-kernel
license: CC-BY-SA-4.0
tags: linux kernel, loadable kernel module, monolithic kernel, kernel preemption
fetched: 2026-07-02
---

# Kernel preemption

In computer operating system design, **kernel preemption** is a property possessed by some kernels, in which the CPU can be interrupted in the middle of executing kernel code and assigned other tasks (from which it later returns to finish its kernel tasks).

## Details

Specifically, the scheduler is permitted to forcibly perform a context switch (on behalf of a runnable and higher-priority process) on a driver or other part of the kernel during its execution, rather than co-operatively waiting for the driver or kernel function (such as a system call) to complete its execution and return control of the processor to the scheduler when done. It is used mainly in monolithic and hybrid kernels, where all or most device drivers are run in kernel space. Linux is an example of a monolithic-kernel operating system with kernel preemption.

The main benefit of kernel preemption is that it solves two issues that would otherwise be problematic for monolithic kernels, in which the kernel consists of one large binary. Without kernel preemption, two major issues exist for monolithic and hybrid kernels:

- A device driver can enter an infinite loop or other unrecoverable state, crashing the whole system.
- Some drivers and system calls on monolithic kernels can be slow to execute, and cannot return control of the processor to the scheduler or other program until they complete execution.
