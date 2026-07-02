---
title: "Wave function (part 2/2)"
source: https://en.wikipedia.org/wiki/Wave_function
domain: quantum-mechanics
license: CC-BY-SA-4.0
tags: quantum mechanics, schrodinger equation, wave function, uncertainty principle
fetched: 2026-07-02
part: 2/2
---

## Wave functions and function spaces

The concept of function spaces enters naturally in the discussion about wave functions. A function space is a set of functions, usually with some defining requirements on the functions (in the present case that they are square integrable), sometimes with an algebraic structure on the set (in the present case a vector space structure with an inner product), together with a topology on the set. The latter will sparsely be used here, it is only needed to obtain a precise definition of what it means for a subset of a function space to be closed. It will be concluded below that the function space of wave functions is a Hilbert space. This observation is the foundation of the predominant mathematical formulation of quantum mechanics.

### Vector space structure

A wave function is an element of a function space partly characterized by the following concrete and abstract descriptions.

- The Schrödinger equation is linear. This means that the solutions to it, wave functions, can be added and multiplied by scalars to form a new solution. The set of solutions to the Schrödinger equation is a vector space.
- The superposition principle of quantum mechanics. If Ψ and Φ are two states in the abstract space of **states** of a quantum mechanical system, and *a* and *b* are any two complex numbers, then *a*Ψ + *b*Φ is a valid state as well. (Whether the null vector counts as a valid state ("no system present") is a matter of definition. The null vector does *not* at any rate describe the vacuum state in quantum field theory.) The set of allowable states is a vector space.

This similarity is of course not accidental. There are also a distinctions between the spaces to keep in mind.

### Representations

Basic states are characterized by a set of quantum numbers. This is a set of eigenvalues of a **maximal set** of commuting observables. Physical observables are represented by linear operators, also called observables, on the vectors space. Maximality means that there can be added to the set no further algebraically independent observables that commute with the ones already present. A choice of such a set may be called a choice of **representation**.

- It is a postulate of quantum mechanics that a physically observable quantity of a system, such as position, momentum, or spin, is represented by a linear Hermitian operator on the state space. The possible outcomes of measurement of the quantity are the eigenvalues of the operator. At a deeper level, most observables, perhaps all, arise as generators of symmetries.
- The physical interpretation is that such a set represents what can – in theory – simultaneously be measured with arbitrary precision. The Heisenberg uncertainty relation prohibits simultaneous exact measurements of two non-commuting observables.
- The set is non-unique. It may for a one-particle system, for example, be position and spin *z*-projection, (*x*, *S**z*), or it may be momentum and spin *y*-projection, (*p*, *S**y*). In this case, the operator corresponding to position (a multiplication operator in the position representation) and the operator corresponding to momentum (a differential operator in the position representation) do not commute.
- Once a representation is chosen, there is still arbitrariness. It remains to choose a coordinate system. This may, for example, correspond to a choice of *x*, *y*- and *z*-axis, or a choice of **curvilinear coordinates** as exemplified by the spherical coordinates used for the Hydrogen atomic wave functions. This final choice also fixes a basis in abstract Hilbert space. The basic states are labeled by the quantum numbers corresponding to the maximal set of commuting observables and an appropriate coordinate system.

The abstract states are "abstract" only in that an arbitrary choice necessary for a particular *explicit* description of it is not given. This is the same as saying that no choice of maximal set of commuting observables has been given. This is analogous to a vector space without a specified basis. Wave functions corresponding to a state are accordingly not unique. This non-uniqueness reflects the non-uniqueness in the choice of a maximal set of commuting observables. For one spin particle in one dimension, to a particular state there corresponds two wave functions, Ψ(*x*, *S**z*) and Ψ(*p*, *S**y*), both describing the *same* state.

- For each choice of maximal commuting sets of observables for the abstract state space, there is a corresponding representation that is associated to a function space of wave functions.
- Between all these different function spaces and the abstract state space, there are one-to-one correspondences (here disregarding normalization and unobservable phase factors), the common denominator here being a particular abstract state. The relationship between the momentum and position space wave functions, for instance, describing the same state is the Fourier transform.

Each choice of representation should be thought of as specifying a unique function space in which wave functions corresponding to that choice of representation lives. This distinction is best kept, even if one could argue that two such function spaces are mathematically equal, e.g. being the set of square integrable functions. One can then think of the function spaces as two distinct copies of that set.

### Inner product

