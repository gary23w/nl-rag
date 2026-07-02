---
title: "Thermistor"
source: https://en.wikipedia.org/wiki/Thermistor
domain: temperature-sensors
license: CC-BY-SA-4.0
tags: thermistor sensor, temperature measurement, infrared thermometer, bimetallic strip
fetched: 2026-07-02
---

# Thermistor

A **thermistor** is a semiconductor type of resistor in which the resistance is strongly dependent on temperature. The word *thermistor* is a portmanteau of *thermal* and *resistor*. The varying resistance with temperature allows these devices to be used as temperature sensors, or to control current as a function of temperature. Some thermistors have decreasing resistance with temperature, while other types have increasing resistance with temperature. This allows them to be used for limiting current to cold circuits, e.g. for inrush current protection, or for limiting current to hot circuits, e.g. to prevent thermal runaway.

Thermistors are categorized based on their conduction models. *Negative-temperature-coefficient* (NTC) thermistors have *less* resistance at *higher* temperatures, while *positive-temperature-coefficient* (PTC) thermistors have *more* resistance at *higher* temperatures.

NTC thermistors are widely used as inrush current limiters and temperature sensors, while PTC thermistors are used as self-resetting overcurrent protectors and self-regulating heating elements. The operational temperature range of a thermistor is dependent on the material and is typically between −100 and 300 °C (−148 and 572 °F).

## Types

Depending on materials used, thermistors are classified into two types:

- With *NTC* (negative temperature coefficient) thermistors, resistance decreases as temperature rises; usually because electrons are bumped up by thermal agitation from the valence band to the conduction band. An NTC is commonly used as a temperature sensor, or in series with a circuit as an inrush current limiter.
- With *PTC* (positive temperature coefficient) thermistors, resistance increases as temperature rises; usually because of increased thermal lattice agitations, particularly those of impurities and imperfections. PTC thermistors are commonly installed in series with a circuit, and used to protect against overcurrent conditions, as resettable fuses.

Thermistors are generally produced using powdered metal oxides. With formulas and techniques vastly improving over the past 20 years as of 2020, NTC thermistors can now achieve accuracies over wide temperature ranges such as ±0.1 °C or ±0.2 °C from 0 °C to 70 °C with excellent long-term stability. NTC thermistor elements come in many styles, such as axial-leaded glass-encapsulated (DO-35, DO-34 and DO-41 diodes), glass-coated chips, epoxy-coated with bare or insulated lead wire and surface-mount, as well as thin film versions. The typical operating temperature range of a thermistor is −55 °C to +150 °C, though some glass-body thermistors have a maximal operating temperature of +300 °C.

Thermistors differ from resistance temperature detectors (RTDs) in that the material used in a thermistor is generally a ceramic or polymer, while RTDs use pure metals. The temperature response is also different; RTDs are useful over larger temperature ranges, while thermistors typically achieve a greater precision within a limited temperature range, typically −90 °C to 130 °C.

## Basic operation

Assuming, as a first-order approximation, that the relationship between resistance and temperature is linear, then

$\Delta R=k\,\Delta T,$

where

$\Delta R$

, change in resistance,

$\Delta T$

, change in temperature,

k

, first-order

temperature coefficient of resistance

.

Depending on type of the thermistor in question the k may be either positive or negative.

If k is positive, the resistance increases with increasing temperature, and the device is called a *positive-temperature-coefficient* (*PTC*) *thermistor*, or *posistor*. There are two types of PTC resistor – *switching thermistor* and *silistor*. If k is negative, the resistance decreases with increasing temperature, and the device is called a *negative-temperature-coefficient* (*NTC*) *thermistor*. Resistors that are not thermistors are designed to have a k as close to 0 as possible so that their resistance remains nearly constant over a wide temperature range.

Instead of the temperature coefficient *k*, sometimes the *temperature coefficient of resistance* $\alpha _{T}$ ("alpha sub T") is used. It is defined as

