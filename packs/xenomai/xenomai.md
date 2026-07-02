---
title: "Xenomai"
source: https://en.wikipedia.org/wiki/Xenomai
domain: xenomai
license: CC-BY-SA-4.0
tags: xenomai cobalt, dual-kernel real-time, adeos pipeline, rtai co-kernel
fetched: 2026-07-02
---

# Xenomai

**Xenomai** is a software framework cooperating with the Linux kernel to provide interface-agnostic, hard real-time computing support to user space application software seamlessly integrated into the Linux environment.

The Xenomai project was launched in August 2001. In 2003, it merged with the Real-Time Application Interface (RTAI) project to produce RTAI/fusion, a real-time free software platform for Linux on Xenomai's abstract real-time operating system (RTOS) core. Eventually, the RTAI/fusion effort became independent from RTAI in 2005 as the Xenomai project.

Xenomai is based on an abstract RTOS core, usable for building any kind of real-time interface, over a nucleus which exports a set of generic RTOS services. Any number of RTOS personalities called “skins” can then be built over the nucleus, providing their own specific interface to the applications, by using the services of a single generic core to implement it.

## Xenomai vs. RTAI

Many differences exist between Xenomai and RTAI, though both projects share a few ideas and support the RTDM (Real Time Data Monitoring) layer. The major differences derive from the goals the projects aim for, and from their respective implementation. While RTAI is focused on lowest technically feasible latencies, Xenomai also considers clean extensibility (RTOS skins), portability, and maintainability as very important goals. Xenomai's path towards Ingo Molnár's PREEMPT_RT support is another major difference compared to RTAI's objectives.
