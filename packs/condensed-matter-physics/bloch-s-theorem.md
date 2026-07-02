---
title: "Bloch's theorem"
source: https://en.wikipedia.org/wiki/Bloch's_theorem
domain: condensed-matter-physics
license: CC-BY-SA-4.0
tags: condensed matter physics, crystal structure, electronic band structure, fermi surface
fetched: 2026-07-02
---

# Bloch's theorem

In condensed matter physics, **Bloch's theorem** states that solutions to the Schrödinger equation in a periodic potential can be expressed as plane waves modulated by periodic functions. The theorem is named after the Swiss physicist Felix Bloch, who discovered the theorem in 1929. Mathematically, they are written

Bloch function

$\psi (\mathbf {r} )=e^{i\mathbf {k} \cdot \mathbf {r} }u(\mathbf {r} )$

where $\mathbf {r}$ is position, $\psi$ is the wave function, u is a periodic function with the same periodicity as the crystal, the wave vector $\mathbf {k}$ is the crystal momentum vector, e is Euler's number, and i is the imaginary unit.

Functions of this form are known as **Bloch functions** or **Bloch states**, and serve as a suitable basis for the wave functions or states of electrons in crystalline solids.

The description of electrons in terms of Bloch functions, termed **Bloch electrons** (or less often *Bloch Waves*), underlies the concept of electronic band structures.

These eigenstates are written with subscripts as $\psi _{n\mathbf {k} }$ , where n is a discrete index, called the band index, which is present because there are many different wave functions with the same $\mathbf {k}$ (each has a different periodic component u ). Within a band (i.e., for fixed n ), $\psi _{n\mathbf {k} }$ varies continuously with $\mathbf {k}$ , as does its energy. Also, $\psi _{n\mathbf {k} }$ is unique only up to a constant reciprocal lattice vector $\mathbf {K}$ , or, $\psi _{n\mathbf {k} }=\psi _{n(\mathbf {k+K} )}$ . Therefore, the wave vector $\mathbf {k}$ can be restricted to the first Brillouin zone of the reciprocal lattice without loss of generality.

## Applications and consequences

### Applicability

The most common example of Bloch's theorem is describing electrons in a crystal, especially in characterizing the crystal's electronic properties, such as electronic band structure. However, a Bloch-wave description applies more generally to any wave-like phenomenon in a periodic medium. For example, a periodic dielectric structure in electromagnetism leads to photonic crystals, and a periodic acoustic medium leads to phononic crystals. It is generally treated in the various forms of the dynamical theory of diffraction.

### Wave vector

Suppose an electron is in a Bloch state $\psi (\mathbf {r} )=e^{i\mathbf {k} \cdot \mathbf {r} }u(\mathbf {r} ),$ where *u* is periodic with the same periodicity as the crystal lattice. The actual quantum state of the electron is entirely determined by $\psi$ , not **k** or *u* directly. This is important because **k** and *u* are *not* unique. Specifically, if $\psi$ can be written as above using **k**, it can *also* be written using (**k** + **K**), where **K** is any reciprocal lattice vector (see figure at right). Therefore, wave vectors that differ by a reciprocal lattice vector are equivalent, in the sense that they characterize the same set of Bloch states.

The first Brillouin zone is a restricted set of values of **k** with the property that no two of them are equivalent, yet every possible **k** is equivalent to one (and only one) vector in the first Brillouin zone. Therefore, if we restrict **k** to the first Brillouin zone, then every Bloch state has a unique **k**. Therefore, the first Brillouin zone is often used to depict all of the Bloch states without redundancy, for example in a band structure, and it is used for the same reason in many calculations.

When **k** is multiplied by the reduced Planck constant, it equals the electron's crystal momentum. Related to this, the group velocity of an electron can be calculated based on how the energy of a Bloch state varies with **k**; for more details see crystal momentum.

### Detailed example

For a detailed example in which the consequences of Bloch's theorem are worked out in a specific situation, see the article Particle in a one-dimensional lattice (periodic potential).

## Statement

**Bloch's theorem**—For electrons in a perfect crystal, there is a basis of wave functions with the following two properties:

