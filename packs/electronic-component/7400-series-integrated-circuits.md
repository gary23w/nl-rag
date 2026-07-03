---
title: "7400-series integrated circuits"
source: https://en.wikipedia.org/wiki/7400-series_integrated_circuits
domain: electronic-component
license: CC-BY-SA-4.0
tags: electronic component
fetched: 2026-07-03
---

# 7400-series integrated circuits

The **7400 series** is a popular logic family of transistor–transistor logic (TTL) integrated circuits (ICs).

In 1964, Texas Instruments introduced the SN5400 series of logic chips, in a ceramic semiconductor package. A low-cost plastic package SN7400 series was introduced in 1966 which quickly gained over 50% of the logic chip market, and eventually becoming *de facto* standardized electronic components. Since the introduction of the original bipolar-transistor TTL parts, pin-compatible parts were introduced with such features as low-power CMOS technology and lower supply voltages. Surface mount packages exist for several popular logic family functions.

## Overview

The 7400 series contains hundreds of devices that provide everything from basic logic gates, flip-flops, and counters, to special purpose bus transceivers and arithmetic logic units (ALU). Specific functions are described in a list of 7400 series integrated circuits. Some TTL parts were made with an extended military-specification temperature range. These parts are prefixed with **54** instead of **74** in the part number. The less-common **64** and **84** prefixes on Texas Instruments parts indicated an industrial temperature range. Since the 1970s, new product families have been released to replace the original 7400 series. More recent TTL-compatible logic families were manufactured using CMOS or BiCMOS technology rather than TTL.

| Prefix | Name | Temperature range | Remarks |
|---|---|---|---|
| **54** | Military | −55 °C to +125 °C |   |
| **64** | Industrial | −40 °C to +85 °C | rare |
| **74** | Commercial | 0 °C to +70 °C | most common |
| **84** | Industrial | −25 °C to +85 °C | rare |

Today, surface-mounted CMOS versions of the 7400 series are used in various applications in electronics and for glue logic in computers and industrial electronics. The original through-hole devices in dual in-line packages (DIP/DIL) were the mainstay of the industry for many decades. They are useful for rapid breadboard-prototyping and for education and remain available from most manufacturers. The fastest types and very low voltage versions are typically surface-mount only, however.

The first part number in the series, the 7400, is a 14-pin IC containing four two-input NAND gates. Each gate uses two input pins and one output pin, with the remaining two pins being power (+5 V) and ground. This part was made in various through-hole and surface-mount packages, including flat pack and plastic/ceramic dual in-line. Additional characters in a part number identify the package and other variations.

Unlike the older resistor–transistor logic integrated circuits, bipolar TTL gates were unsuitable to be used as analog devices, providing low gain, poor stability, and low input impedance. Special-purpose TTL devices were used to provide interface functions such as Schmitt triggers or monostable multivibrator timing circuits. Inverting gates could be cascaded as a ring oscillator, useful for purposes where high stability was not required.

### History

Although the 7400 series was the first *de facto* industry standard TTL logic family (i.e. second-sourced by several semiconductor companies), there were earlier TTL logic families such as:

- Sylvania Universal High-level Logic in 1963
- Motorola MC4000 MTTL
- National Semiconductor DM8000
- Fairchild 9300 series
- Signetics 8200 and 8T00

The 7400 quad 2-input NAND gate was the first product in the series, introduced by Texas Instruments in a military grade metal flat package (5400W) in October 1964. The pin assignment of this early series differed from the *de facto* standard set by the later series in DIP packages (in particular, ground was connected to pin 11 and the power supply to pin 4, compared to pins 7 and 14 for DIP packages). The extremely popular commercial grade plastic DIP (7400N) followed in the third quarter of 1966.

The 5400 and 7400 series were used in many popular minicomputers in the 1970s and early 1980s. Some models of the DEC PDP-series "minis" used the 74181 ALU as the main computing element in the CPU. Other examples were the Data General Nova series and Hewlett-Packard 21MX, 1000, and 3000 series.

