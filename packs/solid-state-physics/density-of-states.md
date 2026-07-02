---
title: "Density of states"
source: https://en.wikipedia.org/wiki/Density_of_states
domain: solid-state-physics
license: CC-BY-SA-4.0
tags: solid-state physics, brillouin zone, density of states, reciprocal lattice
fetched: 2026-07-02
---

# Density of states

In condensed matter physics, the **density of states** (**DOS**) of a system describes the number of allowed modes or states per unit energy range. The density of states is defined as $D(E)=N(E)/V$ , where $N(E)\delta E$ is the number of states in the system of volume V whose energies lie in the range from E to $E+\delta E$ . It is mathematically represented as a distribution by a probability density function, and it is generally an average over the space and time domains of the various states occupied by the system. The density of states is directly related to the dispersion relations of the properties of the system. High DOS at a specific energy level means that many states are available for occupation.

Generally, the density of states of matter is continuous. In isolated systems however, such as atoms or molecules in the gas phase, the density distribution is discrete, like a spectral density. Local variations, most often due to distortions of the original system, are often referred to as **local densities of states** (LDOSs).

## Introduction

In quantum mechanical systems, waves, or wave-like particles, can occupy modes or states with wavelengths and propagation directions dictated by the system. For example, in some systems, the interatomic spacing and the atomic charge of a material might allow only electrons of certain wavelengths to exist. In other systems, the crystalline structure of a material might allow waves to propagate in one direction, while suppressing wave propagation in another direction. Often, only specific states are permitted. Thus, it can happen that many states are available for occupation at a specific energy level, while no states are available at other energy levels.

Looking at the density of states of electrons at the band edge between the valence and conduction bands in a semiconductor, for an electron in the conduction band, an increase of the electron energy makes more states available for occupation. Alternatively, the density of states is discontinuous for an interval of energy, which means that no states are available for electrons to occupy within the band gap of the material. This condition also means that an electron at the conduction band edge must lose at least the band gap energy of the material in order to transition to another state in the valence band.

This determines if the material is an insulator or a metal in the dimension of the propagation. The result of the number of states in a band is also useful for predicting the conduction properties. For example, in a one dimensional crystalline structure an odd number of electrons per atom results in a half-filled top band; there are free electrons at the Fermi level resulting in a metal. On the other hand, an even number of electrons exactly fills a whole number of bands, leaving the rest empty. If then the Fermi level lies in an occupied band gap between the highest occupied state and the lowest empty state, the material will be an insulator or semiconductor.

Depending on the quantum mechanical system, the density of states can be calculated for electrons, photons, or phonons, and can be given as a function of either energy or the wave vector *k*. To convert between the DOS as a function of the energy and the DOS as a function of the wave vector, the system-specific energy dispersion relation between *E* and *k* must be known.

In general, the topological properties of the system such as the band structure, have a major impact on the properties of the density of states. The most well-known systems, like neutron matter in neutron stars and free electron gases in metals (examples of degenerate matter and a Fermi gas), have a 3-dimensional Euclidean topology. Less familiar systems, like two-dimensional electron gases (2DEG) in graphite layers and the quantum Hall effect system in MOSFET type devices, have a 2-dimensional Euclidean topology. Even less familiar are carbon nanotubes, the quantum wire and Luttinger liquid with their 1-dimensional topologies. Systems with 1D and 2D topologies are likely to become more common, assuming developments in nanotechnology and materials science proceed.

## Definition

The density of states related to volume *V* and *N* countable energy levels is defined as: $D(E)={\frac {1}{V}}\,\sum _{i=1}^{N}\delta (E-E({\mathbf {k} }_{i})).$ Because the smallest allowed change of momentum k for a particle in a box of dimension d and length L is $(\Delta k)^{d}=({2\pi }/{L})^{d}$ , the volume-related density of states for continuous energy levels is obtained in the limit $L\to \infty$ as $D(E):=\int _{\mathbb {R} ^{d}}{\frac {\mathrm {d} ^{d}k}{(2\pi )^{d}}}\cdot \delta (E-E(\mathbf {k} )),$ Here, d is the spatial dimension of the considered system and $\mathbf {k}$ the wave vector.

