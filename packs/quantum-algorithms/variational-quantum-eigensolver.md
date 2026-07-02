---
title: "Variational quantum eigensolver"
source: https://en.wikipedia.org/wiki/Variational_quantum_eigensolver
domain: quantum-algorithms
license: CC-BY-SA-4.0
tags: quantum algorithm, shor's algorithm, grover's algorithm, quantum fourier transform
fetched: 2026-07-02
---

# Variational quantum eigensolver

In quantum computing, the **variational quantum eigensolver** (**VQE**) is a quantum algorithm for quantum chemistry, quantum simulations and optimization problems. It is a hybrid algorithm that uses both classical computers and quantum computers to find the ground state of a given physical system. Given a guess or ansatz, the quantum processor calculates the expectation value of the system with respect to an observable, often the Hamiltonian, and a classical optimizer is used to improve the guess. The algorithm is based on the variational method of quantum mechanics.

It was originally proposed in 2014, with corresponding authors Alberto Peruzzo, Alán Aspuru-Guzik and Jeremy O'Brien. The algorithm has also found applications in quantum machine learning and has been further substantiated by general hybrid algorithms between quantum and classical computers. It is an example of a noisy intermediate-scale quantum (NISQ) algorithm.

## Description

### Pauli encoding

The objective of the VQE is to find a set of quantum operations that prepares the lowest energy state (or minima) of a close approximation to some target quantity or observable. While the only strict requirement for the representation of an observable is its efficiency in estimating its expectation values, it is often more straightforward if the operator has a compact or simple expression in terms of Pauli operators or tensor products of Pauli operators.

For a fermionic system, it is often most convenient to qubitize: that is to write the many-body Hamiltonian of the system using second quantization, and then use a mapping to write the creation-annihilation operators in terms of Pauli operators. Common schemes for fermions include Jordan–Wigner transformation, Bravyi–Kitaev transformation, and parity transformation.

Once the Hamiltonian ${\hat {H}}$ is written in terms of Pauli operators and irrelevant states are discarded (finite-dimensional space), it would consist of a linear combination of Pauli strings ${\hat {P}}_{i}$ consisting of tensor products of Pauli operators (for example $X\otimes I\otimes Z\otimes X$ ), such that

${\hat {H}}=\sum _{i}\alpha _{i}{\hat {P}}_{i}$

,

where $\alpha _{i}$ are numerical coefficients. Based on the coefficients, the number of Pauli strings can be reduced in order to optimize the calculation.

The VQE can be adapted to other optimization problems by adapting the Hamiltonian to be a cost function.

### Ansatz and initial trial function

The choice of ansatz state depends on the system of interest. In gate-based quantum computing, the ansatz is given by a parametrized quantum circuit, whose parameters can be updated after each run. The ansatz has to be adaptable enough to not miss the desired state. A common method to obtain a valid ansatz is given by the unitary coupled cluster (UCC) framework and its extensions.

If the ansatz is not chosen adequately the procedure may halt at suboptimal parameters that do not correspond to a minima. In this situation, the algorithm is said to have reached a 'barren plateau'.

The ansatz can be set to an initial trial function to start the algorithm. For example, for a molecular system, one can use the Hartree–Fock method to provide a starting state that is close to the real ground state.

Another variant of the ansatz circuit is the hardware efficient ansatz, which consists of sequence of 1 qubit rotational gates and 2 qubit entangling gates. The number of repetitions of 1-qubit rotational gates and 2-qubit entangling gates is called the depth of the circuit.

### Measurement

The expectation value of a given state $|\psi (\theta _{1},\cdots ,\theta _{N})\rangle$ with parameters $\{\theta _{i}\}_{i=1}^{N}$ , has an expectation value of the energy or cost function given by

$E(\theta _{1},\cdots ,\theta _{n})=\langle {\hat {H}}\rangle =\sum _{i}\alpha _{i}\langle \psi (\theta _{1},\cdots ,\theta _{N})|{\hat {P}}_{i}|\psi (\theta _{1},\cdots ,\theta _{N})\rangle$

so in order to obtain the expectation value of the energy, one can measure the expectation value of each Pauli string (number of counts for a given value over the total number of counts). This step corresponds to measuring each qubit in the axis provided by the Pauli string. For example, for the string $X\otimes Y\otimes Y$ , the first qubit is to be measured in the *x*-axis, while the last two are to be measured in the *y*-axis of the Bloch sphere. If measurement in the *z*-axis is only possible, then Clifford gates can be used to transform between axes. If two Pauli strings commute, then they can be both measured simultaneously using the same circuit and interpreting the result according to the Pauli algebra.

### Variational method and optimization

Given a parametrized ansatz for the ground state eigenstate, with parameters that can be modified, one is sure to find the parametrized state that is closest to the ground state based on the variational method of quantum mechanics. Using classical algorithms in a digital computer, the parameters of the ansatz can be optimized. For this minimization, it is necessary to find the minima of a multivariable function. Classical optimizers using gradient descent can be used for this purpose.

