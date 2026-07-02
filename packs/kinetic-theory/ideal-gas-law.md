---
title: "Ideal gas law"
source: https://en.wikipedia.org/wiki/Ideal_gas_law
domain: kinetic-theory
license: CC-BY-SA-4.0
tags: kinetic theory of gases, mean free path, boltzmann equation, ideal gas law
fetched: 2026-07-02
---

# Ideal gas law

The **ideal gas law**, also called the **general gas equation**, is the equation of state of a hypothetical ideal gas. It is a good approximation of the behavior of many gases under many conditions, although it has several limitations. It was first stated by Benoît Paul Émile Clapeyron and independently of him, Dmitry Mendeleev in 1834 as a combination of the empirical Boyle's law, Charles's law, Avogadro's law, and Gay-Lussac's law. The ideal gas law is often written in an empirical form:

$pV=nRT$ where p, V, and T are respectively the pressure, volume, and temperature, n is the amount of substance, and R is the ideal gas constant. It can also be derived from the microscopic kinetic theory, as was achieved (independently) by August Krönig in 1856 and Rudolf Clausius in 1857.

## Formulations

The state of an amount of gas is determined by its pressure, volume, and temperature. The modern form of the equation relates these simply in two main forms. The temperature used in the equation of state is an absolute temperature: the appropriate SI unit is the kelvin.

### Common forms

The most frequently introduced forms are: $pV=nRT=nk_{\text{B}}N_{\text{A}}T=Nk_{\text{B}}T$ where:

- p is the absolute pressure of the gas,
- V is the volume of the gas,
- n is the amount of substance of gas (also known as number of moles),
- R is the ideal, or universal, gas constant, equal to the product of the Boltzmann constant and the Avogadro constant,
- $k_{\text{B}}$ is the Boltzmann constant,
- ***$N_{A}$*** is the Avogadro constant,
- T is the absolute temperature of the gas,
- N is the number of particles (usually atoms or molecules) of the gas.

In SI units, *p* is measured in pascals, *V* is measured in cubic meters, *n* is measured in moles, and *T* in kelvins (the Kelvin scale is a shifted Celsius scale, where 0 K = −273.15 °C, the lowest possible temperature). *R* has for value 8.314 J/(mol·K) = 1.989 ≈ 2 cal/(mol·K), or 0.0821 L⋅atm/(mol⋅K).

### Molar form

How much gas is present could be specified by giving the mass instead of the chemical amount of gas. Therefore, an alternative form of the ideal gas law may be useful. The chemical amount, *n* (in moles), is equal to total mass of the gas (*m*) (in kilograms) divided by the molar mass, *M* (in kilograms per mole):

$n={\frac {m}{M}}.$

By replacing *n* with *m*/*M* and subsequently introducing density *ρ* = *m*/*V*, we get:

$pV={\frac {m}{M}}RT$

$p={\frac {m}{V}}{\frac {RT}{M}}$

$p=\rho {\frac {R}{M}}T$

Defining the specific gas constant *R*specific as the ratio *R*/*M*,

$p=\rho R_{\text{specific}}T.$

This form of the ideal gas law is very useful because it links pressure, density, and temperature in a unique formula independent of the quantity of the considered gas. Alternatively, the law may be written in terms of the specific volume *v*, the reciprocal of density, as

$pv=R_{\text{specific}}T.$

It is common, especially in engineering and meteorological applications, to represent the **specific** gas constant by the symbol *R*. In such cases, the **universal** gas constant is usually given a different symbol such as ${\bar {R}}$ or $R^{*}$ to distinguish it. In any case, the context and/or units of the gas constant should make it clear as to whether the universal or specific gas constant is being used.

### Statistical mechanics

In statistical mechanics, the following molecular equation (i.e. the ideal gas law in its theoretical form) is derived from first principles:

$p=nk_{\text{B}}T,$

where *p* is the absolute pressure of the gas, *n* is the number density of the molecules (given by the ratio *n* = *N*/*V*, in contrast to the previous formulation in which *n* is the *number of moles*), *T* is the absolute temperature, and *k*B is the Boltzmann constant relating temperature and energy, given by:

$k_{\text{B}}={\frac {R}{N_{\text{A}}}}$

where *N*A is the Avogadro constant. The form can be further simplified by defining the kinetic energy corresponding to the temperature:

$T:=k_{\text{B}}T,$

so the ideal gas law is more simply expressed as:

$p=n\,T.$

