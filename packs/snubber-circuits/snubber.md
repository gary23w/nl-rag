---
title: "Snubber"
source: https://en.wikipedia.org/wiki/Snubber
domain: snubber-circuits
license: CC-BY-SA-4.0
tags: snubber circuit, RC snubber, flyback diode, transient-voltage-suppression diode
fetched: 2026-07-02
---

# Snubber

A **snubber** is a device used to suppress ("snub") a phenomenon such as voltage transients in electrical systems, pressure transients in fluid systems (caused by for example water hammer) or excess force or rapid movement in mechanical systems.

## Electrical systems

Snubbers are frequently used in electrical systems with an inductive load where the sudden interruption of current flow leads to a large counter-electromotive force: a rise in voltage across the current switching device that opposes the change in current, in accordance with Faraday's law. This transient can be a source of electromagnetic interference (EMI) in other circuits. Additionally, if the voltage generated across the device is beyond what the device is intended to tolerate, it may damage or destroy it. The snubber provides a short-term alternative current path around the current switching device so that the inductive element may be safely discharged. Inductive elements are often unintentional, arising from the current loops implied by physical circuitry like long and/or tortuous wires. While current switching is everywhere, snubbers will generally only be required where a major current path is switched, such as in power supplies. Snubbers are also often used to prevent arcing across the contacts of relays and switches, or electrical interference, or the welding of the contacts that can occur (see also arc suppression).

### Resistor-capacitor (RC)

A simple RC snubber uses a small resistor (R) in series with a small capacitor (C). This combination can be used to suppress the rapid rise in voltage across a thyristor, preventing the erroneous turn-on of the thyristor; it does this by limiting the rate of rise in voltage ( $dV/dt$ ) across the thyristor to a value which will not trigger it. An appropriately designed RC snubber can be used with either DC or AC loads. This sort of snubber is commonly used with inductive loads such as electric motors. The voltage across a capacitor cannot change instantaneously, so a decreasing transient current will flow through it for a fraction of a second, allowing the voltage across the switch to increase more slowly when the switch is opened. Determination of voltage rating can be difficult owing to the nature of transient waveforms, and may be defined simply by the power rating of the snubber components and the application. RC snubbers can be made discretely and are also built as a single component (see also Boucherot cell).

### Diodes

When the current flowing is DC, a simple rectifier diode is often employed as a snubber. The snubber diode is wired in parallel with an inductive load (such as a relay coil or electric motor). The diode is installed so that it does not conduct under normal conditions. When the external driving current is interrupted, the inductor current flows instead through the diode. The stored energy of the inductor is then gradually dissipated by the diode voltage drop and the resistance of the inductor itself. One disadvantage of using a simple rectifier diode as a snubber is that the diode allows current to continue flowing for some time, causing the inductor to remain active for slightly longer than desired. When such a snubber is utilized in a relay, this effect may cause a significant delay in the *drop out*, or disengagement, of the actuator.

The diode must immediately enter into forward conduction mode as the driving current is interrupted. Most ordinary diodes, even "slow" power silicon diodes, are able to turn on very quickly, in contrast to their slow reverse recovery time. These are sufficient for snubbing electromechanical devices such as relays and motors.

In high-speed cases, where the switching is faster than 10 nanoseconds, such as in certain switching power regulators, "fast", "ultrafast", or Schottky diodes may be required.

### Resistor-capacitor-diode

More sophisticated designs use a diode with an RC network.

### Solid-state devices

In some DC circuits, a varistor made of inexpensive metal oxide, called a metal oxide varistor (MOV) is used.

They may be unipolar or bipolar, like two inverse-series silicon Zener diodes, but are prone to wear out after about a dozen max-rated joules of energy absorption such as lightning protection, but are suitable for lower energy.

Now with lower series resistance (Rs) in semiconductors they are generally called transient voltage suppressors (TVS), or surge protection devices (SPD).

Transient voltage suppressors (TVS) may be used instead of the simple diode. The coil diode clamp makes the relay turn off slower ( $T=L/R$ ) and thus increases contact arc if with a motor load which also needs a snubber. The diode clamp works well for coasting a uni-directional motor to a stop, but for bi-directional motors, a bipolar TVS is used.

A higher voltage Zener-like TVS may make the relay open faster than it would with a simple rectifier diode clamp, as R is higher while the voltage rises to the clamp level. A Zener diode connected to ground will protect against positive transients that go over the Zener's breakdown voltage, and will protect against negative transients greater than a normal forward diode drop.

Transient-voltage-suppression diodes are like silicon controlled rectifiers (SCRs) which trigger from overvoltage then clamp like Darlington transistors for lower voltage drop over a longer time period.

In AC circuits a rectifier diode snubber cannot be used; if a simple RC snubber is not adequate a more complex bidirectional snubber design must be used.

## Mechanical and hydraulic systems

Snubbers for pipes and equipment are used to control movement during abnormal conditions such as earthquakes, turbine trips, safety valve closure, relief valve closure, or hydraulic fuse closure. Snubbers allow for free thermal movement of a component during regular conditions, but restrain the component in irregular conditions. A hydraulic snubber allows for pipe deflection under normal operating conditions. When subjected to an impulse load, the snubber becomes activated and acts as a restraint in order to restrict pipe movement. A mechanical snubber uses mechanical means to provide the restraint force.
