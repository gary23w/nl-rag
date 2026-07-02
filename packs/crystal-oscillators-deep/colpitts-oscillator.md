---
title: "Colpitts oscillator"
source: https://en.wikipedia.org/wiki/Colpitts_oscillator
domain: crystal-oscillators-deep
license: CC-BY-SA-4.0
tags: crystal oscillator, colpitts oscillator, pierce oscillator, quartz clock
fetched: 2026-07-02
---

# Colpitts oscillator

A **Colpitts oscillator**, invented in 1918 by Canadian-American engineer Edwin H. Colpitts using vacuum tubes, is one of a number of designs for LC oscillators, electronic oscillators that use a combination of inductors (L) and capacitors (C) to produce an oscillation at a certain frequency. The distinguishing feature of the Colpitts oscillator is that the feedback for the active device is taken from a voltage divider made of two capacitors in series across the inductor.

## Overview

Figure 1: Simple

common-base

Colpitts oscillator (with simplified

biasing

)

Figure 2: Simple

common-collector

Colpitts oscillator (with simplified

biasing

)

The Colpitts circuit, like other LC oscillators, consists of a gain device (such as a bipolar junction transistor, field-effect transistor, operational amplifier, or vacuum tube) with its output connected to its input in a feedback loop containing a parallel LC circuit (tuned circuit), which functions as a bandpass filter to set the frequency of oscillation. The amplifier will have differing input and output impedances, and these need to be coupled into the LC circuit without overly damping it.

A Colpitts oscillator uses a pair of capacitors to provide voltage division to couple the energy in and out of the tuned circuit. (It can be considered as the electrical dual of a Hartley oscillator, where the feedback signal is taken from an "inductive" voltage divider consisting of two coils in series (or a tapped coil).) Fig. 1 shows the common-base Colpitts circuit. The inductor *L* and the series combination of *C*1 and *C*2 form the resonant tank circuit, which determines the frequency of the oscillator. The voltage across *C*2 is applied to the base-emitter junction of the transistor, as feedback to create oscillations. Fig. 2 shows the common-collector version. Here the voltage across *C*1 provides feedback. The frequency of oscillation is approximately the resonant frequency of the LC circuit, which is the series combination of the two capacitors in parallel with the inductor:

$f_{0}={\frac {1}{2\pi {\sqrt {L{\frac {C_{1}C_{2}}{C_{1}+C_{2}}}}}}}.$

The actual frequency of oscillation will be slightly lower due to junction capacitances and resistive loading of the transistor.

As with any oscillator, the amplification of the active component should be marginally larger than the attenuation of the resonator losses and its voltage division, to obtain stable operation. Thus, a Colpitts oscillator used as a variable-frequency oscillator (VFO) performs best when a variable inductance is used for tuning, as opposed to tuning just one of the two capacitors. If tuning by variable capacitor is needed, it should be done with a third capacitor connected in parallel to the inductor (or in series as in the Clapp oscillator).

### Practical example

Fig. 3 shows an example with component values. Instead of field-effect transistors, other active components such as bipolar junction transistors or vacuum tubes, capable of producing gain at the desired frequency, could be used.

The common gate amplifier has a low input impedance and a high output impedance. Therefore, the amplifier input, the source, is connected to the low impedance tap of the LC circuit L1, C1, C2, C3 and the amplifier output, the drain, is connected to the high impedance top of the LC circuit. The resistor R1 sets the operating point to 0.5mA drain current with no oscillating. The output is at the low impedance tap and can drive some load. Still, this circuit has low harmonic distortion. An additional variable capacitor between drain of J1 and ground allows to change the frequency of the circuit. The load resistor RL is part of the simulation, not part of the circuit.

## Theory

One method of oscillator analysis is to determine the input impedance of an input port neglecting any reactive components. If the impedance yields a negative resistance term, oscillation is possible. This method will be used here to determine conditions of oscillation and the frequency of oscillation.

An ideal model is shown to the right. This configuration models the common collector circuit in the section above. For initial analysis, parasitic elements and device non-linearities will be ignored. These terms can be included later in a more rigorous analysis. Even with these approximations, acceptable comparison with experimental results is possible.

Ignoring the inductor, the input impedance at the base can be written as

$Z_{\text{in}}={\frac {v_{1}}{i_{1}}},$

where $v_{1}$ is the input voltage, and $i_{1}$ is the input current. The voltage $v_{2}$ is given by

$v_{2}=i_{2}Z_{2},$

where $Z_{2}$ is the impedance of $C_{2}$ . The current flowing into $C_{2}$ is $i_{2}$ , which is the sum of two currents:

$i_{2}=i_{1}+i_{s},$

where $i_{s}$ is the current supplied by the transistor. $i_{s}$ is a dependent current source given by

$i_{s}=g_{m}(v_{1}-v_{2}),$

where $g_{m}$ is the transconductance of the transistor. The input current $i_{1}$ is given by

$i_{1}={\frac {v_{1}-v_{2}}{Z_{1}}},$

where $Z_{1}$ is the impedance of $C_{1}$ . Solving for $v_{2}$ and substituting above yields

$Z_{\text{in}}=Z_{1}+Z_{2}+g_{m}Z_{1}Z_{2}.$

The input impedance appears as the two capacitors in series with the term $R_{\text{in}}$ , which is proportional to the product of the two impedances:

$R_{\text{in}}=g_{m}Z_{1}Z_{2}.$

If $Z_{1}$ and $Z_{2}$ are complex and of the same sign, then $R_{\text{in}}$ will be a negative resistance. If the impedances for $Z_{1}$ and $Z_{2}$ are substituted, $R_{\text{in}}$ is

$R_{\text{in}}={\frac {-g_{m}}{\omega ^{2}C_{1}C_{2}}}.$

If an inductor is connected to the input, then the circuit will oscillate if the magnitude of the negative resistance is greater than the resistance of the inductor and any stray elements. The frequency of oscillation is as given in the previous section.

For the example oscillator above, the emitter current is roughly 1 mA. The transconductance is roughly 40 mS. Given all other values, the input resistance is roughly

$R_{\text{in}}=-30\ \Omega .$

This value should be sufficient to overcome any positive resistance in the circuit. By inspection, oscillation is more likely for larger values of transconductance and smaller values of capacitance. A more complicated analysis of the common-base oscillator reveals that a low-frequency amplifier voltage gain must be at least 4 to achieve oscillation. The low-frequency gain is given by

$A_{v}=g_{m}R_{p}\geq 4.$

If the two capacitors are replaced by inductors, and magnetic coupling is ignored, the circuit becomes a Hartley oscillator. In that case, the input impedance is the sum of the two inductors and a negative resistance given by

$R_{\text{in}}=-g_{m}\omega ^{2}L_{1}L_{2}.$

In the Hartley circuit, oscillation is more likely for larger values of transconductance and larger values of inductance.

The above analysis also describes the behavior of the Pierce oscillator. The Pierce oscillator, with two capacitors and one inductor, is equivalent to the Colpitts oscillator. Equivalence can be shown by choosing the junction of the two capacitors as the ground point. An electrical dual of the standard Pierce oscillator using two inductors and one capacitor is equivalent to the Hartley oscillator.

### Working principle

A Colpitts oscillator is an electronic circuit that generates a sinusoidal waveform, typically in the radio frequency range. It uses an inductor and two capacitors in parallel to form a resonant tank circuit, which determines the oscillation frequency. The output signal from the tank circuit is fed back into the input of an amplifier, where it is amplified and fed back into the tank circuit. The feedback signal provides the necessary phase shift for sustained oscillation.

The working principle of a Colpitts oscillator can be explained as follows:

- When the power supply is switched on, the capacitors $C_{1}$ and $C_{2}$ start charging through the resistor $R_{1}$ and $R_{2}$ . The voltage across $C_{2}$ is coupled to the base of the transistor through the capacitor $C_{\text{in}}$ .
- The transistor amplifies the input signal and produces an inverted output signal at the collector. The output signal is coupled to the tank circuit through the capacitor $C_{\text{out}}$ .
- The tank circuit resonates at its natural frequency, which is given by $f={\frac {1}{2\pi {\sqrt {LC_{t}}}}},$ where *f* is the frequency of oscillation, *L* is the inductance of the inductor, $C_{t}$ is the total capacitance of the series combination of $C_{1}$ and $C_{2}$ , given by $C_{t}={\frac {C_{1}C_{2}}{C_{1}+C_{2}}}.$
- The resonant frequency is independent of the values of $C_{1}$ and $C_{2}$ , but depends on their ratio. The ratio of $C_{1}$ and $C_{2}$ also affects the feedback gain and the stability of the oscillator.
- The voltage across the inductor *L* is in phase with the voltage across $C_{2}$ , and 180° out of phase with the voltage across $C_{1}$ . Therefore, the voltage at the junction of $C_{1}$ and $C_{2}$ is 180° out of phase with the voltage at the collector of the transistor. This voltage is fed back to the base of the transistor through $C_{\text{in}}$ , providing another 180° phase shift. Thus, the total phase shift around the loop is 360°, which is equivalent to no phase shift. This satisfies the Barkhausen criterion for oscillation.
- The amplitude of the oscillation depends on the feedback gain and the losses in the tank circuit. The feedback gain should be equal to or slightly greater than the losses for sustained oscillation. The feedback gain can be adjusted by varying the values of $R_{1}$ and $R_{2}$ , or by using a variable capacitor in place of $C_{1}$ or $C_{2}$ .

The Colpitts oscillator is widely used in various applications, such as RF communication systems, signal generators, and electronic testing equipment. It has better frequency stability than the Hartley oscillator, which uses a tapped inductor instead of a tapped capacitor in the tank circuit. However, the Colpitts oscillator may require a higher supply voltage and a larger coupling capacitor than the Hartley oscillator.

### Oscillation amplitude

The amplitude of oscillation is generally difficult to predict, but it can often be accurately estimated using the describing function method.

For the common-base oscillator in Figure 1, this approach applied to a simplified model predicts an output (collector) voltage amplitude given by

$V_{C}=2I_{C}R_{L}{\frac {C_{1}}{C_{1}+C_{2}}},$

where $I_{C}$ is the bias current, and $R_{L}$ is the load resistance at the collector.

This assumes that the transistor does not saturate, the collector current flows in narrow pulses, and that the output voltage is sinusoidal (low distortion).

This approximate result also applies to oscillators employing different active device, such as MOSFETs and vacuum tubes.
