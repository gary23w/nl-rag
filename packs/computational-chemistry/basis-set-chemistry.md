---
title: "Basis set (chemistry)"
source: https://en.wikipedia.org/wiki/Basis_set_(chemistry)
domain: computational-chemistry
license: CC-BY-SA-4.0
tags: computational chemistry, density functional theory, hartree-fock method, molecular orbital
fetched: 2026-07-02
---

# Basis set (chemistry)

In theoretical and computational chemistry, a **basis set** is a set of functions (called basis functions) that is used to represent the electronic wave function in the Hartree–Fock method or density-functional theory in order to turn the partial differential equations of the model into algebraic equations suitable for efficient implementation on a computer.

The use of basis sets is equivalent to the use of an approximate resolution of the identity: the atomic orbitals $|\psi _{i}\rangle$ are expanded within the basis set as a linear combination of the basis functions ${\textstyle |\psi _{i}\rangle \approx \sum _{\mu }c_{\mu i}|\mu \rangle }$ , where the expansion coefficients $c_{\mu i}$ are given by ${\textstyle c_{\mu i}=\sum _{\nu }\langle \mu |\nu \rangle ^{-1}\langle \nu |\psi _{i}\rangle }$ .

The basis set can either be composed of atomic orbitals (yielding the linear combination of atomic orbitals approach), which is the usual choice within the quantum chemistry community; plane waves which are typically used within the solid state community, or real-space approaches. Several types of atomic orbitals can be used: Gaussian-type orbitals, Slater-type orbitals, or numerical atomic orbitals. Out of the three, Gaussian-type orbitals are by far the most often used, as they allow efficient implementations of post-Hartree–Fock methods.

## Introduction

In modern computational chemistry, quantum chemical calculations are performed using a finite set of basis functions. When the finite basis is expanded towards an (infinite) complete set of functions, calculations using such a basis set are said to approach the complete basis set (CBS) limit. In this context, *basis function* and *atomic orbital* are sometimes used interchangeably, although the basis functions are usually not true atomic orbitals.

Within the basis set, the wavefunction is represented as a vector, the components of which correspond to coefficients of the basis functions in the linear expansion. In such a basis, one-electron operators correspond to matrices (a.k.a. rank two tensors), whereas two-electron operators are rank four tensors.

When molecular calculations are performed, it is common to use a basis composed of atomic orbitals, centered at each nucleus within the molecule (linear combination of atomic orbitals ansatz). The physically best motivated basis set are Slater-type orbitals (STOs), which are solutions to the Schrödinger equation of hydrogen-like atoms, and decay exponentially far away from the nucleus. It can be shown that the molecular orbitals of Hartree–Fock and density-functional theory also exhibit exponential decay. Furthermore, S-type STOs also satisfy Kato's cusp condition at the nucleus, meaning that they are able to accurately describe electron density near the nucleus. However, hydrogen-like atoms lack many-electron interactions, thus the orbitals do not accurately describe electron state correlations.

Unfortunately, calculating integrals with STOs is computationally difficult and it was later realized by Frank Boys that STOs could be approximated as linear combinations of Gaussian-type orbitals (GTOs) instead. Because the product of two GTOs can be written as a linear combination of GTOs, integrals with Gaussian basis functions can be written in closed form, which leads to huge computational savings (see John Pople).

Dozens of Gaussian-type orbital basis sets have been published in the literature. Basis sets typically come in hierarchies of increasing size, giving a controlled way to obtain more accurate solutions, however at a higher cost.

The smallest basis sets are called *minimal basis sets*. A minimal basis set is one in which, on each atom in the molecule, a single basis function is used for each orbital in a Hartree–Fock calculation on the free atom. For atoms such as lithium, basis functions of p type are also added to the basis functions that correspond to the 1s and 2s orbitals of the free atom, because lithium also has a 1s2p bound state. For example, each atom in the second period of the periodic system (Li – Ne) would have a basis set of five functions (two s functions and three p functions).

