---
title: "Crystal oscillator (part 2/2)"
source: https://en.wikipedia.org/wiki/Crystal_oscillator
domain: crystal-oscillators-deep
license: CC-BY-SA-4.0
tags: crystal oscillator, colpitts oscillator, pierce oscillator, quartz clock
fetched: 2026-07-02
part: 2/2
---

## Crystal cuts

The resonator plate can be cut from the source crystal in many different ways. The orientation of the cut influences the crystal's aging characteristics, frequency stability, thermal characteristics, and other parameters. These cuts operate at bulk acoustic wave (BAW); for higher frequencies, surface acoustic wave (SAW) devices are employed.

Image of several crystal cuts

| Cut | Frequency range | Mode | Angles | Description |
|---|---|---|---|---|
| **AT** | 500 kHz – 300 MHz | thickness shear (c mode, slow quasi-shear) | 35°15′, 0° (< 25 MHz) 35°18′, 0° (> 10 MHz) | The most common cut, developed in 1934. The plate contains the crystal's x axis and is inclined by 35°15′ from the z (optical) axis. The frequency-temperature curve is a sine-shaped curve with inflection point at around 25~35 °C . Has frequency constant 1.661 MHz⋅mm. Most (estimated over 90%) of all crystals are this variant. Used for oscillators operating in wider temperature range, for a frequency range of 500 kHz–200 MHz; also used in oven-controlled oscillators. Sensitive to mechanical stresses, whether caused by external forces or by temperature gradients. Thickness-shear crystals typically operate in fundamental mode at 1–30 MHz, 3rd overtone at 30–90 MHz, and 5th overtone at 90–150 MHz; according to other source they can be made for fundamental mode operation up to 300 MHz, though that mode is usually used only to 100 MHz and according to yet another source the upper limit for fundamental frequency of the AT cut is limited to 40 MHz for small diameter blanks. Can be manufactured either as a conventional round disk, or as a strip resonator; the latter allows much smaller size. The thickness of the quartz blank is about (1.661 mm)/(frequency in MHz), with the frequency somewhat shifted by further processing. The third overtone is about 3 times the fundamental frequency; the overtones are higher than the equivalent multiple of the fundamental frequency by about 25 kHz per overtone. Crystals designed for operating in overtone modes have to be specially processed for plane parallelism and surface finish for the best performance at a given overtone frequency. |
| **SC** | 500 kHz – 200 MHz | thickness shear | 35°15′, 21°54′ | A special cut (Stress Compensated) developed in 1974, is a double-rotated cut (35°15′ and 21°54′) for oven-stabilized oscillators with low phase noise and good aging characteristics. Less sensitive to mechanical stresses. Has faster warm-up speed, higher Q, better close-in phase noise, less sensitivity to spatial orientation against the vector of gravity, and less sensitivity to vibrations. Its frequency constant is 1.797 MHz⋅mm. Coupled modes are worse than the AT cut, resistance tends to be higher; much more care is required to convert between overtones. Operates at the same frequencies as the AT cut. The frequency-temperature curve is a third order downward parabola with inflection point at 95 °C and much lower temperature sensitivity than the AT cut. Suitable for OCXOs in e.g. space and GPS systems. Less available than AT cut, more difficult to manufacture; the order-of-magnitude improvement of parameters is traded for an order of magnitude tighter crystal orientation tolerances. Aging characteristics are 2~3 times better than of the AT cuts. Less sensitive to drive levels. Far fewer activity dips. Less sensitive to plate geometry. Requires an oven, does not operate well at ambient temperatures as the frequency rapidly falls off at lower temperatures. Has several times lower motional capacitance than the corresponding AT cut, reducing the possibility to adjust the crystal frequency by attached capacitor; this restricts usage in conventional TCXO and VCXO devices, and other applications where the frequency of the crystal has to be adjustable. The temperature coefficients for the fundamental frequency is different than for its third overtone; when the crystal is driven to operate on both frequencies simultaneously, the resulting beat frequency can be used for temperature sensing in e.g. microcomputer-compensated crystal oscillators. Sensitive to electric fields. Sensitive to air damping, to obtain optimum Q it has to be packaged in vacuum. Temperature coefficient for b mode is −25 ppm/°C , for dual mode 80 to over 100 ppm/°C . |
| **BT** | 500 kHz – 200 MHz | thickness shear (b mode, fast quasi-shear) | −49°8′, 0° | A special cut, similar to AT cut, except the plate is cut at 49° from the z axis. Operates in thickness shear mode, in b mode (fast quasi-shear). It has well known and repeatable characteristics. Has frequency constant 2.536 MHz⋅mm. Has poorer temperature characteristics than the AT cut. Due to the higher frequency constant, can be used for crystals with higher frequencies than the AT cut, up to over 50 MHz . |
| **IT** |   | thickness shear |   | A special cut, a double-rotated cut with improved characteristics for oven-stabilized oscillators. Operates in thickness shear mode. The frequency-temperature curve is a third order downward parabola with inflection point at 78 °C . Rarely used. Has similar performance and properties to the SC cut, more suitable for higher temperatures. |
| **FC** |   | thickness shear |   | A special cut, a double-rotated cut with improved characteristics for oven-stabilized oscillators. Operates in thickness shear mode. The frequency-temperature curve is a third order downward parabola with inflection point at 52 °C . Rarely used. Employed in oven-controlled oscillators; the oven can be set to lower temperature than for the AT / IT / SC cuts, to the beginning of the flat part of the temperature-frequency curve (which is also broader than of the other cuts); when the ambient temperature reaches this region, the oven switches off and the crystal operates at the ambient temperature, while maintaining reasonable accuracy. This cut therefore combines the power saving feature of allowing relatively low oven temperature with reasonable stability at higher ambient temperatures. |
| **AK** |   | thickness shear |   | a double rotated cut with better temperature-frequency characteristics than AT and BT cuts and with higher tolerance to crystallographic orientation than the AT, BT, and SC cuts (calculated to be a factor 50 against a standard AT cut). It operates in thickness-shear mode. |
| **CT** | 300 – 900 kHz | face shear | 38°, 0° | The frequency-temperature curve is a downward parabola. |
| **DT** | 75 – 800 kHz | face shear | −52°, 0° | Similar to CT cut. The frequency-temperature curve is a downward parabola. The temperature coefficient is lower than the CT cut; where the frequency range permits, DT is preferred over CT. |
| **SL** |   | face-shear | −57°, 0° |   |
| **GT** | 100 kHz – 3 MHz | width-extensional | 51°7′ | Its temperature coefficient between −25 ... +75 °C is near-zero, due to cancelling effect between two modes. |
| **E**, **5°X** | 50 – 250 kHz | longitudinal |   | Has reasonably low temperature coefficient, widely used for low-frequency crystal filters. |
| **MT** | 40 – 200 kHz | longitudinal |   |   |
| **ET** |   |   | 66°30′ |   |
| **FT** |   |   | −57° |   |
| **NT** | 8 – 130 kHz | length-width flexure (bending) |   |   |
| **XY**, **tuning fork** | 3 – 85 kHz | length-width flexure |   | The dominant low-frequency crystal, as it is smaller than other low-frequency cuts, less expensive, has low impedance and low ⁠ C0 / C1 ⁠ ratio. The chief application is the 32.768 kHz RTC crystal. Its second overtone is about six times the fundamental frequency. |
| **H** | 8 – 130 kHz | length-width flexure |   | Used extensively for wideband filters. The temperature coefficient is linear. |
| **J** | 1 – 12 kHz | length-thickness flexure |   | J cut is made of two quartz plates bonded together, selected to produce out of phase motion for a given electrical field. |
| **RT** |   |   |   | A double rotated cut. |
| **SBTC** |   |   |   | A double rotated cut. |
| **TS** |   |   |   | A double rotated cut. |
| **X 30°** |   |   |   | A double rotated cut. |
| **LC** |   | thickness shear | 11.17° / 9.39° | A double rotated cut ("linear coefficient") with a linear temperature-frequency response; can be used as a sensor in crystal thermometers. Temperature coefficient is 35.4 ppm/°C . |
| **AC** |   |   | 31° | Temperature-sensitive, can be used as a sensor. Single mode with steep frequency-temperature characteristics. Temperature coefficient is 20 ppm/°C . |
| **BC** |   |   | −60° | Temperature-sensitive. |
| **NLSC** |   |   |   | Temperature-sensitive. Temperature coefficient is about 14 ppm/°C . |
| **Y** |   |   |   | Temperature-sensitive, can be used as a sensor. Single mode with steep frequency-temperature characteristics. The plane of the plate is perpendicular to the y axis of the crystal. Also called **parallel** or **30-degree**. Temperature coefficient is about 90 ppm/°C . |
| **X** |   |   |   | Used in one of the first crystal oscillators in 1921 by W.G. Cady, and as a 50 kHz oscillator in the first crystal clock by Horton and Marrison in 1927. The plane of the plate is perpendicular to the x axis of the crystal. Also called **perpendicular**, **normal**, **Curie**, **zero-angle**, or **ultrasonic**. |

