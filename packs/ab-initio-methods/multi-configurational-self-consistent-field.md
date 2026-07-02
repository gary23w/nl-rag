---
title: "Multi-configurational self-consistent field"
source: https://en.wikipedia.org/wiki/Multi-configurational_self-consistent_field
domain: ab-initio-methods
license: CC-BY-SA-4.0
tags: ab initio quantum chemistry, complete active space, multi-configurational scf, variational method chemistry
fetched: 2026-07-02
---

# Multi-configurational self-consistent field

**Multi-configurational self-consistent field** (**MCSCF**) is a method in quantum chemistry used to generate qualitatively correct reference states of molecules in cases where Hartree–Fock and density functional theory are not adequate (e.g., for molecular ground states which are quasi-degenerate with low-lying excited states or in bond-breaking situations). It uses a linear combination of configuration state functions (CSF), or configuration determinants, to approximate the exact electronic wavefunction of an atom or molecule. In an MCSCF calculation, the set of coefficients of both the CSFs or determinants and the basis functions in the molecular orbitals are varied to obtain the total electronic wavefunction with the lowest possible energy. This method can be considered a combination between configuration interaction (where the molecular orbitals are not varied but the expansion of the wave function is) and Hartree–Fock (where there is only one determinant, but the molecular orbitals are varied).

MCSCF wave functions are often used as reference states for multireference configuration interaction (MRCI) or multi-reference perturbation theories like complete active space perturbation theory (CASPT2). These methods can deal with extremely complex chemical situations and, if computing power permits, may be used to reliably calculate molecular ground and excited states if all other methods fail.

## Introduction

For the simplest single bond, found in the H2 molecule, molecular orbitals can always be written in terms of two functions χ*iA* and χ*iB* (which are atomic orbitals with small corrections) located at the two nuclei *A* and *B*:

$\varphi _{i}=N_{i}(\chi _{iA}\pm \chi _{iB}),$

where *N**i* is a normalization constant. The ground-state wavefunction for H2 at the equilibrium geometry is dominated by the configuration (*φ*1)2, which means that the molecular orbital *φ*1 is nearly doubly occupied. The Hartree–Fock (HF) model *assumes* that it is doubly occupied, which leads to a total wavefunction

$\Phi _{1}=\varphi _{1}(\mathbf {r} _{1})\varphi _{1}(\mathbf {r} _{2})\Theta _{2,0},$

where $\Theta _{2,0}$ is the singlet (*S* = 0) spin function for two electrons. The molecular orbitals in this case *φ*1 are taken as sums of 1s atomic orbitals on both atoms, namely *N*1(1sA + 1sB). Expanding the above equation into atomic orbitals yields

$\Phi _{1}=N_{1}^{2}\left[1s_{A}(\mathbf {r} _{1})1s_{A}(\mathbf {r} _{2})+1s_{A}(\mathbf {r} _{1})1s_{B}(\mathbf {r} _{2})+1s_{B}(\mathbf {r} _{1})1s_{A}(\mathbf {r} _{2})+1s_{B}(\mathbf {r} _{1})1s_{B}(\mathbf {r} _{2})\right]\Theta _{2,0}.$

This Hartree–Fock model gives a reasonable description of H2 around the equilibrium geometry – about 0.735 Å for the bond length (compared to a 0.746 Å experimental value) and 350 kJ/mol (84 kcal/mol) for the bond energy (experimentally, 432 kJ/mol (103 kcal/mol)). This is typical for the HF model, which usually describes closed-shell systems around their equilibrium geometry quite well. At large separations, however, the terms describing both electrons located at one atom remain, which corresponds to dissociation to H+ + H−, which has a much larger energy than H· + H· (two hydrogen radicals). Therefore, the persisting presence of ionic terms leads to an unphysical solution in this case.

Consequently, the HF model cannot be used to describe dissociation processes with open-shell products. The most straightforward solution to this problem is introducing coefficients in front of the different terms in Ψ1:

$\Psi _{1}=C_{\text{ion}}\Phi _{\text{ion}}+C_{\text{cov}}\Phi _{\text{cov}},$

which forms the basis for the valence bond description of chemical bonds. With the coefficients *C*ion and *C*cov varying, the wave function will have the correct form, with *C*ion = 0 for the separated limit, and *C*ion comparable to *C*cov at equilibrium. Such a description, however, uses non-orthogonal basis functions, which complicates its mathematical structure. Instead, multiconfiguration is achieved by using orthogonal molecular orbitals. After introducing an anti-bonding orbital

$\varphi _{2}=N_{2}(1s_{A}-1s_{B}),$

the total wave function of H2 can be written as a linear combination of configurations built from bonding and anti-bonding orbitals:

$\Psi _{\text{MC}}=C_{1}\Phi _{1}+C_{2}\Phi _{2},$

where Φ2 is the electronic configuration (φ2)2. In this multiconfigurational description of the H2 chemical bond, *C*1 = 1 and *C*2 = 0 close to equilibrium, and *C*1 will be comparable to *C*2 for large separations.

## Complete active space SCF

A particularly important MCSCF approach is the **complete active space SCF method** (**CASSCF**), where the linear combination of CSFs includes all that arise from a particular number of electrons in a particular number of orbitals (also known as **full-optimized reaction space** (**FORS-MCSCF**)). For example, one might define CASSCF(11,8) for NO, where the 11 valence electrons are distributed between all configurations that can be constructed from 8 molecular orbitals.

## Restricted active space SCF

Since the number of CSFs quickly increases with the number of active orbitals, along with the computational cost, it may be desirable to use a smaller set of CSFs. One way to make this selection is to restrict the number of electrons in certain subspaces, done in the **restricted active space SCF method** (**RASSCF**). One could, for instance, allow only single and double excitations from some strongly occupied subset of active orbitals, or restrict the number of electrons to at most 2 in another subset of active orbitals.
