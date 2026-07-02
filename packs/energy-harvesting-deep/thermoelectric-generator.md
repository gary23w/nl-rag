---
title: "Thermoelectric generator"
source: https://en.wikipedia.org/wiki/Thermoelectric_generator
domain: energy-harvesting-deep
license: CC-BY-SA-4.0
tags: energy harvesting, rectenna device, thermoelectric generator, vibration powered generator
fetched: 2026-07-02
---

# Thermoelectric generator

A **thermoelectric generator** (**TEG**), also called a **Seebeck generator**, is a solid state device that converts heat (driven by temperature differences) directly into electrical energy through a phenomenon called the *Seebeck effect* (a form of thermoelectric effect). Thermoelectric generators function like heat engines, but are less bulky and have no moving parts. However, TEGs are typically more expensive and less efficient. When the same principle is used in reverse to create a heat gradient from an electric current, it is called a thermoelectric (or Peltier) cooler.

Thermoelectric generators could be used in power plants and factories to convert waste heat into additional electrical power and in automobiles as automotive thermoelectric generators (ATGs) to increase fuel efficiency. Radioisotope thermoelectric generators use radioisotopes to generate the required temperature difference to power space probes. Thermoelectric generators can also be used alongside solar panels.

## History

In 1821, Thomas Johann Seebeck discovered that a thermal gradient formed between two different conductors can produce electricity. At the heart of the thermoelectric effect is that a temperature gradient in a conducting material results in heat flow; this results in the diffusion of charge carriers. The flow of charge carriers between the hot and cold regions in turn creates a voltage difference. In 1834, Jean Charles Athanase Peltier discovered the reverse effect, that running an electric current through the junction of two dissimilar conductors could, depending on the direction of the current, cause it to act as a heater or cooler.

George Cove had accidentally invented a photovoltaic panel, despite intending to invent a thermoelectric generator with thermocouples, in 1909. He notes that heat alone didn't produce any power, only incident light, but he had no explanation for how it could be working. The operational principle is now understood to have been a very simple form of Schottky junction.

## Efficiency

The typical efficiency of TEGs is around 5–8%, although it can be higher. Older devices used bimetallic junctions and were bulky. More recent devices use highly doped semiconductors made from bismuth telluride (Bi2Te3), lead telluride (PbTe), calcium manganese oxide (Ca2Mn3O8), or combinations thereof, depending on application temperature. These are solid-state devices and unlike dynamos have no moving parts, with the occasional exception of a fan or pump to improve heat transfer. If the hot region is around 1273K and the ZT values of 3 - 4 are implemented, the efficiency is approximately 33-37%; allowing TEG's to compete with certain heat engine efficiencies.

As of 2021, there are materials (some containing widely available and inexpensive arsenic and tin) reaching a ZT value > 3; monolayer ${\ce {AsP3}}$ (ZT = 3.36 on the armchair axis); n-type doped ${\ce {InP3}}$ (ZT = 3.23); p-type doped ${\ce {SnP3}}$ (ZT = 3.46); p-type doped ${\ce {SbP3}}$ (ZT = 3.5).

## Construction

Thermoelectric power generators consist of three major components: thermoelectric materials, thermoelectric modules and thermoelectric systems that interface with the heat source.

### Thermoelectric materials

Thermoelectric materials generate power directly from the heat by converting temperature differences into electric voltage. These materials must have both high electrical conductivity (σ) and low thermal conductivity (κ) to be good thermoelectric materials. Having low thermal conductivity ensures that when one side is made hot, the other side stays cold, which helps to generate a large voltage while in a temperature gradient. The measure of the magnitude of electrons flow in response to a temperature difference across that material is given by the Seebeck coefficient (S). The efficiency of a given material to produce a thermoelectric power is simply estimated by its "figure of merit" zT = S2σT/κ.

