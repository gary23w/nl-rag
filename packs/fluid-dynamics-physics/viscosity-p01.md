---
title: "Viscosity (part 1/2)"
source: https://en.wikipedia.org/wiki/Viscosity
domain: fluid-dynamics-physics
license: CC-BY-SA-4.0
tags: fluid dynamics, reynolds number, boundary layer, compressible flow
fetched: 2026-07-02
part: 1/2
---

# Viscosity

In continuum mechanics, **viscosity** is a property of a fluid that quantifies the resistance force acting on fluids when there is relative motion between fluid parcels. This resistance force is caused by the stress in fluid parcels, which ideally is directly proportional to the strain rate (the time derivative of strain) that arises when fluid parcels are in relative motion, and the relative speed between the boundary between adjacent fluid parcels is zero. In liquids, viscosity arises from cohesive molecular forces, while in gases it results from molecular collisions. Except for the case of superfluidity, there is no fluid with zero viscosity, and thus all fluid flows involve viscous effects to some degree.

For liquids, it corresponds to the informal concept of *thickness*; for example, syrup has a higher viscosity than water. Viscosity is defined scientifically as a force multiplied by a time divided by an area. Thus its SI units are newton-seconds per metre squared, or pascal-seconds.

For instance, when a viscous fluid is forced through a tube, it flows more quickly near the tube's center line than near its walls. Some stress (such as a pressure difference between the two ends of the tube) is needed to sustain the flow. This is because a force is required to overcome the friction between the layers of the fluid which are in relative motion. For a tube with a constant rate of flow, the strength of the compensating force is proportional to the fluid's viscosity.

In general, viscosity depends on a fluid's state, such as its temperature, pressure, and rate of deformation. However, the dependence on some of these properties is negligible in certain cases. For example, the viscosity of a Newtonian fluid does not vary significantly with the rate of deformation.

Zero viscosity (no resistance to shear stress) is observed only at very low temperatures in superfluids; otherwise, the second law of thermodynamics requires all fluids to have positive viscosity. A fluid that has zero viscosity (non-viscous) is called *ideal* or *inviscid*.

For non-Newtonian fluids' viscosity, there are pseudoplastic, plastic, and dilatant flows that are time-independent, and there are thixotropic and rheopectic flows that are time-dependent.


## Etymology

The word "viscosity" is derived from the Latin **viscum** ("mistletoe"). **Viscum** also referred to a viscous glue derived from mistletoe berries.


## Definitions

### Dynamic viscosity

In materials science and engineering, there is often interest in understanding the forces or stresses involved in the deformation of a material. For instance, if the material were a simple spring, the answer would be given by Hooke's law, which says that the force experienced by a spring is proportional to the distance displaced from equilibrium. Stresses which can be attributed to the deformation of a material from some rest state are called elastic stresses. In other materials, stresses are present which can be attributed to the deformation rate over time. These are called viscous stresses. For instance, in a fluid such as water the stresses which arise from shearing the fluid do not depend on the *distance* the fluid has been sheared; rather, they depend on how *quickly* the shearing occurs.

Viscosity is the material property which relates the viscous stresses in a material to the rate of change of a deformation (the strain rate). Although it applies to general flows, it is easy to visualize and define in a simple shearing flow, such as a planar Couette flow.

In the Couette flow, a fluid is trapped between two infinitely large plates, one fixed and one in parallel motion at constant speed u (see illustration to the right). If the speed of the top plate is low enough (to avoid turbulence), then in steady state the fluid particles move parallel to it, and their speed varies from 0 at the bottom to u at the top. Each layer of fluid moves faster than the one just below it, and friction between them gives rise to a force resisting their relative motion. In particular, the fluid applies on the top plate a force in the direction opposite to its motion, and an equal but opposite force on the bottom plate. An external force is therefore required in order to keep the top plate moving at constant speed.

In many fluids, the flow velocity is observed to vary linearly from zero at the bottom to u at the top. Moreover, the magnitude of the force, F , acting on the top plate is found to be proportional to the speed u and the area A of each plate, and inversely proportional to their separation y :

$F=\mu A{\frac {u}{y}}.$

The proportionality factor is the *dynamic viscosity* of the fluid, often simply referred to as the *viscosity*. It is denoted by the Greek letter mu (μ). The dynamic viscosity has the dimensions $\mathrm {(mass/length)/time}$ , therefore resulting in the SI units and the derived units:

$[\mu ]={\frac {\rm {kg}}{\rm {m{\cdot }s}}}={\frac {\rm {N}}{\rm {m^{2}}}}{\cdot }{\rm {s}}={\rm {Pa{\cdot }s}}=$

pressure

multiplied by

time

=

energy per unit volume multiplied by time.

The aforementioned ratio $u/y$ is called the *rate of shear deformation* or *shear velocity*, and is the derivative of the fluid speed in the direction parallel to the normal vector of the plates (see illustrations to the right). If the velocity does not vary linearly with y , then the appropriate generalization is:

$\tau =\mu {\frac {\partial u}{\partial y}},$

