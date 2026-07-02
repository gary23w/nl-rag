---
title: "Second quantization"
source: https://en.wikipedia.org/wiki/Second_quantization
domain: quantum-field-theory
license: CC-BY-SA-4.0
tags: quantum field theory, gauge theory, feynman diagram, path integral formulation
fetched: 2026-07-02
---

# Second quantization

**Second quantization**, also referred to as **occupation number representation**, is a formalism used to describe and analyze quantum many-body systems. In quantum field theory, it is known as canonical quantization, in which the fields (typically as the wave functions of matter) are thought of as field operators, in a manner similar to how the physical quantities (position, momentum, etc.) are thought of as operators in first quantization. The key ideas of this method were introduced in 1927 by Paul Dirac, and were later developed, most notably, by Pascual Jordan and Vladimir Fock. In this approach, the quantum many-body states are represented in the Fock state basis, which are constructed by filling up each single-particle state with a certain number of identical particles. The second quantization formalism introduces the creation and annihilation operators to construct and handle the Fock states, providing useful tools to the study of the quantum many-body theory.

## Quantum many-body states

The starting point of the second quantization formalism is the notion of indistinguishability of particles in quantum mechanics. Unlike in classical mechanics, where each particle is labeled by a distinct position vector $\mathbf {r} _{i}$ and different configurations of the set of $\mathbf {r} _{i}$ s correspond to different many-body states, *in quantum mechanics, the particles are identical, such that exchanging two particles, i.e. $\mathbf {r} _{i}\leftrightarrow \mathbf {r} _{j}$ , does not lead to a different many-body quantum state*. This implies that the quantum many-body wave function must be invariant (up to a phase factor) under the exchange of two particles. According to the statistics of the particles, the many-body wave function can either be symmetric or antisymmetric under the particle exchange:

$\Psi _{\rm {B}}(\cdots ,\mathbf {r} _{i},\cdots ,\mathbf {r} _{j},\cdots )=+\Psi _{\rm {B}}(\cdots ,\mathbf {r} _{j},\cdots ,\mathbf {r} _{i},\cdots )$

if the particles are

bosons

,

$\Psi _{\rm {F}}(\cdots ,\mathbf {r} _{i},\cdots ,\mathbf {r} _{j},\cdots )=-\Psi _{\rm {F}}(\cdots ,\mathbf {r} _{j},\cdots ,\mathbf {r} _{i},\cdots )$

if the particles are

fermions

.

This exchange symmetry property imposes a constraint on the many-body wave function. Each time a particle is added or removed from the many-body system, the wave function must be properly symmetrized or anti-symmetrized to satisfy the symmetry constraint. In the first quantization formalism, this constraint is guaranteed by representing the wave function as linear combination of permanents (for bosons) or determinants (for fermions) of single-particle states. In the second quantization formalism, the issue of symmetrization is automatically taken care of by the creation and annihilation operators, such that its notation can be much simpler.

### First-quantized many-body wave function

Consider a complete set of single-particle wave functions $\psi _{\alpha }(\mathbf {r} )$ labeled by $\alpha$ (which may be a combined index of a number of quantum numbers). The following wave function

$\Psi [\mathbf {r} _{i}]=\prod _{i=1}^{N}\psi _{\alpha _{i}}(\mathbf {r} _{i})\equiv \psi _{\alpha _{1}}\otimes \psi _{\alpha _{2}}\otimes \cdots \otimes \psi _{\alpha _{N}}$

represents an *N*-particle state with the *i*-th particle occupying the single-particle state $|{\alpha _{i}}\rangle$ . In the shorthanded notation, the position argument of the wave function may be omitted, and it is assumed that the *i*-th single-particle wave function describes the state of the *i*-th particle. The wave function $\Psi$ has not been symmetrized or anti-symmetrized, thus in general not qualified as a many-body wave function for identical particles. However, it can be brought to the symmetrized (anti-symmetrized) form by operators ${\mathcal {S}}$ for symmetrizer, and ${\mathcal {A}}$ for antisymmetrizer.

For bosons, the many-body wave function must be symmetrized,

$\Psi _{\rm {B}}[\mathbf {r} _{i}]={\mathcal {N}}{\mathcal {S}}\Psi [\mathbf {r} _{i}]={\mathcal {N}}\sum _{\pi \in S_{N}}\prod _{i=1}^{N}\psi _{\alpha _{\pi (i)}}(\mathbf {r} _{i})={\mathcal {N}}\sum _{\pi \in S_{N}}\psi _{\alpha _{\pi (1)}}\otimes \psi _{\alpha _{\pi (2)}}\otimes \cdots \otimes \psi _{\alpha _{\pi (N)}};$

