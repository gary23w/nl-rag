---
title: "Active rectification"
source: https://en.wikipedia.org/wiki/Active_rectification
domain: diode-bridge
license: CC-BY-SA-4.0
tags: diode bridge
fetched: 2026-07-03
---

# Active rectification

**Active rectification**, or **synchronous rectification**, is a technique for improving the efficiency of rectification by replacing diodes with actively controlled switches, usually power MOSFETs or power bipolar junction transistors (BJT). Whereas normal semiconductor diodes have a roughly fixed voltage drop of around 0.5 to 1 volts, active rectifiers behave as resistances, and can have arbitrarily low voltage drop.

Historically, vibrator-driven switches or motor-driven commutators have also been used for mechanical rectifiers and synchronous rectification.

Active rectification has many applications. It is frequently used for arrays of photovoltaic panels to avoid reverse current flow that can cause overheating with partial shading while giving minimum power loss. It is also used in switched-mode power supplies (SMPS).

## Motivation

The constant voltage drop of a standard p-n junction diode is typically between 0.7 V and 1.7 V, causing significant power loss in the diode. Electric power depends on current and voltage: the power loss rises proportional to both current and voltage.

In low voltage converters (around 10 volts and less), the voltage drop of a diode (typically around 0.7 to 1 volt for a silicon diode at its rated current) has an adverse effect on efficiency. One classic solution replaces standard silicon diodes with Schottky diodes, which exhibit very low voltage drops (as low as 0.3 volts). However, even Schottky rectifiers can be significantly more lossy than the synchronous type, notably at high currents and low voltages.

When addressing very low-voltage converters, such as a buck converter power supply for a computer CPU (with a voltage output around 1 volt, and many amperes of output current), Schottky rectification does not provide adequate efficiency. In such applications, active rectification becomes necessary.

## Description

Replacing a diode with an actively controlled switching element such as a MOSFET is the heart of active rectification. MOSFETs have a constant very low resistance when conducting, known as on-resistance (RDS(on)). A typical modern MOSFET has an on-resistance of less than an ohm, with many high-performance devices having specifications of on the order of 10 mΩ or less. The voltage drop across the transistor is then much lower, causing a reduction in power loss and a gain in efficiency. However, Ohm's law governs the voltage drop across the MOSFET, meaning that at high currents, the drop can exceed that of a diode. This limitation is usually dealt with either by placing several transistors in parallel, thereby reducing the current through each individual one, or by using a device with more active area (on FETs, a device-equivalent of parallel).

The control circuitry for active rectification usually uses comparators to sense the voltage of the input AC and open the transistors at the correct times to allow current to flow in the correct direction. The timing is very important, as a short circuit across the input power must be avoided and can easily be caused by one transistor turning on before another has turned off. Active rectifiers also clearly still need the smoothing capacitors present in passive examples to provide smoother power than rectification does alone.

Using active rectification to implement AC/DC conversion allows a design to undergo further improvements (with more complexity) to achieve an active power factor correction, which forces the current waveform of the AC source to follow the voltage waveform, eliminating reactive currents and allowing the total system to achieve greater efficiency.

## MOSFET-based ideal diode

A MOSFET actively controlled to act as a rectifier—actively turned on to allow current in one direction but actively turned off to block current from flowing the other direction—is sometimes called an *ideal diode*.

Using these ideal diodes rather than standard diodes for solar electric panel bypass, reverse-battery protection, or bridge rectifiers reduces the amount of power dissipated in the diodes, improving efficiency and reducing the size of the circuit board and the weight of the heat sink required to deal with the power dissipation.

Such a MOSFET-based ideal diode is not to be confused with an op-amp based super diode, often called a precision rectifier.

## Construction

See H-bridge.
