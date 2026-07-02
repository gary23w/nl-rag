---
title: "Microwave cavity"
source: https://en.wikipedia.org/wiki/Microwave_cavity
domain: cavity-resonators
license: CC-BY-SA-4.0
tags: microwave cavity, dielectric resonator, quality factor, helical resonator
fetched: 2026-07-02
---

# Microwave cavity

A **microwave cavity** or **radio frequency cavity** (**RF cavity**) is a special type of resonator, consisting of a closed (or largely closed) metal structure that confines electromagnetic fields in the microwave or RF region of the spectrum. The structure is either hollow or filled with dielectric material. The microwaves bounce back and forth between the walls of the cavity. At the cavity's resonant frequencies they reinforce to form standing waves in the cavity. Therefore, the cavity functions similarly to an organ pipe or sound box in a musical instrument, oscillating preferentially at a series of frequencies, its resonant frequencies. Thus it can act as a bandpass filter, allowing microwaves of a particular frequency to pass while blocking microwaves at nearby frequencies.

A microwave cavity acts similarly to a resonant circuit with extremely low loss at its frequency of operation, resulting in quality factors (Q factors) up to the order of 106, for copper cavities, compared to 102 for circuits made with separate inductors and capacitors at the same frequency. For superconducting cavities, quality factors up to the order of 1010 are possible. They are used in place of resonant circuits at microwave frequencies, since at these frequencies discrete resonant circuits cannot be built because the values of inductance and capacitance needed are too low. They are used in oscillators and transmitters to create microwave signals, as filters to separate a signal at a given frequency from other signals, wavemeter or frequency meter, Echo Box for pulsed radars to generate artificial targets and to measure the spectrum and transmit frequency, and in microwave relay stations, satellite communications, and microwave ovens.

RF cavities can also manipulate charged particles passing through them by application of acceleration voltage and are thus used in particle accelerators and microwave vacuum tubes such as klystrons and magnetrons.

## Theory of operation

Most resonant cavities are made from closed (or short-circuited) sections of waveguide or high-permittivity dielectric material (see dielectric resonator). Electric and magnetic energy is stored in the cavity. This energy decays over time due to several possible loss mechanisms.

The section on 'Physics of SRF cavities' in the article on superconducting radio frequency contains a number of important and useful expressions which apply to any microwave cavity:

The energy stored in the cavity is given by the integral of field energy density over its volume,

$U={\frac {\mu _{0}}{2}}\int {|{\overrightarrow {H}}|^{2}dV}$

,

where:

H

is the magnetic field in the cavity and

μ

0

is the permeability of free space.

The power dissipated due just to the resistivity of the cavity's walls is given by the integral of resistive wall losses over its surface,

$P_{d}={\frac {R_{s}}{2}}\int {|{\overrightarrow {H}}|^{2}dS}$

,

where:

R

s

is the surface resistance.

For copper cavities operating near room temperature, *Rs* is simply determined by the empirically measured bulk electrical conductivity *σ* see Ramo et al pp.288-289

$R_{s\ normal}={\sqrt {\frac {\omega \mu _{0}}{2\sigma }}}$

.

A resonator's quality factor is defined by

$Q_{o}={\frac {\omega U}{P_{d}}}$

,

where:

ω

is the resonant frequency in [rad/s],

U

is the energy stored in [J], and

P

d

is the power dissipated in [W] in the cavity to maintain the energy

U

.

Basic losses are due to finite conductivity of cavity walls and dielectric losses of material filling the cavity. Other loss mechanisms exist in evacuated cavities, for example the multipactor effect or field electron emission. Both multipactor effect and field electron emission generate copious electrons inside the cavity. These electrons are accelerated by the electric field in the cavity and thus extract energy from the stored energy of the cavity. Eventually the electrons strike the walls of the cavity and lose their energy. In superconducting radio frequency cavities there are additional energy loss mechanisms associated with the deterioration of the electric conductivity of the superconducting surface due to heating or contamination.