$\alpha _{T}={\frac {1}{R(T)}}{\frac {dR}{dT}}.$

This $\alpha _{T}$ coefficient should not be confused with the a parameter below.

## Construction and materials

Thermistors are typically built by using metal oxides. They're typically pressed into a bead, disk, or cylindrical shape and then encapsulated with an impermeable material such as epoxy or glass.

NTC thermistors are manufactured from oxides of the iron group of metals: e.g. chromium (CrO, Cr2O3), manganese (e.g. MnO), cobalt (CoO), iron (iron oxides), and nickel (NiO, Ni2O3). these oxides form a ceramic body with terminals composed of conductive metals such as silver, nickel, and tin.

PTC thermistors are usually prepared from barium (Ba), strontium, or lead titanates (e.g. PbTiO3).

Thermistors can also be produced by resonant acoustic mixing of the previously mentioned oxides, followed by a sintering process. This effort reduces production time and can eliminate the calcination step entirely.

## Steinhart–Hart equation

In practical devices, the linear approximation model (above) is accurate only over a limited temperature range. Over wider temperature ranges, a more complex resistance–temperature transfer function provides a more faithful characterization of the performance. The Steinhart–Hart equation is a widely used third-order approximation:

${\frac {1}{T}}=a+b\ln R+c\,(\ln R)^{3},$

where *a*, *b* and *c* are called the Steinhart–Hart parameters and must be specified for each device. *T* is the absolute temperature, and *R* is the resistance. The equation is not dimensionally correct, since a change in the units of R results in an equation with a different form, containing a $(\ln R)^{2}$ term. In practice, the equation gives good numerical results for resistances expressed in, for example, ohms (Ω) or kiloohms, but the coefficients a, b, and c must be stated with reference to that particular unit. To give resistance as a function of temperature, the above cubic equation in $\ln R$ can be solved, the real root of which is given by

$\ln R={\frac {b}{3c\,x^{1/3}}}-x^{1/3}$

where

${\begin{aligned}y&={\frac {1}{2c}}\left(a-{\frac {1}{T}}\right),\\x&=y+{\sqrt {\left({\frac {b}{3c}}\right)^{3}+y^{2}}}.\end{aligned}}$

The error in the Steinhart–Hart equation is generally less than 0.02 °C in the measurement of temperature over a 200 °C range. As an example, typical values for a thermistor with a resistance of 3 kΩ at room temperature (25 °C = 298.15 K, R in Ω) are:

${\begin{aligned}a&=1.40\times 10^{-3},\\b&=2.37\times 10^{-4},\\c&=9.90\times 10^{-8}.\end{aligned}}$

## *B* or *β* parameter equation

NTC thermistors can also be characterised with the *B* (or *β*) parameter equation, which is essentially the Steinhart–Hart equation with $a=1/T_{0}-(1/B)\ln R_{0}$ , $b=1/B$ and $c=0$ ,

${\frac {1}{T}}={\frac {1}{T_{0}}}+{\frac {1}{B}}\ln {\frac {R}{R_{0}}},$

where the temperatures and the *B* parameter are in kelvins, and *R*0 is the resistance of the thermistor at temperature *T*0 (25 °C = 298.15 K). Solving for *R* yields

$R=R_{0}e^{B\left({\frac {1}{T}}-{\frac {1}{T_{0}}}\right)}$

or, alternatively,

$R=r_{\infty }e^{B/T},$

where $r_{\infty }=R_{0}e^{-B/T_{0}}$ .

This can be solved for the temperature:

$T={\frac {B}{\ln(R/r_{\infty })}}={\frac {T_{0}*B}{T_{0}*\ln(R/R_{0})+B}}.$

The *B*-parameter equation can also be written as $\ln R=B/T+\ln r_{\infty }$ . This can be used to convert the function of resistance vs. temperature of a thermistor into a linear function of $\ln R$ vs. $1/T$ . The average slope of this function will then yield an estimate of the value of the *B* parameter.

