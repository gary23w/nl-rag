---
title: "Transponder (satellite communications)"
source: https://en.wikipedia.org/wiki/Transponder_(satellite_communications)
domain: satellite-systems
license: CC-BY-SA-4.0
tags: satellite systems, communications satellite, geostationary orbit, cubesat
fetched: 2026-07-02
---

# Transponder (satellite communications)

A communications satellite's transponder is the series of interconnected units that form a communications channel between the receiving and the transmitting antennas. It is mainly used in satellite communication to transfer the received signals.

A transponder is typically composed of:

- an input band-limiting device (an input band-pass filter),
- an input low-noise amplifier (LNA), designed to amplify the signals received from the Earth station (normally very weak, because of the large distances involved),
- a frequency translator (normally composed of an oscillator and a frequency mixer) used to convert the frequency of the received signal to the frequency required for the transmitted signal,
- an output band-pass filter,
- a power amplifier (this can be a traveling-wave tube or a solid-state amplifier).

Most communication satellites are radio relay stations in orbit and carry dozens of transponders, each with a bandwidth of tens of megahertz. Most transponders operate on a **bent pipe** (i.e., u-bend) principle, sending back to Earth what goes into the conduit with only amplification and a shift from uplink to downlink frequency. However, some modern satellites use on-board processing, where the signal is demodulated, decoded, re-encoded and modulated aboard the satellite. This type, called a "regenerative" transponder, is more complex, but has many advantages, such as improving the signal to noise ratio as the signal is regenerated from the digital domain, and also permits selective processing of the data in the digital domain.

With data compression and multiplexing, several video (including digital video) and audio channels may travel through a single transponder on a single wideband carrier.

Original analog video only had one channel per transponder, with subcarriers for audio and automatic transmission-identification service ATIS. Non-multiplexed radio stations can also travel in single channel per carrier (SCPC) mode, with multiple carriers (analog or digital) per transponder. This allows each station to transmit directly to the satellite, rather than paying for a whole transponder or using landlines to send it to an Earth station for multiplexing with other stations.

NASA distinguishes between a "transceiver" and "transponder". A transceiver has an independent transmitter and receiver packaged in the same unit. In a transponder the transmit carrier frequency is derived from the received signal. The frequency linkage allows an interrogating ground station to recover the Doppler shift and thus infer range and speed from a communication signal without allocating power to a separate ranging signal.

## Transponder equivalent

A **transponder equivalent** (**TPE**) is a normalized way to refer to transponder bandwidth. It simply means how many transponders would be used if the same total bandwidths used only 36 MHz transponders. So, for example, the ARSAT-1 has 24 IEEE Ku band transponders: 12 with a bandwidth of 36 MHz, 8 with 54 MHz, and 4 with 72 MHz, which totals to 1152 MHz, or 32 TPE (i.e., 1152 MHz divided by 36 MHz).