Every cavity has numerous resonant frequencies that correspond to electromagnetic field modes satisfying necessary boundary conditions on the walls of the cavity. Because of these boundary conditions that must be satisfied at resonance (tangential electric fields must be zero at cavity walls), at resonance, cavity dimensions must satisfy particular values. Depending on the resonance transverse mode, transverse cavity dimensions may be constrained to expressions related to geometric functions, or to zeros of Bessel functions or their derivatives (see below), depending on the symmetry properties of the cavity's shape. Alternately it follows that cavity length must be an integer multiple of half-wavelength at resonance (see page 451 of Ramo et al). In this case, a resonant cavity can be thought of as a resonance in a short circuited half-wavelength transmission line.

The external dimensions of a cavity can be made considerably smaller at its lowest frequency mode by loading the cavity with either capacitive or inductive elements. Loaded cavities usually have lower symmetries and compromise certain performance indicators, such as the best Q factor. As examples, the reentrant cavity and helical resonator are capacitive and inductive loaded cavities, respectively.

### Multi-cell cavity

Single-cell cavities can be combined in a structure to accelerate particles (such as electrons or ions) more efficiently than a string of independent single cell cavities. The figure from the U.S. Department of Energy shows a multi-cell superconducting cavity in a clean room at Fermi National Accelerator Laboratory.

### Loaded microwave cavities

A microwave cavity has a fundamental mode, which exhibits the lowest resonant frequency of all possible resonant modes. For example, the fundamental mode of a cylindrical cavity is the TM010 mode. For certain applications, there is motivation to reduce the dimensions of the cavity. This can be done by using a loaded cavity, where a capacitive or an inductive load is integrated in the cavity's structure.

The precise resonant frequency of a loaded cavity must be calculated using finite element methods for Maxwell's equations with boundary conditions.

Loaded cavities (or resonators) can also be configured as multi-cell cavities.

Loaded cavities are particularly suited for accelerating low velocity charged particles. This application for many types of loaded cavities. Some common types are:

- The reentrant cavity

- The helical resonator
- The spiral resonator

- The split-ring resonator
- The quarter wave resonator
- The half wave resonator. A variant of the half-wave resonator is the spoke resonator.

- The Radio-frequency quadrupole
- Compact Crab cavity. Compact crab cavities are an important upgrade for the LHC.

The Q factor of a particular mode in a resonant cavity can be calculated. For a cavity with high degrees of symmetry, using analytical expressions of the electric and magnetic field, surface currents in the conducting walls and electric field in dielectric lossy material. For cavities with arbitrary shapes, finite element methods for Maxwell's equations with boundary conditions must be used. Measurement of the Q of a cavity are done using a Vector Network analyzer (electrical), or in the case of a very high Q by measuring the exponential decay time $\tau$ of the fields, and using the relationship $Q=\pi f\tau$ .

The electromagnetic fields in the cavity are excited via external coupling. An external power source is usually coupled to the cavity by a small aperture, a small wire probe or a loop, see page 563 of Ramo et al. External coupling structure has an effect on cavity performance and needs to be considered in the overall analysis, see Montgomery et al page 232.

### Resonant frequencies

The resonant frequencies of a cavity are a function of its geometry.

#### Rectangular cavity

Resonance frequencies of a rectangular microwave cavity for any $\scriptstyle TE_{mnl}$ or $\scriptstyle TM_{mnl}$ resonant mode can be found by imposing boundary conditions on electromagnetic field expressions. This frequency is given at page 546 of Ramo et al:

