---
title: "Total harmonic distortion"
source: https://en.wikipedia.org/wiki/Total_harmonic_distortion
domain: power-factor-correction
license: CC-BY-SA-4.0
tags: power factor correction, total harmonic distortion, displacement power factor, reactive power
fetched: 2026-07-02
---

# Total harmonic distortion

The **total harmonic distortion** (**THD** or **THDi**) is a measurement of the harmonic distortion present in a signal and is defined as the ratio of the sum of the powers of all harmonic components to the power of the fundamental frequency. **Distortion factor**, a closely related term, is sometimes used as a synonym.

In audio systems, lower distortion means that the components in a loudspeaker, amplifier or microphone or other equipment produce a more accurate reproduction of an audio recording.

In radio communications, devices with lower THD tend to produce less unintentional interference with other electronic devices. Since harmonic distortion can potentially widen the frequency spectrum of the output emissions from a device by adding signals at multiples of the input frequency, devices with high THD are less suitable in applications such as spectrum sharing and spectrum sensing.

In power systems, lower THD implies lower peak currents, less heating, lower electromagnetic emissions, and less core loss in motors. It is a key metric in the stability and quality of the U.S. electrical grid. IEEE Standard 519-2022 covers the recommended practice and requirements for harmonic control in electric power systems.

## Definitions and examples

To understand a system with an input and an output, such as an audio amplifier, we start with an ideal system where the transfer function is linear and time-invariant. When a sinusoidal signal of frequency *ω* passes through a non-ideal, non-linear device, additional content is added at integer multiples *nω* (harmonics) of the original frequency. THD is a measure of that additional signal content not present in the input signal.

When the main performance criterion is the "purity" of the original sine wave (in other words, the contribution of the original frequency with respect to its harmonics), the measurement is most commonly defined as the ratio of the RMS amplitude of a set of higher harmonic frequencies to the RMS amplitude of the first harmonic, or fundamental frequency

$\mathrm {THD_{F}} ={\frac {\sqrt {V_{2}^{2}+V_{3}^{2}+V_{4}^{2}+\cdots }}{V_{1}}},$

where *Vn* is the RMS value of the *n*th harmonic voltage, and *V*1 is the RMS value of the fundamental component.

In practice, the THDF is commonly used in audio distortion specifications (percentage THD); however, THD is a non-standardized specification, and the results between manufacturers are not easily comparable. Since individual harmonic amplitudes are measured, it is required that the manufacturer disclose the test signal frequency range, level and gain conditions, and number of measurements taken. It is possible to measure the full 20 Hz–20 kHz range using a sweep (though distortion for a fundamental above 10 kHz is inaudible).

Measurements for calculating the THD are made at the output of a device under specified conditions. The THD is usually expressed in percent or in dB relative to the fundamental as distortion attenuation.

A variant definition uses the fundamental plus harmonics as the reference:

$\mathrm {THD_{R}} ={\frac {\sqrt {V_{2}^{2}+V_{3}^{2}+V_{4}^{2}+\cdots }}{\sqrt {V_{1}^{2}+V_{2}^{2}+V_{3}^{2}+\cdots }}}={\frac {\mathrm {THD_{F}} }{\sqrt {1+\mathrm {THD_{F}^{2}} }}}.$

These can be distinguished as **THDF** (for "fundamental"), and **THDR** (for "root mean square"). THDR cannot exceed 100%. At low distortion levels, the difference between the two calculation methods is negligible. For instance, a signal with THDF of 10% has a very similar THDR of 9.95%. However, at higher distortion levels the discrepancy becomes large. For instance, a signal with THDF 266% has a THDR of 94%. A pure square wave with infinite harmonics has THDF of 48.3% and THDR of 43.5%.

Some use the term "distortion factor" as a synonym for THDR, while others use it as a synonym for THDF.

The International Electrotechnical Commission (IEC) also defines another term *total harmonic factor* for the "ratio of the RMS value of the harmonic content of an alternating quantity to the RMS value of the quantity" using a different equation.

## THD + N

**THD + N** means total harmonic distortion plus noise. This measurement is much more common and more comparable between devices. It is usually measured by inputting a sine wave, notch-filtering the output, and comparing the ratio between the output signal with and without the sine wave:

${\text{THD+N}}={\frac {\displaystyle \sum _{n=2}^{\infty }{\text{harmonics}}+{\text{noise}}}{\text{fundamental}}}.$

Like the THD measurement, this is a ratio of RMS amplitudes and can be measured as THDF (bandpassed or calculated fundamental as the denominator) or, more commonly, as THDR (total distorted signal as the denominator).

A meaningful measurement must include the bandwidth of measurement. This measurement includes effects from ground-loop power-line hum, high-frequency interference, intermodulation distortion between these tones and the fundamental, and so on, in addition to harmonic distortion. For psychoacoustic measurements, a weighting curve is applied such as A-weighting or ITU-R BS.468, which is intended to accentuate what is most audible to the human ear, contributing to a more accurate measurement. A-weighting is a rough way to estimate the frequency sensitivity of every persons' ears, as it does not take into account the non-linear behavior of the ear. The loudness model proposed by Zwicker includes these complexities. The model is described in the German standard DIN 45631.

For a given input frequency and amplitude, THD + N is reciprocal to SINAD, provided that both measurements are made over the same bandwidth.

## Measurement

The distortion of a waveform relative to a pure sinewave can be measured either by using a THD analyzer to analyse the output wave into its constituent harmonics and noting the amplitude of each relative to the fundamental; or by cancelling out the fundamental with a notch filter and measuring the remaining signal, which will be total aggregate harmonic distortion plus noise.

