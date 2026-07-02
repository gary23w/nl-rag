---
title: "Quantum Fourier transform"
source: https://en.wikipedia.org/wiki/Quantum_Fourier_transform
domain: quantum-algorithms
license: CC-BY-SA-4.0
tags: quantum algorithm, shor's algorithm, grover's algorithm, quantum fourier transform
fetched: 2026-07-02
---

# Quantum Fourier transform

In quantum computing, the **quantum Fourier transform (QFT)** is a linear transformation on quantum bits, and is the quantum analogue of the discrete Fourier transform. The quantum Fourier transform is a part of many quantum algorithms, notably Shor's algorithm for factoring and computing the discrete logarithm, the quantum phase estimation algorithm for estimating the eigenvalues of a unitary operator, and algorithms for the hidden subgroup problem. The quantum Fourier transform was discovered by Don Coppersmith. With small modifications to the QFT, it can also be used for performing fast integer arithmetic operations such as addition and multiplication.

The quantum Fourier transform can be performed efficiently on a quantum computer with a decomposition into the product of simpler unitary matrices. The discrete Fourier transform on $2^{n}$ amplitudes can be implemented as a quantum circuit consisting of only $O(n^{2})$ Hadamard gates and controlled phase shift gates, where n is the number of qubits. This can be compared with the classical discrete Fourier transform, which takes $O(n2^{n})$ gates (where n is the number of bits), which is exponentially more than $O(n^{2})$ .

The quantum Fourier transform acts on a quantum state vector (a quantum register), and the classical discrete Fourier transform acts on a vector. Both types of vectors can be written as lists of complex numbers. In the classical case, the vector can be represented with e.g. an array of floating-point numbers, and in the quantum case it is a sequence of probability amplitudes for all the possible outcomes upon measurement (the outcomes are the *basis states*, or *eigenstates*). Because measurement collapses the quantum state to a single basis state, not every task that uses the classical Fourier transform can take advantage of the quantum Fourier transform's exponential speedup.

The best quantum Fourier transform algorithms known (as of late 2000) require only $O(n\log n)$ gates to achieve an efficient approximation, provided that a controlled phase gate is implemented as a native operation.

## Definition

The quantum Fourier transform is the classical discrete Fourier transform applied to the vector of amplitudes of a quantum state, which has length $N=2^{n}$ if it is applied to a register of n qubits.

The **classical Fourier transform** acts on a vector $(x_{0},x_{1},\ldots ,x_{N-1})\in \mathbb {C} ^{N}$ and maps it to the vector $(y_{0},y_{1},\ldots ,y_{N-1})\in \mathbb {C} ^{N}$ according to the formula

$y_{k}={\frac {1}{\sqrt {N}}}\sum _{j=0}^{N-1}x_{j}\omega _{N}^{-jk},\quad k=0,1,2,\ldots ,N-1,$

where $\omega _{N}=e^{\frac {2\pi i}{N}}$ is an *N*-th root of unity.

Similarly, the **quantum Fourier transform** acts on a quantum state ${\textstyle |x\rangle =\sum _{j=0}^{N-1}x_{j}|j\rangle }$ and maps it to a quantum state ${\textstyle \sum _{j=0}^{N-1}y_{j}|j\rangle }$ according to the formula

$y_{k}={\frac {1}{\sqrt {N}}}\sum _{j=0}^{N-1}x_{j}\omega _{N}^{jk},\quad k=0,1,2,\ldots ,N-1.$

(Conventions for the sign of the phase factor exponent vary; here the quantum Fourier transform has the same effect as the inverse discrete Fourier transform, and conversely.)

Since $\omega _{N}^{l}$ is a rotation, the **inverse quantum Fourier transform** acts similarly but with

$x_{j}={\frac {1}{\sqrt {N}}}\sum _{k=0}^{N-1}y_{k}\omega _{N}^{-jk},\quad j=0,1,2,\ldots ,N-1,$

In case that $|x\rangle$ is a basis state, the quantum Fourier transform can also be expressed as the map

