---
title: "Logic family"
source: https://en.wikipedia.org/wiki/Logic_family
domain: level-shifters
license: CC-BY-SA-4.0
tags: level shifter, logic level, open collector, logic family
fetched: 2026-07-02
---

# Logic family

In computer engineering, a **logic family** is one of two related concepts:

- A logic family of monolithic digital integrated circuit devices is a group of electronic logic gates constructed using one of several different designs, usually with compatible logic levels and power supply characteristics within a family. Many logic families were produced as individual components, each containing one or a few related basic logical functions, which could be used as "building-blocks" to create systems or as so-called "glue" to interconnect more complex integrated circuits.
- A logic family may also be a set of techniques used to implement logic within VLSI integrated circuits such as central processors, memories, or other complex functions. Some such logic families use static techniques to minimize design complexity. Other such logic families, such as domino logic, use clocked dynamic techniques to minimize size, power consumption and delay.

Before the widespread use of integrated circuits, various solid-state and vacuum-tube logic systems were used but these were never as standardized and interoperable as the integrated-circuit devices. The most common logic family in modern semiconductor devices is metal–oxide–semiconductor (MOS) logic, due to low power consumption, small transistor sizes, and high transistor density.

## Technologies

The list of packaged building-block logic families can be divided into categories, listed here in roughly chronological order of introduction, along with their usual abbreviations:

- Resistor–transistor logic (RTL)
  - Direct-coupled transistor logic (DCTL)
  - Direct-coupled unipolar transistor logic (DCUTL)
  - Resistor–capacitor–transistor logic (RCTL)
- Emitter-coupled logic (ECL)
  - Positive emitter-coupled logic (PECL)
  - Low-voltage PECL (LVPECL)
  - Complementary transistor micrologic (CTuL)
- Diode–transistor logic (DTL)
  - Complemented transistor diode logic (CTDL)
  - High-threshold logic (HTL)
- Transistor–transistor logic (TTL)
- Metal–oxide–semiconductor (MOS) logic
  - P-type MOS (PMOS) logic
  - N-type MOS (NMOS) logic
    - Depletion-load NMOS logic
    - High-density NMOS (HMOS)
  - Complementary MOS (CMOS) logic
  - Bipolar MOS (BiMOS) logic
    - Bipolar CMOS (BiCMOS)
- Integrated injection logic (I2L)
- Gunning transceiver logic (GTL)

The families RTL, DTL, and ECL were derived from the logic circuits used in early computers, originally implemented using discrete components. One example is the Philips NORBIT family of logic building blocks.

The PMOS and I2L logic families were used for relatively short periods, mostly in special purpose custom large-scale integration circuits devices, and are generally considered obsolete. For example, early digital clocks or electronic calculators may have used one or more PMOS devices to provide most of the logic for the finished product. The F-14 Central Air Data Computer, Intel 4004, Intel 4040, and Intel 8008 microprocessors and their support chips were PMOS.

Of these families, only ECL, TTL, NMOS, CMOS, and BiCMOS are currently still in widespread use. ECL is used for very high-speed applications because of its price and power demands, while NMOS logic is mainly used in VLSI circuits applications such as CPUs and memory chips which fall outside of the scope of this article. Present-day "building block" logic gate ICs are based on the ECL, TTL, CMOS, and BiCMOS families.

## Resistor–transistor logic (RTL)

Class of digital circuits built using resistors as the input network and bipolar junction transistors (BJTs) as switching devices.

The Atanasoff–Berry Computer used resistor-coupled vacuum tube logic circuits similar to RTL. Several early transistorized computers (e.g., IBM 1620, 1959) used RTL, where it was implemented using discrete components.

A family of simple resistor–transistor logic integrated circuits was developed at Fairchild Semiconductor for the Apollo Guidance Computer in 1962. Texas Instruments soon introduced its own family of RTL. A variant with integrated capacitors, RCTL, had increased speed, but lower immunity to noise than RTL. This was made by Texas Instruments as their "51XX" series.

## Diode–transistor logic (DTL)

Class of digital circuits in which the logic gating function (e.g., AND) is performed by a diode network and the amplifying function is performed by a transistor.

Diode logic was used with vacuum tubes in the earliest electronic computers in the 1940s including ENIAC. Diode–transistor logic (DTL) was used in the IBM 608, which was the first all-transistorized computer. Early transistorized computers were implemented using discrete transistors, resistors, diodes and capacitors.

