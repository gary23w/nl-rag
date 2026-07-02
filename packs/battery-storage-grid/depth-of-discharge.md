---
title: "Depth of discharge"
source: https://en.wikipedia.org/wiki/Depth_of_discharge
domain: battery-storage-grid
license: CC-BY-SA-4.0
tags: battery storage power station, battery management system, state of charge, grid energy storage
fetched: 2026-07-02
---

# Depth of discharge

**Depth of discharge** (**DoD**) is an important parameter appearing in the context of rechargeable battery operation. Two non-identical definitions can be found in commercial and scientific sources. The depth of discharge is defined as:

1. the maximum fraction of a battery's capacity (given in Ah) which is removed from the charged battery on a regular basis. "*Charged"* does not necessarily refer to *fully or 100% charged*, but rather to the state of charge (SoC), where the battery charger stops charging, which is achieved by different techniques.
2. the fraction of the battery's capacity which is *currently* removed from the battery with regard to its (fully) charged state. For fully charged batteries, the depth of discharge is connected to the state of charge by the simple formula $\mathrm {DoD} =1-\mathrm {SoC}$ . The depth of discharge then is the complement of state of charge: as one increases, the other decreases. This definition is mostly found in scientific sources.

The depth of discharge can therefore (1) refer to the size of the range usually used for discharge or (2) the *current* amount of charge or fraction of the capacity removed from the battery. To avoid confusion, the exact meaning of DoD should be clear for a given context. Also, for both definitions, it remains undefined, whether a charged battery's SoC is 100 % or another value. This reference value is needed to fully describe (1) the *upper and lower limit* of absolute SoC used for operation or (2) the *current value* of the absolute SoC.

## Occurrence

During their use, secondary batteries are repeatedly charged and discharged within a certain range of state of charge. For many battery types, it is beneficial or even mandatory for safety reasons, to not encounter overcharging and/or deep discharge. To prevent adverse effects, a battery management system or battery charger may keep the battery from extreme levels regarding SoC, thereby limiting the SoC to a reduced range between 0 % and 100 % and decreasing *depth of discharge* below 100 % (see example below). This corresponds to the DoD in the sense of definition (1).

For almost all known rechargeable battery technologies, such as lead-acid batteries of all kinds like AGM, there is a correlation between the depth of discharge and the cycle life of the battery. For LiFePO 4 batteries, for example, the state of charge is often limited to the range between 15 % and 85 % to greatly increase their cycle life, resulting in a DoD of 70 %.

While the state of charge is usually expressed using percentage points (0 % = empty; 100 % = full), depth of discharge is either expressed using units of Ah (e.g. for a 50 Ah battery, 0 Ah is full and 50 Ah is empty) or percentage points (100 % is empty and 0 % is full). The capacity of a battery may also be higher than its nominal rating. Thus it is possible for the depth of discharge value to exceed the nominal value (e.g., 55 Ah for a 50 Ah battery, or 110 %).

## Sample calculation

Using definition (2), the depth of discharge of a charged 90 Ah battery is discharged for 20 minutes at a constant current of 50 A is calculated by:

$\mathrm {DoD} ={\frac {50{\text{ A}}\cdot {\frac {20{\text{ mins}}}{60{\text{ mins}}}}{\text{ hours}}}{90{\text{ Ah}}}}\cdot 100\%=18.522\%.$

## Deep discharge