- each of these wave functions is an energy eigenstate,
- each of these wave functions is a Bloch state, meaning that this wave function $\psi$ can be written in the form $\;\psi (\mathbf {r} )=e^{i\mathbf {k} \cdot \mathbf {r} }u(\mathbf {r} ),$ where $u(\mathbf {r} )$ has the same periodicity as the atomic structure of the crystal, such that $u_{\mathbf {k} }(\mathbf {x} )=u_{\mathbf {k} }(\mathbf {x} +\mathbf {n} \cdot \mathbf {a} ).$

A second and equivalent way to state the theorem is the following

**Bloch's theorem**—For any wave function that satisfies the Schrödinger equation and for a translation of a lattice vector $\mathbf {a}$ , there exists at least one vector $\mathbf {k}$ such that: $\psi _{\mathbf {k} }(\mathbf {x} +\mathbf {a} )=e^{i\mathbf {k} \cdot \mathbf {a} }\psi _{\mathbf {k} }(\mathbf {x} ).$

## Proof

### Using lattice periodicity

Bloch's theorem, being a statement about lattice periodicity, all the symmetries in this proof are encoded as translation symmetries of the wave function itself.

Proof Using lattice periodicity

Source:

#### Preliminaries: Crystal symmetries, lattice, and reciprocal lattice

The defining property of a crystal is translational symmetry, which means that if the crystal is shifted an appropriate amount, it winds up with all its atoms in the same places. (A finite-size crystal cannot have perfect translational symmetry, but it is a useful approximation.)

A three-dimensional crystal has three *primitive lattice vectors* **a**1, **a**2, **a**3. If the crystal is shifted by any of these three vectors, or a combination of them of the form $n_{1}\mathbf {a} _{1}+n_{2}\mathbf {a} _{2}+n_{3}\mathbf {a} _{3},$ where ni are three integers, then the atoms end up in the same set of locations as they started.

Another helpful ingredient in the proof is the *reciprocal lattice vectors*. These are three vectors **b**1, **b**2, **b**3 (with units of inverse length), with the property that **a***i* · **b***i* = 2*π*, but **a***i* · **b***j* = 0 when *i* ≠ *j*. (For the formula for **b***i*, see reciprocal lattice vector.)

#### Lemma about translation operators

Let ${\hat {T}}_{n_{1},n_{2},n_{3}}$ denote a translation operator that shifts every wave function by the amount *n*1**a**1 + *n*2**a**2 + *n*3**a**3 (as above, nj are integers). The following fact is helpful for the proof of Bloch's theorem:

**Lemma**—If a wave function ψ is an eigenstate of all of the translation operators (simultaneously), then ψ is a Bloch state.

Proof of Lemma

Assume that we have a wave function ψ which is an eigenstate of all the translation operators. As a special case of this, $\psi (\mathbf {r} +\mathbf {a} _{j})=C_{j}\psi (\mathbf {r} )$ for *j* = 1, 2, 3, where Cj are three numbers (the eigenvalues) which do not depend on **r**. It is helpful to write the numbers Cj in a different form, by choosing three numbers *θ*1, *θ*2, *θ*3 with *e*2*πiθ**j* = *C**j*: $\psi (\mathbf {r} +\mathbf {a} _{j})=e^{2\pi i\theta _{j}}\psi (\mathbf {r} )$ Again, the θj are three numbers which do not depend on **r**. Define **k** = *θ*1**b**1 + *θ*2**b**2 + *θ*3**b**3, where **b***j* are the reciprocal lattice vectors (see above). Finally, define $u(\mathbf {r} )=e^{-i\mathbf {k} \cdot \mathbf {r} }\psi (\mathbf {r} )\,.$ Then ${\begin{aligned}u(\mathbf {r} +\mathbf {a} _{j})&=e^{-i\mathbf {k} \cdot (\mathbf {r} +\mathbf {a} _{j})}\psi (\mathbf {r} +\mathbf {a} _{j})\\&={\big (}e^{-i\mathbf {k} \cdot \mathbf {r} }e^{-i\mathbf {k} \cdot \mathbf {a} _{j}}{\big )}{\big (}e^{2\pi i\theta _{j}}\psi (\mathbf {r} ){\big )}\\&=e^{-i\mathbf {k} \cdot \mathbf {r} }e^{-2\pi i\theta _{j}}e^{2\pi i\theta _{j}}\psi (\mathbf {r} )\\&=u(\mathbf {r} ).\end{aligned}}$ This proves that u has the periodicity of the lattice. Since $\psi (\mathbf {r} )=e^{i\mathbf {k} \cdot \mathbf {r} }u(\mathbf {r} ),$ that proves that the state is a Bloch state.

