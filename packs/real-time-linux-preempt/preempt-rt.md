---
title: "PREEMPT_RT"
source: https://en.wikipedia.org/wiki/PREEMPT_RT
domain: real-time-linux-preempt
license: CC-BY-SA-4.0
tags: preempt rt patch, real-time linux, kernel preemption, interrupt latency bound
fetched: 2026-07-02
---

# PREEMPT_RT

**PREEMPT_RT** is a feature of the Linux kernel which implements both hard and soft real-time computing capabilities. It was formerly maintained as a set of out-of-tree patches. On September 20, 2024, PREEMPT_RT was fully merged and enabled in mainline Linux on the supported architectures x86, x86_64, RISC-V and ARM64. This made kernel v6.12 the first release to include baked-in real-time capability.

## History

The PREEMPT_RT patchset has been in development since 2005 as an effort to make the Linux kernel capable of real-time computing by reducing unbounded latencies in kernel paths. Early real-time enhancements were proposed by Ingo Molnár, Thomas Gleixner, and others. The PREEMPT_RT patch series introduced features such as threaded interrupts, priority-inherited mutexes, and other mechanisms required for deterministic kernel behavior.

For many years PREEMPT_RT was maintained as an out-of-tree patch set applied to stable kernel releases. To support the funding of the ongoing development OSADL, a German software organization with members from PREEMPT_RTs user but also its creators like Gleixners Linutronix, has a working group. While parts of the PREEMPT_RT work were incrementally merged, the majority of the patch set remained external to mainline Linux for decades.

In 2015, the Linux Foundation established the Real-Time Linux (RTL) Collaborative Project to coordinate efforts toward upstreaming PREEMPT_RT and to provide sustained development resources. The project brought together long term industry members and maintainers to focus on refactoring kernel subsystems and pushing critical real-time code into the mainline.

In 2021, the preemption core locking code was merged.

At the September 2024 European Open Source Summit, Linus Torvalds announced that PREEMPT_RT had been accepted into the mainline Linux kernel after a protracted development hurdle involving the `printk` kernel logging facility.

## Usage

PREEMPT-RT is actively used at the moment by distributors and vendors to enhance their own distributions.

MontaVista Software has been releasing a real-time Linux distribution containing the PREEMPT_RT patchset since the early 2000. Montavista's current main embedded Linux product, CGX, contains real-time preemption as a standard feature.

Since February 2023, Canonical sold real-time versions of Ubuntu Pro., even though no notable contributions were made to the development by them.