The first diode–transistor logic family of integrated circuits was introduced by Signetics in 1962. DTL was also made by Fairchild and Westinghouse. A family of diode logic and diode–transistor logic integrated circuits was developed by Texas Instruments for the D-37C Minuteman II Guidance Computer in 1962, but these devices were not available to the public.

A variant of DTL called "high-threshold logic" incorporated Zener diodes to create a large offset between logic 1 and logic 0 voltage levels. These devices usually ran off a 15 volt power supply and were found in industrial control, where the high differential was intended to minimize the effect of noise.

## PMOS and NMOS logic

P-type MOS (PMOS) logic uses p-channel MOSFETs to implement logic gates and other digital circuits. PMOS logic dominated industry approximately from 1960 to 1970.

N-type MOS (NMOS) logic uses n-channel MOSFETs to implement logic gates and other digital circuits.

For devices of equal current driving capability, n-channel MOSFETs can be made smaller than p-channel MOSFETs, due to p-channel charge carriers (holes) having lower mobility than do n-channel charge carriers (electrons); also, producing only one type of MOSFET on a silicon substrate is cheaper and technically simpler. These were the driving principles in the design of NMOS logic, which uses n-channel MOSFETs exclusively. However, neglecting leakage current, NMOS logic consumes power even when no switching is taking place, unlike CMOS logic.

The MOSFET invented at Bell Labs between 1955 and 1960 had both pMOS and nMOS devices with a 20 μm process. Their original MOSFET devices had a gate length of 20 μm and a gate oxide thickness of 100 nm. However, the nMOS devices were impractical, and only the pMOS type were practical working devices. A more practical NMOS process was developed several years later. NMOS was initially faster than CMOS, thus NMOS was more widely used for computers in the 1970s.

With advances in technology, CMOS logic displaced NMOS logic in the mid-1980s to become the preferred process for digital chips.

## Emitter-coupled logic (ECL)

1961 IBM invented ECL (also known as current-mode logic (CML)) as current steering logic for use in the transistorized IBM 7030 Stretch computer, where it was implemented using discrete components. In 1962 Motorolla introduced their first line of ECL integrated circuit devices referred to as *MECL 10000.* MECL required negative power supply. A subsequent development of ECL using positive-supply includes later *PECL* and *LVPECL*.

ECL uses an overdriven bipolar junction transistor (BJT) differential amplifier with single-ended input and limited emitter current.

## Transistor–transistor logic (TTL)

In TTL logic, bipolar junction transistors (BJTs) perform the logic and amplifying functions.

The first transistor–transistor logic family of integrated circuits was introduced by Sylvania as *Sylvania Universal High–Level Logic* (SUHL) in 1963. Texas Instruments introduced the 7400 series TTL family in 1964. Transistor–transistor logic uses bipolar transistors to form its integrated circuits. TTL has changed significantly over the years, with newer versions replacing the older types.

Since the transistors of a standard TTL gate are saturated switches, minority carrier storage time in each junction limits the switching speed of the device. Variations on the basic TTL design are intended to reduce these effects and improve speed, power consumption, or both.

The German physicist Walter H. Schottky formulated a theory predicting the **Schottky effect**, which led to the Schottky diode and later Schottky transistors. For the same power dissipation, Schottky transistors have a faster switching speed than conventional transistors because the Schottky diode prevents the transistor from saturating and storing charge; see Baker clamp. Logic gates built with Schottky transistors switch faster than TTL gates built with ordinary BJTs but consume more power. With **Low-power Schottky** (LS), internal resistance values were increased to reduce power consumption and increase switching speed over the original version. The introduction of **Advanced Low-power Schottky** (ALS) further increased speed and reduced power consumption. A faster logic family called **FAST** (Fairchild Advanced Schottky TTL) (Schottky) (F) was also introduced that was faster than original Schottky TTL.

## Complementary MOS (CMOS) logic

CMOS logic gates use complementary arrangements of enhancement-mode N-channel and P-channel field effect transistor. Since the initial devices used oxide-isolated metal gates, they were called **CMOS** (complementary metal–oxide–semiconductor logic). In contrast to TTL, CMOS uses almost no power in the static state (that is, when inputs are not changing). A CMOS gate draws no current other than leakage when in a steady 1 or 0 state. When the gate switches states, current is drawn from the power supply to charge the capacitance at the output of the gate. This means that the current draw of CMOS devices increases with switching rate (controlled by clock speed, typically).

