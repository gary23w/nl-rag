---
title: "Supercapacitor (part 3/4)"
source: https://en.wikipedia.org/wiki/Supercapacitor
domain: supercapacitors
license: CC-BY-SA-4.0
tags: supercapacitor cell, pseudocapacitance charge, equivalent series resistance, ragone plot
fetched: 2026-07-02
part: 3/4
---

## Electrical parameters

### Capacitance

Capacitance values for commercial capacitors are specified as "rated capacitance CR". This is the value for which the capacitor has been designed. The value for an actual component must be within the limits given by the specified tolerance. Typical values are in the range of farads (F), three to six orders of magnitude larger than those of electrolytic capacitors. The capacitance value results from the energy W (expressed in Joule) of a loaded capacitor loaded via a DC voltage VDC.

$W={\frac {1}{2}}\cdot C_{\text{DC}}\cdot V_{\text{DC}}^{2}$

This value is also called the "DC capacitance".

#### Measurement

Conventional capacitors are normally measured with a small AC voltage (0.5 V) and a frequency of 100 Hz or 1 kHz depending on the capacitor type. The AC capacitance measurement offers fast results, important for industrial production lines. The capacitance value of a supercapacitor depends strongly on the measurement frequency, which is related to the porous electrode structure and the limited electrolyte's ion mobility. Even at a low frequency of 10 Hz, the measured capacitance value drops from 100 to 20 percent of the DC capacitance value.

This extraordinarily strong frequency dependence can be explained by the different distances the ions have to move in the electrode's pores. The area at the beginning of the pores can be easily accessed by the ions; this short distance is accompanied by low electrical resistance. The greater the distance the ions have to cover, the higher the resistance. This phenomenon can be described with a series circuit of cascaded RC (resistor/capacitor) elements with serial RC time constants. These result in delayed current flow, reducing the total electrode surface area that can be covered with ions if polarity changes – capacitance decreases with increasing AC frequency. Thus, the total capacitance is achieved only after longer measuring times. Out of the reason of the very strong frequency dependence of the capacitance, this electrical parameter has to be measured with a special constant current charge and discharge measurement, defined in IEC standards 62391-1 and -2.

Measurement starts with charging the capacitor. The voltage has to be applied and after the constant current/constant voltage power supply has achieved the rated voltage, the capacitor must be charged for 30 minutes. Next, the capacitor has to be discharged with a constant discharge current Idischarge. Then the time t1 and t2, for the voltage to drop from 80% (V1) to 40% (V2) of the rated voltage is measured. The capacitance value is calculated as:

$C_{\text{total}}=I_{\text{discharge}}\cdot {\frac {t_{2}-t_{1}}{V_{1}-V_{2}}}$

The value of the discharge current is determined by the application. The IEC standard defines four classes:

1. Memory backup, discharge current in mA = 1 • C (F)
2. Energy storage, discharge current in mA = 0,4 • C (F) • V (V)
3. Power, discharge current in mA = 4 • C (F) • V (V)
4. Instantaneous power, discharge current in mA = 40 • C (F) • V (V)

The measurement methods employed by individual manufacturers are mainly comparable to the standardized methods.

The standardized measuring method is too time-consuming for manufacturers to use during production for each individual component. For industrial-produced capacitors, the capacitance value is instead measured with a faster, low-frequency AC voltage, and a correlation factor is used to compute the rated capacitance.

This frequency dependence affects capacitor operation. Rapid charge and discharge cycles mean that neither the rated capacitance value nor specific energy are available. In this case the rated capacitance value is recalculated for each application condition.

The time *t* a supercapacitor can deliver a constant current *I* can be calculated as:

$t={\frac {C\cdot (U_{\text{charge}}-U_{\text{min}})}{I}}$

as the capacitor voltage decreases from Ucharge down to Umin.

If the application needs a constant power *P* for a certain time *t* this can be calculated as:

$t={\frac {1}{2P}}\cdot C\cdot (U_{\text{charge}}^{2}-U_{\text{min}}^{2}).$

wherein also the capacitor voltage decreases from Ucharge down to Umin.

### Operating voltage

Supercapacitors are low voltage components. Safe operation requires that the voltage remain within specified limits. The rated voltage UR is the maximum DC voltage or peak pulse voltage that may be applied continuously and remain within the specified temperature range. Capacitors should never be subjected to voltages continuously in excess of the rated voltage.

The rated voltage includes a safety margin against the electrolyte's breakdown voltage at which the electrolyte decomposes. The breakdown voltage decomposes the separating solvent molecules in the Helmholtz double-layer, e.g. water splits into hydrogen and oxygen. The solvent molecules then cannot separate the electrical charges from each other. Higher voltages than rated voltage cause hydrogen gas formation or a short circuit.

