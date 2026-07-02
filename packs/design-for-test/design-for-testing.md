---
title: "Design for testing"
source: https://en.wikipedia.org/wiki/Design_for_testing
domain: design-for-test
license: CC-BY-SA-4.0
tags: design for test, test pattern generation, fault model, built-in self-test
fetched: 2026-07-02
---

# Design for testing

**Design for testing** or **design for testability** (**DFT**) consists of integrated circuit design techniques that add testability features to a hardware product design. The added features make it easier to develop and apply manufacturing tests to the designed hardware. The purpose of manufacturing tests is to validate that the product hardware contains no manufacturing defects that could adversely affect the product's correct functioning.

Tests are applied at several steps in the hardware manufacturing flow and, for certain products, may also be used for hardware maintenance in the customer's environment. The tests are generally driven by test programs that execute using automatic test equipment (ATE) or, in the case of system maintenance, inside the assembled system itself. In addition to finding and indicating the presence of defects (i.e., the test fails), tests may be able to log diagnostic information about the nature of the encountered test failures. The diagnostic information can be used to locate the source of the failure.

In other words, the response of vectors (patterns) from a good circuit is compared with the response of vectors (using the same patterns) from a DUT (device under test). If the response is the same or matches, the circuit is good. Otherwise, the circuit is not manufactured as intended.

DFT plays an important role in the development of test programs and as an interface for test applications and diagnostics. Automatic test pattern generation (ATPG) is much easier if appropriate DFT rules and suggestions have been implemented.

## History

DFT techniques have been used at least since the early days of electric/electronic data processing equipment. Early examples from the 1940s/50s are the switches and instruments that allowed an engineer to "scan" (i.e., selectively probe) the voltage/current at some internal nodes in an analog computer [analog scan]. DFT often is associated with design modifications that provide improved access to internal circuit elements such that the local internal state can be controlled (controllability) and/or observed (observability) more easily. The design modifications can be strictly physical in nature (e.g., adding a physical probe point to a net) or add active circuit elements to facilitate controllability/observability (e.g., inserting a multiplexer into a net). While controllability and observability improvements for internal circuit elements definitely are important for test, they are not the only type of DFT. Other guidelines, for example, deal with the electromechanical characteristics of the interface between the product under test and the test equipment. Examples are guidelines for the size, shape, and spacing of probe points, or the suggestion to add a high-impedance state to drivers attached to probed nets such that the risk of damage from back-driving is mitigated.

Over the years the industry has developed and used a large variety of more or less detailed and more or less formal guidelines for desired and/or mandatory DFT circuit modifications. The common understanding of DFT in the context of electronic design automation (EDA) for modern microelectronics is shaped to a large extent by the capabilities of commercial DFT software tools as well as by the expertise and experience of a professional community of DFT engineers researching, developing, and using such tools. Much of the related body of DFT knowledge focuses on digital circuits, while DFT for analog/mixed-signal circuits takes somewhat of a backseat.

## Objectives of DFT for microelectronics products

DFT affects and depends on the methods used for test development, test application, and diagnostics.

Most tool-supported DFT practiced in the industry today, at least for digital circuits, is predicated on a *Structural test* paradigm. Structural test makes no direct attempt to determine if the overall functionality of the circuit is correct. Instead, it tries to make sure that the circuit has been assembled correctly from some low-level building blocks as specified in a structural netlist. For example, are all specified logic gates present, operating correctly, and connected correctly? The stipulation is that if the netlist is correct and structural testing has confirmed the correct assembly of the circuit elements, then the circuit should be functioning correctly.

Note that this is very different from *functional testing*, which attempts to validate that the circuit under test functions according to its functional specification. This is closely related to the functional verification problem of determining if the circuit specified by the netlist meets the functional specifications, assuming it is built correctly.

One benefit of the Structural paradigm is that test generation can focus on testing a limited number of relatively simple circuit elements rather than having to deal with an exponentially exploding multiplicity of functional states and state transitions. While the task of testing a single logic gate at a time sounds simple, there is an obstacle to overcome. For today's highly complex designs, most gates are deeply embedded whereas the test equipment is only connected to the primary Input/outputs (I/Os) and/or some physical test points. The embedded gates, hence, must be manipulated through intervening layers of logic. If the intervening logic contains state elements, then the issue of an exponentially exploding state space and state transition sequencing creates an unsolvable problem for test generation. To simplify test generation, DFT addresses the accessibility problem by removing the need for complicated state transition sequences when trying to control and/or observe what's happening at some internal circuit element. Depending on the DFT choices made during circuit design/implementation, the generation of Structural tests for complex logic circuits can be more or less automated or self-automated. One key objective of DFT methodologies, hence, is to allow designers to make trade-offs between the amount and type of DFT and the cost/benefit (time, effort, quality) of the test generation task.