For many years, the main three semiconductors known to have both low thermal conductivity and high power factor were bismuth telluride (Bi2Te3), lead telluride (PbTe), and silicon germanium (SiGe). Some of these materials have somewhat rare elements which make them expensive.

Today, the thermal conductivity of semiconductors can be lowered without affecting their high electrical properties using nanotechnology. This can be achieved by creating nanoscale features such as particles, wires or interfaces in bulk semiconductor materials. However, the manufacturing processes of nano-materials are still challenging.

### Thermoelectric advantages

Thermoelectric generators are all-solid-state devices that do not require any fluids for fuel or cooling, making them non-orientation dependent allowing for use in zero-gravity or deep-sea applications. The solid-state design allows for operation in severe environments. Thermoelectric generators have no moving parts which produce a more reliable device that does not require maintenance for long periods. The durability and environmental stability have made thermoelectrics a favorite for NASA's deep space explorers among other applications. One of the key advantages of thermoelectric generators outside of such specialized applications is that they can potentially be integrated into existing technologies to boost efficiency and reduce environmental impact by producing usable power from waste heat.

### Thermoelectric module

A thermoelectric module is a circuit containing thermoelectric materials which generate electricity from heat directly. A thermoelectric module consists of two dissimilar thermoelectric materials joined at their ends: an n-type (with negative charge carriers), and a p-type (with positive charge carriers) semiconductor. Direct electric current will flow in the circuit when there is a temperature difference between the ends of the materials. Generally, the current magnitude is directly proportional to the temperature difference:

$\mathbf {J} =-\sigma S\nabla T$

where $\sigma$ is the local conductivity, S is the Seebeck coefficient (also known as thermopower), a property of the local material, and $\nabla T$ is the temperature gradient.

In application, thermoelectric modules in power generation work in very tough mechanical and thermal conditions. Because they operate in a very high-temperature gradient, the modules are subject to large thermally induced stresses and strains for long periods. They also are subject to mechanical fatigue caused by a large number of thermal cycles.

Thus, the junctions and materials must be selected so that they survive these tough mechanical and thermal conditions. Also, the module must be designed such that the two thermoelectric materials are thermally in parallel, but electrically in series. The efficiency of a thermoelectric module is greatly affected by the geometry of its design.

### Thermoelectric design

Thermoelectric generators are made of several thermopiles, each consisting of many thermocouples made of a connected n-type and p-type material. The arrangement of the thermocouples is typically in three main designs: planar, vertical, and mixed. Planar design involves thermocouples put onto a substrate horizontally between the heat source and cool side, resulting in the ability to create longer and thinner thermocouples, thereby increasing the thermal resistance and temperature gradient and eventually increasing voltage output. Vertical design has thermocouples arranged vertically between the hot and cool plates, leading to high integration of thermocouples as well as a high output voltage, making this design the most widely used design commercially. The mixed design has the thermocouples arranged laterally on the substrate while the heat flow is vertical between plates. Microcavities under the hot contacts of the device allow for a temperature gradient, which allows for the substrate's thermal conductivity to affect the gradient and efficiency of the device.

For microelectromechanical systems, TEGs can be designed on the scale of handheld devices to use body heat in the form of thin films. Flexible TEGs for wearable electronics are able to be made with novel polymers through additive manufacturing or thermal spraying processes. Cylindrical TEGs for using heat from vehicle exhaust pipes can also be made using circular thermocouples arranged in a cylinder. Many designs for TEGs can be made for the different devices they are applied to.

### Thermoelectric systems

Using thermoelectric modules, a thermoelectric system generates power by taking in heat from a source such as a hot exhaust flue. To operate, the system needs a large temperature gradient, which is not easy in real-world applications. The cold side must be cooled by air or water. Heat exchangers are used on both sides of the modules to supply this heating and cooling.

