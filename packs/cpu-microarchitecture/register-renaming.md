---
title: "Register renaming"
source: https://en.wikipedia.org/wiki/Register_renaming
domain: cpu-microarchitecture
license: CC-BY-SA-4.0
tags: cpu microarchitecture, instruction pipelining, risc pipeline stages, processor datapath
fetched: 2026-07-02
---

# Register renaming

In computer architecture, **register renaming** is a technique that abstracts logical registers from physical registers. Every logical register has a set of physical registers associated with it. When a machine language instruction refers to a particular logical register, the processor transposes this name to one specific physical register on the fly. The physical registers are opaque and cannot be referenced directly but only via the canonical names.

This technique is used to eliminate false data dependencies arising from the reuse of registers by successive instructions that do not have any real data dependencies between them. The elimination of these false data dependencies reveals more instruction-level parallelism in an instruction stream, which can be exploited by various and complementary techniques such as superscalar and out-of-order execution for better performance.

## Problem approach

Programs are composed of instructions which operate on values. The instructions must name these values in order to distinguish them from one another. A typical instruction might say: add x and y and put the result in z . In this instruction, x , y and z are the names of storage locations.

It is common for the values being manipulated to be used several times in succession. Register machines take advantage of this by introducing a number of processor registers, which are high-speed memory locations that hold these values. Since register access is typically much faster than accessing memory, high-performance code and processors try to operate on registers when possible. The collection of registers in a particular design is known as its *register file*.

Individual registers in the file are referred to by number in the machine code. Encoding a number in the machine code requires several bits. For instance, in the Zilog Z80 there were eight general-purpose registers in the file. To select one of eight values requires three bits, as 23 = 8. More architectural (logical) registers of the same width and type can result in better performance, as more temporary values can be held in registers and thus avoid the expensive operations of saving or loading from memory. Similarly, wider registers that can hold more data can also improve performance, if the workload can make use of that. Generally, more modern processors and those with larger instruction words will use more registers when possible. For example, the IA-32 instruction set architecture has 8 general purpose registers, x86-64 has 16, many RISCs have 32, and IA-64 has 128.

The advantages of a larger register file are offset by the need to use more bits to encode the register number. For instance, in a system using 32-bit instructions, you might wish to have three registers, such that you can perform operations of the type z = $x+y$ . If the register file contains 32 entries, each one of the references will require 5 bits, and the set of three registers thus takes up 15 bits, leaving 17 to encode the operation and other information. Expanding the register file to 64 entries would require 6 bits, a total of 18 bits. While this may result in faster performance, it also means there are fewer bits left over for encoding the instruction. This leads to an effort to balance the size of the file with the number of possible instructions.

### Out-of-order

Processors in early computers often worked lock-step with their main memory, which reduced the advantages of large register files. A common design note from the minicomputer market of the 1960s was to have the registers be physically implemented in main memory, in which case the performance advantage was simply that the instruction could directly refer to the location rather than having to use a second byte or two to specify a complete memory address. This made the instructions smaller, and thus faster to read. This sort of design, which maximized performance by carefully tuning the instruction set for minimal size, was common until the 1980s. An example of this approach is the MOS 6502, which had only a single register, in which case it is referred to as the accumulator, and a special "zero page" addressing mode for the first 256 bytes of memory. Placing code and data in the zero page meant the instruction was only two bytes long instead of three, greatly improving performance through avoided reads, providing similar benefits to having more registers.

The widespread introduction of dynamic RAM in the 1970s changed this approach. Over time, the performance of the central processing units (CPUs) increased relative to the memory they were attached to, it was no longer reasonable to use main memory as registers. This led to increasingly large register files, internal to the CPU, to avoid referring to memory wherever possible. However, it is not possible to avoid accessing memory entirely in practice, and as the speed difference grew, every such access became more and more expensive in terms of the number of instructions that might be performed had the value been in a register.

Different instructions may take different amounts of time; for example, a processor may be able to execute hundreds of register-to-register instructions while a single load from the main memory is in progress. A key advance in improving performance is to allow those fast instructions to be performed while the others are waiting for data. This means the instructions are no longer completed in the order they are specified in the machine code, they are instead performed out-of-order.

Consider this piece of code running on an out-of-order CPU:

```mw
	r1 ≔ m[1024]     ;read the value in memory location 1024
	r1 ≔ r1 + 2      ;add two to the value
	m[1032] ≔ r1     ;save the result to location 1032
	r1 ≔ m[2048]     ;read value in 2048
	r1 ≔ r1 + 4      ;add 4
	m[2056] ≔ r1     ;save it to 2056
```

The instructions in the final three lines are independent of the first three instructions, but the processor cannot finish `r1 ≔ m[2048]` until the preceding `m[1032] ≔ r1` is complete, as doing so would add four to the value of 1024, not 2048.

