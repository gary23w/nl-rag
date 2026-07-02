---
title: "Variational method (quantum mechanics)"
source: https://en.wikipedia.org/wiki/Variational_method_(quantum_mechanics)
domain: ab-initio-methods
license: CC-BY-SA-4.0
tags: ab initio quantum chemistry, complete active space, multi-configurational scf, variational method chemistry
fetched: 2026-07-02
---

# Variational method (quantum mechanics)

In quantum mechanics, the **variational method** is one way of finding approximations to the lowest energy eigenstate or ground state, and some excited states. This allows calculating approximate wavefunctions such as molecular orbitals. The basis for this method is the variational principle.

The method consists of choosing a "trial wavefunction" depending on one or more parameters, and finding the values of these parameters for which the expectation value of the energy is the lowest possible. The wavefunction obtained by fixing the parameters to such values is then an approximation to the ground state wavefunction, and the expectation value of the energy in that state is an upper bound to the ground state energy. The Hartree–Fock method, density matrix renormalization group, and Ritz method apply the variational method.

## Description

Suppose we are given a Hilbert space and a Hermitian operator over it called the Hamiltonian H . Ignoring complications about continuous spectra, we consider the discrete spectrum of H and a basis of eigenvectors $\{|\psi _{\lambda }\rangle \}$ (see spectral theorem for Hermitian operators for the mathematical background): $\left\langle \psi _{\lambda _{1}}|\psi _{\lambda _{2}}\right\rangle =\delta _{\lambda _{1}\lambda _{2}},$ where $\delta _{ij}$ is the Kronecker delta $\delta _{ij}={\begin{cases}0&{\text{if }}i\neq j,\\1&{\text{if }}i=j,\end{cases}}$ and the $\{|\psi _{\lambda }\rangle \}$ satisfy the eigenvalue equation $H\left|\psi _{\lambda }\right\rangle =\lambda \left|\psi _{\lambda }\right\rangle .$

Once again ignoring complications involved with a continuous spectrum of H , suppose the spectrum of H is bounded from below and that its greatest lower bound is *E*0. The expectation value of H in a state $|\psi \rangle$ is then ${\begin{aligned}\left\langle \psi \right|H\left|\psi \right\rangle &=\sum _{\lambda _{1},\lambda _{2}\in \mathrm {Spec} (H)}\left\langle \psi |\psi _{\lambda _{1}}\right\rangle \left\langle \psi _{\lambda _{1}}\right|H\left|\psi _{\lambda _{2}}\right\rangle \left\langle \psi _{\lambda _{2}}|\psi \right\rangle \\&=\sum _{\lambda \in \mathrm {Spec} (H)}\lambda \left|\left\langle \psi _{\lambda }|\psi \right\rangle \right|^{2}\geq \sum _{\lambda \in \mathrm {Spec} (H)}E_{0}\left|\left\langle \psi _{\lambda }|\psi \right\rangle \right|^{2}=E_{0}\langle \psi |\psi \rangle .\end{aligned}}$

If we were to vary over all possible states with norm 1 trying to minimize the expectation value of H , the lowest value would be $E_{0}$ and the corresponding state would be the ground state, as well as an eigenstate of H . Varying over the entire Hilbert space is usually too complicated for physical calculations, and a subspace of the entire Hilbert space is chosen, parametrized by some (real) differentiable parameters $\alpha _{i}$ (*i* = 1, 2, ..., *N*). The choice of the subspace is called the ansatz. Some choices of ansatzes lead to better approximations than others, therefore the choice of ansatz is important.

Let's assume there is some overlap between the ansatz and the ground state (otherwise, it's a bad ansatz). We wish to normalize the ansatz, so we have the constraints $\left\langle \psi (\mathbf {\alpha } )|\psi (\mathbf {\alpha } )\right\rangle =1$ and we wish to minimize $\varepsilon (\mathbf {\alpha } )=\left\langle \psi (\mathbf {\alpha } )\right|H\left|\psi (\mathbf {\alpha } )\right\rangle .$

This, in general, is not an easy task, since we are looking for a global minimum and finding the zeroes of the partial derivatives of $\varepsilon$ over all $\alpha _{i}$ is not sufficient. If $\psi (\alpha )$ is expressed as a linear combination of other functions ( $\alpha _{i}$ being the coefficients), as in the Ritz method, there is only one minimum and the problem is straightforward. There are other, non-linear methods, however, such as the Hartree–Fock method, that are also not characterized by a multitude of minima and are therefore comfortable in calculations.

Although usually limited to calculations of the ground state energy, this method can be applied in certain cases to calculations of excited states as well. If the ground state wavefunction is known, either by the method of variation or by direct calculation, a subset of the Hilbert space can be chosen which is orthogonal to the ground state wavefunction.

$\left|\psi \right\rangle =\left|\psi _{\text{test}}\right\rangle -\left\langle \psi _{\mathrm {gr} }|\psi _{\text{test}}\right\rangle \left|\psi _{\text{gr}}\right\rangle$

The resulting minimum is usually not as accurate as for the ground state, as any difference between the true ground state and $\psi _{\text{gr}}$ results in a lower excited energy. This defect is worsened with each higher excited state.

