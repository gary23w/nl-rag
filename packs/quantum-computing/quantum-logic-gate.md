---
title: "Quantum logic gate"
source: https://en.wikipedia.org/wiki/Quantum_logic_gate
domain: quantum-computing
license: CC-BY-SA-4.0
tags: quantum computing, quantum logic gate, quantum entanglement, quantum circuit
fetched: 2026-07-02
---

# Quantum logic gate

In quantum computing and specifically the quantum circuit model of computation, a **quantum logic gate** (or simply **quantum gate**) is a basic quantum circuit operating on a small number of qubits. Quantum logic gates are the building blocks of quantum circuits, like classical logic gates are for conventional digital circuits.

According to quantum mechanics, a quantum system can *only either* evolve unitarily according to the Schrödinger equation, or be measured (sometimes called "Observed"). Quantum gates describe these unitary transformations, that occur when the system is not being measured. The expression "quantum gate" appears in relation to quantum processors, and in this context they are the logical operations that the quantum computer at the assembly language-level of abstraction (e.g. OpenQASM) can perform on the quantum data (qubits or quantum states) that they process, although they can also be whole algorithms (e.g. the Quantum Fourier transform) – But this is only true if such algorithms contains no measurement operations. When the quantum data is measured, it is usually transformed into binary bits, which is then sent to a normal ("classical") computer. The quantum processor behaves like a co-processor to such classical binary processors.

Unlike many classical logic gates, quantum logic gates are reversible. It is possible to perform classical computing using only reversible gates. For example, the reversible Toffoli gate can implement all Boolean functions, often at the cost of having to use ancilla bits. The Toffoli gate has a direct quantum equivalent, showing that quantum circuits can perform all operations performed by classical circuits.

Quantum gates are unitary operators, and are described as unitary matrices relative to some orthonormal basis. Usually the *computational basis* is used, which unless comparing it with something, just means that for a *d*-level quantum system (such as a qubit, a quantum register, or qutrits and qudits) the orthonormal basis vectors are labeled $|0\rangle ,|1\rangle ,\dots ,|d-1\rangle$ , or use binary notation.

## History

The current notation for quantum gates was developed by many of the founders of quantum information science including Adriano Barenco, Charles Bennett, Richard Cleve, David P. DiVincenzo, Norman Margolus, Peter Shor, Tycho Sleator, John A. Smolin, and Harald Weinfurter, building on notation introduced by Richard Feynman in 1986.

## Representation

Quantum logic gates are represented by unitary matrices. A gate that acts on n qubits (a register) is represented by a $2^{n}\times 2^{n}$ unitary matrix, and the set of all such gates with the group operation of matrix multiplication is the unitary group U(2*n*). The quantum states that the gates act upon are unit vectors in $2^{n}$ complex dimensions, with the complex Euclidean norm (the 2-norm). The basis vectors (sometimes called *eigenstates*) are the possible outcomes if the state of the qubits is measured, and a quantum state is a linear combination of these outcomes. The most common quantum gates operate on vector spaces of one or two qubits, just like the common classical logic gates operate on one or two bits.

Even though the quantum logic gates belong to continuous symmetry groups, real hardware is inexact and thus limited in precision. The application of gates typically introduces errors, and the quantum states' fidelities decrease over time. If error correction is used, the usable gates are further restricted to a finite set. Later in this article, this is ignored as the focus is on the ideal quantum gates' properties.

Quantum states are typically represented by "kets", from a notation known as bra–ket.

The vector representation of a single qubit is

$|a\rangle =v_{0}|0\rangle +v_{1}|1\rangle \rightarrow {\begin{bmatrix}v_{0}\\v_{1}\end{bmatrix}}.$

Here, $v_{0}$ and $v_{1}$ are the complex probability amplitudes of the qubit. These values determine the probability of measuring a 0 or a 1, when measuring the state of the qubit. See measurement below for details.

The value zero is represented by the ket $|0\rangle ={\begin{bmatrix}1\\0\end{bmatrix}}$ , and the value one is represented by the ket $|1\rangle ={\begin{bmatrix}0\\1\end{bmatrix}}$ .

The tensor product (or Kronecker product) is used to combine quantum states. The combined state for a qubit register is the tensor product of the constituent qubits. The tensor product is denoted by the symbol $\otimes$ .

The vector representation of two qubits is:

$|\psi \rangle =v_{00}|00\rangle +v_{01}|01\rangle +v_{10}|10\rangle +v_{11}|11\rangle \rightarrow {\begin{bmatrix}v_{00}\\v_{01}\\v_{10}\\v_{11}\end{bmatrix}}.$

The action of the gate on a specific quantum state is found by multiplying the vector $|\psi _{1}\rangle$ , which represents the state by the matrix U representing the gate. The result is a new quantum state $|\psi _{2}\rangle$ :

$U|\psi _{1}\rangle =|\psi _{2}\rangle .$

### Relation to the time evolution operator

The Schrödinger equation describes how quantum systems that are not observed evolve over time, and is $i\hbar {\frac {d}{dt}}|\Psi \rangle ={\hat {H}}|\Psi \rangle .$ When the system is in a stable environment, so it has a constant Hamiltonian, the solution to this equation is $U(t)=e^{-i{\hat {H}}t/\hbar }.$ If the time t is always the same it may be omitted for simplicity, and the way quantum states evolve can be described as $U|\psi _{1}\rangle =|\psi _{2}\rangle ,$ just as in the above section.

That is, a quantum gate is how a quantum system that is not observed evolves over some specific time, or equivalently, a gate is the unitary time evolution operator U acting on a quantum state for a specific duration.

## Notable examples

There exists an uncountably infinite number of gates. Some of them have been named by various authors, and below follow some of those most often used in the literature.

### Identity gate

The identity gate is the identity matrix, usually written as *I*, and is defined for a single qubit as

