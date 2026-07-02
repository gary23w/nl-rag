---
title: "Wind turbine design (part 2/2)"
source: https://en.wikipedia.org/wiki/Wind_turbine_design
domain: wind-turbine-control
license: CC-BY-SA-4.0
tags: wind turbine control, blade pitch, yaw system, wind farm
fetched: 2026-07-02
part: 2/2
---

## Tower

### Height

Wind velocities increase at higher altitudes due to surface aerodynamic drag (by land or water surfaces) and air viscosity. The variation in velocity with altitude, called wind shear, is most dramatic near the surface. Typically, the variation follows the wind profile power law, which predicts that wind speed rises proportionally to the seventh root of altitude. Doubling the altitude of a turbine, then, increases the expected wind speeds by 10% and the expected power by 34%. To avoid buckling, doubling the tower height generally requires doubling the tower diameter, increasing the amount of material by a factor of at least four. As of July 2025, the world's tallest wind turbine, at 300 metres (980 ft) hub height with 3.8 MW capacity, was under construction in Germany.

During the night, or when the atmosphere becomes stable, wind speed close to the ground usually subsides whereas at turbine hub altitude it does not decrease that much or may even increase. As a result, the wind speed is higher and a turbine will produce more power than expected from the 1/7 power law: doubling the altitude may increase wind speed by 20% to 60%. A stable atmosphere is caused by radiative cooling of the surface and is common in a temperate climate: it usually occurs when there is a (partly) clear sky at night. When the (high altitude) wind is strong (a 10-meter wind speed higher than approximately 6 to 7 m/s) the stable atmosphere is disrupted because of friction turbulence and the atmosphere turns neutral. A daytime atmosphere is either neutral (no net radiation; usually with strong winds and heavy clouding) or unstable (rising air because of ground heating—by the sun). The 1/7 power law is a good approximation of the wind profile. Indiana was rated as having a wind capacity of 30,000 MW, but by raising the expected turbine height from 50 m to 70 m raised the wind capacity to 40,000 MW, and could be double that at 100 m.

For HAWTs, tower heights approximately two to three times the blade length balance material costs of the tower against better utilisation of the more expensive active components.

Road restrictions make tower transport with a diameter of more than 4.3 m difficult. Swedish analyses showed that the bottom wing tip must be at least 30 m above the tree tops. A 3 MW turbine may increase output from 5,000 MWh to 7,700 MWh per year by rising from 80 to 125 meters. A tower profile made of connected shells rather than cylinders can have a larger diameter and still be transportable. A 100 m prototype tower with TC bolted 18 mm 'plank' shells at the wind turbine test center Høvsøre in Denmark was certified by Det Norske Veritas, with a Siemens nacelle. Shell elements can be shipped in standard 12 m shipping containers.

As of 2003, typical modern wind turbine installations used 65 metres (213 ft) towers. Height is typically limited by the availability of cranes. This led to proposals for "partially self-erecting wind turbines" that, for a given available crane, allow taller towers that locate a turbine in stronger and steadier winds, and "self-erecting wind turbines" that could be installed without cranes.

### Materials

Currently, the majority of wind turbines are supported by conical tubular steel towers. These towers represent 30% – 65% of the turbine weight and therefore account for a large percentage of transport costs. The use of lighter tower materials could reduce the overall transport and construction cost, as long as stability is maintained. Higher grade S500 steel costs 20%-25% more than S355 steel (standard structural steel), but it requires 30% less material because of its improved strength. Therefore, replacing wind turbine towers with S500 steel offer savings in weight and cost.

Another disadvantage of conical steel towers is meeting the requirements of wind turbines taller than 90 meters. High performance concrete may increase tower height and increase lifetime. A hybrid of prestressed concrete and steel improves performance over standard tubular steel at tower heights of 120 meters. Concrete also allows small precast sections to be assembled on site. One downside of concrete towers is the higher CO 2 emissions during concrete production. However, the overall environmental impact should be positive if concrete towers can double the wind turbine lifetime.

Wood is another alternative: a 100-metre tower supporting a 1.5 MW turbine operates in Germany. The wood tower shares the same transportation benefits of the segmented steel shell tower, but without the steel. A 2 MW turbine on a wooden tower started operating in Sweden in 2023.

Another approach is to form the tower on site via spiral welding rolled sheet steel. Towers of any height and diameter can be formed this way, eliminating restrictions driven by transport requirements. A factory can be built in one month. The developer claims 80% labor savings over conventional approaches.


## Grid connection

Grid-connected wind turbines, until the 1970s, were fixed-speed. As recently as 2003, nearly all grid-connected wind turbines operated at constant speed (synchronous generators) or within a few percent of constant speed (induction generators). As of 2011, many turbines used fixed-speed induction generators (FSIG). By then, most newly connected turbines were variable speed.

