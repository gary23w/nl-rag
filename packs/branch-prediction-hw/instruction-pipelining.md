---
title: "Instruction pipelining"
source: https://en.wikipedia.org/wiki/Instruction_pipelining
domain: branch-prediction-hw
license: CC-BY-SA-4.0
tags: hardware branch prediction, branch target predictor, speculative execution, branch misprediction penalty
fetched: 2026-07-02
---

# Instruction pipelining

| Clock cycleInstr. No. | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| 1 | IF | ID | EX | MEM | WB |   |   |
| 2 |   | IF | ID | EX | MEM | WB |   |
| 3 |   |   | IF | ID | EX | MEM | WB |
| 4 |   |   |   | IF | ID | EX | MEM |
| 5 |   |   |   |   | IF | ID | EX |
| (IF = Instruction Fetch, ID = Instruction Decode, EX = Execute, MEM = Memory access, WB = Register write back). In the fourth clock cycle (the green column), the earliest instruction is in MEM stage, and the latest instruction has not yet entered the pipeline. |   |   |   |   |   |   |   |

In computer engineering, **instruction pipelining** is a technique for implementing instruction-level parallelism within a single processor. Pipelining attempts to keep every part of the processor busy with some instruction by dividing incoming instructions into a series of sequential steps (the eponymous "pipeline") performed by different processor units with different parts of instructions processed in parallel.

## Concept and motivation

In a pipelined computer, instructions travel through the central processing unit (CPU) in stages. For example, it might have one stage for each step of the von Neumann cycle: Fetch the instruction, fetch the operands, do the instruction, write the results. A pipelined computer usually has "pipeline registers" after each stage. These store information from the instruction and calculations so that the logic gates of the next stage can do the next step.

This arrangement lets the CPU complete an instruction on each clock cycle. It is common for even-numbered stages to operate on one edge of the square-wave clock, while odd-numbered stages operate on the other edge. This allows more CPU throughput than a multicycle computer at a given clock rate, but may increase latency due to the added overhead of the pipelining process itself. Also, even though the electronic logic has a fixed maximum speed, a pipelined computer can be made faster or slower by varying the number of stages in the pipeline. With more stages, each stage does less work, and so the stage has fewer delays from the logic gates and could run at a higher clock rate.

A pipelined model of computer is often the most economical, when cost is measured as logic gates per instruction per second. At each instant, an instruction is in only one pipeline stage, and on average, a pipeline stage is less costly than a multicycle computer. Also, when made well, most of the pipelined computer's logic is in use most of the time. In contrast, out of order computers usually have large amounts of idle logic at any given instant. Similar calculations usually show that a pipelined computer uses less energy per instruction.

However, a pipelined computer is usually more complex and more costly than a comparable multicycle computer. It typically has more logic gates, registers and a more complex control unit. In a like way, it might use more total energy, while using less energy per instruction. Out of order CPUs can usually do more instructions per second because they can do several instructions at once.

In a pipelined computer, the control unit arranges for the flow to start, continue, and stop as a program commands. The instruction data is usually passed in pipeline registers from one stage to the next, with a somewhat separated piece of control logic for each stage. The control unit also assures that the instruction in each stage does not harm the operation of instructions in other stages. For example, if two stages must use the same piece of data, the control logic assures that the uses are done in the correct sequence.

When operating efficiently, a pipelined computer will have an instruction in each stage. It is then working on all of those instructions at the same time. It can finish about one instruction for each cycle of its clock. But when a program switches to a different sequence of instructions, the pipeline sometimes must discard the data in process and restart. This is called a "stall."

Much of the design of a pipelined computer prevents interference between the stages and reduces stalls.

### Number of steps

The number of dependent steps varies with the machine architecture. For example:

- The 1956–61 IBM Stretch project proposed the terms Fetch, Decode, and Execute that have become common.
- The classic RISC pipeline comprises:
  1. Instruction fetch
  2. Instruction decode and register fetch
  3. Execute
  4. Memory access
  5. Register write back
- The Atmel AVR and the PIC microcontroller each have a two-stage pipeline.
- Many designs include pipelines as long as 7, 10 and even 20 stages (as in the Intel Pentium 4).
- The later "Prescott" and "Cedar Mill" NetBurst cores from Intel, used in the last Pentium 4 models and their Pentium D and Xeon derivatives, have a long 31-stage pipeline.
- The Xelerated X10q Network Processor has a pipeline more than a thousand stages long, although in this case 200 of these stages represent independent CPUs with individually programmed instructions. The remaining stages are used to coordinate accesses to memory and on-chip function units.