A minimal basis set may already be exact for the gas-phase atom at the self-consistent field level of theory. In the next level, additional functions are added to describe polarization of the electron density of the atom in molecules. These are called **polarization functions**. For example, while the minimal basis set for hydrogen is one function approximating the 1s atomic orbital, a simple polarized basis set typically has two s- and one p-function (which consists of three basis functions: px, py and pz). This adds flexibility to the basis set, effectively allowing molecular orbitals involving the hydrogen atom to be more asymmetric about the hydrogen nucleus. This is very important for modeling chemical bonding, because the bonds are often polarized. Similarly, d-type functions can be added to a basis set with valence p orbitals, and f-functions to a basis set with d-type orbitals, and so on.

Another common addition to basis sets is the addition of **diffuse functions**. These are extended Gaussian basis functions with a small exponent, which give flexibility to the "tail" portion of the atomic orbitals, far away from the nucleus. Diffuse basis functions are important for describing anions or dipole moments, but they can also be important for accurate modeling of intra- and inter-molecular bonding.

## STO hierarchy

The most common minimal basis set is STO-nG, where n is an integer. The STO-nG basis sets are derived from a minimal Slater-type orbital basis set, with *n* representing the number of Gaussian primitive functions used to represent each Slater-type orbital. Minimal basis sets typically give rough results that are insufficient for research-quality publication, but are much cheaper than their larger counterparts. Commonly used minimal basis sets of this type are:

- STO-3G
- STO-4G
- STO-6G
- STO-3G* – Polarized version of STO-3G

There are several other minimum basis sets that have been used such as the MidiX basis sets.

## Split-valence basis sets

During most molecular bonding, it is the valence electrons which principally take part in the bonding. In recognition of this fact, it is common to represent valence orbitals by more than one basis function (each of which can in turn be composed of a fixed linear combination of primitive Gaussian functions). Basis sets in which there are multiple basis functions corresponding to each valence atomic orbital are called valence double, triple, quadruple-zeta, and so on, basis sets (zeta, ζ, was commonly used to represent the exponent of an STO basis function). Since the different orbitals of the split have different spatial extents, the combination allows the electron density to adjust its spatial extent appropriate to the particular molecular environment. In contrast, minimal basis sets lack the flexibility to adjust to different molecular environments.

### Pople basis sets

The notation for the *split-valence* basis sets arising from the group of John Pople is typically *X-YZg*. In this case, *X* represents the number of primitive Gaussians comprising each core atomic orbital basis function. The *Y* and *Z* indicate that the valence orbitals are composed of two basis functions each, the first one composed of a linear combination of *Y* primitive Gaussian functions, the other composed of a linear combination of *Z* primitive Gaussian functions. In this case, the presence of two numbers after the hyphens implies that this basis set is a *split-valence double-zeta* basis set. Split-valence triple- and quadruple-zeta basis sets are also used, denoted as *X-YZWg*, *X-YZWVg*, etc.

Polarization functions are denoted by two different notations. The original Pople notation added "*" to indicate that all "heavy" atoms (everything but H and He) have a small set of polarization functions added to the basis (in the case of carbon, a set of 3d orbital functions). The "**" notation indicates that all "light" atoms also receive polarization functions (this adds a set of 2p orbitals to the basis for each hydrogen atom). Eventually it became desirable to add more polarization to the basis sets, and a new notation was developed in which the number and types of polarization functions are given explicitly in parentheses in the order (heavy,light) but with the principal quantum numbers of the orbitals implicit. For example, the * notation becomes (d) and the ** notation is now given as (d,p). If instead 3d and 4f functions were added to each heavy atom and 2p, 3p, 3d functions were added to each light atom, the notation would become (df,2pd).

In all cases, diffuse functions are indicated by either adding a + before the letter G (diffuse functions on heavy atoms only) or ++ (diffuse functions are added to all atoms).

