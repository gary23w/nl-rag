---
title: "ARINC 653"
source: https://en.wikipedia.org/wiki/ARINC_653
domain: arinc-653
license: CC-BY-SA-4.0
tags: arinc 653, integrated modular avionics, time and space partitioning, apex interface
fetched: 2026-07-02
---

# ARINC 653

**ARINC 653** (Avionics Application Software Standard Interface) is a software specification for space and time partitioning in safety-critical avionics real-time operating systems (RTOS). It allows the hosting of multiple applications of different software levels on the same hardware in the context of an integrated modular avionics architecture.

It is part of ARINC 600-Series Standards for Digital Aircraft & Flight Simulators.

## Overview

In order to decouple the real-time operating system platform from the application software, ARINC 653 defines an API called APplication EXecutive (APEX).

Each application software is called a **partition** and has its own memory space. It also has a dedicated time slot allocated by the APEX API. Within each partition, multitasking is allowed. The APEX API provides services to manage partitions, processes and timing, as well as partition/process communication and error handling. The partitioning environment can be implemented by using a hypervisor to map partitions to virtual machines, but this is not required.

The standard is overseen by the AEEC APEX Subcommittee, which is co-chaired by representatives from Airbus and Boeing. Gordon Putsche was the Boeing chair from 2002 until 2023. Steven H. VanderLeest is the current Boeing chair. Pierre Gabrilot is the current Airbus chair.

## History

### Initial version

The initial version of ARINC 653 was published on October 10, 1996.

### ARINC 653-1

Supplement 1 was published in January 1997 and introduced the concepts of APEX and Time and Space partitioning.

### ARINC 653-2

Supplement 2 was published in 3 parts between March 2006 and January 2007:

- Part 1 (mandatory services): ARINC 653 partition management, Cold start and warm start definition, Application software error handling, ARINC 653 compliance, Ada and C language bindings;
- Part 2 (optional services): File system access, Data logging, Service Access points, ...
- Part 3 (Conformity Test Specification);

### Current Organization of Standard

- Part 0 - Introduction to ARINC 653 (currently at revision 3, released November 2021)

- Part 1 - Required Services (currently at supplement 6, released December 2024)
- Part 2 - Extended Services (currently at supplement 5, released December 2024)
- Part 3A - Conformity Test Specification for Required Services (currently at revision 2, released November 2021)
- Part 3B - Conformity Test Specification for Extended Services (currently at revision c1, released July 2019)
- Part 4 - Subset Services (currently at revision 0, released June 2012)
- Part 5 - Core Software Recommended Capabilities (currently at revision 1, released August 2019)

## Basic principles of partitioning

### ARINC 653 Platform

An ARINC 653 platform contains:

- A hardware platform allowing real-time computing deterministic services.
- An abstraction layer managing the timer and space partitioning constraints of the platform (memory, CPU, Input/output).
- An implementation for the ARINC 653 services (the APEX API).
- An interface to be able to configure the platform and its domain of use.
- Various instrumentation tools.

### Initialization

Initialization of an ARINC 653 partition creates resources used by the partition. Resources creation (PROCESS, EVENT, SEMAPHORE...) is performed by calling API services named **CREATE_xxxx**.

### Error handling

The process error handler is a preemptive process of the highest priority dedicated to handle partition exceptions. It is created by the service **CREATE_ERROR_HANDLER** during partition initialization.

The API allows the error handler to stop a faulty process (**STOP_SELF**). In that case, the RTOS scheduler will elicit the next process with the highest priority.

ARINC 653 does not specify how the scheduler should behave if the error handler does not stop a faulty process. In some (theoretical) cases, this could lead to an infinite loop between the faulty process and the error handler.

The error handler can obtain information about the source and the context of the exception.

### Mode management

Each partition can be in several activation modes:

- COLD_START and WARM_START: Only the initialization process is executed,
- NORMAL: The initialization process is stopped, and the other partition processes are called by the RTOS scheduler depending on their priority,
- IDLE: No process is executed. However an implementation could still in theory execute a hidden process of the lowest priority, for example to start an infinite loop.

The **SET_PARTITION_MODE** service allows to manage these states. It can be called by any process in the partition. Entering the IDLE state is irreversible for the partition. Only an external event (such as a platform restart) can change the state to another mode when the partition is in this state.

### Partition and process scheduling

The standard defines a two-level hierarchical schedule. The first level schedules the partitions. This is a round-robin, fixed schedule that repeats a Major Time Frame. The Major Time Frame schedules each partition in a fixed duration Partition Time Window (sometimes called a Minor Time Frame) with a fixed Partition Time Window Offset from the start of the Major Time Frame.

During the Partition Time Window, the second level of scheduling uses process scheduling. Each partition has at least one process. Process scheduling within a partition during the Partition Time Window is preemptive. The scheduler is called either by a timer or by API services.

### Multicore

ARINC 653 P1-5 was updated to address multicore processor architectures. Section 4.2.1 "O/S Multicore Implementation Compliance" indicates that an OS designed for multi-core processing should support two cases:

- Use of multiple cores by a single partition (whose processes span multiple cores)
- Use of multiple cores by multiple partitions

The position paper CAST-32A defines a set of requirements and guidance that should be met to certify and use multi-core processors in civil aviation by FAA and is expected to be replaced by an Advisory Circular, AC 20-193. The European Union aviation authority, EASA, published AMC 20-193 in January 2022.

## API services

The ARINC 653 APEX services are API calls belonging in six categories:

- Partition management
- Process management
- Time management
- Inter-partition communication
- Intra-partition communication
- Error handling

No ARINC 653 services are provided for the memory management of partitions. Each partition has to handle its own memory (still under the constraints of memory partitioning enforced by ARINC 653).

Each service returns a RETURN_CODE value which indicates if the call has been successful:

- NO_ERROR: the service performed nominally after a valid request
- NO_ACTION: the state of the system has not changed after executing the service
- NOT_AVAILABLE: the service is temporarily unavailable
- INVALID_PARAM: at least one of the service's parameters is invalid
- INVALID_CONFIG: at least one of the service's parameters is incompatible with the current configuration of the system
- INVALID_MODE: the service is incompatible with the current mode of the system
- TIMED_OUT: the delay for the execution of the service has expired

## Links to POSIX and ASAAC

The field covered by ARINC 653 is similar to ASAAC *Def Stan 00-74*. However, there are differences between the two standards.

Some ARINC 653 (APEX) calls have a POSIX equivalent, but are different from how they are defined in POSIX.

For example, the following call defined in ASAAC:

```
 receiveBuffer
```

would be translated in ARINC 653 by:

```
 RECEIVE_BUFFER()
```

and also in POSIX by:

```
 recv()
```
