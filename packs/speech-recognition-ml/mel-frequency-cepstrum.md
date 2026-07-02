---
title: "Mel-frequency cepstrum"
source: https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
domain: speech-recognition-ml
license: CC-BY-SA-4.0
tags: speech recognition, acoustic model, voice transcription, audio features, spoken language
fetched: 2026-07-02
---

# Mel-frequency cepstrum

In sound processing, the **mel-frequency cepstrum** (**MFC**) is a representation of the short-term power spectrum of a sound, based on a linear cosine transform of a log power spectrum on a nonlinear mel scale of frequency.

**Mel-frequency cepstral coefficients** (**MFCCs**) are coefficients that collectively make up an MFC. They are derived from a type of cepstral representation of the audio clip (a nonlinear "spectrum-of-a-spectrum"). The difference between the cepstrum and the mel-frequency cepstrum is that in the MFC, the frequency bands are equally spaced on the mel scale, which approximates the human auditory system's response more closely than the linearly-spaced frequency bands used in the normal spectrum. This frequency warping can allow for better representation of sound, for example, in audio compression that might potentially reduce the transmission bandwidth and the storage requirements of audio signals.

MFCCs are commonly derived as follows:

1. Take the Fourier transform of (a windowed excerpt of) a signal.
2. Map the powers of the spectrum obtained above onto the mel scale, using triangular overlapping windows or alternatively, cosine overlapping windows.
3. Take the logs of the powers at each of the mel frequencies.
4. Take the discrete cosine transform of the list of mel log powers, as if it were a signal.
5. The MFCCs are the amplitudes of the resulting spectrum.

There can be variations on this process, for example: differences in the shape or spacing of the windows used to map the scale, or addition of dynamics features such as "delta" and "delta-delta" (first- and second-order frame-to-frame difference) coefficients.

The European Telecommunications Standards Institute in the early 2000s defined a standardised MFCC algorithm to be used in mobile phones.

## Applications

MFCCs are commonly used as features in speech recognition systems, such as the systems which can automatically recognize numbers spoken into a telephone.

MFCCs are also increasingly finding uses in music information retrieval applications such as genre classification, audio similarity measures, etc.

### MFCC for speaker recognition

Since Mel-frequency bands are distributed evenly in MFCC, and they are very similar to the voice system of a human, MFCC can efficiently be used to characterize speakers. For instance, it can be used to recognize the speaker's cell phone model characteristics, and further the details of the speaker's voice.

This type of mobile device recognition is possible because the production of electronic components in a phone have tolerances, because different electronic circuit realizations do not have exact same transfer functions. The dissimilarities in the transfer function from one realization to another becomes more prominent if the task performing circuits are from different manufacturers. Hence, each cell phone introduces a convolutional distortion on input speech that leaves its unique impact on the recordings from the cell phone. Therefore, a particular phone can be identified from the recorded speech by multiplying the original frequency spectrum with further multiplications of transfer functions specific to each phone followed by signal processing techniques. Thus, by using MFCC one can characterize cell phone recordings to identify the brand and model of the phone.

Considering recording section of a cellphone as Linear time-invariant (LTI) filter:

Impulse response- *h(n)*, recorded speech signal *y(n)* as output of filter in response to input *x(n).*

Hence, $y(n)=x(n)*h(n)$ (convolution)

As speech is not stationary signal, it is divided into overlapped frames within which the signal is assumed to be stationary. So, the $p^{th}$ short-term segment (frame) of recorded input speech is:

$y_{p}w(n)=[x(n)w(pW-n)]*h(n)$

,

where *w(n)*: windowed function of length W.

Hence, as specified the footprint of mobile phone of the recorded speech is the convolution distortion that helps to identify the recording phone.

The embedded identity of the cell phone requires a conversion to a better identifiable form, hence, taking short-time Fourier transform:

$Y_{p}w(f)=X_{p}w(f)H(f)$

$H(f)$ can be considered as a concatenated transfer function that produced input speech, and the recorded speech $Y_{p}w(f)$ can be perceived as original speech from cell phone.

So, equivalent transfer function of vocal tract and cell phone recorder is considered as original source of recorded speech. Therefore,

