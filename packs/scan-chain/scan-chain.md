---
title: "Scan chain"
source: https://en.wikipedia.org/wiki/Scan_chain
domain: scan-chain
license: CC-BY-SA-4.0
tags: scan chain, scan flip-flop, boundary scan, jtag test access
fetched: 2026-07-02
---

# Scan chain

**Scan chain** is a technique used in design for testing (DFT). The objective is to make testing easier by providing a simple way to set and observe every flip-flop in an IC. It simplifies the testing and debugging of complex digital systems. In scan-based design, flip-flops operate in two distinct modes: **normal mode** and **scan mode**. In normal mode, they support regular system operations. In scan mode, however, they are reconfigured into one long shift register, known as a **Scan Chain**.

The basic structure of scan include the following set of signals in order to control and observe the scan mechanism.

1. Scan_in (SI) and Scan_out (SO) define the input and output of a scan chain. In a full scan mode usually each input drives only one chain and scan out observe one as well.
2. A scan enable (SE) pin is a special signal that is added to a design. When this signal is asserted, every flip-flop in the design is connected into a long shift register.
3. Clock signal which is used for controlling all the flip-flops in the chain during shift phase and the capture phase. An arbitrary pattern can be entered into the chain of flip-flops, and the state of every flip-flop can be read out.

## Historical Context

The conceptual origins of scan date back to the 1965, notably with IBM’s System/360 Model 50, which implemented scan-in and scan-out functions for processor self-diagnosis. Scan design, as formally applied to VLSI testing, gained traction after the landmark 1973 paper by Williams and Angell, and was widely advanced by IBM researchers including Eichelberger and Williams.

## Implementation and Variants

In a full scan design, automatic test pattern generation (ATPG) is particularly simple. No sequential pattern generation is required - combinatorial tests, which are much easier to generate, will suffice. If you have a combinatorial test, it can be easily applied.

- Assert scan mode, and set up the desired inputs.
- De-assert scan mode, and apply one clock. Now the results of the test are captured in the target flip-flops.
- Re-assert scan mode, and see if the combinatorial test passed.

In a chip that does not have a full scan design—i.e., the chip has sequential circuits, such as memory elements that are not part of the scan chain, sequential pattern generation is required. Test pattern generation for sequential circuits searches for a sequence of vectors to detect a particular fault through the space of all possible vector sequences.

Even a simple stuck-at fault requires a sequence of vectors for detection in a sequential circuit. Also, due to the presence of memory elements, the controllability and observability of the internal signals in a sequential circuit are in general much more difficult than those in a combinational logic circuit. These factors make the complexity of sequential ATPG much higher than that of combinational ATPG.

There are many variants:

- **Partial scan**: Only some of the flip-flops are connected into chains. This method reduces area and delay overhead, but requires more complex **ATPG**.
- **Multiple scan chains**: Two or more scan chains are built in parallel, to reduce the time to load and observe.
- Test compression: the input to the scan chain is provided by on-board logic.

## Advanced Techniques

**Random-access scan** **(RAS)** extends scan design by allowing individual flip-flops to be accessed like RAM cells via addressable selection. This enables rapid access and reduced scan time. However, the increased area from address decoders and control logic has limited its adoption.

**Scan-Hold Flip-Flops (SHFFs)** are a variant where a hold latch is added after the scan flip-flop. This design helps decouple scan and functional modes, making it ideal for delay fault testing. While SHFFs improve test control, they add both area (approx. 30%) and timing overhead.

## Design Automation and Practical Use

Modern Electronic Design Automation (EDA) tools fully support scan insertion, rule checking, and ATPG vector generation. Scan design audits ensure compliance with DFT rules — such as using only D-type flip-flops, clock controllability, and separating scan and functional clocks. Once design verification is complete, automatic scan insertion tools can retrofit flip-flops, wire scan chains, and generate test vectors with high fault coverage.

Scan testing is especially critical in **ASICs and SoCs**, where internal nodes are otherwise unobservable. Despite area and timing costs, scan design remains the industry standard for testability and is supported by all major digital design flows.
