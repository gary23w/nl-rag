---
title: "OpenCL (part 2/2)"
source: https://en.wikipedia.org/wiki/OpenCL
domain: compute-shaders
license: CC-BY-SA-4.0
tags: compute shader, gpgpu compute, opencl kernel, cuda kernel
fetched: 2026-07-02
part: 2/2
---

## Portability, performance and alternatives

A key feature of OpenCL is portability, via its abstracted memory and execution model, and the programmer is not able to directly use hardware-specific technologies such as inline Parallel Thread Execution (PTX) for Nvidia GPUs unless they are willing to give up direct portability on other platforms. It is possible to run any OpenCL kernel on any conformant implementation.

However, performance of the kernel is not necessarily portable across platforms. Existing implementations have been shown to be competitive when kernel code is properly tuned, though, and auto-tuning has been suggested as a solution to the performance portability problem, yielding "acceptable levels of performance" in experimental linear algebra kernels. Portability of an entire application containing multiple kernels with differing behaviors was also studied, and shows that portability only required limited tradeoffs.

A study at Delft University from 2011 that compared CUDA programs and their straightforward translation into OpenCL C found CUDA to outperform OpenCL by at most 30% on the Nvidia implementation. The researchers noted that their comparison could be made fairer by applying manual optimizations to the OpenCL programs, in which case there was "no reason for OpenCL to obtain worse performance than CUDA". The performance differences could mostly be attributed to differences in the programming model (especially the memory model) and to NVIDIA's compiler optimizations for CUDA compared to those for OpenCL.

Another study at D-Wave Systems Inc. found that "The OpenCL kernel’s performance is between about 13% and 63% slower, and the end-to-end time is between about 16% and 67% slower" than CUDA's performance.

The fact that OpenCL allows workloads to be shared by CPU and GPU, executing the same programs, means that programmers can exploit both by dividing work among the devices. This leads to the problem of deciding how to partition the work, because the relative speeds of operations differ among the devices. Machine learning has been suggested to solve this problem: Grewe and O'Boyle describe a system of support-vector machines trained on compile-time features of program that can decide the device partitioning problem statically, without actually running the programs to measure their performance.

In a comparison of actual graphic cards of AMD RDNA 2 and Nvidia RTX Series there is an undecided result by OpenCL-Tests. Possible performance increases from the use of Nvidia CUDA or OptiX were not tested.