## Conduction model

### NTC (negative temperature coefficient)

Many NTC thermistors are made from a pressed disc, rod, plate, bead or cast chip of semiconducting material such as sintered metal oxides. They work because raising the temperature of a semiconductor increases the number of active charge carriers by promoting them into the *conduction band*. The more charge carriers that are available, the more current a material can conduct. In certain materials like ferric oxide (Fe2O3) with titanium (Ti) doping an *n-type* semiconductor is formed and the charge carriers are electrons. In materials such as nickel oxide (NiO) with lithium (Li) doping a *p-type* semiconductor is created, where holes are the charge carriers.

This is described in the formula

$I=n\cdot A\cdot v\cdot e,$

where

I

= electric current (amperes),

n

= density of charge carriers (count/m

3

),

A

= cross-sectional area of the material (m

2

),

v

= drift velocity of electrons (m/s),

e

= charge of an electron (

$e=1.602\times 10^{-19}$

coulomb).

Over large changes in temperature, calibration is necessary. Over small changes in temperature, if the right semiconductor is used, the resistance of the material is linearly proportional to the temperature. There are many different semiconducting thermistors with a range from about 0.01 kelvin to 2,000 kelvins (−273.14 °C to 1,700 °C).

The IEC standard symbol for a NTC thermistor includes a "−t°" under the rectangle.

### PTC (positive temperature coefficient)

Most PTC thermistors are made from doped polycrystalline ceramic (containing barium titanate (BaTiO3) and other compounds) which have the property that their resistance rises suddenly at a certain critical temperature. Barium titanate is ferroelectric and its dielectric constant varies with temperature. Below the Curie point temperature, the high dielectric constant prevents the formation of potential barriers between the crystal grains, leading to a low resistance. In this region the device has a small negative temperature coefficient. At the Curie point temperature, the dielectric constant drops sufficiently to allow the formation of potential barriers at the grain boundaries, and the resistance increases sharply with temperature. At even higher temperatures, the material reverts to NTC behaviour.

Another type of thermistor is a **silistor** (a thermally sensitive silicon resistor). Silistors employ silicon as the semiconductive component material. Unlike ceramic PTC thermistors, silistors have an almost linear resistance-temperature characteristic. Silicon PTC thermistors have a much smaller drift than an NTC thermistor. They are stable devices which are hermetically sealed in an axial leaded glass encapsulated package.

Barium titanate thermistors can be used as self-controlled heaters; for a given voltage, the ceramic will heat to a certain temperature, but the power used will depend on the heat loss from the ceramic.

The dynamics of PTC thermistors being powered lends to a wide range of applications. When first connected to a voltage source, a large current corresponding to the low, cold, resistance flows, but as the thermistor self-heats, the current is reduced until a limiting current (and corresponding peak device temperature) is reached. The current-limiting effect can replace fuses. In the degaussing circuits of many CRT monitors and televisions an appropriately chosen thermistor is connected in series with the degaussing coil. This results in a smooth current decrease for an improved degaussing effect. Some of these degaussing circuits have auxiliary heating elements to heat the thermistor (and reduce the resulting current) further.

Another type of PTC thermistor is the polymer PTC, which is sold under brand names such as "Polyswitch" "Semifuse", and "Multifuse". This consists of plastic with carbon grains embedded in it. When the plastic is cool, the carbon grains are all in contact with each other, forming a conductive path through the device. When the plastic heats up, it expands, forcing the carbon grains apart, and causing the resistance of the device to rise, which then causes increased heating and rapid resistance increase. Like the BaTiO3 thermistor, this device has a highly nonlinear resistance/temperature response useful for thermal or circuit control, not for temperature measurement. Besides circuit elements used to limit current, self-limiting heaters can be made in the form of wires or strips, useful for heat tracing. PTC thermistors "latch" into a hot / high resistance state: once hot, they stay in that high resistance state, until cooled. The effect can be used as a primitive latch/memory circuit, the effect being enhanced by using two PTC thermistors in series, with one thermistor cool, and the other thermistor hot.

