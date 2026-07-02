---
title: "Timing closure"
source: https://en.wikipedia.org/wiki/Timing_closure
domain: static-timing-analysis
license: CC-BY-SA-4.0
tags: static timing analysis, timing closure, clock skew, propagation delay
fetched: 2026-07-02
---

# Timing closure

**Timing closure** in VLSI design and electronics engineering is the iterative design process of assuring all signals satisfy the timing requirements in a clocked synchronous circuit. The goal is to guarantee correct data transfer and reliable operation at the target clock frequency.

A synchronous circuit is composed of two types of primitive elements: combinatorial logic gates (`NOT`, `AND`, `OR`, `NAND`, `NOR`, `XOR` etc.), which process logic functions without memory, and sequential elements (flip-flops, latches, or registers), which can store data and are triggered by clock signals. Through timing closure, the circuit can be adjusted through layout improvement and netlist restructuring to modify path delays to make sure the outputs of logic gates arrive at the correct time relative to the clock signal.

integrated circuit (IC) designs have become increasingly complicated, with modern chips containing billions of transistors and highly interconnected logic. Every path in the design must satisfy its timing constraints, or the design may suffer from functional faults, unpredictable consequences, or system-level failure.

Timing closure is not a simple final validation step, but rather an iterative and comprehensive optimization process. It involves continual improvement of both the logical structure of the design and its physical implementation, such as adjusting gate's logical structure and refining placement and routing, in order to reliably meet all timing constraints across the entire chip.

## Overview

Clocked digital circuits must meet certain constraints to ensure proper operation. For example, the time delay along each path from the output of a D flip-flop, through combinatorial logic gates, then into the next D flip-flop input must satisfy (be less than) the time period between synchronizing clock pulses to the two flip flops. If this constraint is not met, so the delay through the elements is greater than the clock period, the circuit will not function correctly. Therefore, modifying the circuit to remove any timing failures is an important part of the logic design engineer's task.

The *critical path* refers to the longest path (in terms of delay) between any two sequential elements in a design. It defines the maximum delay of all register-to-register paths, and sets the minimum possible clock cycle time, which in turn limits the maximum speed of the chip. In simple design, the user can compute all possible path delays between elements manually, and adjust them until requirements are met. In modern designs with thousands to millions of elements this is impractical, and automation is required.

## Timing constraints

In the process of IC design, the IC layout should satisfy geometric constraints and timing constraints. Geometric constraints refer to physical design regulations and rules imposed by the assembly process, such as correct cell alignment and minimum wire spacing. Timing constraints refer to the timing requirements that all signal paths should satisfy. Usually, before the output of the signal from flip-flop at the clock edge, the input signal should remain stable for a period called the setup time. After the electromagnetic signal reaches the next flip-flop at the clock edge, the signal should remain stable in the storage element for some time, which is called hold time. This yields two types of timing constraints:

**Setup** **constraints (long-path constraints):**

These constraints specify the time length before the clock edge of flip-flop where the data input signal should stay steady, so that the data has enough time to propagate through a logic path and reach the next flip-flop before the next clock edge. If the path delay is too long, it may violate setup time constraints and cause problematic data to be latched.

**Hold constraints (short-path constraints)**:

These constraints specify the time length after the clock edge of flip-flop where the data input signal should stay stable. Violating a hold constraint can result in metastability or unwanted behaviors.

**Hold time constraint:** $t_{logic}>t_{h}-t_{c{-}q}$

**Setup time constraint:** $t_{logic}<t_{CLK}-t_{c{-}q}-t_{su}$

**Where:**

- $t_{logic}$ = combinational logic delay
- $t_{CLK}$ = clock period
- $t_{su}$ = setup time
- $t_{h}$ = hold time
- $t_{c{-}q}$ = clock-to-Q delay of the flip-flop

## Timing closure iterative process

Timing closure is a vital step that ensures that all signals reach their destinations by the required time, and the hold times are all satisfied, so the circuit works reliably. Designers start with the register-transfer level (RTL) abstraction and Verilog or VHDL code that describes the circuit. This is turned into a netlist, which is a collection of logic gates and connections, and used either to create the placement and routing of an IC, or to configure the FPGA hardware.