| ${\begin{aligned}f_{mnl}&={\frac {c}{2\pi {\sqrt {\mu _{r}\epsilon _{r}}}}}\cdot k_{mnl}\\&={\frac {c}{2\pi {\sqrt {\mu _{r}\epsilon _{r}}}}}{\sqrt {\left({\frac {m\pi }{a}}\right)^{2}+\left({\frac {n\pi }{b}}\right)^{2}+\left({\frac {l\pi }{d}}\right)^{2}}}\\&={\frac {c}{2{\sqrt {\mu _{r}\epsilon _{r}}}}}{\sqrt {\left({\frac {m}{a}}\right)^{2}+\left({\frac {n}{b}}\right)^{2}+\left({\frac {l}{d}}\right)^{2}}}\end{aligned}}$ |   | 1 |
|---|---|---|

where $\scriptstyle k_{mnl}$ is the wavenumber, with $\scriptstyle m$ , $\scriptstyle n$ , $\scriptstyle l$ being the mode numbers and $\scriptstyle a$ , $\scriptstyle b$ , $\scriptstyle d$ being the corresponding dimensions; c is the speed of light in vacuum; and $\scriptstyle \mu _{r}$ and $\scriptstyle \epsilon _{r}$ are relative permeability and permittivity of the cavity filling respectively.

#### Cylindrical cavity

The field solutions of a cylindrical cavity of length $\scriptstyle L$ and radius $\scriptstyle R$ follow from the solutions of a cylindrical waveguide with additional electric boundary conditions at the position of the enclosing plates. The resonance frequencies are different for TE and TM modes.

**TM modes**

See Jackson

| $f_{mnp}={\frac {c}{2\pi {\sqrt {\mu _{r}\epsilon _{r}}}}}{\sqrt {\left({\frac {X_{mn}}{R}}\right)^{2}+\left({\frac {p\pi }{L}}\right)^{2}}}$ |   | 2a |
|---|---|---|

**TE modes**

See Jackson

