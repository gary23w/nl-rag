---
title: "High-level synthesis"
source: https://en.wikipedia.org/wiki/High-level_synthesis
domain: high-level-synthesis
license: CC-BY-SA-4.0
tags: high-level synthesis, systemc modeling, behavioral synthesis, c to hdl
fetched: 2026-07-02
---

# High-level synthesis

**High-level synthesis** (**HLS**), sometimes referred to as **C synthesis**, **electronic system-level** (**ESL**) **synthesis**, **algorithmic synthesis**, or **behavioral synthesis**, is an automated design process that takes an abstract behavioral specification of a digital system and finds a register-transfer level structure that realizes the given behavior.

Synthesis begins with a high-level specification of the problem, where behavior is generally decoupled from low-level circuit mechanics such as clock-level timing. Early HLS explored a variety of input specification languages, although recent research and commercial applications generally accept synthesizable subsets of ANSI C/C++/SystemC/MATLAB. The code is analyzed, architecturally constrained, and scheduled to transcompile from a transaction-level model (TLM) into a register-transfer level (RTL) design in a hardware description language (HDL), which is in turn commonly synthesized to the gate level by the use of a logic synthesis tool.

The goal of HLS is to let hardware designers efficiently build and verify hardware, by giving them better control over optimization of their design architecture, and through the nature of allowing the designer to describe the design at a higher level of abstraction while the tool does the RTL implementation. Verification of the RTL is an important part of the process.

Hardware can be designed at varying levels of abstraction. The commonly used levels of abstraction are gate level, register-transfer level (RTL), and algorithmic level.

While logic synthesis uses an RTL description of the design, high-level synthesis works at a higher level of abstraction, starting with an algorithmic description in a high-level language such as SystemC and ANSI C/C++. The designer typically develops the module functionality and the interconnect protocol. The high-level synthesis tools handle the micro-architecture and transform untimed or partially timed functional code into fully timed RTL implementations, automatically creating cycle-by-cycle detail for hardware implementation. The (RTL) implementations are then used directly in a conventional logic synthesis flow to create a gate-level implementation.

## History

Early academic work extracted scheduling, allocation, and binding as the basic steps for high-level-synthesis. Scheduling partitions the algorithm in control steps that are used to define the states in the finite-state machine. Each control step contains one small section of the algorithm that can be performed in a single clock cycle in the hardware. Allocation and binding maps the instructions and variables to the hardware components, multiplexers, registers and wires of the data path.

First generation behavioral synthesis was introduced by Synopsys in 1994 as Behavioral Compiler and used Verilog or VHDL as input languages. The abstraction level used was partially timed (clocked) processes. Tools based on behavioral Verilog or VHDL were not widely adopted in part because neither languages nor the partially timed abstraction were well suited to modeling behavior at a high level. 10 years later, in early 2004, Synopsys end-of-lifed Behavioral Compiler.

Forte Design Systems introduced its Cynthesizer tool which used SystemC as an entry language instead of Verilog or VHDL. Cynthesizer was adopted by many Japanese companies in 2000 as Japan had a very mature SystemC user community. The first high-level synthesis tapeout was achieved in 2001 by Sony using Cynthesizer. Adoption in the United States started in earnest in 2008.

In 2006, an efficient and scalable "SDC modulo scheduling" technique was developed on control and data flow graphs and was later extended to pipeline scheduling. This technique uses the integer linear programming formulation. But it shows that the underlying constraint matrix is totally unimodular (after approximating the resource constraints). Thus, the problem can be solved in polynomial time optimally using a linear programming solver in polynomial time. This work was inducted to the FPGA and Reconfigurable Computing Hall of Fame 2022.

The SDC scheduling algorithm was implemented in the xPilot HLS system developed at UCLA, and later licensed to the AutoESL Design Technologies, a spin-off from UCLA. AutoESL was acquired by Xilinx (now part of AMD) in 2011, and the HLS tool developed by AutoESL became the base of Xilinx HLS solutions, Vivado HLS and Vitis HLS, widely used for FPGA designs.

## Source input

The most common source inputs for high-level synthesis are based on standard languages such as ANSI C/C++, SystemC and MATLAB.

