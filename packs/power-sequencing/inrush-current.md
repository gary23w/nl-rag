---
title: "Inrush current"
source: https://en.wikipedia.org/wiki/Inrush_current
domain: power-sequencing
license: CC-BY-SA-4.0
tags: power-on reset, inrush current, hot swapping, power management integrated circuit
fetched: 2026-07-02
---

# Inrush current

**Inrush current**, **input surge current**, or **switch-on surge** is the maximal instantaneous input current drawn by an electrical device when first turned on. Alternating-current electric motors and transformers may draw several times their normal full-load current when first energized, for a few cycles of the input waveform. Power converters also often have inrush currents much higher than their steady-state currents, due to the charging current of the input capacitance. The selection of over-current-protection devices such as fuses and circuit breakers is made more complicated when high inrush currents must be tolerated. The over-current protection must react quickly to overload or short-circuit faults but must not interrupt the circuit when the (usually harmless) inrush current flows.

## Capacitors

A discharged or partially charged capacitor appears as a short circuit to the source when the source voltage is higher than the potential of the capacitor. A fully discharged capacitor will take approximately 5 *RC* time periods to fully charge; during the charging period, instantaneous current can exceed steady-state current by a substantial multiple. Instantaneous current declines to steady-state current as the capacitor reaches full charge. In the case of open circuit, the capacitor will be charged to the peak AC voltage (one cannot actually charge a capacitor with AC line power, so this refers to a varying but unidirectional voltage; e.g., the voltage output from a rectifier).

In the case of charging a capacitor from a linear DC voltage, like that from a battery, the capacitor will still appear as a short circuit; it will draw current from the source limited only by the internal resistance of the source and ESR of the capacitor. In this case, charging current will be continuous and decline exponentially to the load current. For open circuit, the capacitor will be charged to the DC voltage.

Safeguarding against the filter capacitor’s charging period’s initial current inrush flow is crucial for the performance of the device. Temporarily introducing a high resistance between the input power and rectifier can increase the resistance of the powerup, leading to reducing the inrush current. Using an inrush current limiter for this purpose helps, as it can provide the initial resistance needed.

## Transformers

When a transformer is first energized, a transient current up to 10 to 15 times larger than the rated transformer current can flow for several cycles. Toroidal transformers, using less copper for the same power handling, can have up to 60 times inrush to running current. Worst-case inrush happens when the primary winding is connected at an instant around the zero crossing of the primary voltage (which for a pure inductance would be the current maximum in the AC cycle) and if the polarity of the voltage half-cycle has the same polarity as the remanence in the iron core has (the magnetic remanence was left high from a preceding half cycle). Unless the windings and core are sized to normally never exceed 50% of saturation (and in an efficient transformer they never are, such a construction would be overly heavy and inefficient), then during such a start-up the core will be saturated. This can also be expressed as the remnant magnetism in normal operation is nearly as high as the saturation magnetism at the "knee" of the hysteresis loop. Once the core saturates, however, the winding inductance appears greatly reduced, and only the resistance of the primary-side windings and the impedance of the power line are limiting the current. As saturation occurs for part half-cycles only, harmonic-rich waveforms can be generated and can cause problems to other equipment. For large transformers with low winding resistance and high inductance, these inrush currents can last for several seconds until the transient has died away (decay time proportional to *X*L/*R*) and the regular AC equilibrium is established. To avoid magnetic inrush, only for transformers with an air gap in the core, the inductive load needs to be synchronously connected near a supply voltage peak, in contrast with the zero-voltage switching, which is desirable to minimize sharp-edged current transients with resistive loads such as high-power heaters. But for toroidal transformers only a premagnetising procedure before switching on allows to start those transformers without any inrush-current peak.

Inrush current can be divided in three categories:

Energization inrush current

result of re-energization of transformer. The residual flux in this case can be zero or depending on energization timing.

Recovery inrush current

flow when transformer voltage is restored after having been reduced by system disturbance.

Sympathetic inrush current

flow when multiple transformer connected in same line and one of them energized.

## Motors

When an electric motor, AC or DC, is first energized, the rotor is not moving, and a current equivalent to the stalled current will flow, reducing as the motor picks up speed and develops a back EMF to oppose the supply. AC induction motors behave as transformers with a shorted secondary until the rotor begins to move, while brushed motors present essentially the winding resistance. The duration of the starting transient is less if the mechanical load on the motor is relieved until it has picked up speed.

For high-power motors, the winding configuration may be changed (wye at start and then delta) during start-up to reduce the current drawn.

## Heaters and filament lamps

Metals have a positive temperature coefficient of resistance; they have lower resistance when cold. Any electrical load that contains a substantial component of metallic resistive heating elements, such as an electric kiln or a bank of tungsten-filament incandescent bulbs, will draw a high current until the metallic element reaches operating temperature. For example, wall switches intended to control incandescent lamps will have a "T" rating, indicating that they can safely control circuits with the large inrush currents of incandescent lamps. The inrush may be as much as 14 times the steady-state current and may persist for a few milliseconds for smaller lamps up to several seconds for lamps of 500 watts or more. (Non-graphitized) carbon-filament lamps, rarely used now, have a negative temperature coefficient and draw more current as they warm up; an "inrush" current is not found with these types.

## Protection

A resistor in series with the line can be used to limit the current charging input capacitors. However, this approach is not very efficient, especially in high-power devices, since the resistor will have a voltage drop and dissipate some power.

Inrush current can also be reduced by inrush current limiters. Negative-temperature-coefficient (NTC) thermistors are commonly used in switching power supplies, motor drives and audio equipment to prevent damage caused by inrush current. A thermistor is a thermally-sensitive resistor with a resistance that changes significantly and predictably as a result of temperature changes. The resistance of an NTC thermistor decreases as its temperature increases.

As the inrush current limiter self-heats, the current begins to flow through it and warm it. Its resistance begins to drop, and a relatively small current flow charges the input capacitors. After the capacitors in the power supply become charged, the self-heated inrush current limiter offers little resistance in the circuit, with a low voltage drop with respect to the total voltage drop of the circuit. A disadvantage is that immediately after the device is switched off, the NTC resistor is still hot and has a low resistance. It cannot limit the inrush current unless it cools for more than 1 minute to get a higher resistance. Another disadvantage is that the NTC thermistor is not short-circuit-proof.

Another way to avoid the transformer inrush current is a "transformer switching relay". This does not need time for cool down. It can also deal with power-line half-wave voltage dips and is short-circuit-proof. This technique is important for IEC 61000-4-11 tests.

Another option, particularly for high-voltage circuits, is to use a pre-charge circuit. The circuit would support a current-limited precharge mode during the charging of capacitors and then switch to an unlimited mode for normal operation when the voltage on the load is 90% of full charge.

## Switch-off spike

When a transformer, electric motor, electromagnet, or other inductive load is switched off, the inductor increases the voltage across the switch or breaker and can cause extended arcing. When a transformer is switched off on its primary side, inductive kick produces a voltage spike on the secondary that can damage insulation and connected loads.
