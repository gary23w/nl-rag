---
title: "Butterworth filter"
source: https://en.wikipedia.org/wiki/Butterworth_filter
domain: active-filters
license: CC-BY-SA-4.0
tags: active filter, Sallen-Key topology, state variable filter, gyrator circuit
fetched: 2026-07-02
---

# Butterworth filter

The **Butterworth filter** is a type of signal processing filter designed to have a frequency response that is as flat as possible in the passband. It is also referred to as a **maximally flat magnitude filter**. It was first described in 1930 by the British engineer and physicist Stephen Butterworth in his paper entitled "On the Theory of Filter Amplifiers".

## Original paper

Butterworth had a reputation for solving very complex mathematical problems thought to be 'impossible'. At the time, filter design required a considerable amount of designer experience due to limitations of the theory then in use. The filter was not in common use for over 30 years after its publication. Butterworth stated that:

> "An ideal electrical filter should not only completely reject the unwanted frequencies but should also have uniform sensitivity for the wanted frequencies".

Such an ideal filter cannot be achieved, but Butterworth showed that successively closer approximations were obtained with increasing numbers of filter elements of the right values. At the time, filters generated substantial ripple in the passband, and the choice of component values was highly interactive. Butterworth showed that a low-pass filter could be designed whose gain as a function of frequency (i.e., the magnitude of its frequency response) is:

$G(\omega )={\frac {1}{\sqrt {1+{\omega }^{2n}}}},$

where $\omega$ is the angular frequency in radians per second and n is the number of poles in the filter—equal to the number of reactive elements in a passive filter. Its cutoff frequency (the half-power point of approximately −3 dB or a voltage gain of 1/√2 ≈ 0.7071) is normalized to 𝜔 = 1 radian per second. Butterworth only dealt with filters with an even number of poles in his paper, though odd-order filters can be created with the addition of a single-pole filter applied to the output of the even-order filter. He built his higher-order filters from 2-pole filters separated by vacuum tube amplifiers. His plot of the frequency response of 2-, 4-, 6-, 8-, and 10-pole filters is shown as A, B, C, D, and E in his original graph.

Butterworth solved the equations for two-pole and four-pole filters, showing how the latter could be cascaded when separated by vacuum tube amplifiers and so enabling the construction of higher-order filters despite inductor losses. In 1930, low-loss core materials such as molypermalloy had not been discovered and air-cored audio inductors were rather lossy. Butterworth discovered that it was possible to adjust the component values of the filter to compensate for the winding resistance of the inductors.

He used coil forms of 1.25 inches (32 mm) in diameter and 3 inches (76 mm) in length with plug-in terminals. Associated capacitors and resistors were contained inside the wound coil form. The coil formed part of the plate load resistor. Two poles were used per vacuum tube and RC coupling was used to the grid of the following tube.

Butterworth also showed that the basic low-pass filter could be modified to give low-pass, high-pass, band-pass and band-stop functionality.

## Overview

The frequency response of the Butterworth filter is maximally flat (i.e., has no ripples) in the passband and rolls off towards zero in the stopband. When viewed on a logarithmic Bode plot, the response slopes off linearly towards negative infinity. A first-order filter's response rolls off at −6 dB per octave (−20 dB per decade) (all first-order lowpass filters have the same normalized frequency response). A second-order filter decreases at −12 dB per octave, a third-order at −18 dB and so on. Butterworth filters have a monotonically changing magnitude function with $\omega$ , unlike other filter types that have non-monotonic ripple in the passband or the stopband.

Compared with a Chebyshev Type I/Type II filter or an elliptic filter, the Butterworth filter has a slower roll-off, and thus will require a higher order to implement a particular stopband specification, but Butterworth filters have a more linear phase response in the passband than Chebyshev Type I/Type II and elliptic filters can achieve.

## Example

A transfer function of a third-order low-pass Butterworth filter design shown in the figure on the right looks like this:

${\frac {V_{o}(s)}{V_{i}(s)}}={\frac {R_{4}}{s^{3}(L_{1}C_{2}L_{3})+s^{2}(L_{1}C_{2}R_{4})+s(L_{1}+L_{3})+R_{4}}}$

