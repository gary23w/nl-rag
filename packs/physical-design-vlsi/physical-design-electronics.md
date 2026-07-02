---
title: "Physical design (electronics)"
source: https://en.wikipedia.org/wiki/Physical_design_(electronics)
domain: physical-design-vlsi
license: CC-BY-SA-4.0
tags: physical design flow, vlsi layout, integrated circuit layout, design rule checking
fetched: 2026-07-02
---

# Physical design (electronics)

In integrated circuit design, **physical design** is a step in the standard design cycle which follows after the circuit design. At this step, circuit representations of the components (devices and interconnects) of the design are converted into geometric representations of shapes which, when manufactured in the corresponding layers of materials, will ensure the required functioning of the components. This geometric representation is called an integrated circuit layout. This step is usually split into several sub-steps, which include both design and verification and validation of the layout.

Modern day Integrated Circuit (IC) design is split up into *Front-end Design using HDLs* and *Back-end Design* or *Physical Design*. The inputs to physical design are (i) a netlist, (ii) library information on the basic devices in the design, and (iii) a technology file containing the manufacturing constraints. Physical design is usually concluded by *Layout Post Processing*, in which amendments and additions to the chip layout are performed. This is followed by the wafer fabrication, the manufacturing process whereby designs are transferred via photomasks onto silicon dies which are then packaged into ICs.

Each of the phases mentioned above has design flows associated with them. These design flows lay down the process and guide-lines/framework for that phase. The physical design flow uses the technology libraries that are provided by the fabrication houses. These technology files provide information regarding the type of silicon wafer used, the standard cells used, the layout rules (like DRC in VLSI), etc.

The physical design engineer (sometimes called physical engineer or physical designer) is responsible for the design and layout (routing), specifically in ASIC/FPGA design.

## Divisions

Typically, the IC physical design is categorized into full custom, semi-custom, gate array, and FPGA design.

- Full-Custom: Designer has full flexibility on the layout design; predefined cells may or may not be used. The designer has full control over both the design and placement of the cells, and over the routing connecting them.
- Semi-Custom: Pre-designed library cells (preferably tested with DFM) are used, and the designer has flexibility in placement of the cells and routing.
- Gate array (and similar technologies): The library cells are fixed, and possibly pre-fabricated. The designer controls only the routing.
- Field-programmable gate array (FPGA): Both the cell library and the routing are fixed. The designer controls the settings of switches that connect various logic units to the pre-defined wires.

The design flow used depends strongly on the requirements. Full custom design is the slowest and most expensive, but offers potentially the highest performance. Semi-custom or ASIC is somewhat easier as the components have been pre-characterized, although in some cases the designer has the flexibility to design/modify design blocks from vendor provided libraries in ASIC. This flexibility is missing for flows using FPGAs (e.g. Altera or Xilinx), which are the easiest to implement, as the chips are already fabricated. These offer the advantage of no fabrication time (a chip designed today can be running tomorrow) and by far the easiest debugging, but have the lowest performance and the highest cost per gate.

## ASIC physical design flow

The main steps in the ASIC physical design flow are, starting with the post-synthesis netlist:

- Floorplanning
- Partitioning
- Placement
- Clock-tree Synthesis (CTS)
- Routing
- Physical Verification
- Layout Post Processing with Mask data preparation

These steps are just the basics. There are detailed PD flows that are used depending on the tools used and the methodology/technology. Some of the tools/software commonly used in the back-end design are:

- Cadence (Cadence Encounter RTL Compiler, Encounter Digital Implementation, Cadence Voltus IC Power Integrity Solution, Cadence Tempus Timing Signoff Solution)
- Synopsys (Design Compiler, IC Compiler II, IC Validator, PrimeTime, PrimePower, PrimeRail)
- Magma (BlastFusion, etc.)
- Mentor Graphics (Olympus SoC, IC-Station, Calibre)

The ASIC physical design flow uses the technology libraries that are provided by the fabrication houses. Technologies are commonly classified according to minimal feature size. Standard sizes, in the order of miniaturization, are *2μm, 1μm, 0.5μm, 0.35μm, 0.25μm, 180nm, 130nm, 90nm, 65nm, 45nm, 28nm, 22nm, 18nm, 14nm, etc.* They may be also classified according to major manufacturing approaches: n-Well process, twin-well process, SOI process, etc.

## Design netlist

Physical design is based on a netlist which is the end result of the logic synthesis process. Synthesis converts the RTL design, usually coded in VHDL or Verilog HDL, to gate-level descriptions which the next set of tools can read and understand. This netlist contains information on the cells used, their interconnections, area used, and other details. Typical synthesis tools are:

- Cadence RTL Compiler/Build Gates/Physically Knowledgeable Synthesis (PKS)
- Synopsys Design Compiler

During the synthesis process, constraints are applied to ensure that the design meets the specified functionality and speed. Only after the netlist is verified for functionality and timing it is sent for the physical design flow. Note however that timing at this point is only an estimate, as the parasitics from the physical design are not yet known.

## Steps

### Partitioning

Partitioning is a process of dividing the chip into small blocks. This is done mainly to separate different functional blocks and also to make placement and routing easier. Partitioning can be done in the RTL design phase when the design engineer partitions the entire design into sub-blocks and then proceeds to design each module. These modules are linked together in the main module called the TOP LEVEL module. This kind of partitioning is commonly referred to as Logical Partitioning. The goal of partitioning is to split the circuit such that the number of connections between partitions is minimized.