while for fermions, the many-body wave function must be anti-symmetrized,

$\Psi _{\rm {F}}[\mathbf {r} _{i}]={\mathcal {N}}{\mathcal {A}}\Psi [\mathbf {r} _{i}]={\mathcal {N}}\sum _{\pi \in S_{N}}(-1)^{\pi }\prod _{i=1}^{N}\psi _{\alpha _{\pi (i)}}(\mathbf {r} _{i})={\mathcal {N}}\sum _{\pi \in S_{N}}(-1)^{\pi }\psi _{\alpha _{\pi (1)}}\otimes \psi _{\alpha _{\pi (2)}}\otimes \cdots \otimes \psi _{\alpha _{\pi (N)}}.$

Here $\pi$ is an element in the *N*-body permutation group (or symmetric group) $S_{N}$ , which performs a permutation among the state labels $\alpha _{i}$ , and $(-1)^{\pi }$ denotes the corresponding permutation sign. ${\mathcal {N}}$ is the normalization operator that normalizes the wave function. (It is the operator that applies a suitable numerical normalization factor to the symmetrized tensors of degree *n*; see the next section for its value.)

If one arranges the single-particle wave functions in a matrix U , such that the row-*i* column-*j* matrix element is $U_{ij}=\psi _{\alpha _{j}}(\mathbf {r} _{i})\equiv \langle \mathbf {r} _{i}|\alpha _{j}\rangle$ , then the boson many-body wave function can be simply written as a permanent $\Psi _{\rm {B}}={\mathcal {N}}\operatorname {perm} U$ , and the fermion many-body wave function as a determinant $\Psi _{\rm {F}}={\mathcal {N}}\det U$ (also known as the Slater determinant).

### Second-quantized Fock states

First quantized wave functions involve complicated symmetrization procedures to describe physically realizable many-body states because the language of first quantization is redundant for indistinguishable particles. In the first quantization language, the many-body state is described by answering a series of questions like *"Which particle is in which state?"*. However these are not physical questions, because the particles are identical, and it is impossible to tell which particle is which in the first place. The seemingly different states $\psi _{1}\otimes \psi _{2}$ and $\psi _{2}\otimes \psi _{1}$ are actually redundant names of the same quantum many-body state. So the symmetrization (or anti-symmetrization) must be introduced to eliminate this redundancy in the first quantization description.

In the second quantization language, instead of asking "each particle on which state", one asks *"How many particles are there in each state?"*. Because this description does not refer to the labeling of particles, it contains no redundant information, and hence leads to a precise and simpler description of the quantum many-body state. In this approach, the many-body state is represented in the occupation number basis, and the basis state is labeled by the set of occupation numbers, denoted

$|[n_{\alpha }]\rangle \equiv |n_{1},n_{2},\cdots ,n_{\alpha },\cdots \rangle ,$

meaning that there are $n_{\alpha }$ particles in the single-particle state $|\alpha \rangle$ (or as $\psi _{\alpha }$ ). The occupation numbers sum to the total number of particles, i.e. ${\textstyle \sum _{\alpha }n_{\alpha }=N}$ . For fermions, the occupation number $n_{\alpha }$ can only be 0 or 1, due to the Pauli exclusion principle; while for bosons it can be any non-negative integer

$n_{\alpha }={\begin{cases}0,1&{\text{fermions,}}\\0,1,2,3,...&{\text{bosons.}}\end{cases}}$

The occupation number states $|[n_{\alpha }]\rangle$ are also known as Fock states. All the Fock states form a complete basis of the many-body Hilbert space, or Fock space. Any generic quantum many-body state can be expressed as a linear combination of Fock states.

Note that besides providing a more efficient language, Fock space allows for a variable number of particles. As a Hilbert space, it is isomorphic to the sum of the *n*-particle bosonic or fermionic tensor spaces described in the previous section, including a one-dimensional zero-particle space **C**.