Standard supercapacitors with aqueous electrolyte normally are specified with a rated voltage of 2.1 to 2.3 V and capacitors with organic solvents with 2.5 to 2.7 V. Lithium-ion capacitors with doped electrodes may reach a rated voltage of 3.8 to 4 V, but have a low voltage limit of about 2.2 V. Supercapacitors with ionic electrolytes can exceed an operating voltage of 3.5 V.

Operating supercapacitors below the rated voltage improves the long-time behavior of the electrical parameters. Capacitance values and internal resistance during cycling are more stable and lifetime and charge/discharge cycles may be extended.

Higher application voltages require connecting cells in series. Since each component has a slight difference in capacitance value and ESR, it is necessary to actively or passively balance them to stabilize the applied voltage. Passive balancing employs resistors in parallel with the supercapacitors. Active balancing may include electronic voltage management above a threshold that varies the current.

### Internal resistance

Charging/discharging a supercapacitor is connected to the movement of charge carriers (ions) in the electrolyte across the separator to the electrodes and into their porous structure. Losses occur during this movement that can be measured as the internal DC resistance.

With the electrical model of cascaded, series-connected RC (resistor/capacitor) elements in the electrode pores, the internal resistance increases with the increasing penetration depth of the charge carriers into the pores. The internal DC resistance is time dependent and increases during charge/discharge. In applications often only the switch-on and switch-off range is interesting. The internal resistance Ri can be calculated from the voltage drop ΔV2 at the time of discharge, starting with a constant discharge current Idischarge. It is obtained from the intersection of the auxiliary line extended from the straight part and the time base at the time of discharge start (see picture right). Resistance can be calculated by:

$R_{\text{i}}={\frac {\Delta V_{2}}{I_{\text{discharge}}}}$

The discharge current Idischarge for the measurement of internal resistance can be taken from the classification according to IEC 62391-1.

This internal DC resistance Ri should not be confused with the internal AC resistance called equivalent series resistance (ESR) normally specified for capacitors. It is measured at 1 kHz. ESR is much smaller than DC resistance. ESR is not relevant for calculating supercapacitor inrush currents or other peak currents.

Ri determines several supercapacitor properties. It limits the charge and discharge peak currents as well as charge/discharge times. Ri and the capacitance C results in the time constant $\tau$

$\tau =R_{\text{i}}\cdot C$

This time constant determines the charge/discharge time. A 100 F capacitor with an internal resistance of 30 mΩ for example, has a time constant of 0.03 • 100 = 3 s. After 3 seconds charging with a current limited only by internal resistance, the capacitor has 63.2% of full charge (or is discharged to 36.8% of full charge).

Standard capacitors with constant internal resistance fully charge during about 5 $\tau$ . Since internal resistance increases with charge/discharge, actual times cannot be calculated with this formula. Thus, charge/discharge time depends on specific individual construction details.

### Current load and cycle stability

Because supercapacitors operate without forming chemical bonds, current loads, including charge, discharge and peak currents are not limited by reaction constraints. Current load and cycle stability can be much higher than for rechargeable batteries. Current loads are limited only by internal resistance, which may be substantially lower than for batteries.

Internal resistance "Ri" and charge/discharge currents or peak currents "I" generate internal heat losses "Ploss" according to:

$P_{\text{loss}}=R_{\text{i}}\cdot I^{2}$

This heat must be released and distributed to the ambient environment to maintain operating temperatures below the specified maximum temperature.

Heat generally defines capacitor lifetime due to electrolyte diffusion. The heat generation coming from current loads should be smaller than 5 to 10 K at maximum ambient temperature (which has only minor influence on expected lifetime). For that reason the specified charge and discharge currents for frequent cycling are determined by internal resistance.

The specified cycle parameters under maximal conditions include charge and discharge current, pulse duration and frequency. They are specified for a defined temperature range and over the full voltage range for a defined lifetime. They can differ enormously depending on the combination of electrode porosity, pore size and electrolyte. Generally a lower current load increases capacitor life and increases the number of cycles. This can be achieved either by a lower voltage range or slower charging and discharging.

Supercapacitors (except those with polymer electrodes) can potentially support more than one million charge/discharge cycles without substantial capacity drops or internal resistance increases. Beneath the higher current load is this the second great advantage of supercapacitors over batteries. The stability results from the dual electrostatic and electrochemical storage principles.

The specified charge and discharge currents can be significantly exceeded by lowering the frequency or by single pulses. Heat generated by a single pulse may be spread over the time until the next pulse occurs to ensure a relatively small average heat increase. Such a "peak power current" for power applications for supercapacitors of more than 1000 F can provide a maximum peak current of about 1000 A. Such high currents generate high thermal stress and high electromagnetic forces that can damage the electrode-collector connection requiring robust design and construction of the capacitors.

### Device capacitance and resistance dependence on operating voltage and temperature

