---
title: "Density matrix renormalization group"
source: https://en.wikipedia.org/wiki/Density_matrix_renormalization_group
domain: tensor-networks
license: CC-BY-SA-4.0
tags: tensor network, tensor contraction, density matrix renormalization group, penrose graphical notation
fetched: 2026-07-02
---

# Density matrix renormalization group

The **density matrix renormalization group** (**DMRG**) is a numerical variational technique devised to obtain the low-energy physics of quantum many-body systems with high accuracy. The DMRG algorithm attempts to find the lowest-energy matrix product state wavefunction of a Hamiltonian. It was invented in 1992 by Steven R. White and it is nowadays the most efficient method for 1-dimensional systems.

## History

The first application of the DMRG, by Steven R. White and Reinhard Noack, was to find the spectrum of a 1D tight-binding model, which is the discrete lattice version of a 1D particle in a box; this model had been proposed by Kenneth G. Wilson as a test for any new renormalization group method, because they all happened to fail with this simple problem. The DMRG overcame the problems of previous renormalization group methods by connecting two blocks with the two sites in the middle, rather than just adding a single site to a block at each step, as well as by identifying the most important states to be kept at the end of each step by using eigenvalues of the density matrix, rather than energy eigenvalues. After succeeding with the *toy model*, the DMRG method was tried with success on the quantum Heisenberg model.

## Principle

The main problem of quantum many-body physics is the fact that the Hilbert space grows exponentially with size. In other words if one considers a lattice, with some Hilbert space of dimension d on each site of the lattice, then the total Hilbert space would have dimension $d^{N}$ , where N is the number of sites on the lattice. For example, a spin-1/2 chain of length *L* has 2*L* degrees of freedom. The DMRG is an iterative, variational method that reduces effective degrees of freedom to those most important for a target state. The state one is most often interested in is the ground state.

After a warmup cycle, the method splits the system into two subsystems, or blocks, which need not have equal sizes, and two sites in between. A set of *representative states* has been chosen for the block during the warmup. This set of left blocks + two sites + right blocks is known as the **superblock**. Now a candidate for the ground state of the superblock, which is a reduced version of the full system, may be found. It may have a rather poor accuracy, but the method is iterative and improves with the steps below.

The candidate ground state that has been found is projected into the Hilbert subspace for each block using a density matrix, hence the name. Thus, the *relevant states* for each block are updated.

Now one of the blocks grows at the expense of the other and the procedure is repeated. When the growing block reaches maximum size, the other starts to grow in its place. Each time we return to the original (equal sizes) situation, we say that a *sweep* has been completed. Normally, a few sweeps are enough to get a precision of a part in 1010 for a 1D lattice.

## Implementation guide

A practical implementation of the DMRG algorithm is a lengthy work. A few of the main computational tricks are these:

- Since the size of the renormalized Hamiltonian is usually in the order of a few or tens of thousand while the sought eigenstate is just the ground state, the ground state for the superblock is obtained via iterative algorithm such as the Lanczos algorithm of matrix diagonalization. Another choice is the Arnoldi method, especially when dealing with non-hermitian matrices.
- The Lanczos algorithm usually starts with the best guess of the solution. If no guess is available a random vector is chosen. In DMRG, the ground state obtained in a certain DMRG step, suitably transformed, is a reasonable guess and thus works significantly better than a random starting vector at the next DMRG step.
- In systems with symmetries, we may have conserved quantum numbers, such as total spin in a Heisenberg model. It is convenient to find the ground state within each of the sectors into which the Hilbert space is divided.

## Applications

The DMRG has been successfully applied to get the low energy properties of spin chains: Ising model in a transverse field, Heisenberg model, etc., fermionic systems, such as the Hubbard model, problems with impurities such as the Kondo effect, boson systems, and the physics of quantum dots joined with quantum wires. It has been also extended to work on tree graphs, and has found applications in the study of dendrimers. For 2D systems with one of the dimensions much larger than the other DMRG is also accurate, and has proved useful in the study of ladders.

