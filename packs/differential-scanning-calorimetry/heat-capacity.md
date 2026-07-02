---
title: "Heat capacity"
source: https://en.wikipedia.org/wiki/Heat_capacity
domain: differential-scanning-calorimetry
license: CC-BY-SA-4.0
tags: heat flow, glass transition, melting endotherm, thermal transition
fetched: 2026-07-02
---

# Heat capacity

**Heat capacity** or **thermal capacity** is a physical property of matter, defined as the amount of heat that must be supplied to an object to produce a unit change in its temperature. The SI unit of heat capacity is joule per kelvin (J/K). It quantifies the ability of a material or system to store thermal energy.

Heat capacity is an extensive property. The corresponding intensive property is the specific heat capacity, found by dividing the heat capacity of an object by its mass. Dividing the heat capacity by the amount of substance in moles yields its molar heat capacity. The volumetric heat capacity measures the heat capacity per volume. In architecture and civil engineering, the heat capacity of a building is often referred to as its *thermal mass*.

## Definition

### Basic definition

The heat capacity of an object, denoted by C , is the limit $C=\lim _{\Delta T\to 0}{\frac {Q}{\Delta T}},$ where Q is the amount of heat that must be added to the object (of mass *M*) in order to raise its temperature by $\Delta T$ .

The value of this parameter usually varies considerably depending on the starting temperature T of the object and the pressure p applied to it. In particular, it typically varies dramatically with phase transitions such as melting or vaporization (see enthalpy of fusion and enthalpy of vaporization). Therefore, it is considered a function $C(p,T)$ of those two variables.

### Variation with temperature

The variation can be ignored in contexts when working with objects in narrow ranges of temperature and pressure. For example, the heat capacity of a block of iron weighing one pound is about 204 J/K when measured from a starting temperature *T* = 25 °C and *P* = 1 atm of pressure. That approximate value is adequate for temperatures between 15 °C and 35 °C, and surrounding pressures from 0 to 10 atmospheres, because the exact value varies very little in those ranges. One can trust that the same heat input of 204 J will raise the temperature of the block from 15 °C to 16 °C, or from 34 °C to 35 °C, with negligible error.

### Heat capacities of a homogeneous system undergoing different thermodynamic processes

#### At constant pressure, *dQ* = *dU* + *pdV* (isobaric process)

At constant pressure, heat supplied to the system contributes to both the work done and the change in internal energy, according to the first law of thermodynamics. The heat capacity is called $C_{p}$ and defined as:

$C_{p}=\left.{\frac {dQ}{dT}}\right|_{p={\text{const}}}$

From the first law of thermodynamics follows $dQ=dU+p\,dV$ and the inner energy as a function of p and T is:

$dQ=\left({\frac {\partial U}{\partial T}}\right)_{p}dT+\left({\frac {\partial U}{\partial p}}\right)_{T}dp+p\left[\left({\frac {\partial V}{\partial T}}\right)_{p}dT+\left({\frac {\partial V}{\partial p}}\right)_{T}dp\right]$

For constant pressure $(dp=0)$ the equation simplifies to:

$C_{p}=\left.{\frac {dQ}{dT}}\right|_{p={\text{const}}}=\left({\frac {\partial U}{\partial T}}\right)_{p}+p\left({\frac {\partial V}{\partial T}}\right)_{p}=\left({\frac {\partial H}{\partial T}}\right)_{p}$

where the final equality follows from the appropriate Maxwell relations, and is commonly used as the definition of the isobaric heat capacity.

#### At constant volume, *dV* = 0, *dQ* = *dU* (isochoric process)

A system undergoing a process at constant volume implies that no expansion work is done, so the heat supplied contributes only to the change in internal energy. The heat capacity obtained this way is denoted $C_{V}.$ The value of $C_{V}$ is always less than the value of $C_{p}$ . ( $C_{V}<C_{p}$ .)

Expressing the inner energy as a function of the variables T and V gives:

$dQ=\left({\frac {\partial U}{\partial T}}\right)_{V}dT+\left({\frac {\partial U}{\partial V}}\right)_{T}dV+pdV$

For a constant volume ( $dV=0$ ) the heat capacity reads:

$C_{V}=\left.{\frac {dQ}{dT}}\right|_{V={\text{const}}}=\left({\frac {\partial U}{\partial T}}\right)_{V}$

The relation between $C_{V}$ and $C_{p}$ is then:

$C_{p}=C_{V}+\left(\left({\frac {\partial U}{\partial V}}\right)_{T}+p\right)\left({\frac {\partial V}{\partial T}}\right)_{p}$

#### Calculating *Cp* and *CV* for an ideal gas

Mayer's relation:

$C_{p}-C_{V}=nR.$ $C_{p}/C_{V}=\gamma ,$

