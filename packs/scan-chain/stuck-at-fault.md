---
title: "Stuck-at fault"
source: https://en.wikipedia.org/wiki/Stuck-at_fault
domain: scan-chain
license: CC-BY-SA-4.0
tags: scan chain, scan flip-flop, boundary scan, jtag test access
fetched: 2026-07-02
---

# Stuck-at fault

A **stuck-at fault** is a particular fault model used by fault simulators and automatic test pattern generation (ATPG) tools to mimic a manufacturing defect within an integrated circuit. Individual signals and pins are assumed to be *stuck* at Logical '1', '0' and 'X'.

For example, an input is tied to a logical 1 state during test generation to assure that a manufacturing defect with that type of behavior can be found with a specific test pattern. Likewise the input could be tied to a logical 0 to model the behavior of a defective circuit that cannot switch its output pin. Not all faults can be analyzed using the stuck-at fault model. Compensation for static hazards, namely branching signals, can render a circuit untestable using this model. Also, redundant circuits cannot be tested using this model, since by design there is no change in any output as a result of a single fault.

## Single stuck at line

**Single stuck line** is a fault model used in digital circuits. It is used for post manufacturing testing, not design testing. The model assumes one line or node in the digital circuit is stuck at logic high or logic low. When a line is stuck, it is called a fault.

Digital circuits can be divided into:

1. Gate level or combinational circuits which contain no storage (latches and/or flip flops) but only gates like NAND, OR, XOR, etc.
2. Sequential circuits which contain storage.

This fault model applies to gate level circuits, or a block of a sequential circuit which can be separated from the storage elements. Ideally a gate-level circuit would be completely tested by applying all possible inputs and checking that they gave the right outputs, but this is completely impractical: an adder to add two 32-bit numbers would require 264 = 1.8*1019 tests, taking 58 years at 0.1 ns/test. The *stuck at* fault model assumes that only one input on one gate will be faulty at a time, assuming that if more are faulty, a test that can detect any single fault, should easily find multiple faults.

To use this fault model, each input pin on each gate in turn, is assumed to be grounded, and a *test vector* is developed to indicate the circuit is faulty. The test vector is a collection of bits to apply to the circuit's inputs, and a collection of bits expected at the circuit's output. If the gate pin under consideration is grounded, and this test vector is applied to the circuit, at least one of the output bits will not agree with the corresponding output bit in the test vector. After obtaining the test vectors for grounded pins, each pin is connected in turn to a logic one and another set of test vectors is used to find faults occurring under these conditions. Each of these faults is called a single *stuck-at-0* (s-a-0) or a single *stuck-at-1* (s-a-1) fault, respectively.

This model worked so well for transistor-transistor logic (TTL), which was the logic of choice during the 1970s and 1980s, that manufacturers advertised how well they tested their circuits by a number called "stuck-at fault coverage", which represented the percentage of all possible stuck-at faults that their testing process could find. While the same testing model works moderately well for CMOS, it is not able to detect all possible CMOS faults. This is because CMOS may experience a failure mode known as a *stuck-open* fault, which cannot be reliably detected with one test vector and requires that two vectors be applied sequentially. The model also fails to detect bridging faults between adjacent signal lines, occurring in pins that drive bus connections and array structures. Nevertheless, the concept of single stuck-at faults is widely used, and with some additional tests has allowed industry to ship an acceptable low number of bad circuits.

The testing based on this model is aided by several things:

1. A test developed for a single stuck-at fault often finds a large number of other stuck-at faults.
2. A series of tests for stuck-at faults will often, purely by serendipity, find a large number of other faults, such as stuck-open faults. This is sometimes called "windfall" fault coverage.
3. Another type of testing called *IDDQ testing* measures the way the power supply current of a CMOS integrated circuit changes when a small number of slowly changing test vectors are applied. Since CMOS draws a very low current when its inputs are static, any increase in that current indicates a potential problem.