In both conventional ICs and FPGAs, both gate delays and wiring delays can vary considerably. If signals arrive too late, or too early, the design may fail timing. The timing constraints designers begin to define accurate and realistic timing constraints that reflect the system's performance goals, often in the Synopsys Design Constraint (SDC) format. These constraints may include clock period**,** input/output delays, multi-cycle paths, and setup/hold requirements. It's critical to analyze whether they are achievable, based on the logic architecture and path delays within the design. These constraints guide all downstream timing analysis and optimization processes.

## Problems in timing closure and static timing analysis

There are three main delays in the clocked synchronous circuit that are primarily considered:

**Gate delay** is the length of time it takes for a change in a gate's input to propagate to the output. It's often calculated as the time between a change at the input and the resulting change at the output.

**Wire delay** is also known as interconnect delay, meaning the time that takes for a data signal to propagate through metal wires (interconnect) between circuit element in a synchronous circuit. The delay is mostly caused by the resistance and capacitance of the wire.

**Clock skew** is the difference in arrival time of the same sourced clock signal at different parts of a synchronous circuit. When the clock signal propagates from its source, such as oscillator or clock generator, through many different paths in the circuit, the signal experience propagation delay, which caused the clock skew. In the graph below, the clock skew between points i and j is on a chip: $\delta (i,j)=t_{i}-t_{j}$ While position i and j can vary. The diagram illustrates the concept of clock skew, which refers to the difference in clock arrival times at different flip-flops on a chip. Ideally, all clock signals should reach their destinations simultaneously; however, due to variations in routing, load, and physical placement, this is rarely achieved.

After logic synthesis and constraints analysis, the design undergoes static timing analysis (STA), a process explicitly designed to evaluate whether the circuit meets its defined timing constraints. These tools (such as Cadence Tempus, Synopsys PrimeTime, and Intel Timing Analyzer) can evaluate all timing paths in the design without requiring simulation, making them ideal for scalable and exhaustive analysis. In STA, the combinational circuit can represent as directed acyclic graph (DAG) where nodes represent the gates and links represent the interconnect. Both are annotated with their corresponding delays. Typically initially the clock skew is assumed to be negligible. This will be re-visited after place, route, and clock tree synthesis.

During this process, the STA engine computes:

- **Path delays**: Total delay from one register to another through combinational logic.
- **Slack**: The difference between required arrival time and actual arrival time.
- **Critical paths**: The longest paths with the smallest (or zero) slack.
- **Violations**: Paths with negative slack, meaning they fail to meet timing.

Especially for slack, STA supposes the worst-case scenario where every gate transitions, and computes the slack for each node.

$\mathrm {Slack} =\mathrm {RAT} -\mathrm {AAT}$

Where:

- **RAT** = required arrival time
- **AAT** = actual arrival time

RAT is the required arrival time, meaning the latest time can transit in the required timing. AAT is the actual arrival time, meaning the latest actual transition time, and is defined at the output of every node. Negative slack at any input means the circuit doesn't meet timing, while positive slack at all inputs means the circuit meets timing.

## Physical design

Once the STA reports are generated, engineers can utilize timing optimization techniques, or design automation tools, to examine them to identify the critical or failing paths that need attention. They also optimize the physical layout by adjusting placement and routing. This loop repeats until all timing constraints are met.

Through logic synthesis and initial timing optimization, the physical layout of the chip should be mapped. Through placement, clock tree synthesis, and routing of these key steps, the physical designs are altered so that the timing behaviors can change significantly, and therefore reduce the path delays and enhance the timing in circuit.

### 1. Placement

The EDA tool assigns physical locations to each standard cell (logic gates, flip-flops, etc.) on the IC. Placement can reduce path delays by placing interconnected cells close to each other. Wiring is only estimated at this point.

### 2. Clock tree synthesis (CTS)

A balanced clock distribution network is built to deliver the clock signal to all sequential elements (flip-flops) evenly and synchronously. The CTS tries to minimize **clock skew** (difference in arrival time of the clock signal at different points) while controlling the clock latency (the delivery time of the clock signal to all sequential elements). It also tries to satisfy the maximum transition time and the maximum allowed capacitance to ensure the clock network meets design constraints. The clock skew affects hold and setup times. The clock skew is usually composed of local clock skew and global clock skew.

