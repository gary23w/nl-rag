---
title: "Voltage reference"
source: https://en.wikipedia.org/wiki/Voltage_reference
domain: voltage-references
license: CC-BY-SA-4.0
tags: voltage reference, Zener diode, shunt regulator, precision reference
fetched: 2026-07-02
---

# Voltage reference

A **voltage reference** is an electronic device that ideally produces a fixed (constant) voltage irrespective of the loading on the device, power supply variations, temperature changes, and the passage of time. Voltage references are used in power supplies, analog-to-digital converters, digital-to-analog converters, and other measurement and control systems. Voltage references vary widely in performance; a regulator for a computer power supply may only hold its value to within a few percent of the nominal value, whereas laboratory voltage standards have precisions and stability measured in parts per million.

## In metrology

The earliest voltage references or standards were wet chemical cells such as the Clark cell and Weston cell, which are still used in some laboratory and calibration applications.

Laboratory-grade Zener diode secondary solid-state voltage standards used in metrology can be constructed with a drift of about 1 part per million per year.

The value of the "conventional" volt is now maintained by superconductive integrated circuits using the Josephson effect to get a voltage to an accuracy of 1 parts per billion or better, the Josephson voltage standard. The paper titled, "Possible new effects in superconductive tunnelling", was published by Brian David Josephson in 1962 and earned Josephson the Nobel Prize in Physics in 1973.

Formerly, mercury batteries were much used as convenient voltage references especially in portable instruments such as photographic light meters; mercury batteries had a very stable discharge voltage over their useful life.

## Solid state devices

Any semiconductor diode has an exponential current–voltage characteristic that can be viewed as having a "knee" voltage, sometimes used as an imprecise voltage reference. Datasheets may list a forward voltage drop at a specified "on" current. This voltage is around 0.3 V for germanium diodes, around 0.6 V to 0.7 V for silicon diodes, and from 1.6 V (red) to 4 V (violet) for visible light emitting diodes. These devices have a strong temperature dependence, which may make them useful for temperature measurement or for compensating bias in analog circuits.

Zener diodes are also frequently used to provide a reference voltage of moderate stability and accuracy, useful for many electronic devices. An avalanche diode displays a similar stable voltage over a range of current. The most stable diodes of this type are made by temperature-compensating a Zener diode by placing it in series with a forward diode; such diodes are made as two-terminal devices, e.g. the 1N821 series having an overall voltage drop of 6.2 V at 7.5 mA, but are also sometimes included in integrated circuits.

The most common voltage reference circuit used in integrated circuits is the bandgap voltage reference. A bandgap-based reference (commonly just called a 'bandgap') uses analog circuits to add a multiple of the voltage difference between two bipolar junctions biased at different current densities to the voltage developed across a diode. The diode voltage has a negative temperature coefficient (i.e. it decreases with increasing temperature), and the junction voltage difference has a positive temperature coefficient. When added in the proportion required to make these coefficients cancel out, the resultant constant value is a voltage equal to the bandgap voltage of the semiconductor. In silicon, this is approximately 1.25 V. Buried-Zener references can provide even lower noise levels, but require higher operating voltages that are not available in many battery-operated devices.

## Gas filled devices

Gas filled tubes and neon lamps have also been used as voltage references, primarily in tube-based equipment, as the voltage needed to sustain the gas discharge is comparatively constant. For example, the popular RCA 991 "voltage regulator tube" is an NE-16 neon lamp, which fires at 87 volts and then holds 48 to 67 volts across the discharge path.
