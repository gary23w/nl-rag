---
title: "Re-order buffer"
source: https://en.wikipedia.org/wiki/Reorder_buffer
domain: cpu-microarchitecture
license: CC-BY-SA-4.0
tags: cpu microarchitecture, instruction pipelining, risc pipeline stages, processor datapath
fetched: 2026-07-02
---

# Re-order buffer

(Redirected from

Reorder buffer

)

A **re-order buffer** (**ROB**) is a hardware unit used in an extension to Tomasulo's algorithm to support out-of-order and speculative instruction execution. The extension forces instructions to be committed in-order.

The buffer is a circular buffer (to provide a FIFO instruction ordering queue) implemented as an array/vector (which allows recording of results against instructions as they complete out of order).

There are three stages to the Tomasulo algorithm: "Issue", "Execute", "Write Result". In an extension to the algorithm, there is an additional "Commit" stage. During the Commit stage, instruction results are stored in a register or memory. The "Write Result" stage is modified to place results in the re-order buffer. Each instruction is tagged in the reservation station with its index in the ROB for this purpose.

The contents of the buffer are used for data dependencies of other instructions scheduled in the buffer. The head of the buffer will be committed once its result is valid. Its dependencies will have already been calculated and committed since they must be ahead of the instruction in the buffer though not necessarily adjacent to it. Data dependencies between instructions would normally stall the pipeline while an instruction waits for its dependent values. The ROB allows the pipeline to continue to process other instructions while ensuring results are committed in order to prevent data hazards such as Read after Write (RAW), Write after Read (WAR) and Write after Write (WAW).

There are additional fields in every entry of the buffer to support the extended algorithm:

- Instruction type (jump, store to memory, store to register)
- Destination (either memory address or register number)
- Result (value that goes to destination or indication of a (un)successful jump)
- Validity (does the result already exist?)

The consequences of the re-order buffer include precise exceptions and easy rollback control of target address mis-predictions (branch or jump). When jump prediction is not correct or a nonrecoverable exception is encountered in the instruction stream, the ROB is cleared of all instructions (by setting the circular queue tail to the head) and reservation stations are re-initialized.
