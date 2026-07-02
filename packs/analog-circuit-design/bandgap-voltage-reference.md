---
title: "Bandgap voltage reference"
source: https://en.wikipedia.org/wiki/Bandgap_voltage_reference
domain: analog-circuit-design
license: CC-BY-SA-4.0
tags: analog circuit design, operational amplifier, current mirror, differential amplifier
fetched: 2026-07-02
---

# Bandgap voltage reference

A **bandgap voltage reference** is a voltage reference circuit widely used in integrated circuits. It produces an almost constant voltage corresponding to the particular semiconductor's theoretical band gap, with very little fluctuations from variations of power supply, electrical load, time, temperature (as of 1999, they typically have an initial error of 0.5–1.0% and a temperature coefficient of 25–50 ppm/°C).

David Hilbiber of Fairchild Semiconductor filed a patent in 1963 and published this circuit concept in 1964. Bob Widlar, Paul Brokaw and others followed up with other commercially-successful versions.

## Operation

The voltage difference between two p–n junctions (e.g. diodes), operated at different current densities, is used to generate a current that is *proportional to absolute temperature* (*PTAT*) in a resistor. This current is used to generate a voltage in a second resistor. This voltage in turn is added to the voltage of one of the junctions (or a third one, in some implementations). The voltage across a diode operated at constant current is *complementary to absolute temperature* (*CTAT*), with a temperature coefficient of approximately −2 mV/K. If the ratio between the first and second resistor is chosen properly, the first order effects of the temperature dependency of the diode and the PTAT current will cancel out.

Although silicon's (Si) band gap at 0 K is technically 1.165 eV, the circuit essentially linearly extrapolates the bandgap–temperature curve to determine a slightly higher but precise reference around 1.2–1.3 V (the specific value depends on the particular technology and circuit design); the remaining voltage change over the operating temperature of typical integrated circuits is on the order of a few millivolts. This temperature dependency has a typical parabolic residual behavior since the linear (first order) effects are chosen to cancel.

Because the output voltage is by definition fixed around 1.25 V for typical Si bandgap reference circuits, the minimum operating voltage is about 1.4 V, as in a CMOS circuit at least one drain-source voltage of a field-effect transistor (FET) has to be added. Therefore, recent work concentrates on finding alternative solutions, in which for example currents are summed instead of voltages, resulting in a lower theoretical limit for the operating voltage.

The first letter of the acronym, CTAT, is sometimes misconstrued to represent *constant* rather than *complementary*. The term, *constant with temperature* (*CWT*), exists to address this confusion, but is not in widespread use.

When summing a PTAT and a CTAT current, only the linear terms of current are compensated, while the higher-order terms are limiting the temperature drift (TD) of the bandgap reference at around 20 ppm/°C, over a temperature range of 100 °C. For this reason, in 2001, Malcovati designed a circuit topology that can compensate high-order non-linearities, thus achieving an improved TD. This design used an improved version of Banba's topology and an analysis of base-emitter temperature effects that was performed by Tsividis in 1980. In 2012, Andreou has further improved the high-order non-linear compensation by using a second operational amplifier along with an additional resistor leg at the point where the two currents are summed up. This method enhanced further the curvature correction and achieved superior TD performance over a wider temperature range. In addition it achieved improved line regulation and lower noise.

The other critical issue in design of bandgap references is power efficiency and size of circuit. As a bandgap reference is generally based on BJT devices and resistors, the total size of circuit could be large and therefore expensive for IC design. Moreover, this type of circuit might consume a lot of power to reach to the desired noise and precision specification.

Despite these limitations, the band gap voltage reference is widely used in voltage regulators, covering the majority of 78xx, 79xx devices along with the TL431 and the complementary LM317 and LM337. Temperature coefficients as low as 1.5–2.0 ppm/°C can be obtained with bandgap references. However, the parabolic characteristic of voltage versus temperature means that a single figure in ppm/°C does not adequately describe the behavior of the circuit. Manufacturers' data sheets show that the temperature at which the peak (or trough) of the voltage curve occurs is subject to normal sample variations in production. Bandgap references are also suited for low-power applications.

Mixed-signal microcontrollers may provide an internal bandgap reference signal to be used as reference for any internal comparator(s) and analog-to-digital converter(s).

## Patents

- 1966, US Patent 3271660, *Reference voltage source*, David Hilbiber.
- 1971, US Patent 3617859, *Electrical regulator apparatus including a zero temperature coefficient voltage reference circuit*, Robert Dobkin and Robert Widlar.
- 1981, US Patent 4249122, *Temperature compensated bandgap IC voltage references*, Robert Widlar.
- 1984, US Patent 4447784, *Temperature compensated bandgap voltage reference circuit*, Robert Dobkin.
