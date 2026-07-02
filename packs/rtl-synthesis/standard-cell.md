---
title: "Standard cell"
source: https://en.wikipedia.org/wiki/Standard_cell
domain: rtl-synthesis
license: CC-BY-SA-4.0
tags: rtl synthesis, logic synthesis, technology mapping, gate netlist
fetched: 2026-07-02
---

# Standard cell

In semiconductor design, **standard-cell methodology** is a method of designing application-specific integrated circuits (ASICs) with mostly digital-logic features. Standard-cell methodology is an example of design abstraction, whereby a low-level very-large-scale integration (VLSI) layout is encapsulated into an abstract logic representation (such as a NAND gate).

Cell-based methodology – the general class to which standard cells belong – makes it possible for one designer to focus on the high-level (logical function) aspect of digital design, while another designer focuses on the implementation (physical) aspect. Along with semiconductor manufacturing advances, standard-cell methodology has helped designers scale ASICs from comparatively simple single-function ICs (of several thousand gates), to complex multi-million gate system-on-a-chip (SoC) devices.

## Construction of a standard cell

A standard cell is a group of transistor and interconnect structures that provides a Boolean logic function (e.g., AND, OR, XOR, XNOR, inverters) or a storage function (flipflop or latch). The simplest cells are direct representations of the elemental NAND, NOR, and XOR Boolean function, although cells of much greater complexity are commonly used (such as a 2-bit full-adder, or muxed D-input flipflop.) The cell's Boolean logic function is called its *logical view*: functional behavior is captured in the form of a truth table or Boolean algebra equation (for combinational logic), or a state transition table (for sequential logic).

Usually, the initial design of a standard cell is developed at the transistor level, in the form of a *transistor netlist* or *schematic* view. The netlist is a nodal description of transistors, of their connections to each other, and of their terminals (ports) to the external environment. A schematic view may be generated with a number of different computer-aided design (CAD) or electronic design automation (EDA) programs that provide a graphical user interface (GUI) for this netlist generation process. Designers use additional CAD programs such as SPICE to simulate the electronic behavior of the netlist, by declaring input stimulus (voltage or current waveforms) and then calculating the circuit's time domain (analog) response. The simulations verify whether the netlist implements the desired function and predict other pertinent parameters, such as power consumption or signal propagation delay.

Since the logical and netlist views are only useful for abstract (algebraic) simulation, and not device fabrication, the physical representation of the standard cell must be designed too. Also called the *layout view*, this is the lowest level of design abstraction in common design practice. From a manufacturing perspective, the standard cell's VLSI layout is the most important view, as it is closest to an actual "manufacturing blueprint" of the standard cell. The layout is organized into *base layers*, which correspond to the different structures of the transistor devices, and *interconnect wiring layers* and *via layers*, which join together the terminals of the transistor formations. The *interconnect wiring layers* are usually numbered and have specific *via* layers representing specific connections between each sequential layer. Non-manufacturing layers may also be present in a layout for purposes of design automation, but many layers used explicitly for place and route (PNR) CAD programs are often included in a separate but similar *abstract* view. The abstract view often contains much less information than the layout and may be recognizable as a Library Exchange Format (LEF) file or an equivalent.

After a layout is created, additional CAD tools are often used to perform a number of common validations. A design rule check (DRC) is done to verify that the design meets foundry and other layout requirements. A parasitic extraction (PEX) then is performed to generate a PEX-netlist with parasitic properties from the layout. The nodal connections of that netlist are then compared to those of the schematic netlist with a *layout vs schematic* (LVS) procedure to verify that the connectivity models are equivalent.

The PEX-netlist may then be simulated again (since it contains parasitic properties) to achieve more accurate timing, power, and noise models. These models are often *characterized* (contained) in a Synopsys Liberty format, but other Verilog formats may be used as well.

Finally, powerful place and route (PNR) tools may be used to pull everything together and *synthesize* (generate) very-large-scale integration (VLSI) layouts, in an automated fashion, from higher level design netlists and floor-plans.

Additionally, a number of other CAD tools may be used to validate other aspects of the cell views and models. And other files may be created to support various tools that utilize the standard cells for a plethora of other reasons. All of these files that are created to support the use of all of the standard-cell variations are collectively known as a standard-cell library.

For a typical Boolean function, there are many different functionally equivalent transistor netlists. Likewise, for a typical netlist, there are many different layouts that fit the netlist's performance parameters. The designer's challenge is to minimize the manufacturing cost of the standard cell's layout (generally by minimizing the circuit's die area), while still meeting the cell's speed and power performance requirements. Consequently, integrated circuit layout is a highly labor-intensive job, despite the existence of design tools to aid this process.

## Library

A standard-cell library is a collection of low-level electronic logic functions such as AND, OR, NOT, flip-flops, latches, and buffers. These cells are realized as fixed-height, variable-width full-custom cells. The key aspect with these libraries is that they are of a fixed height, which enables them to be placed in rows, easing the process of automated digital layout. The cells are typically optimized full-custom layouts, which minimize delays and area.