From this we notice that for a gas of mass *m*, with an average particle mass of *μ* times the atomic mass constant, *m*u, (i.e., the mass is *μ* Da) the number of molecules will be given by

$N={\frac {m}{\mu m_{\text{u}}}},$

and since *ρ* = *m*/*V* = *nμm*u, we find that the ideal gas law can be rewritten as

$p={\frac {1}{V}}{\frac {m}{\mu m_{\text{u}}}}k_{\text{B}}T={\frac {k_{\text{B}}}{\mu m_{\text{u}}}}\rho T.$

In SI units, *p* is measured in pascals, *V* in cubic metres, *T* in kelvins, and *k*B = 1.38×10−23 J⋅K−1 in SI units.

### Combined gas law

Combining the laws of Charles, Boyle, and Gay-Lussac gives the **combined gas law**, which can take the same functional form as the ideal gas law. This form does not specify the number of moles, and the ratio of $PV$ to T is simply taken as a constant:

${\frac {PV}{T}}=k,$

where P is the pressure of the gas, V is the volume of the gas, T is the absolute temperature of the gas, and k is a constant. More commonly, when comparing the same substance under two different sets of conditions, the law is written as:

${\frac {P_{1}V_{1}}{T_{1}}}={\frac {P_{2}V_{2}}{T_{2}}}.$

## Energy associated with a gas

According to the assumptions of the kinetic theory of ideal gases, one can consider that there are no intermolecular attractions between the molecules, or atoms, of an ideal gas. In other words, its potential energy is zero. Hence, all the energy possessed by the gas is the kinetic energy of the molecules, or atoms, of the gas.

$E={\frac {3}{2}}nRT$

This corresponds to the kinetic energy of *n* moles of a monoatomic gas having 3 degrees of freedom: *x*, *y*, *z*. The table here below gives this relationship for different amounts of a monoatomic gas.

| Energy of a monoatomic gas | Mathematical expression |
|---|---|
| Energy associated with one mole | $E={\frac {3}{2}}RT$ |
| Energy associated with one gram | $E={\frac {3}{2}}rT$ |
| Energy associated with one atom | $E={\frac {3}{2}}k_{\rm {B}}T$ |

## Applications to thermodynamic processes

The table below essentially simplifies the ideal gas equation for a particular process, making the equation easier to solve using numerical methods.

A thermodynamic process is defined as a system that moves from state 1 to state 2, where the state number is denoted by a subscript. As shown in the first column of the table, basic thermodynamic processes are defined such that one of the gas properties (*P*, *V*, *T*, *S*, or *H*) is constant throughout the process.

For a given thermodynamic process, in order to specify the extent of a particular process, one of the properties ratios (which are listed under the column labeled "known ratio") must be specified (either directly or indirectly). Also, the property for which the ratio is known must be distinct from the property held constant in the previous column (otherwise the ratio would be unity, and not enough information would be available to simplify the gas law equation).

In the final three columns, the properties (*p*, *V*, or *T*) at state 2 can be calculated from the properties at state 1 using the equations listed.

| Process | Constant | Known ratio or delta | p2 | V2 | T2 |
|---|---|---|---|---|---|
| Isobaric process | Pressure | V2/V1 | p2 = p1 | V2 = V1(V2/V1) | T2 = T1(V2/V1) |
| T2/T1 | p2 = p1 | V2 = V1(T2/T1) | T2 = T1(T2/T1) |   |   |
| Isochoric process (Isovolumetric process) (Isometric process) | Volume | p2/p1 | p2 = p1(p2/p1) | V2 = V1 | T2 = T1(p2/p1) |
| T2/T1 | p2 = p1(T2/T1) | V2 = V1 | T2 = T1(T2/T1) |   |   |
| Isothermal process | Temperature | p2/p1 | p2 = p1(p2/p1) | V2 = V1(p1/p2) | T2 = T1 |
| V2/V1 | p2 = p1(V1/V2) | V2 = V1(V2/V1) | T2 = T1 |   |   |
| Isentropic process (Reversible adiabatic process) | Entropy[a] | p2/p1 | p2 = p1(p2/p1) | V2 = V1(p2/p1)(−1/γ) | T2 = T1(p2/p1)(γ − 1)/γ |
| V2/V1 | p2 = p1(V2/V1)−γ | V2 = V1(V2/V1) | T2 = T1(V2/V1)(1 − γ) |   |   |
| T2/T1 | p2 = p1(T2/T1)γ/(γ − 1) | V2 = V1(T2/T1)1/(1 − γ) | T2 = T1(T2/T1) |   |   |
| Polytropic process | P V*n* | p2/p1 | p2 = p1(p2/p1) | V2 = V1(p2/p1)(−1/*n*) | T2 = T1(p2/p1)(*n* − 1)/*n* |
| V2/V1 | p2 = p1(V2/V1)−*n* | V2 = V1(V2/V1) | T2 = T1(V2/V1)(1 − *n*) |   |   |
| T2/T1 | p2 = p1(T2/T1)*n*/(*n* − 1) | V2 = V1(T2/T1)1/(1 − *n*) | T2 = T1(T2/T1) |   |   |
| Isenthalpic process (Irreversible adiabatic process) | Enthalpy[b] | p2 − p1 | p2 = p1 + (p2 − p1) |   | T2 = T1 + μJT(p2 − p1) |
| T2 − T1 | p2 = p1 + (T2 − T1)/μJT |   | T2 = T1 + (T2 − T1) |   |   |