A simple example of a Butterworth filter is the third-order low-pass design shown in the figure on the right, with $C_{2}$  = 4/3 F, $R_{4}$  = 1 Ω, $L_{1}$  = 3/2 H, and $L_{3}$  = 1/2 H. Taking the impedance of the capacitors C to be $1/(Cs)$ and the impedance of the inductors L to be $Ls$ , where $s=\sigma +j\omega$ is the complex frequency, the circuit equations yield the transfer function for this device:

$H(s)={\frac {V_{o}(s)}{V_{i}(s)}}={\frac {1}{1+2s+2s^{2}+s^{3}}}.$

The magnitude of the frequency response (gain) $G(\omega )$ is given by

$G(\omega )=|H(j\omega )|={\frac {1}{\sqrt {1+\omega ^{6}}}},$

obtained from

$G^{2}(\omega )=|H(j\omega )|^{2}=H(j\omega )\cdot H^{*}(j\omega )={\frac {1}{1+\omega ^{6}}},$

and the phase is given by

$\Phi (\omega )=\arg(H(j\omega )).\!$

The group delay is defined as the negative derivative of the phase shift with respect to angular frequency and is a measure of the distortion in the signal introduced by phase differences for different frequencies. The gain and the delay for this filter are plotted in the graph on the left. There are no ripples in the gain curve in either the passband or the stopband.

The log of the absolute value of the transfer function $H(s)$ is plotted in complex frequency space in the second graph on the right. The function is defined by the three poles in the left half of the complex frequency plane.

These are arranged on a circle of radius unity, symmetrical about the real s axis. The gain function will have three more poles on the right half-plane to complete the circle.

By replacing each inductor with a capacitor and each capacitor with an inductor, a high-pass Butterworth filter is obtained.

A band-pass Butterworth filter is obtained by placing a capacitor in series with each inductor and an inductor in parallel with each capacitor to form resonant circuits. The value of each new component must be selected to resonate with the old component at the frequency of interest.

A band-stop Butterworth filter is obtained by placing a capacitor in parallel with each inductor and an inductor in series with each capacitor to form resonant circuits. The value of each new component must be selected to resonate with the old component at the frequency that is to be rejected.

## Transfer function

Like all filters, the typical prototype is the low-pass filter, which can be modified into a high-pass filter, or placed in series with others to form band-pass and band-stop filters, and higher order versions of these.

The gain $G(\omega )$ of an n th-order Butterworth low-pass filter is given in terms of the transfer function $H(s)$ as

$G^{2}(\omega )=\left|H(j\omega )\right|^{2}={\frac {{G_{0}}^{2}}{1+\left({\frac {\omega }{\omega _{c}}}\right)^{2n}}}$

where n is the order of filter, $\omega _{c}$ is the cutoff frequency (approximately the −3 dB frequency), and $G_{0}$ is the DC gain (gain at zero frequency).

It can be seen that as n approaches infinity, the gain becomes a rectangle function and frequencies below $\omega _{c}$ will be passed with gain $G_{0}$ , while frequencies above $\omega _{c}$ will be suppressed. For smaller values of n , the cutoff will be less sharp.

We wish to determine the transfer function $H(s)$ where $s=\sigma +j\omega$ (from Laplace transform). Because $\left|H(s)\right|^{2}=H(s){\overline {H(s)}}$ and, as a general property of Laplace transforms at $s=j\omega$ , $H(-j\omega )={\overline {H(j\omega )}}$ , if we select $H(s)$ such that:

$H(s)H(-s)={\frac {{G_{0}}^{2}}{1+\left({\frac {-s^{2}}{\omega _{c}^{2}}}\right)^{n}}},$

then, with $s=j\omega$ , we have the frequency response of the Butterworth filter.

The n poles of this expression occur on a circle of radius $\omega _{c}$ at equally-spaced points, and symmetric around the negative real axis. For stability, the transfer function, $H(s)$ , is therefore chosen such that it contains only the poles in the negative real half-plane of s . The k -th pole is specified by

$-{\frac {s_{k}^{2}}{\omega _{c}^{2}}}=(-1)^{\frac {1}{n}}=e^{\frac {j(2k-1)\pi }{n}}\qquad k=1,2,3,\ldots ,n$

and hence

$s_{k}=\omega _{c}e^{\frac {j(2k+n-1)\pi }{2n}}\qquad k=1,2,3,\ldots ,n.$

The transfer (or system) function may be written in terms of these poles as

