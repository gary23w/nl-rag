---
title: "HITAC S-810"
source: https://en.wikipedia.org/wiki/HITAC_S-810
domain: hitac-s-810
license: CC-BY-SA-4.0
tags: hitac s-810
fetched: 2026-07-03
---

# HITAC S-810

The **HITAC S-810** is a family of vector supercomputers developed, manufactured and marketed by Hitachi. The S-810, first announced in August 1982, was the second Japanese supercomputer, following the Fujitsu VP-200 (July 1982) but predating the NEC SX-2 (April 1983). The S-810 was Hitachi's first supercomputer, although the company had previously built a vector processor, the IAP.

The first system shipped was a top-end S-810/20 model, which was delivered to the University of Tokyo's Large Computer Center in October 1983. The S-810 was succeeded as Hitachi's top-end supercomputer by the HITAC S-820 announced in July 1987.

## Architecture

The S-810 implements a Hitachi-designed extension of the IBM System/370 instruction set architecture with 83 vector instructions (80 in the S-810/5 and S-810/10). The vector instructions are *register-to-register*, meaning that they do not directly reference memory. The scalar processor is a Hitachi HITAC M-280H mainframe with a 28 nanosecond (ns) cycle time (clock rate of approximately 35.71 MHz). In the S-810/20, there are 32 scalar registers, whereas the other models have 16. In all models, the scalar processor has a large 256 kilobyte cache.

The vector processor has a 14 ns cycle time (clock rate of approximately 71.43 MHz). The vector registers are 256 elements wide, and each element is 64 bits wide. The S-810/20 has 32 of these registers, whereas the other models have 16. These registers are implemented with 1 kilobit (Kbit) bipolar RAM integrated circuits (ICs) with a 4.5 ns access time. All models have eight 256-bit vector mask registers and 48 vector address registers. All models have three load pipelines and one load/store pipeline for accessing the main memory. The S-810/20 has two lanes, each with two add, one multiply followed by add, and one multiply or divide followed by add floating point pipelines, for a total of twelve. The S-810/10 has one lane with the same configuration as the S-810/20 and therefore a total of six pipelines. CPU logic is implemented with two emitter-coupled logic gate array IC types, a 550-gate part with a 250 picosecond (ps) gate delay and a 1,500-gate part with a 450 ps gate delay.

The main memory is implemented with 16 Kbit complementary metal–oxide–semiconductor static random access memory ICs with an access time of 40 ns. The S-810/20 supports 64 to 256 megabyte (MB) of main memory, whereas the other models support 32 to 128 MB.

## Models

There were three models, the low-end S-810/5, the mid-range S-810/10, and the top-end S-810/20. They differ in the number of vector pipelines installed, the number of scalar registers, the number vector registers, and the amount of memory supported. Hitachi claimed that the S-810/5's peak performance was 160 MFLOPS, the S-810/10's was 315 MFLOPS, and the S-810/20's was 630 MFLOPS.