A typical standard-cell library contains two main components:

1. Library database - consists of a number of views often including layout, schematic, symbol, abstract, and other logical or simulation views. From this, various information may be captured in a number of formats including the Cadence LEF format, and the Synopsys Milkyway format, which contain reduced information about the cell layouts, sufficient for automated place and route tools.
2. Timing abstract - generally in Liberty format, to provide functional definitions, timing, power, and noise information for each cell.

A standard-cell library may also contain the following additional components:

- A full layout of the cells
- SPICE models of the cells
- Verilog models or VHDL-VITAL models
- parasitic extraction models
- DRC rule decks

An example is a simple XOR logic gate, which can be formed from OR, NOT and AND gates.

## Application of standard cell

Strictly speaking, a 2-input NAND or NOR function is sufficient to form any arbitrary Boolean function set. But in modern ASIC design, standard-cell methodology is practiced with a sizable library (or libraries) of cells. The library usually contains multiple implementations of the same logic function, differing in area and speed. This variety enhances the efficiency of automated synthesis, place, and route (SPR) tools. Indirectly, it also gives the designer greater freedom to perform implementation trade-offs (area vs. speed vs. power consumption). A complete group of standard-cell descriptions is commonly called a *technology library*.

Commercially available electronic design automation (EDA) tools use the technology libraries to automate synthesis, placement, and routing of a digital ASIC. The technology library is developed and distributed by the foundry operator. The library (along with a design netlist format) is the basis for exchanging design information between different phases of the SPR process.

### Synthesis

Using the technology library's cell logical view, the logic synthesis tool performs the process of mathematically transforming the ASIC's register-transfer level (RTL) description into a technology-dependent netlist. This process is analogous to a software compiler converting a high-level C-program listing into a processor-dependent assembly-language listing.

The netlist is the standard-cell representation of the ASIC design, at the logical view level. It consists of instances of the standard-cell library gates, and port connectivity between gates. Proper synthesis techniques ensure mathematical equivalency between the synthesized netlist and original RTL description. The netlist contains no unmapped RTL statements and declarations.

The high-level synthesis tool performs the process of transforming the C-level models (SystemC, ANSI C/C++) description into a technology-dependent netlist.

### Placement

The placement tool starts the physical implementation of the ASIC. With a 2-D floorplan provided by the ASIC designer, the placer tool assigns locations for each gate in the netlist. The resulting *placed gates* netlist contains the physical location of each of the netlist's standard-cells, but retains an abstract description of how the gates' terminals are wired to each other.

Typically the standard cells have a constant size in at least one dimension that allows them to be lined up in rows on the integrated circuit. The chip will consist of a huge number of rows (with power and ground running next to each row) with each row filled with the various cells making up the actual design. Placers obey certain rules: Each gate is assigned a unique (exclusive) location on the die map. A given gate is placed once, and may not occupy or overlap the location of any other gate.

## Routing

Using the placed-gates netlist and the layout view of the library, the router adds both signal connect lines and power supply lines. The fully routed physical netlist contains the listing of gates from synthesis, the placement of each gate from placement, and the drawn interconnects from routing.

### DRC/LVS

Design rule check (DRC) and layout versus schematic (LVS) are verification processes. Reliable device fabrication at modern deep-submicrometer (0.13 μm and below) requires strict observance of transistor spacing, metal layer thickness, and power density rules. DRC exhaustively compares the physical netlist against a set of "foundry design rules" (from the foundry operator), then flags any observed violations.

The LVS process confirms that the layout has the same structure as the associated schematic; this is typically the final step in the layout process. The LVS tool takes as an input a schematic diagram and the extracted view from a layout. It then generates a netlist from each one and compares them. Nodes, ports, and device sizing are all compared. If they are the same, LVS passes and the designer can continue. LVS tends to consider transistor fingers to be the same as an extra-wide transistor. Thus, 4 transistors (each 1 μm wide) in parallel, a 4-finger 1 μm transistor, or a 4 μm transistor are viewed the same by the LVS tool. The functionality of .lib files will be taken from SPICE models and added as an attribute to the .lib file.

In semiconductor design, standard cells are ensured to be design rule checking (DRC) and layout versus schematic (LVS) compliant. This compliance significantly enhances the efficiency of the design process, leading to reduced turnaround times for designers. By ensuring that these cells meet critical verification standards, designers can streamline the integration of these components into larger chip designs, facilitating a smoother and faster development cycle.

## Other cell-based methodologies

"Standard cell" falls into a more general class of design automation flows called cell-based design. Structured ASICs, FPGAs, and CPLDs are variations on cell-based design. From the designer's standpoint, all share the same input front end: an RTL description of the design. The three techniques, however, differ substantially in the details of the SPR flow (synthesize, place-and-route) and physical implementation.

## Complexity measure

For digital standard-cell designs, for instance in CMOS, a common technology-independent metric for complexity measure is gate equivalents (GE).
