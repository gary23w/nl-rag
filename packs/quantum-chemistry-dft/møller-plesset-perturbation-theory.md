---
title: "Møller–Plesset perturbation theory"
source: https://en.wikipedia.org/wiki/M%C3%B8ller%E2%80%93Plesset_perturbation_theory
domain: quantum-chemistry-dft
license: CC-BY-SA-4.0
tags: quantum chemistry, electronic structure, coupled cluster, configuration interaction
fetched: 2026-07-02
---

# Møller–Plesset perturbation theory

**Møller–Plesset perturbation theory** (**MP**) is one of several quantum chemistry post-Hartree–Fock ab initio methods in the field of computational chemistry. It improves on the Hartree–Fock method by adding electron correlation effects by means of Rayleigh–Schrödinger perturbation theory (RS-PT), usually to second (MP2), third (MP3) or fourth (MP4) order. Its main idea was published as early as 1934 by Christian Møller and Milton S. Plesset.

## Rayleigh–Schrödinger perturbation theory

The MP perturbation theory is a special case of RS perturbation theory. In RS theory one considers an unperturbed Hamiltonian operator ${\hat {H}}_{0}$ , to which a small (often external) perturbation ${\hat {V}}$ is added:

${\hat {H}}={\hat {H}}_{0}+\lambda {\hat {V}}.$

Here, *λ* is an arbitrary real parameter that controls the size of the perturbation. In MP theory the zeroth-order wave function is an exact eigenfunction of the Fock operator, which thus serves as the unperturbed operator. The perturbation is the correlation potential. In RS-PT the perturbed wave function and perturbed energy are expressed as a power series in λ:

$\Psi =\lim _{m\to \infty }\sum _{i=0}^{m}\lambda ^{i}\Psi ^{(i)},$

$E=\lim _{m\to \infty }\sum _{i=0}^{m}\lambda ^{i}E^{(i)}.$

Substitution of these series into the time-independent Schrödinger equation gives a new equation as $m\to \infty$ :

$\left({\hat {H}}_{0}+\lambda V\right)\left(\sum _{i=0}^{m}\lambda ^{i}\Psi ^{(i)}\right)=\left(\sum _{i=0}^{m}\lambda ^{i}E^{(i)}\right)\left(\sum _{i=0}^{m}\lambda ^{i}\Psi ^{(i)}\right).$

Equating the factors of $\lambda ^{k}$ in this equation gives a *k*th-order perturbation equation, where *k* = 0, 1, 2, ..., *m*. See perturbation theory for more details.

## Møller–Plesset perturbation

### Original formulation

The MP-energy corrections are obtained from Rayleigh–Schrödinger (RS) perturbation theory with the unperturbed Hamiltonian defined as the *shifted* Fock operator,

${\hat {H}}_{0}\equiv {\hat {F}}+\langle \Phi _{0}|({\hat {H}}-{\hat {F}})|\Phi _{0}\rangle$

and the perturbation defined as the *correlation potential*,

${\hat {V}}\equiv {\hat {H}}-{\hat {H}}_{0}={\hat {H}}-\left({\hat {F}}+\langle \Phi _{0}|({\hat {H}}-{\hat {F}})|\Phi _{0}\rangle \right),$

where the normalized Slater determinant Φ0 is the lowest eigenstate of the Fock operator:

${\hat {F}}\Phi _{0}\equiv \sum _{k=1}^{N}{\hat {f}}(k)\Phi _{0}=2\sum _{i=1}^{N/2}\varepsilon _{i}\Phi _{0}.$

Here *N* is the number of electrons in the molecule under consideration (a factor of 2 in the energy arises from the fact that each orbital is occupied by a pair of electrons with opposite spin), ${\hat {H}}$ is the usual electronic Hamiltonian, ${\hat {f}}(k)$ is the one-electron Fock operator, and *ε**i* is the orbital energy belonging to the doubly occupied spatial orbital *φ**i*.

Since the Slater determinant Φ0 is an eigenstate of ${\hat {F}}$ , it follows readily that

${\hat {F}}\Phi _{0}-\langle \Phi _{0}|{\hat {F}}|\Phi _{0}\rangle \Phi _{0}=0\implies {\hat {H}}_{0}\Phi _{0}=\langle \Phi _{0}|{\hat {H}}|\Phi _{0}\rangle \Phi _{0},$

i.e. the zeroth-order energy is the expectation value of ${\hat {H}}$ with respect to Φ0, the Hartree-Fock energy. Similarly, it can be seen that *in this formulation* the MP1 energy

$E_{\text{MP1}}\equiv \langle \Phi _{0}|{\hat {V}}|\Phi _{0}\rangle =0$

.

Hence, the first meaningful correction appears at MP2 energy.

In order to obtain the MP2 formula for a closed-shell molecule, the second order RS-PT formula is written in a basis of doubly excited Slater determinants. (Singly excited Slater determinants do not contribute because of the Brillouin theorem). After application of the Slater–Condon rules for the simplification of *N*-electron matrix elements with Slater determinants in bra and ket and integrating out spin, it becomes

