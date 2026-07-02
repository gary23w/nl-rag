---
title: "Pressure measurement (part 2/2)"
source: https://en.wikipedia.org/wiki/Bourdon_tube
domain: pressure-sensors
license: CC-BY-SA-4.0
tags: pressure sensor, piezoresistive effect, bourdon tube, barometer
fetched: 2026-07-02
part: 2/2
---

## Electronic pressure instruments

**Metal strain gauge**

The

strain gauge

is generally glued (foil strain gauge) or deposited (thin-film strain gauge) onto a membrane. Membrane deflection due to pressure causes a resistance change in the strain gauge which can be electronically measured.

**Piezoresistive strain gauge**

Uses the

piezoresistive

effect of bonded or formed strain gauges to detect strain due to applied pressure.

**Piezoresistive silicon pressure sensor**

The sensor is generally a temperature compensated,

piezoresistive

silicon pressure sensor chosen for its excellent performance and long-term stability. Integral temperature compensation is provided over a range of 0–50

°C using

laser-trimmed

resistors. An additional laser-trimmed resistor is included to normalize pressure sensitivity variations by programming the gain of an external differential amplifier. This provides good sensitivity and long-term stability. The two ports of the sensor, apply pressure to the same single transducer, please see pressure flow diagram below.

This is an over-simplified diagram, but you can see the fundamental design of the internal ports in the sensor. The important item here to note is the "diaphragm" as this is the sensor itself. Is it slightly convex in shape (highly exaggerated in the drawing); this is important as it affects the accuracy of the sensor in use.

The shape of the sensor is important because it is calibrated to work in the direction of air flow as shown by the RED arrows. This is normal operation for the pressure sensor, providing a positive reading on the display of the digital pressure meter. Applying pressure in the reverse direction can induce errors in the results as the movement of the air pressure is trying to force the diaphragm to move in the opposite direction. The errors induced by this are small, but can be significant, and therefore it is always preferable to ensure that the more positive pressure is always applied to the positive (+ve) port and the lower pressure is applied to the negative (-ve) port, for normal 'gauge pressure' application. The same applies to measuring the difference between two vacuums, the larger vacuum should always be applied to the negative (-ve) port. The measurement of pressure via the Wheatstone Bridge looks something like this....

The effective electrical model of the transducer, together with a basic signal conditioning circuit, is shown in the application schematic. The pressure sensor is a fully active Wheatstone bridge which has been temperature compensated and offset adjusted by means of thick film, laser trimmed resistors. The excitation to the bridge is applied via a constant current. The low-level bridge output is at +O and -O, and the amplified span is set by the gain programming resistor (r). The electrical design is microprocessor controlled, which allows for calibration, the additional functions for the user, such as Scale Selection, Data Hold, Zero and Filter functions, the Record function that stores/displays MAX/MIN.

**Capacitive**

Uses a diaphragm and pressure cavity to create a variable

capacitor

to detect strain due to applied pressure.

**Magnetic**

Measures the displacement of a diaphragm by means of changes in

inductance

(reluctance),

LVDT

,

Hall effect

, or by

eddy current

principle.

**Piezoelectric**

Uses the

piezoelectric

effect in certain materials such as quartz to measure the strain upon the sensing mechanism due to pressure.

**Optical**

Uses the physical change of an optical fiber to detect strain due to applied pressure.

**Potentiometric**

Uses the motion of a wiper along a resistive mechanism to detect the strain caused by applied pressure.

**Resonant**

Uses the changes in

resonant frequency

in a sensing mechanism to measure stress, or changes in gas density, caused by applied pressure.

### Thermal conductivity

Generally, as a real gas increases in density -which may indicate an increase in pressure- its ability to conduct heat increases. In this type of gauge, a wire filament is heated by running current through it. A thermocouple or resistance thermometer (RTD) can then be used to measure the temperature of the filament. This temperature is dependent on the rate at which the filament loses heat to the surrounding gas, and therefore on the thermal conductivity. A common variant is the Pirani gauge, which uses a single platinum filament as both the heated element and RTD. These gauges are accurate from 10−3 Torr to 10 Torr, but their calibration is sensitive to the chemical composition of the gases being measured.

#### Pirani (one wire)

A Pirani gauge consists of a metal wire open to the pressure being measured. The wire is heated by a current flowing through it and cooled by the gas surrounding it. If the gas pressure is reduced, the cooling effect will decrease, hence the equilibrium temperature of the wire will increase. The resistance of the wire is a function of its temperature: by measuring the voltage across the wire and the current flowing through it, the resistance (and so the gas pressure) can be determined. This type of gauge was invented by Marcello Pirani.

