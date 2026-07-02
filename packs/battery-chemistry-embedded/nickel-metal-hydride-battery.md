---
title: "Nickel–metal hydride battery"
source: https://en.wikipedia.org/wiki/Nickel%E2%80%93metal_hydride_battery
domain: battery-chemistry-embedded
license: CC-BY-SA-4.0
tags: rechargeable battery, nickel metal hydride battery, lead acid battery, energy density
fetched: 2026-07-02
---

# Nickel–metal hydride battery

A **nickel–metal hydride battery** (**NiMH** or **Ni–MH**) is a type of rechargeable battery. The chemical reaction at the positive electrode is similar to that of the older nickel–cadmium cell (NiCd), with both using nickel oxide hydroxide, NiO(OH). However, the negative electrodes use a hydrogen-absorbing alloy instead of cadmium. NiMH batteries typically have two to three times the capacity of NiCd batteries of the same size, with significantly higher energy density, although only about half that of lithium-ion batteries. NiMH batteries have almost entirely replaced NiCd.

These batteries are typically used as a substitute for similarly shaped non-rechargeable alkaline and other primary batteries. They provide a cell voltage of about 1.2V while fresh alkaline cells provide 1.5V; however devices designed for alkaline batteries operate until cell voltage gradually drops to around 1.0V, while the voltage of a fully-charged NiMH cell drops more slowly, giving good endurance for a 1.0V end point. NiMH batteries are less prone to leaking corrosive electrolyte than primary batteries.

## History

Work on NiMH batteries began at the Battelle-Geneva Research Center following the technology's invention in 1967. It was based on sintered Ti2Ni+TiNi+x alloys and NiOOH electrodes. Development was sponsored over nearly two decades by Daimler-Benz and by Volkswagen AG within Deutsche Automobilgesellschaft, now a subsidiary of Daimler AG. The batteries' specific energy reached 50 W·h/kg (180 kJ/kg), specific power up to 1000 W/kg and a life of 500 charge cycles (at 100% depth of discharge). Patent applications were filed in European countries (priority: Switzerland), the United States, and Japan. The patents transferred to Daimler-Benz.

Interest grew in the 1970s with the commercialisation of the nickel–hydrogen battery for satellite applications. Hydride technology promised an alternative, less bulky way to store the hydrogen. Research carried out by Philips Laboratories and France's CNRS developed new high-energy hybrid alloys incorporating rare-earth metals for the negative electrode. However, these suffered from alloy instability in alkaline electrolyte and consequently insufficient cycle life. In 1987, Willems and Buschow demonstrated a successful battery based on this approach (using a mixture of La0.8Nd0.2Ni2.5Co2.4Si0.1), which kept 84% of its charge capacity after 4000 charge-discharge cycles. More economically viable alloys using mischmetal instead of lanthanum were soon developed. Modern NiMH cells were based on this design. The first consumer-grade NiMH cells became commercially available in 1989.

In 1998, Stanford Ovshinsky at Ovonic Battery Co., which had been working on MH-NiOOH batteries since mid-1980, improved the Ti–Ni alloy structure and composition and patented its innovations.

In 2008, more than two million hybrid cars worldwide were manufactured with NiMH batteries.

In the European Union due to its Battery Directive, nickel–metal hydride batteries replaced Ni–Cd batteries for portable consumer use.

In Switzerland in 2009, approximately 60% of portable rechargeable batteries were NiMH. In 2000, almost half of all portable rechargeable batteries sold in Japan were NiMH, compared to 22% in 2010. This percentage has fallen over time due to the increase in manufacture of lithium-ion batteries.

In 2015 BASF produced a modified microstructure that helped make NiMH batteries more durable, in turn allowing changes to the cell design that saved considerable weight, allowing the specific energy to reach 140 watt-hours per kilogram.

## Electrochemistry

The negative electrode reaction occurring in a NiMH cell is

H

2

O + M + e

−

⇌

OH

−

+ MH

On the positive electrode, nickel oxyhydroxide, NiO(OH), is formed:

Ni(OH)

2

+ OH

−

⇌

NiO(OH) + H

2

O + e

−

