---
title: "Audio bit depth"
source: https://en.wikipedia.org/wiki/Audio_bit_depth
domain: flac-lossless
license: CC-BY-SA-4.0
tags: flac lossless, linear predictive coding audio, rice coding, lossless audio
fetched: 2026-07-02
---

# Audio bit depth

In digital audio using pulse-code modulation (PCM), **bit depth** is the number of bits of information in each sample, and it directly corresponds to the **resolution** of each sample. Examples of bit depth include CD-DA and DVD-Video, which uses 16 bits per sample, and DVD-Audio and Blu-ray Disc, which can support up to 24 bits per sample.

In basic implementations, variations in bit depth primarily affect the noise level from quantization error—thus the signal-to-noise ratio (SNR) and dynamic range. However, techniques such as dithering, noise shaping, and oversampling can mitigate these effects without changing the bit depth. Bit depth also affects bit rate and file size.

Bit depth is useful for describing PCM digital signals. Non-PCM formats, such as those using lossy compression, do not have associated bit depths.

## Binary representation

A PCM signal is a sequence of digital audio samples containing the data providing the necessary information to reconstruct the original analog signal. Each sample represents the amplitude of the signal at a specific point in time, and the samples are uniformly spaced in time. The amplitude is the only information explicitly stored in the sample, and it is typically stored as either an integer or a floating-point number, encoded as a binary number with a fixed number of digits – the sample's *bit depth*, also referred to as word length or word size.

The resolution indicates the number of discrete values that can be represented over the range of analog values. The resolution of binary integers increases exponentially as the word length increases: adding one bit doubles the resolution, adding two quadruples it, and so on. The number of possible values that an integer bit depth can represent can be calculated by using 2*n*, where *n* is the bit depth. Thus, a 16-bit system has a resolution of 65,536 (216) possible values.

Integer PCM audio data is typically stored as signed numbers in two's complement format.

Today, most audio file formats and digital audio workstations (DAWs) also support PCM formats with samples represented by floating-point numbers. Both the WAV file format and the AIFF file format support floating-point representations. Unlike integers, whose bit pattern is a single series of bits, a floating-point number is instead composed of separate fields whose mathematical relation forms a number. The most common standard is IEEE 754, which is composed of three fields: a sign bit representing whether the number is positive or negative, a mantissa, and an exponent determining a power-of-two factor to scale the mantissa. The mantissa is expressed as a binary fraction in IEEE base-two floating-point formats.

## Quantization

The bit depth limits the signal-to-noise ratio (SNR) of the reconstructed signal to a maximum level determined by quantization error. The bit depth has no impact on the frequency response, which is constrained by the sample rate.

Quantization error introduced during analog-to-digital conversion (ADC) can be modeled as quantization noise. It is a rounding error between the analog input voltage to the ADC and the output digitized value. The noise is nonlinear and signal-dependent.

In an ideal ADC, where the quantization error is uniformly distributed between $\scriptstyle {\pm {\frac {1}{2}}}$ least significant bit (LSB) and where the signal has a uniform distribution covering all quantization levels, the signal-to-quantization-noise ratio (SQNR) can be calculated from

${\text{SQNR}}=20\log _{10}({\sqrt {1.5}}\cdot 2^{b})\approx (1.76+6.02\,b)\ {\text{dB}},$

where *b* is the number of quantization bits, and the result is measured in decibels (dB).

Therefore, 16-bit digital audio found on CDs has a theoretical maximum SNR of 98 dB, and professional 24-bit digital audio tops out as 146 dB. As of 2011, digital audio converter technology is limited to an SNR of about 123 dB (effectively 21 bits) because of real-world limitations in integrated circuit design. Still, this approximately matches the performance of the human auditory system. Multiple converters can be used to cover different ranges of the same signal, being combined to record a wider dynamic range in the long-term, while still being limited by the single converter's dynamic range in the short term, which is called *dynamic range extension*.

