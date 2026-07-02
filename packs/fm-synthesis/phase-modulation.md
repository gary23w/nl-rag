---
title: "Phase modulation"
source: https://en.wikipedia.org/wiki/Phase_modulation
domain: fm-synthesis
license: CC-BY-SA-4.0
tags: fm synthesis, frequency modulation synthesis, phase modulation synthesis, fm operator synthesis
fetched: 2026-07-02
---

# Phase modulation

**Phase modulation** (**PM**) is a signal modulation method for conditioning communication signals for transmission. It encodes a message signal as variations in the instantaneous phase of a carrier wave. Phase modulation is one of the two principal forms of angle modulation, together with frequency modulation.

In phase modulation, the instantaneous amplitude of the baseband signal modifies the phase of the carrier signal keeping its amplitude and frequency constant. The phase of a carrier signal is modulated to follow the changing signal level (amplitude) of the message signal. The peak amplitude and the frequency of the carrier signal are maintained constant, but as the amplitude of the message signal changes, the phase of the carrier changes correspondingly.

Phase modulation is an integral part of many digital transmission coding schemes that underlie a wide range of technologies like Wi-Fi, GSM and satellite television. However, it is not widely used for transmitting analog audio signals via radio waves, because of the relative complexity needed in the receiver, for no added benefit with audio signals. It is also used for signal and waveform generation in digital synthesizers, such as the Yamaha DX7, to implement FM synthesis. A related type of sound synthesis called phase distortion is used in the Casio CZ synthesizers.

## Foundation

In general form, an analog modulation process of a sinusoidal carrier wave may be described by the following equation:

$m(t)=A(t)\cdot \cos(\omega t+\phi (t))\,$

.

*A(t)* represents the time-varying amplitude of the sinusoidal carrier wave and the cosine-term is the carrier at its angular frequency $\omega$ , and the instantaneous phase deviation $\phi (t)$ . This description directly provides the two major groups of modulation, amplitude modulation and angle modulation. In amplitude modulation, the angle term is held constant, while in angle modulation the term *A(t)* is constant and the second term of the equation has a functional relationship to the modulating message signal.

The functional form of the cosine term, which contains the expression of the instantaneous phase $\omega t+\phi (t)$ as its argument, provides the distinction of the two types of angle modulation, frequency modulation (FM) and phase modulation (PM).

In FM the message signal causes a functional variation of the carrier frequency. These variations are controlled by both the frequency and the amplitude of the modulating wave.

In phase modulation, the instantaneous phase deviation $\phi (t)$ (phase angle) of the carrier is controlled by the modulating waveform, such that the principal frequency remains constant.

In principle, the modulating signal in frequency modulation or phase modulation may either be analog in nature, or it may be digital.

The mathematics of the spectral behavior reveals that there are two regions of particular interest:

- For small amplitude signals, PM is similar to amplitude modulation (AM), and exhibits a doubling of baseband bandwidth and poor efficiency.
- For a single large sinusoidal signal, PM is similar to FM, and its bandwidth is approximately $2\left(h+1\right)f_{\text{M}}$ , Where $f_{\text{M}}=\omega _{\text{m}}/2\pi$ and h is the modulation index defined below. This is also known as Carson's Rule for PM.

## Modulation index

The modulation index reflects the degree of variation of the modulated variable around its unmodulated level. It relates to the variations in the phase of the carrier signal:

$h=\Delta \theta ,$

where $\Delta \theta$ is the peak phase deviation. Compare to the modulation index for frequency modulation.