Device parameters such as capacitance initial resistance and steady state resistance are not constant, but are variable and dependent on the device's operating voltage. Device capacitance will have a measurable increase as the operating voltage increases. For example: a 100F device can be seen to vary 26% from its maximum capacitance over its entire operational voltage range. Similar dependence on operating voltage is seen in steady state resistance (Rss) and initial resistance (Ri). Device properties can also be seen to be dependent on device temperature. As the temperature of the device changes either through operation of varying ambient temperature, the internal properties such as capacitance and resistance will vary as well. Device capacitance is seen to increase as the operating temperature increases.

### Energy capacity

Supercapacitors occupy the gap between high power/low energy electrolytic capacitors and low power/high energy rechargeable batteries. The energy Wmax (expressed in Joule) that can be stored in a capacitor is given by the formula

$W_{\text{max}}={\frac {1}{2}}\cdot C_{\text{total}}\cdot V_{\text{loaded}}^{2}$

This formula describes the amount of energy stored and is often used to describe new research successes. However, only part of the stored energy is available to applications, because the voltage drop and the time constant over the internal resistance mean that some of the stored charge is inaccessible. The effective realized amount of energy Weff is reduced by the used voltage difference between Vmax and Vmin and can be represented as:

$W_{\text{eff}}={\frac {1}{2}}\ C\cdot \ (V_{\text{max}}^{2}-V_{\text{min}}^{2})$

This formula also represents the energy asymmetric voltage components such as lithium ion capacitors.

### Specific energy and specific power

The amount of energy that can be stored in a capacitor *per mass* of that capacitor is called its specific energy. Specific energy is measured gravimetrically (per unit of mass) in watt-hours per kilogram (Wh/kg).

The amount of energy can be stored in a capacitor *per volume* of that capacitor is called its energy density (also called volumetric specific energy in some literature). Energy density is measured volumetrically (per unit of volume) in watt-hours per litre (Wh/L). Units of liters and dm3 can be used interchangeably.

As of 2013 commercial energy density varies widely, but in general range from around 5 to 8 Wh/L. In comparison, petrol fuel has an energy density of 32.4 MJ/L or 9000 Wh/L. Commercial specific energies range from around 0.5 to 15 Wh/kg. For comparison, an aluminum electrolytic capacitor stores typically 0.01 to 0.3 Wh/kg, while a conventional lead–acid battery stores typically 30 to 40 Wh/kg and modern lithium-ion batteries 100 to 265 Wh/kg. Supercapacitors can therefore store 10 to 100 times more energy than electrolytic capacitors, but only one tenth as much as batteries. For reference, petrol fuel has a specific energy of 44.4 MJ/kg or 12300 Wh/kg.

Although the specific energy of supercapacitors is defavorably compared with batteries, capacitors have the important advantage of the specific power. Specific power describes the speed at which energy can be delivered to the load (or, in charging the device, absorbed from the generator). The maximum power Pmax specifies the power of a theoretical rectangular single maximum current peak of a given voltage. In real circuits the current peak is not rectangular and the voltage is smaller, caused by the voltage drop, so IEC 62391–2 established a more realistic effective power Peff for supercapacitors for power applications, which is half the maximum and given by the following formulas :

$P_{\text{eff}}={\frac {1}{8}}\cdot {\frac {V^{2}}{R_{i}}}$

,

$P_{\text{max}}={\frac {1}{4}}\cdot {\frac {V^{2}}{R_{i}}}$

with V = voltage applied and Ri, the internal DC resistance of the capacitor.

Just like specific energy, specific power is measured either gravimetrically in kilowatts per kilogram (kW/kg, specific power) or volumetrically in kilowatts per litre (kW/L, power density). Supercapacitor specific power is typically 10 to 100 times greater than for batteries and can reach values up to 15 kW/kg.

Ragone charts relate energy to power and are a valuable tool for characterizing and visualizing energy storage components. With such a diagram, the position of specific power and specific energy of different storage technologies is easily to compare, see diagram.

### Lifetime

Since supercapacitors do not rely on chemical changes in the electrodes (except for those with polymer electrodes), lifetimes depend mostly on the rate of evaporation of the liquid electrolyte. This evaporation is generally a function of temperature, current load, current cycle frequency and voltage. Current load and cycle frequency generate internal heat, so that the evaporation-determining temperature is the sum of ambient and internal heat. This temperature is measurable as core temperature in the center of a capacitor body. The higher the core temperature, the faster the evaporation, and the shorter the lifetime.

Evaporation generally results in decreasing capacitance and increasing internal resistance. According to IEC/EN 62391-2, capacitance reductions of over 30%, or internal resistance exceeding four times its data sheet specifications, are considered "wear-out failures", implying that the component has reached end-of-life. The capacitors are operable, but with reduced capabilities. Whether the aberration of the parameters have any influence on the proper functionality depends on the application of the capacitors.

Such large changes of electrical parameters specified in IEC/EN 62391-2 are usually unacceptable for high current load applications. Components that support high current loads use much smaller limits, *e.g.*, 20% loss of capacitance or double the internal resistance. The narrower definition is important for such applications, since heat increases linearly with increasing internal resistance, and the maximum temperature should not be exceeded. Temperatures higher than specified can destroy the capacitor.

