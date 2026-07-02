---
title: "Poynting vector"
source: https://en.wikipedia.org/wiki/Poynting_vector
domain: electrodynamics
license: CC-BY-SA-4.0
tags: classical electrodynamics, poynting vector, electromagnetic radiation, retarded potential
fetched: 2026-07-02
---

# Poynting vector

In physics, the **Poynting vector** (or **Umov–Poynting vector**) represents the directional energy flux (the energy transfer per unit area, per unit time) or *power flow* of an electromagnetic field. The SI unit of the Poynting vector is the watt per square metre (W/m2); kg/s3 in SI base units. It is named after its discoverer John Henry Poynting who first derived it in 1884. Nikolay Umov is also credited with formulating the concept. Oliver Heaviside also discovered it independently in the more general form that recognises the freedom of adding the curl of an arbitrary vector field to the definition. The Poynting vector is used throughout electromagnetics in conjunction with Poynting's theorem, the continuity equation expressing conservation of electromagnetic energy, to calculate the power flow in electromagnetic fields.

## Definition

In Poynting's original paper and in most textbooks, the Poynting vector $\mathbf {S}$ is defined as the cross product $\mathbf {S} =\mathbf {E} \times \mathbf {H} ,$ where bold letters represent vectors and

- **E** is the electric field vector;
- **H** is the magnetic field's auxiliary field vector or *magnetizing field*.

This expression is often called the *Abraham form* and is the most widely used. The Poynting vector is usually denoted by **S** or **N**.

In simple terms, the Poynting vector **S**, *at a point*, gives the magnitude and direction of surface power density that are due to electromagnetic fields *at that point*. More rigorously, it is the quantity that must be used to make Poynting's theorem valid. Poynting's theorem essentially says that the difference between the electromagnetic energy entering a region and the electromagnetic energy leaving a region must equal the energy converted or dissipated in that region, that is, turned into a different form of energy (often heat). Poynting's theorem is simply a statement of local conservation of energy.

If electromagnetic energy is not gained from or lost to other forms of energy within some region (e.g., mechanical energy or heating), then electromagnetic energy is locally conserved within that region, yielding a continuity equation as a special case of Poynting's theorem: $\nabla \cdot \mathbf {S} =-{\frac {\partial u}{\partial t}}$ where u is the energy density of the electromagnetic field. This frequent condition holds in the following simple example in which the Poynting vector is calculated and seen to be consistent with the usual computation of power in an electric circuit.

## Example: Power flow in a coaxial cable

We can find a relatively simple solution in the case of power transmission through a section of coaxial cable analyzed in cylindrical coordinates as depicted in the accompanying diagram. The model's symmetry implies that there is no dependence on *θ* (circular symmetry) nor on *Z* (position along the cable). The model (and solution) can be considered simply as a DC circuit with no time dependence, but the following solution applies equally well to the transmission of radio frequency power, as long as we are considering an instant of time (during which the voltage and current don't change), and over a sufficiently short segment of cable (much smaller than a wavelength, so that these quantities are not dependent on *Z*).

