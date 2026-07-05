---
title: "Reflection coefficient"
source: https://en.wikipedia.org/wiki/Reflection_coefficient
domain: adiabatic-quantum-motor
license: CC-BY-SA-4.0
tags: adiabatic quantum motor
fetched: 2026-07-05
---

# Reflection coefficient

In physics and electrical engineering the **reflection coefficient** is a parameter that describes how much of a wave is reflected by an impedance discontinuity in the transmission medium. It is equal to the ratio of the amplitude of the reflected wave to the incident wave, with each expressed as phasors. For example, it is used in optics to calculate the amount of light that is reflected from a surface with a different index of refraction, such as a glass surface, or in an electrical transmission line to calculate how much of the electromagnetic wave is reflected by an impedance discontinuity. The reflection coefficient is closely related to the *transmission coefficient*. The reflectance of a system is also sometimes called a reflection coefficient.

Different disciplines have different applications for the term.

## Transmission lines

In telecommunications and transmission line theory, the reflection coefficient is the ratio of the complex amplitude of the reflected wave to that of the incident wave. The voltage and current at any point along a transmission line can always be resolved into forward and reflected traveling waves given a specified reference impedance *Z0*. The reference impedance used is typically the characteristic impedance of a transmission line that's involved, but one can speak of reflection coefficient without any actual transmission line being present. In terms of the forward and reflected waves determined by the voltage and current, the reflection coefficient is defined as the complex ratio of the voltage of the reflected wave ( $V^{-}$ ) to that of the incident wave ( $V^{+}$ ). This is typically represented with a $\Gamma$ (capital gamma) and can be written as:

$\Gamma ={\frac {V^{-}}{V^{+}}}$

It can also be defined using the *currents* associated with the reflected and forward waves, but introducing a minus sign to account for the opposite orientations of the two currents:

$\Gamma =-{\frac {I^{-}}{I^{+}}}={\frac {V^{-}}{V^{+}}}$

The reflection coefficient may also be established using other field or circuit pairs of quantities whose product defines power resolvable into a forward and reverse wave. With electromagnetic plane waves, one uses the ratio of the electric fields of the reflected to that of the incident wave (or magnetic fields, again with a minus sign); the ratio of each wave's electric field *E* to its magnetic field *H* is the medium's characteristic impedance, $Z_{0}$ , (equal to the impedance of free space if the medium is a vacuum).

In the accompanying figure, a signal source with internal impedance $Z_{S}$ possibly followed by a transmission line of characteristic impedance $Z_{S}$ is represented by its Thévenin equivalent, driving the load $Z_{L}$ . For a real (resistive) source impedance $Z_{S}$ , if we define $\Gamma$ using the reference impedance $Z_{0}=Z_{S}$ then the source's maximum power is delivered to a load $Z_{L}=Z_{0}$ , in which case $\Gamma =0$ implying no reflected power. More generally, the squared-magnitude of the reflection coefficient $|\Gamma |^{2}$ denotes the proportion of that power that is reflected back to the source, with the power actually delivered toward the load being $1-|\Gamma |^{2}$ .

Anywhere along an intervening (lossless) transmission line of characteristic impedance $Z_{0}$ , the magnitude of the reflection coefficient $|\Gamma |$ will remain the same (the powers of the forward and reflected waves stay the same) but with a different phase. In the case of a short circuited load ( $Z_{L}=0$ ), one finds $\Gamma =-1$ at the load. This implies the reflected wave having a 180° phase shift (phase reversal) with the voltages of the two waves being opposite at that point and adding to zero (as a short circuit demands).

### Relation to load impedance

The reflection coefficient is determined by the load impedance at the end of the transmission line, as well as the characteristic impedance of the line. A load impedance of $Z_{L}$ terminating a line with a characteristic impedance of $Z_{0}\,$ will have a reflection coefficient of

$\Gamma ={Z_{L}-Z_{0} \over Z_{L}+Z_{0}}.$

