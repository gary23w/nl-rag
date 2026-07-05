---
title: "Computer cooling (part 1/2)"
source: https://en.wikipedia.org/wiki/Computer_cooling
domain: operating-temperature
license: CC-BY-SA-4.0
tags: operating temperature
fetched: 2026-07-05
part: 1/2
---

# Computer cooling

**Computer cooling** is required to remove the waste heat produced by computer hardware to keep components within permissible operating temperature limits. Components that are susceptible to temporary malfunction or permanent failure if overheated include integrated circuits such as central processing units (CPUs), chipsets, graphics cards, hard disk drives, and solid state drives (SSDs).

Components are often designed to generate as little heat as possible, and computers and operating systems may be designed to reduce power consumption and consequent heating according to workload, but more heat may still be produced than can be removed without attention to cooling. Use of heatsinks cooled by airflow reduces the temperature rise produced by a given amount of heat. Attention to patterns of airflow can prevent the development of hotspots. Computer fans are widely used along with heatsink fans to reduce temperature by actively exhausting hot air. There are also other cooling techniques, such as liquid cooling.

All modern day processors are designed to cut out or reduce their voltage or clock speed if the internal temperature of the processor exceeds a specified limit. This is generally known as *thermal throttling* in the case of reduction of clock speeds, or *thermal shutdown* in the case of a complete shutdown of the device or system.

Cooling may be designed to reduce the ambient temperature within the case of a computer, such as by exhausting hot air, or to cool a single component or small area (spot cooling). Components commonly individually cooled include the CPU, graphics processing unit (GPU) and the northbridge.


## Generators of unwanted heat

Integrated circuits (e.g. CPU and GPU) are the main generators of heat in modern computers. Heat generation can be reduced by efficient design and selection of operating parameters such as voltage and frequency, but ultimately, acceptable performance can often only be achieved by managing significant heat generation.

In operation, the temperature of a computer's components will rise until the heat transferred to the surroundings is equal to the heat produced by the component, that is, when thermal equilibrium is reached. For reliable operation, the temperature must never exceed a specified maximum permissible value unique to each component. For semiconductors, instantaneous junction temperature, rather than component case, heatsink, or ambient temperature is critical.

Cooling can be impaired by:

- **Dust** acting as a thermal insulator and impeding airflow, thereby reducing heatsink and fan performance.
- **Poor airflow** including turbulence due to friction against impeding components such as ribbon cables, or incorrect orientation of fans, can reduce the amount of air flowing through a case and even create localized whirlpools of hot air in the case. In some cases of equipment with bad thermal design, cooling air can easily flow out through "cooling" holes before passing over hot components; cooling in such cases can often be improved by blocking of selected holes.
- **Poor heat transfer** due to poor thermal contact between components to be cooled and cooling devices. This can be improved by the use of thermal compounds to even out surface imperfections, or even by lapping.


## Damage prevention

Because high temperatures can significantly reduce life span or cause permanent damage to components, and the heat output of components can sometimes exceed the computer's cooling capacity, manufacturers often take additional precautions to ensure that temperatures remain within safe limits. A computer with thermal sensors integrated in the CPU, motherboard, chipset, or GPU can shut itself down when high temperatures are detected to prevent permanent damage, although this may not completely guarantee long-term safe operation.

Before an overheating component reaches this point, it may be "throttled" until temperatures fall below a safe point using dynamic frequency scaling technology. Throttling reduces the operating frequency and voltage of an integrated circuit or disables non-essential features of the chip to reduce heat output, often at the cost of slightly or significantly reduced performance. For desktop and notebook computers, throttling is often controlled at the BIOS level. Throttling is also commonly used to manage temperatures in smartphones and tablets, where components are packed tightly together with little to no active cooling, and with additional heat transferred from the hand of the user.

The user can also perform several tasks in order to pre-emptively prevent damage from happening. They can perform a visual inspection of the cooler and case fans. If any of them are not spinning correctly, it is likely that they will need to be replaced. The user should also clean the fans thoroughly, since dust and debris can increase the ambient case temperature and impact fan performance. The best way to do so is with compressed air in an open space. Another pre-emptive technique to prevent damage is to replace the thermal paste regularly.