The coaxial cable is specified as having an inner conductor of radius *R*1 and an outer conductor whose inner radius is *R*2 (its thickness beyond *R*2 doesn't affect the following analysis). In between *R*1 and *R*2 the cable contains an ideal dielectric material of relative permittivity *ε*r and we assume conductors that are non-magnetic (so *μ* = *μ*0) and lossless (perfect conductors), all of which are good approximations to real-world coaxial cable in typical situations.

The central conductor is at voltage *V* and draws a current *I* toward the right, so we expect a total power flow of *P* = *V* · *I* according to basic laws of electricity. By evaluating the Poynting vector, however, we are able to identify the profile of power flow in terms of the electric and magnetic fields inside the coaxial cable. The electric field is zero inside of each conductor, but between the conductors ( $R_{1}<r<R_{2}$ ), symmetry dictates that it is in the radial direction and it can be shown (using Gauss's law) that they must obey the following form: $E_{r}(r)={\frac {W}{r}}$ *W* can be evaluated by integrating the electric field from $r=R_{2}$ to $R_{1}$ which must be the negative of the voltage *V*: $-V=\int _{R_{2}}^{R_{1}}{\frac {W}{r}}dr=-W\ln \left({\frac {R_{2}}{R_{1}}}\right)$ so that: $W={\frac {V}{\ln(R_{2}/R_{1})}}$

The magnetic field, again by symmetry, can be non-zero only in the *θ* direction, that is, a vector field looping around the center conductor at every radius between *R*1 and *R*2. *Inside* the conductors themselves the magnetic field may or may not be zero, but this is of no concern since the Poynting vector in these regions is zero due to the electric field being zero. Outside the entire coaxial cable, the magnetic field is identically zero since paths in this region enclose a net current of zero (+*I* in the center conductor and −*I* in the outer conductor), and again the electric field is zero there anyway. Using Ampère's law in the region from *R*1 to *R*2, which encloses the current +*I* in the center conductor but with no contribution from the current in the outer conductor, we find at radius *r*: ${\begin{aligned}I=\oint _{C}\mathbf {H} \cdot ds&=2\pi rH_{\theta }(r)\\H_{\theta }(r)&={\frac {I}{2\pi r}}\end{aligned}}$ Now, from an electric field in the radial direction, and a tangential magnetic field, the Poynting vector, given by the cross-product of these, is only non-zero in the *Z* direction, along the direction of the coaxial cable itself, as we would expect. Again only a function of *r*, we can evaluate **S**(*r*): $S_{z}(r)=E_{r}(r)H_{\theta }(r)={\frac {W}{r}}{\frac {I}{2\pi r}}={\frac {W\,I}{2\pi r^{2}}}$ where *W* is given above in terms of the center conductor voltage *V*. The *total* power flowing down the coaxial cable can be computed by integrating over the entire cross section **A** of the cable in between the conductors: ${\begin{aligned}P_{\text{tot}}&=\iint _{\mathbf {A} }S_{z}(r,\theta )\,dA=\int _{R_{1}}^{R_{2}}2\pi rdrS_{z}(r)\\&=\int _{R_{1}}^{R_{2}}{\frac {W\,I}{r}}dr=W\,I\,\ln \left({\frac {R_{2}}{R_{1}}}\right).\end{aligned}}$

Substituting the earlier solution for the constant *W* we find: $P_{\mathrm {tot} }=I\ln \left({\frac {R_{2}}{R_{1}}}\right){\frac {V}{\ln(R_{2}/R_{1})}}=V\,I$ that is, the power given by integrating the Poynting vector over a cross section of the coaxial cable is exactly equal to the product of voltage and current as one would have computed for the power delivered using basic laws of electricity.

Other similar examples in which the *P* = *V* · *I* result can be analytically calculated are: the parallel-plate transmission line, using Cartesian coordinates, and the two-wire transmission line, using bipolar cylindrical coordinates.

## Other forms

In the "microscopic" version of Maxwell's equations, this definition must be replaced by a definition in terms of the electric field **E** and the magnetic flux density **B** (described later in the article).

It is also possible to combine the electric displacement field **D** with the magnetic flux **B** to get the *Minkowski form* of the Poynting vector, or use **D** and **H** to construct yet another version. The choice has been controversial: Pfeifer et al. summarize and to a certain extent resolve the century-long dispute between proponents of the Abraham and Minkowski forms (see Abraham–Minkowski controversy).

The Poynting vector represents the particular case of an energy flux vector for electromagnetic energy. However, any type of energy has its direction of movement in space, as well as its density, so energy flux vectors can be defined for other types of energy as well, e.g., for mechanical energy. The Umov–Poynting vector discovered by Nikolay Umov in 1874 describes energy flux in liquid and elastic media in a completely generalized view.

## Interpretation

The Poynting vector appears in Poynting's theorem (see that article for the derivation), an energy-conservation law: ${\frac {\partial u}{\partial t}}=-\mathbf {\nabla } \cdot \mathbf {S} -\mathbf {J_{\mathrm {f} }} \cdot \mathbf {E} ,$ where **J**f is the current density of free charges and *u* is the electromagnetic energy density for linear, nondispersive materials, given by $u={\frac {1}{2}}\!\left(\mathbf {E} \cdot \mathbf {D} +\mathbf {B} \cdot \mathbf {H} \right)\!,$ where

- **E** is the electric field;
- **D** is the electric displacement field;
- **B** is the magnetic flux density;
- **H** is the magnetizing field.

The first term in the right-hand side represents the electromagnetic energy flow into a small volume, while the second term subtracts the work done by the field on free electrical currents, which thereby exits from electromagnetic energy as dissipation, heat, etc. In this definition, bound electrical currents are not included in this term and instead contribute to **S** and *u*.

For light in free space, the linear momentum density is ${\frac {\langle S\rangle }{c^{2}}}.$

For linear, nondispersive (in which all frequency components travel at the same speed) and isotropic (for simplicity) materials, the constitutive relations can be written as $\mathbf {D} =\varepsilon \mathbf {E} ,\quad \mathbf {B} =\mu \mathbf {H} ,$ where

- *ε* is the permittivity of the material;
- *μ* is the permeability of the material.

Here *ε* and *μ* are scalar, real-valued constants independent of position, direction, and frequency.

In principle, this limits Poynting's theorem in this form to fields in vacuum and nondispersive linear materials. A generalization to dispersive materials is possible under certain circumstances at the cost of additional terms.

One consequence of the Poynting formula is that for the electromagnetic field to do work, both magnetic and electric fields must be present. The magnetic field alone or the electric field alone cannot do any work.

## Plane waves

In a propagating electromagnetic plane wave in an isotropic lossless medium, the instantaneous Poynting vector always points in the direction of propagation while rapidly oscillating in magnitude. This can be simply seen given that in a plane wave, the magnitude of the magnetic field **H**(*r*, *t*) is given by the magnitude of the electric field vector **E**(*r*, *t*) divided by *η*, the intrinsic impedance of the transmission medium: $|\mathbf {H} |={\frac {|\mathbf {E} |}{\eta }},$ where |**A**| represents the vector norm of **A**. Since **E** and **H** are at right angles to each other, the magnitude of their cross product is the product of their magnitudes. Without loss of generality let us take *X* to be the direction of the electric field and *Y* to be the direction of the magnetic field. The instantaneous Poynting vector, given by the cross product of **E** and **H** will then be in the positive *Z* direction: $\left|{\mathsf {S_{z}}}\right|=\left|{\mathsf {E_{x}}}{\mathsf {H_{y}}}\right|={\frac {\left|{\mathsf {E_{x}}}\right|^{2}}{\eta }}.$

Finding the time-averaged power in the plane wave then requires averaging over the wave period (the inverse frequency of the wave): $\left\langle {\mathsf {S_{z}}}\right\rangle ={\frac {\left\langle \left|{\mathsf {E_{x}}}\right|^{2}\right\rangle }{\eta }}={\frac {\mathsf {E_{\text{rms}}^{2}}}{\eta }},$ where *E*rms is the root mean square (RMS) electric field amplitude. In the important case that *E*(*t*) is sinusoidally varying at some frequency with peak amplitude *E*peak, *E*rms is ${\mathsf {E_{peak}}}/{\sqrt {2}}$ , with the average Poynting vector then given by: $\left\langle {\mathsf {S_{z}}}\right\rangle ={\frac {\mathsf {E_{peak}^{2}}}{2\eta }}.$ This is the most common form for the energy flux of a plane wave, since sinusoidal field amplitudes are most often expressed in terms of their peak values, and complicated problems are typically solved considering only one frequency at a time. However, the expression using *E*rms is totally general, applying, for instance, in the case of noise whose RMS amplitude can be measured but where the "peak" amplitude is meaningless. In free space the intrinsic impedance *η* is simply given by the impedance of free space *η*0 ≈ 377 Ω. In non-magnetic dielectrics (such as all transparent materials at optical frequencies) with a specified dielectric constant *ε*r, or in optics with a material whose refractive index ${\mathsf {n}}={\sqrt {\epsilon _{r}}}$ , the intrinsic impedance is found as: $\eta ={\frac {\eta _{0}}{\sqrt {\epsilon _{r}}}}.$

In optics, the value of radiated flux crossing a surface, thus the average Poynting vector component in the direction normal to that surface, is technically known as the irradiance, more often simply referred to as the *intensity* (a somewhat ambiguous term).

## Formulation in terms of microscopic fields

The "microscopic" (differential) version of Maxwell's equations admits only the fundamental fields **E** and **B**, without a built-in model of material media. Only the vacuum permittivity and permeability are used, and there is no **D** or **H**. When this model is used, the Poynting vector is defined as $\mathbf {S} ={\frac {1}{\mu _{0}}}\mathbf {E} \times \mathbf {B} ,$ where

- *μ*0 is the vacuum permeability;
- **E** is the electric field vector;
- **B** is the magnetic flux.

This is actually the general expression of the Poynting vector. The corresponding form of Poynting's theorem is ${\frac {\partial u}{\partial t}}=-\nabla \cdot \mathbf {S} -\mathbf {J} \cdot \mathbf {E} ,$ where **J** is the *total* current density and the energy density *u* is given by $u={\frac {1}{2}}\!\left(\varepsilon _{0}|\mathbf {E} |^{2}+{\frac {1}{\mu _{0}}}|\mathbf {B} |^{2}\right)\!,$ where *ε*0 is the vacuum permittivity. It can be derived directly from Maxwell's equations in terms of *total* charge and current and the Lorentz force law only.

The two alternative definitions of the Poynting *vector* are equal in vacuum or in non-magnetic materials, where **B** = *μ*0**H**. In all other cases, they differ in that **S** = (1/*μ*0) **E** × **B** and the corresponding *u* are purely radiative, since the dissipation term −**J** ⋅ **E** covers the total current, while the **E** × **H** definition has contributions from bound currents which are then excluded from the dissipation term.

Since only the microscopic fields **E** and **B** occur in the derivation of **S** = (1/*μ*0) **E** × **B** and the energy density, assumptions about any material present are avoided. The Poynting vector and theorem and expression for energy density are universally valid in vacuum and all materials.

## Time-averaged Poynting vector

The above form for the Poynting vector represents the *instantaneous* power flow due to *instantaneous* electric and magnetic fields. More commonly, problems in electromagnetics are solved in terms of sinusoidally varying fields at a specified frequency. The results can then be applied more generally, for instance, by representing incoherent radiation as a superposition of such waves at different frequencies and with fluctuating amplitudes.

We would thus not be considering the instantaneous **E**(*t*) and **H**(*t*) used above, but rather a complex (vector) amplitude for each which describes a coherent wave's phase (as well as amplitude) using phasor notation. These complex amplitude vectors are *not* functions of time, as they are understood to refer to oscillations over all time. A phasor such as **E**m is understood to signify a sinusoidally varying field whose instantaneous amplitude **E**(*t*) follows the real part of **E**m *ejωt* where ω is the (radian) frequency of the sinusoidal wave being considered.

In the time domain, it will be seen that the instantaneous power flow will be fluctuating at a frequency of 2*ω*. But what is normally of interest is the *average* power flow in which those fluctuations are not considered. In the math below, this is accomplished by integrating over a full cycle *T* = 2*π* / *ω*. The following quantity, still referred to as a "Poynting vector", is expressed directly in terms of the phasors as: $\mathbf {S} _{\mathrm {m} }={\tfrac {1}{2}}\mathbf {E} _{\mathrm {m} }\times \mathbf {H} _{\mathrm {m} }^{*},$ where ∗ denotes the complex conjugate. The time-averaged power flow (according to the instantaneous Poynting vector averaged over a full cycle, for instance) is then given by the *real part* of **S**m. The imaginary part is usually ignored, however, it signifies "reactive power" such as the interference due to a standing wave or the near field of an antenna. In a single electromagnetic plane wave (rather than a standing wave which can be described as two such waves travelling in opposite directions), **E** and **H** are exactly in phase, so **S**m is simply a real number according to the above definition.

The equivalence of Re(**S**m) to the time-average of the *instantaneous* Poynting vector **S** can be shown as follows. ${\begin{aligned}\mathbf {S} (t)&=\mathbf {E} (t)\times \mathbf {H} (t)\\&=\operatorname {Re} \!\left(\mathbf {E} _{\mathrm {m} }e^{j\omega t}\right)\times \operatorname {Re} \!\left(\mathbf {H} _{\mathrm {m} }e^{j\omega t}\right)\\&={\tfrac {1}{2}}\!\left(\mathbf {E} _{\mathrm {m} }e^{j\omega t}+\mathbf {E} _{\mathrm {m} }^{*}e^{-j\omega t}\right)\times {\tfrac {1}{2}}\!\left(\mathbf {H} _{\mathrm {m} }e^{j\omega t}+\mathbf {H} _{\mathrm {m} }^{*}e^{-j\omega t}\right)\\&={\tfrac {1}{4}}\!\left(\mathbf {E} _{\mathrm {m} }\times \mathbf {H} _{\mathrm {m} }^{*}+\mathbf {E} _{\mathrm {m} }^{*}\times \mathbf {H} _{\mathrm {m} }+\mathbf {E} _{\mathrm {m} }\times \mathbf {H} _{\mathrm {m} }e^{2j\omega t}+\mathbf {E} _{\mathrm {m} }^{*}\times \mathbf {H} _{\mathrm {m} }^{*}e^{-2j\omega t}\right)\\&={\tfrac {1}{2}}\operatorname {Re} \!\left(\mathbf {E} _{\mathrm {m} }\times \mathbf {H} _{\mathrm {m} }^{*}\right)+{\tfrac {1}{2}}\operatorname {Re} \!\left(\mathbf {E} _{\mathrm {m} }\times \mathbf {H} _{\mathrm {m} }e^{2j\omega t}\right)\!.\end{aligned}}$

The average of the instantaneous Poynting vector **S** over time is given by: $\langle \mathbf {S} \rangle ={\frac {1}{T}}\int _{0}^{T}\mathbf {S} (t)\,dt={\frac {1}{T}}\int _{0}^{T}\!\left[{\tfrac {1}{2}}\operatorname {Re} \!\left(\mathbf {E} _{\mathrm {m} }\times \mathbf {H} _{\mathrm {m} }^{*}\right)+{\tfrac {1}{2}}\operatorname {Re} \!\left({\mathbf {E} _{\mathrm {m} }}\times {\mathbf {H} _{\mathrm {m} }}e^{2j\omega t}\right)\right]dt.$

The second term is the double-frequency component having an average value of zero, so we find: $\langle \mathbf {S} \rangle ={\tfrac {1}{2}}\operatorname {Re} \!\left({\mathbf {E} _{\mathrm {m} }}\times \mathbf {H} _{\mathrm {m} }^{*}\right)=\operatorname {Re} \!\left(\mathbf {S} _{\mathrm {m} }\right)$

According to some conventions, the factor of 1/2 in the above definition may be left out. Multiplication by 1/2 is required to properly describe the power flow since the magnitudes of **E**m and **H**m refer to the *peak* fields of the oscillating quantities. If rather the fields are described in terms of their root mean square (RMS) values (which are each smaller by the factor ${\sqrt {2}}/2$ ), then the correct average power flow is obtained without multiplication by 1/2.

## Resistive dissipation

If a conductor has significant resistance, then, near the surface of that conductor, the Poynting vector would be tilted toward and impinge upon the conductor. Once the Poynting vector enters the conductor, it is bent to a direction that is almost perpendicular to the surface. This is a consequence of Snell's law and the very slow speed of light inside a conductor. The definition and computation of the speed of light in a conductor can be given. Inside the conductor, the Poynting vector represents energy flow from the electromagnetic field into the wire, producing resistive Joule heating in the wire. For a derivation that starts with Snell's law see Reitz page 454.

## Radiation pressure

The density of the linear momentum of the electromagnetic field is *S*/*c*2 where *S* is the magnitude of the Poynting vector and *c* is the speed of light in free space. The radiation pressure exerted by an electromagnetic wave on the surface of a target is given by $P_{\mathrm {rad} }={\frac {\langle S\rangle }{\mathrm {c} }}.$

## Uniqueness of the Poynting vector

The Poynting vector occurs in Poynting's theorem only through its divergence ∇ ⋅ **S**, that is, it is only required that the surface integral of the Poynting vector around a closed surface describe the net flow of electromagnetic energy into or out of the enclosed volume. This means that adding a solenoidal vector field (one with zero divergence) to **S** will result in another field that satisfies this required property of a Poynting vector field according to Poynting's theorem. Since the divergence of any curl is zero, one can add the curl of any vector field to the Poynting vector and the resulting vector field **S**′ will still satisfy Poynting's theorem.

However even though the Poynting vector was originally formulated only for the sake of Poynting's theorem in which only its divergence appears, it turns out that the above choice of its form *is* unique. The following section gives an example which illustrates why it is *not* acceptable to add an arbitrary solenoidal field to **E** × **H**.

## Static fields

The consideration of the Poynting vector in static fields shows the relativistic nature of the Maxwell equations and allows a better understanding of the magnetic component of the Lorentz force, *q*(**v** × **B**). To illustrate, the accompanying picture is considered, which describes the Poynting vector in a cylindrical capacitor, which is located in an **H** field (pointing into the page) generated by a permanent magnet. Although there are only static electric and magnetic fields, the calculation of the Poynting vector produces a clockwise circular flow of electromagnetic energy, with no beginning or end.

While the circulating energy flow may seem unphysical, its existence is necessary to maintain conservation of angular momentum. The momentum of an electromagnetic wave in free space is equal to its power divided by *c*, the speed of light. Therefore, the circular flow of electromagnetic energy implies an *angular* momentum. If one were to connect a wire between the two plates of the charged capacitor, then there would be a Lorentz force on that wire while the capacitor is discharging due to the discharge current and the crossed magnetic field; that force would be circumferential to the central axis and thus add angular momentum to the system. That angular momentum would match the "hidden" angular momentum, revealed by the Poynting vector, circulating before the capacitor was discharged.
