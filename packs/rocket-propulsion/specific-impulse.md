---
title: "Specific impulse"
source: https://en.wikipedia.org/wiki/Specific_impulse
domain: rocket-propulsion
license: CC-BY-SA-4.0
tags: rocket propulsion, specific impulse, ion thruster, rocket engine
fetched: 2026-07-02
---

# Specific impulse

**Specific impulse** (usually abbreviated as *I*sp) is a physical quantity defined as the ratio of change in momentum (impulse) to the mass used, usually fuel. It typically uses units of metres per second (a SI unit) or feet per second (in imperial units). It is equivalent to thrust (a force, in newtons or pounds) per mass flow rate (in kg/s or lbm/s).

It serves as a measure of how efficiently an engine, such as a rocket or jet engine, generates thrust from propellant. *I*sp is the effective exhaust velocity used in the Tsiolkovsky rocket equation which calculates how much a vehicle's velocity can be changed with a given quantity of fuel.

**Normalized specific impulse** is the ratio of specific impulse to Earth's standard acceleration of gravity, *g* (in m/s2 or ft/s2). It is measured in seconds, and conveniently is the same number in both SI and imperial units. It can be understood as the time that one kilogram of fuel can produce one kilogram-force of thrust, which is equal to the time that one pound-mass of fuel can produce one pound-force of thrust.

## Overview

Reaction engines, such as rockets and jet engines propel a vehicle by expelling mass in one direction, which pushes the vehicle in the other direction according to Newton's third law of motion. This expelled mass is called the *reaction mass*. An engine can push harder if it expels the reaction mass at a higher exhaust velocity $v_{e}$ , or expels mass at a faster rate, ${\frac {\mathrm {d} m}{\mathrm {d} t}}$ .

Assuming that the engine expels mass at a constant exhaust velocity $v_{\text{e}}$ , the thrust is $T=v_{\text{e}}{\frac {\mathrm {d} m}{\mathrm {d} t}}.$

If this is integrated over time, the result is the total change in momentum. Dividing by the mass shows that the specific impulse is equal to the exhaust velocity. In practice, the specific impulse is usually lower than the actual physical exhaust velocity due to inefficiencies in the rocket, and thus corresponds to an "effective" exhaust velocity.

The specific impulse $I_{\text{sp}}$ in units of velocity *is defined by* $T_{\text{avg}}=I_{\text{sp}}{\frac {\mathrm {d} m}{\mathrm {d} t}},$ where $T_{\text{avg}}$ is the average thrust.

### Types of engines

The practical meaning of the measurement varies with different types of engines. Car engines consume onboard fuel, breathe environmental air to burn the fuel, and push against the ground beneath them. There is no reaction mass. In this case, *I*sp is momentum per fuel burned.

Chemical rocket engines, by contrast, carry their fuel, oxidizer, and reaction mass with them, so *I*sp is momentum per reaction mass.

Airplane engines are in the middle, as they only push against airflow through the engine. Some of this reaction mass is carried with them, and some is breathed from the air. Therefore, "specific impulse" could be taken to mean either "per reaction mass", as with a rocket, or "per fuel burned" as with cars. The latter is the traditional and more common choice. Because of these differences, specific impulse is not directly comparable between different types of engines.

Specific impulse can be taken as a measure of efficiency. In cars and planes, it typically corresponds with fuel efficiency, i.e. the distance travelled per unit mass or volume of fuel. In rocketry, it corresponds to the achievable delta-*v*, which is the typical way to measure changes between orbits, via the Tsiolkovsky rocket equation $\Delta v=I_{\text{sp}}\ln {\frac {m_{0}}{m_{\text{f}}}},$ where $I_{\text{sp}}$ is the specific impulse measured in units of velocity, and $m_{0},m_{\text{f}}$ are the initial and final masses of the rocket. The difference between $m_{0}$ and $m_{\text{f}}$ is the reaction mass that was expelled.

## Propulsion systems

### Rockets

For any chemical rocket engine, the momentum transfer efficiency depends heavily on the effectiveness of the nozzle. The nozzle is the primary means of converting reactant energy (e.g. thermal or pressure energy) into a flow of momentum moving the same direction. Nozzle shape and effectiveness has a great impact on total momentum transfer from the reaction mass to the rocket.

The efficiency of the conversion of input energy to reactant energy also affects *I*sp, either thermal energy in combustion engines or electrical energy in ion engines. This efficiency determines the amount of delta-v a rocket can perform with a given load of fuel. Optimizing the tradeoffs between fuel quantity and specific impulse is one of the fundamental engineering challenges in rocketry.

Although the specific impulse has units of velocity, it almost never corresponds to an actual physical velocity. In chemical and cold gas rockets, the shape of the nozzle has a high impact on the energy-to-momentum conversion. There are other sources of losses and inefficiencies as well, such as the details of the chemical combustion in such engines. The physical exhaust velocity is higher than the "effective exhaust velocity", which is the "velocity" of the specific impulse. The momentum exchanged and the mass used to generate it *are* physically real measurements. Typically, rocket nozzles work better when the ambient pressure is lower, such as in space versus in the atmosphere. Engines are typically described by a sea-level *I*sp, and a vacuum *I*sp, which is higher. Ion engines, however, do not use a nozzle, although they have other sources of losses so that the momentum transferred is lower than the physical exhaust velocity of their reaction mass.