**^** **a.** In an isentropic process, system entropy (*S*) is constant. Under these conditions, *p*1*V*1*γ* = *p*2*V*2*γ*, where *γ* is defined as the heat capacity ratio, which is constant for a calorifically perfect gas. The value used for *γ* is typically 1.4 for diatomic gases like nitrogen (N2) and oxygen (O2), (and air, which is 99% diatomic). Also *γ* is typically 1.6 for mono atomic gases like the noble gases helium (He), and argon (Ar). In internal combustion engines *γ* varies between 1.35 and 1.15, depending on constitution gases and temperature.

**^** **b.** In an isenthalpic process, system enthalpy (*H*) is constant. In the case of free expansion for an ideal gas, there are no molecular interactions, and the temperature remains constant. For real gases, the molecules do interact via attraction or repulsion depending on temperature and pressure, and heating or cooling does occur. This is known as the Joule–Thomson effect. For reference, the Joule–Thomson coefficient μJT for air at room temperature and sea level is 0.22 °C/bar.

## Deviations from ideal behavior of real gases

The equation of state given here (*PV* = *nRT*) applies only to an ideal gas, or as an approximation to a real gas that behaves sufficiently like an ideal gas. There are in fact many different forms of the equation of state. Since the ideal gas law neglects both molecular size and intermolecular attractions, it is most accurate for monatomic gases at high temperatures and low pressures. The molecular size becomes less important for lower densities, i.e. for larger volumes at lower pressures, because the average distance between adjacent molecules becomes much larger than the molecular size. The relative importance of intermolecular attractions diminishes with increasing thermal kinetic energy, i.e., with increasing temperatures. More detailed *equations of state*, such as the van der Waals equation, account for deviations from ideality caused by molecular size and intermolecular forces.

## Derivations

### Empirical

The empirical laws that led to the derivation of the ideal gas law were discovered with experiments that changed only 2 state variables of the gas and kept every other one constant.

All the possible gas laws that could have been discovered with this kind of setup are:

- Boyle's law (Equation 1) $PV=C_{1}\quad {\text{or}}\quad P_{1}V_{1}=P_{2}V_{2}$
- Charles's law (Equation 2) ${\frac {V}{T}}=C_{2}\quad {\text{or}}\quad {\frac {V_{1}}{T_{1}}}={\frac {V_{2}}{T_{2}}}$
- Avogadro's law (Equation 3) ${\frac {V}{N}}=C_{3}\quad {\text{or}}\quad {\frac {V_{1}}{N_{1}}}={\frac {V_{2}}{N_{2}}}$
- Gay-Lussac's law (Equation 4) ${\frac {P}{T}}=C_{4}\quad {\text{or}}\quad {\frac {P_{1}}{T_{1}}}={\frac {P_{2}}{T_{2}}}$
- Equation 5 $NT=C_{5}\quad {\text{or}}\quad N_{1}T_{1}=N_{2}T_{2}$
- Equation 6 ${\frac {P}{N}}=C_{6}\quad {\text{or}}\quad {\frac {P_{1}}{N_{1}}}={\frac {P_{2}}{N_{2}}}$

where *P* stands for pressure, *V* for volume, *N* for number of particles in the gas and *T* for temperature; where $C_{1},C_{2},C_{3},C_{4},C_{5},C_{6}$ are constants in this context because of each equation requiring only the parameters explicitly noted in them changing.

To derive the ideal gas law one does not need to know all 6 formulas, one can just know 3 and with those derive the rest or just one more to be able to get the ideal gas law, which needs 4.

