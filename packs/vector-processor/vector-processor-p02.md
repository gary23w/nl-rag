---
title: "Vector processor (part 2/2)"
source: https://en.wikipedia.org/wiki/Vector_processor
domain: vector-processor
license: CC-BY-SA-4.0
tags: vector processor, array processing hardware, cray supercomputer, parallel computing
fetched: 2026-07-02
part: 2/2
---

## Vector processor features

Where many SIMD ISAs borrow or are inspired by the list below, typical features that a vector processor will have are:

- **Vector Load and Store** – Vector architectures with a register-to-register design (analogous to load–store architectures for scalar processors) have instructions for transferring multiple elements between the memory and the vector registers. Typically, multiple addressing modes are supported.
  - The unit-stride addressing mode is essential: elements are contiguous.
  - modern vector architectures typically also support arbitrary constant strides (offsets)
  - modern architectures also have the scatter/gather (also called *indexed*) addressing modes.
  - Advanced architectures may also include support for *segment* load and stores,. Segment loads read a vector from memory, where each element is a data structure containing multiple members. The members are extracted from data structure (element), and each extracted member is placed into a different vector register.
  - Some advanced architectures have *fail-first* variants of the standard vector load and stores (explained below)
  - IBM 370 also had sparse Vector load/store which used a bitmask to specify, sequentially, which elements to Load / Store: in effect the Compress/Expand concept but Memory-register instead of (below) Register-register.
- **Masked Operations** – predicate masks allow parallel if/then/else constructs without resorting to branches. This allows code with conditional statements to be vectorized.
- **Compress and Expand** – usually using a bit-mask, data is linearly compressed or expanded (redistributed) based on whether bits in the mask are set or clear, whilst always preserving the sequential order and never duplicating values (unlike Gather-Scatter aka permute). These instructions feature in AVX-512.
- **Register Gather, Scatter (aka permute)** – a less restrictive more generic variation of the compress/expand theme which instead takes one vector to specify the indices to use to "reorder" another vector. Gather/scatter is more complex to implement than compress/expand, and, being inherently non-sequential, can interfere with vector chaining. Not to be confused with Gather-scatter Memory Load/Store modes, Gather/scatter vector operations act on the vector registers, and are often termed a permute instruction instead.
- **Splat and Extract** – useful for interaction between scalar and vector, these broadcast a single value across a vector, or extract one item from a vector, respectively.
- **Iota** – a very simple and strategically useful instruction which drops sequentially-incrementing immediates into successive elements. Usually starts from zero.
- **Reduction and Iteration** – operations that perform mapreduce on a vector (for example, find the one maximum value of an entire vector, or sum all elements). Iteration is of the form `x[i] = y[i] + x[i-1]` where Reduction is of the form `x = y[0] + y[1]… + y[n-1]`
- **Matrix Multiply support** – either by way of algorithmically loading data from memory, or reordering (remapping) the normally linear access to vector elements, or providing "Accumulators", arbitrary-sized matrices may be efficiently processed. IBM POWER10 provides MMA instructions although for arbitrary Matrix widths that do not fit the exact SIMD size data repetition techniques are needed which is wasteful of register file resources. NVidia provides a high-level Matrix CUDA API although the internal details are not available. The most resource-efficient technique is in-place reordering of access to otherwise linear vector data.
- **Advanced Math formats** – often includes Galois field arithmetic, but can include binary-coded decimal or decimal fixed-point, and support for much larger (arbitrary precision) arithmetic operations by supporting parallel carry-in and carry-out
- **Bit manipulation** – including vectorised versions of bit-level permutation operations, bitfield insert and extract, centrifuge operations, population count, and many others.

### GPU vector processing features

With many 3D shader applications needing trigonometric operations as well as short vectors for common operations (RGB, ARGB, XYZ, XYZW) support for the following is typically present in modern GPUs, in addition to those found in vector processors:

- **Sub-vectors** – elements may typically contain two, three or four sub-elements (vec2, vec3, vec4) where any given bit of a predicate mask applies to the whole vec2/3/4, not the elements in the sub-vector. Sub-vectors are also introduced in RISC-V RVV (termed "LMUL"). Subvectors are a critical integral part of the Vulkan SPIR-V spec.
- **Sub-vector swizzle** – aka "lane shuffling" which allows sub-vector inter-element computations without needing extra (costly, wasteful) instructions to move the sub-elements into the correct SIMD "lanes" and also saves predicate mask bits. Effectively an in-flight mini-permute of the sub-vector, this heavily features in 3D shader binaries (as high as 20% of all instructions) and is sufficiently important as to be part of the Vulkan SPIR-V spec. The Broadcom Videocore IV uses the "lane rotate" terminology where the rest of the industry uses the term "swizzle".
- **Transcendentals** – trigonometric operations such as sine, cosine and logarithm obviously feature much more predominantly in 3D than in many demanding HPC workloads. Of interest, however, is that speed is far more important than accuracy in 3D for GPUs, where computation of pixel coordinates simply do not require high precision. The Vulkan specification recognises this and sets surprisingly low accuracy requirements, so that GPU Hardware can reduce power usage. The concept of reducing accuracy where it is simply not needed is explored in the MIPS-3D extension.

### Fault (or fail) first

Introduced in ARM SVE2 and RISC-V RVV is the concept of speculative sequential vector loads. ARM SVE2 has a special register named "First Fault Register", where RVV modifies (truncates) the vector length (VL).

The basic principle of ffirst is to attempt a large sequential vector load, but to allow the hardware to arbitrarily truncate the *actual* amount loaded to either the amount that would succeed without raising a memory fault or simply to an amount (greater than zero) that is most convenient. The important factor is that *subsequent* instructions are notified or may determine exactly how many loads actually succeeded, using that quantity to only carry out work on the data that has actually been loaded.

Contrast this situation with SIMD, which is a fixed (inflexible) load width and fixed data processing width, unable to cope with loads that cross page boundaries, and even if they were they are unable to adapt to what actually succeeded, yet, paradoxically, if the SIMD program were to even attempt to find out in advance (in each inner loop, every time) what might optimally succeed, those instructions only serve to hinder performance because they would, by necessity, be part of the critical inner loop.

This begins to hint at the reason why ffirst is so innovative, and is best illustrated by memcpy or strcpy when implemented with standard 128-bit non-predicated non-ffirst SIMD. For IBM POWER9 the number of hand-optimised instructions to implement strncpy is in excess of 240. By contrast, the same strncpy routine in hand-optimised RVV assembler is a mere 22 instructions.

The above SIMD example could potentially fault and fail at the end of memory, due to attempts to read too many values: it could also cause significant numbers of page or misaligned faults by similarly crossing over boundaries. In contrast, by allowing the vector architecture the freedom to decide how many elements to load, the first part of a strncpy, if beginning initially on a sub-optimal memory boundary, may return just enough loads such that on *subsequent* iterations of the loop the batches of vectorised memory reads are optimally aligned with the underlying caches and virtual memory arrangements. Additionally, the hardware may choose to use the opportunity to end any given loop iteration's memory reads *exactly* on a page boundary (avoiding a costly second TLB lookup), with speculative execution preparing the next virtual memory page whilst data is still being processed in the current loop. All of this is determined by the hardware, not the program itself.


## Performance and speed up

Let ***r*** be the vector speed ratio and ***f*** be the vectorization ratio. If the time taken for the vector unit to add an array of 64 numbers is 10 times faster than its equivalent scalar counterpart, r = 10. Also, if the total number of operations in a program is 100, out of which only 10 are scalar (after vectorization), then f = 0.9, i.e., 90% of the work is done by the vector unit. It follows the achievable speed up of:

$r/[(1-f)*r+f]$

So, even if the performance of the vector unit is very high ( $r=\infty$ ) there is a speedup less than $1/(1-f)$ , which suggests that the ratio ***f*** is crucial to the performance. This ratio depends on the efficiency of the compilation like adjacency of the elements in memory.