${\begin{aligned}E_{\text{MP2}}&=2\sum _{i,j,a,b}{\frac {\langle \varphi _{i}\varphi _{j}|{\hat {\tilde {v}}}|\varphi _{a}\varphi _{b}\rangle \langle \varphi _{a}\varphi _{b}|{\hat {\tilde {v}}}|\varphi _{i}\varphi _{j}\rangle }{\varepsilon _{i}+\varepsilon _{j}-\varepsilon _{a}-\varepsilon _{b}}}-\sum _{i,j,a,b}{\frac {\langle \varphi _{i}\varphi _{j}|{\hat {\tilde {v}}}|\varphi _{a}\varphi _{b}\rangle \langle \varphi _{a}\varphi _{b}|{\hat {\tilde {v}}}|\varphi _{j}\varphi _{i}\rangle }{\varepsilon _{i}+\varepsilon _{j}-\varepsilon _{a}-\varepsilon _{b}}}\\\end{aligned}}$

where *𝜑**i* and *𝜑**j* are canonical occupied orbitals and *𝜑**a* and *𝜑**b* are virtual (or unoccupied) orbitals. The quantities *ε**i*, *ε**j*, *ε**a*, and *ε**b* are the corresponding orbital energies. Clearly, through second-order in the correlation potential, the total electronic energy is given by the Hartree–Fock energy plus second-order MP correction: *E* ≈ *E*HF + *E*MP2. The solution of the zeroth-order MP equation (which by definition is the Hartree–Fock equation) gives the Hartree–Fock energy. The first non-vanishing perturbation correction beyond the Hartree–Fock treatment is the second-order energy.

### Alternative formulation

Equivalent expressions are obtained by a slightly different partitioning of the Hamiltonian, which results in a different division of energy terms over zeroth- and first-order contributions, while for second- and higher-order energy corrections the two partitionings give identical results. The formulation is commonly used by chemists, who are now large users of these methods. This difference is due to the fact, well known in Hartree–Fock theory, that

$\langle \Phi _{0}|({\hat {H}}-{\hat {F}})|\Phi _{0}\rangle \neq 0\qquad \Longleftrightarrow \qquad E_{\text{HF}}\neq 2\sum _{i=1}^{N/2}\varepsilon _{i}.$

(The Hartree–Fock energy is *not* equal to the sum of occupied-orbital energies). In the alternative partitioning, one defines

${\hat {H}}_{0}\equiv {\hat {F}},\qquad {\hat {V}}\equiv {\hat {H}}-{\hat {F}}.$

Clearly, in this partitioning,

$E_{\text{MP0}}=2\sum _{i=1}^{N/2}\varepsilon _{i},\qquad E_{\text{MP1}}=E_{\text{HF}}-2\sum _{i=1}^{N/2}\varepsilon _{i}.$

Obviously, with this alternative formulation, the Møller–Plesset theorem does not hold in the literal sense that *E*MP1 ≠ 0. The solution of the zeroth-order MP equation is the sum of orbital energies. The zeroth plus first-order correction yields the Hartree–Fock energy. As with the original formulation, the first non-vanishing perturbation correction beyond the Hartree–Fock treatment is the second-order energy. To reiterate, the second- and higher-order corrections are the same in both formulations.

## Methods

Second (MP2), third (MP3), and fourth (MP4) order Møller–Plesset calculations are standard levels used in calculating small systems and are implemented in many computational chemistry codes. Higher level MP calculations, generally only MP5, are possible in some codes. However, they are rarely used because of their cost.

Systematic studies of MP perturbation theory have shown that it is not necessarily a convergent theory at high orders. Convergence can be slow, rapid, oscillatory, regular, highly erratic or simply non-existent, depending on the precise chemical system or basis set. The density matrix for the first-order and higher MP2 wavefunction is of the type known as *response density*, which differs from the more usual *expectation value density*. The eigenvalues of the response density matrix (which are the occupation numbers of the MP2 natural orbitals) can therefore be greater than 2 or negative. Unphysical numbers are a sign of a divergent perturbation expansion.

Additionally, various important molecular properties calculated at MP3 and MP4 level are no better than their MP2 counterparts, even for small molecules.

For open shell molecules, MPn-theory can directly be applied only to unrestricted Hartree–Fock reference functions (since UHF states are not in general eigenvectors of the Fock operator). However, the resulting energies often suffer from severe spin contamination, leading to large errors. A possible better alternative is to use one of the MP2-like methods based on restricted open-shell Hartree–Fock (ROHF). There are many ROHF based MP2-like methods because of arbitrariness in the ROHF wavefunction(for example HCPT, ROMP, RMP (also called ROHF-MBPT2), OPT1 and OPT2, ZAPT, IOPT, etc.). Some of the ROHF based MP2-like theories suffer from spin-contamination in their perturbed density and energies beyond second-order.

These methods, Hartree–Fock, unrestricted Hartree–Fock and restricted Hartree–Fock use a single determinant wave function. Multi-configurational self-consistent field (MCSCF) methods use several determinants and can be used for the unperturbed operator, although not uniquely, so many methods, such as complete active space perturbation theory (CASPT2), and Multi-Configuration Quasi-Degenerate Perturbation Theory (MCQDPT), have been developed. MCSCF based methods are not without perturbation series divergences.

The analogue to what MP perturbation theory is in HF theory is Görling-Levy (GL) perturbation theory in Kohn-Sham (KS) density functional theory (DFT).