If another register is available, this restriction can be eliminated by choosing different registers for the first three and the second three instructions:

```mw
	r1 ≔ m[1024]
	r1 ≔ r1 + 2
	m[1032] ≔ r1
	r2 ≔ m[2048]
	r2 ≔ r2 + 4
	m[2056] ≔ r2
```

Now the last three instructions can be executed in parallel with the first three. The program will run faster than before by eliminating the data dependency caused by unnecessarily using the same register in both sequences. A compiler can detect independent instruction sequences and, if there are registers that are available for use, choose different registers during register allocation in the code generation process.

However, to speed up code generated by compilers that do not perform that optimization, or code for which there were not sufficient registers to perform that optimization, many high-performance CPUs provide a register file with more registers than are specified in the instruction set, and, in hardware, rename references in instruction-set-defined registers to refer to registers in the register file, so that the original instruction sequence, using only r1, behaves as if it were:

```mw
	rA ≔ m[1024]
	rA ≔ rA + 2
	m[1032] ≔ rA
	rB ≔ m[2048]
	rB ≔ rB + 4
	m[2056] ≔ rB
```

with register r1 "renamed" to the internal register rA for the first three instructions and to the internal register rB for the second three instructions. This removes the false data dependency, allowing the first three instructions to be executed in parallel with the second three instructions.

## Data hazards

When more than one instruction references a particular location as an operand, either by reading it (as an input) or by writing to it (as an output), executing those instructions in an order different from the original program order can lead to three kinds of data hazards:

**Read-after-write (RAW)**

a read from a register or memory location must return the value placed there by the last write in program order, not some other write. This is referred to as a

true dependency

or

flow dependency

, and requires the instructions to execute in program order.

**Write-after-write (WAW)**

successive writes to a particular register or memory location must leave that location containing the result of the second write. This can be resolved by

squashing

(also known as cancelling, annulling, or mooting) the first write if necessary. WAW dependencies are also known as

output dependencies

.

**Write-after-read (WAR)**

a read from a register or memory location must return the last prior value written to that location, and not one written programmatically after the read. This is a sort of

false dependency

that can be resolved by renaming. WAR dependencies are also known as

anti-dependencies

.

Instead of delaying the write until all reads are completed, two copies of the location can be maintained, the old value and the new value. Reads that precede, in program order, the write of the new value can be provided with the old value, even while other reads that follow the write are provided with the new value. The false dependency is broken and additional opportunities for out-of-order execution are created. When all reads that need the old value have been satisfied, it can be discarded. This is the essential concept behind register renaming.

Anything that is read and written can be renamed. While the general-purpose and floating-point registers are discussed the most, flag and status registers or even individual status bits are commonly renamed as well.

Memory locations can also be renamed, although it is not commonly done to the extent practiced in register renaming. The Transmeta Crusoe processor's gated store buffer is a form of memory renaming.

If programs refrained from reusing registers immediately, there would be no need for register renaming. Some instruction sets (e.g., IA-64) specify very large numbers of registers for specifically this reason. However, there are limitations to this approach:

- It is very difficult for the compiler to avoid reusing registers without large code size increases. In loops, for instance, successive iterations would have to use different registers, which requires replicating the code in a process called loop unrolling, or utilising self-modifying code to change the operand targets in each iteration.
- Large numbers of registers require more bits for specifying a register as an operand in an instruction, resulting in increased code size.
- Many instruction sets historically specified smaller numbers of registers and cannot be changed while still retaining backwards compatibility.

Code size increases are important because when the program code is larger, the instruction cache misses more often and the processor stalls waiting for new instructions.

## Architectural versus physical registers

Machine language programs specify reads and writes to a limited set of registers specified by the instruction set architecture (ISA). For instance, the Alpha ISA specifies 32 integer registers, each 64 bits wide, and 32 floating-point registers, each 64 bits wide. These are the *architectural* registers. Programs written for processors running the Alpha instruction set will specify operations reading and writing those 64 registers. If a programmer stops the program in a debugger, they can observe the contents of these 64 registers (and a few status registers) to determine the progress of the machine.

One particular processor which implements this ISA, the Alpha 21264, has 80 integer and 72 floating-point *physical* registers. There are, on an Alpha 21264 chip, 80 physically separate locations which can store the results of integer operations, and 72 locations which can store the results of floating point operations (In fact, there are even more locations than that, but those extra locations are not germane to the register renaming operation.)

The following text describes two styles of register renaming, which are distinguished by the circuit which holds the data ready for an execution unit.

In all renaming schemes, the machine converts the architectural registers referenced in the instruction stream into tags. Where the architectural registers might be specified by 3 to 5 bits, the tags are usually a 6 to 8 bit number. The rename file must have a read port for every input of every instruction renamed every cycle, and a write port for every output of every instruction renamed every cycle. Because the size of a register file generally grows as the square of the number of ports, the rename file is usually physically large and consumes significant power.