### Floorplanning

The second step in the physical design flow is *floorplanning*. Floorplanning is the process of identifying structures that should be placed close together, and allocating space for them in such a manner as to meet the sometimes conflicting goals of available space (cost of the chip), required performance, and the desire to have everything close to everything else.

Based on the area of the design and the hierarchy, a suitable floorplan is decided upon. Floorplanning takes into account the macros used in the design, memory, other IP cores and their placement needs, the routing possibilities, and also the area of the entire design. Floorplanning also determines the IO structure and aspect ratio of the design. A bad floorplan will lead to wastage of die area and routing congestion.

In many design methodologies, *area* and *speed* are the subjects of trade-offs. This is due to limited routing resources, as the more resources used, the slower the operation. Optimizing for minimum area allows the design both to use fewer resources, and for greater proximity of the sections of the design. This leads to shorter interconnect distances, fewer routing resources used, faster end-to-end signal paths, and even faster and more consistent place and route times. Done correctly, there are no negatives to floorplanning.

As a general rule, data-path sections benefit most from floorplanning, whereas random logic, state machines, and other non-structured logic can safely be left to the placer section of the place and route software.

Data paths are typically the areas of the design where multiple bits are processed in parallel with each bit being modified the same way with maybe some influence from adjacent bits. Example structures that make up data paths are Adders, Subtractors, Counters, Registers, and Muxes.

### Placement

Earlier stages, when the placement is unknown, generally use a simple Wire Load Model (WLM), often an estimate based on fanout. Placement uses more accurate RC values, typically estimated from the bounding box of all pins of a net, but without detailed routing.

Placement is performed in four optimization phases:

1. Pre-placement optimization
2. In placement optimization
3. Post Placement Optimization (PPO) before clock tree synthesis (CTS)
4. PPO after CTS.

- Pre-placement Optimization optimizes the netlist before placement, HFNs (High Fanout Nets) are collapsed. It can also downsize the cells.
- In-placement optimization re-optimizes the logic based on estimated wire loads. This can perform cell sizing, cell moving, cell bypassing, net splitting, gate duplication, buffer insertion, area recovery. Optimization performs iteration of setup fixing, incremental timing and congestion driven placement.
- Post placement optimization before CTS performs netlist optimization with ideal clocks. It can fix setup, hold, max trans/cap violations. It can do placement optimization based on global routing. It re-does HFN synthesis.
- Post placement optimization after CTS optimizes timing with propagated clock. It tries to preserve clock skew.

### Clock tree synthesis

The goal of **clock tree synthesis** (**CTS**) is to insure proper operation of a clocked circuit, primarily by minimizing skew while controlling insertion delay. The clock is a single logical signal of high fanout before CTS, as shown in the picture. After CTS setup times should be met, and hold slack should be improved. A clock tree begins at a source (normally defined in an .sdc file) and ends at the clock pins of flip-flops. There are two types of stop pins known as *ignore* pins and *sync* pins. 'Don't touch' circuits and pins in front end (logic synthesis) are treated as 'ignore' circuits or pins at back end (physical synthesis). 'Ignore' pins are ignored for timing analysis. If the clock is divided into multiple phases then a separate skew analysis is necessary.

- Global skew is the skew between any two clocked pins, without considering any logic relationship.
- Local skew is the skew between two clocked pins that are connected through logic.
- Useful skew is defined as the condition where the clock is skewed intentionally to improve setup slack.

Rigidity is the term coined in Astro to indicate the relaxation of constraints. Higher the rigidity means tighter constraints.

In **clock tree optimization** (CTO) clock can be shielded so that noise is not coupled to other signals. But shielding increases area by 12 to 15%. Since the clock signal is global in nature the same metal layer used for power routing is used for clock also. CTO is achieved by buffer sizing, gate sizing, buffer relocation, level adjustment and HFN synthesis. We try to improve setup slack in pre-placement, in placement and post placement optimization before CTS stages while neglecting hold slack. In post placement optimization after CTS hold slack is improved. As a result of CTS lot of buffers are added. Generally for 100k gates around 650 buffers are added.

### Routing

There are two types of routing in the physical design process, global routing and detailed routing. Global routing allocates routing resources that are used for connections. It also does track assignment for a particular net.

Detailed routing does the actual connections. Different constraints that are to be taken care during the routing are DRC, wire length, timing etc.

### Physical verification

Physical verification checks the correctness of the generated layout design. This includes verifying that the layout

- Complies with all technology requirements – Design rule checking (DRC)
- Is consistent with the original netlist – Layout versus schematic (LVS)
- Has no antenna effects – Antenna Rule Checking
- This also includes density verification at the full chip level...Cleaning density is a very critical step in the lower technology nodes
- Complies with all electrical requirements – Electrical Rule Checking (ERC).

### Layout post processing

Layout Post Processing, also known mask data preparation, often concludes physical design and verification. It converts the physical layout (polygons) into mask data (instructions for the photomask writer). It includes

- Chip finishing, such as inserting company/chip labels and final structures (e.g., seal ring, filler structures),
- Generating a reticle layout with test patterns and alignment marks,
- Layout-to-mask preparation that extends layout data with graphics operations (e.g., resolution enhancement technologies, RET) and adjusts the data to mask production devices (photomask writer).
