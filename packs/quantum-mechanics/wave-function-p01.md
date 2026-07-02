---
title: "Wave function (part 1/2)"
source: https://en.wikipedia.org/wiki/Wave_function
domain: quantum-mechanics
license: CC-BY-SA-4.0
tags: quantum mechanics, schrodinger equation, wave function, uncertainty principle
fetched: 2026-07-02
part: 1/2
---

# Wave function

In quantum mechanics, a **wave function** (or **wavefunction**) is a mathematical description of the quantum state of an isolated quantum system. The most common symbols for a wave function are the Greek letters *ψ* and Ψ (lower-case and capital psi, respectively).

According to the superposition principle of quantum mechanics, wave functions can be added together and multiplied by complex numbers to form new wave functions and form a Hilbert space. The inner product of two wave functions is a measure of the overlap between the corresponding physical states and is used in the foundational probabilistic interpretation of quantum mechanics, the Born rule, relating transition probabilities to inner products. The Schrödinger equation determines how wave functions evolve over time, and a wave function behaves qualitatively like other waves, such as water waves or waves on a string, because the Schrödinger equation is mathematically a type of wave equation. This explains the name "wave function", and gives rise to wave–particle duality. However, whether the wave function in quantum mechanics describes a kind of physical phenomenon is still open to different interpretations, fundamentally differentiating it from classic mechanical waves.

Wave functions are complex-valued. For example, a wave function might assign a complex number to each point in a region of space. The Born rule provides the means to turn these complex probability amplitudes into actual probabilities. In one common form, it says that the squared modulus of a wave function that depends upon position is the probability density of measuring a particle as being at a given place. The integral of a wavefunction's squared modulus over all the system's degrees of freedom must be equal to 1, a condition called *normalization*. Since the wave function is complex-valued, only its relative phase and relative magnitude can be measured; its value does not, in isolation, tell anything about the magnitudes or directions of measurable observables. One has to apply quantum operators, whose eigenvalues correspond to sets of possible results of measurements, to the wave function *ψ* and calculate the statistical distributions for measurable quantities.

Wave functions can be functions of variables other than position, such as momentum. The information represented by a wave function that is dependent upon position can be converted into a wave function dependent upon momentum and vice versa, by means of a Fourier transform. Some particles, like electrons and photons, have nonzero spin, and the wave function for such particles includes spin as an intrinsic, discrete degree of freedom; other discrete variables can also be included, such as isospin. When a system has internal degrees of freedom, the wave function at each point in the continuous degrees of freedom (e.g., a point in space) assigns a complex number for *each* possible value of the discrete degrees of freedom (e.g., z-component of spin). These values are often displayed in a column matrix (e.g., a 2 × 1 column vector for a non-relativistic electron with spin 1⁄2).


## Historical background

In 1900, Max Planck postulated the proportionality between the frequency f of a photon and its energy E , $E=hf$ , and in 1916 the corresponding relation between a photon's momentum p and wavelength $\lambda$ , $\lambda ={\frac {h}{p}}$ , where h is the Planck constant. In 1923, De Broglie was the first to suggest that the relation $\lambda ={\frac {h}{p}}$ , now called the De Broglie relation, holds for *massive* particles, the chief clue being Lorentz invariance, and this can be viewed as the starting point for the modern development of quantum mechanics. The equations represent wave–particle duality for both massless and massive particles.

In the 1920s and 1930s, quantum mechanics was developed using calculus and linear algebra. Those who used the techniques of calculus included Louis de Broglie, Erwin Schrödinger, and others, developing "wave mechanics". Those who applied the methods of linear algebra included Werner Heisenberg, Max Born, and others, developing "matrix mechanics". Schrödinger subsequently showed that the two approaches were equivalent.

In 1926, Schrödinger published the famous wave equation now named after him, the Schrödinger equation. This equation was based on classical conservation of energy using quantum operators and the de Broglie relations and the solutions of the equation are the wave functions for the quantum system. However, no one was clear on how to interpret it. At first, Schrödinger and others thought that wave functions represent particles that are spread out with most of the particle being where the wave function is large. This was shown to be incompatible with the elastic scattering of a wave packet (representing a particle) off a target; it spreads out in all directions. While a scattered particle may scatter in any direction, it does not break up and take off in all directions. In 1926, Born provided the perspective of probability amplitude. This relates calculations of quantum mechanics directly to probabilistic experimental observations. It is accepted as part of the Copenhagen interpretation of quantum mechanics. There are many other interpretations of quantum mechanics. In 1927, Hartree and Fock made the first step in an attempt to solve the *N*-body wave function, and developed the *self-consistency cycle*: an iterative algorithm to approximate the solution. Now it is also known as the Hartree–Fock method. The Slater determinant and permanent (of a matrix) was part of the method, provided by John C. Slater.

Schrödinger did encounter an equation for the wave function that satisfied relativistic energy conservation *before* he published the non-relativistic one, but discarded it as it predicted negative probabilities and negative energies. In 1927, Klein, Gordon and Fock also found it, but incorporated the electromagnetic interaction and proved that it was Lorentz invariant. De Broglie also arrived at the same equation in 1928. This relativistic wave equation is now most commonly known as the Klein–Gordon equation.

In 1927, Pauli phenomenologically found a non-relativistic equation to describe spin-1/2 particles in electromagnetic fields, now called the Pauli equation. Pauli found the wave function was not described by a single complex function of space and time, but needed two complex numbers, which respectively correspond to the spin +1/2 and −1/2 states of the fermion. Soon after in 1928, Dirac found an equation from the first successful unification of special relativity and quantum mechanics applied to the electron, now called the Dirac equation. In this, the wave function is a *spinor* represented by four complex-valued components: two for the electron and two for the electron's antiparticle, the positron. In the non-relativistic limit, the Dirac wave function resembles the Pauli wave function for the electron. Later, other relativistic wave equations were found.

