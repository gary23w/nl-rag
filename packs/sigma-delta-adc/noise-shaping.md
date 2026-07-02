---
title: "Noise shaping"
source: https://en.wikipedia.org/wiki/Noise_shaping
domain: sigma-delta-adc
license: CC-BY-SA-4.0
tags: delta-sigma modulation, noise shaping, oversampling ratio, decimation filter
fetched: 2026-07-02
---

# Noise shaping

**Noise shaping** is a technique typically used in digital audio, image, and video processing, usually in combination with dithering, as part of the process of quantization or bit-depth reduction of a signal. Its purpose is to increase the apparent signal-to-noise ratio of the resultant signal. It does this by altering the spectral shape of the error that is introduced by dithering and quantization, such that the noise power is at a lower level in frequency bands at which noise is considered to be less desirable and at a correspondingly higher level in bands where it is considered to be more desirable. A popular noise shaping algorithm used in image processing is known as ‘Floyd Steinberg dithering’; and many noise shaping algorithms used in audio processing are based on an ‘Absolute threshold of hearing’ model.

## Operation

Any feedback loop functions as a filter. Noise shaping works by putting quantization noise in a feedback loop designed to filter the noise as desired.

### Low-pass boxcar filter example

For example, consider the feedback system:

$y[n]=x[n]+b\cdot e[n-1],$

where b is a constant, n is the cycle number, *x*[*n*] is the input sample value, *y*[*n*] is the value being quantized, and *e*[*n*] is its quantization error:

$\ e[n]=y_{\text{quantized}}[n]-y[n].$

In this model, when any sample's bit depth is reduced, the quantization error is measured and on the next cycle added with the next sample prior to quantization. The effect is that the quantization error is low-pass filtered by a 2-sample boxcar filter (also known as a simple moving average filter). As a result, compared to before, the quantization error has lower power at higher frequencies and higher power at lower frequencies. The filter's cutoff frequency can be adjusted by modifying b, the proportion of error from the previous sample that is fed back.

### Impulse response filters in general

More generally, any FIR filter or IIR filter can be used to create a more complex frequency response curve. Such filters can be designed using the weighted least squares method. In the case of digital audio, typically the weighting function used is one divided by the absolute threshold of hearing curve, i.e.

$\ W(f)={\frac {1}{A(f)}}.$

### Dithering

Adding an appropriate amount of dither during quantization prevents determinable errors correlated to the signal. If dither is not used, then noise shaping effectively functions merely as distortion shaping — pushing the distortion energy around to different frequency bands, but it is still distortion. If dither is added to the process as

$\ y[n]=x[n]+b\cdot e[n-1]+\mathrm {dither} ,$

then the quantization error truly becomes noise, and the process indeed yields noise shaping.

## In digital audio

- (750 Hz sinusoidal tone sampled at 48 kHz and quantized to 4 bits with no dithering and no noise shaping. This process introduces periodic rounding error with period 64 samples, seen in the frequency domain as harmonics which reach as high as −40 dB with respect to the reference tone.)750 Hz sinusoidal tone sampled at 48 kHz and quantized to 4 bits with no dithering and no noise shaping. This process introduces periodic rounding error with period 64 samples, seen in the frequency domain as harmonics which reach as high as −40 dB with respect to the reference tone.
- (The same pure tone with triangular dither but no noise shaping. Note that the overall noise power has increased, but no frequencies reach higher than −60 dB.)The same pure tone with triangular dither but no noise shaping. Note that the overall noise power has increased, but no frequencies reach higher than −60 dB.
- (The same pure tone with triangular dither and noise shaping. Note that the noise is lowest (−80 dB) around 4 kHz, where the ear is the most sensitive.)The same pure tone with triangular dither and noise shaping. Note that the noise is lowest (−80 dB) around 4 kHz, where the ear is the most sensitive.

Noise shaping in audio is most commonly applied as a bit-reduction scheme. The most basic form of dither is flat, white noise. The ear, however, is less sensitive to certain frequencies than others at low levels (see Equal-loudness contour). By using noise shaping, the quantization error can be effectively spread around so that more of it is focused on frequencies that can't be heard as well and less of it is focused on frequencies that can. The result is that where the ear is most critical, the quantization error can be reduced greatly and where the ear is less sensitive, the noise is much greater. This can give a perceived noise reduction of 4 bits compared to straight dither. So, although 16-bit samples only have 96 dB of dynamic range across the entire spectrum (see quantization distortion calculations), noise-shaped dithering can, however, increase the perceived audio dynamic range to 120 dB.

### Noise shaping and 1-bit converters

Since around 1989, 1-bit delta-sigma modulators have been used in analog-to-digital converters. This involves sampling the audio at a very high rate (2.8224 million samples per second, for example) but only using a single bit. Because only 1 bit is used, this converter only has 6.02 dB of dynamic range. The noise floor, however, is spread throughout the entire non-aliased frequency range below the Nyquist frequency of 1.4112 MHz. Noise shaping is used to lower the noise present in the audible range (20 Hz to 20 kHz) and increase the noise above the audible range. This results in a broadband dynamic range of only 7.78 dB, but it is not consistent among frequency bands, and in the lowest frequencies (the audible range) the dynamic range is much greater — over 100 dB. Noise shaping is inherently built into the delta-sigma modulators.

The 1-bit converter is the basis of the DSD format by Sony. One criticism of the 1-bit converter (and thus the DSD system) is that because only 1 bit is used in both the signal and the feedback loop, adequate amounts of dither cannot be used in the feedback loop and distortion can be heard under some conditions (more discussion at Direct Stream Digital § DSD vs. PCM).

Most A/D converters made since 2000 use multi-bit or multi-level delta-sigma modulators that yield more than 1 bit output so that proper dither can be added in the feedback loop. For traditional PCM sampling the signal is then decimated to 44.1 kHz or other appropriate sample rates.

### In modern ADCs

Analog Devices uses what they refer to as "Noise Shaping Requantizer", and Texas Instruments uses what they refer to as "SNRBoost" to lower the noise floor approximately 30db compared to the surrounding frequencies. This comes at a cost of non-continuous operation but produces a nice bathtub shape to the spectrum floor. This can be combined with other techniques to further enhance the resolution of the spectrum.
