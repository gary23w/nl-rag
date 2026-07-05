---
title: "Computer cooling (part 2/2)"
source: https://en.wikipedia.org/wiki/Computer_cooling
domain: operating-temperature
license: CC-BY-SA-4.0
tags: operating temperature
fetched: 2026-07-05
part: 2/2
---

## Optimization

Cooling can be improved by several techniques, which may involve additional expense or effort. These techniques are often used, in particular, by those who run parts of their computer (such as the CPU and GPU) at higher voltages and frequencies than specified by the manufacturer (overclocking), which increases heat generation.

The installation of higher-performance, non-stock cooling may also be considered modding. Many overclockers simply buy more efficient, and often, more expensive fan and heatsink combinations, while others resort to more exotic ways of computer cooling, such as liquid cooling, Peltier effect heatpumps, heat pipe or phase change cooling.

There are also some related practices that have a positive impact in reducing system temperatures:

### Thermally conductive compounds

Often called Thermal Interface Material (TIM).

Perfectly flat surfaces in contact give optimal cooling, but perfect flatness and absence of microscopic air gaps is not practically possible, particularly in mass-produced equipment. A very thin skim of thermal compound, which is much more thermally conductive than air, though much less so than metal, can improve thermal contact and cooling by filling in the air gaps. If only a small amount of compound just sufficient to fill the gaps is used, the best temperature reduction will be obtained.

There is much debate about the merits of compounds, and overclockers often consider some compounds to be superior to others. The main consideration is to use the minimal amount of thermal compound required to even out surfaces, as the thermal conductivity of compound is typically 1/3 to 1/400 that of metal, though much better than air. The conductivity of the heatsink compound ranges from about 0.5 to 80W/mK (see articles); that of aluminium is about 200, that of air about 0.02. Heat-conductive pads are also used, often fitted by manufacturers to heatsinks. They are less effective than properly applied thermal compound, but simpler to apply and, if fixed to the heatsink, cannot be omitted by users unaware of the importance of good thermal contact, or replaced by a thick and ineffective layer of compound.

Unlike some techniques discussed here, the use of thermal compound or padding is almost universal when dissipating significant amounts of heat.

### Heat sink lapping

Mass-produced CPU heat spreaders and heatsink bases are never perfectly flat or smooth; if these surfaces are placed in the best contact possible, there will be air gaps that reduce heat conduction. This can easily be mitigated by the use of thermal compound, but for the best possible results surfaces must be as flat as possible. This can be achieved by a laborious process known as lapping, which can reduce CPU temperature by typically 2 °C (4 °F).

### Rounded cables

Most older PCs use flat ribbon cables to connect storage drives (IDE or SCSI). These large flat cables greatly impede airflow by causing drag and turbulence. Overclockers and modders often replace these with rounded cables, with the conductive wires bunched together tightly to reduce surface area. Theoretically, the parallel strands of conductors in a ribbon cable serve to reduce crosstalk (signal-carrying conductors inducing signals in nearby conductors), but there is no empirical evidence of rounding cables reducing performance. This may be because the length of the cable is short enough so that the effect of crosstalk is negligible. Problems usually arise when the cable is not electromagnetically protected and the length is considerable, a more frequent occurrence with older network cables.

These computer cables can then be cable tied to the chassis or other cables to further increase airflow.

This is less of a problem with computers that use serial ATA, which has a much narrower cable. Newer computers improve this further by the common use of modular power supplies with removable cables, and cases with cable management areas behind the motherboard, leaving the front of the case free flowing.

### Airflow

The colder the cooling medium (the air), the more effective the cooling. Cooling air temperature can be improved with these guidelines:

- Supply cool air to the hot components as directly as possible. Examples are air snorkels and tunnels that feed outside air directly and exclusively to the CPU or GPU cooler. For example, the BTX case design prescribes a CPU air tunnel.
- Expel warm air as directly as possible. Examples are: Conventional PC (ATX) power supplies blow the warm air out the back of the case. Many dual-slot graphics card designs blow the warm air through the cover of the adjacent slot. There are also some aftermarket coolers that do this. Some CPU cooling designs blow the warm air directly towards the back of the case, where it can be ejected by a case fan.
- Air that has already been used to spot-cool a component should not be reused to spot-cool a different component (this follows from the previous items). The BTX case design violates this rule, since it uses the CPU cooler's exhaust to cool the chipset and often the graphics card. One may come across old or ultra-low-budget ATX cases that feature a PSU mount in the top. Most modern ATX cases do, however, have a PSU mount in the bottom of the case with a filtered air vent directly beneath the PSU.
- Prefer cool intake air, avoid inhaling exhaust air (outside air above or near the exhausts). For example, a CPU cooling air duct at the back of a tower case would inhale warm air from a graphics card exhaust. Moving all exhausts to one side of the case, conventionally the back/top, helps to keep the intake air cool.
- Hiding cables behind the motherboard tray, or simply applying cable ties and tucking cables away, helps to provide unhindered airflow.

Fewer fans strategically placed will improve the airflow internally within the PC and thus lower the overall internal case temperature in relation to ambient conditions. The use of larger fans also improves efficiency and lowers the amount of waste heat along with the amount of noise generated by the fans while in operation.

There is little agreement on the effectiveness of different fan placement configurations, and little in the way of systematic testing has been done. For a rectangular PC (ATX) case, a fan in the front with a fan in the rear and one in the top has been found to be a suitable configuration. However, AMD's (somewhat outdated) system cooling guidelines notes that "A front cooling fan does not seem to be essential. In fact, in some extreme situations, testing showed these fans to be recirculating hot air rather than introducing cool air." It may be that fans in the side panels could have a similar detrimental effect – possibly through disrupting the normal air flow through the case. However, this is unconfirmed and probably varies with the configuration.

#### Air pressure

Loosely speaking, positive pressure means intake into the case is stronger than exhaust from the case. This configuration results in pressure inside of the case being higher than in its environment. Negative pressure means exhaust is stronger than intake. This results in internal air pressure being lower than in the environment. Both configurations have benefits and drawbacks, with positive pressure being the more popular of the two configurations. Negative pressure results in the case pulling air through holes and vents separate from the fans, as the internal gases will attempt to reach an equilibrium pressure with the environment. Consequently, this results in dust entering the computer in all locations. Positive pressure in combination with filtered intake solves this issue, as air will only incline to be exhausted through these holes and vents in order to reach an equilibrium with its environment. Dust is then unable to enter the case except through the intake fans, which need to possess dust filters.


## Computer types

### Desktops

Desktop computers typically use one or more fans for cooling. While almost all desktop power supplies have at least one built-in fan, power supplies should never draw heated air from within the case, as this results in higher PSU operating temperatures which decrease the PSU's energy efficiency, reliability and overall ability to provide a steady supply of power to the computer's internal components. For this reason, all modern ATX cases (with some exceptions found in ultra-low-budget cases) feature a power supply mount in the bottom, with a dedicated PSU air intake (often with its own filter) beneath the mounting location, allowing the PSU to draw cool air from beneath the case.

Most manufacturers recommend bringing cool, fresh air in at the bottom front of the case, and exhausting warm air from the top rear. If fans are fitted to force air into the case more effectively than it is removed, the pressure inside becomes higher than outside, referred to as a "positive" airflow (the opposite case is called "negative" airflow). Worth noting is that positive internal pressure only prevents dust accumulating in the case if the air intakes are equipped with dust filters. A case with negative internal pressure will suffer a higher rate of dust accumulation even if the intakes are filtered, as the negative pressure will draw dust in through any available opening in the case

The air flow inside the typical desktop case is usually not strong enough for a passive CPU heatsink. Most desktop heatsinks are active, including one or even multiple directly attached fans or blowers.

### Servers

A server with seven fans in the middle of the chassis, between drives on the right and main motherboard on the left

Close view of server fans. In this server they are hot swappable.

#### Server coolers

Each server can have an independent internal cooler system; Server cooling fans in (1 U) enclosures are usually located in the middle of the enclosure, between the hard drives at the front and passive CPU heatsinks at the rear. Larger (higher) enclosures also have exhaust fans, and from approximately 4U they may have active heatsinks. Power supplies generally have their own rear-facing exhaust fans.

