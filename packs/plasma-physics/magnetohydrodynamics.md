---
title: "Magnetohydrodynamics"
source: https://en.wikipedia.org/wiki/Magnetohydrodynamics
domain: plasma-physics
license: CC-BY-SA-4.0
tags: plasma physics, magnetohydrodynamics simulation, debye length, plasma oscillation
fetched: 2026-07-02
---

# Magnetohydrodynamics

**Magnetohydrodynamics** (**MHD**; also called **magnetofluid dynamics** or **hydro­magnetics**) is a model of electrically conducting fluids that treats all types of charged particles together as a single continuous fluid. It is primarily concerned with the low-frequency, large-scale magnetic behavior of plasmas and liquid metals and has applications in multiple fields, including space physics, geophysics, astrophysics, and engineering.

## Etymology

The word *magnetohydrodynamics* is derived from **magneto-**, meaning magnetic field; **hydro-**, meaning water; and **dynamics**, meaning movement. The field of MHD was initiated by Hannes Alfvén, who received the Nobel Prize in Physics in 1970 for his work in the field.

## History

The MHD description of electrically conducting fluids was first developed by Hannes Alfvén in a 1942 paper published in *Nature* titled "Existence of Electromagnetic–Hydrodynamic Waves", which outlined his discovery of what are now known as *Alfvén waves*. Alfvén initially referred to these waves as "electromagnetic–hydrodynamic waves"; however, in a later paper, he noted, "As the term 'electromagnetic–hydrodynamic waves' is somewhat complicated, it may be convenient to call this phenomenon 'magneto–hydrodynamic' waves."

## Equations

In MHD, motion in the fluid is described using linear combinations of the mean motions of the individual species: the current density $\mathbf {J}$ and the center-of-mass velocity ⁠ $\mathbf {v}$ ⁠. In a given fluid, each species $\sigma$ has a number density ⁠ $n_{\sigma }$ ⁠, mass ⁠ $m_{\sigma }$ ⁠, electric charge ⁠ $q_{\sigma }$ ⁠, and mean velocity ⁠ $\mathbf {u} _{\sigma }$ ⁠. The fluid's total mass density is then ⁠ $\textstyle \rho =\sum _{\sigma }m_{\sigma }n_{\sigma }$ ⁠, and the fluid's motion can be described by the current density expressed as $\mathbf {J} =\sum _{\sigma }n_{\sigma }q_{\sigma }\mathbf {u} _{\sigma }$ and the center of mass velocity expressed as: $\mathbf {v} ={\frac {1}{\rho }}\sum _{\sigma }m_{\sigma }n_{\sigma }\mathbf {u} _{\sigma }.$

MHD can be described by a set of equations consisting of a continuity equation, an equation of motion (the Cauchy momentum equation), an equation of state, Ampère's law, Faraday's law, and Ohm's law. As with any fluid description of a kinetic system, a closure approximation must be applied to the highest moment of the particle distribution equation. This is often accomplished through approximations to the heat flux under conditions of adiabaticity or isothermality.

In the adiabatic limit, that is, under the assumption of an isotropic pressure p and isotropic temperature, a fluid with adiabatic index ⁠ $\gamma$ ⁠, electrical resistivity ⁠ $\eta$ ⁠, magnetic field ⁠ $\mathbf {B}$ ⁠, and electric field $\mathbf {E}$ can be described by the continuity equation ${\frac {\partial \rho }{\partial t}}+\nabla \cdot \left(\rho \mathbf {v} \right)=0,$ the equation of state ${\frac {\mathrm {d} }{\mathrm {d} t}}\left({\frac {p}{\rho ^{\gamma }}}\right)=0,$ the equation of motion $\rho \left({\frac {\partial }{\partial t}}+\mathbf {v} \cdot \nabla \right)\mathbf {v} =\mathbf {J} \times \mathbf {B} -\nabla p,$ the low-frequency Ampère's law $\mu _{0}\mathbf {J} =\nabla \times \mathbf {B} ,$ Faraday's law ${\frac {\partial \mathbf {B} }{\partial t}}=-\nabla \times \mathbf {E} ,$ and Ohm's law $\mathbf {E} +\mathbf {v} \times \mathbf {B} =\eta \mathbf {J} .$ Taking the curl of this equation and applying Ampère's law and Faraday's law yields the induction equation, ${\frac {\partial \mathbf {B} }{\partial t}}=\nabla \times \left(\mathbf {v} \times \mathbf {B} \right)+{\frac {\eta }{\mu _{0}}}\nabla ^{2}\mathbf {B} ,$ where $\eta /\mu _{0}$ is the magnetic diffusivity.