In 1965, typical quantity-one pricing for the SN5400 (military grade, in ceramic welded flat-pack) was around 22 USD. As of 2007, individual commercial-grade chips in molded epoxy (plastic) packages can be purchased for approximately US$0.25 each, depending on the particular chip.

- (Die of a 74AHC00D, manufactured by NXP) Die of a 74AHC00D, manufactured by NXP
- (SN7400 die in the original flat package, manufactured by TI) SN7400 die in the original flat package, manufactured by TI
- (Die vs Schematic of a NAND gate in a 74H00 (Darlington transistor is visbile on the right)) Die vs Schematic of a NAND gate in a 74H00 (Darlington transistor is visbile on the right)
- (Schematic of one gate in a 7400) Schematic of one gate in a 7400
- (Schematic of one gate in a 74LS00) Schematic of one gate in a 74LS00
- (Schematic of one gate in a 74ALS00) Schematic of one gate in a 74ALS00
- (Size comparison of 74HC00 in DIP vs TSSOP package) Size comparison of 74HC00 in DIP vs TSSOP package

## Families

7400 series parts were constructed using bipolar junction transistors (BJT), forming what is referred to as transistor–transistor logic or **TTL**. Newer series, more or less compatible in function and logic level with the original parts, use CMOS technology or a combination of the two (BiCMOS). Originally the bipolar circuits provided higher speed but consumed more power than the competing 4000 series of CMOS devices. Bipolar devices are also limited to a fixed power-supply voltage, typically 5 V, while CMOS parts often support a range of supply voltages.

Milspec-rated devices for use in extended temperature conditions are available as the 5400 series. Texas Instruments also manufactured radiation-hardened devices with the prefix *RSN*, and the company offered beam-lead bare dies for integration into hybrid circuits with a *BL* prefix designation.

Regular-speed TTL parts were also available for a time in the 6400 series – these had an extended industrial temperature range of −40 °C to +85 °C. While companies such as Mullard listed 6400-series compatible parts in 1970 data sheets, by 1973 there was no mention of the 6400 family in the Texas Instruments *TTL Data Book*. Texas Instruments brought back the 6400 series in 1989 for the SN64BCT540. The SN64BCTxxx series is still in production as of 2023. Some companies have also offered industrial extended temperature range variants using the regular 7400-series part numbers with a prefix or suffix to indicate the temperature grade.

As integrated circuits in the 7400 series were made in different technologies, usually compatibility was retained with the original TTL logic levels and power-supply voltages. An integrated circuit made in CMOS is not a TTL chip, since it uses field-effect transistors (FETs) and not bipolar junction transistors (BJT), but similar part numbers are retained to identify similar logic functions and electrical (power and I/O voltage) compatibility in the different subfamilies.

Over 40 different logic subfamilies use this standardized part number scheme. The headings in the following table are: *V*cc – power-supply voltage; *t*pd – maximum gate delay; *I*OL – maximum output current at low level; *I*OH – maximum output current at high level; *t*pd, *I*OL, and *I*OH apply to most gates in a given family. Driver or buffer gates have higher output currents.

