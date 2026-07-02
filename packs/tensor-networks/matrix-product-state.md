---
title: "Matrix product state"
source: https://en.wikipedia.org/wiki/Matrix_product_state
domain: tensor-networks
license: CC-BY-SA-4.0
tags: tensor network, tensor contraction, density matrix renormalization group, penrose graphical notation
fetched: 2026-07-02
---

# Matrix product state

A **matrix product state (MPS)** is a representation of a quantum many-body state. It is at the core of the density matrix renormalization group (DMRG) algorithm.

For a system of N spins of dimension d , the general form of the MPS for periodic boundary conditions (PBC) can be written in the following form:

$|\Psi \rangle =\sum _{\{s\}}\operatorname {Tr} \left[A_{1}^{(s_{1})}A_{2}^{(s_{2})}\cdots A_{N}^{(s_{N})}\right]|s_{1}s_{2}\ldots s_{N}\rangle .$

For open boundary conditions (OBC), $|\Psi \rangle$ takes the form

$|\Psi \rangle =\sum _{\{s\}}A_{1}^{(s_{1})}A_{2}^{(s_{2})}\cdots A_{N}^{(s_{N})}|s_{1}s_{2}\ldots s_{N}\rangle .$

Here $A_{i}^{(s_{i})}$ are the $D_{i}\times D_{i+1}$ matrices ( D is the dimension of the virtual subsystems) and $|s_{i}\rangle$ are the single-site basis states. For periodic boundary conditions, we consider $D_{N+1}=D_{1}$ , and for open boundary conditions $D_{1}=1$ . The parameter D   is related to the entanglement between particles. In particular, if the state is a product state (i.e. not entangled at all), it can be described as a matrix product state with $D=1$ . $\{s_{i}\}$ represents a d -dimensional local space on site $i=1,2,...,N$ . For qubits, $s_{i}\in \{0,1\}$ . For qudits (*d*-level systems), $s_{i}\in \{0,1,\ldots ,d-1\}$ .

For states that are translationally symmetric, we can choose: $A_{1}^{(s)}=A_{2}^{(s)}=\cdots =A_{N}^{(s)}\equiv A^{(s)}.$ In general, every state can be written in the MPS form (with D growing exponentially with the particle number *N*). Note that the MPS decomposition is not unique. MPS are practical when D is small – for example, does not depend on the particle number. Except for a small number of specific cases (some mentioned in the section Examples), such a thing is not possible, though in many cases it serves as a good approximation.

For introductions see, and. In the context of finite automata see. For emphasis placed on the graphical reasoning of tensor networks, see the introduction.

## Wave function as a matrix product state

For a system of N lattice sites each of which has a d -dimensional Hilbert space, the completely general state can be written as

$|\Psi \rangle =\sum _{\{s\}}\psi _{s_{1}...s_{N}}|s_{1}\ldots s_{N}\rangle ,$

where $\psi _{s_{1}...s_{N}}$ is a $d^{N}$ -dimensional tensor. For example, the wave function of the system described by the Heisenberg model is defined by the $2^{N}$ dimensional tensor, whereas for the Hubbard model the rank is $4^{N}$ .

The main idea of the MPS approach is to separate physical degrees of freedom of each site, so that the wave function can be rewritten as the product of N matrices, where each matrix corresponds to one particular site. The whole procedure includes the series of reshaping and singular value decompositions (SVD).

There are three ways to represent wave function as an MPS: left-canonical decomposition, right-canonical decomposition, and mixed-canonical decomposition.

### Left-Canonical decomposition

The decomposition of the $d^{N}$ -dimensional tensor starts with the separation of the very left index, i.e., the first index $s_{1}$ , which describes physical degrees of freedom of the first site. It is performed by reshaping $|\Psi \rangle$ as follows

$|\Psi \rangle =\sum _{\{s\}}\psi _{s_{1},(s_{2}...s_{N})}|s_{1}\ldots s_{N}\rangle .$

In this notation, $s_{1}$ is treated as a row index, $(s_{2}\ldots s_{N})$ as a column index, and the coefficient $\psi _{s_{1},(s_{2}...s_{N})}$ is of dimension $(d\times d^{N-1})$ . The SVD procedure yields

$\psi _{s_{1},(s_{2}...s_{N})}=\sum _{\alpha _{1}}^{r_{1}}U_{s_{1},\alpha _{1}}D_{\alpha _{1},\alpha _{1}}(V^{\dagger })_{\alpha _{1},(s_{2}...s_{N})}=\sum _{\alpha _{1}}^{r_{1}}U_{s_{1},\alpha _{1}}\psi _{\alpha _{1},(s_{2}...s_{N})}=\sum _{\alpha _{1}}^{r_{1}}A_{\alpha _{1}}^{s_{1}}\psi _{\alpha _{1},(s_{2}...s_{N})}.$