The method has been extended to study equilibrium statistical physics in 2D, and to analyze non-equilibrium phenomena in 1D.

The DMRG has also been applied to the field of quantum chemistry to study strongly correlated systems.

## Example: Quantum Heisenberg model

Let us consider an "infinite" DMRG algorithm for the $S=1$ antiferromagnetic quantum Heisenberg chain. The recipe can be applied for every translationally invariant one-dimensional lattice.

DMRG is a renormalization-group technique because it offers an efficient truncation of the Hilbert space of one-dimensional quantum systems.

### Starting point

To simulate an infinite chain, start with four sites. The first is the *block site*, the last the *universe-block site* and the remaining are the *added sites*, the right one is added to the universe-block site and the other to the block site.

The Hilbert space for the single site is ${\mathfrak {H}}$ with the base $\{|S,S_{z}\rangle \}\equiv \{|1,1\rangle ,|1,0\rangle ,|1,-1\rangle \}$ . With this base the spin operators are $S_{x}$ , $S_{y}$ and $S_{z}$ for the single site. For every block, the two blocks and the two sites, there is its own Hilbert space ${\mathfrak {H}}_{b}$ , its base $\{|w_{i}\rangle \}$ ( $i:1\dots \dim({\mathfrak {H}}_{b})$ )and its own operators $O_{b}:{\mathfrak {H}}_{b}\rightarrow {\mathfrak {H}}_{b}$ where

- block: ${\mathfrak {H}}_{B}$ , $\{|u_{i}\rangle \}$ , $H_{B}$ , $S_{x_{B}}$ , $S_{y_{B}}$ , $S_{z_{B}}$
- left-site: ${\mathfrak {H}}_{l}$ , $\{|t_{i}\rangle \}$ , $S_{x_{l}}$ , $S_{y_{l}}$ , $S_{z_{l}}$
- right-site: ${\mathfrak {H}}_{r}$ , $\{|s_{i}\rangle \}$ , $S_{x_{r}}$ , $S_{y_{r}}$ , $S_{z_{r}}$
- universe: ${\mathfrak {H}}_{U}$ , $\{|r_{i}\rangle \}$ , $H_{U}$ , $S_{x_{U}}$ , $S_{y_{U}}$ , $S_{z_{U}}$

At the starting point all four Hilbert spaces are equivalent to ${\mathfrak {H}}$ , all spin operators are equivalent to $S_{x}$ , $S_{y}$ and $S_{z}$ and $H_{B}=H_{U}=0$ . In the following iterations, this is only true for the left and right sites.

### Step 1: Form the Hamiltonian matrix for the superblock

The ingredients are the four block operators and the four universe-block operators, which at the first iteration are $3\times 3$ matrices, the three left-site spin operators and the three right-site spin operators, which are always $3\times 3$ matrices. The Hamiltonian matrix of the *superblock* (the chain), which at the first iteration has only four sites, is formed by these operators. In the Heisenberg antiferromagnetic S=1 model the Hamiltonian is:

$\mathbf {H} _{SB}=-J\sum _{\langle i,j\rangle }\mathbf {S} _{x_{i}}\mathbf {S} _{x_{j}}+\mathbf {S} _{y_{i}}\mathbf {S} _{y_{j}}+\mathbf {S} _{z_{i}}\mathbf {S} _{z_{j}}$

These operators live in the superblock state space: ${\mathfrak {H}}_{SB}={\mathfrak {H}}_{B}\otimes {\mathfrak {H}}_{l}\otimes {\mathfrak {H}}_{r}\otimes {\mathfrak {H}}_{U}$ , the base is $\{|f\rangle =|u\rangle \otimes |t\rangle \otimes |s\rangle \otimes |r\rangle \}$ . For example: (convention):