| Code | Family | *V*cc | *t*pd | *I*OL | *I*OH | Year | Description |
|---|---|---|---|---|---|---|---|
| Bipolar TTL families |   |   |   |   |   |   |   |
| 74 | Standard TTL | 5 V ±5% | 22 ns | 16 mA | −0.4 mA | 1966 | The original 7400 logic family. Contains no characters between the "74" and the part number. |
| 74H | High-speed | 5 V ±5% | 10 ns | 20 mA | −0.5 mA | 1967 | Higher speed than the original 74 series, at the expense of power dissipation. TTL logic levels. |
| 74L | Low-power | 5 V ±5% | 60 ns | 3.6 mA | −0.2 mA | 1967 | Same technology as the original 74 family, but with larger resistors to lower power consumption at the expense of gate speed. TTL logic levels. Now obsolete. |
| 74S | Schottky | 5 V ±5% | 5 ns | 20 mA | −1 mA | 1969 | Implemented using Schottky diode. High current draw. TTL logic levels. |
| 74LS | Low-power Schottky | 5 V ±5% | 15 ns | 8 mA | −0.4 mA | 1971 | Same technology as the 74S family, but with lower power consumption (2 mW) at the expense of gate speed. TTL logic levels. |
| 74F | FAST | 5 V ±5% | 3.9 ns | 20 mA | −1 mA | 1978 | Originally Fairchild's version of the 74AS family. TTL logic levels. |
| 74ALS | Advanced low-power Schottky | 5 V ±10% | 11 ns | 8 mA | −0.4 mA | 1980 | Same technology as the 74AS family, but with lower power consumption at the expense of gate speed. TTL logic levels. |
| 74AS | Advanced Schottky | 5 V ±10% | 4.5 ns | 20 mA | −2 mA | 1982 | Same technology as the 74S family, but with "miller killer" circuitry to speed up low-to-high transitions. TTL logic levels. |
| CMOS and BiCMOS families |   |   |   |   |   |   |   |
| 74C | CMOS | 3.0–15 V | 60 ns | 0.36 mA | −0.36 mA | 1975 | 74C is standard CMOS, similar to buffered 4000 (4000B) series. Input levels not compatible with TTL families. The 4000A series was introduced in 1968, the 4000B around 1975. |
| 74HC | High-speed CMOS | 2.0–6.0 V | 15 ns | 4 mA | −4 mA | 1983? | Similar performance to 74LS. CMOS logic levels. |
| 74HCT | High-speed CMOS | 5 V ±10% | 15 ns | 4.8 mA | −4.8 mA | 1983? | Similar performance to 74LS. TTL logic levels. |
| 74HCTLS | High-speed CMOS | 5 V ±10% | 15 ns | 8 mA | −4 mA | 1988? | Samsung's version of the 74HCT series. TTL logic levels. |
| 74HCS | Schmitt-trigger integrated high-speed CMOS | 2.0–6.0 V | 13 ns | 7.8 mA | −7.8 mA | 2019? | Schmitt triggers on all inputs. CMOS logic levels. |
| 74AHC | Advanced high-speed CMOS | 2.0–5.5 V | 5.5 ns | 8 mA | −8 mA |   | Up to three times as fast as the 74HC family. 5 V tolerant inputs. CMOS logic levels. Equivalent to 74VHC. |
| 74AHCT | Advanced high-speed CMOS | 5 V ±10% | 6.9 ns | 8 mA | −8 mA | 1986? | Up to three times as fast as the 74HCT family. TTL logic levels. Equivalent to 74VHCT. |
| 74VHC | Very high-speed CMOS | 2.0–5.5 V | 5.5 ns | 8 mA | −8 mA | 1992? | 5 V tolerant inputs. Equivalent to 74AHC. CMOS logic levels. |
| 74VHCT | Very high-speed CMOS | 5 V ±10% | 6.9 ns | 8 mA | −8 mA | 1995? | Equivalent to 74AHCT. TTL logic levels. |
| 74AC | Advanced CMOS | 2.0–6.0 V | 8 ns | 24 mA | −24 mA | 1985 | CMOS logic levels. Outputs may cause ground bounce. |
| 74ACT | Advanced CMOS | 5 V ±10% | 8 ns | 24 mA | −24 mA | 1985 | TTL logic levels. Outputs may cause ground bounce. |
| 74ACQ | Advanced CMOS with "quiet" outputs | 2.0–6.0 V | 6.5 ns | 24 mA | −24 mA | 1989 | Fairchild's "Quiet Series" offering lower ringing and ground bounce on state transitions. Bus interface circuits only in this family. CMOS logic levels. |
| 74ACTQ | Advanced CMOS with "quiet" outputs | 5 V ±10% | 7.5 ns | 24 mA | −24 mA | 1989 | Fairchild's "Quiet Series" offering lower ringing and ground bounce on state transitions. TTL logic levels. |
| 74ABT | Advanced BiCMOS | 5 V ±10% | 3.6 ns | 20 mA | −15 mA | 1991? | TTL logic levels. |
| 74LVCE | Low-voltage CMOS | 1.4–5.5 V | 3.6 ns | 32 mA | −32 mA | 2010? | CMOS logic levels. 5 V tolerant inputs. Extended supply voltage range and higher speed compared to 74LVC. |
| Low-voltage CMOS and BiCMOS families |   |   |   |   |   |   |   |
| 74LVT | Low-voltage BiCMOS | 2.7–3.6 V | 4.1 ns | 32 mA | −20 mA | 1992 | TTL logic levels, 5 V tolerant inputs and outputs. Note, original 1992 LVTs had bus-hold. However a 1996 redesign of LVT emphasized performance, so 1992 LVTs were renamed LVTH to denote the bus-hold feature explicitly in the device name. LVTH also added the high impedance during power up/down feature. |
| 74LVQ | Low-voltage quiet CMOS | 2.0–3.6 V | 9.5 ns | 12 mA | −12 mA | 1992 | TTL logic levels. Guaranteed incident-wave switching for 75 Ω lines. |
| 74LV | Low-voltage CMOS | 2.7–3.6 V | 18 ns | 6 mA | −6 mA | 1993? | TTL logic levels. |
| 74LVC | Low-voltage CMOS | 2.0–3.6 V | 6 ns | 24 mA | −24 mA | 1993? | TTL logic levels, 5 V tolerant inputs. |
| 74ALVC | Advanced low-voltage CMOS | 1.65–3.6 V | 3.0 ns | 24 mA | −24 mA | 1994? | 3.3 V tolerant inputs and outputs. |
| 74VCX | Advanced low-voltage CMOS | 1.20–3.6 V | 3.1 ns | 24 mA | −24 mA | 1997 | Fairchild's version of 74ALVC. 3.3 V tolerant inputs and outputs. |
| 74LCX | Low-voltage high-speed CMOS | 2.0–3.6 V | 4.3 ns | 24 mA | −24 mA | 1994 | Fairchild's version of 74LVC. TTL logic levels. 5 V tolerant inputs and outputs. |
| 74LVX | Low-voltage high-speed CMOS | 2.0–3.6 V | 9.7 ns | 4 mA | −4 mA | 1994? | TTL logic levels. 5 V tolerant inputs. Faster than 74VHC at low voltages. |
| 74AUP | Advanced ultra-low-power | 0.80–3.6 V | 3.8 ns | 4 mA | −4 mA | 2004? | 3.3 V tolerant hysteresis inputs. |
| 74G | Gigahertz | 1.65–3.6 V | 1.5 ns | 12 mA | −12 mA | 2006 | Speeds over 1 gigahertz with 5 V tolerant inputs. |
| Very-low-voltage CMOS families |   |   |   |   |   |   |   |
| 74AUC | Advanced ultra-low-voltage CMOS | 0.80–2.7 V | 2.0 ns | 9 mA | −9 mA | 2002? | 3.3 V tolerant inputs. |
| Limited families for special applications |   |   |   |   |   |   |   |
| 74SC | Standard CMOS | 5 V ±5% | 30 ns | 10 mA | −10 mA | 1981? | Performance like standard TTL at lower power consumption (intermediate step between 74C and 74HC). No simple gates in this family. |
| 74FCT | Fast CMOS | 5 V ±5% | 7 ns | 64 mA | −15 mA | 1986? | Manufactured in CMOS or BiCMOS technology. Performance like 74F at lower power consumption. No simple gates in this family. |
| 74BCT | BiCMOS | 5 V ±10% | 6.6 ns | 64 mA | −15 mA | 1988? | TTL logic levels. Bus interface circuits only in this family. |
| 74FBT | Fast BiCMOS | 5 V ±10% | 4.1 ns | 64 mA | −24 mA | 1990? | Bus interface circuits only in this family. |
| 74FB | Futurebus | 5 V ±5% | 5 ns | 80 mA | – | 1992? | Futurebus+ interface circuits only in this family. |
| 74GTL | Gunning transceiver logic | 5 V ±5% | 4 ns | 64 mA | −32 mA | 1993? | Bus interface circuits only in this family. |
| 74GTLP | Gunning transceiver logic plus | 3.15–3.45 V | 7.5 ns | 50 mA | – | 1996 | Bus interface circuits only in this family. Fairchild's improved version of 74GTL (higher bus speed, lower ground bounce). |
| 74CBT | Crossbar switch | 5 V ±10% | 0.25 ns | 64 mA | −15 mA | 1992? | FET bus switches only in this family. |
| 74FST | Crossbar switch | 5 V ±5% | 0.25 ns | 30 mA | −15 mA | 1995? | FET bus switches only in this family. IDT's version of 74CBT. |
| 74CBTLV | Crossbar switch low-voltage | 2.3–3.6 V | 0.25 ns | 64 mA | −15 mA | 1997? | FET bus switches only in this family. |
| 74ALB | Advanced low-voltage BiCMOS | 3.0–3.6 V | 2.0 ns | 25 mA | −25 mA | 1996? | Bus interface circuits only in this family. |
| 74LPT | Low-voltage CMOS | 2.7–3.6 V | 4.1 ns | 24 mA | −24 mA | 1996? | Bus interface circuits only in this family. 5 V tolerant inputs. |
| 74AVC | Advanced very-low-voltage CMOS | 1.40–3.6 V | 1.7 ns | 12 mA | −12 mA | 1998? | 3.3 V tolerant inputs. Bus interface circuits only in this family. |
| 74ALVT | Advanced low-voltage BiCMOS | 2.3–3.6 V | 2.5 ns | 64 mA | −32 mA | 1999? | 5 V tolerant inputs and outputs. Bus interface circuits only in this family. |
| 74AHCV | Advanced high-speed CMOS | 1.8–5.5 V | 7.5 ns | 16 mA | −16 mA | 2016? | CMOS logic levels. 5 V tolerant inputs. Extended supply voltage range and higher speed compared to 74AHC. Bus interface circuits only in this family. See also 74LVCE. |
| 74AXC | Advanced extremely-low-voltage CMOS | 0.65–3.6 V | 4 ns | 12 mA | −12 mA | 2018? | 3.3 V tolerant inputs. Bus interface circuits only in this family. |
| 74LXC | Low-voltage CMOS | 1.1–5.5 V | 7 ns | 32 mA | −32 mA | 2019? | Extended supply voltage range compared to 74LVC. Bus interface circuits only in this family. See also 74LVCE. |

