---
title: "Density matrix"
source: https://en.wikipedia.org/wiki/Density_matrix
domain: ab-initio-methods
license: CC-BY-SA-4.0
tags: ab initio quantum chemistry, complete active space, multi-configurational scf, variational method chemistry
fetched: 2026-07-02
---

# Density matrix

In quantum mechanics, a **density matrix** (or **density operator**) is a matrix used in calculating the probabilities of the outcomes of measurements performed on physical systems. It is a generalization of the state vectors or wavefunctions: while those can only represent pure states, density matrices can also represent mixed ensembles of states. These arise in quantum mechanics in two different situations:

1. when the preparation of a system can randomly produce different pure states, and thus one must deal with the statistics of the ensemble of possible preparations; and
2. when one wants to describe a physical system that is entangled with another, without describing their combined state. This case is typical for a system interacting with some environment (e.g. decoherence). In this case, the density matrix of an entangled system differs from that of an ensemble of pure states that, combined, would give the same statistical results upon measurement.

Density matrices are thus crucial tools in areas of quantum mechanics that deal with mixed states (not to be confused with superposed states), such as quantum statistical mechanics, open quantum systems and quantum information.

## Definition and motivation

The density matrix is a representation of a linear operator called the **density operator**. The density matrix is obtained from the density operator by a choice of an orthonormal basis in the underlying space. In practice, the terms *density matrix* and *density operator* are often used interchangeably.

Pick a basis with states $|0\rangle$ , $|1\rangle$ in a two-dimensional Hilbert space, then the density operator is represented by the matrix $(\rho _{ij})=\left({\begin{matrix}\rho _{00}&\rho _{01}\\\rho _{10}&\rho _{11}\end{matrix}}\right)=\left({\begin{matrix}p_{0}&\rho _{01}\\\rho _{01}^{*}&p_{1}\end{matrix}}\right)$ where the diagonal elements are real numbers that sum to one (also called populations of the two states $|0\rangle$ , $|1\rangle$ ). The off-diagonal elements are complex conjugates of each other (also called coherences); they are restricted in magnitude by the requirement that $(\rho _{ij})$ be a positive semi-definite operator, see below.

A density operator is a positive semi-definite, self-adjoint operator of trace one acting on the Hilbert space of the system. This definition can be motivated by considering a situation where some pure states $|\psi _{j}\rangle$ (which are not necessarily orthogonal) are prepared with probability $p_{j}$ each. This is known as an *ensemble* of pure states. The probability of obtaining projective measurement result m when using projectors $\Pi _{m}$ is given by $p(m)=\sum _{j}p_{j}\left\langle \psi _{j}\right|\Pi _{m}\left|\psi _{j}\right\rangle ,$ which can be proven equal to $p(m)=\operatorname {tr} \left[\Pi _{m}\left(\sum _{j}p_{j}\left|\psi _{j}\right\rangle \left\langle \psi _{j}\right|\right)\right].$ Consequently, the **density operator**, defined as $\rho =\sum _{j}p_{j}\left|\psi _{j}\right\rangle \left\langle \psi _{j}\right|,$ is a convenient representation for the state of this ensemble. This operator is positive semi-definite, self-adjoint, and has trace one. Conversely, it follows from the spectral theorem that every operator with these properties can be written as ${\textstyle \sum _{j}p_{j}\left|\psi _{j}\right\rangle \left\langle \psi _{j}\right|}$ for some states $\left|\psi _{j}\right\rangle$ and coefficients $p_{j}$ that are non-negative and add up to one. However, this representation will not be unique, as shown by the Schrödinger–HJW theorem.