#### Two-wire

In two-wire gauges, one wire coil is used as a heater, and the other is used to measure temperature due to convection. **Thermocouple gauges** and **thermistor gauges** work in this manner using a thermocouple or thermistor, respectively, to measure the temperature of the heated wire.

### Ionization gauge

**Ionization gauges** are the most sensitive gauges for very low pressures (also referred to as hard or high vacuum). They sense pressure indirectly by measuring the electrical ions produced when the gas is bombarded with electrons. Fewer ions will be produced by lower density gases. The calibration of an ion gauge is unstable and dependent on the nature of the gases being measured, which is not always known. They can be calibrated against a McLeod gauge which is much more stable and independent of gas chemistry.

Thermionic emission generates electrons, which collide with gas atoms and generate positive ions. The ions are attracted to a suitably biased electrode known as the collector. The current in the collector is proportional to the rate of ionization, which is a function of the pressure in the system. Hence, measuring the collector current gives the gas pressure. There are several sub-types of ionization gauge.

Useful range

: 10

−10

- 10

−3

torr (roughly 10

−8

- 10

−1

Pa)

Most ion gauges come in two types: hot cathode and cold cathode. In the hot cathode version, an electrically heated filament produces an electron beam. The electrons travel through the gauge and ionize gas molecules around them. The resulting ions are collected at a negative electrode. The current depends on the number of ions, which depends on the pressure in the gauge. Hot cathode gauges are accurate from 10−3 Torr to 10−10 Torr. The principle behind cold cathode version is the same, except that electrons are produced in the discharge of a high voltage. Cold cathode gauges are accurate from 10−2 Torr to 10−9 Torr. Ionization gauge calibration is very sensitive to construction geometry, chemical composition of gases being measured, corrosion and surface deposits. Their calibration can be invalidated by activation at atmospheric pressure or low vacuum. The composition of gases at high vacuums will usually be unpredictable, so a mass spectrometer must be used in conjunction with the ionization gauge for accurate measurement.

#### Hot cathode

A hot-cathode ionization gauge is composed mainly of three electrodes acting together as a triode, wherein the cathode is the filament. The three electrodes are a collector or plate, a filament, and a grid. The collector current is measured in picoamperes by an electrometer. The filament voltage to ground is usually at a potential of 30 volts, while the grid voltage at 180–210 volts DC, unless there is an optional electron bombardment feature, by heating the grid, which may have a high potential of approximately 565 volts.

The most common ion gauge is the hot-cathode **Bayard–Alpert gauge**, with a small ion collector inside the grid. A glass envelope with an opening to the vacuum can surround the electrodes, but usually the **nude gauge** is inserted in the vacuum chamber directly, the pins being fed through a ceramic plate in the wall of the chamber. Hot-cathode gauges can be damaged or lose their calibration if they are exposed to atmospheric pressure or even low vacuum while hot. The measurements of a hot-cathode ionization gauge are always logarithmic.

Electrons emitted from the filament move several times in back-and-forth movements around the grid before finally entering the grid. During these movements, some electrons collide with a gaseous molecule to form a pair of an ion and an electron (electron ionization). The number of these ions is proportional to the gaseous molecule density multiplied by the electron current emitted from the filament, and these ions pour into the collector to form an ion current. Since the gaseous molecule density is proportional to the pressure, the pressure is estimated by measuring the ion current.

The low-pressure sensitivity of hot-cathode gauges is limited by the photoelectric effect. Electrons hitting the grid produce x-rays that produce photoelectric noise in the ion collector. This limits the range of older hot-cathode gauges to 10−8 Torr and the Bayard–Alpert to about 10−10 Torr. Additional wires at cathode potential in the line of sight between the ion collector and the grid prevent this effect. In the extraction type the ions are not attracted by a wire, but by an open cone. As the ions cannot decide which part of the cone to hit, they pass through the hole and form an ion beam. This ion beam can be passed on to a:

- Faraday cup
- Microchannel plate detector with Faraday cup
- Quadrupole mass analyzer with Faraday cup
- Quadrupole mass analyzer with microchannel plate detector and Faraday cup
- Ion lens and acceleration voltage and directed at a target to form a sputter gun. In this case a valve lets gas into the grid-cage.

#### Cold cathode