High-level synthesis typically also includes a bit-accurate executable specification as input, since to derive an efficient hardware implementation, additional information is needed on what is an acceptable Mean-Square Error or Bit-Error Rate etc. For example, if the designer starts with an FIR filter written using the "double" floating type, before they can derive an efficient hardware implementation, they need to perform numerical refinement to arrive at a fixed-point implementation. The refinement requires additional information on the level of quantization noise that can be tolerated, the valid input ranges etc. This bit-accurate specification makes the high level synthesis source specification functionally complete. Normally the tools infer from the high level code a Finite State Machine and a Datapath that implement arithmetic operations.

## Process stages

The high-level synthesis process consists of a number of activities. Various high-level synthesis tools perform these activities in different orders using different algorithms. Some high-level synthesis tools combine some of these activities or perform them iteratively to converge on the desired solution.

- Lexical processing
- Algorithm optimization
- Control/Dataflow analysis
- Library processing
- Resource allocation
- Scheduling
- Functional unit binding
- Register binding
- Output processing
- Input Rebundling

## Functionality

In general, an algorithm can be performed over many clock cycles with few hardware resources, or over fewer clock cycles using a larger number of ALUs, registers and memories. Correspondingly, from one algorithmic description, a variety of hardware microarchitectures can be generated by an HLS compiler according to the directives given to the tool. This is the same trade off of execution speed for hardware complexity as seen when a given program is run on conventional processors of differing performance, yet all running at roughly the same clock frequency.

### Architectural constraints

Synthesis constraints for the architecture can automatically be applied based on the design analysis. These constraints can be broken into

- Hierarchy
- Interface
- Memory
- Loop
- Low-level timing constraints
- Iteration

### Interface synthesis

Interface Synthesis refers to the ability to accept a pure C/C++ description as its input, then use automated interface synthesis technology to control the timing and communications protocol on the design interface. This enables interface analysis and exploration of a full range of hardware interface options such as streaming, single- or dual-port RAM plus various handshaking mechanisms. With interface synthesis, the designer does not embed interface protocols in the source description. Examples might be: direct connection, one line, 2-line handshake, FIFO.

## Vendors

Data reported on recent Survey

Status

Compiler

Owner

License

Input

Output

Year

Domain

Test

bench

FP

FixP

In use

Stratus HLS

Cadence Design Systems

Commercial

C

–

C++

SystemC

RTL

2015

All

Yes

Yes

Yes

AUGH

TIMA Lab.

Academic

C subset

VHDL

2012

All

Yes

No

No

eXCite

Archived

2019-09-17 at the

Wayback Machine

Y Explorations

Commercial

C

VHDL

–

Verilog

2001

All

Yes

No

Yes

Bambu

PoliMi

Academic

C

VHDL

–

Verilog

2012

All

Yes

Yes

No

Bluespec

BlueSpec, Inc.

BSD

-3

Bluespec

SystemVerilog

(

Haskell

)

SystemVerilog

2007

All

No

No

No

QCC

CacheQ Systems, Inc.

Commercial

C

,

C++

,

Fortran

Host executable +

FPGA

bit file (SystemVerilog is intermediate)

2018

All - multi-core and heterogeneous compute

Yes (C++)

Yes

Yes

CHC

Altium

Commercial

C subset

VHDL

–

Verilog

2008

All

No

Yes

Yes

CoDeveloper

Impulse Accelerated

Commercial

Impulse-C

VHDL

2003

Image

streaming

Yes

Yes

No

HDL Coder

MathWorks

Commercial

MATLAB

,

Simulink

,

Stateflow

, Simscape

VHDL

, Verilog

2003

Control systems, signal processing, wireless, radar, communications, image and computer vision

Yes

Yes

Yes

CyberWorkBench

NEC

Commercial

C, BDL,

SystemC

VHDL

–

Verilog

2004

All

Cycle,

formal

Yes

Yes

Catapult

Siemens EDA

Commercial

C

–

C++

SystemC

VHDL

–

Verilog

2004

All

Yes

Yes

Yes

DWARV

TU. Delft

Academic

C subset

VHDL

2012

All

Yes

Yes

Yes

GAUT

University of Western Brittany

Academic

C

,

C++

VHDL

2010

DSP

Yes

No

Yes

Hastlayer

Lombiq Technologies

BSD

-3

C#

,

C++

,

F#

, ...

(

.NET

)

VHDL

2015

.NET

Yes

Yes

Yes

Instant SoC

