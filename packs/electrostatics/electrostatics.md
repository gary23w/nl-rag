---
title: "Electrostatics"
source: https://en.wikipedia.org/wiki/Electrostatics
domain: electrostatics
license: CC-BY-SA-4.0
tags: electrostatic field, electric charge, electric dipole moment, vacuum permittivity
fetched: 2026-07-02
---

# Electrostatics

**Electrostatics** is a branch of physics that studies slow-moving or stationary electric charges on macroscopic objects where quantum effects can be neglected. Under these circumstances, the electric field, electric potential, and the charge density are related without complications from magnetic effects.

Since classical antiquity, it has been known that some materials, such as amber, attract lightweight particles after rubbing. The Greek word *ḗlektron* (ἤλεκτρον), meaning 'amber', was thus the root of the word *electricity*. Electrostatic phenomena arise from the forces that electric charges exert on each other. Such forces are described by Coulomb's law.

There are many examples of electrostatic phenomena, from those as simple as the attraction of plastic wrap to one's hand after it is removed from a package, to the apparently spontaneous explosion of grain silos, the damage of electronic components during manufacturing, and photocopier and laser printer operation.

## Coulomb's law

Coulomb's law states that:

> The magnitude of the electrostatic force of attraction or repulsion between two point charges is directly proportional to the product of the magnitudes of charges and inversely proportional to the square of the distance between them.

The force is along the straight line joining them. If the two charges have the same sign, the electrostatic force between them is repulsive; if they have different signs, the force between them is attractive.

If r is the distance (in meters) between two charges, then the force between two point charges Q and q is:

$F={1 \over 4\pi \varepsilon _{0}}{|Qq| \over r^{2}},$

where *ε*0 = 8.8541878188(14)×10−12 F⋅m−1‍ is the vacuum permittivity.

The SI unit of *ε*0 is equivalently A2⋅s4 ⋅kg−1⋅m−3 or C2⋅N−1⋅m−2 or F⋅m−1.

## Electric field

The electric field, $\mathbf {E}$ , in units of newtons per coulomb or volts per meter, is a vector field that can be defined everywhere, except at the location of point charges (where it diverges to infinity). It is defined as the electrostatic force $\mathbf {F}$ on a hypothetical small test charge at the point due to Coulomb's law, divided by the charge q

$\mathbf {E} ={\mathbf {F} \over q}$

Electric field lines are useful for visualizing the electric field. Field lines begin on positive charge and terminate on negative charge. They are parallel to the direction of the electric field at each point, and the density of these field lines is a measure of the magnitude of the electric field at any given point.

A collection of n particles of charge $q_{i}$ , located at points $\mathbf {r} _{i}$ (called *source points*) generates the electric field at $\mathbf {r}$ (called the *field point*) of:

$\mathbf {E} (\mathbf {r} )={1 \over 4\pi \varepsilon _{0}}\sum _{i=1}^{n}q_{i}{{\hat {\mathbf {r-r_{i}} }} \over {|\mathbf {r-r_{i}} |}^{2}}={1 \over 4\pi \varepsilon _{0}}\sum _{i=1}^{n}q_{i}{\mathbf {r-r_{i}} \over {|\mathbf {r-r_{i}} |}^{3}},$

where ${\textstyle \mathbf {r} -\mathbf {r} _{i}}$ is the displacement vector from a *source point* $\mathbf {r} _{i}$ to the *field point* $\mathbf {r}$ , and ${\textstyle {\hat {\mathbf {r-r_{i}} }}\ {\stackrel {\mathrm {def} }{=}}\ {\frac {\mathbf {r-r_{i}} }{|\mathbf {r-r_{i}} |}}}$ is the unit vector of the displacement vector that indicates the direction of the field due to the source at point $\mathbf {r_{i}}$ . For a single point charge, q , at the origin, the magnitude of this electric field is $E=q/4\pi \varepsilon _{0}r^{2}$ and points away from that charge if it is positive. The fact that the force (and hence the field) can be calculated by summing over all the contributions due to individual source particles is an example of the superposition principle. The electric field produced by a distribution of charges is given by the volume charge density $\rho (\mathbf {r} )$ and can be obtained by converting this sum into a triple integral:

$\mathbf {E} (\mathbf {r} )={\frac {1}{4\pi \varepsilon _{0}}}\iiint \,\rho (\mathbf {r} '){\mathbf {r-r'} \over {|\mathbf {r-r'} |}^{3}}\mathrm {d} ^{3}|\mathbf {r} '|$

### Gauss's law

Gauss's law states that "the total electric flux through any closed surface in free space of any shape drawn in an electric field is proportional to the total electric charge enclosed by the surface." Many numerical problems can be solved by considering a Gaussian surface around a body. Mathematically, Gauss's law takes the form of an integral equation:

$\Phi _{E}=\oint _{S}\mathbf {E} \cdot \mathrm {d} \mathbf {A} ={Q_{\text{enclosed}} \over \varepsilon _{0}}=\int _{V}{\rho \over \varepsilon _{0}}\mathrm {d} ^{3}r,$

where $\mathrm {d} ^{3}r=\mathrm {d} x\ \mathrm {d} y\ \mathrm {d} z$ is a volume element. If the charge is distributed over a surface or along a line, replace $\rho \,\mathrm {d} ^{3}r$ by $\sigma \,\mathrm {d} A$ or $\lambda \,\mathrm {d} \ell$ . The divergence theorem allows Gauss's law to be written in differential form:

$\nabla \cdot \mathbf {E} ={\rho \over \varepsilon _{0}}.$

where $\nabla \cdot$ is the divergence operator.

### Poisson and Laplace equations

The definition of electrostatic potential, combined with the differential form of Gauss's law (above), provides a relationship between the potential Φ and the charge density *ρ*:

${\nabla }^{2}\phi =-{\rho \over \varepsilon _{0}}.$

This relationship is a form of Poisson's equation. In the absence of unpaired electric charge, the equation becomes Laplace's equation:

${\nabla }^{2}\phi =0,$

## Electrostatic approximation

If the electric field in a system can be assumed to result from static charges, that is, a system that exhibits no significant time-varying magnetic fields, the system is justifiably analyzed using only the principles of electrostatics. This is called the "electrostatic approximation".

The validity of the electrostatic approximation rests on the assumption that the electric field is irrotational, or nearly so:

$\nabla \times \mathbf {E} \approx 0.$

From Faraday's law, this assumption implies the absence or near-absence of time-varying magnetic fields:

${\partial \mathbf {B} \over \partial t}\approx 0.$

In other words, electrostatics does not require the absence of magnetic fields or electric currents. Rather, if magnetic fields or electric currents *do* exist, they must not change with time, or in the worst-case, they must change with time only *very slowly*. In some problems, both electrostatics and magnetostatics may be required for accurate predictions, but the coupling between the two can still be ignored. Electrostatics and magnetostatics can both be seen as non-relativistic Galilean limits for electromagnetism. In addition, conventional electrostatics ignore quantum effects which have to be added for a complete description.

### Electrostatic potential

As the electric field is irrotational, it is possible to express the electric field as the gradient of a scalar function, $\phi$ , called the electrostatic potential (also known as the voltage). An electric field, E , points from regions of high electric potential to regions of low electric potential, expressed mathematically as

$\mathbf {E} =-\nabla \phi .$

The gradient theorem can be used to establish that the electrostatic potential is the amount of work per unit charge required to move a charge from point a to point b with the following line integral:

$-\int _{a}^{b}{\mathbf {E} \cdot \mathrm {d} \mathbf {\ell } }=\phi (\mathbf {b} )-\phi (\mathbf {a} ).$

From these equations, we see that the electric potential is constant in any region for which the electric field vanishes (such as occurs inside a conducting object).

### Electrostatic energy

A test particle's potential energy, $U_{\mathrm {E} }^{\text{single}}$ , can be calculated from a line integral of the work, $q_{n}\mathbf {E} \cdot \mathrm {d} \mathbf {\ell }$ . We integrate from a point at infinity, and assume a collection of N particles of charge $Q_{n}$ , are already situated at the points $\mathbf {r} _{i}$ . This potential energy (in Joules) is:

$U_{\mathrm {E} }^{\text{single}}=q\phi (\mathbf {r} )={\frac {q}{4\pi \varepsilon _{0}}}\sum _{i=1}^{N}{\frac {Q_{i}}{\left\|{\mathcal {\mathbf {R} _{i}}}\right\|}}$

where $\mathbf {\mathcal {R_{i}}} =\mathbf {r} -\mathbf {r} _{i}$ is the distance of each charge $Q_{i}$ from the test charge q , which situated at the point $\mathbf {r}$ , and $\phi (\mathbf {r} )$ is the electric potential that would be at $\mathbf {r}$ if the test charge were not present. If only two charges are present, the potential energy is $Q_{1}Q_{2}/(4\pi \varepsilon _{0}r)$ . The total electric potential energy due a collection of *N* charges is calculated by adding that for each particle:

$U_{\mathrm {E} }^{\text{total}}={\frac {1}{4\pi \varepsilon _{0}}}\sum _{j=1}^{N}Q_{j}\sum _{i=1}^{j-1}{\frac {Q_{i}}{r_{ij}}}={\frac {1}{2}}\sum _{i=1}^{N}Q_{i}\phi _{i},$

where the following sum from, *j* = 1 to *N*, excludes *i* = *j*:

$\phi _{i}={\frac {1}{4\pi \varepsilon _{0}}}\sum _{\stackrel {j=1}{j\neq i}}^{N}{\frac {Q_{j}}{r_{ij}}}.$

This electric potential, $\phi _{i}$ is what would be measured at $\mathbf {r} _{i}$ if the charge $Q_{i}$ were missing. This formula obviously excludes the (infinite) energy that would be required to assemble each point charge from a disperse cloud of charge. The sum over charges can be converted into an integral over charge density using the prescription ${\textstyle \sum (\cdots )\rightarrow \int (\cdots )\rho \,\mathrm {d} ^{3}r}$ :

$U_{\mathrm {E} }^{\text{total}}={\frac {1}{2}}\int \rho (\mathbf {r} )\phi (\mathbf {r} )\,\mathrm {d} ^{3}r={\frac {\varepsilon _{0}}{2}}\int \left|{\mathbf {E} }\right|^{2}\,\mathrm {d} ^{3}r,$

This second expression for electrostatic energy uses the fact that the electric field is the negative gradient of the electric potential, as well as vector calculus identities in a way that resembles integration by parts. These two integrals for electric field energy seem to indicate two mutually exclusive formulas for electrostatic energy density, namely ${\textstyle {\frac {1}{2}}\rho \phi }$ and ${\textstyle {\frac {1}{2}}\varepsilon _{0}E^{2}}$ ; they yield equal values for the total electrostatic energy only if both are integrated over all space.

### Electrostatic pressure

Inside of an electrical conductor, there is no electric field. The external electric field has been balanced by surface charges due to movement of charge carriers, either to or from other parts of the material, known as electrostatic induction. The equation connecting the field just above a small patch of the surface and the surface charge is $\mathbf {E\cdot {\hat {n}}} ={\frac {\sigma }{\epsilon _{0}}}$ where

- $\mathbf {\hat {n}}$ = the surface unit normal vector,
- $\mathbf {\sigma }$ = the surface charge density.

The average electric field, half the external value, also exerts a force (Coulomb's law) on the conductor patch where the force $\mathbf {f}$ is given by

$\mathbf {f} ={\frac {1}{2\epsilon _{0}}}\sigma ^{2}\mathbf {\hat {n}}$

.

In terms of the field just outside the surface, the force is equivalent to a pressure given by:

$P={\frac {\varepsilon _{0}}{2}}(\mathbf {E\cdot {\hat {n}}} )^{2},$

This pressure acts normal to the surface of the conductor, independent of whether: the mobile charges are electrons, holes or mobile protons; the sign of the surface charge; or the sign of the surface normal component of the electric field. Note that there is a similar form for electrostriction in a dielectric.