Finally, we are ready for the main proof of Bloch's theorem which is as follows.

As above, let ${\hat {T}}_{n_{1},n_{2},n_{3}}$ denote a *translation operator* that shifts every wave function by the amount *n*1**a**1 + *n*2**a**2 + *n*3**a**3, where ni are integers. Because the crystal has translational symmetry, this operator commutes with the Hamiltonian operator. Moreover, every such translation operator commutes with every other. Therefore, there is a simultaneous eigenbasis of the Hamiltonian operator and every possible ${\hat {T}}_{n_{1},n_{2},n_{3}}\!$ operator. This basis is what we are looking for. The wave functions in this basis are energy eigenstates (because they are eigenstates of the Hamiltonian), and they are also Bloch states (because they are eigenstates of the translation operators; see Lemma above).

### Using operators

In this proof all the symmetries are encoded as commutation properties of the translation operators

Proof using operators

Source:

We define the translation operator ${\begin{aligned}{\hat {\mathbf {T} }}_{\mathbf {n} }\psi (\mathbf {r} )&=\psi (\mathbf {r} +\mathbf {T} _{\mathbf {n} })\\&=\psi (\mathbf {r} +n_{1}\mathbf {a} _{1}+n_{2}\mathbf {a} _{2}+n_{3}\mathbf {a} _{3})\\&=\psi (\mathbf {r} +\mathbf {A} \mathbf {n} )\end{aligned}}$ with $\mathbf {A} ={\begin{bmatrix}\mathbf {a} _{1}&\mathbf {a} _{2}&\mathbf {a} _{3}\end{bmatrix}},\quad \mathbf {n} ={\begin{pmatrix}n_{1}\\n_{2}\\n_{3}\end{pmatrix}}$ We use the hypothesis of a mean periodic potential $U(\mathbf {x} +\mathbf {T} _{\mathbf {n} })=U(\mathbf {x} )$ and the independent electron approximation with a Hamiltonian ${\hat {H}}={\frac {{\hat {\mathbf {p} }}^{2}}{2m}}+U(\mathbf {x} )$ Given the Hamiltonian is invariant for translations it shall commute with the translation operator $[{\hat {H}},{\hat {\mathbf {T} }}_{\mathbf {n} }]=0$ and the two operators shall have a common set of eigenfunctions. Therefore, we start to look at the eigen-functions of the translation operator: ${\hat {\mathbf {T} }}_{\mathbf {n} }\psi (\mathbf {x} )=\lambda _{\mathbf {n} }\psi (\mathbf {x} )$ Given ${\hat {\mathbf {T} }}_{\mathbf {n} }$ is an additive operator ${\hat {\mathbf {T} }}_{\mathbf {n} _{1}}{\hat {\mathbf {T} }}_{\mathbf {n} _{2}}\psi (\mathbf {x} )=\psi (\mathbf {x} +\mathbf {A} \mathbf {n} _{1}+\mathbf {A} \mathbf {n} _{2})={\hat {\mathbf {T} }}_{\mathbf {n} _{1}+\mathbf {n} _{2}}\psi (\mathbf {x} )$ If we substitute here the eigenvalue equation and dividing both sides for $\psi (\mathbf {x} )$ we have $\lambda _{\mathbf {n} _{1}}\lambda _{\mathbf {n} _{2}}=\lambda _{\mathbf {n} _{1}+\mathbf {n} _{2}}$