The Fock state with all occupation numbers equal to zero is called the vacuum state, denoted $|0\rangle \equiv |\cdots ,0_{\alpha },\cdots \rangle$ . The Fock state with only one non-zero occupation number is a single-mode Fock state, denoted $|n_{\alpha }\rangle \equiv |\cdots ,0,n_{\alpha },0,\cdots \rangle$ . In terms of the first quantized wave function, the vacuum state is the unit tensor product and can be denoted $|0\rangle =1$ . The single-particle state is reduced to its wave function $|1_{\alpha }\rangle =\psi _{\alpha }$ . Other single-mode many-body (boson) states are just the tensor product of the wave function of that mode, such as $|2_{\alpha }\rangle =\psi _{\alpha }\otimes \psi _{\alpha }$ and $|n_{\alpha }\rangle =\psi _{\alpha }^{\otimes n}$ . For multi-mode Fock states (meaning more than one single-particle state $|\alpha \rangle$ is involved), the corresponding first-quantized wave function will require proper symmetrization according to the particle statistics, e.g. $|1_{1},1_{2}\rangle =(\psi _{1}\psi _{2}+\psi _{2}\psi _{1})/{\sqrt {2}}$ for a boson state, and $|1_{1},1_{2}\rangle =(\psi _{1}\psi _{2}-\psi _{2}\psi _{1})/{\sqrt {2}}$ for a fermion state (the symbol $\otimes$ between $\psi _{1}$ and $\psi _{2}$ is omitted for simplicity). In general, the normalization is found to be ${\textstyle {\sqrt {\frac {1}{N!{\prod _{\alpha }{n_{\alpha }!}}}}}}$ , where *N* is the total number of particles. For fermion, this expression reduces to ${\tfrac {1}{\sqrt {N!}}}$ as $n_{\alpha }$ can only be either zero or one. So the first-quantized wave function corresponding to the Fock state reads

$|[n_{\alpha }]\rangle _{\rm {B}}=\left({\frac {1}{N!\prod _{\alpha }n_{\alpha }!}}\right)^{1/2}{\mathcal {S}}\bigotimes \limits _{\alpha }\psi _{\alpha }^{\otimes n_{\alpha }}$

for bosons and

$|[n_{\alpha }]\rangle _{\rm {F}}={\frac {1}{\sqrt {N!}}}{\mathcal {A}}\bigotimes \limits _{\alpha }\psi _{\alpha }^{\otimes n_{\alpha }}$

for fermions. Note that for fermions, $n_{\alpha }=0,1$ only, so the tensor product above is effectively just a product over all occupied single-particle states.

## Creation and annihilation operators

The creation and annihilation operators are introduced to add or remove a particle from the many-body system. These operators lie at the core of the second quantization formalism, bridging the gap between the first- and the second-quantized states. Applying the creation (annihilation) operator to a first-quantized many-body wave function will insert (delete) a single-particle state from the wave function in a symmetrized way depending on the particle statistics. On the other hand, all the second-quantized Fock states can be constructed by applying the creation operators to the vacuum state repeatedly.

The creation and annihilation operators (for bosons) are originally constructed in the context of the quantum harmonic oscillator as the raising and lowering operators, which are then generalized to the field operators in the quantum field theory. They are fundamental to the quantum many-body theory, in the sense that every many-body operator (including the Hamiltonian of the many-body system and all the physical observables) can be expressed in terms of them.

### Insertion and deletion operation

The creation and annihilation of a particle is implemented by the insertion and deletion of the single-particle state from the first quantized wave function in an either symmetric or anti-symmetric manner. Let $\psi _{\alpha }$ be a single-particle state, let 1 be the tensor identity (it is the generator of the zero-particle space **C** and satisfies $\psi _{\alpha }\equiv 1\otimes \psi _{\alpha }\equiv \psi _{\alpha }\otimes 1$ in the tensor algebra over the fundamental Hilbert space), and let $\Psi =\psi _{\alpha _{1}}\otimes \psi _{\alpha _{2}}\otimes \cdots$ be a generic tensor product state. The insertion $\otimes _{\pm }$ and the deletion $\oslash _{\pm }$ operators are linear operators defined by the following recursive equations

$\psi _{\alpha }\otimes _{\pm }1=\psi _{\alpha },\quad \psi _{\alpha }\otimes _{\pm }(\psi _{\beta }\otimes \Psi )=\psi _{\alpha }\otimes \psi _{\beta }\otimes \Psi \pm \psi _{\beta }\otimes (\psi _{\alpha }\otimes _{\pm }\Psi );$

$\psi _{\alpha }\oslash _{\pm }1=0,\quad \psi _{\alpha }\oslash _{\pm }(\psi _{\beta }\otimes \Psi )=\delta _{\alpha \beta }\Psi \pm \psi _{\beta }\otimes (\psi _{\alpha }\oslash _{\pm }\Psi ).$

