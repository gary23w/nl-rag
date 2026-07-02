---
title: "Shunt (electrical)"
source: https://en.wikipedia.org/wiki/Shunt_(electrical)
domain: current-sensing
license: CC-BY-SA-4.0
tags: current sensor, current clamp, rogowski coil, current transformer
fetched: 2026-07-02
---

# Shunt (electrical)

A **shunt** is a device designed to provide a low-impedance path for an electrical current in a circuit. It is typically used to divert current away from a system or component in order to prevent overcurrent. Electrical shunts are used in a wide variety of applications including power distribution systems, electrical measurement systems, automotive and marine applications. Shunts take many physical forms depending on their application. In current measurement, a shunt is a resistor of very low but precisely known resistance placed in parallel with a meter, allowing large currents to be measured indirectly via the voltage drop across it. In circuit protection, shunt devices such as crowbar circuits guard against overvoltage by short-circuiting the supply. Capacitors are employed as shunts to redirect high-frequency electrical noise to ground. In photovoltaics, the term describes an unwanted short circuit within a solar cell, while in lightning protection, gas-filled tubes act as shunts to safely conduct surge energy to ground. On warships, battle short shunts are installed across fuses for essential equipment before entering combat.

## Defective device bypass

One example is in miniature Christmas lights which are wired in series. When the filament burns out in one of the incandescent light bulbs, the full line voltage appears across the burnt out bulb. A shunt resistor, which has been connected in parallel across the filament before it burnt out, will then short out to bypass the burnt filament and allow the rest of the string to light. If too many lights burn out however, a shunt will also burn out, requiring the use of a multimeter to find the point of failure.

## Photovoltaics

In photovoltaics, the term is widely used to describe an unwanted short circuit between the front and back surface contacts of a solar cell, usually caused by wafer damage.

## Lightning arrestor

A gas-filled tube can also be used as a shunt, particularly in a lightning arrester. Neon, like other noble gases, has a high breakdown voltage, so that normally current will not flow across it. However, a direct lightning strike (such as on a radio tower antenna) will cause the shunt to arc and conduct the massive amount of electricity to ground, protecting transmitters and other equipment.

Another older form of lightning arrester employs a simple narrow spark gap, over which an arc will jump when a high voltage is present. While a low cost solution, its high triggering voltage offers almost no protection for modern solid-state electronic devices powered by the protected circuit.

## Electrical noise bypass

Capacitors are used as shunts to redirect high-frequency noise to ground before it can propagate to the load or other circuit components.

## Use in electronic filter circuits

The term shunt is used in filter and similar circuits with a ladder topology to refer to the components connected between the line and common. The term is used in this context to distinguish the shunt components connected between the signal and return lines from the components connected in series along the signal line. More generally, the term shunt can be used for a component connected in parallel with another. For instance, *shunt m-derived half section* is a common filter section from the image impedance method of filter design.

## Diodes as shunts

Where devices are vulnerable to reverse polarity of a signal or power supply, a diode may be used to protect the circuit. If connected in series with the circuit it simply prevents reversed current, but if connected in parallel it can shunt the reversed supply, causing a fuse or other current limiting circuit to open.

All semiconductor diodes have a threshold voltage – typically between 0.5 volt and 1 volt – that must be exceeded before significant current will flow through the diode in the normally allowed direction. Two anti-parallel shunt diodes (one to conduct current in each direction) can be used to limit the signal flowing past them to no more than their threshold voltages, in order to protect later components from overload.

## Shunts as circuit protection

When a circuit must be protected from overvoltage and there are failure modes in the power supply that can produce such overvoltages, the circuit may be protected by a device commonly called a crowbar circuit. When this device detects an overvoltage it causes a short circuit between the power supply and its return. This will cause both an immediate drop in voltage (protecting the device) and an instantaneous high current which is expected to open a current sensitive device (such as a fuse or circuit breaker). This device is called a *crowbar* as it is likened to dropping an actual crowbar across a set of bus bars (exposed electrical conductors).

## Battle short

On warships, it is common to install battle short shunts across fuses for essential equipment before entering combat. This bypasses overcurrent protection at a time when removing power to the equipment is not an appropriate reaction.

## Shunting an instrument but series connected in circuit