The reactions proceed left to right during charge and the opposite during discharge. The metal M in the negative electrode of a NiMH cell is an intermetallic compound. Many different compounds have been developed for this application, but those in current use fall into two classes. The most common is AB5, where A is a rare-earth mixture of lanthanum, cerium, neodymium, praseodymium, and B is nickel, cobalt, manganese, or aluminium. Some cells use higher-capacity negative electrode materials based on AB2 compounds, where A is titanium or vanadium, and B is zirconium or nickel, modified with chromium, cobalt, iron, or manganese.

NiMH cells have an alkaline electrolyte, usually potassium hydroxide. The positive electrode is nickel hydroxide, and the negative electrode is hydrogen in the form of an interstitial metal hydride. Hydrophilic polyolefin nonwovens are used for separation.

## Charge

When fast-charging, it is advisable to charge the NiMH cells with a smart battery charger to avoid overcharging, which can damage cells.

### Trickle charging

The simplest of the safe charging methods is with a fixed low current, with or without a timer. Most manufacturers claim that overcharging is safe at very low currents, below 0.1 *C* (*C*/10) (where *C* is the current equivalent to the capacity of the battery divided by one hour). The Panasonic NiMH charging manual warns that overcharging for long enough can damage a battery and suggests limiting the total charging time to 10–20 hours.

Duracell suggests that a trickle charge at *C*/300 can be used for batteries that must be kept in a fully charged state. Some chargers do this after the charge cycle, to offset natural self-discharge. A similar approach is suggested by Energizer, which indicates that self-catalysis can recombine gas formed at the electrodes for charge rates up to C/10. This leads to cell heating. The company recommends *C*/30 or *C*/40 for indefinite applications where long life is important. This is the approach taken in emergency lighting applications, where the design remains essentially the same as in older NiCd units, except for an increase in the trickle-charging resistor value.

Panasonic's handbook recommends that NiMH batteries on standby be charged by a lower duty cycle approach, where a pulse of a higher current is used whenever the battery's voltage drops below 1.3 V. This can extend battery life and use less energy.

### Δ*V* charging method

To prevent cell damage, fast chargers must terminate their charge cycle before overcharging occurs. One method is to monitor the change of voltage with time. When the battery is fully charged, the voltage across its terminals drops slightly. The charger can detect this and stop charging. This method is often used with nickel–cadmium cells, which display a large voltage drop at full charge. However, the voltage drop is much less pronounced for NiMH and can be non-existent at low charge rates, which can make the approach unreliable.

Another option is to monitor the change of voltage with respect to time and stop when this becomes zero, but this risks premature cutoffs. With this method, a much higher charging rate can be used than with a trickle charge, up to 1 *C*. At this charge rate, Panasonic recommends to terminate charging when the voltage drops 5–10 mV per cell from the peak voltage. Since this method measures the voltage across the battery, a constant-current (rather than a constant-voltage) charging circuit is used.

### Δ*T* charging method

The temperature-change method is similar in principle to the Δ*V* method. Because the charging voltage is nearly constant, constant-current charging delivers energy at a near-constant rate. When the cell is not fully charged, most of this energy is converted to chemical energy. However, when the cell reaches full charge, most of the charging energy is converted to heat. This increases the rate of change of battery temperature, which can be detected by a sensor such as a thermistor. Both Panasonic and Duracell suggest a maximal rate of temperature increase of 1 °C per minute. Using a temperature sensor allows an absolute temperature cutoff, which Duracell suggests at 60 °C. With both the Δ*T* and the Δ*V* charging methods, both manufacturers recommend a further period of trickle charging to follow the initial rapid charge.

### Safety

A resettable fuse in series with the cell, particularly of the bimetallic strip type, increases safety. This fuse opens if either the current or the temperature gets too high.

Modern NiMH cells contain catalysts to handle gases produced by over-charging:

${\ce {2H2{}+O2->[{\overset {}{\text{catalyst}}}]2H2O}}$

However, this only works with overcharging currents of up to 0.1 *C* (that is, nominal capacity divided by ten hours). This reaction causes batteries to heat, ending the charging process.

A method for very rapid charging called in-cell charge control involves an internal pressure switch in the cell, which disconnects the charging current in the event of overpressure.

One inherent risk with NiMH chemistry is that overcharging causes hydrogen gas to form, potentially rupturing the cell. Therefore, cells have a vent to release the gas in the event of serious overcharging.

NiMH batteries are made of environmentally friendly materials. The batteries contain only mildly toxic substances and are recyclable.

