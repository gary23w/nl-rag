---
title: "Acoustic theory"
source: https://en.wikipedia.org/wiki/Acoustic_theory
domain: momentum
license: CC-BY-SA-4.0
tags: momentum
fetched: 2026-07-05
---

# Acoustic theory

**Acoustic theory** is a scientific field that relates to the description of sound waves. It derives from fluid dynamics. See acoustics for the engineering approach.

For sound waves of any magnitude of a disturbance in velocity, pressure, and density we have

${\begin{aligned}{\frac {\partial \rho '}{\partial t}}+\rho _{0}\nabla \cdot \mathbf {v} +\nabla \cdot (\rho '\mathbf {v} )&=0\qquad {\text{(Conservation of Mass)}}\\(\rho _{0}+\rho '){\frac {\partial \mathbf {v} }{\partial t}}+(\rho _{0}+\rho ')(\mathbf {v} \cdot \nabla )\mathbf {v} +\nabla p'&=0\qquad {\text{(Equation of Motion)}}\end{aligned}}$

In the case that the fluctuations in velocity, density, and pressure are small, we can approximate these as

${\begin{aligned}{\frac {\partial \rho '}{\partial t}}+\rho _{0}\nabla \cdot \mathbf {v} &=0\\{\frac {\partial \mathbf {v} }{\partial t}}+{\frac {1}{\rho _{0}}}\nabla p'&=0\end{aligned}}$

Where $\mathbf {v} (\mathbf {x} ,t)$ is the perturbed velocity of the fluid, $p_{0}$ is the pressure of the fluid at rest, $p'(\mathbf {x} ,t)$ is the perturbed pressure of the system as a function of space and time, $\rho _{0}$ is the density of the fluid at rest, and $\rho '(\mathbf {x} ,t)$ is the variance in the density of the fluid over space and time.

In the case that the velocity is irrotational ( $\nabla \times \mathbf {v} =0$ ), we then have the acoustic wave equation that describes the system:

${\frac {1}{c^{2}}}{\frac {\partial ^{2}\phi }{\partial t^{2}}}-\nabla ^{2}\phi =0$

Where we have

${\begin{aligned}\mathbf {v} &=-\nabla \phi \\c^{2}&=({\frac {\partial p}{\partial \rho }})_{s}\\p'&=\rho _{0}{\frac {\partial \phi }{\partial t}}\\\rho '&={\frac {\rho _{0}}{c^{2}}}{\frac {\partial \phi }{\partial t}}\end{aligned}}$

## Derivation for a medium at rest

Starting with the Continuity Equation and the Euler Equation:

${\begin{aligned}{\frac {\partial \rho }{\partial t}}+\nabla \cdot \rho \mathbf {v} &=0\\\rho {\frac {\partial \mathbf {v} }{\partial t}}+\rho (\mathbf {v} \cdot \nabla )\mathbf {v} +\nabla p&=0\end{aligned}}$

If we take small perturbations of a constant pressure and density:

${\begin{aligned}\rho &=\rho _{0}+\rho '\\p&=p_{0}+p'\end{aligned}}$

Then the equations of the system are

${\begin{aligned}{\frac {\partial }{\partial t}}(\rho _{0}+\rho ')+\nabla \cdot (\rho _{0}+\rho ')\mathbf {v} &=0\\(\rho _{0}+\rho '){\frac {\partial \mathbf {v} }{\partial t}}+(\rho _{0}+\rho ')(\mathbf {v} \cdot \nabla )\mathbf {v} +\nabla (p_{0}+p')&=0\end{aligned}}$

Noting that the equilibrium pressures and densities are constant, this simplifies to

${\begin{aligned}{\frac {\partial \rho '}{\partial t}}+\rho _{0}\nabla \cdot \mathbf {v} +\nabla \cdot \rho '\mathbf {v} &=0\\(\rho _{0}+\rho '){\frac {\partial \mathbf {v} }{\partial t}}+(\rho _{0}+\rho ')(\mathbf {v} \cdot \nabla )\mathbf {v} +\nabla p'&=0\end{aligned}}$

### A Moving Medium

Starting with

${\begin{aligned}{\frac {\partial \rho '}{\partial t}}+\rho _{0}\nabla \cdot \mathbf {w} +\nabla \cdot \rho '\mathbf {w} &=0\\(\rho _{0}+\rho '){\frac {\partial \mathbf {w} }{\partial t}}+(\rho _{0}+\rho ')(\mathbf {w} \cdot \nabla )\mathbf {w} +\nabla p'&=0\end{aligned}}$

We can have these equations work for a moving medium by setting $\mathbf {w} =\mathbf {u} +\mathbf {v}$ , where $\mathbf {u}$ is the constant velocity that the whole fluid is moving at before being disturbed (equivalent to a moving observer) and $\mathbf {v}$ is the fluid velocity.

In this case the equations look very similar:

${\begin{aligned}{\frac {\partial \rho '}{\partial t}}+\rho _{0}\nabla \cdot \mathbf {v} +\mathbf {u} \cdot \nabla \rho '+\nabla \cdot \rho '\mathbf {v} &=0\\(\rho _{0}+\rho '){\frac {\partial \mathbf {v} }{\partial t}}+(\rho _{0}+\rho ')(\mathbf {u} \cdot \nabla )\mathbf {v} +(\rho _{0}+\rho ')(\mathbf {v} \cdot \nabla )\mathbf {v} +\nabla p'&=0\end{aligned}}$

Note that setting $\mathbf {u} =0$ returns the equations at rest.

## Linearized Waves

Starting with the above given equations of motion for a medium at rest:

${\begin{aligned}{\frac {\partial \rho '}{\partial t}}+\rho _{0}\nabla \cdot \mathbf {v} +\nabla \cdot \rho '\mathbf {v} &=0\\(\rho _{0}+\rho '){\frac {\partial \mathbf {v} }{\partial t}}+(\rho _{0}+\rho ')(\mathbf {v} \cdot \nabla )\mathbf {v} +\nabla p'&=0\end{aligned}}$

Let us now take $\mathbf {v} ,\rho ',p'$ to all be small quantities.

In the case that we keep terms to first order, for the continuity equation, we have the $\rho '\mathbf {v}$ term going to 0. This similarly applies for the density perturbation times the time derivative of the velocity. Moreover, the spatial components of the material derivative go to 0. We thus have, upon rearranging the equilibrium density:

${\begin{aligned}{\frac {\partial \rho '}{\partial t}}+\rho _{0}\nabla \cdot \mathbf {v} &=0\\{\frac {\partial \mathbf {v} }{\partial t}}+{\frac {1}{\rho _{0}}}\nabla p'&=0\end{aligned}}$

Next, given that our sound wave occurs in an ideal fluid, the motion is adiabatic, and then we can relate the small change in the pressure to the small change in the density by

$p'=\left({\frac {\partial p}{\partial \rho _{0}}}\right)_{s}\rho '$

Under this condition, we see that we now have

${\begin{aligned}{\frac {\partial p'}{\partial t}}+\rho _{0}\left({\frac {\partial p}{\partial \rho _{0}}}\right)_{s}\nabla \cdot \mathbf {v} &=0\\{\frac {\partial \mathbf {v} }{\partial t}}+{\frac {1}{\rho _{0}}}\nabla p'&=0\end{aligned}}$

Defining the speed of sound of the system:

$c\equiv {\sqrt {\left({\frac {\partial p}{\partial \rho _{0}}}\right)_{s}}}$

Everything becomes

${\begin{aligned}{\frac {\partial p'}{\partial t}}+\rho _{0}c^{2}\nabla \cdot \mathbf {v} &=0\\{\frac {\partial \mathbf {v} }{\partial t}}+{\frac {1}{\rho _{0}}}\nabla p'&=0\end{aligned}}$

### For Irrotational Fluids

In the case that the fluid is irrotational, that is $\nabla \times \mathbf {v} =0$ , we can then write $\mathbf {v} =-\nabla \phi$ and thus write our equations of motion as

${\begin{aligned}{\frac {\partial p'}{\partial t}}-\rho _{0}c^{2}\nabla ^{2}\phi &=0\\-\nabla {\frac {\partial \phi }{\partial t}}+{\frac {1}{\rho _{0}}}\nabla p'&=0\end{aligned}}$

The second equation tells us that

$p'=\rho _{0}{\frac {\partial \phi }{\partial t}}$

And the use of this equation in the continuity equation tells us that

$\rho _{0}{\frac {\partial ^{2}\phi }{\partial t}}-\rho _{0}c^{2}\nabla ^{2}\phi =0$

This simplifies to

${\frac {1}{c^{2}}}{\frac {\partial ^{2}\phi }{\partial t^{2}}}-\nabla ^{2}\phi =0$

Thus the velocity potential $\phi$ obeys the wave equation in the limit of small disturbances. The boundary conditions required to solve for the potential come from the fact that the velocity of the fluid must be 0 normal to the fixed surfaces of the system.

Taking the time derivative of this wave equation and multiplying all sides by the unperturbed density, and then using the fact that $p'=\rho _{0}{\frac {\partial \phi }{\partial t}}$ tells us that

${\frac {1}{c^{2}}}{\frac {\partial ^{2}p'}{\partial t^{2}}}-\nabla ^{2}p'=0$

Similarly, we saw that $p'=\left({\frac {\partial p}{\partial \rho _{0}}}\right)_{s}\rho '=c^{2}\rho '$ . Thus we can multiply the above equation appropriately and see that

${\frac {1}{c^{2}}}{\frac {\partial ^{2}\rho '}{\partial t^{2}}}-\nabla ^{2}\rho '=0$

Thus, the velocity potential, pressure, and density all obey the wave equation. Moreover, we only need to solve one such equation to determine all other three. In particular, we have

${\begin{aligned}\mathbf {v} &=-\nabla \phi \\p'&=\rho _{0}{\frac {\partial \phi }{\partial t}}\\\rho '&={\frac {\rho _{0}}{c^{2}}}{\frac {\partial \phi }{\partial t}}\end{aligned}}$

### For a moving medium

Again, we can derive the small-disturbance limit for sound waves in a moving medium. Again, starting with

${\begin{aligned}{\frac {\partial \rho '}{\partial t}}+\rho _{0}\nabla \cdot \mathbf {v} +\mathbf {u} \cdot \nabla \rho '+\nabla \cdot \rho '\mathbf {v} &=0\\(\rho _{0}+\rho '){\frac {\partial \mathbf {v} }{\partial t}}+(\rho _{0}+\rho ')(\mathbf {u} \cdot \nabla )\mathbf {v} +(\rho _{0}+\rho ')(\mathbf {v} \cdot \nabla )\mathbf {v} +\nabla p'&=0\end{aligned}}$

We can linearize these into

${\begin{aligned}{\frac {\partial \rho '}{\partial t}}+\rho _{0}\nabla \cdot \mathbf {v} +\mathbf {u} \cdot \nabla \rho '&=0\\{\frac {\partial \mathbf {v} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {v} +{\frac {1}{\rho _{0}}}\nabla p'&=0\end{aligned}}$

#### For Irrotational Fluids in a Moving Medium

Given that we saw that

${\begin{aligned}{\frac {\partial \rho '}{\partial t}}+\rho _{0}\nabla \cdot \mathbf {v} +\mathbf {u} \cdot \nabla \rho '&=0\\{\frac {\partial \mathbf {v} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {v} +{\frac {1}{\rho _{0}}}\nabla p'&=0\end{aligned}}$

If we make the previous assumptions of the fluid being ideal and the velocity being irrotational, then we have

${\begin{aligned}p'&=\left({\frac {\partial p}{\partial \rho _{0}}}\right)_{s}\rho '=c^{2}\rho '\\\mathbf {v} &=-\nabla \phi \end{aligned}}$

Under these assumptions, our linearized sound equations become

${\begin{aligned}{\frac {1}{c^{2}}}{\frac {\partial p'}{\partial t}}-\rho _{0}\nabla ^{2}\phi +{\frac {1}{c^{2}}}\mathbf {u} \cdot \nabla p'&=0\\-{\frac {\partial }{\partial t}}(\nabla \phi )-(\mathbf {u} \cdot \nabla )[\nabla \phi ]+{\frac {1}{\rho _{0}}}\nabla p'&=0\end{aligned}}$

Importantly, since $\mathbf {u}$ is a constant, we have $(\mathbf {u} \cdot \nabla )[\nabla \phi ]=\nabla [(\mathbf {u} \cdot \nabla )\phi ]$ , and then the second equation tells us that

${\frac {1}{\rho _{0}}}\nabla p'=\nabla \left[{\frac {\partial \phi }{\partial t}}+(\mathbf {u} \cdot \nabla )\phi \right]$

Or just that

$p'=\rho _{0}\left[{\frac {\partial \phi }{\partial t}}+(\mathbf {u} \cdot \nabla )\phi \right]$

Now, when we use this relation with the fact that ${\frac {1}{c^{2}}}{\frac {\partial p'}{\partial t}}-\rho _{0}\nabla ^{2}\phi +{\frac {1}{c^{2}}}\mathbf {u} \cdot \nabla p'=0$ , alongside cancelling and rearranging terms, we arrive at

${\frac {1}{c^{2}}}{\frac {\partial ^{2}\phi }{\partial t^{2}}}-\nabla ^{2}\phi +{\frac {1}{c^{2}}}{\frac {\partial }{\partial t}}[(\mathbf {u} \cdot \nabla )\phi ]+{\frac {1}{c^{2}}}{\frac {\partial }{\partial t}}(\mathbf {u} \cdot \nabla \phi )+{\frac {1}{c^{2}}}\mathbf {u} \cdot \nabla [(\mathbf {u} \cdot \nabla )\phi ]=0$

We can write this in a familiar form as

$\left[{\frac {1}{c^{2}}}\left({\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla \right)^{2}-\nabla ^{2}\right]\phi =0$

This differential equation must be solved with the appropriate boundary conditions. Note that setting $\mathbf {u} =0$ returns us the wave equation. Regardless, upon solving this equation for a moving medium, we then have

${\begin{aligned}\mathbf {v} &=-\nabla \phi \\p'&=\rho _{0}\left({\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla \right)\phi \\\rho '&={\frac {\rho _{0}}{c^{2}}}\left({\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla \right)\phi \end{aligned}}$