This is true for $\lambda _{\mathbf {n} }=e^{s\mathbf {n} \cdot \mathbf {a} }$ where $s\in \mathbb {C}$ if we use the normalization condition over a single primitive cell of volume V $1=\int _{V}|\psi (\mathbf {x} )|^{2}d\mathbf {x} =\int _{V}\left|{\hat {\mathbf {T} }}_{\mathbf {n} }\psi (\mathbf {x} )\right|^{2}d\mathbf {x} =|\lambda _{\mathbf {n} }|^{2}\int _{V}|\psi (\mathbf {x} )|^{2}d\mathbf {x}$ and therefore $1=|\lambda _{\mathbf {n} }|^{2}$ and $s=ik$ where $k\in \mathbb {R}$ . Finally, $\mathbf {{\hat {T}}_{n}} \psi (\mathbf {x} )=\psi (\mathbf {x} +\mathbf {n} \cdot \mathbf {a} )=e^{ik\mathbf {n} \cdot \mathbf {a} }\psi (\mathbf {x} ),$ which is true for a Bloch wave i.e. for $\psi _{\mathbf {k} }(\mathbf {x} )=e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )$ with $u_{\mathbf {k} }(\mathbf {x} )=u_{\mathbf {k} }(\mathbf {x} +\mathbf {A} \mathbf {n} )$

### Using group theory

Apart from the group theory technicalities this proof is interesting because it becomes clear how to generalize the Bloch theorem for groups that are not only translations. This is typically done for space groups which are a combination of a translation and a point group and it is used for computing the band structure, spectrum and specific heats of crystals given a specific crystal group symmetry like FCC or BCC and eventually an extra basis. In this proof it is also possible to notice how it is key that the extra point group is driven by a symmetry in the effective potential but it shall commute with the Hamiltonian.

Proof with character theory

All translations are unitary and abelian. Translations can be written in terms of unit vectors ${\boldsymbol {\tau }}=\sum _{i=1}^{3}n_{i}\mathbf {a} _{i}$ We can think of these as commuting operators ${\hat {\boldsymbol {\tau }}}={\hat {\boldsymbol {\tau }}}_{1}{\hat {\boldsymbol {\tau }}}_{2}{\hat {\boldsymbol {\tau }}}_{3}$ where ${\hat {\boldsymbol {\tau }}}_{i}=n_{i}{\hat {\mathbf {a} }}_{i}$

The commutativity of the ${\hat {\boldsymbol {\tau }}}_{i}$ operators gives three commuting cyclic subgroups (given they can be generated by only one element) which are infinite, 1-dimensional and abelian. All irreducible representations of abelian groups are one dimensional.

Given they are one dimensional the matrix representation and the character are the same. The character is the representation over the complex numbers of the group or also the trace of the representation which in this case is a one dimensional matrix. All these subgroups, given they are cyclic, they have characters which are appropriate roots of unity. In fact they have one generator $\gamma$ which shall obey to $\gamma ^{n}=1$ , and therefore the character $\chi (\gamma )^{n}=1$ . Note that this is straightforward in the finite cyclic group case but in the countable infinite case of the infinite cyclic group (i.e. the translation group here) there is a limit for $n\to \infty$ where the character remains finite.

Given the character is a root of unity, for each subgroup the character can be then written as $\chi _{k_{1}}({\hat {\boldsymbol {\tau }}}_{1}(n_{1},a_{1}))=e^{ik_{1}n_{1}a_{1}}$

If we introduce the Born–von Karman boundary condition on the potential: $V\left(\mathbf {r} +\sum _{i}N_{i}\mathbf {a} _{i}\right)=V(\mathbf {r} +\mathbf {L} )=V(\mathbf {r} )$ where *L* is a macroscopic periodicity in the direction $\mathbf {a}$ that can also be seen as a multiple of $a_{i}$ where ${\textstyle \mathbf {L} =\sum _{i}N_{i}\mathbf {a} _{i}}$

This substituting in the time independent Schrödinger equation with a simple effective Hamiltonian ${\hat {H}}=-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}+V(\mathbf {r} )$ induces a periodicity with the wave function: $\psi \left(\mathbf {r} +\sum _{i}N_{i}\mathbf {a} _{i}\right)=\psi (\mathbf {r} )$