Early control systems were designed for peak power extraction, also called maximum power point tracking—they attempted to pull the maximum power from a given wind turbine under the current wind conditions. More recent systems deliberately pull less than maximum power in most circumstances, in order to provide other benefits, which include:

- Spinning reserves to produce more power when needed—such as when some other generator drops from the grid
- Variable-speed turbines can transiently produce slightly more power than wind conditions support, by storing some energy as kinetic energy (accelerating during brief gusts of faster wind) and later converting that kinetic energy to electric energy (decelerating). either when more power is needed, or to compensate for variable windspeeds.
- damping (electrical) subsynchronous resonances in the grid
- damping (mechanical) tower resonances

The generator produces alternating current (AC). The most common method in large modern turbines is to use a doubly fed induction generator directly connected to the grid. Some turbines drive an AC/AC converter—which converts the AC to direct current (DC) with a rectifier and then back to AC with an inverter—in order to match grid frequency and phase.

A useful technique to connect a PMSG (Permanent Magnet Synchronous Generator) to the grid is via a back-to-back converter. Control schemes can achieve unity power factor in the connection to the grid. In that way the wind turbine does not consume reactive power, which is the most common problem with turbines that use induction machines. This leads to a more stable power system. Moreover, with different control schemes a PMSG turbine can provide or consume reactive power. So, it can work as a dynamic capacitor/inductor bank to help with grid stability.

The diagram shows the control scheme for a unity power factor :

Reactive power regulation consists of one PI controller in order to achieve operation with unity power factor (i.e. Qgrid = 0 ). IdN has to be regulated to reach zero at steady-state (IdNref = 0).

The complete system of the grid side converter and the cascaded PI controller loops is displayed in the figure.


## Construction

As wind turbine usage has increased, so have companies that assist in the planning and construction of wind turbines. Most often, turbine parts are shipped via sea or rail, and then via truck to the installation site. Due to the massive size of the components involved, companies usually need to obtain transportation permits and ensure that the chosen trucking route is free of potential obstacles such as overpasses, bridges, and narrow roads. Groups known as "reconnaissance teams" will scout the way up to a year in advance as they identify problematic roads, cut down trees, and relocate utility poles. Turbine blades continue to increase in size, sometimes necessitating brand new logistical plans, as previously used routes may not allow a larger blade. Specialized vehicles known as Schnabel trailers are custom-designed to load and transport turbine sections: tower sections can be loaded without a crane and the rear end of the trailer is steerable, allowing for easier maneuvering. Drivers must be specially trained.

### Foundations

Wind turbines, by their nature, are very tall, slender structures, and this can cause a number of issues when the structural design of the foundations are considered. The foundations for a conventional engineering structure are designed mainly to transfer the vertical load (dead weight) to the ground, generally allowing comparatively unsophisticated arrangement to be used. However, in the case of wind turbines, the force of the wind's interaction with the rotor at the top of the tower creates a strong tendency to tip the wind turbine over. This loading regime causes large moment loads to be applied to the foundations of a wind turbine. As a result, considerable attention needs to be given when designing the footings to ensure that the foundation will resist this tipping tendency.

One of the most common foundations for offshore wind turbines is the monopile, a single large-diameter (4 to 6 metres) tubular steel pile driven to a depth of 5-6 times the diameter of the pile into the seabed. The cohesion of the soil, and friction between the pile and the soil provide the necessary structural support for the wind turbine.

In onshore turbines the most common type of foundation is a gravity foundation, where a large mass of concrete spread out over a large area is used to resist the turbine loads. Wind turbine size & type, wind conditions and soil conditions at the site are all determining factors in the design of the foundation. Prestressed piles or rock anchors are alternative foundation designs that use much less concrete and steel.


## Costs

A wind turbine is a complex and integrated system. Structural elements comprise the majority of the weight and cost. All parts of the structure must be inexpensive, lightweight, durable, and manufacturable, surviving variable loading and environmental conditions. Turbine systems with fewer failures require less maintenance, are lighter and last longer, reducing costs.

The major parts of a turbine divide as: tower 22%, blades 18%, gearbox 14%, generator 8%.


## Specification

Turbine design specifications contain a power curve and availability guarantee. The wind resource assessment makes it possible to calculate commercial viability. Typical operating temperature range is −20 to 40 °C (−4 to 104 °F). In areas with extreme climate (like Inner Mongolia or Rajasthan) climate-specific versions are required.

Wind turbines can be designed and validated according to IEC 61400 standards.

RDS-PP (Reference Designation System for Power Plants) is a standardized system used worldwide to create structured hierarchy of wind turbine components. This facilitates turbine maintenance and operation cost, and is used during all stages of a turbine creation.