## Formulation

For a given Hamiltonian (H) and a state vector $|\psi \rangle$ if we can vary $|\psi \rangle$ arbitrarily then $\min _{|\psi \rangle }\langle \psi |H|\psi \rangle$ will be the ground state energy and $\operatorname {argmin} _{|\psi \rangle }\langle \psi |H|\psi \rangle$ would be a ground state (assuming no degeneracy). But the above minimization problem over all possible states $|\psi \rangle$ , where state $|\psi \rangle$ is $2^{n}$ dimensional, is impractical. Thus to restrict the search space to a more practical size (e.g. poly(n)), we need to restrict the $|\psi \rangle$ to only a subset of possible n-qubit states which is based on conventional physics, chemistry and quantum mechanics knowledge.

### Algorithm

The adjoining figure illustrates the high level steps in the VQE algorithm.

The circuit $U({\vec {\theta }})$ controls the subset of possible states that can be created, and the parameter ${\vec {\theta }}$ contains the variational parameters, ${\vec {\theta }}={\begin{pmatrix}\theta _{1}\\\theta _{2}\\\vdots \\\theta _{p}\end{pmatrix}}$ where the number of parameters chosen are enough to lend the algorithm expressive power to compute the ground state of the system, but not too big to increase the computational cost of the optimization step.

By running the circuit many times and constantly updating the parameters to find the global minima of the expectation value of the desired observable, one can approach the ground state of the given system and store it in a quantum processor as a series of quantum gate instructions.

In case of gradient descent, it's required to minimize a cost function $f({\vec {\theta }})$ where for the VQE case $f({\vec {\theta }})=\langle \psi ({\vec {\theta }})|H|\psi ({\vec {\theta }})\rangle$ . The update rule is:

${\vec {\theta }}^{({\text{new}})}={\vec {\theta }}^{({\text{old}})}-r\nabla f({\vec {\theta }}^{({\text{old}})})$

where *r* is the learning rate (step size) and

$\nabla f({\vec {\theta }}^{({\text{old}})})=\left({\frac {\partial f({\vec {\theta }}^{({\text{old}})})}{\partial \theta _{1}}},{\frac {\partial f({\vec {\theta }}^{({\text{old}})})}{\partial \theta _{2}}},\ldots \right)^{\top }$

In order to compute the gradients, the parameter shift rule is used.

#### Example

Considering a single Pauli gate example:

$U(\theta )=e^{-i{\frac {\theta }{2}}P},$

where *P* = *X,Y or Z*, then

$\nabla _{\theta }U={\frac {\partial U}{\partial \theta }}=-{\frac {i}{2}}Pe^{-i{\frac {\theta }{2}}P}=-{\frac {i}{2}}PU=-{\frac {i}{2}}UP$

As, $f(\theta )=\langle \phi |U^{\dagger }AU|\phi \rangle$ . Thus,

$\nabla _{\theta }f(\theta )={\frac {\partial }{\partial \theta }}\langle \phi |U^{\dagger }AU|\phi \rangle =\langle \phi |\left({\frac {i}{2}}P\right)U^{\dagger }AU|\phi \rangle +\langle \phi |U^{\dagger }A\left(-{\frac {i}{2}}P\right)U|\phi \rangle$

$={\frac {1}{2}}\langle \phi |U^{\dagger }(\theta +{\frac {\pi }{2}})AU(\theta +{\frac {\pi }{2}})|\phi \rangle -{\frac {1}{2}}\langle \phi |U^{\dagger }(\theta -{\frac {\pi }{2}})AU(\theta -{\frac {\pi }{2}})|\phi \rangle$

$={\frac {1}{2}}\left(f(\theta +{\frac {\pi }{2}})-f(\theta -{\frac {\pi }{2}})\right)$

The above result has interesting properties as:

1. The same circuit can be used to evaluate $f(\theta )$ and $\nabla _{\theta }f(\theta )$
2. $f(\cdot )$ needs to be evaluated 2 times to arrive at the gradient value
3. As the angle precision $\pm {\frac {\pi }{2}}$ is large, gate precision can be kept low

## Advantages and disadvantages

1. The VQE circuit does not require many gates compared with quantum phase estimation algorithm (QPE), it is more robust to errors and lends itself well to error mitigation strategies.
2. It is a heuristic method and thus does not guarantee convergence to the ground state value. The method is highly influenced by the choice of ansatz circuit and the optimization methods.
3. Number of measurements required to conclude the value of ground state is higher compared to the QPE and scales approximately with the number of terms in the Hamiltonian.
4. VQE can run on NISQ hardware.
5. VQE is highly versatile, as problems (apart from chemistry) can be expressed as Hamiltonians.

## Use

### In chemistry

As of 2022, the variational quantum eigensolver can only simulate small molecules like the helium hydride ion or the beryllium hydride molecule. Larger molecules can be simulated by taking into account symmetry considerations. In 2020, a 12-qubit simulation of a hydrogen chain (H12) was demonstrated using Google's Sycamore quantum processor.