In the relation above, matrices D and $V^{\dagger }$ are multiplied and form the matrix $\psi _{\alpha _{1},(s_{2}...s_{N})}$ and $r_{1}\leq d$ . $A_{\alpha _{1}}^{s_{1}}$ stores the information about the first lattice site. It was obtained by decomposing matrix U into d row vectors $A^{s_{1}}$ with entries $A_{\alpha _{1}}^{s_{1}}=U_{s_{1},\alpha _{1}}$ . So, the state vector takes the form

$|\Psi \rangle =\sum _{\{s\}}\sum _{\alpha _{1}}A_{\alpha _{1}}^{s_{1}}\psi _{\alpha _{1},(s_{2}...s_{N})}|s_{1}\ldots s_{N}\rangle .$

The separation of the second site is performed by grouping $s_{2}$ and $\alpha _{1}$ , and representing $\psi _{\alpha _{1},(s_{2}...s_{N})}$ as a matrix $\psi _{(\alpha _{1}s_{2}),(s_{3}...s_{N})}$ of dimension $(r_{1}d\times d^{N-2})$ . The subsequent SVD of $\psi _{(\alpha _{1}s_{2}),(s_{3}...s_{N})}$ can be performed as follows:

$\psi _{(\alpha _{1}s_{2}),(s_{3}...s_{N})}=\sum _{\alpha _{2}}^{r_{2}}U_{(\alpha _{1}s_{2}),\alpha _{2}}D_{\alpha _{2},\alpha _{2}}(V^{\dagger })_{\alpha _{2},(s_{3}...s_{N})}=\sum _{\alpha _{2}}^{r_{2}}A_{\alpha _{1},\alpha _{2}}^{s_{2}}\psi _{\alpha _{2},(s_{3}...s_{N})}$

.

Above we replace U by a set of d matrices of dimension $(r_{1}\times r_{2})$ with entries $A_{\alpha _{1},\alpha _{2}}^{s_{2}}=U_{(\alpha _{1}s_{2}),\alpha _{2}}$ . The dimension of $\psi _{\alpha _{2},(s_{3}...s_{N})}$ is $(r_{2}\times d^{N-2})$ with $r_{2}\leq r_{1}d\leq d^{2}$ . Hence,

$|\Psi \rangle =\sum _{\{s\}}\sum _{\alpha _{1}}A_{\alpha _{1}}^{s_{1}}\psi _{(\alpha _{1}s_{2}),(s_{3}...s_{N})}|s_{1}\ldots s_{N}\rangle =\sum _{\{s\}}\sum _{\alpha _{1},\alpha _{2}}A_{\alpha _{1}}^{s_{1}}A_{\alpha _{1},\alpha _{2}}^{s_{2}}\psi _{\alpha _{2},(s_{3}...s_{N})}|s_{1}\ldots s_{N}\rangle .$

Following the steps described above, the state $|\Psi \rangle$ can be represented as a product of matrices

$|\Psi \rangle =\sum _{\{s\}}\sum _{\alpha _{1},\ldots ,\alpha _{N-1}}A_{\alpha _{1}}^{s_{1}}A_{\alpha _{1},\alpha _{2}}^{s_{2}}\ldots A_{\alpha _{N-2},\alpha _{N-1}}^{s_{N-1}}A_{\alpha _{N-1}}^{s_{N}}|s_{1}\ldots s_{N}\rangle .$

The maximal dimensions of the A -matrices take place in the case of the exact decomposition, i.e., assuming for simplicity that N is even, $(1\times d),(d\times d^{2}),\ldots ,(d^{N/2-1}\times d^{N/2}),(d^{N/2}\times d^{N/2-1}),\ldots ,(d^{2}\times d),(d\times 1)$ going from the first to the last site. However, due to the exponential growth of the matrix dimensions in most of the cases it is impossible to perform the exact decomposition.

The dual MPS is defined by replacing each matrix A with $A^{*}$ :

$\langle \Psi |=\sum \limits _{\{s\}}\sum \limits _{\alpha '_{1},...,\alpha '_{N-1}}A_{\alpha '_{1}}^{*s'_{1}}A_{\alpha '_{1},\alpha '_{2}}^{*s'_{2}}...A_{\alpha '_{N-2},\alpha '_{N-1}}^{*s'_{N-1}}A_{\alpha '_{N-1}}^{*s'_{N}}\langle s'_{1}...s'_{N}|.$

