---
title: "Common-mode signal"
source: https://en.wikipedia.org/wiki/Common-mode_signal
domain: electromagnetic-compatibility
license: CC-BY-SA-4.0
tags: electromagnetic compatibility, electromagnetic interference, signal crosstalk, common-mode signal
fetched: 2026-07-02
---

# Common-mode signal

In electrical engineering, a **common-mode signal** is the identical component of voltage present at both input terminals of an electrical device. In telecommunication, the common-mode signal on a transmission line is also known as **longitudinal voltage**.

**Common-mode interference** (CMI) is a type of common-mode signal. Common-mode interference is interference that appears on both signal leads, or coherent interference that affects two or more elements of a network.

In most electrical circuits, desired signals are transferred by a differential voltage between two conductors. If the voltages on these conductors are *U*1 and *U*2, the common-mode signal is the average of the voltages:

$U_{\text{cm}}={\frac {U_{1}+U_{2}}{2}}$

When referenced to the local common or ground, a common-mode signal appears on both lines of a two-wire cable, in phase and with equal amplitudes. Technically, a common-mode voltage is one-half the vector sum of the voltages from each conductor of a balanced circuit to local ground or common. Such signals can arise from one or more of the following sources:

- Radiated signals coupled equally to both lines,
- An offset from signal common created in the driver circuit, or
- A ground differential between the transmitting and receiving locations.

Noise induced into a cable, or transmitted from a cable, usually occurs in the common mode, as the same signal tends to be picked up by both conductors in a two-wire cable. Likewise, RF noise transmitted from a cable tends to emanate from both conductors. Elimination of common-mode signals on cables entering or leaving electronic equipment is important to ensure electromagnetic compatibility. Unless the intention is to transmit or receive radio signals, an electronic designer generally designs electronic circuits to minimise or eliminate common-mode effects.

## Methods of eliminating common-mode signals

- Differential amplifiers or receivers that respond only to voltage differences, e.g. those between the wires that constitute a pair. This method is particularly suited for instrumentation where signals are transmitted through DC bias. For sensors with very high output impedance that require very high common-mode rejection ratio, a differential amplifier is combined with input buffers to form an instrumentation amplifier.
- An inductor where a pair of signaling wires follow the same path through the inductor, e.g. in a bifilar winding configuration such as used in Ethernet magnetics. Useful for AC and DC signals, but will filter only higher frequency common-mode signals.
- A transformer, which is useful for AC signals only, and will filter any form of common-mode noise, but may be used in combination with a bifilar wound coil to eliminate capacitive coupling of higher frequency common-mode signals across the transformer. Used in twisted pair Ethernet.

Common-mode filtering may also be used to prevent egress of noise for electromagnetic compatibility purposes:

- High frequency common-mode signals (e.g., RF noise from a computing circuit) may be blocked using a ferrite bead clamped to the outside of a cable. These are often observable on laptop computer power supplies near the jack socket, and good quality mouse or printer USB cables and HDMI cables.

- Switch mode power supplies include common and differential mode filtering inductors to block the switching signal noise returning into mains wiring.

Common-mode rejection ratio is a measure of how well a circuit eliminates common-mode interference.
