---
title: "Electromagnetic wave equation"
source: https://en.wikipedia.org/wiki/Electromagnetic_wave_equation
domain: maxwell-equations
license: CC-BY-SA-4.0
tags: maxwell's equations, gauss's law, displacement current, electromagnetic wave equation
fetched: 2026-07-02
---

# Electromagnetic wave equation

The **electromagnetic wave equation** is a second-order partial differential equation that describes the propagation of electromagnetic waves through a medium or in a vacuum. It is a three-dimensional form of the wave equation. The homogeneous form of the equation, written in terms of either the electric field **E** or the magnetic field **B**, takes the form:

${\begin{aligned}\left(v_{\mathrm {ph} }^{2}\nabla ^{2}-{\frac {\partial ^{2}}{\partial t^{2}}}\right)\mathbf {E} &=\mathbf {0} \\\left(v_{\mathrm {ph} }^{2}\nabla ^{2}-{\frac {\partial ^{2}}{\partial t^{2}}}\right)\mathbf {B} &=\mathbf {0} \end{aligned}}$

where

$v_{\mathrm {ph} }={\frac {1}{\sqrt {\mu \varepsilon }}}$

is the speed of light (i.e. phase velocity) in a medium with permeability μ, and permittivity ε, and ∇2 is the Laplace operator. In a vacuum, *v*ph = *c*0 = 299792458 m/s, a fundamental physical constant. The electromagnetic wave equation derives from Maxwell's equations. In most older literature, **B** is called the *magnetic flux density* or *magnetic induction*. The following equations ${\begin{aligned}\nabla \cdot \mathbf {E} &=0\\\nabla \cdot \mathbf {B} &=0\end{aligned}}$ predicate that any electromagnetic wave must be a transverse wave, where the electric field **E** and the magnetic field **B** are both perpendicular to the direction of wave propagation.

## The origin of the electromagnetic wave equation

In his 1865 paper titled A Dynamical Theory of the Electromagnetic Field, James Clerk Maxwell utilized the correction to Ampère's circuital law that he had made in part III of his 1861 paper On Physical Lines of Force. In *Part VI* of his 1864 paper titled *Electromagnetic Theory of Light*, Maxwell combined displacement current with some of the other equations of electromagnetism and he obtained a wave equation with a speed equal to the speed of light. He commented:

> The agreement of the results seems to show that light and magnetism are affections of the same substance, and that light is an electromagnetic disturbance propagated through the field according to electromagnetic laws.

Maxwell's derivation of the electromagnetic wave equation has been replaced in modern physics education by a much less cumbersome method involving combining the corrected version of Ampère's circuital law with Faraday's law of induction.

To obtain the electromagnetic wave equation in a vacuum using the modern method, we begin with the modern '**Heaviside' form of Maxwell's equations**. In a vacuum- and charge-free space, these equations are:

${\begin{aligned}\nabla \cdot \mathbf {E} &=0\\\nabla \times \mathbf {E} &=-{\frac {\partial \mathbf {B} }{\partial t}}\\\nabla \cdot \mathbf {B} &=0\\\nabla \times \mathbf {B} &=\mu _{0}\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}\\\end{aligned}}$

These are the general Maxwell's equations specialized to the case with charge and current both set to zero. Taking the curl of the curl equations gives:

${\begin{aligned}\nabla \times \left(\nabla \times \mathbf {E} \right)&=\nabla \times \left(-{\frac {\partial \mathbf {B} }{\partial t}}\right)=-{\frac {\partial }{\partial t}}\left(\nabla \times \mathbf {B} \right)=-\mu _{0}\varepsilon _{0}{\frac {\partial ^{2}\mathbf {E} }{\partial t^{2}}}\\\nabla \times \left(\nabla \times \mathbf {B} \right)&=\nabla \times \left(\mu _{0}\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}\right)=\mu _{0}\varepsilon _{0}{\frac {\partial }{\partial t}}\left(\nabla \times \mathbf {E} \right)=-\mu _{0}\varepsilon _{0}{\frac {\partial ^{2}\mathbf {B} }{\partial t^{2}}}\end{aligned}}$