Here is a list of commonly used split-valence basis sets of this type:

- 3-21G
- 3-21G* – Polarization functions on heavy atoms
- 3-21G** – Polarization functions on heavy atoms and hydrogen
- 3-21+G – Diffuse functions on heavy atoms
- 3-21++G – Diffuse functions on heavy atoms and hydrogen
- 3-21+G* – Polarization *and* diffuse functions on heavy atoms only
- 3-21+G** – Polarization functions on heavy atoms and hydrogen, as well as diffuse functions on heavy atoms
- 4-21G
- 4-31G
- 6-21G
- 6-31G
- 6-31G*
- 6-31+G*
- 6-31G(3df,3pd) – 3 sets of d functions and 1 set of f functions on heavy atoms and 3 sets of p functions and 1 set of d functions on hydrogen
- 6-311G
- 6-311G*
- 6-311+G*
- 6-311+G(2df,2p)

In summary; the 6-31G* basis set (defined for the atoms H through Zn) is a split-valence double-zeta polarized basis set that adds to the 6-31G set five *d*-type Cartesian-Gaussian polarization functions on each of the atoms Li through Ca and ten *f*-type Cartesian Gaussian polarization functions on each of the atoms Sc through Zn.

The Pople basis sets were originally developed for use in Hartree-Fock calculations. Since then, correlation-consistent or polarization-consistent basis sets (see below) have been developed which are usually more appropriate for correlated wave function calculations.  For Hartree–Fock or density functional theory, however, Pople basis sets are more efficient (per unit basis function) as compared to other alternatives, provided that the electronic structure program can take advantage of combined *sp* shells, and are still widely used for molecular structure determination of large molecules and as components of quantum chemistry composite methods.

## Correlation-consistent basis sets

Some of the most widely used basis sets are those developed by Dunning and coworkers, since they are designed for converging post-Hartree–Fock calculations systematically to the complete basis set limit using empirical extrapolation techniques.

For first- and second-row atoms, the basis sets are cc-pVNZ where *N* = *D*,*T*,*Q*,5,6,... (*D* = double, *T* = triple, etc.). The 'cc-p', stands for 'correlation-consistent polarized' and the 'V' indicates that only basis sets for the valence orbitals are of multiple-zeta quality. (Like the Pople basis sets, the core orbitals are of single-zeta quality.) They include successively larger shells of polarization (correlating) functions (*d*, *f*, *g*, etc.). More recently these 'correlation-consistent polarized' basis sets have become widely used and are the current state of the art for correlated or post-Hartree–Fock calculations. The *aug-* prefix is added if diffuse functions are included in the basis. Examples of these are:

- cc-pVDZ – Double-zeta
- cc-pVTZ – Triple-zeta
- cc-pVQZ – Quadruple-zeta
- cc-pV5Z – Quintuple-zeta, etc.
- aug-cc-pVDZ, etc. – Augmented versions of the preceding basis sets with added diffuse functions.
- cc-pCVDZ – Double-zeta with core correlation

For period-3 atoms (Al–Ar), additional functions have turned out to be necessary; these are the cc-pV(N+d)Z basis sets. Even larger atoms may employ pseudopotential basis sets, cc-pVNZ-PP, or relativistic-contracted Douglas-Kroll basis sets, cc-pVNZ-DK.

While the usual Dunning basis sets are for valence-only calculations, the sets can be augmented with further functions that describe core electron correlation. These core-valence sets (cc-pCVXZ) can be used to approach the exact solution to the all-electron problem, and they are necessary for accurate geometric and nuclear property calculations.

Weighted core-valence sets (cc-pwCVXZ) have also been recently suggested. The weighted sets aim to capture core-valence correlation, while neglecting most of core-core correlation, in order to yield accurate geometries with smaller cost than the cc-pCVXZ sets.

