---
title: "Qubit"
source: https://en.wikipedia.org/wiki/Qubit
domain: quantum-computing
license: CC-BY-SA-4.0
tags: quantum computing, quantum logic gate, quantum entanglement, quantum circuit
fetched: 2026-07-02
---

# Qubit

In quantum computing, a **qubit** (/ˈkjuːbɪt/) or **quantum bit** is a basic unit of quantum information, the quantum version of the classic binary bit. A qubit can be physically realized with a two-state (or two-level) quantum-mechanical system, one of the simplest quantum systems displaying the peculiarity of quantum mechanics. Examples include the spin of the electron in which the two levels can be taken as spin up and spin down; or the polarization of a single photon in which the two spin states (left-handed and the right-handed circular polarization) can also be measured as horizontal and vertical linear polarization. In a classical system, a bit would have to be in one state or the other. However, quantum mechanics allows the qubit to be in a coherent superposition of multiple states simultaneously, a property that is fundamental to quantum mechanics and quantum computing. A qubit can be generalized as a d=2 qudit or a binary *qudit*.

## Etymology

The coining of the term *qubit* is attributed to Benjamin Schumacher. In the acknowledgments of his 1995 paper, Schumacher states that the term *qubit* was created in jest during a conversation with William Wootters.

## Comparison with classical bits

A binary digit, characterized as 0 or 1, is used to represent information in classical computers. When averaged over both of its states (0,1), a binary digit can represent up to one bit of information content, where a bit is the basic unit of information. However, in this article, the word bit is synonymous with a binary digit.

In classical computer technologies, a *processed* bit is implemented by one of two levels of low direct current voltage, and whilst switching from one of these two levels to the other, a so-called "forbidden zone" between two logic levels must be passed as fast as possible, in as much as electrical voltage cannot change amplitude instantaneously.

