---
title: "Direct digital synthesis"
source: https://en.wikipedia.org/wiki/Direct_digital_synthesis
domain: frequency-synthesizer
license: CC-BY-SA-4.0
tags: frequency synthesizer, direct digital synthesis, fractional-N synthesizer, numerically controlled oscillator
fetched: 2026-07-02
---

# Direct digital synthesis

**Direct digital synthesis** (**DDS**) is a method employed by frequency synthesizers to create arbitrary waveforms from a single, fixed-frequency reference clock. DDS is used in applications such as signal generation, local oscillators in communication systems, function generators, mixers, modulators, sound synthesizers and as part of a digital phase-locked loop.

## Overview

A basic Direct Digital Synthesizer consists of a frequency reference (often a crystal or SAW oscillator), a numerically controlled oscillator (NCO) and a digital-to-analog converter (DAC) as shown in Figure 1.

The reference oscillator provides a stable time base for the system and determines the frequency accuracy of the DDS. It provides the clock to the *NCO*, which produces at its output a discrete-time, quantized version of the desired output waveform (often a sinusoid) whose period is controlled by the digital word contained in the *Frequency Control Register*. The sampled, digital waveform is converted to an analog waveform by the *DAC*. The output reconstruction filter rejects the spectral replicas produced by the zero-order hold inherent in the analog conversion process.

## Performance

A DDS has many advantages over its analog counterpart, the phase-locked loop (PLL), including much better frequency agility, improved phase noise, and precise control of the output phase across frequency switching transitions. Disadvantages include spurious responses mainly due to truncation effects in the NCO, crossing spurs resulting from high order (>1) Nyquist images, and a higher noise floor at large frequency offsets due mainly to the digital-to-analog converter.

Because a DDS is a sampled system, in addition to the desired waveform at output frequency Fout, Nyquist images are also generated (the primary image is at Fclk − Fout, where Fclk is the reference clock frequency). In order to reject these undesired images, a DDS is generally used in conjunction with an analog reconstruction lowpass filter as shown in Figure 1.

### Frequency agility

The output frequency of a DDS is determined by the value stored in the frequency control register (FCR) (see Fig.1), which in turn controls the NCO's phase accumulator step size. Because the NCO operates in the discrete-time domain, it changes frequency instantaneously at the clock edge coincident with a change in the value stored in the FCR. The DDS output frequency settling time is determined mainly by the phase response of the reconstruction filter. An ideal reconstruction filter with a linear phase response (meaning the output is simply a delayed version of the input signal) would allow instantaneous frequency response at its output because a linear system can not create frequencies not present at its input.

### Phase noise and jitter

The superior close-in phase noise performance of a DDS stems from the fact that it is a feed-forward system. In a traditional phase locked loop (PLL), the frequency divider in the feedback path acts to multiply the phase noise of the reference oscillator and, within the PLL loop bandwidth, impresses this excess noise onto the VCO output. A DDS, on the other hand, reduces the reference clock phase noise by the ratio $f_{clk}/f_{o}$ because the fractional division of the clock derives its output. Reference clock jitter translates directly to the output, but this jitter is a smaller percentage of the output period (by the ratio above). Since the maximum output frequency is limited to $f_{clk}/2$ , the output phase noise at close-in offsets is always at least 6 dB below the reference clock phase noise.

At offsets far removed from the carrier, the phase-noise floor of a DDS is determined by the power sum of the DAC quantization noise floor and the reference clock phase noise floor.