Here $\delta _{\alpha \beta }$ is the Kronecker delta symbol, which gives 1 if $\alpha =\beta$ , and 0 otherwise. The subscript $\pm$ of the insertion or deletion operators indicates whether symmetrization (for bosons) or anti-symmetrization (for fermions) is implemented.

### Boson creation and annihilation operators

The boson creation (resp. annihilation) operator is usually denoted as $b_{\alpha }^{\dagger }$ (resp. $b_{\alpha }$ ). The creation operator $b_{\alpha }^{\dagger }$ adds a boson to the single-particle state $|\alpha \rangle$ , and the annihilation operator $b_{\alpha }$ removes a boson from the single-particle state $|\alpha \rangle$ . The creation and annihilation operators are Hermitian conjugate to each other, but neither of them are Hermitian operators ( $b_{\alpha }\neq b_{\alpha }^{\dagger }$ ).

#### Definition

The boson creation (annihilation) operator is a linear operator, whose action on a *N*-particle first-quantized wave function $\Psi$ is defined as

$b_{\alpha }^{\dagger }\Psi ={\frac {1}{\sqrt {N+1}}}\psi _{\alpha }\otimes _{+}\Psi ,$

$b_{\alpha }\Psi ={\frac {1}{\sqrt {N}}}\psi _{\alpha }\oslash _{+}\Psi ,$

where $\psi _{\alpha }\otimes _{+}$ inserts the single-particle state $\psi _{\alpha }$ in $N+1$ possible insertion positions symmetrically, and $\psi _{\alpha }\oslash _{+}$ deletes the single-particle state $\psi _{\alpha }$ from N possible deletion positions symmetrically.

##### Examples

Hereinafter the tensor symbol $\otimes$ between single-particle states is omitted for simplicity. Take the state $|1_{1},1_{2}\rangle =(\psi _{1}\psi _{2}+\psi _{2}\psi _{1})/{\sqrt {2}}$ , create one more boson on the state $\psi _{1}$ ,

${\begin{array}{rl}b_{1}^{\dagger }|1_{1},1_{2}\rangle =&{\frac {1}{\sqrt {2}}}(b_{1}^{\dagger }\psi _{1}\psi _{2}+b_{1}^{\dagger }\psi _{2}\psi _{1})\\=&{\frac {1}{\sqrt {2}}}\left({\frac {1}{\sqrt {3}}}\psi _{1}\otimes _{+}\psi _{1}\psi _{2}+{\frac {1}{\sqrt {3}}}\psi _{1}\otimes _{+}\psi _{2}\psi _{1}\right)\\=&{\frac {1}{\sqrt {2}}}\left({\frac {1}{\sqrt {3}}}(\psi _{1}\psi _{1}\psi _{2}+\psi _{1}\psi _{1}\psi _{2}+\psi _{1}\psi _{2}\psi _{1})+{\frac {1}{\sqrt {3}}}(\psi _{1}\psi _{2}\psi _{1}+\psi _{2}\psi _{1}\psi _{1}+\psi _{2}\psi _{1}\psi _{1})\right)\\=&{\frac {\sqrt {2}}{\sqrt {3}}}(\psi _{1}\psi _{1}\psi _{2}+\psi _{1}\psi _{2}\psi _{1}+\psi _{2}\psi _{1}\psi _{1})\\=&{\sqrt {2}}|2_{1},1_{2}\rangle .\end{array}}$

Then annihilate one boson from the state $\psi _{1}$ ,

${\begin{array}{rl}b_{1}|2_{1},1_{2}\rangle =&{\frac {1}{\sqrt {3}}}(b_{1}\psi _{1}\psi _{1}\psi _{2}+b_{1}\psi _{1}\psi _{2}\psi _{1}+b_{1}\psi _{2}\psi _{1}\psi _{1})\\=&{\frac {1}{\sqrt {3}}}\left({\frac {1}{\sqrt {3}}}\psi _{1}\oslash _{+}\psi _{1}\psi _{1}\psi _{2}+{\frac {1}{\sqrt {3}}}\psi _{1}\oslash _{+}\psi _{1}\psi _{2}\psi _{1}+{\frac {1}{\sqrt {3}}}\psi _{1}\oslash _{+}\psi _{2}\psi _{1}\psi _{1}\right)\\=&{\frac {1}{\sqrt {3}}}\left({\frac {1}{\sqrt {3}}}(\psi _{1}\psi _{2}+\psi _{1}\psi _{2}+0)+{\frac {1}{\sqrt {3}}}(\psi _{2}\psi _{1}+0+\psi _{1}\psi _{2})+{\frac {1}{\sqrt {3}}}(0+\psi _{2}\psi _{1}+\psi _{2}\psi _{1})\right)\\=&\psi _{1}\psi _{2}+\psi _{2}\psi _{1}\\=&{\sqrt {2}}|1_{1},1_{2}\rangle .\end{array}}$