Another motivation for the definition of density operators comes from considering local measurements on entangled states. Let $|\Psi \rangle$ be a pure entangled state in the composite Hilbert space ${\mathcal {H}}_{1}\otimes {\mathcal {H}}_{2}$ . The probability of obtaining measurement result m when measuring projectors $\Pi _{m}$ on the Hilbert space ${\mathcal {H}}_{1}$ alone is given by $p(m)=\left\langle \Psi \right|\left(\Pi _{m}\otimes I\right)\left|\Psi \right\rangle ,$ which after algebraic manipulation becomes $p(m)=\operatorname {tr} \left[\Pi _{m}\left(\operatorname {tr} _{2}\left|\Psi \right\rangle \left\langle \Psi \right|\right)\right],$ where $\operatorname {tr} _{2}$ denotes the partial trace over the Hilbert space ${\mathcal {H}}_{2}$ . This makes the operator $\rho =\operatorname {tr} _{2}\left|\Psi \right\rangle \left\langle \Psi \right|$ a convenient tool to calculate the probabilities of these local measurements. This operator has all the properties of a density operator and is known as the reduced density matrix of $|\Psi \rangle$ on subsystem 1. Conversely, the Schrödinger–HJW theorem implies that all density operators can be written as $\operatorname {tr} _{2}\left|\Psi \right\rangle \left\langle \Psi \right|$ for some state $\left|\Psi \right\rangle$ .

## Pure and mixed states

A pure quantum state is a state that can not be written as a probabilistic mixture, or convex combination, of other quantum states. There are several equivalent characterizations of pure states in the language of density operators. A density operator represents a pure state if and only if:

- it can be written as an outer product of a state vector $|\psi \rangle$ with itself, that is, $\rho =|\psi \rangle \langle \psi |.$
- it is a projection, in particular of rank one.
- it is idempotent, that is $\rho =\rho ^{2}.$
- it has purity one, that is, $\operatorname {tr} (\rho ^{2})=1.$

It is important to emphasize the difference between a probabilistic mixture (i.e. an ensemble) of quantum states and the superposition of two states. If an ensemble is prepared to have half of its systems in state $|\psi _{1}\rangle$ and the other half in $|\psi _{2}\rangle$ , it can be described by the density matrix:

$\rho ={\frac {1}{2}}{\begin{pmatrix}1&0\\0&1\end{pmatrix}},$

where $|\psi _{1}\rangle$ and $|\psi _{2}\rangle$ are assumed orthogonal and of dimension 2, for simplicity. On the other hand, a **quantum superposition** of these two states with equal probability amplitudes results in the pure state $|\psi \rangle =(|\psi _{1}\rangle +|\psi _{2}\rangle )/{\sqrt {2}},$ with density matrix

$|\psi \rangle \langle \psi |={\frac {1}{2}}{\begin{pmatrix}1&1\\1&1\end{pmatrix}}.$

Unlike the probabilistic mixture, this superposition can display quantum interference.

Geometrically, the set of density operators is a convex set, and the pure states are the extremal points of that set. The simplest case is that of a two-dimensional Hilbert space, known as a qubit. An arbitrary mixed state for a qubit can be written as a linear combination of the Pauli matrices, which together with the identity matrix provide a basis for $2\times 2$ self-adjoint matrices:

$\rho ={\frac {1}{2}}\left(I+r_{x}\sigma _{x}+r_{y}\sigma _{y}+r_{z}\sigma _{z}\right),$

where the real numbers $(r_{x},r_{y},r_{z})$ are the coordinates of a point within the unit ball and

$\sigma _{x}={\begin{pmatrix}0&1\\1&0\end{pmatrix}},\quad \sigma _{y}={\begin{pmatrix}0&-i\\i&0\end{pmatrix}},\quad \sigma _{z}={\begin{pmatrix}1&0\\0&-1\end{pmatrix}}.$

Points with $r_{x}^{2}+r_{y}^{2}+r_{z}^{2}=1$ represent pure states, while mixed states are represented by points in the interior. This is known as the Bloch sphere picture of qubit state space.

### Example: light polarization