## Mainframes and supercomputers

As electronic computers became larger and more complex, cooling of the active components became a critical factor for reliable operation. Early vacuum-tube computers, with relatively large cabinets, could rely on natural or forced air circulation for cooling. However, solid-state devices were packed much more densely and had lower allowable operating temperatures.

Starting in 1965, IBM and other manufacturers of mainframe computers sponsored intensive research into the physics of cooling densely packed integrated circuits. Many air and liquid cooling systems were devised and investigated, using methods such as natural and forced convection, direct air impingement, direct liquid immersion and forced convection, pool boiling, falling films, flow boiling, and liquid jet impingement. Mathematical analysis was used to predict temperature rises of components for each possible cooling system geometry.

IBM developed three generations of the Thermal Conduction Module (TCM) which used a water-cooled cold plate in direct thermal contact with integrated circuit packages. Each package had a thermally conductive pin pressed onto it, and helium gas surrounded chips and heat-conducting pins. The design could remove up to 27 watts from a chip and up to 2000 watts per module, while maintaining chip package temperatures of around 50 °C (122 °F). Systems using TCMs were the 3081 family (1980), ES/3090 (1984) and some models of the ES/9000 (1990). In the IBM 3081 processor, TCMs allowed up to 2700 watts on a single printed circuit board while maintaining chip temperature at 69 °C (156 °F). Thermal conduction modules using water cooling were also used in mainframe systems manufactured by other companies including Mitsubishi and Fujitsu.

The Cray-1 supercomputer designed in 1976 had a distinctive cooling system. The machine was only 77 inches (2,000 mm) in height and 56+1⁄2 inches (1,440 mm) in diameter, and consumed up to 115 kilowatts; this is comparable to the average power consumption of a few dozen Western homes or a medium-sized car. The integrated circuits used in the machine were the fastest available at the time, using emitter-coupled logic; however, the speed was accompanied by high power consumption compared to later CMOS devices.

Heat removal was critical. Refrigerant was circulated through piping embedded in vertical cooling bars in twelve columnar sections of the machine. Each of the 1662 printed circuit modules of the machine had a copper core and was clamped to the cooling bar. The system was designed to maintain the cases of integrated circuits at no more than 54 °C (129 °F), with refrigerant circulating at 21 °C (70 °F). Final heat rejection was through a water-cooled condenser. Piping, heat exchangers, and pumps for the cooling system were arranged in an upholstered bench seat around the outside of the base of the computer. About 20 percent of the machine's weight in operation was refrigerant.

In the later Cray-2, with its more densely packed modules, Seymour Cray had trouble effectively cooling the machine using the metal conduction technique with mechanical refrigeration, so he switched to 'liquid immersion' cooling. This method involved filling the chassis of the Cray-2 with a liquid called Fluorinert. Fluorinert, as its name implies, is an inert liquid that does not interfere with the operation of electronic components. As the components came to operating temperature, the heat would dissipate into the Fluorinert, which was pumped out of the machine to a chilled water heat exchanger.

Performance per watt of modern systems has greatly improved; many more computations can be carried out with a given power consumption than was possible with the integrated circuits of the 1980s and 1990s. Recent supercomputer projects such as Blue Gene rely on air cooling, which reduces cost, complexity, and size of systems compared to liquid cooling.


## Air cooling

### Heat-sinks

Passive heatsink on a chipset

Active heatsink with a fan and

heat pipes

A component may be fitted in good thermal contact with a heatsink, a passive device with large thermal capacity and with a large surface area relative to its volume. Heatsinks are usually made of a metal with high thermal conductivity such as aluminium or copper, and incorporate fins to increase surface area. Heat from a relatively small component is transferred to the larger heatsink; the equilibrium temperature of the component plus heatsink is much lower than the component's alone would be. Heat is carried away from the heatsink by convective or fan-forced airflow. Fan cooling is often used to cool processors and graphics cards that consume significant amounts of electrical energy. In a computer, a typical heat-generating component may be manufactured with a flat surface. A block of metal with a corresponding flat surface and finned construction, sometimes with an attached fan, is clamped to the component. To fill poorly conducting air gaps due to imperfectly flat and smooth surfaces, a thin layer of thermal grease, a thermal pad, or thermal adhesive may be placed between the component and heatsink.

