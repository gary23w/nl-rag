---
title: "Slater determinant"
source: https://en.wikipedia.org/wiki/Slater_determinant
domain: hartree-fock
license: CC-BY-SA-4.0
tags: hartree-fock method, self-consistent field, slater determinant, roothaan equations
fetched: 2026-07-02
---

# Slater determinant

In quantum mechanics, a **Slater determinant** is an expression that describes the wave function of a multi-fermionic system. It satisfies anti-symmetry requirements, and consequently the Pauli principle, by changing sign upon exchange of two fermions. Only a small subset of all possible many-body fermionic wave functions can be written as a single Slater determinant, but those form an important and useful subset because of their simplicity.

The Slater determinant arises from the consideration of a wave function for a collection of electrons, each with a wave function known as the spin-orbital $\chi (\mathbf {x} )$ , where $\mathbf {x}$ denotes the position and spin of a single electron. A Slater determinant containing two electrons with the same spin orbital would correspond to a wave function that is zero everywhere.

The Slater determinant is named for John C. Slater, who introduced the determinant in 1929 as a means of ensuring the antisymmetry of a many-electron wave function, although the wave function in the determinant form first appeared independently in Heisenberg's and Dirac's articles three years earlier.

## Definition

### Two-particle case

The simplest way to approximate the wave function of a many-particle system is to take the product of properly chosen orthogonal wave functions of the individual particles. For the two-particle case with coordinates $\mathbf {x} _{1}$ and $\mathbf {x} _{2}$ , we have

$\Psi (\mathbf {x} _{1},\mathbf {x} _{2})=\chi _{1}(\mathbf {x} _{1})\chi _{2}(\mathbf {x} _{2}).$

This expression is used in the Hartree method as an ansatz for the many-particle wave function and is known as a Hartree product. However, it is not satisfactory for fermions because the wave function above is not antisymmetric under exchange of any two of the fermions, as it must be according to the Pauli exclusion principle. An antisymmetric wave function can be mathematically described as follows:

$\Psi (\mathbf {x} _{1},\mathbf {x} _{2})=-\Psi (\mathbf {x} _{2},\mathbf {x} _{1}).$

This does not hold for the Hartree product, which therefore does not satisfy the Pauli principle. This problem can be overcome by taking a linear combination of both Hartree products:

${\begin{aligned}\Psi (\mathbf {x} _{1},\mathbf {x} _{2})&={\frac {1}{\sqrt {2}}}\{\chi _{1}(\mathbf {x} _{1})\chi _{2}(\mathbf {x} _{2})-\chi _{1}(\mathbf {x} _{2})\chi _{2}(\mathbf {x} _{1})\}\\&={\frac {1}{\sqrt {2}}}{\begin{vmatrix}\chi _{1}(\mathbf {x} _{1})&\chi _{2}(\mathbf {x} _{1})\\\chi _{1}(\mathbf {x} _{2})&\chi _{2}(\mathbf {x} _{2})\end{vmatrix}},\end{aligned}}$

where the coefficient is the normalization factor. This wave function is now antisymmetric and no longer distinguishes between fermions (that is, one cannot indicate an ordinal number to a specific particle, and the indices given are interchangeable). Moreover, it also goes to zero if any two spin orbitals of two fermions are the same. This is equivalent to satisfying the Pauli exclusion principle.

### Multi-particle case

The expression can be generalised to any number of fermions by writing it as a determinant. For an *N*-electron system, the Slater determinant is defined as

${\begin{aligned}\Psi (\mathbf {x} _{1},\mathbf {x} _{2},\ldots ,\mathbf {x} _{N})&={\frac {1}{\sqrt {N!}}}{\begin{vmatrix}\chi _{1}(\mathbf {x} _{1})&\chi _{2}(\mathbf {x} _{1})&\cdots &\chi _{N}(\mathbf {x} _{1})\\\chi _{1}(\mathbf {x} _{2})&\chi _{2}(\mathbf {x} _{2})&\cdots &\chi _{N}(\mathbf {x} _{2})\\\vdots &\vdots &\ddots &\vdots \\\chi _{1}(\mathbf {x} _{N})&\chi _{2}(\mathbf {x} _{N})&\cdots &\chi _{N}(\mathbf {x} _{N})\end{vmatrix}}\\&\equiv |\chi _{1},\chi _{2},\cdots ,\chi _{N}\rangle \\&\equiv |1,2,\dots ,N\rangle ,\end{aligned}}$

