---
title: "Integrated modular avionics"
source: https://en.wikipedia.org/wiki/Integrated_modular_avionics
domain: arinc-653
license: CC-BY-SA-4.0
tags: arinc 653, integrated modular avionics, time and space partitioning, apex interface
fetched: 2026-07-02
---

# Integrated modular avionics

**Integrated modular avionics** (**IMA**) are real-time computer network airborne systems. This network consists of a number of computing modules capable of supporting numerous applications of differing criticality levels.

In opposition to traditional federated architectures, the IMA concept proposes an integrated architecture with application software portable across an assembly of common hardware modules. An IMA architecture imposes multiple requirements on the underlying operating system.

## History

It is believed that the IMA concept originated with the avionics design of the fourth-generation jet fighters. It has been in use in fighters such as F-22 and F-35, or Dassault Rafale since the beginning of the '90s. Standardization efforts were ongoing at this time (see ASAAC or STANAG 4626), but no final documents were issued then.

## Architecture

IMA modularity simplifies the development process of avionics software:

- As the structure of the modules network is unified, it is mandatory to use a common API to access the hardware and network resources, thus simplifying the hardware and software integration.
- IMA concept also allows the Application developers to focus on the Application layer, reducing the risk of faults in the lower-level software layers.
- As modules often share an extensive part of their hardware and lower-level software architecture, maintenance of the modules is easier than with previous specific architectures.
- Applications can be reconfigured on spare modules if the primary module that supports them is detected faulty during operations, increasing the overall availability of the avionics functions.

Communication between the modules can use an internal high speed Computer bus, or can share an external network, such as ARINC 429 or ARINC 664 (part 7).

However, much complexity is added to the systems, which thus require novel design and verification approaches since applications with different criticality levels share hardware and software resources such as CPU and network schedules, memory, inputs and outputs. Partitioning is generally used in order to help segregate mixed criticality applications and thus ease the verification process.

ARINC 650 and ARINC 651 provide general purpose hardware and software standards used in an IMA architecture. However, parts of the API involved in an IMA network has been standardized, such as:

- ARINC 653 for the software avionics partitioning constraints to the underlying Real-time operating system (RTOS), and the associated API

## Certification considerations

RTCA DO-178C and RTCA DO-254 form the basis for flight certification today, while DO-297 gives specific guidance for Integrated modular avionics. ARINC 653 contributes by providing a framework that enables each software building block (called a partition) of the overall Integrated modular avionics to be tested, validated, and qualified independently (up to a certain measure) by its supplier.

The FAA CAST-32A position paper provides information (not official guidance) for certification of multicore systems, but does not specifically address IMA with multicore. A research paper by VanderLeest and Matthews addresses implementation of IMA principles for multicore"

## Examples of IMA architecture

Examples of aircraft avionics that uses IMA architecture:

- Airbus A220 : Rockwell Collins Pro Line Fusion
- Airbus A350
- Airbus A380
- Airbus A400M
- ATR 42
- ATR 72
- BAE Hawk (Hawk 128 AJT)
- Boeing 777 : includes AIMS avionics from Honeywell Aerospace
- Boeing 777X: will include the Common Core System from GE Aviation
- Boeing 787 : GE Aviation Systems (formerly Smiths Aerospace) IMA architecture is called *Common Core System*
- Bombardier Global 5000 / 6000 : Rockwell Collins Pro Line Fusion
- COMAC C919
- Dassault Falcon 900, Falcon 2000, and Falcon 7X : Honeywell's IMA architecture is called *MAU* (Modular Avionics Units), and the overall platform is called EASy
- F-22 Raptor
- Gulfstream G280: Rockwell Collins Pro Line Fusion
- Gulfstream G400, G500, G600, G700, G800, Data Concentration Network (DCN)
- Rafale : Thales IMA architecture is called *MDPU* (Modular Data Processing Unit)
- Sukhoi Superjet 100
