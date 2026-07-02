---
title: "Chiplet"
source: https://en.wikipedia.org/wiki/Chiplet
domain: chiplet-architecture
license: CC-BY-SA-4.0
tags: chiplet architecture, multi-chip module, die-to-die interconnect, 2.5d integration
fetched: 2026-07-02
---

# Chiplet

A **chiplet** is a tiny integrated circuit (**IC**) that contains a well-defined subset of functionality. It is designed to be combined with other chiplets on an interposer in a single package to create a complex component such as a computer processor. Each chiplet in a computer processor provides only a portion of the processor's total functionality. A set of chiplets can be implemented in a mix-and-match "Lego-like" assembly. This provides several advantages over a traditional system on chip (**SoC**) which is monolithic as it comprises a single silicon die:

- Reusable IP (intellectual property): the same chiplet can be used in many different devices
- Heterogeneous integration: chiplets can be fabricated with different processes, materials, and nodes, each optimized for its particular function
- Known good die: chiplets can be tested before assembly, improving the yield of the final device.

Multiple chiplets working together in a single integrated circuit may be called a multi-chip module, hybrid IC, 2.5D IC, or advanced package.

Chiplets may be connected with standards such as UCIe, bunch of wires (BoW), AIB (Advanced Interface Bus), OpenHBI (Open High Bandwidth Interface), and OIF (Optical Internetworking Forum) XSR (Extra Short Reach). Chiplets not designed by the same company must be designed with interoperability in mind.

The term was coined by University of California, Berkeley professor John Wawrzynek as a component of the RAMP Project (research accelerator for multiple processors) in 2006 extension for the Department of Energy.

Common examples include:

- AMD Ryzen based on Zen 2 and later architecture (except APUs)
- NVidia H100, and later
- Intel Sapphire Rapids / Meteor Lake / Arrow Lake, and later