Heat is removed from the heatsink by convection, to some extent by radiation, and possibly by conduction if the heatsink is in thermal contact with, say, the metal case. Inexpensive fan-cooled aluminium heatsinks are often used on standard desktop computers. Heatsinks with copper base-plates, or made of copper, have better thermal characteristics than those made of aluminium. A copper heatsink is more effective than an aluminium unit of the same size, which is relevant with regard to the high-power-consumption components used in high-performance computers.

Passive heatsinks are commonly found on older CPUs, parts that do not dissipate much power (such as the chipset), computers with low-power processors, and equipment where silent operation is critical and fan noise unacceptable.

Usually a heatsink is clamped to the integrated heat spreader (IHS), a flat metal plate the size of the CPU package which is part of the CPU assembly and spreads the heat locally. A thin layer of thermal compound is placed between them to compensate for surface imperfections. The spreader's primary purpose is to redistribute heat. The heatsink fins improve its efficiency.

Several brands of DDR2, DDR3, DDR4 and DDR5 DRAM memory modules are fitted with a finned heatsink clipped onto the top edge of the module. The same technique is used for video cards that use a finned passive heatsink on the GPU.

Higher-end M.2 SSDs can be prone to significant heat generation, and as a result these may be sold with a heatsink included, or alternatively a third-party heatsink may be attached by the user during installation.

Fan-cooled aluminium heatsinks were originally the norm for desktop computers, but nowadays many heatsinks feature copper base plate, copper base circle, or are entirely made of copper.

Dust tends to build up in the crevices of finned heatsinks, particularly with the high airflow produced by fans. This keeps the air away from the hot component, reducing cooling effectiveness; however, removing the dust restores effectiveness.

### Passive air cooling

Passive heatsink cooling involves attaching a block of machined or extruded metal to the part that needs cooling. A thermal adhesive may be used. More commonly for a personal computer CPU, a clamp holds the heatsink directly over the chip, with a thermal grease or thermal pad spread between. This block has fins and ridges to increase its surface area. The heat conductivity of metal is much better than that of air, and it radiates heat better than the component that it is protecting (usually an integrated circuit or CPU).

Dust build-up between the metal fins of a heatsink gradually reduces efficiency, but can be countered with a gas duster by blowing away the dust along with any other unwanted excess material.

Passive heatsinks are commonly found on older CPUs, parts that do not get very hot (such as the chipset), low-power computers, and embedded devices. Many smartphones use only passive cooling.

Usually a heatsink is attached to the integrated heat spreader (IHS), essentially a large, flat plate attached to the CPU, with conduction paste layered between. This dissipates or spreads the heat locally. Unlike a heatsink, a spreader is meant to redistribute heat, not to remove it. In addition, the IHS protects the fragile CPU.

Passive cooling involves no fan noise, as convection moves air over the heatsink.

### Active air cooling

#### Fans

Fans are used when natural convection is insufficient to remove heat. Fans may be fitted to the computer case or attached to CPUs, GPUs, chipsets, power supply units (PSUs), hard drives, or as cards plugged into an expansion slot. Common fan sizes include 40, 60, 80, 92, 120, and 140 mm. 200, 230, 250 and 300 mm fans are sometimes used in high-performance personal computers.

##### Performance of fans in chassis

A computer has a certain resistance to air flowing through the chassis and components. This is the sum of all the smaller impediments to air flow, such as the inlet and outlet openings, air filters, internal chassis, and electronic components. Fans are simple air pumps that provide pressure to the air of the inlet side relative to the output side. That pressure difference moves air through the chassis, with air flowing to areas of lower pressure.

Fans generally have two published specifications: free air flow and maximum differential pressure. Free air flow is the amount of air a fan will move with zero back-pressure. Maximum differential pressure is the amount of pressure a fan can generate when completely blocked. In between these two extremes are a series of corresponding measurements of flow versus pressure which is usually presented as a graph. Each fan model will have a unique curve, like the dashed curves in the adjacent illustration.

##### Parallel versus series installation