### Loss of capacity

Voltage depression (often mistakenly attributed to the memory effect) from repeated partial discharge can occur, but is reversible with a few full discharge/charge cycles.

## Discharge

A fully charged cell supplies an average 1.25 V/cell during discharge, declining to about 1.0–1.1 V/cell (further discharge may cause permanent damage in the case of multi-cell packs, due to polarity reversal of the weakest cell). Under a light load (0.5 amperes), the starting voltage of a freshly charged AA NiMH cell in good condition is about 1.4 volts.

### Over-discharge

Complete discharge of multi-cell packs can cause reverse polarity in one or more cells, which can permanently damage them. This situation can occur in the common arrangement of four AA cells in series, where one cell completely discharges before the others due to small differences in capacity among the cells. When this happens, the good cells start to drive the discharged cell into reverse polarity (i.e. positive anode and negative cathode). Some cameras, GPS receivers and PDAs detect the safe end-of-discharge voltage of the series cells and perform an auto-shutdown, but devices such as flashlights/torches and some toys do not.

Irreversible damage from polarity reversal is a particular danger, even when a low voltage-threshold cutout is employed, when the cells vary in temperature. This is because capacity significantly declines as the cells are cooled. This results in a lower voltage under load of the colder cells.

### Self-discharge

Historically, NiMH cells have had a somewhat higher self-discharge rate (equivalent to internal leakage) than NiCd cells. The self-discharge rate varies greatly with temperature, where lower storage temperature leads to slower discharge and longer battery life. The self-discharge is 5–20% on the first day and stabilizes around 0.5–4% per day at room temperature. But at 45 °C (113 °F) it is approximately three times as high.

### Low self-discharge

The **low–self-discharge nickel–metal hydride battery** (**LSD NiMH**) has a significantly lower rate of self-discharge. The innovation was introduced in 2005 by Sanyo, branded Eneloop. By using improvements to electrode separator, positive electrode, and other components, manufacturers claim the cells retain 70–85% of their capacity when stored for one year at 20 °C (68 °F), compared to about half for normal NiMH batteries. They are otherwise similar to standard NiMH batteries, and can be charged in standard NiMH chargers. These cells are marketed as "hybrid", "ready-to-use" or "pre-charged" rechargeables. Retention of charge depends in large part on the battery's resistance to leakage (the higher the better), and on its physical size and charge capacity.

Separators keep the two electrodes apart to slow electrical discharge while allowing the transport of ionic charge carriers that close the circuit during the passage of current. High-quality separators are critical for battery performance.

The self-discharge rate depends upon separator thickness; thicker separators reduce self-discharge, but also reduce capacity as they leave less space for active components, and thin separators lead to higher self-discharge. Some batteries may have overcome this tradeoff by using more precisely manufactured thin separators, and a sulfonated polyolefin separator, an improvement over the hydrophilic polyolefin based on ethylene vinyl alcohol.

Low-self-discharge cells have somewhat lower capacity than otherwise equivalent NiMH cells because of the larger volume of the separator. The highest-capacity low-self-discharge AA cells have 2500 mAh capacity, compared to 2700 mAh for high-capacity AA NiMH cells.

Common methods to improve self-discharge include: use of a sulfonated separator (causing removal of N-containing compounds), use of an acrylic acid grafted PP separator (causing reduction in Al- and Mn-debris formation in separator), removal of Co and Mn in A2B7 MH alloy, (causing reduction in debris formation in separator), increase of the amount of electrolyte (causing reduction in the hydrogen diffusion in electrolyte), removal of Cu-containing components (causing reduction in micro-short), PTFE coating on positive electrode (causing suppression of reaction between NiOOH and H2), CMC solution dipping (causing suppression of oxygen evolution), micro-encapsulation of Cu on MH alloy (causing decrease in H2 released from MH alloy), Ni–B alloy coating on MH alloy (causing formation of a protection layer), alkaline treatment of negative electrode (causing reduction of leach-out of Mn and Al), addition of LiOH and NaOH into electrolyte (causing reduction in electrolyte corrosion capabilities), and addition of Al2(SO4)3 into electrolyte (causing reduction in MH alloy corrosion). Most of these improvements have no or negligible effect on cost; some increase cost modestly.

## Compared to other battery types

### Alkaline and other primary batteries

