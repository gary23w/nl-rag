---
title: "Via (electronics)"
source: https://en.wikipedia.org/wiki/Via_(electronics)
domain: pcb-design
license: CC-BY-SA-4.0
tags: pcb design, printed circuit board, surface-mount technology, solder mask
fetched: 2026-07-02
---

# Via (electronics)

A **via** (Latin, 'path' or 'way') is an electrical connection between two or more metal layers of a printed circuit boards (PCB) or integrated circuit. Essentially a via is a small drilled hole that goes through two or more adjacent layers; the hole is plated with metal (often copper) that forms an electrical connection through the insulating layers.

Vias are an important concern in PCB manufacturing. As vertical structures crossing multiple layers, they are specified differently from most of the design, which increases the chance for errors. They place the strictest demands on registration (how closely aligned different layers are). They are manufactured with different tooling from other features -- tooling that typically has looser tolerances. If either the hole or any layer is slightly out of place, the wrong electrical connections may be made; this may not be visible from the surface. After the hole is drilled, it must also be lined with conductive material, as opposed to simply leaving conductive material in place on copper layers. Even an initially good board may develop problems later because the via reacts to heat differently from the substrate around it. Vias also represent a discontinuity in the electrical impedance, which can cause problems for signal integrity.

## In printed circuit boards

In printed circuit board (PCB) design, a via consists of two pads in corresponding positions on different copper layers of the board, that are electrically connected by a hole through the board. The hole is made conductive by electroplating, or is lined with a tube or a rivet. High-density multilayer PCBs may have microvias: **blind vias** are exposed only on one side of the board, while **buried vias** connect internal layers without being exposed on either surface. **Thermal vias** carry heat away from power devices and are typically used in arrays of about a dozen.

A via consists of:

1. Barrel — conductive tube filling the drilled hole
2. Pad — connects each end of the barrel to the component, plane, or trace
3. Antipad — clearance hole between barrel and metal layer to which it is not connected

A via, sometimes called PTV or plated-through-via, should not be confused with a plated through hole (PTH). A via is used as an interconnection between copper layers on a PCB while the PTH is generally made larger than vias and is used as a plated hole for acceptance of component leads - such as non-SMT resistors, capacitors, and DIP package IC. PTH can also be used as holes for mechanical connection while vias may not. Another usage of PTH is known as a **castellated hole** where the PTH is aligned at the edge of the board so that it is cut in half when the board is milled out of the panel - the main usage is for allowing one PCB to be soldered to another in a stack - thus acting both as a fastener and also as a connector.

Three major kinds of vias are shown in right figure. The basic steps of making a PCB are: making the substrate material and stacking it in layers; through-drilling of plating the vias; and copper trace patterning using photolithography and etching. With this standard procedure, possible via configurations are limited to through-holes. Depth-controlled drilling techniques such as using lasers can allow for more varied via types. Laser drills can also be used for smaller and more precisely positioned holes than mechanical drills produce. PCB manufacturing typically starts with a so-called core, a basic double-sided PCB. Layers beyond the first two are stacked from this basic building block. If two more layers are consecutively stacked from bottom of core, you can have a 1-2 via, a 1-3 via and a through hole. Each type of via is made by drilling at each stacking stage. If one layer is stacked on top of the core and other is stacked from the bottom, the possible via configurations are 1-3, 2-3 and through hole. The user must gather information about the PCB manufacturer's allowed methods of stacking and possible vias. For cheaper boards, only through holes are made and antipad (or clearance) is placed on layers which are supposed not to be contacted to vias.

## IPC 4761

IPC 4761 defines the following via types:

- Type I: Tented via
- Type II: Tented & covered via
- Type III-a: Plugged via, sealed with non-conductive material on one side
- Type III-b: Plugged via, sealed with non-conductive material on both sides
- Type IV-a: Plugged & covered via, sealed with non-conductive material and covered with wet solder mask on one side
- Type IV-b: Plugged & covered via, sealed with non-conductive material and covered with wet solder mask on both sides
- Type V: Filled via, filled with non-conductive paste
- Type VI-a: Filled & covered via, covered with dry film or wet solder mask on one side
- Type VI-b: Filled & covered via, covered with dry film or wet solder mask on both sides
- Type VII: Filled & capped via, filled with non-conductive paste and overplated on both sides

## Failure behavior

If well made, PCB vias will primarily fail due to differential expansion and contraction between the copper plating and the PCB in the out of plane direction (Z). This differential expansion and contraction will induce cyclic fatigue in the copper plating, eventually resulting in crack propagation and an electrical open circuit. Various design, material, and environmental parameters will influence the rate of this degradation. To ensure via robustness, IPC sponsored a round-robin exercise that developed a time to failure calculator.

## Vias in integrated circuits

In integrated circuit (IC) design, a via is a small opening in an insulating oxide layer that allows a conductive connection between different layers. A via on an integrated circuit that passes completely through a silicon wafer or die is called a through-chip via or through-silicon via (TSV). **Through-glass vias** (**TGV**) have been studied by Corning Glass for semiconductor packaging, due to the reduced electrical loss of glass versus silicon packaging. A via connecting the lowest layer of metal to diffusion or poly is typically called a "contact".

## Gallery

- (Plated-through holes on a multilayer board (magnified)) Plated-through holes on a multilayer board (magnified)
- (Double layered plating in CAD. Vias makes EDA placement possible., Bottom layer – Red, Top layer – Blue) Double layered plating in CAD. Vias makes EDA placement possible. Bottom layer – Red Top layer – Blue
- (Plating of plated-through holes:, Above – Top layer, Down – Bottom layer) Plating of plated-through holes: Above – Top layer Down – Bottom layer

- (Cross-cut section of a multilayer via) Cross-cut section of a multilayer via
- (The small metallic circles are vias) The small metallic circles are vias
- (Filled vias with no visible hole) Filled vias with no visible hole