where:

- n is the number of moles of the gas,
- R is the universal gas constant,
- $\gamma$ is the heat capacity ratio (which can be calculated by knowing the number of degrees of freedom of the gas molecule).

Using the above two relations, the specific heats can be deduced as follows:

$C_{V}={\frac {nR}{\gamma -1}},$ $C_{p}=\gamma {\frac {nR}{\gamma -1}}.$ Following from the equipartition of energy, it is deduced that an ideal gas has the isochoric heat capacity

$C_{V}=nR{\frac {N_{f}}{2}}=nR{\frac {3+N_{i}}{2}}$

where $N_{f}$ is the number of degrees of freedom of each individual particle in the gas, and $N_{i}=N_{f}-3$ is the number of internal degrees of freedom, where the number 3 comes from the three translational degrees of freedom (for a gas in 3D space). This means that a monoatomic ideal gas (with zero internal degrees of freedom) will have isochoric heat capacity $C_{v}={\frac {3nR}{2}}$ .

#### At constant temperature (Isothermal process)

No change in internal energy (as the temperature of the system is constant throughout the process) leads to only work done by the total supplied heat, and thus an infinite amount of heat is required to increase the temperature of the system by a unit temperature, leading to infinite or undefined heat capacity of the system.

#### At the time of phase change (Phase transition)

Heat capacity of a system undergoing phase transition is infinite, because the heat is utilized in changing the state of the material rather than raising the overall temperature.

### Calculating changes in entropy using heat capacity

The change in entropy of a system is generally not easy to measure directly, and hence it is common to measure the isobaric and isochoric heat capacities as functions of temperature, which are much easier to measure, allowing the change in entropy to be calculated as follows:

Given an isochoric system, $C_{v}=\left({\frac {\partial U}{\partial T}}\right)_{N,V}$ , which can be rewritten as $\left.dU\right|_{N,V=const}=C_{v}dT$ .

where N is the particle number.

The fundamental thermodynamic relation $dU=TdS-pdV+\mu dN$ can be restricted to obtain $\left.dU\right|_{N,V=const}=TdS$

where:

- S is the entropy of the system
- $\mu$ is the chemical potential of the system

Hence $C_{v}dT=TdS$ and $dS={\frac {C_{v}}{T}}dT$ . Integrating both sides, keeping in mind that $C_{v}$ is a function of T , the following relation is obtained:

$S_{2}-S_{1}=\Delta S=\int _{T_{1}}^{T_{2}}{\frac {C_{v}(T)}{T}}dT$

where:

- $S_{1},T_{1}$ are the initial entropy and temperature respectively
- $S_{2},T_{2}$ are the final entropy and temperature respectively
- $\Delta S$ is the change in entropy of the system

Similarly, for an isobaric system, using $C_{p}=\left({\frac {\partial H}{\partial T}}\right)_{N,p}$ and $dH=TdS+Vdp+\mu dN$ , it can also be derived that

$\Delta S=\int _{T_{1}}^{T_{2}}{\frac {C_{p}(T)}{T}}dT$

### Heterogeneous objects

The heat capacity may be well-defined even for heterogeneous objects, with separate parts made of different materials; such as an electric motor, a crucible with some metal, or a whole building. In many cases, the (isobaric) heat capacity of such objects can be computed by simply adding together the (isobaric) heat capacities of the individual parts.

However, this computation is valid only when all parts of the object are at the same external pressure before and after the measurement. That may not be possible in some cases. For example, when heating an amount of gas in an elastic container, its volume *and pressure* will both increase, even if the atmospheric pressure outside the container is kept constant. Therefore, the effective heat capacity of the gas, in that situation, will have a value intermediate between its isobaric and isochoric capacities $C_{p}$ and $C_{V}$ .

For complex thermodynamic systems with several interacting parts and state variables, or for measurement conditions that are neither constant pressure nor constant volume, or for situations where the temperature is significantly non-uniform, the simple definitions of heat capacity above are not useful or even meaningful. The heat energy that is supplied may end up as kinetic energy (energy of motion) and potential energy (energy stored in force fields), both at macroscopic and atomic scales. Then the change in temperature will depend on the particular path that the system followed through its phase space between the initial and final states. Namely, one must somehow specify how the positions, velocities, pressures, volumes, etc. changed between the initial and final states; and use the general tools of thermodynamics to predict the system's reaction to a small energy input. The "constant volume" and "constant pressure" heating modes are just two among infinitely many paths that a simple homogeneous system can follow.

## Measurement

The heat capacity can usually be measured by the method implied by its definition: start with the object at a known uniform temperature, add a known amount of heat energy to it, wait for its temperature to become uniform, and measure the change in its temperature. This method can give moderately accurate values for many solids; however, it cannot provide very precise measurements, especially for gases.