An example of pure and mixed states is light polarization. An individual photon can be described as having right or left circular polarization, described by the orthogonal quantum states $|\mathrm {R} \rangle$ and $|\mathrm {L} \rangle$ or a superposition of the two: it can be in any state $\alpha |\mathrm {R} \rangle +\beta |\mathrm {L} \rangle$ (with $|\alpha |^{2}+|\beta |^{2}=1$ ), corresponding to linear, circular, or elliptical polarization. Consider now a vertically polarized photon, described by the state $|\mathrm {V} \rangle =(|\mathrm {R} \rangle +|\mathrm {L} \rangle )/{\sqrt {2}}$ . If we pass it through a circular polarizer that allows either only $|\mathrm {R} \rangle$ polarized light, or only $|\mathrm {L} \rangle$ polarized light, half of the photons are absorbed in both cases. This may make it *seem* like half of the photons are in state $|\mathrm {R} \rangle$ and the other half in state $|\mathrm {L} \rangle$ , but this is not correct: if we pass $(|\mathrm {R} \rangle +|\mathrm {L} \rangle )/{\sqrt {2}}$ through a linear polarizer there is no absorption whatsoever, but if we pass either state $|\mathrm {R} \rangle$ or $|\mathrm {L} \rangle$ half of the photons are absorbed.

Unpolarized light (such as the light from an incandescent light bulb) cannot be described as *any* state of the form $\alpha |\mathrm {R} \rangle +\beta |\mathrm {L} \rangle$ (linear, circular, or elliptical polarization). Unlike polarized light, it passes through a polarizer with 50% intensity loss whatever the orientation of the polarizer; and it cannot be made polarized by passing it through any wave plate. However, unpolarized light *can* be described as a statistical ensemble, e. g. as each photon having either $|\mathrm {R} \rangle$ polarization or $|\mathrm {L} \rangle$ polarization with probability 1/2. The same behavior would occur if each photon had either vertical polarization $|\mathrm {V} \rangle$ or horizontal polarization $|\mathrm {H} \rangle$ with probability 1/2. These two ensembles are completely indistinguishable experimentally, and therefore they are considered the same mixed state. For this example of unpolarized light, the density operator equals

$\rho ={\frac {1}{2}}|\mathrm {R} \rangle \langle \mathrm {R} |+{\frac {1}{2}}|\mathrm {L} \rangle \langle \mathrm {L} |={\frac {1}{2}}|\mathrm {H} \rangle \langle \mathrm {H} |+{\frac {1}{2}}|\mathrm {V} \rangle \langle \mathrm {V} |={\frac {1}{2}}{\begin{pmatrix}1&0\\0&1\end{pmatrix}}.$

There are also other ways to generate unpolarized light: one possibility is to introduce uncertainty in the preparation of the photon, for example, passing it through a birefringent crystal with a rough surface, so that slightly different parts of the light beam acquire different polarizations. Another possibility is using entangled states: a radioactive decay can emit two photons traveling in opposite directions, in the quantum state $(|\mathrm {R} ,\mathrm {L} \rangle +|\mathrm {L} ,\mathrm {R} \rangle )/{\sqrt {2}}$ . The joint state of the two photons *together* is pure, but the density matrix for each photon individually, found by taking the partial trace of the joint density matrix, is completely mixed.

## Equivalent ensembles and purifications

A given density operator does not uniquely determine which ensemble of pure states gives rise to it; in general there are infinitely many different ensembles generating the same density matrix. Those cannot be distinguished by any measurement. The equivalent ensembles can be completely characterized: let $\{p_{j},|\psi _{j}\rangle \}$ be an ensemble. Then for any complex matrix U such that $U^{\dagger }U=I$ (a partial isometry), the ensemble $\{q_{i},|\varphi _{i}\rangle \}$ defined by

${\sqrt {q_{i}}}\left|\varphi _{i}\right\rangle =\sum _{j}U_{ij}{\sqrt {p_{j}}}\left|\psi _{j}\right\rangle$

will give rise to the same density operator, and all equivalent ensembles are of this form.

A closely related fact is that a given density operator has infinitely many different purifications, which are pure states that generate the density operator when a partial trace is taken. Let