NiMH cells are often used in digital cameras and other high-drain devices, where they outperform primary batteries, usually using alkaline chemistry, but also inferior zinc-carbon and chloride.

NiMH cells are better for high-current-drain applications than alkaline batteries due to their lower internal resistance. Typical alkaline AA-size batteries, which offer approximately 2.6 Ah capacity at low current demand (25 mA), provide only 1.3 Ah capacity with a 500 mA load. Digital cameras with LCDs and flashlights can draw over 1 A, quickly depleting them. NiMH cells can deliver these current levels without similar loss of capacity.

Alkaline (and other technologies such as zinc-carbon or chloride) primary (disposable) batteries supply a voltage of 1.5V when fresh but gradually decreasing in use, and devices using them are usually designed to operate up to an end-point voltage of about 1.0V. NiMH batteries supply 1.2V initially, but the voltage does not decrease as rapidly until the battery is nearly depleted due to their low internal resistance, giving reasonable endurance for a 1.0V end point, so that NiMH batteries can replace primary batteries in almost all applications despite the lower initial voltage. Battery-level indicators designed for alkaline batteries are inaccurate with the lower initial voltage but slower decrease of NiMH.

### Lithium-ion

Lithium-ion batteries can deliver extremely high power and have a higher specific energy than nickel–metal hydride batteries, but they were originally significantly more expensive. The cost of lithium batteries fell drastically during the 2010s and many small consumer devices now have non-consumer-replaceable lithium batteries as a result. Lithium batteries produce a higher voltage (3.2–3.7 V nominal), and are thus not a drop-in replacement for AA (alkaline or NiMh) batteries without circuitry to reduce voltage. Although a single lithium cell will typically provide ideal power to replace 3 NiMH cells, the form factor means that the device still needs modification.

### Lead

NiMH batteries can easily be made smaller and lighter than lead-acid batteries and have completely replaced them in small devices. However, lead-acid batteries can deliver huge current at low cost, making lead-acid batteries more suitable for starter motors in combustion vehicles.

As of 2005, nickel–metal hydride batteries constituted three percent of the battery market.

## Applications

### Consumer electronics

NiMH batteries have replaced NiCd for many roles, notably small rechargeable batteries. NiMH batteries are commonly available in AA (penlight-size) batteries. These have nominal charge capacities (*C*) of 1.1–2.8 Ah at 1.2 V, measured at the rate that discharges the cell in 5 hours. Useful discharge capacity is a decreasing function of the discharge rate, but up to a rate of around 1×*C* (full discharge in 1 hour), it does not differ significantly from the nominal capacity. Fully charged NiMH batteries nominally operate at 1.2 V per cell, somewhat lower than fresh 1.5 V disposable cells, but most devices are designed to continue operating until the voltage drops to about 1.0V, so NiMH batteries can replace alkaline batteries without loss of performance.

### Electric vehicles

NiMH batteries were frequently used in prior-generation electric and hybrid-electric vehicles; as of 2020 they have been superseded almost entirely by lithium-ion batteries in all-electric and plug-in hybrid vehicles, but they remain in use in some hybrid vehicles (2020 Toyota Highlander, for example). Prior all-electric plug-in vehicles included the General Motors EV1, first-generation Toyota RAV4 EV, Honda EV Plus, Ford Ranger EV and Vectrix scooter. Every first generation hybrid vehicle used NIMH batteries, most notably the Toyota Prius and Honda Insight, as well as later models including the Ford Escape Hybrid, Chevrolet Malibu Hybrid and Honda Civic Hybrid also use them.

#### Patent issues

Stanford R. Ovshinsky invented and patented a popular improvement of the NiMH battery and founded Ovonic Battery Company in 1982. General Motors purchased Ovonics' patent in 1994. By the late 1990s, NiMH batteries were being used successfully in many fully electric vehicles, such as the General Motors EV1 and Dodge Caravan EPIC minivan.

This generation of electric cars, although successful, was abruptly pulled off the market.

In October 2000, the patent was sold to Texaco, and a week later Texaco was acquired by Chevron. Chevron's Cobasys subsidiary provides these batteries only to large OEM orders. General Motors shut down production of the EV1, citing lack of battery availability as a chief obstacle. Cobasys control of NiMH batteries created a patent encumbrance for large automotive NiMH batteries.