FPGA Cores

Commercial

C

,

C++

VHDL

–

Verilog

2019

All

Yes

No

No

Intel High Level Synthesis Compiler

Intel FPGA (Formerly Altera)

Commercial

C

,

C++

Verilog

2017

All

Yes

Yes

Yes

LegUp HLS

LegUp Computing

Commercial

C

,

C++

Verilog

2015

All

Yes

Yes

Yes

LegUp

Archived

2020-07-24 at the

Wayback Machine

University of Toronto

Academic

C

Verilog

2010

All

Yes

Yes

No

MaxCompiler

Maxeler

Commercial

MaxJ

RTL

2010

Data-flow analysis

No

Yes

No

ROCCC

Jacquard Comp.

Commercial

C subset

VHDL

2010

Streaming

No

Yes

No

Symphony C

Synopsys

Commercial

C

,

C++

VHDL

–

Verilog

,

SystemC

2010

All

Yes

No

Yes

VivadoHLS

(formerly AutoPilot

from AutoESL

)

Xilinx

Commercial

C

–

C++

SystemC

VHDL

–

Verilog

,

SystemC

2013

All

Yes

Yes

Yes

Kiwi

University of Cambridge

Academic

C#

Verilog

2008

.NET

No

Yes

Yes

CHiMPS

University of Washington

Academic

C

VHDL

2008

All

No

No

No

gcc2verilog

Korea University

Academic

C

Verilog

2011

All

No

No

No

HercuLeS

Ajax Compilers

Commercial

C/NAC

VHDL

2012

All

Yes

Yes

Yes

Shang

University of Illinois Urbana-Champaign

Academic

C

Verilog

2013

All

Yes

?

?

Trident

Los Alamos NL

Academic

C subset

VHDL

2007

Scientific

No

Yes

No

Aban-

doned

AccelDSP

Xilinx

Commercial

MATLAB

VHDL

–

Verilog

2006

DSP

Yes

Yes

Yes

C2H

Altera

Commercial

C

VHDL

–

Verilog

2006

All

No

No

No

CtoVerilog

University of Haifa

Academic

C

Verilog

2008

All

No

No

No

DEFACTO

University South Cailf.

Academic

C

RTL

1999

DSE

No

No

No

Garp

University of California, Berkeley

Academic

C subset

bitstream

2000

Loop

No

No

No

MATCH

Northwest University

Academic

MATLAB

VHDL

2000

Image

No

No

No

Napa-C

Sarnoff Corp.

Academic

C subset

VHDL

–

Verilog

1998

Loop

No

No

No

PipeRench

Carnegie Mellon University

Academic

DIL

bistream

2000

Stream

No

No

No

SA-C

University of Colorado

Academic

SA-C

VHDL

2003

Image

No

No

No

SeaCucumber

Brigham Young University

Academic

Java

EDIF

2002

All

No

Yes

Yes

SPARK

University of California, Irvine

Academic

C

VHDL

2003

Control

No

No

No

- Dynamatic from EPFL/ETH Zurich
- MATLAB HDL Coder [1] from Mathworks
- HLS-QSP from CircuitSutra Technologies
- C-to-Silicon from Cadence Design Systems
- Concurrent Acceleration from Concurrent EDA
- Symphony C Compiler from Synopsys
- QuickPlay from PLDA
- PowerOpt from ChipVision
- Cynthesizer from Forte Design Systems (now Stratus HLS from Cadence Design Systems)
- Catapult C from Calypto Design Systems, part of Mentor Graphics as of 2015, September 16. In November 2016 Siemens announced plans to acquire Mentor Graphics, Mentor Graphics became styled as "Mentor, a Siemens Business". In January 2021, the legal merger of Mentor Graphics with Siemens was completed - merging into the Siemens Industry Software Inc legal entity. Mentor Graphics' name was changed to Siemens EDA, a division of Siemens Digital Industries Software.
- PipelineC [2]
- CyberWorkBench from NEC
- Mega Hardware
- C2R from CebaTech
- CoDeveloper from Impulse Accelerated Technologies
- HercuLeS by Nikolaos Kavvadias
- Program In/Code Out (PICO) from Synfora, acquired by Synopsys in June 2010
- xPilot from University of California, Los Angeles
- Vsyn from vsyn.ru
- ngDesign from SynFlow