There are many challenges in designing a reliable TEG system that operates at high temperatures. Achieving high efficiency in the system requires extensive engineering design to balance between the heat flow through the modules and maximizing the temperature gradient across them. To do this, designing heat exchanger technologies in the system is one of the most important aspects of TEG engineering. In addition, the system requires to minimize the thermal losses due to the interfaces between materials at several places. Another challenging constraint is avoiding large pressure drops between the heating and cooling sources.

If AC power is required (such as for powering equipment designed to run from AC mains power), the DC power from the TE modules must be passed through an inverter, which lowers efficiency and adds to the cost and complexity of the system.

## Materials for TEG

Only a few known materials to date are identified as thermoelectric materials. Most thermoelectric materials today have a zT, the figure of merit, value of around 1, such as in bismuth telluride (Bi2Te3) at room temperature and lead telluride (PbTe) at 500–700 K. However, in order to be competitive with other power generation systems, TEG materials should have a zT of 2–3. Most research in thermoelectric materials has focused on increasing the Seebeck coefficient (S) and reducing the thermal conductivity, especially by manipulating the nanostructure of the thermoelectric materials. Because both the thermal and electrical conductivity correlate with the charge carriers, new means must be introduced in order to conciliate the contradiction between high electrical conductivity and low thermal conductivity, as is needed.

When selecting materials for thermoelectric generation, a number of other factors need to be considered. During operation, ideally, the thermoelectric generator has a large temperature gradient across it. Thermal expansion will then introduce stress in the device which may cause fracture of the thermoelectric legs or separation from the coupling material. The mechanical properties of the materials must be considered and the coefficient of thermal expansion of the n and p-type material must be matched reasonably well. In segmented thermoelectric generators, the material's compatibility must also be considered to avoid incompatibility of relative current, defined as the ratio of electrical current to diffusion heat current, between segment layers.

A material's compatibility factor is defined as

$s={\frac {{\sqrt {1+zT}}-1}{ST}}$ .

When the compatibility factor from one segment to the next differs by more than a factor of about two, the device will not operate efficiently. The material parameters determining s (as well as zT) are temperature-dependent, so the compatibility factor may change from the hot side to the cold side of the device, even in one segment. This behavior is referred to as self-compatibility and may become important in devices designed for wide-temperature application.

In general, thermoelectric materials can be categorized into conventional and new materials:

### Conventional materials

Many TEG materials are employed in commercial applications today. These materials can be divided into three groups based on the temperature range of operation:

1. Low temperature materials (up to around 450 K): Alloys based on bismuth (Bi) in combinations with antimony (Sb), tellurium (Te) or selenium (Se).
2. Intermediate temperature (up to 850 K): such as materials based on alloys of lead (Pb)
3. Highest temperatures material (up to 1300 K): materials fabricated from silicon-germanium (SiGe) alloys.

Although these materials still remain the cornerstone for commercial and practical applications in thermoelectric power generation, significant advances have been made in synthesizing new materials and fabricating material structures with improved thermoelectric performance. Recent research has focused on improving the material's figure-of-merit (zT), and hence the conversion efficiency, by reducing the lattice thermal conductivity.

### New materials

Researchers are trying to develop new thermoelectric materials for power generation by improving the figure-of-merit zT. One example of these materials is the semiconductor compound ß-Zn4Sb3, which possesses an exceptionally low thermal conductivity and exhibits a maximum zT of 1.3 at a temperature of 670K. This material is also relatively inexpensive and stable up to this temperature in a vacuum, and can be a good alternative in the temperature range between materials based on Bi2Te3 and PbTe. Among the most exciting developments in thermoelectric materials was the development of single crystal tin selenide which produced a record zT of 2.6 in one direction. Other new materials of interest include Skutterudites, Tetrahedrites, and rattling ions crystals.

