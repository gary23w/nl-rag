---
title: "Lockstep (computing)"
source: https://en.wikipedia.org/wiki/Lockstep_(computing)
domain: lockstep-cores
license: CC-BY-SA-4.0
tags: lockstep cores, dual-core lockstep, triple modular redundancy, dual modular redundancy
fetched: 2026-07-02
---

# Lockstep (computing)

**Lockstep** systems are fault-tolerant computer systems that run the same set of operations at the same time in parallel. The redundancy (duplication) allows error detection and error correction: the output from lockstep operations can be compared to determine if there has been a fault if there are at least two systems (dual modular redundancy DMR), and the error can be automatically corrected if there are at least three systems (triple modular redundancy TMR), via majority vote. The term "lockstep" originates from army usage, where it refers to synchronized walking, in which marchers walk as closely together as physically practical.

To run in lockstep, each system is set up to progress from one well-defined state to the next well-defined state. When a new set of inputs reaches the system, it processes them, generates new outputs and updates its state. This set of changes (new inputs, new outputs, new state) is considered to define that step, and must be treated as an atomic transaction; in other words, either all of it happens, or none of it happens, but not something in between. Sometimes a timeshift (delay) is set between systems, which increases the detection probability of errors induced by external influences (e.g. voltage spikes, ionizing radiation, or in situ reverse engineering).

## Lockstep memory

Some vendors, including Intel, use the term *lockstep memory* to describe a multi-channel memory layout in which cache lines are distributed between two memory channels, so one half of the cache line is stored in a DIMM on the first channel, while the second half goes to a DIMM on the second channel. By combining the single error correction and double error detection (SECDED) capabilities of two ECC-enabled DIMMs in a lockstep layout, their *single-device data correction* (SDDC) nature can be extended into *double-device data correction* (DDDC), providing protection against the failure of any single memory chip.

Downsides of the Intel's lockstep memory layout are the reduction of effectively usable amount of RAM (in case of a triple-channel memory layout, maximum amount of memory reduces to one third of the physically available maximum), and reduced performance of the memory subsystem.

## Dual modular redundancy

Where the computing systems are duplicated, but both actively process each step, it is difficult to arbitrate between them if their outputs differ at the end of a step. For this reason, it is common practice to run DMR systems as "master/slave" configurations with the slave as a "hot-standby" to the master, rather than in lockstep. Since there is no advantage in having the slave unit actively process each step, a common method of working is for the master to copy its state at the end of each step's processing to the slave. Should the master fail at some point, the slave is ready to continue from the previous known good step.

While either the lockstep or the DMR approach (when combined with some means of detecting errors in the master) can provide redundancy against hardware failure in the master, they do not protect against software error. If the master fails because of a software error, it is highly likely that the slave - in attempting to repeat the execution of the step which failed - will simply repeat the same error and fail in the same way, an example of a common mode failure.

## Triple modular redundancy

Where the computing systems are triplicated, it becomes possible to treat them as "voting" systems. If one unit's output disagrees with the other two, it is detected as having failed. The matched output from the other two is treated as correct.

## GPU Programming

Although the concept originated in fault-tolerant computing, NVIDIA later adopted the terminology to describe warp execution in GPU computing, defining it as the simultaneous execution of all threads within a warp. In the context of NVIDIA's CUDA programming model and SIMT (Single instruction, multiple threads) architecture, lockstep execution ensures that all threads in a warp execute the same kernel instruction at the same time.