And for each dimension a translation operator with a period *L* ${\hat {P}}_{\varepsilon |\tau _{i}+L_{i}}={\hat {P}}_{\varepsilon |\tau _{i}}$

From here we can see that also the character shall be invariant by a translation of $L_{i}$ : $e^{ik_{1}n_{1}a_{1}}=e^{ik_{1}(n_{1}a_{1}+L_{1})}$ and from the last equation we get for each dimension a periodic condition: $k_{1}n_{1}a_{1}=k_{1}(n_{1}a_{1}+L_{1})-2\pi m_{1}$ where $m_{1}\in \mathbb {Z}$ is an integer and $k_{1}={\frac {2\pi m_{1}}{L_{1}}}$

The wave vector $k_{1}$ identify the irreducible representation in the same manner as $m_{1}$ , and $L_{1}$ is a macroscopic periodic length of the crystal in direction $a_{1}$ . In this context, the wave vector serves as a quantum number for the translation operator.

We can generalize this for 3 dimensions $\chi _{k_{1}}(n_{1},a_{1})\chi _{k_{2}}(n_{2},a_{2})\chi _{k_{3}}(n_{3},a_{3})=e^{i\mathbf {k} \cdot {\boldsymbol {\tau }}}$ and the generic formula for the wave function becomes: ${\hat {P}}_{R}\psi _{j}=\sum _{\alpha }\psi _{\alpha }\chi _{\alpha j}(R)$ i.e. specializing it for a translation ${\hat {P}}_{\varepsilon |{\boldsymbol {\tau }}}\psi (\mathbf {r} )=\psi (\mathbf {r} )e^{i\mathbf {k} \cdot {\boldsymbol {\tau }}}=\psi (\mathbf {r} +{\boldsymbol {\tau }})$ and we have proven Bloch’s theorem.

In the generalized version of the Bloch theorem, the Fourier transform, i.e. the wave function expansion, gets generalized from a discrete Fourier transform which is applicable only for cyclic groups, and therefore translations, into a character expansion of the wave function where the characters are given from the specific finite point group.

Also here is possible to see how the characters (as the invariants of the irreducible representations) can be treated as the fundamental building blocks instead of the irreducible representations themselves.

## Velocity and effective mass

If we apply the time-independent Schrödinger equation to the Bloch wave function we obtain ${\hat {H}}_{\mathbf {k} }u_{\mathbf {k} }(\mathbf {r} )=\left[{\frac {\hbar ^{2}}{2m}}\left(-i\nabla +\mathbf {k} \right)^{2}+U(\mathbf {r} )\right]u_{\mathbf {k} }(\mathbf {r} )=\varepsilon _{\mathbf {k} }u_{\mathbf {k} }(\mathbf {r} )$ with boundary conditions $u_{\mathbf {k} }(\mathbf {r} )=u_{\mathbf {k} }(\mathbf {r} +\mathbf {R} )$ Given this is defined in a finite volume we expect an infinite family of eigenvalues; here ${\mathbf {k} }$ is a parameter of the Hamiltonian and therefore we arrive at a "continuous family" of eigenvalues $\varepsilon _{n}(\mathbf {k} )$ dependent on the continuous parameter ${\mathbf {k} }$ and thus at the basic concept of an electronic band structure.

Proof

$E_{\mathbf {k} }\left(e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )\right)=\left[{\frac {-\hbar ^{2}}{2m}}\nabla ^{2}+U(\mathbf {x} )\right]\left(e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )\right)$