In the *tag-indexed register file* style, there is one large register file for data values, containing one register for every tag. For example, if the machine has 80 physical registers, then it would use 7 bit tags. 48 of the possible tag values in this case are unused. In this style, when an instruction is issued to an execution unit, the tags of the source registers are sent to the physical register file, where the values corresponding to those tags are read and sent to the execution unit.

In the *reservation station* style, there are many small associative register files, usually one at the inputs to each execution unit. Each operand of each instruction in an issue queue has a place for a value in one of these register files. In this style, when an instruction is issued to an execution unit, the register file entries corresponding to the issue queue entry are read and forwarded to the execution unit.

**Architectural Register File or Retirement Register File (RRF)**

The committed register state of the machine. RAM indexed by logical register number. Typically written into as results are retired or committed out of a reorder buffer.

**Future File**

The most speculative register state of the machine. RAM indexed by logical register number.

**Active Register File**

The Intel P6 group's term for Future File.

**History Buffer**

Typically used in combination with a future file. Contains the "old" values of registers that have been overwritten. If the producer is still in flight it may be RAM indexed by history buffer number. After a branch misprediction must use results from the history buffer—either they are copied, or the future file lookup is disabled and the history buffer is

content-addressable memory

(CAM) indexed by logical register number.

**Reorder Buffer (ROB)**

A structure that is sequentially (circularly) indexed on a per-operation basis, for instructions in flight. It differs from a history buffer because the reorder buffer typically comes after the future file (if it exists) and before the architectural register file. Reorder buffers can be data-less or data-ful. Some examples: In Willamette's ROB, the ROB entries point to registers in the physical register file (PRF), and also contain other book keeping. This was also the first Out of Order design done by Andy Glew, at Illinois with HaRRM. P6's ROB, the ROB entries contain data; there is no separate PRF. Data values from the ROB are copied from the ROB to the RRF at retirement. One small detail: if there is temporal locality in ROB entries (i.e., if instructions close together in the von Neumann instruction sequence write back close together in time, it may be possible to perform write combining on ROB entries and so have fewer ports than a separate ROB/PRF would). It is not clear if it makes a difference, since a PRF should be banked. ROBs usually don't have associative logic, and certainly none of the ROBs designed by Andy Glew have CAMs.

Keith Diefendorff

insisted that ROBs have complex associative logic for many years. The first ROB proposal may have had CAMs.

### Tag-indexed register file

This is the renaming style used in the MIPS R10000, the Alpha 21264, and in the FP section of the AMD Athlon.

In the renaming stage, every architectural register referenced (for read or write) is looked up in an architecturally-indexed **remap file**. This file returns a tag and a ready bit. The tag is non-ready if there is a queued instruction which will write to it that has not yet executed. For read operands, this tag takes the place of the architectural register in the instruction. For every register write, a new tag is pulled from a free tag FIFO, and a new mapping is written into the remap file, so that future instructions reading the architectural register will refer to this new tag. The tag is marked as unready, because the instruction has not yet executed. The previous physical register allocated for that architectural register is saved with the instruction in the reorder buffer, which is a FIFO that holds the instructions in program order between the decode and graduation stages.

The instructions are then placed in various **issue queues**. As instructions are executed, the tags for their results are broadcast, and the issue queues match these tags against the tags of their non-ready source operands. A match means that the operand is ready. The remap file also matches these tags, so that it can mark the corresponding physical registers as ready. When all the operands of an instruction in an issue queue are ready, that instruction is ready to issue. The issue queues pick ready instructions to send to the various functional units each cycle. Non-ready instructions stay in the issue queues. This unordered removal of instructions from the issue queues can make them large and power-consuming.

Issued instructions read from a tag-indexed physical register file (bypassing just-broadcast operands) and then execute. Execution results are written to tag-indexed physical register file, as well as broadcast to the bypass network preceding each functional unit. Graduation puts the previous tag for the written architectural register into the free queue so that it can be reused for a newly decoded instruction.

An exception or branch misprediction causes the remap file to back up to the remap state at last valid instruction via combination of state snapshots and cycling through the previous tags in the in-order pre-graduation queue. Since this mechanism is required, and since it can recover any remap state (not just the state before the instruction currently being graduated), branch mispredictions can be handled before the branch reaches graduation, potentially hiding the branch misprediction latency.

### Reservation stations

This is the style used in the integer section of the AMD K7 and K8 designs.