Note that each matrix U in the SVD is a semi-unitary matrix with property $U^{\dagger }U=I$ . This leads to

$\delta _{\alpha _{i},\alpha _{j}}=\sum _{\alpha _{i-1}s_{i}}(U^{\dagger })_{\alpha _{i},(\alpha _{i-1}s_{i})}U_{(\alpha _{i-1}s_{i}),\alpha _{j}}=\sum _{\alpha _{i-1}s_{i}}(A^{s_{i}\dagger })_{\alpha _{i},\alpha _{i-1}}A_{\alpha _{i-1},\alpha _{j}}^{s_{i}}=\sum _{s_{i}}(A^{s_{i}\dagger }A^{s_{i}})_{\alpha _{i},\alpha _{j}}$

.

To be more precise, $\sum _{s_{i}}A^{s_{i}\dagger }A^{s_{i}}=I$ . Since matrices are left-normalized, we call the composition left-canonical.

### Right-Canonical decomposition

Similarly, the decomposition can be started from the very right site. After the separation of the first index, the tensor $\psi _{s_{1}...s_{N}}$ transforms as follows:

$\psi _{s_{1}...s_{N}}=\psi _{(s_{1}...s_{N-1}),s_{N}}=\sum _{\alpha _{N-1}}U_{(s_{1}...s_{N-1}),\alpha _{N-1}}D_{\alpha _{N-1},\alpha _{N-1}}(V^{\dagger })_{\alpha _{N-1},s_{N}}=\sum _{\alpha _{N-1}}\psi _{(s_{1}...s_{N-1}),\alpha _{N-1}}B_{\alpha _{N-1}}^{s_{N}}$

.

The matrix $\psi _{(s_{1}...s_{N-1}),\alpha _{N-1}}$ was obtained by multiplying matrices U and D , and the reshaping of $(V^{\dagger })_{\alpha _{N-1},s_{N}}$ into d column vectors forms $B_{\alpha _{N-1}}^{s_{N}}$ . Performing the series of reshaping and SVD, the state vector takes the form

$|\Psi \rangle =\sum _{\{s\}}\sum _{\alpha _{1},\ldots ,\alpha _{N-1}}B_{\alpha _{1}}^{s_{1}}B_{\alpha _{1},\alpha _{2}}^{s_{2}}\ldots B_{\alpha _{N-2},\alpha _{N-1}}^{s_{N-1}}B_{\alpha _{N-1}}^{s_{N}}|s_{1}\ldots s_{N}\rangle .$

Since each matrix V in the SVD is a semi-unitary matrix with property $V^{\dagger }V=I$ , the B -matrices are right-normalized and obey $\sum _{s_{i}}B^{s_{i}}B^{s_{i}\dagger }=I$ . Hence, the decomposition is called right-canonical.

### Mixed-Canonical decomposition

The decomposition performs from both the right and from the left. Assuming that the left-canonical decomposition was performed for the first n sites, $\psi _{s_{1}...s_{N}}$ can be rewritten as

$\psi _{s_{1}...s_{N}}=\sum _{\alpha _{1},\ldots ,\alpha _{n}}A_{\alpha _{1}}^{s_{1}}A_{\alpha _{1},\alpha _{2}}^{s_{2}}\ldots A_{\alpha _{n-1},\alpha _{n}}^{s_{n}}D_{\alpha _{n},\alpha _{n}}(V^{\dagger })_{\alpha _{n},(s_{n+1}...s_{N})}$

.

In the next step, we reshape $(V^{\dagger })_{\alpha _{n},(s_{n+1}...s_{N})}$ as $\psi _{(\alpha _{n}s_{n+1}...s_{n-1}),s_{N}}$ and proceed with the series of reshaping and SVD from the right up to site $s_{n+1}$ :

${\begin{aligned}\psi _{(\alpha _{n}s_{n+1}...s_{n-1}),s_{N}}=&\sum _{\alpha _{n+1}...\alpha _{N}}U_{(\alpha _{n}s_{n+1}),\alpha _{n+1}}D_{\alpha _{n+1},\alpha _{n+1}}B_{\alpha _{n+1},\alpha _{n+2}}^{s_{n+2}}\ldots B_{\alpha _{N-2},\alpha _{N-1}}^{s_{N-1}}B_{\alpha _{N-1}}^{s_{N}}\\=&\sum _{\alpha _{n+1}...\alpha _{N}}B_{\alpha _{n},\alpha _{n+1}}^{s_{n+1}}B_{\alpha _{n+1},\alpha _{n+2}}^{s_{n+2}}\ldots B_{\alpha _{N-2},\alpha _{N-1}}^{s_{N-1}}B_{\alpha _{N-1}}^{s_{N}}\end{aligned}}$

