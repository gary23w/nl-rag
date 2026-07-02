---
title: "2.5D integrated circuit"
source: https://en.wikipedia.org/wiki/2.5D_integrated_circuit
domain: chiplet-architecture
license: CC-BY-SA-4.0
tags: chiplet architecture, multi-chip module, die-to-die interconnect, 2.5d integration
fetched: 2026-07-02
---

# 2.5D integrated circuit

A **2.5D integrated circuit** (**2.5D IC**) is an advanced packaging technique that combines multiple integrated circuit dies in a single package without stacking them into a three-dimensional integrated circuit (3D-IC) with through-silicon vias (TSVs). The term "2.5D" originated when 3D-ICs with TSVs were quite new and still very difficult. Chip designers realized that many of the advantages of 3D integration could be approximated by placing bare dies side by side on an interposer instead of stacking them vertically. If the pitch is very fine and the interconnect very short, the assembly can be packaged as a single component with better size, weight, and power characteristics than a comparable 2D circuit board assembly. This half-way 3D integration was facetiously named "2.5D" and the name stuck.

Since then, 2.5D has proven to be far more than just "half-way to 3D."

An interposer can support heterogeneous integration – that is, dies of different pitch, size, material, and process node. Placing dies side by side instead of stacking them reduces heat buildup. Upgrading or modifying a 2.5D assembly is as easy as swapping in a new component and revamping the interposer to suit; much faster and simpler than reworking an entire 3D-IC or System-on-Chip (SoC). Some sophisticated 2.5D assemblies even incorporate TSVs and 3D components. Several foundries now support 2.5D packaging.

The success of 2.5D assembly has given rise to "chiplets" – small, functional circuit blocks designed to be combined in mix-and-match fashion on interposers. Several high-end products already take advantage of these LEGO-style chiplets; some experts predict the emergence of an industry-wide chiplet ecosystem. Interposers can be larger than the reticle size which is the maximum area that can be projected by a photolithography scanner or stepper.

## Core design and architecture

A 2.5D IC architecture is an intermediate solution between traditional 2D and advanced 3D architectures. While a 2D architecture integrates all components on a single silicon die (SoC) and a 3D architecture stacks multiple dies vertically, the 2.5D approach involves placing multiple chiplets side-by-side on a silicon interposer within a single package. The chiplets, which perform various functions, are bonded to the interposer, and the interconnection between them are routed on this interposer. The interposer is then connected to the package substrate using silicon vias, which provide connections to peripheral hardware such as SRAM or DRAM.

### The Interposer

The interposer, also known as a redistributed layer (RDL), is a key component in the physical design of chiplets. It acts as an intermediate layer that facilitates communication between chiplets and provides interfaces for peripheral devices. The design of the interposer and its wiring is crucial, as the routing of these wires can introduce additional latency and parasitic parameters that can affect overall performance and reliability. In advanced packaging technologies like CoWoS, the interposer design method uses wiring within the interposer and through-silicon-via (TSV) technology to connect chiplets and establish connections to the packaging substrate.

Interposers can be made from different materials, including silicon, glass, and organics. Silicon interposers are widely used due to their ability to achieve fine feature sizes with existing process technology, making them a cost-effective option. Interposers use TSVs for communication between the chip and for connecting to the substrate. A 10x100um TSV is sometimes used in an interposer with three or four metal layers on the probe side and a single copper RDL on the grind side.

### Interposer technologies

There are several interposer technologies used in 2.5D ICs, each with its own set of trade-offs in terms of cost, performance, and complexity.

- **Silicon Interposers:** The most common type, offering very fine-pitch interconnects using Through-Silicon Vias (TSVs) to route signals vertically through the interposer itself. This is the basis for technologies like TSMC's CoWoS (Chip-on-Wafer-on-Substrate).
- **Organic Interposers:** A lower-cost alternative to silicon that uses organic materials. While they don't achieve the same interconnect density, they are improving and offer significant cost savings.
- **Glass Interposers:** An emerging option with good electrical properties and dimensional stability, but with a less mature manufacturing ecosystem.
- **Bridge Technologies:** Mention solutions like Intel's Embedded Multi-die Interconnect Bridge (EMIB), which uses small, localized silicon bridges embedded in an organic substrate to connect dies, offering a compromise between the cost of a full silicon interposer and the performance of high-density interconnects.

### Interconnects

