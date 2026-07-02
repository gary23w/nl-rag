---
title: "Quantum superposition"
source: https://en.wikipedia.org/wiki/Quantum_superposition
domain: quantum-mechanics
license: CC-BY-SA-4.0
tags: quantum mechanics, schrodinger equation, wave function, uncertainty principle
fetched: 2026-07-02
---

# Quantum superposition

**Quantum superposition** is a fundamental principle of quantum mechanics that states that linear combinations of solutions to the Schrödinger equation are also solutions of the Schrödinger equation. This follows from the fact that the Schrödinger equation is a linear differential equation in time and position. More precisely, the state of a system is given by a linear combination of all the eigenfunctions of the Schrödinger equation governing that system.

An example is a qubit used in quantum information processing. A qubit state is most generally a superposition of the basis states $|0\rangle$ and $|1\rangle$ :

$|\Psi \rangle =c_{0}|0\rangle +c_{1}|1\rangle ,$

where $|\Psi \rangle$ is the quantum state of the qubit, and $|0\rangle$ , $|1\rangle$ denote particular solutions to the Schrödinger equation in Dirac notation weighted by the two probability amplitudes $c_{0}$ and $c_{1}$ that both are complex numbers. Here $|0\rangle$ corresponds to the classical 0 bit, and $|1\rangle$ to the classical 1 bit. The probabilities of measuring the system in the $|0\rangle$ or $|1\rangle$ state are given by $|c_{0}|^{2}$ and $|c_{1}|^{2}$ respectively (see the Born rule). Before the measurement occurs the qubit is in a superposition of both states.

The interference fringes in the double-slit experiment provide another example of the superposition principle.

## Wave postulate

The theory of quantum mechanics postulates that a wave equation completely describes the state of a quantum system at all times. Furthermore, this differential equation is restricted to be linear and homogeneous. These conditions mean that for any two solutions of the wave equation, $\Psi _{1}$ and $\Psi _{2}$ , a linear combination of those solutions also solve the wave equation: $\Psi =c_{1}\Psi _{1}+c_{2}\Psi _{2}$ for arbitrary complex coefficients $c_{1}$ and $c_{2}$ . If the wave equation has more than two solutions, combinations of all such solutions are again valid solutions.

## Transformation

The quantum wave equation can be solved using functions of position, $\Psi ({\vec {r}})$ , or using functions of momentum, $\Phi ({\vec {p}})$ and consequently the superposition of momentum functions are also solutions: $\Phi ({\vec {p}})=d_{1}\Phi _{1}({\vec {p}})+d_{2}\Phi _{2}({\vec {p}})$ The position and momentum solutions are related by a linear transformation, a Fourier transformation. This transformation is itself a quantum superposition and every position wave function can be represented as a superposition of momentum wave functions and vice versa. These superpositions involve an infinite number of component waves.

## Generalization to basis states

Other transformations express a quantum solution as a superposition of eigenvectors, each corresponding to a possible result of a measurement on the quantum system. An eigenvector $\psi _{i}$ for a mathematical operator, ${\hat {A}}$ , has the equation ${\hat {A}}\psi _{i}=\lambda _{i}\psi _{i}$ where $\lambda _{i}$ is one possible measured quantum value for the observable A . A superposition of these eigenvectors can represent any solution: $\Psi =\sum _{n}a_{i}\psi _{i}.$ The states like $\psi _{i}$ are called basis states.

## Compact notation for superpositions

Important mathematical operations on quantum system solutions can be performed using only the coefficients of the superposition, suppressing the details of the superposed functions. This leads to quantum systems expressed in the Dirac bra-ket notation: $|v\rangle =d_{1}|1\rangle +d_{2}|2\rangle$ This approach is especially effective for systems like quantum spin with no classical coordinate analog. Such shorthand notation is very common in textbooks and papers on quantum mechanics, and superposition of basis states is a fundamental tool in quantum mechanics.

## Consequences

Paul Dirac described the superposition principle as follows:

> The non-classical nature of the superposition process is brought out clearly if we consider the superposition of two states, *A* and *B*, such that there exists an observation which, when made on the system in state *A*, is certain to lead to one particular result, *a* say, and when made on the system in state *B* is certain to lead to some different result, *b* say. What will be the result of the observation when made on the system in the superposed state? The answer is that the result will be sometimes *a* and sometimes *b*, according to a probability law depending on the relative weights of *A* and *B* in the superposition process. It will never be different from both *a* and *b* [i.e., either *a* or *b*]. *The intermediate character of the state formed by superposition thus expresses itself through the probability of a particular result for an observation being intermediate between the corresponding probabilities for the original states, not through the result itself being intermediate between the corresponding results for the original states.*

Anton Zeilinger, referring to the prototypical example of the double-slit experiment, has elaborated regarding the creation and destruction of quantum superposition:

> "[T]he superposition of amplitudes ... is only valid if there is no way to know, even in principle, which path the particle took. It is important to realize that this does not imply that an observer actually takes note of what happens. It is sufficient to destroy the interference pattern, if the path information is accessible in principle from the experiment or even if it is dispersed in the environment and beyond any technical possibility to be recovered, but in principle still ‘‘out there.’’ The absence of any such information is *the essential criterion* for quantum interference to appear.

