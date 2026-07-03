---
title: "All-pass filter"
source: https://en.wikipedia.org/wiki/All-pass_filter
domain: low-pass-filter
license: CC-BY-SA-4.0
tags: low-pass filter
fetched: 2026-07-03
---

# All-pass filter

An **all-pass filter** is a signal processing filter that passes all frequencies equally in gain, but changes the phase relationship among various frequencies. Most types of filter reduce the amplitude (i.e. the magnitude) of the signal applied to it for some values of frequency, whereas the all-pass filter allows all frequencies through without changes in level.

## Common applications

A common application in electronic music production is in the design of an effects unit known as a "phaser", where a number of all-pass filters are connected in sequence and the output mixed with the raw signal.

It does this by varying its phase shift as a function of frequency. Generally, the filter is described by the frequency at which the phase shift crosses 90° (i.e., when the input and output signals go into quadrature – when there is a quarter wavelength of delay between them).

They are generally used to compensate for other undesired phase shifts that arise in the system, or for mixing with an unshifted version of the original to implement a notch comb filter.

They may also be used to convert a mixed phase filter into a minimum phase filter with an equivalent magnitude response or an unstable filter into a stable filter with an equivalent magnitude response.

## Active analog implementation

### Implementation using low-pass filter

The operational amplifier circuit shown in adjacent figure implements a single-pole active all-pass filter that features a low-pass filter at the non-inverting input of the opamp. The filter's transfer function is given by:

$H(s)=-{\frac {s-{\frac {1}{RC}}}{s+{\frac {1}{RC}}}}={\frac {1-sRC}{1+sRC}},\,$

which has one pole at -1/RC and one zero at 1/RC (i.e., they are *reflections* of each other across the imaginary axis of the complex plane). The magnitude and phase of H(iω) for some angular frequency ω are

$|H(i\omega )|=1\quad {\text{and}}\quad \angle H(i\omega )=-2\arctan(\omega RC).\,$

The filter has unity-gain magnitude for all ω. The filter introduces a different delay at each frequency and reaches input-to-output *quadrature* at ω=1/RC (i.e., phase shift is 90°).

This implementation uses a low-pass filter at the non-inverting input to generate the phase shift and negative feedback.

- At high frequencies, the capacitor is a short circuit, creating an inverting amplifier (i.e., 180° phase shift) with unity gain.
- At low frequencies and DC, the capacitor is an open circuit, creating a unity-gain voltage buffer (i.e., no phase shift).
- At the corner frequency ω=1/RC of the low-pass filter (i.e., when input frequency is 1/(2πRC)), the circuit introduces a 90° shift (i.e., output is in quadrature with input; the output appears to be delayed by a quarter period from the input).

In fact, the phase shift of the all-pass filter is double the phase shift of the low-pass filter at its non-inverting input.

#### Interpretation as a Padé approximation to a pure delay

The Laplace transform of a pure delay is given by

$e^{-sT},$

where T is the delay (in seconds) and $s\in \mathbb {C}$ is complex frequency. This can be approximated using a Padé approximant, as follows:

$e^{-sT}={\frac {e^{-sT/2}}{e^{sT/2}}}\approx {\frac {1-sT/2}{1+sT/2}},$

where the last step was achieved via a first-order Taylor series expansion of the numerator and denominator. By setting $RC=T/2$ we recover $H(s)$ from above.

### Implementation using high-pass filter

The operational amplifier circuit shown in the adjacent figure implements a single-pole active all-pass filter that features a high-pass filter at the non-inverting input of the opamp. The filter's transfer function is given by:

$H(s)={\frac {s-{\frac {1}{RC}}}{s+{\frac {1}{RC}}}},\,$

which has one pole at -1/RC and one zero at 1/RC (i.e., they are *reflections* of each other across the imaginary axis of the complex plane). The magnitude and phase of H(iω) for some angular frequency ω are

$|H(i\omega )|=1\quad {\text{and}}\quad \angle H(i\omega )=\pi -2\arctan(\omega RC).\,$

The filter has unity-gain magnitude for all ω. The filter introduces a different delay at each frequency and reaches input-to-output *quadrature* at ω=1/RC (i.e., phase lead is 90°).