We remain with ${\begin{aligned}E_{\mathbf {k} }e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )&={\frac {-\hbar ^{2}}{2m}}\nabla \cdot \left(i\mathbf {k} e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )+e^{i\mathbf {k} \cdot \mathbf {x} }\nabla u_{\mathbf {k} }(\mathbf {x} )\right)+U(\mathbf {x} )e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )\\[1.2ex]E_{\mathbf {k} }e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )&={\frac {-\hbar ^{2}}{2m}}\left(i\mathbf {k} \cdot \left(i\mathbf {k} e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )+e^{i\mathbf {k} \cdot \mathbf {x} }\nabla u_{\mathbf {k} }(\mathbf {x} )\right)+i\mathbf {k} \cdot e^{i\mathbf {k} \cdot \mathbf {x} }\nabla u_{\mathbf {k} }(\mathbf {x} )+e^{i\mathbf {k} \cdot \mathbf {x} }\nabla ^{2}u_{\mathbf {k} }(\mathbf {x} )\right)+U(\mathbf {x} )e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )\\[1.2ex]E_{\mathbf {k} }e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )&={\frac {\hbar ^{2}}{2m}}\left(\mathbf {k} ^{2}e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )-2i\mathbf {k} \cdot e^{i\mathbf {k} \cdot \mathbf {x} }\nabla u_{\mathbf {k} }(\mathbf {x} )-e^{i\mathbf {k} \cdot \mathbf {x} }\nabla ^{2}u_{\mathbf {k} }(\mathbf {x} )\right)+U(\mathbf {x} )e^{i\mathbf {k} \cdot \mathbf {x} }u_{\mathbf {k} }(\mathbf {x} )\\[1.2ex]E_{\mathbf {k} }u_{\mathbf {k} }(\mathbf {x} )&={\frac {\hbar ^{2}}{2m}}\left(-i\nabla +\mathbf {k} \right)^{2}u_{\mathbf {k} }(\mathbf {x} )+U(\mathbf {x} )u_{\mathbf {k} }(\mathbf {x} )\end{aligned}}$

This shows how the effective momentum can be seen as composed of two parts, ${\hat {\mathbf {p} }}_{\text{eff}}=-i\hbar \nabla +\hbar \mathbf {k} ,$ a standard momentum $-i\hbar \nabla$ and a crystal momentum $\hbar \mathbf {k}$ . More precisely the crystal momentum is not a momentum but it stands for the momentum in the same way as the electromagnetic momentum in the minimal coupling, and as part of a canonical transformation of the momentum.

For the effective velocity we can derive

mean velocity of a Bloch electron

${\frac {\partial \varepsilon _{n}}{\partial \mathbf {k} }}={\frac {\hbar ^{2}}{m}}\int d\mathbf {r} \,\psi _{n\mathbf {k} }^{*}(-i\nabla )\psi _{n\mathbf {k} }={\frac {\hbar }{m}}\langle {\hat {\mathbf {p} }}\rangle =\hbar \langle {\hat {\mathbf {v} }}\rangle$

Proof

We evaluate the derivatives ${\frac {\partial \varepsilon _{n}}{\partial \mathbf {k} }}$ and ${\frac {\partial ^{2}\varepsilon _{n}(\mathbf {k} )}{\partial k_{i}\partial k_{j}}}$ given they are the coefficients of the following expansion in **q** where **q** is considered small with respect to **k** $\varepsilon _{n}(\mathbf {k} +\mathbf {q} )=\varepsilon _{n}(\mathbf {k} )+\sum _{i}{\frac {\partial \varepsilon _{n}}{\partial k_{i}}}q_{i}+{\frac {1}{2}}\sum _{ij}{\frac {\partial ^{2}\varepsilon _{n}}{\partial k_{i}\partial k_{j}}}q_{i}q_{j}+O(q^{3})$ Given $\varepsilon _{n}(\mathbf {k} +\mathbf {q} )$ are eigenvalues of ${\hat {H}}_{\mathbf {k} +\mathbf {q} }$ We can consider the following perturbation problem in q: ${\hat {H}}_{\mathbf {k} +\mathbf {q} }={\hat {H}}_{\mathbf {k} }+{\frac {\hbar ^{2}}{m}}\mathbf {q} \cdot (-i\nabla +\mathbf {k} )+{\frac {\hbar ^{2}}{2m}}q^{2}$ Perturbation theory of the second order states that $E_{n}=E_{n}^{0}+\int d\mathbf {r} \,\psi _{n}^{*}{\hat {V}}\psi _{n}+\sum _{n'\neq n}{\frac {|\int d\mathbf {r} \,\psi _{n}^{*}{\hat {V}}\psi _{n}|^{2}}{E_{n}^{0}-E_{n'}^{0}}}+...$ To compute to linear order in **q** $\sum _{i}{\frac {\partial \varepsilon _{n}}{\partial k_{i}}}q_{i}=\sum _{i}\int d\mathbf {r} \,u_{n\mathbf {k} }^{*}{\frac {\hbar ^{2}}{m}}(-i\nabla +\mathbf {k} )_{i}q_{i}u_{n\mathbf {k} }$ where the integrations are over a primitive cell or the entire crystal, given if the integral $\int d\mathbf {r} \,u_{n\mathbf {k} }^{*}u_{n\mathbf {k} }$ is normalized across the cell or the crystal.

