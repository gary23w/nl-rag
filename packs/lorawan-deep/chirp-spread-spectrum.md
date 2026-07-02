---
title: "Chirp spread spectrum"
source: https://en.wikipedia.org/wiki/Chirp_spread_spectrum
domain: lorawan-deep
license: CC-BY-SA-4.0
tags: lorawan protocol, lora wide-area network, lpwan networking, chirp spread spectrum radio
fetched: 2026-07-02
---

# Chirp spread spectrum

In digital communications, **chirp spread spectrum** (**CSS**) is a spread spectrum technique that uses wideband linear frequency modulated chirp pulses to encode information. A chirp is a sinusoidal signal whose frequency increases or decreases over time (often with a polynomial expression for the relationship between time and frequency).

## Overview

As with other spread spectrum methods, chirp spread spectrum uses its entire allocated bandwidth to broadcast a signal, making it robust to channel noise. Further, because the chirps utilize a broad band of the spectrum, chirp spread spectrum is also resistant to multi-path fading even when operating at very low power. However, it is unlike direct-sequence spread spectrum (DSSS) or frequency-hopping spread spectrum (FHSS) in that it does not add any pseudo-random elements to the signal to help distinguish it from noise on the channel, instead relying on the linear nature of the chirp pulse. Additionally, chirp spread spectrum is resistant to the Doppler effect, which is typical in mobile radio applications.

## Uses

Chirp spread spectrum was originally designed to compete with ultra-wideband for precision ranging and low-rate wireless networks in the 2.45 GHz band. However, since the release of IEEE 802.15.4a (also known as IEEE 802.15.4a-2007), it is no longer actively being considered by the IEEE for standardization in the area of precision ranging.

Chirp spread spectrum is ideal for applications requiring low power usage and needing relatively low data rates (1 Mbit/s or less). In particular, IEEE 802.15.4a specifies CSS as a technique for use in low-rate wireless personal area networks (LR-WPAN). However, whereas IEEE 802.15.4-2006 standard specifies that WPANs encompass an area of 10 m or less, IEEE 802.15.4a-2007, specifies CSS as a physical layer to be used when longer ranges and devices moving at high speeds are part of your network. Nanotron's CSS implementation was actually seen to work at a range of 570 meters between devices. Further, Nanotron's implementation can work at data rates of up to 2 Mbit/s - higher than specified in 802.15.4a. Finally, the IEEE 802.15.4a PHY standard actually mixes CSS encoding techniques with differential phase-shift keying modulation (DPSK) to achieve better data rates.

Chirp spread spectrum may also be used in the future for military applications as it is very difficult to detect and intercept when operating at low power.

Very similar frequency swept waveforms are used in frequency modulated continuous wave radars (FM-CW) to measure range (distance); an unmodulated continuous wave Doppler radar can only measure range-rate (relative velocity along the line of sight). FM-CW radars are very widely used as radio altimeters in aircraft.

One application of chirp spread spectrum is LoRa.