This implementation uses a high-pass filter at the non-inverting input to generate the phase shift and negative feedback.

- At high frequencies, the capacitor is a short circuit, thereby creating a unity-gain voltage buffer (i.e., no phase lead).
- At low frequencies and DC, the capacitor is an open circuit and the circuit is an inverting amplifier (i.e., 180° phase lead) with unity gain.
- At the corner frequency ω=1/RC of the high-pass filter (i.e., when input frequency is 1/(2πRC)), the circuit introduces a 90° phase lead (i.e., output is in quadrature with input; the output appears to be advanced by a quarter period from the input).

In fact, the phase shift of the all-pass filter is double the phase shift of the high-pass filter at its non-inverting input.

### Voltage controlled implementation

The resistor can be replaced with a FET in its *ohmic mode* to implement a voltage-controlled phase shifter; the voltage on the gate adjusts the phase shift. In electronic music, a phaser typically consists of two, four or six of these phase-shifting sections connected in tandem and summed with the original. A low-frequency oscillator (LFO) ramps the control voltage to produce the characteristic swooshing sound.

## Passive analog implementation

The benefit to implementing all-pass filters with active components like operational amplifiers is that they do not require inductors, which are bulky and costly in integrated circuit designs. In other applications where inductors are readily available, all-pass filters can be implemented entirely without active components. There are a number of circuit topologies that can be used for this. The following are the most commonly used circuits.

### Lattice filter

The **lattice phase equaliser**, or **filter**, is a filter composed of lattice, or X-sections. With single element branches it can produce a phase shift up to 180°, and with resonant branches it can produce phase shifts up to 360°. The filter is an example of a constant-resistance network (i.e., its image impedance is constant over all frequencies).

### T-section filter

The phase equaliser based on T topology is the unbalanced equivalent of the lattice filter and has the same phase response. While the circuit diagram may look like a low pass filter it is different in that the two inductor branches are mutually coupled. This results in transformer action between the two inductors and an all-pass response even at high frequency.

### Bridged T-section filter

The bridged T topology is used for delay equalisation, particularly the differential delay between two landlines being used for stereophonic sound broadcasts. This application requires that the filter has a linear phase response with frequency (i.e., constant group delay) over a wide bandwidth and is the reason for choosing this topology.

## Digital implementation

A Z-transform implementation of an all-pass filter with a complex pole at $z_{0}$ is

$H(z)={\frac {z^{-1}-{\overline {z_{0}}}}{1-z_{0}z^{-1}}}\$

which has a zero at $1/{\overline {z_{0}}}$ , where ${\overline {z}}$ denotes the complex conjugate. The pole and zero sit at the same angle but have reciprocal magnitudes (i.e., they are *reflections* of each other across the boundary of the complex unit circle). The placement of this pole-zero pair for a given $z_{0}$ can be rotated in the complex plane by any angle and retain its all-pass magnitude characteristic. Complex pole-zero pairs in all-pass filters help control the frequency where phase shifts occur.

To create an all-pass implementation with real coefficients, the complex all-pass filter can be cascaded with an all-pass that substitutes ${\overline {z_{0}}}$ for $z_{0}$ , leading to the Z-transform implementation

$H(z)={\frac {z^{-1}-{\overline {z_{0}}}}{1-z_{0}z^{-1}}}\times {\frac {z^{-1}-z_{0}}{1-{\overline {z_{0}}}z^{-1}}}={\frac {z^{-2}-2\Re (z_{0})z^{-1}+\left|{z_{0}}\right|^{2}}{1-2\Re (z_{0})z^{-1}+\left|z_{0}\right|^{2}z^{-2}}},\$

which is equivalent to the difference equation

$y[k]-2\Re (z_{0})y[k-1]+\left|z_{0}\right|^{2}y[k-2]=x[k-2]-2\Re (z_{0})x[k-1]+\left|z_{0}\right|^{2}x[k],\,$

where $y[k]$ is the output and $x[k]$ is the input at discrete time step k .

Filters such as the above can be cascaded with unstable or mixed-phase filters to create a stable or minimum-phase filter without changing the magnitude response of the system. For example, by proper choice of $z_{0}$ , a pole of an unstable system that is outside of the unit circle can be canceled and reflected inside the unit circle.
