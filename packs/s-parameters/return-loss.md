---
title: "Return loss"
source: https://en.wikipedia.org/wiki/Return_loss
domain: s-parameters
license: CC-BY-SA-4.0
tags: scattering parameters, two-port network, return loss, insertion loss
fetched: 2026-07-02
---

# Return loss

In telecommunications, **return loss** is a measure in relative terms of the power of the signal reflected by a discontinuity in a transmission line or optical fiber. This discontinuity can be caused by a mismatch between the termination or load connected to the line and the characteristic impedance of the line. It is usually expressed as a ratio in decibels (dB):

${\text{RL}}({\text{dB}})=10\log _{10}{\frac {P_{\text{i}}}{P_{\text{r}}}},$

where RL(dB) is the return loss in dB, *P*i is the incident power, and *P*r is the reflected power.

Return loss is related to both standing wave ratio (SWR) and reflection coefficient (Γ). Increasing return loss corresponds to lower SWR. Return loss is a measure of how well devices or lines are matched. A match is good if the return loss is high. A high return loss is desirable and results in a lower insertion loss.

From a certain perspective "return loss" is a misnomer. The usual function of a transmission line is to convey power from a source to a load with minimal loss. If a transmission line is correctly matched to a load, the reflected power will be zero, no power will be lost due to reflection, and "return loss" will be infinite. Conversely if the line is terminated in an open circuit, the reflected power will be equal to the incident power; all of the incident power will be lost in the sense that none of it will be transferred to a load, and RL will be zero. Thus the numerical values of RL tend in the opposite sense to that expected of a "loss".

## Sign

As defined above, RL will always be positive, since *P*r can never exceed *P*i. However, return loss has historically been expressed as a negative number, and this convention is still widely found in the literature. Strictly speaking, if a negative sign is ascribed to RL, the ratio of *reflected* to *incident* power is implied:

${\text{RL}}'({\text{dB}})=10\log _{10}{\frac {P_{\text{r}}}{P_{\text{i}}}},$

where RL′(dB) is the negative of RL(dB).

In practice, the sign ascribed to RL is largely immaterial. If a transmission line includes several discontinuities along its length, the total return loss will be the sum of the RLs caused by each discontinuity, and provided all RLs are given the same sign, no error or ambiguity will result. Whichever convention is used, it will always be understood that *P*r can never exceed *P*i.

## Electrical

In metallic conductor systems, reflections of a signal traveling down a conductor can occur at a discontinuity or impedance mismatch. The ratio

$\Gamma ={\frac {V_{\text{r}}}{V_{\text{i}}}}$

of the amplitude of the reflected wave *V*r to the amplitude of the incident wave *V*i is known as the reflection coefficient.

Return loss is the negative of the magnitude of the reflection coefficient in dB. Since power is proportional to the square of the voltage, return loss is given by

${\text{RL}}({\text{dB}})=-20\log _{10}|\Gamma |,$

where the vertical bars indicate magnitude. Thus, a large positive return loss indicates that the reflected power is small relative to the incident power, which indicates good impedance match between transmission line and load.

If the incident power and the reflected power are expressed in "absolute" decibel units, (e.g., dBm), then the return loss in dB can be calculated as the difference between the incident power *P*i (in absolute dBm units) and the reflected power *P*r (also in absolute dBm units):

${\text{RL}}({\text{dB}})=P_{\text{i}}({\text{dBm}})-P_{\text{r}}({\text{dBm}}).$

## Optical

In optics (particularly in fiber optics) a loss that takes place at discontinuities of refractive index, especially at an air–glass interface such as a fiber endface. At those interfaces, a fraction of the optical signal is reflected back toward the source. This reflection phenomenon is also called "**Fresnel reflection loss**", or simply "**Fresnel loss**".

Fiber optic transmission systems use lasers to transmit signals over optical fiber, and a low optical return loss

${\text{ORL}}({\text{dB}})=10\log _{10}{\frac {P_{\text{i}}}{P_{\text{r}}}}$

(where $P_{\text{r}}$ is the reflected power, and $P_{\text{i}}$ is the incident, or input, power) can cause the laser to stop transmitting correctly. The measurement of ORL is becoming more important in the characterization of optical networks as the use of wavelength-division multiplexing increases. These systems use lasers that have a lower tolerance for ORL and introduce elements into the network that are located in close proximity to the laser.
