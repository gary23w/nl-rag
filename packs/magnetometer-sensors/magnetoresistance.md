---
title: "Magnetoresistance"
source: https://en.wikipedia.org/wiki/Magnetoresistance
domain: magnetometer-sensors
license: CC-BY-SA-4.0
tags: magnetometer sensor, hall effect, magnetoresistance, fluxgate magnetometer
fetched: 2026-07-02
---

# Magnetoresistance

**Magnetoresistance** is the tendency of a material (often ferromagnetic) to change the value of its electrical resistance in an externally-applied magnetic field. There are a variety of effects that can be called magnetoresistance. Some occur in bulk non-magnetic metals and semiconductors, such as geometrical magnetoresistance, Shubnikov–de Haas oscillations, or the common positive magnetoresistance in metals. Other effects occur in magnetic metals, such as negative magnetoresistance in ferromagnets or anisotropic magnetoresistance (AMR). Finally, in multicomponent or multilayer systems (e.g. magnetic tunnel junctions), giant magnetoresistance (GMR), tunnel magnetoresistance (TMR), colossal magnetoresistance (CMR), and extraordinary magnetoresistance (EMR) can be observed.

The first magnetoresistive effect was discovered in 1856 by William Thomson, better known as Lord Kelvin, but he was unable to lower the electrical resistance of anything by more than 5%. Today, systems including semimetals and concentric ring EMR structures are known. In these, a magnetic field can adjust the resistance by orders of magnitude. Since different mechanisms can alter the resistance, it is useful to separately consider situations where it depends on a magnetic field directly (e.g. geometric magnetoresistance and multiband magnetoresistance) and those where it does so indirectly through magnetization (e.g. AMR and TMR).

## Discovery

William Thomson (Lord Kelvin) first discovered ordinary magnetoresistance in 1856. He experimented with pieces of iron and discovered that the resistance increases when the current is in the same direction as the magnetic force and decreases when the current is at 90° to the magnetic force. He then did the same experiment with nickel and found that it was affected in the same way but the magnitude of the effect was greater. This effect is referred to as anisotropic magnetoresistance (AMR).

In 2007, Albert Fert and Peter Grünberg were jointly awarded the Nobel Prize for the discovery of giant magnetoresistance.

## Geometrical magnetoresistance

An example of magnetoresistance due to direct action of magnetic field on electric current can be studied on a Corbino disc (see Figure). It consists of a conducting annulus with perfectly conducting rims. Without a magnetic field, the battery drives a radial current between the rims. When a magnetic field perpendicular to the plane of the annulus is applied, (either into or out of the page) a circular component of current flows as well, due to Lorentz force. Initial interest in this problem began with Boltzmann in 1886, and independently was re-examined by Corbino in 1911.

In a simple model, supposing the response to the Lorentz force is the same as for an electric field, the carrier velocity **v** is given by: $\mathbf {v} =\mu \left(\mathbf {E} +\mathbf {v\times B} \right),$ where μ is the carrier mobility. Solving for the velocity, we find:

${\begin{aligned}\mathbf {v} &={\frac {\mu }{1+(\mu B)^{2}}}\left(\mathbf {E} +\mu \mathbf {E\times B} +\mu ^{2}(\mathbf {B\cdot E} )\mathbf {B} \right)\\&={\frac {\mu }{1+(\mu B)^{2}}}\left(\mathbf {E} _{\perp }+\mu \mathbf {E\times B} \right)+\mu \mathbf {E} _{\parallel }\,\end{aligned}}$

where the effective reduction in mobility due to the **B**-field (for motion perpendicular to this field) is apparent. Electric current (proportional to the radial component of velocity) will decrease with increasing magnetic field and hence the resistance of the device will increase. Critically, this magnetoresistive scenario depends sensitively on the device geometry and current lines and it does not rely on magnetic materials.