There are two subtypes of cold-cathode ionization gauges: the **Penning gauge** (invented by Frans Michel Penning), and the **inverted magnetron**, also called a **Redhead gauge**. The major difference between the two is the position of the anode with respect to the cathode. Neither has a filament, and each may require a DC potential of about 4 kV for operation. Inverted magnetrons can measure down to 1×10−12 Torr.

Likewise, cold-cathode gauges may be reluctant to start at very low pressures, in that the near-absence of a gas makes it difficult to establish an electrode current - in particular in Penning gauges, which use an axially symmetric magnetic field to create path lengths for electrons that are of the order of metres. In ambient air, suitable ion-pairs are ubiquitously formed by cosmic radiation; in a Penning gauge, design features are used to ease the set-up of a discharge path. For example, the electrode of a Penning gauge is usually finely tapered to facilitate the field emission of electrons.

Maintenance cycles of cold cathode gauges are, in general, measured in years, depending on the gas type and pressure that they are operated in. Using a cold cathode gauge in gases with substantial organic components, such as pump oil fractions, can result in the growth of delicate carbon films and shards within the gauge that eventually either short-circuit the electrodes of the gauge or impede the generation of a discharge path.

| Physical phenomena | Instrument | Governing equation | Limiting factors | Practical pressure range | Ideal accuracy | Response time |
|---|---|---|---|---|---|---|
| Mechanical | Liquid column manometer | $\Delta P=\rho gh$ |   | atm. to 1 mbar |   |   |
| Mechanical | Capsule dial gauge |   | Friction | 1000 to 1 mbar | ±5% of full scale | Slow |
| Mechanical | Strain gauge |   |   | 1000 to 1 mbar |   | Fast |
| Mechanical | Capacitance manometer |   | Temperature fluctuations | atm to 10−6 mbar | ±1% of reading | Slower when filter mounted |
| Mechanical | McLeod | Boyle's law |   | 10 to 10−6 mbar | ±10% of reading between 10−4 and 5⋅10−2 mbar |   |
| Transport | Spinning rotor (drag) |   |   | 10−1 to 10−7 mbar | ±2.5% of reading between 10−7 and 10−2 mbar 2.5 to 13.5% between 10−2 and 1 mbar |   |
| Transport | Pirani (Wheatstone bridge) |   | Thermal conductivity | 1000 to 10−3 mbar (const. temperature) 10 to 10−3 mbar (const. voltage) | ±6% of reading between 10−2 and 10 mbar | Fast |
| Transport | Thermocouple (Seebeck effect) |   | Thermal conductivity | 5 to 10−3 mbar | ±10% of reading between 10−2 and 1 mbar |   |
| Ionization | Cold cathode (Penning) |   | Ionization yield | 10−2 to 10−7 mbar | +100 to -50% of reading |   |
| Ionization | Hot cathode (ionization induced by thermionic emission) |   | Low current measurement; parasitic x-ray emission | 10−3 to 10−10 mbar | ±10% between 10−7 and 10−4 mbar ±20% at 10−3 and 10−9 mbar ±100% at 10−10 mbar |   |


## Dynamic transients

When fluid flows are not in equilibrium, local pressures may be higher or lower than the average pressure in a medium. These disturbances propagate from their source as longitudinal pressure variations along the path of propagation. This is also called sound. Sound pressure is the instantaneous local pressure deviation from the average pressure caused by a sound wave. Sound pressure can be measured using a microphone in air and a hydrophone in water. The effective sound pressure is the root mean square of the instantaneous sound pressure over a given interval of time. Sound pressures are normally small and are often expressed in units of microbar.

- frequency response of pressure sensors
- resonance


## Calibration and standards

The American Society of Mechanical Engineers (ASME) has developed two separate and distinct standards on pressure measurement, B40.100 and PTC 19.2. B40.100 provides guidelines on Pressure Indicated Dial Type and Pressure Digital Indicating Gauges, Diaphragm Seals, Snubbers, and Pressure Limiter Valves. PTC 19.2 provides instructions and guidance for the accurate determination of pressure values in support of the ASME Performance Test Codes. The choice of method, instruments, required calculations, and corrections to be applied depends on the purpose of the measurement, the allowable uncertainty, and the characteristics of the equipment being tested.

The methods for pressure measurement and the protocols used for data transmission are also provided. Guidance is given for setting up the instrumentation and determining the uncertainty of the measurement. Information regarding the instrument type, design, applicable pressure range, accuracy, output, and relative cost is provided. Information is also provided on pressure-measuring devices that are used in field environments i.e., piston gauges, manometers, and low-absolute-pressure (vacuum) instruments.

