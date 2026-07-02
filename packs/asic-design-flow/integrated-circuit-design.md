---
title: "Integrated circuit design"
source: https://en.wikipedia.org/wiki/Integrated_circuit_design
domain: asic-design-flow
license: CC-BY-SA-4.0
tags: asic design flow, chip tape-out, semiconductor ip core, eda sign-off
fetched: 2026-07-02
---

# Integrated circuit design

**Integrated circuit design**, **semiconductor design**, **chip design** or **IC design**, is a sub-field of electronics engineering, encompassing the particular logic and circuit design techniques required to design integrated circuits (ICs). An IC consists of miniaturized electronic components built into an electrical network on a monolithic semiconductor substrate by photolithography.

IC design can be divided into the broad categories of digital and analog IC design. Digital IC design is to produce components such as microprocessors, FPGAs, memories (RAM, ROM, and flash) and digital ASICs. Digital design focuses on logical correctness, maximizing circuit density, and placing circuits so that clock and timing signals are routed efficiently. Analog IC design also has specializations in power IC design and RF IC design. Analog IC design is used in the design of op-amps, linear regulators, phase locked loops, oscillators and active filters. Analog design is more concerned with the physics of the semiconductor devices, such as gain, matching, power dissipation, and resistance. Fidelity of analog signal amplification and filtering is usually critical, and as a result, analog ICs use larger area active devices than digital designs and are usually less dense in circuitry.

Modern ICs are enormously complicated. An average desktop computer chip, as of 2026, has over 20 billion transistors. The rules for what can and cannot be manufactured are also extremely complex. Common IC processes of 2015 have more than 500 rules. Furthermore, since the manufacturing process itself is not completely predictable, designers must account for its statistical nature. The complexity of modern IC design, as well as market pressure to produce designs rapidly, has led to the extensive use of tools in the IC design process, known as electronic design automation (EDA) tools. The design of some processors has become complicated enough to be difficult to fully test, and this has caused problems at large cloud providers. In short, designing an IC using EDA software consists of designing, testing, and verifying the instructions that the IC will carry out.

## Fundamentals

Integrated circuit design involves the creation of electronic components, such as transistors, resistors, capacitors and the interconnection of these components onto a piece of semiconductor, typically silicon. A method to isolate the individual components formed in the substrate is necessary since the substrate silicon is conductive and often forms an active region of the individual components. The two common methods are p-n junction isolation and dielectric isolation. Attention must be given to power dissipation of transistors and interconnect resistances and current density of the interconnect, contacts and vias, since ICs contain very tiny devices compared to discrete components, where such concerns are less of an issue. Electromigration in metallic interconnect and ESD damage to the tiny components are also of concern. Finally, the physical layout of certain circuit subblocks is typically critical, in order to achieve the desired speed of operation, to segregate noisy portions of an IC from quiet portions, to balance the effects of heat generation across the IC, or to facilitate the placement of connections to circuitry outside the IC.

### Design flow

A typical IC design cycle involves several steps:

1. System specification
  1. Feasibility study and die size estimate
  2. Function analysis
2. Architectural or system-level design
3. Logic design
  1. Analogue design, simulation, and layout
  2. Digital design and simulation
  3. System simulation, emulation, and verification
4. Circuit design
  1. Digital design synthesis
  2. Design for testing and automatic test pattern generation
  3. Design for manufacturability
5. Physical design
  1. Floorplanning
  2. Place and route
  3. Parasitic extraction
6. Physical verification and signoff
  1. Static timing
  2. Co-simulation and timing
7. Mask data preparation (layout post-processing)
  1. Chip finishing with tape out
  2. Reticle layout
  3. Layout-to-mask preparation
8. Reticle fabrication
9. Photomask fabrication
10. Wafer fabrication
11. Packaging
12. Die test
  1. Post silicon validation and integration
  2. Device characterization
  3. Tweak (if necessary)
