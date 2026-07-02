---
title: "Array gain"
source: https://en.wikipedia.org/wiki/Array_gain
domain: antenna-arrays
license: CC-BY-SA-4.0
tags: antenna array, phased array, adaptive beamformer, grating lobe
fetched: 2026-07-02
---

# Array gain

In array antenna systems, **array gain** is the measure of the improvement in signal-to-noise ratio (SNR) achieved by the array. It is calculated as the SNR of the array output signal divided by the SNR of the array input signal. Intuitively, the array gain is realized by the fact that the signal is coherently added from *N* array elements, while the noise is incoherently added from those same elements. If the noise is presumed to be uncorrelated the array gain is ≤ *N*, the number of array elements, and the array gain reduces to the inverse of the square of the 2-norm of the array weight vector, under the assumption that the weight vector is normalized such that its sum is unity, so that

$A={1 \over {\vec {w}}^{H}{\vec {w}}}$

For a uniformly weighted array (un-tapered such that all elements contribute equally), the array gain is equal to *N*.

Array gain is not the same thing as "gain," "power gain," "directive gain," or "directivity," but if the noise environment around the array is isotropic and the array input signal is from an isotropic radiator, then array gain is equal to gain defined in the usual way from the array beam pattern. The terms "power gain" and "directive gain" are deprecated by IEEE.

## Applications

In radio astronomy it is difficult to achieve a good signal-to-noise ratio because of background noise from modern communications. Even for strong astronomical radio emission it is typical for SNR levels to be below 0 decibels. To counter this problem exposure of the antenna to the source over large periods of time are needed just as in visible sky viewing. Array gain is achieved using multiple, even dozens of radio receivers to collect as much signal as possible.

Robots equipped with antenna arrays have better communication using array gain to eradicate dead spots and reduce interferences.
