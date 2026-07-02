---
title: "RTAI"
source: https://en.wikipedia.org/wiki/RTAI
domain: xenomai
license: CC-BY-SA-4.0
tags: xenomai cobalt, dual-kernel real-time, adeos pipeline, rtai co-kernel
fetched: 2026-07-02
---

# RTAI

**Real-time application interface** (**RTAI**) is a real-time extension for the Linux kernel, which lets users write applications with strict timing constraints for Linux. Like Linux itself the RTAI software is a community effort. RTAI provides deterministic response to interrupts, POSIX-compliant and native RTAI real-time tasks. RTAI supports several architectures, including IA-32 (with and without FPU and TSC), x86-64, PowerPC, ARM (StrongARM and ARM7: clps711x-family, Cirrus Logic EP7xxx, CS89712, PXA25x), and MIPS.

RTAI consists mainly of two parts: an Adeos-based patch to the Linux kernel which introduces a hardware abstraction layer, and a broad variety of services which make lives of real-time programmers easier. RTAI versions over 3.0 use an Adeos kernel patch, slightly modified in the x86 architecture case, providing additional abstraction and much lessened dependencies on the "patched" operating system. Adeos is a kernel patch comprising an Interrupt Pipeline where different operating system domains register interrupt handlers. This way, RTAI can transparently take over interrupts while leaving the processing of all others to Linux. Use of Adeos also frees RTAI from patent restrictions caused by RTLinux project.

## RTAI-XML

RTAI-XML is a server component of RTAI, implementing a service-oriented way to design and develop real-time (RT) control applications.

This project was born to fulfill the needs of a university group, mainly focused to have a flexible platform for learning control systems design, allowing the students to test their programs remotely, over the Internet. The alpha version of RTAI-XML showed the potential impact of the basic idea of a net separation of *hard* and *soft* real-time tasks in the programmation logic.

RTAI-XML consists of a server component waiting for incoming calls on a box where a real-time process, the Target, is running (or ready to). A generic client program, the Host, can reach the server through the TCP/IP network, using a standard protocol based on XML, and hence interact with the Target, in order to monitor the status of the RT process, to see the signals collected (or generated) by the system and also to fetch and change the RT parameters (for example, the gains of a PID feedback ring). In other words, RTAI-XML provides a simple way towards remoting of control applications, adding flexibility to the RTAI project, without losing the key features of an open and standard implementation.

The RTAI-XML section of this site presents the details of the implementation. The general architecture is revised, in order to focus the three key components, the Server, the *Server-Target* interface and the *Server-Host* communication. The Applications section contains some examples of control systems based on RTAI-XML and the References section contains hints and links for further readings on this topic.
