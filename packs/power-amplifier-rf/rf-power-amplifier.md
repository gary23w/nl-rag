---
title: "RF power amplifier"
source: https://en.wikipedia.org/wiki/RF_power_amplifier
domain: power-amplifier-rf
license: CC-BY-SA-4.0
tags: power amplifier classes, power amplifier, load pull, Doherty amplifier
fetched: 2026-07-02
---

# RF power amplifier

A **radio-frequency power amplifier** (**RF power amplifier**) is a type of electronic amplifier that converts a low-power radio-frequency (RF) signal into a higher-power signal. Typically, RF power amplifiers are used in the final stage of a radio transmitter, their output driving the antenna. Design goals often include gain, power output, bandwidth, power efficiency, linearity (low signal compression at rated output), input and output impedance matching, and heat dissipation.

## Amplifier classes

The operation of RF amplifier circuits is classified based on the proportion of the cycle of the sinusoidal radio signal the amplifier (transistor or vacuum tube) where current is conducting. Class-A, class-AB and class-B are considered the linear amplifier classes in which the active device is used as a controlled current source, while class-C is a nonlinear class in which the active device is used as a switch. The bias at the input of the active device determines the class of the amplifier.

A common trade-off in power amplifier design is the trade-off between efficiency and linearity. The previously named classes become more efficient, but less linear, in the order they are listed. Operating the active device as a switch results in higher efficiency, theoretically up to 100%, but lower linearity. Among the switch-mode classes are class-D, class-E and class-F. The class-D amplifier is not often used in RF applications because the finite switching speed of the active devices and possible charge storage in saturation could lead to a large I-V product, which deteriorates efficiency.

## Solid state vs. vacuum tube amplifiers

Modern RF power amplifiers use solid-state devices, predominantly MOSFETs (metal–oxide–semiconductor field-effect transistors). The earliest MOSFET-based RF amplifiers date back to the mid-1960s. Bipolar junction transistors were also commonly used in the past, up until they were replaced by power MOSFETs, particularly LDMOS transistors, as the standard technology for RF power amplifiers by the 1990s,BJT are still commonly used for high frequency power amplifiers. Generally speaking, solid-state power amplifiers (SSPA) contain four main components: input, output, amplification stage and power supply.

MOSFET transistors and other modern solid-state devices have replaced vacuum tubes in most electronic devices, but tubes are still used in some high-power transmitters (see Valve RF amplifier). Although mechanically robust, transistors are electrically fragile – they are easily damaged by excess voltage or current. Tubes are mechanically fragile but electrically robust – they can handle remarkably high electrical overloads without appreciable damage.

## Applications

The basic applications of the RF power amplifier include driving to another high-power source, driving a transmitting antenna and exciting microwave cavity resonators. Among these applications, driving transmitter antennas is most well known. The transmitter–receivers are used not only for voice and data communication but also for weather sensing (in the form of a radar).

RF power amplifiers using LDMOS (laterally diffused MOSFET) are the most widely used power semiconductor devices in wireless telecommunication networks, particularly mobile networks. LDMOS-based RF power amplifiers are widely used in digital mobile networks such as 2G, 3G, and 4G and the good cost/performance ratio make them the preferred option for amateur radio.

## Wideband amplifier design

Impedance transformations over large bandwidth are difficult to realize, so conventionally, most wideband amplifiers are designed to feed a 50 Ω output load. Transistor output power is then limited to

$P_{\text{out}}\leq {\frac {(V_{\text{br}}-V_{\text{k}})^{2}}{8Z_{\text{o}}}},$

where

$V_{\text{br}}$

is defined as the

breakdown voltage

,

$V_{\text{k}}$

is defined as the knee voltage,

$Z_{\text{o}}$

is chosen so that the rated power can be met.

The external load is, by convention, $Z_{\text{L}}=50~\Omega .$ Therefore, there must be some sort of impedance matching that transforms from $Z_{\text{o}}$ to $Z_{\text{L}}=50~\Omega .$

The loadline method is often used in RF power amplifier design.
