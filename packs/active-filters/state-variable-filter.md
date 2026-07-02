---
title: "State variable filter"
source: https://en.wikipedia.org/wiki/State_variable_filter
domain: active-filters
license: CC-BY-SA-4.0
tags: active filter, Sallen-Key topology, state variable filter, gyrator circuit
fetched: 2026-07-02
---

# State variable filter

A **state variable filter** (SVF) is a type of active filter in electronic circuits. In a state-variable filter architecture the signal and its successive derivatives are treated as the core state variables of the system.

In state variable filters parameters like gain, cutoff frequency and Q can be independently controlled. This makes it, for example, possible to build a tunable filter where the cutoff frequency is adjustable, while the gain and Q remain constant. A state variable filter consists of one or more integrators, connected in some feedback configuration. It is essentially used when a precise Q factor is required, as other multi-order filters are unable to provide. The most common implementation sums the input signal with its integral and its double integral.

State variable filters can also be classified as Multiple Feedback (MFB) and Multi Feedback Loop (MFL) Filters because of the typical feedback configurations. The multiple feedback architecture contributes to the reduced sensitivity to component values of state variable filters.

## Kerwin–Huelsman–Newcomb (KHN) biquad filter example

In their paper Kerwin, Huelsman and Newcomb derive a filter architecture and provide a realisation with Operational Amplifiers, using state-variable synthesis. Filters of this kind, especially the version with three Operational Amplifers are known as KHN filters, or simply as state variable filters.

The example given below can produce simultaneous lowpass, highpass, and bandpass outputs from a single input. This is a second-order (biquad, short for biquadratic) filter. Its derivation comes from rearranging a high-pass filter's transfer function, which is the ratio of two quadratic functions. The rearrangement reveals that one signal is the sum of integrated copies of another. That is, the rearrangement reveals a state-variable-filter structure. By using different states as outputs, different kinds of filters can be produced. In more general state-variable-filter examples, additional filter orders are possible with more integrators (i.e., more states).

With an additional OpAmp (not shown) in summer configuration a bandstop output can be added by summing the lowpass and highpass output. Further, an all-pass filter can be build, again with an OpAmp, by subtracting the bandpass output from the filter input.

The signal input is marked Vin; the LP, HP and BP outputs give the lowpass, highpass, and bandpass filtered signals respectively.

For simplicity, we set:

$R_{f1}=R_{f2}$

$C_{1}=C_{2}$

$R_{1}=R_{2}$

Then:

$F_{0}={\frac {1}{2\pi R_{f1}C_{1}}}$

$Q=\left(1+{\frac {R_{4}}{R_{q}}}\right)\left({\frac {1}{2+{\frac {R_{1}}{R_{g}}}}}\right)$

The pass-band gain for the LP and HP outputs is given by:

$A_{HP}=A_{LP}={\frac {R_{1}}{R_{g}}}$

It can be seen that the frequency of operation and the Q factor can be varied independently. This and the ability to switch between different filter responses make the state-variable filter widely used in analogue synthesizers.

Values for a resonance frequency of 1 kHz are Rf1 = Rf2 = 10k, C1 = C2 = 15nF and R1 = R2 = 10k.

## Tow-Thomas filter

Tow and Thomas independently published what is today known as the Tow-Thomas filter. Other names are the Ring-of-Three Filter and the two-integrator loop. Sometimes it is just called the biquad filter.

The filter can be considered as a rearrangement of the KHN filter and is also a biquad filter. One aspect of the Tow-Thomas filter, compared to the KHN filter, is that all non-inverting OpAmp inputs are grounded. This removes the effect of parasitic capacitances at all of these inputs. Cf the first OpAmp of a KHN filter.

## Åckerberg-Mossberg filter

A variant of the Tow-Thomas filter, and therefore the KHN filter, is the Åckerberg-Mossberg filter.

## Use of Multiplying Digital-to-analog converters or similar components

By replacing resistors in a state variable filter with multiplying DACs (MDACs) it is possible to build state variable filters where the parameters gain, cutoff frequency and Q can be independently digitally controlled.

It is also possible to use components like a voltage-controle amplifier (VCA) to build a digitally controlled state variable filter. Further, switched capacitors can be used to replace resistors in a state variable filter (see Switched capacitor#Filters). The MF10 IC and pin compatible ICs like the LMF100 and LTC1060 are examples of using a state variable filter architecture with switched capacitors.

## Other orders than second-order State Variable Filters

The typical state variable filter is a second-order filter. It is possible to conceptualize and build lower (first order) and higher-order state variable filters by removing or adding additional integrator stages (1/s stages) and corresponding feedback loops.

### Higher-order State Variable Filters

While it is possible to build higher-order state variable filters it is instead common in active filter design to assemble higher-order filters by cascading first and second order filters, because Q-factor and frequency become difficult to control in higher-order filters

If an uneven order is desired a first order filter is needed as part of the filter cascade. This can either be a first-order state variable filter or more typically some other kind of filter.

### First-order State Variable Filters

A first-order state variable filters can be build, although they are not widely used. They contain one integrator stage and typically provide highpass and lowpass output, but no bandpass.(Mode 6a and 6b)

## Applications

State variable filters are frequently used for modifying frequency response in audio signal processing. At low Q settings they are often used in parametric equaliser circuits, and at high or variable Q settings to create resonant filter modules in analog synthesizers. For manual control of frequency, Rf1 and Rf2 in the section above may be replaced by a dual potentiometer; and for voltage control, the devices U2 and U3 may be replaced by voltage controlled amplifiers or operational transconductance amplifiers.
