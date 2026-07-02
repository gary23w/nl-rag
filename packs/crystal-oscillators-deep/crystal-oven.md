---
title: "Crystal oven"
source: https://en.wikipedia.org/wiki/Crystal_oven
domain: crystal-oscillators-deep
license: CC-BY-SA-4.0
tags: crystal oscillator, colpitts oscillator, pierce oscillator, quartz clock
fetched: 2026-07-02
---

# Crystal oven

A **crystal oven** is a temperature-controlled chamber used to maintain the quartz crystal in electronic crystal oscillators at a constant temperature, in order to prevent changes in the frequency due to variations in ambient temperature. An oscillator of this type is known as an *oven-controlled crystal oscillator* (**OCXO**, where "XO" is an old abbreviation for "crystal oscillator"). This type of oscillator achieves the highest frequency stability possible with a crystal. They are typically used to control the frequency of radio transmitters, cellular base stations, military communications equipment, and for precision frequency measurement.

## Description

Quartz crystals are widely used in electronic oscillators to precisely control the frequency produced. The frequency at which a quartz crystal resonator vibrates depends on its physical dimensions. A change in temperature causes the quartz to expand or contract due to thermal expansion, changing the frequency of the signal produced by the oscillator. Although quartz has a very low coefficient of thermal expansion, temperature changes are still the major cause of frequency variation in crystal oscillators.

The oven is a thermally insulated enclosure containing the crystal and one or more electrical heating elements. Since other electronic components in the circuit are also vulnerable to temperature drift, usually the entire oscillator circuit is enclosed in the oven. A thermistor temperature sensor in a closed-loop control circuit is used to control the power to the heater and ensure that the oven is maintained at the precise temperature desired. Because the oven operates above ambient temperature, the oscillator usually requires a warm-up period after power has been applied to reach its operating temperature. During this warm-up period, the frequency will not have the full rated stability.

The temperature selected for the oven is that at which the slope of the crystal's frequency vs. temperature curve is zero, further improving stability. AT- or SC-cut (stress-compensated) crystals are used. The SC-cut has a wider temperature range over which near-zero temperature coefficient is achieved and thus reduces warmup time. Power transistors are usually used for the heaters instead of resistance heating elements. Their power output is proportional to the current, rather than the square of the current, which linearizes the gain of the control loop.

A common temperature for a crystal oven is 75 °C, but the temperature may vary between 30 and 80 °C depending on setup.

Most standard commercial crystals are specified to an environmental temperature of 0–70 °C, industrial versions are usually specified to −40 to +85 °C.

## Stability

Because of the power required to run the heater, OCXOs require more power than oscillators that run at ambient temperature, and the requirement for the heater, thermal mass, and thermal insulation means that they are physically larger. Therefore, they are not used in battery-powered or miniature applications, such as watches. However, in return, the oven-controlled oscillator achieves the best frequency stability possible from a crystal. The short-term frequency stability of OCXOs is typically 1×10−12 over a few seconds, while the long-term stability is limited to around 1×10−8 (10 ppb) per year by aging of the crystal. Achieving better stability requires switching to an atomic frequency standard, such as a rubidium standard, caesium standard, or hydrogen maser. Another cheaper alternative is to discipline a crystal oscillator with a GPS time signal, creating a GPS-disciplined oscillator (GPSDO). Using a GPS receiver that can generate stable time signals (down to within ~30 ns of UTC), a GPSDO can maintain oscillation stability of 10−13 for extended periods of time.

Crystal ovens are also used in optics. In crystals used for nonlinear optics, phase matching is also sensitive to temperature, and thus they require temperature stabilization, especially as the laser beam heats up the crystal. Additionally fast retuning of the crystal is often employed. For this application, the crystal and the thermistor need to be in very close contact and both must have as low a heat capacity as possible. To avoid breaking the crystal, large temperature variations in short times must be avoided.

### Comparison with other frequency standards

| Oscillator type* | Stability** | Aging / 10 year | Power | Mass (g) |
|---|---|---|---|---|
| Crystal oscillator (XO) | 10−5 to 10−4 | 10...20 ppm | 20 μW | 20 |
| Temperature-compensated crystal oscillator (TCXO) | 10−6 | 2...5 ppm | 100 μW | 50 |
| Microcomputer-compensated crystal oscillator (MCXO) | 10−8 to 10−7 | 1...3 ppm | 200 μW | 100 |
| Oven-controlled crystal oscillator (OCXO) 5...10 MHz 15...100 MHz | 2 × 10−8 5 × 10−7 | 2 × 10−8 to 2 × 10−7 2 × 10−6 to 11 × 10−9 | 1...3 W | 200...500 |
| Rubidium atomic frequency standard (RbXO) | 10−9 | 5 × 10−10 to 5 × 10−9 | 6...12 W | 1500...2500 |
| Caesium atomic frequency standard | 10−12 to 10−11 | 10−12 to 10−11 | 25...40 W | 10000...20000 |
| Global Positioning System (GPS) | 4 × 10−8 to 10−11 | 10−13 | 4 W | 340 |
| Radio time signal (DCF77) |   | 4 × 10−13 | — | 87 |

* Sizes and costs range from <5 cm3 and <5 USD for crystal oscillators, to more than 30 liters and 40 000 USD for Cs standards. ** Including the effects of military environments and one year of aging.
