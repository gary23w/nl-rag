---
title: "Subtractive synthesis"
source: https://en.wikipedia.org/wiki/Subtractive_synthesis
domain: audio-synthesis
license: CC-BY-SA-4.0
tags: sound synthesis, subtractive synthesis, fm synthesis, wavetable synthesis
fetched: 2026-07-02
---

# Subtractive synthesis

**Subtractive synthesis** is a method of sound synthesis in which overtones of an audio signal are attenuated by a filter to alter the timbre of the sound.

## Overview

Subtractive synthesis relies on source sounds that have overtones, such as non-sinusoidal waveforms like square and triangle waves, or white and pink noise. These overtones are then modulated to alter the source sound. This modulation can happen in a wide variety of ways, such as voltage-controlled or low-pass filters.

The technology developed in experimental electronic studios which were primarily focused on telecommunications and military applications. Early examples include Bell Labs' Voder (1937–8). Composers began applying the concept of subtractive synthesis beyond the recording studio in concert music. Henri Pousseur's *Scambi* (1957) subjects white noise to filters and uses the resulting sounds to create montages. *Mikrophonie I* (1964) by Karlheinz Stockhausen uses a tam-tam and a microphone as the primary sound source which is then filtered extensively by two sound projectionists.

Until the advent of digital synthesizers, subtractive synthesis was the nearly universal electronic method of sound production. Its popularity was due largely to its relative simplicity. Subtractive synthesis was so prevalent in analog synthesizers that it is sometimes called "analog synthesis". It was the method of sound production in instruments like the Trautonium (1930), Novachord (1939), Buchla 100 (1960s), EMS VCS 3 (1969), Minimoog (1970), ARP 2600 (1971), Oberheim OB-1 (1978), and Korg MS-20 (1978). Programmable sound generators (PSG) relied heavily on subtractive synthesis. PSGs were used in many personal computers, arcade games, and home consoles such as the Commodore 64, Atari ST, Mattel's Intellivision, Sega's Master System, and the ZX Spectrum.

## Nomenclature

Subtractive synthesis has become a catchall for a method where source sounds are modulated, and it is sometimes applied inappropriately.

## Method

The following is an example of subtractive synthesis as it might occur in an electronic instrument to emulate the sound of a plucked string. It was created with a personal computer program designed to emulate an analogue subtractive synthesizer.

### Source Sound

First, an electronic oscillator produces a relatively complex waveform with audible overtones. Only one oscillator is necessary, and the number can vary widely. In this case, two oscillators are used:

|   | (Closeup view of waveform in the audio sample.) |
|---|---|
|   | (Closeup oscilloscope of Waveform #2.) |

Pulse-width modulation is applied to both waveforms to create a more complex tone with vibrato:

|   | (Closeup of pulse-width modulated Waveform 1.) |
|---|---|
|   | (Closeup of pulse-width modulated Waveform 2.) |

The pulse-width modulated sounds are now combined at equal volume. Combining them at different volumes would create different timbres. The result is a 2-second **source sound**, which is ready for subtractive synthesis.

|   | (Combined waveforms and pulse-width modulation.) |
|---|---|

### Subtractive Synthesis

The combined wave is passed through a voltage-controlled amplifier connected to an envelope generator. The parameters of the sound's envelope (attack, decay, sustain and release) are manipulated to change its sound. In this case, the decay is vastly increased, sustain is reduced, and the release shortened. The resulting sound is audible for half as long as the source sound:

|   | (Enveloped waveform.) |
|---|---|

With its new envelope, the sound is run through a low-pass filter, which reduces the volume of higher overtones:

|   | (Low-pass filtered waveform.) |
|---|---|

To better emulate the sound of a plucked string, the filter's cutoff frequency is raised.

|   | (Final waveform) |
|---|---|
|   |   |
