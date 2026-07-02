---
title: "Pulse-amplitude modulation"
source: https://en.wikipedia.org/wiki/Pulse-amplitude_modulation
domain: high-speed-serdes
license: CC-BY-SA-4.0
tags: high-speed serdes, line encoding, channel equalization, clock data recovery
fetched: 2026-07-02
---

# Pulse-amplitude modulation

**Pulse-amplitude modulation** (**PAM**) is a form of signal modulation in which the message information is encoded in the amplitude of a pulse train interrupting the carrier frequency. Demodulation is performed by detecting the amplitude level of the carrier at every single period.

## Types

### Polarities

There are two types of pulse amplitude modulation:

- In *single polarity PAM*, a suitable fixed DC bias is added to the signal to ensure that all the pulses are positive.
- In *double polarity PAM*, the pulses are both positive and negative.

Pulse-amplitude modulation is widely used in modulating signal transmission of digital data, with non-baseband applications having been largely replaced by pulse-code modulation, and, more recently, by pulse-position modulation.

### Amplitudes

The number of possible pulse amplitudes in analog PAM is theoretically infinite. Digital PAM reduces the number of pulse amplitudes to some natural number not less than 3 (PAM-2 would be a simple binary signal and is usually not considered to be PAM). Common choices for the number of amplitudes are: 3, 4, 5, 8, 16.

## Uses

### Ethernet

Some versions of the Ethernet communication standard are an example of PAM usage.

- 100BASE-T4 and BroadR-Reach Ethernet standard use three-level PAM modulation (PAM-3).
- 1000BASE-T Gigabit Ethernet uses five-level PAM-5 modulation.
- 10GBASE-T 10 Gigabit Ethernet uses a Tomlinson–Harashima precoded (THP) version of pulse-amplitude modulation with 16 discrete levels (PAM-16). The THP precoding provides for noise resistance. Two consecutive PAM-16-encoded symbols are interpreted according to a two-dimensional checkerboard pattern known as DSQ128, where 128 out of 256 possible combinations are picked to maximize their "distance" (again for noise resistance). This provides the same SNR as PAM-8 while increasing the data rate by 7⁄6.
- 25 Gigabit Ethernet and some copper variants of 100 Gigabit Ethernet and 200 Gigabit Ethernet use PAM-4 modulation.
- 100 Gigabit Ethernet with single lambda on single-mode optical fiber use PAM-4 modulation.

### USB

USB4 Version 2.0 uses PAM-3 signaling for USB4 80 Gbps (USB4 Gen 4×2) and USB4 120 Gbps (USB4 Gen 4 Asymmetric) transmitting 3 bits per 2 clock cycles. Thunderbolt 5 uses the same PHY.

### Video memory

GDDR6X, developed by Micron and Nvidia and first used in the Nvidia RTX 3080 and 3090 graphics cards, uses PAM-4 signaling to transmit 2 bits per clock cycle without having to resort to higher frequencies or two channels or lanes with associated transmitters and receivers, which may increase power or space consumption and cost. Higher frequencies require higher bandwidth, which is a significant problem beyond 28 GHz when trying to transmit through copper. PAM-4 costs more to implement than earlier NRZ (non return to zero, PAM-2) coding partly because it requires more space in integrated circuits, and is more susceptible to SNR (signal to noise ratio) problems.

GDDR7 utilizes PAM-3 signaling to achieve speeds of 36 Gbps/pin. The higher data transmission rate per cycle compared to NRZ/PAM-2-signaling used by GDDR6 and prior generations improves power efficiency and signal integrity. Compared to PAM-4 (GDDR6X), it is less strict on manufacturing equipment.

### PCI Express

PCI Express 6.0 has introduced PAM-4 usage.

### Digital television

The North American Advanced Television Systems Committee standards for digital television uses a form of PAM to broadcast the data that makes up the television signal. This system, known as 8VSB, is based on an eight-level PAM. It uses additional processing to suppress one sideband and thus make more efficient use of limited bandwidth. Using a single 6 MHz channel allocation, as defined in the previous NTSC analog standard, 8VSB is capable of transmitting 32 Mbit/s. After accounting for error-correcting codes and other overhead, the data rate in the signal is 19.39 Mbit/s.

### Photobiology

The concept is also used for the study of photosynthesis using a specialized instrument that involves a spectrofluorometric measurement of the kinetics of fluorescence rise and decay in the light-harvesting antenna of thylakoid membranes, thus querying various aspects of the state of the photosystems under different environmental conditions. Unlike the traditional dark-adapted chlorophyll fluorescence measurements, pulse amplitude fluorescence devices allow measuring under ambient light conditions, which made measurements significantly more versatile.

### Electronic drivers for LED lighting

Pulse-amplitude modulation has also been developed for the control of light-emitting diodes (LEDs), especially for lighting applications. LED drivers based on the PAM technique offer improved energy efficiency over systems based upon other common driver modulation techniques such as pulse-width modulation (PWM) as the forward current passing through an LED is relative to the intensity of the light output and the LED efficiency increases as the forward current is reduced.

Pulse-amplitude modulation LED drivers are able to synchronize pulses across multiple LED channels to enable perfect color matching. Due to the inherent nature of PAM in conjunction with the rapid switching speed of LEDs, it is possible to use LED lighting as a means of wireless data transmission at high speed.