Another benefit is to diagnose a circuit in case any problem emerges in the future. It is like adding some features or provisions in the design so that devices can be tested in case of any fault during its use.

## Looking forward

One challenge for the industry is keeping up with the rapid advances in chip technology (I/O count/size/placement/spacing, I/O speed, internal circuit count/speed/power, thermal control, etc.) without being forced to continually upgrade the test equipment. Modern DFT techniques, hence, have to offer options that allow next-generation chips and assemblies to be tested on existing test equipment and/or reduce the requirements/cost for new test equipment. As a result, DFT techniques are continually being updated, such as incorporation of compression, in order to make sure that tester application times stay within certain bounds dictated by the cost target for the products under test.

## Diagnostics

Especially for advanced semiconductor technologies, it is expected that some of the chips on each manufactured wafer contain defects that render them non-functional. The primary objective of testing is to find and separate those non-functional chips from the fully functional ones, meaning that one or more responses captured by the tester from a non-functional chip under test differ from the expected response. The percentage of chips that fail testing, hence, should be closely related to the expected functional yield for that chip type. In reality, however, it is not uncommon that all chips of a new chip type arriving at the test floor for the first time fail (so-called zero-yield situation). In that case, the chips have to go through a debug process that tries to identify the reason for the zero-yield situation. In other cases, the test fall-out (percentage of test failures) may be higher than expected/acceptable or fluctuate suddenly. Again, the chips have to be subjected to an analysis process to identify the reason for the excessive test fall-out.

In both cases, vital information about the nature of the underlying problem may be hidden in the way the chips fail during testing. To facilitate better analysis, additional failure information beyond a simple pass/fail is collected into a fail log. The fail log typically contains information about when (e.g., tester cycle), where (e.g., at what tester channel), and how (e.g., logic value) the test failed. Diagnostics attempt to derive from the fail log at which logical/physical location inside the chip the problem most likely started. By running a large number of failures through the diagnostics process, called volume diagnostics, systematic failures can be identified.

In some cases (e.g., printed circuit boards, multi-chip modules (MCMs), embedded or stand-alone memories) it may be possible to repair a failing circuit under test. For that purpose, diagnostics must quickly find the failing unit and create a work order for repairing or replacing the failing unit.

DFT approaches can be more or less diagnostics-friendly. The related objectives of DFT are to facilitate or simplify failure data collection and diagnostics to an extent that can enable intelligent failure analysis (FA) sample selection, as well as improve the cost, accuracy, speed, and throughput of diagnostics and FA.

## Scan design

The most common method for delivering test data from chip inputs to internal *circuits under test* (CUTs, for short), and observing their outputs, is called scan-design. In scan design, registers (flip-flops or latches) in the design are connected in one or more scan chains, which are used to gain access to internal nodes of the chip. Test patterns are shifted in via the scan chain(s), functional clock signals are pulsed to test the circuit during the "capture cycle(s)", and the results are then shifted out to chip output pins and compared against the expected "good machine" results.

Straightforward application of scan techniques can result in large vector sets with corresponding long tester time and memory requirements. Test compression techniques address this problem by decompressing the scan input on chip and compressing the test output. Large gains are possible since any particular test vector usually only needs to set and/or examine a small fraction of the scan chain bits.

The output of a scan design may be provided in forms such as Serial Vector Format (SVF), to be executed by test equipment.

## Debug using DFT features

In addition to being useful for manufacturing "go/no go" testing, scan chains can also be used to "debug" chip designs. In this context, the chip is exercised in normal "functional mode" (for example, a computer or mobile phone chip might execute assembly language instructions). At any time, the chip clock can be stopped, and the chip re-configured into "test mode". At this point, the full internal state can be dumped out or set to any desired values by use of the scan chains. Another use of scan to aid debugging consists of scanning in an initial state to all memory elements and then go back to functional mode to perform system debugging. The advantage is to bring the system to a known state without going through many clock cycles. This use of scan chains, along with the clock control circuits, is a related sub-discipline of logic design called *design for debug* or *design for debuggability*.