In the equation of motion, the Lorentz force term $\mathbf {J} \times \mathbf {B}$ can be expanded using Ampère's law and a vector calculus identity to yield $\mathbf {J} \times \mathbf {B} ={\frac {\left(\mathbf {B} \cdot \nabla \right)\mathbf {B} }{\mu _{0}}}-\nabla \left({\frac {B^{2}}{2\mu _{0}}}\right),$ where the first term on the right-hand side is the magnetic tension force and the second term is the magnetic pressure force.

## Ideal MHD

> In view of the infinite conductivity, every motion (perpendicular to the field) of the liquid in relation to the lines of force is forbidden because it would give infinite eddy currents. Thus the matter of the liquid is "fastened" to the lines of force...

—

Hannes Alfvén

, 1943

The simplest form of MHD, **ideal MHD**, assumes that the resistive term $\eta \mathbf {J}$ in Ohm's law is sufficiently small relative to the other terms that it can be taken to be zero. This occurs in the limit of large magnetic Reynolds numbers, in which magnetic induction dominates magnetic diffusion at the velocity and length scales under consideration. Consequently, processes in ideal MHD that convert magnetic energy into kinetic energy, referred to as *ideal processes*, cannot generate heat or increase entropy.

A fundamental concept underlying ideal MHD is the frozen-in flux theorem, which states that the bulk fluid and the embedded magnetic field are constrained to move together such that one can be said to be "tied" or "frozen" to the other. Therefore, any two points that move with the bulk fluid velocity and lie on the same magnetic field line will continue to lie on that field line even as the points are advected by fluid flows in the system. The connection between the fluid and magnetic field fixes the topology of the magnetic field in the fluid. For example, if a set of magnetic field lines is tied into a knot, then it will remain so as long as the fluid has negligible resistivity. This difficulty in reconnecting magnetic field lines makes it possible to store energy by moving the fluid or the source of the magnetic field. The energy can then become available if the conditions for ideal MHD break down, allowing magnetic reconnection to release the stored energy from the magnetic field.

### Ideal MHD equations

In ideal MHD, the resistive term $\eta \mathbf {J}$ vanishes in Ohm's law, yielding the ideal Ohm's law: $\mathbf {E} +\mathbf {v} \times \mathbf {B} =0.$ Similarly, the magnetic diffusion term $\eta \nabla ^{2}\mathbf {B} /\mu _{0}$ in the induction equation vanishes, yielding the ideal induction equation: ${\frac {\partial \mathbf {B} }{\partial t}}=\nabla \times (\mathbf {v} \times \mathbf {B} ).$

### Applicability of ideal MHD to plasmas

Ideal MHD is strictly applicable when:

1. The plasma is strongly collisional, so that the collision time scale is shorter than the other characteristic time scales in the system, and the particle distributions are therefore close to Maxwellian.
2. The resistivity due to these collisions is small. In particular, the typical magnetic diffusion time over any length scale present in the system must be longer than any time scale of interest.
3. The relevant length scales are much longer than the ion skin depth and the Larmor radius perpendicular to the field, sufficiently long scales along the field to ignore Landau damping, and time scales much longer than the ion gyration time (that is, the system is smooth and slowly evolving).

