---
title: "Virtual power plant"
source: https://en.wikipedia.org/wiki/Virtual_power_plant
domain: microgrid-control
license: CC-BY-SA-4.0
tags: microgrid, distributed generation, islanding, virtual power plant
fetched: 2026-07-02
---

# Virtual power plant

A **virtual power plant** (**VPP**) is a system for aggregating distributed energy resources (DERs) to function as a single power plant. Operators coordinate these resources to balance supply and demand, provide grid services, and participate in energy markets. A VPP typically sells its output to an electric utility. VPPs allow energy resources that are individually too small to be of interest to a utility to aggregate and market their power.

VPPs typically access dispatchable and non-dispatchable resources, including microCHPs, natural gas-fired reciprocating engines, wind power plants, photovoltaics (PV), run-of-river hydroelectricity, biomass, backup generators, battery energy storage systems (BESS) such as home or vehicle batteries. VPPs can manage demand as well as supply; e.g., heat pumps and other devices can be turned on or off based on available energy supply.

Heterogeneity and numbers reduce dependence on any single resource, improving system stability.

Vehicle-to-grid allows grid-connected electric vehicles to participate.

Storage-based VPPs ramp faster than thermal generators, e.g., helping grids with high ramp needs avoid the duck curve.

A management system securely controls operations, billing, and payments to power suppliers and consumers.

VPPs provide peak shaving by delivering power during high demand, avoiding expensive peaker plants (saving 40–60%). They offer load following and ancillary services such as frequency regulation and operating reserves, responding in seconds to minutes.

VPPs can trade energy in wholesale markets, acting as dispatchable plants. Strategies hedge risks in markets:

- Info-gap decision theory (IGDT)
- Robust optimization (RO)
- Conditional value at risk (CVaR)
- First-order Stochastic Dominance (FSD)
- Second-order Stochastic Dominance (SSD)

## History

Shimon Awerbuch proposed the VPP concept in 1997. Early work remained theoretical due to technology and regulatory limits. Papers in the early 2000s examined renewable aggregation. Challenges included communication costs and risks.

RWE launched the first VPP in 2008, aggregating nine hydroelectric plants for 8.6 MW. The University of Kassel piloted one linking solar, wind, biogas, and hydroelectricity for load following. Kraftwerke started in 2011, expanding across seven countries, aggregating biogas, solar, and wind.

In the United States, VPPs built on demand response programs. The 2009 American Recovery and Reinvestment Act supported smart grids. Federal Energy Regulatory Commission Order 745 (2011) treated demand reductions as generation in wholesale markets. Order 2222 (2020) enabled direct DER bidding.

AGL Energy started a 5 MW VPP in Adelaide in 2016 with batteries and PV for 1,000 homes. Tesla opened a VPP in South Australia in 2018, reaching 50,000 homes by 2022; AGL acquired the program in 2025, reaching 25 MW solar and 37 MW storage.

UK Power Networks and Powervault launched London's first VPP in 2018 (0.32 MWh); Tesla partnered with Octopus Energy there in 2020.created London's first VPP in 2018, installing BESS at 40+ homes across Barnet, with capacity of 0.32 MWh, expanding it in 2020. In 2019, SMS plc launched a VPP following the acquisition of Irish firm, Solo Energy. In 2020, Tesla launched its Tesla Energy Plan in the UK in partnership with Octopus Energy. Participant homes are powered with renewable energy either from solar panels or from Octopus Energy.

By 2023, U.S. capacity reached 30–60 GW (4–8% of peak demand). Tesla operated VPPs in Texas and California.

In 2024, Enpal and Entrix (via Flexa) planned Europe's largest VPP, targeting 1 GW by 2026 with solar, batteries, and EVs; launch occurred later that year.

Virginia mandated a Dominion Energy VPP pilot (up to 450 MW) in 2025; the utility proposed it by December. Vermont VPPs saved $3 million during 2025 heat waves. North American capacity reached 37.5 GW in 2025.

## Distributed energy resources

VPPs typically aggregate large numbers of distributed energy resources (DER). Resources can be dispatchable or non-dispatchable, controllable or flexible load (CL or FL). Resources can include micro-CHPs, natural gas-fired reciprocating engines, wind power (WPP), photovoltaics (PV), run-of-river hydroelectricity, small hydro, biomass, backup generators, and BESS, as well as devices whose consumption is adjustable (such as water heaters and appliances). The numbers and heterogeneity mean that system output is not dependent on any single resource, offering the potential for stable output even if the output of any single resource is not.

Vehicle-to-grid (V2G) technology allows grid-connected EVs to participate in VPPs. The VPP controls the rate at which each vehicle charges/discharges (accepts/delivers power).

The same principle applies to consuming systems, such as heat pumps or air conditioners that can lower their power demands to reduce demand.