Since each formula only holds when only the state variables involved in said formula change while the others (which are a property of the gas but are not explicitly noted in said formula) remain constant, we cannot simply use algebra and directly combine them all. This is why: Boyle did his experiments while keeping *N* and *T* constant and this must be taken into account (in this same way, every experiment kept some parameter as constant and this must be taken into account for the derivation).

Keeping this in mind, to carry the derivation on correctly, one must imagine the gas being altered by one process at a time (as it was done in the experiments). The derivation using 4 formulas can look like this:

at first the gas has parameters $P_{1},V_{1},N_{1},T_{1}.$

Say, starting to change only pressure and volume, according to Boyle's law (**Equation 1**), then:

| $P_{1}V_{1}=P_{2}V_{2}.$ |   | 7 |
|---|---|---|

After this process, the gas has parameters $P_{2},V_{2},N_{1},T_{1}.$

Using then equation (**5**) to change the number of particles in the gas and the temperature,

| $N_{1}T_{1}=N_{2}T_{2}.$ |   | 8 |
|---|---|---|

After this process, the gas has parameters $P_{2},V_{2},N_{2},T_{2}.$

Using then equation (**6**) to change the pressure and the number of particles,

| ${\frac {P_{2}}{N_{2}}}={\frac {P_{3}}{N_{3}}}.$ |   | 9 |
|---|---|---|

After this process, the gas has parameters $P_{3},V_{2},N_{3},T_{2}.$

Using then Charles's law (equation 2) to change the volume and temperature of the gas,

| ${\frac {V_{2}}{T_{2}}}={\frac {V_{3}}{T_{3}}}.$ |   | 10 |
|---|---|---|

After this process, the gas has parameters $P_{3},V_{3},N_{3},T_{3}$

Using simple algebra on equations (**7**), (**8**), (**9**) and (**10**) yields the result: ${\frac {P_{1}V_{1}}{N_{1}T_{1}}}={\frac {P_{3}V_{3}}{N_{3}T_{3}}}$ or ${\frac {PV}{NT}}=k_{\text{B}},$ where $k_{\text{B}}$ stands for the Boltzmann constant.

Another equivalent result, using the fact that $nR=Nk_{\text{B}}$ , where *n* is the number of moles in the gas and *R* is the universal gas constant, is: $PV=nRT,$ which is known as the ideal gas law.

If three of the six equations are known, it may be possible to derive the remaining three using the same method. However, because each formula has two variables, this is possible only for certain groups of three. For example, if you were to have equations (**1**), (**2**) and (**4**) you would not be able to get any more because combining any two of them will only give you the third. However, if you had equations (**1**), (**2**) and (**3**) you would be able to get all six equations because combining (**1**) and (**2**) will yield (**4**), then (**1**) and (**3**) will yield (**6**), then (**4**) and (**6**) will yield (**5**), as well as would the combination of (**2**) and (**3**) as is explained in the following visual relation:

where the numbers represent the gas laws numbered above.

If you were to use the same method used above on 2 of the 3 laws on the vertices of one triangle that has a "O" inside it, you would get the third.

For example:

Change only pressure and volume first:

| $P_{1}V_{1}=P_{2}V_{2},$ |   | 1' |
|---|---|---|

then only volume and temperature:

| ${\frac {V_{2}}{T_{1}}}={\frac {V_{3}}{T_{2}}},$ |   | 2' |
|---|---|---|