The real application lifetime of supercapacitors, also called "service life," "life expectancy", or "load life", can reach 10 to 15 years or more, at room temperature. Such long periods cannot be tested by manufacturers. Hence, they specify the expected capacitor lifetime at the maximum temperature and voltage conditions. The results are specified in datasheets using the notation "tested time (hours)/max. temperature (°C)," such as "5000 h/65 °C". With this value, and expressions derived from historical data, lifetimes can be estimated for lower temperature conditions.

Datasheet lifetime specification is tested by the manufactures using an accelerated aging test called an "endurance test", with maximum temperature and voltage over a specified time. For a "zero defect" product policy, no wear out or total failure may occur during this test.

The lifetime specification from datasheets can be used to estimate the expected lifetime for a given design. The "10-degrees-rule" used for electrolytic capacitors with non-solid electrolyte is used in those estimations, and can be used for supercapacitors. This rule employs the Arrhenius equation: a simple formula for the temperature dependence of reaction rates. For every 10 °C reduction in operating temperature, the estimated life doubles.

$L_{x}=L_{0}\cdot 2^{\frac {T_{0}-T_{x}}{10}}$

With:

- Lx = estimated lifetime
- L0 = specified lifetime
- T0 = upper specified capacitor temperature
- Tx = actual operating temperature of the capacitor cell

Calculated with this formula, capacitors specified with 5000 h at 65 °C, have an estimated lifetime of 20,000 h at 45 °C.

Lifetimes are also dependent on the operating voltage, because the development of gas in the liquid electrolyte depends on the voltage. The lower the voltage, the smaller the gas development, and the longer the lifetime. No general formula relates voltage to lifetime. The voltage dependent curves shown from the picture are an empirical result from one manufacturer.

Life expectancy for power applications may be also limited by current load or number of cycles. This limitation has to be specified by the relevant manufacturer and is strongly type dependent.

### Self-discharge

Storing electrical energy in the double-layer separates the charge carriers within the pores by distances in the range of molecules. Irregularities can occur over this short distance, leading to a small exchange of charge carriers and gradual discharge. This self-discharge is called leakage current. Leakage depends on capacitance, voltage, temperature, and the chemical stability of the electrode/electrolyte combination. At room temperature, leakage is so low that it is specified as time to self-discharge in hours, days, or weeks. As an example, a 5.5 V/F Panasonic "Goldcapacitor" specifies a voltage drop at 20 °C from 5.5 V to 3 V in 600 hours (25 days or 3.6 weeks) for a double cell capacitor.

### Post charge voltage relaxation

It has been noticed that after the EDLC experiences a charge or discharge, the voltage will drift over time, relaxing toward its previous voltage level. The observed relaxation can occur over several hours and is likely due to long diffusion time constants of the porous electrodes within the EDLC.

### Polarity

Since the positive and negative electrodes (or simply positrode and negatrode, respectively) of symmetric supercapacitors consist of the same material, theoretically supercapacitors have no true polarity and catastrophic failure does not normally occur. However reverse-charging a supercapacitor lowers its capacity, so it is recommended practice to maintain the polarity resulting from the formation of the electrodes during production. Asymmetric supercapacitors are inherently polar.

Pseudocapacitor and hybrid supercapacitors which have electrochemical charge properties may not be operated with reverse polarity, precluding their use in AC operation. However, this limitation does not apply to EDLC supercapacitors

A bar in the insulating sleeve identifies the negative terminal in a polarized component.

In some literature, the terms "anode" and "cathode" are used in place of negative electrode and positive electrode. Using anode and cathode to describe the electrodes in supercapacitors (and also rechargeable batteries, including lithium-ion batteries) can lead to confusion, because the polarity changes depending on whether a component is considered as a generator or as a consumer of current. In electrochemistry, cathode and anode are related to reduction and oxidation reactions, respectively. However, in supercapacitors based on electric double-layer capacitance, there is no oxidation nor reduction reactions on any of the two electrodes. Therefore, the concepts of cathode and anode do not apply.

### Comparison of selected commercial supercapacitors

The range of electrodes and electrolytes available yields a variety of components suitable for diverse applications. The development of low-ohmic electrolyte systems, in combination with electrodes with high pseudocapacitance, enable many more technical solutions.

The following table shows differences among capacitors of various manufacturers in capacitance range, cell voltage, internal resistance (ESR, DC or AC value) and volumetric and gravimetric specific energy. In the table, ESR refers to the component with the largest capacitance value of the respective manufacturer. Roughly, they divide supercapacitors into two groups. The first group offers greater ESR values of about 20 milliohms and relatively small capacitance of 0.1 to 470 F. These are "double-layer capacitors" for memory back-up or similar applications. The second group offers 100 to 10,000 F with a significantly lower ESR value under 1 milliohm. These components are suitable for power applications. A correlation of some supercapacitor series of different manufacturers to the various construction features is provided in Pandolfo and Hollenkamp.