Diffuse functions can also be added for describing anions and long-range interactions such as Van der Waals forces, or to perform electronic excited-state calculations, electric field property calculations. A recipe for constructing additional augmented functions exists; as many as five augmented functions have been used in second hyperpolarizability calculations in the literature. Because of the rigorous construction of these basis sets, extrapolation can be done for almost any energetic property. However, care must be taken when extrapolating energy differences as the individual energy components converge at different rates: the Hartree–Fock energy converges exponentially, whereas the correlation energy converges only polynomially.

|   | H-He | Li-Ne | Na-Ar |
|---|---|---|---|
| cc-pVDZ | [2*s*1*p*] → 5 func. | [3*s*2*p*1*d*] → 14 func. | [4*s*3*p*1*d*] → 18 func. |
| cc-pVTZ | [3*s*2*p*1*d*] → 14 func. | [4*s*3*p*2*d*1*f*] → 30 func. | [5*s*4*p*2*d*1*f*] → 34 func. |
| cc-pVQZ | [4*s*3*p*2*d*1*f*] → 30 func. | [5*s*4*p*3*d*2*f*1*g*] → 55 func. | [6*s*5*p*3*d*2*f*1*g*] → 59 func. |
| aug-cc-pVDZ | [3*s*2*p*] → 9 func. | [4*s*3*p*2*d*] → 23 func. | [5*s*4*p*2*d*] → 27 func. |
| aug-cc-pVTZ | [4*s*3*p*2*d*] → 23 func. | [5*s*4*p*3*d*2*f*] → 46 func. | [6*s*5*p*3*d*2*f*] → 50 func. |
| aug-cc-pVQZ | [5*s*4*p*3*d*2*f*] → 46 func. | [6*s*5*p*4*d*3*f*2*g*] → 80 func. | [7*s*6*p*4*d*3*f*2*g*] → 84 func. |

To understand how to get the number of functions, consider the cc-pVDZ basis set for H: There are two *s* (*L* = 0) orbitals and one *p* (*L* = 1) orbital that has 3 angular-momentum components along the *z*-axis (*m*L = −1,0,1) corresponding to *p**x*, *p**y* and *p**z*. Thus, there are five spatial orbitals in total. Note that each orbital can hold two electrons of opposite spin.

As another example, Ar [1s, 2s, 2p, 3s, 3p] has 3 s orbitals (*L* = 0) and 2 sets of p orbitals (*L* = 1). Using cc-pVDZ, orbitals are [1s, 2s, 2p, 3s, 3s, 3p, 3p, 3d'] (where ' represents the added in polarisation orbitals), with 4 s orbitals (4 basis functions), 3 sets of p orbitals (3 × 3 = 9 basis functions), and 1 set of d orbitals (5 basis functions). Adding up the basis functions gives a total of 18 functions for Ar with the cc-pVDZ basis-set.

## Polarization-consistent basis sets

Density-functional theory has recently become widely used in computational chemistry. However, the correlation-consistent basis sets described above are suboptimal for density-functional theory, because the correlation-consistent sets have been designed for post-Hartree–Fock, while density-functional theory exhibits much more rapid basis set convergence than wave function methods.

Adopting a similar methodology to the correlation-consistent series, Frank Jensen introduced polarization-consistent (pc-n) basis sets as a way to quickly converge density functional theory calculations to the complete basis set limit. Like the Dunning sets, the pc-n sets can be combined with basis set extrapolation techniques to obtain CBS values.

The pc-n sets can be augmented with diffuse functions to obtain augpc-n sets.

## Karlsruhe basis sets

Some of the various valence adaptations of Karlsruhe basis sets are briefly described below.

