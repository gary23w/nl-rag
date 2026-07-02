---
title: "Polarization density"
source: https://en.wikipedia.org/wiki/Polarization_density
domain: dielectric-materials
license: CC-BY-SA-4.0
tags: dielectric materials, electric permittivity, ferroelectricity phenomena, dielectric strength
fetched: 2026-07-02
---

# Polarization density

In classical electromagnetism, **polarization density** (or **electric polarization**, or simply **polarization**) is the vector field that expresses the volumetric density of permanent or induced electric dipole moments in a dielectric material. When a dielectric is placed in an external electric field, its atoms or molecules gain electric dipole moment and the dielectric is said to be polarized.

Electric polarization of a given dielectric material sample is defined as the quotient of electric dipole moment (a vector quantity, expressed as coulombs-meters (C⋅m) in SI units) to volume (in meters cubed). Polarization density is denoted mathematically by **P**; in SI units, it is expressed in coulombs per square meter (C/m2).

Polarization density also describes how a material responds to an applied electric field as well as the way the material changes the electric field, and can be used to calculate the forces that result from those interactions. It can be compared to magnetization, which is the measure of the corresponding response of a material to a magnetic field in magnetism.

Similar to ferromagnets, which have a non-zero permanent magnetization even if no external magnetic field is applied, ferroelectric materials have a non-zero polarization in the absence of external electric field.

## Definition

An external electric field that is applied to a dielectric material, causes a displacement of bound charged elements.

A ***bound charge*** is a charge that is associated with an atom or molecule within a material. It is called "bound" because it is not free to move within the material like ***free charges***. Positive charged elements are displaced in the direction of the field, and negative charged elements are displaced opposite to the direction of the field. The molecules may remain neutral in charge, yet an electric dipole moment forms.

For a certain volume element $\Delta V$ in the material, which carries a dipole moment $\Delta \mathbf {p}$ , we define the polarization density **P**: $\mathbf {P} ={\frac {\Delta \mathbf {p} }{\Delta V}}$

In general, the dipole moment $\Delta \mathbf {p}$ changes from point to point within the dielectric. Hence, the polarization density **P** of a dielectric inside an infinitesimal volume d*V* with an infinitesimal dipole moment d**p** is:

| $\mathbf {P} ={\frac {\mathrm {d} \mathbf {p} }{\mathrm {d} V}}$ |   | 1 |
|---|---|---|

The net charge appearing as a result of polarization is called bound charge and denoted $Q_{\text{b}}$ .

This definition of polarization density as a "dipole moment per unit volume" is widely adopted, though in some cases it can lead to ambiguities and paradoxes.

## Other expressions

Let a volume d*V* be isolated inside the dielectric. Due to polarization the positive bound charge $\mathrm {d} q_{\text{b}}^{+}$ will be displaced a distance **d** relative to the negative bound charge $\mathrm {d} q_{\text{b}}^{-}$ , giving rise to a dipole moment $\mathrm {d} \mathbf {p} =\mathrm {d} q_{\text{b}}\mathbf {d}$ . Substitution of this expression in **(1)** yields $\mathbf {P} ={\mathrm {d} q_{\text{b}} \over \mathrm {d} V}\mathbf {d}$

Since the charge $\mathrm {d} q_{\text{b}}$ bounded in the volume d*V* is equal to $\rho _{\text{b}}\mathrm {d} V$ the equation for **P** becomes:

| $\mathbf {P} =\rho _{\text{b}}\mathbf {d}$ |   | 2 |
|---|---|---|

where $\rho _{\text{b}}$ is the density of the bound charge in the volume under consideration. It is clear from the definition above that the dipoles are overall neutral and thus $\rho _{\text{b}}$ is balanced by an equal density of opposite charges within the volume. Charges that are not balanced are part of the free charge discussed below.

## Gauss's law for the field of *P*

For a given volume V enclosed by a surface S, the bound charge $Q_{\text{b}}$ inside it is equal to the flux of **P** through S taken with the negative sign, or

| $-Q_{\text{b}}=$ (\oiint) ${\scriptstyle S}$ $\mathbf {P} \cdot \mathrm {d} \mathbf {A}$ |   | 3 |
|---|---|---|

Proof

