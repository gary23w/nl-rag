---
title: "Hazard (computer architecture)"
source: https://en.wikipedia.org/wiki/Hazard_(computer_architecture)
domain: cpu-microarchitecture
license: CC-BY-SA-4.0
tags: cpu microarchitecture, instruction pipelining, risc pipeline stages, processor datapath
fetched: 2026-07-02
---

# Hazard (computer architecture)

In the domain of central processing unit (CPU) design, **hazards** are problems with the instruction pipeline in CPU microarchitectures when the next instruction cannot execute in the following clock cycle, and can potentially lead to incorrect computation results. Three common types of hazards are data hazards, structural hazards, and control hazards (branching hazards).

There are several methods used to deal with hazards, including pipeline stalls/pipeline bubbling, operand forwarding, and in the case of out-of-order execution, the scoreboarding method and the Tomasulo algorithm.

## Background

Instructions in a pipelined processor are performed in several stages, so that at any given time several instructions are being processed in the various stages of the pipeline, such as fetch and execute. There are many different instruction pipeline microarchitectures, and instructions may be executed out-of-order. A hazard occurs when two or more of these simultaneous (possibly out of order) instructions conflict.

## Types

### Structural hazards

A structural hazard occurs when two (or more) instructions which are already in a pipeline need the same resource. The result is that instructions must be executed in series rather than in parallel for a portion of the pipeline. Structural hazards are sometimes referred to as resource hazards.

Example: A situation in which multiple instructions are ready to enter the execution phase but there is a single ALU (Arithmetic Logic Unit). One solution to this resource hazard is to increase available resources, by having multiple ports into main memory and multiple ALUs.

### Control hazards (branch hazards or instruction hazards)

Control hazard occurs when the control logic incorrectly predicts which program branch will be taken and therefore brings a sequence of instructions into the pipeline that are subsequently discarded. The term branch hazard also refers to a control hazard.

## Pipeline bubbling

*Bubbling the pipeline*, also termed a *pipeline break* or *pipeline stall*, is a method to preclude data, structural, and branch hazards. As instructions are fetched, control logic determines whether a hazard could/will occur. If this is true, then the control logic inserts no operations (NOPs) into the pipeline. Thus, before the next instruction (which would cause the hazard) executes, the prior one will have had sufficient time to finish and prevent the hazard. If the number of NOPs equals the number of stages in the pipeline, the processor has been cleared of all instructions and can proceed free from hazards. All forms of stalling introduce a delay before the processor can resume execution.

*Flushing the pipeline* occurs when a branch instruction jumps to a new memory location, invalidating all prior stages in the pipeline. These prior stages are cleared, allowing the pipeline to continue at the new instruction indicated by the branch.

### Data hazards

There are several main solutions and algorithms used to resolve data hazards:

- insert a *pipeline bubble* whenever a read after write (RAW) dependency is encountered, guaranteed to increase latency, or
- use out-of-order execution to potentially prevent the need for pipeline bubbles
- use *operand forwarding* to use data from later stages in the pipeline

In the case of out-of-order execution, the algorithm used can be:

- scoreboarding, in which case a *pipeline bubble* is needed only when there is no functional unit available
- the Tomasulo algorithm, which uses register renaming, allowing continual issuing of instructions

The task of removing data dependencies can be delegated to the compiler, which can fill in an appropriate number of NOP instructions between dependent instructions to ensure correct operation, or re-order instructions where possible.

#### Operand forwarding

#### Examples

In the following examples, computed values are in

bold

, while Register numbers are not.

For example, to write the value 3 to register 1, (which already contains a 6), and then add 7 to register 1 and store the result in register 2, i.e.:

```
i0: R1 = 6
i1: R1 = 3
i2: R2 = R1 + 7 = 10
```

Following execution, register 2 should contain the value **10**. However, if i1 (write **3** to register 1) does not fully exit the pipeline before i2 starts executing, it means that R1 does not contain the value **3** when i2 performs its addition. In such an event, i2 adds **7** to the old value of register 1 (**6**), and so register 2 contains **13** instead, i.e.:

```
i0: R1 = 6
i2: R2 = R1 + 7 = 13
i1: R1 = 3
```

This error occurs because i2 reads Register 1 before i1 has committed/stored the result of its write operation to Register 1. So when i2 is reading the contents of Register 1, register 1 still contains **6**, *not* **3**.

Forwarding (described below) helps correct such errors by depending on the fact that the output of i1 (which is **3**) can be used by subsequent instructions *before* the value **3** is committed to/stored in Register 1.

Forwarding applied to the example means that *there is no wait to commit/store the output of i1 in Register 1 (in this example, the output is **3**) before making that output available to the subsequent instruction (in this case, i2).* The effect is that i2 uses the correct (the more recent) value of Register 1: the commit/store was made immediately and not pipelined.

With forwarding enabled, the *Instruction Decode/Execution* (ID/EX) stage of the pipeline now has two inputs: the value read from the register specified (in this example, the value **6** from Register 1), and the new value of Register 1 (in this example, this value is **3**) which is sent from the next stage *Instruction Execute/Memory Access* (EX/MEM). Added control logic is used to determine which input to use.

### Control hazards (branch hazards)

To avoid control hazards microarchitectures can:

- insert a *pipeline bubble* (discussed above), guaranteed to increase latency, or
- use branch prediction and essentially make educated guesses about which instructions to insert, in which case a *pipeline bubble* will only be needed in the case of an incorrect prediction

In the event that a branch causes a pipeline bubble after incorrect instructions have entered the pipeline, care must be taken to prevent any of the wrongly-loaded instructions from having any effect on the processor state excluding energy wasted processing them before they were discovered to be loaded incorrectly.

### Other techniques

Memory latency is another factor that designers must attend to, because the delay could reduce performance. Different types of memory have different accessing time to the memory. Thus, by choosing a suitable type of memory, designers can improve the performance of the pipelined data path.