Fans can be installed parallel to each other, in series, or a combination of both. Parallel installation would be fans mounted side by side. Series installation would be a second fan in line with another fan such as an inlet fan and an exhaust fan. To simplify the discussion, it is assumed the fans are the same model.

Parallel fans will provide double the free air flow but no additional driving pressure. Series installation, on the other hand, will double the available static pressure but not increase the free air flow rate. The adjacent illustration shows a single fan versus two fans in parallel with a maximum pressure of 0.15 inches (3.8 mm) of water and a doubled flow rate of about 72 cubic feet per minute (2.0 m3/min).

Note that air flow changes as the square root of the pressure. Thus, doubling the pressure will only increase the flow 1.41 (√2) times, not twice as might be assumed. Another way of looking at this is that the pressure must go up by a factor of four to double the flow rate.

To determine flow rate through a chassis, the chassis impedance curve can be measured by imposing an arbitrary pressure at the inlet to the chassis and measuring the flow through the chassis. This requires fairly sophisticated equipment. With the chassis impedance curve (represented by the solid red and black lines on the adjacent curve) determined, the actual flow through the chassis as generated by a particular fan configuration is graphically shown where the chassis impedance curve crosses the fan curve. The slope of the chassis impedance curve is a square root function, where doubling the flow rate required four times the differential pressure.

In this particular example, adding a second fan provided marginal improvement with the flow for both configurations being approximately 27–28 cubic feet per minute (0.76–0.79 m3/min). While not shown on the plot, a second fan in series would provide slightly better performance than the parallel installation.

##### Temperature vis-à-vis flow rate

The equation for required airflow through a chassis is:

${\text{CFM}}={\frac {P}{Cp\times r\times dT}}$

where

- ${\text{CFM}}$ = Cubic Feet per Minute (0.028 m3/min)
- P = Heat transferred (kW)
- $Cp$ = Specific heat of air
- r = Density
- $dT$ = Change in temperature (in °F)

A simple conservative rule of thumb for cooling flow requirements, discounting such effects as heat loss through the chassis walls and laminar versus turbulent flow, and accounting for the constants for specific heat and density at sea level is:

${\text{CFM}}={\frac {3.16\times P}{{\text{allowed temperature rise in}}^{\circ }F}}$

${\text{CFM}}={\frac {1.76\times P}{{\text{allowed temperature rise in}}^{\circ }C}}$

For example, a typical chassis with 500 watts of load, 130 °F (54 °C) maximum internal temperature in a 100 °F (38 °C) environment, i.e. a difference of 30 °F (17 °C):

${\text{CFM}}={\frac {3.16\times 500\ {\text{W}}}{(130-100)}}=53$

This would be actual flow through the chassis and not the free air rating of the fan. It should also be noted that "Q", the heat transferred, is a function of the heat transfer efficiency of a CPU or GPU cooler to the airflow.

#### Piezoelectric pump

A "dual piezo cooling jet", patented by GE, uses vibrations to pump air through the device. The initial device is three millimetres thick and consists of two nickel discs that are connected on either side to a sliver of piezoelectric ceramics. An alternating current passed through the ceramic component causes it to expand and contract at up to 150 times per second so that the nickel discs act like a bellows. Contracted, the edges of the discs are pushed apart and suck in hot air. Expanding brings the nickel discs together, expelling the air at high velocity.

The device has no bearings and does not require a motor. It is thinner and consumes less energy than typical fans. The jet can move the same amount of air as a cooling fan twice its size while consuming half as much electricity and at lower cost.

#### Ionic wind pump

The cooling technology under development by Kronos and Thorn Micro Technologies employs a device called an ionic wind pump (also known as an electrostatic fluid accelerator). The basic operating principle of an ionic wind pump is corona discharge, an electrical discharge near a charged conductor caused by the ionization of the surrounding air.

The corona discharge cooler developed by Kronos works in the following manner: A high electric field is created at the tip of the cathode, which is placed on one side of the CPU. The high energy potential causes the oxygen and nitrogen molecules in the air to become ionized (positively charged) and create a corona (a halo of charged particles). Placing a grounded anode at the opposite end of the CPU causes the charged ions in the corona to accelerate towards the anode, colliding with neutral air molecules on the way. During these collisions, momentum is transferred from the ionized gas to the neutral air molecules, resulting in movement of gas towards the anode.

