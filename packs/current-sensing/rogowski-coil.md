---
title: "Rogowski coil"
source: https://en.wikipedia.org/wiki/Rogowski_coil
domain: current-sensing
license: CC-BY-SA-4.0
tags: current sensor, current clamp, rogowski coil, current transformer
fetched: 2026-07-02
---

# Rogowski coil

A **Rogowski coil**, named after Walter Rogowski, is an electrical device for measuring alternating current (AC) or high-speed current pulses. It sometimes consists of a helical coil of wire with the lead from one end returning through the centre of the coil to the other end so that both terminals are at the same end of the coil. This approach is sometimes referred to as a *counter-wound* Rogowski.

Other approaches use a full toroid geometry that has the advantage of a central excitation not exciting standing waves in the coil. The whole assembly is then wrapped around the straight conductor whose current is to be measured. There is no metal (iron) core. The winding density, the diameter of the coil and the rigidity of the winding are critical for preserving immunity to external fields and low sensitivity to the positioning of the measured conductor.

Since the voltage that is induced in the coil is proportional to the rate of change (derivative) of current in the straight conductor, the output of the Rogowski coil is usually connected to an electrical (or electronic) integrator circuit to provide an output signal that is proportional to the current. Single-chip signal processors with built-in analog to digital converters are often used for this purpose. If the ratio of the coil's inductance to its resistance (the RL time constant) is significantly greater than the length of the current pulse being measured, the coil is considered "self integrating". When both ends of the coil are connected together, the current in the coil is proportional to the current being measured. Connecting the ends of the coil together through a low-value resistor allows the current to be measured by measuring the voltage drop over the resistor. Thus, the device produces an output voltage proportional to the current being measured.

## Advantages

This type of coil has advantages over other types of current transformers.

- It is not a closed loop, because the second terminal is passed back through the center of the toroid core (commonly a plastic or rubber tube) and connected along the first terminal. This allows the coil to be open-ended and flexible, allowing it to be wrapped around a live conductor without disturbing it. However, positioning of the measured conductor is important in that case: It has been shown that, with flexible sensors, the effect of the position on the accuracy ranges from 1 to 3%. Another technique uses two rigid winding halves with a precise locking mechanism.
- Due to its low inductance, it can respond to fast-changing currents, down to several nanoseconds.
- Because it has no iron core to saturate, it is highly linear even when subjected to large currents, such as those used in electric power transmission, welding, or pulsed power applications. This linearity also enables a high-current Rogowski coil to be calibrated using much smaller reference currents.
- No danger of opening the secondary winding.
- Lower construction costs.
- Temperature compensation is simple.
- For larger currents conventional current transformers require an increase of the number of secondary turns, in order to keep the output current constant. Therefore, a Rogowski coil for large current is smaller than an equivalent rating current transformer.

## Disadvantages

This type of coil also has some disadvantages over other types of current transformers.

- The output of the coil must be passed through an integrator circuit to obtain the current waveform. The integrator circuit requires power, typically 3–24 V DC, and many commercial sensors obtain this from batteries.
- Traditional split-core current transformers do not require integrator circuits. The integrator is lossy, so the Rogowski coil does not have a response down to DC; neither does a conventional current transformer (see Néel effect coils for DC). However, they can measure very slow changing currents with frequency components down to 1 Hz and less.
- Constant DC current cannot be measured. The Rogowski coil samples the field, generating a voltage as the field changes.

## Applications

Rogowski coils are used for current monitoring in precision welding systems, arc melting furnaces, or electromagnetic launchers. They are also used in short-circuit testing of electric generators and as sensors in protection systems of electrical plants. Another field of usage is the measurement of harmonic current content, due to their high linearity. Also for lightning research.

## Formulae

The voltage produced by a Rogowski coil is $v(t)={\frac {-AN\mu _{0}}{l}}{\frac {dI(t)}{dt}},$

where

- $A=\pi r^{2}$ is the area of one of the small loops,
- N is the number of turns,
- $l=2\pi R$ is the length of the winding (the circumference of the ring),
- ${\frac {dI(t)}{dt}}$ is the rate of change of the current threading the loop,
- $\mu _{0}=4\pi \times 10^{-7}$ V·s/(A·m) is the magnetic constant,
- R is the major radius of the toroid,
- r is its minor radius.

This formula assumes the turns are evenly spaced and that these turns are small relative to the radius of the coil itself.

The output of the Rogowski coil is proportional to the derivative of the wire current. The output is often integrated so the output is proportional to the wire's current: $V_{\text{out}}=\int v\,dt={\frac {-AN\mu _{0}}{l}}I(t)+C_{\text{integration}}.$ In practice, an instrument will use a lossy integrator with a time constant much less than the lowest frequency of interest. The lossy integrator will reduce the effects of offset voltages and set the constant of integration to zero.

At high frequencies, the Rogowski coil's inductance will decrease its output.

The inductance of a toroid is $L=\mu _{0}N^{2}\left(R-{\sqrt {R^{2}-r^{2}}}\right).$

## Similar devices

A device similar to the Rogowski coil was described by Arthur Prince Chattock of Bristol University in 1887. Chattock used it to measure magnetic fields rather than currents. The definitive description was given by Walter Rogowski and W. Steinhaus in 1912.

More recently, low-cost current sensors based on the principle of a Rogowski coil have been developed. These sensors share the principles of a Rogowski coil, measuring the rate of change of current using a transformer with no magnetic core. The difference from the traditional Rogowski coil is that the sensor can be manufactured using a planar coil rather than a toroidal coil. In order to reject the influence of conductors outside the sensor's measurement region, these planar Rogowski current sensors use a concentric coil geometry instead of a toroidal geometry to limit the response to external fields. The main advantage of the planar Rogowski current sensor is that the coil winding precision that is a requirement for accuracy can be achieved using low-cost printed circuit board manufacturing.
