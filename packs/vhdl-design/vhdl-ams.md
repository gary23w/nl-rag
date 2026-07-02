---
title: "VHDL-AMS"
source: https://en.wikipedia.org/wiki/VHDL-AMS
domain: vhdl-design
license: CC-BY-SA-4.0
tags: vhdl language, vhdl design, hardware description language, rtl design
fetched: 2026-07-02
---

# VHDL-AMS

**VHDL-AMS** is a derivative of the hardware description language VHDL (IEEE 1076-2002). It includes analog and mixed-signal extensions (AMS) in order to define the behavior of analog and mixed-signal systems (IEEE 1076.1-2017).

The VHDL-AMS standard was created with the intent of enabling designers of analog and mixed signal systems and integrated circuits to create and use modules that encapsulate high-level behavioral descriptions as well as structural descriptions of systems and components.

VHDL-AMS is an industry standard modeling language for mixed signal circuits. It provides both continuous-time and event-driven modeling semantics, and so is suitable for analog, digital, and mixed analog/digital circuits. It is particularly well suited for verification of very complex analog, mixed-signal and radio frequency integrated circuits.

## Code example

In VHDL-AMS, a design consists at a minimum of an *entity* which describes the interface and an *architecture* which contains the actual implementation. In addition, most designs import library modules. Some designs also contain multiple architectures and *configurations*.

A simple ideal diode in VHDL-AMS would look something like this:

```mw
library IEEE;
use IEEE.math_real.all;
use IEEE.electrical_systems.all;

-- this is the entity
entity DIODE is
   generic (iss : current := 1.0e-14);   
   port (terminal anode, cathode : electrical);      
end entity DIODE;

architecture IDEAL of DIODE is
  quantity v across i through anode to cathode;
  constant vt : voltage := 0.0258;     
begin

  i == iss * (exp(v/vt) - 1.0);

end architecture IDEAL;
```

## VHDL-AMS Simulators

- ANSYS Simplorer
- Cadence Virtuoso AMS Designer
- Dolphin Integration SMASH
- Mentor Graphics Questa ADMS
- Mentor Graphics SystemVision
- Synopsys SaberRD