Let a surface area S envelope part of a dielectric. Upon polarization negative and positive bound charges will be displaced. Let *d*1 and *d*2 be the distances of the bound charges $\mathrm {d} q_{\text{b}}^{-}$ and $\mathrm {d} q_{\text{b}}^{+}$ , respectively, from the plane formed by the element of area d*A* after the polarization. And let d*V*1 and d*V*2 be the volumes enclosed below and above the area d*A*.

It follows that the negative bound charge $\mathrm {d} q_{\text{b}}^{-}=\rho _{\text{b}}^{-}\ \mathrm {d} V_{1}=\rho _{\text{b}}^{-}d_{1}\ \mathrm {d} A$ moved from the outer part of the surface d*A* inwards, while the positive bound charge $\mathrm {d} q_{\text{b}}^{+}=\rho _{\text{b}}\ \mathrm {d} V_{2}=\rho _{\text{b}}d_{2}\ \mathrm {d} A$ moved from the inner part of the surface outwards.

By the law of conservation of charge the total bound charge $\mathrm {d} Q_{\text{b}}$ left inside the volume $\mathrm {d} V$ after polarization is:

${\begin{aligned}\mathrm {d} Q_{\text{b}}&=\mathrm {d} q_{\text{in}}-\mathrm {d} q_{\text{out}}\\&=\mathrm {d} q_{\text{b}}^{-}-\mathrm {d} q_{\text{b}}^{+}\\&=\rho _{\text{b}}^{-}d_{1}\ \mathrm {d} A-\rho _{\text{b}}d_{2}\ \mathrm {d} A\end{aligned}}$

Since $\rho _{\text{b}}^{-}=-\rho _{\text{b}}$ and (see image to the right) ${\begin{aligned}d_{1}&=(d-a)\cos(\theta )\\d_{2}&=a\cos(\theta )\end{aligned}}$

The above equation becomes ${\begin{aligned}\mathrm {d} Q_{\text{b}}&=-\rho _{\text{b}}(d-a)\cos(\theta )\ \mathrm {d} A-\rho _{\text{b}}a\cos(\theta )\ \mathrm {d} A\\&=-\rho _{\text{b}}d\ \mathrm {d} A\cos(\theta )\end{aligned}}$

By (**2**) it follows that $\rho _{\text{b}}d=P$ , so we get: ${\begin{aligned}\mathrm {d} Q_{\text{b}}&=-P\ \mathrm {d} A\cos(\theta )\\-\mathrm {d} Q_{\text{b}}&=\mathbf {P} \cdot \mathrm {d} \mathbf {A} \end{aligned}}$

And by integrating this equation over the entire closed surface S we find that

$-Q_{\text{b}}=$

$\scriptstyle {S}$

$\mathbf {P} \cdot \mathrm {d} \mathbf {A}$

which completes the proof.

### Differential form

By the divergence theorem, Gauss's law for the field **P** can be stated in *differential form* as: $-\rho _{\text{b}}=\nabla \cdot \mathbf {P} ,$ where ∇ · **P** is the divergence of the field **P** through a given surface containing the bound charge density $\rho _{\text{b}}$ .

Proof

By the divergence theorem we have that $-Q_{\text{b}}=\iiint _{V}\nabla \cdot \mathbf {P} \ \mathrm {d} V,$ for the volume V containing the bound charge $Q_{\text{b}}$ . And since $Q_{\text{b}}$ is the integral of the bound charge density $\rho _{\text{b}}$ taken over the entire volume V enclosed by S, the above equation yields $-\iiint _{V}\rho _{\text{b}}\ \mathrm {d} V=\iiint _{V}\nabla \cdot \mathbf {P} \ \mathrm {d} V,$ which is true if and only if $-\rho _{\text{b}}=\nabla \cdot \mathbf {P}$

## Relationship between the fields of *P* and *E*

### Homogeneous, isotropic dielectrics

In a homogeneous, linear, non-dispersive and isotropic dielectric medium, the **polarization** is aligned with and proportional to the electric field **E**: $\mathbf {P} =\chi \varepsilon _{0}\mathbf {E} ,$

where *ε*0 is the electric constant, and χ is the electric susceptibility of the medium. Note that in this case χ simplifies to a scalar, although more generally it is a tensor. This is a particular case due to the *isotropy* of the dielectric.

Taking into account this relation between **P** and **E**, equation (**3**) becomes:

$-Q_{\text{b}}=\chi \varepsilon _{0}\$

