---
title: "Out-of-order execution"
source: https://en.wikipedia.org/wiki/Out-of-order_execution
domain: meltdown-mitigation
license: CC-BY-SA-4.0
tags: meltdown mitigation, kernel page table isolation, out of order execution defense, transient execution defense
fetched: 2026-07-02
---

# Out-of-order execution

In computer engineering, **out-of-order execution** (or more formally **dynamic execution**) is an instruction scheduling paradigm used in high-performance central processing units (CPUs) to make use of instruction cycles that would otherwise be wasted. In this paradigm, a processor executes instructions in an order governed by the availability of input data and execution units, rather than by their original order in a program. In doing so, the processor can avoid being idle while waiting for the preceding instruction to complete and can, in the meantime, process the next instructions that are able to run immediately and independently.

## History

Out-of-order execution is a restricted form of dataflow architecture, which was a major research area in computer architecture in the 1970s and early 1980s.

### Early use in supercomputers

Arguably the first machine to use out-of-order execution is the CDC 6600 (1964), which used a scoreboard to resolve conflicts. The 6600 however lacked WAW conflict handling, choosing instead to stall. This situation was termed a "First Order Conflict" by Thornton. Whilst it had both RAW conflict resolution (termed "Second Order Conflict") and WAR conflict resolution (termed "Third Order Conflict") all of which is sufficient to declare it capable of full out-of-order execution, the 6600 did not have precise exception handling. An early and limited form of Branch prediction was possible as long as the branch was to locations on what was termed the "Instruction Stack" which was limited to within a depth of seven words from the Program Counter.

About two years later, the IBM System/360 Model 91 (1966) introduced register renaming with Tomasulo's algorithm, which dissolves false dependencies (WAW and WAR), making full out-of-order execution possible. An instruction addressing a write into a register *rn* can be executed before an earlier instruction using the register *rn* is executed, by actually writing into an alternative (renamed) register *alt-rn*, which is turned into a normal register *rn* only when all the earlier instructions addressing *rn* have been executed, but until then *rn* is given for earlier instructions and *alt-rn* for later ones addressing *rn*.

In the Model 91 the register renaming is implemented by a bypass termed *Common Data Bus* (CDB) and memory source operand buffers, leaving the physical architectural registers unused for many cycles as the oldest state of registers addressed by any unexecuted instruction is found on the CDB. Another advantage the Model 91 has over the 6600 is the ability to execute instructions out-of-order in the same execution unit, not just between the units like the 6600. This is accomplished by reservation stations, from which instructions go to the execution unit when ready, as opposed to the FIFO queue of each execution unit of the 6600. The Model 91 is also capable of reordering loads and stores to execute before the preceding loads and stores, unlike the 6600, which only has a limited ability to move loads past loads, and stores past stores, but not loads past stores and stores past loads. Only the floating-point registers of the Model 91 are renamed, making it subject to the same WAW and WAR limitations as the CDC 6600 when running fixed-point calculations. The 91 and 6600 both also suffer from imprecise exceptions, which needed to be solved before out-of-order execution could be applied generally and made practical outside supercomputers.

### Precise exceptions

To have precise exceptions, the proper in-order state of the program's execution must be available upon an exception. By 1985 various approaches were developed as described by James E. Smith and Andrew R. Pleszkun. The CDC Cyber 205 was a precursor, as upon a virtual memory interrupt the entire state of the processor (including the information on the partially executed instructions) is saved into an *invisible exchange package*, so that it can resume at the same state of execution. However to make all exceptions precise, there has to be a way to cancel the effects of instructions. The CDC Cyber 990 (1984) implements precise interrupts by using a history buffer, which holds the old (overwritten) values of registers that are restored when an exception necessitates the reverting of instructions. Through simulation, Smith determined that adding a reorder buffer (or history buffer or equivalent) to the Cray-1S would reduce the performance of executing the first 14 Livermore loops (unvectorized) by only 3%. Important academic research in this subject was led by Yale Patt with his HPSm simulator.

In the 1980s many early RISC microprocessors, had out-of-order writeback to the registers, invariably resulting in imprecise exceptions. The Motorola 88100 was one of the few early microprocessors that did not suffer from imprecise exceptions despite out-of-order writes, although it did allow both precise and imprecise floating-point exceptions. Instructions started execution in order, but some (e.g. floating-point) took more cycles to complete execution. However, the single-cycle execution of the most basic instructions greatly reduced the scope of the problem compared to the CDC 6600.

### Decoupling

Smith also researched how to make different execution units operate more independently of each other and of the memory, front-end, and branching. He implemented those ideas in the Astronautics ZS-1 (1988), featuring a decoupling of the integer/load/store pipeline from the floating-point pipeline, allowing inter-pipeline reordering. The ZS-1 was also capable of executing loads ahead of preceding stores. In his 1984 paper, he opined that enforcing the precise exceptions only on the integer/memory pipeline should be sufficient for many use cases, as it even permits virtual memory. Each pipeline had an instruction buffer to decouple it from the instruction decoder, to prevent the stalling of the front end. To further decouple the memory access from execution, each of the two pipelines was associated with two addressable queues that effectively performed limited register renaming. A similar decoupled architecture had been used a bit earlier in the Culler 7. The ZS-1's ISA, like IBM's subsequent POWER, aided the early execution of branches.