In commercial double-layer capacitors, or, more specifically, EDLCs in which energy storage is predominantly achieved by double-layer capacitance, energy is stored by forming an electrical double layer of electrolyte ions on the surface of conductive electrodes. Since EDLCs are not limited by the electrochemical charge transfer kinetics of batteries, they can charge and discharge at a much higher rate, with lifetimes of more than 1 million cycles. The EDLC energy density is determined by operating voltage and the specific capacitance (farad/gram or farad/cm3) of the electrode/electrolyte system. The specific capacitance is related to the Specific Surface Area (SSA) accessible by the electrolyte, its interfacial double-layer capacitance, and the electrode material density.

Commercial EDLCs are based on two symmetric electrodes impregnated with electrolytes comprising tetraethylammonium tetrafluoroborate salts in organic solvents. Current EDLCs containing organic electrolytes operate at 2.7 V and reach energy densities around 5-8 Wh/kg and 7 to 10 Wh/L. The specific capacitance is related to the specific surface area (SSA) accessible by the electrolyte, its interfacial double-layer capacitance, and the electrode material density. Graphene-based platelets with mesoporous spacer material is a promising structure for increasing the SSA of the electrolyte.


## Standards

Supercapacitors vary sufficiently that they are rarely interchangeable, especially those with higher specific energy. Applications range from low to high peak currents, requiring standardized test protocols.

Test specifications and parameter requirements are specified in the generic specification IEC/EN 62391–1, *Fixed electric double layer capacitors for use in electronic equipment*.

The standard defines four application classes, according to discharge current levels:

1. Memory backup
2. Energy storage, mainly used for driving motors require a short time operation,
3. Power, higher power demand for a long time operation,
4. Instantaneous power, for applications that requires relatively high current units or peak currents ranging up to several hundreds of amperes even with a short operating time

Three further standards describe special applications:

- IEC 62391–2, *Fixed electric double-layer capacitors for use in electronic equipment – Blank detail specification – Electric double-layer capacitors for power application*
- IEC 62576, *Electric double-layer capacitors for use in hybrid electric vehicles. Test methods for electrical characteristics*
- BS/EN 61881-3, *Railway applications. Rolling stock equipment. Capacitors for power electronics. Electric double-layer capacitors*


## Applications

Supercapacitors have advantages in applications where a large amount of power is needed for a relatively short time, where a very high number of charge/discharge cycles or a longer lifetime is required. Typical applications range from milliamp currents or milliwatts of power for up to a few minutes to several amps current or several hundred kilowatts power for much shorter periods.

Supercapacitors do not support alternating current (AC) applications.

### Consumer electronics

In applications with fluctuating loads, such as laptop computers, PDAs, GPS, portable media players, hand-held devices, and photovoltaic systems, supercapacitors can stabilize the power supply.

Supercapacitors deliver power for photographic flashes in digital cameras and for LED flashlights that can be charged in much shorter periods of time, *e.g.*, 90 seconds.

Some portable speakers are powered by supercapacitors.

A cordless electric screwdriver with supercapacitors for energy storage has about half the run time of a comparable battery model, but can be fully charged in 90 seconds. It retains 85% of its charge after three months left idle.

### Power generation and distribution

#### Grid power buffering

Numerous non-linear loads, such as EV chargers, HEVs, air conditioning systems, and advanced power conversion systems cause current fluctuations and harmonics. These current differences create unwanted voltage fluctuations and therefore power oscillations on the grid. Power oscillations not only reduce the efficiency of the grid, but can cause voltage drops in the common coupling bus, and considerable frequency fluctuations throughout the entire system. To overcome this problem, supercapacitors can be implemented as an interface between the load and the grid to act as a buffer between the grid and the high pulse power drawn from the charging station.

#### Low-power equipment power buffering

Supercapacitors provide backup or emergency shutdown power to low-power equipment such as RAM, SRAM, micro-controllers and PC Cards. They are the sole power source for low energy applications such as automated meter reading (AMR) equipment or for event notification in industrial electronics.

Supercapacitors buffer power to and from rechargeable batteries, mitigating the effects of short power interruptions and high current peaks. Batteries kick in only during extended interruptions, *e.g.*, if the mains power or a fuel cell fails, which lengthens battery life.

Uninterruptible power supplies (UPS) may be powered by supercapacitors, which can replace much larger banks of electrolytic capacitors. This combination reduces the cost per cycle, saves on replacement and maintenance costs, enables the battery to be downsized and extends battery life.

Supercapacitors provide backup power for actuators in wind turbine pitch systems, so that blade pitch can be adjusted even if the main supply fails.

#### Voltage stabilization

Supercapacitors can stabilize voltage fluctuations for powerlines by acting as dampers. Wind and photovoltaic systems exhibit fluctuating supply evoked by gusting or clouds that supercapacitors can buffer within milliseconds.

