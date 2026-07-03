---
title: "ASCI Red"
source: https://en.wikipedia.org/wiki/ASCI_Red
domain: hitachi-sr2201
license: CC-BY-SA-4.0
tags: hitachi sr2201
fetched: 2026-07-03
---

# ASCI Red

**ASCI Red** (also known as **ASCI Option Red** or **TFLOPS**) was the first computer built under the Accelerated Strategic Computing Initiative (ASCI), the supercomputing initiative of the United States government created to help the maintenance of the United States nuclear arsenal after the 1992 moratorium on nuclear testing.

ASCI Red was built by Intel and installed at Sandia National Laboratories in late 1996. The design was based on the Intel Paragon computer. The original goals to deliver a true teraflop machine by the end of 1996 that would be capable of running an ASCI application using all memory and nodes by September 1997 were met. It was used by the US government from the years of 1997 to 2005 and was the world's fastest supercomputer until late 2000. It was the first ASCI machine that the Department of Energy acquired, and also the first supercomputer to score above one teraflops on the LINPACK benchmark, a test that measures a computer's calculation speed. Later upgrades to ASCI Red allowed it to perform above two teraflops.

ASCI Red earned a reputation for reliability that some veterans say has never been beaten. Sandia director Bill Camp said that ASCI Red had the best reliability of any supercomputer ever built, and “was supercomputing’s high-water mark in longevity, price, and performance.”

ASCI Red was decommissioned in 2006.

## System structure

The ASCI Red supercomputer was a distributed memory MIMD (Multiple Instruction, Multiple Data) message-passing computer. The design provided a high degree of scalability for I/O, memory, compute nodes, storage capacity, and communications; standard parallel interfaces also made it possible to port parallel applications to the machine. The machine was structured into four partitions: Compute, Service, I/O, and System. Parallel applications executed in the Compute Partition which contained nodes optimized for floating point performance. The compute nodes had only the features required for efficient computation – they were not purposed for general interactive services. The Service Partition provided an integrated, scalable host that supported interactive users (login sessions), application development, and system administration. The I/O Partition supported disk I/O, a scalable parallel file system and network services. The System Partition supported initial booting and system Reliability, Availability, and Serviceability (RAS) capabilities.

The Service partition helps integrate all of the different parts of ASCI Red together. It provides a scalable host for users, and it is used for general system administration. The I/O Partition provides a file system and network services, and the Service partition is made up of the log-in screens, tools for application development, and utilities for network connections. The Compute partition contains nodes that are designed for floating point performance. This is where the actual computing takes place. Every one of the compute nodes accommodated two 200 MHz Pentium Pro processors, each with a 16 KB level-1 cache and a 256 KB level-2 cache, which were upgraded later to two 333 MHz Pentium II OverDrive processors, each with a 32 KB level-1 cache and a 512 KB level-2 cache. According to Intel, the ASCI Red Computer is also the first large scale supercomputer to be built entirely of common commercially available components.

All of ASCI Red's partitions are interconnected to form one supercomputer, however at the same time none of the nodes support global shared memory. Each of the nodes works in its own memory, and each shares data with the others through "explicit message-passing".

## Technical specifications

The computer itself took up almost 1,600 square feet (150 m2) of space, and was made up of 104 "cabinets". Of those cabinets, 76 are computers (processors), 8 are switches, and 20 are disks. It had a total of 1212 GB of RAM, and 9298 separate processors. The original machine used Intel Pentium Pro processors each clocked at 200 MHz. These were later upgraded to specially packaged Pentium II Xeon processors, each clocked at 333 MHz. Overall, it required 850 kW of power (not including air conditioning). What sets ASCI Option Red aside from all of its predecessors in supercomputing is its high I/O bandwidth. Previous supercomputers had multi-GFLOPS performance, yet their slow I/O speeds would slow down, or bottleneck the systems. Intel's TFLOPS PFS is an extremely efficient "Parallel File System" that can sustain transfer speeds of up to 1 GB/s, eliminating bottlenecks.

## First to TFLOPS

In December, 1996, three quarters of ASCI Red was measured at a world record 1.06 TFLOPS on MP LINPACK and held the record for fastest supercomputer in the world for several consecutive years, maxing out at 2.38 TFLOPS after a processor and memory upgrade in 1999. The system used Pentium Pro processors when initially constructed and when it recorded performance above one TFLOPS. In that configuration, when fully built it recorded 1.6 TFLOPS of performance. Upgrades later in 1999, to specially packaged Pentium II Xeon processors, pushed performance to 3.1 TFLOPS.

## Operating system

The different partitions of ASCI Red run on different operating systems. For example, users of the computer work in an environment called "Teraflops OS", an operating system (once called Paragon OS) that was originally developed for the Intel Paragon XP/S Supercomputer. ASCI Red's Compute partition runs on an operating system named Cougar. Cougar is a Sandia Labs and University of New Mexico collaboration; it is a lightweight OS based on PUMA and SUNMOS, two systems that were also designed for use on the Paragon supercomputer. It consists of a lightweight kernel, the Process Control Thread, and other utilities and libraries. The Linux 2.4 kernel was ported to the system and a custom CNIC driver was written, but the heavy weight OS did not perform as well as the Cougar lightweight kernel on many benchmarks.
