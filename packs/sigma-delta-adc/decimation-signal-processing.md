---
title: "Downsampling (signal processing)"
source: https://en.wikipedia.org/wiki/Decimation_(signal_processing)
domain: sigma-delta-adc
license: CC-BY-SA-4.0
tags: delta-sigma modulation, noise shaping, oversampling ratio, decimation filter
fetched: 2026-07-02
---

# Downsampling (signal processing)

(Redirected from

Decimation (signal processing)

)

In digital signal processing, **downsampling**, **subsampling**, **compression**, and **decimation** are terms associated with the process of *resampling* in a multi-rate digital signal processing system. Both *downsampling* and *decimation* can be synonymous with *compression*, or they can describe an entire process of bandwidth reduction (filtering) and sample-rate reduction. When the process is performed on a sequence of samples of a *signal* or a continuous function, it produces an approximation of the sequence that would have been obtained by sampling the signal at a lower rate (or density, as in the case of a photograph).

*Decimation* is a term that historically means the *removal of every tenth one*. But in signal processing, *decimation by a factor of 10* actually means *keeping* only every tenth sample. This factor multiplies the sampling interval or, equivalently, divides the sampling rate. For example, if compact disc audio at 44,100 samples/second is *decimated* by a factor of 5/4, the resulting sample rate is 35,280. A system component that performs decimation is called a *decimator*. Decimation by an integer factor is also called *compression*.

## Downsampling by an integer factor

Rate reduction by an integer factor *M* can be explained as a two-step process, with an equivalent implementation that is more efficient:

1. Reduce high-frequency signal components with a digital lowpass filter.
2. *Decimate* the filtered signal by *M*; that is, keep only every *M*th sample.

Step 2 alone creates undesirable aliasing (i.e. high-frequency signal components will copy into the lower frequency band and be mistaken for lower frequencies). Step 1, when necessary, suppresses aliasing to an acceptable level. In this application, the filter is called an anti-aliasing filter, and its design is discussed below. Also see undersampling for information about decimating bandpass functions and signals.

When the anti-aliasing filter is an IIR design, it relies on feedback from output to input, prior to the second step. With FIR filtering, it is an easy matter to compute only every *M*th output. The calculation performed by a decimating FIR filter for the *n*th output sample is a dot product:

$y[n]=\sum _{k=0}^{K-1}x[nM-k]\cdot h[k],$

where the *h*[•] sequence is the impulse response, and *K* is its length. *x*[•] represents the input sequence being downsampled. In a general purpose processor, after computing *y*[*n*], the easiest way to compute *y*[*n*+1] is to advance the starting index in the *x*[•] array by *M*, and recompute the dot product. In the case *M*=2, *h*[•] can be designed as a half-band filter, where almost half of the coefficients are zero and need not be included in the dot products.

Impulse response coefficients taken at intervals of *M* form a subsequence, and there are *M* such subsequences (phases) multiplexed together. The dot product is the sum of the dot products of each subsequence with the corresponding samples of the *x*[•] sequence. Furthermore, because of downsampling by *M*, the stream of *x*[•] samples involved in any one of the *M* dot products is never involved in the other dot products. Thus *M* low-order FIR filters are each filtering one of *M* multiplexed *phases* of the input stream, and the *M* outputs are being summed. This viewpoint offers a different implementation that might be advantageous in a multi-processor architecture. In other words, the input stream is demultiplexed and sent through a bank of M filters whose outputs are summed. When implemented that way, it is called a **polyphase** filter.

For completeness, we now mention that a possible, but unlikely, implementation of each phase is to replace the coefficients of the other phases with zeros in a copy of the *h*[•] array, process the original *x*[•] sequence at the input rate (which means multiplying by zeros), and decimate the output by a factor of *M*. The equivalence of this inefficient method and the implementation described above is known as the *first Noble identity*. It is sometimes used in derivations of the polyphase method.

### Anti-aliasing filter

Let *X*(*f*) be the Fourier transform of any function, *x*(*t*), whose samples at some interval, *T*, equal the *x*[*n*] sequence. Then the discrete-time Fourier transform (DTFT) is a Fourier series representation of a periodic summation of *X*(*f*):

$\underbrace {\sum _{n=-\infty }^{\infty }\overbrace {x(nT)} ^{x[n]}\ \mathrm {e} ^{-\mathrm {i} 2\pi fnT}} _{\text{DTFT}}={\frac {1}{T}}\sum _{k=-\infty }^{\infty }X{\Bigl (}f-{\frac {k}{T}}{\Bigr )}.$

When *T* has units of seconds, f has units of hertz. Replacing *T* with *MT* in the formulas above gives the DTFT of the decimated sequence, *x*[*nM*]:

$\sum _{n=-\infty }^{\infty }x(n\cdot MT)\ \mathrm {e} ^{-\mathrm {i} 2\pi fn(MT)}={\frac {1}{MT}}\sum _{k=-\infty }^{\infty }X\left(f-{\tfrac {k}{MT}}\right).$

The periodic summation has been reduced in amplitude and periodicity by a factor of *M*. An example of both these distributions is depicted in the two traces of Fig 1. Aliasing occurs when adjacent copies of *X*(*f*) overlap. The purpose of the anti-aliasing filter is to ensure that the reduced periodicity does not create overlap. The condition that ensures the copies of *X*(*f*) do not overlap each other is: $B<{\tfrac {0.5}{T}}\cdot {\tfrac {1}{M}},$ so that is the maximum cutoff frequency of an *ideal* anti-aliasing filter.

## By a rational factor

Let *M/L* denote the decimation factor, where: M, L ∈ $\mathbb {Z}$ ; M > L.

1. Increase (resample) the sequence by a factor of *L*. This is called Upsampling, or *interpolation*.
2. Decimate by a factor of *M*

Step 1 requires a lowpass filter after increasing (*expanding*) the data rate, and step 2 requires a lowpass filter before decimation. Therefore, both operations can be accomplished by a single filter with the lower of the two cutoff frequencies. For the *M* > *L* case, the anti-aliasing filter cutoff,  ${\tfrac {0.5}{M}}$ *cycles per intermediate sample*, is the lower frequency.