**Commonly there are three types of CTS:**

**2.1.Single point CTS**

A single point clock tree starts off from a single clock source and delivers the clock signal to all sequential elements in a tree structure. This method is easy to implement and is appropriate for low-frequency or multi-clock designs. Nevertheless, it will be unsuitable for high-frequency or large-scale designs because path asymmetry can lead to larger clock skew.

**2.2.Clock mesh**

A clock mesh dispatches the clock signal through a grid-like structure, providing enhanced clock balance and lesser skew, which is good for high-frequency designs. However, constructing a clock mesh means higher power and area overhead, and the design complexity will be increased.

**2.3.Multi-source CTS**

A multi-source clock tree integrates the advantages of single-point trees and clock meshes. The design is partitioned into multiple components, each with its own local clock source. This clock tree achieves low skew while reducing power and area consumption, making it well-suited for large-scale designs.

### 3. Routing

After placement and clock tree synthesis, the design automation tool creates wires to physically connect cells. The physical routing introduces actual parasitic resistance and capacitance effects, which can affect signal delay. Incorporating these parasitics enables more precise timing analysis. The routing can help with timing closure by giving the nets with the least slack the most direct (and hence fastest) routes.

## Timing optimization techniques

One common way to improve the circuit performance is to use timing optimization techniques, such as inserting a register in between the combinational path of the critical path. This might improve the performance but increases the total latency (maximum number of registers from input to output path) of the circuit.

The actual timing optimization techniques usually include physical synthesis, which can eliminate negative slack by using a set of timing optimizations. The physical synthesis includes creating timing budgets and implementing timing corrections. Usually, the timing budgets contain allocating target delays along paths or nets during placement, routing stages, and timing correction operations. The timing corrections include:

**Gate sizing:**

Gate sizing involves replacing logic gates with equivalent versions of different drive strengths. Larger gates can drive larger loads faster, reducing delays in critical paths. This technique balances speed against area and power.

Suppose a logic gate comes in three sizes, *a*, *b*, and *c*, where $Size(Vc)>Size(Vb)>Size(Va)$ . The gates with larger sizes have smaller output resistance. Then $R_{out}(V_{c})<R_{out}(V_{b})<R_{out}(V_{a})$ . According to the RC delay approximation, $t=R_{out}\times C_{load}$ , where **t** represents propagation delay, $R_{out}$ represents output resistance, and $C_{load}$ represents load capacitances. Therefore when load capacitances are large, larger logic gates can easily drive larger load capacitances: $t(V_{c})<t(V_{b})<t(V_{a})$ .

The drawbacks of larger gates, however, usually include higher capacitance on the input, more insertion delay, and higher power consumption. Therefore, when load capacitances are small, smaller logic gates are preferred as long as they can meet the timing constraints.

**Buffer insertion**:

Used to break long wires and reduce RC (resistance-capacitance) delays, especially in high fan-out or physically distant connections. Buffers can also help in adjusting path timing to fix hold violations. Buffer insertion must leave the logic function unchanged. This is typically implemented by inserting an even number of inverting buffers, or using non-inverting buffers composed of two serially connected inverters.

**Improvements:**

**1: Speeding up the circuit or serving as delay elements**

Buffers can reduce path delay by easily driving signals through long wires and on large load capacitances. In critical paths, inserting a buffer helps reduce resistance and improve signal propagation. Alternatively, buffers can also be intentionally placed to introduce a fixed delay for timing alignment**.**

### 2. Changing transition times

A signal with a slow rise/fall time can cause unreliable switching and timing violations. Buffers sharpen the **signal edges**, improving the slope of the transitions and resulting in more stable digital behavior. This helps prevent glitches, short-circuit current, and false logic triggering.

### 3. Shielding capacitive load

If a logic gate drives many other gates or long wires, the total load capacitances become large. This large load slows down the gate’s output response. Inserting a buffer between the gate and its heavy load offloads the burden, allowing the original gate to drive only the buffer and not the full load directly.