Besides improving the figure-of-merit, there is increasing focus to develop new materials by increasing the electrical power output, decreasing cost and developing environmentally friendly materials. For example, when the fuel cost is low or almost free, such as in waste heat recovery, then the cost per watt is only determined by the power per unit area and the operating period. As a result, it has initiated a search for materials with high power output rather than conversion efficiency. For example, the rare earth compounds YbAl3 has a low figure-of-merit, but it has a power output of at least double that of any other material, and can operate over the temperature range of a waste heat source.

### Novel processing

To increase the figure of merit (zT), a material's thermal conductivity should be minimized while its electrical conductivity and Seebeck coefficient is maximized. In most cases, methods to increase or decrease one property result in the same effect on other properties due to their interdependence. A novel processing technique exploits the scattering of different phonon frequencies to selectively reduce lattice thermal conductivity without the typical negative effects on electrical conductivity from the simultaneous increased scattering of electrons. In a bismuth antimony tellurium ternary system, liquid-phase sintering is used to produce low-energy semicoherent grain boundaries, which do not have a significant scattering effect on electrons. The breakthrough is then applying a pressure to the liquid in the sintering process, which creates a transient flow of the Te rich liquid and facilitates the formation of dislocations that greatly reduce the lattice conductivity. The ability to selectively decrease the lattice conductivity results in reported zT value of 1.86, which is a significant improvement over the current commercial thermoelectric generators with zT ~ 0.3–0.6. These improvements highlight the fact that in addition to the development of novel materials for thermoelectric applications, using different processing techniques to design microstructure is a viable and worthwhile effort. In fact, it often makes sense to work to optimize both composition and microstructure.

## Uses

Thermoelectric generators (TEG) have a variety of applications. Frequently, thermoelectric generators are used for low power remote applications or where bulkier but more efficient heat engines such as Stirling engines would not be possible. Unlike heat engines, the solid state electrical components typically used to perform thermal to electric energy conversion have no moving parts. The thermal to electric energy conversion can be performed using components that require no maintenance, have inherently high reliability, and can be used to construct generators with long service-free lifetimes. This makes thermoelectric generators well suited for equipment with low to modest power needs in remote uninhabited or inaccessible locations such as mountaintops, the vacuum of space, or the deep ocean.

The main uses of thermoelectric generators are:

- Space probes, including the Mars *Curiosity* rover, generate electricity using a radioisotope thermoelectric generator whose heat source is a radioactive element.
- Waste heat recovery. Every human activity, transport and industrial process generates waste heat, being possible to harvest residual energy from cars, aircraft, ships, industries and the human body. From cars the main source of energy is the exhaust gas. Harvesting that heat energy using a thermoelectric generator can increase the fuel efficiency of the car. Thermoelectric generators have been investigated to replace the alternators in cars demonstrating a 3.45% reduction in fuel consumption. Projections for future improvements are up to a 10% increase in mileage for hybrid vehicles. It has been stated that the potential energy savings could be higher for gasoline engines rather than for diesel engines. For more details, see the article: Automotive thermoelectric generator. For aircraft, engine nozzles have been identified as the best place to recover energy from, but heat from engine bearings and the temperature gradient existing in the aircraft skin have also been proposed.
- Thermoelectric generators are primarily used as remote and off-grid power generators for unmanned sites. They are the most reliable power generator in such situations as they do not have moving parts (thus virtually maintenance-free), work day and night, perform under all weather conditions and can work without battery backup. Although solar photovoltaic systems are also implemented in remote sites, Solar PV may not be a suitable solution where solar radiation is low, i.e. areas at higher latitudes with snow or no sunshine, areas with much cloud or tree canopy cover, dusty deserts, forests, etc. Thermoelectric generators are commonly used on gas pipelines, for example, for cathodic protection, radio communication, and telemetry. On gas pipelines for power consumption of up to 5 kW, thermal generators are preferable to other power sources. The manufacturers of generators for gas pipelines are Global Power Technologies (formerly Global Thermoelectric) (Calgary, Canada) and TELGEN (Russia).
- Microprocessors generate waste heat. Researchers have considered whether some of that energy could be recycled. (However, see below for problems that can arise.)
- Thermoelectric generators have also been investigated as standalone solar-thermal cells. Integration of thermoelectric generators have been directly integrated to a solar thermal cell with efficiency of 4.6%.
- The Maritime Applied Physics Corporation in Baltimore, Maryland is developing a thermoelectric generator to produce electric power on the deep-ocean offshore seabed using the temperature difference between cold seawater and hot fluids released by hydrothermal vents, hot seeps, or from drilled geothermal wells. A high-reliability source of seafloor electric power is needed for ocean observatories and sensors used in the geological, environmental, and ocean sciences, by seafloor mineral and energy resource developers, and by the military. Recent studies have found that deep-sea thermoelectric generators for large scale energy plants are also economically viable.
- Ann Makosinski from British Columbia, Canada has developed several devices using Peltier tiles to harvest heat (from a human hand, the forehead, and hot beverage) that claims to generate enough electricity to power an LED light or charge a mobile device, although the inventor admits that the brightness of the LED light is not competitive with those on the market.
- Thermoelectric generators are used in stove fans. They are put on top of a wood or coal burning stove. The TEG is sandwiched between 2 heat sinks and the difference in temperature will power a slow-moving fan that helps circulate the stove's heat into the room.