| # bits | SNR (audio) | SNR (video) | Minimum dB step difference (quantization rounding error) | No. of possible values (per sample) | Range (per sample) for signed representation |
|---|---|---|---|---|---|
| 4 | 25.84 dB | 34.31 dB | 1.723 dB | 16 | −8 to +7 |
| 8 | 49.93 dB | 58.92 dB | 0.1958 dB | 256 | −128 to +127 |
| 11 | 67.99 dB | 77.01 dB | 0.03321 dB | 2,048 | −1,024 to +1,023 |
| 12 | 74.01 dB | 83.04 dB | 0.01807 dB | 4,096 | −2,048 to +2,047 |
| 16 | 98.09 dB | 107.12 dB | 0.001497 dB | 65,536 | −32,768 to +32,767 |
| 18 | 110.13 dB |   | 0.0004201 dB | 262,144 | −131,072 to +131,071 |
| 20 | 122.17 dB |   | 0.0001165 dB | 1,048,576 | −524,288 to +524,287 |
| 24 | 146.26 dB |   | 0.000008717 dB | 16,777,216 | −8,388,608 to +8,388,607 |
| 32 | 194.42 dB |   | 4.52669593×10−8 dB | 4,294,967,296 | −2,147,483,648 to +2,147,483,647 |
| 48 | 290.75 dB |   | 1.03295047×10−12 dB | 281,474,976,710,656 | −140,737,488,355,328 to +140,737,488,355,327 |
| 64 | 387.08 dB |   | 2.09836113×10−17 dB | 18,446,744,073,709,551,616 | −9,223,372,036,854,775,808 to +9,223,372,036,854,775,807 |

## Floating point

The resolution of floating-point samples is less straightforward than integer samples because floating-point values are not evenly spaced. In floating-point representation, the space between any two adjacent values is in proportion to the value.

The trade-off between floating-point and integer formats is that the space between large floating-point values is greater than the space between large integer values of the same bit depth. Rounding a large floating-point number results in a greater error than rounding a small floating-point number whereas rounding an integer number will always result in the same level of error. In other words, integers have a round-off that is uniform, always rounding the LSB to 0 or 1, and the floating-point format has uniform SNR, the quantization noise level is always of a certain proportion to the signal level. A floating-point noise floor rises as the signal rises and falls as the signal falls, resulting in audible variance if the bit depth is low enough.

## Audio processing

Most processing operations on digital audio involve the re-quantization of samples and thus introduce additional rounding errors analogous to the original quantization error introduced during analog-to-digital conversion. To prevent rounding errors larger than the implicit error during ADC, calculations during processing must be performed at higher precisions than the input samples.

Digital signal processing (DSP) operations can be performed in either fixed-point or floating-point precision. In either case, the precision of each operation is determined by the precision of the hardware operations used to perform each step of the processing and not the resolution of the input data. For example, on x86 processors, floating-point operations are performed with single or double precision, and fixed-point operations at 16-, 32- or 64-bit resolution. Consequently, all processing performed on Intel-based hardware will be performed with these constraints regardless of the source format.

Fixed-point digital signal processors often supports specific word lengths to support specific signal resolutions. For example, the Motorola 56000 DSP chip uses 24-bit multipliers and 56-bit accumulators to perform multiply-accumulate operations on two 24-bit samples without overflow or truncation. On devices that do not support large accumulators, fixed-point results may be truncated, reducing precision. Errors compound through multiple stages of DSP at a rate that depends on the operations being performed. For uncorrelated processing steps on audio data without a DC offset, errors are assumed to be random with zero means. Under this assumption, the standard deviation of the distribution represents the error signal, and quantization error scales with the square root of the number of operations. High levels of precision are necessary for algorithms that involve repeated processing, such as convolution. High levels of precision are also necessary in recursive algorithms, such as infinite impulse response (IIR) filters. In the particular case of IIR filters, rounding error can degrade frequency response and cause instability.

## Dither