### Wave functions and wave equations in modern theories

All these wave equations are of enduring importance. The Schrödinger equation and the Pauli equation are under many circumstances excellent approximations of the relativistic variants. They are considerably easier to solve in practical problems than the relativistic counterparts.

The Klein–Gordon equation and the Dirac equation, while being relativistic, do not represent full reconciliation of quantum mechanics and special relativity. The branch of quantum mechanics where these equations are studied the same way as the Schrödinger equation, often called relativistic quantum mechanics, while very successful, has its limitations (see e.g. Lamb shift) and conceptual problems (see e.g. Dirac sea).

Relativity makes it inevitable that the number of particles in a system is not constant. For full reconciliation, quantum field theory is needed. In this theory, the wave equations and the wave functions have their place, but in a somewhat different guise. The main objects of interest are not the wave functions, but rather operators, so called *field operators* (or just fields where "operator" is understood) on the Hilbert space of states (to be described next section). It turns out that the original relativistic wave equations and their solutions are still needed to build the Hilbert space. Moreover, the *free fields operators*, i.e. when interactions are assumed not to exist, turn out to (formally) satisfy the same equation as do the fields (wave functions) in many cases.

Thus the Klein–Gordon equation (spin 0) and the Dirac equation (spin 1⁄2) in this guise remain in the theory. Higher spin analogues include the Proca equation (spin 1), Rarita–Schwinger equation (spin 3⁄2), and, more generally, the Bargmann–Wigner equations. For *massless* free fields two examples are the free field Maxwell equation (spin 1) and the free field Einstein equation (spin 2) for the field operators. All of them are essentially a direct consequence of the requirement of Lorentz invariance. Their solutions must transform under Lorentz transformation in a prescribed way, i.e. under a particular representation of the Lorentz group and that together with few other reasonable demands, e.g. the cluster decomposition property, with implications for causality is enough to fix the equations.

This applies to free field equations; interactions are not included. If a Lagrangian density (including interactions) is available, then the Lagrangian formalism will yield an equation of motion at the classical level. This equation may be very complex and not amenable to solution. Any solution would refer to a *fixed* number of particles and would not account for the term "interaction" as referred to in these theories, which involves the creation and annihilation of particles and not external potentials as in ordinary "first quantized" quantum theory.

In string theory, the situation remains analogous. For instance, a wave function in momentum space has the role of Fourier expansion coefficient in a general state of a particle (string) with momentum that is not sharply defined.

### Relativistic particles: classical vs quantum

Source:

Classical particles, like bullets, rockets and planets are spatially localized. Classical waves like sound and ocean waves expand over large spatial regions. Quantum wave-particle duality is a unique characteristic of quantum particles. For instance, spatially localized atoms are stable due to the existence of waves associate to the electrons in the atom. There is no consensus about the nature of the waves associated to quantum particles; however, there is consensus on how to calculate the mathematical expressions corresponding to these waves.

In non-relativistic quantum mechanics, there is a wave associate to a spin-0 quantum particle. The Schrödinger wave equation should be solved for obtaining the mathematical expression corresponding to this "Schrödinger" wave. However, in relativistic quantum mechanics a relativistic wave equation should be solved. Alternatively, a pair of relativistic but Schrödinger-like wave equations could be solved for obtaining the mathematical expressions of the two Schrödinger-like waves associated to a spin-0 relativistic quantum particle.

There is no wave associated with a classical particle, but there is one Schrödinger wave associated with a spin-0 non-relativistic quantum particle. Moreover, there are two Schrödinger waves associated with a spin-0 relativistic quantum particle. Free classical and non-relativistic quantum particles have positive kinetic energies. However, a relativistic quantum particle could be associate with an "ordinary" Schrödinger-like wave where the particle has positive kinetic energy, but it could also be associated to an "extraordinary" Schrödinger wave where the particle has negative kinetic energy.

The existence of Schrödinger waves associated to a particle determines the quantum characteristics of the quantum particle. If for any reason the Schrödinger waves disappear, then the particle lost is quantum nature and it transforms in a classical particle. Several transcendent instances of such quantum to classical transitions have been proposed for explaining why the macroscopic objects surrounding us seems to be classical and matter-only made of. Instances of the quantum-classical frontiers are the following:

- The electrostatic attraction between the nucleus and electrons in heavy atoms can collapse the ordinary Schrödinger wave associated to a relativistic electron. This explains why there are not neutral atoms with atomic number Z > 137.
- Gravity can collapse de ordinary Schrödinger wave associate to a relativistic quantum particle with mass. This explains why macroscopic objects are classical.
- Electrostatic repulsion could collapse the extraordinary Schrödinger wave associated to an antiparticle, but it does not occur for relativistic quantum particles. This explains why there is not Periodic Table for antiatoms and life made of antimatter does not exist.


## Definition (one spinless particle in one dimension)

Standing waves

for a

particle in a box

, examples of

stationary states

Travelling waves of a free particle.

The

real parts

of position wave function

Ψ(

x

)

and momentum wave function

Φ(

p

)

, and corresponding probability densities

|Ψ(

x

)|

2

and

|Φ(

p

)|

2

, for one spin-0 particle in one

x

or

p

dimension. The color opacity of the particles corresponds to the probability density (

not

the wave function) of finding the particle at position

x

or momentum

p

.

For now, consider the simple case of a non-relativistic single particle, without spin, in one spatial dimension. More general cases are discussed below.

According to the postulates of quantum mechanics, the state of a physical system, at fixed time t , is given by the wave function belonging to a separable complex Hilbert space. As such, the inner product of two wave functions Ψ1 and Ψ2 can be defined as the complex number (at time t)