| $f_{mnp}={\frac {c}{2\pi {\sqrt {\mu _{r}\epsilon _{r}}}}}{\sqrt {\left({\frac {X'_{mn}}{R}}\right)^{2}+\left({\frac {p\pi }{L}}\right)^{2}}}$ |   | 2b |
|---|---|---|

Here, $\scriptstyle X_{mn}$ denotes the $\scriptstyle n$ -th zero of the $\scriptstyle m$ -th Bessel function, and $\scriptstyle X'_{mn}$ denotes the $\scriptstyle n$ -th zero of the *derivative* of the $\scriptstyle m$ -th Bessel function. $\scriptstyle \mu _{r}$ and $\scriptstyle \epsilon _{r}$ are relative permeability and permittivity respectively.

### Quality factor

The quality factor $\scriptstyle Q$ of a cavity can be decomposed into three parts, representing different power loss mechanisms.

- $\scriptstyle Q_{c}$ , resulting from the power loss in the walls which have finite conductivity. The Q of the lowest frequency mode, or "fundamental mode" are calculated, see pp. 541-551 in Ramo et al for a rectangular cavity (Equation 3a) with dimensions $a,b,d$ and parameters $l=1,m=0,n=0$ , and the $TM_{010}$ mode of a cylindrical cavity (Equation 3b) with parameters $m=0,n=1,p=0$ as defined above.

| $Q_{c}={\frac {\pi \eta }{4R_{s}}}\cdot {\frac {2b\left(a^{2}+d^{2}\right)^{1.5}}{ad\left(a^{2}+d^{2}\right)+2b\left(a^{3}+d^{3}\right)}},$ |   | 3a |
|---|---|---|

| $Q_{c}={\frac {\eta }{2R_{s}}}\cdot {\frac {X_{01}}{{\frac {a}{d}}+1}},$ |   | 3b |
|---|---|---|

where $\scriptstyle \eta$ is the intrinsic impedance of the dielectric, $\scriptstyle R_{s}$ is the surface resistivity of the cavity walls. Note that $X_{01}\approx 2.405$ .

- $\scriptstyle Q_{d}$ , resulting from the power loss in the lossy dielectric material filling the cavity, where $\scriptstyle \tan \delta$ is the loss tangent of the dielectric

| $Q_{d}={\frac {1}{\tan \delta }}\,$ |   | 4 |
|---|---|---|

- $\scriptstyle Q_{ext}$ , resulting from power loss through unclosed surfaces (holes) of the cavity geometry.

Total Q factor of the cavity can be found as in page 567 of Ramo et al

| $Q=\left({\frac {1}{Q_{c}}}+{\frac {1}{Q_{d}}}+{\frac {1}{Q_{ext}}}\right)^{-1}\,$ |   | 5 |
|---|---|---|

## Comparison to LC circuits

Microwave resonant cavities can be represented and thought of as simple LC circuits, see Montgomery et al pages 207-239. For a microwave cavity, the stored electric energy is equal to the stored magnetic energy at resonance as is the case for a resonant LC circuit. In terms of inductance and capacitance, the resonant frequency for a given $\scriptstyle mnl$ mode can be written as given in Montgomery et al page 209

| $L_{mnl}=\mu k_{mnl}^{2}V\,$ |   | 6 |
|---|---|---|

| $C_{mnl}={\frac {\epsilon }{k_{mnl}^{4}V}}\,$ |   | 7 |
|---|---|---|

| ${\begin{aligned}f_{mnl}&={\frac {1}{2\pi {\sqrt {L_{mnl}C_{mnl}}}}}\\&={\frac {1}{2\pi {\sqrt {{\frac {1}{k_{mnl}^{2}}}\mu \epsilon }}}}\end{aligned}}$ |   | 8 |
|---|---|---|

where V is the cavity volume, $\scriptstyle k_{mnl}$ is the mode wavenumber and $\scriptstyle \epsilon$ and $\scriptstyle \mu$ are permittivity and permeability respectively.

To better understand the utility of resonant cavities at microwave frequencies, it is useful to note that conventional inductors and capacitors start to become impractically small with frequency in the VHF, and definitely so for frequencies above one gigahertz. Because of their low losses and high Q factors, cavity resonators are preferred over conventional LC and transmission-line resonators at high frequencies.

### Losses in LC resonant circuits

Conventional inductors are usually wound from wire in the shape of a helix with no core. Skin effect causes the high frequency resistance of inductors to be many times their direct current resistance. In addition, capacitance between turns causes dielectric losses in the insulation which coats the wires. These effects make the high frequency resistance greater and decrease the Q factor.

Conventional capacitors use air, mica, ceramic or perhaps teflon for a dielectric. Even with a low loss dielectric, capacitors are also subject to skin effect losses in their leads and plates. Both effects increase their equivalent series resistance and reduce their Q.

Even if the Q factor of VHF inductors and capacitors is high enough to be useful, their parasitic properties can significantly affect their performance in this frequency range. The shunt capacitance of an inductor may be more significant than its desirable series inductance. The series inductance of a capacitor may be more significant than its desirable shunt capacitance. As a result, in the VHF or microwave regions, a capacitor may appear to be an inductor and an inductor may appear to be a capacitor. These phenomena are better known as parasitic inductance and parasitic capacitance.

### Losses in cavity resonators

Dielectric loss of air is extremely low for high-frequency electric or magnetic fields. Air-filled microwave cavities confine electric and magnetic fields to the air spaces between their walls. Electric losses in such cavities are almost exclusively due to currents flowing in cavity walls. While losses from wall currents are small, cavities are frequently plated with silver to increase their electrical conductivity and reduce these losses even further. Copper cavities frequently oxidize, which increases their loss. Silver or gold plating prevents oxidation and reduces electrical losses in cavity walls. Even though gold is not quite as good a conductor as copper, it still prevents oxidation and the resulting deterioration of Q factor over time. However, because of its high cost, it is used only in the most demanding applications.

Some satellite resonators are silver-plated and covered with a gold flash layer. The current then mostly flows in the high-conductivity silver layer, while the gold flash layer protects the silver layer from oxidizing.