The noise introduced by quantization error, including rounding errors and loss of precision introduced during audio processing, can be mitigated by adding a small amount of random noise, called dither, to the signal before quantizing. Dithering eliminates non-linear quantization error behavior, giving very low distortion, but at the expense of a slightly raised noise floor. Recommended dither for 16-bit digital audio measured using ITU-R 468 noise weighting is about 66 dB below alignment level, or 84 dB below digital full scale, which is comparable to the microphone and room noise level, and hence of little consequence in 16-bit audio.

24-bit and 32-bit audio does not require dithering, as the noise level of the digital converter is always louder than the required level of any dither that might be applied. 24-bit audio could theoretically encode 144 dB of dynamic range, and 32-bit audio can achieve 192 dB, but this is almost impossible to achieve in the real world, as even the best sensors and microphones rarely exceed 130 dB.

Dither can also be used to increase the effective dynamic range. The *perceived* dynamic range of 16-bit audio can be 120 dB or more with noise-shaped dither, taking advantage of the frequency response of the human ear.

## Dynamic range and headroom

Dynamic range is the difference between the largest and smallest signal a system can record or reproduce. Without dither, the dynamic range correlates to the quantization noise floor. For example, 16-bit integer resolution allows for a dynamic range of about 96 dB. With the proper application of dither, digital systems can reproduce signals with levels lower than their resolution would normally allow, extending the effective dynamic range beyond the limit imposed by the resolution. The use of techniques such as oversampling and noise shaping can further extend the dynamic range of sampled audio by moving quantization error out of the frequency band of interest.

If the signal's maximum level is lower than that allowed by the bit depth, the recording has headroom. Using higher bit depths during studio recording can make headroom available while maintaining the same dynamic range. This reduces the risk of clipping without increasing quantization errors at low volumes.

### Oversampling

Oversampling is an alternative method to increase the dynamic range of PCM audio without changing the number of bits per sample. In oversampling, audio samples are acquired at a multiple of the desired sample rate. Because quantization error is assumed to be uniformly distributed with frequency, much of the quantization error is shifted to ultrasonic frequencies and can be removed by the digital-to-analog converter during playback.

For an increase equivalent to *n* additional bits of resolution, a signal must be oversampled by

$\mathrm {number\ of\ samples} =(2^{n})^{2}=2^{2n}.$

For example, a 14-bit ADC can produce 16-bit 48 kHz audio if operated at 16× oversampling, or 768 kHz. Oversampled PCM, therefore, exchanges fewer bits per sample for more samples to obtain the same resolution.

Dynamic range can also be enhanced with oversampling at signal reconstruction, absent oversampling at the source. Consider 16× oversampling at reconstruction. Each sample at reconstruction would be unique in that for each of the original sample points, sixteen are inserted, all having been calculated by a digital reconstruction filter. The mechanism of increased effective bit depth is as previously discussed, that is, quantization noise power has not been reduced, but the noise spectrum has been spread over 16× the audio bandwidth.

Historical note—The compact disc standard was developed by a collaboration between Sony and Philips. The first Sony consumer unit featured a 16-bit DAC; the first Philips units had dual 14-bit DACs. This confused the marketplace and even in professional circles, because 14-bit PCM allows for 84 dB SNR, 12 dB less than 16-bit PCM. Philips had implemented 4× oversampling with first order noise shaping which theoretically realized the full 96 dB dynamic range of the CD format. In practice the Philips CD100 was rated at 90 dB SNR in the audio band of 20 Hz–20 kHz, the same as Sony's CDP-101.

### Noise shaping

Oversampling a signal results in equal quantization noise per unit of bandwidth at all frequencies and a dynamic range that improves with only the square root of the oversampling ratio. Noise shaping is a technique that adds additional noise at higher frequencies, which cancels out some error at lower frequencies, resulting in a larger increase in dynamic range when oversampling. For *n*th-order noise shaping, the dynamic range of an oversampled signal is improved by an additional 6*n* dB relative to oversampling without noise shaping. For example, for a 20 kHz analog audio sampled at 4× oversampling with second-order noise shaping, the dynamic range is increased by 30 dB. Therefore, a 16-bit signal sampled at 176 kHz would have a bit depth equal to a 21-bit signal sampled at 44.1 kHz without noise shaping.