$(\Psi _{1},\Psi _{2})=\int _{-\infty }^{\infty }\,\Psi _{1}^{*}(x,t)\Psi _{2}(x,t)\,dx<\infty$

.

More details are given below. However, the inner product of a wave function Ψ with itself,

$(\Psi ,\Psi )=\|\Psi \|^{2}$

,

is *always* a positive real number. The number ‖Ψ‖ (not ‖Ψ‖2) is called the **norm** of the wave function Ψ. The separable Hilbert space being considered is infinite-dimensional, which means there is no finite set of square integrable functions which can be added together in various combinations to create every possible square integrable function.

### Position-space wave functions

The state of such a particle is completely described by its wave function, $\Psi (x,t)\,,$ where x is position and t is time. This is a complex-valued function of two real variables x and t.

For one spinless particle in one dimension, if the wave function is interpreted as a probability amplitude; the square modulus of the wave function, the positive real number $\left|\Psi (x,t)\right|^{2}=\Psi ^{*}(x,t)\Psi (x,t)=\rho (x),$ is interpreted as the probability density for a measurement of the particle's position at a given time *t*. The asterisk indicates the complex conjugate. If the particle's position is measured, its location cannot be determined from the wave function, but is described by a probability distribution.

#### Normalization condition

The probability that its position *x* will be in the interval *a* ≤ *x* ≤ *b* is the integral of the density over this interval: $P_{a\leq x\leq b}(t)=\int _{a}^{b}\,|\Psi (x,t)|^{2}dx$ where t is the time at which the particle was measured. This leads to the **normalization condition**: $\int _{-\infty }^{\infty }\,|\Psi (x,t)|^{2}dx=1\,,$ because if the particle is measured, there is 100% probability that it will be *somewhere*.

For a given system, the set of all possible normalizable wave functions (at any given time) forms an abstract mathematical vector space, meaning that it is possible to add together different wave functions, and multiply wave functions by complex numbers. Technically, wave functions form a ray in a projective Hilbert space rather than an ordinary vector space.

#### Quantum states as vectors

At a particular instant of time, all values of the wave function Ψ(*x*, *t*) are components of a vector. There are uncountably infinitely many of them and integration is used in place of summation. In Bra–ket notation, this vector is written $|\Psi (t)\rangle =\int \Psi (x,t)|x\rangle dx$ and is referred to as a "quantum state vector", or simply "quantum state". There are several advantages to understanding wave functions as representing elements of an abstract vector space:

- All the powerful tools of linear algebra can be used to manipulate and understand wave functions. For example:
  - Linear algebra explains how a vector space can be given a basis, and then any vector in the vector space can be expressed in this basis. This explains the relationship between a wave function in position space and a wave function in momentum space and suggests that there are other possibilities too.
  - Bra–ket notation can be used to manipulate wave functions.
- The idea that quantum states are vectors in an abstract vector space is completely general in all aspects of quantum mechanics and quantum field theory, whereas the idea that quantum states are complex-valued "wave" functions of space is only true in certain situations.