$\scriptstyle {S}$

$\mathbf {E} \cdot \mathrm {d} \mathbf {A}$

The expression in the integral is Gauss's law for the field **E** which yields the total charge, both free $(Q_{\text{f}})$ and bound $(Q_{\text{b}})$ , in the volume V enclosed by S. Therefore,

${\begin{aligned}-Q_{\text{b}}&=\chi Q_{\text{total}}\\&=\chi \left(Q_{\text{f}}+Q_{\text{b}}\right)\\[3pt]\Rightarrow Q_{\text{b}}&=-{\frac {\chi }{1+\chi }}Q_{\text{f}},\end{aligned}}$

which can be written in terms of free charge and bound charge densities (by considering the relationship between the charges, their volume charge densities and the given volume): $\rho _{\text{b}}=-{\frac {\chi }{1+\chi }}\rho _{\text{f}}$

Since within a homogeneous dielectric there can be no free charges $(\rho _{\text{f}}=0)$ , by the last equation it follows that there is no bulk bound charge in the material $(\rho _{\text{b}}=0)$ . And since free charges can get as close to the dielectric as to its topmost surface, it follows that polarization only gives rise to surface bound charge density (denoted $\sigma _{\text{b}}$ to avoid ambiguity with the volume bound charge density $\rho _{\text{b}}$ ).

$\sigma _{\text{b}}$ may be related to **P** by the following equation: $\sigma _{\text{b}}=\mathbf {\hat {n}} _{\text{out}}\cdot \mathbf {P}$ where $\mathbf {\hat {n}} _{\text{out}}$ is the normal vector to the surface *S* pointing outwards. (see charge density for the rigorous proof)

### Anisotropic dielectrics

The class of dielectrics where the polarization density and the electric field are not in the same direction are known as *anisotropic* materials.

In such materials, the i-th component of the polarization is related to the j-th component of the electric field according to:

$P_{i}=\sum _{j}\varepsilon _{0}\chi _{ij}E_{j},$

This relation shows, for example, that a material can polarize in the x direction by applying a field in the z direction, and so on. The case of an anisotropic dielectric medium is described by the field of crystal optics.

As in most electromagnetism, this relation deals with macroscopic averages of the fields and dipole density, so that one has a continuum approximation of the dielectric materials that neglects atomic-scale behaviors. The polarizability of individual particles in the medium can be related to the average susceptibility and polarization density by the Clausius–Mossotti relation.

In general, the susceptibility is a function of the frequency ω of the applied field. When the field is an arbitrary function of time t, the polarization is a convolution of the Fourier transform of *χ*(*ω*) with the **E**(*t*). This reflects the fact that the dipoles in the material cannot respond instantaneously to the applied field, and causality considerations lead to the Kramers–Kronig relations.

If the polarization **P** is not linearly proportional to the electric field **E**, the medium is termed *nonlinear* and is described by the field of nonlinear optics. To a good approximation (for sufficiently weak fields, assuming no permanent dipole moments are present), **P** is usually given by a Taylor series in **E** whose coefficients are the nonlinear susceptibilities:

${\frac {P_{i}}{\varepsilon _{0}}}=\sum _{j}\chi _{ij}^{(1)}E_{j}+\sum _{jk}\chi _{ijk}^{(2)}E_{j}E_{k}+\sum _{jk\ell }\chi _{ijk\ell }^{(3)}E_{j}E_{k}E_{\ell }+\cdots$

where $\chi ^{(1)}$ is the linear susceptibility, $\chi ^{(2)}$ is the second-order susceptibility (describing phenomena such as the Pockels effect, optical rectification and second-harmonic generation), and $\chi ^{(3)}$ is the third-order susceptibility (describing third-order effects such as the Kerr effect and electric field-induced optical rectification).

In ferroelectric materials, there is no one-to-one correspondence between **P** and **E** at all because of hysteresis.

## Polarization density in Maxwell's equations

The behavior of electric fields (**E**, **D**), magnetic fields (**B**, **H**), charge density (ρ) and current density (**J**) are described by Maxwell's equations in matter.

### Relations between E, D and P

In terms of volume charge densities, the **free** charge density $\rho _{\text{f}}$ is given by

$\rho _{\text{f}}=\rho -\rho _{\text{b}}$