## Units

### International system (SI)

The SI unit for heat capacity of an object is joule per kelvin (J/K or J⋅K−1). Since an increment of temperature of one degree Celsius is the same as an increment of one kelvin, that is the same unit as J/°C.

The heat capacity of an object is an amount of energy divided by a temperature change, which has the dimension L2⋅M⋅T−2⋅Θ−1. Therefore, the SI unit J/K is equivalent to kilogram meter squared per second squared per kelvin (kg⋅m2⋅s−2⋅K−1 ).

### English (Imperial) engineering units

Professionals in construction, civil engineering, chemical engineering, and other technical disciplines, especially in the United States, may use the so-called English Engineering units, that include the pound (lb = 0.45359237 kg) as the unit of mass, the degree Fahrenheit or Rankine (⁠5/9⁠K, about 0.55556 K) as the unit of temperature increment, and the British thermal unit (BTU ≈ 1055.06 J), as the unit of heat. In those contexts, the unit of heat capacity is 1 BTU/°R ≈ 1900 J/K. The BTU was in fact defined so that the average heat capacity of one pound of water would be 1 BTU/°F. In this regard, with respect to mass, note conversion of 1 Btu/lb⋅°R ≈ 4,187 J/kg⋅K and the calorie (below).

### Calories

In chemistry, heat amounts are often measured in calories. Confusingly, two units with that name, denoted "cal" or "Cal", have been commonly used to measure amounts of heat:

- The "small calorie" (or "gram-calorie", "cal") is exactly 4.184 J. It was originally defined so that the heat capacity of 1 gram of liquid water would be 1 cal/°C.
- The "grand calorie" (also "kilocalorie", "kilogram-calorie", or "food calorie"; "kcal" or "Cal") is 1000 cal, that is, exactly 4184 J. It was originally defined so that the heat capacity of 1 kg of water would be 1 kcal/°C.

With these units of heat energy, the units of heat capacity are

- 1 cal/°C = 4.184 J/K ;
- 1 kcal/°C = 4184 J/K.

## Physical basis

## Negative heat capacity

Most physical systems exhibit a positive heat capacity; constant-volume and constant-pressure heat capacities, rigorously defined as partial derivatives, are always positive for homogeneous bodies. However, even though it can seem paradoxical at first, there are some systems for which the heat capacity $Q/\Delta T$ is *negative*. Examples include a reversibly and nearly adiabatically expanding ideal gas, which cools, $\Delta T<0$ , while a small amount of heat $Q>0$ is put in, or combusting methane with increasing temperature, $\Delta T>0$ , and giving off heat, $Q<0$ . Others are inhomogeneous systems that do not meet the strict definition of thermodynamic equilibrium. They include gravitating objects such as stars and galaxies, and also some nano-scale clusters of a few tens of atoms close to a phase transition. A negative heat capacity can result in a negative temperature.

### Stars and black holes

According to the virial theorem, for a self-gravitating body like a star or an interstellar gas cloud, the average potential energy *U*pot and the average kinetic energy *U*kin are locked together in the relation

$U_{\text{pot}}=-2U_{\text{kin}}.$

The total energy *U* (= *U*pot + *U*kin) therefore obeys

$U=-U_{\text{kin}}.$

If the system loses energy, for example, by radiating energy into space, the average kinetic energy actually increases. If a temperature is defined by the average kinetic energy, then the system therefore can be said to have a negative heat capacity.

A more extreme version of this occurs with black holes. According to black-hole thermodynamics, the more mass and energy a black hole absorbs, the colder it becomes. In contrast, if it is a net emitter of energy, through Hawking radiation, it will become hotter and hotter until it boils away.

### Consequences

According to the second law of thermodynamics, when two systems with different temperatures interact via a purely thermal connection, heat will flow from the hotter system to the cooler one (this can also be understood from a statistical point of view). Therefore, if such systems have equal temperatures, they are at thermal equilibrium. However, this equilibrium is stable only if the systems have *positive* heat capacities. For such systems, when heat flows from a higher-temperature system to a lower-temperature one, the temperature of the first decreases and that of the latter increases, so that both approach equilibrium. In contrast, for systems with *negative* heat capacities, the temperature of the hotter system will further increase as it loses heat, and that of the colder will further decrease, so that they will move farther from equilibrium. This means that the equilibrium is unstable.

For example, according to theory, the smaller (less massive) a black hole is, the smaller its Schwarzschild radius will be, and therefore the greater the curvature of its event horizon will be, as well as its temperature. Thus, the smaller the black hole, the more thermal radiation it will emit and the more quickly it will evaporate by Hawking radiation.