1. A question mark indicates that the year of introduction is based on the earliest data sheet or the revision history in a data sheet.
2. Parameters are shown for the 2-input NAND gate (74x00 or 74x1G00) at *V*cc = 5 V,Ta = 25 °C, CL = 50 pF.
3. The letter "U" when added to the family code (e.g. 74HCU) indicates an unbuffered CMOS circuit. Typically, there is only one unbuffered circuit in a family: the hex inverter (74x04). Unbuffered circuits are intended for analogue applications such as crystal oscillators.
4. The letter "H" when added to the family code (e.g. 74LVCH) indicates a circuit with a bus-hold feature. That is, if the input bus goes to a high-impendance or floating state then the outputs keep their state according to the last valid input state. This eliminates the need for pull-up resistors or pull-down resistors. "H" can also be combined with "R" (e.g. 74ALVCHR).
5. The letter "R" when added to the family code (e.g. 74LCXR) indicates a circuit with integrated resistors at the outputs in order to reduce overshoot and undershoot of the output signal.
6. Parameters are shown for the 2-input NAND gate (74x00 or 74x1G00) at Vcc = 3.3 V,Ta = 25 °C, CL = 50 pF.
7. The letter "Z" when added to the family code (e.g. 74LVTZ) indicates a circuit where a high-impedance state of all outputs is guaranteed when the power supply voltage drops below a certain threshold.
8. There are no simple gates in these families. Parameters are for a transceiver (74x245, 74x16245, or similar).
9. B-side outputs are all open-collector in this family.

