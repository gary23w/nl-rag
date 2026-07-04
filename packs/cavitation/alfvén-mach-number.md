---
title: "Alfvén Mach number"
source: https://en.wikipedia.org/wiki/Alfv%C3%A9n_Mach_number
domain: cavitation
license: CC-BY-SA-4.0
tags: cavitation
fetched: 2026-07-04
---

# Alfvén Mach number

The **Alfvén Mach number** (also known as the **Alfvén number**, **Alfvénic Mach number**, and **magnetic Mach number**; **MA** or **MM**) is a dimensionless quantity representing the ratio of the relative velocity of a fluid to the local Alfvén speed. It is used in plasma physics, where it is analogous to the Mach number but based on Alfvén waves rather than sound waves. Alfvén and Mach were physicists who studied shock waves.

Along with the sonic Mach number, the Alfvén Mach number is frequently used to characterize shock fronts and turbulence in magnetized plasmas. $\mathrm {M_{A}} ={\frac {u}{u_{\mathrm {A} }}}$ where

- MA is the Alfvén Mach number,
- u is the flow velocity, and
- uA is the Alfvén speed.

When *u* < MA, the flow is referred to as *sub-Alfvénic*; and when *u* > MA, the flow is referred to as *super-Alfvénic*.

## Derivation from the magnetohydrodynamics momentum equation

Ignoring viscosity and external body forces, the momentum equation for magnetohydrodynamics (MHD) is: $\rho \left({\frac {\partial \mathbf {v} }{\partial t}}+\mathbf {v} \cdot \nabla \mathbf {v} \right)=-\nabla p+\mathbf {J} \times \mathbf {B}$ where $\mathbf {J} \times \mathbf {B}$ is the Lorentz force. Using the low-frequency form of Ampère's law $\mu _{0}\mathbf {J} =\nabla \times \mathbf {B}$ , which neglects the displacement current, the momentum equation becomes: $\rho \left({\frac {\partial \mathbf {v} }{\partial t}}+\mathbf {v} \cdot \nabla \mathbf {v} \right)=-\nabla p+{\frac {1}{\mu _{0}}}\left(\nabla \times \mathbf {B} \right)\times \mathbf {B}$ We may nondimensionalize the momentum equation by introducing the nondimensional variables: $\mathbf {v} =U{\widehat {\mathbf {v} }},\quad \mathbf {x} =L{\widehat {\mathbf {x} }},\quad \mathbf {B} =B{\widehat {\mathbf {B} }},\quad \rho =\rho _{0}{\widehat {\rho }},\quad t={\frac {L}{U}}\tau$ where U is the characteristic velocity, L is the characteristic length, B is the characteristic magnetic field strength, and $\rho _{0}$ is the characteristic mass density. Therefore, the inertial and Lorentz terms in the momentum equation respectively scale as: $\rho \mathbf {v} \cdot \nabla \mathbf {v} \sim {\frac {\rho _{0}U^{2}}{L}},\quad {\frac {1}{\mu _{0}}}\left(\nabla \times \mathbf {B} \right)\times \mathbf {B} \sim {\frac {B^{2}}{\mu _{0}L}}\implies {\frac {\rho \mathbf {v} \cdot \nabla \mathbf {v} }{{\frac {1}{\mu _{0}}}\left(\nabla \times \mathbf {B} \right)\times \mathbf {B} }}\sim {\frac {U^{2}}{B^{2}/\mu _{0}\rho _{0}}}$ Recognizing that the Alfvén speed $u_{\mathrm {A} }=B/{\sqrt {\mu _{0}\rho _{0}}}$ , we may see that this quantity is the square of the Alfvén Mach number $\mathrm {M_{A}} =U/u_{\mathrm {A} }$ . Hence, the Alfvén Mach number naturally arises from comparing the inertial and magnetic terms in the MHD momentum equation, and expresses the ratio of inertial to magnetic forces in a plasma.