### Research comes to fruition

With the POWER1 (1990), IBM returned to out-of-order execution. It was the first processor to combine register renaming (though again only floating-point registers) with precise exceptions. It uses a *physical register file* (i.e. a dynamically remapped file with both uncommitted and committed values) instead of a reorder buffer, but the ability to cancel instructions is needed only in the branch unit, which implements a history buffer (named *program counter stack* by IBM) to undo changes to count, link, and condition registers. The reordering capability of even the floating-point instructions is still very limited; due to POWER1's inability to reorder floating-point arithmetic instructions (results became available in-order), their destination registers aren't renamed. POWER1 also doesn't have reservation stations needed for out-of-order use of the same execution unit. The next year IBM's ES/9000 model 900 had register renaming added for the general-purpose registers. It also has reservation stations with six entries for the dual integer unit (each cycle, from the six instructions up to two can be selected and then executed) and six entries for the FPU. Other units have simple FIFO queues. The reordering distance is up to 32 instructions. The A19 of Unisys' A-series of mainframes was also released in 1991 and was claimed to have out-of-order execution, and one analyst called the A19's technology three to five years ahead of the competition.

### Wide adoption

The first superscalar single-chip processors (Intel i960CA in 1989) used a simple scoreboarding scheduling like the CDC 6600 had a quarter of a century earlier. In 1992–1996 a rapid advancement of techniques, enabled by increasing transistor counts, saw proliferation down to personal computers. The Motorola 88110 (1992) used a history buffer to revert instructions. Loads could be executed ahead of preceding stores. While stores and branches were waiting to start execution, subsequent instructions of other types could keep flowing through all the pipeline stages, including writeback. The 12-entry capacity of the history buffer placed a limit on the reorder distance. The PowerPC 601 (1993) was an evolution of the RISC Single Chip, itself a simplification of POWER1. The 601 permitted branch and floating-point instructions to overtake the integer instructions already in the fetched instruction queue, the lowest four entries of which were scanned for dispatchability. In the case of a cache miss, loads and stores could be reordered. Only the link and count registers could be renamed. In the fall of 1994 NexGen and IBM with Motorola brought the renaming of general-purpose registers to single-chip CPUs. NexGen's Nx586 was the first x86 processor capable of out-of-order execution and featured a reordering distance of up to 14 micro-operations. The PowerPC 603 renamed both the general-purpose and FP registers. Each of the four non-branch execution units can have one instruction wait in front of it without blocking the instruction flow to the other units. A five-entry reorder buffer lets no more than four instructions overtake an unexecuted instruction. Due to a store buffer, a load can access cache ahead of a preceding store.

PowerPC 604 (1995) was the first single-chip processor with execution unit-level reordering, as three out of its six units each had a two-entry reservation station permitting the newer entry to execute before the older. The reorder buffer capacity is 16 instructions. A four-entry load queue and a six-entry store queue track the reordering of loads and stores upon cache misses. HAL SPARC64 (1995) exceeded the reordering capacity of the ES/9000 model 900 by having three 8-entry reservation stations for integer, floating-point, and address generation unit, and a 12-entry reservation station for load/store, which permits greater reordering of cache/memory access than preceding processors. Up to 64 instructions can be in a reordered state at a time. Pentium Pro (1995) introduced a *unified reservation station*, which at the 20 micro-OP capacity permitted very flexible reordering, backed by a 40-entry reorder buffer. Loads can be reordered ahead of both loads and stores.

The practically attainable per-cycle rate of execution rose further as full out-of-order execution was further adopted by SGI/MIPS (R10000) and HP PA-RISC (PA-8000) in 1996. The same year Cyrix 6x86 and AMD K5 brought advanced reordering techniques into mainstream personal computers. Since DEC Alpha gained out-of-order execution in 1998 (Alpha 21264), the top-performing out-of-order processor cores have been unmatched by in-order cores other than HP/Intel Itanium 2 and IBM POWER6, though the latter had an out-of-order floating-point unit. The other high-end in-order processors fell far behind, namely Sun's UltraSPARC III/IV, and IBM's mainframes which had lost the out-of-order execution capability for the second time, remaining in-order into the z10 generation. Later big in-order processors were focused on multithreaded performance, but eventually the SPARC T series and Xeon Phi changed to out-of-order execution in 2011 and 2016 respectively.

Almost all processors for phones and other lower-end applications remained in-order until c. 2010. First, Qualcomm's Scorpion (reordering distance of 32) shipped in Snapdragon, and a bit later Arm's A9 succeeded A8. For low-end x86 personal computers in-order Bonnell microarchitecture in early Intel Atom processors were first challenged by AMD's Bobcat microarchitecture, and in 2013 were succeeded by an out-of-order Silvermont microarchitecture. Because the complexity of out-of-order execution precludes achieving the lowest minimum power consumption, cost and size, in-order execution is still prevalent in microcontrollers and embedded systems, as well as in phone-class cores such as Arm's A55 and A510 in big.LITTLE configurations.