VPPs based on storage can ramp at higher rates than thermal generators (such as fossil fuel plants), which is especially valuable in grids that experience a duck curve and must satisfy high ramping requirements in the morning and evening.

VPPs can be as dependable as conventional plants, while costing 40–60 percent less. One study forecasted that decentralized generation would comprise 500,000 megawatts of capacity compared to centralized generation of 280,000 megawatts.

## Operation

Power delivery is controlled by a management system. The distributed nature of VPPs requires software to respond appropriately and securely to power requests, utility billing, payments to resource owners, etc.

## Services

Typically, the VPP provides power (only) when requested by the utility.

### Peak shaving

With the appropriate resources, a VPP can deliver incremental power on short notice, helping utilities to manage peak loads that would otherwise require purchasing expensive power from a peaker plant (typically powered by natural gas).

### Load following

Given sufficient scale, a VPP can operate as a load-following generator, supplying output dynamically as demand changes throughout the day/night cycle.

### Ancillary services

Virtual power plants can provide ancillary services that help maintain grid stability such as frequency regulation and providing operating reserve. These services are primarily used to maintain the instantaneous balance of electrical supply and demand. These services must respond to signals to increase or decrease load on the order of seconds to minutes.

## Energy trading

Electrical energy markets are wholesale, international markets that trade electrical energy. Market prices fluctuate with demand and supply (e.g., when the wind subsides). The VPP behaves as a conventional dispatchable power plant from the point of view of other market participants. A VPP arbitrages between diverse energy markets (e.g., bilateral and purchase power agreements (PPA), forward and futures markets, and the pool).

Five risk-hedging strategies have been applied to VPP decision-making to measure the degree of conservatism of VPPs' decisions in energy trading (e.g., day-ahead electricity market, derivatives exchange market, and bilateral contracts):

- IGDT: Information Gap Decision Theory
- RO: Robust optimization
- CVaR: Conditional value at risk
- FSD: First-order Stochastic Dominance
- SSD: Second-order Stochastic Dominance

## Markets

### United States

In 2023 the Department of Energy estimated VPP capacity at around 30 to 60 GW, some 4–8% of peak electricity demand.

Texas has two Tesla-operated VPPs. Eligible Tesla Electric members automatically join the Virtual Power Plant, consisting of Tesla Powerwall batteries. Tesla pays the owner a monthly fee in addition to payment per unit of energy delivered.

California has two electric markets: retail and wholesale. As of 2022 PG&E paid VPP providers $2/kWh during peak demand. As of August/September 2022, SunRun VPP often delivered 80 MW at peak times, while Tesla VPP supplied 68 MW. By 2025, California was testing 100,000 residential batteries at a combined 535 MW. That amount of electricity can power a mid-sized city. It is part of the process to advance the smart grid, where utilities don't just send power to customers but the process is interactive.

Virginia's Virtual Power Plant (VPP) pilot program is a state-mandated initiative requiring Dominion Energy Virginia (a Phase II Utility) to implement a pilot VPP. The pilot is capped at 450 MW. It is to include incentives for 15 MW+ of distributed BESS, including residential, commercial, and industrial customers. As of early 2026, the program represented one of the US' largest VPP pilots. A program for electrification of school buses must be filed by December 31, 2027.

Vermont's Green Mountain Power works with Tesla to offer a Powerwall to participating customers at a discounted rate.

Three Massachusetts utilities, National Grid, Eversource, and Cape Light Compact, operate a VPP. The Massachusetts Clean Energy Center (MassCEC) is implementing a vehicle‑to‑everything (V2X) demonstration program as part of its VPP that installs free, bi‑directional EV chargers at school districts, municipalities, and residents.

### Europe

The Institute for Solar Energy Supply Technology of Germany's University of Kassel pilot-tested a VPP that linked solar, wind, biogas, and pumped-storage hydroelectricity to provide load-following power from renewable sources.

A VPP operated on the Scottish Inner Hebrides island of Eigg.

Kraftwerke operates a VPP in seven European countries that provides peak-load resources, power trading and grid balancing. The company aggregates energy from biogas, solar and wind as well as large-scale power consumers.

A London VPP is supported by UK Power Networks, and Powervault. SMS plc operates a UK VPP.

Tesla operates in the UK in partnership with Octopus Energy. Participant homes are powered with renewable energy from solar panels or from Octopus Energy.

German companies Enpal and Entrix operate Europe's largest VPP that integrates PV, BESS, and electric vehicles. Enpal is a solar installer with more than 70,000 installed systems, connects thousands of solar/BESS households to the VPP.

### Australia

AGL Energy operates a 25 MW virtual-power-plant scheme in Adelaide. The company supplies BESS and photovoltaic systems, to >8,000 customers. The systems cost consumers A$3500 with a 7 year payout. As of 2025, the program provided 25 MW solar and 37 MW storage.