As the pipeline is made "deeper" (with a greater number of dependent steps), a given step can be implemented with simpler circuitry, which may let the processor clock run faster. Such pipelines may be called *superpipelines.*

A processor is said to be *fully pipelined* if it can fetch an instruction on every cycle. Thus, if some instructions or conditions require delays that inhibit fetching new instructions, the processor is not fully pipelined.

## History

Seminal uses of pipelining were in the ILLIAC II project and the IBM Stretch project, though a simple version was used earlier in the Z1 in 1939 and the Z3 in 1941.

Pipelining began in earnest in the late 1970s in supercomputers such as vector processors and array processors. One of the early supercomputers was the Cyber series built by Control Data Corporation. Its main architect, Seymour Cray, later headed Cray Research. Cray developed the XMP line of supercomputers, using pipelining for both multiply and add/subtract functions. Later, Star Technologies added parallelism (several pipelined functions working in parallel), developed by Roger Chen. In 1984, Star Technologies added the pipelined divide circuit developed by James Bradley.

Pipelining was not limited to supercomputers. In 1976, the Amdahl Corporation's 470 series general purpose mainframe had a 7-step pipeline, and a patented branch prediction circuit. A central element in RISC design philosophy, by the mid-1980s, pipelining was also being introduced into traditional CISC architectures by their developers.

## Hazards

The model of sequential execution assumes that each instruction completes before the next one begins; this assumption is not true on a pipelined processor. A situation where the expected result is problematic is known as a hazard. Imagine the following two register instructions to a hypothetical processor:

```
1: add 1 to R5
2: copy R5 to R6
```

If the processor has the 5 steps listed in the initial illustration (the 'Basic five-stage pipeline' at the start of the article), instruction 1 would be fetched at time *t*1 and its execution would be complete at *t5*. Instruction 2 would be fetched at *t2* and would be complete at *t6*. The first instruction might deposit the incremented number into R5 as its fifth step (register write back) at *t5*. But the second instruction might get the number from R5 (to copy to R6) in its second step (instruction decode and register fetch) at time *t3*. It seems that the first instruction would not have incremented the value by then. The above code invokes a hazard.

Writing computer programs in a compiled language might not raise these concerns, as the compiler could be designed to generate machine code that avoids hazards.

### Workarounds

In some early DSP and RISC processors, the documentation advises programmers to avoid such dependencies in adjacent and nearly adjacent instructions (called delay slots), or declares that the second instruction uses an old value rather than the desired value (in the example above, the processor might counter-intuitively copy the unincremented value), or declares that the value it uses is undefined. The programmer may have unrelated work that the processor can do in the meantime; or, to ensure correct results, the programmer may insert NOPs into the code, partly negating the advantages of pipelining.

### Solutions

Pipelined processors commonly use three techniques to work as expected when the programmer assumes that each instruction completes before the next one begins:

- The pipeline could stall, or cease scheduling new instructions until the required values are available. This results in empty slots in the pipeline, or *bubbles*, in which no work is performed.
- An additional data path can be added that routes a computed value to a future instruction elsewhere in the pipeline before the instruction that produced it has been fully retired, a process called operand forwarding.
- The processor can locate other instructions which are not dependent on the current ones and which can be immediately executed without hazards, an optimization known as out-of-order execution.

## Branches

A branch out of the normal instruction sequence often involves a hazard. Unless the processor can give effect to the branch in a single time cycle, the pipeline will continue fetching instructions sequentially. Such instructions cannot be allowed to take effect because the programmer has diverted control to another part of the program.

A conditional branch is even more problematic. The processor may or may not branch, depending on a calculation that has not yet occurred. Various processors may stall, may attempt branch prediction, and may be able to begin to execute two different program sequences (eager execution), each assuming the branch is or is not taken, discarding all work that pertains to the incorrect guess.

A processor with an implementation of branch prediction that usually makes correct predictions can minimize the performance penalty from branching. However, if branches are predicted poorly, it may create more work for the processor, such as flushing from the pipeline the incorrect code path that has begun execution before resuming execution at the correct location.