## Basic concept

### Background

Out-of-order execution is more sophisticated relative to the baseline of in-order execution. In pipelined in-order execution processors, execution of instructions overlap in pipelined fashion with each requiring multiple clock cycles to complete. The consequence is that results from a previous instruction will lag behind where they may be needed in the next. In-order execution still has to keep track of these dependencies. Its approach is however quite unsophisticated: stall, every time. Out-of-order uses much more sophisticated data tracking techniques, as described below.

### In-order processors

In earlier processors, the processing of instructions is performed in an instruction cycle normally consisting of the following steps:

1. Instruction fetch.
2. If input operands are available (in processor registers, for instance), the instruction is dispatched to the appropriate functional unit. If one or more operands are unavailable during the current clock cycle (generally because they must be fetched from memory), the processor stalls until they are available.
3. The instruction is executed by the appropriate functional unit.
4. The functional unit writes the results back to the register file.

Often, an in-order processor has a bit vector recording which registers will be written to by a pipeline. If any input operands have the corresponding bit set in this vector, the instruction stalls. Essentially, the vector performs a greatly simplified role of protecting against register hazards. Thus out-of-order execution uses 2D matrices whereas in-order execution uses a 1D vector for hazard avoidance.

### Out-of-order processors

This new paradigm breaks up the processing of instructions into these steps:

1. Instruction fetch.
2. Instruction decoding.
3. Instruction renaming.
4. Instruction dispatch to an instruction queue (also called instruction buffer or reservation stations).
5. The instruction waits in the queue until its input operands are available. The instruction can leave the queue before older instructions.
6. The instruction is issued to the appropriate functional unit and executed by that unit.
7. The results are queued.
8. Only after all older instructions have their results written back to the register file, then this result is written back to the register file. This is called the graduation or retire stage.

The key concept of out-of-order processing is to allow the processor to avoid a class of stalls that occur when the data needed to perform an operation are unavailable. In the outline above, the processor avoids the stall that occurs in step 2 of the in-order processor when the instruction is not completely ready to be processed due to missing data.

Out-of-order processors fill these *slots* in time with other instructions that *are* ready, then either reorder the results at the end to make it appear that the instructions were processed as normal, record and thus apply the original *program order*, or commit in uninterruptible batches where order will not cause data corruption. The way the instructions are ordered in the original computer code is known as *program order*, in the processor they are handled in *data order*, the order in which the data becomes available in the processor's registers. Fairly complex circuitry is needed to convert from one ordering to the other and maintain a logical ordering of the output.

The benefit of out-of-order processing grows as the instruction pipeline deepens and the speed difference between main memory (or cache memory) and the processor widens. On modern machines, the processor runs many times faster than the memory, so during the time an in-order processor spends waiting for data to arrive, it could have theoretically processed a large number of instructions.

## Dispatch and issue decoupling allows out-of-order issue

One of the differences created by the new paradigm is the creation of queues that allow the dispatch step to be decoupled from the issue step and the graduation stage to be decoupled from the execute stage. An early name for the paradigm was *decoupled architecture*. In the earlier *in-order* processors, these stages operated in a fairly lock-step, pipelined fashion.

The fetch and decode stages is separated from the execute stage in a pipelined processor by using a buffer. The buffer's purpose is to partition the memory access and execute functions in a computer program and achieve high performance by exploiting the fine-grain parallelism between the two. In doing so, it effectively hides all memory latency from the processor's perspective.

A larger buffer can, in theory, increase throughput. However, if the processor has a branch misprediction then the entire buffer may need to be flushed, wasting a lot of clock cycles and reducing the effectiveness. Furthermore, larger buffers create more heat and use more die space. For this reason processor designers today favor a multi-threaded design approach.

Decoupled architectures are generally thought of as not useful for general-purpose computing as they do not handle control-intensive code well. Control intensive code include such things as nested branches that occur frequently in operating system kernels. Decoupled architectures play an important role in scheduling in very long instruction word (VLIW) architectures.

## Execute and writeback decoupling allows program restart

The queue for results is necessary to resolve issues such as branch mispredictions and exceptions. The results queue allows programs to be restarted after an exception and for the instructions to be completed in program order. The queue allows results to be discarded due to mispredictions on older branch instructions and exceptions taken on older instructions. The ability to issue instructions past branches that have yet to be resolved is known as speculative execution.

## Micro-architectural choices

Are the instructions dispatched to a centralized queue or to multiple distributed queues?

IBM PowerPC

processors use queues that are distributed among the different functional units while other out-of-order processors use a centralized queue. IBM uses the term

reservation stations

for their distributed queues.

Is there an actual results queue or are the results written directly into a register file? For the latter, the queueing function is handled by register maps that hold the register renaming information for each instruction in flight.

Early Intel out-of-order processors use a results queue called a

reorder buffer

,

while most later out-of-order processors use register maps.