The IEC standard symbol for a PTC thermistor includes a "+t°" under the rectangle.

## Self-heating effects

When a current flows through a thermistor, it generates heat, which raises the temperature of the thermistor above that of its environment. If the thermistor is being used to measure the temperature of the environment, this electrical heating may introduce a significant error (an observer effect) if a correction is not made. Alternatively, this effect itself can be exploited. It can, for example, make a sensitive air-flow device employed in a sailplane rate-of-climb instrument, the electronic variometer, or serve as a timer for a relay as was formerly done in telephone exchanges.

The electrical power input to the thermistor is just

$P_{E}=IV,$

where *I* is current, and *V* is the voltage drop across the thermistor. This power is converted to heat, and this heat energy is transferred to the surrounding environment. The rate of transfer is well described by Newton's law of cooling:

$P_{T}=K(T(R)-T_{0}),$

where *T*(*R*) is the temperature of the thermistor as a function of its resistance *R*, $T_{0}$ is the temperature of the surroundings, and *K* is the *dissipation constant*, usually expressed in units of milliwatts per degree Celsius. At equilibrium, the two rates must be equal:

$P_{E}=P_{T}.$

The current and voltage across the thermistor depend on the particular circuit configuration. As a simple example, if the voltage across the thermistor is held fixed, then by Ohm's law we have $I=V/R$ , and the equilibrium equation can be solved for the ambient temperature as a function of the measured resistance of the thermistor:

$T_{0}=T(R)-{\frac {V^{2}}{KR}}.$

The dissipation constant is a measure of the thermal connection of the thermistor to its surroundings. It is generally given for the thermistor in still air and in well-stirred oil. Typical values for a small glass-bead thermistor are 1.5 mW/°C in still air and 6.0 mW/°C in stirred oil. If the temperature of the environment is known beforehand, then a thermistor may be used to measure the value of the dissipation constant. For example, the thermistor may be used as a flow-rate sensor, since the dissipation constant increases with the rate of flow of a fluid past the thermistor.

The power dissipated in a thermistor is typically maintained at a very low level to ensure insignificant temperature measurement error due to self-heating. However, some thermistor applications depend upon significant "self-heating" to raise the body temperature of the thermistor well above the ambient temperature, so the sensor then detects even subtle changes in the thermal conductivity of the environment. Some of these applications include liquid-level detection, liquid-flow measurement and air-flow measurement.

## Applications

### PTC

- As current-limiting devices for circuit protection, as replacements for fuses. Current through the device causes a small amount of resistive heating. If the current is large enough to generate heat more quickly than the device can lose it to its surroundings, the device heats up, causing its resistance to increase. This creates a self-reinforcing effect that drives the resistance upwards, therefore limiting the current.
- As timers in the degaussing coil circuit of most CRT displays. When the display unit is initially switched on, current flows through the thermistor and degaussing coil. The coil and thermistor are intentionally sized so that the current flow will heat the thermistor to the point that the degaussing coil shuts off in under a second. For effective degaussing, it is necessary that the magnitude of the alternating magnetic field produced by the degaussing coil decreases smoothly and continuously, rather than sharply switching off or decreasing in steps; the PTC thermistor accomplishes this naturally as it heats up. A degaussing circuit using a PTC thermistor is simple, reliable (for its simplicity), and inexpensive.
- As heaters, in the automotive industry, to provide cabin heating (in addition to heating provided by a heat pump or the waste heat of an internal combustion engine), or to heat diesel fuel in cold conditions before engine injection.
- In temperature-compensated voltage-controlled oscillators in synthesizers.
- In lithium battery protection circuits.
- In an electrically actuated wax motor to provide the heat necessary to expand the wax.
- Many electric motors and dry type power transformers incorporate PTC thermistors in their windings. When used in conjunction with a monitoring relay they provide overtemperature protection to prevent insulation damage. The equipment manufacturer selects a thermistor with a highly non-linear response curve where resistance increases dramatically at the maximum allowable winding temperature, causing the relay to operate.
- To prevent thermal runaway in electronic circuits. Many electronic devices, for example bipolar transistors, draw more power as they get hotter. Commonly, such circuits contain ordinary resistors to limit the current available and prevent the device from overheating. However, in some applications, PTC thermistors allow better performance than resistors.
- To prevent current hogging in electronic circuits. Current hogging can occur when electronic devices are connected in parallel. In severe cases, current hogging can cause cascading failure of all the devices. A PTC thermistor attached in series with each device can assure the current is divided reasonably evenly between the devices.
- In crystal oscillators for temperature compensation, medical equipment temperature control, and industrial automation, silicon PTC thermistors display a nearly linear positive temperature coefficient (0.7%/°C). A linearization resistor can be added if further linearization is needed.

