---
title: "Brokaw bandgap reference"
source: https://en.wikipedia.org/wiki/Brokaw_bandgap_reference
domain: bandgap-reference
license: CC-BY-SA-4.0
tags: bandgap voltage reference, Brokaw bandgap reference, Widlar current mirror, temperature compensation
fetched: 2026-07-02
---

# Brokaw bandgap reference

The **Brokaw bandgap reference** is a voltage reference circuit widely used in integrated circuits, with an output voltage around 1.25 V that exhibits low temperature dependence. This particular circuit is one type of a bandgap voltage reference, named after Paul Brokaw, the author of its first publication.

Like all temperature-independent bandgap references, the circuit maintains an internal voltage source that has a positive temperature coefficient and another internal voltage source that has a negative temperature coefficient. By summing the two together, the temperature dependence can be canceled. Additionally, either of the two internal sources can be used as a temperature sensor.

In the Brokaw bandgap reference, the circuit uses negative feedback (by means of an operational amplifier) to force a constant current through two bipolar transistors with different emitter areas. By the Ebers–Moll model of a transistor,

- The transistor with the larger emitter area requires a smaller base–emitter voltage for the same current.
- The *difference* between the two base–emitter voltages has a positive temperature coefficient (i.e., it increases with temperature).
- The base–emitter voltage for each transistor has a negative temperature coefficient (i.e., it decreases with temperature).

The circuit output is the sum of one of the base–emitter voltages with a multiple of the base–emitter voltage differences. With appropriate component choices, the two opposing temperature coefficients will cancel each other exactly and the output will have no temperature dependence.

In the example circuit shown, the opamp ensures that its inverting and non-inverting inputs are at the same voltage. This means that the currents in each collector resistor are identical, so the collector currents of Q1 and Q2 are also identical. If Q2 has an emitter area that is N times larger than Q1, its base-emitter voltage will be lower than that of Q1 by a magnitude of ${\tfrac {kT}{q}}\ln(N)$ . This voltage is generated across $R2$ and so defines the current I in each leg as ${\tfrac {kT}{q}}\ln(N){\tfrac {1}{R2}}$ . The output voltage (at the opamp output) is therefore $V_{BE_{Q1}}+2\cdot I\cdot R1$ , or:

$V_{BE_{Q1}}+2{\tfrac {kT}{q}}\ln(N){\tfrac {R1}{R2}}\,.$

The first term has a negative temperature coefficient; the second term has a positive temperature coefficient (from its T ). By an appropriate choice of N and $R1$ and $R2$ , these temperature coefficients can be made to cancel, giving an output voltage that is nearly independent of temperature. The magnitude of this output voltage can be shown to be approximately equal to the bandgap voltage (EG0) of Silicon extrapolated to 0 K.