#### Micro grids

Micro grids are usually powered by clean and renewable energy. Most of this energy generation, however, is not constant throughout the day and does not usually match demand. Supercapacitors can be used for micro grid storage to instantaneously inject power when the demand is high and the production dips momentarily, and to store energy in the reverse conditions. They are useful in this scenario, because micro grids are increasingly producing power in DC, and capacitors can be utilized in both DC and AC applications. Supercapacitors work best in conjunction with chemical batteries. They provide an immediate voltage buffer to compensate for quick changing power loads due to their high charge and discharge rate through an active control system. Once the voltage is buffered, it is put through an inverter to supply AC power to the grid. Supercapacitors cannot provide frequency correction in this form directly in the AC grid.

#### Energy harvesting

Supercapacitors are suitable temporary energy storage devices for energy harvesting systems. In energy harvesting systems, the energy is collected from the ambient or renewable sources, *e.g.*, mechanical movement, light or electromagnetic fields, and converted to electrical energy in an energy storage device. For example, it was demonstrated that energy collected from RF (radio frequency) fields (using an RF antenna as an appropriate rectifier circuit) can be stored to a printed supercapacitor. The harvested energy was then used to power an application-specific integrated circuit (ASIC) for over 10 hours.

#### Batteries

The UltraBattery is a hybrid rechargeable lead-acid battery and a supercapacitor. Its cell construction contains a standard lead-acid battery positive electrode, standard sulphuric acid electrolyte and a specially prepared negative carbon-based electrode that store electrical energy with double-layer capacitance. The presence of the supercapacitor electrode alters the chemistry of the battery and affords it significant protection from sulfation in high rate partial state of charge use, which is the typical failure mode of valve regulated lead-acid cells used this way. The resulting cell performs with characteristics beyond either a lead-acid cell or a supercapacitor, with charge and discharge rates, cycle life, efficiency and performance all enhanced.

### Medical

Supercapacitors are used in defibrillators where they can deliver 500 joules to shock the heart back into sinus rhythm.

### Military

Supercapacitors' low internal resistance supports applications that require short-term high currents. Among the earliest uses were motor startup (cold engine starts, particularly with diesels) for large engines in tanks and submarines. Supercapacitors buffer the battery, handling short current peaks, reducing cycling and extending battery life. Further military applications that require high specific power are phased array radar antennae, laser power supplies, military radio communications, avionics displays and instrumentation, backup power for airbag deployment and GPS-guided missiles and projectiles.

### Transport

A primary challenge of all transport is reducing energy consumption and reducing CO 2 emissions. Recovery of braking energy (recuperation or regenerative braking) helps with both. This requires components that can quickly store and release energy over long times with a high cycle rate. Supercapacitors fulfill these requirements and are therefore used in various applications in transportation.

#### Aviation

In 2005, aerospace systems and controls company Diehl Luftfahrt Elektronik GmbH chose supercapacitors to power emergency actuators for doors and evacuation slides used in airliners, including the Airbus 380.

#### Rail

Supercapacitors can be used to supplement batteries in starter systems in diesel railroad locomotives with diesel–electric transmission. The capacitors capture the braking energy of a full stop and deliver the peak current for starting the diesel engine and acceleration of the train and ensures the stabilization of line voltage. Depending on the driving mode up to 30% energy saving is possible by recovery of braking energy. Low maintenance and environmentally friendly materials encouraged the choice of supercapacitors.

#### Plant machinery

Mobile hybrid Diesel–electric rubber tyred gantry cranes move and stack containers within a terminal. Lifting the boxes requires large amounts of energy. Some of the energy could be recaptured while lowering the load, resulting in improved efficiency. A triple hybrid forklift truck uses fuel cells and batteries as primary energy storage and supercapacitors to buffer power peaks by storing braking energy. They provide the fork lift with peak power over 30 kW. The triple-hybrid system offers over 50% energy savings compared with Diesel or fuel-cell systems. Supercapacitor-powered terminal tractors transport containers to warehouses. They provide an economical, quiet and pollution-free alternative to Diesel terminal tractors.

#### Light rail

Supercapacitors make it possible not only to reduce energy, but to replace overhead lines in historical city areas, so preserving the city's architectural heritage. This approach may allow many new light rail city lines to replace overhead wires that are too expensive to fully route.

In 2003 Mannheim adopted a prototype light-rail vehicle (LRV) using the MITRAC Energy Saver system from Bombardier Transportation to store mechanical braking energy with a roof-mounted supercapacitor unit. It contains several units each made of 192 capacitors with 2700 F / 2.7 V interconnected in three parallel lines. This circuit results in a 518 V system with an energy content of 1.5 kWh. For acceleration when starting this "on-board-system" can provide the LRV with 600 kW and can drive the vehicle up to 1 km without overhead line supply, thus better integrating the LRV into the urban environment. Compared to conventional LRVs or Metro vehicles that return energy into the grid, onboard energy storage saves up to 30% and reduces peak grid demand by up to 50%.

