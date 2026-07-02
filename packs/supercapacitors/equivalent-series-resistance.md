---
title: "Equivalent series resistance"
source: https://en.wikipedia.org/wiki/Equivalent_series_resistance
domain: supercapacitors
license: CC-BY-SA-4.0
tags: supercapacitor cell, pseudocapacitance charge, equivalent series resistance, ragone plot
fetched: 2026-07-02
---

# Equivalent series resistance

Capacitors and inductors as used in electric circuits are not ideal components with only capacitance or inductance. However, they can be treated, to a very good degree of approximation, as being ideal capacitors and inductors in series with a resistance; this resistance is defined as the **equivalent series resistance** (**ESR)****.** If not otherwise specified, the ESR is always an AC resistance, which means it is measured at specified frequencies, 100 kHz for switched-mode power supply components, 120 Hz for linear power-supply components, and at its self-resonant frequency for general-application components. Additionally, audio components may report a "Q factor", incorporating ESR among other things, at 1000 Hz.

## Overview

Electrical circuit theory deals with ideal resistors, capacitors and inductors, each assumed to contribute only resistance, capacitance or inductance to the circuit. However, all components have a non-zero value of each of these parameters. In particular, all physical devices are constructed of materials with finite electrical resistance, so that physical components have some resistance in addition to their other properties. The physical origins of ESR depend on the device in question. One way to deal with these inherent resistances in circuit analysis is to use a lumped-element model to express each physical component as a combination of an ideal component and a small resistor in series, the ESR. The ESR can be measured and included in a component's datasheet. To some extent it can be calculated from the device properties.

Q factor, which is related to ESR and is sometimes a more convenient parameter than ESR to use in calculations of high-frequency non-ideal performance of real inductors, is quoted in inductor data sheets.

Capacitors, inductors, and resistors are usually designed to minimise other parameters. In many cases this can be done to a sufficient extent that *parasitic* capacitance and inductance of a resistor, for example, are so small as not to affect circuit operation. However, under some circumstances parasitics become important and even dominant.

## Component models

Pure capacitors and inductors do not dissipate energy; any component which dissipates energy must be treated in an equivalent circuit model incorporating one or more resistors. Actual passive two-terminal components can be represented by some network of lumped and distributed ideal inductors, capacitors, and resistors, in the sense that the real component behaves as the network does. Some of the components of the equivalent circuit can vary with conditions, e.g., frequency and temperature.

If driven by a periodic sinewave (alternating current) the component will be characterised by its complex impedance *Z*(ω) = *R* + *j* *X*(ω); the impedance can involve several minor resistances, inductances and capacitances in addition to the main property. These small deviations from the ideal behavior of the device can become significant under certain conditions, typically high frequency, where the reactance of small capacitances and inductances can become a significant element of circuit operation. Models of lesser or greater complexity can be used, depending upon the accuracy required. For many purposes, a simple model with an inductance or capacitance in series with an ESR is good enough.

These models, however simple or complex, can be inserted into a circuit to calculate performance. Computer tools are available for complex circuits; e.g., the SPICE program and its variants.

### Inductors

An inductor consists of a conducting insulated wire coil usually wound around a ferromagnetic core. Inductors have resistance inherent in the metal conductor, quoted as DCR in datasheets. This metallic resistance is small for small inductance values (typically below 1 Ω). The DC wire resistance is an important parameter in transformer and general inductor design because it contributes to the impedance of the component, and current flowing through that resistance is dissipated as waste heat, and energy is lost from the circuit. It can be modeled as a resistor in series with the inductor, often leading to the DC resistance being referred to as the ESR. Though this is not precisely correct usage, the unimportant elements of ESR are often neglected in circuit discussion, since it is rare that all elements of ESR are significant to a particular application.

An inductor using a core to increase inductance will have losses such as hysteresis and eddy current in the core. At high frequencies there are also losses in the windings due to proximity and skin effects. These are in addition to wire resistance, and lead to a higher ESR.

### Capacitors

In a non-electrolytic capacitor and electrolytic capacitors with solid electrolyte, the metallic resistance of the leads and electrodes and losses in the dielectric cause the ESR. Typically quoted values of ESR for ceramic capacitors are between 0.01 and 0.1 Ω. ESR of non-electrolytic capacitors tends to be fairly stable over time; for most purposes real non-electrolytic capacitors can be treated as ideal components.

Aluminium and tantalum electrolytic capacitors with non solid electrolyte have much higher ESR values, up to several ohms; electrolytics of higher capacitance have lower ESR. ESR decreases with frequency up to the capacitor's self-resonant frequency. A very serious problem, particularly with aluminium electrolytics, is that ESR increases over time from evaporation and more importantly from oxygen being depleted in the electrolyte with use. ESR can increase enough to cause circuit malfunction and even component damage, although measured capacitance may remain within tolerance. While this happens with normal aging, high temperatures and large ripple current exacerbate the problem. In a circuit with significant ripple current, an increase in ESR will increase heat accumulation, thus accelerating aging.

Electrolytic capacitors rated for high-temperature operation and of higher quality than basic consumer-grade parts are less susceptible to become prematurely unusable due to ESR increase. A cheap electrolytic capacitor may be rated for a life of less than 1000 hours (6 weeks) at 85 °C. Higher-grade parts are typically rated at a few thousand hours at maximum rated temperature, as can be seen from manufacturers' datasheets. If ESR is critical, specification of a part with higher temperature rating, "low ESR" or larger capacitance than is otherwise required may be advantageous. There is no standard for "low ESR" capacitor rating.

Polymer capacitors usually have lower ESR than wet-electrolytic of same value, and stable under varying temperature. Therefore, polymer capacitors can handle higher ripple current. From about 2007 it became common for better-quality computer motherboards to use only polymer capacitors where wet electrolytics had been used previously.

The ESR of capacitors larger than about 1 μF is easily measured in-circuit with an ESR meter.

| Type | 22 μF | 100 μF | 470 μF |
|---|---|---|---|
| Standard aluminum | 7–30 Ω | 2–7 Ω | 0.13–1.5 Ω |
| Low-ESR aluminum | 1–5 Ω | 0.3–1.6 Ω |   |
| Solid aluminum | 0.2–0.5 Ω |   |   |
| Sanyo OS-CON | 0.04–0.07 Ω | 0.03–0.06 Ω |   |
| Standard solid tantalum | 1.1–2.5 Ω | 0.9–1.5 Ω |   |
| Low-ESR tantalum | 0.2–1 Ω | 0.08–0.4 Ω |   |
| Wet-foil tantalum | 2.5–3.5 Ω | 1.8–3.9 Ω |   |
| Stacked-foil film | < 0.015 Ω |   |   |
| Ceramic | < 0.015 Ω |   |   |