Many parts in the CMOS HC, AC, AHC, and VHC families are also offered in "T" versions (HCT, ACT, AHCT and VHCT) which have input thresholds that are compatible with both TTL and 3.3 V CMOS signals. The non-T parts have conventional CMOS input thresholds, which are more restrictive than TTL thresholds. Typically, CMOS input thresholds require high-level signals to be at least 70% of Vcc and low-level signals to be at most 30% of Vcc. (TTL has the input high level above 2.0 V and the input low level below 0.8 V, so a TTL high-level signal could be in the forbidden middle range for 5 V CMOS.)

The 74H family is the same basic design as the 7400 family with resistor values reduced. This reduced the typical propagation delay from 9 ns to 6 ns but increased the power consumption. The 74H family provided a number of unique devices for CPU designs in the 1970s. Many designers of military and aerospace equipment used this family over a long period and as they need exact replacements, this family is still produced by Lansdale Semiconductor.

The 74S family, using Schottky circuitry, uses more power than the 74, but is faster. The 74LS family of ICs is a lower-power version of the 74S family, with slightly higher speed but lower power dissipation than the original 74 family; it became the most popular variant once it was widely available. Many 74LS ICs can be found in microcomputers and digital consumer electronics manufactured in the 1980s and early 1990s.

The 74F family was introduced by Fairchild Semiconductor and adopted by other manufacturers; it is faster than the 74, 74LS and 74S families.

