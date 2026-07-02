---
title: "Transistor (part 2/2)"
source: https://en.wikipedia.org/wiki/Transistor
domain: transistor-scaling
license: CC-BY-SA-4.0
tags: transistor scaling, dennard scaling, moore's law, gate-all-around transistor
fetched: 2026-07-02
part: 2/2
---

## Construction

### Semiconductor material

| Semiconductor material | Junction forward voltage @ 25 °C, V | Electron mobility @ 25 °C, m2/(V·s) | Hole mobility @ 25 °C, m2/(V·s) | Max. junction temp., °C |
|---|---|---|---|---|
| Ge | 0.27 | 0.39 | 0.19 | 70 to 100 |
| Si | 0.71 | 0.14 | 0.05 | 150 to 200 |
| GaAs | 1.03 | 0.85 | 0.05 | 150 to 200 |
| Al–Si junction | 0.3 | — | — | 150 to 200 |

The first BJTs were made from germanium (Ge). Silicon (Si) types currently predominate but certain advanced microwave and high-performance versions now employ the *compound semiconductor* material gallium arsenide (GaAs) and the *semiconductor alloy* silicon–germanium (SiGe). Single-element semiconductor material (Ge and Si) is described as *elemental*.

Rough parameters for the most common semiconductor materials used to make transistors are given in the adjacent table. These parameters will vary with an increase in temperature, electric field, impurity level, strain, and sundry other factors.

The *junction forward voltage* is the voltage applied to the emitter-base junction of a BJT to make the base conduct a specified current. The current increases exponentially as the junction forward voltage is increased. The values given in the table are typical for a current of 1 mA (the same values apply to semiconductor diodes). The lower the junction forward voltage the better, as this means that less power is required to drive the transistor. The junction forward voltage for a given current decreases with an increase in temperature. For a typical silicon junction, the change is −2.1 mV/°C. In some circuits special compensating elements (sensistors) must be used to compensate for such changes.

The density of mobile carriers in the channel of a MOSFET is a function of the electric field forming the channel and of various other phenomena such as the impurity level in the channel. Some impurities, called dopants, are introduced deliberately in making a MOSFET, to control the MOSFET electrical behavior.

The *electron mobility* and *hole mobility* columns show the average speed that electrons and holes diffuse through the semiconductor material with an electric field of 1 volt per meter applied across the material. In general, the higher the electron mobility the faster the transistor can operate. The table indicates that Ge is a better material than Si in this respect. However, Ge has four major shortcomings compared to silicon and gallium arsenide:

1. Its maximum temperature is limited.
2. It has relatively high leakage current.
3. It cannot withstand high voltages.
4. It is less suitable for fabricating integrated circuits.

Because the electron mobility is higher than the hole mobility for all semiconductor materials, a given bipolar n–p–n transistor tends to be swifter than an equivalent p–n–p transistor. GaAs has the highest electron mobility of the three semiconductors. It is for this reason that GaAs is used in high-frequency applications. A relatively recent FET development, the *high-electron-mobility transistor* (HEMT), has a heterostructure (junction between different semiconductor materials) of aluminium gallium arsenide (AlGaAs)-gallium arsenide (GaAs) which has twice the electron mobility of a GaAs-metal barrier junction. Because of their high speed and low noise, HEMTs are used in satellite receivers working at frequencies around 12 GHz. HEMTs based on gallium nitride and aluminum gallium nitride (AlGaN/GaN HEMTs) provide still higher electron mobility and are being developed for various applications.

Maximum junction temperature values represent a cross-section taken from various manufacturers' datasheets. This temperature should not be exceeded or the transistor may be damaged.

*Al–Si junction* refers to the high-speed (aluminum-silicon) metal–semiconductor barrier diode, commonly known as a Schottky diode. This is included in the table because some silicon power IGFETs have a parasitic reverse Schottky diode formed between the source and drain as part of the fabrication process. This diode can be a nuisance, but sometimes it is used in the circuit.

### Packaging

Discrete transistors can be individually packaged transistors or unpackaged transistor chips.

Transistors come in many different semiconductor packages (see image). The two main categories are *through-hole* (or *leaded*), and *surface-mount*, also known as *surface-mount device* (SMD). The *ball grid array* (BGA) is the latest surface-mount package. It has solder balls on the underside in place of leads. Because they are smaller and have shorter interconnections, SMDs have better high-frequency characteristics but lower power ratings.

Transistor packages are made of glass, metal, ceramic, or plastic. The package often dictates the power rating and frequency characteristics. Power transistors have larger packages that can be clamped to heat sinks for enhanced cooling. Additionally, most power transistors have the collector or drain physically connected to the metal enclosure. At the other extreme, some surface-mount *microwave* transistors are as small as grains of sand.

Often a given transistor type is available in several packages. Transistor packages are mainly standardized, but the assignment of a transistor's functions to the terminals is not: other transistor types can assign other functions to the package's terminals. Even for the same transistor type the terminal assignment can vary (normally indicated by a suffix letter to the part number, q.e. BC212L and BC212K).

Nowadays most transistors come in a wide range of SMT packages. In comparison, the list of available through-hole packages is relatively small. Here is a short list of the most common through-hole transistors packages in alphabetical order: ATV, E-line, MRT, HRT, SC-43, SC-72, TO-3, TO-18, TO-39, TO-92, TO-126, TO220, TO247, TO251, TO262, ZTX851.

Unpackaged transistor chips (die) may be assembled into hybrid devices. The IBM SLT module of the 1960s is one example of such a hybrid circuit module using glass passivated transistor (and diode) die. Other packaging techniques for discrete transistors as chips include *direct chip attach* (DCA) and *chip-on-board* (COB).

#### Flexible transistors

Researchers have made several kinds of flexible transistors, including organic field-effect transistors. Flexible transistors are useful in some kinds of flexible displays and other flexible electronics.