13. Chip deployment
  1. Datasheet generation (usually a PDF file)
  2. Ramp up
  3. Production
  4. Yield analysis / warranty analysis reliability
  5. Failure analysis on any returns
  6. Plan for next-generation chip using production information if possible

Focused ion beams may be used during chip development to establish new connections in a chip.

### Summary

Roughly speaking, digital IC design can be divided into three parts.

- Electronic system-level design: This step creates the user functional specification. The user may use a variety of languages and tools to create this description. Examples include a C/C++ model, VHDL, SystemC, SystemVerilog, transaction-level models, Simulink, and MATLAB.
- RTL design: This step converts the user specification (what the user wants the chip to do) into a register transfer level (RTL) description. The RTL describes the exact behavior of the digital circuits on the chip, as well as the interconnections to inputs and outputs.
- Physical circuit design: This step takes the RTL and a library of available logic gates (standard cell library) and creates a chip design. This step involves use of IC layout editor, layout and floor planning, figuring out which gates to use, defining places for them, and wiring (clock timing synthesis, routing) them together.

Note that the second step, RTL design, is responsible for the chip doing the right thing. The third step, physical design, does not affect the functionality at all (if done correctly) but determines how fast the chip operates and how much it costs.

A standard cell normally represents a single logic gate, a diode or simple logic components such as flip-flops, or logic gates with multiple inputs. The use of standard cells allows the chip's design to be split into logical and physical levels. A fabless company would normally only work on the logical design of a chip, determining how cells are connected and the functionality of the chip, while following design rules from the foundry the chip will be made in, while the physical design of the chip, the cells themselves, are normally done by the foundry and it comprises the physics of the transistor devices and how they are connected to form a logic gate. Standard cells allow chips to be designed and modified more quickly to respond to market demands, but this comes at the cost of lower transistor density in the chip and thus larger die sizes.

Foundries supply libraries of standard cells to fabless companies, for design purposes and to allow manufacturing of their designs using the foundry's facilities. A process design kit (PDK) may be provided by the foundry and it may include the standard cell library as well as the specifications of the cells, and tools to verify the fabless company's design against the design rules specified by the foundry as well as simulate it using the foundry's cells. PDKs may be provided under non-disclosure agreements. Macros/macrocells/macro blocks, macrocell arrays and IP blocks have greater functionality than standard cells, and are used similarly. There are soft macros and hard macros. Standard cells are usually placed following standard cell rows.

## Design lifecycle

The integrated circuit (IC) development process starts with defining product requirements, progresses through architectural definition, implementation, bringup and finally production. The various phases of the integrated circuit development process are described below. Although the phases are presented here in a straightforward fashion, in reality, there is iteration and these steps may occur multiple times.

### Requirements

Before an architecture can be defined, some high-level product goals must be defined. The requirements are usually generated by a cross-functional team that addresses market opportunity, customer needs, feasibility, and much more. This phase should result in a product requirements document.

### Architecture

The *architecture* defines the fundamental structure, goals and principles of the product. It defines high-level concepts and the intrinsic value proposition of the product. Architecture teams take into account many variables and interface with many groups. People creating the architecture generally have a significant amount of experience dealing with systems in the area for which the architecture is being created. The work product of the architecture phase is an architectural specification.

### Micro-architecture

The micro-architecture is a step closer to the hardware. It implements the architecture and defines specific mechanisms and structures for achieving that implementation. The result of the micro-architecture phase is a micro-architecture specification that describes the methods used to implement the architecture.

### Implementation

In the implementation phase, the design itself is created using the micro-architectural specification as the starting point. This involves low-level definition and partitioning, writing code, entering schematics and verification. This phase ends with a design reaching tapeout.

### Bringup

