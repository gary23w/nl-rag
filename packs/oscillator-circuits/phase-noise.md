---
title: "Phase noise"
source: https://en.wikipedia.org/wiki/Phase_noise
domain: oscillator-circuits
license: CC-BY-SA-4.0
tags: electronic oscillator, Colpitts oscillator, crystal oscillator, phase noise
fetched: 2026-07-02
---

# Phase noise

In signal processing, **phase noise** is the frequency-domain representation of random fluctuations in the phase of a waveform, corresponding to time-domain deviations from perfect periodicity (jitter). Generally speaking, radio-frequency engineers speak of the phase noise of an oscillator, whereas digital-system engineers work with the jitter of a clock.

## Definitions

An ideal oscillator would generate a pure sine wave. In the frequency domain, this would be represented as a single pair of Dirac delta functions (positive and negative conjugates) at the oscillator's frequency; i.e., all the signal's power is at a single frequency. All real oscillators have phase modulated noise components. The phase noise components spread the power of a signal to adjacent frequencies, resulting in noise sidebands.

Consider the following noise-free signal:

$x(t)=A\cos(2\pi f_{0}t)$

Phase noise is added to this signal by adding a stochastic process represented by $\phi (t)$ to the signal as follows:

$x(t)=A\cos(2\pi f_{0}t+\phi (t))$

Different phase noise processes, $\phi (t)$ , possess different power Spectral density (PSD). For example, a white noise PSD follows a $f^{0}$ trend, a pink noise PSD follows a $f^{-1}$ trend, and a brown noise PSD follows a $f^{-2}$ trend.

$\operatorname {S} _{\phi }(f)$ is the single-sided (f>0) **phase noise PSD** $\left[{\frac {rad^{2}}{Hz}}\right]$ , given by the Fourier transform of the Autocorrelation of the phase noise, as stated in the Wiener–Khinchin theorem.

$\operatorname {S} _{\phi }(f)={\mathcal {F}}\left[\operatorname {E} \left[\phi (t){\overline {\phi (t+\tau )}}\right]\right]$

The noise can also be represented at the single-sided (f>0) **frequency noise PSD**, $\operatorname {S} _{\Delta \nu }(f)\left[{\frac {Hz^{2}}{Hz}}\right]$ , or the **fractional frequency stability PSD**, $\operatorname {S} _{y}(f)\left[{\frac {1}{Hz}}\right]$ , which defines the frequency fluctuations in terms of the deviation from the carrier frequency, $f_{0}$ .

$\operatorname {S} _{\Delta \nu }(f)=f^{2}\operatorname {S} _{\phi }(f)$

$\operatorname {S} _{y}(f)={\frac {\operatorname {S} _{\Delta \nu }(f)}{f_{0}^{2}}}={\frac {f^{2}\operatorname {S} _{\phi }(f)}{f_{0}^{2}}}$

The phase noise can also be given as the **spectral purity**, ${\mathcal {L}}\left(f\right)\left[{\frac {dBc}{Hz}}\right]$ , the single-sideband power in a 1 Hz bandwidth at a frequency offset, f, from the carrier frequency, $f_{0}$ , referenced to the carrier power.

${\mathcal {L}}\left(f\right)=10\log _{10}\left({\frac {\operatorname {S} _{\phi }(f)}{2}}\right)$

The stochastic dynamics of $\phi (t)$ due to white noise can be understood as a random walk or diffusion process, with a characteristic diffusion coefficient D . The variance of $\phi (t)$ grows with time t according to ${\overline {\phi ^{2}(t)}}=2Dt$ , and the PSD of the signal $x(t)$ yields what is described above in case of white noise perturbation. If phase diffusion is faster (larger D ) for a given signal amplitude A , the PSD becomes wider and shorter, yielding larger phase noise. The problem of determining the PSD (phase noise) is commensurate with determining D .

## Jitter conversions