These methods are designed to assist in the evaluation of measurement uncertainty based on current technology and engineering knowledge, taking into account published instrumentation specifications and measurement and application techniques. This Supplement provides guidance in the use of methods to establish the pressure-measurement uncertainty.

### European (CEN) Standard

- EN 472 : Pressure gauge - Vocabulary.
- EN 837-1 : Pressure gauges. Bourdon tube pressure gauges. Dimensions, metrology, requirements and testing.
- EN 837-2 : Pressure gauges. Selection and installation recommendations for pressure gauges.
- EN 837-3 : Pressure gauges. Diaphragm and capsule pressure gauges. Dimensions, metrology, requirements, and testing.

### US ASME Standards

- B40.100-2013: Pressure gauges and Gauge attachments.
- PTC 19.2-2010 : The Performance test code for pressure measurement.


## Applications

There are many applications for pressure sensors:

- **Pressure sensing**

This is where the measurement of interest is pressure, expressed as a force per unit area. This is useful in weather instrumentation, aircraft, automobiles, and any other machinery that has pressure functionality implemented.

- **Altitude sensing**

This is useful in aircraft, rockets, satellites, weather balloons, and many other applications. All these applications make use of the relationship between changes in pressure relative to the altitude. This relationship is governed by the following equation: $h=(1-(P/P_{\mathrm {ref} })^{0.190284})\times 145366.45\mathrm {ft}$ This equation is calibrated for an altimeter, up to 36,090 feet (11,000 m). Outside that range, an error will be introduced which can be calculated differently for each different pressure sensor. These error calculations will factor in the error introduced by the change in temperature as we go up.

Barometric pressure sensors can have an altitude resolution of less than 1 meter, which is significantly better than GPS systems (about 20 meters altitude resolution). In navigation applications altimeters are used to distinguish between stacked road levels for car navigation and floor levels in buildings for pedestrian navigation.

- **Flow sensing**

This is the use of pressure sensors in conjunction with the venturi effect to measure flow. Differential pressure is measured between two segments of a venturi tube that have a different aperture. The pressure difference between the two segments is directly proportional to the flow rate through the venturi tube. A low pressure sensor is almost always required as the pressure difference is relatively small.

- **Level / depth sensing**

A pressure sensor may also be used to calculate the level of a fluid. This technique is commonly employed to measure the depth of a submerged body (such as a diver or submarine), or level of contents in a tank (such as in a water tower). For most practical purposes, fluid level is directly proportional to pressure. In the case of fresh water where the contents are under atmospheric pressure, 1psi = 27.7 inH2O / 1Pa = 9.81 mmH2O. The basic equation for such a measurement is $P=\rho gh$ where *P* = pressure, *ρ* = density of the fluid, *g* = standard gravity, *h* = height of fluid column above pressure sensor

- **Leak testing**

A pressure sensor may be used to sense the decay of pressure due to a system leak. This is commonly done by either comparison to a known leak using differential pressure, or by means of utilizing the pressure sensor to measure pressure change over time.

- **Groundwater measurement**

A **piezometer** is either a device used to measure liquid pressure in a system by measuring the height to which a column of the liquid rises against gravity, or a device which measures the pressure (more precisely, the piezometric head) of groundwater at a specific point. A piezometer is designed to measure static pressures, and thus differs from a pitot tube by not being pointed into the fluid flow. Observation wells give some information on the water level in a formation, but must be read manually. Electrical pressure transducers of several types can be read automatically, making data acquisition more convenient.

The first piezometers in geotechnical engineering were open wells or standpipes (sometimes called **Casagrande piezometers**) installed into an aquifer. A Casagrande piezometer will typically have a solid casing down to the depth of interest, and a slotted or screened casing within the zone where water pressure is being measured. The casing is sealed into the drillhole with clay, bentonite or concrete to prevent surface water from contaminating the groundwater supply. In an unconfined aquifer, the water level in the piezometer would not be exactly coincident with the water table, especially when the vertical component of flow velocity is significant. In a confined aquifer under artesian conditions, the water level in the piezometer indicates the pressure in the aquifer, but not necessarily the water table. Piezometer wells can be much smaller in diameter than production wells, and a 5 cm diameter standpipe is common.

Piezometers in durable casings can be buried or pushed into the ground to measure the groundwater pressure at the point of installation. The pressure gauges (transducer) can be vibrating-wire, pneumatic, or strain-gauge in operation, converting pressure into an electrical signal. These piezometers are cabled to the surface where they can be read by data loggers or portable readout units, allowing faster or more frequent reading than is possible with open standpipe piezometers.