We can use the vector identity

$\nabla \times \left(\nabla \times \mathbf {V} \right)=\nabla \left(\nabla \cdot \mathbf {V} \right)-\nabla ^{2}\mathbf {V}$

where **V** is any vector function of space. And

$\nabla ^{2}\mathbf {V} =\nabla \cdot \left(\nabla \mathbf {V} \right)$

where ∇**V** is a dyadic which when operated on by the divergence operator ∇ ⋅ yields a vector. Since

${\begin{aligned}\nabla \cdot \mathbf {E} &=0\\\nabla \cdot \mathbf {B} &=0\end{aligned}}$

then the first term on the right in the identity vanishes and we obtain the wave equations:

${\begin{aligned}{\frac {1}{c_{0}^{2}}}{\frac {\partial ^{2}\mathbf {E} }{\partial t^{2}}}-\nabla ^{2}\mathbf {E} &=\mathbf {0} \\{\frac {1}{c_{0}^{2}}}{\frac {\partial ^{2}\mathbf {B} }{\partial t^{2}}}-\nabla ^{2}\mathbf {B} &=\mathbf {0} \end{aligned}}$

where

$c_{0}={\frac {1}{\sqrt {\mu _{0}\varepsilon _{0}}}}=2.99792458\times 10^{8}\;{\textrm {m/s}}$

is the speed of light in free space.

## Covariant form of the homogeneous wave equation

These relativistic equations can be written in contravariant form as

$\Box A^{\mu }=0$

where the electromagnetic four-potential is

$A^{\mu }=\left({\frac {\phi }{c}},\mathbf {A} \right)$

with the Lorenz gauge condition:

$\partial _{\mu }A^{\mu }=0,$

and where

$\Box =\nabla ^{2}-{\frac {1}{c^{2}}}{\frac {\partial ^{2}}{\partial t^{2}}}$

is the d'Alembert operator.

## Homogeneous wave equation in curved spacetime

The electromagnetic wave equation is modified in two ways, the derivative is replaced with the covariant derivative and a new term that depends on the curvature appears.

$-{A^{\alpha ;\beta }}_{;\beta }+{R^{\alpha }}_{\beta }A^{\beta }=0$

where ${R^{\alpha }}_{\beta }$ is the Ricci curvature tensor and the semicolon indicates covariant differentiation.

The generalization of the Lorenz gauge condition in curved spacetime is assumed:

${A^{\mu }}_{;\mu }=0.$

## Inhomogeneous electromagnetic wave equation

Localized time-varying charge and current densities can act as sources of electromagnetic waves in a vacuum. Maxwell's equations can be written in the form of a wave equation with sources. The addition of sources to the wave equations makes the partial differential equations inhomogeneous.

## Solutions to the homogeneous electromagnetic wave equation

The general solution to the electromagnetic wave equation is a linear superposition of waves of the form

${\begin{aligned}\mathbf {E} (\mathbf {r} ,t)&=g(\phi (\mathbf {r} ,t))=g(\omega t-\mathbf {k} \cdot \mathbf {r} )\\\mathbf {B} (\mathbf {r} ,t)&=g(\phi (\mathbf {r} ,t))=g(\omega t-\mathbf {k} \cdot \mathbf {r} )\end{aligned}}$

for virtually *any* well-behaved function g of dimensionless argument φ, where ω is the angular frequency (in radians per second), and **k** = (*kx*, *ky*, *kz*) is the wave vector (in radians per meter).

Although the function g can be and often is a monochromatic sine wave, it does not have to be sinusoidal, or even periodic. In practice, g cannot have infinite periodicity because any real electromagnetic wave must always have a finite extent in time and space. As a result, and based on the theory of Fourier decomposition, a real wave must consist of the superposition of an infinite set of sinusoidal frequencies.

In addition, for a valid solution, the wave vector and the angular frequency are not independent; they must adhere to the dispersion relation:

$k=|\mathbf {k} |={\omega \over c}={2\pi \over \lambda }$

where k is the wavenumber and λ is the wavelength. The variable c can only be used in this equation when the electromagnetic wave is in a vacuum.

