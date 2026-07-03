---
title: "Active filter"
source: https://en.wikipedia.org/wiki/Active_filter
domain: electronic-filter
license: CC-BY-SA-4.0
tags: electronic filter
fetched: 2026-07-03
---

# Active filter

An **active filter** is a type of analog circuit implementing an electronic filter using active components, typically an amplifier. Amplifiers included in a filter design can be used to improve the cost, performance and predictability of a filter.

An amplifier prevents the load impedance of the following stage from affecting the characteristics of the filter. An active filter can have complex poles and zeros without using a bulky or expensive inductor. The shape of the response, the Q (quality factor), and the tuned frequency can often be set with inexpensive variable resistors. In some active filter circuits, one parameter can be adjusted without affecting the others.

## Types

Using active elements has some limitations. Basic filter design equations neglect the finite bandwidth of amplifiers. Available active devices have limited bandwidth, so they are often impractical at high frequencies. Amplifiers consume power and inject noise into a system. Certain circuit topologies may be impractical if no DC path is provided for bias current to the amplifier elements. Power handling capability is limited by the amplifier stages.

Active filter circuit configurations (electronic filter topology) include:

- Sallen-Key, and VCVS filters (low sensitivity to component tolerance)
- State variable filters and biquadratic or biquad filters
- Dual amplifier bandpass (DABP)
- Wien notch
- Multiple feedback filters
- Fliege (lowest component count for 2 opamp but with good controllability over frequency and type)
- Akerberg Mossberg (one of the topologies that offer complete and independent control over gain, frequency, and type)

Active filters can implement the same transfer functions as passive filters. Common transfer functions are:

- High-pass filter – attenuation of frequencies below their cut-off points.
- Low-pass filter – attenuation of frequencies above their cut-off points.
- Band-pass filter – attenuation of frequencies both above and below those they allow to pass.
- Band-stop filter (Notch filter) – attenuation of certain frequencies while allowing all others to pass.

Combinations are possible, such as notch and high-pass (in a

rumble filter

where most of the offending rumble comes from a particular frequency). Another example is an

elliptic filter

.

## Design of active filters

To design filters, the specifications that need to be established include:

- The range of desired frequencies (the passband) together with the shape of the frequency response. This indicates the variety of filter (see above) and the center or corner frequencies.
- Input and output impedance requirements. These limit the circuit topologies available; for example, most, but not all active filter topologies provide a buffered (low impedance) output. However, remember that the internal output impedance of operational amplifiers, if used, may rise markedly at high frequencies and reduce the attenuation from that expected. Be aware that some high-pass filter topologies present the input with almost a short circuit to high frequencies.
- Dynamic range of the active elements. The amplifier should not saturate (run into the power supply rails) at expected input signals, nor should it be operated at such low amplitudes that noise dominates.
- The degree to which unwanted signals should be rejected.
  - In the case of narrow-band bandpass filters, the Q determines the -3 dB bandwidth but also the degree of rejection of frequencies far removed from the center frequency; if these two requirements are in conflict then a staggered-tuning bandpass filter may be needed.
  - For notch filters, the degree to which unwanted signals at the notch frequency must be rejected determines the accuracy of the components, but not the Q, which is governed by desired steepness of the notch, i.e. the bandwidth around the notch before attenuation becomes small.
  - For high-pass and low-pass (as well as band-pass filters far from the center frequency), the required rejection may determine the slope of attenuation needed, and thus the "order" of the filter. A second-order all-pole filter gives an ultimate slope of about 12 dB per octave (40 dB/decade), but the slope close to the corner frequency is much less, sometimes necessitating a notch be added to the filter.
- The allowable "ripple" (variation from a flat response, in decibels) within the passband of high-pass and low-pass filters, along with the shape of the frequency response curve near the corner frequency, determine the damping ratio or damping factor (= 1/(2Q)). This also affects the phase response, and the time response to a square-wave input. Several important response shapes (damping ratios) have well-known names:
  - Chebyshev filter – peaking/ripple in the passband before the corner; Q>0.7071 for 2nd-order filters.
  - Butterworth filter – maximally flat amplitude response; Q=0.7071 for 2nd-order filters
  - Legendre–Papoulis filter – trades off some flatness in the passband, though still monotonic, for a steeper fall-off
  - Linkwitz–Riley filter – desirable properties for audio crossover applications, fastest rise time with no overshoot; Q = 0.5 (critically damped)
  - Paynter or transitional Thompson-Butterworth or "compromise" filter – faster fall-off than Bessel; Q=0.639 for 2nd-order filters
  - Bessel filter – maximally flat group delay; Q=0.577 for 2nd-order filters. It provides good linear phase.
  - Elliptic filter or Cauer filter – add a notch (or "zero") just outside the passband, to give a much greater slope in this region than the combination of order and damping ratio *without* the notch. The output is similar to the ideal filter(i.e., good flat response of both pass band and the stop band).

### Comparison to passive filters

An active filter can have gain, increasing the power available in a signal compared to the input. Passive filters dissipate energy from a signal and cannot have a net power gain. For some ranges of frequencies, for example at audio frequencies and below, an active filter can realize a given transfer function without using inductors, which are relatively large and costly components compared to resistors and capacitors, and which are more expensive to make with the required high quality and accurate values. This advantage may not be as important for active filters entirely integrated on a chip because the available capacitors have relatively low values and so require high value resistors which take up area of the integrated circuit. Active filters have good isolation between stages, and can provide high input impedance and low output impedance; this makes their characteristics independent of the source and load impedances. Multiple stages can be cascaded when desired to improve characteristics. In contrast, design of multiple-stage passive filters must take into account each stage's frequency-dependent loading of the preceding stage. It is feasible to make active filters tunable over a wide range, compared with passive filters. Since inductors are not used, filters can be made in a very compact size and do not produce or interact with magnetic fields that may be present.

Compared with active filters, passive filters require no additional power supplies. The amplifying devices of an active filter must provide predictable gain and performance over the entire frequency range to be processed; the gain–bandwidth product of the amplifier will constrain the maximum frequency that can be used.
