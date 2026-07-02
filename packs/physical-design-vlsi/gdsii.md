---
title: "GDSII"
source: https://en.wikipedia.org/wiki/GDSII
domain: physical-design-vlsi
license: CC-BY-SA-4.0
tags: physical design flow, vlsi layout, integrated circuit layout, design rule checking
fetched: 2026-07-02
---

# GDSII

**GDSII stream format** (**GDSII**), is a binary database file format which is the de facto industry standard for electronic design automation (EDA) data exchange of integrated circuit (IC) or IC layout artwork. It is a binary file format representing planar geometric shapes, text labels, and other information about the layout in hierarchical form (two-dimensional/2D CAD file format). The data can be used to reconstruct all or part of the artwork to be used in sharing layouts, transferring artwork between different tools, or creating photomasks.

## History

Initially, GDSII was designed as a stream format used to control integrated circuit photomask plotting. Despite its limited set of features and low data density, it became the industry conventional stream format for transfer of IC layout data between design tools of different vendors, all of which operated with proprietary data formats.

It was originally developed by Calma for its layout design system, "Graphic Design System" ("GDS") and "GDSII".

GDSII files are usually the final output product of the IC design cycle and are handed over to IC foundries for IC fabrication. GDSII files were originally written on magnetic tape. The final deadline for IC designers is still called tape-out for this reason.

Objects contained in a GDSII file are grouped by assigning numeric attributes to them including a "layer number", "datatype" or "texttype". While these attributes were designed to correspond to the "layers of material" used in manufacturing an integrated circuit, their meaning rapidly became more abstract to reflect the way that the physical layout is designed.

As of April 2008, many EDA software vendors have moved to the stream format OASIS, which replaced GDSII. For smaller designs, GDSII continues to be used today.

## GDSII utilities

As the GDSII stream format is a de facto standard, it is supported by nearly all EDA software. Besides the commercial vendors there are plenty of free GDSII utilities. These free tools include editors, viewers, utilities to convert the 2D layout data into common 3D formats, utilities to fly through a 3D version, utilities to convert the binary format to a human readable ASCII format and program libraries.