## Practical limitations

Besides low efficiency and relatively high cost, practical problems exist in using thermoelectric devices in certain types of applications resulting from a relatively high electrical output resistance, which increases self-heating, and a relatively low thermal conductivity, which makes them unsuitable for applications where heat removal is critical, as with heat removal from an electrical device such as microprocessors.

- **High generator output resistance:** To get voltage output levels in the range required by digital electrical devices, a common approach is to place many thermoelectric elements in series within a generator module. The element's voltages increase, but so does their output resistance. The maximum power transfer theorem dictates that maximum power is delivered to a load when the source and load resistances are identically matched. For low impedance loads near zero ohms, as the generator resistance rises the power delivered to the load decreases. To lower the output resistance, some commercial devices place more individual elements in parallel and fewer in series and employ a boost regulator to raise the voltage to the voltage needed by the load.
- **Low thermal conductivity:** Because a very high thermal conductivity is required to transport thermal energy away from a heat source such as a digital microprocessor, the low thermal conductivity of thermoelectric generators makes them unsuitable to recover the heat.
- **Cold-side heat removal with air:** In air-cooled thermoelectric applications, such as when harvesting thermal energy from a motor vehicle's crankcase, the large amount of thermal energy that must be dissipated into ambient air presents a significant challenge. As a thermoelectric generator's cool side temperature rises, the device's differential working temperature decreases. As the temperature rises, the device's electrical resistance increases causing greater parasitic generator self-heating. In motor vehicle applications a supplementary radiator is sometimes used for improved heat removal, though the use of an electric water pump to circulate a coolant adds parasitic loss to total generator output power. Water cooling the thermoelectric generator's cold side, as when generating thermoelectric power from the hot crankcase of an inboard boat motor, would not suffer from this disadvantage. Water is a far easier coolant to use effectively in contrast to air.

## More on photovoltaic-TEG (PV-TEG) hybrid systems

### Overview

Solar cells use only the high-frequency part of the radiation, while the low-frequency heat energy is wasted. Several patents about the use of thermoelectric devices in parallel or cascade configuration with solar cells have been filed. The idea is to increase the efficiency of the combined solar/thermoelectric system to convert solar radiation into useful electricity. Conventional solar cells also suffer from decreased efficiency (-0.45%/°C) as temperature increases, and the inclusion of TEGs could help dissipate this waste heat while simultaneously increasing solar panel efficiency.

### System architecture