It is common to express specific impulse as the product of two numbers: a characteristic velocity $c^{*}$ , which summarizes combustion-chamber performance into a quantity with units of speed, and a thrust coefficient $C_{F}$ , which is a dimensionless quantity that summarizes nozzle performance. An additional factor of $g_{0}$ is a units conversion. $I_{\text{sp}}={\frac {c^{*}\cdot C_{F}}{g_{0}}}.$

#### Units of seconds

In rocketry, the specific impulse is often reported in seconds instead of effective exhaust velocity of an engine (m/s), by dividing through standard gravity $g_{0}$ : $I_{\text{sp}}={\frac {v_{e}}{g_{0}}}={\frac {F}{{\dot {m}}\cdot g_{0}}}.$ This is convenient when using gravitational force units (kgf or lbf), since *I*sp then expresses the amount of thrust per unit propellant flow (kg/s or lb/s). Representing specific impulse in units of time also has the advantage of being agnostic between imperial and SI units: $I_{\text{sp}}{\text{[s]}}={\Bigl (}{\frac {F{\text{[kgf]}}}{{\dot {m}}{\text{[kg/s]}}}}{\Bigr )}={\Bigl (}{\frac {F{\text{[lbf]}}}{{\dot {m}}{\text{[lb/s]}}}}{\Bigr )}.$

Physically, *I*sp measured in seconds is the amount of time a rocket engine can generate thrust, given a quantity of propellant whose weight (under *g*0) is equal to the engine's thrust. It is the length of time that the engine can produce 1 kgf (or 1 lbf) of thrust from 1 kg (or 1 lb) of propellant.

### Cars

Although the car industry almost never uses specific impulse on any practical level, the measure can be defined, and makes good contrast against other engine types. Car engines breathe external air to combust their fuel, and (via the wheels) react against the ground. The only meaningful way to interpret "specific impulse" is as "thrust per fuelflow", although one must also specify if the force is measured at the crankshaft or at the wheels, since there are transmission losses. Such a measure corresponds to fuel mileage.

### Airplanes

In an aerodynamic context, there are similarities to both cars and rockets. Like cars, airplane engines breathe outside air; unlike cars they react only against fluids flowing through the engine (including the propellers as applicable). There are several possible ways to interpret "specific impulse": as thrust per fuel flow, as thrust per breathing-flow, or as thrust per "turbine-flow" (i.e. excluding air though the propeller/bypass fan). Since the air breathed is not a direct cost, with wide engineering leeway on how much to breathe, the industry traditionally chooses the "thrust per fuel flow" interpretation with its focus on cost efficiency. In this interpretation, the resulting specific impulse numbers are much higher than for rocket engines, although this comparison is quite different — one is with and the other is without reaction mass. It exemplifies the advantage an airplane engine has over a rocket due to not having to carry the air it uses.

As with all kinds of engines, there are many engineering choices and tradeoffs that affect specific impulse. Nonlinear air resistance and the engine's inability to keep a high specific impulse at a fast burn rate are limiting factors to the fuel consumption rate.

As with rocket engines, the interpretation of specific impulse as a "velocity" does not actually correspond to the physical exhaust velocity. Since the usual interpretation excludes much of the reaction mass, the physical velocity of the reactants downstream is much lower than the effective exhaust velocity suggested from the Isp.

## General considerations

Specific impulse should not be confused with energy efficiency, which can decrease as specific impulse increases, since propulsion systems that give high specific impulse require high energy to do so.

Specific impulse should not be confused with total thrust. Thrust is the force supplied by the engine and depends on the propellant mass flow through the engine. Specific impulse measures the thrust *per* propellant mass flow. Thrust and specific impulse are related by the design and propellants of the engine in question, but this relationship is tenuous: in most cases, high thrust and high specific impulse are mutually exclusive engineering goals. For example, LH2/LO2 bipropellant produces higher *I*sp (due to higher chemical energy and lower exhaust molecular mass) but lower thrust than RP-1/LO2 (due to higher density and propellant flow). In many cases, propulsion systems with very high specific impulse—some ion thrusters reach 25–35 times better *I*sp than chemical engines—produce correspondingly low thrust.

When calculating specific impulse, only propellant carried with the vehicle before use is counted, in the standard interpretation. This usage best corresponds to the cost of operating the vehicle. For a chemical rocket, unlike a plane or car, the propellant mass therefore would include both fuel and oxidizer. For any vehicle, optimizing for specific impulse is generally not the same as optimizing for total performance or total cost. In rocketry, a heavier engine with a higher specific impulse may not be as effective in gaining altitude, distance, or velocity as a lighter engine with a lower specific impulse, especially if the latter engine possesses a higher thrust-to-weight ratio. This is a significant reason for most rocket designs having multiple stages. The first stage can optimized for high thrust to effectively fight gravity drag and air drag, while the later stages operating strictly in orbit and in vacuum can be more easily optimized for higher specific impulse, especially for high delta-v orbits.

### Propellant quantity units

The amount of propellant could be defined either in units of mass or weight. If mass is used, specific impulse is an impulse per unit of mass, which dimensional analysis shows to be equivalent to units of speed; this interpretation is commonly labeled the *effective exhaust velocity*. If a force-based unit system is used, impulse is divided by propellant weight (weight is a measure of force), resulting in units of time. The problem with weight, as a measure of quantity, is that it depends on the acceleration applied to the propellant, which is arbitrary with no relation to the design of the engine. Historically, standard gravity was the reference conversion between weight and mass. But since technology has progressed to the point that we can measure Earth gravity's variation across the surface, and where such differences can cause differences in practical engineering projects (not to mention science projects on other solar bodies), modern science and engineering focus on mass as the measure of quantity, so as to remove the acceleration dependence. Measuring specific impulse by propellant mass gives it the same meaning for a car at sea level, an airplane at cruising altitude, or a helicopter on Mars.