### Importance of resistivity

In an imperfectly conducting fluid, the magnetic field can generally move through the fluid according to a diffusion law, with the resistivity of the plasma serving as a diffusion constant. This means that solutions to the ideal MHD equations are applicable only for a limited time within a region of a given size before diffusion becomes too significant to ignore. One can estimate the diffusion time across a solar active region (from collisional resistivity) to be hundreds to thousands of years, much longer than the actual lifetime of a sunspot, so it would seem reasonable to ignore the resistivity. By contrast, a meter-sized volume of seawater has a magnetic diffusion time measured in milliseconds.

Even in physical systems that are large and conductive enough that simple estimates of the Lundquist number suggest that the resistivity can be ignored, resistivity may still be important: many instabilities can increase the effective resistivity of the plasma by factors greater than 109. The enhanced resistivity is usually the result of the formation of small-scale structures such as current sheets or fine-scale magnetic turbulence, introducing small spatial scales into the system over which ideal MHD breaks down and magnetic diffusion can occur rapidly. When this happens, magnetic reconnection may occur in the plasma, releasing stored magnetic energy as waves, bulk mechanical acceleration of material, particle acceleration, and heat.

Magnetic reconnection in highly conductive systems is important because it concentrates energy in time and space, such that gentle forces applied to a plasma over long periods of time can cause violent explosions and bursts of radiation.

When the fluid cannot be considered completely conductive, but the other conditions for ideal MHD are satisfied, it is possible to use an extended model called resistive MHD. This includes an extra term in Ohm's law that models the collisional resistivity. Generally, MHD computer simulations are at least somewhat resistive because their computational grid introduces a numerical resistivity.

## Structures in MHD systems

In many MHD systems, most of the electric current is compressed into thin, nearly two-dimensional ribbons termed current sheets. These can divide the fluid into magnetic domains within which the currents are relatively weak. Current sheets in the solar corona are thought to be between a few meters and a few kilometers thick, which is quite thin compared to the magnetic domains, which are thousands to hundreds of thousands of kilometers across. Another example occurs in the Earth's magnetosphere, where current sheets separate topologically distinct domains, isolating most of the Earth's ionosphere from the solar wind.

## Waves

The wave modes derived from the MHD equations are called **magnetohydrodynamic waves,** or **MHD waves**. There are three MHD wave modes that can be derived from the linearized ideal MHD equations for a fluid with a uniform, and constant magnetic field:

- Alfvén waves
- Slow magnetosonic waves
- Fast magnetosonic waves

Phase velocity plotted with respect to

θ

v

A

>

v

s

v

A

<

v

s

These modes have phase velocities that are independent of the magnitude of the wave vector, so they experience no dispersion. The phase velocity depends on the angle between the wave vector ⁠ $\mathbf {k}$ ⁠ and the magnetic field ⁠ $\mathbf {B}$ ⁠. An MHD wave propagating at an arbitrary angle ⁠ $\theta$ ⁠ with respect to the time-independent, or bulk, field ⁠ $\mathbf {B} _{0}$ ⁠ satisfies the dispersion relation: ${\frac {\omega }{k}}=v_{\text{A}}\cos \theta$ where $v_{\text{A}}={\frac {B_{0}}{\sqrt {\mu _{0}\rho }}}$ is the Alfvén speed. This branch corresponds to the shear Alfvén mode. Additionally the dispersion equation yields: ${\frac {\omega }{k}}=\left[{\frac {1}{2}}\left(v_{\text{A}}^{2}+v_{\text{s}}^{2}\pm {\sqrt {\left(v_{\text{A}}^{2}+v_{\text{s}}^{2}\right)^{2}-4v_{\text{s}}^{2}v_{\text{A}}^{2}\cos ^{2}\theta }}\right)\right]^{1/2}$ where $v_{\text{s}}={\sqrt {\frac {\gamma p}{\rho }}}$ is the ideal gas speed of sound. The plus branch corresponds to the fast MHD wave mode, and the minus branch corresponds to the slow MHD wave mode. A summary of the properties of these waves is provided below:

| Mode | Type | Limiting phase speeds | Group velocity | Direction of energy flow |   |
|---|---|---|---|---|---|
| $\mathbf {k} \parallel \mathbf {B}$ | $\mathbf {k} \perp \mathbf {B}$ |   |   |   |   |
| Alfvén wave | transversal; incompressible | $v_{\text{A}}$ | 0 | ${\frac {\mathbf {B} }{\sqrt {\mu _{0}\rho }}}$ | $\mathbf {Q} \parallel \mathbf {B}$ |
| Fast magnetosonic wave | neither transversal nor longitudinal; compressional | $\max(v_{\text{A}},v_{\text{s}})$ | ${\sqrt {v_{\text{A}}^{2}+v_{\text{s}}^{2}}}$ | equal to phase velocity | approx. $\mathbf {Q} \parallel \mathbf {k}$ |
| Slow magnetosonic wave | $\min(v_{\text{A}},v_{\text{s}})$ | 0 | approx. $\mathbf {Q} \parallel \mathbf {B}$ |   |   |

MHD oscillations are damped if the fluid is not perfectly conducting but has finite conductivity, or if viscous effects are present.

MHD waves and oscillations are popular tools for the remote diagnostics of laboratory and astrophysical plasmas, for example, the Sun's corona (coronal seismology).

## Extensions

**Resistive**

Resistive MHD describes magnetized fluids with finite electron diffusivity (

⁠

$\eta \neq 0$

⁠

). This diffusivity leads to a break in the magnetic topology; magnetic field lines can "reconnect" when they collide. Usually, this term is small, and reconnections can be treated as similar to

shocks

; this process has been shown to be important in Earth-solar magnetic interactions.

**Extended**

Extended MHD describes a class of phenomena in plasmas that are higher-order than resistive MHD, but can adequately be treated with a single-fluid description. These include the effects of Hall physics, electron pressure gradients, finite Larmor radii in the particle gyromotion, and electron inertia.

**Two-fluid**

Two-fluid MHD describes plasmas that include a non-negligible Hall

electric field

. As a result, the electron and ion momenta must be treated separately. This description is more closely tied to Maxwell's equations because an evolution equation for the electric field exists.

**Hall**

In 1960, M. J. Lighthill criticized the applicability of ideal or resistive MHD theory for plasmas.

This concerned the neglect of the "

Hall current

term" in Ohm's law, a frequent simplification made in magnetic fusion theory. Hall magnetohydrodynamics (HMHD) takes into account this electric-field description of magnetohydrodynamics, and Ohm's law takes the form:

$\mathbf {E} +\mathbf {v} \times \mathbf {B} -\underbrace {{\frac {1}{n_{\text{e}}e}}(\mathbf {J} \times \mathbf {B} )} _{\text{Hall current term}}=\eta \mathbf {J} ,$

where

$n_{\text{e}}$

is the electron number density, and

e

is the

elementary charge

. The most important difference is that, in the absence of field line-breaking, the magnetic field is tied to the electrons rather than to the bulk fluid.

**Electron MHD**

Electron magnetohydrodynamics (EMHD) describes small-scale plasmas in which electron motion is much faster than the ion motion. The main effects are changes in conservation laws, additional resistivity, and the importance of electron inertia. Many effects of Electron MHD are similar to those of two-fluid MHD and Hall MHD. EMHD is especially important for

z-pinches

,

magnetic reconnection

,

ion thrusters

,

neutron stars

, and plasma switches.

**Collisionless**

MHD is also used for collisionless plasmas. In that case, the MHD equations are derived from the

Vlasov equation

.

**Reduced**

By using a

multiscale analysis

, the (resistive) MHD equations can be reduced to a set of four closed scalar equations. This allows for, among other things, more efficient numerical calculations.

