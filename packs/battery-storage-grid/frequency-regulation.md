---
title: "Ancillary services"
source: https://en.wikipedia.org/wiki/Frequency_regulation
domain: battery-storage-grid
license: CC-BY-SA-4.0
tags: battery storage power station, battery management system, state of charge, grid energy storage
fetched: 2026-07-02
---

# Ancillary services

(Redirected from

Frequency regulation

)

**Ancillary services** are the services necessary to support the transmission of electric power from generators to consumers given the obligations of control areas and transmission utilities within those control areas to maintain reliable operations of the interconnected transmission system.

"Ancillary services are all services required by the transmission or distribution system operator to enable them to maintain the integrity and stability of the transmission or distribution system as well as the power quality".

Ancillary services are specialty services and functions provided by actors within the electric grid that facilitate and support the continuous flow of electricity, so that the demand for electrical energy is met in real time. The term ancillary services is used to refer to a variety of operations beyond generation and transmission that are required to maintain grid stability and security. These services generally include active power control or frequency control and reactive power control or voltage control, on various timescales. Traditionally, ancillary services have been provided by large production units such as synchronous generators. With the integration of more intermittent generation and the development of smart grid technologies, the provision of ancillary services is extended to smaller distributed generation and consumption units.

## Types of ancillary services

There are two broad categories of ancillary services:

- Frequency related: Inertia, Primary frequency control such as Frequency Containment Reserve (FCR), secondary frequency control such as and Frequency Restoration Reserve (FRR)
- Non-frequency related: reactive power and voltage control and congestion management

Other types of ancillary services provision include:

- system restart
- scheduling and dispatch
- loss compensation
- load following
- system protection
- energy imbalance

### Frequency control

Electricity frequency is directly connected to the balance of consumption and generation of active power ( $\Delta P=P_{generation}-P_{consume}$ ) and the total rotating energy ( $W_{tot,kin}$ ) of the synchronous power system. During a sudden change of $\Delta P$ the frequency will initially (before any remedial actions) change according to the following equation:

${\frac {df}{dt}}={\frac {\Delta P\cdot f}{2\cdot W_{kin}}}$

The equation can be rewritten using the normalized inertial constant H :

${\frac {df}{dt}}={\frac {\Delta P\cdot f}{2\cdot H\cdot S}}$

Where S is the total exchange of active power for the entire grid and H is the normalized inertia constant for the system. A system with a small amount of total rotating kinetic energy will be more sensitive to deviations in $\Delta P$ , as the frequency's derivative will be more significantly affected.

As the total inertia of synchronous grids decreases due to the increasing integration of renewable generation sources, the methodologies and requirements for enabling converter-based generation units to control grid frequency with greater speed and precision are becoming more important.

Frequency control refers to the need to ensure that the grid frequency stays within a specific range of the nominal frequency. Mismatch between electricity generation and demand causes variations in frequency, so control services are required to bring the frequency back to its nominal value and ensure it does not vary out of range.

If we have a graph for a generator where frequency is on the vertical axis and power is on the horizontal axis:

$slope=-R={\frac {\Delta f}{\Delta P_{m}}}$

where Pm is the change in power of the system. If we have multiple generators, each might have its own R. Beta can be found by:

$\beta ={\frac {1}{R_{1}}}+{\frac {1}{R_{2}}}+...+{\frac {1}{R_{n}}}$

The change in frequency due to a change in power can be found with:

$\Delta f={\frac {\Delta P_{m}}{\beta }}$

This simple equation can be rearranged to find the change in power that corresponds to a given change in frequency.

### Reactive power and voltage control

Consumer loads expect voltage within a certain range, and the regulators require it be within a certain percent of the nominal voltage (for example, in the US it is ±5%).

Reactive power can be used to compensate the voltage drops, but must be provided closer to the loads than real power needs (this is because reactive power tend to travel badly through the grid). Notice that voltage can be controlled also using transformer taps and voltage regulators.

### Scheduling and dispatch

Scheduling and dispatch are necessary because in most electrical systems energy storage is nearly zero, so at any instant, the power into the system (produced by a generator) must equal the power out of the system (demand from consumers). Since production must so closely match demand, careful scheduling and dispatch are necessary.

Usually performed by the independent system operator or transmission system operator, both are services dedicated to the commitment and coordination of the generation and transmission units in order to maintain the reliability of the power grid.

Scheduling refers to before-the-fact actions (like scheduling a generator to produce a certain amount of power the next week), while dispatch refers to the real-time control of the available resources.

### Operating reserves

Since production and demand must match so perfectly (see Scheduling and dispatch), operating reserves help make up the difference when production is too low.

An operating reserve is a generator that can quickly be dispatched to ensure that there is sufficient energy generation to meet load. Spinning reserves are generators that are already online and can rapidly increase their power output to meet fast changes in demand. Spinning reserves are required because demand can vary on short timescales and rapid response is needed. Other operating reserves are generators that can be dispatched by the operator to meet demand, but that cannot respond as quickly as spinning reserves, and grid battery storage that can respond within tens of milliseconds, generally faster than even spinning reserve.

## Renewable generation

The grid integration of renewable generation simultaneously requires additional ancillary services and has the potential to provide ancillary services to the grid. The inverters that are installed with distributed generation systems and roof top solar systems have the potential to provide many of the ancillary services that are traditionally provided by spinning generators and voltage regulators. These services include reactive power compensation, voltage regulation, flicker control, active power filtering and harmonic cancellation. Wind turbines with variable-speed generators have the potential to add synthetic inertia to the grid and assist in frequency control. CAISO tested the 131 MW Tule wind farm's synchronverter in 2018, and found it could perform some of the grid services similar or better than traditional generators. Hydro-Québec began requiring synthetic inertia in 2005 as the first grid operator, demanding a temporary 6% power boost when countering frequency drop by combining the power electronics with the rotational inertia of a wind turbine rotor. Similar requirements came into effect in Europe in 2016.

## Electric vehicles

Plug-in electric vehicles have the potential to be utilized to provide ancillary services to the grid, specifically load regulation and spinning reserves. Plug-in electric vehicles can behave like distributed energy storage and have the potential to discharge power back to the grid through bidirectional flow, referred to as vehicle-to-grid (V2G). Plug-in electric vehicles have the ability to supply power at a fast rate which enables them to be used like spinning reserves and provide grid stability with the increased use of intermittent generation such as wind and solar. According to the study cited in the reference, which compared the profitability of offering operating reserve ancillary service with the sales of V2G energy from a fleet of vehicles, providing operating reserve regulation service is more profitable than selling V2G energy alone. However, the technologies to utilize electric vehicles to provide ancillary services are not yet widely implemented, but there is much anticipation of their potential.