$|1000\dots 0\rangle \equiv |f_{1}\rangle =|u_{1},t_{1},s_{1},r_{1}\rangle \equiv |100,100,100,100\rangle$

$|0100\dots 0\rangle \equiv |f_{2}\rangle =|u_{1},t_{1},s_{1},r_{2}\rangle \equiv |100,100,100,010\rangle$

The Hamiltonian in the *DMRG form* is (we set $J=-1$ ):

$\mathbf {H} _{SB}=\mathbf {H} _{B}+\mathbf {H} _{U}+\sum _{\langle i,j\rangle }\mathbf {S} _{x_{i}}\mathbf {S} _{x_{j}}+\mathbf {S} _{y_{i}}\mathbf {S} _{y_{j}}+\mathbf {S} _{z_{i}}\mathbf {S} _{z_{j}}$

The operators are $(d*3*3*d)\times (d*3*3*d)$ matrices, $d=\dim({\mathfrak {H}}_{B})\equiv \dim({\mathfrak {H}}_{U})$ , for example:

$\langle f|\mathbf {H} _{B}|f'\rangle \equiv \langle u,t,s,r|H_{B}\otimes \mathbb {I} \otimes \mathbb {I} \otimes \mathbb {I} |u',t',s',r'\rangle$

$\mathbf {S} _{x_{B}}\mathbf {S} _{x_{l}}=S_{x_{B}}\mathbb {I} \otimes \mathbb {I} S_{x_{l}}\otimes \mathbb {I} \mathbb {I} \otimes \mathbb {I} \mathbb {I} =S_{x_{B}}\otimes S_{x_{l}}\otimes \mathbb {I} \otimes \mathbb {I}$

### Step 2: Diagonalize the superblock Hamiltonian

At this point you must choose the eigenstate of the Hamiltonian for which some observables is calculated, this is the *target state* . At the beginning you can choose the ground state and use some advanced algorithm to find it, one of these is described in:

- *The Iterative Calculation of a Few of the Lowest Eigenvalues and Corresponding Eigenvectors of Large Real-Symmetric Matrices*, Ernest R. Davidson; Journal of Computational Physics 17, 87-94 (1975)

This step is the most time-consuming part of the algorithm.

If $|\Psi \rangle =\sum \Psi _{i,j,k,w}|u_{i},t_{j},s_{k},r_{w}\rangle$ is the target state, expectation value of various operators can be measured at this point using $|\Psi \rangle$ .

### Step 3: Reduce density matrix

Form the reduced density matrix $\rho$ for the first two block system, the block and the left-site. By definition it is the $(d*3)\times (d*3)$ matrix: $\rho _{i,j;i',j'}\equiv \sum _{k,w}\Psi _{i,j,k,w}\Psi _{i',j',k,w}^{*}$

Diagonalize $\rho$ and form the $m\times (d*3)$ matrix T , which rows are the m eigenvectors associated with the m largest eigenvalues $e_{\alpha }$ of $\rho$ . So T is formed by the most significant eigenstates of the reduced density matrix. You choose m looking to the parameter $P_{m}\equiv \sum _{\alpha =1}^{m}e_{\alpha }$ : $1-P_{m}\cong 0$ .

### Step 4: New block and universe-block operators

Form the $(d*3)\times (d*3)$ matrix representation of operators for the system composite of the block and left-site, and for the system composite of right-site and universe-block, for example:

$H_{B-l}=H_{B}\otimes \mathbb {I} +S_{x_{B}}\otimes S_{x_{l}}+S_{y_{B}}\otimes S_{y_{l}}+S_{z_{B}}\otimes S_{z_{l}}$

$S_{x_{B-l}}=\mathbb {I} \otimes S_{x_{l}}$

$H_{r-U}=\mathbb {I} \otimes H_{U}+S_{x_{r}}\otimes S_{x_{U}}+S_{y_{r}}\otimes S_{y_{U}}+S_{z_{r}}\otimes S_{z_{U}}$

