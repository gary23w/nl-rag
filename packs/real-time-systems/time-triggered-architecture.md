---
title: "Time-triggered architecture"
source: https://en.wikipedia.org/wiki/Time-triggered_architecture
domain: real-time-systems
license: CC-BY-SA-4.0
tags: real-time, rtos, scheduling, preemption, interrupt latency, hard real-time
fetched: 2026-07-02
---

# Time-triggered architecture

**Time-triggered architecture** (abbreviated as **TTA**), also known as a **time-triggered system**, is a computer system that executes one or more sets of tasks according to a predetermined and set task schedule. Implementation of a TT system will typically involve use of a single interrupt that is linked to the periodic overflow of a timer. This interrupt may drive a task scheduler (a restricted form of real-time operating system). The scheduler will‍—‌in turn‍—‌release the system tasks at predetermined points in time.

## History and development

Because they have highly deterministic timing behavior, TT systems have been used for many years to develop safety-critical aerospace and related systems.

An early text that sets forth the principles of time triggered architecture, communications, and sparse time approaches is *Real-Time Systems: Design Principles for Distributed Embedded Applications* in 1997.

Use of TT systems was popularized by the publication of *Patterns for Time-Triggered Embedded Systems* (PTTES) in 2001 and the related introductory book *Embedded C* in 2002. The PTTES book also introduced the concepts of time-triggered hybrid schedulers (an architecture for time-triggered systems that require task pre-emption) and shared-clock schedulers (an architecture for distributed time-triggered systems involving multiple, synchronized, nodes).

Since publication of PTTES, extensive research work on TT systems has been carried out.

## Current applications

Time-triggered systems are now commonly associated with international safety standards such as IEC 61508 (industrial systems), ISO 26262 (automotive systems), IEC 62304 (medical systems) and IEC 60730 (household goods).

## Alternatives

Time-triggered systems can be viewed as a subset of a more general event-triggered (ET) system architecture (see event-driven programming).

Implementation of an ET system will typically involve use of multiple interrupts, each associated with specific periodic events (such as timer overflows) or aperiodic events (such as the arrival of messages over a communication bus at random points in time). ET designs are traditionally associated with the use of what is known as a real-time operating system (or RTOS), though use of such a software platform is not a defining characteristic of an ET architecture.
