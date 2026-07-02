---
title: "Rocket engine (part 1/2)"
source: https://en.wikipedia.org/wiki/Rocket_engine
domain: rocket-propulsion
license: CC-BY-SA-4.0
tags: rocket propulsion, specific impulse, ion thruster, rocket engine
fetched: 2026-07-02
part: 1/2
---

# Rocket engine

A **rocket engine**, also known as a **rocket motor**, is a reaction engine, producing thrust in accordance with Newton's third law by ejecting reaction mass rearward, usually a high-speed jet of high-temperature gas produced by the combustion of rocket propellant stored inside the rocket. However, non-combusting forms such as cold gas thrusters, nuclear thermal rockets, and ion engines exist. Rocket vehicles carry their own oxidiser, unlike most combustion engines such as pulse engines or jet engines, so rocket engines can be used in a vacuum, and they can achieve great speed, beyond escape velocity if enough delta V is supplied. Vehicles commonly propelled by rocket engines include missiles, artillery shells, ballistic missiles, and spaceships.

Compared to other types of jet engines, rocket engines typically have the highest thrust, but are the least propellant-efficient (they have the lowest specific impulse). For thermal rockets, pure hydrogen, the lightest of all elements, gives the highest exhaust velocity, but practical chemical rockets produce a mix of heavier species, reducing the exhaust velocity.


## Terminology

Here, "rocket" is used as an abbreviation for "rocket engine".

**Thermal rockets** use an inert propellant, heated by electricity (electrothermal propulsion) or a nuclear reactor (nuclear thermal rocket).

**Chemical rockets** are powered by exothermic reduction-oxidation chemical reactions of the propellant:

- **Solid-fuel rockets** (or **solid-propellant rockets** or **motors**) are chemical rockets which use propellant in a solid state.
- **Liquid-propellant rockets** use one or more propellants in a liquid state fed from tanks by pumps.
- **Hybrid rockets** use a solid propellant in the combustion chamber, to which a second liquid or gas oxidiser or propellant is added to permit combustion.
- **Monopropellant rockets** use a single propellant decomposed by a catalyst. The most common monopropellants are hydrazine and hydrogen peroxide.


## Principle of operation