In another formulation: $E_{\text{ground}}\leq \left\langle \phi \right|H\left|\phi \right\rangle .$

This holds for any trial $\phi$ since, by definition, the ground state wavefunction has the lowest energy, and any trial wavefunction will have energy greater than or equal to it.

Proof: $\phi$ can be expanded as a linear combination of the actual eigenfunctions of the Hamiltonian (which we assume to be normalized and orthogonal): $\phi =\sum _{n}c_{n}\psi _{n}.$

Then, to find the expectation value of the Hamiltonian: ${\begin{aligned}\left\langle H\right\rangle =\left\langle \phi \right|H\left|\phi \right\rangle ={}&\left\langle \sum _{n}c_{n}\psi _{n}\right|H\left|\sum _{m}c_{m}\psi _{m}\right\rangle \\={}&\sum _{n}\sum _{m}\left\langle c_{n}^{*}\psi _{n}\right|E_{m}\left|c_{m}\psi _{m}\right\rangle \\={}&\sum _{n}\sum _{m}c_{n}^{*}c_{m}E_{m}\left\langle \psi _{n}|\psi _{m}\right\rangle \\={}&\sum _{n}|c_{n}|^{2}E_{n}.\end{aligned}}$

Now, the ground state energy is the lowest energy possible, i.e., $E_{n}\geq E_{\text{ground}}$ . Therefore, if the guessed wave function $\phi$ is normalized: $\left\langle \phi \right|H\left|\phi \right\rangle \geq E_{\text{ground}}\sum _{n}|c_{n}|^{2}=E_{\text{ground}}.$

### In general

For a Hamiltonian H that describes the studied system and *any* normalizable function $\Psi$ with arguments appropriate for the unknown wave function of the system, we define the functional $\varepsilon \left[\Psi \right]={\frac {\left\langle \Psi \right|{\hat {H}}\left|\Psi \right\rangle }{\left\langle \Psi |\Psi \right\rangle }}.$

The variational principle states that

- $\varepsilon \geq E_{0}$ , where $E_{0}$ is the lowest energy eigenstate (ground state) of the Hamiltonian
- $\varepsilon =E_{0}$ if and only if $\Psi$ is exactly equal to the wave function of the ground state of the studied system.

The variational principle formulated above is the basis of the variational method used in quantum mechanics and quantum chemistry to find approximations to the ground state.

Another facet in variational principles in quantum mechanics is that since $\Psi$ and $\Psi ^{\dagger }$ can be varied separately (a fact arising due to the complex nature of the wave function), the quantities can be varied in principle just one at a time.

## Helium atom ground state

The helium atom consists of two electrons with mass *m* and electric charge −*e*, around an essentially fixed nucleus of mass *M* ≫ *m* and charge +2*e*. The Hamiltonian for it, neglecting the fine structure, is: $H=-{\frac {\hbar ^{2}}{2m}}\left(\nabla _{1}^{2}+\nabla _{2}^{2}\right)-{\frac {e^{2}}{4\pi \varepsilon _{0}}}\left({\frac {2}{r_{1}}}+{\frac {2}{r_{2}}}-{\frac {1}{|\mathbf {r} _{1}-\mathbf {r} _{2}|}}\right)$ where *ħ* is the reduced Planck constant, *ε*0 is the vacuum permittivity, *ri* (for *i* = 1, 2) is the distance of the i-th electron from the nucleus, and |**r**1 − **r**2| is the distance between the two electrons.

If the term *Vee* = *e*2/(4*πε*0|**r**1 − **r**2|), representing the repulsion between the two electrons, were excluded, the Hamiltonian would become the sum of two hydrogen-like atom Hamiltonians with nuclear charge +2*e*. The ground state energy would then be 8*E*1 = −109 eV, where *E*1 is the Rydberg constant, and its ground state wavefunction would be the product of two wavefunctions for the ground state of hydrogen-like atoms: $\psi (\mathbf {r} _{1},\mathbf {r} _{2})={\frac {Z^{3}}{\pi a_{0}^{3}}}e^{-Z\left(r_{1}+r_{2}\right)/a_{0}}.$ where *a*0 is the Bohr radius and *Z* = 2, helium's nuclear charge. The expectation value of the total Hamiltonian *H* (including the term *Vee*) in the state described by *ψ*0 will be an upper bound for its ground state energy. ⟨*Vee*⟩ is −5*E*1/2 = 34 eV, so ⟨*H*⟩ is 8*E*1 − 5*E*1/2 = −75 eV.

A tighter upper bound can be found by using a better trial wavefunction with 'tunable' parameters. Each electron can be thought to see the nuclear charge partially "shielded" by the other electron, so we can use a trial wavefunction equal with an "effective" nuclear charge *Z* < 2: The expectation value of H in this state is: $\left\langle H\right\rangle =\left[-2Z^{2}+{\frac {27}{4}}Z\right]E_{1}$

This is minimal for *Z* = 27/16 implying shielding reduces the effective charge to ~1.69. Substituting this value of Z into the expression for H yields 729*E*1/128 = −77.5 eV, within 2% of the experimental value, −78.975 eV.

Even closer estimations of this energy have been found using more complicated trial wave functions with more parameters. This is done in physical chemistry via variational Monte Carlo.
