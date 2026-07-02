---
title: "Common-mode rejection ratio"
source: https://en.wikipedia.org/wiki/Common-mode_rejection_ratio
domain: differential-pair
license: CC-BY-SA-4.0
tags: long-tailed pair, differential amplifier, emitter-coupled logic, common-mode rejection ratio
fetched: 2026-07-02
---

# Common-mode rejection ratio

In electronics, the **common mode rejection ratio** (**CMRR**) of a differential amplifier (or other device) is a metric used to quantify the ability of the device to reject common-mode signals, i.e. those that appear simultaneously and in-phase on both inputs. An ideal differential amplifier would have infinite CMRR, however this is not achievable in practice. A high CMRR is required when a differential signal must be amplified in the presence of a possibly large common-mode input, such as strong electromagnetic interference (EMI). An example is audio transmission over balanced line in sound reinforcement or recording.

## CMRR of an amplifier

Ideally, a differential amplifier takes the voltages, $V_{+}$ and $V_{-}$ on its two inputs and produces an output voltage $V_{\mathrm {o} }=A_{\mathrm {d} }(V_{+}-V_{-})$ , where $A_{\mathrm {d} }$ is the differential gain. However, the output of a real differential amplifier is better described as :

$V_{\mathrm {o} }=A_{\mathrm {d} }(V_{+}-V_{-})+A_{\mathrm {cm} }{\tfrac {V_{+}+V_{-}}{2}}$

where $A_{\mathrm {cm} }$ is the "common-mode gain", which is typically much smaller than the differential gain.

The CMRR is defined as the ratio of the powers of the differential gain over the common-mode gain, measured in positive decibels (thus using the 20 log rule):

$\mathrm {CMRR} =\left({\frac {A_{\mathrm {d} }}{|A_{\mathrm {cm} }|}}\right)=10\log _{10}\left({\frac {A_{\mathrm {d} }}{A_{\mathrm {cm} }}}\right)^{2}{\text{dB}}=20\log _{10}\left({\frac {A_{\mathrm {d} }}{|A_{\mathrm {cm} }|}}\right){\text{dB}}$

As differential gain should exceed common-mode gain, this will be a positive number, and the higher the better.

The CMRR is a very important specification, as it indicates how much of the unwanted common-mode signal will appear in the output, typically a measurement of some quantity. The value of the CMRR often depends on signal frequency, and must be specified as a function thereof.

It is often important in reducing noise on transmission lines. For example, when measuring the voltage of a thermocouple in a noisy environment, the electrical noise from the environment appears as an offset on both input leads, making it a common-mode voltage signal. The CMRR of the measurement instrument determines the attenuation applied to the offset or noise.

CMRR is an important feature of operational amplifiers, difference amplifiers and instrumentation amplifiers, and can be found in the datasheet. The CMRR often varies with the frequency of the common-mode signal, and is often much higher at higher gain settings. The key to achieving a high CMRR is usually the use of very precisely matched resistors (better than 0.1%) to minimise any difference in the amplification of the negative and positive sides of the signal. Single-chip instrumentation amplifiers typically have laser-trimmed resistors to achieve a CMRR in excess of 100 dB, sometimes even 130 dB.

## CMRR of a balun

The design of a microwave balun (single-ended to differential conversion circuit) defines the CMRR as the ratio of differential gain to common-mode gain in S-parameters, as follows:

$\mathrm {CMRR} =|{\frac {S_{\mathrm {DS} }}{S_{\mathrm {CS} }}}|=|{\frac {S_{\mathrm {21} }-S_{\mathrm {31} }}{S_{\mathrm {21} }+S_{\mathrm {31} }}}|$

Here, port1 is a single-ended input, and ports 2 and 3 are differential outputs. The CMRR of the balun represents the smallness of the gain and phase error between the differential outputs. If the phase difference between the differential outputs of the balun is close to 180° and the amplitudes are equal, the CMRR will be high.