$I={\begin{bmatrix}1&0\\0&1\end{bmatrix}},$

where *I* is basis independent and does not modify the quantum state. The identity gate is most useful when describing mathematically the result of various gate operations or when discussing multi-qubit circuits.

### Pauli gates (*X*,*Y*,*Z*)

Quantum gates (from top to bottom): Identity gate, NOT gate, Pauli Y, Pauli Z

The Pauli gates $(X,Y,Z)$ are the three Pauli matrices $(\sigma _{x},\sigma _{y},\sigma _{z})$ and act on a single qubit. The Pauli *X*, *Y* and *Z* equate, respectively, to a rotation around the *x*, *y* and *z* axes of the Bloch sphere by $\pi$ radians.

The Pauli-*X* gate is the quantum equivalent of the NOT gate for classical computers with respect to the standard basis $|0\rangle$ , $|1\rangle$ , which distinguishes the *z* axis on the Bloch sphere. It is sometimes called a bit-flip as it maps $|0\rangle$ to $|1\rangle$ and $|1\rangle$ to $|0\rangle$ . Similarly, the Pauli-*Y* maps $|0\rangle$ to $i|1\rangle$ and $|1\rangle$ to $-i|0\rangle$ . Pauli *Z* leaves the basis state $|0\rangle$ unchanged and maps $|1\rangle$ to $-|1\rangle$ . Due to this nature, Pauli *Z* is sometimes called phase-flip.

These matrices are usually represented as

$X=\sigma _{x}=\operatorname {NOT} ={\begin{bmatrix}0&1\\1&0\end{bmatrix}},$

$Y=\sigma _{y}={\begin{bmatrix}0&-i\\i&0\end{bmatrix}},$

$Z=\sigma _{z}={\begin{bmatrix}1&0\\0&-1\end{bmatrix}}.$

The Pauli matrices are involutory, meaning that the square of a Pauli matrix is the identity matrix.

$I^{2}=X^{2}=Y^{2}=Z^{2}=-iXYZ=I$

The Pauli matrices also anti-commute, for example $ZX=iY=-XZ.$

The matrix exponential of a Pauli matrix $\sigma _{j}$ is a rotation operator, often written as $e^{-i\sigma _{j}\theta /2}.$

### Controlled gates

Controlled gates act on 2 or more qubits, where one or more qubits act as a control for some operation. For example, the controlled NOT gate (or CNOT or CX) acts on 2 qubits, and performs the NOT operation on the second qubit only when the first qubit is $|1\rangle$ , and otherwise leaves it unchanged. With respect to the basis $|00\rangle$ , $|01\rangle$ , $|10\rangle$ , $|11\rangle$ , it is represented by the Hermitian unitary matrix:

${\mbox{CNOT}}={\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{bmatrix}}.$

The CNOT (or controlled Pauli-*X*) gate can be described as the gate that maps the basis states $|a,b\rangle \mapsto |a,a\oplus b\rangle$ , where $\oplus$ is XOR.

The CNOT can be expressed in the Pauli basis as:

${\mbox{CNOT}}=e^{i{\frac {\pi }{4}}(I-Z_{1})(I-X_{2})}=e^{-i{\frac {\pi }{4}}(I-Z_{1})(I-X_{2})}.$

Being a Hermitian unitary operator, CNOT has the property that $e^{i\theta U}=(\cos \theta )I+(i\sin \theta )U$ and $U=e^{i{\frac {\pi }{2}}(I-U)}=e^{-i{\frac {\pi }{2}}(I-U)}$ , and is involutory.

More generally if *U* is a gate that operates on a single qubit with matrix representation

$U={\begin{bmatrix}u_{00}&u_{01}\\u_{10}&u_{11}\end{bmatrix}},$

then the *controlled-U gate* is a gate that operates on two qubits in such a way that the first qubit serves as a control. It maps the basis states as follows.

Circuit diagrams of controlled Pauli gates (from left to right): CNOT (or controlled-X), controlled-Y and controlled-Z.

$|00\rangle \mapsto |00\rangle$

$|01\rangle \mapsto |01\rangle$

$|10\rangle \mapsto |1\rangle \otimes U|0\rangle =|1\rangle \otimes (u_{00}|0\rangle +u_{10}|1\rangle )$

$|11\rangle \mapsto |1\rangle \otimes U|1\rangle =|1\rangle \otimes (u_{01}|0\rangle +u_{11}|1\rangle )$

The matrix representing the controlled *U* is

${\mbox{C}}U={\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&u_{00}&u_{01}\\0&0&u_{10}&u_{11}\end{bmatrix}}.$

When *U* is one of the Pauli operators, *X*,*Y*, *Z*, the respective terms "controlled-*X*", "controlled-*Y*", or "controlled-*Z*" are sometimes used. Sometimes this is shortened to just C*X*, C*Y* and C*Z*.

In general, any single qubit unitary gate can be expressed as $U=e^{iH}$ , where *H* is a Hermitian matrix, and then the controlled *U* is ${\mbox{C}}U=e^{i{\frac {1}{2}}(I-Z_{1})H_{2}}.$

Control can be extended to gates with arbitrary number of qubits and functions in programming languages. Functions can be conditioned on superposition states.

#### Classical control

Gates can also be controlled by classical logic. A quantum computer is controlled by a classical computer, and behaves like a coprocessor that receives instructions from the classical computer about what gates to execute on which qubits. Classical control is simply the inclusion, or omission, of gates in the instruction sequence for the quantum computer. Performing measurements in the middle of a quantum circuit, as opposed to the end of it, is difficult and technically challanging because of timing issues and decoherence. Because of this, not all quantum computers support these classical if-statement, where quantum data is converted to bits, which then controls the program flow.

### Phase shift gates

