---
title: "Effective number of bits"
source: https://en.wikipedia.org/wiki/Effective_number_of_bits
domain: analog-to-digital-conversion
license: CC-BY-SA-4.0
tags: analog-to-digital converter, successive approximation, flash ADC, effective number of bits
fetched: 2026-07-02
---

# Effective number of bits

**Effective number of bits** (**ENOB**) is a measure of the real dynamic range of an analog-to-digital converter (ADC), digital-to-analog converter (DAC), or associated circuitry. Although the resolution of a converter may be specified by the number of bits used to represent the analog value, real circuits, however, are imperfect and introduce additional noise and distortion. Those imperfections reduce the number of bits of accuracy. The ENOB describes the effective resolution of a real converter in terms of the number of bits an ideal converter with the same resolution would have.

ENOB is also used as a quality measure for other blocks such as sample-and-hold amplifiers. Thus, analog blocks may be included in signal-chain calculations. The total ENOB of a chain of blocks is usually less than the ENOB of the worst block.

## Definition

An often used definition for ENOB is

$\mathrm {ENOB} ={\frac {\mathrm {SINAD} -1.76}{6.02}},$

where

- ENOB is given in bits
- SINAD (signal, noise, and distortion) is a power ratio indicating the quality of the signal in dB.
- the 6.02 term in the divisor converts decibels (a log10 representation) to bits (a log2 representation),
- the 1.76 term comes from quantization error in an ideal ADC.

This definition compares the SINAD of an ideal converter of ENOB bits with the SINAD of the converter being tested. The ENOB may be fractional. So while an ADC may use 12 bits, its ENOB may only be 9.5, corresponding to a hypothetical ideal converter with 9.5 bits.

## Effective resolution bandwidth

The frequency band of a signal converter where ENOB is still guaranteed is called the **effective resolution bandwidth** and is limited by dynamic quantization problems. For example, an ADC has some aperture uncertainty. The instant at which a real ADC takes a sample of its input varies from sample to sample. Because the input signal changes, that time variation translates to an output variation. For example, an ADC may sample 1 ns late. If the input signal is a 1 V sinewave at 1,000,000 radians/second (roughly 160 kHz), the input voltage may change by as much as 1 MV/s. A sampling time error of 1 ns would cause a sampling error of about 1 mV (an error in the 10th bit). If the frequency were 100 times faster (about 16 MHz), then the maximum error would be 100 times greater: about 100 mV on a 1 V signal (an error in the third or fourth bit).
