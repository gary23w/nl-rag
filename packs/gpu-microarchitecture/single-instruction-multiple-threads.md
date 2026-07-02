---
title: "Single instruction, multiple threads"
source: https://en.wikipedia.org/wiki/Single_instruction,_multiple_threads
domain: gpu-microarchitecture
license: CC-BY-SA-4.0
tags: gpu microarchitecture, stream processing, single instruction multiple threads, shader cores
fetched: 2026-07-02
---

# Single instruction, multiple threads

**Single instruction, multiple threads** (**SIMT**) is an execution model used in parallel computing where a single central "control unit" broadcasts an instruction to multiple "processing units" for them to all *optionally* perform simultaneous synchronous and fully-independent parallel execution of that one instruction. Each PU has its own independent data and address registers, its own independent memory, but no PU in the array has a program counter. In Flynn's 1972 taxonomy this arrangement is a variation of SIMD termed an **array processor**.

The SIMT execution model has been implemented on several GPUs and is relevant for general-purpose computing on graphics processing units (GPGPU), e.g. some supercomputers combine CPUs with GPUs: in the ILLIAC IV that CPU was a Burroughs B6500.

The SIMT execution model is still only a way to present to the programmer what is fundamentally still a predicated SIMD concept. Programs must be designed with predicated SIMD in mind. With instruction issue (as a synchronous broadcast) being handled by the single control unit, SIMT cannot *by design* allow threads (PEs, lanes) to diverge by branching, because only the control unit has a program counter. If possible, therefore, branching is to be avoided.

## Differences from other models

The simplest way to understand SIMT is to imagine a multi-core (MIMD) system, where each core has its own register file, its own ALUs (both SIMD and scalar) and its own data cache, but that unlike a standard multi-core system which has multiple independent instruction caches and decoders, as well as multiple independent program counter registers, the instructions are synchronously **broadcast** to all SIMT cores from a **single** unit with a single instruction cache and a single instruction decoder which reads instructions using a single program counter.

The key difference between SIMT and SIMD lanes is that each of the processing units in the SIMT array have their own local memory, and may have a completely different stack pointer (and thus perform computations on completely different data sets), whereas the ALUs in SIMD lanes know nothing about memory per se, and have no register file. This is illustrated by the ILLIAC IV. Each SIMT core was termed a processing element (PE), and each PE had its own separate memory (PEM). Each PE had an "index register" which was an address into its PEM. In the ILLIAC IV the Burroughs B6500 primarily handled I/O, but also sent instructions to the control unit (CU), which would then handle the broadcasting to the PEs. Additionally, the B6500, in its role as an I/O processor, had access to *all* PEMs.

Additionally, each PE may be made active or inactive. If a given PE is inactive it will not execute the instruction broadcast to it by the control unit: instead it will sit idle until activated. Each PE can be said to be predicated.

Also important to note is the difference between SIMT and SPMD - single program multiple data. SPMD, like standard multi-core systems, has multiple program counters, where SIMT only has one: in the (one) control unit.

## History

In Flynn's taxonomy, Flynn's original papers cite two historic examples of SIMT processors termed "Array Processors": the SOLOMON and ILLIAC IV. SIMT was introduced by NVIDIA in the Tesla GPU microarchitecture with the G80 chip. ATI Technologies, now AMD, released a competing product slightly later on May 14, 2007, the TeraScale 1-based *"R600"* GPU chip.

## Description

SIMT processors execute multiple "threads" (or "work-items" or "sequence of SIMD lane operations"), in lock-step, under the control of a single central unit. The model shares common features with SIMD lanes.

The ILLIAC IV extensively documented its "branching" mechanism, the precursor to modern predicate masking.

As access time of all the widespread RAM types (e.g. DDR SDRAM, GDDR SDRAM, XDR DRAM, etc.) is still relatively high, creating an effect called the memory wall, engineers came up with the idea to hide the latency that inevitably comes with each memory access. As shown in the design of the ILLIAC IV, the individual PEs run at a slower clock rate than a standard CPU, but make up for the lack of clock rate by running massively more such PEs in parallel. The upshot is that each PE's slower speed is better matched to the speed of RAM. The strategy works due to GPU workloads being inherently parallel, and an example is tiled rendering.

SIMT is intended to limit instruction fetching overhead, i.e. the latency that comes with memory access, and is used in modern GPUs (such as those of NVIDIA and AMD) in combination with 'latency hiding' to enable high-performance execution despite considerable latency in memory-access operations. As with SIMD, another major benefit is the sharing of the control logic by many data lanes, leading to an increase in computational density. One block of control logic can manage N data lanes, instead of replicating the control logic N times.

A downside of SIMT execution is the fact that, as there is only one program counter, "predicate masking" is the only strategy to control per-PE execution, leading to poor utilization in complex algorithms.

## Terminology

| NVIDIA CUDA | OpenCL | Hennessy & Patterson |
|---|---|---|
| Thread | Work-item | Sequence of SIMD lane operations |
| Warp | Sub-group | Thread of SIMD instructions |
| Block | Work-group | Body of vectorized loop |
| Grid | NDRange | Vectorized loop |

NVIDIA GPUs have a concept of the thread group called as "warp" composed of 32 hardware threads executed in lock-step. The equivalent in AMD GPUs is "wavefront", although it is composed of 64 hardware threads. In OpenCL, it is called as "sub-group" for the abstract term of warp and wavefront. CUDA also has the warp shuffle instructions which make parallel data exchange in the thread group faster, and OpenCL allows a similar feature support by an extension cl_khr_subgroups.