There are two possible outcomes for the measurement of a qubit, usually taken to have the values "0" and "1", like a bit. However, whereas the state of a bit can only be binary (either 0 or 1), the general state of a qubit according to quantum mechanics can be an arbitrary coherent superposition of *all* computable states simultaneously. Moreover, whereas a measurement of a classical bit would not disturb its state, a measurement of a qubit would destroy its coherence and irrevocably disturb the superposition state. It is possible to fully encode one bit in one qubit. However, a qubit can hold more information, e.g., up to two bits using superdense coding (see Holevo's theorem).

A bit is always completely in either one of its two states, and a set of n bits (e.g. a processor register or some bit array) can only hold a single of its 2n possible states at any time. A quantum state can be in a superposition state, which means that the qubit can have non-zero probability amplitude in both its states simultaneously (popularly expressed as "it can be in both states simultaneously"). A qubit requires two complex numbers to describe its two probability amplitudes, and these two complex numbers can together be viewed as a 2-dimensional complex vector, which is called a *quantum state vector*, or *superposition state vector.* Alternatively and equivalently, the value stored in a qubit can be described as a single point in a 2-dimensional complex coordinate space.

Furthermore, a set of n bits can be represented by n binary digits, simply by concatenating the representations of each of the bits, whereas a set of n qubits, which is also called a register, requires 2n complex numbers to describe its superposition state vector.

## Standard representation

In quantum mechanics, the general quantum state of a qubit can be represented by a linear superposition of its two orthonormal basis states (or basis vectors). These vectors are usually denoted as $|0\rangle ={\bigl [}{\begin{smallmatrix}1\\0\end{smallmatrix}}{\bigr ]}$ and $|1\rangle ={\bigl [}{\begin{smallmatrix}0\\1\end{smallmatrix}}{\bigr ]}$ . They are written in the conventional Dirac—or "bra–ket"—notation; the $|0\rangle$ and $|1\rangle$ are pronounced "ket 0" and "ket 1", respectively. These two orthonormal basis states, $\{|0\rangle ,|1\rangle \}$ , together called the computational basis, are said to span the two-dimensional linear vector (Hilbert) space of the qubit.

Qubit basis states can also be combined to form product basis states. A set of qubits taken together is called a quantum register. For example, two qubits could be represented in a four-dimensional linear vector space spanned by the following product basis states:

$|00\rangle ={\biggl [}{\begin{smallmatrix}1\\0\\0\\0\end{smallmatrix}}{\biggr ]}$ , $|01\rangle ={\biggl [}{\begin{smallmatrix}0\\1\\0\\0\end{smallmatrix}}{\biggr ]}$ , $|10\rangle ={\biggl [}{\begin{smallmatrix}0\\0\\1\\0\end{smallmatrix}}{\biggr ]}$ , and $|11\rangle ={\biggl [}{\begin{smallmatrix}0\\0\\0\\1\end{smallmatrix}}{\biggr ]}$ .

In general, *n* qubits are represented by a superposition state vector in 2*n* dimensional Hilbert space.

## Qubit states

A pure qubit state is a coherent superposition of the basis states. This means that a single qubit ( $\psi$ ) can be described by a linear combination of ${|0\rangle }$ and ${|1\rangle }$ :

${|\psi \rangle }=\alpha {|0\rangle }+\beta {|1\rangle }$

where *α* and *β* are the probability amplitudes, and are both complex numbers. When we measure this qubit in the standard basis, according to the Born rule, the probability of outcome ${|0\rangle }$ with value "0" is ${|\alpha |}^{2}$ and the probability of outcome ${|1\rangle }$ with value "1" is ${|\beta |}^{2}$ . Because the absolute squares of the amplitudes equate to probabilities, it follows that $\alpha$ and $\beta$ must be constrained according to the second axiom of probability theory by the equation

${|\alpha |}^{2}+{|\beta |}^{2}=1.$

The probability amplitudes, $\alpha$ and $\beta$ , encode more than just the probabilities of the outcomes of a measurement; the *relative phase* between $\alpha$ and $\beta$ is, for example, responsible for quantum interference, as seen in the double-slit experiment.

### Bloch sphere representation

The probability amplitudes for the superposition state, ${|\psi \rangle }=\alpha {|0\rangle }+\beta {|1\rangle },\,$ are given by $\alpha =\cos \left({\frac {\theta }{2}}\right)$ and $\beta =e^{i\varphi }\sin \left({\frac {\theta }{2}}\right)$

It might, at first sight, seem that there should be four degrees of freedom in ${|\psi \rangle }=\alpha {|0\rangle }+\beta {|1\rangle }\,$ , as $\alpha$ and $\beta$ are complex numbers with two degrees of freedom each. However, one degree of freedom is removed by the normalization constraint |*α*|2 + |*β*|2 = 1. This means, with a suitable change of coordinates, one can eliminate one of the degrees of freedom. One possible choice is that of Hopf coordinates:

${\begin{aligned}\alpha &=e^{i\delta }\cos {\frac {\theta }{2}},\\\beta &=e^{i(\delta +\varphi )}\sin {\frac {\theta }{2}}.\end{aligned}}$

Additionally, for a single qubit, the *global phase* of the state $e^{i\delta }$ has no physically observable consequences, so we can arbitrarily choose *α* to be real (or *β* in the case that *α* is zero), leaving just two degrees of freedom:

${\begin{aligned}\alpha &=\cos {\frac {\theta }{2}},\\\beta &=e^{i\varphi }\sin {\frac {\theta }{2}},\end{aligned}}$

where $e^{i\varphi }$ is the physically significant *relative phase*.

The possible quantum states for a single qubit can be visualised using a Bloch sphere (see picture). Represented on such a 2-sphere, a classical bit could only be at the "North Pole" or the "South Pole", in the locations where ${|0\rangle }$ and ${|1\rangle }$ are respectively. This particular choice of the polar axis is arbitrary, however. The rest of the surface of the Bloch sphere is inaccessible to a classical bit, but a pure qubit state can be represented by any point on the surface. For example, the pure qubit state $({|0\rangle }+{|1\rangle })/{\sqrt {2}}$ would lie on the equator of the sphere at the positive X-axis. In the classical limit, a qubit, which can have quantum states anywhere on the Bloch sphere, reduces to the classical bit, which can be found only at either poles.

The surface of the Bloch sphere is a two-dimensional space, which represents the observable state space of the pure qubit states. This state space has two local degrees of freedom, which can be represented by the two angles $\varphi$ and $\theta$ .

### Mixed state

A pure state is fully specified by a single ket, ${|\psi \rangle }=\alpha {|0\rangle }+\beta {|1\rangle },\,$ a coherent superposition, represented by a point on the surface of the Bloch sphere as described above. Coherence is essential for a qubit to be in a superposition state. With interactions, quantum noise and decoherence, it is possible to put the qubit in a mixed state, a statistical combination or "incoherent mixture" of different pure states. Mixed states can be represented by points *inside* the Bloch sphere (or in the Bloch ball). A mixed qubit state has three degrees of freedom: the angles $\varphi$ and $\theta$ , as well as the length r of the vector that represents the mixed state.

Quantum error correction can be used to maintain the purity of qubits.

## Operations on qubits

Various kinds of physical operations can be performed on qubits.

- Quantum logic gates, building blocks for a quantum circuit in a quantum computer, operate on a set of qubits (a register); mathematically, the qubits undergo a (reversible) unitary transformation described by multiplying the quantum gate's unitary matrix with the quantum state vector. The result from this multiplication is a new quantum state vector.
- Quantum measurement is an irreversible operation in which information is gained about the state of a single qubit, and coherence is lost. The result of the measurement of a single qubit with the state ${|\psi \rangle }=\alpha {|0\rangle }+\beta {|1\rangle }$ will be either ${|0\rangle }$ with probability ${|\alpha |}^{2}$ or ${|1\rangle }$ with probability ${|\beta |}^{2}$ . Measurement of the state of the qubit alters the magnitudes of *α* and *β*. For instance, if the result of the measurement is ${|1\rangle }$ , *α* is changed to 0 and *β* is changed to 1, while the phase factor $e^{i\phi }$ is no longer experimentally accessible. If measurement is performed on a qubit that is entangled, the measurement may collapse the state of the other entangled qubits.
- Initialization or re-initialization to a known value, often ${|0\rangle }$ . This operation collapses the quantum state (exactly like with measurement). Initialization to ${|0\rangle }$ may be implemented logically or physically: Logically as a measurement, followed by the application of the Pauli-X gate if the result from the measurement was ${|1\rangle }$ . Physically, for example, if it is a superconducting phase qubit, by lowering the energy of the quantum system to its ground state.
- Sending the qubit through a quantum channel to a remote system or machine (an I/O operation), potentially as part of a quantum network.

## Quantum entanglement

An important distinguishing feature between qubits and classical bits is that multiple qubits can exhibit quantum entanglement; the qubit itself is an exhibition of quantum entanglement. In this case, quantum entanglement is a local or nonlocal property of two or more qubits that allows a set of qubits to express higher correlation than is possible in classical systems.

The simplest system to display quantum entanglement is the system of two qubits. Consider, for example, two entangled qubits in the ${|\Phi ^{+}\rangle }$ Bell state:

${\frac {1}{\sqrt {2}}}({|00\rangle }+{|11\rangle }).$

In this state, called an *equal superposition*, there are equal probabilities of measuring either product state ${|00\rangle }$ or ${|11\rangle }$ , as ${|1/{\sqrt {2}}|}^{2}=1/2$ . In other words, there is no way to tell if the first qubit has value "0" or "1" and likewise for the second qubit.

Imagine that these two entangled qubits are separated, with one each given to Alice and Bob. Alice makes a measurement of her qubit, obtaining—with equal probabilities—either ${|0\rangle }$ or ${|1\rangle }$ , i.e., she can now tell if her qubit has value "0" or "1". Because of the qubits' entanglement, Bob must now get exactly the same measurement as Alice. For example, if she measures a ${|0\rangle }$ , Bob must measure the same, as ${|00\rangle }$ is the only state where Alice's qubit is a ${|0\rangle }$ . In short, for these two entangled qubits, whatever Alice measures, so would Bob, with perfect correlation, in any basis, however far apart they may be and even though both can not tell if their qubit has value "0" or "1"—a most surprising circumstance that cannot be explained by classical physics.

### Controlled gate to construct the Bell state

Controlled gates act on 2 or more qubits, where one or more qubits act as a control for some specified operation. In particular, the controlled NOT gate (CNOT or CX) acts on 2 qubits, and performs the NOT operation on the second qubit only when the first qubit is ${|1\rangle }$ , and otherwise leaves it unchanged. With respect to the unentangled product basis $\{{|00\rangle }$ , ${|01\rangle }$ , ${|10\rangle }$ , ${|11\rangle }\}$ , it maps the basis states as follows:

${|00\rangle }\mapsto {|00\rangle }$

${|01\rangle }\mapsto {|01\rangle }$

${|10\rangle }\mapsto {|11\rangle }$

${|11\rangle }\mapsto {|10\rangle }$

.

A common application of the CNOT gate is to maximally entangle two qubits into the ${|\Phi ^{+}\rangle }$ Bell state. To construct ${|\Phi ^{+}\rangle }$ , the inputs A (control) and B (target) to the CNOT gate are:

${\frac {1}{\sqrt {2}}}({|0\rangle }+{|1\rangle })_{A}$ $\otimes$ ${|0\rangle }_{B}$ = ${\frac {1}{\sqrt {2}}}$ $({|00\rangle }+{|10\rangle })$ .

After applying CNOT, the output is the ${|\Phi ^{+}\rangle }$ Bell State: ${\frac {1}{\sqrt {2}}}({|00\rangle }+{|11\rangle })$ .

### Applications

The ${|\Phi ^{+}\rangle }$ Bell state forms part of the setup of the superdense coding, quantum teleportation, and entangled quantum cryptography algorithms.

Quantum entanglement also allows multiple states (such as the Bell state mentioned above) to be acted on simultaneously, unlike classical bits that can only have one value at a time. Entanglement is a necessary ingredient of any quantum computation that cannot be done efficiently on a classical computer. Many of the successes of quantum computation and communication, such as quantum teleportation and superdense coding, make use of entanglement, suggesting that entanglement is a resource that is unique to quantum computation. A major hurdle facing quantum computing, as of 2018, in its quest to surpass classical digital computing, is noise in quantum gates that limits the size of quantum circuits that can be executed reliably.

## Quantum register

A number of qubits taken together is a qubit register. Quantum computers perform calculations by manipulating qubits within a register.

### Qudits and qutrits

The term **qudit** denotes the unit of quantum information that can be realized in suitable *d*-level quantum systems.

Qudits are similar to the integer types in classical computing, and may be mapped to (or realized by) arrays of qubits. Qudits where the *d*-level system is not an exponent of 2 cannot be mapped to arrays of qubits. It is for example possible to have 5-level qudits.

In 2017, scientists at the National Institute of Scientific Research constructed a pair of qudits with 10 different states each, giving more computational power than 6 qubits.

In 2022, researchers at the University of Innsbruck succeeded in developing a universal qudit quantum processor with trapped ions. In the same year, researchers at Tsinghua University's Center for Quantum Information implemented the dual-type qubit scheme in trapped ion quantum computers using the same ion species. In 2025, the Innsbruck team managed to simulate two-dimensional lattice gauge theories on their qudit quantum computer.

Also in 2022, researchers at the University of California, Berkeley developed a technique to dynamically control the cross-Kerr interactions between fixed-frequency qutrits, achieving high two-qutrit gate fidelities. This was followed by a demonstration of extensible control of superconducting qudits up to $d=4$ in 2024 based on programmable two-photon interactions.

Similar to the qubit, the qutrit is the unit of quantum information that can be realized in suitable 3-level quantum systems. This is analogous to the unit of classical information trit of ternary computers. Besides the advantage associated with the enlarged computational space, the third qutrit level can be exploited to implement efficient compilation of multi-qubit gates.

## Physical implementation

Any two-level quantum-mechanical system can be used as a qubit. Multilevel systems can be used as well, if they possess two states that can be effectively decoupled from the rest (e.g., the ground state and first excited state of a nonlinear oscillator). There are various proposals. Several physical implementations that approximate two-level systems to various degrees have been successfully realized. Similarly to a classical bit, where the state of a transistor in a processor, the magnetization of a surface in a hard disk, and the presence of current in a cable can all be used to represent bits in the same computer, an eventual quantum computer is likely to use various combinations of qubits in its design.

All physical implementations are affected by noise. The so-called *T*1 lifetime and *T*2 dephasing time are a time to characterize the physical implementation and represent their sensitivity to noise. A higher time does not necessarily mean that one or the other qubit is better suited for quantum computing, as gate times and fidelities also need to be considered.

Different applications like quantum sensing, quantum computing and quantum communication use different implementations of qubits to suit their application.

The following is an incomplete list of physical implementations of qubits, and the choices of basis are by convention only.

| Physical support | Name | Information support | ${\|0\rangle }$ | ${\|1\rangle }$ |
|---|---|---|---|---|
| photon | polarization encoding | polarization of light | horizontal | vertical |
| number of photons | Fock state | vacuum | single-photon state |   |
| time-bin encoding | time of arrival | early | late |   |
| coherent state of light | squeezed light | quadrature | amplitude-squeezed state | phase-squeezed state |
| electrons | electronic spin | spin | up | down |
| electron number | charge | no electron | two electron |   |
| nucleus | nuclear spin addressed through NMR | spin | up | down |
| neutral atom | atomic energy level | spin | up | down |
| trapped ion | atomic energy level | spin | up | down |
| Josephson junction | superconducting charge qubit | charge | uncharged superconducting island (*Q* = 0) | charged superconducting island (*Q* = 2*e*, one extra Cooper pair) |
| superconducting flux qubit | current | clockwise current | counterclockwise current |   |
| superconducting phase qubit | energy | ground state | first excited state |   |
| singly charged quantum dot pair | electron localization | charge | electron on left dot | electron on right dot |
| quantum dot | dot spin | spin | down | up |
| gapped topological system | non-abelian anyons | braiding of excitations | depends on specific topological system | depends on specific topological system |
| vibrational qubit | vibrational states | phonon/vibron | ${\|01\rangle }$ superposition | ${\|10\rangle }$ superposition |
| van der Waals heterostructure | electron localization | charge | electron on bottom sheet | electron on top sheet |

## Qubit storage

In 2008 a team of scientists from the U.K. and U.S. reported the first relatively long (1.75 seconds) and coherent transfer of a superposition state in an electron spin "processing" qubit to a nuclear spin "memory" qubit. This event can be considered the first relatively consistent quantum data storage, a vital step towards the development of quantum computing. In 2013, a modification of similar systems (using charged rather than neutral donors) has dramatically extended this time, to 3 hours at very low temperatures and 39 minutes at room temperature. Room temperature preparation of a qubit based on electron spins instead of nuclear spin was also demonstrated by a team of scientists from Switzerland and Australia. An increased coherence of qubits is being explored by researchers who are testing the limitations of a Ge hole spin-orbit qubit structure.