### Monochromatic, sinusoidal steady-state

The simplest set of solutions to the wave equation result from assuming sinusoidal waveforms of a single frequency in separable form:

$\mathbf {E} (\mathbf {r} ,t)=\Re \left\{\mathbf {E} (\mathbf {r} )e^{i\omega t}\right\}$

where

- i is the imaginary unit,
- *ω* = 2*π* *f*  is the angular frequency in radians per second,
- *f*  is the frequency in hertz, and
- $e^{i\omega t}=\cos(\omega t)+i\sin(\omega t)$ is Euler's formula.

### Plane wave solutions

Consider a plane defined by a unit normal vector

$\mathbf {n} ={\mathbf {k} \over k}.$

Then planar traveling wave solutions of the wave equations are

${\begin{aligned}\mathbf {E} (\mathbf {r} )&=\mathbf {E} _{0}e^{-i\mathbf {k} \cdot \mathbf {r} }\\\mathbf {B} (\mathbf {r} )&=\mathbf {B} _{0}e^{-i\mathbf {k} \cdot \mathbf {r} }\end{aligned}}$

where **r** = (*x*, *y*, *z*) is the position vector (in meters).

These solutions represent planar waves traveling in the direction of the normal vector **n**. If we define the z direction as the direction of **n**, and the x direction as the direction of **E**, then the magnetic field lies in the y direction and is related to the electric field by the relation

$c^{2}{\partial B \over \partial z}={\partial E \over \partial t}.$

Because the divergence of the electric and magnetic fields are zero, there are no fields in the direction of propagation.

This solution is the linearly polarized solution of the wave equations. There are also circularly polarized solutions in which the fields rotate about the normal vector.

### Spectral decomposition

Because of the linearity of Maxwell's equations in a vacuum, solutions can be decomposed into a superposition of sinusoids. This is the basis for the Fourier transform method for the solution of differential equations. The sinusoidal solution to the electromagnetic wave equation takes the form

${\begin{aligned}\mathbf {E} (\mathbf {r} ,t)&=\mathbf {E} _{0}\cos(\omega t-\mathbf {k} \cdot \mathbf {r} +\phi _{0})\\\mathbf {B} (\mathbf {r} ,t)&=\mathbf {B} _{0}\cos(\omega t-\mathbf {k} \cdot \mathbf {r} +\phi _{0})\end{aligned}}$

where

- t is time (in seconds),
- ω is the angular frequency (in radians per second),
- **k** = (*kx*, *ky*, *kz*) is the wave vector (in radians per meter), and
- $\phi _{0}$ is the phase angle (in radians).

The wave vector is related to the angular frequency by

$k=|\mathbf {k} |={\omega \over c}={2\pi \over \lambda }$

where k is the wavenumber and λ is the wavelength.

The electromagnetic spectrum is a plot of the field magnitudes (or energies) as a function of wavelength.

### Multipole expansion

Assuming monochromatic fields varying in time as $e^{-i\omega t}$ , if one uses Maxwell's Equations to eliminate **B**, the electromagnetic wave equation reduces to the Helmholtz equation for **E**:

$(\nabla ^{2}+k^{2})\mathbf {E} =0,\,\mathbf {B} =-{\frac {i}{k}}\nabla \times \mathbf {E} ,$

