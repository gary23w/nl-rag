---
title: "Insertion loss"
source: https://en.wikipedia.org/wiki/Insertion_loss
domain: s-parameters
license: CC-BY-SA-4.0
tags: scattering parameters, two-port network, return loss, insertion loss
fetched: 2026-07-02
---

# Insertion loss

In telecommunications, **insertion loss** is the loss of signal power resulting from the insertion of a device in a transmission line or optical fiber and is usually expressed in decibels (dB).

If the power transmitted to the load before insertion is *P*T and the power received by the load after insertion is *P*R, then the insertion loss in decibels is given by,

$IL(\mathrm {dB} )=10\log _{10}{P_{\mathrm {T} } \over P_{\mathrm {R} }}$

## Electronic filters

Insertion loss is a figure of merit for an electronic filter and this data is generally specified with a filter. Insertion loss is defined as a ratio of the signal level in a test configuration without the filter installed ( $\left\vert V_{1}\right\vert$ ) to the signal level with the filter installed ( $\left\vert V_{2}\right\vert$ ). This ratio is described in decibels by the following equation:

${\mbox{Insertion loss (dB)}}=10\log _{10}{\frac {\left\vert V_{1}\right\vert ^{2}}{\left\vert V_{2}\right\vert ^{2}}}=20\log _{10}{\frac {\left\vert V_{1}\right\vert }{\left\vert V_{2}\right\vert }}$

For passive filters, $\left\vert V_{2}\right\vert$ will be smaller than $\left\vert V_{1}\right\vert$ . In this case, the insertion loss is positive and measures how much smaller the signal is after adding the filter.

## Link with scattering parameters

In case the two measurement ports use the same reference impedance, the insertion loss ( $IL$ ) is defined as:

$IL=-20\log _{10}\left|S_{21}\right|\,{\text{dB}}$

.

Here $S_{21}$ is one of the scattering parameters. Insertion loss is the extra loss produced by the introduction of the DUT between the 2 reference planes of the measurement. The extra loss can be introduced by intrinsic loss in the DUT and/or mismatch. In case of extra loss the insertion loss is defined to be positive.