This figure shows that the term "shunt resistor" should be understood in the context of what it shunts.

In this example the resistor RL would be understood as "the shunt resistor" (to the load L), because this resistor would pass current around the load L. RL is connected in parallel with the load L.

However, the series resistors RM1 and RM2 are low Ohmic resistors (like in the photo) meant to pass current around the instruments M1 and M2, and function as shunt resistors to those instruments. RM1 and RM2 are connected in parallel with M1 and M2. If seen without the instruments these two resistors would be considered series resistors in this circuit.

## Use in current measuring

An ammeter shunt allows the measurement of current values too large to be directly measured by a particular ammeter. In this case, a separate shunt, a resistor of very low but accurately known resistance, is placed in parallel with a voltmeter, so that virtually all of the current to be measured will flow through the shunt (provided that the very high internal resistance of the voltmeter takes such a low portion of the current that it can be considered negligible). The resistance is chosen so that the resultant voltage drop is measurable but low enough not to disrupt the circuit. The voltage across the shunt is proportional to the current flowing through it, and so the measured voltage can be scaled to directly display the current value.

Shunts are rated by maximum current and voltage drop at that current. For example, a 500 A, 75 mV shunt would have a resistance of 150 microohm, a maximum allowable current of 500 amps and at that current the voltage drop would be 75 millivolts. By convention, most shunts are designed to drop 50 mV, 75 mV or 100 mV when operating at their full rated current and most ammeters consist of a shunt and a voltmeter with full-scale deflections of 50, 75, or 100 mV. All shunts have a derating factor for continuous (more than 2 minutes) use, 66% being the most common, so the example shunt should not be operated above 330 A (and 50 mV drop) longer than that.

This limitation is due to thermal limits at which a shunt will no longer operate correctly. For manganin, a common shunt material, at 80 °C thermal drift begins to occur, at 120 °C thermal drift is a significant problem where error, depending on the design of the shunt, can be several percent and at 140 °C the manganin alloy becomes permanently damaged due to annealing resulting in the resistance value drifting up or down.

If the current being measured is also at a high voltage potential this voltage will be present in the connecting leads too and in the reading instrument itself. Sometimes, the shunt is inserted in the return leg (grounded side) to avoid this problem. Some alternatives to shunts can provide isolation from the high voltage by not directly connecting the meter to the high voltage circuit. Examples of devices that can provide this isolation are Hall effect current sensors and current transformers (see clamp meters). Current shunts are considered more accurate and cheaper than Hall effect devices. Common accuracy specifications of such devices are ±0.1%, ±0.25% or ±0.5%.

The Thomas-type double manganin walled shunt and MI type (improved Thomas-type design) were used by NIST and other standards laboratories as the legal reference of an ohm until superseded in 1990 by the quantum Hall effect. Thomas-type shunts are still used as secondary standards to take very accurate current measurements, as using quantum Hall effect is a time-consuming process. The accuracy of these types of shunts is measured in the ppm and sub-ppm scale of drift per year of set resistance.

Where the circuit is grounded (earthed) on one side, a current measuring shunt can be inserted either in the ungrounded conductor or in the grounded conductor. A shunt in the ungrounded conductor must be insulated for the full circuit voltage to ground; the measuring instrument must be inherently isolated from ground or must include a resistive voltage divider or an isolation amplifier between the relatively high common-mode voltage and lower voltages inside the instrument. A shunt in the grounded conductor may not detect leakage current that bypasses the shunt, but it will not experience high common-mode voltage to ground. The load is removed from a direct path to ground, which may create problems for control circuitry, result in unwanted emissions, or both.

- (Low-side insertion can eliminate common-mode voltage, but if there are other paths to ground, the shunt will not measure this leakage current.)Low-side insertion can eliminate common-mode voltage, but if there are other paths to ground, the shunt will not measure this leakage current.
- (High-side insertion allows measurement of all current, including leakage current, but guarantees common-mode voltage.)High-side insertion allows measurement of all current, including leakage current, but guarantees common-mode voltage.
- (Isolated amplifiers resolve all the difficulties and limitations with high- or low-side current shunt measurements.)Isolated amplifiers resolve all the difficulties and limitations with high- or low-side current shunt measurements.
