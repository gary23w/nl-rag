---
title: "Pierce oscillator"
source: https://en.wikipedia.org/wiki/Pierce_oscillator
domain: crystal-oscillators-deep
license: CC-BY-SA-4.0
tags: crystal oscillator, colpitts oscillator, pierce oscillator, quartz clock
fetched: 2026-07-02
---

# Pierce oscillator

The **Pierce oscillator** is a type of electronic oscillator particularly well-suited for use in piezoelectric crystal oscillator circuits. Named for its inventor, George W. Pierce (1872–1956), the Pierce oscillator is a derivative of the Colpitts oscillator. Virtually all digital IC clock oscillators are of Pierce type, as the circuit can be implemented using a minimum of components: a single digital inverter, one resistor, two capacitors, and the quartz crystal, which acts as a highly selective filter element. The low manufacturing cost of this circuit and the frequency stability of quartz crystals make it advantageous for many consumer electronics applications.

## Operation

If the circuit consists of perfect lossless components, the signal on C1 and C2 will be proportional to the impedance of each, and the ratio of the signal voltages at C1 and C2 will be C2/C1. With C1 and C2 equal size (a common configuration), the current in C1 to C2 would be exactly equal, but out of phase, requiring no current from the amplifier or voltage gain from the amplifier, and allowing a high output impedance amplifier, or the use of an isolating series resistance in the amplifier output. Normal crystals are lossless enough to make this a reasonable approximation: the amplifier does not drive the resonant circuit, but merely stays in sync with it, providing enough power to match losses.

A series resistor is occasionally shown in the amplifier output. When used, a series resistor reduces loop gain, and amplifier gain must be increased to restore total loop gain to unity. The purpose of using such a resistor in the amplifier circuit is to increase phase shift at startup, or when the crystal circuit is pulled out of phase by loading, and to eliminate the effects of amplifier non-linearity and of crystal overtones or spurious modes. It is not part of the basic operation of the Pierce topology.

### Biasing resistor

*R*1 acts as a feedback resistor, biasing the inverter in its linear region of operation and effectively causing it to function as a high-gain inverting amplifier. To better understand this, assume the inverter is ideal, with infinite input impedance and zero output impedance. The resistor forces the input and output voltages to be equal. Hence the inverter will neither be fully on, nor fully off, but will operate in the transition region, where it has gain.

### Resonator

Extremely low-cost applications sometimes use a piezoelectric PZT crystal ceramic resonator rather than a piezoelectric quartz crystal resonator.

The crystal in combination with *C*1 and *C*2 forms a pi network band-pass filter, which provides a 180° phase shift and a voltage gain from the output to input at approximately the resonant frequency of the crystal. To understand the operation, note that at the frequency of oscillation, the crystal appears inductive. Thus, the crystal can be considered a large, high-*Q* inductor. The combination of the 180° phase shift (i.e. inverting gain) from the pi network, and the negative gain from the inverter, results in a positive loop gain (positive feedback), making the bias point set by *R*1 unstable and leading to oscillation.

Recently, MEMS (Micro-Electro-Mechanical-System) resonators fabricated by surface micromachining have enabled ultra-low power stable pierce oscillators. The tiny form factor of MEMS resonators greatly reduced the power consumption of the oscillator while keeping the good stability thanks to their very-high Q.

### Isolation resistor

In addition to the biasing resistor *R*1, Ruan Lourens strongly recommends a series resistor *R*s between the output of the inverter and the crystal. The series resistor *R*s reduces the chance of overtone oscillation and can improve start-up time. This second resistor *R*s isolates the inverter from the crystal network. This would also add additional phase shift to *C*1. Pierce oscillators above 4 MHz should use a small capacitor rather than a resistor for *R*s. This biasing resistor is commonly implemented by a MOSFET biased in its linear region to minimize parasitics.

## Load capacitance

The total capacitance seen from the crystal looking into the rest of the circuit is called the "load capacitance". When a manufacturer makes a "parallel" crystal, a technician uses a Pierce oscillator with a particular fixed load capacitance (often 18 or 20 pF) while trimming the crystal to oscillate at exactly the frequency written on its package.

To assure operation at the correct frequency, one must make sure the capacitances in the circuit match this value specified on the crystal's data sheet. Load capacitance *C*L can be calculated from the series combination of *C*1 and *C*2, taking into account *C*i and *C*o, the input and output capacitance of the inverter, and *C*s, the stray capacitances from the oscillator, PCB layout, and crystal case (typically 3–9 pF):

$C_{\text{L}}={\frac {(C_{1}+C_{\text{i}})(C_{2}+C_{\text{o}})}{C_{1}+C_{\text{i}}+C_{2}+C_{\text{o}}}}+C_{\text{s}}.$

When a manufacturer makes a "series" crystal, a technician uses a different tuning procedure. When a "series" crystal is used in a Pierce oscillator, the Pierce oscillator (as always) drives the crystal at nearly its parallel resonance frequency. But that frequency is a few kilohertz higher than the series resonant frequency printed on the package of a "series" crystal. Increasing the "load capacitance" slightly decreases the frequency generated by a Pierce oscillator, but never enough to reduce it all the way down to the series resonant frequency.
