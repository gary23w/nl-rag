---
title: "Buckingham potential"
source: https://en.wikipedia.org/wiki/Buckingham_potential
domain: buckingham-potential
license: CC-BY-SA-4.0
tags: buckingham potential
fetched: 2026-07-04
---

# Buckingham potential

In theoretical chemistry, the **Buckingham potential** is a model of intermolecular interactions based on pair potentials developed by Richard Buckingham. The model describes repulsion by the Pauli exclusion principle and attraction by van der Waals forces between all atom pairs that are not directly bonded as a function of the interatomic distance r .

The interatomic potential,

$\Phi _{12}(r)=A\exp \left(-Br\right)-{\frac {C}{r^{6}}}$

is given by two terms that represent the attraction and the repulsion, respectively. The constants, A , B , and C are parametrizations of the model tuned to the specific type of each atom pair.

Buckingham proposed this as a simplification of the Lennard-Jones potential, in a theoretical study of the equation of state for gaseous helium, neon and argon.

As explained in Buckingham's original paper and, e.g., in section 2.2.5 of Jensen's text, the repulsion is due to the interpenetration of the closed electron shells. "There is therefore some justification for choosing the repulsive part (of the potential) as an exponential function". The Buckingham potential has been used extensively in simulations of molecular dynamics.

Because the exponential term converges to a constant with decreasing distance, while the $r^{-6}$ term diverges, the Buckingham potential becomes attractive as r becomes small. This may be problematic when dealing with a structure with very short interatomic distances, as any nuclei that cross a certain threshold will become strongly (and unphysically) bound to one another at a distance of zero.

## Modified Buckingham (Exp-Six) potential

The modified Buckingham potential, also called the "exp-six" potential, is used to calculate the interatomic forces for gases based on Chapman and Cowling collision theory. The potential has the form

$\Phi _{12}(r)={\frac {\epsilon }{1-6/\alpha }}\left[{\frac {6}{\alpha }}\exp \left[\alpha \left(1-{\frac {r}{r_{min}}}\right)\right]-\left({\frac {r_{min}}{r}}\right)^{6}\right]$

where $\Phi _{12}(r)$ is the interatomic potential between atom i and atom j, $\epsilon$ is the minimum potential energy, $\alpha$ is the measurement of the repulsive energy steepness which is the ratio $\sigma /r_{min}$ , $\sigma$ is the value of r where $\Phi _{12}(r)$ is zero, and $r_{min}$ is the value of r which can achieve the minimum interatomic potential $\epsilon$ . This potential function is only valid when $r>r_{max}$ , as the potential will decay towards $-\infty$ as $r\rightarrow 0$ . This is corrected by identifying $r_{max}$ , which is the value of r at which the potential is maximized; when $r\leq {r_{max}}$ , the potential is set to infinity.

## Coulomb–Buckingham potential

The Coulomb–Buckingham potential is an extension of the Buckingham potential for application to ionic systems (e.g. ceramic materials). The formula for the interaction is

$\Phi _{12}(r)=A\exp \left(-Br\right)-{\frac {C}{r^{6}}}+{\frac {q_{1}q_{2}}{4\pi \varepsilon _{0}r}}$

where *A*, *B*, and *C* are suitable constants and the additional term is the electrostatic potential energy.

The above equation may be written in its alternate form as

$\Phi (r)=\varepsilon \left\{{\frac {6}{\alpha -6}}\exp \left(\alpha \left[1-{\frac {r}{r_{0}}}\right]\right)-{\frac {\alpha }{\alpha -6}}\left({\frac {r_{0}}{r}}\right)^{6}\right\}+{\frac {q_{1}q_{2}}{4\pi \varepsilon _{0}r}}$

where $r_{0}$ is the minimum energy distance, $\alpha$ is a free dimensionless parameter and $\varepsilon$ is the depth of the minimum energy.

## Beest Kramer van Santen (BKS) potential

The BKS potential is a force field that may be used to simulate the interatomic potential between Silica glass atoms. Rather than relying only on experimental data, the BKS potential is derived by combining *ab initio* quantum chemistry methods on small silica clusters to describe accurate interaction between nearest-neighbors, which is the function of accurate force field. The experimental data is applied to fit larger scale force information beyond nearest neighbors. By combining the microscopic and macroscopic information, the applicability of the BKS potential has been extended to both the silica polymorphs and other tetrahedral network oxides systems that have same cluster structure, such as aluminophosphates, carbon and silicon.

The form of this interatomic potential is the usual Buckingham form, with the addition of a Coulomb force term. The formula for the BKS potential is expressed as

$\Phi _{ij}(r)=\left[A_{ij}\exp \left(-B_{ij}r_{ij}\right)-{\frac {C_{ij}}{r_{ij}^{6}}}\right]+{\frac {q_{i}q_{j}}{r_{ij}}}$

where $\Phi _{ij}(r)$ is the interatomic potential between atom i and atom j , $q_{i}$ and $q_{j}$ are the charges magnitudes, $r_{ij}$ is the distance between atoms, and $A_{ij}$ , $B_{ij}$ and $C_{ij}$ are constant parameters based on the type of atoms.

The BKS potential parameters for common atoms are shown below:

| i-j | Aij(eV) | Bij(Å−1) | Cij(eV•Å6) |
|---|---|---|---|
| O - O | 1388.7730 | 2.76000 | 175.0000 |
| O - Si | 18,003.757 | 4.87318 | 133.5381 |
| Si - Si | 0 | 0 | 0 |
| Al - O | 16,008.5345 | 4.79667 | 130.5659 |
| Al - Al | 0 | 0 | 0 |
| P - O | 9,034.2080 | 5.19098 | 19.8793 |
| P - P | 0 | 0 | 0 |

An updated version of the BKS potential introduced a new repulsive term to prevent atom overlapping. The modified potential is taken as

$\Phi _{12}(r)=\left[A_{12}\exp \left(-B_{12}r_{12}\right)-{\frac {C_{12}}{r_{12}^{6}}}\right]+{\frac {q_{1}q_{2}}{r_{12}}}+{\frac {D_{12}}{r_{12}^{24}}}$

where the constant parameters $D_{ij}$ were chosen to have the following values for Silica glass:

|   | Si - Si | Si - O | O - O |
|---|---|---|---|
| Dij(eV•Å24) | 3423200 | 29 | 113 |