We can simplify over **q** to obtain ${\frac {\partial \varepsilon _{n}}{\partial \mathbf {k} }}={\frac {\hbar ^{2}}{m}}\int d\mathbf {r} \,u_{n\mathbf {k} }^{*}(-i\nabla +\mathbf {k} )u_{n\mathbf {k} }$ and we can reinsert the complete wave functions ${\frac {\partial \varepsilon _{n}}{\partial \mathbf {k} }}={\frac {\hbar ^{2}}{m}}\int d\mathbf {r} \,\psi _{n\mathbf {k} }^{*}(-i\nabla )\psi _{n\mathbf {k} }$

For the effective mass

effective mass theorem

${\frac {\partial ^{2}\varepsilon _{n}(\mathbf {k} )}{\partial k_{i}\partial k_{j}}}={\frac {\hbar ^{2}}{m}}\delta _{ij}+\left({\frac {\hbar ^{2}}{m}}\right)^{2}\sum _{n'\neq n}{\frac {\langle n\mathbf {k} |-i\nabla _{i}|n'\mathbf {k} \rangle \langle n'\mathbf {k} |-i\nabla _{j}|n\mathbf {k} \rangle +\langle n\mathbf {k} |-i\nabla _{j}|n'\mathbf {k} \rangle \langle n'\mathbf {k} |-i\nabla _{i}|n\mathbf {k} \rangle }{\varepsilon _{n}(\mathbf {k} )-\varepsilon _{n'}(\mathbf {k} )}}$

Proof

The second order term ${\frac {1}{2}}\sum _{ij}{\frac {\partial ^{2}\varepsilon _{n}}{\partial k_{i}\partial k_{j}}}q_{i}q_{j}={\frac {\hbar ^{2}}{2m}}q^{2}+\sum _{n'\neq n}{\frac {|\int d\mathbf {r} \,u_{n\mathbf {k} }^{*}{\frac {\hbar ^{2}}{m}}\mathbf {q} \cdot (-i\nabla +\mathbf {k} )u_{n'\mathbf {k} }|^{2}}{\varepsilon _{n\mathbf {k} }-\varepsilon _{n'\mathbf {k} }}}$ Again with $\psi _{n\mathbf {k} }=|n\mathbf {k} \rangle =e^{i\mathbf {k} \mathbf {x} }u_{n\mathbf {k} }$ ${\frac {1}{2}}\sum _{ij}{\frac {\partial ^{2}\varepsilon _{n}}{\partial k_{i}\partial k_{j}}}q_{i}q_{j}={\frac {\hbar ^{2}}{2m}}q^{2}+\sum _{n'\neq n}{\frac {|\langle n\mathbf {k} |{\frac {\hbar ^{2}}{m}}\mathbf {q} \cdot (-i\nabla )|n'\mathbf {k} \rangle |^{2}}{\varepsilon _{n\mathbf {k} }-\varepsilon _{n'\mathbf {k} }}}$ Eliminating $q_{i}$ and $q_{j}$ we have the theorem ${\frac {\partial ^{2}\varepsilon _{n}(\mathbf {k} )}{\partial k_{i}\partial k_{j}}}={\frac {\hbar ^{2}}{m}}\delta _{ij}+\left({\frac {\hbar ^{2}}{m}}\right)^{2}\sum _{n'\neq n}{\frac {\langle n\mathbf {k} |-i\nabla _{i}|n'\mathbf {k} \rangle \langle n'\mathbf {k} |-i\nabla _{j}|n\mathbf {k} \rangle +\langle n\mathbf {k} |-i\nabla _{j}|n'\mathbf {k} \rangle \langle n'\mathbf {k} |-i\nabla _{i}|n\mathbf {k} \rangle }{\varepsilon _{n}(\mathbf {k} )-\varepsilon _{n'}(\mathbf {k} )}}$

