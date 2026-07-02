---
title: "Quarter-wave impedance transformer"
source: https://en.wikipedia.org/wiki/Quarter-wave_impedance_transformer
domain: smith-chart-matching
license: CC-BY-SA-4.0
tags: antenna tuner, quarter-wave transformer, impedance matching, matching stub
fetched: 2026-07-02
---

# Quarter-wave impedance transformer

A **quarter-wave impedance transformer**, often written as **λ/4 impedance transformer**, is a transmission line or waveguide used in electrical engineering of length one-quarter wavelength (λ), terminated with some known impedance. It presents at its input the dual of the impedance with which it is terminated.

The relationship between the characteristic impedance, *Z*0, input impedance, *Z*in and load impedance, *Z*L is: ${\frac {Z_{\mathrm {in} }}{Z_{0}}}={\frac {Z_{0}}{Z_{L}}}$

Alternatives to the quarter-wave impedance transformer include lumped circuits that can produce the impedance inverter function, and stubs for impedance matching.

## Applications

At radio frequencies of upper VHF or higher up to microwave frequencies one quarter wavelength is conveniently short enough to incorporate the component within many products, but not so small that it cannot be manufactured using normal engineering tolerances, and it is at these frequencies where the device is most often encountered. It is especially useful for making an inductor out of a capacitor, since designers have a preference for the latter.

Another application is when DC power needs to be fed into a transmission line, which may be necessary to power an active device connected to the line, such as a switching transistor or a varactor diode for instance. An ideal DC voltage source has zero impedance, that is, it presents a short circuit and it is not useful to connect a short circuit directly across the line. Feeding in the DC via a λ/4 transformer will transform the short circuit into an open circuit which has no effect on the signals on the line. Likewise, an open circuit can be transformed into a short circuit.

The device can be used as a component in a filter, and in this application it is sometimes known as an inverter because it produces the mathematical inverse of an impedance. Impedance inverters are not to be confused with the more common meaning of power inverter for a device that has the inverse function of a rectifier. Inverter is a general term for the class of circuits that have the function of inverting an impedance. There are many such circuits and the term does not necessarily imply a λ/4 transformer. The most common use for inverters is to convert a 2-element-kind *LC* filter design such as a ladder network into a one-element-kind filter. Equally, for bandpass filters, a two-resonator-kind (resonators and anti-resonators) filter can be converted to a one-resonator-kind. Inverters are classified as *K*-inverters or *J*-inverters depending on whether they are inverting a series impedance or a shunt admittance. Filters incorporating λ/4 inverters are only suitable for narrow band applications. This is because the impedance transformer line only has the correct electrical length of λ/4 at one specific frequency. The further the signal is from this frequency the less accurately the impedance transformer will be reproducing the impedance inverter function and the less accurately it will be representing the element values of the original lumped-element filter design.

## Theory of operation

A transmission line that is terminated in some impedance, *Z*L, that is different from the characteristic impedance, *Z*0, will result in a wave being reflected from the termination back to the source. At the input to the line the reflected voltage adds to the incident voltage and the reflected current subtracts (because the wave is travelling in the opposite direction) from the incident current. The result is that the input impedance of the line (ratio of voltage to current) differs from the characteristic impedance and for a line of length *l* is given by;

$Z_{\mathrm {in} }=Z_{0}{\frac {Z_{L}+Z_{0}\tanh(\gamma l)}{Z_{0}+Z_{L}\tanh(\gamma l)}}$

where

γ

is the line

propagation constant

.

A very short transmission line, such as those being considered here, in many situations will have no appreciable loss along the length of the line and the propagation constant can be considered to be purely imaginary phase constant, *iβ* and the impedance expression reduces to,

$Z_{\mathrm {in} }=Z_{0}{\frac {Z_{L}+iZ_{0}\tan(\beta l)}{Z_{0}+iZ_{L}\tan(\beta l)}}$

Since *β* is the same as the angular wavenumber,

$\beta ={\frac {2\pi }{\lambda }}\ ,$

for a quarter-wavelength line,

$l={\frac {\lambda }{4}}\ ,$

$\beta l={\pi \over 2}\ ,$

and the impedance becomes, taking the limit as the tangent function argument approaches $\pi \over 2$

$Z_{\mathrm {in} }=\lim _{\beta l\rightarrow \pi /2}{Z_{0}{\frac {Z_{L}+iZ_{0}\tan({\beta l})}{Z_{0}+iZ_{L}\tan({\beta l})}}}=Z_{0}{\frac {iZ_{0}}{iZ_{L}}}={\frac {{Z_{0}}^{2}}{Z_{L}}}$

which is the same as the condition for dual impedances;

${\frac {Z_{\mathrm {in} }}{Z_{0}}}={\frac {Z_{0}}{Z_{L}}}$

## Alternatives

Similar properties can be realized using either a "T" or "PI" network consisting of lumped elements each of which has a reactance equal to the Zo of the simulated one-quarter wavelength (λ), transmission line. This realization of the transformer is useful at lower frequencies where a quarter-wave transmission line would be impractically long. As with the physical transmission line, the relationship between the characteristic impedance, *Z*0, input impedance, *Z*in and load impedance, *Z*L is: ${\frac {Z_{\mathrm {in} }}{Z_{0}}}={\frac {Z_{0}}{Z_{L}}}$

The quarter wave transformer is an alternative to a stub; but, whereas a stub is terminated in a short (or open) circuit and the length is chosen so as to produce the required impedance transformation, the λ/4 transformer is in series with the load and its length and characteristic impedance are designed to produce the required impedance transformation. The quarter wave transformer is a subset of series line (section) matching methods.