- def2-SV(P) – Split valence with polarization functions on heavy atoms (not hydrogen)
- def2-SVP – Split valence polarization
- def2-SVPD – Split valence polarization with diffuse functions
- def2-TZVP – Valence triple-zeta polarization
- def2-TZVPD – Valence triple-zeta polarization with diffuse functions
- def2-TZVPP – Valence triple-zeta with two sets of polarization functions
- def2-TZVPPD – Valence triple-zeta with two sets of polarization functions and a set of diffuse functions
- def2-QZVP – Valence quadruple-zeta polarization
- def2-QZVPD – Valence quadruple-zeta polarization with diffuse functions
- def2-QZVPP – Valence quadruple-zeta with two sets of polarization functions
- def2-QZVPPD – Valence quadruple-zeta with two sets of polarization functions and a set of diffuse functions

## Completeness-optimized basis sets

Gaussian-type orbital basis sets are typically optimized to reproduce the lowest possible energy for the systems used to train the basis set. However, the convergence of the energy does not imply convergence of other properties, such as nuclear magnetic shieldings, the dipole moment, or the electron momentum density, which probe different aspects of the electronic wave function.

Manninen and Vaara have proposed completeness-optimized basis sets, where the exponents are obtained by maximization of the one-electron completeness profile instead of minimization of the energy. Completeness-optimized basis sets are a way to easily approach the complete basis set limit of any property at any level of theory, and the procedure is simple to automatize.

Completeness-optimized basis sets are tailored to a specific property. This way, the flexibility of the basis set can be focused on the computational demands of the chosen property, typically yielding much faster convergence to the complete basis set limit than is achievable with energy-optimized basis sets.

## Even-tempered basis sets

In 1974 Bardo and Ruedenberg proposed a simple scheme to generate the exponents of a basis set that spans the Hilbert space evenly by following a geometric progression of the form: $\alpha _{i,l}=\alpha _{l}\beta _{l}^{i-1},\quad \alpha _{l},\beta _{l}>0,\quad \beta _{l}\neq 1\quad i=1,2,\dots ,N_{l}$ for each angular momentum l , where $N_{l}$ is the number of primitives functions. Here, only the two parameters $\alpha _{l}$ and $\beta _{l}$ must be optimized, significantly reducing the dimension of the search space or even avoiding the exponent optimization problem. In order to properly describe electronic delocalized states, a previously optimized standard basis set can be complemented with additional delocalized Gaussian functions with small exponent values, generated by the even-tempered scheme. This approach has also been employed to generate basis sets for other types of quantum particles rather than electrons, like quantum nuclei, negative muons or positrons.

## Plane-wave basis sets

In addition to localized basis sets, plane-wave basis sets can also be used in quantum-chemical simulations. Typically, the choice of the plane wave basis set is based on a cutoff energy. The plane waves in the simulation cell that fit below the energy criterion are then included in the calculation. These basis sets are popular in calculations involving three-dimensional periodic boundary conditions.

The main advantage of a plane-wave basis is that it is guaranteed to converge in a *smooth, monotonic manner* to the target wavefunction. In contrast, when localized basis sets are used, monotonic convergence to the basis set limit may be difficult due to problems with over-completeness: in a large basis set, functions on different atoms start to look alike, and many eigenvalues of the overlap matrix approach zero.

In addition, certain integrals and operations are much easier to program and carry out with plane-wave basis functions than with their localized counterparts. For example, the kinetic energy operator is diagonal in the reciprocal space. Integrals over real-space operators can be efficiently carried out using fast Fourier transforms. The properties of the Fourier Transform allow a vector representing the gradient of the total energy with respect to the plane-wave coefficients to be calculated with a computational effort that scales as NPW*ln(NPW) where NPW is the number of plane-waves. When this property is combined with separable pseudopotentials of the Kleinman-Bylander type and pre-conditioned conjugate gradient solution techniques, the dynamic simulation of periodic problems containing hundreds of atoms becomes possible.

In practice, plane-wave basis sets are often used in combination with an 'effective core potential' or pseudopotential, so that the plane waves are only used to describe the valence charge density. This is because core electrons tend to be concentrated very close to the atomic nuclei, resulting in large wavefunction and density gradients near the nuclei which are not easily described by a plane-wave basis set unless a very high energy cutoff, and therefore small wavelength, is used. This combined method of a plane-wave basis set with a core pseudopotential is often abbreviated as a *PSPW* calculation.

