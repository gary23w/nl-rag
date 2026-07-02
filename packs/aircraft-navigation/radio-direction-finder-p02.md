---
title: "Direction finding (part 2/2)"
source: https://en.wikipedia.org/wiki/Radio_direction_finder
domain: aircraft-navigation
license: CC-BY-SA-4.0
tags: air navigation, instrument landing system, vhf omnidirectional range, distance measuring equipment
fetched: 2026-07-02
part: 2/2
---

## DF by amplitude comparison

Amplitude comparison has been popular as a method for DF because systems are relatively simple to implement, have good sensitivity and, very importantly, a high probability of signal detection. Typically, an array of four, or more, squinted directional antennas is used to give 360 degree coverage. DF by phase comparison methods can give better bearing accuracy, but the processing is more complex. Systems using a single rotating dish antenna are more sensitive, small and relatively easy to implement, but have poor PoI.

Usually, the signal amplitudes in two adjacent channels of the array are compared, to obtain the bearing of an incoming wavefront but, sometimes, three adjacent channels are used to give improved accuracy. Although the gains of the antennas and their amplifying chains have to be closely matched, careful design and construction and effective calibration procedures can compensate for shortfalls in the hardware. Overall bearing accuracies of 2° to 10° (rms) have been reported using the method.

### Two-channel DF

Two-channel DF, using two adjacent antennas of a circular array, is achieved by comparing the signal power of the largest signal with that of the second largest signal. The direction of an incoming signal, within the arc described by two antennas with a squint angle of Φ, may be obtained by comparing the relative powers of the signals received. When the signal is on the boresight of one of the antennas, the signal at the other antenna will be about 12 dB lower. When the signal direction is halfway between the two antennas, signal levels will be equal and approximately 3 dB lower than the boresight value. At other bearing angles, φ, some intermediate ratio of the signal levels will give the direction.

If the antenna main lobe patterns have a Gaussian characteristic, and the signal powers are described in logarithmic terms (e.g. decibels (dB) relative to the boresight value), then there is a linear relationship between the bearing angle φ and the power level difference, i.e.: $\varphi \propto P_{1}({\text{dB}})-P_{2}({\text{dB}}),$ where *P*1(dB) and *P*2(dB) are the outputs of two adjacent channels. The thumbnail shows a typical plot.