where the last two expressions use a shorthand for Slater determinants: The normalization constant is implied by noting the number N, and only the one-particle wavefunctions (first shorthand) or the indices for the fermion coordinates (second shorthand) are written down. All skipped labels are implied to behave in ascending sequence. The linear combination of Hartree products for the two-particle case is identical with the Slater determinant for *N* = 2. The use of Slater determinants ensures an antisymmetrized function at the outset. In the same way, the use of Slater determinants ensures conformity to the Pauli principle. Indeed, the Slater determinant vanishes if the set $\{\chi _{i}\}$ is linearly dependent. In particular, this is the case when two (or more) spin orbitals are the same. In chemistry one expresses this fact by stating that no two electrons with the same spin can occupy the same spatial orbital.

## Example: Matrix elements in a many electron problem

Many properties of the Slater determinant come to life with an example in a non-relativistic many electron problem.

- *The one particle terms of the Hamiltonian will contribute in the same manner as for the simple Hartree product, namely the energy is summed and the states are independent*
- *The multi-particle terms of the Hamiltonian will introduce exchange term to lower of the energy for the anti-symmetrized wave function*

Starting from a molecular Hamiltonian: ${\hat {H}}_{\text{tot}}=\sum _{i}{\frac {\mathbf {p} _{i}^{2}}{2m}}+\sum _{I}{\frac {\mathbf {P} _{I}^{2}}{2M_{I}}}+\sum _{i}V_{\text{nucl}}(\mathbf {r_{i}} )+{\frac {1}{2}}\sum _{i\neq j}{\frac {e^{2}}{|\mathbf {r} _{i}-\mathbf {r} _{j}|}}+{\frac {1}{2}}\sum _{I\neq J}{\frac {Z_{I}Z_{J}e^{2}}{|\mathbf {R} _{I}-\mathbf {R} _{J}|}}$ where $\mathbf {r} _{i}$ are the electrons and $\mathbf {R} _{I}$ are the nuclei and

$V_{\text{nucl}}(\mathbf {r} )=-\sum _{I}{\frac {Z_{I}e^{2}}{|\mathbf {r} -\mathbf {R} _{I}|}}$

For simplicity we freeze the nuclei at equilibrium in one position and we remain with a simplified Hamiltonian

${\hat {H}}_{e}=\sum _{i}^{N}{\hat {h}}(\mathbf {r} _{i})+{\frac {1}{2}}\sum _{i\neq j}^{N}{\frac {e^{2}}{r_{ij}}}$

where

${\hat {h}}(\mathbf {r} )={\frac {{\hat {\mathbf {p} }}^{2}}{2m}}+V_{\text{nucl}}(\mathbf {r} )$

and where we will distinguish in the Hamiltonian between the first set of terms as ${\hat {G}}_{1}$ (the "1" particle terms) and the last term ${\hat {G}}_{2}$ (the "2" particle term) which contains exchange term for a Slater determinant.

${\hat {G}}_{1}=\sum _{i}^{N}{\hat {h}}(\mathbf {r} _{i})$

${\hat {G}}_{2}={\frac {1}{2}}\sum _{i\neq j}^{N}{\frac {e^{2}}{r_{ij}}}$

The two parts will behave differently when they have to interact with a Slater determinant wave function. We start to compute the expectation values of one-particle terms

$\langle \Psi _{0}|G_{1}|\Psi _{0}\rangle ={\frac {1}{N!}}\langle \det\{\psi _{1}...\psi _{N}\}|G_{1}|\det\{\psi _{1}...\psi _{N}\}\rangle$

In the above expression, we can just select the identical permutation in the determinant in the left part, since all the other N! − 1 permutations would give the same result as the selected one. We can thus cancel N! at the denominator

$\langle \Psi _{0}|G_{1}|\Psi _{0}\rangle =\langle \psi _{1}...\psi _{N}|G_{1}|\det\{\psi _{1}...\psi _{N}\}\rangle$

Because of the orthonormality of spin-orbitals it is also evident that only the identical permutation survives in the determinant on the right part of the above matrix element

$\langle \Psi _{0}|G_{1}|\Psi _{0}\rangle =\langle \psi _{1}...\psi _{N}|G_{1}|\psi _{1}...\psi _{N}\rangle$

This result shows that the anti-symmetrization of the product does not have any effect for the one particle terms and it behaves as it would do in the case of the simple Hartree product.

And finally we remain with the trace over the one-particle Hamiltonians

$\langle \Psi _{0}|G_{1}|\Psi _{0}\rangle =\sum _{i}\langle \psi _{i}|h|\psi _{i}\rangle$

