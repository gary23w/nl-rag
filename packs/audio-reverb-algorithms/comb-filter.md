---
title: "Comb filter"
source: https://en.wikipedia.org/wiki/Comb_filter
domain: audio-reverb-algorithms
license: CC-BY-SA-4.0
tags: audio reverb algorithm, artificial reverberation, comb filter reverb, reverberation dsp
fetched: 2026-07-02
---

# Comb filter

In signal processing, a **comb filter** is a filter implemented by adding a delayed version of a signal to itself, causing constructive and destructive interference. The frequency response of a comb filter consists of a series of regularly spaced notches in between regularly spaced *peaks* (sometimes called *teeth*), giving the appearance of a comb.

Comb filters exist in two forms, *feedforward* and *feedback*, which refer to the direction in which signals are delayed before they are added to the input.

Comb filters may be implemented in discrete time or continuous time forms, which are very similar.

## Applications

Comb filters are employed in a variety of signal processing applications, including:

- Cascaded integrator–comb (CIC) filters, commonly used for anti-aliasing during interpolation and decimation operations that change the sample rate of a discrete-time system.
- 2D and 3D comb filters implemented in hardware (and occasionally software) in PAL and NTSC analog television decoders reduce artifacts such as dot crawl.
- Audio signal processing, including delay, flanging, physical modelling synthesis and digital waveguide synthesis. If the delay is set to a few milliseconds, a comb filter can model the effect of acoustic standing waves in a cylindrical cavity or in a vibrating string.
- In astronomy the astro-comb promises to increase the precision of existing spectrographs by nearly a hundredfold.

In acoustics, comb filtering can arise as an unwanted artifact. For instance, two loudspeakers playing the same signal at different distances from the listener create a comb filtering effect on the audio. In any enclosed space, listeners hear a mixture of direct sound and reflected sound. The reflected sound takes a longer, delayed path compared to the direct sound, and a comb filter is created where the two mix at the listener. Similarly, comb filtering may result from mono mixing of multiple mics, hence the 3:1 rule of thumb that neighboring mics should be separated at least three times the distance from its source to the mic.

## Discrete time implementation

### Feedforward form

The general structure of a feedforward comb filter is described by the difference equation:

$y[n]=x[n]+\alpha x[n-K]$

where K is the delay length (measured in samples), and *α* is a scaling factor applied to the delayed signal. The *z* transform of both sides of the equation yields:

$Y(z)=\left(1+\alpha z^{-K}\right)X(z)$

The transfer function is defined as:

$H(z)={\frac {Y(z)}{X(z)}}=1+\alpha z^{-K}={\frac {z^{K}+\alpha }{z^{K}}}$

#### Frequency response

The frequency response of a discrete-time system expressed in the *z*-domain is obtained by substitution $z=e^{j\omega },$ where j is the imaginary unit and $\omega$ is angular frequency. Therefore, for the feedforward comb filter:

$H\left(e^{j\omega }\right)=1+\alpha e^{-j\omega K}$

Using Euler's formula, the frequency response is also given by

$H\left(e^{j\omega }\right)={\bigl [}1+\alpha \cos(\omega K){\bigr ]}-j\alpha \sin(\omega K)$

Often of interest is the *magnitude* response, which ignores phase. This is defined as:

$\left|H\left(e^{j\omega }\right)\right|={\sqrt {{\text{Re}}\left\{H\left(e^{j\omega }\right)\right\}^{2}+{\text{Im}}\left\{H\left(e^{j\omega }\right)\right\}^{2}}}$

In the case of the feedforward comb filter, this is:

${\begin{aligned}\left|H(e^{j\omega })\right|&={\sqrt {(1+\alpha \cos(\omega K))^{2}+(\alpha \sin(\omega K))^{2}}}\\&={\sqrt {(1+\alpha ^{2})+2\alpha \cos(\omega K)}}\end{aligned}}$

The $(1+\alpha ^{2})$ term is constant, whereas the $2\alpha \cos(\omega K)$ term varies periodically. Hence, the magnitude response of the comb filter is periodic.

The graphs show the periodic magnitude response for various values of $\alpha .$ Some important properties:

- The response periodically drops to a local minimum (sometimes known as a *notch*), and periodically rises to a local maximum (sometimes known as a *peak* or a *tooth*).
- For positive values of $\alpha$ , the first minimum occurs at half the delay period and repeats at odd multiples of the delay frequency thereafter:

${\begin{aligned}f&={\frac {f_{s}}{2K}},{\frac {3f_{s}}{2K}},{\frac {5f_{s}}{2K}}\cdots \\\omega &={\frac {\pi }{K}},{\frac {3\pi }{K}},{\frac {5\pi }{K}}\cdots \,\end{aligned}}$

- For negative values of $\alpha$ , the first minimum occurs at DC and repeats at even multiples of the delay frequency thereafter:

${\begin{aligned}f&=0,{\frac {f_{s}}{K}},{\frac {2f_{s}}{K}},{\frac {3f_{s}}{K}}\cdots \\\omega &=0,{\frac {2\pi }{K}},{\frac {4\pi }{K}},{\frac {6\pi }{K}}\cdots \,\end{aligned}}$