In a semiconductor with a single carrier type, the magnetoresistance is proportional to (1 + (*μB*)2), where μ is the semiconductor mobility (units m2·V−1·s−1, equivalently m2·Wb−1, or T −1) and B is the magnetic field (units teslas). Indium antimonide, an example of a high mobility semiconductor, could have an electron mobility above 4 m2/Wb at 300 K. So in a 0.25 T field, for example the magnetoresistance increase would be 100%.

## Anisotropic magnetoresistance (AMR)

Thomson's experiments are an example of AMR, a property of a material in which a dependence of electrical resistance on the angle between the direction of electric current and direction of **magnetization** is observed. The effect arises in most cases from the simultaneous action of magnetization and spin–orbit interaction (exceptions related to non-collinear magnetic order notwithstanding) and its detailed mechanism depends on the material. It can be for example due to a larger probability of s-d scattering of electrons in the direction of magnetization (which is controlled by the applied magnetic field). The net effect (in most materials) is that the electrical resistance has maximum value when the direction of current is parallel to the applied magnetic field. AMR of new materials is being investigated and magnitudes up to 50% have been observed in some uranium (but otherwise quite conventional) ferromagnetic compounds. Materials with extreme AMR have been identified driven by unconventional mechanisms such as a metal-insulator transition triggered by rotating the magnetic moments (while for some directions of magnetic moments, the system is semimetallic, for other directions a gap opens).

In polycrystalline ferromagnetic materials, the AMR can only depend on the angle *φ* = *ψ* − *θ* between the magnetization and current direction and (as long as the resistivity of the material can be described by a rank-two tensor), it must follow $\rho (\varphi )=\rho _{\perp }+(\rho _{\parallel }-\rho _{\perp })\cos ^{2}\varphi$ where ρ is the (longitudinal) resistivity of the film and *ρ*∥,⟂ are the resistivities for *φ* = 0° and *φ* = 90°, respectively. Associated with longitudinal resistivity, there is also transversal resistivity dubbed (somewhat confusingly) the planar Hall effect. In monocrystals, resistivity ρ depends also on ψ and θ individually.

To compensate for the non-linear characteristics and inability to detect the polarity of a magnetic field, the following structure is used for sensors. It consists of stripes of aluminum or gold placed on a thin film of permalloy (a ferromagnetic material exhibiting the AMR effect) inclined at an angle of 45°. This structure forces the current not to flow along the "easy axes" of thin film, but at an angle of 45°. The dependence of resistance now has a permanent offset which is linear around the null point. Because of its appearance, this sensor type is called 'barber pole'.

The AMR effect is used in a wide array of sensors for measurement of Earth's magnetic field (electronic compass), for electric current measuring (by measuring the magnetic field created around the conductor), for traffic detection and for linear position and angle sensing. The biggest AMR sensor manufacturers are Honeywell, NXP Semiconductors, STMicroelectronics, and Sensitec GmbH.

As theoretical aspects, I. A. Campbell, A. Fert, and O. Jaoul (*CFJ*) derived an expression of the AMR ratio for Ni-based alloys using the two-current model with s-s and s-d scattering processes, where 's' is a conduction electron, and 'd' is 3d states with the spin-orbit interaction. The AMR ratio is expressed as ${\frac {\Delta \rho }{\rho }}={\frac {\rho _{\parallel }-\rho _{\perp }}{\rho _{\perp }}}=\gamma (\alpha -1),$ with $\gamma =(3/4)(A/H)^{2}$ and $\alpha =\rho _{\downarrow }/\rho _{\uparrow }$ , where A , H , and $\rho _{\sigma }$ are a spin-orbit coupling constant (so-called $\zeta$ ), an exchange field, and a resistivity for spin $\sigma$ , respectively. In addition, recently, Satoshi Kokado et al. have obtained the general expression of the AMR ratio for 3d transition-metal ferromagnets by extending the CFJ theory to a more general one. The general expression can also be applied to half-metals.