The letter ‘T’ in the cut name marks a temperature-compensated cut – a cut oriented in a way that the temperature coefficients of the lattice are minimal; the FC and SC cuts are also temperature-compensated.

The high frequency cuts are mounted by their edges, usually on springs; the stiffness of the spring has to be optimal, as if it is too stiff, mechanical shocks could be transferred to the crystal and cause it to break, and too little stiffness may allow the crystal to collide with the inside of the package when subjected to a mechanical shock, and break. Strip resonators, usually AT cuts, are smaller and therefore less sensitive to mechanical shocks. At the same frequency and overtone, the strip has less pullability, higher resistance, and higher temperature coefficient.

The low frequency cuts are mounted at the nodes where they are virtually motionless; thin wires are attached at such points on each side between the crystal and the leads. The large mass of the crystal suspended on the thin wires makes the assembly sensitive to mechanical shocks and vibrations.

The crystals are usually mounted in hermetically sealed glass or metal cases, filled with a dry and inert atmosphere, usually vacuum, nitrogen, or helium. Plastic housings can be used as well, but those are not hermetic and another secondary sealing has to be built around the crystal.

Several resonator configurations are possible, in addition to the classical way of directly attaching leads to the crystal. E.g. the **BVA resonator** (Boîtier à Vieillissement Amélioré, Enclosure with Improved Aging), developed in 1976; the parts that influence the vibrations are machined from a single crystal (which reduces the mounting stress), and the electrodes are deposited not on the resonator itself but on the inner sides of two condenser discs made of adjacent slices of the quartz from the same bar, forming a three-layer sandwich with no stress between the electrodes and the vibrating element. The gap between the electrodes and the resonator act as two small series capacitors, making the crystal less sensitive to circuit influences. The architecture eliminates the effects of the surface contacts between the electrodes, the constraints in the mounting connections, and the issues related to ion migration from the electrodes into the lattice of the vibrating element. The resulting configuration is rugged, resistant to shock and vibration, resistant to acceleration and ionizing radiation, and has improved aging characteristics. AT cut is usually used, though SC cut variants exist as well. BVA resonators are often used in spacecraft applications.

