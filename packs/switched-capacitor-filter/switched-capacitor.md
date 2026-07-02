---
title: "Switched capacitor"
source: https://en.wikipedia.org/wiki/Switched_capacitor
domain: switched-capacitor-filter
license: CC-BY-SA-4.0
tags: switched capacitor, correlated double sampling, charge redistribution, switched-capacitor filter
fetched: 2026-07-02
---

# Switched capacitor

A **switched capacitor** (**SC**) is an electronic circuit that implements a function by moving charges into and out of capacitors when electronic switches are opened and closed. Usually, non-overlapping clock signals are used to control the switches, so that not all switches are closed simultaneously. Filters implemented with these elements are termed *switched-capacitor filters*, which depend only on the ratios between capacitances and the switching frequency, and not on precise resistors. This makes them much more suitable for use within integrated circuits, where accurately specified resistors and capacitors are not economical to construct, but accurate clocks and accurate *relative ratios* of capacitances are economical.

SC circuits are typically implemented using metal–oxide–semiconductor (MOS) technology, with MOS capacitors and MOS field-effect transistor (MOSFET) switches, and they are commonly fabricated using the complementary MOS (CMOS) process. Common applications of MOS SC circuits include mixed-signal integrated circuits, digital-to-analog converter (DAC) chips, analog-to-digital converter (ADC) chips, pulse-code modulation (PCM) codec-filters, and PCM digital telephony.

## Parallel resistor simulation using a switched-capacitor

The simplest switched-capacitor (SC) circuit is made of one capacitor $C_{S}$ and two switches **S1** and **S2** which alternatively connect the capacitor to either **in** or **out** at a switching frequency of f .

Recall that Ohm's law can express the relationship between voltage, current, and resistance as:

$R={V \over I}.\$

The following equivalent resistance calculation will show how during each switching cycle, this switched-capacitor circuit transfers an amount of charge from **in** to **out** such that it behaves according to a similar linear current–voltage relationship with $R_{\text{equivalent}}=1/(C_{S}f).$

### Equivalent resistance calculation

By definition, the charge q on any capacitor C with a voltage V between its plates is:

$q=CV.\$

Therefore, when **S1** is closed while **S2** is open, the charge stored in the capacitor $C_{S}$ will be:

$q_{\text{in}}=C_{S}V_{\text{in}}$

assuming $V_{\text{in}}$ is an ideal voltage source.

When **S2** is closed (**S1** is open - they are never both closed at the same time), some of that charge is transferred out of the capacitor. Exactly how much charge gets transferred can't be determined without knowing what load is attached to the output. However, by definition, the charge remaining on capacitor $C_{S}$ can be expressed in terms of the unknown variable $V_{\text{out}}$ :

$q_{\text{out}}=C_{S}V_{\text{out}}.\$

Thus, the charge transferred from **in** to **out** during one switching cycle is:

$q_{\text{in-out}}=q_{\text{in}}-q_{\text{out}}=C_{S}(V_{\text{in}}-V_{\text{out}}).\$

This charge is transferred at a rate of f . So the average electric current (rate of transfer of charge per unit time) from **in** to **out** is:

$I_{\text{in-out}}=q_{\text{in-out}}f=C_{S}(V_{\text{in}}-V_{\text{out}})f.\$

The voltage difference from **in** to **out** can be written as:

$V_{\text{in-out}}=V_{\text{in}}-V_{\text{out}}.\$

Finally, the current–voltage relationship from **in** to **out** can be expressed with the same form as Ohm's law, to show that this switched-capacitor circuit simulates a resistor with an equivalent resistance of:

$R_{\text{equivalent}}={V_{\text{in-out}} \over I_{\text{in-out}}}={(V_{\text{in}}-V_{\text{out}}) \over C_{S}(V_{\text{in}}-V_{\text{out}})f}={1 \over {C_{S}f}}.\$

This circuit is called a *parallel resistor simulation* because **in** and **out** are connected in parallel and not directly coupled. Other types of SC simulated resistor circuits are *bilinear resistor simulation*, *series resistor simulation*, *series-parallel resistor simulation*, and *parasitic-insensitive resistor simulation*.

### Difference with real resistor

Charge is transferred from **in** to **out** as discrete pulses, not continuously. This transfer approximates the equivalent continuous transfer of charge of a resistor when the switching frequency is sufficiently higher (≥100x) than the bandlimit of the input signal.

The SC circuit modeled here using ideal switches with zero resistance does not suffer from the ohmic heating energy loss of a regular resistor, and so ideally could be called a loss free resistor. However real switches have some small resistance in their channel or p–n junctions, so power is still dissipated. The capacitors are not ideal either and dissipate power as well.

Because the resistance inside electric switches is typically much smaller than the resistances in circuits relying on regular resistors, SC circuits can have substantially lower Johnson–Nyquist noise. However, harmonics of the switching frequency may be manifested as high frequency noise that may need to be attenuated with a low-pass filter.