The phase shift is a family of single-qubit gates that map the basis states $|0\rangle \mapsto |0\rangle$ and $|1\rangle \mapsto e^{i\varphi }|1\rangle$ . The probability of measuring a $|0\rangle$ or $|1\rangle$ is unchanged after applying this gate, however it modifies the phase of the quantum state. This is equivalent to tracing a horizontal circle (a line of constant latitude), or a rotation about the z-axis on the Bloch sphere by $\varphi$ radians. The phase shift gate is represented by the matrix:

$P(\varphi )={\begin{bmatrix}1&0\\0&e^{i\varphi }\end{bmatrix}}$

where $\varphi$ is the *phase shift* with the period 2π. Some common examples are the *T* gate where ${\textstyle \varphi ={\frac {\pi }{4}}}$ (historically known as the $\pi /8$ gate), the phase gate (also known as the S gate, written as *S*, though *S* is sometimes used for SWAP gates) where ${\textstyle \varphi ={\frac {\pi }{2}}}$ and the Pauli-*Z* gate where $\varphi =\pi .$

The phase shift gates are related to each other as follows:

$Z={\begin{bmatrix}1&0\\0&e^{i\pi }\end{bmatrix}}={\begin{bmatrix}1&0\\0&-1\end{bmatrix}}=P\left(\pi \right)$

$S={\begin{bmatrix}1&0\\0&e^{i{\frac {\pi }{2}}}\end{bmatrix}}={\begin{bmatrix}1&0\\0&i\end{bmatrix}}=P\left({\frac {\pi }{2}}\right)={\sqrt {Z}}$

$T={\begin{bmatrix}1&0\\0&e^{i{\frac {\pi }{4}}}\end{bmatrix}}=P\left({\frac {\pi }{4}}\right)={\sqrt {S}}={\sqrt[{4}]{Z}}$

Note that the phase gate $P(\varphi )$ is not Hermitian (except for all $\varphi =n\pi ,n\in \mathbb {Z}$ ). These gates are different from their Hermitian conjugates: $P^{\dagger }(\varphi )=P(-\varphi )$ . The two adjoint (or conjugate transpose) gates $S^{\dagger }$ and $T^{\dagger }$ are sometimes included in instruction sets.

### Hadamard gate

The Hadamard or Walsh-Hadamard gate, named after Jacques Hadamard (French: [adamaʁ]) and Joseph L. Walsh, acts on a single qubit. It maps the basis states ${\textstyle |0\rangle \mapsto {\frac {|0\rangle +|1\rangle }{\sqrt {2}}}}$ and ${\textstyle |1\rangle \mapsto {\frac {|0\rangle -|1\rangle }{\sqrt {2}}}}$ (it creates an equal superposition state if given a computational basis state). The two states $(|0\rangle +|1\rangle )/{\sqrt {2}}$ and $(|0\rangle -|1\rangle )/{\sqrt {2}}$ are sometimes written $|+\rangle$ and $|-\rangle$ respectively. The Hadamard gate performs a rotation of $\pi$ about the axis $({\hat {x}}+{\hat {z}})/{\sqrt {2}}$ at the Bloch sphere, and is therefore involutory. It is represented by the Hadamard matrix:

$H={\frac {1}{\sqrt {2}}}{\begin{bmatrix}1&1\\1&-1\end{bmatrix}}.$

If the Hermitian (so $H^{\dagger }=H^{-1}=H$ ) Hadamard gate is used to perform a change of basis, it flips ${\hat {x}}$ and ${\hat {z}}$ . For example, $HZH=X$ and $H{\sqrt {X}}\;H={\sqrt {Z}}=S.$

### Swap gate

The swap gate swaps two qubits. With respect to the basis $|00\rangle$ , $|01\rangle$ , $|10\rangle$ , $|11\rangle$ , it is represented by the matrix