Phase noise is sometimes also measured and expressed as a power obtained by integrating ℒ(*f*) over a certain range of offset frequencies. For example, the phase noise may be −40 dBc integrated over the range of 1 kHz to 100 kHz. This integrated phase noise (expressed in degrees) can be converted to **jitter** (expressed in seconds) using the following formula:

${\text{jitter (seconds}})={\frac {{\text{phase error (}}{}^{\circ }{\text{)}}}{360^{\circ }\times {\text{frequency (hertz)}}}}$

In the absence of 1/f noise in a region where the phase noise displays a –20 dBc/decade slope (Leeson's equation), the RMS cycle jitter can be related to the phase noise by:

$\sigma _{c}^{2}={\frac {f^{2}{\mathcal {L}}\left(f\right)}{f_{\text{osc}}^{3}}}$

Likewise:

${\mathcal {L}}\left(f\right)={\frac {f_{\text{osc}}^{3}\sigma _{c}^{2}}{f^{2}}}$

## Measurement

Phase noise can be measured using a spectrum analyzer if the phase noise of the device under test (DUT) is large with respect to the spectrum analyzer's local oscillator. Care should be taken that observed values are due to the measured signal and not the shape factor of the spectrum analyzer's filters. Spectrum analyzer based measurement can show the phase-noise power over many decades of frequency; e.g., 1 Hz to 10 MHz. The slope with offset frequency in various offset frequency regions can provide clues as to the source of the noise; e.g., low frequency flicker noise decreasing at 30 dB per decade (= 9 dB per octave).

Phase noise measurement systems are alternatives to spectrum analyzers. These systems may use internal and external references and allow measurement of both residual (additive) and absolute noise. Additionally, these systems can make low-noise, close-to-the-carrier, measurements.

## Linewidths

The sinusoidal output of an ideal oscillator is a Dirac delta function in the power spectral density centered at the frequency of the sinusoid. Such perfect spectral purity is not achievable in a practical oscillator. Spreading of the spectrum line caused by phase noise is characterized by the fundamental linewidth and the integral linewidth.

The **fundamental linewidth**, also known as the White noise-limited linewidth or the intrinsic linewidth, is the linewidth of an oscillator's PSD in the presence of only white noise sources (noise with a PSD that follows a $f^{0}$ trend, ie. equivalent across all frequencies). The fundamental linewidth takes Lorentzian spectral line shape, and is given by twice the phase diffusion constant, $2D$ (full width, half maximum). White noise provides a $1/{\sqrt {\tau }}$ Allan Deviation plot at small averaging times.

The **integral linewidth**, also known as the effective linewidth or the total linewidth, is the linewidth of an oscillator's PSD in the presence of both white noise sources (noise with a PSD that follows a $f^{0}$ trend) and pink noise sources (noise with a PSD that follows a $f^{-1}$ trend). Pink noise is sometimes called Flicker noise, or simply 1/f noise. The integral linewidth takes Voigt lineshape, a convolution of the white noise-induced Lorentzian lineshape and the pink noise-induced Gaussian lineshape. Pink noise provides a $\tau ^{0}$ Allan Deviation plot at moderate averaging times. This flat line on the Allan Deviation plot is also known as the flicker floor.

Additionally, the oscillator might experience Frequency drift over long periods of time, slowly moving the center frequency of the Voigt lineshape. This drift is a brown noise source (noise with a PSD that follows a $f^{-2}$ trend), and provides a ${\sqrt {\tau }}$ Allan Deviation plot at large averaging times.

## Limiting System Performance

A laser is a common oscillator that is characterized by its noise, and thus its Laser linewidth. The laser noise provides fundamental limitations of the systems that the laser is used in, such as loss of sensitivity in radar and communications systems, lack of definition in imaging systems, and a higher bit error rate in digital systems.

Lasers with a near-Infrared center wavelength are used in many atomic, molecular, and optical physics experiments to provide photons that interact with atoms. The requirements for the spectral purity at specific frequency offsets of the lasers used in qubit operation (such as clock transition lasers and state preparation lasers) are highly stringent because the coherence time of the qubit is directly related to the linewidth of the lasers.