There are two potential methods for coupling TEGs to photovoltaic panels. Mechanically, the simplest is a thermally coupled system. This involves mounting TEGs in an array behind the PV panel. Heat flows from the panel's rear surface into the hot side of the TE modules, which must be cooled on the other side. A simple approach to generate the necessary temperature gradient across the TEGs is to apply heat sinks to promote convective cooling.

The second system is to optically couple photovoltaic cells with TEGs. Using mirrors and filters, incoming solar irradiance is split into two bands. The higher-wavelength infrared spectrum is diverted to an array of TEGs where the thermal energy is scavenged for electricity generation. All other wavelengths are sent to the photovoltaic panel where it is converted to electricity.

### Performance gains

Under ambient conditions, with thermally coupled systems, efficiencies of 3.05% were reported. Higher gains have been noted under optimized conditions. One research group placed a PV-TEG system in an evacuated chamber to prevent convection on the top (hot) surface of the PV array, and to allow them to more carefully control the temperature gradient across the TEGs. They reported an efficiency increase of the TEGs from previously reported values of 0.5% up to 4.4%. Another method for regulating the temperature gradient across TEGs is the use of phase-change materials (PCMs). These materials can help maintain a constant cold-side temperature over the entire panel area and avoid hot spots that may reduce PV efficiency. They also maintain the cold-side of the TEGs at a fixed temperature, and can help smooth out power generation and thus efficiency. Organic-metal hybrid PCMs use nontoxic materials like coconut oil or beeswax coupled with metallic nanoparticles to facilitate thermal conduction into the material for efficient heat transfer.

### Limitations

All of the practical limitations to implementation discussed above apply to these PV-TEG systems. Until TEGs can produce higher than single-digit efficiencies under typical temperature gradients in ambient conditions, they will remain on the fringe of commercial development. The added cost of including TEG arrays on solar panels cannot be justified for the marginal efficiency gains seen with current materials and architectures.

### STEG

The Institute of Optics has announced a Solar Thermoelectric Generator (STEG) capable of efficiencies claimed to be up to 15%. The techniques disclosed are:

- Modified tungsten to selectively absorb light at the optimum solar wavelengths.
- Upper metal surfaces were etched with nanoscale structures to enhance energy absorption within the useful solar spectrum
- Lower surfaces were etched to optimise heat dissipation by radiation at other frequencies.

## Future market

While TEG technology has been used in military and aerospace applications for decades, new TE materials and systems are being developed to generate power using low or high temperatures waste heat, and that could provide a significant opportunity in the near future. These systems can also be scalable to any size and have lower operation and maintenance cost.

The global market for thermoelectric generators is estimated to be US$320 million in 2015 and US$472 million in 2021; up to US$1.44 billion by 2030 with a CAGR of 11.8%. Today, North America captures 66% of the market share and it will continue to be the biggest market in the near future. However, Asia-Pacific and European countries are projected to grow at relatively higher rates. A study found that the Asia-Pacific market would grow at a Compound Annual Growth Rate (CAGR) of 18.3% in the period from 2015 to 2020 due to the high demand of thermoelectric generators by the automotive industries to increase overall fuel efficiency, as well as the growing industrialization in the region.

Small scale thermoelectric generators are also in the early stages of investigation in wearable technologies to reduce or replace charging and boost charge duration. Recent studies focused on the novel development of a flexible inorganic thermoelectric, silver selenide, on a nylon substrate. Thermoelectrics represent particular synergy with wearables by harvesting energy directly from the human body creating a self-powered device. One project used n-type silver selenide on a nylon membrane. Silver selenide is a narrow bandgap semiconductor with high electrical conductivity and low thermal conductivity, making it perfect for thermoelectric applications.

Low power TEG or "sub-watt" (i.e. generating up to 1 watt peak) market is a growing part of the TEG market, capitalizing on the latest technologies. Main applications are sensors, low power applications and more globally Internet of things applications. A specialized market research company indicated that 100,000 units have been shipped in 2014 and expects 9 million units per year by 2020.