$\operatorname {QFT$

Equivalently, the quantum Fourier transform can be viewed as a unitary matrix (or quantum gate) acting on quantum state vectors, where the unitary matrix $F_{N}$ is the DFT matrix

$F_{N}={\frac {1}{\sqrt {N}}}{\begin{bmatrix}1&1&1&1&\cdots &1\\1&\omega &\omega ^{2}&\omega ^{3}&\cdots &\omega ^{N-1}\\1&\omega ^{2}&\omega ^{4}&\omega ^{6}&\cdots &\omega ^{2(N-1)}\\1&\omega ^{3}&\omega ^{6}&\omega ^{9}&\cdots &\omega ^{3(N-1)}\\\vdots &\vdots &\vdots &\vdots &\ddots &\vdots \\1&\omega ^{N-1}&\omega ^{2(N-1)}&\omega ^{3(N-1)}&\cdots &\omega ^{(N-1)(N-1)}\end{bmatrix}},$

where $\omega =\omega _{N}$ . For example, in the case of $N=4=2^{2}$ and phase $\omega =i$ the transformation matrix is

$F_{4}={\frac {1}{2}}{\begin{bmatrix}1&1&1&1\\1&i&-1&-i\\1&-1&1&-1\\1&-i&-1&i\end{bmatrix}}$

## Properties

### Unitarity

Most of the properties of the quantum Fourier transform follow from the fact that it is a unitary transformation. This can be checked by performing matrix multiplication and ensuring that the relation $FF^{\dagger }=F^{\dagger }F=I$ holds, where $F^{\dagger }$ is the Hermitian adjoint of F . Alternately, one can check that orthogonal vectors of norm 1 get mapped to orthogonal vectors of norm 1.

From the unitary property it follows that the inverse of the quantum Fourier transform is the Hermitian adjoint of the Fourier matrix, thus $F^{-1}=F^{\dagger }$ . Since there is an efficient quantum circuit implementing the quantum Fourier transform, the circuit can be run in reverse to perform the inverse quantum Fourier transform. Thus both transforms can be efficiently performed on a quantum computer.

## Circuit implementation

The quantum gates used in the circuit of n qubits are the Hadamard gate and the dyadic rational phase gate $R_{k}$ :

$H={\frac {1}{\sqrt {2}}}{\begin{pmatrix}1&1\\1&-1\end{pmatrix}}\qquad {\text{and}}\qquad R_{k}={\begin{pmatrix}1&0\\0&e^{i2\pi /2^{k}}\end{pmatrix}}$

The circuit is composed of H gates and the controlled version of $R_{k}$ :

(Quantum circuit for Quantum-Fourier-Transform with n qubits using the fractional binary notation defined below.)

An orthonormal basis S is composed of basis states

$S=\{|0\rangle ,\ldots ,|2^{n}-1\rangle \}$

These basis states span all possible states of the qubits. As in, each $|x\rangle \in S$ is:

$|x\rangle =|x_{1}x_{2}\ldots x_{n}\rangle =|x_{1}\rangle \otimes |x_{2}\rangle \otimes \cdots \otimes |x_{n}\rangle$

where, with tensor product notation $\otimes$ , $|x_{j}\rangle$ indicates that qubit j is in state $x_{j}$ , with $x_{j}$ either 0 or 1. By convention, the basis state index x is the binary number encoded by the $x_{j}$ , with $x_{1}$ the most significant bit.

The action of the Hadamard gate is $H|x_{j}\rangle =\left({\frac {1}{\sqrt {2}}}\right)\left(|0\rangle +e^{2\pi ix_{j}2^{-1}}|1\rangle \right)$ , where the sign depends on $x_{j}$ .

The quantum Fourier transform can be written as the tensor product of a series of terms:

${\text{QFT}}(|x\rangle )={\frac {1}{\sqrt {N}}}\bigotimes _{j=1}^{n}\left(|0\rangle +\omega _{N}^{x2^{n-j}}|1\rangle \right).$

Using the fractional binary notation

$[0.x_{1}\ldots x_{m}]=\sum _{k=1}^{m}x_{k}2^{-k},$

the action of the quantum Fourier transform can be expressed in a compact manner:

${\text{QFT}}(|x_{1}x_{2}\ldots x_{n}\rangle )={\frac {1}{\sqrt {N}}}\ \left(|0\rangle +e^{2\pi i\,[0.x_{n}]}|1\rangle \right)\otimes \left(|0\rangle +e^{2\pi i\,[0.x_{n-1}x_{n}]}|1\rangle \right)\otimes \cdots \otimes \left(|0\rangle +e^{2\pi i\,[0.x_{1}x_{2}\ldots x_{n}]}|1\rangle \right).$

To obtain this state from the circuit depicted above, a swap operation of the qubits must be performed to reverse their order. At most $n/2$ swaps are required.

Because the discrete Fourier transform, an operation on *n* qubits, can be factored into the tensor product of *n* single-qubit operations, it is easily represented as a quantum circuit (up to an order reversal of the output). Each of those single-qubit operations can be implemented efficiently using one Hadamard gate and a linear number of controlled phase gates. The first term requires one Hadamard gate and $(n-1)$ controlled phase gates, the next term requires one Hadamard gate and $(n-2)$ controlled phase gate, and each following term requires one fewer controlled phase gate. Summing up the number of gates, excluding the ones needed for the output reversal, gives $n+(n-1)+\cdots +1=n(n+1)/2=O(n^{2})$ gates, which is quadratic polynomial in the number of qubits. This value is much smaller than for the classical Fourier transformation.

The circuit-level implementation of the quantum Fourier transform on a linear nearest neighbor architecture has been studied before. The circuit depth is linear in the number of qubits.

## Example

The quantum Fourier transform on three qubits, $F_{8}$ with $n=3,N=8=2^{3}$ , is represented by the following transformation:

${\text{QFT}}:|x\rangle \mapsto {\frac {1}{\sqrt {8}}}\sum _{k=0}^{7}\omega ^{xk}|k\rangle ,$

where $\omega =\omega _{8}$ is an eighth root of unity satisfying $\omega ^{8}=\left(e^{\frac {i2\pi }{8}}\right)^{8}=1$ .

The matrix representation of the Fourier transform on three qubits is:

$F_{8}={\frac {1}{\sqrt {8}}}{\begin{bmatrix}1&1&1&1&1&1&1&1\\1&\omega &\omega ^{2}&\omega ^{3}&\omega ^{4}&\omega ^{5}&\omega ^{6}&\omega ^{7}\\1&\omega ^{2}&\omega ^{4}&\omega ^{6}&1&\omega ^{2}&\omega ^{4}&\omega ^{6}\\1&\omega ^{3}&\omega ^{6}&\omega &\omega ^{4}&\omega ^{7}&\omega ^{2}&\omega ^{5}\\1&\omega ^{4}&1&\omega ^{4}&1&\omega ^{4}&1&\omega ^{4}\\1&\omega ^{5}&\omega ^{2}&\omega ^{7}&\omega ^{4}&\omega &\omega ^{6}&\omega ^{3}\\1&\omega ^{6}&\omega ^{4}&\omega ^{2}&1&\omega ^{6}&\omega ^{4}&\omega ^{2}\\1&\omega ^{7}&\omega ^{6}&\omega ^{5}&\omega ^{4}&\omega ^{3}&\omega ^{2}&\omega \\\end{bmatrix}}.$

The 3-qubit quantum Fourier transform can be rewritten as:

${\text{QFT}}(|x_{1},x_{2},x_{3}\rangle )={\frac {1}{\sqrt {8}}}\ \left(|0\rangle +e^{2\pi i\,[0.x_{3}]}|1\rangle \right)\otimes \left(|0\rangle +e^{2\pi i\,[0.x_{2}x_{3}]}|1\rangle \right)\otimes \left(|0\rangle +e^{2\pi i\,[0.x_{1}x_{2}x_{3}]}|1\rangle \right).$

The following sketch shows the respective circuit for $n=3$ (with reversed order of output qubits with respect to the proper QFT):

(QFT for 3 Qubits)

As calculated above, the number of gates used is $n(n+1)/2$ which is equal to 6 , for $n=3$ .

## Relation to quantum Hadamard transform

Using the generalized Fourier transform on finite (abelian) groups, there are actually two natural ways to define a quantum Fourier transform on an *n*-qubit quantum register. The QFT as defined above is equivalent to the DFT, which considers these n qubits as indexed by the cyclic group $\mathbb {Z} /2^{n}\mathbb {Z}$ . However, it also makes sense to consider the qubits as indexed by the Boolean group $(\mathbb {Z} /2\mathbb {Z} )^{n}$ , and in this case the Fourier transform is the Hadamard transform. This is achieved by applying a Hadamard gate to each of the n qubits in parallel. Shor's algorithm uses both types of Fourier transforms, an initial Hadamard transform as well as a QFT.

## For other groups

The Fourier transform can be formulated for groups other than the cyclic group, and extended to the quantum setting. For example, consider the symmetric group $S_{n}$ . The Fourier transform can be expressed in matrix form

${\mathfrak {F}}_{n}=\sum _{\lambda \in \Lambda _{n}}\sum _{p,q\in {\mathcal {P}}(\lambda )}\sum _{g\in S_{n}}{\sqrt {\frac {d_{\lambda }}{n!}}}[\lambda (g)]_{q,p}|\lambda ,p,q\rangle \langle g|,$

where $[\lambda (g)]_{q,p}$ is the $(q,p)$ element of the matrix representation of $\lambda (g)$ , ${\mathcal {P}}(\lambda )$ is the set of paths from the root node to $\lambda$ in the Bratteli diagram of $S_{n}$ , $\Lambda _{n}$ is the set of representations of $S_{n}$ indexed by Young diagrams, and g is a permutation.

## Over a finite field

The discrete Fourier transform can also be formulated over a finite field $F_{q}$ , and a quantum version can be defined. Consider $N=q=p^{n}$ . Let $\phi :GF(q)\to GF(p)$ be an arbitrary linear map (trace, for example). Then for each $x\in GF(q)$ define

$F_{q,\phi }:|x\rangle \mapsto {\frac {1}{\sqrt {q}}}\sum _{y\in GF(q)}\omega ^{\phi (xy)}|y\rangle$

for $\omega =e^{2\pi i/p}$ and extend $F_{q,\phi }$ linearly.