The first CMOS family of logic integrated circuits was introduced by RCA as *CD4000 COS/MOS*, the 4000 series, in 1968. Initially CMOS logic was slower than LS-TTL. However, because the logic thresholds of CMOS were proportional to the power supply voltage, CMOS devices were well-adapted to battery-operated systems with simple power supplies. CMOS gates can also tolerate much wider voltage ranges than TTL gates because the logic thresholds are (approximately) proportional to power supply voltage, and not the fixed levels required by bipolar circuits.

The required silicon area for implementing such digital CMOS functions has rapidly shrunk. VLSI technology incorporating millions of basic logic operations onto one chip, almost exclusively uses CMOS. The extremely small capacitance of the on-chip wiring caused an increase in performance by several orders of magnitude. On-chip clock rates as high as 4 GHz have become common, approximately 1000 times faster than the technology by 1970.

### Lowering the power supply voltage

CMOS chips often work with a broader range of power supply voltages than other logic families. Early TTL ICs required a power supply voltage of 5V, but early CMOS could use 3 to 15V. Lowering the supply voltage reduces the charge stored on any capacitances and consequently reduces the energy required for a logic transition. Reduced energy implies less heat dissipation. The energy stored in a capacitance *C* and changing *V* volts is ½ *CV*2. By lowering the power supply from 5V to 3.3V, switching power was reduced by almost 60 percent (power dissipation is proportional to the square of the supply voltage). Many motherboards have a voltage regulator module to provide the even lower power supply voltages required by many CPUs.

### HC logic

Because of the incompatibility of the CD4000 series of chips with the previous TTL family, a new standard emerged which combined the best of the TTL family with the advantages of the CD4000 family. It was known as the 74HC (which used anywhere from 3.3V to 5V power supplies (and used logic levels relative to the power supply)), and with devices that used 5V power supplies and TTL logic levels. The letters "HC" stand for "High-speed CMOS".

### The CMOS–TTL logic level problem

Interconnecting any two logic families often required special techniques such as additional pull-up resistors, or purpose-built interface circuits, since the logic families may use different voltage levels to represent 1 and 0 states, and may have other interface requirements only met within the logic family.

TTL logic levels are different from those of CMOS – generally a TTL output does not rise high enough to be reliably recognized as a logic 1 by a CMOS input. This problem was solved by the invention of the 74HCT family of devices that uses CMOS technology but TTL input logic levels. These devices only work with a 5V power supply. They form a replacement for TTL, although HCT is slower than original TTL (HC logic has about the same speed as original TTL).

### Other CMOS families

Other CMOS circuit families within integrated circuits include cascode voltage switch logic (CVSL) and pass transistor logic (PTL) of various sorts. These are generally used "on-chip" and are not delivered as building-block medium-scale or small-scale integrated circuits.

## Bipolar CMOS (BiCMOS) logic

One major improvement was to combine CMOS inputs and TTL drivers to form of a new type of logic devices called BiCMOS logic, of which the LVT and ALVT logic families are the most important. The BiCMOS family has many members, including ABT logic, ALB logic, ALVT logic, BCT logic and LVT logic.

### Improved versions

With HC and HCT logic and LS-TTL logic competing in the market it became clear that further improvements were needed to create the *ideal* logic device that combined high speed, with low power dissipation and compatibility with older logic families. A whole range of newer families has emerged that use CMOS technology. A short list of the most important family designators of these newer devices includes:

- LV logic (lower supply voltage)
- LVT logic (lower supply voltage while retaining TTL logic levels)
- ALVT logic (an 'advanced' version of LVT logic)

There are many others including AC/ACT logic, AHC/AHCT logic, ALVC logic, AUC logic, AVC logic, CBT logic, CBTLV logic, FCT logic and LVC logic (LVCMOS).

## Integrated injection logic (IIL)

The integrated injection logic (IIL or I2L) uses bipolar transistors in a current-steering arrangement to implement logic functions. It was used in some integrated circuits, but it is now considered obsolete.

## Monolithic integrated circuit logic families compared

The following logic families would either have been used to build up systems from functional blocks such as flip-flops, counters, and gates, or else would be used as "glue" logic to interconnect very-large scale integration devices such as memory and processors. Not shown are some early obscure logic families from the early 1960s such as DCTL (direct-coupled transistor logic), which did not become widely available.