In 2009 supercapacitors enabled LRVs to operate in the historical city area of Heidelberg without overhead wires, thus preserving the city's architectural heritage. The SC equipment cost an additional €270,000 per vehicle, which was expected to be recovered over the first 15 years of operation. The supercapacitors are charged at stop-over stations when the vehicle is at a scheduled stop. In April 2011 German regional transport operator Rhein-Neckar, responsible for Heidelberg, ordered a further 11 units.

In 2009, Alstom and RATP equipped a Citadis tram with an experimental energy recovery system called "STEEM". The system is fitted with 48 roof-mounted supercapacitors to store braking energy, which provides tramways with a high level of energy autonomy by enabling them to run without overhead power lines on parts of its route, recharging while traveling on powered stop-over stations. During the tests, which took place between the Porte d'Italie and Porte de Choisy stops on line T3 of the tramway network in Paris, the tramset used an average of approximately 16% less energy.

In 2012 tram operator Geneva Public Transport began tests of an LRV equipped with a prototype roof-mounted supercapacitor unit to recover braking energy.

Siemens is delivering supercapacitor-enhanced light-rail transport systems that include mobile storage.

Hong Kong's South Island metro line is to be equipped with two 2 MW energy storage units that are expected to reduce energy consumption by 10%.

In August 2012 the CSR Zhuzhou Electric Locomotive corporation of China presented a prototype two-car light metro train equipped with a roof-mounted supercapacitor unit. The train can travel up 2 km without wires, recharging in 30 seconds at stations via a ground mounted pickup. The supplier claimed the trains could be used in 100 small and medium-sized Chinese cities. Seven trams (street cars) powered by supercapacitors were scheduled to go into operation in 2014 in Guangzhou, China. The supercapacitors are recharged in 30 seconds by a device positioned between the rails. That powers the tram for up to 4 kilometres (2.5 mi). As of 2017, Zhuzhou's supercapacitor vehicles are also used on the new Nanjing streetcar system, and are undergoing trials in Wuhan.

In 2012, in Lyon (France), the SYTRAL (Lyon public transportation administration) started experiments of a "way side regeneration" system built by Adetel Group which has developed its own energy saver named "NeoGreen" for LRV, LRT and metros.

In 2014 China began using trams powered with supercapacitors that are recharged in 30 seconds by a device positioned between the rails, storing power to run the tram for up to 4 km — more than enough to reach the next stop, where the cycle can be repeated.

In 2015, Alstom announced SRS, an energy storage system that charges supercapacitors on board a tram by means of ground-level conductor rails located at tram stops. This allows trams to operate without overhead lines for short distances. The system has been touted as an alternative to the company's ground-level power supply (APS) system, or can be used in conjunction with it, as in the case of the VLT network in Rio de Janeiro, Brazil, which opened in 2016.

CAF also offers supercapacitors on their Urbos 3 trams in the form of their ACR system.

#### Buses

Maxwell Technologies, an American supercapacitor maker, claimed that more than 20,000 hybrid buses use the devices to increase acceleration, particularly in China.

The first hybrid electric bus with supercapacitors in Europe came in 2001 in Nuremberg, Germany. It was MAN's so-called "Ultracapbus", and was tested in real operation in 2001/2002. The test vehicle was equipped with a diesel-electric drive in combination with supercapacitors. The system was supplied with 8 Ultracap modules of 80 V, each containing 36 components. The system worked with 640 V and could be charged/discharged at 400 A. Its energy content was 0.4 kWh with a weight of 400 kg.

The supercapacitors recaptured braking energy and delivered starting energy. Fuel consumption was reduced by 10 to 15% compared to conventional diesel vehicles. Other advantages included reduction of CO 2 emissions, quiet and emissions-free engine starts, lower vibration and reduced maintenance costs.

As of 2002 in Luzern, Switzerland an electric bus fleet called TOHYCO-Rider was tested. The supercapacitors could be recharged via an inductive contactless high-speed power charger after every transportation cycle, within 3 to 4 minutes.

In early 2005 Shanghai tested a new form of electric bus called capabus that runs without powerlines (catenary free operation) using large onboard supercapacitors that partially recharge whenever the bus is at a stop (under so-called electric umbrellas), and fully charge in the terminus. In 2006, two commercial bus routes began to use the capabuses; one of them is route 11 in Shanghai. It was estimated that the supercapacitor bus was cheaper than a lithium-ion battery bus, and one of its buses had one-tenth the energy cost of a diesel bus with lifetime fuel savings of $200,000.

A hybrid electric bus called tribrid was unveiled in 2008 by the University of Glamorgan, Wales, for use as student transport. It is powered by hydrogen fuel or solar cells, batteries and ultracapacitors.

#### Motor racing