where $\rho$ is the total charge density. By considering the relationship of each of the terms of the above equation to the divergence of their corresponding fields (of the electric displacement field **D**, **E** and **P** in that order), this can be written as:

$\mathbf {D} =\varepsilon _{0}\mathbf {E} +\mathbf {P} .$

This is known as the constitutive equation for electric fields. Here *ε*0 is the electric permittivity of empty space. In this equation, **P** is the (negative of the) field induced in the material when the "fixed" charges, the dipoles, shift in response to the total underlying field **E**, whereas **D** is the field due to the remaining charges, known as "free" charges.

In general, **P** varies as a function of **E** depending on the medium, as described later in the article. In many problems, it is more convenient to work with **D** and the free charges than with **E** and the total charge.

Therefore, a polarized medium, by way of Green's theorem can be split into four components.

- The bound volumetric charge density: $\rho _{\text{b}}=-\nabla \cdot \mathbf {P}$
- The bound surface charge density: $\sigma _{\text{b}}=\mathbf {\hat {n}} _{\text{out}}\cdot \mathbf {P}$
- The free volumetric charge density: $\rho _{\text{f}}=\nabla \cdot \mathbf {D}$
- The free surface charge density: $\sigma _{\text{f}}=\mathbf {\hat {n}} _{\text{out}}\cdot \mathbf {D}$

### Time-varying polarization density

When the polarization density changes with time, the time-dependent bound-charge density creates a *polarization current density* of

$\mathbf {J} _{p}={\frac {\partial \mathbf {P} }{\partial t}}$

so that the total current density that enters Maxwell's equations is given by

$\mathbf {J} =\mathbf {J} _{\text{f}}+\nabla \times \mathbf {M} +{\frac {\partial \mathbf {P} }{\partial t}}$

where **J**f is the free-charge current density, and the second term is the magnetization current density (also called the *bound current density*), a contribution from atomic-scale magnetic dipoles (when they are present).

## Polarization ambiguity

### Crystalline materials

In a simple approach the polarization inside a solid is not, in general, uniquely defined. Because a bulk solid is periodic, one must choose a unit cell in which to compute the polarization (see figure). In other words, two people, Alice and Bob, looking at the same solid, may calculate different values of **P**, and neither of them will be wrong. For example, if Alice chooses a unit cell with positive ions at the top and Bob chooses the unit cell with negative ions at the top, their computed **P** vectors will have opposite directions. Alice and Bob will agree on the microscopic electric field **E** in the solid, but disagree on the value of the displacement field $\mathbf {D} =\varepsilon _{0}\mathbf {E} +\mathbf {P}$ .

Even though the value of **P** is not uniquely defined in a bulk solid, *variations* in **P** *are* uniquely defined. If the crystal is gradually changed from one structure to another, there will be a current inside each unit cell, due to the motion of nuclei and electrons. This current results in a macroscopic transfer of charge from one side of the crystal to the other, and therefore it can be measured with an ammeter (like any other current) when wires are attached to the opposite sides of the crystal. The time-integral of the current is proportional to the change in **P**. The current can be calculated in computer simulations (such as density functional theory); the formula for the integrated current turns out to be a type of Berry's phase.

The non-uniqueness of **P** is not problematic, because every measurable consequence of **P** is in fact a consequence of a continuous change in **P**. For example, when a material is put in an electric field **E**, which ramps up from zero to a finite value, the material's electronic and ionic positions slightly shift. This changes **P**, and the result is electric susceptibility (and hence permittivity). As another example, when some crystals are heated, their electronic and ionic positions slightly shift, changing **P**. The result is pyroelectricity. In all cases, the properties of interest are associated with a *change* in **P**.

In what is now called the *modern theory of polarization*, the polarization is defined as a difference. Any structure which has inversion symmetry has zero polarization; there is an identical distribution of positive and negative charges about an inversion center. If the material deforms there can be a polarization due to the charge in the charge distribution.

### Amorphous materials

Another problem in the definition of **P** is related to the arbitrary choice of the "unit volume", or more precisely to the system's *scale*. For example, at *microscopic* scale a plasma can be regarded as a gas of *free* charges, thus **P** should be zero. On the contrary, at a *macroscopic* scale the same plasma can be described as a continuous medium, exhibiting a permittivity $\varepsilon (\omega )\neq 1$ and thus a net polarization **P** ≠ **0**.