$X_{p}w(f)=Xe_{p}w(f)X_{v}(f),H'(f)=H(f)X_{v}(f),$

where *Xew(f)* is the excitation function, $X_{v}(f)$ is the vocal tract transfer function for speech in the $p^{th}$ frame and $H'(f)$ is the equivalent transfer function that characterizes the cell phone.

$Y_{p}w(f)=Xe_{p}w(f)H'(f)$

This approach can be useful for speaker recognition as the device identification and the speaker identification are very much connected.

Providing importance to the envelope of the spectrum which multiplied by filter bank (suitable cepstrum with mel-scale filter bank), after smoothing filter bank with transfer function U(f), the log operation on output energies are:

$\log[|Y_{p}w(f)|]=\log[|U(f)||Xe_{p}w(f)||H'(f)|]$

Representing $H_{w}(f)=U(f)H'(f)$

$\log[|Y_{p}w(f)|]=\log[|Xe_{p}w(f)|]+\log[|H_{w}(f)|]$

MFCC is successful because of this nonlinear transformation with additive property.

Transforming back to time domain:

$c_{y}(j)=c_{e}(j)+c_{w}(j)$

where, cy(j), ce(j), cw(j) are the recorded speech cepstrum and weighted equivalent impulse response of cell phone recorder that characterizes the cell phone, respectively, while j is the number of filters in the filter bank.

More precisely, the device specific information is in the recorded speech which is converted to additive form suitable for identification.

cy(j) can be further processed for identification of the recording phone.

Often used frame lengths- 20 or 20 ms.

Commonly used window functions- Hamming and Hanning windows.

Hence, Mel-scale is a commonly used frequency scale that is linear till 1000 Hz and logarithmic above it.

Computation of central frequencies of filters in Mel-scale:

$f_{mel}=1000\log(1+f/1000)/\log 2$

, base 10.

Basic procedure for MFCC calculation:

1. Logarithmic filter bank outputs are produced and multiplied by 20 to obtain spectral envelopes in decibels.
2. MFCCs are obtained by taking Discrete Cosine Transform (DCT) of the spectral envelope.
3. Cepstrum coefficients are obtained as:

$c_{i}=\sum _{n=1}^{N_{f}}S_{n}\cos \left(i(n-0.5)\left({\frac {\pi }{N_{f}}}\right)\right)$ , $i=1,\dots ,L$ ,

where $c_{i}=c_{y}(i)$ corresponds to the i -th MFCC coefficient, $N_{f}$ is the number of triangular filters in the filter bank, $S_{n}$ is the log energy output of n -th filter coefficient, and L is the number of MFCC coefficients that we want to calculate.

## Inversion

An MFCC can be approximately inverted to audio in four steps: (a1) inverse DCT to obtain a mel log-power [dB] spectrogram, (a2) mapping to power to obtain a mel power spectrogram, (b1) rescaling to obtain short-time Fourier transform magnitudes, and finally (b2) phase reconstruction and audio synthesis using Griffin-Lim. Each step corresponds to one step in MFCC calculation.

## Noise sensitivity

MFCC values are not very robust in the presence of additive noise, and so it is common to normalise their values in speech recognition systems to lessen the influence of noise. Some researchers propose modifications to the basic MFCC algorithm to improve robustness, such as by raising the log-mel-amplitudes to a suitable power (around 2 or 3) before taking the discrete cosine transform (DCT), which reduces the influence of low-energy components.

## History

Paul Mermelstein is typically credited with the development of the MFC. Mermelstein credits Bridle and Brown for the idea:

> Bridle and Brown used a set of 19 weighted spectrum-shape coefficients given by the cosine transform of the outputs of a set of nonuniformly spaced bandpass filters. The filter spacing is chosen to be logarithmic above 1 kHz and the filter bandwidths are increased there as well. We will, therefore, call these the mel-based cepstral parameters.

Sometimes both early originators are cited.

Many authors, including Davis and Mermelstein, have commented that the spectral basis functions of the cosine transform in the MFC are very similar to the principal components of the log spectra, which were applied to speech representation and recognition much earlier by Pols and his colleagues.