There is an additional algebraic structure on the vector spaces of wave functions and the abstract state space.

- Physically, different wave functions are interpreted to overlap to some degree. A system in a state Ψ that does *not* overlap with a state Φ cannot be found to be in the state Φ upon measurement. But if Φ1, Φ2, … overlap Ψ to *some* degree, there is a chance that measurement of a system described by Ψ will be found in states Φ1, Φ2, …. Also selection rules are observed apply. These are usually formulated in the preservation of some quantum numbers. This means that certain processes allowable from some perspectives (e.g. energy and momentum conservation) do not occur because the initial and final *total* wave functions do not overlap.
- Mathematically, it turns out that solutions to the Schrödinger equation for particular potentials are **orthogonal** in some manner, this is usually described by an integral $\int \Psi _{m}^{*}\Psi _{n}w\,dV=\delta _{nm},$ where *m*, *n* are (sets of) indices (quantum numbers) labeling different solutions, the strictly positive function w is called a weight function, and *δ**mn* is the Kronecker delta. The integration is taken over all of the relevant space.

This motivates the introduction of an inner product on the vector space of abstract quantum states, compatible with the mathematical observations above when passing to a representation. It is denoted (Ψ, Φ), or in the Bra–ket notation ⟨Ψ|Φ⟩. It yields a complex number. With the inner product, the function space is an inner product space. The explicit appearance of the inner product (usually an integral or a sum of integrals) depends on the choice of representation, but the complex number (Ψ, Φ) does not. Much of the physical interpretation of quantum mechanics stems from the Born rule. It states that the probability p of finding upon measurement the state Φ given the system is in the state Ψ is $p=|(\Phi ,\Psi )|^{2},$ where Φ and Ψ are assumed normalized. Consider a scattering experiment. In quantum field theory, if Φout describes a state in the "distant future" (an "out state") after interactions between scattering particles have ceased, and Ψin an "in state" in the "distant past", then the quantities (Φout, Ψin), with Φout and Ψin varying over a complete set of in states and out states respectively, is called the S-matrix or **scattering matrix**. Knowledge of it is, effectively, having *solved* the theory at hand, at least as far as predictions go. Measurable quantities such as decay rates and scattering cross sections are calculable from the S-matrix.

### Hilbert space

The above observations encapsulate the essence of the function spaces of which wave functions are elements. However, the description is not yet complete. There is a further technical requirement on the function space, that of completeness, that allows one to take limits of sequences in the function space, and be ensured that, if the limit exists, it is an element of the function space. A complete inner product space is called a Hilbert space. The property of completeness is crucial in advanced treatments and applications of quantum mechanics. For instance, the existence of projection operators or **orthogonal projections** relies on the completeness of the space. These projection operators, in turn, are essential for the statement and proof of many useful theorems, e.g. the spectral theorem. It is not very important in introductory quantum mechanics, and technical details and links may be found in footnotes like the one that follows. The space *L*2 is a Hilbert space, with inner product presented later. The function space of the example of the figure is a subspace of *L*2. A subspace of a Hilbert space is a Hilbert space if it is closed.

In summary, the set of all possible normalizable wave functions for a system with a particular choice of basis, together with the null vector, constitute a Hilbert space.

Not all functions of interest are elements of some Hilbert space, say *L*2. The most glaring example is the set of functions *e*2*πi***p** · **x**⁄h. These are plane wave solutions of the Schrödinger equation for a free particle that are not normalizable, hence not in *L*2. But they are nonetheless fundamental for the description. One can, using them, express functions that *are* normalizable using wave packets. They are, in a sense, a basis (but not a Hilbert space basis, nor a Hamel basis) in which wave functions of interest can be expressed. There is also the artifact "normalization to a delta function" that is frequently employed for notational convenience, see further down. The delta functions themselves are not square integrable either.

The above description of the function space containing the wave functions is mostly mathematically motivated. The function spaces are, due to completeness, very *large* in a certain sense. Not all functions are realistic descriptions of any physical system. For instance, in the function space *L*2 one can find the function that takes on the value 0 for all rational numbers and -*i* for the irrationals in the interval [0, 1]. This *is* square integrable, but can hardly represent a physical state.

### Common Hilbert spaces

While the space of solutions as a whole is a Hilbert space there are many other Hilbert spaces that commonly occur as ingredients.

