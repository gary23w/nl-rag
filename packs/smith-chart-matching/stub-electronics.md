---
title: "Stub (electronics)"
source: https://en.wikipedia.org/wiki/Stub_(electronics)
domain: smith-chart-matching
license: CC-BY-SA-4.0
tags: antenna tuner, quarter-wave transformer, impedance matching, matching stub
fetched: 2026-07-02
---

# Stub (electronics)

In microwave and radio-frequency engineering, a **stub** or **resonant stub** is a transmission line or waveguide connected at one end only. The free end of the stub is either left open-circuit, or short-circuited (as is always the case for waveguides). Neglecting transmission line losses, the input impedance of the stub is purely reactive; either capacitive or inductive, depending on the electrical length of the stub, and on whether it is open or short circuit. Stubs may thus function as capacitors, inductors and resonant circuits at radio frequencies.

The behaviour of stubs is due to standing waves along their length. Their reactive properties are determined by their physical length in relation to the wavelength of the radio waves. Therefore, stubs are most commonly used in UHF or microwave circuits in which the wavelengths are short enough that the stub is conveniently small. They are often used to replace discrete capacitors and inductors, because at UHF and microwave frequencies lumped components perform poorly due to parasitic reactance. Stubs are commonly used in antenna impedance matching circuits, frequency selective filters, and resonant circuits for UHF electronic oscillators and RF amplifiers.

Stubs can be constructed with any type of transmission line: parallel conductor line (where they are called Lecher lines), coaxial cable, stripline, waveguide, and dielectric waveguide. Stub circuits can be designed using a Smith chart, a graphical tool which can determine what length line to use to obtain a desired reactance.

## Short circuited stub

The input impedance of a lossless, short circuited line is,

$Z_{\mathsf {sc}}~=~j\ Z_{0}\ \tan(\ \beta \ell \ )~$

where

$\ j\$

is the

imaginary unit

(

$\ j^{2}\equiv -1\$

),

$\ Z_{0}\$

is the

characteristic impedance

of the line,

$\ \beta =2\pi /\lambda \$

is the

phase constant

of the line, and

$\ \ell \$

is the physical length of the line.

Thus, depending on whether $\ \tan(\beta \ell )\$ is positive or negative, the short circuited stub will be inductive or capacitive, respectively.

The length of a stub to act as a capacitor C at an angular frequency of $\ \omega \$ is then given by:

$\ell ~=~{\frac {1}{\ \beta \ }}\left[\ (n+1)\ \pi \ -\ \arctan \left({\frac {1}{\ \omega CZ_{0}\ }}\right)\ \right]~;$

the length of a stub to act as an inductor L at the same frequency is given by:

$\ell ~=~{\frac {1}{\ \beta \ }}\left[\ n\ \pi \ +\ \arctan \left({\frac {\ \omega L\ }{\ Z_{0}\ }}\right)\ \right]~,$

where in both equations, n is an integer number of half-wavelengths (possibly zero) that can be arbitrarily added to the line without changing the impedance.

## Open circuited stub

The input impedance of a lossless open circuit stub is given by

$Z_{\mathsf {oc}}=-j\ Z_{0}\ \cot(\ \beta \ell \ )~,$

where the symbols $\ Z_{0},\beta ,\ell ,\omega ,\$ etc. used in this section have the same meaning as in the section above.

It follows that depending on whether $\cot(\beta \ell )$ is positive or negative, the stub will be capacitive or inductive, respectively.

The length of an open circuit stub to act as an inductor L at an angular frequency of $\ \omega \$ is:

$\ell ~=~{\frac {1}{\ \beta \ }}\left[\ (n+1)\ \pi \ -\ \operatorname {arccot} \left({\frac {\ \omega L\ }{Z_{0}}}\right)\ \right]~=~{\frac {1}{\ \beta \ }}\left[\ (n+1)\ \pi \ -\ \arctan \left({\frac {Z_{0}}{\ \omega L\ }}\right)\ \right]~;$

the length of an open circuit stub to act as a capacitor C at the same frequency is:

$\ell ~=~{\frac {1}{\ \beta \ }}\left[\ n\ \pi \ +\ \operatorname {arccot} \left({\frac {1}{\ \omega CZ_{0}\ }}\right)\ \right]~=~{\frac {1}{\ \beta \ }}\left[\ n\ \pi \ +\ \arctan \left(\ \omega CZ_{0}\ \right)\ \right]~,$

