---
title: "Coupled cluster"
source: https://en.wikipedia.org/wiki/Coupled_cluster
domain: quantum-chemistry-dft
license: CC-BY-SA-4.0
tags: quantum chemistry, electronic structure, coupled cluster, configuration interaction
fetched: 2026-07-02
---

# Coupled cluster

**Coupled cluster** (**CC**) is a numerical technique used for describing many-body systems. Its most common use is as one of several post-Hartree–Fock ab initio quantum chemistry methods in the field of computational chemistry, but it is also used in nuclear physics. Coupled cluster essentially takes the basic Hartree–Fock molecular orbital method and constructs multi-electron wavefunctions using the exponential cluster operator to account for electron correlation. Some of the most accurate calculations for small to medium-sized molecules use this method.

The method was initially developed by Fritz Coester and Hermann Kümmel in the 1950s for studying nuclear-physics phenomena, but became more frequently used when in 1966 Jiří Čížek (and later together with Josef Paldus) reformulated the method for electron correlation in atoms and molecules. It is now one of the most prevalent methods in quantum chemistry that includes electronic correlation.

CC theory is simply the perturbative variant of the many-electron theory (MET) of Oktay Sinanoğlu, which is the exact (and variational) solution of the many-electron problem, so it was also called "coupled-pair MET (CPMET)". J. Čížek used the correlation function of MET and used Goldstone-type perturbation theory to get the energy expression, while original MET was completely variational. Čížek first developed the linear CPMET and then generalized it to full CPMET in the same work in 1966. He then also performed an application of it on the benzene molecule with Sinanoğlu in the same year. Because MET is somewhat difficult to perform computationally, CC is simpler and thus, in today's computational chemistry, CC is the best variant of MET and gives highly accurate results in comparison to experiments.

## Wavefunction ansatz

Coupled-cluster theory provides the exact solution to the time-independent Schrödinger equation

$H|\Psi \rangle =E|\Psi \rangle ,$

where H is the Hamiltonian of the system, $|\Psi \rangle$ is the exact wavefunction, and *E* is the exact energy of the ground state. Coupled-cluster theory can also be used to obtain solutions for excited states using, for example, linear-response, equation-of-motion, state-universal multi-reference, or valence-universal multi-reference coupled cluster approaches.

The wavefunction of the coupled-cluster theory is written as an exponential ansatz:

$|\Psi \rangle =e^{T}|\Phi _{0}\rangle ,$

where $|\Phi _{0}\rangle$ is the reference wave function, which is typically a Slater determinant constructed from Hartree–Fock molecular orbitals, though other wave functions such as configuration interaction, multi-configurational self-consistent field, or Brueckner orbitals can also be used. T is the cluster operator, which, when acting on $|\Phi _{0}\rangle$ , produces a linear combination of excited determinants from the reference wave function (see section below for greater detail).

The choice of the exponential ansatz is opportune because (unlike other ansatzes, for example, configuration interaction) it guarantees the size extensivity of the solution. Size consistency in CC theory, also unlike other theories, does not depend on the size consistency of the reference wave function. This is easily seen, for example, in the single bond breaking of F2 when using a restricted Hartree–Fock (RHF) reference, which is not size-consistent, at the CCSDT (coupled cluster single-double-triple) level of theory, which provides an almost exact, full-CI-quality, potential-energy surface and does not dissociate the molecule into F− and F+ ions, like the RHF wave function, but rather into two neutral F atoms. If one were to use, for example, the CCSD, or CCSD(T) levels of theory, they would not provide reasonable results for the bond breaking of F2, with the latter one approaches unphysical potential energy surfaces, though this is for reasons other than just size consistency.

A criticism of the method is that the conventional implementation employing the similarity-transformed Hamiltonian (see below) is not variational, though there are bi-variational and quasi-variational approaches that have been developed since the first implementations of the theory. While the above ansatz for the wave function itself has no natural truncation, however, for other properties, such as energy, there is a natural truncation when examining expectation values, which has its basis in the linked- and connected-cluster theorems, and thus does not suffer from issues such as lack of size extensivity, like the variational configuration-interaction approach.

## Cluster operator

The cluster operator is written in the form

$T=T_{1}+T_{2}+T_{3}+\cdots ,$

where $T_{1}$ is the operator of all single excitations, $T_{2}$ is the operator of all double excitations, and so forth. In the formalism of second quantization these excitation operators are expressed as

$T_{1}=\sum _{i}\sum _{a}t_{a}^{i}{\hat {a}}^{a}{\hat {a}}_{i},$