## Limitations

### Importance of kinetic effects

Another limitation of MHD (and fluid theories in general) is that it depends on the assumption that the plasma is strongly collisional (this is the first criterion listed above), such that the collision time scale is shorter than the other characteristic time scales in the system, and the particle distributions are Maxwellian. This is usually not the case in fusion, space, and astrophysical plasmas. When this is not the case, or when interest lies in smaller spatial scales, it may be necessary to use a kinetic model that properly accounts for the non-Maxwellian shape of the distribution function. However, because MHD is relatively simple and captures many of the important properties of plasma dynamics, it is often qualitatively accurate and is therefore often the first model tried.

Effects that are essentially kinetic and not captured by fluid models include double layers, Landau damping, a wide range of instabilities, chemical separation in space plasmas, and electron runaway. In the case of ultra-high-intensity laser interactions, the extremely short time scales of energy deposition mean that hydrodynamic codes fail to capture the essential physics.

## Applications

### Geophysics

Beneath the Earth's mantle lies the core, which is made up of two parts: the solid inner core and the liquid outer core. Both contain significant quantities of iron. The liquid outer core moves in the presence of the magnetic field, and eddies are generated within it due to the Coriolis effect. These eddies develop a magnetic field that boosts Earth's original magnetic field, a self-sustaining process known as the geomagnetic dynamo.

Based on the MHD equations, Glatzmaier and Paul Roberts developed a supercomputer model of the Earth's interior. After the simulations are run for thousands of years in virtual time, changes in Earth's magnetic field can be studied. The simulation results are in good agreement with observations because the simulations correctly predict that the Earth's magnetic field reverses every few hundred thousand years. During these reversals, the magnetic field does not vanish altogether; instead, it becomes more complex.

#### Earthquakes

Some monitoring stations have reported that earthquakes are sometimes preceded by a spike in ultra-low-frequency (ULF) activity. A notable example of this occurred before the 1989 Loma Prieta earthquake in California, although a subsequent study indicated that this was little more than a sensor malfunction. On December 9, 2010, geoscientists announced that the DEMETER satellite observed a dramatic increase in ULF radio waves over Haiti in the month before the magnitude 7.0 Mw 2010 earthquake. Researchers are attempting to learn more about this correlation to determine whether this method can be used as part of an earthquake early warning system.

### Space physics

The study of space plasmas near Earth and throughout the Solar System is known as space physics. Researched areas within space physics encompass a wide range of topics, including the ionosphere,auroras, Earth's magnetosphere, the solar wind, and coronal mass ejections.

