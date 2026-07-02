---
title: "Hardware acceleration"
source: https://en.wikipedia.org/wiki/Hardware_acceleration
domain: hardware-accelerator-design
license: CC-BY-SA-4.0
tags: hardware accelerator design, coprocessor architecture, fpga acceleration, digital signal processor
fetched: 2026-07-02
---

# Hardware acceleration

**Hardware acceleration** is the use of computer hardware, known as a **hardware accelerator**, to perform specific functions faster than can be done by software running on a general-purpose central processing unit (CPU). Any transformation of data that can be calculated by software running on a CPU can also be calculated by an appropriate hardware accelerator, or by a combination of both.

To perform computing tasks more efficiently, generally one can invest time and money in improving the software, improving the hardware, or both. There are various approaches with advantages and disadvantages in terms of decreased latency, increased throughput, and reduced energy consumption.

Typical advantages of focusing on software may include greater versatility, more rapid development, lower non-recurring engineering costs, heightened portability, and ease of updating features or patching bugs, at the cost of overhead to compute general operations.

Advantages of focusing on hardware may include speedup, reduced power consumption, lower latency, increased parallelism and bandwidth, and better utilization of area and functional components available on an integrated circuit; at the cost of lower ability to update designs once etched onto silicon and higher costs of functional verification, times to market, and the need for more parts.

In the hierarchy of digital computing systems ranging from general-purpose processors to fully customized hardware, there is a tradeoff between flexibility and efficiency, with efficiency increasing by orders of magnitude when any given application is implemented higher up that hierarchy (that is, towards the more customized end). This hierarchy includes general-purpose processors such as CPUs, more specialized processors such as programmable shaders in a GPU, applications implemented on field-programmable gate arrays (FPGAs), and fixed-function implemented on application-specific integrated circuits (ASICs).

Hardware acceleration is advantageous for performance, and practical when the functions are fixed, so updates are not as needed as in software solutions. With the advent of reprogrammable logic devices such as FPGAs, the restriction of hardware acceleration to fully fixed algorithms has eased since 2010, allowing hardware acceleration to be applied to problem domains requiring modification to algorithms and processing control flow. The disadvantage, however, is that in many open source projects, it requires proprietary libraries that not all vendors are keen to distribute or expose, making it difficult to integrate in such projects.

## Overview

Integrated circuits are designed to handle various operations on both analog and digital signals. In computing, digital signals are the most common and are typically represented as binary numbers. Computer hardware and software use this binary representation to perform computations. This is done by processing Boolean functions on the binary input, and then outputting the results for storage or further processing by other devices.

### Computational equivalence of hardware and software

Because all Turing machines can run any computable function, it is always possible to design custom hardware that performs the same function as a given piece of software. Conversely, software can always be used to emulate the function of a given piece of hardware. Custom hardware may offer higher performance per watt for the same functions that can be specified in software. Hardware description languages (HDLs) such as Verilog and VHDL can model the same semantics as software and synthesize the design into a netlist that can be programmed to an FPGA or composed into the logic gates of an ASIC.

### Stored-program computers

The vast majority of software-based computing occurs on machines implementing the von Neumann architecture, collectively known as stored-program computers. Computer programs are stored as data and executed by processors. Such processors must fetch and decode instructions, as well as load data operands from memory (as part of the instruction cycle), to execute the instructions constituting the software program. Relying on a common cache for code and data leads to the "von Neumann bottleneck", a fundamental limitation on the throughput of software on processors implementing the von Neumann architecture. Even in the modified Harvard architecture, where instructions and data have separate caches in the memory hierarchy, there is overhead to decoding instruction opcodes and multiplexing available execution units on a microprocessor or microcontroller, leading to low circuit utilization. Modern processors that provide simultaneous multithreading exploit under-utilization of available processor functional units and instruction level parallelism between different hardware threads.

### Hardware execution units

Hardware execution units do not in general rely on the von Neumann or modified Harvard architectures and do not need to perform the instruction fetch and decode steps of an instruction cycle and incur those stages' overhead. If needed calculations are specified in a register transfer level (RTL) hardware design, the time and circuit area costs that would be incurred by instruction fetch and decoding stages can be reclaimed and put to other uses.

This reclamation saves time, power, and circuit area in computation. The reclaimed resources can be used for increased parallel computation, other functions, communication, or memory, as well as increased input/output capabilities. This comes at the cost of general-purpose utility.

### Emerging hardware architectures