$H(s)=G_{0}\prod _{k=1}^{n}{\frac {\omega _{c}}{s-s_{k}}}=G_{0}\prod _{k=1}^{n}{\frac {\omega _{c}}{s-\omega _{c}e^{\frac {j(2k+n-1)\pi }{2n}}}}$

.

where $\textstyle {\prod }$ is the product of a sequence operator. The denominator is a Butterworth polynomial in s .

### Normalized Butterworth polynomials

The Butterworth polynomials may be written in complex form as above, but are usually written with real coefficients by multiplying pole pairs that are complex conjugates, such as $s_{1}$ and $s_{n}$ . The polynomials are normalized by setting $\omega _{c}=1$ . The normalized Butterworth polynomials then have the general product form

$B_{n}(s)=\prod _{k=1}^{\frac {n}{2}}\left[s^{2}-2s\cos \left({\frac {2k+n-1}{2n}}\,\pi \right)+1\right]\qquad n={\text{even}}$

$B_{n}(s)=(s+1)\prod _{k=1}^{\frac {n-1}{2}}\left[s^{2}-2s\cos \left({\frac {2k+n-1}{2n}}\,\pi \right)+1\right]\qquad n={\text{odd}}.$

Factors of Butterworth polynomials of order 1 through 10 are shown in the following table (to six decimal places).

| nFactors of Butterworth Polynomials $B_{n}(s)$ 1 $(s+1)$ 2 $(s^{2}+1.414214s+1)$ 3 $(s+1)(s^{2}+s+1)$ 4 $(s^{2}+0.765367s+1)(s^{2}+1.847759s+1)$ 5 $(s+1)(s^{2}+0.618034s+1)(s^{2}+1.618034s+1)$ 6 $(s^{2}+0.517638s+1)(s^{2}+1.414214s+1)(s^{2}+1.931852s+1)$ 7 $(s+1)(s^{2}+0.445042s+1)(s^{2}+1.246980s+1)(s^{2}+1.801938s+1)$ 8 $(s^{2}+0.390181s+1)(s^{2}+1.111140s+1)(s^{2}+1.662939s+1)(s^{2}+1.961571s+1)$ 9 $(s+1)(s^{2}+0.347296s+1)(s^{2}+s+1)(s^{2}+1.532089s+1)(s^{2}+1.879385s+1)$ 10 $(s^{2}+0.312869s+1)(s^{2}+0.907981s+1)(s^{2}+1.414214s+1)(s^{2}+1.782013s+1)(s^{2}+1.975377s+1)$ |
|---|

Factors of Butterworth polynomials of order 1 through 6 are shown in the following table (Exact).

| nFactors of Butterworth Polynomials $B_{n}(s)$ 1 $(s+1)$ 2 $(s^{2}+{\sqrt {2}}s+1)$ 3 $(s+1)(s^{2}+s+1)$ 4 $(s^{2}+{\sqrt {2-{\sqrt {2}}}}s+1)(s^{2}+{\sqrt {2+{\sqrt {2}}}}s+1)$ 5 $(s+1)(s^{2}+\varphi ^{-1}s+1)(s^{2}+\varphi s+1)$ 6 $(s^{2}+{\sqrt {2-{\sqrt {3}}}}s+1)(s^{2}+{\sqrt {2}}s+1)(s^{2}+{\sqrt {2+{\sqrt {3}}}}s+1)$ |
|---|

where the Greek letter phi ( $\varphi$ or $\phi$ ) represents the golden ratio. It is an irrational number that is a solution to the quadratic equation $x^{2}-x-1=0,$ with a value of

$\varphi ={\frac {1+{\sqrt {5}}}{2}}=1.618033988749...$

(

OEIS

:

A001622

)

The nth Butterworth polynomial can also be written as a sum

$B_{n}(s)=\sum _{k=0}^{n}a_{k}s^{k}\,,$

with its coefficients $a_{k}$ given by the recursion formula

${\frac {a_{k+1}}{a_{k}}}={\frac {\cos(k\gamma )}{\sin((k+1)\gamma )}}$

and by the product formula

$a_{k}=\prod _{\mu =1}^{k}{\frac {\cos((\mu -1)\gamma )}{\sin(\mu \gamma )}}\,,$

where

$a_{0}=1\qquad {\text{and}}\qquad \gamma ={\frac {\pi }{2n}}\,.$