*Propagation delay* is the time taken for a two-input NAND gate to produce a result after a change of state at its inputs. *Toggle speed* represents the fastest speed at which a J-K flip flop could operate. *Power per gate* is for an individual 2-input NAND gate; usually there would be more than one gate per IC package. Values are very typical and would vary slightly depending on application conditions, manufacturer, temperature, and particular type of logic circuit. *Introduction year* is when at least some of the devices of the family were available in volume for civilian uses. Some military applications pre-dated civilian use.

| Family | Description | Propagation delay (ns) | Toggle speed (MHz) | Power per gate @1 MHz (mW) | Typical supply voltage V (range) | Introduction year | Remarks |
|---|---|---|---|---|---|---|---|
| RTL | Resistor–transistor logic | 500 | 4 | 10 | 3.3 | 1963 | the first CPU built from integrated circuits (the Apollo Guidance Computer) used RTL. |
| DTL | Diode–transistor logic | 25 |   | 10 | 5 | 1962 | Introduced by Signetics, Fairchild 930 line became industry standard in 1964 |
| PMOS | MEM 1000 | 300 | 1 | 9 | -27 and -13 | 1967 | Introduced by General Instrument |
| CMOS | AC/ACT | 3 | 125 | 0.5 | 3.3 or 5 (2-6 or 4.5-5.5) | 1985 | ACT has TTL compatible levels |
| CMOS | HC/HCT | 9 | 50 | 0.5 | 5 (2-6 or 4.5-5.5) | 1982 | HCT has TTL compatible levels |
| CMOS | 4000B/74C | 30 | 5 | 1.2 | 10V (3-18) | 1970 | Approximately half speed and power at 5 volts |
| TTL | 7400 1st series | 10 | 25 | 10 | 5 (4.75-5.25) | 1964 | Several manufacturers |
| TTL | L | 33 | 3 | 1 | 5 (4.75-5.25) | 1964 | Low power |
| TTL | H | 6 | 43 | 22 | 5 (4.75-5.25) | 1964 | High speed |
| TTL | S | 3 | 100 | 19 | 5 (4.75-5.25) | 1969 | Schottky high speed |
| TTL | LS | 10 | 40 | 2 | 5 (4.75-5.25) | 1976 | Low power Schottky high speed |
| TTL | ALS | 4 | 50 | 1.3 | 5 (4.5-5.5) | 1976 | Advanced Low power Schottky |
| TTL | F | 3.5 | 100 | 5.4 | 5 (4.75-5.25) | 1979 | Fast |
| TTL | AS | 2 | 105 | 8 | 5 (4.5-5.5) | 1980 | Advanced Schottky |
| TTL | G | 1.5 | 1125 (1.125 GHz) |   | 1.65 - 3.6 | 2004 | First GHz 7400 series logic |
| ECL | ECL III | 1 | 500 | 60 | -5.2(-5.19 - -5.21) | 1968 | Improved ECL |
| ECL | MECL I | 8 |   | 31 | -5.2 | 1962 | first integrated logic circuit commercially produced |
| ECL | ECL 10K | 2 | 125 | 25 | -5.2(-5.19 - -5.21) | 1971 | Motorola |
| ECL | ECL 100K | 0.75 | 350 | 40 | -4.5(-4.2 - -5.2) | 1981 |   |
| ECL | ECL 100KH | 1 | 250 | 25 | -5.2(-4.9 - -5.5) | 1981 |   |

## On-chip design styles

Several techniques and design styles are primarily used in designing large single-chip application-specific integrated circuits (ASIC) and CPUs, rather than generic logic families intended for use in multi-chip applications.

These design styles can typically be divided into two main categories, static techniques and clocked dynamic techniques. (See static versus dynamic logic for some discussion on the advantages and disadvantages of each category).

### Static logic

- Pulsed static CMOS
- Differential cascode voltage switch (DCVS)
- Cascode non-threshold logic (CNTL)
- Pass-gate/transmission-gate logic: pass transistor logic (PTL)
- Complementary pass-gate logic (CPL)
- Push–pull logic
- Output prediction logic (OPL)
- Cascode voltage switch logic (CVSL)

### Dynamic logic

- four-phase logic
- domino logic
- Footless domino
- NORA/zipper logic
- Multiple-output domino
- Compound domino
- Dual-rail domino
- Self-resetting domino
- Sample-set differential logic
- Limited-switch dynamic logic