$\rho =\sum _{j}p_{j}|\psi _{j}\rangle \langle \psi _{j}|$

be the density operator generated by the ensemble $\{p_{j},|\psi _{j}\rangle \}$ , with states $|\psi _{j}\rangle$ not necessarily orthogonal. Then for all partial isometries U we have that

$|\Psi \rangle =\sum _{j}{\sqrt {p_{j}}}|\psi _{j}\rangle U|a_{j}\rangle$

is a purification of $\rho$ , where $|a_{j}\rangle$ is an orthogonal basis, and furthermore all purifications of $\rho$ are of this form.

## Measurement

Let A be an observable of the system, and suppose the ensemble is in a mixed state such that each of the pure states $\textstyle |\psi _{j}\rangle$ occurs with probability $p_{j}$ . Then the corresponding density operator equals

$\rho =\sum _{j}p_{j}|\psi _{j}\rangle \langle \psi _{j}|.$

The expectation value of the measurement can be calculated by extending from the case of pure states:

$\langle A\rangle =\sum _{j}p_{j}\langle \psi _{j}|A|\psi _{j}\rangle =\sum _{j}p_{j}\operatorname {tr} \left(|\psi _{j}\rangle \langle \psi _{j}|A\right)=\operatorname {tr} \left(\sum _{j}p_{j}|\psi _{j}\rangle \langle \psi _{j}|A\right)=\operatorname {tr} (\rho A),$

where $\operatorname {tr}$ denotes trace. Thus, the familiar expression $\langle A\rangle =\langle \psi |A|\psi \rangle$ for pure states is replaced by

$\langle A\rangle =\operatorname {tr} (\rho A)$

for mixed states.

Moreover, if A has spectral resolution

$A=\sum _{i}a_{i}P_{i},$

where $P_{i}$ is the projection operator into the eigenspace corresponding to eigenvalue $a_{i}$ , the post-measurement density operator is given by

$\rho _{i}'={\frac {P_{i}\rho P_{i}}{\operatorname {tr} \left[\rho P_{i}\right]}}$

when outcome *i* is obtained. In the case where the measurement result is not known the ensemble is instead described by

$\;\rho '=\sum _{i}P_{i}\rho P_{i}.$

If one assumes that the probabilities of measurement outcomes are linear functions of the projectors $P_{i}$ , then they must be given by the trace of the projector with a density operator. Gleason's theorem shows that in Hilbert spaces of dimension 3 or larger the assumption of linearity can be replaced with an assumption of non-contextuality. This restriction on the dimension can be removed by assuming non-contextuality for POVMs as well, but this has been criticized as physically unmotivated.

## Entropy

The von Neumann entropy S of a mixture can be expressed in terms of the eigenvalues of $\rho$ or in terms of the trace and logarithm of the density operator $\rho$ . Since $\rho$ is a positive semi-definite operator, it has a spectral decomposition such that $\rho =\textstyle \sum _{i}\lambda _{i}|\varphi _{i}\rangle \langle \varphi _{i}|$ , where $|\varphi _{i}\rangle$ are orthonormal vectors, $\lambda _{i}\geq 0$ , and $\textstyle \sum \lambda _{i}=1$ . Then the entropy of a quantum system with density matrix $\rho$ is

$S=-\sum _{i}\lambda _{i}\ln \lambda _{i}=-\operatorname {tr} (\rho \ln \rho ).$

This definition implies that the von Neumann entropy of any pure state is zero. If $\rho _{i}$ are states that have support on orthogonal subspaces, then the von Neumann entropy of a convex combination of these states,

$\rho =\sum _{i}p_{i}\rho _{i},$

is given by the von Neumann entropies of the states $\rho _{i}$ and the Shannon entropy of the probability distribution $p_{i}$ :

$S(\rho )=H(p_{i})+\sum _{i}p_{i}S(\rho _{i}).$

