---
title: "Parallel RAM"
source: https://en.wikipedia.org/wiki/Parallel_RAM
domain: parallel-complexity
license: CC-BY-SA-4.0
tags: parallel complexity, work span model, brent theorem, p complete problem
fetched: 2026-07-02
---

# Parallel RAM

In computer science, a **parallel random-access machine** (**parallel RAM** or **PRAM**) is a shared-memory abstract machine. As its name indicates, the PRAM is intended as the parallel-computing analogy to the random-access machine (RAM) (not to be confused with random-access memory). In the same way that the RAM is used by sequential-algorithm designers to model algorithmic performance (such as time complexity), the PRAM is used by parallel-algorithm designers to model parallel algorithmic performance (such as time complexity, where the number of processors assumed is typically also stated). Similar to the way in which the RAM model neglects practical issues, such as access time to cache memory versus main memory, the PRAM model neglects such issues as synchronization and communication, but provides any (problem-size-dependent) number of processors. Algorithm cost, for instance, is estimated using two parameters O(time) and O(time × processor_number).

## Read/write conflicts

Read/write conflicts, commonly termed interlocking in accessing the same shared memory location simultaneously are resolved by one of the following strategies:

1. Exclusive read exclusive write (EREW)—every memory cell can be read or written to by only one processor at a time
2. Concurrent read exclusive write (CREW)—multiple processors can read a memory cell but only one can write at a time
3. Exclusive read concurrent write (ERCW)—mostly never considered because it mostly doesn't add more power
4. Concurrent read concurrent write (CRCW)—multiple processors can read and write. A CRCW PRAM is sometimes called a **concurrent random-access machine**.

Here, E and C stand for 'exclusive' and 'concurrent' respectively. The read causes no discrepancies while the concurrent write is further defined as:

Common

—all processors write the same value; otherwise is illegal

Arbitrary

—only one arbitrary attempt is successful, others retire

Priority

—processor rank indicates who gets to write

Another kind of

array reduction

operation like SUM, Logical AND or MAX.

Several simplifying assumptions are made while considering the development of algorithms for PRAM. They are:

1. There is no limit on the number of processors in the machine.
2. Any memory location is uniformly accessible from any processor.
3. There is no limit on the amount of shared memory in the system.
4. Resource contention is absent.
5. The programs written on these machines are, in general, of type SIMD.

These kinds of algorithms are useful for understanding the exploitation of concurrency, dividing the original problem into similar sub-problems and solving them in parallel. The introduction of the formal 'P-RAM' model in Wyllie's 1979 thesis had the aim of quantifying analysis of parallel algorithms in a way analogous to the Turing Machine. The analysis focused on a MIMD model of programming using a CREW model but showed that many variants, including implementing a CRCW model and implementing on an SIMD machine, were possible with only constant overhead.

## Implementation

PRAM algorithms cannot be parallelized with the combination of CPU and dynamic random-access memory (DRAM) because DRAM does not allow concurrent access to a single bank (not even different addresses in the bank); but they can be implemented in hardware or read/write to the internal static random-access memory (SRAM) blocks of a field-programmable gate array (FPGA), it can be done using a CRCW algorithm.

However, the test for practical relevance of PRAM (or RAM) algorithms depends on whether their cost model provides an effective abstraction of some computer; the structure of that computer can be quite different than the abstract model. The knowledge of the layers of software and hardware that need to be inserted is beyond the scope of this article. But, articles such as Vishkin (2011) demonstrate how a PRAM-like abstraction can be supported by the explicit multi-threading (XMT) paradigm and articles such as Caragea & Vishkin (2011) demonstrate that a PRAM algorithm for the maximum flow problem can provide strong speedups relative to the fastest serial program for the same problem. The article Ghanim, Vishkin & Barua (2018) demonstrated that PRAM algorithms as-is can achieve competitive performance even without any additional effort to cast them as multi-threaded programs on XMT.

## Example code

This is an example of SystemVerilog code which finds the maximum value in the array in only 2 clock cycles. It compares all the combinations of the elements in the array at the first clock, and merges the result at the second clock. It uses CRCW memory; `m[i] <= 1` and `maxNo <= data[i]` are written concurrently. The concurrency causes no conflicts because the algorithm guarantees that the same value is written to the same memory. This code can be run on FPGA hardware.

```mw
module FindMax #(parameter int len = 8)
                (input bit clock, resetN, input bit[7:0] data[len], output bit[7:0] maxNo);
    typedef enum bit[1:0] {COMPARE, MERGE, DONE} State;
                    
    State state;
    bit m[len];
    int i, j;
    
    always_ff @(posedge clock, negedge resetN) begin
        if (!resetN) begin
            for (i = 0; i < len; i++) m[i] <= 0;
            state <= COMPARE;
        end else begin
            case (state)
                COMPARE: begin
                    for (i = 0; i < len; i++) begin
                        for (j = 0; j < len; j++) begin
                            if (data[i] < data[j]) m[i] <= 1;
                        end
                    end
                    state <= MERGE;
                end
                
                MERGE: begin
                    for (i = 0; i < len; i++) begin
                        if (m[i] == 0) maxNo <= data[i];
                    end
                    state <= DONE;
                end
            endcase
        end
    end
endmodule
```
