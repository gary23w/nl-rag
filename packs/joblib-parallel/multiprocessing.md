---
title: "Multiprocessing"
source: https://en.wikipedia.org/wiki/Multiprocessing
domain: joblib-parallel
license: CC-BY-SA-4.0
tags: python joblib, joblib parallel, task parallelism python
fetched: 2026-07-02
---

# Multiprocessing

**Multiprocessing** (**MP**) is the use of two or more central processing units (CPUs) within one computer system. The term also refers to the ability of a system to support more than one processor or the ability to allocate tasks between them. Many variants of this basic theme exist, and the definition of multiprocessing can vary with context, mostly as a function of how a processor is defined (multi-core processors (multiple cores) on one die, multiple dies in one chip carrier (package), multiple packages in one computer case (system unit), etc.).

A **multiprocessor** is a computer system having two or more CPUs (processors: multiple processors) each sharing main memory and peripherals, to simultaneously process programs. A 2009 textbook defined multiprocessor system similarly, but noted that the processors may share "some or all of the system’s memory and I/O facilities"; it also gave **tightly coupled system** as a synonymous term.

At the operating system level, *multiprocessing* is sometimes used to refer to the execution of multiple concurrent processes in a system, with each process running on a separate CPU or core, in contrast to one process at any one instant. When used with this definition, multiprocessing is sometimes contrasted with multitasking, which may use only one processor but switch it in time slices between tasks (i.e., a time-sharing system). In contrast, multiprocessing means true parallel execution of multiple processes using more than one processor. Multiprocessing doesn't necessarily mean that one process or task uses more than one processor simultaneously; the term parallel processing is generally used to denote that practice. Other authors prefer to refer to the operating system techniques as multiprogramming and reserve the term *multiprocessing* for the hardware aspect of having more than one processor. The remainder of this article discusses multiprocessing only in this hardware sense.

In Flynn's taxonomy, multiprocessors as defined above are Multiple instruction, multiple data (MIMD) machines. As the term "multiprocessor" normally refers to tightly coupled systems in which all processors share memory, multiprocessors are not the entire class of MIMD machines, which also contains message passing multicomputer systems.

## Key topics

### Processor symmetry

In a **multiprocessing** system, all CPUs may be equal, or some may be reserved for special purposes. A combination of hardware and operating system software design considerations determine the symmetry (or lack thereof) in a given system. For example, hardware or software considerations may require that only one particular CPU respond to all hardware interrupts, whereas all other work in the system may be distributed equally among CPUs; or execution of kernel-mode code may be restricted to only one assigned CPU, whereas user-mode code may be executed in any combination of processors. Multiprocessing systems are often easier to design if such restrictions are imposed, but they tend to be less efficient than systems in which all CPUs are used.

Systems that treat all CPUs equally are called symmetric multiprocessing (SMP) systems. In systems where all CPUs are not equal, system resources may be divided in a number of ways, including asymmetric multiprocessing (ASMP), non-uniform memory access (NUMA) multiprocessing, and clustered multiprocessing.

#### Master/slave multiprocessor system

In a master/slave multiprocessor system, the master CPU is in control of the computer and the slave CPU(s) performs assigned tasks. The CPUs can be very different in speed and architecture. Some (or all) of the CPUs can share a common bus, each can also have a private bus (for private resources), or they may be isolated except for a common communications pathway. Likewise, the CPUs can share common RAM and/or have private RAM that the other processor(s) cannot access. The roles of master and slave can change from one CPU to another.

Two early examples of a mainframe computer master/slave multiprocessor are the Bull Gamma 60 and the Burroughs B5000.

An early example of a master/slave multiprocessor system of microprocessors is the Tandy/Radio Shack TRS-80 Model 16 desktop computer, released in February 1982. It ran the multi-user/multi-tasking Xenix operating system, Microsoft's version of Unix (named TRS-XENIX). The Model 16 has two microprocessors: an 8-bit Zilog Z80 CPU running at 4 MHz, and a 16-bit Motorola 68000 CPU running at 6 MHz. When the system is booted, the Z-80 is the master and the Xenix boot process initializes the slave 68000, and then transfers control to the 68000, whereupon the CPUs change roles and the Z-80 becomes a slave processor responsible for all input/output (I/O) operations including disk, communication, printer, and network, keyboard, and integrated monitor, while the operating system and applications run on the 68000 CPU. The Z-80 can be used to do other tasks.

The earlier TRS-80 Model II, released in 1979, is also a multiprocessor system as it has both a Z-80 CPU and an Intel 8021 microcontroller in the keyboard. The 8021 made the Model II the first desktop computer system with a separate detachable lightweight keyboard connected with by one thin flexible wire, and likely the first keyboard to use a dedicated microcontroller, both attributes copied years later by Apple and IBM.

### Instruction and data streams

In multiprocessing, the processors can be used to execute a single sequence of instructions in multiple contexts (single instruction, multiple data (SIMD), often used in vector processing), multiple sequences of instructions in a single context (multiple instruction, single data or MISD, used for redundancy in fail-safe systems and sometimes applied to describe pipelined processors or hyper-threading), or multiple sequences of instructions in multiple contexts (multiple instruction, multiple data or MIMD).

### Processor coupling

#### Tightly coupled multiprocessor system

Tightly coupled multiprocessor systems contain multiple CPUs that are connected at the bus level. These CPUs may have access to a central shared memory (SMP or uniform memory access (UMA)), or may participate in a memory hierarchy with both local and shared memory (SM) (NUMA). The IBM p690 Regatta is an example of a high end SMP system. Intel Xeon processors dominated the multiprocessor market for business PCs and were the only major x86 option until the release of AMD's Opteron range of processors in 2004. Both ranges of processors had their own onboard cache but provided access to shared memory; the Xeon processors via a common pipe and the Opteron processors via independent pathways to the system random-access memory (RAM).

Chip multiprocessors, also known as multi-core computing, involves more than one processor placed on one chip and can be viewed as the most extreme form of tightly coupled multiprocessing. Mainframe systems with multiple processors are often tightly coupled.

#### Loosely coupled multiprocessor system

Loosely coupled multiprocessor systems (often referred to as clusters) are based on multiple standalone relatively low processor count commodity computers interconnected via a high speed communication system (Gigabit Ethernet is common). A Linux Beowulf cluster is an example of a loosely coupled system.

Tightly coupled systems perform better and are physically smaller than loosely coupled systems, but have historically required greater initial investments and may depreciate rapidly; nodes in a loosely coupled system are usually inexpensive commodity computers and can be recycled as independent machines upon retirement from the cluster.

Power consumption is also a consideration. Tightly coupled systems tend to be much more energy-efficient than clusters. This is because a considerable reduction in power consumption can be realized by designing components to work together from the beginning in tightly coupled systems, whereas loosely coupled systems use components that were not necessarily intended specifically for use in such systems.

Loosely coupled systems have the ability to run different operating systems or OS versions on different systems.

## Disadvantages

Merging data from multiple threads or processes may incur significant overhead due to conflict resolution, data consistency, versioning, and synchronization.