$S_{x_{r-U}}=S_{x_{r}}\otimes \mathbb {I}$

Now, form the $m\times m$ matrix representations of the new block and universe-block operators, form a new block by changing basis with the transformation T , for example: ${\begin{matrix}&H_{B}=TH_{B-l}T^{\dagger }&S_{x_{B}}=TS_{x_{B-l}}T^{\dagger }\end{matrix}}$ At this point the iteration is ended and the algorithm goes back to step 1.

The algorithm stops successfully when the observable converges to some value.

## Matrix product ansatz

The success of the DMRG for 1D systems is related to the fact that it is a variational method within the space of matrix product states (MPS). These are states of the form

$|\Psi \rangle =\sum _{s_{1}\cdots s_{N}}\operatorname {Tr} (A^{s_{1}}\cdots A^{s_{N}})|s_{1}\cdots s_{N}\rangle$

where $s_{1}\cdots s_{N}$ are the values of the e.g. *z*-component of the spin in a spin chain, and the *A**s**i* are matrices of arbitrary dimension *m*. As *m* → ∞, the representation becomes exact.

In quantum chemistry application, $s_{i}$ stands for the four possibilities of the projection of the spin quantum number of the two electrons that can occupy a single orbital, thus $s_{i}=|00\rangle ,|10\rangle ,|01\rangle ,|11\rangle$ , where the first (second) entry of these kets corresponds to the spin-up(down) electron. In quantum chemistry, $A^{s_{1}}$ (for a given $s_{i}$ ) and $A^{s_{N}}$ (for a given $s_{N}$ ) are traditionally chosen to be row and column matrices, respectively. This way, the result of $A^{s_{1}}\ldots A^{s_{N}}$ is a scalar value and the trace operation is unnecessary. N is the number of sites (the orbitals basically) used in the simulation.

The matrices in the MPS ansatz are not unique, one can, for instance, insert $B^{-1}B$ in the middle of $A^{s_{i}}A^{s_{i+1}}$ , then define ${\tilde {A}}^{s_{i}}=A^{s_{i}}B^{-1}$ and ${\tilde {A}}^{s_{i+1}}=BA^{s_{i+1}}$ , and the state will stay unchanged. Such gauge freedom is employed to transform the matrices into a canonical form. Three types of canonical form exist: (1) left-normalized form, when

$\sum _{s_{i}}\left({\tilde {A}}^{s_{i}}\right)^{\dagger }{\tilde {A}}^{s_{i}}=I$

for all i , (2) right-normalized form, when

$\sum _{s_{i}}{\tilde {A}}^{s_{i}}\left({\tilde {A}}^{s_{i}}\right)^{\dagger }=I$

for all i , and (3) mixed-canonical form when both left- and right-normalized matrices exist among the N matrices in the above MPS *ansatz*.

The goal of the DMRG calculation is then to solve for the elements of each of the $A^{s_{i}}$ matrices. The so-called one-site and two-site algorithms have been devised for this purpose. In the one-site algorithm, only one matrix (one site) whose elements are solved for at a time. Two-site just means that two matrices are first contracted (multiplied) into a single matrix, and then its elements are solved. The two-site algorithm is proposed because the one-site algorithm is much more prone to getting trapped at a local minimum. Having the MPS in one of the above canonical forms has the advantage of making the computation more favorable - it leads to the ordinary eigenvalue problem. Without canonicalization, one will be dealing with a generalized eigenvalue problem.

## Extensions

In 2004, the time-evolving block decimation method was developed to implement real-time evolution of matrix product states. The idea is based on the classical simulation of a quantum computer. Subsequently, a new method was devised to compute real-time evolution within the DMRG formalism based on Runge-Kutta.

In recent years, some proposals extending the definition of the matrix product states and DMRG methods to 2D and 3D have been put forward.
