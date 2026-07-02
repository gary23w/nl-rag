---
title: "Linear variable differential transformer"
source: https://en.wikipedia.org/wiki/Linear_variable_differential_transformer
domain: inductive-sensing
license: CC-BY-SA-4.0
tags: inductive sensor, eddy current, inductance measurement, linear variable differential transformer
fetched: 2026-07-02
---

# Linear variable differential transformer

The **linear variable differential transformer** (**LVDT**) – also called **linear variable displacement transformer**, **linear variable displacement transducer**, or simply **differential transformer** – is a type of electrical transformer used for measuring linear displacement (position along a given direction). It is the base of LVDT-type displacement sensors. A counterpart to this device that is used for measuring rotary displacement is called a *rotary variable differential transformer* (RVDT).

## Introduction

LVDTs are robust, absolute linear position/displacement transducers; inherently frictionless, they have a virtually infinite cycle life when properly used. As AC operated LVDTs do not contain any electronics, they can be designed to operate at cryogenic temperatures or up to 1200 °F (650 °C), in harsh environments, and under high vibration and shock levels. LVDTs have been widely used in applications such as power turbines, hydraulics, automation, aircraft, satellites, nuclear reactors, and many others. These transducers have low hysteresis and excellent repeatability.

The LVDT converts a position or linear displacement from a mechanical reference (zero or null position) into a proportional electrical signal containing phase (for direction) and amplitude (for distance) information. The LVDT operation does not require an electrical contact between the moving part (probe or core assembly) and the coil assembly, but instead relies on electromagnetic coupling.

## Operation

The linear variable differential transformer has three solenoidal coils placed end-to-end around a tube. The center coil is the primary, and the two outer coils are the top and bottom secondaries. A cylindrical ferromagnetic core, attached to the object whose position is to be measured, slides along the axis of the tube. An alternating current drives the primary and causes a voltage to be induced in each secondary proportional to the length of the core linking to the secondary. The frequency is usually in the range 1 to 10 kHz.

As the core moves, the primary's linkage to the two secondary coils changes and causes the induced voltages to change. The coils are connected so that the output voltage is the difference (hence "differential") between the top secondary voltage and the bottom secondary voltage. When the core is in its central position, equidistant between the two secondaries, equal voltages are induced in the two secondary coils, but the two signals cancel, so the output voltage is theoretically zero. In practice minor variations in the way in which the primary is coupled to each secondary means that a small voltage is output when the core is central.

This small residual voltage is due to phase shift and is often called quadrature error. It is a nuisance in closed loop control systems as it can result in oscillation about the null point, and may also be unacceptable in simple measurement applications. It is a consequence of using synchronous demodulation, with direct subtraction of the secondary voltages at AC. Modern systems, particularly those involving safety, require fault detection of the LVDT, and the normal method is to demodulate each secondary separately, using precision half wave or full wave rectifiers, based on op-amps, and compute the difference by subtracting the DC signals. Because, for constant excitation voltage, the sum of the two secondary voltages is almost constant throughout the operating stroke of the LVDT, its value remains within a small window and can be monitored such that any internal failures of the LVDT will cause the sum voltage to deviate from its limits and be rapidly detected, causing a fault to be indicated. There is no quadrature error with this scheme, and the position-dependent difference voltage passes smoothly through zero at the null point.

Where digital processing in the form of a microprocessor or FPGA is available in the system, it is customary for the processing device to carry out the fault detection, and possibly ratiometric processing to improve accuracy, by dividing the difference in secondary voltages by the sum of the secondary voltages, to make the measurement independent of the exact amplitude of the excitation signal. If sufficient digital processing capacity is available, it is becoming commonplace to use this to generate the sinusoidal excitation via a DAC and possibly also perform the secondary demodulation via a multiplexed ADC.

When the core is displaced toward the top, the voltage in top secondary coil increases as the voltage in the bottom decreases. The resulting output voltage increases from zero. This voltage is in phase with the primary voltage. When the core moves in the other direction, the output voltage also increases from zero, but its phase is opposite to that of the primary. The phase of the output voltage determines the direction of the displacement (up or down) and amplitude indicates the amount of displacement. A synchronous detector can determine a signed output voltage that relates to the displacement.

The LVDT is designed with long slender coils to make the output voltage essentially linear over displacement up to several inches (several hundred millimetres) long.

The LVDT can be used as an absolute position sensor. Even if the power is switched off, on restarting it, the LVDT shows the same measurement, and no positional information is lost. Its biggest advantages are repeatability and reproducibility once it is properly configured. Also, apart from the uni-axial linear motion of the core, any other movements such as the rotation of the core around the axis will not affect its measurements.

Because the sliding core does not touch the inside of the tube, it can move without friction, making the LVDT a highly reliable device. The absence of any sliding or rotating contacts allows the LVDT to be completely sealed against the environment.

LVDTs are commonly used for position feedback in servomechanisms, and for automated measurement in machine tools and many other industrial and scientific applications.