In the 1930s to 1950s, it was fairly common for people to adjust the frequency of the crystals by manual grinding. The crystals were ground using a fine abrasive slurry, or even a toothpaste, to increase their frequency. A slight decrease by 1–2 kHz when the crystal was overground was possible by marking the crystal face with a pencil lead, at the cost of a lowered Q.

The frequency of the crystal is slightly adjustable ("pullable") by modifying the attached capacitances. A varactor, a diode with capacitance depending on applied voltage, is often used in voltage-controlled crystal oscillators, VCXO. The crystal cuts are usually AT or rarely SC, and operate in fundamental mode; the amount of available frequency deviation is inversely proportional to the square of the overtone number, so a third overtone has only one-ninth of the pullability of the fundamental mode. SC cuts, while more stable, are significantly less pullable.


## Circuit notations and abbreviations

On electrical schematic diagrams, *crystals* are designated with the class letter *Y* (Y1, Y2, etc.). Oscillators, whether they are crystal oscillators or others, are designated with the class letter *G* (G1, G2, etc.). Crystals may also be designated on a schematic with *X* or *XTAL* (a phonetic abbreviation, comparable to using *Xmas* for *Christmas*), or a crystal oscillator with ***XO***.

Crystal oscillator types and their abbreviations:

- **ATCXO** — Analog temperature controlled crystal oscillator
- **CDXO** — Calibrated dual crystal oscillator
- **DTCXO** — Digital temperature compensated crystal oscillator
- **EMXO** — Evacuated miniature crystal oscillator
- **GPSDO** — Global positioning system disciplined oscillator
- **MCXO** — Microcomputer-compensated crystal oscillator
- **OCVCXO** — oven-controlled voltage-controlled crystal oscillator
- **OCXO** — Oven-controlled crystal oscillator
- **RbXO** — Rubidium crystal oscillators (RbXO), a crystal oscillator (can be an MCXO) synchronized with a built-in rubidium standard which is run only occasionally to save power
- **TCVCXO** — Temperature-compensated voltage-controlled crystal oscillator
- **TCXO** — Temperature-compensated crystal oscillator
- **TMXO** – Tactical miniature crystal oscillator
- **TSXO** — Temperature-sensing crystal oscillator, an adaptation of the TCXO
- **VCTCXO** — Voltage-controlled temperature-compensated crystal oscillator
- **VCXO** — Voltage-controlled crystal oscillator