SC simulated resistors also have the benefit that their equivalent resistance can be adjusted by changing the switching frequency (i.e., it is a programmable resistance) with a resolution limited by the resolution of the switching period. Thus *online* or *runtime* adjustment can be done by controlling the oscillation of the switches (e.g. using an configurable clock output signal from a microcontroller).

### Applications

SC simulated resistors are used as a replacement for real resistors in integrated circuits because it is easier to fabricate reliably with a wide range of values and can take up much less silicon area.

This same circuit can be used in discrete time systems (such as ADCs) as a sample and hold circuit. During the appropriate clock phase, the capacitor samples the analog voltage through switch **S1** and in the second phase presents this held sampled value through switch **S2** to an electronic circuit for processing.

#### Filters

Electronic filters consisting of resistors and capacitors can have their resistors replaced with equivalent switched-capacitor simulated resistors, allowing the filter to be manufactured using only switches and capacitors without relying on real resistors.

## The parasitic-sensitive integrator

Switched-capacitor simulated resistors can replace the input resistor in an op amp integrator to provide accurate voltage gain and integration.

One of the earliest of these circuits is the parasitic-sensitive integrator developed by the Czech engineer Bedrich Hosticka.

### Analysis

Denote by $T=1/f$ the switching period. In capacitors,

${\text{charge}}={\text{capacitance}}\times {\text{voltage}}$

Then, when **S1** opens and **S2** closes (they are never both closed at the same time), we have the following:

1) Because $C_{s}$ has just charged:

$Q_{s}(t)=C_{s}\cdot V_{s}(t)\,$

2) Because the feedback cap, $C_{fb}$ , is suddenly charged with that much charge (by the op amp, which seeks a virtual short circuit between its inputs):

$Q_{fb}(t)=Q_{s}(t-T)+Q_{fb}(t-T)\,$

Now dividing 2) by $C_{fb}$ :

$V_{fb}(t)={\frac {Q_{s}(t-T)}{C_{fb}}}+V_{fb}(t-T)\,$

And inserting 1):

$V_{fb}(t)={\frac {C_{s}}{C_{fb}}}\cdot V_{s}(t-T)+V_{fb}(t-T)\,$

This last equation represents what is going on in $C_{fb}$ - it increases (or decreases) its voltage each cycle according to the charge that is being "pumped" from $C_{s}$ (due to the op-amp).

However, there is a more elegant way to formulate this fact if T is very short. Let us introduce $dt\leftarrow T$ and $dV_{fb}\leftarrow V_{fb}(t)-V_{fb}(t-dt)$ and rewrite the last equation divided by dt:

${\frac {dV_{fb}(t)}{dt}}=f{\frac {C_{s}}{C_{fb}}}\cdot V_{s}(t)\,$

Therefore, the op-amp output voltage takes the form:

$V_{\text{out}}(t)=-V_{fb}(t)=-{\frac {1}{{\frac {1}{fC_{s}}}C_{fb}}}\int V_{s}(t)dt\,$

This is the same formula as the op amp inverting integrator where the resistance is replaced by a SC simulated resistor with an equivalent resistance of:

$R_{\text{equivalent}}={1 \over {C_{s}f}}.\$

This switched-capacitor circuit is called "parasitic-sensitive" because its behavior is significantly affected by parasitic capacitances, which will cause errors when parasitic capacitances can't be controlled. "Parasitic insensitive" circuits try to overcome this.

## The parasitic insensitive integrator

### Use in discrete-time systems

The delaying parasitic insensitive integrator has a wide use in discrete time electronic circuits such as biquad filters, anti-alias structures, and delta-sigma data converters. This circuit implements the following z-domain function:

$H(z)={\frac {1}{z-1}}$

## The multiplying digital to analog converter

One useful characteristic of switched-capacitor circuits is that they can be used to perform many circuit tasks at the same time, which is difficult with non-discrete time components (i.e. analog electronics). The multiplying digital to analog converter (MDAC) is an example as it can take an analog input, add a digital value d to it, and multiply this by some factor based on the capacitor ratios. The output of the MDAC is given by the following:

$V_{Out}={\frac {V_{i}\cdot (C_{1}+C_{2})-(d-1)\cdot V_{r}\cdot C_{2}+V_{os}\cdot (C_{1}+C_{2}+C_{p})}{C_{1}+{\frac {(C_{1}+C_{2}+C_{p})}{A}}}}$

The MDAC is a common component in modern pipeline analog to digital converters as well as other precision analog electronics and was first created in the form above by Stephen Lewis and others at Bell Laboratories.

## Analysis of switched-capacitor circuits

Switched-capacitor circuits are analysed by writing down charge conservation equations, as in this article, and solving them with a computer algebra tool. For hand analysis and for getting more insight into the circuits, it is also possible to do a Signal-flow graph analysis, with a method that is very similar for switched-capacitor and continuous-time circuits.