After a design is created, taped-out and manufactured, actual hardware, 'first silicon', is received, which is taken into the lab where it goes through *bringup*. Bringup is the process of powering, testing and characterizing the design in the lab. Numerous tests are performed, starting from very simple tests such as ensuring that the device will power on, to much more complicated tests which try to stress the part in various ways. The result of the bringup phase is documentation of characterization data (how well the part performs to spec) and errata (unexpected behavior).

### Productization

Productization is the task of taking a design from engineering into mass production manufacturing. Although a design may have successfully met the specifications of the product in the lab during the bringup phase, there are many challenges that product engineers face when trying to mass-produce those designs. The IC must be ramped up to production volumes with an acceptable yield. The goal of the productization phase is to reach mass production volumes at an acceptable cost.

### Sustaining

Once a design is mature and has reached mass production, it must be sustained. The process must be continually monitored and problems dealt with quickly to avoid a significant impact on production volumes. The goal of sustaining is to maintain production volumes and continually reduce costs until the product reaches end of life.

## Design process

### Microarchitecture and system-level design

The initial chip design process begins with system-level design and microarchitecture planning. Within IC design companies, management and often analytics will draft a proposal for a design team to start the design of a new chip to fit into an industry segment. Upper-level designers will meet at this stage to decide how the chip will operate functionally. This step is where an IC's functionality and design are decided. IC designers will map out the functional requirements, verification testbenches, and testing methodologies for the whole project, and will then turn the preliminary design into a system-level specification that can be simulated with simple models using languages like C++ and MATLAB and emulation tools. For pure and new designs, the system design stage is where an instruction set and operation are planned out, and in most chips, existing instruction sets are modified for newer functionality. Design at this stage often involves statements such as *encodes in the MP3 format* or *implements IEEE floating-point arithmetic*. At later stages in the design process, each of these innocent-looking statements expands to hundreds of pages of textual documentation.

### RTL design

Upon agreement of a system design, RTL designers then implement the functional models in a hardware description language like Verilog, SystemVerilog, or VHDL. Using digital design components like adders, shifters, and state machines as well as computer architecture concepts like pipelining, superscalar execution, and branch prediction, RTL designers will break a functional description into hardware models of components on the chip working together. Each of the simple statements described in the system design can easily turn into thousands of lines of RTL code, which is why it is extremely difficult to verify that the RTL will do the right thing in all the possible cases that the user may throw at it.

To reduce the number of functionality bugs, a separate hardware verification group will take the RTL and design testbenches and systems to check that the RTL actually is performing the same steps under many different conditions, classified as the domain of functional verification. Many techniques are used, none of them perfect but all of them useful – extensive logic simulation, formal methods, hardware emulation, lint-like code checking, code coverage, and so on. Verification such as that done by emulators can be carried out in FPGAs or special processors, and emulation replaced simulation. Simulation was initially done by simulating logic gates in chips, but later on, RTLs in chips were simulated instead. Simulation is still used when creating analog chip designs. Prototyping platforms are used to run software on prototypes of the chip design while it is under development using FPGAs but are slower to iterate on or modify and can't be used to visualize hardware signals as they would appear in the finished design.

A tiny error here can make the whole chip useless, or worse. The famous Pentium FDIV bug caused the results of a division to be wrong by at most 61 parts per million, in cases that occurred very infrequently. No one even noticed it until the chip had been in production for months. Yet Intel was forced to offer to replace, for free, every chip sold until they could fix the bug, at a cost of $475 million (US).

### Physical design

RTL is only a behavioral model of the actual functionality of what the chip is supposed to operate under. It has no link to a physical aspect of how the chip would operate in real life at the materials, physics, and electrical engineering side. For this reason, the next step in the IC design process, physical design stage, is to map the RTL into actual geometric representations of all electronic devices, such as capacitors, resistors, logic gates, and transistors that will go on the chip.

The main steps of physical design are listed below. In practice, there is not a straightforward progression - considerable iteration is required to ensure all objectives are met simultaneously. This is a difficult problem in its own right, called design closure.