$T_{2}={\frac {1}{4}}\sum _{i,j}\sum _{a,b}t_{ab}^{ij}{\hat {a}}^{a}{\hat {a}}^{b}{\hat {a}}_{j}{\hat {a}}_{i},$

and for the general *n*-fold cluster operator

$T_{n}={\frac {1}{(n!)^{2}}}\sum _{i_{1},i_{2},\ldots ,i_{n}}\sum _{a_{1},a_{2},\ldots ,a_{n}}t_{a_{1},a_{2},\ldots ,a_{n}}^{i_{1},i_{2},\ldots ,i_{n}}{\hat {a}}^{a_{1}}{\hat {a}}^{a_{2}}\ldots {\hat {a}}^{a_{n}}{\hat {a}}_{i_{n}}\ldots {\hat {a}}_{i_{2}}{\hat {a}}_{i_{1}}.$

In the above formulae ${\hat {a}}^{a}={\hat {a}}_{a}^{\dagger }$ and ${\hat {a}}_{i}$ denote the creation and annihilation operators respectively, while *i*, *j* stand for occupied (hole) and *a*, *b* for unoccupied (particle) orbitals (states). The creation and annihilation operators in the coupled-cluster terms above are written in canonical form, where each term is in the normal order form, with respect to the Fermi vacuum $|\Phi _{0}\rangle$ . Being the one-particle cluster operator and the two-particle cluster operator, $T_{1}$ and $T_{2}$ convert the reference function $|\Phi _{0}\rangle$ into a linear combination of the singly and doubly excited Slater determinants respectively, if applied without the exponential (such as in CI, where a linear excitation operator is applied to the wave function). Applying the exponential cluster operator to the wave function, one can then generate more than doubly excited determinants due to the various powers of $T_{1}$ and $T_{2}$ that appear in the resulting expressions (see below). Solving for the unknown coefficients $t_{a}^{i}$ and $t_{ab}^{ij}$ is necessary for finding the approximate solution $|\Psi \rangle$ .

The exponential operator $e^{T}$ may be expanded as a Taylor series, and if we consider only the $T_{1}$ and $T_{2}$ cluster operators of T , we can write

$e^{T}=1+T+{\frac {1}{2!}}T^{2}+\cdots =1+T_{1}+T_{2}+{\frac {1}{2}}T_{1}^{2}+{\frac {1}{2}}T_{1}T_{2}+{\frac {1}{2}}T_{2}T_{1}+{\frac {1}{2}}T_{2}^{2}+\cdots$

Though in practice this series is finite because the number of occupied molecular orbitals is finite, as is the number of excitations, it is still very large, to the extent that even modern-day massively parallel computers are inadequate, except for problems of a dozen or so electrons and very small basis sets, when considering all contributions to the cluster operator and not just $T_{1}$ and $T_{2}$ . Often, as was done above, the cluster operator includes only singles and doubles (see CCSD below) as this offers a computationally affordable method that performs better than MP2 and CISD, but is not very accurate usually. For accurate results some form of triples (approximate or full) are needed, even near the equilibrium geometry (in the Franck–Condon region), and especially when breaking single bonds or describing diradical species (these latter examples are often what is referred to as multi-reference problems, since more than one determinant has a significant contribution to the resulting wave function). For double-bond breaking and more complicated problems in chemistry, quadruple excitations often become important as well, though usually they have small contributions for most problems, and as such, the contribution of $T_{5}$ , $T_{6}$ etc. to the operator T is typically small. Furthermore, if the highest excitation level in the T operator is *n*,

$T=T_{1}+...+T_{n},$

then Slater determinants for an *N*-electron system excited more than n ( $<N$ ) times may still contribute to the coupled-cluster wave function $|\Psi \rangle$ because of the non-linear nature of the exponential ansatz, and therefore, coupled cluster terminated at $T_{n}$ usually recovers more correlation energy than CI with maximum *n* excitations.

## Coupled-cluster equations

The Schrödinger equation can be written, using the coupled-cluster wave function, as

$H|\Psi _{0}\rangle =He^{T}|\Phi _{0}\rangle =Ee^{T}|\Phi _{0}\rangle ,$

where there are a total of *q* coefficients (*t*-amplitudes) to solve for. To obtain the *q* equations, first, we multiply the above Schrödinger equation on the left by $e^{-T}$ and then project onto the entire set of up to *m*-tuply excited determinants, where *m* is the highest-order excitation included in T that can be constructed from the reference wave function $|\Phi _{0}\rangle$ , denoted by $|\Phi ^{*}\rangle$ . Individually, $|\Phi _{i}^{a}\rangle$ are singly excited determinants where the electron in orbital *i* has been excited to orbital *a*; $|\Phi _{ij}^{ab}\rangle$ are doubly excited determinants where the electron in orbital *i* has been excited to orbital *a* and the electron in orbital *j* has been excited to orbital *b*, etc. In this way we generate a set of coupled energy-independent non-linear algebraic equations needed to determine the *t*-amplitudes:

$\langle \Phi _{0}|e^{-T}He^{T}|\Phi _{0}\rangle =E\langle \Phi _{0}|\Phi _{0}\rangle =E,$

$\langle \Phi ^{*}|e^{-T}He^{T}|\Phi _{0}\rangle =E\langle \Phi ^{*}|\Phi _{0}\rangle =0,$

the latter being the equations to be solved, and the former the equation for the evaluation of the energy. (Note that we have made use of $e^{-T}e^{T}=1$ , the identity operator, and also assume that orbitals are orthogonal, though this does not necessarily have to be true, e.g., valence bond orbitals can be used, and in such cases the last set of equations are not necessarily equal to zero.)

Considering the basic CCSD method:

$\langle \Phi _{0}|e^{-(T_{1}+T_{2})}He^{(T_{1}+T_{2})}|\Phi _{0}\rangle =E,$

$\langle \Phi _{i}^{a}|e^{-(T_{1}+T_{2})}He^{(T_{1}+T_{2})}|\Phi _{0}\rangle =0,$

$\langle \Phi _{ij}^{ab}|e^{-(T_{1}+T_{2})}He^{(T_{1}+T_{2})}|\Phi _{0}\rangle =0,$

in which the similarity-transformed Hamiltonian ${\bar {H}}$ can be explicitly written down using Hadamard's formula in Lie algebra, also called Hadamard's lemma (see also Baker–Campbell–Hausdorff formula (BCH formula), though note that they are different, in that Hadamard's formula is a lemma of the BCH formula):

${\bar {H}}=e^{-T}He^{T}=H+[H,T]+{\frac {1}{2!}}{\big [}[H,T],T{\big ]}+\dots =(He^{T})_{C}.$

The subscript *C* designates the connected part of the corresponding operator expression.

The resulting similarity-transformed Hamiltonian is non-Hermitian, resulting in different left and right vectors (wave functions) for the same state of interest (this is what is often referred to in coupled-cluster theory as the biorthogonality of the solution, or wave function, though it also applies to other non-Hermitian theories as well). The resulting equations are a set of non-linear equations, which are solved in an iterative manner. Standard quantum-chemistry packages (GAMESS (US), NWChem, ACES II, etc.) solve the coupled-cluster equations using the Jacobi method and direct inversion of the iterative subspace (DIIS) extrapolation of the *t*-amplitudes to accelerate convergence.

## Types of coupled-cluster methods

The classification of traditional coupled-cluster methods rests on the highest number of excitations allowed in the definition of T . The abbreviations for coupled-cluster methods usually begin with the letters "CC" (for "coupled cluster") followed by

1. S – for single excitations (shortened to *singles* in coupled-cluster terminology),
2. D – for double excitations (*doubles*),
3. T – for triple excitations (*triples*),
4. Q – for quadruple excitations (*quadruples*).

Thus, the T operator in CCSDT has the form

$T=T_{1}+T_{2}+T_{3}.$

Terms in round brackets indicate that these terms are calculated based on perturbation theory. For example, the CCSD(T) method means:

1. Coupled cluster with a full treatment singles and doubles.
2. An estimate to the connected triples contribution is calculated non-iteratively using many-body perturbation theory arguments.

## General description of the theory

The complexity of equations and the corresponding computer codes, as well as the cost of the computation, increases sharply with the highest level of excitation. For many applications CCSD, while relatively inexpensive, does not provide sufficient accuracy except for the smallest systems (approximately 2 to 4 electrons), and often an approximate treatment of triples is needed. The most well known coupled-cluster method that provides an estimate of connected triples is CCSD(T), which provides a good description of closed-shell molecules near the equilibrium geometry, but breaks down in more complicated situations such as bond breaking and diradicals. Another popular method that makes up for the failings of the standard CCSD(T) approach is CR-CC(2,3), where the triples contribution to the energy is computed from the difference between the exact solution and the CCSD energy and is not based on perturbation-theory arguments. More complicated coupled-cluster methods such as CCSDT and CCSDTQ are used only for high-accuracy calculations of small molecules. The inclusion of all *n* levels of excitation for the *n*-electron system gives the exact solution of the Schrödinger equation within the given basis set, within the Born–Oppenheimer approximation (although schemes have also been drawn up to work without the BO approximation).

One possible improvement to the standard coupled-cluster approach is to add terms linear in the interelectronic distances through methods such as CCSD-R12. This improves the treatment of dynamical electron correlation by satisfying the Kato cusp condition and accelerates convergence with respect to the orbital basis set. Unfortunately, R12 methods invoke the resolution of the identity, which requires a relatively large basis set in order to be a good approximation.

The coupled-cluster method described above is also known as the *single-reference* (SR) coupled-cluster method because the exponential ansatz involves only one reference function $|\Phi _{0}\rangle$ . The standard generalizations of the SR-CC method are the *multi-reference* (MR) approaches: state-universal coupled cluster (also known as Hilbert space coupled cluster), valence-universal coupled cluster (or Fock space coupled cluster) and state-selective coupled cluster (or state-specific coupled cluster).

## Historical accounts

Kümmel comments:

> Considering the fact that the CC method was well understood around the late fifties[,] it looks strange that nothing happened with it until 1966, as Jiří Čížek published his first paper on a quantum chemistry problem. He had looked into the 1957 and 1960 papers published in *Nuclear Physics* by Fritz and myself. I always found it quite remarkable that a quantum chemist would open an issue of a nuclear physics journal. I myself at the time had almost given up the CC method as not tractable and, of course, I never looked into the quantum chemistry journals. The result was that I learnt about Jiří's work as late as in the early seventies, when he sent me a big parcel with reprints of the many papers he and Joe Paldus had written until then.

Josef Paldus also wrote his first-hand account of the origins of coupled-cluster theory, its implementation, and exploitation in electronic wave-function determination; his account is primarily about the making of coupled-cluster theory rather than about the theory itself.

## Relation to other theories

### Configuration interaction

The *Cj* excitation operators defining the CI expansion of an *N*-electron system for the wave function $|\Psi _{0}\rangle$ ,

$|\Psi _{0}\rangle =(1+C)|\Phi _{0}\rangle ,$

$C=\sum _{j=1}^{N}C_{j},$

are related to the cluster operators T , since in the limit of including up to $T_{N}$ in the cluster operator the CC theory must be equal to full CI, we obtain the following relationships

$C_{1}=T_{1},$

$C_{2}=T_{2}+{\frac {1}{2}}(T_{1})^{2},$

$C_{3}=T_{3}+T_{1}T_{2}+{\frac {1}{6}}(T_{1})^{3},$

$C_{4}=T_{4}+{\frac {1}{2}}(T_{2})^{2}+T_{1}T_{3}+{\frac {1}{2}}(T_{1})^{2}T_{2}+{\frac {1}{24}}(T_{1})^{4},$

etc. For general relationships see J. Paldus, in *Methods in Computational Molecular Physics*, Vol. 293 of *Nato Advanced Study Institute Series B: Physics*, edited by S. Wilson and G. H. F. Diercksen (Plenum, New York, 1992), pp. 99–194.

### Symmetry-adapted cluster

The symmetry-adapted cluster (SAC) approach determines the (spin- and) symmetry-adapted cluster operator

$S=\sum _{I}S_{I}$

by solving the following system of energy-dependent equations:

$\langle \Phi |(H-E_{0})e^{S}|\Phi \rangle =0,$

$\langle \Phi _{i_{1}\ldots i_{n}}^{a_{1}\ldots a_{n}}|(H-E_{0})e^{S}|\Phi \rangle =0,$

$i_{1}<\cdots <i_{n},\quad a_{1}<\cdots <a_{n},\quad n=1,\dots ,M_{s},$

where $|\Phi _{i_{1}\ldots i_{n}}^{a_{1}\ldots a_{n}}\rangle$ are the *n*-tuply excited determinants relative to $|\Phi \rangle$ (usually, in practical implementations, they are the spin- and symmetry-adapted configuration state functions), and $M_{s}$ is the highest order of excitation included in the SAC operator. If all of the nonlinear terms in $e^{S}$ are included, then the SAC equations become equivalent to the standard coupled-cluster equations of Jiří Čížek. This is due to the cancellation of the energy-dependent terms with the disconnected terms contributing to the product of $He^{S}$ , resulting in the same set of nonlinear energy-independent equations. Typically, all nonlinear terms, except ${\tfrac {1}{2}}S_{2}^{2}$ are dropped, as higher-order nonlinear terms are usually small.

## Use in nuclear physics

In nuclear physics, coupled cluster saw significantly less use than in quantum chemistry during the 1980s and 1990s. More powerful computers, as well as advances in theory (such as the inclusion of three-nucleon interactions), have spawned renewed interest in the method since then, and it has been successfully applied to neutron-rich and medium-mass nuclei. Coupled cluster is one of several ab initio methods in nuclear physics and is specifically suitable for nuclei having closed or nearly closed shells.