The advantages of the corona-based cooler are its lack of moving parts, thereby eliminating certain reliability issues and operating with a near-zero noise level and moderate energy consumption.


## Other techniques

### Heat conduction methods

#### Heat pipes and vapor chambers

A heat pipe is a hollow tube containing a heat transfer liquid. The liquid absorbs heat and evaporates at one end of the pipe. The vapor travels to the other (cooler) end of the tube, where it condenses, giving up its latent heat. The liquid returns to the hot end of the tube by gravity or capillary action and repeats the cycle. Heat pipes have a much higher effective thermal conductivity than solid materials. For use in computers, the heatsink on the CPU is attached to a larger radiator heatsink. Both heatsinks are hollow, as is the attachment between them, creating one large heat pipe that transfers heat from the CPU to the radiator, which is then cooled using some conventional method. This method is usually used when space is tight, as in small form-factor PCs and laptops, or where no fan noise can be tolerated, as in audio production. Because of the efficiency of this method of cooling, many desktop CPUs and GPUs, as well as high end chipsets, use heat pipes or vapor chambers in addition to active fan-based cooling and passive heatsinks to remain within safe operating temperatures. A vapor chamber operates on the same principles as a heat pipe but takes on the form of a slab or sheet instead of a pipe. Heat pipes may be placed vertically on top and form part of vapor chambers. Vapor chambers may also be used on high-end smartphones.

#### Liquid cooling

Liquid cooling is a highly effective method of removing excess heat, with the most common heat transfer fluid in desktop PCs being distilled water with additives. The advantages of water cooling over air cooling include water's higher specific heat capacity and thermal conductivity. Liquid cooling is typically combined with air cooling, using liquid cooling for the hottest components while retaining simpler and cheaper air cooling for less demanding components.

The principle used in a typical active liquid cooling system for computers is identical to that used in an automobile's internal combustion engine, with the water being circulated by a water pump through a water block mounted on the CPU (and sometimes additional components such as the GPU, RAM, or chipset) and out to a heat exchanger, typically a radiator. The radiator is itself usually cooled additionally by means of a fan. Besides a fan, it could possibly also be cooled by other means, such as a Peltier cooler (although Peltier elements are most commonly placed directly on top of the hardware to be cooled, and the coolant is used to conduct the heat away from the hot side of the Peltier element). A coolant reservoir is often also connected to the system.

Besides active liquid cooling systems, passive liquid cooling systems are also sometimes used. These systems often leave out a fan or a water pump, theoretically increasing their reliability and making them quieter than active systems. The downsides of these systems are that they are much less efficient in discarding the heat and thus need much more coolant—and a commensurately larger reservoir— to give it time to cool down.

Liquids allow the transfer of more heat from the parts being cooled than air, making liquid cooling suitable for high-performance computer applications. Compared to air cooling, liquid cooling is also influenced less by the ambient temperature. Liquid cooling allows more flexibility in the placement of the radiator, making it easier to optimize cooling inside a case and expel hot air out, compared to air coolers. While liquid cooling reduces noise levels from better cooling performance and thus slower fan speeds, the pumps used to circulate the liquid often run at high RPMs and can be noisy.

