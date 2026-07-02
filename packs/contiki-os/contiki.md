---
title: "Contiki"
source: https://en.wikipedia.org/wiki/Contiki
domain: contiki-os
license: CC-BY-SA-4.0
tags: contiki os, contiki ng, protothread model, micro ip stack
fetched: 2026-07-02
---

# Contiki

**Contiki** is an operating system for networked, memory-constrained systems with a focus on low-power wireless Internet of Things (IoT) devices. Contiki is used for systems for street lighting, sound monitoring for smart cities, radiation monitoring and alarms. It is open-source software released under the BSD-3-Clause license.

Contiki was created by Adam Dunkels in 2002 and has been further developed by a worldwide team of developers from Texas Instruments, Atmel, Cisco, ENEA, ETH Zurich, Redwire, RWTH Aachen University, Oxford University, SAP, Sensinode, Swedish Institute of Computer Science, ST Microelectronics, Zolertia, and many others. Contiki gained popularity because of its built-in TCP/IP stack and lightweight preemptive scheduling over event-driven kernel. The name *Contiki* comes from Thor Heyerdahl's famous Kon-Tiki raft.

Contiki provides multitasking and a built-in Internet Protocol Suite (TCP/IP stack); it needs about 10 kilobytes of random-access memory (RAM) and 30 kilobytes of read-only memory (ROM). A full system, including a graphical user interface, needs about 30 kilobytes of RAM.

A new branch has recently been created, known as Contiki-NG: The OS for Next Generation IoT Devices.

## Hardware

Contiki is designed to run on types of hardware devices that are severely constrained in memory, power, processing power, and communication bandwidth. A typical Contiki system has memory on the order of kilobytes, a power budget on the order of milliwatts, processing speed measured in megaHertz, and communication bandwidth on the order of hundreds of kilobits/second. Such systems include many types of embedded systems, and old 8-bit computers.

## Networking

Contiki provides three network mechanisms: the uIP TCP/IP stack, which provides IPv4 networking, the uIPv6 stack, which provides IPv6 networking, and the Rime stack, which is a set of custom lightweight networking protocols designed for low-power wireless networks. The IPv6 stack was contributed by Cisco and was, when released, the smallest IPv6 stack to receive the *IPv6 Ready* certification. The IPv6 stack also contains the *Routing Protocol for Low power and Lossy Networks* (RPL) routing protocol for low-power lossy IPv6 networks and the 6LoWPAN header compression and adaptation layer for IEEE 802.15.4 links.

Rime is an alternative network stack, for use when the overhead of the IPv4 or IPv6 stacks is prohibitive. The Rime stack provides a set of communication primitives for low-power wireless systems. The default primitives are single-hop unicast, single-hop broadcast, multi-hop unicast, network flooding, and address-free data collection. The primitives can be used on their own or combined to form more complex protocols and mechanisms.

## Low-power operation

Many Contiki systems are severely power-constrained. Battery-operated wireless sensors may need to provide years of unattended operation and with little means to recharge or replace batteries. Contiki provides a set of mechanisms to reduce the power consumption of systems on which it runs. The default mechanism for attaining low-power operation of the radio is called ContikiMAC. With ContikiMAC, nodes can be running in low-power mode and still be able to receive and relay radio messages.

## Simulation

The Contiki system includes a sensor simulator called Cooja, which simulates Contiki nodes. The nodes belong to one of the three following classes: a) emulated Cooja nodes, b) Contiki code compiled and executed on the simulation host, or c) Java nodes, where the behavior of the node must be reimplemented as a Java class. One Cooja simulation may contain a mix of sensor nodes from any of the three classes. Emulated nodes can also be used to include non-Contiki nodes in a simulated network.

In Contiki 2.6, platforms with the TI MSP430 and Atmel AVR microcontrollers can be emulated.

## Programming model

To run efficiently on small-memory systems, the Contiki programming model is based on protothreads. A protothread is a memory-efficient programming abstraction that shares features of both multithreading and event-driven programming to attain a low memory overhead of each protothread. The kernel invokes the protothread of a process in response to an internal or external event. Examples of internal events are timers that fire or messages being posted from other processes. Examples of external events are sensors that trigger or incoming packets from a radio neighbor.

Protothreads are cooperatively scheduled. Thus, a Contiki process must always explicitly yield control back to the kernel at regular intervals. Contiki processes may use a special protothread construct to block waiting for events while yielding control to the kernel between each event invocation.

## Features

Contiki supports per-process optional preemptive multithreading, inter-process communication using message passing through events, as well as an optional graphical user interface (GUI) subsystem with either direct graphic support for locally connected terminals or networked virtual display with Virtual Network Computing (VNC) or over Telnet.

A full installation of Contiki includes the following features:

- Multitasking kernel
- Optional per-application preemptive multithreading
- Protothreads
- Internet Protocol Suite (TCP/IP) networking, including IPv6
- Windowing system and GUI
- Networked remote display using Virtual Network Computing
- A web browser (claimed to be the world's smallest)
- Personal web server
- Simple telnet client
- Screensaver

Contiki is supported by popular SSL/TLS libraries such as wolfSSL, which includes a port in its 3.15.5 release.

## Ports

### Microcontrollers

- Atmel – ARM, AVR
- NXP Semiconductors – LPC1768, LPC2103, MC13224
- Microchip – dsPIC, PIC32 (PIC32MX795F512L)
- Texas Instruments – MSP430, CC2430, CC2538, CC2630, CC2650, CC2538: cctv, Firefly, Zoul (comprises the CC2538 and CC1200 in a single module format)
- STMicroelectronics – STM32 W

### Computers

- Apple II
- Atari 8-bit computers
- Atari ST
- Atari Portfolio
- Pocket Viewer
- Commodore PET
- VIC-20,
- Commodore 64, Commodore 128
- Oric
- NEC PC-6001
- Sharp Wizard
- x86-based Unix-like systems, atop GTK+, or more directly using an X Window System

### Game consoles

- GP32
- Game Boy
- Game Boy Advance
- Jaguar
- Nintendo Entertainment System
- TurboGrafx-16
