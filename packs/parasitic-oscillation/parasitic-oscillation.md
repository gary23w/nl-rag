---
title: "Parasitic oscillation"
source: https://en.wikipedia.org/wiki/Parasitic_oscillation
domain: parasitic-oscillation
license: CC-BY-SA-4.0
tags: parasitic oscillation
fetched: 2026-07-03
---

# Parasitic oscillation

**Parasitic oscillation** is an unintended self-sustaining oscillation in an electronic circuit, typically caused by unintentional feedback combined with sufficient gain and phase shift in an amplifying device. It occurs most commonly in RF and audio amplifiers, but can arise in many types of analog electronic circuits. It is one of the fundamental issues addressed by control theory.

Parasitic oscillation is undesirable for several reasons. The oscillations may be coupled into other circuits or radiate as radio waves, causing electromagnetic interference (EMI) to other devices. In audio systems, parasitic oscillations can sometimes be heard as annoying sounds in the speakers or earphones. The oscillations waste power and may cause undesirable heating. For example, an audio power amplifier that goes into parasitic oscillation may generate enough power to damage connected speakers. A circuit that is oscillating will not amplify linearly, so desired signals passing through the stage will be distorted. In digital circuits, parasitic oscillations may only occur on particular logic transitions and may result in erratic operation of subsequent stages; for example, a counter stage may see many spurious pulses and count erratically.

## Causes

Parasitic oscillation in an amplifier stage occurs when part of the output energy is coupled into the input, with the correct phase and amplitude to provide positive feedback at some frequency. The coupling can occur directly between input and output wiring with stray capacitance or mutual inductance between input and output. In some solid-state or vacuum electron devices there is sufficient internal capacitance to provide a feedback path. Since the ground is common to both input and output, output current flowing through the impedance of the ground connection can also couple signals back to the input.

Similarly, impedance in the power supply can couple input to output and cause oscillation. When a common power supply is used for several stages of amplification, the supply voltage may vary with the changing current in the output stage. The power supply voltage changes will appear in the input stage as positive feedback. An example is a transistor radio which plays well with a fresh battery, but squeals or "motorboats" when the battery is old.

In audio systems, if a microphone is placed close to a loudspeaker, parasitic oscillations may occur. This is caused by positive feedback, from amplifier's output to loudspeaker to sound waves, and back via the microphone to the amplifier input. See Audio feedback.

## Conditions

Feedback control theory was developed to address the problem of parasitic oscillation in servo control systems – the systems oscillated rather than performing their intended function, for example velocity control in engines. The Barkhausen stability criterion gives the necessary condition for oscillation; the loop gain around the feedback loop, which is equal to the amplifier gain multiplied by the transfer function of the inadvertent feedback path, must be equal to one, and the phase shift around the loop must be zero or a multiple of 360° (2π radians).

In practice, feedback may occur over a range of frequencies (for example the operating range of an amplifier); at various frequencies, the phase of the amplifier may be different. If there is one frequency where the feedback is positive and the amplitude condition is also fulfilled – the system will oscillate at that frequency.

These conditions can be expressed in mathematical terms using the Nyquist plot. Another method used in control loop theory uses Bode plots of gain and phase vs. frequency. Using Bode plots, a design engineer checks whether there is a frequency where both conditions for oscillations are met: the phase is zero (positive feedback) and the loop gain is 1 or greater.

When parasitic oscillations occur, the designer can use the various tools of control loop engineering to correct the situation – to reduce the gain or to change the phase at problematic frequencies.

## Mitigation

Several measures are used to prevent parasitic oscillation. Amplifier circuits are laid out so that input and output wiring are not adjacent, preventing capacitive or inductive coupling. A metal shield may be placed over sensitive portions of the circuit. Bypass capacitors may be put at power supply connections, to provide a low-impedance path for AC signals and prevent interstage coupling through the power supply. Where printed circuit boards are used, high- and low-power stages are separated and ground return traces are arranged so that heavy currents don't flow in mutually shared portions of the ground trace. In some cases the problem may only be solved by introduction of another feedback *neutralization* network, calculated and adjusted to eliminate the negative feedback within the passband of the amplifying device. A classic example is the Neutrodyne circuit used in tuned radio frequency receivers.