Greater RTL customization of hardware designs allows emerging architectures such as in-memory computing, transport triggered architectures (TTA) and networks-on-chip (NoC) to further benefit from increased locality of data to execution context, thereby reducing computing and communication latency between modules and functional units.

Custom hardware is limited in parallel processing capability only by the area and logic blocks available on the integrated circuit die. Therefore, hardware is much freer to offer massive parallelism than software on general-purpose processors, offering a possibility of implementing the parallel random-access machine (PRAM) model.

It is common to build multicore and manycore processing units out of microprocessor IP core schematics on a single FPGA or ASIC. Similarly, specialized functional units can be composed in parallel, as in digital signal processing, without being embedded in a processor IP core. Therefore, hardware acceleration is often employed for repetitive, fixed tasks involving little conditional branching, especially on large amounts of data. This is how Nvidia's CUDA line of GPUs are implemented.

### Implementation metrics

As device mobility has increased, new metrics have been developed that measure the relative performance of specific acceleration protocols, considering characteristics such as physical hardware dimensions, power consumption, and operations throughput. These can be summarized into three categories: task efficiency, implementation efficiency, and flexibility. Appropriate metrics consider the area of the hardware along with both the corresponding operations throughput and energy consumed.

## Applications

Examples of hardware acceleration include bit blit acceleration functionality in graphics processing units (GPUs), use of memristors for accelerating neural networks, and regular expression hardware acceleration for spam control in the server industry, intended to prevent regular expression denial of service (ReDoS) attacks. The hardware that performs the acceleration may be part of a general-purpose CPU, or a separate unit called a hardware accelerator, though they are usually referred to with a more specific term, such as 3D accelerator, or cryptographic accelerator.

Traditionally, processors were sequential (instructions are executed one by one), and were designed to run general-purpose algorithms controlled by instruction fetch (for example, moving temporary results to and from a register file). Hardware accelerators improve the execution of a specific algorithm by allowing greater concurrency, having specific datapaths for their temporary variables, and reducing the overhead of instruction control in the fetch-decode-execute cycle.

Modern processors are multi-core and often feature parallel "single-instruction; multiple data" (SIMD) units. Such units can be integrated withint the CPU or offered by additional components as the AMD AI engines. Even so, hardware acceleration still yields benefits. Hardware acceleration is suitable for any computation-intensive algorithm that is executed frequently in a task or program. Depending upon the granularity, hardware acceleration can vary from a small functional unit to a large functional block (like motion estimation in MPEG-2).

## Hardware acceleration units by application

| Application | Hardware accelerator | Acronym |
|---|---|---|
|   |   |   |
| Computer graphics General-purpose computing GP computing, on Nvidia graphics cards Ray tracing Video codec | Graphics processing unit General-purpose computing on GPU CUDA architecture Ray-tracing hardware Various video acceleration hardware | GPU GPGPU CUDA RTX N/A |
|   |   |   |
| Digital signal processing | Digital signal processor | DSP |
| Analog signal processing | Field-programmable analog array Field-programmable RF | FPAA FPRF |
| Image processing | Webcam or image processor | IPU |
| Sound processing | Sound card and sound card mixer | N/A |
| Computer networking on a chip TCP Input/output | Network processor and network interface controller Network on a chip TCP offload engine IPsec offload I/O Acceleration Technology | NPU and NIC NoC TCPOE or TOE I/OAT or IOAT |
| Cryptography Encryption ISA SSL/TLS Attack Random number generation | Cryptographic accelerator and secure cryptoprocessor Hardware-based encryption AES instruction set SSL acceleration Custom hardware attack Hardware random number generator | N/A |
| Artificial intelligence Machine vision/computer vision Neural networks Brain simulation | AI accelerator Vision processing unit Physical neural network Neuromorphic engineering | N/A VPU PNN N/A |
| Multilinear algebra | Tensor processing unit | TPU |
| Physics simulation | Physics processing unit | PPU |
| Regular expressions | Regular expression coprocessor | N/A |
| Data compression | Data compression accelerator | N/A |
| In-memory processing | Network on a chip and Systolic array | NoC; N/A |
| Data processing | Data processing unit | DPU |
| Any computing task | Computer hardware Field-programmable gate arrays Application-specific integrated circuits Complex programmable logic devices Systems-on-Chip Multi-processor system-on-chip Programmable system-on-chip | HW (sometimes) FPGA ASIC CPLD SoC MPSoC PSoC |