#### Action on Fock states

Starting from the single-mode vacuum state $|0_{\alpha }\rangle =1$ , applying the creation operator $b_{\alpha }^{\dagger }$ repeatedly, one finds

$b_{\alpha }^{\dagger }|0_{\alpha }\rangle =\psi _{\alpha }\otimes _{+}1=\psi _{\alpha }=|1_{\alpha }\rangle ,$

$b_{\alpha }^{\dagger }|n_{\alpha }\rangle ={\frac {1}{\sqrt {n_{\alpha }+1}}}\psi _{\alpha }\otimes _{+}\psi _{\alpha }^{\otimes n_{\alpha }}={\sqrt {n_{\alpha }+1}}\psi _{\alpha }^{\otimes (n_{\alpha }+1)}={\sqrt {n_{\alpha }+1}}|n_{\alpha }+1\rangle .$

The creation operator raises the boson occupation number by 1. Therefore, all the occupation number states can be constructed by the boson creation operator from the vacuum state

$|n_{\alpha }\rangle ={\frac {1}{\sqrt {n_{\alpha }!}}}(b_{\alpha }^{\dagger })^{n_{\alpha }}|0_{\alpha }\rangle .$

On the other hand, the annihilation operator $b_{\alpha }$ lowers the boson occupation number by 1

$b_{\alpha }|n_{\alpha }\rangle ={\frac {1}{\sqrt {n_{\alpha }}}}\psi _{\alpha }\oslash _{+}\psi _{\alpha }^{\otimes n_{\alpha }}={\sqrt {n_{\alpha }}}\psi _{\alpha }^{\otimes (n_{\alpha }-1)}={\sqrt {n_{\alpha }}}|n_{\alpha }-1\rangle .$

It will also quench the vacuum state $b_{\alpha }|0_{\alpha }\rangle =0$ as there has been no boson left in the vacuum state to be annihilated. Using the above formulae, it can be shown that

$b_{\alpha }^{\dagger }b_{\alpha }|n_{\alpha }\rangle =n_{\alpha }|n_{\alpha }\rangle ,$

meaning that ${\hat {n}}_{\alpha }=b_{\alpha }^{\dagger }b_{\alpha }$ defines the boson number operator.

The above result can be generalized to any Fock state of bosons.

$b_{\alpha }^{\dagger }|\cdots ,n_{\beta },n_{\alpha },n_{\gamma },\cdots \rangle ={\sqrt {n_{\alpha }+1}}|\cdots ,n_{\beta },n_{\alpha }+1,n_{\gamma },\cdots \rangle .$

$b_{\alpha }|\cdots ,n_{\beta },n_{\alpha },n_{\gamma },\cdots \rangle ={\sqrt {n_{\alpha }}}|\cdots ,n_{\beta },n_{\alpha }-1,n_{\gamma },\cdots \rangle .$

These two equations can be considered as the defining properties of boson creation and annihilation operators in the second-quantization formalism. The complicated symmetrization of the underlying first-quantized wave function is automatically taken care of by the creation and annihilation operators (when acting on the first-quantized wave function), so that the complexity is not revealed on the second-quantized level, and the second-quantization formulae are simple and neat.

#### Operator identities

The following operator identities follow from the action of the boson creation and annihilation operators on the Fock state,

$[b_{\alpha }^{\dagger },b_{\beta }^{\dagger }]=[b_{\alpha },b_{\beta }]=0,\quad [b_{\alpha },b_{\beta }^{\dagger }]=\delta _{\alpha \beta }.$

These commutation relations can be considered as the algebraic definition of the boson creation and annihilation operators. The fact that the boson many-body wave function is symmetric under particle exchange is also manifested by the commutation of the boson operators.