Programs written for a pipelined processor deliberately avoid branching to minimize possible loss of speed. For example, the programmer can handle the usual case with sequential execution and branch only on detecting unusual cases. Using programs such as gcov to analyze code coverage lets the programmer measure how often particular branches are actually executed and gain insight with which to optimize the code. In some cases, a programmer can handle both the usual case and unusual case with branch-free code.

## Special situations

**Self-modifying programs**

The technique of

self-modifying code

can be problematic on a pipelined processor. In this technique, one of the effects of a program is to modify its own upcoming instructions. If the processor has an

instruction cache

, the original instruction may already have been copied into a

prefetch input queue

and the modification will not take effect. Some processors such as the

Zilog Z280

can configure their on-chip cache memories for data-only fetches, or as part of their ordinary memory address space, and avoid such difficulties with self-modifying instructions.

**Uninterruptible instructions**

An instruction may be uninterruptible to ensure its

atomicity

, such as when it swaps two items. A sequential processor permits

interrupts

between instructions, but a pipelining processor overlaps instructions, so executing an uninterruptible instruction renders portions of ordinary instructions uninterruptible too. The

Cyrix coma bug

would

hang

a single-core system using an infinite loop in which an uninterruptible instruction was always in the pipeline.

## Design considerations

**Speed**

Pipelining keeps all portions of the processor occupied and increases the amount of useful work the processor can do in a given time. Pipelining typically reduces the processor's cycle time and increases the throughput of instructions. The speed advantage is diminished to the extent that execution encounters

hazards

that require execution to slow below its ideal rate. A non-pipelined processor executes only a single instruction at a time. The start of the next instruction is delayed not based on hazards but unconditionally.

A pipelined processor's need to organize all its work into modular steps may require the duplication of registers, which increases the latency of some instructions.

**Economy**

By making each dependent step simpler, pipelining can enable complex operations more economically than adding complex circuitry, such as for numerical calculations. However, a processor that declines to pursue increased speed with pipelining may be simpler and cheaper to manufacture.

**Predictability**

Compared to environments where the programmer needs to avoid or work around hazards, use of a non-pipelined processor may make it easier to program and to train programmers. The non-pipelined processor also makes it easier to predict the exact timing of a given sequence of instructions.

## Illustrated example

To the right is a generic pipeline with four stages: fetch, decode, execute and write-back. The top gray box is the list of instructions waiting to be executed, the bottom gray box is the list of instructions that have had their execution completed, and the middle white box is the pipeline.

The execution is as follows:

| Clock | Execution |
|---|---|
| 0 | Four instructions are waiting to be executed |
| 1 | The green instruction is fetched from memory |
| 2 | The green instruction is decoded The purple instruction is fetched from memory |
| 3 | The green instruction is executed (actual operation is performed) The purple instruction is decoded The blue instruction is fetched |
| 4 | The green instruction's results are written back to the register file or memory The purple instruction is executed The blue instruction is decoded The red instruction is fetched |
| 5 | The execution of green instruction is completed The purple instruction is written back The blue instruction is executed The red instruction is decoded |
| 6 | The execution of purple instruction is completed The blue instruction is written back The red instruction is executed |
| 7 | The execution of blue instruction is completed The red instruction is written back |
| 8 | The execution of red instruction is completed |
| 9 | The execution of all four instructions is completed |

### Pipeline bubble

A pipelined processor may deal with hazards by stalling and creating a bubble in the pipeline, resulting in one or more cycles in which nothing useful happens.

In the illustration at right, in cycle 3, the processor cannot decode the purple instruction, perhaps because the processor determines that decoding depends on results produced by the execution of the green instruction. The green instruction can proceed to the Execute stage and then to the Write-back stage as scheduled, but the purple instruction is stalled for one cycle at the Fetch stage. The blue instruction, which was due to be fetched during cycle 3, is stalled for one cycle, as is the red instruction after it.

Because of the bubble (the blue ovals in the illustration), the processor's Decode circuitry is idle during cycle 3. Its Execute circuitry is idle during cycle 4 and its Write-back circuitry is idle during cycle 5.

When the bubble moves out of the pipeline (at cycle 6), normal execution resumes. But everything now is one cycle late. It will take 8 cycles (cycle 1 through 8) rather than 7 to completely execute the four instructions shown in colors.
