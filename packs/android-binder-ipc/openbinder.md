---
title: "OpenBinder"
source: https://en.wikipedia.org/wiki/OpenBinder
domain: android-binder-ipc
license: CC-BY-SA-4.0
tags: android binder, binder ipc, interface description language, remote procedure call
fetched: 2026-07-02
---

# OpenBinder

**OpenBinder** is a system for inter-process communication. It was developed at Be Inc. and then Palm, Inc. and was the basis for the Binder framework now used in the Android operating system developed by Google.

OpenBinder allows processes to present interfaces which may be called by other threads. Each process maintains a thread pool which may be used to service such requests. OpenBinder takes care of reference counting, recursion back into the original thread, and the inter-process communication itself. On the Linux version of OpenBinder, the communication is achieved using ioctls on a given file descriptor, communicating with a kernel driver.

The kernel-side component of the Linux version of OpenBinder was merged into the Linux kernel mainline in kernel version 3.19, which was released on February 8, 2015.