The raising and lowering operators of the quantum harmonic oscillator also satisfy the same set of commutation relations, implying that the bosons can be interpreted as the energy quanta (phonons) of an oscillator. The position and momentum operators of a Harmonic oscillator (or a collection of Harmonic oscillating modes) are given by Hermitian combinations of phonon creation and annihilation operators,

$x_{\alpha }=(b_{\alpha }+b_{\alpha }^{\dagger })/{\sqrt {2}},\quad p_{\alpha }=(b_{\alpha }-b_{\alpha }^{\dagger })/({\sqrt {2}}\mathrm {i} ),$

which reproduce the canonical commutation relation between position and momentum operators (with $\hbar =1$ )

$[x_{\alpha },p_{\beta }]=\mathrm {i} \delta _{\alpha \beta },\quad [x_{\alpha },x_{\beta }]=[p_{\alpha },p_{\beta }]=0.$

This idea is generalized in the quantum field theory, which considers each mode of the matter field as an oscillator subject to quantum fluctuations, and the bosons are treated as the excitations (or energy quanta) of the field.

### Fermion creation and annihilation operators

The fermion creation (annihilation) operator is usually denoted as $c_{\alpha }^{\dagger }$ ( $c_{\alpha }$ ). The creation operator $c_{\alpha }^{\dagger }$ adds a fermion to the single-particle state $|\alpha \rangle$ , and the annihilation operator $c_{\alpha }$ removes a fermion from the single-particle state $|\alpha \rangle$ .

#### Definition

The fermion creation (annihilation) operator is a linear operator, whose action on a *N*-particle first-quantized wave function $\Psi$ is defined as

$c_{\alpha }^{\dagger }\Psi ={\frac {1}{\sqrt {N+1}}}\psi _{\alpha }\otimes _{-}\Psi ,$

$c_{\alpha }\Psi ={\frac {1}{\sqrt {N}}}\psi _{\alpha }\oslash _{-}\Psi ,$

where $\psi _{\alpha }\otimes _{-}$ inserts the single-particle state $\psi _{\alpha }$ in $N+1$ possible insertion positions anti-symmetrically, and $\psi _{\alpha }\oslash _{-}$ deletes the single-particle state $\psi _{\alpha }$ from N possible deletion positions anti-symmetrically.

It is particularly instructive to view the results of creation and annihilation operators on states of two (or more) fermions, because they demonstrate the effects of exchange. A few illustrative operations are given in the example below. The complete algebra for creation and annihilation operators on a two-fermion state can be found in *Quantum Photonics*.

##### Examples

Hereinafter the tensor symbol $\otimes$ between single-particle states is omitted for simplicity. Take the state $|1_{1},1_{2}\rangle =(\psi _{1}\psi _{2}-\psi _{2}\psi _{1})/{\sqrt {2}}$ , attempt to create one more fermion on the occupied $\psi _{1}$ state will quench the whole many-body wave function,

${\begin{array}{rl}c_{1}^{\dagger }|1_{1},1_{2}\rangle =&{\frac {1}{\sqrt {2}}}(c_{1}^{\dagger }\psi _{1}\psi _{2}-c_{1}^{\dagger }\psi _{2}\psi _{1})\\=&{\frac {1}{\sqrt {2}}}\left({\frac {1}{\sqrt {3}}}\psi _{1}\otimes _{-}\psi _{1}\psi _{2}-{\frac {1}{\sqrt {3}}}\psi _{1}\otimes _{-}\psi _{2}\psi _{1}\right)\\=&{\frac {1}{\sqrt {2}}}\left({\frac {1}{\sqrt {3}}}(\psi _{1}\psi _{1}\psi _{2}-\psi _{1}\psi _{1}\psi _{2}+\psi _{1}\psi _{2}\psi _{1})-{\frac {1}{\sqrt {3}}}(\psi _{1}\psi _{2}\psi _{1}-\psi _{2}\psi _{1}\psi _{1}+\psi _{2}\psi _{1}\psi _{1})\right)\\=&0.\end{array}}$

Annihilate a fermion on the $\psi _{2}$ state, take the state $|1_{1},1_{2}\rangle =(\psi _{1}\psi _{2}-\psi _{2}\psi _{1})/{\sqrt {2}}$ ,