where $\tau =F/A$ , and $\partial u/\partial y$ is the local shear velocity. This expression is referred to as Newton's law of viscosity. In shearing flows with planar symmetry, it is what *defines* $\mu$ . It is a special case of the general definition of viscosity (see below), which can be expressed in coordinate-free form.

Use of the Greek letter mu ( $\mu$ ) for the dynamic viscosity (sometimes also called the *absolute viscosity*) is common among mechanical and chemical engineers, as well as mathematicians and physicists. However, the Greek letter eta ( $\eta$ ) is also used by chemists, physicists, and the IUPAC. The viscosity $\mu$ is sometimes also called the *shear viscosity*. However, at least one author discourages the use of this terminology, noting that $\mu$ can appear in non-shearing flows in addition to shearing flows.

### Kinematic viscosity

In fluid dynamics, it is sometimes more appropriate to work in terms of *kinematic viscosity* (sometimes also called the *momentum diffusivity*), defined as the ratio of the dynamic viscosity (μ) over the density of the fluid (ρ). It is usually denoted by the Greek letter nu (ν):

$\nu ={\frac {\mu }{\rho }},$

and has the dimensions $\mathrm {(length)^{2}/time}$ , therefore resulting in the SI units and the derived units:

$[\nu ]=\mathrm {\frac {m^{2}}{s}} =\mathrm {{\frac {N{\cdot }m}{kg}}{\cdot }s} =\mathrm {{\frac {J}{kg}}{\cdot }s} =$

specific energy

multiplied by

time

=

energy per unit mass multiplied by time.

### General definition

In very general terms, the viscous stresses in a fluid are defined as those resulting from the relative velocity of different fluid particles. As such, the viscous stresses must depend on spatial gradients of the flow velocity. If the velocity gradients are small, then to a first approximation the viscous stresses depend only on the first derivatives of the velocity. (For Newtonian fluids, this is also a linear dependence.) In Cartesian coordinates, the general relationship can then be written as

$\tau _{ij}=\sum _{k}\sum _{\ell }\mu _{ijk\ell }{\frac {\partial v_{k}}{\partial r_{\ell }}},$

where $\mu _{ijk\ell }$ is a viscosity tensor that maps the velocity gradient tensor $\partial v_{k}/\partial r_{\ell }$ onto the viscous stress tensor $\tau _{ij}$ . Since the indices in this expression can vary from 1 to 3, there are 81 "viscosity coefficients" $\mu _{ijkl}$ in total. However, assuming that the viscosity rank-2 tensor is isotropic reduces these 81 coefficients to three independent parameters $\alpha$ , $\beta$ , $\gamma$ :

$\mu _{ijk\ell }=\alpha \delta _{ij}\delta _{k\ell }+\beta \delta _{ik}\delta _{j\ell }+\gamma \delta _{i\ell }\delta _{jk},$

and furthermore, it is assumed that no viscous forces may arise when the fluid is undergoing simple rigid-body rotation, thus $\beta =\gamma$ , leaving only two independent parameters. The most usual decomposition is in terms of the standard (scalar) viscosity $\mu$ and the bulk viscosity $\kappa$ such that $\alpha =\kappa -{\tfrac {2}{3}}\mu$ and $\beta =\gamma =\mu$ . In vector notation this appears as:

${\boldsymbol {\tau }}=\mu \left[\nabla \mathbf {v} +(\nabla \mathbf {v} )^{\mathrm {T} }\right]-\left({\frac {2}{3}}\mu -\kappa \right)(\nabla \cdot \mathbf {v} )\mathbf {\delta } ,$

where $\mathbf {\delta }$ is the unit tensor. This equation can be thought of as a generalized form of Newton's law of viscosity.

The bulk viscosity (also called volume viscosity) expresses a type of internal friction that resists the shearless compression or expansion of a fluid. Knowledge of $\kappa$ is frequently not necessary in fluid dynamics problems. For example, an incompressible fluid satisfies $\nabla \cdot \mathbf {v} =0$ and so the term containing $\kappa$ drops out. Moreover, $\kappa$ is often assumed to be negligible for gases since it is 0 in a monatomic ideal gas. One situation in which $\kappa$ can be important is the calculation of energy loss in sound and shock waves, described by Stokes' law of sound attenuation, since these phenomena involve rapid expansions and compressions.

The defining equations for viscosity are not fundamental laws of nature, so their usefulness, as well as methods for measuring or calculating the viscosity, must be established using separate means. A potential issue is that viscosity depends, in principle, on the full microscopic state of the fluid, which encompasses the positions and momenta of every particle in the system. Such highly detailed information is typically not available in realistic systems. However, under certain conditions most of this information can be shown to be negligible. In particular, for Newtonian fluids near equilibrium and far from boundaries (bulk state), the viscosity depends only space- and time-dependent macroscopic fields (such as temperature and density) defining local equilibrium.

Nevertheless, viscosity may still carry a non-negligible dependence on several system properties, such as temperature, pressure, and the amplitude and frequency of any external forcing. Therefore, precision measurements of viscosity are only defined with respect to a specific fluid state. To standardize comparisons among experiments and theoretical models, viscosity data is sometimes extrapolated to ideal limiting cases, such as the *zero shear* limit, or (for gases) the *zero density* limit.


## Momentum transport