## Theory

### General formalism

Any quantum state can be expanded as a sum or superposition of the eigenstates of an Hermitian operator, like the Hamiltonian, because the eigenstates form a complete basis:

$|\alpha \rangle =\sum _{n}c_{n}|n\rangle ,$

where $|n\rangle$ are the energy eigenstates of the Hamiltonian. For continuous variables like position eigenstates, $|x\rangle$ :

$|\alpha \rangle =\int dx'|x'\rangle \langle x'|\alpha \rangle ,$

where $\phi _{\alpha }(x)=\langle x|\alpha \rangle$ is the projection of the state into the $|x\rangle$ basis and is called the wave function of the particle. In both instances we notice that $|\alpha \rangle$ can be expanded as a superposition of an infinite number of basis states.

### Example

Given the Schrödinger equation

${\hat {H}}|n\rangle =E_{n}|n\rangle ,$

where $|n\rangle$ indexes the set of eigenstates of the Hamiltonian with energy eigenvalues $E_{n},$ we see immediately that

${\hat {H}}{\big (}|n\rangle +|n'\rangle {\big )}=E_{n}|n\rangle +E_{n'}|n'\rangle ,$

where

$|\Psi \rangle =|n\rangle +|n'\rangle$

is a solution of the Schrödinger equation but is not generally an eigenstate because $E_{n}$ and $E_{n'}$ are not generally equal. We say that $|\Psi \rangle$ is made up of a superposition of energy eigenstates. Now consider the more concrete case of an electron that has either spin up or down. We now index the eigenstates with the spinors in the ${\hat {z}}$ basis:

$|\Psi \rangle =c_{1}|{\uparrow }\rangle +c_{2}|{\downarrow }\rangle ,$

where $|{\uparrow }\rangle$ and $|{\downarrow }\rangle$ denote spin-up and spin-down states respectively. As previously discussed, the magnitudes of the complex coefficients give the probability of finding the electron in either definite spin state:

$P{\big (}|{\uparrow }\rangle {\big )}=|c_{1}|^{2},$

$P{\big (}|{\downarrow }\rangle {\big )}=|c_{2}|^{2},$

$P_{\text{total}}=P{\big (}|{\uparrow }\rangle {\big )}+P{\big (}|{\downarrow }\rangle {\big )}=|c_{1}|^{2}+|c_{2}|^{2}=1,$

where the probability of finding the particle with either spin up or down is normalized to 1. Notice that $c_{1}$ and $c_{2}$ are complex numbers, so that

$|\Psi \rangle ={\frac {3}{5}}i|{\uparrow }\rangle +{\frac {4}{5}}|{\downarrow }\rangle .$

is an example of an allowed state. We now get

$P{\big (}|{\uparrow }\rangle {\big )}=\left|{\frac {3i}{5}}\right|^{2}={\frac {9}{25}},$

$P{\big (}|{\downarrow }\rangle {\big )}=\left|{\frac {4}{5}}\right|^{2}={\frac {16}{25}},$

$P_{\text{total}}=P{\big (}|{\uparrow }\rangle {\big )}+P{\big (}|{\downarrow }\rangle {\big )}={\frac {9}{25}}+{\frac {16}{25}}=1.$

If we consider a qubit with both position and spin, the state is a superposition of all possibilities for both:

$\Psi =\psi _{+}(x)\otimes |{\uparrow }\rangle +\psi _{-}(x)\otimes |{\downarrow }\rangle ,$

where we have a general state $\Psi$ is the sum of the tensor products of the position space wave functions and spinors.

## Experiments

Successful experiments involving superpositions of relatively large (by the standards of quantum physics) objects have been performed.

- A beryllium ion has been trapped in a superposed state.
- A double slit experiment has been performed with molecules as large as buckyballs and functionalized oligoporphyrins with up to 2000 atoms.
- Molecules with masses exceeding 10,000 and composed of over 810 atoms have successfully been superposed, and metal clusters with masses over 170,000 Da and containing more than 7,000 atoms have also been demonstrated in quantum superposition.
- Very sensitive magnetometers have been realized using superconducting quantum interference devices (SQUIDS) that operate using quantum interference effects in superconducting circuits.

- A piezoelectric "tuning fork" has been constructed, which can be placed into a superposition of vibrating and non-vibrating states. The resonator comprises about 10 trillion atoms.
- Recent research indicates that chlorophyll within plants appears to exploit the feature of quantum superposition to achieve greater efficiency in transporting energy, allowing pigment proteins to be spaced further apart than would otherwise be possible.

## In quantum computers

In quantum computers, a qubit is the analog of the classical information bit, but rather than having one of two distinct values, qubits are a superposition of two values. Controlling this superposition qubits is a central challenge in quantum computation. The superposition needs to be robust to unintended interactions and yet interactions are needed for computing with qubits. Qubit systems like nuclear spins with small coupling strength are robust to outside disturbances but the same small coupling makes it difficult to readout results.