- The levels of the maxima and minima are always equidistant from 1.
- When $\alpha =\pm 1,$ the minima have zero amplitude. In this case, the minima are sometimes known as *nulls*.
- The maxima for positive values of $\alpha$ coincide with the minima for negative values of $\alpha$ , and vice versa.

#### Impulse response

The feedforward comb filter is one of the simplest finite impulse response filters. Its response is simply the initial impulse with a second impulse after the delay.

#### Pole–zero interpretation

Looking again at the *z*-domain transfer function of the feedforward comb filter:

$H(z)={\frac {z^{K}+\alpha }{z^{K}}}$

the numerator is equal to zero whenever *zK* = −*α*. This has *K* solutions, equally spaced around a circle in the complex plane; these are the zeros of the transfer function. The denominator is zero at *zK* = 0, giving *K* poles at *z* = 0. This leads to a pole–zero plot like the ones shown.

|   |   |
|---|---|

Similarly, the general structure of a feedback comb filter is described by the difference equation:

$y[n]=x[n]+\alpha y[n-K]$

This equation can be rearranged so that all terms in y are on the left-hand side, and then taking the *z* transform:

$\left(1-\alpha z^{-K}\right)Y(z)=X(z)$

The transfer function is therefore:

$H(z)={\frac {Y(z)}{X(z)}}={\frac {1}{1-\alpha z^{-K}}}={\frac {z^{K}}{z^{K}-\alpha }}$

#### Frequency response

By substituting $z=e^{j\omega }$ into the feedback comb filter's *z*-domain expression:

$H\left(e^{j\omega }\right)={\frac {1}{1-\alpha e^{-j\omega K}}}\,,$

the magnitude response becomes:

$\left|H\left(e^{j\omega }\right)\right|={\frac {1}{\sqrt {\left(1+\alpha ^{2}\right)-2\alpha \cos(\omega K)}}}\,.$

Again, the response is periodic, as the graphs demonstrate. The feedback comb filter has some properties in common with the feedforward form:

- The response periodically drops to a local minimum and rises to a local maximum.
- The maxima for positive values of $\alpha$ coincide with the minima for negative values of $\alpha ,$ and vice versa.
- For positive values of $\alpha$ , the first maximum occurs at 0 and repeats at even multiples of the delay frequency thereafter:

${\begin{aligned}f&=0,{\frac {f_{s}}{K}},{\frac {2f_{s}}{K}},{\frac {3f_{s}}{K}}\cdots \\\omega &=0,{\frac {2\pi }{K}},{\frac {4\pi }{K}},{\frac {6\pi }{K}}\cdots \end{aligned}}$

- For negative values of $\alpha$ , the first maximum occurs at $\omega =\pi$ and repeats at odd multiples of the delay frequency thereafter:

${\begin{aligned}f&={\frac {f_{s}}{2K}},{\frac {3f_{s}}{2K}},{\frac {5f_{s}}{2K}}\cdots \\\omega &={\frac {\pi }{K}},{\frac {3\pi }{K}},{\frac {5\pi }{K}}\cdots \end{aligned}}$

However, there are also some important differences because the magnitude response has a term in the denominator:

- The levels of the maxima and minima are no longer equidistant from 1. The maxima have an amplitude of ⁠1/1 − *α*⁠.
- The filter is only stable if |*α*| is strictly less than 1. As can be seen from the graphs, as |*α*| increases, the amplitude of the maxima rises increasingly rapidly.

#### Impulse response

The feedback comb filter is a simple type of infinite impulse response filter. If stable, the response simply consists of a repeating series of impulses decreasing in amplitude over time.

#### Pole–zero interpretation

Looking again at the *z*-domain transfer function of the feedback comb filter:

$H(z)={\frac {z^{K}}{z^{K}-\alpha }}$

This time, the numerator is zero at *zK* = 0, giving *K* zeros at *z* = 0. The denominator is equal to zero whenever *zK* = *α*. This has *K* solutions, equally spaced around a circle in the complex plane; these are the poles of the transfer function. This leads to a pole–zero plot like the ones shown below.

|   |   |
|---|---|

## Continuous time implementation

Comb filters may also be implemented in continuous time, which can be expressed in the Laplace domain as a function of the complex frequency domain parameter $s=\sigma +j\omega$ analogous to the z domain. Analog circuits use some form of analog delay line for the delay element. Continuous-time implementations share all the properties of the respective discrete-time implementations.

### Feedforward form

The feedforward form may be described by the equation:

$y(t)=x(t)+\alpha x(t-\tau )$

where *τ* is the delay (measured in seconds). This has the following transfer function:

$H(s)=1+\alpha e^{-s\tau }$

The feedforward form consists of an infinite number of zeros spaced along the jω axis (which corresponds to the Fourier domain).

The feedback form has the equation:

$y(t)=x(t)+\alpha y(t-\tau )$

and the following transfer function:

$H(s)={\frac {1}{1-\alpha e^{-s\tau }}}$

The feedback form consists of an infinite number of poles spaced along the jω axis.
