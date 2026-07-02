---
title: "Level shifter"
source: https://en.wikipedia.org/wiki/Level_shifter
domain: level-shifters
license: CC-BY-SA-4.0
tags: level shifter, logic level, open collector, logic family
fetched: 2026-07-02
---

# Level shifter

In digital electronics, a **level shifter**, also called **level converter** or **logic level shifter**, or **voltage level translator**, is a circuit used to translate signals from one logic level or voltage domain to another, allowing compatibility between integrated circuits with different voltage requirements, such as TTL and CMOS. Modern systems use level shifters to bridge domains between processors, logic, sensors, and other circuits. In recent years, the three most common logic levels have been 1.8V, 3.3V, and 5V, though levels above and below these voltages are also used.

## Types of level shifter

Uni-directional – All input pins are dedicated to one voltage domain, all output pins are dedicated to the other.

Bi-directional with Dedicated ports – Each voltage domain has both input and output pins, but the data direction of a pin does not change.

Bi-directional with external direction indicator – When an external signal is changed, inputs become outputs and vice versa.

Bi-directional, auto-sensing – A pair of I/O spanning voltage domains can act as either inputs or outputs depending on external stimulus without the need for a dedicated direction control pin.

## Hardware implementation

Fixed function level shifter ICs - These ICs provide several different types of level shift in fixed function devices. Often lumped into 2-bit, 4-bit, or 8-bit level shift configurations offered with various VDD1 and VDD2 ranges, these devices translate logic levels without any additional integrated logic or timing adjustment.

Configurable mixed-signal ICs (CMICs) – Level shifter circuitry can also be implemented in a CMIC. The no-code programmable nature of CMICs allows designers to implement fully customizable level shifters with the added option to integrate configurable logic or timing adjustments in the same device.

Power Management ICs realize level shifters using differential signaling. The differential pair steers the current in one of its two legs which then drives a latch in a different voltage domain and level shifts the voltage.

## Applications of level shifters

Since level shifters are used to resolve the voltage incompatibility between various parts of a system, they have a wide range of applications as well. Level shifters are widely used in interfacing legacy devices and also in SD cards, SIM cards, CF cards, audio codecs and UARTs.

Level shifters are also widely used in gate driver circuits used in power management ICs. In these applications, level shifter translates the control logic signal to high voltages used in driving power MOSFETs.