Rocket engines produce thrust by the expulsion of gas that has been accelerated to high speed through a nozzle. The fluid is usually a gas created by high pressure (150-to-4,350-pound-per-square-inch (10 to 300 bar)) combustion of solid or liquid propellants, consisting of fuel and oxidiser components, within a combustion chamber. As the gases expand through the nozzle, they are accelerated to very high (supersonic) speed, and the reaction to this pushes the vehicle (rocket) in the opposite direction. Combustion is most frequently used for practical rockets, as the laws of thermodynamics (more specifically Carnot's theorem) dictate that high temperatures and pressures are desirable for the best thermal efficiency. Nuclear thermal rockets are capable of higher efficiencies, but have low thrust, thanks to the low mass of the propellants used, and also have environmental problems which preclude their routine use in the Earth's atmosphere and cislunar space.

For model rocketry, an available alternative to combustion is a water rocket pressurized by compressed air, carbon dioxide, nitrogen, or any other readily available, inert gas.

### Propellant

Rocket propellant is mass that is stored, usually in some form of tank, or within the combustion chamber itself, prior to being ejected from a rocket engine in the form of a fluid jet to produce thrust.

Chemical rocket propellants are the most commonly used. These undergo exothermic chemical reactions producing a hot jet of gas for propulsion. Alternatively, a chemically inert reaction mass can be heated by a high-energy power source through a heat exchanger in lieu of a combustion chamber.

Solid rocket propellants are prepared in a mixture of fuel and oxidising components called *grain*, and the propellant storage casing effectively becomes the combustion chamber.

### Injection

Liquid-fueled rockets force separate fuel and oxidizer components into the combustion chamber, where they mix and burn. Hybrid rocket engines use a combination of solid and liquid or gaseous propellants. Both liquid and hybrid rockets use *injectors* to introduce the propellant into the chamber. These are often an array of simple jets – holes through which the propellant escapes under pressure; but sometimes may be more complex spray nozzles. When two or more propellants are injected, the jets usually deliberately cause the propellants to collide as this breaks up the flow into smaller droplets that burn more easily.

### Combustion chamber

For chemical rockets the combustion chamber is typically cylindrical, and flame holders, used to hold a part of the combustion in a slower-flowing portion of the combustion chamber, are not needed. The dimensions of the cylinder are such that the propellant is able to combust thoroughly; different rocket propellants require different combustion chamber sizes for this to occur.

This leads to a number called $L^{*}$ , the characteristic length:

$L^{*}={\frac {V_{c}}{A_{t}}}$

where:

- $V_{c}$ is the volume of the chamber
- $A_{t}$ is the area of the throat of the nozzle.

L* is typically in the range of 64–152 centimetres (25–60 in).

The temperatures and pressures typically reached in a rocket combustion chamber in order to achieve practical thermal efficiency are extreme compared to a non-afterburning airbreathing jet engine. No atmospheric nitrogen is present to dilute and cool the combustion, so the propellant mixture can reach true stoichiometric ratios. This, in combination with the high pressures, means that the rate of heat conduction through the walls is very high.

In order for fuel and oxidiser to flow into the chamber, the pressure of the propellants entering the combustion chamber must exceed the pressure inside the combustion chamber itself. This may be accomplished by a variety of design approaches including turbopumps or, in simpler engines, via sufficient tank pressure to advance fluid flow. Tank pressure may be maintained by several means, including a high-pressure helium pressurization system common to many large rocket engines or, in some newer rocket systems, by a bleed-off of high-pressure gas from the engine cycle to autogenously pressurize the propellant tanks For example, the self-pressurization gas system of the SpaceX Starship is a critical part of SpaceX strategy to reduce launch vehicle fluids from five in their legacy Falcon 9 vehicle family to just two in Starship, eliminating not only the helium tank pressurant but all hypergolic propellants as well as nitrogen for cold-gas reaction-control thrusters.

### Nozzle

The hot gas produced in the combustion chamber is permitted to escape through a narrow space, called the throat, to increase the velocity until it reaches Mach 1, and then continues to accelerate through a diverging expansion section. When sufficient pressure is provided to the nozzle (about 2.5–3 times ambient pressure), the nozzle *chokes* and a supersonic jet is formed, dramatically accelerating the gas, converting most of the thermal energy into kinetic energy. Exhaust speeds vary, depending on the expansion ratio the nozzle is designed for, but exhaust speeds as high as ten times the speed of sound in air at sea level are not uncommon. About half of the rocket engine's thrust comes from the unbalanced pressures inside the combustion chamber, and the rest comes from the pressures acting against the inside of the nozzle (see diagram). As the gas expands (adiabatically) the pressure against the nozzle's walls forces the rocket engine in one direction while accelerating the gas in the other.

The most commonly used nozzle is the de Laval nozzle, a fixed geometry nozzle with a high expansion-ratio. The large bell- or cone-shaped nozzle extension beyond the throat gives the rocket engine its characteristic shape.

The exit static pressure of the exhaust jet depends on the chamber pressure and the ratio of exit to throat area of the nozzle. As exit pressure varies from the ambient (atmospheric) pressure, a choked nozzle is said to be

- **under-expanded** (exit pressure greater than ambient),
- **perfectly expanded** (exit pressure equals ambient),
- **over-expanded** (exit pressure less than ambient; shock diamonds form outside the nozzle), or
- **grossly over-expanded** (a shock wave forms inside the nozzle extension).

In practice, perfect expansion is only achievable with a variable–exit-area nozzle (since ambient pressure decreases as altitude increases), and is not possible above a certain altitude as ambient pressure approaches zero. If the nozzle is not perfectly expanded, then loss of efficiency occurs. Grossly over-expanded nozzles lose less efficiency, but can cause mechanical problems with the nozzle. Fixed-area nozzles become progressively more under-expanded as they gain altitude. Almost all de Laval nozzles will be momentarily grossly over-expanded during startup in an atmosphere.

Nozzle efficiency is affected by operation in the atmosphere because atmospheric pressure changes with altitude; but due to the supersonic speeds of the gas exiting from a rocket engine, the pressure of the jet may be either below or above ambient, and equilibrium between the two is not reached at all altitudes (see diagram).

#### Back pressure and optimal expansion

For optimal performance, the pressure of the gas at the end of the nozzle should just equal the ambient pressure: if the exhaust's pressure is lower than the ambient pressure, then the vehicle will be slowed by the difference in pressure between the top of the engine and the exit; on the other hand, if the exhaust's pressure is higher, then exhaust pressure that could have been converted into thrust is not converted, and energy is wasted.

To maintain this ideal of equality between the exhaust's exit pressure and the ambient pressure, the diameter of the nozzle would need to increase with altitude, giving the pressure a longer nozzle to act on (and reducing the exit pressure and temperature). This increase is difficult to arrange in a lightweight fashion, although is routinely done with other forms of jet engines. In rocketry a lightweight compromise nozzle is generally used and some reduction in atmospheric performance occurs when used at other than the 'design altitude' or when throttled. To improve on this, various exotic nozzle designs such as the plug nozzle, stepped nozzles, the expanding nozzle and the aerospike have been proposed, each providing some way to adapt to changing ambient air pressure and each allowing the gas to expand further against the nozzle, giving extra thrust at higher altitudes.

When exhausting into a sufficiently low ambient pressure (vacuum) several issues arise. One is the sheer weight of the nozzle—beyond a certain point, for a particular vehicle, the extra weight of the nozzle outweighs any performance gained. Secondly, as the exhaust gases adiabatically expand within the nozzle they cool, and eventually some of the chemicals can freeze, producing 'snow' within the jet. This causes instabilities in the jet and must be avoided.

On a De Laval nozzle, exhaust gas flow detachment will occur in a grossly over-expanded nozzle. As the detachment point will not be uniform around the axis of the engine, a side force may be imparted to the engine. This side force may change over time and result in control problems with the launch vehicle.

Advanced altitude-compensating designs, such as the aerospike or plug nozzle, attempt to minimize performance losses by adjusting to varying expansion ratio caused by changing altitude.

### Propellant efficiency

For a rocket engine to be propellant efficient, it is important that the maximum pressures possible be created on the walls of the chamber and nozzle by a specific amount of propellant; as this is the source of the thrust. This can be achieved by all of:

- heating the propellant to as high a temperature as possible (using a high energy fuel, containing hydrogen and carbon and sometimes metals such as aluminium, or even using nuclear energy)
- using a low specific density gas (as hydrogen rich as possible)
- using propellants which are, or decompose to, simple molecules with few degrees of freedom to maximise translational velocity

Since all of these things minimise the mass of the propellant used, and since pressure is proportional to the mass of propellant present to be accelerated as it pushes on the engine, and since from Newton's third law the pressure that acts on the engine also reciprocally acts on the propellant, it turns out that for any given engine, the speed that the propellant leaves the chamber is unaffected by the chamber pressure (although the thrust is proportional). However, speed is significantly affected by all three of the above factors and the exhaust speed is an excellent measure of the engine propellant efficiency. This is termed *exhaust velocity*, and after allowance is made for factors that can reduce it, the **effective exhaust velocity** is one of the most important parameters of a rocket engine (although weight, cost, ease of manufacture etc. are usually also very important).

For aerodynamic reasons the flow goes sonic ("chokes") at the narrowest part of the nozzle, the 'throat'. Since the speed of sound in gases increases with the square root of temperature, the use of hot exhaust gas greatly improves performance. By comparison, at room temperature the speed of sound in air is about 340 m/s while the speed of sound in the hot gas of a rocket engine can be over 1700 m/s; much of this performance is due to the higher temperature, but additionally rocket propellants are chosen to be of low molecular mass, and this also gives a higher velocity compared to air.

Expansion in the rocket nozzle then further multiplies the speed, typically between 1.5 and 2 times, giving a highly collimated hypersonic exhaust jet. The speed increase of a rocket nozzle is mostly determined by its area expansion ratio—the ratio of the area of the exit to the area of the throat, but detailed properties of the gas are also important. Larger ratio nozzles are more massive but are able to extract more heat from the combustion gases, increasing the exhaust velocity.

### Thrust vectoring

Vehicles typically require the overall thrust to change direction over the length of the burn. A number of different ways to achieve this have been flown:

- The entire engine is mounted on a hinge or gimbal and any propellant feeds reach the engine via low pressure flexible pipes or rotary couplings.
- Just the combustion chamber and nozzle is gimballed, the pumps are fixed, and high pressure feeds attach to the engine.
- Multiple engines (often canted at slight angles) are deployed but throttled to give the overall vector that is required, giving only a very small penalty.
- High-temperature vanes protrude into the exhaust and can be tilted to deflect the jet.


## Overall performance

Rocket technology can combine very high thrust (meganewtons), very high exhaust speeds (around 10 times the speed of sound in air at sea level) and very high thrust/weight ratios (>100) *simultaneously* as well as being able to operate outside the atmosphere, and while permitting the use of low pressure and hence lightweight tanks and structure.

Rockets can be further optimised to even more extreme performance along one or more of these axes at the expense of the others.

### Specific impulse

| Rocket | Propellants | *I*sp, vacuum (s) |
|---|---|---|
| Space Shuttle liquid engines | LOX/LH2 | 453 |
| Space Shuttle solid motors | APCP | 268 |
| Space Shuttle OMS | NTO/MMH | 313 |
| Saturn V stage 1 | LOX/RP-1 | 304 |

The most important metric for the efficiency of a rocket engine is impulse per unit of propellant, this is called specific impulse (usually written $I_{sp}$ ). This is either measured as a speed (the *effective exhaust velocity* $v_{e}$ in metres/second or ft/s) or as a time (seconds). For example, if an engine producing 100 pounds of thrust runs for 320 seconds and burns 100 pounds of propellant, then the specific impulse is 320 seconds. The higher the specific impulse, the less propellant is required to provide the desired impulse.

The specific impulse that can be achieved is primarily a function of the propellant mix (and ultimately would limit the specific impulse), but practical limits on chamber pressures and the nozzle expansion ratios reduce the performance that can be achieved.

### Net thrust

Below is an approximate equation for calculating the net thrust of a rocket engine:

$F_{n}={\dot {m}}\;v_{e}={\dot {m}}\;v_{e-opt}+A_{e}(p_{e}-p_{amb})$

| where: |   |
|---|---|
| ${\dot {m}}$ | = exhaust gas mass flow |
| $v_{e}$ | = effective exhaust velocity (sometimes otherwise denoted as *c* in publications) |
| $v_{e-opt}$ | = effective jet velocity when Pamb = Pe |
| $A_{e}$ | = flow area at nozzle exit plane (or the plane where the jet leaves the nozzle if separated flow) |
| $p_{e}$ | = static pressure at nozzle exit plane |
| $p_{amb}$ | = ambient (or atmospheric) pressure |

Since, unlike a jet engine, a conventional rocket motor lacks an air intake, there is no 'ram drag' to deduct from the gross thrust. Consequently, the net thrust of a rocket motor is equal to the gross thrust (apart from static back pressure).

The ${\dot {m}}\;v_{e-opt}\,$ term represents the momentum thrust, which remains constant at a given throttle setting, whereas the $A_{e}(p_{e}-p_{amb})\,$ term represents the pressure thrust term. At full throttle, the net thrust of a rocket motor improves slightly with increasing altitude, because as atmospheric pressure decreases with altitude, the pressure thrust term increases. At the surface of the Earth the pressure thrust may be reduced by up to 30%, depending on the engine design. This reduction drops roughly exponentially to zero with increasing altitude.

Maximum efficiency for a rocket engine is achieved by maximising the momentum contribution of the equation without incurring penalties from over expanding the exhaust. This occurs when $p_{e}=p_{amb}$ . Since ambient pressure changes with altitude, most rocket engines spend very little time operating at peak efficiency.

Since specific impulse is force divided by the rate of mass flow, this equation means that the specific impulse varies with altitude.

### Vacuum specific impulse, Isp

Due to the specific impulse varying with pressure, a quantity that is easy to compare and calculate with is useful. Because rockets choke at the throat, and because the supersonic exhaust prevents external pressure influences travelling upstream, it turns out that the pressure at the exit is ideally exactly proportional to the propellant flow ${\dot {m}}$ , provided the mixture ratios and combustion efficiencies are maintained. It is thus quite usual to rearrange the above equation slightly:

$F_{vac}=C_{f}\,{\dot {m}}\,c^{*}$

and so define the *vacuum Isp* to be:

$v_{evac}=C_{f}\,c^{*}\,$

where:

$c^{*}$

= the

characteristic velocity

of the combustion chamber (dependent on propellants and combustion efficiency)

$C_{f}$

= the

thrust coefficient

of the nozzle (dependent on nozzle geometry, typically about 2)

And hence:

$F_{n}={\dot {m}}\,v_{evac}-A_{e}\,p_{amb}$

### Throttling

Rockets can be throttled by controlling the propellant combustion rate ${\dot {m}}$ (usually measured in kg/s or lb/s). In liquid and hybrid rockets, the propellant flow entering the chamber is controlled using valves, in solid rockets it is controlled by changing the area of propellant that is burning and this can be designed into the propellant grain (and hence cannot be controlled in real-time).

Rockets can usually be throttled down to an exit pressure of about one-third of ambient pressure (often limited by flow separation in nozzles) and up to a maximum limit determined only by the mechanical strength of the engine.

In practice, the degree to which rockets can be throttled varies greatly, but most rockets can be throttled by a factor of 2 without great difficulty; the typical limitation is combustion stability, as for example, injectors need a minimum pressure to avoid triggering damaging oscillations (chugging or combustion instabilities); but injectors can be optimised and tested for wider ranges.

For example, some more recent liquid-propellant engine designs that have been optimised for greater throttling capability (BE-3, Raptor) can be throttled to as low as 18–20 per cent of rated thrust.

Solid rockets can be throttled by using shaped grains that will vary their surface area over the course of the burn.

### Energy efficiency

Rocket engine nozzles are surprisingly efficient heat engines for generating a high speed jet, as a consequence of the high combustion temperature and high compression ratio. Rocket nozzles give an excellent approximation to adiabatic expansion which is a reversible process, and hence they give efficiencies which are very close to that of the Carnot cycle. Given the temperatures reached, over 60% efficiency can be achieved with chemical rockets.

For a *vehicle* employing a rocket engine the energetic efficiency is very good if the vehicle speed approaches or somewhat exceeds the exhaust velocity (relative to launch); but at low speeds the energy efficiency goes to 0% at zero speed (as with all jet propulsion). See Rocket energy efficiency for more details.

### Thrust-to-weight ratio

Rockets, of all the jet engines, indeed of essentially all engines, have the highest thrust-to-weight ratio. This is especially true for liquid-fueled rocket engines.

This high performance is due to the small volume of pressure vessels that make up the engine—the pumps, pipes and combustion chambers involved. The lack of inlet duct and the use of dense liquid propellant allows the pressurisation system to be small and lightweight, whereas duct engines have to deal with air which has around three orders of magnitude lower density.

| Jet or rocket engine | Mass | Thrust | Thrust-to- weight ratio |   |   |
|---|---|---|---|---|---|
| (kg) | (lb) | (kN) | (lbf) |   |   |
| RD-0410 nuclear rocket engine | 2,000 | 4,400 | 35.2 | 7,900 | 1.8 |
| J58 jet engine (SR-71 Blackbird) | 2,722 | 6,001 | 150 | 34,000 | 5.2 |
| Rolls-Royce/Snecma Olympus 593 turbojet with reheat (Concorde) | 3,175 | 7,000 | 169.2 | 38,000 | 5.4 |
| Pratt & Whitney F119 | 1,800 | 3,900 | 91 | 20,500 | 7.95 |
| RD-0750 rocket engine, three-propellant mode | 4,621 | 10,188 | 1,413 | 318,000 | 31.2 |
| RD-0146 rocket engine | 260 | 570 | 98 | 22,000 | 38.4 |
| Rocketdyne RS-25 rocket engine | 3,177 | 7,004 | 2,278 | 512,000 | 73.1 |
| RD-180 rocket engine | 5,393 | 11,890 | 4,152 | 933,000 | 78.5 |
| RD-170 rocket engine | 9,750 | 21,500 | 7,887 | 1,773,000 | 82.5 |
| F-1 (Saturn V first stage) | 8,391 | 18,499 | 7,740.5 | 1,740,100 | 94.1 |
| NK-33 rocket engine | 1,222 | 2,694 | 1,638 | 368,000 | 136.7 |
| Merlin 1D rocket engine, full-thrust version | 467 | 1,030 | 825 | 185,000 | 180.1 |

Of the liquid fuels used, density is lowest for liquid hydrogen. Although hydrogen/oxygen burning has the highest specific impulse of any in-use chemical rocket, hydrogen's very low density (about one-fourteenth that of water) requires larger and heavier turbopumps and pipework, which decreases the engine's thrust-to-weight ratio (for example the RS-25) compared to those that do not use hydrogen (NK-33).


## Mechanical issues

Rocket combustion chambers are normally operated at fairly high pressure, typically 10–200 bar (1–20 MPa, 150–3,000 psi). When operated within significant atmospheric pressure, higher combustion chamber pressures give better performance by permitting a larger and more efficient nozzle to be fitted without it being grossly overexpanded.

However, these high pressures cause the outermost part of the chamber to be under very large hoop stresses – rocket engines are pressure vessels.

Worse, due to the high temperatures created in rocket engines the materials used tend to have a significantly lowered working tensile strength.

In addition, significant temperature gradients are set up in the walls of the chamber and nozzle, these cause differential expansion of the inner liner that create internal stresses.

### Hard starts

A **hard start** refers to an over-pressure condition during start of a rocket engine at ignition. In the worst cases, this takes the form of an unconfined explosion, resulting in the damage or destruction of the engine.

Rocket fuels, hypergolic or otherwise, must be introduced into the combustion chamber at the correct rate in order to have a controlled rate of production of hot gas. A "hard start" indicates that the quantity of combustible propellant that entered the combustion chamber prior to ignition was too large. The result is an excessive spike of pressure, possibly leading to structural failure or explosion.

Avoiding hard starts involves careful timing of the ignition relative to valve timing or varying the mixture ratio so as to limit the maximum pressure that can occur or simply ensuring an adequate ignition source is present well prior to propellant entering the chamber.

Explosions from hard starts usually cannot happen with purely gaseous propellants, since the amount of the gas present in the chamber is limited by the injector area relative to the throat area, and for practical designs, propellant mass escapes too quickly to be an issue.

A famous example of a hard start was the explosion of Wernher von Braun's "1W" engine during a demonstration to General Walter Dornberger on December 21, 1932. Delayed ignition allowed the chamber to fill with alcohol and liquid oxygen, which exploded violently. Shrapnel was embedded in the walls, but nobody was hit.


## Acoustic issues

The extreme vibration and acoustic environment inside a rocket motor commonly result in peak stresses well above mean values, especially in the presence of organ pipe-like resonances and gas turbulence.

### Combustion instabilities

The combustion may display undesired instabilities, of sudden or periodic nature. The pressure in the injection chamber may increase until the propellant flow through the injector plate decreases; a moment later the pressure drops and the flow increases, injecting more propellant in the combustion chamber which burns a moment later, and again increases the chamber pressure, repeating the cycle. This may lead to high-amplitude pressure oscillations, often in ultrasonic range, which may damage the motor. Oscillations of ±200 psi at 25 kHz were the cause of failures of early versions of the Titan II missile second stage engines. The other failure mode is a deflagration to detonation transition; the supersonic pressure wave formed in the combustion chamber may destroy the engine.

Combustion instability was also a problem during Atlas development. The Rocketdyne engines used in the Atlas family were found to suffer from this effect in several static firing tests, and three missile launches exploded on the pad due to rough combustion in the booster engines. In most cases, it occurred while attempting to start the engines with a "dry start" method whereby the igniter mechanism would be activated prior to propellant injection. During the process of man-rating Atlas for Project Mercury, solving combustion instability was a high priority, and the final two Mercury flights sported an upgraded propulsion system with baffled injectors and a hypergolic igniter.

The problem affecting Atlas vehicles was mainly the so-called "racetrack" phenomenon, where burning propellant would swirl around in a circle at faster and faster speeds, eventually producing vibration strong enough to rupture the engine, leading to complete destruction of the rocket. It was eventually solved by adding several baffles around the injector face to break up swirling propellant.

More significantly, combustion instability was a problem with the Saturn F-1 engines. Some of the early units tested exploded during static firing, which led to the addition of injector baffles.

In the Soviet space program, combustion instability also proved a problem on some rocket engines, including the RD-107 engine used in the R-7 family and the RD-216 used in the R-14 family, and several failures of these vehicles occurred before the problem was solved. Soviet engineering and manufacturing processes never satisfactorily resolved combustion instability in larger RP-1/LOX engines, so the RD-171 engine used to power the Zenit family still used four smaller thrust chambers fed by a common engine mechanism.

The combustion instabilities can be provoked by remains of cleaning solvents in the engine (e.g. the first attempted launch of a Titan II in 1962), reflected shock wave, initial instability after ignition, explosion near the nozzle that reflects into the combustion chamber, and many more factors. In stable engine designs the oscillations are quickly suppressed; in unstable designs they persist for prolonged periods. Oscillation suppressors are commonly used.

Three different types of combustion instabilities occur:

#### Chugging

A low frequency oscillation in chamber pressure below 200 Hertz. Usually it is caused by pressure variations in feed lines due to variations in acceleration of the vehicle, when rocket engines are building up thrust, are shut down or are being throttled.

Chugging can cause a worsening feedback loop, as cyclic variation in thrust causes longitudinal vibrations to travel up the rocket, causing the fuel lines to vibrate, which in turn do not deliver propellant smoothly into the engines. This phenomenon is known as "pogo oscillations" or "pogo", named after the pogo stick.

In the worst case, this may result in damage to the payload or vehicle. Chugging can be minimised by using several methods, such as installing energy-absorbing devices on feed lines. Chugging may cause Screeching.

#### Buzzing

An intermediate frequency oscillation in chamber pressure between 200 and 1000 Hertz. Usually caused due to insufficient pressure drop across the injectors. It generally is mostly annoying, rather than being damaging.

Buzzing is known to have adverse effects on engine performance and reliability, primarily as it causes material fatigue. In extreme cases combustion can end up being forced backwards through the injectors – this can cause explosions with monopropellants. Buzzing may cause Screeching.

#### Screeching

A high frequency oscillation in chamber pressure above 1000 Hertz, sometimes called screaming or squealing. The most immediately damaging, and the hardest to control. It is due to acoustics within the combustion chamber that often couples to the chemical combustion processes that are the primary drivers of the energy release, and can lead to unstable resonant "screeching" that commonly leads to catastrophic failure due to thinning of the insulating thermal boundary layer. Acoustic oscillations can be excited by thermal processes, such as the flow of hot air through a pipe or combustion in a chamber. Specifically, standing acoustic waves inside a chamber can be intensified if combustion occurs more intensely in regions where the pressure of the acoustic wave is maximal.

Such effects are very difficult to predict analytically during the design process, and have usually been addressed by expensive, time-consuming and extensive testing, combined with trial and error remedial correction measures.

Screeching is often dealt with by detailed changes to injectors, changes in the propellant chemistry, vaporising the propellant before injection or use of Helmholtz dampers within the combustion chambers to change the resonant modes of the chamber.

Testing for the possibility of screeching is sometimes done by exploding small explosive charges outside the combustion chamber with a tube set tangentially to the combustion chamber near the injectors to determine the engine's impulse response and then evaluating the time response of the chamber pressure- a fast recovery indicates a stable system.

### Exhaust noise

For all but the very smallest sizes, rocket exhaust compared to other engines is generally very noisy. As the hypersonic exhaust mixes with the ambient air, shock waves are formed. The Space Shuttle generated over 200 dB(A) of noise around its base. To reduce this, and the risk of payload damage or injury to the crew atop the stack, the mobile launcher platform was fitted with a Sound Suppression System that sprayed 1.1 million litres (290,000 US gal) of water around the base of the rocket in 41 seconds at launch time. Using this system kept sound levels within the payload bay to 142 dB.

The sound intensity from the shock waves generated depends on the size of the rocket and on the exhaust velocity. Such shock waves seem to account for the characteristic crackling and popping sounds produced by large rocket engines when heard live. These noise peaks typically overload microphones and audio electronics, and so are generally weakened or entirely absent in recorded or broadcast audio reproductions. For large rockets at close range, the acoustic effects could actually kill.

More worryingly for space agencies, such sound levels can also damage the launch structure, or worse, be reflected back at the comparatively delicate rocket above. This is why so much water is typically used at launches. The water spray changes the acoustic qualities of the air and reduces or deflects the sound energy away from the rocket.

Generally speaking, noise is most intense when a rocket is close to the ground, since the noise from the engines radiates up away from the jet, as well as reflecting off the ground. Also, when the vehicle is moving slowly, little of the chemical energy input to the engine can go into increasing the kinetic energy of the rocket (since useful power *P* transmitted to the vehicle is $P=F*V$ for thrust *F* and speed *V*). Then the largest portion of the energy is dissipated in the exhaust's interaction with the ambient air, producing noise. This noise can be reduced somewhat by flame trenches with roofs, by water injection around the jet and by deflecting the jet at an angle.


## Rocket engine development

### United States

The development of the US rocket engine industry has been shaped by a complex web of relationships between government agencies, private companies, research institutions, and other stakeholders.

Since the establishment of the first liquid-propellant rocket engine company (Reaction Motors, Inc.) in 1941 and the first government laboratory (GALCIT) devoted to the subject, the US liquid-propellant rocket engine (LPRE) industry has undergone significant changes. At least 14 US companies have been involved in the design, development, manufacture, testing, and flight support operations of various types of rocket engines from 1940 to 2000. In contrast to other countries like Russia, China, or India, where only government or pseudogovernment organisations engage in this business, the US government relies heavily on private industry. These commercial companies are essential to the continued viability of the United States and its form of governance, as they compete with one another to provide cutting-edge rocket engines that meet the needs of the government, the military, and the private sector. In the United States the company that develops the LPRE usually is awarded the production contract.

Generally, the need or demand for a new rocket engine comes from government agencies such as NASA or the Department of Defense. Once the need is identified, government agencies may issue requests for proposals (RFPs) to solicit proposals from private companies and research institutions. Private companies and research institutions, in turn, may invest in research and development (R&D) activities to develop new rocket engine technologies that meet the needs and specifications outlined in the RFPs.

Alongside private companies, universities, independent research institutes and government laboratories also play a critical role in the research and development of rocket engines.

Universities provide graduate and undergraduate education to train qualified technical personnel, and their research programs often contribute to the advancement of rocket engine technologies. More than 25 universities in the US have taught or are currently teaching courses related to Liquid Propellant Rocket Engines (LPREs), and their graduate and undergraduate education programs are considered one of their most important contributions. Universities such as Princeton University, Cornell University, Purdue University, Pennsylvania State University, University of Alabama, the Navy's Post-Graduate School, or the California Institute of Technology have conducted excellent R&D work on topics related to the rocket engine industry. One of the earliest examples of the contribution of universities to the rocket engine industry is the work of the GALCIT in 1941. They demonstrated the first jet-assisted takeoff (JATO) rockets to the Army, leading to the establishment of the Jet Propulsion Laboratory.

However the transfer of knowledge from research professors and their projects to the rocket engine industry has been a mixed experience. While some notable professors and relevant research projects have positively influenced industry practices and understanding of LPREs, the connection between university research and commercial companies has been inconsistent and weak. Universities were not always aware of the industry's specific needs, and engineers and designers in the industry had limited knowledge of university research. As a result, many university research programs remained relatively unknown to industry decision-makers. Furthermore, in the last few decades, certain university research projects, while interesting to professors, were not useful to the industry due to a lack of communication or relevance to industry needs.

Government laboratories, including the Rocket Propulsion Laboratory (now part of Air Force Research Laboratory), Arnold Engineering Test Center, NASA Marshall Space Flight Center, Jet Propulsion Laboratory, Stennis Space Center, White Sands Proving Grounds, and NASA John H. Glenn Research Center, have played crucial roles in the development of liquid rocket propulsion engines (LPREs). They have conducted unbiased testing, guided work at US and some non-US contractors, performed research and development, and provided essential testing facilities including hover test facilities and simulated altitude test facilities and resources. Initially, private companies or foundations financed smaller test facilities, but since the 1950s, the U.S. government has funded larger test facilities at government laboratories. This approach reduced costs for the government by not building similar facilities at contractors' plants but increased complexity and expenses for contractors. Nonetheless, government laboratories have solidified their significance and contributed to LPRE advancements.

LPRE programs have been subject to several cancellations in the United States, even after spending millions of dollars on their development. For example, the M-l LOX/LH2 LPRE, Titan I, and the RS-2200 aerospike, as well as several JATO units and large uncooled thrust chambers were cancelled. The cancellations of these programs were not related to the specific LPRE's performance or any issues with it. Instead, they were due to the cancellation of the vehicle programs the engine was intended for or budget cuts imposed by the government.

### USSR

Russia and the former Soviet Union was and still is the world's foremost nation in developing and building rocket engines. From 1950 to 1998, their organisations developed, built, and put into operation a larger number and a larger variety of liquid propellant rocket engine (LPRE) designs than any other country. Approximately 500 different LPREs have been developed before 2003. For comparison the United States has developed slightly more than 300 (before 2003). The Soviets also had the most rocket-propelled flight vehicles. They had more liquid propellant ballistic missiles and more space launch vehicles derived or converted from these decommissioned ballistic missiles than any other nation. As of the end of 1998, the Russians (or earlier the Soviet Union) had successfully launched 2573 satellites with LPREs or almost 65% of the world total of 3973. All of these vehicle flights were made possible by the timely development of suitable high-performance reliable LPREs.

#### Institutions and actors

Unlike many other countries where the development and production of rocket engines were consolidated within a single organisation, the Soviet Union took a different approach, they established numerous specialised design bureaus (DB) which would compete for development contracts. These design bureaus, or "konstruktorskoye buro" (KB) in Russian were state run organisations which were primarily responsible for carrying out research, development and prototyping of advanced technologies usually related to military hardware, such as turbojet engines, aircraft components, missiles, or space launch vehicles.

Design bureaus which specialised in rocket engines often possessed the necessary personnel, facilities, and equipment to conduct laboratory tests, flow tests, and ground testing of experimental rocket engines. Some even had specialised facilities for testing very large engines, conducting static firings of engines installed in vehicle stages, or simulating altitude conditions during engine tests. In certain cases, engine testing, certification and quality control were outsourced to other organisations and locations with more suitable test facilities. Many DBs also had housing complexes, gymnasiums, and medical facilities intended to support the needs of their employees and their families.

The Soviet Union's LPRE development effort saw significant growth during the 1960s and reached its peak in the 1970s. This era coincided with the Cold War between the Soviet Union and the United States, characterised by intense competition in spaceflight achievements. Between 14 and 17 Design Bureaus and research institutes were actively involved in developing LPREs during this period. These organisations received relatively steady support and funding due to high military and spaceflight priorities, which facilitated the continuous development of new engine concepts and manufacturing methods.

Once a mission with a new vehicle (missile or spacecraft) was established it was passed on to a design bureau whose role was to oversee the development of the entire rocket. If none of the previously developed rocket engines met the needs of the mission, a new rocket engine with specific requirements would be contracted to another DB specialised in LPRE development (oftentimes each DB had expertise in specific types of LPREs with different applications, propellants, or engine sizes). This meant that the development or design study of a rocket engine was always aimed at a specific application which entailed set requirements.

When it comes to which DBs were awarded contracts for the development of new rocket engines either a single design bureau would be chosen or several design bureaus would be given the same contract which sometimes led to fierce competition between DBs.

When only one DB was picked for the development, it was often the result of the relationship between a vehicle or system's chief designer and the chief designer of a rocket engine specialised DB. If the vehicle's chief designer was happy with previous work done by a certain design bureau it was not unusual to see continued reliance on that LPRE bureau for that class of engines. For example, all but one of the LPREs for submarine-launched missiles were developed by the same design bureau for the same vehicle development prime contractor.

However, when two parallel engine development programs were supported in order to select the superior one for a specific application, several qualified rocket engine models were never used. This luxury of choice was not commonly available in other nations. However, the use of design bureaus also led to certain issues, including program cancellations and duplication. Some major programs were cancelled, resulting in the disposal or storage of previously developed engines.

One notable example of duplication and cancellation was the development of engines for the R-9A ballistic missile. Two sets of engines were supported, but ultimately only one set was selected, leaving several perfectly functional engines unused. Similarly, for the ambitious heavy N-l space launch vehicle intended for lunar and planetary missions, the Soviet Union developed and put into production at least two engines for each of the six stages. Additionally, they developed alternate engines for a more advanced N-l vehicle. However, the program faced multiple flight failures, and with the United States' successful Moon landing, the program was ultimately cancelled, leaving the Soviet Union with a surplus of newly qualified engines without a clear purpose.

These examples demonstrate the complex dynamics and challenges faced by the Soviet Union in managing the development and production of rocket engines through Design Bureaus.

#### Accidents

The development of rocket engines in the Soviet Union was marked by significant achievements, but it also carried ethical considerations due to numerous accidents and fatalities. From a Science and Technology Studies point of view, the ethical implications of these incidents shed light on the complex relationship between technology, human factors, and the prioritisation of scientific advancement over safety.

The Soviet Union encountered a series of tragic accidents and mishaps in the development and operation of rocket engines. Notably, the USSR holds the unfortunate distinction of having experienced more injuries and deaths resulting from liquid propellant rocket engine (LPRE) accidents than any other country. These incidents brought into question the ethical considerations surrounding the development, testing, and operational use of rocket engines.

One of the most notable disasters occurred in 1960 when the R-16 ballistic missile suffered a catastrophic accident on the launchpad at the Tyuratam launch facility. This incident resulted in the deaths of 124 engineers and military personnel, including Marshal M.I. Nedelin, a former deputy minister of defence. The explosion occurred after the second-stage rocket engine suddenly ignited, causing the fully loaded missile to disintegrate. The explosion resulted from the ignition and explosion of the mixed hypergolic propellants, consisting of nitric acid with additives and UDMH (unsymmetrical dimethylhydrazine).

While the immediate cause of the 1960 accident was attributed to a lack of protective circuits in the missile control unit, the ethical considerations surrounding LPRE accidents in the USSR extend beyond specific technical failures. The secrecy surrounding these accidents, which remained undisclosed for approximately three decades, raises concerns about transparency, accountability, and the protection of human life.

The decision to keep fatal LPRE accidents hidden from the public eye reflects a broader ethical dilemma. The Soviet government, driven by the pursuit of scientific and technological superiority during the Cold War, sought to maintain an image of invincibility and conceal the failures that accompanied their advancements. This prioritisation of national prestige over the well-being and safety of workers raises questions about the ethical responsibility of the state and the organisations involved.