To give 360° coverage, antennas of a circular array are chosen, in pairs, according to the signal levels received at each antenna. If there are N antennas in the array, at angular spacing (squint angle) Φ, then Φ = 2π/*N* radians (= 360/*N* degrees).

#### Basic equations for two-port DF

If the main lobes of the antennas have a Gaussian characteristic, then the output *P*1(*φ*), as a function of bearing angle φ, is given by

$P_{1}(\varphi )=G_{0}\exp \left[-A\left({\frac {\varphi }{\Psi _{0}}}\right)^{2}\right]$

where

G

0

is the

antenna boresight

gain (i.e. when

φ

= 0

),

Ψ

0

is one half the half-power

beamwidth

A

=

–

ln(0.5)

, so that

P

1

(

φ

)/

G

0

= 0.5

when

φ

= Ψ

0

and angles are in radians.

The second antenna, squinted at Φ and with the same boresight gain *G*0 gives an output

$P_{2}=G_{0}\exp \left[-A\left({\frac {\Phi -\varphi }{\Psi _{0}}}\right)^{2}\right]$

Comparing signal levels,

${\frac {P_{1}}{P_{2}}}={\frac {G_{0}\exp \left[-A\left({\frac {\varphi }{\Psi _{0}}}\right)^{2}\right]}{G_{0}\exp \left[-A\left({\frac {\Phi -\varphi }{\Psi _{0}}}\right)^{2}\right]}}=\exp \left[{\frac {A}{\Psi _{0}^{2}}}\left(\Phi ^{2}-2\Phi \varphi \right)\right]$

The natural logarithm of the ratio is

$\ln \left({\frac {P_{1}}{P_{2}}}\right)=\ln P_{1}-\ln P_{2}={\frac {A}{\Psi _{0}^{2}}}\left(\Phi ^{2}-2\Phi \varphi \right)$

Rearranging: $\varphi ={\frac {\Psi _{0}^{2}}{2A\Phi }}\left(\ln P_{2}-\ln P_{1}\right)+{\frac {\Phi }{2}}$

This shows the linear relationship between the output level difference, expressed logarithmically, and the bearing angle φ.

Natural logarithms can be converted to decibels (dBs) (where dBs are referred to boresight gain) by using $\ln(X)={\tfrac {X({\text{dB}})}{10\log _{10}(e)}},$ so the equation can be written

$\varphi ={\frac {\Psi _{0}^{2}}{6.0202\,\Phi }}{\bigl (}P_{2}({\text{dB}})-P_{1}({\text{dB}}){\bigr )}+{\frac {\Phi }{2}}$

### Three-channel DF

Improvements in bearing accuracy may be achieved if amplitude data from a third antenna are included in the bearing processing.

For three-channel DF, with three antennas squinted at angles Φ, the direction of the incoming signal is obtained by comparing the signal power of the channel containing the largest signal with the signal powers of the two adjacent channels, situated at each side of it.

For the antennas in a circular array, three antennas are selected according to the signal levels received, with the largest signal present at the central channel.

When the signal is on the boresight of Antenna 1 (*φ* = 0), the signal from the other two antennas will equal and about 12 dB lower. When the signal direction is halfway between two antennas (*φ* = 30°), their signal levels will be equal and approximately 3 dB lower than the boresight value, with the third signal now about 24 dB lower. At other bearing angles, φ, some intermediate ratios of the signal levels will give the direction.

#### Basic equations for three-port DF

For a signal incoming at a bearing φ, taken here to be to the right of boresight of Antenna 1, the three channel outputs are the following:

${\begin{aligned}P_{1}&=G_{T}\exp \left[-A\left({\frac {\varphi }{\Psi _{0}}}\right)^{2}\right]\\[4pt]P_{2}&=G_{T}\exp \left[-A\left({\frac {\Phi -\varphi }{\Psi _{0}}}\right)^{2}\right]\\[4pt]P_{3}&=G_{T}\exp \left[-A\left({\frac {\Phi +\varphi }{\Psi _{0}}}\right)^{2}\right]\end{aligned}}$

where GT is the overall gain of each channel, including antenna boresight gain, and is assumed to be the same in all three channels. As before, in these equations, angles are in radians, Φ = 360/*N* degrees = 2π/*N* radians and *A* = –ln(0.5).

As earlier, these can be expanded and combined to give:

${\begin{aligned}\ln P_{1}-\ln P_{2}&={\frac {A}{\Psi _{0}^{2}}}(\Phi ^{2}-2\Phi \varphi )\\[4pt]\ln P_{1}-\ln P_{3}&={\frac {A}{\Psi _{0}^{2}}}(\Phi ^{2}+2\Phi \varphi )\end{aligned}}$

Eliminating ${\tfrac {A}{\Psi _{0}^{2}}}$ and rearranging:

$\varphi ={\frac {\Delta _{1,2}-\Delta _{1,3}}{\Delta _{1,2}+\Delta _{1,3}}}{\frac {\Phi }{2}}={\frac {\Delta _{2,3}}{\Delta _{1,2}+\Delta _{1,3}}}{\frac {\Phi }{2}}$

where:

${\begin{aligned}\Delta _{1,3}&=\ln P_{1}-\ln P_{3}\\[2pt]\Delta _{1,2}&=\ln P_{1}-\ln P_{2}\\[2pt]\Delta _{2,3}&=\ln P_{2}-\ln P_{3}\end{aligned}}$

The difference values here are in nepers but could be in decibels.

The bearing value, obtained using this equation, is independent of the antenna beamwidth (= 2Ψ0), so this value does not have to be known for accurate bearing results to be obtained. Also, there is a smoothing affect, for bearing values near to the boresight of the middle antenna, so there is no discontinuity in bearing values there, as an incoming signals moves from left to right (or vice versa) through boresight, as can occur with 2-channel processing.

### Bearing uncertainty due to noise

Many of the causes of bearing error, such as mechanical imperfections in the antenna structure, poor gain matching of receiver gains, or non-ideal antenna gain patterns may be compensated by calibration procedures and corrective look-up tables, but thermal noise will always be a degrading factor. As all systems generate thermal noise then, when the level of the incoming signal is low, the signal-to-noise ratios in the receiver channels will be poor, and the accuracy of the bearing prediction will suffer.

In general, a guide to bearing uncertainty is given by

$\Delta \varphi _{\text{RMS}}=0.724{\frac {2\Psi _{0}}{\sqrt {{\text{SNR}}_{0}}}}\quad {\text{[degrees]}}$

for a signal at crossover, but where SNR0 is the signal-to-noise ratio that would apply at boresight.

To obtain more precise predictions at a given bearing, the actual S:N ratios of the signals of interest are used. (The results may be derived assuming that noise induced errors are approximated by relating differentials to uncorrelated noise).

For adjacent processing using, say, Channel 1 and Channel 2, the bearing uncertainty (angle noise), Δ*φ* (rms), is given below. In these results, square-law detection is assumed and the SNR figures are for signals at video (baseband), for the bearing angle φ.

$\Delta \varphi _{\text{RMS}}={\frac {\Phi }{2}}{\frac {\Psi _{0}^{2}}{-\ln(0.5)\Phi }}{\sqrt {{\frac {1}{{\text{SNR}}_{1}}}+{\frac {1}{{\text{SNR}}_{2}}}}}\quad {\text{[rads]}}$

where SNR1 and SNR2 are the video (base-band) signal-to-noise values for the channels for Antenna 1 and Antenna 2, when square-law detection is used.

In the case of 3-channel processing, an expression which is applicable when the S:N ratios in all three channels exceeds unity (when ln(1 + 1/SNR) ≈ 1/SNR is true in all three channels), is

$\Delta \varphi _{\text{RMS}}={\frac {1}{-2\ln(0.5)}}{\frac {\Psi _{0}^{2}}{\Phi ^{2}}}{\sqrt {\left(\varphi +{\frac {\Phi }{2}}\right)^{2}{\frac {1}{{\text{SNR}}_{2}}}+{\frac {4\varphi ^{2}}{{\text{SNR}}_{1}}}+\left(\varphi -{\frac {\Phi }{2}}\right)^{2}{\frac {1}{{\text{SNR}}_{3}}}}}$

where SNR1, SNR2 and SNR3 are the video signal-to-noise values for Channel 1, Channel 2, and Channel 3 respectively, for the bearing angle φ.

### A typical DF system with six antennas

A schematic of a possible DF system, employing six antennas, is shown in the figure.

The signals received by the antennas are first amplified by a low-noise preamplifier before detection by detector-log-video-amplifiers (DLVAs). The signal levels from the DLVAs are compared to determine the angle of arrival. By considering the signal levels on a logarithmic scale, as provided by the DLVAs, a large dynamic range is achieved and, in addition, the direction finding calculations are simplified when the main lobes of antenna patterns have a Gaussian characteristic, as shown earlier.

A necessary part of the DF analysis is to identify the channel which contains the largest signal and this is achieved by means of a fast comparator circuit. In addition to the DF process, other properties of the signal may be investigated, such as pulse duration, frequency, pulse repetition frequency (PRF) and modulation characteristics. The comparator operation usually includes hysteresis, to avoid jitter in the selection process when the bearing of the incoming signal is such that two adjacent channels contain signals of similar amplitude.

Often, the wideband amplifiers are protected from local high power sources (as on a ship) by input limiters and/or filters. Similarly the amplifiers might contain notch filters to remove known, but unwanted, signals which could impairs the system's ability to process weaker signals. Some of these issues are covered in RF chain.
