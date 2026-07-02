---
title: "Power integrity"
source: https://en.wikipedia.org/wiki/Power_integrity
domain: power-integrity
license: CC-BY-SA-4.0
tags: power integrity, decoupling capacitor, ground bounce, voltage regulator module
fetched: 2026-07-02
---

# Power integrity

**Power integrity** or **PI** involves a series of electronic engineering efforts aimed at ensuring that power supply subsystems adequately support the performance of an entire electronic system.

PI engineering focuses on designing and evaluating power supply subsystems to prevent any degradation in system performance due to potential adverse effects from the power supplies. For instance, a noisy power supply can cause audible or visible disturbances or slow down data communication. PI engineering employs various methods to minimize or eliminate such noise. The effectiveness of PI engineering is measured by the overall system performance, even though it specifically addresses power supply circuits. In other words, PI engineering identifies circuit blocks that are sensitive to power supply perturbations and requires careful attention.

PI is essential for achieving successful signal integrity (SI) engineering, which deals with impedance matching among multiple elements. Like SI, PI also ensures proper connections between a power supply and a load device, which is often a concern for SI. This connection path is known as a power delivery network (PDN), and tuning the PDN path from the power source to load devices is referred to as PDN impedance design.

## History

### Before 2000

In the Computer industry, the increasing power demands of Microprocessors necessitated dedicated decoupling capacitor designs for power supply buses on printed circuit boards. As a microprocessor transitions between idle and heavy computation states, it draws rapidly changing current from its power supply unit, often referred to as a voltage regulator module (VRM).

At a high level, this effort involved balancing two scenarios:

**From heavy computation state to idle state**

When a microprocessor suddenly stops drawing current from the VRM, the slower response time of the VRM compared to the microprocessor causes an increase in power bus voltage (

overshoot

). This can lead to potential over-voltage damage to the microprocessor.

**From idle state to heavy computation state**

When a microprocessor suddenly starts drawing

electric charge

from a power bus, the instantaneous current supply comes from decoupling capacitors until the VRM begins supplying current. This causes a drop in power bus voltage (undershoot), potentially leading to digital data loss as the microprocessor's internal logic circuitry may fail to maintain digital high or low states.

The engineering efforts involved in designing these decoupling capacitors laid the foundation for PDN impedance design.

## Importance of Power Integrity

- Stable operation
- Reduced noise and interference
- Thermal management
- Component longevity
- EMI Compliance and reliability

## Key Elements in Power Integrity

- Power Delivery Network (PDN)
- Voltage Ripple and Noise
- Impedance Control
- Decoupling Capacitors
- Ground Planes

## Power distribution network

The current path from the power supply through the PCB and IC package to the die (consumer) is called the power distribution network. Its role is to transfer the power to the consumers with little DC voltage drop, and to allow little ripple induced by dynamic current at the consumer (switching current). The DC voltage drop occurs if there is too much resistance in the plane or power traces leading from the VRM (Voltage Regulator Module) to the consumer. This can be countered by raising the voltage on the VRM, or extending the "sense" point of the VRM to the consumer.

Dynamic current occurs when the consumer switches its transistors, typically triggered by a clock signal. This dynamic current can be considerably larger than the static current (internal leakage) of the consumer. This fast change in current consumption can pull the voltage of the rail down, or cause it to spike, creating a voltage ripple. This change in current happens much faster than the VRM can react. The switching current must therefore be handled by decoupling capacitors.

The noise or voltage ripple must be handled differently depending on the frequency of operation. The highest frequencies must be handled on-die. This noise is decoupled by parasitic coupling on the die, and capacitive coupling between metal layers. Frequencies above 50–100 MHz must be handled on the package. This is done by on-package capacitors. Frequencies below 100 MHz are handled on the PCB by plane capacitance and using decoupling capacitors. Capacitors work on different frequencies depending on their type, capacitance and physical size. It is therefore necessary to utilize multiple capacitors of different sizes to ensure a low PDN impedance across the frequency range.

The physical size of the capacitors affect its parasitic inductance. The parasitic inductance creates impedance spikes at certain frequencies. Physically smaller capacitors are therefore better. The placement of the capacitors is of varying importance depending on its frequency of operation. The smallest value capacitors should be as close as possible to the consumer to minimize the AC current loop area. Larger capacitors in the microfarad range can be placed more or less anywhere.

### Target impedance

The target impedance is the impedance at which the ripple created by the dynamic current of the specific consumer is within the specified range. The target impedance is given by the following equation

$Z_{\textrm {Target}}={\frac {\Delta V}{\Delta I}}[\Omega ]$

In addition to the target impedance, it is important to know which frequencies it applies, and at which frequency the consumer package is responsible (this is specified in the datasheet of the specific consumer IC).

## Power Integrity Tools

- *"K-SIM". KEMET. Retrieved 2018-03-18.*
- *"CST PDN ANALYZER". Altium. Retrieved 2018-03-18.*
- *"W3036E Conducted EMI (CEMI) with PIPro". Keysight. Retrieved 2025-01-02.*
- *"HyperLynx Power Integrity". Siemens. 2018. Retrieved 2018-03-18.*