Furthermore, as all functions in the basis are mutually orthogonal and are not associated with any particular atom, plane-wave basis sets do not exhibit basis-set superposition error. However, the plane-wave basis set is dependent on the size of the simulation cell, complicating cell size optimization.

Due to the assumption of periodic boundary conditions, plane-wave basis sets are less well suited to gas-phase calculations than localized basis sets. Large regions of vacuum need to be added on all sides of the gas-phase molecule in order to avoid interactions with the molecule and its periodic copies. However, the plane waves use a similar accuracy to describe the vacuum region as the region where the molecule is, meaning that obtaining the truly noninteracting limit may be computationally costly.

## Linearized augmented-plane-wave basis sets

A combination of some of the properties of localized basis sets and plane-wave approaches is achieved by linearized augmented-plane-wave (LAPW) basis sets. These are based on a partitioning of space into nonoverlapping spheres around each atom and an interstitial region in between the spheres. An LAPW basis function is a plane wave in the interstitial region, which is augmented by numerical atomic functions in each sphere. The numerical atomic functions hereby provide a linearized representation of wave functions for arbitrary energies around automatically determined energy parameters.

Similarly to plane-wave basis sets an LAPW basis set is mainly determined by a cutoff parameter for the plane-wave representation in the interstitial region. In the spheres the variational degrees of freedom can be extended by adding local orbitals to the basis set. This allows representations of wavefunctions beyond the linearized description.

The plane waves in the interstitial region imply three-dimensional periodic boundary conditions, though it is possible to introduce additional augmentation regions to reduce this to one or two dimensions, e.g., for the description of chain-like structures or thin films. The atomic-like representation in the spheres allows to treat each atom with its potential singularity at the nucleus and to not rely on a pseudopotential approximation.

The disadvantage of LAPW basis sets is its complex definition, which comes with many parameters that have to be controlled either by the user or an automatic recipe. Another consequence of the form of the basis set are complex mathematical expressions, e.g., for the calculation of a Hamiltonian matrix or atomic forces.

## Real-space basis sets

Real-space approaches offer powerful methods to solve electronic structure problems thanks to their controllable accuracy. Real-space basis sets can be thought to arise from the theory of interpolation, as the central idea is to represent the (unknown) orbitals in terms of some set of interpolation functions.

Various methods have been proposed for constructing the solution in real space, including finite elements, basis splines, Lagrange sinc-functions, and wavelets. Finite difference algorithms are also often included in this category, even though precisely speaking, they do not form a proper basis set and are not variational unlike e.g. finite element methods.

A common feature of all real-space methods is that the accuracy of the numerical basis set is improvable, so that the complete basis set limit can be reached in a systematical manner. Moreover, in the case of wavelets and finite elements, it is easy to use different levels of accuracy in different parts of the system, so that more points are used close to the nuclei where the wave function undergoes rapid changes and where most of the total energies lie, whereas a coarser representation is sufficient far away from nuclei; this feature is extremely important as it can be used to make all-electron calculations tractable.

For example, in finite element methods (FEMs), the wave function is represented as a linear combination of a set of piecewise polynomials. Lagrange interpolating polynomials (LIPs) are a commonly used basis for FEM calculations. The local interpolation error in LIP basis of order n is of the form $h^{n+1}\max f^{(n+1)}(\xi )$ . The complete basis set can thereby be reached either by going to smaller and smaller elements (i.e. dividing space in smaller and smaller subdivisions; h -adaptive FEM), by switching to the use of higher and higher order polynomials ( p -adaptive FEM), or by a combination of both strategies ( $hp$ -adaptive FEM). The use of high-order LIPs has been shown to be highly beneficial for accuracy.