Further, $a_{k}=a_{n-k}$ . The rounded coefficients $a_{k}$ for the first 10 Butterworth polynomials $B_{n}(s)$ are:

Butterworth Coefficients

$a_{k}$

to Four Decimal Places

n

$a_{0}$

$a_{1}$

$a_{2}$

$a_{3}$

$a_{4}$

$a_{5}$

$a_{6}$

$a_{7}$

$a_{8}$

$a_{9}$

$a_{10}$

1

1

1

2

1

1.4142

1

3

1

2

2

1

4

1

2.6131

3.4142

2.6131

1

5

1

3.2361

5.2361

5.2361

3.2361

1

6

1

3.8637

7.4641

9.1416

7.4641

3.8637

1

7

1

4.4940

10.0978

14.5918

14.5918

10.0978

4.4940

1

8

1

5.1258

13.1371

21.8462

25.6884

21.8462

13.1371

5.1258

1

9

1

5.7588

16.5817

31.1634

41.9864

41.9864

31.1634

16.5817

5.7588

1

10

1

6.3925

20.4317

42.8021

64.8824

74.2334

64.8824

42.8021

20.4317

6.3925

1

The normalized Butterworth polynomials can be used to determine the transfer function for any low-pass filter cut-off frequency $\omega _{c}$ , as follows

$H(s)={\frac {G_{0}}{B_{n}(a)}}$

, where

$a={\frac {s}{\omega _{c}}}.$

Transformation to other bandforms are also possible, see prototype filter.

### Maximal flatness

Assuming $\omega _{c}=1$ and $G_{0}=1$ , the derivative of the gain with respect to frequency can be shown to be

${\frac {dG}{d\omega }}=-nG^{3}\omega ^{2n-1}$

which is monotonically decreasing for all $\omega$ since the gain G is always positive. The gain function of the Butterworth filter therefore has no ripple. The series expansion of the gain is given by

$G(\omega )=1-{\frac {1}{2}}\omega ^{2n}+{\frac {3}{8}}\omega ^{4n}+\ldots$

In other words, all derivatives of the gain up to but not including the 2 n -th derivative are zero at $\omega =0$ , resulting in "maximal flatness". If the requirement to be monotonic is limited to the passband only and ripples are allowed in the stopband, then it is possible to design a filter of the same order, such as the inverse Chebyshev filter, that is flatter in the passband than the "maximally flat" Butterworth.

### High-frequency roll-off

Again assuming $\omega _{c}=1$ , the slope of the log of the gain for large $\omega$ is

$\lim _{\omega \rightarrow \infty }{\frac {d\log(G)}{d\log(\omega )}}=-n.$

In decibels, the high-frequency roll-off is therefore 20 n  dB/decade, or 6 n  dB/octave (the factor of 20 is used because the power is proportional to the square of the voltage gain; see 20 log rule.)

### Minimum order

To design a Butterworth filter using the minimum required number of elements, the minimum order of the Butterworth filter may be calculated as follows.

$n=\left\lceil {\frac {\log {{\bigr (}{\frac {10^{\alpha _{s}/10}-1}{10^{\alpha _{p}/10}-1}}}{\bigr )}}{2\log {(\omega _{s}/\omega _{p})}}}\right\rceil$

where:

$\omega _{p}$

and

$\alpha _{p}$

are the pass band frequency and attenuation at that frequency in dB.

$\omega _{s}$

and

$\alpha _{s}$

are the stop band frequency and attenuation at that frequency in dB.

n

is the minimum number of poles, the order of the filter.

$\lceil \cdot \rceil$

denotes the

ceiling function

.

### Nonstandard cutoff attenuation

The cutoff attenuation for Butterworth filters is usually defined to be −3.01 dB. If it is desired to use a different attenuation at the cutoff frequency, then the following factor may be applied to each pole, whereupon the poles will continue to lie on a circle, but the radius will no longer be unity. The cutoff attenuation equation may be derived through algebraic manipulation of the Butterworth defining equation stated at the top of the page.

${\begin{aligned}p_{A}=p_{1}\times (10^{\alpha /10}-1)^{{-1}/{2n}}&\qquad {\text{For 0}}\leq \alpha <\infty \end{aligned}}$

where:

$p_{A}$

is the relocated pole positioned to set the desired cutoff attenuation.

$p_{1}$

is a

−

3.01 dB cutoff pole that lies on the unit circle.

$\alpha$

