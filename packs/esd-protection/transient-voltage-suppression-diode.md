---
title: "Transient-voltage-suppression diode"
source: https://en.wikipedia.org/wiki/Transient-voltage-suppression_diode
domain: esd-protection
license: CC-BY-SA-4.0
tags: electrostatic discharge, human body model, ohmic contact, clamp diode
fetched: 2026-07-02
---

# Transient-voltage-suppression diode

A **transient-voltage-suppression** (**TVS**) **diode**, also **transil**, **transorb** or **thyrector**, is an electronic component used to protect electronics from voltage spikes induced on connected wires.

## Description

The device operates by shunting excess current when the induced voltage exceeds the avalanche breakdown potential. It is a clamping device, suppressing all overvoltages above its breakdown voltage. It automatically resets when the overvoltage goes away, but absorbs much more of the transient energy internally than a similarly rated crowbar device.

| Comparison of TVS Components |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
| Component type | Protection time | Protection voltage | Power dissipation | Reliable performance | Expected life | Other considerations |
| Avalanche TVS | 50 ps | 3−400 V | Low | Yes | Long | Low power dissipation. Bidirectional also available. |
| Thyristor TVS | < 3 ns | 30−400 V | None | Yes | Long | High capacitance. Temperature sensitive. |
| MOV | 10−20 ns | > 300 V | None | No | Degrades | Fusing required. Degrades. Voltage level too high. |
| Gas discharge tube | > 1 μs | 60−100 V | None | No | Limited | Only 50−2500 surges. Can short power line. |

A transient-voltage-suppression diode may be either unidirectional or bidirectional. A unidirectional device operates as a rectifier in the forward direction like any other avalanche diode, but is made and tested to handle very large peak currents.

A bidirectional transient-voltage-suppression diode can be represented by two mutually opposing avalanche diodes in series with one another and connected in parallel with the circuit to be protected. While this representation is schematically accurate, physically the devices are now manufactured as a single component.

A transient-voltage-suppression diode can respond to over-voltages faster than other common over-voltage protection components such as varistors or gas discharge tubes. The actual clamping occurs in roughly one picosecond, but in a practical circuit the inductance of the wires leading to the device imposes a higher limit. This makes transient-voltage-suppression diodes useful for protection against very fast and often damaging voltage transients. These fast over-voltage transients are present on all distribution networks and can be caused by either internal or external events, such as lightning or motor arcing.

Transient voltage suppressors will fail if they are subjected to voltages or conditions beyond those that the particular product was designed to accommodate. There are three key modes in which the TVS will fail: short, open, and degraded device.

TVS diodes are sometimes referred to as transorbs, from the Vishay trademark *TransZorb*.

## Characterization

A TVS diode is characterized by:

- Leakage current: the amount of current conducted when voltage applied is below the maximum reverse standoff voltage.
- Maximum reverse standoff voltage: the voltage below which no significant conduction occurs.
- Breakdown voltage: the voltage at which some specified and significant conduction occurs.
- Clamping voltage: the voltage at which the device will conduct its fully rated current (hundreds to thousands of amperes).
- Parasitic capacitance: The nonconducting diode behaves like a capacitor, which can distort and corrupt high-speed signals. Lower capacitance is generally preferred.
- Parasitic impedance: Because the actual over voltage switching is so fast, the package inductance is the limiting factor for response speed.
- Amount of energy it can absorb: Because the transients are so brief, all of the energy is initially stored internally as heat; a heat sink only affects the time to cool down afterwards. Thus, a high-energy TVS must be physically large. If this capacity is too small, the over voltage will possibly destroy the device and leave the circuit unprotected.