The quantity on the right multiplied by a factor ${\frac {1}{\hbar ^{2}}}$ is called effective mass tensor $\mathbf {M} (\mathbf {k} )$ and we can use it to write a semi-classical equation for a charge carrier in a band

Second order semi-classical equation of motion for a

charge carrier

in a band

$\mathbf {M} (\mathbf {k} )\mathbf {a} =\mp e\left(\mathbf {E} +\mathbf {v} (\mathbf {k} )\times \mathbf {B} \right)$

where $\mathbf {a}$ is an acceleration. This equation is analogous to the de Broglie wave type of approximation

First order semi-classical equation of motion for electron in a band

$\hbar {\dot {k}}=-e\left(\mathbf {E} +\mathbf {v} \times \mathbf {B} \right)$

As an intuitive interpretation, both of the previous two equations resemble formally and are in a semi-classical analogy with Newton's second law for an electron in an external Lorentz force.

## Mathematical caveat

Mathematically, a rigorous theorem such as Bloch's theorem cannot exist in Quantum Mechanics: The spectral values of a band structure in a solid crystal or lattice system belong to the continuous spectrum, for which no finite norm eigenstates in the Hilbert space exist, i.e, no eigenstates with finite energy or finite probability can exist – cf. decomposition of spectrum –, because eigenvalues belong to the point spectrum by definition. Therefore, all physicists' calculations in Bloch's theorem with eigenstate decompositions in a Hilbert space are in some sense purely formal: The decomposition series do not converge in Hilbert space, and no proper spatially periodic function can be a finite norm state in the full Hilbert space.

Decompositions of periodic continuous functions – similarly to Bloch – can possibly be performed in spaces of bounded or bounded continuous functions, but not in spaces of functions square integrable over full x-space, which would be the required Hilbert space setting for Quantum Mechanics.

In Mathematical Physics, as a substitute, different rigorous decompositions can be obtained which also provide the band structure, by exploiting lattice symmetry based on a Hilbert space direct integral decomposition. By that method, the Hamiltonian operator is decomposed into a parameter dependent family of so-called *reduced* Hamiltonian operators on a corresponding family of Hilbert spaces and with corresponding domains of definitions (e.g. characterized by different boundary conditions). Each of these Hamiltonians has (in general) a discrete point spectrum with finite eigenstates of finite multiplicity, corresponding to the physicist's eigenvalue computations. Superposing these states with the direct integral would throw the states out of the original Hilbert space (and - possibly - provide only generalized eigenstates in a larger space, e.g. in the top space of a Gelfand triple), but the spectra of these Hamiltonians combine into the continuous band spectrum of the original Hamiltonian.

The concept of the Bloch state was developed by Felix Bloch in 1928 to describe the conduction of electrons in crystalline solids. The same underlying mathematics, however, was also discovered independently several times: by George William Hill (1877), Gaston Floquet (1883), and Alexander Lyapunov (1892). As a result, a variety of nomenclatures are common: applied to ordinary differential equations, it is called Floquet theory (or occasionally the *Lyapunov–Floquet theorem*). The general form of a one-dimensional periodic potential equation is Hill's equation: ${\frac {d^{2}y}{dt^{2}}}+f(t)y=0,$ where *f*(*t*) is a periodic potential. Specific periodic one-dimensional equations include the Kronig–Penney model and Mathieu's equation.

Mathematically, various theorems similar to Bloch's theorem are for instance interpreted in terms of unitary characters of a lattice group, and applied to spectral geometry.

Floquet theory is usually not done in a Hilbert space of functions square integrable with respect to the periodic independent variable, but in Banach spaces of continuous or differentiable functions, or in Frechet or nuclear spaces. So the methods used there do not directly apply to the Hilbert space setting required in Quantum Mechanics and require proper adaptation, such as using a Hilbert space direct integral.
