---
title: "Cooperative multitasking"
source: https://en.wikipedia.org/wiki/Cooperative_multitasking
domain: requestidlecallback
license: CC-BY-SA-4.0
tags: request idle callback, idle period scheduling, background task deadline, cooperative task chunking
fetched: 2026-07-02
---

# Cooperative multitasking

**Cooperative multitasking**, also known as **non-preemptive multitasking**, is a computer multitasking technique in which the operating system never initiates a context switch from a running process to another process. Instead, in order to run multiple applications concurrently, processes voluntarily yield control periodically or when idle or logically blocked. This type of multitasking is called *cooperative* because all programs must cooperate for the scheduling scheme to work.

In this scheme, the process scheduler of an operating system is known as a **cooperative scheduler** whose role is limited to starting the processes and letting them return control back to it voluntarily.

This is related to the asynchronous programming approach.

## Usage

Although it is rarely used as the primary scheduling mechanism in modern operating systems, it is widely used in memory-constrained embedded systems and in specific applications such as CICS or the JES2 subsystem. Cooperative multitasking was the primary scheduling scheme for 16-bit applications employed by Microsoft Windows before Windows 95 and Windows NT, and by the classic Mac OS. Windows 9x used non-preemptive multitasking for 16-bit legacy applications, and the PowerPC Versions of Mac OS X prior to Leopard used it for classic applications. NetWare, which is a network-oriented operating system, used cooperative multitasking up to NetWare 6.5. Cooperative multitasking is still used on RISC OS systems.

Cooperative multitasking is similar to async/await in languages, such as JavaScript or Python, that feature a single-threaded event-loop in their runtime. This contrasts with cooperative multitasking in that await cannot be invoked from a non-async function, but only an async function, which is a kind of coroutine.

Cooperative multitasking allows much simpler implementation of applications because their execution is never unexpectedly interrupted by the process scheduler; for example, various functions inside the application do not need to be reentrant.

## Problems

As a cooperatively multitasked system relies on each process regularly giving up time to other processes on the system, one poorly designed program can consume all of the CPU time for itself, either by performing extensive calculations or by busy waiting; both would cause the whole system to hang. In a server environment, this is a hazard that is often considered to make the entire environment unacceptably fragile, though as noted above, cooperative multitasking has been used frequently in server environments, including NetWare and CICS.

In contrast, preemptive multitasking interrupts applications and gives control to other processes outside the application's control.

The potential for system hang can be alleviated by using a watchdog timer, often implemented in hardware; this typically invokes a hardware reset.