- Square integrable complex valued functions on the interval [0, 2*π*]. The set {*e**int*/2*π*, *n* ∈ **Z**} is a Hilbert space basis, i.e. a maximal orthonormal set.
- The Fourier transform takes functions in the above space to elements of *l*2(**Z**), the space of *square summable* functions **Z** → **C**. The latter space is a Hilbert space and the Fourier transform is an isomorphism of Hilbert spaces. Its basis is {*e**i*, *i* ∈ **Z**} with *e**i*(*j*) = *δ**ij*, *i*, *j* ∈ **Z**.
- The most basic example of spanning polynomials is in the space of square integrable functions on the interval [–1, 1] for which the Legendre polynomials is a Hilbert space basis (complete orthonormal set).
- The square integrable functions on the unit sphere *S*2 is a Hilbert space. The basis functions in this case are the spherical harmonics. The Legendre polynomials are ingredients in the spherical harmonics. Most problems with rotational symmetry will have "the same" (known) solution with respect to that symmetry, so the original problem is reduced to a problem of lower dimensionality.
- The associated Laguerre polynomials appear in the hydrogenic wave function problem after factoring out the spherical harmonics. These span the Hilbert space of square integrable functions on the semi-infinite interval [0, ∞).

More generally, one may consider a unified treatment of all second order polynomial solutions to the Sturm–Liouville equations in the setting of Hilbert space. These include the Legendre and Laguerre polynomials as well as Chebyshev polynomials, Jacobi polynomials and Hermite polynomials. All of these actually appear in physical problems, the latter ones in the harmonic oscillator, and what is otherwise a bewildering maze of properties of special functions becomes an organized body of facts. For this, see Byron & Fuller (1992, Chapter 5).

There occurs also finite-dimensional Hilbert spaces. The space **C***n* is a Hilbert space of dimension n. The inner product is the standard inner product on these spaces. In it, the "spin part" of a single particle wave function resides.

- In the non-relativistic description of an electron one has *n* = 2 and the total wave function is a solution of the Pauli equation.
- In the corresponding relativistic treatment, *n* = 4 and the wave function solves the Dirac equation.

With more particles, the situations is more complicated. One has to employ tensor products and use representation theory of the symmetry groups involved (the rotation group and the Lorentz group respectively) to extract from the tensor product the spaces in which the (total) spin wave functions reside. (Further problems arise in the relativistic case unless the particles are free. See the Bethe–Salpeter equation.) Corresponding remarks apply to the concept of isospin, for which the symmetry group is SU(2). The models of the nuclear forces of the sixties (still useful today, see nuclear force) used the symmetry group SU(3). In this case, as well, the part of the wave functions corresponding to the inner symmetries reside in some **C***n* or subspaces of tensor products of such spaces.

- In quantum field theory the underlying Hilbert space is Fock space. It is built from free single-particle states, i.e. wave functions when a representation is chosen, and can accommodate any finite, not necessarily constant in time, number of particles. The interesting (or rather the *tractable*) dynamics lies not in the wave functions but in the field operators that are operators acting on Fock space. Thus the Heisenberg picture is the most common choice (constant states, time varying operators).

Due to the infinite-dimensional nature of the system, the appropriate mathematical tools are objects of study in functional analysis.

### Simplified description

Not all introductory textbooks take the long route and introduce the full Hilbert space machinery, but the focus is on the non-relativistic Schrödinger equation in position representation for certain standard potentials. The following constraints on the wave function are sometimes explicitly formulated for the calculations and physical interpretation to make sense:

- The wave function must be square integrable. This is motivated by the Copenhagen interpretation of the wave function as a probability amplitude.
- It must be everywhere continuous and everywhere continuously differentiable. This is motivated by the appearance of the Schrödinger equation for most physically reasonable potentials.

It is possible to relax these conditions somewhat for special purposes. If these requirements are not met, it is not possible to interpret the wave function as a probability amplitude. Note that exceptions can arise to the continuity of derivatives rule at points of infinite discontinuity of potential field. For example, in particle in a box where the derivative of wavefunction can be discontinuous at the boundary of the box where the potential is known to have infinite discontinuity.

This does not alter the structure of the Hilbert space that these particular wave functions inhabit, but the subspace of the square-integrable functions *L*2, which is a Hilbert space, satisfying the second requirement *is not closed* in *L*2, hence not a Hilbert space in itself. The functions that does not meet the requirements are still needed for both technical and practical reasons.


## More on wave functions and abstract state space