- Logic synthesis: The RTL is mapped into a gate-level netlist in the target technology of the chip.
- Floorplanning: The RTL of the chip is assigned to gross regions of the chip, input/output (I/O) pins are assigned and large objects (arrays, cores, etc.) are placed.
- Placement: The gates in the netlist are assigned to non-overlapping locations on the die area.
- Logic/placement refinement: Iterative logical and placement transformations to close performance and power constraints.
- Clock insertion: Clock signal wiring is (commonly, clock trees) introduced into the design.
- Routing: The wires that connect the gates in the netlist are added.
- Postwiring optimization: Performance (timing closure), noise (signal integrity), and yield (design for manufacturability) violations are removed.
- Design for manufacturability: The design is modified, where possible, to make it as easy and efficient as possible to produce. One common improvement, for example, is to make the areal density of features as uniform as possible across the chip. This is achieved by adding extra vias or adding dummy metal/diffusion/poly layers wherever possible while complying to the design rules set by the foundry.
- Final checking: Since errors are expensive, time-consuming and hard to spot, extensive error checking is the rule, making sure the mapping to logic was done correctly, and checking that the manufacturing rules were followed faithfully.
- Chip finishing with tapeout and mask generation: the design data is turned into photomasks in mask data preparation.

## Analog design

Before the advent of the microprocessor and software-based design tools, analog ICs were designed using hand calculations and process kit parts. These ICs were low complexity circuits, for example, op-amps, usually involving no more than ten transistors and few connections. An iterative trial-and-error process and "overengineering" of device size was often necessary to achieve a manufacturable IC. Reuse of proven designs allowed progressively more complicated ICs to be built upon prior knowledge. When inexpensive computer processing became available in the 1970s, computer programs were written to simulate circuit designs with greater accuracy than was practical using hand calculation. The first circuit simulator designed specifically for ICs was called SPICE (Simulation Program with Integrated Circuits Emphasis), released in 1973. Its successors still dominate the analog design market. These computerized circuit simulation tools enable greater IC design complexity than hand calculations can achieve, making the design of analog ASICs practical.

As many functional constraints must be considered in analog design, manual design is still widespread today, in contrast to digital design which is highly automated, including automated routing and synthesis. As a result, modern design flows for analog circuits are characterized by two different design styles – top-down and bottom-up. The top-down design style makes use of optimization-based tools similar to conventional digital flows. Bottom-up procedures re-use “expert knowledge” with the result of solutions previously conceived and captured in a procedural description, imitating an expert's decision. An example are cell generators, such as PCells.

### Coping with variability

A challenge most critical to analog IC design involves the variability of the individual devices built on the semiconductor chip. Unlike board-level circuit design, which permits the designer to select devices that have each been tested and binned according to value, the device values on an IC can vary widely in ways that are not under the control of the designer. For example, identically drawn IC resistors can vary ±20% and β (gain) of an integrated BJT can vary from 20 to 100. In the latest CMOS processes, β of vertical PNP transistors can even go below 1. To add to the design challenge, device properties often vary between each processed semiconductor wafer. Device properties can even vary significantly across each individual IC due to doping gradients. The underlying cause of this variability is that many semiconductor devices are highly sensitive to uncontrollable random variances in the process. Slight changes to the amount of diffusion time, uneven doping levels, etc., can have large effects on device properties.

Some design techniques used to reduce the effects of the device variation are:

- Using the ratios of resistors, which do match closely, rather than the absolute resistor value.
- Using devices with matched geometrical shapes so they have matched variations.
- Making devices large so that statistical variations become an insignificant fraction of the overall device property.
- Segmenting large devices, such as resistors, into parts and interweaving them to cancel variations.
- Using common centroid device layout to cancel variations in devices which must match closely (such as the transistor differential pair of an op amp).

## Vendors

The three largest companies selling electronic design automation tools are Synopsys, Cadence, and Mentor Graphics (now Siemens EDA).
