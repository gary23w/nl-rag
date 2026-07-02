---
title: "Floorplan (microelectronics)"
source: https://en.wikipedia.org/wiki/Floorplan_(microelectronics)
domain: floorplanning
license: CC-BY-SA-4.0
tags: chip floorplanning, die floorplan, vlsi partitioning, block placement
fetched: 2026-07-02
---

# Floorplan (microelectronics)

In electronic design automation, a **floorplan** of an integrated circuit consists of a schematic arrangement of its major functional blocks on the chip area and the specification of high-level parameters such as the **aspect ratio** or **core utilization**.

The design step in which floorplans are created is called **floorplanning**, an early stage in the design flow for integrated circuit design.

Various mathematical abstractions of this problem have been studied.

## Floorplanning design stage

The floorplanning design stage consists of various steps with the aim of finding floorplans that allow a timing-clean routing and spread power consumption over the whole chip.

- **Chip Area Estimation**: The dimensions and aspect ratio of the chip area are determined. The estimation considers the space required to place macros, standard cells and I/O ports while also leaving enough space for routing resources to enable a successful place and route design flow. Usually a core utilization $U={\frac {A_{macros}+A_{std\_cells}}{A_{core}}}$ of 60%-70% is targeted.

- **I/O Pad Positioning**: Input/Output Pads usually need to be positioned along the periphery of the chip. Near the I/O Pads space for line drivers needs to be reserved to minimize delay and signal degradation.
- **Macro Placement**: During macro placement large functional blocks with a fixed size and fixed pins such as memory arrays, clock generators or custom components need to be placed within the floorplan's outline. Effective macro placement minimizes the length of timing critical paths, avoids routing congestion and ensures thermal balance.
- **Standard Cell Row Creation**: Areas where standard cells should be placed are determined and divided into standard cell rows. During the placement stage standard cells are forced to align with standard cell rows although they might be of multi-row height. The height of the standard cell rows determines the available routing resources per row while also influencing the power.

- **Power / Ground Structures**: Obtaining a power/ground network is not always included in the floorplanning stage. There are however approaches to cosynthesize floorplans and **P/G networks** based on the idea that if macros and I/O pads are fixed, a power grid analysis is possible.

## Mathematical models

In mathematics floorplanning refers to the problem of packing smaller rectangles with a fixed or unfixed orientation into a larger rectangle. The dimensions of the larger and smaller rectangles might be fixed (hard constraints) or must be optimized (soft constraints). Additionally, a measure modelling the quality of routing that the floorplan allows might be optimized.

Various variants of rectangle packing are NP-hard.

## Sliceable floorplans

A sliceable floorplan is a floorplan that may be defined recursively as described below.

- A floorplan that consists of a single rectangular block is sliceable.
- If a block from a sliceable floorplan is cut ("sliced") in two by a vertical or horizontal line, the resulting floorplan is sliceable.

The process is known as guillotine cutting. Sliceable floorplans have been used in a number of early electronic design automation tools for a number of reasons. Sliceable floorplans may be conveniently represented by binary trees (more specifically, *k*-d trees), which correspond to the order of slicing. More importantly, a number of NP-hard problems with floorplans have polynomial time algorithms when restricted to sliceable floorplans.

- (A sliceable floorplan)A sliceable floorplan
- (A non-sliceable floorplan)A non-sliceable floorplan