${\mbox{SWAP}}={\begin{bmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{bmatrix}}.$

The swap gate can be decomposed into summation form:

${\mbox{SWAP}}={\frac {I\otimes I+X\otimes X+Y\otimes Y+Z\otimes Z}{2}}$

### Toffoli (CCNOT) gate

The Toffoli gate, named after Tommaso Toffoli and also called the CCNOT gate or Deutsch gate $D(\pi /2)$ , is a 3-bit gate that is universal for classical computation but not for quantum computation. The quantum Toffoli gate is the same gate, defined for 3 qubits. If we limit ourselves to only accepting input qubits that are $|0\rangle$ and $|1\rangle$ , then if the first two bits are in the state $|1\rangle$ it applies a Pauli-*X* (or NOT) on the third bit, else it does nothing. It is an example of a CC-U (controlled-controlled Unitary) gate. Since it is the quantum analog of a classical gate, it is completely specified by its truth table. The Toffoli gate is universal when combined with the single qubit Hadamard gate.

| Truth table | Matrix form |
|---|---|
| Input Output 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0 1 0 0 1 1 0 1 1 1 0 0 1 0 0 1 0 1 1 0 1 1 1 0 1 1 1 1 1 1 1 1 0 | ${\begin{bmatrix}1&0&0&0&0&0&0&0\\0&1&0&0&0&0&0&0\\0&0&1&0&0&0&0&0\\0&0&0&1&0&0&0&0\\0&0&0&0&1&0&0&0\\0&0&0&0&0&1&0&0\\0&0&0&0&0&0&0&1\\0&0&0&0&0&0&1&0\\\end{bmatrix}}$ |

The Toffoli gate is related to the classical AND ( $\land$ ) and XOR ( $\oplus$ ) operations as it performs the mapping $|a,b,c\rangle \mapsto |a,b,c\oplus (a\land b)\rangle$ on states in the computational basis.

The Toffoli gate can be expressed using Pauli matrices as

${\mbox{Toff}}=e^{i{\frac {\pi }{8}}(I-Z_{1})(I-Z_{2})(I-X_{3})}=e^{-i{\frac {\pi }{8}}(I-Z_{1})(I-Z_{2})(I-X_{3})}.$

## Universal quantum gates

A set of **universal quantum gates** is any set of gates to which any operation possible on a quantum computer can be reduced, that is, any other unitary operation can be expressed as a finite sequence of gates from the set. Technically, this is impossible with anything less than an uncountable set of gates since the number of possible quantum gates is uncountable, whereas the number of finite sequences from a finite set is countable. To solve this problem, we only require that any quantum operation can be approximated by a sequence of gates from this finite set. Moreover, for unitaries on a constant number of qubits, the Solovay–Kitaev theorem guarantees that this can be done efficiently. Checking if a set of quantum gates is universal can be done using group theory methods and/or relation to (approximate) unitary t-designs. The spectral gap conjecture, if true, would imply that a generically chosen set of quantum gates is efficiently universal.

Some universal quantum gate sets include:

- The rotation operators *Rx*(*θ*), *Ry*(*θ*), *Rz*(*θ*), the phase shift gate *P*(*φ*) and CNOT are commonly used to form a universal quantum gate set.
- The Clifford set {CNOT, *H*, *S*} + *T* gate. The Clifford set alone is not a universal quantum gate set, as it can be efficiently simulated classically according to the Gottesman–Knill theorem.
- The Toffoli gate + Hadamard gate. The Toffoli gate alone forms a set of universal gates for reversible Boolean algebraic logic circuits, which encompasses all classical computation.

### Deutsch gate

A single-gate set of universal quantum gates can also be formulated using the parametrized three-qubit Deutsch gate $D(\theta )$ , named after physicist David Deutsch. It is a general case of *CC-U*, or *controlled-controlled-unitary* gate, and is defined as

$|a,b,c\rangle \mapsto {\begin{cases}i\cos(\theta )|a,b,c\rangle +\sin(\theta )|a,b,1-c\rangle &{\text{for}}\ a=b=1,\\|a,b,c\rangle &{\text{otherwise}}.\end{cases}}$

Unfortunately, a working Deutsch gate has remained out of reach, due to lack of a protocol. There are some proposals to realize a Deutsch gate with dipole–dipole interaction in neutral atoms.

A universal logic gate for reversible classical computing, the Toffoli gate, is reducible to the Deutsch gate $D(\pi /2)$ , thus showing that all reversible classical logic operations can be performed on a universal quantum computer.

There also exist single two-qubit gates sufficient for universality. In 1996, Adriano Barenco showed that the Deutsch gate can be decomposed using only a single two-qubit gate (Barenco gate), but it is hard to realize experimentally. This feature is exclusive to quantum circuits, as there is no classical two-bit gate that is both reversible and universal. Universal two-qubit gates could be implemented to improve classical reversible circuits in fast low-power microprocessors.

## Circuit composition

### Serially wired gates

Assume that we have two gates *A* and *B* that both act on n qubits. When *B* is put after *A* in a series circuit, then the effect of the two gates can be described as a single gate *C*.

$C=B\cdot A$

where $\cdot$ is matrix multiplication. The resulting gate *C* will have the same dimensions as *A* and *B*. The order in which the gates would appear in a circuit diagram is reversed when multiplying them together.

For example, putting the Pauli *X* gate after the Pauli *Y* gate, both of which act on a single qubit, can be described as a single combined gate *C*:

$C=X\cdot Y={\begin{bmatrix}0&1\\1&0\end{bmatrix}}\cdot {\begin{bmatrix}0&-i\\i&0\end{bmatrix}}={\begin{bmatrix}i&0\\0&-i\end{bmatrix}}=iZ$

The product symbol ( $\cdot$ ) is often omitted.

#### Exponents of quantum gates

All real exponents of unitary matrices are also unitary matrices, and all quantum gates are unitary matrices.

Positive integer exponents are equivalent to sequences of serially wired gates (e.g. $X^{3}=X\cdot X\cdot X$ ), and the real exponents is a generalization of the series circuit. For example, $X^{\pi }$ and ${\sqrt {X}}=X^{1/2}$ are both valid quantum gates.

$U^{0}=I$ for any unitary matrix U . The identity matrix ( I ) behaves like a NOP and can be represented as bare wire in quantum circuits, or not shown at all.

All gates are unitary matrices, so that $U^{\dagger }U=UU^{\dagger }=I$ and $U^{\dagger }=U^{-1}$ , where $\dagger$ is the conjugate transpose. This means that negative exponents of gates are unitary inverses of their positively exponentiated counterparts: $U^{-n}=(U^{n})^{\dagger }$ . For example, some negative exponents of the phase shift gates are $T^{-1}=T^{\dagger }$ and $T^{-2}=(T^{2})^{\dagger }=S^{\dagger }$ .

Note that for a Hermitian matrix $H^{\dagger }=H,$ and because of unitarity, $HH^{\dagger }=I,$ so $H^{2}=I$ for all Hermitian gates. They are involutory. Examples of Hermitian gates are the Pauli gates, Hadamard, CNOT, SWAP and Toffoli. Each Hermitian unitary matrix H has the property that $e^{i\theta H}=(\cos \theta )I+(i\sin \theta )H$ where $H=e^{i{\frac {\pi }{2}}(I-H)}=e^{-i{\frac {\pi }{2}}(I-H)}.$

The exponent of a gate is a multiple of the duration of time that the time evolution operator is applied to a quantum state. E.g., in a spin qubit quantum computer the ${\sqrt {\mathrm {SWAP} }}$ gate could be realized via exchange interaction on the spin of two electrons for half the duration of a full exchange interaction.

### Parallel gates

The tensor product (or Kronecker product) of two quantum gates is the gate that is equal to the two gates in parallel.

If we, as in the picture, combine the Pauli-*Y* gate with the Pauli-*X* gate in parallel, then this can be written as:

$C=Y\otimes X={\begin{bmatrix}0&-i\\i&0\end{bmatrix}}\otimes {\begin{bmatrix}0&1\\1&0\end{bmatrix}}={\begin{bmatrix}0{\begin{bmatrix}0&1\\1&0\end{bmatrix}}&-i{\begin{bmatrix}0&1\\1&0\end{bmatrix}}\\i{\begin{bmatrix}0&1\\1&0\end{bmatrix}}&0{\begin{bmatrix}0&1\\1&0\end{bmatrix}}\end{bmatrix}}={\begin{bmatrix}0&0&0&-i\\0&0&-i&0\\0&i&0&0\\i&0&0&0\end{bmatrix}}$

Both the Pauli-*X* and the Pauli-*Y* gate act on a single qubit. The resulting gate C act on two qubits.

Sometimes the tensor product symbol is omitted, and indexes are used for the operators instead.

#### Hadamard transform

The gate $H_{2}=H\otimes H$ is the Hadamard gate ( H ) applied in parallel on 2 qubits. It can be written as:

$H_{2}=H\otimes H={\frac {1}{\sqrt {2}}}{\begin{bmatrix}1&1\\1&-1\end{bmatrix}}\otimes {\frac {1}{\sqrt {2}}}{\begin{bmatrix}1&1\\1&-1\end{bmatrix}}={\frac {1}{2}}{\begin{bmatrix}1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1\end{bmatrix}}$

This "two-qubit parallel Hadamard gate" will, when applied to, for example, the two-qubit zero-vector ( $|00\rangle$ ), create a quantum state that has equal probability of being observed in any of its four possible outcomes; $|00\rangle$ , $|01\rangle$ , $|10\rangle$ , and $|11\rangle$ . We can write this operation as:

$H_{2}|00\rangle ={\frac {1}{2}}{\begin{bmatrix}1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1\end{bmatrix}}{\begin{bmatrix}1\\0\\0\\0\end{bmatrix}}={\frac {1}{2}}{\begin{bmatrix}1\\1\\1\\1\end{bmatrix}}={\frac {1}{2}}|00\rangle +{\frac {1}{2}}|01\rangle +{\frac {1}{2}}|10\rangle +{\frac {1}{2}}|11\rangle ={\frac {|00\rangle +|01\rangle +|10\rangle +|11\rangle }{2}}$

Here the amplitude for each measurable state is 1⁄2. The probability to observe any state is the square of the absolute value of the measurable states amplitude, which in the above example means that there is one in four that we observe any one of the individual four cases. See measurement for details.

$H_{2}$ performs the Hadamard transform on two qubits. Similarly the gate $\underbrace {H\otimes H\otimes \dots \otimes H} _{n{\text{ times}}}=\bigotimes _{i=0}^{n-1}H=H^{\otimes n}=H_{n}$ performs a Hadamard transform on a register of n qubits.

When applied to a register of n qubits all initialized to $|0\rangle$ , the Hadamard transform puts the quantum register into a superposition with equal probability of being measured in any of its $2^{n}$ possible states:

$\bigotimes _{i=0}^{n-1}(H|0\rangle )={\frac {1}{\sqrt {2^{n}}}}{\begin{bmatrix}1\\1\\\vdots \\1\end{bmatrix}}={\frac {1}{\sqrt {2^{n}}}}{\Big (}|0\rangle +|1\rangle +\dots +|2^{n}-1\rangle {\Big )}={\frac {1}{\sqrt {2^{n}}}}\sum _{i=0}^{2^{n}-1}|i\rangle$

This state is a *uniform superposition* and it is generated as the first step in some search algorithms, for example in amplitude amplification and phase estimation.

Measuring this state results in a random number between $|0\rangle$ and $|2^{n}-1\rangle$ . How random the number is depends on the fidelity of the logic gates. If not measured, it is a quantum state with equal probability amplitude ${\frac {1}{\sqrt {2^{n}}}}$ for each of its possible states.

The Hadamard transform acts on a register $|\psi \rangle$ with n qubits such that ${\textstyle |\psi \rangle =\bigotimes _{i=0}^{n-1}|\psi _{i}\rangle }$ as follows:

$\bigotimes _{i=0}^{n-1}H|\psi \rangle =\bigotimes _{i=0}^{n-1}{\frac {|0\rangle +(-1)^{\psi _{i}}|1\rangle }{\sqrt {2}}}={\frac {1}{\sqrt {2^{n}}}}\bigotimes _{i=0}^{n-1}{\Big (}|0\rangle +(-1)^{\psi _{i}}|1\rangle {\Big )}=H|\psi _{0}\rangle \otimes H|\psi _{1}\rangle \otimes \cdots \otimes H|\psi _{n-1}\rangle$

#### Application on entangled states

If two or more qubits are viewed as a single quantum state, this combined state is equal to the tensor product of the constituent qubits. Any state that can be written as a tensor product from the constituent subsystems are called *separable states*. On the other hand, an *entangled state* is any state that cannot be tensor-factorized, or in other words: *An entangled state can not be written as a tensor product of its constituent qubits states.* Special care must be taken when applying gates to constituent qubits that make up entangled states.

If we have a set of *N* qubits that are entangled and wish to apply a quantum gate on *M* < *N* qubits in the set, we will have to extend the gate to take *N* qubits. This application can be done by combining the gate with an identity matrix such that their tensor product becomes a gate that act on *N* qubits. The identity matrix ( I ) is a representation of the gate that maps every state to itself (i.e., does nothing at all). In a circuit diagram the identity gate or matrix will often appear as just a bare wire.

For example, the Hadamard gate ( H ) acts on a single qubit, but if we feed it the first of the two qubits that constitute the entangled Bell state ${\frac {|00\rangle +|11\rangle }{\sqrt {2}}}$ , we cannot write that operation easily. We need to extend the Hadamard gate H with the identity gate I so that we can act on quantum states that span *two* qubits:

$K=H\otimes I={\frac {1}{\sqrt {2}}}{\begin{bmatrix}1&1\\1&-1\end{bmatrix}}\otimes {\begin{bmatrix}1&0\\0&1\end{bmatrix}}={\frac {1}{\sqrt {2}}}{\begin{bmatrix}1&0&1&0\\0&1&0&1\\1&0&-1&0\\0&1&0&-1\end{bmatrix}}$

The gate K can now be applied to any two-qubit state, entangled or otherwise. The gate K will leave the second qubit untouched and apply the Hadamard transform to the first qubit. If applied to the Bell state in our example, we may write that as:

$K{\frac {|00\rangle +|11\rangle }{\sqrt {2}}}={\frac {1}{\sqrt {2}}}{\begin{bmatrix}1&0&1&0\\0&1&0&1\\1&0&-1&0\\0&1&0&-1\end{bmatrix}}{\frac {1}{\sqrt {2}}}{\begin{bmatrix}1\\0\\0\\1\end{bmatrix}}={\frac {1}{2}}{\begin{bmatrix}1\\1\\1\\-1\end{bmatrix}}={\frac {|00\rangle +|01\rangle +|10\rangle -|11\rangle }{2}}$

#### Computational complexity and the tensor product

The time complexity for multiplying two $n\times n$ -matrices is at least $\Omega (n^{2}\log n)$ , if using a classical machine. Because the size of a gate that operates on q qubits is $2^{q}\times 2^{q}$ it means that the time for simulating a step in a quantum circuit (by means of multiplying the gates) that operates on generic entangled states is $\Omega ({2^{q}}^{2}\log({2^{q}}))$ . For this reason it is believed to be intractable to simulate large entangled quantum systems using classical computers. Subsets of the gates, such as the Clifford gates, or the trivial case of circuits that only implement classical Boolean functions (e.g. combinations of X, CNOT, Toffoli), can however be efficiently simulated on classical computers.

The state vector of a quantum register with n qubits is $2^{n}$ complex entries. Storing the probability amplitudes as a list of floating point values is not tractable for large n .

### Unitary inversion of gates

Because all quantum logical gates are reversible, any composition of multiple gates is also reversible. All products and tensor products (i.e. series and parallel combinations) of unitary matrices are also unitary matrices. This means that it is possible to construct an inverse of all algorithms and functions, as long as they contain only gates.

Initialization, measurement, I/O and spontaneous decoherence are side effects in quantum computers. Gates however are purely functional and bijective.

If U is a unitary matrix, then $U^{\dagger }U=UU^{\dagger }=I$ and $U^{\dagger }=U^{-1}$ . The dagger ( $\dagger$ ) denotes the conjugate transpose. It is also called the Hermitian adjoint.

If a function F is a product of m gates, $F=A_{1}\cdot A_{2}\cdot \dots \cdot A_{m}$ , the unitary inverse of the function $F^{\dagger }$ can be constructed:

Because $(UV)^{\dagger }=V^{\dagger }U^{\dagger }$ we have, after repeated application on itself

$F^{\dagger }=\left(\prod _{i=1}^{m}A_{i}\right)^{\dagger }=\prod _{i=m}^{1}A_{i}^{\dagger }=A_{m}^{\dagger }\cdot \dots \cdot A_{2}^{\dagger }\cdot A_{1}^{\dagger }$

Similarly if the function G consists of two gates A and B in parallel, then $G=A\otimes B$ and $G^{\dagger }=(A\otimes B)^{\dagger }=A^{\dagger }\otimes B^{\dagger }$ .

Gates that are their own unitary inverses are called Hermitian or self-adjoint operators. Some elementary gates such as the Hadamard (*H*) and the Pauli gates (*I*, *X*, *Y*, *Z*) are Hermitian operators, while others like the phase shift (*S*, *T*, *P*, CPhase) gates generally are not.

For example, an algorithm for addition can be used for subtraction, if it is being "run in reverse", as its unitary inverse. The inverse quantum Fourier transform is the unitary inverse. Unitary inverses can also be used for uncomputation. Programming languages for quantum computers, such as Microsoft's Q#, Bernhard Ömer's QCL, and IBM's Qiskit, contain function inversion as programming concepts.

## Measurement

Measurement (sometimes called *observation*) is irreversible and therefore not a quantum gate, because it assigns the observed quantum state to a single value. Measurement takes a quantum state and projects it to one of the basis vectors, with a likelihood equal to the square of the vector's length (in the 2-norm) along that basis vector. This is known as the Born rule and appears as a stochastic non-reversible operation as it probabilistically sets the quantum state equal to the basis vector that represents the measured state. At the instant of measurement, the state is said to "collapse" to the definite single value that was measured. Why and how, or even if the quantum state collapses at measurement, is called the measurement problem.

The probability of measuring a value with probability amplitude $\phi$ is $1\geq |\phi |^{2}\geq 0$ , where $|\cdot |$ is the modulus.

Measuring a single qubit, whose quantum state is represented by the vector $a|0\rangle +b|1\rangle ={\begin{bmatrix}a\\b\end{bmatrix}}$ , will result in $|0\rangle$ with probability $|a|^{2}$ , and in $|1\rangle$ with probability $|b|^{2}$ .

For example, measuring a qubit with the quantum state ${\frac {|0\rangle -i|1\rangle }{\sqrt {2}}}={\frac {1}{\sqrt {2}}}{\begin{bmatrix}1\\-i\end{bmatrix}}$ will yield with equal probability either $|0\rangle$ or $|1\rangle$ .

A quantum state $|\Psi \rangle$ that spans n qubits can be written as a vector in $2^{n}$ complex dimensions: $|\Psi \rangle \in \mathbb {C} ^{2^{n}}$ . This is because the tensor product of n qubits is a vector in $2^{n}$ dimensions. This way, a register of n qubits can be measured to $2^{n}$ distinct states, similar to how a register of n classical bits can hold $2^{n}$ distinct states. Unlike with the bits of classical computers, quantum states can have non-zero probability amplitudes in multiple measurable values simultaneously. This is called *superposition*.

The sum of all probabilities for all outcomes must always be equal to 1. Another way to say this is that the Pythagorean theorem generalized to $\mathbb {C} ^{2^{n}}$ has that all quantum states $|\Psi \rangle$ with n qubits must satisfy ${\textstyle 1=\sum _{x=0}^{2^{n}-1}|a_{x}|^{2},}$ where $a_{x}$ is the probability amplitude for measurable state $|x\rangle$ . A geometric interpretation of this is that the possible value-space of a quantum state $|\Psi \rangle$ with n qubits is the surface of the unit sphere in $\mathbb {C} ^{2^{n}}$ and that the unitary transforms (i.e. quantum logic gates) applied to it are rotations on the sphere. The rotations that the gates perform form the symmetry group U(2n). Measurement is then a probabilistic projection of the points at the surface of this complex sphere onto the basis vectors that span the space (and labels the outcomes).

In many cases the space is represented as a Hilbert space ${\mathcal {H}}$ rather than some specific $2^{n}$ -dimensional complex space. The number of dimensions (defined by the basis vectors, and thus also the possible outcomes from measurement) is then often implied by the operands, for example as the required state space for solving a problem. In Grover's algorithm, Grover named this generic basis vector set *"the database"*.

The selection of basis vectors against which to measure a quantum state will influence the outcome of the measurement. See change of basis and Von Neumann entropy for details. In this article, we always use the *computational basis*, which means that we have labeled the $2^{n}$ basis vectors of an n-qubit register $|0\rangle ,|1\rangle ,|2\rangle ,\cdots ,|2^{n}-1\rangle$ , or use the binary representation $|0_{10}\rangle =|0\dots 00_{2}\rangle ,|1_{10}\rangle =|0\dots 01_{2}\rangle ,|2_{10}\rangle =|0\dots 10_{2}\rangle ,\cdots ,|2^{n}-1\rangle =|111\dots 1_{2}\rangle$ .

In quantum mechanics, the basis vectors constitute an orthonormal basis.

An example of usage of an alternative measurement basis is in the BB84 cipher.

### The effect of measurement on entangled states

If two quantum states (i.e. qubits, or registers) are entangled (meaning that their combined state cannot be expressed as a tensor product), measurement of one register affects or reveals the state of the other register by partially or entirely collapsing its state too. This effect can be used for computation, and is used in many algorithms.

The Hadamard-CNOT combination acts on the zero-state as follows:

$\operatorname {CNOT} (H\otimes I)|00\rangle =\left({\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{bmatrix}}\left({\frac {1}{\sqrt {2}}}{\begin{bmatrix}1&1\\1&-1\end{bmatrix}}\otimes {\begin{bmatrix}1&0\\0&1\end{bmatrix}}\right)\right){\begin{bmatrix}1\\0\\0\\0\end{bmatrix}}={\frac {1}{\sqrt {2}}}{\begin{bmatrix}1\\0\\0\\1\end{bmatrix}}={\frac {|00\rangle +|11\rangle }{\sqrt {2}}}$

This resulting state is the Bell state ${\frac {|00\rangle +|11\rangle }{\sqrt {2}}}={\frac {1}{\sqrt {2}}}{\begin{bmatrix}1\\0\\0\\1\end{bmatrix}}$ . It cannot be described as a tensor product of two qubits. There is no solution for

${\begin{bmatrix}x\\y\end{bmatrix}}\otimes {\begin{bmatrix}w\\z\end{bmatrix}}={\begin{bmatrix}xw\\xz\\yw\\yz\end{bmatrix}}={\frac {1}{\sqrt {2}}}{\begin{bmatrix}1\\0\\0\\1\end{bmatrix}},$

because for example w needs to be both non-zero and zero in the case of xw and yw.

The quantum state *spans* the two qubits. This is called *entanglement*. Measuring one of the two qubits that make up this Bell state will result in that the other qubit logically must have the same value, both must be the same: Either it will be found in the state $|00\rangle$ , or in the state $|11\rangle$ . If we measure one of the qubits to be for example $|1\rangle$ , then the other qubit must also be $|1\rangle$ , because their combined state *became* $|11\rangle$ . Measurement of one of the qubits collapses the entire quantum state, that span the two qubits.

The GHZ state is a similar entangled quantum state that spans three or more qubits.

This type of value-assignment occurs *instantaneously over any distance* and this has as of 2018 been experimentally verified by QUESS for distances of up to 1200 kilometers. That the phenomena appears to happen instantaneously as opposed to the time it would take to traverse the distance separating the qubits at the speed of light is called the EPR paradox, and it is an open question in physics how to resolve this. Originally it was solved by giving up the assumption of local realism, but other interpretations have also emerged. For more information see the Bell test experiments. The no-communication theorem proves that this phenomenon cannot be used for faster-than-light communication of classical information.

### Measurement on registers with pairwise entangled qubits

Take a register A with n qubits all initialized to $|0\rangle$ , and feed it through a parallel Hadamard gate ${\textstyle H^{\otimes n}}$ . Register A will then enter the state ${\textstyle {\frac {1}{\sqrt {2^{n}}}}\sum _{k=0}^{2^{n}-1}|k\rangle }$ that have equal probability of when measured to be in any of its $2^{n}$ possible states; $|0\rangle$ to $|2^{n}-1\rangle$ . Take a second register B, also with n qubits initialized to $|0\rangle$ and pairwise CNOT its qubits with the qubits in register A, such that for each p the qubits $A_{p}$ and $B_{p}$ forms the state $|A_{p}B_{p}\rangle ={\frac {|00\rangle +|11\rangle }{\sqrt {2}}}$ .

If we now measure the qubits in register A, then register B will be found to contain the same value as A. If we however instead apply a quantum logic gate F on A and then measure, then $|A\rangle =F|B\rangle \iff F^{\dagger }|A\rangle =|B\rangle$ , where $F^{\dagger }$ is the unitary inverse of F.

Because of how unitary inverses of gates act, $F^{\dagger }|A\rangle =F^{-1}(|A\rangle )=|B\rangle$ . For example, say $F(x)=x+3{\pmod {2^{n}}}$ , then $|B\rangle =|A-3{\pmod {2^{n}}}\rangle$ .

The equality will hold no matter in which order measurement is performed (on the registers A or B), assuming that F has run to completion. Measurement can even be randomly and concurrently interleaved qubit by qubit, since the measurements assignment of one qubit will limit the possible value-space from the other entangled qubits.

Even though the equalities holds, the probabilities for measuring the possible outcomes may change as a result of applying F, as may be the intent in a quantum search algorithm.

This effect of value-sharing via entanglement is used in Shor's algorithm, phase estimation and in quantum counting. Using the Fourier transform to amplify the probability amplitudes of the solution states for some problem is a generic method known as "Fourier fishing".

## Logic function synthesis

Functions and routines that only use gates can themselves be described as matrices, just like the smaller gates. The matrix that represents a quantum function acting on q qubits has size $2^{q}\times 2^{q}$ . For example, a function that acts on a "qubyte" (a register of 8 qubits) would be represented by a matrix with $2^{8}\times 2^{8}=256\times 256$ elements.

Unitary transformations that are not in the set of gates natively available at the quantum computer (the primitive gates) can be synthesised, or approximated, by combining the available primitive gates in a circuit. One way to do this is to factor the matrix that encodes the unitary transformation into a product of tensor products (i.e. series and parallel circuits) of the available primitive gates. The group U(2*q*) is the symmetry group for the gates that act on q qubits. Factorization is then the problem of finding a path in U(2*q*) from the generating set of primitive gates. The Solovay–Kitaev theorem shows that given a sufficient set of primitive gates, there exist an efficient approximate for any gate. For the general case with a large number of qubits this direct approach to circuit synthesis is intractable. This puts a limit on how large functions can be brute-force factorized into primitive quantum gates. Typically quantum programs are instead built using relatively small and simple quantum functions, similar to normal classical programming.

Because of the gates unitary nature, all functions must be reversible and always be bijective mappings of input to output. There must always exist a function $F^{-1}$ such that $F^{-1}(F(|\psi \rangle ))=|\psi \rangle$ . Functions that are not invertible can be made invertible by adding ancilla qubits to the input or the output, or both. After the function has run to completion, the ancilla qubits can then either be uncomputed or left untouched. Measuring or otherwise collapsing the quantum state of an ancilla qubit (e.g. by re-initializing the value of it, or by its spontaneous decoherence) that have not been uncomputed may result in errors, as their state may be entangled with the qubits that are still being used in computations.

Logically irreversible operations, for example addition modulo $2^{n}$ of two n -qubit registers *a* and *b*, $F(a,b)=a+b{\pmod {2^{n}}}$ , can be made logically reversible by adding information to the output, so that the input can be computed from the output (i.e. there exists a function $F^{-1}$ ). In our example, this can be done by passing on one of the input registers to the output: $F(|a\rangle \otimes |b\rangle )=|a+b{\pmod {2^{n}}}\rangle \otimes |a\rangle$ . The output can then be used to compute the input (i.e. given the output $a+b$ and a , we can easily find the input; a is given and $(a+b)-a=b$ ) and the function is made bijective.

All Boolean algebraic expressions can be encoded as unitary transforms (quantum logic gates), for example by using combinations of the Pauli-X, CNOT and Toffoli gates. These gates are functionally complete in the Boolean logic domain.

There are many unitary transforms available in the libraries of Q#, QCL, Qiskit, and other quantum programming languages. It also appears in the literature.

For example, $\mathrm {inc} (|x\rangle )=|x+1{\pmod {2^{x_{\text{length}}}}}\rangle$ , where $x_{\text{length}}$ is the number of qubits that constitutes the register x , is implemented as the following in QCL:

```mw
cond qufunct inc(qureg x) { // increment register
  int i;
  for i = #x-1 to 0 step -1 {
    CNot(x[i], x[0::i]);     // apply controlled-not from
  }                          // MSB to LSB
}
```

In QCL, decrement is done by "undoing" increment. The prefix `!` is used to instead run the unitary inverse of the function. `!inc(x)` is the inverse of `inc(x)` and instead performs the operation $\mathrm {inc} ^{\dagger }|x\rangle =\mathrm {inc} ^{-1}(|x\rangle )=|x-1{\pmod {2^{x_{\text{length}}}}}\rangle$ . The `cond` keyword means that the function can be conditional.

In the model of computation used in this article (the quantum circuit model), a classic computer generates the gate composition for the quantum computer, and the quantum computer behaves as a coprocessor that receives instructions from the classical computer about which primitive gates to apply to which qubits. Measurement of quantum registers results in binary values that the classical computer can use in its computations. Quantum algorithms often contain both a classical and a quantum part. Unmeasured I/O (sending qubits to remote computers without collapsing their quantum states) can be used to create networks of quantum computers. Entanglement swapping can then be used to realize distributed algorithms with quantum computers that are not directly connected. Examples of distributed algorithms that only require the use of a handful of quantum logic gates are superdense coding, the quantum Byzantine agreement and the BB84 cipherkey exchange protocol.