MHD provides a framework for understanding how plasma populations interact within the local geospace environment. Researchers have developed global models using MHD to simulate phenomena within Earth's magnetosphere, such as the location of Earth's magnetopause (the boundary between Earth's magnetic field and the solar wind), the formation of the ring current, auroral electrojets, and geomagnetically induced currents.

One prominent use of global MHD models is space weather forecasting. Intense solar storms have the potential to cause extensive damage to satellites and infrastructure; thus, it is crucial that such events be detected early. The Space Weather Prediction Center (SWPC) uses MHD models to predict the arrival and impacts of space weather events at Earth.

### Astrophysics

MHD applies to astrophysics, including stars, the interplanetary medium (space between the planets), the interstellar medium (space between the stars), and jets. Most astrophysical systems are not in local thermal equilibrium and therefore require an additional kinematic treatment to describe all the phenomena within the system (see Astrophysical plasma).

Sunspots are caused by the Sun's magnetic fields, as Joseph Larmor theorized in 1919. The solar wind, predicted by Eugene Parker, is also described by MHD. The differential solar rotation may be the long-term effect of magnetic drag at the Sun's poles, an MHD phenomenon resulting from the Parker spiral shape of the Sun's extended magnetic field.

Previously, theories describing the formation of the Sun and planets could not explain how the Sun contains 99.87% of the mass, yet only 0.54% of the angular momentum, in the Solar System. In a closed system, such as the cloud of gas and dust from which the Sun formed, mass and angular momentum are both conserved. That conservation would imply that, as the mass concentrated at the center of the cloud to form the Sun, it would spin faster, much like a skater pulling in their arms. The high rotational speed predicted by early theories would have flung the proto-Sun apart before it could form. However, magnetohydrodynamic effects transfer the Sun's angular momentum to the outer solar system, slowing its rotation.

Breakdown of ideal MHD, in the form of magnetic reconnection, is thought to be the likely cause of solar flares. The magnetic field in a solar active region above a sunspot can store energy that is suddenly released as a burst of motion, X-rays, and radiation when the main current sheet collapses and reconnects the field.

### Magnetic confinement fusion

MHD describes a wide range of physical phenomena occurring in fusion plasmas in devices such as tokamaks and stellarators.

The Grad-Shafranov equation, derived from ideal MHD, describes the equilibrium of axisymmetric toroidal plasma in a tokamak. In tokamak experiments, the equilibrium during each discharge is routinely calculated and reconstructed, providing information on the shape and position of the plasma controlled by currents in external coils.

MHD stability theory governs the operational limits of tokamaks. For example, ideal MHD kink modes provide hard limits on the achievable plasma beta (Troyon limit) and plasma current (set by the $q>2$ requirement for the safety factor).

In a tokamak, instabilities also arise from resistive MHD. For instance, tearing modes are instabilities that arise within the framework of non-ideal MHD. This is an active field of research because these instabilities are the starting point for disruptions.

### Sensors

Magnetohydrodynamic sensors are used for precise measurements of angular velocity in inertial navigation systems such as those used in aerospace engineering. Accuracy improves with sensor size. The sensor is capable of operating in harsh environments.

### Engineering

MHD is related to engineering problems such as plasma confinement, liquid-metal cooling in nuclear reactors, and electromagnetic casting.

A magnetohydrodynamic drive, or MHD propulsor, is a method for propelling seagoing vessels using only electric and magnetic fields, with no moving parts. The working principle involves electrifying the propellant (gas or water), which can then be directed by a magnetic field, thereby pushing the vehicle in the opposite direction. Although some working prototypes exist, MHD drives remain impractical.

The first prototype of this type of propulsion was built and tested in 1965 by Steward Way, a professor of mechanical engineering at the University of California, Santa Barbara. While on leave from his job at Westinghouse Electric, Way assigned his senior-year undergraduate students to develop a submarine using this new propulsion system. In the early 1990s, the Ship & Ocean Foundation (Minato-ku, Tokyo) built an experimental boat, the *Yamato-1*, which used a magnetohydrodynamic drive incorporating a superconductor cooled by liquid helium and could travel at 15 km/h.

MHD power generation fueled by potassium-seeded coal-combustion gas showed potential for more efficient energy conversion (the absence of solid moving parts allows operation at higher temperatures) but ultimately failed due to cost-prohibitive technical difficulties. One major engineering problem was the abrasion-induced failure of the wall of the primary-coal combustion chamber.

In microfluidics, MHD is studied as a fluid pump for producing continuous, nonpulsating flow in a complex microchannel design.

MHD can be implemented in the continuous casting of metals to suppress instabilities and control flow.

Industrial MHD problems can be modeled using the open-source software EOF-Library. Two simulation examples are three-dimensional MHD with a free surface for electromagnetic levitation melting and liquid-metal stirring using rotating permanent magnets.

### Magnetic drug targeting

An important task in cancer research is developing more precise methods for delivering medicine to affected areas. One method involves binding of medicine to biologically compatible magnetic particles (such as ferrofluids), which are guided to the target through careful placement of permanent magnets on the exterior of the body. Magnetohydrodynamic equations and finite element analysis are used to study interactions between magnetic fluid particles in the bloodstream and the external magnetic field.