For isotropic one-dimensional systems with parabolic energy dispersion, the density of states is ${\textstyle D_{1D}(E)={\tfrac {1}{2\pi \hbar }}({\tfrac {2m}{E}})^{1/2}}$ . In two dimensions the density of states is a constant $D_{2D}={\tfrac {m}{2\pi \hbar ^{2}}}$ , while in three dimensions it becomes $D_{3D}(E)={\tfrac {m}{2\pi ^{2}\hbar ^{3}}}(2mE)^{1/2}$ .

Equivalently, the density of states can also be understood as the derivative of the microcanonical partition function $Z_{m}(E)$ (that is, the total number of states with energy less than E ) with respect to the energy: $D(E)={\frac {1}{V}}\cdot {\frac {\mathrm {d} Z_{m}(E)}{\mathrm {d} E}}.$

The number of states with energy $E'$ (degree of degeneracy) is given by: $g\left(E'\right)=\lim _{\Delta E\to 0}\int _{E'}^{E'+\Delta E}D(E)\,\mathrm {d} E=\lim _{\Delta E\to 0}D\left(E'\right)\Delta E,$ where the last equality only applies when the mean value theorem for integrals is valid.

## Symmetry

There is a large variety of systems and types of states for which DOS calculations can be done.

Some condensed matter systems possess a structural symmetry on the microscopic scale which can be exploited to simplify calculation of their densities of states. In spherically symmetric systems, the integrals of functions are one-dimensional because all variables in the calculation depend only on the radial parameter of the dispersion relation. Fluids, glasses and amorphous solids are examples of a symmetric system whose dispersion relations have a rotational symmetry.

Measurements on powders or polycrystalline samples require evaluation and calculation functions and integrals over the whole domain, most often a Brillouin zone, of the dispersion relations of the system of interest. Sometimes the symmetry of the system is high, which causes the shape of the functions describing the dispersion relations of the system to appear many times over the whole domain of the dispersion relation. In such cases the effort to calculate the DOS can be reduced by a great amount when the calculation is limited to a reduced zone or fundamental domain. The Brillouin zone of the face-centered cubic lattice (FCC) in the figure on the right has the 48-fold symmetry of the point group *Oh* with full octahedral symmetry. This configuration means that the integration over the whole domain of the Brillouin zone can be reduced to a 48-th part of the whole Brillouin zone. As a crystal structure periodic table shows, there are many elements with a FCC crystal structure, like diamond, silicon and platinum and their Brillouin zones and dispersion relations have this 48-fold symmetry. Two other familiar crystal structures are the body-centered cubic lattice (BCC) and hexagonal closed packed structures (HCP) with cubic and hexagonal lattices, respectively. The BCC structure has the 24-fold pyritohedral symmetry of the point group *Th*. The HCP structure has the 12-fold prismatic dihedral symmetry of the point group *D3h*. A complete list of symmetry properties of a point group can be found in point group character tables.

In general it is easier to calculate a DOS when the symmetry of the system is higher and the number of topological dimensions of the dispersion relation is lower. The DOS of dispersion relations with rotational symmetry can often be calculated analytically. This result is fortunate, since many materials of practical interest, such as steel and silicon, have high symmetry.

In anisotropic condensed matter systems such as a single crystal of a compound, the density of states could be different in one crystallographic direction than in another. These causes the anisotropic density of states to be more difficult to visualize, and might require methods such as calculating the DOS for particular points or directions only, or calculating the projected density of states (PDOS) to a particular crystal orientation.

## *k*-space topologies

The density of states is dependent upon the dimensional limits of the object itself. In a system described by three orthogonal parameters (3 Dimension), the units of DOS is [Energy]−1[Volume]−1, in a two dimensional system, the units of DOS is [Energy]−1[Area]−1, in a one dimensional system, the units of DOS is [Energy]−1[Length]−1. The referenced volume is the volume of *k*-space; the space enclosed by the constant energy surface of the system derived through a dispersion relation that relates *E* to *k*. An example of a 3-dimensional *k*-space is given in Fig. 1. It can be seen that the dimensionality of the system confines the momentum of particles inside the system.

### Density of wave vector states (sphere)

The calculation for DOS starts by counting the *N* allowed states at a certain *k* that are contained within [*k*, *k* + d*k*] inside the volume of the system. This procedure is done by differentiating the whole k-space volume $\Omega _{n,k}$ in n-dimensions at an arbitrary *k*, with respect to *k*. The volume, area or length in 3, 2 or 1-dimensional spherical *k*-spaces are expressed by $\Omega _{n}(k)=c_{n}k^{n}$

for a *n*-dimensional *k*-space with the topologically determined constants $c_{1}=2,\ c_{2}=\pi ,\ c_{3}={\frac {4\pi }{3}}$ for linear, disk and spherical symmetrical shaped functions in 1, 2 and 3-dimensional Euclidean *k*-spaces respectively.

According to this scheme, the density of wave vector states *N* is, through differentiating $\Omega _{n,k}$ with respect to *k*, expressed by $N_{n}(k)={\frac {\mathrm {d} \Omega _{n}(k)}{\mathrm {d} k}}=n\;c_{n}\;k^{n-1}$

The 1, 2 and 3-dimensional density of wave vector states for a line, disk, or sphere are explicitly written as ${\begin{aligned}N_{1}(k)&=2\\N_{2}(k)&=2\pi k\\N_{3}(k)&=4\pi k^{2}\end{aligned}}$

One state is large enough to contain particles having wavelength λ. The wavelength is related to *k* through the relationship. $k={\frac {2\pi }{\lambda }}$

In a quantum system the length of λ will depend on a characteristic spacing of the system L that is confining the particles. Finally the density of states *N* is multiplied by a factor $s/V_{k}$ , where *s* is a constant degeneracy factor that accounts for internal degrees of freedom due to such physical phenomena as spin or polarization. If no such phenomenon is present then $s=1$ . *Vk* is the volume in k-space whose wavevectors are smaller than the smallest possible wavevectors decided by the characteristic spacing of the system.

### Density of energy states

To finish the calculation for DOS find the number of states per unit sample volume at an energy E inside an interval $[E,E+\mathrm {d} E]$ . The general form of DOS of a system is given as $D_{n}\left(E\right)={\frac {\mathrm {d} \Omega _{n}(E)}{\mathrm {d} E}}$ The scheme sketched so far *only* applies to *monotonically rising* and *spherically symmetric* dispersion relations. In general the dispersion relation $E(k)$ is not spherically symmetric and in many cases it isn't continuously rising either. To express *D* as a function of *E* the inverse of the dispersion relation $E(k)$ has to be substituted into the expression of $\Omega _{n}(k)$ as a function of *k* to get the expression of $\Omega _{n}(E)$ as a function of the energy. If the dispersion relation is not spherically symmetric or continuously rising and can't be inverted easily then in most cases the DOS has to be calculated numerically. More detailed derivations are available.

## Dispersion relations

The dispersion relation for electrons in a solid is given by the electronic band structure.

The kinetic energy of a particle depends on the magnitude and direction of the wave vector *k*, the properties of the particle and the environment in which the particle is moving. For example, the kinetic energy of an electron in a Fermi gas is given by $E=E_{0}+{\frac {\left(\hbar k\right)^{2}}{2m}}\ ,$

where *m* is the electron mass. The dispersion relation is a spherically symmetric parabola and it is continuously rising so the DOS can be calculated easily.

For longitudinal phonons in a string of atoms the dispersion relation of the kinetic energy in a 1-dimensional *k*-space, as shown in Figure 2, is given by $E=2\hbar \omega _{0}\left|\sin \left({\frac {ka}{2}}\right)\right|$ where ${\textstyle \omega _{0}={\sqrt {k_{\text{F}}/m}}}$ is the oscillator frequency, m the mass of the atoms, $k_{\text{F}}$ the inter-atomic force constant and a inter-atomic spacing. For small values of $k\ll \pi /a$ the dispersion relation is linear: $E=\hbar \omega _{0}ka$

When $k\approx \pi /a$ the energy is $E=2\hbar \omega _{0}\left|\cos \left({\frac {\pi -ka}{2}}\right)\right|$

With the transformation $q=k-\pi /a$ and small q this relation can be transformed to $E\approx 2\hbar \omega _{0}\left[1-\left({\frac {qa}{2}}\right)^{2}\right]$

### Isotropic dispersion relations

The two examples mentioned here can be expressed like $E=E_{0}+c_{k}k^{p}$

This expression is a kind of dispersion relation because it interrelates two wave properties and it is isotropic because only the length and not the direction of the wave vector appears in the expression. The magnitude of the wave vector is related to the energy as: $k=\left({\frac {E-E_{0}}{c_{k}}}\right)^{{1}/{p}},$

Accordingly, the volume of n-dimensional *k*-space containing wave vectors smaller than *k* is: $\Omega _{n}(k)=c_{n}k^{n}$

Substitution of the isotropic energy relation gives the volume of occupied states $\Omega _{n}(E)={\frac {c_{n}}{{c_{k}}^{\frac {n}{p}}}}\left(E-E_{0}\right)^{{n}/{p}},$

Differentiating this volume with respect to the energy gives an expression for the DOS of the isotropic dispersion relation $D_{n}\left(E\right)={\frac {\mathrm {d} }{\mathrm {d} E}}\Omega _{n}(E)={\frac {nc_{n}}{p{c_{k}}^{\frac {n}{p}}}}\left(E-E_{0}\right)^{{\frac {n}{p}}-1}$

### Parabolic dispersion

In the case of a parabolic dispersion relation (*p* = 2), such as applies to free electrons in a Fermi gas, the resulting density of states, $D_{n}\left(E\right)$ , for electrons in a n-dimensional systems is

${\begin{aligned}D_{1}\left(E\right)&={\frac {1}{\sqrt {c_{k}\left(E-E_{0}\right)}}}\\[1ex]D_{2}\left(E\right)&={\frac {\pi }{c_{k}}}\\[1ex]D_{3}\left(E\right)&=2\pi {\sqrt {\frac {E-E_{0}}{c_{k}^{3}}}}\,.\end{aligned}}$

for $E>E_{0}$ , with $D(E)=0$ for $E<E_{0}$ .

In 1-dimensional systems the DOS diverges at the bottom of the band as E drops to $E_{0}$ . In 2-dimensional systems the DOS turns out to be independent of E . Finally for 3-dimensional systems the DOS rises as the square root of the energy.

Including the prefactor $s/V_{k}$ , the expression for the 3D DOS is $N(E)={\frac {V}{2\pi ^{2}}}\left({\frac {2m}{\hbar ^{2}}}\right)^{\frac {3}{2}}{\sqrt {E-E_{0}}},$

where V is the total volume, and $N(E-E_{0})$ includes the 2-fold spin degeneracy.

### Linear dispersion

In the case of a linear relation (*p* = 1), such as applies to photons, acoustic phonons, or to some special kinds of electronic bands in a solid, the DOS in 1, 2 and 3 dimensional systems is related to the energy as:

${\begin{aligned}D_{1}\left(E\right)&={\frac {2\pi }{c_{k}}}\\[1ex]D_{2}\left(E\right)&=2\pi {\frac {E-E_{0}}{c_{k}^{2}}}\\[1ex]D_{3}\left(E\right)&=4\pi {\frac {\left(E-E_{0}\right)^{2}}{c_{k}^{3}}}\end{aligned}}$

## Distribution functions

The density of states plays an important role in the kinetic theory of solids. The product of the density of states and the probability distribution function is the number of occupied states per unit volume at a given energy for a system in thermal equilibrium. This value is widely used to investigate various physical properties of matter. The following are examples, using two common distribution functions, of how applying a distribution function to the density of states can give rise to physical properties.

Fermi–Dirac statistics: The Fermi–Dirac probability distribution function, Fig. 4, is used to find the probability that a fermion occupies a specific quantum state in a system at thermal equilibrium. Fermions are particles which obey the Pauli exclusion principle (e.g. electrons, protons, neutrons). The distribution function can be written as $f_{\mathrm {FD} }(E)={\frac {1}{\exp \left({\frac {E-\mu }{k_{\mathrm {B} }T}}\right)+1}}.$

$\mu$ is the chemical potential (also denoted as EF and called the Fermi level when *T*=0), $k_{\mathrm {B} }$ is the Boltzmann constant, and T is temperature. Fig. 4 illustrates how the product of the Fermi-Dirac distribution function and the three-dimensional density of states for a semiconductor can give insight to physical properties such as carrier concentration and Energy band gaps.

Bose–Einstein statistics: The Bose–Einstein distribution function $f_{\mathrm {BE} }(E)$ is the average number of bosons occupying any quantum state with energy E in a system at thermal equilibrium. Bosons are particles which do not obey the Pauli exclusion principle (e.g. phonons and photons), so $f_{\mathrm {BE} }(E)$ can be greater than 1. The distribution function can be written as $f_{\mathrm {BE} }(E)={\frac {1}{\exp \left({\frac {E-\mu }{k_{\text{B}}T}}\right)-1}}.$

From these two distributions it is possible to calculate properties such as the internal energy per unit volume u , the number of particles N , specific heat capacity c , and thermal conductivity k . The relationships between these properties and the product of the density of states and the probability distribution, denoting the density of states by $g(E)$ instead of $D(E)$ , are given by ${\begin{aligned}u&=\int E\,f(E)\,g(E)\,\mathrm {d} E\\[1ex]N&=V\int f(E)\,g(E)\,\mathrm {d} E\\[1ex]c&={\frac {\partial }{\partial T}}\int E\,f(E)\,g(E)\,\mathrm {d} E\\[1ex]k&={\frac {1}{d}}{\frac {\partial }{\partial T}}\int Ef(E)\,g(E)\,\nu (E)\,\Lambda (E)\,\mathrm {d} E\end{aligned}}$

d is dimensionality, $\nu$ is sound velocity and $\Lambda$ is mean free path.

## Applications

The density of states appears in many areas of physics, and helps to explain a number of quantum mechanical phenomena.

### Quantization

Calculating the density of states for small structures shows that the distribution of electrons changes as dimensionality is reduced. For quantum wires, the DOS for certain energies actually becomes higher than the DOS for bulk semiconductors, and for quantum dots the electrons become quantized to certain energies.

### Photonic crystals

The photon density of states can be manipulated by using periodic structures with length scales on the order of the wavelength of light. Some structures can completely inhibit the propagation of light of certain colors (energies), creating a photonic band gap: the DOS is zero for those photon energies. Other structures can inhibit the propagation of light only in certain directions to create mirrors, waveguides, and cavities. Such periodic structures are known as photonic crystals. In nanostructured media the concept of local density of states (LDOS) is often more relevant than that of DOS, as the DOS varies considerably from point to point.

## Computational calculation

Interesting systems are in general complex, for instance compounds, biomolecules, polymers, etc. Because of the complexity of these systems the analytical calculation of the density of states is in most of the cases impossible. Computer simulations offer a set of algorithms to evaluate the density of states with a high accuracy. One of these algorithms is called the Wang and Landau algorithm.

Within the Wang and Landau scheme any previous knowledge of the density of states is required. One proceeds as follows: the cost function (for example the energy) of the system is discretized. Each time the bin *i* is reached one updates a histogram for the density of states, $g(i)$ , by $g(i)\rightarrow g(i)+f$ where *f* is called the modification factor. As soon as each bin in the histogram is visited a certain number of times (10-15), the modification factor is reduced by some criterion, for instance, $f_{n+1}\rightarrow {\frac {1}{2}}f_{n}$ where *n* denotes the *n*-th update step. The simulation finishes when the modification factor is less than a certain threshold, for instance $f_{n}<10^{-8}$ .

The Wang and Landau algorithm has some advantages over other common algorithms such as multicanonical simulations and parallel tempering. For example, the density of states is obtained as the main product of the simulation. Additionally, Wang and Landau simulations are completely independent of the temperature. This feature allows to compute the density of states of systems with very rough energy landscape such as proteins.

Mathematically the density of states is formulated in terms of a tower of covering maps.

## Local density of states

An important feature of the definition of the DOS is that it can be extended to any system. One of its properties are the translationally invariability which means that the density of the states is homogeneous and it's the same at each point of the system. But this is just a particular case and the LDOS gives a wider description with a heterogeneous density of states through the system.

### Concept

**Local density of states** (LDOS) describes a space-resolved density of states. In materials science, for example, this term is useful when interpreting the data from a scanning tunneling microscope (STM), since this method is capable of imaging electron densities of states with atomic resolution. According to crystal structure, this quantity can be predicted by computational methods, as for example with density functional theory.

### A general definition

In a local density of states the contribution of each state is weighted by the density of its wave function at the point. $N(E)$ becomes $n(E,x)$

$n(E,x)=\sum _{j}|\phi _{j}(x)|^{2}\delta (E-\varepsilon _{j})$

the factor of $|\phi _{j}(x)|^{2}$ means that each state contributes more in the regions where the density is high. An average over x of this expression will restore the usual formula for a DOS. The LDOS is useful in inhomogeneous systems, where $n(E,x)$ contains more information than $n(E)$ alone.

For a one-dimensional system with a wall, the sine waves give

$n_{1D}(E,x)={\frac {2}{\pi \hbar }}{\sqrt {\frac {2m}{E}}}\sin ^{2}{kx}$

where ${\textstyle k={\sqrt {2mE}}/\hbar }$ .

In a three-dimensional system with $x>0$ the expression is

$n_{3D}(E,x)=\left(1-{\frac {\sin {2kx}}{2kx}}\right)n_{3D}(E)$

In fact, we can generalise the local density of states further to

$n(E,x,x')=\sum _{j}\phi _{j}(x)\phi _{j}^{*}(x')\delta (E-\varepsilon _{j})$

this is called the *spectral function* and it's a function with each wave function separately in its own variable. In more advanced theory it is connected with the Green's functions and provides a compact representation of some results such as optical absorption.

### Solid state devices

LDOS can be used to gain profit into a solid-state device. For example, the figure on the right illustrates LDOS of a transistor as it turns on and off in a ballistic simulation. The LDOS has clear boundary in the source and drain, that corresponds to the location of band edge. In the channel, the DOS is increasing as gate voltage increase and potential barrier goes down.

### Optics and photonics

In optics and photonics, the concept of local density of states refers to the states that can be occupied by a photon. For light it is usually measured by fluorescence methods, near-field scanning methods or by cathodoluminescence techniques. Different photonic structures have different LDOS behaviors with different consequences for spontaneous emission. In photonic crystals, near-zero LDOS are expected, inhibiting spontaneous emission. Similar LDOS enhancement is also expected in plasmonic cavity. However, in disordered photonic nanostructures, the LDOS behave differently. They fluctuate spatially with their statistics, and are proportional to the scattering strength of the structures. In addition, the relationship with the mean free path of the scattering is trivial as the LDOS can be still strongly influenced by the short details of strong disorders in the form of a strong Purcell enhancement of the emission. and finally, for the plasmonic disorder, this effect is much stronger for LDOS fluctuations as it can be observed as a strong near-field localization.