In the renaming stage, every architectural register referenced for reads is looked up in both the architecturally-indexed **future file** and the rename file. The future file read gives the value of that register, if there is no outstanding instruction yet to write to it (i.e., it's ready). When the instruction is placed in an issue queue, the values read from the future file are written into the corresponding entries in the reservation stations. Register writes in the instruction cause a new, non-ready tag to be written into the rename file. The tag number is usually serially allocated in instruction order—no free tag FIFO is necessary.

Just as with the tag-indexed scheme, the issue queues wait for non-ready operands to see matching tag broadcasts. Unlike the tag-indexed scheme, matching tags cause the corresponding broadcast value to be written into the issue queue entry's reservation station.

Issued instructions read their arguments from the reservation station, bypass just-broadcast operands, and then execute. As mentioned earlier, the reservation station register files are usually small, with perhaps eight entries.

Execution results are written to the reorder buffer, to the reservation stations (if the issue queue entry has a matching tag), and to the future file if this is the last instruction to target that architectural register (in which case register is marked ready).

Graduation copies the value from the reorder buffer into the architectural register file. The sole use of the architectural register file is to recover from exceptions and branch mispredictions.

Exceptions and branch mispredictions, recognized at graduation, cause the architectural file to be copied to the future file, and all registers marked as ready in the rename file. There is usually no way to reconstruct the state of the future file for some instruction intermediate between decode and graduation, so there is usually no way to do early recovery from branch mispredictions.

### Comparison between the schemes

In both schemes, instructions are inserted in-order into the issue queues, but are removed out-of-order. If the queues do not collapse empty slots, then they will either have many unused entries, or require some sort of variable priority encoding for when multiple instructions are simultaneously ready to go. Queues that collapse holes have simpler priority encoding, but require simple but large circuitry to advance instructions through the queue.

Reservation stations have better latency from rename to execute, because the rename stage finds the register values directly, rather than finding the physical register number, and then using that to find the value. This latency shows up as a component of the branch misprediction latency.

Reservation stations also have better latency from instruction issue to execution, because each local register file is smaller than the large central file of the tag-indexed scheme. Tag generation and exception processing are also simpler in the reservation station scheme, as discussed below.

The physical register files used by reservation stations usually collapse unused entries in parallel with the issue queue they serve, which makes these register files larger in aggregate, and consume more power, and more complicated than the simpler register files used in a tag-indexed scheme. Worse yet, every entry in each reservation station can be written by every result bus, so that a reservation-station machine with, e.g., 8 issue queue entries per functional unit will typically have 9 times as many bypass networks as an equivalent tag-indexed machine. Consequently, result forwarding consumes much more power and area than in a tag-indexed design.

Furthermore, the reservation station scheme has four places (Future File, Reservation Station, Reorder Buffer and Architectural File) where a result value can be stored, whereas the tag-indexed scheme has just one (the physical register file). Because the results from the functional units, broadcast to all these storage locations, must reach a much larger number of locations in the machine than in the tag-indexed scheme, this function consumes more power, area, and time. Still, in machines equipped with very accurate branch prediction schemes and if execute latencies are a major concern, reservation stations can work remarkably well.

## History

The IBM System/360 Model 91 was an early machine that supported out-of-order execution of instructions; it used the Tomasulo algorithm, which uses register renaming.

The POWER1 from 1990 is the first microprocessor that used register renaming and out-of-order execution. This processor implemented register renaming only for floating-point loads. The POWER1 had only one FPU, so using renaming for floating-point instructions other than memory operation was unnecessary. The POWER2 had multiple FPUs, so renaming was used for all floating-point instructions.

The original R10000 design had neither collapsing issue queues nor variable priority encoding, and suffered starvation problems as a result—the oldest instruction in the queue would sometimes not be issued until both instruction decode stopped completely for lack of rename registers, and every other instruction had been issued. Later revisions of the design starting with the R12000 used a partially variable priority encoder to mitigate this problem.

Early out-of-order machines did not separate the renaming and ROB/PRF storage functions. For that matter, some of the earliest, such as Sohi's RUU or the Metaflow DCAF, combined scheduling, renaming, and storage all in the same structure.

Most modern machines do renaming by RAM indexing a map table with the logical register number. E.g., P6 did this; future files do this, and have data storage in the same structure.

However, earlier machines used content-addressable memory (CAM) in the renamer. E.g., the HPSM RAT, or Register Alias Table, essentially used a CAM on the logical register number in combination with different versions of the register.

In many ways, the story of out-of-order microarchitecture has been how these CAMs have been progressively eliminated. Small CAMs are useful; large CAMs are impractical.

The P6 microarchitecture was the first microarchitecture by Intel to implement both out-of-order execution and register renaming. The P6 microarchitecture was used in Pentium Pro, Pentium II, Pentium III, Pentium M, Core, and Core 2 microprocessors. The Cyrix M1, released on October 2, 1995, was the first x86 processor to use register renaming and out-of-order execution. Other x86 processors (such as NexGen Nx686 and AMD K5) released in 1996 also featured register renaming and out-of-order execution of RISC μ-operations (rather than native x86 instructions).