where again, n is an arbitrary whole number of half-wavelengths that can be inserted into the segment (including zero).

## Resonant stub

Stubs are often used as resonant circuits in oscillators and distributed element filters. An open circuit stub of length $\ \ell$ will have a capacitive impedance at low frequency when $\ \beta \ell <\pi /2$ . Above this frequency the impedance is inductive. At precisely $\beta \ell =\pi /2$ the stub presents a short circuit. This is qualitatively the same behaviour as a series resonant circuit. For a lossless line the phase change constant is proportional to frequency,

$\beta ={\omega \over v}$

where $\ v$ is the velocity of propagation and is constant with frequency for a lossless line. For such a case the resonant frequency is given by,

$\omega _{0}={\frac {\pi v}{2\ell }}$

While stubs function as resonant circuits, they differ from lumped element resonant circuits in that they have multiple resonant frequencies; in addition to the fundamental resonant frequency $\ \omega _{0}\,$ , they resonate at multiples of this frequency: $\ n\omega _{0}\,$ . The impedance will not continue to rise monotonically with frequency after resonance as in a lumped tuned circuit. It will rise until the point where $\ \beta l=\pi$ at which point it will be open circuit. After this point (which is an anti-resonance point), the impedance will again become capacitive and start to fall. It will continue to fall until at $\ \beta l=3\pi /2\,$ it again presents a short circuit. At this point, the filtering action of the stub has failed. This response of the stub continues to repeat with increasing frequency alternating between resonance and anti-resonance. It is not only a characteristic of stubs but of all distributed element filters that there is some frequency beyond which the filter fails and multiple unwanted passbands are produced.

Similarly, a short circuit stub is an anti-resonator at $\ \pi /2$ , that is, it behaves as a parallel resonant circuit, but again fails as $\ 3\pi /2$ is approached.

## Stub matching

Stubs can match a load impedance to the transmission line characteristic impedance. The stub is positioned a distance from the load. This distance is chosen so that at that point, the resistive part of the load impedance is made equal to the resistive part of the characteristic impedance by impedance transformer action of the length of the main line. The length of the stub is chosen so that it exactly cancels the reactive part of the presented impedance. The stub is made capacitive or inductive according to whether the main line presents an inductive or capacitive impedance, respectively. This is not the same as the actual impedance of the load since the reactive part of the load impedance will be subject to impedance transformer action and the resistive part. Matching stubs can be made adjustable so that matching can be corrected on test.

A single stub will only achieve a perfect match at one specific frequency. Multiple stubs can be placed along the main transmission line to achieve wideband matching. This creates a structure similar to a filter. Filter design methods, such as Chebyshev filter design, may be used, but the focus is on impedance matching rather than passband performance. The resulting transmission function of the network has a passband ripple like the Chebyshev filter, but the ripples never reach 0 dB insertion loss at any point in the passband, as they would do for the standard filter.

## Radial stub

Radial stubs are a planar component that consists of a sector of a circle rather than a constant-width line. They are used with planar transmission lines when a low impedance stub is required. Low characteristic impedance lines require a wide line. With a wide line, the junction of the stub with the main line is not at a well-defined point. Radial stubs overcome this difficulty by narrowing to a point at the junction. Filter circuits using stubs often use them in pairs, one connected to each side of the main line. A pair of radial stubs so connected is called a butterfly stub or a bowtie stub.

## Unwanted stub

Open circuit stubs can inadvertently be created in the design of printed circuit boards. A 1⁄4-wavelength stub would completely cancel out the desired signal and historically the elimination of extraneous conductors have managed to avoid this issue. However, higher-frequency signaling on the order of 12 Gbps (6 GHz) have greatly decreased the length of the stub required to reach 1⁄4-wavelength, making vias a new common culprit. Since the 2020s, backdrilling is used to shorten vias so that they do not affect the intended signal frequency.

Elimination of extraneous conductors may run contrary to a desire to make a device extensible or more easily testable. For example, it used to be common practice to leave openings on computer memory buses where additional DIMM (memory modules) can be plugged in. However, at DDR5/LPDDR5 data rates, the stubs become a limiting factor for achieving higher signaling frequencies.