### NTC

- As a thermometer for low-temperature measurements of the order of 10 K.
- As an inrush current limiter device in power supply circuits, they present a higher resistance initially, which prevents large currents from flowing at turn-on, and then heat up and become much lower resistance to allow higher current flow during normal operation. These thermistors are usually much larger than measuring type thermistors, and are purposely designed for this application.
- As sensors in automotive applications to monitor fluid temperatures like the engine coolant, cabin air, external air or engine oil temperature, and feed the relative readings to control units like the ECU and to the dashboard.
- To monitor the temperature of an incubator.
- Thermistors are also commonly used in modern digital thermostats and to monitor the temperature of battery packs while charging.
- Thermistors are often used in the hot ends of 3D printers; they monitor the heat produced and allow the printer's control circuitry to keep a constant temperature for melting the plastic filament.
- In the food handling and processing industry, especially for food storage systems and food preparation. Maintaining the correct temperature is critical to prevent foodborne illness.
- Throughout the consumer appliance industry for measuring temperature. Toasters, coffee makers, refrigerators, freezers, hair dryers, etc. all rely on thermistors for proper temperature control.
- NTC thermistors come in bare and lugged forms, the former is for point sensing to achieve high accuracy for specific points, such as laser diode die, etc.
- For measurement of temperature profile inside the sealed cavity of a convective (thermal) inertial sensor.
- Thermistor Probe Assemblies offer protection of the sensor in harsh environments. The thermistor sensing element can be packaged into a variety of enclosures for use in industries such as HVAC/R, Building Automation, Pool/Spa, Energy and Industrial Electronics. Enclosures can be made out of stainless steel, aluminum, copper brass or plastic and configurations include threaded (NPT, etc.), flanged (with mounting holes for ease of installation) and straight (flat tip, pointed tip, radius tip, etc.). Thermistor probe assemblies are very rugged and are highly customizable to fit the application needs. Probe assemblies have gained in popularity over the years as improvements in research, engineering and manufacturing techniques have been made.
- UL Recognized NTC thermistors in the XGPU2 category helps save equipment manufacturers time and money when applying for safety approvals for their end product. DO-35 hermetically sealed glass encapsulated thermistors can operate up to 250 °C which gives them an advantage in many applications when UL is requested for a sensing element.

## History

The first NTC thermistor was discovered in 1833 by Michael Faraday, who reported on the semiconducting behavior of silver sulfide. Faraday noticed that the resistance of silver sulfide decreased dramatically as temperature increased. This was also the first documented observation of a semiconducting material.

Because early thermistors were difficult to produce and applications for the technology were limited, commercial production of thermistors did not begin until the 1930s. A commercially viable thermistor was invented by Samuel Ruben in 1930.