${\begin{array}{rl}c_{2}|1_{1},1_{2}\rangle =&{\frac {1}{\sqrt {2}}}(c_{2}\psi _{1}\psi _{2}-c_{2}\psi _{2}\psi _{1})\\=&{\frac {1}{\sqrt {2}}}\left({\frac {1}{\sqrt {2}}}\psi _{2}\oslash _{-}\psi _{1}\psi _{2}-{\frac {1}{\sqrt {2}}}\psi _{2}\oslash _{-}\psi _{2}\psi _{1}\right)\\=&{\frac {1}{\sqrt {2}}}\left({\frac {1}{\sqrt {2}}}(0-\psi _{1})-{\frac {1}{\sqrt {2}}}(\psi _{1}-0)\right)\\=&-\psi _{1}\\=&-|1_{1},0_{2}\rangle .\end{array}}$

The minus sign (known as the fermion sign) appears due to the anti-symmetric property of the fermion wave function.

#### Action on Fock states

Starting from the single-mode vacuum state $|0_{\alpha }\rangle =1$ , applying the fermion creation operator $c_{\alpha }^{\dagger }$ ,

$c_{\alpha }^{\dagger }|0_{\alpha }\rangle =\psi _{\alpha }\otimes _{-}1=\psi _{\alpha }=|1_{\alpha }\rangle ,$

$c_{\alpha }^{\dagger }|1_{\alpha }\rangle ={\frac {1}{\sqrt {2}}}\psi _{\alpha }\otimes _{-}\psi _{\alpha }=0.$

If the single-particle state $|\alpha \rangle$ is empty, the creation operator will fill the state with a fermion. However, if the state is already occupied by a fermion, further application of the creation operator will quench the state, demonstrating the Pauli exclusion principle that two identical fermions can not occupy the same state simultaneously. Nevertheless, the fermion can be removed from the occupied state by the fermion annihilation operator $c_{\alpha }$ ,

$c_{\alpha }|1_{\alpha }\rangle =\psi _{\alpha }\oslash _{-}\psi _{\alpha }=1=|0_{\alpha }\rangle ,$

$c_{\alpha }|0_{\alpha }\rangle =0.$

The vacuum state is quenched by the action of the annihilation operator.

Similar to the boson case, the fermion Fock state can be constructed from the vacuum state using the fermion creation operator

$|n_{\alpha }\rangle =(c_{\alpha }^{\dagger })^{n_{\alpha }}|0_{\alpha }\rangle .$

It is easy to check (by enumeration) that

$c_{\alpha }^{\dagger }c_{\alpha }|n_{\alpha }\rangle =n_{\alpha }|n_{\alpha }\rangle ,$

meaning that ${\hat {n}}_{\alpha }=c_{\alpha }^{\dagger }c_{\alpha }$ defines the fermion number operator.

The above result can be generalized to any Fock state of fermions.

$c_{\alpha }^{\dagger }|\cdots ,n_{\beta },n_{\alpha },n_{\gamma },\cdots \rangle =(-1)^{\sum _{\beta <\alpha }n_{\beta }}{\sqrt {1-n_{\alpha }}}|\cdots ,n_{\beta },1+n_{\alpha },n_{\gamma },\cdots \rangle .$

$c_{\alpha }|\cdots ,n_{\beta },n_{\alpha },n_{\gamma },\cdots \rangle =(-1)^{\sum _{\beta <\alpha }n_{\beta }}{\sqrt {n_{\alpha }}}|\cdots ,n_{\beta },1-n_{\alpha },n_{\gamma },\cdots \rangle .$

Recall that the occupation number $n_{\alpha }$ can only take 0 or 1 for fermions. These two equations can be considered as the defining properties of fermion creation and annihilation operators in the second quantization formalism. Note that the fermion sign structure $(-1)^{\sum _{\beta <\alpha }n_{\beta }}$ , also known as the Jordan-Wigner string, requires there to exist a predefined ordering of the single-particle states (the spin structure) and involves a counting of the fermion occupation numbers of all the preceding states; therefore the fermion creation and annihilation operators are considered non-local in some sense. This observation leads to the idea that fermions are emergent particles in the long-range entangled local qubit system.

#### Operator identities

The following operator identities follow from the action of the fermion creation and annihilation operators on the Fock state,

$\{c_{\alpha }^{\dagger },c_{\beta }^{\dagger }\}=\{c_{\alpha },c_{\beta }\}=0,\quad \{c_{\alpha },c_{\beta }^{\dagger }\}=\delta _{\alpha \beta }.$

These anti-commutation relations can be considered as the algebraic definition of the fermion creation and annihilation operators. The fact that the fermion many-body wave function is anti-symmetric under particle exchange is also manifested by the anti-commutation of the fermion operators.