The time parameter is often suppressed, and will be in the following. The x coordinate is a continuous index. The |*x*⟩ are called *improper vectors* which, unlike *proper vectors* that are normalizable to unity, can only be normalized to a Dirac delta function. $\langle x'|x\rangle =\delta (x'-x)$ thus $\langle x'|\Psi \rangle =\int \Psi (x)\langle x'|x\rangle dx=\Psi (x')$ and $|\Psi \rangle =\int |x\rangle \langle x|\Psi \rangle dx=\left(\int |x\rangle \langle x|dx\right)|\Psi \rangle$ which illuminates the identity operator $I=\int |x\rangle \langle x|dx\,.$ which is analogous to completeness relation of orthonormal basis in N-dimensional Hilbert space.

Finding the identity operator in a basis allows the abstract state to be expressed explicitly in a basis, and more (the inner product between two state vectors, and other operators for observables, can be expressed in the basis).

### Momentum-space wave functions

The particle also has a wave function in momentum space: $\Phi (p,t)$ where p is the momentum in one dimension, which can be any value from −∞ to +∞, and t is time.

Analogous to the position case, the inner product of two wave functions Φ1(*p*, *t*) and Φ2(*p*, *t*) can be defined as: $(\Phi _{1},\Phi _{2})=\int _{-\infty }^{\infty }\,\Phi _{1}^{*}(p,t)\Phi _{2}(p,t)dp\,.$

One particular solution to the time-independent Schrödinger equation is $\Psi _{p}(x)=e^{ipx/\hbar },$ a plane wave, which can be used in the description of a particle with momentum exactly p, since it is an eigenfunction of the momentum operator. These functions are not normalizable to unity (they are not square-integrable), so they are not really elements of physical Hilbert space. The set $\{\Psi _{p}(x,t),-\infty \leq p\leq \infty \}$ forms what is called the **momentum basis**. This "basis" is not a basis in the usual mathematical sense. For one thing, since the functions are not normalizable, they are instead **normalized to a delta function**, $(\Psi _{p},\Psi _{p'})=\delta (p-p').$

For another thing, though they are linearly independent, there are too many of them (they form an uncountable set) for a basis for physical Hilbert space. They can still be used to express all functions in it using Fourier transforms as described next.

### Relations between position and momentum representations

The *x* and *p* representations are ${\begin{aligned}|\Psi \rangle =I|\Psi \rangle &=\int |x\rangle \langle x|\Psi \rangle dx=\int \Psi (x)|x\rangle dx,\\|\Psi \rangle =I|\Psi \rangle &=\int |p\rangle \langle p|\Psi \rangle dp=\int \Phi (p)|p\rangle dp.\end{aligned}}$

Now take the projection of the state Ψ onto eigenfunctions of momentum using the last expression in the two equations, $\int \Psi (x)\langle p|x\rangle dx=\int \Phi (p')\langle p|p'\rangle dp'=\int \Phi (p')\delta (p-p')dp'=\Phi (p).$

Then utilizing the known expression for suitably normalized eigenstates of momentum in the position representation solutions of the free Schrödinger equation $\langle x|p\rangle =p(x)={\frac {1}{\sqrt {2\pi \hbar }}}e^{{\frac {i}{\hbar }}px}\Rightarrow \langle p|x\rangle ={\frac {1}{\sqrt {2\pi \hbar }}}e^{-{\frac {i}{\hbar }}px},$ one obtains $\Phi (p)={\frac {1}{\sqrt {2\pi \hbar }}}\int \Psi (x)e^{-{\frac {i}{\hbar }}px}dx\,.$

Likewise, using eigenfunctions of position, $\Psi (x)={\frac {1}{\sqrt {2\pi \hbar }}}\int \Phi (p)e^{{\frac {i}{\hbar }}px}dp\,.$

The position-space and momentum-space wave functions are thus found to be Fourier transforms of each other. They are two representations of the same state; containing the same information, and either one is sufficient to calculate any property of the particle.

In practice, the position-space wave function is used much more often than the momentum-space wave function. The potential entering the relevant equation (Schrödinger, Dirac, etc.) determines in which basis the description is easiest. For the harmonic oscillator, x and p enter symmetrically, so there it does not matter which description one uses. The same equation (modulo constants) results. From this, with a little bit of afterthought, it follows that solutions to the wave equation of the harmonic oscillator are eigenfunctions of the Fourier transform in *L*2.


## Definitions (other cases)

Following are the general forms of the wave function for systems in higher dimensions and more particles, as well as including other degrees of freedom than position coordinates or momentum components.

### Finite dimensional Hilbert space

While Hilbert spaces originally refer to infinite dimensional complete inner product spaces they, by definition, include finite dimensional complete inner product spaces as well. In physics, they are often referred to as *finite dimensional Hilbert spaces*. For every finite dimensional Hilbert space there exist orthonormal basis kets that span the entire Hilbert space.

If the *N*-dimensional set ${\textstyle \{|\phi _{i}\rangle \}}$ is orthonormal, then the projection operator for the space spanned by these states is given by:

$P=\sum _{i}|\phi _{i}\rangle \langle \phi _{i}|=I$ where the projection is equivalent to identity operator since ${\textstyle \{|\phi _{i}\rangle \}}$ spans the entire Hilbert space, thus leaving any vector from Hilbert space unchanged. This is also known as completeness relation of finite dimensional Hilbert space.

The wavefunction is instead given by:

$|\psi \rangle =I|\psi \rangle =\sum _{i}|\phi _{i}\rangle \langle \phi _{i}|\psi \rangle$ where ${\textstyle \{\langle \phi _{i}|\psi \rangle \}}$ , is a set of complex numbers which can be used to construct a wavefunction using the above formula.

#### Probability interpretation of inner product

If the set ${\textstyle \{|\phi _{i}\rangle \}}$ are eigenkets of a non-degenerate observable with eigenvalues ${\textstyle \lambda _{i}}$ , by the postulates of quantum mechanics, the probability of measuring the observable to be ${\textstyle \lambda _{i}}$ is given according to Born rule as:

$P_{\psi }(\lambda _{i})=|\langle \phi _{i}|\psi \rangle |^{2}$

For non-degenerate ${\textstyle \{|\phi _{i}\rangle \}}$ of some observable, if eigenvalues ${\textstyle \lambda }$ have subset of eigenvectors labelled as ${\textstyle \{|\lambda ^{(j)}\rangle \}}$ , by the postulates of quantum mechanics, the probability of measuring the observable to be ${\textstyle \lambda }$ is given by:

$P_{\psi }(\lambda )=\sum _{j}|\langle \lambda ^{(j)}|\psi \rangle |^{2}=|{\widehat {P}}_{\lambda }|\psi \rangle |^{2}$ where ${\textstyle {\widehat {P}}_{\lambda }=\sum _{j}|\lambda ^{(j)}\rangle \langle \lambda ^{(j)}|}$ is a projection operator of states to subspace spanned by ${\textstyle \{|\lambda ^{(j)}\rangle \}}$ . The equality follows due to orthogonal nature of ${\textstyle \{|\phi _{i}\rangle \}}$ .

Hence, ${\textstyle \{\langle \phi _{i}|\psi \rangle \}}$ which specify state of the quantum mechanical system, have magnitudes whose square gives the probability of measuring the respective ${\textstyle |\phi _{i}\rangle }$ state.

#### Physical significance of relative phase

While the relative phase has observable effects in experiments, the global phase of the system is experimentally indistinguishable. For example in a particle in superposition of two states, the global phase of the particle cannot be distinguished by finding expectation value of observable or probabilities of observing different states but relative phases can affect the expectation values of observables.

While the overall phase of the system is considered to be arbitrary, the relative phase for each state ${\textstyle |\phi _{i}\rangle }$ of a prepared state in superposition can be determined based on physical meaning of the prepared state and its symmetry. For example, the construction of spin states along x direction as a superposition of spin states along z direction, can done by applying appropriate rotation transformation on the spin along z states which provides appropriate phase of the states relative to each other.

#### Application to include spin

An example of finite dimensional Hilbert space can be constructed using spin eigenkets of ${\textstyle s}$ -spin particles which forms a ${\textstyle 2s+1}$ dimensional Hilbert space. However, the general wavefunction of a particle that fully describes its state, is always from an infinite dimensional Hilbert space since it involves a tensor product with Hilbert space relating to the position or momentum of the particle. Nonetheless, the techniques developed for finite dimensional Hilbert space are useful since they can either be treated independently or treated in consideration of linearity of tensor product.

Since the spin operator for a given ${\textstyle s}$ -spin particles can be represented as a finite ${\textstyle (2s+1)^{2}}$ matrix which acts on ${\textstyle 2s+1}$ independent spin vector components, it is usually preferable to denote spin components using matrix/column/row notation as applicable.

For example, each |*sz*⟩ is usually identified as a column vector: $|s\rangle \leftrightarrow {\begin{bmatrix}1\\0\\\vdots \\0\\0\\\end{bmatrix}}\,,\quad |s-1\rangle \leftrightarrow {\begin{bmatrix}0\\1\\\vdots \\0\\0\\\end{bmatrix}}\,,\ldots \,,\quad |-(s-1)\rangle \leftrightarrow {\begin{bmatrix}0\\0\\\vdots \\1\\0\\\end{bmatrix}}\,,\quad |-s\rangle \leftrightarrow {\begin{bmatrix}0\\0\\\vdots \\0\\1\\\end{bmatrix}}$

but it is a common abuse of notation, because the kets |*sz*⟩ are not synonymous or equal to the column vectors. Column vectors simply provide a convenient way to express the spin components.

Corresponding to the notation, the z-component spin operator can be written as: ${\frac {1}{\hbar }}{\hat {S}}_{z}={\begin{bmatrix}s&0&\cdots &0&0\\0&s-1&\cdots &0&0\\\vdots &\vdots &\ddots &\vdots &\vdots \\0&0&\cdots &-(s-1)&0\\0&0&\cdots &0&-s\end{bmatrix}}$

since the eigenvectors of z-component spin operator are the above column vectors, with eigenvalues being the corresponding spin quantum numbers.

Corresponding to the notation, a vector from such a finite dimensional Hilbert space is hence represented as:

$|\phi \rangle ={\begin{bmatrix}\langle s|\phi \rangle \\\langle s-1|\phi \rangle \\\vdots \\\langle -(s-1)|\phi \rangle \\\langle -s|\phi \rangle \\\end{bmatrix}}={\begin{bmatrix}\varepsilon _{s}\\\varepsilon _{s-1}\\\vdots \\\varepsilon _{-s+1}\\\varepsilon _{-s}\\\end{bmatrix}}$ where ${\textstyle \{\varepsilon _{i}\}}$ are corresponding complex numbers.

In the following discussion involving spin, the complete wavefunction is considered as tensor product of spin states from finite dimensional Hilbert spaces and the wavefunction which was previously developed. The basis for this Hilbert space are hence considered: $|\mathbf {r} ,s_{z}\rangle =|\mathbf {r} \rangle |s_{z}\rangle$ .

### One-particle states in 3d position space

The position-space wave function of a single particle without spin in three spatial dimensions is similar to the case of one spatial dimension above: $\Psi (\mathbf {r} ,t)$ where **r** is the position vector in three-dimensional space, and *t* is time. As always Ψ(**r**, *t*) is a complex-valued function of real variables. As a single vector in Dirac notation $|\Psi (t)\rangle =\int d^{3}\!\mathbf {r} \,\Psi (\mathbf {r} ,t)\,|\mathbf {r} \rangle$

All the previous remarks on inner products, momentum space wave functions, Fourier transforms, and so on extend to higher dimensions.

For a particle with spin, ignoring the position degrees of freedom, the wave function is a function of spin only (time is a parameter); $\xi (s_{z},t)$ where *s*z is the spin projection quantum number along the z axis. (The z axis is an arbitrary choice; other axes can be used instead if the wave function is transformed appropriately, see below.) The *sz* parameter, unlike **r** and t, is a discrete variable. For example, for a spin-1/2 particle, *s*z can only be +1/2 or −1/2, and not any other value. (In general, for spin s, *sz* can be *s*, *s* − 1, ..., −*s* + 1, −*s*). Inserting each quantum number gives a complex valued function of space and time, there are 2*s* + 1 of them. These can be arranged into a column vector

$\xi ={\begin{bmatrix}\xi (s,t)\\\xi (s-1,t)\\\vdots \\\xi (-(s-1),t)\\\xi (-s,t)\\\end{bmatrix}}=\xi (s,t){\begin{bmatrix}1\\0\\\vdots \\0\\0\\\end{bmatrix}}+\xi (s-1,t){\begin{bmatrix}0\\1\\\vdots \\0\\0\\\end{bmatrix}}+\cdots +\xi (-(s-1),t){\begin{bmatrix}0\\0\\\vdots \\1\\0\\\end{bmatrix}}+\xi (-s,t){\begin{bmatrix}0\\0\\\vdots \\0\\1\\\end{bmatrix}}$

In bra–ket notation, these easily arrange into the components of a vector: $|\xi (t)\rangle =\sum _{s_{z}=-s}^{s}\xi (s_{z},t)\,|s_{z}\rangle$

The entire vector *ξ* is a solution of the Schrödinger equation (with a suitable Hamiltonian), which unfolds to a coupled system of 2*s* + 1 ordinary differential equations with solutions *ξ*(*s*, *t*), *ξ*(*s* − 1, *t*), ..., *ξ*(−*s*, *t*). The term "spin function" instead of "wave function" is used by some authors. This contrasts the solutions to position space wave functions, the position coordinates being continuous degrees of freedom, because then the Schrödinger equation does take the form of a wave equation.

More generally, for a particle in 3d with any spin, the wave function can be written in "position–spin space" as: $\Psi (\mathbf {r} ,s_{z},t)$ and these can also be arranged into a column vector $\Psi (\mathbf {r} ,t)={\begin{bmatrix}\Psi (\mathbf {r} ,s,t)\\\Psi (\mathbf {r} ,s-1,t)\\\vdots \\\Psi (\mathbf {r} ,-(s-1),t)\\\Psi (\mathbf {r} ,-s,t)\\\end{bmatrix}}$ in which the spin dependence is placed in indexing the entries, and the wave function is a complex vector-valued function of space and time only.

All values of the wave function, not only for discrete but continuous variables also, collect into a single vector $|\Psi (t)\rangle =\sum _{s_{z}}\int d^{3}\!\mathbf {r} \,\Psi (\mathbf {r} ,s_{z},t)\,|\mathbf {r} ,s_{z}\rangle$

For a single particle, the tensor product ⊗ of its position state vector |*ψ*⟩ and spin state vector |*ξ*⟩ gives the composite position-spin state vector $|\psi (t)\rangle \!\otimes \!|\xi (t)\rangle =\sum _{s_{z}}\int d^{3}\!\mathbf {r} \,\psi (\mathbf {r} ,t)\,\xi (s_{z},t)\,|\mathbf {r} \rangle \!\otimes \!|s_{z}\rangle$ with the identifications $|\Psi (t)\rangle =|\psi (t)\rangle \!\otimes \!|\xi (t)\rangle$ $\Psi (\mathbf {r} ,s_{z},t)=\psi (\mathbf {r} ,t)\,\xi (s_{z},t)$ $|\mathbf {r} ,s_{z}\rangle =|\mathbf {r} \rangle \!\otimes \!|s_{z}\rangle$

The tensor product factorization of energy eigenstates is always possible if the orbital and spin angular momenta of the particle are separable in the Hamiltonian operator underlying the system's dynamics (in other words, the Hamiltonian can be split into the sum of orbital and spin terms). The time dependence can be placed in either factor, and time evolution of each can be studied separately. Under such Hamiltonians, any tensor product state evolves into another tensor product state, which essentially means any unentangled state remains unentangled under time evolution. This is said to happen when there is no physical interaction between the states of the tensor products. In the case of non separable Hamiltonians, energy eigenstates are said to be some linear combination of such states, which need not be factorizable; examples include a particle in a magnetic field, and spin–orbit coupling.

The preceding discussion is not limited to spin as a discrete variable, the total angular momentum *J* may also be used. Other discrete degrees of freedom, like isospin, can expressed similarly to the case of spin above.

### Many-particle states in 3d position space

If there are many particles, in general there is only one wave function, not a separate wave function for each particle. The fact that *one* wave function describes *many* particles is what makes quantum entanglement and the EPR paradox possible. The position-space wave function for *N* particles is written: $\Psi (\mathbf {r} _{1},\mathbf {r} _{2}\cdots \mathbf {r} _{N},t)$ where **r***i* is the position of the i-th particle in three-dimensional space, and t is time. Altogether, this is a complex-valued function of 3*N* + 1 real variables.

In quantum mechanics there is a fundamental distinction between *identical particles* and *distinguishable* particles. For example, any two electrons are identical and fundamentally indistinguishable from each other; the laws of physics make it impossible to "stamp an identification number" on a certain electron to keep track of it. This translates to a requirement on the wave function for a system of identical particles: $\Psi \left(\ldots \mathbf {r} _{a},\ldots ,\mathbf {r} _{b},\ldots \right)=\pm \Psi \left(\ldots \mathbf {r} _{b},\ldots ,\mathbf {r} _{a},\ldots \right)$ where the + sign occurs if the particles are *all bosons* and − sign if they are *all fermions*. In other words, the wave function is either totally symmetric in the positions of bosons, or totally antisymmetric in the positions of fermions. The physical interchange of particles corresponds to mathematically switching arguments in the wave function. The antisymmetry feature of fermionic wave functions leads to the Pauli principle. Generally, bosonic and fermionic symmetry requirements are the manifestation of particle statistics and are present in other quantum state formalisms.

For *N* *distinguishable* particles (no two being identical, i.e. no two having the same set of quantum numbers), there is no requirement for the wave function to be either symmetric or antisymmetric.

For a collection of particles, some identical with coordinates **r**1, **r**2, ... and others distinguishable **x**1, **x**2, ... (not identical with each other, and not identical to the aforementioned identical particles), the wave function is symmetric or antisymmetric in the identical particle coordinates **r***i* only: $\Psi \left(\ldots \mathbf {r} _{a},\ldots ,\mathbf {r} _{b},\ldots ,\mathbf {x} _{1},\mathbf {x} _{2},\ldots \right)=\pm \Psi \left(\ldots \mathbf {r} _{b},\ldots ,\mathbf {r} _{a},\ldots ,\mathbf {x} _{1},\mathbf {x} _{2},\ldots \right)$

Again, there is no symmetry requirement for the distinguishable particle coordinates **x***i*.

The wave function for *N* particles each with spin is the complex-valued function $\Psi (\mathbf {r} _{1},\mathbf {r} _{2}\cdots \mathbf {r} _{N},s_{z\,1},s_{z\,2}\cdots s_{z\,N},t)$

Accumulating all these components into a single vector,

$|\Psi \rangle =\overbrace {\sum _{s_{z\,1},\ldots ,s_{z\,N}}} ^{\text{discrete labels}}\overbrace {\int _{R_{N}}d^{3}\mathbf {r} _{N}\cdots \int _{R_{1}}d^{3}\mathbf {r} _{1}} ^{\text{continuous labels}}\;\underbrace {{\Psi }(\mathbf {r} _{1},\ldots ,\mathbf {r} _{N},s_{z\,1},\ldots ,s_{z\,N})} _{\begin{array}{c}{\text{wave function (component of }}\\{\text{ state vector along basis state)}}\end{array}}\;\underbrace {|\mathbf {r} _{1},\ldots ,\mathbf {r} _{N},s_{z\,1},\ldots ,s_{z\,N}\rangle } _{\text{basis state (basis ket)}}\,.$

For identical particles, symmetry requirements apply to both position and spin arguments of the wave function so it has the overall correct symmetry.

The formulae for the inner products are integrals over all coordinates or momenta and sums over all spin quantum numbers. For the general case of *N* particles with spin in 3-d, $(\Psi _{1},\Psi _{2})=\sum _{s_{z\,N}}\cdots \sum _{s_{z\,2}}\sum _{s_{z\,1}}\int \limits _{\mathrm {all\,space} }d^{3}\mathbf {r} _{1}\int \limits _{\mathrm {all\,space} }d^{3}\mathbf {r} _{2}\cdots \int \limits _{\mathrm {all\,space} }d^{3}\mathbf {r} _{N}\Psi _{1}^{*}\left(\mathbf {r} _{1}\cdots \mathbf {r} _{N},s_{z\,1}\cdots s_{z\,N},t\right)\Psi _{2}\left(\mathbf {r} _{1}\cdots \mathbf {r} _{N},s_{z\,1}\cdots s_{z\,N},t\right)$ this is altogether N three-dimensional volume integrals and N sums over the spins. The differential volume elements *d*3**r***i* are also written "*dV**i*" or "*dxi dyi dzi*".

The multidimensional Fourier transforms of the position or position–spin space wave functions yields momentum or momentum–spin space wave functions.

#### Probability interpretation

For the general case of N particles with spin in 3d, if Ψ is interpreted as a probability amplitude, the probability density is $\rho \left(\mathbf {r} _{1}\cdots \mathbf {r} _{N},s_{z\,1}\cdots s_{z\,N},t\right)=\left|\Psi \left(\mathbf {r} _{1}\cdots \mathbf {r} _{N},s_{z\,1}\cdots s_{z\,N},t\right)\right|^{2}$

and the probability that particle 1 is in region *R*1 with spin *s**z*1 = *m*1 *and* particle 2 is in region *R*2 with spin *s**z*2 = *m*2 etc. at time *t* is the integral of the probability density over these regions and evaluated at these spin numbers:

$P_{\mathbf {r} _{1}\in R_{1},s_{z\,1}=m_{1},\ldots ,\mathbf {r} _{N}\in R_{N},s_{z\,N}=m_{N}}(t)=\int _{R_{1}}d^{3}\mathbf {r} _{1}\int _{R_{2}}d^{3}\mathbf {r} _{2}\cdots \int _{R_{N}}d^{3}\mathbf {r} _{N}\left|\Psi \left(\mathbf {r} _{1}\cdots \mathbf {r} _{N},m_{1}\cdots m_{N},t\right)\right|^{2}$

#### Physical significance of phase

In non-relativistic quantum mechanics, it can be shown using Schrodinger's time dependent wave equation that the equation:

${\frac {\partial \rho }{\partial t}}+\nabla \cdot \mathbf {J} =0$ is satisfied, where ${\textstyle \rho (\mathbf {x} ,t)=|\psi (\mathbf {x} ,t)|^{2}}$ is the probability density and ${\textstyle \mathbf {J} (\mathbf {x} ,t)={\frac {\hbar }{2im}}(\psi ^{*}\nabla \psi -\psi \nabla \psi ^{*})={\frac {\hbar }{m}}{\text{Im}}(\psi ^{*}\nabla \psi )}$ , is known as the probability flux in accordance with the continuity equation form of the above equation.

Using the following expression for wavefunction: $\psi (\mathbf {x} ,t)={\sqrt {\rho (\mathbf {x} ,t)}}\exp {\frac {iS(\mathbf {x} ,t)}{\hbar }}$ where ${\textstyle \rho (\mathbf {x} ,t)=|\psi (\mathbf {x} ,t)|^{2}}$ is the probability density and ${\textstyle S(\mathbf {x} ,t)}$ is the phase of the wavefunction, it can be shown that:

$\mathbf {J} (\mathbf {x} ,t)={\frac {\rho \nabla S}{m}}$

Hence the spacial variation of phase characterizes the probability flux.

In classical analogy, for ${\textstyle \mathbf {J} =\rho \mathbf {v} }$ , the quantity ${\textstyle {\frac {\nabla S}{m}}}$ is analogous with velocity. Note that this does not imply a literal interpretation of ${\textstyle {\frac {\nabla S}{m}}}$ as velocity since velocity and position cannot be simultaneously determined as per the uncertainty principle. Substituting the form of wavefunction in Schrodinger's time dependent wave equation, and taking the classical limit, ${\textstyle \hbar |\nabla ^{2}S|\ll |\nabla S|^{2}}$ :

${\frac {1}{2m}}|\nabla S(\mathbf {x} ,t)|^{2}+V(\mathbf {x} )+{\frac {\partial S}{\partial t}}=0$

Which is analogous to Hamilton-Jacobi equation from classical mechanics. This interpretation fits with Hamilton–Jacobi theory, in which ${\textstyle \mathbf {P} _{\text{class.}}=\nabla S}$ , where *S* is Hamilton's principal function.


## Time dependence

For systems in time-independent potentials, the wave function can always be written as a function of the degrees of freedom multiplied by a time-dependent phase factor, the form of which is given by the Schrödinger equation. For N particles, considering their positions only and suppressing other degrees of freedom, $\Psi (\mathbf {r} _{1},\mathbf {r} _{2},\ldots ,\mathbf {r} _{N},t)=e^{-iEt/\hbar }\,\psi (\mathbf {r} _{1},\mathbf {r} _{2},\ldots ,\mathbf {r} _{N})\,,$ where E is the energy eigenvalue of the system corresponding to the eigenstate Ψ. Wave functions of this form are called stationary states.

The time dependence of the quantum state and the operators can be placed according to unitary transformations on the operators and states. For any quantum state |Ψ⟩ and operator *O*, in the Schrödinger picture |Ψ(*t*)⟩ changes with time according to the Schrödinger equation while *O* is constant. In the Heisenberg picture it is the other way round, |Ψ⟩ is constant while *O*(*t*) evolves with time according to the Heisenberg equation of motion. The Dirac (or interaction) picture is intermediate, time dependence is places in both operators and states which evolve according to equations of motion. It is useful primarily in computing S-matrix elements.


## Non-relativistic examples

The following are solutions to the Schrödinger equation for one non-relativistic spinless particle.

### Finite potential barrier

One of the most prominent features of wave mechanics is the possibility for a particle to reach a location with a prohibitive (in classical mechanics) force potential. A common model is the "potential barrier", the one-dimensional case has the potential $V(x)={\begin{cases}V_{0}&|x|<a\\0&|x|\geq a\end{cases}}$ and the steady-state solutions to the wave equation have the form (for some constants *k*, *κ*) $\Psi (x)={\begin{cases}A_{\mathrm {r} }e^{ikx}+A_{\mathrm {l} }e^{-ikx}&x<-a,\\B_{\mathrm {r} }e^{\kappa x}+B_{\mathrm {l} }e^{-\kappa x}&|x|\leq a,\\C_{\mathrm {r} }e^{ikx}+C_{\mathrm {l} }e^{-ikx}&x>a.\end{cases}}$

Note that these wave functions are not normalized; see scattering theory for discussion.

The standard interpretation of this is as a stream of particles being fired at the step from the left (the direction of negative x): setting *A*r = 1 corresponds to firing particles singly; the terms containing *A*r and *C*r signify motion to the right, while *A*l and *C*l – to the left. Under this beam interpretation, put *C*l = 0 since no particles are coming from the right. By applying the continuity of wave functions and their derivatives at the boundaries, it is hence possible to determine the constants above.

In a semiconductor crystallite whose radius is smaller than the size of its exciton Bohr radius, the excitons are squeezed, leading to quantum confinement. The energy levels can then be modeled using the particle in a box model in which the energy of different states is dependent on the length of the box.

### Quantum harmonic oscillator

The wave functions for the quantum harmonic oscillator can be expressed in terms of Hermite polynomials *Hn*, they are $\Psi _{n}(x)={\sqrt {\frac {1}{2^{n}\,n!}}}\cdot \left({\frac {m\omega }{\pi \hbar }}\right)^{1/4}\cdot e^{-{\frac {m\omega x^{2}}{2\hbar }}}\cdot H_{n}{\left({\sqrt {\frac {m\omega }{\hbar }}}x\right)}$ where *n* = 0, 1, 2, ....

### Hydrogen atom

The wave functions of an electron in a Hydrogen atom are expressed in terms of spherical harmonics and generalized Laguerre polynomials (these are defined differently by different authors—see main article on them and the hydrogen atom).

It is convenient to use spherical coordinates, and the wave function can be separated into functions of each coordinate, $\Psi _{n\ell m}(r,\theta ,\phi )=R(r)\,\,Y_{\ell }^{m}\!(\theta ,\phi )$ where *R* are radial functions and *Y**m* *ℓ*(*θ*, *φ*) are spherical harmonics of degree *ℓ* and order *m*. This is the only atom for which the Schrödinger equation has been solved exactly. Multi-electron atoms require approximative methods. The family of solutions is: $\Psi _{n\ell m}(r,\theta ,\phi )={\sqrt {{\left({\frac {2}{na_{0}}}\right)}^{3}{\frac {(n-\ell -1)!}{2n[(n+\ell )!]}}}}e^{-r/na_{0}}\left({\frac {2r}{na_{0}}}\right)^{\ell }L_{n-\ell -1}^{2\ell +1}\left({\frac {2r}{na_{0}}}\right)\cdot Y_{\ell }^{m}(\theta ,\phi )$ where *a*0 = 4*πε*0*ħ*2/*mee*2 is the Bohr radius, *L*2*ℓ* + 1 *n* − *ℓ* − 1 are the generalized Laguerre polynomials of degree *n* − *ℓ* − 1, *n* = 1, 2, ... is the principal quantum number, *ℓ* = 0, 1, ..., *n* − 1 the azimuthal quantum number, *m* = −*ℓ*, −*ℓ* + 1, ..., *ℓ* − 1, *ℓ* the magnetic quantum number. Hydrogen-like atoms have very similar solutions.

This solution does not take into account the spin of the electron.

In the figure of the hydrogen orbitals, the 19 sub-images are images of wave functions in position space (their norm squared). The wave functions represent the abstract state characterized by the triple of quantum numbers (*n*, *ℓ*, *m*), in the lower right of each image. These are the principal quantum number, the orbital angular momentum quantum number, and the magnetic quantum number. Together with one spin-projection quantum number of the electron, this is a complete set of observables.

The figure can serve to illustrate some further properties of the function spaces of wave functions.

- In this case, the wave functions are square integrable. One can initially take the function space as the space of square integrable functions, usually denoted *L*2.
- The displayed functions are solutions to the Schrödinger equation. Obviously, not every function in *L*2 satisfies the Schrödinger equation for the hydrogen atom. The function space is thus a subspace of *L*2.
- The displayed functions form part of a basis for the function space. To each triple (*n*, *ℓ*, *m*), there corresponds a basis wave function. If spin is taken into account, there are two basis functions for each triple. The function space thus has a countable basis.
- The basis functions are mutually orthonormal.