Transport theory provides an alternative interpretation of viscosity in terms of momentum transport: viscosity is the material property which characterizes momentum transport within a fluid, just as thermal conductivity characterizes heat transport, and (mass) diffusivity characterizes mass transport. This perspective is implicit in Newton's law of viscosity, $\tau =\mu (\partial u/\partial y)$ , because the shear stress $\tau$ has units equivalent to a momentum flux, i.e., momentum per unit time per unit area. Thus, $\tau$ can be interpreted as specifying the flow of momentum in the y direction from one fluid layer to the next. Per Newton's law of viscosity, this momentum flow occurs across a velocity gradient, and the magnitude of the corresponding momentum flux is determined by the viscosity.

The analogy with heat and mass transfer can be made explicit. Just as heat flows from high temperature to low temperature and mass flows from high density to low density, momentum flows from high velocity to low velocity. These behaviors are all described by compact expressions, called constitutive relations, whose one-dimensional forms are given here:

${\begin{aligned}\mathbf {J} &=-D{\frac {\partial \rho }{\partial x}}&&{\text{(Fick's law of diffusion)}}\\[5pt]\mathbf {q} &=-k_{t}{\frac {\partial T}{\partial x}}&&{\text{(Fourier's law of heat conduction)}}\\[5pt]\tau &=\mu {\frac {\partial u}{\partial y}}&&{\text{(Newton's law of viscosity)}}\end{aligned}}$

where $\rho$ is the density, $\mathbf {J}$ and $\mathbf {q}$ are the mass and heat fluxes, and D and $k_{t}$ are the mass diffusivity and thermal conductivity. The fact that mass, momentum, and energy (heat) transport are among the most relevant processes in continuum mechanics is not a coincidence: these are among the few physical quantities that are conserved at the microscopic level in interparticle collisions. Thus, rather than being dictated by the fast and complex microscopic interaction timescale, their dynamics occurs on macroscopic timescales, as described by the various equations of transport theory and hydrodynamics.


## Newtonian and non-Newtonian fluids

Newton's law of viscosity is not a fundamental law of nature, but rather a constitutive equation (like Hooke's law, Fick's law, and Ohm's law) which serves to define the viscosity $\mu$ . Its form is motivated by experiments which show that for a wide range of fluids, $\mu$ is independent of strain rate. Such fluids are called Newtonian. Gases, water, and many common liquids can be considered Newtonian in ordinary conditions and contexts. However, there are many non-Newtonian fluids that significantly deviate from this behavior. For example:

- Shear-thickening (dilatant) liquids, whose viscosity increases with the rate of shear strain.
- Shear-thinning liquids, whose viscosity decreases with the rate of shear strain.
- Thixotropic liquids, that become less viscous over time when shaken, agitated, or otherwise stressed.
- Rheopectic liquids, that become more viscous over time when shaken, agitated, or otherwise stressed.
- Bingham plastics that behave as a solid at low stresses but flow as a viscous fluid at high stresses.

Trouton's ratio is the ratio of extensional viscosity to shear viscosity. For a Newtonian fluid, the Trouton ratio is 3. Shear-thinning liquids are very commonly, but misleadingly, described as thixotropic.

Viscosity may also depend on the fluid's physical state (temperature and pressure) and other, *external*, factors. For gases and other compressible fluids, it depends on temperature and varies very slowly with pressure. The viscosity of some fluids may depend on other factors. A magnetorheological fluid, for example, becomes thicker when subjected to a magnetic field, possibly to the point of behaving like a solid.


## In solids

The viscous forces that arise during fluid flow are distinct from the elastic forces that occur in a solid in response to shear, compression, or extension stresses. While in the latter the stress is proportional to the *amount* of shear deformation, in a fluid it is proportional to the *rate* of deformation over time. For this reason, James Clerk Maxwell used the term *fugitive elasticity* for fluid viscosity.

However, many liquids (including water) will briefly react like elastic solids when subjected to sudden stress. Conversely, many "solids" (even granite) will flow like liquids, albeit very slowly, even under arbitrarily small stress. Such materials are best described as viscoelastic—that is, possessing both elasticity (reaction to deformation) and viscosity (reaction to rate of deformation).

Viscoelastic solids may exhibit both shear viscosity and bulk viscosity. The extensional viscosity is a linear combination of the shear and bulk viscosities that describes the reaction of a solid elastic material to elongation. It is widely used for characterizing polymers.

In geology, earth materials that exhibit viscous deformation at least three orders of magnitude greater than their elastic deformation are sometimes called rheids.


## Measurement

Viscosity is measured with various types of viscometers and rheometers. Close temperature control of the fluid is essential to obtain accurate measurements, particularly in materials like lubricants, whose viscosity can double with a change of only 5 °C. A rheometer is used for fluids that cannot be defined by a single value of viscosity and therefore require more parameters to be set and measured than is the case for a viscometer.

For some fluids, the viscosity is constant over a wide range of shear rates (Newtonian fluids). The fluids without a constant viscosity (non-Newtonian fluids) cannot be described by a single number. Non-Newtonian fluids exhibit a variety of different correlations between shear stress and shear rate.

One of the most common instruments for measuring kinematic viscosity is the glass capillary viscometer.

In coating industries, viscosity may be measured with a cup in which the efflux time is measured. There are several sorts of cup—such as the Zahn cup and the Ford viscosity cup—with the usage of each type varying mainly according to the industry.

Also used in coatings, a *Stormer viscometer* employs load-based rotation to determine viscosity. The viscosity is reported in Krebs units (KU), which are unique to Stormer viscometers.

Vibrating viscometers can also be used to measure viscosity. Resonant, or vibrational viscometers work by creating shear waves within the liquid. In this method, the sensor is submerged in the fluid and is made to resonate at a specific frequency. As the surface of the sensor shears through the liquid, energy is lost due to its viscosity. This dissipated energy is then measured and converted into a viscosity reading. A higher viscosity causes a greater loss of energy.

*Extensional viscosity* can be measured with various rheometers that apply extensional stress.

Volume viscosity can be measured with an acoustic rheometer.

Apparent viscosity is a calculation derived from tests performed on drilling fluid used in oil or gas well development. These calculations and tests help engineers develop and maintain the properties of the drilling fluid to the specifications required.

Nanoviscosity (viscosity sensed by nanoprobes) can be measured by fluorescence correlation spectroscopy.


## Units

The SI unit of dynamic viscosity is the newton-second per metre squared (N·s/m2), also frequently expressed in the equivalent forms pascal-second (Pa·s), kilogram per meter per second (kg·m−1·s−1) and poiseuille (Pl). The CGS unit is the poise (P, or g·cm−1·s−1 = 0.1 Pa·s), named after Jean Léonard Marie Poiseuille. It is commonly expressed, particularly in ASTM standards, as *centipoise* (cP). The centipoise is convenient because the viscosity of water at 20 °C is about 1 cP, and one centipoise is equal to the SI millipascal second (mPa·s).

The SI unit of kinematic viscosity is metre squared per second (m2/s), whereas the CGS unit for kinematic viscosity is the **stokes** (St, or cm2·s−1 = 0.0001 m2·s−1), named after Sir George Gabriel Stokes. In U.S. usage, *stoke* is sometimes used as the singular form. The submultiple *centistokes* (cSt) is often used instead, 1 cSt = 1 mm2·s−1 = 10−6 m2·s−1. 1 cSt is 1 cP divided by 1000 kg/m^3, close to the density of water. The kinematic viscosity of water at 20 °C is about 1 cSt.

The most frequently used systems of US customary, or Imperial, units are the British Gravitational (BG) and English Engineering (EE). In the BG system, dynamic viscosity has units of *pound*-seconds per square foot (lb·s/ft2), and in the EE system it has units of *pound-force*-seconds per square foot (lbf·s/ft2). The pound and pound-force are equivalent; the two systems differ only in how force and mass are defined. In the BG system the pound is a basic unit from which the unit of mass (the slug) is defined by Newton's second law, whereas in the EE system the units of force and mass (the pound-force and pound-mass respectively) are defined independently through the second law using the proportionality constant *gc*.

Kinematic viscosity has units of square feet per second (ft2/s) in both the BG and EE systems.

Nonstandard units include the reyn (lbf·s/in2), a British unit of dynamic viscosity. In the automotive industry the viscosity index is used to describe the change of viscosity with temperature.

The reciprocal of viscosity is *fluidity*, usually symbolized by $\phi =1/\mu$ or $F=1/\mu$ , depending on the convention used, measured in *reciprocal poise* (P−1, or cm·s·g−1), sometimes called the *rhe*. Fluidity is seldom used in engineering practice.

At one time the petroleum industry relied on measuring kinematic viscosity by means of the Saybolt viscometer, and expressing kinematic viscosity in units of Saybolt universal seconds (SUS). Other abbreviations such as SSU (*Saybolt seconds universal*) or SUV (*Saybolt universal viscosity*) are sometimes used. Kinematic viscosity in centistokes can be converted from SUS according to the arithmetic and the reference table provided in ASTM D 2161.


## Molecular origins

Momentum transport in gases is mediated by discrete molecular collisions, and in liquids by attractive forces that bind molecules close together. Because of this, the dynamic viscosities of liquids are typically much larger than those of gases. In addition, viscosity tends to increase with temperature in gases and decrease with temperature in liquids.

Above the liquid-gas critical point, the liquid and gas phases are replaced by a single supercritical phase. In this regime, the mechanisms of momentum transport interpolate between liquid-like and gas-like behavior. For example, along a supercritical isobar (constant-pressure surface), the kinematic viscosity decreases at low temperature and increases at high temperature, with a minimum in between. Kostya Trachenko and Vadim Brazhkin provided a rough estimate for the value at the minimum, given by

$\nu _{\text{min}}={\frac {1}{4\pi }}{\frac {\hbar }{\sqrt {m_{\text{e}}m}}}$

where $\hbar$ is the Planck constant, $m_{\text{e}}$ is the electron mass, and m is the molecular mass.

In general, however, the viscosity of a system depends in detail on how the molecules constituting the system interact, and there are no simple but correct formulas for it. The simplest exact expressions are the Green–Kubo relations for the linear shear viscosity or the *transient time correlation function* expressions derived by Evans and Morriss in 1988. Although these expressions are each exact, calculating the viscosity of a dense fluid using these relations currently requires the use of molecular dynamics computer simulations. Somewhat more progress can be made for a dilute gas, as elementary assumptions about how gas molecules move and interact lead to a basic understanding of the molecular origins of viscosity. More sophisticated treatments can be constructed by systematically coarse-graining the equations of motion of the gas molecules. An example of such a treatment is Chapman–Enskog theory, which derives expressions for the viscosity of a dilute gas from the Boltzmann equation.

### Pure gases

#### Elementary calculation of viscosity for a dilute gas

Consider a dilute gas moving parallel to the x -axis with velocity $u(y)$ that depends only on the y coordinate. To simplify the discussion, the gas is assumed to have uniform temperature and density.

Under these assumptions, the x velocity of a molecule passing through $y=0$ is equal to whatever velocity that molecule had when its mean free path $\lambda$ began. Because $\lambda$ is typically small compared with macroscopic scales, the average x velocity of such a molecule has the form

$u(0)\pm \alpha \lambda {\frac {du}{dy}}(0),$

where $\alpha$ is a numerical constant on the order of 1 . (Some authors estimate $\alpha =2/3$ ; on the other hand, a more careful calculation for rigid elastic spheres gives $\alpha \simeq 0.998$ .) Next, because half the molecules on either side are moving towards $y=0$ , and doing so on average with half the average molecular speed $(8k_{\text{B}}T/\pi m)^{1/2}$ , the momentum flux from either side is

${\frac {1}{4}}\rho \cdot {\sqrt {\frac {8k_{\text{B}}T}{\pi m}}}\cdot \left(u(0)\pm \alpha \lambda {\frac {du}{dy}}(0)\right).$ The net momentum flux at $y=0$ is the difference of the two: $-{\frac {1}{2}}\rho \cdot {\sqrt {\frac {8k_{\text{B}}T}{\pi m}}}\cdot \alpha \lambda {\frac {du}{dy}}(0).$

According to the definition of viscosity, this momentum flux should be equal to $-\mu {\frac {du}{dy}}(0)$ , which leads to

$\mu =\alpha \rho \lambda {\sqrt {\frac {2k_{\text{B}}T}{\pi m}}}.$

Viscosity in gases arises principally from the molecular diffusion that transports momentum between layers of flow. An elementary calculation for a dilute gas at temperature T and density $\rho$ gives

$\mu =\alpha \rho \lambda {\sqrt {\frac {2k_{\text{B}}T}{\pi m}}},$

where $k_{\text{B}}$ is the Boltzmann constant, m the molecular mass, and $\alpha$ a numerical constant on the order of 1 . The quantity $\lambda$ , the mean free path, measures the average distance a molecule travels between collisions. Even without *a priori* knowledge of $\alpha$ , this expression has nontrivial implications. In particular, since $\lambda$ is typically inversely proportional to density and increases with temperature, $\mu$ itself should increase with temperature and be independent of density at fixed temperature. In fact, both of these predictions persist in more sophisticated treatments, and accurately describe experimental observations. By contrast, liquid viscosity typically decreases with temperature.

For rigid elastic spheres of diameter $\sigma$ , $\lambda$ can be computed, giving

$\mu ={\frac {\alpha }{\pi ^{3/2}}}{\frac {\sqrt {k_{\text{B}}mT}}{\sigma ^{2}}}.$

In this case $\lambda$ is independent of temperature, so $\mu \propto T^{1/2}$ . For more complicated molecular models, however, $\lambda$ depends on temperature in a non-trivial way, and simple kinetic arguments as used here are inadequate. More fundamentally, the notion of a mean free path becomes imprecise for particles that interact over a finite range, which limits the usefulness of the concept for describing real-world gases.

#### Chapman–Enskog theory

A technique developed by Sydney Chapman and David Enskog in the early 1900s allows a more refined calculation of $\mu$ . It is based on the Boltzmann equation, which provides a statistical description of a dilute gas in terms of intermolecular interactions. The technique allows accurate calculation of $\mu$ for molecular models that are more realistic than rigid elastic spheres, such as those incorporating intermolecular attractions. Doing so is necessary to reproduce the correct temperature dependence of $\mu$ , which experiments show increases more rapidly than the $T^{1/2}$ trend predicted for rigid elastic spheres. Indeed, the Chapman–Enskog analysis shows that the predicted temperature dependence can be tuned by varying the parameters in various molecular models. A simple example is the Sutherland model, which describes rigid elastic spheres with *weak* mutual attraction. In such a case, the attractive force can be treated perturbatively, which leads to a simple expression for $\mu$ : $\mu ={\frac {5}{16\sigma ^{2}}}\left({\frac {k_{\text{B}}mT}{\pi }}\right)^{\!\!1/2}\ \left(1+{\frac {S}{T}}\right)^{\!\!-1},$ where S is independent of temperature, being determined only by the parameters of the intermolecular attraction. To connect with experiment, it is convenient to rewrite as $\mu =\mu _{0}\left({\frac {T}{T_{0}}}\right)^{\!\!3/2}\ {\frac {T_{0}+S}{T+S}},$ where $\mu _{0}$ is the viscosity at temperature $T_{0}$ . This expression is usually named Sutherland's formula. If $\mu$ is known from experiments at $T=T_{0}$ and at least one other temperature, then S can be calculated. Expressions for $\mu$ obtained in this way are qualitatively accurate for a number of simple gases. Slightly more sophisticated models, such as the Lennard-Jones potential, or the more flexible Mie potential, may provide better agreement with experiments, but only at the cost of a more opaque dependence on temperature. A further advantage of these more complex interaction potentials is that they can be used to develop accurate models for a wide variety of properties using the same potential parameters. In situations where little experimental data is available, this makes it possible to obtain model parameters from fitting to properties such as pure-fluid vapour-liquid equilibria, before using the parameters thus obtained to predict the viscosities of interest with reasonable accuracy.

In some systems, the assumption of spherical symmetry must be abandoned, as is the case for vapors with highly polar molecules like H2O. In these cases, the Chapman–Enskog analysis is significantly more complicated.

#### Bulk viscosity

In the kinetic-molecular picture, a non-zero bulk viscosity arises in gases whenever there are non-negligible relaxational timescales governing the exchange of energy between the translational energy of molecules and their internal energy, e.g. rotational and vibrational. As such, the bulk viscosity is 0 for a monatomic ideal gas, in which the internal energy of molecules is negligible, but is nonzero for a gas like carbon dioxide, whose molecules possess both rotational and vibrational energy.

### Pure liquids

In contrast with gases, there is no simple yet accurate picture for the molecular origins of viscosity in liquids.

At the simplest level of description, the relative motion of adjacent layers in a liquid is opposed primarily by attractive molecular forces acting across the layer boundary. In this picture, one (correctly) expects viscosity to decrease with increasing temperature. This is because increasing temperature increases the random thermal motion of the molecules, which makes it easier for them to overcome their attractive interactions.

Building on this visualization, a simple theory can be constructed in analogy with the discrete structure of a solid: groups of molecules in a liquid are visualized as forming "cages" which surround and enclose single molecules. These cages can be occupied or unoccupied, and stronger molecular attraction corresponds to stronger cages. Due to random thermal motion, a molecule "hops" between cages at a rate which varies inversely with the strength of molecular attractions. In equilibrium these "hops" are not biased in any direction. On the other hand, in order for two adjacent layers to move relative to each other, the "hops" must be biased in the direction of the relative motion. The force required to sustain this directed motion can be estimated for a given shear rate, leading to

| $\mu \approx {\frac {N_{\text{A}}h}{V}}\operatorname {exp} \left(3.8{\frac {T_{\text{b}}}{T}}\right),$ |   | 1 |
|---|---|---|

where $N_{\text{A}}$ is the Avogadro constant, h is the Planck constant, V is the volume of a mole of liquid, and $T_{\text{b}}$ is the normal boiling point. This result has the same form as the well-known empirical relation

| $\mu =Ae^{B/T},$ |   | 2 |
|---|---|---|

where A and B are constants fit from data. On the other hand, several authors express caution with respect to this model. Errors as large as 30% can be encountered using equation (**1**), compared with fitting equation (**2**) to experimental data. More fundamentally, the physical assumptions underlying equation (**1**) have been criticized. It has also been argued that the exponential dependence in equation (**1**) does not necessarily describe experimental observations more accurately than simpler, non-exponential expressions.

In light of these shortcomings, the development of a less ad hoc model is a matter of practical interest. Foregoing simplicity in favor of precision, it is possible to write rigorous expressions for viscosity starting from the fundamental equations of motion for molecules. A classic example of this approach is Irving–Kirkwood theory. On the other hand, such expressions are given as averages over multiparticle correlation functions and are therefore difficult to apply in practice.

In general, empirically derived expressions (based on existing viscosity measurements) appear to be the only consistently reliable means of calculating viscosity in liquids.

Local atomic structure changes observed in undercooled liquids on cooling below the equilibrium melting temperature either in terms of radial distribution function *g*(*r*) or structure factor *S*(*Q*) are found to be directly responsible for the liquid fragility: deviation of the temperature dependence of viscosity of the undercooled liquid from the Arrhenius equation (2) through modification of the activation energy for viscous flow. At the same time equilibrium liquids follow the Arrhenius equation.

### Mixtures and blends

#### Gaseous mixtures

The same molecular-kinetic picture of a single component gas can also be applied to a gaseous mixture. For instance, in the Chapman–Enskog approach the viscosity $\mu _{\text{mix}}$ of a binary mixture of gases can be written in terms of the individual component viscosities $\mu _{1,2}$ , their respective volume fractions, and the intermolecular interactions.

As for the single-component gas, the dependence of $\mu _{\text{mix}}$ on the parameters of the intermolecular interactions enters through various collisional integrals which may not be expressible in closed form. To obtain usable expressions for $\mu _{\text{mix}}$ which reasonably match experimental data, the collisional integrals may be computed numerically or from correlations. In some cases, the collision integrals are regarded as fitting parameters, and are fitted directly to experimental data. This is a common approach in the development of reference equations for gas-phase viscosities. An example of such a procedure is the Sutherland approach for the single-component gas, discussed above.

For gas mixtures consisting of simple molecules, Revised Enskog Theory has been shown to accurately represent both the density- and temperature dependence of the viscosity over a wide range of conditions.

#### Blends of liquids

As for pure liquids, the viscosity of a blend of liquids is difficult to predict from molecular principles. One method is to extend the molecular "cage" theory presented above for a pure liquid. This can be done with varying levels of sophistication. One expression resulting from such an analysis is the Lederer–Roegiers equation for a binary mixture:

$\ln \mu _{\text{blend}}={\frac {x_{1}}{x_{1}+\alpha x_{2}}}\ln \mu _{1}+{\frac {\alpha x_{2}}{x_{1}+\alpha x_{2}}}\ln \mu _{2},$

where $\alpha$ is an empirical parameter, and $x_{1,2}$ and $\mu _{1,2}$ are the respective mole fractions and viscosities of the component liquids.

Since blending is an important process in the lubricating and oil industries, a variety of empirical and proprietary equations exist for predicting the viscosity of a blend.

### Solutions and suspensions

#### Aqueous solutions

Depending on the solute and range of concentration, an aqueous electrolyte solution can have either a larger or smaller viscosity compared with pure water at the same temperature and pressure. For instance, a 20% saline (sodium chloride) solution has viscosity over 1.5 times that of pure water, whereas a 20% potassium iodide solution has viscosity about 0.91 times that of pure water.

An idealized model of dilute electrolytic solutions leads to the following prediction for the viscosity $\mu _{s}$ of a solution:

${\frac {\mu _{s}}{\mu _{0}}}=1+A{\sqrt {c}},$

where $\mu _{0}$ is the viscosity of the solvent, c is the concentration, and A is a positive constant which depends on both solvent and solute properties. However, this expression is only valid for very dilute solutions, having c less than 0.1 mol/L. For higher concentrations, additional terms are necessary which account for higher-order molecular correlations:

${\frac {\mu _{s}}{\mu _{0}}}=1+A{\sqrt {c}}+Bc+Cc^{2},$

where B and C are fit from data. In particular, a negative value of B is able to account for the decrease in viscosity observed in some solutions. Estimated values of these constants are shown below for sodium chloride and potassium iodide at temperature 25 °C (mol = mole, L = liter).

| Solute | A (mol−1/2 L1/2) | B (mol−1 L) | C (mol−2 L2) |
|---|---|---|---|
| Sodium chloride (NaCl) | 0.0062 | 0.0793 | 0.0080 |
| Potassium iodide (KI) | 0.0047 | −0.0755 | 0.0000 |

#### Suspensions

In a suspension of solid particles (e.g. micron-size spheres suspended in oil), an effective viscosity $\mu _{\text{eff}}$ can be defined in terms of stress and strain components which are averaged over a volume large compared with the distance between the suspended particles, but small with respect to macroscopic dimensions. Such suspensions generally exhibit non-Newtonian behavior. However, for dilute systems in steady flows, the behavior is Newtonian and expressions for $\mu _{\text{eff}}$ can be derived directly from the particle dynamics. In a very dilute system, with volume fraction $\phi \lesssim 0.02$ , interactions between the suspended particles can be ignored. In such a case one can explicitly calculate the flow field around each particle independently, and combine the results to obtain $\mu _{\text{eff}}$ . For spheres, this results in the Einstein's effective viscosity formula:

$\mu _{\text{eff}}=\mu _{0}\left(1+{\frac {5}{2}}\phi \right),$

where $\mu _{0}$ is the viscosity of the suspending liquid. The linear dependence on $\phi$ is a consequence of neglecting interparticle interactions. For dilute systems in general, one expects $\mu _{\text{eff}}$ to take the form

$\mu _{\text{eff}}=\mu _{0}\left(1+B\phi \right),$

where the coefficient B may depend on the particle shape (e.g. spheres, rods, disks). Experimental determination of the precise value of B is difficult, however: even the prediction $B=5/2$ for spheres has not been conclusively validated, with various experiments finding values in the range $1.5\lesssim B\lesssim 5$ . This deficiency has been attributed to difficulty in controlling experimental conditions.

In denser suspensions, $\mu _{\text{eff}}$ acquires a nonlinear dependence on $\phi$ , which indicates the importance of interparticle interactions. Various analytical and semi-empirical schemes exist for capturing this regime. At the most basic level, a term quadratic in $\phi$ is added to $\mu _{\text{eff}}$ :

$\mu _{\text{eff}}=\mu _{0}\left(1+B\phi +B_{1}\phi ^{2}\right),$

and the coefficient $B_{1}$ is fit from experimental data or approximated from the microscopic theory. However, some authors advise caution in applying such simple formulas since non-Newtonian behavior appears in dense suspensions ( $\phi \gtrsim 0.25$ for spheres), or in suspensions of elongated or flexible particles.

There is a distinction between a suspension of solid particles, described above, and an emulsion. The latter is a suspension of tiny droplets, which themselves may exhibit internal circulation. The presence of internal circulation can decrease the observed effective viscosity, and different theoretical or semi-empirical models must be used.

### Amorphous materials

In the high and low temperature limits, viscous flow in amorphous materials (e.g. in glasses and melts) has the Arrhenius form:

$\mu =Ae^{Q/(RT)},$

where Q is a relevant activation energy, given in terms of molecular parameters; T is temperature; R is the molar gas constant; and A is approximately a constant. The activation energy Q takes a different value depending on whether the high or low temperature limit is being considered: it changes from a high value *Q*H at low temperatures (in the glassy state) to a low value *Q*L at high temperatures (in the liquid state).

For intermediate temperatures, Q varies nontrivially with temperature and the simple Arrhenius form fails. On the other hand, the two-exponential equation

$\mu =AT\exp \left({\frac {B}{RT}}\right)\left[1+C\exp \left({\frac {D}{RT}}\right)\right],$

where A , B , C , D are all constants, provides a good fit to experimental data over the entire range of temperatures, while at the same time reducing to the correct Arrhenius form in the low and high temperature limits. This expression, also known as Duouglas-Doremus-Ojovan model, can be motivated from various theoretical models of amorphous materials at the atomic level.

A two-exponential equation for the viscosity can be derived within the Dyre shoving model of supercooled liquids, where the Arrhenius energy barrier is identified with the high-frequency shear modulus times a characteristic shoving volume. Upon specifying the temperature dependence of the shear modulus via thermal expansion and via the repulsive part of the intermolecular potential, another two-exponential equation is retrieved:

$\mu =\exp {\left\{{\frac {V_{c}C_{G}}{k_{B}T}}\exp {\left[(2+\lambda )\alpha _{T}T_{g}\left(1-{\frac {T}{T_{g}}}\right)\right]}\right\}}$

where $C_{G}$ denotes the high-frequency shear modulus of the material evaluated at a temperature equal to the glass transition temperature $T_{g}$ , $V_{c}$ is the so-called shoving volume, i.e. it is the characteristic volume of the group of atoms involved in the shoving event by which an atom/molecule escapes from the cage of nearest-neighbours, typically on the order of the volume occupied by few atoms. Furthermore, $\alpha _{T}$ is the thermal expansion coefficient of the material, $\lambda$ is a parameter which measures the steepness of the power-law rise of the ascending flank of the first peak of the radial distribution function, and is quantitatively related to the repulsive part of the interatomic potential. Finally, $k_{B}$ denotes the Boltzmann constant.

### Eddy viscosity

In the study of turbulence in fluids, a common practical strategy is to ignore the small-scale vortices (or eddies) in the motion and to calculate a large-scale motion with an *effective* viscosity, called the "eddy viscosity", which characterizes the transport and dissipation of energy in the smaller-scale flow (see large eddy simulation). In contrast to the viscosity of the fluid itself, which must be positive by the second law of thermodynamics, the eddy viscosity can be negative.


## Prediction

Because viscosity depends continuously on temperature and pressure, it cannot be fully characterized by a finite number of experimental measurements. Predictive formulas become necessary if experimental values are not available at the temperatures and pressures of interest. This capability is important for thermophysical simulations, in which the temperature and pressure of a fluid can vary continuously with space and time. A similar situation is encountered for mixtures of pure fluids, where the viscosity depends continuously on the concentration ratios of the constituent fluids

For the simplest fluids, such as dilute monatomic gases and their mixtures, *ab initio* quantum mechanical computations can accurately predict viscosity in terms of fundamental atomic constants, i.e., without reference to existing viscosity measurements. For the special case of dilute helium, uncertainties in the *ab initio* calculated viscosity are two order of magnitudes smaller than uncertainties in experimental values.

For slightly more complex fluids and mixtures at moderate densities (i.e. sub-critical densities) Revised Enskog Theory can be used to predict viscosities with some accuracy. Revised Enskog Theory is predictive in the sense that predictions for viscosity can be obtained using parameters fitted to other, pure-fluid thermodynamic properties or transport properties, thus requiring no *a priori* experimental viscosity measurements.

For most fluids, high-accuracy, first-principles computations are not feasible. Rather, theoretical or empirical expressions must be fit to existing viscosity measurements. If such an expression is fit to high-fidelity data over a large range of temperatures and pressures, then it is called a "reference correlation" for that fluid. Reference correlations have been published for many pure fluids; a few examples are water, carbon dioxide, ammonia, benzene, and xenon. Many of these cover temperature and pressure ranges that encompass gas, liquid, and supercritical phases.

Thermophysical modeling software often relies on reference correlations for predicting viscosity at user-specified temperature and pressure. These correlations may be proprietary. Examples are REFPROP (proprietary) and CoolProp (open-source).

Viscosity can also be computed using formulas that express it in terms of the statistics of individual particle trajectories. These formulas include the Green–Kubo relations for the linear shear viscosity and the *transient time correlation function* expressions derived by Evans and Morriss in 1988. The advantage of these expressions is that they are formally exact and valid for general systems. The disadvantage is that they require detailed knowledge of particle trajectories, available only in computationally expensive simulations such as molecular dynamics. An accurate model for interparticle interactions is also required, which may be difficult to obtain for complex molecules.