No matter the choice of mass or weight, the resulting quotient of "velocity" or "time" usually doesn't correspond directly to an actual velocity or time. Due to various losses in real engines, the actual exhaust velocity is different from the *I*sp "velocity" (and for cars there isn't even a sensible definition of "actual exhaust velocity"). Rather, the specific impulse is just that: a physical momentum from a physical quantity of propellant (be that in mass or weight).

## Units

|   | Specific impulse | Effective exhaust velocity | Specific fuel consumption |   |
|---|---|---|---|---|
| By weight* | By mass |   |   |   |
| SI | = *x* s | = 9.80665·*x* N·s/kg | = 9.80665·*x* m/s | = 101,972/*x* g/(kN·s) |
| US customary units | = *x* s | = *x* lbf·s/lb | = 32.17405·*x* ft/s | = 3,600/*x* lb/(lbf·h) |
| *as mentioned below, *x* s·*g0* would be physically correct |   |   |   |   |

The most common unit for specific impulse is the second, as values are identical regardless of whether the calculations are done in SI, imperial, or US customary units. Nearly all manufacturers quote their engine performance in seconds, and the unit is also useful for specifying aircraft engine performance.

The use of metres per second to specify effective exhaust velocity is also reasonably common. The unit is intuitive when describing rocket engines, although the effective exhaust speed of the engines may be significantly different from the actual exhaust speed, especially in gas-generator cycle engines. For airbreathing jet engines, the effective exhaust velocity does not account for the mass of the air used (as the air is taken in from the environment), although it can still be used for comparison purposes.

Metres per second are numerically equivalent to newton-seconds per kg (N·s/kg), and SI measurements of specific impulse can be written in terms of either units interchangeably. This unit highlights the definition of specific impulse as impulse per unit mass of propellant.

Specific fuel consumption is inversely proportional to specific impulse and has units of g/(kN·s) or lb/(lbf·h). Specific fuel consumption is used extensively for describing the performance of air-breathing jet engines.

### Specific impulse in seconds

Specific impulse, measured in seconds, can be thought of as how many seconds one kilogram of fuel can produce one kilogram of thrust. Or, more precisely, how many seconds a given propellant, when paired with a given engine, can accelerate its own initial mass at 1 g. The longer it can accelerate its own mass, the more delta-V it delivers to the whole system.

In other words, given a particular engine and a mass of a particular propellant, specific impulse measures for how long a time that engine can exert a continuous force (thrust) until fully burning that mass of propellant. A given mass of a more energy-dense propellant can burn for a longer duration than some less energy-dense propellant made to exert the same force while burning in an engine. Different engine designs burning the same propellant may not be equally efficient at directing their propellant's energy into effective thrust.

For all vehicles, specific impulse (impulse per unit weight-on-Earth of propellant) in seconds can be defined by the following equation:

| $I_{sp}={\frac {F_{avg}}{{\dot {m}}\cdot g_{0}}}$ Where: $I_{\text{sp}}$ is the specific impulse (seconds), $F_{avg}$ is the *average* thrust (newtons, kilograms-force or pounds-force), ${\dot {m}}$ is the mass flow rate of the propellant (kg/s or slugs/s), $g_{0}$ is the standard gravity (defined as 9.80665 m/s2, which is about 32.17405 ft/s2). | $I_{sp}={\frac {I_{total}}{m\cdot g_{0}}}$ Where: $I_{\text{sp}}$ is the specific impulse (seconds), $I_{total}$ is the total impulse (newton-seconds, kg⋅m/s or lbf⋅s), m is the mass of the used propellant (kilograms or pounds), $g_{0}$ is the standard gravity (defined as 9.80665 m/s2, which is about 32.17405 ft/s2). |
|---|---|

*I*sp in seconds is the amount of time a rocket engine can generate thrust, given a quantity of propellant the weight of which is equal to the engine's thrust.

The advantage of this formulation is that it may be used for rockets, where all the reaction mass is carried on board, as well as airplanes, where most of the reaction mass is taken from the atmosphere. In addition, giving the result as a unit of time makes the result easily comparable between calculations in SI units, imperial units, US customary units or other unit framework.

#### Imperial units conversion

The English unit pound mass is more commonly used than the slug, and when using pounds per second for mass flow rate, it is more convenient to express standard gravity as 1 pound-force per pound-mass. Note that this is equivalent to 32.17405 ft/s2, but expressed in more convenient units. This gives:

$F_{\text{thrust}}=I_{\text{sp}}\cdot {\dot {m}}\cdot \left(1\mathrm {\frac {lbf}{lbm}} \right).$

#### Rocketry

In rocketry, the only reaction mass is the propellant, so the specific impulse is calculated using an alternative method, giving results with units of seconds. Specific impulse is defined as the thrust integrated over time per unit weight-on-Earth of the propellant:

$I_{\text{sp}}={\frac {v_{\text{e}}}{g_{0}}},$

where

- $I_{\text{sp}}$ is the specific impulse measured in seconds,
- $v_{\text{e}}$ is the average exhaust speed along the axis of the engine (in m/s or ft/s),
- $g_{0}$ is the standard gravity (in m/s2 or ft/s2).

In rockets, due to atmospheric effects, the specific impulse varies with altitude, reaching a maximum in a vacuum. This is because the exhaust velocity is not simply a function of the chamber pressure, but is a function of the difference between the interior and exterior of the combustion chamber. Values are usually given for operation at sea level ("sl") or in a vacuum ("vac").

### Specific impulse as effective exhaust velocity

Because of the geocentric factor of *g*0 in the equation for specific impulse, many prefer an alternative definition. The specific impulse of a rocket can be defined in terms of thrust per unit mass flow of propellant. This is an equally valid (and in some ways somewhat simpler) way of defining the effectiveness of a rocket propellant. For a rocket, the specific impulse defined in this way is simply the effective exhaust velocity relative to the rocket, *v*e. "In actual rocket nozzles, the exhaust velocity is not really uniform over the entire exit cross section and such velocity profiles are difficult to measure accurately. A uniform axial velocity, *v*e, is assumed for all calculations which employ one-dimensional problem descriptions. This effective exhaust velocity represents an average or mass equivalent velocity at which propellant is being ejected from the rocket vehicle." The two definitions of specific impulse are proportional to one another, and related to each other by: $v_{\text{e}}=g_{0}\cdot I_{\text{sp}},$ where

- $I_{\text{sp}}$ is the specific impulse in seconds,
- $v_{\text{e}}$ is the specific impulse measured in m/s, which is the same as the effective exhaust velocity measured in m/s (or ft/s if g is in ft/s2),
- $g_{0}$ is the standard gravity, 9.80665 m/s2 (in United States customary units 32.174 ft/s2).

This equation is also valid for air-breathing jet engines, but is rarely used in practice.

(Note that different symbols are sometimes used; for example, *c* is also sometimes seen for exhaust velocity. While the symbol $I_{\text{sp}}$ might logically be used for specific impulse in units of (N·s3)/(m·kg); to avoid confusion, it is desirable to reserve this for specific impulse measured in seconds.)

It is related to the thrust, or forward force on the rocket by the equation: $F_{\text{thrust}}=v_{\text{e}}\cdot {\dot {m}},$ where ${\dot {m}}$ is the propellant mass flow rate, which is the rate of decrease of the vehicle's mass.

A rocket must carry all its propellant with it, so the mass of the unburned propellant must be accelerated along with the rocket itself. Minimizing the mass of propellant required to achieve a given change in velocity is crucial to building effective rockets. The Tsiolkovsky rocket equation shows that for a rocket with a given empty mass and a given amount of propellant, the total change in velocity it can accomplish is proportional to the effective exhaust velocity.

A spacecraft without propulsion follows an orbit determined by its trajectory and any gravitational field. Deviations from the corresponding velocity pattern (these are called Δ*v*) are achieved by sending exhaust mass in the direction opposite to that of the desired velocity change.

### Actual exhaust speed versus effective exhaust speed

When an engine is run within the atmosphere, the exhaust velocity is reduced by atmospheric pressure, in turn reducing specific impulse. This is a reduction in the effective exhaust velocity, versus the actual exhaust velocity achieved in vacuum conditions. In the case of gas-generator cycle rocket engines, more than one exhaust gas stream is present as turbopump exhaust gas exits through a separate nozzle. Calculating the effective exhaust velocity requires averaging the two mass flows as well as accounting for any atmospheric pressure.

For air-breathing jet engines, particularly turbofans, the actual exhaust velocity and the effective exhaust velocity are different by orders of magnitude. This happens for several reasons. First, a good deal of additional momentum is obtained by using air as reaction mass, such that combustion products in the exhaust have more mass than the burned fuel. Next, inert gases in the atmosphere absorb heat from combustion, and through the resulting expansion provide additional thrust. Lastly, for turbofans and other designs there is even more thrust created by pushing against intake air which never sees combustion directly. These all combine to allow a better match between the airspeed and the exhaust speed, which saves energy/propellant and enormously increases the *effective* exhaust velocity while reducing the *actual* exhaust velocity. Again, this is because the mass of the air is not counted in the specific impulse calculation, thus attributing *all* of the thrust momentum to the mass of the fuel component of the exhaust, and omitting the reaction mass, inert gas, and effect of driven fans on overall engine efficiency from consideration.

Essentially, the momentum of engine exhaust includes a lot more than just fuel, but specific impulse calculation ignores everything but the fuel. Even though the *effective* exhaust velocity for an air-breathing engine seems nonsensical in the context of actual exhaust velocity, this is still useful for comparing absolute fuel efficiency of different engines.

### Density specific impulse

A related measure, the **density specific impulse**, sometimes also referred to as **Density Impulse** and usually abbreviated as *I*s*d* is the product of the average specific gravity of a given propellant mixture and the specific impulse. While less important than the specific impulse, it is an important measure in launch vehicle design, as a low specific impulse implies that bigger tanks will be required to store the propellant, which in turn will have a detrimental effect on the launch vehicle's mass ratio.

### Specific fuel consumption

Specific impulse is inversely proportional to specific fuel consumption (SFC) by the relationship *I*sp = 1/(*go*·SFC) for SFC in kg/(N·s) and *I*sp = 3600/SFC for SFC in lb/(lbf·hr).

## Examples

| Rocket engines in vacuum |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Model | Type | First run | Application | TSFC | Isp (by weight) | Isp (by mass) |   |
| lb/lbf·h | g/kN·s | s | m/s |   |   |   |   |
| Avio P80 | solid fuel | 2006 | Vega stage 1 | 13 | 360 | 280 | 2700 |
| Avio Zefiro 23 | solid fuel | 2006 | Vega stage 2 | 12.52 | 354.7 | 287.5 | 2819 |
| Avio Zefiro 9A | solid fuel | 2008 | Vega stage 3 | 12.20 | 345.4 | 295.2 | 2895 |
| Merlin 1D | liquid fuel | 2013 | Falcon 9 | 12 | 330 | 310 | 3000 |
| RD-843 | liquid fuel | 2012 | Vega upper stage | 11.41 | 323.2 | 315.5 | 3094 |
| Kuznetsov NK-33 | liquid fuel | 1970s | N-1F, Soyuz-2-1v stage 1 | 10.9 | 308 | 331 | 3250 |
| NPO Energomash RD-171M | liquid fuel | 1985 | Zenit-2M, -3SL, -3SLB, -3F stage 1 | 10.7 | 303 | 337 | 3300 |
| LE-7A | cryogenic | 2001 | H-IIA, H-IIB stage 1 | 8.22 | 233 | 438 | 4300 |
| Snecma HM-7B | cryogenic | 1979 | Ariane 2, 3, 4, 5 ECA upper stage | 8.097 | 229.4 | 444.6 | 4360 |
| LE-5B-2 | cryogenic | 2009 | H-IIA, H-IIB upper stage | 8.05 | 228 | 447 | 4380 |
| Aerojet Rocketdyne RS-25 | cryogenic | 1981 | Space Shuttle, SLS stage 1 | 7.95 | 225 | 453 | 4440 |
| Aerojet Rocketdyne RL-10B-2 | cryogenic | 1998 | Delta III, Delta IV, SLS upper stage | 7.734 | 219.1 | 465.5 | 4565 |
| NERVA NRX A6 | nuclear | 1967 |   |   |   | 869 |   |

| Jet engines with Reheat, static, sea level |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Model | Type | First run | Application | TSFC | Isp (by weight) | Isp (by mass) |   |
| lb/lbf·h | g/kN·s | s | m/s |   |   |   |   |
| Turbo-Union RB.199 | turbofan |   | Tornado | 2.5 | 70.8 | 1440 | 14120 |
| GE F101-GE-102 | turbofan | 1970s | B-1B | 2.46 | 70 | 1460 | 14400 |
| Tumansky R-25-300 | turbojet |   | MIG-21bis | 2.206 | 62.5 | 1632 | 16000 |
| GE J85-GE-21 | turbojet |   | F-5E/F | 2.13 | 60.3 | 1690 | 16570 |
| GE F110-GE-132 | turbofan |   | F-16E/F | 2.09 | 59.2 | 1722 | 16890 |
| Honeywell/ITEC F125 | turbofan |   | F-CK-1 | 2.06 | 58.4 | 1748 | 17140 |
| Snecma M53-P2 | turbofan |   | Mirage 2000C/D/N | 2.05 | 58.1 | 1756 | 17220 |
| Snecma Atar 09C | turbojet |   | Mirage III | 2.03 | 57.5 | 1770 | 17400 |
| Snecma Atar 09K-50 | turbojet |   | Mirage IV, 50, F1 | 1.991 | 56.4 | 1808 | 17730 |
| GE J79-GE-15 | turbojet |   | F-4E/EJ/F/G, RF-4E | 1.965 | 55.7 | 1832 | 17970 |
| Saturn AL-31F | turbofan |   | Su-27/P/K | 1.96 | 55.5 | 1837 | 18010 |
| GE F110-GE-129 | turbofan |   | F-16C/D, F-15EX | 1.9 | 53.8 | 1895 | 18580 |
| Soloviev D-30F6 | turbofan |   | MiG-31, S-37/Su-47 | 1.863 | 52.8 | 1932 | 18950 |
| Lyulka AL-21F-3 | turbojet |   | Su-17, Su-22 | 1.86 | 52.7 | 1935 | 18980 |
| Klimov RD-33 | turbofan | 1974 | MiG-29 | 1.85 | 52.4 | 1946 | 19080 |
| Saturn AL-41F-1S | turbofan |   | Su-35S/T-10BM | 1.819 | 51.5 | 1979 | 19410 |
| Volvo RM12 | turbofan | 1978 | Gripen A/B/C/D | 1.78 | 50.4 | 2022 | 19830 |
| GE F404-GE-402 | turbofan |   | F/A-18C/D | 1.74 | 49 | 2070 | 20300 |
| Kuznetsov NK-32 | turbofan | 1980 | Tu-144LL, Tu-160 | 1.7 | 48 | 2100 | 21000 |
| Snecma M88-2 | turbofan | 1989 | Rafale | 1.663 | 47.11 | 2165 | 21230 |
| Eurojet EJ200 | turbofan | 1991 | Eurofighter | 1.66–1.73 | 47–49 | 2080–2170 | 20400–21300 |

| Dry jet engines, static, sea level |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Model | Type | First run | Application | TSFC | Isp (by weight) | Isp (by mass) |   |
| lb/lbf·h | g/kN·s | s | m/s |   |   |   |   |
| GE J85-GE-21 | turbojet |   | F-5E/F | 1.24 | 35.1 | 2900 | 28500 |
| Snecma Atar 09C | turbojet |   | Mirage III | 1.01 | 28.6 | 3560 | 35000 |
| Snecma Atar 09K-50 | turbojet |   | Mirage IV, 50, F1 | 0.981 | 27.8 | 3670 | 36000 |
| Snecma Atar 08K-50 | turbojet |   | Super Étendard | 0.971 | 27.5 | 3710 | 36400 |
| Tumansky R-25-300 | turbojet |   | MIG-21bis | 0.961 | 27.2 | 3750 | 36700 |
| Lyulka AL-21F-3 | turbojet |   | Su-17, Su-22 | 0.86 | 24.4 | 4190 | 41100 |
| GE J79-GE-15 | turbojet |   | F-4E/EJ/F/G, RF-4E | 0.85 | 24.1 | 4240 | 41500 |
| Snecma M53-P2 | turbofan |   | Mirage 2000C/D/N | 0.85 | 24.1 | 4240 | 41500 |
| Volvo RM12 | turbofan | 1978 | Gripen A/B/C/D | 0.824 | 23.3 | 4370 | 42800 |
| RR Turbomeca Adour | turbofan | 1999 | Jaguar retrofit | 0.81 | 23 | 4400 | 44000 |
| Honeywell/ITEC F124 | turbofan | 1979 | L-159, X-45 | 0.81 | 22.9 | 4440 | 43600 |
| Honeywell/ITEC F125 | turbofan |   | F-CK-1 | 0.8 | 22.7 | 4500 | 44100 |
| PW J52-P-408 | turbojet |   | A-4M/N, TA-4KU, EA-6B | 0.79 | 22.4 | 4560 | 44700 |
| Saturn AL-41F-1S | turbofan |   | Su-35S/T-10BM | 0.79 | 22.4 | 4560 | 44700 |
| Snecma M88-2 | turbofan | 1989 | Rafale | 0.782 | 22.14 | 4600 | 45100 |
| Klimov RD-33 | turbofan | 1974 | MiG-29 | 0.77 | 21.8 | 4680 | 45800 |
| RR Pegasus 11-61 | turbofan |   | AV-8B+ | 0.76 | 21.5 | 4740 | 46500 |
| Eurojet EJ200 | turbofan | 1991 | Eurofighter | 0.74–0.81 | 21–23 | 4400–4900 | 44000–48000 |
| GE F414-GE-400 | turbofan | 1993 | F/A-18E/F | 0.724 | 20.5 | 4970 | 48800 |
| Kuznetsov NK-32 | turbofan | 1980 | Tu-144LL, Tu-160 | 0.72-0.73 | 20–21 | 4900–5000 | 48000–49000 |
| Soloviev D-30F6 | turbofan |   | MiG-31, S-37/Su-47 | 0.716 | 20.3 | 5030 | 49300 |
| Snecma Larzac | turbofan | 1972 | Alpha Jet | 0.716 | 20.3 | 5030 | 49300 |
| IHI F3 | turbofan | 1981 | Kawasaki T-4 | 0.7 | 19.8 | 5140 | 50400 |
| Saturn AL-31F | turbofan |   | Su-27 /P/K | 0.666-0.78 | 18.9–22.1 | 4620–5410 | 45300–53000 |
| RR Spey RB.168 | turbofan |   | AMX | 0.66 | 18.7 | 5450 | 53500 |
| GE F110-GE-129 | turbofan |   | F-16C/D, F-15 | 0.64 | 18 | 5600 | 55000 |
| GE F110-GE-132 | turbofan |   | F-16E/F | 0.64 | 18 | 5600 | 55000 |
| Turbo-Union RB.199 | turbofan |   | Tornado ECR | 0.637 | 18.0 | 5650 | 55400 |
| PW F119-PW-100 | turbofan | 1992 | F-22 | 0.61 | 17.3 | 5900 | 57900 |
| Turbo-Union RB.199 | turbofan |   | Tornado | 0.598 | 16.9 | 6020 | 59000 |
| GE F101-GE-102 | turbofan | 1970s | B-1B | 0.562 | 15.9 | 6410 | 62800 |
| PW TF33-P-3 | turbofan |   | B-52H, NB-52H | 0.52 | 14.7 | 6920 | 67900 |
| RR AE 3007H | turbofan |   | RQ-4, MQ-4C | 0.39 | 11.0 | 9200 | 91000 |
| GE F118-GE-100 | turbofan | 1980s | B-2 | 0.375 | 10.6 | 9600 | 94000 |
| GE F118-GE-101 | turbofan | 1980s | U-2S | 0.375 | 10.6 | 9600 | 94000 |
| General Electric CF6-50C2 | turbofan |   | A300, DC-10-30 | 0.371 | 10.5 | 9700 | 95000 |
| GE TF34-GE-100 | turbofan |   | A-10 | 0.37 | 10.5 | 9700 | 95000 |
| CFM CFM56-2B1 | turbofan |   | C-135, RC-135 | 0.36 | 10 | 10000 | 98000 |
| Progress D-18T | turbofan | 1980 | An-124, An-225 | 0.345 | 9.8 | 10400 | 102000 |
| PW F117-PW-100 | turbofan |   | C-17 | 0.34 | 9.6 | 10600 | 104000 |
| PW PW2040 | turbofan |   | Boeing 757 | 0.33 | 9.3 | 10900 | 107000 |
| CFM CFM56-3C1 | turbofan |   | 737 Classic | 0.33 | 9.3 | 11000 | 110000 |
| GE CF6-80C2 | turbofan |   | 744, 767, MD-11, A300/310, C-5M | 0.307-0.344 | 8.7–9.7 | 10500–11700 | 103000–115000 |
| EA GP7270 | turbofan |   | A380-861 | 0.299 | 8.5 | 12000 | 118000 |
| GE GE90-85B | turbofan |   | 777-200/200ER/300 | 0.298 | 8.44 | 12080 | 118500 |
| GE GE90-94B | turbofan |   | 777-200/200ER/300 | 0.2974 | 8.42 | 12100 | 118700 |
| RR Trent 970-84 | turbofan | 2003 | A380-841 | 0.295 | 8.36 | 12200 | 119700 |
| GE GEnx-1B70 | turbofan |   | 787-8 | 0.2845 | 8.06 | 12650 | 124100 |
| RR Trent 1000C | turbofan | 2006 | 787-9 | 0.273 | 7.7 | 13200 | 129000 |

| Jet engines, cruise |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Model | Type | First run | Application | TSFC | Isp (by weight) | Isp (by mass) |   |
| lb/lbf·h | g/kN·s | s | m/s |   |   |   |   |
|   | Ramjet |   | Mach 1 | 4.5 | 130 | 800 | 7800 |
| J-58 | turbojet | 1958 | SR-71 at Mach 3.2 (Reheat) | 1.9 | 53.8 | 1895 | 18580 |
| RR/Snecma Olympus | turbojet | 1966 | Concorde at Mach 2 | 1.195 | 33.8 | 3010 | 29500 |
| PW JT8D-9 | turbofan |   | 737 Original | 0.8 | 22.7 | 4500 | 44100 |
| Honeywell ALF502R-5 | GTF |   | BAe 146 | 0.72 | 20.4 | 5000 | 49000 |
| Soloviev D-30KP-2 | turbofan |   | Il-76, Il-78 | 0.715 | 20.3 | 5030 | 49400 |
| Soloviev D-30KU-154 | turbofan |   | Tu-154M | 0.705 | 20.0 | 5110 | 50100 |
| RR Tay RB.183 | turbofan | 1984 | Fokker 70, Fokker 100 | 0.69 | 19.5 | 5220 | 51200 |
| GE CF34-3 | turbofan | 1982 | Challenger, CRJ100/200 | 0.69 | 19.5 | 5220 | 51200 |
| GE CF34-8E | turbofan |   | E170/175 | 0.68 | 19.3 | 5290 | 51900 |
| Honeywell TFE731-60 | GTF |   | Falcon 900 | 0.679 | 19.2 | 5300 | 52000 |
| CFM CFM56-2C1 | turbofan |   | DC-8 Super 70 | 0.671 | 19.0 | 5370 | 52600 |
| GE CF34-8C | turbofan |   | CRJ700/900/1000 | 0.67-0.68 | 19–19 | 5300–5400 | 52000–53000 |
| CFM CFM56-3C1 | turbofan |   | 737 Classic | 0.667 | 18.9 | 5400 | 52900 |
| CFM CFM56-2A2 | turbofan | 1974 | E-3, E-6 | 0.66 | 18.7 | 5450 | 53500 |
| RR BR725 | turbofan | 2008 | G650/ER | 0.657 | 18.6 | 5480 | 53700 |
| CFM CFM56-2B1 | turbofan |   | C-135, RC-135 | 0.65 | 18.4 | 5540 | 54300 |
| GE CF34-10A | turbofan |   | ARJ21 | 0.65 | 18.4 | 5540 | 54300 |
| CFE CFE738-1-1B | turbofan | 1990 | Falcon 2000 | 0.645 | 18.3 | 5580 | 54700 |
| RR BR710 | turbofan | 1995 | G. V/G550, Global Express | 0.64 | 18 | 5600 | 55000 |
| GE CF34-10E | turbofan |   | E190/195 | 0.64 | 18 | 5600 | 55000 |
| General Electric CF6-50C2 | turbofan |   | A300B2/B4/C4/F4, DC-10-30 | 0.63 | 17.8 | 5710 | 56000 |
| PowerJet SaM146 | turbofan |   | Superjet LR | 0.629 | 17.8 | 5720 | 56100 |
| CFM CFM56-7B24 | turbofan |   | 737 NG | 0.627 | 17.8 | 5740 | 56300 |
| RR BR715 | turbofan | 1997 | 717 | 0.62 | 17.6 | 5810 | 56900 |
| GE CF6-80C2-B1F | turbofan |   | 747-400 | 0.605 | 17.1 | 5950 | 58400 |
| CFM CFM56-5A1 | turbofan |   | A320 | 0.596 | 16.9 | 6040 | 59200 |
| Aviadvigatel PS-90A1 | turbofan |   | Il-96-400 | 0.595 | 16.9 | 6050 | 59300 |
| PW PW2040 | turbofan |   | 757-200 | 0.582 | 16.5 | 6190 | 60700 |
| PW PW4098 | turbofan |   | 777-300 | 0.581 | 16.5 | 6200 | 60800 |
| GE CF6-80C2-B2 | turbofan |   | 767 | 0.576 | 16.3 | 6250 | 61300 |
| IAE V2525-D5 | turbofan |   | MD-90 | 0.574 | 16.3 | 6270 | 61500 |
| IAE V2533-A5 | turbofan |   | A321-231 | 0.574 | 16.3 | 6270 | 61500 |
| RR Trent 700 | turbofan | 1992 | A330 | 0.562 | 15.9 | 6410 | 62800 |
| RR Trent 800 | turbofan | 1993 | 777-200/200ER/300 | 0.560 | 15.9 | 6430 | 63000 |
| Progress D-18T | turbofan | 1980 | An-124, An-225 | 0.546 | 15.5 | 6590 | 64700 |
| CFM CFM56-5B4 | turbofan |   | A320-214 | 0.545 | 15.4 | 6610 | 64800 |
| CFM CFM56-5C2 | turbofan |   | A340-211 | 0.545 | 15.4 | 6610 | 64800 |
| RR Trent 500 | turbofan | 1999 | A340-500/600 | 0.542 | 15.4 | 6640 | 65100 |
| CFM LEAP-1B | turbofan | 2014 | 737 MAX | 0.53-0.56 | 15–16 | 6400–6800 | 63000–67000 |
| Aviadvigatel PD-14 | turbofan | 2014 | MC-21-310 | 0.526 | 14.9 | 6840 | 67100 |
| RR Trent 900 | turbofan | 2003 | A380 | 0.522 | 14.8 | 6900 | 67600 |
| GE GE90-85B | turbofan |   | 777-200/200ER | 0.52 | 14.7 | 6920 | 67900 |
| GE GEnx-1B76 | turbofan | 2006 | 787-10 | 0.512 | 14.5 | 7030 | 69000 |
| PW PW1400G | GTF |   | MC-21 | 0.51 | 14.4 | 7100 | 69000 |
| CFM LEAP-1C | turbofan | 2013 | C919 | 0.51 | 14.4 | 7100 | 69000 |
| CFM LEAP-1A | turbofan | 2013 | A320neo family | 0.51 | 14.4 | 7100 | 69000 |
| RR Trent 7000 | turbofan | 2015 | A330neo | 0.506 | 14.3 | 7110 | 69800 |
| RR Trent 1000 | turbofan | 2006 | 787 | 0.506 | 14.3 | 7110 | 69800 |
| RR Trent XWB-97 | turbofan | 2014 | A350-1000 | 0.478 | 13.5 | 7530 | 73900 |
| PW 1127G | GTF | 2012 | A320neo | 0.463 | 13.1 | 7780 | 76300 |

| Engine | Effective exhaust velocity (m/s) | Specific impulse (s) | Exhaust specific energy (MJ/kg) |
|---|---|---|---|
| Turbofan jet engine (*actual* V is ~300 m/s) | 29,000 | 3,000 | Approx. 0.05 |
| Space Shuttle Solid Rocket Booster | 2,500 | 250 | 3 |
| Liquid oxygen–liquid hydrogen | 4,400 | 450 | 9.7 |
| NSTAR electrostatic xenon ion thruster | 20,000–30,000 | 1,950–3,100 |   |
| NEXT electrostatic xenon ion thruster | 40,000 | 1,320–4,170 |   |
| VASIMR predictions | 30,000–120,000 | 3,000–12,000 | 1,400 |
| DS4G electrostatic ion thruster | 210,000 | 21,400 | 22,500 |
| Ideal photonic rocket | 299,792,458 | 30,570,000 | 89,875,517,874 |

An example of a specific impulse measured in time is 453 seconds, which is equivalent to an effective exhaust velocity of 4.440 km/s (14,570 ft/s), for the RS-25 engines when operating in a vacuum. An air-breathing jet engine typically has a much larger specific impulse than a rocket; for example a turbofan jet engine may have a specific impulse of 6,000 seconds or more at sea level whereas a rocket would be between 200 and 400 seconds.

An air-breathing engine is thus much more propellant efficient than a rocket engine, because the air serves as reaction mass and oxidizer for combustion which does not have to be carried as propellant, and the actual exhaust speed is much lower, so the kinetic energy the exhaust carries away is lower and thus the jet engine uses far less energy to generate thrust. While the *actual* exhaust velocity is lower for air-breathing engines, the *effective* exhaust velocity is very high for jet engines. This is because the effective exhaust velocity calculation assumes that the carried propellant is providing all the reaction mass and all the thrust. Hence effective exhaust velocity is not physically meaningful for air-breathing engines; nevertheless, it is useful for comparison with other types of engines.

The highest specific impulse for a chemical propellant ever test-fired in a rocket engine was 542 seconds (5.32 km/s) with a tripropellant of lithium, fluorine, and hydrogen. However, this combination is impractical. Lithium and fluorine are both extremely corrosive, lithium ignites on contact with air, fluorine ignites on contact with most fuels, and hydrogen, while not hypergolic, is an explosive hazard. Fluorine and the hydrogen fluoride (HF) in the exhaust are very toxic, which damages the environment, makes work around the launch pad difficult, and makes getting a launch license that much more difficult. The rocket exhaust is also ionized, which would interfere with radio communication with the rocket.

Nuclear thermal rocket engines differ from conventional rocket engines in that energy is supplied to the propellants by an external nuclear heat source instead of the heat of combustion. The nuclear rocket typically operates by passing liquid hydrogen gas through an operating nuclear reactor. Testing in the 1960s yielded specific impulses of about 850 seconds (8,340 m/s), about twice that of the Space Shuttle engines.

A variety of other rocket propulsion methods, such as ion thrusters, give much higher specific impulse but with much lower thrust; for example the Hall-effect thruster on the SMART-1 satellite has a specific impulse of 1,640 s (16.1 km/s) but a maximum thrust of only 68 mN (0.015 lbf). The variable specific impulse magnetoplasma rocket (VASIMR) engine currently in development will theoretically yield 20 to 300 km/s (66,000 to 984,000 ft/s), and a maximum thrust of 5.7 N (1.3 lbf).