When the states $\rho _{i}$ do not have orthogonal supports, the sum on the right-hand side is strictly greater than the von Neumann entropy of the convex combination $\rho$ .

Given a density operator $\rho$ and a projective measurement as in the previous section, the state $\rho '$ defined by the convex combination

$\rho '=\sum _{i}P_{i}\rho P_{i},$

which can be interpreted as the state produced by performing the measurement but not recording which outcome occurred, has a von Neumann entropy larger than that of $\rho$ , except if $\rho =\rho '$ . It is however possible for the $\rho '$ produced by a *generalized* measurement, or POVM, to have a lower von Neumann entropy than $\rho$ .

## Von Neumann equation for time evolution

Just as the Schrödinger equation describes how pure states evolve in time, the **von Neumann equation** (also known as the **Liouville–von Neumann equation**) describes how a density operator evolves in time. The von Neumann equation dictates that

$i\hbar {\frac {d}{dt}}\rho =[H,\rho ]~,$

where the brackets denote a commutator.

This equation only holds when the density operator is taken to be in the Schrödinger picture, even though this equation seems at first look to emulate the Heisenberg equation of motion in the Heisenberg picture, with a crucial sign difference:

$i\hbar {\frac {d}{dt}}A_{\text{H}}=-[H_{\text{H}},A_{\text{H}}]~,$

where $A_{\text{H}}(t)$ is some *Heisenberg picture* operator; but in this picture the density matrix is *not time-dependent*, and the relative sign ensures that the time derivative of the expected value $\langle A\rangle$ comes out *the same as in the Schrödinger picture*.

If the Hamiltonian is time-independent, the von Neumann equation can be easily solved to yield

$\rho (t)=e^{-iHt/\hbar }\rho (0)e^{iHt/\hbar }.$

For a more general Hamiltonian, if $G(t)$ is the wavefunction propagator over some interval, then the time evolution of the density matrix over that same interval is given by

$\rho (t)=G(t)\rho (0)G(t)^{\dagger }.$

If one enters the interaction picture, choosing to focus on some component $H_{1}$ of the Hamiltonian $H=H_{0}+H_{1}$ , the equation for the evolution of the interaction-picture density operator $\rho _{\,\mathrm {I} }(t)$ possesses identical structure to the von Neumann equation, except the Hamiltonian must also be transformed into the new picture:

${\displaystyle i\hbar {\frac {d}{dt}}\rho _{\text{I}}(t)=[H_{1,{\text{I}}}(t),\rho _{\text{I}}(t)],}$

where ${\displaystyle H_{1,{\text{I}}}(t)=e^{iH_{0}t/\hbar }H_{1}e^{-iH_{0}t/\hbar }}$ .

## Wigner functions and classical analogies

The density matrix operator may also be realized in phase space. Under the Wigner map, the density matrix transforms into the equivalent Wigner function,

$W(x,p)\,\ {\stackrel {\mathrm {def} }{=}}\ \,{\frac {1}{\pi \hbar }}\int _{-\infty }^{\infty }\psi ^{*}(x+y)\psi (x-y)e^{2ipy/\hbar }\,dy.$

The equation for the time evolution of the Wigner function, known as Moyal equation, is then the Wigner-transform of the above von Neumann equation,

${\frac {\partial W(x,p,t)}{\partial t}}=-\{\{W(x,p,t),H(x,p)\}\},$

where $H(x,p)$ is the Hamiltonian, and $\{\{\cdot ,\cdot \}\}$ is the Moyal bracket, the transform of the quantum commutator.

The evolution equation for the Wigner function is then analogous to that of its classical limit, the Liouville equation of classical physics. In the limit of a vanishing Planck constant $\hbar$ , $W(x,p,t)$ reduces to the classical Liouville probability density function in phase space.

## Example applications

Density matrices are a basic tool of quantum mechanics, and appear at least occasionally in almost any type of quantum-mechanical calculation. Some specific examples where density matrices are especially helpful and common are as follows:

- Statistical mechanics uses density matrices, most prominently to express the idea that a system is prepared at a nonzero temperature. Constructing a density matrix using a canonical ensemble gives a result of the form $\rho =\exp(-\beta H)/Z(\beta )$ , where $\beta$ is the inverse temperature $(k_{\rm {B}}T)^{-1}$ and H is the system's Hamiltonian. The normalization condition that the trace of $\rho$ be equal to 1 defines the partition function to be $Z(\beta )=\mathrm {tr} \exp(-\beta H)$ . If the number of particles involved in the system is itself not certain, then a grand canonical ensemble can be applied, where the states summed over to make the density matrix are drawn from a Fock space.
- Quantum decoherence theory typically involves non-isolated quantum systems developing entanglement with other systems, including measurement apparatuses. Density matrices make it much easier to describe the process and calculate its consequences. Quantum decoherence explains why a system interacting with an environment transitions from being a pure state, exhibiting superpositions, to a mixed state, an incoherent combination of classical alternatives. This transition is fundamentally reversible, as the combined state of system and environment is still pure, but for all practical purposes irreversible, as the environment is a very large and complex quantum system, and it is not feasible to reverse their interaction. Decoherence is thus very important for explaining the classical limit of quantum mechanics, but cannot explain wave function collapse, as all classical alternatives are still present in the mixed state, and wave function collapse selects only one of them.
- Similarly, in quantum computation, quantum information theory, open quantum systems, and other fields where state preparation is noisy and decoherence can occur, density matrices are frequently used. Noise is often modelled via a depolarizing channel or an amplitude damping channel. Quantum tomography is a process by which, given a set of data representing the results of quantum measurements, a density matrix consistent with those measurement results is computed.
- When analyzing a system with many electrons, such as an atom or molecule, an imperfect but useful first approximation is to treat the electrons as uncorrelated or each having an independent single-particle wavefunction. This is the usual starting point when building the Slater determinant in the Hartree–Fock method. If there are N electrons filling the N single-particle wavefunctions $|\psi _{i}\rangle$ and if only single-particle observables are considered, then their expectation values for the N -electron system can be computed using the density matrix ${\textstyle \sum _{i=1}^{N}|\psi _{i}\rangle \langle \psi _{i}|}$ (the *one-particle density matrix* of the N -electron system).

## C*-algebraic formulation of states

It is now generally accepted that the description of quantum mechanics in which all self-adjoint operators represent observables is untenable. For this reason, observables are identified with elements of an abstract C*-algebra *A* (that is one without a distinguished representation as an algebra of operators) and states are positive linear functionals on *A*. However, by using the GNS construction, we can recover Hilbert spaces that realize *A* as a subalgebra of operators.

Geometrically, a pure state on a C*-algebra *A* is a state that is an extreme point of the set of all states on *A*. By properties of the GNS construction these states correspond to irreducible representations of *A*.

The states of the C*-algebra of compact operators *K*(*H*) correspond exactly to the density operators, and therefore the pure states of *K*(*H*) are exactly the pure states in the sense of quantum mechanics.

The C*-algebraic formulation can be seen to include both classical and quantum systems. When the system is classical, the algebra of observables become an abelian C*-algebra. In that case the states become probability measures.

## History

This formalism of the operators and matrices was introduced in 1927 by John von Neumann and independently, but less systematically, by Lev Landau and later in 1946 by Felix Bloch. Von Neumann introduced a matrix in order to develop both quantum statistical mechanics and a theory of quantum measurements. The term ***density*** was introduced by Dirac in 1931 when he used von Neumann's operator to calculate electron density clouds.

Nowadays the term "density matrix" obtained a significance of its own, and corresponds to a classical phase-space probability measure (probability distribution of position and momentum) in classical statistical mechanics, which was introduced by Eugene Wigner in 1932.

In contrast, the motivation that inspired Landau was the impossibility of describing a subsystem of a composite quantum system by a state vector.