However, the drawbacks may include increased area usage and increased power consumption.

**Netlist restructuring**:

**Netlist restructuring** refers to the process of modifying the structure of an existing gate-level circuit **without changing its logical functionality**. It focuses on optimizing timing, area, or power by reorganizing or transforming how existing gates are connected or represented. The transformations include:

**Cloning**: Duplicating gates to reduce load capacitances or balance load across multiple paths.

**Redesigning the input/output tree**: Changing how signals are distributed or received to improve timing or reduce congestion.

**Swapping commutative pins**: Reordering inputs of commutative gates (like AND, OR) to optimize critical paths and change connections.

**Gate decomposition**: Breaking complex gates into simpler forms, such as converting AND-OR logic into NAND-NAND logic by using CMOS inverters to simplify the logic gates and reduce path delay.

**Boolean restructuring**: Applying Boolean algebra rules to simplify or re-express logic equations, often minimizes path delay or leads to smaller implementations.

### Reverse transformations are also possible

Operations such as gate downsizing, merging, or simplifying previously expanded logic structures can also be performed if it benefits overall design metrics (e.g., area or power).

These techniques are often applied automatically by physical synthesis and place-and-route tools (such as Synopsys IC compiler, Cadence Innovus, or Intel Quartus), but can also be manually guided by designers through constraints and optimization directives.

## Design flow

**Utilize STA in iterative verification and validation:**

After the routing steps are completed, the physical details of the design including wire lengths, capacitances, and resistance will be examined and determined. Conduct thorough functional verification and validation of the design such as STA to guarantee the integrity of function of timing optimizations, help to identify the timing violations and delay, and verify the effectiveness of the recent timing closure and optimization. Also, the designers can use simulation, verification, and hardware testing to validate the design's functionality and performance. If the circuit fails to meet the timing then the whole circuit will be placed at the STA process from the start iteratively.

**Post-implementation timing analysis:**

When the design is completed on the FPGA, post-implementation timing analysis validates that all timing goals are met. This analysis acts as a final examination of timing closure confirms the successful timing closure process and accounts for any implementation-specific factors.

## Examples of commercial tools implementing timing closure

Many logic circuit changes, such as timing optimization techniques, are automatically handled by the user's EDA tools guided by timing constraint directives prepared by a designer. A design is said to have achieved timing closure when the design has reached the end of the flow and all its timing requirements are satisfied.

As of 2026 all major design steps, such as synthesis, placement, and routing, need to be timing-aware for a design to meet its timing requirements properly, but with older technologies only logic synthesis EDA tools were timing aware.

Even though timing awareness was extended to all these steps starting from well-established principles used for logic synthesis, the logic phase and the physical phase of the timing closure process are still handled by different design teams and different EDA tools. Design Compiler by Synopsys, Encounter RTL Compiler by Cadence Design Systems, and BlastCreate by Magma Design Automation are examples of logic synthesis tools. IC Compiler by Synopsys, SoC Encounter by Cadence Design Systems, and Blast Fusion by Magma Design Automation are examples of tools capable of timing-aware placement, clock tree synthesis, and routing and therefore used for physical timing closure.

Some FPGA tools utilize machine learning programs, such as InTime by Plunify, to find an optimum set of FPGA synthesis, map, place and route tool configuration parameters that ensures the circuit will close timing. A timing requirement needs to be translated into a static timing constraint for an EDA tool to be able to handle it.

Recently, the timing closure process has gradually integrated logic synthesis and physical implementation under unified platforms to process optimization. Tools such as Fusion Compiler by Synopsys and the Genus-Innovus flow by Cadence offer end-to-end solutions combining logic synthesis, placement, clock tree synthesis, and routing within a single environment. Additionally, open-source toolchains like OpenROAD and OpenSTA have gained traction in academia and startup prototyping for their ability to support timing-aware design closure workflows. These modern tools are designed to encounter the growing complexity of nanometer-scale circuits by automating trade-offs between performance, area, and power (PPA), and enabling earlier detection and resolution of timing violations in the RTL-to-GDSII design flow.