Disadvantages of liquid cooling include complexity and the potential for a coolant leak. Leaking water (and any additives in the water) can damage electronic components with which it comes into contact, and the need to test for and repair leaks makes for more complex and less reliable installations. (The first major foray into the field of liquid-cooled personal computers for general use, the high-end versions of Apple's Power Mac G5, was ultimately doomed by a propensity for coolant leaks.) An air-cooled heatsink is generally much simpler to build, install, and maintain than a water cooling solution, although AIO kits simplify installation.

While originally limited to mainframe computers, liquid cooling has become a practice largely associated with overclocking in the form of either manufactured all-in-one (AIO) kits or do-it-yourself setups assembled from individually gathered parts. Following the invention of the closed-loop liquid cooler (AIO) by Asetek, the 2010s have seen an increase in the popularity of liquid cooling in pre-assembled, moderate to high performance, desktop computers. Sealed closed-loop systems incorporating a pre-filled radiator, fan or fans, and waterblock incorporating a pump simplify the installation and maintenance of water cooling at a slight cost in cooling effectiveness relative to larger and more complex setups.

Additional uses of the heat carried by liquid cooling have been demonstrated. The IBM Aquasar system uses *hot water cooling* to achieve energy efficiency and the water being used to heat buildings as well.

##### Pumped thermosiphon

Alternately, a new breed of the cooling system is being developed, inserting a pump into the thermosiphon loop. This adds another degree of flexibility for the design engineer, as the heat can now be effectively transported away from the heat source and either reclaimed or dissipated to ambient. Junction temperature can be tuned by adjusting the system pressure; higher pressure equals higher fluid saturation temperatures. This allows for smaller condensers, smaller fans, and/or the effective dissipation of heat in a high ambient temperature environment. These systems are, in essence, the next-generation fluid cooling paradigm, as they are approximately 10 times more efficient than single-phase water. Since the system uses a dielectric as the heat transport medium, leaks do not cause a catastrophic failure of the electric system.

A "thermosiphon" traditionally refers to a closed system consisting of several pipes and/or chambers, with a larger chamber containing a small reservoir of liquid (often having a boiling point just above ambient temperature, but not necessarily). The larger chamber is as close to the heat source and designed to conduct as much heat from it into the liquid as possible, for example, a CPU cold plate with the chamber inside it filled with the liquid. One or more pipes extend upward into some sort of radiator or similar heat dissipation area, and this is all set up such that the CPU heats the reservoir and liquid it contains, which begins boiling, and the vapor travels up the tube(s) into the radiator/heat dissipation area, and then after condensing, drips back down into the reservoir, or runs down the sides of the tube. This requires no moving parts, and is somewhat similar to a heat pump, except that capillary action is not used, making it potentially better in some sense (perhaps most importantly, better in that it is much easier to build, and much more customizable for specific use cases and the flow of coolant/vapor can be arranged in a much wider variety of positions and distances, and have far greater thermal mass and maximum capacity compared to heat pipes which are limited by the amount of coolant present and the speed and flow rate of coolant that capillary action can achieve with the wicking used, often sintered copper powder on the walls of the tube, which have a limited flow rate and capacity.)

#### Chip-integrated

Conventional cooling techniques all attach their "cooling" component to the outside of the computer chip package. This "attaching" technique will always exhibit some thermal resistance, reducing its effectiveness. The heat can be more efficiently and quickly removed by directly cooling the local hot spots of the chip, within the package. At these locations, power dissipation of over 300 W/cm2 (typical CPU is less than 100 W/cm2) can occur, although future systems are expected to exceed 1000 W/cm2. This form of local cooling is essential to developing high power density chips. This ideology has led to the investigation of integrating cooling elements into the computer chip. Currently there are two techniques: micro-channel heatsinks, and jet impingement cooling.

In micro-channel heatsinks, channels are fabricated into the silicon chip (CPU), and coolant is pumped through them. The channels are designed with very large surface area which results in large heat transfers. Heat dissipation of 3000 W/cm2 has been reported with this technique. The heat dissipation can be further increased if two-phase flow cooling is applied. Unfortunately, the system requires large pressure drops, due to the small channels, and the heat flux is lower with dielectric coolants used in electronic cooling.

Another local chip cooling technique is jet impingement cooling. In this technique, a coolant is flowed through a small orifice to form a jet. The jet is directed toward the surface of the CPU chip, and can effectively remove large heat fluxes. Heat dissipation of over 1000 W/cm2 has been reported. The system can be operated at lower pressure in comparison to the micro-channel method. The heat transfer can be further increased using two-phase flow cooling and by integrating return flow channels (hybrid between micro-channel heatsinks and jet impingement cooling).

### Heat conduction targets

#### Liquid nitrogen

As liquid nitrogen boils at −196 °C (−320.8 °F), far below the freezing point of water, it is valuable as an extreme coolant for short overclocking sessions.

In a typical installation of liquid nitrogen cooling, a copper or aluminium pipe is mounted on top of the processor or graphics card. After the system has been heavily insulated against condensation, the liquid nitrogen is poured into the pipe, resulting in temperatures well below −100 °C (−148 °F).

Evaporation devices ranging from cut out heatsinks with pipes attached to custom-milled copper containers are used to hold the nitrogen as well as to prevent large temperature changes. However, after the nitrogen evaporates, it has to be refilled. In the realm of personal computers, this method of cooling is seldom used in contexts other than overclocking trial runs and record-setting attempts, as the CPU will usually expire within a relatively short period of time due to temperature stress caused by changes in internal temperature.

Although liquid nitrogen is non-flammable, it can condense oxygen directly from air. Mixtures of liquid oxygen and flammable materials can be dangerously explosive.

Liquid nitrogen cooling is, generally, only used for processor benchmarking, due to the fact that continuous usage may cause permanent damage to one or more parts of the computer and, if handled in a careless way, can even harm the user, causing frostbite.

#### Liquid helium

Liquid helium, colder than liquid nitrogen, has also been used for cooling. Liquid helium boils at −269 °C (−452.20 °F), and temperatures ranging from −230 to −240 °C (−382.0 to −400.0 °F) have been measured from the heatsink. However, liquid helium is more expensive and more difficult to store and use than liquid nitrogen. Also, extremely low temperatures can cause integrated circuits to stop functioning. Silicon-based semiconductors, for example, will freeze out at around −233 °C (−387.4 °F).

#### Evaporative tower

Commonly known as bong or boiler cooling, due to the outward appearance. Water is atomized and blown through a heatsink with a fan. The mist increases the surface area of water, which cools the water itself. Ice can be added for lower temperatures.

#### Refrigeration

##### Peltier (thermoelectric) cooling

Peltier junctions are generally only around 10–15% as efficient as the ideal refrigerator (Carnot cycle), compared with 40–60% achieved by conventional compression cycle systems (reverse Rankine systems using compression/expansion). Due to this lower efficiency, thermoelectric cooling is generally only used in environments where the solid state nature (no moving parts, low maintenance, compact size, and orientation insensitivity) outweighs pure efficiency.

Modern TECs use several stacked units each composed of dozens or hundreds of thermocouples laid out next to each other, which allows for a substantial amount of heat transfer. A combination of bismuth and tellurium is most commonly used for the thermocouples.

As active heat pumps which consume power, TECs can produce temperatures below ambient, impossible with passive heatsinks, radiator-cooled liquid cooling, and heatpipe HSFs. However, while pumping heat, a Peltier module will typically consume more electric power than the heat amount being pumped.

It is also possible to use a Peltier element together with a high pressure refrigerant (two phase cooling) to cool the CPU.

##### Vapor compression

Phase-change cooling is an extremely effective way to cool the processor. A vapor compression phase-change cooler is a unit that usually sits underneath the PC, with a tube leading to the processor. Inside the unit is a compressor of the same type as in an air conditioner. The compressor compresses a gas (or mixture of gases) which comes from the evaporator (CPU cooler discussed below). Then, the very hot high-pressure vapor is pushed into the condenser (heat dissipation device) where it condenses from a hot gas into a liquid, typically subcooled at the exit of the condenser then the liquid is fed to an expansion device (restriction in the system) to cause a drop in pressure a vaporize the fluid (cause it to reach a pressure where it can boil at the desired temperature); the expansion device used can be a simple capillary tube to a more elaborate thermal expansion valve. The liquid evaporates (changing phase), absorbing the heat from the processor as it draws extra energy from its environment to accommodate this change (see latent heat). The evaporation can produce temperatures reaching around −15 to −150 °C (5 to −238 °F). The liquid flows into the evaporator cooling the CPU, turning into a vapor at low pressure. At the end of the evaporator this gas flows down to the compressor and the cycle begins over again. This way, the processor can be cooled to temperatures ranging from −15 to −150 °C (5 to −238 °F), depending on the load, wattage of the processor, the refrigeration system (see refrigeration) and the gas mixture used. This type of system suffers from a number of issues (cost, weight, size, vibration, maintenance, cost of electricity, noise, need for a specialized computer tower) but, mainly, one must be concerned with dew point and the proper insulation of all sub-ambient surfaces that must be done (the pipes will sweat, dripping water on sensitive electronics).

This type of cooling is seen as a more extreme way to cool components since the units are relatively expensive compared to the average desktop. They also generate a significant amount of noise, since they are essentially refrigerators; however, the compressor choice and air cooling system is the main determinant of this, allowing for flexibility for noise reduction based on the parts chosen.

### Both

#### Liquid immersion cooling

Another growing trend due to the increasing heat density of computers, GPUs, FPGAs, and ASICs is to immerse the entire computer or select components in a thermally, but not electrically, conductive liquid. Although rarely used for the cooling of personal computers, liquid immersion is a routine method of cooling large power distribution components such as transformers. It is also becoming popular with data centers. Personal computers cooled in this manner may not require either fans or pumps, and may be cooled exclusively by passive heat exchange between the computer hardware and the enclosure it is placed in. A heat exchanger (i.e. heater core or radiator) might still be needed though, and the piping also needs to be placed correctly.

The coolant used must have sufficiently low electrical conductivity not to interfere with the normal operation of the computer. If the liquid is somewhat electrically conductive, it may cause electrical shorts between components or traces and permanently damage them. For these reasons, it is preferred that the liquid be an insulator (dielectric) and not conduct electricity.

A wide variety of liquids exist for this purpose, including transformer oils, synthetic single-phase and dual phase dielectric coolants such as 3M Fluorinert or 3M Novec. Non-purpose oils, including cooking, motor and silicone oils, have been successfully used for cooling personal computers.

Some fluids used in immersion cooling, especially hydrocarbon-based materials such as mineral oils, cooking oils, and organic esters, may degrade some common materials used in computers such as rubbers, polyvinyl chloride (PVC), and thermal greases. Therefore, it is critical to review the material compatibility of such fluids prior to use. Mineral oil in particular has been found to have negative effects on PVC and rubber-based wire insulation. Thermal pastes used to transfer heat to heatsinks from processors and graphic cards has been reported to dissolve in some liquids, however with negligible impact to cooling, unless the components were removed and operated in air.

Evaporation, especially for 2-phase coolants, can pose a problem, and the liquid may require either to be regularly refilled or sealed inside the computer's enclosure. Immersion cooling can allow for extremely low PUE values of 1.05, vs air cooling's 1.35, and allow for up to 100 KW of computing power (heat dissipation, TDP) per 19-inch rack, as opposed to air cooling, which usually handles up to 23 KW.

### Other

### Waste heat reduction

#### Part selection

Where powerful computers with many features are not required, less powerful computers or ones with fewer features can be used. As of 2011 a VIA EPIA motherboard with CPU typically dissipates approximately 25 watts of heat, whereas a more capable Pentium 4 motherboard and CPU typically dissipates around 140 watts. Computers can be powered with direct current from an external power supply unit which does not generate heat inside the computer case. The replacement of cathode-ray-tube (CRT) displays by more efficient thin-screen liquid crystal display (LCD) ones in the early twenty-first century has reduced power consumption significantly.

#### Soft cooling

Soft cooling is the practice of utilizing software to take advantage of CPU power saving technologies to minimize energy use. This is done using halt instructions to turn off or put in standby state CPU subparts that aren't being used or by underclocking the CPU. While resulting in lower total speeds, this can be very useful if overclocking a CPU to improve user experience rather than increase raw processing power, since it can prevent the need for noisier cooling. Contrary to what the term suggests, it is not a form of cooling but of reducing heat creation.

##### Undervolting

Undervolting is a practice of running the CPU or any other component with voltages below the device specifications. An undervolted component draws less power and thus produces less heat. The ability to do this varies by manufacturer, product line, and even different production runs of the same product (as well as that of other components in the system), but processors are often specified to use voltages higher than strictly necessary. This tolerance ensures that the processor will have a higher chance of performing correctly under sub-optimal conditions, such as a lower-quality motherboard or low power supply voltages. Below a certain limit, the processor will not function correctly, although undervolting too far does not typically lead to permanent hardware damage (unlike overvolting).

Undervolting is used for quiet systems, as less cooling is needed because of the reduction of heat production, allowing noisy fans to be omitted. It is also used when battery charge life must be maximized.