is the desired attenuation at the cutoff frequency in dB (1 dB, 10 dB, etc.).

n

is the number of poles, the order of the filter.

## Filter implementation and design

There are several different filter topologies available to implement a linear analogue filter. The most often used topology for a passive realisation is the Cauer topology, and the most often used topology for an active realisation is the Sallen–Key topology.

### Cauer topology

The Cauer topology uses passive components (shunt capacitors and series inductors) to implement a linear analog filter. The Butterworth filter having a given transfer function can be realised using a Cauer 1-form. The *k*-th element is given by

$C_{k}=2\sin \left[{\frac {(2k-1)}{2n}}\pi \right]\qquad k={\text{odd}}$

$L_{k}=2\sin \left[{\frac {(2k-1)}{2n}}\pi \right]\qquad k={\text{even}}.$

The filter may start with a series inductor if desired, in which case the *Lk* are *k* odd and the *Ck* are *k* even. These formulae may usefully be combined by making both *Lk* and *Ck* equal to *gk*. That is, *gk* is the immittance divided by *s*.

$g_{k}=2\sin \left[{\frac {(2k-1)}{2n}}\pi \right]\qquad k=1,2,3,\ldots ,n.$

These formulae apply to a doubly terminated filter (that is, the source and load impedance are both equal to unity) with ωc = 1. This prototype filter can be scaled for other values of impedance and frequency. For a singly terminated filter (that is, one driven by an ideal voltage or current source) the element values are given by

$g_{j}={\frac {a_{j}a_{j-1}}{c_{j-1}g_{j-1}}}\qquad j=2,3,\ldots ,n$

where

$g_{1}=a_{1}$

and

$a_{j}=\sin \left[{\frac {(2j-1)}{2n}}\pi \right]\qquad j=1,2,3,\ldots ,n$

$c_{j}=\cos ^{2}\left[{\frac {j}{2n}}\pi \right]\qquad j=1,2,3,\ldots ,n.$

Voltage driven filters must start with a series element and current driven filters must start with a shunt element. These forms are useful in the design of diplexers and multiplexers.

### Sallen–Key topology

The Sallen–Key topology uses active and passive components (noninverting buffers, usually op amps, resistors, and capacitors) to implement a linear analog filter. Each Sallen–Key stage implements a conjugate pair of poles; the overall filter is implemented by cascading all stages in series. If there is a real pole (in the case where n is odd), this must be implemented separately, usually as an RC circuit, and cascaded with the active stages.

For the second-order Sallen–Key circuit shown to the right the transfer function is given by

$H(s)={\frac {V_{\text{out}}(s)}{V_{\text{in}}(s)}}={\frac {1}{1+C_{2}(R_{1}+R_{2})s+C_{1}C_{2}R_{1}R_{2}s^{2}}}.$

We wish the denominator to be one of the quadratic terms in a Butterworth polynomial. Assuming that $\omega _{c}=1$ , this will mean that

$C_{1}C_{2}R_{1}R_{2}=1\,$

and

$C_{2}(R_{1}+R_{2})=-2\cos \left({\frac {2k+n-1}{2n}}\pi \right).$

This leaves two undefined component values that may be chosen at will.

Butterworth lowpass filters with Sallen–Key topology of third and fourth order, using only one op amp, are described by Huelsman, and further single-amplifier Butterworth filters also of higher order are given by Jurišić et al.

### Digital implementation

Digital implementations of Butterworth and other filters are often based on the bilinear transform method or the matched Z-transform method, two different methods to discretize an analog filter design. In the case of all-pole filters such as the Butterworth, the matched Z-transform method is equivalent to the impulse invariance method. For higher orders, digital filters are sensitive to quantization errors, so they are often calculated as cascaded biquad sections, plus one first-order or third-order section for odd orders.

## Comparison with other linear filters

Properties of the Butterworth filter are:

- Monotonic amplitude response in both passband and stopband
- Quick roll-off around the cutoff frequency, which improves with increasing order
- Considerable overshoot and ringing in step response, which worsens with increasing order
- Slightly non-linear phase response
- Group delay largely frequency-dependent

Here is an image showing the gain of a discrete-time Butterworth filter next to other common filter types. All of these filters are fifth-order.

The Butterworth filter rolls off more slowly around the cutoff frequency than the Chebyshev filter or the Elliptic filter, but without ripple.
