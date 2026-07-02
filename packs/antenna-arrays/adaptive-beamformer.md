---
title: "Adaptive beamformer"
source: https://en.wikipedia.org/wiki/Adaptive_beamformer
domain: antenna-arrays
license: CC-BY-SA-4.0
tags: antenna array, phased array, adaptive beamformer, grating lobe
fetched: 2026-07-02
---

# Adaptive beamformer

An **adaptive beamformer** is a system that performs adaptive spatial signal processing with an array of transmitters or receivers. The signals are combined in a manner which increases the signal strength to/from a chosen direction. Signals to/from other directions are combined in a benign or destructive manner, resulting in degradation of the signal to/from the undesired direction. This technique is used in both radio frequency and acoustic arrays, and provides for directional sensitivity without physically moving an array of receivers or transmitters.

## Motivation/Applications

Adaptive beamforming was initially developed in the 1960s for the military applications of sonar and radar. There exist several modern applications for beamforming, one of the most visible applications being commercial wireless networks such as LTE. Initial applications of adaptive beamforming were largely focused in radar and electronic countermeasures to mitigate the effect of signal jamming in the military domain.

- Radar uses can be seen here Phased array radar. Although not strictly adaptive, these radar applications make use of either static or dynamic (scanning) beamforming.
- Commercial wireless standards such as 3GPP Long Term Evolution (LTE (telecommunication)) and IEEE 802.16 WiMax rely on adaptive beamforming to enable essential services within each standard.

## Basic Concepts

An adaptive beamforming system relies on principles of wave propagation and phase relationships. See Constructive interference, and Beamforming. Using the principles of superimposing waves, a higher or lower amplitude wave is created (e.g. by delaying and weighting the signal received). The adaptive beamforming system dynamically adapts in order to maximize or minimize a desired parameter, such as Signal-to-interference-plus-noise ratio.

## Adaptive Beamforming Schemes

There are several ways to approach the beamforming design, the first approach was implemented by maximizing the signal to noise ratio (SNR) by Applebaum 1965. This technique adapts the system parameters in order to maximize the receive signal power, while minimizing noise (such as interference or jamming). Another approach is the Least Mean Squares (LMS) error method implemented by Widrow, and Maximum Likelihood Method (MLM), developed in 1969 by Capon. Both the Applebaum and the Widrow algorithms are very similar, and converge toward an optimal solution. However, these techniques have implementation drawbacks. In 1974, Reed demonstrated a technique known as Sample-Matrix Inversion (SMI). SMI determines the adaptive antenna array weights directly, unlike the algorithms of Applebaum and Widrow.

A detailed explanation of the adaptive techniques introduced above can be found here:

- Least Mean Squares Algorithm
- Sample Matrix Inversion Algorithm
- Recursive Least Square Algorithm
- Conjugate gradient method
- Constant Modulus Algorithm