Noise shaping is commonly implemented with delta-sigma modulation. Using delta-sigma modulation, Direct Stream Digital achieves a theoretical 120 dB SNR at audio frequencies using 1-bit audio with 64× oversampling.

## Applications

Bit depth is a fundamental property of digital audio implementations. Depending on application requirements and equipment capabilities, different bit depths are used for different applications.

| Application | Description | Audio format(s) |
|---|---|---|
| CD-DA (Red Book) | Digital media | 16-bit LPCM |
| DVD-Video (Audio track) | Digital media | 16-bit LPCM |
| DVD-Audio | Digital media | 16-, 20- and 24-bit LPCM |
| Super Audio CD | Digital media | 1-bit Direct Stream Digital (PDM) |
| Blu-ray Disc audio | Digital media | 16-, 20- and 24-bit LPCM and others |
| DV audio | Digital media | 12- and 16-bit uncompressed PCM |
| ITU-T Recommendation G.711 | Compression standard for telephony | 8-bit PCM with companding |
| NICAM-1, NICAM-2 and NICAM-3 | Compression standards for broadcasting | 10-, 11- and 10-bit PCM respectively, with companding |
| Ardour | DAW by Paul Davis and the Ardour Community | 32-bit floating point |
| Pro Tools 11 | DAW by Avid Technology | 16- and 24-bit or 32-bit floating point sessions and 64-bit floating point mixing |
| Logic Pro X | DAW by Apple Inc. | 16- and 24-bit projects and 32-bit or 64-bit floating point mixing |
| Cubase | DAW by Steinberg | Allows audio processing precision to 32-bit float or 64-bit float |
| Ableton Live | DAW by Ableton | 32-bit floating point bit depth and 64-bit summing |
| Reason 7 | DAW by Propellerhead Software | 16-, 20- and 24-bit I/O, 32-bit floating point arithmetic and 64-bit summing |
| Reaper 5 | DAW by Cockos Inc. | 8-bit PCM, 16-bit PCM, 24-bit PCM, 32-bit PCM, 32-bit FP, 64-bit FP, 4-bit IMA ADPCM & 2-bit cADPCM rendering; 8-bit int, 16-bit int, 24-bit int, 32-bit int, 32-bit float, and 64-bit float mixing |
| GarageBand '11 (version 6) | DAW by Apple Inc. | 16-bit default with 24-bit real instrument recording |
| Audacity | Open source audio editor | 16- and 24-bit LPCM and 32-bit floating point |
| FL Studio | DAW by Image-Line | 16- and 24-bit int and 32-bit floating point (controlled by OS) |
| Android (Smartphone) | Digital device | Typically 16-bit LPCM |
| Android (Smart TV) | Digital device | Typically 24-bit LPCM |
| Windows (PC) | Digital device | Typically 24-bit LPCM since Windows Vista |

1. DVD-Audio also supports optional Meridian Lossless Packing, a lossless compression scheme.
2. Blu-ray supports a variety of non-LPCM formats but all conform to some combination of 16, 20, or 24 bits per sample.
3. ITU-T specifies the A-law and μ-law companding algorithms, compressing down from 13 and 14 bits respectively.
4. NICAM systems 1, 2 and 3 compress down from 13, 14 and 14 bits respectively.

## Bit rate and file size

Bit depth affects bit rate and file size. Bits are the basic unit of data used in computing and digital communications. Bit rate refers to the amount of data, specifically bits, transmitted or received per second. In MP3 and other lossy compressed audio formats, bit rate describes the amount of information used to encode an audio signal. It is usually measured in kb/s.
