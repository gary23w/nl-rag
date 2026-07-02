---
title: "State of charge"
source: https://en.wikipedia.org/wiki/State_of_charge
domain: lithium-battery-management
license: CC-BY-SA-4.0
tags: lithium-ion battery, battery management system, state of charge, battery balancing
fetched: 2026-07-02
---

# State of charge

**State of charge** (**SoC**) quantifies the remaining capacity available in a battery at a given time and in relation to a given state of ageing. It is usually expressed as percentage (0% = empty; 100% = full). An alternative form of the same measure is the depth of discharge (DoD), calculated as 1 − SoC (100% = empty; 0% = full). It refers to the amount of charge that may be used up if the cell is fully discharged. State of charge is normally used when discussing the present state of a battery in use, while depth of discharge is most often used to discuss a constant variation of state of charge during repeated cycles.

## In electric vehicles

In a battery electric vehicle (BEV), the state of charge indicates the remaining energy in the battery pack. It is the equivalent of a fuel gauge.

The state of charge can help to reduce electrical car owners' anxiety when they are waiting in the line or stay at home since it will reflect the progress of charging and let owners know when it will be ready. However on any vehicle dashboard, especially in plug-in hybrid vehicles, the state of charge presented as a gauge or percentage value may not be representative of a real level of charge. A noticeable amount of energy may be reserved for hybrid-work operations. Examples of such cars are Mitsubishi Outlander PHEV (all versions/years of production), where a charge level of zero is indicated to the driver when the real charge level is 20–22%. Another one is the BMW i3 REX (Range Extender version), where about 6% of SoC is reserved for PHEV-alike operations.

State of charge is also known to impact battery aging. To extend battery lifetime, extremes of state of charge should be avoided and reduced variations windows are also preferable.

## Determining SoC

Usually, SoC cannot be measured directly but it can be estimated from direct measurement variables in two ways: offline and online. In offline techniques, the battery desires to be charged and discharged in constant rate such as Coulomb-counting. This method gives precise estimation of battery SoC, but they are protracted, costly, and interrupt main battery performance. Therefore, researchers are looking for some online techniques. In general there are five methods to determine SoC indirectly:

- chemical
- voltage
- current integration
- Kalman filtering
- pressure

### Chemical method

This method works only with batteries that offer access to their liquid electrolyte, such as non-sealed lead acid batteries. The specific gravity of the electrolyte can be used to indicate the SoC of the battery.

Hydrometers are used to calculate the specific gravity of a battery. To find specific gravity, it is necessary to measure out volume of the electrolyte and to weigh it. Then specific gravity is given by (mass of electrolyte [g]/ volume of electrolyte [ml])/ (Density of Water, i.e. 1g/1ml). To find SoC from specific gravity, a look-up table of SG vs SoC is needed.

Refractometry has been shown to be a viable method for continuous monitoring of the state of charge. The refractive index of the battery electrolyte is directly relatable to the specific gravity or density of the electrolyte of the cell.

Notably, analysis of electrolyte does not provide information about the state-of-charge in the case of lithium-ion batteries and other batteries, that do not produce or consume solvent or dissolved species during their operation. The method works for lead-acid batteries, because the concentration of sulfuric acid changes with the battery's state-of-charge according to the following reaction:

Pb

(s) +

PbO

2

(s) + 2

H

2

SO

4

(aq) → 2

PbSO

4

(s) + 2

H

2

O

(l)

$E_{cell}^{\circ }=2.05{\text{ V}}$

### Voltage method

This method converts a reading of the battery voltage to SoC, using the known discharge curve (voltage vs. SoC) of the battery. However, the voltage is more significantly affected by the battery current (due to the battery's electrochemical kinetics) and temperature. This method can be made more accurate by compensating the voltage reading by a correction term proportional to the battery current, and by using a look-up table of battery's open circuit voltage vs. temperature.

In fact, it is a stated goal of battery design to provide a voltage as constant as possible no matter the SoC, which makes this method difficult to apply. For batteries, that have voltage independent on their state-of-charge (such as lithium iron phosphate battery), open-circuit voltage measurements cannot provide a reliable estimate of the SoC. On the other hand, batteries with a sloping voltage-charge curves (such as nickel-cobalt-manganese battery), are more amenable to SoC estimation from the open-circuit voltage measurements.

### Current integration method

This method, also known as *coulomb counting*, calculates the SoC by measuring the battery current and integrating it in time. Since no measurement can be perfect, this method suffers from long-term drift and lack of a reference point: therefore, the SoC must be re-calibrated on a regular basis, such as by resetting the SoC to 100% when a charger determines that the battery is fully charged (using one of the other methods described here).

### Combined approaches

Maxim Integrated touts a combined voltage and charge approach that is claimed superior to either method alone; it is implemented in their ModelGauge m3 series of chips, such as MAX17050, which is used in the Nexus 6 and Nexus 9 Android devices, for example.

### Kalman filtering

To overcome the shortcomings of the voltage method and the current integration method, a Kalman filter can be used. The battery can be described with an electrical model which the Kalman filter will use to predict the over-voltage given the observed current. In combination with coulomb counting, it can make an accurate estimation of the state of charge. The strength of this technique is that a Kalman filter adjusts its relative trust of the battery voltage and coulomb counting in real time.

### Pressure method

This method can be used with certain NiMH batteries, whose internal pressure increases rapidly when the battery is charged. More commonly, a pressure switch indicates if the battery is fully charged. This method may be improved by taking into account Peukert's law which is a function of charge/discharge current.