The creation and annihilation operators are Hermitian conjugate to each other, but neither of them are Hermitian operators ( $c_{\alpha }\neq c_{\alpha }^{\dagger }$ ). The Hermitian combination of the fermion creation and annihilation operators

$\chi _{\alpha ,{\text{Re}}}=(c_{\alpha }+c_{\alpha }^{\dagger })/{\sqrt {2}},\quad \chi _{\alpha ,{\text{Im}}}=(c_{\alpha }-c_{\alpha }^{\dagger })/({\sqrt {2}}\mathrm {i} ),$

are called Majorana fermion operators. They can be viewed as the fermionic analog of position and momentum operators of a "fermionic" Harmonic oscillator. They satisfy the anticommutation relation

$\{\chi _{i},\chi _{j}\}=\delta _{ij},$

where $i,j$ labels any Majorana fermion operators on equal footing (regardless their origin from Re or Im combination of complex fermion operators $c_{\alpha }$ ). The anticommutation relation indicates that Majorana fermion operators generates a Clifford algebra, which can be systematically represented as Pauli operators in the many-body Hilbert space.

## Quantum field operators

Defining $a_{\nu }^{\dagger }$ as a general annihilation (creation) operator for a single-particle state $\nu$ that could be either fermionic $(c_{\nu }^{\dagger })$ or bosonic $(b_{\nu }^{\dagger })$ , the real space representation of the operators defines the quantum field operators $\Psi (\mathbf {r} )$ and $\Psi ^{\dagger }(\mathbf {r} )$ by

$\Psi (\mathbf {r} )=\sum _{\nu }\psi _{\nu }\left(\mathbf {r} \right)a_{\nu }$

$\Psi ^{\dagger }(\mathbf {r} )=\sum _{\nu }\psi _{\nu }^{*}\left(\mathbf {r} \right)a_{\nu }^{\dagger }$

These are second quantization operators, with coefficients $\psi _{\nu }\left(\mathbf {r} \right)$ and $\psi _{\nu }^{*}\left(\mathbf {r} \right)$ that are ordinary first-quantization wavefunctions. Thus, for example, any expectation values will be ordinary first-quantization wavefunctions. Loosely speaking, $\Psi ^{\dagger }(\mathbf {r} )$ is the sum of all possible ways to add a particle to the system at position **r** through any of the basis states $\psi _{\nu }\left(\mathbf {r} \right)$ , not necessarily plane waves, as below.

Since $\Psi (\mathbf {r} )$ and $\Psi ^{\dagger }(\mathbf {r} )$ are second quantization operators defined in every point in space they are called quantum field operators. They obey the following fundamental commutator and anti-commutator relations,

$\left[\Psi (\mathbf {r} _{1}),\Psi ^{\dagger }(\mathbf {r} _{2})\right]=\delta (\mathbf {r} _{1}-\mathbf {r} _{2})$

boson fields,

$\{\Psi (\mathbf {r} _{1}),\Psi ^{\dagger }(\mathbf {r} _{2})\}=\delta (\mathbf {r} _{1}-\mathbf {r} _{2})$

fermion fields.

For homogeneous systems it is often desirable to transform between real space and the momentum representations, hence, the quantum fields operators in Fourier basis yields:

$\Psi (\mathbf {r} )={1 \over {\sqrt {V}}}\sum _{\mathbf {k} }e^{i\mathbf {k\cdot r} }a_{\mathbf {k} }$

$\Psi ^{\dagger }(\mathbf {r} )={1 \over {\sqrt {V}}}\sum _{\mathbf {k} }e^{-i\mathbf {k\cdot r} }a_{\mathbf {k} }^{\dagger }$

The term "second quantization", introduced by Jordan, is a misnomer that has persisted for historical reasons. At the origin of quantum field theory, it was inappositely thought that the Dirac equation described a relativistic wavefunction (hence the obsolete "Dirac sea" interpretation), rather than a classical spinor field which, when quantized (like the scalar field), yielded a fermionic quantum field (vs. a bosonic quantum field).

One is not quantizing "again", as the term "second" might suggest; the field that is being quantized is not a Schrödinger wave function that was produced as the result of quantizing a particle, but is a classical field (such as the electromagnetic field or Dirac spinor field), essentially an assembly of coupled oscillators, that was not previously quantized. One is merely quantizing each oscillator in this assembly, shifting from a semiclassical treatment of the system to a fully quantum-mechanical one.
