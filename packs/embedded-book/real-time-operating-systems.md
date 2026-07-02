---
title: "Embedded Systems/Real-Time Operating Systems"
source: https://en.wikibooks.org/wiki/Embedded_Systems/Real-Time_Operating_Systems
domain: embedded-book
license: CC-BY-SA-4.0 (Wikibooks Embedded Systems)
tags: embedded programming, interrupt service routine, embedded c
fetched: 2026-07-02
---

# Embedded Systems/Real-Time Operating Systems

<

Embedded Systems

|   | Wikipedia has related information at ***Real-time operating system***. |
|---|---|

A **Real-Time Operating System** (RTOS) is a computing environment that reacts to input within a specific time period. A real-time deadline can be so small that system reaction appears instantaneous. The term real-time computing has also been used, however, to describe "slow real-time" output that has a longer, but fixed, time limit.

Learning the difference between real-time and standard operating systems is as easy as imagining yourself in a computer game. Each of the actions you take in the game is like a program running in that environment. A game that has a real-time operating system for its environment can feel like an extension of your body because you can count on a specific "lag time:" the time between your request for action and the computer's noticeable execution of your request. A standard operating system, however, may feel disjointed because the lag time is unreliable. To achieve time reliability, real-time programs and their operating system environment must prioritize deadline actualization before anything else. In the gaming example, this might result in dropped frames or lower visual quality when reaction time and visual effects conflict.

## Methods

An operating system is considered real-time if it invariably enables its programs to perform tasks within specific time constraints, usually those expected by the user. To meet this definition, some or all of the following methods are employed:

- The RTOS performs few tasks, thus ensuring that the tasks will always be executed before the deadline
- The RTOS drops or reduces certain functions when they cannot be executed within the time constraints ("load shedding")
- The RTOS monitors input consistently and in a timely manner
- The RTOS monitors resources and can interrupt background processes as needed to ensure real-time execution
- The RTOS anticipates potential requests and frees enough of the system to allow timely reaction to the user's request
- The RTOS keeps track of how much of each resource (CPU time per timeslice, RAM, communications bandwidth, etc.) might possibly be used in the worst-case by the currently-running tasks, and refuses to accept a new task unless it "fits" in the remaining un-allocated resources.

Chapters in this section will discuss how an RTOS works, some general methods for working with an RTOS, and a few popular RTOSes. Finally, in some later chapters, we will discuss how to write your own RTOS

## Objectives

An RTOS must respond in a timely manner to changes, but that does not necessarily mean that an RTOS can handle a large throughput of data. In fact in an RTOS, small response times are valued much higher than computing power, or data speed. Sometimes an RTOS will even need to drop data to ensure that it meets its strict deadlines. In essence, that provides us with a perfect definition: **an RTOS is an operating system designed to meet strict deadlines.** Beyond that definition, there are few requirements as to what an RTOS must be, or what features it must have. Some RTOS implementations are very complete and very robust, while other implementations are very simple, and suited for only one particular purpose.

An RTOS may be either event-driven or time-sharing. An **event-driven RTOS** is a system that changes state only in response to an incoming event. A **time-sharing RTOS** is a system that changes state as a function of time.

## The Fundamentals

To most people, embedded systems are not recognizable as computers. Instead, they are hidden inside everyday objects that surround us and help us in our lives. Embedded systems typically do not interface with the outside world through familiar personal computer interface devices such as a mouse, keyboard and graphic user interface. Instead, they interface with the outside world through unusual interfaces such as sensors, actuators and specialized communication links. Real-time and embedded systems operate in constrained environments in which computer memory and processing power are limited. They often need to provide their services within strict time deadlines to their users and to the surrounding world. It is these memory, speed and timing constraints that dictate the use of real-time operating systems in embedded software.

## Real-Time Kernel

The heart of a real-time OS (and the heart of every OS, for that matter) is the **kernel**. A kernel is the central core of an operating system, and it takes care of all the OS jobs:

1. Booting
2. Task Scheduling
3. Standard Function Libraries

Now, we will talk about booting and bootloaders later, and we will also devote several chapters to task scheduling. So we should mention at least one thing about standard function libraries: In an embedded system, there is rarely enough memory (if any) to maintain a large function library. If functions are going to be included, they must be small, and important.

In an embedded system, frequently the kernel will boot the system, initialize the ports and the global data items. Then, it will start the scheduler and instantiate any hardware timers that need to be started. After all that, the Kernel basically gets dumped out of memory (except for the library functions, if any), and the scheduler will start running the child tasks.

## Basic Kernel Services

In the discussion below, we will focus on the "kernel" — the part of an operating system that provides the most basic services to application software running on a processor. The "kernel" of a real-time operating system ("RTOS") provides an "abstraction layer" that hides from application software the hardware details of the processor (or set of processors) upon which the application software will run.

## For further reading

|   | Wikipedia has related information at ***real-time operating system***. |
|---|---|

- Operating System Design
- RTEMS for Embedded Software Developers
- Embedded Control Systems Design/Operating systems
- Atmel AVR/Operating systems and task managers
- "Operating systems on the rise" by Jim Turley, *Embedded Systems Design* 2006-06-21. Survey results show that about 3/4 of all embedded system projects use some kind of an operating system. About 1/4 of all embedded system projects use no operating system at all (presumably using a Embedded Systems/Super Loop Architecture instead).

See Embedded Systems/Common RTOS for a list of common real-time operating systems.

Retrieved from "

https://en.wikibooks.org/w/index.php?title=Embedded_Systems/Real-Time_Operating_Systems&oldid=3828321

"
