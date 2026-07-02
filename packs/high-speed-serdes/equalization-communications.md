---
title: "Equalization (communications)"
source: https://en.wikipedia.org/wiki/Equalization_(communications)
domain: high-speed-serdes
license: CC-BY-SA-4.0
tags: high-speed serdes, line encoding, channel equalization, clock data recovery
fetched: 2026-07-02
---

# Equalization (communications)

In telecommunication, **equalization** is the reversal of distortion incurred by a signal transmitted through a channel. **Equalizers** are used to render the frequency response—for instance of a telephone line—*flat* from end-to-end. When a channel has been equalized the frequency domain attributes of the signal at the input are faithfully reproduced at the output. Telephones, DSL lines and television cables use equalizers to prepare data signals for transmission.

Equalizers are critical to the successful operation of electronic systems such as analog broadcast television. In this application the actual waveform of the transmitted signal must be preserved, not just its frequency content. Equalizing filters must cancel out any group delay and phase delay between different frequency components.

## Analog telecommunications

### Audio lines

Early telephone systems used equalization to correct for the reduced level of high frequencies in long cables, typically using Zobel networks. These kinds of equalizers can also be used to produce a circuit with a wider bandwidth than the standard telephone band of 300 Hz to 3.4 kHz. This was particularly useful for broadcasters who needed "music" quality, not "telephone" quality on landlines carrying program material. It is necessary to remove or cancel any loading coils in the line before equalization can be successful. Equalization was also applied to correct the response of the transducers, for example, a particular microphone might be more sensitive to low frequency sounds than to high frequency sounds, so an equalizer would be used to increase the volume of the higher frequencies (*boost*), and reduce the volume of the low frequency sounds (*cut*).

### Television lines

A similar approach to audio was taken with television landlines with two important additional complications. The first of these is that the television signal is a wide bandwidth covering many more octaves than an audio signal. A television equalizer consequently typically requires more filter sections than an audio equalizer. To keep this manageable, television equalizer sections were often combined into a single network using ladder topology to form a Cauer equalizer.

The second issue is that phase equalization is essential for an analog television signal. Without it dispersion causes the loss of integrity of the original wave-shape and is seen as smearing of what were originally sharp edges in the picture.

### Analog equalizer types

- Zobel network
- Lattice phase equalizer
- Bridged T delay equalizer

## Digital telecommunications

Modern digital telephone systems have less trouble in the voice frequency range as only the local line to the subscriber now remains in analog format, but DSL circuits operating in the MHz range on those same wires may suffer severe attenuation distortion, which is dealt with by automatic equalization or by abandoning the worst frequencies. Picturephone circuits also had equalizers.

In digital communications, the equalizer's purpose is to reduce intersymbol interference to allow recovery of the transmit symbols. It may be a simple linear filter or a complex algorithm.

### Digital equalizer types

- Linear equalizer: processes the incoming signal with a linear filter
  - MMSE equalizer: designs the filter to minimize E[|e|2], where e is the error signal, which is the filter output minus the transmitted signal.
  - Zero-forcing equalizer: approximates the inverse of the channel with a linear filter.
- Decision feedback equalizer: augments a linear equalizer by adding a filtered version of previous symbol estimates to the original filter output.
- Blind equalizer: estimates the transmitted signal without knowledge of the channel statistics, using only knowledge of the transmitted signal's statistics.
- Adaptive equalizer: is typically a linear equalizer or a DFE. It updates the equalizer parameters (such as the filter coefficients) as it processes the data. Typically, it uses the MSE cost function; it assumes that it makes the correct symbol decisions, and uses its estimate of the symbols to compute e, which is defined above.
- Viterbi equalizer: Finds the maximum likelihood (ML) optimal solution to the equalization problem. Its goal is to minimize the probability of making an error over the entire sequence.
- BCJR equalizer: uses the BCJR algorithm (also called the Forward-backward algorithm) to find the maximum *a posteriori* (MAP) solution. Its goal is to minimize the probability that a given bit was incorrectly estimated.
- Turbo equalizer: applies turbo decoding while treating the channel as a convolutional code.