Which tells us that to the extent of the one-particle terms the wave functions of the electrons are independent of each other and the expectation value of total system is given by the sum of expectation value of the single particles.

For the two-particle terms instead

$\langle \Psi _{0}|G_{2}|\Psi _{0}\rangle ={\frac {1}{N!}}\langle \det\{\psi _{1}...\psi _{N}\}|G_{2}|\det\{\psi _{1}...\psi _{N}\}\rangle =\langle \psi _{1}...\psi _{N}|G_{2}|\det\{\psi _{1}...\psi _{N}\}\rangle$

If we focus on the action of one term of $G_{2}$ , it will produce only the two terms

$\langle \psi _{1}(r_{1},\sigma _{1})...\psi _{N}(r_{N},\sigma _{N})|{\frac {e^{2}}{r_{12}}}|\mathrm {det} \{\psi _{1}(r_{1},\sigma _{1})...\psi _{N}(r_{N},\sigma _{N})\}\rangle =\langle \psi _{1}\psi _{2}|{\frac {e^{2}}{r_{12}}}|\psi _{1}\psi _{2}\rangle -\langle \psi _{1}\psi _{2}|{\frac {e^{2}}{r_{12}}}|\psi _{2}\psi _{1}\rangle$

And finally $\langle \Psi _{0}|G_{2}|\Psi _{0}\rangle ={\frac {1}{2}}\sum _{i\neq j}\left[\langle \psi _{i}\psi _{j}|{\frac {e^{2}}{r_{ij}}}|\psi _{i}\psi _{j}\rangle -\langle \psi _{i}\psi _{j}|{\frac {e^{2}}{r_{ij}}}|\psi _{j}\psi _{i}\rangle \right]$

which instead is a mixing term. The first contribution is called the "coulomb" term or "coulomb" integral and the second is the "exchange" term or exchange integral. Sometimes different range of index in the summation is used ${\textstyle \sum _{ij}}$ since the Coulomb and exchange contributions exactly cancel each other for $i=j$ .

It is important to notice explicitly that the exchange term, which is always positive for local spin-orbitals, is absent in the simple Hartree product. Hence the electron-electron repulsive energy $\langle \Psi _{0}|G_{2}|\Psi _{0}\rangle$ on the antisymmetrized product of spin-orbitals is always lower than the electron-electron repulsive energy on the simple Hartree product of the same spin-orbitals. Since exchange bielectronic integrals are different from zero only for spin-orbitals with parallel spins, we link the decrease in energy with the physical fact that electrons with parallel spin are kept apart in real space in Slater determinant states.

## Connection with Grassmann manifolds

The space of all pure quantum states in a Hilbert space ${\mathcal {H}}$ can be identified with a projective Hilbert space, the manifold of all 1-dimensional subspaces of ${\mathcal {H}}$ , since states differing by a global phase represent the same physical state. A Slater determinant in the tensor product ${\mathcal {H}}^{\otimes N}$ is uniquely determined, up to a global phase, by the N -dimensional subspace of ${\mathcal {H}}$ spanned by the corresponding one-particle states. The space of states that can be written as a single Slater determinant in ${\mathcal {H}}$ forms a smooth manifold and projective algebraic variety which is naturally identified with the Grassmannian $\mathbf {Gr} _{N}({\mathcal {H}})$ . Its embedding into the projective many-particle Hilbert space $\mathbf {P} ({\mathcal {H}}^{\otimes N})$ is equivalent to the Plücker embedding, which corresponds exactly to taking the many-particle Slater determinant of a given set of N one-particle states. In quantum chemistry, the geometric structure of these spaces plays an important role in theoretical analysis of the Hartree-Fock method and can be used to prove theoretical results on the existence of solutions to the Hartree-Fock equations.

## As an approximation

Most fermionic wavefunctions cannot be represented as a Slater determinant. The best Slater approximation to a given fermionic wave function can be defined to be the one that maximizes the overlap between the Slater determinant and the target wave function. The maximal overlap is a geometric measure of entanglement between the fermions.

A single Slater determinant is used as an approximation to the electronic wavefunction in Hartree–Fock theory. In more accurate theories (such as configuration interaction and MCSCF), a linear combination of Slater determinants is needed.

## Discussion

The word "**detor**" was proposed by S. F. Boys to refer to a Slater determinant of orthonormal orbitals, but this term is rarely used.

Unlike fermions that are subject to the Pauli exclusion principle, two or more bosons can occupy the same single-particle quantum state. Wavefunctions describing systems of identical bosons are symmetric under the exchange of particles and can be expanded in terms of permanents.