with *k* = *ω*/*c* as given above. Alternatively, one can eliminate **E** in favor of **B** to obtain:

$(\nabla ^{2}+k^{2})\mathbf {B} =0,\,\mathbf {E} =-{\frac {i}{k}}\nabla \times \mathbf {B} .$

A generic electromagnetic field with frequency ω can be written as a sum of solutions to these two equations. The three-dimensional solutions of the Helmholtz Equation can be expressed as expansions in spherical harmonics with coefficients proportional to the spherical Bessel functions. However, applying this expansion to each vector component of **E** or **B** will give solutions that are not generically divergence-free (∇ ⋅ **E** = ∇ ⋅ **B** = 0), and therefore require additional restrictions on the coefficients.

The multipole expansion circumvents this difficulty by expanding not **E** or **B**, but **r** ⋅ **E** or **r** ⋅ **B** into spherical harmonics. These expansions still solve the original Helmholtz equations for **E** and **B** because for a divergence-free field **F**, ∇2 (**r** ⋅ **F**) = **r** ⋅ (∇2 **F**). The resulting expressions for a generic electromagnetic field are:

${\begin{aligned}\mathbf {E} &=e^{-i\omega t}\sum _{l,m}{\sqrt {l(l+1)}}\left[a_{E}(l,m)\mathbf {E} _{l,m}^{(E)}+a_{M}(l,m)\mathbf {E} _{l,m}^{(M)}\right]\\\mathbf {B} &=e^{-i\omega t}\sum _{l,m}{\sqrt {l(l+1)}}\left[a_{E}(l,m)\mathbf {B} _{l,m}^{(E)}+a_{M}(l,m)\mathbf {B} _{l,m}^{(M)}\right]\,,\end{aligned}}$

where $\mathbf {E} _{l,m}^{(E)}$ and $\mathbf {B} _{l,m}^{(E)}$ are the *electric multipole fields of order (l, m)*, and $\mathbf {E} _{l,m}^{(M)}$ and $\mathbf {B} _{l,m}^{(M)}$ are the corresponding *magnetic multipole fields*, and *aE*(*l*, *m*) and *aM*(*l*, *m*) are the coefficients of the expansion. The multipole fields are given by

${\begin{aligned}\mathbf {B} _{l,m}^{(E)}&={\sqrt {l(l+1)}}\left[B_{l}^{(1)}h_{l}^{(1)}(kr)+B_{l}^{(2)}h_{l}^{(2)}(kr)\right]\mathbf {\Phi } _{l,m}\\\mathbf {E} _{l,m}^{(E)}&={\frac {i}{k}}\nabla \times \mathbf {B} _{l,m}^{(E)}\\\mathbf {E} _{l,m}^{(M)}&={\sqrt {l(l+1)}}\left[E_{l}^{(1)}h_{l}^{(1)}(kr)+E_{l}^{(2)}h_{l}^{(2)}(kr)\right]\mathbf {\Phi } _{l,m}\\\mathbf {B} _{l,m}^{(M)}&=-{\frac {i}{k}}\nabla \times \mathbf {E} _{l,m}^{(M)}\,,\end{aligned}}$

where *h*l(1,2)(*x*) are the spherical Hankel functions, *E*l(1,2) and *B*l(1,2) are determined by boundary conditions, and

$\mathbf {\Phi } _{l,m}={\frac {1}{\sqrt {l(l+1)}}}(\mathbf {r} \times \nabla )Y_{l,m}$

are vector spherical harmonics normalized so that

$\int \mathbf {\Phi } _{l,m}^{*}\cdot \mathbf {\Phi } _{l',m'}d\Omega =\delta _{l,l'}\delta _{m,m'}.$

The multipole expansion of the electromagnetic field finds application in a number of problems involving spherical symmetry, for example antennae radiation patterns, or nuclear gamma decay. In these applications, one is often interested in the power radiated in the far-field. In this regions, the **E** and **B** fields asymptotically approach

${\begin{aligned}\mathbf {B} &\approx {\frac {e^{i(kr-\omega t)}}{kr}}\sum _{l,m}(-i)^{l+1}\left[a_{E}(l,m)\mathbf {\Phi } _{l,m}+a_{M}(l,m)\mathbf {\hat {r}} \times \mathbf {\Phi } _{l,m}\right]\\\mathbf {E} &\approx \mathbf {B} \times \mathbf {\hat {r}} .\end{aligned}}$

The angular distribution of the time-averaged radiated power is then given by

${\frac {dP}{d\Omega }}\approx {\frac {1}{2k^{2}}}\left|\sum _{l,m}(-i)^{l+1}\left[a_{E}(l,m)\mathbf {\Phi } _{l,m}\times \mathbf {\hat {r}} +a_{M}(l,m)\mathbf {\Phi } _{l,m}\right]\right|^{2}.$