Through the late 1980s and 1990s newer versions of this family were introduced to support the lower operating voltages used in newer CPU devices.

| Parameter | 74C | 74HC | 74AC | 74HCT | 74ACT | Units |
|---|---|---|---|---|---|---|
| *V*IH (min) | 3.5 | 2.0 | V |   |   |   |
| *V*OH (min) | 4.5 | 4.9 | V |   |   |   |
| *V*IL (max) | 1.5 | 1.0 | 1.5 | 0.8 | V |   |
| *V*OL (max) | 0.5 | 0.1 | V |   |   |   |
| *I*IH (max) | 1 | μA |   |   |   |   |
| *I*IL (max) | 1 | μA |   |   |   |   |
| *I*OH (max) | 0.4 | 4.0 | 24 | 4.0 | 24 | mA |
| *I*OL (max) | 0.4 | 4.0 | 24 | 4.0 | 24 | mA |
| *t*P (max) | 50 | 8 | 4.7 | 8 | 4.7 | ns |

## Part numbering

Part number schemes varied by manufacturer. The part numbers for 7400-series logic devices often use the following designators:

- Often first, a two or three letter prefix, denoting the manufacturer and flow class of the device. These codes are no longer closely associated with a single manufacturer, for example, Fairchild Semiconductor manufactures parts with MM and DM prefixes, and no prefixes. Examples:
  - SN: Texas Instruments using a commercial processing
  - SNV: Texas Instruments using military processing
  - M: ST Microelectronics
  - DM: National Semiconductor
  - UT: Cobham PLC
  - SG: Sylvania
  - RD: RIFA AB
- Two digits for temperature range. Examples:
  - 54: military temperature range
  - 64: short-lived historical series with intermediate "industrial" temperature range
  - 74: commercial temperature range device
- Zero to four letters denoting the logic subfamily. Examples:
  - zero letters: basic bipolar TTL
  - LS: low-power Schottky
  - HCT: High-speed CMOS compatible with TTL