The FIA, a governing body for motor racing events, proposed in the *Power-Train Regulation Framework for Formula 1* version 1.3 of 23 May 2007 that a new set of power train regulations be issued that includes a hybrid drive of up to 200 kW input and output power using "superbatteries" made with batteries and supercapacitors connected in parallel (KERS). About 20% tank-to-wheel efficiency could be reached using the KERS system. The Toyota TS030 Hybrid LMP1 car, a racing car developed under Le Mans Prototype rules, uses a hybrid drivetrain with supercapacitors. In the 2012 24 Hours of Le Mans race a TS030 qualified with a fastest lap only 1.055 seconds slower (3:24.842 versus 3:23.787) than the fastest car, an Audi R18 e-tron quattro with flywheel energy storage. The supercapacitor and flywheel components, whose rapid charge-discharge capabilities help in both braking and acceleration, made the Audi and Toyota hybrids the fastest cars in the race. In the 2012 Le Mans race the two competing TS030s, one of which was in the lead for part of the race, both retired for reasons unrelated to the supercapacitors. The TS030 won three of the 8 races in the 2012 FIA World Endurance Championship season. In 2014 the Toyota TS040 Hybrid used a supercapacitor to add 480 horsepower from two electric motors. In 2024 the IndyCar racing series introduced a hybrid power system composed of 20 supercapacitors.

#### Hybrid electric vehicles

Supercapacitor/battery combinations in electric vehicles (EV) and hybrid electric vehicles (HEV) are well investigated. A 20 to 60% fuel reduction has been claimed by recovering brake energy in EVs or HEVs. The ability of supercapacitors to charge much faster than batteries, their stable electrical properties, broader temperature range and longer lifetime are suitable, but weight, volume and especially cost mitigate those advantages.

Supercapacitors' lower specific energy makes them unsuitable for use as a stand-alone energy source for long-distance driving. The fuel economy improvement between a capacitor and a battery solution is about 20% and is available only for shorter trips. For long-distance driving the advantage decreases to 6%. Vehicles combining capacitors and batteries run only in experimental vehicles.

As of 2013 all automotive manufacturers of EV or HEVs have developed prototypes that uses supercapacitors instead of batteries to store braking energy in order to improve driveline efficiency. The Mazda 6 was reportedly the first production car to use supercapacitors to recover braking energy. Branded as i-eloop, the system stores energy in a supercapacitor during deceleration and uses it to power on-board electrical systems while the engine is stopped by the stop-start system. The regenerative braking is claimed to reduce fuel consumption by about 10%. The Toyota Yaris Hybrid-R concept car uses a supercapacitor to provide bursts of power. PSA Peugeot Citroën fit supercapacitors to some of its cars as part of its stop-start fuel-saving system, as this permits faster start-ups when the traffic lights turn green. Russian Yo-cars Ё-mobile series was a concept and crossover hybrid vehicle working with a gasoline driven rotary vane type and an electric generator for driving the traction motors. A supercapacitor with relatively low capacitance recovers brake energy to power the electric motor when accelerating from a stop.

#### Gondolas

In Zell am See, Austria, an aerial lift connects the city with Schmittenhöhe mountain. The gondolas sometimes run 24 hours per day, using electricity for lights, door opening and communication. The only available time for recharging batteries at the stations is during the brief intervals of guest loading and unloading, which is too short to recharge batteries. Supercapacitors offer a fast charge, higher number of cycles and longer life time than batteries. Emirates Air Line (cable car), also known as the Thames cable car, is a 1-kilometre (0.62 mi) gondola line in London, UK, that crosses the Thames from the Greenwich Peninsula to the Royal Docks. The cabins are equipped with a modern infotainment system, which is powered by supercapacitors.


## Supercapacitor assisted (SCA) techniques

Within the two decades (2005-2025) there was a new family of supercapacitor applications emerged and known as Supercapacitor Assisted (SCA) techniques, based on the research happening at the University of Waikato in Hamilton, New Zealand. This SCA techniques family includes unique types of DC-DC converters, lightning protection systems, DC circuit breakers and DC powered appliances such as white goods etc. These techniques developed by the Waikato Power Electronics Research (WaiPER) group under the leadership of Prof Nihal Kularatna has culminated several patents, research publications and some commercial products such as Prodigy 8 series.

Supercapacitor assisted low dropout regulator (SCALDO) is the first successful power converter technique under the SCA family. Supercapacitor assisted surge absorber (SCASA) is the first supercapacitor based surge protector technique which was commercialized by Thor Technologies, Perth, Australia. Supercapacitor assisted LED (SCALED) technique is a high efficiency DC lighting technique aimed at DC grid based future buildings. With future DC microgrid based DC systems developing, SCA Transient Energy Pump (SCATEP) based DC circuit breaker technique was also recently developed.

SCA techniques are based on a unique new theoretical concept now published as SCA Loss Management (SCALoM) theory and this new family of power converters and protection systems are aimed at future DC microgrids, DC homes and DC appliances based on renewable energy.
