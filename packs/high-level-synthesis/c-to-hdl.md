---
title: "C to HDL"
source: https://en.wikipedia.org/wiki/C_to_HDL
domain: high-level-synthesis
license: CC-BY-SA-4.0
tags: high-level synthesis, systemc modeling, behavioral synthesis, c to hdl
fetched: 2026-07-02
---

# C to HDL

**C to HDL** tools convert C language or C-like source code into a hardware description language (HDL) such as VHDL or Verilog. The converted code can then be synthesized and translated into a hardware device such as a field-programmable gate array. Compared to software, equivalent designs in hardware consume less power (yielding higher performance per watt) and execute faster with lower latency, more parallelism and higher throughput. However, system design and functional verification in a hardware description language can be tedious and time-consuming, so systems engineers often write critical modules in HDL and other modules in a high-level language and synthesize these into HDL through C to HDL or high-level synthesis tools.

**C to RTL** is another name for this methodology. RTL refers to the register transfer level representation of a program necessary to implement it in logic.

## History

Early development on C to HDL was done by Ian Page, Charles Sweeney and colleagues at Oxford University in the 1990s who developed the Handel-C language. They commercialized their research by forming Embedded Solutions Limited (ESL) in 1999 which was renamed Celoxica in September 2000. In 2008, the embedded systems departments of Celoxica was sold to Catalytic for $3 million and which later merged to become Agility Computing. In January 2009, Mentor Graphics acquired Agility's C synthesis assets. Celoxica continues to trade concentrating on hardware acceleration to process transactions in the financial sector and other industries.

## Applications

C to HDL techniques are most commonly applied to applications that have unacceptably high execution times on existing general-purpose supercomputer architectures. Examples include bioinformatics, computational fluid dynamics (CFD), financial processing, and oil and gas survey data analysis. Embedded applications requiring high performance or real-time data processing are also an area of use. System-on-chip (SoC) design may also take advantage of C to HDL techniques.

C-to-VHDL compilers are very useful for large designs or for implementing code that might change in the future. Designing a large application entirely in HDL may be very difficult and time-consuming; the abstraction of a high level language for such a large application will often reduce total development time. Furthermore, an application coded in HDL will almost certainly be more difficult to modify than one coded in a higher level language. If the designer needs to add new functionality to the application, adding a few lines of C code will almost always be easier than remodeling the equivalent HDL code.

Flow to HDL tools have a similar aim, but with flow rather than C-based design.

## Example tools

- SmartHLS (originally LegUp), ANSI C to Verilog tool developed by Microchip Technology, based on LLVM compiler.
- CBG CtoV A tool developed 1995–99 by DJ Greaves (University of Cambridge) that instantiated RAMs and interpreted various SystemC constructs and datatypes.
- C-to-Verilog tool (NISC) from University of California, Irvine
- Altium Designer 6.9 and 7.0 (a.k.a. Summer 08) from Altium
- Nios II C-to-Hardware Acceleration Compiler from Altera
- Catapult C tool from Mentor Graphics
- Cynthesizer from Forte Design Systems
- SystemC from Celoxica (defunct)
- Handel-C from Celoxica (defunct)
- DIME-C from Nallatech
- Impulse C from Impulse Accelerated Technologies
- Instant-SoC from FPGA-Cores
- FpgaC which is an open source initiative
- SA-C programming language
- Mitrion-C from Mitrionics
- SPARK (a C-to-VHDL) from University of California, San Diego
- VLSI/VHDL CAD Group Index of Useful Tools from Case Western Reserve University
- MyHDL is a Python-subset compiler and simulator to VHDL and Verilog