- Two or more arbitrarily assigned digits that identify the function of the device. There are hundreds of different devices in each family.
- Additional suffix letters and numbers may be appended to denote the package type, quality grade, or other information, but this varies widely by manufacturer.

For example, "SN5400N" signifies that the part is a 7400-series IC probably manufactured by Texas Instruments ("SN" originally meaning "Semiconductor Network") using commercial processing, is of the military temperature rating ("54"), and is of the TTL family (absence of a family designator), its function being the *quad 2-input NAND gate* ("00") implemented in a plastic through-hole DIP package ("N").

Many logic families maintain a consistent use of the device numbers as an aid to designers. Often a part from a different 74x00 subfamily could be substituted ("drop-in replacement") in a circuit, with the same function and pin-out yet more appropriate characteristics for an application (perhaps speed or power consumption), which was a large part of the appeal of the 74C00 series over the competing CD4000B series, for example. But there are a few exceptions where incompatibilities (mainly in pin-out) across the subfamilies occurred, such as:

- some flat-pack devices (e.g. 7400W) and surface-mount devices,
- some of the faster CMOS series (for example 74AC),
- a few low-power TTL devices (e.g. 74L86, 74L9 and 74L95) have a different pin-out than the regular (or even 74LS) series part.
- five versions of the 74x54 (4-wide AND-OR-INVERT gates IC), namely 7454(N), 7454W, 74H54, 74L54W and 74L54N/74LS54, are different from each other in pin-out and/or function,

## Second sources from Europe and Eastern Bloc

Some manufacturers, such as Mullard and Siemens, had pin-compatible TTL parts, but with a completely different numbering scheme; however, data sheets identified the *7400-compatible* number as an aid to recognition.

At the time the 7400 series was being made, some European manufacturers (that traditionally followed the Pro Electron naming convention), such as Philips/Mullard, produced a series of TTL integrated circuits with part names beginning with FJ. Some examples of FJ series are:

- FJH101 (=7430) single 8-input NAND gate,
- FJH131 (=7400) quadruple 2-input NAND gate,
- FJH181 (=7454N or J) 2+2+2+2 input AND-OR-NOT gate.

The Soviet Union started manufacturing TTL ICs with 7400-series pinout in the late 1960s and early 1970s, such as the K155ЛA3, which was pin-compatible with the 7400 part available in the United States, except for using a metric spacing of 2.5 mm between pins instead of the 0.1 inches (2.54 mm) pin-to-pin spacing used in the west. Another peculiarity of the Soviet-made 7400 series was the packaging material used in the 1970s–1980s. Instead of the ubiquitous black resin, they had a brownish-green body colour with subtle swirl marks created during the moulding process. It was jokingly referred to in the Eastern Bloc electronics industry as the "elephant-dung packaging", due to its appearance.

The Soviet integrated circuit designation is different from the Western series:

- the technology modifications were considered different series and were identified by different numbered prefixes – К155 series is equivalent to plain 74, К555 series is 74LS, К1533 is 74ALS, etc.;
- the function of the unit is described with a two-letter code followed by a number:
  - the first letter represents the functional group – logical, triggers, counters, multiplexers, etc.;
  - the second letter shows the functional subgroup, making the distinction between logical NAND and NOR, D- and JK-triggers, decimal and binary counters, etc.;
  - the number distinguishes variants with different number of inputs or different number of elements within a die – ЛА1/ЛА2/ЛА3 (LA1/LA2/LA3) are 2 four-input / 1 eight-input / 4 two-input NAND elements respectively (equivalent to 7420/7430/7400).

Before July 1974 the two letters from the functional description were inserted after the first digit of the series. Examples: К1ЛБ551 and К155ЛА1 (7420), К1ТМ552 and К155ТМ2 (7474) are the same ICs made at different times.

Clones of the 7400 series were also made in other Eastern Bloc countries:

- Bulgaria (Mikroelektronika Botevgrad) used a designation somewhat similar to that of the Soviet Union, e.g. *1ЛБ00ШМ* (1LB00ShM) for a 74LS00. Some of the two-letter functional groups were borrowed from the Soviet designation, while others differed. Unlike the Soviet scheme, the two or three digit number after the functional group matched the western counterpart. The series followed at the end (i.e. *ШМ* for LS). Only the LS series is known to have been manufactured in Bulgaria.
- Czechoslovakia (TESLA) used the 7400 numbering scheme with manufacturer prefix MH. Example: MH7400. Tesla also produced industrial grade (8400, −25 ° to 85 °C) and military grade (5400, −55 ° to 125 °C) ones.
- Poland (Unitra CEMI) used the 7400 numbering scheme with manufacturer prefixes UCA for the 5400 and 6400 series, as well as UCY for the 7400 series. Examples: UCA6400, UCY7400. Note that ICs with the prefix MCY74 correspond to the 4000 series (e.g. MCY74002 corresponds to 4002 and not to 7402).
- Hungary (Tungsram, later Mikroelektronikai Vállalat / MEV) also used the 7400 numbering scheme, but with manufacturer suffix – 7400 is marked as 7400APC.
- Romania (I.P.R.S.) used a trimmed 7400 numbering with the manufacturer prefix CDB (example: CDB4123E corresponds to 74123) for the 74 and 74H series, where the suffix *H* indicated the 74H series. For the later 74LS series, the standard numbering was used.
- East Germany (HFO) also used trimmed 7400 numbering without manufacturer prefix or suffix. The prefix D (or E) designates digital IC, and not the manufacturer. Example: D174 is 7474. 74LS clones were designated by the prefix DL; e.g. DL000 = 74LS00. In later years East German made clones were also available with standard 74* numbers, usually for export.

A number of different technologies were available from the Soviet Union, Czechoslovakia, Poland, and East Germany. The 8400 series in the table below indicates an industrial temperature range from −25 °C to +85 °C (as opposed to −40 °C to +85 °C for the 6400 series).

Prefixes of Eastern European series

Soviet Union

Czechoslovakia

Poland

East Germany

5400

7400

5400

7400

8400

5400

6400

7400

6400

7400

8400

74

133

К155

MH54

MH74

MH84

UCA54

UCA64

UCY74

D1

E1

74L

134,

136

КР134, К158

74H

130

К131

UCA64H

UCY74H

D2

E2

74S

530

КР531

MH54S

MH74S

MH84S

UCY74S

DS

74LS

533

К555

UCY74LS

DL...D

DL...DG

74AS

1530

КР1530

74ALS

1533

КР1533

MH54ALS

MH74ALS

74F

1531

КР1531

74HC

1564

КР1564

74HCT

5564

U74HCT...DK

74AC

1554

КР1554

74ACT

1594

КР1594

74LVC

5574

74VHC

5584

1. The pin assignment of the 134 series mostly follows Texas Instruments' original flat-pack series, i.e. ground on pin 11 and power on pin 4.

Around 1990 the production of standard logic ceased in all Eastern European countries except the Soviet Union and later Russia and Belarus. As of 2016, the series 133, К155, 1533, КР1533, 1554, 1594, and 5584 were in production at "Integral" in Belarus, as well as the series 130 and 530 at "NZPP-KBR", 134 and 5574 at "VZPP", 533 at "Svetlana", 1564, К1564, КР1564 at "NZPP", 1564, К1564 at "Voshod", 1564 at "Exiton", and 133, 530, 533, 1533 at "Mikron" in Russia. The Russian company Angstrem manufactures 54HC circuits as the 5514БЦ1 series, 54AC as the 5514БЦ2 series, and 54LVC as the 5524БЦ2 series. As of 2024, the 133, 136, and 1533 series are in production at Kvazar Kyiv in Ukraine.