The interconnects in a 2.5D IC, including micro-bumps and underfill materials, play an important role in the enablement of high bandwidth and low power consumption. The signal channels in a 2.5D integration consist of I/O drivers and receivers, I/O pads, micro-bumps, and chip-to-chip wires. The wires are horizontally routed on an interconnect carrier, such as a bridge-chip, stitch-chip, or an interposer.

The use of smaller pads and micro-bumps in technologies like HIST (Heterogeneous Interconnect Stitching Technology) and interposers leads to smaller capacitance, which improves electrical performance. For example, the total capacitance of a micro-bump and a pair of pads for HIST is about 18 times smaller than that of a bridge-chip because bridge-chip bumps also include organic package vias. The reduced capacitance and shorter interconnects contribute to lower latency and energy consumption. Furthermore, HIST and interposer-based solutions achieve the largest bandwidth-density (BWD) among 2.5D solutions due to the ultralow parasitics of micro-bumps and pads.

## Challenges and limitations

While 2.5D IC technology offers numerous advantages, it also presents several challenges and limitations that must be addressed.

- **Cost:** While 2.5D integration can be more cost-effective than 3D integration, especially at high power densities, it is still more expensive than traditional 2D designs. The fabrication of interposers, particularly silicon interposers, adds to the overall cost. However, for large designs, the yield improvement from partitioning a large die into smaller chiplets can offset these additional costs.
- **Design complexity:** The design of 2.5D ICs is complex and requires careful consideration of various factors, including chiplet partitioning, interconnect topology, and thermal management. EDA tools play a crucial role in optimizing the architecture, but there is a need for more advanced tools that can handle the complexity of heterogeneous integration.
- **Thermal management:** Although 2.5D integration has better thermal performance than 3D integration, thermal management remains a critical challenge. The close proximity of high-power dies can lead to thermal coupling and hotspots, which can affect the performance and reliability of the system. Advanced cooling solutions may be necessary to manage the heat generated by high-performance 2.5D ICs.
- **Supply chain complexity:** The use of chiplets from different vendors can introduce logistical challenges and complexities in the supply chain. Ensuring the compatibility and reliability of chiplets from different sources is a major concern that requires careful management.

## Applications and commercial implementations

2.5D and 3D heterogeneous integration technologies are used in a variety of applications, particularly in high-performance computing (HPC), AI accelerators, high-end CPUs, and FPGAs.

- **High-performance computing (HPC) and AI Accelerators:** Intel's Ponte Vecchio, a high-performance GPU for supercomputers, uses Co-EMIB, a combination of EMIB (2.5D) and Foveros (3D) interconnects. The product is built from 47 components, including compute tiles, SRAM cache tiles, HBM memory stacks, and EMIB interconnect tiles. This combination enables a high-performance supercomputing product that would not be possible with conventional monolithic approaches.
- **High-end CPUs:** AMD's Zen with V-cache uses hybrid bonding 3D stacking technology to increase the size of the L3 cache, which significantly boosts performance for gaming applications.
- **FPGAs:** Intel's Stratix 10 and Agilex families of FPGAs use a mix-and-match approach with 2.5D integration. The Stratix 10 FPGA was the first product to use Intel's EMIB technology and a standardized die-to-die interface called Advanced Interface Bus (AIB).

## Industry standardization and future outlook

The development of industry standards is crucial for the widespread adoption of 2.5D and 3D integration technologies. The Universal Chiplet Interconnect Express (UCIe) is a standardized communication protocol that simplifies the integration of diverse chiplets by offering a unified interface that supports a wide range of chip types, ensuring compatibility across different manufacturing processes and technology nodes.

Some future trends in 2.5D and 3D integration include the use of bridge technologies and co-packaged optics. Intel's Co-EMIB combines Foveros and EMIB to provide 2.5D and 3D connectivity between dies in a package, achieving high interconnect density in both horizontal and vertical directions. Another example is the omnidirectional interconnect (ODI), which can support high-bandwidth interconnects and direct power delivery using smaller TSVs and high-bandwidth interconnects.

Another approach is the use of photonic interconnects as a solution for high-bandwidth, low-power communication in 2.5D integrated systems. In this case an Arrayed Waveguide Grating Router (AWGR) can be used, for example, as an optical switch fabric to construct a photonic Network-on-Chip (NoC) for interposer-based implementations.