#### Rack-mounted coolers

Rack cabinet is a typical enclosure for horizontally mounted servers. Air typically drawn in at the front of the rack and exhausted at the rear. Each cabinet can have additional cooling options; for example, they can have a Close Coupled Cooling attachable module or integrated with cabinet elements (like cooling doors in iDataPlex server rack).

Another way of accommodating large numbers of systems in a small space is to use blade chassis, oriented vertically rather than horizontally, to facilitate convection. Air heated by the hot components tends to rise, creating a natural air flow along the boards (stack effect), cooling them. Some manufacturers take advantage of this effect.

#### Data center cooling

Because data centers typically contain large numbers of computers and other power-dissipating devices, they risk equipment overheating; extensive HVAC systems are used to prevent this. Often a raised floor is used so the area under the floor may be used as a large plenum for cooled air from a CRAC (Computer Room Air Conditioner) or a CRAH (Computer Room Air Handler) and power cabling. A plenum made with a false ceiling can also be present. Hot Aisle containment or cold aisle containment are also used in datacenters to improve cooling efficiency. Alternatively slab floors can be used which are similar to conventional floors, and overhead ducts can be used for cooling.

Direct Contact Liquid Cooling has emerged more efficient than air cooling options, resulting in smaller footprint, lower capital requirements and lower operational costs than air cooling. It uses warm liquid instead of air to move heat away from the hottest components. Energy efficiency gains from liquid cooling is also driving its adoption. Single and dual/two phase immersion/open tub cooling and single and dual phase direct-to-chip cooling as well as immersion cooling confined to individual server blades have also been proposed for use in data centers. In-row cooling, rack cooling, rear door heat exchangers, racktop cooling which places heat exchangers above the rack, overhead cooling above aisles or fan walls/thermal walls in a data center can also be used. Direct Liquid Cooling (DLC) with cold plates for cooling chips in servers can be used due to the higher heat removal capacities of these systems. These systems can either cool some or all components on a server, using rubber or copper tubing respectively. Rear door heat exchangers were traditionally used for cooling high heat densities in data centers, but these did not see widespread adoption. They can be cooled with refrigerant or chilled water. Those cooled with chilled water can either be active, which have fans, or passive, which have no fans. Liquid-to-air heat exchangers (radiators) can be used to cool servers cooled with direct-to-chip liquid cooling, in order to avoid installation of facility water piping. These heat exchangers can be installed separately from racks, or as a rear door on a rack.

### Laptops

Laptops present a difficult mechanical airflow design, power dissipation, and cooling challenge. Constraints specific to laptops include: the device as a whole has to be as light as possible; the form factor has to be built around the standard keyboard layout; users are very close, so noise must be kept to a minimum, and the case exterior temperature must be kept low enough to be used on a lap. Cooling generally uses forced air cooling but heat pipes and the use of the metal chassis or case as a passive heatsink are also common. Solutions to reduce heat include using lower power consumption ARM or Intel Atom processors.

- (A laptop computer's CPU and GPU heatsinks, and copper heat pipes transferring heat to an exhaust fan expelling hot air)A laptop computer's CPU and GPU heatsinks, and copper heat pipes transferring heat to an exhaust fan expelling hot air
- (The working fluid in the heatpipes transfers heat away from the laptop's CPU and video processor over to the fin stack. Heat is dissipated from the fin stack by method of convective heat transfer from a fan. This fin stack is from an HP ZBook mobile workstation laptop.)The working fluid in the heatpipes transfers heat away from the laptop's CPU and video processor over to the fin stack. Heat is dissipated from the fin stack by method of convective heat transfer from a fan. This fin stack is from an HP ZBook mobile workstation laptop.
- (The heat is expelled from a laptop by an exhaust centrifugal fan.)The heat is expelled from a laptop by an exhaust centrifugal fan.

### Mobile devices

Mobile devices such as phones and tablets usually use passive cooling as mobile CPU and GPU chips are designed for maximum power efficiency due to the constraints of the device's battery. Some higher-performance devices may include a heat spreader that aids in transferring heat to the external case of a phone or tablet.
