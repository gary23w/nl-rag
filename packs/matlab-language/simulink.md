---
title: "Simulink"
source: https://en.wikipedia.org/wiki/Simulink
domain: matlab-language
license: CC-BY-SA-4.0
tags: matlab language, matlab lang, matlab script, simulink
fetched: 2026-07-02
---

# Simulink

**Simulink** is a MATLAB-based graphical programming environment for modeling, simulating and analyzing multidomain dynamical systems. Its primary interface is a graphical block diagramming tool and a customizable set of block libraries. It offers tight integration with the rest of the MATLAB environment and can either drive MATLAB or be scripted from it. Simulink is widely used in automatic control and digital signal processing for multidomain simulation and model-based design.

## Add-on products

MathWorks and other third-party hardware and software products can be used with Simulink. For example, Stateflow extends Simulink with a design environment for developing state machines and flow charts. Simscape is an add-on product that extends Simulink with support for physical modeling. Developed by MathWorks, it enables the modeling and simulation of multidomain physical systems by connecting physical components whose interactions represent domains such as electrical, mechanical, thermal, and fluid systems. Simscape models can be combined with standard Simulink block diagrams, allowing the simulation of systems that couple physical dynamics with control algorithms and signal-based components. Coupled with another of their products, Simulink can automatically generate C source code for real-time implementation of systems. As the efficiency and flexibility of the code improves, this is becoming more widely adopted for production systems, in addition to being a tool for embedded system design work because of its flexibility and capacity for quick iteration. Embedded Coder creates code efficient enough for use in embedded systems.

Simulink Real-Time (formerly known as xPC Target), together with x86-based real-time systems, is an environment for simulating and testing Simulink and Stateflow models in real-time on the physical system. Another MathWorks product also supports specific embedded targets. When used with other generic products, Simulink and Stateflow can automatically generate synthesizable VHDL and Verilog.

Simulink Verification and Validation enables systematic verification and validation of models through modeling style checking, requirements traceability and model coverage analysis. Simulink Design Verifier uses formal methods to identify design errors like integer overflow, division by zero and dead logic, and generates test case scenarios for model checking within the Simulink environment.

SimEvents is used to add a library of graphical building blocks for modeling queuing systems to the Simulink environment, and to add an event-based simulation engine to the time-based simulation engine in Simulink.

## Release history

| MATLAB Version | Release name | Simulink version | Year | Notes |
|---|---|---|---|---|
| 1.0 |   |   | 1984 |   |
| 2 |   |   | 1986 |   |
| 3 |   |   | 1987 |   |
| 3.5 |   |   | 1990 | Ran on MS-DOS but required at least a 386 processor. Version 3.5m required math coprocessor |
| 4 |   |   | 1992 | Renamed from Simulab to SIMULINK |
| 4.2c | R7 |   | 1994 | Ran on Windows 3.1. Required a math coprocessor |
| 5.0 | R8 |   | 1996 |   |
| 5.1 | R9 |   | 1997 |   |
| 5.1.1 | R9.1 |   |   |   |
| 5.2 | R10 |   | 1998 |   |
| 5.2.1 | R10.1 |   |   |   |
| 5.3 | R11 |   | 1999 |   |
| 5.3.1 | R11.1 |   |   |   |
| 6.0 | R12 |   | 2000 |   |
| 6.1 | R12.1 |   | 2001 |   |
| 6.5 | R13 | Simulink 5.0.2 | 2002 |   |
| 6.5.1 | R13SP1 | Simulink 5.1 | 2003 |   |
| 6.5.2 | R13SP2 | Simulink 5.2 |   |   |
| 7 | R14 | Simulink 6.0 | 2004 |   |
| 7.0.1 | R14SP1 | Simulink 6.1 |   |   |
| 7.0.4 | R14SP2 | Simulink 6.2 | 2005 |   |
| 7.1 | R14SP3 | Simulink 6.3 |   |   |
| 7.2 | R2006a | Simulink 6.4 | 2006 |   |
| 7.3 | R2006b | Simulink 6.5 |   |   |
| 7.4 | R2007a | Simulink 6.6 | 2007 |   |
| 7.5 | R2007b | Simulink 7.0 | Last release for Windows 2000 and PowerPC Mac. |   |
| 7.6 | R2008a | Simulink 7.1 | 2008 |   |
| 7.7 | R2008b | Simulink 7.2 |   |   |
| 7.8 | R2009a | Simulink 7.3 | 2009 | First release for 32-bit & 64-bit Windows 7. |
| 7.9 | R2009b | Simulink 7.4 | First release for Intel 64-bit Mac, and last for Solaris SPARC. |   |
| 7.10 | R2010a | Simulink 7.5 | 2010 | Last release for Intel 32-bit Mac. |
| 7.11 | R2010b | Simulink 7.6 |   |   |
| 7.12 | R2011a | Simulink 7.7 | 2011 |   |
| 7.13 | R2011b | Simulink 7.8 |   |   |
| 7.14 | R2012a | Simulink 7.9 | 2012 |   |
| 8 | R2012b | Simulink 8.0 |   |   |
| 8.1 | R2013a | Simulink 8.1 | 2013 |   |
| 8.2 | R2013b | Simulink 8.2 |   |   |
| 8.3 | R2014a | Simulink 8.3 | 2014 |   |
| 8.4 | R2014b | Simulink 8.4 |   |   |
| 8.5 | R2015a | Simulink 8.5 | 2015 |   |
| 8.6 | R2015b | Simulink 8.6 | Last release supporting 32-bit Windows |   |
| 9.0 | R2016a | Simulink 8.7 | 2016 |   |
| 9.1 | R2016b | Simulink 8.8 |   |   |
| 9.2 | R2017a | Simulink 8.9 | 2017 |   |
| 9.3 | R2017b | Simulink 9.0 |   |   |
| 9.4 | R2018a | Simulink 9.1 | 2018 |   |
| 9.5 | R2018b | Simulink 9.2 |   |   |
| 9.6 | R2019a | Simulink 9.3 | 2019 | Simulink Onramp; Schedule Editor; |
| 9.7 | R2019b | Simulink 10.0 | Toolstrip; Messages; Blockset Designer; Subsystem Reference |   |
| 9.8 | R2020a | Simulink 10.1 | 2020 |   |
| 9.9 | R2020b | Simulink 10.2 |   |   |
| 9.10 | R2021a | Simulink 10.3 | 2021 |   |
| 9.11 | R2021b | Simulink 10.4 |   |   |
| 9.12 | R2022a | Simulink 10.5 | 2022 |   |
| 9.13 | R2022b | Simulink 10.6 |   |   |
| 9.14 | R2023a | Simulink 10.7 | 2023 |   |
| 23.2 | R2023b | Simulink 23.2 |   |   |
| 24.1 | R2024a | Simulink 24.1 | 2024 |   |
| 24.2 | R2024b | Simulink 24.2 |   |   |