Given a sinewave generator of very low inherent distortion, it can be used as input to amplification equipment, whose distortion at different frequencies and signal levels can be measured by examining the output waveform.

There is electronic equipment both to generate sinewaves and to measure distortion; but a general-purpose digital computer equipped with a sound card can carry out harmonic analysis with suitable software. Different software can be used to generate sinewaves, but the inherent distortion may be too high for measurement of very low-distortion amplifiers.

### Interpretation

For many purposes, different types of harmonics are not equivalent. For instance, crossover distortion at a given THD is much more audible than clipping distortion at the same THD, since the harmonics produced by crossover distortion are nearly as strong at higher-frequency harmonics, such as 10× to 20× the fundamental, as they are at lower-frequency harmonics like 3× or 5× the fundamental. Those harmonics appearing far away in frequency from a fundamental (desired signal) are not as easily masked by that fundamental. In contrast, at the onset of clipping, harmonics first appear at low-order frequencies and gradually start to occupy higher-frequency harmonics. A single THD number is therefore inadequate to specify audibility and must be interpreted with care. Taking THD measurements at different output levels would expose whether the distortion is clipping (which decreases with a decreasing level) or crossover (which stays constant with varying output level, and thus is a *greater percentage* of the sound produced at low volumes).

THD is a summation of a number of harmonics equally weighted, even though research performed decades ago identifies that lower-order harmonics are harder to hear at the same level, compared with higher-order ones. In addition, even-order harmonics are said to be generally harder to hear than odd-order. A number of methods have been developed to estimate the actual audibility of THD, used to quantify crossover distortion or loudspeaker rub and buzz, such as "high-order harmonic distortion" (HOHD) or "higher harmonic distortion" (HHD) which measures only the 10th and higher harmonics, or metrics that apply psychoacoustic loudness curves to the residual.

## Examples

For many standard signals, the above criterion may be calculated analytically in a closed form. For example, a pure square wave has THDF equal to

$\mathrm {THD_{F}} ={\sqrt {{\frac {\pi ^{2}}{8}}-1}}\approx 0.483=48.3\%.$

The sawtooth signal possesses

$\mathrm {THD_{F}} ={\sqrt {{\frac {\pi ^{2}}{6}}-1}}\approx 0.803=80.3\%.$

The pure symmetrical triangle wave has

$\mathrm {THD_{F}} ={\sqrt {{\frac {\pi ^{4}}{96}}-1}}\approx 0.121=12.1\%.$

For the rectangular pulse train with the *duty cycle* *μ* (called sometimes the *cyclic ratio*), the THDF has the form

$\operatorname {THD_{F}} (\mu )={\sqrt {{\frac {\mu (1-\mu )\pi ^{2}}{2\sin ^{2}\pi \mu }}-1}},\quad 0<\mu <1,$

and logically, reaches the minimum (≈0.483) when the signal becomes symmetrical *μ* = 0.5, i.e. the pure square wave. Appropriate filtering of these signals may drastically reduce the resulting THD. For instance, the pure square wave filtered by the Butterworth low-pass filter of the second order (with the cutoff frequency set equal to the fundamental frequency) has THDF of 5.3%, while the same signal filtered by the fourth-order filter has THDF of 0.6%. However, analytic computation of the THDF for complicated waveforms and filters often represents a difficult task, and the resulting expressions may be quite laborious to obtain. For example, the closed-form expression for the THDF of the sawtooth wave filtered by the first-order Butterworth low-pass filter is simply

$\mathrm {THD_{F}} ={\sqrt {{\frac {\pi ^{2}}{3}}-\pi \coth \pi }}\approx 0.370=37.0\%,$

while that for the same signal filtered by the second-order Butterworth filter is given by a rather cumbersome formula

$\mathrm {THD_{F}} ={\sqrt {\pi {\frac {\cot {\dfrac {\pi }{\sqrt {2}}}\cdot \coth ^{2}{\dfrac {\pi }{\sqrt {2}}}-\cot ^{2}{\dfrac {\pi }{\sqrt {2}}}\cdot \coth {\dfrac {\pi }{\sqrt {2}}}-\cot {\dfrac {\pi }{\sqrt {2}}}-\coth {\dfrac {\pi }{\sqrt {2}}}}{{\sqrt {2}}\left(\cot ^{2}{\dfrac {\pi }{\sqrt {2}}}+\coth ^{2}{\dfrac {\pi }{\sqrt {2}}}\right)}}+{\frac {\pi ^{2}}{3}}-1}}\approx 0.181=18.1\%.$

Yet, the closed-form expression for the THDF of the pulse train filtered by the *p*th-order Butterworth low-pass filter is even more complicated and has the following form:

$\operatorname {THD_{F}} (\mu ,p)=\csc \pi \mu \cdot {\sqrt {\mu (1-\mu )\pi ^{2}-\sin ^{2}\pi \mu -{\frac {\pi }{2}}\sum _{s=1}^{2p}{\frac {\cot \pi z_{s}}{z_{s}^{2}}}\prod \limits _{\scriptstyle l=1 \atop \scriptstyle l\neq s}^{2p}{\frac {1}{z_{s}-z_{l}}}+{\frac {\pi }{2}}\operatorname {Re} \sum _{s=1}^{2p}{\frac {e^{i\pi z_{s}(2\mu -1)}}{z_{s}^{2}\sin \pi z_{s}}}\prod \limits _{\scriptstyle l=1 \atop \scriptstyle l\neq s}^{2p}{\frac {1}{z_{s}-z_{l}}}}},$

where *μ* is the duty cycle, 0 < *μ* < 1, and

$z_{l}\equiv \exp {\frac {i\pi (2l-1)}{2p}},\quad l=1,2,\ldots ,2p.$