This is the coefficient at the load. The reflection coefficient can also be measured at other points on the line. The *magnitude* of the reflection coefficient in a lossless transmission line is constant along the line (as are the powers in the forward and reflected waves). However its *phase* will be shifted by an amount dependent on the electrical distance $\phi$ from the load. If the coefficient is measured at a point L meters from the load, so the electrical distance from the load is $\phi =2\pi L/\lambda$ radians, the coefficient $\Gamma '$ at that point will be

$\Gamma '=\Gamma e^{-i\,2\phi }$

Note that the phase of the reflection coefficient is changed by *twice* the phase length of the attached transmission line. That is to take into account not only the phase delay of the reflected wave, but the phase shift that had first been applied to the forward wave, with the reflection coefficient being the quotient of these. The reflection coefficient so measured, $\Gamma '$ , corresponds to an impedance which is generally dissimilar to $Z_{L}$ present at the far side of the transmission line.

The complex reflection coefficient (in the region $|\Gamma |\leq 1$ , corresponding to passive loads) may be displayed graphically using a Smith chart. The Smith chart is a polar plot of $\Gamma$ , therefore the magnitude of $\Gamma$ is given directly by the distance of a point to the center (with the edge of the Smith chart corresponding to $|\Gamma |=1$ ). Its evolution along a transmission line is likewise described by a rotation of $2\phi$ around the chart's center. Using the scales on a Smith chart, the resulting impedance (normalized to $Z_{0}$ ) can directly be read. Before the advent of modern electronic computers, the Smith chart was of particular use as a sort of analog computer for this purpose.

The reflected power in terms of the reflection coefficient is:

$P_{reflected}=P_{incident}|\Gamma |^{2}$

.

### Standing wave ratio

The standing wave ratio (SWR) is determined solely by the *magnitude* of the reflection coefficient:

$SWR={1+|\Gamma | \over 1-|\Gamma |}.$

Along a lossless transmission line of characteristic impedance *Z*0, the SWR signifies the ratio of the voltage (or current) maxima to minima (or what it would be if the transmission line were long enough to produce them). The above calculation assumes that $\Gamma$ has been calculated using *Z*0 as the reference impedance. Since it uses only the *magnitude* of $\Gamma$ , the SWR intentionally ignores the specific value of the load impedance *ZL* responsible for it, but only the magnitude of the resulting impedance mismatch. That SWR remains the same wherever measured along a transmission line (looking towards the load) since the addition of a transmission line length to a load $Z_{L}$ only changes the phase, not magnitude of $\Gamma$ . While having a one-to-one correspondence with reflection coefficient, SWR is the most commonly used figure of merit in describing the mismatch affecting a radio antenna or antenna system. It is most often measured at the transmitter side of a transmission line, but having, as explained, the same value as would be measured at the antenna (load) itself.

## Electrical networks

A transmission line is an example of a 2-port electrical network, but reflection coefficients are useful in the analysis of any electrical networks. A reflection coefficient for each port in the same way as for the boundary of a transmission line. It will, however, also depend on the properties of connections at other ports and so is not a property intrinsic to the network itself. For a 2-port network with the 2x2 scattering matrix *S*, and with a source and load connected to its input and output, where the reflections off the source back into the input are $\Gamma _{S}$ and the reflections off the load back into the output are $\Gamma _{L}$ , then the reflection coefficients at the input and output are given by:

$|\Gamma _{\mathrm {in} }|=\left|S_{11}+{\frac {S_{12}S_{21}\Gamma _{L}}{1-S_{22}\Gamma _{L}}}\right|$

and

$|\Gamma _{\mathrm {out} }|=\left|S_{22}+{\frac {S_{12}S_{21}\Gamma _{S}}{1-S_{11}\Gamma _{S}}}\right|$

## Seismology

Reflection coefficient is used in feeder testing for reliability of medium.

## Optics and microwaves

In optics and electromagnetics in general, *reflection coefficient* can refer to either the amplitude reflection coefficient described here, or the reflectance, depending on context. Typically, the reflectance is represented by a capital *R*, while the amplitude reflection coefficient is represented by a lower-case *r*. These related concepts are covered by Fresnel equations in classical optics.

## Acoustics

Acousticians use reflection coefficients to understand the effect of different materials on their acoustic environments. The field properties used to define the reflection coefficient are typically the acoustic pressure and velocity in the incident and reflected acoustic waves.