As has been demonstrated, the set of all possible wave functions in some representation for a system constitute an in general infinite-dimensional Hilbert space. Due to the multiple possible choices of representation basis, these Hilbert spaces are not unique. One therefore talks about an abstract Hilbert space, **state space**, where the choice of representation and basis is left undetermined. Specifically, each state is represented as an abstract vector in state space. A quantum state |Ψ⟩ in any representation is generally expressed as a vector $|\Psi \rangle =\sum _{\boldsymbol {\alpha }}\int d^{m}\!{\boldsymbol {\omega }}\,\,\Psi _{t}({\boldsymbol {\alpha }},{\boldsymbol {\omega }})\,|{\boldsymbol {\alpha }},{\boldsymbol {\omega }}\rangle$ where

- |**α**, **ω**⟩ the basis vectors of the chosen representation
- *dm***ω** = *dω*1*dω*2...*dωm* a differential volume element in the continuous degrees of freedom
- ${\boldsymbol {\Psi }}_{t}({\boldsymbol {\alpha }},{\boldsymbol {\omega }})$ a component of the vector $|\Psi \rangle$ , called the **wave function** of the system
- **α** = (*α*1, *α*2, ..., *αn*) dimensionless discrete quantum numbers
- **ω** = (*ω*1, *ω*2, ..., *ωm*) continuous variables (not necessarily dimensionless)

These quantum numbers index the components of the state vector. More, all **α** are in an *n*-dimensional set *A* = *A*1 × *A*2 × ... × *An* where each *Ai* is the set of allowed values for *αi*; all **ω** are in an *m*-dimensional "volume" Ω ⊆ ℝ*m* where Ω = Ω1 × Ω2 × ... × Ω*m* and each Ω*i* ⊆ **R** is the set of allowed values for *ωi*, a subset of the real numbers **R**. For generality n and m are not necessarily equal.

**Example:**

1. For a single particle in 3d with spin *s*, neglecting other degrees of freedom, using Cartesian coordinates, we could take **α** = (*sz*) for the spin quantum number of the particle along the z direction, and **ω** = (*x*, *y*, *z*) for the particle's position coordinates. Here *A* = {−*s*, −*s* + 1, ..., *s* − 1, *s*} is the set of allowed spin quantum numbers and Ω = **R**3 is the set of all possible particle positions throughout 3d position space.
2. An alternative choice is **α** = (*sy*) for the spin quantum number along the y direction and **ω** = (*px*, *py*, *pz*) for the particle's momentum components. In this case *A* and Ω are the same as before.

The probability density of finding the system at time t at state |**α**, **ω**⟩ is $\rho _{\alpha ,\omega }(t)=|\Psi ({\boldsymbol {\alpha }},{\boldsymbol {\omega }},t)|^{2}$

The probability of finding system with **α** in some or all possible discrete-variable configurations, *D* ⊆ *A*, and **ω** in some or all possible continuous-variable configurations, *C* ⊆ Ω, is the sum and integral over the density, $P(t)=\sum _{{\boldsymbol {\alpha }}\in D}\int _{C}d^{m}\!{\boldsymbol {\omega }}\,\,\rho _{\alpha ,\omega }(t)$

Since the sum of all probabilities must be 1, the normalization condition $1=\sum _{{\boldsymbol {\alpha }}\in A}\int _{\Omega }d^{m}\!{\boldsymbol {\omega }}\,\,\rho _{\alpha ,\omega }(t)$ must hold at all times during the evolution of the system.

The normalization condition requires *ρ dm***ω** to be dimensionless, by dimensional analysis Ψ must have the same units as (*ω*1*ω*2...*ωm*)−1/2.


## Ontology

Whether the wave function exists in reality, and what it represents, are major questions in the interpretation of quantum mechanics. Many famous physicists of a previous generation puzzled over this problem, such as Erwin Schrödinger, Albert Einstein and Niels Bohr. Some advocate formulations or variants of the Copenhagen interpretation (e.g. Bohr, Eugene Wigner and John von Neumann) while others, such as John Archibald Wheeler or Edwin Thompson Jaynes, take the more classical approach and regard the wave function as representing information in the mind of the observer, i.e. a measure of our knowledge of reality. Some, including Schrödinger, David Bohm and Hugh Everett III and others, argued that the wave function must have an objective, physical existence. Einstein thought that a complete description of physical reality should refer directly to physical space and time, as distinct from the wave function, which refers to an abstract mathematical space.