then as we can choose any value for $V_{3}$ , if we set $V_{1}=V_{3}$ , equation (**2'**) becomes:

| ${\frac {V_{2}}{T_{1}}}={\frac {V_{1}}{T_{2}}}.$ |   | 3' |
|---|---|---|

Combining equations (**1'**) and (**3'**) yields ${\frac {P_{1}}{T_{1}}}={\frac {P_{2}}{T_{2}}}$ , which is equation (**4**), of which we had no prior knowledge until this derivation.

### Theoretical

#### Kinetic theory

The ideal gas law can also be derived from first principles using the kinetic theory of gases, in which several simplifying assumptions are made, chief among which are that the molecules, or atoms, of the gas are point masses, possessing mass but no significant volume, and undergo only elastic collisions with each other and the sides of the container in which both linear momentum and kinetic energy are conserved.

First we show that the fundamental assumptions of the kinetic theory of gases, that total momentum gets equally applied, so (1/3) in each direction, imply that

$P={\frac {1}{3}}nmv_{\text{rms}}^{2}.$

Consider a container in the $xyz$ Cartesian coordinate system. For simplicity, we assume that a third of the molecules moves parallel to the x -axis, a third moves parallel to the y -axis and a third moves parallel to the z -axis. If all molecules move with the same velocity v , denote the corresponding pressure by $P_{0}$ . We choose an area S on a wall of the container, perpendicular to the x -axis. When time t elapses, all molecules in the volume $vtS$ moving in the positive direction of the x -axis will hit the area. There are $NvtS$ molecules in a part of volume $vtS$ of the container, but only one sixth (i.e. a half of a third) of them moves in the positive direction of the x -axis. Therefore, the number of molecules $N'$ that will hit the area S when the time t elapses is $NvtS/6$ .

When a molecule bounces off the wall of the container, it changes its momentum $\mathbf {p} _{1}$ to $\mathbf {p} _{2}=-\mathbf {p} _{1}$ . Hence the magnitude of change of the momentum of one molecule is $|\mathbf {p} _{2}-\mathbf {p} _{1}|=2mv$ . The magnitude of the change of momentum of all molecules that bounce off the area S when time t elapses is then $|\Delta \mathbf {p} |=2mvN'/V=NtSmv^{2}/(3V)=ntSmv^{2}/3$ . From $F=|\Delta \mathbf {p} |/t$ and $P_{0}=F/S$ we get

$P_{0}={\frac {1}{3}}nmv^{2}.$

We considered a situation where all molecules move with the same velocity v . Now we consider a situation where they can move with different velocities, so we apply an "averaging transformation" to the above equation, effectively replacing $P_{0}$ by a new pressure P and $v^{2}$ by the arithmetic mean of all squares of all velocities of the molecules, i.e. by $v_{\text{rms}}^{2}.$ Therefore

$P={\frac {1}{3}}nmv_{\text{rms}}^{2}$

which gives the desired formula.

Using the Maxwell–Boltzmann distribution, the fraction of molecules that have a speed in the range v to $v+dv$ is $f(v)\,dv$ , where

$f(v)=4\pi \left({\frac {m}{2\pi k_{\rm {B}}T}}\right)^{\!{\frac {3}{2}}}v^{2}e^{-{\frac {mv^{2}}{2k_{\rm {B}}T}}}$

and k denotes the Boltzmann constant. The root-mean-square speed can be calculated by

$v_{\text{rms}}^{2}=\int _{0}^{\infty }v^{2}f(v)\,dv=4\pi \left({\frac {m}{2\pi k_{\rm {B}}T}}\right)^{\frac {3}{2}}\int _{0}^{\infty }v^{4}e^{-{\frac {mv^{2}}{2k_{\rm {B}}T}}}\,dv.$

Using the integration formula

$\int _{0}^{\infty }x^{2n}e^{-{\frac {x^{2}}{a^{2}}}}\,dx={\sqrt {\pi }}\,{\frac {(2n)!}{n!}}\left({\frac {a}{2}}\right)^{2n+1},\quad n\in \mathbb {N} ,\,a\in \mathbb {R} ^{+},$

it follows that

$v_{\text{rms}}^{2}=4\pi \left({\frac {m}{2\pi k_{\rm {B}}T}}\right)^{\!{\frac {3}{2}}}{\sqrt {\pi }}\,{\frac {4!}{2!}}\left({\frac {\sqrt {\frac {2k_{\rm {B}}T}{m}}}{2}}\right)^{\!5}={\frac {3k_{\rm {B}}T}{m}},$

from which we get the ideal gas law:

$P={\frac {1}{3}}nm\left({\frac {3k_{\rm {B}}T}{m}}\right)=nk_{\rm {B}}T.$

#### Statistical mechanics

Let **q** = (*q*x, *q*y, *q*z) and **p** = (*p*x, *p*y, *p*z) denote the position vector and momentum vector of a particle of an ideal gas, respectively. Let **F** denote the net force on that particle. Then (two times) the time-averaged kinetic energy of the particle is:

${\begin{aligned}\langle \mathbf {q} \cdot \mathbf {F} \rangle &=\left\langle q_{x}{\frac {dp_{x}}{dt}}\right\rangle +\left\langle q_{y}{\frac {dp_{y}}{dt}}\right\rangle +\left\langle q_{z}{\frac {dp_{z}}{dt}}\right\rangle \\&=-\left\langle q_{x}{\frac {\partial H}{\partial q_{x}}}\right\rangle -\left\langle q_{y}{\frac {\partial H}{\partial q_{y}}}\right\rangle -\left\langle q_{z}{\frac {\partial H}{\partial q_{z}}}\right\rangle =-3k_{\text{B}}T,\end{aligned}}$

where the first equality is Newton's second law, and the second line uses Hamilton's equations and the equipartition theorem. Summing over a system of *N* particles yields

$3Nk_{\rm {B}}T=-\left\langle \sum _{k=1}^{N}\mathbf {q} _{k}\cdot \mathbf {F} _{k}\right\rangle .$

By Newton's third law and the ideal gas assumption, the net force of the system is the force applied by the walls of the container, and this force is given by the pressure *P* of the gas. Hence

$-\left\langle \sum _{k=1}^{N}\mathbf {q} _{k}\cdot \mathbf {F} _{k}\right\rangle =P\oint _{\text{surface}}\mathbf {q} \cdot d\mathbf {S} ,$

where d**S** is the infinitesimal area element along the walls of the container. Since the divergence of the position vector **q** is

$\nabla \cdot \mathbf {q} ={\frac {\partial q_{x}}{\partial q_{x}}}+{\frac {\partial q_{y}}{\partial q_{y}}}+{\frac {\partial q_{z}}{\partial q_{z}}}=3,$

the divergence theorem implies that

$P\oint _{\text{surface}}\mathbf {q} \cdot d\mathbf {S} =P\int _{\text{volume}}\left(\nabla \cdot \mathbf {q} \right)dV=3PV,$

where *dV* is an infinitesimal volume within the container and *V* is the total volume of the container.

Putting these equalities together yields

$3Nk_{\text{B}}T=-\left\langle \sum _{k=1}^{N}\mathbf {q} _{k}\cdot \mathbf {F} _{k}\right\rangle =3PV,$

which immediately implies the ideal gas law for *N* particles:

$PV=Nk_{\rm {B}}T=nRT,$

where *n* = *N*/*N*A is the number of moles of gas and *R* = *N*A*k*B is the gas constant.

#### Quantum mechanics

An additional derivation is possible using the particle in a box model of quantum mechanics. In a rectangular box of dimensions $a\times b\times c$ , the possible quantized energy levels are given as

$E=E_{x}+E_{y}+E_{z}={\frac {{n_{x}}^{2}{h^{2}}}{8m{a^{2}}}}+{\frac {{n_{y}}^{2}{h^{2}}}{8m{b^{2}}}}+{\frac {{n_{z}}^{2}{h^{2}}}{8m{c^{2}}}},$

where $n_{x}$ , $n_{y}$ and $n_{z}$ are the quantum numbers for translational motion in the three base directions, $E_{x}$ , $E_{y}$ and $E_{z}$ are the kinetic energies associated with translational motion in these directions. The force ( F ) acting upon the wall perpendicular to direction a is calculated as the derivative of the particle energy with respect to a change in side length a

$F={\frac {{\rm {d}}E}{{\rm {d}}a}}=-{\frac {2{n_{x}}^{2}{h^{2}}}{8m{a^{3}}}}=-{\frac {2{E_{x}}}{a}}.$

The overall force is calculated as the sum of the contributions from N independent particles as

$F=\sum \limits _{i=1}^{N}{\frac {-2{E_{x}}\left(i\right)}{a}}=-{\frac {2}{a}}\sum \limits _{i=1}^{N}{{E_{x}}\left(i\right)}.$

Then the equipartition theorem is used to give the average value of $E_{x}$ as

${\frac {1}{N}}\sum \limits _{i=1}^{N}{{E_{x}}\left(i\right)}={\frac {1}{2}}k_{\text{B}}T.$

Finally, pressure P is calculated as the ratio of the force and the area it acts upon:

$P={\frac {\left|F\right|}{bc}}={\frac {{\frac {2}{a}}\sum \limits _{i=1}^{N}{{E_{x}}\left(i\right)}}{bc}}={\frac {k_{\text{B}}TN}{V}}.$

Analogs of this derivation for cylindrical and spherical boxes give the same result.

## Other dimensions

In a *d*-dimensional space, the ideal gas pressure is:

$P^{(d)}={\frac {Nk_{\rm {B}}T}{L^{d}}},$

where $L^{d}$ is the extent of the *d*-dimensional domain in which the gas exists. The quantity dimension of the pressure-like quantity $P^{(d)}$ changes with the space dimensionality *d*: it corresponds to a force per length (for *d*=1), force per area (*d*=2), or force per volume (*d*=3).