.

As the result,

$\psi _{s_{1}...s_{N}}=\sum _{\alpha _{1},\ldots ,\alpha _{N}}A_{\alpha _{1}}^{s_{1}}A_{\alpha _{1},\alpha _{2}}^{s_{2}}\ldots A_{\alpha _{n-1},\alpha _{n}}^{s_{n}}D_{\alpha _{n},\alpha _{n}}B_{\alpha _{n},\alpha _{n+1}}^{s_{n+1}}B_{\alpha _{n+1},\alpha _{n+2}}^{s_{n+2}}\ldots B_{\alpha _{N-2},\alpha _{N-1}}^{s_{N-1}}B_{\alpha _{N-1}}^{s_{N}}$

.

## Examples

### Greenberger–Horne–Zeilinger state

Greenberger–Horne–Zeilinger state, which for *N* particles can be written as superposition of *N* zeros and *N* ones

$|\mathrm {GHZ} \rangle ={\frac {|0\rangle ^{\otimes N}+|1\rangle ^{\otimes N}}{\sqrt {2}}}$

can be expressed as a Matrix Product State, up to normalization, with

$A^{(0)}={\begin{bmatrix}1&0\\0&0\end{bmatrix}}\quad A^{(1)}={\begin{bmatrix}0&0\\0&1\end{bmatrix}},$

or equivalently, using notation from:

$A={\begin{bmatrix}|0\rangle &0\\0&|1\rangle \end{bmatrix}}.$

This notation uses matrices with entries being state vectors (instead of complex numbers), and when multiplying matrices using tensor product for its entries (instead of product of two complex numbers). Such matrix is constructed as

$A\equiv |0\rangle A^{(0)}+|1\rangle A^{(1)}+\ldots +|d-1\rangle A^{(d-1)}.$

Note that tensor product is not commutative.

In this particular example, a product of two *A* matrices is:

$AA={\begin{bmatrix}|00\rangle &0\\0&|11\rangle \end{bmatrix}}.$

### W state

W state, i.e., the superposition of all the computational basis states of Hamming weight one.

$|\mathrm {W} \rangle ={\frac {1}{\sqrt {3}}}(|001\rangle +|010\rangle +|100\rangle )$

Even though the state is permutation-symmetric, its simplest MPS representation is not. For example:

$A_{1}={\begin{bmatrix}|0\rangle &0\\|0\rangle &|1\rangle \end{bmatrix}}\quad A_{2}={\begin{bmatrix}|0\rangle &|1\rangle \\0&|0\rangle \end{bmatrix}}\quad A_{3}={\begin{bmatrix}|1\rangle &0\\0&|0\rangle \end{bmatrix}}.$

### AKLT model

The AKLT ground state wavefunction, which is the historical example of MPS approach, corresponds to the choice

$A^{+}={\sqrt {\frac {2}{3}}}\ \sigma ^{+}={\begin{bmatrix}0&{\sqrt {2/3}}\\0&0\end{bmatrix}}$

$A^{0}={\frac {-1}{\sqrt {3}}}\ \sigma ^{z}={\begin{bmatrix}-1/{\sqrt {3}}&0\\0&1/{\sqrt {3}}\end{bmatrix}}$

$A^{-}=-{\sqrt {\frac {2}{3}}}\ \sigma ^{-}={\begin{bmatrix}0&0\\-{\sqrt {2/3}}&0\end{bmatrix}}$

where the $\sigma {\text{'s}}$ are Pauli matrices, or

$A={\frac {1}{\sqrt {3}}}{\begin{bmatrix}-|0\rangle &{\sqrt {2}}|+\rangle \\-{\sqrt {2}}|-\rangle &|0\rangle \end{bmatrix}}.$

### Majumdar–Ghosh model

Majumdar–Ghosh ground state can be written as MPS with

$A={\begin{bmatrix}0&\left|\uparrow \right\rangle &\left|\downarrow \right\rangle \\{\frac {-1}{\sqrt {2}}}\left|\downarrow \right\rangle &0&0\\{\frac {1}{\sqrt {2}}}\left|\uparrow \right\rangle &0&0\end{bmatrix}}.$
